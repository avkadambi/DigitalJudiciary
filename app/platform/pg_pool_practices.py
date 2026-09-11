"""PostgreSQL connection-pool best practices for Digital Judiciary.

This module is documentation-as-code: helpers that encode safe patterns when
``DJ_DATABASE_URL`` is used behind PgBouncer, Cloud SQL Auth Proxy, or an
in-process pool (psycopg_pool).

Why pools matter here
---------------------
* Job workers open short connections for ``FOR UPDATE SKIP LOCKED``.
* Advisory locks may run on the same database.
* Cloud Run / multi-instance deploys multiply backends quickly.

Rules of thumb
--------------
1. **Prefer transaction-scoped advisory locks** (``pg_advisory_xact_lock``).
   Session locks (``pg_advisory_lock``) stick to the *backend process*. A
   pool will hand that backend to the next borrower → leaked or stolen locks.

2. **Never hold a pool connection across await / HTTP / LLM calls.**
   Checkout → query → commit/rollback → return. Nothing else in between.

3. **Use transaction-mode pooling when possible** (PgBouncer
   ``pool_mode = transaction``). Session features (temp tables, prepared
   statements without DEALLOCATE, session advisory locks) break in that mode.

4. **Size for workers, not for peak HTTP.**
   Rough formula for DJ job workers::

       pool_max ≈ DJ_WORKER_THREADS * instances * 2
       server Postgres max_connections ≥ pool_max * services + headroom

5. **Reset session state on checkout** if you must use session pooling::

       SELECT pg_advisory_unlock_all();
       DISCARD ALL;   -- or pool server_reset_query

6. **Health-check with a cheap query** (``SELECT 1``), not with a lock.

7. **Idempotency still wins.** Even with perfect pooling, GitHub redelivers;
   ``delivery_id`` uniqueness remains the correctness backstop.

See also
--------
* ``app.platform.pg_locks`` — xact locks by default
* ``app.platform.queue.PostgresJobQueue`` — short-lived connections per claim
* ``docs/CONNECTION_POOLING.md`` — operator checklist
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator


# Recommended defaults (operators may override via env)
DEFAULT_POOL_MIN = int(os.environ.get("DJ_PG_POOL_MIN", "1"))
DEFAULT_POOL_MAX = int(os.environ.get("DJ_PG_POOL_MAX", "10"))
DEFAULT_POOL_TIMEOUT_S = float(os.environ.get("DJ_PG_POOL_TIMEOUT_S", "30"))


POOL_CHECKLIST = """
PostgreSQL connection pool checklist (Digital Judiciary)
========================================================

[ ] DJ_DATABASE_URL points at the *primary* (writers need it for SKIP LOCKED)
[ ] Pool mode is transaction (PgBouncer) OR app uses short-lived connections
[ ] No session-level advisory locks under a transaction pool
[ ] Gate coordination uses pg_advisory_xact_lock / with_gate_lock only
[ ] Connections are not held across LLM judge HTTP calls
[ ] server_reset_query / DISCARD ALL configured if session pooling is forced
[ ] max_connections on Postgres > sum of all client pools + admin headroom
[ ] Cloud Run: min instances * workers sized so lock wait ≠ request timeout
[ ] Job visibility timeout (DJ_JOB_VISIBILITY_S) > max claim work duration
[ ] Metrics: pool wait time, lock wait time, jobs_reclaimed
"""


def recommended_pool_size(
    worker_threads: int | None = None,
    instances: int | None = None,
) -> dict[str, int]:
    """Suggest client pool max for DJ job workers (not a hard limit)."""
    workers = worker_threads or int(os.environ.get("DJ_WORKER_THREADS", "2"))
    inst = instances or int(os.environ.get("DJ_INSTANCES", "1"))
    # Each worker may hold 1 job-queue conn; leave headroom for status/admin.
    per_instance = max(2, workers * 2)
    return {
        "worker_threads": workers,
        "instances": inst,
        "suggested_pool_max_per_instance": per_instance,
        "suggested_postgres_max_connections_floor": per_instance * inst + 10,
    }


def pool_safe_advisory_lock_guidance() -> dict[str, str]:
    """Map lock APIs to pool safety."""
    return {
        "pg_advisory_xact_lock": "SAFE with transaction pooling — released at COMMIT/ROLLBACK",
        "pg_try_advisory_xact_lock": "SAFE with transaction pooling",
        "pg_advisory_lock": "UNSAFE with transaction pooling — use only with session pooling + unlock",
        "pg_advisory_unlock_all": "Use on checkout when repairing a session-pooled backend",
        "FOR UPDATE SKIP LOCKED": "SAFE — row locks, transaction scoped; preferred for job claim",
    }


@contextmanager
def short_connection(url: str | None = None) -> Iterator[Any]:
    """Open a single connection, always close — the pattern PostgresJobQueue uses.

    Prefer this over a long-lived connection when holding advisory xact locks
    or claiming jobs. A process-wide pool is optional; correctness does not
    require one if each operation is short.
    """
    url = url or os.environ.get("DJ_DATABASE_URL", "")
    if not url.startswith("postgres"):
        raise RuntimeError("short_connection requires DJ_DATABASE_URL=postgres://...")
    try:
        import psycopg
    except ImportError as e:
        raise RuntimeError("pip install 'psycopg[binary]>=3.1'") from e
    conn = psycopg.connect(url)
    try:
        yield conn
        if not conn.closed and conn.info.transaction_status != 0:
            # INTRANS / INERROR — ensure we do not return a dirty session
            try:
                conn.rollback()
            except Exception:
                pass
    finally:
        conn.close()


def pgbouncer_ini_snippet() -> str:
    """Example PgBouncer settings compatible with DJ's Postgres usage."""
    return """\
; pgbouncer.ini — transaction pooling for Digital Judiciary job workers
[databases]
judiciary = host=127.0.0.1 port=5432 dbname=judiciary user=dj

[pgbouncer]
pool_mode = transaction
default_pool_size = 20
max_client_conn = 200
server_reset_query = DISCARD ALL
; Do NOT use session-level advisory locks with pool_mode=transaction
ignore_startup_parameters = extra_float_digits
"""


def cloud_run_notes() -> str:
    return """\
Cloud Run + Postgres pooling
----------------------------
* Each instance is a separate client: pool_max is per instance.
* Scale-to-zero drops session state; durable work must be in the queue table.
* Point DJ_DATABASE_URL at Cloud SQL via Auth Proxy or connector.
* Prefer Cloud SQL max_connections sized for max_instances * pool_max.
* Advisory xact locks are released when the request/worker transaction ends;
  do not rely on session locks across instance recycle.
"""
