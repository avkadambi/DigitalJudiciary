"""Bootstrap ceremony (SDD v3.0 Phase 0): assemble the service graph, create
the founding principals, enact the bootstrap rulebook, and import the seed
jurisprudence — through the Challenge Gate, so even seeds satisfy every
axiom the Gate enforces (authority-at-time, exhaustion for tier k, A5
completeness, A7 expiry+referral)."""
from __future__ import annotations

import json
import os
import uuid
from datetime import datetime, timedelta

from . import db, judges, kernel, lifecycle
from .platform.dj_config import load_and_apply
from .db import now_iso
from .adjudicate import Adjudicator
from .httpapi import Services

SEED_DIR = os.environ.get("DJ_SEED_DIR",
                          os.path.join(os.path.dirname(__file__), "..", "seed"))
# Which jurisprudence file inside SEED_DIR to admit. The demo packs ship two:
# the full post-run store (default) and the store as it stood at the first
# case, for a run that regrows it.
SEED_STORE = os.environ.get("DJ_SEED_STORE", "store_seed.json")
GENESIS = "2025-06-01T00:00:00.000000+00:00"

DEV_KEYS = {
    "alice.grc":  "devkey-alice",   # Lawmakers (GRC council chair)
    "coo.pat":    "devkey-pat",     # RiskOwner (COO)
    "eng.sam":    "devkey-sam",     # engineer: no branch; files & contests
    "svc:tier1":  "devkey-t1",      # Judges (workloads)
    "svc:tier2":  "devkey-t2",
    "svc:tier3":  "devkey-t3",
    # The inbound gateway. Deliberately granted NOTHING: it appears in the
    # registry so its acts are attributable, and holds no branch so the
    # Kernel refuses it any resolution or acceptance. A hostile gateway can
    # file bad cases and lie to GitHub; it cannot decide one.
    "svc:github": "devkey-gh",
    # The consolidation pipeline. Like the gateway, it appears in the registry
    # so that its acts are attributable and holds no branch, so the Kernel
    # refuses it any resolution or acceptance. CC-22(a) checks the second half
    # against the ledger's own historical role table rather than against this
    # dictionary.
    "svc:classify": "devkey-cls",
}


def build_services(path: str | None = None) -> Services:
    load_and_apply()  # config/dj.toml → env (demo works with no file)
    db.init_db(path)
    registry = kernel.AuthorityRegistry(path)
    constitution = kernel.ConstitutionStore(registry, path)
    chain = kernel.ContestChain(path)
    # Ledger first so the Gate can keep the process-local active-holdings
    # cache coherent on every admit and lifecycle event.
    ledger = kernel.LedgerReader(path)
    gate = kernel.ChallengeGate(registry, chain, constitution, path,
                                ledger=ledger)
    # The constitution store writes lifecycle events too (supersession), so
    # it needs the same cache-coherence wiring the Gate was given. Without
    # this, an amended-away clause keeps binding new cases from stale cache.
    constitution.attach_ledger(ledger)
    provenance = kernel.JudgmentProvenance(judges.make_judges(), path)
    adjudicator = Adjudicator(registry, constitution, ledger, gate,
                              provenance, chain, path)
    lcm = lifecycle.LifecycleManager(gate, path)
    svc = Services(registry, constitution, ledger, gate, provenance,
                   chain, adjudicator, lcm)
    # L5 last: the gateway is a client of the container, not a member of it.
    from .inbound_github import PRGateway
    svc.gateway = PRGateway(svc, path)
    # Platform tables live in the same SQLite file on the demo path.
    from . import jobs, enterprise
    from .platform import tenancy
    from .platform.workers import WorkerPlane
    jobs.ensure_schema(path)
    enterprise.ensure_schema(path)
    tenancy.ensure_schema(path)
    # Worker plane: one or more job workers (DJ_WORKER_THREADS)
    svc.worker_plane = WorkerPlane(svc, path)
    svc.job_worker = jobs.JobWorker(svc, path)  # back-compat alias
    # Consolidation (Definition 16). A separate object with its own writer,
    # holding no authority: it forms classes and records artefacts, and it is
    # the only thing in the process that can. CC-22(a) asserts that its
    # identity appears in no auth_id field and in no role assignment.
    from . import consolidate
    svc.classifier = consolidate.ClassRegistry(path)
    return svc


