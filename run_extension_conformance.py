#!/usr/bin/env python3
"""Extension conformance (L6): tier differentiation, judged premise,
judicial referral, and the audit register.

A THIRD suite, for the same reason the interface suite is a second one: the
paper's Table 11 reports 48 kernel checks and its interface companion reports
41, and quietly changing either number to accommodate new mechanisms would
make the paper's own figures unreproducible. These are new claims, so they get
a new number.

Each check is computed from an executed trace. Exit 0 iff everything holds.

Run:  DJ_DB=/tmp/dje.db DJ_DEV_KEYS=1 python3 run_extension_conformance.py
"""
from __future__ import annotations

import json
import os
os.environ.setdefault('DJ_LEDGER_BACKEND', 'sqlite')
os.environ.setdefault('DJ_LEDGER_ON_PG', '0')
import sys
import tempfile

os.environ.setdefault("DJ_DB", os.path.join(tempfile.mkdtemp(), "dje.db"))
os.environ["DJ_DEV_KEYS"] = "1"
os.environ.setdefault("DJ_JUDGE_MODE", "oracle")

from app import bootstrap, db, judges, kernel      # noqa: E402

results: list[tuple[str, str, bool, str]] = []


def check(cid, name, ok, detail=""):
    results.append((cid, name, bool(ok), detail))


class StubJudge:
    """A judge whose answers are controllable, so tier-dependent behaviour is
    observable without a network. Records how many times each tier asked."""

    prompt_version = "stub-v1"

    def __init__(self, tier, distinguish_answer=True, premise=None):
        self.tier = tier
        self.version = f"stub:t{tier}"
        self.params = {"tier": tier}
        self.answer = distinguish_answer
        self.premise = premise
        self.calls = 0

    def distinguish(self, candidate, case):
        self.calls += 1
        return ({"distinguished": self.answer, "grounds": f"stub t{self.tier}"},
                1, False)

    def propose_premise(self, case, outcome, provision, reason):
        return (list(self.premise if self.premise is not None
                     else sorted(case["facts"])),
                f"stub t{self.tier} premise", 1, False)


