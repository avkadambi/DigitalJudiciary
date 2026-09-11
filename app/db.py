"""L1 Substrate: SQLite schema carrying the physical enforcement of the contract.

Design decisions (see README, "Review decisions"):
  * SQLite replaces PostgreSQL for the single-container goal. Every contract
    property that v3.0 placed in Postgres (EXCLUDE, CHECK, immutability
    triggers, revoked grants) is re-expressed here as SQLite CHECKs and
    RAISE(ABORT) triggers, plus read-only connections for non-Kernel code.
  * WAL mode; a single writer connection per Kernel service class. The
    sole-writer property of the Challenge Gate (Def. 7 / CC-11) is physical:
    only the Gate object is ever handed the ledger writer.
  * Timestamps are ISO-8601 UTC strings with a fixed format, so lexicographic
    comparison is chronological comparison, in SQL and in Python alike.
"""
from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone

DB_PATH = os.environ.get("DJ_DB", "/data/judiciary.db")

def use_postgres_ledger() -> bool:
    """True when the Kernel ledger is stored in Postgres."""
    try:
        from .platform.pg_ledger import ledger_on_postgres
        return ledger_on_postgres()
    except Exception:
        return False


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")

SCHEMA = r"""
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

------------------------------------------------------------------
-- Principals and Authority Registry (Axiom A1)
------------------------------------------------------------------
------------------------------------------------------------------
-- Tenancy
--
-- `organization` is NULLABLE everywhere on purpose, and NULL means
-- PLATFORM-WIDE rather than "unset". A single-tenant deployment leaves
-- every column NULL and behaves exactly as before; a multi-tenant one
-- scopes principals to a tenant and leaves auditors and group-level
-- officers unscoped. Scoping is therefore additive: it can be introduced
-- to a running ledger without rewriting a single existing row.
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS organization (
  org_id      TEXT PRIMARY KEY,
  name        TEXT NOT NULL,
  created_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS principal (
  principal_id  TEXT PRIMARY KEY,
  kind          TEXT NOT NULL CHECK (kind IN ('human','workload')),
  api_key_hash  TEXT NOT NULL,
  created_at    TEXT NOT NULL,
  -- NULL = platform-wide: sees and serves every tenant.
  organization  TEXT REFERENCES organization(org_id),
  -- Free text, for the sign-in bench only. Authority comes from the branch;
  -- this just says what the person is for.
  role_hint     TEXT
);

CREATE TABLE IF NOT EXISTS authority_assignment (
  assignment_id TEXT PRIMARY KEY,
  principal_id  TEXT NOT NULL REFERENCES principal(principal_id),
  branch        TEXT NOT NULL CHECK (branch IN ('lawmakers','judges','risk_owner')),
  valid_from    TEXT NOT NULL,
  valid_to      TEXT,                 -- NULL = open-ended
  granted_by    TEXT NOT NULL,
  grant_reason  TEXT NOT NULL
);

-- A1: one principal, one branch, at any instant. SQLite has no EXCLUDE
-- constraint; this trigger is its equivalent and CC-01 re-verifies it.
CREATE TRIGGER IF NOT EXISTS aa_no_overlap
BEFORE INSERT ON authority_assignment
WHEN EXISTS (
  SELECT 1 FROM authority_assignment a
  WHERE a.principal_id = NEW.principal_id
    AND (a.valid_to IS NULL OR a.valid_to > NEW.valid_from)
    AND (NEW.valid_to IS NULL OR NEW.valid_to > a.valid_from)
)
BEGIN
  SELECT RAISE(ABORT, 'A1 violation: overlapping branch assignment for principal');
END;

-- Assignments are historical records. The only permitted mutation is
-- closing an open valid_to (revocation); everything else is immutable.
CREATE TRIGGER IF NOT EXISTS aa_immutable
BEFORE UPDATE ON authority_assignment
WHEN NOT (OLD.valid_to IS NULL AND NEW.valid_to IS NOT NULL
          AND NEW.assignment_id = OLD.assignment_id
          AND NEW.principal_id  = OLD.principal_id
          AND NEW.branch        = OLD.branch
          AND NEW.valid_from    = OLD.valid_from
          AND NEW.granted_by    = OLD.granted_by
          AND NEW.grant_reason  = OLD.grant_reason)
BEGIN
  SELECT RAISE(ABORT, 'authority_assignment is immutable except revocation');
END;

CREATE TRIGGER IF NOT EXISTS aa_nodelete
BEFORE DELETE ON authority_assignment
BEGIN SELECT RAISE(ABORT, 'authority_assignment rows are never deleted'); END;

------------------------------------------------------------------
-- Constitution Store (Axiom A3, Definition 1)
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS rulebook_version (
  version_id    TEXT PRIMARY KEY,
  content_hash  TEXT NOT NULL UNIQUE,
  enacted_at    TEXT NOT NULL,
  enacted_by    TEXT NOT NULL,
  amendment_id  TEXT               -- NULL only for the bootstrap version
);
CREATE TRIGGER IF NOT EXISTS rv_immutable BEFORE UPDATE ON rulebook_version
BEGIN SELECT RAISE(ABORT, 'rulebook versions are immutable once enacted'); END;
CREATE TRIGGER IF NOT EXISTS rv_nodelete BEFORE DELETE ON rulebook_version
BEGIN SELECT RAISE(ABORT, 'rulebook versions are never deleted'); END;

CREATE TABLE IF NOT EXISTS provision (
  version_id    TEXT NOT NULL REFERENCES rulebook_version(version_id),
  -- The tenant whose constitution this clause belongs to. Provision ids are
  -- globally unique, which is what makes retrieval tenant-safe without a
  -- filter on the hot path: retrieval is keyed by provision_id, so a holding
  -- of one tenant can never be a candidate for another tenant's case.
  -- EX-20 enforces that uniqueness rather than trusting it.
  organization  TEXT,
  provision_id  TEXT NOT NULL,
  text          TEXT NOT NULL,
  policy_source TEXT NOT NULL,     -- JSON predicate, see adjudicate.rule_eval
  absolute      INTEGER NOT NULL CHECK (absolute IN (0,1)),
  PRIMARY KEY (version_id, provision_id)
);
CREATE TRIGGER IF NOT EXISTS pv_immutable BEFORE UPDATE ON provision
BEGIN SELECT RAISE(ABORT, 'provisions are immutable within a version'); END;
CREATE TRIGGER IF NOT EXISTS pv_nodelete BEFORE DELETE ON provision
BEGIN SELECT RAISE(ABORT, 'provisions are never deleted'); END;

-- A9: the standing declaration. A first-class, append-only object stating
-- whether any party holds contest standing adverse to grants -- globally
-- (scope = '_global') or per provision. The declaration does not create
-- standing and repairs nothing; it makes the presence or absence of an
-- adverse contestant a stated, attributed, dated fact that every audit
-- export and rationale trail carries (kernel.LedgerReader.rebuild). The
-- declaration in force at a time t is the most recent row with
-- declared_at <= t, a provision-scoped row taking precedence over the
-- global one. Rows are never updated or deleted; to change the
-- declaration, declare again.
CREATE TABLE IF NOT EXISTS standing_declaration (
  declaration_id    TEXT PRIMARY KEY,
  scope             TEXT NOT NULL,      -- '_global' or a provision_id
  adverse_to_grants INTEGER NOT NULL CHECK (adverse_to_grants IN (0,1)),
  holder            TEXT,               -- the party holding it, when yes
  declared_by       TEXT NOT NULL,      -- the authority that declared
  declared_at       TEXT NOT NULL
);
CREATE TRIGGER IF NOT EXISTS sd_immutable BEFORE UPDATE ON standing_declaration
BEGIN SELECT RAISE(ABORT, 'standing declarations are immutable; declare again'); END;
CREATE TRIGGER IF NOT EXISTS sd_nodelete BEFORE DELETE ON standing_declaration
BEGIN SELECT RAISE(ABORT, 'standing declarations are never deleted'); END;

CREATE TABLE IF NOT EXISTS draft_amendment (
  id            TEXT PRIMARY KEY,
  proposed_by   TEXT NOT NULL,
  origin        TEXT NOT NULL CHECK (origin IN
                ('engineer','adjudication_tier','risk_acceptance_referral',
                 'lifecycle_referral','lawmaker','control_plane_routed',
                 -- A tier reporting that the rulebook is underdetermined on
                 -- facts it just had to decide. A3 forbids adjudication from
                 -- ENACTING an amendment; it does not forbid proposing one,
                 -- and the Lawmakers still decide (decide_amendment).
                 'judicial_referral')),
  source_record TEXT,
  body          TEXT NOT NULL,     -- JSON: proposed provision changes
  status        TEXT NOT NULL DEFAULT 'pending' CHECK (status IN
                ('pending','adopted','rejected','withdrawn')),
  decided_by    TEXT,
  decided_at    TEXT,
  created_at    TEXT NOT NULL,
  -- The tenant whose constitution this proposal touches. A lawmaker holds
  -- the branch for their own company, not for everyone's: without this,
  -- one tenant's GRC council could amend another's rulebook.
  organization  TEXT
);
-- The only permitted mutation is a single pending -> terminal transition.
CREATE TRIGGER IF NOT EXISTS da_transitions
BEFORE UPDATE ON draft_amendment
WHEN NOT (OLD.status = 'pending'
          AND NEW.status IN ('adopted','rejected','withdrawn')
          AND NEW.id = OLD.id AND NEW.body = OLD.body
          AND NEW.proposed_by = OLD.proposed_by
          AND NEW.decided_by IS NOT NULL AND NEW.decided_at IS NOT NULL)
BEGIN
  SELECT RAISE(ABORT, 'draft_amendment permits only pending->terminal, decided_by set');
END;
CREATE TRIGGER IF NOT EXISTS da_nodelete BEFORE DELETE ON draft_amendment
BEGIN SELECT RAISE(ABORT, 'amendments are never deleted'); END;

------------------------------------------------------------------
-- Consolidation classes (Definitions 15, 16)
--
-- The class artefact is the whole of what Classify produces, and it is
-- written BEFORE any member is adjudicated. It carries the pinned snapshot
-- hash, the parameters in force, the signature, the ordered member list, the
-- representative and the identity of the pipeline service that produced it.
-- The producing service holds no credential of any authority class; CC-22(a)
-- asserts that against the ledger's own role table.
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS consolidation_class (
  class_id         TEXT PRIMARY KEY,
  snapshot_hash    TEXT NOT NULL,
  rulebook_version TEXT NOT NULL REFERENCES rulebook_version(version_id),
  provision_id     TEXT NOT NULL,
  signature        TEXT NOT NULL,   -- JSON: sorted facts(c) INTERSECT F_p
  n0               INTEGER NOT NULL CHECK (n0 >= 2),
  delta_seconds    INTEGER NOT NULL CHECK (delta_seconds > 0),
  members          TEXT NOT NULL,   -- JSON array, ordered by the published key
  -- Every unit the boundary considered, member or not. The member list alone
  -- cannot support a completeness claim: an auditor reading it can see that
  -- the members are alike and cannot see whether a like unit was left out.
  -- CC-20(g) reads this, and the grain mutant is caught by nothing else.
  docket           TEXT NOT NULL,   -- JSON array of unit ids in D_t
  representative   TEXT NOT NULL,
  producer_service TEXT NOT NULL,
  formed_at        TEXT NOT NULL,
  -- The class is keyed on the same triple CC-21 keys the ledger on, so a
  -- second class over a signature already covered is a uniqueness failure
  -- here as well as at the ledger.
  UNIQUE (provision_id, rulebook_version, signature)
);
CREATE TRIGGER IF NOT EXISTS cc_immutable BEFORE UPDATE ON consolidation_class
BEGIN SELECT RAISE(ABORT, 'class artefacts are immutable'); END;
CREATE TRIGGER IF NOT EXISTS cc_nodelete BEFORE DELETE ON consolidation_class
BEGIN SELECT RAISE(ABORT, 'class artefacts are never deleted'); END;

-- The disposition of a non-representative member. These rows are the
-- pipeline's decision log and they are NOT the Store: no guarantee of the
-- chapter attaches to them, which is exactly what Corollary 2 as restated
-- says of the N-1.
CREATE TABLE IF NOT EXISTS consolidated_disposition (
  seq          INTEGER PRIMARY KEY AUTOINCREMENT,
  class_id     TEXT NOT NULL REFERENCES consolidation_class(class_id),
  member_unit  TEXT NOT NULL,
  -- The case the unit was filed as. CC-22(b) needs it: the temporal limb
  -- asserts that no judgment invocation for any member predates the class
  -- artefact, and without this the member's case cannot be found from the
  -- artefact at all.
  case_id      TEXT NOT NULL,
  cites_record TEXT NOT NULL REFERENCES precedent_record(id),
  disposition  TEXT NOT NULL,
  decided_at   TEXT NOT NULL,
  UNIQUE (class_id, member_unit)
);
CREATE TRIGGER IF NOT EXISTS cd_immutable BEFORE UPDATE ON consolidated_disposition
BEGIN SELECT RAISE(ABORT, 'consolidated dispositions are immutable'); END;
CREATE TRIGGER IF NOT EXISTS cd_nodelete BEFORE DELETE ON consolidated_disposition
BEGIN SELECT RAISE(ABORT, 'consolidated dispositions are never deleted'); END;

------------------------------------------------------------------
-- Precedent Ledger (Axioms A5, A7; Definitions 7, 8)
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS precedent_record (
  id                  TEXT PRIMARY KEY,
  organization        TEXT,          -- inherited from the provision
  content_hash        TEXT NOT NULL UNIQUE,
  case_id             TEXT NOT NULL,
  provision_id        TEXT NOT NULL,
  rulebook_version    TEXT NOT NULL REFERENCES rulebook_version(version_id),
  facts               TEXT NOT NULL,   -- JSON array of factors
  premise             TEXT NOT NULL,   -- JSON array: facts the holding rested on
  interpretation      TEXT NOT NULL,   -- JSON
  conditions          TEXT,            -- JSON
  authority_tier      INTEGER NOT NULL CHECK (authority_tier BETWEEN 1 AND 4),
  -- Definition 7's admission bar, at the schema.
  --
  -- Until 1 September 2026 this column was CHECK (authority_tier BETWEEN 2 AND 4):
  -- a first-instance record was unrepresentable, full stop, and probe PRB-3
  -- asserted exactly that. RA-3's Definition 7(ii) admits a *consolidated*
  -- record at first instance, so the flat bar had to go.
  --
  -- What replaces it is narrower, not looser. Tier 1 remains unrepresentable on
  -- every ground but one, and the one is named in the row itself. A build that
  -- writes a tier-1 record without an admission_ground of 'consolidation' still
  -- aborts at the schema, which is what PRB-3 now asserts.
  admission_ground    TEXT CHECK (admission_ground IN ('contest','consolidation')),
  -- Definition 7(ii)'s class artefact. Null on every contested admission and
  -- non-null on every consolidated one: the record says under which clause it
  -- entered and, where it entered under (ii), which co-pending units it
  -- disposed of. Both fields are on the RECORD and not in configuration, which
  -- is what lets CC-21 and CC-22 be computed from a released ledger by a
  -- reader who has never seen the pipeline.
  class_id            TEXT REFERENCES consolidation_class(class_id),
  resolving_principal TEXT NOT NULL,
  consulted_ids       TEXT NOT NULL,   -- JSON array (may be empty, never null)
  controlling_id      TEXT REFERENCES precedent_record(id),
  controlling_state   TEXT NOT NULL CHECK (controlling_state IN
                      ('bound','none_empty','none_all_distinguished',
                       'none_tie','none_degraded')),
  tie_members         TEXT,            -- JSON array
  rationale_text      TEXT NOT NULL CHECK (length(rationale_text) > 0),
  judgment_batch_id   TEXT NOT NULL,
  scope               TEXT NOT NULL,   -- JSON
  -- 'platform' sits BELOW 'org' in closeness: a shared holding is general
  -- law, and a tenant's own holding on the same facts outranks it on the
  -- scope key. Tenant law above platform law is the point of an overlay.
  scope_level         TEXT NOT NULL CHECK (scope_level IN
                      ('platform','service','team','domain','org')),
  is_acceptance       INTEGER NOT NULL DEFAULT 0 CHECK (is_acceptance IN (0,1)),
  expiry              TEXT,
  renews_record       TEXT REFERENCES precedent_record(id),
  -- Set when the lawmakers ratify a tenant holding as generally applicable.
  promoted_from       TEXT REFERENCES precedent_record(id),
  resolved_at         TEXT NOT NULL,
  degraded            INTEGER NOT NULL DEFAULT 0 CHECK (degraded IN (0,1)),
  -- v3.0 errata: the spec's CHECK (tier < 4 OR expiry NOT NULL) forbade the
  -- paper's own "RiskOwner upholds the denial" case (a tier-k record that is
  -- not an acceptance). Corrected: the expiry obligation attaches to
  -- ACCEPTANCES, and acceptances exist only at tier k. (A7)
  CHECK (is_acceptance = 0 OR authority_tier = 4),
  CHECK (is_acceptance = 0 OR expiry IS NOT NULL),
  CHECK ((controlling_state = 'bound') = (controlling_id IS NOT NULL)),
  CHECK (controlling_state <> 'none_tie' OR tie_members IS NOT NULL),
  -- Definition 7's admission bar, as a table constraint because it spans two
  -- columns. Tier 1 is representable on exactly one ground and no other; a
  -- build that writes a first-instance record for any other reason aborts here.
  -- COALESCE, not a bare comparison: with admission_ground NULL the bare form
  -- evaluates to NULL and SQLite passes a NULL CHECK, so the bar would not
  -- bind on exactly the rows it exists to stop.
  -- Definition 7 as amended, in one table constraint because it spans three
  -- columns. Clause (i) admissions are tier 2..4 and carry no class; clause
  -- (ii) admissions are tier 1 and must name their class artefact. A tier-1
  -- row on any other footing aborts here, which is what PRB-3 and PRB-3b
  -- assert; PRB-11 asserts the licensed row is licensed and PRB-12 asserts a
  -- consolidated row without a class is not.
  --
  -- COALESCE, not a bare comparison, on the first limb: a legacy row carries
  -- admission_ground NULL and means 'contest', and with a bare comparison the
  -- limb would evaluate to NULL, which SQLite passes — so the bar would not
  -- bind on exactly the rows it exists to stop.
  CHECK (
    (COALESCE(admission_ground,'contest') = 'contest'
       AND authority_tier BETWEEN 2 AND 4
       AND class_id IS NULL)
    OR
    (admission_ground = 'consolidation'
       AND authority_tier = 1
       AND class_id IS NOT NULL)
  ),
  -- Definition 8's `cites`, in both its roles: on an acceptance it names
  -- the lapsed acceptance this one renews (A7); on an ordinary holding it
  -- names the earlier holding this one supersedes (Sect. 4.6), which is
  -- what lets recency displace a conflicting record at all.
  CHECK (renews_record IS NULL OR renews_record <> id)
);
CREATE INDEX IF NOT EXISTS pr_provision ON precedent_record (provision_id);
CREATE TRIGGER IF NOT EXISTS pr_immutable BEFORE UPDATE ON precedent_record
BEGIN SELECT RAISE(ABORT, 'A5: precedent records are immutable'); END;
CREATE TRIGGER IF NOT EXISTS pr_nodelete BEFORE DELETE ON precedent_record
BEGIN SELECT RAISE(ABORT, 'A5: precedent records are never deleted'); END;

CREATE TABLE IF NOT EXISTS precedent_lifecycle_event (
  seq          INTEGER PRIMARY KEY AUTOINCREMENT,
  record_id    TEXT NOT NULL REFERENCES precedent_record(id),
  event_type   TEXT NOT NULL CHECK (event_type IN
               ('lapsed','referral_emitted','referral_adopted',
                'referral_rejected','referral_withdrawn',
                'renewed_by','outcome_recorded',
                -- The legislature changed the clause this holding
                -- interpreted. Lapse is what the clock does to a holding;
                -- supersession is what the legislature does to one.
                'superseded',
                -- A later holding on the same provision expressly cited this
                -- one as the record it departs from, so recency may displace
                -- it at the ordering step (Sect. 4.6). The record stays in
                -- the Store: this is a displacement, not an overruling.
                'displaced_by')),
  payload      TEXT NOT NULL,       -- JSON
  actor        TEXT NOT NULL,
  occurred_at  TEXT NOT NULL
);
CREATE TRIGGER IF NOT EXISTS ple_immutable BEFORE UPDATE ON precedent_lifecycle_event
BEGIN SELECT RAISE(ABORT, 'lifecycle events are immutable'); END;
CREATE TRIGGER IF NOT EXISTS ple_nodelete BEFORE DELETE ON precedent_lifecycle_event
BEGIN SELECT RAISE(ABORT, 'lifecycle events are never deleted'); END;

-- Derived lapse state (A7). A view, exactly as in the spec: lapse is
-- computed, never a mutable flag.
-- The register reads newest-first and pages by (resolved_at, id); the
-- lifecycle lookup below is the correlated subquery inside record_effective,
-- which runs per row and would otherwise scan.
CREATE INDEX IF NOT EXISTS pr_resolved
  ON precedent_record (resolved_at DESC, id DESC);
CREATE INDEX IF NOT EXISTS ple_record_type
  ON precedent_lifecycle_event (record_id, event_type);

CREATE INDEX IF NOT EXISTS pr_org ON precedent_record (organization);
-- Composite covering the retrieve() filter path: provision + tenant pool.
-- Speeds the SQL load that fills the process-local active-holdings cache.
CREATE INDEX IF NOT EXISTS pr_provision_org
  ON precedent_record (provision_id, organization);

CREATE VIEW IF NOT EXISTS record_effective AS
SELECT r.*,
  (r.is_acceptance = 1
   AND r.expiry < strftime('%Y-%m-%dT%H:%M:%f000+00:00','now')
   AND NOT EXISTS (SELECT 1 FROM precedent_lifecycle_event e
                   WHERE e.record_id = r.id
                     AND e.event_type = 'referral_adopted')) AS lapsed,
  -- Computed the same way `lapsed` is: the row stays in the ledger forever,
  -- but it stops being live. A superseded holding interpreted words that no
  -- longer exist, so it may not control a case decided under the new ones.
  EXISTS (SELECT 1 FROM precedent_lifecycle_event e2
          WHERE e2.record_id = r.id
            AND e2.event_type = 'superseded') AS superseded
FROM precedent_record r;

------------------------------------------------------------------
-- Judgment Provenance (P3) and the verdict cache
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS judgment_invocation (
  id              TEXT PRIMARY KEY,
  batch_id        TEXT NOT NULL,
  kind            TEXT NOT NULL CHECK (kind IN
                  ('similar','distinguish','premise')),
  candidate_hash  TEXT NOT NULL,
  case_hash       TEXT NOT NULL,
  -- The tier that asked. Without this a re-adjudication one rung up reuses
  -- the rung below's verdict from cache, which makes escalation a relabeling
  -- rather than a fresh look. Escalation has to be able to reach a different
  -- answer or the ladder means nothing.
  tier            INTEGER NOT NULL DEFAULT 0,
  judge_version   TEXT NOT NULL,
  prompt_version  TEXT NOT NULL,
  params          TEXT NOT NULL,
  verdict         TEXT NOT NULL,
  quorum_votes    TEXT,
  latency_ms      INTEGER NOT NULL,
  -- Real usage as reported by the API, never estimated from string length.
  -- NULL in oracle mode and on a cache hit, because in both cases no call
  -- went out and nothing was spent.
  input_tokens    INTEGER,
  output_tokens   INTEGER,
  from_cache      INTEGER NOT NULL CHECK (from_cache IN (0,1)),
  degraded        INTEGER NOT NULL DEFAULT 0 CHECK (degraded IN (0,1)),
  invoked_at      TEXT NOT NULL
);
CREATE UNIQUE INDEX IF NOT EXISTS ji_cache ON judgment_invocation
  (candidate_hash, case_hash, judge_version, prompt_version, tier)
  WHERE from_cache = 0;
CREATE TRIGGER IF NOT EXISTS ji_immutable BEFORE UPDATE ON judgment_invocation
BEGIN SELECT RAISE(ABORT, 'judgment invocations are immutable'); END;
CREATE TRIGGER IF NOT EXISTS ji_nodelete BEFORE DELETE ON judgment_invocation
BEGIN SELECT RAISE(ABORT, 'judgment invocations are never deleted'); END;

------------------------------------------------------------------
-- Retrieval log (CC-08 evidence: absolute provisions never retrieved)
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS retrieval_log (
  id            TEXT PRIMARY KEY,
  case_id       TEXT NOT NULL,
  provision_id  TEXT NOT NULL,
  theta         REAL NOT NULL,
  candidates    INTEGER NOT NULL,
  snapshot_at   TEXT NOT NULL
);

------------------------------------------------------------------
-- Case state (transient adjudication state; process authority)
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS case_state (
  -- The tenant this case belongs to. Carried on the CASE rather than derived
  -- from the provision, because a provision may now be shared: base clauses
  -- have no tenant, and the record must still know whose ledger it joins.
  organization  TEXT,
  case_id          TEXT PRIMARY KEY,
  case_hash        TEXT NOT NULL,
  provision_id     TEXT NOT NULL,
  rulebook_version TEXT NOT NULL,   -- pinned at intake (CC-04)
  facts            TEXT NOT NULL,
  author           TEXT NOT NULL,
  case_scope       TEXT NOT NULL,   -- JSON: {service, team, domain}
  status           TEXT NOT NULL CHECK (status IN
                   ('decided_t1','denied_absolute','escalated',
                    'awaiting_risk_owner','final')),
  current_tier     INTEGER NOT NULL,
  artifacts        TEXT NOT NULL,   -- JSON: {tier: ResolutionArtifact}
  final_record_id  TEXT,
  created_at       TEXT NOT NULL,
  updated_at       TEXT NOT NULL
);

-- Contest events form the hash-chained escalation history the Gate
-- verifies for A4 (the single-container stand-in for a signed Temporal
-- history). chain_hash = HMAC(key, prev_hash | case | tier | actor | ts).
CREATE TABLE IF NOT EXISTS contest_event (
  seq        INTEGER PRIMARY KEY AUTOINCREMENT,
  case_id    TEXT NOT NULL,
  tier       INTEGER NOT NULL,      -- the tier whose decision was contested
  actor      TEXT NOT NULL,
  grounds    TEXT NOT NULL,
  ts         TEXT NOT NULL,
  prev_hash  TEXT NOT NULL,
  chain_hash TEXT NOT NULL
);
CREATE TRIGGER IF NOT EXISTS ce_immutable BEFORE UPDATE ON contest_event
BEGIN SELECT RAISE(ABORT, 'contest events are immutable'); END;
CREATE TRIGGER IF NOT EXISTS ce_nodelete BEFORE DELETE ON contest_event
BEGIN SELECT RAISE(ABORT, 'contest events are never deleted'); END;

------------------------------------------------------------------
-- L5 Interface: what the outside world asked, and what we answered
--
-- The kernel tables above record adjudication. These record the
-- TRANSLATION on either side of it: the pull request that became a
-- case, and the disposition that went back. They are separated
-- deliberately, because the trustworthy claim is not "the gateway
-- behaved" but "whatever the gateway did, the ledger is still sound".
-- Everything here is therefore append-only evidence about a component
-- that holds no authority.
------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pr_session (
  session_id        TEXT PRIMARY KEY,
  -- One session per GitHub delivery. This UNIQUE is the physical form of
  -- webhook idempotency: GitHub retries, and a retry must not be able to
  -- file a second set of cases on the same facts.
  delivery_id       TEXT NOT NULL UNIQUE,
  source            TEXT NOT NULL CHECK (source IN ('github', 'simulator')),
  event_type        TEXT NOT NULL,
  action            TEXT NOT NULL,
  repo              TEXT NOT NULL,
  pr_number         INTEGER NOT NULL,
  head_sha          TEXT NOT NULL,
  pr_author         TEXT NOT NULL,     -- the GitHub login, as received
  filed_by          TEXT NOT NULL,     -- the DJ principal the case was filed as
  -- The extractor pin. Same role for the interface that rulebook_version
  -- plays for the kernel (CC-04): a session can be replayed forever
  -- against the exact map that read it.
  extractor_version TEXT NOT NULL,
  factor_map_hash   TEXT NOT NULL,
  factors           TEXT NOT NULL,     -- JSON array
  provisions        TEXT NOT NULL,     -- JSON array (those actually filed)
  not_reached       TEXT NOT NULL,     -- JSON array (A6: never weighed)
  case_scope        TEXT NOT NULL,     -- JSON
  escalation_policy TEXT NOT NULL CHECK (escalation_policy IN ('manual','auto')),
  payload_hash      TEXT NOT NULL,
  received_at       TEXT NOT NULL,
  organization      TEXT
);
CREATE INDEX IF NOT EXISTS prs_head ON pr_session (head_sha);
CREATE INDEX IF NOT EXISTS prs_org ON pr_session (organization);
CREATE TRIGGER IF NOT EXISTS prs_immutable BEFORE UPDATE ON pr_session
BEGIN SELECT RAISE(ABORT, 'inbound sessions are immutable'); END;
CREATE TRIGGER IF NOT EXISTS prs_nodelete BEFORE DELETE ON pr_session
BEGIN SELECT RAISE(ABORT, 'inbound sessions are never deleted'); END;

-- Which cases this pull request became, in the order they were filed.
-- `seq` carries the floor-first ordering: seq 0 is adjudicated first, and
-- if it is an absolute denial nothing after it is adjudicated at all.
CREATE TABLE IF NOT EXISTS pr_case (
  session_id   TEXT NOT NULL REFERENCES pr_session(session_id),
  case_id      TEXT NOT NULL,
  provision_id TEXT NOT NULL,
  absolute     INTEGER NOT NULL CHECK (absolute IN (0, 1)),
  seq          INTEGER NOT NULL,
  PRIMARY KEY (session_id, case_id)
);
CREATE INDEX IF NOT EXISTS prc_case ON pr_case (case_id);
CREATE TRIGGER IF NOT EXISTS prc_immutable BEFORE UPDATE ON pr_case
BEGIN SELECT RAISE(ABORT, 'the case list of a session is immutable'); END;
CREATE TRIGGER IF NOT EXISTS prc_nodelete BEFORE DELETE ON pr_case
BEGIN SELECT RAISE(ABORT, 'the case list of a session is never deleted'); END;

-- Every answer this system ever gave about a pull request, in order.
-- Append-only: a later lane does not overwrite an earlier disposition, it
-- adds one. The current state is the last row (see pr_session_current),
-- so the history of a contested PR is legible rather than lost.
CREATE TABLE IF NOT EXISTS pr_disposition (
  seq         INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id  TEXT NOT NULL REFERENCES pr_session(session_id),
  disposition TEXT NOT NULL,
  lane        TEXT NOT NULL,
  reason      TEXT NOT NULL,
  detail      TEXT NOT NULL,     -- JSON: per-provision case detail
  actor       TEXT NOT NULL,
  occurred_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS prd_session ON pr_disposition (session_id, seq);
CREATE TRIGGER IF NOT EXISTS prd_immutable BEFORE UPDATE ON pr_disposition
BEGIN SELECT RAISE(ABORT, 'dispositions are append-only'); END;
CREATE TRIGGER IF NOT EXISTS prd_nodelete BEFORE DELETE ON pr_disposition
BEGIN SELECT RAISE(ABORT, 'dispositions are never deleted'); END;

-- What we told the outside world, written BEFORE the network is touched.
-- The audit trail must not depend on GitHub being reachable, which is also
-- what lets the benchmark run entirely offline through identical code.
CREATE TABLE IF NOT EXISTS outbound_delivery (
  id         TEXT PRIMARY KEY,
  session_id TEXT NOT NULL,
  target     TEXT NOT NULL,     -- github_checks | github_comment | jira | ...
  kind       TEXT NOT NULL,
  payload    TEXT NOT NULL,
  status     TEXT NOT NULL CHECK (status IN
             ('recorded', 'sent', 'skipped', 'failed')),
  attempts   INTEGER NOT NULL DEFAULT 0,
  transport  TEXT,
  response   TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS od_session ON outbound_delivery (session_id);
-- Delivery *status* is mutable (a retry is a real event); the message is
-- not. What we said cannot be edited after the fact.
CREATE TRIGGER IF NOT EXISTS od_payload_immutable
BEFORE UPDATE ON outbound_delivery
WHEN NEW.payload <> OLD.payload OR NEW.session_id <> OLD.session_id
  OR NEW.target <> OLD.target OR NEW.kind <> OLD.kind
  OR NEW.created_at <> OLD.created_at OR NEW.id <> OLD.id
BEGIN SELECT RAISE(ABORT, 'the outbound message is immutable'); END;
CREATE TRIGGER IF NOT EXISTS od_nodelete BEFORE DELETE ON outbound_delivery
BEGIN SELECT RAISE(ABORT, 'outbound deliveries are never deleted'); END;

-- The human-review lane: the task that sits in a named person's queue.
-- The task holds NO authority. It is a pointer to a case plus the dossier
-- needed to decide it; the decision itself goes through
-- Adjudicator.risk_decision, which re-checks the branch in the Kernel.
CREATE TABLE IF NOT EXISTS review_task (
  task_id       TEXT PRIMARY KEY,
  session_id    TEXT NOT NULL REFERENCES pr_session(session_id),
  case_id       TEXT NOT NULL,
  provision_id  TEXT NOT NULL,
  title         TEXT NOT NULL,
  summary       TEXT NOT NULL,     -- JSON dossier rendered by the screen
  sinks         TEXT NOT NULL,     -- JSON array: ui | jira | servicenow
  external_refs TEXT NOT NULL,     -- JSON: sink name -> external id
  state         TEXT NOT NULL CHECK (state IN ('open', 'decided')),
  outcome       TEXT,
  decided_by    TEXT,
  record_id     TEXT,
  opened_at     TEXT NOT NULL,
  closed_at     TEXT,
  organization  TEXT,
  -- A5 at the schema: a review cannot be closed anonymously. A decision
  -- that nobody's name is on is not a decision this system can represent.
  CHECK (state = 'open' OR decided_by IS NOT NULL)
);
CREATE INDEX IF NOT EXISTS rt_case ON review_task (case_id);
CREATE INDEX IF NOT EXISTS rt_state ON review_task (state, opened_at);
CREATE INDEX IF NOT EXISTS rt_org ON review_task (organization, state);
-- Finality: once a named person has decided, the task is closed for good.
-- Reopening it, reassigning it, or rewriting the dossier it was decided on
-- are all the same attack, so all three are refused at the substrate.
CREATE TRIGGER IF NOT EXISTS rt_final BEFORE UPDATE ON review_task
WHEN OLD.state = 'decided'
BEGIN SELECT RAISE(ABORT, 'a decided review is final'); END;
CREATE TRIGGER IF NOT EXISTS rt_nodelete BEFORE DELETE ON review_task
BEGIN SELECT RAISE(ABORT, 'review tasks are never deleted'); END;

-- The read model: a session plus its most recent disposition. Every field
-- is stored, none is recomputed, so the API is a projection (Def. 11).
CREATE VIEW IF NOT EXISTS pr_session_current AS
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
              WHERE x.session_id = s.session_id);
"""


