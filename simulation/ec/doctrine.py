"""
Doctrine: holdings written back as glosses (EC §3.5, §3.6; DESIGN §2.5).

A Bench holding does not change the constitution. It is written to the
engaged entry's *gloss*: the holding is appended, and a denial on a T1 class
bars that class from further dispensation (`no_waiver_classes`), so the next
tokenless act of the same kind is blocked at the gate without another hearing.
When a T1 class has been denied `K_CODIFY` times the class *codifies*: the
registry issues no further tokens for it.

`write_gloss` touches `entry.gloss` and nothing else. Tier, office and violate
factors are fixed at build time; `assert_gloss_invariants` is the check EC-08
runs over a canon before and after a year of doctrine.

`aggregate_disclosures` is the only examen-derived input the Bench receives:
counts, with no act id and no narrative (EC-09).
"""

from __future__ import annotations

from .canon import Canon

K_CODIFY = 3
HOLDING_FIELDS = ("day", "case", "holding", "act_class", "outcome")
FIXED_FIELDS = ("tier", "violate_factors", "kind", "office")


def gloss_oracle(entry, holding: dict, day: int) -> dict:
    """The clerk's answer key (governance build DC-D1), read-only: the holding
    as it is appended to the gloss, and whether it bars its class."""
    h = {k: holding.get(k) for k in HOLDING_FIELDS}
    h["day"] = day
    if h["act_class"] is None:
        h["act_class"] = entry.act_class
    if h["outcome"] is None:
        h["outcome"] = h["holding"]
    bars = entry.tier == "T1" and h["holding"] == "deny" and h["act_class"] not in entry.gloss.no_waiver_classes
    return {"holding": h, "bars_class": bool(bars)}


def write_gloss(canon: Canon, entry_id: str, holding: dict, day: int) -> None:
    """Append a holding to the entry's gloss. On a deny of a T1 class, bar the
    class from dispensation. Bumps `gloss.version`."""
    e = canon.entry(entry_id)
    g = gloss_oracle(e, holding, day)
    h = g["holding"]
    e.gloss.holdings.append(h)
    if g["bars_class"]:
        e.gloss.no_waiver_classes.append(h["act_class"])
    e.gloss.version += 1


def codify_oracle(entry, k: int = K_CODIFY) -> bool:
    """The lawmaker's answer key (governance build LW-D1), read-only: a T1 entry
    whose own act class has been denied `k` times and is not yet codified."""
    if entry.tier != "T1" or entry.gloss.codified:
        return False
    denies = sum(1 for h in entry.gloss.holdings if h.get("holding") == "deny" and h.get("act_class") == entry.act_class)
    return denies >= k


def maybe_codify(canon: Canon, entry_id: str, k: int = K_CODIFY) -> bool:
    """Codify a T1 entry whose own act class has been denied `k` times. Returns
    True only when this call codified it."""
    e = canon.entry(entry_id)
    if not codify_oracle(e, k):
        return False
    e.gloss.codified = True
    e.gloss.version += 1
    return True


def aggregate_disclosures(entries: list, day: int) -> dict:
    """Counts of examen entries by reported event, tier and canon entry. No
    act id, no reason text, no narrative."""
    by_event: dict[str, int] = {}
    by_tier: dict[str, int] = {}
    by_entry: dict[str, int] = {}
    for en in entries:
        by_event[en.reported_event] = by_event.get(en.reported_event, 0) + 1
        t = en.tier or "none"
        by_tier[t] = by_tier.get(t, 0) + 1
        if en.entry:
            by_entry[en.entry] = by_entry.get(en.entry, 0) + 1
    return {"day": day, "n": len(entries), "by_reported_event": by_event, "by_tier": by_tier,
            "by_entry": by_entry}


def assert_gloss_invariants(canon_before: dict, canon_after: dict) -> list:
    """Entries whose tier, violate_factors, kind or office changed between two
    canon dicts, plus a marker if the canon version moved or an entry appeared
    or vanished. Empty list = pass."""
    before = {e["id"]: e for e in canon_before.get("entries") or []}
    after = {e["id"]: e for e in canon_after.get("entries") or []}
    changed = []
    for eid in sorted(set(before) | set(after)):
        b, a = before.get(eid), after.get(eid)
        if b is None or a is None:
            changed.append(eid)
            continue
        if any(b.get(f) != a.get(f) for f in FIXED_FIELDS) or b.get("canon_version") != a.get("canon_version"):
            changed.append(eid)
    if canon_before.get("version") != canon_after.get("version"):
        changed.append("<canon_version>")
    return changed
