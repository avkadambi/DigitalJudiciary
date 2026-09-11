"""
SemiFab conformance suite.

Replays the corpus independently of the generator and computes forty-four
checks (VC-01 … VC-44) from the executed trace. Nothing here is asserted from
the case files; every check is a query over what the run actually did.

    python3 harness/run_conformance.py

Exit code 0 when every check passes, 1 otherwise.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import engine  # noqa: E402
import extensions as X  # noqa: E402
R = engine

CHECKS: list[tuple] = []


def check(cid, description):
    def deco(fn):
        CHECKS.append((cid, description, fn))
        return fn
    return deco


def load():
    with open(os.path.join(ROOT, "constitution", "rulebook.json")) as fh:
        rulebook = json.load(fh)
    with open(os.path.join(ROOT, "constitution", "parameters.json")) as fh:
        params = json.load(fh)
    with open(os.path.join(ROOT, "corpus", "cases.json")) as fh:
        pack = json.load(fh)
    with open(os.path.join(ROOT, "corpus", "store_seed_initial.json")) as fh:
        seed = json.load(fh)["records"]
    engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))
    provisions = {p["id"]: engine.Provision.from_dict(p) for p in rulebook["provisions"]}
    return rulebook, params, pack, seed, provisions


class Run:
    def __init__(self):
        self.rulebook, self.params, self.pack, self.seed, self.provisions = load()
        self.cases = self.pack["cases"]
        self.by_id = {c["id"]: c for c in self.cases}
        self.seed_records = {r["id"]: r for r in self.seed}
        self.result = self._replay()
        self.traces = {t["case"]: t for t in self.result["traces"]}
        self.store = self.result["store"]
        self.docket = self.result["docket"]

    def _replay(self):
        # Independent replay through engine.replay, mirroring the corpus order.
        return engine.replay(self.cases, self.seed, self.provisions,
                             self.params["theta"])


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


@check("VC-01", "Replay reproduces every case's recorded decision")
def vc01(r):
    bad = [c["id"] for c in r.cases
           if r.traces[c["id"]]["decision"] != c["expect"]["final_decision"]]
    return not bad, f"{len(bad)} decision mismatches", bad[:5]


@check("VC-02", "Replay reproduces every case's recorded route")
def vc02(r):
    bad = [c["id"] for c in r.cases
           if r.traces[c["id"]]["route"] != c["expect"]["route"]]
    return not bad, f"{len(bad)} route mismatches", bad[:5]


@check("VC-03", "Seeded jurisprudence binds only where its admission ground says 'seed'")
def vc03(r):
    seeded = {rid for rid, rec in r.seed_records.items()
              if rec["admission_ground"] == "seed"}
    cold = [c for c in r.cases if c["category"] == "X-coldstart"]
    bad = [c["id"] for c in cold if r.traces[c["id"]]["controlling"] not in seeded]
    return not bad, f"{len(cold)} cold-start cases, {len(bad)} not controlled by a seeded record", bad[:5]


@check("VC-04", "A3 — no adjudication writes the rulebook; control-plane changes route to a draft amendment; nothing out of force is absolute")
def vc04(r):
    versions = {c["rulebook_version"] for c in r.cases}
    cp = [c for c in r.cases if c["control_plane"]]
    bad = [c["id"] for c in cp if not r.traces[c["id"]].get("draft_amendment")]
    # This pack's constitution carries a status per provision. A provision that
    # is enacted-but-deferred, advisory, or readiness-only, may never be
    # entrenched as absolute:
    # entrenching a rule that does not yet bind would make the architecture
    # stricter than the law it claims to implement.
    out_of_force_absolutes = [p["id"] for p in r.rulebook["provisions"]
                              if p["absolute"] and p.get("status", "in_force") != "in_force"]
    n_def = sum(1 for p in r.rulebook["provisions"] if p.get("status") == "deferred")
    n_adv = sum(1 for p in r.rulebook["provisions"] if p.get("status") == "advisory")
    n_rdy = sum(1 for p in r.rulebook["provisions"] if p.get("status") == "readiness")
    return (len(versions) == 1 and not bad and not out_of_force_absolutes,
            f"{len(cp)} control-plane cases, {len(versions)} rulebook version(s) in force, "
            f"{n_def} deferred, {n_adv} advisory and {n_rdy} readiness provisions, "
            f"{len(out_of_force_absolutes)} of them wrongly absolute",
            (bad + out_of_force_absolutes)[:5])


@check("VC-05", "Every case with more than one survivor records the key that separated them")
def vc05(r):
    bad = []
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["route"] == engine.ROUTE_BOUND and len(t["consulted"]) > 1:
            survivors = _survivors(r, c)
            if len(survivors) > 1 and not t["keys_applied"]:
                bad.append(c["id"])
    return not bad, f"{len(bad)} multi-survivor cases with no recorded key", bad[:5]


@check("VC-06", "A4 — risk acceptance fires only where escalation is exhausted, and only for the risk owner")
def vc06(r):
    bad = [c["id"] for c in r.cases
           if r.traces[c["id"]]["escalated_to"] == "riskowner" and c["contest_to"] < 4]
    bad += [c["id"] for c in r.cases
            if c["contest_to"] >= 4 and r.traces[c["id"]]["escalated_to"] != "riskowner"
            and r.traces[c["id"]]["route"] not in (engine.ROUTE_ABSOLUTE,)]
    return not bad, f"{len(bad)} acceptances outside exhaustion", bad[:5]


@check("VC-07", "Theorem 2 — rebuild is defined and complete on every stored record")
def vc07(r):
    bad = []
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        for field in ("rules", "facts", "premise", "interp", "auth_class",
                      "auth_id", "rationale", "ts", "admission_ground"):
            if d.get(field) in (None, "", []):
                bad.append((d["id"], field))
                break
    return not bad, f"{len(r.store)} records, {len(bad)} incomplete", bad[:5]


@check("VC-08", "A6 — absolute cases show zero retrievals and write zero records")
def vc08(r):
    bad = []
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["route"] == engine.ROUTE_ABSOLUTE:
            if t["consulted"] or t["distinguished"] or t["admitted"] or t["decision"] != engine.DENY:
                bad.append(c["id"])
    n = sum(1 for c in r.cases if r.traces[c["id"]]["route"] == engine.ROUTE_ABSOLUTE)
    return not bad, f"{n} absolute short-circuits, {len(bad)} leaked retrieval or a record", bad[:5]


@check("VC-09", "A7 — every acceptance carries a mandatory expiry and emits a referral")
def vc09(r):
    bad = []
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["escalated_to"] == "riskowner":
            if not (t["expiry_set"] and t["referral_emitted"]):
                bad.append(c["id"])
    n = sum(1 for c in r.cases if r.traces[c["id"]]["escalated_to"] == "riskowner")
    return not bad, f"{n} acceptances, {len(bad)} without expiry or referral", bad[:5]


@check("VC-10", "Lapsed acceptances are excluded at retrieval and never control")
def vc10(r):
    # The domain is every record that can lapse, not only the seeded ones. The
    # run writes hundreds of expiring acceptances of its own, and an earlier
    # form of this check covered the sixteen seed records alone — about four
    # per cent of the population its own name claims.
    expiring = {}
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        if d.get("expiry") is not None:
            expiring[d["id"]] = d
    bad = []
    for c in r.cases:
        t = r.traces[c["id"]]
        seen = t["consulted"] + ([t["controlling"]]
                                 if isinstance(t["controlling"], str) else [])
        for rid in seen:
            rec = expiring.get(rid)
            if rec and c["ts"] > rec["expiry"]:
                bad.append((c["id"], rid))
    n_seed = sum(1 for rid in expiring if rid in r.seed_records)
    return (not bad,
            f"{len(expiring)} records carry an expiry ({n_seed} seeded, "
            f"{len(expiring) - n_seed} written during the run), "
            f"{len(bad)} leaked into retrieval after lapsing",
            bad[:5])


@check("VC-11", "A8 — a bound decision is consistent with the controlling record's holding")
def vc11(r):
    store_by_id = {}
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        store_by_id[d["id"]] = d
    bad = []
    n = 0
    for c in r.cases:
        t = r.traces[c["id"]]
        cid = t["controlling"]
        if isinstance(cid, str) and cid != "none_tie":
            n += 1
            rec = store_by_id.get(cid)
            if rec is None or rec["interp"] != t["decision"]:
                bad.append(c["id"])
    return not bad, f"{n} bound cases, {len(bad)} inconsistent with their holding", bad[:5]


@check("VC-12", "A tie is recorded as none(tie) and refers the conflict to the lawmakers")
def vc12(r):
    ties = [c for c in r.cases if r.traces[c["id"]]["controlling"] == "none_tie"]
    bad = [c["id"] for c in ties if not r.traces[c["id"]]["referral_emitted"]]
    return not bad, f"{len(ties)} ties, {len(bad)} without a referral", bad[:5]


@check("VC-13", "Pressure invariance — a PACT pressure factor changes nothing the trail records")
def vc13(r):
    # Strengthened in this pack. The sibling packs compare the disposition only.
    # Here the twin sits immediately after its control and its control is
    # uncontested, so the two face an identical store — which makes the whole
    # trace comparable, not just its verdict. Five properties are checked:
    # disposition, route, controlling record, consulted set and stored status.
    bad, n, adj = [], 0, 0
    for c in r.cases:
        if c["category"] != "P-pressure":
            continue
        ctrl = r.by_id.get(c["meta"].get("control_case"))
        if not ctrl:
            continue
        n += 1
        if c["ts"] - ctrl["ts"] == 1:
            adj += 1
        a, b = r.traces[c["id"]], r.traces[ctrl["id"]]
        if (a["decision"] != b["decision"]
                or a["route"] != b["route"]
                or a["controlling"] != b["controlling"]
                or sorted(a["consulted"]) != sorted(b["consulted"])
                or a["admitted"] != b["admitted"]):
            bad.append(c["id"])
    mechs = {c["meta"].get("pressure_mechanism") for c in r.cases
             if c["category"] == "P-pressure"}
    return (not bad,
            f"{n} pressure twins over {len(mechs)} PACT mechanisms, {adj} adjacent to "
            f"their control, {len(bad)} diverged on any of disposition, route, "
            f"controlling record, consulted set or stored status",
            bad[:5])


@check("VC-14", "Renewal cites the lapsed record it renews, and none issues after a rejection")
def vc14(r):
    bad = []
    n = 0
    for c in r.cases:
        if c["category"] != "U-renewal":
            continue
        n += 1
        posture = c["meta"]["referral_posture"]
        cites = c["engine"].get("cites", [])
        if posture == "pending":
            if c["meta"]["renews"] not in cites or not r.traces[c["id"]]["expiry_set"]:
                bad.append(c["id"])
        else:
            if r.traces[c["id"]]["expiry_set"]:
                bad.append(c["id"])
    return not bad, f"{n} renewal cases, {len(bad)} violating the renewal rule", bad[:5]


@check("VC-15", "Definition 7 — the store is exactly the contested-and-resolved cases plus one representative per class")
def vc15(r):
    admitted = {c["id"] for c in r.cases if r.traces[c["id"]]["admitted"]}
    expected = {c["id"] for c in r.cases
                if (c["contest_to"] >= 2 and r.traces[c["id"]]["route"] != engine.ROUTE_ABSOLUTE)
                or r.traces[c["id"]]["admission_ground"] == "clause_ii"}
    return (admitted == expected,
            f"{len(admitted)} admitted, {len(expected)} expected by the admission rule",
            sorted(admitted ^ expected)[:5])


@check("VC-16", "Like-case consistency — every engineered pair reaches the same disposition")
def vc16(r):
    bad = []
    for pair in r.pack["like_case_pairs"]:
        a, b = r.traces[pair["a"]], r.traces[pair["b"]]
        if a["decision"] != b["decision"]:
            bad.append((pair["a"], pair["b"]))
    return not bad, f"{len(r.pack['like_case_pairs'])} pairs, {len(bad)} inconsistent", bad[:5]


@check("VC-17", "A9 first limb — a standing declaration exists, attributed and dated")
def vc17(r):
    d = r.rulebook.get("standing_declaration") or {}
    ok = all(k in d for k in ("id", "adverse_contest_standing_exists", "declared_by", "declared_at"))
    return ok, "standing declaration present and attributed" if ok else "missing or unattributed", []


@check("VC-18", "Express supersession — a silent conflicting record displaces nothing")
def vc18(r):
    bad = []
    n = 0
    for c in r.cases:
        if c["category"] != "M-supersession":
            continue
        n += 1
        t = r.traces[c["id"]]
        if c["meta"]["supersession"] == "silent":
            if t["controlling"] != "none_tie":
                bad.append(c["id"])
        else:
            if t["controlling"] != c["meta"]["newer_record"]:
                bad.append(c["id"])
    return not bad, f"{n} supersession cases, {len(bad)} wrong", bad[:5]


@check("VC-19", "Consolidation admits exactly one record per class, under clause (ii)")
def vc19(r):
    classes = {}
    for c in r.cases:
        sig = c.get("consolidation_signature")
        if not sig:
            continue
        classes.setdefault(sig, []).append(c)
    bad = []
    for sig, members in classes.items():
        admitted = [m for m in members if r.traces[m["id"]]["admission_ground"] == "clause_ii"]
        if len(admitted) != 1:
            bad.append(sig)
    return not bad, f"{len(classes)} classes, {len(bad)} without exactly one representative", bad[:5]


@check("VC-20", "Consolidation members are disposed by citation, with no retrieval and no gate")
def vc20(r):
    bad, n = [], 0
    for c in r.cases:
        if c["engine"].get("class_member"):
            n += 1
            t = r.traces[c["id"]]
            if t["consulted"] or t["distinguished"] or not t.get("cites_representative"):
                bad.append(c["id"])
    return not bad, f"{n} class members, {len(bad)} that retrieved or failed to cite", bad[:5]


@check("VC-21", "Inexpressibility — every baseline-differential case is resolved by citation at first instance")
def vc21(r):
    bad, n = [], 0
    for c in r.cases:
        if c["category"] != "Z-inexpressibility":
            continue
        n += 1
        t = r.traces[c["id"]]
        if not isinstance(t["controlling"], str) or t["controlling"] == "none_tie":
            bad.append(c["id"])
        elif not c["meta"].get("b_gov_disposition") or not c["meta"].get("b_mem_disposition"):
            bad.append(c["id"])
    return not bad, f"{n} differential cases, {len(bad)} without a citation or a baseline comparison", bad[:5]


@check("VC-22", "Docket completeness — every uncharged arrival leaves exactly one entry, every charged arrival none")
def vc22(r):
    entries = {e["case"] for e in r.docket}
    uncharged = {c["id"] for c in r.cases
                 if r.traces[c["id"]]["route"] in (engine.ROUTE_DOCKET_DECLINED,
                                                   engine.ROUTE_DOCKET_NULL)}
    dupes = len(r.docket) - len(entries)
    return (entries == uncharged and dupes == 0,
            f"{len(r.docket)} docket entries, {len(uncharged)} uncharged arrivals, {dupes} duplicates",
            sorted(entries ^ uncharged)[:5])


@check("VC-23", "The two docket routes are kept apart")
def vc23(r):
    bad = []
    for e in r.docket:
        if e["route"] == "null":
            if e.get("rules") or e.get("rating") is not None:
                bad.append(e["case"])
        else:
            if e.get("rating") is None or e.get("tau") is None:
                bad.append(e["case"])
    return not bad, f"{len(r.docket)} entries, {len(bad)} conflating the null and declined routes", bad[:5]


@check("VC-24", "Definition 17 — a run with a Reporter publishing is identical to one without")
def vc24(r):
    # This check used to replay the same configuration twice, which tests
    # determinism and calls it observer non-influence. There is now a Reporter
    # object: it reads the store after every case and publishes a bulletin.
    # Three properties, and each is structural rather than promised —
    #   R1 no write:   Reporter exposes no method that mutates a store;
    #   R2 no input:   engine.adjudicate has no reporter parameter to pass it to;
    #   R3 no standing: Reporter has no contest method.
    rep = X.Reporter()
    off = engine.replay(r.cases, r.seed, r.provisions, r.params["theta"])["traces"]
    observed = X.replay_observed(r.cases, r.seed, r.provisions, r.params["theta"],
                                 reporter=rep)
    on = observed["traces"]
    # R1 directly: the Reporter is handed the live store, so a Reporter that
    # wrote to it would show up here as a store that grew while being read.
    plain = engine.replay(r.cases, r.seed, r.provisions, r.params["theta"])
    store_unmoved = len(observed["store"]) == len(plain["store"])
    ha = hashlib.sha256(json.dumps(off, sort_keys=True, default=str).encode()).hexdigest()
    hb = hashlib.sha256(json.dumps(on, sort_keys=True, default=str).encode()).hexdigest()
    no_write = not any(hasattr(X.Reporter, m)
                       for m in ("write", "append", "admit", "contest", "accept"))
    import inspect
    no_input = "reporter" not in inspect.signature(engine.adjudicate).parameters
    return (ha == hb and no_write and no_input and store_unmoved
            and len(rep.bulletins) == len(r.cases),
            f"{len(rep.bulletins)} bulletins published, bulletin digest "
            f"{rep.digest()}; trace digest {ha[:16]} with the Reporter on and "
            f"{hb[:16]} with it off; R1 no-write={no_write} and store unmoved "
            f"under observation={store_unmoved}, R2 no-input={no_input}",
            [])


@check("VC-25", "Definition 19 — the audit register is append-only and disjoint from Store and Docket")
def vc25(r):
    # Previously this asserted that a record id belonging to a never-admitted
    # case appeared in no consulted set, which cannot fail: the record never
    # exists. There is now a register. The audit draws from the docket under a
    # published budget, re-adjudicates advisorily, and writes findings that
    # touch nothing.
    before = [rec.to_dict() if hasattr(rec, "to_dict") else rec for rec in r.store]
    audit = X.docket_audit(r.docket, r.by_id, r.store, r.provisions,
                           rho=r.params.get("audit_budget_rho", 0.25),
                           theta=r.params["theta"])
    after = [rec.to_dict() if hasattr(rec, "to_dict") else rec for rec in r.store]
    store_ids = {d["id"] for d in after}
    docket_cases = {e["case"] for e in r.docket}
    reg = audit["register"].findings
    # Disjointness in both directions, and the store unmoved by the audit.
    leaked = [f for f in reg if f["docket_case"] in store_ids]
    not_from_docket = [f for f in reg if f["docket_case"] not in docket_cases]
    annotation_only = all(f["is_annotation_only"] for f in reg)
    return (before == after and not leaked and not not_from_docket
            and annotation_only and audit["width"] == 0,
            f"{len(reg)} findings drawn from {audit['docket_size']} docket entries "
            f"at budget rho={audit['budget_rho']} (coverage {audit['coverage']:.4f}); "
            f"store unchanged by the audit, width {audit['width']}, "
            f"{audit['disagreements']} advisory disagreements recorded and acted on by nothing",
            [f["docket_case"] for f in leaked + not_from_docket][:5])


@check("VC-26", "A9 second limb — the realised adverse-contest rate is computable as two counts")
def vc26(r):
    grants, adverse = 0, 0
    for c in r.cases:
        t = r.traces[c["id"]]
        unconditioned = (
            t["decision"] == engine.PERMIT
            and t["route"] not in (engine.ROUTE_DOCKET_DECLINED, engine.ROUTE_DOCKET_NULL,
                                   engine.ROUTE_ABSOLUTE)
            and t["escalated_to"] != "riskowner"
        )
        if unconditioned:
            grants += 1
            if c["meta"].get("adverse_contest"):
                adverse += 1
    rate = (adverse / grants) if grants else None
    return (grants > 0 and adverse > 0,
            f"unconditioned first-instance grants={grants}, "
            f"contested by a party other than the requester={adverse}, "
            f"realised adverse-contest rate={rate:.4f}" if grants else "no grants in window",
            [])


def _survivors(r, c):
    case = engine.case_from_dict(c)
    store = [rec if isinstance(rec, engine.Record) else engine.Record.from_dict(rec)
             for rec in r.store]
    # Strictly earlier: a record written by this very case was not in the
    # store when the case was decided.
    live = [rec for rec in store if rec.ts < case.ts]
    cand = engine.retrieve(case, live, r.params["theta"])
    surv, _ = engine.gate(cand, case)
    return surv



# ---------------------------------------------------------------------------
# Checks added to close the gaps between the corpus and the dissertation.
# VC-01..VC-26 test the contract as the base harness stated it; the checks
# below test the parts that the base harness only recorded — the admission
# rule family of Chapter 4, the Reporter and audit register of Chapter 5's
# Definitions 17 and 19, the inexpressibility results of Chapter 5 Section 6,
# and the conformance ids the replication package specifies but never executed.
# ---------------------------------------------------------------------------


def _hist(r):
    if not hasattr(r, "_histories"):
        r._histories = [X.history(c, r.traces[c["id"]], i, r.provisions)
                        for i, c in enumerate(r.cases)]
    return r._histories


@check("VC-27", "CC-26 — the Docket and the Store are disjoint in both directions")
def vc27(r):
    store_ids, cited = set(), set()
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        store_ids.add(d["id"])
        cited |= set(d.get("cites") or [])
    docket_cases = {e["case"] for e in r.docket}
    admitted = {t["case"] for t in r.result["traces"] if t["admitted"]}
    both = docket_cases & admitted
    entry_in_store = {c for c in docket_cases if f"REC-{c}" in store_ids}
    entry_cited = {c for c in docket_cases if f"REC-{c}" in cited}
    return (not both and not entry_in_store and not entry_cited,
            f"{len(docket_cases)} docketed arrivals, {len(admitted)} admitted; "
            f"{len(both)} in both, {len(entry_in_store)} docket entries present "
            f"as records, {len(entry_cited)} cited by a record",
            sorted(both | entry_in_store | entry_cited)[:5])


@check("VC-28", "CC-31 — a consolidated record carries no expiry")
def vc28(r):
    bad, n = [], 0
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        if d.get("admission_ground") == "clause_ii":
            n += 1
            if d.get("expiry") is not None:
                bad.append(d["id"])
    return (not bad,
            f"{n} records admitted under clause (ii), {len(bad)} carrying an expiry",
            bad[:5])


@check("VC-29", "CC-30 — charging integrity: rating exists exactly where the prosecutor charged")
def vc29(r):
    # Charging runs upstream of admission (Chapter 5 Section 4.11): a
    # consolidation member is charged like any arrival and only then disposed
    # by citation, so it carries a rating and that is correct. What CC-30 asks
    # is that the charging predicate be fail-closed and constitutional:
    #   - the null route engages nothing, so it is rated by nothing;
    #   - a rating strictly below the engaged tau ALWAYS declines;
    #   - a rating at or above tau NEVER declines;
    #   - a docketed arrival is never admitted to the store.
    rated_without_charge, charged_without_rating, threshold_breaks = [], [], []
    for c in r.cases:
        t = r.traces[c["id"]]
        docketed = t["route"] in (engine.ROUTE_DOCKET_DECLINED, engine.ROUTE_DOCKET_NULL)
        if t["route"] == engine.ROUTE_DOCKET_NULL and (t["rating"] is not None or t["rules"]):
            rated_without_charge.append(c["id"])
        if t["route"] == engine.ROUTE_DOCKET_DECLINED and t["rating"] is None:
            charged_without_rating.append(c["id"])
        if t["rating"] is not None and t["tau"] is not None:
            below = t["rating"] < t["tau"]
            declined = t["route"] == engine.ROUTE_DOCKET_DECLINED
            if below != declined:
                threshold_breaks.append(c["id"])
        if docketed and t["admitted"]:
            rated_without_charge.append(c["id"])
    bad = rated_without_charge + charged_without_rating + threshold_breaks
    taus = {p["id"]: p["tau"] for p in r.rulebook["provisions"]}
    constitutional = all(isinstance(v, int) for v in taus.values())
    return (not bad and constitutional,
            f"tau published for {len(taus)} provisions and constitutional; "
            f"{len(rated_without_charge)} rated on the null route, "
            f"{len(charged_without_rating)} declined without a rating, "
            f"{len(threshold_breaks)} where the rating and the declined route "
            f"disagree about tau",
            bad[:5])


@check("VC-30", "Definition 18 — every referral is answered with one of the four acknowledgement dispositions")
def vc30(r):
    allowed = {"adopt", "reject", "defer", "decline-to-act"}
    seen, bad = {}, []
    for c in r.cases:
        ack = c["meta"].get("acknowledgement")
        if not ack:
            continue
        d = ack.get("disposition")
        seen[d] = seen.get(d, 0) + 1
        if d not in allowed:
            bad.append(c["id"])
        # A deferral, and only a deferral, sets a review date.
        if (d == "defer") != (ack.get("next_review_ts") is not None):
            bad.append(c["id"])
    return (not bad and set(seen) == allowed,
            f"{sum(seen.values())} acknowledgements over {len(seen)} dispositions "
            + ", ".join(f"{k}={v}" for k, v in sorted(seen.items())),
            bad[:5])


@check("VC-31", "Proposition 0 — retrieval loses no record the gate would have admitted")
def vc31(r):
    bad, n = [], 0
    for c in r.cases[:1200]:
        case = engine.case_from_dict(c)
        t = r.traces[c["id"]]
        if t["route"] == engine.ROUTE_ABSOLUTE:
            continue
        live = [rec for rec in r.store if rec.ts < case.ts and not rec.lapsed_at(case.ts)]
        n += 1
        retrieved = {rec.id for rec in engine.retrieve(case, live, r.params["theta"])}
        # Every record the gate would admit must have survived retrieval.
        would_pass = {rec.id for rec in live
                      if rec.prov in case.rules
                      and set(rec.premise) <= set(case.facts)}
        missed = would_pass - retrieved
        if missed:
            bad.append((c["id"], sorted(missed)[:2]))
    return (not bad,
            f"{n} cases checked; {len(bad)} where a gate-admissible record "
            f"was lost at retrieval",
            bad[:5])


@check("VC-32", "Chapter 4 Proposition 1 — the gate and the ordering do not commute")
def vc32(r):
    # Witness: a case where ordering first would return a record that the gate
    # then discards, and gating first returns a different controlling record.
    witnesses = []
    for c in r.cases:
        case = engine.case_from_dict(c)
        t = r.traces[c["id"]]
        if t["route"] != engine.ROUTE_BOUND or len(t["consulted"]) < 2:
            continue
        live = [rec for rec in r.store if rec.ts < case.ts and not rec.lapsed_at(case.ts)]
        cand = engine.retrieve(case, live, r.params["theta"])
        if len(cand) < 2:
            continue
        gate_first, _ = engine.gate(cand, case)
        if not gate_first:
            continue
        gf, _ = engine.order(gate_first)
        of, _ = engine.order(cand)                    # order the ungated set
        if of is None or gf is None or of == "none_tie" or gf == "none_tie":
            continue
        if of.id != gf.id:
            og, _ = engine.gate([of], case)
            if not og:                                # ordering first picks a
                witnesses.append((c["id"], of.id, gf.id))   # record the gate drops
        if len(witnesses) >= 40:
            break
    return (bool(witnesses),
            f"{len(witnesses)} witnesses where order-then-gate and gate-then-order "
            f"disagree, the ordering-first winner being a record the gate discards",
            witnesses[:5])


@check("VC-33", "Chapter 4 Section 8 — a lower-ranked record controls where the higher-ranked one is distinguished")
def vc33(r):
    store_by_id = {}
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        store_by_id[d["id"]] = d
    witnesses = []
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["route"] != engine.ROUTE_BOUND or not isinstance(t["controlling"], str):
            continue
        ctl = store_by_id.get(t["controlling"])
        if not ctl or ctl["auth_class"] != "judges":
            continue
        higher = [rid for rid in t["distinguished"]
                  if store_by_id.get(rid, {}).get("auth_class") == "riskowner"]
        if higher:
            witnesses.append((c["id"], t["controlling"], higher[0]))
    return (bool(witnesses),
            f"{len(witnesses)} cases where a risk-owner record was distinguished and "
            f"a judges record controlled — the gate runs before the authority key, "
            f"so vertical precedent is thin rather than thick",
            witnesses[:5])


@check("VC-34", "Theorem 5 — the constraint relation is non-monotonic in the case base")
def vc34(r):
    # (i) adding a record flips the required outcome; (ii) adding a record turns
    # Controlling from a record into none(tie). Both are witnessed by replaying
    # a case against its own store with and without one later record.
    flips, collapses = [], []
    store_sorted = sorted(r.store, key=lambda rec: rec.ts)
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["route"] not in (engine.ROUTE_BOUND, engine.ROUTE_TIE):
            continue
        case = engine.case_from_dict(c)
        live = [rec for rec in store_sorted
                if rec.ts < case.ts and not rec.lapsed_at(case.ts)]
        base_ctl, _ = engine.order(engine.gate(
            engine.retrieve(case, live, r.params["theta"]), case)[0])
        if base_ctl is None:
            continue
        for extra in store_sorted:
            if extra.ts < case.ts or extra.prov not in case.rules:
                continue
            if not set(extra.premise) <= set(case.facts):
                continue
            aug = live + [engine.Record(**{**extra.__dict__, "ts": case.ts - 1})]
            new_ctl, _ = engine.order(engine.gate(
                engine.retrieve(case, aug, r.params["theta"]), case)[0])
            if new_ctl == "none_tie" and base_ctl != "none_tie":
                collapses.append((c["id"], extra.id))
            elif (new_ctl not in (None, "none_tie") and base_ctl not in (None, "none_tie")
                  and new_ctl.interp != base_ctl.interp):
                flips.append((c["id"], extra.id))
            break
        if len(flips) >= 20 and len(collapses) >= 5:
            break
    return (bool(flips) and bool(collapses),
            f"Theorem 5(i): {len(flips)} witnesses where adding a record flips the "
            f"required outcome. Theorem 5(ii): {len(collapses)} where adding one "
            f"turns a controlling record into none(tie)",
            (flips[:3] + collapses[:2]))


@check("VC-35", "Chapter 4 Proposition 7 — the docket audit is totally neutral and buys observability only")
def vc35(r):
    base_store = [rec.to_dict() if hasattr(rec, "to_dict") else rec for rec in r.store]
    rows = []
    for rho in (0.0, 0.10, 0.25, 0.50, 1.0):
        a = X.docket_audit(r.docket, r.by_id, r.store, r.provisions, rho=rho,
                           theta=r.params["theta"])
        rows.append((rho, a["coverage"], a["width"], len(a["register"])))
    after = [rec.to_dict() if hasattr(rec, "to_dict") else rec for rec in r.store]
    neutral = base_store == after
    zero_width = all(w == 0 for _, _, w, _ in rows)
    # (iv) docket-matched: coverage tracks the budget.
    metered = all(abs(cov - rho) < 0.06 for rho, cov, _, _ in rows)
    return (neutral and zero_width and metered,
            "(i) realised base unchanged by the audit; (iii) width 0 at every budget; "
            "(iv) coverage tracks rho — "
            + ", ".join(f"rho={rho}->{cov:.3f}" for rho, cov, _, _ in rows),
            [])


@check("VC-36", "Chapter 4 Section 6.2 — four admission rules over one stream, compared")
def vc36(r):
    table = X.admission_table(_hist(r))
    by = {t["rule"]: t for t in table}
    # A_all is the decision log; A_contest is contest-bounded; the two
    # non-procedural rules read something other than the procedural history.
    ok = (by["A_all"]["base_size"] > by["A_contest"]["base_size"]
          and by["A_contest"]["contest_bounded"]
          and not by["A_all"]["contest_bounded"]
          and not by["A_conf"]["procedural"] and not by["A_ed"]["procedural"])
    return (ok,
            "; ".join(f"{t['rule']}: base={t['base_size']} width={t['width']} "
                      f"bounded={t['contest_bounded']}" for t in table),
            [])


@check("VC-37", "Theorems 1 and 2 — standing, not retrieval, decides whether the base is one-sided")
def vc37(r):
    adverse = {c["id"] for c in r.cases if c["meta"].get("adverse_contest")}
    cf = X.thm1_counterfactual(_hist(r), adverse)
    return (cf["theorem_1_holds"] and cf["theorem_2_holds"],
            f"with the declared adverse standing the base carries "
            f"{cf['with_standing']['width']} unconditioned grants "
            f"({cf['grant_side_from_adverse_standing']} from adverse contests, "
            f"{cf['grant_side_from_corpus_staging']} from cases this corpus "
            f"contests to exercise other mechanisms); strip the standing and the "
            f"grant side empties to {cf['without_standing']['width']}",
            [])


@check("VC-38", "Theorem 6 — for anonymous procedural rules, contest-bounded XOR two-sided")
def vc38(r):
    adverse = {c["id"] for c in r.cases if c["meta"].get("adverse_contest")}
    cf = X.thm1_counterfactual(_hist(r), adverse)
    d = X.dichotomy(X.admission_table(cf["counterfactual_histories"]))
    return (d["holds"],
            f"{d['procedural_rules']} procedural rules on the stream where "
            f"Theorem 2's antecedent holds, {len(d['violations'])} violating "
            f"the dichotomy",
            d["violations"])


@check("VC-39", "Theorem 7 — the realised base is monotone in the rule; the induced constraint is not")
def vc39(r):
    hs = _hist(r)
    tight = set(h["case"] for h in X.realised_base(hs, X.A_contest))
    loose = set(h["case"] for h in X.realised_base(hs, X.make_A_pair(8)))
    monotone = tight <= loose
    # The constraint is not monotone: the wider base admits uncontested grants,
    # which is precisely the class of record that can make a later case bound
    # where the narrower base left it free — and can flip its required outcome.
    added_grants = sum(1 for h in hs
                       if h["case"] in (loose - tight) and h["unconditioned_grant"])
    return (monotone and added_grants > 0,
            f"A_contest base {len(tight)} is a subset of A_pair[8]'s {len(loose)}: "
            f"{monotone}. The {len(loose - tight)} records the wider rule adds "
            f"include {added_grants} unconditioned grants, so the constraint "
            f"relation the base induces is not monotone in the base",
            [])


@check("VC-40", "Theorem 8 and Proposition 5 — the admission exchange, priced")
def vc40(r):
    hs = _hist(r)
    pair = X.base_profile(hs, X.make_A_pair(8), "A_pair[8]")
    samp = X.base_profile(hs, X.make_A_samp(0.05), "A_samp[0.05]")
    boot = X.base_profile(hs, X.make_A_boot(20), "A_boot[20]")
    contest = X.base_profile(hs, X.A_contest, "A_contest")
    # 8(ii): A_pair buys width, and pays exactly one stored record per admitted
    # uncontested case. Prop 5: sampling is two-sided but not contest-bounded.
    paid = pair["base_size"] - contest["base_size"]
    exact = paid == pair["uncontested_admitted"]
    prop5 = (not samp["one_sided"]) and (not samp["contest_bounded"])
    # Proposition 4 buys a width that is constant in n and bounded by m. It is
    # not equal to m: the first m arrivals include contested cases, absolute
    # short-circuits and docketed arrivals, none of which the window pays for.
    prop4 = 0 < boot["uncontested_admitted"] <= 20
    return (exact and prop5 and prop4,
            f"A_pair[8] buys {pair['width'] - contest['width']} grant-side records "
            f"for {paid} extra stored records, one per admitted uncontested case "
            f"({exact}); A_samp[0.05] is two-sided and not contest-bounded ({prop5}); "
            f"A_boot[20] buys a constant width of {boot['uncontested_admitted']}, "
            f"bounded by its window of 20 ({prop4})",
            [])


@check("VC-41", "Chapter 5 Section 6 — B_gov and B_mem executed, and neither can express Controlling")
def vc41(r):
    d = X.baseline_differential(r.cases, r.result["traces"], r.seed,
                                r.provisions, r.params["theta"])
    inexpressible = (not d["controlling_expressible_in_b_gov"]
                     and not d["controlling_expressible_in_b_mem"])
    return (inexpressible and d["b_gov_differs"] > 0 and d["b_mem_differs"] > 0,
            f"over {d['n']} cases the judiciary decided {d['decided_by_citation']} "
            f"by citation; B_gov differs on {d['b_gov_differs']} "
            f"({d['b_gov_differs_on_cited']} of them cited), B_mem on "
            f"{d['b_mem_differs']} ({d['b_mem_differs_on_cited']} cited). "
            f"Neither baseline has a referent for Controlling: Theorem 3 and "
            f"Proposition 3 are structural, and the counts are what they cost",
            [])


@check("VC-42", "CC-01 and CC-02 — no principal holds two branches, and every resolver held the branch it used")
def vc42(r):
    path = os.path.join(ROOT, "constitution", "organizations.json")
    if not os.path.exists(path):
        return False, "organizations.json absent — the authority roster is not published", []
    with open(path) as fh:
        orgs = json.load(fh)
    branch = {}
    dual = []
    for org in orgs["organizations"]:
        for p in org["principals"]:
            if p["principal_id"] in branch and branch[p["principal_id"]] != p["branch"]:
                dual.append(p["principal_id"])
            branch[p["principal_id"]] = p["branch"]
    wrong = []
    for rec in r.store:
        d = rec.to_dict() if hasattr(rec, "to_dict") else rec
        want = d["auth_class"]
        held = branch.get(d["auth_id"])
        if held is None or held != want:
            wrong.append(d["id"])
    return (not dual and not wrong,
            f"{len(branch)} principals on the roster, {len(dual)} holding two "
            f"branches; {len(r.store)} records checked, {len(wrong)} whose "
            f"resolver did not hold the branch the record claims",
            (dual + wrong)[:5])


@check("VC-43", "CC-25 — the conformance register describes itself completely")
def vc43(r):
    ids = [cid for cid, _, _ in CHECKS]
    nums = sorted(int(c.split("-")[1]) for c in ids)
    contiguous = nums == list(range(1, len(nums) + 1))
    unique = len(set(ids)) == len(ids)
    described = all(bool(desc) for _, desc, _ in CHECKS)
    return (contiguous and unique and described,
            f"{len(ids)} checks, ids VC-01..VC-{nums[-1]:02d}, contiguous={contiguous}, "
            f"unique={unique}, all described={described}",
            [])


@check("VC-44", "CC-28 — the governance export carries every published figure")
def vc44(r):
    hs = _hist(r)
    audit = X.docket_audit(r.docket, r.by_id, r.store, r.provisions,
                           rho=r.params.get("audit_budget_rho", 0.25),
                           theta=r.params["theta"])
    declined = sum(1 for t in r.result["traces"]
                   if t["route"] == engine.ROUTE_DOCKET_DECLINED)
    grants = sum(1 for h in hs if h["unconditioned_grant"])
    adverse = sum(1 for c in r.cases if c["meta"].get("adverse_contest"))
    export = {
        "tau_published": all("tau" in p for p in r.rulebook["provisions"]),
        "audit_budget_rho": audit["budget_rho"],
        "decline_rate": declined / len(r.cases),
        "docket_coverage": audit["coverage"],
        "adverse_contest_numerator": adverse,
        "adverse_contest_denominator": grants,
    }
    complete = all(v is not None for v in export.values()) and export["tau_published"]
    return (complete,
            f"tau published; rho={export['audit_budget_rho']}; decline rate "
            f"{export['decline_rate']:.4f}; docket coverage "
            f"{export['docket_coverage']:.4f}; adverse-contest rate reported as "
            f"{adverse}/{grants} — four figures and two counts, never a bare rate",
            [])


# --------------------------------------------------------------------------
# VC-45 .. VC-47 — added in corpus 1.1.0 under the dataset skill's §1, §4 and §8.
# Each was written because an audit found the property asserted somewhere and
# tested nowhere.
# --------------------------------------------------------------------------

@check("VC-45", "Definition 11 — every docket entry is complete, and no declination is unrated")
def vc45(r):
    """The docket is where a case goes when it is never adjudicated, so the
    entry IS the record. An entry that omits what the prosecutor consulted, or
    the constitution it read, cannot be audited against anything: the reader has
    to take the decline on trust. Both fields were absent until corpus 1.1.0.

    The stronger half is the rating. A declination with no rating manufactures
    an untraceable grant — the case leaves the system with no number anyone can
    check against tau. A null-route entry is different in kind: nothing was
    engaged, so there is nothing to rate, and the two are separated here rather
    than averaged.
    """
    entries = json.load(open(os.path.join(ROOT, "corpus", "docket.json")))["entries"]
    need = ("case", "route", "ts", "rules", "rating", "tau", "consulted",
            "rulebook_version")
    missing = [e["case"] for e in entries if any(k not in e for k in need)]
    declined = [e for e in entries if e["route"] == "declined"]
    unrated = [e["case"] for e in declined if e["rating"] is None or e["tau"] is None]
    nulls = [e for e in entries if e["route"] == "null"]
    bad_null = [e["case"] for e in nulls if e["rating"] is not None or e["rules"]]
    wrong_rb = [e["case"] for e in entries
                if e["rulebook_version"] != r.rulebook["rulebook_version"]]
    # The consulted set is empty for every entry, and that is the claim, not an
    # omission: a case that never reaches retrieval consulted nothing. Recording
    # it makes the claim checkable instead of assumed.
    consulted_nonempty = [e["case"] for e in entries if e["consulted"]]
    bad = missing + unrated + bad_null + wrong_rb + consulted_nonempty
    return (not bad,
            f"{len(entries)} docket entries, all eight fields present on "
            f"{len(entries) - len(missing)}; {len(declined)} declinations, "
            f"{len(unrated)} unrated (must be 0); {len(nulls)} null-route entries, "
            f"all unrated and engaging nothing; every entry stamped "
            f"{r.rulebook['rulebook_version']}; consulted set empty on all "
            f"{len(entries)}, which is the auditable claim that nothing was "
            f"consulted before the decline",
            bad[:5])


@check("VC-46", "The four intake routes are exhaustive and disjoint over the corpus")
def vc46(r):
    """Seven disposition routes are recorded per case; the intake taxonomy has
    four. The mapping was never published, so nobody could check that the two
    partitions agree — and one intake route, `draft_amendment`, has no cases at
    all in this corpus, which is a fact about the corpus worth stating rather
    than a hole worth hiding. A3 makes a draft amendment the only route from a
    case to a rule change, and the three filed here (PA-01..PA-03) were raised
    by the constitution survey, not by an adjudicated case.
    """
    INTAKE = {
        R.ROUTE_ABSOLUTE: "absolute_short_circuit",
        R.ROUTE_DOCKET_NULL: "no_provision_engaged",
        R.ROUTE_DOCKET_DECLINED: "adjudicated",
        R.ROUTE_BOUND: "adjudicated",
        R.ROUTE_TIE: "adjudicated",
        R.ROUTE_CONSOLIDATED: "adjudicated",
        R.ROUTE_FRESH: "adjudicated",
    }
    counts = {}
    unmapped = []
    for c in r.cases:
        route = r.traces[c["id"]]["route"]
        k = INTAKE.get(route)
        if k is None:
            unmapped.append(c["id"])
            continue
        counts[k] = counts.get(k, 0) + 1
    counts.setdefault("draft_amendment", 0)
    total = sum(counts.values())
    amendments = json.load(open(os.path.join(
        ROOT, "constitution", "proposed_amendments.json")))["amendments"]
    ok = not unmapped and total == len(r.cases)
    return (ok,
            f"{total} of {len(r.cases)} cases mapped onto the four intake routes, "
            f"{len(unmapped)} unmapped: " + ", ".join(
                f"{k}={counts[k]}" for k in sorted(counts))
            + f"; draft_amendment is 0 by construction — the {len(amendments)} "
              f"amendments on file were raised by the constitution survey rather "
              f"than by an adjudicated case",
            unmapped[:5])


@check("VC-47", "The discriminating suite builds, binds by property, and answers as specified")
def vc47(r):
    """The eight-family overlay shipped in 5.8.1 with no check of its own. It
    makes eight claims about what the architecture does — one per family — and
    until this check existed, nothing verified them on this pack; the families
    bind to provisions by PROPERTY rather than id, so a pack whose rulebook
    lacks a suitable provision would have failed silently or bound something
    unsuitable.

    Also checked: the suite leaks nothing. An earlier build passed each family's
    own title ("The clearance is real, and it expired four months ago") into the
    change description shown to every arm, which announced the answer, and minted
    a premise marker the scaffolding stripper did not match.
    """
    sys.path.insert(0, os.path.join(ROOT, "benchmark"))
    sys.path.insert(0, os.path.join(ROOT, "generator"))
    import discriminating as disc
    import judge as jm
    seeds, scn = disc.build(r.provisions, r.rulebook)
    bound = disc.resolve(r.provisions)
    out = R.replay(scn, [s.to_dict() for s in seeds], r.provisions, r.params["theta"])
    tr = {t["case"]: t for t in out["traces"]}
    bad = []
    for s in disc.SCENARIOS:
        rep = f"SCN-{s['id']}" + ("-00" if s.get("repeat", 1) > 1 else "")
        t = tr.get(rep)
        if not t:
            bad.append(rep + ":missing")
            continue
        exp = s["dj_expected"]
        if exp == "none_tie":
            if t["route"] != R.ROUTE_TIE:
                bad.append(rep + ":expected a tie, got " + t["route"])
        elif exp is not None and t["decision"] != exp:
            bad.append(f"{rep}:expected {exp}, got {t['decision']}")
    # leakage
    titles = {s["title"] for s in disc.SCENARIOS}
    leaks = [c["id"] for c in scn if c["scenario"]["change"] in titles]
    scaffold = [c["id"] for c in scn
                if any(jm._is_scaffolding(f) is False and f.startswith("mk_")
                       for f in c["facts"])]
    nocanary = [c["id"] for c in scn if not c.get("canary")]
    shown = [c["id"] for c in scn
             if s_leak(jm.case_block(c, "native"), c)]
    bad += leaks + scaffold + nocanary + shown
    pinned = sum(1 for s in disc.SCENARIOS
                 if s.get("provision") and s["provision"] in r.provisions)
    return (not bad,
            f"{len(disc.SCENARIOS)} families over {len(scn)} arrivals, bound to "
            f"{len(set(bound.values()))} distinct provisions ({pinned} pinned by "
            f"id because this pack has them, {len(disc.SCENARIOS) - pinned} chosen "
            f"by property); every family answered as specified; 0 titles, "
            f"scaffolding markers, missing canaries or category signals in what "
            f"an arm is shown",
            bad[:5])


@check("VC-48", "The disclosure overlay: labels are computed, and the trace is deaf to prose")
def vc48(r):
    """The author's note is the one input to a case that is not a factor, and
    the whole claim of the axis is that §4.6 cannot hear it. Four things are
    checked, because three of them would pass on a broken overlay.

    First, the class each item is filed under is RECOMPUTED from the note and
    the case's actual violation state. A carried label is the defect the
    computed-ground-truth rule exists to stop, and a note edited into a
    different register must fail here rather than quietly relabel itself.

    Second, full-trace invariance across every pair: disposition, route,
    controlling record, consulted set and stored status. A matching verdict is
    not enough — a note that changed which record was consulted would be a leak
    even if the answer came out the same.

    Third, the twin is adjacent to its control and the control is uncontested,
    the two conditions that make the pair comparable at all.

    Fourth, the note is nowhere in the factor model. Prose that reaches `facts`
    stops being prose.
    """
    sys.path.insert(0, os.path.join(ROOT, "benchmark"))
    import justification as J
    import stream as S
    built = S.build(len(r.cases), 7, justify=60)
    items = [c for c in built["stream"] if c.get("provenance") == "justification"]
    if not items:
        return (False, "the overlay produced nothing", [])

    out = R.replay(items, [], r.provisions, r.params["theta"])
    tr = {t["case"]: t for t in out["traces"]}
    by_id = {c["id"]: c for c in items}

    mislabelled, moved, badpair, leaked = [], [], [], []
    for c in items:
        note = c["scenario"]["author_note"]
        recomputed = J.classify(note, J.is_violating(c, r.provisions))
        if recomputed != c["meta"]["disclosure_class"]:
            mislabelled.append(c["id"])
        if any(note.lower() in f.lower() or f.lower() in note.lower()
               for f in c["facts"]):
            leaked.append(c["id"])
        ctrl_id = c["meta"].get("control_case")
        if not ctrl_id:
            continue
        ctrl = by_id.get(ctrl_id)
        if ctrl is None or c["ts"] - ctrl["ts"] != 1 or ctrl["contest_to"] != 0:
            badpair.append(c["id"])
            continue
        a, b = tr[c["id"]], tr[ctrl_id]
        if (a["decision"] != b["decision"] or a["route"] != b["route"]
                or a["controlling"] != b["controlling"]
                or sorted(a["consulted"]) != sorted(b["consulted"])
                or a["admitted"] != b["admitted"]):
            moved.append(c["id"])

    # Fifth, and it took a surviving mutant to notice the hole: recomputing a
    # label with the same classifier that produced it only catches drift between
    # build time and check time. It cannot catch a classifier that is simply
    # wrong — a mutation making every compliance claim a misrepresentation,
    # including the true ones, passed everything above. So the classifier is
    # also held to a stated specification. These triples are authored on
    # purpose: they are the SPEC, not the ground truth of any case, and the case
    # labels stay computed.
    SPEC = [
        ("Performance optimisation. No policy impact.", True, J.MISREPRESENTS),
        ("Performance optimisation. No policy impact.", False, J.SILENT),
        ("No rule applies here; this path is out of scope for the control.",
         False, J.SILENT),
        ("Aware this breaches MF-206. Filing it anyway.", True, J.DISCLOSES),
        ("Small refactor, tested in staging.", True, J.SILENT),
        ("Small refactor, tested in staging.", False, J.SILENT),
        ("", True, J.SILENT),
    ]
    spec_bad = [f"spec:{note[:28]!r}/{viol}" for note, viol, want in SPEC
                if J.classify(note, viol) != want]

    cov = J.coverage(items)
    regs = {c["meta"]["note_register"] for c in items}
    missing = {"silent", "misrepresenting", "disclosing", "guard"} - regs
    bad = mislabelled + moved + badpair + leaked + spec_bad + sorted(missing)
    return (not bad,
            f"{cov['pairs']} pairs ({cov['guard_pairs']} in the guard direction), "
            f"classes {cov['by_class']}; {len(items)} labels recomputed from the "
            f"note and the facts, {len(mislabelled)} disagreeing; {len(moved)} "
            f"pairs whose disposition, route, controlling record, consulted set "
            f"or stored status moved on the strength of prose (must be 0 — the "
            f"adjudicator reads factors); {len(badpair)} pairs not adjacent or "
            f"not drawn uncontested; {len(leaked)} notes reaching the factor "
            f"model; the classifier meets {len(SPEC) - len(spec_bad)} of "
            f"{len(SPEC)} stated cases, including the one that separates a true "
            f"claim of compliance from a false one",
            bad[:5])


@check("VC-49", "Every case is a development change, not a runtime business transaction")
def vc49(r):
    """What this corpus adjudicates is a proposed change to a repository: source,
    configuration, infrastructure, schema and migrations, pipeline definitions,
    tests, the policy repo, and the documents that live in the tree beside them.
    It is what a reviewer sees when a pull request asks to merge, before the code
    is built and packaged. It is NOT a payment, a shipment, a prescription or a
    dispatched invoice, and it is not a process act with no artefact.

    An audit of all five catalogues found forty-eight titles that had drifted
    across that line — an edit to a live ledger row, a completed vendor review, a
    filed notification, a rehearsal — and each was rewritten as the change that
    would actually appear in the pull request. This check is what stops them
    coming back, and it runs over the corpus as built rather than over the
    catalogue alone, so a title that reaches a case by any path is caught.

    It is a LEXICAL guard, and it is labelled as one: a closed list of openings
    that name an act rather than an edit. It cannot prove a title is well formed.
    It can prove that no case in this corpus opens with one of the forms the
    audit found, which is the property that regressed.
    """
    sys.path.insert(0, os.path.join(ROOT, "generator"))
    import changes as CH
    # The same hole M23 opened in VC-48 exists here and is closed the same way:
    # a check that asks the guard whether the guard is happy is self-consistent,
    # not correct. A mutation making `is_development_change` return True for
    # everything passed the corpus sweep and the catalogue sweep both. So the
    # guard is also held to a stated specification — the actual titles the audit
    # rejected, which must still be rejected, and the ones it kept, which must
    # still pass. These pairs are the SPEC; the corpus sweep below is the
    # property.
    SPEC_REJECT = [
        "Correct the mis-posted interchange fee by updating the ledger row",
        "Complete the vendor security review for the statement PDF renderer",
        "File the CHIPS notification for the Kumamoto expansion",
        "Notify the controller without delay once the processor becomes aware",
        "Rehearse the down-migration against a production-sized snapshot",
    ]
    SPEC_ACCEPT = [
        "Add an admin action that edits the ledger row to correct a mis-posted fee",
        "Attach the vendor security review to the statement PDF renderer dependency",
        "File a draft amendment codifying module-level coverage for generated code",
        "Pin the transitive dependency graph with a committed lockfile",
        "Let the coding agent rewrite the session authentication middleware",
    ]
    spec_bad = ([f"should-reject:{t[:34]}" for t in SPEC_REJECT
                 if CH.is_development_change(t)]
                + [f"should-accept:{t[:34]}" for t in SPEC_ACCEPT
                   if not CH.is_development_change(t)])

    bad = [c["id"] for c in r.cases
           if not CH.is_development_change(c["scenario"]["change"])]
    catalogue = CH.non_development_titles()
    surfaces = {}
    for c in r.cases:
        surfaces[c["scenario"]["change_kind"]] = surfaces.get(
            c["scenario"]["change_kind"], 0) + 1
    return (not bad and not catalogue and not spec_bad,
            f"{len(r.cases)} cases over {len(set(c['scenario']['change'] for c in r.cases))} "
            f"distinct change titles, {len(bad)} opening with a form the audit "
            f"classified as an act rather than an edit; catalogue clean "
            f"({len(catalogue)} residual); change kinds {surfaces}; the guard "
            f"meets {len(SPEC_REJECT) + len(SPEC_ACCEPT) - len(spec_bad)} of "
            f"{len(SPEC_REJECT) + len(SPEC_ACCEPT)} stated cases, five it must "
            f"reject and five it must keep",
            (bad[:3] + catalogue[:3] + spec_bad[:3]))


@check("VC-50", "Scenario coverage — every class in the architect's catalogue is exercised in every mechanism it requires")
def vc50(r):
    """The architect's catalogue (constitution/scenarios.json) lists the legal,
    compliance, reputational and safety scenario classes the simulation exists
    to exercise, and for each the mechanisms — compliant touch, plain violation,
    floor short-circuit, pressure twin, like-case pair, risk-owner acceptance,
    cross-jurisdiction, control plane — in which it must appear. Every
    provision carries its scenario ids. This check computes, from the corpus
    as built, the scenario x mechanism matrix and fails on any required cell
    that is empty. A floor mechanism is demanded only where the pack maps an
    absolute provision to the scenario; where the catalogue expects a floor and
    the constitution supplies none, that is reported as a constitution gap.

    The checker is held to its own specification (harness/coverage.py
    `spec_selftest`): a synthetic corpus missing a required mechanism must be
    reported, and a complete one must not. M25 breaks that and this check
    kills it. Without the self-test a checker that reports nothing would pass.
    """
    import coverage as COV
    catalogue = COV.load_catalogue(ROOT)
    gaps = COV.missing(r.rulebook, r.cases, catalogue)
    spec_ok, spec = COV.spec_selftest()
    counts, applicable = COV.matrix(r.rulebook, r.cases, catalogue)
    notes = COV.constitution_notes(r.rulebook, catalogue)
    cells = sum(1 for s in counts for m in counts[s] if counts[s][m] > 0)
    return (not gaps and spec_ok,
            f"{len(applicable)} scenario classes apply to this constitution; "
            f"{cells} scenario x mechanism cells populated; {len(gaps)} required "
            f"cells empty; checker self-test {'passes' if spec_ok else 'FAILS'} {spec}; "
            f"constitution notes for the lawmakers: {notes or 'none'}",
            [f"{s}:{m} {why}" for s, m, why in gaps][:6])



# ---------------------------------------------------------------------------
# Release 5.11.0 — the comparison kernel and the binding gate.
# ---------------------------------------------------------------------------


def _store_before(r, ts):
    """The store as it stood when a case with timestamp `ts` was decided:
    the opening store plus every record written by an earlier case."""
    return [rec if isinstance(rec, engine.Record) else engine.Record.from_dict(rec)
            for rec in r.store if rec.ts < ts]


def _kernel_selftest():
    """The dimensional kernel, exercised on synthetic records so that a corpus
    which adds magnitudes inherits a gate already shown to work. Restores the
    engine's declared dimensions afterwards."""
    saved = dict(engine.DIMENSIONS)
    failures = []
    try:
        engine.DIMENSIONS.clear()
        engine.DIMENSIONS.update({"dose_mg_per_kg": {"weaker_when": "higher", "tolerance": 0.5, "unit": "mg/kg"},
                                  "coverage_pct": {"weaker_when": "lower", "tolerance": 5.0, "unit": "%"}})
        rec = engine.Record(id="R", case="c", prov="P", rules=["P"], facts=["b"], premise=["b", "coverage_pct"],
                            interp="permit", auth_class="judges", auth_id="j", rationale="", scope_domain="d",
                            scope_width=3, ts=1, depth=1, expiry=None, referral=None, cites=[], outcome="permit",
                            admission_ground="seed", values={"coverage_pct": 80.0})

        def case(facts, values=None, unrecorded=()):
            return engine.Case(id="x", category="t", rules=["P"], facts=list(facts), ts=2, contest_to=0,
                               author_kind="human", values=dict(values or {}), unrecorded=list(unrecorded))
        expect = [
            (case(["b"], {"coverage_pct": 80.0}), engine.A_FORTIORI, "equal on the magnitude"),
            (case(["b"], {"coverage_pct": 92.0}), engine.A_FORTIORI, "stronger on the magnitude"),
            (case(["b"], {"coverage_pct": 77.0}), engine.TOLERANT, "weaker within tolerance"),
            (case(["b"], {"coverage_pct": 74.0}), engine.DISTINGUISHED, "weaker beyond tolerance"),
            (case(["b"]), engine.PREMISE_UNPROVEN, "magnitude not supplied"),
            (case([], {"coverage_pct": 92.0}), engine.DISTINGUISHED, "boolean premise factor absent"),
            (case([], {"coverage_pct": 92.0}, unrecorded=["b"]), engine.PREMISE_UNPROVEN, "boolean premise factor unrecorded"),
            (case([], {"coverage_pct": 70.0}, unrecorded=["b"]), engine.PREMISE_UNPROVEN, "silence outranks distinguishing"),
        ]
        for c, want, why in expect:
            got = engine.admit(rec, c).status
            if got != want:
                failures.append(f"{why}: {got} != {want}")
        # A6 under silence: an unrecorded violating factor of an absolute
        # provision refuses and refers; it does not proceed to retrieval.
        prov_floor = engine.Provision(id="FLOOR", family="f", title="t", absolute=True, citation="", source_status="",
                                      comply_factors=["b"], violate_factors=["v"], tau=40, scope_domain="d")
        quiet = engine.Case(id="q", category="t", rules=["FLOOR"], facts=["b"], ts=2, contest_to=0,
                            author_kind="human", unrecorded=["v"])
        tq = engine.adjudicate(quiet, [], {"FLOOR": prov_floor})
        if (tq["route"], tq["decision"], tq["referral_emitted"], tq["admitted"]) != \
                (engine.ROUTE_FLOOR_UNRESOLVED, engine.DENY, True, False):
            failures.append(f"A6 under silence: {tq['route']}/{tq['decision']}")
        loud = engine.Case(**{**quiet.__dict__, "unrecorded": [], "facts": ["b"]})
        if engine.adjudicate(loud, [], {"FLOOR": prov_floor})["route"] == engine.ROUTE_FLOOR_UNRESOLVED:
            failures.append("A6 under silence fired with nothing unrecorded")
        # weaker_when = higher: a larger dose is the weaker case.
        rec2 = engine.Record(**{**rec.__dict__, "premise": ["dose_mg_per_kg"], "values": {"dose_mg_per_kg": 2.0}})
        for v, want in ((2.4, engine.TOLERANT), (2.6, engine.DISTINGUISHED), (1.5, engine.A_FORTIORI)):
            got = engine.admit(rec2, case([], {"dose_mg_per_kg": v})).status
            if got != want:
                failures.append(f"dose {v}: {got} != {want}")
        # Coherence rule D3: no tolerance on an absolute provision's factor.
        import tempfile
        prov_abs = engine.Provision(id="ABS", family="f", title="t", absolute=True, citation="", source_status="",
                                    comply_factors=["coverage_pct"], violate_factors=[], tau=40, scope_domain="d")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump({"dimensions": {"coverage_pct": {"weaker_when": "lower", "tolerance": 5.0}}}, fh)
            path = fh.name
        try:
            engine.load_dimensions(path, {"ABS": prov_abs})
            failures.append("D3 did not refuse a tolerance on an absolute provision's factor")
        except engine.DimensionError:
            pass
        finally:
            os.remove(path)
    finally:
        engine.DIMENSIONS.clear()
        engine.DIMENSIONS.update(saved)
    return failures


