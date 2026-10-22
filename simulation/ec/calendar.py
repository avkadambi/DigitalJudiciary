"""
The shared working-day calendar (DESIGN §0).

An engine timestamp is ``ts = 1000 + day*DAY_TICKS + seq`` with ``seq < DAY_TICKS``,
so the engine's strict ``ts`` ordering and ``_displaces`` keep working within a
day, and every seed record (ts 1..200) sits below every arrival.

The engine writes record expiry as ``ts + 180``; the driver patches it to
``ts + 180*DAY_TICKS`` so an acceptance lasts 180 days. That patch is the only
engine-semantic overlay in the package and lives here.
"""

from __future__ import annotations

DAY_TICKS = 100
TS_BASE = 1000

D_BENCH = 3
K_CODIFY = 3
T3_SAMPLE_RATE = 0.10
TWIN_RATE = 0.25
CONFLICT_RATE = 0.02
LAMBDA = 6000 / 365
REGISTERED_SEEDS = [11, 13, 17, 19, 23]
# calibration run, executed 2026-10-20 (disclosed in the registration)
CONFIRMATORY_SEEDS = [59, 61, 67, 71, 73]
DAYS = 365
EXPIRY_DAYS = 180


def ts(day: int, seq: int) -> int:
    if not 0 <= seq < DAY_TICKS:
        raise ValueError(f"seq {seq} out of range 0..{DAY_TICKS - 1}")
    if day < 1:
        raise ValueError(f"day {day} < 1")
    return TS_BASE + day * DAY_TICKS + seq


def day_of(t: int) -> int:
    return (int(t) - TS_BASE) // DAY_TICKS


def seq_of(t: int) -> int:
    return (int(t) - TS_BASE) % DAY_TICKS


def patch_expiry(rec):
    """Rewrite ``rec.expiry`` from the engine's ``ts + 180`` to ``ts + 180*DAY_TICKS``.
    Leaves interpretive records (expiry None) alone. Returns the record."""
    if getattr(rec, "expiry", None) is not None:
        rec.expiry = rec.ts + EXPIRY_DAYS * DAY_TICKS
    return rec
