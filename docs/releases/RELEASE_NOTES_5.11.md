# Release 5.11.0 — the comparison kernel, the binding gate, and characterisation as a stage (pack 2.1.0, federation 1.1.0)

10 September 2026. Additive to 5.10.0. Every constitution, corpus, opening
store, docket, generator digest and every pre-existing conformance figure is
byte-identical to 5.10.0; the release changes the reference engine's gate,
adds three conformance checks and three mutants per pack, adds a scoring
endpoint to the benchmark, and adds a shared offline extraction stage under
`simulation/tools/extraction/`. What was ported, and from where, is stated in
`simulation/LIKEWISE_INTEGRATION.md`: the author's Likewise 0.15.0 engine was
measured against these corpora first (§1–§3 there), and the parts that
transferred were re-implemented in the packs' standard-library engine rather
than imported.

## The gate is a comparison kernel (engine.py)

The distinguishing gate was `set(premise) <= facts`. It still is, on a
closed-world boolean corpus — VC-51 compares the new kernel with containment
on every (record, case) admission of every gate-reaching case in every pack
(14,832–16,972 admissions per pack, zero disagreements) — but the line is now
the tolerance-zero, all-recorded special case of a kernel that carries three
things the old gate could not:

- **Three-valued facts.** A case's factor is present, absent, or
  *unrecorded* (`Case.unrecorded`, `"unrecorded": [...]` in a case dict). An
  unrecorded premise factor gives the record the admission status
  `premise_unproven`, which outranks `distinguished` and never binds. VC-52
  silences the first premise factor of the controlling record on every bound
  case (1,187–1,198 per pack) and re-adjudicates: every bind either re-forms
  on an untouched record or breaks with the cause named; zero false binds,
  zero guard binds. FC-11 does the same across divisions on Numerals (400
  cross-division binds).
- **A6 under silence.** A case unrecorded on a violating factor of an engaged
  absolute provision takes the new route `floor_unresolved`: refused and
  referred for characterisation, nothing stored. Silence never binds a
  precedent; it must not clear a floor either. Unreachable on a closed-world
  corpus; measured by the extraction stage below (floors missed: 0).
- **Magnitude and tolerance.** `constitution/dimensions.json` (shipped empty
  and valid in every pack) declares a factor as a dimension with a direction
  and a tolerance; the kernel then distinguishes on "weaker beyond
  tolerance" and reports `a_fortiori` and `tolerant` admission separately.
  Coherence rules D1–D4 at load refuse an undeclared direction, a negative
  tolerance, any tolerance on an absolute provision's factor, and an unknown
  factor. VC-51's self-test exercises every regime on synthetic records, so a
  corpus that adds magnitudes inherits a gate already shown to work.

Every trace now carries `gate_outcome` — one of `governed`, `no_candidates`,
`all_distinguished`, `premise_not_established`, `no_controlling` — and a
per-candidate `admissions` map; the docket entry carries the outcome. The
route, decision, controlling record and every pre-existing key are unchanged
on every case of every pack (checked by diff against the 2.0.1 engine).

## The binding gate (harness/binding_gate.py, VC-53, benchmark)

A conformance check counts agreements; this bounds a rate and refuses. An
exact one-sided Clopper-Pearson upper limit on the false-bind rate; `None`
rather than zero when nothing was bound; a floor on binds below which the
verdict is `inconclusive` (300; 3,000 where an absolute provision is
present); guard items on which a single bind fails; and a refusal to call a
pass on an oracle written by the engine's authors. VC-53 applies it to the
engine's own trace with the E-distinguish cases as guards: 0 false binds in
1,187–1,198 binds, 0 guard binds, upper bound 0.0025, verdict `inconclusive`
by the self-authored-oracle rule — which is the verdict a suite should give
itself. The benchmark gains a `binding_gate` endpoint and a `falsebind`
column per arm: on a 1,500-case oracle run of VetPOC, A+ (retrieval without
the gate) binds falsely 88 times in 373 (upper bound 27.5%, 5 guard binds),
B_gov's log citations are false binds 738 times in 759, B and B_mem 0 in 302.
The agreement rate could not separate those arms; the bound does.

## Characterisation as its own stage (simulation/tools/extraction/)

Paper 4 §5's largest admitted limitation is that `facts(c)` is precompiled
and the Evaluator is modelled at ε = 1.00. The new stage renders each case
into a change description in one of five styles (plus three guard styles
that put a factor's words in the text when the case does not carry it),
extracts it back through a backend, decides speak-or-abstain against a floor
fitted for precision on training styles the evaluation never sees, emits a
three-valued facts snapshot, and replays the pack's engine over it against
the reference. Backends: `literal` (proximity; fails the gate on every pack
with ~59,000 guard assertions), `cued` (proximity with negation, hedge,
attribution and sibling-shadowing cues; model-free, passes the gate on every
pack), `deterministic` (fixture), and `modernbert` — a fine-tuned multi-label
head over the pack's factor vocabulary on `answerdotai/ModernBERT-large`
pinned to commit `45bb4654…`, with `modernbert-base` `8949b909…` as the
scale control and `add_prefix_space` recorded per backbone
(`train_modernbert.py` trains it; torch is imported lazily and only there;
the packs stay standard-library).

Measured with the cued baseline, ε on precedent is 0.93–0.98 across the five
packs (reference binds still reached from extracted facts); every bind that
broke, broke as `premise_not_established`; floors missed are zero on every
pack because A6 under silence refused and referred 133–172 floor cases per
pack on which the extractor was silent, at a price of 65–81 over-referrals.
The full table, the literal-baseline contrast and the upper-bound caveat are
in `simulation/tools/extraction/README.md`; reports are in
`tools/extraction/results/`.

## Suites

Every pack: 53/53 conformance (VC-51 reduction and kernel self-test, VC-52
silence never binds, VC-53 binding gate), 27/27 faults killed and 4/4
controls survived (M2 re-anchored on the kernel; M26 silence binds, killed by
VC-52; M27 tolerance padded, killed by VC-51). Numerals: 11/11 (FC-11), 7/7
and 2/2 (MF7). Generator digests unchanged; oracle benchmark and federated
benchmark unchanged on every pre-existing endpoint.

## Not done, on purpose

No pack carries a magnitude factor yet, so the tolerance sweep the
constitutional argument turns on remains unmeasured; the kernel, the
declaration file, the coherence rules and the self-test are the
prerequisite, and adding dimensions to one family of one pack is the next
generator change. No ModernBERT head was trained in this release — the
training script, the pinned backbones and the round-trip harness are here,
and the cued baseline is the number a model has to beat. Rosenbaum's Γ,
free-text embeddings anywhere near the gate, and any admissibility claim
stay out, as `LIKEWISE_INTEGRATION.md` §6 says.
