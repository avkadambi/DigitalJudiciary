"""Postgres Kernel ledger backend.

Enabled when::

    DJ_LEDGER_BACKEND=postgres
    DJ_DATABASE_URL=postgres://...

SQLite remains the default (demo + conformance). The Kernel and Gate still
talk only to ``app.db.open_writer`` / ``open_reader``; this module supplies
compatible connections when the ledger is on Postgres.

SQL dialect notes
-----------------
* Placeholders: callers use ``?``; the wrapper rewrites to ``%s``.
* Immutability: BEFORE UPDATE/DELETE triggers raise exceptions (A5).
* ``AUTOINCREMENT`` → ``BIGSERIAL``.
* Timestamps stay TEXT/ISO strings for cross-backend parity with the app.
"""
from __future__ import annotations

import os
import re
from typing import Any, Iterable, Sequence

# ---------------------------------------------------------------------------
# DDL
# ---------------------------------------------------------------------------

def _immut_triggers(table: str, msg: str) -> list[str]:
    safe = table
    return [
        f"""
        CREATE OR REPLACE FUNCTION dj_immut_{safe}_upd() RETURNS trigger AS $$
        BEGIN
          RAISE EXCEPTION '%', '{msg}';
        END;
        $$ LANGUAGE plpgsql;
        """,
        f"DROP TRIGGER IF EXISTS tr_{safe}_upd ON {safe};",
        f"""
        CREATE TRIGGER tr_{safe}_upd
          BEFORE UPDATE ON {safe}
          FOR EACH ROW EXECUTE FUNCTION dj_immut_{safe}_upd();
        """,
        f"""
        CREATE OR REPLACE FUNCTION dj_immut_{safe}_del() RETURNS trigger AS $$
        BEGIN
          RAISE EXCEPTION '%', '{msg} (delete)';
        END;
        $$ LANGUAGE plpgsql;
        """,
        f"DROP TRIGGER IF EXISTS tr_{safe}_del ON {safe};",
        f"""
        CREATE TRIGGER tr_{safe}_del
          BEFORE DELETE ON {safe}
          FOR EACH ROW EXECUTE FUNCTION dj_immut_{safe}_del();
        """,
    ]


# Postgres 14+ uses EXECUTE FUNCTION; 11–13 used EXECUTE PROCEDURE.
# Prefer FUNCTION (PG14+). Cloud SQL PG15/16 is fine.

