# Characterisation as its own stage

*Release 5.11.0 (facts), 5.12.0 (records, dimensions). This directory is
the offline stage that turns a change description into the three-valued facts
the engine reads, and — from 5.12.0 — a rationale into the record fields that
decide what binds later. It is shared by the five packs and Numerals, it is
not imported by any pack, and nothing in it touches torch unless a model
backend is asked for.*

## Why it exists

Paper 4 §5 names the artefact's largest limitation: `facts(c)` is precompiled,
the Evaluator is modelled at ε = 1.00 ⟦identity⟧, and no stage is scored on
turning a messy change into factors. The corpora have what that stage needs
and real records do not — computed ground truth, so a case's factors are
known by construction. Render the case into prose, extract it back, compare.
No human labels anything, and the Evaluator's ε becomes ⟦measured⟧ per pack.

## What crosses the seam

A facts snapshot in which every factor of an engaged provision has one of
three statuses, plus a fourth for what the extractor never sees:

| status | engine reads it as | meaning |
| :-- | :-- | :-- |
| `observed` | `facts` | the description states it and the reading clears the floor |
| `abstained` | `unrecorded` — silence | the extractor read something and was not confident enough |
| `absent` | not a fact | the description does not speak to it |
| `carried` | `facts`, verbatim | outside the engaged provisions' vocabulary (context markers); passed through |

Under a rule of precedence silence outranks distinguishing and never binds
(`PREMISE_UNPROVEN`, VC-52); silence on a violating factor of an absolute
provision refuses and refers rather than proceeding (`floor_unresolved`, A6
under silence). Both are unreachable on a closed-world corpus and both are
reached the moment facts come from here.

## The pipeline

```
render.py      case + engaged vocabulary + style  →  prose with truth attached
backends.py    prose  →  readings with per-token probabilities (no decisions)
abstain.py     temperature, weakest-link aggregation, precision-constrained floor
snapshot.py    readings + calibration  →  ExtractedCase; replay against the reference
roundtrip.py   seven verdicts, assertion precision, the acceptance gate
run_roundtrip.py   calibrate on training styles → evaluate on held-out styles → snapshot → ε
records.py     (5.12.0) rationale → premise, citation stance, scope, magnitude; readers with inverted defaults
run_record_stage.py   (5.12.0) record round-trip with guards → records rebuilt from the reading → replay
dimensional_overlay.py   (5.12.0) synthetic magnitudes on the k most-premised factors → the tolerance sweep
train_modernbert.py   fine-tune ModernBERT heads: --task facts | premise | stance | scope
```

Five rendering styles say a fact five ways; three **guard** styles (hedged,
negated, third-party) put a factor's words in the text when the case does
not carry it, so the only correct behaviour is silence. Styles are split
disjointly into train and eval; guard styles are eval-only; the report
refuses a headline on overlap. Every document carries two guard sentences.

## Backends

| backend | needs | what it is |
| :-- | :-- | :-- |
| `literal` | nothing | label proximity; asserts on every guard. The extractor somebody writes in an afternoon, kept because the harness must reject something |
| `cued` | nothing | literal match; a negation / hedge / attribution cue in the sentence collapses the confidence so the floor abstains. The first honest baseline |
| `deterministic` | nothing | a seeded fake; exercises the pipeline end to end in tests |
| `modernbert` | torch, a fine-tuned head | multi-label classification over the pack's factor vocabulary on a pinned ModernBERT backbone |
| `nli` | torch, no training | a ready NLI head (ModernBERT-large-zeroshot-v2.0, Apache-2.0): each factor is a hypothesis, P(entailment) is the reading; `--reader nli` does premise / stance / scope the same way with the inverted defaults. The first model baseline to run |
| GLiNER2 (magnitudes) | `gliner2` package | schema-driven number-plus-unit spans for declared dimensions, span score as confidence |

