    # ---- REPORTED, ORACLE-DERIVED: the binding gate (release 5.11.0) -------
    # Every arm names a controlling record or none. Where it names one it has
    # BOUND — compelled a disposition from a precedent — and the question the
    # binding gate asks is whether that record in fact governs. Unlike the
    # agreement rate above this is one-sided and bounded: an exact upper limit
    # on the false-bind rate, `None` rather than zero when an arm never binds,
    # a floor below which the verdict is inconclusive, and E-distinguish guard
    # items on which a single bind fails. The oracle is the reference engine's
    # own trace, so the verdict can never be 'pass' here; what the endpoint
    # adds is the bound, which the agreement rate does not carry. Model arms
    # are not asked WHY they did not cite, so their abstention causes are
    # scored as 'not elicited' and the divergence count is not meaningful for
    # them.
    import binding_gate as BG
    bg_oracle = []
    for cid in sorted(corpus_ids):
        c = by_id[cid]
        t = ref_traces.get(cid)
        if not t:
            continue
        oc = BG.oracle_from_trace(c, t, provisions)
        if oc is not None and cid in answers:
            bg_oracle.append(oc)

    def bg_answer(oc):
        _, ctl = final(oc.case_id)
        if isinstance(ctl, str) and ctl not in ("none", "null", ""):
            return BG.Answer(engine.GOVERNED, ctl)
        return BG.Answer("not_elicited", None)
    bg = BG.evaluate(bg_oracle, bg_answer).as_dict() if bg_oracle else None
    if bg:
        bg = {k: bg[k] for k in ("verdict", "cause", "n_cases", "binds", "false_binds",
                                 "false_bind_upper_bound", "missed_bind_rate", "by_verdict")}
        bg["guard_items"] = sum(1 for o in bg_oracle if o.guard)
        bg["guard_binds"] = sum(1 for o in bg_oracle if o.guard and bg_answer(o).outcome == engine.GOVERNED)
        bg["note"] = ("One-sided: bounds false binds (a citation of a record that does not govern, or the "
                      "wrong record), reports missed binds. Verdict is 'inconclusive' at best because the "
                      "oracle is the reference engine's own trace; an independently labelled arm is what "
                      "would lift it.")
    binding = bg

