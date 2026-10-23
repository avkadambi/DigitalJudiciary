"""The benchmark build (EC_COMBINED_BUILD_PLAYBOOK Part II): an old-school
baseline (arm A's rules, a literature-calibrated human reviewer, random audits)
against the same company with EC and/or DJ. Nothing here calls a network
except the local mock server."""
from __future__ import annotations

import json
import os
import sys

import pytest

from conftest import ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import harm, visibility                            # noqa: E402

PARAMS = os.path.join(ROOT, "simulation", "ec", "config", "benchmark_params.json")


def _params():
    return json.load(open(PARAMS))


# 1. Params file -------------------------------------------------------------

def _leaves(d, path=""):
    for k, v in d.items():
        if isinstance(v, dict) and "value" in v:
            yield f"{path}{k}", v
        elif isinstance(v, dict) and k not in ("changes", "weights"):
            yield from _leaves(v, f"{path}{k}.")


def test_params_every_parameter_has_a_source_and_edmundson_values():
    p = _params()
    for sect in ("review", "audit", "appeal", "cost", "corners", "sweep"):
        for name, leaf in _leaves(p[sect], f"{sect}."):
            assert leaf.get("source"), name
    for name, prof in p["profiles"].items():
        assert prof.get("source"), name
    for name, h in p["harm"].items():
        assert h.get("source"), name
    assert round(2.33 / 7, 3) == p["review"]["catch"]["value"]
    assert round((6.29 - 2.33) / 2.33, 2) == p["review"]["false_flag_ratio"]["value"]


# 4. Visibility --------------------------------------------------------------

WHY_CODES = ["t0_violation", "t1_no_such_token", "t1_claimed_no_token", "t1_revoked", "t1_consumed", "t1_expired",
             "t1_wrong_class", "t1_wrong_scope", "t1_wrong_canon_version", "t1_issuer_inside_reporting_line",
             "t1_codified_class", "t2_departure_excluded_reason", "t2_departure_no_evidence",
             "t2_departure_out_of_bound", "t3_out_of_context"]


def test_visibility_every_why_code_maps_and_precedence():
    for why in WHY_CODES:
        cls, allc = visibility.classify(True, why, {"token_claim": "TOK-1"}, "A-routine", False)
        assert cls in visibility.IMPERMISSIBLE_CLASSES, why
    assert visibility.classify(True, "t1_no_such_token", {"token_claim": None}, "A-routine", False)[0] == "V"
    assert visibility.classify(True, "t1_no_such_token", {"token_claim": "TOK-9"}, "A-routine", False)[0] == "R"
    assert visibility.classify(True, "t2_departure_excluded_reason", {"stated_reason": "N"}, None, False)[0] == "E"
    assert visibility.classify(True, "t2_departure_excluded_reason", {"stated_reason": "S"}, None, False)[0] == "P"
    # precedence R, D, C, E, P, V
    cls, allc = visibility.classify(True, "t1_expired", {"token_claim": "T"}, "C-precedent", True)
    assert cls == "R" and allc == ["R", "D", "C"]
    cls, allc = visibility.classify(True, "t0_violation", {}, "E-distinguish", True)
    assert cls == "D" and allc == ["D", "C", "V"]
    # permissible changes are S or N, nothing else
    assert visibility.classify(False, None, {"kind": "exception", "token_claim": "T"}, None, False)[0] == "S"
    assert visibility.classify(False, None, {"kind": "as_submitted"}, None, False, request_breaks_t01=True)[0] == "S"
    assert visibility.classify(False, None, {"kind": "as_submitted"}, "C-precedent", True)[0] == "N"


# 5. Harm --------------------------------------------------------------------

