#!/usr/bin/env python3
"""OPTIONAL cross-check against a separate project; not used by any test, script or figure.

Run Likewise's precedence engine as the distinguishing gate over a Digital
Judiciary pack, and score it through Likewise's own binding gate against the
pack's computed ground truth.

    python3 tools/likewise_gate_bridge.py <pack-dir> --likewise <path-to-likewise-0.15.0> [--tolerance 0.0]

This is step 5 of docs/DISTINGUISH_ENGINE.md in the Likewise repository — "a
judiciary specification and a minimal worked corpus slice, run end to end
through the existing engine" — done on a whole 6,000-case pack rather than a
slice. The DJ engine supplies retrieval (premise coverage >= theta, lapse
filter) and the ordering rule; Likewise supplies `admit` (the five-valued
comparison lattice, the PREMISE_UNPROVEN > DISTINGUISHED > TOLERANT > A_FORTIORI
ladder) and `binding_gate.evaluate` (the one-sided false-bind bound with guard
items and an attainability floor). Every boolean factor is a point dimension:
present = 1.0, absent = 0.0, weaker when lower, tolerance as given.

Two mapping decisions are made explicit because they decide the result:

  * facts are a CLOSED world in these corpora (the Evaluator is modelled at
    epsilon = 1.00), so a premise factor the case lacks is a recorded 0.0 and
    not a silence. PREMISE_UNPROVEN therefore cannot arise here; it is the
    status that WOULD arise once facts come from an extractor that abstains.
  * the oracle's expectation is read from the DJ trace: bound -> GOVERNED with
    the controlling record; tie -> NO_CONTROLLING; fresh with candidates ->
    ALL_DISTINGUISHED; fresh without -> NO_CANDIDATES. Absolute short-circuits,
    docketed and consolidated arrivals never reach the gate and are excluded.
    E-distinguish cases are guard items: binding is wrong by construction.

Also reports the gate-margin distribution — how many premise factors each
discard turned on — which is the quantity DISTINGUISH_ENGINE.md §9 names as the
thing that would change its author's mind.
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("pack")
    ap.add_argument("--likewise", required=True, help="path to the likewise-0.15.0 checkout")
    ap.add_argument("--tolerance", type=float, default=0.0)
    ap.add_argument("--theta", type=float, default=None)
    a = ap.parse_args(argv)

    pack = os.path.abspath(a.pack)
    sys.path.insert(0, os.path.join(pack, "harness"))
    sys.path.insert(0, os.path.abspath(a.likewise))
    import engine  # noqa: E402
    from likewise import precedent as LP  # noqa: E402
    from likewise import binding_gate as BG  # noqa: E402

    rb = json.load(open(os.path.join(pack, "constitution", "rulebook.json")))
    params = json.load(open(os.path.join(pack, "constitution", "parameters.json")))
    theta = a.theta if a.theta is not None else params["theta"]
    engine.load_roster(os.path.join(pack, "constitution", "organizations.json"))
    P = {p["id"]: engine.Provision.from_dict(p) for p in rb["provisions"]}
    cases = json.load(open(os.path.join(pack, "corpus", "cases.json")))["cases"]
    store = [engine.Record.from_dict(r) for r in json.load(open(os.path.join(pack, "corpus", "store_seed_initial.json")))["records"]]

    # ---- one chronological pass: oracle from the DJ engine, ruling from Likewise
    oracle_cases, rulings = [], {}
    margins = collections.Counter()
    status_counts = collections.Counter()
    skipped = collections.Counter()
    for cd in cases:
        case = engine.case_from_dict(cd)
        tr = engine.adjudicate(case, store, P, theta)
        route = tr["route"]
        if route in (engine.ROUTE_ABSOLUTE, engine.ROUTE_DOCKET_DECLINED, engine.ROUTE_DOCKET_NULL,
                     engine.ROUTE_CONSOLIDATED) or case.control_plane:
            skipped[route] += 1
        else:
            facts = set(case.facts)
            candidates = engine.retrieve(case, store, theta)
            # -- Likewise admission on each candidate
            admissions = []
            for r in candidates:
                premise = [LP.PremiseDim(f, "lower", a.tolerance) for f in r.premise]
                subj = {f: 1.0 if f in facts else 0.0 for f in r.premise}
                ref = {f: 1.0 for f in r.premise}
                adm = LP.admit(r.id, premise, subj, ref)
                admissions.append(adm)
                status_counts[adm.status] += 1
                if adm.status == LP.DISTINGUISHED:
                    margins[len(adm.distinguishing)] += 1
            admitted = [adm for adm in admissions if adm.admitted]
            # -- DJ ordering over the admitted set supplies authority
            if not candidates:
                ruling = LP.Ruling(LP.NO_CANDIDATES, cause="retrieval returned no candidate")
            elif not admitted:
                ruling = LP.Ruling(LP.ALL_DISTINGUISHED, cause="every candidate was distinguished",
                                   admissions=tuple(admissions))
            else:
                recs = {r.id: r for r in candidates}
                top, keys = engine.order([recs[adm.precedent_id] for adm in admitted])
                if isinstance(top, engine.Record):
                    ruling = LP.Ruling(LP.GOVERNED, controlling=top.id, admissions=tuple(admitted))
                else:
                    ruling = LP.Ruling(LP.NO_CONTROLLING, cause="the ordering rule tied", admissions=tuple(admitted))
            # -- the oracle, from the DJ trace
            if route == engine.ROUTE_BOUND:
                expected, ctrl = LP.GOVERNED, tr["controlling"]
            elif route == engine.ROUTE_TIE:
                expected, ctrl = LP.NO_CONTROLLING, None
            elif tr["consulted"]:
                expected, ctrl = LP.ALL_DISTINGUISHED, None
            else:
                expected, ctrl = LP.NO_CANDIDATES, None
            oc = BG.OracleCase(case_id=case.id, expected=expected, expected_controlling=ctrl,
                               guard=(cd["category"] == "E-distinguish"),
                               provision=case.rules[0] if case.rules else None,
                               absolute=any(P[p].absolute for p in case.rules if p in P))
            oracle_cases.append(oc)
            rulings[case.id] = ruling
        if tr["admitted"]:
            rec = engine._record_from(case, tr, P)
            store.append(rec)
    report = BG.evaluate(oracle_cases, lambda oc: rulings[oc.case_id],
                         min_binds=300, target_false_bind_rate=0.01)
    d = report.as_dict()
    n_disc = sum(margins.values())
    out = {
        "pack": os.path.basename(pack), "theta": theta, "tolerance": a.tolerance,
        "cases_reaching_the_gate": len(oracle_cases), "excluded_before_the_gate": dict(skipped),
        "likewise_admission_statuses": dict(status_counts),
        "gate_margin_histogram": dict(sorted(margins.items())),
        "single_factor_discard_share": round(margins[1] / n_disc, 4) if n_disc else None,
        "binding_gate": {k: d[k] for k in ("verdict", "cause", "n_cases", "binds", "false_binds",
                                           "false_bind_upper_bound", "missed_bind_rate", "by_verdict")},
        "guard_binds": d["guard_binds"][:5],
        "abstention_divergences": d["abstention_divergences"][:5],
        "note": ("Likewise's admit() as the gate, the DJ engine's retrieve() and order() around it, "
                 "scored by Likewise's binding gate against the DJ trace as oracle. Facts are a closed "
                 "world here, so PREMISE_UNPROVEN cannot arise; it is the status an abstaining "
                 "extractor would produce. The verdict is 'inconclusive' by Likewise's own rule "
                 "when the oracle is self-authored, whatever the counts say."),
    }
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
