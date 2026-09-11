#!/usr/bin/env python3
"""Mutation matrix for the federation checks — evidence the suite can fail.

Each fault is a one-line edit to federation.py or engine.py; the suite must
fail. Each control is a behaviour-preserving edit; the suite must still pass.
Files are restored in a finally block and a backup sidecar survives a kill.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FED = os.path.join(HERE, "federation.py")
ENG = os.path.join(HERE, "engine.py")
SUITE = os.path.join(HERE, "run_federation_checks.py")
BAK = ".mutation-backup"

MUTANTS = [
    ("MF1", "fault", FED, "FOREIGN_SCOPE_OFFSET = 1", "FOREIGN_SCOPE_OFFSET = 0",
     "foreign records are no longer wider: vertical precedent stops being thin (FC-07)"),
    ("MF2", "fault", FED, "        if home is None or home == division:", "        if True:",
     "every record is presented as home: scope no longer separates divisions (FC-07)"),
    ("MF3", "fault", FED, "            out.append(r)\n        else:", "            continue\n        else:",
     "home records are hidden from their own division (FC-01, FC-07)"),
    ("MF4", "fault", ENG, "        if p.absolute and violates(facts, p):", "        if False and p.absolute and violates(facts, p):",
     "the A6 short-circuit is disabled at the enterprise level (FC-01, FC-09)"),
    ("MF5", "fault", ENG, "s.scope_domain == r.scope_domain and s.scope_width < r.scope_width",
     "s.scope_domain == r.scope_domain and s.scope_width > r.scope_width",
     "the scope key prefers the WIDER record: foreign beats home (FC-07)"),
    ("MF6", "fault", FED, "            record_division[rec.id] = c[\"division\"]", "            record_division[rec.id] = None",
     "written records lose their division: nothing counts as foreign (FC-06)"),
    ("MF7", "fault", ENG, "    if unproven:\n        return Admission(record.id, PREMISE_UNPROVEN",
     "    if False:\n        return Admission(record.id, PREMISE_UNPROVEN",
     "silence binds: a foreign record governs a case that never established its premise (FC-11)"),
    ("MC1", "control", FED, "FOREIGN_SCOPE_OFFSET = 1", "FOREIGN_SCOPE_OFFSET = 1  # control",
     "a comment only"),
    ("MC2", "control", FED, "    out = []\n    for r in store:", "    out = list()\n    for r in store:",
     "list() for []"),
]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run_suite():
    p = subprocess.run([sys.executable, SUITE], capture_output=True, text=True, cwd=ROOT)
    for line in p.stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip(), p.returncode
    return "CRASH", p.returncode


def recover():
    for t in (FED, ENG):
        b = t + BAK
        if os.path.exists(b):
            open(t, "w").write(open(b).read()); os.remove(b)
            print(f"recovered {os.path.basename(t)} from an interrupted run")
            cache = os.path.join(os.path.dirname(t), "__pycache__")   # the mutant's newer .pyc would shadow the restored source
            stem = os.path.splitext(os.path.basename(t))[0] + "."
            for name in (os.listdir(cache) if os.path.isdir(cache) else []):
                if name.startswith(stem):
                    os.remove(os.path.join(cache, name))


def main():
    recover()
    base, code = run_suite()
    print(f"baseline: {base}")
    if code != 0:
        print("baseline is not clean; aborting"); return 1
    killed = survived = 0
    rows = []
    for mid, kind, target, anchor, repl, what in MUTANTS:
        original = open(target).read()
        if original.count(anchor) != 1:
            rows.append((mid, kind, what, f"ANCHOR x{original.count(anchor)}", "ERROR")); continue
        h = sha(target)
        try:
            open(target + BAK, "w").write(original)
            open(target, "w").write(original.replace(anchor, repl))
            result, code = run_suite()
        finally:
            open(target, "w").write(original)
            assert sha(target) == h, "restoration failed"
            if os.path.exists(target + BAK):
                os.remove(target + BAK)
        caught = code != 0 or result == "CRASH"
        if kind == "fault":
            outcome = "KILLED" if caught else "SURVIVED (unexpected)"; killed += caught
        else:
            outcome = "survived" if not caught else "KILLED (unexpected)"; survived += (not caught)
        rows.append((mid, kind, what, result, outcome))
    print()
    print(f"{'ID':5} {'KIND':8} {'SUITE':8} {'OUTCOME':22} WHAT IT BREAKS")
    print("-" * 100)
    for r in rows:
        print(f"{r[0]:5} {r[1]:8} {r[3]:8} {r[4]:22} {r[2]}")
    faults = sum(1 for m in MUTANTS if m[1] == "fault"); controls = len(MUTANTS) - faults
    print(f"RESULT: {killed}/{faults} faults killed, {survived}/{controls} controls survived")
    return 0 if (killed == faults and survived == controls) else 1


if __name__ == "__main__":
    sys.exit(main())
