#!/usr/bin/env python3
"""How much jurisprudence an adopted amendment unsettles — measured, not guessed.

    python3 tools/amendment_overlay.py <pack-dir> [--brief] [--out DIR]

Release 5.13.0 gave records a provision text version and the gate a rung,
`decided_under_prior_text`: a holding decided under text version n does not
govern once an adopted amendment has touched a factor the holding turned on.
Nothing in a released pack is amended, so this script adopts amendments in
memory and replays, three ways per provision that has records:

    limb       the amendment redefines the VIOLATING limb (touched = the violate factors)
    factor     it touches ONE compliant factor, the one most often in premises
    citation   it changes a citation only (touched = nothing)

and reports, against the unamended replay, the records that go stale, the
binds that fall to prior_text, the binds kept, and how quickly the store
heals — records written AFTER adoption carry the new version and bind again.
Adoption is placed at the first quartile of the stream by default (the
precedent-heavy categories are scheduled early) so that most binds fall
after it; `--adopt-at` moves it.

It also adopts the pack's own filed draft amendments (constitution/
proposed_amendments.json) under the reading that a status or limb change
touches the violating factors and a citation change touches nothing, and
reports what THEY would unsettle if the lawmakers adopted them today.

⟦synthetic overlay⟧: nothing is written to the pack; the constitution is not
amended by running this.
"""
from __future__ import annotations

import argparse
import collections
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extraction import snapshot  # noqa: E402

MODES = ("limb", "factor", "citation")


def _amend(provisions: dict, pid: str, touched: list, version: int = 2) -> dict:
    out = dict(provisions)
    p = copy.copy(provisions[pid])
    p.version = version
    p.amendments = list(provisions[pid].amendments) + [{"version": version, "touched_factors": sorted(touched)}]
    out[pid] = p
    return out


def _replay_with_adoption(engine, cases, seed, provisions, theta, adopt_at_ts, amended):
    """Replay: before adopt_at_ts the old text governs; from it the amended text does.
    Records written after adoption are stamped with the new version by the engine."""
    store = [engine.Record.from_dict(r) for r in seed]
    traces = []
    consolidation_seen = {}
    for c in cases:
        case = engine.case_from_dict(c)
        provs = amended if case.ts >= adopt_at_ts else provisions
        tr = engine.adjudicate(case, store, provs, theta)
        # the same consolidation bookkeeping as engine.replay
        if (case.consolidation_signature and tr["controlling"] is None and tr["route"] == engine.ROUTE_FRESH
                and case.consolidation_signature not in consolidation_seen and case.extra.get("class_representative")):
            consolidation_seen[case.consolidation_signature] = case.id
            tr["admitted"], tr["admission_ground"] = True, "clause_ii"
        elif case.consolidation_signature and case.extra.get("class_member"):
            tr["route"], tr["consulted"], tr["distinguished"] = engine.ROUTE_CONSOLIDATED, [], []
            tr["admitted"], tr["gate_outcome"] = False, None
        if tr["admitted"]:
            store.append(engine._record_from(case, tr, provs))
        traces.append(tr)
    return traces, store


