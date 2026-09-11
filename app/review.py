"""L5 Human review: the lane that ends at a named person.

When the automated tiers are exhausted, A4 says a human RiskOwner decides,
and A5 says their reasoning is recorded under their own name. This module
owns the *task* — the thing that sits in someone's queue — and nothing else.
It does not decide, and it cannot: the decision goes through
`Adjudicator.risk_decision`, which re-checks the branch in the Kernel. A
compromised review UI can misrepresent a case; it cannot manufacture
authority.

Sinks are pluggable because the destination is an organizational fact, not an
architectural one. Today the built-in screen is the system of record. Jira and
ServiceNow are written as real payload builders that record what they would
send and go live the moment their base URL and token are configured — so
adopting them is a deployment change, not a code change. That is the same
substitution rule the container applies everywhere else: change the mechanism,
never the guarantee.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
import uuid

from . import db
from .db import now_iso
from .kernel import canonical


class ReviewSink:
    name = "ui"

    def open_task(self, task: dict) -> str | None:
        """Return an external reference, or None if this sink has none."""
        return None

    def close_task(self, task: dict, outcome: str) -> None:
        return None


class UIReviewSink(ReviewSink):
    """The built-in screen. No external reference: the task *is* the row."""
    name = "ui"


class _HTTPSink(ReviewSink):
    base_env = ""
    token_env = ""

    def __init__(self, log):
        self.log = log
        self.base = os.environ.get(self.base_env, "").rstrip("/")
        self.token = os.environ.get(self.token_env, "")
        self.timeout = float(os.environ.get("DJ_ITSM_TIMEOUT_S", "15"))

    def configured(self) -> bool:
        return bool(self.base and self.token)

    def _post(self, path: str, body: dict) -> str:
        req = urllib.request.Request(
            self.base + path, data=json.dumps(body).encode(), method="POST",
            headers={"authorization": f"Bearer {self.token}",
                     "content-type": "application/json",
                     "accept": "application/json"})
        with urllib.request.urlopen(req, timeout=self.timeout) as r:
            return json.loads(r.read() or b"{}").get("key") or \
                json.loads("{}").get("x") or f"http-{r.status}"


class JiraReviewSink(_HTTPSink):
    """Creates an issue in the risk project. Payload is built whether or not
    transport is configured, so the mapping is reviewable before go-live."""

    name = "jira"
    base_env = "DJ_JIRA_BASE_URL"
    token_env = "DJ_JIRA_TOKEN"

    def payload(self, task: dict) -> dict:
        s = task["summary"]
        return {
            "fields": {
                "project": {"key": os.environ.get("DJ_JIRA_PROJECT", "RISK")},
                "issuetype": {"name": os.environ.get(
                    "DJ_JIRA_ISSUETYPE", "Risk Acceptance")},
                "summary": task["title"][:250],
                "description": _plain_dossier(s),
                "labels": ["digital-judiciary", f"provision-{task['provision_id']}"],
                "duedate": None,
            },
            "dj": {"task_id": task["task_id"], "case_id": task["case_id"],
                   "session_id": task["session_id"],
                   "decide_url": s.get("decide_url")},
        }

    def open_task(self, task: dict) -> str | None:
        body = self.payload(task)
        did = self.log.record(task["session_id"], "jira", "create_issue", body)
        if not self.configured():
            self.log.mark(did, "skipped", None, "DJ_JIRA_BASE_URL unset")
            return None
        try:
            ref = self._post("/rest/api/3/issue", body)
            self.log.mark(did, "sent", self.base, ref)
            return ref
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            self.log.mark(did, "failed", self.base, str(e))
            return None


class ServiceNowReviewSink(_HTTPSink):
    """Creates a risk-acceptance record. Same posture as Jira."""

    name = "servicenow"
    base_env = "DJ_SNOW_BASE_URL"
    token_env = "DJ_SNOW_TOKEN"

    def payload(self, task: dict) -> dict:
        s = task["summary"]
        return {
            "short_description": task["title"][:160],
            "description": _plain_dossier(s),
            "category": "governance",
            "u_provision": task["provision_id"],
            "u_case_id": task["case_id"],
            "u_dj_session": task["session_id"],
            "u_decide_url": s.get("decide_url"),
            "assignment_group": os.environ.get("DJ_SNOW_GROUP", "Risk Owners"),
        }

    def open_task(self, task: dict) -> str | None:
        table = os.environ.get("DJ_SNOW_TABLE", "sn_risk_acceptance")
        body = self.payload(task)
        did = self.log.record(task["session_id"], "servicenow",
                              f"create_{table}", body)
        if not self.configured():
            self.log.mark(did, "skipped", None, "DJ_SNOW_BASE_URL unset")
            return None
        try:
            ref = self._post(f"/api/now/table/{table}", body)
            self.log.mark(did, "sent", self.base, ref)
            return ref
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            self.log.mark(did, "failed", self.base, str(e))
            return None


def _plain_dossier(summary: dict) -> str:
    lines = [
        f"Pull request: {summary.get('pr_url', 'n/a')}",
        f"Provision: {summary.get('provision_id')} — {summary.get('provision_text', '')}",
        f"Facts: {', '.join(summary.get('facts', []))}",
        "",
        f"Tier {summary.get('contested_tier')} denial, contested at every "
        f"automated tier. The automated ladder is exhausted.",
        "",
        "Rationale of the last automated tier:",
        summary.get("rationale", ""),
        "",
    ]
    guard = summary.get("renewal_guard") or {}
    if guard.get("state") == "barred":
        lines.append("BARRED: the Lawmakers rejected the referral of a "
                     "materially similar lapsed acceptance. Accepting this "
                     "risk is not available (Proposition 2).")
    elif guard.get("state") == "must_cite":
        lines.append(f"RENEWAL: this would renew lapsed acceptance "
                     f"{guard.get('predecessor')}, whose referral is still "
                     f"pending.")
    lines.append("")
    lines.append("Decide in the Digital Judiciary review screen: "
                 + str(summary.get("decide_url")))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
class ReviewQueue:
    """Sole writer to review_task; fans out to the configured sinks."""

    def __init__(self, delivery_log, path: str | None = None):
        self._w = db.open_writer(path)
        self._r = db.open_reader(path)
        self.log = delivery_log
        self.sinks: list[ReviewSink] = [UIReviewSink()]
        for name in os.environ.get("DJ_REVIEW_SINK", "ui").split(","):
            name = name.strip().lower()
            if name == "jira":
                self.sinks.append(JiraReviewSink(delivery_log))
            elif name == "servicenow":
                self.sinks.append(ServiceNowReviewSink(delivery_log))

    def open(self, session_id: str, case_id: str, provision_id: str,
             title: str, summary: dict, org: str | None = None) -> dict:
        existing = self._w.execute(
            "SELECT * FROM review_task WHERE case_id=? AND state='open'",
            (case_id,)).fetchone()
        if existing:
            return dict(existing)          # idempotent: one open task per case

        task_id = f"RT-{uuid.uuid4().hex[:8]}"
        summary = {**summary,
                   "decide_url": f"/review/{task_id}"}
        task = {"task_id": task_id, "session_id": session_id,
                "case_id": case_id, "provision_id": provision_id,
                "title": title, "summary": summary}
        refs = {}
        for sink in self.sinks:
            ref = sink.open_task(task)
            if ref:
                refs[sink.name] = ref
        self._w.execute(
            "INSERT INTO review_task (task_id, session_id, case_id,"
            " provision_id, title, summary, sinks, external_refs, state,"
            " opened_at, organization)"
            " VALUES (?,?,?,?,?,?,?,?,'open',?,?)",
            (task_id, session_id, case_id, provision_id, title,
             canonical(summary), canonical([s.name for s in self.sinks]),
             canonical(refs), now_iso(), org))
        self._w.commit()
        return self.get(task_id)

    def close(self, task_id: str, outcome: str, decided_by: str,
              record_id: str | None) -> None:
        task = self.get(task_id)
        self._w.execute(
            "UPDATE review_task SET state='decided', outcome=?,"
            " decided_by=?, record_id=?, closed_at=? WHERE task_id=?",
            (outcome, decided_by, record_id, now_iso(), task_id))
        self._w.commit()
        for sink in self.sinks:
            try:
                sink.close_task(task, outcome)
            except Exception:              # noqa: BLE001
                pass                       # the DJ record is the source of truth

    def get(self, task_id: str) -> dict | None:
        r = self._r.execute("SELECT * FROM review_task WHERE task_id=?",
                            (task_id,)).fetchone()
        if not r:
            return None
        d = dict(r)
        d["summary"] = json.loads(d["summary"])
        d["sinks"] = json.loads(d["sinks"])
        d["external_refs"] = json.loads(d["external_refs"])
        return d

    def list(self, state: str = "open",
             org: str | None = None) -> list[dict]:
        # The tenant filter is part of the query. A queue that fetches every
        # tenant's work and hides the rest in the template is one template bug
        # away from showing a risk owner another company's docket.
        sql = "SELECT task_id FROM review_task WHERE state=?"
        args = [state]
        if org:
            sql += " AND organization=?"
            args.append(org)
        rows = self._r.execute(
            sql + " ORDER BY opened_at DESC LIMIT 200", args).fetchall()
        return [self.get(r["task_id"]) for r in rows]

    def by_case(self, case_id: str) -> dict | None:
        r = self._r.execute(
            "SELECT task_id FROM review_task WHERE case_id=?"
            " ORDER BY opened_at DESC LIMIT 1", (case_id,)).fetchone()
        return self.get(r["task_id"]) if r else None