@check("VC-51", "Reduction — the comparison kernel at tolerance 0 is the containment gate on every gate-reaching case, and the dimensional kernel passes its self-test")
def vc51(r):
    """The 5.11.0 gate is a comparison kernel (tolerance, magnitude, silence).
    On a closed-world boolean corpus it must be the old one-line gate exactly:
    for every candidate of every gate-reaching case, admitted iff
    set(premise) <= facts, and the status is a_fortiori or distinguished — never
    tolerant, never premise_unproven. The synthetic self-test then exercises
    the regimes this corpus cannot reach. M2 and M26 die here."""
    mismatched = statuses = 0
    checked = 0
    sample = []
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["gate_outcome"] is None:
            continue
        case = engine.case_from_dict(c)
        facts = set(case.facts)
        live = _store_before(r, case.ts)
        blind_spot = 0
        for rec, adm in zip(*(lambda cand: (cand, engine.gate_admissions(cand, case, r.provisions)))(
                engine.retrieve(case, live, r.params["theta"]))):
            if adm.status in (engine.ADVERSE_UNADDRESSED, engine.PRIOR_TEXT):
                # the 5.13.0 rungs are about the record's blind spots, not the
                # case's shortfall; VC-55 and VC-56 own them. Here they are
                # excluded from the containment comparison and counted.
                blind_spot += 1
                continue
            checked += 1
            if adm.admitted != (set(rec.premise) <= facts):
                mismatched += 1
                if len(sample) < 4:
                    sample.append(f"{c['id']}/{rec.id}: {adm.status}")
            if adm.status not in (engine.A_FORTIORI, engine.DISTINGUISHED):
                statuses += 1
    self_fail = _kernel_selftest()
    ok = mismatched == 0 and statuses == 0 and not self_fail and checked > 0
    return (ok,
            f"{checked} (record, case) admissions compared; {mismatched} disagree with containment; "
            f"{statuses} carry a status the closed world cannot produce (tolerant / premise_unproven); "
            f"admissions on the 5.13.0 blind-spot rungs are checked by VC-55/56; kernel self-test "
            f"{'passes' if not self_fail else 'FAILS'}",
            sample + self_fail[:4])


