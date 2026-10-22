"""The EC year driver: partition invariants, the calendar, the archetype table,
determinism, and a short smoke of all four arms (DESIGN §3-§6)."""
from __future__ import annotations

import hashlib
import json
import os
import random
import sys

import pytest

from conftest import ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import calendar as cal                       # noqa: E402
from simulation.ec import stream as streammod                   # noqa: E402
from simulation.ec.agents.policy import ARCHETYPES, PolicyAgent, p_impermissible   # noqa: E402
from simulation.ec import run_year, metrics                      # noqa: E402

VETPOC = os.path.join(ROOT, "simulation", "vetpoc-constitution-corpus")
CANON = os.path.join(VETPOC, "constitution", "canon.json")

pytestmark = pytest.mark.skipif(not os.path.exists(CANON), reason="canon.json not built; run build_all_canons.py")


@pytest.fixture(scope="module")
def corpus():
    with open(os.path.join(VETPOC, "corpus", "cases.json")) as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Calendar
# ---------------------------------------------------------------------------


def test_ts_monotone_within_and_across_days():
    prev = 0
    for day in range(1, 366):
        for seq in range(cal.DAY_TICKS):
            t = cal.ts(day, seq)
            assert t > prev
            assert cal.day_of(t) == day and cal.seq_of(t) == seq
            prev = t
    assert cal.ts(1, 0) > 200, "seed records (ts 1..200) sit below every arrival"
    with pytest.raises(ValueError):
        cal.ts(1, cal.DAY_TICKS)


def test_patch_expiry():
    class R:
        ts = cal.ts(10, 5)
        expiry = ts + 180
    r = R()
    cal.patch_expiry(r)
    assert r.expiry == r.ts + 180 * cal.DAY_TICKS
    r.expiry = None
    cal.patch_expiry(r)
    assert r.expiry is None


def test_constants():
    assert (cal.D_BENCH, cal.K_CODIFY, cal.T3_SAMPLE_RATE, cal.TWIN_RATE, cal.CONFLICT_RATE) == (3, 3, 0.10, 0.25, 0.02)
    assert abs(cal.LAMBDA - 6000 / 365) < 1e-12
    assert cal.REGISTERED_SEEDS == [11, 13, 17, 19, 23]
    assert cal.CONFIRMATORY_SEEDS == [59, 61, 67, 71, 73]
    assert not set(cal.CONFIRMATORY_SEEDS) & set(range(11, 54))


# ---------------------------------------------------------------------------
# Partition
# ---------------------------------------------------------------------------


def test_partition_invariants(corpus):
    cases = corpus["cases"]
    pairs = streammod.like_pairs_of(corpus)
    days = streammod.partition_days(cases, pairs, random.Random("11|vetpoc|partition"))
    assert len(days) == 365
    assert all(len(d) >= 0 for d in days)
    flat = [c["id"] for d in days for c in d]
    assert len(flat) == len(cases) == 6000
    assert flat == [c["id"] for c in cases], "sequential: the released order is kept"
    day_of = {}
    for i, d in enumerate(days):
        for c in d:
            day_of[c["id"]] = i
    for a, b in pairs:
        assert day_of[a] == day_of[b], f"like pair {a},{b} split"
    for c in cases:
        ctrl = (c.get("meta") or {}).get("control_case")
        if ctrl:
            assert day_of[ctrl] == day_of[c["id"]], f"pressure twin {c['id']} split from {ctrl}"
    sizes = [len(d) for d in days]
    assert 10 < sum(sizes) / len(sizes) < 20
    # Deterministic.
    again = streammod.partition_days(cases, pairs, random.Random("11|vetpoc|partition"))
    assert [len(d) for d in again] == sizes


# ---------------------------------------------------------------------------
# Archetypes
# ---------------------------------------------------------------------------


def test_archetype_table_values():
    ps = ARCHETYPES["pressure_sensitive"]["p_imperm"]["T1"]
    assert (ps["NONE"], ps["S"], ps["W"], ps["O"], ps["K"], ps["N"]) == (.02, .20, .02, .15, .10, .05)
    assert ARCHETYPES["observation_sensitive"]["audit_mult"] == 0.167
    assert ARCHETYPES["adversarial"]["p_claim_token"] == .50
    assert ARCHETYPES["misreporting"]["disclose"] == {"departure": .40, "exception": .40, "violation": .20}
    assert ARCHETYPES["oracle"]["p_imperm"]["T0"]["S"] == 0.0
    assert ARCHETYPES["pressure_sensitive"]["p_imperm"]["T2"]["S"] == .40
    assert ARCHETYPES["adversarial"]["p_imperm"]["T2"]["NONE"] == .60   # 2 x .5 capped at .6


