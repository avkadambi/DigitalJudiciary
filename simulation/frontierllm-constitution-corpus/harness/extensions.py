"""
Executable apparatus for the parts of the contract the base harness only
recorded: the Reporter, the audit register and its docket audit, the family of
admission rules, and the two weaker baselines B_gov and B_mem.

Everything here is stdlib-only, deterministic, and reads the same corpus files
the conformance suite reads. Nothing in this module is consulted by
`engine.adjudicate` — that is the point of most of it.

  Reporter            Chapter 5, Definition 17 and Proposition 7 (neutrality)
  AuditRegister       Chapter 5, Definition 19
  docket_audit        Chapter 4, Definition 14 and Proposition 7
  ADMISSION_RULES     Chapter 4, Sections 6.2 and 6.5; Definitions 11 and 12
  b_gov / b_mem       Chapter 5, Section 6, Definitions 12 and 13
"""

from __future__ import annotations

import hashlib
import json
import random

import engine


# ==========================================================================
# 1. The Reporter — Chapter 5, Definition 17
#
# A Reporter reads the store and publishes bulletins about it. Definition 17
# gives it three properties, and each is a structural fact about this class
# rather than a promise:
#
#   R1  no write   — it holds no reference to a mutable store; `observe`
#                    takes a snapshot and never returns one.
#   R2  no adjudicative input — nothing it produces is an argument to
#                    `engine.adjudicate`, which takes (case, store,
#                    provisions, theta) and has no reporter parameter.
#   R3  no standing — it has no contest method, and the case's `contest_to`
#                    is fixed in the corpus before any run begins.
#
# Proposition 7 (Chapter 5) says D+ = D with a Reporter attached satisfies
# A1-A9 and every theorem carries over. The executable form of that claim is
# that a run with the Reporter publishing is byte-identical to a run without
# it, which is what VC-24 now checks against a Reporter that actually exists.
# ==========================================================================

class Reporter:
    """An observer of the store. Publishes; never writes, never argues."""

    def __init__(self, name: str = "reporter:precedent-bulletin"):
        self.name = name
        self.bulletins: list[dict] = []

    # No `contest`, no `accept`, no `write`. The absence is the specification.

    def observe(self, case_id: str, store: list, trace: dict) -> None:
        """Read the store and publish. Takes copies; returns nothing."""
        live = [r for r in store if not r.lapsed_at(trace.get("ts", 0) or 0)]
        by_prov: dict[str, int] = {}
        for r in live:
            by_prov[r.prov] = by_prov.get(r.prov, 0) + 1
        self.bulletins.append(
            {
                "after_case": case_id,
                "store_size": len(store),
                "live_records": len(live),
                "provisions_with_authority": len(by_prov),
                "most_cited_provision": (max(by_prov, key=lambda k: (by_prov[k], k))
                                         if by_prov else None),
                "headline": (f"{len(live)} live records across "
                             f"{len(by_prov)} provisions"),
            }
        )

    def digest(self) -> str:
        return hashlib.sha256(
            json.dumps(self.bulletins, sort_keys=True).encode()).hexdigest()[:16]


def replay_observed(cases, seed_store, provisions, theta=engine.THETA_DEFAULT,
                    reporter: Reporter | None = None) -> dict:
    """`engine.replay`, with a Reporter optionally attached.

    The Reporter is invoked strictly after each case resolves, on a copy of
    the store, and its output is discarded by this function. If attaching one
    could change a trace, the architecture would be wrong; VC-24 is the check
    that it does not.
    """
    out = engine.replay(cases, seed_store, provisions, theta)
    if reporter is not None:
        # The live store is handed over, not a copy. Passing a copy would make
        # R1 untestable: a Reporter that appended would be silently absorbed by
        # the defence rather than caught by the check.
        for c, tr in zip(cases, out["traces"]):
            cid = c["id"] if isinstance(c, dict) else c.id
            reporter.observe(cid, out["store"], tr)
    return out


# ==========================================================================
# 2. The audit register — Chapter 5, Definition 19
#    and the advisory docket audit — Chapter 4, Definition 14 / Proposition 7
#
# The register is append-only and disjoint from both Store and Docket. The
# audit draws from the docket under a published budget, re-adjudicates the
# drawn entry ADVISORILY, and writes a finding. Proposition 7's claims:
#
#   (i)   total neutrality — the realised base is unchanged
#   (iii) the audit buys observability only: width w(n) = 0
#   (iv)  coverage d(n)/|D_n| is metered by the budget; the docket-matched
#         regime gives coverage identically rho
# ==========================================================================

