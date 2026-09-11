"""The five arms, over one interface.

Each arm answers the same question about the same change: what is the
disposition, and which earlier decision controls. What differs is what the arm
sees, and whether an earlier decision BINDS it.

The store is grown identically for every arm, from the executed reference run,
so no arm is advantaged or disadvantaged by seeing a different case base. What
an arm is SHOWN out of that store is the manipulation.

One asymmetry is deliberate and is the whole point of arm B: the judiciary does
not call a model where the architecture does not ask anyone. An absolute floor,
a controlling record and a docketed arrival are decided without a call, so the
cost of arm B falls with the contest rate rather than with volume. That is R7,
and it is measured here rather than assumed.
"""

from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import engine  # noqa: E402


def shown_records(arm, case, store, theta):
    """What this arm gets to see out of the store."""
    view = arm["store_view"]
    if view == "none":
        return []
    c = engine.case_from_dict(case)
    if view == "topk":
        # Retrieval only: no gate, no ordering, AND NO LAPSE FILTER.
        #
        # This was wrong until the discriminating scenarios exposed it.
        # `engine.retrieve` drops records whose acceptance has expired, which is
        # one of the architecture's own mechanisms — so routing the monolith
        # arms through it handed them the lapse clock for free and made them
        # look better than a document store makes them. A retrieval index over
        # an exception log has no expiry semantics: it returns the approval, and
        # the approval does not say it is dead.
        cand = [r for r in store
                if r.prov in c.rules and engine.coverage(r, set(c.facts)) >= theta]
        return sorted(cand, key=lambda r: -r.ts)[: arm["k_records"]]
    if view == "gated":
        cand = engine.retrieve(c, store, theta)
        surv, _ = engine.gate(cand, c)
        return surv[: arm["k_records"]]
    if view == "log":
        # Same correction: an exception log lists acceptances, live or lapsed.
        # B_gov: an exception log. Attribution, no case-level relation — so the
        # entries shown are risk-owner acceptances on the engaged provisions,
        # with their premises stripped, because a log records who accepted what
        # and not what facts it turned on.
        entries = [r for r in store
                   if r.auth_class == "riskowner" and r.prov in case["rules"]]
        # no lapse filter: the log is a list of what was approved, not of what
        # is still in force
        out = []
        for r in sorted(entries, key=lambda r: -r.ts)[: arm["k_records"]]:
            stripped = engine.Record(**{**r.__dict__, "premise": []})
            out.append(stripped)
        return out
    raise ValueError(view)


def decide(arm_name, arm, case, store, provisions, theta, judge, rulebook):
    """Return (answer, called_model).

    `answer` is {disposition, controlling, reasons, malformed?} or None in dry
    mode. `called_model` records whether this arrival consumed a model call,
    which is what the cost endpoint is really measuring.
    """
    c = engine.case_from_dict(case)
    facts = set(case["facts"])

    if arm["binds"]:
        # ---- Arm B: the Digital Judiciary ------------------------------
        engaged = [provisions[p] for p in case["rules"] if p in provisions]

        # A6: an absolute floor short-circuits before retrieval. No call.
        for p in engaged:
            if p.absolute and engine.violates(facts, p):
                return ({"disposition": engine.DENY, "controlling": None,
                         "route": "absolute floor",
                         "reasons": f"{p.id} is absolute and is violated"}, False)

        # No provision engaged: the Evaluator's null route. No call.
        if not engaged:
            return ({"disposition": None, "controlling": None,
                     "route": "no provision, docketed",
                     "reasons": "no provision engaged; docketed"}, False)

        # Retrieve, gate, order. A controlling record BINDS: no call. This runs
        # BEFORE the prosecutor rates, as in engine.adjudicate — an earlier form
        # of this arm rated first and docketed a fully compliant arrival that a
        # live record in fact controlled, which the federated stream exposed:
        # the arm declined two cross-division cases the reference bound.
        surv, _ = engine.gate(engine.retrieve(c, store, theta), c)
        if surv:
            top, _ = engine.order(surv)
            if top not in (None, "none_tie"):
                return ({"disposition": top.interp, "controlling": top.id,
                         "route": "bound by " + top.id,
                         "reasons": "bound by the controlling record"}, False)

        # Nothing controls. The prosecutor declines below tau, and the arrival
        # is docketed. No call.
        rating = engine.rate(c, provisions)
        tau = min(p.tau for p in engaged)
        if rating is not None and rating < tau:
            return ({"disposition": None, "controlling": None,
                     "route": "declined, docketed",
                     "reasons": "declined below the charging threshold; docketed"}, False)

        # Nothing controls. This is where the architecture asks for judgment,
        # and the only place arm B pays for a model.
        ans = judge.judge(case, surv[: arm["k_records"]], provisions, arm, rulebook)
        if ans is not None:
            top = engine.order(surv)[0] if surv else None
            ans.setdefault("route", "tie, decided fresh" if top == "none_tie"
                           else "nothing controls, escalated")
        return (ans, True)

    # ---- Arms A, A+, B_mem, B_gov: the model decides every arrival -------
    shown = shown_records(arm, case, store, theta)
    ans = judge.judge(case, shown, provisions, arm, rulebook)
    if ans is not None:
        ans.setdefault("route", "model call, %d record(s) shown" % len(shown))
    return (ans, True)
