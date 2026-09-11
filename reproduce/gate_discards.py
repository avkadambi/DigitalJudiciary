#!/usr/bin/env python3
"""The one-factor gate-discard query, recovered 1 September 2026.

Appendix C reported, for the 101-case build, "33 distinct candidate-case pairs the
distinguishing gate discards, 31 of them because exactly one factor of the recorded
premise is absent." The query that produced it was not in the released `reproduce/`
directory and six cells across Chapters 4 and 5 and Appendices C and F carried
REGENERATE markers in its place.

It is recoverable from `judgment_invocation`, which the kernel writes for every
distinguish call: `verdict` carries {"distinguished": bool, "grounds": "..."} and the
grounds name the absent premise factors verbatim.

Usage: gate_discards.py <database>
"""
import ast, json, re, sqlite3, sys


def discards(db):
    c = sqlite3.connect(db)
    total = distinct = 0
    by_missing = {}
    seen = set()
    for cand, case, verdict in c.execute(
            "select candidate_hash, case_hash, verdict from judgment_invocation "
            "where kind = 'distinguish'"):
        try:
            v = json.loads(verdict)
        except Exception:
            continue
        if not v.get("distinguished"):
            continue
        total += 1
        key = (cand, case)
        if key in seen:
            continue
        seen.add(key)
        distinct += 1
        m = re.search(r"holding rested on (\[.*?\])", v.get("grounds", ""))
        n = len(ast.literal_eval(m.group(1))) if m else None
        by_missing[n] = by_missing.get(n, 0) + 1
    cases = len({case for cand, case, verdict in c.execute(
        "select candidate_hash, case_hash, verdict from judgment_invocation "
        "where kind = 'distinguish'")
        if (lambda v: v.get("distinguished"))(json.loads(verdict))})
    return distinct, total, by_missing, cases


if __name__ == "__main__":
    d, t, by, cases = discards(sys.argv[1])
    one = by.get(1, 0)
    print(f"  distinct discarded candidate-case pairs : {d}")
    print(f"  discard events (pairs may recur by tier) : {t}")
    print(f"  distinct cases carrying a discard        : {cases}")
    print(f"  discarded because exactly one factor absent : {one}")
    print(f"  by number of absent factors              : "
          f"{ {k: by[k] for k in sorted(by, key=lambda x: (x is None, x))} }")
