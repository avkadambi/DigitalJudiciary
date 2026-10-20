"""
Analysis over the metrics table (DESIGN §6): equivalence and arm differences.

    python3 simulation/ec/analyze.py <results_root> [--margin 0.03] [--boot 2000]

Reads `<root>/metrics.csv`. Writes `analysis.md` and `analysis.json` beside it.

  TOST     E2 (pressure sensitivity) and E3 (observation gap) are properties of
           the proposal stream, which every arm shares before its gate, so they
           should be *equivalent* across arms. For every arm pair the paired
           differences over (pack, seed) are tested with two one-sided t tests
           against ±margin; equivalence is declared when both p < 0.05.
  Bootstrap percentile intervals over (pack, seed) units for the difference
           between arms on E1, E6 (recall), E7 (blind spot) and E8 (escalations
           per 30 days after - before the first gloss).

Pure standard library: Student t tail from the regularised incomplete beta.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import os
import random
import sys

TOST_METRICS = ("e2_ps", "e3_og")
BOOT_METRICS = {"e1_imperm": "E1 proposal risk", "e6_recall": "E6 disclosure recall",
                "e7_blind_spot": "E7 blind spot", "e8_return": "E8 doctrine return (after - before)"}
ARM_ORDER = ("A", "B", "C", "D")


# ---------------------------------------------------------------------------
# Student t
# ---------------------------------------------------------------------------


def _betacf(a: float, b: float, x: float) -> float:
    MAXIT, EPS, FPMIN = 300, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < EPS:
            break
    return h


def betainc(a: float, b: float, x: float) -> float:
    """Regularised incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1.0 - x)
    bt = math.exp(lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def t_cdf(t: float, df: float) -> float:
    if df <= 0:
        return float("nan")
    x = df / (df + t * t)
    tail = 0.5 * betainc(df / 2.0, 0.5, x)
    return 1.0 - tail if t >= 0 else tail


def t_quantile(p: float, df: float) -> float:
    lo, hi = -1e3, 1e3
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_cdf(mid, df) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------


def paired_tost(diffs: list, margin: float) -> dict:
    n = len(diffs)
    out = {"n": n, "mean": None, "sd": None, "se": None, "p_lower": None, "p_upper": None, "p": None,
           "ci90": None, "equivalent": None, "margin": margin}
    if n == 0:
        return out
    mean = sum(diffs) / n
    out["mean"] = mean
    if n < 2:
        out["equivalent"] = abs(mean) < margin if n == 1 else None
        out["note"] = "n < 2: point estimate only; no test"
        return out
    var = sum((d - mean) ** 2 for d in diffs) / (n - 1)
    sd = math.sqrt(var)
    se = sd / math.sqrt(n)
    out["sd"], out["se"] = sd, se
    df = n - 1
    if se == 0.0:
        inside = abs(mean) < margin
        out["p_lower"] = out["p_upper"] = out["p"] = (0.0 if inside else 1.0)
        out["ci90"] = [mean, mean]
        out["equivalent"] = inside
        return out
    t_low = (mean + margin) / se          # H0: mean <= -margin
    t_up = (mean - margin) / se           # H0: mean >= +margin
    p_low = 1.0 - t_cdf(t_low, df)
    p_up = t_cdf(t_up, df)
    q = t_quantile(0.95, df)
    out.update(p_lower=p_low, p_upper=p_up, p=max(p_low, p_up), ci90=[mean - q * se, mean + q * se],
               equivalent=(max(p_low, p_up) < 0.05))
    return out


def bootstrap_diff(diffs: list, reps: int, rng: random.Random) -> dict:
    n = len(diffs)
    if n == 0:
        return {"n": 0, "mean": None, "lo": None, "hi": None}
    mean = sum(diffs) / n
    if n == 1:
        return {"n": 1, "mean": mean, "lo": mean, "hi": mean, "note": "n = 1: interval degenerate"}
    means = []
    for _ in range(reps):
        s = [diffs[rng.randrange(n)] for _ in range(n)]
        means.append(sum(s) / n)
    means.sort()
    lo = means[int(0.025 * (reps - 1))]
    hi = means[int(0.975 * (reps - 1))]
    return {"n": n, "mean": mean, "lo": lo, "hi": hi, "reps": reps}


# ---------------------------------------------------------------------------
# Table handling
# ---------------------------------------------------------------------------


def read_metrics(path: str) -> list:
    rows = []
    with open(path, newline="") as fh:
        for r in csv.DictReader(fh):
            d = {}
            for k, v in r.items():
                if v in ("NA", "", None):
                    d[k] = None
                else:
                    try:
                        d[k] = float(v) if ("." in v or "e" in v.lower() or k not in ("seed", "days")) else int(v)
                    except ValueError:
                        d[k] = v
            if d.get("e8_esc_per30_after") is not None and d.get("e8_esc_per30_before") is not None:
                d["e8_return"] = d["e8_esc_per30_after"] - d["e8_esc_per30_before"]
            else:
                d["e8_return"] = None
            rows.append(d)
    return rows


def paired_diffs(rows: list, metric: str, arm1: str, arm2: str) -> list:
    """arm2 - arm1 over matching (pack, seed, archetype)."""
    by = {}
    for r in rows:
        by[(r["pack"], r["seed"], r["archetype"], r["arm"])] = r.get(metric)
    out = []
    for (pack, seed, arch, arm), v1 in by.items():
        if arm != arm1:
            continue
        v2 = by.get((pack, seed, arch, arm2))
        if v1 is None or v2 is None:
            continue
        out.append(float(v2) - float(v1))
    return out


def arms_in(rows: list) -> list:
    present = {r["arm"] for r in rows}
    return [a for a in ARM_ORDER if a in present] + sorted(present - set(ARM_ORDER))


def fmt(v, nd=4) -> str:
    if v is None:
        return "NA"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def analyze(rows: list, margin: float, reps: int, seed: int = 20260906) -> dict:
    arms = arms_in(rows)
    pairs = list(itertools.combinations(arms, 2))
    rng = random.Random(seed)
    tost = {m: {} for m in TOST_METRICS}
    for m in TOST_METRICS:
        for a1, a2 in pairs:
            tost[m][f"{a1}-{a2}"] = paired_tost(paired_diffs(rows, m, a1, a2), margin)
    boot = {m: {} for m in BOOT_METRICS}
    for m in BOOT_METRICS:
        for a1, a2 in pairs:
            boot[m][f"{a1}-{a2}"] = bootstrap_diff(paired_diffs(rows, m, a1, a2), reps, rng)
    means = {}
    for arm in arms:
        sub = [r for r in rows if r["arm"] == arm]
        means[arm] = {}
        for m in list(TOST_METRICS) + list(BOOT_METRICS):
            xs = [r[m] for r in sub if r.get(m) is not None]
            means[arm][m] = (sum(xs) / len(xs)) if xs else None
        means[arm]["n_runs"] = len(sub)
    units = sorted({(r["pack"], r["seed"]) for r in rows})
    return {"margin": margin, "bootstrap_reps": reps, "arms": arms, "units": [list(u) for u in units],
            "provenance": sorted({r.get("provenance") for r in rows if r.get("provenance")}),
            "arm_means": means, "tost": tost, "bootstrap": boot}


def render_md(an: dict) -> str:
    L = []
    L.append("# EC year analysis\n")
    L.append(f"Units: {len(an['units'])} (pack, seed) pairs; arms: {', '.join(an['arms'])}; "
             f"TOST margin ±{an['margin']}; bootstrap reps {an['bootstrap_reps']}; "
             f"provenance: {', '.join(an['provenance'])}\n")
    L.append("## Arm means\n")
    ms = list(TOST_METRICS) + list(BOOT_METRICS)
    L.append("| arm | runs | " + " | ".join(ms) + " |")
    L.append("|---|---|" + "---|" * len(ms))
    for arm, d in an["arm_means"].items():
        L.append(f"| {arm} | {d['n_runs']} | " + " | ".join(fmt(d[m]) for m in ms) + " |")
    L.append("")
    L.append("## TOST equivalence across arms (paired by pack and seed)\n")
    L.append("E2 and E3 are properties of the shared proposal stream; arms should be equivalent.\n")
    L.append("| metric | arms | n | mean diff | 90% CI | p lower | p upper | equivalent |")
    L.append("|---|---|---|---|---|---|---|---|")
    for m, d in an["tost"].items():
        for pair, t in d.items():
            ci = f"[{fmt(t['ci90'][0])}, {fmt(t['ci90'][1])}]" if t.get("ci90") else "NA"
            L.append(f"| {m} | {pair} | {t['n']} | {fmt(t['mean'])} | {ci} | {fmt(t['p_lower'])} | "
                     f"{fmt(t['p_upper'])} | {fmt(t['equivalent'])} |")
    L.append("")
    L.append("## Bootstrap intervals for arm differences (second minus first)\n")
    L.append("| metric | arms | n | mean diff | 2.5% | 97.5% |")
    L.append("|---|---|---|---|---|---|")
    for m, d in an["bootstrap"].items():
        for pair, b in d.items():
            L.append(f"| {BOOT_METRICS[m]} | {pair} | {b['n']} | {fmt(b['mean'])} | {fmt(b['lo'])} | {fmt(b['hi'])} |")
    L.append("")
    if len(an["units"]) < 2:
        L.append("Note: fewer than two (pack, seed) units; tests are point estimates only.\n")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="EC analysis: TOST and bootstrap over metrics.csv")
    ap.add_argument("root", help="results root (containing metrics.csv) or the csv path")
    ap.add_argument("--margin", type=float, default=0.03)
    ap.add_argument("--boot", type=int, default=2000)
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    csv_path = a.root if a.root.endswith(".csv") else os.path.join(a.root, "metrics.csv")
    if not os.path.exists(csv_path):
        print(f"no metrics.csv at {csv_path}; run metrics.py first", file=sys.stderr)
        return 1
    rows = read_metrics(csv_path)
    an = analyze(rows, a.margin, a.boot)
    out_dir = a.out or os.path.dirname(os.path.abspath(csv_path))
    os.makedirs(out_dir, exist_ok=True)
    md = render_md(an)
    with open(os.path.join(out_dir, "analysis.md"), "w") as fh:
        fh.write(md)
    with open(os.path.join(out_dir, "analysis.json"), "w") as fh:
        json.dump(an, fh, indent=1, ensure_ascii=False)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