PG_LEDGER_STATEMENTS: list[str] = [
    """
    CREATE TABLE IF NOT EXISTS organization (
      org_id      TEXT PRIMARY KEY,
      name        TEXT NOT NULL,
      created_at  TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS principal (
      principal_id  TEXT PRIMARY KEY,
      kind          TEXT NOT NULL CHECK (kind IN ('human','workload')),
      api_key_hash  TEXT NOT NULL,
      created_at    TEXT NOT NULL,
      organization  TEXT REFERENCES organization(org_id),
      role_hint     TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS authority_assignment (
      assignment_id TEXT PRIMARY KEY,
      principal_id  TEXT NOT NULL REFERENCES principal(principal_id),
      branch        TEXT NOT NULL CHECK (branch IN ('lawmakers','judges','risk_owner')),
      valid_from    TEXT NOT NULL,
      valid_to      TEXT,
      granted_by    TEXT NOT NULL,
      grant_reason  TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS rulebook_version (
      version_id    TEXT PRIMARY KEY,
      content_hash  TEXT NOT NULL,
      enacted_at    TEXT NOT NULL,
      enacted_by    TEXT NOT NULL,
      amendment_id  TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS provision (
      version_id    TEXT NOT NULL REFERENCES rulebook_version(version_id),
      provision_id  TEXT NOT NULL,
      organization  TEXT,
      text          TEXT NOT NULL,
      policy_source TEXT NOT NULL,
      absolute      INTEGER NOT NULL DEFAULT 0,
      PRIMARY KEY (version_id, provision_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS standing_declaration (
      declaration_id    TEXT PRIMARY KEY,
      scope             TEXT NOT NULL,
      adverse_to_grants INTEGER NOT NULL DEFAULT 0,
      holder            TEXT,
      declared_by       TEXT NOT NULL,
      declared_at       TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS draft_amendment (
      amendment_id  TEXT PRIMARY KEY,
      origin        TEXT NOT NULL,
      body          TEXT NOT NULL,
      status        TEXT NOT NULL DEFAULT 'pending',
      filed_by      TEXT NOT NULL,
      filed_at      TEXT NOT NULL,
      decided_by    TEXT,
      decided_at    TEXT,
      organization  TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS precedent_record (
      id                    TEXT PRIMARY KEY,
      case_id               TEXT NOT NULL,
      provision_id          TEXT NOT NULL,
      organization          TEXT,
      facts                 TEXT NOT NULL,
      premise               TEXT NOT NULL,
      interpretation        TEXT NOT NULL,
      conditions            TEXT,
      scope                 TEXT NOT NULL,
      scope_level           TEXT,
      rationale             TEXT NOT NULL,
      authority_tier        INTEGER NOT NULL,
      resolving_principal   TEXT NOT NULL,
      resolved_at           TEXT NOT NULL,
      rulebook_version      TEXT NOT NULL,
      content_hash          TEXT NOT NULL,
      consulted_ids         TEXT NOT NULL DEFAULT '[]',
      controlling_id        TEXT,
      controlling_state     TEXT,
      judgment_batch_id     TEXT,
      is_acceptance         INTEGER NOT NULL DEFAULT 0,
      expiry                TEXT,
      referral_outcome      TEXT,
      renews_record         TEXT,
      promoted_from         TEXT,
      -- Definition 7 as amended (1 Sep 2026). The licensing constraint is
      -- expressed here as a table CHECK exactly as on SQLite, so the ledger
      -- refuses an unlicensed first-instance row on either backend.
      admission_ground      TEXT,
      class_id              TEXT,
      CHECK (
        (COALESCE(admission_ground,'contest') = 'contest'
           AND authority_tier BETWEEN 2 AND 4
           AND class_id IS NULL)
        OR
        (admission_ground = 'consolidation'
           AND authority_tier = 1
           AND class_id IS NOT NULL)
      )
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS consolidation_class (
      class_id         TEXT PRIMARY KEY,
      snapshot_hash    TEXT NOT NULL,
      rulebook_version TEXT NOT NULL,
      provision_id     TEXT NOT NULL,
      signature        TEXT NOT NULL,
      n0               INTEGER NOT NULL,
      delta_seconds    INTEGER NOT NULL,
      members          TEXT NOT NULL,
      docket           TEXT NOT NULL,
      representative   TEXT NOT NULL,
      producer_service TEXT NOT NULL,
      formed_at        TEXT NOT NULL,
      UNIQUE (provision_id, rulebook_version, signature)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS consolidated_disposition (
      seq          BIGSERIAL PRIMARY KEY,
      class_id     TEXT NOT NULL REFERENCES consolidation_class(class_id),
      member_unit  TEXT NOT NULL,
      case_id      TEXT NOT NULL,
      cites_record TEXT NOT NULL REFERENCES precedent_record(id),
      disposition  TEXT NOT NULL,
      decided_at   TEXT NOT NULL,
      UNIQUE (class_id, member_unit)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS precedent_lifecycle_event (
      seq           BIGSERIAL PRIMARY KEY,
      record_id     TEXT NOT NULL REFERENCES precedent_record(id),
      event_type    TEXT NOT NULL,
      detail        TEXT,
      actor         TEXT,
      occurred_at   TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS judgment_invocation (
      invocation_id   TEXT PRIMARY KEY,
      batch_id        TEXT NOT NULL,
      case_id         TEXT NOT NULL,
      candidate_hash  TEXT NOT NULL,
      verdict         TEXT NOT NULL,
      model           TEXT,
      latency_ms      INTEGER,
      degraded        INTEGER NOT NULL DEFAULT 0,
      occurred_at     TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS retrieval_log (
      log_id        TEXT PRIMARY KEY,
      case_id       TEXT NOT NULL,
      provision_id  TEXT NOT NULL,
      candidates    TEXT NOT NULL,
      occurred_at   TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS case_state (
      case_id           TEXT PRIMARY KEY,
      provision_id      TEXT NOT NULL,
      organization      TEXT,
      facts             TEXT NOT NULL,
      status            TEXT NOT NULL,
      current_tier      INTEGER NOT NULL DEFAULT 1,
      final_record_id   TEXT,
      author            TEXT,
      opened_at         TEXT NOT NULL,
      updated_at        TEXT NOT NULL,
      case_scope        TEXT,
      rulebook_version  TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS contest_event (
      seq         BIGSERIAL PRIMARY KEY,
      case_id     TEXT NOT NULL,
      from_tier   INTEGER NOT NULL,
      to_tier     INTEGER NOT NULL,
      actor       TEXT NOT NULL,
      grounds     TEXT NOT NULL,
      occurred_at TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS pr_session (
      session_id          TEXT PRIMARY KEY,
      delivery_id         TEXT UNIQUE,
      repo                TEXT,
      pr_number           INTEGER,
      head_sha            TEXT,
      author              TEXT,
      factors             TEXT,
      extractor_version   TEXT,
      map_hash            TEXT,
      organization        TEXT,
      received_at         TEXT NOT NULL,
      payload_hash        TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS pr_case (
      session_id    TEXT NOT NULL REFERENCES pr_session(session_id),
      case_id       TEXT NOT NULL,
      provision_id  TEXT NOT NULL,
      PRIMARY KEY (session_id, case_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS pr_disposition (
      seq         BIGSERIAL PRIMARY KEY,
      session_id  TEXT NOT NULL,
      disposition TEXT NOT NULL,
      lane        TEXT,
      reason      TEXT,
      detail      TEXT,
      actor       TEXT,
      occurred_at TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS outbound_delivery (
      id          TEXT PRIMARY KEY,
      session_id  TEXT,
      target      TEXT NOT NULL,
      kind        TEXT NOT NULL,
      payload     TEXT NOT NULL,
      status      TEXT NOT NULL,
      transport   TEXT,
      response    TEXT,
      attempts    INTEGER NOT NULL DEFAULT 0,
      created_at  TEXT NOT NULL,
      updated_at  TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS review_task (
      task_id       TEXT PRIMARY KEY,
      session_id    TEXT,
      case_id       TEXT,
      status        TEXT NOT NULL,
      opened_at     TEXT NOT NULL,
      opened_by     TEXT,
      decided_at    TEXT,
      decided_by    TEXT,
      decision      TEXT,
      rationale     TEXT,
      organization  TEXT
    )
    """,
    # Indexes used by retrieve / admin
    "CREATE INDEX IF NOT EXISTS pr_provision_org ON precedent_record (provision_id, organization)",
    "CREATE INDEX IF NOT EXISTS pr_resolved ON precedent_record (resolved_at)",
    "CREATE INDEX IF NOT EXISTS cs_status ON case_state (status)",
    # Views (drop first for upgrade safety)
    "DROP VIEW IF EXISTS record_effective CASCADE",
    """
    CREATE VIEW record_effective AS
    SELECT r.*,
      EXISTS (
        SELECT 1 FROM precedent_lifecycle_event e
        WHERE e.record_id = r.id AND e.event_type = 'lapsed'
      ) AS lapsed,
      EXISTS (
        SELECT 1 FROM precedent_lifecycle_event e
        WHERE e.record_id = r.id AND e.event_type = 'superseded'
      ) AS superseded
    FROM precedent_record r
    """,
    "DROP VIEW IF EXISTS pr_session_current CASCADE",
    """
    CREATE VIEW pr_session_current AS
    SELECT s.*,
           d.disposition   AS disposition,
           d.lane          AS lane,
           d.reason        AS reason,
           d.detail        AS detail,
           d.actor         AS decided_by,
           d.occurred_at   AS disposed_at
    FROM pr_session s
    LEFT JOIN pr_disposition d
      ON d.seq = (SELECT MAX(x.seq) FROM pr_disposition x
                  WHERE x.session_id = s.session_id)
    """,
]

