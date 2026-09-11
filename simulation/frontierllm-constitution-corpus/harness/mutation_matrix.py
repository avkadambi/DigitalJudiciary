"""
Mutation matrix — evidence that the conformance suite discriminates.

A suite that passes is worth nothing unless it can fail. This applies single-line
edits to the reference engine one at a time, each anchored on a string that must
occur exactly once in its file, re-runs the whole suite after each edit, restores
the file, and verifies the restoration by SHA-256 before proceeding.

Thirty edits are faults and are expected to be caught. Four are semantic no-ops
and are expected to survive; each records a real fact about the corpus rather
than padding the denominator.

    python3 harness/mutation_matrix.py
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ENGINE = os.path.join(HERE, "engine.py")
EXTENSIONS = os.path.join(HERE, "extensions.py")
DISCRIMINATING = os.path.join(ROOT, "benchmark", "discriminating.py")
JUSTIFICATION = os.path.join(ROOT, "benchmark", "justification.py")
CHANGES = os.path.join(ROOT, "generator", "changes.py")
COVERAGE = os.path.join(HERE, "coverage.py")
TARGETS = {"extensions": EXTENSIONS, "discriminating": DISCRIMINATING,
           "justification": JUSTIFICATION, "changes": CHANGES,
           "coverage": COVERAGE}
SUITE = os.path.join(HERE, "run_conformance.py")

# (id, kind, anchor, replacement, what it breaks / records)
# Mutants M13-M18 target harness/extensions.py rather than the engine:
# a check on machinery that no mutant can break is a check that has
# never been shown to be able to fail.
MUTANTS = [
    ("M1", "fault",
     'AUTH_RANK = {"judges": 1, "riskowner": 2}',
     'AUTH_RANK = {"judges": 2, "riskowner": 1}',
     "the authority key is inverted: a judge outranks the risk owner"),
    ("M2", "fault",
     "        if adm.status in ADMITTED:",
     "        if True:",
     "the distinguishing gate never distinguishes"),
    ("M3", "fault",
     "        if p.absolute and violates(facts, p):",
     "        if False and p.absolute and violates(facts, p):",
     "the A6 absolute short-circuit is disabled"),
    ("M4", "fault",
     "    if case.contest_to >= 2:\n        trace[\"admitted\"] = True",
     "    if case.contest_to >= 0:\n        trace[\"admitted\"] = True",
     "the Definition 7 admission bar is removed: uncontested decisions become law"),
    ("M5", "fault",
     "        and not r.lapsed_at(case.ts)",
     "        and True",
     "the lapse filter is removed from retrieval"),
    ("M6", "fault",
     "    if newer.ts <= older.ts:",
     "    if newer.ts >= older.ts:",
     "the recency key is inverted: the oldest survivor wins"),
    ("M7", "fault",
     "            keys.append(\"ts\")",
     "            pass",
     "the recency key is applied but never recorded in the trail"),
    ("M8", "fault",
     "                s.scope_domain == r.scope_domain and s.scope_width < r.scope_width",
     "                s.scope_domain == r.scope_domain and s.scope_width > r.scope_width",
     "the scope key is inverted: the widest holding wins"),
    ("M9", "fault",
     "    return older.id in newer.cites",
     "    return True",
     "express supersession is dropped: a newer holding may silently reverse one it contradicts"),
    ("M10", "fault",
     "        trace[\"expiry_set\"] = True",
     "        trace[\"expiry_set\"] = False",
     "a risk acceptance is granted with no mandatory expiry"),
    ("M11", "fault",
     "    if case.contest_to >= 4:",
     "    if case.contest_to >= 3:",
     "risk acceptance fires before escalation is exhausted"),
    ("M12", "fault",
     "            tr[\"consulted\"] = []\n            tr[\"distinguished\"] = []",
     "            tr[\"distinguished\"] = []\n            tr[\"distinguished\"] = []",
     "a consolidation member retrieves instead of being disposed by citation"),
    ("S1", "control",
     "    prem = set(record.premise)",
     "    prem = set(list(record.premise))",
     "nothing — a pure no-op"),
    ("S2", "control",
     "def gate(candidates: list, case: Case, provisions: dict | None = None) -> tuple:",
     "def gate(candidates: list, case: Case, provisions: dict | None = None) -> tuple:  # noqa",
     "nothing — a comment"),
    ("S3", "control",
     "THETA_DEFAULT = 0.25",
     "THETA_DEFAULT = 0.20",
     "records a fact: lowering the retrieval threshold changes no disposition, "
     "because premise coverage cannot cost a controlling record"),
    ("S4", "control",
     "        top = max(r.depth for r in pool)",
     "        top = max([r.depth for r in pool])",
     "nothing — a generator expression rewritten as a list comprehension. "
     "Whether the depth key is ever decisive is a fact about the corpus, "
     "reported by VC-05 rather than claimed here"),
    ("M13", "fault",
     "        live = [r for r in store if not r.lapsed_at(trace.get(\"ts\", 0) or 0)]",
     "        store.append(store[0]) if store else None\n"
     "        live = [r for r in store if not r.lapsed_at(trace.get(\"ts\", 0) or 0)]",
     "the Reporter writes to the store it observes (Definition 17, R1)",
     "extensions"),
    ("M14", "fault",
     "        advisory = engine.adjudicate(case, list(store), provisions, theta)",
     "        advisory = engine.adjudicate(case, store, provisions, theta)\n"
     "        store.append(store[-1])",
     "the docket audit appends to the store, so it is no longer neutral (Prop. 7(i))",
     "extensions"),
    ("M15", "fault",
     '    return _adjudicated(h) and h["contested"]',
     "    return _adjudicated(h)",
     "A_contest admits uncontested arrivals: the admission bar is gone",
     "extensions"),
    ("M16", "fault",
     "    if auth_class == \"riskowner\":\n        return pool[0]",
     "    if auth_class == \"riskowner\":\n        return \"riskowner:unappointed\"",
     "a record names a resolver the constitution never appointed (CC-01/CC-02)",
     "engine"),
    ("M17", "fault",
     '    return {"decision": fresh,\n            "shown": [r.id for r in survivors][:3],\n            "controlling": None,          # advice does not control\n            "expressible_controlling": False}',
     '    return {"decision": fresh,\n            "shown": [r.id for r in survivors][:3],\n            "controlling": survivors[0].id if survivors else None,\n            "expressible_controlling": True}',
     "B_mem is credited with expressing Controlling, which Proposition 3 denies",
     "extensions"),
    ("M18", "fault",
     '            "is_annotation_only": True,',
     '            "is_annotation_only": False,',
     "an audit finding stops being an annotation and claims force (Definition 19)",
     "extensions"),

    # M19-M21 target benchmark/discriminating.py and benchmark/stream.py. The
    # 5.8.1 overlay and the widened guard set shipped with checks that had never
    # been shown able to fail; these three show it.
    ("M19", "fault",
     '                "scenario": _placed(cm, prov, facts, s),',
     '                "scenario": {"change": s["title"], "change_kind": "violating",\n'
     '                             "area": "org", "service": "svc:core"},',
     "the discriminating suite announces its own trap in the change description",
     "discriminating"),
    ("M20", "fault",
     '                "canary": _vocab.canary_for(cid),',
     '                "canary": None,',
     "scenario cases ship without a contamination canary",
     "discriminating"),
    # The first M21 mutated resolve()'s picking branch. It survived, and the
    # reason is worth recording: this pack pins all eight families to named
    # provisions, so that branch never executes here — the mutant was
    # unreachable rather than undetected. It is replaced by one that is
    # reachable in every pack.
    ("M21", "fault",
     '        if s.get("drop_premise") and recs:',
     '        if False and recs:',
     "S3 stops distinguishing: the fact the exception turned on is left in place",
     "discriminating"),

    # M22-M23 target benchmark/justification.py, the disclosure overlay.
    ("M22", "fault",
     '    c["scenario"]["author_note"] = note',
     '    c["scenario"]["author_note"] = note\n    c["facts"] = sorted(set(c["facts"]) | {note})',
     "the author's note enters the factor model, so prose becomes a fact",
     "justification"),
    ("M23", "fault",
     '        return MISREPRESENTS if violating else SILENT',
     '        return MISREPRESENTS',
     "a truthful note over a clean change is labelled a misrepresentation",
     "justification"),

    # M24 targets generator/changes.py: the development-change guard.
    ("M24", "fault",
     '    if any(t.startswith(x) for x in DEVELOPMENT_EXEMPTIONS):',
     '    if True:',
     "the development-change guard passes everything, so a runtime business "
     "transaction can re-enter the corpus",
     "changes"),
    ("M25", "fault",
     "            if counts[s][m] == 0:",
     "            if False:",
     "the scenario-coverage checker reports no empty cell; VC-50's self-test kills it",
     "coverage"),
    # M26-M27 target the 5.11.0 comparison kernel.
    ("M26", "fault",
     "    if unproven:\n        return Admission(record.id, PREMISE_UNPROVEN",
     "    if False:\n        return Admission(record.id, PREMISE_UNPROVEN",
     "silence is no longer a status: a record binds on a premise the case never established; VC-52 kills it"),
    ("M27", "fault",
     "    if shortfall > tol:",
     "    if shortfall > tol + 1:",
     "the tolerance is padded by one: on a boolean factor an absent premise factor no longer distinguishes; VC-51 kills it"),
    ("M28", "fault",
     "    return older.id in newer.cites and newer.stance_of(older.id) == STANCE_SUPERSEDED",
     "    return older.id in newer.cites",
     "citation stance is ignored: a record that merely FOLLOWED or DISTINGUISHED an older holding displaces it; VC-54 kills it"),
    ("M29", "fault",
     "    if adverse and not distinguishing:",
     "    if False and adverse and not distinguishing:",
     "the adverse-fact rung is removed: a permit binds a case carrying a violation it never saw; VC-55 kills it"),
    ("M30", "fault",
     "    if touched:\n        return Admission(record.id, PRIOR_TEXT",
     "    if False:\n        return Admission(record.id, PRIOR_TEXT",
     "the prior-text rung is removed: a holding on amended text still governs; VC-56 kills it"),
    ("M31", "fault",
     "    if withheld and trace[\"admitted\"]:",
     "    if False and withheld and trace[\"admitted\"]:",
     "a record is written on a premise the case never established, narrowed by silence; VC-52 kills it"),
]


BACKUP_SUFFIX = ".mutation-backup"


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def recover():
    """Undo a mutation left behind by a run that was killed outright.

    `finally` restores the file when the process gets to run its cleanup. It
    does not when the process is killed — a hard timeout, an OOM, a closed
    container — and that is not hypothetical: a batch run of the five packs hit
    a two-minute limit mid-mutant and left a pack's benchmark/discriminating.py
    carrying the M19 fault on disk, where the next conformance run found it as a
    real failure. So every mutation now writes the pristine file beside itself
    first, and every run starts by putting back anything it finds.
    """
    for target in (ENGINE, EXTENSIONS, DISCRIMINATING, JUSTIFICATION, CHANGES, COVERAGE):
        bak = target + BACKUP_SUFFIX
        if os.path.exists(bak):
            original = open(bak).read()
            if open(target).read() != original:
                print(f"recovered {os.path.basename(target)} from an interrupted run")
            open(target, "w").write(original)
            os.remove(bak)
            _purge_bytecode(target)


def _purge_bytecode(target):
    """Drop the target's compiled bytecode. A file restored with an old mtime
    (a manual `mv` of the sidecar, say) can be shadowed by the mutant's newer
    .pyc, and CPython would keep running the mutant on an intact source."""
    cache = os.path.join(os.path.dirname(target), "__pycache__")
    stem = os.path.splitext(os.path.basename(target))[0] + "."
    if os.path.isdir(cache):
        for name in os.listdir(cache):
            if name.startswith(stem):
                try:
                    os.remove(os.path.join(cache, name))
                except OSError:
                    pass


def run_suite():
    p = subprocess.run([sys.executable, SUITE], capture_output=True, text=True, cwd=ROOT)
    for line in p.stdout.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip(), p.returncode
    return "CRASH", p.returncode


def main():
    recover()
    base_result, base_code = run_suite()
    print(f"baseline: {base_result}")
    if base_code != 0:
        print("baseline is not clean; aborting")
        return 1

    killed = survived = 0
    rows = []
    for m in MUTANTS:
        mid, kind, anchor, repl, what = m[:5]
        target = TARGETS.get(m[5] if len(m) > 5 else None, ENGINE)
        original = open(target).read()
        baseline_hash = sha(target)
        occurrences = original.count(anchor)
        if occurrences != 1:
            rows.append((mid, kind, what, f"ANCHOR x{occurrences}", "ERROR"))
            continue
        # Restore in a finally block. An interrupted run — a timeout, a
        # keyboard interrupt — used to leave the mutated file on disk, and the
        # next run then reported the anchor missing rather than the corruption.
        bak = target + BACKUP_SUFFIX
        try:
            open(bak, "w").write(original)       # survives a kill; see recover()
            open(target, "w").write(original.replace(anchor, repl))
            result, code = run_suite()
        finally:
            open(target, "w").write(original)
            assert sha(target) == baseline_hash, "restoration failed"
            if os.path.exists(bak):
                os.remove(bak)

        caught = code != 0 or result == "CRASH"
        if kind == "fault":
            outcome = "KILLED" if caught else "SURVIVED (unexpected)"
            killed += 1 if caught else 0
        else:
            outcome = "survived" if not caught else "KILLED (unexpected)"
            survived += 1 if not caught else 0
        rows.append((mid, kind, what, result, outcome))

    print()
    print(f"{'ID':5} {'KIND':8} {'SUITE':8} {'OUTCOME':22} WHAT IT BREAKS")
    print("-" * 110)
    for mid, kind, what, result, outcome in rows:
        print(f"{mid:5} {kind:8} {result:8} {outcome:22} {what}")
    print("-" * 110)
    faults = sum(1 for m in MUTANTS if m[1] == "fault")
    controls = sum(1 for m in MUTANTS if m[1] == "control")
    print(f"RESULT: {killed}/{faults} faults killed, {survived}/{controls} controls survived")
    ok = killed == faults and survived == controls
    # Final restoration check.
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
