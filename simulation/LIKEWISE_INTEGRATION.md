# Likewise 0.15.0 against the Digital Judiciary — what transfers, measured

> **Scope note (5.15.0).** Likewise is a separate project by the same authors. Nothing in
> this repository imports it: the comparison kernel, the binding gate and the extraction
> harness are standard-library re-implementations, and every figure in this repository is
> produced without Likewise installed. The one bridge, `simulation/tools/likewise_gate_bridge.py`,
> is an optional cross-check that takes a path to a Likewise checkout on its command line and
> is not exercised by the tests, the reproduction scripts or CI.


*10 September 2026 (status table in §7 added the same day, after the 5.11.0 build). Likewise is the author's HMDA comparative-review engine; its
`docs/DISTINGUISH_ENGINE.md` (9 Sept) argues that its comparison kernel is the same
object as the judiciary's distinguishing gate and proposes a sequence for joining them,
ending with "what would change my mind". This note runs that sequence's measurable
steps against the five 6,000-case packs and answers the question the author posed.
Every figure is ⟦measured⟧ by `simulation/tools/likewise_gate_bridge.py`, which is in
this tree and needs only a Likewise checkout on the path.*

## 1. The reduction holds on 25,215 real cases, not 256 synthetic combinations

Likewise's `precedent.admit` (the five-valued comparison lattice and the
PREMISE_UNPROVEN › DISTINGUISHED › TOLERANT › A_FORTIORI ladder) was substituted for
`engine.gate` in every pack, with the DJ engine supplying retrieval (premise coverage
≥ θ, lapse filter) and the ordering rule, every boolean factor mapped to a point
dimension (present 1.0, absent 0.0, weaker when lower), tolerance 0. Likewise's own
`binding_gate.evaluate` scored the result against the DJ trace as oracle, with the
E-distinguish cases as guard items.

| pack | cases reaching the gate | binds | false binds | wrong precedent | missed | abstention divergences |
| :-- | --: | --: | --: | --: | --: | --: |
| vetpoc | 5,049 | 1,130 | 0 | 0 | 0 | 0 |
| semifab | 5,027 | 1,122 | 0 | 0 | 0 | 0 |
| frontierllm | 5,046 | 1,097 | 0 | 0 | 0 | 0 |
| dcvigil | 5,046 | 1,111 | 0 | 0 | 0 | 0 |
| meridian | 5,047 | 1,137 | 0 | 0 | 0 | 0 |

Trace-identical in all five: 5,597 binds agreed on disposition and controlling record,
19,618 abstentions agreed on cause. The kernel is a drop-in for the boolean gate. Every
admission was `A_FORTIORI` — as it must be at tolerance zero — and none was `TOLERANT` or
`PREMISE_UNPROVEN`, for the reason in §3.

Likewise's gate returns **`inconclusive`**, not `pass`, on every pack: 1,097–1,137 binds
against its floor of 3,000 where an absolute provision is present, and a self-authored
oracle. That is the right verdict and it is worth keeping: the DJ suites (VC-11, VC-31)
report agreement counts; Likewise's gate additionally refuses to call agreement a pass
when the evidence base is thin or the oracle was written by the engine's authors. Porting
that discipline costs nothing.

## 2. The falsifier fires: single-factor discards are a third, not nine-tenths

`DISTINGUISH_ENGINE.md` §9: *"If the boolean gate's discards are not concentrated at the
single-dimension margin at corpus scale, the case for a dimensional reformulation weakens
considerably."* The dissertation's figure (94% of gate discards at a one-factor margin)
was measured on the 144-case demo corpora; Likewise's own instantiation reported 31 of 33.

At 6,000 cases per pack:

| pack | gate discards | margin 1 | margin 2 | margin 3 | ≥4 | single-factor share |
| :-- | --: | --: | --: | --: | --: | --: |
| vetpoc | 13,913 | 4,311 | 6,500 | 2,020 | 1,082 | 31.0% |
| semifab | 13,240 | 4,327 | 6,083 | 1,680 | 1,150 | 32.7% |
| frontierllm | 12,008 | 3,856 | 5,718 | 1,517 | 917 | 32.1% |
| dcvigil | 12,832 | 3,957 | 6,102 | 1,837 | 936 | 30.8% |
| meridian | 12,305 | 3,976 | 5,995 | 1,634 | 700 | 32.3% |

The mode is a two-factor margin (about 47%); one-factor discards are 31–33%, and the
300 engineered E-distinguish cases per pack account for only about 2% of them. So the
94% does not transfer to the simulation corpora, and the argument that a tolerant gate
would recover most discards does not hold here.

Read it with the caveat it deserves. The margin distribution is a property of how the
generator draws noise factors (two or three compliant factors around a premise of three
to seven), so it is a fact about these synthetic corpora and says nothing about real
records in either direction. What the measurement settles is narrower and still useful:
the one-factor-margin claim is corpus-dependent, and the instrument to measure it on any
corpus now exists.