def bootstrap(svc: Services, path: str | None = None) -> dict:
    """Idempotent. Returns {principal: api_key} on first run (dev keys when
    DJ_DEV_KEYS=1, random otherwise), {} on later runs."""
    conn = db.open_writer(path)
    already = conn.execute("SELECT COUNT(*) AS c FROM principal").fetchone()["c"]
    conn.close()
    if already:
        return {}

    dev = os.environ.get("DJ_DEV_KEYS") == "1"
    keys: dict[str, str] = {}
    for pid in DEV_KEYS:
        kind = "workload" if pid.startswith("svc:") else "human"
        keys[pid] = svc.registry.create_principal(
            pid, kind, DEV_KEYS[pid] if dev else None)

    # Founding grants: the ceremony (documented, one-time; the bootstrap
    # flag exists only here). All branch pairs disjoint by trigger.
    #
    # The ceremony must PREDATE the jurisprudence it admits. The Gate checks
    # that a record's resolving principal held the required branch at that
    # record's own resolved_at (CC-02), so a seed corpus reaching further
    # back than the default genesis would be refused — correctly, because a
    # record cannot have been resolved before the authority to resolve it
    # existed. Rather than weaken that check for seeds, the ceremony date is
    # pulled back to cover them.
    genesis = _genesis_for_seeds()
    svc.registry.grant("alice.grc", "lawmakers", "bootstrap-ceremony",
                       "founding Lawmaker", bootstrap=True,
                       valid_from=genesis)
    svc.registry.grant("coo.pat", "risk_owner", "alice.grc",
                       "founding RiskOwner", valid_from=genesis)
    for t in ("svc:tier1", "svc:tier2", "svc:tier3"):
        svc.registry.grant(t, "judges", "alice.grc",
                           f"adjudication workload {t}", valid_from=genesis)
    # eng.sam holds no branch: engineers file cases and challenges, and
    # that is a principal capability, not a branch capability.

    keys.update(_seed_organizations(svc, genesis))

    # Constitution: explicit path (config/upload) wins over seed default.
    rb_path = os.environ.get("DJ_CONSTITUTION_PATH") or os.path.join(
        SEED_DIR, "rulebook.json")
    rb = json.load(open(rb_path))
    provisions = rb["provisions"] if isinstance(rb, dict) and "provisions" in rb else rb
    svc.constitution.enact_version(provisions, "alice.grc",
                                   amendment_id=None, bootstrap=True)

    # A9: the standing declaration is part of the constitution and is
    # recorded at the ceremony, attributed to the founding Lawmaker and
    # dated at genesis so that it is in force for the seed jurisprudence
    # too. A pack that ships no declaration still boots, but fails the A9
    # conformance check (CC-17): the axiom requires the declaration, and
    # the suite is where that requirement bites.
    if isinstance(rb, dict) and rb.get("standing_declaration") is not None:
        svc.constitution.declare_standing(
            rb["standing_declaration"], "alice.grc", at=genesis)

    _import_seed_store(svc)
    return keys


def _seed_organizations(svc: Services, genesis: str) -> dict:
    """Create the tenants a seed corpus declares, and their officers.

    Each tenant gets its OWN risk owner, granted the branch like any other:
    tenancy does not introduce a second authority mechanism, it just means
    more than one principal holds the same branch and each is scoped to the
    ledger they serve. The founding officers stay unscoped, which is what
    makes them group-level rather than special.
    """
    path = os.path.join(SEED_DIR, "organizations.json")
    if not os.path.exists(path):
        return {}
    dev = os.environ.get("DJ_DEV_KEYS") == "1"
    conn = db.open_writer()
    out: dict[str, str] = {}
    pack = json.load(open(path))
    for org in pack["organizations"]:
        if org.get("org_id"):
            conn.execute(
                "INSERT OR IGNORE INTO organization (org_id, name, created_at)"
                " VALUES (?,?,?)", (org["org_id"], org["name"], now_iso()))
            conn.commit()
        for pr in org.get("principals", []):
            out[pr["principal_id"]] = svc.registry.create_principal(
                pr["principal_id"], pr.get("kind", "human"),
                pr["key"] if dev else None,
                organization=org.get("org_id"))
            if pr.get("role"):
                conn.execute("UPDATE principal SET role_hint=?"
                             " WHERE principal_id=?",
                             (pr["role"], pr["principal_id"]))
                conn.commit()
            if pr.get("branch"):
                svc.registry.grant(
                    pr["principal_id"], pr["branch"], "alice.grc",
                    f"{org['name']} {pr['branch']}", valid_from=genesis)
    # Scope the ceremony accounts. They exist so the founding grants have a
    # granter; they are not an operating position, and leaving them unscoped
    # would mean several accounts could read across tenants when the design
    # says exactly one should.
    scope = pack.get("founding_scope")
    if scope:
        conn.executemany(
            "UPDATE principal SET organization = ? WHERE principal_id = ?"
            " AND organization IS NULL",
            [(scope, p) for p in ("alice.grc", "coo.pat", "eng.sam")])
        conn.commit()
    conn.close()
    return out


