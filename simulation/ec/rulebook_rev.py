"""
The rulebook revision the simulated companies operate under (Realism revision R1).

The five released 5.15.0 rulebooks stay byte-identical: other manuscripts cite
figures computed on them. The simulation instead adopts, by addition, the draft
amendments those rulebooks already carry on file that reclassify an absolute
provision resting on internal practice rather than on an external instrument.
A normal company does not treat its own engineering policy as beyond the reach
of everyone below the legislature (Definition 1): its policy owner can grant an
exception. Each adopted amendment is named here with its file and option, and
nothing else in any provision changes (title, factors, harm classes, tau).

`amended_provisions(provisions)` returns the rulebook's provision dicts with the
revision applied; `amend_engine(provisions)` applies it to the engine's loaded
`Provision` objects, so the DJ engine (A6) and the EC canon (tier rule) read the
same rulebook. With the absolute flag off, the tier rule places all five at T1
(each carries a safety harm), office `office:safety-lead`.
"""

from __future__ import annotations

REVISION = "R1"

# provision id -> (pack, amendment on file, the option adopted)
DEMOTED_TO_ORDINARY = {
    "DV-341": ("dcvigil", "PA-07", "reclassify as ordinary in AC; deciding authority is the platform governance board"),
    "DV-342": ("dcvigil", "PA-07", "reclassify as ordinary in AC; deciding authority is the platform governance board"),
    "FL-BS-001": ("frontierllm", "PA-05", "reclassify as ordinary with the policy board as the named exception authority"),
    "SF-WI-001": ("semifab", "PA-04", "demote to ordinary; SF-EX-003 and SF-QS-002 carry the absolute and contractual cases"),
    "SF-WI-002": ("semifab", "PA-04", "demote to ordinary; SF-EX-003 and SF-QS-002 carry the absolute and contractual cases"),
}


def amended_provisions(provisions: list) -> list:
    out = []
    for p in provisions:
        if p.get("id") in DEMOTED_TO_ORDINARY and p.get("absolute"):
            q = dict(p)
            pack, pa, option = DEMOTED_TO_ORDINARY[p["id"]]
            q["absolute"] = False
            q["amended_by"] = f"{REVISION}:{pa}"
            out.append(q)
        else:
            out.append(p)
    return out


def amend_engine(provisions: dict) -> dict:
    """In place on the engine's {id: Provision}; returns it."""
    for pid in DEMOTED_TO_ORDINARY:
        p = provisions.get(pid)
        if p is not None and getattr(p, "absolute", False):
            p.absolute = False
    return provisions


__all__ = ["REVISION", "DEMOTED_TO_ORDINARY", "amended_provisions", "amend_engine"]
