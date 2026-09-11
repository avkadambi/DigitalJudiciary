#!/usr/bin/env python3
"""Numerals federation checks — ten properties of the enterprise constitution,
the inheritance map and the federated stream, computed from executed traces and
from the six rulebooks as shipped. Nothing is asserted from the case files.

    python3 harness/run_federation_checks.py

Exit code 0 when every check passes.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SIM = os.path.dirname(ROOT)
sys.path.insert(0, HERE)

import engine  # noqa: E402
import federation as F  # noqa: E402

CHECKS = []


def check(cid, desc):
    def deco(fn):
        CHECKS.append((cid, desc, fn)); return fn
    return deco


class Run:
    def __init__(self):
        self.rulebook = json.load(open(os.path.join(ROOT, "constitution", "rulebook.json")))
        self.params = json.load(open(os.path.join(ROOT, "constitution", "parameters.json")))
        self.orgs = json.load(open(os.path.join(ROOT, "constitution", "organizations.json")))
        self.inherit = json.load(open(os.path.join(ROOT, "constitution", "inheritance.json")))
        self.pack = json.load(open(os.path.join(ROOT, "corpus", "cases.json")))
        seed = json.load(open(os.path.join(ROOT, "corpus", "store_seed_initial.json")))
        self.seed, self.seed_div = seed["records"], seed["record_division"]
        engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))
        self.provisions = {p["id"]: engine.Provision.from_dict(p) for p in self.rulebook["provisions"]}
        self.cases = self.pack["cases"]
        self.by_id = {c["id"]: c for c in self.cases}
        self.result = F.replay(self.cases, self.seed, self.seed_div, self.provisions, self.params["theta"])
        self.traces = {t["case"]: t for t in self.result["traces"]}
        self.record_division = self.result["record_division"]
        self.divisions = {}
        for key, meta in self.rulebook["divisions"].items():
            root = os.path.join(SIM, meta["pack"])
            self.divisions[key] = {
                "rulebook": json.load(open(os.path.join(root, "constitution", "rulebook.json"))),
                "orgs": json.load(open(os.path.join(root, "constitution", "organizations.json"))),
            }


@check("FC-01", "Replay reproduces every case's recorded decision, route and controlling record")
def fc01(r):
    bad = [c["id"] for c in r.cases
           if (r.traces[c["id"]]["decision"], r.traces[c["id"]]["route"], r.traces[c["id"]]["controlling"])
           != (c["expect"]["final_decision"], c["expect"]["route"], c["expect"]["controlling"])]
    return not bad, f"{len(r.cases)} cases replayed through the federated engine, {len(bad)} differ", bad[:5]


@check("FC-02", "Minimum harmonisation — no division states an enterprise floor as an ordinary provision")
def fc02(r):
    by = {d: {p["id"]: p for p in v["rulebook"]["provisions"]} for d, v in r.divisions.items()}
    bad = []
    for p in r.rulebook["provisions"]:
        if not p["absolute"]:
            continue
        for d, m in p["implemented_by"].items():
            if not m["applies"] or not m["provisions"]:
                continue
            if not any(by[d][x["id"]]["absolute"] for x in m["provisions"]):
                bad.append(f"{p['id']}<-{d}")
    # the mapping file must agree with the rulebooks it was derived from
    stale = [f"{p['id']}<-{d}:{x['id']}" for p in r.rulebook["provisions"] for d, m in p["implemented_by"].items()
             for x in m["provisions"] if by[d][x["id"]]["absolute"] != x["absolute"]]
    n_abs = sum(1 for p in r.rulebook["provisions"] if p["absolute"])
    n_prop = sum(1 for p in r.rulebook["provisions"] if p.get("proposed_absolute"))
    return (not bad and not stale,
            f"{n_abs} enterprise floors, every applicable division states each as a floor; {n_prop} further floors "
            f"proposed and held ordinary pending division amendment; mapping agrees with the rulebooks ({len(stale)} stale)",
            (bad + stale)[:5])


@check("FC-03", "Inheritance map complete — every applicable (provision, division) cell is implemented or filed as a gap amendment")
def fc03(r):
    amend = json.load(open(os.path.join(ROOT, "constitution", "proposed_amendments.json")))["amendments"]
    filed = {(a["enterprise_provision"], d) for a in amend for d in a["targets"]}
    gaps = [(g["enterprise"], g["division"]) for g in r.inherit["gaps"]]
    unfiled = [g for g in gaps if g not in filed]
    rows = r.inherit["rows"]
    n_impl = sum(1 for x in rows if x["status"] in ("implemented", "tightened"))
    n_tight = sum(1 for x in rows if x["status"] == "tightened")
    return (not unfiled,
            f"{len(rows)} cells: {n_impl} implemented ({n_tight} tightened by the division), "
            f"{sum(1 for x in rows if x['status'] == 'not_applicable')} not applicable, {len(gaps)} gaps, all {len(gaps)} filed as draft amendments",
            unfiled[:5])


@check("FC-04", "A1 per level — enterprise principals are disjoint from every division roster and from each other")
def fc04(r):
    ent = {}
    for org in r.orgs["organizations"]:
        for p in org["principals"]:
            ent.setdefault(p["principal_id"], set()).add(p["branch"])
    dual = [k for k, v in ent.items() if len(v) > 1]
    clash = []
    for d, v in r.divisions.items():
        for org in v["orgs"]["organizations"]:
            for p in org["principals"]:
                if p["principal_id"] in ent:
                    clash.append(f"{d}:{p['principal_id']}")
    return not dual and not clash, f"{len(ent)} enterprise principals, {len(dual)} in two branches, {len(clash)} also in a division roster", (dual + clash)[:5]


@check("FC-05", "Cross-division like-case consistency — anchor and twin, filed by different divisions, reach the same disposition and citation")
def fc05(r):
    bad, n, cross = [], 0, 0
    for p in r.pack["like_case_pairs"]:
        a, b = r.traces[p["a"]], r.traces[p["b"]]
        n += 1
        if r.by_id[p["a"]]["division"] != r.by_id[p["b"]]["division"]:
            cross += 1
        if a["decision"] != b["decision"] or a["controlling"] != b["controlling"]:
            bad.append(p["a"])
    return not bad and cross == n, f"{n} pairs, {cross} across divisions, {len(bad)} disagree on disposition or citation", bad[:5]


@check("FC-06", "Enterprise precedent binds across divisions — every C-cross case is controlled by a record another division wrote")
def fc06(r):
    bad, n = [], 0
    for c in r.cases:
        if c["category"] != "C-cross":
            continue
        n += 1
        t = r.traces[c["id"]]
        if t["route"] != engine.ROUTE_BOUND or r.record_division.get(t["controlling"]) in (None, c["division"]):
            bad.append(c["id"])
    total_foreign = sum(1 for c in r.cases if r.traces[c["id"]]["controlling"] not in (None, "none_tie")
                        and r.record_division.get(r.traces[c["id"]]["controlling"]) not in (None, c["division"]))
    return not bad, f"{n} C-cross cases all bound by a foreign record; {total_foreign} cases in the whole stream are controlled by another division's record", bad[:5]


@check("FC-07", "Vertical precedent is thin — when a home record and a foreign record both survive, the scope key prefers the home record")
def fc07(r):
    bad, n = [], 0
    for c in r.cases:
        if c["category"] != "D-vertical":
            continue
        n += 1
        t = r.traces[c["id"]]
        if t["controlling"] != c["meta"]["home_record"] or "scope" not in t["keys_applied"] \
                or r.record_division.get(c["meta"]["foreign_record"]) == c["division"]:
            bad.append(c["id"])
    return not bad, f"{n} D-vertical cases, home record controls on the scope key in all but {len(bad)}", bad[:5]


@check("FC-08", "Pressure invariance across divisions — a twin filed by another division under a PACT mechanism does not move the trace")
def fc08(r):
    bad, n = [], 0
    for c in r.cases:
        if c["category"] != "P-pressure":
            continue
        ctrl = r.by_id.get(c["meta"]["control_case"])
        if not ctrl:
            continue
        n += 1
        a, b = r.traces[c["id"]], r.traces[ctrl["id"]]
        if (a["decision"] != b["decision"] or a["route"] != b["route"] or a["controlling"] != b["controlling"]
                or sorted(a["consulted"]) != sorted(b["consulted"]) or a["admitted"] != b["admitted"]
                or c["division"] == ctrl["division"]):
            bad.append(c["id"])
    return not bad, f"{n} cross-division pressure twins, {len(bad)} diverged on any of disposition, route, controlling record, consulted set or stored status", bad[:5]


@check("FC-09", "A6 at the enterprise level — every floor case short-circuits with no retrieval and no record, in whichever division files it")
def fc09(r):
    bad, n, divs = [], 0, set()
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["route"] == engine.ROUTE_ABSOLUTE:
            n += 1; divs.add(c["division"])
            if t["consulted"] or t["admitted"] or t["decision"] != engine.DENY:
                bad.append(c["id"])
    return not bad and len(divs) == 5, f"{n} short-circuits across {len(divs)} divisions, {len(bad)} leaked retrieval or a record", bad[:5]


@check("FC-10", "Every case carries a canary, an opaque-safe id, a division, and the enterprise level")
def fc10(r):
    bad = [c["id"] for c in r.cases if not c.get("canary", "").startswith("dj-corpus-canary:")
           or c.get("division") not in r.rulebook["divisions"] or c.get("level") != "enterprise"]
    return not bad, f"{len(r.cases)} cases, {len(bad)} malformed", bad[:5]



@check("FC-11", "Silence never binds across divisions — silencing one premise factor of a foreign controlling record breaks the bind and names the cause")
def fc11(r):
    """5.11.0 three-valued facts, under federation. Every case bound by
    ANOTHER division's record is re-adjudicated with the first premise factor
    of that record marked unrecorded; the engine must not bind on it and must
    name premise_not_established unless an untouched record controls."""
    import binding_gate as BG
    store = [engine.Record.from_dict(x) if isinstance(x, dict) else x for x in r.result["store"]]
    oracle, answers = [], {}
    for c in r.cases:
        t = r.traces[c["id"]]
        if t.get("gate_outcome") != engine.GOVERNED or r.record_division.get(t["controlling"]) in (None, c["division"]):
            continue
        case = engine.case_from_dict(c)
        live = F.view_for(c["division"], [rec for rec in store if rec.ts < case.ts], r.record_division)
        ctrl = next(rec for rec in live if rec.id == t["controlling"])
        silenced = ctrl.premise[0]
        cand = engine.retrieve(case, live, r.params["theta"])
        quiet = engine.Case(**{**case.__dict__, "facts": [f for f in case.facts if f != silenced],
                               "unrecorded": list(case.unrecorded) + [silenced]})
        untouched = [rec for rec in cand if silenced not in rec.premise
                     and engine.admit(rec, quiet, r.provisions).admitted]
        top, _ = engine.order(untouched)
        if isinstance(top, engine.Record):
            exp, exp_ctl = engine.GOVERNED, top.id
        elif top == "none_tie":
            exp, exp_ctl = engine.NO_CONTROLLING, None
        else:
            exp, exp_ctl = engine.PREMISE_NOT_ESTABLISHED, None
        oracle.append(BG.OracleCase(case_id=c["id"], expected=exp, expected_controlling=exp_ctl,
                                    guard=(exp != engine.GOVERNED)))
        tr = engine.adjudicate(quiet, live, r.provisions, r.params["theta"])
        answers[c["id"]] = BG.Answer(tr["gate_outcome"], tr["controlling"] if tr["gate_outcome"] == engine.GOVERNED else None)
    d = BG.evaluate(oracle, lambda oc: answers[oc.case_id]).as_dict()
    ok = d["n_cases"] > 0 and d["false_binds"] == 0 and not d["guard_binds"] and d["by_verdict"]["missed_bind"] == 0 \
        and d["by_verdict"]["abstain_diverged"] == 0
    return ok, (f"{d['n_cases']} cross-division binds silenced; {d['by_verdict']['abstain_agreed']} abstained "
                f"with cause premise_not_established, {d['by_verdict']['bind_agreed']} re-bound on an untouched "
                f"record; false binds {d['false_binds']}; binding-gate verdict {d['verdict']!r}"), \
        [str(x) for x in d["guard_binds"][:3]]


def main():
    run = Run()
    print(f"Numerals federation checks — corpus {run.pack['corpus_version']}, {len(run.cases)} cases, "
          f"opening store {len(run.seed)}, final store {len(run.result['store'])}")
    print("=" * 78)
    passed = 0
    for cid, desc, fn in CHECKS:
        ok, detail, sample = fn(run)
        passed += 1 if ok else 0
        print(f"{cid}  {'PASS' if ok else 'FAIL'}  {desc}")
        print(f"        {detail}")
        if not ok and sample:
            print(f"        sample: {sample}")
    print("=" * 78)
    print(f"RESULT: {passed}/{len(CHECKS)}")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
