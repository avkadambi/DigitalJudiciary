"""Generic JSON webhook connector — second plugin proving the registry.

Accepts a neutral ChangeRequest-shaped JSON body (or a thin envelope) after
optional shared-secret header check. Use this to integrate non-GitHub CI
without waiting on a first-class GitLab/Azure module.

Auth: header ``X-DJ-Webhook-Secret`` must match ``DJ_GENERIC_WEBHOOK_SECRET``
when that env is set. If unset, only ``DJ_GITHUB_ALLOW_UNSIGNED=1``-style
local demos should call it (still gated by that env for safety).
"""
from __future__ import annotations

import hmac
import json
import os
import uuid

from .. import tenancy
from .base import ChangeRequest, ConnectorResult


class GenericWebhookConnector:
    name = "generic"

    def __init__(self, path: str | None = None):
        self.path = path

    def accept(self, headers: dict[str, str], raw_body: bytes) -> ConnectorResult:
        headers = {k.lower(): v for k, v in headers.items()}
        secret = os.environ.get("DJ_GENERIC_WEBHOOK_SECRET", "")
        provided = headers.get("x-dj-webhook-secret", "")
        if secret:
            if not hmac.compare_digest(secret, provided):
                return ConnectorResult(
                    ok=False, error="bad generic webhook secret", status=401)
        elif os.environ.get("DJ_GITHUB_ALLOW_UNSIGNED", "0") != "1":
            return ConnectorResult(
                ok=False,
                error="set DJ_GENERIC_WEBHOOK_SECRET or "
                      "DJ_GITHUB_ALLOW_UNSIGNED=1 for local demo",
                status=503)

        try:
            body = json.loads(raw_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            return ConnectorResult(ok=False, error=f"bad json: {e}", status=400)

        # Allow either a flat ChangeRequest-like object or { "change": {...} }
        c = body.get("change") if isinstance(body.get("change"), dict) else body
        repo = str(c.get("repo") or "")
        delivery = str(
            c.get("delivery_id")
            or headers.get("x-dj-delivery")
            or f"gen-{uuid.uuid4().hex[:12]}")
        org = c.get("organization") or tenancy.resolve_org_for_repo(repo, self.path)

        change = ChangeRequest(
            provider="generic",
            delivery_id=delivery,
            event_type=str(c.get("event_type") or "change_request"),
            action=str(c.get("action") or "submit"),
            repo=repo,
            number=int(c.get("number") or 0),
            title=str(c.get("title") or ""),
            body=str(c.get("body") or ""),
            head_sha=str(c.get("head_sha") or ""),
            base_ref=str(c.get("base_ref") or "main"),
            author_login=str(c.get("author_login") or ""),
            labels=list(c.get("labels") or []),
            paths=list(c.get("paths") or []),
            checks=list(c.get("checks") or []),
            organization=org,
            raw_headers=dict(headers),
            raw_body=raw_body,
        )
        return ConnectorResult(ok=True, change=change, status=200)
