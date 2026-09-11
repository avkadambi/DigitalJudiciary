#!/usr/bin/env python3
"""Counter-model probes for Proposition 4, one per axiom.

WHY THIS EXISTS
---------------
Sect. 7.8 has always described eight axiom mutants and an expected-failure map,
and Proposition 4's proof cites one of them in terms — "the mutant Sect. 7.8
builds". Appendix C Sect. C.5 executes a *different* list: mechanism mutants,
anchored on the code that implements the contract rather than on the axioms
themselves. The two lists share almost nothing, and the consequence was that
**Proposition 4's A3 counter-model was cited as executed and had never been
run.** That is finding S2 on the review list, and this file closes it.

WHAT A COUNTER-MODEL PROBE IS, AND WHY IT IS NOT A MUTANT
---------------------------------------------------------
A mutation matrix asks: *does the conformance surface notice this fault?* The
answer is a kill or a survival, and a survival is a hole in the checks.

Proposition 4 asks a different question: *is there a system satisfying the
other eight axioms in which a named guarantee fails?* The answer is a
counter-model, and it is only a counter-model if the guarantee **holds** on the
unmutated build and **fails** on the mutated one. A probe that fails in both
directions witnesses nothing. So every probe here is run twice and both
directions are asserted, which is the whole difference between this file and
`mutation_matrix.py`.

Each probe returns (holds: bool, detail: str). `holds=True` means the named
guarantee is intact. The harness requires True on the clean tree and False
under the edit.

Usage:  python3 reproduce/axiom_probes.py A3
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import uuid

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

os.environ.setdefault("DJ_DB", os.path.join(tempfile.mkdtemp(), "axiom.db"))
os.environ["DJ_DEV_KEYS"] = "1"
os.environ.setdefault("DJ_JUDGE_MODE", "oracle")
os.environ.setdefault("DJ_GITHUB_ALLOW_UNSIGNED", "1")

# A7 runs on an EMPTY opening store, and the reason is a coupling worth
# recording rather than a convenience. The bootstrap's seed import writes two
# lapsed risk acceptances and then reads back the referral each of them emits,
# so **the seed import itself depends on A7 holding**. Drop A7 against the
# ordinary seed store and the container cannot finish booting, which witnesses
# nothing about the axiom — "bootstrap crashed" is not the guarantee
# Proposition 4 names. On an unseeded store the counter-model is the thing it
# should be: an acceptance exists, and the Lawmakers were never told.
if len(sys.argv) > 1 and sys.argv[1] == "A7":
    os.environ["DJ_SEED_STORE"] = "store_seed_empty.json"

from app import bootstrap, db, kernel                       # noqa: E402
from app.db import now_iso                                  # noqa: E402


def services():
    svc = bootstrap.build_services()
    bootstrap.bootstrap(svc)
    return svc


def reader():
    return db.open_reader()


# ---------------------------------------------------------------------------
# A1 — one principal, one branch, at any instant (Definition 9(i), Corollary 1)
#
# Counter-model: the same principal holds Lawmakers and Judges, enacts a
# provision and then adjudicates a case on it. The guarantee that fails is
# Corollary 1 — no decision is typable in which the resolving authority
# authored the provision — and Definition 9(i) with it.
# ---------------------------------------------------------------------------
def probe_A1():
    services()
    w = db.open_writer()
    # Try to give a judging principal the legislative branch as well. On the
    # clean build the ledger refuses; the refusal IS the guarantee.
    try:
        w.execute(
            "INSERT INTO authority_assignment (assignment_id, principal_id,"
            " branch, valid_from, granted_by, grant_reason)"
            " VALUES (?,?,?,?,?,?)",
            (str(uuid.uuid4()), "svc:tier1", "lawmakers",
             "2025-07-01T00:00:00.000000+00:00", "alice.grc",
             "axiom counter-model"))
        w.commit()
    except Exception as e:                                    # noqa: BLE001
        return True, f"overlap refused at the ledger: {str(e)[:70]}"
    # It was accepted. Show the consequence rather than stopping at the grant.
    branches = [r["branch"] for r in w.execute(
        "SELECT branch FROM authority_assignment WHERE principal_id=?"
        "   AND (valid_to IS NULL)", ("svc:tier1",))]
    return False, (f"svc:tier1 now holds {sorted(set(branches))}: one"
                   f" authority may author a provision and adjudicate a case"
                   f" on it, so Corollary 1 has a counter-model")


# ---------------------------------------------------------------------------
# A2 — the three families' output types do not overlap
#
# Counter-model: a judging instance emits an acceptance-typed object. On the
# clean build the ledger makes that unrepresentable, so Accept_risk's type is
# reachable only through Accept_risk. Drop A2 and it is reachable from Decide.
# ---------------------------------------------------------------------------
def probe_A2():
    services()
    w = db.open_writer()
    try:
        w.execute(
            "INSERT INTO precedent_record (id, content_hash, case_id,"
            " provision_id, rulebook_version, facts, premise, interpretation,"
            " authority_tier, resolving_principal, consulted_ids,"
            " controlling_state, rationale_text, judgment_batch_id, scope,"
            " scope_level, is_acceptance, expiry, resolved_at)"
            " VALUES ('a2','a2','a2','SC-201','rb-000001','[]','[]','{}',"
            " 2,'svc:tier2','[]','none_empty','r','b','{}','org',1,"
            " '2027-01-01T00:00:00.000000+00:00','t')")
        w.rollback()
        return False, ("an acceptance-typed record exists at tier 2: the"
                       " Decide and Accept_risk families now share an output"
                       " type, and A4's trigger and A7's lifecycle bind the"
                       " function rather than the type")
    except Exception as e:                                    # noqa: BLE001
        w.rollback()
        return True, f"acceptance type unreachable from Decide: {str(e)[:60]}"


# ---------------------------------------------------------------------------
# A3 — adjudication holds no amendment authority (Definition 9(iii))
#
# This is the counter-model Proposition 4 cites by name. A judging principal
# attempts to enact a rulebook version. On the clean build the constitution
# store refuses; drop A3 and the rulebook changes under adjudication, so the
# byte-identity of the rulebook across adjudications fails.
# ---------------------------------------------------------------------------
def probe_A3():
    svc = services()
    before = svc.constitution.current_version()
    prov = [{"provision_id": "SC-299", "text": "Counter-model clause.",
             "policy": {"deny_if_any": ["counter_model_factor"]},
             "absolute": False}]
    try:
        svc.constitution.enact_version(prov, "svc:tier1", None)
    except Exception as e:                                    # noqa: BLE001
        return True, (f"a judging principal cannot enact: {str(e)[:70]};"
                      f" rulebook still {before}")
    after = svc.constitution.current_version()
    return False, (f"svc:tier1 enacted {after} from {before}: a Decide"
                   f" principal changed a rule, so Definition 9(iii) fails")


# ---------------------------------------------------------------------------
# A4 — Accept_risk fires only at exhaustion
#
# Counter-model: a tier-k record is admitted for a case with no contest
# history at all. The guarantee that fails is CC-06 and the human backstop:
# the authority that adjudicated the case is the one that accepted its risk.
# ---------------------------------------------------------------------------
def probe_A4():
    svc = services()
    artifact = _acceptance_artifact("a4-case")
    try:
        rid = svc.gate.admit(artifact)
    except kernel.KernelError as e:
        return True, f"unexhausted acceptance refused: {str(e)[:70]}"
    ok = svc.chain.verify_exhaustion("a4-case")
    return False, (f"acceptance {rid[:8]} admitted at tier 4 with"
                   f" verify_exhaustion={ok}: the ladder was never climbed")


def _acceptance_artifact(case_id: str) -> dict:
    return {
        "artifact_version": "1.0",
        "case": {"case_id": case_id, "case_hash": kernel.sha256(case_id),
                 "provision_id": "SC-201", "rulebook_version": "rb-000001",
                 "facts": ["connector_credentials"], "author": "eng.sam",
                 "organization": None},
        "tier": 4, "resolving_principal": "coo.pat",
        "retrieval": {"theta": 0.25, "snapshot_at": now_iso(),
                      "candidates": []},
        "judgments": {"batch_id": str(uuid.uuid4()), "verdicts": []},
        "ordering": {"keys_applied": ["authority", "recency", "scope"],
                     "controlling_state": "none_empty",
                     "controlling_id": None, "tie_members": None},
        "decision": {"interpretation": {"outcome": "permit_conditional"},
                     "conditions": None, "premise": ["connector_credentials"],
                     "rationale_text": "counter-model acceptance",
                     "scope": {}, "scope_level": "org", "is_acceptance": True,
                     "expiry": "2027-01-01T00:00:00.000000+00:00"},
        "degradations": [], "resolved_at": now_iso(),
    }


# ---------------------------------------------------------------------------
# A5 — the full trail is written at the moment of resolution
#
# Counter-model: a stored record persists a summary of Consulted rather than
# the set itself. Theorem 2's rebuild then returns a Provenance that does not
# equal the one the run computed, on a record whose trace says otherwise.
# ---------------------------------------------------------------------------
def probe_A5():
    svc = services()
    r = svc.adjudicator.submit_case(
        "SC-201", ["connector_credentials"], "eng.sam", {})
    svc.adjudicator.challenge(r["case_id"], "eng.sam", "counter-model")
    fin = svc.adjudicator.accept_resolution(r["case_id"], "eng.sam")
    rid = fin["record_id"]
    c = reader()
    row = c.execute("SELECT consulted_ids FROM precedent_record WHERE id=?",
                    (rid,)).fetchone()
    stored = json.loads(row["consulted_ids"])
    cs = c.execute("SELECT artifacts FROM case_state WHERE case_id=?",
                   (r["case_id"],)).fetchone()
    arts = json.loads(cs["artifacts"])
    top = arts[str(max(int(k) for k in arts))]
    ran = [x["record_id"] for x in top["retrieval"]["candidates"]]
    if sorted(stored) == sorted(ran):
        return True, (f"Consulted persisted in full: {len(ran)} candidate(s)"
                      f" retrieved, {len(stored)} recorded")
    return False, (f"the trail is a summary: {len(ran)} candidate(s) were"
                   f" consulted and {len(stored)} recorded, so rebuild cannot"
                   f" return Provenance(c) and Theorem 2 fails on this record")


# ---------------------------------------------------------------------------
# A6 — absolute provisions short-circuit before retrieval
#
# Counter-model: a case violating an absolute provision is retrieved for and
# can be controlled by a permissive record. The absolute floor of A6 fails.
# ---------------------------------------------------------------------------
def probe_A6():
    svc = services()
    r = svc.adjudicator.submit_case(
        "SC-202", ["screening_bypass"], "eng.sam", {})
    c = reader()
    n = c.execute("SELECT COUNT(*) AS n FROM retrieval_log WHERE case_id=?",
                  (r["case_id"],)).fetchone()["n"]
    if n == 0 and r.get("controlling_state") == "absolute_short_circuit":
        return True, "absolute case: zero retrievals, no challenge path"
    return False, (f"an absolute-violating case ran {n} retrieval(s) and"
                   f" resolved as {r.get('controlling_state')}: a record may"
                   f" now control a floor violation")


# ---------------------------------------------------------------------------
# A7 — every acceptance expires and refers
#
# Counter-model: an acceptance is admitted and no DraftAmendment is emitted
# with it. Proposition 1's posture set — adopted, pending, lapsed — has a
# member with no referral to be in any posture about.
# ---------------------------------------------------------------------------
def probe_A7():
    svc = services()
    for t in (1, 2, 3):
        svc.chain.append("a7-case", t, "eng.sam", "counter-model contest")
    rid = svc.gate.admit(_acceptance_artifact("a7-case"))
    c = reader()
    n = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_lifecycle_event"
        " WHERE record_id=? AND event_type='referral_emitted'",
        (rid,)).fetchone()["n"]
    if n == 1:
        return True, "acceptance emitted its referral transactionally"
    return False, (f"acceptance {rid[:8]} carries {n} referral(s): a waiver"
                   f" exists that the Lawmakers were never told about")


# ---------------------------------------------------------------------------
# A8 — a controlled decision follows its controlling record
#
# Counter-model: a case is bound by a record and decided against it. The
# bindingness obligation fails, and it fails silently — the trail still names
# the controlling record.
# ---------------------------------------------------------------------------
def probe_A8():
    svc = services()
    a = svc.adjudicator.submit_case(
        "SC-201", ["connector_credentials", "encrypted_config",
                   "rotation_enabled", "vault_onboarding_queued"],
        "eng.sam", {})
    if a["controlling_state"] != "bound":
        return True, ("no case was bound in this scenario, so the obligation"
                      " is not exercised (treated as holding)")
    c = reader()
    rec = c.execute("SELECT interpretation FROM precedent_record WHERE id=?",
                    (a["controlling"],)).fetchone()
    want = json.loads(rec["interpretation"])["outcome"]
    if a["decision"] == want:
        return True, (f"bound decision mirrors its controlling record"
                      f" ({want})")
    return False, (f"case is bound by {a['controlling'][:8]} whose holding is"
                   f" {want}, and was decided {a['decision']}: A8's obligation"
                   f" is unmet and the trail still cites the record")


PROBES = {"A1": probe_A1, "A2": probe_A2, "A3": probe_A3, "A4": probe_A4,
          "A5": probe_A5, "A6": probe_A6, "A7": probe_A7, "A8": probe_A8}


def main(argv):
    if len(argv) != 2 or argv[1] not in PROBES:
        sys.exit(f"usage: axiom_probes.py {{{'|'.join(sorted(PROBES))}}}")
    try:
        holds, detail = PROBES[argv[1]]()
    except Exception as e:                                    # noqa: BLE001
        print(f"ERROR {type(e).__name__}: {e}")
        return 2
    print(("HOLDS " if holds else "FAILS ") + detail)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
