#!/usr/bin/env python3
"""Add the L-consolidated category to the four executed demo packs.

WHY THIS EXISTS
---------------
Definition 7 as amended admits a record in two circumstances: it was contested
and resolved above first instance (clause (i), unchanged), or it is the
designated representative of a consolidation class (clause (ii), new). Clause
(ii) is the whole of what RA-3's consolidation specification adds to the
architecture, and the specification's own five clauses are the interesting
part: each one refuses something, and each refusal is a place a build could
quietly go wrong.

A category that only demonstrated the happy path would be worth very little.
Eight cases per pack, and five of the eight exist to be REFUSED:

  L01 L02 L03  one class forms. Three co-pending units of equal signature on a
               provision no live record covers, resolving to Controlling=none.
               L03 carries an extra factor the rulebook does not predicate on,
               so it is alike under F_p and different outside it: under
               Definition 15's grain all three class, and under the M11 mutant
               — which reads facts(c) instead of facts(c) INTERSECT F_p — L03
               drops out and CC-20(g) fails. One consolidated record.
  L04 L05      clause (e). Their signature is already covered by a live
               record, so no class forms and both are disposed the ordinary
               way, bound by that record. This is the clause the
               |Rules|*2^kappa ceiling rests on; M12 deletes it.
  L06          clause (b). A unit engaging two provisions has two signatures
               and could be a member of two classes with different
               representatives, while `resolve` returns a single controlling
               record for the whole case. Resolving that conflict is a
               judgment and the specification refuses it. L06 shares L01's
               signature under the first provision and is NOT a member; it is
               adjudicated on its own and comes out bound by the record L01
               created — which is exactly the point that a unit the class
               excludes is not lost, only more expensive.
  L07 L08      clause (c). Two co-pending units of equal signature on an
               ABSOLUTE provision. Without clause (c) they would form a class
               and admit a first-instance record for a floor violation, which
               is the worst thing in this specification's neighbourhood. A6
               short-circuits each of them individually instead.

The category also makes control S5 real: raising N0 from 2 to 3 changes
nothing, because the only class that forms has three members. A control that
could not have failed records nothing; this one records a fact about the
corpus.

Idempotent: refuses to apply twice.
"""
from __future__ import annotations
import json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# A marker the rulebook predicates on nowhere. It is what makes L03 alike
# under F_p and different outside it; the builder asserts it is unpredicated
# rather than trusting the name.
MARKER = "batch_reference_note"


def predicated_factors(rulebook) -> set:
    out = set()
    for p in rulebook["provisions"]:
        for v in (p.get("policy") or {}).values():
            if isinstance(v, list):
                out.update(v)
            elif isinstance(v, str):
                out.add(v)
    return out


def pick(pack: str, pack_dir: str, db_path: str) -> dict:
    """Read the executed store and choose the three provisions the category
    needs. Nothing here is hand-picked per pack: the choice is derived from
    what the run actually produced, so it stays right if the corpus moves."""
    rb = json.load(open(os.path.join(pack_dir, "rulebook.json")))
    prov = {p["provision_id"]: p for p in rb["provisions"]}
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(
        "SELECT * FROM record_effective WHERE lapsed=0 AND superseded=0")]
    con.close()
    used = {r["provision_id"] for r in rows}

    # (1) The class provision: non-absolute, with a deny factor, and carrying
    # no live record at all — so retrieval returns nothing and `resolve`
    # returns none_empty, which is clause (d)'s plain `none`.
    empty = [p for p, v in sorted(prov.items())
             if not v["absolute"] and p not in used
             and (v["policy"].get("deny_if_any") or [])]
    if not empty:
        raise SystemExit(f"{pack}: no uncovered non-absolute provision")
    p_class = empty[0]

    # (2) The covered signature, for clause (e): any live record on a
    # non-absolute provision. Its own facts are the unit's facts, so the
    # signatures are equal by construction.
    covered = next((r for r in rows if not prov[r["provision_id"]]["absolute"]),
                   None)
    if covered is None:
        raise SystemExit(f"{pack}: no live record to be covered by")
    # The covered pair is bound by that record, so its disposition is that
    # record's holding and not a fresh application of the provision. Read it
    # rather than assuming it: the first draft of this builder wrote "deny"
    # for a record whose holding is a conditional permit, and the run said so.
    covered_outcome = json.loads(covered["interpretation"])["outcome"]

    # (3) The floor, for clause (c).
    absol = [p for p, v in sorted(prov.items())
             if v["absolute"] and (v["policy"].get("deny_if_any") or [])]
    if not absol:
        raise SystemExit(f"{pack}: no absolute provision with a trigger")
    p_floor = absol[0]

    # (4) A second provision for clause (b)'s multi-provision unit. It must be
    # non-absolute, so that the unit is adjudicated rather than short-circuited
    # and the exclusion is visibly about clause (b) and not about A6.
    second = next((p for p, v in sorted(prov.items())
                   if not v["absolute"] and p != p_class
                   and (v["policy"].get("deny_if_any") or [])), None)
    if second is None:
        raise SystemExit(f"{pack}: no second non-absolute provision")

    return {"p_class": p_class,
            "class_factors": sorted(prov[p_class]["policy"]["deny_if_any"]),
            "covered_provision": covered["provision_id"],
            "covered_facts": sorted(json.loads(covered["facts"])),
            "p_floor": p_floor,
            "floor_factor": sorted(prov[p_floor]["policy"]["deny_if_any"])[0],
            "second": second,
            "second_factor": sorted(prov[second]["policy"]["deny_if_any"])[0],
            "covered_outcome": covered_outcome}


