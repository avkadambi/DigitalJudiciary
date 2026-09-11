"""The closed set of encoder backbones, with pinned revisions.

A backbone is named, not supplied: a result is cited by digest, and a digest
over a free-form repository string certifies the string, not the weights.
Revisions are commit hashes, read from the Hugging Face API on 10-11 September
2026; `main` is refused for anything that produces a snapshot. The set was
widened on 11 September after a sweep of open encoders and extractors; each
entry states its ROLE and the reason it is in the set, and no entry is a
default merely because it is newer.

Why ModernBERT-large is the default here and CaseLawModernBERT is not: the
Digital Judiciary's documents are pull-request descriptions and change
tickets, not court opinions, so continued pretraining on 8.3M US opinions is
not a prior that transfers. The base model is kept as the cheap control arm.
DeBERTaV3-large is the matched-data comparison (it wins token classification
by ~1.4 F1 under identical pretraining data; ModernBERT buys context length
and speed, and a change description fits in 512 tokens, so the trade is live
here in a way it is not for a legal filing). `add_prefix_space` is recorded
per backbone: the ModernBERT tokenizer prepends whitespace on a plain call,
which costs ~1.7 NER F1 and the whole family inherits it.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Backbone:
    name: str
    repo: str
    revision: str
    family: str
    params: int
    context: int
    licence: str
    add_prefix_space: bool
    role: str
    note: str


BACKBONES = {
    "modernbert-large": Backbone(
        name="modernbert-large", repo="answerdotai/ModernBERT-large",
        revision="45bb4654a4d5aaff24dd11d4781fa46d39bf8c13",
        family="modernbert", params=395_000_000, context=8192, licence="apache-2.0",
        add_prefix_space=True, role="default",
        note="The default. Pull-request prose is closer to ModernBERT's web+code pretraining mix than to court opinions."),
    "modernbert-base": Backbone(
        name="modernbert-base", repo="answerdotai/ModernBERT-base",
        revision="8949b909ec900327062f0ebf497f51aef5e6f0c8",
        family="modernbert", params=149_000_000, context=8192, licence="apache-2.0",
        add_prefix_space=True, role="control",
        note="The control arm: same recipe, a third of the parameters. Any claimed gain from scale is the difference."),
    "deberta-v3-large": Backbone(
        name="deberta-v3-large", repo="microsoft/deberta-v3-large",
        revision="64a8c8eab3e352a784c658aef62be1662607476f",
        family="deberta", params=434_000_000, context=512, licence="mit",
        add_prefix_space=False, role="comparison",
        note="Matched-data comparison: wins token classification by ~1.4 F1 under identical pretraining data; "
             "512 tokens, so long descriptions are chunked."),
    # ---- added in the 11 September 2026 sweep (see README, 'Other open models') ----
    "ettin-encoder-400m": Backbone(
        name="ettin-encoder-400m", repo="jhu-clsp/ettin-encoder-400m",
        revision="7662476d60abb071a5bd319c9f3074f3072c062d",
        family="modernbert", params=400_000_000, context=8000, licence="mit",
        add_prefix_space=True, role="open-data",
        note="ModernBERT recipe, 2T tokens of fully public and reproducible data; reported to match or beat "
             "ModernBERT-large. The arm to cite when training-data provenance is questioned."),
    "ettin-encoder-1b": Backbone(
        name="ettin-encoder-1b", repo="jhu-clsp/ettin-encoder-1b",
        revision="befd76be43d08b89ff9957012f3ff29d0842780b",
        family="modernbert", params=1_000_000_000, context=8000, licence="mit",
        add_prefix_space=True, role="scale",
        note="The largest open-data encoder in the family; the arm that tests whether scale beyond 400M buys "
             "anything on factor characterisation."),
    "mmbert-base": Backbone(
        name="mmbert-base", repo="jhu-clsp/mmBERT-base",
        revision="c5955035435e2bf121cde7f3c8863ef52ff35d82",
        family="modernbert", params=307_000_000, context=8192, licence="mit",
        add_prefix_space=True, role="multilingual",
        note="1,800+ languages, 8k context, GLUE within ~1 point of ModernBERT-base. For change descriptions "
             "not written in English — Numerals divisions file across jurisdictions."),
    "modernbert-large-zeroshot-v2.0": Backbone(
        name="modernbert-large-zeroshot-v2.0", repo="MoritzLaurer/ModernBERT-large-zeroshot-v2.0",
        revision="a51e07b524299e309dd2b88d48b0cfa2bd9ec598",
        family="modernbert", params=395_000_000, context=8192, licence="apache-2.0",
        add_prefix_space=True, role="zero-shot",
        note="A ready NLI head on ModernBERT-large (entailment / not-entailment). Needs no training: a factor is "
             "a hypothesis, the description is the premise, entailment probability is the reading. The "
             "no-training baseline a fine-tuned head must beat; contradiction handles negation natively."),
    "gliner2-base-v1": Backbone(
        name="gliner2-base-v1", repo="fastino/gliner2-base-v1",
        revision="f5b2ecedebe4381b088c1cf276f5bf72a52cac54",
        family="gliner", params=205_000_000, context=512, licence="apache-2.0",
        add_prefix_space=False, role="extraction",
        note="Schema-driven span extraction on CPU (entities with descriptions, multi-label classification, "
             "structured fields). Used for MAGNITUDES: number-plus-unit spans for a declared dimension, with the "
             "span's score as the confidence. Needs the `gliner2` package, not transformers alone."),
    "nuextract-2.0-2b": Backbone(
        name="nuextract-2.0-2b", repo="numind/NuExtract-2.0-2B",
        revision="5eb4a99746edc2ac44900f56a5c9431d3c03b16d",
        family="decoder-vl", params=2_000_000_000, context=32768, licence="mit",
        add_prefix_space=False, role="comparison-generative",
        note="Template-to-JSON structured extraction on Qwen2-VL-2B (MIT; the 4B is non-commercial). A "
             "generative comparison arm: emits a whole facts record in one pass but gives no per-token "
             "probability, so its confidence is a self-report and the floor cannot be calibrated the same way. "
             "Kept for the contrast, not as a default."),
    "codesage-large-v2": Backbone(
        name="codesage-large-v2", repo="codesage/codesage-large-v2",
        revision="6e5d6dc15db3e310c37c6dbac072409f95ffa5c5",
        family="code-encoder", params=1_300_000_000, context=2048, licence="apache-2.0",
        add_prefix_space=False, role="diff",
        note="Code encoder (The Stack, 9 languages, code-text pairs). For characterising the DIFF rather than "
             "the description — the author's prose is a claim, the diff is the evidence. Not wired to a "
             "backend yet: the corpora carry no diffs."),
}
DEFAULT_BACKBONE = "modernbert-large"


def get(name: str) -> Backbone:
    if name not in BACKBONES:
        raise KeyError(f"unknown backbone {name!r}; the set is closed: {sorted(BACKBONES)}. Adding one is a "
                       "versioned change with a rationale and a named author, not a configuration value.")
    return BACKBONES[name]


def require_pinned(bb: Backbone) -> None:
    if bb.revision in ("main", "master", "", None):
        raise ValueError(f"{bb.name} is pinned to a moving branch ({bb.revision!r}); a result cited against it "
                         "cannot be replayed. Pin a commit hash before producing a snapshot.")
