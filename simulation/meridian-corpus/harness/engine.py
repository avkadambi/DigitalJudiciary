"""
Meridian Financial reference adjudication engine.

A minimal, dependency-free implementation of the ordering procedure of
"When Retrieval Binds" (Chapter 5 §4.6) together with axioms A1-A9, sufficient
to replay the corpus and check every case's expect block against an executed
trace rather than an assertion.

This is a *reference* engine, not the Digital Judiciary reference implementation.
Its purpose is that any financial-technology vendor can run the corpus against
their own adjudicator and compare, and that the corpus's own ground truth is
computed rather than declared.

Standard library only. Deterministic: same inputs, same trace, byte for byte.

Release 5.11.0 — the distinguishing gate is a comparison kernel
-----------------------------------------------------------------
The gate used to be one line: a record is distinguished when its premise is
not a subset of the case's facts. That line is still the whole of the gate for
a corpus whose facts are boolean and closed-world, and every trace this engine
produced before 5.11.0 is reproduced byte for byte (VC-51 checks the
reduction on every gate-reaching case). What changed is that the line is now
the tolerance-zero, all-recorded special case of a kernel that also answers
two questions the old gate could not ask:

  * **Silence.** A fact can now be *unrecorded* — neither present nor absent —
    which is what an extractor that abstains produces (see
    ``simulation/tools/extraction``). The old gate read "not recorded" as
    "absent", and under a rule of precedence that reading is wrong in both
    directions: a silence would defeat a record that should govern, or, under
    any tolerance, bind on a premise nobody established. The kernel gives
    silence its own admission status, PREMISE_UNPROVEN, which outranks
    DISTINGUISHED and never binds (VC-52 checks that no bind survives the
    silencing of one premise factor).
  * **Magnitude.** A premise factor may carry a value and a declared tolerance
    (``constitution/dimensions.json``). "Weaker beyond the tolerance" is then
    the distinguishing test, a-fortiori admission is reported separately from
    tolerant admission, and coherence rules at load refuse a tolerance on an
    absolute provision's factor. The released corpora carry no magnitudes yet;
    the mechanism is exercised by VC-51's self-test so that a corpus that adds
    them inherits a gate that has already been shown to work.

The four admission statuses and the five case-level gate outcomes are the
vocabulary of the Likewise comparative-review engine (0.15.0), re-implemented
here rather than imported: the packs promise a standard-library runtime.

Release 5.12.0 — records are constructed, not assumed
-----------------------------------------------------
A citation now carries a stance (superseded / followed / distinguished /
unstated) and only a SUPERSEDED citation lets a conflicting newer holding
displace the older one in the ordering rule; a citation with no stance on a
legacy record is read as superseded, so every 5.11.0 trace is reproduced
(VC-54). Records carry `construction` provenance for premise, scope and
cites, so a record whose premise was extracted from a rationale is
distinguishable from one whose premise was authored. The extraction stage
that fills those fields, with the inverted (inclusion-biased) floor a premise
needs, is `simulation/tools/extraction/records.py`.

Release 5.13.0 — what the record did not see
--------------------------------------------
Two more rungs on the admission ladder, both about the record's blind spots
rather than the case's shortfalls. ADVERSE_UNADDRESSED: a permissive holding
does not govern a case that carries a violating factor of any engaged
provision the record's facts never contained — the gate was one-directional
before, and a permit on {a, b} bound a case doing {a, b, v} a-fortiori.
PRIOR_TEXT: a record decided under provision text version n does not govern
once an adopted amendment (rulebook `amendment_history`) has touched a factor
the holding turned on; a citation-only amendment touches nothing and
unsettles nothing. Both are inert on the released corpora (VC-55, VC-56
measure zero traces changed) and both fire on the synthetic cases that need
them; the discriminating suite gains S9 for the first.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

# ---------------------------------------------------------------------------
# Ordering constants
# ---------------------------------------------------------------------------

AUTH_RANK = {"judges": 1, "riskowner": 2}

THETA_DEFAULT = 0.25

# Outcomes an interpretation can carry.
PERMIT = "permit"
PERMIT_CONDITIONAL = "permit_conditional"
DENY = "deny"

# Routes a case can take through the pipeline.
ROUTE_ABSOLUTE = "absolute_shortcircuit"
ROUTE_BOUND = "bound_by_precedent"
ROUTE_FRESH = "fresh_interpretation"
ROUTE_TIE = "fresh_interpretation_after_tie"
ROUTE_CONSOLIDATED = "consolidated_citation"
ROUTE_DOCKET_DECLINED = "docketed_declined"
ROUTE_DOCKET_NULL = "docketed_null"
ROUTE_FLOOR_UNRESOLVED = "floor_unresolved"   # 5.11.0: an absolute floor's factor is unrecorded

# ---------------------------------------------------------------------------
# The comparison kernel's vocabulary
# ---------------------------------------------------------------------------

# Admission status of ONE candidate record against the present case. Ranked:
# PREMISE_UNPROVEN outranks DISTINGUISHED outranks TOLERANT outranks A_FORTIORI.
# The ranking is the safety argument — a premise the case never established
# defeats a record however favourable the recorded dimensions look.
A_FORTIORI = "a_fortiori"              # at least as strong on every premise factor at tolerance 0
TOLERANT = "tolerant"                  # admitted, but the admission rests on a declared tolerance
DISTINGUISHED = "distinguished"        # weaker beyond tolerance on some premise factor
PREMISE_UNPROVEN = "premise_unproven"  # the case is silent on a premise factor
# 5.13.0 — two more ways out of admission, both about what the RECORD did not see.
ADVERSE_UNADDRESSED = "adverse_unaddressed"  # the case carries a violating factor the record never considered
PRIOR_TEXT = "decided_under_prior_text"      # the provision was amended on a factor the holding turned on
ADMISSION_STATUS = (A_FORTIORI, TOLERANT, DISTINGUISHED, PREMISE_UNPROVEN, ADVERSE_UNADDRESSED, PRIOR_TEXT)
ADMITTED = frozenset({A_FORTIORI, TOLERANT})
PERMISSIVE = frozenset({PERMIT, PERMIT_CONDITIONAL})

# Gate outcome for the CASE: exactly one, and the empty survivor set keeps its
# four causes apart instead of collapsing into one empty list.
GOVERNED = "governed"                              # a controlling record was found
NO_CANDIDATES = "no_candidates"                    # retrieval returned nothing
ALL_DISTINGUISHED = "all_distinguished"            # candidates existed; every one was distinguished
PREMISE_NOT_ESTABLISHED = "premise_not_established"  # no survivor, and some candidate fell on silence
NO_CONTROLLING = "no_controlling"                  # survivors, but the ordering rule tied
ADVERSE_FACT = "adverse_fact_unaddressed"          # no survivor; some candidate fell on a fact it never saw
PRIOR_TEXT_ONLY = "decided_under_prior_text"       # no survivor; some candidate was decided under amended text
GATE_OUTCOMES = (GOVERNED, NO_CANDIDATES, ALL_DISTINGUISHED, PREMISE_NOT_ESTABLISHED, NO_CONTROLLING,
                 ADVERSE_FACT, PRIOR_TEXT_ONLY)

# The provisions the gate reads adverse factors and text versions from. Set by
# `adjudicate` on every call and by `load_constitution`; a caller of `gate`
# may pass its own. Without any, the two 5.13.0 checks are inert and the gate
# is the 5.12.0 gate.
_PROVISIONS: dict = {}

# Per-factor comparison results (the five-valued chain, silence split out).
STRICTLY_WORSE = "strictly_worse"
WEAKLY_WORSE = "weakly_worse"
TIED = "tied"
UNRECORDED = "unrecorded"
WEAKLY_BETTER = "weakly_better"
STRICTLY_BETTER = "strictly_better"

# Citation stance (5.12.0). A record that names an earlier record does so for a
# reason, and only one of the reasons is supersession. `_displaces` reads the
# stance; a citation with no stance recorded is read as SUPERSEDED for records
# built before stances existed (the generator asserts supersession when it
# writes a cite), and as UNSTATED — which does not displace — when the record
# was constructed by an extractor that could not tell. Under a rule of
# precedence the safe default for "I do not know why this was cited" is to
# leave the conflict standing and let the ordering tie and refer.
STANCE_SUPERSEDED = "superseded"
STANCE_FOLLOWED = "followed"
STANCE_DISTINGUISHED = "distinguished"
STANCE_UNSTATED = "unstated"
STANCES = (STANCE_SUPERSEDED, STANCE_FOLLOWED, STANCE_DISTINGUISHED, STANCE_UNSTATED)

# Declared dimensions: factor -> {"weaker_when": "lower"|"higher", "tolerance": float}.
# Empty means every factor is boolean, present = 1.0 / absent = 0.0, weaker when
# lower, tolerance 0 — which is exactly the containment gate.
DIMENSIONS: dict = {}


class DimensionError(ValueError):
    """A dimensions file that fails a coherence rule. Refused, never repaired."""


def load_dimensions(path: str, provisions: dict | None = None) -> dict:
    """Load and validate constitution/dimensions.json.

    Coherence rules, each a mistake that would otherwise be silent:
      D1  weaker_when is declared, lower or higher — never inferred from a name;
      D2  tolerance is a finite number >= 0;
      D3  a factor of an ABSOLUTE provision carries tolerance 0 — a floor is
          not a matter of degree;
      D4  when provisions are given, every dimension names a factor the
          constitution knows.
    """
    global DIMENSIONS
    with open(path) as fh:
        raw = json.load(fh)
    dims = raw.get("dimensions", raw) if isinstance(raw, dict) else {}
    failures = []
    known = set()
    absolute_factors = set()
    if provisions:
        for p in provisions.values():
            known.update(p.comply_factors)
            known.update(p.violate_factors)
            if p.absolute:
                absolute_factors.update(p.comply_factors)
                absolute_factors.update(p.violate_factors)
    out = {}
    for name, d in sorted(dims.items()):
        ww = d.get("weaker_when")
        tol = d.get("tolerance", 0.0)
        if ww not in ("lower", "higher"):
            failures.append(("D1", name, f"weaker_when must be lower|higher, got {ww!r}"))
        if not isinstance(tol, (int, float)) or isinstance(tol, bool) or tol != tol or tol < 0:
            failures.append(("D2", name, f"tolerance must be a number >= 0, got {tol!r}"))
        elif name in absolute_factors and tol > 0:
            failures.append(("D3", name, "a factor of an absolute provision may not carry a tolerance"))
        if provisions and name not in known:
            failures.append(("D4", name, "not a factor of any provision"))
        out[name] = {"weaker_when": ww, "tolerance": float(tol) if isinstance(tol, (int, float)) else tol,
                     "unit": d.get("unit")}
    if failures:
        raise DimensionError(failures)
    DIMENSIONS = out
    return out


# ---------------------------------------------------------------------------
# Data objects
# ---------------------------------------------------------------------------


@dataclass
class Provision:
    id: str
    family: str
    title: str
    absolute: bool
    citation: str
    source_status: str
    comply_factors: list
    violate_factors: list
    tau: int  # per-provision charging threshold, constitutional (CC-29)
    scope_domain: str
    version: int = 1                 # 5.13.0: the provision TEXT version; bumped by an adopted amendment
    amendments: list = field(default_factory=list)  # [{"version": n, "touched_factors": [...]}], ascending

    @staticmethod
    def from_dict(d: dict) -> "Provision":
        hist = list(d.get("amendment_history") or [])
        versions = [int(a.get("version", 0)) for a in hist]
        if versions != sorted(versions) or len(set(versions)) != len(versions) or any(v < 2 for v in versions):
            raise ValueError(f"{d['id']}: amendment_history versions must be distinct, ascending and >= 2")
        version = int(d.get("version", (versions[-1] if versions else 1)))
        if versions and version != versions[-1]:
            raise ValueError(f"{d['id']}: version {version} does not match the last amendment {versions[-1]}")
        return Provision(
            id=d["id"],
            family=d["family"],
            title=d["title"],
            absolute=d["absolute"],
            citation=d.get("citation", ""),
            source_status=d.get("source_status", ""),
            comply_factors=list(d["factors"]["comply"]),
            violate_factors=list(d["factors"]["violate"]),
            tau=int(d.get("tau", 40)),
            scope_domain=d.get("scope_domain", d["family"]),
            version=version,
            amendments=[{"version": int(a["version"]), "touched_factors": sorted(a.get("touched_factors") or [])}
                        for a in hist],
        )

    def touched_since(self, version: int) -> set:
        """Factors an adopted amendment touched after text version `version`."""
        out: set = set()
        for a in self.amendments:
            if a["version"] > version:
                out.update(a["touched_factors"])
        return out


@dataclass
class Record:
    """Chapter 5, Definition 8 — the precedent record."""

    id: str
    case: str
    prov: str
    rules: list
    facts: list
    premise: list
    interp: str          # the holding: permit | permit_conditional | deny
    auth_class: str      # judges | riskowner
    auth_id: str
    rationale: str
    scope_domain: str
    scope_width: int     # smaller is narrower
    ts: int              # ordinal resolution time
    depth: int
    expiry: int | None   # ordinal; None for interpretive records
    referral: str | None  # pending | rejected | adopted | None
    cites: list
    outcome: str
    admission_ground: str  # clause_i | clause_ii | seed
    values: dict = field(default_factory=dict)  # magnitude of a premise factor, when declared
    cite_stance: dict = field(default_factory=dict)  # cited record id -> stance; absent = superseded (legacy)
    construction: dict = field(default_factory=dict)  # provenance of premise/scope/cites: authored | extracted
    prov_version: int = 1            # 5.13.0: the provision text version the holding was decided under

    def stance_of(self, cited_id: str) -> str:
        return self.cite_stance.get(cited_id, STANCE_SUPERSEDED)

    def lapsed_at(self, now: int) -> bool:
        return self.expiry is not None and now > self.expiry

    def to_dict(self) -> dict:
        d = {
            "id": self.id,
            "case": self.case,
            "prov": self.prov,
            "rules": self.rules,
            "facts": self.facts,
            "premise": self.premise,
            "interp": self.interp,
            "auth_class": self.auth_class,
            "auth_id": self.auth_id,
            "rationale": self.rationale,
            "scope": {"domain": self.scope_domain, "width": self.scope_width},
            "ts": self.ts,
            "depth": self.depth,
            "expiry": self.expiry,
            "referral": self.referral,
            "cites": self.cites,
            "outcome": self.outcome,
            "admission_ground": self.admission_ground,
        }
        if self.values:
            d["values"] = dict(self.values)
        if self.cite_stance:
            d["cite_stance"] = dict(self.cite_stance)
        if self.construction:
            d["construction"] = dict(self.construction)
        if self.prov_version != 1:
            d["prov_version"] = self.prov_version
        return d

    @staticmethod
    def from_dict(d: dict) -> "Record":
        return Record(
            id=d["id"],
            case=d["case"],
            prov=d["prov"],
            rules=list(d["rules"]),
            facts=list(d["facts"]),
            premise=list(d["premise"]),
            interp=d["interp"],
            auth_class=d["auth_class"],
            auth_id=d["auth_id"],
            rationale=d["rationale"],
            scope_domain=d["scope"]["domain"],
            scope_width=int(d["scope"]["width"]),
            ts=int(d["ts"]),
            depth=int(d["depth"]),
            expiry=d["expiry"],
            referral=d["referral"],
            cites=list(d["cites"]),
            outcome=d["outcome"],
            admission_ground=d["admission_ground"],
            values=dict(d.get("values") or {}),
            cite_stance=dict(d.get("cite_stance") or {}),
            construction=dict(d.get("construction") or {}),
            prov_version=int(d.get("prov_version", 1)),
        )


@dataclass
class Case:
    """Chapter 5, Definition 3 — a case is (id, rules, facts), plus the
    procedural and narrative fields a corpus needs.

    Facts are three-valued from 5.11.0: a factor is PRESENT (in `facts`),
    UNRECORDED (in `unrecorded` — the characterisation stage could not say),
    or ABSENT (neither). `values` carries a magnitude for a factor the
    constitution declares as a dimension."""

    id: str
    category: str
    rules: list
    facts: list
    ts: int
    contest_to: int          # 0 uncontested, 2/3 resolved above first, 4 risk owner
    author_kind: str         # human | ai-agent
    control_plane: bool = False
    consolidation_signature: str | None = None
    extra: dict = field(default_factory=dict)
    unrecorded: list = field(default_factory=list)
    values: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# The comparison kernel
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Comparison:
    """One premise factor's verdict on one (record, case) pair."""

    factor: str
    order: str
    margin: float          # how far the case falls short (positive = weaker)
    tolerance: float