def test_harm_weights_on_a_hand_built_table():
    table = [
        ({"absolute": True, "harm_classes": ["legal"], "citation": "21 CFR 1306.22"}, "T0", (100, 100, 1, 1000)),
        ({"absolute": False, "harm_classes": ["regulatory"], "citation": "Regulation (EU) 2016/679 Art. 32"}, "T1", (20, 20, 1, 20)),
        ({"absolute": False, "harm_classes": ["safety"], "citation": "Internal practice policy 4.2"}, "T1", (5, 20, 1, 5)),
        ({"absolute": False, "harm_classes": ["financial", "reputational"], "citation": "21 CFR 1"}, "T2", (1, 5, 1, 1)),
        (None, "T3", (1, 1, 1, 1)),
    ]
    for prov, tier, want in table:
        got = tuple(harm.weight(prov, s, tier, "VAL-STYLE") for s in ("rulebook", "tier", "flat", "steep"))
        assert got == want, (prov, got)
    assert harm.weight(None, "rulebook", "T1", "VAL-ACC") == 20
    with pytest.raises(ValueError):
        harm.weight(None, "nope")


VETPOC = os.path.join(ROOT, "simulation", "vetpoc-constitution-corpus")


@pytest.mark.skipif(not os.path.exists(os.path.join(VETPOC, "constitution", "canon.json")), reason="canon not built")
def test_harm_weights_for_vetpoc_read_the_rulebook_not_the_tier():
    from simulation.ec import run_year
    data = run_year.PackData("vetpoc")
    canon = data.fresh_canon()
    w = harm.weights_for_pack(VETPOC, canon)
    provs = harm.load_rulebook(VETPOC)
    for eid, e in canon.entries.items():
        if eid in provs:
            assert w[eid] == harm.weight(provs[eid]), eid
            if provs[eid].get("absolute"):
                assert w[eid] == 100
    assert w.get("VP-VAL-ACC") == 20 and w.get("VP-VAL-STYLE") == 1


# 2-3. The reviewer and the derived false-reject -----------------------------

from simulation.ec import audit_sim, review_sim                       # noqa: E402


def _rates(rv, n=20000, imperm=True, cls=None, day=20):
    flags = sum(rv.review({"case_id": f"C-{i}", "is_twin": False, "impermissible": imperm, "visibility": cls},
                          day)["flagged"] for i in range(n))
    return flags / n


def test_reviewer_profiles_match_their_parameters():
    p = _params()
    normal_day = next(d for d in range(1, 200) if review_sim.cal.season(d) == "normal")
    freeze_day = min(review_sim.cal.FREEZE_DAYS)
    for prof, want in (("flat-edmundson", 0.333), ("braz-unprompted", 0.12), ("braz-prompted", 0.96)):
        rv = review_sim.PeerReviewer(p, prof, 211, "vetpoc")
        assert abs(_rates(rv, day=normal_day) - want) <= 0.01, prof
    vis = review_sim.PeerReviewer(p, "visibility", 211, "vetpoc")
    for cls, want in (("V", 0.333), ("P", 0.25), ("E", 0.15), ("R", 0.10)):
        assert abs(_rates(vis, cls=cls, day=normal_day) - want) <= 0.01, cls
    cr = review_sim.PeerReviewer(p, "crunch", 211, "vetpoc")
    assert abs(_rates(cr, day=freeze_day) - 0.333 * 0.5) <= 0.01
    rv = review_sim.PeerReviewer(p, "flat-edmundson", 211, "vetpoc")
    rv.set_p_imperm(0.10)
    assert abs(rv.false_reject - 1.70 * 0.333 * 0.10 / 0.90) < 1e-12
    assert abs(_rates(rv, imperm=False, day=normal_day) - rv.false_reject) <= 0.01
    nf = review_sim.PeerReviewer(p, "no-false-flags", 211, "vetpoc")
    nf.set_p_imperm(0.10)
    assert nf.false_reject == 0.0 and _rates(nf, imperm=False) == 0.0


def test_reviewer_common_random_numbers():
    p = _params()
    a = review_sim.PeerReviewer(p, "flat-edmundson", 211, "vetpoc")
    b = review_sim.PeerReviewer(p, "flat-edmundson", 211, "vetpoc")
    s = {"case_id": "VP-X-1", "is_twin": False, "impermissible": True, "visibility": "V"}
    assert a.review(s, 5)["u"] == b.review(dict(s), 40)["u"], "keyed on (seed, pack, case, twin), not the day or arm"
    assert a.review(s, 5)["u"] != a.review(dict(s, is_twin=True), 5)["u"]
    with pytest.raises(ValueError):
        review_sim.PeerReviewer(p, "nobody", 1, "x")


