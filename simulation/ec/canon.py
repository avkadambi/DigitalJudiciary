"""
The canon: a company's constitution read as tiers (EC §3.1, DESIGN §2.1).

The Enterprise Conscience fast track does not re-adjudicate a provision each
time it is engaged. It reads the constitution once into a *canon* whose entries
are tiered by what they may yield to:

  T0  absolute: never traded, never tokened (the DJ's A6 floor, read here)
  T1  dispensable only by a token from an office outside the agent's line
  T2  tradable within a bound for an admitted reason (N, O, K)
  T3  customary: departures allowed in listed contexts, sampled for review

The tier rule is deterministic and runs over `constitution/rulebook.json`;
`build_canon` writes it, `build_all_canons.py` runs it for every pack. The six
value entries (EC Table 1) are the company's own commitments, which the DJ
never sees as provisions and which the gate reads alongside them.

Doctrine (`doctrine.py`) only ever writes to an entry's `gloss`. Tier, office
and violate factors are fixed at build time, which is what EC-08 checks.

Standard library only. Same rulebook, same canon, byte for byte.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

TIERS = ("T0", "T1", "T2", "T3")
KINDS = ("provision", "value")
ROLE = "coding-agent"
GOVERNANCE_LINE = "governance"
ENGINEERING_LINE = "engineering"

# The tier rule and the office set live in `authority.py` (Realism revision R2: authority
# follows policy ownership and a binding-citation test, not harm tags).
from . import authority as _auth  # noqa: E402

OFFICE_ACCESSIBILITY = _auth.OFFICE_ACCESSIBILITY
OFFICE_COMPLIANCE = _auth.OFFICE_COMPLIANCE
OFFICE_SECURITY = _auth.OFFICE_SECURITY
OFFICES = (_auth.OFFICE_SECURITY, _auth.OFFICE_SAFETY, _auth.OFFICE_LEGAL, OFFICE_COMPLIANCE, OFFICE_ACCESSIBILITY)
T3_PROVISION_CONTEXTS = ["internal-prototype", "spike"]   # advisory provisions (R2)

STANDING_EMERGENCY_CLASS = "incident-hotfix"

# EC Table 1: the six value entries. (suffix, tier, title, admitted_reasons, bound, contexts, office)
VALUE_TABLE = (
    ("VAL-SHIP", "T2",
     "Ship fast or test fully: ship with at most one open non-security checklist item, with a remediation ticket",
     ["N", "O"], {"max_open_items": 1, "ticket_required": True}, [], None),
    ("VAL-COST", "T2",
     "Cost or quality: cost cuts may not remove a documented quality control",
     ["K"], {"max_controls_removed": 0}, [], None),
    ("VAL-CUST", "T2",
     "Customer first: customer-visible latency regressions need a stated customer benefit",
     ["O"], {"max_regression_pct": 5}, [], None),
    ("VAL-ACC", "T1",
     "Accessibility beyond law: never remove an existing accessibility feature without a token from the accessibility lead",
     [], {}, [], OFFICE_ACCESSIBILITY),
    ("VAL-STYLE", "T3",
     "House style for alternative text and messages",
     ["N", "O", "K"], {}, ["internal-prototype", "spike"], None),
    ("VAL-DOCS", "T3",
     "Documentation currency: docs updated with the change",
     ["N", "O", "K"], {}, ["hotfix", "internal-prototype"], None),
)


@dataclass
class Office:
    """An issuing office. Tokens are valid only from an office outside the
    agent's reporting line (EC §3.3); every office here reports to governance."""

    id: str
    reporting_line: str
    may_issue_for: list = field(default_factory=list)   # act classes

    def to_dict(self) -> dict:
        return {"id": self.id, "reporting_line": self.reporting_line, "may_issue_for": list(self.may_issue_for)}

    @staticmethod
    def from_dict(d: dict) -> "Office":
        return Office(id=d["id"], reporting_line=d["reporting_line"], may_issue_for=list(d.get("may_issue_for") or []))