@dataclass(frozen=True)
class Admission:
    """What one candidate record says about the present case."""

    record_id: str
    status: str
    comparisons: tuple
    distinguishing: tuple = ()   # factors that defeated it
    unproven: tuple = ()         # premise factors the case is silent on
    adverse: tuple = ()          # violating factors the case carries and the record never saw
    touched: tuple = ()          # premise factors an adopted amendment touched since the holding

    @property
    def admitted(self) -> bool:
        return self.status in ADMITTED


def _subject_value(factor: str, case: Case):
    """The case's value on a premise factor: a number, or None for silence.

    A declared dimension is read from `values` only — a magnitude factor that
    arrives without its magnitude is unrecorded, not present. A boolean factor
    is 1.0 when present, 0.0 when absent, None when unrecorded."""
    if factor in DIMENSIONS:
        v = case.values.get(factor)
        return None if v is None else float(v)
    if factor in case.unrecorded:
        return None
    return 1.0 if factor in case.facts else 0.0


def _reference_value(factor: str, record: Record):
    if factor in DIMENSIONS:
        v = record.values.get(factor)
        return None if v is None else float(v)
    return 1.0


def compare(factor: str, subject, reference) -> Comparison:
    """Place one premise factor on the chain. None on either side is silence."""
    dim = DIMENSIONS.get(factor)
    tol = float(dim["tolerance"]) if dim else 0.0
    if subject is None or reference is None:
        return Comparison(factor, UNRECORDED, float("nan"), tol)
    higher_is_weaker = bool(dim and dim["weaker_when"] == "higher")
    shortfall = (subject - reference) if higher_is_weaker else (reference - subject)
    if shortfall > tol:
        order = STRICTLY_WORSE
    elif shortfall > 0:
        order = WEAKLY_WORSE
    elif shortfall == 0:
        order = TIED
    elif -shortfall > tol:
        order = STRICTLY_BETTER
    else:
        order = WEAKLY_BETTER
    return Comparison(factor, order, shortfall, tol)


