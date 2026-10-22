"""
The rulebook revision the simulated companies operate under (Realism revisions R1 and R2).

The five released 5.15.0 rulebooks stay byte-identical, because other
manuscripts cite figures computed on them. The simulation instead adopts, by
addition, a dated overlay: per-provision field values with a reason. The overlay
is applied to the canon (tier rule, `authority.py`) and to the DJ engine
(A6 reads `absolute`) alike, so every arm sees the same rulebook.

R1 (22 October 2026) adopted five draft amendments already on file. Each
reclassifies an absolute that rests on internal practice rather than an external
instrument.

R2 (22 October 2026, after a four-reviewer external review) adopted the 19
consensus overlays:
  - 16 more such absolutes become non-absolute. Their only footing is a voluntary
    framework, an internal "floor", a benchmark or risk architecture.
  - MF-611 (TCPA consent) becomes absolute, matching VP-CC-001 on the same statute.
  - DV-408 (Data Act Art. 29, applying from 12 January 2027) and DV-435 (CRA
    Art. 14, applying from 11 September 2026) come into force for the 2027 year.

A released absolute overlaid as non-absolute keeps a T1 floor in the canon
(`released_absolute`); it is never tradable for a business reason.

`amended_provisions(provisions)` returns the provision dicts with the overlay
applied. `amend_engine(provisions)` applies the `absolute` changes to the
engine's loaded `Provision` objects in place. The engine reads no status.
"""

from __future__ import annotations

REVISION = "R2"

# provision id -> (revision, source of the change, reason)
DEMOTED_TO_ORDINARY = {
    # R1: draft amendments on file
    "DV-341": ("R1", "DCVigil PA-07", "internal risk-architecture floor; governance board is the deciding authority"),
    "DV-342": ("R1", "DCVigil PA-07", "practice policy; governance board is the deciding authority"),
    "FL-BS-001": ("R1", "FrontierLLM PA-05", "risk architecture only; policy board is the exception authority"),
    "SF-WI-001": ("R1", "SemiFab PA-04", "operational integrity floor; SF-EX-003 and SF-QS-002 carry the binding cases"),
    "SF-WI-002": ("R1", "SemiFab PA-04", "operational integrity floor; SF-EX-003 and SF-QS-002 carry the binding cases"),
    # R2: consensus of the external review (each supported by at least two reviewers, opposed by none)
    "VP-PO-001": ("R2", "review R1,R3", "cites only a clinical safety floor; internal standard of the medical director"),
    "SF-SG-002": ("R2", "review R1,R3", "a SECS/GEM message id cited as a fact, not an instrument"),
    "SF-SS-001": ("R2", "review R1,R3,R4", "SLSA and in-toto are voluntary"),
    "FL-MB-001": ("R2", "review R1,R3,R4", "risk architecture plus a voluntary OpenSSF specification"),
    "FL-MB-002": ("R2", "review R1,R3", "OpenSSF model signing is voluntary"),
    "FL-MB-003": ("R2", "review R1,R3,R4", "the safetensors threat model is library documentation"),
    "FL-LS-001": ("R2", "review R1,R3", "internal risk architecture (insecure output handling)"),
    "FL-LS-002": ("R2", "review R1,R3", "a benchmark plus practice policy"),
    "FL-EV-001": ("R2", "review R1,R3", "benchmark-hygiene practice"),
    "FL-FG-001": ("R2", "review R1,R3,R4", "a circuit breaker is engineering practice; the T1 floor keeps it above T2"),
    "FL-IP-001": ("R2", "review R1,R3", "copyleft clearance is a licence-review decision"),
    "FL-SC-001": ("R2", "review R1,R3,R4", "SLSA is voluntary"),
    "FL-PI-001": ("R2", "review R2,R3", "EDPB Opinion 28/2024 is case by case, not a per-se bar"),
    "DV-313": ("R2", "review R2,R3", "the GDPR imposes no residency duty; DCVigil PA-01 already re-cites it to contract"),
    "DV-321": ("R2", "review R2,R3", "SOC 2 and ISO 27001 set no seven-year retention; immutability stays T0 via DV-339, DV-412"),
    "DV-343": ("R2", "review R1,R3", "NIST SP 800-53 does not bind a private SOC 2 firm; duplicates DV-337"),
}
PROMOTED_TO_ABSOLUTE = {
    "MF-611": ("R2", "review R2,R3", "TCPA consent: the same statute and duty as VP-CC-001, which is absolute"),
}
STATUS_IN_FORCE = {
    "DV-408": ("R2", "review R1,R2,R3,R4", "Data Act Art. 29(1) applies from 12 January 2027"),
    "DV-435": ("R2", "review R3,R4", "CRA Art. 14 reporting applies from 11 September 2026"),
}


def amended_provisions(provisions: list) -> list:
    out = []
    for p in provisions:
        pid = p.get("id")
        q = dict(p)
        changed = []
        if pid in DEMOTED_TO_ORDINARY and p.get("absolute"):
            q["absolute"] = False
            q["released_absolute"] = True
            changed.append(DEMOTED_TO_ORDINARY[pid][0])
        if pid in PROMOTED_TO_ABSOLUTE and not p.get("absolute"):
            q["absolute"] = True
            changed.append(PROMOTED_TO_ABSOLUTE[pid][0])
        if pid in STATUS_IN_FORCE and p.get("status") != "in_force":
            q["status"] = "in_force"
            changed.append(STATUS_IN_FORCE[pid][0])
        if changed:
            q["amended_by"] = ",".join(sorted(set(changed)))
        out.append(q)
    return out


def amend_engine(provisions: dict) -> dict:
    """In place on the engine's {id: Provision}; returns it."""
    for pid in DEMOTED_TO_ORDINARY:
        p = provisions.get(pid)
        if p is not None and getattr(p, "absolute", False):
            p.absolute = False
    for pid in PROMOTED_TO_ABSOLUTE:
        p = provisions.get(pid)
        if p is not None and not getattr(p, "absolute", False):
            p.absolute = True
    return provisions


__all__ = ["REVISION", "DEMOTED_TO_ORDINARY", "PROMOTED_TO_ABSOLUTE", "STATUS_IN_FORCE",
           "amended_provisions", "amend_engine"]