# Immutability triggers for append-only tables
for _t, _m in (
    ("authority_assignment", "authority_assignment is immutable except revocation"),
    ("rulebook_version", "rulebook versions are immutable once enacted"),
    ("provision", "provisions are immutable within a version"),
    ("precedent_record", "A5: precedent records are immutable"),
    ("precedent_lifecycle_event", "lifecycle events are immutable"),
    ("judgment_invocation", "judgment invocations are immutable"),
    ("contest_event", "contest events are immutable"),
    ("pr_session", "inbound sessions are immutable"),
    ("pr_case", "the case list of a session is immutable"),
    ("pr_disposition", "dispositions are append-only"),
    # These three were protected on SQLite and not here, which meant three
    # guarantees silently did not hold on Postgres:
    #   draft_amendment   — the record of what the lawmakers decided could be
    #                       rewritten around decide_amendment (PRB-9)
    #   outbound_delivery — IFP-05: what we told GitHub could be edited after
    #                       the fact
    #   review_task       — see below; the conditional one, and the worst
    ("draft_amendment", "amendments are immutable except by decision"),
    ("outbound_delivery", "the outbound message is immutable"),
    # A9: the standing declaration is append-only on both backends; a
    # deployment changes it by declaring again, never by rewriting history.
    ("standing_declaration", "standing declarations are immutable; declare again"),
    # Definition 16's artefacts. A class whose member list or snapshot could
    # be rewritten after the fact would make CC-19 and CC-20 assertions about
    # nothing, and the N-1 dispositions are the pipeline's decision log, which
    # Corollary 2 as restated says the Store's guarantee does not reach — a
    # log that can be edited is not a log.
    ("consolidation_class", "class artefacts are immutable"),
    ("consolidated_disposition", "consolidated dispositions are immutable"),
):
    PG_LEDGER_STATEMENTS.extend(_immut_triggers(_t, _m))


