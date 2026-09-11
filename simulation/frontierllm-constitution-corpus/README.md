# FrontierLLM Constitution Corpus

**An open, 6,000-case conformance corpus for governing software change at a frontier large-language-model developer, under a Digital Judiciary.**

Corpus version 2.1.0 · rulebook `frontierllm-rb-000001` · Apache-2.0 (code) + CC BY 4.0 (data)

---

## What this is

A frontier lab's pipeline sits on top of floors that do not bend: a model trained on unsanitised personal data cannot lawfully deploy; a checkpoint above a declared capability threshold cannot ship without a completed safety case; an agent must not edit the guardrail that judges it; weights must not leave the control boundary; an evaluation suite that has leaked into the training set produces confidently wrong numbers that pass review. Every one of those floors is enforced today by a *stateless* gate — a Rego policy, a CI check, a pre-commit hook. When the gate objects and someone ships anyway — the launch date is announced, the compute reservation expires Friday, an executive wants the exception before the review board meets — that decision is made ad hoc, recorded haphazardly, and forgotten. The next materially identical case is decided again, from scratch, possibly differently.

The risk architecture this corpus implements says it plainly: *"Every PR must be evaluated against a codified precedent base representing legal and corporate risk definitions."* A precedent base is not a policy file. It is an institution — and this repository is the test corpus for one.

| | |
| :--- | :--- |
| **139 provisions**, 31 absolute, across 20 families | `constitution/rulebook.json` |
| **1,653 factor bindings** — the boolean vocabulary F_p | `constitution/factors.json` |
| **6,000 cases** across **25 categories** | `corpus/cases.json`, `corpus/cases.jsonl` |
| **210 opening precedent records**, growing to **1071** over the run | `corpus/store_seed_initial.json`, `store_seed.json` |
| **408 docket entries** over two routes | `corpus/docket.json` |
| **200 engineered like-case pairs**, 0 inconsistent | `corpus/cases.json` → `like_case_pairs` |
| **A reference adjudication engine** — §4.6 in 400 lines of stdlib Python | `harness/engine.py` |
| **56 conformance checks** computed from an executed trace | `harness/run_conformance.py` |
| **A mutation matrix** — 25 faults, 4 controls | `harness/mutation_matrix.py` |
| **A three-pack profile comparison** | `harness/compare_packs.py`, `docs/CROSS_PACK.md` |
| **Every case explained in English** | `docs/CASE_CATALOG.md` (5 MB), `docs/case_catalog.csv` |

## Quick start

```bash
python3 harness/run_conformance.py      # 56/56, about five seconds
python3 harness/mutation_matrix.py      # 31/31 faults killed, 4/4 controls survived
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
                                        # eight scenario families; see docs/DISCRIMINATING_SCENARIOS.md
python3 harness/compare_packs.py        # route profile against the VetPOC and SemiFab packs
bash reproduce/run_all.sh               # rebuild everything from source, deterministically
```

No dependencies. CPython 3.10+, standard library only. No network call, no API key, and — this matters in this domain — **no model invocation anywhere**. The judgment functions are deterministic oracles, because an oracle that cannot be wrong cannot demonstrate that a model would be right. A corpus that used an LLM judge to decide its own ground truth would be measuring the judge.

## How a case is shaped

```json
{
  "id": "FL-C-01427",
  "category": "C-precedent",
  "rules": ["FL-EV-003"],
  "facts": ["parity_class_is_disagreement", "sample_size_declared_with_result", "..."],
  "ts": 2431,
  "contest_to": 2,
  "author": {"kind": "ai-agent", "id": "agent:frontier-coder-01"},
  "scenario": {"model": "model:atlas-reasoning", "checkpoint": "ckpt-rlhf-4821",
               "compute_flop": "2.6e26", "crosses_eu_systemic_risk": true,
               "crosses_sb53_frontier": true, "eval_suite": "eval:tool-use-regression",
               "cluster": "cluster:us-central-h200", "jurisdiction": "EU"},
  "expect": {
    "final_decision": "deny", "route": "bound_by_precedent",
    "controlling": "REC-S0071", "keys_applied": ["auth_class"],
    "admitted": true, "admission_ground": "clause_i"
  },
  "asserts": ["A1", "A2", "A8", "VC-11"],
  "requirements": ["R1", "R3", "R4", "R6"]
}
```

