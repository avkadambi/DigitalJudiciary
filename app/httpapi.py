"""L4/API surface (SDD v3.0 §10.2), on the Python stdlib http.server.

Deliberate choice: zero third-party packages means zero pip installs in the
image, a ~50 MB container, and no supply-chain surface beyond CPython. The
routing below is 100 lines; a framework buys nothing at this API size.
Auth: Bearer <api_key> -> principal, branch re-resolved at the point of
action inside the Kernel (never at connection time)."""
from __future__ import annotations

import json
import os
import sys
import re
import secrets
import urllib.parse
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import reviewui
from .inbound_github import InboundError
from .kernel import KernelError

# The browser session for the review screen. The cookie carries the
# principal's API key and nothing else — there is no server-side session
# table and no separate login identity, so the screen cannot outlive or
# out-rank the credential it was opened with. Authority is still resolved
# in the Kernel at the moment of decision, never here.
SESSION_COOKIE = "dj_review"
MAX_BODY = int(__import__('os').environ.get('DJ_MAX_BODY_BYTES', str(2 * 1024 * 1024)))


class Services:
    """Dependency container assembled in serve.py / conformance runner."""

    def __init__(self, registry, constitution, ledger, gate, provenance,
                 chain, adjudicator, lifecycle, gateway=None):
        self.registry = registry
        self.constitution = constitution
        self.ledger = ledger
        self.gate = gate
        self.provenance = provenance
        self.chain = chain
        self.adjudicator = adjudicator
        self.lifecycle = lifecycle
        # L5. Attached after construction because the gateway holds a
        # reference to the container it lives in — it calls the Kernel for
        # every adjudicative act and is never given a shortcut around it.
        self.gateway = gateway
        # The consolidation pipeline (Definition 16). Attached after
        # construction for the same reason the gateway is, and separate from
        # every adjudicative object on purpose: forming a class is a power
        # over admission, and A1-A4 confer it on no authority.
        self.classifier = None