def adverse_unaddressed(record: Record, case: Case, provisions: dict | None = None) -> tuple:
    """Violating factors of any engaged provision that the case carries and the
    record's facts do not — facts the holding never considered.

    Asymmetric on purpose: only a PERMISSIVE holding is exposed. A precedent
    that permitted on {a, b} says nothing about a case that also does v; a
    precedent that denied for v is not cured by the case's extra compliance.
    A6 already catches v when the provision is absolute; this is the same
    rule for every ordinary provision, and for a second engaged provision
    the record was never about.
    """
    provisions = provisions if provisions is not None else _PROVISIONS
    if record.interp not in PERMISSIVE or not provisions:
        return ()
    facts, seen = set(case.facts), set(record.facts)
    out: set = set()
    for pid in case.rules:
        p = provisions.get(pid)
        if p is not None:
            out |= (facts & set(p.violate_factors)) - seen
    return tuple(sorted(out))


def touched_premise(record: Record, provisions: dict | None = None) -> tuple:
    """Premise factors an adopted amendment of the record's provision touched
    after the text version the holding was decided under. A citation-only
    amendment touches nothing and unsettles nothing."""
    provisions = provisions if provisions is not None else _PROVISIONS
    p = provisions.get(record.prov) if provisions else None
    if p is None or p.version <= record.prov_version:
        return ()
    return tuple(sorted(p.touched_since(record.prov_version) & set(record.premise)))