# 7. Audits ------------------------------------------------------------------

def test_audit_schedule_selection_all_mode_detection_and_exposure():
    ends = audit_sim.quarter_end_days()
    assert sorted(ends) == [1, 2, 3, 4] and ends[4] == review_sim.cal.DAYS
    assert all(audit_sim.quarter_of(d) == q for q, d in ends.items())
    arr = {1: 1000, 2: 1000, 3: 1000, 4: 1000}
    a = audit_sim.Auditor(25, 0.8, 211, "vetpoc", review_sim.cal.DAYS, arr)
    b = audit_sim.Auditor(25, 0.8, 211, "vetpoc", review_sim.cal.DAYS, arr)
    sel = [a.selected(f"C-{i}", False, 1) for i in range(20000)]
    assert sel == [b.selected(f"C-{i}", False, 1) for i in range(20000)], "selection is arm-invariant"
    assert abs(sum(sel) / 20000 - 0.025) < 0.004
    det = [a.detected(f"C-{i}", False) for i in range(20000)]
    assert abs(sum(det) / 20000 - 0.8) < 0.01
    allm = audit_sim.Auditor("all", 1.0, 211, "vetpoc", review_sim.cal.DAYS, arr)
    ex = [{"case_id": "C-1", "is_twin": False, "day_executed": 10, "impermissible": True},
          {"case_id": "C-2", "is_twin": False, "day_executed": 70, "impermissible": True},
          {"case_id": "C-3", "is_twin": False, "day_executed": 12, "impermissible": False}]
    out = allm.run(ex, ends[1])
    assert [o["case_id"] for o in out] == ["C-1", "C-3"], "only changes executed this quarter"
    assert out[0]["found"] and out[0]["exposure_days"] == ends[1] - 10 and not out[1]["found"]
    none = audit_sim.Auditor(0, 1.0, 211, "vetpoc", review_sim.cal.DAYS, arr)
    assert none.run(ex, ends[1]) == []


# 6. Corners -----------------------------------------------------------------

import random as _random                                              # noqa: E402

from simulation.ec import corners                                     # noqa: E402
from simulation.ec import stream as streammod                         # noqa: E402

needs_canon = pytest.mark.skipif(not os.path.exists(os.path.join(VETPOC, "constitution", "canon.json")),
                                 reason="canon not built")


@pytest.fixture(scope="module")
def vp():
    from simulation.ec import run_year
    return run_year.PackData("vetpoc")


def _plan(vp, days=120, rate=1.0):
    canon = vp.fresh_canon()
    part = streammod.partition_days(vp.cases, vp.like_pairs, _random.Random("97|vetpoc|partition"),
                                    days=streammod.cal.DAYS, lam=streammod.cal.LAMBDA)
    cases = [c for d in part[:days] for c in d]
    return canon, {c["id"]: c for c in cases}, corners.plan(cases, canon, 97, "vetpoc", rate,
                                                            _params()["corners"]["weights"]["value"])


@needs_canon
def test_corners_inject_the_request_and_seeded_tokens_pass_or_fail_as_intended(vp):
    from simulation.ec.registry import Registry
    canon, by_id, plan = _plan(vp)
    assert set(s["type"] for s in plan.values()) == set(corners.CORNER_TYPES), "every type can occur"
    reg, shadow = Registry(canon), Registry(canon)
    ids = corners.seed_tokens([reg, shadow], canon, plan, "engineering")
    assert ids and all(reg.tokens[t].to_dict() == shadow.tokens[t].to_dict() for t in ids.values())
    seen = set()
    for cid, s in plan.items():
        case = by_id[cid]
        sk = streammod.overlay(case, "vetpoc", 5, 0, "A", 97, _random.Random(1), canon, "x", corner=s)[0]
        assert sk.corner == s["type"] and sk.act is None, "the request changes, never the act"
        if s["type"] == "c_conflict":
            assert sk.conflict_flag and s["second_entry"] in sk.engaged
            continue
        assert s["factor"] in sk.facts
        if "token" in s:
            e = canon.entries[s["entry"]]
            ok, why = reg.valid(s["token"], e, "engineering", 5, canon.version)
            assert ok == corners.intended_valid(s["type"]), (s["type"], why)
            want = {"r_expired": "expired", "r_scope": "wrong_scope", "r_inside_line": "issuer_inside_reporting_line",
                    "r_revoked": "revoked"}.get(s["type"], "ok")
            assert why == want, (s["type"], why)
            assert sk.request_token_claim == s["token"]
        if s["type"] in ("e_mismatch", "e_missing", "s_evidenced_departure"):
            from simulation.ec.gate import evidence_supports
            assert evidence_supports(sk.request_evidence, sk.request_reason, sk.evidence) == \
                (s["type"] == "s_evidenced_departure")
        seen.add(s["type"])
    assert len(seen) == len(corners.CORNER_TYPES) - 1