def open_writer(path: str | None = None):
    """A writable connection. Handed only to Kernel service classes."""
    if use_postgres_ledger() and path is None:
        from .platform.pg_ledger import open_writer as pg_writer
        return pg_writer()
    p = path or DB_PATH
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    conn = sqlite3.connect(p, check_same_thread=False, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=30000")
    # Single-process performance knobs. Safe defaults; override via env
    # only if an operator has measured a need. cache_size is in pages
    # (negative = KiB). 64 MiB is modest for a container and keeps the
    # active holdings warm under the process-local cache.
    cache_kib = int(os.environ.get("DJ_SQLITE_CACHE_KIB", "65536"))
    conn.execute(f"PRAGMA cache_size={-abs(cache_kib)}")
    conn.execute("PRAGMA temp_store=MEMORY")
    conn.execute("PRAGMA synchronous=NORMAL")   # safe with WAL
    return conn


def open_reader(path: str | None = None):
    """A physically read-only connection (URI mode=ro on SQLite; app-level
    RO on Postgres). Non-Kernel code is handed one of these and cannot write."""
    if use_postgres_ledger() and path is None:
        from .platform.pg_ledger import open_reader as pg_reader
        return pg_reader()
    p = path or DB_PATH
    conn = sqlite3.connect(f"file:{p}?mode=ro", uri=True,
                           check_same_thread=False, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=30000")
    cache_kib = int(os.environ.get("DJ_SQLITE_CACHE_KIB", "65536"))
    conn.execute(f"PRAGMA cache_size={-abs(cache_kib)}")
    conn.execute("PRAGMA temp_store=MEMORY")
    return conn


def init_db(path: str | None = None) -> None:
    if use_postgres_ledger() and path is None:
        from .platform.pg_ledger import init_ledger
        init_ledger()
        return
    conn = open_writer(path)
    try:
        # Migrations run FIRST, and the order is load-bearing.
        #
        # CREATE TABLE IF NOT EXISTS silently does nothing when a table
        # already exists, so on an upgraded database the old tables are still
        # missing any newly added column — and the very same script then tries
        # to build an index over that column and fails with a bare
        # "no such column". Bringing existing tables up to shape before the
        # script runs is what makes an in-place upgrade work; on a fresh
        # database every migration no-ops, because there is nothing to alter.
        _migrate(conn)
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()


# Columns added after the first release, as (table, column, definition).
# Declarative on purpose: adding a column to SCHEMA and forgetting to add it
# here is the one mistake that breaks upgrades, so the two live side by side
# and ADDED_COLUMNS is checked against the live database on every boot.
ADDED_COLUMNS = (
    ("principal", "organization", "TEXT"),
    ("provision", "organization", "TEXT"),
    ("precedent_record", "organization", "TEXT"),
    ("pr_session", "organization", "TEXT"),
    ("review_task", "organization", "TEXT"),
    ("judgment_invocation", "tier", "INTEGER NOT NULL DEFAULT 0"),
    ("draft_amendment", "organization", "TEXT"),
    ("principal", "role_hint", "TEXT"),
    ("judgment_invocation", "input_tokens", "INTEGER"),
    ("judgment_invocation", "output_tokens", "INTEGER"),
    ("case_state", "organization", "TEXT"),
    ("precedent_record", "promoted_from", "TEXT"),
    # 1 Sep 2026, with Definition 7's amendment. ALTER TABLE cannot add a
    # table-level CHECK, so a database upgraded in place gets the columns and
    # not the new licensing constraint; a fresh database gets both. The
    # extension suite's upgrade check asserts the columns, and REPRODUCE.md
    # says plainly that the constraint binds fresh ledgers only.
    ("precedent_record", "admission_ground", "TEXT"),
    ("precedent_record", "class_id", "TEXT"),
)

# Indexes whose definition changed. Dropped before the schema script rebuilds
# them, because CREATE INDEX IF NOT EXISTS will not redefine an index that
# already exists under the same name.
REDEFINED_INDEXES = ("ji_cache",)


def _migrate(conn) -> None:
    """Forward-only, idempotent, and safe on a database that does not exist.

    Runs before the schema script (see init_db). Every step is guarded on
    what the live database actually has, so this is a no-op on a fresh file
    and on an already-current one.
    """
    # Views first, and unconditionally. CREATE VIEW IF NOT EXISTS is a no-op
    # against an existing view, so an upgraded database keeps serving the OLD
    # definition and any column added to a view is silently missing — which
    # surfaces later as a bare "no such column" from a query that is perfectly
    # correct against the current schema.
    #
    # Dropping every view is safe precisely because a view holds no data: it
    # is derived, and the schema script immediately rebuilds it. Doing it for
    # ALL views rather than a maintained list means the next view change is
    # covered without anyone having to remember this.
    for v in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='view'").fetchall():
        conn.execute(f"DROP VIEW IF EXISTS {v['name']}")

    changed = False
    for table, column, decl in ADDED_COLUMNS:
        have = {r["name"] for r in
                conn.execute(f"PRAGMA table_info({table})").fetchall()}
        if have and column not in have:          # empty => table not created
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {decl}")
            changed = True
    if changed:
        for name in REDEFINED_INDEXES:
            conn.execute(f"DROP INDEX IF EXISTS {name}")
    conn.commit()
