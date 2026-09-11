# Open models for the characterisation and record stages — a sweep

*11 September 2026. What exists beyond ModernBERT that the Digital Judiciary's
extraction code can use, task by task, with licence, size and the reason it
is or is not in the closed backbone set (`backbones.py`). Everything below
is open-weights; nothing here changes a pack, and no model was run in the
build environment — the entries marked "wired" have a backend or reader in
the code and pinned revisions, and the first GPU session is what turns them
into numbers.*

## The tasks the code actually asks a model to do

| task | text in | answer out | safe default | code |
| :-- | :-- | :-- | :-- | :-- |
| facts | change description | per factor: present / abstain / absent | silence | `backends.py` |
| premise | rationale | per fact: decisive or not | **include** | `records.py` |
| citation stance | the citing sentence | superseded / followed / distinguished | unstated | `records.py` |
| scope | rationale | width 1–5 | widest | `records.py` |
| magnitude | rationale or description | number + unit per dimension | unrecorded | `records.py`, overlay |

Four of these are sentence- or document-level classification with a per-label
probability; one is span extraction with normalisation. That shapes the
sweep: encoders and schema extractors are the right class of model; decoders
are a comparison arm, not a default; embeddings are excluded near retrieval
and the gate on principle (a similarity score has no box-shaped admission
region — `LIKEWISE_INTEGRATION.md` §6).

## Encoders to fine-tune (the `--task` heads)

| model | params / ctx | licence | in the set as | why |
| :-- | :-- | :-- | :-- | :-- |
| ModernBERT-large `45bb4654` | 395M / 8k | Apache-2.0 | **default** | pull-request prose is closer to its web+code pretraining mix than to court opinions; the recipe the rest of the family inherits |
| ModernBERT-base `8949b909` | 149M / 8k | Apache-2.0 | control | same recipe, a third of the parameters: the scale control |
| Ettin-encoder-400m `7662476d` | 400M / 8k | MIT | open-data | ModernBERT recipe on 2T tokens of fully public, reproducible data; reported to match or beat ModernBERT-large. The arm to cite when training-data provenance is questioned |
| Ettin-encoder-1b `befd76be` | 1B / 8k | MIT | scale | the largest open-data encoder in the family; tests whether scale past 400M buys anything here |
| mmBERT-base `c5955035` | 307M / 8k | MIT | multilingual | 1,800+ languages, GLUE within ~1 point of ModernBERT-base; for descriptions not written in English (Numerals divisions file across jurisdictions). Inherits ModernBERT's prefix-whitespace issue on token tasks |
| DeBERTa-v3-large `64a8c8ea` | 434M / 512 | MIT | comparison | wins token classification by ~1.4 F1 under identical pretraining data; 512 tokens means chunking a long description |
| NeoBERT | 250M / 4k | — | **not in the set** | strong GLUE/MTEB, but loads through `trust_remote_code` and its weight licence is not stated on the card; a closed, digest-cited set cannot carry an entry it cannot pin cleanly. Revisit when it is in `transformers` proper |
| CaseLawModernBERT-large | 395M / 8k | Apache-2.0 | **not in the set** | Likewise's default; continued pretraining on US court opinions is not a prior that transfers to change descriptions, and its token-classification gain was never measured |

## Zero-shot: the baseline that runs before any head is trained — **wired**

| model | licence | role | how the code uses it |
| :-- | :-- | :-- | :-- |
| ModernBERT-large-zeroshot-v2.0 `a51e07b5` | Apache-2.0 | zero-shot | `NLIZeroShotBackend`: each factor is a hypothesis ("This change ensures …"), the description is the premise, P(entailment) is the reading; below 0.05 the factor proposes nothing. `NLIRecordReader`: premise / stance / scope as hypotheses with the inverted defaults (premise included at P ≥ 0.2; stance and scope need P ≥ 0.7 or fall to unstated / widest). Slightly behind DeBERTa-v3-large-zeroshot on the author's benchmark, several times faster |
| DeBERTa-v3-large-zeroshot-v2.0 | MIT | alternative | same backend via `--checkpoint`; stronger, slower, 512 tokens |
| GLiClass (modern-large-v2.0 / v3.0) | **CC BY-NC-ND 4.0** | not in the set | a genuinely good uni-encoder multi-label zero-shot classifier (label tokens in the same pass), but the licence forbids commercial use and derivatives, which an Apache-2.0 open-source release cannot depend on. Fine for a private experiment; it cannot ship |

Why zero-shot NLI first: it needs no labelled rows, it handles negation
natively (a negated sentence contradicts the hypothesis), and its known
weakness — reading "the author asserts X" as weak entailment — is exactly
what the hedged guard style prices. It is the honest comparator for every
fine-tuned head and it can run on a laptop.

## Span extraction for magnitudes — **wired**

