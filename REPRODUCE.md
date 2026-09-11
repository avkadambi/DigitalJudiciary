# Reproducing the paper

Everything the papers report can be regenerated on a laptop in about two minutes.
There is no network call, no API key, and no `pip install` — the system is CPython plus
SQLite, and the judgment oracles are deterministic by default.

```bash
bash reproduce/run_all.sh
```

If you only want the headline table:

```bash
export DJ_JUDGE_MODE=oracle DJ_DEV_KEYS=1 DJ_GITHUB_ALLOW_UNSIGNED=1
export DJ_SEED_STORE=store_seed_initial.json     # the 20-record OPENING store
python3 demo/reset.py --db /tmp/dj.db --company sctower --sign --yes
python3 reproduce/report.py /tmp/dj.db sctower
```

which prints

```
sctower   store 45 = 20 seed + 25 stored | controlling 43 | bound 55
          | distinguished 35 | tie 1 | absolute 18 | candidates 167
          routes 144 = 110 adjudicated + 10 no-provision + 18 absolute
          + 6 amendment | consolidation: 1 class, 1 record, 2 members
          by citation
```

The second line is new in 5.7.0 and is there because of an erratum. The chapters
used to report a three-way route split — "87 adjudicated / 8 absolute / 6
amendment" — which folds the no-provision route in with the adjudicated one and
moves φ, a hypothesis of the cost proposition, by eight percent. `report.py` now
prints four routes and **asserts that they sum to the session count**, so the
split cannot silently come apart again.

## Which build these numbers belong to

This package is the **144-case, post-consolidation build** — the one the journal manuscripts
describe. The lineage, so that a reader holding an earlier paper can place its figures:

| Build | Cases per pack | Opening store | Headline (sctower) | Reported in |
| :-- | :-- | :-- | :-- | :-- |
| Conference (pre-tie) | 100 | 15 | `37 = 15 + 22 \| tie 0 \| candidates 132` | the JURIX paper |
| Post-tie (23 Aug 2026) | 101 | 17 | `39 = 17 + 22 \| tie 1 \| candidates 134`; controlling 32, bound 44, distinguished 27, absolute 8; suites 47/41/49; matrix 9 of 9, 3 of 3 | intermediate releases |
| **Post-consolidation (5.7.0 onward; this package)** | **144** | **20** | `45 = 20 + 25 \| controlling 43 \| bound 55 \| distinguished 35 \| tie 1 \| absolute 18 \| candidates 167`; suites 61/44/53; matrix 13 of 13, 5 of 5; axiom matrix 8 of 8 | the two journal manuscripts, the dissertation |

Each step added cases by extension and never edited an existing one: the tie case (one per
pack), then the pressure twins and the L-consolidated class members (136 → 144, thirteen
categories). Every figure in this file and in `reproduce/run_all.sh` is the post-consolidation
one; the earlier rows are here only so that no reader mistakes a superseded figure for a
discrepancy.

## Read this before you run anything

**`DJ_SEED_STORE=store_seed_initial.json` is not optional.** The default seed file,
`store_seed.json`, holds the *final* 39-record store — it is what the demo UI loads so that
a browser session has case law in it from the first click. Seeding from that file and
replaying reproduces the dispositions but not the store growth, because the store is already
full. The paper's §7 begins from the 20-record opening store, and that is
`store_seed_initial.json`.

**`--sign` is not optional either.** Without it the ten cases that exhaust the automated
ladder are left waiting on a named human, which is the architecture behaving correctly and
also means those ten resolutions are never written. `--sign` closes them with a stand-in risk
owner so the run completes.

## What each claim maps to

