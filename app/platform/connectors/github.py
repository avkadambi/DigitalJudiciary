"""GitHub connector — verifies HMAC and normalizes to ChangeRequest.

Heavy lifting of adjudication remains in ``app.inbound_github.PRGateway``.
This connector only owns transport identity and neutral shape.
"""
from __future__ import annotations

import json
import os

from ...inbound_github import InboundError, verify_signature
from .. import tenancy
from .base import ChangeRequest, ConnectorResult


class GitHubConnector:
    name = "github"

    def __init__(self, path: str | None = None):
        self.path = path

    def accept(self, headers: dict[str, str], raw_body: bytes) -> ConnectorResult:
        headers = {k.lower(): v for k, v in headers.items()}
        try:
            verify_signature(raw_body, headers.get("x-hub-signature-256"))
        except InboundError as e:
            return ConnectorResult(
                ok=False, error=str(e), status=e.status)

        event = headers.get("x-github-event", "")
        delivery = headers.get("x-github-delivery") or ""
        if not delivery:
            return ConnectorResult(
                ok=False, error="missing X-GitHub-Delivery", status=400)

        try:
            body = json.loads(raw_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            return ConnectorResult(ok=False, error=f"bad json: {e}", status=400)

        # Ping / installation lifecycle — acknowledge without adjudicating
        if event in ("ping", "installation", "installation_repositories"):
            self._maybe_register_installation(body, event)
            return ConnectorResult(
                ok=True, ignore_reason=f"lifecycle:{event}", status=200)

        if event not in ("pull_request", "check_run", "issue_comment"):
            return ConnectorResult(
                ok=True, ignore_reason=f"unhandled event {event}", status=200)

        pr = body.get("pull_request") or {}
        if event == "check_run":
            pr = (body.get("check_run") or {}).get("pull_requests") or []
            pr = pr[0] if pr else {}
            # check_run actions are handled by gateway; pass through shape
        repo_obj = body.get("repository") or {}
        repo = repo_obj.get("full_name") or ""
        if not repo and pr:
            repo = (pr.get("base") or {}).get("repo", {}).get("full_name") or ""

        number = int(pr.get("number") or body.get("number") or 0)
        head = pr.get("head") or {}
        base = pr.get("base") or {}
        user = pr.get("user") or body.get("sender") or {}
        labels = []
        for lab in pr.get("labels") or []:
            if isinstance(lab, dict):
                labels.append(lab.get("name") or "")
            else:
                labels.append(str(lab))

        org = tenancy.resolve_org_for_repo(repo, path=self.path)
        installation = body.get("installation") or {}
        inst_id = str(installation.get("id") or "") or None
        if inst_id and org:
            tenancy.upsert_installation(
                inst_id, organization=org,
                account_login=(installation.get("account") or {}).get("login"),
                repos=[repo] if repo else None,
                path=self.path)

        change = ChangeRequest(
            provider="github",
            delivery_id=delivery,
            event_type=event,
            action=str(body.get("action") or "submit"),
            repo=repo,
            number=number,
            title=pr.get("title") or "",
            body=pr.get("body") or "",
            head_sha=(head.get("sha") or ""),
            base_ref=(base.get("ref") or "main"),
            author_login=user.get("login") or "",
            labels=[x for x in labels if x],
            organization=org,
            installation_id=inst_id,
            raw_headers={
                "x-github-event": event,
                "x-github-delivery": delivery,
                "x-hub-signature-256": headers.get("x-hub-signature-256", ""),
            },
            raw_body=raw_body,
        )
        return ConnectorResult(ok=True, change=change, status=200)

    def _maybe_register_installation(self, body: dict, event: str) -> None:
        inst = body.get("installation") or {}
        inst_id = str(inst.get("id") or "")
        if not inst_id:
            return
        account = inst.get("account") or {}
        repos = []
        for r in body.get("repositories") or body.get("repositories_added") or []:
            name = r.get("full_name")
            if name:
                repos.append(name)
        # Organization from env map on account login if present
        login = account.get("login") or ""
        org = None
        if login:
            org = tenancy.resolve_org_for_repo(f"{login}/_", path=self.path)
            if org is None:
                org = os.environ.get("DJ_DEFAULT_ORG")
        tenancy.upsert_installation(
            inst_id,
            account_login=login,
            external_org_id=str(account.get("id") or "") or None,
            organization=org,
            repos=repos,
            path=self.path,
        )
