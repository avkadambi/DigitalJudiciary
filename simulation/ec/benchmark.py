"""
Benchmark settings (benchmark build §3.1, §4.1): the H arms, their flags and
the seed guard.

    H0     arm A's rules -> the human reviewer; a rejection is final; audits
    HL     as H0 with the LLM peer reviewer instead of the human
    HEC    arm A's rules -> the EC gate (arm C semantics, internal office) -> the reviewer; audits
    HDJ    arm A's rules -> the reviewer -> the DJ hears appealed rejections and the
           corpus's own contests; holdings stay in the DJ store; audits
    HECDJ  arm A's rules -> the EC gate (arm D semantics) -> the reviewer -> the DJ
           hears EC escalations and appealed rejections; holdings return as glosses; audits

With no new flag nothing changes for arms A-D (every flag here is dropped from
run_config.json at its default).
"""

from __future__ import annotations

BENCH_ARMS = ("H0", "HL", "HEC", "HDJ", "HECDJ")
# Which registered arm's machinery each H arm reuses after its rules stage.
BASE_ARM = {"H0": "A", "HL": "A", "HEC": "C", "HDJ": "A", "HECDJ": "D"}
GATED = ("HEC", "HECDJ")
DJ_ARMS = ("HDJ", "HECDJ")
FORBIDDEN_SEED_RANGES = ((11, 53), (59, 73), (101, 113))
BENCHMARK_SEEDS = (211, 223, 227, 229, 233)
PILOT_SEED = 97
REVIEW_PROFILES = ("flat-edmundson", "braz-unprompted", "braz-prompted", "visibility", "crunch", "no-false-flags")
HARM_SCHEMES = ("rulebook", "tier", "flat", "steep")
NEW_FLAG_DEFAULTS = {"review_profile": "flat-edmundson", "audit": "25", "audit_detect": 0.8, "appeal_p": 0.30,
                     "harm_scheme": "rulebook", "corner_overlay": 0.0, "benchmark_params": None, "reviewer": None}


def add_args(ap) -> None:
    g = ap.add_argument_group("benchmark (old-school baseline vs EC and/or DJ)")
    g.add_argument("--review-profile", choices=REVIEW_PROFILES, default="flat-edmundson")
    g.add_argument("--audit", default="25", help="audits per company per quarter: 0, 25, 60 or all")
    g.add_argument("--audit-detect", type=float, default=0.8)
    g.add_argument("--appeal-p", type=float, default=0.30)
    g.add_argument("--harm-scheme", choices=HARM_SCHEMES, default="rulebook")
    g.add_argument("--corner-overlay", type=float, default=0.0, help="share of ai-agent arrivals given a corner (0 = off)")
    g.add_argument("--benchmark-params", default=None, help="default simulation/ec/config/benchmark_params.json")
    g.add_argument("--reviewer", default=None, help="llm:<provider>:<model> for arm HL (or roles.reviewer)")


def forbidden_seed(seed: int) -> bool:
    return any(lo <= int(seed) <= hi for lo, hi in FORBIDDEN_SEED_RANGES)


def check_seeds(arms: list, seeds: list) -> None:
    """B-12: no H arm on a registered, confirmatory or EC-07 seed."""
    if any(a in BENCH_ARMS for a in arms):
        bad = [s for s in seeds if forbidden_seed(s)]
        if bad:
            raise SystemExit(f"benchmark arms may not run on seeds {bad}: seeds 11-53, 59-73 and 101-113 are "
                             f"registered or consumed; use {PILOT_SEED} (pilot) or {list(BENCHMARK_SEEDS)}")


def audit_sample(v):
    return "all" if str(v) == "all" else int(v)