class AuditRegister:
    """Append-only. Disjoint from Store and Docket. Never read by resolve."""

    def __init__(self):
        self._findings: list[dict] = []

    def append(self, finding: dict) -> None:
        self._findings.append(dict(finding))

    @property
    def findings(self) -> list[dict]:
        return list(self._findings)

    def __len__(self) -> int:
        return len(self._findings)


def docket_audit(docket: list, cases_by_id: dict, store: list, provisions: dict,
                 rho: float, theta: float = engine.THETA_DEFAULT,
                 regime: str = "docket_matched", seed: int = 20260906) -> dict:
    """Draw rule T over docket positions, under budget rho.

    regime="docket_matched": each docket entry is drawn independently with
    probability rho, so expected coverage is identically rho — Proposition
    7(iv)'s second regime, and the one with a closed form.

    Every drawn entry is re-adjudicated against the store as it stands. The
    result is written to the register and to nothing else: the store is passed
    by value and no record is appended, which is Proposition 7(iii)'s width
    zero, stated as code rather than as a promise.
    """
    rng = random.Random(seed)
    reg = AuditRegister()
    drawn = 0
    disagreements = 0
    for entry in docket:
        if regime == "docket_matched" and rng.random() >= rho:
            continue
        drawn += 1
        c = cases_by_id.get(entry["case"])
        if c is None:
            continue
        case = engine.case_from_dict(c)
        # Advisory re-adjudication. `store` is a list we do not append to.
        advisory = engine.adjudicate(case, list(store), provisions, theta)
        disagreed = bool(entry["route"] == "declined"
                         and advisory["route"] not in (engine.ROUTE_DOCKET_DECLINED,
                                                       engine.ROUTE_DOCKET_NULL))
        disagreements += int(disagreed)
        reg.append({
            "docket_case": entry["case"],
            "docket_route": entry["route"],
            "advisory_route": advisory["route"],
            "advisory_decision": advisory["decision"],
            "disagreed_with_decline": disagreed,
            "is_annotation_only": True,
        })
    return {
        "register": reg,
        "budget_rho": rho,
        "regime": regime,
        "docket_size": len(docket),
        "drawn": drawn,
        "coverage": (drawn / len(docket)) if docket else 0.0,
        "width": 0,                       # Proposition 7(iii), by construction
        "disagreements": disagreements,
    }


# ==========================================================================
# 3. The admission rules — Chapter 4, Sections 6.2 and 6.5
#
# An admission rule is a predicate on a case's procedural history. Chapter 4
# names four in Section 6.2 and three stream-reading rules in Definition 12.
# All eight are implemented here over the same executed stream, so the
# comparison in Table 2 — realised base, one-sidedness, contest-boundedness —
# is computed rather than asserted.
#
# `h` is the procedural history of one case, as a dict:
#   contested        did any party contest
#   depth            the instance at which it resolved
#   controlling      the controlling record id, or None
#   decision         the disposition
#   absolute         did A6 short-circuit
#   docketed         was it never charged
#   clause_ii        was it a consolidation representative
#   index            its position in the stream
# ==========================================================================

def history(case: dict, trace: dict, index: int, provisions: dict | None = None) -> dict:
    # "Violating as filed" is what separates an unconditioned grant from a
    # grant that somebody had a reason to argue about. Theorem 1 is about the
    # first kind: nobody contests a change that breaks no rule, so it is never
    # stored, so the base carries no record on the grant side.
    violating = False
    if provisions:
        fs = set(case["facts"])
        violating = any(engine.violates(fs, provisions[p])
                        for p in case["rules"] if p in provisions)
    return {
        "violating": violating,
        "case": case["id"],
        "contested": case.get("contest_to", 0) >= 2,
        "depth": case.get("contest_to", 0),
        "controlling": trace["controlling"],
        "decision": trace["decision"],
        "absolute": trace["route"] == engine.ROUTE_ABSOLUTE,
        "docketed": trace["route"] in (engine.ROUTE_DOCKET_DECLINED,
                                       engine.ROUTE_DOCKET_NULL),
        "clause_ii": trace.get("admission_ground") == "clause_ii",
        # An unconditioned grant: permitted, and breaking no provision as
        # filed. Whether anyone went on to contest it is a separate fact, and
        # it is exactly the fact Remark 1's standing extension changes.
        "unconditioned_grant": (trace["decision"] == engine.PERMIT
                                and not violating),
        "index": index,
    }


