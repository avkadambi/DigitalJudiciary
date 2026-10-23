"""
Benchmark analysis (benchmark build §3.9): paired bootstrap intervals for the
draft hypotheses HR1-HR5 over units (company, seed), and `benchmark.md`.

    python3 simulation/ec/analyze_benchmark.py <results_root> [--out DIR] [--resamples 2000]

    HR1 wasted blocks    H0 - HEC false_block_rate and wasted_reviewer_hours: interval above 0
    HR2 missed changes   H0 - HEC hwl_per_1000 above 0, and the share of H0's excess leakage
                         in classes R, D, C, E exceeds their share of impermissible changes
    HR3 DJ               HDJ - H0 hwl_per_1000: interval below 0
    HR4 robustness       HR1 and HR2 under each other review profile found in the root (runs
                         carry their profile in the manifest), and the break-even catch rate
                         above 0.333 (from breakeven_summary.csv when present)
    HR5 LLM reviewer     HL vs H0 and vs HEC on the same measures, no test

The bootstrap resamples units with replacement (seeded, 2,000 resamples); the
interval is the 2.5th-97.5th percentile of the mean paired difference. With
fewer than two units an interval is degenerate and is reported as such.
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import sys

if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path[:] = [x for x in sys.path if os.path.abspath(x or os.curdir) != _HERE]
    sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from simulation.ec import review_sim, scorecard                       # noqa: E402

BOOT_SEED = 20261023
RDCE = ("R", "D", "C", "E")


def paired(units: dict, a: str, b: str, key: str, resamples: int, rng_seed: int = BOOT_SEED) -> dict:
    """Mean of (a - b) over units having both, with a percentile bootstrap interval."""
    diffs = [u[a][key] - u[b][key] for u in units.values() if a in u and b in u
             and u[a].get(key) is not None and u[b].get(key) is not None]
    if not diffs:
        return {"n": 0, "mean": None, "lo": None, "hi": None}
    rng = random.Random(f"{rng_seed}|{a}|{b}|{key}")
    means = []
    for _ in range(resamples):
        s = [diffs[rng.randrange(len(diffs))] for _ in diffs]
        means.append(sum(s) / len(s))
    means.sort()
    lo, hi = means[int(0.025 * resamples)], means[min(resamples - 1, int(0.975 * resamples))]
    return {"n": len(diffs), "mean": sum(diffs) / len(diffs), "lo": lo, "hi": hi}


def excess_share(units_lines: dict) -> tuple:
    """(share of H0's excess leakage over HEC in R/D/C/E, share of impermissible changes in R/D/C/E)."""
    ex = ex_rdce = imp = imp_rdce = 0.0
    for u in units_lines.values():
        if "H0" not in u or "HEC" not in u:
            continue
        def leak(L):
            out = {}
            for x in L:
                if x["executed"] and x["impermissible"]:
                    out[x["visibility"]] = out.get(x["visibility"], 0) + x["harm_weights"].get("rulebook", 0)
            return out
        a, b = leak(u["H0"]), leak(u["HEC"])
        for c in set(a) | set(b):
            d = a.get(c, 0) - b.get(c, 0)
            ex += d
            if c in RDCE:
                ex_rdce += d
        for x in u["H0"]:
            if x["impermissible"]:
                imp += 1
                imp_rdce += int(x["visibility"] in RDCE)
    return ((ex_rdce / ex) if ex else None, (imp_rdce / imp) if imp else None)


def analyze(root: str, params: dict, resamples: int = 2000) -> dict:
    by_profile: dict = {}
    lines_by_unit: dict = {}
    cache: dict = {}
    for d in scorecard.find_runs(root):
        row, L = scorecard.scorecard(d, params, cache)
        prof = row.get("review_profile") or "flat-edmundson"
        unit = (row["pack"], row["seed"])
        # A-D carry no review profile: they belong to every profile's comparison.
        profs = [prof] if row["arm"] in ("H0", "HL", "HEC", "HDJ", "HECDJ") else [None]
        for pf in profs:
            by_profile.setdefault(pf, {}).setdefault(unit, {})[row["arm"]] = row
        if prof == "flat-edmundson":
            lines_by_unit.setdefault(unit, {})[row["arm"]] = L
    res = {"profiles": {}}
    for prof, units in by_profile.items():
        if prof is None:
            continue
        r = {"units": sorted(str(u) for u in units)}
        r["HR1_false_block"] = paired(units, "H0", "HEC", "false_block_rate", resamples)
        r["HR1_wasted_hours"] = paired(units, "H0", "HEC", "wasted_reviewer_hours", resamples)
        r["HR2_hwl"] = paired(units, "H0", "HEC", "hwl_per_1000", resamples)
        r["HR3_hwl"] = paired(units, "HDJ", "H0", "hwl_per_1000", resamples)
        r["HR5_HL_H0_hwl"] = paired(units, "HL", "H0", "hwl_per_1000", resamples)
        r["HR5_HL_HEC_hwl"] = paired(units, "HL", "HEC", "hwl_per_1000", resamples)
        res["profiles"][prof] = r
    res["HR2_rdce_shares"] = excess_share(lines_by_unit)
    be = os.path.join(root, "breakeven_summary.csv")
    if os.path.exists(be):
        with open(be) as fh:
            res["breakeven"] = list(csv.DictReader(fh))
    return res


def _iv(x: dict) -> str:
    if not x or not x.get("n"):
        return "NA (no paired units)"
    deg = " (degenerate: one unit)" if x["n"] < 2 else ""
    return f"{x['mean']:.4g} [{x['lo']:.4g}, {x['hi']:.4g}], n={x['n']}{deg}"


def report(res: dict) -> str:
    out = ["# Benchmark analysis", "", f"> {scorecard.HONESTY}", ""]
    for prof, r in sorted(res["profiles"].items()):
        p1 = r["HR1_false_block"]
        p2 = r["HR2_hwl"]
        p3 = r["HR3_hwl"]
        out += [f"## Review profile `{prof}` (units: {', '.join(r['units'])})", "",
                "| Hypothesis | Paired difference, mean [95% bootstrap interval] | Supported |", "|---|---|---|",
                f"| HR1 false-block rate H0 - HEC | {_iv(p1)} | {bool(p1.get('lo') is not None and p1['lo'] > 0)} |",
                f"| HR1 wasted reviewer hours H0 - HEC | {_iv(r['HR1_wasted_hours'])} | "
                f"{bool(r['HR1_wasted_hours'].get('lo') is not None and r['HR1_wasted_hours']['lo'] > 0)} |",
                f"| HR2 harm-weighted leakage H0 - HEC | {_iv(p2)} | {bool(p2.get('lo') is not None and p2['lo'] > 0)} |",
                f"| HR3 harm-weighted leakage HDJ - H0 | {_iv(p3)} | {bool(p3.get('hi') is not None and p3['hi'] < 0)} |",
                f"| HR5 HL - H0 (exploratory) | {_iv(r['HR5_HL_H0_hwl'])} | no test |",
                f"| HR5 HL - HEC (exploratory) | {_iv(r['HR5_HL_HEC_hwl'])} | no test |", ""]
    ex, imp = res["HR2_rdce_shares"]
    out += ["## HR2 concentration (flat-Edmundson)", "",
            f"Share of H0's excess leakage over HEC in classes R, D, C, E: {ex if ex is None else round(ex, 4)}; "
            f"their share of H0's impermissible changes: {imp if imp is None else round(imp, 4)}.", ""]
    profs = [p for p in res["profiles"] if p != "flat-edmundson"]
    out += ["## HR4 robustness", "",
            ("Other profiles in this root: " + ", ".join(profs)) if profs else
            "No other review profile in this root: HR4 needs the sensitivity runs.", ""]
    for b in res.get("breakeven") or []:
        out.append(f"- break-even ({b.get('pack')}, seed {b.get('seed')}): catch vs HEC {b.get('breakeven_catch_vs_HEC')}, "
                   f"false-flag ratio vs HEC {b.get('breakeven_false_flag_ratio_vs_HEC')}")
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Benchmark analysis: HR1-HR5")
    ap.add_argument("root")
    ap.add_argument("--out", default=None)
    ap.add_argument("--resamples", type=int, default=2000)
    ap.add_argument("--benchmark-params", default=None)
    a = ap.parse_args(argv)
    res = analyze(a.root, review_sim.load_params(a.benchmark_params), a.resamples)
    if not res["profiles"]:
        print(f"no benchmark runs under {a.root}", file=sys.stderr)
        return 1
    out = a.out or a.root
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "benchmark.md")
    with open(path, "w") as fh:
        fh.write(report(res))
    print(report(res))
    print(f"-> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