def admit(record: Record, case: Case, provisions: dict | None = None) -> Admission:
    """Does this record govern, on the premise factors it rested on?

    The ladder, top first — each rung is a reason the record cannot govern
    however the rungs below it read:

        PRIOR_TEXT         the text it construed was amended on a factor it turned on
        PREMISE_UNPROVEN   the case is silent on a premise factor
        ADVERSE_UNADDRESSED the case carries a violating factor the record never saw (permissive holdings)
        DISTINGUISHED      the case is weaker beyond tolerance on a premise factor
        TOLERANT / A_FORTIORI  admitted

    At tolerance 0, every factor recorded, no amendments and no adverse facts
    this is `set(premise) <= facts` exactly (VC-51); VC-55 and VC-56 check
    that the two 5.13.0 rungs change nothing on the released corpora and fire
    on the synthetic cases that need them.
    """
    touched = touched_premise(record, provisions)
    comparisons, distinguishing, unproven = [], [], []
    for f in record.premise:
        c = compare(f, _subject_value(f, case), _reference_value(f, record))
        comparisons.append(c)
        if c.order == UNRECORDED:
            unproven.append(f)
        elif c.order == STRICTLY_WORSE:
            distinguishing.append(f)
    cmp_t = tuple(comparisons)
    if touched:
        return Admission(record.id, PRIOR_TEXT, cmp_t, tuple(distinguishing), tuple(unproven), touched=touched)
    if unproven:
        return Admission(record.id, PREMISE_UNPROVEN, cmp_t, tuple(distinguishing), tuple(unproven))
    adverse = adverse_unaddressed(record, case, provisions)
    if adverse and not distinguishing:
        return Admission(record.id, ADVERSE_UNADDRESSED, cmp_t, adverse=adverse)
    if distinguishing:
        return Admission(record.id, DISTINGUISHED, cmp_t, tuple(distinguishing), adverse=adverse)
    if all(c.order in (TIED, WEAKLY_BETTER, STRICTLY_BETTER) for c in cmp_t):
        return Admission(record.id, A_FORTIORI, cmp_t)
    return Admission(record.id, TOLERANT, cmp_t)


