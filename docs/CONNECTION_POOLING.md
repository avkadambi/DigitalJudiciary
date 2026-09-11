# Connection pool best practices (PostgreSQL)

Applies when `DJ_DATABASE_URL=postgres://...` is set (job queue + advisory locks).
The SQLite demo path does not use a pool.

## Goals

1. Safe multi-worker `FOR UPDATE SKIP LOCKED` job claims  
2. Safe Gate coordination via **transaction** advisory locks  
3. No lock or session-state leaks under PgBouncer / Cloud SQL  

## Do

| Practice | Why |
|----------|-----|
| Prefer **short-lived connections** per claim/finish (current `PostgresJobQueue`) | No shared session state between jobs |
| Use **`pg_advisory_xact_lock`** (`with_gate_lock`, `advisory_xact`) | Released at COMMIT/ROLLBACK; pool-safe |
| Hold connections only for DB work — never across LLM HTTP calls | Avoids pool exhaustion and idle-in-transaction |
| Size `max_connections` ≥ Σ client pools + admin headroom | Prevents `too many connections` |
| Set `DJ_JOB_VISIBILITY_S` > worst-case job duration | Crash recovery without stuck `running` rows |
| Use **transaction** pooling in PgBouncer | Matches how DJ uses the database |

## Don't

| Anti-pattern | Consequence |
|--------------|-------------|
| `pg_advisory_lock` (session) under transaction pooling | Lock held on backend; next client inherits or blocks forever |
| Checkout a connection, call Anthropic/OpenAI, then query | Pool starvation; timeouts cascade |
| One global long-lived connection for all workers | Serialization bottleneck; single point of failure |
| `SELECT pg_advisory_lock(id) FROM t LIMIT n` | Unbounded locks if LIMIT applies late |
| Point workers at a **read replica** for claims | SKIP LOCKED must run on primary |

## PgBouncer

```ini
pool_mode = transaction
server_reset_query = DISCARD ALL
```

With `pool_mode = transaction`:

- Safe: row locks, `SKIP LOCKED`, `pg_advisory_xact_lock*`
- Unsafe: session advisory locks, temp tables, session GUCs that must stick

Generate the same snippet from Python:

```python
from app.platform.pg_pool_practices import pgbouncer_ini_snippet
print(pgbouncer_ini_snippet())
```

## Sizing

```python
from app.platform.pg_pool_practices import recommended_pool_size
print(recommended_pool_size(worker_threads=4, instances=3))
# suggested_pool_max_per_instance, suggested_postgres_max_connections_floor
```

Rough guide:

```text
pool_max_per_instance ≈ DJ_WORKER_THREADS * 2
postgres max_connections ≥ pool_max * instances + 10
```

## Cloud Run

- Each instance has its own pool; multiply by `max_instances`
- Scale-to-zero drops in-memory state; durability is the **job_queue** table
- Use Cloud SQL Auth Proxy or connector; set `DJ_DATABASE_URL` accordingly
- Prefer xact advisory locks only

See `app.platform.pg_pool_practices.cloud_run_notes()`.

## Checklist

```python
from app.platform.pg_pool_practices import POOL_CHECKLIST
print(POOL_CHECKLIST)
```

## Related code

| Module | Role |
|--------|------|
| `app/platform/queue.py` | Postgres job claim — short connections |
| `app/platform/pg_locks.py` | Xact advisory locks by default |
| `app/platform/pg_pool_practices.py` | Sizing helpers + guidance |
| `examples/pg_advisory_locks_example.py` | Lock behaviour demo |

## Explicit locking (reference)

Postgres docs: [Explicit Locking — Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html).
