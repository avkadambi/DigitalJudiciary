#!/usr/bin/env python3
"""Conformance harness (SDD v3.0 §4 / paper §11): boots the full container
process on a fresh database, drives a mechanism-complete corpus over live
HTTP, then computes every conformance check from the executed traces —
nothing is asserted that is not computed. Exit code 0 iff everything holds.

Run:  DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 python3 run_conformance.py
"""
from __future__ import annotations

import json
import os
os.environ.setdefault('DJ_LEDGER_BACKEND', 'sqlite')
os.environ.setdefault('DJ_LEDGER_ON_PG', '0')
import sqlite3
import sys
import tempfile
import threading
import urllib.error
import urllib.request

# Environment must be fixed before app modules import db.DB_PATH.
os.environ.setdefault("DJ_DB", os.path.join(tempfile.mkdtemp(), "judiciary.db"))
os.environ["DJ_DEV_KEYS"] = "1"
os.environ.setdefault("DJ_JUDGE_MODE", "oracle")   # only certifiable mode

from app import bootstrap, db, httpapi, kernel          # noqa: E402
from app.adjudicate import order                        # noqa: E402

PORT = int(os.environ.get("DJ_PORT", "18080"))
BASE = f"http://127.0.0.1:{PORT}"
KEYS = bootstrap.DEV_KEYS

results: list[tuple[str, str, bool, str]] = []   # (id, name, ok, detail)
narrative: list[tuple[str, str]] = []


def check(cid: str, name: str, ok: bool, detail: str = "") -> None:
    results.append((cid, name, bool(ok), detail))