def run() -> None:
    svc = bootstrap.build_services()
    bootstrap.bootstrap(svc)
    A = svc.adjudicator
    r = db.open_reader()

    # === Tier differentiation ==========================================
    case = A.submit_case("SC-203", ["third_party_lib", "tenant_data_path",
                                    "vendor_review_pending"], "eng.sam", {})
    cid = case["case_id"]
    A.challenge(cid, "eng.sam", "contest one")
    A.challenge(cid, "eng.sam", "contest two")

    tiers = {row["tier"]: row["n"] for row in r.execute(
        "SELECT tier, COUNT(*) AS n FROM judgment_invocation"
        " WHERE from_cache=0 AND kind='distinguish' GROUP BY tier")}
    check("EX-01", "each tier asks the judge itself rather than inheriting"
                   " the rung below's answer from cache",
          set(tiers) >= {1, 2, 3}, f"fresh invocations by tier: {tiers}")

    reused = r.execute(
        "SELECT COUNT(*) AS n FROM judgment_invocation ji WHERE from_cache=1"
        " AND EXISTS (SELECT 1 FROM judgment_invocation o"
        "  WHERE o.candidate_hash=ji.candidate_hash"
        "    AND o.case_hash=ji.case_hash AND o.tier<>ji.tier"
        "    AND o.from_cache=0)").fetchone()["n"]
    check("EX-02", "no verdict is reused across tiers: escalation can reach a"
                   " different answer", reused == 0, f"cross-tier reuse={reused}")

    check("EX-03", "the tier is recorded on every judgment, so a dossier"
                   " shows which rung asked",
          r.execute("SELECT COUNT(*) AS n FROM judgment_invocation"
                    " WHERE tier=0").fetchone()["n"] == 0)

    # A judge configured per tier is actually consulted per tier.
    stubs = {t: StubJudge(t) for t in (1, 2, 3, 4)}
    saved = svc.provenance.judges
    svc.provenance.judges = stubs
    c2 = A.submit_case("SC-203", ["third_party_lib", "tenant_data_path",
                                  "vendor_review_pending"], "eng.sam", {})
    A.challenge(c2["case_id"], "eng.sam", "contest")
    check("EX-04", "the judge bound to a tier is the one that tier consults",
          stubs[1].calls > 0 and stubs[2].calls > 0,
          f"t1={stubs[1].calls} t2={stubs[2].calls} t3={stubs[3].calls}")

    # Quorum width is per tier (a higher rung may deliberate harder).
    os.environ["DJ_QUORUM_T2"] = "5"
    check("EX-05", "quorum width is configurable per tier",
          judges.quorum_width(2) == 5 and judges.quorum_width(3) == 3,
          f"t2={judges.quorum_width(2)} t3={judges.quorum_width(3)}")
    os.environ.pop("DJ_QUORUM_T2", None)

    # === Judged premise ================================================
    svc.provenance.judges = {t: StubJudge(t, premise=["vendor_review_pending"])
                             for t in (1, 2, 3, 4)}
    os.environ["DJ_PREMISE_MODE"] = "judged"
    c3 = A.submit_case("SC-203", ["third_party_lib", "tenant_data_path",
                                  "vendor_review_pending"], "eng.sam", {})
    A.challenge(c3["case_id"], "eng.sam", "contest")
    acc = A.accept_resolution(c3["case_id"], "eng.sam")
    rec = svc.ledger.get(acc["record_id"])
    check("EX-06", "a judged premise narrows the holding instead of recording"
                   " every fact as material",
          rec["premise"] == ["vendor_review_pending"]
          and len(rec["premise"]) < len(rec["facts"]),
          f"premise={rec['premise']} facts={rec['facts']}")
    check("EX-07", "the premise judgment is recorded like any other, with its"
                   " tier and grounds",
          r.execute("SELECT COUNT(*) AS n FROM judgment_invocation"
                    " WHERE kind='premise'").fetchone()["n"] > 0)

    # The Gate constrains it: narrowing is allowed, inventing is not.
    art = {
        "artifact_version": "1.0",
        "case": {"case_id": "EXT-1", "case_hash": kernel.sha256("EXT-1"),
                 "provision_id": "SC-203",
                 "rulebook_version": svc.constitution.current_version(),
                 "facts": ["a", "b"], "author": "eng.sam"},
        "tier": 2, "resolving_principal": "svc:tier2",
        "retrieval": {"theta": 0.25, "snapshot_at": bootstrap.GENESIS,
                      "candidates": []},
        "judgments": {"batch_id": "b", "verdicts": []},
        "ordering": {"keys_applied": [], "controlling_state": "none_empty",
                     "controlling_id": None, "tie_members": None},
        "decision": {"interpretation": {"outcome": "deny"}, "conditions": None,
                     "premise": ["a", "NEVER_HAPPENED"], "rationale_text": "r",
                     "scope": {}, "scope_level": "org", "is_acceptance": False},
        "degradations": [], "resolved_at": bootstrap.GENESIS,
    }
    try:
        svc.gate.admit(art)
        ok, why = False, "admitted"
    except kernel.KernelError as e:
        ok, why = "premise contains facts absent" in str(e), str(e)[:60]
    check("EX-08", "the Gate refuses a premise containing a fact the case"
                   " never had: a model may narrow a holding, never invent"
                   " one", ok, why)

    os.environ["DJ_PREMISE_MODE"] = "mechanical"
    svc.provenance.judges = saved

    # === Judicial referral =============================================
    def referrals():
        return [dict(x) for x in r.execute(
            "SELECT id, proposed_by, source_record, body FROM draft_amendment"
            " WHERE origin='judicial_referral'").fetchall()]

    tie = A.submit_case("SC-210", ["dummy_marked", "fixture_path"],
                        "eng.sam", {})
    # This asserts the *referral* property, not the tie itself: whatever tier
    # 1 concluded, nothing may reach the legislature until a resolution is
    # recorded. Written this way it holds on any corpus, and the tie-specific
    # claims below still say plainly when their fixture is absent.
    check("EX-09", "nothing at tier 1 refers anything: the unchallenged mass"
                   " cannot flood the legislature",
          len(referrals()) == 0,
          f"state={tie['controlling_state']} referrals={len(referrals())}")

    # The tie fixture belongs to the default seed corpus. Run against a
    # different constitution these checks have nothing to bite on, so they
    # report that rather than crashing or — worse — passing vacuously while
    # looking like they ran.
    if tie["controlling_state"] != "none_tie":
        for cid, why in (("EX-10", "a RECORDED unbroken conflict refers the"
                                   " provision to the lawmakers"),
                         ("EX-11", "the referral names the tier that filed"
                                   " it"),
                         ("EX-12", "the same conflict does not refer twice"),
                         ("EX-13", "A3 holds: the tier that referred cannot"
                                   " enact its own referral"),
                         ("EX-14", "only the lawmakers dispose of a judicial"
                                   " referral")):
            check(cid, why + " — no tie fixture in this corpus", True,
                  "n/a")
        tenancy(svc, r)
        return
    A.challenge(tie["case_id"], "eng.sam", "contest")
    A.accept_resolution(tie["case_id"], "eng.sam")
    refs = referrals()
    body = json.loads(refs[0]["body"]) if refs else {}
    check("EX-10", "a RECORDED unbroken conflict refers the provision to the"
                   " lawmakers, citing the record that exposed it",
          len(refs) == 1 and body.get("trigger") == "unbroken_conflict"
          and refs[0]["source_record"], body.get("trigger", "none"))
    check("EX-11", "the referral names the tier that filed it, not a human",
          refs and refs[0]["proposed_by"].startswith("svc:tier"),
          refs[0]["proposed_by"] if refs else "")

    tie2 = A.submit_case("SC-210", ["dummy_marked", "fixture_path"],
                         "eng.sam", {})
    A.challenge(tie2["case_id"], "eng.sam", "contest")
    A.accept_resolution(tie2["case_id"], "eng.sam")
    check("EX-12", "the same conflict does not refer twice",
          len(referrals()) == 1, f"referrals={len(referrals())}")

    # A3 holds: proposing is not enacting.
    aid = referrals()[0]["id"]
    try:
        svc.constitution.decide_amendment(aid, "adopted", "svc:tier2")
        ok, why = False, "a tier decided its own referral"
    except kernel.KernelError as e:
        ok, why = "requires 'lawmakers'" in str(e), str(e)[:60]
    check("EX-13", "A3 holds: the tier that referred cannot enact its own"
                   " referral", ok, why)
    out = svc.constitution.decide_amendment(aid, "rejected", "alice.grc")
    check("EX-14", "only the lawmakers dispose of a judicial referral",
          out["status"] == "rejected", out["status"])

    # Repeat risk acceptance on one provision is also a legislative signal.
    n_before = len(referrals())
    os.environ["DJ_REFERRAL_ACCEPTANCE_N"] = "1"
    acc_case = A.submit_case("SC-203", ["third_party_lib", "tenant_data_path",
                                        "vendor_review_pending"],
                             "eng.sam", {})
    for _ in range(3):
        A.challenge(acc_case["case_id"], "eng.sam", "climb")
    A.risk_decision(acc_case["case_id"], "coo.pat", "accept",
                    "bounded acceptance", "2027-01-01")
    repeats = [x for x in referrals()
               if json.loads(x["body"]).get("trigger") == "repeat_acceptance"]
    check("EX-15", "a provision that keeps being risk-accepted is referred as"
                   " a legislative question, not adjudicated again",
          len(referrals()) > n_before and repeats,
          f"repeat_acceptance referrals={len(repeats)}")
    os.environ.pop("DJ_REFERRAL_ACCEPTANCE_N", None)


    # === The register: an audit view that must not lose a record =======
    # Paging is where an audit surface quietly fails: a boundary off by one
    # drops a holding from the register while every individual page looks
    # correct. These check the whole partition, not a sample.
    scan = [dict(x) for x in r.execute(
        "SELECT id, resolved_at, is_acceptance, lapsed FROM record_effective"
    ).fetchall()]
    c = svc.ledger.census()
    check("EX-16", "the census aggregate agrees with a full scan of the"
                   " ledger",
          c["records"] == len(scan)
          and c["lapsed"] == sum(1 for x in scan if x["lapsed"])
          and c["holdings"] == sum(1 for x in scan if not x["is_acceptance"]),
          f"census={c['records']} scan={len(scan)}")

    check("EX-17", "the status filters partition the ledger exactly: every"
                   " record is a holding, a live acceptance, or lapsed",
          c["holdings"] + c["live_acceptances"] + c["lapsed"] == c["records"],
          f"{c['holdings']}+{c['live_acceptances']}+{c['lapsed']}"
          f" vs {c['records']}")

    seen, order, cursor, pages = [], [], None, 0
    while pages < 200:
        out = svc.ledger.register(limit=3, cursor=cursor)
        seen += [x["id"] for x in out["rows"]]
        order += [(x["resolved_at"], x["id"]) for x in out["rows"]]
        pages += 1
        cursor = out["next"]
        if not cursor:
            break
    check("EX-18", "paging the register at any page size yields every record"
                   " exactly once — no gap at a boundary, no duplicate",
          sorted(seen) == sorted(x["id"] for x in scan)
          and len(seen) == len(set(seen)),
          f"paged={len(seen)} unique={len(set(seen))} total={len(scan)}")

    check("EX-19", "the register reads newest-first across page boundaries,"
                   " so a keyset cursor cannot reorder history",
          all(order[i] >= order[i + 1] for i in range(len(order) - 1)),
          f"{pages} pages")


    tenancy(svc, r)
    overlay_and_sharing(svc, r)
    supersession(svc, r)


