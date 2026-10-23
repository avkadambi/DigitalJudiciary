"""
Random audits after the fact (benchmark build §3.6), every H arm.

Each quarter's audit runs on the last working day of the calendar quarter and
looks at changes executed in that quarter. Selection uses common random
numbers: a change is selected when sha256(f"{seed}|{pack}|{case_id}|{is_twin}|audit")
as a fraction of 2**256 falls under the quarter's rate, rate = sample /
(the quarter's arrivals in the stream), which is the same for every arm; it is
audited only if it executed. `all` audits every executed change. An audited
impermissible change is found with probability `detect` (its own CRN draw).
A found violation gets `detected_by_audit` and `exposure_days` = audit day -
execution day; an undetected executed violation carries exposure to the end of
the run. Nothing is rolled back.
"""

from __future__ import annotations

import hashlib

from . import calendar as cal


def _u(key: str) -> float:
    return int(hashlib.sha256(key.encode("utf-8")).hexdigest(), 16) / float(2 ** 256)


def quarter_of(day: int) -> int:
    return (cal.date_of(day).month - 1) // 3 + 1


def quarter_end_days(days: int = cal.DAYS) -> dict:
    """{quarter: last working day of that quarter} within the first `days` working days."""
    out = {}
    for d in range(1, days + 1):
        out[quarter_of(d)] = d
    return out


class Auditor:
    def __init__(self, sample, detect: float, seed: int, pack: str, days: int, arrivals_by_quarter: dict):
        self.sample = sample                     # int per quarter, or "all"
        self.detect = float(detect)
        self.seed, self.pack, self.days = seed, pack, days
        self.ends = quarter_end_days(days)
        self.arrivals = dict(arrivals_by_quarter)

    def rate(self, quarter: int) -> float:
        if self.sample == "all":
            return 1.0
        n = self.arrivals.get(quarter, 0)
        return min(1.0, float(self.sample) / n) if n else 0.0

    def selected(self, case_id: str, is_twin: bool, quarter: int) -> bool:
        return _u(f"{self.seed}|{self.pack}|{case_id}|{bool(is_twin)}|audit") < self.rate(quarter)

    def detected(self, case_id: str, is_twin: bool) -> bool:
        return _u(f"{self.seed}|{self.pack}|{case_id}|{bool(is_twin)}|audit-detect") < self.detect

    def is_audit_day(self, day: int) -> bool:
        return day in self.ends.values()

    def run(self, executed: list, day: int) -> list:
        """executed: dicts (case_id, is_twin, day_executed, impermissible) executed in this
        quarter. Returns one audit record per selected change."""
        q = quarter_of(day)
        out = []
        for x in executed:
            if quarter_of(x["day_executed"]) != q or not self.selected(x["case_id"], x["is_twin"], q):
                continue
            found = bool(x["impermissible"]) and self.detected(x["case_id"], x["is_twin"])
            out.append({"case_id": x["case_id"], "is_twin": x["is_twin"], "audit_day": day, "quarter": q,
                        "found": found, "exposure_days": (day - x["day_executed"]) if found else None})
        return out

    def describe(self) -> dict:
        return {"sample_per_quarter": self.sample, "detect": self.detect, "quarter_end_days": self.ends,
                "arrivals_by_quarter": self.arrivals}
