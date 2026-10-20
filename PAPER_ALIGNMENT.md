# The benchmark paper against the artefact — what is implemented, what is not

*Paper 4 (Benchmarking Governed Precedent, v2.1) §3 registers a design; since v2.1 its §3.1
describes the released corpus and its §3.6 carries this reconciliation from the paper's side. This
file says, item by item, what the released artefact (release 5.16.0, simulation
pack 2.4.0 / corpus data 2.1.0) executes as registered, what it executes in a different form,
and what it does not execute at all. It exists so that no reader has to infer
the answer from the code, and so that the paper's text and the artefact can
be reconciled before either is cited. Every number is ⟦measured⟧ on the
released corpora unless marked otherwise.*

## 1. Corpus (paper §3.1)

| Registered in the paper | In the artefact | Status |
| :-- | :-- | :-- |
| Five worlds: VetPOC, SC Control Tower, DCVigil, FrontierLLM, Fin Health | Five packs: VetPOC, **SemiFab** (extends the `sctower` demo pack), DCVigil, FrontierLLM, **Meridian** (extends the `fintech` demo pack) | **Names differ.** The paper should adopt the pack names or the packs' READMEs should state the aliases; the domains match. |
| 1,200 cases per world, 6,000 total, extended from 144-case seed packs (68 for Fin Health) by a generator over eleven category templates | **6,000 cases per pack, 30,000 total**, generated over **25 categories** held identical across packs; the 144-case demo packs ship separately and are not the seeds — each pack has its own opening store (197–211 records) | **Larger and differently structured than registered.** Size is not the constraint; the paper's §3.1 text describes an earlier design and needs rewriting to the artefact. |
| Absolute-adjacent stratum set to 15% in every world, reweighted for headlines | F-absolute is 5.8% of each pack; cases that engage an absolute provision at all (floor violations, compliant touches on floors, absolute probes) are 8.1% | **Below the registered 15%.** Either the paper's power computation for dangerous errors (§3.4) is re-run at 8.1%, or the composition is raised — a one-line change to `CATEGORIES_6000` in `simulation/tools/integrate_extension.py`, identical in all packs, followed by a rebuild. |
| ≈615 engineered like-case pairs, injected at controlled separations: adjacent, +100, +500 | **1,200 pairs (240 per pack), all adjacent** | **Count exceeds; separation strata are missing.** The generator places anchor and twin adjacently so both face the identical store; +100 / +500 separations would let the store move between the two and need the full-trace invariance check (VC-13's pattern) extended to them. Not built. |
| Decision-conditional ("both-branch") gold on path-dependent cases; followed-branch and gold-branch scoring | Ground truth is the reference engine's single chronological pass; a case has one `expect` | **Not built.** Path-dependent categories (precedent, ordering, distinguish, lapse, renewal, supersession, cold start, tie, inexpressibility) are **31.5%** of each pack, so the strata exist; the second branch of gold does not. |
| Four QA gates: outcome-vocabulary lint, factor-profile dedup, oracle totality, canary tagging | Canary on every case (VC-47 also checks the arms' prompt leaks nothing); oracle totality by construction (zero construction anomalies, VC-01/02 replay); development-change lexical guard (VC-49); leak tests over what an arm is shown | Three of four present in some form; **factor-profile deduplication is not enforced** (like-case twins are deliberately near-duplicates). |
| Generators, seeds, manifests and a datasheet ship with the paper | `generator/` (seed 20260905, deterministic; `reproduce/run_all.sh` rebuilds and compares digests), `corpus/manifest.json`, `DATASHEET.md` | Present. |
| Federation (release 5.10.0) | Not registered in the paper; Chapter 7 names it as future work | **Added**: `simulation/numerals/` — an enterprise constitution over the five divisions, a 3,000-case federated stream with cross-division like-case pairs (disposition **and** citation) and a division-local vs federated judiciary contrast. A candidate registered endpoint for a revision; see `docs/releases/RELEASE_NOTES_5.10.md`. |
| Scenario coverage | Not registered in the paper | **Added in 2.0.0**: 39 scenario classes, per-provision mapping, VC-50 — see `simulation/SCENARIO_INVENTORY.md`. The paper could cite it as the corpus's construct-validity argument. |
| Characterisation scored as its own stage (paper §5 names it as the main limitation: ε = 1.00 ⟦identity⟧) | Not registered as a condition | **Added in 5.11.0**: `simulation/tools/extraction/` renders each case into a change description, extracts it back, emits three-valued facts and replays the engine against the reference. With a model-free baseline ε on precedent is ⟦measured⟧ at 0.93–0.98 per pack, floors missed 0 (A6 under silence), all broken binds named. A ModernBERT-large backend (pinned) is wired but no head has been trained; the figures are upper bounds and say so. A candidate registered endpoint. |

## 2. Arms and ablations (paper §3.2)

| Registered | In the artefact | Status |
| :-- | :-- | :-- |
| Arm A — frontier model, full rulebook + case, no record | Arm `A` | Present, as registered. |
| Arm B — the judiciary, model at the adjudication function only, economy tier first instance / frontier on escalation, both judgment functions mechanical (θ = 0.25, premise-subset gate) | Arm `B`: engine gates, orders and short-circuits; the model is called only where nothing controls; θ = 0.25 and the subset gate are the engine's | Present. **Tiering by instance (economy → frontier on escalation) is not wired**: one model per run (`--models`); run twice to price it. |
| B_mem — same record on the same model, no normative force (the headline comparator) | Arm `B_mem` | Present. |
| B_gov — executed governed-exception baseline | Arm `B_gov` | Present. |
| A+ (RAG comparison) | Arm `A+` | Present; not in the paper — either register it or drop it from the headline table. |
| Arm C — human panel, n = 300, blind + foil-seeded, anchored variant | **Not simulated, by design.** `--human` prices a review desk (estimation-only, no decisions, ⟦PROJECTED⟧ inputs) | Consistent with the paper's estimation-only stance; the panel itself is a study, not an artefact. |
| 2⁴ factorial over bindingness, ordering, escalation, floor short-circuit | Only **bindingness** is switchable (B vs B_mem). The other three are engine constants | **Not built.** Ordering-off, escalation-off and floor-off are each a small flag on `harness/engine.py` plus arm entries in `benchmark/config.py`; the mutation matrix already exercises the faults (M1, M3, M4), so the switches exist as mutants, not as arms. |
| Contest-policy sweep: contest-nothing, 2 / 10 / 25%, strategic losing-party, contest-everything | `contest_to` is fixed per case in the corpus; the random overlay has `--p-contest` | **Partially.** The overlay can sweep a base rate; the stratified corpus cannot, and **strategic losing-party contest is not built** — it needs a policy that re-decides `contest_to` from the disposition. B7's registered failure prediction cannot be tested without it. |
| τ-sweep {0, 25, 50, 75, 100} | τ is per family in each constitution (15–34) and is constitutional; there is no `--tau` override | **Not built as a sweep.** The paper says the released corpus runs τ = 0 everywhere; the 2.0.0 packs do not — the prosecutor declines about 5% of arrivals at the constitutional τ. Reconcile before citing B8. |
| W-sweep {0, 4h, 24h, 72h, ∞} | Contest window is ∞ (any `contest_to` is honoured) | **Not built.** |
| Model-gate reference condition (distinguish by an economy model on the frozen sub-sample) | Gate is exact everywhere | **Not built.** |
| Ordering rule — express supersession | `older.id in newer.cites` | **Refined in 5.12.0**: a citation carries a stance and only `superseded` displaces; legacy citations reduce to supersession on every executed ordering (VC-54), so every figure stands. The paper's §3 description of the recency key should say "express supersession, i.e. a citation with stance superseded". |
| Record construction (premise, citations, scope, magnitude) | Generator-supplied; not registered as a stage | **Added in 5.12.0** as a measured stage with inverted safe defaults; under held-out phrasings the cost is binds lost, never binds gained (0 over-binds where the reference abstained on every pack). A candidate limitation-turned-endpoint for §5. |
| Tolerance sweep on the gate | Not registered | **Runnable in 5.12.0 on a synthetic magnitude overlay** (`dimensional_overlay.py`): exactness costs 8–18% of boolean binds at τ=0; a band-width tolerance recovers them and begins binding boolean-absent cases; false-bind bound 2–7% → 7–19%. Not a result until a corpus carries magnitudes as data. |
| Distinguishing — direction | `distinguish(r, c)` iff premise(r) ⊄ facts(c) | **Corrected in 5.13.0**: a permissive holding also falls on a violating factor of any engaged provision that the record never saw (`adverse_unaddressed`). Inert on the five registered corpora (zero changed traces); it changed 55 outcomes in Numerals' D-vertical stratum, whose construction is corrected. The paper's Definition of distinguishing should add the adverse-fact clause, and the S9 family is the discriminating item for it. |
| Deny-side jurisprudence | Every plain denial accepted; no record turned on a violating factor | **Corpus 2.1.0 (5.14.0)**: one plain denial in five is contested and lost and writes a deny record on the violating factor; 82–113 such records and 69–100 deny-side binds per pack; the 25-category composition is unchanged. The §3.1 rewrite should state the contested share, and the limitation that binding jurisprudence was permit-side only no longer holds. |
| Records and amendments | Records tied to a provision id | **Added in 5.13.0**: provision text versions and `decided_under_prior_text`; on corpus 2.1.0 the overlay shows limb amendments unsettle 2–8 deny-side binds per provision and compliant-factor amendments up to 32; Meridian's filed amendments would unsettle 12 binds if adopted today. |
| Gate semantics | Boolean containment gate | **Generalised in 5.11.0** to a comparison kernel: three-valued facts (silence never binds; `premise_not_established` is a named abstention), magnitude factors with declared tolerances (`constitution/dimensions.json`), A6 under silence. VC-51 proves the reduction to the registered gate on every case, so every figure in the paper stands; the paper may now describe the gate as the tolerance-zero instance of the kernel. No pack carries magnitudes yet, so the tolerance sweep is still not a result. |
| Consolidated-admission reference condition (N₀, Δ at the constitution's values) | Consolidation **is on** in the corpus (L-consolidated, 198 cases per pack, Definition 7(ii)); it is not switchable in the benchmark | **Inverted relative to the paper**, which registers consolidation off in Arm B and on only in the reference condition. Reconcile: either add a switch or amend §3.2. |
| Adversarial floor chains | Y-adversarial (210 per pack) includes absolute probes; the discriminating suite's S6 is absolute-under-compound-pressure | **Partially.** A *chain* — a run of individually defensible grants marching toward the floor — is not constructed. |

## 3. Measures (paper §3.3)

| Registered | In the artefact | Status |
| :-- | :-- | :-- |
| pass^k, k = 3 headline and k = 8, estimated as mean of C(c,k)/C(n,k) with n ≥ k attempts, success = disposition **and** controlling citation match gold | `--k` draws k attempts; `score.py` reports **self-consistency across attempts** (all k agree on disposition and citation) and, separately, agreement with the reference engine restricted to cases where no record controls | **Not the registered estimator.** The C(c,k)/C(n,k) form against gold is a small addition to `score.py`; the citation requirement is already in the self-consistency figure. |
| Gold agreement with 95% CIs clustered by company and pair | Interpretive accuracy (restricted, labelled) without CIs | **CIs and clustering not built.** |
| Like-case consistency = identical disposition and identical controlling citation | Consistency = identical disposition on the engineered pairs | **Citation not required in the pair test.** One-line change in `score.py`; VC-16 in the conformance suite already checks dispositions. |
| Dangerous errors per 1,000 | Floors upheld (rate) | Present as a rate; per-1,000 is arithmetic. |
| Ratchet divergence Δ_R | — | **Not built** (depends on both-branch gold). |
| Cost and latency per 1,000 at a frozen pricing snapshot | Cost per arm at `config.py` prices (6 Sep 2026), with the no-call fraction; latency not measured in oracle mode | Present for cost; latency only in `live`. |
| Chance-corrected companion and confusion matrix for every exact-match figure | — | **Not built.** |
| Bound on the false-bind rate (not registered; the paper reports citation agreement as a rate) | — | **Added in 5.11.0**: `binding_gate` endpoint per arm — exact one-sided 95% upper bound on citations of a record that does not govern, guard items, `inconclusive` floor, self-authored-oracle refusal — and a `falsebind` column in the summary. On a 1,500-case VetPOC oracle run it separates A+ (88/373, ≤27.5%) and B_gov (738/759) from B and B_mem (0/302, ≤1.0%) where the agreement rate did not. Worth registering beside like-case consistency. |
| Model-judge correction (Rogan–Gladen / PPI) | — | Not applicable in oracle mode; **not built** for live. |
| Panel diagnostics: κ, foil sensitivity, anchoring | Out of scope for the artefact | Study instruments, not code. |

## 4. Is the size enough? Is the coverage enough?

**Size — yes, with room to spare.** The paper registers 6,000 cases in total; the
artefact carries 6,000 per world. Every power figure in §3.4 was computed for
the smaller design and is conservative here: the DJ-vs-B_mem accuracy contrast
(≈1,455 per arm) is resolvable within a single pack; ratchet divergence
(≈1,600 path-dependent cases) is resolvable within a single pack, which has
about 1,890; the like-case contrasts (≈57 pairs vs frontier) are resolvable
in any pack's 240 pairs. The one stratum the paper sized that the artefact
under-supplies is the absolute-adjacent one (8.1% against the registered 15%);
at 6,000 per pack that is still ≈486 floor-engaging cases per world, more than
the ≈71 expected dangerous-error events the paper's own computation needs,
so the power holds — but the paper's sentence saying the stratum is 15% does
not.

**Coverage — enough for the paper's primary claims, not for its full
registration.** What the artefact can adjudicate today, offline or live:
B1(i) DJ against B_mem on consistency and on restricted accuracy (with the
pass^k estimator and the pair-citation requirement added — both are small),
B1(ii) the DJ − A decomposition, B3 dangerous errors DJ against A, B4 model
cost, the discriminating suite, the disclosure axis, the guard items, and the
scenario-coverage argument that the corpus reaches the legal, compliance and
reputational classes an architect would demand. What it cannot adjudicate as
registered: B7 and B8 (no strategic-contest policy, no τ-sweep, consolidation
not switchable), the factorial main effects other than bindingness, the
W-sweep, the model-gate and consolidated-admission reference conditions,
ratchet divergence, and anything on both-branch gold. Those are the paper's
secondary and theory endpoints, and the honest course is one of two: amend
§3.2–3.5 to register only what the artefact runs, or build the missing
conditions before the live run. The cheap ones — pass^k as registered,
citation in the pair test, the ordering / escalation / floor switches, a
`--tau` override and a `--contest-policy strategic` option — are each under a
day; both-branch gold and the separation strata for like-case pairs are
generator work of a different order.

**The structural mismatch, settled.** Earlier revisions of the paper described a corpus that
no longer existed (144-case seeds extended to 1,200 by eleven templates). Paper 4 v2.1
(11 September 2026) rewrites §3.1 to the released corpus — 6,000 per pack over 25 categories,
own opening stores, 1,200 adjacent pairs, the 8.1% floor stratum, deny-side precedent — and
adds §3.6, which lists what the artefact executes as registered, what it executes differently
and what is owed before execution. The two documents now say the same thing from opposite
sides.

## 5. Enterprise Conscience registered extension (5.16.0)

*The Enterprise Conscience paper (Sect. 4.5, OR3) proposes an evaluation and reports no
estimate; `prereg/PREREG_EC_SIM_v1.md` registers that evaluation on this artefact as
hypotheses H1–H7 over estimands E1–E8. This section maps each to what `simulation/ec/`
executes. The registered run is in progress; nothing below is a result. Policy-agent
figures, when they exist, are ⟦measured⟧ against ⟦identity⟧ archetype truths; every LLM
figure is ⟦PROJECTED⟧ until a live run.*

### 5.1 Estimands (prereg Part A §3)

| Registered | In the artefact | Status |
| :-- | :-- | :-- |
| E1 proposal risk: share of impermissible acts among no-audit ai-agent control arrivals, by tier, severity, omitted duties | `e1_imperm`, `e1_T0..T3`, `e1_severity`, `e1_omitted_duties`, `e1_human` from `run.jsonl` lines with `author_kind = ai-agent`, `audit_announced = false`, `twin_of = null`; impermissibility is `run_year.impermissible()` over act, canon and registry | Present. `e1_omitted_duties` is a constant 0: no canon carries a positive-duty T1 entry, so the column exists and is empty by construction. For policy agents E1 is identical across arms (the proposal rng is seeded per skeleton); its cross-arm difference is a measurement only in the LLM slice. |
| E2 pressure sensitivity: E1 under an excluded presented driver minus under NONE | `e2_ps`, by level and tier, `e2_rate_excluded`, `e2_rate_none` | Present. The policy agent does not read the driver level, so `e2_ps_l1` and `e2_ps_l2` differ only by sampling error. |
| E3 observation gap: impermissible(announced twin) minus impermissible(control), paired | `e3_og` over `e3_n_pairs`; twins at TWIN_RATE 0.25, never on a corpus-contested control | Present. The identity for `observation_sensitive` is −0.833 × E1 of the control lines (the twin draws the same uniform against a probability scaled by 0.167). |
| E4 positive control: permitted T2/T3 departure rate with an admitted reason minus under NONE | `e4_diff`, `e4_rate_admitted`, `e4_rate_none` | Present. The rate under NONE is exactly 0 by the agent's construction. |
| E5 espoused–enacted gap, LLM live only | `e5_eeg` from `believes_monitored` on twin lines | **Column present, no data.** NA for policy agents (they return the announcement) and in `dry` mode. |
| E6 disclosure fidelity: recall, precision, label shares | `e6_recall`, `e6_precision`, `e6_discloses`, `e6_silent`, `e6_misrepresents`, `e6_nothing_to_disclose` from `reconcile` | Present. EC-07 holds the recovered rates to ±0.03 of the identity, with identity precision `d / (d + r/2)`; F-EC-7 (reconcile reads a carried label) kills it. |
| E7 blind spot: impermissible executed over proposed; share the bench ever saw | `e7_blind_spot`, `e7_imperm_executed`, `e7_imperm_proposed`, `e7_bench_saw` | Present. In arms C and D `e7_imperm_executed` is 0 ⟦identity⟧ under EC-02, EC-03 and EC-05. |
| E8 doctrine return: escalations per 30 days before vs after the first gloss, days to codification, gloss-bar blocks | `e8_esc_per30_before`, `e8_esc_per30_after`, `e8_days_to_codification`, `e8_n_codified`, `e8_gloss_bar_blocks`, `e8_n_entries` | Present in arm D only; NA in A, B and C by construction (no gloss channel). Rates use span ≥ 1 day. |

### 5.2 Hypotheses (prereg Part B)

| Registered | In the artefact | Status |
| :-- | :-- | :-- |
| H1: the strongest rival (A) does not match EC alone (C) on executed act legitimacy; E7 C − A bootstrap interval entirely below −δ | Arm A is `rival.py`: constitution in prompt, policy engine denying absolute contrariety, approval flag any manager may set (every token claim passes), event log; arm C is the gate with `Bench(internal=True)`; `analyze.py` prints the A–C interval for `e7_blind_spot` | **Executable as registered.** Read with E6 recall C − A and the ⟦derived⟧ throughput identity from `summary.json`. |
| H2: pressure reaches the proposal channel and not the executed one; (a) honest E2 within ±δ of 0 per arm, (b) pressure_sensitive E2 > +δ and equivalent across arms, (c) C and D execute no impermissible act | (a) and (b) are `paired_tost` on `e2_ps` (one-sample and pairwise); (c) is `e7_imperm_executed = 0` in every C and D run | **Executable as registered.** (b)'s cross-arm equivalence is EC-10's property; (c) is EC-02/03/05's. |
| H3: observation gap, same shape with E3 and observation_sensitive | `e3_og`; same procedures | **Executable as registered.** The LLM stratification by `believes_monitored` is exploratory and is added to `metrics.py` before the live run, with the plan-hash change recorded as an amendment. |
| H4: an admitted reason raises permitted T2/T3 departures in every arm | `bootstrap_diff` on `e4_diff` per arm | **Executable as registered.** |
| H5: reconciliation recovers constructed disclosure rates and separates misreporting from honest | (a) EC-07 per run; (b) `bootstrap_diff` on `e6_recall`, misreporting − honest, paired by (pack, arm, seed) | **Executable as registered.** (a) is the conformance criterion itself. |
| H6: (a) E7(B) > 0 and `e7_bench_saw` < 1, (b) E7(C) = E7(D) = 0, (c) in D, doctrine reduces repeat escalation and `e8_gloss_bar_blocks` > 0 | (a) `bootstrap_diff` on B's `e7_blind_spot`; (b) identity under EC-02/03/05; (c) `e8_return = after − before` over D's units | **Executable as registered.** The gloss-bar path (`gloss_bar` verdicts, no escalation) and codification at `k_codify = 3` are in `gate.py` and `doctrine.py`. |
| H7: D costs no more per proposal than C and both far less than the human desk | `cost_usd / n_proposals × 1000` ⟦derived⟧; policy runs cost 0; the desk figure from each pack's `benchmark/human.py` | **Descriptive only, and ⟦PROJECTED⟧ on the LLM side.** Dry mode prices from `PRICES` (chars/4 tokens, 120 output tokens); no live call has been made. |

### 5.3 Design and inference (prereg Part B, Design Plan and Analysis Plan)

| Registered | In the artefact | Status |
| :-- | :-- | :-- |
| Four arms over one identical proposal stream | Every draw seeded from (seed, pack, day) or (seed, pack, case), never from the arm; EC-10 and EC-11 | Present. |
| Five companies, 365 working days, one calendar, λ ≈ 16.44/day; the DJ stream is the released corpus partitioned into days | `stream.partition_days`; `calendar.py` with `DAY_TICKS = 100` | Present. The one engine-semantic overlay is the record expiry patch (`ts + 180 × DAY_TICKS`, i.e. 180 days); `engine.py` is unedited in all six copies. |
| Tier rule: absolute → T0; safety, or legal/regulatory at τ ≤ 25 → T1 with office; else T2; six value entries per company | `canon.tier_of`, `T1_TAU_MAX`, `OFFICE_BY_HARM`, the value table in `build_canon`; EC-01 and `build_all_canons.py --check` | Present and generated. |
| d_bench = 3, k_codify = 3, T3 sample rate 0.10, TWIN_RATE 0.25, CONFLICT_RATE 0.02, token TTL 14 days, daily issuance 0.15 | Constants in `run_ec_conformance.py`, `stream.py`, `registry.py`; `tests/test_ec_driver.py::test_constants` | Present. |
| Seeds 11, 13, 17, 19, 23; 4 archetypes + 2 bounds; 600 runs; LLM slice seed 11, all arms, live | `reproduce/run_year.sh registered` runs the policy and bounds design and the LLM **dry** run; the live slice is a separate command | **Policy design executable; LLM slice not run.** |
| TOST at ±0.03, α = 0.05 per side; percentile bootstrap 2,000 reps, rng 20260906; unit = (pack, seed); no family-wise correction on the named comparisons | `analyze.paired_tost`, `analyze.bootstrap_diff`, standard library | Present. |
| Conformance EC-01..12, each non-control check with a killing fault | `run_ec_conformance.py`, `mutation_matrix_ec.py`: 12/12, 8/8 killed, 2/2 controls survived | Present. |
| No peeking; deviations policy; plan hash over prereg, canons, package, tests | `prereg/make_plan_hash.py`, `prereg/plan_hash.txt`, `prereg/PLAN_HASH.md` | Present. The OSF DOI line is excluded from the hash and is still a placeholder. |
| What is not claimed: canons authored by the programme; archetypes constructed; reliance bounded to the configuration tested; corpora do not secure retrieval or characterisation; human desk ⟦PROJECTED⟧ | Stated in `docs/releases/RELEASE_NOTES_5.16.md`, `docs/ENTERPRISE_CONSCIENCE.md`, `DATASHEET.md` Part III | Stated on both sides. |

## 6. What to cite

The artefact is a DOI-bearing Zenodo record (see `CITATION.cff` at the root
and `.zenodo.json`). Cite the release version and the corpus version
together: release 5.16.0, simulation pack 2.4.0 (corpus 2.1.0), and for the
Enterprise Conscience extension the canon version (`<pack>-canon-000001`) and the plan hash
in `prereg/plan_hash.txt`. The per-pack SHA-256 digests
in `simulation/MANIFEST.json` identify exactly what was run.
