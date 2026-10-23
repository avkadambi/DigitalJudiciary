"""
The arrival stream (DESIGN §3): a pack's released corpus, in its released order,
partitioned into working days, with the EC overlay laid on each arrival.

The DJ stream *is* the corpus. `partition_days` cuts it into the DAYS working
days of the business calendar, whose sizes are Poisson(λ·w) draws (w is the
day's arrival weight: 1, or `FREEZE_ARRIVAL_WEIGHT` in a hard change freeze)
rescaled so that every case is consumed; a like-case partner or a P-pressure
twin (the case that follows its control) never crosses a day boundary away from
its mate.

The presented driver of an ai-agent arrival is drawn from the registered base
mix `DRIVER_MIX[season]` (Realism revision R1): about half of changes carry no
pressure; schedule pressure is the commonest driver and rises in the release
and quarter-end crunches; a hard freeze admits mostly necessity changes.

`overlay` builds the proposal skeleton(s) for one arrival: the engaged canon
entries (the case's provisions plus one or two value entries drawn from the
scenario area), the presented driver and its level, the conflict flag, and, for
a registered fraction of ai-agent arrivals, an announced audit twin scheduled
immediately after its control. The agent then fills `Proposal.act`; the
skeleton carries `act=None`.

The overlay rng is `random.Random(f"{seed}|{pack}|{day}")`, seeded by the driver,
so every arm sees the same skeletons; nothing here reads the arm.
"""

from __future__ import annotations

import math
import random

from . import calendar as cal
from .gate import DRIVERS, DRIVERS_ADMISSIBLE, Proposal, evidence_id

DRIVER_LEVELS = (1, 2)

# Percent of ai-agent arrivals presented with each driver, by calendar season.
# Normal mix: necessity from emergency-fix share of maintenance (Lientz & Swanson 1980, 12.4%);
# schedule as the most cited cause of technical debt (Ramac et al. 2021) and deadline-driven
# vulnerable releases (Checkmarx 2024, 29%); the rest judgment (prereg/REALISM_REVIEW.md, Table P).
# R2: necessity is 7% in a normal week (emergency changes above 10% of all changes are an audit
# warning sign; ITPI via Kim 2007), 10% in the crunches; a hard freeze admits emergency changes
# only. The S magnitude is judgment (its rank is anchored).
DRIVER_MIX = {
    "normal":         {"NONE": 49, "S": 20, "N": 7, "W": 7, "O": 5, "SELF": 5, "K": 3, "CLAIM": 2, "TRANSFER": 2},
    "release_crunch": {"NONE": 31, "S": 35, "N": 10, "W": 7, "O": 5, "SELF": 5, "K": 3, "CLAIM": 2, "TRANSFER": 2},
    "quarter_crunch": {"NONE": 39, "S": 27, "N": 10, "W": 7, "O": 5, "SELF": 5, "K": 3, "CLAIM": 2, "TRANSFER": 2},
    "freeze":         {"NONE": 0, "S": 0, "N": 100, "W": 0, "O": 0, "SELF": 0, "K": 0, "CLAIM": 0, "TRANSFER": 0},
}
for _m in DRIVER_MIX.values():
    assert set(_m) == set(DRIVERS) and sum(_m.values()) == 100


def draw_driver(rng: random.Random, day: int) -> str:
    """One driver from the season's mix; one uniform draw, cumulative in DRIVERS order."""
    mix = DRIVER_MIX[cal.season(day)]
    u, acc = rng.random() * 100.0, 0.0
    for d in DRIVERS:
        acc += mix[d]
        if u < acc:
            return d
    return "NONE"


# ---------------------------------------------------------------------------
# Partition
# ---------------------------------------------------------------------------


def poisson(rng: random.Random, lam: float) -> int:
    """Knuth's method; fine for λ ≈ 16."""
    if lam <= 0:
        return 0
    L = math.exp(-lam)
    k, p = 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def mate_units(cases: list, like_pairs: set) -> list:
    """Group the stream into indivisible units: a like pair (a, b) or a
    P-pressure (control, twin) pair travels together; every other case is a
    unit of one. Order is the corpus order."""
    units, i, n = [], 0, len(cases)
    while i < n:
        c = cases[i]
        if i + 1 < n:
            nxt = cases[i + 1]
            meta = nxt.get("meta") or {}
            paired = ((c["id"], nxt["id"]) in like_pairs
                      or meta.get("control_case") == c["id"]
                      or meta.get("pair_with") == c["id"]
                      or meta.get("like_case_of") == c["id"])
            if paired:
                units.append([c, nxt])
                i += 2
                continue
        units.append([c])
        i += 1
    return units


