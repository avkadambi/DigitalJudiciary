"""Tenant / installation registry.

Trusted mapping from external systems (GitHub App installation, repo full
name) to an internal ``organization`` id. Never taken from an unverified
webhook body alone — connectors resolve tenant via this registry after
signature verification.
"""
from __future__ import annotations

import json
import os
from typing import Any

from .. import db
from ..db import now_iso

SCHEMA_TENANCY = """
CREATE TABLE IF NOT EXISTS tenant_installation (
  installation_id   TEXT PRIMARY KEY,
  provider          TEXT NOT NULL DEFAULT 'github',
  organization      TEXT,
  account_login     TEXT,
  external_org_id   TEXT,
  repos_json        TEXT NOT NULL DEFAULT '[]',
  factor_map_version TEXT,
  status            TEXT NOT NULL DEFAULT 'active'
                    CHECK (status IN ('active','suspended','removed')),
  created_at        TEXT NOT NULL,
  updated_at        TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ti_org ON tenant_installation (organization);
CREATE INDEX IF NOT EXISTS ti_provider ON tenant_installation (provider, status);

CREATE TABLE IF NOT EXISTS tenant_repo (
  repo_full_name    TEXT PRIMARY KEY,
  organization      TEXT,
  installation_id   TEXT,
  provider          TEXT NOT NULL DEFAULT 'github',
  created_at        TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS tr_org ON tenant_repo (organization);
"""


def ensure_schema(path: str | None = None) -> None:
    w = db.open_writer(path)
    try:
        w.executescript(SCHEMA_TENANCY)
        w.commit()
    finally:
        w.close()


def upsert_installation(
    installation_id: str,
    *,
    provider: str = "github",
    organization: str | None = None,
    account_login: str | None = None,
    external_org_id: str | None = None,
    repos: list[str] | None = None,
    path: str | None = None,
) -> None:
    ensure_schema(path)
    now = now_iso()
    w = db.open_writer(path)
    try:
        existing = w.execute(
            "SELECT installation_id FROM tenant_installation WHERE installation_id=?",
            (installation_id,)).fetchone()
        repos_json = json.dumps(sorted(set(repos or [])))
        if existing:
            w.execute(
                "UPDATE tenant_installation SET organization=COALESCE(?,organization),"
                " account_login=COALESCE(?,account_login),"
                " external_org_id=COALESCE(?,external_org_id),"
                " repos_json=?, status='active', updated_at=? WHERE installation_id=?",
                (organization, account_login, external_org_id, repos_json,
                 now, installation_id))
        else:
            w.execute(
                "INSERT INTO tenant_installation (installation_id, provider,"
                " organization, account_login, external_org_id, repos_json,"
                " status, created_at, updated_at) VALUES (?,?,?,?,?,?,'active',?,?)",
                (installation_id, provider, organization, account_login,
                 external_org_id, repos_json, now, now))
        for repo in (repos or []):
            w.execute(
                "INSERT INTO tenant_repo (repo_full_name, organization,"
                " installation_id, provider, created_at) VALUES (?,?,?,?,?)"
                " ON CONFLICT(repo_full_name) DO UPDATE SET"
                " organization=excluded.organization,"
                " installation_id=excluded.installation_id",
                (repo, organization, installation_id, provider, now))
        w.commit()
    finally:
        w.close()


def resolve_org_for_repo(repo_full_name: str, path: str | None = None) -> str | None:
    """Trusted resolution order:

    1. tenant_repo table (installation registry)
    2. DJ_REPO_ORG_MAP env JSON (deploy config)
    3. DJ_DEFAULT_ORG
    """
    ensure_schema(path)
    r = db.open_reader(path)
    try:
        row = r.execute(
            "SELECT organization FROM tenant_repo WHERE repo_full_name=?",
            (repo_full_name,)).fetchone()
        if row and row["organization"]:
            return row["organization"]
    finally:
        r.close()

    raw = os.environ.get("DJ_REPO_ORG_MAP", "") or "{}"
    try:
        mapping = json.loads(raw)
    except json.JSONDecodeError:
        mapping = {}
    if repo_full_name in mapping:
        return mapping[repo_full_name]
    if "/" in repo_full_name:
        owner = repo_full_name.split("/", 1)[0]
        wild = f"{owner}/*"
        if wild in mapping:
            return mapping[wild]
    return os.environ.get("DJ_DEFAULT_ORG") or None


def list_installations(path: str | None = None) -> list[dict[str, Any]]:
    ensure_schema(path)
    r = db.open_reader(path)
    try:
        rows = r.execute(
            "SELECT * FROM tenant_installation ORDER BY created_at DESC"
        ).fetchall()
        out = []
        for row in rows:
            d = dict(row)
            try:
                d["repos"] = json.loads(d.pop("repos_json") or "[]")
            except json.JSONDecodeError:
                d["repos"] = []
            out.append(d)
        return out
    finally:
        r.close()
