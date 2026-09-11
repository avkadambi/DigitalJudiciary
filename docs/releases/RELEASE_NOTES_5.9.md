# Release 5.9.0 — the scenario extension (simulation corpus 2.0.0)

6 September 2026. Everything below is additive to 5.8.4; the 144-case demo packs
under `demo/companies/` are untouched and every figure the manuscripts cite from
them is unchanged. The five simulation packs move from corpus 1.2.0 (5,000 cases)
to **2.0.0 (6,000 cases)** and are regenerated, so 1.x simulation figures are
superseded by each pack's `corpus/manifest.json`.

## What the release asks

The packs were built to exercise the *architecture*. This release asks whether the
*constitutions* reach every way a regulated software organisation gets hurt — legal
liability, supervisory findings, the public-relations event, a safety incident, a
financial loss — and whether the corpus makes each of the three arms under
comparison (the Digital Judiciary; a monolithic per-case reasoner with no memory; a
priced human review desk) show its work on each of them. It answers by
construction and by computation, not by assertion.

## What was built

1. **The architect's scenario inventory** — `simulation/SCENARIO_INVENTORY.md`, data
   in `simulation/scenarios.json`: 39 scenario classes, each with harm classes
   (legal, regulatory, reputational, safety, financial), whether a floor is expected,
   the mechanisms in which it must be exercised (compliant touch, plain violation,
   floor short-circuit, pressure twin, like-case pair, risk-owner acceptance,
   cross-jurisdiction, control plane), the packs it applies to, and the provisions
   in each pack that instantiate it.
2. **The constitution audit** — `simulation/CONSTITUTION_AUDIT.md`: for each of the
   five constitutions, the topics the survey found it silent on; the provisions
   added **by addition** to close them (23–26 per pack, 8–9 absolute, in 6–8 new
   families per pack, `origin: extension`; nothing existing edited); the draft
   amendments filed against existing provisions (wrong pins, superseded
   instruments, absolutes cited to "practice policy", provisions that will tie on
   every ordering key) and left pending under A3; and what was deliberately not
   closed, with the reason. VetPOC, SemiFab and FrontierLLM now carry amendments
   for the first time.
3. **Coverage, computed** — `simulation/SCENARIO_COVERAGE.md` and each pack's
   `docs/SCENARIO_COVERAGE.md`: the scenario × pack × mechanism matrix, every cell
   ⟦measured⟧ on the executed corpus; `simulation/tools/coverage_matrix.py`
   regenerates it. **VC-50** runs the same computation inside the conformance suite
   and fails on any demanded cell that is empty; where the catalogue expects a floor
   and a constitution supplies none, that is printed as a note for the lawmakers
   rather than counted as coverage. **M25** breaks the checker; VC-50's own
   self-test kills it. Result in all five packs: 50/50, 25/25 faults killed, 4/4
   controls survived, zero construction anomalies.
4. **Coverage by construction** — the generator now walks shuffled queues before
   drawing at random, so every provision receives a compliant touch (the guard
   item), every titled violation appears, every absolute receives a floor case *and*
   a compliant touch (A6's conjunction — touching a floor is not violating it, and
   the 1.x corpora never exercised it), and every provision receives a pressure twin
   and a like-case anchor. The 25-category composition is scaled identically in all
   five packs; `compare_packs` still reports composition identical, with the widest
   route-share spread at 0.40 points and the decision-share spread at 2.20.
5. **Arm C, the human desk** — `benchmark/run.py --human`: a priced human
   exception-review desk that reads every arrival against the rulebook with no case
   base. Estimation-only: it makes no decisions and is scored on nothing, in keeping
   with Chapter 6. Every input (minutes by complexity and contest depth, loaded
   hourly rates by tier, QA sampling, queue turnaround) is a stated ⟦PROJECTED⟧
   parameter with its basis and a tripwire in `benchmark/human.py`; the output is
   ⟦derived⟧ and is replaced wholesale when the timed labelling subsample runs.
   Under the default register it prices at roughly $42,000 per 1,000 arrivals and
   38 minutes per arrival, against the dissertation's ~$18,000 extrapolation
   (quoted beside it) and arm B's $0.72 per 1,000 in the offline harness.

## Construction findings

- A pressure twin in the first 6,000-case build diverged from its control because a
  stored acceptance lapsed at exactly the twin's timestamp. Adjacency and an
  uncontested control were not sufficient; the control must also not have consulted
  a record that dies one tick later. The generator now refuses such a control.
  VC-13's full-trace comparison is what caught it; the 5,000-case build passed by
  luck of timing.
- The base corpora never gave an absolute provision a compliant touch, so nothing in
  them measured over-blocking on floors; only the benchmark's `--guard` overlay did.
  It is in the corpus now.

## Generator defects fixed in place (bugs, not content)

`cases.json` in three packs said `"pack": "vetpoc"`; the two HTML documents were
not byte-stable (gzip header mtime); `status` and `origin` were missing from two
packs' provision schema; VetPOC/SemiFab/FrontierLLM did not write
`proposed_amendments.json` from their vocabulary.

## Tooling

`simulation/tools/`: `EXTENSION_AUTHORING_SPEC.md` (how to write an extension the
generator and the checks will accept), `validate_extension.py` (what it demands,
enforced), `integrate_extension.py` (the idempotent merge into a pack),
`coverage_matrix.py`, `build_audit_docs.py`.

## What is not secured, restated

Retrieval quality, precedent-replication error, factor characterisation, anything
about a model until `--mode live` runs — and now also anything about a human until
the timed subsample replaces the desk register. Every scenario class is exercised;
no claim is made that the catalogue is complete, and the audit's "deliberately not
closed" lists say where it is known not to be.