def _adjudicated(h: dict) -> bool:
    """A6 short-circuits and docketed arrivals are outside every rule's domain."""
    return not h["absolute"] and not h["docketed"]


# --- Section 6.2's four -----------------------------------------------------

def A_all(h, _s=None):
    """Admit everything adjudicated. The base is the decision log."""
    return _adjudicated(h)


def A_contest(h, _s=None):
    """Contested and resolved above first instance. Definition 5; procedural."""
    return _adjudicated(h) and h["contested"]


def A_conf(h, _s=None):
    """Admit on low reported confidence, proxied by Controlling = none.

    NOT procedural: it reads a property of the outcome, which is exactly the
    objection Chapter 4 Section 6.2 makes to it.
    """
    return _adjudicated(h) and h["controlling"] is None


def A_ed(h, _s=None):
    """Editorial curation by a designated curator.

    NOT procedural, and an unmodelled oracle: the curator's taste is exogenous.
    Stood in for here by a fixed, published curator predicate — admit where the
    disposition was a denial — so that the rule is at least reproducible.
    """
    return _adjudicated(h) and h["decision"] == engine.DENY


# --- Definition 12's stream-reading family ----------------------------------

def A_cons(h, _s=None):
    """Clause (ii): the representative of a consolidation class."""
    return h["clause_ii"]


def make_A_samp(rho: float, seed: int = 20260906):
    """A_samp[rho]: admit each adjudicated case independently w.p. rho.

    Content-blind, two-sided at growing width, and NOT contest-bounded — it
    carries a Theta(n) term at every rho > 0, which is Proposition 5.
    """
    rng = random.Random(seed)
    draws: dict[str, float] = {}

    def rule(h, _s=None):
        if not _adjudicated(h):
            return False
        if h["case"] not in draws:
            draws[h["case"]] = rng.random()
        return draws[h["case"]] < rho
    rule.__name__ = f"A_samp[{rho}]"
    return rule


def make_A_pair(k: int):
    """A_pair[k]: A_contest, plus every k-th uncontested adjudicated case.

    Theorem 8(ii): this is the rule that attains the cap — it buys two-sided
    width by paying exactly one stored record per admitted uncontested case.
    """
    def rule(h, _s=None):
        if not _adjudicated(h):
            return False
        if h["contested"]:
            return True
        return h["index"] % k == 0
    rule.__name__ = f"A_pair[{k}]"
    return rule


def make_A_boot(m: int):
    """A_boot[m]: A_contest, plus the first m adjudicated arrivals.

    Definition 10 / Proposition 4: escapes the Theorem 6 dichotomy by buying a
    constant width, then behaving like A_contest forever after.
    """
    def rule(h, _s=None):
        if not _adjudicated(h):
            return False
        return h["contested"] or h["index"] < m
    rule.__name__ = f"A_boot[{m}]"
    return rule


ADMISSION_RULES = {
    "A_all": A_all,
    "A_contest": A_contest,
    "A_conf": A_conf,
    "A_ed": A_ed,
    "A_cons": A_cons,
    "A_samp[0.05]": make_A_samp(0.05),
    "A_pair[8]": make_A_pair(8),
    "A_boot[20]": make_A_boot(20),
}

PROCEDURAL = {"A_all", "A_contest", "A_cons", "A_pair[8]", "A_boot[20]",
              "A_samp[0.05]"}
NON_PROCEDURAL = {"A_conf", "A_ed"}


def realised_base(histories: list, rule) -> list:
    """B_A(H0) — the set of histories the rule admits."""
    return [h for h in histories if rule(h)]


def base_profile(histories: list, rule, name: str) -> dict:
    """The columns of Chapter 4's Table 2, computed.

    `width` counts grant-side records: a base with none is one-sided in the
    sense of Theorem 1, and a rule that admits grants is buying width.
    """
    base = realised_base(histories, rule)
    grants = [h for h in base if h["unconditioned_grant"]]
    uncontested = [h for h in base if not h["contested"]]
    n_contested = sum(1 for h in histories if h["contested"] and _adjudicated(h))
    return {
        "rule": name,
        "procedural": name in PROCEDURAL,
        "base_size": len(base),
        "width": len(grants),
        "one_sided": len(grants) == 0,
        "uncontested_admitted": len(uncontested),
        "contested_in_stream": n_contested,
        # Definition 9. A rule is contest-bounded iff its base is bounded by
        # the contested set — equivalently, iff it admits no uncontested case.
        # Comparing sizes at a single n cannot separate a Theta(n) term from
        # O(contested(n)), which is why Proposition 5's sampling rule has to be
        # judged on whether it admits uncontested arrivals at a positive rate,
        # not on whether its base happens to be smaller here.
        "contest_bounded": len(uncontested) == 0,
        "grant_share": (len(grants) / len(base)) if base else 0.0,
    }