The backbone set is closed and pinned to commit hashes (`backbones.py`):
`modernbert-large` `45bb4654…` is the default because pull-request prose is
closer to ModernBERT's pretraining mix than to court opinions;
`modernbert-base` is the scale control; `deberta-v3-large` the matched-data
comparison; `ettin-encoder-400m` / `-1b` the open-data and scale arms;
`mmbert-base` the multilingual arm; `modernbert-large-zeroshot-v2.0` the
zero-shot head; `gliner2-base-v1` the magnitude extractor; `nuextract-2.0-2b`
a generative comparison; `codesage-large-v2` registered for a future
diff-reading stage. Each entry states its role; `MODEL_SWEEP.md` is the
survey behind the set, including what was left out and why (GLiClass's
non-commercial licence, NeoBERT's remote code, CaseLawModernBERT's domain).
`add_prefix_space` is recorded per backbone.

## Measured on the five packs (cued baseline; corpus 2.1.0; floor fitted on plain/formal/narrative, evaluated on tabular/elliptical + the three guard styles)

| pack | gate | assertion precision | recall of carried factors | reference binds | binds kept | binds broken: by silence / otherwise | records withheld | binds on another record / **where the reference abstained** | floors missed | floors referred on silence (of which the reference proceeded) | decision agreement |
| :-- | :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| vetpoc | pass | 1.0000 | 0.973 | 1,189 | 1,098 | 66 / 14 | 42 | 11 / **0** | **0** | 131 (65) | 0.966 |
| semifab | pass | 1.0000 | 0.977 | 1,182 | 1,067 | 92 / 12 | 50 | 11 / **0** | **0** | 135 (66) | 0.962 |
| frontierllm | pass | 1.0000 | 0.952 | 1,188 | 1,036 | 87 / 47 | 154 | 18 / **0** | **0** | 172 (77) | 0.959 |
| dcvigil | pass | 0.9994 | 0.958 | 1,189 | 1,085 | 62 / 24 | 135 | 18 / **0** | **0** | 163 (62) | 0.960 |
| meridian | pass | 1.0000 | 0.975 | 1,201 | 1,148 | 22 / 25 | 80 | 6 / **0** | **0** | 179 (76) | 0.958 |

How to read it. *Recall* below one is the baseline abstaining on factors whose
own slug contains a cue word (`…_not_relaxed`, `…_without_…`) and on factors
shadowed by a longer sibling; those abstentions become `unrecorded`. *Binds
kept* is ε on precedent: 87–96% of reference binds are still reached from
extracted facts. Binds that break do so mostly with the cause named
(`premise_not_established`); the "otherwise" column is store divergence —
a record the extracted run did not write. *Records withheld* (5.14.0) is the
new safety rule in action: a contested case whose hinted premise carried an
unrecorded factor is decided but its record is not written, because a
record with a premise narrowed by silence binds cases the instance never
decided — before the rule, one pack showed 167 such over-binds. The cost is
the lower bind retention; the return is the bold column: **zero cases bound
where the reference abstained, on every pack.** *Floors missed* is the
dangerous error and it is zero everywhere: the 131–179 floor violations the
extractor was silent on were refused and referred (`floor_unresolved`)
rather than let through, at a price of 62–77 over-referrals per pack.

The same runs with the `literal` backend fail the gate on every pack:
59,040–59,370 guard assertions, assertion precision 0.642–0.650,
3,236–3,344 decisions changed and 62–77 floors *invented* per pack by
hallucinated violating factors (`results/roundtrip_*_literal.json`). That
difference is what the guard styles are for.

Every figure is an **upper bound**: the renderer and the extractor share a
vocabulary. The gap to a real change description is unmeasured, and the
report carries the caveat as a field.

## Record construction (5.12.0)

A record's premise, citations, scope and magnitudes are what decide later
binds, and in the corpora they come from the generator. `records.py` renders
the rationale a judge would have written from those known fields, reads it
back, and rebuilds the records from the reading. The error asymmetry runs the
other way from facts, field by field, and each reader's safe default follows
it:

| field | expensive error | safe default when unsure |
| :-- | :-- | :-- |
| premise | a decisive factor **omitted** → the record over-binds | **include** |
| citation stance | followed / distinguished read as **superseded** → a conflicting older holding is displaced | **unstated** (never displaces; the ordering ties and refers) |
| scope | read **narrower** than stated → wins the scope key wrongly | **widest** |
| magnitude | a wrong number binds | **unrecorded** |

The engine reads the stance from 5.12.0 (`Record.cite_stance`; `_displaces`
requires `superseded`; a legacy citation with no stance is superseded, so
every 5.11.0 trace is reproduced — VC-54). Records carry `construction`
provenance (`authored` | `extracted`) per field.

