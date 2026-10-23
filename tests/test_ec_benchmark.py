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
