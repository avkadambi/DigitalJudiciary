"""
EC mutation matrix: evidence that EC-01..EC-12 can fail (DESIGN §7).

    python3 simulation/ec/mutation_matrix_ec.py [--pack vetpoc] [--days 45] [--seed 11]
        [--archetype pressure_sensitive] [--jobs N] [--keep]

Eight faults, F-EC-1..F-EC-8, and two controls that must survive. Every one is
a `unittest.mock.patch` of a function or constant in the ec package, applied
inside try/finally in a forked worker process; nothing on disk is edited and
the parent process never sees a patched module. Each worker reruns the short
pilot the conformance suite needs (one pack, `--days` days, the four arms, the
EC-11 repeat and the EC-07 archetype runs) and the twelve checks in process,
and reports which checks the fault killed.

    F-EC-1  canon.tier_of maps an absolute provision to T1                 -> EC-01
    F-EC-2  gate skips step 1 unless an audit is announced                 -> EC-02, EC-10
            (DESIGN's "gate skips step 1" and its EC-10 variant in one
            fault: the skip is what EC-02 sees, the audit condition is
            what the AST check and the twin-pair check see)
    F-EC-3  Registry.valid accepts a `claimed:` id as a token              -> EC-03
            (and consume tolerates it, else the run dies on a KeyError
            before any check can name the fault)
    F-EC-4  Registry.valid drops the reporting-line check                  -> EC-04
    F-EC-5  gate admits reason S at T2                                     -> EC-05
    F-EC-6  Bench.file drops holds (conflict holds and agent escalations)  -> EC-06
    F-EC-7  reconcile labels from the entry's own claim                    -> EC-07
    F-EC-8  write_gloss moves the entry's tier                             -> EC-08
    C-1     a run.jsonl field no check reads is renamed                    survives
    C-2     the gate's docstring is changed                                survives

Gate faults are compiled from the gate's own source with one anchored edit
(the anchor must occur exactly once), written to a temp file so that
`inspect.getsource` on the live function sees the mutant (EC-10's AST check
reads the function that is actually gated with, not the file in the repo).

The matrix passes when every fault is killed, both controls survive, and
every check DESIGN does not mark `control` (EC-09, EC-11, EC-12) is killed by
at least one fault. `RESULT: k/8 faults killed, c/2 controls survived`; exit 1
otherwise.
"""

from __future__ import annotations

import argparse
import contextlib
import inspect
import json
import multiprocessing
import os
import shutil
import sys
import tempfile
import time
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import calendar as cal             # noqa: E402
from simulation.ec import canon as canon_mod          # noqa: E402
from simulation.ec import doctrine                    # noqa: E402
from simulation.ec import escalate                    # noqa: E402
from simulation.ec import examen                      # noqa: E402
from simulation.ec import gate as gate_mod            # noqa: E402
from simulation.ec import metrics                     # noqa: E402,F401  (so its reconcile is patchable)
from simulation.ec import registry as registry_mod    # noqa: E402
from simulation.ec import run_year                    # noqa: E402
from simulation.ec import run_ec_conformance as conf  # noqa: E402

CONTROL_CHECKS = ("EC-09", "EC-11", "EC-12")
ALL_CHECKS = [cid for cid, _, _ in conf.CHECKS]


# ---------------------------------------------------------------------------
# Mutants
# ---------------------------------------------------------------------------


def gate_mutant(anchor: str, replacement: str, tmp_dir: str, tag: str):
    """The gate function recompiled from its own source with one edit, from a
    temp file so the live function's source is inspectable."""
    src = inspect.getsource(gate_mod.gate)
    if src.count(anchor) != 1:
        raise RuntimeError(f"{tag}: anchor occurs {src.count(anchor)} times, expected 1")
    path = os.path.join(tmp_dir, f"gate_{tag}.py")
    with open(path, "w") as fh:
        fh.write(src.replace(anchor, replacement))
    ns = dict(gate_mod.__dict__)
    with open(path) as fh:
        exec(compile(fh.read(), path, "exec"), ns)
    return ns["gate"]


def tier_of_absolute_t1(prov: dict):
    tier, office = _ORIG["tier_of"](prov)
    if prov.get("absolute"):
        return "T1", "office:compliance"
    return tier, office


