"""L3 Adjudication: intake, tier-1, resolve(), escalation, risk acceptance.

resolve() runs as the spec's three stages. In one process there is no
Temporal, so the stage boundary is a durability boundary instead: stage 2's
ResolutionArtifact is persisted to case_state before stage 3 admission, so
a crash between them replays admission idempotently (content_hash), never
re-adjudication. The write never re-adjudicates; the judge never runs
inside a ledger transaction.
"""
from __future__ import annotations

import json
import os
import uuid

from . import consolidate, db, judges, kernel
from .db import now_iso
from .judges import THETA
from .kernel import KernelError, canonical, sha256

K = 4                       # tier k: 1..3 automated, 4 = human RiskOwner
SCOPE_RANK = {"service": 3, "team": 2, "domain": 1, "org": 0}


def case_hash(facts: list[str], provision_id: str, rulebook_version: str) -> str:
    return sha256(canonical({"facts": sorted(facts),
                             "provision": provision_id,
                             "rb": rulebook_version}))


def authority_rank(tier: int) -> int:
    """The `auth` key's two levels (Paper 2 Sect. 4.6).

    The exceptive authority — the human RiskOwner at tier K — outranks the
    adjudicative function, and all adjudicative instances are equal. The
    integer in `authority_tier` is the *depth* at which a case was resolved,
    i.e. how many re-adjudications it received; that is a record of resources
    spent, not a conferred institutional power, and ranking on it would rank
    precedent by persistence rather than by legitimacy. The column keeps
    recording it — the ledger, the review screens and the A4 checks all read
    it — but the ordering does not rank on it. The separate `depth` key the
    specification reserves for it is not instantiated here.
    """
    return 1 if tier >= K else 0


def scope_closeness(record: dict, case: dict) -> int:
    """Declared partial order (spec §8.2): narrower is closer when it
    covers the case; a scope that does not cover the case scores lowest."""
    level = record["scope_level"]
    if level == "platform":
        # Shared law covers every case, but is the most general thing that
        # can: a tenant's own org-level holding on the same facts outranks
        # it. Tenant law above platform law.
        return -1
    if level == "org":
        return 0
    rec_val = record["scope"].get(level)
    case_val = case["case_scope"].get(level)
    return SCOPE_RANK[level] if rec_val and rec_val == case_val else -2


def cited_by(record: dict) -> set[str]:
    """Definition 8's `cites`, as this build carries it.

    The schema stores the citation in `renews_record`. A7 requires a
    renewal to name the lapsed acceptance it renews; Sect. 4.6 requires a
    record that supersedes an earlier holding on the same provision to name
    that holding. Both are the one field of Definition 8, used in its two
    roles, which is why this build does not add a column for the second.
    """
    v = record.get("renews_record")
    if not v:
        return set()
    return {v} if isinstance(v, str) else set(v)


def ts_survivors(pool: list[dict]) -> list[dict]:
    """The `ts` key, conditioned on express supersession (Sect. 4.6).

    Recency displaces a *conflicting* record only where the displacement is
    declared. A newer record eliminates an older survivor when the two
    holdings agree — following needs no overruling act, and recency is then
    a tiebreak between records that would decide the case identically — or
    when it names the older record in `cites`. Horizontal stare decisis does
    not let a newer coordinate decision silently reverse an older one; the
    append-only Store has no overruling operation, so the citation is the
    overruling act, recorded. Where the newer record conflicts and is silent
    the two are incomparable on this key, the comparison falls through to
    `scope`, and if nothing separates them the case surfaces as a tie — and
    the tie refers the provision to the Lawmakers — rather than as a quiet
    reversal.
    """
    def outcome(r):
        return (r.get("interpretation") or {}).get("outcome")

    def displaces(newer, older):
        # Following needs no overruling act; departing does. Where the two
        # holdings agree, recency is a mere tiebreak between records that
        # would decide the case identically, and the older one falls. Where
        # they conflict, the newer record displaces only if it says so.
        if newer["resolved_at"] <= older["resolved_at"]:
            return False
        return outcome(newer) == outcome(older) or older["id"] in cited_by(newer)

    superseded = {r["id"] for r in pool
                  if any(displaces(o, r) for o in pool)}
    remaining = [r for r in pool if r["id"] not in superseded]
    return remaining or pool


def order(survivors: list[dict], case: dict):
    """Explicit three-key elimination; ties surface as none_tie.

    The keys are auth, ts, scope. `auth` has two levels only (see
    authority_rank): the exceptive authority above the adjudicative function,
    all adjudicative instances equal. `ts` displaces only where supersession
    is express (see ts_survivors). The specified fourth key, `depth`, is
    not instantiated.

    DJ_ORDER (experiment only) selects the key sequence, e.g. "auth,ts,scope"
    (default), "ts", "auth", "auth,scope,ts". Absent, behaviour is unchanged.
    """
    if not survivors:
        return None, "none_empty", []
    import os as _os
    keys = [k for k in _os.environ.get("DJ_ORDER", "auth,ts,scope").split(",") if k]
    pool = list(survivors)
    for k in keys:
        if len(pool) == 1:
            return pool[0], "bound", []
        if k == "auth":
            top = max(authority_rank(r["authority_tier"]) for r in pool)
            pool = [r for r in pool
                    if authority_rank(r["authority_tier"]) == top]
        elif k == "ts":
            pool = ts_survivors(pool)
        elif k == "scope":
            best = max(scope_closeness(r, case) for r in pool)
            pool = [r for r in pool if scope_closeness(r, case) == best]
    if len(pool) == 1:
        return pool[0], "bound", []
    return None, "none_tie", sorted(r["id"] for r in pool)


