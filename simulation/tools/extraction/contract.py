"""What an extractor is allowed to hand the engine.

Three statuses, and the distinction between the last two is the point. OBSERVED
puts the factor in `facts`. ABSTAINED puts it in `unrecorded`, where the engine
reads it as silence -- a premise nobody established, which never binds. ABSENT
leaves it out. ABSTAINED and ABSENT are kept apart in the provenance because
they are different facts about the world: "the model could not read this" is a
defect in the instrument; "the description does not mention it" is a property
of the description. Collapsing them makes the extractor's own miss rate
unmeasurable against true absences.

CARRIED is the fourth status and is not an extraction result at all: a fact
outside the engaged provisions' vocabulary (context markers, engineered
markers) passes through verbatim, and the provenance says so.
"""
from __future__ import annotations

from dataclasses import dataclass, field

OBSERVED = "observed"
ABSTAINED = "abstained"
ABSENT = "absent"
CARRIED = "carried"
STATUSES = (OBSERVED, ABSTAINED, ABSENT, CARRIED)
SILENT = frozenset({ABSTAINED, ABSENT})


@dataclass(frozen=True)
class Span:
    start: int
    end: int
    text: str


@dataclass(frozen=True)
class FieldValue:
    name: str
    status: str
    confidence: float | None = None
    span: Span | None = None
    floor: float | None = None

    def __post_init__(self):
        if self.status not in STATUSES:
            raise ValueError(f"unknown status {self.status!r}")
        if self.status == ABSENT and self.confidence is not None:
            raise ValueError(f"{self.name}: an absent factor carries no reading")


@dataclass(frozen=True)
class ExtractedCase:
    case_id: str
    fields: tuple
    provenance: dict = field(default_factory=dict)

    def __post_init__(self):
        names = [f.name for f in self.fields]
        if len(names) != len(set(names)):
            raise ValueError(f"{self.case_id}: repeated factors")

    def facts(self) -> list:
        return sorted(f.name for f in self.fields if f.status in (OBSERVED, CARRIED))

    def unrecorded(self) -> list:
        return sorted(f.name for f in self.fields if f.status == ABSTAINED)

    def to_case_patch(self) -> dict:
        """The two case fields the engine reads (5.11.0 three-valued facts)."""
        return {"facts": self.facts(), "unrecorded": self.unrecorded(), "facts_source": "extracted"}

    def audit(self) -> dict:
        return {"case": self.case_id, "provenance": dict(self.provenance),
                "fields": [{"name": f.name, "status": f.status,
                            "confidence": None if f.confidence is None else round(f.confidence, 6),
                            "floor": f.floor, "span": None if f.span is None else [f.span.start, f.span.end]}
                           for f in self.fields]}


def coverage(records: list) -> dict:
    """Per-status counts across a corpus. The number to watch is ABSTAINED: a
    vocabulary that abstains on most of the corpus cannot carry a precedent."""
    out: dict = {s: 0 for s in STATUSES}
    for r in records:
        for f in r.fields:
            out[f.status] += 1
    return out