# ---------------------------------------------------------------------------
# The ordering procedure (§4.6)
# ---------------------------------------------------------------------------


def coverage(record: Record, case_facts: set) -> float:
    """cov(r, c) = |premise(r) ∩ facts(c)| / |premise(r)|."""
    if not record.premise:
        return 0.0
    prem = set(record.premise)
    return len(prem & case_facts) / len(prem)


def violates(case_facts: set, prov: Provision) -> bool:
    return bool(case_facts & set(prov.violate_factors))


def retrieve(case: Case, store: list, theta: float = THETA_DEFAULT) -> list:
    facts = set(case.facts)
    rules = set(case.rules)
    return [
        r
        for r in store
        if r.prov in rules
        and not r.lapsed_at(case.ts)
        and coverage(r, facts) >= theta
    ]


def gate_admissions(candidates: list, case: Case, provisions: dict | None = None) -> list:
    """One Admission per candidate, in candidate order."""
    return [admit(r, case, provisions) for r in candidates]


def gate(candidates: list, case: Case, provisions: dict | None = None) -> tuple:
    """distinguish(r, c) holds exactly when the case is weaker than premise(r)
    beyond tolerance on some factor, carries a violating factor the record
    never saw, or the record construed amended text. Returns (survivors,
    distinguished); records that fell on silence are in neither list and are
    reported by `gate_admissions`."""
    survivors, distinguished = [], []
    for r, adm in zip(candidates, gate_admissions(candidates, case, provisions)):
        if adm.status in ADMITTED:
            survivors.append(r)
        elif adm.status in (DISTINGUISHED, ADVERSE_UNADDRESSED, PRIOR_TEXT):
            distinguished.append(r)
    return survivors, distinguished


def _displaces(newer: Record, older: Record) -> bool:
    """Recency conditioned on express supersession: a newer survivor displaces
    an older one when the two holdings agree, and when they conflict only if
    the newer record names the older in cites."""
    if newer.ts <= older.ts:
        return False
    if newer.interp == older.interp:
        return True
    return older.id in newer.cites and newer.stance_of(older.id) == STANCE_SUPERSEDED