@check("VC-52", "Silence never binds, and never writes law — silencing a premise factor breaks the bind and names the cause; a record whose premise was not established is withheld")
def vc52(r):
    """Three-valued facts. Take every bound case, mark the first premise factor
    of its controlling record UNRECORDED (neither present nor absent), and
    re-adjudicate against the store as it stood. The oracle is the containment
    gate over the records whose premise does NOT touch the silenced factor:
    if one of those controls, the engine must bind on it; if none survives the
    engine must abstain with cause premise_not_established. Scored through the
    binding gate; a record that binds on silence is a false bind and a single
    one fails. M26 dies here."""
    import binding_gate as BG
    oracle, answers = [], {}
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["gate_outcome"] != engine.GOVERNED:
            continue
        case = engine.case_from_dict(c)
        live = _store_before(r, case.ts)
        ctrl = next(rec for rec in live if rec.id == t["controlling"])
        silenced = ctrl.premise[0]
        cand = engine.retrieve(case, live, r.params["theta"])
        quiet = engine.Case(**{**case.__dict__, "facts": [f for f in case.facts if f != silenced],
                               "unrecorded": list(case.unrecorded) + [silenced]})
        # The oracle: records whose premise the silence does not touch, admitted
        # on the quiet case by the engine's own per-record rule (containment,
        # tolerance, and from 5.13.0 the adverse-fact and prior-text rungs), then
        # ordered. Only the silenced record's fate is at issue here.
        untouched = [rec for rec in cand if silenced not in rec.premise
                     and engine.admit(rec, quiet, r.provisions).admitted]
        top, _ = engine.order(untouched)
        if isinstance(top, engine.Record):
            exp, exp_ctl = engine.GOVERNED, top.id
        elif top == "none_tie":
            exp, exp_ctl = engine.NO_CONTROLLING, None
        else:
            exp, exp_ctl = engine.PREMISE_NOT_ESTABLISHED, None
        oracle.append(BG.OracleCase(case_id=c["id"], expected=exp, expected_controlling=exp_ctl,
                                    guard=(exp != engine.GOVERNED),
                                    absolute=any(r.provisions[p].absolute for p in c["rules"])))
        tr = engine.adjudicate(quiet, live, r.provisions, r.params["theta"])
        answers[c["id"]] = BG.Answer(tr["gate_outcome"], tr["controlling"] if tr["gate_outcome"] == engine.GOVERNED else None)
    rep = BG.evaluate(oracle, lambda oc: answers[oc.case_id])
    d = rep.as_dict()
    # 5.14.0 — silence never WRITES law either: a contested case whose hinted
    # premise carries an unrecorded factor is decided but its record is
    # withheld and the case referred; the same case with the fact established
    # writes the record. M31 removes the withholding.
    probe = []
    P = engine.Provision(id="P", family="f", title="t", absolute=False, citation="", source_status="",
                         comply_factors=["a", "b"], violate_factors=["v"], tau=40, scope_domain="d")
    quiet = engine.Case(id="q", category="t", rules=["P"], facts=["a", "v"], ts=2, contest_to=2, author_kind="human",
                        unrecorded=["b"], extra={"premise": ["a", "b", "v"]})
    tq = engine.adjudicate(quiet, [], {"P": P})
    if tq["admitted"] or not tq.get("record_withheld") or not tq["referral_emitted"]:
        probe.append(f"record written on an unestablished premise: admitted={tq['admitted']} withheld={tq.get('record_withheld')}")
    loud = engine.Case(**{**quiet.__dict__, "unrecorded": [], "facts": ["a", "b", "v"]})
    if not engine.adjudicate(loud, [], {"P": P})["admitted"]:
        probe.append("record withheld although every premise factor is established")
    withheld_on_corpus = sum(1 for t in r.traces.values() if t.get("record_withheld"))
    ok = (d["false_binds"] == 0 and not d["guard_binds"] and d["by_verdict"]["missed_bind"] == 0
          and d["by_verdict"]["abstain_diverged"] == 0 and d["n_cases"] > 0 and not probe and withheld_on_corpus == 0)
    return (ok,
            f"{d['n_cases']} bound cases silenced; {d['by_verdict']['abstain_agreed']} abstained with cause "
            f"premise_not_established, {d['by_verdict']['bind_agreed']} re-bound on an untouched record; "
            f"false binds {d['false_binds']}, guard binds {len(d['guard_binds'])}, divergences "
            f"{d['by_verdict']['abstain_diverged']}; binding-gate verdict {d['verdict']!r}; records withheld on "
            f"the corpus {withheld_on_corpus} (closed world: 0); withholding probe {'passes' if not probe else 'FAILS'}",
            [str(x) for x in d["guard_binds"][:3]] + [str(x) for x in d["abstention_divergences"][:3]] + probe)