| Claim in the paper | Command | Expected |
|---|---|---|
| Three conformance suites | `python3 run_conformance.py`, `run_interface_conformance.py`, `run_extension_conformance.py` | 61/61, 44/44, 53/53 |
| A9 standing declaration recorded, attributed, carried by every record's provenance | `run_conformance.py`, check `CC-17` | PASS with the declaration in the pack's `rulebook.json`; FAIL (47/48) when it is removed |
| Store growth, admissions, control (§7) | `reproduce/run_all.sh` step 2 | 20 → 45 (46 on `vetpoc`), 25 stored of which **1 consolidated**, 43 controlling, 18 absolute |
| Route split (four routes, asserted to sum) | `reproduce/report.py`, second line | 144 = 110 adjudicated + 10 no-provision + 18 absolute + 6 amendment. The three-way "87 / 8 / 6" of earlier releases folded the no-provision route into the adjudicated one; it is corrected here and the sum is asserted rather than reported |
| Threshold stability interval | step 3 | the final disposition of every case is identical for θ ∈ [0, 0.50]; the aggregates (controlling, bound) are stable only on [0, 0.25], moving to 31/40 at θ = 0.50 |
| θ = 0 endpoint | step 3, `DJ_THETA=0.0` | 214 candidate–case pairs against 156; same 24 stored, same 38 controlling |
| Ordering ablation | step 4 | controlling records: full order 38; auth+ts 34; auth alone 31; ts alone 31. Ties: 1 / 7 / 13 / 11 |
| Contest-rate sweep | step 5 | 24 / 9 / 4 / 1 / 0 records at 100 / 50 / 25 / 10 / 5 % |
| **Pressure invariance (CC-33)** | `reproduce/cc33_pressure_invariance.py <db> <cases.json>`, per pack | 9 of 9 pairs invariant on all four packs |
| **Consolidation (Def. 7(ii))** | `reproduce/report.py`, second line; `run_conformance.py` checks `COR-26`…`COR-29`, `CC-19`…`CC-22` | one class per pack over three co-pending like units; one first-instance record; two members disposed by citation with **zero** gate invocations between them; five refusals (clause (e) twice, (b) once, (c) twice) |
| Mutation matrix | step 6 | 13 of 13 fault mutants caught; 5 of 5 no-op controls survive |
| **Proposition 4, executed** | step 6b, `reproduce/axiom_matrix.py` | **8 of 8 axiom counter-models witnessed** — each guarantee holds with its axiom enforced and fails with it dropped |
| Negative control | step 7, `reproduce/shuffle_control.py` | re-pairing the intact seed records to other provisions collapses controlling 38 → 3 and bound 50 → 7, with the 24 admissions unchanged |
| B_gov baseline (§7.5) | step 8, `reproduce/bgov_baseline.py` | 21 permits and 6 control-plane merges; 74 denials split 41 hard stops / 33 fresh exception tickets; **33 approver decisions** against the architecture's 10 RiskOwner interventions; the 24 cases DJ resolves by citation at first instance become 18 tickets and 6 hard stops |

## Things we would rather you found here than in review

**The mutation pass is 13 of 13, and three of the thirteen earned it by finding a check that
passed for the wrong reason.** Two of those three are new in 5.7.0 and are worth reading, because
both failures were of the same kind — a check that agreed with the code it was checking.

`M10` empties the class artefact's store snapshot, so the store a member was decided against
cannot be recovered from the artefact. `CC-19` was written to catch exactly that, and on the
first pass the mutant survived: the check recomputed the snapshot digest **by calling the same
function the writer calls**, so both sides went empty together and matched. `CC-19` now computes
the digest from the definition, inline. `M12` deletes clause (e) — the guard that stops a second
consolidated record being admitted for a signature a live record already covers — and it survived
because nothing in the conformance corpus was covered, so removing the guard changed nothing. The
corpus now runs a **second docket boundary** after the first class's record is live (`COR-29`), and
the mutant dies at `CC-21`. Neither of those was a bug in the implementation. Both were a check or
a corpus that could not have failed, which is the thing a mutation pass exists to find.

**The 9-of-9 pass that preceded these earned itself the same way.**

