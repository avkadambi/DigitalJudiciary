"""Enterprise controls that stay inside a single container.

- Repo → organization mapping (trusted config, never from the webhook body)
- Simple token-bucket rate limit on inbound webhooks
- Break-glass merge override with full audit trail (named principal, reason)
- Post-merge continuous-compliance scan (secondary control; pre-merge remains primary)

No external dependencies. All state lives in the same SQLite file as the ledger.
"""
from __future__ import annotations

import os
import threading
import time
import uuid

from . import db, metrics
from .db import now_iso
from .kernel import KernelError, canonical

SCHEMA_ENTERPRISE = """
CREATE TABLE IF NOT EXISTS break_glass_event (
  event_id      TEXT PRIMARY KEY,
  session_id    TEXT,
  repo          TEXT,
  pr_number     INTEGER,
  principal_id  TEXT NOT NULL,
  reason        TEXT NOT NULL,
  expires_at    TEXT,
  created_at    TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS compliance_scan (
  scan_id       TEXT PRIMARY KEY,
  repo          TEXT NOT NULL,
  sha           TEXT NOT NULL,
  organization  TEXT,
  factors       TEXT NOT NULL,
  provisions    TEXT NOT NULL,
  disposition   TEXT,
  detail        TEXT,
  created_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS cs_repo_sha ON compliance_scan (repo, sha);
"""


def ensure_schema(path: str | None = None) -> None:
    w = db.open_writer(path)
    try:
        w.executescript(SCHEMA_ENTERPRISE)
        w.commit()
    finally:
        w.close()


# ---------------------------------------------------------------------------
# Repo → tenant mapping (trusted deployment config)
# ---------------------------------------------------------------------------
def repo_organization(repo_full_name: str) -> str | None:
    """Map 'owner/repo' to a tenant org_id via the platform tenancy registry.

    Resolution order (trusted config only — never the raw webhook body):
      1. tenant_repo table (GitHub App installation registry)
      2. DJ_REPO_ORG_MAP JSON
      3. DJ_DEFAULT_ORG
    """
    from .platform import tenancy
    return tenancy.resolve_org_for_repo(repo_full_name)


# ---------------------------------------------------------------------------
# Rate limit (process-local token bucket)
# ---------------------------------------------------------------------------
class RateLimiter:
    def __init__(self, rate_per_s: float, burst: int):
        self.rate = max(0.1, rate_per_s)
        self.burst = max(1, burst)
        self.tokens = float(burst)
        self.updated = time.monotonic()
        self._lock = threading.Lock()

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()
            self.tokens = min(
                self.burst,
                self.tokens + (now - self.updated) * self.rate)
            self.updated = now
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            metrics.inc("inbound_rate_limited")
            return False


def inbound_limiter() -> RateLimiter:
    rate = float(os.environ.get("DJ_INBOUND_RATE_PER_S", "20"))
    burst = int(os.environ.get("DJ_INBOUND_BURST", "40"))
    if not hasattr(inbound_limiter, "_inst"):
        inbound_limiter._inst = RateLimiter(rate, burst)  # type: ignore[attr-defined]
    return inbound_limiter._inst  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------