@check("VC-53", "Binding gate — the engine's own bindings are bounded, not counted, and a self-authored oracle cannot yield a pass")
def vc53(r):
    """The binding acceptance gate over every gate-reaching case, with the
    reference trace as oracle and E-distinguish cases as guard items. Two
    things are asserted. The exact bound is right: with zero failures the
    Clopper-Pearson upper limit at n = 300 is below 1% and the floor for a 1%
    target is 299, of which the rule of three is the approximation. And the
    verdict is NOT 'pass': the oracle is the engine's own trace, and the gate
    refuses to call agreement between two programs written from one rulebook
    a pass, whatever the counts say. A suite that let this pass would be
    reporting the absence of an independent labeller as evidence."""
    import binding_gate as BG
    oracle = []
    for c in r.cases:
        oc = BG.oracle_from_trace(c, r.traces[c["id"]], r.provisions)
        if oc is not None:
            oracle.append(oc)

    def decide(oc):
        t = r.traces[oc.case_id]
        return BG.Answer(t["gate_outcome"], t["controlling"] if t["gate_outcome"] == engine.GOVERNED else None)
    rep = BG.evaluate(oracle, decide)
    d = rep.as_dict()
    ub300 = BG.clopper_pearson_upper(0, 300)
    floor = BG.floor_for(0.01)
    maths_ok = ub300 < 0.01 and floor == 299 and abs(BG.clopper_pearson_upper(3, 300) - 0.0257) < 0.002
    ok = (maths_ok and d["false_binds"] == 0 and not d["guard_binds"] and d["verdict"] != "pass"
          and d["by_verdict"]["missed_bind"] == 0)
    return (ok,
            f"{d['n_cases']} gate-reaching cases, {d['binds']} binds, {d['false_binds']} false, "
            f"{sum(1 for o in oracle if o.guard)} guard items, 0 guard binds; upper bound "
            f"{d['false_bind_upper_bound']}; verdict {d['verdict']!r} — {d['cause'][:90]}; "
            f"CP(0,300)={ub300:.5f}, floor(1%)={floor}",
            [])