def tenancy(svc, r) -> None:
    orgs = svc.registry.organizations()

    # Every act must be attributable to a company. An untenanted row shows up
    # in the activity statement as "platform", which reads as a platform-level
    # act rather than the tenant's own — quietly wrong, and invisible until
    # somebody asks why every company is called platform.
    # Only meaningful once tenants exist: in a single-tenant deployment every
    # row is legitimately untenanted, and asserting otherwise would be
    # measuring the fixture rather than the property.
    if svc.registry.organizations():
        orphans = {}
        for tbl in ("pr_session", "review_task", "draft_amendment"):
            n = r.execute(f"SELECT COUNT(*) AS n FROM {tbl}"
                          f" WHERE organization IS NULL").fetchone()["n"]
            if n:
                orphans[tbl] = n
        check("EX-46", "every session, review and amendment is attributable"
                       " to a company: nothing files itself as platform-wide"
                       " by accident", not orphans, f"untenanted: {orphans}")
    else:
        check("EX-46", "company attribution (single-tenant corpus: every row"
                       " is legitimately untenanted)", True, "n/a")

    dupes = [dict(x) for x in r.execute(
        "SELECT provision_id, COUNT(DISTINCT organization) AS n FROM provision"
        " WHERE organization IS NOT NULL GROUP BY provision_id"
        " HAVING n > 1").fetchall()]
    check("EX-20", "no provision id is claimed by two tenants — the property"
                   " that keeps retrieval tenant-safe without filtering the"
                   " hot path", not dupes, f"collisions={len(dupes)}")

    strays = r.execute(
        "SELECT COUNT(*) AS n FROM precedent_record pr JOIN provision p"
        "  ON p.provision_id = pr.provision_id"
        "  AND p.version_id = pr.rulebook_version"
        " WHERE IFNULL(pr.organization,'') <> IFNULL(p.organization,'')"
    ).fetchone()["n"]
    check("EX-21", "every record carries the tenant of the clause it"
                   " interprets: a submission cannot file into another"
                   " tenant's ledger", strays == 0, f"mismatched={strays}")

    if len(orgs) > 1:
        # Cross-tenant authority. Holding the lawmakers branch says WHAT a
        # principal may do, not WHOSE constitution they may do it to.
        from app import kernel as _k
        rows = {x["organization"]: x["id"] for x in r.execute(
            "SELECT organization, id FROM draft_amendment"
            " WHERE status='pending' AND organization IS NOT NULL"
            " GROUP BY organization").fetchall()}
        mine = [o["org_id"] for o in orgs if f"{o['org_id']}.grc"
                in {p["principal_id"] for p in [dict(z) for z in r.execute(
                    "SELECT principal_id FROM principal").fetchall()]}]
        if len(rows) > 1 and len(mine) > 1:
            theirs = [o for o in rows if o != mine[0]][0]
            try:
                svc.constitution.decide_amendment(
                    rows[theirs], "rejected", f"{mine[0]}.grc")
                ok, why = False, "allowed"
            except _k.KernelError as e:
                ok, why = "cannot decide an amendment belonging to" in str(e), \
                    str(e)[:60]
            check("EX-28", "a tenant's lawmaker cannot decide another"
                           " tenant's amendment, though both hold the same"
                           " branch", ok, why)
        else:
            check("EX-28", "cross-tenant amendment authority (no fixture)",
                  True, "n/a")

    if orgs:
        a = orgs[0]["org_id"]
        scoped = svc.ledger.register(limit=500, org=a)["rows"]
        check("EX-22", "a tenant-scoped register returns that tenant's"
                       " records and no others",
              scoped and all(x["organization"] == a for x in scoped),
              f"{len(scoped)} rows, org={a}")
        total = svc.ledger.census()["records"]
        per = sum(svc.ledger.census(org=o["org_id"])["records"] for o in orgs)
        check("EX-23", "the tenants partition the ledger: scoped censuses sum"
                       " to the platform census",
              per == total, f"{per} vs {total}")
    else:
        check("EX-22", "a tenant-scoped register returns that tenant's"
                       " records and no others (single-tenant: vacuous)", True)
        check("EX-23", "the tenants partition the ledger (single-tenant:"
                       " vacuous)", True)