| model | params | licence | role | how |
| :-- | :-- | :-- | :-- | :-- |
| GLiNER2-base-v1 `f5b2eced` | 205M | Apache-2.0 | extraction | `GLiNER2MagnitudeBackend`: one schema field per declared dimension ("the stated value of …, a number with its unit"), span normalised by the same number/unit regex the cued reader uses, span score as confidence; below the floor the dimension is unrecorded. CPU-deployable; needs `pip install gliner2` in the model environment |
| GLiNER (v1 family) | 200–300M | Apache-2.0 | superseded by GLiNER2 | zero-shot NER only; GLiNER2 adds classification and structured fields in the same model |

## Generative structured extraction — a comparison arm, not a default

| model | params | licence | role | why it is not a default |
| :-- | :-- | :-- | :-- | :-- |
| NuExtract-2.0-2B `5eb4a997` | 2B (Qwen2-VL-2B) | MIT | comparison-generative | emits a whole facts record from a JSON template in one pass, text or image; but it returns no per-token probability, so its confidence is a self-report and the precision-constrained floor cannot be fitted the same way. Worth running once as the "what a small decoder does" contrast |
| NuExtract-2.0-4B | 3B | Qwen Research (non-commercial) | not in the set | licence |
| NuExtract-2.0-8B | 7B | MIT | not in the set | too large for the stage's posture; the 2B carries the contrast |
| NuExtract3 | — | — | not assessed | released after the design; assess when a GPU session is scheduled |

## Diff-aware characterisation — the next instrument, registered but not wired

| model | params | licence | role | why |
| :-- | :-- | :-- | :-- | :-- |
| CodeSage-large-v2 `6e5d6dc1` | 1.3B | Apache-2.0 | diff | a code encoder (The Stack, 9 languages, code–text pairs). The author's prose is a *claim*; the diff is the *evidence*. A characterisation stage that reads factors off the diff, with the description as a second witness, is the version of ε that would survive contact with a real repository. The corpora carry no diffs, so this waits on a generator that emits them |
| UniXcoder, StarEncoder | 125M / 125M | Apache-2.0 / OpenRAIL-M | not in the set | older and shorter-context; CodeSage-v2 supersedes both for this use |

## What stays out, and why

Embeddings of any kind near retrieval or the gate (the admission region is a
box; no score reproduces it). Any model whose licence is non-commercial or
no-derivatives (GLiClass, NuExtract-4B) — the packs are Apache-2.0 and the
data CC BY 4.0, and a dependency the release cannot carry is not a
dependency. Any entry that cannot be pinned to a commit and loaded without
remote code (NeoBERT today). And nothing in this file changes the rule that
torch never enters a pack: every backend imports lazily, and `import
extraction` leaves `sys.modules` free of it.

## The order to run them in, when a GPU session is available

1. `run_roundtrip.py --backend nli` and `run_record_stage.py --reader nli
   --novel-phrasing` on one pack — zero training, one afternoon, and the
   first model numbers beside the cued baseline (facts: ε ≈ 0.95 to beat;
   records: 742–770 of ~1,190 binds kept with zero over-binds to beat).
2. `train_modernbert.py --task facts|premise|stance|scope` on
   `modernbert-large`, with `--control` (base) and then `ettin-encoder-400m`
   as the open-data arm; report the three side by side with the upper-bound
   caveat.
3. `GLiNER2MagnitudeBackend` on the dimensional overlay's rationales, against
   the cued regex (exact on 1,613–2,159 values per pack, but only because the
   renderer is cooperative).
4. NuExtract-2.0-2B once, as the generative contrast.
5. A diff-emitting generator family, then CodeSage on the diffs.

## Sources

- [mmBERT: a Multilingual Modern Encoder](https://arxiv.org/html/2509.06888v1)
- [ModernBERT or DeBERTaV3? Architecture and data influence](https://arxiv.org/html/2504.08716v2)
- [NeoBERT: A Next-Generation BERT](https://arxiv.org/html/2502.19587v1)
- [Ettin Suite: paired encoders and decoders](https://huggingface.co/blog/ettin) · [paper](https://huggingface.co/papers/2507.11412)
- [GLiNER2: An Efficient Multi-Task Information Extraction System](https://arxiv.org/html/2507.18546v1) · [GitHub](https://github.com/fastino-ai/GLiNER2)
- [GLiClass: Generalist Lightweight Model for Sequence Classification](https://arxiv.org/html/2508.07662v1) · [gliclass-modern-large-v2.0](https://huggingface.co/knowledgator/gliclass-modern-large-v2.0)
- [MoritzLaurer/ModernBERT-large-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/ModernBERT-large-zeroshot-v2.0) · [deberta-v3-large-zeroshot-v2.0](https://huggingface.co/MoritzLaurer/deberta-v3-large-zeroshot-v2.0)
- [numind/NuExtract-2.0-2B](https://huggingface.co/numind/NuExtract-2.0-2B) · [NuExtract-2.0-4B](https://huggingface.co/numind/NuExtract-2.0-4B) · [NuExtract-2.0-8B](https://huggingface.co/numind/NuExtract-2.0-8B) · [NuExtract3](https://huggingface.co/numind/NuExtract3)
- [codesage/codesage-large](https://huggingface.co/codesage/codesage-large) · [CodeSage](https://code-representation-learning.github.io/)
- [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large)
