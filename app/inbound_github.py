"""L5 Inbound: a pull request becomes cases; resolutions become PR outcomes.

The gateway is deliberately thin and deliberately powerless. It can:
  * verify that an event really came from GitHub (HMAC, constant-time),
  * translate PR signals into facts (prfacts, versioned and pinned),
  * decide *which* provisions are engaged and in what order,
  * file cases, relay challenges, and open review tasks,
  * write down everything it did.

It cannot decide anything, cannot admit a precedent, and cannot grant itself
authority. Every adjudicative step below is a call into the Kernel, which
re-checks the axioms at the point of action regardless of what this file
believes. If the whole gateway were replaced by a hostile implementation, the
worst it could do is file bad cases and lie to GitHub — the ledger would still
be sound, and the provenance would still show what happened.

Floor-first evaluation. When a PR trips both an absolute provision and an
ordinary one, the absolute is adjudicated first and the rest are recorded as
`not_reached`. This is A6 taken seriously: a floor is not one input among
several to be weighed, so the system must not produce a record that looks like
it weighed anything.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import uuid

from . import db, outbound
from .db import now_iso
from .kernel import KernelError, canonical, sha256
from .prfacts import ADJUDICABLE, FactorMap, normalize_event

BOT_PRINCIPAL = os.environ.get("DJ_GITHUB_PRINCIPAL", "svc:github")
WEBHOOK_SECRET = os.environ.get("DJ_GITHUB_WEBHOOK_SECRET", "")
ALLOW_UNSIGNED = os.environ.get("DJ_GITHUB_ALLOW_UNSIGNED") == "1"
DEFAULT_ESCALATION = os.environ.get("DJ_PR_ESCALATION", "manual")
K = 4

# Where pull requests live on the web. Configurable because GitHub Enterprise
# is not github.com, and a dead link inside a legislative package is worse
# than no link — it looks like evidence and isn't.
GITHUB_WEB = os.environ.get("DJ_GITHUB_WEB", "https://github.com").rstrip("/")


class InboundError(Exception):
    def __init__(self, msg: str, status: int = 400, code: str = "inbound"):
        super().__init__(msg)
        self.status, self.code = status, code


def verify_signature(raw: bytes, header: str | None) -> None:
    """GitHub's X-Hub-Signature-256, compared in constant time.

    An unsigned deployment is allowed only when it is asked for explicitly,
    because an inbound endpoint that files cases on anyone's say-so is a way
    to pollute the precedent store with attacker-chosen facts."""
    if not WEBHOOK_SECRET:
        if ALLOW_UNSIGNED:
            return
        raise InboundError(
            "inbound webhook is not configured: set DJ_GITHUB_WEBHOOK_SECRET,"
            " or DJ_GITHUB_ALLOW_UNSIGNED=1 for a local run", 503,
            "webhook_unconfigured")
    if not header or not header.startswith("sha256="):
        raise InboundError("missing X-Hub-Signature-256", 401, "unsigned")
    expected = "sha256=" + hmac.new(WEBHOOK_SECRET.encode(), raw,
                                    hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, header):
        raise InboundError("signature mismatch", 401, "bad_signature")


class PRGateway:
    def __init__(self, svc, path: str | None = None):
        self.svc = svc
        self._w = db.open_writer(path)
        self._r = db.open_reader(path)
        self.map = FactorMap()
        self.log, self.checks, self.comments = outbound.build_outbound(path)
        from .review import ReviewQueue
        self.reviews = ReviewQueue(self.log, path)
        self.base_url = os.environ.get("DJ_PUBLIC_URL", "")

    # ==================================================================
    # Intake
    # ==================================================================
    def receive(self, headers: dict, raw: bytes) -> dict:
        verify_signature(raw, headers.get("x-hub-signature-256"))
        try:
            payload = json.loads(raw or b"{}")
        except json.JSONDecodeError as e:
            raise InboundError(f"malformed payload: {e}", 422, "bad_json")

        event = headers.get("x-github-event", "simulator")
        delivery = headers.get("x-github-delivery") or str(uuid.uuid4())
        action = payload.get("action", "submit")

        prior = self._r.execute(
            "SELECT session_id FROM pr_session WHERE delivery_id=?",
            (delivery,)).fetchone()
        if prior:
            # Redelivery. GitHub retries; the answer must not change and a
            # second set of cases must not be filed.
            return {**self.session_view(prior["session_id"]),
                    "idempotent_replay": True}

        # A button click on the check run comes back as its own event and is
        # a lane action on an existing session, not a new one.
        if event == "check_run" and action == "requested_action":
            return self._requested_action(payload)

        if (event, action) not in ADJUDICABLE:
            return {"disposition": "ignored", "event": event,
                    "action": action,
                    "reason": "event is not adjudicable"}

        pr = normalize_event(event, payload)
        scenario = payload.get("dj_simulation")
        return self._adjudicate_pr(pr, delivery, event, action, raw,
                                   payload.get("dj_options") or {},
                                   scenario=scenario)

    def _scenario_extraction(self, scenario: dict) -> dict:
        """Facts for a replayed scenario, which never had GitHub signals.

        The demo corpus states its facts and its engaged provisions outright,
        because in the original simulation both were scenario properties
        rather than things inferred from a diff. Pretending otherwise would
        mean inventing a factor map and then measuring our own invention, so
        the provenance is recorded as `declared` and the extractor version
        says plainly that no extraction happened.
        """
        factors = sorted(set(scenario.get("factors") or []))
        return {
            "extractor_version": "scenario/1.0",
            "factor_map_hash": sha256(canonical(
                {"factors": factors,
                 "provisions": sorted(scenario.get("provisions") or [])})),
            "factors": factors,
            "observed": factors,
            "self_asserted": [],
            "provenance": {f: "declared" for f in factors},
        }

    def _adjudicate_pr(self, pr: dict, delivery: str, event: str, action: str,
                       raw: bytes, options: dict,
                       scenario: dict | None = None) -> dict:
        if scenario is not None:
            ex = self._scenario_extraction(scenario)
            scope = dict(scenario.get("scope") or {})
            control_plane = "constitution" in (scenario.get("provisions") or [])
            declared = [p for p in (scenario.get("provisions") or [])
                        if p != "constitution"]
        else:
            ex = self.map.extract(pr)
            scope = self.map.scope(pr)
            control_plane = self.map.is_control_plane(pr)
            declared = None
        author = self._principal_for(pr.get("author", ""))
        escalation = options.get("escalation") or DEFAULT_ESCALATION
        if escalation not in ("manual", "auto"):
            raise InboundError("escalation must be manual|auto", 422)

        session_id = f"PRS-{uuid.uuid4().hex[:10]}"
        # Derived before any branch below files a session: a control-plane
        # pull request belongs to a tenant too, and its amendment must be
        # attributable to the constitution it proposes to change.
        org = self._org_for(declared if declared is not None
                            else self.map.provisions_engaged(ex["factors"]))
        if org is None and scenario:
            # A control-plane change engages only "constitution", so no clause
            # names its tenant. A replayed scenario may declare one.
            org = scenario.get("organization")
        if org is None:
            # Trusted deployment config — never the webhook body.
            from . import enterprise
            org = enterprise.repo_organization(pr.get("repo") or "")

        # A3 first of all: a change to the rulebook is never a case.
        if control_plane:
            routed = self.svc.adjudicator.submit_case(
                "constitution", ex["factors"], author,
                {**scope, "organization": org,
                 # Everything a lawmaker needs to find the actual edit.
                 "control_plane": {
                     "repo": pr.get("repo"), "number": pr.get("number"),
                     "title": pr.get("title"), "author": pr.get("author"),
                     "session_id": session_id,
                     "files": [f.get("filename") if isinstance(f, dict)
                               else f for f in (pr.get("files") or [])][:12],
                     # A replayed scenario has no pull request to open. Say so
                     # rather than linking somewhere that does not exist.
                     "source": ("simulator" if event == "simulator"
                                else "github"),
                     "url": (f"{GITHUB_WEB}/{pr.get('repo')}/pull/"
                             f"{pr.get('number')}"
                             if event != "simulator" and pr.get("repo")
                             else None),
                 }})
            self._insert_session(session_id, delivery, event, action, pr,
                                 author, ex, [], [], scope, escalation, raw, org)
            detail = [{"provision_id": "constitution",
                       "outcome": "not_adjudicated",
                       "rationale": routed["rationale"],
                       "amendment_id": routed["amendment_id"],
                       "controlling_state": "n/a", "tier": 0}]
            return self._dispose(session_id, "routed_amendment", "amendment",
                                 "A3: adjudication holds no amendment"
                                 " authority", detail, author, ex)

        engaged = self._order_provisions(ex["factors"], declared, org)
        if not engaged:
            self._insert_session(session_id, delivery, event, action, pr,
                                 author, ex, [], [], scope, escalation, raw, org)
            return self._dispose(session_id, "proceed", "request",
                                 "no provision is engaged by these facts",
                                 [], author, ex)

        # ---- file the cases, floor-first ----------------------------
        filed, detail, not_reached = [], [], []
        stop = False
        for seq, (pid, absolute) in enumerate(engaged):
            if stop:
                not_reached.append(pid)
                continue
            res = self.svc.adjudicator.submit_case(
                pid, ex["factors"], author, {**scope, "organization": org})
            filed.append({"case_id": res["case_id"], "provision_id": pid,
                          "absolute": absolute, "seq": seq})
            detail.append(self._case_detail(res, pid, absolute))
            if absolute and res["decision"] == "deny":
                stop = True          # A6: nothing below a floor gets weighed

        self._insert_session(session_id, delivery, event, action, pr, author,
                             ex, filed, not_reached, scope, escalation, raw, org)
        for f in filed:
            self._w.execute(
                "INSERT INTO pr_case (session_id, case_id, provision_id,"
                " absolute, seq) VALUES (?,?,?,?,?)",
                (session_id, f["case_id"], f["provision_id"],
                 1 if f["absolute"] else 0, f["seq"]))
        self._w.commit()

        disposition = outbound.worst([d["disposition"] for d in detail])
        result = self._dispose(session_id, disposition, "intake",
                               "initial adjudication", detail, author, ex)

        if escalation == "auto" and disposition == "blocked_challengeable":
            return self.challenge(
                session_id, author,
                "auto-escalation (simulation mode): the tier-1 denial is"
                " contested by policy, not by a human judgement",
                auto=True)
        return result

    # ==================================================================
    # Lanes
    # ==================================================================
    def challenge(self, session_id: str, actor: str, grounds: str,
                  auto: bool = False) -> dict:
        """Challenge lane: every blocking case in the session climbs a tier."""
        session = self._session_row(session_id)
        if not session:
            raise InboundError("session not found", 404, "no_session")
        if not (grounds or "").strip():
            raise InboundError("grounds are mandatory", 422, "no_grounds")

        detail, escalated = [], 0
        for pc in self._cases(session_id):
            case = self.svc.adjudicator.get_case(pc["case_id"])
            if case is None or case["status"] in ("final", "denied_absolute"):
                detail.append(self._final_case_detail(pc, case))
                continue
            d = self._climb(pc, actor, grounds, once=not auto)
            detail.append(d)
            escalated += 1

        disposition = outbound.worst([d["disposition"] for d in detail])
        res = self._dispose(session_id, disposition, "challenge",
                            ("auto-escalated" if auto else "challenged")
                            + f" by {actor}", detail, actor)
        if disposition == "human_review":
            self._open_reviews(session_id, detail, actor)
            res = self.session_view(session_id)
        res["escalated_cases"] = escalated
        return res

    def request_human_review(self, session_id: str, actor: str,
                             grounds: str) -> dict:
        """Human-review lane. A4 is not negotiable: tier k may only be reached
        after every automated tier has actually been contested, so asking for
        a human walks the ladder rather than skipping it, and the contest
        chain records each rung."""
        session = self._session_row(session_id)
        if not session:
            raise InboundError("session not found", 404, "no_session")
        if not (grounds or "").strip():
            raise InboundError("grounds are mandatory", 422, "no_grounds")

        detail = []
        for pc in self._cases(session_id):
            case = self.svc.adjudicator.get_case(pc["case_id"])
            if case is None:
                continue
            if case["status"] == "denied_absolute":
                raise InboundError(
                    "A6: an absolute provision has no human-review lane."
                    " The only exit is a proposed amendment.", 409,
                    "absolute_no_review")
            if case["status"] == "final":
                detail.append(self._final_case_detail(pc, case))
                continue
            detail.append(self._climb(pc, actor, grounds, once=False))

        disposition = outbound.worst([d["disposition"] for d in detail]) \
            if detail else "proceed"
        self._dispose(session_id, disposition, "human_review",
                      f"human review requested by {actor}", detail, actor)
        if disposition == "human_review":
            self._open_reviews(session_id, detail, actor)
        return self.session_view(session_id)

    def _climb(self, pc: dict, actor: str, grounds: str, once: bool) -> dict:
        """Escalate one case, one rung (once=True) or until it stops moving."""
        case_id = pc["case_id"]
        while True:
            r = self.svc.adjudicator.challenge(case_id, actor, grounds)
            if r.get("status") == "awaiting_risk_owner":
                return {"case_id": case_id,
                        "provision_id": pc["provision_id"],
                        "disposition": "human_review",
                        "tier": K, "outcome": "awaiting_risk_owner",
                        "renewal_guard": r.get("renewal_guard"),
                        "rationale": "the automated tiers are exhausted;"
                                     " a risk owner must decide",
                        "controlling_state": "n/a"}
            d = {"case_id": case_id, "provision_id": pc["provision_id"],
                 "tier": r["tier"], "outcome": r["decision"],
                 "controlling": r.get("controlling"),
                 "controlling_state": r.get("controlling_state"),
                 "rationale": r.get("rationale", ""),
                 "disposition": outbound.outcome_to_disposition(
                     r["decision"], absolute=False, final=False)}
            if once or d["disposition"] != "blocked_challengeable":
                if d["disposition"] != "blocked_challengeable":
                    # The challenge succeeded: accept the resolution so the
                    # eventual record is admitted through the Gate (Def. 7).
                    acc = self.svc.adjudicator.accept_resolution(case_id, actor)
                    d["record_id"] = acc.get("record_id")
                    d["final"] = True
                return d

    # ==================================================================
    # Human review decision
    # ==================================================================
    def decide_review(self, task_id: str, principal: str, decision: str,
                      rationale: str, expiry: str | None) -> dict:
        task = self.reviews.get(task_id)
        if not task:
            raise InboundError("review task not found", 404, "no_task")
        if task["state"] != "open":
            raise InboundError("this review is already decided", 409,
                               "task_closed")
        # Authority is re-checked inside risk_decision; the UI holds none.
        res = self.svc.adjudicator.risk_decision(
            task["case_id"], principal, decision, rationale, expiry)
        self.reviews.close(task_id, res["decision"], principal,
                           res.get("record_id"))

        session_id = task["session_id"]
        detail = []
        for pc in self._cases(session_id):
            case = self.svc.adjudicator.get_case(pc["case_id"])
            detail.append(self._final_case_detail(pc, case))
        disposition = outbound.worst([d["disposition"] for d in detail])
        self._dispose(session_id, disposition, "human_review",
                      f"risk owner {principal} decided: {res['decision']}",
                      detail, principal)
        return {**res, "task_id": task_id, "session_id": session_id,
                "disposition": disposition}

    # ==================================================================
    # Helpers
    # ==================================================================
    def _requested_action(self, payload: dict) -> dict:
        ident = (payload.get("requested_action") or {}).get("identifier", "")
        head = ((payload.get("check_run") or {}).get("head_sha")
                or (payload.get("pull_request") or {}).get("head", {}).get("sha"))
        actor = self._principal_for(
            (payload.get("sender") or {}).get("login", ""))
        row = self._r.execute(
            "SELECT session_id FROM pr_session WHERE head_sha=?"
            " ORDER BY received_at DESC LIMIT 1", (head,)).fetchone()
        if not row:
            raise InboundError("no session for that commit", 404, "no_session")
        sid = row["session_id"]
        grounds = (f"requested from the pull request check by {actor}"
                   f" (action {ident})")
        if ident == "dj_challenge":
            return self.challenge(sid, actor, grounds)
        if ident == "dj_review":
            return self.request_human_review(sid, actor, grounds)
        return {"session_id": sid, "disposition": "ignored",
                "reason": f"unhandled action {ident}"}

    def _org_for(self, provision_ids: list[str]) -> str | None:
        """Which tenant this pull request belongs to.

        Read from the constitution via the clauses it engages, not from the
        payload. A webhook cannot declare which tenant it is filing into.
        """
        rb = self.svc.constitution.current_version()
        for pid in provision_ids:
            if pid == "constitution":
                continue
            row = self._r.execute(
                "SELECT organization FROM provision"
                " WHERE version_id=? AND provision_id=?",
                (rb, pid)).fetchone()
            if row and row["organization"]:
                return row["organization"]
        return None

    def _order_provisions(self, factors: list[str],
                          declared: list[str] | None = None,
                          org: str | None = None
                          ) -> list[tuple[str, bool]]:
        """Engaged provisions, absolutes first, deterministic within class.

        `declared` lets a replayed scenario name the provisions it engages
        instead of having them inferred from signals. It does NOT let the
        caller decide what is absolute: that is read from the live
        constitution either way, so A6 ordering is never caller-supplied.
        """
        rb = self.svc.constitution.current_version()
        out = []
        pids = (declared if declared is not None
                else self.map.provisions_engaged(factors))
        for pid in pids:
            try:
                prov = self.svc.constitution.get_provision(rb, pid, org=org)
            except KernelError:
                continue          # provision retired by amendment; skip
            out.append((pid, bool(prov["absolute"])))
        return sorted(out, key=lambda t: (0 if t[1] else 1, t[0]))

    def _principal_for(self, login: str) -> str:
        mapping = json.loads(os.environ.get("DJ_GITHUB_USER_MAP", "{}"))
        pid = mapping.get(login, BOT_PRINCIPAL)
        row = self._r.execute("SELECT 1 FROM principal WHERE principal_id=?",
                              (pid,)).fetchone()
        return pid if row else BOT_PRINCIPAL

    def _case_detail(self, res: dict, pid: str, absolute: bool) -> dict:
        return {
            "case_id": res["case_id"],
            "provision_id": pid,
            "absolute": absolute,
            "tier": res.get("tier", 1),
            "outcome": res["decision"],
            "conditions": res.get("conditions"),
            "consulted": res.get("consulted", []),
            "controlling": res.get("controlling"),
            "controlling_state": res.get("controlling_state"),
            "degradations": res.get("degradations", []),
            "rationale": res.get("rationale", ""),
            "disposition": outbound.outcome_to_disposition(
                res["decision"], absolute and res["decision"] == "deny",
                final=bool(res.get("final"))),
        }

    def _final_case_detail(self, pc: dict, case: dict | None) -> dict:
        if case is None:
            return {"case_id": pc["case_id"],
                    "provision_id": pc["provision_id"],
                    "disposition": "proceed", "outcome": "unknown",
                    "controlling_state": "n/a", "tier": 0, "rationale": ""}
        rec = None
        if case.get("final_record_id"):
            rec = self.svc.ledger.get(case["final_record_id"])
        outcome = (rec or {}).get("interpretation", {}).get("outcome") \
            if rec else ("deny" if case["status"] == "denied_absolute"
                         else "permit")
        absolute = case["status"] == "denied_absolute"
        final = case["status"] in ("final", "denied_absolute")
        return {
            "case_id": pc["case_id"], "provision_id": pc["provision_id"],
            "absolute": absolute, "tier": case["current_tier"],
            "outcome": outcome,
            "record_id": case.get("final_record_id"),
            "controlling": (rec or {}).get("controlling_id"),
            "controlling_state": (rec or {}).get("controlling_state", "n/a"),
            "rationale": (rec or {}).get("rationale_text", ""),
            "expiry": (rec or {}).get("expiry"),
            "disposition": ("human_review"
                            if case["status"] == "awaiting_risk_owner"
                            else outbound.outcome_to_disposition(
                                outcome, absolute, final)),
        }

    def _open_reviews(self, session_id: str, detail: list[dict],
                      actor: str) -> None:
        session = self._session_row(session_id)
        rb = session["rulebook_version"] if "rulebook_version" in \
            session.keys() else self.svc.constitution.current_version()
        for d in detail:
            if d["disposition"] != "human_review":
                continue
            prov = self.svc.constitution.get_provision(
                self.svc.constitution.current_version(), d["provision_id"])
            case = self.svc.adjudicator.get_case(d["case_id"])
            trail = [dict(r) for r in self._r.execute(
                "SELECT tier, actor, grounds, ts, chain_hash FROM"
                " contest_event WHERE case_id=? ORDER BY seq",
                (d["case_id"],)).fetchall()]
            artifacts = self._artifacts(d["case_id"])
            last = artifacts.get(str(K - 1)) or {}
            summary = {
                "session_id": session_id,
                "provision_id": d["provision_id"],
                "provision_text": prov["text"],
                "absolute": prov["absolute"],
                "facts": case["facts"] if case else [],
                "repo": session["repo"],
                "pr_number": session["pr_number"],
                "pr_url": (f"{GITHUB_WEB}/{session['repo']}/pull/"
                           f"{session['pr_number']}"),
                "head_sha": session["head_sha"],
                "contested_tier": K - 1,
                "trail": trail,
                "rationale": (last.get("decision", {})
                              .get("rationale_text", d.get("rationale", ""))),
                "consulted": [c["record_id"] for c in
                              last.get("retrieval", {}).get("candidates", [])],
                "verdicts": last.get("judgments", {}).get("verdicts", []),
                "controlling_state": last.get("ordering", {})
                                         .get("controlling_state"),
                "renewal_guard": d.get("renewal_guard"),
                "requested_by": actor,
                "rulebook_version": rb,
            }
            title = (f"Risk decision: {d['provision_id']} on "
                     f"{session['repo']}#{session['pr_number']}")
            self.reviews.open(session_id, d["case_id"], d["provision_id"],
                              title, summary,
                              org=session["organization"]
                              if "organization" in session.keys() else None)

    def _artifacts(self, case_id: str) -> dict:
        row = self._r.execute(
            "SELECT artifacts FROM case_state WHERE case_id=?",
            (case_id,)).fetchone()
        return json.loads(row["artifacts"]) if row else {}

    def _insert_session(self, session_id, delivery, event, action, pr, author,
                        ex, filed, not_reached, scope, escalation, raw,
                        org=None):
        self._w.execute(
            "INSERT INTO pr_session (session_id, delivery_id, source,"
            " event_type, action, repo, pr_number, head_sha, pr_author,"
            " filed_by, extractor_version, factor_map_hash, factors,"
            " provisions, not_reached, case_scope, escalation_policy,"
            " payload_hash, received_at, organization)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (session_id, delivery,
             "github" if event != "simulator" else "simulator",
             event, action, pr["repo"], pr["number"], pr["head_sha"],
             pr["author"], author, ex["extractor_version"],
             ex["factor_map_hash"], canonical(ex["factors"]),
             canonical([f["provision_id"] for f in filed]),
             canonical(not_reached), canonical(scope), escalation,
             sha256(raw.decode("utf-8", "replace")), now_iso(), org))
        self._w.commit()

    def _dispose(self, session_id: str, disposition: str, lane: str,
                 reason: str, detail: list[dict], actor: str,
                 ex: dict | None = None) -> dict:
        self._w.execute(
            "INSERT INTO pr_disposition (session_id, disposition, lane,"
            " reason, detail, actor, occurred_at) VALUES (?,?,?,?,?,?,?)",
            (session_id, disposition, lane, reason, canonical(detail),
             actor, now_iso()))
        self._w.commit()
        self._emit(session_id, disposition, detail, ex)
        return self.session_view(session_id)

    def _emit(self, session_id: str, disposition: str, detail: list[dict],
              ex: dict | None) -> None:
        session = dict(self._session_row(session_id))
        session["factors"] = json.loads(session["factors"])
        session["not_reached"] = json.loads(session["not_reached"])
        session["provenance"] = (ex or {}).get("provenance", {})
        check = outbound.check_run_payload(session, detail, disposition,
                                           self.base_url)
        self.checks.deliver(session_id, "check_run", check)
        self.comments.deliver(session_id, "pr_comment",
                              {"body": check["output"]["summary"]})

    def _session_row(self, session_id: str):
        return self._r.execute(
            "SELECT * FROM pr_session WHERE session_id=?",
            (session_id,)).fetchone()

    def _cases(self, session_id: str) -> list[dict]:
        return [dict(r) for r in self._r.execute(
            "SELECT * FROM pr_case WHERE session_id=? ORDER BY seq",
            (session_id,)).fetchall()]

    # ==================================================================
    # Read model
    # ==================================================================
    def session_view(self, session_id: str) -> dict:
        row = self._r.execute(
            "SELECT * FROM pr_session_current WHERE session_id=?",
            (session_id,)).fetchone()
        if not row:
            raise InboundError("session not found", 404, "no_session")
        d = dict(row)
        history = [dict(r) for r in self._r.execute(
            "SELECT disposition, lane, reason, actor, occurred_at"
            " FROM pr_disposition WHERE session_id=? ORDER BY seq",
            (session_id,)).fetchall()]
        deliveries = [dict(r) for r in self._r.execute(
            "SELECT id, target, kind, status, created_at FROM"
            " outbound_delivery WHERE session_id=? ORDER BY created_at",
            (session_id,)).fetchall()]
        tasks = [{"task_id": t["task_id"], "state": t["state"],
                  "outcome": t["outcome"], "url": f"/review/{t['task_id']}"}
                 for c in self._cases(session_id)
                 if (t := self.reviews.by_case(c["case_id"]))]
        return {
            "session_id": session_id,
            "repo": d["repo"], "pr_number": d["pr_number"],
            "head_sha": d["head_sha"], "pr_author": d["pr_author"],
            "filed_by": d["filed_by"],
            "extractor_version": d["extractor_version"],
            "factor_map_hash": d["factor_map_hash"],
            "factors": json.loads(d["factors"]),
            "provisions": json.loads(d["provisions"]),
            "not_reached": json.loads(d["not_reached"]),
            "case_scope": json.loads(d["case_scope"]),
            "escalation_policy": d["escalation_policy"],
            "disposition": d["disposition"],
            "lane": d["lane"],
            "reason": d["reason"],
            "cases": json.loads(d["detail"]) if d["detail"] else [],
            "lanes_open": outbound.lanes_for(d["disposition"] or "proceed",
                                             session_id, self.base_url),
            "review_tasks": tasks,
            "history": history,
            "deliveries": deliveries,
            "received_at": d["received_at"],
        }