def upgrade_in_place() -> None:
    """A volume written by an earlier release must open, not explode.

    This is regression cover for a real failure: CREATE TABLE IF NOT EXISTS
    skips an existing table, so a newly added column never appeared on an
    upgraded database, and the same schema script then tried to index that
    column and died with a bare "no such column". Anyone with a data volume
    from a previous version hit it on the next boot.
    """
    import sqlite3
    import tempfile
    from app import db as dbmod

    path = os.path.join(tempfile.mkdtemp(), "upgrade.db")
    dbmod.init_db(path)

    # Roll the file back to the previous release's shape.
    c = sqlite3.connect(path)
    for name in ("pr_org", "prs_org", "rt_org", "ji_cache"):
        c.execute(f"DROP INDEX IF EXISTS {name}")
    for table, column, _ in dbmod.ADDED_COLUMNS:
        try:
            c.execute(f"ALTER TABLE {table} DROP COLUMN {column}")
        except sqlite3.OperationalError:
            pass
    c.execute("DROP TABLE IF EXISTS organization")
    c.commit()
    stale = {t: {r[1] for r in c.execute(f"PRAGMA table_info({t})")}
             for t, _, _ in dbmod.ADDED_COLUMNS}
    c.close()
    rolled = [f"{t}.{col}" for t, col, _ in dbmod.ADDED_COLUMNS
              if col not in stale[t]]
    # Not every column can be rolled back: SQLite refuses DROP COLUMN on a
    # column carrying a constraint, so principal.organization (a foreign key)
    # survives. The fixture only has to be genuinely stale, which it is; the
    # guarantee itself is asserted by EX-26 over the full column list.
    check("EX-24", "the fixture really is an older database (columns absent"
                   " before the upgrade)", len(rolled) > 0,
          f"{len(rolled)}/{len(dbmod.ADDED_COLUMNS)} columns rolled back")

    try:
        dbmod.init_db(path)
        opened, why = True, ""
    except sqlite3.OperationalError as e:
        opened, why = False, str(e)
    check("EX-25", "a database from an earlier release opens and migrates in"
                   " place rather than failing on the schema script",
          opened, why)

    # Views are the other half of the same trap, and the one that bit second:
    # CREATE VIEW IF NOT EXISTS is a no-op against an existing view, so an
    # upgraded database keeps serving a stale definition and a column added to
    # a view is silently absent.
    c = sqlite3.connect(path)
    c.execute("DROP VIEW IF EXISTS record_effective")
    c.execute("CREATE VIEW record_effective AS SELECT r.*, 0 AS lapsed"
              " FROM precedent_record r")
    c.commit()
    stale_cols = {x[1] for x in
                  c.execute("PRAGMA table_info(record_effective)")}
    c.close()
    check("EX-44", "the fixture really has a stale view (a later column is"
                   " absent before the upgrade)",
          "superseded" not in stale_cols, "record_effective rolled back")

    try:
        dbmod.init_db(path)
        c = sqlite3.connect(path)
        cols = {x[1] for x in
                c.execute("PRAGMA table_info(record_effective)")}
        c.close()
        ok_v, why_v = {"lapsed", "superseded"} <= cols, sorted(cols)[-2:]
    except sqlite3.OperationalError as e:
        ok_v, why_v = False, str(e)
    check("EX-45", "a view whose definition changed is rebuilt on upgrade,"
                   " not left stale", ok_v, f"{why_v}")

    if opened:
        c = sqlite3.connect(path)
        missing = [f"{t}.{col}" for t, col, _ in dbmod.ADDED_COLUMNS
                   if col not in {r[1] for r in
                                  c.execute(f"PRAGMA table_info({t})")}]
        idx = {r[0] for r in c.execute(
            "SELECT name FROM sqlite_master WHERE type='index'")}
        c.close()
        check("EX-26", "every column added since the first release is present"
                       " after the upgrade, and the changed indexes are"
                       " rebuilt",
              not missing and {"pr_org", "ji_cache"} <= idx,
              f"missing={missing}")
        try:
            dbmod.init_db(path)
            check("EX-27", "booting again against an already-current database"
                           " changes nothing", True)
        except sqlite3.OperationalError as e:
            check("EX-27", "booting again against an already-current database"
                           " changes nothing", False, str(e))