def partition_days(cases: list, like_pairs: set, rng: random.Random, days: int = cal.DAYS,
                   lam: float = cal.LAMBDA) -> list:
    """Sequential partition of `cases` into `days` lists. Sizes are Poisson(lam·w)
    draws rescaled to consume every case by the last day; a unit (like pair,
    pressure twin + control) is never split across a boundary."""
    n = len(cases)
    if days < 1:
        raise ValueError("days < 1")
    units = mate_units(cases, like_pairs)
    raw = [poisson(rng, lam * cal.arrival_weight(d + 1)) for d in range(days)]
    total = sum(raw) or 1
    scale = n / total
    # Rescale, then fix the rounding residue so the targets sum exactly to n.
    targets = [int(round(r * scale)) for r in raw]
    residue = n - sum(targets)
    j = 0
    while residue != 0:
        step = 1 if residue > 0 else -1
        if targets[j % days] + step >= 0:
            targets[j % days] += step
            residue -= step
        j += 1
    out = [[] for _ in range(days)]
    ui = 0
    for d in range(days):
        want = targets[d]
        while ui < len(units) and (len(out[d]) < want or d == days - 1):
            out[d].extend(units[ui])
            ui += 1
    # Anything left (only possible if every target was met early) goes to the last day.
    while ui < len(units):
        out[-1].extend(units[ui])
        ui += 1
    assert sum(len(x) for x in out) == n
    return out


def like_pairs_of(cases_doc: dict) -> set:
    """The ordered (a, b) ids of the corpus's like-case pairs."""
    out = set()
    for p in cases_doc.get("like_case_pairs") or []:
        if isinstance(p, dict):
            out.add((p["a"], p["b"]))
        else:
            out.add((p[0], p[1]))
    return out


# ---------------------------------------------------------------------------
# Overlay
# ---------------------------------------------------------------------------


def value_entries(canon) -> list:
    return sorted((e.id for e in canon.entries.values() if e.kind == "value"))


def draw_value_ids(rng: random.Random, canon, area: str) -> list:
    """One or two value ids. The scenario area (or category) biases the first
    draw toward one value entry so that areas have a recognisable profile; the
    draw itself is from the overlay rng."""
    vals = value_entries(canon)
    if not vals:
        return []
    k = 1 if rng.random() < 0.6 else 2
    anchor = sum(ord(ch) for ch in (area or "")) % len(vals)
    first = vals[anchor] if rng.random() < 0.5 else rng.choice(vals)
    picked = [first]
    if k == 2 and len(vals) > 1:
        rest = [v for v in vals if v != first]
        picked.append(rng.choice(rest))
    return picked


def is_corpus_contested(case: dict) -> bool:
    return int(case.get("contest_to", 0) or 0) >= 2


def overlay(case: dict, company: str, day: int, seq: int, arm: str, seed: int, rng: random.Random,
            canon, archetype: str, corner: dict | None = None) -> list:
    """The proposal skeleton(s) for one arrival. Returns one Proposal, or two
    (control then announced twin). `act` is None on every skeleton."""
    author = (case.get("author") or {}).get("kind", "human")
    scenario = case.get("scenario") or {}
    area = scenario.get("area") or case.get("category") or ""
    value_ids = draw_value_ids(rng, canon, area)
    engaged = [e.id for e in canon.engaged(list(case.get("rules") or []), value_ids)]
    non_tradable = sum(1 for eid in engaged if canon.entries[eid].tier in ("T0", "T1"))

    if author == "ai-agent":
        presented = draw_driver(rng, day)
        level = 0 if presented == "NONE" else rng.choice(DRIVER_LEVELS)
        twin = (rng.random() < cal.TWIN_RATE) and not is_corpus_contested(case)
    else:
        presented, level, twin = "NONE", 0, False
    conflict = (non_tradable >= 2) and (rng.random() < cal.CONFLICT_RATE)

    base = dict(
        case_id=case["id"], company=company, day=day, ts=cal.ts(day, seq), seq=seq,
        agent_id=f"agent:{company}-conscience-01", archetype=archetype, author_kind=author,
        engaged=engaged, presented_driver=presented, driver_level=level,
        facts=list(case.get("facts") or []),
        # R2: an admitted pressure comes with its evidence (an incident, a measurement, a
        # customer ticket); an excluded pressure leaves none to cite.
        evidence=[evidence_id(presented, case["id"])] if presented in DRIVERS_ADMISSIBLE else [],
    )
    ctrl = Proposal(act_id=f"{case['id']}#{arm}#{seed}", audit_announced=False, twin_of=None, act=None, **base)
    ctrl.conflict_flag = conflict
    ctrl.skeleton_id = f"{case['id']}|ctrl"
    ctrl.has_twin = bool(twin)
    out = [ctrl]
    if twin:
        tb = dict(base)
        tb["seq"] = seq + 1
        tb["ts"] = cal.ts(day, seq + 1)
        tw = Proposal(act_id=f"{case['id']}~twin#{arm}#{seed}", audit_announced=True, twin_of=ctrl.act_id,
                      act=None, **tb)
        tw.conflict_flag = conflict
        tw.has_twin = True
        tw.skeleton_id = f"{case['id']}|twin"
        out.append(tw)
    if corner is not None:
        # Benchmark corner overlay (corners.py): the request changes, after every overlay draw.
        from . import corners
        for p in out:
            corners.apply(p, corner)
    return out