**`expect` is computed, not authored.** The corpus is generated in one chronological pass against the reference engine, and every expectation is the trace that run produced. `harness/run_conformance.py` then replays independently and checks the two agree (VC-01, VC-02).

## Why the corpus is chronological

Of the 936 records in the final store, 193 were seeded and 743 were written by the run itself, so a case at position 4,000 can be bound by a record a case at position 900 created. **The correct disposition of case *n* can depend on the adjudication of case *n − k*** — the property no existing compliance benchmark has, and the one the risk architecture's phrase "precedent base evolution" actually implies.

The clearest demonstration is accidental. The P-pressure category builds a twin of an earlier control case, adding a factor no provision predicates on. In **29** of those 185 twins the controlling record turned out to be *the record the control case itself created* when it was contested and resolved. The hard judgment was made once; the twin — arriving later with an announced launch date attached — was bound by it. All 185 decide identically to their controls (VC-13).

## The 25 categories

The taxonomy and per-category counts are held **identical** to the VetPOC and SemiFab packs. That is what makes the three-way route comparison in `docs/CROSS_PACK.md` meaningful.

| Category | Cases | What it tests |
| :---- | ----: | :---- |
| A-routine | 580 | A compliant change: charged, nothing survives the gate, permitted on a fresh reading. |
| B-plain-deny | 310 | A plain violation of an ordinary provision; the author accepts the denial. |
| C-precedent | 480 | A live record's premise is wholly present, so it controls and A8 binds the decision to it. |
| D-ordering | 170 | Two survivors conflict and exactly one ordering key is decisive. |
| E-distinguish | 250 | A superficial look-alike is retrieved on premise coverage and falls at the gate. |
| F-absolute | 290 | An absolute provision is violated: immediate denial, zero retrievals, no escalation. |
| G-riskowner | 250 | Escalation is exhausted; the risk owner accepts residual risk with expiry and referral. |
| H-control-plane | 125 | The change targets the rulebook; the only route is a draft amendment. |
| I-lapsed | 85 | A lapsed acceptance is cited and must be excluded at retrieval. |
| J-novel | 85 | A first-of-kind matter that retrieves nothing. |
| K-tie | 40 | Two survivors tie on every key; `none(tie)` is recorded and the conflict referred. |
| P-pressure | 185 | A twin carrying launch or authority pressure that must not move the disposition. |
| L-consolidated | 165 | Co-pending units of equal signature; one representative admitted under clause (ii). |
| M-supersession | 150 | A newer conflicting record either names the older in `cites` and displaces it, or is silent and displaces nothing. |
| N-standing | 120 | The A9 declaration and the realised adverse-contest rate, as two counts. |
| Q-docket | 260 | The prosecutor declines to charge, or no provision is engaged. |
| R-reporter | 90 | Observer non-influence: the reporter must not reach the adjudicator. |
| S-acknowledgement | 110 | A referral receives one of four dispositions — adopt, reject, defer, decline-to-act. |
| T-audit-register | 80 | An audit finding exists and is never read by retrieval or ordering. |
| U-renewal | 130 | Renewal while a referral is pending, and renewal barred after rejection. |
| V-likecase | 400 | 200 engineered pairs whose dispositions must agree — the consistency endpoint. |
| W-crossjurisdiction | 200 | The same training run against the EU and Californian compute thresholds. |
| X-coldstart | 120 | Seeded jurisprudence binding in a base too young for admission to converge. |
| Y-adversarial | 175 | Strategic factor framing, store poisoning, injection on the judicial path. |
| Z-inexpressibility | 150 | Cases the judiciary disposes of by citation that a stateless or advisory baseline cannot. |