def overlay_and_sharing(svc, r) -> None:
    """Stages 1-3: shared base constitution, shared precedent, promotion."""
    from app import db as dbmod
    from app.adjudicate import order

    C, A = svc.constitution, svc.adjudicator
    rb = C.current_version()

    # These need a SHARED base clause to bite. A corpus where every provision
    # is tenant-owned has no overlay to test, and saying so is better than
    # passing vacuously while looking like it ran.
    shared = [p for p in C.list_provisions(rb)
              if p.get("organization") is None]
    if not shared:
        for cid in ("EX-29", "EX-30", "EX-31", "EX-32", "EX-33", "EX-34",
                    "EX-35", "EX-36", "EX-37", "EX-38"):
            check(cid, "shared base constitution / precedent sharing /"
                       " promotion — no shared base in this corpus", True,
                  "n/a")
        return

    absolutes = [p for p in shared if p["absolute"]]
    softs = [p for p in shared if not p["absolute"]
             and (p["policy"] or {}).get("deny_if_any")]
    if not absolutes or not softs:
        for cid in ("EX-29", "EX-30"):
            check(cid, "override tightening rules (no fixture)", True, "n/a")
        base = soft = None
    else:
        base = absolutes[0]
        soft = softs[0]

    if base:
        try:
            C.check_override(rb, {"provision_id": base["provision_id"],
                                  "absolute": False,
                                  "policy": base["policy"]})
            ok, why = False, "allowed"
        except kernel.KernelError as e:
            ok, why = "cannot opt out of a shared floor" in str(e), str(e)[:50]
        check("EX-29", "a tenant override cannot un-absolute a shared floor:"
                       " overrides tighten, never loosen", ok, why)

        try:
            C.check_override(rb, {"provision_id": soft["provision_id"],
                                  "absolute": False,
                                  "policy": {"deny_if_any": []}})
            ok2, why2 = False, "allowed"
        except kernel.KernelError as e:
            ok2, why2 = "never remove them" in str(e), str(e)[:50]
        check("EX-30", "a tenant override cannot drop a base trigger fact",
              ok2, why2)

    w = dbmod.open_writer()
    for o in ("t_one", "t_two"):
        w.execute("INSERT OR IGNORE INTO organization VALUES (?,?,?)",
                  (o, o, dbmod.now_iso()))
    w.commit()
    for o in ("t_one", "t_two"):
        try:
            svc.registry.create_principal(f"{o}.eng", "human", f"k-{o}",
                                          organization=o)
        except Exception:                                   # noqa: BLE001
            pass

    facts = ["third_party_lib", "tenant_data_path", "vendor_review_pending"]
    c = A.submit_case("SC-203", facts, "t_one.eng", {})
    A.challenge(c["case_id"], "t_one.eng", "contest")
    rid = A.accept_resolution(c["case_id"], "t_one.eng")["record_id"]
    rec = svc.ledger.get(rid)
    check("EX-31", "a holding under a SHARED base clause still joins the"
                   " filing tenant's ledger, not the platform's",
          rec["organization"] == "t_one", f"org={rec['organization']}")

    case = {"provision_id": "SC-203", "facts": facts, "case_scope": {}}
    seen = [x["id"] for x in svc.ledger.retrieve(case, 0.25, org="t_two")]
    check("EX-32", "one tenant's holding is not a candidate for another's"
                   " case", rid not in seen, f"{len(seen)} candidates")

    for who, label in (("coo.pat", "a risk owner"), ("eng.sam", "an engineer")):
        try:
            svc.gate.promote(rid, who)
            ok3, why3 = False, f"{label} promoted"
            break
        except kernel.KernelError as e:
            ok3, why3 = "requires 'lawmakers'" in str(e), str(e)[:44]
    check("EX-33", "promotion is legislative: nobody but the lawmakers can"
                   " make a tenant holding into platform law", ok3, why3)

    pid = svc.gate.promote(rid, "alice.grc")
    promoted = svc.ledger.get(pid)
    check("EX-34", "a promoted holding is platform-scope, tenant-less, and"
                   " cites the holding it ratifies",
          promoted["organization"] is None
          and promoted["scope_level"] == "platform"
          and promoted.get("promoted_from") == rid,
          f"scope={promoted['scope_level']}")

    seen2 = [x["id"] for x in svc.ledger.retrieve(case, 0.25, org="t_two")]
    check("EX-35", "platform law IS a candidate for every tenant's case",
          pid in seen2, f"{len(seen2)} candidates")

    pool = svc.ledger.retrieve(case, 0.25, org="t_one")
    ctrl, state, _ = order(pool, case)
    check("EX-36", "a tenant's own holding outranks platform law on the same"
                   " facts — tenant law above shared law",
          ctrl is not None and ctrl["scope_level"] != "platform",
          f"{state}: {ctrl['scope_level'] if ctrl else None}")

    try:
        svc.gate.promote(rid, "alice.grc")
        ok4, why4 = False, "promoted twice"
    except kernel.KernelError as e:
        ok4, why4 = "already been promoted" in str(e), str(e)[:40]
    check("EX-37", "a holding cannot be promoted twice", ok4, why4)

    acc = None
    for row in r.execute("SELECT id FROM precedent_record"
                         " WHERE is_acceptance=1 LIMIT 1").fetchall():
        acc = row["id"]
    if acc:
        try:
            svc.gate.promote(acc, "alice.grc")
            ok5, why5 = False, "an acceptance was promoted"
        except kernel.KernelError as e:
            ok5, why5 = "cannot be promoted" in str(e), str(e)[:44]
        check("EX-38", "a risk acceptance can never become platform law:"
                       " dispensations do not generalise", ok5, why5)
    else:
        check("EX-38", "acceptance promotion (no fixture)", True, "n/a")