def valid_accepts_claims(self, token_id, entry, agent_line, day, canon_version):
    if isinstance(token_id, str) and token_id.startswith("claimed:"):
        return True, "ok"
    return _ORIG["valid"](self, token_id, entry, agent_line, day, canon_version)


def consume_tolerant(self, token_id, day, act_id):
    if token_id not in self.tokens:
        self.events.append({"event": "consume", "day": day, "token": token_id, "act_id": act_id,
                            "act_class": None, "single_use": True})
        return None
    return _ORIG["consume"](self, token_id, day, act_id)


def valid_no_line_check(self, token_id, entry, agent_line, day, canon_version):
    ok, why = _ORIG["valid"](self, token_id, entry, agent_line, day, canon_version)
    if not ok and why == "issuer_inside_reporting_line":
        return (False, "codified_class") if entry.gloss.codified else (True, "ok")
    return ok, why


def file_drops_holds(self, esc):
    if esc.reason_code in ("conflict_hold", "agent_escalated"):   # every hold, as EC-06 counts them
        return None
    return _ORIG["file"](self, esc)


def reconcile_trusts_entry(entries, events):
    by_act = {}
    for en in entries:
        by_act.setdefault(en.act_id, en)
    labels, counts = {}, {k: 0 for k in examen.LABELS}
    reportable = reported = disclosed = 0
    for ev in events:
        en = by_act.get(ev.act_id)
        if en is None or en.reported_event == "none":
            lab = "nothing_to_disclose"
        else:
            lab = "discloses"          # the entry's own claim, never checked against the event
        labels[ev.act_id] = lab
        counts[lab] += 1
        reportable += int(examen.is_reportable(ev))
        reported += int(en is not None and en.reported_event != "none")
        disclosed += int(lab == "discloses")
    return examen.DFReport(recall=(disclosed / reportable) if reportable else None,
                           precision=(disclosed / reported) if reported else None,
                           label_counts=counts, labels=labels, reportable=reportable, reported=reported,
                           disclosed=disclosed)


def write_gloss_moves_tier(canon, entry_id, holding, day):
    _ORIG["write_gloss"](canon, entry_id, holding, day)
    e = canon.entry(entry_id)
    e.tier = {"T0": "T1", "T1": "T2", "T2": "T3", "T3": "T3"}[e.tier]


def process_renames_field(self, p, case, agent_rng, day, view):
    line, rec = _ORIG["process"](self, p, case, agent_rng, day, view)
    line["believes_watched"] = line.pop("believes_monitored")
    return line, rec


_ORIG = {
    "tier_of": canon_mod.tier_of,
    "valid": registry_mod.Registry.valid,
    "consume": registry_mod.Registry.consume,
    "file": escalate.Bench.file,
    "write_gloss": doctrine.write_gloss,
    "process": run_year.Run.process,
}


def patches_for(fid: str, tmp_dir: str) -> list:
    """The mock.patch objects one fault applies."""
    if fid == "F-EC-1":
        return [mock.patch("simulation.ec.canon.tier_of", tier_of_absolute_t1)]
    if fid == "F-EC-2":
        g = gate_mutant("        if e.tier == \"T0\" and contravenes(e, act, facts):",
                        "        if e.tier == \"T0\" and contravenes(e, act, facts) and p.audit_announced:",
                        tmp_dir, "f2")
        return [mock.patch("simulation.ec.gate.gate", g), mock.patch("simulation.ec.run_year.gate", g)]
    if fid == "F-EC-3":
        return [mock.patch.object(registry_mod.Registry, "valid", valid_accepts_claims),
                mock.patch.object(registry_mod.Registry, "consume", consume_tolerant)]
    if fid == "F-EC-4":
        return [mock.patch.object(registry_mod.Registry, "valid", valid_no_line_check)]
    if fid == "F-EC-5":
        g = gate_mutant("            if act.stated_reason not in e.gloss.admitted_reasons:",
                        "            if act.stated_reason not in e.gloss.admitted_reasons and act.stated_reason != \"S\":",
                        tmp_dir, "f5")
        return [mock.patch("simulation.ec.gate.gate", g), mock.patch("simulation.ec.run_year.gate", g)]
    if fid == "F-EC-6":
        return [mock.patch.object(escalate.Bench, "file", file_drops_holds)]
    if fid == "F-EC-7":
        return [mock.patch("simulation.ec.examen.reconcile", reconcile_trusts_entry),
                mock.patch("simulation.ec.run_year.reconcile", reconcile_trusts_entry),
                mock.patch("simulation.ec.metrics.reconcile", reconcile_trusts_entry)]
    if fid == "F-EC-8":
        return [mock.patch("simulation.ec.doctrine.write_gloss", write_gloss_moves_tier),
                mock.patch("simulation.ec.run_year.write_gloss", write_gloss_moves_tier)]
    if fid == "C-1":
        return [mock.patch.object(run_year.Run, "process", process_renames_field)]
    if fid == "C-2":
        return [mock.patch.object(gate_mod.gate, "__doc__", "Evaluate the proposal. (docstring changed by C-2)")]
    if fid == "baseline":
        return []
    raise KeyError(fid)


