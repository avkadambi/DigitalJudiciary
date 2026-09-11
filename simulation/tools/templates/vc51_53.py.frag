

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
        facts = set(case.facts)
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
