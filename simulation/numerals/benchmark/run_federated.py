#!/usr/bin/env python3
"""The federated benchmark — offline (oracle) mode.

Four arms decide the 3,000-case enterprise stream in which five divisions file
changes against one constitution and one shared store:

  A       the monolith: constitution and case, no record, no memory
  B_mem   the gated survivors shown as advice, without normative force
  B_div   the judiciary with a DIVISION-LOCAL store: records bind, but a
          division sees only what its own contests wrote — the un-federated
          comparator, i.e. five judiciaries that do not talk to each other
  B       the federated judiciary: one enterprise store, foreign records bind,
          home records win on scope

Endpoints, in order: cross-division like-case consistency (disposition AND
citation; oracle-free); agreement with the reference on the C-cross stratum
(cases the reference binds to another division's record — the stratum only
federation can decide); floors; no-call fraction and cost. Oracle mode is a
perfect reader of what each arm is shown: an upper bound on the arm, never a
prediction about a model. `--mode live` is what produces a claim.

    python3 benchmark/run_federated.py [--mode oracle|dry] [--models sonnet]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

def _portable_config(a):
    """argparse namespace as a dict, with filesystem paths made relative to the pack.

    Result files are shipped; they must not carry the build machine's directory layout."""
    cfg = dict(vars(a))
    for k, v in list(cfg.items()):
        if isinstance(v, str) and os.path.isabs(v):
            try:
                cfg[k] = os.path.relpath(v, os.path.dirname(HERE))
            except ValueError:
                pass
    return cfg

ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import engine  # noqa: E402
import federation as F  # noqa: E402
import arms as armsmod  # noqa: E402
import judge as judgemod  # noqa: E402
import config  # noqa: E402

ARMS = {
    "A": config.ARMS["A"],
    "B_mem": config.ARMS["B_mem"],
    "B_div": {**config.ARMS["B"], "label": "Digital Judiciary, division-local store — records bind, nothing is shared", "division_local": True},
    "B": {**config.ARMS["B"], "label": "Digital Judiciary, federated — one enterprise store, foreign records bind, home records win on scope"},
}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("oracle", "dry"), default="oracle")
    ap.add_argument("--models", default="sonnet")
    ap.add_argument("--arms", default="A,B_mem,B_div,B")
    ap.add_argument("--out", default=os.path.join(HERE, "results"))
    a = ap.parse_args(argv)

    rb = json.load(open(os.path.join(ROOT, "constitution", "rulebook.json")))
    params = json.load(open(os.path.join(ROOT, "constitution", "parameters.json")))
    pack = json.load(open(os.path.join(ROOT, "corpus", "cases.json")))
    seed = json.load(open(os.path.join(ROOT, "corpus", "store_seed_initial.json")))
    engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))
    provisions = {p["id"]: engine.Provision.from_dict(p) for p in rb["provisions"]}
    theta = params["theta"]
    stream = pack["cases"]
    ref = F.replay(stream, seed["records"], seed["record_division"], provisions, theta)
    ref_traces = {t["case"]: t for t in ref["traces"]}
    cross_ids = {c["id"] for c in stream if c["category"] == "C-cross"}
    pairs = pack["like_case_pairs"]

    results = []
    for model in [config.ALIASES.get(m.strip(), m.strip()) for m in a.models.split(",")]:
        for arm_name in [x.strip() for x in a.arms.split(",")]:
            arm = ARMS[arm_name]
            j = judgemod.Judge(model, mode=a.mode)
            store = [engine.Record.from_dict(r) for r in seed["records"]]
            rec_div = dict(seed["record_division"])
            answers, no_call, total = {}, 0, 0
            for case in stream:
                d = case["division"]
                if arm.get("division_local"):
                    view = [r for r in store if rec_div.get(r.id) == d]
                elif arm["binds"] or arm["store_view"] != "none":
                    view = F.view_for(d, store, rec_div)
                else:
                    view = []
                ans, called = armsmod.decide(arm_name, arm, case, view, provisions, theta, j, rb)
                total += 1; no_call += (0 if called else 1)
                if ans is not None:
                    answers[case["id"]] = ans
                t = ref_traces[case["id"]]
                if t.get("admitted"):
                    rec = engine._record_from(engine.case_from_dict(case), t, provisions)
                    store.append(rec); rec_div[rec.id] = d
            # ---- endpoints -------------------------------------------------
            agree = disagree = 0
            for p in pairs:
                x, y = answers.get(p["a"]), answers.get(p["b"])
                if not x or not y:
                    continue
                if x["disposition"] == y["disposition"] and x.get("controlling") == y.get("controlling"):
                    agree += 1
                else:
                    disagree += 1
            cross_ok = sum(1 for cid in cross_ids if answers.get(cid) and answers[cid]["disposition"] == ref_traces[cid]["decision"])
            cross_cite = sum(1 for cid in cross_ids if answers.get(cid) and answers[cid].get("controlling") == ref_traces[cid]["controlling"])
            floors = [c for c in stream if ref_traces[c["id"]]["route"] == engine.ROUTE_ABSOLUTE]
            floor_ok = sum(1 for c in floors if answers.get(c["id"]) and answers[c["id"]]["disposition"] == engine.DENY)
            foreign_bound = sum(1 for c in stream if answers.get(c["id"]) and answers[c["id"]].get("controlling")
                                and rec_div.get(answers[c["id"]]["controlling"]) not in (None, c["division"]))
            u = j.usage
            row = {"arm": arm_name, "model": model, "label": arm["label"],
                   "cross_division_consistency": {"pairs": agree + disagree, "consistent": agree,
                                                   "rate": agree / (agree + disagree) if (agree + disagree) else None},
                   "c_cross_stratum": {"cases": len(cross_ids), "disposition_agrees_with_reference": cross_ok,
                                       "cites_the_foreign_record": cross_cite},
                   "floors": {"cases": len(floors), "upheld": floor_ok},
                   "answers_citing_a_foreign_division_record": foreign_bound,
                   "no_call_fraction": no_call / total if total else 0.0,
                   "usage": u.as_dict(model) if a.mode != "dry" else u.as_dict(model)}
            results.append(row)
            print(f"  {model:18} {arm_name:6} pairs {agree:>3}/{agree + disagree:<3}  "
                  f"C-cross disp {cross_ok:>3}/{len(cross_ids)} cite {cross_cite:>3}  "
                  f"floors {floor_ok}/{len(floors)}  foreign-cited {foreign_bound:>4}  "
                  f"no-call {100 * no_call / total:5.1f}%  ${u.cost(model):>8,.2f}")
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, f"federated-{a.mode}.json")
    json.dump({"config": _portable_config(a), "stream": len(stream), "results": results,
               "note": ("oracle mode is a perfect reader of what each arm was shown — an upper bound on the arm, "
                        "not a prediction about any model")}, open(path, "w"), indent=2)
    print(f"\nresults: {path}")
    print("pairs      = cross-division like-case pairs agreeing on disposition AND citation (oracle-free)")
    print("C-cross    = the stratum the reference binds to ANOTHER division's record; disp = disposition agrees,")
    print("             cite = the arm names that foreign record. Only a federated store can do the second.")
    print("foreign-cited = answers across the whole stream that cite a record another division wrote")
    return 0


if __name__ == "__main__":
    sys.exit(main())
