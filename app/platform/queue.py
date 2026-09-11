"""Durable job queue — SQLite (demo) or Postgres SKIP LOCKED (enterprise).

Selection:
  * ``DJ_DATABASE_URL=postgres://...`` → Postgres backend (requires
    ``psycopg`` — see requirements-postgres.txt). Multiple workers across
    processes claim jobs safely with ``FOR UPDATE SKIP LOCKED``.
  * otherwise → SQLite backend in the same file as the ledger (demo path).

The Kernel never talks to this module; only the platform worker plane does.

Pool guidance: ``docs/CONNECTION_POOLING.md`` and ``app.platform.pg_pool_practices``.
"""
from __future__ import annotations

import json
import os
import threading
import time
import uuid
from typing import Protocol, runtime_checkable

from .. import db, metrics
from ..db import now_iso

# How long a "running" job may sit before another worker may reclaim it
# (process crash / OOM / scale-to-zero mid-job).
DEFAULT_VISIBILITY_S = int(os.environ.get("DJ_JOB_VISIBILITY_S", "300"))

SCHEMA_SQLITE = """
CREATE TABLE IF NOT EXISTS job_queue (
  job_id        TEXT PRIMARY KEY,
  kind          TEXT NOT NULL,
  payload       TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'pending'
                CHECK (status IN ('pending','running','done','failed')),
  attempts      INTEGER NOT NULL DEFAULT 0,
  last_error    TEXT,
  created_at    TEXT NOT NULL,
  updated_at    TEXT NOT NULL,
  locked_at     TEXT
);
CREATE INDEX IF NOT EXISTS jq_status ON job_queue (status, created_at);
"""

SCHEMA_POSTGRES = """
CREATE TABLE IF NOT EXISTS job_queue (
  job_id        TEXT PRIMARY KEY,
  kind          TEXT NOT NULL,
  payload       TEXT NOT NULL,
  status        TEXT NOT NULL DEFAULT 'pending'
                CHECK (status IN ('pending','running','done','failed')),
  attempts      INTEGER NOT NULL DEFAULT 0,
  last_error    TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  locked_at     TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS jq_status ON job_queue (status, created_at);
"""


@runtime_checkable
class JobQueue(Protocol):
    name: str

    def ensure_schema(self) -> None: ...
    def enqueue(self, kind: str, payload: dict) -> str: ...
    def claim(self) -> dict | None: ...
    def finish(self, job_id: str, ok: bool, error: str | None = None) -> None: ...
    def pending_count(self) -> int: ...
    def reclaim_stale(self, older_than_s: int = DEFAULT_VISIBILITY_S) -> int: ...


# ---------------------------------------------------------------------------
# SQLite
# ---------------------------------------------------------------------------
class SQLiteJobQueue:
    name = "sqlite"

    def __init__(self, path: str | None = None):
        self.path = path

    def ensure_schema(self) -> None:
        w = db.open_writer(self.path)
        try:
            w.executescript(SCHEMA_SQLITE)
            w.commit()
        finally:
            w.close()

    def enqueue(self, kind: str, payload: dict) -> str:
        job_id = f"JOB-{uuid.uuid4().hex[:12]}"
        w = db.open_writer(self.path)
        try:
            w.execute(
                "INSERT INTO job_queue (job_id, kind, payload, status, attempts,"
                " created_at, updated_at) VALUES (?,?,?,'pending',0,?,?)",
                (job_id, kind, json.dumps(payload), now_iso(), now_iso()))
            w.commit()
        finally:
            w.close()
        metrics.inc("jobs_enqueued")
        return job_id

    def claim(self) -> dict | None:
        """Claim one pending job. SQLite has no SKIP LOCKED; we use a
        write-lock transaction and a conditional UPDATE so concurrent
        threads in one process still serialise correctly."""
        self.reclaim_stale()
        w = db.open_writer(self.path)
        try:
            w.execute("BEGIN IMMEDIATE")
            row = w.execute(
                "SELECT * FROM job_queue WHERE status='pending'"
                " ORDER BY created_at LIMIT 1").fetchone()
            if not row:
                w.rollback()
                return None
            w.execute(
                "UPDATE job_queue SET status='running', attempts=attempts+1,"
                " locked_at=?, updated_at=? WHERE job_id=? AND status='pending'",
                (now_iso(), now_iso(), row["job_id"]))
            if w.total_changes == 0:
                w.rollback()
                return None
            w.commit()
            d = dict(row)
            d["payload"] = json.loads(d["payload"])
            d["status"] = "running"
            return d
        except Exception:
            try:
                w.rollback()
            except Exception:
                pass
            raise
        finally:
            w.close()

    def finish(self, job_id: str, ok: bool, error: str | None = None) -> None:
        w = db.open_writer(self.path)
        try:
            w.execute(
                "UPDATE job_queue SET status=?, last_error=?, updated_at=?,"
                " locked_at=NULL WHERE job_id=?",
                ("done" if ok else "failed", (error or "")[:2000],
                 now_iso(), job_id))
            w.commit()
        finally:
            w.close()
        metrics.inc("jobs_done" if ok else "jobs_failed")

    def pending_count(self) -> int:
        r = db.open_reader(self.path)
        try:
            return r.execute(
                "SELECT COUNT(*) AS c FROM job_queue WHERE status='pending'"
            ).fetchone()["c"]
        finally:
            r.close()

    def reclaim_stale(self, older_than_s: int = DEFAULT_VISIBILITY_S) -> int:
        """Return running jobs whose lock is older than visibility timeout."""
        w = db.open_writer(self.path)
        try:
            # ISO timestamps compare lexicographically when formatted uniformly
            rows = w.execute(
                "SELECT job_id, locked_at FROM job_queue WHERE status='running'"
            ).fetchall()
            n = 0
            cutoff = time.time() - older_than_s
            for row in rows:
                locked = row["locked_at"] or ""
                try:
                    # 2026-07-26T12:00:00.000000+00:00
                    from datetime import datetime
                    ts = datetime.fromisoformat(locked.replace("Z", "+00:00")).timestamp()
                except Exception:
                    ts = 0
                if ts and ts < cutoff:
                    w.execute(
                        "UPDATE job_queue SET status='pending', locked_at=NULL,"
                        " updated_at=?, last_error=? WHERE job_id=? AND status='running'",
                        (now_iso(), "reclaimed: visibility timeout", row["job_id"]))
                    n += 1
            if n:
                w.commit()
                metrics.inc("jobs_reclaimed", n)
            return n
        finally:
            w.close()


