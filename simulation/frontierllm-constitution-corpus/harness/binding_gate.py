"""The binding acceptance gate — is a gate fit to compel a decision?

A conformance check counts agreements. This module bounds a rate and refuses:
it scores an adjudicator's bindings against an oracle, puts a one-sided exact
binomial upper bound on the false-bind rate, and returns `pass` only when the
evidence base is large enough for the bound to mean anything, when no guard
item was bound, and when the oracle was not written by the engine's authors.

Why one-sided. A missed bind costs a reviewer a case they must decide
themselves. A **false bind** compels a disposition from a record that does not
govern, and its audit trail is accurate in every field, so nothing downstream
can catch it. The gate bounds false binds and merely reports missed ones;
gating recall would trade the expensive error for the cheap one.

Why a floor. Perfect precision is satisfiable by never binding. Below a floor
on binds actually made the verdict is `inconclusive`, never `pass`, and the
upper bound is `None` when nothing was bound — not zero.

Why guards. A guard is a case where binding is wrong by construction. One
guard bind fails at any n.

Why the oracle matters. Computed ground truth is a second program written from
the same rulebook. A shared misreading reads as perfect precision. A pass on a
self-authored oracle alone is therefore `inconclusive`, with the cause named;
an independently authored arm (`arm="independent"`) is what lifts it.

The mathematics is one function: the Clopper-Pearson exact upper limit, the
largest rate p at which observing k or fewer failures in n trials is still
plausible at level alpha, found by bisection on the binomial CDF summed in log
space. At k = 0 it is 1 - alpha^(1/n), of which the rule of three (3/n) is the
large-n approximation; computing it exactly also gives a usable bound when
k > 0. Standard library only.

Ported from Likewise 0.15.0 `binding_gate.py` (same author); the vocabulary of
outcomes is the engine's `GATE_OUTCOMES`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

GOVERNED = "governed"

# --- verdicts ---------------------------------------------------------------
BIND_AGREED = "bind_agreed"                    # bound, and on the record the oracle names
BIND_WRONG_PRECEDENT = "bind_wrong_precedent"  # bound, on the wrong record
FALSE_BIND = "false_bind"                      # bound where the oracle abstains
MISSED_BIND = "missed_bind"                    # abstained where the oracle binds
ABSTAIN_AGREED = "abstain_agreed"              # abstained, same cause
ABSTAIN_DIVERGED = "abstain_diverged"          # abstained, different cause
VERDICTS = (BIND_AGREED, BIND_WRONG_PRECEDENT, FALSE_BIND, MISSED_BIND,
            ABSTAIN_AGREED, ABSTAIN_DIVERGED)
FALSE_BINDS = frozenset({FALSE_BIND, BIND_WRONG_PRECEDENT})
BINDS = frozenset({BIND_AGREED, BIND_WRONG_PRECEDENT, FALSE_BIND})

ENGINE_ARM = "engine"
INDEPENDENT_ARM = "independent"


@dataclass(frozen=True)
class OracleCase:
    """One case and what the oracle says the gate should have done."""

    case_id: str
    expected: str                       # a gate outcome: governed | no_candidates | ...
    expected_controlling: str | None = None
    guard: bool = False                 # binding is wrong by construction
    arm: str = ENGINE_ARM               # who authored the expectation
    absolute: bool = False              # an absolute provision is engaged: higher floor

    def __post_init__(self):
        if self.expected == GOVERNED and not self.expected_controlling:
            raise ValueError(f"{self.case_id}: an expected bind must name its controlling record")
        if self.expected != GOVERNED and self.expected_controlling:
            raise ValueError(f"{self.case_id}: only an expected bind names a controlling record")
        if self.guard and self.expected == GOVERNED:
            raise ValueError(f"{self.case_id}: a guard cannot expect a bind")
        if self.arm not in (ENGINE_ARM, INDEPENDENT_ARM):
            raise ValueError(f"unknown arm {self.arm!r}")


@dataclass(frozen=True)
class Answer:
    """What the adjudicator under test did: an outcome and, if it bound, on what."""

    outcome: str
    controlling: str | None = None


def verdict_for(answer: Answer, oracle: OracleCase) -> str:
    bound = answer.outcome == GOVERNED
    should = oracle.expected == GOVERNED
    if bound and should:
        return BIND_AGREED if answer.controlling == oracle.expected_controlling else BIND_WRONG_PRECEDENT
    if bound and not should:
        return FALSE_BIND
    if not bound and should:
        return MISSED_BIND
    return ABSTAIN_AGREED if answer.outcome == oracle.expected else ABSTAIN_DIVERGED


# --- the bound ---------------------------------------------------------------
def clopper_pearson_upper(k: int, n: int, alpha: float = 0.05) -> float:
    """Exact one-sided upper confidence limit on a binomial rate."""
    if n <= 0:
        raise ValueError("no trials")
    if not (0 <= k <= n):
        raise ValueError(f"{k} failures in {n} trials is not possible")
    if not (0.0 < alpha < 1.0):
        raise ValueError("alpha must be in (0, 1)")
    if k == n:
        return 1.0

    lgn = math.lgamma(n + 1)

    def cdf(p: float) -> float:
        if p <= 0.0:
            return 1.0
        if p >= 1.0:
            return 1.0 if k >= n else 0.0
        lp, lq = math.log(p), math.log1p(-p)
        total = 0.0
        for i in range(k + 1):
            total += math.exp(lgn - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * lp + (n - i) * lq)
        return min(total, 1.0)

    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if cdf(mid) > alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def floor_for(target: float, alpha: float = 0.05) -> int:
    """The smallest n at which zero failures bounds the rate at `target`."""
    n = 1
    while clopper_pearson_upper(0, n, alpha) > target:
        n += 1
    return n


# --- the gate ----------------------------------------------------------------
@dataclass
class GateReport:
    n_cases: int = 0
    by_verdict: dict = field(default_factory=lambda: dict.fromkeys(VERDICTS, 0))
    by_arm: dict = field(default_factory=dict)
    guard_binds: list = field(default_factory=list)
    diverged: list = field(default_factory=list)
    verdict: str = "inconclusive"
    cause: str = ""
    detail: dict = field(default_factory=dict)

    @property
    def binds(self) -> int:
        return sum(self.by_verdict[v] for v in BINDS)

    @property
    def false_binds(self) -> int:
        return sum(self.by_verdict[v] for v in FALSE_BINDS)

    def false_bind_upper(self, alpha: float = 0.05):
        return None if self.binds == 0 else clopper_pearson_upper(self.false_binds, self.binds, alpha)

    @property
    def missed_bind_rate(self):
        opp = self.by_verdict[BIND_AGREED] + self.by_verdict[BIND_WRONG_PRECEDENT] + self.by_verdict[MISSED_BIND]
        return None if opp == 0 else self.by_verdict[MISSED_BIND] / opp

    def as_dict(self, alpha: float = 0.05) -> dict:
        ub = self.false_bind_upper(alpha)
        return {
            "verdict": self.verdict, "cause": self.cause,
            "n_cases": self.n_cases, "binds": self.binds, "false_binds": self.false_binds,
            "false_bind_upper_bound": None if ub is None else round(ub, 6),
            "missed_bind_rate": None if self.missed_bind_rate is None else round(self.missed_bind_rate, 6),
            "by_verdict": dict(self.by_verdict),
            "by_arm": {k: dict(v) for k, v in sorted(self.by_arm.items())},
            "guard_binds": self.guard_binds[:10],
            "abstention_divergences": self.diverged[:10],
            "detail": self.detail,
        }


def evaluate(cases, decide, *, min_binds: int = 300, min_binds_absolute: int = 3000,
             target_false_bind_rate: float = 0.01, alpha: float = 0.05,
             min_independent_binds: int = 1) -> GateReport:
    """Score `decide(oracle_case) -> Answer` over the oracle and apply the gate."""
    r = GateReport()
    absolute_present = False
    for oc in cases:
        ans = decide(oc)
        v = verdict_for(ans, oc)
        r.n_cases += 1
        r.by_verdict[v] += 1
        r.by_arm.setdefault(oc.arm, dict.fromkeys(VERDICTS, 0))[v] += 1
        absolute_present = absolute_present or oc.absolute
        if oc.guard and v in BINDS:
            r.guard_binds.append({"case_id": oc.case_id, "verdict": v, "expected": oc.expected,
                                  "got_controlling": ans.controlling})
        if v == ABSTAIN_DIVERGED:
            r.diverged.append({"case_id": oc.case_id, "expected": oc.expected, "got": ans.outcome})

    floor = min_binds_absolute if absolute_present else min_binds
    ind = r.by_arm.get(INDEPENDENT_ARM, {})
    ind_binds = sum(ind.get(v, 0) for v in BINDS)
    ind_false = sum(ind.get(v, 0) for v in FALSE_BINDS)
    ub = r.false_bind_upper(alpha)
    r.detail = {
        "min_binds_required": floor,
        "floor_reason": "an absolute provision is present" if absolute_present else "no absolute provision present",
        "target_false_bind_rate": target_false_bind_rate, "alpha": alpha,
        "independent_arm": {"binds": ind_binds, "false_binds": ind_false, "required": min_independent_binds,
                            "false_bind_upper_bound": None if ind_binds == 0 else
                            round(clopper_pearson_upper(ind_false, ind_binds, alpha), 6)},
        "abstention_divergence_count": len(r.diverged),
    }
    if r.guard_binds:
        r.verdict, r.cause = "fail", (f"{len(r.guard_binds)} guard bind(s). A guard is a case where binding "
                                      "is wrong by construction; one fails at any n.")
    elif r.binds < floor:
        r.verdict, r.cause = "inconclusive", (f"{r.binds} binds against a floor of {floor}. A false-bind rate "
                                              "of zero is satisfiable by never binding.")
    elif ind_binds < min_independent_binds:
        r.verdict, r.cause = "inconclusive", (
            f"{ind_binds} bind(s) on the independently authored arm against a required "
            f"{min_independent_binds}. The oracle is a second program written from the same rulebook; "
            "a shared misreading reads as perfect precision. A pass on a self-authored oracle is not a pass.")
    elif ub is not None and ub <= target_false_bind_rate:
        r.verdict, r.cause = "pass", (f"{r.false_binds} false bind(s) in {r.binds}; "
                                      f"{int((1 - alpha) * 100)}% upper bound {ub:.4f} <= {target_false_bind_rate}")
    else:
        r.verdict, r.cause = "fail", (f"{r.false_binds} false bind(s) in {r.binds}; "
                                      f"{int((1 - alpha) * 100)}% upper bound "
                                      f"{ub if ub is None else round(ub, 4)} > {target_false_bind_rate}")
    return r


def oracle_from_trace(case: dict, trace: dict, provisions: dict, arm: str = ENGINE_ARM) -> OracleCase | None:
    """The reference engine's trace as an oracle for one gate-reaching case.

    Returns None for a case the gate never saw (absolute short-circuit, null or
    declined docket before retrieval is impossible, consolidated member,
    control plane). E-distinguish cases are guard items: the corpus built them
    so that the only correct behaviour is to distinguish."""
    outcome = trace.get("gate_outcome")
    if outcome is None:
        return None
    return OracleCase(
        case_id=case["id"], expected=outcome,
        expected_controlling=trace["controlling"] if outcome == GOVERNED else None,
        guard=(case.get("category") == "E-distinguish" and outcome != GOVERNED),
        arm=arm,
        absolute=any(provisions[p].absolute for p in case.get("rules", []) if p in provisions),
    )
