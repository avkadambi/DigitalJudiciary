#!/usr/bin/env python3
"""M16 / M17 — the two mutants that give CC-33 its standing.

Section 7.6's rule is that a conformance check earns its place by killing a
mutant nothing else catches. CC-33 asserts pressure invariance: a case carrying
a non-predicated pressure factor decides exactly as its control. Two things
secure that property and they are secured differently:

  (1) `distinguish` is the subset test premise(r) subset-of facts(c). It is
      MONOTONE in facts(c), so an extra fact can never distinguish a record
      that survived without it. This half is structural.

  (2) Retrieval scores by Jaccard against theta = 0.25. Adding a fact enlarges
      the union and so LOWERS the score. This half is contingent on headroom,
      and it is the half CC-33 exists to guard.

M16 attacks (2) with a plausible mis-specification, not a strawman: score a
record by how much of the PRESENT CASE it explains, |premise & facts| / |facts|,
rather than by symmetric overlap. That is a metric a reasonable implementer
might choose, and under it every extra fact dilutes the score directly.

M17 attacks (1): require premise(r) == facts(c) rather than containment.

Both are applied as single-line source edits on an exact anchor, in the style
of reproduce/mutation_matrix.py.
"""
import os, shutil, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/dj-press"
KERNEL = os.path.join(ROOT, "app", "kernel.py")

MUTANTS = [
    ("M16", KERNEL,
     "            j = (len(case_facts & rec_facts) / len(union)) if union else 0.0",
     "            j = (len(case_facts & rec_facts) / len(case_facts)) if case_facts else 0.0",
     "retrieval scores case-coverage instead of symmetric overlap; extra facts dilute"),
    ("M17", os.path.join(ROOT, "app", "judges.py"),
     "        missing = sorted(premise - facts)",
     "        missing = sorted(premise ^ facts)",
     "the gate requires premise == facts rather than containment"),
]


def run(cmd, cwd=ROOT):
    p = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def suites():
    out = {}
    for name, script in (("conformance", "run_conformance.py"),
                         ("interface", "run_interface_conformance.py"),
                         ("extension", "run_extension_conformance.py")):
        rc, txt = run(f"python3 {script}")
        line = [l for l in txt.splitlines() if l.startswith("RESULT:")]
        out[name] = line[0].replace("RESULT: ", "") if line else "CRASH"
    return out


def cc33():
    rc, txt = run("OUT=/tmp/m-run bash reproduce/run_all.sh > /dev/null 2>&1; "
                  "for p in sctower vetpoc dcvigil frontierllm; do "
                  "python3 reproduce/cc33_pressure_invariance.py /tmp/m-run/$p.db "
                  "demo/companies/$p/cases.json; done")
    passed = txt.count("CC-33  PASS")
    return ("PASS" if passed == 4 else f"FAIL ({passed}/4 packs pass)"), txt


print("CLEAN BASELINE")
base_s = suites()
base_c, _ = cc33()
print(f"  suites: {base_s}")
print(f"  CC-33 : {base_c}\n")

for mid, path, old, new, gloss in MUTANTS:
    src = open(path).read()
    n = src.count(old)
    if n != 1:
        print(f"{mid}  ANCHOR ERROR: {n} occurrences of the anchor in {path}")
        continue
    shutil.copy(path, path + ".bak")
    open(path, "w").write(src.replace(old, new))
    try:
        s = suites()
        c, _ = cc33()
        killed_by_others = any(v != base_s[k] for k, v in s.items())
        killed_by_cc33 = c != base_c
        verdict = ("KILLED BY CC-33 ALONE" if killed_by_cc33 and not killed_by_others else
                   "killed by CC-33 and by other suites" if killed_by_cc33 else
                   "SURVIVED CC-33")
        print(f"{mid}  {gloss}")
        print(f"     other suites: {s}")
        print(f"     CC-33       : {c}")
        print(f"     -> {verdict}\n")
    finally:
        shutil.move(path + ".bak", path)
        for d in ("app/__pycache__",):
            shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