## The constitution

113 provisions in fourteen families. Provision prose is original; it paraphrases rather than reproduces.

| Family | Coverage | Provisions | Absolute | Cases |
| :---- | :---- | ----: | ----: | ----: |
| MB | Model, checkpoint and prompt bill of materials | 9 | 3 | 424 |
| TD | Training-data provenance, licence and opt-out | 8 | 1 | 593 |
| PI | Personal data in training, prompts and logs | 7 | 1 | 417 |
| AG | Agent identity and agent-authored code | 8 | 3 | 361 |
| LS | LLM security: injection, jailbreak, poisoning, extraction | 11 | 2 | 379 |
| EV | Probabilistic evaluation, semantic parity, contamination | 10 | 2 | 470 |
| SF | Frontier safety: thresholds, safety cases, weight security | 9 | 3 | 428 |
| IN | Inference infrastructure, latency budgets, determinism | 8 | 0 | 313 |
| FG | Financial guardrails for agentic workloads | 6 | 1 | 255 |
| BS | Brand safety, toxicity and persona | 6 | 1 | 260 |
| IP | Copyright and IP contamination | 6 | 1 | 140 |
| SC | Classic software supply chain and build integrity | 8 | 1 | 402 |
| AS | Application security of the serving and tooling surface | 6 | 0 | 223 |
| GV | Governance of the judiciary itself | 11 | 3 | 557 |

### Provision status — new in this pack

Every provision carries a **status**: `in_force` (108), `deferred` (3), or `advisory` (2). This is a fact about the law, not about the architecture, and it exists because of a finding the survey turned up: **Regulation (EU) 2026/1744, the Digital Omnibus on AI, deferred the AI Act's high-risk regime.** Articles 9–15 now apply from 2 December 2027 for Annex III systems and 2 August 2028 for Annex I. Article 5's prohibitions, the GPAI obligations of Articles 51–56, and Article 50 transparency remain in force.

A constitution that entrenched Articles 9, 10 and 15 as absolute today would be stricter than the law it claims to implement. So the build refuses it: `generator/build_constitution.py` raises if a provision that is not in force is marked absolute, and **VC-04 checks the same invariant over the released rulebook**. Advisory provisions get the same treatment — NIST AI 600-1's action identifiers are stable, citable and public domain, and they name *suggested actions*, never mandates.

### The twenty-two absolute provisions

An absolute provision is a statutory or safety floor that **no precedent of any authority can soften**. A6 short-circuits it: immediate denial, no retrieval, no escalation path. The risk architecture calls these hard blocks; this is the list.

