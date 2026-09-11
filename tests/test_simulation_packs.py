"""Each simulation pack's own conformance suite (56 checks), plus Numerals (11), plus the digests."""
import hashlib
import json
import os

import pytest

from conftest import PACKS, ROOT, result_line, run

MANIFEST = json.load(open(os.path.join(ROOT, "simulation", "MANIFEST.json")))


@pytest.mark.parametrize("pack", PACKS)
def test_pack_conformance(pack):
    line = result_line(run(["harness/run_conformance.py"], cwd=os.path.join(ROOT, "simulation", pack)))
    assert line.strip() == f"RESULT: {MANIFEST['checks']['conformance_per_pack']}/{MANIFEST['checks']['conformance_per_pack']}", line


@pytest.mark.parametrize("pack", PACKS)
def test_pack_has_no_construction_anomalies(pack):
    man = json.load(open(os.path.join(ROOT, "simulation", pack, "corpus", "manifest.json")))
    assert man["construction_anomalies"] == 0
    assert man["cases"] == 6000


def test_numerals_conformance():
    line = result_line(run(["harness/run_federation_checks.py"], cwd=os.path.join(ROOT, "simulation", "numerals")))
    assert line.strip() == "RESULT: 11/11", line


def _digest_rows():
    for p in MANIFEST["packs"]:
        for rel, h in p["sha256"].items():
            yield p["directory"], rel, h
    for rel, h in MANIFEST["numerals"]["sha256"].items():
        yield "simulation/numerals", rel, h


@pytest.mark.parametrize("directory,rel,expected", list(_digest_rows()), ids=lambda v: v if isinstance(v, str) and "/" in v else None)
def test_manifest_digest(directory, rel, expected):
    path = os.path.join(ROOT, directory, rel)
    assert os.path.exists(path), path
    assert hashlib.sha256(open(path, "rb").read()).hexdigest() == expected, f"{directory}/{rel} differs from MANIFEST.json"


def test_composition_identical_across_packs():
    cats = None
    for pack in PACKS:
        man = json.load(open(os.path.join(ROOT, "simulation", pack, "corpus", "manifest.json")))
        c = dict(sorted(man["categories"].items()))
        if cats is None:
            cats = c
        assert c == cats, pack


@pytest.mark.slow
@pytest.mark.parametrize("pack", PACKS)
def test_pack_mutation_matrix(pack):
    line = result_line(run(["harness/mutation_matrix.py"], cwd=os.path.join(ROOT, "simulation", pack), timeout=3600))
    assert line.strip().startswith(f"RESULT: {MANIFEST['checks']['mutants']}/{MANIFEST['checks']['mutants']} faults killed"), line
