#!/usr/bin/env python3
"""Publish a run's results, and compare a live model against the oracle.

    python3 demo/publish_run.py --db /tmp/dj-live.db --label "sonnet, ladder"
    python3 demo/publish_run.py --compare runs/oracle.json runs/sonnet.json

=== What "gold standard" means here, and what it does not ===

The oracle is the premise-subset rule:

    distinguished  ==  premise(candidate) - facts(case)  !=  {}

It is the paper's own definition of distinguishing, executed. So it cannot be
wrong about that definition — which makes it a fixed, reproducible reference
point, and NOT a measure of good judgement. A model that disagrees with the
oracle has departed from the formal definition; whether the departure was
right is a question this tool cannot answer and does not try to.

Read the output as "how far does this model's behaviour sit from the formal
rule", never as "how accurate is this model".

=== Why per-verdict and not just per-case ===

Two runs can reach the same disposition for different reasons: a model may
distinguish the wrong precedent and still land on the same outcome because
another candidate happened to control. Comparing only dispositions would
score that as agreement. This compares the verdicts themselves, then reports
disposition agreement separately, and the gap between the two numbers is
itself informative — it is how often a wrong verdict was masked by the
ordering.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RUNS = os.path.join(ROOT, "runs")
sys.path.insert(0, ROOT)


def extract(db_path: str, label: str) -> dict:
    """Everything needed to compare this run, keyed so runs line up.

    Verdicts are keyed by (case_hash, candidate_hash, tier): the same question
    asked of the same pair at the same rung. That key is stable across runs
    because it is derived from content, not from row ids — two runs of the
    same corpus produce different record ids but identical question keys.
    """
    from app import db as dbmod

    os.environ["DJ_DB"] = db_path
    r = dbmod.open_reader(db_path)

    # The candidate's PREMISE, not its record id. A precedent written during
    # a live run gets a different id and content_hash than the equivalent one
    # from an oracle run, so keying on identity finds zero overlap the moment
    # the two ledgers diverge — which is exactly when you most want to
    # compare them. The distinguishing question is "does this premise hold
    # against these facts", and that is what the key has to name.
    premise_of = {}
    for row in r.execute(
            "SELECT content_hash, premise, provision_id"
            " FROM precedent_record").fetchall():
        premise_of[row["content_hash"]] = (
            f"{row['provision_id']}:"
            f"{','.join(sorted(json.loads(row['premise'])))}")

    verdicts, judges = {}, {}
    for row in r.execute(
            "SELECT case_hash, candidate_hash, tier, judge_version, verdict,"
            " degraded, from_cache, latency_ms, input_tokens, output_tokens"
            " FROM judgment_invocation WHERE kind='distinguish'").fetchall():
        v = json.loads(row["verdict"])
        cand = premise_of.get(row["candidate_hash"], row["candidate_hash"])
        key = f"{row['case_hash']}|{cand}|{row['tier']}"
        # A cache hit is the same verdict re-served; keep the first.
        verdicts.setdefault(key, {
            "distinguished": bool(v.get("distinguished")),
            "grounds": (v.get("grounds") or "")[:200],
            "tier": row["tier"], "degraded": bool(row["degraded"]),
            "judge": row["judge_version"],
            "latency_ms": row["latency_ms"] or 0,
            "in": row["input_tokens"] or 0, "out": row["output_tokens"] or 0,
        })
        judges[row["judge_version"]] = judges.get(row["judge_version"], 0) + 1

    # Keyed by repo#number: head_sha is derived from the scenario id via
    # hash(), which Python randomises per process, so it is not stable across
    # runs. The pull request a scenario represents is.
    dispositions = {}
    for row in r.execute(
            "SELECT s.repo, s.pr_number, c.disposition"
            " FROM pr_session s JOIN pr_session_current c"
            "   ON c.session_id = s.session_id").fetchall():
        dispositions[f"{row['repo']}#{row['pr_number']}"] = row["disposition"]

    paid = [v for v in verdicts.values() if not v["degraded"]]
    return {
        "label": label,
        "captured_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "db": db_path,
        "judges": judges,
        "mode": ("oracle" if all(j.startswith("oracle") for j in judges)
                 else "live"),
        "counts": {
            "verdicts": len(verdicts),
            "dispositions": len(dispositions),
            "degraded": sum(1 for v in verdicts.values() if v["degraded"]),
            "tokens_in": sum(v["in"] for v in verdicts.values()),
            "tokens_out": sum(v["out"] for v in verdicts.values()),
            "mean_latency_ms": (round(sum(v["latency_ms"] for v in paid)
                                      / len(paid)) if paid else 0),
        },
        "verdicts": verdicts,
        "dispositions": dispositions,
    }


def compare(gold: dict, run: dict) -> dict:
    """Verdict-level and disposition-level agreement, plus every disagreement.

    Disagreements are listed rather than counted. A rate tells you something
    is wrong; the list is what lets you find out what.
    """
    shared = set(gold["verdicts"]) & set(run["verdicts"])
    agree, disagree = 0, []
    by_tier: dict = {}
    for k in shared:
        g, x = gold["verdicts"][k], run["verdicts"][k]
        t = g["tier"]
        by_tier.setdefault(t, {"n": 0, "agree": 0})
        by_tier[t]["n"] += 1
        if g["distinguished"] == x["distinguished"]:
            agree += 1
            by_tier[t]["agree"] += 1
        else:
            case_h, cand_h, _ = k.split("|")
            disagree.append({
                "case": case_h[:10], "candidate": cand_h[:10], "tier": t,
                # Named from the ORACLE's point of view, because the oracle is
                # the definition. "over-distinguished" = the model set aside a
                # precedent the rule says applies, which is the direction that
                # loses precedent and re-litigates settled matters.
                "direction": ("over-distinguished" if x["distinguished"]
                              else "under-distinguished"),
                "model_said": x["grounds"][:120],
            })

    d_shared = set(gold["dispositions"]) & set(run["dispositions"])
    d_agree = sum(1 for h in d_shared
                  if gold["dispositions"][h] == run["dispositions"][h])
    d_diff = [{"change": h[:10], "gold": gold["dispositions"][h],
               "run": run["dispositions"][h]}
              for h in d_shared if gold["dispositions"][h]
              != run["dispositions"][h]]

    def rate(k, n):
        return {"k": k, "n": n, "rate": round(k / n, 4) if n else None}

    over = sum(1 for d in disagree if d["direction"] == "over-distinguished")
    return {
        "gold": gold["label"], "run": run["label"],
        "verdict_agreement": rate(agree, len(shared)),
        "disposition_agreement": rate(d_agree, len(d_shared)),
        "over_distinguished": over,
        "under_distinguished": len(disagree) - over,
        "by_tier": {str(t): rate(v["agree"], v["n"])
                    for t, v in sorted(by_tier.items())},
        "degraded_in_run": run["counts"]["degraded"],
        "disagreements": disagree[:40],
        "disposition_differences": d_diff[:40],
        "unmatched": {
            "questions_only_in_gold": len(set(gold["verdicts"]) - shared),
            "questions_only_in_run": len(set(run["verdicts"]) - shared),
        },
    }


def report(c: dict) -> None:
    va, da = c["verdict_agreement"], c["disposition_agreement"]
    print(f"\n  {c['run']}  vs  {c['gold']} (the formal rule)\n")
    print(f"    verdict agreement      {va['rate']}   "
          f"({va['k']}/{va['n']} distinguishing questions)")
    print(f"    disposition agreement  {da['rate']}   "
          f"({da['k']}/{da['n']} changes)")
    print(f"\n    departed by setting a precedent aside that the rule keeps:"
          f" {c['over_distinguished']}")
    print(f"    departed by keeping one the rule sets aside:               "
          f" {c['under_distinguished']}")
    if c["degraded_in_run"]:
        print(f"\n    WARNING: {c['degraded_in_run']} verdict(s) degraded —"
              f" a call failed and fell back.")
        print("    Those are not model judgements and this comparison is"
              " not clean.")
    if c["by_tier"]:
        print("\n    by tier:")
        for t, r in c["by_tier"].items():
            print(f"      tier {t}: {r['rate']}  ({r['k']}/{r['n']})")
    if c["disagreements"]:
        print("\n    first disagreements:")
        for d in c["disagreements"][:5]:
            print(f"      {d['case']} vs {d['candidate']} (tier {d['tier']})"
                  f" — {d['direction']}")
            if d["model_said"]:
                print(f"        model: {d['model_said'][:96]}")
    u = c["unmatched"]
    if u["questions_only_in_gold"] or u["questions_only_in_run"]:
        print(f"\n    note: {u['questions_only_in_gold']} question(s) only in"
              f" the gold run, {u['questions_only_in_run']} only in this one.")
        print("    The runs saw different ledgers — compare runs seeded from"
              " the same corpus.")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Publish a run for analysis, or compare one against the"
                    " oracle baseline.")
    ap.add_argument("--db", default=os.environ.get("DJ_DB", "/tmp/dj.db"))
    ap.add_argument("--label", default=None,
                    help="how this run should be named in the output")
    ap.add_argument("--out", default=None, help="where to write the JSON")
    ap.add_argument("--compare", nargs=2, metavar=("GOLD", "RUN"),
                    help="compare two published runs")
    ap.add_argument("--list", action="store_true",
                    help="list published runs")
    a = ap.parse_args()

    os.makedirs(RUNS, exist_ok=True)

    if a.list:
        for f in sorted(os.listdir(RUNS)):
            if f.endswith(".json"):
                d = json.load(open(os.path.join(RUNS, f)))
                if "verdicts" in d:
                    print(f"  {f:34s} {d['mode']:7s}"
                          f" {d['counts']['verdicts']:5d} verdicts"
                          f"  {', '.join(d['judges'])}")
        return 0

    if a.compare:
        gold = json.load(open(a.compare[0]))
        run = json.load(open(a.compare[1]))
        if gold["mode"] != "oracle":
            print("  NOTE: the first argument is not an oracle run. Comparing"
                  " two live runs\n  tells you how far they sit from each"
                  " other, not from the formal rule.\n")
        c = compare(gold, run)
        report(c)
        out = os.path.join(RUNS, f"compare-{int(time.time())}.json")
        json.dump(c, open(out, "w"), indent=1)
        print(f"  written {out}\n")
        return 0

    if not os.path.exists(a.db):
        print(f"  no database at {a.db}", file=sys.stderr)
        return 2
    label = a.label or os.path.basename(a.db)
    d = extract(a.db, label)
    name = a.out or os.path.join(
        RUNS, f"{d['mode']}-{time.strftime('%Y%m%d-%H%M%S')}.json")
    json.dump(d, open(name, "w"), indent=1)
    print(f"\n  published {name}")
    print(f"    mode        {d['mode']}")
    print(f"    judges      {', '.join(d['judges']) or 'none'}")
    print(f"    verdicts    {d['counts']['verdicts']}"
          f"  ({d['counts']['degraded']} degraded)")
    print(f"    changes     {d['counts']['dispositions']}")
    if d["counts"]["tokens_in"]:
        print(f"    tokens      {d['counts']['tokens_in']} in,"
              f" {d['counts']['tokens_out']} out")
        print(f"    latency     {d['counts']['mean_latency_ms']} ms mean")
    print("\n  compare against an oracle run:")
    print(f"    python3 demo/publish_run.py --compare runs/oracle-*.json"
          f" {name}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
