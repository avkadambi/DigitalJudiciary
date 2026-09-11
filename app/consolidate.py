# -*- coding: utf-8 -*-
"""Consolidation — Definitions 15 and 16 of Chapter 5.

NUMBERING. RA-3's memo called these Definitions 14 and 15. So did RA-2's, of
two different objects: the Reporter and the Acknowledgement. Both memos were
camera-ready and both were wrong about the other, and the Docket needed a
number as well. D12 ratified one allocation by order of first appearance in
the chapter — 14 Docket, 15 consolidation signature, 16 consolidation class,
17 Reporter, 18 Acknowledgement, 19 audit register — and this file uses it.
Renumbering was refused because it would break every external citation to the
JURIX and *AI and Law* versions; the memos are substituted into the allocation
instead.

`Classify` is pipeline machinery of the same kind as the intake router that
sends control-plane changes to the draft-amendment channel under A3. It reads
published parameters and recorded facts, it takes **no authority as argument**,
and it produces a type — `ClassSet` — that no authority produces, so A2's
non-overlap of output types is not disturbed.

Why that matters, in one line: forming a class decides which unit's record
becomes law and which N-1 are disposed without one, which is a power over
admission. Definition 7 exercises that power by procedural predicate and never
by judgment, and an adjudicating instance that formed classes would hold a
power A1-A4 do not confer. CC-22 is how a conformance run asserts it.

The widest class this module can form is signature equality (Definition 15).
The *valuable* class — units a single holding would govern — is at the
containment grain, and it cannot be formed without the holding, which is the
adjudicator's own product. That class is refused here deliberately; see
`REPRODUCE.md` and the chapter's §4.10 for what the refusal costs.
"""
from __future__ import annotations

import hashlib
import json
import uuid
from typing import Iterable

# The identity of the pipeline service that forms classes. It holds no
# credential of any authority class, and CC-22(a) asserts that against the
# ledger's own historical role table rather than taking this string on trust.
PRODUCER_SERVICE = "svc:classify"

# Constitutional parameters, versioned with the rulebook and amendable only
# through Legislate. They are defaults here in the same sense theta is a
# default here: a deployment sets them in its constitution.
DEFAULT_N0 = 2
DEFAULT_DELTA_SECONDS = 24 * 3600


def factor_vocabulary(provision: dict) -> set[str]:
    """F_p — the polarised factor vocabulary of Chapter 4 Definition A.

    In this build a provision's vocabulary is exactly the factor set its
    published policy names. That is the whole of what the constitution says
    about p, so it is the whole of what a signature may read.
    """
    policy = provision.get("policy") or {}
    vocab: set[str] = set()
    for key in ("deny_if_any", "permit_if_any", "require_all"):
        vocab |= set(policy.get(key) or [])
    return vocab


def signature(provision_id: str, rulebook_version: str,
              facts: Iterable[str], vocab: set[str]) -> tuple:
    """Definition 15. `Sig(u) = (p, rulebook_version, facts(c) INTERSECT F_p)`.

    Three exclusions are deliberate and each has its reason. Not premise-
    identical: `premise` is authored at resolution and does not exist for a
    pending unit. Not facts-identical: `facts(c)` may carry factors of other
    provisions the case engages, and two units alike under p would then fail
    to class on differences irrelevant to p. Not containment-based: see the
    module docstring.
    """
    return (provision_id, rulebook_version,
            tuple(sorted(set(facts) & vocab)))


def snapshot_hash(store_rows: Iterable[dict]) -> str:
    """Content hash pinning S_t. Every member of a class is resolved against
    this exact store, and the class artefact records the hash so CC-19 can
    recompute `resolve` against it rather than against the store as it later
    became."""
    payload = sorted(r["content_hash"] for r in store_rows)
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def _rep_key(unit: dict) -> tuple:
    """The published total order: lodgement timestamp, then unit identifier.
    Nothing about the unit's content enters it, which is what makes CC-22(c)
    — permute the input and get the same representative — a real check."""
    return (unit["lodged_at"], unit["unit_id"])