def _genesis_for_seeds() -> str:
    """The later of the default genesis and one day before the oldest seed."""
    try:
        seeds = json.load(open(os.path.join(SEED_DIR, SEED_STORE)))
        stamps = [r["resolved_at"] for r in seeds["records"]
                  if r.get("resolved_at")]
    except (OSError, KeyError, json.JSONDecodeError):
        return GENESIS
    if not stamps:
        return GENESIS
    earliest = min(stamps)
    if earliest > GENESIS:
        return GENESIS
    day = datetime.fromisoformat(earliest) - timedelta(days=1)
    return day.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")


def _import_seed_store(svc: Services) -> None:
    seeds = json.load(open(os.path.join(SEED_DIR, SEED_STORE)))
    reader = db.open_reader()
    rbv = svc.constitution.current_version()
    by_seed_id: dict[str, str] = {}
    for s in seeds["records"]:
        case_id = f"SEED-{s['seed_id']}"
        if s["tier"] == 4:  # tier-k seeds need an A4-verifiable history
            for t in (1, 2, 3):
                svc.chain.append(case_id, t, "eng.sam",
                                 f"seed-import contest of tier {t}")
        artifact = {
            "artifact_version": "1.0",
            "case": {"case_id": case_id,
                     "case_hash": kernel.sha256(case_id),
                     "provision_id": s["provision_id"],
                     "rulebook_version": rbv,
                     "facts": sorted(s["facts"]),
                     "author": "seed-import"},
            "tier": s["tier"],
            "resolving_principal": s["resolving_principal"],
            "retrieval": {"theta": judges.THETA, "snapshot_at": GENESIS,
                          "candidates": []},
            "judgments": {"batch_id": str(uuid.uuid4()), "verdicts": []},
            "ordering": {"keys_applied": ["authority", "recency", "scope"],
                         "controlling_state": "none_empty",
                         "controlling_id": None, "tie_members": None},
            "decision": {"interpretation": s["interpretation"],
                         "conditions": s.get("conditions"),
                         "premise": sorted(s["premise"]),
                         "rationale_text": s["rationale"],
                         "scope": s.get("scope", {}),
                         "scope_level": s.get("scope_level", "org"),
                         "is_acceptance": bool(s.get("is_acceptance")),
                         "expiry": s.get("expiry"),
                         # Definition 8's `cites`: a seed may name the earlier
                         # seed it supersedes, which is what lets recency
                         # displace it at the ordering step (Sect. 4.6). The
                         # cited seed must appear earlier in the file.
                         "renews_record": by_seed_id.get(s.get("cites"))},
            "degradations": [],
            "resolved_at": s["resolved_at"],
        }
        rid = svc.gate.admit(artifact)
        by_seed_id[s["seed_id"]] = rid
        if s.get("cites") and s["cites"] not in by_seed_id:
            raise KeyError(f"seed {s['seed_id']} cites {s['cites']},"
                           " which is not admitted before it")

        # Decide the referral where the seed says the Lawmakers already did.
        # Each tenant's OWN legislature decides its own referrals: a lawmaker
        # of one company disposing of another's proposal is precisely what
        # decide_amendment refuses, and seeding it that way would write an
        # act into the ledger that the live system would reject.
        if s.get("referral_outcome") == "rejected":
            ev = [e for e in svc.ledger.lifecycle(rid)
                  if e["event_type"] == "referral_emitted"]
            amendment_id = json.loads(ev[0]["payload"])["amendment_id"]
            org = svc.ledger.get(rid).get("organization")
            lawmaker = f"{org}.grc" if org else "alice.grc"
            if svc.registry.resolve_branch(lawmaker) != "lawmakers":
                lawmaker = "alice.grc"
            svc.constitution.decide_amendment(amendment_id, "rejected",
                                              lawmaker)
    lifecycle.mirror_referral_outcomes(reader, svc.gate)
    reader.close()
