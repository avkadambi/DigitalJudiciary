#!/usr/bin/env python3
"""Convert the original Paper-3 simulation into container-native demo packs.

The original simulation (`paper3_simulation/groundtruth_<company>.json`) was
written against a standalone formal engine. This script re-expresses it in the
vocabulary the deployed container speaks — a rulebook the ConstitutionStore can
enact, seed jurisprudence the Challenge Gate can admit, and a case list the
inbound gateway can replay — WITHOUT inventing anything the original did not
say.

Two conversions need care, and both are recorded rather than hidden:

1. **Deny predicates.** The original provisions carry text and an `absolute`
   flag but no fact-predicate: whether a case violated its provision was a
   declared scenario property (`violation`), exactly like `contest_to`. The
   container's tier-1 evaluation needs an actual predicate over facts, so one
   is DERIVED here:

       deny_if_any(P) = { factors of violating cases engaging P }
                        - { factors appearing in any premise of a record on P }
                        - { "compliant" }

   The subtraction matters. A factor that appears in a record's premise is a
   MITIGATING fact — the thing a precedent's holding rested on — and making it
   a trigger would collapse the distinguishing gate into the predicate. The
   derivation is then verified case-by-case against the original's own
   `tier1_decision`, and the script fails loudly if any case disagrees.

2. **Provision engagement.** Which provisions a change engages is likewise a
   scenario property in the original (`prov`), not something it derived from
   signals. The demo therefore replays `prov` directly instead of fabricating a
   GitHub factor map for 4 companies x ~21 provisions. Floor-first ordering is
   still decided by the live constitution at replay time, so A6 is enforced by
   the container, not by this file.

Usage:  python3 demo/build_packs.py <path-to-paper3_simulation>
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "companies")

COMPANIES = {
    "sctower": "SC Control Tower",
    "vetpoc": "VetPOC",
    "dcvigil": "DCVigil",
    "frontierllm": "FrontierLLM",
}

# The original's authority vocabulary -> the container's tiers and principals.
AUTH = {"Tier2": (2, "svc:tier2"),
        "Tier3": (3, "svc:tier3"),
        "RiskOwner": (4, "coo.pat")}

CONTROL_PLANE = "constitution"


def iso(day: str | None) -> str | None:
    """'2025-11-18' -> the container's fixed ISO-8601 UTC form."""
    if not day:
        return None
    return f"{day}T00:00:00.000000+00:00" if len(day) == 10 else day


def anchor_offset(gt: dict, margin_days: int = 7) -> int:
    """Days to shift every timestamp so the corpus's lapse state is reproduced.

    The original corpus has an implicit as-of date that it never states. Every
    one of its acceptances carries a referral_status, which means the engine
    evaluated all of them as already lapsed and having emitted their referral —
    and that is only true at an instant later than the latest expiry in the
    file. The container, correctly, evaluates lapse against the clock, so
    replaying the raw dates today would leave most of those waivers still live
    and the lapse and renewal scenarios would silently not fire.

    So the whole corpus is shifted by ONE constant, chosen to put the latest
    expiry `margin_days` in the past. A constant offset preserves every
    relative ordering, which is what the recency elimination key reads, and it
    is a single declared number rather than a set of hand-edited dates.
    """
    from datetime import date, datetime, timedelta
    expiries = [r.get("expiry") for r in gt["all_records"] if r.get("expiry")]
    if not expiries:
        return 0
    latest = datetime.fromisoformat(max(expiries)).date()
    target = date.today() - timedelta(days=margin_days)
    return (target - latest).days


def shift(day: str | None, days: int) -> str | None:
    if not day:
        return None
    from datetime import datetime, timedelta
    d = datetime.fromisoformat(day) + timedelta(days=days)
    return d.strftime("%Y-%m-%d")


def derive_policy(gt: dict) -> dict:
    """deny_if_any per provision, from violating cases minus record premises."""
    mitigators: dict[str, set[str]] = {}
    for r in gt["all_records"]:
        for p in r["prov"]:
            mitigators.setdefault(p, set()).update(r.get("premise") or [])

    triggers: dict[str, set[str]] = {}
    for c in gt["cases"]:
        if not c["violation"]:
            continue
        for p in c["prov"]:
            if p == CONTROL_PLANE:
                continue
            triggers.setdefault(p, set()).update(c["factors"])
    return {p: sorted(fs - mitigators.get(p, set()) - {"compliant"})
            for p, fs in triggers.items()}


