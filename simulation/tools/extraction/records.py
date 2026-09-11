"""Record construction as its own stage — premise, citation stance, scope, magnitude.

`facts(c)` is what a case brings in. A RECORD is what the judiciary writes out
when a contested case resolves, and four of its fields decide what binds
later: the premise (which facts the holding turned on), the citations and the
stance of each (was the earlier record followed, distinguished or superseded),
the scope (how wide the holding reaches), and, once dimensions exist, the
magnitudes. In the corpora those fields come from the generator; in a real
judiciary they come from the rationale a judge wrote. This module renders a
rationale from known fields, reads it back, and measures what the reading
does to the store — the same discipline as facts extraction, with one
inversion that matters:

    facts      when unsure, STAY SILENT   — a hallucinated fact can bind
    premise    when unsure, INCLUDE       — an omitted premise factor over-binds
    stance     when unsure, UNSTATED      — an unstated citation never displaces
    scope      when unsure, WIDEST        — a wide record loses the scope key
    magnitude  when unsure, UNRECORDED    — an unrecorded magnitude never binds

Each default is the one whose failure costs a reviewer a case rather than
compelling a disposition the record does not support.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from .render import GUARD_STYLES, STYLES, sentences, words

STANCES = ("superseded", "followed", "distinguished")
SCOPE_PHRASES = {
    1: ("confined to this repository and no other", "for this site only"),
    2: ("for this team's services", "within the filing team's services"),
    3: ("across this product line", "for the division's practice generally"),
    4: ("across every division of the enterprise", "enterprise-wide"),
    5: ("in every context, including third-party integrations", "without limitation of context"),
}
WIDEST = max(SCOPE_PHRASES)

IMMATERIAL_CUES = ("immaterial", "did not rest on", "played no part", "regardless of", "irrespective of",
                   "not relied on", "noted but not decisive", "without weight")
STANCE_CUES = {
    "superseded": ("supersedes", "superseded", "displaces", "overrules", "no longer good law", "is departed from"),
    "followed": ("follows", "followed", "applied", "in line with", "consistent with", "as held in"),
    "distinguished": ("distinguishes", "distinguished", "does not govern", "turned on a different premise",
                      "is not on point", "differs on"),
}
NUMBER_UNIT = re.compile(r"(-?\d+(?:\.\d+)?)\s*(%|percent|days?|hours?|minutes?|ms|seconds?|mg/kg|mg|kg|gb|mb|x)?",
                         re.IGNORECASE)


def _h(*parts) -> int:
    return int(hashlib.sha256("\x1f".join(str(p) for p in parts).encode()).hexdigest(), 16)


@dataclass(frozen=True)
class RecordTruth:
    case_id: str
    premise: tuple          # factors the holding turned on
    immaterial: tuple       # present facts written as immaterial (premise guards)
    cites: dict             # cited record id -> stance
    scope_width: int
    values: dict            # factor -> magnitude, when the overlay declares one


@dataclass(frozen=True)
class RationaleRendering:
    case_id: str
    prose: str
    truth: RecordTruth
    style: str
    guard: bool


def _w(f: str) -> str:
    """Words for a factor; opaque markers are named as such so a reader can find them."""
    return words(f) if not f.startswith(("ctx_", "mk_", "forged_")) else f"context marker {f}"


def _premise_phrase(style: str, w: str) -> str:
    if style == "plain":
        return f"The holding turned on the fact that {w}."
    if style == "formal":
        return f"The instance found {w} and treated it as decisive."
    if style == "narrative":
        return f"What decided the matter was that {w}."
    if style == "tabular":
        return f"- decisive: {w}"
    return f"{w} — decisive."


def _immaterial_phrase(style: str, w: str) -> str:
    h = _h(w, style) % 4
    return [f"It was noted that {w}, but the holding did not rest on it.",
            f"{w} was present and immaterial to the outcome.",
            f"The instance reached its holding regardless of {w}.",
            f"- noted but not decisive: {w}"][h]


def _cite_phrase(style: str, rid: str, stance: str) -> str:
    h = _h(rid, style, stance) % 2
    if stance == "superseded":
        return [f"This holding supersedes {rid}, which is departed from.",
                f"{rid} is no longer good law on this premise; the present holding displaces it."][h]
    if stance == "followed":
        return [f"The instance follows {rid} and applies its reading.",
                f"As held in {rid}, and consistent with it, the same reading is applied."][h]
    return [f"{rid} is distinguished: it turned on a different premise and does not govern here.",
            f"The instance distinguishes {rid}, which is not on point."][h]


def _scope_phrase(style: str, width: int) -> str:
    ph = SCOPE_PHRASES[width][_h(width, style) % 2]
    return f"The holding applies {ph}."


# --- held-out phrasings: none of these strings appear in any reader's cue list.
# They exist to show what the safe defaults do when the reader does not
# understand the sentence: an immaterial fact it cannot recognise is INCLUDED
# (the record narrows — cheap), a stance it cannot read is UNSTATED (no
# displacement — cheap), a scope it cannot read is WIDEST (loses the scope key
# — cheap). A reader trained on the cue phrasings and evaluated here measures
# generalisation, which is what a fine-tuned head is for.
NOVEL_IMMATERIAL = ("The panel set no store by {w}.", "{w} was recorded without bearing on the result.",
                    "Nothing in the outcome depends on {w}.")
NOVEL_CITE = {"superseded": ("{rid} gives way to the present ruling.", "The reading in {rid} is abandoned here."),
              "followed": ("The panel adheres to {rid}.", "{rid} settles the question and is adopted."),
              "distinguished": ("{rid} stands on other facts and is left untouched.", "{rid} answers a different question.")}
NOVEL_SCOPE = {1: "This ruling reaches this repository alone.", 2: "This ruling reaches the filing team's own services.",
               3: "This ruling reaches the whole product line.", 4: "This ruling reaches every division.",
               5: "This ruling reaches everything, third parties included."}


def render_rationale(case: dict, style: str, *, stance_for: dict | None = None, scope_width: int | None = None,
                     values: dict | None = None, n_immaterial: int = 2,
                     premise_override: list | None = None, novel: bool = False) -> RationaleRendering:
    """Write the rationale a judge would have written, from fields known by construction.

    Guards, by field: premise — present facts stated as immaterial (must NOT be
    read into the premise); stance — a followed or distinguished citation (must
    NOT be read as superseded); scope — none needed, abstention is the widest.
    """
    if style not in STYLES + GUARD_STYLES:
        raise ValueError(style)
    body_style = style if style in STYLES else "plain"
    extra = case.get("engine") or {}
    premise = sorted(premise_override if premise_override is not None else (extra.get("premise") or case["facts"]))
    others = sorted(f for f in case["facts"] if f not in set(premise))
    imm = others[:0]
    if others and n_immaterial:
        h = _h(case["id"], "imm")
        imm = sorted({others[(h + i * 7919) % len(others)] for i in range(min(n_immaterial, len(others)))})
    cites = {}
    for rid in extra.get("cites") or []:
        cites[rid] = (stance_for or {}).get(rid, "superseded")
    width = scope_width if scope_width is not None else int(extra.get("scope_width", 3))
    vals = dict(values or {})
    lines = [f"Ruling on {case['id']} — {(case.get('scenario') or {}).get('change', 'the change')}.", ""]
    body = []
    for f in premise:
        w = _w(f)
        if f in vals:
            body.append((f, _premise_phrase(body_style, f"{w} stood at {vals[f]:g}")))
        else:
            body.append((f, _premise_phrase(body_style, w)))
    for f in imm:
        if novel:
            body.append((f, NOVEL_IMMATERIAL[_h(f, style) % 3].format(w=_w(f))))
        else:
            body.append((f, _immaterial_phrase(body_style, _w(f))))
    for rid, st in cites.items():
        if novel:
            body.append((rid, NOVEL_CITE[st][_h(rid, style) % 2].format(rid=rid)))
        else:
            body.append((rid, _cite_phrase(body_style, rid, st)))
    body.sort(key=lambda x: _h(x[0], case["id"], style))
    lines += [p for _, p in body]
    lines.append(NOVEL_SCOPE[width] if novel else _scope_phrase(body_style, width))
    truth = RecordTruth(case["id"], tuple(premise), tuple(imm), cites, width,
                        {f: v for f, v in vals.items() if f in set(premise)})
    return RationaleRendering(case["id"], "\n".join(lines), truth, style,
                              guard=bool(imm) or any(s != "superseded" for s in cites.values()))


# ---------------------------------------------------------------------------
# Readers: rationale prose -> the four fields, each with its safe default
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class RecordReading:
    case_id: str
    premise: tuple                 # included factors
    premise_confidence: dict       # factor -> confidence that it was decisive
    cite_stance: dict              # rid -> stance | "unstated"
    stance_confidence: dict
    scope_width: int
    scope_confidence: float
    values: dict                   # factor -> float
    abstained_values: tuple
    provenance: dict = field(default_factory=dict)


def _sentence_of(prose: str, m) -> str:
    for s, e, t in sentences(prose):
        if s <= m.start() < e:
            return t
    return prose[m.start():m.end()]


class LiteralRecordReader:
    """Every factor mentioned is decisive; every citation supersedes; the first
    scope phrase wins. The reader somebody writes in an afternoon; wrong in
    exactly the ways the guards catch."""

    name = "literal"

    def identity(self) -> dict:
        return {"reader": "literal", "note": "mention = premise; cite = superseded; no abstention"}

    def read(self, prose: str, case: dict, candidates: list, cite_ids: list, magnitude_factors: list) -> RecordReading:
        premise, conf = [], {}
        for f in candidates:
            w = _w(f)
            if re.search(re.escape(w).replace(r"\ ", r"\s+"), prose, re.IGNORECASE):
                premise.append(f)
                conf[f] = 0.95
        stance = {rid: "superseded" for rid in cite_ids if rid in prose}
        width = None
        for wdt, phrases in SCOPE_PHRASES.items():
            if any(p in prose for p in phrases):
                width = wdt
                break
        vals, abst = {}, []
        for f in magnitude_factors:
            m = re.search(re.escape(words(f)) + r"\s+stood at\s+" + NUMBER_UNIT.pattern, prose, re.IGNORECASE)
            if m:
                vals[f] = float(m.group(1))
        return RecordReading(case["id"], tuple(sorted(premise)), conf, stance,
                             {rid: 0.95 for rid in stance}, width if width is not None else WIDEST,
                             0.95 if width is not None else 0.0, vals, tuple(abst), self.identity())


class CuedRecordReader(LiteralRecordReader):
    """Reads the cues, and applies the safe default on each field when it cannot.

    premise:  a mention inside an immaterial cue sentence is excluded with
              confidence; an ambiguous mention (both a decisive and an
              immaterial cue) is INCLUDED — inclusion is the safe failure;
    stance:   the cue family in the citing sentence; two families or none →
              'unstated', which never displaces;
    scope:    a scope phrase or, absent one, the WIDEST width;
    values:   a number after the factor's words, or unrecorded.
    """

    name = "cued"

    def __init__(self, floor: float = 0.9):
        self.floor = floor

    def identity(self) -> dict:
        return {"reader": "cued", "floor": self.floor,
                "note": "cue-driven; premise inclusion-biased, stance unstated on doubt, scope widest on doubt"}

    def read(self, prose: str, case: dict, candidates: list, cite_ids: list, magnitude_factors: list) -> RecordReading:
        premise, conf = [], {}
        for f in candidates:
            w = _w(f)
            m = re.search(re.escape(w).replace(r"\ ", r"\s+"), prose, re.IGNORECASE)
            if not m:
                continue
            sent = _sentence_of(prose, m).lower()
            immaterial = any(c in sent for c in IMMATERIAL_CUES)
            decisive = any(c in sent for c in ("- decisive:", "turned on", "decided the matter", "treated it as decisive",
                                               "— decisive"))
            if immaterial and not decisive:
                conf[f] = 0.1                 # confidently not decisive
                continue
            # decisive, or ambiguous: include. Ambiguity lowers the confidence
            # but does not exclude — the inverted floor.
            conf[f] = 0.95 if decisive and not immaterial else 0.5
            premise.append(f)
        stance, sconf = {}, {}
        for rid in cite_ids:
            m = re.search(re.escape(rid), prose)
            if not m:
                continue
            sent = _sentence_of(prose, m).lower()
            hits = [st for st, cues in STANCE_CUES.items() if any(c in sent for c in cues)]
            if len(hits) == 1:
                stance[rid], sconf[rid] = hits[0], 0.95
            else:
                stance[rid], sconf[rid] = "unstated", 0.3
        width, wconf = WIDEST, 0.0
        for wdt, phrases in SCOPE_PHRASES.items():
            if any(p in prose for p in phrases):
                width, wconf = wdt, 0.95
                break
        vals, abst = {}, []
        for f in magnitude_factors:
            m = re.search(re.escape(words(f)) + r"\s+stood at\s+" + NUMBER_UNIT.pattern, prose, re.IGNORECASE)
            if m:
                vals[f] = float(m.group(1))
            elif re.search(re.escape(words(f)), prose, re.IGNORECASE):
                abst.append(f)
        return RecordReading(case["id"], tuple(sorted(premise)), conf, stance, sconf, width, wconf, vals,
                             tuple(abst), self.identity())


class ModernBERTRecordReader:
    """Three fine-tuned heads over the rationale (see train_modernbert.py --task):
    premise (multi-label over the case's facts; decision threshold set for
    RECALL, not precision), stance (3-way over the citing sentence; below the
    floor → unstated) and scope (5-way ordinal; below the floor → widest).
    Magnitudes use the same regex normaliser after a token-classification span
    head. torch is imported lazily; the packs never see it."""

    name = "modernbert"

    def __init__(self, premise_ckpt: str, stance_ckpt: str | None = None, scope_ckpt: str | None = None,
                 backbone_name: str = "modernbert-large", premise_recall_threshold: float = 0.2,
                 floor: float = 0.9):
        from . import backbones as BB
        self.backbone = BB.get(backbone_name)
        BB.require_pinned(self.backbone)
        self.ckpts = {"premise": premise_ckpt, "stance": stance_ckpt, "scope": scope_ckpt}
        self.premise_recall_threshold = premise_recall_threshold
        self.floor = floor
        self._models = {}

    def identity(self) -> dict:
        return {"reader": "modernbert", "backbone": self.backbone.name, "backbone_revision": self.backbone.revision,
                "checkpoints": dict(self.ckpts), "premise_recall_threshold": self.premise_recall_threshold,
                "floor": self.floor}

    def _load(self, task):  # pragma: no cover — needs weights
        if task in self._models:
            return self._models[task]
        from transformers import AutoModelForSequenceClassification, AutoTokenizer
        ck = self.ckpts[task]
        if not ck:
            return None
        tok = AutoTokenizer.from_pretrained(ck, add_prefix_space=self.backbone.add_prefix_space)
        model = AutoModelForSequenceClassification.from_pretrained(ck)
        model.eval()
        self._models[task] = (tok, model)
        return self._models[task]

    def read(self, prose, case, candidates, cite_ids, magnitude_factors):  # pragma: no cover
        import torch
        fallback = CuedRecordReader(self.floor)
        base = fallback.read(prose, case, candidates, cite_ids, magnitude_factors)
        premise, pconf = list(base.premise), dict(base.premise_confidence)
        pm = self._load("premise")
        if pm:
            tok, model = pm
            enc = tok(prose, return_tensors="pt", truncation=True, max_length=2048)
            with torch.no_grad():
                probs = torch.sigmoid(model(**enc).logits[0]).tolist()
            l2i = model.config.label2id
            premise, pconf = [], {}
            for f in candidates:
                if f in l2i:
                    p = float(probs[l2i[f]])
                    pconf[f] = p
                    # inclusion-biased: a LOW threshold, because omission over-binds
                    if p >= self.premise_recall_threshold:
                        premise.append(f)
        stance, sconf = dict(base.cite_stance), dict(base.stance_confidence)
        sm = self._load("stance")
        if sm:
            tok, model = sm
            for rid in cite_ids:
                m = re.search(re.escape(rid), prose)
                if not m:
                    continue
                sent = _sentence_of(prose, m)
                enc = tok(sent, return_tensors="pt", truncation=True, max_length=256)
                with torch.no_grad():
                    pr = torch.softmax(model(**enc).logits[0], dim=-1).tolist()
                j = max(range(len(pr)), key=lambda i: pr[i])
                lab, p = model.config.id2label[j], float(pr[j])
                stance[rid], sconf[rid] = (lab, p) if p >= self.floor else ("unstated", p)
        width, wconf = base.scope_width, base.scope_confidence
        cm = self._load("scope")
        if cm:
            tok, model = cm
            enc = tok(prose, return_tensors="pt", truncation=True, max_length=2048)
            with torch.no_grad():
                pr = torch.softmax(model(**enc).logits[0], dim=-1).tolist()
            j = max(range(len(pr)), key=lambda i: pr[i])
            p = float(pr[j])
            width, wconf = (int(model.config.id2label[j]), p) if p >= self.floor else (WIDEST, p)
        return RecordReading(case["id"], tuple(sorted(premise)), pconf, stance, sconf, width, wconf,
                             base.values, base.abstained_values, self.identity())


# ---------------------------------------------------------------------------
# Scoring a reading against the truth it was rendered from
# ---------------------------------------------------------------------------
@dataclass
class RecordScore:
    premise_omitted: int = 0      # truth premise factor not included — the expensive error
    premise_included: int = 0     # truth premise factor included
    premise_over: int = 0         # non-premise factor included (cheap: narrows the record)
    guard_included: int = 0       # an IMMATERIAL factor read into the premise
    stance_correct: int = 0
    stance_unstated: int = 0
    stance_wrong: int = 0         # the expensive one when the wrong answer is 'superseded'
    stance_false_supersession: int = 0
    scope_correct: int = 0
    scope_widened: int = 0        # abstained to widest (cheap)
    scope_narrowed: int = 0       # read narrower than truth — the expensive one
    values_correct: int = 0
    values_wrong: int = 0
    values_unrecorded: int = 0


def score_reading(rd: RecordReading, truth: RecordTruth, sc: RecordScore | None = None) -> RecordScore:
    sc = sc or RecordScore()
    got = set(rd.premise)
    for f in truth.premise:
        if f in got:
            sc.premise_included += 1
        else:
            sc.premise_omitted += 1
    for f in got - set(truth.premise):
        sc.premise_over += 1
        if f in truth.immaterial:
            sc.guard_included += 1
    for rid, st in truth.cites.items():
        g = rd.cite_stance.get(rid, "unstated")
        if g == st:
            sc.stance_correct += 1
        elif g == "unstated":
            sc.stance_unstated += 1
        else:
            sc.stance_wrong += 1
            if g == "superseded":
                sc.stance_false_supersession += 1
    if rd.scope_width == truth.scope_width:
        sc.scope_correct += 1
    elif rd.scope_width > truth.scope_width:
        sc.scope_widened += 1
    else:
        sc.scope_narrowed += 1
    for f, v in truth.values.items():
        if f in rd.values:
            if abs(rd.values[f] - v) < 1e-9:
                sc.values_correct += 1
            else:
                sc.values_wrong += 1
        else:
            sc.values_unrecorded += 1
    return sc


def gate(sc: RecordScore, *, min_records: int, n_records: int, premise_recall_target: float = 0.995) -> dict:
    """The acceptance gate for a record reader. Expensive errors fail at any n:
    a premise factor omitted, a false supersession, a scope read narrower than
    stated. Guard inclusions and unstated stances are reported, not gated."""
    carried = sc.premise_included + sc.premise_omitted
    recall = (sc.premise_included / carried) if carried else None
    if n_records < min_records:
        v, why = "inconclusive", f"{n_records} records against a floor of {min_records}"
    elif sc.stance_false_supersession:
        v, why = "fail", f"{sc.stance_false_supersession} false supersession(s): a followed or distinguished record would be displaced"
    elif sc.scope_narrowed:
        v, why = "fail", f"{sc.scope_narrowed} record(s) read narrower than the rationale states: the scope key would prefer them wrongly"
    elif recall is not None and recall < premise_recall_target:
        v, why = "fail", f"premise recall {recall:.4f} < {premise_recall_target}: omitted premise factors over-bind"
    elif sc.values_wrong:
        v, why = "fail", f"{sc.values_wrong} magnitude(s) read wrongly"
    else:
        v, why = "pass", f"premise recall {recall if recall is None else round(recall, 4)}, 0 false supersessions, 0 narrowed scopes"
    return {"verdict": v, "why": why, "premise_recall": None if recall is None else round(recall, 6),
            "premise_precision": None if not (sc.premise_included + sc.premise_over) else
            round(sc.premise_included / (sc.premise_included + sc.premise_over), 6),
            "guard_inclusions": sc.guard_included, "stance_unstated": sc.stance_unstated,
            "scope_widened": sc.scope_widened, "min_records": min_records, "premise_recall_target": premise_recall_target}


class NLIRecordReader:
    """Record fields without training, through a ready NLI head.

    Each field is a hypothesis against the rationale, and each field keeps its
    safe default:

      premise   "The holding turned on <factor>."      include when P(entail) >= include_at (LOW — inclusion-biased)
      stance    three hypotheses per citation; the argmax wins only if it clears the floor, else UNSTATED
      scope     five hypotheses; argmax if it clears the floor, else WIDEST
      values    delegated to the cued regex, or to GLiNER2MagnitudeBackend when given

    The premise threshold is deliberately far below the stance and scope floor:
    omitting a decisive factor over-binds, so weak evidence that a factor was
    decisive is enough to keep it.
    """

    name = "nli"

    def __init__(self, nli, include_at: float = 0.2, floor: float = 0.7, magnitudes=None):
        self.nli = nli                        # a backends.NLIZeroShotBackend
        self.include_at = include_at
        self.floor = floor
        self.magnitudes = magnitudes          # optional GLiNER2MagnitudeBackend

    def identity(self) -> dict:
        return {"reader": "nli", "nli": self.nli.identity(), "include_at": self.include_at, "floor": self.floor,
                "magnitudes": None if self.magnitudes is None else self.magnitudes.identity()}

    def read(self, prose, case, candidates, cite_ids, magnitude_factors):  # pragma: no cover — needs weights
        premise, pconf = [], {}
        for f in candidates:
            p = self.nli.entailment(prose, f"The holding turned on {_w(f)}.")
            pconf[f] = p
            if p >= self.include_at:
                premise.append(f)
        stance, sconf = {}, {}
        hyps = {"superseded": "This holding supersedes and displaces {rid}.",
                "followed": "This holding follows and applies {rid}.",
                "distinguished": "This holding distinguishes {rid} as not governing."}
        for rid in cite_ids:
            m = re.search(re.escape(rid), prose)
            if not m:
                continue
            sent = _sentence_of(prose, m)
            scores = {st: self.nli.entailment(sent, h.format(rid=rid)) for st, h in hyps.items()}
            best = max(scores, key=scores.get)
            stance[rid], sconf[rid] = (best, scores[best]) if scores[best] >= self.floor else ("unstated", scores[best])
        scope_h = {1: "The holding applies to this repository or site only.",
                   2: "The holding applies to the filing team's services.",
                   3: "The holding applies across the product line or division.",
                   4: "The holding applies across every division of the enterprise.",
                   5: "The holding applies in every context, third parties included."}
        sc = {w: self.nli.entailment(prose, h) for w, h in scope_h.items()}
        bw = max(sc, key=sc.get)
        width, wconf = (bw, sc[bw]) if sc[bw] >= self.floor else (WIDEST, sc[bw])
        base = CuedRecordReader().read(prose, case, [], [], magnitude_factors)
        vals, abst = dict(base.values), list(base.abstained_values)
        if self.magnitudes is not None and magnitude_factors:
            got = self.magnitudes.values(prose, magnitude_factors)
            vals = {f: v for f, (v, _u, c) in got.items() if c >= self.floor}
            abst = [f for f in magnitude_factors if f not in vals]
        return RecordReading(case["id"], tuple(sorted(premise)), pconf, stance, sconf, width, wconf, vals,
                             tuple(abst), self.identity())
