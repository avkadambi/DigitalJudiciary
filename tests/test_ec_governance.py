"""The LLM governance build (EC_LLM_GOVERNANCE_BUILD_PLAYBOOK v3): every governance
seat can be deterministic (today's code), llm (the model binds) or shadow (the
answer key binds and the model is only logged). Nothing here calls a network
except the local mock server."""
from __future__ import annotations

import io
import os
import shutil
import sys

import pytest

from conftest import ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import run_year                                   # noqa: E402
from simulation.ec.tools import check_r2_digests                     # noqa: E402

R2_DIR = os.path.join(ROOT, check_r2_digests.REL_DIR)


# ---------------------------------------------------------------------------
# H1: the R2 digest check
# ---------------------------------------------------------------------------


def _ref_available() -> bool:
    import subprocess
    r = subprocess.run(["git", "-C", ROOT, "cat-file", "-e", check_r2_digests.REF_COMMIT + "^{commit}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return r.returncode == 0


needs_ref = pytest.mark.skipif(not _ref_available() or not os.path.isdir(R2_DIR),
                               reason="R2 reference commit or calibration_r2 tree not available")


@needs_ref
def test_h1_reference_files_match():
    out = io.StringIO()
    assert check_r2_digests.check(R2_DIR, out=out) == 20
    assert "RESULT: 20/20" in out.getvalue()


@needs_ref
def test_h1_modified_copy_fails(tmp_path):
    copy = tmp_path / "calibration_r2"
    shutil.copytree(R2_DIR, copy)
    with open(copy / "honest" / "metrics.csv", "a") as fh:
        fh.write("tampered\n")
    out = io.StringIO()
    assert check_r2_digests.check(str(copy), out=out) == 19
    assert "DIFF  honest/metrics.csv" in out.getvalue()
    assert check_r2_digests.main(["--results", str(copy)]) == 1


# ---------------------------------------------------------------------------
# H2: Python 3.9 or later
# ---------------------------------------------------------------------------


def test_h2_python_check_rejects_38():
    with pytest.raises(SystemExit) as ei:
        run_year.check_python((3, 8, 18))
    assert "Python 3.9 or later is required (found 3.8)" in str(ei.value)


def test_h2_python_check_accepts_39_and_later():
    run_year.check_python((3, 9, 0))
    run_year.check_python(sys.version_info)


# ---------------------------------------------------------------------------
# R1: the answer keys (pure)
# ---------------------------------------------------------------------------

import json                                                          # noqa: E402

from simulation.ec import bench_oracle as bo                         # noqa: E402
from simulation.ec.gate import Act, Proposal, four_way, gate, gate_oracle, Verdict   # noqa: E402
from simulation.ec.registry import Registry                          # noqa: E402

FIXTURE = os.path.join(ROOT, "tests", "fixtures", "oracle_split_case.json")
VETPOC_CANON = os.path.join(ROOT, "simulation", "vetpoc-constitution-corpus", "constitution", "canon.json")
needs_canon = pytest.mark.skipif(not os.path.exists(VETPOC_CANON), reason="canon.json not built")


@pytest.fixture(scope="module")
def vetpoc():
    return run_year.PackData("vetpoc")


@needs_canon
def test_r1_split_fixture_engine_permits_canon_denies(vetpoc):
    fx = json.load(open(FIXTURE))
    store = [vetpoc.engine.Record.from_dict(r) for r in fx["store"]]
    r = bo.bench_oracle(fx["case"], store, vetpoc.provisions, vetpoc.theta, vetpoc.engine, fx["filing"])
    assert r["engine"]["holding"] == "permit" and r["engine"]["route"] == "bound_by_precedent"
    assert r["canon"]["holding"] == "deny" and r["disagree"] is True
    assert len(store) == 1, "the oracle never writes the store"


def _pe(tier, **kw):
    d = {"id": "E", "tier": tier, "contravened": False, "departure": None, "token_valid": None, "token_fail": None,
         "say_so": None, "t2_admitted": None, "t2_evidence": None, "t2_in_bound": None, "t3_in_context": None,
         "gloss_bar": None}
    d.update(kw)
    return d


def test_r1_canon_precedence_table():
    ch = bo.canon_holding
    assert ch([_pe("T0", contravened=True)])[0] == "deny"
    assert ch([_pe("T1", contravened=True, token_valid=True)])[0] == "permit"
    assert ch([_pe("T1", contravened=True, token_valid=False, token_fail="no_such_token")])[0] == "deny"
    assert ch([_pe("T1", contravened=True, token_valid=False, gloss_bar=True)])[1] == "t1_binding_gloss"
    assert ch([_pe("T1", contravened=True, token_valid=False, token_fail="codified_class")])[1] == "t1_binding_gloss"
    ok = dict(departure=True, t2_admitted=True, t2_evidence=True, t2_in_bound=True)
    assert ch([_pe("T2", **ok)])[0] == "permit"
    for miss in ("t2_admitted", "t2_evidence", "t2_in_bound"):
        assert ch([_pe("T2", **dict(ok, **{miss: False}))])[0] == "deny"
    assert ch([_pe("T3", departure=True, t3_in_context=True)])[0] == "permit"
    assert ch([_pe("T3", departure=True, t3_in_context=False)])[0] == "deny"
    assert ch([_pe("T2"), _pe("T1")])[0] is None, "no contravention or departure: the engine's holding"
    h, basis, t0 = ch([_pe("T1", contravened=True, token_valid=True), _pe("T0", contravened=True)], conflict=True)
    assert h == "deny" and basis.startswith("conflict_most_restrictive") and t0


@needs_canon
def test_r1_corpus_contest_keys_equal_and_a6_outranks_a4(vetpoc):
    fx = json.load(open(FIXTURE))
    store = [vetpoc.engine.Record.from_dict(r) for r in fx["store"]]
    corpus = dict(fx["filing"], origin="corpus_contest", per_entry=None)
    r = bo.bench_oracle(fx["case"], store, vetpoc.provisions, vetpoc.theta, vetpoc.engine, corpus)
    assert r["canon"]["holding"] == r["engine"]["holding"] and not r["disagree"]
    # contest_to 4: the risk-owner overlay applies after a T1 deny ...
    ro = dict(fx["filing"], contest_to=4)
    r4 = bo.bench_oracle(fx["case"], store, vetpoc.provisions, vetpoc.theta, vetpoc.engine, ro)
    assert r4["engine"]["holding"] == "permit_conditional" and r4["canon"]["holding"] == "permit_conditional"
    # ... but not after a T0 deny (A6 outranks A4)
    t0 = dict(ro, per_entry=[_pe("T0", contravened=True)])
    r0 = bo.bench_oracle(fx["case"], store, vetpoc.provisions, vetpoc.theta, vetpoc.engine, t0)
    assert r0["canon"]["holding"] == "deny" and r0["disagree"]


@needs_canon
def test_gate_oracle_is_pure_and_agrees_with_gate(vetpoc):
    canon = vetpoc.fresh_canon()
    e = next(x for x in canon.entries.values() if x.tier == "T1" and x.kind == "provision" and x.office)
    reg = Registry(canon)
    tok = reg.issue(e.office, e.act_class, e.id, 1, single_use=True)
    act = Act("exception", e.id, e.violate_factors[0], "N", None, None, tok.id, False)
    p = Proposal("A-1", "C-1", "vetpoc", 2, 2000, 0, "agent:x", "llm", "ai-agent", [e.id], "NONE", 0, False, None,
                 act, facts=[])
    before = json.dumps(reg.to_dict(), sort_keys=True)
    v, consumed, per = gate_oracle(p, canon, reg, 2)
    assert json.dumps(reg.to_dict(), sort_keys=True) == before, "gate_oracle consumed nothing"
    assert consumed == [tok.id] and per[0]["token_valid"] is True and per[0]["contravened"] is True
    v2 = gate(p, canon, reg, 2)
    assert v2.to_dict() == v.to_dict() and reg.tokens[tok.id].consumed
    assert four_way(v) == "allow"
    assert four_way(Verdict("block", "t0_violation", escalate=True)) == "escalate"
    assert four_way(Verdict("hold", "x", escalate=False)) == "hold"
    assert four_way(Verdict("block", "gloss_bar", escalate=False)) == "block"


@needs_canon
def test_decide_request_oracle_matches_decide_requests(vetpoc):
    from simulation.ec.registry import EXCEPTION_LEAD_DAYS
    canon = vetpoc.fresh_canon()
    e = next(x for x in canon.entries.values() if x.tier == "T1" and x.kind == "provision" and x.office)
    reg = Registry(canon)
    reg.request(e, 1, "N", True, "A-1")
    want = reg.decide_request_oracle(reg.requests[0], canon, 1 + EXCEPTION_LEAD_DAYS)
    got = reg.decide_requests(canon, 1 + EXCEPTION_LEAD_DAYS)
    assert want == "granted" and len(got) == 1
    assert reg.events[-1]["outcome"] == "granted"


# ---------------------------------------------------------------------------
# Config, keys, flags, prompts (commit 4; R4 prompt styles; H5)
# ---------------------------------------------------------------------------

from simulation.ec import governance as gov                          # noqa: E402
from simulation.ec import llm_client                                  # noqa: E402

ROLES_EXAMPLE = os.path.join(ROOT, "simulation", "ec", "config", "llm_roles.example.json")
PROMPT_SEATS = ("conscience", "office", "auditor", "judge", "prosecutor", "clerk", "lawmaker", "l4_proxy")


def test_r4_both_prompt_styles_exist_for_every_seat_and_canon_is_clean():
    for seat in PROMPT_SEATS:
        for style in gov.PROMPT_STYLES:
            assert gov.load_prompt(seat, style), (seat, style)
        assert gov.canon_leaks(gov.load_prompt(seat, "canon")) == [], seat
    assert set(gov.load_stances()) == set(llm_client.STANCES)
    assert len(set(gov.load_stances().values())) == 3, "the stance preambles differ"


def test_r4_ec22_catches_a_seeded_leak():
    canon = gov.load_prompt("conscience", "canon")
    assert gov.canon_leaks(canon + "\nThen call registry.valid(token).") != []
    assert gov.canon_leaks(gov.load_prompt("conscience", "procedural")) != []


def test_roles_config_literal_key_is_fatal(tmp_path):
    cfg = json.load(open(ROLES_EXAMPLE))
    cfg["providers"]["anthropic"]["api_key"] = "sk-not-a-real-key"
    p = tmp_path / "roles.json"
    p.write_text(json.dumps(cfg))
    with pytest.raises(llm_client.ConfigError, match="literal api_key"):
        llm_client.load_roles_config(str(p))


def test_roles_config_prices_need_a_source(tmp_path):
    cfg = json.load(open(ROLES_EXAMPLE))
    cfg["prices"]["meta-llama/Llama-3.3-70B-Instruct-Turbo"].pop("source")
    p = tmp_path / "roles.json"
    p.write_text(json.dumps(cfg))
    with pytest.raises(llm_client.ConfigError, match="source"):
        llm_client.load_roles_config(str(p))


def test_keys_file_refused_inside_repo_or_world_readable(tmp_path, monkeypatch):
    inside = os.path.join(ROOT, "simulation", "ec", "config", "_test_keys.env")
    try:
        with open(inside, "w") as fh:
            fh.write("X_TEST_KEY=1\n")
        os.chmod(inside, 0o600)
        with pytest.raises(llm_client.ConfigError, match="outside the repository"):
            llm_client.load_keys_file(inside, ROOT)
    finally:
        os.remove(inside)
    f = tmp_path / "keys.env"
    f.write_text("X_TEST_KEY=abc\n")
    os.chmod(f, 0o644)
    with pytest.raises(llm_client.ConfigError, match="private"):
        llm_client.load_keys_file(str(f), ROOT)
    os.chmod(f, 0o600)
    monkeypatch.delenv("X_TEST_KEY", raising=False)
    assert llm_client.load_keys_file(str(f), ROOT) == ["X_TEST_KEY"]
    assert os.environ["X_TEST_KEY"] == "abc"


def test_default_flags_keep_run_config_and_dir_layout():
    a = run_year.parse_args(["--packs", "vetpoc", "--arms", "C", "--seeds", "11", "--days", "3"])
    cfg = run_year.run_config_of(a)
    assert not set(cfg) & set(gov.NEW_FLAG_DEFAULTS), "a deterministic run records no governance flag"
    assert run_year.run_dir_for(a, "vetpoc", "C", 11).endswith(os.path.join("vetpoc", "C", "seed-11"))
    b = run_year.parse_args(["--governance", "shadow", "--roles-config", ROLES_EXAMPLE, "--keys-file", "/x/y"])
    cfg = run_year.run_config_of(b)
    assert cfg["governance"] == "shadow" and cfg["keys_file"] == "<set>" and "roles_config_sha256" in cfg
    assert run_year.run_dir_for(b, "vetpoc", "D", 11).endswith("seed-11+gov-shadow")
    c = run_year.parse_args(["--governance", "llm", "--prompt-style", "procedural", "--roles-config", ROLES_EXAMPLE])
    assert run_year.run_dir_for(c, "vetpoc", "D", 11).endswith("seed-11+gov-llm+procedural")


def test_live_startup_names_missing_keys_never_values(monkeypatch, tmp_path):
    for k in ("ANTHROPIC_API_KEY", "DEEPINFRA_API_KEY", "NOVITA_API_KEY"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setenv("DEEPINFRA_API_KEY", "secret-value-123")
    a = run_year.parse_args(["--governance", "llm", "--roles-config", ROLES_EXAMPLE, "--mode", "live",
                             "--agent", "llm:anthropic:sonnet", "--out", str(tmp_path)])
    a.requested_mode = "live"
    with pytest.raises(SystemExit) as ei:
        run_year.prepare_governance(a)
    msg = str(ei.value)
    assert "ANTHROPIC_API_KEY" in msg and "NOVITA_API_KEY" in msg and "secret-value-123" not in msg
    assert "DEEPINFRA_API_KEY" not in msg
