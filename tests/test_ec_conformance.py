"""The EC conformance suite (EC-01..EC-12) on a fresh 45-day vetpoc pilot, and
the mutation matrix under --runslow (DESIGN §7)."""
from __future__ import annotations

import json
import os
import sys

import pytest

from conftest import ROOT, result_line, run

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import run_ec_conformance as conf   # noqa: E402
from simulation.ec import calendar as cal               # noqa: E402

CANON = os.path.join(ROOT, "simulation", "vetpoc-constitution-corpus", "constitution", "canon.json")
pytestmark = pytest.mark.skipif(not os.path.exists(CANON), reason="canon.json not built; run build_all_canons.py")


@pytest.fixture(scope="module")
def suite(tmp_path_factory):
    out = str(tmp_path_factory.mktemp("ec_conformance"))
    return conf.Suite("vetpoc", 11, "pressure_sensitive", 45, cal.DAYS, "A", None, out)


@pytest.fixture(scope="module")
def results(suite):
    return conf.run_checks(suite, quiet=True)


def test_conformance_twelve_of_twelve(results):
    failed = [(c["id"], c["detail"], c["sample"]) for c in results["checks"] if not c["pass"]]
    assert results["total"] == 12
    assert not failed, failed
    assert results["passed"] == 12


@pytest.mark.parametrize("cid", [cid for cid, _, _ in conf.CHECKS])
def test_each_check_passes(results, cid):
    c = next(c for c in results["checks"] if c["id"] == cid)
    assert c["pass"], f"{cid}: {c['detail']} {c['sample']}"


def test_no_check_is_vacuous(results):
    assert not any("VACUOUS" in c["detail"] for c in results["checks"])


def test_cli_reads_existing_results_and_writes_report(suite, results, tmp_path):
    """The CLI over --results reuses the fixture's runs (pilot and EC-07 seeds)
    and reproduces the in-process answer; the report lands next to them."""
    out = str(tmp_path / "aux")
    proc = run([os.path.join(ROOT, "simulation", "ec", "run_ec_conformance.py"), "--pack", "vetpoc", "--seed", "11",
                "--archetype", "pressure_sensitive", "--results", suite.out, "--out", out])
    assert proc.returncode == 0, proc.stdout[-2000:] + proc.stderr[-2000:]
    assert result_line(proc).startswith("RESULT: 12/12")
    rep = json.load(open(os.path.join(suite.out, "ec_conformance.json")))
    assert rep["passed"] == 12 and [c["id"] for c in rep["checks"]] == [cid for cid, _, _ in conf.CHECKS]
    assert rep["days"] == 45
    assert [c["detail"] for c in rep["checks"]] == [c["detail"] for c in results["checks"]]


@pytest.mark.slow
def test_mutation_matrix():
    proc = run([os.path.join(ROOT, "simulation", "ec", "mutation_matrix_ec.py"), "--days", "45"], timeout=1200)
    assert result_line(proc).startswith("RESULT: 8/8 faults killed, 2/2 controls survived"), proc.stdout[-3000:]
    assert proc.returncode == 0, proc.stdout[-3000:]