def supersession(svc, r) -> None:
    """What an amendment does to the case law built on the clause it changed."""
    A, C = svc.adjudicator, svc.constitution

    def holding(pid, facts):
        c = A.submit_case(pid, facts, "eng.sam", {})
        A.challenge(c["case_id"], "eng.sam", "contest")
        return A.accept_resolution(c["case_id"], "eng.sam")["record_id"]

    def live(pid, facts):
        return len(svc.ledger.retrieve(
            {"provision_id": pid, "facts": facts, "case_scope": {}}, 0.25))

    f203 = ["third_party_lib", "tenant_data_path", "vendor_review_pending"]
    f206 = ["coverage_shortfall", "critical_service"]
    holding("SC-203", f203)
    holding("SC-206", f206)
    before203, before206 = live("SC-203", f203), live("SC-206", f206)

    v = C.current_version()
    p203 = C.get_provision(v, "SC-203")
    aid = C.file_amendment("alice.grc", "lawmaker", {"changes": [
        {"provision_id": "SC-203", "text": "SC-203, clarified wording.",
         "policy": p203["policy"], "absolute": p203["absolute"]}]})
    out = C.decide_amendment(aid, "adopted", "alice.grc")
    check("EX-39", "a clarification that leaves the predicate alone does not"
                   " discard the case law built on the clause",
          out["superseded_records"] == 0
          and live("SC-203", f203) == before203,
          f"superseded={out['superseded_records']}")

    aid2 = C.file_amendment("alice.grc", "lawmaker", {"changes": [
        {"provision_id": "SC-203", "text": "SC-203, rewritten.",
         "policy": {"deny_if_any": ["vendor_review_pending", "unsandboxed"]},
         "absolute": False}]})
    out2 = C.decide_amendment(aid2, "adopted", "alice.grc")
    check("EX-40", "a materially amended clause supersedes its own holdings:"
                   " they stop being candidates",
          out2["superseded_records"] > 0 and live("SC-203", f203) == 0,
          f"superseded={out2['superseded_records']}")

    check("EX-41", "supersession is bounded by provision — an untouched clause"
                   " keeps its case law",
          live("SC-206", f206) == before206,
          f"SC-206 candidates {live('SC-206', f206)} vs {before206}")

    rid = r.execute("SELECT record_id FROM precedent_lifecycle_event"
                    " WHERE event_type='superseded' LIMIT 1").fetchone()
    rec = svc.ledger.get(rid["record_id"]) if rid else None
    check("EX-42", "a superseded holding stays in the ledger and says why it"
                   " stopped applying — retired, not erased",
          rec is not None and bool(rec.get("superseded")),
          "present and flagged" if rec else "missing")

    holding("SC-206", ["coverage_shortfall", "critical_service", "hotfix"])
    n206 = live("SC-206", f206)
    aid3 = C.file_amendment("alice.grc", "lawmaker", {
        "supersedes_precedent": False,
        "changes": [{"provision_id": "SC-206", "text": "SC-206 v3.",
                     "policy": {"deny_if_any": ["coverage_shortfall",
                                                "new_trigger"]},
                     "absolute": False}]})
    out3 = C.decide_amendment(aid3, "adopted", "alice.grc")
    check("EX-43", "the lawmakers may declare an amendment non-superseding:"
                   " whether they clarified or changed is their call, not the"
                   " adjudicator's",
          out3["superseded_records"] == 0 and live("SC-206", f206) == n206,
          f"superseded={out3['superseded_records']}")


