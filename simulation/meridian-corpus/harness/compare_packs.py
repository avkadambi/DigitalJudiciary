"""
Cross-pack profile comparison, over two or more packs.

Chapter 5's RQ3 asks a domain-parameterisation question: when the provision
inventory, factor vocabulary, seed records and case content are re-instantiated
for a different enterprise — holding the case-category composition fixed by
design — do the route, stage and storage profiles remain identical?

It is a claim about the implementation, not a discovery about the world. Matched
composition makes matched profiles the expected outcome, and a deviation
falsifies the implementation rather than the theory. This script computes the
comparison so a reader can see which cells match and which move.

    python3 harness/compare_packs.py [manifest.json ...]

With no arguments it compares this pack against any sibling pack directories it
finds alongside this repository.
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PARENT = os.path.normpath(os.path.join(ROOT, ".."))

SIBLINGS = [
    "vetpoc-constitution-corpus",
    "semifab-constitution-corpus",
    "frontierllm-constitution-corpus",
    "dcvigil-constitution-corpus",
    "meridian-corpus",
]


def discover():
    paths = [os.path.join(ROOT, "corpus", "manifest.json")]
    for name in SIBLINGS:
        p = os.path.join(PARENT, name, "corpus", "manifest.json")
        if os.path.exists(p) and os.path.normpath(p) != os.path.normpath(paths[0]):
            paths.append(p)
    return paths


def load(path):
    with open(path) as fh:
        return json.load(fh)


def pack_name(path):
    return os.path.basename(os.path.dirname(os.path.dirname(path))).replace(
        "-constitution-corpus", "").replace("-corpus", "")


def main():
    paths = sys.argv[1:] or discover()
    if len(paths) < 2:
        print("Only one pack found. Pass two or more manifest paths to compare.")
        return 1
    packs = [(pack_name(p), load(p)) for p in paths]
    names = [n for n, _ in packs]

    def row(label, values, note=""):
        same = "=" if len(set(values)) == 1 else "≠"
        cells = " | ".join(str(v) for v in values)
        return f"| {label} | {cells} | {same} | {note} |"

    header = "| Quantity | " + " | ".join(names) + " | | Note |"
    sep = "| :--- | " + " | ".join("---:" for _ in names) + " | :-: | :--- |"
    lines = [header, sep]

    for label, key, note in [
        ("cases", "cases", "held fixed by design"),
        ("opening store", "opening_store", "one seed record per ordinary provision, plus the fixed conflict, tie, supersession, lapse and seeded sets"),
        ("records written in run", "records_written_in_run", "contest is a social input, not a decision"),
        ("final store", "final_store", ""),
        ("docket entries", "docket_entries", ""),
        ("consolidation classes", "consolidation_classes", "class size is drawn, so the count moves"),
        ("like-case pairs", "like_case_pairs", ""),
        ("construction anomalies", "construction_anomalies", "zero in all packs"),
    ]:
        lines.append(row(label, [p[key] for _, p in packs], note))

    lines.append("| | " + " | ".join("" for _ in names) + " | | |")
    routes = sorted({k for _, p in packs for k in p["routes"]})
    for r in routes:
        lines.append(row(f"route: {r}", [p["routes"].get(r, 0) for _, p in packs]))
    decisions = sorted({k for _, p in packs for k in p["decisions"]})
    for d in decisions:
        lines.append(row(f"decision: {d}", [p["decisions"].get(d, 0) for _, p in packs]))

    print("\n".join(lines))
    print()

    cats_match = len({json.dumps(p["categories"], sort_keys=True) for _, p in packs}) == 1
    print(f"Category composition identical across {len(packs)} packs: {cats_match}")

    total = packs[0][1]["cases"]
    worst_route, worst_gap = None, 0.0
    for r in routes:
        vals = [p["routes"].get(r, 0) for _, p in packs]
        gap = (max(vals) - min(vals)) / total
        if gap > worst_gap:
            worst_route, worst_gap = r, gap
    print(f"Largest route-share spread: {worst_route} at "
          f"{worst_gap * 100:.2f} percentage points of the corpus")

    dec_worst, dec_gap = None, 0.0
    for d in decisions:
        vals = [p["decisions"].get(d, 0) for _, p in packs]
        gap = (max(vals) - min(vals)) / total
        if gap > dec_gap:
            dec_worst, dec_gap = d, gap
    print(f"Largest decision-share spread: {dec_worst} at "
          f"{dec_gap * 100:.2f} percentage points of the corpus")
    return 0


if __name__ == "__main__":
    sys.exit(main())