MUTANTS = [
    ("F-EC-1", "fault", "tier rule maps absolute -> T1", ("EC-01",)),
    ("F-EC-2", "fault", "gate skips step 1 unless an audit is announced", ("EC-02", "EC-10")),
    ("F-EC-3", "fault", "`valid` accepts `claimed:` ids", ("EC-03",)),
    ("F-EC-4", "fault", "reporting-line check removed", ("EC-04",)),
    ("F-EC-5", "fault", "S admitted at T2", ("EC-05",)),
    ("F-EC-6", "fault", "bench drops holds", ("EC-06",)),
    ("F-EC-7", "fault", "reconcile reads a carried label", ("EC-07",)),
    ("F-EC-8", "fault", "write_gloss bumps tier", ("EC-08",)),
    ("C-1", "control", "run.jsonl field believes_monitored renamed (no check reads it)", ()),
    ("C-2", "control", "gate docstring changed", ()),
]


# ---------------------------------------------------------------------------
# One worker: apply, run, restore
# ---------------------------------------------------------------------------


def run_one(job: tuple) -> dict:
    fid, cfg = job
    out = os.path.join(cfg["tmp"], fid)
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    failed, crash = [], None
    try:
        with contextlib.ExitStack() as stack:
            for p in patches_for(fid, out):
                stack.enter_context(p)
            try:
                suite = conf.Suite(cfg["pack"], cfg["seed"], cfg["archetype"], cfg["days"], cfg["ec07_days"], "A",
                                   None, out)
                res = conf.run_checks(suite, quiet=True)
                failed = [c["id"] for c in res["checks"] if not c["pass"]]
                details = {c["id"]: c["detail"] for c in res["checks"] if not c["pass"]}
            except Exception as e:        # a fault that crashes the run is a kill without a named check
                crash = f"{type(e).__name__}: {str(e)[:120]}"
                details = {}
    finally:
        # Leaving the ExitStack restored every patch; verify from the originals.
        assert canon_mod.tier_of is _ORIG["tier_of"]
        assert registry_mod.Registry.valid is _ORIG["valid"]
        assert registry_mod.Registry.consume is _ORIG["consume"]
        assert escalate.Bench.file is _ORIG["file"]
        assert doctrine.write_gloss is _ORIG["write_gloss"] and run_year.write_gloss is _ORIG["write_gloss"]
        assert run_year.Run.process is _ORIG["process"]
        assert run_year.gate is gate_mod.gate and gate_mod.gate.__code__.co_filename.endswith("gate.py")
        assert examen.reconcile is run_year.reconcile
        if not cfg["keep"]:
            shutil.rmtree(out, ignore_errors=True)
    return {"id": fid, "failed": failed, "crash": crash, "details": details, "elapsed_s": round(time.time() - t0, 1)}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="EC mutation matrix F-EC-1..8 + 2 controls")
    ap.add_argument("--pack", default="vetpoc")
    ap.add_argument("--days", type=int, default=45)
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--archetype", default="pressure_sensitive")
    ap.add_argument("--ec07-days", type=int, default=cal.DAYS)
    ap.add_argument("--jobs", type=int, default=max(1, os.cpu_count() or 1))
    ap.add_argument("--keep", action="store_true", help="keep every worker's run directory")
    ap.add_argument("--report", default=None, help="JSON report path (default: simulation/ec/results/mutation_matrix_ec.json)")
    return ap.parse_args(argv)


