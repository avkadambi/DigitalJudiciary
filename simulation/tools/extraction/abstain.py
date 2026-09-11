"""Turning a reading's probabilities into a decision to speak or stay silent.

Three pieces, all standard library, all chosen because encoder confidence
collapses under domain shift (error-detection AUROC 0.92 in-domain to 0.63
out-of-domain on NER; ECE 0.36-0.41) and nothing published measures
calibration for ModernBERT at all:

  * temperature scaling, fitted per corpus (monotone: accuracy untouched);
  * span aggregation, weakest link by default — a span is only as identified
    as its least certain token;
  * a precision-constrained floor, per corpus and per factor, that expires
    with the corpus it was fitted on. Fit for precision at a target, never
    for F1: a missed factor abstains, a hallucinated one binds.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

MIN, MEAN, PRODUCT = "min", "mean", "product"
AGGREGATIONS = (MIN, MEAN, PRODUCT)
DEFAULT_AGGREGATION = MIN


def temperature_scale(logits, temperature: float) -> list:
    if not (temperature > 0.0):
        raise ValueError("temperature must be positive")
    if not logits:
        raise ValueError("no logits")
    z = [v / temperature for v in logits]
    m = max(z)
    e = [math.exp(v - m) for v in z]
    s = sum(e)
    return [v / s for v in e]


def span_confidence(token_probs, aggregation: str = DEFAULT_AGGREGATION) -> float:
    if aggregation not in AGGREGATIONS:
        raise ValueError(f"unknown aggregation {aggregation!r}")
    if not token_probs:
        raise ValueError("a span with no tokens has no confidence")
    for p in token_probs:
        if not (0.0 <= p <= 1.0):
            raise ValueError(f"{p} is not a probability")
    if aggregation == MIN:
        return min(token_probs)
    if aggregation == MEAN:
        return sum(token_probs) / len(token_probs)
    out = 1.0
    for p in token_probs:
        out *= p
    return out


@dataclass(frozen=True)
class Calibration:
    """A fitted decision rule and the corpus it is only valid on."""
    corpus_id: str
    temperature: float
    aggregation: str
    floors: dict            # factor -> floor; "*" is the corpus-wide default when fitted as one
    target_precision: float
    fitted_n: int

    def __post_init__(self):
        if not (self.temperature > 0.0):
            raise ValueError("temperature must be positive")
        if self.aggregation not in AGGREGATIONS:
            raise ValueError(f"unknown aggregation {self.aggregation!r}")
        if not (0.0 < self.target_precision <= 1.0):
            raise ValueError("target_precision must be in (0, 1]")
        for k, v in self.floors.items():
            if not (0.0 < v <= 1.0):
                raise ValueError(f"floor for {k!r} is {v}; a floor of 0 makes abstention unreachable and is refused")

    def floor_for(self, factor: str) -> float:
        if factor in self.floors:
            return self.floors[factor]
        if "*" in self.floors:
            return self.floors["*"]
        raise KeyError(f"no floor calibrated for {factor!r} and no corpus-wide floor; a borrowed threshold is refused")

    def as_dict(self) -> dict:
        return {"corpus_id": self.corpus_id, "temperature": self.temperature, "aggregation": self.aggregation,
                "floors": dict(self.floors), "target_precision": self.target_precision, "fitted_n": self.fitted_n}


def floor_for_precision(scored, target_precision: float) -> tuple:
    """The LOWEST threshold whose precision meets the target: (floor, precision, recall).

    `scored` is (confidence, correct) over held-out assertions. Lowest, not
    best: any higher cut buys precision the constraint did not ask for at the
    cost of coverage. If no cut reaches the target the highest observed
    confidence is returned with its achieved precision and the caller refuses."""
    if not scored:
        raise ValueError("nothing to calibrate on")
    total_correct = sum(1 for _, ok in scored if ok)
    cands = sorted({c for c, _ in scored})
    for t in cands:
        kept = [ok for c, ok in scored if c >= t]
        prec = sum(kept) / len(kept)
        rec = (sum(kept) / total_correct) if total_correct else 0.0
        if prec >= target_precision:
            return t, prec, rec
    t = cands[-1]
    kept = [ok for c, ok in scored if c >= t]
    return t, sum(kept) / len(kept), (sum(kept) / total_correct) if total_correct else 0.0


def fit_temperature(logit_rows, labels, lo: float = 0.05, hi: float = 10.0, iters: int = 60) -> float:
    """Temperature minimising NLL by ternary search (NLL is unimodal in T)."""
    if len(logit_rows) != len(labels) or not logit_rows:
        raise ValueError("nothing to fit on")

    def nll(t):
        s = 0.0
        for row, y in zip(logit_rows, labels):
            s -= math.log(max(temperature_scale(row, t)[y], 1e-12))
        return s / len(labels)
    for _ in range(iters):
        a = lo + (hi - lo) / 3.0
        b = hi - (hi - lo) / 3.0
        if nll(a) < nll(b):
            hi = b
        else:
            lo = a
    return (lo + hi) / 2.0