## 3. The dimensional gate has nothing to bite on yet

Every factor in every pack is boolean. On a boolean dimension a tolerance in [0, 1) is
containment and a tolerance ≥ 1 is vacuous — Likewise's own test says so, and the packs
confirm it: at tolerance 1.0 on Meridian, 3,514 binds, **2,998 false binds, 462 on the
wrong precedent, 5 guard binds**. There is no intermediate regime to sweep.

So the order of work the Likewise document proposes has a prerequisite it does not name:
**the corpora need magnitude factors before a dimensional gate can be evaluated at all.**
Candidates already sit in the scenario vocabulary as colour rather than as facts — latency
regression (%), retention (days), changed-line coverage (%), DTI-style thresholds in
Meridian's lending family, dose-per-kilogram in VetPOC, latency budgets in SemiFab. A
"dimensional factors" extension (the `ext_vocab` mechanism of 2.0.0, one family per pack)
with values on the fact, a declared tolerance per dimension in `parameters.json`, and
Likewise's load-time coherence rules 5, 8 and 9 ported into the constitution loader is the
build that makes the reformulation measurable. Until then the engine work is speculative
and the reduction result in §1 is the whole story.

## 4. What transfers now, without a corpus change

Three things, in order of value.

**`PREMISE_UNPROVEN` and three-valued facts.** The DJ engine treats a factor the case
lacks as absent. That is correct while the Evaluator is modelled at ε = 1.00 and facts are
a closed world; it is wrong the moment facts come from an extractor that abstains, because
"not recorded" would be read as "distinguished" and a silence would defeat a precedent that
should govern — or, under a tolerant gate, a silence would bind. Likewise's ladder puts
silence *above* distinguishing and refuses to bind on it. The DJ engine needs a
three-valued fact representation (present / absent / unrecorded) and this status before
any real record is loaded. That is an engine change of about forty lines, guarded by the
§1 result as its reduction test.

**The binding gate's verdict discipline.** Attainability floor on binds, one-sided
Clopper-Pearson bound on the false-bind rate, guard items that fail at any n, and a
refusal to pass on a self-authored oracle. VC-11 and VC-31 count; this bounds and refuses.

**Named abstention causes.** Nothing retrieved, everything distinguished, premise not
established, admitted but unorderable, conflict unresolved — the DJ trace carries `route`
and `controlling ∈ {record, none, none_tie}` and collapses the first three into "fresh".
The docket entry and the rationale trail would both be better for carrying the cause.

## 5. The ModernBERT extractor is aimed at the right gap

The dissertation's largest admitted limitation (Paper 4 §5; `RELEASE_TIERS.md`) is that
factor characterisation is precompiled: the Evaluator is modelled at ε = 1.00 ⟦identity⟧
and no stage is scored on turning a messy change into `facts(c)`. Likewise's `extract/`
is precisely that stage, and its round-trip harness — render a record whose values are
known into prose, extract it back, score assertion precision with guard styles, refuse a
headline if the evaluation styles were trained on — needs computed ground truth, which
these corpora have and HMDA does not.

Concretely, for the DJ: render each case's factors and change title into a pull-request
description in several registers (the disclosure overlay of 5.8.3 already has four); hold
guard registers out; extract with a backbone; score. That converts ε from an identity into
a measured quantity per pack and per factor family, and it is the "field replication on
raw artefacts with characterisation scored as its own stage" that Paper 4 lists as future
work.

Four notes on the extractor as shipped, for the DJ use:

- `CaseLawModernBERT-large` is the default because it was pretrained on court opinions.
  DJ facts live in pull-request prose, not opinions; `ModernBERT-large` (the control arm)
  or a code/PR-adapted encoder is the right default here, and the closed-set,
  pinned-revision discipline in `backbones.py` is exactly right for a corpus whose
  results are digest-cited.
- `backbones.py` says `"main" is refused by the gate` and pins every revision to `main`.
  Pin to commit hashes before any result is cited.
- The abstention design (temperature scaling per corpus, weakest-link span aggregation,
  precision-constrained floor, floor expires with the corpus) is the part worth taking
  verbatim; its error asymmetry — a miss abstains, a hallucination binds — is the DJ's.
- Torch and transformers must never enter the packs' runtime: the packs' promise is
  standard library only. Extraction is an offline stage that emits a facts snapshot with
  `facts_source: extracted` and per-fact `status ∈ {observed, abstained, absent}`, which is
  why §4's three-valued facts come first. `LiteralMatchBackend` — the afternoon extractor
  that asserts confidently on negated and hedged prose — is the right first baseline and
  needs no model.

## 6. What should not transfer

