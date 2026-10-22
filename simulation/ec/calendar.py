"""
The shared business calendar (DESIGN §0).

A simulated year is one fiscal year of a mid-size US software company: calendar
year 2027, Monday to Friday, less ten observed holidays (nine company holidays and
the New Year 2028 holiday observed on Friday 31 December), which gives 251 working
days. Day ``d`` (1..DAYS) is the d-th working day. Weekends and holidays carry
no arrivals and do not count toward any interval measured in days (bench delay,
token life, record expiry): every interval in the package is in working days.

The calendar also carries the three seasonal features a normal company's change
process has (Realism revision R1, `prereg/REALISM_REVIEW.md`):

  * hard change freezes (US Thanksgiving week, Wednesday to Monday, and the
    year-end lock from 20 December), when only emergency changes arrive
    (``FREEZE_ARRIVAL_WEIGHT`` of a normal day's arrivals). The year opens on
    the first working day after the previous year's lock, so day 1 is normal;
  * a monthly release train, released on the last working day of each month
    (17 December in December, before the year-end lock), with a crunch over the
    last ``RELEASE_CRUNCH_DAYS`` working days up to and including release day;
  * a quarter-end crunch over the last ``QUARTER_CRUNCH_DAYS`` working days of
    March, June, September and December, outside the release crunch.

`season(day)` names the regime of a working day; `stream.overlay` reads it to
draw the presented driver and `stream.partition_days` reads `arrival_weight`.

An engine timestamp is ``ts = 1000 + day*DAY_TICKS + seq`` with ``seq < DAY_TICKS``,
so the engine's strict ``ts`` ordering and ``_displaces`` keep working within a
day, and every seed record (ts 1..200) sits below every arrival.

The engine writes record expiry as ``ts + 180``; the driver patches it to
``ts + EXPIRY_DAYS*DAY_TICKS`` so an acceptance lasts 124 working days (about
180 calendar days). That patch is the only engine-semantic overlay in the
package and lives here.
"""

from __future__ import annotations

import datetime as _dt

DAY_TICKS = 100
TS_BASE = 1000

YEAR = 2027
# Nine company paid holidays (BLS: private-industry average 8 paid holidays, 2017; one added for the
# day after Thanksgiving, which most US employers give). Observed dates for 2027.
HOLIDAYS = (
    _dt.date(2027, 1, 1),    # New Year's Day
    _dt.date(2027, 1, 18),   # Martin Luther King Jr. Day
    _dt.date(2027, 5, 31),   # Memorial Day
    _dt.date(2027, 6, 18),   # Juneteenth (observed; 19 June is a Saturday)
    _dt.date(2027, 7, 5),    # Independence Day (observed; 4 July is a Sunday)
    _dt.date(2027, 9, 6),    # Labor Day
    _dt.date(2027, 11, 25),  # Thanksgiving
    _dt.date(2027, 11, 26),  # Day after Thanksgiving
    _dt.date(2027, 12, 24),  # Christmas (observed; 25 December is a Saturday)
    _dt.date(2027, 12, 31),  # New Year's Day 2028 (observed; 1 January 2028 is a Saturday; 5 U.S.C. 6103(b)) (R2)
)
# Hard change freezes, inclusive calendar ranges (GitLab handbook, production change locks:
# Thanksgiving week, and 20 December to 5 January; the January tail belongs to the previous
# year's lock, so the simulated year opens on a normal working day).
FREEZES = (
    (_dt.date(2027, 11, 24), _dt.date(2027, 11, 29)),
    (_dt.date(2027, 12, 20), _dt.date(2027, 12, 31)),
)
FREEZE_ARRIVAL_WEIGHT = 0.15
RELEASE_CRUNCH_DAYS = 5
QUARTER_CRUNCH_DAYS = 10


def _working_dates() -> list:
    d, out = _dt.date(YEAR, 1, 1), []
    hol = set(HOLIDAYS)
    while d.year == YEAR:
        if d.weekday() < 5 and d not in hol:
            out.append(d)
        d += _dt.timedelta(days=1)
    return out


WORKING_DATES = _working_dates()          # index 0 is working day 1
DAYS = len(WORKING_DATES)                 # 251


def date_of(day: int) -> _dt.date:
    if not 1 <= day <= DAYS:
        raise ValueError(f"day {day} outside 1..{DAYS}")
    return WORKING_DATES[day - 1]


def _in_freeze(d: _dt.date) -> bool:
    return any(a <= d <= b for a, b in FREEZES)


FREEZE_DAYS = frozenset(i + 1 for i, d in enumerate(WORKING_DATES) if _in_freeze(d))


def _release_days() -> list:
    """The last non-freeze working day of each month."""
    out = []
    for m in range(1, 13):
        cands = [i + 1 for i, d in enumerate(WORKING_DATES) if d.month == m and (i + 1) not in FREEZE_DAYS]
        if cands:
            out.append(max(cands))
    return out


RELEASE_DAYS = tuple(_release_days())
RELEASE_CRUNCH = frozenset(d for r in RELEASE_DAYS for d in range(r - RELEASE_CRUNCH_DAYS + 1, r + 1)
                           if d not in FREEZE_DAYS)
QUARTER_CRUNCH = frozenset(
    d for r in RELEASE_DAYS if date_of(r).month in (3, 6, 9, 12)
    for d in range(r - QUARTER_CRUNCH_DAYS + 1, r + 1)
    if d not in FREEZE_DAYS and d not in RELEASE_CRUNCH)


def season(day: int) -> str:
    """'freeze' | 'release_crunch' | 'quarter_crunch' | 'normal'."""
    if day in FREEZE_DAYS:
        return "freeze"
    if day in RELEASE_CRUNCH:
        return "release_crunch"
    if day in QUARTER_CRUNCH:
        return "quarter_crunch"
    return "normal"


def arrival_weight(day: int) -> float:
    return FREEZE_ARRIVAL_WEIGHT if day in FREEZE_DAYS else 1.0


D_BENCH = 3                  # working days from filing to hearing
K_CODIFY = 3
T3_SAMPLE_RATE = 0.10
TWIN_RATE = 0.25
CONFLICT_RATE = 0.02
CORPUS_SIZE = 6000
LAMBDA = CORPUS_SIZE / sum(arrival_weight(d) for d in range(1, DAYS + 1))   # arrivals on a normal day
REGISTERED_SEEDS = [11, 13, 17, 19, 23]
# calibration run, executed 2026-10-20 (disclosed in the registration)
CONFIRMATORY_SEEDS = [59, 61, 67, 71, 73]
EXPIRY_DAYS = 124            # working days, about 180 calendar days


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
    """Rewrite ``rec.expiry`` from the engine's ``ts + 180`` to ``ts + EXPIRY_DAYS*DAY_TICKS``.
    Leaves interpretive records (expiry None) alone. Returns the record."""
    if getattr(rec, "expiry", None) is not None:
        rec.expiry = rec.ts + EXPIRY_DAYS * DAY_TICKS
    return rec
