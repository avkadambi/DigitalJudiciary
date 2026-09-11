"""Build constitution/rulebook.json, constitution/factors.json and
constitution/parameters.json from the vocabulary module.

Deterministic: no randomness, no clock, no network.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import vocab  # noqa: E402

OUT = os.path.join(ROOT, "constitution")

RULEBOOK_VERSION = "vetpoc-rb-000001"
ORG_ID = "vetpoc"
ORG_NAME = "VetPOC"
CORPUS_VERSION = "2.1.0"

# Per-family charging threshold tau (Chapter 5 §4.4). Constitutional: changed
# only by a legislative enactment, never by the function that applies it (CC-29).
TAU = {
    "CS": 25, "VC": 25, "PO": 30, "PD": 30, "RB": 30, "SC": 40,
    "AI": 30, "AS": 35, "HA": 40, "RR": 30, "AW": 30, "GV": 25,
}


STATUSES = ("in_force", "deferred", "advisory", "readiness")


def slice_pool(pool, offset, count):
    """Deterministic contiguous slice with wraparound."""
    if not pool:
        return []
    return [pool[(offset + i) % len(pool)] for i in range(min(count, len(pool)))]


TAU.update(vocab.TAU_EXT)


def build():
    provisions = []
    family_index = {}
    for idx, _row in enumerate(vocab.PROVISIONS):
        pid, fam, title, absolute, citation, source = _row[:6]
        _meta = vocab.PROVISION_META[pid]
        status, origin = _meta["status"], _meta["origin"]
        if status not in STATUSES:
            raise SystemExit(f"{pid}: unknown status {status!r}")
        if absolute and status != "in_force":
            raise SystemExit(f"{pid}: a {status} provision cannot be absolute")
        f = vocab.FAMILIES[fam]
        n = family_index.get(fam, 0)
        family_index[fam] = n + 1
        comply = slice_pool(f["comply"], n * 3, 8)
        violate = slice_pool(f["violate"], n * 2, 5)
        slug = pid.lower().replace("-", "_")
        comply = comply + [f"{slug}_control_evidenced"]
        violate = violate + [f"{slug}_control_absent"]
        provisions.append(
            {
                "id": pid,
                "family": fam,
                "family_title": f["title"],
                "title": title,
                "absolute": absolute,
                "citation": citation,
                "source_status": source,
                "risk_framework": f["risk"],
                "status": status,
                "origin": origin,
                "scenarios": _meta["scenarios"],
                "harm_classes": _meta["harm_classes"],
                "tau": TAU[fam],
                "scope_domain": fam,
                "factors": {
                    "comply": sorted(set(comply)),
                    "violate": sorted(set(violate)),
                },
            }
        )

    rulebook = {
        "rulebook_version": RULEBOOK_VERSION,
        "corpus_version": CORPUS_VERSION,
        "name": "VetPOC Constitution",
        "description": (
            "An open constitution for veterinary practice-management and "
            "point-of-care software, expressed as ordinary and absolute "
            "provisions in the sense of Chapter 5, Definition 1 of the Digital "
            "Judiciary programme."
        ),
        "counts": {
            "provisions": len(provisions),
            "absolute": sum(1 for p in provisions if p["absolute"]),
            "families": len(vocab.FAMILIES),
            "in_force": sum(1 for p in provisions if p["status"] == "in_force"),
            "deferred": sum(1 for p in provisions if p["status"] == "deferred"),
            "advisory": sum(1 for p in provisions if p["status"] == "advisory"),
            "readiness": sum(1 for p in provisions if p["status"] == "readiness"),
            "shipped": sum(1 for p in provisions if p["origin"] == "shipped"),
            "base": sum(1 for p in provisions if p["origin"] == "base"),
            "extension": sum(1 for p in provisions if p["origin"] == "extension"),
            "scenario_extension": sum(1 for p in provisions if p["id"] in vocab.EXT_IDS),
            "scenario_extension_absolute": sum(1 for p in provisions if p["id"] in vocab.EXT_IDS and p["absolute"]),
        },
        "authorities": {
            "lawmakers": vocab.LAWMAKERS,
            "judges": vocab.JUDGES,
            "riskowner": vocab.RISK_OWNERS,
            "disjointness": "A1: the three classes are pairwise disjoint over the deployment lifetime.",
        },
        "standing_declaration": {
            "id": "STAND-0001",
            "scope": "global",
            "adverse_contest_standing_exists": True,
            "declared_by": "lawmaker:clinical-governance-board",
            "declared_at": 0,
            "note": (
                "A9 first limb. This corpus declares that a party holds contest "
                "standing adverse to grants, namely the practice compliance "
                "officer, so that the N-standing cases can exercise both "
                "postures. A deployment must replace this with its own fact."
            ),
        },
        "provisions": provisions,
    }

    parameters = {
        "theta": 0.25,
        "theta_note": "Retrieval threshold on premise coverage (Chapter 5 §4.6).",
        "N0": 2,
        "delta_days": 14,
        "consolidation_note": "Definition 16 class threshold and co-pendency window.",
        "escalation_ladder": ["J1", "J2", "J3", "riskowner"],
        "acceptance_expiry_days": 180,
        "amendable_only_by": "Legislate",
        "conformance_check_ids": [
            "VC-01", "VC-02", "VC-03", "VC-04", "VC-05", "VC-06", "VC-07",
            "VC-08", "VC-09", "VC-10", "VC-11", "VC-12", "VC-13", "VC-14",
            "VC-15", "VC-16", "VC-17", "VC-18", "VC-19", "VC-20", "VC-21",
            "VC-22", "VC-23", "VC-24", "VC-25", "VC-26",
        ],
    }

    factors = {}
    for p in provisions:
        factors[p["id"]] = p["factors"]

    os.makedirs(OUT, exist_ok=True)
    # The authority roster. A1 is a claim about people, so it cannot be checked
    # against a run unless the run can say which branch a principal held. The
    # roster is what CC-01 and CC-02 read; the schema follows the replication
    # package's demo/companies/<pack>/organizations.json.
    principals = []
    for a in vocab.LAWMAKERS:
        principals.append({"principal_id": a, "branch": "lawmakers",
                           "kind": "human", "role": a.split(":", 1)[1].replace("-", " ")})
    for a in vocab.JUDGES:
        principals.append({"principal_id": a, "branch": "judges",
                           "kind": "automated instance",
                           "role": a.split(":", 1)[1].replace("-", " ")})
    for a in vocab.RISK_OWNERS:
        principals.append({"principal_id": a, "branch": "riskowner",
                           "kind": "human", "role": a.split(":", 1)[1].replace("-", " ")})
    _write(os.path.join(OUT, "organizations.json"), {
        "organizations": [{"org_id": ORG_ID, "name": ORG_NAME,
                           "principals": principals}],
        "disjointness": ("A1. Each principal appears once and holds exactly one "
                         "branch. No principal appears under two, and the roster "
                         "is what CC-01 checks rather than an assurance in prose."),
        "founding_scope": ORG_ID,
    })

    _write(os.path.join(OUT, "proposed_amendments.json"),
           {"note": ("Findings against existing provisions, filed as draft "
                     "amendments rather than applied. Under Axiom A3 the only route "
                     "from a case — or from a corpus author — to a rule change is a "
                     "draft amendment the legislative process may adopt or reject."),
            "amendments": vocab.PROPOSED_AMENDMENTS})
    rulebook["scenario_catalogue"] = vocab.SCENARIO_CATALOGUE_META
    _write(os.path.join(OUT, "rulebook.json"), rulebook)
    _write(os.path.join(OUT, "parameters.json"), parameters)
    _write(os.path.join(OUT, "factors.json"), factors)

    print(
        f"constitution: {len(provisions)} provisions, "
        f"{rulebook['counts']['absolute']} absolute, "
        f"{sum(len(v['comply']) + len(v['violate']) for v in factors.values())} factor bindings"
    )


def _write(path, obj):
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2, sort_keys=False)
        fh.write("\n")


if __name__ == "__main__":
    build()
# --- scenario extension (corpus 2.0.0) ---