The Likewise document's own list stands: Rosenbaum's Γ (meaningless on a generated
corpus; report oracle disagreement and mark Γ `not_applicable`), free-text embeddings
anywhere near retrieval or the gate (a proxy for everything in the narrative), any
admissibility claim, and any relaxation of the disclosure machinery for synthetic worlds.
One addition from this side: Likewise's `authority` is a key function, and the DJ ordering
is not — express supersession is a pairwise relation on the survivors — so the DJ ordering
stays as it is and Likewise's `rule()` is used only up to the admitted set, as the bridge
does.

## 7. Sequence, revised by the measurements — and what 5.11.0 built

*Status, release 5.12.0 (table extended from 5.11.0).* Steps 1, 2, 4 and now 5 (as an overlay) below are done, not by importing
Likewise but by re-implementing the parts that transferred in the packs'
standard-library engine (the two projects stay separate). Step 3 is prepared
(the kernel, `constitution/dimensions.json`, coherence rules D1–D4 and a
self-test that exercises every tolerance regime) and waits on a generator
change that gives one family of one pack real magnitudes; step 5 follows it.

| step | where it landed | evidence |
| :-- | :-- | :-- |
| 1. three-valued facts, `PREMISE_UNPROVEN` | `harness/engine.py` in every pack and Numerals: `Case.unrecorded`, `admit()`, gate outcomes on every trace, `floor_unresolved` (A6 under silence — the addition this side made: silence must not clear a floor either) | VC-51 reduction on 14,832–16,972 admissions per pack, 0 disagreements; VC-52 / FC-11 silence never binds; M26 killed |
| 2. binding-gate verdict discipline | `harness/binding_gate.py`; VC-53; `benchmark/score.py` `binding_gate` endpoint and `falsebind` column | verdict `inconclusive` on the engine's own trace, as it should be; A+ 88/373 ≤27.5% vs B 0/302 ≤1.0% on a 1,500-case oracle run |
| 3. dimensional factors in one pack | kernel, declaration file, coherence rules, self-test — no corpus magnitudes yet | VC-51 self-test: a-fortiori / tolerant / distinguished / unproven on synthetic magnitudes; D3 refusal; M27 killed |
| 4. extraction round-trip, ε measured | `simulation/tools/extraction/` — renderer with guard styles, `literal` / `cued` / `deterministic` / `modernbert` backends, precision-constrained floor, round-trip gate, snapshot + replay | cued baseline passes on all five packs; ε on precedent 0.93–0.98; floors missed 0; `literal` fails on every pack (~59,000 guard assertions) |
| 5. tolerance sweep | `tools/extraction/dimensional_overlay.py` (5.12.0) — runnable on a synthetic magnitude overlay, eight dimensions per pack | exactness costs 8–18% of boolean binds at τ=0; band-width tolerance recovers them and begins binding boolean-absent cases (false-bind bound 2–7% → 7–19%); single-dimension margins 2–4% of discards — the falsifier reads as it did on booleans. A registered result still needs a corpus with magnitudes as data |
| 7. (5.13.0) the gate's blind spots — a permissive record falls on a violating factor it never saw; a holding falls once its text was amended on a premise factor | `engine.admit` rungs `adverse_unaddressed`, `decided_under_prior_text`; VC-55/56, M29/30, S9; `tools/amendment_overlay.py` | this is `weaker_when` relative to the HOLDING on booleans, which the Likewise lattice states per dimension and the DJ gate had never applied; inert on the division corpora, 55 outcomes corrected in Numerals |
| 6. (5.12.0) record construction — premise, citation stance, scope, magnitude read from a rationale | `records.py`, `run_record_stage.py`; `Record.cite_stance` in the ordering rule (VC-54, M28) | safe defaults inverted per field; held-out phrasings: binds lost, never gained; literal reader fails on false supersessions |

ModernBERT: `modernbert-large` is the default backend, pinned to commit
`45bb4654a4d5aaff24dd11d4781fa46d39bf8c13`; `modernbert-base`
`8949b909ec900327062f0ebf497f51aef5e6f0c8` is the scale control;
`deberta-v3-large` is refused until pinned. `train_modernbert.py` fine-tunes
a multi-label head on the training styles only. No head was trained for this
release; the cued baseline is the number it has to beat, and the round-trip
gate is what it has to pass.

*The original sequence, for the record:*


1. Three-valued facts and `PREMISE_UNPROVEN` in `engine.py`, with §1 as the reduction
   test (VC-51: the Likewise gate and the engine gate agree on every trace at tolerance 0).
2. The binding-gate verdict discipline into the conformance suite.
3. A dimensional-factors extension to one pack, with tolerances in `parameters.json` and
   the coherence rules at load — the prerequisite the Likewise sequence skipped.
4. The extraction round-trip on that pack: `LiteralMatchBackend` first, ModernBERT-large
   offline second; ε becomes ⟦measured⟧.
5. Only then the tolerance sweep the constitutional argument rests on.

Step 5 of the Likewise sequence — run a judiciary slice end to end — is done, and its
result is the reduction in §1 plus the falsifier in §2.