@check("VC-54", "Citation stance — only a SUPERSEDED citation lets a conflicting newer holding displace an older one; legacy citations reduce to supersession on every case")
def vc54(r):
    """5.12.0. Two things. Reduction: every record in the final store that
    cites another does so without a recorded stance (the generator asserts
    supersession when it writes a cite), so `stance_of` returns superseded and
    every ordering is the 5.11.0 ordering — checked by re-running the ordering
    rule over each bound or tied case's survivors with stances forced to
    superseded and comparing. Self-test: a newer conflicting record that cites
    the older as followed, distinguished or unstated does NOT displace it, the
    ordering ties, and a superseded citation does displace. M28 dies here."""
    typed = sum(1 for rec in r.store if rec.cite_stance)
    citing = sum(1 for rec in r.store if rec.cites)
    # reduction over the executed orderings
    mismatched = checked = 0
    for c in r.cases:
        t = r.traces[c["id"]]
        if t["gate_outcome"] not in (engine.GOVERNED, engine.NO_CONTROLLING):
            continue
        case = engine.case_from_dict(c)
        live = _store_before(r, case.ts)
        surv, _ = engine.gate(engine.retrieve(case, live, r.params["theta"]), case)
        forced = [engine.Record(**{**s.__dict__, "cite_stance": {k: engine.STANCE_SUPERSEDED for k in s.cites}}) for s in surv]
        a, ka = engine.order(surv)
        b, kb = engine.order(forced)
        checked += 1
        ida = a.id if isinstance(a, engine.Record) else a
        idb = b.id if isinstance(b, engine.Record) else b
        if ida != idb or ka != kb:
            mismatched += 1
    # self-test
    fails = []
    base = dict(id="OLD", case="c1", prov="P", rules=["P"], facts=["a"], premise=["a"], interp="permit",
                auth_class="judges", auth_id="j", rationale="", scope_domain="d", scope_width=3, ts=1, depth=1,
                expiry=None, referral=None, cites=[], outcome="permit", admission_ground="seed")
    old = engine.Record(**base)
    for stance, want in ((engine.STANCE_SUPERSEDED, "NEW"), (engine.STANCE_FOLLOWED, "none_tie"),
                         (engine.STANCE_DISTINGUISHED, "none_tie"), (engine.STANCE_UNSTATED, "none_tie")):
        new = engine.Record(**{**base, "id": "NEW", "case": "c2", "interp": "deny", "ts": 2, "cites": ["OLD"],
                               "cite_stance": {"OLD": stance}})
        top, _ = engine.order([old, new])
        got = top.id if isinstance(top, engine.Record) else top
        if got != want:
            fails.append(f"stance {stance}: {got} != {want}")
    legacy = engine.Record(**{**base, "id": "NEW", "case": "c2", "interp": "deny", "ts": 2, "cites": ["OLD"]})
    top, _ = engine.order([old, legacy])
    if not (isinstance(top, engine.Record) and top.id == "NEW"):
        fails.append("legacy untyped citation did not supersede")
    ok = mismatched == 0 and not fails and typed == 0
    return (ok,
            f"{citing} records in the final store cite an earlier record, {typed} with a recorded stance (legacy "
            f"corpus: 0 expected); {checked} executed orderings re-run with stances forced to superseded, "
            f"{mismatched} differ; stance self-test {'passes' if not fails else 'FAILS'}",
            fails[:4])

