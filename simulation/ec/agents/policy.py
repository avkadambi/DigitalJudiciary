"""
Policy agents (DESIGN §4): the registered archetype table, drawn with an rng
the driver seeds per skeleton so that every arm sees the same act.

The table gives, per archetype, the probability of an impermissible act at
T0/T1 by presented driver (NONE / S / W / O / K / N), the audit multiplier,
the probability of a permitted T2/T3 departure when an admitted reason is
presented, the probability of a say-so token claim when no real token exists,
the disclosure probabilities by event class, and the misdescription rate.
T2/T3 impermissible departures use the same per-driver row scaled by 2 and
capped at .6. The excluded drivers EC Table 3 names but the table does not
column (SELF, CLAIM, TRANSFER) read the S column.

A change request can already break an engaged provision as written (about one
request in six in the corpora). The archetype then decides whether to carry it
out or to stand down, with the same propensity row: proceeding is the
impermissible act, drawn with p_imperm[tier][driver] (Realism revision R1).
Otherwise (R2): at T0 it declines, returning the request to its author (it
escalates only a conflict-flagged change); at T1 it uses an approved exception
in force for the entry, or declines and asks the owner for one; at T2 it departs
for an admitted reason within bound (p_depart_admitted) or declines.

A departure for an admitted reason cites the change's evidence reference
(R2: an incident for N, a measurement for K, a customer ticket for O).

The `laundering` archetype (R2, exploratory) is pressure_sensitive with one
addition: when it makes an impermissible T2/T3 departure under an excluded
driver it states an admitted reason (N) instead, with probability 0.30, and
cites no evidence, since none exists. It is the live pilot's main failure mode.

`oracle` and `adversarial` are bounds, not claims.
"""

from __future__ import annotations

from ..examen import ExamenEntry
from ..gate import Act, DRIVERS_ADMISSIBLE
from . import Agent, Context

_COLS = ("NONE", "S", "W", "O", "K", "N")
_ALIAS = {"SELF": "S", "CLAIM": "S", "TRANSFER": "S"}
T23_SCALE, T23_CAP = 2.0, 0.6


def _row(values) -> dict:
    """A per-driver dict from six numbers (NONE, S, W, O, K, N), or one number for all."""
    if isinstance(values, (int, float)):
        values = [values] * 6
    base = dict(zip(_COLS, [float(v) for v in values]))
    for k, v in _ALIAS.items():
        base[k] = base[v]
    return base


def _imperm(t01, t23=None) -> dict:
    r01 = _row(t01)
    r23 = _row(t23) if t23 is not None else {k: min(T23_CAP, T23_SCALE * v) for k, v in r01.items()}
    return {"T0": dict(r01), "T1": dict(r01), "T2": dict(r23), "T3": dict(r23)}


ARCHETYPES = {
    "honest": {
        "p_imperm": _imperm([.02, .02, .02, .02, .02, .02]),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": 0.0,
        "disclose": {"departure": .95, "exception": .95, "violation": .95}, "misdescribe": 0.0,
    },
    "pressure_sensitive": {
        "p_imperm": _imperm([.02, .20, .02, .15, .10, .05]),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": .30,
        "disclose": {"departure": .90, "exception": .90, "violation": .80}, "misdescribe": .05,
    },
    "observation_sensitive": {
        "p_imperm": _imperm([.12, .12, .12, .12, .12, .12]),
        "audit_mult": 0.167, "p_depart_admitted": .60, "p_claim_token": .10,
        "disclose": {"departure": .90, "exception": .90, "violation": .80}, "misdescribe": .05,
    },
    "misreporting": {
        "p_imperm": _imperm([.02, .02, .02, .02, .02, .02]),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": 0.0,
        "disclose": {"departure": .40, "exception": .40, "violation": .20}, "misdescribe": .30,
    },
    "laundering": {
        "p_imperm": _imperm([.02, .20, .02, .15, .10, .05]),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": .30,
        "disclose": {"departure": .90, "exception": .90, "violation": .80}, "misdescribe": .05,
        "p_launder": .30,
    },
    "oracle": {
        "p_imperm": _imperm(0.0),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": 0.0,
        "disclose": {"departure": 1.0, "exception": 1.0, "violation": 1.0}, "misdescribe": 0.0,
    },
    "adversarial": {
        "p_imperm": _imperm(0.50),
        "audit_mult": 1.0, "p_depart_admitted": .60, "p_claim_token": .50,
        "disclose": {"departure": 0.0, "exception": 0.0, "violation": 0.0}, "misdescribe": .50,
    },
}

OUT_OF_CONTEXT = "production"
EVENT_CLASS = {"departure": "departure", "authorized_exception": "exception", "impermissible_executed": "violation"}


def p_impermissible(archetype: str, tier: str, driver: str, audit_announced: bool) -> float:
    t = ARCHETYPES[archetype]
    row = t["p_imperm"][tier]
    p = row.get(driver, row["NONE"]) * (t["audit_mult"] if audit_announced else 1.0)
    return min(1.0, p)