**The axiom map used to describe a run that had never happened.** `REPRODUCE.md` and the chapter both
carried an expected-failure map over A1–A8, and the redundancy proposition cited one of those mutants
as built. The executed matrix is a different list — mechanism mutants, anchored on the code — so the
axiom map had never been run at all. `reproduce/axiom_matrix.py` now runs it, **both ways**: for each
axiom a single-line relaxation drops that axiom's enforcement, and the guarantee the proposition names
must *hold* with the axiom in place and *fail* without it. A probe that fails both ways witnesses
nothing; one that holds both ways has not dropped the axiom. Eight of eight are witnessed.

Two things fell out of running it. A6's relaxation is the same edit as mechanism mutant M3, and the
duplication is kept: M3 asks whether the checks notice the fault, A6 asks whether anything is lost
when the axiom goes, and collapsing them would answer one question twice. And **the bootstrap's own
seed import depends on A7 holding** — it writes two lapsed acceptances and reads back the referral
each emits — so dropping A7 against the ordinary opening store stops the container booting before
anything can be observed. The A7 counter-model runs against `seed/store_seed_empty.json` instead, and
the coupling is written down here because no check states it. Deleting the `tier >= 2` precondition on admission — the substance of the
admission rule — originally left all of the checks as they then stood (137) passing. The probe for it (`PRB-8`) *did*
attempt a first-instance admission, but asserted only that the Kernel raised a 422; and a
first-instance artifact is malformed in several other ways, so the call fell through to the
A5 completeness check and raised 422 anyway. The probe now asserts the refusal *reason*, and
the mutant dies. This is what a mutation pass is for, and it is why we report the controls
alongside: three no-op mutants survive, so the suite is discriminating rather than merely
brittle.

**The `depth` ordering key is specified and not instantiated.** `app/adjudicate.py::order`
runs a three-key elimination — authority, recency, scope. There is no fourth key.

**`auth` has two levels, not three.** The key ranks the exceptive authority — the human
RiskOwner at tier k — above the adjudicative function, and treats every adjudicative
instance as equal (`app/adjudicate.py::authority_rank`). The integer in the ledger's
`authority_tier` column is the *depth* at which a case was resolved, i.e. how many
re-adjudications it received. That column is still written and still read — by the A4
exhaustion checks, the review screens and the tier-k queries — but the ordering does not
rank on it, because ranking precedent on resources spent would rank by persistence rather
than by legitimacy (Paper 2 Sect. 4.6). Before this change the `auth` key compared
`authority_tier` directly with `max()`, which fused authority and depth into one
three-level key; that is the behaviour this release corrects. Per pack it moves three
controlling records (`D03`, `D04`, `G06`) and two dispositions (`D03`, `D04`), without
moving any aggregate: the Sect. 7 line is bit-identical for all four packs (sctower
`39 = 17 + 22 | 32 | 44 | 27 | 1 | 8 | 134`, and likewise vetpoc, dcvigil and frontierllm),
as are the three conformance suites, the theta sweep, the contest-rate sweep, the mutation
matrix, the shuffled-store control and the B_gov baseline. The one reported figure it does
move is the `auth`-alone ablation row in the claim table above.

**The tie branch fires exactly once per corpus, and it was put there on purpose.** Every pack
carries one constructed case (category `K-tie`) on which two seed records of equal authority,
equal timestamp and equal scope point opposite ways, so the three keys eliminate nothing and
`resolve` returns `none_tie`. It is a deliberate exercise of a branch that a realistic case mix
had left unexercised, and we say so rather than presenting it as something the corpus happened
to produce. Removing that one case returns the pack to `37 = 15 + 22 | tie 0 | candidates 132`.

**Most gate discards are one factor from surviving.** Of the 33 distinct candidate–case
pairs the distinguishing gate discards in the lead run, 31 are discarded because exactly one
factor of the recorded premise is absent. On a boolean factor vocabulary that is the smallest
difference the gate can register.

**θ is inert on this instantiation, not merely safe.** A record survives the gate exactly
when `premise(r) ⊆ facts(c)`, which is exactly when coverage is 1. So every admissible record
scores the maximum and no threshold at or below 1 can exclude one. The sweep confirms it; the
composition guarantees it.