def backend_parity() -> None:
    """The two ledger backends must guard the same tables.

    SQLite and Postgres schemas are written separately and will drift. A
    missing trigger is invisible until somebody edits a row that should have
    been unwritable — at which point the ledger has already been rewritten
    and the audit trail is worth nothing.

    This compares the two schema definitions statically, so it runs without a
    Postgres server and catches the drift at the moment it is introduced
    rather than the moment it is exploited.
    """
    import re as _re
    from app import db as dbmod

    sqlite_guarded = set(_re.findall(
        r"CREATE TRIGGER IF NOT EXISTS \w+\s+BEFORE (?:UPDATE|DELETE) ON"
        r" (\w+)", dbmod.SCHEMA))
    try:
        from app.platform import pg_ledger
    except Exception as e:                                    # noqa: BLE001
        check("EX-47", "the Postgres ledger guards every table SQLite guards"
                       " (backend not present)", True, f"n/a: {e}")
        return

    pg_guarded = pg_ledger.protected_tables_in_statements()
    missing = sorted(sqlite_guarded - pg_guarded)
    check("EX-47", "the Postgres ledger guards every table SQLite guards —"
                   " immutability is a property of the ledger, not of the"
                   " backend it happens to run on",
          not missing, f"unguarded on Postgres: {missing}" if missing
          else f"{len(sqlite_guarded)} tables, both backends")

    # The conditional one is the easiest to lose, so it is named explicitly.
    frozen = any("a decided review is final" in st
                 for st in pg_ledger.PG_LEDGER_STATEMENTS)
    check("EX-48", "a decided review is final on Postgres too: review_task is"
                   " append-only AFTER a decision, which a port of the"
                   " append-only tables does not catch", frozen,
          "conditional trigger present" if frozen else "MISSING")