def order(survivors: list) -> tuple:
    """Return (controlling, keys_applied). controlling is a Record, None, or
    the string 'none_tie'."""
    keys: list = []
    if not survivors:
        return None, keys
    pool = list(survivors)

    # 1. auth_class
    if len(pool) > 1:
        top = max(AUTH_RANK[r.auth_class] for r in pool)
        nxt = [r for r in pool if AUTH_RANK[r.auth_class] == top]
        if len(nxt) < len(pool):
            keys.append("auth_class")
        pool = nxt

    # 2. ts, conditioned on express supersession
    if len(pool) > 1:
        maximal = [r for r in pool if not any(_displaces(s, r) for s in pool if s.id != r.id)]
        if maximal and len(maximal) < len(pool):
            keys.append("ts")
            pool = maximal

    # 3. scope — narrower preferred, incomparable domains tie
    if len(pool) > 1:
        def dominated(r):
            return any(
                s.scope_domain == r.scope_domain and s.scope_width < r.scope_width
                for s in pool
                if s.id != r.id
            )
        maximal = [r for r in pool if not dominated(r)]
        if maximal and len(maximal) < len(pool):
            keys.append("scope")
            pool = maximal

    # 4. depth — more re-adjudications preferred
    if len(pool) > 1:
        top = max(r.depth for r in pool)
        nxt = [r for r in pool if r.depth == top]
        if len(nxt) < len(pool):
            keys.append("depth")
        pool = nxt

    if len(pool) == 1:
        return pool[0], keys
    return "none_tie", keys


def rate(case: Case, provisions: dict) -> int:
    """The prosecutor's violation-likelihood rating, deterministic and model-free.

    Rating is 100 when a violating factor of an engaged provision is present,
    and otherwise a small score driven by how much of the provision's compliant
    vocabulary the case's facts already satisfy. A case whose facts are wholly
    compliant rates low and is declined, which is what puts it on the Docket.
    """
    facts = set(case.facts)
    best = 0
    for pid in case.rules:
        p = provisions[pid]
        if facts & set(p.violate_factors):
            return 100
        comply = set(p.comply_factors)
        if comply:
            satisfied = len(facts & comply) / len(comply)
        else:
            satisfied = 0.0
        # Unsatisfied compliant vocabulary is weak evidence something is missing.
        score = int(round(20 + 60 * (1.0 - satisfied)))
        best = max(best, score)
    return best


# ---------------------------------------------------------------------------
# Adjudication
# ---------------------------------------------------------------------------


