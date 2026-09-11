"""L2 Contract Kernel: the five services that carry the axioms.

Sole-writer discipline in one process: each service class owns the only
writer connection that touches its tables; everything else in the process
receives read-only connections from db.open_reader(). The Challenge Gate is
the only object that can INSERT into precedent_record (Def. 7 / CC-11), and
that is enforced by object capability, not convention: the ledger writer is
created inside the Gate's constructor and never leaves it.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import sqlite3
import threading
import uuid

from . import db, metrics
from .db import now_iso
from .judges import MAX_CANDIDATES

def _chain_key() -> bytes:
    """Prefer DJ_CHAIN_KEY; otherwise derive a process-stable key from the
    DB path so dev/default is not a fixed public string. Production MUST set
    DJ_CHAIN_KEY explicitly."""
    env = os.environ.get("DJ_CHAIN_KEY")
    if env:
        return env.encode()
    # Dev fallback: not secret across hosts, but not a published constant.
    material = ("dj-dev-chain|" + os.environ.get("DJ_DB", "/data/judiciary.db")).encode()
    return hashlib.sha256(material).digest()

CHAIN_KEY = _chain_key()


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def hash_key(api_key: str) -> str:
    return hashlib.sha256(("dj-key:" + api_key).encode()).hexdigest()


def _consteq(a: str, b: str) -> bool:
    """Constant-time string equality to avoid API-key timing oracles."""
    return hmac.compare_digest(a.encode(), b.encode())


class KernelError(Exception):
    def __init__(self, msg: str, status: int = 400, code: str | None = None):
        super().__init__(msg)
        self.status = status
        self.code = code or f"http_{status}"


# ---------------------------------------------------------------------------
# Authority Registry (A1)
# ---------------------------------------------------------------------------
class AuthorityRegistry:
    def __init__(self, path: str | None = None):
        self._w = db.open_writer(path)

    # -- principals -----------------------------------------------------
    def create_principal(self, principal_id: str, kind: str,
                         api_key: str | None = None,
                         organization: str | None = None) -> str:
        key = api_key or secrets.token_urlsafe(24)
        self._w.execute(
            "INSERT INTO principal (principal_id, kind, api_key_hash,"
            " created_at, organization) VALUES (?,?,?,?,?)",
            (principal_id, kind, hash_key(key), now_iso(), organization))
        self._w.commit()
        return key

    def authenticate(self, api_key: str) -> str | None:
        # Fetch candidates by hash, then constant-time compare to defeat
        # any residual timing difference in the DB path itself.
        target = hash_key(api_key)
        rows = self._w.execute(
            "SELECT principal_id, api_key_hash FROM principal").fetchall()
        for row in rows:
            if _consteq(row["api_key_hash"], target):
                return row["principal_id"]
        return None

    # -- branch assignments (A1) ----------------------------------------
    def grant(self, principal_id: str, branch: str, granted_by: str,
              reason: str, bootstrap: bool = False,
              valid_from: str | None = None) -> str:
        if not bootstrap and self.resolve_branch(granted_by) != "lawmakers":
            raise KernelError("grants require a Lawmaker principal", 403)
        aid = str(uuid.uuid4())
        try:
            self._w.execute(
                "INSERT INTO authority_assignment"
                " (assignment_id, principal_id, branch, valid_from, valid_to,"
                "  granted_by, grant_reason) VALUES (?,?,?,?,NULL,?,?)",
                (aid, principal_id, branch, valid_from or now_iso(),
                 granted_by, reason))
            self._w.commit()
        except sqlite3.IntegrityError as e:
            raise KernelError(str(e), 409)
        return aid

    def revoke(self, principal_id: str, revoked_by: str) -> None:
        if self.resolve_branch(revoked_by) != "lawmakers":
            raise KernelError("revocations require a Lawmaker principal", 403)
        self._w.execute(
            "UPDATE authority_assignment SET valid_to = ?"
            " WHERE principal_id = ? AND valid_to IS NULL",
            (now_iso(), principal_id))
        self._w.commit()

    def organization_of(self, principal_id: str) -> str | None:
        """The tenant a principal belongs to. NULL means platform-wide —
        an auditor or a group officer who serves every tenant."""
        r = self._w.execute(
            "SELECT organization FROM principal WHERE principal_id = ?",
            (principal_id,)).fetchone()
        return r["organization"] if r else None

    def organizations(self) -> list[dict]:
        return [dict(x) for x in self._w.execute(
            "SELECT org_id, name FROM organization ORDER BY name").fetchall()]

    def resolve_branch(self, principal_id: str,
                       at_time: str | None = None) -> str | None:
        """The A1 check, at the point of action (v3.0 §11.1)."""
        t = at_time or now_iso()
        row = self._w.execute(
            "SELECT branch FROM authority_assignment"
            " WHERE principal_id = ? AND valid_from <= ?"
            "   AND (valid_to IS NULL OR valid_to > ?)",
            (principal_id, t, t)).fetchone()
        return row["branch"] if row else None

    def require_branch(self, principal_id: str, branch: str) -> None:
        actual = self.resolve_branch(principal_id)
        if actual != branch:
            raise KernelError(
                f"principal '{principal_id}' holds branch "
                f"'{actual}', operation requires '{branch}'", 403)


# ---------------------------------------------------------------------------
# Constitution Store (A3, Definition 1)
# ---------------------------------------------------------------------------
def _materially_changed(before: dict | None, after: dict | None) -> bool:
    """Did an amendment change what a clause MEANS, or only how it reads?

    Text alone is not material: a clarification or a typo fix should not
    discard the case law built on the clause. The predicate and the absolute
    flag are material, because they change which facts the clause reaches and
    whether it can be argued with at all. The lawmakers can override this
    either way with `supersedes_precedent` on the amendment, since whether
    they were clarifying or changing is their call, not the adjudicator's.
    """
    if before is None or after is None:
        return True                       # newly added or removed outright
    return (canonical(before.get("policy") or {})
            != canonical(after.get("policy") or {})
            or bool(before.get("absolute")) != bool(after.get("absolute")))


class ConstitutionStore:
    def __init__(self, registry: AuthorityRegistry, path: str | None = None):
        self._w = db.open_writer(path)
        self._registry = registry
        # Attached after construction (see bootstrap): this store is a WRITER
        # to precedent_lifecycle_event via _supersede, so it changes which
        # holdings are active and must be able to invalidate the read cache.
        self._ledger = None

    def attach_ledger(self, ledger) -> None:
        """Give this store the reader whose cache it must keep honest.

        The Gate is not usable for this. Supersession writes its events inside
        the amendment's own transaction — which is correct, because a clause
        change and the retirement of the holdings under it must land together
        or not at all — and the Gate holds a different writer connection.
        Routing through it would deadlock on the write lock this store is
        already holding. So the invalidation happens here, after commit.
        """
        self._ledger = ledger

    @staticmethod
    def version_digest(provisions) -> str:
        """The content hash of a rulebook version.

        It is computed over exactly the four fields the `provision` table
        stores as the clause — id, text, policy and absoluteness — and over
        nothing else, so that ANY reader can recompute it from the published
        table and get the same answer. That property is the whole point of
        A3's integrity claim, and it is what CC-04 checks.

        It did not hold until 1 September 2026. `enact_version` hashed the
        provision dicts as they were handed to it, which for a bootstrap
        carried exactly those four keys and for an amendment carried an
        `organization` key as well. The two hashes therefore agreed on
        rb-000001 and disagreed on every amended version — and the defect was
        invisible because no record in the conformance corpus had ever pinned
        an amended version. The consolidation corpus put a record on
        rb-000002 and CC-04 failed the same afternoon. One projection,
        used by the writer and by the check, is the repair.
        """
        rows = []
        for p in sorted(provisions,
                        key=lambda q: (q["provision_id"],
                                       q.get("organization") or "")):
            policy = p.get("policy")
            if policy is None and p.get("policy_source") is not None:
                policy = json.loads(p["policy_source"])
            rows.append({"provision_id": p["provision_id"],
                         "text": p["text"],
                         "policy": policy,
                         "absolute": bool(p["absolute"])})
        return sha256(canonical(rows))

    def enact_version(self, provisions: list[dict], enacted_by: str,
                      amendment_id: str | None, bootstrap: bool = False) -> str:
        if not bootstrap:
            self._registry.require_branch(enacted_by, "lawmakers")
        n = self._w.execute(
            "SELECT COUNT(*) AS c FROM rulebook_version").fetchone()["c"]
        vid = f"rb-{n + 1:06d}"
        content_hash = self.version_digest(provisions)
        self._w.execute(
            "INSERT INTO rulebook_version"
            " (version_id, content_hash, enacted_at, enacted_by, amendment_id)"
            " VALUES (?,?,?,?,?)",
            (vid, content_hash, now_iso(), enacted_by, amendment_id))
        for p in provisions:
            self._w.execute(
                "INSERT INTO provision"
                " (version_id, provision_id, organization, text,"
                "  policy_source, absolute)"
                " VALUES (?,?,?,?,?,?)",
                (vid, p["provision_id"], p.get("organization"), p["text"],
                 canonical(p["policy"]), 1 if p.get("absolute") else 0))
        self._w.commit()
        return vid

    def declare_standing(self, declarations, declared_by: str,
                         at: str | None = None) -> list[str]:
        """A9: record the standing declaration as a first-class object.

        `declarations` is one dict or a list of dicts, each carrying
        `adverse_to_grants` (bool), an optional `scope` (a provision id;
        default global), and an optional `holder` naming the party that
        holds the adverse standing. The declaration is attributed and
        dated; it is append-only, and it confers nothing — whether anyone
        may contest a grant is an institutional fact this store can only
        record. Requires the lawmakers branch outside bootstrap, which is
        signalled by an explicit `at` (the ceremony predates the registry
        check the same way founding grants do).
        """
        if isinstance(declarations, dict):
            declarations = [declarations]
        if at is None:
            self._registry.require_branch(declared_by, "lawmakers")
        stamp = at or now_iso()
        ids = []
        for d in declarations:
            did = f"sd-{uuid.uuid4().hex[:12]}"
            self._w.execute(
                "INSERT INTO standing_declaration"
                " (declaration_id, scope, adverse_to_grants, holder,"
                "  declared_by, declared_at) VALUES (?,?,?,?,?,?)",
                (did, d.get("scope") or "_global",
                 1 if d.get("adverse_to_grants") else 0,
                 d.get("holder"), declared_by, stamp))
            ids.append(did)
        self._w.commit()
        return ids

    def current_version(self) -> str:
        row = self._w.execute(
            "SELECT version_id FROM rulebook_version"
            " ORDER BY enacted_at DESC, version_id DESC LIMIT 1").fetchone()
        if not row:
            raise KernelError("no rulebook enacted", 500)
        return row["version_id"]

    # -- the overlay ---------------------------------------------------
    # A constitution is a shared BASE (organization IS NULL) with per-tenant
    # OVERRIDES layered above it. A tenant clause with the same provision id
    # replaces the base clause for that tenant and nobody else.
    #
    # An override may only TIGHTEN. It may make a permissive clause absolute
    # and it may add trigger facts; it may not un-absolute a floor or remove
    # a trigger. Otherwise a tenant could opt out of a shared floor by
    # overriding it, which would make the base constitution advisory and A6
    # a suggestion.
    @staticmethod
    def _row(r) -> dict:
        return {"provision_id": r["provision_id"], "text": r["text"],
                "policy": json.loads(r["policy_source"]),
                "absolute": bool(r["absolute"]),
                "organization": r["organization"],
                "scope": "tenant" if r["organization"] else "platform"}

    def get_provision(self, version_id: str, provision_id: str,
                      org: str | None = None) -> dict:
        # org=None is PLATFORM-WIDE, not "no tenant". It means the caller
        # serves every tenant — the same reading as everywhere else in this
        # system — so it sees the whole constitution rather than only the
        # shared base.
        if org is None:
            rows = self._w.execute(
                "SELECT * FROM provision WHERE version_id = ?"
                " AND provision_id = ?",
                (version_id, provision_id)).fetchall()
        else:
            rows = self._w.execute(
                "SELECT * FROM provision WHERE version_id = ?"
                " AND provision_id = ?"
                " AND (organization IS NULL OR organization = ?)",
                (version_id, provision_id, org)).fetchall()
        if not rows:
            raise KernelError(
                f"provision {provision_id} not in {version_id}", 404)
        # Tenant override wins over base.
        rows.sort(key=lambda r: 0 if r["organization"] else 1)
        return self._row(rows[0])

    def list_provisions(self, version_id: str,
                        org: str | None = None) -> list[dict]:
        if org is None:
            rows = self._w.execute(
                "SELECT * FROM provision WHERE version_id = ?"
                " ORDER BY provision_id", (version_id,)).fetchall()
        else:
            rows = self._w.execute(
                "SELECT * FROM provision WHERE version_id = ?"
                " AND (organization IS NULL OR organization = ?)"
                " ORDER BY provision_id", (version_id, org)).fetchall()
        best: dict[str, dict] = {}
        for r in rows:
            pid = r["provision_id"]
            if pid not in best or r["organization"]:
                best[pid] = self._row(r)
        return [best[k] for k in sorted(best)]

    def check_override(self, version_id: str, provision: dict) -> None:
        """Refuse an override that loosens the shared base."""
        base = self._w.execute(
            "SELECT * FROM provision WHERE version_id = ? AND provision_id = ?"
            " AND organization IS NULL",
            (version_id, provision["provision_id"])).fetchone()
        if not base:
            return                       # a tenant-only clause overrides nothing
        pid = provision["provision_id"]
        if bool(base["absolute"]) and not provision.get("absolute"):
            raise KernelError(
                f"override of {pid} would make an absolute base provision"
                f" non-absolute; a tenant cannot opt out of a shared floor",
                422)
        base_trig = set((json.loads(base["policy_source"]) or {}).get(
            "deny_if_any") or [])
        new_trig = set((provision.get("policy") or {}).get("deny_if_any") or [])
        dropped = sorted(base_trig - new_trig)
        if dropped:
            raise KernelError(
                f"override of {pid} drops base trigger(s) {dropped}; an"
                f" override may add facts that deny, never remove them", 422)

    # -- amendments (A3: anyone proposes; only Lawmakers dispose) --------
    def file_amendment(self, proposed_by: str, origin: str, body: dict,
                       source_record: str | None = None,
                       organization: str | None = None) -> str:
        aid = str(uuid.uuid4())
        self._w.execute(
            "INSERT INTO draft_amendment"
            " (id, proposed_by, origin, source_record, body, created_at,"
            "  organization) VALUES (?,?,?,?,?,?,?)",
            (aid, proposed_by, origin, source_record, canonical(body),
             now_iso(), organization))
        self._w.commit()
        return aid

    def _supersede(self, provision_ids: list[str], by: str,
                   amendment_id: str, new_version: str) -> int:
        """Retire the holdings whose clause the legislature just rewrote.

        BOUNDED by provision, never a sweep of the whole ledger: an amendment
        to one clause has nothing to say about holdings under another, and
        invalidating everything on every enactment would reset the system to
        cold start after each legislative session — which is the opposite of
        what a precedent ledger is for.

        The record is not deleted or edited. It stops being LIVE, exactly as
        a lapsed acceptance does, and the ledger keeps saying what was
        decided and why it stopped applying.
        """
        if not provision_ids:
            return 0
        n = 0
        marks = ",".join("?" * len(provision_ids))
        rows = self._w.execute(
            f"SELECT id FROM precedent_record WHERE provision_id IN ({marks})"
            f" AND NOT EXISTS (SELECT 1 FROM precedent_lifecycle_event e"
            f"   WHERE e.record_id = precedent_record.id"
            f"     AND e.event_type = 'superseded')",
            provision_ids).fetchall()
        for r in rows:
            self._w.execute(
                "INSERT INTO precedent_lifecycle_event"
                " (record_id, event_type, payload, actor, occurred_at)"
                " VALUES (?,?,?,?,?)",
                (r["id"], "superseded",
                 canonical({"amendment_id": amendment_id,
                            "new_version": new_version,
                            "reason": "the clause this holding interpreted was"
                                      " materially amended"}),
                 by, now_iso()))
            n += 1
        return n

    def decide_amendment(self, amendment_id: str, decision: str,
                         decided_by: str) -> dict:
        self._registry.require_branch(decided_by, "lawmakers")
        row = self._w.execute("SELECT * FROM draft_amendment WHERE id = ?",
                              (amendment_id,)).fetchone()
        if not row:
            raise KernelError("amendment not found", 404)
        # Holding the lawmakers branch says WHAT you may do, not WHOSE
        # constitution you may do it to. A tenant-scoped lawmaker is a
        # lawmaker of their own company only; an unscoped one is a group
        # officer and may act for any tenant.
        mine = self._registry.organization_of(decided_by)
        if mine and row["organization"] and row["organization"] != mine:
            raise KernelError(
                f"principal '{decided_by}' is a lawmaker of '{mine}' and"
                f" cannot decide an amendment belonging to"
                f" '{row['organization']}'", 403)
        if row["status"] != "pending":
            raise KernelError("amendment already decided", 409)
        try:
            self._w.execute(
                "UPDATE draft_amendment SET status=?, decided_by=?, decided_at=?"
                " WHERE id = ?",
                (decision, decided_by, now_iso(), amendment_id))
        except sqlite3.IntegrityError as e:
            raise KernelError(str(e), 409)

        new_version = None
        superseded = 0
        enacted = False
        if decision == "adopted":
            body = json.loads(row["body"])
            provisions = {p["provision_id"]: p
                          for p in self.list_provisions(self.current_version())}
            for change in body.get("changes", []):
                pid = change["provision_id"]
                if change.get("action") == "remove":
                    provisions.pop(pid, None)
                else:
                    provisions[pid] = {
                        "provision_id": pid,
                        "text": change.get("text",
                                           provisions.get(pid, {}).get("text", "")),
                        "policy": change.get("policy",
                                             provisions.get(pid, {}).get("policy", {})),
                        "absolute": change.get(
                            "absolute",
                            provisions.get(pid, {}).get("absolute", False)),
                    }
            # Which clauses did this amendment MATERIALLY change? A typo fix
            # should not discard case law; a changed predicate must.
            before = {p["provision_id"]: p
                      for p in self.list_provisions(self.current_version())}
            declared = body.get("supersedes_precedent")
            touched = [c["provision_id"] for c in body.get("changes", [])]
            material = [pid for pid in touched
                        if _materially_changed(before.get(pid),
                                               provisions.get(pid))]
            if declared is True:
                material = touched
            elif declared is False:
                material = []

            # A proposal can be adopted without changing any rule — a
            # referral asking "should this exception become law?" carries no
            # concrete edits, and the demo's control-plane notices carry
            # none either. Enacting an identical rulebook produces an
            # identical content hash and hits the UNIQUE constraint, which
            # surfaced as a 500 on the Adopt button. Adoption is still
            # recorded; there is simply no new version to enact, and the
            # caller is told so rather than left to infer it.
            wanted = sorted(provisions.values(),
                            key=lambda p: p["provision_id"])
            current = sorted(
                self.list_provisions(self.current_version()),
                key=lambda p: p["provision_id"])
            unchanged = canonical([
                {"provision_id": p["provision_id"], "text": p["text"],
                 "policy": p["policy"], "absolute": bool(p["absolute"])}
                for p in wanted]) == canonical([
                {"provision_id": p["provision_id"], "text": p["text"],
                 "policy": p["policy"], "absolute": bool(p["absolute"])}
                for p in current])
            if unchanged:
                new_version = self.current_version()
                enacted = False
            else:
                new_version = self.enact_version(wanted, decided_by,
                                                 amendment_id)
                enacted = True
            superseded = (self._supersede(material, decided_by, amendment_id,
                                          new_version) if enacted else 0)
        self._w.commit()
        # AFTER the commit, never before. Invalidating while the transaction
        # is still open would let a concurrent reader refill the cache from
        # pre-commit state and re-cache exactly the stale rows this is meant
        # to evict.
        if superseded and self._ledger is not None:
            self._ledger.invalidate_cache()
        return {"amendment_id": amendment_id, "status": decision,
                "superseded_records": superseded,
                "enacted": enacted,
                "no_rule_change": decision == "adopted" and not enacted,
                "new_version": new_version}

    def get_amendment(self, amendment_id: str) -> sqlite3.Row | None:
        return self._w.execute("SELECT * FROM draft_amendment WHERE id = ?",
                               (amendment_id,)).fetchone()


# ---------------------------------------------------------------------------
# Contest chain (A4 evidence)
# ---------------------------------------------------------------------------
class ContestChain:
    """Hash-chained escalation history: the single-container stand-in for a
    signed Temporal workflow history. The Gate verifies the chain and tier
    coverage before admitting a tier-k record (A4 / CC-06)."""

    def __init__(self, path: str | None = None):
        self._w = db.open_writer(path)

    def append(self, case_id: str, tier: int, actor: str, grounds: str) -> str:
        prev = self._w.execute(
            "SELECT chain_hash FROM contest_event WHERE case_id = ?"
            " ORDER BY seq DESC LIMIT 1", (case_id,)).fetchone()
        prev_hash = prev["chain_hash"] if prev else "genesis"
        ts = now_iso()
        msg = f"{prev_hash}|{case_id}|{tier}|{actor}|{ts}".encode()
        chain_hash = hmac.new(CHAIN_KEY, msg, hashlib.sha256).hexdigest()
        self._w.execute(
            "INSERT INTO contest_event"
            " (case_id, tier, actor, grounds, ts, prev_hash, chain_hash)"
            " VALUES (?,?,?,?,?,?,?)",
            (case_id, tier, actor, grounds, ts, prev_hash, chain_hash))
        self._w.commit()
        return chain_hash

    def verify_exhaustion(self, case_id: str, k: int = 4) -> bool:
        rows = self._w.execute(
            "SELECT * FROM contest_event WHERE case_id = ? ORDER BY seq",
            (case_id,)).fetchall()
        prev_hash = "genesis"
        tiers = set()
        for r in rows:
            msg = (f"{prev_hash}|{r['case_id']}|{r['tier']}|{r['actor']}|"
                   f"{r['ts']}").encode()
            if hmac.new(CHAIN_KEY, msg, hashlib.sha256).hexdigest() \
                    != r["chain_hash"]:
                return False
            prev_hash = r["chain_hash"]
            tiers.add(r["tier"])
        return tiers >= set(range(1, k))          # tiers 1..k-1 all contested


# ---------------------------------------------------------------------------
# Judgment Provenance Service (P3) — the sole caller of judges
# ---------------------------------------------------------------------------
class JudgmentProvenance:
    def __init__(self, judges, path: str | None = None):
        self._w = db.open_writer(path)
        # {tier: judge}. A bare judge is accepted and used at every tier so
        # existing callers keep working.
        self.judges = judges if isinstance(judges, dict) else {}
        self.judge = judges if not isinstance(judges, dict) else \
            judges[min(judges)]

    def for_tier(self, tier: int):
        return self.judges.get(tier, self.judge)

    def distinguish(self, batch_id: str, candidate: dict, case: dict,
                    tier: int = 0) -> dict:
        """Cache-first distinguish verdict, fully recorded (P3).

        The cache key includes the tier. It has to: a verdict reached at tier
        1 is not evidence about what tier 2 would say, and reusing it made
        escalation a no-op that also skipped the pivotal-quorum path.
        """
        judge = self.for_tier(tier)
        cand_hash, case_hash = candidate["content_hash"], case["case_hash"]
        jv, pv = judge.version, judge.prompt_version
        cached = self._w.execute(
            "SELECT verdict, degraded FROM judgment_invocation"
            " WHERE candidate_hash=? AND case_hash=? AND judge_version=?"
            "   AND prompt_version=? AND tier=? AND from_cache=0"
            "   AND degraded=0",
            (cand_hash, case_hash, jv, pv, tier)).fetchone()
        if cached:
            verdict = json.loads(cached["verdict"])
            self._record(batch_id, cand_hash, case_hash, verdict,
                         latency_ms=0, from_cache=True, degraded=False,
                         tier=tier, judge=judge)
            return {**verdict, "degraded": False, "from_cache": True}

        verdict, latency_ms, degraded = judge.distinguish(candidate, case)
        self._record(batch_id, cand_hash, case_hash, verdict,
                     latency_ms=latency_ms, from_cache=False,
                     degraded=degraded, tier=tier, judge=judge)
        return {**verdict, "degraded": degraded, "from_cache": False}

    # -- concurrent distinguishing ------------------------------------
    # Every candidate in a batch is an independent question: "does THIS
    # precedent's holding rest on something the present case lacks?" Nothing
    # about one answer informs another, and the ordering that follows runs
    # only once all of them are back. Asking them one at a time is an
    # accident of how the loop was written, and with a live model it is the
    # difference between seconds and minutes.
    #
    # What is NOT parallelised, deliberately:
    #   * the cache lookup and the _record write, which share one SQLite
    #     writer. Doing those on worker threads would serialise on the write
    #     lock anyway, and would interleave rows non-deterministically.
    #   * cases. Case n can be bound by a precedent case n-1 wrote, so
    #     concurrency there changes what the ledger says, not just how fast
    #     it is said.
    #
    # Results are recorded in the ORIGINAL candidate order, so the ledger is
    # byte-identical to a sequential run.
    def distinguish_many(self, batch_id: str, candidates: list, case: dict,
                         tier: int = 0) -> dict:
        from .judges import judge_concurrency

        out: dict = {}
        judge = self.for_tier(tier)
        jv, pv = judge.version, judge.prompt_version
        case_hash = case["case_hash"]

        # 1. Serve what the cache already knows, on this thread, in order.
        pending = []
        for cand in candidates:
            ch = cand["content_hash"]
            row = self._w.execute(
                "SELECT verdict FROM judgment_invocation"
                " WHERE candidate_hash=? AND case_hash=? AND judge_version=?"
                "   AND prompt_version=? AND tier=? AND from_cache=0"
                "   AND degraded=0", (ch, case_hash, jv, pv, tier)).fetchone()
            if row:
                v = json.loads(row["verdict"])
                self._record(batch_id, ch, case_hash, v, latency_ms=0,
                             from_cache=True, degraded=False, tier=tier,
                             judge=judge)
                out[cand["id"]] = {**v, "degraded": False, "from_cache": True}
            else:
                pending.append(cand)

        if not pending:
            return out

        width = judge_concurrency()
        if width <= 1 or len(pending) == 1:
            for cand in pending:
                out[cand["id"]] = self.distinguish(batch_id, cand, case, tier)
            return out

        # 2. Ask the rest concurrently. Only judge.distinguish runs on a
        #    worker; it touches no database.
        from concurrent.futures import ThreadPoolExecutor
        answers: dict = {}
        with ThreadPoolExecutor(max_workers=min(width, len(pending))) as pool:
            futures = {pool.submit(judge.distinguish, c, case): c
                       for c in pending}
            for fut, cand in futures.items():
                try:
                    answers[cand["id"]] = fut.result()
                except Exception as e:                        # noqa: BLE001
                    # A judge that raises is a degradation, not a crash: the
                    # sequential path treats it the same way (§12).
                    answers[cand["id"]] = (
                        {"distinguished": False,
                         "grounds": f"DEGRADED: {type(e).__name__}: {e}"},
                        0, True)

        # 3. Record on this thread, in the order the candidates were given.
        for cand in pending:
            verdict, latency_ms, degraded = answers[cand["id"]]
            self._record(batch_id, cand["content_hash"], case_hash, verdict,
                         latency_ms=latency_ms, from_cache=False,
                         degraded=degraded, tier=tier, judge=judge)
            out[cand["id"]] = {**verdict, "degraded": degraded,
                               "from_cache": False}
        return out

    def quorum(self, batch_id: str, candidate: dict, case: dict,
               tier: int = 0) -> dict:
        """N-sample quorum for pivotal verdicts; majority stands. The width
        is per-tier, so a higher rung can deliberate harder as well as think
        with a larger model."""
        from .judges import quorum_width
        judge = self.for_tier(tier)
        width = quorum_width(tier) if tier else 3
        # The samples are independent by construction — that is what makes a
        # quorum a quorum — so they go out together. Concurrency changes only
        # how long the vote takes, never its outcome: the tally below is over
        # a set, and a set has no order.
        from .judges import judge_concurrency
        votes, degraded_any = [], False
        if judge_concurrency() > 1 and width > 1:
            from concurrent.futures import ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=width) as pool:
                results = list(pool.map(
                    lambda _: judge.distinguish(candidate, case),
                    range(width)))
        else:
            results = [judge.distinguish(candidate, case)
                       for _ in range(width)]
        for v, latency_ms, degraded in results:
            votes.append(v)
            degraded_any = degraded_any or degraded
        yes = sum(1 for v in votes if v["distinguished"])
        verdict = {"distinguished": yes * 2 >= width,
                   "grounds": "; ".join(v["grounds"] for v in votes[:1]),
                   "quorum_disagreement": 0 < yes < width}
        self._record(batch_id, candidate["content_hash"], case["case_hash"],
                     verdict, latency_ms=0, from_cache=False,
                     degraded=degraded_any, quorum_votes=votes, tier=tier,
                     judge=judge)
        return {**verdict, "degraded": degraded_any, "from_cache": False}

    def propose_premise(self, batch_id: str, case: dict, tier: int,
                        outcome: str, provision: str, reason: str) -> dict:
        """Which facts the holding rested on. Recorded like any other
        judgment, so the dossier shows who narrowed the holding and why."""
        judge = self.for_tier(tier)
        fn = getattr(judge, "propose_premise", None)
        if fn is None:
            return {"premise": sorted(case["facts"]), "grounds": "mechanical",
                    "degraded": False}
        premise, grounds, latency_ms, degraded = fn(
            case, outcome, provision, reason)
        verdict = {"premise": premise, "grounds": grounds}
        self._record(batch_id, "premise:" + case["case_hash"],
                     case["case_hash"], verdict, latency_ms=latency_ms,
                     from_cache=False, degraded=degraded, tier=tier,
                     judge=judge, kind="premise")
        return {**verdict, "degraded": degraded}

    def _record(self, batch_id, cand_hash, case_hash, verdict, latency_ms,
                from_cache, degraded, quorum_votes=None, tier=0, judge=None,
                kind="distinguish"):
        try:
            self._w.execute(
                "INSERT INTO judgment_invocation"
                " (id, batch_id, kind, candidate_hash, case_hash, tier,"
                "  judge_version, prompt_version, params, verdict,"
                "  quorum_votes, latency_ms, input_tokens, output_tokens,"
                "  from_cache, degraded, invoked_at)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (str(uuid.uuid4()), batch_id, kind, cand_hash,
                 case_hash, tier, (judge or self.judge).version,
                 (judge or self.judge).prompt_version,
                 canonical((judge or self.judge).params), canonical(verdict),
                 canonical(quorum_votes) if quorum_votes else None,
                 latency_ms,
                 # Only a call that actually went out has usage. A cache hit
                 # costs nothing and must not be attributed a cost.
                 *((None, None) if from_cache else
                   getattr(judge or self.judge, "last_usage", (None, None))),
                 1 if from_cache else 0, 1 if degraded else 0,
                 now_iso()))
            self._w.commit()
        except sqlite3.IntegrityError:
            # Duplicate non-cache row for the same key: a concurrent write
            # already recorded this verdict; the cache index did its job.
            self._w.rollback()


# ---------------------------------------------------------------------------
# Active-holdings cache (process-local, coherent with the sole writer)
# ---------------------------------------------------------------------------
# Under the single-container constraint the only safe acceleration for
# retrieve() is a process-local cache of the active (non-lapsed,
# non-superseded) rows for each provision. The Challenge Gate is the sole
# writer to the ledger, so every path that changes the active set
# (admit, lifecycle emission that marks lapsed/superseded) calls
# invalidate(). Between those events the cache is exact.
#
# Disabled with DJ_HOLDINGS_CACHE=0. Default on.
# ---------------------------------------------------------------------------
_HOLDINGS_CACHE_ON = os.environ.get("DJ_HOLDINGS_CACHE", "1") != "0"


class ActiveHoldingsCache:
    """Thread-safe, provision-keyed cache of active holdings.

    Key is (provision_id, org_key) where org_key is the tenant string or
    the sentinel '' for the unscoped / platform pool. Values are lists of
    already-materialised row dicts ready for Jaccard scoring.
    """

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._data: dict[tuple[str, str], list[dict]] = {}
        self._generation = 0

    def get(self, provision_id: str, org_key: str) -> list[dict] | None:
        with self._lock:
            hit = self._data.get((provision_id, org_key))
            if hit is not None:
                metrics.inc("holdings_cache_hit")
                return list(hit)          # defensive copy
            metrics.inc("holdings_cache_miss")
            return None

    def put(self, provision_id: str, org_key: str, rows: list[dict]) -> None:
        with self._lock:
            self._data[(provision_id, org_key)] = list(rows)
            metrics.set_gauge("holdings_cache_entries", len(self._data))

    def invalidate(self, provision_id: str | None = None) -> None:
        """Drop one provision's entries, or the whole cache.

        Called from the Gate after every admit and after lifecycle events
        that change lapsed/superseded state. Broad invalidation is cheap
        relative to a wrong candidate set.
        """
        with self._lock:
            if provision_id is None:
                self._data.clear()
            else:
                dead = [k for k in self._data if k[0] == provision_id]
                for k in dead:
                    del self._data[k]
            self._generation += 1
            metrics.set_gauge("holdings_cache_entries", len(self._data))
            metrics.inc("holdings_cache_invalidate")

    def stats(self) -> dict:
        with self._lock:
            return {
                "enabled": _HOLDINGS_CACHE_ON,
                "entries": len(self._data),
                "generation": self._generation,
            }


# ---------------------------------------------------------------------------
# Precedent Ledger reader + Challenge Gate (sole writer)
# ---------------------------------------------------------------------------
class LedgerReader:
    """Read-only ledger access for adjudication and audit (physically
    read-only connection: the §11.2 ledger_reader role)."""

    def __init__(self, path: str | None = None):
        self._r = db.open_reader(path)
        self.cache = ActiveHoldingsCache()

    def invalidate_cache(self, provision_id: str | None = None) -> None:
        self.cache.invalidate(provision_id)

    def _load_active(self, provision_id: str, org: str | None) -> list:
        """SQL load of active holdings for one provision / tenant pool."""
        if org:
            return self._r.execute(
                "SELECT * FROM record_effective WHERE provision_id = ?"
                " AND lapsed = 0 AND superseded = 0 AND (organization = ?"
                "   OR (organization IS NULL AND is_acceptance = 0))",
                (provision_id, org)).fetchall()
        return self._r.execute(
            "SELECT * FROM record_effective WHERE provision_id = ?"
            " AND lapsed = 0 AND superseded = 0",
            (provision_id,)).fetchall()

    def retrieve(self, case: dict, theta: float, log_writer=None,
                 org: str | None = None,
                 max_candidates: int | None = None) -> list[dict]:
        """Candidates for this case.

        With a tenant, the pool is that tenant's own holdings PLUS shared
        platform holdings — never another tenant's, and never anyone else's
        risk acceptance. An acceptance is not an interpretation of what a
        clause means; it is one organisation declaring it will bear a risk,
        and it must bind nobody else. Interpretations propagate; dispensations
        do not.

        Uses a process-local active-holdings cache (see ActiveHoldingsCache)
        so repeated adjudication against the same provision does not re-scan
        the view. Jaccard scoring and the hard candidate cap still run in
        Python; the cache only removes repeated SQL work.
        """
        metrics.inc("retrieve_calls")
        provision_id = case["provision_id"]
        org_key = org or ""
        cap = max_candidates if max_candidates is not None else MAX_CANDIDATES

        rows = None
        if _HOLDINGS_CACHE_ON:
            rows = self.cache.get(provision_id, org_key)
        if rows is None:
            raw = self._load_active(provision_id, org)
            # Materialise once so the cache holds plain dicts, not Row objects
            # that become invalid when the connection is used again.
            rows = [dict(r) for r in raw]
            if _HOLDINGS_CACHE_ON:
                self.cache.put(provision_id, org_key, rows)
            metrics.inc("retrieve_sql_loads")

        case_facts = set(case["facts"])
        out = []
        examined = 0
        for r in rows:
            examined += 1
            rec_facts = set(json.loads(r["facts"]))
            union = case_facts | rec_facts
            j = (len(case_facts & rec_facts) / len(union)) if union else 0.0
            if j >= theta:
                out.append(self._row_to_dict(r, similarity=j))
        out.sort(key=lambda d: (-d["similarity"], d["id"]))
        metrics.inc("retrieve_rows_examined", examined)
        metrics.inc("retrieve_candidates_returned", len(out[:cap]))
        return out[:cap]

    def get(self, record_id: str) -> dict | None:
        r = self._r.execute("SELECT * FROM record_effective WHERE id = ?",
                            (record_id,)).fetchone()
        return self._row_to_dict(r) if r else None

    def lapsed_similar_acceptance(self, case: dict, theta: float) -> dict | None:
        """A7 renewal guard input: the most recent lapsed acceptance
        materially similar to this case."""
        rows = self._r.execute(
            "SELECT * FROM record_effective WHERE provision_id = ?"
            " AND is_acceptance = 1 AND lapsed = 1"
            " ORDER BY resolved_at DESC", (case["provision_id"],)).fetchall()
        case_facts = set(case["facts"])
        for r in rows:
            rec_facts = set(json.loads(r["facts"]))
            union = case_facts | rec_facts
            if union and len(case_facts & rec_facts) / len(union) >= theta:
                return self._row_to_dict(r)
        return None

    # -- the register: census and pages, for auditing a ledger too large
    #    to hold in memory ------------------------------------------------
    REGISTER_COLUMNS = (
        "id, provision_id, organization, authority_tier,"
        " resolving_principal, resolved_at, interpretation, controlling_id,"
        " controlling_state, is_acceptance, expiry, lapsed")

    def census(self, provision: str | None = None,
               org: str | None = None) -> dict:
        """Every count the register needs, in one aggregate.

        Counting by loading rows is fine at demo scale and quietly quadratic
        after that. These four numbers are also the filter controls, so they
        are computed together and scoped by the same provision filter the
        list uses — filter to one provision and the census describes that
        provision rather than lying about the whole ledger.
        """
        clauses, args = [], []
        if provision:
            clauses.append("provision_id = ?")
            args.append(provision)
        if org:
            clauses.append("organization = ?")
            args.append(org)
        where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
        r = self._r.execute(
            "SELECT COUNT(*) AS records,"
            " COALESCE(SUM(CASE WHEN is_acceptance = 0 THEN 1 ELSE 0 END), 0)"
            "   AS holdings,"
            " COALESCE(SUM(CASE WHEN is_acceptance = 1 AND lapsed = 0"
            "   THEN 1 ELSE 0 END), 0) AS live_acceptances,"
            " COALESCE(SUM(lapsed), 0) AS lapsed,"
            " COUNT(DISTINCT provision_id) AS provisions"
            f" FROM record_effective{where}", args).fetchone()
        return dict(r)

    def register(self, limit: int = 50, cursor: tuple | None = None,
                 status: str | None = None, provision: str | None = None,
                 org: str | None = None) -> dict:
        """One page of the ledger, newest first.

        Keyset pagination on (resolved_at, id) rather than OFFSET: an
        immutable append-only ledger is exactly the case where OFFSET degrades
        as the table grows, and a keyset cursor is also stable under
        concurrent admission — a record written while an auditor pages
        through cannot shift rows onto a page they already read.
        """
        where, args = [], []
        if status == "lapsed":
            where.append("lapsed = 1")
        elif status == "acceptance":
            where.append("is_acceptance = 1 AND lapsed = 0")
        elif status == "holding":
            where.append("is_acceptance = 0")
        if provision:
            where.append("provision_id = ?")
            args.append(provision)
        if org:
            # Applied in the QUERY, not to results already fetched. A tenant
            # filter applied afterwards is a display convention; applied here
            # it is an access control.
            #
            # Note this is deliberately STRICTER than retrieval or the
            # activity feed, which also admit platform-wide rows. Those
            # answer "what may I cite" and "what happened that concerns me";
            # the register answers "whose holdings are these", and platform
            # law is not this tenant's. EX-22 and EX-23 pin that reading.
            where.append("organization = ?")
            args.append(org)
        if cursor:
            ts, cid = cursor
            where.append("(resolved_at < ? OR (resolved_at = ? AND id < ?))")
            args += [ts, ts, cid]
        sql = f"SELECT {self.REGISTER_COLUMNS} FROM record_effective"
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY resolved_at DESC, id DESC LIMIT ?"
        args.append(limit + 1)          # one extra row answers "is there more"
        rows = [dict(r) for r in self._r.execute(sql, args).fetchall()]
        more = len(rows) > limit
        rows = rows[:limit]
        for r in rows:
            r["interpretation"] = json.loads(r["interpretation"])
        nxt = ((rows[-1]["resolved_at"], rows[-1]["id"])
               if more and rows else None)
        return {"rows": rows, "next": nxt, "more": more}

    def lifecycle(self, record_id: str) -> list[dict]:
        rows = self._r.execute(
            "SELECT * FROM precedent_lifecycle_event WHERE record_id = ?"
            " ORDER BY seq", (record_id,)).fetchall()
        return [dict(r) for r in rows]

    def judgments(self, batch_id: str) -> list[dict]:
        rows = self._r.execute(
            "SELECT * FROM judgment_invocation WHERE batch_id = ?"
            " ORDER BY invoked_at", (batch_id,)).fetchall()
        return [dict(r) for r in rows]

    @staticmethod
    def _row_to_dict(r, similarity: float | None = None) -> dict:
        """Accept a sqlite3.Row or a plain dict (cache stores the latter)."""
        d = dict(r)
        for f in ("facts", "premise", "interpretation", "conditions",
                  "consulted_ids", "tie_members", "scope"):
            v = d.get(f)
            if v is not None and isinstance(v, str):
                d[f] = json.loads(v)
        if similarity is not None:
            d["similarity"] = similarity
        return d

    def standing_in_force(self, provision_id: str, at: str) -> dict | None:
        """A9: the standing declaration in force at time `at` for a
        provision — the most recent declaration not later than `at`, a
        provision-scoped declaration taking precedence over the global
        one. None means no declaration was in force, which is the state
        the A9 conformance check (CC-17) refuses."""
        for scope in (provision_id, "_global"):
            row = self._r.execute(
                "SELECT * FROM standing_declaration WHERE scope = ?"
                " AND declared_at <= ?"
                " ORDER BY declared_at DESC, declaration_id DESC LIMIT 1",
                (scope, at)).fetchone()
            if row:
                return {"scope": row["scope"],
                        "adverse_to_grants": bool(row["adverse_to_grants"]),
                        "holder": row["holder"],
                        "declared_by": row["declared_by"],
                        "declared_at": row["declared_at"]}
        return None

    def rebuild(self, record_id: str) -> dict:
        """Definition 11 / Theorem 2: reads fields, recomputes nothing
        (CC-13 is the absence of any judge or retrieval call here). The
        provenance also carries the A9 standing declaration in force at
        the record's own resolved_at, so every audit export discloses
        whether any party held contest standing adverse to grants when
        the decision was taken."""
        rec = self.get(record_id)
        if not rec:
            raise KernelError("record not found", 404)
        return {
            "record_id": rec["id"],
            "rules": [rec["provision_id"]],
            "consulted": rec["consulted_ids"],
            "controlling": rec["controlling_id"],
            "controlling_state": rec["controlling_state"],
            "tie_members": rec.get("tie_members"),
            "resolving_authority": rec["resolving_principal"],
            "authority_tier": rec["authority_tier"],
            "rationale": rec["rationale_text"],
            "rulebook_version": rec["rulebook_version"],
            "resolved_at": rec["resolved_at"],
            "degraded": bool(rec["degraded"]),
            "standing_declaration": self.standing_in_force(
                rec["provision_id"], rec["resolved_at"]),
        }


class ChallengeGate:
    def promote(self, record_id: str, by: str) -> str:
        """Ratify a tenant holding as generally applicable — Stage 3.

        Promotion is LEGISLATIVE and never automatic. If a local
        interpretation became everyone's law merely by being filed, authority
        would have transferred without anyone exercising it, which is the
        failure this architecture exists to prevent. So it requires the
        lawmakers branch, and it writes a NEW platform-scope record rather
        than mutating the original: the ledger is immutable, and the tenant's
        own holding stays theirs.

        Acceptances are refused. There is no reading of "we chose to bear
        this" that generalises to anyone else.
        """
        self._registry.require_branch(by, "lawmakers")
        src = self.__w.execute(
            "SELECT * FROM precedent_record WHERE id = ?",
            (record_id,)).fetchone()
        if not src:
            raise KernelError("record not found", 404)
        if src["is_acceptance"]:
            raise KernelError(
                "a risk acceptance cannot be promoted: it records what one"
                " organisation was willing to bear, not what a clause means",
                422)
        if src["organization"] is None:
            raise KernelError("this holding is already platform law", 409)
        if self.__w.execute(
                "SELECT id FROM precedent_record WHERE promoted_from = ?",
                (record_id,)).fetchone():
            raise KernelError("this holding has already been promoted", 409)

        return self.admit({
            "artifact_version": "1.0",
            "case": {"case_id": src["case_id"],
                     "case_hash": sha256(f"promote:{record_id}"),
                     "provision_id": src["provision_id"],
                     "rulebook_version": src["rulebook_version"],
                     "facts": json.loads(src["facts"]),
                     "author": by, "organization": None},
            "tier": src["authority_tier"], "resolving_principal": by,
            "retrieval": {"theta": 0.0, "snapshot_at": now_iso(),
                          "candidates": []},
            "judgments": {"batch_id": src["judgment_batch_id"],
                          "verdicts": []},
            # Bound to the holding it ratifies: the platform record says the
            # same thing the tenant record said, and cites it as its source.
            "ordering": {"keys_applied": [], "controlling_state": "bound",
                         "controlling_id": record_id, "tie_members": None},
            "decision": {
                "interpretation": json.loads(src["interpretation"]),
                "conditions": (json.loads(src["conditions"])
                               if src["conditions"] else None),
                "premise": json.loads(src["premise"]),
                "rationale_text": (
                    f"Promoted to platform law by {by}: the holding of"
                    f" {record_id[:8]} was ratified as generally applicable."),
                "scope": {}, "scope_level": "platform",
                "is_acceptance": False},
            "degradations": [], "resolved_at": now_iso(),
        }, promoted_from=record_id)

    def _org_of(self, provision_id: str, version_id: str) -> str | None:
        """Which tenant owns the clause this record interprets."""
        r = self.__w.execute(
            "SELECT organization FROM provision"
            " WHERE version_id=? AND provision_id=?",
            (version_id, provision_id)).fetchone()
        return r["organization"] if r else None

    """Sole writer to the Precedent Ledger (Def. 7). The ledger writer
    connection is created here and never escapes this object."""

    def __init__(self, registry: AuthorityRegistry, chain: ContestChain,
                 constitution: ConstitutionStore, path: str | None = None,
                 ledger: "LedgerReader | None" = None):
        self.__w = db.open_writer(path)          # name-mangled: capability
        self._registry = registry
        self._chain = chain
        self._constitution = constitution
        # Optional back-reference so admit / lifecycle can keep the
        # process-local active-holdings cache coherent. The Gate remains
        # the sole writer; the ledger is only asked to drop cached rows.
        self._ledger = ledger

    def admit(self, artifact: dict, promoted_from: str | None = None,
              admission_ground: str | None = None,
              class_id: str | None = None) -> str:
        a = artifact
        # 1. Depth (Definition 7, as amended 1 Sep 2026)
        #
        # Clause (i) is unchanged and is the ordinary route: only depth >= 2 is
        # admissible, because only a contested-and-resolved-above-first case
        # becomes law. Clause (ii) admits ONE other thing — the designated
        # representative of a consolidation class — and it is admitted at first
        # instance, which is why the bar had to become conditional rather than
        # flat. It is not a relaxation of the bar for anybody else: the ground
        # must be named, the class artefact must exist, and the schema refuses
        # the row otherwise (PRB-3, PRB-3b, PRB-11, PRB-12).
        consolidated = admission_ground == "consolidation"
        if consolidated:
            if not class_id:
                raise KernelError(
                    "Def.7(ii): a consolidated admission must name its class",
                    422)
            if a["tier"] != 1:
                raise KernelError(
                    "Def.7(ii): a consolidated record is written at first"
                    " instance", 422)
            if not self.__w.execute(
                    "SELECT 1 FROM consolidation_class WHERE class_id=?",
                    (class_id,)).fetchone():
                raise KernelError(
                    f"Def.7(ii): no class artefact {class_id}", 422)
        elif a["tier"] < 2:
            raise KernelError("Def.7: only depth >= 2 is admissible", 422)
        # 2. Authority at resolved_at (A1 / CC-02)
        # A promotion is a LEGISLATIVE act — ratifying a tenant's reading as
        # generally applicable — so it needs the lawmakers branch, not the
        # judicial one. Everything else about the record is checked exactly
        # as usual; the ratifier gains no adjudicative authority by doing it.
        need = ("lawmakers" if promoted_from else
                "risk_owner" if a["tier"] == 4 else "judges")
        actual = self._registry.resolve_branch(
            a["resolving_principal"], a["resolved_at"])
        if actual != need:
            raise KernelError(
                f"resolving principal held '{actual}', need '{need}'", 403)
        # 3. Exhaustion, tier 4 only (A4 / CC-06). A promoted holding
        # inherits the tier of the holding it ratifies and was already
        # exhausted when that one was admitted.
        if a["tier"] == 4 and not promoted_from and not \
                self._chain.verify_exhaustion(
                a["case"]["case_id"]):
            raise KernelError(
                "A4: tier-k admission requires verified contest at every"
                " automated tier", 422)
        # 4. Completeness (A5)
        d = a["decision"]
        for field, msg in (
            (a.get("judgments", {}).get("batch_id"), "judgment batch"),
            (d.get("rationale_text"), "rationale"),
            (d.get("premise") is not None or None, "premise"),
            (a.get("ordering", {}).get("controlling_state"), "controlling_state"),
        ):
            if not field:
                raise KernelError(f"A5: artifact missing {msg}", 422)
        o = a["ordering"]
        if (o["controlling_state"] == "bound") != bool(o.get("controlling_id")):
            raise KernelError("A5: controlling_state/id inconsistent", 422)
        is_acceptance = bool(d.get("is_acceptance"))
        if is_acceptance and not d.get("expiry"):
            raise KernelError("A7: acceptances carry a mandatory expiry", 422)
        # 5. The premise is a claim about THIS case's facts (Def. 8). A
        # proposed premise may narrow the holding; it may not invent a fact
        # the case never had, because every future distinguishing verdict is
        # computed against it.
        stray = sorted(set(d["premise"]) - set(a["case"]["facts"]))
        if stray:
            raise KernelError(
                f"Def.8: premise contains facts absent from the case:"
                f" {stray}", 422)

        content_hash = sha256(canonical(a))
        # 6. Idempotency
        existing = self.__w.execute(
            "SELECT id FROM precedent_record WHERE content_hash = ?",
            (content_hash,)).fetchone()
        if existing:
            return existing["id"]

        rid = str(uuid.uuid4())
        try:
            self.__w.execute("BEGIN")
            self.__w.execute(
                "INSERT INTO precedent_record"
                " (id, organization, content_hash, case_id, provision_id,"
                "  rulebook_version,"
                "  facts, premise, interpretation, conditions, authority_tier,"
                "  admission_ground, class_id,"
                "  resolving_principal, consulted_ids, controlling_id,"
                "  controlling_state, tie_members, rationale_text,"
                "  judgment_batch_id, scope, scope_level, is_acceptance,"
                "  expiry, renews_record, promoted_from, resolved_at,"
                "  degraded)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,"
                "         ?,?)",
                # The tenant comes from the CASE. With a shared base
                # constitution a provision may belong to nobody, so the
                # clause can no longer name the ledger a holding joins; the
                # case can, and it was fixed at submission.
                (rid, a["case"].get("organization")
                 or self._org_of(a["case"]["provision_id"],
                                 a["case"]["rulebook_version"]),
                 content_hash, a["case"]["case_id"],
                 a["case"]["provision_id"], a["case"]["rulebook_version"],
                 canonical(a["case"]["facts"]), canonical(d["premise"]),
                 canonical(d["interpretation"]),
                 canonical(d.get("conditions")) if d.get("conditions") else None,
                 a["tier"],
                 # The ground is on the record, not in configuration. That is
                 # what lets CC-21 and CC-22 be computed from a released
                 # ledger by a reader who has never seen the pipeline.
                 "consolidation" if consolidated else "contest",
                 class_id if consolidated else None,
                 a["resolving_principal"],
                 canonical([c["record_id"]
                            for c in a["retrieval"]["candidates"]]),
                 o.get("controlling_id"), o["controlling_state"],
                 canonical(o["tie_members"]) if o.get("tie_members") else None,
                 d["rationale_text"], a["judgments"]["batch_id"],
                 canonical(d.get("scope", {})), d.get("scope_level", "org"),
                 1 if is_acceptance else 0, d.get("expiry"),
                 d.get("renews_record"), promoted_from, a["resolved_at"],
                 1 if a.get("degradations") else 0))
            if is_acceptance:
                # 5. A7: referral emitted transactionally with admission.
                ref_id = str(uuid.uuid4())
                self.__w.execute(
                    "INSERT INTO draft_amendment"
                    " (id, proposed_by, origin, source_record, body,"
                    "  created_at, organization) VALUES (?,?,?,?,?,?,?)",
                    (ref_id, a["resolving_principal"],
                     "risk_acceptance_referral", rid,
                     canonical({"question": "should this exception become law",
                                "provision_id": a["case"]["provision_id"],
                                "acceptance": rid,
                                "changes": []}),
                     now_iso(),
                     # The referral belongs to the tenant whose clause was
                     # waived; without this a company could not see the
                     # referrals raised by its own expiring waivers.
                     self._org_of(a["case"]["provision_id"],
                                  a["case"]["rulebook_version"])))
                self.__w.execute(
                    "INSERT INTO precedent_lifecycle_event"
                    " (record_id, event_type, payload, actor, occurred_at)"
                    " VALUES (?,?,?,?,?)",
                    (rid, "referral_emitted",
                     canonical({"amendment_id": ref_id}),
                     "challenge_gate", now_iso()))
                if d.get("renews_record"):
                    self.__w.execute(
                        "INSERT INTO precedent_lifecycle_event"
                        " (record_id, event_type, payload, actor, occurred_at)"
                        " VALUES (?,?,?,?,?)",
                        (d["renews_record"], "renewed_by",
                         canonical({"successor": rid}),
                         "challenge_gate", now_iso()))
            elif d.get("renews_record"):
                # An ordinary holding citing the holding it supersedes.
                # The append-only Store has no overruling operation, so the
                # citation is the overruling act and this event is its
                # record (Sect. 4.6, express supersession).
                self.__w.execute(
                    "INSERT INTO precedent_lifecycle_event"
                    " (record_id, event_type, payload, actor, occurred_at)"
                    " VALUES (?,?,?,?,?)",
                    (d["renews_record"], "displaced_by",
                     canonical({"successor": rid}),
                     "challenge_gate", now_iso()))
            self.__w.execute("COMMIT")
        except sqlite3.IntegrityError as e:
            self.__w.execute("ROLLBACK")
            raise KernelError(f"ledger constraint: {e}", 422)
        # Active set changed: drop the provision's cache entries so the
        # next retrieve sees the new holding.
        if self._ledger is not None:
            pid = (a.get("case") or {}).get("provision_id")
            self._ledger.invalidate_cache(pid)
        metrics.inc("gate_admits")
        return rid

    # Lifecycle events pass through the Gate's writer too: the ledger and
    # its event log share one sole writer.
    def emit_lifecycle(self, record_id: str, event_type: str, payload: dict,
                       actor: str) -> None:
        self.__w.execute(
            "INSERT INTO precedent_lifecycle_event"
            " (record_id, event_type, payload, actor, occurred_at)"
            " VALUES (?,?,?,?,?)",
            (record_id, event_type, canonical(payload), actor, now_iso()))
        self.__w.commit()
        # Lapse / supersession change which rows are active. We do not
        # always know the provision_id here without an extra read, so
        # invalidate the whole cache — it is process-local and cheap to
        # refill on the next retrieve.
        if event_type in ("lapsed", "superseded", "referral_adopted",
                          "referral_rejected") and self._ledger is not None:
            self._ledger.invalidate_cache()
        metrics.inc("gate_lifecycle_events")

    def log_retrieval(self, case_id: str, provision_id: str, theta: float,
                      n_candidates: int) -> None:
        self.__w.execute(
            "INSERT INTO retrieval_log"
            " (id, case_id, provision_id, theta, candidates, snapshot_at)"
            " VALUES (?,?,?,?,?,?)",
            (str(uuid.uuid4()), case_id, provision_id, theta, n_candidates,
             now_iso()))
        self.__w.commit()
