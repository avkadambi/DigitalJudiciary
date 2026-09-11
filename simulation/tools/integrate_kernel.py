#!/usr/bin/env python3
"""Release 5.11.0 — propagate the comparison kernel and the binding gate.

Idempotent. For every division pack and for Numerals:

  harness/engine.py          the 5.11.0 engine (kernel gate, three-valued facts,
                             gate outcomes), with the pack's own two header lines kept
  harness/binding_gate.py    the binding acceptance gate (std-lib)
  harness/run_conformance.py VC-51 (reduction + kernel self-test), VC-52 (silence
                             never binds), VC-53 (binding-gate verdict discipline)
  harness/mutation_matrix.py M2 re-anchored on the kernel; M26 (silence binds) and
                             M27 (tolerance ignored) added
  constitution/dimensions.json  an empty, valid declaration with the schema documented
  numerals: engine + binding_gate + FC-11 + MF7

    python3 tools/integrate_kernel.py [--check]
"""
from __future__ import annotations

import os
import sys

SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_PACK = os.path.join(SIM, "vetpoc-constitution-corpus")
PACKS = ["vetpoc-constitution-corpus", "semifab-constitution-corpus", "frontierllm-constitution-corpus",
         "dcvigil-constitution-corpus", "meridian-corpus"]
NUMERALS = os.path.join(SIM, "numerals")
TEMPLATES = os.path.join(SIM, "tools", "templates")
MARK = "Release 5.11.0 — the comparison kernel and the binding gate."


def read(p):
    return open(p).read()


def write(p, s):
    open(p, "w").write(s)


def with_header(new_engine: str, old_engine: str) -> str:
    """Keep the target pack's two identifying header lines (name, vendor)."""
    new_lines = new_engine.split("\n")
    old_lines = old_engine.split("\n")
    new_lines[1] = old_lines[1]
    # the vendor line: "Its purpose is that any ... can run the corpus against"
    for i, line in enumerate(old_lines[:20]):
        if line.startswith("Its purpose is that any"):
            for j, nl in enumerate(new_lines[:40]):
                if nl.startswith("Its purpose is that any"):
                    new_lines[j] = line
            break
    return "\n".join(new_lines)


DIMENSIONS_JSON = """{
  "_schema": "constitution/dimensions.json — magnitude factors and their tolerances (release 5.11.0)",
  "_note": "A factor listed here is read from a case's `values`, not from `facts`. weaker_when is declared, never inferred: 'lower' means a smaller value is the weaker case (coverage, retention days), 'higher' means a larger value is (latency regression, dose per kg). Coherence rules at load: D1 direction declared; D2 tolerance a number >= 0; D3 a factor of an ABSOLUTE provision carries tolerance 0; D4 every dimension is a factor of some provision. This corpus declares no dimensions yet: every factor is boolean and the kernel reduces to containment (VC-51). Adding one is a constitutional amendment (Legislate), not a configuration value.",
  "_example": {"changed_line_coverage_pct": {"weaker_when": "lower", "tolerance": 5.0, "unit": "%"}},
  "dimensions": {}
}
"""

M2_OLD = '''     "        if set(r.premise) <= facts:",
     "        if True:",
     "the distinguishing gate never distinguishes"),'''
M2_NEW = '''     "        if adm.status in ADMITTED:",
     "        if True:",
     "the distinguishing gate never distinguishes"),'''
M26_27 = '''    # M26-M27 target the 5.11.0 comparison kernel.
    ("M26", "fault",
     "    if unproven:\\n        return Admission(record.id, PREMISE_UNPROVEN",
     "    if False:\\n        return Admission(record.id, PREMISE_UNPROVEN",
     "silence is no longer a status: a record binds on a premise the case never established; VC-52 kills it"),
    ("M27", "fault",
     "    if shortfall > tol:",
     "    if shortfall > tol + 1:",
     "the tolerance is padded by one: on a boolean factor an absent premise factor no longer distinguishes; VC-51 kills it"),
]'''