def adjudicate(case: Case, store: list, provisions: dict, theta: float = THETA_DEFAULT) -> dict:
    """Run one case against the store. Returns the executed trace."""
    global _PROVISIONS
    _PROVISIONS = provisions
    facts = set(case.facts)

    trace: dict[str, Any] = {
        "case": case.id,
        "rules": list(case.rules),
        "consulted": [],
        "distinguished": [],
        "premise_unproven": [],
        "adverse_unaddressed": [],
        "prior_text": [],
        "admissions": {},
        "gate_outcome": None,
        "controlling": None,
        "keys_applied": [],
        "route": None,
        "decision": None,
        "escalated_to": None,
        "admitted": False,
        "admission_ground": None,
        "referral_emitted": False,
        "expiry_set": False,
        "docket_route": None,
        "rating": None,
        "tau": None,
    }

    # --- Evaluator: is any provision engaged at all? (Definition 14, ⊥ route)
    if not case.rules:
        trace["route"] = ROUTE_DOCKET_NULL
        trace["decision"] = PERMIT
        trace["docket_route"] = "null"
        return trace

    # --- A6: absolute short-circuit. No retrieval runs.
    for pid in case.rules:
        p = provisions[pid]
        if p.absolute and violates(facts, p):
            trace["route"] = ROUTE_ABSOLUTE
            trace["decision"] = DENY
            trace["absolute_provision"] = pid
            return trace

    # --- A6 under silence (5.11.0). Silence never binds a precedent; it must
    # not clear a floor either. If the case is UNRECORDED on a violating factor
    # of an engaged absolute provision, nobody has established that the floor
    # is intact, and the change is refused and referred for characterisation
    # rather than allowed to proceed to retrieval on the strength of a gap.
    # Nothing is stored: a refusal on silence is not a holding. Unreachable on
    # a closed-world corpus; measured by tools/extraction (floors_missed).
    if case.unrecorded:
        quiet = set(case.unrecorded)
        for pid in case.rules:
            p = provisions[pid]
            if p.absolute and (quiet & set(p.violate_factors)):
                trace["route"] = ROUTE_FLOOR_UNRESOLVED
                trace["decision"] = DENY
                trace["absolute_provision"] = pid
                trace["unresolved_factors"] = sorted(quiet & set(p.violate_factors))
                trace["referral_emitted"] = True
                return trace

    # --- Control-plane changes are routed to a draft amendment (A3).
    if case.control_plane:
        trace["route"] = ROUTE_FRESH
        trace["decision"] = DENY
        trace["draft_amendment"] = True
        trace["referral_emitted"] = True
        return trace

    # --- Retrieval, gate, ordering
    candidates = retrieve(case, store, theta)
    admissions = gate_admissions(candidates, case, provisions)
    survivors = [r for r, a in zip(candidates, admissions) if a.admitted]
    trace["consulted"] = [r.id for r in candidates]
    trace["distinguished"] = [a.record_id for a in admissions if a.status == DISTINGUISHED]
    trace["premise_unproven"] = [a.record_id for a in admissions if a.status == PREMISE_UNPROVEN]
    trace["adverse_unaddressed"] = {a.record_id: list(a.adverse) for a in admissions if a.status == ADVERSE_UNADDRESSED}
    trace["prior_text"] = {a.record_id: list(a.touched) for a in admissions if a.status == PRIOR_TEXT}
    trace["admissions"] = {a.record_id: a.status for a in admissions}
    controlling, keys = order(survivors)
    trace["keys_applied"] = keys

    if isinstance(controlling, Record):
        trace["gate_outcome"] = GOVERNED
        trace["controlling"] = controlling.id
        trace["route"] = ROUTE_BOUND
        trace["decision"] = controlling.interp  # A8: consistent with the holding
    elif controlling == "none_tie":
        trace["gate_outcome"] = NO_CONTROLLING
        trace["controlling"] = "none_tie"
        trace["route"] = ROUTE_TIE
        trace["decision"] = _base_eval(facts, case, provisions)
        trace["referral_emitted"] = True  # unbroken conflict referred to Lawmakers
    else:
        # No record survives. The cause is named: nothing retrieved, everything
        # distinguished on the merits, or a premise the case never established.
        if not candidates:
            trace["gate_outcome"] = NO_CANDIDATES
        elif trace["prior_text"]:
            trace["gate_outcome"] = PRIOR_TEXT_ONLY
        elif trace["premise_unproven"]:
            trace["gate_outcome"] = PREMISE_NOT_ESTABLISHED
        elif trace["adverse_unaddressed"]:
            trace["gate_outcome"] = ADVERSE_FACT
        else:
            trace["gate_outcome"] = ALL_DISTINGUISHED
        # The prosecutor decides whether to charge.
        v = rate(case, provisions)
        tau = min(provisions[p].tau for p in case.rules)
        trace["rating"] = v
        trace["tau"] = tau
        if v < tau:
            trace["route"] = ROUTE_DOCKET_DECLINED
            trace["decision"] = PERMIT
            trace["docket_route"] = "declined"
            return trace
        trace["route"] = ROUTE_FRESH
        trace["decision"] = _base_eval(facts, case, provisions)

    # --- Escalation and the risk owner (A4, A7)
    if case.contest_to >= 4:
        trace["escalated_to"] = "riskowner"
        trace["decision"] = PERMIT_CONDITIONAL
        trace["referral_emitted"] = True
        trace["expiry_set"] = True
    elif case.contest_to >= 2:
        trace["escalated_to"] = f"J{case.contest_to}"

    # --- Definition 7 clause (i): admission on contest resolved above first
    if case.contest_to >= 2:
        trace["admitted"] = True
        trace["admission_ground"] = "clause_i"

    # --- 5.14.0: no law on facts nobody established. A record's premise is
    # the set of facts the holding turned on; if the characterisation stage
    # left one of them UNRECORDED, writing the record without it would narrow
    # the premise and make the holding bind cases the instance never decided
    # (measured: 167 such over-binds on one pack before this rule). The
    # decision stands; the record is withheld and the case referred so that a
    # person can establish the fact and the record can be written on it.
    withheld = _premise_unestablished(case)
    if withheld and trace["admitted"]:
        trace["admitted"] = False
        trace["admission_ground"] = None
        trace["record_withheld"] = {"cause": "premise_not_established", "factors": withheld}
        trace["referral_emitted"] = True

    return trace


def _premise_unestablished(case: Case) -> list:
    """Hinted premise factors the case carries as unrecorded."""
    if not case.unrecorded:
        return []
    hinted = case.extra.get("premise") or case.facts
    return sorted(set(hinted) & set(case.unrecorded))


def _base_eval(facts: set, case: Case, provisions: dict) -> str:
    for pid in case.rules:
        if violates(facts, provisions[pid]):
            return DENY
    return PERMIT


# ---------------------------------------------------------------------------
# Replay
# ---------------------------------------------------------------------------


def replay(cases: list, seed_store: list, provisions: dict, theta: float = THETA_DEFAULT) -> dict:
    """Replay the corpus in chronological order, growing the store as contested
    cases resolve. Returns traces, the final store, and the docket."""
    store = [Record.from_dict(r) if isinstance(r, dict) else r for r in seed_store]
    traces, docket, records_written = [], [], []
    consolidation_seen: dict = {}

    for c in cases:
        case = c if isinstance(c, Case) else case_from_dict(c)
        tr = adjudicate(case, store, provisions, theta)

        # Definition 7 clause (ii): the representative of a consolidation class.
        if (
            case.consolidation_signature
            and tr["controlling"] is None
            and tr["route"] in (ROUTE_FRESH,)
            and case.consolidation_signature not in consolidation_seen
            and case.extra.get("class_representative")
            and not _premise_unestablished(case)
        ):
            consolidation_seen[case.consolidation_signature] = case.id
            tr["admitted"] = True
            tr["admission_ground"] = "clause_ii"
        elif case.consolidation_signature and case.extra.get("class_member"):
            tr["route"] = ROUTE_CONSOLIDATED
            tr["consulted"] = []
            tr["distinguished"] = []
            tr["premise_unproven"] = []
            tr["adverse_unaddressed"] = {}
            tr["prior_text"] = {}
            tr["admissions"] = {}
            tr["gate_outcome"] = None
            rep = consolidation_seen.get(case.consolidation_signature)
            tr["cites_representative"] = rep
            tr["admitted"] = False
            tr["admission_ground"] = None

        if tr["route"] in (ROUTE_DOCKET_DECLINED, ROUTE_DOCKET_NULL):
            docket.append(
                {
                    "case": case.id,
                    "route": "declined" if tr["route"] == ROUTE_DOCKET_DECLINED else "null",
                    "rules": list(case.rules) if tr["route"] == ROUTE_DOCKET_DECLINED else [],
                    "facts": list(case.facts),
                    "rating": tr["rating"],
                    "tau": tr["tau"],
                    "ts": case.ts,
                    "gate_outcome": tr["gate_outcome"],
                }
            )

        if tr["admitted"]:
            rec = _record_from(case, tr, provisions)
            store.append(rec)
            records_written.append(rec)

        traces.append(tr)

    return {
        "traces": traces,
        "store": store,
        "docket": docket,
        "records_written": records_written,
    }


