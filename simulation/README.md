# Simulation packs — five executed enterprises, 6,000 changes each

Added in release 5.8.0; the discriminating suite in 5.8.1; the dataset-skill audit and its three new checks in 5.8.2; the disclosure overlay in 5.8.3; the development-change audit in 5.8.4; **the scenario extension (corpus 2.0.0) in 5.9.0** — see the section of that name below. These are **executed simulations**: five invented
engineering organisations, each proposing 6,000 code changes against a written
constitution, with every disposition computed by a reference adjudicator rather
than authored.

They **extend** the demo packs under `demo/companies/` and replace nothing. The
144-case-per-pack demo corpora are frozen, and every figure the manuscripts cite
from them is unchanged.

| Simulation pack | Demo pack it extends | Domain | Provisions | Absolute | Cases |
| :--- | :--- | :--- | ---: | ---: | ---: |
| `vetpoc-constitution-corpus` | `demo/companies/vetpoc` | Veterinary practice management and point of care | 121 | 26 | 6,000 |
| `semifab-constitution-corpus` | `demo/companies/sctower` | Semiconductor supply-chain control tower | 126 | 28 | 6,000 |
| `frontierllm-constitution-corpus` | `demo/companies/frontierllm` | Frontier model development | 139 | 31 | 6,000 |
| `dcvigil-constitution-corpus` | `demo/companies/dcvigil` | Multi-tenant data-centre monitoring and AIOps | 134 | 26 | 6,000 |
| `numerals` | — (the parent of all five) | Enterprise constitution inherited by every division; 3,000-case federated stream | 33 | 6 | 3,000 |
| `meridian-corpus` | `demo/companies/fintech` | Regulated fintech: payments, cards, ledger, lending | 142 | 33 | 6,000 |

Two of the five are **supersets of a shipped pack**: DCVigil reproduces the 29
provisions of `demo/companies/dcvigil` and Meridian the 37 of
`demo/companies/fintech`, in both cases with identifiers, text and absolute
flags unchanged, so the shipped cases remain valid against the larger
constitution.

## Verify

```bash
bash reproduce/run_all_simulation.sh              # verify all five
bash reproduce/run_all_simulation.sh --rebuild    # regenerate first, then verify
```

Standard library only, CPython 3.10+. No network, no API key, no model is
invoked anywhere.

Current state, reproduced from a clean tree:

```
vetpoc         56/56   0 anomalies   31/31 faults killed, 4/4 controls survived
semifab        56/56   0 anomalies   31/31 faults killed, 4/4 controls survived
frontierllm    56/56   0 anomalies   31/31 faults killed, 4/4 controls survived
dcvigil        56/56   0 anomalies   31/31 faults killed, 4/4 controls survived
meridian       56/56   0 anomalies   31/31 faults killed, 4/4 controls survived
```

All ⟦measured⟧, reproduced from a clean extract of this archive.

## What each pack contains

```
constitution/   rulebook.json, organizations.json, factors.json, parameters.json,
                proposed_amendments.json
corpus/         cases.json, store_seed_initial.json, store_seed.json,
                docket.json, manifest.json, anomalies.json
benchmark/      the five-arm benchmark: stream, arms, judge, scoring, CLI
generator/      the deterministic build — vocab, changes, constitution, corpus,
                docs, explorer, simulation
harness/        engine.py (the §4.6 reference adjudicator), extensions.py
                (Reporter, audit register, admission-rule family, B_gov and
                B_mem), run_conformance.py (56 checks), mutation_matrix.py,
                compare_packs.py
docs/           SIMULATION.md — the run, read end to end, with a ledger of every
                change; simulation.html — the same run, browsable;
                DISCRIMINATING_SCENARIOS.md, COVERAGE.md, MAPPING.md,
                SOURCES.md, CROSS_PACK.md
research/       the surveys the constitution was built from
```

## The easy read, at three depths

