"""Scenario coverage — the architect's catalogue against the executed corpus.

Every provision carries `scenarios`, a list of ids from
constitution/scenarios.json (the architect's catalogue of legal, compliance,
reputational and safety scenario classes). This module computes, from the
corpus as built, how many cases exercised each scenario in each mechanism
(case-category letter), and which required mechanisms are missing. VC-50
calls `missing()`; `matrix()` is what docs/COVERAGE.md and the cross-pack
coverage tool print.

The mechanism letters are the first letter of the case category:

    A routine (compliant touch — the guard item for the scenario)
    B plain deny (an ordinary provision violated)
    F absolute short-circuit (a floor violated)
    P pressure twin (PACT mechanism must not move the answer)
    V like-case pair (consistency)
    G risk-owner acceptance with sunset
    W cross-jurisdiction
    H control-plane (rulebook governance; counted for every H case)

A scenario applies to a pack when at least one provision maps to it. For each
applicable scenario the catalogue names the mechanisms in which it must be
exercised; a floor mechanism (F) is demanded only when the pack maps at least
one ABSOLUTE provision to the scenario, and its absence in that case is a
constitution gap, reported as such.

Pure standard library.
"""

from __future__ import annotations

import json
import os

MECHANISMS = ("A", "B", "F", "P", "V", "G", "W", "H")


def load_catalogue(root):
    with open(os.path.join(root, "constitution", "scenarios.json")) as fh:
        return json.load(fh)


def provision_scenarios(rulebook):
    return {p["id"]: list(p.get("scenarios") or []) for p in rulebook["provisions"]}


def _letter(case):
    return case["category"].split("-", 1)[0]


def matrix(rulebook, cases, catalogue):
    """scenario id -> {mechanism letter -> case count}, plus per-scenario meta."""
    ps = provision_scenarios(rulebook)
    absolute = {p["id"] for p in rulebook["provisions"] if p["absolute"]}
    applicable = {}
    for pid, lst in ps.items():
        for s in lst:
            applicable.setdefault(s, {"provisions": set(), "absolute": set()})
            applicable[s]["provisions"].add(pid)
            if pid in absolute:
                applicable[s]["absolute"].add(pid)
    counts = {s: {m: 0 for m in MECHANISMS} for s in applicable}
    for c in cases:
        L = _letter(c)
        if L not in MECHANISMS:
            continue
        if L == "H":
            for s in applicable:
                counts[s]["H"] += 1
            continue
        if L == "F":
            engaged = [c["expect"].get("absolute_provision")] if c["expect"].get("absolute_provision") else c["rules"][:1]
        else:
            engaged = c["rules"][:1]
        seen = set()
        for pid in engaged:
            for s in ps.get(pid, []):
                if s not in seen:
                    counts[s][L] += 1
                    seen.add(s)
    return counts, applicable


def missing(rulebook, cases, catalogue):
    """[(scenario id, mechanism, reason)] for every required mechanism with no case.

    A corpus gap, not a constitution gap: where the catalogue expects a floor
    and this constitution maps no absolute provision to the scenario, no F
    case can exist and none is demanded here — `constitution_notes()` reports
    that separately, because it is a finding about the rulebook for the
    lawmakers, not a defect in the corpus.
    """
    counts, applicable = matrix(rulebook, cases, catalogue)
    by_id = {s["id"]: s for s in catalogue["scenarios"]}
    out = []
    for s, meta in sorted(applicable.items()):
        spec = by_id.get(s)
        if spec is None:
            out.append((s, "*", "scenario id not in the catalogue"))
            continue
        for m in spec["required_mechanisms"]:
            if m == "F" and not meta["absolute"]:
                continue
            if m in ("B", "G", "V") and not (meta["provisions"] - meta["absolute"]):
                # no ordinary provision maps here: nothing can be plainly denied,
                # risk-accepted or anchor a like-case pair. Reported by
                # constitution_notes(), not demanded of the corpus.
                continue
            # A required mechanism with no executed case is a coverage gap.
            if counts[s][m] == 0:
                out.append((s, m, "required mechanism has no case"))
    return out


def constitution_notes(rulebook, catalogue):
    """Scenarios the catalogue marks `floor` to which this constitution maps no
    absolute provision. Filed for the lawmakers; VC-50 prints them and does not
    fail on them."""
    _, applicable = matrix(rulebook, [], catalogue)
    by_id = {s["id"]: s for s in catalogue["scenarios"]}
    out = []
    for s, meta in sorted(applicable.items()):
        if by_id.get(s, {}).get("floor") and not meta["absolute"]:
            out.append(f"{s}: floor expected, no absolute provision mapped")
        if not (meta["provisions"] - meta["absolute"]):
            out.append(f"{s}: only absolute provisions mapped; no ordinary limb to deny, accept or pair")
    return out


def spec_selftest():
    """The check's own specification: a corpus that omits a required mechanism
    must be reported as missing it, and one that supplies every mechanism must
    not. A checker that cannot fail this is not a checker."""
    catalogue = {"scenarios": [
        {"id": "S-T1", "floor": True, "required_mechanisms": ["F", "A", "B"]},
        {"id": "S-T2", "floor": False, "required_mechanisms": ["A", "B"]},
    ]}
    rulebook = {"provisions": [
        {"id": "T-1", "absolute": True, "scenarios": ["S-T1"]},
        {"id": "T-2", "absolute": False, "scenarios": ["S-T1", "S-T2"]},
    ]}
    mk = lambda cat, pid: {"category": cat, "rules": [pid], "expect": {}}
    complete = [mk("F-absolute", "T-1"), mk("A-routine", "T-2"), mk("B-plain-deny", "T-2")]
    incomplete = [mk("A-routine", "T-2"), mk("B-plain-deny", "T-2")]  # no F
    ok_complete = missing(rulebook, complete, catalogue) == []
    gaps = missing(rulebook, incomplete, catalogue)
    ok_incomplete = ("S-T1", "F", "required mechanism has no case") in gaps
    return ok_complete and ok_incomplete, {"complete": ok_complete, "incomplete": ok_incomplete}
