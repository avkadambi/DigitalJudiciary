#!/usr/bin/env python3
"""Proposition 4, executed: one counter-model per axiom, run both ways.

Sect. 7.8 describes eight axiom mutants and an expected-failure map, and
Proposition 4's proof cites one of them as built. Until 2 September 2026 none
of the eight had ever been run — Appendix C Sect. C.5 executes a different
list, of mechanism mutants — so the proposition's A3 clause rested on a
counter-model that existed only in prose. This harness runs all eight.

**Both directions are asserted, and that is the point.** A mutation matrix
reports a kill or a survival. A counter-model has to show that the named
guarantee HOLDS with the axiom enforced and FAILS with it dropped; a probe
that fails in both directions witnesses nothing at all, and one that holds in
both has not dropped the axiom. Each row therefore runs the probe twice, on
the clean tree and under a single-line relaxation, and a row passes only on
HOLDS → FAILS.

The relaxation is a source edit anchored on an exact string that must occur
exactly once in its file. The file is restored afterwards and the restoration
is verified by SHA-256, exactly as the mechanism matrix does.

One overlap is acknowledged rather than hidden: A6's relaxation is the same
edit as mechanism mutant M3. That is not duplication to be tidied away — the
two ask different questions of it. M3 asks whether the conformance suites
notice the absolute short-circuit being disabled; A6 asks whether anything is
lost when the axiom goes, which is a question about the contract and not about
the checks.

Usage:  python3 reproduce/axiom_matrix.py
"""
from __future__ import annotations

import glob
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENV = dict(os.environ, DJ_JUDGE_MODE="oracle", DJ_DEV_KEYS="1",
           DJ_GITHUB_ALLOW_UNSIGNED="1", PYTHONDONTWRITEBYTECODE="1")

# (axiom, file, anchor, replacement, the guarantee the counter-model breaks)
AXIOMS = [
 ("A1", "app/db.py",
  "  SELECT RAISE(ABORT, 'A1 violation: overlapping branch assignment for principal');",
  "  SELECT 1;",
  "Definition 9(i) and Corollary 1 — one authority may author a provision and adjudicate a case on it"),
 ("A2", "app/db.py",
  "  CHECK (is_acceptance = 0 OR authority_tier = 4),",
  "  CHECK (is_acceptance = 0 OR authority_tier >= 1),",
  "A2's type separation — Decide and Accept_risk share an output type, so A4's trigger and A7's lifecycle bind a function no one has to call"),
 ("A3", "app/kernel.py",
  '            self._registry.require_branch(enacted_by, "lawmakers")',
  "            pass  # A3 dropped for the counter-model",
  "Definition 9(iii) — a Decide principal changes a rule, and the rulebook is no longer byte-identical across adjudications"),
 ("A4", "app/kernel.py",
  '        if a["tier"] == 4 and not promoted_from and not \\',
  '        if False and a["tier"] == 4 and not promoted_from and not \\',
  "A4's exhaustion trigger and the human backstop — risk is accepted on a case that was never contested"),
 ("A5", "app/kernel.py",
  '                            for c in a["retrieval"]["candidates"]]),',
  '                            for c in a["retrieval"]["candidates"]][:0]),',
  "Theorem 2 — a summary is persisted where the trail is required, so rebuild cannot return Provenance(c)"),
 ("A6", "app/adjudicate.py",
  '        if prov["absolute"]:',
  '        if False and prov["absolute"]:',
  "the absolute floor of A6 — a floor violation is retrieved for and may be controlled by a permissive record"),
 ("A7", "app/kernel.py",
  "            if is_acceptance:",
  "            if False and is_acceptance:",
  "Proposition 1's posture set — a waiver exists that the Lawmakers were never told about"),
 ("A8", "app/adjudicate.py",
  '        if state == "bound":',
  '        if False and state == "bound":',
  "A8's bindingness obligation — a bound case is decided against the record its own trail cites"),
]


def clear_cache():
    for p in glob.glob(os.path.join(ROOT, "**", "__pycache__"), recursive=True):
        shutil.rmtree(p, ignore_errors=True)


def run_probe(axiom: str) -> tuple[bool, str]:
    dbp = os.path.join(tempfile.mkdtemp(), f"{axiom}.db")
    p = subprocess.run(
        [sys.executable, "reproduce/axiom_probes.py", axiom],
        cwd=ROOT, env=dict(ENV, DJ_DB=dbp),
        capture_output=True, text=True, timeout=300)
    line = (p.stdout.strip().splitlines() or [""])[-1]
    if line.startswith("HOLDS"):
        return True, line[6:]
    if line.startswith("FAILS"):
        return False, line[6:]
    return None, (line or p.stderr.strip().splitlines()[-1:] or ["no output"])[0]


def main() -> int:
    clear_cache()
    print("PROPOSITION 4, EXECUTED — one counter-model per axiom, run both ways")
    print("A row passes only on HOLDS (axiom enforced) -> FAILS (axiom dropped).")
    print()
    print("%-4s %-9s %-9s %s" % ("id", "enforced", "dropped", "the guarantee the counter-model breaks"))
    ok_rows = 0
    detail_lines = []
    for axiom, rel, anchor, repl, guarantee in AXIOMS:
        path = os.path.join(ROOT, rel)
        orig = open(path, encoding="utf8").read()
        if orig.count(anchor) != 1:
            print("%-4s ANCHOR MISS (%d occurrences in %s)"
                  % (axiom, orig.count(anchor), rel))
            continue
        h0 = hashlib.sha256(orig.encode()).hexdigest()

        clear_cache()
        holds_clean, d_clean = run_probe(axiom)

        clear_cache()
        open(path, "w", encoding="utf8").write(orig.replace(anchor, repl, 1))
        try:
            holds_dropped, d_drop = run_probe(axiom)
        finally:
            open(path, "w", encoding="utf8").write(orig)
            clear_cache()
        assert hashlib.sha256(
            open(path, encoding="utf8").read().encode()).hexdigest() == h0, \
            "restore failed for " + axiom

        good = (holds_clean is True) and (holds_dropped is False)
        ok_rows += 1 if good else 0
        print("%-4s %-9s %-9s %s%s"
              % (axiom,
                 {True: "HOLDS", False: "fails", None: "ERROR"}[holds_clean],
                 {True: "holds", False: "FAILS", None: "ERROR"}[holds_dropped],
                 guarantee, "" if good else "   <-- NOT A COUNTER-MODEL"))
        detail_lines.append(f"  {axiom} enforced: {d_clean}")
        detail_lines.append(f"  {axiom} dropped : {d_drop}")

    print()
    print("What each probe observed")
    print("\n".join(detail_lines))
    print()
    print("counter-models witnessed : %d/%d" % (ok_rows, len(AXIOMS)))
    print("A9 is exercised directly and not by a source edit: its single fault"
          " mode is an absent declaration, and the kernel suite's CC-17 fails"
          " when the declaration is removed from the deployment's constitution"
          " while every other check passes.")
    return 0 if ok_rows == len(AXIOMS) else 1


if __name__ == "__main__":
    sys.exit(main())