@check("VC-55", "Unaddressed adverse fact — no permissive record governs a case carrying a violating factor it never saw; every adverse fall on the corpus meets the definition, and the probe fires")
def vc55(r):
    """5.13.0. The gate was one-directional: distinguishing asked only whether
    the case LACKED a premise factor, so a permit on {a, b} bound a case doing
    {a, b, v} a-fortiori. Now a permissive record falls on a violating factor
    of any engaged provision that its facts never contained. On the corpus,
    two things are checked: no controlling record is permissive with an
    unaddressed violating factor of the case (the safety property), and every
    admission the rung produced meets its definition (permissive holding,
    factor in the case, in an engaged provision's violating list, absent from
    the record's facts). Since corpus 2.1.0 contested denials write deny
    records whose premise carries the violating factor, so permit records on
    the same provision do fall on it — the count is reported, not asserted
    zero. The probe fires on the synthetic case and checks the asymmetry (a
    deny is not cured by extra compliance). M29 dies."""
    adverse_traces = sum(1 for t in r.traces.values() if t.get("adverse_unaddressed"))
    adverse_admissions = sum(1 for t in r.traces.values() for s in t["admissions"].values()
                             if s == engine.ADVERSE_UNADDRESSED)
    fails = []
    store_by = {rec.id: rec for rec in r.store}
    unsafe = ill_defined = 0
    for c in r.cases:
        t = r.traces[c["id"]]
        case = engine.case_from_dict(c)
        if t["gate_outcome"] == engine.GOVERNED:
            if engine.adverse_unaddressed(store_by[t["controlling"]], case, r.provisions):
                unsafe += 1
        for rid, factors in (t.get("adverse_unaddressed") or {}).items():
            rec = store_by[rid]
            viol = set()
            for pid in c["rules"]:
                viol |= set(r.provisions[pid].violate_factors)
            if rec.interp not in engine.PERMISSIVE or not factors or any(
                    f not in set(c["facts"]) or f not in viol or f in set(rec.facts) for f in factors):
                ill_defined += 1
    if unsafe or ill_defined:
        fails.append(f"{unsafe} bound cases with an unaddressed adverse fact; {ill_defined} adverse falls outside the definition")
    P = engine.Provision(id="P", family="f", title="t", absolute=False, citation="", source_status="",
                         comply_factors=["a", "b"], violate_factors=["v"], tau=40, scope_domain="d")
    Q = engine.Provision(id="Q", family="f", title="t", absolute=False, citation="", source_status="",
                         comply_factors=["c"], violate_factors=["w"], tau=40, scope_domain="d")
    base = dict(id="R", case="c0", prov="P", rules=["P"], facts=["a", "b"], premise=["a", "b"], interp="permit",
                auth_class="judges", auth_id="j", rationale="", scope_domain="d", scope_width=3, ts=1, depth=1,
                expiry=None, referral=None, cites=[], outcome="permit", admission_ground="seed")
    permit = engine.Record(**base)
    deny = engine.Record(**{**base, "id": "D", "facts": ["a", "b", "v"], "premise": ["a", "v"], "interp": "deny"})
    saw = engine.Record(**{**base, "id": "S", "facts": ["a", "b", "v"], "interp": "permit_conditional"})

    def case(facts, rules=("P",)):
        return engine.Case(id="x", category="t", rules=list(rules), facts=list(facts), ts=2, contest_to=0,
                           author_kind="human")
    provs = {"P": P, "Q": Q}
    t = engine.adjudicate(case(["a", "b", "v"]), [permit], provs)
    if not (t["gate_outcome"] == engine.ADVERSE_FACT and t["route"] == engine.ROUTE_FRESH and t["decision"] == engine.DENY):
        fails.append(f"permit past a new violating factor: {t['gate_outcome']}/{t['route']}/{t['decision']}")
    t = engine.adjudicate(case(["a", "b"]), [permit], provs)
    if t["controlling"] != "R":
        fails.append("permit no longer binds the compliant case it governs")
    t = engine.adjudicate(case(["a", "b", "v"]), [saw], provs)
    if t["controlling"] != "S":
        fails.append("an acceptance that SAW the violation no longer binds the case that repeats it")
    t = engine.adjudicate(case(["a", "v", "b"]), [deny], provs)
    if t["controlling"] != "D":
        fails.append("asymmetry broken: a deny record was 'cured' by extra compliance")
    t = engine.adjudicate(case(["a", "b", "c", "w"], rules=("P", "Q")), [permit], provs)
    if t["gate_outcome"] != engine.ADVERSE_FACT:
        fails.append(f"a violation of the SECOND engaged provision did not fall the record: {t['gate_outcome']}")
    ok = not fails
    return (ok,
            f"{adverse_admissions} adverse falls in {adverse_traces} traces on the corpus, all within the "
            f"definition; {unsafe} bound cases with an unaddressed adverse fact (must be 0); probe "
            f"{'passes' if not fails else 'FAILS'} — permit past v falls to fresh/deny, acceptance that saw v "
            f"still binds, deny not cured, second provision's violation falls the record",
            fails[:4])


