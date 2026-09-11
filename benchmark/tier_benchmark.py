#!/usr/bin/env python3
"""Paper 3 benchmark harness — now running on the deployed framework.

    python3 tier_benchmark.py --company all --condition rules_only
    python3 tier_benchmark.py --company all --condition b_mem
    python3 tier_benchmark.py --company all                     # dj (default)
    python3 tier_benchmark.py --company all --tiered            # model ladder

Add --mock to validate the whole pipeline offline with no API key and no
network. Mock output is written with `"mock": true` in every summary and a
banner on the dashboard, because a mock number that escapes into a paper is
the single worst failure mode this harness has.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

COMPANY_DIR = os.path.join(HERE, "companies")
CONDITIONS = ("rules_only", "b_mem", "dj")
TIERS = ("haiku", "sonnet", "opus")

FIELDS = ["case_id", "class", "condition", "gold_disposition", "disposition",
          "gold_outcome", "outcome", "tier", "controlling_state",
          "controlling_id", "consulted", "cited_records", "relied_on_lapsed",
          "memory_had_lapsed", "not_reached", "lanes", "control_plane",
          "self_asserted", "degraded", "factors", "provisions",
          "input_tokens", "output_tokens", "latency_ms", "rationale",
          "session_id", "review_tasks", "review_outcome", "renewal_barred"]


def companies() -> list[str]:
    return sorted(d for d in os.listdir(COMPANY_DIR)
                  if os.path.isdir(os.path.join(COMPANY_DIR, d)))


def load_company(name: str) -> tuple[dict, list[dict]]:
    base = os.path.join(COMPANY_DIR, name)
    with open(os.path.join(base, "company.json")) as fh:
        cfg = json.load(fh)
    cases = []
    with open(os.path.join(base, "corpus.jsonl")) as fh:
        for line in fh:
            line = line.strip()
            if line:
                cases.append(json.loads(line))
    for key in ("rulebook", "store_seed", "factor_map"):
        if cfg.get(key):
            cfg[key + "_path"] = os.path.normpath(os.path.join(base, cfg[key]))
    return cfg, cases


def suffix(condition: str, model: str, tiered: bool) -> str:
    s = "" if condition == "dj" else f"_{condition}"
    if tiered:
        s += f"_{model}"
    return s


def run_one(company: str, condition: str, model: str, args) -> dict:
    from harness import DJInstance, run_case
    import models as modelmod
    import scoring

    ladder = ([x.strip() for x in args.ladder.split(",") if x.strip()]
              if (args.ladder and condition == "dj") else None)
    cfg, cases = load_company(company)
    if args.limit:
        cases = cases[:args.limit]

    workdir = tempfile.mkdtemp(prefix=f"dj-bench-{company}-")
    judge_mode = "llm" if (condition == "dj" and not args.mock) else "oracle"
    client = (None if condition == "dj"
              else modelmod.build_model(condition, model, args.mock))

    rows = []
    dj = None
    try:
        if args.isolation == "run":
            dj = DJInstance(os.path.join(workdir, "run.db"), judge_mode,
                            modelmod.resolve_model(model),
                            cfg.get("factor_map_path"),
                            ladder=ladder, premise_mode=args.premise)
        for i, case in enumerate(cases):
            if args.isolation == "case":
                dj = DJInstance(os.path.join(workdir, f"c{i}.db"), judge_mode,
                                modelmod.resolve_model(model),
                                cfg.get("factor_map_path"),
                                ladder=ladder, premise_mode=args.premise)
            row = run_case(condition, dj, client, case, args.escalate,
                           args.human)
            rows.append(row)
            if not args.quiet:
                mark = "ok " if row["disposition"] == row["gold_disposition"] \
                    else "DIFF"
                print(f"  [{mark}] {row['case_id']:8s} {row['class']:16s}"
                      f" {row['disposition']:24s}"
                      f" (gold {row['gold_disposition']})")
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    meta = {
        "company": company, "condition": condition,
        "model": f"mock:{model}" if args.mock
                 else modelmod.resolve_model(model),
        "judge_position_model": (modelmod.resolve_model(model)
                                 if condition == "dj" and not args.mock
                                 else None),
        "mock": bool(args.mock),
        "isolation": args.isolation,
        "escalation": args.escalate,
        "human_review_policy": args.human,
        "tier_ladder": ladder,
        "premise_mode": args.premise,
        "gold_source": cfg.get("gold_source"),
        "gold_note": cfg.get("gold_note"),
        "framework": "digital-judiciary single-container v3.1-hardened + L5 interfaces",
        "run_at": datetime.now(timezone.utc).isoformat(),
    }
    summary = scoring.summarize(rows, meta)
    pricing = load_pricing(args.pricing)
    summary["cost"] = scoring.cost(summary, pricing)

    sfx = suffix(condition, model, args.tiered)
    with open(f"results_{company}{sfx}.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    with open(f"summary_{company}{sfx}.json", "w") as fh:
        json.dump(summary, fh, indent=2)
    print(f"  wrote results_{company}{sfx}.csv and"
          f" summary_{company}{sfx}.json")
    return summary


def load_pricing(path: str | None) -> dict | None:
    p = path or os.path.join(HERE, "pricing.json")
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        data = json.load(fh)
    return data if data.get("snapshot_date") else None


# ---------------------------------------------------------------------------
def dashboard(summaries: list[dict], path: str = "dashboard.html") -> None:
    from report import render
    with open(path, "w") as fh:
        fh.write(render(summaries))
    print(f"  wrote {path}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--company", default="all",
                    help="company key, or 'all'")
    ap.add_argument("--condition", default="dj", choices=CONDITIONS,
                    help="rules_only | b_mem | dj (default dj)")
    ap.add_argument("--model", default="sonnet",
                    help="haiku|sonnet|opus or a full model id")
    ap.add_argument("--tiered", action="store_true",
                    help="sweep the model ladder for the cost/accuracy frontier")
    ap.add_argument("--mock", action="store_true",
                    help="deterministic offline run; results are pipeline "
                         "checks, not findings")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--escalate", default="manual", choices=("manual", "auto"),
                    help="manual keeps Corollary 2 semantics (a challenge is "
                         "an act); auto walks the ladder on every denial")
    ap.add_argument("--ladder", default=None,
                    help="per-tier judge models for the dj condition, e.g. "
                         "'haiku,sonnet,opus'. Configures the CONTAINER's "
                         "tier judges; --tiered by contrast sweeps one model "
                         "at all tiers and is for the baselines")
    ap.add_argument("--premise", default="mechanical",
                    choices=("mechanical", "judged"),
                    help="mechanical records every case fact as the holding's "
                         "premise; judged asks the model which were material")
    ap.add_argument("--human", default="leave",
                    choices=("leave", "accept", "decline"),
                    help="standing policy for the human-review lane. leave "
                         "(default) leaves the task open, which is a real "
                         "state, not a gap. accept/decline close the lane "
                         "through the same risk_decision path the screen "
                         "uses, and are a STAND-IN for a person, never a "
                         "measurement of one")
    ap.add_argument("--isolation", default="run", choices=("run", "case"),
                    help="run: precedent accumulates across the corpus, as in "
                         "production. case: a fresh seeded store per case")
    ap.add_argument("--pricing", default=None)
    ap.add_argument("--no-ui", dest="ui", action="store_false",
                    help="skip the dashboard")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    targets = companies() if args.company == "all" else [args.company]
    for t in targets:
        if not os.path.isdir(os.path.join(COMPANY_DIR, t)):
            print(f"unknown company '{t}'; have: {', '.join(companies())}")
            return 2

    model_list = list(TIERS) if args.tiered else [args.model]
    summaries = []
    for company in targets:
        for model in model_list:
            print(f"\n{company} / {args.condition} / {model}"
                  + ("  [MOCK]" if args.mock else ""))
            summaries.append(run_one(company, args.condition, model, args))

    print("\n" + "=" * 78)
    for s in summaries:
        a = s["disposition_agreement"]
        label = (",".join(s["meta"]["tier_ladder"])
                 if s["meta"].get("tier_ladder") else str(s["meta"]["model"]))
        print(f"{s['meta']['company']:20s} {s['meta']['condition']:11s}"
              f" {label[:22]:24s}"
              f" agreement {a['rate']} {a['ci95']}")
    print("=" * 78)
    if any(s["meta"]["mock"] for s in summaries):
        print("MOCK RUN — these numbers validate the pipeline. They are not"
              " findings and must not be cited.")
    if any(s["meta"]["condition"] == "dj" and s["meta"]["mock"]
           for s in summaries):
        print("Note: a mock DJ run puts the deterministic premise-subset"
              " oracle at the judge position, so it measures the MECHANISM"
              " and cannot be wrong about its own definition. Near-perfect"
              " agreement here is expected and means nothing about judgment"
              " quality. Drop --mock to measure a real model at that"
              " position.")

    if args.ui:
        dashboard(summaries)
    return 0


if __name__ == "__main__":
    sys.exit(main())