# ---------------------------------------------------------------------------
# Postgres
# ---------------------------------------------------------------------------
class PostgresJobQueue:
    """Multi-worker safe queue using ``FOR UPDATE SKIP LOCKED``."""

    name = "postgres"

    def __init__(self, url: str | None = None):
        self.url = url or os.environ.get("DJ_DATABASE_URL", "")
        if not self.url:
            raise RuntimeError("PostgresJobQueue requires DJ_DATABASE_URL")
        self._lock = threading.Lock()

    def _connect(self):
        try:
            import psycopg
            from psycopg.rows import dict_row
        except ImportError as e:
            raise RuntimeError(
                "Postgres queue requires psycopg. Install with:\n"
                "  pip install 'psycopg[binary]>=3.1'\n"
                "Or use the SQLite demo path (unset DJ_DATABASE_URL)."
            ) from e
        conn = psycopg.connect(self.url, row_factory=dict_row)
        conn.autocommit = False
        return conn

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(SCHEMA_POSTGRES)
            conn.commit()

    def enqueue(self, kind: str, payload: dict) -> str:
        job_id = f"JOB-{uuid.uuid4().hex[:12]}"
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO job_queue (job_id, kind, payload, status, attempts)"
                    " VALUES (%s, %s, %s, 'pending', 0)",
                    (job_id, kind, json.dumps(payload)))
            conn.commit()
        metrics.inc("jobs_enqueued")
        return job_id

    def claim(self) -> dict | None:
        """Atomically claim one pending row; concurrent workers skip locked rows."""
        self.reclaim_stale()
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE job_queue
                    SET status = 'running',
                        attempts = attempts + 1,
                        locked_at = NOW(),
                        updated_at = NOW()
                    WHERE job_id = (
                        SELECT job_id FROM job_queue
                        WHERE status = 'pending'
                        ORDER BY created_at
                        FOR UPDATE SKIP LOCKED
                        LIMIT 1
                    )
                    RETURNING job_id, kind, payload, status, attempts,
                              last_error, created_at, updated_at, locked_at
                    """
                )
                row = cur.fetchone()
            conn.commit()
        if not row:
            return None
        d = dict(row)
        payload = d.get("payload")
        if isinstance(payload, str):
            d["payload"] = json.loads(payload)
        elif payload is None:
            d["payload"] = {}
        # Normalise timestamps to iso strings for callers
        for k in ("created_at", "updated_at", "locked_at"):
            if d.get(k) is not None and hasattr(d[k], "isoformat"):
                d[k] = d[k].isoformat()
        return d

    def finish(self, job_id: str, ok: bool, error: str | None = None) -> None:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE job_queue SET status=%s, last_error=%s,"
                    " updated_at=NOW(), locked_at=NULL WHERE job_id=%s",
                    ("done" if ok else "failed", (error or "")[:2000], job_id))
            conn.commit()
        metrics.inc("jobs_done" if ok else "jobs_failed")

    def pending_count(self) -> int:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT COUNT(*) AS c FROM job_queue WHERE status='pending'")
                row = cur.fetchone()
            conn.commit()
        return int(row["c"] if row else 0)

    def reclaim_stale(self, older_than_s: int = DEFAULT_VISIBILITY_S) -> int:
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE job_queue
                    SET status = 'pending',
                        locked_at = NULL,
                        updated_at = NOW(),
                        last_error = 'reclaimed: visibility timeout'
                    WHERE status = 'running'
                      AND locked_at < NOW() - (%s * INTERVAL '1 second')
                    """,
                    (older_than_s,))
                n = cur.rowcount
            conn.commit()
        if n:
            metrics.inc("jobs_reclaimed", n)
        return n


def open_queue(path: str | None = None) -> JobQueue:
    """Factory: Postgres when DJ_DATABASE_URL is postgres*, else SQLite."""
    url = os.environ.get("DJ_DATABASE_URL", "")
    if url.startswith("postgres"):
        return PostgresJobQueue(url)
    return SQLiteJobQueue(path)