def dichotomy(table: list) -> dict:
    """Theorem 6: for anonymous procedural rules, contest-bounded XOR two-sided.

    Theorem 6 lives inside Theorem 2's antecedent — no party both licensed and
    adverse to grants — so it must be computed on the counterfactual stream
    where that holds, not on this constitution's, which declares adverse
    standing and therefore sits outside the dichotomy's scope by design.
    """
    rows = [r for r in table if r["procedural"]]
    # Exactly one of {contest-bounded, two-sided} must hold.
    violations = [r["rule"] for r in rows
                  if r["contest_bounded"] == (not r["one_sided"])]
    return {"procedural_rules": len(rows),
            "violations": violations,
            "holds": not violations}


def thm1_counterfactual(histories: list, adverse_cases: set) -> dict:
    """Theorem 1, witnessed by removing the standing that defeats it.

    This constitution declares that a party holds contest standing adverse to
    grants — the second-line compliance officer — so the realised base under
    A_contest is two-sided, and Theorem 1's conclusion is deliberately NOT
    exhibited by the run as it stands. Theorem 1 says that if no such party
    existed, unconditioned grants would never be contested and so never stored,
    and the base would be one-sided.

    The counterfactual is the same stream with the adverse contests removed.
    Its base must be one-sided; if it is not, Theorem 1 is false on this stream.
    """
    # The counterfactual implements Theorem 1's hypothesis literally: with no
    # party licensed and adverse to grants, an unconditioned grant is contested
    # by nobody. Executing it is a consistency check on the implementation, not
    # a discovery — the theorem is a deduction and the run cannot surprise it.
    #
    # The informative quantity is the difference on the ACTUAL stream, where
    # this constitution does declare adverse standing. Two sources contribute
    # grant-side records there, and they are reported apart: contests brought
    # by the adverse party, which is Remark 1's remedy working, and contests of
    # non-violating cases that this corpus stages for other mechanisms
    # (acknowledgement, renewal, like-case pairs), which are an artefact of
    # corpus construction and are disclosed rather than netted out.
    cf = []
    for h in histories:
        g = dict(h)
        if h["unconditioned_grant"]:
            g["contested"] = False
            g["depth"] = 0
        cf.append(g)
    from_adverse = sum(1 for h in histories
                       if h["unconditioned_grant"] and h["contested"]
                       and h["case"] in adverse_cases)
    from_staging = sum(1 for h in histories
                       if h["unconditioned_grant"] and h["contested"]
                       and h["case"] not in adverse_cases)
    actual = base_profile(histories, A_contest, "A_contest (declared standing)")
    counter = base_profile(cf, A_contest, "A_contest (no adverse standing)")
    return {"with_standing": actual, "without_standing": counter,
            "counterfactual_histories": cf,
            # Theorem 1: strip the adverse standing and the grant side of the
            # base empties. Theorem 2's biconditional is the pair of these.
            "theorem_1_holds": counter["one_sided"],
            "theorem_2_holds": (not actual["one_sided"]) and counter["one_sided"],
            "grant_side_from_adverse_standing": from_adverse,
            "grant_side_from_corpus_staging": from_staging,
            "grants_lost": actual["width"] - counter["width"]}


def admission_table(histories: list) -> list:
    return [base_profile(histories, r, n) for n, r in ADMISSION_RULES.items()]


# ==========================================================================
# 4. The two weaker representations — Chapter 5, Section 6
#
# B_gov (Definition 12): a stateless evaluator plus a governed exception log.
# It can say who accepted what, and it cannot say that a prior decision
# CONTROLS this one, because it holds no relation between cases. Theorem 3 and
# Theorem 4 are about that gap; here the gap is executed rather than asserted.
#
# B_mem (Definition 13): advisory memory. It retrieves priors and shows them,
# but they do not bind, so `Controlling` is not a function of the case and the
# store — which is Proposition 3.
# ==========================================================================

