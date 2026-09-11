"""GitHub App / token resolution for outbound check runs and comments.

Zero pip dependencies. Token resolution order:

1. DJ_GITHUB_TOKEN — classic PAT or fine-grained token (demo / simple deploy)
2. DJ_GITHUB_INSTALLATION_TOKEN — pre-minted installation token (operator-rotated)
3. GitHub App JWT → installation access token when
   DJ_GITHUB_APP_ID + DJ_GITHUB_APP_INSTALLATION_ID + DJ_GITHUB_APP_KEY_PATH
   are set. JWT is signed with openssl(1) so the container stays dependency-free.

Inbound webhook verification remains HMAC (X-Hub-Signature-256) as today;
GitHub Apps use the same header with the App's webhook secret
(DJ_GITHUB_WEBHOOK_SECRET).
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import time
import urllib.error
import urllib.request

GITHUB_API = os.environ.get("DJ_GITHUB_API", "https://api.github.com")

_cached_token: str | None = None
_cached_until: float = 0.0


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _app_jwt(app_id: str, key_path: str) -> str:
    """RS256 JWT for GitHub App authentication (max 10 minutes)."""
    now = int(time.time())
    header = _b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    payload = _b64url(json.dumps({
        "iat": now - 60,
        "exp": now + 9 * 60,
        "iss": app_id,
    }).encode())
    signing_input = f"{header}.{payload}".encode()
    try:
        sig = subprocess.check_output(
            ["openssl", "dgst", "-sha256", "-sign", key_path],
            input=signing_input, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError) as e:
        raise RuntimeError(
            f"GitHub App JWT signing failed (is openssl available and "
            f"DJ_GITHUB_APP_KEY_PATH readable?): {e}") from e
    return f"{header}.{payload}.{_b64url(sig)}"


def _installation_token(app_id: str, installation_id: str,
                        key_path: str) -> tuple[str, float]:
    jwt = _app_jwt(app_id, key_path)
    url = f"{GITHUB_API}/app/installations/{installation_id}/access_tokens"
    req = urllib.request.Request(
        url, data=b"{}", method="POST",
        headers={
            "authorization": f"Bearer {jwt}",
            "accept": "application/vnd.github+json",
            "x-github-api-version": "2022-11-28",
            "content-type": "application/json",
        })
    timeout = float(os.environ.get("DJ_GITHUB_TIMEOUT_S", "15"))
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read())
    token = body["token"]
    # GitHub returns expires_at; keep a 60s safety margin.
    expires = body.get("expires_at")
    if expires:
        # 2026-07-25T12:00:00Z
        from datetime import datetime
        exp = datetime.fromisoformat(expires.replace("Z", "+00:00")).timestamp()
        until = exp - 60
    else:
        until = time.time() + 50 * 60
    return token, until


def resolve_token(force: bool = False) -> str:
    """Return a bearer token for GitHub API calls, or '' if none configured."""
    global _cached_token, _cached_until
    static = os.environ.get("DJ_GITHUB_TOKEN", "") or \
        os.environ.get("DJ_GITHUB_INSTALLATION_TOKEN", "")
    if static:
        return static

    app_id = os.environ.get("DJ_GITHUB_APP_ID", "")
    inst = os.environ.get("DJ_GITHUB_APP_INSTALLATION_ID", "")
    key = os.environ.get("DJ_GITHUB_APP_KEY_PATH", "")
    if not (app_id and inst and key):
        return ""

    now = time.time()
    if not force and _cached_token and now < _cached_until:
        return _cached_token
    try:
        token, until = _installation_token(app_id, inst, key)
        _cached_token, _cached_until = token, until
        return token
    except (urllib.error.URLError, RuntimeError, KeyError, ValueError):
        return _cached_token or ""


def configured() -> dict:
    return {
        "pat_or_static": bool(os.environ.get("DJ_GITHUB_TOKEN") or
                              os.environ.get("DJ_GITHUB_INSTALLATION_TOKEN")),
        "app": bool(os.environ.get("DJ_GITHUB_APP_ID") and
                    os.environ.get("DJ_GITHUB_APP_INSTALLATION_ID") and
                    os.environ.get("DJ_GITHUB_APP_KEY_PATH")),
        "webhook_secret_set": bool(os.environ.get("DJ_GITHUB_WEBHOOK_SECRET")),
        "check_name": os.environ.get("DJ_CHECK_NAME", "digital-judiciary"),
        "async_inbound": os.environ.get("DJ_ASYNC_INBOUND", "0") == "1",
    }