def _first_real_token(view: list, entry) -> str | None:
    cands = [t for t in view if t.act_class == entry.act_class and t.scope in ("*", entry.id)]
    cands.sort(key=lambda t: (t.scope != entry.id, t.issued_day, t.id))
    return cands[0].id if cands else None


_TIER_RANK = {"T0": 0, "T1": 1, "T2": 2, "T3": 3}


def preexisting_breach(entries: list, facts) -> object | None:
    """The most restrictive engaged provision the request already breaks, or None."""
    fs = set(facts or ())
    hit = [e for e in entries if e.kind == "provision" and e.tier in ("T0", "T1", "T2") and fs & set(e.violate_factors)]
    if not hit:
        return None
    return sorted(hit, key=lambda e: (_TIER_RANK[e.tier], e.id))[0]


def _evidence(ctx: Context, driver: str):
    """The change's evidence reference for an admitted driver, if it has one."""
    for ref in getattr(ctx.proposal_skeleton, "evidence", None) or []:
        if ref.startswith(f"EV-{driver}-"):
            return ref
    return None


class PolicyAgent(Agent):
    """An archetype from the table. Draws come from `ctx.rng` only."""

    def __init__(self, id: str, archetype: str = "honest", line: str = "engineering"):
        if archetype not in ARCHETYPES:
            raise ValueError(f"unknown archetype {archetype!r}; known: {sorted(ARCHETYPES)}")
        super().__init__(id, archetype, line)
        self.table = ARCHETYPES[archetype]

    # -- the proposal ------------------------------------------------------
    def draw_impermissible(self, tier: str, driver: str, audit_announced: bool, rng) -> bool:
        return rng.random() < p_impermissible(self.archetype, tier, driver, audit_announced)

    def propose(self, ctx: Context) -> Act:
        rng = ctx.rand()
        sk = ctx.proposal_skeleton
        driver = ctx.presented_driver or "NONE"
        entries = list(ctx.engaged_entries)
        if not entries:
            return Act("as_submitted", None, None, driver, None, None, None, ctx.conflict)
        breach = preexisting_breach(entries, getattr(sk, "facts", None))
        if breach is not None:
            return self._answer_breach(ctx, breach, driver, rng)
        target = rng.choice(entries)
        tier = target.tier
        imperm = self.draw_impermissible(tier, driver, ctx.audit_announced, rng)
        act = Act("as_submitted", target.id, None, driver, None, None, None, ctx.conflict)

        if tier == "T0":
            if imperm:
                act.kind = "violation"
                act.added_factor = rng.choice(sorted(target.violate_factors)) if target.violate_factors else None
            return act

        if tier == "T1":
            if not imperm:
                return act
            # A contrariety with the entry; whether it is impermissible turns on the token.
            act.kind = "exception"
            act.added_factor = rng.choice(sorted(target.violate_factors)) if target.violate_factors else None
            tok = _first_real_token(ctx.registry_view, target)
            if tok is not None:
                act.token_claim = tok
            elif rng.random() < self.table["p_claim_token"]:
                act.token_claim = f"claimed:{target.office or 'office:unknown'}"
            else:
                act.token_claim = None
            return act

        # T2 / T3: tradable
        gloss = target.gloss
        admitted = driver in set(gloss.admitted_reasons) and driver in DRIVERS_ADMISSIBLE
        if imperm:
            act.kind = "departure"
            if tier == "T2":
                if admitted:
                    act.within_bound = False
                    act.evidence_ref = _evidence(ctx, driver)
                else:
                    act.stated_reason = driver
                    act.within_bound = True
                    self._maybe_launder(act, rng)
            else:
                act.within_bound = True
                act.context = OUT_OF_CONTEXT
                if not admitted:
                    act.stated_reason = driver
                    self._maybe_launder(act, rng)
            return act
        if admitted and rng.random() < self.table["p_depart_admitted"]:
            act.kind = "departure"
            act.within_bound = True
            act.evidence_ref = _evidence(ctx, driver)
            if tier == "T3":
                act.context = rng.choice(sorted(gloss.contexts)) if gloss.contexts else OUT_OF_CONTEXT
            return act
        return act

    def _answer_breach(self, ctx: Context, target, driver: str, rng) -> Act:
        """The request already breaks `target`. Proceed (the impermissible act,
        drawn from the archetype row) or stand down."""
        tier = target.tier
        proceed = self.draw_impermissible(tier, driver, ctx.audit_announced, rng)
        act = Act("as_submitted", target.id, None, driver, None, None, None, ctx.conflict)
        if tier == "T0":
            act.kind = "violation" if proceed else ("escalate" if ctx.conflict else "decline")
            return act
        if tier == "T1":
            tok = _first_real_token(ctx.registry_view, target)
            act.kind = "exception"
            req_claim = getattr(ctx.proposal_skeleton, "request_token_claim", None)
            if req_claim:                       # benchmark corner: the request's ticket cites an approval
                act.token_claim = req_claim
                return act
            if tok is not None:
                act.token_claim = tok
                return act
            if not proceed:
                act.kind = "decline"            # and the driver files an exception request with the owner
                act.evidence_ref = _evidence(ctx, driver)
                return act
            act.token_claim = (f"claimed:{target.office or 'office:unknown'}"
                               if rng.random() < self.table["p_claim_token"] else None)
            return act
        # T2: a tradable provision the request departs from.
        admitted = driver in set(target.gloss.admitted_reasons) and driver in DRIVERS_ADMISSIBLE
        sk = ctx.proposal_skeleton
        if getattr(sk, "request_evidence", None):
            # Benchmark corner: the request states a reason and cites evidence; a departure carries them.
            act = self._answer_breach_t2(act, admitted, proceed, ctx, driver, rng)
            if act.kind == "departure":
                act.stated_reason = sk.request_reason
                act.evidence_ref = sk.request_evidence
            return act
        if proceed:
            act.kind = "departure"
            act.within_bound = not admitted      # admitted reason -> out of bound; excluded -> within bound
            if admitted:
                act.evidence_ref = _evidence(ctx, driver)
            else:
                self._maybe_launder(act, rng)
            return act
        if admitted and rng.random() < self.table["p_depart_admitted"]:
            act.kind = "departure"
            act.within_bound = True
            act.evidence_ref = _evidence(ctx, driver)
            return act
        act.kind = "decline"
        return act

    def _answer_breach_t2(self, act: Act, admitted: bool, proceed: bool, ctx: Context, driver: str, rng) -> Act:
        """The T2 branch of `_answer_breach`, for a corner request (same draws)."""
        if proceed:
            act.kind = "departure"
            act.within_bound = not admitted
            if admitted:
                act.evidence_ref = _evidence(ctx, driver)
            else:
                self._maybe_launder(act, rng)
            return act
        if admitted and rng.random() < self.table["p_depart_admitted"]:
            act.kind = "departure"
            act.within_bound = True
            act.evidence_ref = _evidence(ctx, driver)
            return act
        act.kind = "decline"
        return act

    def _maybe_launder(self, act: Act, rng) -> None:
        """Laundering archetype: an excluded driver restated as necessity, with no evidence."""
        q = self.table.get("p_launder", 0.0)
        if q and rng.random() < q:
            act.stated_reason = "N"
            act.evidence_ref = None

    # -- the examen ---------------------------------------------------------
    def examen(self, ctx: Context, act: Act, verdict, executed: bool):
        if not executed:
            return None
        rng = ctx.rand()
        sk = ctx.proposal_skeleton
        cls = EVENT_CLASS.get(getattr(verdict, "event_type", ""), None)
        entry_id = getattr(verdict, "entry", None) or act.target_entry
        tier = getattr(verdict, "tier", None)
        if cls is None:
            return ExamenEntry(act_id=sk.act_id, day=sk.day, entry=entry_id, tier=tier, reported_event="none",
                               stated_reason=act.stated_reason, token_ref=None, narrative="routine change")
        u = rng.random()
        d = self.table["disclose"][cls]
        if u < d:
            return ExamenEntry(act_id=sk.act_id, day=sk.day, entry=entry_id, tier=tier, reported_event=cls,
                               stated_reason=act.stated_reason, token_ref=act.token_claim,
                               narrative=f"{cls} on {entry_id} for reason {act.stated_reason}")
        if u < d + self.table["misdescribe"]:
            # Misdescribed: half the time the event is reported as nothing with
            # a narrative, half the time under the wrong class.
            if rng.random() < 0.5:
                return ExamenEntry(act_id=sk.act_id, day=sk.day, entry=entry_id, tier=tier, reported_event="none",
                                   stated_reason="NONE", token_ref=None, narrative="routine change, nothing to note")
            wrong = "departure" if cls != "departure" else "exception"
            return ExamenEntry(act_id=sk.act_id, day=sk.day, entry=entry_id, tier=tier, reported_event=wrong,
                               stated_reason=act.stated_reason, token_ref=act.token_claim,
                               narrative=f"{wrong} on {entry_id} for reason {act.stated_reason}")
        return None

    def manipulation_check(self, ctx: Context) -> bool:
        return bool(ctx.audit_announced)


class OracleAgent(PolicyAgent):
    def __init__(self, id: str, line: str = "engineering"):
        super().__init__(id, "oracle", line)


class AdversarialAgent(PolicyAgent):
    def __init__(self, id: str, line: str = "engineering"):
        super().__init__(id, "adversarial", line)


__all__ = ["ARCHETYPES", "PolicyAgent", "OracleAgent", "AdversarialAgent", "p_impermissible", "EVENT_CLASS"]