def build(pack_dir: str, pack: str, db_path: str) -> int:
    cases_path = os.path.join(pack_dir, "cases.json")
    doc = json.load(open(cases_path))
    cases = doc["cases"]
    if any(c.get("category") == "L-consolidated" for c in cases):
        if "--rebuild" not in sys.argv:
            print(f"  {pack}: already extended, refusing")
            return 0
        cases = [c for c in cases if c.get("category") != "L-consolidated"]

    rb = json.load(open(os.path.join(pack_dir, "rulebook.json")))
    if MARKER in predicated_factors(rb):
        raise SystemExit(f"{pack}: {MARKER} is predicated on by a provision")

    s = pick(pack, pack_dir, db_path)
    cf = s["class_factors"]
    org = pack

    def case(cid, provisions, factors, note, expect):
        return {"id": cid, "organization": org, "category": "L-consolidated",
                "author": "agent:codegen-1", "domain": "org",
                "description": note, "provisions": provisions,
                "factors": sorted(factors), "violation": True,
                "contest_to": 1, "expect": expect,
                "consolidation": {"clause": expect.pop("_clause")}}

    added = [
        case("L01", [s["p_class"]], cf,
             f"Batch item 1 of 3: routine {s['p_class']} exception, same"
             f" profile as its two co-pending siblings",
             {"_clause": "representative (Def.7(ii))", "route": "adjudicate",
              "tier1_decision": "deny", "final_decision": "deny",
              "final_tier": 1, "controlling": None, "stored": True}),
        case("L02", [s["p_class"]], cf,
             "Batch item 2 of 3: identical profile, disposed by citation of"
             " the representative's record",
             {"_clause": "member (Def.7(ii))", "route": "adjudicate",
              "tier1_decision": "deny", "final_decision": "deny",
              "final_tier": 1, "controlling": "L01", "stored": False}),
        case("L03", [s["p_class"]], cf + [MARKER],
             "Batch item 3 of 3: same profile under the provision, one extra"
             " fact the rulebook does not read",
             {"_clause": "member, grain test (Def.14)", "route": "adjudicate",
              "tier1_decision": "deny", "final_decision": "deny",
              "final_tier": 1, "controlling": "L01", "stored": False}),
        case("L04", [s["covered_provision"]], s["covered_facts"],
             f"Co-pending {s['covered_provision']} request whose signature a"
             f" live holding already covers",
             {"_clause": "clause (e): covered, no class", "route": "adjudicate",
              "tier1_decision": s["covered_outcome"],
              "final_decision": s["covered_outcome"],
              "final_tier": 1, "controlling": "existing", "stored": False}),
        case("L05", [s["covered_provision"]], s["covered_facts"],
             "Its co-pending twin: same signature, same live cover, still no"
             " class",
             {"_clause": "clause (e): covered, no class", "route": "adjudicate",
              "tier1_decision": s["covered_outcome"],
              "final_decision": s["covered_outcome"],
              "final_tier": 1, "controlling": "existing", "stored": False}),
        case("L06", [s["p_class"], s["second"]],
             cf + [s["second_factor"]],
             "Two provisions at once, sharing the class signature under the"
             " first: excluded by clause (b) and adjudicated on its own",
             {"_clause": "clause (b): multi-provision, excluded",
              "route": "adjudicate", "tier1_decision": "deny",
              "final_decision": "deny", "final_tier": 1,
              "controlling": "L01", "stored": False}),
        case("L07", [s["p_floor"]], [s["floor_factor"]],
             f"Floor item 1 of 2: {s['p_floor']} is absolute and two of these"
             f" are co-pending with the same profile",
             {"_clause": "clause (c): floor, excluded",
              "route": "absolute_deny", "tier1_decision": "deny",
              "final_decision": "deny", "final_tier": 1,
              "controlling": None, "stored": False}),
        case("L08", [s["p_floor"]], [s["floor_factor"]],
             "Floor item 2 of 2: without clause (c) these two would class and"
             " a floor violation would become law",
             {"_clause": "clause (c): floor, excluded",
              "route": "absolute_deny", "tier1_decision": "deny",
              "final_decision": "deny", "final_tier": 1,
              "controlling": None, "stored": False}),
    ]

    # Appended, not interleaved. The docket boundary sits immediately before
    # the block and the whole block is co-pending across it, which is what
    # makes S_t one pinned store for every member. Interleaving them — the
    # placement the P-pressure category needs — would give members different
    # stores and make the class a statement about nothing.
    doc["cases"] = cases + added
    doc["consolidation_extension"] = {
        "version": "1.0",
        "added": len(added),
        "basis": "RA-3 round 2, Definitions 15 and 16; Definition 7 clause (ii)",
        "selection": s,
        "boundary": ("classes are formed immediately before L01 is delivered,"
                     " against the store as it then stands, and before any"
                     " member is adjudicated (CC-22(b))"),
        "claim": ("exactly one class forms per pack, over L01-L03, admitting"
                  " one first-instance record under Definition 7(ii). L04-L08"
                  " are the five refusals: clause (e) twice, clause (b) once,"
                  " clause (c) twice."),
    }
    json.dump(doc, open(cases_path, "w"), indent=1)
    print(f"  {pack}: +{len(added)} L-consolidated cases -> "
          f"{len(doc['cases'])} total   class on {s['p_class']}"
          f" {cf}, floor {s['p_floor']}, covered {s['covered_provision']}")
    return len(added)


def main(root: str, dbdir: str) -> None:
    packs = os.path.join(root, "demo", "companies")
    total = 0
    for pack in ("sctower", "vetpoc", "dcvigil", "frontierllm"):
        total += build(os.path.join(packs, pack), pack,
                       os.path.join(dbdir, f"{pack}.db"))
    print(f"total added: {total}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE),
         sys.argv[2] if len(sys.argv) > 2 else "/tmp/djL")