@dataclass
class Gloss:
    """The doctrinal layer on an entry: the only part doctrine may write."""

    version: int = 1
    admitted_reasons: list = field(default_factory=list)
    bound: dict = field(default_factory=dict)
    contexts: list = field(default_factory=list)
    priorities: list = field(default_factory=list)
    holdings: list = field(default_factory=list)
    no_waiver_classes: list = field(default_factory=list)
    codified: bool = False

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "admitted_reasons": list(self.admitted_reasons),
            "bound": dict(self.bound),
            "contexts": list(self.contexts),
            "priorities": list(self.priorities),
            "holdings": [dict(h) for h in self.holdings],
            "no_waiver_classes": list(self.no_waiver_classes),
            "codified": bool(self.codified),
        }

    @staticmethod
    def from_dict(d: dict) -> "Gloss":
        return Gloss(
            version=int(d.get("version", 1)),
            admitted_reasons=list(d.get("admitted_reasons") or []),
            bound=dict(d.get("bound") or {}),
            contexts=list(d.get("contexts") or []),
            priorities=list(d.get("priorities") or []),
            holdings=[dict(h) for h in (d.get("holdings") or [])],
            no_waiver_classes=list(d.get("no_waiver_classes") or []),
            codified=bool(d.get("codified", False)),
        )


@dataclass
class CanonEntry:
    id: str
    kind: str
    tier: str
    title: str
    role: str
    family: str
    act_class: str
    office: str | None
    violate_factors: list
    gloss: Gloss
    canon_version: str

    def __post_init__(self):
        if self.tier not in TIERS:
            raise ValueError(f"{self.id}: unknown tier {self.tier!r}")
        if self.kind not in KINDS:
            raise ValueError(f"{self.id}: unknown kind {self.kind!r}")
        if self.tier == "T1" and not self.office:
            raise ValueError(f"{self.id}: a T1 entry names its issuing office")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "kind": self.kind,
            "tier": self.tier,
            "title": self.title,
            "role": self.role,
            "family": self.family,
            "act_class": self.act_class,
            "office": self.office,
            "violate_factors": list(self.violate_factors),
            "gloss": self.gloss.to_dict(),
            "canon_version": self.canon_version,
        }

    @staticmethod
    def from_dict(d: dict) -> "CanonEntry":
        return CanonEntry(
            id=d["id"],
            kind=d["kind"],
            tier=d["tier"],
            title=d.get("title", ""),
            role=d.get("role", ROLE),
            family=d["family"],
            act_class=d["act_class"],
            office=d.get("office"),
            violate_factors=list(d.get("violate_factors") or []),
            gloss=Gloss.from_dict(d.get("gloss") or {}),
            canon_version=d["canon_version"],
        )


class Canon:
    """The tiered reading of one pack's constitution plus its value entries."""

    def __init__(self, pack: str, version: str, entries: dict | None = None, offices: dict | None = None,
                 standing_emergency_classes: list | None = None,
                 standing_emergency_office: str = OFFICE_COMPLIANCE):
        self.pack = pack
        self.version = version
        self.entries: dict[str, CanonEntry] = dict(entries or {})
        self.offices: dict[str, Office] = dict(offices or {})
        self.standing_emergency_classes: list[str] = list(
            standing_emergency_classes if standing_emergency_classes is not None else [STANDING_EMERGENCY_CLASS])
        self.standing_emergency_office = standing_emergency_office

    # -- access -----------------------------------------------------------
    def entry(self, id: str) -> CanonEntry:
        return self.entries[id]

    def engaged(self, case_rules: list, value_ids: list) -> list:
        """The entries an arrival engages: the case's provisions, then the value
        ids the overlay drew. Ids the canon does not carry are skipped; order
        is preserved and duplicates dropped."""
        out, seen = [], set()
        for eid in list(case_rules) + list(value_ids):
            if eid in seen or eid not in self.entries:
                continue
            seen.add(eid)
            out.append(self.entries[eid])
        return out

    def by_tier(self) -> dict:
        counts = {t: 0 for t in TIERS}
        for e in self.entries.values():
            counts[e.tier] += 1
        return counts

    def bump(self) -> None:
        """New canon_version. Only a tier change calls this, and none happens at
        run time: the version is what the registry checks tokens against."""
        stem, _, num = self.version.rpartition("-")
        self.version = f"{stem}-{int(num) + 1:06d}"
        for e in self.entries.values():
            e.canon_version = self.version

    # -- serialisation ----------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "pack": self.pack,
            "version": self.version,
            "standing_emergency": {
                "office": self.standing_emergency_office,
                "act_classes": list(self.standing_emergency_classes),
                "requires": "recorded_cause",
            },
            "offices": {k: v.to_dict() for k, v in self.offices.items()},
            "entries": [e.to_dict() for e in self.entries.values()],
        }

    @staticmethod
    def from_dict(d: dict) -> "Canon":
        se = d.get("standing_emergency") or {}
        return Canon(
            pack=d["pack"],
            version=d["version"],
            entries={e["id"]: CanonEntry.from_dict(e) for e in d.get("entries") or []},
            offices={k: Office.from_dict(v) for k, v in (d.get("offices") or {}).items()},
            standing_emergency_classes=list(se.get("act_classes") or [STANDING_EMERGENCY_CLASS]),
            standing_emergency_office=se.get("office", OFFICE_COMPLIANCE),
        )

    @staticmethod
    def load(path: str) -> "Canon":
        with open(path) as fh:
            return Canon.from_dict(json.load(fh))

    def save(self, path: str) -> None:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w") as fh:
            json.dump(self.to_dict(), fh, indent=2, sort_keys=True)
            fh.write("\n")


