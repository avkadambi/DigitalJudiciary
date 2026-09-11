# Architecture — Digital Judiciary (enterprise / open-source target)

## Two layers

```
┌──────────────────────────────────────────────────────────────┐
│  PLATFORM                                                    │
│  connectors · tenancy · jobs · workers · config · HTTP edge  │
└────────────────────────────┬─────────────────────────────────┘
                             │ neutral ChangeRequest / Kernel API
┌────────────────────────────▼─────────────────────────────────┐
│  KERNEL                                                      │
│  Challenge Gate · ledger · adjudicate · axioms · constitution│
└──────────────────────────────────────────────────────────────┘
```

**Kernel** is the product: formal governance. It does not import GitHub types.

**Platform** is what scales when every company embeds DJ in CI/CD: webhooks,
queues, tenant registry, workers, deploy profiles.

## Demo path (must always work)

```bash
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=off python3 serve.py
# or with the full demo corpus (default):
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 python3 serve.py
```

- Storage: **SQLite** (`app.db` + `platform.storage.SQLiteBackend`)
- Queue: SQLite `job_queue` (idle unless `DJ_ASYNC_INBOUND=1`)
- Profile: `DJ_PROFILE=demo` (default)
- Zero pip installs; single process; single container

## Profiles

| Profile | Env | Intent |
|---------|-----|--------|
| `demo` | `DJ_PROFILE=demo` | SQLite, sync inbound, oracle judge, local review UI |
| `selfhost` | `DJ_PROFILE=selfhost` | Same binary; async inbound default; multi-worker optional |
| `enterprise` | `DJ_PROFILE=enterprise` | Same + expect GitHub App, repo map, rate limits |

Postgres is a **documented seam** (`DJ_DATABASE_URL=postgres://…` →
`platform.storage.PostgresBackend`). The zero-dep image does not ship a
Postgres driver; production self-host can add an adapter without rewriting
the Kernel.

## Connectors

```
platform.connectors.base.Connector
    └── GitHubConnector   (HMAC verify → ChangeRequest)
    └── (future) GitLabConnector, AzureDevOpsConnector, …
```

Inbound HTTP still accepts `/v1/inbound/github` and runs the existing
`PRGateway` (idempotent, floor-first, check runs). The connector package is
the extension point for additional VCS systems.

## Tenancy

Trusted resolution only:

1. `tenant_repo` / `tenant_installation` tables (App installs)
2. `DJ_REPO_ORG_MAP` JSON
3. `DJ_DEFAULT_ORG`

Register installs:

```http
POST /v1/admin/installations/register
{"installation_id":"123","organization":"acme","repos":["acme/api"]}
```

## Workers

`platform.workers.WorkerPlane` starts `DJ_WORKER_THREADS` (default 1) job
workers. Jobs call the same gateway paths as sync HTTP — Gate remains the
sole ledger writer.

## What stayed inviolable

- Challenge Gate sole admit path  
- A1–A7, Def. 7, floor-first (A6)  
- Outbound recorded before network  
- Powerless inbound principal  
- Rulebook + factor-map pinning  

## Scale roadmap (not all in this tree)

| Phase | Capability |
|-------|------------|
| Done (this tree) | Kernel/platform split, connector interface, tenancy registry, job workers, profiles, SQLite demo |
| Next | Postgres adapter package, OIDC for `/review`, multi-install GitHub App token cache |
| Later | Horizontal connector replicas, read replicas, per-tenant quotas, GitLab connector |

## Layout

```
app/
  kernel.py adjudicate.py db.py …     # KERNEL
  inbound_github.py outbound.py …     # gateway (uses kernel)
  platform/
    config.py storage.py tenancy.py workers.py
    connectors/base.py connectors/github.py
serve.py                              # demo + self-host entry
docker-compose.yml                    # single container
ARCHITECTURE.md                       # this file
```


## Config file (`config/dj.toml`)

See `config/dj.example.toml`. Loaded via `DJ_CONFIG` or default paths.
Sets per-tier judge **model**, **provider** (anthropic|openai), and **api_key_env**.

## GCP

See `deploy/gcp/README.md` and `deploy/gcp/deploy.sh`.


## Job queue (SKIP LOCKED)

| Mode | Backend | How |
|------|---------|-----|
| Demo | SQLite | `BEGIN IMMEDIATE` + conditional UPDATE |
| Enterprise | Postgres | `FOR UPDATE SKIP LOCKED` via `DJ_DATABASE_URL` |

```bash
# Demo (default)
unset DJ_DATABASE_URL
python3 serve.py

# Postgres queue (ledger still SQLite in this phase)
pip install -r requirements-postgres.txt
export DJ_DATABASE_URL=postgres://dj:dj@localhost:5432/judiciary
export DJ_ASYNC_INBOUND=1 DJ_WORKER_THREADS=4
python3 serve.py

# Compose
docker compose -f docker-compose.yml -f docker-compose.postgres.yml up --build
```

Stale running jobs are reclaimed after `DJ_JOB_VISIBILITY_S` (default 300s).


## Postgres advisory locks

Module: `app/platform/pg_locks.py`  
Example: `examples/pg_advisory_locks_example.py`

Use **transaction-scoped** locks (`pg_advisory_xact_lock`) around Gate admits
when multiple workers share one Postgres-backed deployment:

```python
from app.platform.pg_locks import with_gate_lock

record_id = with_gate_lock(organization, gate.admit, artifact)
```

On SQLite / unset `DJ_DATABASE_URL`, `with_gate_lock` is a no-op so the demo
path is unchanged.

| Helper | Postgres function | Use |
|--------|-------------------|-----|
| `advisory_xact` | `pg_advisory_xact_lock` | Short critical sections (admit) |
| `advisory_session` | `pg_advisory_lock` | Longer sections; unlock in finally |
| `try_advisory_xact` | `pg_try_advisory_xact_lock` | Leader election (lifecycle sweep) |
| `gate_lock_key(org)` | — | Stable key for `gate:<org\|global>` |


## Connection pooling

Operator guide: [`docs/CONNECTION_POOLING.md`](docs/CONNECTION_POOLING.md)

Code: `app/platform/pg_pool_practices.py`

**Summary:** short connections for job claim; **transaction** advisory locks only;
never hold a pool connection across LLM calls; PgBouncer `pool_mode = transaction`.


## Postgres Kernel ledger

| Env | Effect |
|-----|--------|
| (default) | Ledger on SQLite (`DJ_DB`) |
| `DJ_DATABASE_URL=postgres://…` | Job queue on Postgres only |
| `DJ_LEDGER_BACKEND=postgres` + URL | **Ledger + jobs** on Postgres |

Implementation: `app/platform/pg_ledger.py` (DDL, immutability triggers, `?`→`%s` wrapper).