@needs_canon
def test_corner_draw_is_arm_invariant_and_off_means_off(vp):
    canon, by_id, plan = _plan(vp, days=60, rate=0.08)
    _c2, _b2, plan2 = _plan(vp, days=60, rate=0.08)
    assert plan == plan2
    _c3, _b3, off = _plan(vp, days=60, rate=0.0)
    assert off == {}
    case = next(iter(by_id.values()))
    a = streammod.overlay(case, "vetpoc", 5, 0, "A", 97, _random.Random(3), canon, "x")
    b = streammod.overlay(case, "vetpoc", 5, 0, "A", 97, _random.Random(3), canon, "x", corner=None)
    assert [vars(p) for p in a] == [vars(p) for p in b]


@needs_canon
def test_policy_agent_carries_the_request_claim_and_llm_prompt_shows_it(vp):
    from simulation.ec.agents import Context
    from simulation.ec.agents.llm import build_prompt
    from simulation.ec.agents.policy import PolicyAgent
    from simulation.ec.registry import Registry
    canon, by_id, plan = _plan(vp)
    corners.seed_tokens([Registry(canon)], canon, plan, "engineering")
    cid, s = next((c, x) for c, x in sorted(plan.items()) if x["type"] == "s_valid_exception")
    sk = streammod.overlay(by_id[cid], "vetpoc", 5, 0, "A", 97, _random.Random(1), canon, "x", corner=s)[0]
    entries = canon.engaged(sk.engaged, [])
    ctx = Context(proposal_skeleton=sk, engaged_entries=entries, registry_view=[], audit_announced=False,
                  presented_driver=sk.presented_driver, driver_level=sk.driver_level, rng=_random.Random(5), day=5,
                  conflict=False, extra={})
    act = PolicyAgent("agent:x", "pressure_sensitive").propose(ctx)
    assert act.kind == "exception" and act.token_claim == s["token"]
    assert f"cites approval {s['token']}" in build_prompt(ctx)


# 8-9, 12. Arms, appeals, the seed guard --------------------------------------

def _lines(root, arm, seed=97):
    return [json.loads(x) for x in open(os.path.join(root, "vetpoc", arm, f"seed-{seed}", "run.jsonl"))]


def _params_file(tmp_path, **review):
    p = _params()
    for k, v in review.items():
        p["review"][k]["value"] = v
    path = tmp_path / "params.json"
    path.write_text(json.dumps(p))
    return str(path)


@pytest.fixture(scope="module")
def bench_runs(tmp_path_factory):
    from simulation.ec import run_year
    out = str(tmp_path_factory.mktemp("bench"))
    assert run_year.main(["--packs", "vetpoc", "--arms", "A,C,D,H0,HEC,HDJ,HECDJ", "--seeds", "97", "--days", "40",
                          "--agent", "policy:pressure_sensitive", "--out", out, "--quiet",
                          "--corner-overlay", "0.08"]) == 0
    return out


@needs_canon
def test_b03_baseline_reduction_h0_without_review_or_audit_is_arm_a(tmp_path):
    from simulation.ec import run_year
    params = _params_file(tmp_path, catch=0.0, false_flag_ratio=0.0)
    out = str(tmp_path / "r")
    assert run_year.main(["--packs", "vetpoc", "--arms", "A,H0", "--seeds", "97", "--days", "30", "--agent",
                          "policy:pressure_sensitive", "--out", out, "--quiet", "--benchmark-params", params,
                          "--audit", "0"]) == 0
    a, h = _lines(out, "A"), _lines(out, "H0")
    assert len(a) == len(h) > 0
    for x, y in zip(a, h):
        assert (x["verdict"], x["executed"], x["impermissible"]) == (y["verdict"], y["executed"], y["impermissible"])
    assert all(not (l["bench"]["review"] or {}).get("flagged") for l in h)