# ---------------------------------------------------------------------------
# Building a canon from a pack
# ---------------------------------------------------------------------------


def tier_of(prov: dict) -> tuple[str, str | None]:
    """The tier rule (DESIGN §2.1; authority.py). Returns (tier, office)."""
    tier, office, _why = _auth.tier_of(prov)
    return tier, office


def _provision_gloss(tier: str) -> Gloss:
    if tier == "T2":
        return Gloss(admitted_reasons=["N", "O", "K"], bound={"max_departure_units": 1})
    if tier == "T3":
        return Gloss(admitted_reasons=["N", "O", "K"], contexts=list(T3_PROVISION_CONTEXTS))
    return Gloss()


def id_prefix(provision_id: str) -> str:
    """"VP-CS-001" -> "VP"; "DV-301" -> "DV"."""
    return provision_id.split("-", 1)[0]


def canon_version_for(pack: str) -> str:
    return f"{pack}-canon-000001"


def build_canon(pack_dir: str) -> Canon:
    """Read `<pack_dir>/constitution/rulebook.json` and tier every provision,
    then add the six value entries and the five offices."""
    pack = os.path.basename(os.path.normpath(pack_dir))
    with open(os.path.join(pack_dir, "constitution", "rulebook.json")) as fh:
        rulebook = json.load(fh)
    from .rulebook_rev import amended_provisions
    provisions = amended_provisions(rulebook["provisions"])
    if not provisions:
        raise ValueError(f"{pack}: rulebook carries no provisions")
    prefix = id_prefix(provisions[0]["id"])
    version = canon_version_for(pack)

    entries: dict[str, CanonEntry] = {}
    for prov in provisions:
        tier, office = tier_of(prov)
        entries[prov["id"]] = CanonEntry(
            id=prov["id"],
            kind="provision",
            tier=tier,
            title=prov.get("title", ""),
            role=ROLE,
            family=prov["family"],
            act_class=prov["family"],
            office=office,
            violate_factors=sorted(prov.get("factors", {}).get("violate", [])),
            gloss=_provision_gloss(tier),
            canon_version=version,
        )

    for suffix, tier, title, reasons, bound, contexts, office in VALUE_TABLE:
        vid = f"{prefix}-{suffix}"
        entries[vid] = CanonEntry(
            id=vid,
            kind="value",
            tier=tier,
            title=title,
            role=ROLE,
            family="VAL",
            act_class=vid,
            office=office,
            violate_factors=[],
            gloss=Gloss(admitted_reasons=list(reasons), bound=dict(bound), contexts=list(contexts)),
            canon_version=version,
        )

    offices = {oid: Office(id=oid, reporting_line=GOVERNANCE_LINE, may_issue_for=[]) for oid in OFFICES}
    for e in entries.values():
        if e.tier == "T1" and e.office:
            offices.setdefault(e.office, Office(id=e.office, reporting_line=GOVERNANCE_LINE, may_issue_for=[]))
            if e.act_class not in offices[e.office].may_issue_for:
                offices[e.office].may_issue_for.append(e.act_class)
    if STANDING_EMERGENCY_CLASS not in offices[OFFICE_COMPLIANCE].may_issue_for:
        offices[OFFICE_COMPLIANCE].may_issue_for.append(STANDING_EMERGENCY_CLASS)
    for o in offices.values():
        o.may_issue_for.sort()

    return Canon(pack=pack, version=version, entries=entries, offices=offices,
                 standing_emergency_classes=[STANDING_EMERGENCY_CLASS],
                 standing_emergency_office=OFFICE_COMPLIANCE)


def engaged(canon: Canon, case_rules: list, value_ids: list) -> list:
    """Module-level alias of `Canon.engaged`."""
    return canon.engaged(case_rules, value_ids)

