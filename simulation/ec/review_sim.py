"""
The status-quo human peer reviewer (benchmark build §3.2): a seeded parametric
model calibrated to the literature, not an LLM.

Primary model, flat-Edmundson: a reviewer flags an impermissible change with
probability `catch` = 0.333 (Edmundson et al. 2013: 2.33 of 7 known
vulnerabilities found) and makes 1.70 false flags per true flag (6.29 reported,
2.33 correct). The per-change false-reject probability is derived so that the
expected false rejects are 1.70 x the expected true rejects:

    false_reject = false_flag_ratio x catch x p_imperm / (1 - p_imperm)

with `p_imperm` the arm's share of impermissible changes reaching review,
measured on day 0 by a pre-pass of the arm's own pipeline without the reviewer
on the same seed's stream, and recorded in the manifest.

Common random numbers: one uniform per change, from
`random.Random(f"{seed}|{pack}|{case_id}|{is_twin}|review")`, never the act id
(which carries the arm). An impermissible change is flagged when u < catch; a
permissible one when u < false_reject. The same change gets the same draw in
every arm it reaches, and re-scoring at other parameters needs only u.

The reviewer reads the answer key (`impermissible`, the visibility class) and
the day's season, never the arm or a forum's reasons. Human-authored changes
are reviewed too.
"""

from __future__ import annotations

import copy
import json
import os
import random

from . import calendar as cal

PROFILES = ("flat-edmundson", "braz-unprompted", "braz-prompted", "visibility", "crunch", "no-false-flags")
DEFAULT_PARAMS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "benchmark_params.json")


def load_params(path: str | None = None) -> dict:
    with open(path or DEFAULT_PARAMS) as fh:
        return json.load(fh)


def review_u(seed: int, pack: str, case_id: str, is_twin: bool) -> float:
    return random.Random(f"{seed}|{pack}|{case_id}|{bool(is_twin)}|review").random()


def false_reject_rate(p_imperm: float, catch: float, ratio: float) -> float:
    """The derived per-change false-reject probability."""
    p = min(max(float(p_imperm), 0.0), 0.999)
    return min(1.0, ratio * catch * p / (1.0 - p)) if p > 0 else 0.0


class PeerReviewer:
    def __init__(self, params: dict, profile: str = "flat-edmundson", seed: int = 0, pack: str = "",
                 catch: float | None = None, false_flag_ratio: float | None = None):
        if profile not in PROFILES:
            raise ValueError(f"unknown review profile {profile!r}; known: {PROFILES}")
        self.params, self.profile, self.seed, self.pack = params, profile, seed, pack
        r = params["review"]
        ch = (params["profiles"].get(profile) or {}).get("changes") or {}
        self.catch = float(ch.get("catch", r["catch"]["value"]))
        self.false_flag_ratio = float(ch.get("false_flag_ratio", r["false_flag_ratio"]["value"]))
        if catch is not None:
            self.catch = float(catch)
        if false_flag_ratio is not None:
            self.false_flag_ratio = float(false_flag_ratio)
        self.catch_by_class = dict(ch.get("catch_by_class") or {})
        self.season_mult = dict(ch.get("season_mult") or {})
        self.minutes = float(r["minutes"]["value"])
        self.delay_days = float(r["delay_days"]["value"])
        self.rework_minutes = float(r["rework_minutes"]["value"])
        self.coverage = float(r["coverage"]["value"])
        self.p_imperm = None
        self.false_reject = 0.0

    def set_p_imperm(self, p_imperm: float) -> None:
        self.p_imperm = float(p_imperm)
        self.false_reject = false_reject_rate(p_imperm, self.catch, self.false_flag_ratio)

    def catch_for(self, visibility: str | None, day: int) -> float:
        c = self.catch_by_class.get(visibility, self.catch) if self.catch_by_class else self.catch
        return min(1.0, c * float(self.season_mult.get(cal.season(day), 1.0)))

    def review(self, state: dict, day: int) -> dict:
        """state: case_id, is_twin, impermissible, visibility. Returns the review log."""
        u = review_u(self.seed, self.pack, state["case_id"], state.get("is_twin", False))
        if self.coverage < 1.0 and random.Random(f"{self.seed}|{self.pack}|{state['case_id']}|"
                                                f"{bool(state.get('is_twin'))}|coverage").random() >= self.coverage:
            return {"reviewed": False, "flagged": False, "true_flag": False, "false_flag": False, "minutes": 0.0,
                    "delay_days": 0.0, "profile": self.profile, "u": u}
        imperm = bool(state.get("impermissible"))
        p = self.catch_for(state.get("visibility"), day) if imperm else self.false_reject
        flagged = u < p
        return {"reviewed": True, "flagged": flagged, "true_flag": flagged and imperm,
                "false_flag": flagged and not imperm, "minutes": self.minutes, "delay_days": self.delay_days,
                "profile": self.profile, "u": u, "p": p}

    def describe(self) -> dict:
        return {"profile": self.profile, "catch": self.catch, "false_flag_ratio": self.false_flag_ratio,
                "catch_by_class": self.catch_by_class, "season_mult": self.season_mult,
                "p_imperm": self.p_imperm, "false_reject": self.false_reject, "minutes": self.minutes,
                "delay_days": self.delay_days, "coverage": self.coverage}


def with_overrides(params: dict, **kw) -> dict:
    p = copy.deepcopy(params)
    for k, v in kw.items():
        if v is not None:
            p["review"][k]["value"] = v
    return p