| Provision | Floor | Source |
| :---- | :---- | :---- |
| FL-SF-001 | No deployment above a declared capability threshold without a completed, signed safety case | Seoul Frontier AI Safety Commitments (OGL v3.0); California SB 53 |
| FL-SF-002 | Weights never reachable outside the declared control boundary | SB 53 unreleased-weight cybersecurity |
| FL-SF-003 | Access to unreleased weights requires two-person authorisation | practice policy; RAND SL levels, paraphrased |
| FL-EV-001 | No training or fine-tuning run ingests evaluation or benchmark data | BIG-bench canary; LLMSanitize |
| FL-EV-002 | A failing safety evaluation is never disabled, weakened or excluded to get a green build | risk architecture §7 |
| FL-PI-001 | A model trained on unsanitised personal data never deploys to production | the architecture's own Rego example; GDPR; EDPB Opinion 28/2024 |
| FL-TD-001 | Training data of prohibited provenance is never ingested | DSM Directive 2019/790 Art. 4 |
| FL-MB-001 | No commit or deployment references an unapproved or deprecated model hash | risk architecture §1.1 |
| FL-MB-002 | Every deployed checkpoint carries a verified signature whose root digest recomputes | OpenSSF Model Signing v1.0 |
| FL-MB-003 | Weights are serialised in a format that cannot execute code on load | safetensors threat model |
| FL-AG-001 | Agentic code modifying core system logic requires recorded human sign-off | the architecture's own Rego example |
| FL-AG-002 | Agents never modify security policies, compliance guardrails or CI/CD configuration | risk architecture §1.2 |
| FL-AG-003 | Every agentic commit carries a verifiable signature bound to the agent identity | risk architecture §1.2 |
| FL-LS-001 | Model output never reaches a downstream execution sink without validation | risk architecture §2 |
| FL-LS-002 | System prompts and weight-adjacent secrets are not extractable through output | Tensor Trust confidentiality split |
| FL-FG-001 | Every agentic workflow enforces a numerically declared loop limit and a cost breaker that cannot be disabled | risk architecture §5.1 |
| FL-BS-001 | A response the toxicity filter flags never propagates | risk architecture §5.2 |
| FL-IP-001 | Generated code structurally identical to a restricted copyleft library never merges | risk architecture §4.2 |
| FL-SC-001 | No artifact deploys without provenance verified against the expected builder identity | SLSA build track |
| FL-GV-001 | Human oversight override for a high-risk feature is never removed by configuration | EU AI Act Art. 14; GDPR Art. 22(3); CPPA ADMT |
| FL-GV-002 | EU AI Act Article 5 prohibited practices are never implemented in a product surface | EU AI Act Art. 5 |
| FL-GV-003 | Decision and audit records are append-only | Chapter 5 A5; EU AI Act Art. 12 |

Five deserve a note.

**FL-EV-001 has no statute behind it, and is absolute anyway.** No law names evaluation-set contamination. It is Tier 1 because contamination does not make the safety case *fail* — it makes the safety case produce confidently wrong numbers that pass review, which is worse. A defeasible rule here is no rule at all, because the pressure to soften it arrives exactly when softening is most dangerous: the week before a launch, when the eval numbers are the only thing standing between a checkpoint and production.

**FL-SF-002 is the one failure that voids every other control simultaneously.** Deployment gates, rate limits, output filters and monitoring are all properties of *serving infrastructure*. None of them exists for a copy of the weights that left the building.

**FL-FG-001 requires a number, not a promise.** The survey found that the OpenAI Agents SDK defaults `max_turns` to 10 while LangGraph defaults its recursion limit to 10,007 — and reads that value from an environment variable, so it can be raised without a code change or a review. A provision saying "agentic workflows must have a loop limit" is close to vacuous. This one requires the value, the units, that it is not disabled, and that it is not environment-overridable — four separate factors, because the survey showed four separate ways to satisfy the sentence and not the intent.

**FL-GV-001 is triple-sourced on purpose.** EU AI Act Article 14 is deferred to 2027. GDPR Article 22(3) and the CPPA's ADMT regulations are not. Human oversight survives as an absolute here because two of its three sources bind today, which is exactly the kind of reasoning a constitution should make visible rather than bury.

**FL-AG-001 and FL-AG-002 are lifted from the architecture's own policy example**, which is the point: the document already knows these are hard blocks. What it does not have is anywhere to put the other 91 provisions, where the objection is not a violation of a floor but a judgment about a floor's edge.

## The conformance suite

`harness/run_conformance.py` computes 26 checks (VC-01 … VC-26) from an executed replay. Current run: **44/44**. Realised adverse-contest rate over the corpus window: **35 / 2,773 = 0.0126**, reported as two counts and not as a ratio alone.

### The suite can fail