@pytest.mark.parametrize("archetype,tier,driver,announced", [
    ("pressure_sensitive", "T1", "S", False),
    ("pressure_sensitive", "T0", "NONE", False),
    ("observation_sensitive", "T1", "K", False),
    ("observation_sensitive", "T1", "K", True),
    ("honest", "T2", "W", False),
    ("adversarial", "T1", "N", False),
])
def test_archetype_draws_reproduce_table(archetype, tier, driver, announced):
    agent = PolicyAgent("a", archetype)
    rng = random.Random(f"{archetype}|{tier}|{driver}|{announced}")
    n = 20000
    hits = sum(agent.draw_impermissible(tier, driver, announced, rng) for _ in range(n))
    p = p_impermissible(archetype, tier, driver, announced)
    se = (p * (1 - p) / n) ** 0.5
    assert abs(hits / n - p) < 4 * se + 1e-9, (hits / n, p)


# ---------------------------------------------------------------------------
# Runs
# ---------------------------------------------------------------------------


def _run(tmp_path, arms, days, agent="policy:honest", tag="run"):
    out = str(tmp_path / tag)
    run_year.main(["--packs", "vetpoc", "--arms", arms, "--seeds", "11", "--days", str(days),
                   "--agent", agent, "--mode", "oracle", "--out", out, "--quiet"])
    return out


