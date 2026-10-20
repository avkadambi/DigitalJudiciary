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
                else:
                    act.stated_reason = driver
                    act.within_bound = True
            else:
                act.within_bound = True
                act.context = OUT_OF_CONTEXT
                if not admitted:
                    act.stated_reason = driver
            return act
        if admitted and rng.random() < self.table["p_depart_admitted"]:
            act.kind = "departure"
            act.within_bound = True
            if tier == "T3":
                act.context = rng.choice(sorted(gloss.contexts)) if gloss.contexts else OUT_OF_CONTEXT
            return act
        return act

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
