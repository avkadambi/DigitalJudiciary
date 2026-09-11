"""Where a reading is produced — and the seam that keeps models out of the packs.

A backend proposes readings with per-token probabilities and takes no
decision. Aggregation, temperature, floor, speak-or-stay-silent all happen in
`abstain.py` and `snapshot.py`, where they are testable without a model.

Four backends, one protocol:

  DeterministicBackend   a seeded fake; exercises the whole pipeline with no weights
  LiteralMatchBackend    the afternoon extractor: the factor's words appear → asserted.
                         Confidently wrong on every guard style, which is the point —
                         it proves the guards have teeth before any model is trained
  CuedLiteralBackend     the same, but a negation / hedge / attribution cue in the
                         sentence collapses the confidence, so the floor turns the
                         reading into an abstention. Model-free and gate-passing;
                         the first honest baseline
  ModernBERTBackend      a fine-tuned multi-label head over the pack's factor
                         vocabulary. torch and transformers are imported lazily
                         inside the call; `import extraction` never touches them
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass

from . import backbones as BB
from .render import sentences, words

NEGATION_CUES = ("does not", "did not", "do not", "not ", "no longer", "without", "never", "removed", "n't")
HEDGE_CUES = ("asserts", "claims", "could not confirm", "unverified", "reportedly", "allegedly", "believed",
              "should", "intends", "plans to", "will ", "to be confirmed")
ATTRIBUTION_CUES = ("previous release", "prior release", "in the cited", "earlier change", "the present change differs",
                    "last quarter", "other team", "sister service")


@dataclass(frozen=True)
class Reading:
    factor: str
    token_probs: tuple
    start: int
    end: int
    text: str


class DeterministicBackend:
    def __init__(self, seed: str = "dj-extract", silent_factors=()):
        self.seed = seed
        self._silent = set(silent_factors)

    def identity(self) -> dict:
        return {"backend": "deterministic", "seed": self.seed, "note": "fixture; no evidence about any document"}

    def _u(self, *parts) -> float:
        h = hashlib.sha256("\x1f".join((self.seed, *parts)).encode()).digest()
        return int.from_bytes(h[:8], "big") / float(1 << 64)

    def score(self, document: str, factors) -> list:
        out = []
        for f in factors:
            if f in self._silent:
                continue
            u = self._u(document, f)
            n = 1 + int(self._u(document, f, "n") * 3)
            probs = tuple(min(0.999, max(0.001, u + 0.05 * i)) for i in range(n))
            out.append(Reading(f, probs, 0, min(len(document), 12), document[:12]))
        return out


def _find(document: str, factor: str):
    pat = re.escape(words(factor)).replace(r"\ ", r"\s+")
    return re.search(pat, document, re.IGNORECASE)


class LiteralMatchBackend:
    """Label proximity is all it knows; it cannot represent negation, hedging or attribution."""

    def __init__(self, confidence: float = 0.95):
        self.confidence = confidence

    def identity(self) -> dict:
        return {"backend": "literal_match", "confidence": self.confidence,
                "note": "keys on the factor's words alone; asserts on every guard style"}

    def score(self, document: str, factors) -> list:
        out = []
        for f in factors:
            m = _find(document, f)
            if not m:
                continue
            out.append(Reading(f, (self.confidence,), m.start(), m.end(), m.group(0)))
        return out


class CuedLiteralBackend(LiteralMatchBackend):
    """Literal match with a sentence-level cue check. A cue does not delete the
    reading — it lowers the per-token probability so that the FLOOR decides,
    which keeps the decision in the calibrated part of the pipeline."""

    def __init__(self, confidence: float = 0.95, cued_confidence: float = 0.30):
        super().__init__(confidence)
        self.cued_confidence = cued_confidence

    def identity(self) -> dict:
        return {"backend": "cued_literal", "confidence": self.confidence, "cued_confidence": self.cued_confidence,
                "note": "literal match; negation/hedge/attribution cues in the sentence, or a longer sibling factor matched at the same place, collapse the confidence"}

    def score(self, document: str, factors) -> list:
        sents = sentences(document)
        found = {}
        for f in factors:
            m = _find(document, f)
            if m:
                found[f] = m
        out = []
        for f, m in found.items():
            sent = next((t for s, e, t in sents if s <= m.start() < e), document[m.start():m.end()])
            low = sent.lower()
            cued = any(c in low for c in NEGATION_CUES + HEDGE_CUES + ATTRIBUTION_CUES)
            # A sibling factor whose words CONTAIN this factor's words, matched at
            # the same place, makes the reading ambiguous: "remediation action
            # reversible" inside "remediation action reversible within window" is
            # evidence for the longer factor, not the shorter. Ambiguity lowers the
            # confidence and lets the floor abstain; it does not pick a winner.
            shadowed = any(g != f and n.start() <= m.start() and n.end() >= m.end() and (n.end() - n.start()) > (m.end() - m.start())
                           for g, n in found.items())
            conf = self.cued_confidence if (cued or shadowed) else self.confidence
            out.append(Reading(f, (conf,), m.start(), m.end(), m.group(0)))
        return out


class ModernBERTBackend:
    """A fine-tuned multi-label sequence classifier over the factor vocabulary.

    `checkpoint` is the fine-tuned head (see train_modernbert.py); the backbone
    is what it was adapted from and is recorded, revision and all, in the
    provenance. Extraction against a bare backbone is not a supported mode: a
    pretrained encoder has no factor labels.

    The per-factor probability is exposed as a one-token span so the same
    aggregation and floor apply. Character spans are the sentence with the
    highest attribution when `--explain` is on; otherwise the whole document.
    """

    def __init__(self, checkpoint: str, backbone_name: str = BB.DEFAULT_BACKBONE, device=None, max_length=None):
        self.backbone = BB.get(backbone_name)
        BB.require_pinned(self.backbone)
        self.checkpoint = checkpoint
        self.device = device
        self.max_length = max_length or min(self.backbone.context, 2048)
        self._tok = self._model = None

    def _load(self):
        if self._model is not None:
            return
        try:
            import torch  # noqa: F401
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
        except ImportError as e:
            raise RuntimeError("extraction with a model needs torch and transformers in a SEPARATE environment "
                               "(tools/extraction/requirements-model.txt); the packs never carry them") from e
        self._tok = AutoTokenizer.from_pretrained(self.checkpoint, add_prefix_space=self.backbone.add_prefix_space)
        self._model = AutoModelForSequenceClassification.from_pretrained(self.checkpoint)
        self._model.eval()
        if self.device:
            self._model.to(self.device)

    def identity(self) -> dict:
        return {"backend": "modernbert", "backbone": self.backbone.name, "backbone_repo": self.backbone.repo,
                "backbone_revision": self.backbone.revision, "checkpoint": self.checkpoint,
                "add_prefix_space": self.backbone.add_prefix_space, "max_length": self.max_length}

    def score(self, document: str, factors) -> list:  # pragma: no cover — needs weights
        import torch
        self._load()
        enc = self._tok(document, return_tensors="pt", truncation=True, max_length=self.max_length)
        if self.device:
            enc = {k: v.to(self.device) for k, v in enc.items()}
        with torch.no_grad():
            logits = self._model(**enc).logits[0]
        probs = torch.sigmoid(logits).tolist()
        label2id = self._model.config.label2id
        out = []
        for f in factors:
            if f not in label2id:
                continue
            p = float(probs[label2id[f]])
            # A probability below one half is a reading that the document does NOT
            # carry the factor: proposing nothing is how ABSENT is expressed.
            if p < 0.5:
                continue
            m = _find(document, f)
            s, e = (m.start(), m.end()) if m else (0, len(document))
            out.append(Reading(f, (p,), s, e, document[s:e]))
        return out


class NLIZeroShotBackend:
    """Facts without training: a ready NLI head reads each factor as a hypothesis.

    premise    = the change description
    hypothesis = "This change ensures <factor words>."
    reading    = P(entailment), exposed as a one-token span so the same
                 aggregation, temperature and floor apply

    Why this is the first model backend to run, before any fine-tuned head:
    it needs no labelled rows and no GPU of note, it handles negation and
    hedging natively (a negated sentence contradicts the hypothesis rather
    than entailing it), and it is exactly the baseline a fine-tuned head has
    to beat on the held-out styles. Its weakness is also known in advance —
    an NLI head reads "the author asserts X" as weak entailment — and the
    guard styles will price it. Default backbone: modernbert-large-zeroshot-v2.0
    (Apache-2.0); `deberta-v3-large-zeroshot-v2.0` is the stronger, slower
    alternative and can be named with `--checkpoint`.

    Below `absent_below` the reading is dropped altogether (ABSENT): a factor
    the description contradicts or never mentions proposes nothing.
    """

    def __init__(self, checkpoint: str | None = None, backbone_name: str = "modernbert-large-zeroshot-v2.0",
                 device=None, absent_below: float = 0.05, template: str = "This change ensures {w}."):
        self.backbone = BB.get(backbone_name)
        BB.require_pinned(self.backbone)
        self.checkpoint = checkpoint or self.backbone.repo
        self.revision = None if checkpoint else self.backbone.revision
        self.device = device
        self.absent_below = absent_below
        self.template = template
        self._tok = self._model = self._ent = None

    def identity(self) -> dict:
        return {"backend": "nli_zeroshot", "backbone": self.backbone.name, "checkpoint": self.checkpoint,
                "revision": self.revision, "template": self.template, "absent_below": self.absent_below,
                "note": "no training; P(entailment) of a per-factor hypothesis"}

    def _load(self):  # pragma: no cover — needs weights
        if self._model is not None:
            return
        try:
            import torch  # noqa: F401
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
        except ImportError as e:
            raise RuntimeError("NLI extraction needs torch and transformers in a separate environment") from e
        kw = {"revision": self.revision} if self.revision else {}
        self._tok = AutoTokenizer.from_pretrained(self.checkpoint, **kw)
        self._model = AutoModelForSequenceClassification.from_pretrained(self.checkpoint, **kw)
        self._model.eval()
        if self.device:
            self._model.to(self.device)
        labels = {v.lower(): k for k, v in self._model.config.id2label.items()}
        self._ent = next(i for name, i in labels.items() if name.startswith("entail"))

    def entailment(self, premise: str, hypothesis: str) -> float:  # pragma: no cover
        import torch
        self._load()
        enc = self._tok(premise, hypothesis, return_tensors="pt", truncation=True, max_length=2048)
        if self.device:
            enc = {k: v.to(self.device) for k, v in enc.items()}
        with torch.no_grad():
            pr = torch.softmax(self._model(**enc).logits[0], dim=-1)
        return float(pr[self._ent])

    def score(self, document: str, factors) -> list:  # pragma: no cover
        out = []
        for f in factors:
            p = self.entailment(document, self.template.format(w=words(f)))
            if p < self.absent_below:
                continue
            m = _find(document, f)
            s, e = (m.start(), m.end()) if m else (0, len(document))
            out.append(Reading(f, (p,), s, e, document[s:e]))
        return out


class GLiNER2MagnitudeBackend:
    """Number-plus-unit spans for declared dimensions, via GLiNER2's schema extraction.

    For each dimension the schema asks for one field — the dimension's words as
    the entity description — and the returned span is normalised with the same
    number/unit regex the cued reader uses, so a reading is a float and a unit
    or it is nothing. The span score is the confidence; below the floor the
    dimension is ABSTAINED and the engine reads it as unrecorded. Needs the
    `gliner2` package (Apache-2.0, CPU-deployable, 205M parameters).
    """

    def __init__(self, backbone_name: str = "gliner2-base-v1", threshold: float = 0.3):
        self.backbone = BB.get(backbone_name)
        BB.require_pinned(self.backbone)
        self.threshold = threshold
        self._model = None

    def identity(self) -> dict:
        return {"backend": "gliner2_magnitude", "backbone": self.backbone.name,
                "revision": self.backbone.revision, "threshold": self.threshold}

    def _load(self):  # pragma: no cover
        if self._model is None:
            try:
                from gliner2 import GLiNER2
            except ImportError as e:
                raise RuntimeError("magnitude extraction with GLiNER2 needs `pip install gliner2` in the model "
                                   "environment; the packs never carry it") from e
            self._model = GLiNER2.from_pretrained(self.backbone.repo, revision=self.backbone.revision)

    def values(self, document: str, dimensions) -> dict:  # pragma: no cover
        """factor -> (value, unit, confidence) for the dimensions the document states."""
        from .records import NUMBER_UNIT
        self._load()
        labels = {words(d): f"the stated value of {words(d)}, a number with its unit" for d in dimensions}
        result = self._model.extract_entities(document, list(labels), include_confidence=True,
                                              threshold=self.threshold)
        out = {}
        for d in dimensions:
            for ent in result.get("entities", {}).get(words(d), []) or []:
                text = ent["text"] if isinstance(ent, dict) else str(ent)
                conf = float(ent.get("confidence", self.threshold)) if isinstance(ent, dict) else self.threshold
                m = NUMBER_UNIT.search(text)
                if m:
                    out[d] = (float(m.group(1)), (m.group(2) or "").lower(), conf)
                    break
        return out
