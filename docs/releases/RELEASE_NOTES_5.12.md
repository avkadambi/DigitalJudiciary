# Release 5.12.0 — records are constructed, not assumed (pack 2.2.0, federation 1.2.0)

11 September 2026. Additive to 5.11.0. Every constitution, corpus, opening
store, docket, generator digest and every pre-existing conformance figure is
byte-identical; the release changes one line of the ordering rule (guarded by
a reduction check), adds record-construction provenance to the record, and
adds two measurement stages and a tolerance sweep under
`simulation/tools/extraction/`. It completes the programme opened by 5.11.0:
after facts, the four record fields that decide later binds — premise,
citation stance, scope, magnitude — are now read from a rationale under the
same abstention discipline, with the error asymmetry inverted where the field
requires it.

## Citation stance in the ordering rule (engine.py, VC-54, M28)

`_displaces` let any citation of an older record by a conflicting newer one
displace it. A record cites for three reasons and only one is supersession.
Records now carry `cite_stance` (superseded / followed / distinguished /
unstated) and the ordering rule displaces only on `superseded`. A citation
with no recorded stance on a legacy record is read as superseded — the
generator asserts supersession when it writes a cite — so VC-54 re-runs every
executed ordering with stances forced to superseded and finds zero
differences (1,332–1,350 orderings per pack). The self-test in the same check
shows followed, distinguished and unstated citations leave the conflict
standing (the ordering ties and refers) and a superseded one displaces; M28
drops the stance and dies there. Records also carry `construction`
provenance per field (`authored` | `extracted`), so a premise a reader
produced is distinguishable from one the generator produced.

## Record construction as a stage (records.py, run_record_stage.py)

The rationale a judge would have written is rendered from the fields known
by construction — premise, citations with an assigned stance, a scope
statement, and present-but-immaterial facts as premise guards — read back,
and the records rebuilt from the reading. The safe default is different for
each field and is the design: when unsure, a premise factor is *included*
(omission over-binds), a stance is *unstated* (never displaces), a scope is
*widest* (loses the scope key), a magnitude is *unrecorded* (never binds).
The gate fails at any n on an omitted premise factor, a false supersession or
a narrowed scope; the cheap failures are reported.

On the five packs the cued reader passes on cue phrasings with every field
exact and every bind kept. Under **held-out phrasings** no cue matches, and
what happens is the point: premises widen (2,782–2,966 guard inclusions per
pack), stances go unstated (140–190), scopes go widest (1,342–1,410), 311–379
reference binds are lost per pack — and **not one case is bound where the
reference abstained**. The literal reader, which has no defaults, produces
102–142 false supersessions per pack and fails. `train_modernbert.py` gains
`--task premise | stance | scope` (multi-label, 3-way, 5-way heads) with
training rows rendered from the cue phrasings only, so the held-out run is
the generalisation measurement a head has to win.

## The tolerance sweep (dimensional_overlay.py)

No pack carries magnitudes, so the sweep runs on a synthetic overlay: the
eight most-premised compliant factors per pack, each read as a threshold on a
0–100 index, values drawn from ids, declared as dimensions in the engine's
namespace. At τ=0 exactness costs 8–18% of the boolean binds; a tolerance the
width of the value band recovers them all and, wherever a record sits near
the threshold, begins binding cases the boolean reading calls absent — the
binding gate's false-bind bound against the boolean trace rises from 2–7% to
7–19% across the sweep. Single-dimension margins are 2–4% of discards, so
the falsifier at magnitude reads as it did on booleans. The magnitude
round-trip through the rationale is exact on 1,613–2,159 values per pack.
All ⟦synthetic overlay⟧; the overlay writes nothing to any pack.

## The model sweep (11 September, same release)

`tools/extraction/MODEL_SWEEP.md` surveys the open models the stages can use,
task by task. The closed backbone set grows from three entries to ten, each
pinned to a commit and carrying its role: the Ettin open-data encoders (MIT),
mmBERT for non-English descriptions, a ready ModernBERT NLI head as the
zero-shot baseline, GLiNER2 for magnitude spans, NuExtract-2.0-2B as a
generative comparison, and CodeSage-v2 registered for a future diff-reading
stage. Two backends are wired but not run here (no weights in the build
environment): `NLIZeroShotBackend` / `NLIRecordReader` (facts, premise,
stance and scope as hypotheses under the inverted defaults, no training) and
`GLiNER2MagnitudeBackend`. GLiClass and NuExtract-4B were assessed and left
out on licence; NeoBERT on remote-code loading.

## Suites

Every pack: 54/54 conformance (VC-54 added), 28/28 faults killed and 4/4
controls survived (M28 added). Numerals 11/11, 7/7 + 2/2 on the same
engine. Generator digests unchanged; the oracle benchmark and the federated
benchmark are unchanged on every pre-existing endpoint.

## Not done, on purpose

No pack's corpus carries magnitude factors as data; the overlay is the
instrument, and a generator family with real values is the corpus change
that would let the sweep be a registered result. No ModernBERT head was
trained (no GPU in the build environment); four heads' training rows,
pinned backbones and the held-out measurement are in place. Consolidation
clustering by an encoder stays out: a docket function a judge would have to
confirm, and the gate protects each member on its own premise regardless.