FC11 = '''

@check("FC-11", "Silence never binds across divisions — silencing one premise factor of a foreign controlling record breaks the bind and names the cause")
def fc11(r):
    """5.11.0 three-valued facts, under federation. Every case bound by
    ANOTHER division's record is re-adjudicated with the first premise factor
    of that record marked unrecorded; the engine must not bind on it and must
    name premise_not_established unless an untouched record controls."""
    import binding_gate as BG
    store = [engine.Record.from_dict(x) if isinstance(x, dict) else x for x in r.result["store"]]
    oracle, answers = [], {}
    for c in r.cases:
        t = r.traces[c["id"]]
        if t.get("gate_outcome") != engine.GOVERNED or r.record_division.get(t["controlling"]) in (None, c["division"]):
            continue
        case = engine.case_from_dict(c)
        live = F.view_for(c["division"], [rec for rec in store if rec.ts < case.ts], r.record_division)
        ctrl = next(rec for rec in live if rec.id == t["controlling"])
        silenced = ctrl.premise[0]
        facts = set(case.facts)
        cand = engine.retrieve(case, live, r.params["theta"])
        quiet = engine.Case(**{**case.__dict__, "facts": [f for f in case.facts if f != silenced],
                               "unrecorded": list(case.unrecorded) + [silenced]})
        untouched = [rec for rec in cand if silenced not in rec.premise
                     and engine.admit(rec, quiet, r.provisions).admitted]
        top, _ = engine.order(untouched)
        if isinstance(top, engine.Record):
            exp, exp_ctl = engine.GOVERNED, top.id
        elif top == "none_tie":
            exp, exp_ctl = engine.NO_CONTROLLING, None
        else:
            exp, exp_ctl = engine.PREMISE_NOT_ESTABLISHED, None
        oracle.append(BG.OracleCase(case_id=c["id"], expected=exp, expected_controlling=exp_ctl,
                                    guard=(exp != engine.GOVERNED)))
        tr = engine.adjudicate(quiet, live, r.provisions, r.params["theta"])
        answers[c["id"]] = BG.Answer(tr["gate_outcome"], tr["controlling"] if tr["gate_outcome"] == engine.GOVERNED else None)
    d = BG.evaluate(oracle, lambda oc: answers[oc.case_id]).as_dict()
    ok = d["n_cases"] > 0 and d["false_binds"] == 0 and not d["guard_binds"] and d["by_verdict"]["missed_bind"] == 0 \\
        and d["by_verdict"]["abstain_diverged"] == 0
    return ok, (f"{d['n_cases']} cross-division binds silenced; {d['by_verdict']['abstain_agreed']} abstained "
                f"with cause premise_not_established, {d['by_verdict']['bind_agreed']} re-bound on an untouched "
                f"record; false binds {d['false_binds']}; binding-gate verdict {d['verdict']!r}"), \\
        [str(x) for x in d["guard_binds"][:3]]
'''

MF7 = '''    ("MF7", "fault", ENG, "    if unproven:\\n        return Admission(record.id, PREMISE_UNPROVEN",
     "    if False:\\n        return Admission(record.id, PREMISE_UNPROVEN",
     "silence binds: a foreign record governs a case that never established its premise (FC-11)"),
    ("MC1", "control",'''


def patch_pack(pack: str, check_only: bool) -> list:
    root = os.path.join(SIM, pack)
    changes = []
    src_engine = read(os.path.join(SOURCE_PACK, "harness", "engine.py"))
    eng_p = os.path.join(root, "harness", "engine.py")
    cur = read(eng_p)
    new = with_header(src_engine, cur) if root != SOURCE_PACK else src_engine
    if cur != new:
        changes.append("engine.py")
        if not check_only:
            write(eng_p, new)
    bg_src = read(os.path.join(SOURCE_PACK, "harness", "binding_gate.py"))
    bg_p = os.path.join(root, "harness", "binding_gate.py")
    if not os.path.exists(bg_p) or read(bg_p) != bg_src:
        changes.append("binding_gate.py")
        if not check_only:
            write(bg_p, bg_src)
    rc_p = os.path.join(root, "harness", "run_conformance.py")
    rc = read(rc_p)
    block = read(os.path.join(TEMPLATES, "vc51_53.py.frag")).rstrip("\n") + "\n\n"
    assert rc.count("\ndef s_leak(") == 1
    if MARK in rc:
        start = rc.index("\n\n# ---------------------------------------------------------------------------\n# " + MARK)
        end = rc.index("\ndef s_leak(")
        rc2 = rc[:start] + block + rc[end:]
    else:
        rc2 = rc.replace("\ndef s_leak(", block + "\ndef s_leak(", 1)
    if rc2 != rc:
        changes.append("run_conformance.py (VC-51..53)")
        if not check_only:
            write(rc_p, rc2)
    mm_p = os.path.join(root, "harness", "mutation_matrix.py")
    mm = read(mm_p)
    mm2 = mm
    if M2_OLD in mm2:
        mm2 = mm2.replace(M2_OLD, M2_NEW)
    if "M26" not in mm2:
        assert mm2.count('     "coverage"),\n]') == 1
        mm2 = mm2.replace('     "coverage"),\n]', '     "coverage"),\n' + M26_27)
        mm2 = mm2.replace("Twenty-four edits are faults", "Twenty-six edits are faults")
    if mm2 != mm:
        changes.append("mutation_matrix.py (M2, M26, M27)")
        if not check_only:
            write(mm_p, mm2)
    dim_p = os.path.join(root, "constitution", "dimensions.json")
    if not os.path.exists(dim_p):
        changes.append("constitution/dimensions.json")
        if not check_only:
            write(dim_p, DIMENSIONS_JSON)
    return changes


