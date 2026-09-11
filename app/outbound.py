"""L5 Outbound: turning a resolution back into something a pull request can do.

The judiciary's answer to a PR is never just "blocked". It is a disposition
plus the *exits that remain open*, and the exits are the point — they are the
mechanical form of Corollary 2 (challenge coverage is social: a path that is
never offered is never taken).

Three lanes leave this module, and exactly three:

  request       the PR continues down the normal path (merge is not held)
  challenge     the decision is contested; the case climbs a tier
  human review  the automated tiers are exhausted; a RiskOwner must sign

Every delivery is written to `outbound_delivery` BEFORE any network attempt.
That ordering is deliberate: the audit record of what the judiciary decided
to say must not depend on whether GitHub was reachable, and it lets the whole
benchmark run offline in `recorded` status against the identical code path.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
import uuid

from . import db, github_app
from .db import now_iso
from .kernel import canonical

CHECK_NAME = os.environ.get("DJ_CHECK_NAME", "digital-judiciary")
GITHUB_API = os.environ.get("DJ_GITHUB_API", "https://api.github.com")

# Severity ordering for aggregating several provisions on one PR.
SEVERITY = {
    "proceed": 0,
    "proceed_with_conditions": 1,
    "blocked_challengeable": 2,
    "human_review": 3,
    "routed_amendment": 4,
    "blocked_final": 5,
    "blocked_absolute": 6,
}

# disposition -> (check conclusion, headline)
CONCLUSION = {
    "proceed": ("success", "Permitted"),
    "proceed_with_conditions": ("success", "Permitted with conditions"),
    "blocked_challengeable": ("failure", "Blocked — you can contest this"),
    "human_review": ("action_required", "Waiting on a risk owner"),
    "blocked_final": ("failure", "Blocked — the risk owner upheld the denial"),
    "blocked_absolute": ("failure", "Blocked by an absolute provision"),
    "routed_amendment": ("action_required", "This changes the rulebook itself"),
    "ignored": ("neutral", "Nothing to adjudicate"),
    "error": ("neutral", "Adjudication did not complete"),
}


def worst(dispositions: list[str]) -> str:
    """Aggregate several per-provision dispositions into one PR verdict."""
    if not dispositions:
        return "proceed"
    return max(dispositions, key=lambda d: SEVERITY.get(d, 0))


def outcome_to_disposition(outcome: str, absolute: bool, final: bool) -> str:
    if absolute:
        return "blocked_absolute"
    if outcome in ("permit", "not_adjudicated"):
        return "proceed"
    if outcome == "permit_conditional" or outcome == "accept_risk":
        return "proceed_with_conditions"
    if outcome == "deny":
        return "blocked_final" if final else "blocked_challengeable"
    return "proceed"


# ---------------------------------------------------------------------------
# Lanes
# ---------------------------------------------------------------------------
def lanes_for(disposition: str, session_id: str, base: str = "") -> list[dict]:
    """Which exits stay open. A6 is enforced here as an absence: an absolute
    denial offers no challenge lane and no human-review lane, because neither
    exists (CC-08). The only exit is the amendment channel."""
    challenge = {"lane": "challenge", "label": "Challenge",
                 "identifier": "dj_challenge",
                 "description": "Contest this at the next tier",
                 "url": f"{base}/v1/pr/{session_id}/challenge"}
    review = {"lane": "human_review", "label": "Ask for review",
              "identifier": "dj_review",
              "description": "Send to a human risk owner",
              "url": f"{base}/v1/pr/{session_id}/human-review"}
    amend = {"lane": "amendment", "label": "Propose change",
             "identifier": "dj_amend",
             "description": "File a rulebook amendment",
             "url": f"{base}/v1/amendments"}
    merge = {"lane": "request", "label": "Continue",
             "identifier": "dj_continue",
             "description": "Proceed down the normal path",
             "url": f"{base}/v1/pr/{session_id}"}

    if disposition == "blocked_absolute":
        return [amend]
    if disposition == "blocked_challengeable":
        return [challenge, review, amend]
    if disposition == "human_review":
        return [review]
    if disposition == "blocked_final":
        return [amend]
    if disposition == "routed_amendment":
        return [amend]
    return [merge]


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _fmt_facts(factors: list[str], provenance: dict) -> str:
    if not factors:
        return "_none extracted_"
    out = []
    for f in factors:
        mark = "" if provenance.get(f) == "observed" else " _(claimed by author)_"
        out.append(f"`{f}`{mark}")
    return ", ".join(out)


def summary_markdown(session: dict, cases: list[dict],
                     disposition: str) -> str:
    """The explanation that lands on the PR. Every line of this is a
    projection of stored fields (Definition 11 / rebuild) — the outbound
    layer recomputes nothing."""
    _, headline = CONCLUSION.get(disposition, ("neutral", disposition))
    lines = [f"### {headline}", ""]
    lines.append(f"Facts read from this pull request: "
                 f"{_fmt_facts(session['factors'], session.get('provenance', {}))}")
    lines.append("")
    lines.append(f"Extractor `{session['extractor_version']}` · "
                 f"rulebook `{session.get('rulebook_version', 'current')}`")
    lines.append("")

    if not cases:
        lines.append("No provision in the constitution is engaged by these "
                     "facts, so there is nothing to adjudicate.")
        return "\n".join(lines)

    lines.append("| Provision | Tier | Decision | Controlling precedent |")
    lines.append("|---|---|---|---|")
    for c in cases:
        ctrl = c.get("controlling") or f"_{c.get('controlling_state', '—')}_"
        lines.append(f"| `{c['provision_id']}` | {c.get('tier', 1)} | "
                     f"**{c.get('outcome', '?')}** | {ctrl} |")
    lines.append("")

    for c in cases:
        lines.append(f"**{c['provision_id']}** — {c.get('rationale', '')}")
        if c.get("conditions"):
            lines.append(f"  · Conditions: `{json.dumps(c['conditions'])}`")
        if c.get("consulted"):
            lines.append(f"  · Consulted {len(c['consulted'])} prior "
                         f"record(s); ordering keys: authority, recency, scope")
        if c.get("degradations"):
            lines.append("  · ⚠ A judgment degraded; the escalation path is "
                         "the remedy, not a guess")
        lines.append("")

    if session.get("not_reached"):
        lines.append(f"_Not reached (a floor decided first): "
                     f"{', '.join(session['not_reached'])}_")
    if disposition == "blocked_absolute":
        lines.append("This provision is **absolute**. There is no tier above "
                     "it and no risk acceptance below it. The only route is a "
                     "proposed amendment to the rulebook.")
    elif disposition == "blocked_challengeable":
        lines.append("If you think this reads the facts wrongly, challenge it. "
                     "A challenge is a first-class act: it is recorded, it "
                     "climbs a tier, and if the tiers run out a named human "
                     "decides.")
    return "\n".join(lines)


def check_run_payload(session: dict, cases: list[dict], disposition: str,
                      base_url: str = "") -> dict:
    conclusion, headline = CONCLUSION.get(disposition, ("neutral", disposition))
    actions = []
    for lane in lanes_for(disposition, session["session_id"], base_url):
        if lane["lane"] == "request":
            continue                      # nothing to click; the PR just goes
        actions.append({
            "label": lane["label"][:20],
            "description": lane["description"][:40],
            "identifier": lane["identifier"][:20],
        })
    payload = {
        "name": CHECK_NAME,
        "head_sha": session["head_sha"],
        "status": "completed",
        "conclusion": conclusion,
        "output": {
            "title": headline,
            "summary": summary_markdown(session, cases, disposition),
        },
        "details_url": f"{base_url}/v1/pr/{session['session_id']}",
    }
    if actions:
        payload["actions"] = actions[:3]      # GitHub caps actions at 3
    return payload


# ---------------------------------------------------------------------------
# Sinks
# ---------------------------------------------------------------------------
class DeliveryLog:
    """Sole writer to outbound_delivery."""

    def __init__(self, path: str | None = None):
        self._w = db.open_writer(path)

    def record(self, session_id: str, target: str, kind: str,
               payload: dict) -> str:
        did = str(uuid.uuid4())
        self._w.execute(
            "INSERT INTO outbound_delivery (id, session_id, target, kind,"
            " payload, status, attempts, created_at, updated_at)"
            " VALUES (?,?,?,?,?,'recorded',0,?,?)",
            (did, session_id, target, kind, canonical(payload),
             now_iso(), now_iso()))
        self._w.commit()
        return did

    def mark(self, delivery_id: str, status: str, transport: str | None,
             response: str | None) -> None:
        self._w.execute(
            "UPDATE outbound_delivery SET status=?, transport=?,"
            " attempts=attempts+1, response=?, updated_at=? WHERE id=?",
            (status, transport, (response or "")[:2000], now_iso(),
             delivery_id))
        self._w.commit()


class OutboundSink:
    """Record, then (optionally) transport. Subclasses override _transport."""

    target = "ui"

    def __init__(self, log: DeliveryLog):
        self.log = log

    def deliver(self, session_id: str, kind: str, payload: dict) -> dict:
        did = self.log.record(session_id, self.target, kind, payload)
        try:
            transport, response = self._transport(payload)
        except Exception as e:                       # noqa: BLE001
            self.log.mark(did, "failed", None, str(e))
            return {"delivery_id": did, "status": "failed", "error": str(e)}
        if transport is None:
            self.log.mark(did, "skipped", None, "no transport configured")
            return {"delivery_id": did, "status": "skipped"}
        self.log.mark(did, "sent", transport, response)
        return {"delivery_id": did, "status": "sent"}

    def _transport(self, payload: dict):
        return None, None                # record-only by default


class GitHubChecksSink(OutboundSink):
    """Posts a Check Run. Configured by DJ_GITHUB_TOKEN; without it the sink
    records the exact body it would have sent and reports 'skipped', which is
    the mode every offline test and every benchmark run uses."""

    target = "github_checks"

    def __init__(self, log: DeliveryLog, repo_of):
        super().__init__(log)
        self.timeout = float(os.environ.get("DJ_GITHUB_TIMEOUT_S", "15"))
        self._repo_of = repo_of          # session_id -> "owner/repo"

    def deliver(self, session_id: str, kind: str, payload: dict) -> dict:
        self._repo = self._repo_of(session_id)
        return super().deliver(session_id, kind, payload)

    def _transport(self, payload: dict):
        token = github_app.resolve_token()
        if not token or not getattr(self, "_repo", None):
            return None, None
        url = f"{GITHUB_API}/repos/{self._repo}/check-runs"
        req = urllib.request.Request(
            url, data=json.dumps(payload).encode(), method="POST",
            headers={"authorization": f"Bearer {token}",
                     "accept": "application/vnd.github+json",
                     "x-github-api-version": "2022-11-28",
                     "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return url, f"{r.status}"
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"github {e.code}: {e.read()[:200]!r}") from e


class GitHubCommentSink(OutboundSink):
    """The long-form explanation as a PR comment. Same posture as above."""

    target = "github_comment"

    def __init__(self, log: DeliveryLog, repo_of, number_of):
        super().__init__(log)
        # token resolved at transport time via github_app.resolve_token()
        self.timeout = float(os.environ.get("DJ_GITHUB_TIMEOUT_S", "15"))
        self._repo_of, self._number_of = repo_of, number_of

    def deliver(self, session_id: str, kind: str, payload: dict) -> dict:
        self._repo = self._repo_of(session_id)
        self._number = self._number_of(session_id)
        return super().deliver(session_id, kind, payload)

    def _transport(self, payload: dict):
        if not github_app.resolve_token() or not getattr(self, "_repo", None):
            return None, None
        url = (f"{GITHUB_API}/repos/{self._repo}/issues/"
               f"{self._number}/comments")
        req = urllib.request.Request(
            url, data=json.dumps({"body": payload["body"]}).encode(),
            method="POST",
            headers={"authorization": f"Bearer {github_app.resolve_token()}",
                     "accept": "application/vnd.github+json",
                     "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return url, f"{r.status}"
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"github {e.code}: {e.read()[:200]!r}") from e



def retry_failed(path: str | None = None, limit: int = 20,
                 max_attempts: int = 5) -> dict:
    """Re-attempt outbound deliveries stuck in ``failed``.

    Only rows with attempts < max_attempts are claimed. Skipped (no token)
    rows are left alone. Returns counts for ops/metrics.
    """
    import json as _json
    log = DeliveryLog(path)
    reader = db.open_reader(path)
    rows = reader.execute(
        "SELECT * FROM outbound_delivery WHERE status='failed'"
        " AND attempts < ? ORDER BY updated_at LIMIT ?",
        (max_attempts, limit)).fetchall()
    reader.close()
    if not rows:
        return {"retried": 0, "sent": 0, "failed": 0, "skipped": 0}

    # Rebuild sinks the same way as the live path
    _, checks, comment = build_outbound(path)
    sinks = {"github_checks": checks, "github_comment": comment}
    sent = failed = skipped = 0
    for row in rows:
        target = row["target"]
        sink = sinks.get(target)
        if sink is None:
            skipped += 1
            continue
        try:
            payload = _json.loads(row["payload"])
        except Exception:
            log.mark(row["id"], "failed", None, "retry: bad payload json")
            failed += 1
            continue
        # Re-drive transport only; do not insert a second audit row.
        sink._repo = None
        if hasattr(sink, "_repo_of"):
            try:
                sink._repo = sink._repo_of(row["session_id"])
            except Exception:
                sink._repo = None
        if hasattr(sink, "_number_of"):
            try:
                sink._number = sink._number_of(row["session_id"])
            except Exception:
                pass
        try:
            transport, response = sink._transport(payload)
        except Exception as e:  # noqa: BLE001
            log.mark(row["id"], "failed", None, f"retry: {e}")
            failed += 1
            continue
        if transport is None:
            log.mark(row["id"], "skipped", None, "retry: no transport")
            skipped += 1
        else:
            log.mark(row["id"], "sent", transport, response)
            sent += 1
    return {"retried": len(rows), "sent": sent, "failed": failed,
            "skipped": skipped}


def build_outbound(path: str | None = None):
    """Assemble the outbound stack. Returns (log, checks, comment)."""
    log = DeliveryLog(path)
    reader = db.open_reader(path)

    def repo_of(session_id: str):
        r = reader.execute("SELECT repo FROM pr_session WHERE session_id=?",
                           (session_id,)).fetchone()
        return r["repo"] if r else None

    def number_of(session_id: str):
        r = reader.execute(
            "SELECT pr_number FROM pr_session WHERE session_id=?",
            (session_id,)).fetchone()
        return r["pr_number"] if r else None

    return log, GitHubChecksSink(log, repo_of), \
        GitHubCommentSink(log, repo_of, number_of)
