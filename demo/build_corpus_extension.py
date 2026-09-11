#!/usr/bin/env python3
"""Extend the four demo packs with the Absolute Rules Corpus.

Source: seed/absolute_rules_corpus.json (Absolute Rules Corpus v0.1,
Digital Judiciary Research Program) and docs/ABSOLUTE_RULES_CORPUS.md
(the four-criterion absoluteness test). Each company gains eight
corpus-derived provisions — three absolute (corpus strictness 4/4:
EU AI Act Art. 5(1)(b), Art. 5(1)(e), GDPR Art. 7(3)) and five
statute-tier (Art. 5(1)(f), Art. 50(1), GDPR Art. 9(1), Art. 33(1)/
NIS2 Art. 23(4), NIST IA-2/SC-8) — three seed holdings, and a
26-case ladder that exercises the statute/absolute asymmetry:
absolutes short-circuit (A6) and cannot be risk-accepted; statutes
adjudicate, distinguish, and may be risk-accepted at tier k.

The corpus classification IS the `absolute` flag: a clause enters as
absolute only if it passed all four corpus criteria (derogation-free,
determinate conduct, transposition-invariant, context-independent
bindingness). Everything else — proportionality-scoped, exception-
carrying, transposition-dependent, or attachment-bound — enters as an
adjudicable provision, because somebody inside the company lawfully
holds the authority to decide the marginal case.

Idempotent: refuses to apply twice. After running, rebuild demos with
demo/reset.py. Applies to the four Paper-3 packs, then re-fuses _all.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PACKS = os.path.join(HERE, "companies")
CORPUS = os.path.join(ROOT, "seed", "absolute_rules_corpus.json")

COMPANIES = {
    "sctower": {
        "pfx": "SC", "base": 230, "seed_pfx": "SP", "seed_base": 40,
        "flavor": {
            0: ("portal", "Shipper-portal 'smart nudge' engine tuned on"
                          " small-shipper financial distress signals"),
            1: ("screening", "Warehouse CCTV harvester feeding a"
                             " facial-recognition gallery of drivers"),
            2: ("portal", "Marketing-consent withdrawal flow in the shipper"
                          " portal"),
            3: ("telematics", "Driver-cab camera emotion/fatigue inference"),
            4: ("portal", "Shipper-portal booking chatbot"),
            5: ("customs", "Broker-license health-exemption records in the"
                           " customs filing path"),
            6: ("alerting", "Tenant-breach notification pipeline"),
            7: ("edi", "Carrier EDI endpoint authentication"),
        },
    },
    "vetpoc": {
        "pfx": "VP", "base": 130, "seed_pfx": "PR", "seed_base": 40,
        "flavor": {
            0: ("billing", "Payment-plan upsell prompts targeted at"
                           " financially distressed owners at euthanasia"
                           " decision points"),
            1: ("records", "Clinic lobby camera importer feeding a"
                           " client facial-recognition gallery"),
            2: ("portal", "Owner marketing/reminder consent withdrawal flow"),
            3: ("staffing", "Break-room camera emotion inference on clinic"
                            " staff"),
            4: ("triage", "After-hours triage chatbot"),
            5: ("records", "Staff biometric time-clock and health-record"
                           " fields"),
            6: ("alerting", "Client-data breach notification pipeline"),
            7: ("dispensing", "Dispensing-station shared logins"),
        },
    },
    "dcvigil": {
        "pfx": "DV", "base": 330, "seed_pfx": "DP", "seed_base": 40,
        "flavor": {
            0: ("portal", "Capacity-upsell nudges tuned on customer outage"
                          " panic signals"),
            1: ("ingestion", "Perimeter CCTV scraper enrolling visitors"
                             " into a facial-recognition gallery"),
            2: ("telemetry", "Operator telemetry consent withdrawal path"),
            3: ("alerting", "NOC operator fatigue/emotion inference from"
                            " console cameras"),
            4: ("portal", "Customer status-page assistant"),
            5: ("access", "Badge-system biometric templates in the access"
                          " analytics path"),
            6: ("alerting", "CSIRT early-warning (24h) notification"
                            " pipeline"),
            7: ("ingestion", "Collector fleet authentication"),
        },
    },
    "frontierllm": {
        "pfx": "FL", "base": 430, "seed_pfx": "FP", "seed_base": 40,
        "flavor": {
            0: ("serving", "Engagement-maximizing fine-tune targeting"
                           " vulnerable-user cohorts"),
            1: ("data", "Untargeted web/CCTV face-image crawler for a"
                        " recognition training set"),
            2: ("gateway", "User training-data consent withdrawal endpoint"),
            3: ("staffing", "Annotator webcam emotion/wellbeing inference"),
            4: ("serving", "Consumer assistant AI-disclosure banner"),
            5: ("data", "Special-category (health/orientation) records in a"
                        " new training corpus path"),
            6: ("alerting", "Model-incident regulator notification"
                            " pipeline"),
            7: ("training", "Cluster access authentication"),
        },
    },
}

# (slot, absolute, corpus_ids, text, policy)
PROVISIONS = [
    (0, True,
     ["EU-AIACT-A5.1.b"],
     "No change may ship, tune, or enable an AI feature that exploits"
     " vulnerabilities of age, disability, or a specific social or economic"
     " situation to materially distort a person's behaviour. (EU AI Act"
     " Art. 5(1)(b) floor — corpus EU-AIACT-A5.1.b, absolute, strictness"
     " 4/4: no derogation exists and no officer holds authority to accept"
     " this risk.)",
     {"deny_if_any": ["vulnerability_targeting", "behavioral_distortion"]}),
    (1, True,
     ["EU-AIACT-A5.1.e"],
     "No change may create or expand a facial-recognition database through"
     " untargeted scraping of facial images from the internet or CCTV"
     " footage. (EU AI Act Art. 5(1)(e) floor — corpus EU-AIACT-A5.1.e,"
     " absolute, strictness 4/4.)",
     {"deny_if_any": ["untargeted_scraping", "facial_db_expansion"]}),
    (2, True,
     ["EU-GDPR-A7.3"],
     "Consent withdrawal must remain available at any time and as easy as"
     " giving consent; no change may add friction, delay, approval steps,"
     " or dark patterns to a withdrawal path, or remove one. (GDPR"
     " Art. 7(3) floor — corpus EU-GDPR-A7.3, absolute: outside the"
     " Art. 23 restriction list, all four corpus criteria pass.)",
     {"deny_if_any": ["withdrawal_friction", "withdrawal_path_removed"]}),
    (3, False,
     ["EU-AIACT-A5.1.f"],
     "No AI inference of emotions of a natural person in workplace"
     " contexts; the Art. 5(1)(f) medical/safety exception requires a"
     " documented justification and a completed DPIA. (EU AI Act"
     " Art. 5(1)(f) — corpus EU-AIACT-A5.1.f, statute: the medical/safety"
     " carve-out fails the derogation-free criterion, so the marginal case"
     " is adjudicable.)",
     {"deny_if_any": ["emotion_inference", "workplace_context"]}),
    (4, False,
     ["EU-AIACT-A50.1"],
     "Natural persons must be informed they are interacting with an AI"
     " system unless this is obvious to a reasonably well-informed person."
     " (EU AI Act Art. 50(1) — corpus EU-AIACT-A50.1, statute: the"
     " obviousness proviso and law-enforcement exception fail the"
     " derogation-free criterion.)",
     {"deny_if_any": ["undisclosed_ai_interaction"]}),
    (5, False,
     ["EU-GDPR-A9.1"],
     "Special-category personal data (health, biometric-for-ID, orientation,"
     " beliefs) may not enter a new processing path without a documented"
     " GDPR Art. 9(2) gate. (GDPR Art. 9(1) — corpus EU-GDPR-A9.1, statute:"
     " ten enumerated derogations in Art. 9(2), so the gate question is"
     " adjudicable.)",
     {"deny_if_any": ["special_category_data", "new_processing_path"]}),
    (6, False,
     ["EU-GDPR-A33.1", "EU-NIS2-A23.4.a"],
     "No change may remove, disable, or add delay to the supervisory-"
     "notification path (GDPR Art. 33(1) 72h; NIS2 Art. 23(4) 24h early"
     " warning). (Corpus EU-GDPR-A33.1 and EU-NIS2-A23.4.a, statute: the"
     " low-risk dispensation and 'where feasible' hedge fail determinacy;"
     " the NIS2 deadline fails transposition-invariance.)",
     {"deny_if_any": ["notification_delay_path", "breach_pipeline_removal"]}),
    (7, False,
     ["US-NIST80053-IA-2", "US-NIST80053-SC-8"],
     "Every service and operator access path must uniquely identify and"
     " authenticate its principal, and protect transmission"
     " confidentiality; no shared accounts, unauthenticated endpoints, or"
     " plaintext transport. (NIST SP 800-53 IA-2 / SC-8 — corpus"
     " US-NIST80053-IA-2 and -SC-8, statute: framework guidance binding via"
     " contractual attachment, tailorable, so compensating controls are"
     " adjudicable.)",
     {"deny_if_any": ["shared_account_path", "unauthenticated_endpoint",
                      "plaintext_transmission"]}),
]

# Seed holdings: (slot, seed_slot, facts, premise, outcome, cond_note,
#                 rationale)
SEEDS = [
    (3, 0,
     ["emotion_inference", "workplace_context",
      "medical_safety_justification", "dpia_complete"],
     ["medical_safety_justification", "dpia_complete"],
     "permit_conditional",
     "safety-monitoring scope only; DPIA on file; annual re-justification",
     "Art. 5(1)(f) excepts systems put in place for medical or safety"
     " reasons; a documented safety justification with a completed DPIA is"
     " precisely the carve-out the corpus records as the reason this clause"
     " is statute-tier rather than absolute."),
    (4, 1,
     ["undisclosed_ai_interaction", "obvious_ai_context",
      "ux_review_complete"],
     ["obvious_ai_context", "ux_review_complete"],
     "permit_conditional",
     "obviousness finding documented by UX review; re-test on major redesign",
     "Art. 50(1) applies 'unless this is obvious from the point of view of"
     " a reasonably well-informed person'; a documented obviousness finding"
     " is the proviso working as written."),
    (5, 2,
     ["special_category_data", "new_processing_path",
      "explicit_consent_documented", "purpose_limited"],
     ["explicit_consent_documented", "purpose_limited"],
     "permit_conditional",
     "Art. 9(2)(a) gate: explicit consent recorded per purpose; audit"
     " annually",
     "Art. 9(1) is a prohibition with ten derogations; documented explicit"
     " consent for a limited purpose satisfies the Art. 9(2)(a) gate."),
]


def prov_id(co: dict, slot: int) -> str:
    return f"{co['pfx']}-{co['base'] + slot}"


def seed_id(co: dict, seed_slot: int) -> str:
    return f"{co['seed_pfx']}-{co['seed_base'] + seed_slot:03d}"


def expect(route, t1, final, tier, controlling=None, stored=False):
    return {"route": route, "tier1_decision": t1, "final_decision": final,
            "final_tier": tier, "controlling": controlling, "stored": stored}


def build_cases(key: str, co: dict) -> list[dict]:
    """The 26-case ladder. Case ids RC01..RC26, appended after the pack's
    existing cases; per-provision order ends with the risk-acceptance case
    so a stored acceptance cannot shadow an earlier scenario."""
    n = [0]

    def case(slot, category, author, desc, factors, violation, contest,
             exp):
        n[0] += 1
        return {"id": f"RC{n[0]:02d}", "organization": key,
                "category": category, "author": author,
                "domain": co["flavor"][slot][0],
                "description": f"{co['flavor'][slot][1]} — {desc}",
                "provisions": [prov_id(co, slot)], "factors": sorted(factors),
                "violation": violation, "contest_to": contest,
                "expect": exp, "corpus_refs": PROVISIONS[slot][2]}

    A = "agent:codegen-1"
    A2 = "agent:codegen-2"
    H = "human:backend"
    cases = []

    # --- absolutes: compliant / violation (contested) / violation variant
    for slot, vf in ((0, ["vulnerability_targeting",
                          "behavioral_distortion", "growth_experiment"]),
                     (1, ["untargeted_scraping", "facial_db_expansion"]),
                     (2, ["withdrawal_friction", "retention_experiment"])):
        pid = prov_id(co, slot)
        # A compliant change cites NO provision: an absolute short-circuits
        # any case filed under it (A6 — "nothing to adjudicate"), so the
        # clean variant is clean precisely because it implicates nothing.
        clean = case(
            slot, "A-routine", A,
            "reworked with the prohibited pattern removed; implicates no"
            " provision",
            ["compliant"], False, 1,
            expect("adjudicate", "permit", "permit", 1))
        clean["provisions"] = []
        cases.append(clean)
        cases.append(case(
            slot, "F-absolute", A2,
            f"lands the prohibited pattern; {pid} is an absolute floor —"
            " A6 short-circuit, contested and refused (no escalation path"
            " from an absolute)",
            vf, True, 2,
            expect("absolute_deny", "deny", "deny", 1)))
        variant = {0: ["vulnerability_targeting"],
                   1: ["facial_db_expansion", "backfill_job"],
                   2: ["withdrawal_path_removed"]}[slot]
        cases.append(case(
            slot, "F-absolute", H,
            "second attempt via a narrower path; the floor does not narrow",
            variant, True, 1,
            expect("absolute_deny", "deny", "deny", 1)))

    # --- slot 3: emotion inference (statute) A/B/C/E
    s3 = seed_id(co, 0)
    cases.append(case(3, "A-routine", A,
                      "camera pipeline refactor, inference disabled;"
                      " corpus-clean",
                      ["compliant"], False, 1,
                      expect("adjudicate", "permit", "permit", 1)))
    cases.append(case(3, "B-plain-deny", A2,
                      "productivity-analytics build with no medical or"
                      " safety justification",
                      ["emotion_inference", "workplace_context",
                       "productivity_analytics"], True, 1,
                      expect("adjudicate", "deny", "deny", 1)))
    cases.append(case(3, "C-precedent", A,
                      "fatigue-safety monitor with documented safety"
                      f" justification and DPIA — {s3} controls",
                      ["emotion_inference", "workplace_context",
                       "medical_safety_justification", "dpia_complete"],
                      True, 1,
                      expect("adjudicate", "permit_conditional",
                             "permit_conditional", 1, controlling=s3)))
    cases.append(case(3, "E-distinguish", A2,
                      "safety justification claimed but the DPIA was never"
                      f" completed — {s3} distinguished; deny",
                      ["emotion_inference", "workplace_context",
                       "medical_safety_justification"], True, 1,
                      expect("adjudicate", "deny", "deny", 1)))

    # --- slot 4: AI disclosure (statute) A/B/C
    s4 = seed_id(co, 1)
    cases.append(case(4, "A-routine", A,
                      "adds the 'AI assistant' disclosure banner;"
                      " corpus-clean",
                      ["compliant"], False, 1,
                      expect("adjudicate", "permit", "permit", 1)))
    cases.append(case(4, "B-plain-deny", A2,
                      "ships a human-persona voice with no disclosure",
                      ["undisclosed_ai_interaction", "customer_facing"],
                      True, 1,
                      expect("adjudicate", "deny", "deny", 1)))
    cases.append(case(4, "C-precedent", H,
                      "internal tool where AI interaction is obvious and"
                      f" UX-documented — {s4} controls",
                      ["undisclosed_ai_interaction", "obvious_ai_context",
                       "ux_review_complete"], True, 1,
                      expect("adjudicate", "permit_conditional",
                             "permit_conditional", 1, controlling=s4)))

    # --- slot 5: special-category data (statute) A/B/C/E
    s5 = seed_id(co, 2)
    cases.append(case(5, "A-routine", A,
                      "schema change with special-category fields dropped;"
                      " corpus-clean",
                      ["compliant"], False, 1,
                      expect("adjudicate", "permit", "permit", 1)))
    cases.append(case(5, "B-plain-deny", A2,
                      "new pipeline ingests the data with no Art. 9(2)"
                      " gate",
                      ["special_category_data", "new_processing_path",
                       "analytics_enrichment"], True, 1,
                      expect("adjudicate", "deny", "deny", 1)))
    cases.append(case(5, "C-precedent", A,
                      "explicit consent recorded, purpose-limited —"
                      f" Art. 9(2)(a) gate; {s5} controls",
                      ["special_category_data", "new_processing_path",
                       "explicit_consent_documented", "purpose_limited"],
                      True, 1,
                      expect("adjudicate", "permit_conditional",
                             "permit_conditional", 1, controlling=s5)))
    cases.append(case(5, "E-distinguish", A2,
                      "consent captured but the purpose limitation was"
                      f" dropped in review — {s5} distinguished; deny",
                      ["special_category_data", "new_processing_path",
                       "explicit_consent_documented"], True, 1,
                      expect("adjudicate", "deny", "deny", 1)))

    # --- slot 6: notification path (statute) A/B/G
    cases.append(case(6, "A-routine", A,
                      "notification pipeline hardened, deadlines intact;"
                      " corpus-clean",
                      ["compliant"], False, 1,
                      expect("adjudicate", "permit", "permit", 1)))
    cases.append(case(6, "B-plain-deny", A2,
                      "batching change quietly moves notification outside"
                      " the deadline window",
                      ["notification_delay_path", "batch_optimization"],
                      True, 1,
                      expect("adjudicate", "deny", "deny", 1)))
    cases.append(case(6, "G-riskowner", H,
                      "migration forces a 48h notification-path outage;"
                      " statute-tier clause, so the risk owner may accept"
                      " what an absolute would refuse",
                      ["notification_delay_path", "vendor_outage",
                       "migration_window"], True, 4,
                      expect("adjudicate", "deny", "accept_risk", 4,
                             stored=True)))

    # --- slot 7: authentication/transmission (statute) A/B/G
    cases.append(case(7, "A-routine", A,
                      "rotates credentials onto per-service identities;"
                      " corpus-clean",
                      ["compliant"], False, 1,
                      expect("adjudicate", "permit", "permit", 1)))
    cases.append(case(7, "B-plain-deny", A2,
                      "debug build exposes an unauthenticated plaintext"
                      " endpoint",
                      ["unauthenticated_endpoint", "plaintext_transmission"],
                      True, 1,
                      expect("adjudicate", "deny", "deny", 1)))
    cases.append(case(7, "G-riskowner", H,
                      "incident break-glass shared account, time-boxed;"
                      " NIST-tier guidance admits compensating controls",
                      ["shared_account_path", "break_glass_incident"],
                      True, 4,
                      expect("adjudicate", "deny", "accept_risk", 4,
                             stored=True)))
    return cases


def build_provisions(key: str, co: dict) -> list[dict]:
    return [{"provision_id": prov_id(co, slot), "absolute": absolute,
             "text": text, "policy": policy, "organization": key}
            for slot, absolute, _refs, text, policy in PROVISIONS]


def build_seeds(key: str, co: dict) -> list[dict]:
    out = []
    for slot, seed_slot, facts, premise, outcome, cond, rationale in SEEDS:
        out.append({
            "seed_id": seed_id(co, seed_slot),
            "provision_id": prov_id(co, slot),
            "tier": 2, "resolving_principal": "svc:tier2",
            "resolved_at": "2025-07-15T00:00:00.000000+00:00",
            "facts": sorted(facts), "premise": sorted(premise),
            "interpretation": {"outcome": outcome},
            "conditions": {"note": cond},
            "scope": {}, "scope_level": "org",
            "rationale": rationale,
            "is_acceptance": False, "expiry": None,
            "organization": key,
        })
    return out


def apply_company(key: str) -> dict:
    co = COMPANIES[key]
    d = os.path.join(PACKS, key)
    rb = json.load(open(os.path.join(d, "rulebook.json")))
    if any(p["provision_id"] == prov_id(co, 0) for p in rb["provisions"]):
        raise SystemExit(f"  {key}: corpus extension already applied"
                         f" ({prov_id(co, 0)} present); nothing to do")
    st = json.load(open(os.path.join(d, "store_seed.json")))
    cs = json.load(open(os.path.join(d, "cases.json")))

    provs = build_provisions(key, co)
    seeds = build_seeds(key, co)
    cases = build_cases(key, co)

    rb["provisions"].extend(provs)
    st["records"].extend(seeds)
    cs["cases"].extend(cases)
    cs["store_initial"] = cs.get("store_initial", 0) + len(seeds)
    cs["corpus_extension"] = {
        "source": "seed/absolute_rules_corpus.json (Absolute Rules Corpus"
                  " v0.1); schema in docs/ABSOLUTE_RULES_CORPUS.md",
        "provisions": [p["provision_id"] for p in provs],
        "absolutes": [p["provision_id"] for p in provs if p["absolute"]],
        "note": "absolute == the corpus clause passed all four absoluteness"
                " criteria; statute-tier clauses enter as adjudicable"
                " provisions because a lawful exception-holder exists",
    }

    json.dump(rb, open(os.path.join(d, "rulebook.json"), "w"), indent=1)
    json.dump(st, open(os.path.join(d, "store_seed.json"), "w"), indent=1)
    json.dump(cs, open(os.path.join(d, "cases.json"), "w"), indent=1)

    # store_seed_initial.json is "the store as of the first case"; corpus
    # seeds predate the replay, so they belong there too.
    p0 = os.path.join(d, "store_seed_initial.json")
    if os.path.exists(p0):
        st0 = json.load(open(p0))
        st0["records"].extend(seeds)
        json.dump(st0, open(p0, "w"), indent=1)

    return {"provisions": len(provs), "records": len(seeds),
            "cases": len(cases)}


def refuse_all_pack(added: dict) -> None:
    """Append the fused view to _all, mirroring build_packs.build_multitenant:
    provisions tagged with owner, seed ids and case ids namespaced."""
    d = os.path.join(PACKS, "_all")
    rb = json.load(open(os.path.join(d, "rulebook.json")))
    st = json.load(open(os.path.join(d, "store_seed.json")))
    cs = json.load(open(os.path.join(d, "cases.json")))
    have = {p["provision_id"] for p in rb["provisions"]}
    for key in COMPANIES:
        src = os.path.join(PACKS, key)
        rb_c = json.load(open(os.path.join(src, "rulebook.json")))
        st_c = json.load(open(os.path.join(src, "store_seed.json")))
        cs_c = json.load(open(os.path.join(src, "cases.json")))
        pids = set(cs_c["corpus_extension"]["provisions"])
        for p in rb_c["provisions"]:
            if p["provision_id"] in pids and p["provision_id"] not in have:
                rb["provisions"].append({**p, "organization": key})
        seed_ids = {s["seed_id"] for s in build_seeds(key, COMPANIES[key])}
        for r in st_c["records"]:
            if r["seed_id"] in seed_ids:
                st["records"].append({**r, "organization": key,
                                      "seed_id": f"{key}:{r['seed_id']}"})
        for c in cs_c["cases"]:
            if c["id"].startswith("RC"):
                cs["cases"].append({**c, "organization": key,
                                    "id": f"{key}:{c['id']}"})
    rb["provisions"].sort(key=lambda p: p["provision_id"])
    json.dump(rb, open(os.path.join(d, "rulebook.json"), "w"), indent=1)
    json.dump(st, open(os.path.join(d, "store_seed.json"), "w"), indent=1)
    json.dump(cs, open(os.path.join(d, "cases.json"), "w"), indent=1)


def main() -> int:
    if not os.path.exists(CORPUS):
        print("seed/absolute_rules_corpus.json missing", file=sys.stderr)
        return 2
    corpus = json.load(open(CORPUS))
    by_id = {e["id"]: e for e in corpus["entries"]}
    # Sanity: every cited corpus clause exists and its classification
    # matches the absolute flag we assign.
    for slot, absolute, refs, _t, _p in PROVISIONS:
        for r in refs:
            e = by_id[r]
            if absolute:
                assert e["classification"] == "absolute", (r, slot)
            else:
                assert e["classification"] == "statute", (r, slot)

    totals = {}
    for key in COMPANIES:
        totals[key] = apply_company(key)
        print(f"  {key:12s} +{totals[key]['provisions']} provisions"
              f" +{totals[key]['records']} seed records"
              f" +{totals[key]['cases']} cases")
    refuse_all_pack(totals)
    print("  _all         re-fused with the corpus extension")

    idx_path = os.path.join(PACKS, "index.json")
    idx = json.load(open(idx_path))
    for entry in idx["companies"]:
        t = totals.get(entry["key"])
        if t:
            entry["provisions"] += t["provisions"]
            entry["records"] += t["records"]
            entry["cases"] += t["cases"]
    json.dump(idx, open(idx_path, "w"), indent=1)
    print("  index.json   counts updated")
    print("\n  now rebuild the demo ledgers: python3 demo/reset.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
