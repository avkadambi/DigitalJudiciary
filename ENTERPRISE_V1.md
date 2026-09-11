# Digital Judiciary — Enterprise Version 1 (Pilot)

**Status:** pilot / self-host ready  
**Not:** multi-tenant SaaS GA for every CI/CD org

## What EV1 includes

| Capability | Notes |
|------------|--------|
| Formal Kernel | Gate, axioms A1–A7, Def. 7, floor-first; conformance suites |
| Demo path | `python3 serve.py` + SQLite, zero pip installs |
| Pre-merge GitHub | Webhook → adjudicate → check run / comments / review UI |
| Config file | `config/dj.toml` — per-tier model + `api_key_env` |
| Constitution | Path in config or `POST /v1/admin/constitution` |
| Async jobs | SQLite queue, or Postgres `FOR UPDATE SKIP LOCKED` |
| Advisory locks | Optional Postgres helpers for multi-worker Gate coordination |
| Outbound retry | Failed check/comment deliveries reaped periodically |
| GCP sketch | `deploy/gcp/` Cloud Build + Cloud Run |
| Connector registry | GitHub implemented; GitLab/Azure stubs |

## Explicit non-goals for EV1

| Deferred | Reason |
|----------|--------|
| Full Kernel ledger on Postgres | **Available opt-in** via `DJ_LEDGER_BACKEND=postgres` (SQLite still default) |
| OIDC / SAML | API keys for pilot; SSO later |
| Hard RLS / DB-per-tenant | Soft `organization` scoping |
| GitLab / Azure DevOps connectors | Registry stubs only |
| Multi-region active-active Gate | Single-region pilot |

## Profiles

| `DJ_PROFILE` / config | Intent |
|----------------------|--------|
| `demo` | Oracle judges, SQLite, local review UI |
| `selfhost` | Async workers, still one container |
| `enterprise` / `gcp` | Fail-fast config; **no inline API keys** in toml |

## Boot validation

When `DJ_JUDGE_MODE=llm` or profile is `enterprise`/`gcp`:

* Missing tier 1–3 API keys → **process exits** with `ConfigError`
* Inline `api_key` in toml under enterprise/gcp → **rejected**

Override: `DJ_VALIDATE_CONFIG=1` forces validation even in demo.

## Operator entrypoints

```bash
# Demo
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=off python3 serve.py

# Smoke
./scripts/smoke_enterprise.sh

# Outbound retry (also runs in-process every DJ_OUTBOUND_RETRY_S)
curl -X POST -H "Authorization: Bearer $KEY" http://127.0.0.1:8080/v1/admin/outbound-retry
```

## Support boundary

EV1 is intended for design partners and single-tenant self-host. Production
at “every company embeds this in CI/CD” requires later phases (Postgres ledger,
SSO, hard tenancy) described in `ARCHITECTURE.md`.
