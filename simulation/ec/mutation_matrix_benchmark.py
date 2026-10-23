"""
Benchmark mutation matrix: evidence that B-01..B-12 can fail (benchmark build §5).

    python3 simulation/ec/mutation_matrix_benchmark.py [--days 60] [--seed 97] [--jobs N]

Twelve faults FB-1..FB-12, one per check, and two controls that must survive.
Each is a `unittest.mock.patch` applied in a forked worker, which reruns the
benchmark fixture and the twelve checks; nothing on disk is edited.

    FB-1   the review draw is keyed on the act id (which carries the arm)        -> B-01
    FB-2   the corner draw includes the arm                                      -> B-02
    FB-3   H0 skips arm A's T2 CI check                                          -> B-03
    FB-4   false_reject is derived over all changes, not those reaching review   -> B-04
    FB-5   the request's approval is written into the act whatever the agent does -> B-05
    FB-6   r_expired seeds an unexpired token                                    -> B-06
    FB-7   the visibility class is recomputed from the arm's verdict             -> B-07
    FB-8   undetected exposure runs to the calendar quarter's audit day          -> B-08
    FB-9   harm weights come from the canon tier                                 -> B-09
    FB-10  the break-even re-scorer ignores the crunch multiplier                -> B-10
    FB-11  the reviewer also sees changes the gate blocked in HEC (review first)  -> B-11
    FB-12  the seed guard is removed                                             -> B-12
    CB-1   a ledger field no check reads (author_kind) is renamed                survives
    CB-2   the reviewer's docstring is changed                                    survives

`RESULT: k/12 faults killed, c/2 controls survived`; exit 1 otherwise.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import multiprocessing
import os
import random
import shutil
import sys
import tempfile
import time
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path[:] = [x for x in sys.path if os.path.abspath(x or os.curdir) != _HERE]
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import audit_sim, benchmark, breakeven, corners, harm, ledger, review_sim   # noqa: E402
from simulation.ec import run_benchmark_conformance as conf                                     # noqa: E402
from simulation.ec import run_year, stream                                                      # noqa: E402
from simulation.ec.agents import policy                                                         # noqa: E402
from simulation.ec.gate import Verdict                                                          # noqa: E402

_ORIG = {
    "review_stage": run_year.Run.review_stage, "overlay": stream.overlay, "rival": run_year.rival_decide,
    "process": run_year.Run.process, "prepass": run_year.Run.prepass, "answer_breach": policy.PolicyAgent._answer_breach,
    "seed_tokens": corners.seed_tokens, "build": ledger.build, "weight": harm.weight, "rescore": breakeven.rescore,
    "check_seeds": benchmark.check_seeds, "doc": review_sim.PeerReviewer.__doc__,
}
_CUR: dict = {}


def review_keyed_on_act(self, p, act, v, executed, rules_v, inv, day, human, imperm):
    cid = p.case_id
    p.case_id = p.act_id
    try:
        return _ORIG["review_stage"](self, p, act, v, executed, rules_v, inv, day, human, imperm)
    finally:
        p.case_id = cid


def overlay_with_arm(case, company, day, seq, arm, seed, rng, canon, archetype, corner=None):
    if corner is not None and random.Random(f"{seed}|{company}|{case['id']}|{arm}|corner").random() < 0.5:
        corner = None
    return _ORIG["overlay"](case, company, day, seq, arm, seed, rng, canon, archetype, corner=corner)


def process_marks_arm(self, *a, **k):
    _CUR["bench"] = self.bench_arm
    return _ORIG["process"](self, *a, **k)


def rival_skips_t2(p, canon, registry=None):
    v = _ORIG["rival"](p, canon, registry)
    if _CUR.get("bench") and v.reason_code == "t2_no_reason":
        return Verdict("allow", "clean", None, None, escalate=False, channel=None, event_type="legitimate_act")
    return v


def prepass_over_all_changes(self):
    import argparse as _a
    a2 = _a.Namespace(**vars(self.args))
    a2._bench_prepass = True
    tmp = tempfile.mkdtemp(prefix="bench_prepass_fb4_")
    try:
        r = run_year.Run(self.data, self.arm, self.seed, a2, tmp)
        n = k = 0
        for d in range(1, self.args.days + 1):
            c = r.run_day(d)
            n += c["proposals"]
            k += c["impermissible_proposed"]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    self.prepass_counts = {"reaching_review": n, "impermissible": k}
    return (k / n) if n else 0.0


def breach_writes_claim(self, ctx, target, driver, rng):
    claim = getattr(ctx.proposal_skeleton, "request_token_claim", None)
    if not claim:
        return _ORIG["answer_breach"](self, ctx, target, driver, rng)
    sk = ctx.proposal_skeleton
    sk.request_token_claim = None                 # run the agent's own choice ...
    try:
        act = _ORIG["answer_breach"](self, ctx, target, driver, rng)
    finally:
        sk.request_token_claim = claim
    act.token_claim = claim                       # ... and write the request's approval into the act regardless
    return act


def seed_unexpired(registries, canon, the_plan, agent_line):
    ids = _ORIG["seed_tokens"](registries, canon, the_plan, agent_line)
    for cid, s in the_plan.items():
        if s["type"] == "r_expired":
            for reg in registries:
                reg.tokens[s["token"]].expires_day = 999
    return ids


def review_stage_reads_verdict(self, p, act, v, executed, rules_v, inv, day, human, imperm):
    inv = dict(inv)
    if v.reason_code != "clean":
        inv["visibility"] = "V" if inv["impermissible"] else "S"
    return _ORIG["review_stage"](self, p, act, v, executed, rules_v, inv, day, human, imperm)


def build_exposure_to_quarter_end(run_dir, canon=None, weights_by_scheme=None, review_override=None, loaded=None):
    L = _ORIG["build"](run_dir, canon, weights_by_scheme, review_override, loaded)
    ends = audit_sim.quarter_end_days()                       # the full calendar's quarter ends
    for x in L:
        if x["found_by"] == "never" and x["day_executed"] is not None:
            x["exposure_days"] = ends[audit_sim.quarter_of(x["day_executed"])] - x["day_executed"]
    return L


def weight_from_tier(prov, scheme="rulebook", tier=None, entry_id=None):
    if scheme == "rulebook":
        return harm.TIER_WEIGHT.get(tier or "", 1)
    return _ORIG["weight"](prov, scheme, tier, entry_id)


def rescore_without_multipliers(run_dir, params, catch, ratio, cache, loaded=None):
    loaded = loaded or ledger.load_run(run_dir)
    rv_meta = (loaded["manifest"].get("benchmark") or {}).get("review") or {}
    reviewer = review_sim.PeerReviewer(params, rv_meta.get("profile") or "flat-edmundson", 0, "", catch=catch,
                                       false_flag_ratio=ratio)
    reviewer.set_p_imperm(rv_meta.get("p_imperm") or 0.0)

    def override(line, rv):
        inv = line["bench"]["invariant"]
        return rv["u"] < (reviewer.catch if inv["impermissible"] else reviewer.false_reject)
    pack = loaded["manifest"]["pack"]
    if pack not in cache:
        from simulation.ec.scorecard import weights_by_scheme
        canon = run_year.PackData(pack).fresh_canon()
        cache[pack] = (canon, weights_by_scheme(pack, canon))
    canon, w = cache[pack]
    from simulation.ec.scorecard import score_lines
    L = ledger.build(run_dir, canon, w, review_override=override, loaded=loaded)
    return score_lines(L, params, loaded["manifest"], loaded["bench_log"], loaded.get("registry"))


def review_before_gate(self, p, act, v, executed, rules_v, inv, day, human, imperm):
    if self.bench_arm in benchmark.GATED and rules_v.decision == "allow" and not executed:
        nv, ex, st = _ORIG["review_stage"](self, p, act, v, True, rules_v, inv, day, human, imperm)
        return v, False, st
    return _ORIG["review_stage"](self, p, act, v, executed, rules_v, inv, day, human, imperm)


def build_renames_author(run_dir, canon=None, weights_by_scheme=None, review_override=None, loaded=None):
    L = _ORIG["build"](run_dir, canon, weights_by_scheme, review_override, loaded)
    for x in L:
        x["author"] = x.pop("author_kind")
    return L


def patches_for(fid: str) -> list:
    if fid == "FB-1":
        return [mock.patch.object(run_year.Run, "review_stage", review_keyed_on_act)]
    if fid == "FB-2":
        return [mock.patch("simulation.ec.stream.overlay", overlay_with_arm),
                mock.patch("simulation.ec.run_year.streammod.overlay", overlay_with_arm)]
    if fid == "FB-3":
        return [mock.patch.object(run_year.Run, "process", process_marks_arm),
                mock.patch("simulation.ec.run_year.rival_decide", rival_skips_t2)]
    if fid == "FB-4":
        return [mock.patch.object(run_year.Run, "prepass", prepass_over_all_changes)]
    if fid == "FB-5":
        return [mock.patch.object(policy.PolicyAgent, "_answer_breach", breach_writes_claim)]
    if fid == "FB-6":
        return [mock.patch("simulation.ec.corners.seed_tokens", seed_unexpired)]
    if fid == "FB-7":
        return [mock.patch.object(run_year.Run, "review_stage", review_stage_reads_verdict)]
    if fid == "FB-8":
        return [mock.patch("simulation.ec.ledger.build", build_exposure_to_quarter_end)]
    if fid == "FB-9":
        return [mock.patch("simulation.ec.harm.weight", weight_from_tier)]
    if fid == "FB-10":
        return [mock.patch("simulation.ec.breakeven.rescore", rescore_without_multipliers)]
    if fid == "FB-11":
        return [mock.patch.object(run_year.Run, "review_stage", review_before_gate)]
    if fid == "FB-12":
        return [mock.patch("simulation.ec.benchmark.check_seeds", lambda arms, seeds: None)]
    if fid == "CB-1":
        return [mock.patch("simulation.ec.ledger.build", build_renames_author)]
    if fid == "CB-2":
        return [mock.patch.object(review_sim.PeerReviewer, "__doc__", "The reviewer. (docstring changed by CB-2)")]
    if fid == "baseline":
        return []
    raise KeyError(fid)


MUTANTS = [(f"FB-{i}", "fault", f"B-{i:02d}") for i in range(1, 13)] + [("CB-1", "control", None),
                                                                         ("CB-2", "control", None)]


def run_one(job: tuple) -> dict:
    fid, cfg = job
    out = os.path.join(cfg["tmp"], fid)
    t0 = time.time()
    failed, crash = [], None
    try:
        with contextlib.ExitStack() as stack:
            for p in patches_for(fid):
                stack.enter_context(p)
            try:
                fx = conf.Fixture(cfg["days"], cfg["seed"], out)
                res = conf.run_checks(fx, quiet=True)
                failed = [c["id"] for c in res["checks"] if not c["pass"]]
            except (Exception, SystemExit) as e:
                crash = f"{type(e).__name__}: {str(e)[:120]}"
    finally:
        assert run_year.Run.review_stage is _ORIG["review_stage"] and stream.overlay is _ORIG["overlay"]
        assert run_year.rival_decide is _ORIG["rival"] and run_year.Run.process is _ORIG["process"]
        assert run_year.Run.prepass is _ORIG["prepass"] and policy.PolicyAgent._answer_breach is _ORIG["answer_breach"]
        assert corners.seed_tokens is _ORIG["seed_tokens"] and ledger.build is _ORIG["build"]
        assert harm.weight is _ORIG["weight"] and breakeven.rescore is _ORIG["rescore"]
        assert benchmark.check_seeds is _ORIG["check_seeds"] and review_sim.PeerReviewer.__doc__ == _ORIG["doc"]
        shutil.rmtree(out, ignore_errors=True)
    return {"id": fid, "failed": failed, "crash": crash, "elapsed_s": round(time.time() - t0, 1)}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Benchmark mutation matrix FB-1..12 + 2 controls")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--seed", type=int, default=97)
    ap.add_argument("--jobs", type=int, default=max(1, os.cpu_count() or 1))
    ap.add_argument("--report", default=None)
    a = ap.parse_args(argv)
    tmp = tempfile.mkdtemp(prefix="bench_mutation_")
    cfg = {"days": a.days, "seed": a.seed, "tmp": tmp}
    jobs = [("baseline", cfg)] + [(m[0], cfg) for m in MUTANTS]
    t0 = time.time()
    print(f"Benchmark mutation matrix — vetpoc, seed {a.seed}, {a.days}-day fixture, {len(MUTANTS)} mutants + baseline")
    if a.jobs > 1:
        with multiprocessing.get_context("fork").Pool(a.jobs) as pool:
            results = pool.map(run_one, jobs, chunksize=1)
    else:
        results = [run_one(j) for j in jobs]
    by = {r["id"]: r for r in results}
    base = by["baseline"]
    n_faults = sum(1 for m in MUTANTS if m[1] == "fault")
    if base["crash"] or base["failed"]:
        print(f"baseline is not clean: crash={base['crash']} failed={base['failed']}")
        print(f"RESULT: 0/{n_faults} faults killed, 0/2 controls survived")
        return 1
    killed = survived = 0
    missing = []
    print(f"{'ID':7} {'KIND':8} {'OUTCOME':22} CHECKS KILLED")
    for fid, kind, expect in MUTANTS:
        r = by[fid]
        caught = bool(r["failed"]) or r["crash"] is not None
        if kind == "fault":
            killed += int(caught)
            if expect not in r["failed"]:
                missing.append((fid, expect))
            outcome = "KILLED" if caught else "SURVIVED (unexpected)"
        else:
            survived += int(not caught)
            outcome = "survived" if not caught else "KILLED (unexpected)"
        print(f"{fid:7} {kind:8} {outcome:22} {r['crash'] and 'CRASH ' + r['crash'] or ','.join(r['failed']) or '-'}"
              f"  ({r['elapsed_s']}s)")
    ok = killed == n_faults and survived == 2 and not missing
    if missing:
        print(f"faults that missed their check: {missing}")
    print(f"RESULT: {killed}/{n_faults} faults killed, {survived}/2 controls survived   ({time.time() - t0:.0f}s)")
    report = a.report or os.path.join(tmp, "mutation_matrix_benchmark.json")
    with open(report, "w") as fh:
        json.dump({"results": results, "ok": ok}, fh, indent=1)
    shutil.rmtree(tmp, ignore_errors=True) if a.report else None
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
