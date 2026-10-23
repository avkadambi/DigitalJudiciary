"""
The break-even sweep (benchmark build §3.8): how far would the human reviewer
have to move before the conclusion flips?

    python3 simulation/ec/breakeven.py <results_root> [--out DIR]

`H0` is re-scored over a grid (catch 0..1 by 0.05, false-flag ratio 0..3 by
0.25) without re-running the agent: the reviewer stage is a pure function of
each change's common-random-number draw `u`, the answer key and the
parameters (`review_sim.PeerReviewer`, with the run's own profile, so class
and season multipliers apply). Stages after review are not recomputed (H0 has
none). For each (pack, seed) with H0 and HEC (and HECDJ) runs it finds the
catch rate at which H0's harm-weighted leakage equals HEC's (and HECDJ's), at
the run's false-flag ratio, and the false-flag ratio at which H0's
false-block rate equals HEC's, at the run's catch rate. Writes
`breakeven.csv` (every grid point), `breakeven_summary.csv` and
`fig_breakeven.png` (a heatmap with the literature points marked) when
matplotlib is available.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys

if __name__ == "__main__":
    # Run as a script: drop this folder from the path (its calendar.py would shadow the
    # standard library's for matplotlib) and put the repository root first.
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path[:] = [x for x in sys.path if os.path.abspath(x or os.curdir) != _HERE]
    sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from simulation.ec import ledger, review_sim, scorecard                # noqa: E402

LITERATURE = {"flat-edmundson": (0.333, 1.70), "braz-unprompted": (0.12, 1.70), "braz-prompted": (0.96, 1.70)}


def grid(params: dict) -> tuple:
    def rng(spec):
        lo, hi, step = spec
        n = int(round((hi - lo) / step))
        return [round(lo + i * step, 10) for i in range(n + 1)]
    return rng(params["sweep"]["catch"]["value"]), rng(params["sweep"]["false_flag_ratio"]["value"])


def rescore(run_dir: str, params: dict, catch: float, ratio: float, cache: dict, loaded: dict | None = None) -> dict:
    """H0's scorecard at (catch, false-flag ratio), from its ledger and the review draws."""
    loaded = loaded or ledger.load_run(run_dir)
    rv_meta = (loaded["manifest"].get("benchmark") or {}).get("review") or {}
    reviewer = review_sim.PeerReviewer(params, rv_meta.get("profile") or "flat-edmundson", 0, "",
                                       catch=catch, false_flag_ratio=ratio)
    reviewer.set_p_imperm(rv_meta.get("p_imperm") or 0.0)

    def override(line, rv):
        inv = line["bench"]["invariant"]
        p = reviewer.catch_for(inv["visibility"], line["day"]) if inv["impermissible"] else reviewer.false_reject
        return rv["u"] < p
    pack = loaded["manifest"]["pack"]
    if pack not in cache:
        from simulation.ec.run_year import PackData
        canon = PackData(pack).fresh_canon()
        cache[pack] = (canon, scorecard.weights_by_scheme(pack, canon))
    canon, w = cache[pack]
    L = ledger.build(run_dir, canon, w, review_override=override, loaded=loaded)
    return scorecard.score_lines(L, params, loaded["manifest"], loaded["bench_log"], loaded.get("registry"))


def _cross(xs: list, ys: list, target: float, rising: bool):
    """The first x at which y reaches `target` (linear interpolation), or None."""
    for i in range(len(xs)):
        y = ys[i]
        if y is None:
            continue
        hit = (y >= target) if rising else (y <= target)
        if hit:
            if i == 0:
                return xs[0]
            y0 = ys[i - 1]
            if y0 is None or y == y0:
                return xs[i]
            return xs[i - 1] + (target - y0) * (xs[i] - xs[i - 1]) / (y - y0)
    return None