def api(method: str, path: str, who: str, body: dict | None = None,
        expect: int = 200) -> dict:
    req = urllib.request.Request(
        BASE + path, method=method,
        data=json.dumps(body or {}).encode() if method == "POST" else None,
        headers={"authorization": f"Bearer {KEYS[who]}",
                 "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            status, payload = r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        status, payload = e.code, json.loads(e.read() or b"{}")
    if status != expect:
        raise AssertionError(
            f"{method} {path} as {who}: expected {expect}, got {status}: "
            f"{payload}")
    return payload


def submit(who: str, provision: str, facts: list[str],
           scope: dict | None = None) -> dict:
    return api("POST", "/v1/cases", who,
               {"provision_id": provision, "facts": facts,
                "case_scope": scope or {}})


# ===========================================================================
# The corpus: every mechanism of the contract, exercised over live HTTP
# ===========================================================================
def run_corpus(svc) -> dict:
    ids: dict[str, str] = {}

    # A — routine compliant change: final at tier 1, precedentially silent
    a01 = submit("eng.sam", "SC-206", ["compliant", "unit_tests"])
    check("COR-A", "A01 routine permit, no precedent consulted",
          a01["decision"] == "permit"
          and a01["controlling_state"] == "none_empty")
    ids["A01"] = a01["case_id"]
    narrative.append(("A01", "routine change -> permit (t1), silent"))

    # B — plain violation, uncontested: Controlling = none is an answer
    b01 = submit("eng.sam", "SC-206",
                 ["coverage_shortfall", "critical_service", "new_feature"])
    check("COR-B", "B01 plain violation denied; none recorded as answer",
          b01["decision"] == "deny"
          and b01["controlling_state"] == "none_empty")
    narrative.append(("B01", "plain violation -> deny (t1), unchallenged"))

    # C — single controlling precedent: citation flips a flat deny
    c_facts = ["connector_credentials", "encrypted_config",
               "rotation_enabled", "vault_onboarding_queued"]
    c01 = submit("eng.sam", "SC-201", c_facts)
    check("COR-C1", "C01 bound by SP-001: permit_conditional by citation",
          c01["decision"] == "permit_conditional"
          and c01["controlling_state"] == "bound")
    narrative.append(("C01", "vault-lag hotfix -> permit_conditional, "
                             "controls: SP-001, no human involved"))

    # C19 — same case, contested; tier 2 affirms; affirmation is stored
    c19 = submit("eng.sam", "SC-201", c_facts)
    ch = api("POST", f"/v1/decisions/{c19['case_id']}/challenge", "eng.sam",
             {"grounds": "the conditions are too narrow for our team"})
    check("COR-C2", "C19 tier-2 re-adjudication still bound by SP-001",
          ch["tier"] == 2 and ch["controlling_state"] == "bound")
    fin = api("POST", f"/v1/decisions/{c19['case_id']}/accept", "eng.sam")
    check("COR-C3", "C19 contested-and-affirmed case is stored (Def.7)",
          fin["record_id"] is not None)
    ids["C19_record"] = fin["record_id"]
    narrative.append(("C19", "same case contested -> t2 affirms SP-001; "
                             "affirmation stored: the corpus's first record"))

    # D — conflicting precedents: each ordering key decisive somewhere
    d01 = submit("eng.sam", "SC-203",
                 ["third_party_lib", "community_audit_complete",
                  "touches_telematics", "tenant_data_path",
                  "vendor_review_pending"])
    check("COR-D1", "D01 authority key: RiskOwner SP-002 outranks tier-3"
                    " SP-003",
          d01["controlling_state"] == "bound"
          and d01["decision"] == "permit_conditional")
    narrative.append(("D01", "audited lib on telematics: both precedents "
                             "survive; authority key -> SP-002 controls"))

    d05 = submit("eng.sam", "SC-206",
                 ["legacy_module", "coverage_waiver_request"])
    check("COR-D2", "D05 recency key: newer equal-authority denial controls",
          d05["controlling_state"] == "bound" and d05["decision"] == "deny")
    narrative.append(("D05", "legacy coverage waiver: recency key -> "
                             "newer SP-014 denial controls"))

    d07 = submit("eng.sam", "SC-217",
                 ["flagged_off_default", "tracking_service"],
                 scope={"service": "tracking"})
    check("COR-D3", "D07 scope key: narrower service-scoped denial controls"
                    " its own domain",
          d07["controlling_state"] == "bound" and d07["decision"] == "deny")
    narrative.append(("D07", "flagged change on tracking: scope key -> "
                             "service-scoped SP-015 controls"))

    # E — the gate: distinguish runs before any ranking
    e01 = submit("eng.sam", "SC-201",
                 ["connector_credentials", "encrypted_config",
                  "rotation_enabled", "vault_onboarding_rejected"])
    check("COR-E1", "E01 rejected-onboarding case: all candidates"
                    " distinguished, direct deny",
          e01["controlling_state"] == "none_all_distinguished"
          and e01["decision"] == "deny")
    narrative.append(("E01", "onboarding REJECTED (not queued): SP-001 and "
                             "its progeny fall at the gate -> deny"))

    e08 = submit("eng.sam", "SC-203",
                 ["third_party_lib", "touches_telematics",
                  "tenant_data_path", "vendor_review_pending"])
    check("COR-E2", "E08 gate discards higher authority; lower-rank SP-003"
                    " controls (paper Example 2)",
          e08["controlling_state"] == "bound" and e08["decision"] == "deny")
    narrative.append(("E08", "no community audit: higher-authority SP-002 "
                             "distinguished BEFORE ranking; SP-003 controls"))

    # F — absolute provision: short-circuit, no retrieval, no escalation
    f01 = submit("eng.sam", "SC-202", ["screening_bypass", "allowlist_path"])
    check("COR-F1", "F01 absolute short-circuit denies at once (A6)",
          f01["decision"] == "deny"
          and f01["controlling_state"] == "absolute_short_circuit"
          and f01.get("storable") is False)
    ids["F01"] = f01["case_id"]
    err = api("POST", f"/v1/decisions/{f01['case_id']}/challenge", "eng.sam",
              {"grounds": "deadline"}, expect=409)
    check("COR-F2", "F01 challenge against an absolute provision has no"
                    " path (A6)", "final" in err.get("error", ""))
    narrative.append(("F01", "screening bypass: A6 fires; no retrieval, no "
                             "precedent, no escalation, ever"))

    # TIE — a tie surviving all three keys is Controlling = none
    tie = submit("eng.sam", "SC-210", ["dummy_marked", "fixture_path"])
    check("COR-T", "TIE: unbroken seed conflict -> none_tie, direct"
                   " interpretation",
          tie["controlling_state"] == "none_tie"
          and tie["decision"] == "permit")
    narrative.append(("TIE", "identical-rank seed conflict: none_tie "
                             "recorded; agent interprets directly"))

    # I — lapse: the expired waiver is excluded mechanically
    api("POST", "/v1/admin/lifecycle-sweep", "alice.grc")
    i01 = submit("eng.sam", "SC-211", ["freeze_deploy", "carrier_outage"])
    check("COR-I", "I01 lapsed SP-008 excluded inside retrieval (A7)",
          i01["controlling_state"] == "none_empty"
          and i01["decision"] == "deny")
    narrative.append(("I01", "citing last quarter's waiver: lapsed SP-008 "
                             "never reaches Candidates -> deny"))

    # G — the RiskOwner: renewal-while-pending, with mandatory expiry
    g03 = submit("eng.sam", "SC-211",
                 ["freeze_deploy", "carrier_outage", "port_disruption"])
    for tier in (1, 2, 3):
        r = api("POST", f"/v1/decisions/{g03['case_id']}/challenge",
                "eng.sam", {"grounds": f"contest tier {tier}: port "
                                       f"disruption is an emergency"})
    check("COR-G1", "G03 exhaustion reaches the RiskOwner with the renewal"
                    " guard evaluated first",
          r["status"] == "awaiting_risk_owner"
          and r["renewal_guard"]["state"] == "must_cite")
    acc = api("POST", f"/v1/cases/{g03['case_id']}/risk-decision", "coo.pat",
              {"decision": "accept",
               "rationale": "port disruption rerouting is time-critical",
               "expiry": "2026-10-22T00:00:00.000000+00:00"})
    check("COR-G2", "G03 acceptance stored with expiry and citation of the"
                    " lapsed predecessor (A7)",
          acc["record_id"] is not None and acc["renews_record"] is not None)
    ids["G03_record"] = acc["record_id"]
    narrative.append(("G03", "renewal issues ONLY because SP-008's referral "
                             "is still pending; cites the record it renews"))

    # GB — the bar: rejection closes the acceptance path (Prop. 2)
    gb = submit("eng.sam", "SC-215",
                ["growth_experiment", "portal_feature_v2"])
    for tier in (1, 2, 3):
        r = api("POST", f"/v1/decisions/{gb['case_id']}/challenge",
                "eng.sam", {"grounds": f"contest tier {tier}: growth "
                                       f"targets slip without it"})
    check("COR-GB1", "GB guard reports barred: predecessor's referral was"
                     " rejected",
          r["renewal_guard"]["state"] == "barred")
    err = api("POST", f"/v1/cases/{gb['case_id']}/risk-decision", "coo.pat",
              {"decision": "accept", "rationale": "try anyway",
               "expiry": "2026-12-01T00:00:00.000000+00:00"}, expect=422)
    check("COR-GB2", "GB acceptance is REFUSED at tier k (Proposition 2"
                     " renewal bar)", "Proposition 2" in err["error"])
    dec = api("POST", f"/v1/cases/{gb['case_id']}/risk-decision", "coo.pat",
              {"decision": "decline",
               "rationale": "the Council already said no"})
    check("COR-GB3", "GB upheld denial stored under the RiskOwner's name"
                     " (paper §11.3 G)", dec["record_id"] is not None
          and dec["decision"] == "deny")
    ids["GB_record"] = dec["record_id"]
    narrative.append(("GB", "renewal barred after rejection; RiskOwner "
                            "declines; upheld denial stored at tier k"))

    # H — control-plane attempt: never a case (A3)
    h01 = submit("svc:tier1", "constitution", [])
    check("COR-H", "H01 policy-repo change routed to the legislative"
                   " channel, never adjudicated (A3)",
          h01.get("routed") == "draft_amendment")
    narrative.append(("H01", "remediation agent edits the rulebook: routed "
                             "as DraftAmendment; adjudication cannot enact"))

    # J — novelty: none flagged; the contested resolution becomes precedent
    j_facts = ["llm_copilot", "sandboxed_runtime", "tenant_data_path",
               "vendor_review_pending", "first_of_kind"]
    j01 = submit("eng.sam", "SC-203", j_facts)
    check("COR-J1", "J01 first-of-kind: candidates exist, all"
                    " distinguished, flagged",
          j01["controlling_state"] == "none_all_distinguished")
    api("POST", f"/v1/decisions/{j01['case_id']}/challenge", "eng.sam",
        {"grounds": "sandboxing changes the risk profile"})
    finj = api("POST", f"/v1/decisions/{j01['case_id']}/accept", "eng.sam")
    check("COR-J2", "J01 contested novel matter enters the store",
          finj["record_id"] is not None)
    ids["J01_record"] = finj["record_id"]

    j02 = submit("eng.sam", "SC-203", j_facts + ["expanded_rollout"])
    check("COR-J3", "J02 bound by the record this corpus itself created:"
                    " the Store's growth acting within its own run",
          j02["controlling_state"] == "bound"
          and j02["controlling"] == ids["J01_record"])
    narrative.append(("J01/J02", "novel copilot matter litigated once at t2;"
                                 " the next rollout resolves by citation"))

    # Amendment lifecycle: propose, adopt, new pinned version thereafter
    am = api("POST", "/v1/amendments", "alice.grc",
             {"origin": "lawmaker",
              "body": {"changes": [{"provision_id": "SC-230",
                                    "text": "Model updates require a shadow"
                                            " evaluation report.",
                                    "policy": {"deny_if_any":
                                               ["no_shadow_eval"]},
                                    "absolute": False}]}})
    ad = api("POST", f"/v1/amendments/{am['amendment_id']}/decision",
             "alice.grc", {"decision": "adopted"})
    check("COR-L1", "amendment adopted through the only channel; new"
                    " rulebook version enacted (A3)",
          ad["new_version"] == "rb-000002")
    post = submit("eng.sam", "SC-230", ["shadow_eval_complete"])
    got = api("GET", f"/v1/decisions/{post['case_id']}", "eng.sam")
    check("COR-L2", "post-amendment case pins the new version at intake"
                    " (CC-04 substrate)",
          got["rulebook_version"] == "rb-000002")
    narrative.append(("AMD", "SC-230 enacted by the Lawmakers; new cases pin"
                             " rb-000002; in-flight pins are untouched"))

    # L — consolidation (Definitions 15 and 16; Definition 7 clause (ii)).
    #
    # Run on SC-230 because the Lawmakers have just enacted it and nothing has
    # been decided under it, so retrieval is empty and `resolve` returns the
    # plain `none` clause (d) requires. The class is formed HERE, before any
    # member is submitted, by the pipeline service — which takes no authority
    # as argument and produces a type no authority produces. CC-22 asserts all
    # of that from the trace rather than from this comment.
    from app import consolidate                              # noqa: E402
    rb2 = svc.constitution.current_version()
    lodged = "2026-09-01T09:%02d:00.000000+00:00"
    docket = [
        {"unit_id": "L01", "case_id": "L01", "provisions": ["SC-230"],
         "facts": ["no_shadow_eval"], "rulebook_version": rb2,
         "lodged_at": lodged % 0},
        {"unit_id": "L02", "case_id": "L02", "provisions": ["SC-230"],
         "facts": ["no_shadow_eval"], "rulebook_version": rb2,
         "lodged_at": lodged % 5},
        # Alike under F_p, different outside it. Under Definition 15's grain
        # this is a member; under the M11 mutant, which reads facts(c) whole,
        # it is not — and CC-20(g) is what notices.
        {"unit_id": "L03", "case_id": "L03", "provisions": ["SC-230"],
         "facts": ["no_shadow_eval", "batch_reference_note"],
         "rulebook_version": rb2, "lodged_at": lodged % 10},
        # Two provisions at once: excluded by clause (b), because it would
        # otherwise be a member of two classes with different representatives
        # while `resolve` returns one controlling record for the whole case.
        {"unit_id": "L04", "case_id": "L04",
         "provisions": ["SC-230", "SC-206"],
         "facts": ["no_shadow_eval", "coverage_shortfall"],
         "rulebook_version": rb2, "lodged_at": lodged % 15},
    ]
    provisions = {pid: svc.constitution.get_provision(rb2, pid)
                  for pid in ("SC-230", "SC-206")}
    classes = consolidate.classify(
        docket, svc.adjudicator.live_store(), provisions, now=db.now_iso(),
        resolve_state=lambda pid, f: svc.adjudicator.classify_probe(
            pid, f, None))
    for cls in classes:
        svc.classifier.write(cls)
    check("COR-26", "one class forms over the three like units; the"
                    " two-provision unit is excluded by clause (b) and the"
                    " representative is the published total order's, not the"
                    " first to arrive",
          len(classes) == 1
          and classes[0]["members"] == ["L01", "L02", "L03"]
          and classes[0]["representative"] == "L01",
          f"{[ (c['members'], c['representative']) for c in classes ]}")

    ji_before = svc.adjudicator._w.execute(
        "SELECT COUNT(*) AS n FROM judgment_invocation").fetchone()["n"]
    l01 = submit("eng.sam", "SC-230", ["no_shadow_eval"], {"unit": "L01"})
    ids["L01_record"] = l01.get("record_id")
    check("COR-26b", "the representative is admitted at FIRST INSTANCE under"
                     " Definition 7(ii), naming its class",
          l01.get("record_id") is not None
          and l01.get("consolidation", {}).get("role") == "representative",
          f"record={l01.get('record_id')}")

    ji_mid = svc.adjudicator._w.execute(
        "SELECT COUNT(*) AS n FROM judgment_invocation").fetchone()["n"]
    l02 = submit("eng.sam", "SC-230", ["no_shadow_eval"], {"unit": "L02"})
    l03 = submit("eng.sam", "SC-230",
                 ["no_shadow_eval", "batch_reference_note"], {"unit": "L03"})
    ji_after = svc.adjudicator._w.execute(
        "SELECT COUNT(*) AS n FROM judgment_invocation").fetchone()["n"]
    check("COR-27", "the two members are disposed by direct citation of the"
                    " representative's record: bound, no retrieval and not one"
                    " gate invocation between them",
          l02["controlling"] == ids["L01_record"]
          and l03["controlling"] == ids["L01_record"]
          and ji_after == ji_mid,
          f"gate invocations during the two members: {ji_after - ji_mid}"
          f" (representative cost {ji_mid - ji_before})")
    narrative.append(("L01/L02/L03", "three co-pending like units: one"
                                     " adjudication, one record, two"
                                     " citations"))

    # L04 engages two provisions, so the pipeline files two cases for it —
    # which is exactly why clause (b) excluded it, and which is how CC-20(g)
    # can tell an excluded unit from a dropped one.
    l04 = submit("eng.sam", "SC-230",
                 ["no_shadow_eval", "coverage_shortfall"], {"unit": "L04"})
    submit("eng.sam", "SC-206",
           ["no_shadow_eval", "coverage_shortfall"], {"unit": "L04"})
    check("COR-28", "the unit clause (b) excluded is not lost: it is"
                    " adjudicated on its own and comes out BOUND by the record"
                    " the class created. The refusal costs retrieval and gate"
                    " work, and nothing in correctness or coverage",
          l04["controlling_state"] == "bound"
          and l04["controlling"] == ids["L01_record"],
          f"{l04['controlling_state']} / {l04.get('controlling')}")
    # A second docket boundary, after the class's record is live. Two more
    # co-pending units of the SAME signature arrive. Clause (e) refuses to
    # form a class over a signature a live record already covers, and it is
    # the clause the |Rules|*2^kappa ceiling of Proposition A_cons(ii) rests
    # on: without it a stream could mint a consolidated record per docket for
    # ever and the constant would stop being a ceiling.
    docket2 = [
        {"unit_id": "L05", "case_id": "L05", "provisions": ["SC-230"],
         "facts": ["no_shadow_eval"], "rulebook_version": rb2,
         "lodged_at": lodged % 20},
        {"unit_id": "L06", "case_id": "L06", "provisions": ["SC-230"],
         "facts": ["no_shadow_eval"], "rulebook_version": rb2,
         "lodged_at": lodged % 25},
    ]
    classes2 = consolidate.classify(
        docket2, svc.adjudicator.live_store(), provisions, now=db.now_iso(),
        resolve_state=lambda pid, f: svc.adjudicator.classify_probe(
            pid, f, None))
    for cls in classes2:
        svc.classifier.write(cls)
    l05 = submit("eng.sam", "SC-230", ["no_shadow_eval"], {"unit": "L05"})
    submit("eng.sam", "SC-230", ["no_shadow_eval"], {"unit": "L06"})
    check("COR-29", "clause (e): a second class does NOT form over a"
                    " signature a live consolidated record already covers,"
                    " and the two units are disposed by ordinary citation of"
                    " that record — the ceiling holds without a second"
                    " admission",
          not classes2 and l05["controlling"] == ids["L01_record"]
          and l05.get("consolidation") is None,
          f"{len(classes2)} further class(es); L05 controlling"
          f" {str(l05.get('controlling'))[:8]}")
    narrative.append(("L05/L06", "same signature, live cover: no second"
                                 " class, no second record"))

    ids["class_id"] = classes[0]["class_id"]
    return ids


# ===========================================================================
# Violation probes: each guarantee must FAIL correctly when attacked
# ===========================================================================
def run_probes(svc) -> None:
    path = os.environ["DJ_DB"]
    w = db.open_writer(path)

    def expect_abort(pid, name, sql, params=()):
        try:
            w.execute(sql, params)
            w.commit()
            check(pid, name, False, "write was ACCEPTED")
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            w.rollback()
            check(pid, name, True, str(e).split("\n")[0][:70])

    def expect_accept(pid, name, sql, params=()):
        """The mirror of expect_abort: a write the schema must ALLOW.

        A relaxation stated only as an absence is untestable. PRB-11 asserts
        that the one ground Definition 7(ii) licenses is genuinely licensed,
        so that a build which over-tightened the CHECK back to BETWEEN 2 AND 4
        fails here rather than passing silently."""
        try:
            w.execute(sql, params)
            w.rollback()
            check(pid, name, True, "write accepted, as Def.7(ii) requires")
        except (sqlite3.IntegrityError, sqlite3.OperationalError) as e:
            w.rollback()
            check(pid, name, False, "write was REFUSED: " + str(e).split("\n")[0][:60])

    rid = w.execute("SELECT id FROM precedent_record LIMIT 1").fetchone()["id"]
    expect_abort("PRB-1", "UPDATE on a precedent record aborts (A5)",
                 "UPDATE precedent_record SET rationale_text='x' WHERE id=?",
                 (rid,))
    expect_abort("PRB-2", "DELETE on a precedent record aborts (A5)",
                 "DELETE FROM precedent_record WHERE id=?", (rid,))
    # PRB-3 changed on 1 September 2026, and the change is a contract change.
    #
    # It used to assert that a tier-1 row is unrepresentable, full stop. RA-3's
    # Definition 7(ii) admits a consolidated record at first instance, so that
    # bar could not stand. What it asserts now is sharper: a tier-1 row is
    # unrepresentable on every ground EXCEPT consolidation, and the ground must
    # be named in the row. PRB-11 below asserts the other half — that the
    # licensed ground is genuinely licensed — so the pair together pin the
    # schema exactly where Definition 7 puts it.
    expect_abort("PRB-3", "tier-1 row without admission_ground='consolidation'"
                          " is unrepresentable (Def.7 at the schema)",
                 "INSERT INTO precedent_record (id, content_hash, case_id,"
                 " provision_id, rulebook_version, facts, premise,"
                 " interpretation, authority_tier, resolving_principal,"
                 " consulted_ids, controlling_state, rationale_text,"
                 " judgment_batch_id, scope, scope_level, resolved_at)"
                 " VALUES ('x','x','x','SC-201','rb-000001','[]','[]','{}',"
                 " 1,'svc:tier1','[]','none_empty','r','b','{}','org','t')")
    expect_abort("PRB-3b", "tier-1 row with a non-consolidation ground is"
                           " unrepresentable (the relaxation is conditional)",
                 "INSERT INTO precedent_record (id, content_hash, case_id,"
                 " provision_id, rulebook_version, facts, premise,"
                 " interpretation, authority_tier, admission_ground,"
                 " resolving_principal, consulted_ids, controlling_state,"
                 " rationale_text, judgment_batch_id, scope, scope_level,"
                 " resolved_at)"
                 " VALUES ('x3b','x3b','x3b','SC-201','rb-000001','[]','[]',"
                 " '{}',1,'contest','svc:tier1','[]','none_empty','r','b',"
                 " '{}','org','t')")
    # A class artefact has to exist for the licensed row to name, because the
    # licence is not "tier 1 with a word in a column" but "tier 1 with the
    # class it disposed of, on the record". The probe writes the artefact
    # first, exactly as Classify does.
    w.execute("INSERT INTO consolidation_class (class_id, snapshot_hash,"
              " rulebook_version, provision_id, signature, n0, delta_seconds,"
              " members, docket, representative, producer_service, formed_at)"
              " VALUES ('cls-probe','snap','rb-000001','SC-201','[]',2,3600,"
              " '[\"u1\",\"u2\"]','[\"u1\",\"u2\"]','u1','svc:classify',"
              " 't')")
    # Deliberately NOT committed. The artefact and the record it licenses are
    # written in one transaction, and expect_accept rolls that transaction
    # back — so the probe proves the schema admits the pair and leaves no
    # fixture behind in a ledger the CC checks then count.
    expect_accept("PRB-11", "tier-1 row WITH admission_ground='consolidation'"
                            " and a class artefact is representable"
                            " (Def.7(ii))",
                  "INSERT INTO precedent_record (id, content_hash, case_id,"
                  " provision_id, rulebook_version, facts, premise,"
                  " interpretation, authority_tier, admission_ground,"
                  " class_id, resolving_principal, consulted_ids,"
                  " controlling_state, rationale_text, judgment_batch_id,"
                  " scope, scope_level, resolved_at)"
                  " VALUES ('x11','x11','x11','SC-201','rb-000001','[]','[]',"
                  " '{}',1,'consolidation','cls-probe','svc:classify','[]',"
                  " 'none_empty','r','b','{}','org','t')")
    # The other half of the same clause: the ground alone does not license the
    # row. A consolidated record that names no class is a first-instance
    # admission with nothing behind it, and it aborts.
    expect_abort("PRB-12", "consolidated row with a null class_id is"
                           " unrepresentable (Def.7(ii)'s artefact is not"
                           " optional)",
                 "INSERT INTO precedent_record (id, content_hash, case_id,"
                 " provision_id, rulebook_version, facts, premise,"
                 " interpretation, authority_tier, admission_ground,"
                 " resolving_principal, consulted_ids, controlling_state,"
                 " rationale_text, judgment_batch_id, scope, scope_level,"
                 " resolved_at)"
                 " VALUES ('x12','x12','x12','SC-201','rb-000001','[]','[]',"
                 " '{}',1,'consolidation','svc:classify','[]','none_empty',"
                 " 'r','b','{}','org','t')")
    expect_abort("PRB-4", "acceptance without expiry is unrepresentable"
                          " (A7 at the schema)",
                 "INSERT INTO precedent_record (id, content_hash, case_id,"
                 " provision_id, rulebook_version, facts, premise,"
                 " interpretation, authority_tier, resolving_principal,"
                 " consulted_ids, controlling_state, rationale_text,"
                 " judgment_batch_id, scope, scope_level, is_acceptance,"
                 " resolved_at)"
                 " VALUES ('y','y','y','SC-211','rb-000001','[]','[]','{}',"
                 " 4,'coo.pat','[]','none_empty','r','b','{}','org',1,'t')")
    expect_abort("PRB-5", "overlapping branch grant aborts (A1 EXCLUDE"
                          " equivalent)",
                 "INSERT INTO authority_assignment (assignment_id,"
                 " principal_id, branch, valid_from, granted_by,"
                 " grant_reason) VALUES ('z','alice.grc','judges',"
                 " '2026-07-01T00:00:00.000000+00:00','x','probe')")
    expect_abort("PRB-6", "lifecycle events are immutable (P4)",
                 "DELETE FROM precedent_lifecycle_event WHERE seq=1")
    w.close()

    r = db.open_reader(path)
    try:
        r.execute("INSERT INTO retrieval_log (id, case_id, provision_id,"
                  " theta, candidates, snapshot_at)"
                  " VALUES ('p','p','p',0,0,'t')")
        check("PRB-7", "read-only connections physically cannot write"
                       " (§11.2 role model)", False, "write ACCEPTED")
    except sqlite3.OperationalError as e:
        check("PRB-7", "read-only connections physically cannot write"
                       " (§11.2 role model)", True, str(e)[:70])
    r.close()

    # Gate- and Kernel-level refusals
    try:
        svc.gate.admit({"tier": 1, "case": {"case_id": "p"},
                        "resolving_principal": "svc:tier1",
                        "resolved_at": db.now_iso(), "decision": {},
                        "ordering": {}, "judgments": {}, "retrieval": {}})
        check("PRB-8", "Gate refuses depth < 2 (Def.7)", False,
              "admit() accepted a first-instance artifact")
    except kernel.KernelError as e:
        # The refusal must be the DEPTH refusal, not merely some 422. A
        # first-instance artifact is malformed in several other ways too, so
        # a status-only assertion passes even when the Def. 7 guard is gone
        # -- which is exactly what a mutation pass on this line revealed.
        check("PRB-8", "Gate refuses depth < 2 for the RIGHT reason (Def.7)",
              e.status == 422 and "Def.7" in str(e), str(e)[:70])
    err = api("POST", "/v1/amendments/nonexistent/decision", "eng.sam",
              {"decision": "adopted"}, expect=403)
    check("PRB-9", "non-Lawmaker cannot decide an amendment (A1/A3)",
          "lawmakers" in err["error"])
    err = api("POST", "/v1/cases/nonexistent/risk-decision", "eng.sam",
              {"decision": "accept"}, expect=403)
    check("PRB-10", "non-RiskOwner cannot accept risk (A1/A4)",
          "risk_owner" in err["error"])


# ===========================================================================
# CC checks: computed from the executed traces (SDD §4)
# ===========================================================================
def run_cc(svc, ids: dict) -> None:
    path = os.environ["DJ_DB"]
    c = db.open_reader(path)

    # CC-01 A1: no principal holds two branches at any instant, ever.
    n = c.execute(
        "SELECT COUNT(*) AS n FROM authority_assignment a"
        " JOIN authority_assignment b ON a.principal_id = b.principal_id"
        "  AND a.assignment_id < b.assignment_id"
        "  AND (a.valid_to IS NULL OR a.valid_to > b.valid_from)"
        "  AND (b.valid_to IS NULL OR b.valid_to > a.valid_from)"
    ).fetchone()["n"]
    check("CC-01", "role disjointness over all historical assignments (A1)",
          n == 0, f"{n} overlaps")

    # CC-02 A1 at resolution time, per record.
    recs = c.execute("SELECT * FROM precedent_record").fetchall()
    bad = [r["id"] for r in recs if svc.registry.resolve_branch(
        r["resolving_principal"], r["resolved_at"])
        != ("risk_owner" if r["authority_tier"] == 4 else "judges")]
    check("CC-02", "every record's resolver held the required branch at"
                   " resolved_at", not bad, f"bad: {bad}")

    # CC-04 pinning + constitution integrity.
    ok = True
    for r in recs:
        v = c.execute("SELECT * FROM rulebook_version WHERE version_id=?",
                      (r["rulebook_version"],)).fetchone()
        if not v:
            ok = False
            continue
        provs = c.execute(
            "SELECT provision_id, organization, text, policy_source,"
            " absolute FROM provision WHERE version_id=? ORDER BY"
            " provision_id",
            (v["version_id"],)).fetchall()
        # The same projection the writer uses. Two spellings of "the hash of
        # a rulebook version" is how CC-04 came to be checking something the
        # writer never computed.
        recomputed = kernel.ConstitutionStore.version_digest(
            [dict(p) for p in provs])
        ok = ok and (recomputed == v["content_hash"])
    check("CC-04", "every record pins an intact, hash-verified rulebook"
                   " version (A3)", ok)

    # CC-06 A4: tier-k records carry a verified exhaustion history.
    t4 = [r for r in recs if r["authority_tier"] == 4]
    bad = [r["id"] for r in t4
           if not svc.chain.verify_exhaustion(r["case_id"])]
    check("CC-06", "tier-k records verify contest at every automated tier"
                   " (A4)", not bad, f"{len(t4)} tier-k records")

    # CC-07 Theorem 2: rebuild is defined and complete on every record.
    ok = True
    for r in recs:
        p = svc.ledger.rebuild(r["id"])
        ok = ok and all(p.get(k) is not None for k in
                        ("rules", "consulted", "controlling_state",
                         "resolving_authority", "rationale",
                         "rulebook_version"))
    check("CC-07", f"rebuild() returns full Provenance on every stored"
                   f" record (Theorem 2): {len(recs)} of {len(recs)}", ok)

    # CC-08 A6: absolute cases show zero retrievals and zero records.
    absolutes = c.execute(
        "SELECT case_id FROM case_state WHERE status='denied_absolute'"
    ).fetchall()
    n_ret = sum(c.execute(
        "SELECT COUNT(*) AS n FROM retrieval_log WHERE case_id=?",
        (a["case_id"],)).fetchone()["n"] for a in absolutes)
    n_rec = sum(c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record WHERE case_id=?",
        (a["case_id"],)).fetchone()["n"] for a in absolutes)
    check("CC-08", "absolute cases: zero retrievals, zero records,"
                   " tier-1 denial (A6)",
          absolutes and n_ret == 0 and n_rec == 0,
          f"{len(absolutes)} absolute cases")

    # CC-09 Propositions 1: every acceptance is adopted, pending-live,
    # or lapsed-and-non-controlling.
    accs = c.execute("SELECT * FROM record_effective WHERE is_acceptance=1"
                     ).fetchall()
    states = {"adopted": 0, "pending_live": 0, "lapsed": 0, "OTHER": 0}
    now = db.now_iso()
    for a in accs:
        adopted = c.execute(
            "SELECT 1 FROM precedent_lifecycle_event WHERE record_id=?"
            " AND event_type='referral_adopted'", (a["id"],)).fetchone()
        if adopted:
            states["adopted"] += 1
        elif a["expiry"] > now:
            states["pending_live"] += 1
        elif a["lapsed"]:
            states["lapsed"] += 1
        else:
            states["OTHER"] += 1
    check("CC-09", "every acceptance in {adopted, pending live, lapsed"
                   " non-controlling} (Prop. 1)",
          states["OTHER"] == 0 and len(accs) > 0, json.dumps(states))

    # CC-10 Proposition 2: no acceptance postdates the rejection of a
    # materially similar lapsed predecessor's referral.
    violations = 0
    for a in accs:
        for b in accs:
            if a["id"] == b["id"] or a["provision_id"] != b["provision_id"]:
                continue
            rej = c.execute(
                "SELECT occurred_at FROM precedent_lifecycle_event"
                " WHERE record_id=? AND event_type='referral_rejected'",
                (b["id"],)).fetchone()
            fa, fb = set(json.loads(a["facts"])), set(json.loads(b["facts"]))
            similar = len(fa & fb) / len(fa | fb) >= 0.25 if fa | fb else 0
            if rej and similar and a["resolved_at"] > rej["occurred_at"]:
                violations += 1
    check("CC-10", "no acceptance issued after a similar predecessor's"
                   " referral was rejected (Prop. 2)", violations == 0)

    # CC-11 / CC-15 Def. 7 + Prop. 3: Stored = {depth >= 2} exactly; one
    # write per stored case, zero elsewhere.
    stored_corpus = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record"
        " WHERE case_id NOT LIKE 'SEED-%'").fetchone()["n"]
    finalized = c.execute(
        "SELECT COUNT(*) AS n FROM case_state WHERE status='final'"
        " AND current_tier>=2 AND final_record_id IS NOT NULL"
    ).fetchone()["n"]
    t1_cases = c.execute(
        "SELECT COUNT(*) AS n FROM case_state"
        " WHERE status IN ('decided_t1','denied_absolute')").fetchone()["n"]
    t1_leaked = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record p"
        " JOIN case_state s ON s.case_id=p.case_id"
        " WHERE s.status IN ('decided_t1','denied_absolute')"
    ).fetchone()["n"]
    # Definition 7 as amended (1 Sep 2026) admits in two circumstances, so
    # CC-11 is restated over the union rather than over clause (i) alone. The
    # boundary is still exact; what changed is which cases it runs through,
    # and the record says which clause admitted it. A check left at "depth >=
    # 2" would have been a check on a definition the build no longer has.
    consolidated = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record"
        " WHERE admission_ground = 'consolidation'").fetchone()["n"]
    classes = c.execute(
        "SELECT COUNT(*) AS n FROM consolidation_class").fetchone()["n"]
    # Every consolidated record is tier 1 and names a class; no contested
    # record names one. The two clauses do not blur.
    crossed = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record"
        " WHERE (admission_ground = 'consolidation')"
        "    <> (class_id IS NOT NULL)").fetchone()["n"]
    check("CC-11", "Stored = {cases resolved at depth >= 2} UNION"
                   " {consolidation representatives}, exactly, and each"
                   " record says which clause admitted it (Def. 7 amended)",
          stored_corpus == finalized + consolidated and t1_leaked == 0
          and crossed == 0 and consolidated == classes,
          f"stored={stored_corpus} contested={finalized}"
          f" consolidated={consolidated} of {classes} classes"
          f" t1_cases={t1_cases} leaked={t1_leaked} crossed={crossed}")
    # The N-1 members are the whole of what consolidation buys, and they are
    # exactly the cases that must NOT produce a record. Counting them here is
    # what keeps Fact 1's price honest: the domain contracted, the price per
    # record did not move.
    members = c.execute(
        "SELECT COUNT(*) AS n FROM consolidated_disposition").fetchone()["n"]
    member_leak = c.execute(
        "SELECT COUNT(*) AS n FROM precedent_record p"
        " JOIN consolidated_disposition d"
        "   ON d.member_unit = p.case_id").fetchone()["n"]
    check("CC-15", "one write per stored case; zero writes for the"
                   " unchallenged mass and zero for the N-1 members a class"
                   " disposed by citation (Prop. 3; Fact 1 restated)",
          stored_corpus == finalized + consolidated and t1_leaked == 0
          and member_leak == 0,
          f"{t1_cases} uncontested cases and {members} consolidated members"
          f" produced 0 records")

    # CC-14: renewals cite their predecessor; renewed_by is mirrored.
    renewing = [a for a in accs if a["renews_record"]]
    ok = all(c.execute(
        "SELECT 1 FROM precedent_lifecycle_event WHERE record_id=?"
        " AND event_type='renewed_by'", (a["renews_record"],)).fetchone()
        for a in renewing)
    check("CC-14", "every renewal cites its predecessor and the chain is"
                   " mirrored in the event log (A7)",
          ok and len(renewing) == 1, f"{len(renewing)} renewal(s)")

    # CC-16 determinism: field-only replay of ordering reproduces every
    # stored outcome (§5 design principle).
    ok, replayed = True, 0
    for r in recs:
        consulted = json.loads(r["consulted_ids"])
        if not consulted:
            ok = ok and r["controlling_state"] in (
                "none_empty", "absolute_short_circuit")
            continue
        verdicts = {}
        for j in c.execute(
                "SELECT * FROM judgment_invocation WHERE batch_id=?",
                (r["judgment_batch_id"],)).fetchall():
            cand = c.execute(
                "SELECT id FROM precedent_record WHERE content_hash=?",
                (j["candidate_hash"],)).fetchone()
            if cand:
                verdicts[cand["id"]] = json.loads(j["verdict"])
        survivors = [svc.ledger.get(cid) for cid in consulted
                     if cid in verdicts
                     and not verdicts[cid]["distinguished"]]
        case = {"facts": json.loads(r["facts"]),
                "case_scope": json.loads(r["scope"])}
        ctrl, state, _ = order(survivors, case)
        if state == "none_empty" and consulted:
            state = "none_all_distinguished"
        ok = ok and state == r["controlling_state"] and \
            ((ctrl or {}).get("id") == r["controlling_id"])
        replayed += 1
    check("CC-16", f"field-only replay reproduces controlling_state and"
                   f" controlling_id on {replayed} records with candidates",
          ok)

    # CC-17 A9: a standing declaration exists, every row is attributed and
    # dated, and every stored record's provenance carries the declaration
    # in force at that record's own resolved_at. One-sidedness of the base
    # is thereby a disclosed fact of every audit export, not an unexamined
    # assumption; absence of the declaration is a conformance failure.
    decls = c.execute("SELECT * FROM standing_declaration").fetchall()
    attributed = all(d["declared_by"] and d["declared_at"] for d in decls)
    uncovered = []
    for r in recs:
        d = svc.ledger.rebuild(r["id"]).get("standing_declaration")
        if not d or d["declared_at"] > r["resolved_at"]:
            uncovered.append(r["id"])
    check("CC-17", "standing declaration recorded, attributed, and carried"
                   " in force by every record's provenance (A9)",
          bool(decls) and attributed and not uncovered,
          f"{len(decls)} declaration(s); uncovered records:"
          f" {len(uncovered)}")

    # CC-18 Sect. 4.6, express supersession: recency displaces a conflicting
    # record only where the newer record cites the record it displaces. The
    # append-only Store has no overruling operation, so the citation is the
    # overruling act; without it a newer coordinate decision cannot quietly
    # reverse an older one, and the unbroken conflict surfaces as a tie and
    # a referral. Probed live on a constructed pair, because a trace can
    # only show what did happen and this is a claim about what cannot.
    def _probe(older_out, newer_out, cite):
        older = {"id": "R-old", "authority_tier": 2,
                 "resolved_at": "2025-01-01T00:00:00Z",
                 "interpretation": {"outcome": older_out},
                 "scope": {}, "scope_level": "org", "renews_record": None}
        newer = {"id": "R-new", "authority_tier": 2,
                 "resolved_at": "2026-01-01T00:00:00Z",
                 "interpretation": {"outcome": newer_out},
                 "scope": {}, "scope_level": "org",
                 "renews_record": "R-old" if cite else None}
        ctrl, state, _ = order([older, newer], {"case_scope": {}})
        return (ctrl or {}).get("id"), state

    silent = _probe("permit_conditional", "deny", cite=False)
    express = _probe("permit_conditional", "deny", cite=True)
    agreeing = _probe("deny", "deny", cite=False)
    ok = (silent == (None, "none_tie")
          and express == ("R-new", "bound")
          and agreeing == ("R-new", "bound"))

    # And on the trace: where a record does cite one it supersedes, the
    # displacement is recorded against the record displaced.
    superseding = [r for r in recs
                   if r["renews_record"] and not r["is_acceptance"]]
    mirrored = all(c.execute(
        "SELECT 1 FROM precedent_lifecycle_event WHERE record_id=?"
        " AND event_type='displaced_by'", (r["renews_record"],)).fetchone()
        for r in superseding)
    check("CC-18", "recency displaces a conflicting record only where the"
                   " newer record cites it, and the displacement is"
                   " recorded (Sect. 4.6)",
          ok and mirrored,
          f"silent={silent[1]} express={express[1]} agreeing={agreeing[1]};"
          f" {len(superseding)} express supersession(s), mirrored={mirrored}")

    # ------------------------------------------------------------------
    # CC-19 to CC-22: consolidation (Definitions 15, 16; Definition 7(ii))
    #
    # All four are CC-* rather than COR-* on the register's own test: they
    # check properties that leave no trace when they hold. A correct batch is
    # observationally identical to N correct singletons — nothing in the
    # ledger distinguishes them — and an adjudicator that never in fact formed
    # a class leaves no trace of not having done so.
    # ------------------------------------------------------------------
    from app import consolidate                              # noqa: E402
    classes = [dict(r) for r in c.execute(
        "SELECT * FROM consolidation_class")]
    members_of = {}
    for r in c.execute("SELECT * FROM consolidated_disposition"):
        members_of.setdefault(r["class_id"], []).append(dict(r))

    def _case(case_id):
        row = c.execute("SELECT * FROM case_state WHERE case_id=?",
                        (case_id,)).fetchone()
        return dict(row) if row else None

    def _rep_record(cid):
        row = c.execute("SELECT * FROM precedent_record WHERE class_id=?",
                        (cid,)).fetchone()
        return dict(row) if row else None

    # --- CC-19 ---------------------------------------------------------
    # Recompute `resolve` for every member against the store snapshot the
    # artefact NAMES, by content hash, and require the representative's
    # recorded Consulted and Controlling field for field. Retrieval is
    # replicated here from the ledger's own rule (symmetric Jaccard over fact
    # sets at theta) and the gate from the oracle's (premise containment), so
    # the check is a recomputation and not a re-reading of what the run wrote.
    from app.judges import THETA as _THETA                   # noqa: E402
    cc19_fail, cc19_seen = [], 0
    for cls in classes:
        rep = _rep_record(cls["class_id"])
        if rep is None:
            continue
        snap = [dict(r) for r in c.execute(
            "SELECT * FROM record_effective WHERE lapsed=0 AND superseded=0"
            "   AND resolved_at <= ?", (cls["formed_at"],))]
        # Recomputed HERE, from the definition, and not by calling the
        # module that wrote it. A check that re-runs the writer's own
        # function agrees with the writer by construction — which is how a
        # build that pinned no store at all passed this check the first time
        # it was mutated. The digest is a sorted list of content hashes.
        import hashlib as _h
        digest = _h.sha256(json.dumps(
            sorted(r["content_hash"] for r in snap),
            separators=(",", ":")).encode()).hexdigest()
        if digest != cls["snapshot_hash"]:
            cc19_fail.append((cls["class_id"],
                              "the artefact's snapshot hash does not"
                              " reconstruct from the store at formation"))
            continue
        rep_case = _case(rep["case_id"])
        want_consulted = set(json.loads(rep["consulted_ids"]))
        want_ctrl = rep["controlling_id"]
        units = [(rep["case_id"], json.loads(rep_case["facts"]))] + [
            (m["case_id"], json.loads(_case(m["case_id"])["facts"]))
            for m in members_of.get(cls["class_id"], [])]
        for case_id, facts in units:
            fs = set(facts)
            cands = []
            for r in snap:
                if r["provision_id"] != cls["provision_id"]:
                    continue
                rf = set(json.loads(r["facts"]))
                union = fs | rf
                j = (len(fs & rf) / len(union)) if union else 0.0
                if j >= _THETA:
                    cands.append(r)
            survivors = [r for r in cands
                         if set(json.loads(r["premise"])) <= fs]
            ctrl, _state, _ties = order(
                [{**r, "scope": json.loads(r["scope"]),
                  "interpretation": json.loads(r["interpretation"]),
                  "premise": json.loads(r["premise"])} for r in survivors],
                {"facts": sorted(fs), "case_scope": {}})
            got_ctrl = (ctrl or {}).get("id")
            if {r["id"] for r in cands} != want_consulted or got_ctrl != want_ctrl:
                cc19_fail.append(
                    (case_id, f"consulted/controlling differ from the"
                              f" representative's: {sorted(r['id'][:8] for r in cands)}"
                              f" / {got_ctrl}"))
            cc19_seen += 1
    check("CC-19", "consolidation faithfulness: every member recomputes the"
                   " SAME Consulted and Controlling against the pinned"
                   " snapshot as the representative recorded (Prop. 2 is what"
                   " licenses disposal by citation)",
          not cc19_fail, f"{cc19_seen} units over {len(classes)} class(es)"
                         + (f"; {cc19_fail}" if cc19_fail else ""))

    # --- CC-20 ---------------------------------------------------------
    cc20 = []
    for cls in classes:
        rep = _rep_record(cls["class_id"])
        if rep is None:
            continue
        prov = svc.constitution.get_provision(cls["rulebook_version"],
                                              cls["provision_id"])
        vocab = consolidate.factor_vocabulary(prov)
        want_sig = tuple(json.loads(cls["signature"]))
        member_cases = [rep["case_id"]] + [
            m["case_id"] for m in members_of.get(cls["class_id"], [])]
        for case_id in member_cases:
            st = _case(case_id)
            facts = set(json.loads(st["facts"]))
            # (a) equal Sig under Definition 15, at the published grain
            if tuple(sorted(facts & vocab)) != want_sig:
                cc20.append((case_id, "a: signature differs at F_p"))
            # (b) one provision only
            if st["provision_id"] != cls["provision_id"]:
                cc20.append((case_id, "b: provision differs"))
            # (c) no member satisfies A6's conjunction
            if prov["absolute"]:
                cc20.append((case_id, "c: the class provision is absolute"))
            # (e) no member cites a record admitted after the snapshot
            for rid in json.loads(_case(case_id)["artifacts"]).get(
                    "1", {}).get("retrieval", {}).get("candidates", []):
                row = c.execute("SELECT resolved_at FROM precedent_record"
                                " WHERE id=?", (rid["record_id"],)).fetchone()
                if row and row["resolved_at"] > cls["formed_at"] \
                        and rid["record_id"] != rep["id"]:
                    cc20.append((case_id, "e: cites a post-snapshot record"))
        # (d) the recorded resolve result is the plain none, never none(tie)
        if rep["controlling_state"] not in ("none_empty",
                                            "none_all_distinguished"):
            cc20.append((cls["class_id"],
                         f"d: representative resolved"
                         f" {rep['controlling_state']}"))
        # (f) every member lodged inside Delta — carried on the artefact, and
        # the member list is the artefact's, so a member outside the window
        # would have to have been written there, which (g) also catches.
        if len(json.loads(cls["members"])) < cls["n0"]:
            cc20.append((cls["class_id"], "a: fewer members than N0"))
        # (g) COMPLETENESS, which is the limb the register did not have and
        # which the grain mutant needs. Every unit in the recorded docket that
        # shares the class's signature must be IN the member list. A build
        # that computed signatures on the whole fact set silently drops the
        # unit that differs outside F_p, and every other limb still passes.
        member_units = set(json.loads(cls["members"]))
        # Read from the artefact's own docket, which is the set of units the
        # boundary considered. A unit that filed more than one case engaged
        # more than one provision and clause (b) excluded it; a unit on a
        # different provision, or on an absolute one, was excluded by (b) or
        # (c). Everything else in D_t that shares the signature must be a
        # member, and a build computing signatures at the wrong grain drops
        # exactly one such unit while every other limb of this check passes.
        by_unit = {}
        for row in c.execute("SELECT case_id, facts, provision_id,"
                             " case_scope, created_at FROM case_state"):
            unit = json.loads(row["case_scope"]).get("unit")
            if unit:
                by_unit.setdefault(unit, []).append(dict(row))
        for unit in json.loads(cls["docket"]):
            if unit in member_units:
                continue
            rows = by_unit.get(unit) or []
            if len(rows) != 1:
                continue                      # clause (b) excluded it
            row = rows[0]
            if row["provision_id"] != cls["provision_id"]:
                continue
            if tuple(sorted(set(json.loads(row["facts"])) & vocab)) == want_sig:
                cc20.append((unit, "g: in the recorded docket, shares the"
                                   " class signature, eligible, and not a"
                                   " member"))
    check("CC-20", "class purity: equal signature at the published grain, one"
                   " provision, no floor, the plain none, no post-snapshot"
                   " citation — and no eligible like unit left out (g)",
          not cc20, f"{len(classes)} class(es)"
                    + (f"; {cc20}" if cc20 else ""))

    # --- CC-21 ---------------------------------------------------------
    # The clause the |Rules|*2^kappa ceiling of Proposition A_cons(ii) rests
    # on. Without it the bound is a hope. The key carries the rulebook version
    # because legislative supersession makes a record non-live, at which point
    # a later class on the same signature under the new version may
    # legitimately form.
    seen, dup = {}, []
    for r in c.execute(
            "SELECT * FROM record_effective WHERE lapsed=0 AND superseded=0"
            "   AND admission_ground='consolidation'"):
        prov = svc.constitution.get_provision(r["rulebook_version"],
                                              r["provision_id"])
        key = consolidate.signature(r["provision_id"], r["rulebook_version"],
                                    json.loads(r["facts"]),
                                    consolidate.factor_vocabulary(prov))
        if key in seen:
            dup.append(key)
        seen[key] = r["id"]
    check("CC-21", "consolidated-admission uniqueness: at most one LIVE"
                   " consolidated record per (provision, rulebook version,"
                   " factor profile), which is what makes the constant a"
                   " ceiling rather than a hope",
          not dup, f"{len(seen)} consolidated signature(s), {len(dup)} dup(s)")

    # --- CC-22 ---------------------------------------------------------
    cc22 = []
    producer = consolidate.PRODUCER_SERVICE
    # (a) the producing service holds no credential of any authority class
    if c.execute("SELECT COUNT(*) AS n FROM authority_assignment"
                 " WHERE principal_id=?", (producer,)).fetchone()["n"]:
        cc22.append("a: the class producer holds a branch assignment")
    if c.execute("SELECT COUNT(*) AS n FROM precedent_record"
                 " WHERE resolving_principal=?",
                 (producer,)).fetchone()["n"]:
        cc22.append("a: the class producer resolved a record")
    for cls in classes:
        if cls["producer_service"] != producer:
            cc22.append(f"a: {cls['class_id']} names another producer")
        # (b) temporal: the class is formed BEFORE any member is adjudicated
        rep = _rep_record(cls["class_id"])
        if rep is None:
            continue
        for case_id in [rep["case_id"]] + [
                m["case_id"] for m in members_of.get(cls["class_id"], [])]:
            st = _case(case_id)
            if st["created_at"] < cls["formed_at"]:
                cc22.append(f"b: {case_id} predates its class")
            early = c.execute(
                "SELECT COUNT(*) AS n FROM judgment_invocation"
                " WHERE case_hash=? AND invoked_at < ?",
                (st["case_hash"], cls["formed_at"])).fetchone()["n"]
            if early:
                cc22.append(f"b: {early} gate invocation(s) for {case_id}"
                            f" predate the class artefact")
        # (c) determinacy: re-run Classify with the member list permuted and
        # require the same representative and the same membership. The
        # representative is fixed by the published total order, so input
        # order can make no difference — and a build in which it did would be
        # a build where arrival order chose which unit becomes law.
        prov = svc.constitution.get_provision(cls["rulebook_version"],
                                              cls["provision_id"])
        units = []
        for n_, case_id in enumerate([rep["case_id"]] + [
                m["case_id"] for m in members_of.get(cls["class_id"], [])]):
            st = _case(case_id)
            unit = json.loads(st["case_scope"]).get("unit") or case_id
            units.append({"unit_id": unit, "case_id": case_id,
                          "provisions": [st["provision_id"]],
                          "facts": json.loads(st["facts"]),
                          "rulebook_version": st["rulebook_version"],
                          "lodged_at": cls["formed_at"]})
        again = consolidate.classify(
            list(reversed(units)), [], {cls["provision_id"]: prov},
            n0=cls["n0"], delta_seconds=cls["delta_seconds"],
            now=cls["formed_at"],
            resolve_state=lambda *_: "none_empty")
        if len(again) != 1 or again[0]["representative"] != cls["representative"] \
                or again[0]["members"] != json.loads(cls["members"]):
            cc22.append(f"c: {cls['class_id']} is not order-independent")
    check("CC-22", "no authority in class formation: the producer holds no"
                   " branch and resolved nothing, every class predates every"
                   " member's first gate invocation, and the representative"
                   " is unchanged under permutation of the input",
          not cc22, f"{len(classes)} class(es)" + (f"; {cc22}" if cc22 else ""))
    c.close()


