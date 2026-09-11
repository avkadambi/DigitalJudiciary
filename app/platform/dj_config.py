"""Load ``config/dj.toml`` (or ``DJ_CONFIG``) and apply it to the process.

Uses stdlib ``tomllib`` only — no PyYAML, no extra packages.

Call ``load_and_apply()`` once at process start (serve.py / bootstrap).
Existing env vars always win over the file so Cloud Run secrets and local
overrides remain authoritative.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import tomllib
except ImportError:  # pragma: no cover
    tomllib = None  # type: ignore


_ROOT = Path(__file__).resolve().parents[2]
_LOADED: "DJFileConfig | None" = None


@dataclass
class TierJudgeConfig:
    provider: str = "anthropic"
    model: str = "claude-sonnet-4-6"
    api_key_env: str = "ANTHROPIC_API_KEY"
    api_key_env_fallback: str = "ANTHROPIC_API_KEY"
    api_key: str = ""          # discouraged; prefer env
    quorum: int = 3


@dataclass
class ConnectorConfig:
    type: str = "github"
    enabled: bool = True
    webhook_path: str = "/v1/inbound/github"
    check_name: str = "digital-judiciary"
    options: dict[str, Any] = field(default_factory=dict)


@dataclass
class DJFileConfig:
    profile: str = "demo"
    constitution_path: str | None = None
    store_path: str | None = None
    judges_mode: str = "oracle"
    tiers: dict[int, TierJudgeConfig] = field(default_factory=dict)
    connectors: list[ConnectorConfig] = field(default_factory=list)
    default_org: str | None = None
    repo_org_map: dict[str, str] = field(default_factory=dict)
    async_inbound: bool = False
    worker_threads: int = 1
    inbound_rate_per_s: float = 20.0
    host: str = "0.0.0.0"
    port: int = 8080
    gcp: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    def api_key_for_tier(self, tier: int) -> str:
        t = self.tiers.get(tier) or TierJudgeConfig()
        if t.api_key:
            return t.api_key
        for name in (t.api_key_env, t.api_key_env_fallback, "ANTHROPIC_API_KEY",
                     "OPENAI_API_KEY"):
            if name and os.environ.get(name):
                return os.environ[name]
        return ""

    def model_for_tier(self, tier: int) -> str:
        t = self.tiers.get(tier)
        if t and t.model:
            return t.model
        return os.environ.get(f"DJ_JUDGE_MODEL_T{tier}") or os.environ.get(
            "DJ_JUDGE_MODEL", "claude-sonnet-4-6")

    def provider_for_tier(self, tier: int) -> str:
        t = self.tiers.get(tier)
        return (t.provider if t else None) or os.environ.get(
            f"DJ_JUDGE_PROVIDER_T{tier}", "anthropic")

    def quorum_for_tier(self, tier: int) -> int:
        t = self.tiers.get(tier)
        if t:
            return max(1, int(t.quorum))
        return 3


def _config_path() -> Path | None:
    explicit = os.environ.get("DJ_CONFIG", "").strip()
    if explicit:
        p = Path(explicit)
        return p if p.is_file() else None
    for candidate in (
        _ROOT / "config" / "dj.toml",
        _ROOT / "dj.toml",
        Path("/config/dj.toml"),
        Path("/data/dj.toml"),
    ):
        if candidate.is_file():
            return candidate
    return None


def _parse_tier(data: dict | None, default_model: str) -> TierJudgeConfig:
    data = data or {}
    return TierJudgeConfig(
        provider=str(data.get("provider") or "anthropic"),
        model=str(data.get("model") or default_model),
        api_key_env=str(data.get("api_key_env") or "ANTHROPIC_API_KEY"),
        api_key_env_fallback=str(
            data.get("api_key_env_fallback") or "ANTHROPIC_API_KEY"),
        api_key=str(data.get("api_key") or ""),
        quorum=int(data.get("quorum") or 3),
    )


def load_file_config(path: Path | None = None) -> DJFileConfig:
    path = path or _config_path()
    if path is None or tomllib is None:
        return DJFileConfig()
    with open(path, "rb") as f:
        raw = tomllib.load(f)

    judges = raw.get("judges") or {}
    mode = str(judges.get("mode") or "oracle")
    tiers = {
        1: _parse_tier(judges.get("tier1"), "claude-haiku-4-5-20251001"),
        2: _parse_tier(judges.get("tier2"), "claude-sonnet-4-6"),
        3: _parse_tier(judges.get("tier3"), "claude-opus-4-6"),
    }

    connectors: list[ConnectorConfig] = []
    for c in raw.get("connectors") or []:
        if not isinstance(c, dict):
            continue
        options = {k: v for k, v in c.items()
                   if k not in ("type", "enabled", "webhook_path", "check_name")}
        connectors.append(ConnectorConfig(
            type=str(c.get("type") or "github"),
            enabled=bool(c.get("enabled", True)),
            webhook_path=str(c.get("webhook_path") or "/v1/inbound/github"),
            check_name=str(c.get("check_name") or "digital-judiciary"),
            options=options,
        ))

    constitution = raw.get("constitution") or {}
    tenancy = raw.get("tenancy") or {}
    runtime = raw.get("runtime") or {}
    project = raw.get("project") or {}

    repo_map = tenancy.get("repo_org_map") or {}
    if isinstance(repo_map, dict):
        repo_map = {str(k): str(v) for k, v in repo_map.items()}
    else:
        repo_map = {}

    return DJFileConfig(
        profile=str(project.get("profile") or raw.get("profile") or "demo"),
        constitution_path=(str(constitution["path"])
                           if constitution.get("path") else None),
        store_path=(str(constitution["store_path"])
                    if constitution.get("store_path") else None),
        judges_mode=mode,
        tiers=tiers,
        connectors=connectors,
        default_org=(str(tenancy["default_org"])
                     if tenancy.get("default_org") else None),
        repo_org_map=repo_map,
        async_inbound=bool(runtime.get("async_inbound", False)),
        worker_threads=int(runtime.get("worker_threads") or 1),
        inbound_rate_per_s=float(runtime.get("inbound_rate_per_s") or 20),
        host=str(runtime.get("host") or "0.0.0.0"),
        port=int(runtime.get("port") or 8080),
        gcp=dict(raw.get("gcp") or {}),
        raw=raw,
    )


def apply_to_env(cfg: DJFileConfig) -> None:
    """Set env only where the operator has not already set a value."""
    def setdefault(key: str, value: str | None) -> None:
        if value is None or value == "":
            return
        os.environ.setdefault(key, str(value))

    setdefault("DJ_PROFILE", cfg.profile)
    setdefault("DJ_JUDGE_MODE", cfg.judges_mode)
    setdefault("DJ_HOST", cfg.host)
    setdefault("DJ_PORT", str(cfg.port))
    setdefault("DJ_ASYNC_INBOUND", "1" if cfg.async_inbound else "0")
    setdefault("DJ_WORKER_THREADS", str(cfg.worker_threads))
    setdefault("DJ_INBOUND_RATE_PER_S", str(cfg.inbound_rate_per_s))
    if cfg.default_org:
        setdefault("DJ_DEFAULT_ORG", cfg.default_org)
    if cfg.repo_org_map:
        setdefault("DJ_REPO_ORG_MAP", json.dumps(cfg.repo_org_map))

    for tier, tc in cfg.tiers.items():
        setdefault(f"DJ_JUDGE_MODEL_T{tier}", tc.model)
        setdefault(f"DJ_JUDGE_PROVIDER_T{tier}", tc.provider)
        setdefault(f"DJ_QUORUM_T{tier}", str(tc.quorum))
        # Inline api_key only allowed for demo/selfhost; enterprise/gcp must use env.
        if tc.api_key and tc.api_key_env and cfg.profile not in ("enterprise", "gcp"):
            setdefault(tc.api_key_env, tc.api_key)

    for c in cfg.connectors:
        if c.type == "github" and c.enabled:
            setdefault("DJ_CHECK_NAME", c.check_name)
            secret_env = c.options.get("webhook_secret_env")
            if secret_env:
                # just documents the expected env; value comes from secrets
                pass

    if cfg.constitution_path:
        # Resolve relative to repo root
        p = Path(cfg.constitution_path)
        if not p.is_absolute():
            p = _ROOT / p
        if p.is_file():
            # Point seed dir parent logic: if path is .../rulebook.json,
            # SEED_DIR becomes its parent when store is sibling
            setdefault("DJ_CONSTITUTION_PATH", str(p))
            setdefault("DJ_SEED_DIR", str(p.parent))




class ConfigError(RuntimeError):
    """Fatal configuration problem — process should exit before serving."""


def validate_for_boot(cfg: DJFileConfig | None = None) -> DJFileConfig:
    """Fail fast for enterprise pilot rules.

    * profile enterprise|gcp: reject inline api_key in toml
    * judges.mode=llm: every tier 1–3 must resolve a non-empty key
    """
    cfg = cfg or get_config()
    errors: list[str] = []

    enterpriseish = cfg.profile in ("enterprise", "gcp")
    if enterpriseish:
        for tier, tc in cfg.tiers.items():
            if tc.api_key:
                errors.append(
                    f"judges.tier{tier}: inline api_key is forbidden when "
                    f"profile={cfg.profile!r}; set api_key_env and inject the "
                    f"secret via the environment (e.g. GCP Secret Manager)")

    mode = os.environ.get("DJ_JUDGE_MODE", cfg.judges_mode or "oracle").lower()
    if mode == "llm":
        for tier in (1, 2, 3):
            key = cfg.api_key_for_tier(tier)
            # api_key_for_tier still returns inline for demo; for enterprise
            # inline is already rejected above, so env must supply the key.
            if not key:
                tc = cfg.tiers.get(tier) or TierJudgeConfig()
                errors.append(
                    f"DJ_JUDGE_MODE=llm but no API key for tier {tier} "
                    f"(set env {tc.api_key_env!r} or ANTHROPIC_API_KEY)")

    if errors:
        msg = "Digital Judiciary config validation failed:\n  - " + "\n  - ".join(errors)
        raise ConfigError(msg)
    return cfg

def load_and_apply() -> DJFileConfig:
    global _LOADED
    if _LOADED is not None:
        return _LOADED
    cfg = load_file_config()
    apply_to_env(cfg)
    _LOADED = cfg
    # Env wins after apply_to_env (setdefault leaves pre-set DJ_JUDGE_MODE).
    mode = os.environ.get("DJ_JUDGE_MODE", cfg.judges_mode or "oracle").lower()
    profile = os.environ.get("DJ_PROFILE", cfg.profile or "demo").lower()
    force = os.environ.get("DJ_VALIDATE_CONFIG", "0") == "1"
    if force or mode == "llm" or profile in ("enterprise", "gcp"):
        # Keep cfg.profile in sync for validate_for_boot enterprise checks
        if profile in ("enterprise", "gcp"):
            cfg.profile = profile
        cfg.judges_mode = mode
        validate_for_boot(cfg)
    return cfg


def get_config() -> DJFileConfig:
    return _LOADED or load_and_apply()


def public_view(cfg: DJFileConfig | None = None) -> dict[str, Any]:
    """Safe for /v1/admin/status — never includes API keys."""
    cfg = cfg or get_config()
    return {
        "profile": cfg.profile,
        "judges_mode": cfg.judges_mode,
        "tiers": {
            str(t): {
                "provider": tc.provider,
                "model": tc.model,
                "api_key_env": tc.api_key_env,
                "key_present": bool(cfg.api_key_for_tier(t)),
                "quorum": tc.quorum,
            }
            for t, tc in cfg.tiers.items()
        },
        "connectors": [
            {"type": c.type, "enabled": c.enabled,
             "webhook_path": c.webhook_path}
            for c in cfg.connectors
        ],
        "constitution_path": cfg.constitution_path,
        "gcp_project": (cfg.gcp or {}).get("project_id"),
    }