def make_handler(svc: Services):

    def _ent_status() -> dict:
        from . import github_app, jobs, enterprise
        from .platform.dj_config import public_view
        try:
            jobs.ensure_schema()
            enterprise.ensure_schema()
            pending = jobs.pending_count()
        except Exception:
            pending = None
        return {
            "github": github_app.configured(),
            "jobs_pending": pending,
            "queue_backend": __import__("app.jobs", fromlist=["backend_name"]).backend_name(),
            "default_org": os.environ.get("DJ_DEFAULT_ORG"),
            "repo_map_configured": bool(os.environ.get("DJ_REPO_ORG_MAP")),
            "inbound_rate_per_s": float(os.environ.get(
                "DJ_INBOUND_RATE_PER_S", "20")),
            "profile": os.environ.get("DJ_PROFILE", "demo"),
            "storage": "sqlite",
            "worker_threads": int(os.environ.get("DJ_WORKER_THREADS", "1")),
            "config": public_view(),
        }

    class Handler(BaseHTTPRequestHandler):
        server_version = "DigitalJudiciary/3.0"

        # -- plumbing ---------------------------------------------------
        def _rid(self) -> str:
            return secrets.token_hex(8)

        def _send(self, status: int, obj, rid: str | None = None) -> None:
            rid = rid or self._rid()
            if isinstance(obj, dict) and "request_id" not in obj:
                obj = {**obj, "request_id": rid}
            body = json.dumps(obj, indent=2, default=str).encode()
            self.send_response(status)
            self.send_header("content-type", "application/json")
            self.send_header("content-length", str(len(body)))
            self.send_header("x-request-id", rid)
            self.send_header("x-content-type-options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def _body(self) -> dict:
            n = int(self.headers.get("content-length") or 0)
            if n > MAX_BODY:
                raise ValueError(f"body exceeds {MAX_BODY} bytes")
            return json.loads(self.rfile.read(n) or b"{}")

        def _principal(self) -> str | None:
            auth = self.headers.get("authorization", "")
            if not auth.startswith("Bearer "):
                return None
            return svc.registry.authenticate(auth.removeprefix("Bearer "))

        def log_message(self, *a):  # quiet by default
            pass

        # -- L5 plumbing: HTML, forms, cookies --------------------------
        def _html(self, status: int, markup: str) -> None:
            body = markup.encode()
            self.send_response(status)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.send_header("content-length", str(len(body)))
            self.send_header("x-content-type-options", "nosniff")
            self.send_header("referrer-policy", "same-origin")
            self.send_header("x-frame-options", "DENY")
            self.send_header("cache-control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _redirect(self, location: str, cookie: str | None = None) -> None:
            self.send_response(303)
            self.send_header("location", location)
            if cookie:
                self.send_header("set-cookie", cookie)
            self.send_header("content-length", "0")
            self.end_headers()

        def _form(self) -> dict:
            n = int(self.headers.get("content-length") or 0)
            raw = self.rfile.read(n).decode("utf-8", "replace")
            return {k: v[0] for k, v in
                    urllib.parse.parse_qs(raw, keep_blank_values=True).items()}

        def _raw_body(self) -> bytes:
            n = int(self.headers.get("content-length") or 0)
            if n > MAX_BODY:
                raise ValueError(f"body exceeds {MAX_BODY} bytes")
            return self.rfile.read(n)

        def _session_key(self) -> str:
            jar = SimpleCookie(self.headers.get("cookie", ""))
            m = jar.get(SESSION_COOKIE)
            return m.value if m else ""

        # -- data behind the desks ---------------------------------------
        def _scoped(self, sql: str, org, args=()) -> list[dict]:
            """Run a query with the viewer's tenant applied in SQL."""
            from . import db as dbmod
            # Same reading as above: a tenant sees its own rows plus the
            # platform-wide ones that govern it.
            where = " AND (organization = ? OR organization IS NULL)" \
                if org else ""
            rows = dbmod.open_reader().execute(
                sql.replace("{ORG}", where),
                tuple(args) + ((org,) if org else ())).fetchall()
            return [dict(r) for r in rows]

        def _change_view(self, session_id, org):
            """One change, tenant-checked. Cross-tenant reads are told the
            change does not exist rather than that it exists and is
            forbidden."""
            from . import db as dbmod
            row = dbmod.open_reader().execute(
                "SELECT organization FROM pr_session WHERE session_id=?",
                (session_id,)).fetchone()
            if not row or (org and row["organization"] != org):
                return None
            try:
                return svc.gateway.session_view(session_id)
            except InboundError:
                return None

        def _change_stream(self, org):
            rows = self._scoped(
                "SELECT session_id, repo, pr_number, provisions, received_at,"
                " disposition FROM pr_session_current"
                " WHERE 1=1{ORG} ORDER BY received_at DESC LIMIT 200", org)
            tally = self._scoped(
                "SELECT disposition, COUNT(*) AS n FROM pr_session_current"
                " WHERE 1=1{ORG} GROUP BY disposition", org)
            by = {t["disposition"] or "pending": t["n"] for t in tally}
            counts = {
                "Governed": sum(by.values()),
                "Cleared": by.get("proceed", 0)
                + by.get("proceed_with_conditions", 0),
                "Open to you": by.get("blocked_challengeable", 0),
                "With a human": by.get("human_review", 0),
                "At a floor": by.get("blocked_absolute", 0),
            }
            return rows, counts

        def _legislature(self, org):
            from . import db as dbmod
            r = dbmod.open_reader()
            # Scoped in the query. A lawmaker of one company has no business
            # reading, still less being offered a control over, another
            # company's constitution — and the Kernel refusing the write is
            # not a reason to draw the button.
            where, args = "", ()
            if org:
                where, args = " AND organization = ?", (org,)
            pend = [dict(x) for x in r.execute(
                "SELECT * FROM draft_amendment WHERE status='pending'"
                + where + " ORDER BY created_at DESC LIMIT 50",
                args).fetchall()]
            done = [dict(x) for x in r.execute(
                "SELECT * FROM draft_amendment WHERE status<>'pending'"
                + where + " ORDER BY created_at DESC LIMIT 5",
                args).fetchall()]
            # Where the rulebook is under strain: clauses that keep having to
            # be waived or litigated are legislative problems wearing an
            # adjudicative costume.
            friction = self._scoped(
                "SELECT provision_id, COUNT(*) AS records,"
                " SUM(is_acceptance) AS waivers FROM precedent_record"
                " WHERE 1=1{ORG} GROUP BY provision_id"
                " ORDER BY waivers DESC, records DESC LIMIT 6", org)
            for a in pend:
                a["_brief"] = self._amendment_brief(a, org)
                a["_dossier"] = self._amendment_dossier(a, org)
            return pend, done, [f for f in friction if f["records"]]

        # -- the statement -----------------------------------------------
        ACTIVITY_SQL = """
        SELECT 'change' AS kind, s.received_at AS at, s.organization AS org,
               s.repo || '#' || s.pr_number AS what,
               'filed as ' || s.filed_by AS detail, s.pr_author AS actor,
               '/review/change/' || s.session_id AS url, '' AS tone
          FROM pr_session s
        UNION ALL
        SELECT 'decision', d.occurred_at, s2.organization, d.disposition,
               d.reason, d.actor, '/review/change/' || d.session_id,
               CASE WHEN d.disposition LIKE 'blocked%' THEN 'deny'
                    WHEN d.disposition = 'human_review' THEN 'wait'
                    WHEN d.disposition = 'routed_amendment' THEN 'law'
                    ELSE '' END
          FROM pr_disposition d JOIN pr_session s2
            ON s2.session_id = d.session_id
        UNION ALL
        SELECT 'review', COALESCE(t.closed_at, t.opened_at), t.organization,
               COALESCE(t.outcome, 'awaiting a risk owner'), t.title,
               COALESCE(t.decided_by, ''), '/review/' || t.task_id,
               CASE WHEN t.state = 'open' THEN 'wait' ELSE '' END
          FROM review_task t
        UNION ALL
        SELECT 'precedent', p.resolved_at, p.organization,
               p.provision_id || ' — ' ||
                 json_extract(p.interpretation, '$.outcome'),
               p.rationale_text, p.resolving_principal,
               '/review/ledger/' || p.id,
               CASE WHEN p.is_acceptance = 1 THEN 'wait' ELSE '' END
          FROM precedent_record p
        UNION ALL
        SELECT 'lifecycle', e.occurred_at, p2.organization, e.event_type,
               p2.provision_id, e.actor, '/review/ledger/' || e.record_id,
               CASE WHEN e.event_type = 'lapsed' THEN 'deny' ELSE '' END
          FROM precedent_lifecycle_event e
          JOIN precedent_record p2 ON p2.id = e.record_id
        UNION ALL
        SELECT 'amendment', a.created_at, a.organization,
               a.origin || COALESCE(' — ' || a.status, ''),
               COALESCE(json_extract(a.body, '$.note'),
                        json_extract(a.body, '$.question'), ''),
               a.proposed_by, '/review/amendments', 'law'
          FROM draft_amendment a
        """

        def _amendment_brief(self, a, org):
            """Clause-by-clause: what it says now, what it would say, and what
            adopting it does to the decisions already made under it."""
            import json as _json
            from . import db as dbmod
            from .kernel import _materially_changed
            from . import reviewui as ui

            body = _json.loads(a["body"] or "{}")
            changes = body.get("changes") or []
            if not changes:
                return {}
            r = dbmod.open_reader()
            version = svc.constitution.current_version()
            declared = body.get("supersedes_precedent")
            out = []
            for c in changes:
                pid = c.get("provision_id")
                try:
                    cur = svc.constitution.get_provision(version, pid, org=org)
                except Exception:                              # noqa: BLE001
                    cur = None
                after = {"provision_id": pid,
                         "text": c.get("text", (cur or {}).get("text", "")),
                         "policy": c.get("policy", (cur or {}).get("policy",
                                                                   {})),
                         "absolute": c.get("absolute",
                                           bool((cur or {}).get("absolute")))}
                material = _materially_changed(cur, after)
                if declared is True:
                    material = True
                elif declared is False:
                    material = False

                diff = []
                if cur is None:
                    headline, effect = "a new rule", "new"
                elif c.get("action") == "remove":
                    headline, effect = "would be removed", "supersedes"
                else:
                    if (cur.get("text") or "") != after["text"]:
                        diff.append(("wording", cur.get("text", "")[:180],
                                     after["text"][:180]))
                    was = (cur.get("policy") or {}).get("deny_if_any") or []
                    now = (after.get("policy") or {}).get("deny_if_any") or []
                    if sorted(was) != sorted(now):
                        diff.append(("triggers",
                                     ", ".join(x.replace("_", " ")
                                               for x in sorted(was)) or "none",
                                     ", ".join(x.replace("_", " ")
                                               for x in sorted(now)) or "none"))
                    if bool(cur.get("absolute")) != bool(after["absolute"]):
                        diff.append(("appealable",
                                     "no — a floor" if cur.get("absolute")
                                     else "yes",
                                     "no — a floor" if after["absolute"]
                                     else "yes"))
                    headline = ("changes what the rule reaches" if material
                                else "changes the wording only")
                    effect = "supersedes" if material else "wording"

                held = r.execute(
                    "SELECT COUNT(*) AS n FROM record_effective"
                    " WHERE provision_id=? AND superseded=0", (pid,)
                ).fetchone()["n"]
                if effect == "supersedes":
                    consequence = (
                        f"Adopting this retires the {held} decision(s) already"
                        f" recorded under {pid}: they interpreted wording that"
                        f" would no longer be in force, so they stop applying"
                        f" to new cases. They stay in the ledger."
                        if held else
                        f"No decisions have been recorded under {pid} yet, so"
                        f" nothing is retired.")
                elif effect == "new":
                    consequence = ("A rule that does not exist today. Nothing"
                                   " is retired; it starts applying to new"
                                   " changes immediately.")
                else:
                    consequence = (
                        f"The wording changes but what the rule reaches does"
                        f" not, so the {held} decision(s) recorded under {pid}"
                        f" still stand.")

                out.append({
                    "provision_id": pid, "headline": headline,
                    "effect": effect, "diff": diff,
                    "plain": ui.explain_provision(after),
                    "consequence": consequence,
                })
            return {"clauses": out}

        def _amendment_dossier(self, a, org):
            """The package a lawmaker needs to decide, assembled from the
            ledger.

            A referral arrives as one sentence. That is enough to notify
            somebody and nowhere near enough to decide: what does the rule say
            today, what has it actually done, who waived it and why, what
            happens to existing decisions either way. All of that is already
            in the ledger — it was simply never put in front of the person
            being asked to legislate.
            """
            import json as _json
            from . import db as dbmod
            from . import reviewui as ui

            body = _json.loads(a["body"] or "{}")
            pid = body.get("provision_id")
            if not pid:
                src = a.get("source_record")
                if src:
                    rec = svc.ledger.get(src)
                    pid = rec and rec.get("provision_id")
            if not pid:
                return {}

            r = dbmod.open_reader()
            version = svc.constitution.current_version()
            try:
                prov = svc.constitution.get_provision(version, pid, org=org)
            except Exception:                                  # noqa: BLE001
                prov = None

            # What this rule has actually done.
            stats = r.execute(
                "SELECT COUNT(*) AS decisions,"
                " SUM(is_acceptance) AS waivers,"
                " SUM(CASE WHEN controlling_state='bound' THEN 1 ELSE 0 END)"
                "   AS bound,"
                " MIN(resolved_at) AS first_at, MAX(resolved_at) AS last_at"
                " FROM record_effective WHERE provision_id=? AND superseded=0",
                (pid,)).fetchone()

            # Every waiver ever granted on it, and what became of each.
            waivers = []
            for w in r.execute(
                    "SELECT id, resolving_principal, resolved_at, expiry,"
                    " rationale_text, lapsed FROM record_effective"
                    " WHERE provision_id=? AND is_acceptance=1"
                    " ORDER BY resolved_at DESC LIMIT 6", (pid,)).fetchall():
                waivers.append({
                    "id": w["id"][:8], "who": w["resolving_principal"],
                    "when": (w["resolved_at"] or "")[:10],
                    "until": (w["expiry"] or "")[:10],
                    "state": "expired" if w["lapsed"] else "still live",
                    "why": (w["rationale_text"] or "")[:150],
                })

            # The record that provoked this referral, in full.
            trigger = None
            if a.get("source_record"):
                rec = svc.ledger.get(a["source_record"])
                if rec:
                    events = [e["event_type"]
                              for e in svc.ledger.lifecycle(rec["id"])]
                    trigger = {
                        "id": rec["id"][:8],
                        "who": rec["resolving_principal"],
                        "when": (rec["resolved_at"] or "")[:10],
                        "until": (rec.get("expiry") or "")[:10],
                        "facts": rec.get("facts") or [],
                        "premise": rec.get("premise") or [],
                        "why": rec.get("rationale_text") or "",
                        "events": [ui.say("event", e) for e in events],
                    }

            # How much work this rule touches.
            engaged = r.execute(
                "SELECT COUNT(*) AS n FROM pr_case WHERE provision_id=?",
                (pid,)).fetchone()["n"]

            return {
                "provision_id": pid,
                "text": prov and prov["text"],
                "plain": prov and ui.explain_provision(prov),
                "absolute": bool(prov and prov["absolute"]),
                "source": (prov or {}).get("scope", "tenant"),
                "decisions": stats["decisions"] or 0,
                "waivers": stats["waivers"] or 0,
                "bound": stats["bound"] or 0,
                "first_at": (stats["first_at"] or "")[:10],
                "last_at": (stats["last_at"] or "")[:10],
                "engaged": engaged,
                "waiver_log": waivers,
                "trigger": trigger,
            }

        def _rulebook(self, org):
            """The clauses in force, as they apply to this viewer.

            Resolved through the same overlay adjudication uses, so the page
            cannot show a reader one rulebook while the system enforces
            another. Where a tenant has its own version of a shared clause,
            that is surfaced rather than silently substituted.
            """
            from . import db as dbmod
            r = dbmod.open_reader()
            version = svc.constitution.current_version()
            provisions = svc.constitution.list_provisions(version, org=org)

            # Which ids exist at BOTH levels: those are real overrides.
            base_ids = {x["provision_id"] for x in r.execute(
                "SELECT provision_id FROM provision"
                " WHERE version_id = ? AND organization IS NULL",
                (version,)).fetchall()}
            counts = {x["provision_id"]: x for x in r.execute(
                "SELECT provision_id, COUNT(*) AS holdings,"
                " SUM(CASE WHEN is_acceptance=1 AND lapsed=0 AND superseded=0"
                "     THEN 1 ELSE 0 END) AS live_waivers"
                " FROM record_effective GROUP BY provision_id").fetchall()}

            out = []
            for p in provisions:
                c = counts.get(p["provision_id"])
                out.append({
                    **p,
                    "is_override": bool(p.get("organization")
                                        and p["provision_id"] in base_ids),
                    "holdings": (c["holdings"] if c else 0),
                    "live_waivers": (c["live_waivers"] if c else 0),
                })
            tname = None
            if org:
                row = r.execute("SELECT name FROM organization"
                                " WHERE org_id = ?", (org,)).fetchone()
                tname = row["name"] if row else org
            return out, version, tname

        def _rulebook_history(self, org):
            from . import db as dbmod
            where, args = "", ()
            if org:
                where = " WHERE organization = ? OR organization IS NULL"
                args = (org,)
            return [dict(x) for x in dbmod.open_reader().execute(
                "SELECT * FROM draft_amendment" + where
                + " ORDER BY created_at DESC LIMIT 100", args).fetchall()]

        @staticmethod
        def _is_auditor(principal: str) -> bool:
            return str(principal).endswith(".audit")

        def _desk(self, principal, branch, org):
            """What is waiting for THIS principal.

            Assembled per branch. Nothing here grants authority — every item
            is one the Kernel would let this principal act on, so the desk
            can never offer work somebody cannot do.
            """
            from . import db as dbmod
            from . import reviewui as ui
            r = dbmod.open_reader()
            ow = " AND (organization = ? OR organization IS NULL)" if org \
                else ""
            oa = [org] if org else []
            out = {"reviews": [], "my_waivers": [], "expiring": [],
                   "amendments": [], "friction": [], "decided": [],
                   "blocked": [], "waiting": [], "floored": [],
                   "degraded": [], "lapsed_recent": [], "decided_final": [],
                   "counts": []}

            # An auditor holds no branch and is identified by role, not by
            # authority — which is the point: reading everything while being
            # able to change nothing is a position, not a lesser engineer.
            if self._is_auditor(principal):
                for x in r.execute(
                        "SELECT j.invoked_at, j.tier, j.judge_version,"
                        " j.verdict FROM judgment_invocation j"
                        " WHERE j.degraded=1 ORDER BY j.invoked_at DESC"
                        " LIMIT 15").fetchall():
                    out["degraded"].append({
                        "tag": f"tier {x['tier']}",
                        "what": "the judge did not answer",
                        "detail": f"fell back · {x['judge_version']}",
                        "url": "/review/activity/judge?view=degraded",
                        "tone": "deny",
                        "when": (x["invoked_at"] or "")[:10]})
                for x in r.execute(
                        "SELECT id, provision_id, expiry, resolving_principal"
                        " FROM record_effective WHERE lapsed=1" + ow +
                        " ORDER BY expiry DESC LIMIT 15", oa).fetchall():
                    out["lapsed_recent"].append({
                        "tag": x["provision_id"],
                        "what": f"expired {(x['expiry'] or '')[:10]}",
                        "detail": f"accepted by {x['resolving_principal']}",
                        "url": f"/review/ledger/{x['id']}", "tone": "deny"})
                for x in r.execute(
                        "SELECT id, provision_id, resolving_principal,"
                        " resolved_at FROM precedent_record"
                        " WHERE authority_tier=4" + ow +
                        " ORDER BY resolved_at DESC LIMIT 15", oa).fetchall():
                    out["decided_final"].append({
                        "tag": x["provision_id"],
                        "what": f"signed by {x['resolving_principal']}",
                        "detail": "final — cannot be reopened",
                        "url": f"/review/ledger/{x['id']}",
                        "when": (x["resolved_at"] or "")[:10]})
                out["counts"] = [
                    ("Decisions on record", r.execute(
                        "SELECT COUNT(*) AS n FROM precedent_record"
                        " WHERE 1=1" + ow, oa).fetchone()["n"], ""),
                    ("Waivers that expired", len(out["lapsed_recent"]),
                     " lapsed" if out["lapsed_recent"] else ""),
                    ("Answers that fell back", len(out["degraded"]),
                     " lapsed" if out["degraded"] else "")]
                return out

            if branch == "risk_owner":
                for t in svc.gateway.reviews.list("open", org=org):
                    out["reviews"].append({
                        "tag": t["provision_id"], "what": t["title"][:90],
                        "detail": "the automated tiers are exhausted",
                        "url": f"/review/{t['task_id']}", "tone": "wait",
                        "when": (t["opened_at"] or "")[:10]})
                for x in r.execute(
                        "SELECT id, provision_id, expiry, rationale_text"
                        " FROM record_effective WHERE is_acceptance=1"
                        " AND lapsed=0 AND superseded=0"
                        " AND resolving_principal=?" + ow
                        + " ORDER BY expiry LIMIT 25",
                        [principal] + oa).fetchall():
                    days = _days_until(x["expiry"])
                    row = {"tag": x["provision_id"],
                           "what": f"expires {(x['expiry'] or '')[:10]}",
                           "detail": (x["rationale_text"] or "")[:110],
                           "url": f"/review/ledger/{x['id']}",
                           "note": (f"{days} days" if days is not None
                                    else ""),
                           "tone": "wait"}
                    out["my_waivers"].append(row)
                    if days is not None and days <= 30:
                        out["expiring"].append({**row, "tone": "deny"})
                out["counts"] = [
                    ("Waiting for you", len(out["reviews"]),
                     " amber" if out["reviews"] else ""),
                    ("Your live acceptances", len(out["my_waivers"]), ""),
                    ("Expiring in 30 days", len(out["expiring"]),
                     " lapsed" if out["expiring"] else "")]

            elif branch == "lawmakers":
                aw = " AND (organization = ? OR organization IS NULL)" \
                    if org else ""
                for x in r.execute(
                        "SELECT id, origin, body, created_at, source_record"
                        " FROM draft_amendment WHERE status='pending'" + aw
                        + " ORDER BY created_at DESC LIMIT 25",
                        oa).fetchall():
                    b = json.loads(x["body"] or "{}")
                    out["amendments"].append({
                        "tag": b.get("provision_id") or "constitution",
                        "what": ui.say("origin", x["origin"]),
                        "detail": (b.get("note") or b.get("question")
                                   or "")[:110],
                        "url": "/review/amendments", "tone": "wait",
                        "note": f"#{x['id'][:8]}",
                        "when": (x["created_at"] or "")[:10]})
                for x in r.execute(
                        "SELECT provision_id, COUNT(*) AS n,"
                        " SUM(is_acceptance) AS w FROM record_effective"
                        " WHERE superseded=0" + ow
                        + " GROUP BY provision_id HAVING w > 0"
                        " ORDER BY w DESC, n DESC LIMIT 8", oa).fetchall():
                    out["friction"].append({
                        "tag": x["provision_id"],
                        "what": f"waived {x['w']} time(s)",
                        "detail": f"{x['n']} decision(s) recorded under it",
                        "url": "/review/rulebook", "tone": "wait"})
                for x in r.execute(
                        "SELECT id, origin, body, status, decided_at"
                        " FROM draft_amendment WHERE status<>'pending'" + aw
                        + " ORDER BY decided_at DESC LIMIT 8",
                        oa).fetchall():
                    b = json.loads(x["body"] or "{}")
                    out["decided"].append({
                        "tag": b.get("provision_id") or "constitution",
                        "what": ui.say("status", x["status"]),
                        "detail": ui.say("origin", x["origin"]),
                        "url": "/review/rulebook/history",
                        "when": (x["decided_at"] or "")[:10]})
                out["counts"] = [
                    ("Awaiting your decision", len(out["amendments"]),
                     " amber" if out["amendments"] else ""),
                    ("Rules under strain", len(out["friction"]), ""),
                    ("Recently decided", len(out["decided"]), "")]

            else:
                sw = " AND (organization = ? OR organization IS NULL)" \
                    if org else ""
                rows = r.execute(
                    "SELECT session_id, repo, pr_number, disposition,"
                    " provisions, received_at FROM pr_session_current"
                    " WHERE disposition IN ('blocked_challengeable',"
                    " 'human_review','blocked_absolute','blocked_final')"
                    + sw + " ORDER BY received_at DESC LIMIT 40",
                    oa).fetchall()
                for x in rows:
                    provs = json.loads(x["provisions"] or "[]")
                    row = {"tag": f"{x['repo']}#{x['pr_number']}",
                           "what": ui.say("disposition", x["disposition"]),
                           "detail": ", ".join(provs) or "no clause engaged",
                           "url": f"/review/change/{x['session_id']}",
                           "when": (x["received_at"] or "")[:10]}
                    if x["disposition"] == "blocked_challengeable":
                        out["blocked"].append({**row, "tone": "open",
                                               "note": "you can contest"})
                    elif x["disposition"] == "human_review":
                        out["waiting"].append({**row, "tone": "wait",
                                               "note": "with a risk owner"})
                    else:
                        out["floored"].append({**row, "tone": "floor",
                                               "note": "no appeal"})
                out["counts"] = [
                    ("Open to you", len(out["blocked"]),
                     " amber" if out["blocked"] else ""),
                    ("Waiting on a person", len(out["waiting"]), ""),
                    ("At a floor", len(out["floored"]),
                     " lapsed" if out["floored"] else "")]
            return out

        def _judge_activity(self, org, view, cursor, limit=60):
            """Every distinguishing question, with the facts it was about.

            Joined back to the case and the candidate so the question can be
            shown in full. Scoped by tenant like everything else: a judge
            call belongs to the case that provoked it.
            """
            from . import db as dbmod
            r = dbmod.open_reader()

            where, args = [], []
            if view == "paid":
                where.append("j.from_cache = 0")
            elif view == "cached":
                where.append("j.from_cache = 1")
            elif view == "degraded":
                where.append("j.degraded = 1")
            elif view == "quorum":
                where.append("j.quorum_votes IS NOT NULL")
            elif view == "disagreed":
                where.append("json_extract(j.verdict,'$.distinguished') = 1")
            if org:
                where.append("(cs.organization = ? OR cs.organization IS NULL)")
                args.append(org)
            if cursor:
                where.append("j.invoked_at < ?")
                args.append(cursor)

            sql = f"""
                SELECT j.invoked_at, j.tier, j.judge_version, j.prompt_version,
                       j.verdict, j.from_cache, j.degraded, j.latency_ms,
                       j.input_tokens, j.output_tokens, j.quorum_votes,
                       cs.facts AS case_facts, cs.provision_id,
                       pr.premise AS cand_premise
                  FROM judgment_invocation j
                  LEFT JOIN case_state cs ON cs.case_hash = j.case_hash
                  LEFT JOIN precedent_record pr
                         ON pr.content_hash = j.candidate_hash
                 WHERE j.kind = 'distinguish'
                   {(' AND ' + ' AND '.join(where)) if where else ''}
                 ORDER BY j.invoked_at DESC LIMIT ?"""
            rows = r.execute(sql, args + [limit + 1]).fetchall()
            more = len(rows) > limit
            rows = rows[:limit]

            out = []
            for x in rows:
                v = json.loads(x["verdict"])
                votes = json.loads(x["quorum_votes"]) if x["quorum_votes"] \
                    else None
                out.append({
                    "at": x["invoked_at"], "tier": x["tier"],
                    "judge": x["judge_version"],
                    "prompt_version": x["prompt_version"],
                    "distinguished": bool(v.get("distinguished")),
                    "grounds": v.get("grounds") or "",
                    "from_cache": bool(x["from_cache"]),
                    "degraded": bool(x["degraded"]),
                    "latency_ms": x["latency_ms"] or 0,
                    "in_tok": x["input_tokens"] or 0,
                    "out_tok": x["output_tokens"] or 0,
                    "votes": len(votes) if votes else 0,
                    "provision_id": x["provision_id"],
                    "facts": json.loads(x["case_facts"] or "[]"),
                    "premise": json.loads(x["cand_premise"] or "[]"),
                })

            org_w = (" AND (cs.organization = ? OR cs.organization IS NULL)"
                     if org else "")
            org_a = [org] if org else []
            base = ("SELECT COUNT(*) AS n FROM judgment_invocation j"
                    " LEFT JOIN case_state cs ON cs.case_hash = j.case_hash"
                    " WHERE j.kind='distinguish'" + org_w)
            one = lambda extra, a=(): r.execute(  # noqa: E731
                base + extra, org_a + list(a)).fetchone()["n"]
            judges = [x["judge_version"] for x in r.execute(
                "SELECT DISTINCT judge_version FROM judgment_invocation"
            ).fetchall()]
            stats = {
                None: one(""),
                "paid": one(" AND j.from_cache=0"),
                "cached": one(" AND j.from_cache=1"),
                "degraded": one(" AND j.degraded=1"),
                "quorum": one(" AND j.quorum_votes IS NOT NULL"),
                "disagreed": one(" AND json_extract(j.verdict,"
                                 "'$.distinguished')=1"),
                "mode": ("oracle" if judges and all(
                    j.startswith("oracle") for j in judges) else "live"),
                "prompt_version": (out[0]["prompt_version"] if out else None),
            }
            return out, stats, (rows[-1]["invoked_at"] if more and rows
                                else None)

        def _activity_where(self, f, org, cursor):
            where, args = [], []
            if org:
                # NULL means PLATFORM-WIDE, not "unattributed", and this feed
                # answers "what happened that concerns me". A shared clause
                # being amended, or a holding promoted to platform law,
                # concerns every tenant — and retrieval and the legislature
                # list already read NULL that way. Activity alone did not,
                # so on any ledger holding platform-level events a scoped
                # user saw an empty page while every other screen worked.
                where.append("(org = ? OR org IS NULL)")
                args.append(org)
            if f.get("kind"):
                where.append("kind = ?")
                args.append(f["kind"])
            if f.get("q"):
                like = f"%{f['q']}%"
                where.append("(what LIKE ? OR detail LIKE ? OR actor LIKE ?)")
                args += [like, like, like]
            if f.get("since"):
                try:
                    days = int(f["since"])
                    where.append("at >= datetime('now', ?)")
                    args.append(f"-{days} days")
                except ValueError:
                    pass
            if cursor:
                where.append("at < ?")
                args.append(cursor)
            return (" WHERE " + " AND ".join(where) if where else ""), args

        def _activity(self, f, org, cursor, limit=60):
            from . import db as dbmod
            w, args = self._activity_where(f, org, cursor)
            rows = [dict(x) for x in dbmod.open_reader().execute(
                f"SELECT * FROM ({self.ACTIVITY_SQL}){w}"
                f" ORDER BY at DESC LIMIT ?", args + [limit + 1]).fetchall()]
            more = len(rows) > limit
            rows = rows[:limit]
            out = [{"kind": r["kind"], "at": r["at"], "what": r["what"],
                    "detail": r["detail"], "actor": r["actor"],
                    "url": r["url"], "tone": r["tone"],
                    "organization": r["org"]} for r in rows]
            return out, (rows[-1]["at"] if more and rows else None)

        def _activity_counts(self, org):
            from . import db as dbmod
            w, args = self._activity_where({}, org, None)
            return {x["kind"]: x["n"] for x in dbmod.open_reader().execute(
                f"SELECT kind, COUNT(*) AS n FROM ({self.ACTIVITY_SQL}){w}"
                f" GROUP BY kind", args).fetchall()}

        def _analytics(self):
            """Adjudication cost per level of escalation.

            Container-wide rather than per tenant: a judgment records the
            TIER that asked, not the company, and inventing an attribution
            the data does not support would be worse than saying so.
            """
            from . import db as dbmod
            r = dbmod.open_reader()
            price_in = float(os.environ.get("DJ_PRICE_IN", "3.00"))
            price_out = float(os.environ.get("DJ_PRICE_OUT", "15.00"))
            k = 4

            inv = [dict(x) for x in r.execute(
                "SELECT tier,"
                " SUM(CASE WHEN from_cache=0 THEN 1 ELSE 0 END) AS paid,"
                " SUM(from_cache) AS cached,"
                " COALESCE(SUM(input_tokens),0) AS tin,"
                " COALESCE(SUM(output_tokens),0) AS tout,"
                " CAST(AVG(latency_ms) AS INTEGER) AS lat"
                " FROM judgment_invocation GROUP BY tier ORDER BY tier"
            ).fetchall()]
            ending = {x["current_tier"]: x["n"] for x in r.execute(
                "SELECT current_tier, COUNT(*) AS n FROM case_state"
                " GROUP BY current_tier").fetchall()}
            cases = sum(ending.values())
            oracle_only = (r.execute(
                "SELECT COUNT(*) AS n FROM judgment_invocation"
                " WHERE input_tokens IS NOT NULL").fetchone()["n"] == 0)

            def money(tin, tout):
                return (tin / 1e6) * price_in + (tout / 1e6) * price_out

            tiers, total_cost = [], 0.0
            for row in inv:
                t = row["tier"] or 1
                cost = money(row["tin"], row["tout"])
                total_cost += cost
                n = ending.get(t, 0)
                tiers.append({
                    "tier": t, "cases": n, "paid": row["paid"] or 0,
                    "cached": row["cached"] or 0, "tokens_in": row["tin"],
                    "tokens_out": row["tout"], "latency": row["lat"] or 0,
                    "cost_display": f"${cost:.4f}" if cost else "$0",
                    "per_case": (f"${cost / n:.4f}" if cost and n else
                                 f"{round((row['paid'] or 0) / n, 1)} calls"
                                 if n else "—"),
                })
            for t in sorted(ending):
                if not any(x["tier"] == t for x in tiers):
                    tiers.append({"tier": t, "cases": ending[t], "paid": 0,
                                  "cached": 0, "tokens_in": 0,
                                  "tokens_out": 0, "latency": 0,
                                  "cost_display": "$0", "per_case": "—"})
            tiers.sort(key=lambda x: x["tier"])

            paid = sum(t["paid"] for t in tiers)
            cached = sum(t["cached"] for t in tiers)
            contested = sum(n for t, n in ending.items() if t >= 2)
            to_human = ending.get(k, 0)

            top = [t for t in tiers if t["cases"]]
            reading = (
                "Most cases end at the first rung and cost one pass of"
                " retrieval and distinguishing. Escalation is rare and each"
                " rung costs a fresh set of judgements, because a tier that"
                " reused the rung below's verdict would not be reviewing"
                " anything." if len(top) > 1 else
                "Everything decided at a single tier so far, so there is no"
                " escalation gradient to read yet.")

            return {
                "tiers": tiers, "k": k, "cases": cases,
                "calls_paid": paid, "calls_cached": cached,
                "mean_calls": round(paid / cases, 2) if cases else 0,
                "mean_cost_display": (f"${total_cost / cases:.4f}"
                                      if cases and total_cost else
                                      "$0" if oracle_only else "$0"),
                "mean_contested_display": (
                    f"${total_cost / contested:.4f}" if contested and
                    total_cost else f"{contested} contested"),
                "degraded": r.execute(
                    "SELECT COUNT(*) AS n FROM judgment_invocation"
                    " WHERE degraded=1").fetchone()["n"],
                "oracle_only": oracle_only, "price_in": price_in,
                "price_out": price_out, "to_human": to_human,
                "reading": reading,
            }

        def _impact(self, org):
            from . import db as dbmod
            r = dbmod.open_reader()
            by = {x["disposition"] or "pending": x["n"] for x in self._scoped(
                "SELECT disposition, COUNT(*) AS n FROM pr_session_current"
                " WHERE 1=1{ORG} GROUP BY disposition", org)}
            c = svc.ledger.census(org=org)
            # Citation is counted over DECISIONS, not records. Proposition 3
            # means the uncontested majority writes nothing, so counting
            # precedent reuse by counting rows in the ledger structurally
            # undercounts it — the citation happened whether or not anyone
            # challenged the result afterwards.
            bsql = ("SELECT COUNT(*) AS n FROM pr_session_current s,"
                    " json_each(s.detail) j WHERE"
                    " json_extract(j.value,'$.controlling_state')='bound'")
            bargs = ()
            if org:
                bsql += " AND (s.organization = ? OR s.organization IS NULL)"
                bargs = (org,)
            bound = r.execute(bsql, bargs).fetchone()["n"]
            csql = bsql.replace(
                "json_extract(j.value,'$.controlling_state')='bound'",
                "json_array_length(json_extract(j.value,'$.consulted')) > 0")
            consulted = r.execute(csql, bargs).fetchone()["n"]
            refs = r.execute(
                "SELECT COUNT(*) AS n FROM draft_amendment"
                " WHERE origin='judicial_referral'").fetchone()["n"]
            j = r.execute(
                "SELECT COUNT(*) AS n,"
                " SUM(CASE WHEN from_cache=1 THEN 1 ELSE 0 END) AS cached"
                " FROM judgment_invocation").fetchone()
            return {
                "governed": sum(by.values()),
                "cleared": by.get("proceed", 0)
                + by.get("proceed_with_conditions", 0),
                "to_human": by.get("human_review", 0),
                "floors": by.get("blocked_absolute", 0),
                "to_legislature": by.get("routed_amendment", 0),
                "records": c["records"], "bound": bound,
                "consulted": consulted,
                "live_acceptances": c["live_acceptances"],
                "lapsed": c["lapsed"], "referrals": refs,
                "judge_calls": (j["n"] or 0) - (j["cached"] or 0),
                "cache_hits": j["cached"] or 0,
            }

        def _live_state(self) -> dict:
            """What the sign-in page needs to know about live judging.

            Reports only whether a key is PRESENT. The value is never read
            into the page, never logged, and never echoed — the panel needs
            to know it exists, not what it is.
            """
            return {
                "mode": os.environ.get("DJ_JUDGE_MODE", "oracle"),
                "have_key": bool(os.environ.get("ANTHROPIC_API_KEY", "")),
                "running": bool(getattr(svc, "_live_switch", None)),
                "ladder": ", ".join(
                    f"tier {i}: {os.environ[f'DJ_JUDGE_MODEL_T{i}']}"
                    for i in (1, 2, 3)
                    if os.environ.get(f"DJ_JUDGE_MODEL_T{i}")) or None,
            }

        def _roster(self) -> list[dict]:
            """The sign-in bench. DEVELOPMENT ONLY — it lists credentials,
            so it is built only when the container was booted with
            deterministic dev keys and is empty in any real deployment."""
            if os.environ.get("DJ_DEV_KEYS") != "1":
                return []
            from . import bootstrap as bs
            from . import db as dbmod
            # Read the REGISTRY, not a hardcoded list. Tenant officers are
            # created from the demo corpus rather than from DEV_KEYS, and a
            # bench that only knew about the founding accounts could not sign
            # anyone in to the tenants the demo just created.
            people = dbmod.open_reader().execute(
                "SELECT principal_id, organization, role_hint FROM principal"
                " WHERE kind='human' ORDER BY organization, principal_id"
            ).fetchall()
            out = []
            for row in people:
                pid = row["principal_id"]
                key = bs.DEV_KEYS.get(pid) or self._demo_key(pid)
                if not key:
                    continue
                branch = svc.registry.resolve_branch(pid)
                out.append({
                    "principal": pid, "key": key, "branch": branch,
                    "organization": row["organization"],
                    "can": row["role_hint"] or (
                        "decides risk acceptances"
                        if branch == "risk_owner" else
                        "amends the constitution"
                        if branch == "lawmakers" else
                        "adjudicates" if branch == "judges" else
                        "files and contests only"),
                })
            # Grouped by tenant, most powerful first within each: the bench
            # is there to make the difference between principals obvious.
            rank = {"risk_owner": 0, "lawmakers": 1, "judges": 2}
            return sorted(out, key=lambda r: (r["organization"] or "",
                                              rank.get(r["branch"], 3),
                                              r["principal"]))

        def _demo_key(self, principal_id: str) -> str | None:
            """Dev key for a tenant officer, from whichever corpus created it.

            Searches the SELECTED pack first and then every other pack, which
            matters more than it looks: the registry and the seed directory
            can disagree. A database built with `_all` and then served with
            DJ_DEMO=sctower still contains all four tenants' officers, and
            looking only in the selected pack dropped twelve real accounts
            from the sign-in list with no error — they existed, their keys
            worked, and the page simply could not name them.
            """
            import json as _json
            from . import bootstrap as bs
            packs = [os.path.join(bs.SEED_DIR, "organizations.json")]
            root = os.path.join(os.path.dirname(os.path.dirname(
                os.path.abspath(__file__))), "demo", "companies")
            if os.path.isdir(root):
                packs += [os.path.join(root, d, "organizations.json")
                          for d in sorted(os.listdir(root))]
            seen = set()
            for path in packs:
                rp = os.path.realpath(path)
                if rp in seen or not os.path.exists(rp):
                    continue
                seen.add(rp)
                try:
                    doc = _json.load(open(rp))
                except (OSError, ValueError):
                    continue
                for org in doc.get("organizations", []):
                    for pr in org.get("principals", []):
                        if pr["principal_id"] == principal_id:
                            return pr["key"]
            return None

        def _holds_risk_owner(self, principal: str) -> bool:
            """Whether to DRAW the instrument. Never whether to allow it —
            that is the Kernel's call, made again at the point of action."""
            return svc.registry.resolve_branch(principal) == "risk_owner"

        def _viewer(self) -> tuple[str, str]:
            """(api_key, principal_id) for the review screen, or ('','')."""
            key = self._session_key()
            if not key:
                return "", ""
            return key, (svc.registry.authenticate(key) or "")

        # -- routing ----------------------------------------------------
        def do_GET(self):
            try:
                if self.path == "/v1/healthz":
                    return self._send(200, {"ok": True})
                if self.path == "/v1/admin/status":
                    return self._send(200, self._admin_status())
                if self.path == "/v1/admin/installations":
                    from .platform import tenancy
                    return self._send(200, {
                        "installations": tenancy.list_installations()})
                if self.path == "/v1/demo/status":
                    from . import demo as demomod
                    return self._send(200, demomod.status(svc))
                if self.path.startswith("/review"):
                    return self._review_get()
                p = self._principal()
                if p is None:
                    return self._send(401, {"error": "authentication required"})
                if m := re.fullmatch(r"/v1/pr/([\w-]+)", self.path):
                    return self._send(200,
                                      svc.gateway.session_view(m.group(1)))
                if m := re.fullmatch(r"/v1/decisions/([\w-]+)", self.path):
                    c = svc.adjudicator.get_case(m.group(1))
                    return self._send(200, c) if c else \
                        self._send(404, {"error": "case not found"})
                if m := re.fullmatch(r"/v1/records/([\w-]+)/dossier",
                                     self.path):
                    return self._send(200, self._dossier(m.group(1)))
                if m := re.fullmatch(r"/v1/records/([\w-]+)", self.path):
                    r = svc.ledger.get(m.group(1))
                    return self._send(200, r) if r else \
                        self._send(404, {"error": "record not found"})
                if self.path == "/v1/constitution/current":
                    v = svc.constitution.current_version()
                    return self._send(200, {
                        "version_id": v,
                        "provisions": svc.constitution.list_provisions(v)})
                return self._send(404, {"error": "no such route"})
            except InboundError as e:
                return self._send(e.status, {"error": str(e),
                                             "code": e.code})
            except KernelError as e:
                return self._send(e.status, {"error": str(e)})
            except Exception as e:  # noqa: BLE001
                return self._send(500, {"error": f"internal: {e}"})

        def do_POST(self):
            try:
                # -- L5 inbound. Deliberately BEFORE the bearer check: a
                # webhook does not carry an API key, it carries an HMAC over
                # the body. That signature is the authentication, and the
                # gateway acts as its own low-privilege principal, so the
                # exception widens no authority (see IFP-09).
                if self.path == "/v1/inbound/github":
                    return self._inbound_github()
                if self.path == "/v1/inbound/generic":
                    return self._inbound_generic()
                if self.path.startswith("/review"):
                    return self._review_post()

                p = self._principal()
                if p is None:
                    return self._send(401, {"error": "authentication required"})

                if m := re.fullmatch(r"/v1/pr/([\w-]+)/(challenge|human-review)",
                                     self.path):
                    return self._pr_lane(m.group(1), m.group(2), p)

                b = self._body()
                if self.path == "/v1/cases":
                    facts = b.get("facts", [])
                    if not isinstance(facts, list) or not all(
                            isinstance(x, str) for x in facts):
                        return self._send(422, {
                            "error": "facts must be a list of strings",
                            "code": "bad_facts"})
                    if not b.get("provision_id"):
                        return self._send(422, {
                            "error": "provision_id is required",
                            "code": "bad_request"})
                    return self._send(200, svc.adjudicator.submit_case(
                        b["provision_id"], facts, p,
                        b.get("case_scope") or {}))
                if m := re.fullmatch(r"/v1/decisions/([\w-]+)/challenge",
                                     self.path):
                    return self._send(200, svc.adjudicator.challenge(
                        m.group(1), p, b.get("grounds", "")))
                if m := re.fullmatch(r"/v1/decisions/([\w-]+)/accept",
                                     self.path):
                    return self._send(200, svc.adjudicator.accept_resolution(
                        m.group(1), p))
                if m := re.fullmatch(r"/v1/cases/([\w-]+)/risk-decision",
                                     self.path):
                    return self._send(200, svc.adjudicator.risk_decision(
                        m.group(1), p, b["decision"],
                        b.get("rationale", ""), b.get("expiry")))
                if self.path == "/v1/amendments":
                    aid = svc.constitution.file_amendment(
                        p, b.get("origin", "engineer"), b.get("body", {}),
                        organization=svc.registry.organization_of(p))
                    return self._send(200, {"amendment_id": aid,
                                            "status": "pending"})
                if m := re.fullmatch(r"/v1/amendments/([\w-]+)/decision",
                                     self.path):
                    return self._send(200, svc.constitution.decide_amendment(
                        m.group(1), b["decision"], p))
                if self.path == "/v1/admin/lifecycle-sweep":
                    n = svc.lifecycle.sweep_once()
                    return self._send(200, {"lapsed_emitted": n})
                if self.path == "/v1/admin/outbound-retry":
                    from . import outbound
                    return self._send(200, outbound.retry_failed())
                if self.path == "/v1/admin/installations":
                    from .platform import tenancy
                    return self._send(200, {
                        "installations": tenancy.list_installations()})
                if self.path == "/v1/admin/installations/register":
                    from .platform import tenancy
                    b = self._body()
                    iid = b.get("installation_id") or ""
                    if not iid:
                        return self._send(422, {
                            "error": "installation_id required"})
                    tenancy.upsert_installation(
                        iid,
                        provider=b.get("provider") or "github",
                        organization=b.get("organization"),
                        account_login=b.get("account_login"),
                        repos=b.get("repos") or [])
                    return self._send(200, {"registered": iid})
                if self.path == "/v1/admin/break-glass":
                    from . import enterprise
                    return self._send(200, enterprise.break_glass(
                        svc, p, b.get("reason", ""),
                        session_id=b.get("session_id"),
                        repo=b.get("repo"),
                        pr_number=b.get("pr_number"),
                        expiry_hours=int(b.get("expiry_hours") or 24)))
                if self.path == "/v1/admin/post-merge-scan":
                    from . import enterprise, jobs
                    repo = b.get("repo") or ""
                    sha = b.get("sha") or ""
                    if not repo or not sha:
                        return self._send(422, {
                            "error": "repo and sha are required",
                            "code": "bad_request"})
                    payload = {
                        "repo": repo, "sha": sha,
                        "factors": b.get("factors") or [],
                        "provisions": b.get("provisions") or [],
                        "organization": b.get("organization")
                        or enterprise.repo_organization(repo),
                    }
                    if os.environ.get("DJ_ASYNC_INBOUND") == "1":
                        jid = jobs.enqueue("post_merge_scan", payload)
                        return self._send(202, {"job_id": jid,
                                                "mode": "async"})
                    return self._send(200, enterprise.run_post_merge_scan(
                        svc, payload))
                if self.path == "/v1/admin/constitution":
                    # Upload / enact a rulebook JSON: {"provisions":[...]} or a bare list.
                    # Lawmakers only. Does not delete prior versions — pins a new one.
                    # (body already read into b above)
                    provisions = b.get("provisions") if isinstance(b, dict) else b
                    if not isinstance(provisions, list) or not provisions:
                        return self._send(422, {
                            "error": "body must be {\"provisions\": [...]} "
                                     "or a non-empty list",
                            "code": "bad_constitution"})
                    for i, pr in enumerate(provisions):
                        if not isinstance(pr, dict) or not pr.get("provision_id"):
                            return self._send(422, {
                                "error": f"provision[{i}] needs provision_id",
                                "code": "bad_constitution"})
                    ver = svc.constitution.enact_version(
                        provisions, p, amendment_id=None, bootstrap=False)
                    return self._send(200, {
                        "version_id": ver if not isinstance(ver, dict) else ver,
                        "provisions": len(provisions),
                        "enacted_by": p})
                if self.path == "/v1/admin/connectors":
                    from .platform.connectors import registry as creq
                    from .platform.dj_config import get_config, public_view
                    return self._send(200, {
                        "known": creq.known(),
                        "configured": public_view(get_config()).get("connectors"),
                    })
                return self._send(404, {"error": "no such route"})
            except InboundError as e:
                return self._send(e.status, {"error": str(e),
                                             "code": e.code})
            except KernelError as e:
                return self._send(e.status, {"error": str(e)})
            except (KeyError, json.JSONDecodeError) as e:
                return self._send(422, {"error": f"bad request: {e}"})
            except Exception as e:  # noqa: BLE001
                return self._send(500, {"error": f"internal: {e}"})

        # ==============================================================
        # L5 inbound: a pull request arrives
        # ==============================================================

        def _inbound_generic(self):
            """Plugin path: generic connector → optional enqueue → gateway.

            For EV1 the normalized ChangeRequest is re-encoded as a synthetic
            GitHub-like submit only when the operator wires a bridge; until
            then this endpoint validates the connector and returns the
            normalized change for integration tests.
            """
            from .platform.connectors.registry import get as get_connector
            headers = {k.lower(): v for k, v in self.headers.items()}
            raw = self._raw_body()
            result = get_connector("generic").accept(headers, raw)
            if not result.ok:
                return self._send(result.status, {
                    "error": result.error or "connector rejected",
                    "code": "connector_error"})
            if result.ignore_reason:
                return self._send(200, {"ignored": result.ignore_reason})
            ch = result.change
            return self._send(200, {
                "accepted": True,
                "provider": ch.provider,
                "delivery_id": ch.delivery_id,
                "repo": ch.repo,
                "organization": ch.organization,
                "note": "generic connector normalized OK; wire to PRGateway "
                        "via DJ_GENERIC_BRIDGE=1 in a later pass",
            })

        def _inbound_github(self):
            from . import enterprise, jobs
            if not enterprise.inbound_limiter().allow():
                return self._send(429, {"error": "rate limited",
                                        "code": "rate_limited"})
            headers = {k.lower(): v for k, v in self.headers.items()}
            raw = self._raw_body()
            # Async path: enqueue and acknowledge so GitHub is not held
            # open while adjudication (or an LLM judge) runs. The worker
            # calls the same gateway.receive path; delivery_id idempotency
            # still holds on redelivery.
            if os.environ.get("DJ_ASYNC_INBOUND") == "1":
                try:
                    # Verify signature before enqueue so junk never lands
                    # in the job table.
                    from .inbound_github import verify_signature
                    verify_signature(raw, headers.get("x-hub-signature-256"))
                except InboundError as e:
                    return self._send(e.status, {"error": str(e),
                                                 "code": e.code})
                job_id = jobs.enqueue("github_inbound", {
                    "headers": {
                        "x-github-event": headers.get("x-github-event", ""),
                        "x-github-delivery": headers.get(
                            "x-github-delivery", ""),
                        "x-hub-signature-256": headers.get(
                            "x-hub-signature-256", ""),
                    },
                    "raw": raw.decode("utf-8", "replace"),
                })
                return self._send(202, {"accepted": True, "job_id": job_id,
                                        "mode": "async"})
            try:
                out = svc.gateway.receive(headers, raw)
            except InboundError as e:
                return self._send(e.status, {"error": str(e), "code": e.code})
            except KernelError as e:
                return self._send(e.status, {"error": str(e)})
            return self._send(200, out)

        # -- L5 outbound lanes: what the PR may do next ----------------
        def _pr_lane(self, session_id: str, lane: str, principal: str):
            grounds = self._body().get("grounds", "")
            if lane == "challenge":
                out = svc.gateway.challenge(session_id, principal, grounds)
            else:
                out = svc.gateway.request_human_review(
                    session_id, principal, grounds)
            return self._send(200, out)

        # ==============================================================
        # L5 human review: the screen where a named person signs
        # ==============================================================
        LEDGER_PAGE = 50

        def _review_get(self):
            key, principal = self._viewer()
            split = urllib.parse.urlsplit(self.path)
            path = split.path
            qs = urllib.parse.parse_qs(split.query)

            def arg(name):
                v = qs.get(name, [""])[0].strip()
                return v or None
            if path in ("/review/login", "/review/login/"):
                branch = svc.registry.resolve_branch(principal) \
                    if principal else None
                return self._html(200, reviewui.login_page(
                    current=(principal, branch) if principal else None,
                    roster=self._roster(),
                    orgs=svc.registry.organizations(),
                    corpus=os.environ.get("DJ_DEMO") or None,
                    live=self._live_state()))
            if path in ("/review/logout", "/review/logout/"):
                # A GET cannot be trusted to be intentional (a prefetch is a
                # GET), so it offers the control rather than performing it.
                return self._html(200, reviewui.login_page(
                    current=((principal, svc.registry.resolve_branch(principal))
                             if principal else None),
                    roster=self._roster()))
            if not principal:
                return self._html(200, reviewui.login_page(
                    next_url=path, roster=self._roster(),
                    orgs=svc.registry.organizations(),
                    corpus=os.environ.get("DJ_DEMO") or None,
                    live=self._live_state()))
            branch = svc.registry.resolve_branch(principal)
            # The viewer's tenant, resolved from the PRINCIPAL. It is never
            # read from the URL, so there is no parameter to tamper with:
            # a scoped principal cannot ask for another tenant's ledger.
            vorg = svc.registry.organization_of(principal)
            # Tenant switcher. It can only NARROW: a principal already scoped
            # to a tenant has their own scope applied and the parameter
            # ignored entirely, so there is nothing here to tamper with. For
            # a group officer who can already see every tenant, choosing one
            # is a convenience, not an escalation.
            if vorg is None:
                vorg = arg("as") or None
            scoped = svc.registry.organization_of(principal) is not None
            tenants = [] if scoped else svc.registry.organizations()
            if path in ("/review", "/review/"):
                return self._html(200, reviewui.desk_page(
                    self._desk(principal, branch, vorg), principal, branch,
                    vorg, scoped=scoped, tenants=tenants,
                    is_auditor=self._is_auditor(principal)))
            if path in ("/review/queue", "/review/queue/"):
                open_tasks = svc.gateway.reviews.list("open", org=vorg)
                try:
                    from . import db as _db, jobs as _jobs
                    from .platform.dj_config import get_config
                    _cfg = get_config()
                    _ledger = "postgres" if _db.use_postgres_ledger() else "sqlite"
                    _strip = reviewui.status_strip(
                        open_count=len(open_tasks),
                        judge_mode=os.environ.get(
                            "DJ_JUDGE_MODE", _cfg.judges_mode),
                        ledger=_ledger,
                        profile=os.environ.get("DJ_PROFILE", _cfg.profile),
                        async_inbound=os.environ.get(
                            "DJ_ASYNC_INBOUND", "0") == "1",
                        queue_backend=_jobs.backend_name(),
                    )
                except Exception:
                    _strip = reviewui.status_strip(
                        open_count=len(open_tasks))
                return self._html(200, reviewui.queue_page(
                    open_tasks, principal, branch, org=vorg, scoped=scoped,
                    tenants=tenants, here='/review/queue', strip=_strip))
            # Ordered before the task route: /review/{id} would match these.
            if path in ("/review/changes", "/review/changes/"):
                rows, counts = self._change_stream(vorg)
                return self._html(200, reviewui.changes_page(
                    rows, counts, principal, branch, vorg, scoped=scoped,
                    tenants=tenants))
            # Ordered before /review/{task}: a two-segment path would
            # otherwise fall through to the task route and 404.
            if m := re.fullmatch(r"/review/change/([\w-]+)", path):
                view = self._change_view(m.group(1), vorg)
                if view is None:
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such change"
                        "</h1><p>Nothing under that session id.</p></div>"))
                return self._html(200, reviewui.change_page(
                    view, principal, branch, vorg,
                    token=reviewui.csrf_token(m.group(1), key)))
            if path in ("/review/amendments", "/review/amendments/"):
                pend, done, friction = self._legislature(vorg)
                flash = {"id": arg("decided") or "", "status": arg("outcome"),
                         "superseded": arg("superseded"),
                         "no_rule_change": arg("norule") == "1"}
                return self._html(200, reviewui.amendments_page(
                    pend, done, friction, principal, branch, vorg,
                    token=reviewui.csrf_token("amendments", key),
                    flash=flash if flash["status"] else None))
            if path in ("/review/admin", "/review/admin/"):
                from . import simulator
                # 404, not 403: when the simulator is off it does not exist
                # as far as this application is concerned.
                if not simulator.enabled():
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such page</h1>"
                        "<p>Live generation is switched off.</p></div>"))
                return self._html(200, reviewui.admin_page(
                    svc.registry.organizations() or
                    [{"org_id": "", "name": "the default constitution"}],
                    simulator.status(), principal, branch, vorg,
                    token=reviewui.csrf_token("simulator", key)))
            if path in ("/review/rulebook", "/review/rulebook/"):
                rows, version, tname = self._rulebook(vorg)
                return self._html(200, reviewui.rulebook_page(
                    rows, version, tname, principal, branch, vorg))
            if path in ("/review/rulebook/history",
                        "/review/rulebook/history/"):
                return self._html(200, reviewui.rulebook_history_page(
                    self._rulebook_history(vorg), principal, branch, vorg))
            if path in ("/review/activity/judge",
                        "/review/activity/judge/"):
                jf = {"view": arg("view")}
                jrows, jstats, jnext = self._judge_activity(
                    vorg, jf.get("view"), arg("cursor"))
                return self._html(200, reviewui.judge_activity_page(
                    jrows, jstats, principal, branch, vorg, jf, jnext,
                    tenants))
            if path in ("/review/activity", "/review/activity/"):
                f = {"kind": arg("kind"), "q": arg("q"),
                     "tenant": arg("tenant"), "since": arg("since")}
                # A scoped principal's tenant always wins; the filter is a
                # convenience for someone who can already see everything.
                eff = vorg or (f["tenant"] if not scoped else None)
                rows, nxt = self._activity(f, eff, arg("cursor"))
                # The full tenant list is passed for NAMING even to a scoped
                # viewer — showing them "SC Control Tower" rather than a raw
                # key. `scoped` still governs whether a switcher is drawn, so
                # this reveals no tenant they could not already name.
                return self._html(200, reviewui.activity_page(
                    rows, self._activity_counts(eff),
                    svc.registry.organizations(), f, nxt,
                    principal, branch, vorg, scoped=scoped))
            if path in ("/review/analytics", "/review/analytics/"):
                return self._html(200, reviewui.analytics_page(
                    self._analytics(), principal, branch, vorg))
            if path in ("/review/impact", "/review/impact/"):
                return self._html(200, reviewui.impact_page(
                    self._impact(vorg), principal, branch, vorg,
                    scoped=scoped, tenants=tenants))
            if path in ("/review/ledger", "/review/ledger/"):
                status, prov = arg("status"), arg("provision")
                ats, aid = arg("ats"), arg("aid")
                cursor = (ats, aid) if ats and aid else None
                pageout = svc.ledger.register(
                    limit=self.LEDGER_PAGE, cursor=cursor,
                    status=status, provision=prov, org=vorg)
                return self._html(200, reviewui.ledger_page(
                    svc.ledger.census(prov, org=vorg), pageout["rows"],
                    principal, branch, status=status, provision=prov,
                    next_cursor=pageout["next"], org=vorg,
                    show_org=vorg is None))
            if m := re.fullmatch(r"/review/ledger/([\w-]+)", path):
                rec = svc.ledger.get(m.group(1))
                # A scoped principal is told the record does not exist rather
                # than that it exists and is forbidden: the second answer
                # leaks another tenant's ledger one probe at a time.
                if rec and vorg and rec.get("organization") != vorg:
                    rec = None
                if not rec:
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such record"
                        "</h1><p>Nothing in the ledger has that id.</p>"
                        "</div>"))
                return self._html(200, reviewui.record_page(
                    rec, svc.ledger.lifecycle(rec["id"]),
                    svc.ledger.judgments(rec["judgment_batch_id"]),
                    principal, branch, org=vorg,
                    may_promote=(branch == "lawmakers"
                                 and not rec["is_acceptance"]
                                 and rec.get("organization")),
                    token=reviewui.csrf_token(rec["id"], key)))
            if m := re.fullmatch(r"/review/([\w-]+)", path):
                task = svc.gateway.reviews.get(m.group(1))
                if task and vorg and task.get("organization") != vorg:
                    task = None
                if not task:
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such review"
                        "</h1><p>This task does not exist.</p></div>"))
                return self._html(200, reviewui.task_page(
                    task, principal,
                    reviewui.csrf_token(task["task_id"], key),
                    can_decide=self._holds_risk_owner(principal),
                    viewer_branch=branch))
            return self._html(404, reviewui.page(
                "Not found", "<div class='card'><h1>No such page</h1></div>"))

        def _review_post(self):
            if self.path in ("/review/live", "/review/live/"):
                import subprocess
                if not os.environ.get("ANTHROPIC_API_KEY"):
                    return self._html(409, reviewui.page(
                        "Not configured",
                        "<div class='card'><h1>No API key</h1><p>Set"
                        " ANTHROPIC_API_KEY in the server's environment and"
                        " restart. It cannot be supplied from this page.</p>"
                        "</div>"))
                if getattr(svc, "_live_switch", None):
                    return self._redirect("/review/login")
                root = os.path.dirname(os.path.dirname(
                    os.path.abspath(__file__)))
                # Detached: this rebuilds the demo and restarts the server,
                # so it must outlive the process that requested it.
                svc._live_switch = subprocess.Popen(
                    [sys.executable, os.path.join(root, "demo",
                                                  "run_live.py"),
                     "--company", os.environ.get("DJ_DEMO", "sctower"),
                     "--port", str(os.environ.get("DJ_PORT", "8080")),
                     "--db", os.environ.get("DJ_DB", "/tmp/dj.db")],
                    cwd=root, start_new_session=True,
                    stdout=open("/tmp/dj-live-switch.log", "w"),
                    stderr=subprocess.STDOUT)
                return self._redirect("/review/login")

            if self.path in ("/review/logout", "/review/logout/"):
                # Expire the cookie on the same path it was set, otherwise the
                # browser keeps the old one and "signing out" silently does
                # nothing. Nothing server-side is discarded: there is no
                # server session, and the ledger is untouched by signing out.
                self.send_response(200)
                self.send_header("set-cookie",
                                 f"{SESSION_COOKIE}=; Path=/; Max-Age=0;"
                                 " HttpOnly; SameSite=Lax")
                body = reviewui.signed_out_page().encode()
                self.send_header("content-type", "text/html; charset=utf-8")
                self.send_header("content-length", str(len(body)))
                self.send_header("x-content-type-options", "nosniff")
                self.end_headers()
                return self.wfile.write(body)

            if self.path in ("/review/login", "/review/login/"):
                form = self._form()
                key = (form.get("key") or "").strip()
                nxt = form.get("next") or "/review"
                if not svc.registry.authenticate(key):
                    return self._html(401, reviewui.login_page(
                        "That key does not belong to a known principal.", nxt,
                        roster=self._roster(),
                    live=self._live_state()))
                # Path=/review keeps the credential off the JSON API surface;
                # HttpOnly keeps it out of page scripts.
                return self._redirect(nxt, f"{SESSION_COOKIE}={key}; Path=/;"
                                           " HttpOnly; SameSite=Lax")

            if self.path in ("/review/admin/generate",):
                from . import simulator
                if not simulator.enabled():
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such page</h1>"
                        "</div>"))
                key, principal = self._viewer()
                if not principal:
                    return self._html(401, reviewui.login_page(
                        "Sign in first.", "/review/admin",
                    live=self._live_state()))
                form = self._form()
                if not reviewui.csrf_ok("simulator", key,
                                        form.get("csrf", "")):
                    return self._html(403, reviewui.page(
                        "Refused", "<div class='card'><h1>Stale form</h1>"
                        "<p>Reload the console and try again.</p></div>"))
                vorg = svc.registry.organization_of(principal)
                want = form.get("company") or None
                # A tenant-scoped principal may only generate into their own
                # ledger, whatever the form says.
                org = vorg or want
                tenants = svc.registry.organizations()
                try:
                    simulator.start(
                        svc, company=(org or "the default constitution"),
                        org=org if tenants else None,
                        n=int(form.get("n") or 25), challenger=principal)
                except (RuntimeError, ValueError) as e:
                    return self._html(409, reviewui.admin_page(
                        tenants or [{"org_id": "", "name": "default"}],
                        simulator.status(), principal,
                        svc.registry.resolve_branch(principal), vorg,
                        token=reviewui.csrf_token("simulator", key),
                        error=str(e)))
                return self._redirect("/review/admin")

            if m := re.fullmatch(
                    r"/review/change/([\w-]+)/(challenge|human-review)",
                    self.path):
                sid, lane = m.group(1), m.group(2)
                key, principal = self._viewer()
                if not principal:
                    return self._html(401, reviewui.login_page(
                        "Sign in first.", f"/review/change/{sid}",
                    live=self._live_state()))
                form = self._form()
                if not reviewui.csrf_ok(sid, key, form.get("csrf", "")):
                    return self._html(403, reviewui.page(
                        "Refused", "<div class='card'><h1>Stale form</h1>"
                        "<p>Reload the change and try again.</p></div>"))
                vorg = svc.registry.organization_of(principal)
                view = self._change_view(sid, vorg)
                if view is None:
                    return self._html(404, reviewui.page(
                        "Not found", "<div class='card'><h1>No such change"
                        "</h1></div>"))
                try:
                    # The Kernel decides whether this lane is open, not the
                    # screen. An absolute denial has no challenge lane, and
                    # the refusal comes from there in its own words.
                    if lane == "challenge":
                        svc.gateway.challenge(sid, principal,
                                              form.get("grounds", ""))
                    else:
                        svc.gateway.request_human_review(
                            sid, principal, form.get("grounds", ""))
                except (InboundError, KernelError) as e:
                    return self._html(e.status, reviewui.change_page(
                        view, principal,
                        svc.registry.resolve_branch(principal), vorg,
                        token=reviewui.csrf_token(sid, key), error=str(e)))
                return self._redirect(f"/review/change/{sid}")

            # Stage 3: ratify a tenant holding as platform law. Legislative,
            # never automatic — the Kernel re-checks the lawmakers branch.
            if m := re.fullmatch(r"/review/ledger/([\w-]+)/promote",
                                 self.path):
                key, principal = self._viewer()
                if not principal:
                    return self._html(401, reviewui.login_page(
                        "Sign in first.", f"/review/ledger/{m.group(1)}",
                    live=self._live_state()))
                if not reviewui.csrf_ok(m.group(1), key,
                                        self._form().get("csrf", "")):
                    return self._html(403, reviewui.page(
                        "Refused", "<div class='card'><h1>Stale form</h1>"
                        "</div>"))
                try:
                    svc.gate.promote(m.group(1), principal)
                except KernelError as e:
                    return self._html(e.status, reviewui.page(
                        "Refused", f"<div class='card'><h1>Not promoted</h1>"
                        f"<p>{reviewui._e(str(e))}</p><div class='actions'>"
                        f"<a class='open' href='/review/ledger/{m.group(1)}'>"
                        f"Back</a></div></div>"))
                return self._redirect(f"/review/ledger/{m.group(1)}")

            if m := re.fullmatch(r"/review/amendments/([\w-]+)/decide",
                                 self.path):
                key, principal = self._viewer()
                if not principal:
                    return self._html(401, reviewui.login_page(
                        "Sign in first.", "/review/amendments",
                    live=self._live_state()))
                form = self._form()
                if not reviewui.csrf_ok("amendments", key,
                                        form.get("csrf", "")):
                    return self._html(403, reviewui.page(
                        "Refused", "<div class='card'><h1>Stale form</h1>"
                        "<p>Reload and try again.</p></div>"))
                try:
                    # No branch check here: the Kernel does it. A screen that
                    # pre-authorised would become a second place authority
                    # lives, and there must only ever be one.
                    out = svc.constitution.decide_amendment(
                        m.group(1), form.get("decision", ""), principal)
                except KernelError as e:
                    return self._html(e.status, reviewui.page(
                        "Refused", f"<div class='card'><h1>Refused</h1>"
                        f"<p>{reviewui._e(str(e))}</p>"
                        f"<div class='actions'><a class='open'"
                        f" href='/review/amendments'>Back</a></div></div>"))
                # Carry the outcome through the redirect, so the page can say
                # what happened rather than returning a list that looks
                # identical to the one just submitted.
                return self._redirect(
                    f"/review/amendments?decided={m.group(1)}"
                    f"&outcome={out['status']}"
                    f"&superseded={out.get('superseded_records', 0)}"
                    f"&norule={'1' if out.get('no_rule_change') else '0'}")

            m = re.fullmatch(r"/review/([\w-]+)/decide", self.path)
            if not m:
                return self._html(404, reviewui.page(
                    "Not found", "<div class='card'><h1>No such page</h1></div>"))
            task_id = m.group(1)
            key, principal = self._viewer()
            if not principal:
                return self._html(401, reviewui.login_page(
                    "Sign in before deciding.", f"/review/{task_id}",
                    live=self._live_state()))

            form = self._form()
            # The token binds this form to this task AND this credential, so
            # a page rendered for one principal cannot be posted by another.
            if not reviewui.csrf_ok(task_id, key, form.get("csrf", "")):
                return self._html(403, reviewui.page(
                    "Refused", "<div class='card'><h1>Stale form</h1>"
                    "<p>Reload the review and submit it again.</p></div>"))

            task = svc.gateway.reviews.get(task_id)
            if not task:
                return self._html(404, reviewui.page(
                    "Not found", "<div class='card'><h1>No such review</h1>"
                    "</div>"))

            token = reviewui.csrf_token(task_id, key)
            try:
                svc.gateway.decide_review(
                    task_id, principal, form.get("decision", ""),
                    form.get("rationale", ""), form.get("expiry") or None)
            except (KernelError, InboundError) as e:
                # The refusal is rendered back onto the docket, with the
                # Kernel's own words. The screen never softens or reinterprets
                # a refusal it did not issue.
                return self._html(e.status, reviewui.task_page(
                    task, principal, token, str(e),
                    can_decide=self._holds_risk_owner(principal),
                    viewer_branch=svc.registry.resolve_branch(principal)))
            return self._redirect(f"/review/{task_id}")

        # -- dossier (§13.1: projection of stored fields only) ----------
        

        def _admin_status(self) -> dict:
            """Public operator snapshot — no secrets, no auth required.

            Includes process-local metrics and a soft scale envelope so
            operators can see when the single-container design is approaching
            its documented limits without needing an external monitoring stack.
            """
            try:
                from . import db as dbmod, metrics as metricsmod
                from .judges import THETA, MAX_CANDIDATES
                r = dbmod.open_reader()
                ver = None
                provisions = []
                try:
                    ver = svc.constitution.current_version()
                    provisions = svc.constitution.list_provisions(ver)
                except Exception:
                    pass
                precedent_count = r.execute(
                    "SELECT COUNT(*) AS c FROM precedent_record"
                ).fetchone()["c"]
                open_cases = r.execute(
                    "SELECT COUNT(*) AS c FROM case_state"
                    " WHERE status NOT IN ('final','denied_absolute')"
                ).fetchone()["c"]
                principal_count = r.execute(
                    "SELECT COUNT(*) AS c FROM principal"
                ).fetchone()["c"]
                # Soft envelope for the single-container deployment.
                # These are operator signals, not hard refusals.
                warnings = []
                if precedent_count >= 10_000:
                    warnings.append(
                        "precedent_count >= 10000: retrieve latency and "
                        "cache memory will grow; plan a backend migration")
                elif precedent_count >= 2_000:
                    warnings.append(
                        "precedent_count >= 2000: monitor retrieve metrics; "
                        "active-holdings cache is doing the heavy lifting")
                if open_cases >= 500:
                    warnings.append(
                        "open_cases >= 500: review queue pressure is high "
                        "for a single-process review UI")
                cache_stats = {}
                try:
                    cache_stats = svc.ledger.cache.stats()
                except Exception:
                    pass
                return {
                    "ok": True,
                    "db": os.environ.get("DJ_DB", "/data/judiciary.db"),
                    "judge_mode": os.environ.get("DJ_JUDGE_MODE", "oracle"),
                    "rulebook_version": ver,
                    "provisions": [
                        {"provision_id": p["provision_id"],
                         "absolute": bool(p.get("absolute")),
                         "text": (p.get("text") or "")[:80]}
                        for p in (provisions or [])
                    ],
                    "precedent_count": precedent_count,
                    "open_cases": open_cases,
                    "principal_count": principal_count,
                    "config": {
                        "theta": THETA,
                        "max_candidates": MAX_CANDIDATES,
                        "holdings_cache": os.environ.get(
                            "DJ_HOLDINGS_CACHE", "1") != "0",
                        "sqlite_cache_kib": int(os.environ.get(
                            "DJ_SQLITE_CACHE_KIB", "65536")),
                    },
                    "holdings_cache": cache_stats,
                    "metrics": metricsmod.snapshot(),
                    "scale_warnings": warnings,
                    "scale_envelope": {
                        "note": "single-container SQLite design; "
                                "comfortable below ~2k active holdings "
                                "and low concurrent review traffic",
                        "comfortable_precedents": 2000,
                        "plan_migration_precedents": 10000,
                    },
                    "enterprise": _ent_status(),
                }
            except Exception as e:
                return {"ok": False, "error": str(e)}

        def _dossier(self, record_id: str) -> dict:
            prov = svc.ledger.rebuild(record_id)
            rec = svc.ledger.get(record_id)
            return {
                "provenance": prov,
                "record": rec,
                "lifecycle": svc.ledger.lifecycle(record_id),
                "judgments": [
                    {k: j[k] for k in ("kind", "candidate_hash",
                                       "judge_version", "prompt_version",
                                       "verdict", "from_cache", "degraded")}
                    for j in svc.ledger.judgments(rec["judgment_batch_id"])],
            }

    return Handler


def _days_until(stamp: str | None) -> int | None:
    """Whole days from now until an ISO timestamp, or None."""
    if not stamp:
        return None
    from datetime import datetime, timezone
    try:
        d = datetime.fromisoformat(stamp)
    except ValueError:
        return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return (d - datetime.now(timezone.utc)).days


def serve(svc: Services, host: str = "0.0.0.0", port: int = 8080):
    httpd = ThreadingHTTPServer((host, port), make_handler(svc))
    return httpd