Every pack ships all three, for all 5,000 of its changes:

| Depth | File | What it gives you |
| :-- | :-- | :-- |
| The run | `docs/SIMULATION.md` | The whole simulation in plain English: what the firm is, how the case base grew phase by phase, twelve changes read in full, a table of what happened to each of the 25 kinds of change, and **a ledger listing all 5,000 changes** with what each engaged, the answer it got, how that answer was reached, the controlling record, and whether it became precedent. |
| The run, browsable | `docs/simulation.html` | The same run with the store-growth curve, the disposition mix, and a searchable, filterable ledger. Self-contained; open it in a browser. |
| Every case, in full | `docs/CASE_CATALOG.md` (+ `case_catalog.csv`) | Each of the 5,000 cases as its own entry: what the change was, **why that case exists in the corpus**, what the reference engine actually did with it, and which axioms and conformance checks it exercises. The CSV is the same content as one row per case. |
| Every case, browsable | `docs/explorer.html` | The case explorer: facet by disposition, route, category, provision status and origin; full-text search across change titles, provisions and record ids. |

`corpus/cases.jsonl` and `corpus/explorer_data.json` are **not shipped** — they
are machine-readable derivatives of `corpus/cases.json` with no reading value,
and `bash reproduce/run_all_simulation.sh --rebuild` regenerates them.

## The 56 checks

VC-01 to VC-26 test the contract as the demo suites do. VC-27 to VC-44 were
added in 5.8.0 and test what the earlier suites recorded rather than executed.
VC-45 to VC-47 were added in 5.8.2, VC-48 in 5.8.3 and VC-49 in 5.8.4, each because an audit against the
programme's dataset-construction rules found a property asserted somewhere and
tested nowhere:

| | |
| :--- | :--- |
| VC-27, VC-28, VC-29 | CC-26 Docket/Store disjointness; CC-31 consolidated records carry no expiry; CC-30 charging integrity, fail-closed against τ |
| VC-30 | Definition 18 — all four acknowledgement dispositions, exercised |
| VC-31 | Proposition 0 — retrieval loses no gate-admissible record |
| VC-32, VC-33 | Chapter 4 Proposition 1, gate and ordering do not commute; §8 vertical precedent is thin, not thick |
| VC-34 | Theorem 5 — non-monotonicity, both limbs witnessed |
| VC-35 | Chapter 4 Proposition 7 — the docket audit is neutral, width 0, coverage metered by ρ |
| VC-36 | Chapter 4 §6.2 — A_all, A_contest, A_conf and A_ed run over one stream and compared |
| VC-37, VC-38 | Theorems 1 and 2 (standing, not retrieval); Theorem 6's dichotomy |
| VC-39, VC-40 | Theorem 7 (base monotone, constraint not); Theorem 8 and Proposition 5, the admission exchange priced |
| VC-41 | Chapter 5 §6 — B_gov and B_mem executed, neither able to express `Controlling` |
| VC-42 | CC-01 and CC-02 against the published authority roster |
| VC-43, VC-44 | CC-25 register self-check; CC-28 export completeness |

