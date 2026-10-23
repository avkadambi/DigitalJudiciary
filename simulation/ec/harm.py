"""
Harm weights from the rulebook (benchmark build §3.5).

Leakage is weighted by the harm of the provision broken, read from the released
rulebook fields (after the R2 overlay of `rulebook_rev.py`) and
`authority.binding()`, never from EC's own tiers, so the scorecard carries no
home-field advantage for EC:

    100  the provision is absolute (after the R2 overlay)
     20  the citation is binding and the harm classes include legal, regulatory or safety
      5  an internal standard with a legal, regulatory or safety harm class
      1  everything else, including value entries other than VAL-ACC
     20  VAL-ACC

Sensitivities: `tier` (T0 100, T1 20, T2 5, T3 1), `flat` (every violation 1)
and `steep` (absolute 1,000, else as `rulebook`). The weights are assumptions on
an order-of-magnitude scale. Weight-1 (T3 and style) leakage is always reported
separately, so EC is never credited for enforcing its own house style.
"""

from __future__ import annotations

import json
import os

from .authority import binding
from .rulebook_rev import amended_provisions

SCHEMES = ("rulebook", "tier", "flat", "steep")
LRS = {"legal", "regulatory", "safety"}
TIER_WEIGHT = {"T0": 100, "T1": 20, "T2": 5, "T3": 1}


def weight(prov: dict | None, scheme: str = "rulebook", tier: str | None = None, entry_id: str | None = None) -> int:
    """The harm weight of one provision (a released rulebook dict, overlaid) or value entry."""
    if scheme not in SCHEMES:
        raise ValueError(f"unknown harm scheme {scheme!r}")
    if scheme == "flat":
        return 1
    if scheme == "tier":
        return TIER_WEIGHT.get(tier or "", 1)
    if prov is None:                                     # a value entry
        return 20 if str(entry_id or "").endswith("VAL-ACC") else 1     # VAL-ACC, under any company prefix
    if prov.get("absolute"):
        return 1000 if scheme == "steep" else 100
    lrs = bool(set(prov.get("harm_classes") or []) & LRS)
    if lrs and binding(prov.get("citation") or ""):
        return 20
    if lrs:
        return 5
    return 1


def load_rulebook(pack_dir: str) -> dict:
    with open(os.path.join(pack_dir, "constitution", "rulebook.json")) as fh:
        rb = json.load(fh)
    return {p["id"]: p for p in amended_provisions(rb["provisions"])}


def weights_for_pack(pack_dir: str, canon, scheme: str = "rulebook") -> dict:
    """{entry id: weight} for every canon entry (provisions and values)."""
    provs = load_rulebook(pack_dir)
    return {eid: weight(provs.get(eid), scheme, e.tier, eid) for eid, e in canon.entries.items()}


def change_weight(entry_ids: list, weights: dict) -> int:
    """The weight of an impermissible change: the largest weight among the entries it breaks."""
    ws = [weights.get(e, 1) for e in entry_ids or []]
    return max(ws) if ws else 1