def sweep(root: str, params: dict) -> tuple:
    runs = {}
    for d in scorecard.find_runs(root):
        m = ledger._load(os.path.join(d, "manifest.json"), {})
        runs.setdefault((m.get("pack"), m.get("seed")), {})[m.get("arm")] = d
    catches, ratios = grid(params)
    rows, summary, cache = [], [], {}
    for (pack, seed), arms in sorted(runs.items(), key=lambda kv: str(kv[0])):
        if "H0" not in arms:
            continue
        loaded = ledger.load_run(arms["H0"])
        rv = (loaded["manifest"].get("benchmark") or {}).get("review") or {}
        refs = {a: scorecard.scorecard(arms[a], params, cache)[0] for a in ("HEC", "HECDJ") if a in arms}
        table = {}
        for c in catches:
            for r in ratios:
                s = rescore(arms["H0"], params, c, r, cache, loaded)
                table[(c, r)] = s
                rows.append({"pack": pack, "seed": seed, "catch": c, "false_flag_ratio": r,
                             "hwl_per_1000": s["hwl_per_1000"], "false_block_rate": s["false_block_rate"],
                             **{f"{a}_hwl_per_1000": ref["hwl_per_1000"] for a, ref in refs.items()},
                             **{f"{a}_false_block_rate": ref["false_block_rate"] for a, ref in refs.items()}})
        r0 = min(ratios, key=lambda r: abs(r - float(rv.get("false_flag_ratio", 1.7))))
        c0 = min(catches, key=lambda c: abs(c - float(rv.get("catch", 0.333))))
        out = {"pack": pack, "seed": seed, "run_catch": rv.get("catch"), "run_false_flag_ratio": rv.get("false_flag_ratio")}
        for a, ref in refs.items():
            out[f"breakeven_catch_vs_{a}"] = _cross(catches, [table[(c, r0)]["hwl_per_1000"] for c in catches],
                                                    ref["hwl_per_1000"], rising=False)
            out[f"breakeven_false_flag_ratio_vs_{a}"] = _cross(
                ratios, [table[(c0, r)]["false_block_rate"] for r in ratios], ref["false_block_rate"] or 0.0, rising=True)
        summary.append(out)
    return rows, summary


def figure(rows: list, path: str) -> bool:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return False
    if not rows or "HEC_hwl_per_1000" not in rows[0]:
        return False
    catches = sorted({r["catch"] for r in rows})
    ratios = sorted({r["false_flag_ratio"] for r in rows})
    z = [[0.0] * len(catches) for _ in ratios]
    count = [[0] * len(catches) for _ in ratios]
    for r in rows:
        i, j = ratios.index(r["false_flag_ratio"]), catches.index(r["catch"])
        z[i][j] += r["hwl_per_1000"] - r["HEC_hwl_per_1000"]
        count[i][j] += 1
    z = [[z[i][j] / max(1, count[i][j]) for j in range(len(catches))] for i in range(len(ratios))]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    im = ax.imshow(z, origin="lower", aspect="auto", cmap="RdBu_r",
                   extent=[catches[0], catches[-1], ratios[0], ratios[-1]])
    fig.colorbar(im, ax=ax, label="H0 - HEC harm-weighted leakage per 1,000")
    for name, (c, r) in LITERATURE.items():
        ax.plot([c], [r], "k^")
        ax.annotate(name, (c, r), textcoords="offset points", xytext=(4, 4), fontsize=8)
    ax.set_xlabel("reviewer catch rate")
    ax.set_ylabel("false flags per true flag")
    ax.set_title("Break-even: old-school review vs EC (plumbing unless run on the benchmark seeds)")
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Break-even sweep of the H0 reviewer")
    ap.add_argument("root")
    ap.add_argument("--out", default=None)
    ap.add_argument("--benchmark-params", default=None)
    a = ap.parse_args(argv)
    params = review_sim.load_params(a.benchmark_params)
    rows, summary = sweep(a.root, params)
    if not rows:
        print(f"no H0 runs under {a.root}", file=sys.stderr)
        return 1
    out = a.out or a.root
    os.makedirs(out, exist_ok=True)
    scorecard.write_csv(os.path.join(out, "breakeven.csv"), rows, list(rows[0].keys()))
    scorecard.write_csv(os.path.join(out, "breakeven_summary.csv"), summary,
                        sorted({k for s in summary for k in s}, key=lambda k: (k not in ("pack", "seed"), k)))
    fig = figure(rows, os.path.join(out, "fig_breakeven.png"))
    for s in summary:
        print(s)
    print(f"{len(rows)} grid points -> {os.path.join(out, 'breakeven.csv')}" + ("; fig_breakeven.png" if fig else
                                                                               "; (no matplotlib: no figure)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
