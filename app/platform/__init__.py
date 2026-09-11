"""Platform layer: everything that is *not* the Judiciary Kernel.

The Kernel (adjudication, Challenge Gate, ledger, axioms) lives in
``app.kernel`` / ``app.adjudicate`` / ``app.db`` and must remain small and
formally constrained.

This package holds the concerns that scale with popularity:

* configuration
* storage backend selection (SQLite demo vs Postgres-ready interface)
* durable job queue
* multi-tenant installation registry
* VCS connectors (GitHub first; interface for GitLab / Azure DevOps / …)
* background workers

Demo path (``python3 serve.py`` + SQLite) uses the same Kernel through
this layer — it does not bypass it.
"""

from .config import PlatformConfig, load_config

__all__ = ["PlatformConfig", "load_config"]

# pg_locks is imported on demand (requires psycopg + DJ_DATABASE_URL)