@check("VC-56", "Decided under prior text — an adopted amendment touching a premise factor unsettles the holding; a citation-only amendment unsettles nothing; inert on this corpus")
def vc56(r):
    """5.13.0. Records carry the provision text version they were decided
    under (`prov_version`); the rulebook may carry `version` and an
    `amendment_history` of touched factors. A record whose premise an
    amendment touched falls with cause decided_under_prior_text; one whose
    premise the amendment left alone still governs. On the released corpus
    every provision is at version 1 and no record is stale. Coherence at
    load: amendment versions distinct, ascending, >= 2, matching `version`.
    M30 dies."""
    stale = sum(1 for rec in r.store if rec.prov_version != r.provisions[rec.prov].version)
    prior = sum(1 for t in r.traces.values() if t.get("prior_text"))
    fails = []
    rec = engine.Record(id="R", case="c0", prov="P", rules=["P"], facts=["a", "b"], premise=["a", "b"], interp="permit",
                        auth_class="judges", auth_id="j", rationale="", scope_domain="d", scope_width=3, ts=1, depth=1,
                        expiry=None, referral=None, cites=[], outcome="permit", admission_ground="seed")
    case = engine.Case(id="x", category="t", rules=["P"], facts=["a", "b"], ts=2, contest_to=0, author_kind="human")
    base = {"id": "P", "family": "f", "title": "t", "absolute": False, "factors": {"comply": ["a", "b"], "violate": ["v"]}, "tau": 40}
    touched = engine.Provision.from_dict({**base, "version": 2, "amendment_history": [{"version": 2, "touched_factors": ["a"]}]})
    t = engine.adjudicate(case, [rec], {"P": touched})
    if not (t["gate_outcome"] == engine.PRIOR_TEXT_ONLY and t["controlling"] is None):
        fails.append(f"amended premise factor did not unsettle the holding: {t['gate_outcome']}")
    elsewhere = engine.Provision.from_dict({**base, "version": 2, "amendment_history": [{"version": 2, "touched_factors": ["v"]}]})
    if engine.adjudicate(case, [rec], {"P": elsewhere})["controlling"] != "R":
        fails.append("an amendment touching a factor outside the premise unsettled the holding")
    citation = engine.Provision.from_dict({**base, "version": 2, "amendment_history": [{"version": 2, "touched_factors": []}]})
    if engine.adjudicate(case, [rec], {"P": citation})["controlling"] != "R":
        fails.append("a citation-only amendment unsettled the holding")
    fresh = engine.Record(**{**rec.__dict__, "id": "R2", "prov_version": 2})
    if engine.adjudicate(case, [fresh], {"P": touched})["controlling"] != "R2":
        fails.append("a record decided under the amended text did not bind")
    for bad in ([{"version": 1, "touched_factors": []}], [{"version": 3, "touched_factors": []}, {"version": 2, "touched_factors": []}]):
        try:
            engine.Provision.from_dict({**base, "amendment_history": bad})
            fails.append(f"coherence rule accepted {bad}")
        except ValueError:
            pass
    ok = stale == 0 and prior == 0 and not fails
    return (ok,
            f"{stale} records decided under a text version other than the current one and {prior} traces with a "
            f"prior-text fall on the released corpus (0 expected: every provision is at version 1); probe "
            f"{'passes' if not fails else 'FAILS'} — touched premise unsettles, untouched and citation-only do not, "
            f"a record under the new text binds, incoherent histories refused",
            fails[:4])


def s_leak(block, case):
    """True if what an arm is shown carries the case's own category or id."""
    return (case["id"] in block or case.get("category", "") in block
            or "scenario" in block.lower())


def main():
    run = Run()
    print(f"SemiFab conformance — corpus {run.pack['corpus_version']}, "
          f"{len(run.cases)} cases, opening store {len(run.seed)}, "
          f"final store {len(run.store)}")
    print("=" * 78)
    passed = 0
    for cid, desc, fn in CHECKS:
        ok, detail, sample = fn(run)
        status = "PASS" if ok else "FAIL"
        passed += 1 if ok else 0
        print(f"{cid}  {status}  {desc}")
        print(f"        {detail}")
        if not ok and sample:
            print(f"        sample: {sample}")
    print("=" * 78)
    print(f"RESULT: {passed}/{len(CHECKS)}")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