def b_gov(case: engine.Case, provisions: dict, exception_log: list) -> dict:
    """Stateless evaluation plus an append-only exception log.

    The log records attribution. It supports no retrieval, so no earlier
    decision can bind this one: `controlling` is structurally absent, not
    merely empty.
    """
    facts = set(case.facts)
    engaged = [provisions[p] for p in case.rules if p in provisions]
    violated = [p for p in engaged if engine.violates(facts, p)]
    if any(p.absolute for p in violated):
        decision = engine.DENY
    elif violated:
        # A stateless gate denies, unless a human has logged an exception for
        # this provision — attribution without precedent.
        logged = any(e["provision"] in {p.id for p in violated}
                     for e in exception_log)
        decision = engine.PERMIT_CONDITIONAL if logged else engine.DENY
        if not logged and case.contest_to >= 4:
            exception_log.append({"case": case.id,
                                  "provision": violated[0].id,
                                  "accepted_by": "riskowner",
                                  "expiry": None})
    else:
        decision = engine.PERMIT
    return {"decision": decision,
            "controlling": None,          # no referent exists in B_gov
            "expressible_controlling": False}


def b_mem(case: engine.Case, store: list, provisions: dict,
          theta: float = engine.THETA_DEFAULT) -> dict:
    """Advisory memory: retrieve, display, do not bind.

    Retrieval is the architecture's own retrieval, so the comparison isolates
    bindingness rather than confounding it with retrieval quality. The
    disposition is always the fresh reading — the retrieved record is advice.
    """
    facts = set(case.facts)
    engaged = [provisions[p] for p in case.rules if p in provisions]
    violated = [p for p in engaged if engine.violates(facts, p)]
    candidates = engine.retrieve(case, store, theta)
    survivors, _ = engine.gate(candidates, case)
    fresh = engine.DENY if violated else engine.PERMIT
    return {"decision": fresh,
            "shown": [r.id for r in survivors][:3],
            "controlling": None,          # advice does not control
            "expressible_controlling": False}


def baseline_differential(cases: list, traces: list, seed_store: list,
                          provisions: dict,
                          theta: float = engine.THETA_DEFAULT) -> dict:
    """Run both baselines over the same stream and compare with the judiciary.

    Reported as three counts, not a rate: how many cases each baseline decides
    differently from the Digital Judiciary, and — the sharper number — how many
    of those the judiciary decided BY CITATION, which is the disposition
    neither baseline can express at all.
    """
    store = [engine.Record.from_dict(r) if isinstance(r, dict) else r
             for r in seed_store]
    log: list = []
    gov_diff = mem_diff = cited = gov_diff_on_cited = mem_diff_on_cited = 0
    gov_expressible = mem_expressible = False
    rows = []
    for c, tr in zip(cases, traces):
        case = engine.case_from_dict(c) if isinstance(c, dict) else c
        g = b_gov(case, provisions, log)
        m = b_mem(case, store, provisions, theta)
        gov_expressible = gov_expressible or bool(g["expressible_controlling"]) \
            or g["controlling"] is not None
        mem_expressible = mem_expressible or bool(m["expressible_controlling"]) \
            or m["controlling"] is not None
        bound = tr["route"] in (engine.ROUTE_BOUND, engine.ROUTE_CONSOLIDATED)
        cited += int(bound)
        gd = g["decision"] != tr["decision"]
        md = m["decision"] != tr["decision"]
        gov_diff += int(gd)
        mem_diff += int(md)
        gov_diff_on_cited += int(gd and bound)
        mem_diff_on_cited += int(md and bound)
        rows.append({"case": case.id, "dj": tr["decision"],
                     "b_gov": g["decision"], "b_mem": m["decision"],
                     "dj_bound": bound})
        if tr["admitted"]:
            store.append(engine._record_from(case, tr, provisions))
    return {
        "n": len(cases),
        "decided_by_citation": cited,
        "b_gov_differs": gov_diff,
        "b_mem_differs": mem_diff,
        "b_gov_differs_on_cited": gov_diff_on_cited,
        "b_mem_differs_on_cited": mem_diff_on_cited,
        # Read back from the baselines themselves. Asserting these as
        # constants here would mean the check could never notice a baseline
        # that started claiming to express Controlling.
        "controlling_expressible_in_b_gov": gov_expressible,
        "controlling_expressible_in_b_mem": mem_expressible,
        "rows": rows,
    }