Guards: present-but-immaterial facts written into the rationale (must not be
read into the premise), and followed / distinguished citations (must not be
read as superseded). The gate fails at any n on an omitted premise factor, a
false supersession, or a narrowed scope; guard inclusions, unstated stances
and widened scopes are reported, not gated — they are the safe defaults doing
their job.

Measured on the five packs (corpus 2.1.0), round-trip over every admitted case (about
1,800 renderings per pack) and replay with records rebuilt from the reading:

| pack | cued (cue phrasings) | cued, **held-out phrasings** | literal |
| :-- | :-- | :-- | :-- |
| vetpoc | pass; premise recall 1.000, 0 guard inclusions, 0 false supersessions; replay 1,189/1,189 binds kept | pass; 3,070 guard inclusions, 176 unstated, 1,472 widened; replay 698/1,189 kept, 411 under-binds, **0 over-binds where the reference abstained** | fail: 114 false supersessions |
| semifab | pass; premise recall 1.000, 0 guard inclusions, 0 false supersessions; replay 1,182/1,182 binds kept | pass; 3,154 guard inclusions, 166 unstated, 1,506 widened; replay 685/1,182 kept, 407 under-binds, **0 over-binds where the reference abstained** | fail: 104 false supersessions |
| frontierllm | pass; premise recall 1.000, 0 guard inclusions, 0 false supersessions; replay 1,188/1,188 binds kept | pass; 3,088 guard inclusions, 186 unstated, 1,484 widened; replay 719/1,188 kept, 397 under-binds, **0 over-binds where the reference abstained** | fail: 122 false supersessions |
| dcvigil | pass; premise recall 1.000, 0 guard inclusions, 0 false supersessions; replay 1,189/1,189 binds kept | pass; 3,158 guard inclusions, 160 unstated, 1,548 widened; replay 704/1,189 kept, 379 under-binds, **0 over-binds where the reference abstained** | fail: 110 false supersessions |
| meridian | pass; premise recall 1.000, 0 guard inclusions, 0 false supersessions; replay 1,201/1,201 binds kept | pass; 3,040 guard inclusions, 154 unstated, 1,444 widened; replay 766/1,201 kept, 328 under-binds, **0 over-binds where the reference abstained** | fail: 102 false supersessions |

Read the middle column as the point of the design. Under phrasings no reader
cue matches, the cued reader cannot tell an immaterial fact from a decisive
one, a supersession from a following, or a scope statement from prose — and
what happens is that premises widen, stances go unstated and scopes go
widest, so binds are *lost* (328–411 under-binds per pack, all with cause
`all_distinguished`) and none is *gained*: the "over-binds" column is
entirely binds on another record after the store trajectory diverged; there
is not one case bound where the reference abstained. The literal reader,
which has no defaults, produces 102–122 false supersessions per pack and
fails. A fine-tuned head is what closes the gap between the two cued
columns; `train_modernbert.py --task premise|stance|scope` renders its
training rows from the cue phrasings only, so the held-out run measures
generalisation.

## The tolerance sweep on a magnitude overlay (5.12.0)

No pack carries a magnitude factor, so `dimensional_overlay.py` makes eight:
the compliant, non-absolute factors that appear in the most record premises,
each read as a threshold on a 0–100 index (present ≥ 80, absent 40–79),
with values drawn deterministically from case and record ids and the factors
declared as dimensions in the engine's namespace. ⟦synthetic overlay⟧ — a
statement about what the kernel does at each tolerance on these corpora's
structure, not about which tolerance a constitution should declare.

| pack | τ=0 kept / lost vs boolean | τ=20 kept / lost / gained where boolean abstained | τ=40 gained where boolean abstained | discards at τ=0 turning on a dimension alone |
| :-- | --: | --: | --: | --: |
| vetpoc | 1,007 / 163 | 1,189 / 0 / 24 | 85 | 345 of 15,281 (2.3%) |
| semifab | 931 / 194 | 1,181 / 0 / 19 | 58 | 493 of 15,602 (3.2%) |
| frontierllm | 1,053 / 126 | 1,183 / 0 / 42 | 151 | 281 of 13,647 (2.1%) |
| dcvigil | 1,060 / 94 | 1,175 / 6 / 63 | 168 | 348 of 14,427 (2.4%) |
| meridian | 1,080 / 94 | 1,195 / 0 / 41 | 131 | 307 of 13,600 (2.3%) |