| VC-45 | Definition 11 — every docket entry carries its rating, threshold, consulted set and rulebook version, and no declination is unrated |
| VC-46 | the four intake routes are exhaustive and disjoint over the corpus, and `draft_amendment` is 0 by construction rather than by omission |
| VC-47 | the discriminating suite builds, binds by property, answers as specified, and leaks nothing to the arms |
| VC-48 | the disclosure overlay's labels are recomputed from the note and the facts, its classifier meets a stated specification, and no pair's trace moves on the strength of prose |
| VC-49 | every case is a development change — something a reviewer sees in a pull request — and not a runtime business transaction or a process act with no artefact |
| VC-50 | scenario coverage — every class in the architect's catalogue (`constitution/scenarios.json`) is exercised in every mechanism it requires, computed from the executed corpus; the checker is held to its own self-test, which M25 breaks |
| VC-51 | (5.11.0) reduction — the comparison kernel at tolerance 0 agrees with `set(premise) <= facts` on every (record, case) admission of every gate-reaching case, and the dimensional kernel (tolerance, magnitude, silence, A6 under silence, coherence rule D3) passes its self-test; M27 breaks it |
| VC-52 | (5.11.0) silence never binds — silencing one premise factor of the controlling record on every bound case either re-forms the bind on an untouched record or breaks it with cause `premise_not_established`; scored through the binding gate, zero false binds; M26 breaks it |
| VC-53 | (5.11.0) the binding gate — the engine's own bindings are bounded (exact one-sided Clopper-Pearson) rather than counted, E-distinguish cases are guard items, and the verdict is `inconclusive` because the oracle is self-authored |
| VC-54 | (5.12.0) citation stance — only a `superseded` citation lets a conflicting newer holding displace an older one; every executed ordering re-run with stances forced to superseded is unchanged (the legacy reduction), and followed / distinguished / unstated citations leave the conflict standing; M28 breaks it |
| VC-55 | (5.13.0) the unaddressed adverse fact — a permissive record does not govern a case carrying a violating factor of any engaged provision that the record's facts never contained; zero adverse admissions on the released corpus (every trace is the 5.12.0 trace) and a probe that fires, keeps the acceptance-that-saw-v binding, and refuses to cure a deny; M29 breaks it |
| VC-56 | (5.13.0) decided under prior text — records carry the provision text version; an adopted amendment (`amendment_history`) that touched a premise factor unsettles the holding, a citation-only one does not, a record under the new text binds; zero stale records on the released corpus; incoherent histories refused at load; M30 breaks it |

Three checks in the earlier suites were **fixed rather than added to**, because
their names claimed more than their bodies did: observer non-influence replayed
one configuration twice with no Reporter in existence; the audit-register check
passed on a set that could never be non-empty; and the lapse check covered 16 of
the 442 records that carry an expiry. All three now test the thing they name.

## The benchmark

Each pack carries `benchmark/` — Chapter 6's design, executable. Five arms over
one stream, scored on consistency, floor integrity, interpretive accuracy and
measured cost, with three modes: `oracle` (offline, no key), `dry` (cost
projection) and `live`. See `benchmark/README.md`, or from the package root:

```bash
bash reproduce/run_benchmark.sh          # offline pilot
bash reproduce/run_benchmark.sh cost     # price the full design
```

## What the corpora contain, exactly

Every case is a **development change**: something a developer or a coding agent
proposes, and a reviewer sees, before the code is built and packaged. It is what
a pull request contains — source, configuration, infrastructure, schema and
migrations, pipeline definitions, tests, the policy repository, and the documents
that live in the tree beside them.