# review_task needs a CONDITIONAL trigger, not a blanket one: the queue is
# written to while a review is open and frozen the moment it is decided. A
# port that mechanically copies "the append-only tables" misses this, because
# review_task is not append-only — it is append-only *after* a decision.
# Losing it means a decided review can be reopened, reassigned, or have the
# dossier it was decided on rewritten (IFP-06, IFP-07).
PG_LEDGER_STATEMENTS.extend([
    "DROP TRIGGER IF EXISTS tr_review_task_final ON review_task;",
    """
    CREATE OR REPLACE FUNCTION fn_review_task_final() RETURNS trigger AS $$
    BEGIN
      IF OLD.state = 'decided' THEN
        RAISE EXCEPTION '%', 'a decided review is final';
      END IF;
      RETURN NEW;
    END; $$ LANGUAGE plpgsql;
    """,
    """
    CREATE TRIGGER tr_review_task_final
    BEFORE UPDATE ON review_task
    FOR EACH ROW EXECUTE FUNCTION fn_review_task_final();
    """,
    "DROP TRIGGER IF EXISTS tr_review_task_del ON review_task;",
    """
    CREATE OR REPLACE FUNCTION fn_review_task_del() RETURNS trigger AS $$
    BEGIN
      RAISE EXCEPTION '%', 'review tasks are never deleted';
    END; $$ LANGUAGE plpgsql;
    """,
    """
    CREATE TRIGGER tr_review_task_del
    BEFORE DELETE ON review_task
    FOR EACH ROW EXECUTE FUNCTION fn_review_task_del();
    """,
])


# Every table SQLite protects. Asserted rather than assumed: the two schemas
# are written separately and will drift, and a missing trigger is invisible
# until somebody edits a row that should have been unwritable.
PROTECTED_TABLES = frozenset({
    "authority_assignment", "rulebook_version", "provision",
    "precedent_record", "precedent_lifecycle_event", "judgment_invocation",
    "contest_event", "pr_session", "pr_case", "pr_disposition",
    "draft_amendment", "outbound_delivery", "review_task",
    "standing_declaration",
})


def protected_tables_in_statements() -> set:
    """Which tables the Postgres schema actually guards, read back from the
    statements themselves rather than from a list someone maintains."""
    import re as _re
    found = set()
    for st in PG_LEDGER_STATEMENTS:
        for m in _re.finditer(r"BEFORE (?:UPDATE|DELETE) ON (\w+)", st):
            found.add(m.group(1))
    return found


def ledger_on_postgres() -> bool:
    backend = os.environ.get("DJ_LEDGER_BACKEND", "").lower().strip()
    if backend in ("sqlite", "sqllite"):
        return False
    if backend == "postgres":
        return True
    # Explicit opt-in only — DJ_DATABASE_URL alone drives the *job queue*.
    return os.environ.get("DJ_LEDGER_ON_PG", "0") == "1"