def build_rulebook(gt: dict, policy: dict, org: str | None = None) -> dict:
    provisions = []
    for pid, meta in gt["provisions"].items():
        if pid == CONTROL_PLANE:
            continue
        deny = policy.get(pid, [])
        provisions.append({
            "provision_id": pid,
            "absolute": bool(meta["absolute"]),
            "text": meta["text"],
            # A provision no violating case ever engaged gets an empty
            # predicate: it is in the constitution and permits on these facts.
            "policy": {"deny_if_any": deny},
            "organization": org,
        })
    return {"provisions": sorted(provisions,
                                 key=lambda p: p["provision_id"])}


def build_store(gt: dict, offset: int = 0, org: str | None = None) -> dict:
    records = []
    for r in gt["all_records"]:
        tier, principal = AUTH[r["auth"]]
        scope_name = r.get("scope") or "org"
        is_acceptance = r["interp"] == "accept_risk"
        rec = {
            "seed_id": r["rid"],
            "provision_id": r["prov"][0],
            "tier": tier,
            "resolving_principal": principal,
            "resolved_at": iso(shift(r["ts"], offset)),
            "facts": sorted(r["facts"]),
            "premise": sorted(r.get("premise") or []),
            "interpretation": {"outcome": r["interp"]},
            "conditions": ({"note": r["conditions"]}
                           if r.get("conditions") else None),
            "scope": {} if scope_name == "org" else {"service": scope_name},
            "scope_level": "org" if scope_name == "org" else "service",
            "rationale": r["rationale_text"],
            "is_acceptance": is_acceptance,
            "expiry": iso(shift(r.get("expiry"), offset)),
            "organization": org,
        }
        if r.get("referral_status") == "rejected":
            rec["referral_outcome"] = "rejected"
        records.append(rec)
    return {"records": records}


def build_cases(gt: dict, org: str | None = None) -> list[dict]:
    out = []
    for c in gt["cases"]:
        g = c["ground_truth"]
        out.append({
            "id": c["id"],
            "organization": org,
            "category": c["category"],
            "author": c["author"],
            "domain": c.get("domain") or "org",
            "description": c["desc"],
            "provisions": list(c["prov"]),
            "factors": sorted(c["factors"]),
            "violation": bool(c["violation"]),
            # A social input in the original, preserved as one here: how far
            # somebody actually pushed back. It is not a model output.
            "contest_to": int(c["contest_to"]),
            "expect": {
                "route": g["route"],
                "tier1_decision": g.get("tier1_decision"),
                "final_decision": g["final_decision"],
                "final_tier": g["final_tier"],
                "controlling": g.get("controlling"),
                "stored": bool(g.get("stored")),
            },
        })
    return out


def verify(gt: dict, policy: dict) -> list[str]:
    """The derived predicate must reproduce the original's tier-1 call."""
    problems = []
    for c in gt["cases"]:
        if c["ground_truth"]["route"] != "adjudicate":
            continue
        facts = set(c["factors"])
        fired = any(set(policy.get(p, [])) & facts for p in c["prov"]
                    if p != CONTROL_PLANE)
        if fired != c["violation"]:
            problems.append(
                f"{c['id']} ({c['category']}): predicate fired={fired} but the"
                f" original recorded violation={c['violation']}")
    return problems


