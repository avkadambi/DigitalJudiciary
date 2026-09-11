#!/usr/bin/env python3
"""Interface conformance (L5): the inbound GitHub adapter, the outbound
disposition layer, and the human-review lane.

Deliberately a SEPARATE suite from `run_conformance.py`. The paper's Table 11
is a claim about the contract kernel, and adding interface checks to it would
silently change a number the paper reports. The kernel suite stays at exactly
48 (47 plus the A9 standing-declaration check, CC-17, which the manuscripts
report); this file answers a different question — does the translation layer
preserve the guarantees when the outside world is doing the talking?

Every check is computed from an executed trace over the live HTTP surface.
Exit 0 iff everything holds.

Run:  DJ_DB=/tmp/dji.db DJ_DEV_KEYS=1 python3 run_interface_conformance.py
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
os.environ.setdefault('DJ_LEDGER_BACKEND', 'sqlite')
os.environ.setdefault('DJ_LEDGER_ON_PG', '0')
import re
import sqlite3
import sys
import tempfile
import threading
import urllib.error
import urllib.request

os.environ.setdefault("DJ_DB", os.path.join(tempfile.mkdtemp(), "dji.db"))
os.environ["DJ_DEV_KEYS"] = "1"
os.environ.setdefault("DJ_JUDGE_MODE", "oracle")
os.environ["DJ_GITHUB_WEBHOOK_SECRET"] = "conformance-secret"
os.environ.pop("DJ_GITHUB_ALLOW_UNSIGNED", None)

from app import bootstrap, db, httpapi          # noqa: E402

PORT = int(os.environ.get("DJ_IF_PORT", "18077"))
BASE = f"http://127.0.0.1:{PORT}"
SECRET = b"conformance-secret"
KEYS = bootstrap.DEV_KEYS
FORM = {"content-type": "application/x-www-form-urlencoded"}

results: list[tuple[str, str, bool, str]] = []
narrative: list[tuple[str, str]] = []


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(_NoRedirect)


def check(cid, name, ok, detail=""):
    results.append((cid, name, bool(ok), detail))


def raw(method, path, data=None, headers=None):
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers=headers or {})
    try:
        with OPENER.open(req, timeout=20) as r:
            return r.status, r.read(), r.headers
    except urllib.error.HTTPError as e:
        return e.code, e.read(), e.headers


def api(method, path, who, body=None):
    s, b, _ = raw(method, path, json.dumps(body or {}).encode(),
                  {"authorization": f"Bearer {KEYS[who]}",
                   "content-type": "application/json"})
    return s, json.loads(b or b"{}")


def pr_event(number, files, labels=(), checks=(), title="change", body="",
             author="dev-jo", options=None):
    return json.dumps({
        "action": "opened",
        "repository": {"full_name": "acme/control-tower"},
        "pull_request": {
            "number": number, "title": title, "body": body,
            "labels": [{"name": l} for l in labels],
            "base": {"ref": "main"}, "head": {"sha": f"{number:040d}"},
            "user": {"login": author}},
        "dj_context": {
            "files": [{"filename": f} for f in files],
            "check_runs": [{"name": n, "conclusion": c} for n, c in checks]},
        "dj_options": options or {},
    }).encode()


def deliver(body, delivery, event="pull_request", sign=True, secret=SECRET):
    h = {"x-github-event": event, "x-github-delivery": delivery,
         "content-type": "application/json"}
    if sign:
        h["x-hub-signature-256"] = "sha256=" + hmac.new(
            secret, body, hashlib.sha256).hexdigest()
    s, b, _ = raw("POST", "/v1/inbound/github", body, h)
    return s, json.loads(b or b"{}")


def login(key):
    s, b, hdr = raw("POST", "/review/login", f"key={key}".encode(), FORM)
    return s, (hdr.get("set-cookie") or "").split(";")[0]


def csrf_of(page: str) -> str:
    m = re.search(r"name='csrf' value='([0-9a-f]+)'", page)
    return m.group(1) if m else ""


# ===========================================================================
def run(svc) -> dict:
    ids = {}
    c = db.open_reader()

    # -- Authentication of the inbound edge ---------------------------
    body = pr_event(101, ["services/portal/connectors/m.yaml"],
                    labels=["connector-config"],
                    checks=[("config-encryption", "success"),
                            ("secret-rotation", "success")],
                    body="Vault onboarding is queued.")
    s_unsigned, _ = deliver(body, "d-unsigned", sign=False)
    s_bad, _ = deliver(body, "d-badsig", secret=b"wrong")
    check("IF-01", "unsigned inbound event is rejected", s_unsigned == 401)
    check("IF-02", "forged signature is rejected", s_bad == 401)

    # -- A permitted PR ------------------------------------------------
    s, ok_pr = deliver(body, "d-101")
    ids["permit"] = ok_pr["session_id"]
    check("IF-03", "signed event is accepted and adjudicated",
          s == 200 and ok_pr["disposition"] == "proceed_with_conditions",
          ok_pr.get("disposition"))
    check("IF-04", "extractor version and map hash are pinned into the"
                   " session (CC-04 analogue)",
          bool(ok_pr["extractor_version"]) and
          len(ok_pr["factor_map_hash"]) == 64)
    narrative.append(("PERMIT", "connector PR -> SP-001 controls ->"
                                " permitted with conditions"))

    # -- Idempotent redelivery ----------------------------------------
    n_before = c.execute("SELECT COUNT(*) n FROM case_state").fetchone()["n"]
    s, replay = deliver(body, "d-101")
    n_after = c.execute("SELECT COUNT(*) n FROM case_state").fetchone()["n"]
    check("IF-05", "GitHub redelivery is idempotent: same session, no second"
                   " case filed",
          replay.get("idempotent_replay") is True
          and replay["session_id"] == ids["permit"] and n_before == n_after,
          f"cases {n_before}->{n_after}")

    # -- Determinism ---------------------------------------------------
    s, again = deliver(pr_event(102, ["services/portal/connectors/m.yaml"],
                                labels=["connector-config"],
                                checks=[("config-encryption", "success"),
                                        ("secret-rotation", "success")],
                                body="Vault onboarding is queued."),
                       "d-102")
    check("IF-06", "extraction is deterministic: identical signals yield an"
                   " identical factor set and disposition",
          again["factors"] == ok_pr["factors"]
          and again["disposition"] == ok_pr["disposition"]
          and again["factor_map_hash"] == ok_pr["factor_map_hash"])

    # -- Self-asserted vs observed facts -------------------------------
    s, claimed = deliver(pr_event(
        103, ["legacy/mod.py"], labels=["coverage-waiver"],
        body="dj-factor: community_audit_complete\n"), "d-103")
    row = c.execute("SELECT factors FROM pr_session WHERE session_id=?",
                    (claimed["session_id"],)).fetchone()
    sess = svc.gateway.map.extract({
        "files": [{"filename": "legacy/mod.py"}], "labels": ["coverage-waiver"],
        "body": "dj-factor: community_audit_complete\n", "title": "",
        "check_runs": []})
    check("IF-07", "author-claimed facts are recorded but distinguishable"
                   " from machine-observed ones",
          sess["self_asserted"] == ["community_audit_complete"]
          and "community_audit_complete" not in sess["observed"]
          and "community_audit_complete" in json.loads(row["factors"]))

    # -- Floor-first + A6 ----------------------------------------------
    s, floor = deliver(pr_event(
        104, ["services/screening/allowlist.yaml", "legacy/mod.py"],
        labels=["coverage-waiver"],
        title="Skip screening for pilot partners"), "d-104")
    ids["floor"] = floor["session_id"]
    filed = [r["provision_id"] for r in c.execute(
        "SELECT provision_id FROM pr_case WHERE session_id=?",
        (ids["floor"],)).fetchall()]
    check("IF-08", "floor-first: an absolute provision is adjudicated first"
                   " and the rest are recorded as not reached",
          floor["disposition"] == "blocked_absolute"
          and filed == ["SC-202"] and floor["not_reached"] == ["SC-206"],
          f"filed={filed} not_reached={floor['not_reached']}")
    lanes = {l["lane"] for l in floor["lanes_open"]}
    check("IF-09", "A6 at the interface: an absolute denial offers no"
                   " challenge lane and no human-review lane (CC-08)",
          lanes == {"amendment"}, str(sorted(lanes)))
    s, err = api("POST", f"/v1/pr/{ids['floor']}/human-review", "eng.sam",
                 {"grounds": "please look at this"})
    check("IF-10", "asking for a human on an absolute denial is refused,"
                   " not queued",
          s == 409 and err.get("code") == "absolute_no_review", str(s))
    n_rec = c.execute(
        "SELECT COUNT(*) n FROM precedent_record p JOIN pr_case pc"
        " ON pc.case_id=p.case_id WHERE pc.session_id=?",
        (ids["floor"],)).fetchone()["n"]
    check("IF-11", "an absolute denial writes no precedent",
          n_rec == 0, f"records={n_rec}")
    narrative.append(("FLOOR", "screening-bypass PR -> SC-202 short-circuits;"
                               " SC-206 never adjudicated"))

    # -- A3 control-plane routing --------------------------------------
    s, cp = deliver(pr_event(105, ["governance/rulebook.json"],
                             title="Loosen the coverage floor"), "d-105")
    ids["control"] = cp["session_id"]
    cp_cases = c.execute("SELECT COUNT(*) n FROM pr_case WHERE session_id=?",
                         (ids["control"],)).fetchone()["n"]
    check("IF-12", "a PR that edits the rulebook routes to the legislative"
                   " channel and is never adjudicated (A3)",
          cp["disposition"] == "routed_amendment" and cp_cases == 0
          and cp["cases"][0].get("amendment_id"),
          f"cases={cp_cases}")
    narrative.append(("A3", "policy-repo PR -> DraftAmendment, no case"))

    # -- The challenge ladder and A4 -----------------------------------
    s, blocked = deliver(pr_event(
        106, ["services/telematics/pkg/requirements.txt",
              "services/telematics/tenant/a.py"],
        labels=["vendor-review-pending"], title="Bump telemetry lib"),
        "d-106")
    ids["ladder"] = blocked["session_id"]
    check("IF-13", "a denied PR is blocked but challengeable, and all three"
                   " exits are offered",
          blocked["disposition"] == "blocked_challengeable"
          and {l["lane"] for l in blocked["lanes_open"]}
          == {"challenge", "human_review", "amendment"})

    s, esc = api("POST", f"/v1/pr/{ids['ladder']}/challenge", "eng.sam",
                 {"grounds": "the community audit is complete for this lib"})
    check("IF-14", "the challenge lane climbs exactly one tier",
          esc["cases"][0]["tier"] == 2, str(esc["cases"][0]["tier"]))
    s, noG = api("POST", f"/v1/pr/{ids['ladder']}/challenge", "eng.sam",
                 {"grounds": "   "})
    check("IF-15", "a challenge without grounds is refused", s == 422)

    s, hr = api("POST", f"/v1/pr/{ids['ladder']}/human-review", "eng.sam",
                {"grounds": "we need a decision before the freeze"})
    check("IF-16", "the human-review lane reaches a named person",
          hr["disposition"] == "human_review" and len(hr["review_tasks"]) == 1)
    case_id = c.execute("SELECT case_id FROM pr_case WHERE session_id=?",
                        (ids["ladder"],)).fetchone()["case_id"]
    tiers = [r["tier"] for r in c.execute(
        "SELECT tier FROM contest_event WHERE case_id=? ORDER BY seq",
        (case_id,)).fetchall()]
    check("IF-17", "A4 is not skippable: reaching the risk owner required a"
                   " recorded contest at every automated tier",
          set(tiers) >= {1, 2, 3} and svc.chain.verify_exhaustion(case_id),
          f"tiers contested {sorted(set(tiers))}")
    task_id = hr["review_tasks"][0]["task_id"]
    ids["task"] = task_id

    s, hr2 = api("POST", f"/v1/pr/{ids['ladder']}/human-review", "eng.sam",
                 {"grounds": "asking again"})
    open_tasks = c.execute(
        "SELECT COUNT(*) n FROM review_task WHERE case_id=? AND state='open'",
        (case_id,)).fetchone()["n"]
    check("IF-18", "asking twice does not open a second review task",
          open_tasks == 1, f"open={open_tasks}")
    narrative.append(("LADDER", "telematics PR -> deny -> challenge -> t2 ->"
                                " ladder walked -> risk owner"))

    # -- The review UI holds no authority ------------------------------
    s, ck_eng = login(KEYS["eng.sam"])
    st, page_b, _ = raw("GET", f"/review/{task_id}", None, {"cookie": ck_eng})
    page = page_b.decode()
    # Asserted structurally rather than by copy: 5.5 renamed the rungs to
    # plain English and moved the tier numbers into the drawer, so matching
    # display strings tested the wording, not the disclosure.
    check("IF-19", "the review screen renders the full dossier for any"
                   " authenticated principal (transparency)",
          st == 200
          and "trail2" in page              # every rung, incl. the ones skipped
          and "Contested at" in page        # the tier number is still disclosed
          and "Earlier rulings consulted" in page)
    st, err_b, _ = raw(
        "POST", f"/review/{task_id}/decide",
        f"csrf={csrf_of(page)}&decision=accept&expiry=2026-12-01"
        f"&rationale=because+I+said+so".encode(), {**FORM, "cookie": ck_eng})
    check("IF-20", "the screen cannot grant authority: a principal without"
                   " the risk-owner branch is refused by the Kernel",
          st == 403 and "requires &#x27;risk_owner&#x27;" in err_b.decode(),
          str(st))
    st, _, _ = raw("POST", f"/review/{task_id}/decide",
                   b"csrf=deadbeef&decision=decline&rationale=x",
                   {**FORM, "cookie": ck_eng})
    check("IF-21", "a forged form token is refused", st == 403, str(st))
    st, _, _ = raw("POST", f"/review/{task_id}/decide",
                   b"csrf=x&decision=decline&rationale=x", FORM)
    check("IF-22", "an unauthenticated decision is refused", st == 401)

    # -- The risk owner decides ----------------------------------------
    s, ck_ro = login(KEYS["coo.pat"])
    st, page_b, _ = raw("GET", f"/review/{task_id}", None, {"cookie": ck_ro})
    tok = csrf_of(page_b.decode())
    st, _, hdr = raw(
        "POST", f"/review/{task_id}/decide",
        f"csrf={tok}&decision=accept&expiry=2026-12-01"
        f"&rationale=Bounded+pilot%3B+vendor+review+lands+in+three+weeks"
        .encode(), {**FORM, "cookie": ck_ro})
    check("IF-23", "the risk owner's decision is accepted and redirects to"
                   " the decided docket", st == 303, str(st))
    rec = c.execute(
        "SELECT p.* FROM precedent_record p JOIN pr_case pc"
        " ON pc.case_id=p.case_id WHERE pc.session_id=?"
        " AND p.is_acceptance=1", (ids["ladder"],)).fetchone()
    ref = c.execute(
        "SELECT COUNT(*) n FROM precedent_lifecycle_event"
        " WHERE record_id=? AND event_type='referral_emitted'",
        (rec["id"],)).fetchone()["n"] if rec else 0
    check("IF-24", "A7 survives the UI: the acceptance carries a mandatory"
                   " expiry and emitted its referral",
          rec is not None and rec["expiry"] and rec["authority_tier"] == 4
          and ref == 1)
    s, after = api("GET", f"/v1/pr/{ids['ladder']}", "eng.sam")
    check("IF-25", "the accepted risk unblocks the pull request",
          after["disposition"] == "proceed_with_conditions",
          after["disposition"])
    st, _, _ = raw("POST", f"/review/{task_id}/decide",
                   f"csrf={tok}&decision=decline&rationale=changed+my+mind"
                   .encode(), {**FORM, "cookie": ck_ro})
    check("IF-26", "a decided review cannot be decided again", st == 409,
          str(st))
    narrative.append(("SIGN", "risk owner accepts with expiry; referral"
                              " emitted; PR unblocked"))

    # -- Proposition 2 through the interface ---------------------------
    s, growth = deliver(pr_event(
        107, ["services/portal/analytics/funnel.ts"],
        labels=["growth-experiment"], title="Add funnel telemetry"), "d-107")
    s, growth = api("POST", f"/v1/pr/{growth['session_id']}/human-review",
                    "eng.sam", {"grounds": "growth needs this for Q4"})
    btask = growth["review_tasks"][0]["task_id"]
    st, page_b, _ = raw("GET", f"/review/{btask}", None, {"cookie": ck_ro})
    bpage = page_b.decode()
    check("IF-27", "Proposition 2 in the interface: when renewal is barred,"
                   " the accept control is absent, not merely disabled",
          # The load-bearing claim is that the control is not emitted at all.
          # Asserted against the form input, not the button label, so a copy
          # change cannot make this pass or fail spuriously.
          "name='decision' value='accept'" not in bpage
          and "name='decision' value='decline'" in bpage
          and "Proposition" in bpage)
    st, err_b, _ = raw(
        "POST", f"/review/{btask}/decide",
        f"csrf={csrf_of(bpage)}&decision=accept&expiry=2026-12-01"
        f"&rationale=we+want+it".encode(), {**FORM, "cookie": ck_ro})
    check("IF-28", "and the Kernel refuses it independently of the screen",
          st == 422 and "Proposition 2" in err_b.decode(), str(st))
    st, _, _ = raw(
        "POST", f"/review/{btask}/decide",
        f"csrf={csrf_of(bpage)}&decision=decline"
        f"&rationale=The+lawmakers+already+rejected+this".encode(),
        {**FORM, "cookie": ck_ro})
    s, bsess = api("GET", f"/v1/pr/{growth['session_id']}", "eng.sam")
    check("IF-29", "an upheld denial at tier k leaves no challenge lane",
          bsess["disposition"] == "blocked_final"
          and {l["lane"] for l in bsess["lanes_open"]} == {"amendment"},
          bsess["disposition"])
    narrative.append(("BARRED", "growth PR -> renewal barred by Prop. 2 ->"
                                " decline -> blocked, amendment only"))

    # -- Nothing is engaged --------------------------------------------
    s, quiet = deliver(pr_event(108, ["docs/readme.md"],
                                title="Fix a typo"), "d-108")
    check("IF-30", "a PR that engages no provision proceeds, with no case"
                   " and no precedent",
          quiet["disposition"] == "proceed" and quiet["provisions"] == []
          and quiet["cases"] == [])

    # -- Def. 7 preserved through the interface ------------------------
    t1_only = c.execute(
        "SELECT COUNT(*) n FROM precedent_record p JOIN case_state s"
        " ON s.case_id=p.case_id JOIN pr_case pc ON pc.case_id=p.case_id"
        " WHERE s.status IN ('decided_t1','denied_absolute')").fetchone()["n"]
    check("IF-31", "Def. 7 through the interface: PRs resolved at tier 1"
                   " leave no precedent behind", t1_only == 0,
          f"leaked={t1_only}")

    # -- Consolidation is not reachable through the interface -----------
    #
    # Forming a class is a power over admission. A1-A4 confer it on no
    # authority, and the review screen is where a human authority meets the
    # system — so the screen is precisely where a back door would be found.
    # These two checks assert there is none: the gateway exposes no route that
    # writes or edits a class artefact, and the artefact table is append-only
    # through the same connection the interface holds.
    routes = []
    for path, method in (("/v1/consolidation/classes", "POST"),
                         ("/v1/consolidation/classes", "GET"),
                         ("/review/consolidate", "POST")):
        st, _b, _h = raw(
            method, path, b"{}" if method == "POST" else None,
            {"authorization": f"Bearer {KEYS['alice.grc']}",
             "content-type": "application/json"})
        if st not in (404, 405):
            routes.append((method, path, st))
    check("IF-32", "the interface exposes no route that forms or edits a"
                   " consolidation class: class formation is pipeline"
                   " machinery and reaches no authority, including the"
                   " highest one",
          not routes, f"{routes or 'no such route on any surface'}")

    ic = db.open_reader()
    engaged = ic.execute(
        "SELECT COUNT(*) n FROM precedent_record"
        " WHERE admission_ground='consolidation'").fetchone()["n"]
    ic.close()
    check("IF-33", "no record admitted through the interface carries the"
                   " consolidation ground: everything the gateway files"
                   " enters under clause (i) or not at all",
          engaged == 0, f"{engaged} consolidated record(s) via the gateway")

    return ids


def run_probes(svc, ids):
    """Each interface guarantee must fail correctly when attacked."""
    w = db.open_writer()

    def must_abort(sql, args=()):
        try:
            w.execute(sql, args)
            w.commit()
            return False
        except sqlite3.IntegrityError:
            return True
        except sqlite3.DatabaseError:
            return True

    check("IFP-01", "an inbound session cannot be rewritten after the fact",
          must_abort("UPDATE pr_session SET factors='[]' WHERE session_id=?",
                     (ids["floor"],)))
    check("IFP-02", "an inbound session cannot be deleted",
          must_abort("DELETE FROM pr_session WHERE session_id=?",
                     (ids["floor"],)))
    check("IFP-03", "a recorded disposition cannot be edited; the log is"
                    " append-only",
          must_abort("UPDATE pr_disposition SET disposition='proceed'"
                     " WHERE session_id=?", (ids["floor"],)))
    check("IFP-04", "a disposition cannot be deleted",
          must_abort("DELETE FROM pr_disposition WHERE session_id=?",
                     (ids["floor"],)))
    check("IFP-05", "what we told GitHub cannot be rewritten",
          must_abort("UPDATE outbound_delivery SET payload='{}'"
                     " WHERE session_id=?", (ids["floor"],)))
    check("IFP-06", "a decided review cannot be reopened",
          must_abort("UPDATE review_task SET state='open', decided_by=NULL,"
                     " closed_at=NULL WHERE task_id=?", (ids["task"],)))
    check("IFP-07", "a review task cannot be closed without a named decider",
          must_abort("UPDATE review_task SET state='decided'"
                     " WHERE task_id=?", (ids["task"],)))
    check("IFP-08", "a second session cannot claim the same GitHub delivery",
          must_abort(
              "INSERT INTO pr_session (session_id, delivery_id, source,"
              " event_type, action, repo, pr_number, head_sha, pr_author,"
              " filed_by, extractor_version, factor_map_hash, factors,"
              " provisions, not_reached, case_scope, escalation_policy,"
              " payload_hash, received_at) VALUES"
              " ('PRS-forged','d-104','github','pull_request','opened',"
              "  'a/b',1,'x','y','z','v','h','[]','[]','[]','{}','manual',"
              "  'p','2026-01-01T00:00:00.000000+00:00')"))

    r = db.open_reader()
    check("IFP-09", "the inbound gateway principal holds no branch: it can"
                    " file and contest, never resolve or accept",
          svc.registry.resolve_branch("svc:github") is None)
    orphan = r.execute(
        "SELECT COUNT(*) n FROM pr_disposition d WHERE NOT EXISTS"
        " (SELECT 1 FROM outbound_delivery o WHERE o.session_id=d.session_id"
        "  AND o.target='github_checks')").fetchone()["n"]
    check("IFP-11", "a class artefact cannot be rewritten through the"
                    " connection the interface holds: the member list and the"
                    " snapshot a class was decided against are fixed when the"
                    " class forms",
          must_abort("INSERT INTO consolidation_class (class_id,"
                     " snapshot_hash, rulebook_version, provision_id,"
                     " signature, n0, delta_seconds, members, docket,"
                     " representative, producer_service, formed_at)"
                     " VALUES ('ifp','s','rb-000001','SC-201','[]',2,3600,"
                     " '[\"a\"]','[\"a\"]','a','x','t')")
          is False
          and must_abort("UPDATE consolidation_class SET members='[]'"))
    check("IFP-10", "every disposition produced an outbound record: the audit"
                    " trail does not depend on GitHub being reachable",
          orphan == 0, f"silent dispositions={orphan}")


def report() -> int:
    width = 100
    print("\n" + "=" * width)
    print("DIGITAL JUDICIARY — INTERFACE CONFORMANCE (L5)")
    print("=" * width)
    sections = [("Inbound / outbound / review", "IF-"),
                ("Violation probes", "IFP-")]
    failures = 0
    for title, prefix in sections:
        print(f"\n{title}")
        print("-" * width)
        for cid, name, ok, detail in results:
            if not cid.startswith(prefix):
                continue
            failures += 0 if ok else 1
            line = f"  [{'PASS' if ok else 'FAIL'}] {cid:8s} {name}"
            print(line if not detail else f"{line}  ({detail})")
    print("\nTrace narrative")
    print("-" * width)
    for cid, text in narrative:
        print(f"  {cid:8s} {text}")
    print("\n" + "=" * width)
    total = len(results)
    print(f"RESULT: {total - failures}/{total} interface checks hold"
          + ("" if failures == 0 else f"  —  {failures} FAILURES"))
    print("=" * width)
    return 1 if failures else 0


def main() -> int:
    svc = bootstrap.build_services()
    keys = bootstrap.bootstrap(svc)
    assert keys, "interface conformance requires a fresh database (set DJ_DB)"
    httpd = httpapi.serve(svc, "127.0.0.1", PORT)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        ids = run(svc)
        run_probes(svc, ids)
    finally:
        httpd.shutdown()
    return report()


if __name__ == "__main__":
    sys.exit(main())