def patch_numerals(check_only: bool) -> list:
    changes = []
    src_engine = read(os.path.join(SOURCE_PACK, "harness", "engine.py"))
    eng_p = os.path.join(NUMERALS, "harness", "engine.py")
    cur = read(eng_p)
    new = with_header(src_engine, cur)
    if cur != new:
        changes.append("numerals/harness/engine.py")
        if not check_only:
            write(eng_p, new)
    bg_src = read(os.path.join(SOURCE_PACK, "harness", "binding_gate.py"))
    bg_p = os.path.join(NUMERALS, "harness", "binding_gate.py")
    if not os.path.exists(bg_p) or read(bg_p) != bg_src:
        changes.append("numerals/harness/binding_gate.py")
        if not check_only:
            write(bg_p, bg_src)
    fc_p = os.path.join(NUMERALS, "harness", "run_federation_checks.py")
    fc = read(fc_p)
    assert fc.count("\ndef main():") == 1
    if "FC-11" in fc:
        start = fc.index('\n\n@check("FC-11"')
        end = fc.index("\ndef main():")
        fc2 = fc[:start] + FC11.rstrip("\n") + "\n\n" + fc[end:]
    else:
        fc2 = fc.replace("\ndef main():", FC11.rstrip("\n") + "\n\n\ndef main():", 1)
    if fc2 != fc:
        changes.append("numerals FC-11")
        if not check_only:
            write(fc_p, fc2)
    mm_p = os.path.join(NUMERALS, "harness", "mutation_matrix.py")
    mm = read(mm_p)
    if "MF7" not in mm:
        assert mm.count('    ("MC1", "control",') == 1
        mm = mm.replace('    ("MC1", "control",', MF7, 1)
        changes.append("numerals MF7")
        if not check_only:
            write(mm_p, mm)
    dim_p = os.path.join(NUMERALS, "constitution", "dimensions.json")
    if not os.path.exists(dim_p):
        changes.append("numerals/constitution/dimensions.json")
        if not check_only:
            write(dim_p, DIMENSIONS_JSON)
    return changes


def main(argv=None):
    check_only = "--check" in (argv or sys.argv[1:])
    total = 0
    for pack in PACKS:
        ch = patch_pack(pack, check_only)
        total += len(ch)
        print(f"{pack}: {', '.join(ch) or 'up to date'}")
    ch = patch_numerals(check_only)
    total += len(ch)
    print(f"numerals: {', '.join(ch) or 'up to date'}")
    return 1 if (check_only and total) else 0



# ---------------------------------------------------------------------------
# benchmark/score.py — the binding-gate endpoint
# ---------------------------------------------------------------------------
SCORE_MARK = "the binding gate (release 5.11.0)"


def patch_score(pack: str, check_only: bool) -> list:
    p = os.path.join(SIM, pack, "benchmark", "score.py")
    s = read(p)
    if SCORE_MARK in s:
        return []
    block = read(os.path.join(TEMPLATES, "score_binding_gate.py.frag"))
    anchor = "    # ---- refusals --------------------------------------------------------\n"
    assert s.count(anchor) == 1, pack
    s = s.replace(anchor, block + anchor)
    s = s.replace('            "vs_reference_engine": oracle,\n',
                  '            "vs_reference_engine": oracle,\n            "binding_gate": binding,\n')
    s = s.replace('    w = "{:<8}{:>10}{:>9}{:>10}{:>8}{:>9}{:>9}{:>11}{:>10}{:>11}"',
                  '    w = "{:<8}{:>10}{:>9}{:>10}{:>8}{:>9}{:>9}{:>11}{:>10}{:>10}{:>11}"')
    s = s.replace('"transp.", "disclos.", "interp.acc", "no-call", "cost $"))',
                  '"transp.", "disclos.", "interp.acc", "falsebind", "no-call", "cost $"))')
    s = s.replace('    lines.append("-" * 97)', '    lines.append("-" * 107)')
    s = s.replace('            pct(s["vs_reference_engine"]["interpretive_subset"]["rate"]),\n',
                  '            pct(s["vs_reference_engine"]["interpretive_subset"]["rate"]),\n'
                  '            _fb(s.get("binding_gate")),\n')
    helper = '''

def _fb(bg):
    """The binding gate's false-bind column: 'k/n<=ub' or a dash when the arm never bound."""
    if not bg or bg.get("binds") in (None, 0):
        return "—"
    return f"{bg['false_binds']}/{bg['binds']}<={100*bg['false_bind_upper_bound']:.1f}%"

'''
    s = s.replace("\n\ndef summarise(results):", helper + "\ndef summarise(results):", 1)
    if not check_only:
        write(p, s)
    return ["benchmark/score.py (binding gate endpoint)"]