Three things the sweep settles on this structure. Exactness has a price:
at τ=0 the boolean binds a magnitude gate loses are 8–17% of them (a case
at 82 no longer binds a record at 90). A tolerance the width of the value
band recovers them all, and at the same time starts binding cases the
boolean reading calls absent whenever a record sits near the threshold — the
binding gate's false-bind upper bound against the boolean trace rises from
2–10% at τ=0 to 6–16% at τ=40, which is the sweep the constitutional argument
turns on, now runnable. And the falsifier at magnitude reads the same way
it did on booleans: single-dimension margins are 2–3% of discards, not the
majority. The magnitude round-trip (value rendered into the rationale, read
back by the cued reader) is exact on 1,463–2,216 values per pack.

## What an adopted amendment unsettles (5.13.0, measured on corpus 2.1.0)

`tools/amendment_overlay.py` adopts amendments in memory at the first
quartile of the stream and replays under the `decided_under_prior_text`
rung. Three kinds per provision — **limb** (the violating factors are
redefined), **factor** (one compliant factor often in premises), **citation**
(nothing touched) — over the most-bound provisions and, separately, the
provisions with the most *deny-side* binds. Corpus 2.1.0 is what gives the
limb column something to act on: one plain denial in five is now contested
and lost, and the deny record it writes turns on the violating factor.

| pack | binds by deny-side records | limb amendment (deny-side provisions): stale records, binds lost to prior text | factor amendment (most-bound provisions): binds lost | the pack's filed draft amendments, if adopted today |
| :-- | --: | :-- | :-- | :-- |
| vetpoc | 69 of 1,189 | 1–3 records, 2–5 binds per provision | 9–30 binds per provision | 6 filed: 0 binds, 0 records |
| semifab | 96 of 1,182 | 1–3 records, 2–8 binds per provision | 0–20 binds per provision | 5 filed: 0 binds, 0 records |
| frontierllm | 93 of 1,188 | 2–3 records, 2–6 binds per provision | 0–29 binds per provision | 6 filed: 0 binds, 0 records |
| dcvigil | 71 of 1,189 | 1–2 records, 2–5 binds per provision | 12–32 binds per provision | 10 filed: 0 binds, 0 records |
| meridian | 100 of 1,201 | 1–4 records, 3–6 binds per provision | 13–27 binds per provision | 12 filed: 12 binds, 4 records |

A citation-only amendment unsettles nothing anywhere. Meridian's twelve filed
amendments are the only set that would unsettle binding jurisprudence today
(12 binds); the others target provisions whose records are all
permit-side. Deny-side jurisprudence is 6–8% of binds after 2.1.0, against
zero before it.

## Running it

```
python3 tools/extraction/run_roundtrip.py simulation/vetpoc-constitution-corpus --backend cued --out out/
python3 tools/extraction/run_roundtrip.py simulation/meridian-corpus --backend literal      # watch it fail
python3 tools/extraction/train_modernbert.py simulation/vetpoc-constitution-corpus --out runs/mbl --control
python3 tools/extraction/run_roundtrip.py simulation/vetpoc-constitution-corpus --backend modernbert --checkpoint runs/mbl
python3 tools/extraction/run_record_stage.py simulation/vetpoc-constitution-corpus --reader cued --brief
python3 tools/extraction/run_record_stage.py simulation/vetpoc-constitution-corpus --reader cued --novel-phrasing --brief
python3 tools/extraction/dimensional_overlay.py simulation/vetpoc-constitution-corpus --brief
python3 tools/extraction/train_modernbert.py simulation/vetpoc-constitution-corpus --task stance --out runs/stance
python3 tools/extraction/run_roundtrip.py simulation/vetpoc-constitution-corpus --backend nli          # zero training, first model numbers
python3 tools/extraction/run_record_stage.py simulation/vetpoc-constitution-corpus --reader nli --novel-phrasing --brief
python3 tools/amendment_overlay.py simulation/meridian-corpus --brief       # what an adoption would unsettle
```

The model steps run in a separate environment
(`requirements-model.txt`); the packs' `requirements` stay empty.
