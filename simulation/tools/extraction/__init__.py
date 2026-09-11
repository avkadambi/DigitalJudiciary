"""Offline characterisation: prose in, three-valued facts out.

The Digital Judiciary corpora precompile `facts(c)`; the Evaluator is modelled
at epsilon = 1.00 and nothing is scored on turning a messy change into factors.
This package is that stage, and it is kept OUT of the packs: the packs promise
a standard-library runtime, and a model backend imports torch lazily and only
here. What crosses the seam is a facts snapshot in which every factor of an
engaged provision carries one of three statuses --

    observed    the document states it and the extractor is above its floor
    abstained   the extractor read something and was not confident enough
    absent      the document does not speak to it

-- and the engine reads `abstained` as UNRECORDED (Case.unrecorded), which
under a rule of precedence outranks distinguishing and never binds.

The design is the extraction package of Likewise 0.15.0 (same author),
re-implemented for boolean factors and pull-request prose: closed backbone set
with pinned revisions, temperature scaling per corpus, weakest-link span
aggregation, a precision-constrained floor, and a round-trip harness that
scores the extractor against ground truth the corpus already carries.
"""
from .contract import ABSENT, ABSTAINED, CARRIED, OBSERVED, SILENT, ExtractedCase, FieldValue
from .abstain import Calibration, fit_temperature, floor_for_precision, span_confidence, temperature_scale
from .backbones import BACKBONES, DEFAULT_BACKBONE, Backbone
from .backends import CuedLiteralBackend, DeterministicBackend, LiteralMatchBackend, ModernBERTBackend, Reading
from . import render, roundtrip, snapshot

__all__ = ["ABSENT", "ABSTAINED", "CARRIED", "OBSERVED", "SILENT", "ExtractedCase", "FieldValue",
           "Calibration", "fit_temperature", "floor_for_precision", "span_confidence", "temperature_scale",
           "BACKBONES", "DEFAULT_BACKBONE", "Backbone", "CuedLiteralBackend", "DeterministicBackend",
           "LiteralMatchBackend", "ModernBERTBackend", "Reading", "render", "roundtrip", "snapshot"]