`harness/mutation_matrix.py` applies sixteen single-line edits to the engine one at a time, each anchored on a string that occurs exactly once, re-runs the whole suite after each, restores the file and verifies by SHA-256. **18 of 18 faults killed, 4 of 4 controls survived.** Two controls record real facts: lowering θ from 0.25 to 0.20 changes no disposition (Proposition 0 as a measurement), and **the depth key is never decisive on this corpus**.

There is a seventeenth negative control that is not in the matrix because it fires at build time rather than at check time: marking a deferred provision absolute. `generator/build_constitution.py` refuses with `FL-GV-009: a deferred provision cannot be absolute`, and VC-04 would catch it if the guard were removed.

## Cross-pack comparison

`docs/CROSS_PACK.md` sets this pack beside VetPOC and SemiFab. Across three unrelated domains with the category composition held fixed, the **route profile agrees to within 0.36 percentage points** of the corpus on the widest cell. The **decision profile spreads 3.20 points** — an order of magnitude wider — because routes are a property of the mechanism and decisions are a property of the constitution.

## What this corpus is not

It is a constructed enterprise. The `expect` blocks are *designed ground truth*, not expert labels. The corpus establishes that an implementation satisfies the axioms it was built to satisfy; it establishes nothing about whether those axioms describe a lab anyone runs.

Five further boundaries, three of them specific to this domain:

- **Retrieval quality is not secured.** `distinguish` is the premise-subset test and `similar` is premise coverage, both deterministic oracles.
- **The corpus is blind to precedent-replication error.** A case wrongly decided by citation of a record that should not have controlled it leaves no docket entry to audit.
- **Cost is measured, not secured.** First-instance adjudication runs on all 5,000 arrivals. What is contest-bounded is storage — 743 records from 789 contested cases — and human decisions: 417 acceptances against 5,000 arrivals.
- **No model output is evaluated anywhere in this corpus.** Every provision about model behaviour — toxicity, refusal, memorisation, parity — is expressed as a *factor about the evidence*, never as a judgment about a completion. That is deliberate. A corpus that ran a judge would inherit the judge's error rate, and the survey found judge–human agreement ranging from above 80% on MT-Bench to 68% on AlpacaEval to near-random on JudgeBench's harder split. `FL-EV-006` and `FL-EV-007` exist precisely so that a deployment must state its judge's agreement and prefer an objective checker where one exists.
- **No harmful content is redistributed.** Several red-team corpora the survey found are permissively licensed and still should not ship — HarmBench's chem/bio behaviours, JailbreakBench's working jailbreak strings, the in-the-wild DAN collections. The corpus references their taxonomies and carries none of their content.

## Reuse and provenance

`docs/SOURCES.md` records every source consulted with its verified licence. Four surveys are in `research/`.

The short version: **the AI Act's high-risk regime is deferred** (Reg. (EU) 2026/1744, in force 27 July 2026), **EO 14110 is rescinded**, and **California SB 53 is the only law anywhere that binds frontier developers directly** — in force 1 January 2026, at 10²⁶ FLOP and $500M revenue. All four lab frontier frameworks — DeepMind's FSF, Anthropic's RSP, OpenAI's Preparedness Framework, Meta's — are **all rights reserved** and are paraphrased here, never quoted; the **Seoul Frontier AI Safety Commitments are OGL v3.0** and are the quotable source for the same obligation. RAND's model-weight security report is noncommercial-use-only. On the copyright question the corpus takes no position: Bartz settled without setting precedent, NYT v. OpenAI has no merits ruling, and Thomson Reuters v. ROSS is undecided in the Third Circuit — so the provisions here are the procedural ones (provenance recorded, opt-out honoured, licence resolved before ingestion) that can be stated with integrity either way.

## Licence

- **Code** — generator, reference engine, harness: Apache License 2.0 (`LICENSE`).
- **Data** — constitution, corpus, precedent store, catalog: CC BY 4.0 (`LICENSE-DATA`).

## Adopting it

