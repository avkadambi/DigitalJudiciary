"""
Benchmark conformance suite B-01 .. B-12 (benchmark build §5), computed from
executed runs on a 60-day vetpoc fixture at seed 97, deterministic governance,
no keys.

    python3 simulation/ec/run_benchmark_conformance.py [--days 60] [--seed 97] [--out DIR]

The fixture: arms A, C, D, H0, HEC, HDJ, HECDJ with the corner overlay at
0.08 (policy:pressure_sensitive); A and H0 with the reviewer at catch 0,
false-flag ratio 0 and audits off (B-03); H0 under the crunch profile (B-10);
and arm A with the overlay off (B-05). Prints `B-nn  PASS/FAIL  name  detail`
and `RESULT: n/12`; exit 1 on any FAIL.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path[:] = [x for x in sys.path if os.path.abspath(x or os.curdir) != _HERE]
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import audit_sim, authority, benchmark, breakeven, corners, harm, ledger   # noqa: E402
from simulation.ec import review_sim, run_year, scorecard                                     # noqa: E402

ARMS = ("A", "C", "D", "H0", "HEC", "HDJ", "HECDJ")
H_ARMS = ("H0", "HEC", "HDJ", "HECDJ")
CHECKS: list = []


def check(cid, name):
    def deco(fn):
        CHECKS.append((cid, name, fn))
        return fn
    return deco


def _lines(d: str) -> list:
    with open(os.path.join(d, "run.jsonl")) as fh:
        return [json.loads(x) for x in fh if x.strip()]


def _json(d: str, name: str):
    with open(os.path.join(d, name)) as fh:
        return json.load(fh)


class Fixture:
    def __init__(self, days: int = 60, seed: int = 97, out: str | None = None, quiet: bool = True):
        self.days, self.seed = days, seed
        self.out = out or tempfile.mkdtemp(prefix="bench_conf_")
        self.params = review_sim.load_params()
        self.timings = {}
        base = ["--packs", "vetpoc", "--seeds", str(seed), "--days", str(days), "--agent", "policy:pressure_sensitive",
                "--quiet"]
        zero = dict(self.params)
        zero = json.loads(json.dumps(self.params))
        zero["review"]["catch"]["value"] = 0.0
        zero["review"]["false_flag_ratio"]["value"] = 0.0
        os.makedirs(self.out, exist_ok=True)
        self.zero_params = os.path.join(self.out, "zero_params.json")
        with open(self.zero_params, "w") as fh:
            json.dump(zero, fh)
        for tag, extra in (("main", ["--arms", ",".join(ARMS), "--corner-overlay", "0.08"]),
                           ("zero", ["--arms", "A,H0", "--corner-overlay", "0.08", "--benchmark-params", self.zero_params,
                                     "--audit", "0"]),
                           ("crunch", ["--arms", "H0", "--corner-overlay", "0.08", "--review-profile", "crunch"]),
                           ("off", ["--arms", "A"])):
            t0 = time.time()
            run_year.main(base + ["--out", os.path.join(self.out, tag)] + extra)
            self.timings[tag] = round(time.time() - t0, 2)

    def run(self, tag: str, arm: str) -> str:
        return os.path.join(self.out, tag, "vetpoc", arm, f"seed-{self.seed}")


# ---------------------------------------------------------------------------


def _tokens(reg: dict) -> dict:
    t = reg.get("tokens") or {}
    return {x["id"]: x for x in t} if isinstance(t, list) else dict(t)


def _reviews(d: str) -> dict:
    return {(l["proposal"]["case_id"], l["proposal"]["twin_of"] is not None): l for l in _lines(d)
            if l.get("bench") and l["bench"]["review"]}


@check("B-01", "common random numbers (review): a change reaching review in two H arms has the same draw, and the same outcome where the arms' rates agree")
def b01(f: Fixture):
    rv = {a: _reviews(f.run("main", a)) for a in H_ARMS}
    bad, n = [], 0
    for a in H_ARMS[1:]:
        for k in set(rv["H0"]) & set(rv[a]):
            n += 1
            x, y = rv["H0"][k]["bench"]["review"], rv[a][k]["bench"]["review"]
            if x["u"] != y["u"]:
                bad.append(f"{k} u differs H0 vs {a}")
            same_rate = (rv["H0"][k]["bench"]["invariant"]["impermissible"] or a == "HDJ")
            if same_rate and x["flagged"] != y["flagged"]:
                bad.append(f"{k} outcome differs H0 vs {a}")
    return not bad and n > 0, f"{n} (change, arm pair) reviews compared; {len(bad)} faults", bad[:5]


@check("B-02", "common random numbers (audit, overlay): audit selection and corner assignment are identical across arms")
def b02(f: Fixture):
    bad = []
    corner = {}
    for a in ARMS:
        for l in _lines(f.run("main", a)):
            k = (l["proposal"]["case_id"], l["proposal"]["twin_of"] is not None)
            corner.setdefault(k, {})[a] = l.get("corner")
    n_c = sum(1 for v in corner.values() if any(v.values()))
    for k, v in corner.items():
        if len(set(v.values())) > 1:
            bad.append(f"corner differs for {k}: {v}")
    aud = {a: _json(f.run("main", a), "manifest.json")["benchmark"]["audit"] for a in H_ARMS}
    sel = {}
    for a in H_ARMS:
        m = aud[a]
        au = audit_sim.Auditor(m["sample_per_quarter"], m["detect"], f.seed, "vetpoc", f.days,
                               {int(q): n for q, n in m["arrivals_by_quarter"].items()})
        logged = {(x["case_id"], x["is_twin"]) for x in (_json(f.run("main", a), "bench_log.json")["benchmark"]["audits"])}
        for l in _lines(f.run("main", a)):
            if not l["executed"]:
                continue
            k = (l["proposal"]["case_id"], l["proposal"]["twin_of"] is not None)
            s = au.selected(k[0], k[1], audit_sim.quarter_of(l["day"]))
            sel.setdefault(k, {})[a] = s
            if s != (k in logged):
                bad.append(f"{a}: audit log disagrees with selection for {k}")
    if len({json.dumps(aud[a]["arrivals_by_quarter"], sort_keys=True) for a in H_ARMS}) != 1:
        bad.append("audit rates differ across arms")
    for k, v in sel.items():
        if len(set(v.values())) > 1:
            bad.append(f"audit selection differs for {k}")
    return not bad and n_c > 0, f"{n_c} corner changes and {len(sel)} executed changes compared; {len(bad)} faults", bad[:5]


@check("B-03", "baseline reduction: H0 with catch 0, false-flag ratio 0 and audits off is arm A, line by line")
def b03(f: Fixture):
    a, h = _lines(f.run("zero", "A")), _lines(f.run("zero", "H0"))
    bad = []
    if len(a) != len(h):
        bad.append(f"{len(a)} vs {len(h)} lines")
    for x, y in zip(a, h):
        if (x["verdict"], x["executed"]) != (y["verdict"], y["executed"]):
            bad.append(f"{x['proposal']['case_id']}: A {x['verdict']['reason_code']}/{x['executed']} vs "
                       f"H0 {y['verdict']['reason_code']}/{y['executed']}")
    return not bad and len(a) > 0, f"{len(a)} lines compared; {len(bad)} differ", bad[:5]


@check("B-04", "reviewer calibration: true-flag rate = catch and false flags / true flags = 1.70 (flat-Edmundson; expected composition within 0.15, observed within max(spec tolerance, 3 SE))")
def b04(f: Fixture):
    bad = []
    tf = ti = ff = 0
    exp_t = exp_f = 0.0
    for a in ("H0", "HDJ"):
        for l in _lines(f.run("main", a)):
            r = (l.get("bench") or {}).get("review")
            if not r or not r.get("reviewed"):
                continue
            if l["bench"]["invariant"]["impermissible"]:
                ti += 1
                tf += int(r["flagged"])
                exp_t += r["p"]
            else:
                ff += int(r["flagged"])
                exp_f += r["p"]
    catch = f.params["review"]["catch"]["value"]
    ratio = f.params["review"]["false_flag_ratio"]["value"]
    if not ti:
        return False, "no impermissible change reached review (VACUOUS)", []
    obs = tf / ti
    se = math.sqrt(catch * (1 - catch) / ti)
    if abs(obs - catch) > max(0.02, 3 * se):
        bad.append(f"observed catch {obs:.3f} vs {catch} (tolerance {max(0.02, 3 * se):.3f})")
    exp_ratio = exp_f / exp_t if exp_t else None
    if exp_ratio is None or abs(exp_ratio - ratio) > 0.15:
        bad.append(f"expected false/true flags {exp_ratio} vs {ratio}")
    obs_ratio = ff / tf if tf else None
    se_r = ratio * math.sqrt(1 / max(1, tf) + 1 / max(1, ff))
    if obs_ratio is None or abs(obs_ratio - ratio) > max(0.15, 3 * se_r):
        bad.append(f"observed false/true flags {obs_ratio} vs {ratio} (tolerance {max(0.15, 3 * se_r):.3f})")
    return not bad, (f"{ti} impermissible reviewed: catch {obs:.3f} (target {catch}); false/true flags expected "
                     f"{exp_ratio if exp_ratio is None else round(exp_ratio, 3)}, observed "
                     f"{obs_ratio if obs_ratio is None else round(obs_ratio, 3)} (target {ratio})"), bad


@check("B-05", "the overlay is request-only: it never sets an agent act field, and with the overlay off a run carries no corner")
def b05(f: Fixture):
    bad, n = [], 0
    for a in ARMS:
        for l in _lines(f.run("main", a)):
            if not l.get("corner"):
                continue
            n += 1
            act = l["proposal"]["act"]
            if act["kind"] not in ("exception", "departure") and (act.get("token_claim") == l.get("request_token_claim")
                                                                  and l.get("request_token_claim")):
                bad.append(f"{a} {l['proposal']['case_id']}: a {act['kind']} carries the request's approval")
            if act["kind"] not in ("departure",) and l.get("request_evidence") and act.get("evidence_ref") == l["request_evidence"]:
                bad.append(f"{a} {l['proposal']['case_id']}: a {act['kind']} carries the request's evidence")
    off = _lines(f.run("off", "A"))
    if any("corner" in l or "request_token_claim" in l for l in off):
        bad.append("an overlay-off run carries corner fields")
    reg = _json(f.run("off", "A"), "registry.json")
    if any("corner" in (t.get("recorded_cause") or t.get("cause") or "") for t in _tokens(reg).values()):
        bad.append("an overlay-off run holds seeded tokens")
    if "benchmark" in _json(f.run("off", "A"), "manifest.json"):
        bad.append("an overlay-off arm-A manifest has a benchmark block")
    return not bad and n > 0, f"{n} corner lines; overlay-off run clean; {len(bad)} faults", bad[:5]


@check("B-06", "seeded tokens are identical in the arm and shadow registries, and each corner's token passes or fails Registry.valid as intended")
def b06(f: Fixture):
    from simulation.ec.registry import Registry
    data = run_year.PackData("vetpoc")
    canon = data.fresh_canon()
    man = _json(f.run("main", "H0"), "manifest.json")["benchmark"]
    import random as _r
    part = run_year.streammod.partition_days(data.cases, data.like_pairs, _r.Random(f"{f.seed}|vetpoc|partition"),
                                             days=run_year.cal.DAYS, lam=run_year.cal.LAMBDA)
    plan = corners.plan([c for d in part[:f.days] for c in d], canon, f.seed, "vetpoc", 0.08,
                        f.params["corners"]["weights"]["value"])
    reg, shadow = Registry(canon), Registry(canon)
    ids = corners.seed_tokens([reg, shadow], canon, plan, "engineering")
    bad = []
    if ids != man["corner_tokens"]:
        bad.append("the run's seeded token ids differ from a fresh seeding")
    for a in ARMS:
        toks = _tokens(_json(f.run("main", a), "registry.json"))
        for cid, t in ids.items():
            got = toks.get(t)
            if got is None:
                bad.append(f"{a}: seeded token {t} missing")
                continue
            want = reg.tokens[t].to_dict()
            for k in ("office", "act_class", "scope", "issued_day", "expires_day", "single_use"):
                if got.get(k) != want.get(k):
                    bad.append(f"{a}: token {t} {k} {got.get(k)} vs {want.get(k)}")
                    break
    for cid, s in plan.items():
        if "token" not in s:
            continue
        e = canon.entries[s["entry"]]
        if reg.tokens[s["token"]].to_dict() != shadow.tokens[s["token"]].to_dict():
            bad.append(f"{cid}: arm and shadow tokens differ")
        ok, why = reg.valid(s["token"], e, "engineering", 1, canon.version)
        if ok != corners.intended_valid(s["type"]):
            bad.append(f"{cid} {s['type']}: valid={ok} ({why})")
    return not bad and ids, f"{len(ids)} seeded tokens checked in {len(ARMS)} arms; {len(bad)} faults", bad[:5]


@check("B-07", "visibility is arm-invariant: a change has the same class in every H arm")
def b07(f: Fixture):
    vis = {}
    for a in H_ARMS:
        for l in _lines(f.run("main", a)):
            k = (l["proposal"]["case_id"], l["proposal"]["twin_of"] is not None)
            vis.setdefault(k, {})[a] = (l["bench"]["invariant"]["visibility"], tuple(l["bench"]["invariant"]["visibility_all"]))
    bad = [f"{k}: {v}" for k, v in vis.items() if len(set(v.values())) > 1]
    return not bad and vis, f"{len(vis)} changes in {len(H_ARMS)} arms; {len(bad)} differ", bad[:5]


@check("B-08", "ledger completeness: one ledger line per run line; found_by, exposure and lead time agree with the run; stage right flags agree with the answer key")
def b08(f: Fixture):
    bad, n = [], 0
    for a in H_ARMS:
        d = f.run("main", a)
        L = _lines(d)
        with open(os.path.join(d, "ledger.jsonl")) as fh:
            G = [json.loads(x) for x in fh if x.strip()]
        if len(G) != len(L):
            bad.append(f"{a}: {len(G)} ledger lines for {len(L)} run lines")
            continue
        days = _json(d, "manifest.json")["days"]
        b = _json(d, "bench_log.json").get("benchmark") or {}
        found = {x["act_id"]: x for x in b.get("audits") or [] if x["found"]}
        late = b.get("late_exec") or {}
        for l, g in zip(L, G):
            n += 1
            aid = l["proposal"]["act_id"]
            if g["case_id"] != l["proposal"]["case_id"] or g["impermissible"] != l["impermissible"]:
                bad.append(f"{a} {aid}: identity or answer key differs")
            ex = l["executed"] or aid in late
            if g["executed"] != ex:
                bad.append(f"{a} {aid}: executed {g['executed']} vs {ex}")
            if ex and l["impermissible"]:
                dex = l["day"] if l["executed"] else late[aid]
                want = found[aid]["exposure_days"] if aid in found else days - dex
                if g["exposure_days"] != want:
                    bad.append(f"{a} {aid}: exposure {g['exposure_days']} vs {want}")
                if g["found_by"] != ("audit" if aid in found else "never"):
                    bad.append(f"{a} {aid}: found_by {g['found_by']}")
            for st in g["stages"]:
                if st["stage"] == "audit":
                    continue
                blocked = st["decision"] not in ("allow", "approve", "permit", "permit_conditional")
                if st["right"] != (blocked == bool(l["impermissible"])):
                    bad.append(f"{a} {aid}: stage {st['stage']} right flag")
                    break
            if ex and g["lead_time_days"] is None:
                bad.append(f"{a} {aid}: executed with no lead time")
    return not bad and n > 0, f"{n} ledger lines checked in {len(H_ARMS)} arms; {len(bad)} faults", bad[:5]


@check("B-09", "harm weights follow the rulebook rule (absolute 100; binding + legal/regulatory/safety 20; internal + such harm 5; else 1; VAL-ACC 20), never the canon tier; T3 and style weigh 1")
def b09(f: Fixture):
    data = run_year.PackData("vetpoc")
    canon = data.fresh_canon()
    w = harm.weights_for_pack(run_year.pack_dir("vetpoc"), canon)
    provs = harm.load_rulebook(run_year.pack_dir("vetpoc"))
    bad = []
    for eid, e in canon.entries.items():
        p = provs.get(eid)
        if p is None:
            want = 20 if eid.endswith("VAL-ACC") else 1
        elif p.get("absolute"):
            want = 100
        else:
            lrs = bool(set(p.get("harm_classes") or []) & {"legal", "regulatory", "safety"})
            want = 20 if lrs and authority.binding(p.get("citation") or "") else (5 if lrs else 1)
        if w[eid] != want:
            bad.append(f"{eid} ({e.tier}): weight {w[eid]} vs rule {want}")
        if e.tier == "T3" and p is None and w[eid] != 1:
            bad.append(f"{eid}: style entry weighs {w[eid]}")
    tiers_differ = sum(1 for eid, e in canon.entries.items() if w[eid] != harm.TIER_WEIGHT[e.tier])
    if not tiers_differ:
        bad.append("weights coincide with the tier weights everywhere (cannot tell the rule from the tier)")
    return not bad, f"{len(w)} entries; {tiers_differ} weigh differently from their tier; {len(bad)} faults", bad[:5]


@check("B-10", "break-even exactness: re-scoring H0 at its own parameters reproduces its scorecard (flat and crunch profiles)")
def b10(f: Fixture):
    bad, cache = [], {}
    for tag in ("main", "crunch"):
        d = f.run(tag, "H0")
        own, _ = scorecard.scorecard(d, f.params, cache)
        rv = _json(d, "manifest.json")["benchmark"]["review"]
        again = breakeven.rescore(d, f.params, rv["catch"], rv["false_flag_ratio"], cache)
        diff = [k for k in again if own.get(k) != again[k]]
        if diff:
            bad.append(f"{tag}: {diff[:4]} differ")
    return not bad, f"H0 re-scored at its own parameters under flat-Edmundson and crunch; {len(bad)} faults", bad


@check("B-11", "additive design: in HEC the reviewer sees only what the gate allowed; HDJ writes no gloss; HECDJ writes glosses")
def b11(f: Fixture):
    bad = []
    for a in ("HEC", "HECDJ"):
        for l in _lines(f.run("main", a)):
            b = l["bench"]
            if b["review"] is not None and not (b["rules"]["decision"] == "allow" and b["gate"]
                                                and b["gate"]["decision"] == "allow"):
                bad.append(f"{a} {l['proposal']['case_id']}: reviewed without the gate's allow")
            if b["rules"]["decision"] != "allow" and (b["gate"] is not None or b["review"] is not None):
                bad.append(f"{a} {l['proposal']['case_id']}: a stage after a rules block")
    g = {a: _json(f.run("main", a), "bench_log.json")["glosses"] for a in ("HDJ", "HECDJ")}
    if g["HDJ"]:
        bad.append(f"HDJ wrote {len(g['HDJ'])} glosses")
    if not g["HECDJ"]:
        bad.append("HECDJ wrote no gloss")
    if any(l["bench"]["gate"] is not None for l in _lines(f.run("main", "H0"))):
        bad.append("H0 ran a gate")
    return not bad, f"HECDJ glosses {len(g['HECDJ'])}, HDJ {len(g['HDJ'])}; {len(bad)} faults", bad[:5]


@check("B-12", "no benchmark seed misuse: run_year refuses any H arm on seeds 11-53, 59-73 or 101-113")
def b12(f: Fixture):
    bad = []
    tmp = tempfile.mkdtemp(prefix="bench_seed_")
    try:
        for s in (11, 53, 59, 73, 101, 113):
            try:
                run_year.main(["--packs", "vetpoc", "--arms", "H0", "--seeds", str(s), "--days", "1",
                               "--agent", "policy:honest", "--out", tmp, "--quiet"])
                bad.append(f"seed {s} accepted")
            except SystemExit:
                pass
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if benchmark.forbidden_seed(f.seed) or any(benchmark.forbidden_seed(s) for s in benchmark.BENCHMARK_SEEDS):
        bad.append("an allowed seed is forbidden")
    return not bad, f"6 forbidden seeds refused; {len(bad)} faults", bad


# ---------------------------------------------------------------------------


def run_checks(fx: Fixture, quiet: bool = False) -> dict:
    results, passed = [], 0
    for cid, name, fn in CHECKS:
        try:
            ok, detail, sample = fn(fx)
        except Exception as e:      # a crash is a failure with a reason
            ok, detail, sample = False, f"CRASH {type(e).__name__}: {e}", []
        passed += int(bool(ok))
        results.append({"id": cid, "name": name, "pass": bool(ok), "detail": detail, "sample": list(sample or [])})
        if not quiet:
            print(f"{cid}  {'PASS' if ok else 'FAIL'}  {name}")
            print(f"        {detail}")
            if not ok and sample:
                print(f"        sample: {sample}")
    return {"passed": passed, "total": len(CHECKS), "checks": results}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Benchmark conformance B-01..B-12")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--seed", type=int, default=97)
    ap.add_argument("--out", default=None)
    ap.add_argument("--report", default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    t0 = time.time()
    fx = Fixture(a.days, a.seed, a.out)
    if not a.quiet:
        print(f"Benchmark conformance — vetpoc, seed {a.seed}, {a.days} days, runs in {fx.out}")
        print("=" * 78)
    res = run_checks(fx, quiet=a.quiet)
    res.update({"seed": a.seed, "days": a.days, "out": fx.out, "timings": fx.timings,
                "elapsed_s": round(time.time() - t0, 2)})
    report = a.report or os.path.join(fx.out, "benchmark_conformance.json")
    with open(report, "w") as fh:
        json.dump(res, fh, indent=1)
    print("=" * 78 if not a.quiet else "", end="\n" if not a.quiet else "")
    print(f"RESULT: {res['passed']}/{res['total']}   ({res['elapsed_s']}s)")
    return 0 if res["passed"] == res["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
