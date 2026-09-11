"""Typed platform configuration from environment.

Defaults preserve the original demo path: SQLite, in-process work, oracle
judge, no external services required.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field


@dataclass
class PlatformConfig:
    # Core
    db_path: str = "/data/judiciary.db"
    host: str = "0.0.0.0"
    port: int = 8080
    judge_mode: str = "oracle"          # oracle | llm
    base_url: str = "http://localhost:8080"

    # Scale / SQLite tuning
    theta: float = 0.25
    max_candidates: int = 25
    holdings_cache: bool = True
    sqlite_cache_kib: int = 65536

    # Inbound plane
    async_inbound: bool = False
    inbound_rate_per_s: float = 20.0
    inbound_burst: int = 40
    github_allow_unsigned: bool = False
    github_webhook_secret: str = ""
    check_name: str = "digital-judiciary"

    # Tenancy
    default_org: str | None = None
    repo_org_map: dict = field(default_factory=dict)

    # Feature flags for platform maturity
    profile: str = "demo"               # demo | selfhost | enterprise


def load_config() -> PlatformConfig:
    raw_map = os.environ.get("DJ_REPO_ORG_MAP", "") or "{}"
    try:
        repo_map = json.loads(raw_map)
        if not isinstance(repo_map, dict):
            repo_map = {}
    except json.JSONDecodeError:
        repo_map = {}

    profile = os.environ.get("DJ_PROFILE", "demo").lower()
    # Self-host / enterprise profiles default async on unless explicitly off
    async_default = "1" if profile in ("selfhost", "enterprise") else "0"

    return PlatformConfig(
        db_path=os.environ.get("DJ_DB", "/data/judiciary.db"),
        host=os.environ.get("DJ_HOST", "0.0.0.0"),
        port=int(os.environ.get("DJ_PORT", "8080")),
        judge_mode=os.environ.get("DJ_JUDGE_MODE", "oracle"),
        base_url=os.environ.get(
            "DJ_BASE_URL",
            f"http://localhost:{os.environ.get('DJ_PORT', '8080')}"),
        theta=float(os.environ.get("DJ_THETA", "0.25")),
        max_candidates=int(os.environ.get("DJ_MAX_CANDIDATES", "25")),
        holdings_cache=os.environ.get("DJ_HOLDINGS_CACHE", "1") != "0",
        sqlite_cache_kib=int(os.environ.get("DJ_SQLITE_CACHE_KIB", "65536")),
        async_inbound=os.environ.get(
            "DJ_ASYNC_INBOUND", async_default) == "1",
        inbound_rate_per_s=float(
            os.environ.get("DJ_INBOUND_RATE_PER_S", "20")),
        inbound_burst=int(os.environ.get("DJ_INBOUND_BURST", "40")),
        github_allow_unsigned=os.environ.get(
            "DJ_GITHUB_ALLOW_UNSIGNED", "0") == "1",
        github_webhook_secret=os.environ.get("DJ_GITHUB_WEBHOOK_SECRET", ""),
        check_name=os.environ.get("DJ_CHECK_NAME", "digital-judiciary"),
        default_org=os.environ.get("DJ_DEFAULT_ORG") or None,
        repo_org_map=repo_map,
        profile=profile,
    )
