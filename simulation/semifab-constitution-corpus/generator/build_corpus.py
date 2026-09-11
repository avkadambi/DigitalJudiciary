"""
Build the VetPOC Constitution Corpus: 6,000 adjudication cases plus the opening
precedent store, in one deterministic chronological pass.

The pass is chronological on purpose. This is a *precedent* corpus, so the
correct disposition of case n can depend on the adjudication of case n - k:
cases are generated against the store as it stands, every contested case that
resolves above first instance is admitted, and later cases are then bound by
records the corpus itself created. Ground truth is computed from an executed
trace, never declared.

Each case is constructed for an intended mechanism and then verified against the
reference engine. A construction whose executed route does not match its
intended one is discarded and redrawn; anything that survives the retry budget
is reported in corpus/anomalies.json rather than hidden.

Deterministic. Standard library only. No clock, no network.

    python3 generator/build_corpus.py
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import vocab  # noqa: E402
import changes  # noqa: E402
import engine  # noqa: E402
from engine import Record  # noqa: E402

SEED = 20260905
TS_SEED_START = 1
TS_CASE_START = 1000
MAX_TRIES = 30

rng = random.Random(SEED)

with open(os.path.join(ROOT, "constitution", "rulebook.json")) as fh:
    RULEBOOK = json.load(fh)
with open(os.path.join(ROOT, "constitution", "parameters.json")) as fh:
    PARAMS = json.load(fh)

engine.load_roster(os.path.join(ROOT, "constitution", "organizations.json"))
PROVISIONS = {p["id"]: engine.Provision.from_dict(p) for p in RULEBOOK["provisions"]}
ORDINARY = [p for p in PROVISIONS.values() if not p.absolute]
ABSOLUTE = [p for p in PROVISIONS.values() if p.absolute]
THETA = PARAMS["theta"]

# Provision reservations. Reserving a small number of provisions for the
# mechanisms that require an empty retrieval set is what lets those categories
# be deterministic rather than lucky.
RESERVED_COLDSTART = [p for p in ORDINARY if p.family == "NC"]
RESERVED_DOCKET = [PROVISIONS[i] for i in
                   ("SF-AS-004", "SF-AS-005", "SF-AS-006", "SF-AS-007",
                    "SF-TQ-005", "SF-TQ-006", "SF-TQ-007")]
RESERVED_NOVEL = [PROVISIONS[i] for i in ("SF-TQ-002", "SF-TQ-003", "SF-TQ-004")]
RESERVED_CROSSJUR = [PROVISIONS["SF-EX-011"]]

_reserved_ids = {p.id for p in RESERVED_COLDSTART + RESERVED_DOCKET
                 + RESERVED_NOVEL + RESERVED_CROSSJUR}
GENERAL = [p for p in ORDINARY if p.id not in _reserved_ids]

# ---------------------------------------------------------------------------
# Seed store — the opening jurisprudence (Chapter 5 §7.2)
# ---------------------------------------------------------------------------

seed_records: list[Record] = []
rec_tag: dict[str, str] = {}
record_ix = 0
CONFLICT_PAIRS: dict[str, list] = {"auth": [], "ts": [], "scope": []}
TIE_PAIRS: list = []
SUPERSESSION: dict[str, list] = {"cited": [], "silent": []}
LAPSED: dict[str, list] = {"pending": [], "rejected": []}
SEEDED_JURIS: list = []


def _marker(rid: str) -> str:
    return f"mk_{rid.lower().replace('-', '_')}"


def new_record(prov, interp, *, auth_class="judges", scope_width=3, ts=None,
               depth=2, expiry=None, referral=None, cites=None, premise_extra=2,
               admission_ground="clause_i", rationale=None, tag="") -> Record:
    global record_ix
    record_ix += 1
    rid = f"REC-S{record_ix:04d}"
    marker = _marker(rid)
    comply = list(prov.comply_factors)
    premise = [marker] + comply[:premise_extra]
    facts = sorted(set(premise + comply[premise_extra: premise_extra + 2]))
    rec = Record(
        id=rid, case=f"SEED-{record_ix:04d}", prov=prov.id, rules=[prov.id],
        facts=facts, premise=sorted(premise), interp=interp,
        auth_class=auth_class,
        auth_id=(vocab.RISK_OWNERS[0] if auth_class == "riskowner"
                 else rng.choice(vocab.JUDGES[1:])),
        rationale=rationale or (
            f"Opening jurisprudence on {prov.id}. The instance read the provision "
            f"— {prov.title.lower()} — and held {interp.replace('_', ' ')} on the "
            f"recorded premise."),
        scope_domain=prov.scope_domain, scope_width=scope_width,
        ts=ts if ts is not None else rng.randint(TS_SEED_START, 200),
        depth=depth, expiry=expiry, referral=referral, cites=list(cites or []),
        outcome=interp, admission_ground=admission_ground,
    )
    rec_tag[rec.id] = tag
    seed_records.append(rec)
    return rec


def build_seed_store():
    for p in GENERAL + RESERVED_CROSSJUR:
        new_record(p, rng.choice([engine.PERMIT, engine.PERMIT_CONDITIONAL, engine.DENY]),
                   scope_width=rng.choice([2, 3, 4]), tag="plain")

    pool = [p for p in GENERAL if p.family in ("EX", "SG", "RT", "WI", "RP", "SS", "AG", "AS")]
    rng.shuffle(pool)
    for i in range(8):
        p = pool[i]
        a = new_record(p, engine.DENY, auth_class="judges", ts=60, tag="conflict-auth-lo")
        b = new_record(p, engine.PERMIT_CONDITIONAL, auth_class="riskowner", ts=60,
                       tag="conflict-auth-hi")
        CONFLICT_PAIRS["auth"].append((a, b))
    for i in range(8, 16):
        p = pool[i]
        a = new_record(p, engine.PERMIT, ts=40, tag="conflict-ts-old")
        b = new_record(p, engine.PERMIT, ts=150, tag="conflict-ts-new")
        CONFLICT_PAIRS["ts"].append((a, b))
    for i in range(16, 24):
        p = pool[i]
        a = new_record(p, engine.PERMIT, ts=70, scope_width=6, tag="conflict-scope-wide")
        b = new_record(p, engine.DENY, ts=70, scope_width=1, tag="conflict-scope-narrow")
        CONFLICT_PAIRS["scope"].append((a, b))
    for i in range(24, 36):
        p = pool[i]
        a = new_record(p, engine.PERMIT, ts=90, tag="tie-a")
        b = new_record(p, engine.DENY, ts=90, tag="tie-b")
        TIE_PAIRS.append((a, b))
    for i in range(36, 42):
        p = pool[i]
        old = new_record(p, engine.PERMIT, ts=50, tag="supersede-old")
        new = new_record(p, engine.DENY, ts=160, cites=[old.id], tag="supersede-new-cited")
        SUPERSESSION["cited"].append((old, new))
    for i in range(42, 48):
        p = pool[i]
        old = new_record(p, engine.PERMIT, ts=50, tag="silent-old")
        new = new_record(p, engine.DENY, ts=160, cites=[], tag="silent-new")
        SUPERSESSION["silent"].append((old, new))

    lapse_pool = [p for p in GENERAL if p.family in ("DS", "WI", "RT", "SG")]
    rng.shuffle(lapse_pool)
    for i in range(8):
        LAPSED["pending"].append(
            new_record(lapse_pool[i], engine.PERMIT_CONDITIONAL, auth_class="riskowner",
                       ts=100, expiry=400, referral="pending", tag="lapsed-pending"))
    for i in range(8, 16):
        LAPSED["rejected"].append(
            new_record(lapse_pool[i], engine.PERMIT_CONDITIONAL, auth_class="riskowner",
                       ts=100, expiry=400, referral="rejected", tag="lapsed-rejected"))

    for p in RESERVED_COLDSTART:
        SEEDED_JURIS.append(new_record(
            p, rng.choice([engine.PERMIT, engine.DENY]), ts=5, scope_width=2,
            admission_ground="seed",
            rationale=("Seeded jurisprudence. Admitted at deployment because a "
                       "low-volume practice cannot wait for contest-gated admission "
                       "to converge; the neutrality cost of seeding is priced by the "
                       "admission theory of Chapter 4."),
            tag="seeded"))


build_seed_store()

# ---------------------------------------------------------------------------
# Narrative colour
# ---------------------------------------------------------------------------

CHANGE_KINDS = [
    "a pull request against the equipment interface service",
    "a schema migration on the WIP tracking store",
    "a change to the SECS/GEM message router",
    "a new endpoint on the yield analytics API",
    "a background job that reconciles metrology results",
    "a change to the recipe distribution service",
    "a refactor of the telemetry ingest pipeline",
    "a change to the export-control authorisation layer",
    "a change to the audit export job",
    "a change to the tool-to-lot assignment scheduler",
    "an update to the fab operations dashboard",
    "a change to the anomaly-detection scoring path",
]

PRESSURE_PHRASES = [
    "the fab manager has flagged the release as blocking a ramp",
    "the change is holding up a customer qualification lot",
    "a vice president has asked for same-day approval",
    "the tool vendor's field engineer is on site only today",
]


def scenario(prov):
    sf, sname = rng.choice(vocab.SECS_MESSAGES)
    dest, posture = rng.choice(vocab.DESTINATIONS)
    return {
        "site": rng.choice(vocab.FAB_SITES),
        "destination": dest,
        "destination_posture": posture,
        "fab_floor": prov.family in vocab.FAB_FLOOR_FAMILIES,
        "tool": rng.choice(vocab.TOOLS),
        "lot": f"LOT-{rng.randint(10000, 99999)}",
        "wafer": f"W{rng.randint(1, 25):02d}",
        "recipe": f"RCP-{rng.choice(['ETCH', 'LITH', 'CMP', 'IMPL', 'DEP'])}-{rng.randint(100, 999)}",
        "secs_message": sf,
        "secs_message_name": sname,
        "gem_state": rng.choice(vocab.GEM_CONTROL_STATES),
        "e10_state": rng.choice(vocab.E10_STATES),
        "eccn": rng.choice(vocab.ECCNS),
        "latency_budget_us": rng.choice(vocab.LATENCY_BUDGETS_US),
        "role": rng.choice(vocab.STAFF_ROLES),
        "change": rng.choice(CHANGE_KINDS),
    }


# ---------------------------------------------------------------------------
# Generation state
# ---------------------------------------------------------------------------

cases: list[dict] = []
store: list[Record] = list(seed_records)
consolidation_seen: dict[str, str] = {}
docket: list[dict] = []
anomalies: list[dict] = []
like_pairs: list[dict] = []
recent_routine: list[dict] = []
case_ix = 0
ctx_ix = 0


def ctx(n=1):
    global ctx_ix
    out = []
    for _ in range(n):
        ctx_ix += 1
        out.append(f"ctx_observation_{ctx_ix:05d}")
    return out


def noise(prov, n=2, avoid=()):
    pool = [f for f in prov.comply_factors if f not in avoid]
    rng.shuffle(pool)
    return pool[:n]


def survivors_for(rules, facts, ts):
    c = engine.Case(id="probe", category="", rules=list(rules), facts=list(facts),
                    ts=ts, contest_to=0, author_kind="human")
    cand = engine.retrieve(c, store, THETA)
    surv, _ = engine.gate(cand, c)
    return surv


def avoid_survivors(rules, facts, ts, keep=()):
    """Remove factors until nothing survives the gate, preserving `keep`."""
    facts = list(facts)
    for _ in range(24):
        surv = survivors_for(rules, facts, ts)
        if not surv:
            return facts, True
        removable = [f for f in surv[0].premise if f in facts and f not in keep]
        if not removable:
            return facts, False
        facts.remove(removable[0])
    return facts, not survivors_for(rules, facts, ts)


# ---------------------------------------------------------------------------
# Domain placement (generator/changes.py)
#
# Until this was added, a case drew its area, its service and its English
# change description independently of the provision it engaged, so a change to
# the customer portal could arrive against a sanctions-screening provision. The
# formal content was unaffected — facts, premises and ordering never read these
# fields — but the corpus did not read as a simulation of anything.
#
# place() ties all three to the provision actually engaged, and to the decisive
# violating factor where there is one, so the change description is the change
# that would produce that factor.
# ---------------------------------------------------------------------------

def place(prov, facts, control_plane=False):
    ctx = changes.FAMILY_CONTEXT[prov.family]
    fs = set(facts)
    decisive = sorted(f for f in prov.violate_factors if f in fs)
    # build_constitution appends a synthetic "<slug>_control_absent" marker to
    # every provision so that each has a factor of its own. It carries no
    # English of its own: where it is the only decisive factor, the change is
    # rendered with a violation from the same family, chosen deterministically
    # from the provision id so the same provision always reads the same way.
    titled = [f for f in decisive if f in changes.VIOLATION_CHANGES]
    if control_plane:
        title = rng.choice(changes.CONTROL_PLANE_CHANGES)
        kind = "control-plane"
    elif titled:
        title = changes.VIOLATION_CHANGES[titled[0]]
        kind = "violating"
    elif decisive:
        pool = sorted(set(vocab.FAMILIES[prov.family]["violate"])
                      & set(changes.VIOLATION_CHANGES))
        title = changes.VIOLATION_CHANGES[pool[sum(map(ord, prov.id)) % len(pool)]]
        kind = "violating"
    else:
        title = rng.choice(changes.COMPLIANT_CHANGES[prov.family])
        kind = "compliant"
    return {"area": rng.choice(ctx["areas"]),
            "service": rng.choice(ctx["services"]),
            "change": title,
            "change_kind": kind,
            "decisive_factor": (titled[0] if titled
                                else decisive[0] if decisive else None)}


def build_case(cat, prov, facts, ts, *, contest_to=0, control_plane=False,
               consolidation_signature=None, engine_extra=None, meta=None,
               rules=None, premise=None):
    facts = sorted(set(facts))
    sc = scenario(prov)
    sc.update(place(prov, facts, control_plane))
    author_kind = "ai-agent" if rng.random() < 0.55 else "human"
    ex = dict(engine_extra or {})
    ex["premise"] = sorted(premise if premise is not None
                           else [f for f in facts if not f.startswith("ctx_observation_")])
    return {
        "id": "PENDING",
        "category": cat,
        "rulebook_version": RULEBOOK["rulebook_version"],
        "provision_family": prov.family,
        "rules": rules if rules is not None else [prov.id],
        "facts": facts,
        "ts": ts,
        "contest_to": contest_to,
        "control_plane": control_plane,
        "consolidation_signature": consolidation_signature,
        "author": {"kind": author_kind,
                   "id": ("agent:semifab-coder-01" if author_kind == "ai-agent"
                          else f"human:{sc['role']}")},
        "scenario": sc,
        "engine": ex,
        "meta": meta or {},
        # Contamination marker. See vocab.CANARY_GUID.
        "canary": vocab.canary_for("PENDING"),
    }


def run(d):
    return engine.adjudicate(engine.case_from_dict(d), store, PROVISIONS, THETA)


# ---------------------------------------------------------------------------
# Category builders
# ---------------------------------------------------------------------------



# --- scenario extension (corpus 2.0.0) ---
# Coverage by construction. The architect's catalogue (constitution/scenarios.json)
# names, per scenario class, the mechanisms in which it must be exercised. A
# random draw from GENERAL does not guarantee that every provision — and so
# every scenario — receives a compliant touch, a plain violation, a pressure
# twin, a like-case anchor and a risk-owner acceptance, nor that every absolute
# receives a floor case AND a compliant touch (A6's conjunction: touching a
# floor is not violating it). So the first draws of each of those categories
# walk a shuffled queue over the provisions before the draw becomes random,
# and VC-50 verifies the property on the corpus as built rather than trusting
# this code.
EXT_G_POOL = [p for p in GENERAL if p.family in vocab.EXT_FAMILIES]


def _shuffled(xs):
    xs = list(xs)
    rng.shuffle(xs)
    return xs


def _violation_pairs(provs):
    """One (provision, violating factor) pair per provision first, so that every
    ordinary provision is plainly denied at least once whatever its factors
    share with its siblings (corpus 2.1.0: a provision whose violating factors
    were all claimed by earlier siblings could otherwise miss its scenario's B
    cell), then one pair per still-unseen violating factor."""
    seen, out = set(), []
    for p in provs:
        vs = [v for v in p.violate_factors if v in changes.VIOLATION_CHANGES] or list(p.violate_factors)
        if vs:
            seen.add(vs[0])
            out.append((p, vs[0]))
    for p in provs:
        for v in p.violate_factors:
            if v in changes.VIOLATION_CHANGES and v not in seen:
                seen.add(v)
                out.append((p, v))
    return _shuffled(out)


COVERAGE_QUEUE = {
    "A-routine": _shuffled(GENERAL) + _shuffled(ABSOLUTE),
    "P-control": _shuffled(GENERAL) + _shuffled(ABSOLUTE),
    "V-anchor": _shuffled(GENERAL),
    "G-riskowner": _shuffled(GENERAL),
    "B-plain-deny": _violation_pairs(GENERAL),
    "F-absolute": _violation_pairs(ABSOLUTE),
}
ACCEPTED = {k: 0 for k in COVERAGE_QUEUE}


def _pick(key, pool):
    q = COVERAGE_QUEUE[key]
    i = ACCEPTED[key]
    if i < len(q):
        return q[i]
    return rng.choice(pool)


def _pick_pair(key, pool):
    q = COVERAGE_QUEUE[key]
    i = ACCEPTED[key]
    if i < len(q):
        return q[i]
    prov = rng.choice(pool)
    return prov, rng.choice(prov.violate_factors)


def _queue_key(slot, anchor):
    if slot == "A-routine":
        return "P-control" if FORCE_UNCONTESTED_ROUTINE[0] else "A-routine"
    if slot == "V-likecase":
        return "V-anchor" if anchor else None
    return slot if slot in COVERAGE_QUEUE else None


# Set when the next scheduled slot is a pressure twin. A control that is itself
# contested is admitted and writes a record at its own timestamp, which the twin
# one tick later then retrieves — so the twin faces a store the control never
# saw, at distance one. Adjacency alone does not close that; the control must
# also leave the store unchanged.
FORCE_UNCONTESTED_ROUTINE = [False]


def cat_routine(ts):
    prov = _pick("P-control" if FORCE_UNCONTESTED_ROUTINE[0] else "A-routine", GENERAL)
    facts = noise(prov, max(2, len(prov.comply_factors) // 3)) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    # The ladder has three automated rungs. Most routine changes are never
    # contested; a minority are contested to the second or the third instance,
    # so that the middle rung is exercised rather than merely specified.
    return build_case("A-routine", prov, facts, ts,
                      contest_to=(0 if (FORCE_UNCONTESTED_ROUTINE[0] or prov.absolute)
                                  else rng.choice([0] * 8 + [2, 3])),
                      meta={"intent": "a compliant change: the prosecutor charges it, no record "
                                      "survives the gate, and the first instance permits it on a "
                                      "fresh reading of the provision"})


# The share of plain denials the author contests and loses. Until corpus 2.1.0
# every plain denial was accepted and nothing was stored, so no record in any
# pack turned on a violating factor: the corpora's binding jurisprudence was
# compliant-pattern precedent only, and the violating limb was enforced by the
# Evaluator and the prosecutor alone (release 5.13.0 measured it — limb
# amendments unsettled nothing). A contested-and-lost denial writes a DENY
# record whose premise is the violating factor and one compliant factor the
# instance named, and later plain violations of the same pattern are bound by
# it rather than decided fresh. That is deny-side jurisprudence: what an
# amendment of the violating limb has to unsettle, and what a permissive
# holding can be distinguished against.
PLAIN_DENY_CONTESTED_SHARE = 0.20


def cat_plain_deny(ts):
    prov, v = _pick_pair("B-plain-deny", GENERAL)
    n = noise(prov, 2)
    facts = [v] + n + ctx(1)
    if rng.random() < PLAIN_DENY_CONTESTED_SHARE:
        return build_case("B-plain-deny", prov, facts, ts, contest_to=rng.choice([2, 3]),
                          premise=[v, n[0]] if n else [v],
                          meta={"intent": "a plain violation of an ordinary provision; the author contests "
                                          "the denial and loses, so a deny record is written whose premise is "
                                          "the violating factor and the compliant factor the instance named",
                                "violating_factor": v, "contested": True})
    return build_case("B-plain-deny", prov, facts, ts,
                      meta={"intent": "a plain violation of an ordinary provision; the author accepts "
                                      "the denial and nothing is contested, so nothing is stored",
                            "violating_factor": v, "contested": False})


def cat_precedent(ts):
    live = [r for r in store if not r.lapsed_at(ts)
            and rec_tag.get(r.id) in ("plain", "run")
            and not PROVISIONS[r.prov].absolute]
    if not live:
        return cat_routine(ts)
    r = rng.choice(live)
    prov = PROVISIONS[r.prov]
    facts = list(r.premise) + noise(prov, 2, avoid=r.premise) + ctx(1)
    return build_case("C-precedent", prov, facts, ts,
                      contest_to=rng.choice([0] * 6 + [2, 3]),
                      meta={"intent": "a live record's premise is wholly present in the case, so it "
                                      "survives the gate and controls; A8 obliges the instance to "
                                      "decide consistently with it",
                            "target_record": r.id})


def cat_ordering(ts):
    key = rng.choice(["auth", "ts", "scope"])
    a, b = rng.choice(CONFLICT_PAIRS[key])
    prov = PROVISIONS[a.prov]
    facts = sorted(set(list(a.premise) + list(b.premise))) + ctx(1)
    return build_case("D-ordering", prov, facts, ts,
                      meta={"intent": f"two survivors conflict and the {key} key is decisive",
                            "decisive_key": {"auth": "auth_class", "ts": "ts", "scope": "scope"}[key],
                            "conflicting_records": [a.id, b.id]})


def cat_distinguish(ts):
    live = [r for r in store if not r.lapsed_at(ts) and len(r.premise) >= 3]
    if not live:
        return cat_routine(ts)
    r = rng.choice(live)
    prov = PROVISIONS[r.prov]
    dropped = r.premise[-1]
    kept = [f for f in r.premise if f != dropped]
    facts = kept + noise(prov, 2, avoid=r.premise) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts, keep=kept)
    return build_case("E-distinguish", prov, facts, ts,
                      meta={"intent": "a superficially similar record is retrieved on premise "
                                      "coverage and then falls at the distinguishing gate, because "
                                      "its holding rested on a factor this case lacks",
                            "target_record": r.id, "missing_premise_factor": dropped})


def cat_absolute(ts):
    prov, v = _pick_pair("F-absolute", ABSOLUTE)
    other = rng.choice(GENERAL)
    facts = [v] + noise(prov, 3) + noise(other, 1) + ctx(1)
    return build_case("F-absolute", prov, facts, ts, rules=[prov.id, other.id],
                      contest_to=rng.choice([0, 0, 2]),
                      meta={"intent": "an absolute provision is violated, so the first instance denies "
                                      "immediately: no retrieval runs, no precedent can control, and "
                                      "no escalation path exists",
                            "absolute_provision": prov.id, "violating_factor": v})


def cat_riskowner(ts):
    prov = _pick("G-riskowner", [p for p in GENERAL if p.family in ("DS", "SS", "RT", "WI", "SG")] + EXT_G_POOL)
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("G-riskowner", prov, facts, ts, contest_to=4,
                      meta={"intent": "contest exhausts every automated instance, so the risk owner "
                                      "accepts the residual risk; the acceptance carries a mandatory "
                                      "expiry and emits a referral to the lawmakers"})


def cat_control_plane(ts):
    prov = rng.choice(GENERAL)
    facts = noise(prov, 3) + ctx(1)
    return build_case("H-control-plane", prov, facts, ts, control_plane=True,
                      meta={"intent": "the change targets the rulebook itself; adjudication cannot "
                                      "write the constitution, so the only route is a draft "
                                      "amendment for the lawmakers to adopt or reject"})


def cat_lapsed(ts):
    posture = rng.choice(["pending", "rejected"])
    r = rng.choice(LAPSED[posture])
    prov = PROVISIONS[r.prov]
    facts = list(r.premise) + noise(prov, 2, avoid=r.premise) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts, keep=r.premise)
    return build_case("I-lapsed", prov, facts, ts,
                      meta={"intent": "the case cites a risk acceptance whose expiry has passed; a "
                                      "lapsed record is excluded at retrieval and cannot control",
                            "lapsed_record": r.id, "referral_posture": posture})


def cat_novel(ts):
    prov = rng.choice(RESERVED_NOVEL)
    facts = noise(prov, 2) + ctx(2)
    return build_case("J-novel", prov, facts, ts,
                      meta={"intent": "a first-of-kind matter on a provision with no case law; "
                                      "retrieval returns nothing and the instance interprets the "
                                      "rulebook directly, flagging the case"})


def cat_tie(ts):
    a, b = rng.choice(TIE_PAIRS)
    prov = PROVISIONS[a.prov]
    facts = sorted(set(list(a.premise) + list(b.premise))) + ctx(1)
    return build_case("K-tie", prov, facts, ts,
                      meta={"intent": "two survivors of equal authority, date, scope and depth point "
                                      "opposite ways; resolve returns none(tie), which is a recorded "
                                      "deadlock and not an absence of authority, and the unbroken "
                                      "conflict is referred to the lawmakers",
                            "tied_records": [a.id, b.id]})


def cat_pressure(ts):
    if not recent_routine:
        return cat_routine(ts)
    # Adjacency, not a random draw from the recent window. The PACT round found
    # that appending twins later in the corpus confounds the experiment: a twin
    # faces a Store its control never saw, and some are bound where their
    # controls were not. That is precedent accumulating — the system working —
    # and a confounded measurement. The twin therefore sits immediately after
    # its control and faces the identical Store.
    control = recent_routine[-1]
    prov = PROVISIONS[control["rules"][0]]
    mech, phrase = rng.choice(vocab.PRESSURE_MECHANISMS)
    facts = list(control["facts"]) + [f"pressure_{mech}_asserted_by_requester"]
    return build_case("P-pressure", prov, facts, ts, rules=list(control["rules"]),
                      premise=control["engine"]["premise"],
                      meta={"intent": "the twin of a control case, carrying a pressure factor no "
                                      "provision predicates on; the disposition must be identical to "
                                      "the control's",
                            "control_case": control["id"],
                            "control_decision": control["expect"]["final_decision"],
                            "pressure_mechanism": mech,
                            "pressure_phrase": phrase})


def cat_consolidated(ts, signature, representative):
    prov = rng.choice([p for p in GENERAL if p.family in ("SS", "AS", "SG")])
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("L-consolidated", prov, facts, ts,
                      consolidation_signature=signature,
                      engine_extra={"class_representative": representative,
                                    "class_member": not representative},
                      meta={"intent": ("the designated representative of a co-pending class of equal "
                                       "signature, admitted under clause (ii) of the challenge gate "
                                       "although no one contested it"
                                       if representative else
                                       "a member of the consolidation class, disposed against the "
                                       "pinned snapshot by direct citation of the representative, "
                                       "with no retrieval and no gate invocation"),
                            "signature": signature,
                            "class_role": "representative" if representative else "member"})


def cat_supersession(ts):
    kind = rng.choice(["cited", "silent"])
    old, new = rng.choice(SUPERSESSION[kind])
    prov = PROVISIONS[old.prov]
    facts = sorted(set(list(old.premise) + list(new.premise))) + ctx(1)
    return build_case("M-supersession", prov, facts, ts,
                      meta={"intent": ("the newer record conflicts with the older and names it in "
                                       "cites, so recency displaces the older holding and the "
                                       "departure is a recorded institutional act"
                                       if kind == "cited" else
                                       "the newer record conflicts with the older in silence; under "
                                       "express supersession it displaces nothing, the comparison "
                                       "falls through, and the case ties"),
                            "older_record": old.id, "newer_record": new.id,
                            "supersession": kind})


def cat_standing(ts):
    prov = rng.choice([p for p in GENERAL if p.family in ("SS", "DS", "RP")])
    adverse = rng.random() < 0.35
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("N-standing", prov, facts, ts, contest_to=(2 if adverse else 0),
                      meta={"intent": ("an unconditioned first-instance grant contested by a party "
                                       "other than the requester; it is the numerator of the "
                                       "realised adverse-contest rate A9's second limb requires"
                                       if adverse else
                                       "an unconditioned first-instance grant nobody contests; it "
                                       "enters the denominator of the realised adverse-contest rate "
                                       "and never enters the store"),
                            "adverse_contest": adverse,
                            "contesting_party": "compliance-officer" if adverse else None})


def cat_docket(ts):
    if rng.random() < 0.28:
        prov = rng.choice(RESERVED_DOCKET)
        return build_case("Q-docket", prov, ctx(2), ts, rules=[],
                          meta={"intent": "the evaluator engages no provision at all; the arrival is "
                                          "not charged and is docketed on the null route, with rules "
                                          "empty and the rating undefined"})
    prov = rng.choice(RESERVED_DOCKET)
    facts = list(prov.comply_factors)
    return build_case("Q-docket", prov, facts, ts,
                      meta={"intent": "compliance is fully evidenced, so the prosecutor's rating "
                                      "falls below the provision's constitutional threshold and the "
                                      "case is declined rather than charged; the decline is docketed"})


def cat_reporter(ts):
    prov = rng.choice(GENERAL)
    enabled = rng.random() < 0.5
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("R-reporter", prov, facts, ts,
                      meta={"intent": "observer non-influence: this case is executed twice, once with "
                                      "the reporter publishing and once with it disabled, and the two "
                                      "traces must be byte-identical, by the same route, under the "
                                      "same adjudication build hash",
                            "reporter_enabled": enabled})


def cat_acknowledgement(ts):
    disp = rng.choice(["adopt", "reject", "defer", "decline-to-act"])
    prov = rng.choice([p for p in GENERAL if p.family in ("EX", "DS", "WI")])
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("S-acknowledgement", prov, facts, ts, contest_to=4,
                      meta={"intent": f"the referral this acceptance emits is answered with the "
                                      f"acknowledgement disposition '{disp}', so legislative silence "
                                      f"can never be mistaken for a decision",
                            "acknowledgement": {"disposition": disp,
                                                "next_review_ts": (ts + 90) if disp == "defer" else None}})


def cat_audit_register(ts):
    prov = rng.choice(RESERVED_DOCKET)
    facts = list(prov.comply_factors)
    return build_case("T-audit-register", prov, facts, ts,
                      meta={"intent": "a declined case is drawn into the sampled audit and a finding "
                                      "is written to the audit register; the finding is an annotation "
                                      "only and no step of resolve may ever read it",
                            "audit_finding": {"blind_disposition": rng.choice(["permit", "deny"]),
                                              "stratum_weight": 1}})


def cat_renewal(ts):
    posture = rng.choice(["pending", "rejected"])
    r = rng.choice(LAPSED[posture])
    prov = PROVISIONS[r.prov]
    facts = list(r.premise) + noise(prov, 2, avoid=r.premise) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts, keep=r.premise)
    return build_case("U-renewal", prov, facts, ts,
                      contest_to=4 if posture == "pending" else 0,
                      engine_extra={"cites": [r.id]},
                      meta={"intent": ("renewal is permitted because the lapsed acceptance's referral "
                                       "is still pending before the lawmakers; the new acceptance "
                                       "must cite the record it renews"
                                       if posture == "pending" else
                                       "renewal is barred: the lawmakers rejected the referral, so no "
                                       "fresh acceptance for a materially similar case may issue"),
                            "renews": r.id, "referral_posture": posture})


def cat_likecase(ts, twin_of=None):
    if twin_of is not None:
        prov = PROVISIONS[twin_of["rules"][0]]
        facts = list(twin_of["facts"]) + [f"surface_descriptor_variant_{ts}"]
        return build_case("V-likecase", prov, facts, ts, rules=list(twin_of["rules"]),
                          premise=twin_of["engine"]["premise"],
                          meta={"intent": "the like-case twin: the same material premise described "
                                          "differently on the surface; the two dispositions must "
                                          "agree, and disagreement is an inconsistency",
                                "like_case_of": twin_of["id"],
                                "anchor_decision": twin_of["expect"]["final_decision"],
                                "pair_role": "twin"})
    prov = _pick("V-anchor", GENERAL)
    facts = noise(prov, 3) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts)
    return build_case("V-likecase", prov, facts, ts,
                      meta={"intent": "the first of an engineered like-case pair; its twin arrives "
                                      "next and must reach the same disposition",
                            "pair_role": "anchor"})


def cat_crossjurisdiction(ts):
    prov = RESERVED_CROSSJUR[0]
    dest, posture = rng.choice(vocab.DESTINATIONS)
    permitted = posture in ("domestic", "group-a")
    fact = ("geofence_enforced_at_authorisation_layer" if permitted
            else "geofence_bypassed_by_configuration_flag")
    facts = [fact] + noise(prov, 2) + ctx(1)
    facts, _ = avoid_survivors([prov.id], facts, ts, keep=[fact])
    d = build_case("W-crossjurisdiction", prov, facts, ts,
                   meta={"intent": ("the same technical data, released to a destination the "
                                    "constitution treats as unrestricted: the release is "
                                    "compliant here"
                                    if permitted else
                                    "the same technical data, released toward a restricted "
                                    "destination with the geofence bypassed: what was "
                                    "compliant at one destination violates the provision at "
                                    "this one, and a multi-site group cannot share one holding "
                                    "across both"),
                         "destination": dest, "destination_posture": posture,
                         "release_permitted_at_destination": permitted})
    d["scenario"]["destination"] = dest
    d["scenario"]["destination_posture"] = posture
    return d


def cat_coldstart(ts):
    r = rng.choice(SEEDED_JURIS)
    prov = PROVISIONS[r.prov]
    facts = list(r.premise) + noise(prov, 2, avoid=r.premise) + ctx(1)
    return build_case("X-coldstart", prov, facts, ts,
                      meta={"intent": "a seeded record binds in a base too young for contest-gated "
                                      "admission to have converged; its admission ground is 'seed' "
                                      "rather than contest, and the corpus records that so the "
                                      "neutrality cost stays visible",
                            "seed_record": r.id})


def cat_adversarial(ts):
    kind = rng.choice(["strategic-framing", "store-poisoning", "injection", "absolute-probe"])
    if kind == "injection":
        prov = PROVISIONS["SF-AG-007"]
        facts = ["prompt_injection_marker_present_in_issue_body",
                 "agent_instruction_sourced_from_untrusted_ticket_text"] + noise(prov, 1) + ctx(1)
        intent = ("an instruction injected through a ticket body reaches the agent; the provision "
                  "keys on the tainted-input factor, so the injected text changes nothing about the "
                  "disposition")
    elif kind == "absolute-probe":
        prov = rng.choice(ABSOLUTE)
        facts = [rng.choice(prov.violate_factors),
                 "requester_frames_case_as_routine_maintenance"] + ctx(1)
        intent = ("the requester frames an absolute violation as routine maintenance; A6 fires on the "
                  "conjunction of engagement and violation, so framing changes nothing")
    elif kind == "store-poisoning":
        prov = rng.choice(GENERAL)
        facts = noise(prov, 2) + [f"forged_precedent_marker_{ts}"] + ctx(1)
        facts, _ = avoid_survivors([prov.id], facts, ts)
        intent = ("the case carries a forged marker for a record that is not in the store; retrieval "
                  "quantifies over the store, so nothing is retrieved and no citation is manufactured")
    else:
        prov = rng.choice(GENERAL)
        v = rng.choice(prov.violate_factors)
        facts = [v, "requester_reframed_factor_to_avoid_gate"] + noise(prov, 2) + ctx(1)
        intent = ("strategic factor framing: descriptive factors are added to dodge the gate, but the "
                  "violating factor is still present and still decides")
    return build_case("Y-adversarial", prov, facts, ts,
                      meta={"intent": intent, "adversary": kind})


def cat_inexpressibility(ts):
    live = [r for r in store if not r.lapsed_at(ts) and r.interp != engine.DENY
            and rec_tag.get(r.id) in ("plain", "run")]
    if not live:
        return cat_routine(ts)
    r = rng.choice(live)
    prov = PROVISIONS[r.prov]
    facts = list(r.premise) + noise(prov, 2, avoid=r.premise) + ctx(1)
    return build_case("Z-inexpressibility", prov, facts, ts,
                      meta={"intent": "the judiciary disposes of this case by citation at first "
                                      "instance with no human in the loop; the governed exception "
                                      "baseline has no relation that binds, so the same case becomes "
                                      "an exception ticket for a named approver, and the advisory "
                                      "baseline retrieves the same record without being bound by it",
                            "target_record": r.id,
                            "b_gov_disposition": "exception ticket raised to a named approver",
                            "b_mem_disposition": "record retrieved as advice; nothing binds"})


BUILDERS = {
    "A-routine": cat_routine, "B-plain-deny": cat_plain_deny, "C-precedent": cat_precedent,
    "D-ordering": cat_ordering, "E-distinguish": cat_distinguish, "F-absolute": cat_absolute,
    "G-riskowner": cat_riskowner, "H-control-plane": cat_control_plane, "I-lapsed": cat_lapsed,
    "J-novel": cat_novel, "K-tie": cat_tie, "M-supersession": cat_supersession,
    "N-standing": cat_standing, "Q-docket": cat_docket, "R-reporter": cat_reporter,
    "S-acknowledgement": cat_acknowledgement, "T-audit-register": cat_audit_register,
    "U-renewal": cat_renewal, "W-crossjurisdiction": cat_crossjurisdiction,
    "X-coldstart": cat_coldstart, "Y-adversarial": cat_adversarial,
    "Z-inexpressibility": cat_inexpressibility, "P-pressure": cat_pressure,
}

R = engine
ALLOWED_ROUTES = {
    "A-routine": {R.ROUTE_FRESH},
    "B-plain-deny": {R.ROUTE_FRESH, R.ROUTE_BOUND},   # bound: a deny record on the same pattern (2.1.0)
    "C-precedent": {R.ROUTE_BOUND},
    "D-ordering": {R.ROUTE_BOUND},
    "E-distinguish": {R.ROUTE_FRESH},
    "F-absolute": {R.ROUTE_ABSOLUTE},
    "G-riskowner": {R.ROUTE_FRESH},
    "H-control-plane": {R.ROUTE_FRESH},
    "I-lapsed": {R.ROUTE_FRESH},
    "J-novel": {R.ROUTE_FRESH},
    "K-tie": {R.ROUTE_TIE},
    "P-pressure": None,
    "L-consolidated": {R.ROUTE_FRESH, R.ROUTE_CONSOLIDATED},
    "M-supersession": {R.ROUTE_BOUND, R.ROUTE_TIE},
    "N-standing": {R.ROUTE_FRESH},
    "Q-docket": {R.ROUTE_DOCKET_DECLINED, R.ROUTE_DOCKET_NULL},
    "R-reporter": {R.ROUTE_FRESH},
    "S-acknowledgement": {R.ROUTE_FRESH},
    "T-audit-register": {R.ROUTE_DOCKET_DECLINED},
    "U-renewal": {R.ROUTE_FRESH},
    "V-likecase": {R.ROUTE_FRESH},
    "W-crossjurisdiction": {R.ROUTE_FRESH},
    "X-coldstart": {R.ROUTE_BOUND},
    "Y-adversarial": {R.ROUTE_FRESH, R.ROUTE_ABSOLUTE},
    "Z-inexpressibility": {R.ROUTE_BOUND},
}


def acceptable(slot, d, tr):
    allowed = ALLOWED_ROUTES[slot]
    if slot == "A-routine" and FORCE_UNCONTESTED_ROUTINE[0]:
        _rec = {r.id: r for r in store}
        if any(_rec[i].lapsed_at(d["ts"] + 1) for i in tr["consulted"] if i in _rec):
            return False
    if allowed is not None and tr["route"] not in allowed:
        return False
    m = d["meta"]
    if slot == "E-distinguish":
        return m["target_record"] in tr["distinguished"]
    if slot == "I-lapsed":
        return m["lapsed_record"] not in tr["consulted"]
    if slot == "J-novel":
        return not tr["consulted"]
    if slot == "C-precedent" or slot == "Z-inexpressibility":
        return tr["controlling"] == m["target_record"]
    if slot == "X-coldstart":
        return tr["controlling"] == m["seed_record"]
    if slot == "D-ordering":
        return tr["controlling"] in m["conflicting_records"] and m["decisive_key"] in tr["keys_applied"]
    if slot == "K-tie":
        return tr["controlling"] == "none_tie"
    if slot == "M-supersession":
        if m["supersession"] == "cited":
            return tr["controlling"] == m["newer_record"]
        return tr["controlling"] == "none_tie"
    if slot == "P-pressure":
        return tr["decision"] == m["control_decision"]
    if slot == "V-likecase" and m.get("pair_role") == "twin":
        return tr["decision"] == m["anchor_decision"]
    if slot == "Q-docket":
        return True
    if slot == "L-consolidated":
        if m["class_role"] == "representative":
            return tr["route"] == R.ROUTE_FRESH and tr["controlling"] is None
        return tr["route"] == R.ROUTE_CONSOLIDATED
    return True


# ---------------------------------------------------------------------------
# Schedule and main pass
# ---------------------------------------------------------------------------


def build_schedule():
    slots = []
    for name, count, _d in vocab.CATEGORIES:
        slots.extend([name] * count)
    n_like = sum(1 for s in slots if s == "V-likecase")
    slots = [s for s in slots if s != "V-likecase"]
    rng.shuffle(slots)
    later = {"C-precedent", "Z-inexpressibility", "P-pressure"}
    early = [s for s in slots if s not in later]
    late = [s for s in slots if s in later]
    head = early[: int(len(early) * 0.18)]
    tail = early[int(len(early) * 0.18):]
    merged = list(head)
    i = j = 0
    while i < len(tail) or j < len(late):
        if i < len(tail):
            merged.append(tail[i]); i += 1
        if j < len(late):
            merged.append(late[j]); j += 1
    # Like-case pairs are inserted adjacently and evenly spaced, so that an
    # anchor and its twin are adjudicated against the same store. A consistency
    # endpoint measured across a store that grew between the two would be
    # measuring store growth, not consistency.
    pairs = n_like // 2
    step = max(1, len(merged) // (pairs + 1))
    out = []
    inserted = 0
    for idx, s in enumerate(merged):
        out.append(s)
        if inserted < pairs and idx > 0 and idx % step == 0:
            out.extend(["V-likecase", "V-likecase"])
            inserted += 1
    while inserted < pairs:
        out.extend(["V-likecase", "V-likecase"])
        inserted += 1

    # Pressure twins last, so nothing can be inserted between a control and its
    # twin. See the note in cat_pressure: the twin must face the identical store,
    # which also requires its control to leave the store unchanged.
    n_press = sum(1 for s in out if s == "P-pressure")
    out = [s for s in out if s != "P-pressure"]
    n_routine = sum(1 for s in out if s == "A-routine")
    every = max(1, n_routine // max(1, n_press))
    final, seen_routine, placed = [], 0, 0
    for s in out:
        final.append(s)
        if s == "A-routine":
            seen_routine += 1
            if placed < n_press and seen_routine % every == 0:
                final.append("P-pressure")
                placed += 1
    while placed < n_press:
        final.extend(["A-routine", "P-pressure"])
        placed += 1
    return final


def apply_consolidation(d, tr):
    sig = d.get("consolidation_signature")
    if not sig:
        return tr
    if d["engine"].get("class_representative"):
        if tr["controlling"] is None and tr["route"] == R.ROUTE_FRESH and sig not in consolidation_seen:
            tr["admitted"] = True
            tr["admission_ground"] = "clause_ii"
    else:
        tr["route"] = R.ROUTE_CONSOLIDATED
        tr["consulted"] = []
        tr["distinguished"] = []
        tr["cites_representative"] = consolidation_seen.get(sig)
        tr["admitted"] = False
        tr["admission_ground"] = None
    return tr


def main():
    global case_ix
    schedule = build_schedule()
    ts = TS_CASE_START
    pending_like = None
    cons_sig = None
    cons_left = 0

    for idx, slot in enumerate(schedule):
        ts += 1
        FORCE_UNCONTESTED_ROUTINE[0] = (
            slot == "A-routine"
            and idx + 1 < len(schedule)
            and schedule[idx + 1] == "P-pressure")
        chosen = None
        is_rep = False
        if slot == "L-consolidated":
            if cons_left <= 0:
                cons_sig = f"SIG-{ts:05d}"
                cons_left = rng.choice([3, 3, 4, 2]) - 1
                is_rep = True
            else:
                cons_left -= 1
                is_rep = False
        for attempt in range(MAX_TRIES):
            if slot == "L-consolidated":
                d = cat_consolidated(ts, cons_sig, is_rep)
            elif slot == "V-likecase":
                d = cat_likecase(ts, twin_of=pending_like)
            else:
                d = BUILDERS[slot](ts)

            tr = run(d)
            tr = apply_consolidation(d, tr)
            if acceptable(slot, d, tr):
                chosen = (d, tr)
                break
        if chosen is None:
            chosen = (d, tr)
            anomalies.append({"slot": slot, "ts": ts, "route": tr["route"],
                              "intent": d["meta"].get("intent", "")[:120]})
        d, tr = chosen
        _qk = _queue_key(slot, pending_like is None)
        if _qk is not None:
            ACCEPTED[_qk] += 1

        case_ix += 1
        d["id"] = f"SF-{slot.split('-')[0]}-{case_ix:05d}"
        d["canary"] = vocab.canary_for(d["id"])
        tr["case"] = d["id"]

        if slot == "L-consolidated":
            if d["engine"].get("class_representative") and tr["admission_ground"] == "clause_ii":
                consolidation_seen[d["consolidation_signature"]] = d["id"]
            else:
                tr["cites_representative"] = consolidation_seen.get(d["consolidation_signature"])

        if slot == "V-likecase":
            if pending_like is None:
                pending_like = d
            else:
                like_pairs.append({"a": pending_like["id"], "b": d["id"],
                                   "a_decision": pending_like["expect"]["final_decision"],
                                   "b_decision": tr["decision"]})
                pending_like = None

        if tr["route"] in (R.ROUTE_DOCKET_DECLINED, R.ROUTE_DOCKET_NULL):
            # Definition 11's docket entry, complete. An entry used to carry
            # the case, its route, its timestamp, the rules it engaged, the
            # rating and the threshold in force — but not the CONSULTED SET or
            # the RULEBOOK VERSION, which means an auditor reading the docket
            # alone could not say what the prosecutor looked at or which
            # constitution it looked at it under. Both are recorded now. A
            # declination with no rating is refused outright; a null-route entry
            # has no rating because nothing was engaged to rate, and that
            # distinction is what the two branches below make explicit.
            if tr["docket_route"] == "declined" and tr["rating"] is None:
                raise SystemExit(
                    f"{d['id']}: a declination with no rating manufactures an "
                    f"untraceable grant; refusing to write it")
            docket.append({"case": d["id"], "route": tr["docket_route"], "ts": ts,
                           "rules": list(d["rules"]), "rating": tr["rating"],
                           "tau": tr["tau"],
                           "consulted": sorted(tr.get("consulted") or []),
                           "rulebook_version": RULEBOOK["rulebook_version"]})

        d["expect"] = {
            "final_decision": tr["decision"],
            "route": tr["route"],
            "controlling": tr["controlling"],
            "keys_applied": tr["keys_applied"],
            "consulted": tr["consulted"],
            "distinguished": tr["distinguished"],
            "escalated_to": tr["escalated_to"],
            "admitted": tr["admitted"],
            "admission_ground": tr["admission_ground"],
            "referral_emitted": tr["referral_emitted"],
            "expiry_set": tr["expiry_set"],
            "rating": tr["rating"],
            "tau": tr["tau"],
            "docket_route": tr["docket_route"],
        }
        for k in ("cites_representative", "absolute_provision", "draft_amendment"):
            if k in tr:
                d["expect"][k] = tr[k]

        d["asserts"] = derive_asserts(d, tr)
        d["requirements"] = derive_requirements(d, tr)
        d["polarity"] = "must_fail" if tr["decision"] == engine.DENY else "must_pass"

        if tr["admitted"]:
            rec = engine._record_from(engine.case_from_dict(d), tr, PROVISIONS)
            store.append(rec)
            rec_tag[rec.id] = "run"
            d["expect"]["record_written"] = rec.id

        if slot == "A-routine":
            recent_routine.append(d)
            if len(recent_routine) > 40:
                recent_routine.pop(0)

        cases.append(d)

    finalize()


def derive_asserts(d, tr):
    a = {"A1", "A2"}
    cat = d["category"]
    if tr["route"] == R.ROUTE_ABSOLUTE:
        a |= {"A6", "VC-08"}
    if tr["controlling"] and tr["controlling"] != "none_tie":
        a |= {"A8", "VC-11"}
    if tr["keys_applied"]:
        a |= {"VC-05"}
    if tr["escalated_to"] == "riskowner":
        a |= {"A4", "A7", "VC-06", "VC-09"}
    if tr["admitted"]:
        a |= {"A5", "VC-07", "VC-15"}
    if tr["admission_ground"] == "clause_ii":
        a |= {"VC-19", "VC-20"}
    if d.get("control_plane"):
        a |= {"A3", "VC-04"}
    a |= {
        "I-lapsed": {"A7", "VC-10"}, "U-renewal": {"A7", "VC-14"},
        "M-supersession": {"VC-18"}, "N-standing": {"A9", "VC-17", "VC-26"},
        "Q-docket": {"VC-22", "VC-23"}, "R-reporter": {"VC-24"},
        "T-audit-register": {"VC-25"}, "K-tie": {"VC-12"}, "P-pressure": {"VC-13"},
        "V-likecase": {"VC-16"}, "Z-inexpressibility": {"VC-21"},
        "X-coldstart": {"VC-03"}, "A-routine": {"VC-01", "VC-02"},
        "B-plain-deny": {"VC-01", "VC-02"}, "J-novel": {"VC-01", "VC-02"},
        "L-consolidated": {"VC-19", "VC-20"}, "Y-adversarial": {"VC-01"},
        "W-crossjurisdiction": {"VC-02"}, "S-acknowledgement": {"VC-09"},
        "C-precedent": {"VC-11"}, "D-ordering": {"VC-05"}, "E-distinguish": {"VC-02"},
        "F-absolute": {"VC-08"}, "G-riskowner": {"VC-06"}, "H-control-plane": {"VC-04"},
    }.get(cat, set())
    return sorted(a)


def derive_requirements(d, tr):
    r = {"R1", "R6"}
    if tr["admitted"]:
        r |= {"R2"}
    if tr["consulted"]:
        r |= {"R3"}
    if tr["controlling"] and tr["controlling"] != "none_tie":
        r |= {"R4"}
    if tr["expiry_set"] or d["category"] in ("I-lapsed", "U-renewal"):
        r |= {"R5"}
    if d["contest_to"] >= 2:
        r |= {"R7"}
    return sorted(r)


def finalize():
    os.makedirs(os.path.join(ROOT, "corpus"), exist_ok=True)
    pack = {
        "pack": "semifab",
        "display_name": "VetPOC — veterinary practice management and point of care",
        "corpus_version": RULEBOOK["corpus_version"],
        "rulebook_version": RULEBOOK["rulebook_version"],
        "theta": THETA, "N0": PARAMS["N0"], "delta_days": PARAMS["delta_days"],
        "case_count": len(cases),
        "categories": {n: sum(1 for c in cases if c["category"] == n)
                       for n, _c, _d in vocab.CATEGORIES},
        "like_case_pairs": like_pairs,
        "cases": cases,
    }
    _write(os.path.join(ROOT, "corpus", "cases.json"), pack)
    with open(os.path.join(ROOT, "corpus", "cases.jsonl"), "w") as fh:
        for c in cases:
            fh.write(json.dumps(c, sort_keys=True) + "\n")
    _write(os.path.join(ROOT, "corpus", "store_seed_initial.json"),
           {"records": [r.to_dict() for r in seed_records]})
    _write(os.path.join(ROOT, "corpus", "store_seed.json"),
           {"records": [r.to_dict() for r in store]})
    _write(os.path.join(ROOT, "corpus", "docket.json"), {"entries": docket})
    _write(os.path.join(ROOT, "corpus", "anomalies.json"),
           {"count": len(anomalies), "entries": anomalies})

    routes, decisions = {}, {}
    for c in cases:
        routes[c["expect"]["route"]] = routes.get(c["expect"]["route"], 0) + 1
        dec = c["expect"]["final_decision"]
        decisions[dec] = decisions.get(dec, 0) + 1

    manifest = {
        "corpus_version": RULEBOOK["corpus_version"], "generator_seed": SEED,
        "cases": len(cases), "opening_store": len(seed_records),
        "final_store": len(store), "records_written_in_run": len(store) - len(seed_records),
        "docket_entries": len(docket), "like_case_pairs": len(like_pairs),
        "consolidation_classes": len(consolidation_seen),
        "construction_anomalies": len(anomalies),
        "routes": routes, "decisions": decisions, "categories": pack["categories"],
        "sha256": {},
    }
    for name in ("cases.json", "cases.jsonl", "store_seed_initial.json",
                 "store_seed.json", "docket.json"):
        path = os.path.join(ROOT, "corpus", name)
        manifest["sha256"][name] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    _write(os.path.join(ROOT, "corpus", "manifest.json"), manifest)
    print(json.dumps({k: v for k, v in manifest.items() if k != "sha256"}, indent=2))


def _write(path, obj):
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2, sort_keys=False)
        fh.write("\n")


if __name__ == "__main__":
    main()
# --- scenario extension (corpus 2.0.0) ---
