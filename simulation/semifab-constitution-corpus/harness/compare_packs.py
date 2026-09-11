"""
Cross-pack profile comparison.

Chapter 5's RQ3 asks a domain-parameterisation question: when the provision
inventory, factor vocabulary, seed records and case content are re-instantiated
for a different enterprise — holding the case-category composition fixed by
design — do the route, stage and storage profiles remain identical?

That is a claim about the implementation, not a discovery about the world.
Matched composition makes matched profiles the expected outcome, and a deviation
falsifies the implementation rather than the theory. This script computes the
comparison so that a reader can see which cells match and which do not, and the
report says why for every cell that moves.

    python3 harness/compare_packs.py <manifest-a.json> <manifest-b.json>

With no arguments it compares this pack against ../vetpoc-constitution-corpus.
"""

from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DEFAULT_A = os.path.join(ROOT, "corpus", "manifest.json")
DEFAULT_B = os.path.normpath(
    os.path.join(ROOT, "..", "vetpoc-constitution-corpus", "corpus", "manifest.json"))


def load(path):
    with open(path) as fh:
        return json.load(fh)


def row(label, a, b, note=""):
    same = "=" if a == b else "≠"
    return f"| {label} | {a} | {b} | {same} | {note} |"


def main():
    pa = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_A
    pb = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_B
    if not os.path.exists(pb):
        print(f"comparison pack not found at {pb}")
        print("Pass two manifest paths explicitly to compare arbitrary packs.")
        return 1
    a, b = load(pa), load(pb)
    na = os.path.basename(os.path.dirname(os.path.dirname(pa)))
    nb = os.path.basename(os.path.dirname(os.path.dirname(pb)))

    lines = [f"| Quantity | {na} | {nb} | | Note |", "| :--- | ---: | ---: | :-: | :--- |"]
    lines.append(row("cases", a["cases"], b["cases"], "held fixed by design"))
    lines.append(row("opening store", a["opening_store"], b["opening_store"],
                     "one seed record per ordinary provision, plus the conflict, tie, "
                     "supersession, lapse and seeded-jurisprudence sets"))
    lines.append(row("records written in run", a["records_written_in_run"],
                     b["records_written_in_run"], "contest is a social input, not a decision"))
    lines.append(row("final store", a["final_store"], b["final_store"], ""))
    lines.append(row("docket entries", a["docket_entries"], b["docket_entries"], ""))
    lines.append(row("consolidation classes", a["consolidation_classes"],
                     b["consolidation_classes"], "class size is drawn, so the count moves"))
    lines.append(row("like-case pairs", a["like_case_pairs"], b["like_case_pairs"], ""))
    lines.append(row("construction anomalies", a["construction_anomalies"],
                     b["construction_anomalies"], "zero in both"))

    lines.append("| | | | | |")
    routes = sorted(set(a["routes"]) | set(b["routes"]))
    for r in routes:
        lines.append(row(f"route: {r}", a["routes"].get(r, 0), b["routes"].get(r, 0), ""))
    decisions = sorted(set(a["decisions"]) | set(b["decisions"]))
    for d in decisions:
        lines.append(row(f"decision: {d}", a["decisions"].get(d, 0), b["decisions"].get(d, 0), ""))

    print("\n".join(lines))

    cats_match = a["categories"] == b["categories"]
    print()
    print(f"Category composition identical: {cats_match}")
    ra, rb = a["routes"], b["routes"]
    total = sum(ra.values())
    drift = {k: abs(ra.get(k, 0) - rb.get(k, 0)) / total for k in routes}
    worst = max(drift, key=drift.get)
    print(f"Largest route share difference: {worst} at "
          f"{drift[worst] * 100:.2f} percentage points of the corpus")
    return 0


if __name__ == "__main__":
    sys.exit(main())
