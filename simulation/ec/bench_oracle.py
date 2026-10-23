"""
The bench's two answer keys (governance build v3, §3.1 R1).

Judges are shown the canon tier, the glosses and the conscience's filing, so
they are asked to apply the canon as well as the rulebook. `engine.adjudicate`
never sees the canon, so it alone is not a fair key. Two keys are kept:

  oracle_engine  `engine.adjudicate` on a copy of the case and a read-only view
                 of the store, unchanged;
  oracle_canon   the engine's holding, then the canon rules the gate already
                 uses applied to the act as filed, on the canon and registry
                 state of the filing day (the gate's per-entry answers, snapshot
                 at filing). The final canon key is the most restrictive of the
                 engine holding and the canon holding (deny > permit_conditional
                 > permit), except that a risk-owner contest (contest_to >= 4)
                 takes the engine's permit_conditional overlay after the canon
                 unless the canon denied on T0 (A6 outranks A4).

No rule is written twice: the per-entry answers come from `gate.entry_answers`.
DJ-D4..D6 and D8..D9 concern precedent and have no canon counterpart, so on
them the canon key equals the engine key; the canon moves only the holding.
Pure: nothing here writes the store, the canon or the registry.
"""

from __future__ import annotations

PERMIT = "permit"
PERMIT_CONDITIONAL = "permit_conditional"
DENY = "deny"
HOLDING_RANK = {PERMIT: 0, PERMIT_CONDITIONAL: 1, DENY: 2}
ORIGIN_EC = "ec_filing"
ORIGIN_CORPUS = "corpus_contest"


def most_restrictive(*holdings) -> str | None:
    hs = [h for h in holdings if h in HOLDING_RANK]
    if not hs:
        return None
    return max(hs, key=lambda h: HOLDING_RANK[h])


def entry_canon_outcome(pe: dict) -> tuple:
    """(holding or None, basis) for one engaged entry's per-entry answers."""
    tier = pe.get("tier")
    if tier == "T0":
        return (DENY, "t0_absolute") if pe.get("contravened") else (None, None)
    if tier == "T1":
        if not pe.get("contravened"):
            return None, None
        if pe.get("gloss_bar") or pe.get("token_fail") == "codified_class":
            return DENY, "t1_binding_gloss"
        return (PERMIT, "t1_valid_token") if pe.get("token_valid") else (DENY, "t1_no_valid_token")
    if tier == "T2":
        if not pe.get("departure"):
            return None, None
        ok = pe.get("t2_admitted") and pe.get("t2_evidence") and pe.get("t2_in_bound")
        return (PERMIT, "t2_admitted_in_bound") if ok else (DENY, "t2_not_admitted")
    if tier == "T3":
        if not pe.get("departure"):
            return None, None
        return (PERMIT, "t3_in_context") if pe.get("t3_in_context") else (DENY, "t3_out_of_context")
    return None, None


def canon_holding(per_entry: list, conflict: bool = False) -> tuple:
    """(holding or None, basis, t0_deny). Several engaged entries (and a conflict
    hold between non-tradables) give the most restrictive of their outcomes."""
    outs = [entry_canon_outcome(pe) for pe in (per_entry or [])]
    outs = [(h, b) for h, b in outs if h is not None]
    if not outs:
        return None, "no_contravention", False
    h = most_restrictive(*[o[0] for o in outs])
    basis = next(b for hh, b in outs if hh == h)
    if conflict and len(outs) >= 2:
        basis = "conflict_most_restrictive:" + basis
    t0 = any(b == "t0_absolute" for _hh, b in outs)
    return h, basis, t0


def engine_answers(trace: dict, case, engine) -> dict:
    """The engine's answers to DJ-D1..D10 and PR-D1, from one trace."""
    route = trace.get("route")
    absolute = route in (engine.ROUTE_ABSOLUTE, getattr(engine, "ROUTE_FLOOR_UNRESOLVED", "floor_unresolved"))
    hinted = case.extra.get("premise") or case.facts
    premise = sorted(f for f in hinted if f not in case.unrecorded)
    charge = None
    if trace.get("rating") is not None and trace.get("tau") is not None:
        charge = trace["rating"] >= trace["tau"]
    return {
        "engaged": bool(case.rules),
        "absolute": {"violated": bool(absolute), "silent_floor": route == getattr(engine, "ROUTE_FLOOR_UNRESOLVED", None),
                     "provision": trace.get("absolute_provision")},
        "control_plane": bool(trace.get("draft_amendment")),
        "relevant": list(trace.get("consulted") or []),
        "admissions": dict(trace.get("admissions") or {}),
        "controlling": trace.get("controlling"),
        "ordering_keys": list(trace.get("keys_applied") or []),
        "holding": trace.get("decision"),
        "premise": premise,
        "write_precedent": bool(trace.get("admitted")),
        "premise_established": not bool(trace.get("record_withheld")),
        "refer_up": bool(trace.get("referral_emitted")),
        "route": route,
        "gate_outcome": trace.get("gate_outcome"),
        "escalated_to": trace.get("escalated_to"),
        "prosecutor_charge": charge,
        "rating": trace.get("rating"),
        "tau": trace.get("tau"),
    }


def bench_oracle(case_dict: dict, store: list, provisions: dict, theta, engine, filing: dict) -> dict:
    """{"engine": answers, "trace": trace, "canon": {"holding", "basis"}, "disagree": bool}.

    `filing` carries `contest_to`, `origin` (ec_filing | corpus_contest), the
    gate's `per_entry` answers snapshot at filing (None for a corpus contest)
    and `conflict`."""
    d = dict(case_dict)
    d["contest_to"] = int(filing.get("contest_to", d.get("contest_to", 0)) or 0)
    case = engine.case_from_dict(d)
    trace = engine.adjudicate(case, list(store), provisions, theta)
    eng = engine_answers(trace, case, engine)
    e_hold = eng["holding"]
    per_entry = filing.get("per_entry")
    if filing.get("origin") == ORIGIN_CORPUS or not per_entry:
        final, basis = e_hold, "canon_silent"
    else:
        ch, cbasis, t0 = canon_holding(per_entry, bool(filing.get("conflict")))
        if ch is None:
            final, basis = e_hold, "no_contravention"
        else:
            final, basis = most_restrictive(e_hold, ch), cbasis
            if d["contest_to"] >= 4 and not t0:
                final, basis = PERMIT_CONDITIONAL, cbasis + "+risk_owner_overlay"
    return {"engine": eng, "trace": trace, "canon": {"holding": final, "basis": basis}, "disagree": final != e_hold}