**One pack admits 23 records where its `expect` blocks call for 22, and the reason is a
modelling question rather than a bug.** `vetpoc` case J02 engages two provisions; every other
stored case in all four packs engages one. The architecture files a case per provision
throughout — `pr_case`, `retrieval_log` and admission are all per `(case, provision)` — so a
two-provision case resolved above first instance admits two records, one per provision. The
corpus's `expect.stored` is a per-case boolean and cannot express that. Whether one record per
resolved provision or one per case is right is the open question §4.6 flags as an obvious
refinement; we have not resolved it, and we note that the "identical behavioural profiles
across domains" claim is therefore identical on three of four, with the fourth differing
exactly where the per-provision question bites.

**The B_gov headline — 33 approver decisions — depends on a convention Definition 12 does
not fix, and the script prints the alternatives rather than hiding them.** B_gov's `eval` is
a pure function of `(Rulebook, c)`, so re-running it on a contested denial returns the same
denial and decides nothing; the only channel past a denial is `approve`. That leaves open
which of the corpus's two scripted fields decides that a denial reaches an approver —
`contest_to` (a social input) or `expect.final_decision` (the disposition the case study
recorded). `reproduce/bgov_baseline.py` takes a denial to an approver when the script records
a named human deciding it (the recorded disposition is a permission, which only `approve` can
produce, or `contest_to = 4`, an explicit push to a named approver), which gives **31**. The
narrower readings give 29 and 30, and reading every contest as a ticket gives 47. The counting
convention is the paper's to state; the run underneath it does not change.

**The corpora are constructed, and their expected outcomes are authored.**
`demo/companies/<pack>/cases.json` carries an `expect` block per case. Those are designed
ground truth, not expert labels. Any agreement number computed against them is a pipeline
check, not a finding — `benchmark/companies/sc_control_tower/company.json` says so in its own
`gold_note` and we repeat it here.

## Experiment hooks

Two environment variables exist only for the experiments above and default to current
behaviour, so an unset run is the ordinary run:

- `DJ_ORDER` — the ordering key sequence, default `auth,ts,scope`.
- `DJ_CONTEST_RATE` — keeps that share of the contests the corpus records, chosen
  deterministically by case id, default unset (all contests replayed).

`DJ_THETA` (default `0.25`) and `DJ_SEED_STORE` are pre-existing configuration.

## Running with a model instead of the oracles

`DJ_JUDGE_MODE=llm` puts a language model at the distinguishing position and needs an API
key. **No number in either paper was produced that way.** The oracle mode is the only
certifiable one and is the default; the LLM path exists so the architecture can be exercised
against a real judgment function, and its outputs are not comparable to the reported runs.

## Layout

```
app/            the contract: kernel, adjudicator, judges, ledger, gateway
seed/           default rulebook, seed store, factor map
demo/companies/ the four executed enterprises, plus a fintech reference pack
benchmark/      the three-condition harness (rules_only | b_mem | dj)
reproduce/      run_all.sh, report.py, mutation_matrix.py,
                shuffle_control.py, bgov_baseline.py,
                run_all_simulation.sh, run_benchmark.sh, make_pack_zips.sh
run_*.py        the three conformance suites
simulation/     the five 6,000-case simulation packs (as directories; archives are release assets),
                the Numerals enterprise package, the scenario catalogue and the
                cross-pack coverage, audit and alignment documents
```

## The simulation packs, the scenario extension, Numerals, the kernel, the record stage, the gate's blind spots and deny-side jurisprudence (5.8.0 → 5.14.0)

Everything above reproduces the demo-pack figures the manuscripts cite. The
simulation packs are a second, larger instrument and reproduce separately:

```bash
bash reproduce/run_all_simulation.sh          # unpack, 56/56 and 31/31 in each of five packs,
                                              # Numerals 11/11 and 7/7, cross-pack comparison, coverage,
                                              # the extraction round-trip, the record stage and the
                                              # tolerance sweep on every pack
bash reproduce/run_all_simulation.sh --rebuild
bash reproduce/run_benchmark.sh               # offline benchmark pilot; `human`, `discriminating`, `disclosure`
python3 simulation/tools/coverage_matrix.py   # scenario x pack x mechanism, recomputed
python3 simulation/tools/extraction/run_roundtrip.py simulation/vetpoc-constitution-corpus --backend cued
                                              # characterisation as a stage: ε measured, no model needed
python3 simulation/tools/extraction/run_record_stage.py simulation/vetpoc-constitution-corpus --novel-phrasing --brief
                                              # record construction under held-out phrasings: binds lost, never gained
python3 simulation/tools/extraction/dimensional_overlay.py simulation/vetpoc-constitution-corpus --brief
                                              # the tolerance sweep on a synthetic magnitude overlay
python3 simulation/tools/amendment_overlay.py simulation/vetpoc-constitution-corpus --brief
                                              # what an adopted amendment would unsettle (prior-text rung)
```

What each release added is in `docs/releases/RELEASE_NOTES_5.8.md` (the packs, the discriminating
suite, the disclosure overlay, the development-change audit), `docs/releases/RELEASE_NOTES_5.9.md`
(the architect's scenario catalogue, 23–26 provisions per pack added by addition, the
6,000-case regeneration with coverage by construction, VC-50, the priced human desk)
`docs/releases/RELEASE_NOTES_5.10.md` (Numerals: the enterprise constitution, the inheritance
map, the federated stream and its checks) `docs/releases/RELEASE_NOTES_5.11.md` (the comparison
kernel, three-valued facts, the binding gate, the extraction stage) and
`docs/releases/RELEASE_NOTES_5.12.md` (citation stance, record construction, the tolerance sweep) and
`docs/releases/RELEASE_NOTES_5.13.md` (the unaddressed adverse fact, decided under prior text) and
`docs/releases/RELEASE_NOTES_5.14.md` (deny-side jurisprudence, corpus 2.1.0; record withholding). `PAPER_ALIGNMENT.md` states, item by item,
which registered conditions of the benchmark paper this artefact executes.

Apache 2.0. Issues and corrections are welcome; if a number here does not reproduce on your
machine we want to know before a reader finds it.


## Corpus provenance, September 2026

This package's corpora are the **144-case build, and the corpus is frozen at this cut.**
Three extensions were applied to the original 101-case Paper-3 packs, in this order,
and all three scripts ship with the package and are idempotent:

1. `demo/build_corpus_extension.py` — the **Absolute Rules Corpus v0.1**: eight
   corpus-derived provisions per company (three absolute at corpus strictness 4/4,
   five statute-tier) and a 26-case ladder exercising the statute/absolute
   asymmetry. 101 → 127 cases, 21 → 29 provisions, 4 → 7 absolute.
2. `demo/build_pressure_extension.py` — the **P-pressure** category: nine cases per
   pack, one per scored pressure mechanism in PACT (Okamoto & Erol 2026, Table 14).
   Each is a twin of a named control case carrying one factor no provision reads,
   placed immediately after its control so both face the same Store, and drawn from
   an uncontested source so that no twin is admitted. 127 → 136 cases, twelve
   categories. **The store counts do not move.**
3. `demo/build_consolidation_extension.py` — the **L-consolidated** category:
   eight cases per pack exercising Definition 16's five clauses. Three
   co-pending units of equal signature form one class, whose representative is
   admitted at first instance under Definition 7 clause (ii); the other five
   cases are the refusals — two whose signature a live record already covers
   (clause (e)), one engaging two provisions (clause (b)), and two on an
   absolute provision (clause (c)). 136 → 144 cases, thirteen categories.
   **The store moves by exactly one record per pack: 44 → 45, and 45 → 46 on
   `vetpoc`.** The provisions the category uses are not hand-picked: the
   builder reads the executed store and derives them, so it stays right if the
   corpus moves.

   The eight cases are appended rather than interleaved, and that is the
   opposite of what the P-pressure category needs. A pressure twin must sit
   next to its control so the pair faces the same Store; a consolidation class
   must face **one pinned Store for every member**, which is what a docket
   boundary is. Interleaving them would give members different stores and make
   the class a statement about nothing.