# ===========================================================================
def report() -> int:
    width = 100
    print("\n" + "=" * width)
    print("DIGITAL JUDICIARY — CONFORMANCE REPORT"
          "  (every row computed from executed traces; none asserted)")
    print("=" * width)
    sections = [("Corpus: every mechanism exercised", "COR"),
                ("Violation probes: each guarantee fails correctly when"
                 " attacked", "PRB"),
                ("Continuous conformance checks (SDD v3.0 §4)", "CC")]
    failures = 0
    for title, prefix in sections:
        print(f"\n{title}")
        print("-" * width)
        for cid, name, ok, detail in results:
            if not cid.startswith(prefix):
                continue
            mark = "PASS" if ok else "FAIL"
            failures += 0 if ok else 1
            line = f"  [{mark}] {cid:8s} {name}"
            print(line if not detail else f"{line}  ({detail})")
    print("\nCorpus narrative")
    print("-" * width)
    for cid, text in narrative:
        print(f"  {cid:8s} {text}")
    print("\n" + "=" * width)
    total = len(results)
    print(f"RESULT: {total - failures}/{total} checks hold"
          + ("" if failures == 0 else f"  —  {failures} FAILURES"))
    print("=" * width)
    return 1 if failures else 0


def main() -> int:
    svc = bootstrap.build_services()
    keys = bootstrap.bootstrap(svc)
    assert keys, "conformance requires a fresh database (set DJ_DB)"
    httpd = httpapi.serve(svc, "127.0.0.1", PORT)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        ids = run_corpus(svc)
        run_probes(svc)
        run_cc(svc, ids)
    finally:
        httpd.shutdown()
    return report()


if __name__ == "__main__":
    sys.exit(main())