def classify(docket: list[dict], store: list[dict], provisions: dict,
             n0: int = DEFAULT_N0, delta_seconds: int = DEFAULT_DELTA_SECONDS,
             now: str | None = None, resolve_state=None) -> list[dict]:
    """`Classify : Docket x Store x N x N -> ClassSet` (Definition 16).

    `docket` is D_t: units lodged and undecided at t whose lodgement time lies
    in [t - Delta, t]. A unit is a dict with `unit_id`, `case_id`,
    `provisions`, `facts`, `lodged_at`, and `resolve_result`, the last being
    the disposition `resolve` returned for it against the pinned store —
    'none_empty', 'none_all_distinguished', 'none_tie', 'none_degraded' or
    'bound'. Clause (d) admits the first two: they are the plain `none`. It
    excludes `none_tie` deliberately and for a legislative reason rather than
    an authority one — a tie escalates AND refers the unbroken conflict to the
    Lawmakers, so consolidating N ties would emit one referral where the
    docket generated N. It excludes `none_degraded` because a degraded
    resolution is not a resolution.

    `store` is S_t, a list of live record rows.

    `resolve_state` is how clause (d) is evaluated: a callable
    (provision_id, facts) -> controlling_state that MUST NOT write anything,
    since CC-22(b) requires that no judgment invocation for any member predate
    the class artefact. Where it is not supplied the unit's own
    `resolve_result` is read instead, which is what a caller replaying a
    recorded docket does. Clause (d) is applied last, after (a), (b), (c) and
    (e), so that no probe is run for a group those clauses have already
    excluded.

    Returns the classes, each carrying everything the artefact records. No
    `Authorities` argument appears anywhere in this signature, and none is
    read.
    """
    snap = snapshot_hash(store)

    # Clauses (b) and (c) are unit-level and are applied before grouping,
    # because a unit they exclude must not even appear in a class's member
    # list. (b): a multi-provision unit has two signatures and could join two
    # classes with different representatives, and `resolve` returns a single
    # controlling record for the whole case — resolving that conflict is a
    # judgment, and the specification refuses it. (c): a floor-violating unit
    # is short-circuited by A6 individually and never joins anything.
    eligible = []
    for u in docket:
        if len(u["provisions"]) != 1:
            continue                                   # clause (b)
        p = u["provisions"][0]
        prov = provisions.get(p)
        if prov is None:
            continue
        if prov.get("absolute") and (
                set(u["facts"]) & set((prov.get("policy") or {})
                                      .get("deny_if_any") or [])):
            continue                                   # clause (c)
        eligible.append((u, prov))

    groups: dict[tuple, list[dict]] = {}
    for u, prov in eligible:
        sig = signature(u["provisions"][0], u["rulebook_version"],
                        u["facts"], factor_vocabulary(prov))
        groups.setdefault(sig, []).append(u)

    # Clause (e), computed once over the pinned store: a live record already
    # covering the signature means no class forms. This is the clause the
    # `|Rules| * 2^kappa` ceiling of Proposition A_cons(ii) rests on, and
    # CC-21 is what makes it a bound rather than a hope.
    covered = set()
    for r in store:
        prov = provisions.get(r["provision_id"])
        if prov is None:
            continue
        covered.add(signature(r["provision_id"], r["rulebook_version"],
                              json.loads(r["facts"]),
                              factor_vocabulary(prov)))

    classes = []
    for sig, members in sorted(groups.items()):
        if len(members) < n0:                          # clause (a)
            continue
        if sig in covered:                             # clause (e)
            continue
        members = sorted(members, key=_rep_key)
        span = _span_seconds([m["lodged_at"] for m in members])
        if span > delta_seconds:
            continue                                   # co-pendency window
        rep = members[0]
        # Clause (d): the plain value, never `none(tie)`. A tie escalates AND
        # refers the unbroken conflict to the Lawmakers; consolidating N ties
        # would emit one referral where the docket generated N, suppressing
        # exactly the signal about how often a conflict bites that the
        # Lawmakers need. The exclusion is a legislative-signal argument and
        # not an authority one, and the text says so.
        state = (resolve_state(sig[0], rep["facts"]) if resolve_state
                 else rep.get("resolve_result"))
        if state not in ("none_empty", "none_all_distinguished"):
            continue
        classes.append({
            "class_id": "cls-" + uuid.uuid5(
                uuid.NAMESPACE_URL,
                f"{snap}|{sig[0]}|{sig[1]}|{'.'.join(sig[2])}").hex[:16],
            "snapshot_hash": snap,
            "rulebook_version": sig[1],
            "provision_id": sig[0],
            "signature": list(sig[2]),
            "n0": n0,
            "delta_seconds": delta_seconds,
            "members": [m["unit_id"] for m in members],
            "docket": [u["unit_id"] for u in docket],
            "representative": rep["unit_id"],
            "producer_service": PRODUCER_SERVICE,
            "formed_at": now,
        })
    return classes


def _span_seconds(stamps: list[str]) -> float:
    """Width of the lodgement window the members actually occupy. A class may
    only form over units co-pending inside Delta; a unit lodged after the
    boundary is eligible for the next snapshot and never joins a formed one."""
    ts = sorted(_parse(t) for t in stamps)
    return (ts[-1] - ts[0]).total_seconds()


def _parse(stamp: str):
    from datetime import datetime
    txt = stamp.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(txt)
    except ValueError:
        # The ledger writes six-digit fractional seconds with a trailing
        # "000"; trim to what fromisoformat accepts rather than guessing.
        head, _, tail = txt.partition(".")
        digits = "".join(c for c in tail if c.isdigit())[:6]
        rest = tail[len(digits):].lstrip("0123456789")
        return datetime.fromisoformat(f"{head}.{digits or '0'}{rest}")


class ClassRegistry:
    """The pipeline service that forms and records consolidation classes.

    It owns its own writer, on the package's sole-writer discipline: the Gate
    writes the ledger and nothing else does, and this object writes the class
    artefacts and nothing else does. It is a separate object rather than a
    method on the adjudicator for the reason CC-22 exists — an adjudicating
    instance that formed classes would hold a power over admission that
    A1-A4 do not confer, and keeping the capability in a different object is
    how that is enforced rather than merely asserted.
    """

    def __init__(self, path: str | None = None):
        from . import db
        self._w = db.open_writer(path)

    def write(self, cls: dict) -> None:
        write_class(self._w, cls)
        self._w.commit()

    def classes(self) -> list[dict]:
        return [dict(r) for r in self._w.execute(
            "SELECT * FROM consolidation_class ORDER BY formed_at, class_id")]


def write_class(conn, cls: dict) -> None:
    """Persist a class artefact. Append-only at the schema; the triggers
    refuse an UPDATE and a DELETE."""
    conn.execute(
        "INSERT INTO consolidation_class (class_id, snapshot_hash,"
        " rulebook_version, provision_id, signature, n0, delta_seconds,"
        " members, docket, representative, producer_service, formed_at)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (cls["class_id"], cls["snapshot_hash"], cls["rulebook_version"],
         cls["provision_id"], json.dumps(cls["signature"]), cls["n0"],
         cls["delta_seconds"], json.dumps(cls["members"]),
         json.dumps(cls["docket"]), cls["representative"],
         cls["producer_service"], cls["formed_at"]))