def classify_amendment(a: dict) -> str:
    text = (a.get("proposed", "") + " " + a.get("finding", "")).lower()
    if "citation" in text and ("restate the citation" in text or "cite" in text) and "absolute" not in text:
        return "citation"
    return "limb"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("--out", default=None)
    ap.add_argument("--brief", action="store_true")
    ap.add_argument("--top", type=int, default=12, help="provisions to sweep (most-recorded first)")
    ap.add_argument("--adopt-at", type=float, default=0.25,
                    help="adoption point as a fraction of the stream (default 0.25: precedent-heavy categories sit early)")
    a = ap.parse_args(argv)

    engine, rb, params, cases, seed, provisions = snapshot.load_pack(a.pack)
    pack_name = os.path.basename(os.path.abspath(a.pack))
    theta = params["theta"]
    ref = engine.replay(cases, seed, provisions, theta)
    ref_tr = {t["case"]: t for t in ref["traces"]}
    adopt_at = cases[int(len(cases) * a.adopt_at)]["ts"]
    by_prov = collections.Counter(r.prov for r in ref["store"])
    binds_by_prov = collections.Counter()
    for t in ref["traces"]:
        if t["gate_outcome"] == engine.GOVERNED:
            binds_by_prov[next(r.prov for r in ref["store"] if r.id == t["controlling"])] += 1
    sweep_provs = [p for p, _ in binds_by_prov.most_common(a.top) if not provisions[p].absolute]
    # deny-side jurisprudence (corpus 2.1.0): provisions ranked by binds whose
    # controlling record turned on a violating factor — where a limb amendment
    # has something to unsettle.
    viol = {pid: set(pv.violate_factors) for pid, pv in provisions.items()}
    ctl = {r.id: r for r in ref["store"]}
    deny_binds = collections.Counter()
    for t in ref["traces"]:
        if t["gate_outcome"] == engine.GOVERNED:
            rec = ctl[t["controlling"]]
            if set(rec.premise) & viol[rec.prov]:
                deny_binds[rec.prov] += 1
    deny_provs = [p for p, _ in deny_binds.most_common(a.top) if p not in sweep_provs and not provisions[p].absolute]

    ts_by_id = {c["id"]: c["ts"] for c in cases}

    def measure(amended):
        traces, store = _replay_with_adoption(engine, cases, seed, provisions, theta, adopt_at, amended)
        k = collections.Counter()
        for t in traces:
            r = ref_tr[t["case"]]
            rb_ = r["gate_outcome"] == engine.GOVERNED
            ob = t["gate_outcome"] == engine.GOVERNED
            after = ts_by_id[t["case"]] >= adopt_at
            if rb_ and ob and r["controlling"] == t["controlling"]:
                k["binds_kept"] += 1
            elif rb_ and not ob:
                k["binds_lost"] += 1
                if t["gate_outcome"] == engine.PRIOR_TEXT_ONLY:
                    k["binds_lost_to_prior_text"] += 1
            elif ob and (not rb_ or r["controlling"] != t["controlling"]):
                k["rebound_on_other_record"] += 1
                if after and t["controlling"] and any(s.id == t["controlling"] and s.prov_version >= 2 for s in store):
                    k["rebound_on_post_adoption_record"] += 1
            if r["decision"] != t["decision"]:
                k["decisions_changed"] += 1
        k["stale_records"] = sum(1 for s in store if s.prov_version < amended.get(s.prov, provisions[s.prov]).version
                                 and amended[s.prov].touched_since(s.prov_version) & set(s.premise))
        k["records_written_under_new_text"] = sum(1 for s in store if s.prov_version >= 2)
        return dict(k)

    sweep = []
    prem_freq = collections.Counter(f for r in ref["store"] for f in r.premise)
    for pid in sweep_provs + deny_provs:
        p = provisions[pid]
        row = {"provision": pid, "records": by_prov[pid], "binds": binds_by_prov[pid],
               "binds_by_deny_records": deny_binds[pid], "ranked_by": "binds" if pid in sweep_provs else "deny-side binds"}
        for mode in MODES:
            if mode == "limb":
                touched = list(p.violate_factors)
            elif mode == "factor":
                touched = [max(p.comply_factors, key=lambda f: prem_freq[f])] if p.comply_factors else []
            else:
                touched = []
            row[mode] = measure(_amend(provisions, pid, touched))
        sweep.append(row)

    # the pack's own filed amendments, adopted today
    filed = []
    pa = json.load(open(os.path.join(a.pack, "constitution", "proposed_amendments.json")))
    for am in pa.get("amendments", []):
        targets = am.get("targets") or []
        if isinstance(targets, dict):
            targets = [t for v in targets.values() for t in v]
        kind = classify_amendment(am)
        amended = dict(provisions)
        for pid in targets:
            if pid in provisions:
                touched = list(provisions[pid].violate_factors) if kind == "limb" else []
                amended = _amend(amended, pid, touched)
        filed.append({"id": am["id"], "targets": targets, "read_as": kind,
                      "records_on_targets": sum(by_prov[t] for t in targets if t in by_prov),
                      **measure(amended)})

    tot = lambda key: sum(r.get(key, 0) for r in filed)  # noqa: E731
    out = {"pack": pack_name, "adoption_ts": adopt_at, "reference_binds": sum(binds_by_prov.values()),
           "binds_by_deny_records": sum(deny_binds.values()),
           "sweep": sweep, "filed_amendments": filed,
           "filed_summary": {"amendments": len(filed), "read_as_limb": sum(1 for r in filed if r["read_as"] == "limb"),
                             "read_as_citation": sum(1 for r in filed if r["read_as"] == "citation"),
                             "binds_lost_to_prior_text_if_all_adopted_separately": tot("binds_lost_to_prior_text"),
                             "stale_records_if_all_adopted_separately": tot("stale_records")},
           "provenance": "synthetic overlay; nothing written to the pack"}
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump(out, open(os.path.join(a.out, f"amendments_{pack_name}.json"), "w"), indent=1)
    if a.brief:
        print(f"{pack_name:<34} adoption at ts {adopt_at}; {len(sweep)} provisions swept")
        for r in sweep[:3] + [x for x in sweep if x["ranked_by"] == "deny-side binds"][:3]:
            print(f"    {r['provision']:<12} recs {r['records']:>3} binds {r['binds']:>4} (deny-side {r['binds_by_deny_records']:>3}) | limb: stale {r['limb']['stale_records']:>3} "
                  f"lost {r['limb'].get('binds_lost_to_prior_text', 0):>3} healed-on-new {r['limb'].get('rebound_on_post_adoption_record', 0):>3} "
                  f"| factor: stale {r['factor']['stale_records']:>3} lost {r['factor'].get('binds_lost_to_prior_text', 0):>3} "
                  f"| citation: stale {r['citation']['stale_records']:>3} lost {r['citation'].get('binds_lost_to_prior_text', 0):>3}")
        fs = out["filed_summary"]
        print(f"    filed amendments: {fs['amendments']} ({fs['read_as_limb']} read as limb, {fs['read_as_citation']} citation); "
              f"if each were adopted today: {fs['binds_lost_to_prior_text_if_all_adopted_separately']} binds fall to prior text, "
              f"{fs['stale_records_if_all_adopted_separately']} records go stale")
    else:
        print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