_main = main


def main(argv=None):  # noqa: F811
    rc = _main(argv)
    check_only = "--check" in (argv or sys.argv[1:])
    for pack in PACKS:
        ch = patch_score(pack, check_only)
        if ch:
            print(f"{pack}: {', '.join(ch)}")
            rc = 1 if check_only else rc
    return rc


# ---------------------------------------------------------------------------
# 5.12.0 — M28 (citation stance) on the mutation matrices
# ---------------------------------------------------------------------------
_M28_TAIL = ('     "citation stance is ignored: a record that merely FOLLOWED or DISTINGUISHED an older holding displaces it; VC-54 kills it"),\n]')
_M29_30 = ('     "citation stance is ignored: a record that merely FOLLOWED or DISTINGUISHED an older holding displaces it; VC-54 kills it"),\n'
           '    ("M29", "fault",\n'
           '     "    if adverse and not distinguishing:",\n'
           '     "    if False and adverse and not distinguishing:",\n'
           '     "the adverse-fact rung is removed: a permit binds a case carrying a violation it never saw; VC-55 kills it"),\n'
           '    ("M30", "fault",\n'
           '     "    if touched:\\n        return Admission(record.id, PRIOR_TEXT",\n'
           '     "    if False:\\n        return Admission(record.id, PRIOR_TEXT",\n'
           '     "the prior-text rung is removed: a holding on amended text still governs; VC-56 kills it"),\n]')


_S2_OLD = ('"def gate(candidates: list, case: Case) -> tuple:",\n'
           '     "def gate(candidates: list, case: Case) -> tuple:  # noqa",')
_S2_NEW = ('"def gate(candidates: list, case: Case, provisions: dict | None = None) -> tuple:",\n'
           '     "def gate(candidates: list, case: Case, provisions: dict | None = None) -> tuple:  # noqa",')


def patch_m29_30(pack: str, check_only: bool) -> list:
    p = os.path.join(SIM, pack, "harness", "mutation_matrix.py")
    s = read(p)
    out = []
    if _S2_OLD in s:
        out.append("mutation_matrix.py (S2 anchor for the 5.13.0 gate signature)")
        if not check_only:
            s = s.replace(_S2_OLD, _S2_NEW)
            write(p, s)
    _M30_TAIL = ('     "the prior-text rung is removed: a holding on amended text still governs; VC-56 kills it"),\n]')
    _M31 = ('     "the prior-text rung is removed: a holding on amended text still governs; VC-56 kills it"),\n'
            '    ("M31", "fault",\n'
            '     "    if withheld and trace[\\"admitted\\"]:",\n'
            '     "    if False and withheld and trace[\\"admitted\\"]:",\n'
            '     "a record is written on a premise the case never established, narrowed by silence; VC-52 kills it"),\n]')
    if "M31" not in s and _M30_TAIL in s:
        out.append("mutation_matrix.py (M31)")
        if not check_only:
            s = s.replace(_M30_TAIL, _M31).replace("Twenty-nine edits are faults", "Thirty edits are faults")
            write(p, s)
    if "M29" in s or _M28_TAIL not in s:
        return out
    if not check_only:
        write(p, s.replace(_M28_TAIL, _M29_30).replace("Twenty-seven edits are faults", "Twenty-nine edits are faults"))
    return ["mutation_matrix.py (M29, M30)"]


_M27_TAIL = '     "the tolerance is padded by one: on a boolean factor an absent premise factor no longer distinguishes; VC-51 kills it"),\n]'
_M28 = ('     "the tolerance is padded by one: on a boolean factor an absent premise factor no longer distinguishes; VC-51 kills it"),\n'
        '    ("M28", "fault",\n'
        '     "    return older.id in newer.cites and newer.stance_of(older.id) == STANCE_SUPERSEDED",\n'
        '     "    return older.id in newer.cites",\n'
        '     "citation stance is ignored: a record that merely FOLLOWED or DISTINGUISHED an older holding displaces it; VC-54 kills it"),\n]')


def patch_m28(pack: str, check_only: bool) -> list:
    p = os.path.join(SIM, pack, "harness", "mutation_matrix.py")
    s = read(p)
    if "M28" in s or _M27_TAIL not in s:
        return []
    if not check_only:
        write(p, s.replace(_M27_TAIL, _M28).replace("Twenty-six edits are faults", "Twenty-seven edits are faults"))
    return ["mutation_matrix.py (M28)"]


_main2 = main


def main(argv=None):  # noqa: F811
    rc = _main2(argv)
    check_only = "--check" in (argv or sys.argv[1:])
    for pack in PACKS:
        ch = patch_m28(pack, check_only) + patch_m29_30(pack, check_only)
        if ch:
            print(f"{pack}: {', '.join(ch)}")
            rc = 1 if check_only else rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