# Break-glass: audited override that does NOT invent tier-1 precedent
# ---------------------------------------------------------------------------
def break_glass(svc, principal: str, reason: str,
                session_id: str | None = None,
                repo: str | None = None,
                pr_number: int | None = None,
                expiry_hours: int = 24,
                path: str | None = None) -> dict:
    """Record a named emergency override.

    This does not admit a permit into the precedent store (Def. 7). It writes
    an audit event and, if a session is supplied, emits an outbound check
    conclusion of success so a required status check can pass. The Gate is
    never asked to store a depth-1 holding.
    """
    if not (reason or "").strip():
        raise KernelError("break-glass requires a non-empty reason", 422)
    # Only risk owners or lawmakers may break glass.
    branch = svc.registry.resolve_branch(principal)
    if branch not in ("risk_owner", "lawmakers"):
        raise KernelError(
            f"break-glass requires risk_owner or lawmakers; held '{branch}'",
            403)
    ensure_schema(path)
    from datetime import datetime, timedelta, timezone
    exp = (datetime.now(timezone.utc) + timedelta(hours=max(1, expiry_hours)))
    event_id = f"BG-{uuid.uuid4().hex[:10]}"
    w = db.open_writer(path)
    try:
        w.execute(
            "INSERT INTO break_glass_event (event_id, session_id, repo,"
            " pr_number, principal_id, reason, expires_at, created_at)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (event_id, session_id, repo, pr_number, principal,
             reason.strip()[:2000],
             exp.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"), now_iso()))
        w.commit()
    finally:
        w.close()
    metrics.inc("break_glass_events")

    # If there is an open PR session, mark a disposition note and refresh the
    # check run to success so branch protection can proceed. No precedent.
    if session_id:
        try:
            gw = svc.gateway
            gw._w.execute(
                "INSERT INTO pr_disposition (session_id, disposition, lane,"
                " reason, detail, actor, occurred_at) VALUES (?,?,?,?,?,?,?)",
                (session_id, "proceed_with_conditions", "break_glass",
                 f"break-glass by {principal}: {reason.strip()[:200]}",
                 canonical({"event_id": event_id, "expires_at":
                            exp.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")}),
                 principal, now_iso()))
            gw._w.commit()
            # Re-emit outbound under the new disposition
            view = gw.session_view(session_id)
            from . import outbound
            detail = view.get("cases") or []
            check = outbound.check_run_payload(
                {**view, "factors": view.get("factors") or []},
                detail, "proceed_with_conditions", gw.base_url)
            # Force success conclusion for the emergency path
            check["conclusion"] = "success"
            check["output"] = {
                "title": "Break-glass override",
                "summary": (f"Emergency override by **{principal}**.\n\n"
                            f"Reason: {reason.strip()}\n\n"
                            f"Event: `{event_id}` — expires "
                            f"{exp.isoformat()}. No precedent was written."),
            }
            gw.checks.deliver(session_id, "check_run", check)
        except Exception:  # noqa: BLE001
            pass

    return {
        "event_id": event_id,
        "principal_id": principal,
        "expires_at": exp.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00"),
        "session_id": session_id,
        "precedent_written": False,
    }


# ---------------------------------------------------------------------------
# Post-merge continuous compliance (secondary control)
# ---------------------------------------------------------------------------
def enqueue_post_merge(repo: str, sha: str, factors: list[str],
                       provisions: list[str], organization: str | None,
                       path: str | None = None) -> str:
    from . import jobs
    return jobs.enqueue("post_merge_scan", {
        "repo": repo, "sha": sha, "factors": factors,
        "provisions": provisions, "organization": organization,
    }, path=path)


def run_post_merge_scan(svc, payload: dict) -> dict:
    """Adjudicate factors against the live constitution without a PR session.

    Results are recorded in compliance_scan for audit. Absolute denials and
    challengeable blocks surface as findings; they do not rewrite history on
    main — operators open follow-up work from the finding.
    """
    ensure_schema()
    repo = payload["repo"]
    sha = payload["sha"]
    factors = list(payload.get("factors") or [])
    provisions = list(payload.get("provisions") or [])
    org = payload.get("organization")
    author = os.environ.get("DJ_GITHUB_PRINCIPAL", "svc:github")
    findings = []
    worst = "proceed"
    for pid in provisions:
        if pid == "constitution":
            continue
        try:
            res = svc.adjudicator.submit_case(
                pid, factors, author,
                {"organization": org} if org else {})
        except Exception as e:  # noqa: BLE001
            findings.append({"provision_id": pid, "error": str(e)})
            continue
        findings.append({
            "provision_id": pid,
            "decision": res.get("decision"),
            "controlling_state": res.get("controlling_state"),
            "case_id": res.get("case_id"),
        })
        if res.get("decision") == "deny":
            worst = "blocked"
    scan_id = f"CS-{uuid.uuid4().hex[:10]}"
    w = db.open_writer()
    try:
        w.execute(
            "INSERT INTO compliance_scan (scan_id, repo, sha, organization,"
            " factors, provisions, disposition, detail, created_at)"
            " VALUES (?,?,?,?,?,?,?,?,?)",
            (scan_id, repo, sha, org, canonical(factors),
             canonical(provisions), worst, canonical(findings), now_iso()))
        w.commit()
    finally:
        w.close()
    metrics.inc("post_merge_scans")
    return {"scan_id": scan_id, "disposition": worst, "findings": findings}


def recent_scans(limit: int = 50, path: str | None = None) -> list[dict]:
    ensure_schema(path)
    r = db.open_reader(path)
    try:
        rows = r.execute(
            "SELECT scan_id, repo, sha, organization, disposition, created_at"
            " FROM compliance_scan ORDER BY created_at DESC LIMIT ?",
            (limit,)).fetchall()
        return [dict(x) for x in rows]
    finally:
        r.close()


def recent_break_glass(limit: int = 50, path: str | None = None) -> list[dict]:
    ensure_schema(path)
    r = db.open_reader(path)
    try:
        rows = r.execute(
            "SELECT * FROM break_glass_event ORDER BY created_at DESC LIMIT ?",
            (limit,)).fetchall()
        return [dict(x) for x in rows]
    finally:
        r.close()