def build_multitenant(index: list[dict]) -> None:
    """Fuse the per-company packs into one multi-tenant corpus.

    Every company keeps its own constitution — the provisions are simply
    carried into one rulebook, each tagged with the tenant that owns it. That
    is safe here and only here because the provision namespaces are disjoint
    (SC-, VP-, DV-, FL-), which is the property that keeps retrieval
    tenant-safe without filtering the hot path: retrieval is keyed by
    provision_id, so one tenant's holding can never surface as a candidate
    for another's case. `verify_namespaces` refuses to build if that ever
    stops being true.
    """
    d = os.path.join(OUT, "_all")
    os.makedirs(d, exist_ok=True)
    provisions, records, cases, orgs = [], [], [], []
    owner: dict[str, str] = {}

    for entry in index:
        key = entry["key"]
        src = os.path.join(OUT, key)
        rb = json.load(open(os.path.join(src, "rulebook.json")))
        st = json.load(open(os.path.join(src, "store_seed.json")))
        cs = json.load(open(os.path.join(src, "cases.json")))

        for prov in rb["provisions"]:
            pid = prov["provision_id"]
            if pid in owner:
                raise SystemExit(
                    f"provision {pid} is claimed by both {owner[pid]} and"
                    f" {key}; the multi-tenant pack cannot be built safely")
            owner[pid] = key
            provisions.append({**prov, "organization": key})

        for r in st["records"]:
            records.append({**r, "organization": key,
                            "seed_id": f"{key}:{r['seed_id']}"})
        for c in cs["cases"]:
            cases.append({**c, "organization": key,
                          "id": f"{key}:{c['id']}"})

        orgs.append({
            "org_id": key, "name": entry["display_name"],
            # Each tenant gets its own officers. The risk owner of one
            # company must not be able to close another company's docket,
            # which is a property of the principal, not of the screen.
            # A full cast per tenant, because the point of the demo is that
            # the same docket affords different powers to different people.
            # One of each is the minimum needed to walk all four desks
            # without ever signing in as a platform account.
            "principals": cast_for(key),
        })

    json.dump({"provisions": sorted(provisions,
                                    key=lambda p: p["provision_id"])},
              open(os.path.join(d, "rulebook.json"), "w"), indent=1)
    json.dump({"records": records},
              open(os.path.join(d, "store_seed.json"), "w"), indent=1)
    orgs.append({"org_id": None, "name": "Platform",
                 "principals": PLATFORM_STAFF})
    json.dump({"organizations": [o for o in orgs if o["org_id"]]
               + [o for o in orgs if not o["org_id"]],
               "founding_scope": index[0]["key"]},
              open(os.path.join(d, "organizations.json"), "w"), indent=1)
    json.dump({"company": "_all", "display_name": "All tenants",
               "multi_tenant": True,
               "organizations": [o["org_id"] for o in orgs],
               "provenance": "the four converted case-study corpora fused"
                             " into one multi-tenant ledger; provision"
                             " namespaces verified disjoint",
               "cases": cases},
              open(os.path.join(d, "cases.json"), "w"), indent=1)
    print(f"  {'_all':12s} multi-tenant: {len(orgs)} tenants,"
          f" {len(provisions)} provisions, {len(records)} records,"
          f" {len(cases)} cases — namespaces disjoint")


def cast_for(key: str) -> list[dict]:
    """One officer per desk, so ANY demo — a single company or all four —
    can be walked end to end without signing in as a platform account."""
    return [
        {"principal_id": f"{key}.risk", "branch": "risk_owner",
         "key": f"devkey-{key}-risk", "kind": "human",
         "role": "risk owner", "desk": "/review"},
        {"principal_id": f"{key}.grc", "branch": "lawmakers",
         "key": f"devkey-{key}-grc", "kind": "human",
         "role": "GRC council", "desk": "/review/amendments"},
        {"principal_id": f"{key}.eng", "branch": None,
         "key": f"devkey-{key}-eng", "kind": "human",
         "role": "engineer", "desk": "/review/changes"},
        {"principal_id": f"{key}.audit", "branch": None,
         "key": f"devkey-{key}-audit", "kind": "human",
         "role": "auditor", "desk": "/review/ledger"},
    ]


# Unscoped, therefore platform-wide: they read every tenant and decide
# nothing. Written into every pack so there is always somebody who can see
# across tenants without holding authority over any of them.
# EXACTLY ONE unscoped human. Cross-tenant visibility is the one privilege
# that cannot be granted by a branch — it is the absence of a tenant — so it
# is deliberately held by a single account that holds no branch at all: it
# reads every tenant and can decide nothing in any of them.
PLATFORM_STAFF = [
    {"principal_id": "platform.admin", "branch": None,
     "key": "devkey-platform-admin", "kind": "human",
     "role": "platform administrator — the only account that reads across"
             " tenants, and it decides nothing"},
]


def acc0(store: dict) -> int:
    return sum(1 for r in store["records"] if r["is_acceptance"])


