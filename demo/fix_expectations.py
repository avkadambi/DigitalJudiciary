#!/usr/bin/env python3
"""Repair the six unresolvable `expect.controlling` identifiers (App. C item 11 / G9).

Decided 1 September 2026: repair per pack, from the mechanism.

D03 and D04 named `SP-0101` and its parallels — identifiers that do not exist. The
correct value follows from the ordering rule rather than from the run. Each pack's
`-012` seed is a service-scoped denial; `scope` prefers the narrower recorded scope
*that covers the case*. In sctower, vetpoc and frontierllm, D03 and D04 sit inside
that service, so the service-scoped denial covers them and outranks the org-scoped
`-001` permit. In dcvigil the cases sit in `edge` while `DP-012` is scoped to
`remediation`, so the denial does not cover them and the org-scoped permit controls.
The cross-pack divergence Appendix G recorded as G9 is therefore the scope key
behaving exactly as specified; what was wrong is that the corpus copied one outcome
into all four packs.

G04 named `SP-0109`. That is not a typo for `SP-009`: `SP-009` is a lapsed
acceptance, which A7 excludes from Candidates, so it cannot control anything. The
record that does control G04 is created during the run by an earlier case, and the
corpus's `expect.controlling` convention names seed identifiers only — it cannot
express a run-created record. The field is therefore set to null with a note, which
is the same modelling limitation Appendix C item 10 already records for vetpoc's
two-provision case. The outcome expectation (`deny`) was already correct and is
unchanged.

Nothing here is read off the executed traces. Every value is derived from the
ordering rule, A7, and the scope data in the packs; the run is then used to *check*
the result, never to produce it.
"""
import json, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/dj-press"
PACKS = ("sctower", "vetpoc", "dcvigil", "frontierllm")

# per pack: does the service-scoped -012 denial cover D03/D04?
COVERS = {"sctower": True, "vetpoc": True, "dcvigil": False, "frontierllm": True}
SEED_PREFIX = {"sctower": "SP", "vetpoc": "PR", "dcvigil": "DP", "frontierllm": "FP"}


def fix(pack):
    p = os.path.join(ROOT, "demo", "companies", pack, "cases.json")
    doc = json.load(open(p))
    pre = SEED_PREFIX[pack]
    changed = []
    for c in doc["cases"]:
        e = c["expect"]
        if c["id"] in ("D03", "D04"):
            if COVERS[pack]:
                e["controlling"] = f"{pre}-012"
                e["tier1_decision"] = "deny"
                e["final_decision"] = "deny"
            else:
                e["controlling"] = f"{pre}-001"
                e["tier1_decision"] = "permit_conditional"
                e["final_decision"] = "permit_conditional"
            e["controlling_basis"] = (
                "scope key: the service-scoped denial covers this case and outranks the "
                "org-scoped permit" if COVERS[pack] else
                "scope key: the service-scoped denial does not cover this case, so the "
                "org-scoped permit controls")
            changed.append((c["id"], e["controlling"], e["final_decision"]))
        elif c["id"] == "G04":
            e["controlling"] = None
            e["controlling_basis"] = (
                "a record created earlier in this run controls; the seed-identifier "
                "convention cannot name it. The former value named a lapsed acceptance, "
                "which A7 excludes from Candidates and which therefore could never control")
            changed.append((c["id"], None, e["final_decision"]))
    doc["expectation_repair"] = {
        "date": "2026-09-01",
        "scope": "D03, D04, G04 — six unresolvable expect.controlling identifiers across four packs",
        "derived_from": "the ordering rule, A7, and the packs' own scope data; not from executed traces",
        "recorded_at": "Appendix C item 11; Appendix G row G9",
    }
    json.dump(doc, open(p, "w"), indent=1)
    print(f"  {pack}: " + " · ".join(f"{i}→{c}/{d}" for i, c, d in changed))


for pack in PACKS:
    fix(pack)