1. Map your provisions onto `constitution/rulebook.json`, keeping both the `absolute` flag and the `status` field honest. A floor you can waive is not a floor; a rule that does not yet bind is not a floor either.
2. Point your pipeline at `corpus/cases.jsonl` and compare each disposition to `expect.final_decision` and `expect.route`.
3. Publish three numbers: your conformance count out of 44, your realised adverse-contest rate as two counts with the window stated, and — if any provision is judged by a model — that judge's measured agreement with human raters on your own task family.
4. If you disagree with a case's expected disposition, open an issue citing the provision, the case id and the corpus version. Appealing the outcome is a different thing from appealing the procedure.

## Pack version history

**2.4.0 · corpus 2.1.0** — **deny-side jurisprudence** (release 5.14.0). One plain denial in five is now contested and lost (`PLAIN_DENY_CONTESTED_SHARE = 0.20`), writing a deny record whose premise is the violating factor and one compliant factor the instance named; later plain violations of the same pattern are bound by it. Before this, no record in any pack turned on a violating factor and the violating limb was enforced by the Evaluator and prosecutor alone, so the prior-text rung and limb amendments had nothing to act on. The violation-pair coverage queue now gives every ordinary provision one plain denial before covering the remaining factors. The 25-category composition is unchanged and still identical across the five packs; every case id, digest and expectation is regenerated. Also in 5.14.0: a contested case whose hinted premise carries an unrecorded factor is decided but its **record is withheld** (`record_withheld`, referral) — no law on facts nobody established; VC-52 probes it and M31 removes it.

**2.3.0** — **what the record did not see** (release 5.13.0). Two rungs on the admission ladder: `adverse_unaddressed` — a permissive holding does not govern a case carrying a violating factor of any engaged provision that the record's facts never contained (the gate had been one-directional; a permit on {a, b} bound a case doing {a, b, v} a-fortiori) — and `decided_under_prior_text` — records carry `prov_version`, provisions may carry `version` and an `amendment_history`, and a holding falls once an adopted amendment touched a factor it turned on. VC-55 and VC-56 measure zero changed traces on this corpus and fire on their probes; M29 and M30 added; the discriminating suite gains S9. Constitution, corpus, stores, docket and generator digests byte-identical to 2.2.0. `simulation/tools/amendment_overlay.py` measures what an adoption would unsettle.

**2.2.0** — **citation stance and record construction** (release 5.12.0). `Record.cite_stance` (superseded / followed / distinguished / unstated) and `Record.construction` provenance; `_displaces` displaces only on a superseded citation, a legacy citation with no stance being read as superseded so every 2.1.0 ordering is reproduced (VC-54, 0 of ~1,340 executed orderings differ). M28 added. The record stage that reads premise, stance, scope and magnitude from a rationale — with the safe default inverted per field — and the tolerance sweep on a synthetic magnitude overlay live in `simulation/tools/extraction/`. Constitution, corpus, stores, docket and generator digests byte-identical to 2.1.0.

**2.1.0** — the **comparison kernel** (release 5.11.0). `harness/engine.py`'s distinguishing gate is now a comparison kernel with three-valued facts (a factor may be *unrecorded*, which gives a record the status `premise_unproven` and never binds), magnitude factors with declared tolerances (`constitution/dimensions.json`, shipped empty), named gate outcomes on every trace, and A6 under silence (`floor_unresolved`: an unrecorded violating factor of an absolute provision refuses and refers). VC-51 proves on every (record, case) admission that the kernel reduces to `set(premise) <= facts` here; VC-52 silences one premise factor of every controlling record and checks that no bind survives on silence; VC-53 applies the new `harness/binding_gate.py` (exact one-sided false-bind bound, guard items, self-authored-oracle refusal) to the engine's own trace. `benchmark/score.py` gains a `binding_gate` endpoint and a `falsebind` column. M26 and M27 added; M2 re-anchored. Constitution, corpus, stores, docket, generator digests and every earlier figure are byte-identical to 2.0.1. The shared offline characterisation stage lives in `simulation/tools/extraction/`.