It is **not** a runtime business transaction. These packs do not adjudicate
payments, shipments, prescriptions or dispatched invoices; they adjudicate the
change that would alter how those are handled. An audit in 5.8.4 read all 1,525
catalogue titles across the five packs and found forty-eight that had drifted
across that line in one of two ways — an act on live data ("Correct the
mis-posted interchange fee by updating the ledger row" is a data edit, not a
diff), or a process with no artefact ("Complete the vendor security review for
the statement PDF renderer" happens in a meeting, not in a tree). Each was
rewritten as the change that would actually appear in the pull request: the
admin action that edits the row, the review attached to the dependency.

VC-49 is what stops the drift returning, and it is labelled as what it is — a
lexical guard over a closed list of openings the audit rejected, held to a stated
specification of five titles it must reject and five it must keep, because a
check that only asks the guard whether the guard is happy is self-consistent
rather than correct. M24 breaks it.

Corpus version 1.2.0 carries the rewrite. **Only the change descriptions moved**:
every disposition, route, controlling record, consulted set, store entry, docket
entry, category count and published figure is byte-identical to 1.1.0, verified
field by field across all five packs.

## The disclosure overlay

`--justify N` attaches the **author's** account of a change to the case, in four
registers: a truthful admission of a breach, a plain note claiming nothing, a
false claim of compliance over a change that strips a control, and — the row
that keeps the axis honest — the same false-sounding words over a change that is
genuinely clean. The class is computed from the note *and* the case's violation
state, because "no policy impact" is a misrepresentation over a dirty change and
a statement of fact over a clean one.

```bash
bash reproduce/run_benchmark.sh disclosure
```

The design is the pressure twins' design: the same change filed twice, adjacent,
control uncontested, scored on whether the disposition moved. For the judiciary
the answer cannot move — §4.6 takes factors and a note is prose — so its figure
is an ⟦identity⟧ and VC-48 checks the whole trace rather than the verdict alone.
For every arm that hands the change to a model, the note sits in the context
window beside the rule and the figure is a measurement: offline, under the naive
reader, the model arms lose about six of ten misrepresenting pairs while holding
the disclosing and guard directions ⟦measured⟧.

## The discriminating suite

The scored benchmark measures every arm over the whole stream. The
discriminating suite does the opposite: nine small families (eight since 5.8.1,
S9 added in 5.13.0), twenty arrivals, each built so that one specific mechanism is
the only thing that can decide it correctly. Each family names the PACT finding it is built from, and each is
placed in one of three tiers, because conflating them is how a benchmark becomes
an advertisement.

| Tier | Claim | Families |
| :-- | :-- | :-- |
| structural | the monolith cannot close this in principle: what it would need is state, and no larger context window supplies it | S1 stale clearance, S2 silent reversal, S3 exception creep, S4 consolidated pressure, S5 authority order |
| measured | it could; PACT measures that it frequently does not, and a better model narrows it | S6 absolute under compound pressure, S7 plausible record |
| adverse | the architecture does no better, or worse — reported for the same reason as the rest | S8 scope relocation |

```bash
bash reproduce/run_benchmark.sh discriminating          # offline, no key
bash reproduce/run_benchmark.sh discriminating-live sonnet
```

`docs/DISCRIMINATING_SCENARIOS.md` in each pack is generated from the
definitions and carries, per family, the PACT finding, the mechanism that
decides it, what the architecture is expected to answer and the trap the
monolith is predicted to fall into. **The trap is a prediction, not a score.**

Two offline readers exist and the difference is not cosmetic.
`--oracle-reader perfect` answers every arm with a reasoner that applies the gate
and the ordering itself — which hands the monolith arms the architecture's own
work and makes all five arms agree, by construction. `--oracle-reader naive`,
the default for this suite, decides arm B with the engine and reads the arms
nothing binds with a stand-in for three behaviours PACT measures: recency taken
for supersession, a recorded clearance taken at face value, similarity taken for
premise containment. That stand-in **is not a model and is not evidence about
one**; `--mode live` is what produces a claim.

Under the naive reader, in all five packs, four of the nine families answer
differently under arm B than under at least one other arm (S9, the permit that
never saw the violation, separates B from the retrieval-only arm A+), and S4
separates on cost rather than disposition — one model call against twelve for the
same twelve co-pending changes. The families bind to provisions by property rather
than by identifier, which is why the same nine scenarios instantiate in five
different constitutions and produce the same table.

One fairness correction is recorded because it changed the result: the monolith
arms retrieve on coverage alone. An earlier build routed them through the
engine's own `retrieve`, which drops records whose acceptance has expired,
handing them the lapse clock — one of the mechanisms under test. A retrieval
index over an exception log has no expiry semantics: it returns the approval, and
the approval does not say it is dead.

## The scenario extension (release 5.9.0, corpus 2.0.0; corpus 2.1.0 since 5.14.0 adds contested denials)

The packs were built to exercise the *architecture*. This release asks the other
question — does the *constitution* reach every way the firm gets hurt? — and
answers it the way the programme answers everything else: by computing it.

Three documents at this level carry the work. **`SCENARIO_INVENTORY.md`** is the
architect's catalogue: 39 scenario classes (`scenarios.json`), each with its harm
classes (legal, regulatory, reputational, safety, financial), whether a floor is
expected, the mechanisms in which it must be exercised, and the provisions in
each pack that instantiate it. **`CONSTITUTION_AUDIT.md`** is the survey of each
constitution against that catalogue — what was missing, the provisions added by
addition to close it, the draft amendments filed against existing provisions,
and what was deliberately left open. **`SCENARIO_COVERAGE.md`** is the scenario ×
pack × mechanism matrix, every cell ⟦measured⟧ on the executed corpus
(`python3 tools/coverage_matrix.py` regenerates it).

| Pack | New provisions | of which absolute |
| :--- | ---: | ---: |
| `vetpoc-constitution-corpus` | 23 | 8 |
| `semifab-constitution-corpus` | 23 | 8 |
| `frontierllm-constitution-corpus` | 26 | 9 |
| `dcvigil-constitution-corpus` | 26 | 9 |
| `meridian-corpus` | 26 | 9 |

Everything was added, nothing edited: new families with their own factor pools
(`generator/ext_vocab.py`, `ext_changes.py`), `origin: extension`. Findings about
existing provisions — a wrong pin, a superseded instrument, an absolute cited to
"practice policy", two provisions that will tie on every key — are filed in
`proposed_amendments.json` and left pending (A3). Every provision now carries
`scenarios` and a computed `harm_classes`; `status` and `origin` are present in
all five packs, not three.

The corpus was regenerated at **6,000 cases**, the 25-category composition scaled
identically in every pack so the cross-pack comparison survives (`compare_packs`:
composition identical; widest route spread 0.40 points; decision spread 2.20).
The generator now guarantees coverage rather than hoping for it: the first draws
of the routine, plain-deny, floor, pressure-control, like-case-anchor and
risk-owner categories walk shuffled queues over the provisions, so every
provision gets a compliant touch (the guard item), every titled violation
appears, every absolute gets a floor case *and* a compliant touch (touching a
floor is not violating it — A6's conjunction, now exercised 400-odd times per
pack), and every provision gets a pressure twin and a like-case anchor.
**VC-50** verifies the property on the corpus as built and fails on any empty
demanded cell; where the catalogue expects a floor and a constitution supplies
none, that is printed as a note for the lawmakers, not passed off as coverage.

Two construction findings are worth naming. A pressure twin in the first 6,000-
case build diverged from its control because a stored acceptance lapsed at
exactly the twin's timestamp — adjacency and an uncontested control were not
enough; the control must also not have consulted a record that dies one tick
later. The generator now refuses such a control, and VC-13 (full-trace pressure
invariance) is what caught it. And the base packs never gave an absolute
provision a compliant touch, so nothing in the corpora measured over-blocking on
floors; the `--guard` overlay did that only in the benchmark. It is in the corpus
now.

**Arm C, the human desk.** `benchmark/run.py --human` prices a human exception-
review desk that reads every arrival against the rulebook with no case base:
minutes per arrival by complexity and contest depth, loaded hourly rates by tier,
QA sampling, queue turnaround. It makes no decisions and is scored on nothing —
Chapter 6 scopes the human comparison as estimation-only and this keeps to it.
Every input is a stated ⟦PROJECTED⟧ parameter with its basis in
`benchmark/human.py`, the output is ⟦derived⟧, and the dissertation's ~$18,000
per 1,000 extrapolation is quoted beside it as a comparison. Under the default
register the desk prices at roughly $42,000 per 1,000 arrivals and 38 minutes
per arrival against arm B's $0.72 per 1,000 in the offline harness; neither
number is evidence until the timed labelling subsample replaces the register.

Generator defects fixed in place (bugs, not content): three packs' `cases.json`
header said `"pack": "vetpoc"`; the two HTML documents were not byte-stable
(gzip mtime); `status`/`origin` were missing from two packs' schemas.

## Numerals — the parent company (release 5.10.0, federation 1.0.0)

The five packs were always secretly one company: the governance, agent,
application-security and supply-chain blocks recur in every constitution under
different ids. `simulation/numerals/` makes that principled. **Numerals** is the
invented parent; each pack is a division that keeps its own constitution
(unchanged) and inherits an enterprise one of 33 provisions. Inheritance is
minimum harmonisation — a division may tighten, never loosen; an enterprise
absolute is a floor everywhere — and the enterprise may not impose a floor over a
frozen division constitution: where a division states an enterprise floor
ordinarily, the build holds the provision ordinary, marks it `proposed_absolute`
and files a draft amendment against that division (A3 across levels). The
inheritance map is curated by id and checked against the six rulebooks; 22 gaps
were found (change control outside Meridian; CWE-level AppSec in DCVigil and
Meridian) and filed.

The federated stream is 3,000 changes filed by the five divisions against one
shared store. Records on enterprise provisions bind across divisions; a
division's own record is presented one scope step narrower than a foreign one, so
the ordering rule's existing scope key gives Chapter 4 §8's thin vertical
precedent. Ten federation checks and a 6+2 mutation matrix; the offline benchmark
adds a division-local judiciary (`B_div`) beside the federated one so that what
federation buys — citing the record another division wrote, without a model
call — is a column rather than a claim. Start at `numerals/README.md`.

## Cross-pack comparison

Category composition is held identical across all five by construction, so
Chapter 5's RQ3 is answerable by comparing profiles:

- **route shares agree to within 0.40 percentage points** of the corpus on the
  widest cell;
- **decision shares spread 2.20 points.**

Routes belong to the mechanism; decisions belong to the constitution. Run
`python3 harness/compare_packs.py` from any pack to reproduce the table.

## The pack archives — release assets

In the repository the packs are directories under `simulation/`, and that is what
`reproduce/run_all_simulation.sh` and the tests run against. For anyone who needs a
single pack without the whole repository, `reproduce/make_pack_zips.sh` builds one
archive per pack into `simulation/zips/` (not committed; attached to each GitHub
release), and `run_all_simulation.sh` will unpack archives dropped there on first run.

```bash
bash reproduce/run_all_simulation.sh      # verifies all five packs and Numerals
bash reproduce/make_pack_zips.sh          # build the release archives from the trees
```

`make_pack_zips.sh` prints each archive's SHA-256, and the hash of the archive built at
release time is recorded per pack in `simulation/MANIFEST.json`, so a recipient can check
what they were sent.

One difference is worth naming so nobody chases it. Neither the repository nor the
archives carry `corpus/cases.jsonl` and `corpus/explorer_data.json` — machine-readable
derivatives of `corpus/cases.json` with no reading value, regenerated by
`bash reproduce/run_all_simulation.sh --rebuild` (the case explorer under `docs/` is
pre-built and does not need them).

## Release tiers, and what the corpora do not secure

`simulation/RELEASE_TIERS.md` states the public / trusted-contributor / withheld
split, why nothing in these packs falls in the withheld tier (no real external
identifier appears anywhere; the adversarial stratum is adversarial toward the
adjudicator, not toward software; the generator composes a fixed catalogue and
invents nothing), and what the corpora do **not** secure — retrieval quality,
precedent-replication error, factor characterisation, and anything at all about
a model until `--mode live` runs.

## Licence

Code Apache-2.0; corpora, constitutions and documents CC BY 4.0. Each pack
carries its own `LICENSE`, `LICENSE-DATA` and `NOTICE`, and its `docs/SOURCES.md`
records every external source with its verified licence position.