# The authority roster, read from the constitution rather than invented here.
# An earlier form of _record_from minted "riskowner:medical-director" and
# "judge:J3-review" — identifiers from a sibling pack and from no pack at all.
# The records were internally consistent and named principals the constitution
# had never appointed, which is precisely what CC-01 and CC-02 exist to catch.
_ROSTER: dict = {}


def load_roster(path: str) -> None:
    """Bind the resolver identifiers to the published organizations file."""
    global _ROSTER
    with open(path) as fh:
        orgs = json.load(fh)
    by_branch: dict = {}
    for org in orgs["organizations"]:
        for p in org["principals"]:
            by_branch.setdefault(p["branch"], []).append(p["principal_id"])
    _ROSTER = {k: sorted(v) for k, v in by_branch.items()}


def _resolver(auth_class: str, depth: int) -> str:
    pool = _ROSTER.get(auth_class)
    if not pool:
        raise RuntimeError(
            f"no principal is appointed to the {auth_class!r} branch; "
            "call engine.load_roster(constitution/organizations.json) first")
    if auth_class == "riskowner":
        return pool[0]
    # Judges are ordered by instance: the deeper the contest, the higher the
    # instance that resolved it, capped at the highest appointed.
    return pool[min(max(1, depth - 1), len(pool) - 1)]


def _record_from(case: Case, tr: dict, provisions: dict) -> Record:
    prov = case.rules[0]
    auth_class = "riskowner" if tr["escalated_to"] == "riskowner" else "judges"
    auth_id = _resolver(auth_class, case.contest_to)
    # A premise is made of facts the case ESTABLISHED. An unrecorded factor is
    # not one of them, whatever the generator's premise hint says.
    premise = sorted(f for f in (case.extra.get("premise") or case.facts)
                     if f not in case.unrecorded)
    return Record(
        id=f"REC-{case.id}",
        case=case.id,
        prov=prov,
        rules=list(case.rules),
        facts=sorted(case.facts),
        premise=premise,
        interp=tr["decision"],
        auth_class=auth_class,
        auth_id=auth_id,
        rationale=case.extra.get("rationale", "") or f"Resolved on contest for {case.id}.",
        scope_domain=provisions[prov].scope_domain,
        scope_width=int(case.extra.get("scope_width", 3)),
        ts=case.ts,
        depth=max(1, case.contest_to),
        expiry=(case.ts + 180) if tr["expiry_set"] else None,
        referral="pending" if tr["referral_emitted"] else None,
        cites=list(case.extra.get("cites", [])),
        outcome=tr["decision"],
        admission_ground=tr["admission_ground"] or "clause_i",
        values={f: v for f, v in case.values.items() if f in premise},
        cite_stance={k: v for k, v in (case.extra.get("cite_stance") or {}).items() if v in STANCES},
        construction=dict(case.extra.get("construction") or {}),
        prov_version=provisions[prov].version,
    )


def case_from_dict(d: dict) -> Case:
    unrecorded = list(d.get("unrecorded") or [])
    facts = [f for f in d["facts"] if f not in unrecorded]
    return Case(
        id=d["id"],
        category=d["category"],
        rules=list(d["rules"]),
        facts=facts,
        ts=int(d["ts"]),
        contest_to=int(d.get("contest_to", 0)),
        author_kind=d.get("author", {}).get("kind", "human"),
        control_plane=bool(d.get("control_plane", False)),
        consolidation_signature=d.get("consolidation_signature"),
        extra=d.get("engine", {}) or {},
        unrecorded=unrecorded,
        values={k: float(v) for k, v in (d.get("values") or {}).items()},
    )


def load_constitution(path: str) -> dict:
    global _PROVISIONS
    with open(path) as fh:
        data = json.load(fh)
    _PROVISIONS = {p["id"]: Provision.from_dict(p) for p in data["provisions"]}
    return _PROVISIONS
