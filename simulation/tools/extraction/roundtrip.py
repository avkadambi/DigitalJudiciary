"""Score an extractor against ground truth the corpus already carries.

Assertion precision, not F1 and not accuracy: correct assertions over all
assertions. A silence is not a wrong answer here; F1 would average the
expensive error (a hallucinated factor, which can bind) against the cheap
one (a miss, which abstains). The undefined case is preserved: zero
assertions is `None`, never 1.0. A guard assertion fails at any n.

Seven verdicts, because three extractor statuses against two truth states do
not collapse into right and wrong.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field

from .contract import ABSENT, ABSTAINED, OBSERVED

CORRECT = "correct"                  # asserted, and the case carries the factor
HALLUCINATED = "hallucinated"        # asserted a factor the case does not carry (guard or unmentioned)
MISSED = "missed"                    # the case carries it; the extractor abstained
NOT_RENDERED = "not_rendered"        # the case carries it; the extractor saw nothing
CORRECT_SILENCE = "correct_silence"  # not carried, extractor absent
CAUTIOUS = "cautious"                # not carried, extractor abstained (a guard, read and refused)
VERDICTS = (CORRECT, HALLUCINATED, MISSED, NOT_RENDERED, CORRECT_SILENCE, CAUTIOUS)
ASSERTIONS = frozenset({CORRECT, HALLUCINATED})
SILENCES = frozenset({MISSED, NOT_RENDERED, CORRECT_SILENCE, CAUTIOUS})

UPPER_BOUND_CAVEAT = ("Round-trip figures are an UPPER BOUND, not an estimate. The renderer and the extractor "
                      "share a vocabulary; a real change description was written by someone who never saw the "
                      "renderer. Do not report these numbers as extraction accuracy on real records.")


def verdict_for(status: str, truth) -> str:
    if status == OBSERVED:
        return CORRECT if truth else HALLUCINATED
    if status == ABSTAINED:
        return MISSED if truth else CAUTIOUS
    if status == ABSENT:
        return NOT_RENDERED if truth else CORRECT_SILENCE
    raise ValueError(status)


@dataclass(frozen=True)
class Scored:
    case_id: str
    style: str
    guard: bool          # this factor was written in a guard style
    factor: str
    verdict: str
    confidence: float | None
    floor: float | None


def score(extracted, rendering) -> list:
    out = []
    guards = set(rendering.guards)
    for f in extracted.fields:
        if f.name not in rendering.truth:
            continue
        out.append(Scored(extracted.case_id, rendering.style, f.name in guards, f.name,
                          verdict_for(f.status, rendering.truth[f.name]), f.confidence, f.floor))
    return out


@dataclass
class Report:
    n_cases: int = 0
    n_decisions: int = 0
    by_verdict: dict = field(default_factory=lambda: dict.fromkeys(VERDICTS, 0))
    by_style: dict = field(default_factory=dict)
    guard_assertions: list = field(default_factory=list)
    styles_seen: set = field(default_factory=set)
    gate: dict = field(default_factory=dict)

    @property
    def assertions(self) -> int:
        return sum(self.by_verdict[v] for v in ASSERTIONS)

    @property
    def assertion_precision(self):
        n = self.assertions
        return None if n == 0 else self.by_verdict[CORRECT] / n

    @property
    def recall(self):
        carried = self.by_verdict[CORRECT] + self.by_verdict[MISSED] + self.by_verdict[NOT_RENDERED]
        return None if carried == 0 else self.by_verdict[CORRECT] / carried

    def as_dict(self) -> dict:
        return {"n_cases": self.n_cases, "n_decisions": self.n_decisions, "assertions": self.assertions,
                "assertion_precision": None if self.assertion_precision is None else round(self.assertion_precision, 6),
                "recall_of_carried_factors": None if self.recall is None else round(self.recall, 6),
                "by_verdict": dict(self.by_verdict),
                "by_style": {k: dict(v) for k, v in sorted(self.by_style.items())},
                "guard_assertions": len(self.guard_assertions), "guard_examples": self.guard_assertions[:5],
                "styles_evaluated": sorted(self.styles_seen), "gate": self.gate, "caveat": UPPER_BOUND_CAVEAT}


def report(scored, *, train_styles=(), min_assertions: int = 300, target_precision: float = 0.98) -> Report:
    r = Report()
    keys = set()
    for s in scored:
        keys.add(s.case_id)
        r.n_decisions += 1
        r.by_verdict[s.verdict] += 1
        r.by_style.setdefault(s.style, dict.fromkeys(VERDICTS, 0))[s.verdict] += 1
        r.styles_seen.add(s.style)
        if s.guard and s.verdict in ASSERTIONS:
            r.guard_assertions.append({"case": s.case_id, "factor": s.factor, "style": s.style,
                                       "confidence": s.confidence, "floor": s.floor})
    r.n_cases = len(keys)
    leak = sorted(r.styles_seen & set(train_styles))
    prec = r.assertion_precision
    if leak:
        verdict, why = "invalid", f"styles {leak} appear in both training and evaluation; this measures memorisation"
    elif r.guard_assertions:
        verdict, why = "fail", (f"{len(r.guard_assertions)} guard assertion(s). A guard is a factor written so that "
                                "the only correct behaviour is silence; one is a failure at any n.")
    elif r.assertions < min_assertions:
        verdict, why = "inconclusive", (f"{r.assertions} assertions against a floor of {min_assertions}; perfect "
                                        "precision is satisfiable by never speaking")
    elif prec is not None and prec >= target_precision:
        verdict, why = "pass", f"assertion precision {prec:.4f} >= {target_precision}"
    else:
        verdict, why = "fail", f"assertion precision {prec if prec is None else round(prec, 4)} < {target_precision}"
    r.gate = {"verdict": verdict, "why": why, "min_assertions": min_assertions, "target_precision": target_precision,
              "train_styles": sorted(train_styles), "style_leak": leak}
    return r


def readings(scored) -> list:
    """Labelled assertions for `floor_for_precision`. Silences are not fed to the
    fitter: a silence is the absence of a reading, and counting it as a negative
    would push the floor DOWN."""
    return [{"factor": s.factor, "confidence": s.confidence, "correct": s.verdict == CORRECT,
             "guard": s.guard, "style": s.style, "case": s.case_id}
            for s in scored if s.verdict in ASSERTIONS and s.confidence is not None]


def write_readings(scored, path: str) -> int:
    rows = readings(scored)
    with open(path, "w") as fh:
        for row in rows:
            fh.write(json.dumps(row) + "\n")
    return len(rows)