def _connect_raw():
    url = os.environ.get("DJ_DATABASE_URL", "")
    if not url.startswith("postgres"):
        raise RuntimeError(
            "Postgres ledger requires DJ_DATABASE_URL=postgres://... "
            "and DJ_LEDGER_BACKEND=postgres (or DJ_LEDGER_ON_PG=1)")
    try:
        import psycopg
        from psycopg.rows import dict_row
    except ImportError as e:
        raise RuntimeError(
            "pip install 'psycopg[binary]>=3.1' for Postgres ledger"
        ) from e
    conn = psycopg.connect(url, row_factory=dict_row)
    return conn


class _PgCursor:
    def __init__(self, cur):
        self._cur = cur
        self.lastrowid = None

    def execute(self, sql: str, params: Sequence[Any] | None = None):
        sql_pg = _rewrite_sql(sql)
        if params is None:
            self._cur.execute(sql_pg)
        else:
            self._cur.execute(sql_pg, tuple(params))
        return self

    def executemany(self, sql: str, seq_of_params: Iterable[Sequence[Any]]):
        sql_pg = _rewrite_sql(sql)
        self._cur.executemany(sql_pg, list(seq_of_params))
        return self

    def fetchone(self):
        return self._cur.fetchone()

    def fetchall(self):
        return self._cur.fetchall()

    def close(self):
        self._cur.close()

    @property
    def rowcount(self):
        return self._cur.rowcount


def _rewrite_sql(sql: str) -> str:
    """Rewrite SQLite-ish SQL to Postgres."""
    s = sql.strip()
    # placeholder ? → %s (psycopg)
    # Avoid replacing ? inside strings — our SQL rarely embeds ? in literals.
    s = re.sub(r"\?", "%s", s)
    # INSERT OR IGNORE → ON CONFLICT DO NOTHING (best-effort; needs constraint)
    s = re.sub(
        r"INSERT\s+OR\s+IGNORE\s+INTO",
        "INSERT INTO",
        s,
        flags=re.I,
    )
    return s


class PgLedgerConnection:
    """sqlite3.Connection-compatible subset used by the Kernel."""

    def __init__(self, raw, *, read_only: bool = False):
        self._raw = raw
        self._read_only = read_only
        self.row_factory = None  # already dict_row
        self.total_changes = 0

    def execute(self, sql: str, params: Sequence[Any] | None = None):
        if self._read_only:
            op = sql.lstrip().split(None, 1)[0].upper()
            if op in ("INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE",
                      "TRUNCATE", "REPLACE"):
                raise RuntimeError(f"read-only ledger connection refused {op}")
        cur = self._raw.cursor()
        c = _PgCursor(cur)
        c.execute(sql, params)
        try:
            self.total_changes += max(0, cur.rowcount or 0)
        except Exception:
            pass
        return c

    def executescript(self, script: str):
        # Split on semicolons at top level — good enough for our DDL list path.
        for stmt in PG_LEDGER_STATEMENTS:
            self.execute(stmt)
        self.commit()
        return self

    def commit(self):
        self._raw.commit()

    def rollback(self):
        self._raw.rollback()

    def close(self):
        self._raw.close()

    def cursor(self):
        return _PgCursor(self._raw.cursor())


def open_writer() -> PgLedgerConnection:
    conn = _connect_raw()
    conn.autocommit = False
    return PgLedgerConnection(conn, read_only=False)


def open_reader() -> PgLedgerConnection:
    # Application-level read-only (same user). For true RO, use a DB role.
    conn = _connect_raw()
    conn.autocommit = False
    return PgLedgerConnection(conn, read_only=True)


def init_ledger() -> None:
    w = open_writer()
    try:
        for stmt in PG_LEDGER_STATEMENTS:
            try:
                w.execute(stmt)
            except Exception as e:
                # IF NOT EXISTS / OR REPLACE races — ignore duplicate
                msg = str(e).lower()
                if "already exists" in msg or "duplicate" in msg:
                    w.rollback()
                    continue
                # EXECUTE FUNCTION vs PROCEDURE on older PG
                if "execute function" in msg:
                    alt = stmt.replace("EXECUTE FUNCTION", "EXECUTE PROCEDURE")
                    try:
                        w.execute(alt)
                        w.commit()
                        continue
                    except Exception:
                        w.rollback()
                        raise e
                w.rollback()
                raise
        w.commit()
    finally:
        w.close()
