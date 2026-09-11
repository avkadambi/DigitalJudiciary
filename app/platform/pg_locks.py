"""PostgreSQL advisory locks — multi-process sole-writer coordination.

Why this exists
---------------
The Challenge Gate is the logical sole writer of precedent. In a single
SQLite process that is physical (one writer connection). On Postgres with
many adjudication workers, you still want **at most one admit at a time
per tenant** (or globally) without serialising the entire HTTP plane.

Postgres advisory locks are integer locks maintained by the server, outside
row data. They are ideal for:

  * Gate admit serialisation (``gate:global`` or ``gate:<org>``)
  * Per-tenant critical sections
  * Leader election for lifecycle sweeps

Two flavours
------------
  * **Transaction-scoped** (``pg_advisory_xact_lock``) — released at COMMIT
    or ROLLBACK. Preferred for short Gate admits.
  * **Session-scoped** (``pg_advisory_lock``) — held until unlock or
    disconnect. Use for longer critical sections; always unlock in
    ``finally``.

Requires ``DJ_DATABASE_URL=postgres://...`` and ``psycopg``.

Example (transaction lock around an admit)::

    from app.platform.pg_locks import advisory_xact, lock_key

    with advisory_xact(lock_key("gate", org or "global")) as conn:
        # run admit using the same connection if desired, or just hold
        # the lock while the SQLite/legacy Gate runs:
        record_id = gate.admit(artifact)

Example (session lock)::

    from app.platform.pg_locks import advisory_session, lock_key

    with advisory_session(lock_key("lifecycle", "sweep")):
        lifecycle.sweep_once()
"""
from __future__ import annotations

import hashlib
import os
from contextlib import contextmanager
from typing import Generator, Iterator


def lock_key(*parts: str) -> int:
    """Map an arbitrary string namespace to a signed 64-bit advisory lock id.

    Postgres advisory locks take one ``bigint`` or two ``int``s. We use a
    stable SHA-256 prefix so ``gate:acme`` always hashes the same across
    workers and deploys.
    """
    material = ":".join(parts).encode("utf-8")
    digest = hashlib.sha256(material).digest()
    # signed int64 range
    n = int.from_bytes(digest[:8], "big", signed=False)
    if n >= (1 << 63):
        n -= (1 << 64)
    return n


def _connect():
    url = os.environ.get("DJ_DATABASE_URL", "")
    if not url.startswith("postgres"):
        raise RuntimeError(
            "pg advisory locks require DJ_DATABASE_URL=postgres://...")
    try:
        import psycopg
    except ImportError as e:
        raise RuntimeError(
            "psycopg required for advisory locks: "
            "pip install 'psycopg[binary]>=3.1'"
        ) from e
    return psycopg.connect(url)


@contextmanager
def advisory_xact(key: int, shared: bool = False) -> Iterator:
    """Hold a **transaction-scoped** advisory lock until the ``with`` block ends.

    The lock is taken with ``pg_advisory_xact_lock`` and released automatically
    on commit/rollback when the connection closes at the end of the block.

    Parameters
    ----------
    key:
        From :func:`lock_key`.
    shared:
        If True, use the shared variant (multiple holders; blocks exclusive).
    """
    conn = _connect()
    try:
        conn.autocommit = False
        with conn.cursor() as cur:
            fn = ("pg_advisory_xact_lock_shared" if shared
                  else "pg_advisory_xact_lock")
            cur.execute(f"SELECT {fn}(%s)", (key,))
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


@contextmanager
def advisory_session(key: int, shared: bool = False) -> Iterator:
    """Hold a **session-scoped** advisory lock; always unlocked in ``finally``."""
    conn = _connect()
    locked = False
    try:
        conn.autocommit = True
        with conn.cursor() as cur:
            fn = ("pg_advisory_lock_shared" if shared
                  else "pg_advisory_lock")
            cur.execute(f"SELECT {fn}(%s)", (key,))
            locked = True
        yield conn
    finally:
        if locked:
            try:
                with conn.cursor() as cur:
                    ufn = ("pg_advisory_unlock_shared" if shared
                           else "pg_advisory_unlock")
                    cur.execute(f"SELECT {ufn}(%s)", (key,))
            except Exception:
                pass
        conn.close()


@contextmanager
def try_advisory_xact(key: int) -> Generator[bool, None, None]:
    """Non-blocking attempt. Yields True if the lock was acquired.

    Useful for "only one lifecycle sweep across replicas" patterns::

        with try_advisory_xact(lock_key("lifecycle", "sweep")) as got:
            if not got:
                return  # another replica is sweeping
            lifecycle.sweep_once()
    """
    conn = _connect()
    got = False
    try:
        conn.autocommit = False
        with conn.cursor() as cur:
            cur.execute("SELECT pg_try_advisory_xact_lock(%s)", (key,))
            row = cur.fetchone()
            got = bool(row[0] if not isinstance(row, dict) else list(row.values())[0])
        yield got
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def gate_lock_key(organization: str | None = None) -> int:
    """Convenience: exclusive key for Challenge Gate admits."""
    return lock_key("dj", "gate", organization or "global")


def with_gate_lock(organization: str | None, fn, *args, **kwargs):
    """Run ``fn(*args, **kwargs)`` under a transaction advisory lock.

    No-op (runs ``fn`` directly) when ``DJ_DATABASE_URL`` is not Postgres,
    so the SQLite demo path stays unchanged.
    """
    url = os.environ.get("DJ_DATABASE_URL", "")
    if not url.startswith("postgres"):
        return fn(*args, **kwargs)
    with advisory_xact(gate_lock_key(organization)):
        return fn(*args, **kwargs)