def rule_eval(policy: dict, facts: list[str]) -> tuple[str, str]:
    """The embedded stand-in for OPA/Cedar: a declarative predicate over
    the factor set. deny_if_any: any listed factor present -> deny.
    deny_if_missing: any listed factor absent -> deny."""
    fs = set(facts)
    hit = sorted(set(policy.get("deny_if_any", [])) & fs)
    if hit:
        return "deny", f"factors {hit} violate the provision"
    missing = sorted(set(policy.get("deny_if_missing", [])) - fs)
    if missing:
        return "deny", f"required factors {missing} are absent"
    return "permit", "no provision predicate violated"


class Adjudicator:
    def __init__(self, registry: kernel.AuthorityRegistry,
                 constitution: kernel.ConstitutionStore,
                 ledger: kernel.LedgerReader, gate: kernel.ChallengeGate,
                 provenance: kernel.JudgmentProvenance,
                 chain: kernel.ContestChain, path: str | None = None):
        self._w = db.open_writer(path)          # case_state writer only
        self.registry, self.constitution = registry, constitution
        self.ledger, self.gate = ledger, gate
        self.provenance, self.chain = provenance, chain
        self.tier_principal = {1: "svc:tier1", 2: "svc:tier2", 3: "svc:tier3"}

    # ------------------------------------------------------------------
    # Intake + tier 1
    # ------------------------------------------------------------------
    def submit_case(self, provision_id: str, facts: list[str], author: str,
                    case_scope: dict) -> dict:
        rb = self.constitution.current_version()   # pinned here (CC-04)
        # Fixed at submission and carried for the life of the case: with a
        # shared base constitution the clause can no longer say whose ledger
        # a holding joins, so the case must.
        org = (case_scope or {}).get("organization") \
            or self.registry.organization_of(author)
        # The lodged unit's own identifier, where the caller has one. It is
        # kept on the case scope rather than stripped out: scope closeness
        # reads only the service, team and domain keys, so it changes no
        # ordering, and CC-22(c) needs to recover the unit from the trace to
        # re-run Classify against a permuted member list. A determinacy check
        # that cannot name the units is a determinacy check about nothing.
        unit_id = (case_scope or {}).get("unit")
        case_scope = {k: v for k, v in (case_scope or {}).items()
                      if k != "organization"}

        # Control-plane routing (A3, paper Example 3): a change targeting
        # the constitution is never a case.
        if provision_id == "constitution":
            # Carry the CHANGE with the proposal. A referral that tells a
            # lawmaker to "read the pull request" without naming which one is
            # not a proposal, it is a riddle — and until now that is exactly
            # what this filed.
            cp = (case_scope or {}).get("control_plane") or {}
            aid = self.constitution.file_amendment(
                author, "control_plane_routed",
                {"note": "Someone proposed a change to the rulebook itself."
                         " It is not judged as ordinary work: only the"
                         " lawmakers can change a rule.",
                 "changes": [], "change_request": cp},
                # `org`, not case_scope: the tenant was resolved above and
                # then stripped out of the scope dict, so reading it back
                # from there always yielded None and every rulebook change
                # was filed with no company against it.
                organization=org)
            return {"routed": "draft_amendment", "amendment_id": aid,
                    "decision": "not_adjudicated",
                    "rationale": "A3: adjudication holds no amendment"
                                 " authority; proposal filed with the"
                                 " Lawmakers"}

        prov = self.constitution.get_provision(rb, provision_id, org=org)
        case_id = f"C-{uuid.uuid4().hex[:8]}"
        case = {"case_id": case_id, "provision_id": provision_id,
                "rulebook_version": rb, "facts": sorted(facts),
                "author": author, "case_scope": case_scope,
                "organization": org,
                "case_hash": case_hash(facts, provision_id, rb)}

        # A6: absolute short-circuit BEFORE anything else. No retrieval,
        # no judgment batch, no storage, no escalation path (CC-08).
        if prov["absolute"]:
            self._save_case(case, status="denied_absolute", tier=1,
                            artifacts={})
            return {"case_id": case_id, "decision": "deny", "tier": 1,
                    "final": True, "storable": False,
                    "controlling_state": "absolute_short_circuit",
                    "rationale": f"{provision_id} is absolute; nothing to"
                                 " adjudicate. The only exit is a"
                                 " DraftAmendment to the Lawmakers.",
                    "challenge_url": None}

        # Definition 7(ii). A class is formed at a docket boundary, before
        # any member is adjudicated, by Classify — pipeline machinery holding
        # no authority. What happens here is the consequence of a class that
        # already exists: the representative is adjudicated once and its
        # record admitted at first instance; every other member is disposed by
        # direct citation of that record, with no retrieval and no gate
        # invocation. Nothing on this path decides WHICH unit becomes law —
        # that was fixed by the published total order when the class formed.
        cls = self._class_for(case, unit_id)
        if cls is not None:
            rep_record = self._consolidated_record(cls["class_id"])
            if rep_record is None:
                if unit_id is not None and unit_id != cls["representative"]:
                    raise KernelError(
                        f"Def.7(ii): {unit_id} is not the representative of"
                        f" {cls['class_id']} ({cls['representative']} is);"
                        " the representative resolves first", 409)
                return self._adjudicate_representative(case, cls)
            return self._dispose_by_citation(case, cls, rep_record, unit_id)

        artifact = self._adjudicate_at_tier(case, tier=1)
        self._save_case(case, status="decided_t1", tier=1,
                        artifacts={1: artifact})
        d = artifact["decision"]
        return {"case_id": case_id, "decision": d["interpretation"]["outcome"],
                "tier": 1, "final": False,
                "conditions": d.get("conditions"),
                "consulted": [c["record_id"]
                              for c in artifact["retrieval"]["candidates"]],
                "controlling": artifact["ordering"].get("controlling_id"),
                "controlling_state": artifact["ordering"]["controlling_state"],
                "degradations": artifact["degradations"],
                "rationale": d["rationale_text"],
                "challenge_url": f"/v1/decisions/{case_id}/challenge"}

    # ------------------------------------------------------------------
    # Consolidation (Definitions 15, 16; Definition 7 clause (ii))
    # ------------------------------------------------------------------
    def _class_for(self, case: dict, unit_id: str | None) -> dict | None:
        """The formed class covering this unit's signature, or None.

        Signature equality is decidable from published data — the provision
        and rulebook version are recorded on the unit, F_p is published in the
        constitution, and facts(c) is the deterministic extraction the
        interface suite already checks — so this lookup reads nothing an
        auditor could not recompute.
        """
        prov = self.constitution.get_provision(
            case["rulebook_version"], case["provision_id"],
            org=case.get("organization"))
        sig = consolidate.signature(
            case["provision_id"], case["rulebook_version"], case["facts"],
            consolidate.factor_vocabulary(prov))
        row = self._w.execute(
            "SELECT * FROM consolidation_class"
            " WHERE provision_id=? AND rulebook_version=? AND signature=?",
            (sig[0], sig[1], json.dumps(list(sig[2])))).fetchone()
        if row is None:
            return None
        # Membership is fixed when the class forms and is not rediscovered
        # here. A unit that shares the signature but was excluded by clause
        # (b) or (c), or that was lodged after the boundary, is NOT a member
        # and is adjudicated on its own — which is what those clauses mean.
        # A caller that lodges no unit identifier is not at a docket boundary
        # at all, and consolidation never fires for it.
        if unit_id is None or unit_id not in json.loads(row["members"]):
            return None
        return dict(row)

    def _consolidated_record(self, class_id: str):
        row = self._w.execute(
            "SELECT * FROM precedent_record WHERE class_id=?",
            (class_id,)).fetchone()
        return dict(row) if row else None

    def _adjudicate_representative(self, case: dict, cls: dict) -> dict:
        """The representative resolves first, and its record is admitted under
        clause (ii). It is an ordinary first-instance adjudication in every
        respect except its admission: retrieval runs, the gate runs, and the
        holding is the adjudicator's. What consolidation supplies is the
        admission, not the decision."""
        artifact = self._adjudicate_at_tier(case, tier=1)
        self._save_case(case, status="final", tier=1,
                        artifacts={1: artifact})
        record_id = self.gate.admit(
            artifact, admission_ground="consolidation",
            class_id=cls["class_id"])
        self._update_case(case["case_id"], status="final", tier=1,
                          final_record_id=record_id)
        d = artifact["decision"]
        return {"case_id": case["case_id"],
                "decision": d["interpretation"]["outcome"], "tier": 1,
                "final": False,
                "conditions": d.get("conditions"),
                "consulted": [c["record_id"]
                              for c in artifact["retrieval"]["candidates"]],
                "controlling": artifact["ordering"].get("controlling_id"),
                "controlling_state": artifact["ordering"]["controlling_state"],
                "degradations": artifact["degradations"],
                "record_id": record_id,
                "consolidation": {"class_id": cls["class_id"],
                                  "role": "representative",
                                  "members": json.loads(cls["members"])},
                "rationale": d["rationale_text"],
                "challenge_url":
                    f"/v1/decisions/{case['case_id']}/challenge"}

    def _dispose_by_citation(self, case: dict, cls: dict, rep: dict,
                             unit_id: str | None) -> dict:
        """A non-representative member. Disposed against the pinned snapshot
        plus the representative's record, by direct citation of that record.

        No retrieval log is written and no `distinguish` is invoked, which is
        the whole of what consolidation buys: it removes one term from
        Proposition 6(iii)'s sum per member. Proposition 2 (Determinacy) is
        what licenses it — `resolve` reads only prov, facts and S, and every
        member computed the same Consulted and Controlling against S_t as the
        representative did, so the record just written now controls each.

        The member retains its contest path. A member whose disposition is
        contested escalates on its own history and is re-adjudicated on its
        own facts; if resolved above first instance it enters the store by
        clause (i) like any other contested case. Consolidation admits the
        representative and nothing else.
        """
        interp = json.loads(rep["interpretation"])
        artifact = {
            "artifact_version": "1.0",
            "case": {**{k: case[k] for k in
                        ("case_id", "case_hash", "provision_id",
                         "rulebook_version", "facts", "author")},
                     "organization": case.get("organization")},
            "tier": 1,
            "resolving_principal": self.tier_principal.get(1, "unknown"),
            # No retrieval ran. The candidate set is the single cited record,
            # and theta is recorded as None so that nothing downstream reads
            # this as a threshold result.
            "retrieval": {"theta": None, "snapshot_at": now_iso(),
                          "by_citation": True,
                          "class_id": cls["class_id"],
                          "snapshot_hash": cls["snapshot_hash"],
                          "candidates": [{"record_id": rep["id"],
                                          "content_hash":
                                              rep["content_hash"]}]},
            # No gate invocation. An empty verdict list is the honest record
            # of that, and CC-19 recomputes what the gate WOULD have returned
            # rather than trusting this.
            "judgments": {"batch_id": f"cite:{cls['class_id']}",
                          "verdicts": []},
            "ordering": {"keys_applied": [], "controlling_state": "bound",
                         "controlling_id": rep["id"], "tie_members": None},
            "decision": {"interpretation": interp,
                         "conditions": json.loads(rep["conditions"])
                         if rep["conditions"] else None,
                         "premise": json.loads(rep["premise"]),
                         "rationale_text":
                             (f"Consolidated with {cls['class_id']}: this"
                              f" unit's signature is that of the class, and"
                              f" the representative's record {rep['id']}"
                              f" controls it by direct citation. No retrieval"
                              f" and no distinguishing were run, and none"
                              f" could have changed the outcome — every"
                              f" member computed the same Consulted and"
                              f" Controlling against the pinned snapshot."
                              f" Contest remains open on this unit's own"
                              f" facts."),
                         "scope": case["case_scope"], "scope_level": "org",
                         "is_acceptance": False},
            "degradations": [],
            "resolved_at": now_iso(),
        }
        self._save_case(case, status="final", tier=1, artifacts={1: artifact})
        self._w.execute(
            "INSERT INTO consolidated_disposition (class_id, member_unit,"
            " case_id, cites_record, disposition, decided_at)"
            " VALUES (?,?,?,?,?,?)",
            (cls["class_id"], unit_id or case["case_id"], case["case_id"],
             rep["id"], interp["outcome"], now_iso()))
        self._w.commit()
        return {"case_id": case["case_id"], "decision": interp["outcome"],
                "tier": 1, "final": False,
                "conditions": artifact["decision"]["conditions"],
                "consulted": [rep["id"]],
                "controlling": rep["id"],
                "controlling_state": "bound",
                "degradations": [],
                "consolidation": {"class_id": cls["class_id"],
                                  "role": "member",
                                  "cites": rep["id"]},
                "rationale": artifact["decision"]["rationale_text"],
                "challenge_url":
                    f"/v1/decisions/{case['case_id']}/challenge"}

    def classify_probe(self, provision_id: str, facts: list[str],
                       org: str | None) -> str:
        """Clause (d) of Definition 16, evaluated without writing anything.

        `resolve` reads only (prov, facts, S) — Proposition 2 — so its result
        can be recomputed exactly. It is recomputed here rather than invoked,
        because `resolve` as the service runs it writes a retrieval log and a
        judgment batch, and CC-22(b) requires that no judgment invocation for
        any member predate the class artefact. Classify must therefore be able
        to look without leaving a mark, and this is the only place in the
        package that does. The judge object it calls touches no database.
        """
        rb = self.constitution.current_version()
        case = {"case_id": "classify-probe", "provision_id": provision_id,
                "rulebook_version": rb, "facts": sorted(facts),
                "author": consolidate.PRODUCER_SERVICE, "case_scope": {},
                "organization": org,
                "case_hash": case_hash(facts, provision_id, rb)}
        candidates = self.ledger.retrieve(case, THETA, org=org)
        judge = self.provenance.for_tier(1)
        survivors = [c for c in candidates
                     if not judge.distinguish(c, case)["distinguished"]]
        _ctrl, state, _ties = order(survivors, case)
        if state == "none_empty" and candidates:
            state = "none_all_distinguished"
        return state

    def live_store(self, org: str | None = None) -> list[dict]:
        """S_t. The class artefact pins this by content hash, and CC-19
        recomputes `resolve` against exactly it."""
        rows = self._w.execute(
            "SELECT * FROM record_effective"
            " WHERE lapsed = 0 AND superseded = 0"
            + (" AND (organization IS NULL OR organization = ?)"
               if org else ""),
            (org,) if org else ()).fetchall()
        return [dict(r) for r in rows]

    # ------------------------------------------------------------------
    # resolve(): stage 1 retrieve, stage 2 judge & order
    # ------------------------------------------------------------------
    def _resolve(self, case: dict, tier: int = 0,
                 org: str | None = None) -> dict:
        batch_id = str(uuid.uuid4())
        candidates = self.ledger.retrieve(case, THETA, org=org)
        self.gate.log_retrieval(case["case_id"], case["provision_id"],
                                THETA, len(candidates))

        verdicts, degradations = {}, []
        # One round trip per batch instead of one per candidate. The verdicts
        # come back in the same order and are recorded identically, so this
        # is a wall-clock change only — the conformance suites are the proof.
        answers = self.provenance.distinguish_many(batch_id, candidates,
                                                   case, tier)
        for cand in candidates:
            v = answers[cand["id"]]
            verdicts[cand["id"]] = v
            if v["degraded"]:
                degradations.append({"kind": "distinguish_degraded",
                                     "candidate": cand["id"]})

        def outcome_with(vd):
            survivors = [c for c in candidates
                         if not vd[c["id"]]["distinguished"]]
            ctrl, state, ties = order(survivors, case)
            if state == "none_empty" and candidates:
                # Distinct causes, distinct record: nothing retrieved vs
                # everything distinguished (schema controlling_state).
                state = "none_all_distinguished"
            return ctrl, state, ties

        controlling, state, ties = outcome_with(verdicts)

        # Pivotality (spec §8.2): flip each verdict; if the controlling
        # outcome changes, that verdict is pivotal -> quorum.
        pivotal_ids = []
        for cand in candidates:
            flipped = dict(verdicts)
            flipped[cand["id"]] = {
                **verdicts[cand["id"]],
                "distinguished": not verdicts[cand["id"]]["distinguished"]}
            c2, s2, _ = outcome_with(flipped)
            if (s2 != state) or ((c2 or {}).get("id")
                                 != (controlling or {}).get("id")):
                pivotal_ids.append(cand["id"])

        pivotal_degraded = False
        for cand in candidates:
            if cand["id"] in pivotal_ids:
                if verdicts[cand["id"]]["degraded"]:
                    pivotal_degraded = True
                elif not verdicts[cand["id"]]["from_cache"]:
                    q = self.provenance.quorum(batch_id, cand, case, tier)
                    verdicts[cand["id"]] = q
                    if q.get("quorum_disagreement"):
                        degradations.append({"kind": "quorum_disagreement",
                                             "candidate": cand["id"]})
                    pivotal_degraded = pivotal_degraded or q["degraded"]
        controlling, state, ties = outcome_with(verdicts)

        return {"batch_id": batch_id, "candidates": candidates,
                "verdicts": verdicts, "controlling": controlling,
                "state": state, "ties": ties,
                "degradations": degradations,
                "pivotal_degraded": pivotal_degraded}

    def _adjudicate_at_tier(self, case: dict, tier: int) -> dict:
        prov = self.constitution.get_provision(case["rulebook_version"],
                                               case["provision_id"],
                                               org=case.get("organization"))
        r = self._resolve(case, tier, org=case.get("organization"))
        eval_outcome, eval_reason = rule_eval(prov["policy"], case["facts"])

        if r["pivotal_degraded"]:
            # §12: pivotal uncertainty does not decide — surface as a
            # degraded none; the escalation path is the remedy.
            state, controlling = "none_degraded", None
        else:
            state, controlling = r["state"], r["controlling"]

        if state == "bound":
            interp = dict(controlling["interpretation"])
            conditions = controlling.get("conditions")
            premise = controlling["premise"]
            rationale = (f"Controlling precedent {controlling['id']}"
                         f" (tier {controlling['authority_tier']},"
                         f" {controlling['resolved_at'][:10]}): decision"
                         " mirrors its holding. Binding, not advisory.")
        else:
            interp = {"outcome": eval_outcome}
            conditions = None
            # Stored, and read by people. The state name is kept in the
            # artifact for machines; the sentence a person reads should be a
            # sentence.
            why = {
                "none_empty": "No earlier decision covered these facts",
                "none_all_distinguished": "Earlier decisions were looked at"
                                          " but none fitted these facts",
                "none_tie": "Earlier decisions conflicted and could not be"
                            " ranked against each other",
            }.get(state, f"No earlier decision controlled ({state})")
            rationale = (f"{why}, so {case['provision_id']} was applied"
                         f" directly: {eval_reason}. This is the kind of"
                         f" decision most worth contesting if you disagree.")
            # Nothing controlled, so this resolution may become the holding a
            # later case is measured against. What the holding RESTS on is
            # therefore a real decision, not bookkeeping: recording every
            # fact as material produces a precedent that any case missing any
            # detail can distinguish away.
            if judges.premise_mode() == "judged":
                pp = self.provenance.propose_premise(
                    r["batch_id"], case, tier, eval_outcome,
                    case["provision_id"], eval_reason)
                premise = pp["premise"]
                if pp.get("degraded"):
                    r["degradations"].append({"kind": "premise_degraded"})
                else:
                    rationale += (f" Holding rests on {premise}:"
                                  f" {pp.get('grounds', '')}")
            else:
                premise = sorted(case["facts"])

        return {
            "artifact_version": "1.0",
            # The tenant travels ON the artifact. Without it the Gate falls
            # back to the provision's owner, which is NULL for a shared base
            # clause — and a tenant's holding would silently be admitted as
            # platform law, readable by every other tenant.
            "case": {**{k: case[k] for k in
                        ("case_id", "case_hash", "provision_id",
                         "rulebook_version", "facts", "author")},
                     "organization": case.get("organization")},
            "tier": tier,
            "resolving_principal": self.tier_principal.get(tier, "unknown"),
            "retrieval": {"theta": THETA,
                          "snapshot_at": now_iso(),
                          "candidates": [{"record_id": c["id"],
                                          "content_hash": c["content_hash"]}
                                         for c in r["candidates"]]},
            "judgments": {"batch_id": r["batch_id"],
                          "verdicts": [
                              {"record_id": cid,
                               "distinguished": v["distinguished"],
                               "grounds": v["grounds"],
                               "degraded": v["degraded"]}
                              for cid, v in r["verdicts"].items()]},
            "ordering": {"keys_applied": ["authority", "recency", "scope"],
                         "controlling_state": state,
                         "controlling_id": (controlling or {}).get("id"),
                         "tie_members": r["ties"] or None},
            "decision": {"interpretation": interp, "conditions": conditions,
                         "premise": premise, "rationale_text": rationale,
                         "scope": case["case_scope"], "scope_level": "org",
                         "is_acceptance": False},
            "degradations": r["degradations"],
            "resolved_at": now_iso(),
        }

    # ------------------------------------------------------------------
    # Escalation (challenge path)
    # ------------------------------------------------------------------
    def challenge(self, case_id: str, challenger: str, grounds: str) -> dict:
        cs = self._load_case(case_id)
        if cs is None:
            raise KernelError("case not found", 404)
        if cs["status"] in ("final", "denied_absolute"):
            raise KernelError(
                "no escalation path: case is final"
                + (" (absolute provision, A6)"
                   if cs["status"] == "denied_absolute" else ""), 409)
        if self.registry.resolve_branch(challenger) is None \
                and not self._principal_exists(challenger):
            raise KernelError("challenger must be an authenticated"
                              " principal", 403)
        if not grounds.strip():
            raise KernelError("grounds are mandatory", 422)

        contested_tier = cs["current_tier"]
        self.chain.append(case_id, contested_tier, challenger, grounds)
        next_tier = contested_tier + 1

        if next_tier >= K:
            # Automated tiers exhausted -> the human RiskOwner (A4).
            self._update_case(case_id, status="awaiting_risk_owner",
                              tier=K)
            guard = self._renewal_guard(cs)
            return {"case_id": case_id, "status": "awaiting_risk_owner",
                    "tier": K, "renewal_guard": guard}

        case = self._case_dict(cs)
        artifact = self._adjudicate_at_tier(case, next_tier)
        artifacts = json.loads(cs["artifacts"])
        artifacts[str(next_tier)] = artifact
        self._update_case(case_id, status="escalated", tier=next_tier,
                          artifacts=artifacts)
        d = artifact["decision"]
        return {"case_id": case_id, "tier": next_tier,
                "decision": d["interpretation"]["outcome"],
                "controlling": artifact["ordering"].get("controlling_id"),
                "controlling_state": artifact["ordering"]["controlling_state"],
                "rationale": d["rationale_text"],
                "accept_url": f"/v1/decisions/{case_id}/accept",
                "challenge_url": f"/v1/decisions/{case_id}/challenge"}

    # ------------------------------------------------------------------
    # Judicial referral to the legislature (A3-compatible)
    # ------------------------------------------------------------------
    def _maybe_refer(self, record_id: str, artifact: dict) -> str | None:
        """Report upward that the rulebook is underdetermined.

        A3 forbids adjudication from ENACTING an amendment. It does not
        forbid proposing one, and the schema already separates the two: only
        `decide_amendment` requires the lawmakers branch. A tier that has just
        been forced to resolve an unbroken conflict, or that is watching the
        same provision get risk-accepted over and over, is holding exactly the
        evidence a legislature needs — and until now that evidence was
        computed and thrown away.

        Fires only on RECORDED resolutions (depth >= 2), so the unchallenged
        tier-1 mass cannot flood the legislature (Prop. 3 posture).
        """
        if os.environ.get("DJ_JUDICIAL_REFERRAL", "1") != "1":
            return None
        o, d = artifact["ordering"], artifact["decision"]
        pid = artifact["case"]["provision_id"]
        who = artifact["resolving_principal"]

        if o["controlling_state"] == "none_tie":
            members = sorted(o.get("tie_members") or [])
            return self._file_referral(
                # Provision-scoped, not member-scoped. An unbroken conflict
                # on a provision is one legislative question — "which reading
                # governs?" — however many records are tangled in it, and the
                # tangle can grow: a tier that resolves a tie by direct
                # interpretation writes a record that cites nothing, so under
                # express supersession (Sect. 4.6) it displaces neither of the
                # conflicting records and the conflict recurs with one more
                # member. Re-filing then would flood the legislature with the
                # same question. The repeat-acceptance referral above is keyed
                # the same way, for the same reason.
                key=f"tie:{pid}", provision_id=pid,
                proposed_by=who, source_record=record_id,
                trigger="unbroken_conflict",
                note=(f"{pid} produced an unbroken conflict: records"
                      f" {members} are of equal authority, equal recency and"
                      f" equal scope, so the declared ordering cannot"
                      f" separate them. The tier resolved by direct"
                      f" interpretation. Only the lawmakers can settle which"
                      f" reading governs."),
                evidence={"tie_members": members})

        if d.get("is_acceptance"):
            n = self._w.execute(
                "SELECT COUNT(*) AS c FROM precedent_record"
                " WHERE provision_id=? AND is_acceptance=1",
                (pid,)).fetchone()["c"]
            threshold = int(os.environ.get("DJ_REFERRAL_ACCEPTANCE_N", "3"))
            if n >= threshold:
                return self._file_referral(
                    key=f"acceptances:{pid}", provision_id=pid,
                    proposed_by=who, source_record=record_id,
                    trigger="repeat_acceptance",
                    note=(f"{pid} has now been risk-accepted {n} times. A"
                          f" provision that must be waived repeatedly is"
                          f" either mis-scoped or out of date; that is a"
                          f" legislative question, not an adjudicative one."),
                    evidence={"acceptance_count": n})
        return None

    def _file_referral(self, key: str, provision_id: str, proposed_by: str,
                       source_record: str, trigger: str, note: str,
                       evidence: dict) -> str | None:
        """Idempotent: one open referral per distinct concern."""
        for row in self._w.execute(
                "SELECT body FROM draft_amendment WHERE"
                " origin='judicial_referral' AND status='pending'"
        ).fetchall():
            try:
                if json.loads(row["body"]).get("referral_key") == key:
                    return None
            except json.JSONDecodeError:
                continue
        return self.constitution.file_amendment(
            proposed_by, "judicial_referral",
            {"referral_key": key, "provision_id": provision_id,
             "trigger": trigger, "note": note, "evidence": evidence,
             "changes": []},
            source_record=source_record,
            # The referral belongs to the tenant whose clause provoked it.
            organization=self._w.execute(
                "SELECT organization FROM precedent_record WHERE id = ?",
                (source_record,)).fetchone()["organization"])

    def accept_resolution(self, case_id: str, actor: str) -> dict:
        """Challenger accepts the current tier's resolution -> final; if
        depth >= 2 the eventual resolution is admitted (Def. 7 admits the
        final resolution, not intermediate steps)."""
        cs = self._load_case(case_id)
        if cs is None:
            raise KernelError("case not found", 404)
        tier = cs["current_tier"]
        artifacts = json.loads(cs["artifacts"])
        record_id = None
        if tier >= 2:
            record_id = self.gate.admit(artifacts[str(tier)])
            self._maybe_refer(record_id, artifacts[str(tier)])
        self._update_case(case_id, status="final", tier=tier,
                          final_record_id=record_id)
        return {"case_id": case_id, "final": True, "tier": tier,
                "record_id": record_id}

    # ------------------------------------------------------------------
    # Risk acceptance (tier k)
    # ------------------------------------------------------------------
    def _renewal_guard(self, cs) -> dict:
        """A7 / Proposition 2: evaluated BEFORE the RiskOwner decides."""
        case = self._case_dict(cs)
        lapsed = self.ledger.lapsed_similar_acceptance(case, THETA)
        if not lapsed:
            return {"state": "clear", "predecessor": None}
        events = self.ledger.lifecycle(lapsed["id"])
        ref = next((e for e in events
                    if e["event_type"] == "referral_emitted"), None)
        amendment_id = json.loads(ref["payload"])["amendment_id"] if ref else None
        status = "pending"
        if amendment_id:
            row = self.constitution.get_amendment(amendment_id)
            status = row["status"] if row else "pending"
        if status in ("rejected", "withdrawn"):
            return {"state": "barred", "predecessor": lapsed["id"],
                    "referral": amendment_id, "referral_status": status}
        return {"state": "must_cite", "predecessor": lapsed["id"],
                "referral": amendment_id, "referral_status": status}

    def risk_decision(self, case_id: str, principal: str, decision: str,
                      rationale: str, expiry: str | None = None) -> dict:
        self.registry.require_branch(principal, "risk_owner")
        cs = self._load_case(case_id)
        if cs is None or cs["status"] != "awaiting_risk_owner":
            raise KernelError("case is not awaiting the RiskOwner", 409)
        artifacts = json.loads(cs["artifacts"])
        base = artifacts[str(K - 1)]          # tier k adopts the k-1 trail

        guard = self._renewal_guard(cs)
        if decision == "accept":
            if guard["state"] == "barred":
                raise KernelError(
                    "Proposition 2: the Lawmakers rejected the referral of"
                    f" lapsed acceptance {guard['predecessor']}"
                    f" (amendment {guard['referral']}); a materially"
                    " similar acceptance is barred. The only exit is the"
                    " amendment channel.", 422)
            if not expiry:
                raise KernelError("A7: acceptance requires an expiry", 422)
            renews = guard["predecessor"] if guard["state"] == "must_cite" \
                else None
            interp = {"outcome": "accept_risk"}
            is_acceptance = True
            text = (f"RiskOwner {principal} accepts residual risk:"
                    f" {rationale}. Mandatory expiry {expiry};"
                    " DraftAmendment referral emitted (A7)."
                    + (f" Renews lapsed acceptance {renews}"
                       f" (referral pending)." if renews else ""))
        elif decision == "decline":
            interp = {"outcome": "deny"}
            is_acceptance, expiry, renews = False, None, None
            text = (f"RiskOwner {principal} declines to accept the residual"
                    f" risk; the tier-{K-1} denial is upheld under the"
                    f" RiskOwner's name. {rationale}")
        else:
            raise KernelError("decision must be accept|decline", 422)

        artifact = {
            **base,
            "tier": K,
            "resolving_principal": principal,
            "decision": {**base["decision"],
                         "interpretation": interp,
                         "rationale_text": text,
                         "is_acceptance": is_acceptance,
                         "expiry": expiry,
                         "renews_record": renews},
            "resolved_at": now_iso(),
        }
        record_id = self.gate.admit(artifact)
        self._maybe_refer(record_id, artifact)
        self._update_case(case_id, status="final", tier=K,
                          final_record_id=record_id)
        return {"case_id": case_id, "final": True, "tier": K,
                "record_id": record_id, "decision": interp["outcome"],
                "expiry": expiry, "renews_record": renews}

    # ------------------------------------------------------------------
    # case_state helpers
    # ------------------------------------------------------------------
    def _save_case(self, case: dict, status: str, tier: int,
                   artifacts: dict) -> None:
        self._w.execute(
            "INSERT INTO case_state (case_id, case_hash, provision_id,"
            " rulebook_version, facts, author, case_scope, status,"
            " current_tier, artifacts, created_at, updated_at,"
            " organization)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (case["case_id"], case["case_hash"], case["provision_id"],
             case["rulebook_version"], canonical(case["facts"]),
             case["author"], canonical(case["case_scope"]), status, tier,
             canonical({str(k): v for k, v in artifacts.items()}),
             now_iso(), now_iso(), case.get("organization")))
        self._w.commit()

    def _update_case(self, case_id: str, status: str, tier: int,
                     artifacts: dict | None = None,
                     final_record_id: str | None = None) -> None:
        if artifacts is not None:
            self._w.execute(
                "UPDATE case_state SET status=?, current_tier=?,"
                " artifacts=?, updated_at=? WHERE case_id=?",
                (status, tier, canonical(artifacts), now_iso(), case_id))
        else:
            self._w.execute(
                "UPDATE case_state SET status=?, current_tier=?,"
                " final_record_id=COALESCE(?, final_record_id),"
                " updated_at=? WHERE case_id=?",
                (status, tier, final_record_id, now_iso(), case_id))
        self._w.commit()

    def _load_case(self, case_id: str):
        return self._w.execute("SELECT * FROM case_state WHERE case_id=?",
                               (case_id,)).fetchone()

    def _case_dict(self, cs) -> dict:
        return {"case_id": cs["case_id"], "case_hash": cs["case_hash"],
                "provision_id": cs["provision_id"],
                "rulebook_version": cs["rulebook_version"],
                "facts": json.loads(cs["facts"]), "author": cs["author"],
                "case_scope": json.loads(cs["case_scope"]),
                # Reloaded on every challenge, so an escalated case keeps the
                # tenant it was filed under rather than picking one up from
                # whoever contested it.
                "organization": (cs["organization"]
                                 if "organization" in cs.keys() else None)}

    def _principal_exists(self, principal_id: str) -> bool:
        return self._w.execute(
            "SELECT 1 FROM principal WHERE principal_id=?",
            (principal_id,)).fetchone() is not None

    def get_case(self, case_id: str) -> dict | None:
        cs = self._load_case(case_id)
        if cs is None:
            return None
        return {**self._case_dict(cs), "status": cs["status"],
                "current_tier": cs["current_tier"],
                "final_record_id": cs["final_record_id"]}