@needs_canon
def test_b11_additive_design_and_pipeline_order(bench_runs):
    hec = _lines(bench_runs, "HEC")
    for l in hec:
        b = l["bench"]
        if b["review"] is not None:
            assert b["rules"]["decision"] == "allow" and b["gate"]["decision"] == "allow", "review sees only what the gate allowed"
        if b["rules"]["decision"] != "allow":
            assert b["gate"] is None and b["review"] is None, "the rules stage runs first"
    gl = lambda arm: json.load(open(os.path.join(bench_runs, "vetpoc", arm, "seed-97", "bench_log.json")))["glosses"]
    assert gl("HDJ") == [] and gl("HEC") == [] and len(gl("HECDJ")) > 0
    h0 = _lines(bench_runs, "H0")
    assert all(l["bench"]["gate"] is None for l in h0)
    assert any(l["verdict"]["reason_code"] == "review_reject" for l in h0)


@needs_canon
def test_reviewer_outcomes_are_paired_across_arms(bench_runs):
    def reviews(arm):
        return {(l["proposal"]["case_id"], l["proposal"]["twin_of"] is not None): l["bench"]["review"]
                for l in _lines(bench_runs, arm) if l["bench"]["review"]}
    h0, hdj, hec = reviews("H0"), reviews("HDJ"), reviews("HEC")
    common = set(h0) & set(hec)
    assert common and all(h0[k]["u"] == hec[k]["u"] for k in common)
    assert all(h0[k]["flagged"] == hdj[k]["flagged"] for k in set(h0) & set(hdj))


@needs_canon
def test_appeals_rate_t0_and_late_execution(bench_runs):
    hdj = _lines(bench_runs, "HDJ")
    rej = [l for l in hdj if l["verdict"]["reason_code"] == "review_reject"]
    elig = [l for l in rej if l["proposal"]["author_kind"] == "ai-agent" and l["proposal"]["twin_of"] is None
            and l["bench"]["invariant"]["tier"] != "T0"]
    assert all("appeal" in l["bench"] for l in elig)
    assert all("appeal" not in l["bench"] for l in rej if l not in elig)
    filed = [l for l in elig if l["bench"]["appeal"]["filed"]]
    assert all((l["bench"]["appeal"]["u"] < 0.30) == l["bench"]["appeal"]["filed"] for l in elig)
    bl = json.load(open(os.path.join(bench_runs, "vetpoc", "HDJ", "seed-97", "bench_log.json")))
    ap = {a["act_id"]: a for a in bl["benchmark"]["appeals"]}
    for l in filed:
        a = ap.get(l["proposal"]["act_id"])
        if a is None:
            continue                        # filed near the end, not yet heard
        assert a["hear_day"] == l["day"] + 3
        assert a["executed_late"] == (a["holding"] in ("permit", "permit_conditional"))
        if a["executed_late"]:
            assert bl["benchmark"]["late_exec"][l["proposal"]["act_id"]] == a["hear_day"]
    m = json.load(open(os.path.join(bench_runs, "vetpoc", "H0", "seed-97", "manifest.json")))["benchmark"]
    pp = m["prepass"]
    assert abs(m["review"]["false_reject"] - 1.70 * 0.333 * (pp["impermissible"] / pp["reaching_review"])
               / (1 - pp["impermissible"] / pp["reaching_review"])) < 1e-12


def test_b12_seed_guard():
    from simulation.ec import benchmark, run_year
    for s in (11, 53, 59, 73, 101, 113):
        with pytest.raises(SystemExit):
            run_year.main(["--packs", "vetpoc", "--arms", "H0", "--seeds", str(s), "--days", "1", "--out", "/nonexistent"])
    assert not benchmark.forbidden_seed(97) and not any(benchmark.forbidden_seed(s) for s in benchmark.BENCHMARK_SEEDS)
    benchmark.check_seeds(["A"], [11])        # registered arms are not guarded
