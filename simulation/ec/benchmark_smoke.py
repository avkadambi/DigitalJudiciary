"""
The benchmark smoke assertions (benchmark build §8), printed as PASS or FAIL.

    python3 simulation/ec/benchmark_smoke.py <smoke_root>

Over a `run_year.sh benchmark-smoke` root: every arm finished; B-01..B-12 hold
(the conformance report under <root>/conformance); H0 shows nonzero review
false rejects and misses; deterministic HEC executes no impermissible change
(the upper bound); every corner type occurred at least once; the break-even
grid is complete. Smoke figures are a plumbing test, seed 97, not a result.
"""

from __future__ import annotations

import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path[:] = [x for x in sys.path if os.path.abspath(x or os.curdir) != _HERE]
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import corners                                    # noqa: E402

ARMS = ("A", "C", "D", "H0", "HEC", "HDJ", "HECDJ")


def main(argv=None) -> int:
    root = (argv or sys.argv[1:])[0]
    runs = os.path.join(root, "runs", "vetpoc")
    results = []

    def say(name, ok, detail):
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")
    done = [a for a in ARMS if os.path.exists(os.path.join(runs, a, "seed-97", "manifest.json"))]
    say("every arm finished", len(done) == len(ARMS), ", ".join(done))
    rep = os.path.join(root, "conformance", "benchmark_conformance.json")
    if os.path.exists(rep):
        r = json.load(open(rep))
        say("B-01..B-12 hold", r["passed"] == r["total"] == 12, f"{r['passed']}/{r['total']}")
    else:
        say("B-01..B-12 hold", False, "no conformance report")
    rows = {r["arm"]: r for r in csv.DictReader(open(os.path.join(root, "scorecard.csv")))}
    h0 = rows.get("H0", {})
    say("H0 shows review false rejects and misses", int(h0.get("review_false_rejects", 0) or 0) > 0
        and int(h0.get("review_misses", 0) or 0) > 0,
        f"false rejects {h0.get('review_false_rejects')}, misses {h0.get('review_misses')}")
    lines = [json.loads(x) for x in open(os.path.join(runs, "HEC", "seed-97", "run.jsonl"))]
    n = sum(1 for l in lines if l["executed"] and l["impermissible"])
    say("HEC-det executes no impermissible change (upper bound)", n == 0, f"{n} executed impermissible")
    seen = set()
    for a in ARMS:
        for x in open(os.path.join(runs, a, "seed-97", "run.jsonl")):
            c = json.loads(x).get("corner")
            if c:
                seen.add(c)
    say("every corner type occurred", seen == set(corners.CORNER_TYPES),
        f"{len(seen)}/{len(corners.CORNER_TYPES)}" + (f" (missing {sorted(set(corners.CORNER_TYPES) - seen)})"
                                                      if seen != set(corners.CORNER_TYPES) else ""))
    bp = os.path.join(root, "runs", "breakeven.csv")
    be = list(csv.DictReader(open(bp))) if os.path.exists(bp) else []
    say("the break-even grid is complete", len(be) == 21 * 13, f"{len(be)} grid points")
    print("smoke figures are a plumbing test, seed 97, not a result")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