def main(argv=None) -> int:
    a = parse_args(argv)
    tmp = tempfile.mkdtemp(prefix="ec_mutation_")
    cfg = {"pack": a.pack, "seed": a.seed, "archetype": a.archetype, "days": a.days, "ec07_days": a.ec07_days,
           "tmp": tmp, "keep": a.keep}
    jobs = [("baseline", cfg)] + [(m[0], cfg) for m in MUTANTS]
    t0 = time.time()
    print(f"EC mutation matrix — pack {a.pack}, seed {a.seed}, archetype {a.archetype}, {a.days}-day pilot, "
          f"{len(MUTANTS)} mutants + baseline, {a.jobs} worker(s)")
    if a.jobs > 1:
        ctx = multiprocessing.get_context("fork")
        with ctx.Pool(a.jobs) as pool:
            results = pool.map(run_one, jobs, chunksize=1)
    else:
        results = [run_one(j) for j in jobs]
    by_id = {r["id"]: r for r in results}

    base = by_id["baseline"]
    if base["crash"] or base["failed"]:
        print(f"baseline is not clean: crash={base['crash']} failed={base['failed']}")
        print("RESULT: 0/8 faults killed, 0/2 controls survived")
        return 1
    print(f"baseline: 12/12 in {base['elapsed_s']}s")

    killed = survived = 0
    killers: dict = {c: [] for c in ALL_CHECKS}
    rows = []
    for fid, kind, what, expect in MUTANTS:
        r = by_id[fid]
        caught = bool(r["failed"]) or r["crash"] is not None
        if kind == "fault":
            outcome = "KILLED" if caught else "SURVIVED (unexpected)"
            killed += int(caught)
        else:
            outcome = "survived" if not caught else "KILLED (unexpected)"
            survived += int(not caught)
        for c in r["failed"]:
            killers[c].append(fid)
        hit = r["crash"] and f"CRASH {r['crash']}" or ",".join(r["failed"]) or "-"
        missing = [c for c in expect if c not in r["failed"]]
        rows.append((fid, kind, outcome, hit, what, missing, r["elapsed_s"]))

    print()
    print(f"{'ID':8} {'KIND':8} {'OUTCOME':22} {'CHECKS KILLED':22} WHAT IT BREAKS")
    print("-" * 110)
    for fid, kind, outcome, hit, what, missing, el in rows:
        note = f"  [expected {','.join(missing)} not killed]" if missing else ""
        print(f"{fid:8} {kind:8} {outcome:22} {hit:22} {what}{note}  ({el}s)")
    print("-" * 110)
    print(f"{'CHECK':8} KILLED BY")
    uncovered = []
    for c in ALL_CHECKS:
        tag = "control" if c in CONTROL_CHECKS else ""
        ks = ",".join(killers[c]) or "-"
        if c not in CONTROL_CHECKS and not killers[c]:
            uncovered.append(c)
        print(f"{c:8} {ks:40} {tag}")
    print("-" * 110)
    faults = sum(1 for m in MUTANTS if m[1] == "fault")
    controls = sum(1 for m in MUTANTS if m[1] == "control")
    expected_missing = [(fid, m) for fid, kind, _o, _h, _w, m, _e in rows if kind == "fault" and m]
    ok = killed == faults and survived == controls and not uncovered and not expected_missing
    if uncovered:
        print(f"checks with no killing fault: {uncovered}")
    if expected_missing:
        print(f"faults that missed the check DESIGN names: {expected_missing}")
    print(f"RESULT: {killed}/{faults} faults killed, {survived}/{controls} controls survived   ({time.time() - t0:.0f}s)")
    report = a.report or os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "mutation_matrix_ec.json")
    os.makedirs(os.path.dirname(report), exist_ok=True)
    with open(report, "w") as fh:
        json.dump({"pack": a.pack, "seed": a.seed, "archetype": a.archetype, "days": a.days,
                   "baseline": base, "mutants": [by_id[m[0]] | {"kind": m[1], "what": m[2], "expected": list(m[3])}
                                                 for m in MUTANTS],
                   "killers": killers, "ok": ok, "elapsed_s": round(time.time() - t0, 1)}, fh, indent=1)
    if not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
