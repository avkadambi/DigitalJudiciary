"""Storage backend boundary.

Demo path: SQLite via ``app.db``.
Enterprise queue path: Postgres when ``DJ_DATABASE_URL`` is set (psycopg).

The full Kernel ledger on Postgres is a separate migration; today the URL
primarily drives the durable job queue (``platform.queue``). This module
still exposes a connection helper for future ledger adapters.
"""
from __future__ import annotations

import os
from typing import Protocol, runtime_checkable

from .. import db as sqlite_db


@runtime_checkable
class StorageBackend(Protocol):
    name: str

    def init(self) -> None: ...
    def open_writer(self): ...
    def open_reader(self): ...
    def path(self) -> str: ...


class SQLiteBackend:
    name = "sqlite"

    def __init__(self, path: str | None = None):
        self._path = path or os.environ.get("DJ_DB", "/data/judiciary.db")

    def init(self) -> None:
        sqlite_db.init_db(self._path)

    def open_writer(self):
        return sqlite_db.open_writer(self._path)

    def open_reader(self):
        return sqlite_db.open_reader(self._path)

    def path(self) -> str:
        return self._path


class PostgresBackend:
    """Postgres connection helper (optional dependency: psycopg).

    Used by the job queue today. Raising at init keeps the zero-dep demo
    image honest when someone sets DJ_DATABASE_URL without installing the driver.
    """

    name = "postgres"

    def __init__(self, url: str):
        self._url = url

    def _connect(self):
        try:
            import psycopg
            from psycopg.rows import dict_row
        except ImportError as e:
            raise RuntimeError(
                "DJ_DATABASE_URL is set but psycopg is not installed.\n"
                "  pip install 'psycopg[binary]>=3.1'\n"
                "Or unset DJ_DATABASE_URL to use the SQLite demo path."
            ) from e
        return psycopg.connect(self._url, row_factory=dict_row)

    def init(self) -> None:
        # Job schema is owned by platform.queue; probe connectivity only.
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
            conn.commit()

    def open_writer(self):
        return self._connect()

    def open_reader(self):
        return self._connect()

    def path(self) -> str:
        return self._url


def open_backend(path: str | None = None) -> StorageBackend:
    url = os.environ.get("DJ_DATABASE_URL", "")
    if url.startswith("postgres"):
        return PostgresBackend(url)
    return SQLiteBackend(path)