`reproduce/cc33_pressure_invariance.py` checks the property the second extension
exists to test: that the pressured twin and its control agree on disposition,
outcome, controlling record, gate state and stored status, with the twin's fact set
verified a strict superset of the control's so the comparison is not vacuous.

**Stated against the check rather than for it:** CC-33 survives both mutants written
against it (`reproduce/mutants_pressure.py` — M16 scores retrieval by case-coverage
instead of symmetric overlap; M17 requires the gate to match the premise exactly).
Under §7.6's own rule — a check earns its place by killing a mutant nothing else
catches — CC-33 has not earned its place, and it is shipped as a regression guard
rather than as a discriminating check. What secures the invariance is two things and
only one is structural: the gate is a subset test and therefore monotone in the
facts, which no parameter changes; and retrieval scores well clear of θ on this
corpus, which the threshold sweep already documents as contingent.

`store_seed.json` was regenerated from an executed replay on 2 September 2026 by
`demo/regenerate_store_seed.py`, which now records the corpus size and the
consolidated count in the file itself so that the next reader can tell at a glance
whether it still describes the corpus in front of them. It lagged the corpus by two
records once (Appendix C item 4a); a file nothing imports goes stale quietly, and
this is the cheapest way to notice.

## What consolidation does and does not buy

Consolidation removes one term from the cumulative-gate-work sum per member — the
retrieval and the distinguishing a member would otherwise have run — and it does not
change the order of that sum. It buys a constant factor on a quadratic. Set beside the
width result, which bounds the number of consolidated records that can ever exist by a
constant of the rulebook version, **consolidation buys a constant twice: a constant
width of admission and a constant factor of work.** It is a cost mechanism that happens
to be two-sided; it is not a repair for the one-sidedness the standing theorems
establish and it must not be read as one.

Three things about this build are stated because a reader will otherwise have to find
them:

* **A consolidated record never *outranks* a contested one, and it does not rank
  *below* one either.** `authority_rank` implements the `auth` key's two levels — the
  exceptive authority at tier k above every adjudicative instance, which are equal to
  one another — so a first-instance consolidated record ranks EQUAL to a contested
  tier-2 or tier-3 record and strictly below a risk acceptance. Where both survive the
  gate at a case, the `auth` key does not separate them and **recency does**. The
  specification's phrase "the lowest admissible authority rank" is true of the tier and
  not of the rank this build computes from it. `EX-50` asserts the property that
  actually holds and says so in its own name.
* **Consolidation is a precedent-manufacturing mechanism as well as a cost mechanism,
  and it depends on the good-faith scope condition in a way contest-gated admission does
  not.** Under clause (i), minting a favourable precedent means bringing a contest and
  prevailing above first instance. Under clause (ii), a requester who splits one change
  into N near-identical co-pending units obtains a binding record from a **single
  uncontested first-instance adjudication** — and volume is what an agentic author has
  by definition. Four things contain it and all four are detection rather than
  prevention: `CC-21` caps the total at one live record per (provision, version,
  profile); clause (c) keeps floor-violating units out of every class; the artefact
  records every member, the docket, the snapshot and the parameters, so manufacturing is
  legible; and N₀ and Δ are constitutional parameters the legislature sets, not the
  requester.
* **Class formation holds no authority, and that is enforced rather than asserted.** The
  producing service is a separate object with its own writer (`app/consolidate.py`), it
  appears in the registry so its acts are attributable, and it holds no branch. `CC-22`
  checks all three limbs from the trace: the producer holds no assignment and resolved
  no record, every class artefact predates every member's first gate invocation, and
  re-running `Classify` on a permuted member list returns the same representative.