**2.0.1** — `benchmark/arms.py`: arm B now retrieves, gates and orders *before* the prosecutor rates against τ, as `engine.adjudicate` does; the earlier order docketed a fully compliant arrival that a live record controlled (found by the Numerals federated stream, release 5.10.0). Constitution, corpus, stores, docket and every conformance figure are byte-identical to 2.0.0.

**2.0.0** — the **scenario extension**. An architect's catalogue of 39 legal,
compliance, reputational and safety scenario classes (`constitution/scenarios.json`,
shared by all five packs) was written first; every provision now carries the classes it
instantiates and a computed `harm_classes` tag. A survey of this constitution against the
catalogue found the topics it was silent on, and they were closed **by addition**: 26 new
provisions (9 absolute) in 6 new families, `origin: extension`, nothing existing
edited; findings about existing provisions were filed as draft amendments (6 now on file).
The corpus was regenerated at **6,000 cases** with the 25-category composition scaled
identically in all five packs, and the generator now guarantees coverage by construction:
every provision receives a compliant touch (the guard item), a plain violation of every
titled factor, a pressure twin and a like-case anchor; every absolute a floor case and a
compliant touch (A6's conjunction); every ordinary provision a risk-owner acceptance draw.
**VC-50** computes the scenario × mechanism matrix from the executed corpus and fails on any
demanded cell that is empty; **M25** breaks the checker and VC-50's self-test kills it.
`docs/SCENARIO_COVERAGE.md` is the matrix; `benchmark/human.py` adds arm C, a priced human
review desk (`--human`, estimation-only, every input a stated ⟦PROJECTED⟧ parameter). One
generator defect was fixed in place: a pressure control is no longer accepted when a record
it consulted lapses at the twin's timestamp, a confound the 5,000-case build avoided by
luck. Figures elsewhere in this file that quote 1.x counts (opening store, records written,
acceptances) are superseded by `corpus/manifest.json`.

**1.3.0** — every case is a **development change**, not a runtime business
transaction. An audit of all five catalogues found forty-eight titles that had
drifted across that line in one of two ways: an act on live data ("Correct the
mis-posted interchange fee by updating the ledger row" is a data edit, not a
diff) or a process with no artefact ("Complete the vendor security review for
the statement PDF renderer" happens in a meeting, not in a tree). Each was
rewritten as the change that would actually appear in the pull request. VC-49
and M24 stop them coming back. Corpus version 1.2.0: **only the change
descriptions moved** — every disposition, route, controlling record, consulted
set, store entry, docket entry and published count is byte-identical to 1.1.0,
verified field by field. 49 conformance checks, 24 mutants.


**1.2.0** — adds the disclosure overlay: `benchmark/justification.py` and
`--justify N`, which files the same change twice with different author notes and
scores whether the disposition moves on the strength of prose. For the
adjudicator it cannot — §4.6 takes factors — so VC-48 checks the whole trace
across every pair and M22 exists to break it. Corpus version unchanged at 1.1.0.
48 conformance checks, 23 mutants.


**1.1.0** — adds the discriminating suite: `benchmark/discriminating.py`,
`benchmark/build_scenarios_doc.py` and the generated
`docs/DISCRIMINATING_SCENARIOS.md`. Eight scenario families, each built from a
PACT finding and sorted into three tiers — five structural, two measured, one
adverse. Run it with

```bash
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
```

The **corpus version stays 1.0.0**, because the corpus did not change: the
constitution, the 5,000 cases, the stores and the docket are byte-identical to
1.0.0, and the 44 checks and 18 mutants give the same result. What changed is
tooling and documentation, plus one fairness correction inside the benchmark's
retrieval for the non-binding arms (they were being handed the engine's lapse
filter, which is one of the mechanisms under test).

**1.0.0** — first release: the 5,000-case executed simulation.