def main() -> int:
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(OUT, exist_ok=True)
    total_problems = 0
    index = []

    for key, display in COMPANIES.items():
        path = os.path.join(src, f"groundtruth_{key}.json")
        if not os.path.exists(path):
            print(f"  skip {key}: {path} not found")
            continue
        gt = json.load(open(path))
        policy = derive_policy(gt)
        problems = verify(gt, policy)
        total_problems += len(problems)

        d = os.path.join(OUT, key)
        os.makedirs(d, exist_ok=True)
        offset = anchor_offset(gt)
        # A single company is a tenant too. Tagging its constitution,
        # jurisprudence and cases means a one-company demo exercises the same
        # tenancy the four-company one does, instead of quietly running
        # everything as platform-wide.
        rulebook = build_rulebook(gt, policy, key)
        store = build_store(gt, offset, key)
        cases = build_cases(gt, key)

        json.dump(rulebook, open(os.path.join(d, "rulebook.json"), "w"),
                  indent=1)
        json.dump(store, open(os.path.join(d, "store_seed.json"), "w"),
                  indent=1)
        # The corpus is a SEQUENCE: 15 records existed at the first case and
        # the rest were created by the run itself. Seeding all of them up
        # front is convenient (every mechanism is demonstrable immediately,
        # including lapse and the renewal bar) but slightly anachronistic —
        # an early case can be controlled by a record the original narrative
        # created later. Both stores are emitted so the choice is the
        # operator's and the trade-off is visible.
        initial_ids = set(gt["cases"][0]["store_before"])
        initial = {"records": [r for r in store["records"]
                               if r["seed_id"] in initial_ids]}
        json.dump(initial,
                  open(os.path.join(d, "store_seed_initial.json"), "w"),
                  indent=1)
        anachronistic = sorted(
            c["id"] for c in gt["cases"]
            if c["ground_truth"].get("controlling")
            and c["ground_truth"]["controlling"] not in initial_ids)
        json.dump({"company": key, "display_name": display,
                   "theta": gt["theta"], "k": gt["k"],
                   "source": f"groundtruth_{key}.json",
                   "date_offset_days": offset,
                   "store_initial": len(initial["records"]),
                   "store_created_during_original_run":
                       len(store["records"]) - len(initial["records"]),
                   "anachronism_note":
                       "store_seed.json seeds the full post-run store."
                       " These cases were controlled by a record the original"
                       " run created later, so they may resolve differently"
                       " than the corpus records; DJ_SEED_STORE="
                       "store_seed_initial.json avoids this at the cost of"
                       " needing the run to regrow the store.",
                   "anachronism_cases": anachronistic,
                   "date_offset_note": "every record timestamp and expiry is"
                                       " shifted by this constant so the"
                                       " corpus's own lapse state is"
                                       " reproduced against the clock;"
                                       " relative order is unchanged",
                   "provenance": "converted from the Paper-3 simulation;"
                                 " deny predicates derived and verified,"
                                 " engagement and contest depth replayed as"
                                 " declared scenario properties",
                   "cases": cases},
                  open(os.path.join(d, "cases.json"), "w"), indent=1)

        json.dump({"organizations": [
            {"org_id": key, "name": display, "principals": cast_for(key)},
            # Separate entry, no org_id: these principals must be UNSCOPED or
            # they inherit the tenant and can no longer see across tenants.
            {"org_id": None, "name": "Platform",
             "principals": PLATFORM_STAFF}],
            # The bootstrap ceremony accounts are scoped like anybody else.
            # They exist because the founding grants need a granter, not
            # because anyone should operate from them; leaving them unscoped
            # would quietly create more cross-tenant accounts than intended.
            "founding_scope": key},
            open(os.path.join(d, "organizations.json"), "w"), indent=1)

        acc = sum(1 for r in store["records"] if r["is_acceptance"])
        exp = sum(1 for r in store["records"] if r["expiry"])
        lapsed = sum(1 for r in store["records"]
                     if r["expiry"] and r["expiry"][:10] < str(__import__("datetime").date.today()))
        print(f"  {key:12s} offset {offset:+5d}d, {lapsed}/{acc0(store)}"
              f" acceptances now lapsed")
        print(f"  {'':12s} {len(rulebook['provisions']):2d} provisions,"
              f" {len(store['records'])} records ({acc} acceptances,"
              f" {exp} with expiry), {len(cases)} cases"
              + (f"  — {len(problems)} PREDICATE MISMATCHES" if problems
                 else "  — predicate verified on every case"))
        for p in problems[:5]:
            print(f"      ! {p}")
        index.append({"key": key, "display_name": display,
                      "provisions": len(rulebook["provisions"]),
                      "records": len(store["records"]),
                      "cases": len(cases)})

    json.dump({"companies": index}, open(os.path.join(OUT, "index.json"), "w"),
              indent=1)
    if len(index) > 1:
        build_multitenant(index)
    if total_problems:
        print(f"\nFAILED: {total_problems} cases where the derived predicate"
              f" disagrees with the original's own tier-1 decision.")
        return 1
    print("\nAll packs built; the derived predicate reproduces the original"
          " tier-1 decision on every adjudicated case.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
