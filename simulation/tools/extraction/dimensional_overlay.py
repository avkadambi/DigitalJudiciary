#!/usr/bin/env python3
"""The dimensional kernel on a magnitude overlay — the tolerance sweep, at last.

    python3 tools/extraction/dimensional_overlay.py <pack-dir> [--k 8 | --factor F1,F2] [--tolerances 0,2,5,10,20,40] [--brief]

No pack carries a magnitude factor, so this script makes some: it takes the k
compliant, non-absolute boolean factors that appear in the most record
premises, reads each one's boolean meaning as a threshold ("present" = at or
above 80 on a 0-100 index, "absent" = below), and gives every case and every
record a synthetic value consistent with that reading — present 80-100,
absent 40-79, deterministic in the case id and factor. The factors are then
declared as dimensions (weaker when lower) in the engine's namespace and the
corpus is replayed at each tolerance. Because present values span 80-100, a
tolerance of 20 is the point at which no boolean bind is lost to exactness;
and because a record can sit right at the threshold, any tolerance above zero
can already bind a case the boolean reading calls absent. Both costs are
reported, and the binding gate scores the second against the boolean trace.

What is measured, all ⟦synthetic overlay⟧:

  * admissions by status (a_fortiori / tolerant / distinguished / premise_unproven)
    at each tolerance — the regime the closed-world corpora cannot reach;
  * binds against the BOOLEAN reference: kept, lost (a case at 82 no longer
    binds a record at 90 at tolerance 0 — the price of exactness), and gained
    (a case at 74 binds a record at 90 at tolerance 20 — a bind the boolean
    reading calls false), scored through the binding gate with the boolean
    trace as oracle;
  * the gate-margin distribution on the dimension: how many discards turned
    on this one factor, which is the quantity the Likewise falsifier names;
  * the magnitude round-trip: the value rendered into the rationale and read
    back by the cued reader, with unreadable values left unrecorded.

The overlay is not a corpus change and nothing here writes to the pack.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extraction import records as R  # noqa: E402
from extraction import snapshot  # noqa: E402

THRESHOLD = 80.0


def _h(*p):
    return int(hashlib.sha256("\x1f".join(str(x) for x in p).encode()).hexdigest(), 16)


def value_for(key: str, present: bool) -> float:
    return float(THRESHOLD + _h(key, "v") % 21) if present else float(40 + _h(key, "v") % 40)


def pick_factors(rb: dict, seed: list, written: list, k: int) -> list:
    """The k compliant, non-absolute factors that appear in the most record premises."""
    comply = {f for p in rb["provisions"] for f in p["factors"]["comply"] if not p["absolute"]}
    cnt = collections.Counter(f for r in seed + written for f in r["premise"] if f in comply)
    return [f for f, _ in cnt.most_common(k)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("--factor", default=None, help="comma-separated factors to overlay; default: the k most-premised")
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--tolerances", default="0,2,5,10,20,40")
    ap.add_argument("--out", default=None)
    ap.add_argument("--brief", action="store_true")
    a = ap.parse_args(argv)

    engine, rb, params, cases, seed, provisions = snapshot.load_pack(a.pack)
    pack_name = os.path.basename(os.path.abspath(a.pack))
    boolean = engine.replay(cases, seed, provisions, params["theta"])
    factors = a.factor.split(",") if a.factor else pick_factors(rb, seed, [r.to_dict() for r in boolean["records_written"]], a.k)
    tols = [float(t) for t in a.tolerances.split(",")]

    # overlay: values on cases and seed records, consistent with the boolean reading
    ov_cases = []
    for c in cases:
        d = dict(c)
        d["values"] = {f: value_for(c["id"] + f, f in c["facts"]) for f in factors}
        ov_cases.append(d)
    ov_seed = []
    for r in seed:
        d = json.loads(json.dumps(r))
        d["values"] = {f: value_for(r["id"] + f, True) for f in factors if f in r["premise"]}
        ov_seed.append(d)

    import importlib.util
    spec = importlib.util.spec_from_file_location("dj_pack_binding_gate",
                                                  os.path.join(os.path.abspath(a.pack), "harness", "binding_gate.py"))
    BG = importlib.util.module_from_spec(spec)
    sys.modules["dj_pack_binding_gate"] = BG
    spec.loader.exec_module(BG)  # the pack's own copy of the binding gate
    b_traces = {t["case"]: t for t in boolean["traces"]}
    results = []
    for tol in tols:
        engine.DIMENSIONS.clear()
        for f in factors:
            engine.DIMENSIONS[f] = {"weaker_when": "lower", "tolerance": tol, "unit": "index"}
        run = engine.replay(ov_cases, ov_seed, provisions, params["theta"])
        st = collections.Counter()
        kept = lost = gained = gained_abst = 0
        oracle, answers = [], {}
        for t in run["traces"]:
            for s in t["admissions"].values():
                st[s] += 1
            b = b_traces[t["case"]]
            a_b = b["gate_outcome"] == engine.GOVERNED
            o_b = t["gate_outcome"] == engine.GOVERNED
            if a_b and o_b and b["controlling"] == t["controlling"]:
                kept += 1
            elif a_b and not o_b:
                lost += 1
            elif o_b:
                gained += 1
                gained_abst += 0 if a_b else 1
            if b["gate_outcome"] is not None and t["gate_outcome"] is not None:
                oc = BG.OracleCase(case_id=t["case"], expected=b["gate_outcome"],
                                   expected_controlling=b["controlling"] if a_b else None,
                                   guard=False, absolute=False)
                oracle.append(oc)
                answers[t["case"]] = BG.Answer(t["gate_outcome"], t["controlling"] if o_b else None)
        rep = BG.evaluate(oracle, lambda oc: answers[oc.case_id], min_binds=300, target_false_bind_rate=0.01).as_dict()
        results.append({"tolerance": tol, "admissions": dict(st), "binds": kept + gained,
                        "kept_vs_boolean": kept, "lost_vs_boolean": lost, "gained_vs_boolean": gained,
                        "gained_where_boolean_abstained": gained_abst,
                        "binding_gate": {k: rep[k] for k in ("verdict", "cause", "false_binds", "false_bind_upper_bound")}})

    # margin distribution at tolerance 0: discards that turned on the dimension alone
    engine.DIMENSIONS.clear()
    for f in factors:
        engine.DIMENSIONS[f] = {"weaker_when": "lower", "tolerance": 0.0, "unit": "index"}
    run0 = engine.replay(ov_cases, ov_seed, provisions, params["theta"])
    store0 = [r for r in run0["store"]]
    by_id = {c["id"]: c for c in ov_cases}
    margin = collections.Counter()
    dim_only = 0
    for t in run0["traces"]:
        if t["gate_outcome"] is None:
            continue
        case = engine.case_from_dict(by_id[t["case"]])
        live = [r for r in store0 if r.ts < case.ts]
        for rec in engine.retrieve(case, live, params["theta"]):
            adm = engine.admit(rec, case)
            if adm.status == engine.DISTINGUISHED:
                margin[len(adm.distinguishing)] += 1
                if len(adm.distinguishing) == 1 and adm.distinguishing[0] in factors:
                    dim_only += 1
    engine.DIMENSIONS.clear()

    # magnitude round-trip through the rationale
    reader = R.CuedRecordReader()
    vc = vw = vu = 0
    for c in ov_cases:
        prem = (c.get("engine") or {}).get("premise") or c["facts"]
        mine = [f for f in factors if f in prem]
        if not mine:
            continue
        rd = R.render_rationale(c, "plain", values={f: c["values"][f] for f in mine})
        reading = reader.read(rd.prose, c, list(c["facts"]), [], mine)
        sc = R.score_reading(reading, rd.truth)
        vc += sc.values_correct
        vw += sc.values_wrong
        vu += sc.values_unrecorded
    n_disc = sum(margin.values())
    out = {"pack": pack_name, "factors": factors, "threshold": THRESHOLD, "provenance": "synthetic overlay",
           "sweep": results,
           "margin_at_tolerance_0": {"discards": n_disc, "by_factor_count": dict(sorted(margin.items())),
                                     "dimension_alone": dim_only,
                                     "dimension_alone_share": round(dim_only / n_disc, 4) if n_disc else None},
           "magnitude_roundtrip": {"correct": vc, "wrong": vw, "unrecorded": vu},
           "caveat": ("Synthetic overlay: values are drawn deterministically from case ids to be consistent with the "
                      "boolean reading. The sweep shows what the kernel DOES at each tolerance on this corpus's "
                      "structure; it says nothing about which tolerance a constitution should declare.")}
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump(out, open(os.path.join(a.out, f"overlay_{pack_name}.json"), "w"), indent=1)
    if a.brief:
        row = "\n    ".join(f"τ={r['tolerance']:>4g}: binds {r['binds']:>5} kept {r['kept_vs_boolean']:>5} lost {r['lost_vs_boolean']:>4} "
                            f"gained {r['gained_vs_boolean']:>4} (where boolean abstained {r['gained_where_boolean_abstained']:>3})  "
                            f"tolerant {r['admissions'].get('tolerant', 0):>4}  false-bind UB {r['binding_gate']['false_bind_upper_bound']}"
                            for r in results)
        print(f"{pack_name:<34} {len(factors)} dimensions\n    {row}\n    margin@0: a dimension alone {dim_only}/{n_disc}; magnitudes read {vc}/{vc+vw+vu}")
    else:
        print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