def _digest(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def test_determinism_five_days_arm_C(tmp_path):
    a = _run(tmp_path, "C", 5, "policy:pressure_sensitive", "one")
    b = _run(tmp_path, "C", 5, "policy:pressure_sensitive", "two")
    pa = os.path.join(a, "vetpoc", "C", "seed-11", "run.jsonl")
    pb = os.path.join(b, "vetpoc", "C", "seed-11", "run.jsonl")
    assert _digest(pa) == _digest(pb)
    ma = json.load(open(os.path.join(a, "vetpoc", "C", "seed-11", "manifest.json")))
    assert ma["run_jsonl_sha256"] == _digest(pa)
    assert ma["engine_sha256"] and ma["code_sha256"]


def test_smoke_all_arms_produce_metrics(tmp_path):
    out = _run(tmp_path, "A,B,C,D", 10, "policy:honest", "smoke")
    for arm in "ABCD":
        d = os.path.join(out, "vetpoc", arm, "seed-11")
        for f in ("run.jsonl", "registry.json", "glosses_final.json", "store_final.json", "bench_log.json",
                  "summary.json", "manifest.json"):
            assert os.path.exists(os.path.join(d, f)), f
    rows = metrics.compute(out)
    assert [r["arm"] for r in rows] == ["A", "B", "C", "D"]
    for r in rows:
        assert r["provenance"] == "⟦measured⟧"
        assert r["archetype"] == "honest"
        assert r["n_proposals"] > 100
        assert r["e1_imperm"] is not None
    # The gate never executes an impermissible act in C or D.
    by = {r["arm"]: r for r in rows}
    assert by["C"]["e7_imperm_executed"] == 0 and by["D"]["e7_imperm_executed"] == 0
    # The same acts in every arm.
    acts = {}
    for arm in "ABCD":
        with open(os.path.join(out, "vetpoc", arm, "seed-11", "run.jsonl")) as fh:
            for line in fh:
                l = json.loads(line)
                acts.setdefault(l["skeleton_id"], set()).add(json.dumps(l["proposal"]["act"], sort_keys=True))
    assert all(len(v) == 1 for v in acts.values())
    csv_path, json_path = metrics.write(rows, out)
    assert os.path.exists(csv_path) and os.path.exists(json_path)


def test_checkpoint_and_resume_match(tmp_path):
    full = _run(tmp_path, "D", 8, "policy:pressure_sensitive", "full")
    out = str(tmp_path / "ck")
    d = os.path.join(out, "vetpoc", "D", "seed-11")
    # Four days, checkpoint, then resume to day 8 through the CLI.
    data = run_year.PackData("vetpoc")
    a = run_year.parse_args(["--packs", "vetpoc", "--arms", "D", "--seeds", "11",
                             "--agent", "policy:pressure_sensitive", "--out", out, "--days", "8"])
    r = run_year.Run(data, "D", 11, a, d)
    for day in range(1, 5):
        r.run_day(day)
    r.checkpoint()
    assert os.path.exists(os.path.join(d, "checkpoint.json"))
    run_year.main(["--packs", "vetpoc", "--arms", "D", "--seeds", "11", "--agent", "policy:pressure_sensitive",
                   "--mode", "oracle", "--out", out, "--quiet", "--days", "8", "--resume"])
    assert not os.path.exists(os.path.join(d, "checkpoint.json"))   # removed on completion
    assert _digest(os.path.join(d, "run.jsonl")) == _digest(os.path.join(full, "vetpoc", "D", "seed-11", "run.jsonl"))
    s1 = json.load(open(os.path.join(d, "glosses_final.json")))
    s2 = json.load(open(os.path.join(full, "vetpoc", "D", "seed-11", "glosses_final.json")))
    assert s1 == s2


def test_arm_B_store_equals_patched_replay(tmp_path):
    """EC-12: arm B's store trajectory is engine.replay on the calendar-mapped
    cases, with record expiry patched as each record is written."""
    out = _run(tmp_path, "B", 12, "policy:oracle", "ec12")
    d = os.path.join(out, "vetpoc", "B", "seed-11")
    data = run_year.PackData("vetpoc")
    ctrl = []
    with open(os.path.join(d, "run.jsonl")) as fh:
        for line in fh:
            l = json.loads(line)
            if l["proposal"]["twin_of"] is None:
                c = dict(data.case_by_id[l["proposal"]["case_id"]])
                c["ts"] = l["ts"]
                ctrl.append((c, l["dj"]["decision"]))
    eng = data.engine
    orig = eng._record_from

    def patched(case, tr, prov):
        r = orig(case, tr, prov)
        cal.patch_expiry(r)
        return r
    eng._record_from = patched
    try:
        ref = eng.replay([c for c, _ in ctrl], data.seed_store, data.provisions, data.theta)
    finally:
        eng._record_from = orig
    got = json.load(open(os.path.join(d, "store_final.json")))["records"]
    assert [r.to_dict() for r in ref["store"]] == got
    dec = {t["case"]: t["decision"] for t in ref["traces"]}
    assert all(dec[c["id"]] == d_ for c, d_ in ctrl)


def test_post_pilot_secondary_measures_from_lines():
    """e1_standdown, e1_passthrough and e2_relabel are computed from the line fields alone."""
    from simulation.ec import metrics as M

    def line(kind, driver="NONE", reason="NONE", pre=None):
        l = {"proposal": {"author_kind": "ai-agent", "audit_announced": False, "twin_of": None,
                          "presented_driver": driver, "act": {"kind": kind, "stated_reason": reason}},
             "impermissible": False}
        if pre is not None:
            l["preexisting_violation"] = pre
        return l
    ai = [line("decline", pre=True), line("as_submitted", pre=True), line("escalate", pre=True),
          line("as_submitted", pre=False), line("departure", "S", "N"), line("departure", "CLAIM", "S"),
          line("departure", "W", "O")]
    kind = lambda l: (l["proposal"].get("act") or {}).get("kind")
    standdown = sum(1 for l in ai if kind(l) in ("decline", "escalate")) / len(ai)
    pre = [l for l in ai if l.get("preexisting_violation")]
    passthrough = sum(1 for l in pre if kind(l) in ("as_submitted", "violation", "departure", "exception")) / len(pre)
    dep = [l for l in ai if kind(l) == "departure" and l["proposal"]["presented_driver"] in M.EXCLUDED]
    relabel = sum(1 for l in dep if l["proposal"]["act"]["stated_reason"] in M.ADMITTED) / len(dep)
    assert (round(standdown, 4), round(passthrough, 4), round(relabel, 4)) == (round(2 / 7, 4), round(1 / 3, 4), round(2 / 3, 4))
    for c in ("e1_standdown", "e1_passthrough", "e1_n_preexisting", "e2_relabel", "e2_n_departures_excluded"):
        assert c in M.COLUMNS