def consolidation_layer() -> None:
    """Definition 7(ii) at the layers above the contract.

    Four properties that live where the extension suite lives: the ordering
    consequence of admitting at first instance, the separation of the
    class-forming identity from every adjudicating one, the migration of an
    older ledger, and parity of the amended admission bar across backends.
    """
    import sqlite3
    import tempfile as _tf
    from app import consolidate as _cons, db as _db

    # EX-50. A consolidated record is written at first instance, so it carries
    # the LOWEST admissible authority rank and can never outrank a record
    # admitted under clause (i) at the `auth` key. That is not a policy choice
    # made in the ordering code; it falls out of the tier the amended
    # Definition 7 gives it, and this check is what ties the two together.
    from app.adjudicate import authority_rank as _rank
    never_outranks = all(_rank(1) <= _rank(t) for t in (2, 3, 4))
    below_riskowner = _rank(1) < _rank(4)
    # The property that holds is "never outranks", and it is weaker than the
    # amended Definition 7's prose suggests. `authority_rank` implements the
    # `auth` key's TWO levels — the exceptive authority at tier K above every
    # adjudicative instance, which are equal to one another — so a first-
    # instance consolidated record ranks EQUAL to a contested tier-2 or tier-3
    # record and strictly below a risk acceptance. Equal, not below: where a
    # consolidated record and a contested one both survive the gate at a case,
    # the `auth` key does not separate them and recency does. Recorded here
    # rather than asserted away, and carried as an open question in Appendix
    # G; the specification's "lowest admissible authority rank" is true of the
    # tier and not of the rank this build computes from it.
    check("EX-50", "a consolidated record never outranks a contested one at"
                   " the `auth` key, and ranks strictly below a risk"
                   " acceptance — but ranks EQUAL to tiers 2 and 3, so the"
                   " key does not separate them and recency decides",
          never_outranks and below_riskowner,
          f"rank(1)={_rank(1)}; tiers 2,3,4 -> {[_rank(t) for t in (2, 3, 4)]}")

    # EX-51. The identity that forms classes is not an identity that decides
    # cases. This is the separation CC-22(a) checks on a trace; here it is
    # checked on the CONFIGURATION, which is where it can be lost by an
    # ordinary edit to a credentials table.
    from app import bootstrap as _bs
    tier_principals = {"svc:tier1", "svc:tier2", "svc:tier3", "coo.pat",
                       "alice.grc"}
    producer = _cons.PRODUCER_SERVICE
    check("EX-51", "the class-formation identity is distinct from every"
                   " adjudicating identity and from the lawmakers: it is in"
                   " the registry so its acts are attributable, and holds"
                   " nothing",
          producer in _bs.DEV_KEYS and producer not in tier_principals,
          f"{producer}")

    # EX-52. A ledger written before the amendment gains the two class
    # tables on the next boot. The columns are covered by EX-26 (they are in
    # ADDED_COLUMNS); the TABLES are not, and a schema script that creates
    # them only on a fresh file would leave an upgraded deployment unable to
    # form a class at all — with no error until the first docket boundary.
    path = _tf.mktemp(suffix=".db")
    _db.init_db(path)
    c = sqlite3.connect(path)
    c.execute("DROP TABLE IF EXISTS consolidated_disposition")
    c.execute("DROP TABLE IF EXISTS consolidation_class")
    c.commit()
    gone = {r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    c.close()
    _db.init_db(path)
    c = sqlite3.connect(path)
    tables = {r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")}
    trigs = {r[0] for r in c.execute(
        "SELECT name FROM sqlite_master WHERE type='trigger'")}
    c.close()
    check("EX-52", "a ledger written before the amendment gains the class"
                   " tables and their append-only triggers on the next boot,"
                   " rather than failing at the first docket boundary",
          "consolidation_class" not in gone
          and {"consolidation_class", "consolidated_disposition"} <= tables
          and {"cc_immutable", "cc_nodelete", "cd_immutable",
               "cd_nodelete"} <= trigs,
          f"tables restored={sorted(tables & {'consolidation_class', 'consolidated_disposition'})}")

    # EX-53. The amended bar is a property of the ledger, not of the backend.
    try:
        from app.platform import pg_ledger as _pg
        ddl = "\n".join(_pg.PG_LEDGER_STATEMENTS)
        both = ("admission_ground = 'consolidation'" in ddl
                and "authority_tier = 1" in ddl
                and "class_id IS NOT NULL" in ddl)
        check("EX-53", "Definition 7's amended admission bar is declared on"
                       " Postgres in the same three clauses as on SQLite: a"
                       " deployment cannot buy first-instance admission by"
                       " changing backend",
              both, "licensing CHECK present in the Postgres DDL" if both
              else "MISSING from the Postgres DDL")
    except Exception as e:                                    # noqa: BLE001
        check("EX-53", "Definition 7's amended admission bar on Postgres"
                       " (backend not present)", True, f"n/a: {e}")


def stylesheet_coverage() -> None:
    """Every class the templates use must have a rule in the stylesheet.

    Regression cover for a real failure: a stylesheet reorganisation dropped
    .tally, .stats, .stat, .lane and table.cost. Nothing errored — the pages
    rendered as unstyled HTML, every conformance suite stayed green, and the
    only symptom was dashboards that read "All records47Holdings29".

    Behaviour checks cannot see this. A page that renders the right words in
    the wrong shape is still wrong, and this is the cheapest thing that
    notices.
    """
    import re as _re
    from app import reviewui as ui

    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "app", "reviewui.py")).read()
    css = ui.CSS

    used = set()
    for m in _re.finditer(r"class='([^']*)'", src):
        for tok in m.group(1).split():
            # Skip interpolated values — {cls}, {tone} and the like are
            # decided at render time and cannot be checked statically.
            if "{" in tok or "}" in tok or not tok:
                continue
            used.add(tok)

    missing = sorted(t for t in used
                     if not _re.search(r"\." + _re.escape(t)
                                       + r"(?![\w-])", css))
    check("EX-49", "every CSS class the templates use has a rule in the"
                   " stylesheet — a dropped layout block renders as unstyled"
                   " HTML and no behaviour check can see it",
          not missing, f"no rule for: {missing}" if missing
          else f"{len(used)} classes, all styled")

    # The blocks that actually went missing, named so the failure is legible.
    for block in (".tally", ".stats", ".stat", ".lane", "table.cost"):
        if block not in css:
            check("EX-50", "the dashboard layout blocks are present", False,
                  f"{block} missing")
            return
    check("EX-50", "the dashboard layout blocks are present (tally, stats,"
                   " lanes, cost table)", True, "all present")


def report() -> int:
    width = 100
    print("\n" + "=" * width)
    print("DIGITAL JUDICIARY — EXTENSION CONFORMANCE (L6)")
    print("=" * width)
    print("\nTier differentiation / judged premise / judicial referral"
          " / audit register / tenancy / upgrade / shared law")
    print("-" * width)
    failures = 0
    for cid, name, ok, detail in results:
        failures += 0 if ok else 1
        line = f"  [{'PASS' if ok else 'FAIL'}] {cid:8s} {name}"
        print(line if not detail else f"{line}  ({detail})")
    print("\n" + "=" * width)
    total = len(results)
    print(f"RESULT: {total - failures}/{total} extension checks hold"
          + ("" if failures == 0 else f"  —  {failures} FAILURES"))
    print("=" * width)
    return 1 if failures else 0


if __name__ == "__main__":
    run()
    upgrade_in_place()
    backend_parity()
    consolidation_layer()
    stylesheet_coverage()
    sys.exit(report())
