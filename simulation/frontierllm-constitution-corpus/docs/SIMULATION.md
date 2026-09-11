# FrontierLLM Constitution — the simulation, read end to end

Corpus 2.1.0 · rulebook frontierllm-rb-000001 · 6,000 proposed code changes · Apache-2.0 (code) + CC BY 4.0 (data)

## What this document is

This is the whole run in plain English. A simulated engineering organisation proposed five thousand code changes, one after another, and an adjudicator governed by a written constitution decided every one of them. Nothing here is an intention or a specification: every disposition below is what the reference engine actually did when the corpus was replayed, and the ledger at the end lists all five thousand changes with the answer each one got.

Read it as you would read a docket. The interesting part is not that the adjudicator said no to bad changes — a linter does that. It is that when a change was contested and resolved, the decision was written down, and the next materially identical change was **bound** by it.

## The firm and its constitution

An open constitution for frontier large-language-model development — pretraining, fine-tuning, evaluation, serving and agentic tooling — expressed as ordinary and absolute provisions in the sense of Chapter 5, Definition 1 of the Digital Judiciary programme. Provisions carry a status: in_force, deferred, or advisory. A provision that is not in force may never be absolute.

| | |
| :--- | ---: |
| Provisions | 139 |
| — of them absolute | 31 |
| Provision families | 20 |
| Opening precedent records | 210 |
| Records written during the run | 933 |
| Final store | 1143 |
| Retrieval threshold θ | 0.25 |


## The run in numbers

| The answer given | Changes |
| :--- | ---: |
| permitted | 3,656 |
| denied | 1,575 |
| permitted with conditions | 769 |

| How the answer was reached | Changes |
| :--- | ---: |
| decided fresh | 3,733 |
| bound by precedent | 1,188 |
| refused at the floor | 394 |
| docketed — not charged | 327 |
| decided fresh after a tie | 146 |
| disposed by citation | 131 |
| docketed — nothing engaged | 81 |

## How the run unfolded

The case base starts almost empty and grows only when a decision is contested and resolved above the first instance. That is the whole mechanism, and its consequence is visible in the run: early changes are mostly decided fresh, and later ones are increasingly decided by citing a decision the organisation already made.

| Fifth of the run | Changes | Bound by precedent | Share | New records | Refused at a floor |
| :--- | :--- | ---: | ---: | ---: | ---: |
| 1 | 1–1,200 | 191 | 15.9% | 195 | 88 |
| 2 | 1,201–2,400 | 511 | 42.6% | 177 | 49 |
| 3 | 2,401–3,600 | 273 | 22.8% | 181 | 81 |
| 4 | 3,601–4,800 | 113 | 9.4% | 185 | 77 |
| 5 | 4,801–6,000 | 100 | 8.3% | 195 | 99 |

Precedent goes from **15.9%** of changes in the first fifth to **8.3%** in the last. Nothing was tuned to produce that: it is what contest-gated admission does to a stream of changes over time.

## Twelve changes, read in full

One of each kind, taken from the run rather than chosen for effect — the first case of each category, whatever it happens to be.

### FL-A-00008 — *Backfill lineage records for the older quantised checkpoints*

**Why this kind of change is in the run.** An ordinary change that engages a provision and breaks nothing.

**What it touched.** The model registry in the release area, filed by a named engineer. It engaged `FL-MB-008`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### FL-B-00004 — *Accept attestations from the personal runner that built the hotfix*

**Why this kind of change is in the run.** An unarguable violation nobody contests.

**What it touched.** The api gateway in the gateway area, filed by a named engineer. It engaged `FL-SC-003`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### FL-C-00941 — *Record the capability-threshold determination on the release record*

**Why this kind of change is in the run.** The case that makes this a judiciary: a prior decision controls.

**What it touched.** The checkpoint signer in the training area, filed by an AI coding agent. It engaged `FL-SF-005`.

**What happened.** The change was bound by precedent and permitted with conditions, controlled by record `REC-FL-G-00920`. Nothing was stored: the decision is final and leaves no precedent.

### FL-E-00005 — *Quarantine ticket text before it reaches the agent's instruction slot*

**Why this kind of change is in the run.** The near-miss the system must refuse to follow.

**What it touched.** The experiment tracker in the experiments area, filed by a named engineer. It engaged `FL-AG-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### FL-D-00078 — *Record the tolerance band used for each accuracy comparison*

**Why this kind of change is in the run.** Two prior decisions disagree and one ordering key decides.

**What it touched.** The experiment tracker in the experiments area, filed by an AI coding agent. It engaged `FL-EV-010`.

**What happened.** The change was bound by precedent and denied, controlled by record `REC-S0135`. Nothing was stored: the decision is final and leaves no precedent.

### FL-F-00002 — *Promote the checkpoint that recites whole published chapters on request*

**Why this kind of change is in the run.** A floor: refused before any retrieval happens.

**What it touched.** The training corpus builder in the data-pipeline area, filed by an AI coding agent. It engaged `FL-IP-001`, `FL-GV-007`.

**What happened.** The change was refused at the floor. Nothing was stored: the decision is final and leaves no precedent.

### FL-G-00007 — *Require the safety-case signature from outside the authoring team*

**Why this kind of change is in the run.** The automated tiers are exhausted and a named human accepts the risk.

**What it touched.** The training orchestrator in the release area, filed by an AI coding agent. It engaged `FL-SF-007`.

**What happened.** The change was decided fresh and permitted with conditions; escalation was exhausted and the named risk owner accepted the residual risk. The decision was written into the case base and binds later materially identical changes.

### FL-H-00032 — *Flip the data-provenance floor from absolute to ordinary in policy metadata*

**Why this kind of change is in the run.** A change to the rulebook itself, routed to an amendment.

**What it touched.** The inference engine in the platform area, filed by an AI coding agent. It engaged `FL-LS-003`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### FL-K-00202 — *Embed the canary string in every generated evaluation case*

**Why this kind of change is in the run.** Two records tie on every key and the trail says so.

**What it touched.** The experiment tracker in the release area, filed by an AI coding agent. It engaged `FL-EV-006`.

**What happened.** The change was decided fresh after a tie and permitted, controlled by record `none_tie`, with the trail recording none(tie) rather than an absence of authority. Nothing was stored: the decision is final and leaves no precedent.

### FL-P-00017 — *Require two-person authorisation for unreleased-weight access*

**Why this kind of change is in the run.** The twin of a control case, carrying a pressure argument.

**What it touched.** The checkpoint signer in the org area, filed by a named engineer. It engaged `FL-SF-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### FL-L-00098 — *Separate the production prompt label from its version string*

**Why this kind of change is in the run.** Co-pending changes decided once and cited.

**What it touched.** The model registry in the weights-infra area, filed by an AI coding agent. It engaged `FL-MB-007`.

**What happened.** The change was decided fresh and permitted. The decision was written into the case base and binds later materially identical changes.

### FL-I-00010 — *Route flagged responses to the block path rather than a warning*

**Why this kind of change is in the run.** An expired acceptance is cited and must not be followed.

**What it touched.** The eval harness in the experiments area, filed by a named engineer. It engaged `FL-BS-004`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

## What happened to each kind of change

| Kind of change | Changes | Permitted | Denied | With conditions | Bound by precedent | Became precedent |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A-routine | 696 | 696 | 0 | 0 | 0 | 82 |
| B-plain-deny | 372 | 0 | 372 | 0 | 2 | 71 |
| C-precedent | 576 | 263 | 203 | 110 | 576 | 144 |
| D-ordering | 204 | 59 | 73 | 72 | 204 | 0 |
| E-distinguish | 300 | 300 | 0 | 0 | 0 | 0 |
| F-absolute | 348 | 0 | 348 | 0 | 0 | 0 |
| G-riskowner | 300 | 0 | 0 | 300 | 0 | 300 |
| H-control-plane | 150 | 0 | 150 | 0 | 0 | 0 |
| I-lapsed | 102 | 102 | 0 | 0 | 0 | 0 |
| J-novel | 102 | 102 | 0 | 0 | 0 | 0 |
| K-tie | 48 | 48 | 0 | 0 | 0 | 0 |
| P-pressure | 222 | 222 | 0 | 0 | 0 | 0 |
| L-consolidated | 198 | 198 | 0 | 0 | 0 | 67 |
| M-supersession | 180 | 98 | 82 | 0 | 82 | 0 |
| N-standing | 144 | 144 | 0 | 0 | 0 | 44 |
| Q-docket | 312 | 312 | 0 | 0 | 0 | 0 |
| R-reporter | 108 | 108 | 0 | 0 | 0 | 0 |
| S-acknowledgement | 132 | 0 | 0 | 132 | 0 | 132 |
| T-audit-register | 96 | 96 | 0 | 0 | 0 | 0 |
| U-renewal | 156 | 63 | 0 | 93 | 0 | 93 |
| V-likecase | 480 | 480 | 0 | 0 | 0 | 0 |
| W-crossjurisdiction | 240 | 127 | 113 | 0 | 0 | 0 |
| X-coldstart | 144 | 65 | 79 | 0 | 144 | 0 |
| Y-adversarial | 210 | 55 | 155 | 0 | 0 | 0 |
| Z-inexpressibility | 180 | 118 | 0 | 62 | 180 | 0 |

## The ledger — every change, and how it was treated

All five thousand, in the order they arrived. **Answer** is what the change got; **how** is the route that produced it; **controlling** names the record that decided it, where one did; **precedent** marks the changes whose decision entered the case base.

| # | Change | Engages | Answer | How | Controlling | Precedent |
| ---: | :--- | :--- | :--- | :--- | :--- | :-: |
| 1 | Redact prompt and completion logs before they reach retention | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 2 | Promote the checkpoint that recites whole published chapters on request | FL-IP-001 FL-GV-007 ⛔ | denied | refused at the floor | — |  |
| 3 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4 | Accept attestations from the personal runner that built the hotfix | FL-SC-003 | denied | decided fresh | — |  |
| 5 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-007 | permitted | decided fresh | — |  |
| 6 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-006 | permitted | decided fresh | — |  |
| 7 | Require the safety-case signature from outside the authoring team | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 8 | Backfill lineage records for the older quantised checkpoints | FL-MB-008 | permitted | decided fresh | — |  |
| 9 | Exempt agent-authored files from the licence scan to speed reviews | FL-IP-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 10 | Route flagged responses to the block path rather than a warning | FL-BS-004 | permitted | decided fresh | — |  |
| 11 | Route flagged responses to the block path rather than a warning | FL-BS-006 | permitted | decided fresh | — |  |
| 12 | Enable batch invariance before claiming bitwise replay | FL-IN-006 | permitted | decided fresh | — |  |
| 13 | Record a disposition for every referral the board acknowledges | FL-GV-007 | permitted | decided fresh | — |  |
| 14 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 15 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 16 | Record the frontier framework version in force on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 17 | Require two-person authorisation for unreleased-weight access | FL-SF-007 | permitted | decided fresh | — |  |
| 18 | Parameterise the new experiment-metrics filter queries | FL-AS-003 | permitted | docketed — not charged | — |  |
| 19 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 20 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | decided fresh | — | ● |
| 21 | Write a docket entry for every arrival that is not charged | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 22 | Skip signature verification on load to cut startup time | FL-MB-002 ⛔ | denied | refused at the floor | — |  |
| 23 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted | decided fresh | — |  |
| 24 | Drop the failing refusal suite from the promotion gate this train | FL-EV-001 FL-SC-004 ⛔ | denied | refused at the floor | — |  |
| 25 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 26 | Report preemption counts in the load-test summary | FL-IN-002 | permitted | decided fresh | — |  |
| 27 | Record the frontier framework version in force on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 28 | Attach Croissant metadata to the new publisher corpus | FL-TD-004 | permitted | decided fresh | — |  |
| 29 | Deploy the model line before the transparency report is published | FL-TR-002 | denied | decided fresh | — |  |
| 30 | Redact prompt and completion logs before they reach retention | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 31 | Fail the merge when the scanner reports an unresolved licence | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 32 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-LS-003 | denied | decided fresh | — |  |
| 33 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 34 | Justify the two remaining special-category fields on the dataset record | FL-PI-003 | permitted | decided fresh | — | ● |
| 35 | Restrict agent outbound calls to the allowlisted host set | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 36 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-PV-001 | denied | decided fresh | — |  |
| 37 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-006 | permitted | decided fresh | — |  |
| 38 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted | decided fresh | — |  |
| 39 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 40 | State the percentile on every latency claim in the dashboard | FL-IN-005 | permitted | decided fresh | — |  |
| 41 | Add a weekly sampling job over production refusals | FL-BS-004 | permitted | decided fresh | — |  |
| 42 | Give the coding agent its own short-lived signing credential | FL-AG-007 | permitted | decided fresh | — |  |
| 43 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted | decided fresh | — |  |
| 44 | Re-pin the batch scorer to the retired atlas-base hash | FL-MB-001 FL-EV-007 ⛔ | denied | refused at the floor | — |  |
| 45 | Reduce the eval harness's flakiness by retrying failed probe runs up to twice | FL-CB-002 | permitted | decided fresh | — |  |
| 46 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-002 | permitted | decided fresh | — |  |
| 47 | Record the tolerance band used for each accuracy comparison | FL-EV-009 | permitted | decided fresh | — |  |
| 48 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-006 | permitted | decided fresh | — |  |
| 49 | Record the compute-threshold determination separately per jurisdiction | FL-GV-011 | permitted | decided fresh | — |  |
| 50 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-006 | permitted | decided fresh | — |  |
| 51 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-006 | permitted | decided fresh | — |  |
| 52 | Write a docket entry for every arrival that is not charged | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 53 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-003 | permitted | decided fresh | — |  |
| 54 | Block internal address ranges in the web-fetch tool | FL-AS-004 | permitted | docketed — not charged | — |  |
| 55 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | decided fresh | — |  |
| 56 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — |  |
| 57 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — |  |
| 58 | Sample the abuse-monitoring pipeline at one percent to cut compute cost | FL-UH-004 | denied | decided fresh | — |  |
| 59 | Hold the audit register in a store the retrieval path cannot read | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 60 | Submit an amendment retiring the deferred data-governance clauses early | FL-EV-009 | denied | decided fresh | — |  |
| 61 | Keep cases released after the training cutoff in the holdout | FL-EV-003 | permitted | decided fresh | — | ● |
| 62 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-004 ⛔ | denied | refused at the floor | — |  |
| 63 | Move retrieved documents into a separate, clearly marked context block | FL-LS-007 | permitted | decided fresh | — |  |
| 64 | Attach Croissant metadata to the new publisher corpus | FL-TD-003 | permitted | decided fresh | — |  |
| 65 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-008 | permitted | docketed — not charged | — |  |
| 66 | Remove the cyber-offence eval from the promotion gate to speed up nightly builds | FL-CB-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 67 | Transfer the checkpoint to the partner cluster before classification is recorded | FL-WX-002 | denied | decided fresh | — |  |
| 68 | Raise mitigations to match the assessed capability level | FL-SF-009 | permitted | decided fresh | — |  |
| 69 | Block promotion until the dangerous-capability reports complete | FL-SF-009 | permitted | decided fresh | — |  |
| 70 | Gate promotion on the full safety suite, not the fast subset | FL-EV-008 | permitted | decided fresh | — |  |
| 71 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 72 | Keep cases released after the training cutoff in the holdout | FL-EV-005 | permitted | decided fresh | — |  |
| 73 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-001 FL-LS-003 ⛔ | denied | refused at the floor | — |  |
| 74 | Separate the audit register from the precedent store at schema level | FL-GV-009 | permitted | decided fresh | — |  |
| 75 | Strip annotator identity from the exported preference dataset | FL-PV-001 | permitted | decided fresh | — | ● |
| 76 | Embed the canary string in every generated evaluation case | FL-EV-003 | permitted | decided fresh | — |  |
| 77 | Pin the golden-prompt baseline to a commit digest | FL-EV-003 | permitted | decided fresh | — |  |
| 78 | Record the tolerance band used for each accuracy comparison | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 79 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | permitted with conditions | decided fresh | — | ● |
| 80 | Grant a new hire weight-store access before the vetting record clears | FL-WX-001 FL-EV-007 ⛔ | denied | refused at the floor | — |  |
| 81 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 82 | Ship the quantised build four points below the tolerance band | FL-EV-001 ⛔ | denied | refused at the floor | — |  |
| 83 | Move retrieved documents into a separate, clearly marked context block | FL-LS-006 | permitted | decided fresh | — |  |
| 84 | Scan responses for canary tokens before they leave the gateway | FL-LS-007 | permitted | decided fresh | — |  |
| 85 | Move retrieved documents into a separate, clearly marked context block | FL-LS-007 | permitted | decided fresh | — |  |
| 86 | Give the coding agent its own short-lived signing credential | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 87 | Report first-token and per-token latency against the tier budgets | FL-IN-006 | permitted | decided fresh | — |  |
| 88 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-003 | denied | decided fresh | — |  |
| 89 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 90 | Run agent-authored code only inside the sandboxed runner | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 91 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-TD-004 | denied | decided fresh | — |  |
| 92 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 93 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-003 | permitted | docketed — not charged | — |  |
| 94 | Add the new sampling library to the licence inventory | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 95 | Fail the build on scan findings above the severity threshold | FL-SC-006 | permitted with conditions | decided fresh | — | ● |
| 96 | Record the frontier framework version in force on the release record | FL-SF-008 | permitted | decided fresh | — | ● |
| 97 | Default unparsed licence strings to permissive so ingestion stops stalling | FL-TD-003 | denied | decided fresh | — |  |
| 98 | Separate the production prompt label from its version string | FL-MB-007 | permitted | decided fresh | — | ● |
| 99 | Block promotion until the dangerous-capability reports complete | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 100 | Let the next training run start before the unlearning exclusion list refreshes | FL-PV-001 | denied | decided fresh | — |  |
| 101 | Enable batch invariance before claiming bitwise replay | FL-IN-001 | permitted | decided fresh | — |  |
| 102 | Pin the key-value cache budget for the agentic serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 103 | Give every system prompt an immutable version identifier | FL-MB-006 | permitted | disposed by citation | — |  |
| 104 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 105 | Strip the notice file from the container image to shrink the layer | FL-IP-001 FL-CB-004 ⛔ | denied | refused at the floor | — |  |
| 106 | Auto-clear denied-party screening hits below a similarity threshold | FL-WX-004 FL-CB-002 ⛔ | denied | refused at the floor | — |  |
| 107 | Report first-token and per-token latency against the tier budgets | FL-IN-007 | permitted | docketed — not charged | — |  |
| 108 | Run the decontamination check over the new code corpus | FL-EV-005 | permitted | decided fresh | — |  |
| 109 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 110 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 111 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | decided fresh | — | ● |
| 112 | Carry attribution notices through to the shipped container image | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 113 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 114 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 115 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-002 | permitted | decided fresh | — |  |
| 116 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-002 | permitted | decided fresh | — |  |
| 117 | Pin the key-value cache budget for the agentic serving tier | FL-IN-006 | permitted | decided fresh | — |  |
| 118 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-001 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 119 | Hold goodput at the tier threshold under the burst profile | FL-IN-008 | permitted | docketed — not charged | — |  |
| 120 | Ship the quantised build four points below the tolerance band | FL-EV-010 | denied | decided fresh | — |  |
| 121 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 122 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-005 | permitted | decided fresh | — |  |
| 123 | Record the availability type on every newly onboarded source | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 124 | Add hash-list refresh monitoring to the training ingestion dashboard | FL-CS-003 | permitted | decided fresh | — |  |
| 125 | Turn off commit signing for the agent runner while its key rotates | FL-AG-001 FL-EV-009 ⛔ | denied | refused at the floor | — |  |
| 126 | Project token spend before dispatching a long-horizon agent run | FL-FG-004 | permitted | decided fresh | — |  |
| 127 | Move cost control from a meter to a pre-flight breaker | FL-FG-004 | permitted | decided fresh | — |  |
| 128 | Resolve internal packages from the private registry first | FL-SC-005 | permitted | decided fresh | — | ● |
| 129 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 130 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted | decided fresh | — |  |
| 131 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-003 | permitted | decided fresh | — |  |
| 132 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 133 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 134 | Block promotion until the dangerous-capability reports complete | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 135 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 136 | State turns rather than seconds as the loop-limit unit | FL-FG-005 | permitted with conditions | decided fresh | — | ● |
| 137 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-003 | denied | decided fresh | — |  |
| 138 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 139 | Publish the prompt-log retention clock in the customer portal | FL-PI-007 | permitted | decided fresh | — |  |
| 140 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-005 | permitted | decided fresh | — | ● |
| 141 | Enable batch invariance before claiming bitwise replay | FL-IN-002 | permitted | decided fresh | — |  |
| 142 | Publish a review checklist for agent changes to the eval harness | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 143 | Change the escalation ladder so an automated tier may accept frontier risk | FL-TD-006 | denied | decided fresh | — |  |
| 144 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 145 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 146 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-002 | denied | decided fresh | — |  |
| 147 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 148 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 149 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 150 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-004 | permitted | decided fresh | — |  |
| 151 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted | decided fresh | — |  |
| 152 | Add an incident-reporting path test against the statutory clock | FL-SF-004 | permitted | decided fresh | — |  |
| 153 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 154 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 155 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | disposed by citation | — |  |
| 156 | Let the mail agent follow instructions it finds in the message body | FL-LS-004 | denied | decided fresh | — |  |
| 157 | Paste the copyleft sampling routine into the hosted inference engine | FL-IP-001 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 158 | Fail closed when a dataset licence string does not parse | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 159 | Attach Croissant metadata to the new publisher corpus | FL-TD-003 | permitted | decided fresh | — |  |
| 160 | Parameterise the new experiment-metrics filter queries | FL-AS-003 | permitted | docketed — not charged | — |  |
| 161 | Parameterise the new experiment-metrics filter queries | FL-AS-006 | permitted | docketed — not charged | — |  |
| 162 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 FL-FG-003 ⛔ | denied | refused at the floor | — |  |
| 163 | Validate tenant scope on every portal export request | FL-AS-001 | permitted | decided fresh | — |  |
| 164 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 165 | Fail closed when a dataset licence string does not parse | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 166 | Scan responses for canary tokens before they leave the gateway | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 167 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 168 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — |  |
| 169 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-EV-004 | denied | decided fresh | — |  |
| 170 | Run release builds on ephemeral runners with pinned images | FL-SC-005 | permitted | decided fresh | — | ● |
| 171 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-001 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 172 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-004 | permitted | decided fresh | — |  |
| 173 | Report first-token and per-token latency against the tier budgets | FL-IN-001 | permitted | decided fresh | — |  |
| 174 | Run release builds on ephemeral runners with pinned images | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 175 | Require human confirmation before the agent executes a write tool | FL-LS-008 | permitted | decided fresh | — |  |
| 176 | Measure membership-inference advantage on the release candidate | FL-LS-008 | permitted | decided fresh | — |  |
| 177 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 178 | Remove the cache ceiling so long sessions stop being evicted | FL-IN-001 | denied | decided fresh | — |  |
| 179 | Raise mitigations to match the assessed capability level | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 180 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 181 | Escape tool output before it reaches the shell adapter | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 182 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted with conditions | decided fresh | — | ● |
| 183 | Separate the production prompt label from its version string | FL-MB-006 | permitted | decided fresh | — |  |
| 184 | Have the agent loosen the guardrail thresholds it kept tripping | FL-AG-006 | denied | decided fresh | — |  |
| 185 | Ship the research agent with no turn limit in its configuration | FL-FG-001 FL-PV-002 ⛔ | denied | refused at the floor | — |  |
| 186 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 187 | Check the code-signing extended key usage on the release chain | FL-MB-004 | permitted | disposed by citation | — |  |
| 188 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh | — |  |
| 189 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-004 | permitted | decided fresh | — |  |
| 190 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-001 ⛔ | denied | refused at the floor | — |  |
| 191 | Require a human reviewer on agent changes to request routing | FL-AG-008 | permitted | decided fresh | — |  |
| 192 | Verify de-identification by sampling rather than by assertion | FL-PI-007 | permitted | decided fresh | — |  |
| 193 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-007 | permitted | disposed by citation | — |  |
| 194 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-010 | permitted | decided fresh | — |  |
| 195 | Enforce the instruction and data boundary on the retrieval path | FL-LS-011 | permitted | decided fresh | — |  |
| 196 | Enforce the instruction and data boundary on the retrieval path | FL-LS-008 | permitted | decided fresh | — |  |
| 197 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-003 | permitted | decided fresh | — |  |
| 198 | Enforce server-side authorization on the new batch endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 199 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | decided fresh | — | ● |
| 200 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-002 | permitted | decided fresh | — |  |
| 201 | Strip annotator identity from the exported preference dataset | FL-PV-002 | permitted | decided fresh | — |  |
| 202 | Embed the canary string in every generated evaluation case | FL-EV-006 | permitted | decided fresh after a tie | none_tie |  |
| 203 | Widen the parity report to distinguish immaterial differences | FL-EV-009 | permitted | decided fresh | — |  |
| 204 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-009 | permitted | decided fresh | — |  |
| 205 | Resolve internal packages from the private registry first | FL-SC-007 | permitted | decided fresh | — |  |
| 206 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 207 | Gate promotion on the full safety suite, not the fast subset | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 208 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | permitted with conditions | decided fresh | — | ● |
| 209 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 210 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 211 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-EV-010 | denied | decided fresh | — |  |
| 212 | Declare the carrier channel for each untrusted input source | FL-LS-008 | permitted | decided fresh | — |  |
| 213 | Give the coding agent its own short-lived signing credential | FL-AG-008 | permitted with conditions | decided fresh | — | ● |
| 214 | Give the coding agent its own short-lived signing credential | FL-AG-006 | permitted with conditions | decided fresh | — | ● |
| 215 | Verify provenance against the expected builder identity before deploy | FL-SC-006 | permitted | disposed by citation | — |  |
| 216 | Record a disposition for every referral the board acknowledges | FL-GV-010 | permitted | decided fresh | — |  |
| 217 | Attribute the standing declaration in the exported rulebook | FL-GV-010 | permitted | decided fresh | — |  |
| 218 | Record the agent identity on every quota decision | FL-FG-002 | permitted | decided fresh | — |  |
| 219 | State the percentile on every latency claim in the dashboard | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 220 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted | decided fresh | — |  |
| 221 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 222 | Restrict agent outbound calls to the allowlisted host set | FL-AG-004 | permitted | decided fresh | — |  |
| 223 | Compare the provenance subject digest to the distributed artifact | FL-SC-004 | permitted | decided fresh | — |  |
| 224 | Revoke weight-store access automatically on a role-change event | FL-WX-002 | permitted with conditions | decided fresh | — | ● |
| 225 | Check the code-signing extended key usage on the release chain | FL-MB-008 | permitted | decided fresh | — |  |
| 226 | Publish the signing certificate chain alongside each release digest | FL-MB-006 | permitted | decided fresh | — |  |
| 227 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh | — |  |
| 228 | Document which attack class the new defence was evaluated against | FL-LS-007 | permitted | decided fresh | — |  |
| 229 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 230 | Move cost control from a meter to a pre-flight breaker | FL-FG-006 | permitted | decided fresh | — |  |
| 231 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-006 | denied | decided fresh | — | ● |
| 232 | Publish the release without an updated training-content summary | FL-TR-001 FL-MB-007 ⛔ | denied | refused at the floor | — |  |
| 233 | Store the provenance chain for derived synthetic corpora | FL-TD-007 | permitted | decided fresh | — |  |
| 234 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted | decided fresh | — |  |
| 235 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-001 FL-PI-007 ⛔ | denied | refused at the floor | — |  |
| 236 | Record the availability type on every newly onboarded source | FL-TD-004 | permitted | decided fresh | — |  |
| 237 | Enable batch invariance before claiming bitwise replay | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 238 | Require human confirmation before the agent executes a write tool | FL-LS-008 | permitted | decided fresh | — |  |
| 239 | Give the assistant a first-person human backstory in the release build | FL-BS-001 FL-PV-002 ⛔ | denied | refused at the floor | — |  |
| 240 | Widen the prompt-label review rule to cover staging labels too | FL-SF-006 | denied | decided fresh | — |  |
| 241 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-004 | permitted | decided fresh | — |  |
| 242 | Report refusal and over-refusal rates side by side | FL-BS-004 | permitted | decided fresh | — |  |
| 243 | Make the inference-engine build hermetic and reproducible | FL-SC-004 | permitted | decided fresh | — |  |
| 244 | Run agent-authored code only inside the sandboxed runner | FL-AG-005 | permitted | decided fresh | — | ● |
| 245 | Separate the production prompt label from its version string | FL-MB-007 | permitted | disposed by citation | — |  |
| 246 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 247 | Expose a contest path to affected customers in the portal | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 248 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-004 | permitted with conditions | decided fresh | — | ● |
| 249 | Sample the de-identified shard weekly and report the residual rate | FL-PI-007 | permitted with conditions | decided fresh | — | ● |
| 250 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted | decided fresh | — |  |
| 251 | Scan responses for canary tokens before they leave the gateway | FL-LS-004 | permitted | decided fresh | — |  |
| 252 | Fail the build on scan findings above the severity threshold | FL-SC-008 | permitted | decided fresh | — |  |
| 253 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-008 | permitted | decided fresh | — |  |
| 254 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 255 | Give the assistant a first-person human backstory in the release build | FL-BS-002 | denied | decided fresh | — |  |
| 256 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 257 | Keep reporter bulletins off the adjudication input path | FL-GV-006 | permitted | decided fresh | — |  |
| 258 | Turn off the abuse-material classifier on the image-generation path to cut moderation latency | FL-CS-001 FL-BS-006 ⛔ | denied | refused at the floor | — |  |
| 259 | Pin the golden-prompt baseline to a commit digest | FL-EV-006 | permitted | decided fresh after a tie | none_tie |  |
| 260 | Train on the partner's user conversations before the basis is recorded | FL-PI-007 | denied | decided fresh | — | ● |
| 261 | Escape tool output before it reaches the shell adapter | FL-LS-003 | permitted | decided fresh | — |  |
| 262 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-008 | permitted | decided fresh | — |  |
| 263 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted with conditions | decided fresh | — | ● |
| 264 | Drop the failing refusal suite from the promotion gate this train | FL-EV-008 | denied | decided fresh | — |  |
| 265 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 266 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | decided fresh | — |  |
| 267 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | decided fresh | — |  |
| 268 | Name a data-governance custodian on each dataset record | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 269 | Require two-person authorisation for unreleased-weight access | FL-SF-007 | permitted | decided fresh | — |  |
| 270 | Move authorization checks out of the client and into the gateway | FL-AS-004 | permitted | docketed — not charged | — |  |
| 271 | Check agent diffs for structural matches against known libraries | FL-IP-004 | permitted | decided fresh | — |  |
| 272 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 273 | Hide the human override behind a flag that ships off | FL-GV-001 FL-PI-007 ⛔ | denied | refused at the floor | — |  |
| 274 | Let the agent edit the release workflow to unblock its own branch | FL-AG-004 | denied | decided fresh | — |  |
| 275 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 276 | Move retrieved documents into a separate, clearly marked context block | FL-LS-009 | permitted | decided fresh | — |  |
| 277 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted | decided fresh | — |  |
| 278 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | decided fresh | — |  |
| 279 | Enable batch invariance before claiming bitwise replay | FL-IN-008 | permitted | docketed — not charged | — |  |
| 280 | Ship the research agent with no turn limit in its configuration | FL-FG-002 | denied | decided fresh | — |  |
| 281 | Report parity as a single percentage with no sample size | FL-EV-003 | denied | decided fresh | — |  |
| 282 | Check the code-signing extended key usage on the release chain | FL-MB-005 | permitted | disposed by citation | — |  |
| 283 | Change the escalation ladder so an automated tier may accept frontier risk | FL-MB-009 | denied | decided fresh | — |  |
| 284 | Report refusal and over-refusal rates side by side | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 285 | Exclude the election-integrity classifier from this release's gate | FL-UH-001 FL-BS-003 ⛔ | denied | refused at the floor | — |  |
| 286 | Sample the de-identified shard weekly and report the residual rate | FL-PI-006 | permitted | decided fresh | — |  |
| 287 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 288 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 289 | Respect the robots.txt AI directive in the web crawler | FL-TD-004 | permitted | decided fresh | — |  |
| 290 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 291 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-001 FL-SC-006 ⛔ | denied | refused at the floor | — |  |
| 292 | Bake the build timestamp and hostname into the engine binary | FL-SC-005 | denied | decided fresh | — |  |
| 293 | Let the video transcoder strip provenance metadata during re-encoding | FL-TR-001 FL-TD-008 ⛔ | denied | refused at the floor | — |  |
| 294 | Fail closed when a dataset licence string does not parse | FL-TD-002 | permitted | decided fresh | — | ● |
| 295 | Expose a contest path to affected customers in the portal | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 296 | Gate external evaluator access on the signed agreement | FL-SF-009 | permitted | decided fresh | — |  |
| 297 | Cover the new administrative routes in the authorization test suite | FL-AS-002 | permitted | docketed — not charged | — |  |
| 298 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — | ● |
| 299 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted | decided fresh | — |  |
| 300 | Give the coding agent its own short-lived signing credential | FL-AG-008 | permitted | decided fresh | — |  |
| 301 | Restrict agent outbound calls to the allowlisted host set | FL-AG-007 | permitted | decided fresh | — |  |
| 302 | Fail the build when an agent commit arrives unsigned | FL-AG-007 | permitted | decided fresh | — |  |
| 303 | Hold verbatim third-party reproduction below the span threshold | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 304 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-003 | denied | decided fresh | — | ● |
| 305 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | decided fresh | — |  |
| 306 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 307 | Attach Croissant metadata to the new publisher corpus | FL-TD-003 | permitted | decided fresh | — |  |
| 308 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-008 | permitted | decided fresh | — | ● |
| 309 | Give every system prompt an immutable version identifier | FL-MB-008 | permitted | disposed by citation | — |  |
| 310 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-009 | permitted | decided fresh | — |  |
| 311 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted | decided fresh | — |  |
| 312 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | permitted | decided fresh | — |  |
| 313 | Remove the canary check from the response filter to cut latency | FL-LS-001 FL-IN-004 ⛔ | denied | refused at the floor | — |  |
| 314 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 315 | Block internal address ranges in the web-fetch tool | FL-AS-004 | permitted | docketed — not charged | — |  |
| 316 | Onboard the new chat source without running the de-identification sample | FL-PI-006 | denied | decided fresh | — |  |
| 317 | Publish the notice file alongside each inference-engine release | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 318 | Publish the release notes without the downstream-provider information section | FL-TR-004 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 319 | Ship the quantised build four points below the tolerance band | FL-EV-001 ⛔ | denied | refused at the floor | — |  |
| 320 | Give the tool-call graph an explicit terminator | FL-FG-005 | permitted | decided fresh | — |  |
| 321 | Make the breaker unreachable from the agent's own configuration | FL-FG-005 | permitted | decided fresh | — |  |
| 322 | Return a generic error identifier instead of the stack trace | — | permitted | docketed — nothing engaged | — |  |
| 323 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted | decided fresh | — |  |
| 324 | Write a docket entry for every arrival that is not charged | FL-GV-006 | permitted | decided fresh | — |  |
| 325 | Let retrieval read audit findings so precedent search returns more | FL-GV-008 | denied | decided fresh | — |  |
| 326 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-004 | permitted | decided fresh | — |  |
| 327 | Record a lawful basis for each conversation-data source | FL-PI-004 | permitted | decided fresh | — |  |
| 328 | Enable the new sampler that slows per-token output beyond budget | FL-IN-001 | denied | decided fresh | — |  |
| 329 | Exclude special-category fields from the support-transcript schema | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 330 | Reject artifacts whose served hash differs from the registry entry | FL-MB-007 | permitted with conditions | decided fresh | — | ● |
| 331 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 332 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 333 | Separate the audit register from the precedent store at schema level | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 334 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 335 | File a draft amendment carving out build-time-only dependencies | FL-SC-005 | denied | decided fresh | — |  |
| 336 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-005 | permitted | decided fresh | — |  |
| 337 | Set the planner's recursion limit to zero, meaning unlimited | FL-FG-001 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 338 | Declare sample size and percentile alongside the parity result | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 339 | State the percentile on every latency claim in the dashboard | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 340 | Pin every dependency to an immutable digest in the lockfile | FL-SC-003 | permitted with conditions | decided fresh | — | ● |
| 341 | Add an eval-awareness probe to the pre-release harness run | FL-CB-003 | permitted | decided fresh | — |  |
| 342 | Route threshold-crossing results to an automatic deployment hold | FL-CB-003 | permitted | decided fresh | — |  |
| 343 | Redact prompt and completion logs before they reach retention | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 344 | Publish a review checklist for agent changes to the eval harness | FL-AG-005 | permitted | decided fresh | — |  |
| 345 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 346 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 347 | Declare sample size and percentile alongside the parity result | FL-EV-009 | permitted | decided fresh | — |  |
| 348 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 349 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | decided fresh | — |  |
| 350 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-001 FL-TD-006 ⛔ | denied | refused at the floor | — |  |
| 351 | Redact prompt and completion logs before they reach retention | FL-PI-006 | permitted | decided fresh | — |  |
| 352 | Split personal-data handling out of the shared ingestion library | FL-PI-006 | permitted | decided fresh | — |  |
| 353 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 354 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-006 | permitted | decided fresh | — |  |
| 355 | Keep reporter bulletins off the adjudication input path | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 356 | Require a human reviewer on agent changes to request routing | FL-AG-007 | permitted | disposed by citation | — |  |
| 357 | Strip internal identifiers from gateway error responses | FL-AS-005 | permitted | docketed — not charged | — |  |
| 358 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 359 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted | decided fresh | — |  |
| 360 | Move authorization checks out of the client and into the gateway | FL-AS-001 | permitted | decided fresh | — |  |
| 361 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 362 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | disposed by citation | — |  |
| 363 | Gate external evaluator access on the signed agreement | FL-SF-006 | permitted | decided fresh | — |  |
| 364 | Record the frontier framework version in force on the release record | FL-SF-006 | permitted | decided fresh | — |  |
| 365 | Block internal address ranges in the web-fetch tool | FL-AS-006 | permitted | docketed — not charged | — |  |
| 366 | Stop reading the loop limit from an environment variable | FL-FG-003 | permitted with conditions | decided fresh | — | ● |
| 367 | Inline retrieved documents into the system prompt to save tokens | FL-LS-001 ⛔ | denied | refused at the floor | — |  |
| 368 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-004 | permitted | decided fresh | — |  |
| 369 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh after a tie | none_tie |  |
| 370 | Declare the agent loop limit numerically with its units | FL-FG-003 | permitted | decided fresh | — |  |
| 371 | State turns rather than seconds as the loop-limit unit | FL-FG-003 | permitted | decided fresh | — |  |
| 372 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-002 FL-EV-004 ⛔ | denied | refused at the floor | — |  |
| 373 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | decided fresh | — |  |
| 374 | Publish the signing certificate chain alongside each release digest | FL-MB-009 | permitted | decided fresh | — |  |
| 375 | Record the agent identity on every quota decision | FL-FG-004 | permitted | decided fresh | — | ● |
| 376 | Widen the prompt-label review rule to cover staging labels too | FL-BS-004 | denied | decided fresh | — |  |
| 377 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | permitted | decided fresh | — |  |
| 378 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | permitted | decided fresh | — |  |
| 379 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-003 | permitted | decided fresh | — |  |
| 380 | Redact prompt and completion logs before they reach retention | FL-PI-006 | permitted | decided fresh | — | ● |
| 381 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-001 | permitted | decided fresh | — |  |
| 382 | Change the escalation ladder so an automated tier may accept frontier risk | FL-PI-005 | denied | decided fresh | — |  |
| 383 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-003 | permitted with conditions | decided fresh | — | ● |
| 384 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-002 | permitted | decided fresh after a tie | none_tie |  |
| 385 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 386 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 387 | Hide the human override behind a flag that ships off | FL-GV-005 | denied | decided fresh | — |  |
| 388 | Remove insider-anomaly detection from the training cluster to cut alert noise | FL-WX-004 ⛔ | denied | refused at the floor | — |  |
| 389 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh | — |  |
| 390 | Widen the prompt-label review rule to cover staging labels too | FL-EV-010 | denied | decided fresh | — |  |
| 391 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 392 | Require human confirmation before the agent executes a write tool | FL-LS-010 | permitted | decided fresh | — |  |
| 393 | Sample the de-identified shard weekly and report the residual rate | FL-PI-007 | permitted | decided fresh | — |  |
| 394 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — |  |
| 395 | Add a new exemption class to the agent sign-off rule | FL-LS-005 | denied | decided fresh | — |  |
| 396 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-EV-005 | denied | decided fresh | — |  |
| 397 | Split personal-data handling out of the shared ingestion library | FL-PI-003 | permitted with conditions | decided fresh | — | ● |
| 398 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-008 | permitted | decided fresh | — | ● |
| 399 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-002 | permitted with conditions | decided fresh | — | ● |
| 400 | Check every new import against the upstream registry before build | FL-AG-007 | permitted | decided fresh | — |  |
| 401 | Screen new fine-tuning shards for backdoor triggers | FL-LS-011 | permitted | decided fresh | — |  |
| 402 | Enforce the instruction and data boundary on the retrieval path | FL-LS-011 | permitted | decided fresh | — |  |
| 403 | Add a weekly sampling job over production refusals | FL-BS-004 | permitted | decided fresh | — |  |
| 404 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — |  |
| 405 | Collapse the two compute thresholds into a single configuration field | FL-GV-003 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 406 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 407 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-003 | permitted | docketed — not charged | — |  |
| 408 | Return a generic error identifier instead of the stack trace | FL-AS-006 | permitted | docketed — not charged | — |  |
| 409 | Move retrieved documents into a separate, clearly marked context block | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 410 | Register the new fused kernel as a nondeterministic operation | FL-IN-005 | permitted | decided fresh | — |  |
| 411 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 412 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 413 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-008 | permitted | decided fresh after a tie | none_tie |  |
| 414 | Screen new fine-tuning shards for backdoor triggers | FL-LS-011 | permitted with conditions | decided fresh | — | ● |
| 415 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 416 | Propagate attribution obligations from corpus records to release notes | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 417 | Screen new fine-tuning shards for backdoor triggers | FL-LS-007 | permitted | decided fresh | — |  |
| 418 | Log the named authority for every override exercised | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 419 | Split personal-data handling out of the shared ingestion library | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 420 | Measure judge and human agreement for the new grader configuration | FL-EV-003 | permitted | decided fresh | — |  |
| 421 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | decided fresh | — |  |
| 422 | Fuzz the changed completions parameters before release | FL-AS-001 | permitted | decided fresh | — |  |
| 423 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 424 | Run agent-authored code only inside the sandboxed runner | FL-AG-004 | permitted | decided fresh | — |  |
| 425 | Register the new fused kernel as a nondeterministic operation | FL-IN-005 | permitted | decided fresh | — |  |
| 426 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 427 | Update the third-party licence inventory with this dependency change | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 428 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-007 | permitted | decided fresh | — |  |
| 429 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — |  |
| 430 | Measure judge and human agreement for the new grader configuration | FL-EV-006 | permitted | decided fresh | — |  |
| 431 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 432 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-004 | permitted with conditions | decided fresh | — | ● |
| 433 | Record the builder identity in attestations for nightly checkpoints | FL-SC-003 | permitted | decided fresh | — |  |
| 434 | Make decision records append-only in the store schema | FL-GV-009 | permitted | decided fresh | — |  |
| 435 | Keep reporter bulletins off the adjudication input path | FL-GV-009 | permitted | decided fresh | — |  |
| 436 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted | decided fresh | — |  |
| 437 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-002 | denied | decided fresh | — |  |
| 438 | Backfill lineage records for the older quantised checkpoints | FL-MB-005 | permitted | decided fresh | — |  |
| 439 | Run the uplift eval on the safety-trained checkpoint without the elicitation prompts | FL-CB-004 | denied | decided fresh | — |  |
| 440 | Parameterise the new experiment-metrics filter queries | FL-AS-002 | permitted | docketed — not charged | — |  |
| 441 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-003 | permitted | decided fresh | — |  |
| 442 | Turn off commit signing for the agent runner while its key rotates | FL-AG-005 | denied | decided fresh | — | ● |
| 443 | Broaden the refusal trigger list until safe prompts start bouncing | FL-BS-005 | denied | decided fresh | — |  |
| 444 | Resolve internal packages from the private registry first | FL-SC-003 | permitted | decided fresh | — | ● |
| 445 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 446 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 447 | Fail the merge when the scanner reports an unresolved licence | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 448 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-008 | permitted | docketed — not charged | — |  |
| 449 | Declare the downstream sink for every model output field | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 450 | Declare the carrier channel for each untrusted input source | FL-LS-006 | permitted | decided fresh | — |  |
| 451 | Make the inference-engine build hermetic and reproducible | FL-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 452 | Loosen the toxicity cut-off in the gate config to clear the backlog | FL-BS-001 FL-SF-006 ⛔ | denied | refused at the floor | — |  |
| 453 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-007 | permitted | decided fresh | — |  |
| 454 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | decided fresh | — |  |
| 455 | Record attribution for the reused tokenizer snippet | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 456 | Record a lawful basis for each conversation-data source | FL-PI-004 | permitted | decided fresh | — |  |
| 457 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — |  |
| 458 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted | decided fresh | — |  |
| 459 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-006 | denied | decided fresh | — | ● |
| 460 | Check persona guidance against the shipped system prompt | FL-BS-002 | permitted | decided fresh | — |  |
| 461 | Bind weight-store access grants to the current personnel-vetting record | FL-WX-002 | permitted | decided fresh | — |  |
| 462 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-006 | permitted | decided fresh | — | ● |
| 463 | Commit the live cluster token into the test fixtures directory | FL-SC-002 | denied | decided fresh | — | ● |
| 464 | Strip internal identifiers from gateway error responses | FL-AS-002 | permitted | docketed — not charged | — |  |
| 465 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted | decided fresh | — |  |
| 466 | Block promotion until the dangerous-capability reports complete | FL-SF-004 | permitted | decided fresh | — |  |
| 467 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted | decided fresh | — |  |
| 468 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 469 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 470 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-001 FL-SF-006 ⛔ | denied | refused at the floor | — |  |
| 471 | Carry attribution notices through to the shipped container image | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 472 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 473 | Queue nonconsensual-imagery takedown requests behind the general moderation backlog | FL-UH-004 | denied | decided fresh | — |  |
| 474 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted | decided fresh | — | ● |
| 475 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 476 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-004 | permitted | decided fresh | — |  |
| 477 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-008 | permitted | decided fresh | — |  |
| 478 | Publish a review checklist for agent changes to the eval harness | FL-AG-008 | permitted | decided fresh | — |  |
| 479 | Restrict agent outbound calls to the allowlisted host set | FL-AG-008 | permitted | decided fresh | — |  |
| 480 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | decided fresh | — |  |
| 481 | Name a data-governance custodian on each dataset record | FL-TD-002 | permitted | decided fresh | — |  |
| 482 | Add hash-list refresh monitoring to the training ingestion dashboard | FL-CS-004 | permitted | decided fresh | — |  |
| 483 | Route flagged responses to the block path rather than a warning | FL-BS-002 | permitted | decided fresh | — |  |
| 484 | Propose allowing sampled rather than exhaustive licence detection | FL-LS-004 | denied | decided fresh | — |  |
| 485 | Add a weekly sampling job over production refusals | FL-BS-002 | permitted | decided fresh | — |  |
| 486 | Have trade counsel sign the export-classification determination record | FL-WX-003 | permitted with conditions | decided fresh | — | ● |
| 487 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | permitted | decided fresh | — |  |
| 488 | Reject unexpected content types on the tool-callback endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 489 | Check every new import against the upstream registry before build | FL-AG-008 | permitted | decided fresh | — |  |
| 490 | Cover the new administrative routes in the authorization test suite | — | permitted | docketed — nothing engaged | — |  |
| 491 | Update the third-party licence inventory with this dependency change | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 492 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 493 | Merge the agent's scheduler that mirrors a copyleft project function by function | FL-IP-001 FL-AG-008 ⛔ | denied | refused at the floor | — |  |
| 494 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 495 | Downgrade the shard distribution halt to a warning banner | FL-LS-002 FL-LS-010 ⛔ | denied | refused at the floor | — |  |
| 496 | Land the fallback that quietly turns draft-model decoding off | FL-EV-004 | denied | decided fresh | — |  |
| 497 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 498 | Rewrite the last raw query in the usage-reporting job | FL-AS-002 | permitted | docketed — not charged | — |  |
| 499 | Inline retrieved documents into the system prompt to save tokens | FL-LS-001 FL-SF-005 ⛔ | denied | refused at the floor | — |  |
| 500 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-TD-002 | denied | decided fresh | — |  |
| 501 | Give the tool-call graph an explicit terminator | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 502 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-001 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 503 | Fuzz the changed completions parameters before release | FL-AS-002 | permitted | docketed — not charged | — |  |
| 504 | Measure demographic disparity across the ambiguous-context suite | FL-BS-006 | permitted | decided fresh | — |  |
| 505 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-006 | permitted | decided fresh | — |  |
| 506 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 507 | Route the internal safety-concern channel through a ticketing system that logs the reporter's identity | FL-TR-002 | denied | decided fresh | — |  |
| 508 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-007 | permitted with conditions | decided fresh | — | ● |
| 509 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted | decided fresh | — |  |
| 510 | Require two-person authorisation for unreleased-weight access | FL-SF-008 | permitted | decided fresh | — |  |
| 511 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-001 ⛔ | denied | refused at the floor | — |  |
| 512 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 513 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | decided fresh | — |  |
| 514 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-004 | permitted | decided fresh | — |  |
| 515 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-006 | denied | decided fresh | — |  |
| 516 | Relax the coverage floor in the policy bundle to unblock a release train | FL-PI-002 | denied | decided fresh | — |  |
| 517 | Test egress-monitoring coverage in the quarterly weight-security drill | FL-WX-003 | permitted | decided fresh | — |  |
| 518 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 519 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-002 | permitted | decided fresh | — |  |
| 520 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-005 | denied | decided fresh | — |  |
| 521 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-004 | permitted | decided fresh | — |  |
| 522 | Report first-token and per-token latency against the tier budgets | FL-IN-004 | permitted | decided fresh | — |  |
| 523 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-SC-007 | denied | decided fresh | — |  |
| 524 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-002 FL-SC-005 ⛔ | denied | refused at the floor | — |  |
| 525 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 526 | Move release signing keys onto the hardware security module | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 527 | Write matched shards into the training corpus before the quarantine step finishes | FL-CS-001 FL-FG-003 ⛔ | denied | refused at the floor | — |  |
| 528 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 529 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | permitted | decided fresh | — | ● |
| 530 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-005 | permitted | decided fresh | — |  |
| 531 | Embed the canary string in every generated evaluation case | FL-EV-005 | permitted | decided fresh | — |  |
| 532 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | permitted | decided fresh | — |  |
| 533 | Sign agent commits with a workload identity rather than a person's key | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 534 | Propose allowing sampled rather than exhaustive licence detection | FL-LS-005 | denied | decided fresh | — |  |
| 535 | Declare sample size and percentile alongside the parity result | FL-EV-008 | permitted | decided fresh | — |  |
| 536 | Run the decontamination check over the new code corpus | FL-EV-008 | permitted | decided fresh | — |  |
| 537 | Check persona guidance against the shipped system prompt | FL-BS-003 | permitted | decided fresh | — |  |
| 538 | Have the crawler submit the consent form to reach the archive body | FL-TD-002 | denied | decided fresh | — | ● |
| 539 | Declare the downstream sink for every model output field | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 540 | Make the breaker unreachable from the agent's own configuration | FL-FG-006 | permitted | decided fresh | — | ● |
| 541 | Gate promotion on the full safety suite, not the fast subset | FL-EV-009 | permitted | decided fresh | — |  |
| 542 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-006 | permitted | decided fresh | — |  |
| 543 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 544 | Widen the parity report to distinguish immaterial differences | FL-EV-007 | permitted | decided fresh | — |  |
| 545 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | decided fresh | — | ● |
| 546 | Store the provenance chain for derived synthetic corpora | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 547 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 548 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 549 | Raise the capability threshold in the policy repository | FL-SF-005 | denied | decided fresh | — |  |
| 550 | Restrict agent outbound calls to the allowlisted host set | FL-AG-006 | permitted | disposed by citation | — |  |
| 551 | Pin workflow actions to commit digests across the release repository | FL-SC-008 | permitted | bound by precedent | REC-S0115 |  |
| 552 | Embed the canary string in every generated evaluation case | FL-EV-010 | permitted | decided fresh | — |  |
| 553 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | permitted | decided fresh | — |  |
| 554 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | decided fresh | — |  |
| 555 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 556 | Check the code-signing extended key usage on the release chain | FL-MB-009 | permitted | decided fresh | — |  |
| 557 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | decided fresh | — |  |
| 558 | Parameterise the new experiment-metrics filter queries | — | permitted | docketed — nothing engaged | — |  |
| 559 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-001 | permitted | decided fresh | — |  |
| 560 | Log every read of the weights store to the perimeter audit trail | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 561 | Propose allowing sampled rather than exhaustive licence detection | FL-TD-004 | denied | decided fresh | — |  |
| 562 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 563 | State the percentile on every latency claim in the dashboard | — | permitted | docketed — nothing engaged | — |  |
| 564 | Run the decontamination check over the new code corpus | FL-EV-003 | permitted with conditions | decided fresh | — | ● |
| 565 | Move release signing keys onto the hardware security module | FL-SF-006 | permitted | decided fresh | — |  |
| 566 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 567 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-005 | permitted | decided fresh | — | ● |
| 568 | Pin every dependency to an immutable digest in the lockfile | FL-SC-007 | permitted with conditions | decided fresh | — | ● |
| 569 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-007 | permitted | disposed by citation | — |  |
| 570 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted | decided fresh | — |  |
| 571 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-004 | permitted | decided fresh | — |  |
| 572 | Change the escalation ladder so an automated tier may accept frontier risk | FL-FG-002 | denied | decided fresh | — |  |
| 573 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted | decided fresh after a tie | none_tie |  |
| 574 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-007 | permitted | decided fresh | — |  |
| 575 | Relax the coverage floor in the policy bundle to unblock a release train | FL-LS-010 | denied | decided fresh | — |  |
| 576 | Strip internal identifiers from gateway error responses | FL-AS-005 | permitted | docketed — not charged | — |  |
| 577 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 578 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 579 | Record the availability type on every newly onboarded source | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 580 | Replace the abuse-material classifier's legacy matcher with the clearinghouse's current API | FL-CS-004 | permitted | decided fresh | — |  |
| 581 | Extend report-preservation storage to eighteen months ahead of the statutory floor | FL-CS-004 | permitted | decided fresh | — |  |
| 582 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — |  |
| 583 | Default unparsed licence strings to permissive so ingestion stops stalling | FL-TD-001 FL-TD-006 ⛔ | denied | refused at the floor | — |  |
| 584 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | decided fresh | — | ● |
| 585 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-002 | permitted | decided fresh | — |  |
| 586 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 587 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 588 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 589 | Exclude special-category fields from the support-transcript schema | FL-PI-004 | permitted with conditions | decided fresh | — | ● |
| 590 | Respect the robots.txt AI directive in the web crawler | FL-TD-003 | permitted | decided fresh | — |  |
| 591 | Propose allowing sampled rather than exhaustive licence detection | FL-TR-002 | denied | decided fresh | — |  |
| 592 | Validate tenant scope on every portal export request | FL-AS-005 | permitted | docketed — not charged | — |  |
| 593 | Enable batch invariance before claiming bitwise replay | FL-IN-007 | permitted | docketed — not charged | — |  |
| 594 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-004 | permitted | decided fresh | — |  |
| 595 | Reject artifacts whose served hash differs from the registry entry | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 596 | Redact prompt and completion logs before they reach retention | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 597 | Require human confirmation before the agent executes a write tool | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 598 | Record the capability-threshold determination on the release record | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 599 | Restrict weight egress to the declared perimeter buckets | FL-SF-005 | permitted | decided fresh | — |  |
| 600 | Check agent diffs for structural matches against known libraries | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 601 | Require two-person authorisation for unreleased-weight access | FL-SF-008 | permitted | decided fresh | — |  |
| 602 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-006 | permitted | decided fresh | — |  |
| 603 | Move cost control from a meter to a pre-flight breaker | FL-FG-003 | permitted | decided fresh | — |  |
| 604 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-002 FL-PV-002 ⛔ | denied | refused at the floor | — |  |
| 605 | Put a circuit breaker on the recursive summarisation path | FL-FG-005 | permitted | decided fresh | — |  |
| 606 | Fail the run outright when no loop limit is declared | FL-FG-005 | permitted | decided fresh | — |  |
| 607 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 608 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | decided fresh | — |  |
| 609 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted | decided fresh | — |  |
| 610 | Log the named authority for every override exercised | FL-GV-008 | permitted | decided fresh | — |  |
| 611 | Publish the tier latency figure with no percentile attached | FL-IN-003 | denied | decided fresh | — |  |
| 612 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 613 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 614 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-001 | permitted | decided fresh | — |  |
| 615 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-003 | permitted | decided fresh | — |  |
| 616 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-002 FL-CS-004 ⛔ | denied | refused at the floor | — |  |
| 617 | State turns rather than seconds as the loop-limit unit | FL-FG-004 | permitted with conditions | decided fresh | — | ● |
| 618 | Run semantic analysis over the agent diff in continuous integration | FL-AG-005 | permitted | decided fresh | — | ● |
| 619 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-010 | permitted | decided fresh | — |  |
| 620 | Reorder the index list so the public registry answers first | FL-SC-001 FL-GV-007 ⛔ | denied | refused at the floor | — |  |
| 621 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 622 | Land the new forum corpus with its provenance fields left blank | FL-TD-002 | denied | decided fresh | — |  |
| 623 | Record the licence class for every corpus the crawler ingests | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 624 | Record the builder identity in attestations for nightly checkpoints | FL-SC-004 | permitted | disposed by citation | — |  |
| 625 | Let the mail agent follow instructions it finds in the message body | FL-LS-010 | denied | decided fresh | — |  |
| 626 | Keep the toxicity filter in the response path for streaming replies | FL-BS-005 | permitted | decided fresh | — |  |
| 627 | Pin the key-value cache budget for the agentic serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 628 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | decided fresh | — | ● |
| 629 | Run the decontamination check over the new code corpus | FL-EV-004 | permitted | decided fresh | — |  |
| 630 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-004 | permitted | decided fresh | — |  |
| 631 | Keep the toxicity filter in the response path for streaming replies | FL-BS-003 | permitted | decided fresh | — |  |
| 632 | Check persona guidance against the shipped system prompt | FL-BS-003 | permitted | decided fresh | — |  |
| 633 | Record attribution for the reused tokenizer snippet | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 634 | Resolve internal packages from the private registry first | FL-SC-008 | permitted | decided fresh | — |  |
| 635 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 636 | Widen the prompt-label review rule to cover staging labels too | FL-LS-008 | denied | decided fresh | — |  |
| 637 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted | decided fresh | — |  |
| 638 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted | decided fresh after a tie | none_tie |  |
| 639 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | permitted | decided fresh | — |  |
| 640 | Require a named owner to approve production prompt label moves | FL-MB-006 | permitted | decided fresh | — |  |
| 641 | Run the memorisation probe on the release candidate | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 642 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-006 | permitted | decided fresh | — | ● |
| 643 | Extend report-preservation storage to eighteen months ahead of the statutory floor | FL-CS-004 | permitted | decided fresh | — |  |
| 644 | Resolve internal packages from the private registry first | FL-SC-008 | permitted | decided fresh | — |  |
| 645 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-004 | permitted | decided fresh | — |  |
| 646 | Exclude special-category fields from the support-transcript schema | FL-PI-007 | permitted | decided fresh | — |  |
| 647 | Add a new exemption class to the agent sign-off rule | FL-AG-007 | denied | decided fresh | — |  |
| 648 | Record the agent identity on every quota decision | FL-FG-006 | permitted | decided fresh | — |  |
| 649 | Move cost control from a meter to a pre-flight breaker | FL-FG-006 | permitted | decided fresh | — |  |
| 650 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 651 | Keep the human override reachable in the high-risk review flow | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 652 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-004 | permitted | decided fresh | — |  |
| 653 | Cover the new administrative routes in the authorization test suite | FL-AS-002 | permitted | docketed — not charged | — |  |
| 654 | Carry attribution notices through to the shipped container image | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 655 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 656 | Widen the parity report to distinguish immaterial differences | FL-EV-010 | permitted | decided fresh | — |  |
| 657 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted | decided fresh | — |  |
| 658 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted | decided fresh | — |  |
| 659 | Run release builds on ephemeral runners with pinned images | FL-SC-002 | permitted | decided fresh | — |  |
| 660 | Report first-token and per-token latency against the tier budgets | FL-IN-007 | permitted | docketed — not charged | — |  |
| 661 | Record the capability-threshold determination on the release record | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 662 | Gate promotion on the full safety suite, not the fast subset | FL-EV-005 | permitted with conditions | decided fresh | — | ● |
| 663 | Run the personal-data scan on every new training shard | FL-PI-006 | permitted | decided fresh | — |  |
| 664 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-004 | permitted | decided fresh | — |  |
| 665 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-004 | permitted | decided fresh | — |  |
| 666 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-003 | permitted | decided fresh | — | ● |
| 667 | Remove the contest link from the customer decision notice | FL-GV-001 ⛔ | denied | refused at the floor | — |  |
| 668 | Hold goodput at the tier threshold under the burst profile | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 669 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted | decided fresh | — |  |
| 670 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-011 | denied | decided fresh | — |  |
| 671 | Re-pin the batch scorer to the retired atlas-base hash | FL-MB-005 | denied | decided fresh | — |  |
| 672 | Turn off egress monitoring on the weight store during the migration window | FL-WX-001 FL-GV-009 ⛔ | denied | refused at the floor | — |  |
| 673 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 674 | File a draft amendment carving out build-time-only dependencies | FL-BS-006 | denied | decided fresh | — |  |
| 675 | Move cost control from a meter to a pre-flight breaker | FL-FG-002 | permitted | decided fresh | — |  |
| 676 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-002 | permitted | decided fresh | — | ● |
| 677 | Report refusal and over-refusal rates side by side | FL-BS-004 | permitted | decided fresh | — |  |
| 678 | Pin the key-value cache budget for the agentic serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 679 | Report first-token and per-token latency against the tier budgets | FL-IN-001 | permitted | decided fresh | — |  |
| 680 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 681 | Name a data-governance custodian on each dataset record | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 682 | Publish the signing certificate chain alongside each release digest | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 683 | Escape tool output before it reaches the shell adapter | FL-LS-003 | permitted | decided fresh | — |  |
| 684 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-003 | permitted | decided fresh | — |  |
| 685 | Pin every dependency to an immutable digest in the lockfile | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 686 | Let the agent mark the failing provenance test as skipped | FL-AG-004 | denied | decided fresh | — |  |
| 687 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 688 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 689 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 690 | Validate tenant scope on every portal export request | FL-AS-004 | permitted | docketed — not charged | — |  |
| 691 | Keep the human override reachable in the high-risk review flow | FL-GV-010 | permitted | decided fresh | — |  |
| 692 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 693 | Run the uplift eval on the safety-trained checkpoint without the elicitation prompts | FL-CB-004 | denied | decided fresh | — | ● |
| 694 | Replace the unit-test grader with a model judge for speed | FL-EV-003 | denied | decided fresh | — |  |
| 695 | Hold verbatim third-party reproduction below the span threshold | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 696 | Register the new fused kernel as a nondeterministic operation | — | permitted | docketed — nothing engaged | — |  |
| 697 | Disable the break reminder in companion mode for the premium tier | FL-UH-002 | denied | decided fresh | — |  |
| 698 | Propose an amendment codifying coverage rules for generated eval configs | FL-WX-003 | denied | decided fresh | — |  |
| 699 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | decided fresh | — | ● |
| 700 | Replace the unit-test grader with a model judge for speed | FL-EV-002 FL-LS-004 ⛔ | denied | refused at the floor | — |  |
| 701 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 702 | Exclude special-category fields from the support-transcript schema | FL-PI-006 | permitted | decided fresh | — |  |
| 703 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 704 | Edit the toxicity threshold directly through the adjudication service credentials | FL-SC-008 | denied | decided fresh | — |  |
| 705 | Parameterise the new experiment-metrics filter queries | FL-AS-005 | permitted | docketed — not charged | — |  |
| 706 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 707 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-003 | permitted | decided fresh | — |  |
| 708 | Route nonconsensual-imagery takedown requests ahead of the general moderation queue | FL-UH-003 | permitted | decided fresh | — |  |
| 709 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 710 | Require a human reviewer on agent changes to request routing | FL-AG-005 | permitted | decided fresh | — |  |
| 711 | Run the personal-data scan on every new training shard | FL-PI-005 | permitted | decided fresh | — | ● |
| 712 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 713 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh | — |  |
| 714 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 715 | Move cost control from a meter to a pre-flight breaker | FL-FG-003 | permitted | decided fresh | — |  |
| 716 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 717 | Exercise injection detection on the changed tool-calling path | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 718 | Add a training-manifest filter that excludes under-13 sourced conversations | FL-CS-003 | permitted with conditions | decided fresh | — | ● |
| 719 | Remove the synthetic-content marker from the image-generation output path | FL-TR-001 FL-BS-006 ⛔ | denied | refused at the floor | — |  |
| 720 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted | decided fresh | — | ● |
| 721 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted with conditions | decided fresh | — | ● |
| 722 | Record attribution for the reused tokenizer snippet | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 723 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-003 | denied | decided fresh | — |  |
| 724 | Check the code-signing extended key usage on the release chain | FL-MB-005 | permitted | decided fresh | — |  |
| 725 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-004 | permitted | decided fresh | — |  |
| 726 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-004 | permitted | decided fresh | — |  |
| 727 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 728 | Re-run the probe after the distillation step, not before it | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 729 | Enable batch invariance before claiming bitwise replay | FL-IN-002 | permitted | decided fresh | — |  |
| 730 | Change the escalation ladder so an automated tier may accept frontier risk | FL-UH-003 | denied | decided fresh | — |  |
| 731 | Bake the build timestamp and hostname into the engine binary | FL-SC-001 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 732 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 733 | Make decision records append-only in the store schema | FL-GV-010 | permitted | decided fresh | — |  |
| 734 | Route parameter changes through the amendment workflow instead | FL-GV-010 | permitted | decided fresh | — |  |
| 735 | Downgrade the weight-store data-loss-prevention alert from blocking to advisory | FL-WX-001 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 736 | Batch the mandatory-reporting webhook into a nightly job instead of firing per match | FL-CS-001 ⛔ | denied | refused at the floor | — |  |
| 737 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 738 | Release the run record with the threshold determination left blank | FL-SF-007 | denied | decided fresh | — |  |
| 739 | State the percentile on every latency claim in the dashboard | — | permitted | docketed — nothing engaged | — |  |
| 740 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 741 | Document the engine version pinned for each serving tier | FL-IN-003 | permitted | decided fresh | — |  |
| 742 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 743 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-003 | permitted with conditions | decided fresh | — | ● |
| 744 | Split personal-data handling out of the shared ingestion library | FL-PI-002 | permitted | decided fresh | — |  |
| 745 | Give the tool-call graph an explicit terminator | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 746 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 747 | Check the code-signing extended key usage on the release chain | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 748 | Require the safety-case signature from outside the authoring team | FL-SF-006 | permitted | decided fresh | — |  |
| 749 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | disposed by citation | — |  |
| 750 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 751 | Pin workflow actions to commit digests across the release repository | FL-SC-008 | permitted | bound by precedent | REC-S0115 |  |
| 752 | Measure membership-inference advantage on the release candidate | FL-LS-011 | permitted | decided fresh | — |  |
| 753 | Make the inference-engine build hermetic and reproducible | FL-SC-008 | permitted | decided fresh | — | ● |
| 754 | Publish the prompt-log retention clock in the customer portal | FL-PI-004 | permitted | decided fresh | — | ● |
| 755 | Widen the parity report to distinguish immaterial differences | FL-EV-010 | permitted with conditions | decided fresh | — | ● |
| 756 | Declare the agent loop limit numerically with its units | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 757 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | decided fresh | — |  |
| 758 | Propagate attribution obligations from corpus records to release notes | FL-TD-003 | permitted | decided fresh | — |  |
| 759 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-008 | permitted | docketed — not charged | — |  |
| 760 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-006 | permitted | decided fresh | — |  |
| 761 | Report refusal and over-refusal rates side by side | FL-BS-006 | permitted | decided fresh | — |  |
| 762 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-003 | permitted | decided fresh | — |  |
| 763 | Bind the research agent's quota to its cost centre | FL-FG-005 | permitted | decided fresh | — |  |
| 764 | Record a disposition for every referral the board acknowledges | FL-GV-008 | permitted | decided fresh | — |  |
| 765 | Write a docket entry for every arrival that is not charged | FL-GV-008 | permitted | decided fresh | — |  |
| 766 | Hardcode a real customer address into the escalation prompt template | FL-PI-003 | denied | decided fresh | — |  |
| 767 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-003 | permitted | decided fresh | — |  |
| 768 | Split personal-data handling out of the shared ingestion library | FL-PI-007 | permitted | decided fresh | — |  |
| 769 | Reject unexpected content types on the tool-callback endpoint | FL-AS-006 | permitted | docketed — not charged | — |  |
| 770 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 771 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | decided fresh | — | ● |
| 772 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-004 | permitted | disposed by citation | — |  |
| 773 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 774 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 775 | Recompute the root digest from resource digests before promotion | FL-MB-004 | permitted | disposed by citation | — |  |
| 776 | Enforce server-side authorization on the new batch endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 777 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-003 | denied | decided fresh | — |  |
| 778 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 779 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 780 | Remove the non-human disclosure line from the companion persona's opening message | FL-UH-005 | denied | decided fresh | — | ● |
| 781 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — | ● |
| 782 | Route law-enforcement data requests straight to on-call fulfilment, skipping the legal-review queue | FL-PV-003 FL-CS-004 ⛔ | denied | refused at the floor | — |  |
| 783 | Measure demographic disparity across the ambiguous-context suite | FL-BS-005 | permitted | decided fresh | — |  |
| 784 | Measure demographic disparity across the ambiguous-context suite | FL-BS-005 | permitted | decided fresh | — |  |
| 785 | Record attribution for the reused tokenizer snippet | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 786 | Repack the shard files after signing and reuse the old manifest | FL-MB-006 | denied | decided fresh | — |  |
| 787 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-001 | permitted | decided fresh | — |  |
| 788 | Backfill lineage records for the older quantised checkpoints | FL-MB-006 | permitted | decided fresh | — | ● |
| 789 | Let the agent edit the release workflow to unblock its own branch | FL-AG-006 | denied | decided fresh | — |  |
| 790 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 791 | Record the compute-threshold determination separately per jurisdiction | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 792 | Separate the production prompt label from its version string | FL-MB-008 | permitted | disposed by citation | — |  |
| 793 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-002 | permitted | decided fresh | — |  |
| 794 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 795 | Keep cases released after the training cutoff in the holdout | FL-EV-008 | permitted | decided fresh | — |  |
| 796 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-002 | permitted | decided fresh | — |  |
| 797 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-002 | denied | decided fresh | — |  |
| 798 | Compare the provenance subject digest to the distributed artifact | FL-SC-007 | permitted | decided fresh | — |  |
| 799 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 800 | Fail closed when a dataset licence string does not parse | FL-TD-002 | permitted | decided fresh | — |  |
| 801 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | permitted | decided fresh | — | ● |
| 802 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 803 | Widen the parity report to distinguish immaterial differences | FL-EV-006 | permitted | decided fresh | — |  |
| 804 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted | decided fresh | — |  |
| 805 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-004 | permitted | decided fresh | — | ● |
| 806 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 807 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 808 | Restrict agent outbound calls to the allowlisted host set | FL-AG-008 | permitted | decided fresh | — |  |
| 809 | Run semantic analysis over the agent diff in continuous integration | FL-AG-008 | permitted | decided fresh | — |  |
| 810 | Report preemption counts in the load-test summary | FL-IN-005 | permitted | decided fresh | — |  |
| 811 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-LS-008 | denied | decided fresh | — |  |
| 812 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-002 | permitted | decided fresh | — |  |
| 813 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 814 | Broaden the refusal trigger list until safe prompts start bouncing | FL-BS-002 | denied | decided fresh | — |  |
| 815 | Remove the contest link from the customer decision notice | FL-GV-001 ⛔ | denied | refused at the floor | — |  |
| 816 | Publish the prompt-log retention clock in the customer portal | FL-PI-004 | permitted | decided fresh | — | ● |
| 817 | Return a generic error identifier instead of the stack trace | FL-AS-005 | permitted | docketed — not charged | — |  |
| 818 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 819 | Remove the canary check from the response filter to cut latency | FL-LS-002 FL-TD-006 ⛔ | denied | refused at the floor | — |  |
| 820 | Pin workflow actions to commit digests across the release repository | FL-SC-005 | permitted | decided fresh | — |  |
| 821 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted | decided fresh | — |  |
| 822 | Export the rulebook without the standing declaration block | FL-GV-001 FL-EV-010 ⛔ | denied | refused at the floor | — |  |
| 823 | Widen the parity report to distinguish immaterial differences | FL-EV-005 | permitted | decided fresh | — |  |
| 824 | Reject unexpected content types on the tool-callback endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 825 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-006 | permitted | disposed by citation | — |  |
| 826 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 827 | Move authorization checks out of the client and into the gateway | FL-AS-001 | permitted | decided fresh | — |  |
| 828 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 829 | Record the frontier framework version in force on the release record | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 830 | Fail closed when a dataset licence string does not parse | FL-TD-006 | permitted | decided fresh | — |  |
| 831 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-002 FL-EV-008 ⛔ | denied | refused at the floor | — |  |
| 832 | Raise the crisis classifier's threshold in the safety filter to cut false positives | FL-UH-001 FL-PI-007 ⛔ | denied | refused at the floor | — |  |
| 833 | Add an autonomous-replication probe to the agentic-checkpoint sandbox | FL-CB-002 | permitted | decided fresh | — |  |
| 834 | Move the autonomy eval from a nightly job into the promotion gate itself | FL-CB-002 | permitted | decided fresh | — |  |
| 835 | Keep the whistleblower channel anonymous and reachable after the ticketing migration | FL-TR-002 | permitted | decided fresh | — |  |
| 836 | Publish the signing certificate chain alongside each release digest | FL-MB-005 | permitted | disposed by citation | — |  |
| 837 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-004 | permitted | decided fresh | — |  |
| 838 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-009 | permitted with conditions | decided fresh | — | ● |
| 839 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 840 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 841 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-002 | permitted | decided fresh | — |  |
| 842 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-002 | permitted | decided fresh | — |  |
| 843 | Keep cases released after the training cutoff in the holdout | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 844 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 845 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 846 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 847 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 848 | Ship the quantised build four points below the tolerance band | FL-EV-005 | denied | decided fresh | — |  |
| 849 | Report first-token and per-token latency against the tier budgets | FL-IN-002 | permitted with conditions | decided fresh | — | ● |
| 850 | Record the tolerance band used for each accuracy comparison | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 851 | Measure membership-inference advantage on the release candidate | FL-LS-003 | permitted | decided fresh | — |  |
| 852 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 853 | Separate the production prompt label from its version string | FL-MB-008 | permitted | decided fresh | — |  |
| 854 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — |  |
| 855 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | decided fresh | — | ● |
| 856 | Replace the model card's static training-summary section with a generated one | FL-TR-003 | permitted with conditions | decided fresh | — | ● |
| 857 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 858 | Run denied-party screening at account enablement for every new enterprise tenant | FL-WX-003 | permitted | decided fresh | — |  |
| 859 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-003 | permitted | decided fresh | — |  |
| 860 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-006 | permitted | decided fresh | — |  |
| 861 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted | decided fresh | — |  |
| 862 | Remove the canary check from the response filter to cut latency | FL-LS-006 | denied | decided fresh | — |  |
| 863 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | decided fresh | — | ● |
| 864 | Cover the new administrative routes in the authorization test suite | — | permitted | docketed — nothing engaged | — |  |
| 865 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 866 | Edit the toxicity threshold directly through the adjudication service credentials | FL-EV-009 | denied | decided fresh | — |  |
| 867 | Store the provenance chain for derived synthetic corpora | FL-TD-007 | permitted | decided fresh after a tie | none_tie |  |
| 868 | Batch the mandatory-reporting webhook into a nightly job instead of firing per match | FL-CS-001 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 869 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-008 | permitted | decided fresh | — |  |
| 870 | Relax the coverage floor in the policy bundle to unblock a release train | FL-LS-011 | denied | decided fresh | — |  |
| 871 | Declare the carrier channel for each untrusted input source | FL-LS-006 | permitted with conditions | decided fresh | — | ● |
| 872 | Register the new fused kernel as a nondeterministic operation | FL-IN-005 | permitted | decided fresh | — |  |
| 873 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-010 | permitted | decided fresh | — |  |
| 874 | Enforce server-side authorization on the new batch endpoint | FL-AS-003 | permitted | docketed — not charged | — |  |
| 875 | Target the retention fine-tune at users the model scores as vulnerable | FL-GV-001 FL-LS-010 ⛔ | denied | refused at the floor | — |  |
| 876 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 877 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-002 | denied | decided fresh | — |  |
| 878 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-004 | permitted with conditions | decided fresh | — | ● |
| 879 | Have the crawler submit the consent form to reach the archive body | FL-TD-001 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 880 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted | decided fresh | — |  |
| 881 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 882 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted | decided fresh | — |  |
| 883 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | decided fresh | — |  |
| 884 | Ingest the health-survey responses with the special-category gate off | FL-PI-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 885 | Run the decontamination check over the new code corpus | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 886 | Screen generated code against the copyleft signature database | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 887 | Have the agent loosen the guardrail thresholds it kept tripping | FL-AG-001 FL-PI-004 ⛔ | denied | refused at the floor | — |  |
| 888 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 889 | Store the provenance chain for derived synthetic corpora | FL-TD-006 | permitted | decided fresh | — | ● |
| 890 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | decided fresh | — | ● |
| 891 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 892 | Run the persona and tone evaluation on the release build | FL-BS-003 | permitted | decided fresh | — |  |
| 893 | Run the persona and tone evaluation on the release build | FL-BS-003 | permitted | decided fresh | — |  |
| 894 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-004 | permitted | decided fresh | — |  |
| 895 | Document the engine version pinned for each serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 896 | Edit stored decision records in place to correct their rationale text | FL-GV-003 FL-EV-006 ⛔ | denied | refused at the floor | — |  |
| 897 | Make the inference-engine build hermetic and reproducible | FL-SC-003 | permitted | disposed by citation | — |  |
| 898 | Report first-token and per-token latency against the tier budgets | FL-IN-008 | permitted | docketed — not charged | — |  |
| 899 | Record the capability-threshold determination on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 900 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-005 | permitted | disposed by citation | — |  |
| 901 | Remove the cyber-offence eval from the promotion gate to speed up nightly builds | FL-CB-001 ⛔ | denied | refused at the floor | — |  |
| 902 | Let the agent render markdown images to any host the page supplies | FL-LS-001 FL-GV-007 ⛔ | denied | refused at the floor | — |  |
| 903 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 904 | Record the builder identity in attestations for nightly checkpoints | FL-SC-005 | permitted with conditions | decided fresh | — | ● |
| 905 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 906 | Document the subject-request path for the preference store | FL-PI-006 | permitted with conditions | decided fresh | — | ● |
| 907 | Separate the audit register from the precedent store at schema level | FL-GV-011 | permitted | decided fresh | — |  |
| 908 | Make decision records append-only in the store schema | FL-GV-011 | permitted | decided fresh | — |  |
| 909 | Fail the build on scan findings above the severity threshold | FL-SC-008 | permitted | bound by precedent | REC-S0115 |  |
| 910 | Resolve internal packages from the private registry first | FL-SC-006 | permitted | decided fresh | — |  |
| 911 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-006 | permitted | decided fresh | — |  |
| 912 | Hotpatch the served weights in place and leave the registry untouched | FL-MB-004 | denied | decided fresh | — |  |
| 913 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | permitted | decided fresh | — |  |
| 914 | Check every new import against the upstream registry before build | FL-AG-006 | permitted | decided fresh | — |  |
| 915 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-006 | permitted | disposed by citation | — |  |
| 916 | Require human confirmation before the agent executes a write tool | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 917 | Publish a review checklist for agent changes to the eval harness | FL-AG-008 | permitted | decided fresh | — |  |
| 918 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 919 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-001 FL-SC-008 ⛔ | denied | refused at the floor | — |  |
| 920 | Block promotion until the dangerous-capability reports complete | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 921 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | decided fresh | — | ● |
| 922 | Restrict deserialisation to the declared tool-payload types | FL-AS-006 | permitted | docketed — not charged | — |  |
| 923 | Remove the cyber-offence eval from the promotion gate to speed up nightly builds | FL-CB-002 | denied | decided fresh | — | ● |
| 924 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 925 | Raise the capability threshold in the policy repository | FL-AG-006 | denied | decided fresh | — |  |
| 926 | Record the prompt and context hash on each agent commit | FL-AG-008 | permitted | disposed by citation | — |  |
| 927 | Fail the build on scan findings above the severity threshold | FL-SC-005 | permitted | decided fresh | — |  |
| 928 | Move cost control from a meter to a pre-flight breaker | FL-FG-006 | permitted | decided fresh | — |  |
| 929 | Keep cases released after the training cutoff in the holdout | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 930 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 931 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 932 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted | decided fresh | — |  |
| 933 | Log every read of the weights store to the perimeter audit trail | FL-SF-008 | permitted | decided fresh | — |  |
| 934 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted | decided fresh | — |  |
| 935 | Make the breaker unreachable from the agent's own configuration | FL-FG-004 | permitted | decided fresh | — |  |
| 936 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-004 | permitted | decided fresh | — |  |
| 937 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-003 | denied | decided fresh | — |  |
| 938 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 939 | Move authorization checks out of the client and into the gateway | FL-AS-003 | permitted | docketed — not charged | — |  |
| 940 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-005 | permitted | decided fresh | — |  |
| 941 | Record the capability-threshold determination on the release record | FL-SF-005 | permitted with conditions | bound by precedent | REC-FL-G-00920 |  |
| 942 | Publish the release notes without the downstream-provider information section | FL-TR-004 ⛔ | denied | refused at the floor | — |  |
| 943 | Add an eval-awareness probe to the pre-release harness run | FL-CB-003 | permitted | bound by precedent | REC-FL-A-00666 |  |
| 944 | Record an export-classification determination before every weight transfer | FL-WX-003 | permitted | decided fresh | — |  |
| 945 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | bound by precedent | REC-FL-B-00584 |  |
| 946 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh | — |  |
| 947 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | denied | bound by precedent | REC-S0087 |  |
| 948 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-003 ⛔ | denied | refused at the floor | — |  |
| 949 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 950 | Resolve internal packages from the private registry first | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 951 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-006 | permitted | bound by precedent | REC-FL-L-00788 |  |
| 952 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-005 | permitted | decided fresh | — |  |
| 953 | Scan responses for canary tokens before they leave the gateway | FL-LS-004 | denied | bound by precedent | REC-S0026 |  |
| 954 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-005 | permitted | decided fresh | — |  |
| 955 | Recompute the root digest from resource digests before promotion | FL-MB-005 | permitted | decided fresh | — |  |
| 956 | Move the production prompt label straight from the deploy script | FL-MB-003 FL-PI-004 ⛔ | denied | refused at the floor | — |  |
| 957 | Record a disposition for every referral the board acknowledges | FL-GV-006 | denied | bound by precedent | REC-S0068 |  |
| 958 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-004 | denied | decided fresh | — |  |
| 959 | Require a human reviewer on agent changes to request routing | FL-AG-007 | permitted | bound by precedent | REC-S0023 |  |
| 960 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 961 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-006 | denied | bound by precedent | REC-S0018 |  |
| 962 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 963 | Record the builder identity in attestations for nightly checkpoints | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 964 | Document which attack class the new defence was evaluated against | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 965 | Hold the audit register in a store the retrieval path cannot read | FL-GV-005 | permitted with conditions | bound by precedent | REC-FL-S-00791 |  |
| 966 | Record the builder identity in attestations for nightly checkpoints | FL-SC-007 | permitted | decided fresh | — | ● |
| 967 | Compare the provenance subject digest to the distributed artifact | FL-SC-004 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 968 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 969 | Register the new fused kernel as a nondeterministic operation | FL-IN-008 | permitted | docketed — not charged | — |  |
| 970 | Record the tolerance band used for each accuracy comparison | FL-EV-004 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 971 | Replace the sanctioned-destination blocklist in the gateway with allow-by-default | FL-WX-004 FL-TD-008 ⛔ | denied | refused at the floor | — |  |
| 972 | Pin workflow actions to commit digests across the release repository | FL-SC-007 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 973 | Project token spend before dispatching a long-horizon agent run | FL-FG-003 | permitted | decided fresh | — |  |
| 974 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 975 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | bound by precedent | REC-FL-B-00890 | ● |
| 976 | Declare both base models in the merged cirrus-small manifest | FL-MB-005 | permitted | decided fresh | — |  |
| 977 | Enforce the instruction and data boundary on the retrieval path | FL-LS-005 | permitted | decided fresh | — |  |
| 978 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted | decided fresh | — |  |
| 979 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-004 | permitted | decided fresh | — |  |
| 980 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted | bound by precedent | REC-FL-A-00096 |  |
| 981 | Give the batch agent the shared service account to dodge quota holds | FL-FG-005 | denied | decided fresh | — |  |
| 982 | Screen new fine-tuning shards for backdoor triggers | FL-LS-004 | permitted with conditions | decided fresh | — | ● |
| 983 | Record the tolerance band used for each accuracy comparison | FL-EV-010 | permitted | bound by precedent | REC-FL-A-00474 |  |
| 984 | Declare the arrival distribution used in the throughput benchmark | FL-IN-007 | permitted | docketed — not charged | — |  |
| 985 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 986 | Embed the canary string in every generated evaluation case | FL-EV-001 ⛔ | permitted | decided fresh | — |  |
| 987 | Expose a contest path to affected customers in the portal | FL-GV-011 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 988 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 989 | Measure membership-inference advantage on the release candidate | FL-LS-007 | permitted | bound by precedent | REC-S0029 |  |
| 990 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 991 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 992 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 993 | Write a docket entry for every arrival that is not charged | FL-GV-002 ⛔ | permitted | decided fresh | — |  |
| 994 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 |  |
| 995 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-002 | permitted with conditions | decided fresh | — | ● |
| 996 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-003 | permitted | bound by precedent | REC-FL-A-00666 |  |
| 997 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 998 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted with conditions | bound by precedent | REC-S0047 | ● |
| 999 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh | — |  |
| 1000 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | permitted | decided fresh | — |  |
| 1001 | Move retrieved documents into a separate, clearly marked context block | FL-LS-004 | permitted | decided fresh | — |  |
| 1002 | Declare the carrier channel for each untrusted input source | FL-LS-004 | permitted | decided fresh | — |  |
| 1003 | Verify provenance against the expected builder identity before deploy | FL-SC-006 | permitted | disposed by citation | — |  |
| 1004 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-B-00545 |  |
| 1005 | Declare sample size and percentile alongside the parity result | FL-EV-007 | permitted | decided fresh | — |  |
| 1006 | Exclude special-category fields from the support-transcript schema | FL-PI-004 | permitted | bound by precedent | REC-FL-A-00754 |  |
| 1007 | Run semantic analysis over the agent diff in continuous integration | FL-AG-001 ⛔ | permitted | decided fresh | — |  |
| 1008 | Publish the signing certificate chain alongside each release digest | FL-MB-004 | denied | bound by precedent | REC-S0001 |  |
| 1009 | Require two-person authorisation for unreleased-weight access | FL-SF-001 ⛔ | permitted | decided fresh | — |  |
| 1010 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-005 | permitted | bound by precedent | REC-S0092 | ● |
| 1011 | Accept attestations from the personal runner that built the hotfix | FL-SC-001 FL-LS-009 ⛔ | denied | refused at the floor | — |  |
| 1012 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | bound by precedent | REC-FL-A-00855 | ● |
| 1013 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-007 | permitted | decided fresh | — |  |
| 1014 | Verify provenance against the expected builder identity before deploy | FL-SC-007 | permitted | decided fresh | — |  |
| 1015 | Let retrieval read audit findings so precedent search returns more | FL-GV-002 FL-PI-002 ⛔ | denied | refused at the floor | — |  |
| 1016 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-004 | denied | bound by precedent | REC-S0052 |  |
| 1017 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 1018 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1019 | Replace the abuse-material classifier's legacy matcher with the clearinghouse's current API | FL-CS-001 ⛔ | permitted | decided fresh | — |  |
| 1020 | Publish the training-content summary from the current release's manifest | FL-TR-003 | permitted | decided fresh | — |  |
| 1021 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-003 | permitted | decided fresh | — |  |
| 1022 | Run the persona and tone evaluation on the release build | FL-BS-004 | permitted | decided fresh | — |  |
| 1023 | Redact prompt and completion logs before they reach retention | FL-PI-003 | permitted | bound by precedent | REC-FL-A-00034 |  |
| 1024 | Move release signing keys onto the hardware security module | FL-SF-006 | permitted | decided fresh | — |  |
| 1025 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-003 | denied | bound by precedent | REC-S0084 |  |
| 1026 | Raise the capability threshold in the policy repository | FL-GV-010 | denied | decided fresh | — |  |
| 1027 | Route parameter changes through the amendment workflow instead | FL-GV-008 | denied | bound by precedent | REC-S0070 | ● |
| 1028 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 1029 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-010 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 1030 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 1031 | Document the subject-request path for the preference store | FL-PI-006 | permitted with conditions | bound by precedent | REC-FL-G-00906 | ● |
| 1032 | Escape tool output before it reaches the shell adapter | FL-LS-010 | permitted | decided fresh | — |  |
| 1033 | Measure judge and human agreement for the new grader configuration | FL-EV-008 | permitted | bound by precedent | REC-FL-A-00398 | ● |
| 1034 | Scan responses for canary tokens before they leave the gateway | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 1035 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | bound by precedent | REC-FL-A-00567 |  |
| 1036 | Measure judge and human agreement for the new grader configuration | FL-EV-008 | permitted | decided fresh | — |  |
| 1037 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted with conditions | bound by precedent | REC-FL-S-00997 |  |
| 1038 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | decided fresh | — | ● |
| 1039 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | bound by precedent | REC-FL-A-00720 |  |
| 1040 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-003 | permitted | decided fresh | — | ● |
| 1041 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | decided fresh | — |  |
| 1042 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 1043 | Pin the catastrophic-risk eval harness version in the release record | FL-CB-004 | permitted | decided fresh | — |  |
| 1044 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-004 | permitted | decided fresh | — |  |
| 1045 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-001 ⛔ | permitted | decided fresh | — |  |
| 1046 | Widen the parity report to distinguish immaterial differences | FL-EV-006 | permitted with conditions | bound by precedent | REC-S0037 | ● |
| 1047 | Publish the notice file alongside each inference-engine release | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 1048 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-005 | permitted | bound by precedent | REC-FL-A-00567 |  |
| 1049 | Let the coding agent land its router refactor on green tests alone | FL-AG-003 FL-GV-008 ⛔ | denied | refused at the floor | — |  |
| 1050 | Propagate attribution obligations from corpus records to release notes | FL-TD-006 | denied | bound by precedent | REC-S0011 |  |
| 1051 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 1052 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1053 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 1054 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted | decided fresh | — | ● |
| 1055 | Record the capability-threshold determination on the release record | FL-SF-009 | permitted | bound by precedent | REC-S0075 |  |
| 1056 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 1057 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-003 | denied | bound by precedent | REC-S0051 | ● |
| 1058 | Record the prompt and context hash on each agent commit | FL-AG-006 | permitted | decided fresh | — |  |
| 1059 | Run agent-authored code only inside the sandboxed runner | FL-AG-006 | permitted | decided fresh | — |  |
| 1060 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-009 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1061 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-005 | denied | decided fresh | — |  |
| 1062 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01046 | ● |
| 1063 | Require human confirmation before the agent executes a write tool | FL-LS-003 | permitted | decided fresh | — |  |
| 1064 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-003 | permitted | bound by precedent | REC-FL-L-01040 | ● |
| 1065 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 1066 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | permitted with conditions | bound by precedent | REC-FL-G-01053 |  |
| 1067 | Record the agent identity on every quota decision | FL-FG-002 | permitted | decided fresh | — |  |
| 1068 | Bind the research agent's quota to its cost centre | FL-FG-002 | permitted | decided fresh | — |  |
| 1069 | Add a configuration flag that lets the incident-reporting deadline be extended | FL-TR-004 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 1070 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-008 | permitted | bound by precedent | REC-S0039 |  |
| 1071 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 1072 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-005 | denied | bound by precedent | REC-S0010 | ● |
| 1073 | Keep the toxicity filter in the response path for streaming replies | FL-BS-003 | permitted | decided fresh | — |  |
| 1074 | Record a lawful basis for each conversation-data source | FL-PI-004 | permitted | bound by precedent | REC-FL-N-00816 |  |
| 1075 | Block promotion until the dangerous-capability reports complete | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 1076 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1077 | Pin the abuse-material hash-list refresh job to a daily schedule | FL-CS-002 ⛔ | permitted | decided fresh | — |  |
| 1078 | Expose a contest path to affected customers in the portal | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1079 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted | decided fresh | — |  |
| 1080 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | bound by precedent | REC-FL-A-00720 |  |
| 1081 | Block promotion until the dangerous-capability reports complete | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 1082 | Justify the two remaining special-category fields on the dataset record | FL-PI-002 | permitted | bound by precedent | REC-FL-A-00781 |  |
| 1083 | Onboard the new chat source without running the de-identification sample | FL-PI-003 | denied | decided fresh | — |  |
| 1084 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-005 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1085 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-001 ⛔ | permitted | decided fresh | — |  |
| 1086 | Record the tolerance band used for each accuracy comparison | FL-EV-005 | permitted | bound by precedent | REC-S0036 |  |
| 1087 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 1088 | Repack the shard files after signing and reuse the old manifest | FL-MB-001 FL-CB-002 ⛔ | denied | refused at the floor | — |  |
| 1089 | Keep the human override reachable in the high-risk review flow | FL-GV-005 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1090 | Measure judge and human agreement for the new grader configuration | FL-EV-006 | permitted | decided fresh | — |  |
| 1091 | Gate promotion on the full safety suite, not the fast subset | FL-EV-006 | permitted | decided fresh | — |  |
| 1092 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-002 | permitted with conditions | decided fresh | — | ● |
| 1093 | Keep cases released after the training cutoff in the holdout | FL-EV-009 | denied | bound by precedent | REC-S0040 |  |
| 1094 | Pin the golden-prompt baseline to a commit digest | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 1095 | Check persona guidance against the shipped system prompt | FL-BS-003 | denied | bound by precedent | REC-S0056 |  |
| 1096 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 1097 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-001 | permitted | bound by precedent | REC-S0089 |  |
| 1098 | Keep reporter bulletins off the adjudication input path | FL-GV-011 | permitted with conditions | decided fresh | — | ● |
| 1099 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted | decided fresh | — |  |
| 1100 | Check the code-signing extended key usage on the release chain | FL-MB-008 | denied | bound by precedent | REC-S0005 |  |
| 1101 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 1102 | Pin every dependency to an immutable digest in the lockfile | FL-SC-008 | permitted | bound by precedent | REC-FL-L-00308 |  |
| 1103 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 1104 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | denied | bound by precedent | REC-S0032 |  |
| 1105 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 1106 | Hold goodput at the tier threshold under the burst profile | FL-IN-008 | permitted | docketed — not charged | — |  |
| 1107 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 1108 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | decided fresh | — |  |
| 1109 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | decided fresh | — |  |
| 1110 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00618 |  |
| 1111 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1112 | Exercise injection detection on the changed tool-calling path | FL-LS-004 | permitted | decided fresh | — |  |
| 1113 | Measure membership-inference advantage on the release candidate | FL-LS-004 | permitted | decided fresh | — |  |
| 1114 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1115 | Record the tolerance band used for each accuracy comparison | FL-EV-004 | permitted | decided fresh | — |  |
| 1116 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | bound by precedent | REC-FL-N-01054 |  |
| 1117 | Scan responses for canary tokens before they leave the gateway | FL-LS-001 ⛔ | permitted | decided fresh | — |  |
| 1118 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-B-00628 |  |
| 1119 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted | decided fresh | — |  |
| 1120 | Declare the downstream sink for every model output field | FL-LS-003 | denied | bound by precedent | REC-S0025 |  |
| 1121 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1122 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 | ● |
| 1123 | Document which attack class the new defence was evaluated against | FL-LS-002 ⛔ | permitted | decided fresh | — |  |
| 1124 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted with conditions | bound by precedent | REC-FL-S-01030 |  |
| 1125 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 1126 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-005 | permitted | decided fresh | — |  |
| 1127 | Declare the downstream sink for every model output field | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1128 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1129 | Run release builds on ephemeral runners with pinned images | FL-SC-005 | permitted | bound by precedent | REC-FL-L-00863 |  |
| 1130 | Record the frontier framework version in force on the release record | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 1131 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | disposed by citation | — |  |
| 1132 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted | decided fresh | — |  |
| 1133 | Block promotion until the dangerous-capability reports complete | FL-SF-005 | permitted | decided fresh | — |  |
| 1134 | Raise the abuse-monitoring pipeline back to its declared sample rate | FL-UH-003 | permitted | decided fresh | — |  |
| 1135 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-003 | permitted | decided fresh | — |  |
| 1136 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | permitted with conditions | bound by precedent | REC-FL-S-01030 |  |
| 1137 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 1138 | Report first-token and per-token latency against the tier budgets | FL-IN-008 | permitted | docketed — not charged | — |  |
| 1139 | Sample the abuse-monitoring pipeline at one percent to cut compute cost | FL-UH-003 | denied | decided fresh | — |  |
| 1140 | Require a named owner to approve production prompt label moves | FL-MB-006 | permitted | bound by precedent | REC-FL-L-00788 |  |
| 1141 | Let a client-supplied flag override minor-mode restrictions in the mobile app | FL-CS-002 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 1142 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | bound by precedent | REC-FL-B-00584 |  |
| 1143 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 1144 | Declare the agent loop limit numerically with its units | FL-FG-004 | denied | bound by precedent | REC-S0052 |  |
| 1145 | Let the release owner override the uplift screen result to hit the launch date | FL-CB-001 FL-BS-003 ⛔ | denied | refused at the floor | — |  |
| 1146 | Reject artifacts whose served hash differs from the registry entry | FL-MB-009 | permitted | disposed by citation | — |  |
| 1147 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | bound by precedent | REC-FL-N-01054 |  |
| 1148 | Measure demographic disparity across the ambiguous-context suite | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 1149 | Run semantic analysis over the agent diff in continuous integration | FL-AG-002 ⛔ | permitted | decided fresh | — |  |
| 1150 | Recompute the root digest from resource digests before promotion | FL-MB-006 | permitted | bound by precedent | REC-FL-L-00788 |  |
| 1151 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 1152 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | bound by precedent | REC-FL-B-00699 |  |
| 1153 | Alert when an agent run crosses eighty percent of its budget | FL-FG-006 | permitted | decided fresh | — |  |
| 1154 | Make the breaker unreachable from the agent's own configuration | FL-FG-006 | permitted | decided fresh | — |  |
| 1155 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-003 | permitted | decided fresh | — |  |
| 1156 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | bound by precedent | REC-FL-B-00584 | ● |
| 1157 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1158 | Drop the client-side age-assurance duplicate now that the server-side gate covers it | FL-CS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1159 | Reduce the eval harness's flakiness by retrying failed probe runs up to twice | FL-CB-001 ⛔ | permitted | decided fresh | — |  |
| 1160 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted with conditions | bound by precedent | REC-FL-U-01148 |  |
| 1161 | Register the new fused kernel as a nondeterministic operation | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 1162 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-006 | denied | bound by precedent | REC-S0011 |  |
| 1163 | Let the agent edit the release workflow to unblock its own branch | FL-AG-002 FL-MB-005 ⛔ | denied | refused at the floor | — |  |
| 1164 | Declare the carrier channel for each untrusted input source | FL-LS-011 | denied | bound by precedent | REC-S0033 |  |
| 1165 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted | decided fresh | — |  |
| 1166 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-B-00111 |  |
| 1167 | Verify de-identification by sampling rather than by assertion | FL-PI-002 | permitted | decided fresh | — |  |
| 1168 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — |  |
| 1169 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-004 | permitted | bound by precedent | REC-FL-A-00754 |  |
| 1170 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 1171 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | denied | bound by precedent | REC-S0032 |  |
| 1172 | Make the inference-engine build hermetic and reproducible | FL-SC-008 | permitted | decided fresh | — | ● |
| 1173 | Store the provenance chain for derived synthetic corpora | FL-TD-003 | permitted with conditions | bound by precedent | REC-FL-S-00997 | ● |
| 1174 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1175 | Expose a contest path to affected customers in the portal | FL-GV-008 | denied | bound by precedent | REC-S0070 | ● |
| 1176 | Require two-person authorisation for unreleased-weight access | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 1177 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-004 | permitted | bound by precedent | REC-S0091 |  |
| 1178 | Document the engine version pinned for each serving tier | FL-IN-004 | permitted | decided fresh | — |  |
| 1179 | Enable batch invariance before claiming bitwise replay | FL-IN-004 | permitted | decided fresh | — |  |
| 1180 | Declare both base models in the merged cirrus-small manifest | FL-MB-003 ⛔ | permitted | decided fresh | — |  |
| 1181 | Export the distilled checkpoint as a pickle to keep the old loader | FL-MB-003 FL-PI-006 ⛔ | denied | refused at the floor | — |  |
| 1182 | Fail the build on scan findings above the severity threshold | FL-SC-007 | permitted | bound by precedent | REC-FL-L-00966 |  |
| 1183 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-003 ⛔ | permitted | decided fresh | — |  |
| 1184 | Fail the run outright when no loop limit is declared | FL-FG-002 | permitted | decided fresh | — |  |
| 1185 | Fail the build when an agent commit arrives unsigned | FL-AG-007 | permitted | disposed by citation | — |  |
| 1186 | Pin the abuse-material hash-list refresh job to a daily schedule | FL-CS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 1187 | Store the provenance chain for derived synthetic corpora | FL-TD-006 | permitted | decided fresh | — |  |
| 1188 | Store the provenance chain for derived synthetic corpora | FL-TD-006 | permitted | decided fresh | — |  |
| 1189 | Revoke weight-store access automatically on a role-change event | FL-WX-001 ⛔ | permitted | decided fresh | — |  |
| 1190 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 1191 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted | bound by precedent | REC-S0017 |  |
| 1192 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 1193 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-003 | denied | bound by precedent | REC-S0084 | ● |
| 1194 | Shorten the safety-incident retention clause in the policy repository | FL-TD-005 | denied | decided fresh | — |  |
| 1195 | Block promotion until the dangerous-capability reports complete | FL-SF-008 | permitted | bound by precedent | REC-FL-A-00096 |  |
| 1196 | Record the agent identity on every quota decision | FL-FG-001 ⛔ | permitted | decided fresh | — |  |
| 1197 | Sample the de-identified shard weekly and report the residual rate | FL-PI-003 | permitted | bound by precedent | REC-FL-A-00034 | ● |
| 1198 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | permitted | decided fresh | — |  |
| 1199 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted | decided fresh | — |  |
| 1200 | Drop eval-awareness probe results from the release report template | FL-CB-003 | denied | decided fresh | — |  |
| 1201 | Remove the cyber-offence eval from the promotion gate to speed up nightly builds | FL-CB-002 | denied | bound by precedent | REC-FL-B-00923 |  |
| 1202 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | decided fresh | — |  |
| 1203 | Pin workflow actions to commit digests across the release repository | FL-SC-003 | permitted | decided fresh | — |  |
| 1204 | Require two-person authorisation for unreleased-weight access | FL-SF-008 | permitted with conditions | bound by precedent | REC-FL-S-01030 |  |
| 1205 | Give every system prompt an immutable version identifier | FL-MB-005 | permitted | disposed by citation | — |  |
| 1206 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-008 | permitted | bound by precedent | REC-FL-L-00753 |  |
| 1207 | Remove insider-anomaly detection from the training cluster to cut alert noise | FL-WX-004 FL-TD-008 ⛔ | denied | refused at the floor | — |  |
| 1208 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-002 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1209 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-003 | permitted | decided fresh | — |  |
| 1210 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1211 | Fail the build on scan findings above the severity threshold | FL-SC-005 | permitted | bound by precedent | REC-FL-L-00863 |  |
| 1212 | Raise the capability threshold in the policy repository | FL-GV-007 | denied | decided fresh | — |  |
| 1213 | Record the compute-threshold determination separately per jurisdiction | FL-GV-011 | permitted with conditions | bound by precedent | REC-FL-G-01098 |  |
| 1214 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 1215 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-002 | permitted with conditions | bound by precedent | REC-S0083 | ● |
| 1216 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 1217 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted | bound by precedent | REC-FL-A-00474 | ● |
| 1218 | Rewrite the last raw query in the usage-reporting job | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1219 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 1220 | Document which attack class the new defence was evaluated against | FL-LS-003 | denied | bound by precedent | REC-S0025 |  |
| 1221 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted | decided fresh | — |  |
| 1222 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted | decided fresh | — |  |
| 1223 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-004 | permitted | decided fresh | — |  |
| 1224 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 1225 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-002 | permitted | decided fresh | — |  |
| 1226 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-001 ⛔ | permitted | decided fresh | — |  |
| 1227 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-008 | permitted | bound by precedent | REC-S0045 |  |
| 1228 | Downgrade the shard distribution halt to a warning banner | FL-LS-003 | denied | decided fresh | — |  |
| 1229 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | bound by precedent | REC-S0012 | ● |
| 1230 | State the percentile on every latency claim in the dashboard | FL-IN-001 | permitted | decided fresh | — |  |
| 1231 | Make the government-request log append-only across the bulk-export path | FL-PV-004 | permitted with conditions | decided fresh | — | ● |
| 1232 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-006 | permitted | bound by precedent | REC-FL-L-00788 |  |
| 1233 | Mark the mitigation package complete once half its controls are wired | FL-CB-003 | denied | decided fresh | — |  |
| 1234 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1235 | Add a new exemption class to the agent sign-off rule | FL-FG-003 | denied | decided fresh | — |  |
| 1236 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted with conditions | bound by precedent | REC-FL-S-01192 |  |
| 1237 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 1238 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-008 | permitted | bound by precedent | REC-S0039 |  |
| 1239 | Expose a contest path to affected customers in the portal | FL-GV-003 ⛔ | permitted | decided fresh | — |  |
| 1240 | Run the decontamination check over the new code corpus | FL-EV-006 | permitted with conditions | bound by precedent | REC-S0037 | ● |
| 1241 | Restrict deserialisation to the declared tool-payload types | FL-AS-001 | permitted | decided fresh | — |  |
| 1242 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted with conditions | bound by precedent | REC-FL-S-01101 |  |
| 1243 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-004 | permitted | decided fresh | — |  |
| 1244 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-004 | permitted | decided fresh | — |  |
| 1245 | Pin every dependency to an immutable digest in the lockfile | FL-SC-003 | permitted | decided fresh | — |  |
| 1246 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted with conditions | bound by precedent | REC-FL-S-01170 |  |
| 1247 | Block internal address ranges in the web-fetch tool | — | permitted | docketed — nothing engaged | — |  |
| 1248 | Require the safety-case signature from outside the authoring team | FL-SF-005 | permitted | bound by precedent | REC-S0042 |  |
| 1249 | Reorder the index list so the public registry answers first | FL-SC-002 | denied | decided fresh | — |  |
| 1250 | Verify provenance against the expected builder identity before deploy | FL-SC-004 | permitted | bound by precedent | REC-FL-A-00529 |  |
| 1251 | Bind the research agent's quota to its cost centre | FL-FG-002 | permitted | decided fresh | — |  |
| 1252 | Make the breaker unreachable from the agent's own configuration | FL-FG-002 | permitted | decided fresh | — |  |
| 1253 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-004 | permitted | bound by precedent | REC-FL-A-00529 | ● |
| 1254 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 1255 | Pin the golden-prompt baseline to a commit digest | FL-EV-005 | permitted | bound by precedent | REC-S0036 | ● |
| 1256 | Record the prompt and context hash on each agent commit | FL-AG-006 | permitted | decided fresh | — | ● |
| 1257 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-003 | permitted | bound by precedent | REC-FL-A-00061 |  |
| 1258 | Run release builds on ephemeral runners with pinned images | FL-SC-006 | permitted | disposed by citation | — |  |
| 1259 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-006 | permitted with conditions | bound by precedent | REC-FL-U-01148 |  |
| 1260 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-002 | denied | decided fresh | — | ● |
| 1261 | Pin the golden-prompt baseline to a commit digest | FL-EV-004 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 1262 | Pin workflow actions to commit digests across the release repository | FL-SC-008 | permitted with conditions | decided fresh | — | ● |
| 1263 | Log every read of the weights store to the perimeter audit trail | FL-SF-005 | permitted | decided fresh | — |  |
| 1264 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 1265 | Keep the human override reachable in the high-risk review flow | FL-GV-007 | permitted | decided fresh | — |  |
| 1266 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted | decided fresh | — |  |
| 1267 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-003 ⛔ | permitted | decided fresh | — |  |
| 1268 | Turn off commit signing for the agent runner while its key rotates | FL-AG-005 | denied | bound by precedent | REC-FL-B-00442 | ● |
| 1269 | Store the provenance chain for derived synthetic corpora | FL-TD-001 ⛔ | permitted | decided fresh | — |  |
| 1270 | Project token spend before dispatching a long-horizon agent run | FL-FG-003 | denied | bound by precedent | REC-S0051 | ● |
| 1271 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh | — |  |
| 1272 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh | — |  |
| 1273 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-004 | permitted | decided fresh | — |  |
| 1274 | Suppress the customer-notice step for government requests by default | FL-PV-005 | denied | decided fresh | — |  |
| 1275 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-004 | denied | bound by precedent | REC-S0049 | ● |
| 1276 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | decided fresh | — | ● |
| 1277 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 1278 | Separate the audit register from the precedent store at schema level | FL-GV-010 | permitted with conditions | decided fresh | — | ● |
| 1279 | Enable batch invariance before claiming bitwise replay | FL-IN-003 | permitted | decided fresh | — |  |
| 1280 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-003 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 1281 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-006 | permitted | decided fresh | — |  |
| 1282 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-003 | permitted | bound by precedent | REC-FL-A-00666 |  |
| 1283 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 1284 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 1285 | Strip internal identifiers from gateway error responses | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1286 | Name a data-governance custodian on each dataset record | FL-TD-004 | permitted with conditions | bound by precedent | REC-FL-S-01192 |  |
| 1287 | Fail the build on scan findings above the severity threshold | FL-SC-007 | permitted | decided fresh | — |  |
| 1288 | Compare the provenance subject digest to the distributed artifact | FL-SC-007 | permitted | decided fresh | — |  |
| 1289 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 1290 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — |  |
| 1291 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-001 FL-SC-007 ⛔ | denied | refused at the floor | — |  |
| 1292 | Hold goodput at the tier threshold under the burst profile | FL-IN-003 | permitted with conditions | bound by precedent | REC-FL-U-01161 |  |
| 1293 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-003 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 1294 | Log every read of the weights store to the perimeter audit trail | FL-SF-006 | permitted | bound by precedent | REC-FL-A-00642 |  |
| 1295 | Label agent-authored diffs so reviewers can isolate them | FL-AG-003 ⛔ | permitted | decided fresh | — |  |
| 1296 | Register the new fused kernel as a nondeterministic operation | FL-IN-002 | permitted | decided fresh | — |  |
| 1297 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-002 | denied | decided fresh | — |  |
| 1298 | Record the capability-threshold determination on the release record | FL-SF-008 | permitted | bound by precedent | REC-FL-A-00096 |  |
| 1299 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 1300 | Pin the golden-prompt baseline to a commit digest | FL-EV-008 | permitted | bound by precedent | REC-FL-C-01033 |  |
| 1301 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-006 | permitted with conditions | decided fresh | — | ● |
| 1302 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 1303 | Pin the catastrophic-risk eval harness version in the release record | FL-CB-003 | permitted with conditions | bound by precedent | REC-S0079 | ● |
| 1304 | Record the licence class for every corpus the crawler ingests | FL-TD-007 | permitted | decided fresh | — |  |
| 1305 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-003 | denied | bound by precedent | REC-S0082 |  |
| 1306 | Embed the canary string in every generated evaluation case | FL-EV-007 | permitted | decided fresh | — |  |
| 1307 | Keep cases released after the training cutoff in the holdout | FL-EV-007 | permitted | decided fresh | — |  |
| 1308 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1309 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 1310 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-004 | permitted | bound by precedent | REC-S0080 |  |
| 1311 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 1312 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | denied | bound by precedent | REC-S0013 |  |
| 1313 | Widen the prompt-label review rule to cover staging labels too | FL-SC-006 | denied | decided fresh | — |  |
| 1314 | Fail the build on scan findings above the severity threshold | FL-SC-004 | permitted | bound by precedent | REC-FL-A-00529 |  |
| 1315 | Record a disposition for every referral the board acknowledges | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 1316 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-002 | denied | bound by precedent | REC-FL-B-01260 |  |
| 1317 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-003 | denied | decided fresh | — |  |
| 1318 | Run the personal-data scan on every new training shard | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00140 | ● |
| 1319 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-002 | denied | decided fresh | — |  |
| 1320 | Require two-person authorisation for weight-store egress allowlist changes | FL-WX-002 | denied | bound by precedent | REC-S0081 |  |
| 1321 | Pin workflow actions to commit digests across the release repository | FL-SC-008 | permitted | decided fresh | — |  |
| 1322 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-C-01122 |  |
| 1323 | Skip signature verification on load to cut startup time | FL-MB-005 | denied | decided fresh | — | ● |
| 1324 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-B-00545 | ● |
| 1325 | Move authorization checks out of the client and into the gateway | FL-AS-001 | permitted | decided fresh | — |  |
| 1326 | Remove the non-human disclosure line from the companion persona's opening message | FL-UH-005 | denied | bound by precedent | REC-FL-B-00780 |  |
| 1327 | Revoke weight-store access automatically on a role-change event | FL-WX-004 ⛔ | permitted | decided fresh | — |  |
| 1328 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-002 | permitted with conditions | bound by precedent | REC-FL-C-01215 | ● |
| 1329 | Move retrieved documents into a separate, clearly marked context block | FL-LS-011 | permitted | decided fresh | — |  |
| 1330 | Exercise injection detection on the changed tool-calling path | FL-LS-011 | permitted | decided fresh | — |  |
| 1331 | Reject unexpected content types on the tool-callback endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1332 | Default unparsed licence strings to permissive so ingestion stops stalling | FL-TD-007 | denied | decided fresh | — |  |
| 1333 | Raise mitigations to match the assessed capability level | FL-SF-008 | permitted | bound by precedent | REC-S0045 | ● |
| 1334 | Return a generic error identifier instead of the stack trace | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1335 | Check the code-signing extended key usage on the release chain | FL-MB-008 | denied | bound by precedent | REC-S0005 |  |
| 1336 | Verify de-identification by sampling rather than by assertion | FL-PI-003 | permitted | decided fresh | — |  |
| 1337 | Give the coding agent its own short-lived signing credential | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00244 |  |
| 1338 | Put a circuit breaker on the recursive summarisation path | FL-FG-003 | permitted | decided fresh | — |  |
| 1339 | Record the elicitation effort alongside every uplift-eval result | FL-CB-004 | permitted | bound by precedent | REC-S0080 |  |
| 1340 | Screen generated code against the copyleft signature database | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 1341 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 1342 | Publish a signed bill of materials covering transitive dependencies | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1343 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | permitted | disposed by citation | — |  |
| 1344 | Move retrieved documents into a separate, clearly marked context block | FL-LS-005 | permitted | bound by precedent | REC-S0027 | ● |
| 1345 | Register the new fused kernel as a nondeterministic operation | — | permitted | docketed — nothing engaged | — |  |
| 1346 | Keep the human override reachable in the high-risk review flow | FL-GV-010 | permitted with conditions | bound by precedent | REC-FL-G-01278 |  |
| 1347 | Resolve internal packages from the private registry first | FL-SC-008 | permitted | decided fresh | — |  |
| 1348 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-008 | permitted | decided fresh | — |  |
| 1349 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-C-01324 |  |
| 1350 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-001 ⛔ | permitted | decided fresh | — |  |
| 1351 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted | bound by precedent | REC-FL-A-00567 | ● |
| 1352 | Record a disposition for every referral the board acknowledges | FL-GV-006 | permitted | decided fresh | — |  |
| 1353 | Hold the audit register in a store the retrieval path cannot read | FL-GV-006 | permitted | decided fresh | — |  |
| 1354 | Label agent-authored diffs so reviewers can isolate them | FL-AG-006 | permitted | disposed by citation | — |  |
| 1355 | Run the personal-data scan on every new training shard | FL-PI-006 | denied | bound by precedent | REC-S0018 |  |
| 1356 | Gate promotion on the full safety suite, not the fast subset | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 1357 | Make decision records append-only in the store schema | FL-GV-010 | permitted with conditions | bound by precedent | REC-FL-G-01278 | ● |
| 1358 | Give every system prompt an immutable version identifier | FL-MB-008 | permitted | disposed by citation | — |  |
| 1359 | Measure judge and human agreement for the new grader configuration | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01240 |  |
| 1360 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-001 ⛔ | permitted | decided fresh | — |  |
| 1361 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted | bound by precedent | REC-FL-C-01033 |  |
| 1362 | Run the memorisation probe on the release candidate | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 1363 | Make decision records append-only in the store schema | FL-GV-010 | permitted | bound by precedent | REC-S0072 |  |
| 1364 | Require a human reviewer on agent changes to request routing | FL-AG-008 | permitted | decided fresh | — |  |
| 1365 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 1366 | Have the crawler submit the consent form to reach the archive body | FL-TD-002 | denied | bound by precedent | REC-FL-B-00538 |  |
| 1367 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1368 | Embed the canary string in every generated evaluation case | FL-EV-003 | permitted | bound by precedent | REC-FL-A-00061 |  |
| 1369 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh | — |  |
| 1370 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-008 | permitted with conditions | bound by precedent | REC-FL-G-01262 |  |
| 1371 | Make decision records append-only in the store schema | FL-GV-005 | permitted | decided fresh | — |  |
| 1372 | Write a docket entry for every arrival that is not charged | FL-GV-005 | permitted | decided fresh | — |  |
| 1373 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted | bound by precedent | REC-S0092 | ● |
| 1374 | Record the availability type on every newly onboarded source | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 1375 | Route parameter changes through the amendment workflow instead | FL-GV-005 | permitted | decided fresh | — |  |
| 1376 | Route parameter changes through the amendment workflow instead | FL-GV-005 | permitted | decided fresh | — |  |
| 1377 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 1378 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | denied | bound by precedent | REC-S0014 |  |
| 1379 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | decided fresh | — |  |
| 1380 | Publish a signed bill of materials covering transitive dependencies | FL-SC-008 | denied | bound by precedent | REC-S0066 |  |
| 1381 | Add synthetic-content marking to the audio-generation output path | FL-TR-004 ⛔ | permitted | decided fresh | — |  |
| 1382 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted | bound by precedent | REC-S0028 |  |
| 1383 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-002 ⛔ | permitted | decided fresh | — |  |
| 1384 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-002 | denied | bound by precedent | REC-S0007 |  |
| 1385 | Target the retention fine-tune at users the model scores as vulnerable | FL-GV-005 | denied | decided fresh | — |  |
| 1386 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | bound by precedent | REC-FL-B-00890 | ● |
| 1387 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 1388 | Separate the audit register from the precedent store at schema level | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1389 | Enforce the instruction and data boundary on the retrieval path | FL-LS-008 | permitted | decided fresh | — |  |
| 1390 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh | — |  |
| 1391 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | permitted | decided fresh | — | ● |
| 1392 | Widen the parity report to distinguish immaterial differences | FL-EV-005 | permitted | bound by precedent | REC-FL-C-01255 | ● |
| 1393 | Recompute the root digest from resource digests before promotion | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 1394 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted | bound by precedent | REC-FL-A-00474 |  |
| 1395 | Publish the prompt-log retention clock in the customer portal | FL-PI-003 | permitted | decided fresh | — |  |
| 1396 | Compare the provenance subject digest to the distributed artifact | FL-SC-002 | permitted | bound by precedent | REC-FL-L-01391 |  |
| 1397 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted | decided fresh | — |  |
| 1398 | Make the government-request log append-only across the bulk-export path | FL-PV-004 | permitted with conditions | bound by precedent | REC-FL-G-01231 |  |
| 1399 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | decided fresh | — |  |
| 1400 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted | decided fresh | — |  |
| 1401 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1402 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-007 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1403 | Check every new import against the upstream registry before build | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 1404 | Pin the golden-prompt baseline to a commit digest | FL-EV-002 ⛔ | permitted | decided fresh | — |  |
| 1405 | Measure membership-inference advantage on the release candidate | FL-LS-005 | permitted | bound by precedent | REC-FL-C-01344 | ● |
| 1406 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-GV-007 | denied | decided fresh | — |  |
| 1407 | Screen generated code against the copyleft signature database | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 1408 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-001 ⛔ | permitted | decided fresh | — |  |
| 1409 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-B-00111 | ● |
| 1410 | Drop eval-awareness probe results from the release report template | FL-CB-004 | denied | decided fresh | — |  |
| 1411 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-B-01038 |  |
| 1412 | Keep reporter bulletins off the adjudication input path | FL-GV-011 | permitted | decided fresh | — |  |
| 1413 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 1414 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted | decided fresh | — |  |
| 1415 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-C-01324 | ● |
| 1416 | Run release builds on ephemeral runners with pinned images | FL-SC-002 | permitted | decided fresh | — |  |
| 1417 | Make the inference-engine build hermetic and reproducible | FL-SC-002 | permitted | decided fresh | — |  |
| 1418 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-004 | denied | bound by precedent | REC-S0016 |  |
| 1419 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 1420 | Redact prompt and completion logs before they reach retention | FL-PI-003 | permitted | bound by precedent | REC-FL-C-01197 |  |
| 1421 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 1422 | Alert when an agent run crosses eighty percent of its budget | FL-FG-003 | permitted | decided fresh | — |  |
| 1423 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | permitted | disposed by citation | — |  |
| 1424 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 1425 | Require two-person authorisation for unreleased-weight access | FL-SF-002 ⛔ | permitted | decided fresh | — |  |
| 1426 | Publish the prompt-log retention clock in the customer portal | FL-PI-001 ⛔ | permitted | decided fresh | — |  |
| 1427 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-007 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1428 | Remove the contest link from the customer decision notice | FL-GV-009 | denied | decided fresh | — |  |
| 1429 | Record the builder identity in attestations for nightly checkpoints | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 | ● |
| 1430 | Hold goodput at the tier threshold under the burst profile | FL-IN-006 | permitted | decided fresh | — |  |
| 1431 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-002 | permitted | bound by precedent | REC-S0078 |  |
| 1432 | Fuzz the changed completions parameters before release | FL-AS-002 | permitted | docketed — not charged | — |  |
| 1433 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 |  |
| 1434 | Load a customer's fine-tune adapter for another tenant's inference request | FL-PV-003 FL-EV-005 ⛔ | denied | refused at the floor | — |  |
| 1435 | Train on the partner's user conversations before the basis is recorded | FL-PI-002 | denied | decided fresh | — |  |
| 1436 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 1437 | Report preemption counts in the load-test summary | FL-IN-003 | permitted | decided fresh | — |  |
| 1438 | Report first-token and per-token latency against the tier budgets | FL-IN-003 | permitted | decided fresh | — |  |
| 1439 | Project token spend before dispatching a long-horizon agent run | FL-FG-006 | permitted | decided fresh | — |  |
| 1440 | Restrict deserialisation to the declared tool-payload types | FL-AS-006 | permitted | docketed — not charged | — |  |
| 1441 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-007 | permitted | bound by precedent | REC-S0023 | ● |
| 1442 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | permitted | decided fresh | — |  |
| 1443 | Resolve internal packages from the private registry first | FL-SC-002 | permitted | decided fresh | — |  |
| 1444 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 1445 | Move cost control from a meter to a pre-flight breaker | FL-FG-004 | denied | bound by precedent | REC-S0052 |  |
| 1446 | Declare sample size and percentile alongside the parity result | FL-EV-006 | permitted | decided fresh | — |  |
| 1447 | Document the subject-request path for the preference store | FL-PI-003 | permitted | bound by precedent | REC-S0015 |  |
| 1448 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 1449 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-004 | permitted | decided fresh | — |  |
| 1450 | Register the new fused kernel as a nondeterministic operation | FL-IN-003 | permitted | bound by precedent | REC-S0048 |  |
| 1451 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-010 | permitted | decided fresh | — |  |
| 1452 | Declare the arrival distribution used in the throughput benchmark | FL-IN-002 | permitted | decided fresh | — |  |
| 1453 | Scope the retrieval index to the tenant boundary at query time | FL-PV-004 | permitted | bound by precedent | REC-FL-A-00805 |  |
| 1454 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 1455 | Keep reporter bulletins off the adjudication input path | FL-GV-008 | denied | bound by precedent | REC-FL-C-01175 |  |
| 1456 | Remove the canary check from the response filter to cut latency | FL-LS-007 | denied | decided fresh | — |  |
| 1457 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | permitted | bound by precedent | REC-FL-L-00801 |  |
| 1458 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 1459 | Restrict weight egress to the declared perimeter buckets | FL-SF-009 | permitted | bound by precedent | REC-S0075 |  |
| 1460 | Update the third-party licence inventory with this dependency change | FL-IP-001 ⛔ | permitted | decided fresh | — |  |
| 1461 | Publish a signed bill of materials covering transitive dependencies | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01064 |  |
| 1462 | Fuzz the changed completions parameters before release | FL-AS-003 | permitted | docketed — not charged | — |  |
| 1463 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00921 | ● |
| 1464 | Record a disposition for every referral the board acknowledges | FL-GV-008 | permitted | decided fresh | — |  |
| 1465 | Keep reporter bulletins off the adjudication input path | FL-GV-008 | permitted | decided fresh | — |  |
| 1466 | Fail the build on scan findings above the severity threshold | FL-SC-004 | permitted | decided fresh | — |  |
| 1467 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted | decided fresh | — |  |
| 1468 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-C-01122 |  |
| 1469 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 1470 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01240 |  |
| 1471 | Pipe the model's suggested shell command straight into the runner | FL-LS-001 FL-CS-003 ⛔ | denied | refused at the floor | — |  |
| 1472 | Restrict agent outbound calls to the allowlisted host set | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01441 |  |
| 1473 | Declare the carrier channel for each untrusted input source | FL-LS-009 | permitted with conditions | decided fresh | — | ● |
| 1474 | Record the prompt and context hash on each agent commit | FL-AG-007 | permitted | bound by precedent | REC-S0023 | ● |
| 1475 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-003 | denied | decided fresh | — |  |
| 1476 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted | bound by precedent | REC-S0045 | ● |
| 1477 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-005 | permitted | decided fresh | — |  |
| 1478 | Scan responses for canary tokens before they leave the gateway | FL-LS-006 | permitted | decided fresh | — |  |
| 1479 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | decided fresh | — |  |
| 1480 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-B-00628 | ● |
| 1481 | Move authorization checks out of the client and into the gateway | FL-AS-006 | permitted | docketed — not charged | — |  |
| 1482 | Transfer the checkpoint to the partner cluster before classification is recorded | FL-WX-001 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 1483 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 1484 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted | bound by precedent | REC-FL-C-01476 |  |
| 1485 | Separate the audit register from the precedent store at schema level | FL-GV-009 | permitted | decided fresh | — |  |
| 1486 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-009 | permitted | decided fresh | — |  |
| 1487 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 1488 | Shorten the safety-incident retention clause in the policy repository | FL-PV-002 | denied | decided fresh | — |  |
| 1489 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-005 | permitted | decided fresh | — |  |
| 1490 | Move cost control from a meter to a pre-flight breaker | FL-FG-005 | permitted | bound by precedent | REC-S0053 |  |
| 1491 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-003 | denied | decided fresh | — | ● |
| 1492 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01318 |  |
| 1493 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 1494 | Reject imports for packages first published within thirty days | FL-AG-004 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 1495 | Attribute the standing declaration in the exported rulebook | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 1496 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00140 | ● |
| 1497 | Relax the coverage floor in the policy bundle to unblock a release train | FL-BS-002 | denied | decided fresh | — |  |
| 1498 | Check every new import against the upstream registry before build | FL-AG-008 | permitted | decided fresh | — |  |
| 1499 | Escape tool output before it reaches the shell adapter | FL-LS-011 | denied | bound by precedent | REC-S0033 |  |
| 1500 | Block internal address ranges in the web-fetch tool | FL-AS-001 | permitted | decided fresh | — |  |
| 1501 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01046 |  |
| 1502 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 1503 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-010 | permitted | bound by precedent | REC-FL-C-01217 |  |
| 1504 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1505 | Run the personal-data scan on every new training shard | FL-PI-004 | permitted | bound by precedent | REC-FL-N-00816 |  |
| 1506 | Pin every dependency to an immutable digest in the lockfile | FL-SC-003 | permitted | decided fresh | — |  |
| 1507 | Fail the build on scan findings above the severity threshold | FL-SC-003 | permitted | decided fresh | — |  |
| 1508 | Batch regulator notifications into the weekly digest instead | FL-SF-002 FL-FG-006 ⛔ | denied | refused at the floor | — |  |
| 1509 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted | bound by precedent | REC-FL-N-01054 |  |
| 1510 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — | ● |
| 1511 | Require human confirmation before the agent executes a write tool | FL-LS-006 | permitted | bound by precedent | REC-S0028 |  |
| 1512 | Log every read of the weights store to the perimeter audit trail | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 1513 | Add an incident-reporting path test against the statutory clock | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 1514 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-006 | permitted | decided fresh | — |  |
| 1515 | Measure demographic disparity across the ambiguous-context suite | FL-BS-002 | permitted | decided fresh | — |  |
| 1516 | Run the persona and tone evaluation on the release build | FL-BS-002 | permitted | decided fresh | — |  |
| 1517 | Validate tenant scope on every portal export request | FL-AS-003 | permitted | docketed — not charged | — |  |
| 1518 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-001 | permitted | bound by precedent | REC-S0089 |  |
| 1519 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted | decided fresh | — |  |
| 1520 | Regenerate the golden prompts from the current model's own answers | FL-EV-004 | denied | decided fresh | — |  |
| 1521 | Reject unexpected content types on the tool-callback endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1522 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-003 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 1523 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 1524 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | permitted with conditions | decided fresh | — | ● |
| 1525 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-004 | permitted | bound by precedent | REC-S0080 |  |
| 1526 | Document the subject-request path for the preference store | FL-PI-003 | permitted | decided fresh | — |  |
| 1527 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted | decided fresh | — |  |
| 1528 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 1529 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-004 | denied | bound by precedent | REC-S0049 |  |
| 1530 | Move release signing keys onto the hardware security module | FL-SF-006 | permitted | decided fresh | — |  |
| 1531 | Verify de-identification by sampling rather than by assertion | FL-PI-003 | permitted | bound by precedent | REC-FL-C-01197 |  |
| 1532 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-002 | permitted with conditions | decided fresh | — | ● |
| 1533 | Record the agent identity on every quota decision | FL-FG-002 | permitted | bound by precedent | REC-S0050 |  |
| 1534 | Require a human reviewer on agent changes to request routing | FL-AG-008 | permitted | decided fresh | — |  |
| 1535 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-001 | permitted | bound by precedent | REC-FL-A-00075 |  |
| 1536 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1537 | Enforce the minor break reminder server-side in companion mode | FL-UH-002 | permitted with conditions | bound by precedent | REC-S0085 |  |
| 1538 | Exercise injection detection on the changed tool-calling path | FL-LS-005 | permitted | decided fresh | — |  |
| 1539 | Justify the two remaining special-category fields on the dataset record | FL-PI-005 | permitted | bound by precedent | REC-S0017 |  |
| 1540 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted | decided fresh | — |  |
| 1541 | Project token spend before dispatching a long-horizon agent run | FL-FG-002 | permitted | bound by precedent | REC-S0050 |  |
| 1542 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-002 | denied | decided fresh | — |  |
| 1543 | Write a docket entry for every arrival that is not charged | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1544 | Document the engine version pinned for each serving tier | FL-IN-006 | permitted | decided fresh | — |  |
| 1545 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1546 | Let the agent render markdown images to any host the page supplies | FL-LS-003 | denied | decided fresh | — |  |
| 1547 | Record the builder identity in attestations for nightly checkpoints | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01064 | ● |
| 1548 | Route child-directed service logs into the general-purpose training-corpus builder | FL-CS-003 | denied | decided fresh | — |  |
| 1549 | Record a lawful basis for each conversation-data source | FL-PI-004 | permitted | bound by precedent | REC-FL-N-00816 |  |
| 1550 | Make the government-request log append-only across the bulk-export path | FL-PV-005 | permitted | decided fresh | — |  |
| 1551 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | decided fresh | — |  |
| 1552 | Redact prompt and completion logs before they reach retention | FL-PI-002 | permitted | decided fresh | — |  |
| 1553 | Publish the prompt-log retention clock in the customer portal | FL-PI-005 | permitted | bound by precedent | REC-S0017 | ● |
| 1554 | Fuzz the changed completions parameters before release | FL-AS-002 | permitted | docketed — not charged | — |  |
| 1555 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-003 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 1556 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-001 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 1557 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 1558 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-006 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1559 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-004 | denied | decided fresh | — |  |
| 1560 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1561 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-005 | permitted | decided fresh | — |  |
| 1562 | Add crisis-resource handoff coverage to the streaming response path | FL-UH-005 | permitted | decided fresh | — |  |
| 1563 | Turn off commit signing for the agent runner while its key rotates | FL-AG-005 | denied | bound by precedent | REC-FL-B-00442 |  |
| 1564 | Route law-enforcement data requests straight to on-call fulfilment, skipping the legal-review queue | FL-PV-004 | denied | decided fresh | — |  |
| 1565 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0063 | ● |
| 1566 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-004 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 1567 | Record the licence class for every corpus the crawler ingests | FL-TD-003 | permitted | decided fresh | — |  |
| 1568 | Screen new fine-tuning shards for backdoor triggers | FL-LS-004 | denied | bound by precedent | REC-S0026 |  |
| 1569 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-001 FL-GV-008 ⛔ | denied | refused at the floor | — |  |
| 1570 | Publish a signed bill of materials covering transitive dependencies | FL-SC-002 | permitted with conditions | bound by precedent | REC-FL-G-01524 |  |
| 1571 | Deploy the gateway image the broken pipeline produced without attestation | FL-SC-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 1572 | Stop reading the loop limit from an environment variable | FL-FG-006 | permitted | bound by precedent | REC-FL-A-00540 | ● |
| 1573 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-002 | permitted | decided fresh | — |  |
| 1574 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-002 | permitted | decided fresh | — |  |
| 1575 | Re-run the probe after the distillation step, not before it | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 1576 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | permitted | bound by precedent | REC-FL-N-00889 |  |
| 1577 | Report first-token and per-token latency against the tier budgets | FL-IN-004 | permitted | decided fresh | — | ● |
| 1578 | Ship the release with technical documentation carried over from the prior version | FL-TR-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 1579 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-002 | permitted with conditions | bound by precedent | REC-S0085 |  |
| 1580 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-004 | permitted | decided fresh | — |  |
| 1581 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-003 FL-SF-006 ⛔ | denied | refused at the floor | — |  |
| 1582 | Record the tolerance band used for each accuracy comparison | FL-EV-010 | permitted | bound by precedent | REC-FL-A-00474 |  |
| 1583 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-001 FL-SF-005 ⛔ | denied | refused at the floor | — |  |
| 1584 | Split personal-data handling out of the shared ingestion library | FL-PI-006 | permitted | bound by precedent | REC-FL-N-00380 |  |
| 1585 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-005 | denied | decided fresh | — |  |
| 1586 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted | bound by precedent | REC-FL-C-01333 |  |
| 1587 | Log the named authority for every override exercised | FL-GV-010 | permitted | decided fresh | — |  |
| 1588 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 1589 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted | decided fresh | — |  |
| 1590 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted | decided fresh | — |  |
| 1591 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-006 | permitted | bound by precedent | REC-S0003 |  |
| 1592 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | permitted | decided fresh | — |  |
| 1593 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted | bound by precedent | REC-S0012 |  |
| 1594 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | permitted | disposed by citation | — |  |
| 1595 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted with conditions | bound by precedent | REC-FL-G-01454 | ● |
| 1596 | Make the inference-engine build hermetic and reproducible | FL-SC-004 | permitted | decided fresh | — |  |
| 1597 | Run release builds on ephemeral runners with pinned images | FL-SC-004 | permitted | decided fresh | — |  |
| 1598 | Require a named owner to approve production prompt label moves | FL-MB-005 | permitted with conditions | decided fresh | — | ● |
| 1599 | Skip signature verification on load to cut startup time | FL-MB-001 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 1600 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted | decided fresh | — | ● |
| 1601 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | bound by precedent | REC-FL-B-00771 |  |
| 1602 | Separate the audit register from the precedent store at schema level | FL-GV-007 | permitted | decided fresh | — |  |
| 1603 | Measure membership-inference advantage on the release candidate | FL-LS-011 | denied | bound by precedent | REC-S0033 |  |
| 1604 | Set the planner's recursion limit to zero, meaning unlimited | FL-FG-003 | denied | decided fresh | — |  |
| 1605 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | bound by precedent | REC-FL-B-00699 |  |
| 1606 | Relax the coverage floor in the policy bundle to unblock a release train | FL-PV-001 | denied | decided fresh | — |  |
| 1607 | Verify provenance against the expected builder identity before deploy | FL-SC-004 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1608 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-002 | denied | decided fresh | — |  |
| 1609 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-007 | permitted | bound by precedent | REC-FL-N-01510 |  |
| 1610 | Verify de-identification by sampling rather than by assertion | FL-PI-002 | permitted | decided fresh | — | ● |
| 1611 | Log every read of the weights store to the perimeter audit trail | FL-SF-006 | permitted | decided fresh after a tie | none_tie |  |
| 1612 | Exercise injection detection on the changed tool-calling path | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1613 | Block internal address ranges in the web-fetch tool | FL-AS-001 | permitted | decided fresh | — |  |
| 1614 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | bound by precedent | REC-FL-C-00975 | ● |
| 1615 | Name a data-governance custodian on each dataset record | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 1616 | Make the inference-engine build hermetic and reproducible | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 1617 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-009 | permitted | decided fresh | — |  |
| 1618 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | permitted | decided fresh | — |  |
| 1619 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1620 | Remove the contest link from the customer decision notice | FL-GV-009 | denied | decided fresh | — |  |
| 1621 | Hold the audit register in a store the retrieval path cannot read | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1622 | Respect the robots.txt AI directive in the web crawler | FL-TD-004 | permitted | decided fresh | — |  |
| 1623 | Write a docket entry for every arrival that is not charged | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1624 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted | decided fresh | — |  |
| 1625 | Screen new fine-tuning shards for backdoor triggers | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1626 | Require a human reviewer on agent changes to request routing | FL-AG-007 | permitted | decided fresh | — |  |
| 1627 | Restrict agent outbound calls to the allowlisted host set | FL-AG-007 | permitted | decided fresh | — |  |
| 1628 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1629 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-004 | permitted | decided fresh | — |  |
| 1630 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-005 | permitted with conditions | bound by precedent | REC-FL-G-01598 | ● |
| 1631 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted | decided fresh | — |  |
| 1632 | Regenerate the golden prompts from the current model's own answers | FL-EV-009 | denied | decided fresh | — |  |
| 1633 | Make the government-request log append-only across the bulk-export path | FL-PV-002 | permitted | bound by precedent | REC-FL-A-00676 | ● |
| 1634 | Restrict agent outbound calls to the allowlisted host set | FL-AG-006 | permitted | decided fresh | — |  |
| 1635 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | bound by precedent | REC-FL-A-00075 |  |
| 1636 | Make the inference-engine build hermetic and reproducible | FL-SC-004 | permitted | decided fresh | — |  |
| 1637 | Run release builds on ephemeral runners with pinned images | FL-SC-004 | permitted | decided fresh | — |  |
| 1638 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 1639 | Consolidate three redundant age-assurance checks into one server-side gate | FL-CS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1640 | Record the frontier framework version in force on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 1641 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted | decided fresh | — |  |
| 1642 | Record a lawful basis for each conversation-data source | FL-PI-007 | permitted | decided fresh | — |  |
| 1643 | Separate the production prompt label from its version string | FL-MB-007 | permitted | bound by precedent | REC-FL-L-00098 |  |
| 1644 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-001 FL-LS-003 ⛔ | denied | refused at the floor | — |  |
| 1645 | Record the tolerance band used for each accuracy comparison | FL-EV-005 | permitted | bound by precedent | REC-FL-C-01392 |  |
| 1646 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-002 | denied | decided fresh | — |  |
| 1647 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | bound by precedent | REC-FL-A-00567 |  |
| 1648 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1649 | Have the crawler submit the consent form to reach the archive body | FL-TD-002 | denied | bound by precedent | REC-FL-B-00538 |  |
| 1650 | Move the production prompt label straight from the deploy script | FL-MB-003 ⛔ | denied | refused at the floor | — |  |
| 1651 | Label agent-authored diffs so reviewers can isolate them | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00921 | ● |
| 1652 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | decided fresh | — |  |
| 1653 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | bound by precedent | REC-FL-B-00771 | ● |
| 1654 | Justify the two remaining special-category fields on the dataset record | FL-PI-003 | permitted | decided fresh | — |  |
| 1655 | Exclude special-category fields from the support-transcript schema | FL-PI-007 | permitted | bound by precedent | REC-FL-N-01510 |  |
| 1656 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-003 | permitted | decided fresh | — |  |
| 1657 | Replace the model card's static training-summary section with a generated one | FL-TR-003 | permitted | decided fresh | — |  |
| 1658 | Run semantic analysis over the agent diff in continuous integration | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01441 |  |
| 1659 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | permitted | decided fresh | — |  |
| 1660 | Store the provenance chain for derived synthetic corpora | FL-TD-003 | permitted | decided fresh | — | ● |
| 1661 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-005 | permitted with conditions | bound by precedent | REC-FL-S-01512 |  |
| 1662 | Enforce server-side authorization on the new batch endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1663 | Remove the non-human disclosure line from the companion persona's opening message | FL-UH-005 | denied | bound by precedent | REC-FL-B-00780 |  |
| 1664 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | decided fresh | — |  |
| 1665 | Label agent-authored diffs so reviewers can isolate them | FL-AG-006 | permitted | decided fresh | — |  |
| 1666 | Require a named owner to approve production prompt label moves | FL-MB-006 | permitted | decided fresh | — |  |
| 1667 | Keep annotator identifiers in the exported preference dataset for the vendor handoff | FL-PV-003 FL-BS-003 ⛔ | denied | refused at the floor | — |  |
| 1668 | Log every read of the weights store to the perimeter audit trail | FL-SF-009 | permitted | bound by precedent | REC-FL-C-01012 |  |
| 1669 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-004 | permitted | decided fresh | — |  |
| 1670 | Make the government-request log append-only across the bulk-export path | FL-PV-002 | permitted | bound by precedent | REC-FL-A-00676 |  |
| 1671 | Test egress-monitoring coverage in the quarterly weight-security drill | FL-WX-002 | permitted | decided fresh | — |  |
| 1672 | Run denied-party screening at account enablement for every new enterprise tenant | FL-WX-002 | permitted | decided fresh | — |  |
| 1673 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01441 | ● |
| 1674 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | decided fresh | — |  |
| 1675 | Require a human reviewer on agent changes to request routing | FL-AG-006 | denied | bound by precedent | REC-S0022 |  |
| 1676 | Document the subject-request path for the preference store | FL-PI-007 | permitted | decided fresh | — |  |
| 1677 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-008 | denied | bound by precedent | REC-S0005 |  |
| 1678 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted | decided fresh | — |  |
| 1679 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-B-01038 | ● |
| 1680 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-005 | permitted | decided fresh | — |  |
| 1681 | Run the persona and tone evaluation on the release build | FL-BS-005 | permitted | decided fresh | — |  |
| 1682 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | bound by precedent | REC-FL-A-00075 |  |
| 1683 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — |  |
| 1684 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | bound by precedent | REC-FL-A-00128 |  |
| 1685 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 1686 | Raise the verbatim-span limit so the code assistant stops truncating | FL-LS-003 | denied | decided fresh | — |  |
| 1687 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted with conditions | bound by precedent | REC-FL-C-00998 |  |
| 1688 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-006 | permitted | decided fresh | — |  |
| 1689 | Resolve internal packages from the private registry first | FL-SC-006 | permitted | decided fresh | — |  |
| 1690 | Give the batch agent the shared service account to dodge quota holds | FL-FG-004 | denied | decided fresh | — |  |
| 1691 | Stop reading the loop limit from an environment variable | FL-FG-005 | permitted | bound by precedent | REC-S0053 |  |
| 1692 | Move release signing keys onto the hardware security module | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 1693 | Parameterise the new experiment-metrics filter queries | FL-AS-005 | permitted | docketed — not charged | — |  |
| 1694 | Fail the build on scan findings above the severity threshold | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01547 | ● |
| 1695 | Propose allowing sampled rather than exhaustive licence detection | FL-EV-007 | denied | decided fresh | — |  |
| 1696 | Pin the golden-prompt baseline to a commit digest | FL-EV-007 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1697 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 1698 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-005 | permitted | bound by precedent | REC-FL-A-00567 | ● |
| 1699 | Record the agent identity on every quota decision | FL-FG-006 | permitted | decided fresh | — |  |
| 1700 | Raise mitigations to match the assessed capability level | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 1701 | Verify provenance against the expected builder identity before deploy | FL-SC-004 | permitted with conditions | decided fresh | — | ● |
| 1702 | Report refusal and over-refusal rates side by side | FL-BS-003 | denied | bound by precedent | REC-S0056 | ● |
| 1703 | Test egress-monitoring coverage in the quarterly weight-security drill | FL-WX-002 | permitted | decided fresh | — |  |
| 1704 | Paste the copyleft sampling routine into the hosted inference engine | FL-IP-001 ⛔ | denied | refused at the floor | — |  |
| 1705 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — | ● |
| 1706 | Screen new fine-tuning shards for backdoor triggers | FL-LS-010 | denied | bound by precedent | REC-S0032 | ● |
| 1707 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-003 ⛔ | denied | refused at the floor | — |  |
| 1708 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01496 |  |
| 1709 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-005 | permitted | decided fresh | — |  |
| 1710 | Enforce the minor break reminder server-side in companion mode | FL-UH-005 | permitted | decided fresh | — |  |
| 1711 | Strip internal identifiers from gateway error responses | — | permitted | docketed — nothing engaged | — |  |
| 1712 | Resolve internal packages from the private registry first | FL-SC-006 | permitted | bound by precedent | REC-S0064 | ● |
| 1713 | Run release builds on ephemeral runners with pinned images | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 1714 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted with conditions | bound by precedent | REC-FL-C-00998 | ● |
| 1715 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-005 | permitted | decided fresh | — |  |
| 1716 | Declare sample size and percentile alongside the parity result | FL-EV-005 | permitted | decided fresh | — |  |
| 1717 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01046 |  |
| 1718 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted | decided fresh | — |  |
| 1719 | Add the new sampling library to the licence inventory | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 1720 | Run the personal-data scan on every new training shard | FL-PI-005 | permitted | bound by precedent | REC-S0017 | ● |
| 1721 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 1722 | Keep the whistleblower channel anonymous and reachable after the ticketing migration | FL-TR-002 | permitted with conditions | bound by precedent | REC-FL-C-01328 |  |
| 1723 | Give the tool-call graph an explicit terminator | FL-FG-006 | permitted | decided fresh | — |  |
| 1724 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1725 | Fuzz the changed completions parameters before release | — | permitted | docketed — nothing engaged | — |  |
| 1726 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | permitted with conditions | bound by precedent | REC-FL-U-01685 |  |
| 1727 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 1728 | Route parameter changes through the amendment workflow instead | FL-GV-006 | denied | bound by precedent | REC-S0068 |  |
| 1729 | Scan responses for canary tokens before they leave the gateway | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 1730 | Report refusal and over-refusal rates side by side | FL-BS-004 | denied | bound by precedent | REC-S0057 | ● |
| 1731 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 1732 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-005 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1733 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-001 | permitted | decided fresh | — |  |
| 1734 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-001 | permitted | decided fresh | — |  |
| 1735 | Require a human reviewer on agent changes to request routing | FL-AG-006 | permitted | decided fresh | — |  |
| 1736 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-005 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1737 | Screen new fine-tuning shards for backdoor triggers | FL-LS-008 | permitted | decided fresh | — |  |
| 1738 | Put a circuit breaker on the recursive summarisation path | FL-FG-006 | permitted | bound by precedent | REC-FL-C-01572 |  |
| 1739 | Strip annotator identity from the exported preference dataset | FL-PV-001 | permitted | decided fresh | — |  |
| 1740 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-001 | permitted | decided fresh | — |  |
| 1741 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-002 | permitted | bound by precedent | REC-S0090 |  |
| 1742 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — |  |
| 1743 | Document the engine version pinned for each serving tier | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 1744 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | bound by precedent | REC-FL-U-01685 |  |
| 1745 | Require two-person authorisation for unreleased-weight access | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 1746 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — | ● |
| 1747 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00921 |  |
| 1748 | Enable batch invariance before claiming bitwise replay | — | permitted | docketed — nothing engaged | — |  |
| 1749 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-004 | permitted | bound by precedent | REC-FL-A-00805 |  |
| 1750 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-002 | permitted | decided fresh | — |  |
| 1751 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-C-01409 |  |
| 1752 | Give the assistant a first-person human backstory in the release build | FL-BS-003 | denied | decided fresh | — |  |
| 1753 | Add a quarterly compliance drill that exercises the incident-reporting path end to end | FL-TR-002 | permitted with conditions | bound by precedent | REC-S0083 |  |
| 1754 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 1755 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted | bound by precedent | REC-FL-N-01054 |  |
| 1756 | Record the frontier framework version in force on the release record | FL-SF-009 | permitted | decided fresh | — |  |
| 1757 | Log every read of the weights store to the perimeter audit trail | FL-SF-009 | permitted | decided fresh | — |  |
| 1758 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 1759 | Document the subject-request path for the preference store | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01318 | ● |
| 1760 | Fail closed when a dataset licence string does not parse | FL-TD-004 | permitted | decided fresh | — |  |
| 1761 | Block promotion until the dangerous-capability reports complete | FL-SF-006 | permitted | bound by precedent | REC-FL-A-00642 | ● |
| 1762 | Propose an amendment codifying coverage rules for generated eval configs | FL-SC-004 | denied | decided fresh | — |  |
| 1763 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-003 | permitted | bound by precedent | REC-FL-A-00061 |  |
| 1764 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-003 | permitted | decided fresh | — |  |
| 1765 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01318 |  |
| 1766 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 1767 | Run the decontamination check over the new code corpus | FL-EV-005 | permitted | bound by precedent | REC-FL-C-01392 |  |
| 1768 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-007 | permitted with conditions | decided fresh | — | ● |
| 1769 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-006 | denied | bound by precedent | REC-FL-B-00459 |  |
| 1770 | Add an autonomous-replication probe to the agentic-checkpoint sandbox | FL-CB-002 | permitted | decided fresh | — |  |
| 1771 | Keep the human override reachable in the high-risk review flow | FL-GV-008 | denied | bound by precedent | REC-FL-C-01027 |  |
| 1772 | Run licence detection over every agent-authored file | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 1773 | Publish the prompt-log retention clock in the customer portal | FL-PI-007 | permitted | bound by precedent | REC-FL-N-01510 |  |
| 1774 | Replace the sanctioned-destination blocklist in the gateway with allow-by-default | FL-WX-003 | denied | decided fresh | — |  |
| 1775 | Attribute the standing declaration in the exported rulebook | FL-GV-009 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1776 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — |  |
| 1777 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | denied | bound by precedent | REC-S0010 |  |
| 1778 | Require a named owner to approve production prompt label moves | FL-MB-004 | permitted | decided fresh | — | ● |
| 1779 | Record a lawful basis for each conversation-data source | FL-PI-004 | denied | bound by precedent | REC-S0016 |  |
| 1780 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh | — |  |
| 1781 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | permitted | decided fresh | — |  |
| 1782 | Record a disposition for every referral the board acknowledges | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 1783 | Train on the partner's user conversations before the basis is recorded | FL-PI-007 | denied | bound by precedent | REC-FL-B-00260 |  |
| 1784 | Update the third-party licence inventory with this dependency change | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 1785 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-002 | permitted with conditions | bound by precedent | REC-S0085 |  |
| 1786 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 1787 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-C-01679 |  |
| 1788 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-007 | permitted | decided fresh | — |  |
| 1789 | Record the frontier framework version in force on the release record | FL-SF-009 | permitted | bound by precedent | REC-FL-A-00855 | ● |
| 1790 | Fail the merge when the scanner reports an unresolved licence | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 1791 | Pin the golden-prompt baseline to a commit digest | FL-EV-004 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 1792 | Record the tolerance band used for each accuracy comparison | FL-EV-007 | permitted | decided fresh | — |  |
| 1793 | Publish the frontier transparency report ahead of the deployment date | FL-TR-002 | permitted with conditions | bound by precedent | REC-FL-C-01328 |  |
| 1794 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted | decided fresh | — |  |
| 1795 | Publish the prompt-log retention clock in the customer portal | FL-PI-006 | denied | bound by precedent | REC-S0018 |  |
| 1796 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1797 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-C-01480 |  |
| 1798 | Give every system prompt an immutable version identifier | FL-MB-006 | permitted | disposed by citation | — |  |
| 1799 | Scope the retrieval index to the tenant boundary at query time | FL-PV-002 | permitted | bound by precedent | REC-S0090 |  |
| 1800 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-002 | permitted with conditions | decided fresh | — | ● |
| 1801 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | denied | bound by precedent | REC-S0007 |  |
| 1802 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 1803 | Enable batch invariance before claiming bitwise replay | FL-IN-003 | permitted with conditions | bound by precedent | REC-FL-U-01743 |  |
| 1804 | Attach an external evaluator attestation to the cyber-uplift result record | FL-CB-003 | permitted | decided fresh | — |  |
| 1805 | Move the autonomy eval from a nightly job into the promotion gate itself | FL-CB-003 | permitted | decided fresh | — |  |
| 1806 | Update the third-party licence inventory with this dependency change | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 1807 | Verify de-identification by sampling rather than by assertion | FL-PI-006 | permitted | bound by precedent | REC-FL-N-00380 |  |
| 1808 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 1809 | Record a disposition for every referral the board acknowledges | FL-GV-006 | permitted | decided fresh | — |  |
| 1810 | Expose a contest path to affected customers in the portal | FL-GV-006 | permitted | decided fresh | — |  |
| 1811 | Make the government-request log append-only across the bulk-export path | FL-PV-004 | permitted | bound by precedent | REC-FL-A-00805 | ● |
| 1812 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 1813 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-002 | permitted | decided fresh | — |  |
| 1814 | Gate promotion on the full safety suite, not the fast subset | FL-EV-010 | permitted | bound by precedent | REC-FL-C-01217 |  |
| 1815 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 1816 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-002 | permitted | bound by precedent | REC-FL-C-01633 |  |
| 1817 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-001 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 1818 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-003 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 1819 | Hold goodput at the tier threshold under the burst profile | — | permitted | docketed — nothing engaged | — |  |
| 1820 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-005 | denied | bound by precedent | REC-S0002 |  |
| 1821 | Publish the training-content summary from the current release's manifest | FL-TR-003 | permitted | decided fresh | — |  |
| 1822 | Require the safety-case signature from outside the authoring team | FL-SF-009 | permitted | bound by precedent | REC-FL-C-01789 |  |
| 1823 | Separate the audit register from the precedent store at schema level | FL-GV-009 | permitted | decided fresh | — |  |
| 1824 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted with conditions | bound by precedent | REC-FL-C-01173 |  |
| 1825 | Require human confirmation before the agent executes a write tool | FL-LS-005 | permitted | decided fresh | — |  |
| 1826 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-G-01800 | ● |
| 1827 | Check every new import against the upstream registry before build | FL-AG-004 | permitted | decided fresh | — |  |
| 1828 | Require a human reviewer on agent changes to request routing | FL-AG-004 | permitted | decided fresh | — |  |
| 1829 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-004 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 1830 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1831 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | denied | bound by precedent | REC-S0013 |  |
| 1832 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-005 | permitted | decided fresh | — |  |
| 1833 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | decided fresh | — |  |
| 1834 | Measure judge and human agreement for the new grader configuration | FL-EV-010 | permitted | bound by precedent | REC-FL-C-01217 |  |
| 1835 | Validate tenant scope on every portal export request | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1836 | Enforce the instruction and data boundary on the retrieval path | FL-LS-005 | permitted | decided fresh | — |  |
| 1837 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | bound by precedent | REC-S0006 |  |
| 1838 | Add a new exemption class to the agent sign-off rule | FL-TR-002 | denied | decided fresh | — |  |
| 1839 | Recompute the root digest from resource digests before promotion | FL-MB-006 | permitted | bound by precedent | REC-S0003 |  |
| 1840 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-001 FL-FG-006 ⛔ | denied | refused at the floor | — |  |
| 1841 | Separate the production prompt label from its version string | FL-MB-006 | permitted | bound by precedent | REC-S0003 | ● |
| 1842 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-007 | permitted | decided fresh | — | ● |
| 1843 | State the percentile on every latency claim in the dashboard | FL-IN-003 | permitted with conditions | bound by precedent | REC-FL-U-01743 | ● |
| 1844 | Run the personal-data scan on every new training shard | FL-PI-005 | permitted | decided fresh | — |  |
| 1845 | Measure demographic disparity across the ambiguous-context suite | FL-BS-004 | denied | bound by precedent | REC-FL-C-01730 |  |
| 1846 | Let retrieval read audit findings so precedent search returns more | FL-GV-003 FL-GV-011 ⛔ | denied | refused at the floor | — |  |
| 1847 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-C-01415 |  |
| 1848 | Separate the production prompt label from its version string | FL-MB-007 | permitted | decided fresh | — | ● |
| 1849 | Move release signing keys onto the hardware security module | FL-SF-006 | permitted | decided fresh | — |  |
| 1850 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-006 | permitted | decided fresh | — |  |
| 1851 | Reject unexpected content types on the tool-callback endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 1852 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-005 | permitted | bound by precedent | REC-FL-A-01705 | ● |
| 1853 | Exclude the election-integrity classifier from this release's gate | FL-UH-002 | denied | decided fresh | — |  |
| 1854 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01373 | ● |
| 1855 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-004 ⛔ | denied | refused at the floor | — |  |
| 1856 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-010 | permitted | bound by precedent | REC-FL-C-01217 |  |
| 1857 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 1858 | Gate promotion on the full safety suite, not the fast subset | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01062 |  |
| 1859 | Record a lawful basis for each conversation-data source | FL-PI-005 | permitted | decided fresh | — |  |
| 1860 | Verify provenance against the expected builder identity before deploy | FL-SC-002 | permitted | bound by precedent | REC-FL-L-01276 |  |
| 1861 | Bake the build timestamp and hostname into the engine binary | FL-SC-002 | denied | decided fresh | — |  |
| 1862 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-004 | permitted | bound by precedent | REC-S0091 |  |
| 1863 | Backfill lineage records for the older quantised checkpoints | FL-MB-008 | permitted | decided fresh | — |  |
| 1864 | Publish the signing certificate chain alongside each release digest | FL-MB-008 | permitted | decided fresh | — |  |
| 1865 | Project token spend before dispatching a long-horizon agent run | FL-FG-004 | permitted | decided fresh | — |  |
| 1866 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | bound by precedent | REC-FL-L-00444 |  |
| 1867 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-004 | permitted | decided fresh | — |  |
| 1868 | Screen new fine-tuning shards for backdoor triggers | FL-LS-009 | denied | bound by precedent | REC-S0031 |  |
| 1869 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 1870 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-001 FL-SC-003 ⛔ | denied | refused at the floor | — |  |
| 1871 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted | decided fresh | — |  |
| 1872 | Name a data-governance custodian on each dataset record | FL-TD-004 | permitted | decided fresh | — |  |
| 1873 | Release the run record with the threshold determination left blank | FL-SF-003 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 1874 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | permitted | bound by precedent | REC-FL-C-01572 |  |
| 1875 | Declare the carrier channel for each untrusted input source | FL-LS-010 | permitted | decided fresh | — |  |
| 1876 | Shorten the report-preservation window in the retention job to ninety days | FL-CS-003 | denied | decided fresh | — | ● |
| 1877 | Add an eval-awareness probe to the pre-release harness run | FL-CB-002 | permitted | bound by precedent | REC-S0078 |  |
| 1878 | Validate tenant scope on every portal export request | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1879 | Fail the build on scan findings above the severity threshold | FL-SC-005 | permitted with conditions | bound by precedent | REC-FL-C-01565 |  |
| 1880 | Declare both base models in the merged cirrus-small manifest | FL-MB-005 | permitted | decided fresh | — |  |
| 1881 | Check the code-signing extended key usage on the release chain | FL-MB-005 | permitted | decided fresh | — |  |
| 1882 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 1883 | Make the breaker unreachable from the agent's own configuration | FL-FG-003 | permitted | decided fresh | — |  |
| 1884 | Declare sample size and percentile alongside the parity result | FL-EV-005 | permitted | bound by precedent | REC-S0036 |  |
| 1885 | Let the agent edit the release workflow to unblock its own branch | FL-AG-001 FL-TD-005 ⛔ | denied | refused at the floor | — |  |
| 1886 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-007 | permitted | bound by precedent | REC-FL-A-01842 |  |
| 1887 | Run the persona and tone evaluation on the release build | FL-BS-004 | permitted | decided fresh | — |  |
| 1888 | Write a docket entry for every arrival that is not charged | FL-GV-010 | permitted with conditions | bound by precedent | REC-FL-C-01357 |  |
| 1889 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 1890 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted | bound by precedent | REC-S0069 |  |
| 1891 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 1892 | Record the prompt and context hash on each agent commit | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01673 |  |
| 1893 | Require a named owner to approve production prompt label moves | FL-MB-008 | permitted | decided fresh | — |  |
| 1894 | Backfill lineage records for the older quantised checkpoints | FL-MB-008 | permitted | decided fresh | — |  |
| 1895 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 1896 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1897 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 1898 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 1899 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01720 |  |
| 1900 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-007 | permitted | decided fresh | — |  |
| 1901 | Run release builds on ephemeral runners with pinned images | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 1902 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh | — |  |
| 1903 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | bound by precedent | REC-FL-C-01653 |  |
| 1904 | Enforce the instruction and data boundary on the retrieval path | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 1905 | Split personal-data handling out of the shared ingestion library | FL-PI-002 | permitted | bound by precedent | REC-FL-A-00781 |  |
| 1906 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-003 | permitted | docketed — not charged | — |  |
| 1907 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | bound by precedent | REC-S0017 |  |
| 1908 | Reject unexpected content types on the tool-callback endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1909 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-B-00628 |  |
| 1910 | Return a generic error identifier instead of the stack trace | FL-AS-002 | permitted | docketed — not charged | — |  |
| 1911 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-005 | permitted with conditions | bound by precedent | REC-FL-C-01565 |  |
| 1912 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1913 | Publish a signed bill of materials covering transitive dependencies | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01064 |  |
| 1914 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 1915 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-002 | permitted | decided fresh | — |  |
| 1916 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-002 | permitted | decided fresh | — |  |
| 1917 | Export the distilled checkpoint as a pickle to keep the old loader | FL-MB-004 | denied | decided fresh | — |  |
| 1918 | Escape tool output before it reaches the shell adapter | FL-LS-005 | permitted with conditions | decided fresh | — | ● |
| 1919 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-004 | permitted | bound by precedent | REC-FL-C-01811 |  |
| 1920 | Remove the contest link from the customer decision notice | FL-GV-006 | denied | decided fresh | — |  |
| 1921 | Ship the image whose layer digests no longer match the recorded inventory | FL-SC-006 | denied | decided fresh | — | ● |
| 1922 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-006 | permitted | decided fresh | — |  |
| 1923 | Widen the parity report to distinguish immaterial differences | FL-EV-006 | permitted | decided fresh after a tie | none_tie |  |
| 1924 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-006 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1925 | Run release builds on ephemeral runners with pinned images | FL-SC-006 | permitted | decided fresh | — |  |
| 1926 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted with conditions | bound by precedent | REC-FL-U-01898 |  |
| 1927 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1928 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 1929 | Run licence detection over every agent-authored file | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 1930 | Store the provenance chain for derived synthetic corpora | FL-TD-007 | permitted | bound by precedent | REC-S0012 |  |
| 1931 | Run the persona and tone evaluation on the release build | FL-BS-002 | permitted | decided fresh | — |  |
| 1932 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted | decided fresh after a tie | none_tie |  |
| 1933 | Record the frontier framework version in force on the release record | FL-SF-008 | permitted with conditions | bound by precedent | REC-FL-S-01895 |  |
| 1934 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-008 | permitted | decided fresh | — |  |
| 1935 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-008 | permitted | decided fresh | — |  |
| 1936 | Require two-person authorisation for unreleased-weight access | FL-SF-005 | permitted | decided fresh | — |  |
| 1937 | Raise mitigations to match the assessed capability level | FL-SF-005 | permitted | decided fresh | — |  |
| 1938 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | permitted | bound by precedent | REC-FL-C-01476 |  |
| 1939 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-004 | permitted | decided fresh | — |  |
| 1940 | Record the capability-threshold determination on the release record | FL-SF-006 | permitted | bound by precedent | REC-FL-A-00642 |  |
| 1941 | Pin every dependency to an immutable digest in the lockfile | FL-SC-005 | permitted | decided fresh | — |  |
| 1942 | Respect the robots.txt AI directive in the web crawler | FL-TD-005 | permitted | decided fresh | — |  |
| 1943 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-006 | permitted | bound by precedent | REC-FL-A-00462 |  |
| 1944 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 1945 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1946 | Document which attack class the new defence was evaluated against | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 1947 | Disable the government-request log for the bulk export tool | FL-PV-004 | denied | decided fresh | — | ● |
| 1948 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-005 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1949 | Raise mitigations to match the assessed capability level | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 1950 | Sign agent commits with a workload identity rather than a person's key | FL-AG-007 | permitted | bound by precedent | REC-S0023 |  |
| 1951 | Add the visiting researcher's account to the weights cluster without a deemed-export review | FL-WX-002 | denied | decided fresh | — |  |
| 1952 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | bound by precedent | REC-S0006 |  |
| 1953 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-003 ⛔ | denied | refused at the floor | — |  |
| 1954 | Measure membership-inference advantage on the release candidate | FL-LS-005 | permitted | bound by precedent | REC-S0027 |  |
| 1955 | Give the tool-call graph an explicit terminator | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 1956 | Add a weekly sampling job over production refusals | FL-BS-002 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1957 | Cut the incident-severity form down to the fields the reporting clock actually reads | FL-TR-002 | permitted | decided fresh | — |  |
| 1958 | Replace the model card's static training-summary section with a generated one | FL-TR-002 | permitted | decided fresh | — |  |
| 1959 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 1960 | Compare the provenance subject digest to the distributed artifact | FL-SC-008 | permitted | bound by precedent | REC-FL-L-01172 | ● |
| 1961 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | disposed by citation | — |  |
| 1962 | Declare both base models in the merged cirrus-small manifest | FL-MB-009 | permitted | bound by precedent | REC-S0006 |  |
| 1963 | Report first-token and per-token latency against the tier budgets | FL-IN-008 | permitted | docketed — not charged | — |  |
| 1964 | Require a named owner to approve production prompt label moves | FL-MB-008 | permitted | disposed by citation | — |  |
| 1965 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01698 | ● |
| 1966 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 1967 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 1968 | Declare sample size and percentile alongside the parity result | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 1969 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | bound by precedent | REC-FL-B-00699 | ● |
| 1970 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 1971 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted | decided fresh | — |  |
| 1972 | Require human confirmation before the agent executes a write tool | FL-LS-006 | permitted | bound by precedent | REC-S0028 |  |
| 1973 | Screen new fine-tuning shards for backdoor triggers | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 1974 | State turns rather than seconds as the loop-limit unit | FL-FG-002 | permitted | bound by precedent | REC-S0050 |  |
| 1975 | Pin workflow actions to commit digests across the release repository | FL-SC-007 | permitted | decided fresh | — | ● |
| 1976 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-006 | permitted | bound by precedent | REC-FL-N-00889 |  |
| 1977 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 1978 | Skip signature verification on load to cut startup time | FL-MB-005 | denied | bound by precedent | REC-FL-B-01323 |  |
| 1979 | Move the loop-limit requirement out of the rulebook into service defaults | FL-IN-003 | denied | decided fresh | — |  |
| 1980 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00244 |  |
| 1981 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-003 | permitted | decided fresh | — |  |
| 1982 | Move the minor-mode restriction check from the client SDK into the gateway | FL-CS-003 | permitted | decided fresh | — |  |
| 1983 | Block internal address ranges in the web-fetch tool | FL-AS-006 | permitted | docketed — not charged | — |  |
| 1984 | Replace the model card's static training-summary section with a generated one | FL-TR-002 | permitted with conditions | bound by precedent | REC-FL-C-01328 |  |
| 1985 | Escape tool output before it reaches the shell adapter | FL-LS-010 | permitted | decided fresh | — |  |
| 1986 | Fail the build on scan findings above the severity threshold | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01694 |  |
| 1987 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted | decided fresh | — |  |
| 1988 | Exercise injection detection on the changed tool-calling path | FL-LS-003 | denied | bound by precedent | REC-S0025 |  |
| 1989 | Verify de-identification by sampling rather than by assertion | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 1990 | Keep reporter bulletins off the adjudication input path | FL-GV-011 | permitted with conditions | decided fresh | — | ● |
| 1991 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1992 | Rewrite the last raw query in the usage-reporting job | FL-AS-004 | permitted | docketed — not charged | — |  |
| 1993 | Make decision records append-only in the store schema | FL-GV-009 | permitted with conditions | bound by precedent | REC-S0071 | ● |
| 1994 | Project token spend before dispatching a long-horizon agent run | FL-FG-006 | permitted | decided fresh | — |  |
| 1995 | Give the batch agent the shared service account to dodge quota holds | FL-FG-006 | denied | decided fresh | — |  |
| 1996 | Record the elicitation effort alongside every uplift-eval result | FL-CB-004 | permitted | bound by precedent | REC-S0080 |  |
| 1997 | Enable batch invariance before claiming bitwise replay | FL-IN-008 | permitted | docketed — not charged | — |  |
| 1998 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 1999 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted | decided fresh | — |  |
| 2000 | Require the safety-case signature from outside the authoring team | FL-SF-005 | permitted | bound by precedent | REC-FL-C-01852 | ● |
| 2001 | Verify provenance against the expected builder identity before deploy | FL-SC-007 | permitted | disposed by citation | — |  |
| 2002 | Move release signing keys onto the hardware security module | FL-SF-006 | permitted | bound by precedent | REC-FL-A-00642 |  |
| 2003 | Restrict agent outbound calls to the allowlisted host set | FL-AG-005 | permitted | decided fresh | — |  |
| 2004 | Reject imports for packages first published within thirty days | FL-AG-005 | permitted | decided fresh | — |  |
| 2005 | Hold verbatim third-party reproduction below the span threshold | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 2006 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-C-01480 |  |
| 2007 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 2008 | Move release signing keys onto the hardware security module | FL-SF-009 | permitted | bound by precedent | REC-FL-A-00855 | ● |
| 2009 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-003 | permitted with conditions | decided fresh | — | ● |
| 2010 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | denied | bound by precedent | REC-S0007 | ● |
| 2011 | Name a data-governance custodian on each dataset record | FL-TD-007 | permitted | decided fresh | — |  |
| 2012 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-011 | permitted | decided fresh | — |  |
| 2013 | Route parameter changes through the amendment workflow instead | FL-GV-011 | permitted | decided fresh | — |  |
| 2014 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-006 | permitted | bound by precedent | REC-FL-C-01761 |  |
| 2015 | Stop reading the loop limit from an environment variable | FL-FG-003 | permitted | decided fresh | — |  |
| 2016 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-006 | permitted | bound by precedent | REC-FL-C-01841 |  |
| 2017 | Bind the research agent's quota to its cost centre | FL-FG-006 | permitted | decided fresh | — |  |
| 2018 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-003 | denied | bound by precedent | REC-FL-B-00304 |  |
| 2019 | Declare the carrier channel for each untrusted input source | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 2020 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-C-01480 |  |
| 2021 | Record the builder identity in attestations for nightly checkpoints | FL-SC-004 | permitted | disposed by citation | — |  |
| 2022 | Measure demographic disparity across the ambiguous-context suite | FL-BS-004 | denied | bound by precedent | REC-S0057 |  |
| 2023 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted | decided fresh | — |  |
| 2024 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 2025 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 2026 | Record an export-classification determination before every weight transfer | FL-WX-002 | permitted | decided fresh | — |  |
| 2027 | Bind weight-store access grants to the current personnel-vetting record | FL-WX-002 | permitted | decided fresh | — |  |
| 2028 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 2029 | Return a generic error identifier instead of the stack trace | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2030 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-003 | denied | bound by precedent | REC-FL-B-01491 | ● |
| 2031 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-002 | permitted | decided fresh | — |  |
| 2032 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-006 | denied | bound by precedent | REC-FL-B-00459 |  |
| 2033 | Route flagged responses to the block path rather than a warning | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 2034 | Measure demographic disparity across the ambiguous-context suite | FL-BS-002 | permitted with conditions | bound by precedent | REC-S0055 | ● |
| 2035 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 2036 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00140 |  |
| 2037 | Cover the new administrative routes in the authorization test suite | FL-AS-001 | permitted | decided fresh | — |  |
| 2038 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-006 | permitted | bound by precedent | REC-S0003 |  |
| 2039 | List only the instruct parent on the merged checkpoint card | FL-MB-002 FL-LS-007 ⛔ | denied | refused at the floor | — |  |
| 2040 | Track system-prompt versions in a free-text description field | FL-MB-002 FL-EV-010 ⛔ | denied | refused at the floor | — |  |
| 2041 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | denied | bound by precedent | REC-FL-C-02010 | ● |
| 2042 | Put a circuit breaker on the recursive summarisation path | FL-FG-006 | permitted | decided fresh | — |  |
| 2043 | Verify de-identification by sampling rather than by assertion | FL-PI-004 | denied | bound by precedent | REC-S0016 |  |
| 2044 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted | decided fresh | — |  |
| 2045 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | decided fresh | — |  |
| 2046 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted with conditions | bound by precedent | REC-FL-C-01565 |  |
| 2047 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 2048 | Check persona guidance against the shipped system prompt | FL-BS-004 | denied | bound by precedent | REC-FL-C-01730 |  |
| 2049 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-004 | permitted | decided fresh | — |  |
| 2050 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-004 | permitted | decided fresh | — |  |
| 2051 | Load a customer's fine-tune adapter for another tenant's inference request | FL-PV-002 | denied | decided fresh | — |  |
| 2052 | Fail the run outright when no loop limit is declared | FL-FG-004 | denied | bound by precedent | REC-S0052 |  |
| 2053 | Roll out the new grader configuration without an agreement study | FL-EV-002 FL-IN-001 ⛔ | denied | refused at the floor | — |  |
| 2054 | Pin the golden-prompt baseline to a commit digest | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01240 |  |
| 2055 | Embed the canary string in every generated evaluation case | FL-EV-010 | permitted | decided fresh | — |  |
| 2056 | Remove the contest link from the customer decision notice | FL-GV-010 | denied | decided fresh | — |  |
| 2057 | Hold agentic-checkpoint promotion on a completed autonomy-eval result | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-C-01826 | ● |
| 2058 | Enforce server-side authorization on the new batch endpoint | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2059 | Check persona guidance against the shipped system prompt | FL-BS-003 | denied | bound by precedent | REC-S0056 |  |
| 2060 | Compare the provenance subject digest to the distributed artifact | FL-SC-008 | permitted | decided fresh | — | ● |
| 2061 | Log every read of the weights store to the perimeter audit trail | FL-SF-008 | permitted | bound by precedent | REC-FL-A-00096 |  |
| 2062 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 2063 | Check the code-signing extended key usage on the release chain | FL-MB-007 | permitted | bound by precedent | REC-FL-L-00098 |  |
| 2064 | Restrict deserialisation to the declared tool-payload types | FL-AS-001 | permitted | decided fresh | — |  |
| 2065 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-C-01415 |  |
| 2066 | Respect the robots.txt AI directive in the web crawler | FL-TD-006 | permitted | decided fresh | — | ● |
| 2067 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-003 | denied | bound by precedent | REC-FL-C-01702 |  |
| 2068 | Move the loop-limit requirement out of the rulebook into service defaults | FL-IN-002 | denied | decided fresh | — |  |
| 2069 | Make the breaker unreachable from the agent's own configuration | FL-FG-004 | permitted | bound by precedent | REC-FL-A-00375 |  |
| 2070 | Ship the quantised build four points below the tolerance band | FL-EV-001 FL-WX-003 ⛔ | denied | refused at the floor | — |  |
| 2071 | Publish a review checklist for agent changes to the eval harness | FL-AG-005 | permitted with conditions | bound by precedent | REC-S0021 |  |
| 2072 | Gate promotion on the full safety suite, not the fast subset | FL-EV-010 | permitted | decided fresh | — |  |
| 2073 | Keep cases released after the training cutoff in the holdout | FL-EV-010 | permitted | decided fresh | — |  |
| 2074 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-005 | permitted | decided fresh | — |  |
| 2075 | Keep cases released after the training cutoff in the holdout | FL-EV-008 | permitted | bound by precedent | REC-S0039 |  |
| 2076 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-002 FL-GV-005 ⛔ | denied | refused at the floor | — |  |
| 2077 | Document the subject-request path for the preference store | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01553 | ● |
| 2078 | Onboard the new chat source without running the de-identification sample | FL-PI-005 | denied | decided fresh | — |  |
| 2079 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 2080 | Split personal-data handling out of the shared ingestion library | FL-PI-006 | denied | bound by precedent | REC-S0018 | ● |
| 2081 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 2082 | Log the named authority for every override exercised | FL-GV-008 | permitted | decided fresh | — |  |
| 2083 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | bound by precedent | REC-FL-N-01610 | ● |
| 2084 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted | decided fresh after a tie | none_tie |  |
| 2085 | Run the decontamination check over the new code corpus | FL-EV-009 | permitted with conditions | bound by precedent | REC-FL-G-01968 |  |
| 2086 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 2087 | Run release builds on ephemeral runners with pinned images | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 |  |
| 2088 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2089 | Restrict weight egress to the declared perimeter buckets | FL-SF-008 | permitted | bound by precedent | REC-FL-C-01476 |  |
| 2090 | Move retrieved documents into a separate, clearly marked context block | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 2091 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-B-00545 | ● |
| 2092 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 2093 | Strip annotator identity from the exported preference dataset | FL-PV-002 | permitted | bound by precedent | REC-FL-C-01633 |  |
| 2094 | Enforce the instruction and data boundary on the retrieval path | FL-LS-006 | permitted | decided fresh | — |  |
| 2095 | Scan responses for canary tokens before they leave the gateway | FL-LS-006 | permitted | decided fresh | — |  |
| 2096 | Require human confirmation before the agent executes a write tool | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 2097 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-003 | denied | bound by precedent | REC-FL-B-00304 |  |
| 2098 | Return a generic error identifier instead of the stack trace | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2099 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-C-01679 |  |
| 2100 | Add audio-generation coverage to the abuse-material classifier suite | FL-CS-003 | permitted | decided fresh | — |  |
| 2101 | Add audio-generation coverage to the abuse-material classifier suite | FL-CS-003 | permitted | decided fresh | — |  |
| 2102 | Require human confirmation before the agent executes a write tool | FL-LS-005 | permitted | bound by precedent | REC-FL-C-01344 |  |
| 2103 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 2104 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-003 | denied | bound by precedent | REC-FL-C-01702 | ● |
| 2105 | Enforce server-side authorization on the new batch endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 2106 | Run release builds on ephemeral runners with pinned images | FL-SC-008 | permitted | bound by precedent | REC-FL-C-01960 |  |
| 2107 | Report first-token and per-token latency against the tier budgets | FL-IN-006 | permitted | decided fresh | — |  |
| 2108 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01698 |  |
| 2109 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-007 | permitted | decided fresh | — |  |
| 2110 | Fail the run outright when no loop limit is declared | FL-FG-002 | permitted with conditions | bound by precedent | REC-FL-U-02092 | ● |
| 2111 | Run release builds on ephemeral runners with pinned images | FL-SC-003 | permitted | disposed by citation | — |  |
| 2112 | Publish a signed bill of materials covering transitive dependencies | FL-SC-008 | permitted | bound by precedent | REC-FL-C-01960 |  |
| 2113 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-002 | permitted | decided fresh | — |  |
| 2114 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 |  |
| 2115 | Report preemption counts in the load-test summary | FL-IN-005 | permitted | decided fresh | — |  |
| 2116 | Record the builder identity in attestations for nightly checkpoints | FL-SC-007 | permitted | bound by precedent | REC-FL-L-01975 |  |
| 2117 | List only the instruct parent on the merged checkpoint card | FL-MB-008 | denied | decided fresh | — |  |
| 2118 | Run the personal-data scan on every new training shard | FL-PI-002 | permitted | decided fresh | — |  |
| 2119 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | decided fresh | — |  |
| 2120 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 2121 | Run agent-authored code only inside the sandboxed runner | FL-AG-005 | permitted | bound by precedent | REC-FL-C-01651 |  |
| 2122 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-GV-010 | denied | decided fresh | — |  |
| 2123 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-004 | permitted | bound by precedent | REC-FL-A-00375 |  |
| 2124 | Enforce vetting-record expiry automatically in the access-control system | FL-WX-003 | permitted | decided fresh | — |  |
| 2125 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-003 | permitted | decided fresh | — |  |
| 2126 | Reject unexpected content types on the tool-callback endpoint | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2127 | Require two-person authorisation for unreleased-weight access | FL-SF-009 | permitted | bound by precedent | REC-FL-C-01789 |  |
| 2128 | Run the decontamination check over the new code corpus | FL-EV-010 | permitted | decided fresh | — |  |
| 2129 | Check the code-signing extended key usage on the release chain | FL-MB-005 | permitted with conditions | bound by precedent | REC-FL-C-01630 |  |
| 2130 | Stop reading the loop limit from an environment variable | FL-FG-003 | permitted | decided fresh | — |  |
| 2131 | Require human confirmation before the agent executes a write tool | FL-LS-003 | permitted with conditions | bound by precedent | REC-FL-G-02009 |  |
| 2132 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TD-006 | denied | decided fresh | — |  |
| 2133 | Remove the graphic-content exposure limits from the labeling-queue config | FL-PV-004 | denied | decided fresh | — | ● |
| 2134 | Give the batch agent the shared service account to dodge quota holds | FL-FG-002 | denied | decided fresh | — |  |
| 2135 | Remove the non-human disclosure line from the companion persona's opening message | FL-UH-005 | denied | bound by precedent | REC-FL-B-00780 |  |
| 2136 | Submit an amendment retiring the deferred data-governance clauses early | FL-LS-008 | denied | decided fresh | — |  |
| 2137 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-003 | denied | bound by precedent | REC-S0051 |  |
| 2138 | Pin the golden-prompt baseline to a commit digest | FL-EV-008 | permitted | decided fresh after a tie | none_tie |  |
| 2139 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-C-01122 |  |
| 2140 | Redact prompt and completion logs before they reach retention | FL-PI-005 | permitted | decided fresh | — |  |
| 2141 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | decided fresh | — |  |
| 2142 | Publish the prompt-log retention clock in the customer portal | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 2143 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 2144 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 2145 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | decided fresh | — |  |
| 2146 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-003 | denied | bound by precedent | REC-FL-C-02030 | ● |
| 2147 | Remove the crisis-resource handoff from the consumer response path | FL-UH-001 FL-SF-008 ⛔ | denied | refused at the floor | — |  |
| 2148 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01720 | ● |
| 2149 | Declare sample size and percentile alongside the parity result | FL-EV-003 | permitted | decided fresh | — |  |
| 2150 | Export the rulebook without the standing declaration block | FL-GV-005 | denied | decided fresh | — |  |
| 2151 | Attach an external evaluator attestation to the cyber-uplift result record | FL-CB-002 | permitted | bound by precedent | REC-S0078 |  |
| 2152 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-009 | permitted | decided fresh | — |  |
| 2153 | Block promotion until the dangerous-capability reports complete | FL-SF-008 | permitted | bound by precedent | REC-FL-C-01476 |  |
| 2154 | Keep reporter bulletins off the adjudication input path | FL-GV-005 | permitted | decided fresh | — |  |
| 2155 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-002 | denied | decided fresh | — |  |
| 2156 | Declare sample size and percentile alongside the parity result | FL-EV-004 | permitted with conditions | bound by precedent | REC-S0035 | ● |
| 2157 | Exercise injection detection on the changed tool-calling path | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 2158 | Pin every dependency to an immutable digest in the lockfile | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 2159 | Expose a contest path to affected customers in the portal | FL-GV-008 | permitted | decided fresh | — |  |
| 2160 | Fail the build when an agent commit arrives unsigned | FL-AG-004 | permitted with conditions | bound by precedent | REC-S0020 | ● |
| 2161 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-004 | permitted | decided fresh | — |  |
| 2162 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-004 | permitted | decided fresh | — |  |
| 2163 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 2164 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 2165 | Justify the two remaining special-category fields on the dataset record | FL-PI-004 | permitted | bound by precedent | REC-FL-N-01746 |  |
| 2166 | Cover the new administrative routes in the authorization test suite | FL-AS-002 | permitted | docketed — not charged | — |  |
| 2167 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01553 | ● |
| 2168 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — |  |
| 2169 | Export the rulebook without the standing declaration block | FL-GV-011 | denied | decided fresh | — |  |
| 2170 | Record the capability-threshold determination on the release record | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 2171 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 2172 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 2173 | Enforce server-side authorization on the new batch endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2174 | Strip annotator identity from the exported preference dataset | FL-PV-002 | permitted | bound by precedent | REC-FL-C-01633 |  |
| 2175 | Run the persona and tone evaluation on the release build | FL-BS-002 | permitted | decided fresh | — |  |
| 2176 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-006 | permitted with conditions | bound by precedent | REC-FL-C-01031 | ● |
| 2177 | Declare the downstream sink for every model output field | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 2178 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 2179 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-006 | denied | decided fresh | — |  |
| 2180 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-005 | denied | bound by precedent | REC-S0058 |  |
| 2181 | Record the licence class for every corpus the crawler ingests | FL-TD-007 | permitted | decided fresh | — |  |
| 2182 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-002 | denied | bound by precedent | REC-S0007 | ● |
| 2183 | Stop reading the loop limit from an environment variable | FL-FG-005 | permitted | decided fresh | — |  |
| 2184 | Project token spend before dispatching a long-horizon agent run | FL-FG-005 | permitted | decided fresh | — |  |
| 2185 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 2186 | Gate external evaluator access on the signed agreement | FL-SF-006 | permitted | bound by precedent | REC-FL-C-01761 |  |
| 2187 | Split personal-data handling out of the shared ingestion library | FL-PI-006 | permitted | decided fresh after a tie | none_tie |  |
| 2188 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-001 | permitted | bound by precedent | REC-FL-A-00075 |  |
| 2189 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted | decided fresh | — |  |
| 2190 | Route parameter changes through the amendment workflow instead | FL-GV-009 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 2191 | Restrict weight egress to the declared perimeter buckets | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 2192 | Disable the government-request log for the bulk export tool | FL-PV-004 | denied | bound by precedent | REC-FL-B-01947 |  |
| 2193 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2194 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-008 | permitted | bound by precedent | REC-FL-A-00398 |  |
| 2195 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-001 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 2196 | Publish the signing certificate chain alongside each release digest | FL-MB-008 | denied | bound by precedent | REC-S0005 |  |
| 2197 | Let the agent mark the failing provenance test as skipped | FL-AG-002 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 2198 | Backfill lineage records for the older quantised checkpoints | FL-MB-007 | permitted | bound by precedent | REC-FL-L-01848 | ● |
| 2199 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted | decided fresh | — |  |
| 2200 | Pin the key-value cache budget for the agentic serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2201 | Backfill lineage records for the older quantised checkpoints | FL-MB-007 | permitted | bound by precedent | REC-FL-L-00098 |  |
| 2202 | Write a docket entry for every arrival that is not charged | FL-GV-011 | permitted | decided fresh | — |  |
| 2203 | Diff the model card against the previous release before publishing | FL-TR-003 | denied | bound by precedent | REC-FL-C-01193 |  |
| 2204 | Expose a contest path to affected customers in the portal | FL-GV-007 | permitted | decided fresh | — |  |
| 2205 | Record the compute-threshold determination separately per jurisdiction | FL-GV-007 | permitted | decided fresh | — |  |
| 2206 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | denied | bound by precedent | REC-S0032 |  |
| 2207 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-008 | permitted | decided fresh | — |  |
| 2208 | Fail the build when an agent commit arrives unsigned | FL-AG-008 | permitted | decided fresh | — |  |
| 2209 | Record a disposition for every referral the board acknowledges | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 2210 | Name a data-governance custodian on each dataset record | FL-TD-006 | permitted | bound by precedent | REC-FL-N-00889 |  |
| 2211 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 2212 | Make decision records append-only in the store schema | FL-GV-009 | permitted | decided fresh | — |  |
| 2213 | Record the capability-threshold determination on the release record | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 2214 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-008 | permitted | bound by precedent | REC-FL-C-01033 |  |
| 2215 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 2216 | Remove the contest link from the customer decision notice | FL-GV-001 FL-SC-004 ⛔ | denied | refused at the floor | — |  |
| 2217 | Measure membership-inference advantage on the release candidate | FL-LS-007 | permitted | bound by precedent | REC-S0029 |  |
| 2218 | Add the new sampling library to the licence inventory | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 2219 | Embed the canary string in every generated evaluation case | FL-EV-004 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 2220 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2221 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 |  |
| 2222 | Rewrite the last raw query in the usage-reporting job | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2223 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-008 | denied | bound by precedent | REC-S0013 |  |
| 2224 | Require two-person authorisation for unreleased-weight access | FL-SF-009 | permitted | decided fresh | — |  |
| 2225 | Record the builder identity in attestations for nightly checkpoints | FL-SC-008 | permitted | bound by precedent | REC-FL-L-01172 |  |
| 2226 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-005 | denied | decided fresh | — |  |
| 2227 | Strip annotator identity from the exported preference dataset | FL-PV-001 | permitted with conditions | bound by precedent | REC-FL-G-02086 | ● |
| 2228 | Report refusal and over-refusal rates side by side | FL-BS-004 | permitted | decided fresh | — |  |
| 2229 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-004 | permitted | decided fresh | — |  |
| 2230 | Measure judge and human agreement for the new grader configuration | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 2231 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-B-00545 |  |
| 2232 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | permitted with conditions | decided fresh | — | ● |
| 2233 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-007 | permitted | decided fresh | — |  |
| 2234 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-007 | permitted | bound by precedent | REC-FL-L-00098 |  |
| 2235 | Declare both base models in the merged cirrus-small manifest | FL-MB-008 | permitted with conditions | decided fresh | — | ● |
| 2236 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted | bound by precedent | REC-FL-A-00075 |  |
| 2237 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | decided fresh | — |  |
| 2238 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | bound by precedent | REC-FL-C-01156 |  |
| 2239 | Route threshold-crossing results to an automatic deployment hold | FL-CB-003 | permitted with conditions | decided fresh | — | ● |
| 2240 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-002 | permitted with conditions | decided fresh | — | ● |
| 2241 | Keep cases released after the training cutoff in the holdout | FL-EV-008 | permitted | bound by precedent | REC-S0039 | ● |
| 2242 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 2243 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted with conditions | bound by precedent | REC-FL-G-02163 |  |
| 2244 | Validate tenant scope on every portal export request | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2245 | Require a human reviewer on agent changes to request routing | FL-AG-007 | permitted | bound by precedent | REC-S0023 |  |
| 2246 | Let the runtime environment override the agent's recursion limit | FL-FG-001 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 2247 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | bound by precedent | REC-FL-A-00061 |  |
| 2248 | Keep the toxicity filter in the response path for streaming replies | FL-BS-005 | permitted with conditions | decided fresh | — | ● |
| 2249 | Publish the signing certificate chain alongside each release digest | FL-MB-007 | permitted | bound by precedent | REC-FL-L-00098 |  |
| 2250 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted | decided fresh | — |  |
| 2251 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-006 | permitted | decided fresh | — |  |
| 2252 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 2253 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-003 | denied | bound by precedent | REC-FL-C-02030 | ● |
| 2254 | Document the subject-request path for the preference store | FL-PI-006 | permitted | decided fresh | — |  |
| 2255 | Publish the prompt-log retention clock in the customer portal | FL-PI-006 | permitted | decided fresh | — |  |
| 2256 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-002 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 2257 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted with conditions | bound by precedent | REC-FL-G-02120 |  |
| 2258 | Retire two supply-chain provisions from the rulebook manifest | FL-UH-002 | denied | decided fresh | — |  |
| 2259 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-007 | denied | bound by precedent | REC-S0019 |  |
| 2260 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2261 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | permitted | bound by precedent | REC-FL-C-01217 |  |
| 2262 | Log every read of the weights store to the perimeter audit trail | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 2263 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 2264 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | decided fresh | — |  |
| 2265 | Make decision records append-only in the store schema | FL-GV-010 | permitted with conditions | bound by precedent | REC-FL-C-01357 |  |
| 2266 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2267 | Store the provenance chain for derived synthetic corpora | FL-TD-007 | permitted | bound by precedent | REC-FL-N-01054 | ● |
| 2268 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 2269 | State the percentile on every latency claim in the dashboard | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 2270 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted | bound by precedent | REC-FL-C-01033 |  |
| 2271 | Sign agent commits with a workload identity rather than a person's key | FL-AG-004 | permitted | decided fresh | — |  |
| 2272 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 2273 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | permitted | decided fresh | — | ● |
| 2274 | Open the agentic tier to customers while the safety case is in draft | FL-SF-003 ⛔ | denied | refused at the floor | — |  |
| 2275 | Move retrieved documents into a separate, clearly marked context block | FL-LS-006 | permitted | bound by precedent | REC-S0028 |  |
| 2276 | Separate the production prompt label from its version string | FL-MB-006 | permitted | disposed by citation | — |  |
| 2277 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-B-00545 |  |
| 2278 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | decided fresh | — |  |
| 2279 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 |  |
| 2280 | Report first-token and per-token latency against the tier budgets | FL-IN-008 | permitted | docketed — not charged | — |  |
| 2281 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00711 |  |
| 2282 | Train on the partner's user conversations before the basis is recorded | FL-PI-001 FL-CS-004 ⛔ | denied | refused at the floor | — |  |
| 2283 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-004 | permitted | bound by precedent | REC-FL-A-00805 |  |
| 2284 | Hold goodput at the tier threshold under the burst profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2285 | Move release signing keys onto the hardware security module | FL-SF-005 | permitted | bound by precedent | REC-FL-C-01852 |  |
| 2286 | Record the prompt and context hash on each agent commit | FL-AG-005 | permitted | decided fresh | — |  |
| 2287 | Reject imports for packages first published within thirty days | FL-AG-005 | permitted | decided fresh | — |  |
| 2288 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-C-01480 |  |
| 2289 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-003 | permitted | decided fresh | — |  |
| 2290 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01351 |  |
| 2291 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 2292 | Run release builds on ephemeral runners with pinned images | FL-SC-003 | permitted | decided fresh | — |  |
| 2293 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-005 | denied | bound by precedent | REC-S0058 |  |
| 2294 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — |  |
| 2295 | Raise mitigations to match the assessed capability level | FL-SF-005 | permitted | decided fresh | — |  |
| 2296 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-001 FL-WX-003 ⛔ | denied | refused at the floor | — |  |
| 2297 | Backfill lineage records for the older quantised checkpoints | FL-MB-006 | permitted | bound by precedent | REC-FL-A-00462 |  |
| 2298 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 2299 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-002 | permitted with conditions | bound by precedent | REC-FL-G-02240 |  |
| 2300 | Document the subject-request path for the preference store | FL-PI-004 | permitted | decided fresh | — | ● |
| 2301 | Commit the live cluster token into the test fixtures directory | FL-SC-002 | denied | bound by precedent | REC-FL-B-00463 |  |
| 2302 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 2303 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-006 | permitted | bound by precedent | REC-FL-N-02066 |  |
| 2304 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — |  |
| 2305 | Measure membership-inference advantage on the release candidate | FL-LS-006 | permitted | bound by precedent | REC-FL-A-01600 | ● |
| 2306 | Record the capability-threshold determination on the release record | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 2307 | Load a customer's fine-tune adapter for another tenant's inference request | FL-PV-003 ⛔ | denied | refused at the floor | — |  |
| 2308 | Move the minor-mode restriction check from the client SDK into the gateway | FL-CS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 2309 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 2310 | Run semantic analysis over the agent diff in continuous integration | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00244 |  |
| 2311 | Route the child-safety escalation queue to a staffed on-call rotation | FL-CS-004 | permitted | decided fresh | — |  |
| 2312 | Route the child-safety escalation queue to a staffed on-call rotation | FL-CS-004 | permitted | decided fresh | — |  |
| 2313 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | bound by precedent | REC-FL-L-00444 |  |
| 2314 | Propagate attribution obligations from corpus records to release notes | FL-TD-005 | permitted | decided fresh | — |  |
| 2315 | Keep the toxicity filter in the response path for streaming replies | FL-BS-003 | denied | bound by precedent | REC-FL-C-01702 |  |
| 2316 | Record the builder identity in attestations for nightly checkpoints | FL-SC-008 | permitted | decided fresh | — |  |
| 2317 | Document the subject-request path for the preference store | FL-PI-003 | permitted | bound by precedent | REC-FL-A-00034 |  |
| 2318 | Compare the provenance subject digest to the distributed artifact | FL-SC-007 | permitted | decided fresh | — |  |
| 2319 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-007 | permitted | decided fresh | — |  |
| 2320 | Relax the coverage floor in the policy bundle to unblock a release train | FL-AG-006 | denied | decided fresh | — |  |
| 2321 | Separate the audit register from the precedent store at schema level | FL-GV-005 | permitted | decided fresh | — |  |
| 2322 | Remove the non-human disclosure line from the companion persona's opening message | FL-UH-005 | denied | bound by precedent | REC-FL-B-00780 | ● |
| 2323 | Separate the production prompt label from its version string | FL-MB-009 | permitted | decided fresh | — | ● |
| 2324 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted | bound by precedent | REC-FL-A-00642 |  |
| 2325 | Record the compute-threshold determination separately per jurisdiction | FL-GV-006 | permitted | decided fresh | — |  |
| 2326 | Give every system prompt an immutable version identifier | FL-MB-008 | permitted with conditions | bound by precedent | REC-FL-G-02235 |  |
| 2327 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-002 | permitted | decided fresh | — | ● |
| 2328 | Redact prompt and completion logs before they reach retention | FL-PI-003 | permitted | bound by precedent | REC-FL-C-01197 | ● |
| 2329 | Point the canary tier at a checkpoint that was never registered | FL-MB-009 | denied | decided fresh | — |  |
| 2330 | Restrict agent outbound calls to the allowlisted host set | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00921 |  |
| 2331 | Return a generic error identifier instead of the stack trace | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2332 | Fail closed when a dataset licence string does not parse | FL-TD-008 | permitted | bound by precedent | REC-FL-N-00298 |  |
| 2333 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-004 | permitted | decided fresh | — |  |
| 2334 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-004 | permitted with conditions | bound by precedent | REC-FL-G-02232 |  |
| 2335 | Move release signing keys onto the hardware security module | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 2336 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted with conditions | bound by precedent | REC-FL-G-02163 |  |
| 2337 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-002 | permitted | decided fresh | — |  |
| 2338 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-002 | permitted | decided fresh | — |  |
| 2339 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted | decided fresh | — |  |
| 2340 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted | bound by precedent | REC-FL-A-01660 |  |
| 2341 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted | decided fresh | — |  |
| 2342 | Add a weekly sampling job over production refusals | FL-BS-006 | permitted | decided fresh | — |  |
| 2343 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 2344 | Fail the run outright when no loop limit is declared | FL-FG-002 | permitted with conditions | bound by precedent | REC-FL-C-02110 |  |
| 2345 | Embed the canary string in every generated evaluation case | FL-EV-005 | permitted | decided fresh | — |  |
| 2346 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted | bound by precedent | REC-FL-C-02008 |  |
| 2347 | Extend the erasure-processing window to six weeks in the deletion job | FL-PV-005 | denied | decided fresh | — |  |
| 2348 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-C-01679 |  |
| 2349 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 2350 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-006 | permitted | bound by precedent | REC-FL-L-00788 |  |
| 2351 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 2352 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | bound by precedent | REC-FL-L-00863 |  |
| 2353 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-002 | permitted | decided fresh | — |  |
| 2354 | Verify de-identification by sampling rather than by assertion | FL-PI-006 | permitted with conditions | bound by precedent | REC-FL-C-01031 |  |
| 2355 | Validate tenant scope on every portal export request | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2356 | Publish a review checklist for agent changes to the eval harness | FL-AG-004 | permitted with conditions | bound by precedent | REC-FL-G-02232 |  |
| 2357 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-002 ⛔ | denied | refused at the floor | — |  |
| 2358 | Pin every dependency to an immutable digest in the lockfile | FL-SC-007 | permitted | disposed by citation | — |  |
| 2359 | Declare the arrival distribution used in the throughput benchmark | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2360 | Parameterise the new experiment-metrics filter queries | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2361 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-006 | denied | bound by precedent | REC-S0018 |  |
| 2362 | Log every read of the weights store to the perimeter audit trail | FL-SF-008 | permitted | decided fresh | — |  |
| 2363 | Raise mitigations to match the assessed capability level | FL-SF-008 | permitted | decided fresh | — |  |
| 2364 | Keep cases released after the training cutoff in the holdout | FL-EV-010 | permitted with conditions | decided fresh | — | ● |
| 2365 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-005 | denied | bound by precedent | REC-S0058 |  |
| 2366 | Screen new fine-tuning shards for backdoor triggers | FL-LS-009 | permitted | decided fresh | — |  |
| 2367 | Document which attack class the new defence was evaluated against | FL-LS-009 | permitted | decided fresh | — |  |
| 2368 | List only the instruct parent on the merged checkpoint card | FL-MB-003 FL-LS-006 ⛔ | denied | refused at the floor | — |  |
| 2369 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 2370 | Respect the robots.txt AI directive in the web crawler | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 2371 | Record the builder identity in attestations for nightly checkpoints | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 | ● |
| 2372 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 2373 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | bound by precedent | REC-FL-N-00294 |  |
| 2374 | Widen the prompt-label review rule to cover staging labels too | FL-SC-005 | denied | decided fresh | — |  |
| 2375 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 2376 | Fail the build on scan findings above the severity threshold | FL-SC-002 | permitted | decided fresh | — | ● |
| 2377 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-006 | denied | bound by precedent | REC-FL-B-00231 |  |
| 2378 | Record the frontier framework version in force on the release record | FL-SF-006 | permitted | decided fresh | — |  |
| 2379 | Register the new fused kernel as a nondeterministic operation | FL-IN-004 | denied | bound by precedent | REC-S0049 |  |
| 2380 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 2381 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | bound by precedent | REC-FL-C-02267 |  |
| 2382 | Exercise injection detection on the changed tool-calling path | FL-LS-011 | permitted | decided fresh | — |  |
| 2383 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-002 | permitted | bound by precedent | REC-FL-A-00676 |  |
| 2384 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted | decided fresh | — |  |
| 2385 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-001 | permitted | decided fresh | — |  |
| 2386 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | permitted | decided fresh | — |  |
| 2387 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 2388 | Propagate attribution obligations from corpus records to release notes | FL-TD-006 | denied | bound by precedent | REC-S0011 |  |
| 2389 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-009 | permitted | decided fresh | — |  |
| 2390 | Make the inference-engine build hermetic and reproducible | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 |  |
| 2391 | Widen the parity report to distinguish immaterial differences | FL-EV-007 | permitted | decided fresh | — |  |
| 2392 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-007 | permitted | decided fresh | — |  |
| 2393 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00711 |  |
| 2394 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted | decided fresh | — | ● |
| 2395 | Write a docket entry for every arrival that is not charged | FL-GV-008 | denied | bound by precedent | REC-S0070 |  |
| 2396 | Enforce server-side authorization on the new batch endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 2397 | Pin the catastrophic-risk eval harness version in the release record | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-C-02057 |  |
| 2398 | Give the batch agent the shared service account to dodge quota holds | FL-FG-001 FL-EV-007 ⛔ | denied | refused at the floor | — |  |
| 2399 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-006 | permitted with conditions | bound by precedent | REC-FL-C-01240 |  |
| 2400 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 2401 | Publish the notice file alongside each inference-engine release | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 2402 | Redact prompt and completion logs before they reach retention | FL-PI-002 | denied | bound by precedent | REC-S0014 |  |
| 2403 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-006 | permitted | disposed by citation | — |  |
| 2404 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | bound by precedent | REC-FL-L-00444 |  |
| 2405 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-003 | permitted | decided fresh | — |  |
| 2406 | Hold the audit register in a store the retrieval path cannot read | FL-GV-011 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2407 | Publish a review checklist for agent changes to the eval harness | FL-AG-004 | permitted | decided fresh | — |  |
| 2408 | Sign agent commits with a workload identity rather than a person's key | FL-AG-004 | permitted | decided fresh | — |  |
| 2409 | Pin every dependency to an immutable digest in the lockfile | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 2410 | Run the personal-data scan on every new training shard | FL-PI-006 | permitted with conditions | bound by precedent | REC-FL-C-01031 |  |
| 2411 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted | decided fresh | — |  |
| 2412 | Route critical-incident detection signals to the on-call dashboard instead of the reporting queue | FL-TR-004 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 2413 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-003 | denied | bound by precedent | REC-FL-B-01491 | ● |
| 2414 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | decided fresh | — |  |
| 2415 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-009 | permitted | bound by precedent | REC-FL-L-02323 |  |
| 2416 | Remove the graphic-content exposure limits from the labeling-queue config | FL-PV-003 FL-TD-005 ⛔ | denied | refused at the floor | — |  |
| 2417 | Pin workflow actions to commit digests across the release repository | FL-SC-008 | permitted | bound by precedent | REC-FL-L-01172 |  |
| 2418 | Open the agentic tier to customers while the safety case is in draft | FL-SF-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 2419 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-003 | denied | bound by precedent | REC-S0056 |  |
| 2420 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-006 | denied | decided fresh | — |  |
| 2421 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh | — | ● |
| 2422 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-006 | permitted | bound by precedent | REC-FL-A-00462 |  |
| 2423 | Update the third-party licence inventory with this dependency change | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 2424 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | denied | bound by precedent | REC-S0054 |  |
| 2425 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2426 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-008 | denied | bound by precedent | REC-S0005 |  |
| 2427 | Escape tool output before it reaches the shell adapter | FL-LS-003 | permitted | decided fresh | — |  |
| 2428 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 2429 | Document which attack class the new defence was evaluated against | FL-LS-004 | denied | bound by precedent | REC-S0026 |  |
| 2430 | Keep the human override reachable in the high-risk review flow | FL-GV-008 | permitted | decided fresh | — |  |
| 2431 | Make decision records append-only in the store schema | FL-GV-008 | permitted | decided fresh | — |  |
| 2432 | Enforce server-side authorization on the new batch endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 2433 | Bind weight-store access grants to the current personnel-vetting record | FL-WX-003 | denied | bound by precedent | REC-S0082 |  |
| 2434 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2435 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-002 | permitted | bound by precedent | REC-FL-A-00676 |  |
| 2436 | Report refusal and over-refusal rates side by side | FL-BS-006 | permitted | decided fresh | — |  |
| 2437 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 2438 | Merge the streaming path whose profile still leaks after warm-up | FL-IN-001 | denied | decided fresh | — |  |
| 2439 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted with conditions | bound by precedent | REC-FL-G-02375 |  |
| 2440 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 2441 | Keep reporter bulletins off the adjudication input path | FL-GV-009 | permitted | decided fresh | — |  |
| 2442 | Move retrieved documents into a separate, clearly marked context block | FL-LS-007 | permitted | decided fresh | — |  |
| 2443 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-004 | permitted | decided fresh | — |  |
| 2444 | Add an autonomous-replication probe to the agentic-checkpoint sandbox | FL-CB-004 | permitted | decided fresh | — |  |
| 2445 | Justify the two remaining special-category fields on the dataset record | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01496 |  |
| 2446 | Reject unexpected content types on the tool-callback endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2447 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-C-01409 |  |
| 2448 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 2449 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | bound by precedent | REC-S0006 |  |
| 2450 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted | decided fresh | — |  |
| 2451 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-007 | permitted | decided fresh | — |  |
| 2452 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-001 | permitted | decided fresh | — |  |
| 2453 | Embed the canary string in every generated evaluation case | FL-EV-005 | permitted with conditions | decided fresh | — | ● |
| 2454 | Scope the retrieval index to the tenant boundary at query time | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 2455 | Attach Croissant metadata to the new publisher corpus | FL-TD-003 | permitted with conditions | bound by precedent | REC-S0008 |  |
| 2456 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-002 | permitted | decided fresh | — |  |
| 2457 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01474 |  |
| 2458 | Hold goodput at the tier threshold under the burst profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2459 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | bound by precedent | REC-S0089 | ● |
| 2460 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-005 | denied | decided fresh | — |  |
| 2461 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 2462 | Run the personal-data scan on every new training shard | FL-PI-004 | permitted | bound by precedent | REC-FL-N-01746 |  |
| 2463 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted | decided fresh | — |  |
| 2464 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-006 | permitted with conditions | bound by precedent | REC-FL-G-02375 |  |
| 2465 | Track system-prompt versions in a free-text description field | FL-MB-004 | denied | decided fresh | — | ● |
| 2466 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | bound by precedent | REC-FL-L-01848 |  |
| 2467 | Fail the merge when the scanner reports an unresolved licence | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 2468 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | bound by precedent | REC-FL-C-02305 | ● |
| 2469 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 2470 | Record a lawful basis for each conversation-data source | FL-PI-002 | permitted | bound by precedent | REC-FL-N-01610 |  |
| 2471 | Expose a contest path to affected customers in the portal | FL-GV-005 | permitted | decided fresh | — |  |
| 2472 | Log the named authority for every override exercised | FL-GV-005 | permitted | decided fresh | — |  |
| 2473 | Have the crawler submit the consent form to reach the archive body | FL-TD-001 ⛔ | denied | refused at the floor | — |  |
| 2474 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 2475 | Declare the agent loop limit numerically with its units | FL-FG-003 | denied | bound by precedent | REC-FL-C-01270 | ● |
| 2476 | Block internal address ranges in the web-fetch tool | FL-AS-002 | permitted | docketed — not charged | — |  |
| 2477 | Route threshold-crossing results to an automatic deployment hold | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 2478 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-005 | permitted | bound by precedent | REC-S0036 |  |
| 2479 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — |  |
| 2480 | Shorten the report-preservation window in the retention job to ninety days | FL-CS-003 | denied | bound by precedent | REC-FL-B-01876 |  |
| 2481 | Loosen the toxicity cut-off in the gate config to clear the backlog | FL-BS-002 | denied | decided fresh | — |  |
| 2482 | Run the decontamination check over the new code corpus | FL-EV-008 | permitted | bound by precedent | REC-FL-A-00398 | ● |
| 2483 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh | — | ● |
| 2484 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted with conditions | bound by precedent | REC-FL-C-02156 |  |
| 2485 | Keep cases released after the training cutoff in the holdout | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 2486 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-004 | permitted | decided fresh | — | ● |
| 2487 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-004 | permitted | bound by precedent | REC-S0091 |  |
| 2488 | Scan responses for canary tokens before they leave the gateway | FL-LS-005 | permitted | decided fresh | — |  |
| 2489 | Measure membership-inference advantage on the release candidate | FL-LS-005 | permitted | decided fresh | — |  |
| 2490 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 2491 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | denied | bound by precedent | REC-S0001 | ● |
| 2492 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-002 | permitted | decided fresh | — |  |
| 2493 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-002 | permitted | decided fresh | — |  |
| 2494 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | decided fresh | — |  |
| 2495 | Block promotion until the dangerous-capability reports complete | FL-SF-004 | permitted | bound by precedent | REC-S0041 |  |
| 2496 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-010 | permitted | decided fresh | — |  |
| 2497 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 2498 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted | decided fresh | — |  |
| 2499 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2500 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 |  |
| 2501 | Declare the arrival distribution used in the throughput benchmark | FL-IN-002 | permitted | decided fresh | — |  |
| 2502 | Skip signature verification on load to cut startup time | FL-MB-005 | denied | bound by precedent | REC-FL-B-01323 |  |
| 2503 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 2504 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | denied | bound by precedent | REC-S0007 | ● |
| 2505 | Deploy the model line before the transparency report is published | FL-TR-001 FL-SC-008 ⛔ | denied | refused at the floor | — |  |
| 2506 | Declare sample size and percentile alongside the parity result | FL-EV-004 | permitted | decided fresh | — |  |
| 2507 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-004 | permitted | bound by precedent | REC-FL-N-01746 |  |
| 2508 | Record the tolerance band used for each accuracy comparison | FL-EV-010 | permitted | decided fresh | — |  |
| 2509 | Screen new fine-tuning shards for backdoor triggers | FL-LS-007 | permitted | bound by precedent | REC-S0029 |  |
| 2510 | Return a generic error identifier instead of the stack trace | — | permitted | docketed — nothing engaged | — |  |
| 2511 | Cut the mandatory-reporting webhook's median delay to under a minute | FL-CS-004 | permitted | decided fresh | — |  |
| 2512 | Wire the verified age signal through to the safety filter's request context | FL-CS-004 | permitted | decided fresh | — |  |
| 2513 | Record the capability-threshold determination on the release record | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 2514 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-BS-006 | denied | decided fresh | — |  |
| 2515 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | bound by precedent | REC-FL-C-02468 |  |
| 2516 | Sample the abuse-monitoring pipeline at one percent to cut compute cost | FL-UH-005 | denied | decided fresh | — |  |
| 2517 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | denied | bound by precedent | REC-S0014 | ● |
| 2518 | Log every read of the weights store to the perimeter audit trail | FL-SF-003 ⛔ | permitted | decided fresh | — |  |
| 2519 | Restrict weight egress to the declared perimeter buckets | FL-SF-003 ⛔ | permitted | decided fresh | — |  |
| 2520 | Pin the golden-prompt baseline to a commit digest | FL-EV-007 | permitted | bound by precedent | REC-FL-A-01842 |  |
| 2521 | Move retrieved documents into a separate, clearly marked context block | FL-LS-010 | permitted | decided fresh | — |  |
| 2522 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 2523 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — |  |
| 2524 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2525 | Replace the manual denied-party screening spreadsheet with an automated gateway check | FL-WX-003 | denied | bound by precedent | REC-S0082 |  |
| 2526 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted | decided fresh | — |  |
| 2527 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted with conditions | bound by precedent | REC-FL-G-02474 |  |
| 2528 | Hold goodput at the tier threshold under the burst profile | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 2529 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | denied | bound by precedent | REC-S0010 | ● |
| 2530 | Scan responses for canary tokens before they leave the gateway | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 2531 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2532 | Check the code-signing extended key usage on the release chain | FL-MB-007 | permitted | decided fresh | — |  |
| 2533 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | decided fresh | — |  |
| 2534 | Land the new forum corpus with its provenance fields left blank | FL-TD-008 | denied | decided fresh | — |  |
| 2535 | Move retrieved documents into a separate, clearly marked context block | FL-LS-004 | permitted | bound by precedent | REC-FL-A-02486 |  |
| 2536 | Ship the research agent with no turn limit in its configuration | FL-FG-001 ⛔ | denied | refused at the floor | — |  |
| 2537 | Make the government-request log append-only across the bulk-export path | FL-PV-004 | permitted | bound by precedent | REC-FL-A-00805 |  |
| 2538 | Apply an allowlist to the retrieval connector's target parameter | — | permitted | docketed — nothing engaged | — |  |
| 2539 | Declare the downstream sink for every model output field | FL-LS-003 | permitted | decided fresh | — |  |
| 2540 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | bound by precedent | REC-FL-C-01441 |  |
| 2541 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 2542 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | denied | bound by precedent | REC-FL-C-02529 | ● |
| 2543 | Require human confirmation before the agent executes a write tool | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 2544 | Attribute the standing declaration in the exported rulebook | FL-GV-007 | permitted | decided fresh | — | ● |
| 2545 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | permitted with conditions | bound by precedent | REC-FL-G-02474 |  |
| 2546 | Enforce server-side authorization on the new batch endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 2547 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | permitted | bound by precedent | REC-FL-C-02371 |  |
| 2548 | Require two-person authorisation for unreleased-weight access | FL-SF-001 ⛔ | permitted | decided fresh | — |  |
| 2549 | Record the capability-threshold determination on the release record | FL-SF-001 ⛔ | permitted | decided fresh | — |  |
| 2550 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | bound by precedent | REC-FL-C-02459 |  |
| 2551 | Justify the two remaining special-category fields on the dataset record | FL-PI-005 | permitted | decided fresh | — |  |
| 2552 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted | bound by precedent | REC-FL-C-02482 |  |
| 2553 | Strip internal identifiers from gateway error responses | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2554 | Resolve internal packages from the private registry first | FL-SC-002 | permitted | bound by precedent | REC-FL-L-02376 |  |
| 2555 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-004 | permitted | decided fresh | — |  |
| 2556 | Hold goodput at the tier threshold under the burst profile | FL-IN-004 | permitted | decided fresh | — |  |
| 2557 | Ship the image whose layer digests no longer match the recorded inventory | FL-SC-007 | denied | decided fresh | — |  |
| 2558 | Make the inference-engine build hermetic and reproducible | FL-SC-002 | permitted | bound by precedent | REC-FL-L-01391 |  |
| 2559 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2560 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-003 | permitted | decided fresh | — |  |
| 2561 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01010 | ● |
| 2562 | Skip signature verification on load to cut startup time | FL-MB-006 | denied | decided fresh | — |  |
| 2563 | Project token spend before dispatching a long-horizon agent run | FL-FG-002 | permitted with conditions | bound by precedent | REC-FL-C-02110 |  |
| 2564 | Reject unexpected content types on the tool-callback endpoint | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2565 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 2566 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 2567 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | bound by precedent | REC-FL-B-00890 |  |
| 2568 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 2569 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-008 | permitted | bound by precedent | REC-FL-L-01172 |  |
| 2570 | Keep reporter bulletins off the adjudication input path | FL-GV-006 | permitted | decided fresh | — |  |
| 2571 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-008 | permitted | bound by precedent | REC-FL-A-00398 | ● |
| 2572 | Require the safety-case signature from outside the authoring team | FL-SF-005 | permitted | decided fresh | — | ● |
| 2573 | Report preemption counts in the load-test summary | FL-IN-002 | permitted | bound by precedent | REC-FL-A-02327 |  |
| 2574 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-003 | denied | decided fresh | — |  |
| 2575 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | bound by precedent | REC-FL-C-01653 | ● |
| 2576 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 2577 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-005 | permitted | bound by precedent | REC-S0092 |  |
| 2578 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-004 | permitted | decided fresh | — |  |
| 2579 | Report refusal and over-refusal rates side by side | FL-BS-004 | permitted | decided fresh | — |  |
| 2580 | Hardcode a real customer address into the escalation prompt template | FL-PI-001 FL-LS-006 ⛔ | denied | refused at the floor | — |  |
| 2581 | Enforce the instruction and data boundary on the retrieval path | FL-LS-007 | permitted | bound by precedent | REC-S0029 |  |
| 2582 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2583 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-001 | denied | decided fresh | — | ● |
| 2584 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted | decided fresh | — |  |
| 2585 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-001 | permitted | bound by precedent | REC-FL-C-02459 |  |
| 2586 | Batch regulator notifications into the weekly digest instead | FL-SF-006 | denied | decided fresh | — |  |
| 2587 | Record the elicitation effort alongside every uplift-eval result | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-C-02057 | ● |
| 2588 | Parameterise the new experiment-metrics filter queries | — | permitted | docketed — nothing engaged | — |  |
| 2589 | Expose a contest path to affected customers in the portal | FL-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2590 | Record a disposition for every referral the board acknowledges | FL-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2591 | Replace the model card's static training-summary section with a generated one | FL-TR-002 | permitted with conditions | bound by precedent | REC-FL-C-01328 |  |
| 2592 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-004 | permitted | decided fresh | — |  |
| 2593 | Run the decontamination check over the new code corpus | FL-EV-005 | permitted | bound by precedent | REC-FL-C-01255 |  |
| 2594 | Point the canary tier at a checkpoint that was never registered | FL-MB-001 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 2595 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-B-00111 |  |
| 2596 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2597 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | bound by precedent | REC-FL-C-02468 |  |
| 2598 | Make the inference-engine build hermetic and reproducible | FL-SC-008 | permitted | decided fresh | — |  |
| 2599 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted | bound by precedent | REC-FL-A-00034 |  |
| 2600 | Scan responses for canary tokens before they leave the gateway | FL-LS-009 | permitted | decided fresh | — |  |
| 2601 | Enforce the instruction and data boundary on the retrieval path | FL-LS-009 | permitted | decided fresh | — |  |
| 2602 | Run agent-authored code only inside the sandboxed runner | FL-AG-005 | permitted | decided fresh | — |  |
| 2603 | Add audio-generation coverage to the abuse-material classifier suite | FL-CS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 2604 | Redact prompt and completion logs before they reach retention | FL-PI-006 | permitted | decided fresh | — | ● |
| 2605 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-005 | denied | bound by precedent | REC-FL-C-01480 | ● |
| 2606 | Declare both base models in the merged cirrus-small manifest | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 2607 | Recompute the root digest from resource digests before promotion | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 2608 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | bound by precedent | REC-FL-C-02267 |  |
| 2609 | Carry attribution notices through to the shipped container image | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 2610 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-003 | denied | bound by precedent | REC-FL-B-00304 |  |
| 2611 | Name a data-governance custodian on each dataset record | FL-TD-001 ⛔ | permitted | decided fresh | — |  |
| 2612 | Name a data-governance custodian on each dataset record | FL-TD-001 ⛔ | permitted | decided fresh | — |  |
| 2613 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 2614 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-C-01679 |  |
| 2615 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh | — |  |
| 2616 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01698 |  |
| 2617 | Move retrieved documents into a separate, clearly marked context block | FL-LS-004 | permitted | decided fresh | — |  |
| 2618 | Commit the live cluster token into the test fixtures directory | FL-SC-002 | denied | bound by precedent | REC-FL-B-00463 |  |
| 2619 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 2620 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-B-00111 |  |
| 2621 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-001 FL-PI-006 ⛔ | denied | refused at the floor | — |  |
| 2622 | Split personal-data handling out of the shared ingestion library | FL-PI-004 | denied | bound by precedent | REC-S0016 |  |
| 2623 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-001 | permitted | decided fresh | — |  |
| 2624 | Scope the retrieval index to the tenant boundary at query time | FL-PV-001 | permitted | decided fresh | — |  |
| 2625 | Write zero-retention tenant prompts to the debug capture store during an incident | FL-PV-001 | denied | decided fresh | — |  |
| 2626 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | denied | bound by precedent | REC-S0087 |  |
| 2627 | Screen generated code against the copyleft signature database | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 2628 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2629 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-003 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 2630 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 2631 | Replace the model card's static training-summary section with a generated one | FL-TR-001 ⛔ | permitted | decided fresh | — |  |
| 2632 | Test marking survivability across the video transcoder's re-encode step | FL-TR-001 ⛔ | permitted | decided fresh | — |  |
| 2633 | State turns rather than seconds as the loop-limit unit | FL-FG-006 | permitted | bound by precedent | REC-FL-A-00540 |  |
| 2634 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-001 | permitted | decided fresh | — |  |
| 2635 | Log the named authority for every override exercised | FL-GV-009 | permitted with conditions | bound by precedent | REC-FL-C-01993 |  |
| 2636 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 2637 | Require two-person authorisation for unreleased-weight access | FL-SF-009 | permitted | bound by precedent | REC-S0075 |  |
| 2638 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 2639 | Record the frontier framework version in force on the release record | FL-SF-009 | permitted | bound by precedent | REC-S0075 |  |
| 2640 | Let the runtime environment override the agent's recursion limit | FL-FG-002 | denied | decided fresh | — |  |
| 2641 | Restrict agent outbound calls to the allowlisted host set | FL-AG-005 | permitted | disposed by citation | — |  |
| 2642 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | denied | bound by precedent | REC-FL-C-02491 |  |
| 2643 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2644 | Name a data-governance custodian on each dataset record | FL-TD-006 | permitted | bound by precedent | REC-FL-N-00889 |  |
| 2645 | Measure judge and human agreement for the new grader configuration | FL-EV-004 | permitted | decided fresh | — |  |
| 2646 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted | decided fresh | — |  |
| 2647 | Propose an amendment codifying coverage rules for generated eval configs | FL-EV-006 | denied | decided fresh | — |  |
| 2648 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01373 |  |
| 2649 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 2650 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | bound by precedent | REC-FL-C-01694 |  |
| 2651 | Exercise injection detection on the changed tool-calling path | FL-LS-005 | permitted | decided fresh | — |  |
| 2652 | Declare the downstream sink for every model output field | FL-LS-006 | permitted | bound by precedent | REC-FL-A-01600 |  |
| 2653 | Alert when an agent run crosses eighty percent of its budget | FL-FG-001 ⛔ | permitted | decided fresh | — |  |
| 2654 | Put a circuit breaker on the recursive summarisation path | FL-FG-001 ⛔ | permitted | decided fresh | — |  |
| 2655 | Run release builds on ephemeral runners with pinned images | FL-SC-004 | permitted | bound by precedent | REC-FL-C-02371 | ● |
| 2656 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted | decided fresh | — |  |
| 2657 | Run agent-authored code only inside the sandboxed runner | FL-AG-005 | permitted with conditions | bound by precedent | REC-S0021 |  |
| 2658 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 2659 | Attribute the standing declaration in the exported rulebook | FL-GV-006 | denied | bound by precedent | REC-S0068 |  |
| 2660 | Document the subject-request path for the preference store | FL-PI-004 | permitted | decided fresh | — |  |
| 2661 | Write a docket entry for every arrival that is not charged | FL-GV-005 | permitted | decided fresh | — | ● |
| 2662 | List only the instruct parent on the merged checkpoint card | FL-MB-007 | denied | bound by precedent | REC-FL-C-01679 |  |
| 2663 | Write a docket entry for every arrival that is not charged | FL-GV-011 | permitted | decided fresh | — |  |
| 2664 | Broaden the refusal trigger list until safe prompts start bouncing | FL-BS-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 2665 | Compare the provenance subject digest to the distributed artifact | FL-SC-006 | permitted | bound by precedent | REC-S0064 | ● |
| 2666 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 2667 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-006 | denied | bound by precedent | REC-FL-B-00459 |  |
| 2668 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-003 | permitted | decided fresh | — |  |
| 2669 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-003 | permitted | decided fresh | — |  |
| 2670 | Record the tolerance band used for each accuracy comparison | FL-EV-007 | permitted | decided fresh | — |  |
| 2671 | Bake the build timestamp and hostname into the engine binary | FL-SC-007 | denied | decided fresh | — |  |
| 2672 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-002 | permitted with conditions | decided fresh | — | ● |
| 2673 | Verify de-identification by sampling rather than by assertion | FL-PI-004 | denied | bound by precedent | REC-S0016 | ● |
| 2674 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-003 | permitted | decided fresh | — |  |
| 2675 | Run the memorisation probe on the release candidate | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 2676 | Record the builder identity in attestations for nightly checkpoints | FL-SC-005 | permitted with conditions | bound by precedent | REC-FL-C-01565 | ● |
| 2677 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 2678 | Validate tenant scope on every portal export request | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2679 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | bound by precedent | REC-FL-C-01651 |  |
| 2680 | Screen generated code against the copyleft signature database | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 2681 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted | bound by precedent | REC-FL-A-00128 |  |
| 2682 | Log every weight-store read to the tamper-evident perimeter audit trail | FL-WX-003 | permitted with conditions | decided fresh | — | ● |
| 2683 | Hold the audit register in a store the retrieval path cannot read | FL-GV-010 | permitted with conditions | bound by precedent | REC-FL-C-01357 | ● |
| 2684 | Let retrieval read audit findings so precedent search returns more | FL-GV-007 | denied | decided fresh | — |  |
| 2685 | Fail the build on scan findings above the severity threshold | FL-SC-004 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 2686 | Bake the build timestamp and hostname into the engine binary | FL-SC-008 | denied | decided fresh | — |  |
| 2687 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted | decided fresh | — |  |
| 2688 | Declare the carrier channel for each untrusted input source | FL-LS-006 | permitted | decided fresh | — |  |
| 2689 | Exclude special-category fields from the support-transcript schema | FL-PI-003 | permitted | decided fresh | — |  |
| 2690 | Have the crawler submit the consent form to reach the archive body | FL-TD-002 | denied | bound by precedent | REC-FL-B-00538 |  |
| 2691 | Skip the crisis classifier on streaming responses to keep first-token latency low | FL-UH-004 | denied | decided fresh | — |  |
| 2692 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-003 ⛔ | permitted | decided fresh | — |  |
| 2693 | Require a human reviewer on agent changes to request routing | FL-AG-003 ⛔ | permitted | decided fresh | — |  |
| 2694 | Skip signature verification on load to cut startup time | FL-MB-005 | denied | bound by precedent | REC-FL-B-01323 |  |
| 2695 | Keep annotator identifiers in the exported preference dataset for the vendor handoff | FL-PV-004 | denied | decided fresh | — |  |
| 2696 | Project token spend before dispatching a long-horizon agent run | FL-FG-005 | permitted | bound by precedent | REC-S0053 | ● |
| 2697 | Name a data-governance custodian on each dataset record | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 2698 | Log the named authority for every override exercised | FL-GV-011 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2699 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 2700 | Give every system prompt an immutable version identifier | FL-MB-009 | permitted | bound by precedent | REC-S0006 |  |
| 2701 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 2702 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01854 |  |
| 2703 | Keep the toxicity filter in the response path for streaming replies | FL-BS-002 | permitted | decided fresh | — | ● |
| 2704 | Separate the audit register from the precedent store at schema level | FL-GV-008 | denied | bound by precedent | REC-S0070 |  |
| 2705 | Recompute the root digest from resource digests before promotion | FL-MB-009 | permitted | disposed by citation | — |  |
| 2706 | Let the summariser call itself on its own output with no stop condition | FL-FG-002 | denied | bound by precedent | REC-FL-C-01409 | ● |
| 2707 | Give the tool-call graph an explicit terminator | FL-FG-006 | permitted | decided fresh | — |  |
| 2708 | Drop the client-side age-assurance duplicate now that the server-side gate covers it | FL-CS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2709 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-007 | permitted | decided fresh | — |  |
| 2710 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-002 | permitted | decided fresh | — |  |
| 2711 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-002 | permitted | decided fresh | — |  |
| 2712 | Propagate attribution obligations from corpus records to release notes | FL-TD-007 | permitted | decided fresh | — |  |
| 2713 | Ship the prefill rewrite that pushes first-token time past budget | FL-IN-001 | denied | decided fresh | — | ● |
| 2714 | Move retrieved documents into a separate, clearly marked context block | FL-LS-005 | permitted | bound by precedent | REC-FL-C-01344 | ● |
| 2715 | Publish the notice file alongside each inference-engine release | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 2716 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted | decided fresh | — |  |
| 2717 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-002 | permitted with conditions | bound by precedent | REC-FL-C-02034 |  |
| 2718 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 2719 | Recompute the root digest from resource digests before promotion | FL-MB-004 | denied | bound by precedent | REC-FL-C-02491 | ● |
| 2720 | Move the loop-limit requirement out of the rulebook into service defaults | FL-SF-005 | denied | decided fresh | — |  |
| 2721 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-005 | permitted | bound by precedent | REC-FL-C-02167 |  |
| 2722 | Run release builds on ephemeral runners with pinned images | FL-SC-005 | permitted | decided fresh | — |  |
| 2723 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-007 | permitted | bound by precedent | REC-FL-L-00801 |  |
| 2724 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2725 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-001 | permitted | bound by precedent | REC-FL-C-02459 |  |
| 2726 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-006 | permitted | decided fresh | — | ● |
| 2727 | Add hash-list refresh monitoring to the training ingestion dashboard | FL-CS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2728 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-001 ⛔ | permitted | decided fresh | — |  |
| 2729 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-001 ⛔ | permitted | decided fresh | — |  |
| 2730 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 2731 | Report preemption counts in the load-test summary | FL-IN-004 | permitted | bound by precedent | REC-FL-A-01577 |  |
| 2732 | Report first-token and per-token latency against the tier budgets | FL-IN-003 | permitted | decided fresh | — |  |
| 2733 | Report preemption counts in the load-test summary | FL-IN-003 | permitted | decided fresh | — |  |
| 2734 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-002 | denied | decided fresh | — |  |
| 2735 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-002 | permitted with conditions | bound by precedent | REC-FL-G-02672 |  |
| 2736 | Route the child-safety escalation queue to a staffed on-call rotation | FL-CS-003 | permitted | decided fresh | — |  |
| 2737 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-007 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 2738 | Test egress-monitoring coverage in the quarterly weight-security drill | FL-WX-003 | permitted with conditions | decided fresh | — | ● |
| 2739 | Document the subject-request path for the preference store | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01318 |  |
| 2740 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 2741 | Run the personal-data scan on every new training shard | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01759 |  |
| 2742 | Ship the checkpoint past the uplift screen while the mitigation package is still in draft | FL-CB-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 2743 | Verify provenance against the expected builder identity before deploy | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 2744 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-007 | permitted | bound by precedent | REC-FL-N-01510 |  |
| 2745 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 2746 | Move cost control from a meter to a pre-flight breaker | FL-FG-002 | permitted with conditions | bound by precedent | REC-FL-C-02110 |  |
| 2747 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-005 | denied | decided fresh | — |  |
| 2748 | Register the new fused kernel as a nondeterministic operation | FL-IN-001 | permitted | decided fresh | — | ● |
| 2749 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-006 | permitted | bound by precedent | REC-S0064 |  |
| 2750 | Make decision records append-only in the store schema | FL-GV-003 ⛔ | permitted | decided fresh | — |  |
| 2751 | Route parameter changes through the amendment workflow instead | FL-GV-003 ⛔ | permitted | decided fresh | — |  |
| 2752 | Declare both base models in the merged cirrus-small manifest | FL-MB-007 | permitted | bound by precedent | REC-FL-C-02198 | ● |
| 2753 | Pipe the model's suggested shell command straight into the runner | FL-LS-004 | denied | decided fresh | — |  |
| 2754 | Check every new import against the upstream registry before build | FL-AG-005 | permitted | bound by precedent | REC-FL-L-00921 |  |
| 2755 | Block promotion until the dangerous-capability reports complete | FL-SF-008 | permitted | decided fresh | — |  |
| 2756 | Require the safety-case signature from outside the authoring team | FL-SF-008 | permitted | decided fresh | — |  |
| 2757 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2758 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted | bound by precedent | REC-FL-C-01229 | ● |
| 2759 | Respect the robots.txt AI directive in the web crawler | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 2760 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | denied | bound by precedent | REC-FL-C-02504 | ● |
| 2761 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | disposed by citation | — |  |
| 2762 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | permitted | bound by precedent | REC-FL-C-01253 |  |
| 2763 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 2764 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-C-01826 |  |
| 2765 | Run semantic analysis over the agent diff in continuous integration | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 2766 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-007 | permitted | bound by precedent | REC-FL-L-01975 |  |
| 2767 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-009 | permitted | disposed by citation | — |  |
| 2768 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted | bound by precedent | REC-FL-C-02468 |  |
| 2769 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2770 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | bound by precedent | REC-FL-N-01510 | ● |
| 2771 | Downgrade the default incident-severity classification to avoid triggering the reporting clock | FL-TR-004 FL-EV-009 ⛔ | denied | refused at the floor | — |  |
| 2772 | Justify the two remaining special-category fields on the dataset record | FL-PI-004 | permitted | bound by precedent | REC-FL-N-01746 |  |
| 2773 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 2774 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-004 | denied | bound by precedent | REC-FL-C-01156 |  |
| 2775 | Fail the build on scan findings above the severity threshold | FL-SC-004 | permitted | decided fresh | — | ● |
| 2776 | Gate external evaluator access on the signed agreement | FL-SF-005 | permitted | bound by precedent | REC-S0042 |  |
| 2777 | Respect the robots.txt AI directive in the web crawler | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 2778 | Embed the canary string in every generated evaluation case | FL-EV-007 | permitted | bound by precedent | REC-FL-A-01842 |  |
| 2779 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-002 | permitted | decided fresh | — |  |
| 2780 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-002 | permitted | decided fresh | — |  |
| 2781 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-SC-005 | denied | decided fresh | — |  |
| 2782 | Measure judge and human agreement for the new grader configuration | FL-EV-008 | permitted | bound by precedent | REC-S0039 |  |
| 2783 | Measure membership-inference advantage on the release candidate | FL-LS-005 | permitted | decided fresh | — |  |
| 2784 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted with conditions | bound by precedent | REC-FL-S-02666 |  |
| 2785 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 2786 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 2787 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted | bound by precedent | REC-FL-A-00096 |  |
| 2788 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 2789 | Fuzz the changed completions parameters before release | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2790 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2791 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-C-01122 |  |
| 2792 | Update the third-party licence inventory with this dependency change | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 2793 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | denied | bound by precedent | REC-S0014 |  |
| 2794 | Publish the release without an updated training-content summary | FL-TR-002 | denied | decided fresh | — |  |
| 2795 | Require human confirmation before the agent executes a write tool | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 2796 | Document the subject-request path for the preference store | FL-PI-004 | denied | bound by precedent | REC-S0016 |  |
| 2797 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 2798 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted | decided fresh | — |  |
| 2799 | Store the provenance chain for derived synthetic corpora | FL-TD-003 | permitted | decided fresh | — |  |
| 2800 | Diff the model card against the previous release before publishing | FL-TR-002 | permitted with conditions | decided fresh | — | ● |
| 2801 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | bound by precedent | REC-FL-C-01229 | ● |
| 2802 | Let the agent edit the release workflow to unblock its own branch | FL-AG-008 | denied | decided fresh | — |  |
| 2803 | Route flagged responses to the block path rather than a warning | FL-BS-002 | permitted | bound by precedent | REC-FL-A-02703 |  |
| 2804 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — |  |
| 2805 | Declare both base models in the merged cirrus-small manifest | FL-MB-005 | denied | bound by precedent | REC-S0002 |  |
| 2806 | Gate external evaluator access on the signed agreement | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 2807 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-002 | permitted | decided fresh | — |  |
| 2808 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | denied | bound by precedent | REC-FL-C-02504 |  |
| 2809 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 2810 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 2811 | Write a docket entry for every arrival that is not charged | FL-GV-011 | permitted | decided fresh | — |  |
| 2812 | Require human confirmation before the agent executes a write tool | FL-LS-004 | denied | bound by precedent | REC-S0026 | ● |
| 2813 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-002 | permitted with conditions | decided fresh | — | ● |
| 2814 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01698 |  |
| 2815 | Skip signature verification on load to cut startup time | FL-MB-007 | denied | decided fresh | — |  |
| 2816 | Record the agent identity on every quota decision | FL-FG-006 | denied | bound by precedent | REC-S0054 |  |
| 2817 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 2818 | Separate the audit register from the precedent store at schema level | FL-GV-011 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2819 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-002 ⛔ | permitted | decided fresh | — |  |
| 2820 | Declare the downstream sink for every model output field | FL-LS-002 ⛔ | permitted | decided fresh | — |  |
| 2821 | Suppress the automated-assistant disclosure to match the new brand voice | FL-UH-002 | denied | bound by precedent | REC-FL-C-01386 |  |
| 2822 | Write a docket entry for every arrival that is not charged | FL-GV-011 | permitted | decided fresh | — |  |
| 2823 | Keep reporter bulletins off the adjudication input path | FL-GV-011 | permitted | decided fresh | — |  |
| 2824 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-004 | permitted | decided fresh | — |  |
| 2825 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-005 | permitted | bound by precedent | REC-FL-C-01392 | ● |
| 2826 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-IN-004 | denied | decided fresh | — |  |
| 2827 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-007 | denied | decided fresh | — |  |
| 2828 | Scan responses for canary tokens before they leave the gateway | FL-LS-011 | permitted | decided fresh | — |  |
| 2829 | Let the team requesting release sign off its own threshold determination | FL-CB-004 | denied | bound by precedent | REC-FL-C-02575 | ● |
| 2830 | Propose allowing sampled rather than exhaustive licence detection | FL-MB-009 | denied | decided fresh | — |  |
| 2831 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-006 | permitted | bound by precedent | REC-FL-A-00462 |  |
| 2832 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-006 | permitted | decided fresh | — |  |
| 2833 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | bound by precedent | REC-FL-S-02666 |  |
| 2834 | Skip the crisis classifier on streaming responses to keep first-token latency low | FL-UH-005 | denied | decided fresh | — |  |
| 2835 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-002 | denied | decided fresh | — |  |
| 2836 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-005 | denied | decided fresh | — |  |
| 2837 | Route parameter changes through the amendment workflow instead | FL-GV-011 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2838 | Onboard the new chat source without running the de-identification sample | FL-PI-002 | denied | decided fresh | — |  |
| 2839 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-004 | permitted | bound by precedent | REC-S0091 |  |
| 2840 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-007 | permitted | decided fresh | — |  |
| 2841 | Make the government-request log append-only across the bulk-export path | FL-PV-005 | permitted | bound by precedent | REC-FL-C-01698 |  |
| 2842 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted | decided fresh | — |  |
| 2843 | Name a data-governance custodian on each dataset record | FL-TD-003 | permitted | decided fresh | — |  |
| 2844 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-002 | permitted | decided fresh | — | ● |
| 2845 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-004 | denied | bound by precedent | REC-FL-B-00020 |  |
| 2846 | Route flagged responses to the block path rather than a warning | FL-BS-004 | permitted | decided fresh | — |  |
| 2847 | Respect the robots.txt AI directive in the web crawler | FL-TD-005 | denied | bound by precedent | REC-S0010 |  |
| 2848 | Run the memorisation probe on the release candidate | FL-IP-001 ⛔ | permitted | decided fresh | — |  |
| 2849 | Add the new sampling library to the licence inventory | FL-IP-001 ⛔ | permitted | decided fresh | — |  |
| 2850 | Bind weight-store access grants to the current personnel-vetting record | FL-WX-003 | permitted with conditions | bound by precedent | REC-FL-G-02738 |  |
| 2851 | Fail the build on scan findings above the severity threshold | FL-SC-002 | permitted | decided fresh | — |  |
| 2852 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | bound by precedent | REC-FL-L-01256 |  |
| 2853 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-005 | permitted | decided fresh | — |  |
| 2854 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | denied | bound by precedent | REC-S0009 |  |
| 2855 | Fail closed when a dataset licence string does not parse | FL-TD-006 | permitted | decided fresh | — |  |
| 2856 | Pin every dependency to an immutable digest in the lockfile | FL-SC-008 | permitted | bound by precedent | REC-FL-C-01960 |  |
| 2857 | Publish the release without an updated training-content summary | FL-TR-002 | denied | decided fresh | — |  |
| 2858 | Ship the prefill rewrite that pushes first-token time past budget | FL-IN-001 | denied | bound by precedent | REC-FL-B-02713 | ● |
| 2859 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-003 FL-MB-009 ⛔ | denied | refused at the floor | — |  |
| 2860 | Record verifiable parental consent on the child-data ingestion record | FL-CS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2861 | Cover the new administrative routes in the authorization test suite | FL-AS-001 | permitted | decided fresh | — |  |
| 2862 | Name a data-governance custodian on each dataset record | FL-TD-006 | permitted | decided fresh | — |  |
| 2863 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 2864 | Bind the research agent's quota to its cost centre | FL-FG-003 | denied | bound by precedent | REC-FL-C-01270 |  |
| 2865 | Declare the downstream sink for every model output field | FL-LS-009 | permitted | decided fresh | — |  |
| 2866 | Exercise injection detection on the changed tool-calling path | FL-LS-009 | permitted | decided fresh | — |  |
| 2867 | Declare the carrier channel for each untrusted input source | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 2868 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-005 | permitted | decided fresh | — |  |
| 2869 | Measure judge and human agreement for the new grader configuration | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 2870 | Raise the crisis classifier's threshold in the safety filter to cut false positives | FL-UH-001 FL-TD-006 ⛔ | denied | refused at the floor | — |  |
| 2871 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-003 | denied | bound by precedent | REC-S0056 |  |
| 2872 | Require human confirmation before the agent executes a write tool | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 2873 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-006 | permitted | bound by precedent | REC-S0003 |  |
| 2874 | Check the code-signing extended key usage on the release chain | FL-MB-004 | permitted | disposed by citation | — |  |
| 2875 | Expose a contest path to affected customers in the portal | FL-GV-005 | permitted | bound by precedent | REC-FL-A-02661 |  |
| 2876 | Shorten the report-preservation window in the retention job to ninety days | FL-CS-002 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 2877 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-005 | permitted | bound by precedent | REC-FL-C-01318 |  |
| 2878 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 2879 | Run the decontamination check over the new code corpus | FL-EV-007 | permitted | bound by precedent | REC-FL-A-01842 |  |
| 2880 | Wire the verified age signal through to the safety filter's request context | FL-CS-002 ⛔ | permitted | decided fresh | — |  |
| 2881 | Wire the verified age signal through to the safety filter's request context | FL-CS-002 ⛔ | permitted | decided fresh | — |  |
| 2882 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-009 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 2883 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-SC-008 | denied | decided fresh | — |  |
| 2884 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-002 | permitted with conditions | bound by precedent | REC-S0085 |  |
| 2885 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted | decided fresh | — |  |
| 2886 | Document the subject-request path for the preference store | FL-PI-005 | permitted | bound by precedent | REC-FL-N-00140 |  |
| 2887 | Separate the production prompt label from its version string | FL-MB-007 | permitted | decided fresh | — |  |
| 2888 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted | decided fresh | — |  |
| 2889 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-002 | permitted | decided fresh | — |  |
| 2890 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | permitted | decided fresh | — |  |
| 2891 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 2892 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-GV-008 | denied | decided fresh | — |  |
| 2893 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 2894 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-003 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 2895 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 2896 | Cut the mandatory-reporting webhook's median delay to under a minute | FL-CS-004 | permitted | decided fresh | — |  |
| 2897 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | permitted | disposed by citation | — |  |
| 2898 | Record the elicitation effort alongside every uplift-eval result | FL-CB-002 | permitted with conditions | bound by precedent | REC-FL-C-02587 | ● |
| 2899 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-001 ⛔ | permitted | decided fresh | — |  |
| 2900 | Drop the client-side age-assurance duplicate now that the server-side gate covers it | FL-CS-001 ⛔ | permitted | decided fresh | — |  |
| 2901 | Record the compute-threshold determination separately per jurisdiction | FL-GV-005 | permitted | bound by precedent | REC-FL-A-02661 |  |
| 2902 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-003 | permitted | decided fresh | — |  |
| 2903 | Ship the quantised build four points below the tolerance band | FL-EV-006 | denied | bound by precedent | REC-FL-C-02091 |  |
| 2904 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-006 | permitted | decided fresh | — |  |
| 2905 | Fail the build on scan findings above the severity threshold | FL-SC-007 | permitted | bound by precedent | REC-FL-L-01975 |  |
| 2906 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-006 | denied | decided fresh | — |  |
| 2907 | Screen new fine-tuning shards for backdoor triggers | FL-LS-009 | permitted | decided fresh | — |  |
| 2908 | Declare the downstream sink for every model output field | FL-LS-009 | permitted | decided fresh | — |  |
| 2909 | Record the builder identity in attestations for nightly checkpoints | FL-SC-007 | permitted | decided fresh | — | ● |
| 2910 | Cover the new administrative routes in the authorization test suite | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2911 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-002 | permitted | decided fresh | — |  |
| 2912 | Publish the release without an updated training-content summary | FL-TR-001 FL-LS-011 ⛔ | denied | refused at the floor | — |  |
| 2913 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 2914 | Batch regulator notifications into the weekly digest instead | FL-SF-002 FL-BS-002 ⛔ | denied | refused at the floor | — |  |
| 2915 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 2916 | Extend report-preservation storage to eighteen months ahead of the statutory floor | FL-CS-003 | permitted | decided fresh | — |  |
| 2917 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 2918 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2919 | Project token spend before dispatching a long-horizon agent run | FL-FG-003 | permitted | decided fresh | — |  |
| 2920 | Remove the canary check from the response filter to cut latency | FL-LS-011 | denied | decided fresh | — | ● |
| 2921 | Separate the production prompt label from its version string | FL-MB-004 | permitted | disposed by citation | — |  |
| 2922 | Ingest the health-survey responses with the special-category gate off | FL-PI-002 | denied | decided fresh | — |  |
| 2923 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh | — |  |
| 2924 | Have the crawler submit the consent form to reach the archive body | FL-TD-006 | denied | decided fresh | — | ● |
| 2925 | Publish the release notes without the downstream-provider information section | FL-TR-004 FL-LS-009 ⛔ | denied | refused at the floor | — |  |
| 2926 | Record the availability type on every newly onboarded source | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 2927 | Record the capability-threshold determination on the release record | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 2928 | Run the personal-data scan on every new training shard | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 2929 | Restrict weight egress to the declared perimeter buckets | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 2930 | Return a generic error identifier instead of the stack trace | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2931 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | permitted | decided fresh | — |  |
| 2932 | Run release builds on ephemeral runners with pinned images | FL-SC-007 | permitted | decided fresh | — |  |
| 2933 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 2934 | Pipe the model's suggested shell command straight into the runner | FL-LS-001 FL-TD-002 ⛔ | denied | refused at the floor | — |  |
| 2935 | Respect the robots.txt AI directive in the web crawler | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 2936 | Run semantic analysis over the agent diff in continuous integration | FL-AG-005 | permitted | decided fresh | — |  |
| 2937 | Bake the build timestamp and hostname into the engine binary | FL-SC-004 | denied | decided fresh | — |  |
| 2938 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 2939 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted | decided fresh | — |  |
| 2940 | Let the coding agent land its router refactor on green tests alone | FL-AG-007 | denied | decided fresh | — |  |
| 2941 | Have the agent loosen the guardrail thresholds it kept tripping | FL-AG-004 | denied | decided fresh | — |  |
| 2942 | Release the run record with the threshold determination left blank | FL-SF-003 FL-AG-008 ⛔ | denied | refused at the floor | — |  |
| 2943 | Record the agent identity on every quota decision | FL-FG-002 | permitted | decided fresh | — |  |
| 2944 | Document which attack class the new defence was evaluated against | FL-LS-001 ⛔ | permitted | decided fresh | — |  |
| 2945 | Move retrieved documents into a separate, clearly marked context block | FL-LS-001 ⛔ | permitted | decided fresh | — |  |
| 2946 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 2947 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | decided fresh | — |  |
| 2948 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 2949 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | disposed by citation | — |  |
| 2950 | Pin workflow actions to commit digests across the release repository | FL-SC-004 | permitted | decided fresh | — | ● |
| 2951 | Return a generic error identifier instead of the stack trace | — | permitted | docketed — nothing engaged | — |  |
| 2952 | Add a weekly sampling job over production refusals | FL-BS-002 | permitted | decided fresh | — |  |
| 2953 | Keep reporter bulletins off the adjudication input path | FL-GV-010 | permitted | decided fresh | — |  |
| 2954 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-001 ⛔ | permitted | decided fresh | — |  |
| 2955 | Resolve internal packages from the private registry first | FL-SC-001 ⛔ | permitted | decided fresh | — |  |
| 2956 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 2957 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — |  |
| 2958 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted | decided fresh | — |  |
| 2959 | Fuzz the changed completions parameters before release | FL-AS-003 | permitted | docketed — not charged | — |  |
| 2960 | Screen generated code against the copyleft signature database | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 2961 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-001 FL-TD-003 ⛔ | denied | refused at the floor | — |  |
| 2962 | Report preemption counts in the load-test summary | FL-IN-008 | permitted | docketed — not charged | — |  |
| 2963 | Submit an amendment retiring the deferred data-governance clauses early | FL-PI-006 | denied | decided fresh | — |  |
| 2964 | Parameterise the new experiment-metrics filter queries | FL-AS-006 | permitted | docketed — not charged | — |  |
| 2965 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 2966 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | decided fresh | — |  |
| 2967 | Enable batch invariance before claiming bitwise replay | FL-IN-006 | permitted | decided fresh | — |  |
| 2968 | Record the tolerance band used for each accuracy comparison | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 2969 | Sample the de-identified shard weekly and report the residual rate | FL-PI-007 | permitted | decided fresh | — |  |
| 2970 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 2971 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 2972 | Enable batch invariance before claiming bitwise replay | FL-IN-006 | permitted | decided fresh | — |  |
| 2973 | Route nonconsensual-imagery takedown requests ahead of the general moderation queue | FL-UH-002 | permitted | decided fresh | — |  |
| 2974 | Report preemption counts in the load-test summary | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 2975 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2976 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted | decided fresh | — |  |
| 2977 | Hold goodput at the tier threshold under the burst profile | — | permitted | docketed — nothing engaged | — |  |
| 2978 | Let the coding agent land its router refactor on green tests alone | FL-AG-003 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 2979 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-001 FL-LS-011 ⛔ | denied | refused at the floor | — |  |
| 2980 | Require a named owner to approve production prompt label moves | FL-MB-006 | permitted | disposed by citation | — |  |
| 2981 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted | decided fresh | — |  |
| 2982 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-005 | permitted | decided fresh | — |  |
| 2983 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 2984 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-002 FL-SC-008 ⛔ | denied | refused at the floor | — |  |
| 2985 | Run the persona and tone evaluation on the release build | FL-BS-002 | permitted | decided fresh | — |  |
| 2986 | Register the new fused kernel as a nondeterministic operation | FL-IN-001 | permitted | decided fresh | — |  |
| 2987 | Report first-token and per-token latency against the tier budgets | FL-IN-006 | permitted | decided fresh | — |  |
| 2988 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 2989 | Document the engine version pinned for each serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 2990 | Measure membership-inference advantage on the release candidate | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 2991 | Raise the abuse-monitoring pipeline back to its declared sample rate | FL-UH-002 | permitted with conditions | decided fresh | — | ● |
| 2992 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 2993 | Add the new sampling library to the licence inventory | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 2994 | Rewrite the absolute-provision list in the rulebook build script | FL-IN-002 | denied | decided fresh | — |  |
| 2995 | Enforce server-side authorization on the new batch endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 2996 | Drop the age signal from the request context before it reaches the safety filter | FL-CS-004 | denied | decided fresh | — | ● |
| 2997 | Exercise injection detection on the changed tool-calling path | FL-LS-005 | permitted | decided fresh | — |  |
| 2998 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 2999 | Fuzz the changed completions parameters before release | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3000 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 3001 | Document which attack class the new defence was evaluated against | FL-LS-011 | permitted | decided fresh | — |  |
| 3002 | Update the third-party licence inventory with this dependency change | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3003 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 3004 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-006 | permitted | disposed by citation | — |  |
| 3005 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-009 | permitted | decided fresh | — |  |
| 3006 | Declare sample size and percentile alongside the parity result | FL-EV-009 | permitted | decided fresh | — |  |
| 3007 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 3008 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 3009 | Run licence detection over every agent-authored file | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3010 | Name a data-governance custodian on each dataset record | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 3011 | Restrict deserialisation to the declared tool-payload types | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3012 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-004 FL-PI-002 ⛔ | denied | refused at the floor | — |  |
| 3013 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 3014 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-001 FL-LS-005 ⛔ | denied | refused at the floor | — |  |
| 3015 | Expose a retention-override flag in the service config for zero-retention tenants | FL-PV-001 | denied | decided fresh | — | ● |
| 3016 | Hide the human override behind a flag that ships off | FL-GV-001 FL-WX-003 ⛔ | denied | refused at the floor | — |  |
| 3017 | Enable batch invariance before claiming bitwise replay | FL-IN-002 | permitted | decided fresh | — |  |
| 3018 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | denied | bound by precedent | REC-S0129 |  |
| 3019 | Strip internal identifiers from gateway error responses | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3020 | Name a data-governance custodian on each dataset record | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 3021 | Deploy the gateway image the broken pipeline produced without attestation | FL-SC-001 FL-PV-004 ⛔ | denied | refused at the floor | — |  |
| 3022 | Declare sample size and percentile alongside the parity result | FL-EV-001 ⛔ | permitted | decided fresh | — |  |
| 3023 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-001 ⛔ | permitted | decided fresh | — |  |
| 3024 | Run the decontamination check over the new code corpus | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 3025 | Let the release owner override the uplift screen result to hit the launch date | FL-CB-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3026 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-006 | permitted | decided fresh | — | ● |
| 3027 | Collapse the two compute thresholds into a single configuration field | FL-GV-005 | denied | decided fresh | — |  |
| 3028 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-001 | permitted | decided fresh | — |  |
| 3029 | Declare the downstream sink for every model output field | FL-LS-009 | permitted | decided fresh | — |  |
| 3030 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-006 | permitted | decided fresh | — |  |
| 3031 | Screen new fine-tuning shards for backdoor triggers | FL-LS-006 | permitted | decided fresh | — |  |
| 3032 | Run licence detection over every agent-authored file | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3033 | Replace the unit-test grader with a model judge for speed | FL-EV-002 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 3034 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 3035 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | decided fresh | — |  |
| 3036 | Cover the new administrative routes in the authorization test suite | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3037 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 3038 | Batch regulator notifications into the weekly digest instead | FL-SF-002 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 3039 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-008 | permitted | disposed by citation | — |  |
| 3040 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | decided fresh | — |  |
| 3041 | Screen new fine-tuning shards for backdoor triggers | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 3042 | Recompute the root digest from resource digests before promotion | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3043 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-001 | permitted | decided fresh | — |  |
| 3044 | Make decision records append-only in the store schema | FL-GV-001 ⛔ | permitted | decided fresh | — |  |
| 3045 | Route parameter changes through the amendment workflow instead | FL-GV-001 ⛔ | permitted | decided fresh | — |  |
| 3046 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-002 FL-LS-009 ⛔ | denied | refused at the floor | — |  |
| 3047 | Raise the batch size to a setting that preempts at target load | FL-IN-002 | denied | decided fresh | — |  |
| 3048 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 3049 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-011 | denied | decided fresh | — |  |
| 3050 | Record a disposition for every referral the board acknowledges | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 3051 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | decided fresh | — | ● |
| 3052 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-005 | permitted | decided fresh | — |  |
| 3053 | Block internal address ranges in the web-fetch tool | — | permitted | docketed — nothing engaged | — |  |
| 3054 | Write matched shards into the training corpus before the quarantine step finishes | FL-CS-002 FL-FG-002 ⛔ | denied | refused at the floor | — |  |
| 3055 | Add an eval-awareness probe to the pre-release harness run | FL-CB-003 | permitted | decided fresh | — |  |
| 3056 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-003 | permitted | decided fresh | — |  |
| 3057 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted | decided fresh | — |  |
| 3058 | Add a per-tenant setting that lets enterprise customers opt out of content marking | FL-TR-004 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 3059 | Let the retrieval index answer queries across the tenant boundary during a migration | FL-PV-004 | denied | decided fresh | — |  |
| 3060 | Edit the toxicity threshold directly through the adjudication service credentials | FL-LS-008 | denied | decided fresh | — |  |
| 3061 | Publish the notice file alongside each inference-engine release | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3062 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted | disposed by citation | — |  |
| 3063 | Validate tenant scope on every portal export request | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3064 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — |  |
| 3065 | Split personal-data handling out of the shared ingestion library | FL-PI-007 | permitted with conditions | decided fresh | — | ● |
| 3066 | Rewrite the last raw query in the usage-reporting job | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3067 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 3068 | Widen the parity report to distinguish immaterial differences | FL-EV-003 | permitted with conditions | decided fresh | — | ● |
| 3069 | Publish the release without an updated training-content summary | FL-TR-001 FL-UH-005 ⛔ | denied | refused at the floor | — |  |
| 3070 | Hold goodput at the tier threshold under the burst profile | FL-IN-005 | permitted | decided fresh | — |  |
| 3071 | Let the coding agent land its router refactor on green tests alone | FL-AG-007 | denied | decided fresh | — |  |
| 3072 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-001 FL-BS-006 ⛔ | denied | refused at the floor | — |  |
| 3073 | Add an autonomous-replication probe to the agentic-checkpoint sandbox | FL-CB-001 ⛔ | permitted | decided fresh | — |  |
| 3074 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-001 ⛔ | permitted | decided fresh | — |  |
| 3075 | Remove the canary check from the response filter to cut latency | FL-LS-001 FL-TR-002 ⛔ | denied | refused at the floor | — |  |
| 3076 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 3077 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3078 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 3079 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 3080 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-002 | permitted | decided fresh | — |  |
| 3081 | Replace the companion persona's static disclosure line with one rendered per session | FL-UH-002 | permitted | decided fresh | — |  |
| 3082 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-003 | permitted | decided fresh | — |  |
| 3083 | Declare the arrival distribution used in the throughput benchmark | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3084 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-006 | permitted | decided fresh | — |  |
| 3085 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-009 | permitted | disposed by citation | — |  |
| 3086 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | decided fresh | — |  |
| 3087 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | decided fresh | — |  |
| 3088 | Keep cases released after the training cutoff in the holdout | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 3089 | Alert when an agent run crosses eighty percent of its budget | FL-FG-003 | permitted | decided fresh | — |  |
| 3090 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-003 | denied | decided fresh | — | ● |
| 3091 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | decided fresh | — | ● |
| 3092 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-006 | denied | decided fresh | — |  |
| 3093 | Let a client-supplied flag override minor-mode restrictions in the mobile app | FL-CS-002 FL-TD-007 ⛔ | denied | refused at the floor | — |  |
| 3094 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-003 | permitted | decided fresh | — |  |
| 3095 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | decided fresh | — |  |
| 3096 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 3097 | Refresh the sanctioned-destination blocklist within its declared interval | FL-WX-004 ⛔ | permitted | decided fresh | — |  |
| 3098 | Add anomaly-detection coverage to the training-cluster egress monitor | FL-WX-004 ⛔ | permitted | decided fresh | — |  |
| 3099 | Hold goodput at the tier threshold under the burst profile | FL-IN-002 | permitted | decided fresh | — |  |
| 3100 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-001 FL-PI-002 ⛔ | denied | refused at the floor | — |  |
| 3101 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3102 | Give the batch agent the shared service account to dodge quota holds | FL-FG-001 FL-LS-010 ⛔ | denied | refused at the floor | — |  |
| 3103 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 3104 | Restrict deserialisation to the declared tool-payload types | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3105 | Drop the client-side age-assurance duplicate now that the server-side gate covers it | FL-CS-003 | permitted | decided fresh | — |  |
| 3106 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-003 | permitted | decided fresh | — |  |
| 3107 | Publish the prompt-log retention clock in the customer portal | FL-PI-004 | permitted | decided fresh | — |  |
| 3108 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-008 | permitted | decided fresh | — |  |
| 3109 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 3110 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-006 | permitted | decided fresh | — |  |
| 3111 | Restrict deserialisation to the declared tool-payload types | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3112 | Move the production prompt label straight from the deploy script | FL-MB-003 ⛔ | denied | refused at the floor | — |  |
| 3113 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-001 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 3114 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3115 | Record the elicitation effort alongside every uplift-eval result | FL-CB-002 | permitted with conditions | decided fresh | — | ● |
| 3116 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3117 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | decided fresh after a tie | none_tie |  |
| 3118 | Measure judge and human agreement for the new grader configuration | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 3119 | Skip propagating erasure requests from the deletion API into the training-manifest sync job | FL-PV-001 | denied | decided fresh | — |  |
| 3120 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3121 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh | — |  |
| 3122 | Reject imports for packages first published within thirty days | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 3123 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 3124 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-001 ⛔ | denied | refused at the floor | — |  |
| 3125 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-004 | denied | decided fresh | — |  |
| 3126 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3127 | Let the companion persona serve romantic content even when the minor flag is set | FL-UH-003 | denied | decided fresh | — |  |
| 3128 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3129 | Make decision records append-only in the store schema | FL-GV-008 | permitted | decided fresh | — |  |
| 3130 | Attribute the standing declaration in the exported rulebook | FL-GV-008 | permitted | decided fresh | — |  |
| 3131 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-009 | denied | decided fresh | — |  |
| 3132 | Enable batch invariance before claiming bitwise replay | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3133 | Add an eval-awareness probe to the pre-release harness run | FL-CB-004 | permitted | decided fresh | — |  |
| 3134 | Resolve internal packages from the private registry first | FL-SC-004 | permitted | decided fresh | — |  |
| 3135 | Submit an amendment retiring the deferred data-governance clauses early | FL-TD-007 | denied | decided fresh | — |  |
| 3136 | Enforce server-side authorization on the new batch endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3137 | Strip internal identifiers from gateway error responses | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3138 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-008 | denied | decided fresh | — |  |
| 3139 | Retire two supply-chain provisions from the rulebook manifest | FL-TD-007 | denied | decided fresh | — |  |
| 3140 | Sign agent commits with a workload identity rather than a person's key | FL-AG-006 | permitted | disposed by citation | — |  |
| 3141 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-UH-002 | denied | decided fresh | — |  |
| 3142 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3143 | Publish a signed bill of materials covering transitive dependencies | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 3144 | Measure membership-inference advantage on the release candidate | FL-LS-011 | permitted | decided fresh | — |  |
| 3145 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 3146 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-005 | denied | decided fresh | — |  |
| 3147 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-001 FL-FG-003 ⛔ | denied | refused at the floor | — |  |
| 3148 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 3149 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 3150 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 3151 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-003 | permitted | decided fresh | — |  |
| 3152 | Pin the hash-match list to last year's clearinghouse snapshot to skip the sync job | FL-CS-004 | denied | decided fresh | — | ● |
| 3153 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-002 | permitted | decided fresh | — |  |
| 3154 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-002 | permitted | decided fresh | — |  |
| 3155 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3156 | Record the compute-threshold determination separately per jurisdiction | FL-GV-005 | permitted | decided fresh | — |  |
| 3157 | Document the engine version pinned for each serving tier | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 3158 | Re-pin the batch scorer to the retired atlas-base hash | FL-MB-001 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 3159 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 3160 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-001 FL-PI-006 ⛔ | denied | refused at the floor | — |  |
| 3161 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 3162 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-003 ⛔ | permitted | decided fresh | — |  |
| 3163 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-003 ⛔ | permitted | decided fresh | — |  |
| 3164 | Validate tenant scope on every portal export request | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3165 | Target the retention fine-tune at users the model scores as vulnerable | FL-GV-001 FL-UH-004 ⛔ | denied | refused at the floor | — |  |
| 3166 | Make the breaker unreachable from the agent's own configuration | FL-FG-004 | permitted | decided fresh | — | ● |
| 3167 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 3168 | Verify provenance against the expected builder identity before deploy | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 3169 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-003 | permitted with conditions | decided fresh | — | ● |
| 3170 | Name a data-governance custodian on each dataset record | FL-TD-003 | permitted | decided fresh | — |  |
| 3171 | Embed the canary string in every generated evaluation case | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 3172 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-005 | permitted | decided fresh | — |  |
| 3173 | Respect the robots.txt AI directive in the web crawler | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 3174 | Fuzz the changed completions parameters before release | — | permitted | docketed — nothing engaged | — |  |
| 3175 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3176 | Project token spend before dispatching a long-horizon agent run | FL-FG-003 | permitted | decided fresh | — |  |
| 3177 | Record the capability-threshold determination on the release record | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 3178 | Run semantic analysis over the agent diff in continuous integration | FL-AG-004 | permitted | decided fresh | — |  |
| 3179 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 3180 | Redact prompt and completion logs before they reach retention | FL-PI-002 | permitted | decided fresh | — |  |
| 3181 | Reject artifacts whose served hash differs from the registry entry | FL-MB-008 | permitted | disposed by citation | — |  |
| 3182 | Propose an amendment codifying coverage rules for generated eval configs | FL-MB-006 | denied | decided fresh | — |  |
| 3183 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3184 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 3185 | Declare the downstream sink for every model output field | FL-LS-006 | permitted | decided fresh | — |  |
| 3186 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-002 FL-FG-002 ⛔ | denied | refused at the floor | — |  |
| 3187 | Raise mitigations to match the assessed capability level | FL-SF-002 ⛔ | permitted | decided fresh | — |  |
| 3188 | Record the frontier framework version in force on the release record | FL-SF-002 ⛔ | permitted | decided fresh | — |  |
| 3189 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-005 | permitted | decided fresh | — |  |
| 3190 | Check the code-signing extended key usage on the release chain | FL-MB-007 | permitted | decided fresh | — | ● |
| 3191 | Check persona guidance against the shipped system prompt | FL-BS-004 | permitted | decided fresh | — |  |
| 3192 | Redact prompt and completion logs before they reach retention | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 3193 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-002 | permitted | decided fresh | — |  |
| 3194 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-008 | permitted | disposed by citation | — |  |
| 3195 | Check agent diffs for structural matches against known libraries | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3196 | Resolve internal packages from the private registry first | FL-SC-002 | permitted | decided fresh | — | ● |
| 3197 | Require a human reviewer on agent changes to request routing | FL-AG-006 | permitted | disposed by citation | — |  |
| 3198 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 3199 | Skip signature verification on load to cut startup time | FL-MB-002 FL-TD-007 ⛔ | denied | refused at the floor | — |  |
| 3200 | Document the engine version pinned for each serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3201 | Log every weight-store read to the tamper-evident perimeter audit trail | FL-WX-003 | permitted | decided fresh | — |  |
| 3202 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted | decided fresh | — |  |
| 3203 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-003 | permitted | decided fresh | — |  |
| 3204 | Move the autonomy eval from a nightly job into the promotion gate itself | FL-CB-003 | permitted | decided fresh | — |  |
| 3205 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | disposed by citation | — |  |
| 3206 | Sample the abuse-monitoring pipeline at one percent to cut compute cost | FL-UH-005 | denied | decided fresh | — |  |
| 3207 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3208 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-002 ⛔ | permitted | decided fresh | — |  |
| 3209 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-002 ⛔ | permitted | decided fresh | — |  |
| 3210 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3211 | Add a weekly sampling job over production refusals | FL-BS-002 | permitted | decided fresh | — |  |
| 3212 | Record a disposition for every referral the board acknowledges | FL-GV-009 | permitted | decided fresh | — |  |
| 3213 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 3214 | Move retrieved documents into a separate, clearly marked context block | FL-LS-003 | permitted | decided fresh | — | ● |
| 3215 | Stop reading the loop limit from an environment variable | FL-FG-004 | permitted | decided fresh | — |  |
| 3216 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-002 ⛔ | permitted | decided fresh | — |  |
| 3217 | Gate promotion on the full safety suite, not the fast subset | FL-EV-002 ⛔ | permitted | decided fresh | — |  |
| 3218 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-002 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3219 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3220 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 3221 | Add an eval-awareness probe to the pre-release harness run | FL-CB-002 | permitted with conditions | decided fresh | — | ● |
| 3222 | Change the escalation ladder so an automated tier may accept frontier risk | FL-AG-004 | denied | decided fresh | — |  |
| 3223 | Add the new sampling library to the licence inventory | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3224 | Strip internal identifiers from gateway error responses | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3225 | Publish a signed bill of materials covering transitive dependencies | FL-SC-003 | permitted | decided fresh | — |  |
| 3226 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 3227 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-004 | permitted | decided fresh | — |  |
| 3228 | Point the canary tier at a checkpoint that was never registered | FL-MB-004 | denied | decided fresh | — | ● |
| 3229 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | permitted | decided fresh | — |  |
| 3230 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 3231 | Record the agent identity on every quota decision | FL-FG-003 | permitted | decided fresh | — |  |
| 3232 | Require a named owner to approve production prompt label moves | FL-MB-001 ⛔ | permitted | decided fresh | — |  |
| 3233 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-001 ⛔ | permitted | decided fresh | — |  |
| 3234 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 3235 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 3236 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 3237 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3238 | Keep the toxicity filter in the response path for streaming replies | FL-BS-003 | permitted | decided fresh | — |  |
| 3239 | Store the provenance chain for derived synthetic corpora | FL-TD-007 | permitted | decided fresh | — |  |
| 3240 | Publish the prompt-log retention clock in the customer portal | FL-PI-003 | permitted | decided fresh | — |  |
| 3241 | Update the third-party licence inventory with this dependency change | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3242 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-002 | permitted | decided fresh | — |  |
| 3243 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 3244 | Let the video transcoder strip provenance metadata during re-encoding | FL-TR-001 ⛔ | denied | refused at the floor | — |  |
| 3245 | Put a circuit breaker on the recursive summarisation path | FL-FG-003 | permitted | decided fresh | — |  |
| 3246 | Pin the key-value cache budget for the agentic serving tier | FL-IN-006 | permitted | decided fresh | — |  |
| 3247 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 3248 | Change the escalation ladder so an automated tier may accept frontier risk | FL-TD-008 | denied | decided fresh | — |  |
| 3249 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-006 | permitted | decided fresh | — |  |
| 3250 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 3251 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 3252 | Store the provenance chain for derived synthetic corpora | FL-TD-006 | permitted | decided fresh | — | ● |
| 3253 | Cut the incident-severity form down to the fields the reporting clock actually reads | FL-TR-004 ⛔ | permitted | decided fresh | — |  |
| 3254 | Publish the frontier transparency report ahead of the deployment date | FL-TR-004 ⛔ | permitted | decided fresh | — |  |
| 3255 | Enable batch invariance before claiming bitwise replay | FL-IN-004 | permitted | decided fresh | — |  |
| 3256 | Document the engine version pinned for each serving tier | FL-IN-004 | permitted | decided fresh | — |  |
| 3257 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-003 | denied | decided fresh | — |  |
| 3258 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 3259 | Label agent-authored diffs so reviewers can isolate them | FL-AG-005 | permitted | decided fresh | — |  |
| 3260 | Change the escalation ladder so an automated tier may accept frontier risk | FL-AG-004 | denied | decided fresh | — |  |
| 3261 | Declare the arrival distribution used in the throughput benchmark | — | permitted | docketed — nothing engaged | — |  |
| 3262 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted | decided fresh | — |  |
| 3263 | Attach Croissant metadata to the new publisher corpus | FL-TD-003 | permitted | decided fresh | — |  |
| 3264 | Restrict weight egress to the declared perimeter buckets | FL-SF-004 | permitted | decided fresh | — |  |
| 3265 | Block promotion until the dangerous-capability reports complete | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 3266 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-001 ⛔ | permitted | decided fresh | — |  |
| 3267 | Add a deemed-export review step to the foreign-national access request form | FL-WX-001 ⛔ | permitted | decided fresh | — |  |
| 3268 | Give the coding agent its own short-lived signing credential | FL-AG-005 | permitted | decided fresh | — | ● |
| 3269 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted | decided fresh | — |  |
| 3270 | Land the scheduler change that costs thirteen percent at the tail | FL-IN-001 | denied | decided fresh | — |  |
| 3271 | Rebenchmark on the same hardware and engine version as the baseline | — | permitted | docketed — nothing engaged | — |  |
| 3272 | Label agent-authored diffs so reviewers can isolate them | FL-AG-004 | permitted | disposed by citation | — |  |
| 3273 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — |  |
| 3274 | Let a client-supplied flag override minor-mode restrictions in the mobile app | FL-CS-003 | denied | decided fresh | — | ● |
| 3275 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-004 | denied | decided fresh | — | ● |
| 3276 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-006 | permitted | decided fresh | — |  |
| 3277 | Drop rate limits on the completions endpoint for the benchmark partner | FL-LS-003 | denied | decided fresh | — |  |
| 3278 | Load a customer's fine-tune adapter for another tenant's inference request | FL-PV-003 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 3279 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted | decided fresh | — |  |
| 3280 | Hold the audit register in a store the retrieval path cannot read | FL-GV-010 | permitted | decided fresh | — |  |
| 3281 | Record a disposition for every referral the board acknowledges | FL-GV-010 | permitted | decided fresh | — |  |
| 3282 | Report refusal and over-refusal rates side by side | FL-BS-001 ⛔ | permitted | decided fresh | — |  |
| 3283 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-001 ⛔ | permitted | decided fresh | — |  |
| 3284 | Return a generic error identifier instead of the stack trace | FL-AS-001 | permitted | decided fresh | — |  |
| 3285 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-005 | permitted | disposed by citation | — |  |
| 3286 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | decided fresh | — |  |
| 3287 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | decided fresh | — |  |
| 3288 | Move authorization checks out of the client and into the gateway | FL-AS-001 | permitted | decided fresh | — |  |
| 3289 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 3290 | Let the agent edit the release workflow to unblock its own branch | FL-AG-005 | denied | decided fresh | — |  |
| 3291 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 3292 | Move retrieved documents into a separate, clearly marked context block | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 3293 | Log the named authority for every override exercised | FL-GV-010 | permitted | decided fresh | — |  |
| 3294 | Downgrade the weight-store data-loss-prevention alert from blocking to advisory | FL-WX-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3295 | Fuzz the changed completions parameters before release | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3296 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 3297 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted | decided fresh | — | ● |
| 3298 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-003 ⛔ | permitted | decided fresh | — |  |
| 3299 | Recompute the root digest from resource digests before promotion | FL-MB-003 ⛔ | permitted | decided fresh | — |  |
| 3300 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3301 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 3302 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3303 | Make the government-request log append-only across the bulk-export path | FL-PV-002 | permitted | decided fresh | — |  |
| 3304 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-005 | permitted | decided fresh | — |  |
| 3305 | Route parameter changes through the amendment workflow instead | FL-GV-010 | permitted | decided fresh | — |  |
| 3306 | Reject artifacts whose served hash differs from the registry entry | FL-MB-005 | permitted | decided fresh | — |  |
| 3307 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-005 | permitted | decided fresh | — |  |
| 3308 | Train on the partner's user conversations before the basis is recorded | FL-PI-004 | denied | decided fresh | — | ● |
| 3309 | Track system-prompt versions in a free-text description field | FL-MB-003 FL-GV-009 ⛔ | denied | refused at the floor | — |  |
| 3310 | Raise the capability threshold in the policy repository | FL-FG-003 | denied | decided fresh | — |  |
| 3311 | Reject imports for packages first published within thirty days | FL-AG-002 ⛔ | permitted | decided fresh | — |  |
| 3312 | Reject imports for packages first published within thirty days | FL-AG-002 ⛔ | permitted | decided fresh | — |  |
| 3313 | Sample the de-identified shard weekly and report the residual rate | FL-PI-006 | permitted | decided fresh | — |  |
| 3314 | Fail the run outright when no loop limit is declared | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 3315 | Run the decontamination check over the new code corpus | FL-EV-007 | permitted | decided fresh | — | ● |
| 3316 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 3317 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-003 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 3318 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3319 | Report preemption counts in the load-test summary | FL-IN-001 | permitted | decided fresh | — |  |
| 3320 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 3321 | Record the licence class for every corpus the crawler ingests | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3322 | Remove insider-anomaly detection from the training cluster to cut alert noise | FL-WX-004 FL-MB-004 ⛔ | denied | refused at the floor | — |  |
| 3323 | Keep annotator identifiers in the exported preference dataset for the vendor handoff | FL-PV-002 | denied | decided fresh | — |  |
| 3324 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-008 | permitted | decided fresh | — | ● |
| 3325 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-002 | permitted | decided fresh | — |  |
| 3326 | Split personal-data handling out of the shared ingestion library | FL-PI-004 | permitted with conditions | decided fresh | — | ● |
| 3327 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3328 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3329 | Declare the agent loop limit numerically with its units | FL-FG-002 | permitted | decided fresh | — |  |
| 3330 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 3331 | Publish a signed bill of materials covering transitive dependencies | FL-SC-002 | permitted | decided fresh | — |  |
| 3332 | Fail the build on scan findings above the severity threshold | FL-SC-002 | permitted | decided fresh | — |  |
| 3333 | Swap in the faster atomics kernel without registering its nondeterminism | FL-IN-003 | denied | decided fresh | — |  |
| 3334 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3335 | Strip internal identifiers from gateway error responses | — | permitted | docketed — nothing engaged | — |  |
| 3336 | Split personal-data handling out of the shared ingestion library | FL-PI-001 ⛔ | permitted | decided fresh | — |  |
| 3337 | Verify de-identification by sampling rather than by assertion | FL-PI-001 ⛔ | permitted | decided fresh | — |  |
| 3338 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-003 FL-FG-005 ⛔ | denied | refused at the floor | — |  |
| 3339 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3340 | Change the escalation ladder so an automated tier may accept frontier risk | FL-MB-004 | denied | decided fresh | — |  |
| 3341 | Remove the contest link from the customer decision notice | FL-GV-005 | denied | decided fresh | — | ● |
| 3342 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | disposed by citation | — |  |
| 3343 | Name a data-governance custodian on each dataset record | FL-TD-006 | permitted | decided fresh | — |  |
| 3344 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-005 | permitted | decided fresh | — | ● |
| 3345 | Run licence detection over every agent-authored file | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3346 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 3347 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted | disposed by citation | — |  |
| 3348 | Gate external evaluator access on the signed agreement | FL-SF-006 | permitted | decided fresh | — |  |
| 3349 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 3350 | Restrict weight egress to the declared perimeter buckets | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 3351 | Redact prompt and completion logs before they reach retention | FL-PI-007 | permitted with conditions | decided fresh | — | ● |
| 3352 | Strip internal identifiers from gateway error responses | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3353 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-002 | permitted | decided fresh | — |  |
| 3354 | Log every read of the weights store to the perimeter audit trail | FL-SF-007 | permitted | decided fresh | — |  |
| 3355 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3356 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-006 | permitted | decided fresh | — |  |
| 3357 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-006 | permitted | decided fresh | — |  |
| 3358 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-002 | permitted | decided fresh | — |  |
| 3359 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-001 FL-BS-002 ⛔ | denied | refused at the floor | — |  |
| 3360 | Separate the production prompt label from its version string | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 3361 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted | decided fresh after a tie | none_tie |  |
| 3362 | Run denied-party screening at account enablement for every new enterprise tenant | FL-WX-002 | permitted | decided fresh | — |  |
| 3363 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3364 | Recompute the root digest from resource digests before promotion | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 3365 | Label agent-authored diffs so reviewers can isolate them | FL-AG-001 ⛔ | permitted | decided fresh | — |  |
| 3366 | Check every new import against the upstream registry before build | FL-AG-001 ⛔ | permitted | decided fresh | — |  |
| 3367 | Re-run the probe after the distillation step, not before it | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3368 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3369 | Write a docket entry for every arrival that is not charged | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 3370 | Run the persona and tone evaluation on the release build | FL-BS-002 | permitted | decided fresh | — |  |
| 3371 | Block internal address ranges in the web-fetch tool | — | permitted | docketed — nothing engaged | — |  |
| 3372 | Gate external evaluator access on the signed agreement | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 3373 | Record attribution for the reused tokenizer snippet | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3374 | Pin the key-value cache budget for the agentic serving tier | FL-IN-005 | permitted | decided fresh | — |  |
| 3375 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3376 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh | — |  |
| 3377 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3378 | Move retrieved documents into a separate, clearly marked context block | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 3379 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-006 | permitted | decided fresh | — | ● |
| 3380 | Report first-token and per-token latency against the tier budgets | FL-IN-005 | permitted | decided fresh | — |  |
| 3381 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-008 | permitted | decided fresh | — |  |
| 3382 | Run the decontamination check over the new code corpus | FL-EV-008 | permitted | decided fresh | — |  |
| 3383 | Declare both base models in the merged cirrus-small manifest | FL-MB-004 | permitted | disposed by citation | — |  |
| 3384 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted | decided fresh | — |  |
| 3385 | Route parameter changes through the amendment workflow instead | FL-GV-005 | permitted | decided fresh | — | ● |
| 3386 | Run licence detection over every agent-authored file | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3387 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 3388 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-004 | permitted | decided fresh | — | ● |
| 3389 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 3390 | Respect the robots.txt AI directive in the web crawler | FL-TD-006 | permitted | decided fresh | — | ● |
| 3391 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 3392 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 ⛔ | denied | refused at the floor | — |  |
| 3393 | Publish the prompt-log retention clock in the customer portal | FL-PI-003 | permitted | decided fresh | — |  |
| 3394 | Expose a contest path to affected customers in the portal | FL-GV-007 | permitted | decided fresh | — |  |
| 3395 | Run the decontamination check over the new code corpus | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 3396 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | disposed by citation | — |  |
| 3397 | Ship the release with technical documentation carried over from the prior version | FL-TR-002 | denied | decided fresh | — |  |
| 3398 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3399 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3400 | Record the prompt and context hash on each agent commit | FL-AG-007 | permitted | decided fresh | — | ● |
| 3401 | Resolve internal packages from the private registry first | FL-SC-006 | permitted | disposed by citation | — |  |
| 3402 | Sign agent commits with a workload identity rather than a person's key | FL-AG-008 | permitted | decided fresh | — |  |
| 3403 | Enforce the instruction and data boundary on the retrieval path | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 3404 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-005 | permitted | disposed by citation | — |  |
| 3405 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | decided fresh | — |  |
| 3406 | Publish a signed bill of materials covering transitive dependencies | FL-SC-005 | permitted | decided fresh | — |  |
| 3407 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 3408 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-006 | permitted | decided fresh | — | ● |
| 3409 | Refresh the sanctioned-destination blocklist within its declared interval | FL-WX-002 | permitted with conditions | decided fresh | — | ● |
| 3410 | Enforce server-side authorization on the new batch endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3411 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3412 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3413 | Recompute the root digest from resource digests before promotion | FL-MB-004 | permitted | disposed by citation | — |  |
| 3414 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-005 | permitted | decided fresh | — |  |
| 3415 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | permitted | decided fresh | — |  |
| 3416 | Block promotion until the dangerous-capability reports complete | FL-SF-006 | permitted | decided fresh | — |  |
| 3417 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-003 | permitted | decided fresh | — |  |
| 3418 | Respect the robots.txt AI directive in the web crawler | FL-TD-003 | permitted | decided fresh | — |  |
| 3419 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3420 | Run the memorisation probe on the release candidate | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 3421 | Propagate attribution obligations from corpus records to release notes | FL-TD-007 | permitted | decided fresh | — |  |
| 3422 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3423 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | decided fresh | — |  |
| 3424 | Let retrieval read audit findings so precedent search returns more | FL-GV-011 | denied | decided fresh | — |  |
| 3425 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — |  |
| 3426 | Open the agentic tier to customers while the safety case is in draft | FL-SF-004 | denied | decided fresh | — |  |
| 3427 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-009 | permitted | decided fresh | — |  |
| 3428 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-009 | permitted | decided fresh | — |  |
| 3429 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 3430 | Roll out the new grader configuration without an agreement study | FL-EV-003 | denied | decided fresh | — |  |
| 3431 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-004 | permitted | decided fresh | — |  |
| 3432 | Run the personal-data scan on every new training shard | FL-PI-004 | permitted | decided fresh | — |  |
| 3433 | Escape tool output before it reaches the shell adapter | FL-LS-006 | permitted | decided fresh | — |  |
| 3434 | Declare the carrier channel for each untrusted input source | FL-LS-004 | permitted | decided fresh | — |  |
| 3435 | Escape tool output before it reaches the shell adapter | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 3436 | Apply an allowlist to the retrieval connector's target parameter | — | permitted | docketed — nothing engaged | — |  |
| 3437 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-002 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 3438 | Fail closed when a dataset licence string does not parse | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 3439 | Keep the human override reachable in the high-risk review flow | FL-GV-010 | permitted | decided fresh | — |  |
| 3440 | Scan responses for canary tokens before they leave the gateway | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 3441 | Target the retention fine-tune at users the model scores as vulnerable | FL-GV-001 FL-TD-007 ⛔ | denied | refused at the floor | — |  |
| 3442 | Run the personal-data scan on every new training shard | FL-PI-002 | permitted | decided fresh | — |  |
| 3443 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3444 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted with conditions | decided fresh | — | ● |
| 3445 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 3446 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3447 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted | decided fresh | — |  |
| 3448 | Submit an amendment retiring the deferred data-governance clauses early | FL-CB-003 | denied | decided fresh | — |  |
| 3449 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 3450 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 3451 | Downgrade the default incident-severity classification to avoid triggering the reporting clock | FL-TR-004 FL-SC-005 ⛔ | denied | refused at the floor | — |  |
| 3452 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted | decided fresh | — |  |
| 3453 | Deploy the gateway image the broken pipeline produced without attestation | FL-SC-003 | denied | decided fresh | — |  |
| 3454 | Check the code-signing extended key usage on the release chain | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3455 | Route flagged responses to the block path rather than a warning | FL-BS-006 | permitted | decided fresh | — |  |
| 3456 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-006 | permitted | decided fresh | — |  |
| 3457 | Propagate attribution obligations from corpus records to release notes | FL-TD-007 | permitted | decided fresh | — | ● |
| 3458 | Drop the failing refusal suite from the promotion gate this train | FL-EV-003 | denied | decided fresh | — |  |
| 3459 | Scan responses for canary tokens before they leave the gateway | FL-LS-009 | permitted | decided fresh | — |  |
| 3460 | Screen new fine-tuning shards for backdoor triggers | FL-LS-009 | permitted | decided fresh | — |  |
| 3461 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-PI-004 | denied | decided fresh | — |  |
| 3462 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-001 FL-EV-006 ⛔ | denied | refused at the floor | — |  |
| 3463 | Track system-prompt versions in a free-text description field | FL-MB-008 | denied | decided fresh | — |  |
| 3464 | Disable usage-policy enforcement actions for the enterprise tier's private deployments | FL-UH-005 | denied | decided fresh | — |  |
| 3465 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-002 FL-SF-008 ⛔ | denied | refused at the floor | — |  |
| 3466 | Widen the parity report to distinguish immaterial differences | FL-EV-010 | permitted | decided fresh | — |  |
| 3467 | Widen the prompt-label review rule to cover staging labels too | FL-EV-006 | denied | decided fresh | — |  |
| 3468 | Let the agent render markdown images to any host the page supplies | FL-LS-001 FL-GV-005 ⛔ | denied | refused at the floor | — |  |
| 3469 | Add a configuration flag that lets the incident-reporting deadline be extended | FL-TR-002 | denied | decided fresh | — |  |
| 3470 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3471 | Embed the canary string in every generated evaluation case | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 3472 | Keep annotator identifiers in the exported preference dataset for the vendor handoff | FL-PV-002 | denied | decided fresh | — |  |
| 3473 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-CB-003 | denied | decided fresh | — |  |
| 3474 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-001 FL-PI-004 ⛔ | denied | refused at the floor | — |  |
| 3475 | Gate promotion on the full safety suite, not the fast subset | FL-EV-007 | permitted | decided fresh | — |  |
| 3476 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — | ● |
| 3477 | Gate promotion on the full safety suite, not the fast subset | FL-EV-010 | permitted | decided fresh | — | ● |
| 3478 | Make decision records append-only in the store schema | FL-GV-009 | permitted | decided fresh | — |  |
| 3479 | Separate the audit register from the precedent store at schema level | FL-GV-009 | permitted | decided fresh | — |  |
| 3480 | Record the availability type on every newly onboarded source | FL-TD-002 | permitted | decided fresh | — | ● |
| 3481 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-002 | permitted | decided fresh | — |  |
| 3482 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 3483 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 3484 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-006 | denied | decided fresh | — |  |
| 3485 | Record the elicitation effort alongside every uplift-eval result | FL-CB-003 | permitted with conditions | decided fresh | — | ● |
| 3486 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-007 | permitted | decided fresh | — |  |
| 3487 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-006 | permitted | disposed by citation | — |  |
| 3488 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted | decided fresh | — |  |
| 3489 | Check agent diffs for structural matches against known libraries | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3490 | Publish a signed bill of materials covering transitive dependencies | FL-SC-002 | permitted | decided fresh | — |  |
| 3491 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 3492 | Screen generated code against the copyleft signature database | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3493 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 3494 | Separate the production prompt label from its version string | FL-MB-009 | permitted | decided fresh | — |  |
| 3495 | Skip signature verification on load to cut startup time | FL-MB-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 3496 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-003 FL-TR-002 ⛔ | denied | refused at the floor | — |  |
| 3497 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | decided fresh | — | ● |
| 3498 | Run denied-party screening at account enablement for every new enterprise tenant | FL-WX-002 | permitted with conditions | decided fresh | — | ● |
| 3499 | Check the code-signing extended key usage on the release chain | FL-MB-005 | permitted | decided fresh | — |  |
| 3500 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 3501 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 3502 | Propagate attribution obligations from corpus records to release notes | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 3503 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 3504 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-004 | permitted | decided fresh | — |  |
| 3505 | Report refusal and over-refusal rates side by side | FL-BS-004 | permitted | decided fresh | — |  |
| 3506 | Restrict weight egress to the declared perimeter buckets | FL-SF-008 | permitted | decided fresh | — |  |
| 3507 | Log every read of the weights store to the perimeter audit trail | FL-SF-008 | permitted | decided fresh | — |  |
| 3508 | Sample the de-identified shard weekly and report the residual rate | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 3509 | Check agent diffs for structural matches against known libraries | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3510 | Export the rulebook without the standing declaration block | FL-GV-002 FL-TR-002 ⛔ | denied | refused at the floor | — |  |
| 3511 | Justify the two remaining special-category fields on the dataset record | FL-PI-006 | permitted | decided fresh | — | ● |
| 3512 | Resolve internal packages from the private registry first | FL-SC-005 | permitted | decided fresh | — | ● |
| 3513 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-005 | permitted | decided fresh | — |  |
| 3514 | Let the mail agent follow instructions it finds in the message body | FL-LS-005 | denied | decided fresh | — |  |
| 3515 | Repack the shard files after signing and reuse the old manifest | FL-MB-001 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 3516 | Grant a new hire weight-store access before the vetting record clears | FL-WX-001 FL-AG-004 ⛔ | denied | refused at the floor | — |  |
| 3517 | Register the new fused kernel as a nondeterministic operation | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3518 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3519 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh | — |  |
| 3520 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | decided fresh | — |  |
| 3521 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-002 FL-EV-004 ⛔ | denied | refused at the floor | — |  |
| 3522 | Screen new fine-tuning shards for backdoor triggers | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 3523 | Record attribution for the reused tokenizer snippet | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 3524 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-002 | denied | decided fresh | — | ● |
| 3525 | Move the production prompt label straight from the deploy script | FL-MB-004 | denied | decided fresh | — |  |
| 3526 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 3527 | Stop reading the loop limit from an environment variable | FL-FG-003 | permitted | decided fresh | — |  |
| 3528 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — | ● |
| 3529 | Blend the share-alike corpus into the proprietary preference set | FL-TD-002 | denied | decided fresh | — |  |
| 3530 | Record an export-classification determination before every weight transfer | FL-WX-002 | permitted with conditions | decided fresh | — | ● |
| 3531 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | decided fresh | — |  |
| 3532 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | decided fresh | — |  |
| 3533 | Rewrite the absolute-provision list in the rulebook build script | FL-FG-003 | denied | decided fresh | — |  |
| 3534 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-002 FL-IN-004 ⛔ | denied | refused at the floor | — |  |
| 3535 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-002 | permitted | decided fresh | — | ● |
| 3536 | Embed the canary string in every generated evaluation case | FL-EV-006 | permitted | decided fresh | — |  |
| 3537 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted | decided fresh | — |  |
| 3538 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — |  |
| 3539 | Publish the release notes without the downstream-provider information section | FL-TR-004 FL-PI-004 ⛔ | denied | refused at the floor | — |  |
| 3540 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-002 | denied | decided fresh | — |  |
| 3541 | Attribute the standing declaration in the exported rulebook | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 3542 | Inline retrieved documents into the system prompt to save tokens | FL-LS-005 | denied | decided fresh | — |  |
| 3543 | Update the third-party licence inventory with this dependency change | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3544 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-002 | permitted | decided fresh | — |  |
| 3545 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 3546 | Hold goodput at the tier threshold under the burst profile | FL-IN-002 | permitted | decided fresh | — |  |
| 3547 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-002 | denied | decided fresh | — |  |
| 3548 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-001 FL-SF-007 ⛔ | denied | refused at the floor | — |  |
| 3549 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-006 | permitted | decided fresh | — |  |
| 3550 | Pin every dependency to an immutable digest in the lockfile | FL-SC-006 | permitted | decided fresh | — |  |
| 3551 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-001 FL-LS-003 ⛔ | denied | refused at the floor | — |  |
| 3552 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted | decided fresh | — |  |
| 3553 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3554 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted | decided fresh | — |  |
| 3555 | Validate tenant scope on every portal export request | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3556 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | disposed by citation | — |  |
| 3557 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-004 | permitted | decided fresh | — |  |
| 3558 | Enforce the minor break reminder server-side in companion mode | FL-UH-004 | permitted | decided fresh | — |  |
| 3559 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3560 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-003 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 3561 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 3562 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3563 | Edit stored decision records in place to correct their rationale text | FL-GV-007 | denied | decided fresh | — | ● |
| 3564 | Record the builder identity in attestations for nightly checkpoints | FL-SC-006 | permitted | disposed by citation | — |  |
| 3565 | Sign agent commits with a workload identity rather than a person's key | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 3566 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-008 | denied | decided fresh | — | ● |
| 3567 | Fail the merge when the scanner reports an unresolved licence | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3568 | Move release signing keys onto the hardware security module | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 3569 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3570 | Fuzz the changed completions parameters before release | FL-AS-001 | permitted | decided fresh | — |  |
| 3571 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-002 FL-BS-003 ⛔ | denied | refused at the floor | — |  |
| 3572 | Cover the new administrative routes in the authorization test suite | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3573 | Pin the key-value cache budget for the agentic serving tier | — | permitted | docketed — nothing engaged | — |  |
| 3574 | Screen new fine-tuning shards for backdoor triggers | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 3575 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted | decided fresh | — |  |
| 3576 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-002 FL-SC-006 ⛔ | denied | refused at the floor | — |  |
| 3577 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 3578 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 3579 | Let the mail agent follow instructions it finds in the message body | FL-LS-009 | denied | decided fresh | — |  |
| 3580 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 3581 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-001 | permitted | decided fresh | — |  |
| 3582 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-001 | permitted | decided fresh | — |  |
| 3583 | Return a generic error identifier instead of the stack trace | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3584 | Route parameter changes through the amendment workflow instead | FL-GV-011 | permitted | decided fresh | — |  |
| 3585 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-008 | permitted | decided fresh | — |  |
| 3586 | Pin the golden-prompt baseline to a commit digest | FL-EV-008 | permitted | decided fresh | — |  |
| 3587 | Log every read of the weights store to the perimeter audit trail | FL-SF-004 | permitted | decided fresh | — |  |
| 3588 | Remove the sandbagging detector from the eval harness to simplify the report | FL-CB-002 | denied | decided fresh | — |  |
| 3589 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 3590 | Verify de-identification by sampling rather than by assertion | FL-PI-003 | permitted with conditions | decided fresh | — | ● |
| 3591 | Reject artifacts whose served hash differs from the registry entry | FL-MB-007 | permitted | decided fresh | — | ● |
| 3592 | Let the agent render markdown images to any host the page supplies | FL-LS-008 | denied | decided fresh | — |  |
| 3593 | Measure judge and human agreement for the new grader configuration | FL-EV-007 | permitted | decided fresh | — |  |
| 3594 | Block promotion until the dangerous-capability reports complete | FL-SF-007 | permitted | decided fresh | — |  |
| 3595 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-002 FL-GV-008 ⛔ | denied | refused at the floor | — |  |
| 3596 | Apply an allowlist to the retrieval connector's target parameter | — | permitted | docketed — nothing engaged | — |  |
| 3597 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-001 ⛔ | denied | refused at the floor | — |  |
| 3598 | Declare the carrier channel for each untrusted input source | FL-LS-010 | permitted | decided fresh | — |  |
| 3599 | Add a configuration flag that lets the incident-reporting deadline be extended | FL-TR-003 | denied | decided fresh | — |  |
| 3600 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-005 | permitted | decided fresh | — |  |
| 3601 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-005 | permitted | decided fresh | — |  |
| 3602 | Exercise injection detection on the changed tool-calling path | FL-LS-007 | permitted | decided fresh | — |  |
| 3603 | Exercise injection detection on the changed tool-calling path | FL-LS-007 | permitted | decided fresh | — |  |
| 3604 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | permitted | decided fresh | — |  |
| 3605 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | disposed by citation | — |  |
| 3606 | Report preemption counts in the load-test summary | FL-IN-006 | permitted | decided fresh | — |  |
| 3607 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted | decided fresh | — |  |
| 3608 | Stop reading the loop limit from an environment variable | FL-FG-002 | permitted | decided fresh | — |  |
| 3609 | Expose a contest path to affected customers in the portal | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 3610 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-003 | permitted | decided fresh | — |  |
| 3611 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3612 | Measure membership-inference advantage on the release candidate | FL-LS-007 | permitted | decided fresh | — |  |
| 3613 | Declare the agent loop limit numerically with its units | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 3614 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh | — |  |
| 3615 | Recompute the root digest from resource digests before promotion | FL-MB-004 | permitted | decided fresh | — |  |
| 3616 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3617 | Drop the failing refusal suite from the promotion gate this train | FL-EV-001 FL-MB-004 ⛔ | denied | refused at the floor | — |  |
| 3618 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-007 | denied | decided fresh | — |  |
| 3619 | Give the batch agent the shared service account to dodge quota holds | FL-FG-003 | denied | decided fresh | — |  |
| 3620 | Sample the de-identified shard weekly and report the residual rate | FL-PI-003 | permitted | decided fresh | — |  |
| 3621 | Scan responses for canary tokens before they leave the gateway | FL-LS-006 | permitted | decided fresh | — |  |
| 3622 | Route critical-incident detection signals to the on-call dashboard instead of the reporting queue | FL-TR-003 | denied | decided fresh | — |  |
| 3623 | Fuzz the changed completions parameters before release | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3624 | Record a lawful basis for each conversation-data source | FL-PI-005 | permitted | decided fresh | — |  |
| 3625 | Strip internal identifiers from gateway error responses | FL-AS-002 | permitted | docketed — not charged | — |  |
| 3626 | Keep reporter bulletins off the adjudication input path | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 3627 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3628 | Recompute the root digest from resource digests before promotion | FL-MB-005 | permitted | decided fresh | — |  |
| 3629 | Give every system prompt an immutable version identifier | FL-MB-005 | permitted | decided fresh | — |  |
| 3630 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-002 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 3631 | Resolve internal packages from the private registry first | FL-SC-007 | permitted | decided fresh | — |  |
| 3632 | Retire two supply-chain provisions from the rulebook manifest | FL-SC-008 | denied | decided fresh | — |  |
| 3633 | Enforce the instruction and data boundary on the retrieval path | FL-LS-004 | permitted | decided fresh | — |  |
| 3634 | Escape tool output before it reaches the shell adapter | FL-LS-004 | permitted | decided fresh | — |  |
| 3635 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 3636 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | decided fresh | — |  |
| 3637 | Escape tool output before it reaches the shell adapter | FL-LS-007 | permitted | decided fresh | — |  |
| 3638 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-003 | permitted | decided fresh | — |  |
| 3639 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-001 FL-SF-007 ⛔ | denied | refused at the floor | — |  |
| 3640 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3641 | Sample the de-identified shard weekly and report the residual rate | FL-PI-004 | permitted | decided fresh | — |  |
| 3642 | Train on the partner's user conversations before the basis is recorded | FL-PI-001 FL-SF-005 ⛔ | denied | refused at the floor | — |  |
| 3643 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | disposed by citation | — |  |
| 3644 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3645 | Check the code-signing extended key usage on the release chain | FL-MB-006 | permitted | decided fresh | — |  |
| 3646 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 3647 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3648 | Move retrieved documents into a separate, clearly marked context block | FL-LS-006 | permitted | decided fresh | — |  |
| 3649 | Embed the canary string in every generated evaluation case | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 3650 | Let the release owner override the uplift screen result to hit the launch date | FL-CB-001 FL-GV-009 ⛔ | denied | refused at the floor | — |  |
| 3651 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 3652 | Publish the notice file alongside each inference-engine release | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3653 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | permitted | decided fresh | — |  |
| 3654 | Disable the self-exfiltration probe in the agent sandbox to fix a flaky test | FL-CB-002 | denied | decided fresh | — |  |
| 3655 | Route parameter changes through the amendment workflow instead | FL-GV-011 | permitted with conditions | decided fresh | — | ● |
| 3656 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-SC-008 | denied | decided fresh | — |  |
| 3657 | Escape tool output before it reaches the shell adapter | FL-LS-011 | permitted | decided fresh | — |  |
| 3658 | Require human confirmation before the agent executes a write tool | FL-LS-011 | permitted | decided fresh | — |  |
| 3659 | Make the inference-engine build hermetic and reproducible | FL-SC-003 | permitted | decided fresh | — |  |
| 3660 | Keep reporter bulletins off the adjudication input path | FL-GV-011 | permitted | decided fresh | — |  |
| 3661 | Record the compute-threshold determination separately per jurisdiction | FL-GV-011 | permitted | decided fresh | — |  |
| 3662 | Grant a new hire weight-store access before the vetting record clears | FL-WX-002 | denied | decided fresh | — |  |
| 3663 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 3664 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh | — | ● |
| 3665 | Gate promotion on the full safety suite, not the fast subset | FL-EV-005 | permitted | decided fresh | — | ● |
| 3666 | Record the capability-threshold determination on the release record | FL-SF-007 | permitted | decided fresh after a tie | none_tie |  |
| 3667 | Restrict agent outbound calls to the allowlisted host set | FL-AG-006 | permitted | decided fresh | — |  |
| 3668 | Pin the hash-match list to last year's clearinghouse snapshot to skip the sync job | FL-CS-004 | denied | decided fresh | — | ● |
| 3669 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 3670 | Run agent-authored code only inside the sandboxed runner | FL-AG-005 | permitted | decided fresh | — |  |
| 3671 | Publish a review checklist for agent changes to the eval harness | FL-AG-005 | permitted | decided fresh | — |  |
| 3672 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3673 | Write a docket entry for every arrival that is not charged | FL-GV-005 | permitted | decided fresh | — |  |
| 3674 | Separate the production prompt label from its version string | FL-MB-008 | permitted | disposed by citation | — |  |
| 3675 | State the percentile on every latency claim in the dashboard | FL-IN-003 | permitted | decided fresh | — |  |
| 3676 | Raise mitigations to match the assessed capability level | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 3677 | Repack the shard files after signing and reuse the old manifest | FL-MB-002 FL-SF-008 ⛔ | denied | refused at the floor | — |  |
| 3678 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3679 | Reject unexpected content types on the tool-callback endpoint | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3680 | Move cost control from a meter to a pre-flight breaker | FL-FG-002 | permitted | decided fresh | — |  |
| 3681 | Record the tolerance band used for each accuracy comparison | FL-EV-009 | permitted | decided fresh | — |  |
| 3682 | Pin the key-value cache budget for the agentic serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3683 | Keep cases released after the training cutoff in the holdout | FL-EV-003 | permitted | decided fresh | — |  |
| 3684 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | decided fresh | — |  |
| 3685 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 3686 | Restrict deserialisation to the declared tool-payload types | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3687 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 3688 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3689 | Publish the notice file alongside each inference-engine release | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3690 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TD-002 | denied | decided fresh | — |  |
| 3691 | Release the run record with the threshold determination left blank | FL-SF-004 | denied | decided fresh | — |  |
| 3692 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 3693 | Validate tenant scope on every portal export request | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3694 | Measure membership-inference advantage on the release candidate | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 3695 | Record verifiable parental consent on the child-data ingestion record | FL-CS-004 | permitted | decided fresh | — |  |
| 3696 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 3697 | Hold verbatim third-party reproduction below the span threshold | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 3698 | Restrict weight egress to the declared perimeter buckets | FL-SF-004 | permitted | decided fresh | — |  |
| 3699 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted | decided fresh | — |  |
| 3700 | Remove the canary check from the response filter to cut latency | FL-LS-001 FL-SC-002 ⛔ | denied | refused at the floor | — |  |
| 3701 | State the percentile on every latency claim in the dashboard | FL-IN-001 | permitted | decided fresh | — |  |
| 3702 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-003 | permitted with conditions | decided fresh | — | ● |
| 3703 | Let the agent edit the release workflow to unblock its own branch | FL-AG-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3704 | Rewrite the last raw query in the usage-reporting job | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3705 | Route law-enforcement data requests straight to on-call fulfilment, skipping the legal-review queue | FL-PV-003 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 3706 | Block promotion until the dangerous-capability reports complete | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 3707 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3708 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | decided fresh | — |  |
| 3709 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | decided fresh | — |  |
| 3710 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted | decided fresh | — |  |
| 3711 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3712 | Let the coding agent land its router refactor on green tests alone | FL-AG-004 | denied | decided fresh | — |  |
| 3713 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 3714 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | decided fresh | — |  |
| 3715 | Reject artifacts whose served hash differs from the registry entry | FL-MB-005 | permitted | disposed by citation | — |  |
| 3716 | Gate promotion on the full safety suite, not the fast subset | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 3717 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted | decided fresh | — |  |
| 3718 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-002 | permitted | disposed by citation | — |  |
| 3719 | Let the mail agent follow instructions it finds in the message body | FL-LS-010 | denied | decided fresh | — |  |
| 3720 | Cut the incident-severity form down to the fields the reporting clock actually reads | FL-TR-003 | permitted with conditions | decided fresh | — | ● |
| 3721 | Propagate attribution obligations from corpus records to release notes | FL-TD-007 | permitted | decided fresh | — |  |
| 3722 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-001 FL-PI-005 ⛔ | denied | refused at the floor | — |  |
| 3723 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3724 | Export the rulebook without the standing declaration block | FL-GV-011 | denied | decided fresh | — |  |
| 3725 | Turn off commit signing for the agent runner while its key rotates | FL-AG-001 FL-GV-005 ⛔ | denied | refused at the floor | — |  |
| 3726 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 3727 | Repack the shard files after signing and reuse the old manifest | FL-MB-001 FL-SF-005 ⛔ | denied | refused at the floor | — |  |
| 3728 | Carry attribution notices through to the shipped container image | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3729 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-003 | permitted | decided fresh | — |  |
| 3730 | Run the persona and tone evaluation on the release build | FL-BS-003 | permitted | decided fresh | — |  |
| 3731 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-003 | permitted | decided fresh | — |  |
| 3732 | Hold agentic-checkpoint promotion on a completed autonomy-eval result | FL-CB-003 | permitted | decided fresh | — |  |
| 3733 | Make decision records append-only in the store schema | FL-GV-011 | permitted | decided fresh | — |  |
| 3734 | Route parameter changes through the amendment workflow instead | FL-GV-011 | permitted | decided fresh | — |  |
| 3735 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 3736 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-005 | permitted | decided fresh | — |  |
| 3737 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3738 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 3739 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 3740 | Restrict weight egress to the declared perimeter buckets | FL-SF-007 | permitted | decided fresh | — |  |
| 3741 | Name a data-governance custodian on each dataset record | FL-TD-007 | permitted | decided fresh | — |  |
| 3742 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-001 FL-AG-005 ⛔ | denied | refused at the floor | — |  |
| 3743 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-003 | permitted | decided fresh | — |  |
| 3744 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-003 | permitted | decided fresh | — |  |
| 3745 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 3746 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-002 FL-BS-006 ⛔ | denied | refused at the floor | — |  |
| 3747 | Record the tolerance band used for each accuracy comparison | FL-EV-005 | permitted | decided fresh | — | ● |
| 3748 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 3749 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-003 | permitted | decided fresh | — |  |
| 3750 | Update the third-party licence inventory with this dependency change | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3751 | Publish a signed bill of materials covering transitive dependencies | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 3752 | Redact prompt and completion logs before they reach retention | FL-PI-003 | permitted | decided fresh | — |  |
| 3753 | Run the personal-data scan on every new training shard | FL-PI-003 | permitted | decided fresh | — |  |
| 3754 | Run the personal-data scan on every new training shard | FL-PI-004 | permitted | decided fresh | — |  |
| 3755 | Justify the two remaining special-category fields on the dataset record | FL-PI-007 | permitted | decided fresh | — | ● |
| 3756 | Attach Croissant metadata to the new publisher corpus | FL-TD-004 | permitted | decided fresh | — |  |
| 3757 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3758 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 3759 | Stop reading the loop limit from an environment variable | FL-FG-003 | permitted | decided fresh | — |  |
| 3760 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 3761 | Gate external evaluator access on the signed agreement | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 3762 | State the percentile on every latency claim in the dashboard | FL-IN-004 | permitted | decided fresh | — |  |
| 3763 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-004 | permitted | decided fresh | — |  |
| 3764 | Move retrieved documents into a separate, clearly marked context block | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 3765 | Publish the signing certificate chain alongside each release digest | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3766 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-009 | permitted | decided fresh | — | ● |
| 3767 | Give the tool-call graph an explicit terminator | FL-FG-006 | permitted | decided fresh | — |  |
| 3768 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 3769 | Add the new sampling library to the licence inventory | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3770 | Label agent-authored diffs so reviewers can isolate them | FL-AG-004 | permitted | decided fresh | — |  |
| 3771 | Reject artifacts whose served hash differs from the registry entry | FL-MB-006 | permitted | decided fresh | — |  |
| 3772 | Record the licence class for every corpus the crawler ingests | FL-TD-003 | permitted | decided fresh | — |  |
| 3773 | Change the escalation ladder so an automated tier may accept frontier risk | FL-TD-005 | denied | decided fresh | — |  |
| 3774 | Export the rulebook without the standing declaration block | FL-GV-007 | denied | decided fresh | — |  |
| 3775 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 3776 | Propose allowing sampled rather than exhaustive licence detection | FL-IN-003 | denied | decided fresh | — |  |
| 3777 | Widen the parity report to distinguish immaterial differences | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 3778 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-004 | permitted | decided fresh | — |  |
| 3779 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 3780 | Propose an amendment codifying coverage rules for generated eval configs | FL-GV-006 | denied | decided fresh | — |  |
| 3781 | Parameterise the new experiment-metrics filter queries | — | permitted | docketed — nothing engaged | — |  |
| 3782 | Exempt agent-authored files from the licence scan to speed reviews | FL-IP-001 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 3783 | Give the coding agent its own short-lived signing credential | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3784 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-004 | permitted | decided fresh | — |  |
| 3785 | Hold goodput at the tier threshold under the burst profile | FL-IN-004 | permitted | decided fresh | — |  |
| 3786 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-006 | permitted | decided fresh | — |  |
| 3787 | Replace the manual denied-party screening spreadsheet with an automated gateway check | FL-WX-003 | permitted | decided fresh | — |  |
| 3788 | Restrict agent outbound calls to the allowlisted host set | FL-AG-005 | permitted | decided fresh | — |  |
| 3789 | Record the prompt and context hash on each agent commit | FL-AG-005 | permitted | decided fresh | — |  |
| 3790 | Measure membership-inference advantage on the release candidate | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 3791 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3792 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3793 | Pin every dependency to an immutable digest in the lockfile | FL-SC-008 | permitted | decided fresh | — | ● |
| 3794 | Pin the key-value cache budget for the agentic serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3795 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 3796 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 3797 | Give every system prompt an immutable version identifier | FL-MB-009 | permitted | disposed by citation | — |  |
| 3798 | Backfill lineage records for the older quantised checkpoints | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 3799 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 3800 | Report first-token and per-token latency against the tier budgets | FL-IN-006 | permitted | decided fresh | — |  |
| 3801 | Keep cases released after the training cutoff in the holdout | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 3802 | Verify de-identification by sampling rather than by assertion | FL-PI-007 | permitted | decided fresh | — |  |
| 3803 | Register the new fused kernel as a nondeterministic operation | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3804 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-009 | denied | decided fresh | — |  |
| 3805 | Declare the arrival distribution used in the throughput benchmark | FL-IN-001 | permitted | decided fresh | — | ● |
| 3806 | Scan responses for canary tokens before they leave the gateway | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 3807 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 3808 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted | decided fresh | — |  |
| 3809 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — |  |
| 3810 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted | decided fresh | — |  |
| 3811 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-002 | denied | decided fresh | — |  |
| 3812 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 3813 | Route critical-incident detection signals to the on-call dashboard instead of the reporting queue | FL-TR-004 FL-TD-008 ⛔ | denied | refused at the floor | — |  |
| 3814 | Embed the canary string in every generated evaluation case | FL-EV-010 | permitted with conditions | decided fresh | — | ● |
| 3815 | Run the personal-data scan on every new training shard | FL-PI-006 | permitted | decided fresh | — |  |
| 3816 | Exercise injection detection on the changed tool-calling path | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 3817 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted | decided fresh | — |  |
| 3818 | Turn off egress monitoring on the weight store during the migration window | FL-WX-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 3819 | Record the prompt and context hash on each agent commit | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 3820 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3821 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-004 | permitted | decided fresh | — |  |
| 3822 | Hold agentic-checkpoint promotion on a completed autonomy-eval result | FL-CB-004 | permitted | decided fresh | — |  |
| 3823 | Edit the toxicity threshold directly through the adjudication service credentials | FL-LS-003 | denied | decided fresh | — |  |
| 3824 | Pin the key-value cache budget for the agentic serving tier | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 3825 | Run the personal-data scan on every new training shard | FL-PI-006 | permitted | decided fresh | — |  |
| 3826 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-004 | permitted | decided fresh | — | ● |
| 3827 | Let a client-supplied flag override minor-mode restrictions in the mobile app | FL-CS-002 FL-GV-008 ⛔ | denied | refused at the floor | — |  |
| 3828 | Restrict weight egress to the declared perimeter buckets | FL-SF-005 | permitted | decided fresh | — |  |
| 3829 | Point the canary tier at a checkpoint that was never registered | FL-MB-004 | denied | decided fresh | — |  |
| 3830 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-001 FL-GV-010 ⛔ | denied | refused at the floor | — |  |
| 3831 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh | — |  |
| 3832 | Move the production prompt label straight from the deploy script | FL-MB-009 | denied | decided fresh | — |  |
| 3833 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-MB-005 | denied | decided fresh | — |  |
| 3834 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-003 | permitted | decided fresh | — |  |
| 3835 | Declare sample size and percentile alongside the parity result | FL-EV-003 | permitted | decided fresh | — |  |
| 3836 | Measure judge and human agreement for the new grader configuration | FL-EV-008 | permitted | decided fresh | — |  |
| 3837 | Measure membership-inference advantage on the release candidate | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 3838 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3839 | Record the licence class for every corpus the crawler ingests | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3840 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | permitted | decided fresh | — |  |
| 3841 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-003 | permitted | decided fresh | — |  |
| 3842 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted | decided fresh | — |  |
| 3843 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | decided fresh | — |  |
| 3844 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 3845 | Run semantic analysis over the agent diff in continuous integration | FL-AG-007 | permitted | disposed by citation | — |  |
| 3846 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 3847 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | decided fresh | — |  |
| 3848 | Run release builds on ephemeral runners with pinned images | FL-SC-004 | permitted | decided fresh | — | ● |
| 3849 | Let the companion persona serve romantic content even when the minor flag is set | FL-UH-003 | denied | decided fresh | — |  |
| 3850 | Run the decontamination check over the new code corpus | FL-EV-004 | permitted | decided fresh | — |  |
| 3851 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-004 | permitted | decided fresh | — |  |
| 3852 | Drop the failing refusal suite from the promotion gate this train | FL-EV-007 | denied | decided fresh | — |  |
| 3853 | Ship the prefill rewrite that pushes first-token time past budget | FL-IN-004 | denied | decided fresh | — |  |
| 3854 | Add a quarterly compliance drill that exercises the incident-reporting path end to end | FL-TR-002 | permitted | decided fresh | — |  |
| 3855 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-007 | permitted | decided fresh | — |  |
| 3856 | Update the third-party licence inventory with this dependency change | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3857 | Raise the capability threshold in the policy repository | FL-EV-009 | denied | decided fresh | — |  |
| 3858 | Compare the provenance subject digest to the distributed artifact | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 3859 | Record attribution for the reused tokenizer snippet | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3860 | Label agent-authored diffs so reviewers can isolate them | FL-AG-008 | permitted | decided fresh | — |  |
| 3861 | Run agent-authored code only inside the sandboxed runner | FL-AG-008 | permitted | decided fresh | — |  |
| 3862 | Raise mitigations to match the assessed capability level | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 3863 | Embed the canary string in every generated evaluation case | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 3864 | Report preemption counts in the load-test summary | FL-IN-006 | permitted | decided fresh | — |  |
| 3865 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3866 | Require a named owner to approve production prompt label moves | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 3867 | Commit the live cluster token into the test fixtures directory | FL-SC-004 | denied | decided fresh | — |  |
| 3868 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 3869 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-007 | denied | decided fresh | — |  |
| 3870 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted | decided fresh | — |  |
| 3871 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-008 | permitted | disposed by citation | — |  |
| 3872 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-001 FL-AG-008 ⛔ | denied | refused at the floor | — |  |
| 3873 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 3874 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 3875 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 3876 | Update the third-party licence inventory with this dependency change | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 3877 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 3878 | Turn off commit signing for the agent runner while its key rotates | FL-AG-006 | denied | decided fresh | — |  |
| 3879 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — |  |
| 3880 | Validate tenant scope on every portal export request | FL-AS-006 | permitted | docketed — not charged | — |  |
| 3881 | Recompute the root digest from resource digests before promotion | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 3882 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-005 | permitted | decided fresh | — |  |
| 3883 | Make the government-request log append-only across the bulk-export path | FL-PV-005 | permitted | decided fresh | — |  |
| 3884 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-002 | denied | decided fresh | — |  |
| 3885 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-004 | permitted | decided fresh | — |  |
| 3886 | Declare the agent loop limit numerically with its units | FL-FG-004 | permitted | decided fresh | — |  |
| 3887 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | permitted | decided fresh | — | ● |
| 3888 | Point the canary tier at a checkpoint that was never registered | FL-MB-006 | denied | decided fresh | — |  |
| 3889 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-001 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 3890 | State turns rather than seconds as the loop-limit unit | FL-FG-002 | permitted | decided fresh | — |  |
| 3891 | Declare the arrival distribution used in the throughput benchmark | FL-IN-005 | permitted | decided fresh | — |  |
| 3892 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-003 | permitted with conditions | decided fresh | — | ● |
| 3893 | Record the capability-threshold determination on the release record | FL-SF-008 | permitted | decided fresh | — |  |
| 3894 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 3895 | Enable batch invariance before claiming bitwise replay | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3896 | Declare the arrival distribution used in the throughput benchmark | FL-IN-008 | permitted | docketed — not charged | — |  |
| 3897 | Separate the production prompt label from its version string | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 3898 | Let the agent mark the failing provenance test as skipped | FL-AG-006 | denied | decided fresh | — |  |
| 3899 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-007 | permitted | disposed by citation | — |  |
| 3900 | Validate tenant scope on every portal export request | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3901 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 3902 | Separate the production prompt label from its version string | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 3903 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-003 | permitted | decided fresh | — |  |
| 3904 | Re-pin the batch scorer to the retired atlas-base hash | FL-MB-001 FL-TD-002 ⛔ | denied | refused at the floor | — |  |
| 3905 | Record the capability-threshold determination on the release record | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 3906 | Embed the canary string in every generated evaluation case | FL-EV-009 | permitted | decided fresh | — |  |
| 3907 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-002 | permitted | decided fresh | — |  |
| 3908 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-002 | permitted | decided fresh | — |  |
| 3909 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-WX-003 | denied | decided fresh | — |  |
| 3910 | Sample the de-identified shard weekly and report the residual rate | FL-PI-002 | permitted | decided fresh | — |  |
| 3911 | Redact prompt and completion logs before they reach retention | FL-PI-002 | permitted | decided fresh | — |  |
| 3912 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TD-007 | denied | decided fresh | — |  |
| 3913 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted | decided fresh | — |  |
| 3914 | Fail closed when a dataset licence string does not parse | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 3915 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — |  |
| 3916 | Give the coding agent its own short-lived signing credential | FL-AG-005 | permitted | decided fresh | — | ● |
| 3917 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-002 | denied | decided fresh | — |  |
| 3918 | Pin the abuse-material hash-list refresh job to a daily schedule | FL-CS-004 | permitted with conditions | decided fresh | — | ● |
| 3919 | Log the named authority for every override exercised | FL-GV-009 | permitted | decided fresh | — |  |
| 3920 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | permitted | decided fresh | — | ● |
| 3921 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 3922 | Document the engine version pinned for each serving tier | FL-IN-005 | permitted | decided fresh | — |  |
| 3923 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-002 | permitted with conditions | decided fresh | — | ● |
| 3924 | Have trade counsel sign the export-classification determination record | FL-WX-003 | permitted | decided fresh | — |  |
| 3925 | Commit the live cluster token into the test fixtures directory | FL-SC-006 | denied | decided fresh | — | ● |
| 3926 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-004 | permitted | decided fresh | — |  |
| 3927 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 3928 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-002 | permitted | decided fresh | — |  |
| 3929 | Keep cases released after the training cutoff in the holdout | FL-EV-005 | permitted with conditions | decided fresh | — | ● |
| 3930 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-004 | permitted | decided fresh | — |  |
| 3931 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — |  |
| 3932 | Hold goodput at the tier threshold under the burst profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 3933 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-002 | permitted | decided fresh | — |  |
| 3934 | Enable batch invariance before claiming bitwise replay | FL-IN-006 | permitted | decided fresh | — |  |
| 3935 | Scope the retrieval index to the tenant boundary at query time | FL-PV-001 | permitted | decided fresh | — |  |
| 3936 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-001 | permitted | decided fresh | — |  |
| 3937 | Record the licence class for every corpus the crawler ingests | FL-TD-007 | permitted | decided fresh | — |  |
| 3938 | Record the availability type on every newly onboarded source | FL-TD-005 | permitted | decided fresh | — |  |
| 3939 | Require human confirmation before the agent executes a write tool | FL-LS-004 | permitted | decided fresh | — |  |
| 3940 | Record a disposition for every referral the board acknowledges | FL-GV-008 | permitted | decided fresh | — |  |
| 3941 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | decided fresh | — |  |
| 3942 | Reject unexpected content types on the tool-callback endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 3943 | Fail the build on scan findings above the severity threshold | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 3944 | Give every system prompt an immutable version identifier | FL-MB-007 | permitted | decided fresh | — |  |
| 3945 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-007 | permitted | decided fresh | — |  |
| 3946 | List only the instruct parent on the merged checkpoint card | FL-MB-008 | denied | decided fresh | — |  |
| 3947 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-010 | denied | decided fresh | — |  |
| 3948 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 3949 | Enforce the instruction and data boundary on the retrieval path | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 3950 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted | decided fresh | — |  |
| 3951 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-002 | permitted with conditions | decided fresh | — | ● |
| 3952 | Disable the government-request log for the bulk export tool | FL-PV-004 | denied | decided fresh | — | ● |
| 3953 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 3954 | Run licence detection over every agent-authored file | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 3955 | Recompute the root digest from resource digests before promotion | FL-MB-005 | permitted | disposed by citation | — |  |
| 3956 | Loosen the toxicity cut-off in the gate config to clear the backlog | FL-BS-006 | denied | decided fresh | — |  |
| 3957 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-004 | permitted | decided fresh | — |  |
| 3958 | Declare both base models in the merged cirrus-small manifest | FL-MB-004 | permitted | decided fresh | — |  |
| 3959 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 3960 | Scan responses for canary tokens before they leave the gateway | FL-LS-011 | permitted | decided fresh | — |  |
| 3961 | Require human confirmation before the agent executes a write tool | FL-LS-011 | permitted | decided fresh | — |  |
| 3962 | Pin the key-value cache budget for the agentic serving tier | FL-IN-005 | permitted | decided fresh | — |  |
| 3963 | Declare the arrival distribution used in the throughput benchmark | FL-IN-002 | permitted | decided fresh | — |  |
| 3964 | Record a lawful basis for each conversation-data source | FL-PI-006 | permitted with conditions | decided fresh | — | ● |
| 3965 | Scan responses for canary tokens before they leave the gateway | FL-LS-003 | permitted | decided fresh | — |  |
| 3966 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-005 | permitted | decided fresh | — |  |
| 3967 | Release the run record with the threshold determination left blank | FL-SF-008 | denied | decided fresh | — |  |
| 3968 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 3969 | Update the third-party licence inventory with this dependency change | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 3970 | Publish a review checklist for agent changes to the eval harness | FL-AG-006 | permitted | decided fresh | — | ● |
| 3971 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 3972 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — | ● |
| 3973 | Record verifiable parental consent on the child-data ingestion record | FL-CS-004 | permitted | decided fresh | — |  |
| 3974 | Gate external evaluator access on the signed agreement | FL-SF-007 | permitted | decided fresh | — |  |
| 3975 | Pipe the model's suggested shell command straight into the runner | FL-LS-010 | denied | decided fresh | — |  |
| 3976 | Reject imports for packages first published within thirty days | FL-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3977 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 3978 | Hold verbatim third-party reproduction below the span threshold | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3979 | Run licence detection over every agent-authored file | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 3980 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-010 | permitted with conditions | decided fresh | — | ● |
| 3981 | Publish the notice file alongside each inference-engine release | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3982 | Export the rulebook without the standing declaration block | FL-GV-005 | denied | decided fresh | — |  |
| 3983 | Cut the incident-severity form down to the fields the reporting clock actually reads | FL-TR-003 | permitted with conditions | decided fresh | — | ● |
| 3984 | Enforce the instruction and data boundary on the retrieval path | FL-LS-007 | permitted | decided fresh | — |  |
| 3985 | Declare the downstream sink for every model output field | FL-LS-007 | permitted | decided fresh | — |  |
| 3986 | Propagate attribution obligations from corpus records to release notes | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 3987 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-002 FL-EV-004 ⛔ | denied | refused at the floor | — |  |
| 3988 | Enable batch invariance before claiming bitwise replay | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 3989 | Re-run the probe after the distillation step, not before it | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 3990 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 3991 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 3992 | Run the tensor leak check after warm-up in the nightly profile | — | permitted | docketed — nothing engaged | — |  |
| 3993 | Add an incident-reporting path test against the statutory clock | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 3994 | Move retrieved documents into a separate, clearly marked context block | FL-LS-010 | permitted | decided fresh | — |  |
| 3995 | Scan responses for canary tokens before they leave the gateway | FL-LS-010 | permitted | decided fresh | — |  |
| 3996 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | permitted | decided fresh | — |  |
| 3997 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | decided fresh | — |  |
| 3998 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted | decided fresh | — |  |
| 3999 | Blend the share-alike corpus into the proprietary preference set | FL-TD-007 | denied | decided fresh | — |  |
| 4000 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-001 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 4001 | Enforce server-side authorization on the new batch endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4002 | Open the agentic tier to customers while the safety case is in draft | FL-SF-007 | denied | decided fresh | — |  |
| 4003 | Give the coding agent its own short-lived signing credential | FL-AG-007 | permitted | disposed by citation | — |  |
| 4004 | Publish a review checklist for agent changes to the eval harness | FL-AG-006 | permitted | decided fresh | — |  |
| 4005 | Raise mitigations to match the assessed capability level | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 4006 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-004 | permitted with conditions | decided fresh | — | ● |
| 4007 | Pin workflow actions to commit digests across the release repository | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 4008 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4009 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-003 | permitted | decided fresh | — |  |
| 4010 | Route nonconsensual-imagery takedown requests ahead of the general moderation queue | FL-UH-003 | permitted | decided fresh | — |  |
| 4011 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 4012 | Measure demographic disparity across the ambiguous-context suite | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 4013 | Separate the audit register from the precedent store at schema level | FL-GV-010 | permitted with conditions | decided fresh | — | ● |
| 4014 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted | decided fresh | — |  |
| 4015 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted | decided fresh | — |  |
| 4016 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4017 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-002 FL-WX-003 ⛔ | denied | refused at the floor | — |  |
| 4018 | State the percentile on every latency claim in the dashboard | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4019 | Propagate attribution obligations from corpus records to release notes | FL-TD-006 | permitted | decided fresh | — |  |
| 4020 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-001 FL-FG-006 ⛔ | denied | refused at the floor | — |  |
| 4021 | Run agent-authored code only inside the sandboxed runner | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4022 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-007 | permitted | decided fresh | — |  |
| 4023 | Turn off commit signing for the agent runner while its key rotates | FL-AG-001 FL-PV-001 ⛔ | denied | refused at the floor | — |  |
| 4024 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-003 | permitted | decided fresh | — |  |
| 4025 | Declare the arrival distribution used in the throughput benchmark | FL-IN-004 | permitted | decided fresh | — |  |
| 4026 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-004 | permitted | decided fresh | — |  |
| 4027 | Restrict weight egress to the declared perimeter buckets | FL-SF-008 | permitted | decided fresh | — |  |
| 4028 | Route critical-incident detection signals to the on-call dashboard instead of the reporting queue | FL-TR-004 FL-SF-009 ⛔ | denied | refused at the floor | — |  |
| 4029 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-008 | denied | decided fresh | — |  |
| 4030 | Move the loop-limit requirement out of the rulebook into service defaults | FL-UH-002 | denied | decided fresh | — |  |
| 4031 | Turn off the abuse-material classifier on the image-generation path to cut moderation latency | FL-CS-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 4032 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-005 | denied | decided fresh | — |  |
| 4033 | Bake the build timestamp and hostname into the engine binary | FL-SC-002 | denied | decided fresh | — |  |
| 4034 | Enable batch invariance before claiming bitwise replay | FL-IN-003 | permitted | decided fresh | — |  |
| 4035 | Report preemption counts in the load-test summary | FL-IN-003 | permitted | decided fresh | — |  |
| 4036 | Broaden the refusal trigger list until safe prompts start bouncing | FL-BS-002 | denied | decided fresh | — | ● |
| 4037 | Publish a signed bill of materials covering transitive dependencies | FL-SC-005 | permitted | decided fresh | — | ● |
| 4038 | Reject imports for packages first published within thirty days | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 4039 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | decided fresh | — |  |
| 4040 | Skip propagating erasure requests from the deletion API into the training-manifest sync job | FL-PV-001 | denied | decided fresh | — |  |
| 4041 | Add the new sampling library to the licence inventory | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4042 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 4043 | Hold goodput at the tier threshold under the burst profile | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4044 | Carry attribution notices through to the shipped container image | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4045 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 4046 | Attach Croissant metadata to the new publisher corpus | FL-TD-004 | permitted | decided fresh | — |  |
| 4047 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-001 FL-TD-007 ⛔ | denied | refused at the floor | — |  |
| 4048 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 4049 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted with conditions | decided fresh | — | ● |
| 4050 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted | decided fresh | — |  |
| 4051 | Verify de-identification by sampling rather than by assertion | FL-PI-003 | permitted | decided fresh | — |  |
| 4052 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4053 | Document the subject-request path for the preference store | FL-PI-002 | permitted | decided fresh | — | ● |
| 4054 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4055 | Return a generic error identifier instead of the stack trace | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4056 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-004 | denied | decided fresh | — |  |
| 4057 | Strip annotator identity from the exported preference dataset | FL-PV-002 | permitted with conditions | decided fresh | — | ● |
| 4058 | Add an eval-awareness probe to the pre-release harness run | FL-CB-002 | permitted | decided fresh | — |  |
| 4059 | Pin the catastrophic-risk eval harness version in the release record | FL-CB-002 | permitted | decided fresh | — |  |
| 4060 | Declare sample size and percentile alongside the parity result | FL-EV-003 | permitted | decided fresh | — |  |
| 4061 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4062 | Sign agent commits with a workload identity rather than a person's key | FL-AG-004 | permitted | decided fresh | — |  |
| 4063 | Sign agent commits with a workload identity rather than a person's key | FL-AG-004 | permitted | decided fresh | — |  |
| 4064 | Bake the build timestamp and hostname into the engine binary | FL-SC-004 | denied | decided fresh | — |  |
| 4065 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 4066 | Document which attack class the new defence was evaluated against | FL-LS-006 | permitted | decided fresh | — |  |
| 4067 | Reject artifacts whose served hash differs from the registry entry | FL-MB-007 | permitted | decided fresh | — |  |
| 4068 | Move authorization checks out of the client and into the gateway | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4069 | Add regression coverage for the minor-interaction safeguard suite | FL-CS-003 | permitted with conditions | decided fresh | — | ● |
| 4070 | Pin the key-value cache budget for the agentic serving tier | — | permitted | docketed — nothing engaged | — |  |
| 4071 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted | decided fresh | — |  |
| 4072 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | disposed by citation | — |  |
| 4073 | Onboard the new chat source without running the de-identification sample | FL-PI-005 | denied | decided fresh | — |  |
| 4074 | Pin every dependency to an immutable digest in the lockfile | FL-SC-002 | permitted | disposed by citation | — |  |
| 4075 | Record the capability-threshold determination on the release record | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 4076 | Publish a review checklist for agent changes to the eval harness | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4077 | Fail the build on scan findings above the severity threshold | FL-SC-004 | permitted | decided fresh | — |  |
| 4078 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-003 | permitted with conditions | decided fresh | — | ● |
| 4079 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4080 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-002 | permitted | decided fresh | — |  |
| 4081 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4082 | Re-pin the batch scorer to the retired atlas-base hash | FL-MB-006 | denied | decided fresh | — |  |
| 4083 | Justify the two remaining special-category fields on the dataset record | FL-PI-006 | permitted | decided fresh | — |  |
| 4084 | Publish the prompt-log retention clock in the customer portal | FL-PI-006 | permitted | decided fresh | — |  |
| 4085 | State the percentile on every latency claim in the dashboard | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4086 | Route child-directed service logs into the general-purpose training-corpus builder | FL-CS-003 | denied | decided fresh | — | ● |
| 4087 | Declare both base models in the merged cirrus-small manifest | FL-MB-005 | permitted | decided fresh | — | ● |
| 4088 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted | decided fresh | — |  |
| 4089 | Record a lawful basis for each conversation-data source | FL-PI-005 | permitted | decided fresh | — |  |
| 4090 | Gate promotion on the full safety suite, not the fast subset | FL-EV-005 | permitted | decided fresh | — |  |
| 4091 | Gate promotion on the full safety suite, not the fast subset | FL-EV-005 | permitted | decided fresh | — |  |
| 4092 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4093 | Release the run record with the threshold determination left blank | FL-SF-003 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 4094 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4095 | Restrict agent outbound calls to the allowlisted host set | FL-AG-004 | denied | bound by precedent | REC-S0129 |  |
| 4096 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-008 | denied | decided fresh | — |  |
| 4097 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 4098 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — |  |
| 4099 | Reject artifacts whose served hash differs from the registry entry | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 4100 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | permitted | decided fresh | — |  |
| 4101 | Record the frontier framework version in force on the release record | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 4102 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-003 | permitted | decided fresh | — |  |
| 4103 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-007 | denied | decided fresh | — | ● |
| 4104 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4105 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-003 | permitted | decided fresh | — |  |
| 4106 | Run release builds on ephemeral runners with pinned images | FL-SC-007 | permitted | decided fresh | — |  |
| 4107 | Publish the notice file alongside each inference-engine release | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4108 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | decided fresh | — |  |
| 4109 | Backfill lineage records for the older quantised checkpoints | FL-MB-007 | permitted | decided fresh | — |  |
| 4110 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 4111 | Attach Croissant metadata to the new publisher corpus | FL-TD-002 | permitted | decided fresh | — |  |
| 4112 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted | decided fresh | — |  |
| 4113 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-002 | permitted with conditions | decided fresh | — | ● |
| 4114 | Ship the image whose layer digests no longer match the recorded inventory | FL-SC-002 | denied | decided fresh | — |  |
| 4115 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh | — |  |
| 4116 | Edit the toxicity threshold directly through the adjudication service credentials | FL-SC-002 | denied | decided fresh | — |  |
| 4117 | Pin the golden-prompt baseline to a commit digest | FL-EV-004 | permitted | decided fresh | — |  |
| 4118 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-004 | permitted | decided fresh | — |  |
| 4119 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-003 FL-MB-004 ⛔ | denied | refused at the floor | — |  |
| 4120 | Declare the carrier channel for each untrusted input source | FL-LS-009 | permitted | decided fresh | — |  |
| 4121 | Pin workflow actions to commit digests across the release repository | FL-SC-005 | permitted | decided fresh | — |  |
| 4122 | Keep reporter bulletins off the adjudication input path | FL-GV-010 | permitted | decided fresh | — |  |
| 4123 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-001 FL-PI-006 ⛔ | denied | refused at the floor | — |  |
| 4124 | Restrict deserialisation to the declared tool-payload types | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4125 | Block internal address ranges in the web-fetch tool | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4126 | Move retrieved documents into a separate, clearly marked context block | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 4127 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 4128 | Hold goodput at the tier threshold under the burst profile | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 4129 | Record the licence class for every corpus the crawler ingests | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 4130 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4131 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted | decided fresh | — |  |
| 4132 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4133 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-005 | permitted | decided fresh | — |  |
| 4134 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-005 | permitted | decided fresh | — |  |
| 4135 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4136 | Report preemption counts in the load-test summary | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4137 | Enforce server-side authorization on the new batch endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4138 | Report refusal and over-refusal rates side by side | FL-BS-003 | permitted | decided fresh | — |  |
| 4139 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4140 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4141 | Loosen the toxicity cut-off in the gate config to clear the backlog | FL-BS-005 | denied | decided fresh | — |  |
| 4142 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4143 | Record the frontier framework version in force on the release record | FL-SF-006 | permitted | decided fresh | — |  |
| 4144 | Restrict weight egress to the declared perimeter buckets | FL-SF-006 | permitted | decided fresh | — |  |
| 4145 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 4146 | Hardcode the critical-incident reporting deadline into the reporting-queue config | FL-TR-003 | permitted | decided fresh | — |  |
| 4147 | Write a docket entry for every arrival that is not charged | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 4148 | Make the government-request log append-only across the bulk-export path | FL-PV-002 | permitted | decided fresh | — |  |
| 4149 | Add the new sampling library to the licence inventory | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 4150 | Declare the arrival distribution used in the throughput benchmark | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4151 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4152 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4153 | Enable the new sampler that slows per-token output beyond budget | FL-IN-001 | denied | decided fresh | — |  |
| 4154 | Declare the carrier channel for each untrusted input source | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4155 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4156 | Route parameter changes through the amendment workflow instead | FL-GV-009 | permitted | decided fresh | — |  |
| 4157 | Point the canary tier at a checkpoint that was never registered | FL-MB-006 | denied | decided fresh | — |  |
| 4158 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted | decided fresh | — |  |
| 4159 | Require two-person authorisation for unreleased-weight access | FL-SF-006 | permitted | decided fresh | — |  |
| 4160 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-005 | permitted | decided fresh | — |  |
| 4161 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | permitted | decided fresh | — |  |
| 4162 | Replace the companion persona's static disclosure line with one rendered per session | FL-UH-005 | permitted | decided fresh | — |  |
| 4163 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 4164 | Retire two supply-chain provisions from the rulebook manifest | FL-LS-009 | denied | decided fresh | — |  |
| 4165 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4166 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-003 | permitted | decided fresh | — |  |
| 4167 | Strip internal identifiers from gateway error responses | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4168 | Test marking survivability across the video transcoder's re-encode step | FL-TR-002 | permitted with conditions | decided fresh | — | ● |
| 4169 | Edit the toxicity threshold directly through the adjudication service credentials | FL-SF-008 | denied | decided fresh | — |  |
| 4170 | Make the breaker unreachable from the agent's own configuration | FL-FG-003 | permitted | decided fresh | — |  |
| 4171 | Put a circuit breaker on the recursive summarisation path | FL-FG-003 | permitted | decided fresh | — |  |
| 4172 | Record attribution for the reused tokenizer snippet | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4173 | Hide the human override behind a flag that ships off | FL-GV-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 4174 | Enable batch invariance before claiming bitwise replay | FL-IN-001 | permitted | decided fresh | — |  |
| 4175 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-009 | permitted | decided fresh | — | ● |
| 4176 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-003 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 4177 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-001 FL-FG-002 ⛔ | denied | refused at the floor | — |  |
| 4178 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 4179 | Export the rulebook without the standing declaration block | FL-GV-002 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 4180 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 4181 | Check persona guidance against the shipped system prompt | FL-BS-004 | permitted | decided fresh | — |  |
| 4182 | Measure judge and human agreement for the new grader configuration | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 4183 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted | decided fresh | — |  |
| 4184 | Add a weekly sampling job over production refusals | FL-BS-006 | permitted | decided fresh | — |  |
| 4185 | Regenerate the golden prompts from the current model's own answers | FL-EV-010 | denied | decided fresh | — |  |
| 4186 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4187 | Record a lawful basis for each conversation-data source | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 4188 | Pin every dependency to an immutable digest in the lockfile | FL-SC-004 | permitted | decided fresh | — |  |
| 4189 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-004 | permitted | decided fresh | — |  |
| 4190 | Require the safety-case signature from outside the authoring team | FL-SF-009 | permitted | decided fresh | — |  |
| 4191 | Report first-token and per-token latency against the tier budgets | FL-IN-005 | permitted | decided fresh | — |  |
| 4192 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh | — |  |
| 4193 | Give the coding agent its own short-lived signing credential | FL-AG-007 | permitted | decided fresh | — |  |
| 4194 | Hold goodput at the tier threshold under the burst profile | FL-IN-005 | permitted | decided fresh | — |  |
| 4195 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-004 | denied | decided fresh | — |  |
| 4196 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-005 | permitted | decided fresh | — |  |
| 4197 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 4198 | Require two-person authorisation for unreleased-weight access | FL-SF-007 | permitted | decided fresh after a tie | none_tie |  |
| 4199 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-002 | denied | decided fresh | — |  |
| 4200 | Report preemption counts in the load-test summary | FL-IN-006 | permitted | decided fresh | — |  |
| 4201 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-003 | permitted | decided fresh | — |  |
| 4202 | Inline retrieved documents into the system prompt to save tokens | FL-LS-001 FL-BS-005 ⛔ | denied | refused at the floor | — |  |
| 4203 | Propagate attribution obligations from corpus records to release notes | FL-TD-006 | permitted | decided fresh | — |  |
| 4204 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 4205 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-001 FL-LS-004 ⛔ | denied | refused at the floor | — |  |
| 4206 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh | — |  |
| 4207 | Record the availability type on every newly onboarded source | FL-TD-005 | permitted | decided fresh | — |  |
| 4208 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 4209 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | decided fresh | — |  |
| 4210 | Fail the build on scan findings above the severity threshold | FL-SC-002 | permitted | decided fresh | — |  |
| 4211 | Register the new fused kernel as a nondeterministic operation | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4212 | Publish the notice file alongside each inference-engine release | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 4213 | Attach Croissant metadata to the new publisher corpus | FL-TD-007 | permitted | decided fresh after a tie | none_tie |  |
| 4214 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted | decided fresh | — |  |
| 4215 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-001 FL-UH-002 ⛔ | denied | refused at the floor | — |  |
| 4216 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-011 | permitted | decided fresh | — |  |
| 4217 | Batch the mandatory-reporting webhook into a nightly job instead of firing per match | FL-CS-003 | denied | decided fresh | — | ● |
| 4218 | Pin the golden-prompt baseline to a commit digest | FL-EV-003 | permitted with conditions | decided fresh | — | ● |
| 4219 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | decided fresh | — |  |
| 4220 | Pin the key-value cache budget for the agentic serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 4221 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted | decided fresh | — |  |
| 4222 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-007 | permitted | decided fresh | — |  |
| 4223 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-003 | permitted | decided fresh | — |  |
| 4224 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 4225 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4226 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4227 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 4228 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 4229 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-002 | permitted | decided fresh | — |  |
| 4230 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-004 | permitted | decided fresh | — |  |
| 4231 | Register the new fused kernel as a nondeterministic operation | FL-IN-006 | permitted | decided fresh | — |  |
| 4232 | Fail closed when a dataset licence string does not parse | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 4233 | Give every system prompt an immutable version identifier | FL-MB-007 | permitted | disposed by citation | — |  |
| 4234 | Declare the downstream sink for every model output field | FL-LS-004 | permitted | decided fresh | — |  |
| 4235 | Exercise injection detection on the changed tool-calling path | FL-LS-004 | permitted | decided fresh | — |  |
| 4236 | Publish a signed bill of materials covering transitive dependencies | FL-SC-006 | permitted | decided fresh | — |  |
| 4237 | Fuzz the changed completions parameters before release | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4238 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-002 ⛔ | denied | refused at the floor | — |  |
| 4239 | Run the memorisation probe on the release candidate | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 4240 | Carry attribution notices through to the shipped container image | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4241 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-003 | permitted | decided fresh | — |  |
| 4242 | Pin the key-value cache budget for the agentic serving tier | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 4243 | Record the frontier framework version in force on the release record | FL-SF-008 | permitted | decided fresh | — |  |
| 4244 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted | decided fresh | — |  |
| 4245 | Add a sandbagging detector to the eval harness's promotion checks | FL-CB-002 | permitted | decided fresh | — |  |
| 4246 | Block internal address ranges in the web-fetch tool | — | permitted | docketed — nothing engaged | — |  |
| 4247 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 4248 | Require an independent reviewer's sign-off on every threshold determination | FL-CB-002 | permitted | decided fresh | — |  |
| 4249 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-005 | permitted | decided fresh | — |  |
| 4250 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted | decided fresh | — | ● |
| 4251 | Report first-token and per-token latency against the tier budgets | FL-IN-005 | permitted | decided fresh | — |  |
| 4252 | Declare the arrival distribution used in the throughput benchmark | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 4253 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | disposed by citation | — |  |
| 4254 | Separate the production prompt label from its version string | FL-MB-006 | permitted | decided fresh | — |  |
| 4255 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 4256 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 4257 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted | decided fresh | — |  |
| 4258 | Pin workflow actions to commit digests across the release repository | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 4259 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-011 | permitted | decided fresh | — |  |
| 4260 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-011 | permitted | decided fresh | — |  |
| 4261 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-005 | permitted | decided fresh | — |  |
| 4262 | Check agent diffs for structural matches against known libraries | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4263 | Name a data-governance custodian on each dataset record | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 4264 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-008 | permitted | decided fresh | — |  |
| 4265 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted | decided fresh | — |  |
| 4266 | Fail closed when a dataset licence string does not parse | FL-TD-004 | permitted | decided fresh | — |  |
| 4267 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-002 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 4268 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-002 | permitted | decided fresh | — |  |
| 4269 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4270 | Remove the graphic-content exposure limits from the labeling-queue config | FL-PV-002 | denied | decided fresh | — |  |
| 4271 | Publish the prompt-log retention clock in the customer portal | FL-PI-004 | permitted | decided fresh | — | ● |
| 4272 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 4273 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4274 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 4275 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 4276 | Strip internal identifiers from gateway error responses | — | permitted | docketed — nothing engaged | — |  |
| 4277 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 4278 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4279 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 4280 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-003 | denied | decided fresh | — |  |
| 4281 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-FG-002 | denied | decided fresh | — |  |
| 4282 | Strip internal identifiers from gateway error responses | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4283 | Escape tool output before it reaches the shell adapter | FL-LS-007 | permitted | decided fresh | — |  |
| 4284 | Require human confirmation before the agent executes a write tool | FL-LS-007 | permitted | decided fresh | — |  |
| 4285 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 4286 | Restrict agent outbound calls to the allowlisted host set | FL-AG-004 | permitted | decided fresh | — |  |
| 4287 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | decided fresh | — |  |
| 4288 | Publish the signing certificate chain alongside each release digest | FL-MB-004 | permitted | decided fresh | — |  |
| 4289 | Verify de-identification by sampling rather than by assertion | FL-PI-004 | permitted with conditions | decided fresh | — | ● |
| 4290 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 4291 | Run licence detection over every agent-authored file | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4292 | Compare the provenance subject digest to the distributed artifact | FL-SC-003 | permitted | decided fresh | — |  |
| 4293 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted | decided fresh | — |  |
| 4294 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4295 | Propose allowing sampled rather than exhaustive licence detection | FL-GV-007 | denied | decided fresh | — |  |
| 4296 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | permitted | decided fresh | — |  |
| 4297 | Record a lawful basis for each conversation-data source | FL-PI-002 | permitted | decided fresh | — |  |
| 4298 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4299 | Gate promotion on the full safety suite, not the fast subset | FL-EV-007 | permitted with conditions | decided fresh | — | ● |
| 4300 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-003 | denied | decided fresh | — |  |
| 4301 | Register the new fused kernel as a nondeterministic operation | FL-IN-004 | permitted | decided fresh | — |  |
| 4302 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4303 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 4304 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | permitted | decided fresh | — |  |
| 4305 | Pin the golden-prompt baseline to a commit digest | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 4306 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-009 | denied | decided fresh | — | ● |
| 4307 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 4308 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 4309 | Report preemption counts in the load-test summary | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 4310 | Sign agent commits with a workload identity rather than a person's key | FL-AG-006 | permitted | decided fresh | — |  |
| 4311 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | decided fresh | — |  |
| 4312 | Make decision records append-only in the store schema | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 4313 | Check agent diffs for structural matches against known libraries | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4314 | Fail the build on scan findings above the severity threshold | FL-SC-007 | permitted | decided fresh | — | ● |
| 4315 | Restore the withdrawn scraped-book shard into the pretraining mix | FL-TD-001 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 4316 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4317 | Publish the signing certificate chain alongside each release digest | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 4318 | Ship the checkpoint past the uplift screen while the mitigation package is still in draft | FL-CB-001 FL-AG-004 ⛔ | denied | refused at the floor | — |  |
| 4319 | Stop reading the loop limit from an environment variable | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 4320 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-002 | permitted | decided fresh | — |  |
| 4321 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4322 | Commit the live cluster token into the test fixtures directory | FL-SC-003 | denied | decided fresh | — |  |
| 4323 | Repack the shard files after signing and reuse the old manifest | FL-MB-001 FL-SC-004 ⛔ | denied | refused at the floor | — |  |
| 4324 | Fuzz the changed completions parameters before release | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4325 | Advertise bitwise replay while batch invariance stays off in production | FL-IN-004 | denied | decided fresh | — |  |
| 4326 | Batch the mandatory-reporting webhook into a nightly job instead of firing per match | FL-CS-003 | denied | decided fresh | — |  |
| 4327 | Give every system prompt an immutable version identifier | FL-MB-006 | permitted | decided fresh | — |  |
| 4328 | Reject imports for packages first published within thirty days | FL-AG-005 | permitted | decided fresh | — |  |
| 4329 | Collapse the two compute thresholds into a single configuration field | FL-GV-003 FL-EV-010 ⛔ | denied | refused at the floor | — |  |
| 4330 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4331 | Resolve internal packages from the private registry first | FL-SC-008 | permitted | decided fresh | — |  |
| 4332 | Fail the build on scan findings above the severity threshold | FL-SC-008 | permitted | decided fresh | — |  |
| 4333 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4334 | Strip internal identifiers from gateway error responses | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4335 | Run the personal-data scan on every new training shard | FL-PI-003 | permitted | decided fresh | — |  |
| 4336 | Justify the two remaining special-category fields on the dataset record | FL-PI-003 | permitted | decided fresh | — |  |
| 4337 | Require the safety-case signature from outside the authoring team | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 4338 | Add hash-list refresh monitoring to the training ingestion dashboard | FL-CS-003 | permitted | decided fresh | — |  |
| 4339 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 4340 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh | — |  |
| 4341 | Make decision records append-only in the store schema | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 4342 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-004 | permitted | decided fresh | — |  |
| 4343 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-004 | permitted | decided fresh | — |  |
| 4344 | Fail the build on scan findings above the severity threshold | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 4345 | Sign agent commits with a workload identity rather than a person's key | FL-AG-004 | permitted | disposed by citation | — |  |
| 4346 | Record the frontier framework version in force on the release record | FL-SF-008 | permitted | decided fresh | — |  |
| 4347 | Reject imports for packages first published within thirty days | FL-AG-008 | permitted | disposed by citation | — |  |
| 4348 | Publish the signing certificate chain alongside each release digest | FL-MB-007 | permitted | decided fresh | — | ● |
| 4349 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted | decided fresh after a tie | none_tie |  |
| 4350 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4351 | Require human confirmation before the agent executes a write tool | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4352 | Escape tool output before it reaches the shell adapter | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4353 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4354 | Name a data-governance custodian on each dataset record | FL-TD-002 | permitted | decided fresh | — |  |
| 4355 | Publish the signing certificate chain alongside each release digest | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 4356 | Register the new fused kernel as a nondeterministic operation | FL-IN-005 | permitted | decided fresh | — |  |
| 4357 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 4358 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4359 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-009 | permitted | disposed by citation | — |  |
| 4360 | Report preemption counts in the load-test summary | FL-IN-003 | permitted | decided fresh | — |  |
| 4361 | Enable batch invariance before claiming bitwise replay | FL-IN-003 | permitted | decided fresh | — |  |
| 4362 | Restrict weight egress to the declared perimeter buckets | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 4363 | Declare the arrival distribution used in the throughput benchmark | FL-IN-003 | permitted | decided fresh | — |  |
| 4364 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-001 FL-LS-011 ⛔ | denied | refused at the floor | — |  |
| 4365 | Run release builds on ephemeral runners with pinned images | FL-SC-008 | permitted | disposed by citation | — |  |
| 4366 | Run the memorisation probe on the release candidate | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4367 | Shorten the safety-incident retention clause in the policy repository | FL-LS-009 | denied | decided fresh | — |  |
| 4368 | Declare the carrier channel for each untrusted input source | FL-LS-003 | permitted | decided fresh | — |  |
| 4369 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-001 FL-GV-009 ⛔ | denied | refused at the floor | — |  |
| 4370 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — |  |
| 4371 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 4372 | Run the memorisation probe on the release candidate | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4373 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-002 | permitted | decided fresh | — |  |
| 4374 | Return a generic error identifier instead of the stack trace | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4375 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4376 | Record the licence class for every corpus the crawler ingests | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 4377 | Separate the production prompt label from its version string | FL-MB-007 | permitted | decided fresh | — |  |
| 4378 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 4379 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-002 | permitted | decided fresh | — |  |
| 4380 | Hide the human override behind a flag that ships off | FL-GV-008 | denied | decided fresh | — |  |
| 4381 | Hold the audit register in a store the retrieval path cannot read | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 4382 | Verify de-identification by sampling rather than by assertion | FL-PI-004 | permitted with conditions | decided fresh | — | ● |
| 4383 | Change the escalation ladder so an automated tier may accept frontier risk | FL-GV-009 | denied | decided fresh | — |  |
| 4384 | Raise mitigations to match the assessed capability level | FL-SF-008 | permitted | decided fresh | — |  |
| 4385 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted | decided fresh | — |  |
| 4386 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 4387 | Log every read of the weights store to the perimeter audit trail | FL-SF-005 | permitted | decided fresh | — |  |
| 4388 | Register the new fused kernel as a nondeterministic operation | FL-IN-003 | permitted | decided fresh | — |  |
| 4389 | Publish a review checklist for agent changes to the eval harness | FL-AG-004 | denied | bound by precedent | REC-S0129 |  |
| 4390 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-001 FL-TR-002 ⛔ | denied | refused at the floor | — |  |
| 4391 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4392 | Remove the canary check from the response filter to cut latency | FL-LS-001 FL-SF-004 ⛔ | denied | refused at the floor | — |  |
| 4393 | Update the third-party licence inventory with this dependency change | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 4394 | Register the new fused kernel as a nondeterministic operation | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4395 | Verify provenance against the expected builder identity before deploy | FL-SC-002 | permitted | disposed by citation | — |  |
| 4396 | Publish a review checklist for agent changes to the eval harness | FL-AG-008 | permitted | decided fresh | — | ● |
| 4397 | Deploy the model line before the transparency report is published | FL-TR-003 | denied | decided fresh | — |  |
| 4398 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4399 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-001 | permitted | decided fresh | — |  |
| 4400 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-001 | permitted | decided fresh | — |  |
| 4401 | Propose an amendment codifying coverage rules for generated eval configs | FL-MB-009 | denied | decided fresh | — |  |
| 4402 | Respect the robots.txt AI directive in the web crawler | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 4403 | Add a weekly sampling job over production refusals | FL-BS-006 | permitted | decided fresh | — |  |
| 4404 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-009 | permitted | disposed by citation | — |  |
| 4405 | Fail the merge when the scanner reports an unresolved licence | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4406 | Declare both base models in the merged cirrus-small manifest | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 4407 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4408 | Ship the persona fine-tune whose disparity scores sit above the bar | FL-BS-005 | denied | decided fresh | — | ● |
| 4409 | Test marking survivability across the video transcoder's re-encode step | FL-TR-002 | permitted | decided fresh | — |  |
| 4410 | Refresh the model card and GPAI documentation ahead of every release cut | FL-TR-002 | permitted | decided fresh | — |  |
| 4411 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 4412 | Run the personal-data scan on every new training shard | FL-PI-004 | permitted | decided fresh | — |  |
| 4413 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-003 FL-CS-003 ⛔ | denied | refused at the floor | — |  |
| 4414 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4415 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-007 | denied | decided fresh | — |  |
| 4416 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-006 | permitted | decided fresh | — | ● |
| 4417 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-005 | permitted | decided fresh | — |  |
| 4418 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | decided fresh | — |  |
| 4419 | Inline retrieved documents into the system prompt to save tokens | FL-LS-005 | denied | decided fresh | — |  |
| 4420 | Let the mail agent follow instructions it finds in the message body | FL-LS-005 | denied | decided fresh | — |  |
| 4421 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 4422 | Run licence detection over every agent-authored file | FL-IP-005 | permitted | decided fresh | — |  |
| 4423 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 4424 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4425 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted | decided fresh after a tie | none_tie |  |
| 4426 | Gate promotion on the full safety suite, not the fast subset | FL-EV-004 | permitted | bound by precedent | REC-S0119 |  |
| 4427 | Turn off commit signing for the agent runner while its key rotates | FL-AG-007 | denied | decided fresh | — | ● |
| 4428 | Propagate attribution obligations from corpus records to release notes | FL-TD-004 | permitted | decided fresh | — |  |
| 4429 | Document which attack class the new defence was evaluated against | FL-LS-005 | permitted | decided fresh | — |  |
| 4430 | Fail closed when a dataset licence string does not parse | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 4431 | Enforce server-side authorization on the new batch endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4432 | Run release builds on ephemeral runners with pinned images | FL-SC-002 | permitted | disposed by citation | — |  |
| 4433 | Name a data-governance custodian on each dataset record | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4434 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-008 | permitted | decided fresh | — |  |
| 4435 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | decided fresh | — |  |
| 4436 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 4437 | Exclude special-category fields from the support-transcript schema | FL-PI-004 | permitted | decided fresh | — |  |
| 4438 | Accept attestations from the personal runner that built the hotfix | FL-SC-005 | denied | decided fresh | — |  |
| 4439 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4440 | Pin the golden-prompt baseline to a commit digest | FL-EV-006 | permitted | decided fresh | — |  |
| 4441 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted | decided fresh | — |  |
| 4442 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted | decided fresh | — | ● |
| 4443 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-EV-009 | denied | decided fresh | — |  |
| 4444 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-005 | denied | decided fresh | — |  |
| 4445 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 FL-GV-005 ⛔ | denied | refused at the floor | — |  |
| 4446 | Exclude special-category fields from the support-transcript schema | FL-PI-003 | permitted with conditions | decided fresh | — | ● |
| 4447 | Give the coding agent its own short-lived signing credential | FL-AG-007 | permitted | decided fresh | — |  |
| 4448 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh | — |  |
| 4449 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 4450 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 4451 | Turn off egress monitoring on the weight store during the migration window | FL-WX-001 FL-TD-002 ⛔ | denied | refused at the floor | — |  |
| 4452 | Pin workflow actions to commit digests across the release repository | FL-SC-003 | permitted | decided fresh | — |  |
| 4453 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-001 | permitted | decided fresh | — |  |
| 4454 | Require a human reviewer on agent changes to request routing | FL-AG-005 | permitted | decided fresh | — |  |
| 4455 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-005 | permitted | decided fresh | — |  |
| 4456 | Recompute the root digest from resource digests before promotion | FL-MB-007 | permitted | decided fresh | — |  |
| 4457 | Escape tool output before it reaches the shell adapter | FL-LS-010 | permitted | decided fresh | — |  |
| 4458 | Bind the research agent's quota to its cost centre | FL-FG-004 | permitted | decided fresh | — |  |
| 4459 | Accept attestations from the personal runner that built the hotfix | FL-SC-001 FL-SC-003 ⛔ | denied | refused at the floor | — |  |
| 4460 | Bind the research agent's quota to its cost centre | FL-FG-005 | permitted | decided fresh | — |  |
| 4461 | Make the breaker unreachable from the agent's own configuration | FL-FG-005 | permitted | decided fresh | — |  |
| 4462 | Pin the key-value cache budget for the agentic serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4463 | Cover the new administrative routes in the authorization test suite | — | permitted | docketed — nothing engaged | — |  |
| 4464 | Hold the audit register in a store the retrieval path cannot read | FL-GV-006 | permitted | decided fresh | — |  |
| 4465 | Separate the audit register from the precedent store at schema level | FL-GV-006 | permitted | decided fresh | — |  |
| 4466 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 4467 | Report preemption counts in the load-test summary | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 4468 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted | decided fresh | — |  |
| 4469 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-008 | permitted | decided fresh | — |  |
| 4470 | Open the agentic tier to customers while the safety case is in draft | FL-SF-001 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 4471 | Enforce vetting-record expiry automatically in the access-control system | FL-WX-003 | permitted | decided fresh | — |  |
| 4472 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted | decided fresh | — |  |
| 4473 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-001 | permitted | decided fresh | — |  |
| 4474 | Hold verbatim third-party reproduction below the span threshold | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 4475 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | decided fresh | — | ● |
| 4476 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4477 | Declare the arrival distribution used in the throughput benchmark | FL-IN-006 | permitted | decided fresh | — |  |
| 4478 | Respect the robots.txt AI directive in the web crawler | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4479 | Sample the de-identified shard weekly and report the residual rate | FL-PI-006 | permitted with conditions | decided fresh | — | ● |
| 4480 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted | decided fresh | — |  |
| 4481 | Run the memorisation probe on the release candidate | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4482 | Blend the share-alike corpus into the proprietary preference set | FL-TD-002 | denied | decided fresh | — |  |
| 4483 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 4484 | Check every new import against the upstream registry before build | FL-AG-005 | permitted | decided fresh | — |  |
| 4485 | Alert when an agent run crosses eighty percent of its budget | FL-FG-004 | permitted | decided fresh | — |  |
| 4486 | State turns rather than seconds as the loop-limit unit | FL-FG-004 | permitted | decided fresh | — |  |
| 4487 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4488 | Raise the batch size to a setting that preempts at target load | FL-IN-002 | denied | decided fresh | — |  |
| 4489 | Open the agentic tier to customers while the safety case is in draft | FL-SF-001 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 4490 | Redact prompt and completion logs before they reach retention | FL-PI-002 | permitted | decided fresh | — |  |
| 4491 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-002 | denied | decided fresh | — |  |
| 4492 | Run the personal-data scan on every new training shard | FL-PI-003 | permitted | decided fresh | — |  |
| 4493 | Record the prompt and context hash on each agent commit | FL-AG-004 | permitted | decided fresh | — |  |
| 4494 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | decided fresh | — |  |
| 4495 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted | decided fresh | — |  |
| 4496 | Repack the shard files after signing and reuse the old manifest | FL-MB-007 | denied | decided fresh | — | ● |
| 4497 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | permitted | decided fresh | — |  |
| 4498 | Let the team requesting release sign off its own threshold determination | FL-CB-002 | denied | decided fresh | — |  |
| 4499 | Cover the new administrative routes in the authorization test suite | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4500 | Bake the build timestamp and hostname into the engine binary | FL-SC-001 FL-EV-004 ⛔ | denied | refused at the floor | — |  |
| 4501 | Declare the downstream sink for every model output field | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4502 | File a draft amendment carving out build-time-only dependencies | FL-IN-003 | denied | decided fresh | — |  |
| 4503 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4504 | Enforce server-side authorization on the new batch endpoint | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4505 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | decided fresh | — |  |
| 4506 | Accept attestations from the personal runner that built the hotfix | FL-SC-001 FL-CB-002 ⛔ | denied | refused at the floor | — |  |
| 4507 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-002 | denied | decided fresh | — |  |
| 4508 | Recompute the root digest from resource digests before promotion | FL-MB-006 | permitted | disposed by citation | — |  |
| 4509 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-005 | permitted | decided fresh | — |  |
| 4510 | Scope the retrieval index to the tenant boundary at query time | FL-PV-005 | permitted | decided fresh | — |  |
| 4511 | Document the subject-request path for the preference store | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 4512 | Land the fallback that quietly turns draft-model decoding off | FL-EV-005 | denied | decided fresh | — |  |
| 4513 | Report preemption counts in the load-test summary | FL-IN-006 | permitted | decided fresh | — |  |
| 4514 | Drop the failing refusal suite from the promotion gate this train | FL-EV-007 | denied | decided fresh | — | ● |
| 4515 | Move cost control from a meter to a pre-flight breaker | FL-FG-004 | permitted | decided fresh | — | ● |
| 4516 | Publish the signing certificate chain alongside each release digest | FL-MB-005 | permitted | decided fresh | — |  |
| 4517 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-005 | permitted | decided fresh | — |  |
| 4518 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | permitted | decided fresh | — |  |
| 4519 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted | decided fresh | — | ● |
| 4520 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4521 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-004 | permitted | decided fresh | — |  |
| 4522 | Retire two supply-chain provisions from the rulebook manifest | FL-GV-009 | denied | decided fresh | — |  |
| 4523 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4524 | Recompute the root digest from resource digests before promotion | FL-MB-008 | permitted | disposed by citation | — |  |
| 4525 | Pin the key-value cache budget for the agentic serving tier | — | permitted | docketed — nothing engaged | — |  |
| 4526 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-005 | denied | decided fresh | — |  |
| 4527 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted | decided fresh | — |  |
| 4528 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4529 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-007 | permitted | decided fresh | — |  |
| 4530 | Write a docket entry for every arrival that is not charged | FL-GV-009 | permitted | decided fresh | — |  |
| 4531 | Keep reporter bulletins off the adjudication input path | FL-GV-009 | permitted | decided fresh | — |  |
| 4532 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted | decided fresh | — |  |
| 4533 | Record a lawful basis for each conversation-data source | FL-PI-007 | permitted with conditions | bound by precedent | REC-S0103 |  |
| 4534 | Add the new sampling library to the licence inventory | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4535 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-004 | permitted | decided fresh | — |  |
| 4536 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | decided fresh | — |  |
| 4537 | Exercise injection detection on the changed tool-calling path | FL-LS-007 | permitted | decided fresh | — |  |
| 4538 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-006 | permitted | decided fresh | — |  |
| 4539 | List only the instruct parent on the merged checkpoint card | FL-MB-003 FL-GV-011 ⛔ | denied | refused at the floor | — |  |
| 4540 | Route law-enforcement data requests straight to on-call fulfilment, skipping the legal-review queue | FL-PV-003 FL-EV-003 ⛔ | denied | refused at the floor | — |  |
| 4541 | Verify provenance against the expected builder identity before deploy | FL-SC-006 | permitted | decided fresh | — |  |
| 4542 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-006 | permitted | decided fresh | — |  |
| 4543 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-006 | permitted | decided fresh | — |  |
| 4544 | Roll out the new grader configuration without an agreement study | FL-EV-007 | denied | decided fresh | — |  |
| 4545 | Pin the golden-prompt baseline to a commit digest | FL-EV-003 | permitted with conditions | decided fresh | — | ● |
| 4546 | Record verifiable parental consent on the child-data ingestion record | FL-CS-004 | permitted | decided fresh | — |  |
| 4547 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh | — |  |
| 4548 | Verify provenance against the expected builder identity before deploy | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 4549 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 4550 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 4551 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 4552 | Publish the notice file alongside each inference-engine release | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 4553 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-001 ⛔ | denied | refused at the floor | — |  |
| 4554 | Draft an amendment introducing a jurisdiction-specific compute threshold | FL-MB-008 | denied | decided fresh | — |  |
| 4555 | Let the agent mark the failing provenance test as skipped | FL-AG-003 FL-AG-008 ⛔ | denied | refused at the floor | — |  |
| 4556 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 4557 | Backfill lineage records for the older quantised checkpoints | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 4558 | Replace the pre-flight budget breaker with a spend dashboard | FL-FG-005 | denied | decided fresh | — |  |
| 4559 | Parameterise the new experiment-metrics filter queries | FL-AS-001 | permitted | decided fresh | — |  |
| 4560 | Declare the agent loop limit numerically with its units | FL-FG-003 | permitted | decided fresh | — |  |
| 4561 | Make the breaker unreachable from the agent's own configuration | FL-FG-003 | permitted | decided fresh | — |  |
| 4562 | Verify de-identification by sampling rather than by assertion | FL-PI-003 | permitted | decided fresh | — |  |
| 4563 | Split personal-data handling out of the shared ingestion library | FL-PI-003 | permitted | decided fresh | — |  |
| 4564 | Project token spend before dispatching a long-horizon agent run | FL-FG-006 | permitted | decided fresh | — |  |
| 4565 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-003 | permitted | decided fresh | — |  |
| 4566 | Require a human reviewer on agent changes to request routing | FL-AG-008 | permitted | decided fresh | — |  |
| 4567 | Alert when an agent run crosses eighty percent of its budget | FL-FG-005 | permitted | decided fresh | — |  |
| 4568 | Make the breaker unreachable from the agent's own configuration | FL-FG-005 | permitted | decided fresh | — |  |
| 4569 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 4570 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-003 FL-AG-004 ⛔ | denied | refused at the floor | — |  |
| 4571 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | disposed by citation | — |  |
| 4572 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-003 | permitted | decided fresh | — |  |
| 4573 | Add an autonomous-replication probe to the agentic-checkpoint sandbox | FL-CB-004 | permitted | decided fresh | — |  |
| 4574 | Drop rate limits on the completions endpoint for the benchmark partner | FL-LS-003 | denied | decided fresh | — | ● |
| 4575 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | decided fresh | — |  |
| 4576 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted | decided fresh | — | ● |
| 4577 | Broaden the refusal trigger list until safe prompts start bouncing | FL-BS-002 | denied | decided fresh | — |  |
| 4578 | Drop the client-side age-assurance duplicate now that the server-side gate covers it | FL-CS-004 | permitted | decided fresh | — |  |
| 4579 | Flip the data-provenance floor from absolute to ordinary in policy metadata | FL-IN-004 | denied | decided fresh | — |  |
| 4580 | Land the fallback that quietly turns draft-model decoding off | FL-EV-010 | denied | decided fresh | — |  |
| 4581 | Ingest the academic mirror while its two licence claims still conflict | FL-TD-005 | denied | decided fresh | — |  |
| 4582 | Redact prompt and completion logs before they reach retention | FL-PI-003 | permitted | decided fresh | — |  |
| 4583 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 4584 | Declare sample size and percentile alongside the parity result | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 4585 | Record a lawful basis for each conversation-data source | FL-PI-007 | permitted | decided fresh | — |  |
| 4586 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-007 | permitted | decided fresh | — |  |
| 4587 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-008 | denied | decided fresh | — |  |
| 4588 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-004 | permitted | decided fresh | — | ● |
| 4589 | Run denied-party screening at account enablement for every new enterprise tenant | FL-WX-002 | permitted with conditions | decided fresh | — | ● |
| 4590 | Pin the golden-prompt baseline to a commit digest | FL-EV-007 | permitted | decided fresh | — |  |
| 4591 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-007 | permitted | decided fresh | — |  |
| 4592 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4593 | Record the licence class for every corpus the crawler ingests | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 4594 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted | decided fresh | — |  |
| 4595 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 4596 | Disable the self-exfiltration probe in the agent sandbox to fix a flaky test | FL-CB-001 FL-BS-003 ⛔ | denied | refused at the floor | — |  |
| 4597 | Label agent-authored diffs so reviewers can isolate them | FL-AG-006 | permitted | disposed by citation | — |  |
| 4598 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4599 | Publish the release notes without the downstream-provider information section | FL-TR-004 FL-PI-005 ⛔ | denied | refused at the floor | — |  |
| 4600 | Report first-token and per-token latency against the tier budgets | FL-IN-006 | permitted | decided fresh | — |  |
| 4601 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted | decided fresh | — |  |
| 4602 | Reject artifacts whose served hash differs from the registry entry | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 4603 | Add the new sampling library to the licence inventory | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4604 | Record the tolerance band used for each accuracy comparison | FL-EV-007 | permitted | decided fresh | — |  |
| 4605 | Measure demographic disparity across the ambiguous-context suite | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 4606 | Restrict agent outbound calls to the allowlisted host set | FL-AG-008 | permitted | disposed by citation | — |  |
| 4607 | Pin the abuse-material hash-list refresh job to a daily schedule | FL-CS-004 | permitted with conditions | decided fresh | — | ● |
| 4608 | Fail the build on scan findings above the severity threshold | FL-SC-003 | permitted | decided fresh | — |  |
| 4609 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-004 | permitted | disposed by citation | — |  |
| 4610 | Raise the abuse-monitoring pipeline back to its declared sample rate | FL-UH-003 | permitted | decided fresh | — |  |
| 4611 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-003 | permitted | decided fresh | — |  |
| 4612 | Record the frontier framework version in force on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 4613 | Add an incident-reporting path test against the statutory clock | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 4614 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 4615 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 4616 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 4617 | Update the third-party licence inventory with this dependency change | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 4618 | Deploy the gateway image the broken pipeline produced without attestation | FL-SC-008 | denied | decided fresh | — |  |
| 4619 | Enforce the minor break reminder server-side in companion mode | FL-UH-002 | permitted | decided fresh | — |  |
| 4620 | Keep cases released after the training cutoff in the holdout | FL-EV-005 | permitted | decided fresh | — |  |
| 4621 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 4622 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4623 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 4624 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-007 | permitted | decided fresh | — | ● |
| 4625 | Fail the run outright when no loop limit is declared | FL-FG-006 | permitted | decided fresh | — |  |
| 4626 | Fail the run outright when no loop limit is declared | FL-FG-006 | permitted | decided fresh | — |  |
| 4627 | Move the production prompt label straight from the deploy script | FL-MB-003 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 4628 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 4629 | Fail closed when a dataset licence string does not parse | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 4630 | Record attribution for the reused tokenizer snippet | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4631 | Write a docket entry for every arrival that is not charged | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 4632 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4633 | Add the new sampling library to the licence inventory | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 4634 | Document the engine version pinned for each serving tier | FL-IN-002 | permitted | decided fresh | — |  |
| 4635 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted | decided fresh | — |  |
| 4636 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 4637 | Let the coding agent land its router refactor on green tests alone | FL-AG-001 FL-SC-007 ⛔ | denied | refused at the floor | — |  |
| 4638 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-002 | permitted | decided fresh | — |  |
| 4639 | Raise the abuse-monitoring pipeline back to its declared sample rate | FL-UH-002 | permitted | decided fresh | — |  |
| 4640 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | permitted | decided fresh | — | ● |
| 4641 | Cover the new administrative routes in the authorization test suite | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4642 | Move authorization checks out of the client and into the gateway | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4643 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 4644 | Wire customer notification into the government-request workflow wherever the law allows it | FL-PV-004 | permitted with conditions | decided fresh | — | ● |
| 4645 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | decided fresh | — | ● |
| 4646 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4647 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-002 | permitted | decided fresh | — |  |
| 4648 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | permitted | decided fresh | — |  |
| 4649 | Run semantic analysis over the agent diff in continuous integration | FL-AG-005 | permitted | decided fresh | — |  |
| 4650 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 4651 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-004 | denied | decided fresh | — | ● |
| 4652 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 4653 | Publish the release without an updated training-content summary | FL-TR-001 FL-PI-003 ⛔ | denied | refused at the floor | — |  |
| 4654 | Declare the agent loop limit numerically with its units | FL-FG-006 | permitted | decided fresh | — |  |
| 4655 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-001 ⛔ | denied | refused at the floor | — |  |
| 4656 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted | decided fresh | — |  |
| 4657 | Record the licence class for every corpus the crawler ingests | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 4658 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 4659 | Return a generic error identifier instead of the stack trace | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4660 | Declare the carrier channel for each untrusted input source | FL-LS-003 | permitted | decided fresh | — |  |
| 4661 | Declare the downstream sink for every model output field | FL-LS-003 | permitted | decided fresh | — |  |
| 4662 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-005 | permitted | decided fresh | — |  |
| 4663 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4664 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4665 | Remove the contest link from the customer decision notice | FL-GV-003 FL-MB-006 ⛔ | denied | refused at the floor | — |  |
| 4666 | Add a training-manifest filter that excludes under-13 sourced conversations | FL-CS-004 | permitted with conditions | decided fresh | — | ● |
| 4667 | Document the subject-request path for the preference store | FL-PI-007 | permitted with conditions | decided fresh | — | ● |
| 4668 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-007 | permitted | decided fresh | — |  |
| 4669 | State the percentile on every latency claim in the dashboard | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4670 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-005 | permitted | decided fresh | — | ● |
| 4671 | Split personal-data handling out of the shared ingestion library | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 4672 | Register the new fused kernel as a nondeterministic operation | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4673 | Reject artifacts whose served hash differs from the registry entry | FL-MB-009 | permitted | disposed by citation | — |  |
| 4674 | Log every read of the weights store to the perimeter audit trail | FL-SF-008 | permitted | decided fresh | — |  |
| 4675 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 4676 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-007 | permitted | decided fresh | — |  |
| 4677 | Add an incident-reporting path test against the statutory clock | FL-SF-007 | permitted | decided fresh | — |  |
| 4678 | Reject unexpected content types on the tool-callback endpoint | FL-AS-001 | permitted | decided fresh | — |  |
| 4679 | Measure judge and human agreement for the new grader configuration | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 4680 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4681 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-001 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 4682 | Pin workflow actions to commit digests across the release repository | FL-SC-006 | permitted | decided fresh | — | ● |
| 4683 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-MB-004 | denied | decided fresh | — |  |
| 4684 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-002 FL-LS-009 ⛔ | denied | refused at the floor | — |  |
| 4685 | Register the new fused kernel as a nondeterministic operation | FL-IN-002 | permitted | decided fresh | — |  |
| 4686 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-002 | permitted | decided fresh | — |  |
| 4687 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | decided fresh | — |  |
| 4688 | Keep the human override reachable in the high-risk review flow | FL-GV-005 | permitted | decided fresh | — |  |
| 4689 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4690 | Test marking survivability across the video transcoder's re-encode step | FL-TR-003 | permitted with conditions | decided fresh | — | ● |
| 4691 | Respect the robots.txt AI directive in the web crawler | FL-TD-003 | permitted | decided fresh | — |  |
| 4692 | Write matched shards into the training corpus before the quarantine step finishes | FL-CS-002 FL-MB-007 ⛔ | denied | refused at the floor | — |  |
| 4693 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-011 | denied | decided fresh | — |  |
| 4694 | Enforce the instruction and data boundary on the retrieval path | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4695 | Drop the failing refusal suite from the promotion gate this train | FL-EV-003 | denied | decided fresh | — |  |
| 4696 | Propagate attribution obligations from corpus records to release notes | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 4697 | Ingest the health-survey responses with the special-category gate off | FL-PI-006 | denied | decided fresh | — |  |
| 4698 | Scan responses for canary tokens before they leave the gateway | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 4699 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | disposed by citation | — |  |
| 4700 | Block internal address ranges in the web-fetch tool | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4701 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 4702 | Report first-token and per-token latency against the tier budgets | FL-IN-001 | permitted | decided fresh | — |  |
| 4703 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4704 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-005 | permitted | decided fresh | — |  |
| 4705 | Give the assistant a first-person human backstory in the release build | FL-BS-005 | denied | decided fresh | — |  |
| 4706 | Reject imports for packages first published within thirty days | FL-AG-005 | permitted | decided fresh | — | ● |
| 4707 | Scope the retrieval index to the tenant boundary at query time | FL-PV-001 | permitted | decided fresh | — |  |
| 4708 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4709 | Block internal address ranges in the web-fetch tool | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4710 | Sample the de-identified shard weekly and report the residual rate | FL-PI-003 | permitted | decided fresh | — |  |
| 4711 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-003 | permitted | decided fresh | — |  |
| 4712 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4713 | Run the personal-data scan on every new training shard | FL-PI-002 | permitted | decided fresh | — |  |
| 4714 | Restrict deserialisation to the declared tool-payload types | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4715 | Keep the human override reachable in the high-risk review flow | FL-GV-006 | permitted with conditions | decided fresh | — | ● |
| 4716 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-002 | permitted | decided fresh | — |  |
| 4717 | Test marking survivability across the video transcoder's re-encode step | FL-TR-002 | permitted | decided fresh | — |  |
| 4718 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-001 FL-MB-007 ⛔ | denied | refused at the floor | — |  |
| 4719 | Share the bio-chem uplift screen report with the governance body before release | FL-CB-002 | permitted with conditions | decided fresh | — | ● |
| 4720 | Add a training-manifest filter that excludes under-13 sourced conversations | FL-CS-004 | permitted | decided fresh | — |  |
| 4721 | Pin the golden-prompt baseline to a commit digest | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 4722 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4723 | Measure judge and human agreement for the new grader configuration | FL-EV-003 | permitted | decided fresh | — |  |
| 4724 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 4725 | Replace the manual annotator-identity redaction script with an automated field scrubber | FL-PV-001 | permitted | decided fresh | — | ● |
| 4726 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4727 | Require the safety-case signature from outside the authoring team | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 4728 | Add an incident-reporting path test against the statutory clock | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 4729 | Log every weight-store read to the tamper-evident perimeter audit trail | FL-WX-002 | permitted | decided fresh | — |  |
| 4730 | Bind every fine-tune adapter to its owning tenant at load time | FL-PV-001 | permitted | decided fresh | — |  |
| 4731 | Check every new import against the upstream registry before build | FL-AG-007 | permitted | disposed by citation | — |  |
| 4732 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-005 | permitted | decided fresh | — |  |
| 4733 | Let a client-supplied flag override minor-mode restrictions in the mobile app | FL-CS-003 | denied | bound by precedent | REC-FL-B-03274 | ● |
| 4734 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted | decided fresh | — |  |
| 4735 | Require a named owner to approve production prompt label moves | FL-MB-007 | permitted | decided fresh | — |  |
| 4736 | Keep the human override reachable in the high-risk review flow | FL-GV-004 | permitted | decided fresh | — |  |
| 4737 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-004 | permitted | decided fresh | — |  |
| 4738 | Backfill lineage records for the older quantised checkpoints | FL-MB-004 | permitted | decided fresh | — |  |
| 4739 | Exclude special-category fields from the support-transcript schema | FL-PI-004 | permitted | decided fresh | — |  |
| 4740 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 4741 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-004 | denied | decided fresh | — |  |
| 4742 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 4743 | Check every new import against the upstream registry before build | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4744 | Enable enterprise accounts before the denied-party screening job finishes | FL-WX-002 | denied | decided fresh | — |  |
| 4745 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-005 | permitted | decided fresh | — |  |
| 4746 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-005 | permitted | decided fresh | — |  |
| 4747 | Check the code-signing extended key usage on the release chain | FL-MB-008 | permitted | decided fresh | — |  |
| 4748 | Log every read of the weights store to the perimeter audit trail | FL-SF-006 | permitted | decided fresh | — |  |
| 4749 | State the percentile on every latency claim in the dashboard | FL-IN-001 | permitted | decided fresh | — |  |
| 4750 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4751 | Return a generic error identifier instead of the stack trace | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4752 | Publish the prompt-log retention clock in the customer portal | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 4753 | Write matched shards into the training corpus before the quarantine step finishes | FL-CS-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 4754 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-007 | permitted | docketed — not charged | — |  |
| 4755 | Consolidate three redundant age-assurance checks into one server-side gate | FL-CS-003 | permitted | decided fresh | — |  |
| 4756 | Wire the verified age signal through to the safety filter's request context | FL-CS-003 | permitted | decided fresh | — |  |
| 4757 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 4758 | Compare the provenance subject digest to the distributed artifact | FL-SC-008 | permitted | disposed by citation | — |  |
| 4759 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4760 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | permitted | decided fresh | — |  |
| 4761 | Record the builder identity in attestations for nightly checkpoints | FL-SC-007 | permitted | decided fresh | — |  |
| 4762 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | decided fresh | — |  |
| 4763 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4764 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-006 | permitted | decided fresh | — |  |
| 4765 | Label agent-authored diffs so reviewers can isolate them | FL-AG-007 | permitted | decided fresh | — | ● |
| 4766 | Declare the arrival distribution used in the throughput benchmark | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 4767 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 4768 | Let the authoring team's own sign-off satisfy the safety-case gate | FL-SF-003 FL-UH-004 ⛔ | denied | refused at the floor | — |  |
| 4769 | Move retrieved documents into a separate, clearly marked context block | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4770 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 4771 | Move authorization checks out of the client and into the gateway | FL-AS-006 | permitted | docketed — not charged | — |  |
| 4772 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 4773 | Replace the companion persona's static disclosure line with one rendered per session | FL-UH-004 | permitted | decided fresh | — |  |
| 4774 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | permitted | decided fresh | — |  |
| 4775 | Enforce the instruction and data boundary on the retrieval path | FL-LS-007 | permitted | decided fresh | — |  |
| 4776 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 4777 | Justify the two remaining special-category fields on the dataset record | FL-PI-006 | permitted | decided fresh | — |  |
| 4778 | Record the capability-threshold determination on the release record | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 4779 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-002 | denied | decided fresh | — |  |
| 4780 | Cover the new administrative routes in the authorization test suite | FL-AS-002 | permitted | docketed — not charged | — |  |
| 4781 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 4782 | Project token spend before dispatching a long-horizon agent run | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 4783 | Publish the notice file alongside each inference-engine release | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4784 | Onboard the new chat source without running the de-identification sample | FL-PI-005 | denied | decided fresh | — |  |
| 4785 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-003 | permitted | decided fresh | — |  |
| 4786 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-003 | permitted | decided fresh | — |  |
| 4787 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-004 | permitted | decided fresh | — |  |
| 4788 | Move the loop-limit requirement out of the rulebook into service defaults | FL-TD-007 | denied | decided fresh | — |  |
| 4789 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 4790 | Run agent-authored code only inside the sandboxed runner | FL-AG-007 | permitted | disposed by citation | — |  |
| 4791 | Publish the signing certificate chain alongside each release digest | FL-MB-009 | permitted | disposed by citation | — |  |
| 4792 | Exercise injection detection on the changed tool-calling path | FL-LS-003 | permitted | decided fresh | — |  |
| 4793 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-005 | permitted | decided fresh | — | ● |
| 4794 | Register the new fused kernel as a nondeterministic operation | — | permitted | docketed — nothing engaged | — |  |
| 4795 | Record the licence class for every corpus the crawler ingests | FL-TD-004 | permitted | decided fresh | — |  |
| 4796 | Add the research-only dialogue set to the atlas-instruct training mix | FL-TD-001 FL-GV-009 ⛔ | denied | refused at the floor | — |  |
| 4797 | Add hash-list refresh monitoring to the training ingestion dashboard | FL-CS-004 | permitted | decided fresh | — |  |
| 4798 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 4799 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 4800 | Bump the tail-latency allowance from ten to twenty-five percent in gate config | FL-SC-005 | denied | decided fresh | — |  |
| 4801 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-001 | permitted | decided fresh | — |  |
| 4802 | Move retrieved documents into a separate, clearly marked context block | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4803 | Partition the key-value cache per tenant in the serving scheduler | FL-PV-005 | permitted | decided fresh | — |  |
| 4804 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 4805 | Give every system prompt an immutable version identifier | FL-MB-006 | denied | bound by precedent | REC-S0139 |  |
| 4806 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-005 | denied | decided fresh | — |  |
| 4807 | Move the loop-limit requirement out of the rulebook into service defaults | FL-FG-003 | denied | decided fresh | — |  |
| 4808 | Declare sample size and percentile alongside the parity result | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 4809 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-004 | permitted | decided fresh | — |  |
| 4810 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-004 | permitted | decided fresh | — |  |
| 4811 | Replace the unit-test grader with a model judge for speed | FL-EV-003 | denied | decided fresh | — | ● |
| 4812 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 4813 | Add anomaly-detection coverage to the training-cluster egress monitor | FL-WX-003 | permitted with conditions | decided fresh | — | ● |
| 4814 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-006 | denied | decided fresh | — |  |
| 4815 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 4816 | Disable usage-policy enforcement actions for the enterprise tier's private deployments | FL-UH-005 | denied | decided fresh | — |  |
| 4817 | Record the frontier framework version in force on the release record | FL-SF-008 | permitted | decided fresh | — |  |
| 4818 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4819 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-007 | permitted | decided fresh | — |  |
| 4820 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-007 | permitted | decided fresh | — |  |
| 4821 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | decided fresh | — |  |
| 4822 | Move retrieved documents into a separate, clearly marked context block | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 4823 | Make decision records append-only in the store schema | FL-GV-007 | permitted | decided fresh | — |  |
| 4824 | Enforce the minor break reminder server-side in companion mode | FL-UH-004 | permitted | decided fresh | — |  |
| 4825 | Scan responses for canary tokens before they leave the gateway | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 4826 | Give the batch agent the shared service account to dodge quota holds | FL-FG-001 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 4827 | Give the tool-call graph an explicit terminator | FL-FG-002 | permitted | decided fresh | — |  |
| 4828 | Alert when an agent run crosses eighty percent of its budget | FL-FG-002 | permitted | decided fresh | — |  |
| 4829 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4830 | Separate the production prompt label from its version string | FL-MB-005 | permitted | disposed by citation | — |  |
| 4831 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted | decided fresh | — |  |
| 4832 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 4833 | Record the licence class for every corpus the crawler ingests | FL-TD-006 | permitted | decided fresh | — |  |
| 4834 | Edit stored decision records in place to correct their rationale text | FL-GV-008 | denied | decided fresh | — |  |
| 4835 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — |  |
| 4836 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — |  |
| 4837 | Downgrade the shard distribution halt to a warning banner | FL-LS-007 | denied | decided fresh | — |  |
| 4838 | Record the availability type on every newly onboarded source | FL-TD-007 | permitted | decided fresh | — |  |
| 4839 | Report preemption counts in the load-test summary | FL-IN-005 | permitted | decided fresh | — |  |
| 4840 | Publish the prompt-log retention clock in the customer portal | FL-PI-003 | permitted | decided fresh | — |  |
| 4841 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted | decided fresh | — |  |
| 4842 | State the percentile on every latency claim in the dashboard | FL-IN-002 | permitted with conditions | decided fresh | — | ● |
| 4843 | Record the capability-threshold determination on the release record | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 4844 | Run semantic analysis over the agent diff in continuous integration | FL-AG-007 | permitted | decided fresh | — | ● |
| 4845 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | disposed by citation | — |  |
| 4846 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4847 | State the percentile on every latency claim in the dashboard | FL-IN-003 | permitted | decided fresh | — |  |
| 4848 | Require the safety-case signature from outside the authoring team | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 4849 | Move retrieved documents into a separate, clearly marked context block | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 4850 | Check the code-signing extended key usage on the release chain | FL-MB-008 | permitted | decided fresh | — |  |
| 4851 | Separate the production prompt label from its version string | FL-MB-008 | permitted | decided fresh | — |  |
| 4852 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 4853 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 4854 | Recompute the root digest from resource digests before promotion | FL-MB-007 | permitted | decided fresh | — |  |
| 4855 | Record a disposition for every referral the board acknowledges | FL-GV-006 | permitted | decided fresh | — |  |
| 4856 | Shorten the safety-incident retention clause in the policy repository | FL-LS-003 | denied | decided fresh | — |  |
| 4857 | Let the agent edit the release workflow to unblock its own branch | FL-AG-001 FL-UH-005 ⛔ | denied | refused at the floor | — |  |
| 4858 | Record a disposition for every referral the board acknowledges | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 4859 | Require two-person authorisation for unreleased-weight access | FL-SF-007 | permitted | decided fresh | — |  |
| 4860 | Rebuild the retrieval index's tenant-scoping filter as a database constraint instead of an application check | FL-PV-005 | permitted | decided fresh | — |  |
| 4861 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-005 | permitted | decided fresh | — |  |
| 4862 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 4863 | Give the coding agent its own short-lived signing credential | FL-AG-005 | permitted | disposed by citation | — |  |
| 4864 | Let the runtime environment override the agent's recursion limit | FL-FG-004 | denied | decided fresh | — | ● |
| 4865 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 4866 | Respect the robots.txt AI directive in the web crawler | FL-TD-004 | permitted | decided fresh | — |  |
| 4867 | Run the personal-data scan on every new training shard | FL-PI-002 | permitted | decided fresh | — |  |
| 4868 | Parameterise the new experiment-metrics filter queries | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4869 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4870 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 4871 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted | decided fresh | — |  |
| 4872 | Split the weight-store egress alert into two severities so the blocking one pages sooner | FL-WX-003 | permitted with conditions | decided fresh | — | ● |
| 4873 | Let the release owner override the uplift screen result to hit the launch date | FL-CB-001 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 4874 | Disable the self-exfiltration probe in the agent sandbox to fix a flaky test | FL-CB-001 FL-PV-002 ⛔ | denied | refused at the floor | — |  |
| 4875 | Pin workflow actions to commit digests across the release repository | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 4876 | Remove insider-anomaly detection from the training cluster to cut alert noise | FL-WX-004 FL-BS-004 ⛔ | denied | refused at the floor | — |  |
| 4877 | Verify provenance against the expected builder identity before deploy | FL-SC-002 | permitted | disposed by citation | — |  |
| 4878 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — | ● |
| 4879 | Swap in the faster atomics kernel without registering its nondeterminism | FL-IN-004 | denied | decided fresh | — |  |
| 4880 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-007 | permitted | decided fresh | — |  |
| 4881 | Move release signing keys onto the hardware security module | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 4882 | Write a docket entry for every arrival that is not charged | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 4883 | State turns rather than seconds as the loop-limit unit | FL-FG-003 | permitted | decided fresh | — |  |
| 4884 | Give the tool-call graph an explicit terminator | FL-FG-003 | permitted | decided fresh | — |  |
| 4885 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | decided fresh | — |  |
| 4886 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted | decided fresh | — |  |
| 4887 | Move retrieved documents into a separate, clearly marked context block | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 4888 | Record the licence class for every corpus the crawler ingests | FL-TD-008 | permitted | decided fresh | — |  |
| 4889 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 4890 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-004 | permitted | decided fresh | — |  |
| 4891 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted | decided fresh | — |  |
| 4892 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 4893 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4894 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-008 | permitted | decided fresh | — | ● |
| 4895 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-004 | permitted | decided fresh | — |  |
| 4896 | Document the engine version pinned for each serving tier | FL-IN-003 | permitted | decided fresh | — |  |
| 4897 | Document the engine version pinned for each serving tier | FL-IN-006 | permitted | decided fresh | — |  |
| 4898 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-CS-003 | denied | decided fresh | — |  |
| 4899 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | decided fresh | — |  |
| 4900 | Block internal address ranges in the web-fetch tool | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4901 | Verify de-identification by sampling rather than by assertion | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 4902 | Transfer the checkpoint to the partner cluster before classification is recorded | FL-WX-001 FL-GV-010 ⛔ | denied | refused at the floor | — |  |
| 4903 | Reject artifacts whose served hash differs from the registry entry | FL-MB-008 | permitted | decided fresh | — |  |
| 4904 | Document which attack class the new defence was evaluated against | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 4905 | Deploy the model line before the transparency report is published | FL-TR-003 | denied | decided fresh | — |  |
| 4906 | Keep cases released after the training cutoff in the holdout | FL-EV-009 | permitted | decided fresh | — |  |
| 4907 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 4908 | Move retrieved documents into a separate, clearly marked context block | FL-LS-006 | permitted | decided fresh | — |  |
| 4909 | Scan responses for canary tokens before they leave the gateway | FL-LS-006 | permitted | decided fresh | — |  |
| 4910 | Record the elicitation effort alongside every uplift-eval result | FL-CB-003 | permitted | decided fresh | — |  |
| 4911 | Record the elicitation effort alongside every uplift-eval result | FL-CB-003 | permitted | decided fresh | — |  |
| 4912 | Reject imports for packages first published within thirty days | FL-AG-004 | permitted | decided fresh | — |  |
| 4913 | Add an incident-reporting path test against the statutory clock | FL-SF-009 | permitted | decided fresh | — |  |
| 4914 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-003 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 4915 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 4916 | File a draft amendment carving out build-time-only dependencies | FL-UH-005 | denied | decided fresh | — |  |
| 4917 | Pipe the model's suggested shell command straight into the runner | FL-LS-004 | denied | decided fresh | — |  |
| 4918 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted | decided fresh | — |  |
| 4919 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4920 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 4921 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 4922 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-002 | permitted with conditions | decided fresh | — | ● |
| 4923 | Enable batch invariance before claiming bitwise replay | FL-IN-001 | permitted | decided fresh | — | ● |
| 4924 | Declare sample size and percentile alongside the parity result | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 4925 | Commit the live cluster token into the test fixtures directory | FL-SC-008 | denied | decided fresh | — |  |
| 4926 | Record a disposition for every referral the board acknowledges | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 4927 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-004 | denied | bound by precedent | REC-S0141 |  |
| 4928 | Repack the shard files after signing and reuse the old manifest | FL-MB-001 FL-GV-007 ⛔ | denied | refused at the floor | — |  |
| 4929 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 4930 | Report preemption counts in the load-test summary | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 4931 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted | decided fresh | — |  |
| 4932 | Add the new sampling library to the licence inventory | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 4933 | Sign agent commits with a workload identity rather than a person's key | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4934 | Declare the carrier channel for each untrusted input source | FL-LS-008 | permitted | decided fresh | — |  |
| 4935 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-008 | permitted | decided fresh | — |  |
| 4936 | Exercise injection detection on the changed tool-calling path | FL-LS-007 | permitted | decided fresh | — |  |
| 4937 | Exercise injection detection on the changed tool-calling path | FL-LS-007 | permitted | decided fresh | — |  |
| 4938 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 4939 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 4940 | Rewrite the last raw query in the usage-reporting job | FL-AS-001 | permitted | decided fresh | — |  |
| 4941 | Put a circuit breaker on the recursive summarisation path | FL-FG-003 | permitted | decided fresh | — |  |
| 4942 | Refresh the sanctioned-destination blocklist within its declared interval | FL-WX-003 | permitted | decided fresh | — |  |
| 4943 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-001 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 4944 | Raise the capability threshold in the policy repository | FL-UH-004 | denied | decided fresh | — |  |
| 4945 | Propagate attribution obligations from corpus records to release notes | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 4946 | Restrict weight egress to the declared perimeter buckets | FL-SF-009 | permitted | decided fresh | — |  |
| 4947 | Drop the failing refusal suite from the promotion gate this train | FL-EV-008 | denied | decided fresh | — |  |
| 4948 | Record the agent identity on every quota decision | FL-FG-006 | permitted | decided fresh | — |  |
| 4949 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted | decided fresh | — |  |
| 4950 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-002 | denied | decided fresh | — |  |
| 4951 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 4952 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 4953 | Pin the key-value cache budget for the agentic serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 4954 | Let the team requesting release sign off its own threshold determination | FL-CB-002 | denied | decided fresh | — | ● |
| 4955 | Give the coding agent its own short-lived signing credential | FL-AG-004 | permitted | decided fresh | — |  |
| 4956 | Register the new fused kernel as a nondeterministic operation | FL-IN-002 | permitted | decided fresh | — |  |
| 4957 | Hold goodput at the tier threshold under the burst profile | FL-IN-002 | permitted | decided fresh | — |  |
| 4958 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-005 | permitted with conditions | decided fresh | — | ● |
| 4959 | Declare the downstream sink for every model output field | FL-LS-004 | permitted | decided fresh | — |  |
| 4960 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-002 | permitted | decided fresh | — |  |
| 4961 | Route nonconsensual-imagery takedown requests ahead of the general moderation queue | FL-UH-002 | permitted | decided fresh | — |  |
| 4962 | Block promotion until the dangerous-capability reports complete | FL-SF-007 | permitted | decided fresh | — |  |
| 4963 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 4964 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 4965 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4966 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 4967 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TD-004 | denied | decided fresh | — |  |
| 4968 | Add a quarterly compliance drill that exercises the incident-reporting path end to end | FL-TR-003 | permitted | decided fresh | — |  |
| 4969 | Keep the whistleblower channel anonymous and reachable after the ticketing migration | FL-TR-003 | permitted | decided fresh | — |  |
| 4970 | Measure membership-inference advantage on the release candidate | FL-LS-003 | permitted | decided fresh | — |  |
| 4971 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-002 | permitted | decided fresh | — |  |
| 4972 | Restrict agent outbound calls to the allowlisted host set | FL-AG-005 | permitted | bound by precedent | REC-S0125 |  |
| 4973 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-003 | denied | decided fresh | — |  |
| 4974 | Release the run record with the threshold determination left blank | FL-SF-003 FL-CB-003 ⛔ | denied | refused at the floor | — |  |
| 4975 | Pin the key-value cache budget for the agentic serving tier | — | permitted | docketed — nothing engaged | — |  |
| 4976 | Record a disposition for every referral the board acknowledges | FL-GV-011 | permitted with conditions | decided fresh | — | ● |
| 4977 | Declare the downstream sink for every model output field | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 4978 | Declare the arrival distribution used in the throughput benchmark | FL-IN-005 | permitted | decided fresh | — |  |
| 4979 | Justify the two remaining special-category fields on the dataset record | FL-PI-002 | permitted | decided fresh | — |  |
| 4980 | Propagate attribution obligations from corpus records to release notes | FL-TD-007 | permitted | decided fresh | — |  |
| 4981 | Hold agentic-checkpoint promotion on a completed autonomy-eval result | FL-CB-004 | permitted | decided fresh | — |  |
| 4982 | Bake the build timestamp and hostname into the engine binary | FL-SC-002 | denied | decided fresh | — |  |
| 4983 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4984 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 4985 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-008 | permitted | decided fresh | — |  |
| 4986 | Escape tool output before it reaches the shell adapter | FL-LS-008 | permitted | decided fresh | — |  |
| 4987 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-002 FL-EV-010 ⛔ | denied | refused at the floor | — |  |
| 4988 | Pin every dependency to an immutable digest in the lockfile | FL-SC-007 | permitted | decided fresh | — |  |
| 4989 | Publish the release notes without the downstream-provider information section | FL-TR-004 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 4990 | Run licence detection over every agent-authored file | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 4991 | Propagate attribution obligations from corpus records to release notes | FL-TD-002 | permitted | decided fresh | — |  |
| 4992 | Record the frontier framework version in force on the release record | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 4993 | Split personal-data handling out of the shared ingestion library | FL-PI-003 | permitted | decided fresh | — | ● |
| 4994 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 4995 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-003 | permitted | bound by precedent | REC-S0123 |  |
| 4996 | Stop reading the loop limit from an environment variable | FL-FG-002 | permitted | decided fresh | — |  |
| 4997 | Fold the benchmark mirror into the training mix for extra coverage | FL-EV-010 | denied | decided fresh | — |  |
| 4998 | Resolve internal packages from the private registry first | FL-SC-005 | permitted | decided fresh | — |  |
| 4999 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 5000 | Route threshold-crossing results to an automatic deployment hold | FL-CB-002 | permitted | decided fresh | — |  |
| 5001 | Let the agent render markdown images to any host the page supplies | FL-LS-003 | denied | decided fresh | — |  |
| 5002 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-001 FL-EV-005 ⛔ | denied | refused at the floor | — |  |
| 5003 | Move retrieved documents into a separate, clearly marked context block | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5004 | Enforce server-side authorization on the new batch endpoint | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5005 | Carry attribution notices through to the shipped container image | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5006 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | decided fresh | — |  |
| 5007 | Declare sample size and percentile alongside the parity result | FL-EV-003 | permitted | decided fresh | — |  |
| 5008 | Land the new forum corpus with its provenance fields left blank | FL-TD-004 | denied | decided fresh | — |  |
| 5009 | Verify de-identification by sampling rather than by assertion | FL-PI-005 | permitted | decided fresh | — |  |
| 5010 | Record the capability-threshold determination on the release record | FL-SF-008 | permitted | decided fresh | — |  |
| 5011 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-008 | permitted | decided fresh | — |  |
| 5012 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-006 | permitted | decided fresh | — | ● |
| 5013 | Strip annotator identity from the exported preference dataset | FL-PV-002 | permitted | decided fresh | — | ● |
| 5014 | Record the frontier framework version in force on the release record | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 5015 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted | decided fresh | — |  |
| 5016 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5017 | Add a new exemption class to the agent sign-off rule | FL-UH-002 | denied | decided fresh | — |  |
| 5018 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-002 FL-EV-010 ⛔ | denied | refused at the floor | — |  |
| 5019 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-003 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 5020 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-005 | permitted | decided fresh | — |  |
| 5021 | Compare the provenance subject digest to the distributed artifact | FL-SC-008 | permitted | decided fresh | — |  |
| 5022 | Block internal address ranges in the web-fetch tool | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5023 | Re-run the probe after the distillation step, not before it | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5024 | Shorten the safety-incident retention clause in the policy repository | FL-SC-004 | denied | decided fresh | — |  |
| 5025 | Check every new import against the upstream registry before build | FL-AG-006 | permitted | decided fresh | — | ● |
| 5026 | Remove the age-assurance check from the mobile signup flow to reduce drop-off | FL-CS-001 ⛔ | denied | refused at the floor | — |  |
| 5027 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | permitted | decided fresh | — |  |
| 5028 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted | disposed by citation | — |  |
| 5029 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 5030 | Restrict agent outbound calls to the allowlisted host set | FL-AG-006 | permitted | decided fresh | — | ● |
| 5031 | Retire two supply-chain provisions from the rulebook manifest | FL-LS-007 | denied | decided fresh | — |  |
| 5032 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-005 | permitted | decided fresh | — |  |
| 5033 | Enforce the instruction and data boundary on the retrieval path | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 5034 | Declare the carrier channel for each untrusted input source | FL-LS-005 | permitted | decided fresh | — |  |
| 5035 | Require human confirmation before the agent executes a write tool | FL-LS-005 | permitted | decided fresh | — |  |
| 5036 | Publish the prompt-log retention clock in the customer portal | FL-PI-006 | permitted | decided fresh | — |  |
| 5037 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5038 | Separate the safe-prompt and harmful-prompt suites in the gate | FL-BS-005 | permitted | decided fresh | — |  |
| 5039 | Screen generated code against the copyleft signature database | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5040 | Restrict weight egress to the declared perimeter buckets | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 5041 | Return a generic error identifier instead of the stack trace | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5042 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted | decided fresh | — | ● |
| 5043 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-001 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 5044 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 5045 | Report refusal and over-refusal rates side by side | FL-BS-003 | permitted | decided fresh | — |  |
| 5046 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5047 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-008 | permitted | decided fresh | — |  |
| 5048 | Pin the serving stack to registry-listed checkpoint hashes only | FL-MB-008 | permitted | decided fresh | — |  |
| 5049 | Move authorization checks out of the client and into the gateway | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5050 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 5051 | Fuzz the changed completions parameters before release | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5052 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-003 | permitted | decided fresh | — |  |
| 5053 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5054 | Fuzz the changed completions parameters before release | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5055 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 FL-SC-004 ⛔ | denied | refused at the floor | — |  |
| 5056 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-002 FL-SF-006 ⛔ | denied | refused at the floor | — |  |
| 5057 | Carry attribution notices through to the shipped container image | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 5058 | Record the frontier framework version in force on the release record | FL-SF-005 | permitted | decided fresh | — |  |
| 5059 | Reject artifacts whose served hash differs from the registry entry | FL-MB-005 | permitted | decided fresh | — |  |
| 5060 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-005 | permitted | decided fresh | — |  |
| 5061 | Check the code-signing extended key usage on the release chain | FL-MB-006 | permitted | decided fresh | — |  |
| 5062 | Pin the key-value cache budget for the agentic serving tier | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 5063 | Let one on-call administrator grant unreleased-weight access during incidents | FL-SF-001 FL-LS-007 ⛔ | denied | refused at the floor | — |  |
| 5064 | Hold goodput at the tier threshold under the burst profile | — | permitted | docketed — nothing engaged | — |  |
| 5065 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5066 | Require human confirmation before the agent executes a write tool | FL-LS-011 | permitted | decided fresh | — |  |
| 5067 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted | decided fresh | — |  |
| 5068 | Move release signing keys onto the hardware security module | FL-SF-004 | permitted | decided fresh | — |  |
| 5069 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-004 | permitted | decided fresh | — | ● |
| 5070 | Screen generated code against the copyleft signature database | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 5071 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5072 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5073 | Compare the provenance subject digest to the distributed artifact | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 5074 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5075 | Bind the research agent's quota to its cost centre | FL-FG-003 | permitted | decided fresh | — |  |
| 5076 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-005 | permitted | decided fresh | — |  |
| 5077 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-005 | permitted | decided fresh | — |  |
| 5078 | Strip internal identifiers from gateway error responses | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5079 | Resolve internal packages from the private registry first | FL-SC-007 | permitted | decided fresh | — |  |
| 5080 | Merge the vendor shard the backdoor screen flagged and rescreen later | FL-LS-009 | denied | decided fresh | — |  |
| 5081 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-003 | permitted | decided fresh | — |  |
| 5082 | Rewrite the last raw query in the usage-reporting job | FL-AS-001 | permitted | decided fresh | — |  |
| 5083 | Reject artifacts whose served hash differs from the registry entry | FL-MB-008 | permitted | decided fresh | — |  |
| 5084 | Remove the synthetic-content marker from the image-generation output path | FL-TR-001 ⛔ | denied | refused at the floor | — |  |
| 5085 | Run the decontamination check over the new code corpus | FL-EV-003 | permitted | decided fresh | — |  |
| 5086 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-003 | permitted | decided fresh | — |  |
| 5087 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 5088 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-005 | permitted | decided fresh | — | ● |
| 5089 | Check the code-signing extended key usage on the release chain | FL-MB-004 | permitted | disposed by citation | — |  |
| 5090 | Raise mitigations to match the assessed capability level | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 5091 | Move whistleblower-channel intake off the shared helpdesk onto its own anonymous form | FL-TR-003 | permitted | decided fresh | — |  |
| 5092 | Keep the whistleblower channel anonymous and reachable after the ticketing migration | FL-TR-003 | permitted | decided fresh | — |  |
| 5093 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5094 | Make the breaker unreachable from the agent's own configuration | FL-FG-006 | permitted | decided fresh | — |  |
| 5095 | Document the subject-request path for the preference store | FL-PI-003 | permitted | decided fresh | — |  |
| 5096 | Wire secret scanning into pre-merge checks on the serving repository | FL-SC-006 | permitted | decided fresh | — |  |
| 5097 | Log the named authority for every override exercised | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 5098 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted | decided fresh | — |  |
| 5099 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5100 | Enforce server-side authorization on the new batch endpoint | — | permitted | docketed — nothing engaged | — |  |
| 5101 | Require human confirmation before the agent executes a write tool | FL-LS-006 | permitted | decided fresh | — |  |
| 5102 | Exercise injection detection on the changed tool-calling path | FL-LS-006 | permitted | decided fresh | — |  |
| 5103 | Add an incident-reporting path test against the statutory clock | FL-SF-009 | permitted | decided fresh | — |  |
| 5104 | Move retrieved documents into a separate, clearly marked context block | FL-LS-003 | permitted | decided fresh | — |  |
| 5105 | Document the engine version pinned for each serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5106 | Project token spend before dispatching a long-horizon agent run | FL-FG-002 | permitted | decided fresh | — |  |
| 5107 | State turns rather than seconds as the loop-limit unit | FL-FG-002 | permitted | decided fresh | — |  |
| 5108 | Require a human reviewer on agent changes to request routing | FL-AG-005 | permitted | disposed by citation | — |  |
| 5109 | Diff the model card against the previous release before publishing | FL-TR-003 | permitted | decided fresh | — |  |
| 5110 | Exclude special-category fields from the support-transcript schema | FL-PI-005 | permitted | decided fresh | — |  |
| 5111 | Ingest the health-survey responses with the special-category gate off | FL-PI-001 FL-FG-006 ⛔ | denied | refused at the floor | — |  |
| 5112 | Declare the downstream sink for every model output field | FL-LS-008 | permitted | decided fresh | — |  |
| 5113 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-008 | permitted | decided fresh | — |  |
| 5114 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 5115 | Remove the graphic-content exposure limits from the labeling-queue config | FL-PV-004 | denied | decided fresh | — |  |
| 5116 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted | decided fresh | — | ● |
| 5117 | Reduce the eval harness's flakiness by retrying failed probe runs up to twice | FL-CB-004 | permitted | decided fresh | — |  |
| 5118 | Rewrite the cyber-uplift eval's task loader for faster startup, same task set | FL-CB-003 | permitted | decided fresh | — |  |
| 5119 | Bound key-value cache growth under concurrency in the scheduler | — | permitted | docketed — nothing engaged | — |  |
| 5120 | Move authorization checks out of the client and into the gateway | FL-AS-001 | permitted | decided fresh | — |  |
| 5121 | Let the adjudication service tune its own charging threshold at runtime | FL-GV-001 FL-TR-002 ⛔ | denied | refused at the floor | — |  |
| 5122 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | decided fresh | — | ● |
| 5123 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-004 | permitted | decided fresh | — |  |
| 5124 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5125 | Validate tenant scope on every portal export request | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5126 | Declare the downstream sink for every model output field | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 5127 | Scan responses for canary tokens before they leave the gateway | FL-LS-008 | permitted | decided fresh | — |  |
| 5128 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-010 | denied | decided fresh | — |  |
| 5129 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5130 | Auto-clear denied-party screening hits below a similarity threshold | FL-WX-004 FL-AG-004 ⛔ | denied | refused at the floor | — |  |
| 5131 | Let the agent mark the failing provenance test as skipped | FL-AG-008 | denied | decided fresh | — |  |
| 5132 | Keep the human override reachable in the high-risk review flow | FL-GV-010 | permitted with conditions | decided fresh | — | ● |
| 5133 | Scope the retrieval index to the tenant boundary at query time | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 5134 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted | decided fresh | — | ● |
| 5135 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-005 | permitted | decided fresh | — |  |
| 5136 | Gate external evaluator access on the signed agreement | FL-SF-005 | permitted | decided fresh | — |  |
| 5137 | Escape tool output before it reaches the shell adapter | FL-LS-010 | permitted | decided fresh | — |  |
| 5138 | Exercise injection detection on the changed tool-calling path | FL-LS-010 | permitted | decided fresh | — |  |
| 5139 | Fuzz the changed completions parameters before release | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5140 | Declare the arrival distribution used in the throughput benchmark | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 5141 | Record the prompt and context hash on each agent commit | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 5142 | Document the engine version pinned for each serving tier | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5143 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-007 | permitted | decided fresh | — | ● |
| 5144 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5145 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5146 | Change the escalation ladder so an automated tier may accept frontier risk | FL-LS-007 | denied | decided fresh | — |  |
| 5147 | Record the prompt and context hash on each agent commit | FL-AG-006 | permitted | decided fresh | — |  |
| 5148 | Hold the audit register in a store the retrieval path cannot read | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 5149 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-003 | permitted | decided fresh | — |  |
| 5150 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-PI-005 | denied | decided fresh | — |  |
| 5151 | Test marking survivability across the video transcoder's re-encode step | FL-TR-002 | permitted | decided fresh | — |  |
| 5152 | Open the agentic tier to customers while the safety case is in draft | FL-SF-001 FL-UH-003 ⛔ | denied | refused at the floor | — |  |
| 5153 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5154 | Screen generated code against the copyleft signature database | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 5155 | Give the batch agent the shared service account to dodge quota holds | FL-FG-001 FL-TD-005 ⛔ | denied | refused at the floor | — |  |
| 5156 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5157 | Give every system prompt an immutable version identifier | FL-MB-007 | permitted | decided fresh | — |  |
| 5158 | Cover the new administrative routes in the authorization test suite | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5159 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 5160 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5161 | Attribute the standing declaration in the exported rulebook | FL-GV-009 | permitted | decided fresh | — |  |
| 5162 | Route parameter changes through the amendment workflow instead | FL-GV-009 | permitted | decided fresh | — |  |
| 5163 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-005 | permitted | decided fresh | — |  |
| 5164 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-005 | permitted | decided fresh | — |  |
| 5165 | Parameterise the new experiment-metrics filter queries | FL-AS-001 | permitted | decided fresh | — |  |
| 5166 | Log every read of the weights store to the perimeter audit trail | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 5167 | Document the engine version pinned for each serving tier | FL-IN-003 | permitted | decided fresh | — |  |
| 5168 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-003 | denied | decided fresh | — |  |
| 5169 | Compare the provenance subject digest to the distributed artifact | FL-SC-005 | permitted | disposed by citation | — |  |
| 5170 | Register the new fused kernel as a nondeterministic operation | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 5171 | Record the prompt and context hash on each agent commit | FL-AG-004 | denied | bound by precedent | REC-S0129 |  |
| 5172 | Propose narrowing the weights-perimeter provision to exclude eval clusters | FL-MB-007 | denied | decided fresh | — |  |
| 5173 | Collapse the two compute thresholds into a single configuration field | FL-GV-003 FL-FG-002 ⛔ | denied | refused at the floor | — |  |
| 5174 | Require human confirmation before the agent executes a write tool | FL-LS-011 | permitted | decided fresh | — |  |
| 5175 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-001 ⛔ | denied | refused at the floor | — |  |
| 5176 | Require two-person authorisation for unreleased-weight access | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 5177 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 5178 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-001 FL-CB-004 ⛔ | denied | refused at the floor | — |  |
| 5179 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-004 | denied | decided fresh | — | ● |
| 5180 | Name a documentation owner on every release record | FL-TR-003 | permitted | decided fresh | — |  |
| 5181 | Route critical-incident detection signals to the on-call dashboard instead of the reporting queue | FL-TR-003 | denied | decided fresh | — |  |
| 5182 | Enable batch invariance before claiming bitwise replay | FL-IN-004 | permitted | decided fresh | — |  |
| 5183 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-006 | permitted | decided fresh | — |  |
| 5184 | Label agent-authored diffs so reviewers can isolate them | FL-AG-004 | permitted | decided fresh | — |  |
| 5185 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5186 | Embed the canary string in every generated evaluation case | FL-EV-006 | permitted | decided fresh | — |  |
| 5187 | Widen the parity report to distinguish immaterial differences | FL-EV-006 | permitted | decided fresh | — |  |
| 5188 | Bake the build timestamp and hostname into the engine binary | FL-SC-001 FL-MB-005 ⛔ | denied | refused at the floor | — |  |
| 5189 | Update the third-party licence inventory with this dependency change | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5190 | Check every new import against the upstream registry before build | FL-AG-004 | permitted | disposed by citation | — |  |
| 5191 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5192 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 5193 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 5194 | Validate tenant scope on every portal export request | FL-AS-001 | permitted | decided fresh | — |  |
| 5195 | Embed the canary string in every generated evaluation case | FL-EV-003 | permitted | decided fresh | — |  |
| 5196 | Keep cases released after the training cutoff in the holdout | FL-EV-003 | permitted | decided fresh | — |  |
| 5197 | Check agent diffs for structural matches against known libraries | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5198 | Move the loop-limit requirement out of the rulebook into service defaults | FL-EV-006 | denied | decided fresh | — |  |
| 5199 | Run licence detection over every agent-authored file | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5200 | Collapse the two compute thresholds into a single configuration field | FL-GV-003 FL-EV-007 ⛔ | denied | refused at the floor | — |  |
| 5201 | Give the tool-call graph an explicit terminator | FL-FG-003 | permitted | decided fresh | — |  |
| 5202 | Let the coding agent land its router refactor on green tests alone | FL-AG-005 | denied | decided fresh | — |  |
| 5203 | Add a new exemption class to the agent sign-off rule | FL-PI-002 | denied | decided fresh | — |  |
| 5204 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 5205 | Pin workflow actions to commit digests across the release repository | FL-SC-004 | permitted | disposed by citation | — |  |
| 5206 | Hold the audit register in a store the retrieval path cannot read | FL-GV-011 | permitted with conditions | decided fresh | — | ● |
| 5207 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5208 | Let the runtime environment override the agent's recursion limit | FL-FG-001 FL-PV-002 ⛔ | denied | refused at the floor | — |  |
| 5209 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 5210 | Report preemption counts in the load-test summary | FL-IN-002 | permitted | decided fresh | — |  |
| 5211 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-009 | permitted | decided fresh | — |  |
| 5212 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-009 | permitted | decided fresh | — |  |
| 5213 | Add a new exemption class to the agent sign-off rule | FL-TD-007 | denied | decided fresh | — |  |
| 5214 | Track system-prompt versions in a free-text description field | FL-MB-002 ⛔ | denied | refused at the floor | — |  |
| 5215 | Export the distilled checkpoint as a pickle to keep the old loader | FL-MB-006 | denied | decided fresh | — |  |
| 5216 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | decided fresh | — |  |
| 5217 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5218 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5219 | Keep the automated-assistant disclosure present across every companion persona | FL-UH-003 | permitted with conditions | decided fresh | — | ● |
| 5220 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-007 | permitted | decided fresh | — |  |
| 5221 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-007 | permitted | decided fresh | — |  |
| 5222 | Alert when an agent run crosses eighty percent of its budget | FL-FG-002 | permitted | decided fresh | — |  |
| 5223 | Reject imports for packages first published within thirty days | FL-AG-008 | permitted | decided fresh | — |  |
| 5224 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5225 | Record the licence class for every corpus the crawler ingests | FL-TD-004 | permitted | decided fresh | — |  |
| 5226 | Restrict weight egress to the declared perimeter buckets | FL-SF-004 | permitted | decided fresh | — |  |
| 5227 | Gate external evaluator access on the signed agreement | FL-SF-004 | permitted | decided fresh | — |  |
| 5228 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-005 | permitted | decided fresh | — |  |
| 5229 | Route child-directed service logs into the general-purpose training-corpus builder | FL-CS-004 | denied | decided fresh | — |  |
| 5230 | Update the third-party licence inventory with this dependency change | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5231 | Return a generic error identifier instead of the stack trace | — | permitted | docketed — nothing engaged | — |  |
| 5232 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 5233 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5234 | Restrict weight egress to the declared perimeter buckets | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 5235 | Respect the robots.txt AI directive in the web crawler | FL-TD-006 | permitted | decided fresh | — |  |
| 5236 | Put a circuit breaker on the recursive summarisation path | FL-FG-003 | permitted | decided fresh | — |  |
| 5237 | Make the breaker unreachable from the agent's own configuration | FL-FG-003 | permitted | decided fresh | — |  |
| 5238 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-003 | permitted | decided fresh | — |  |
| 5239 | Add crisis-resource handoff coverage to the streaming response path | FL-UH-003 | permitted | decided fresh | — |  |
| 5240 | Change the escalation ladder so an automated tier may accept frontier risk | FL-SC-002 | denied | decided fresh | — |  |
| 5241 | Add an eval-awareness probe to the pre-release harness run | FL-CB-003 | permitted | decided fresh | — |  |
| 5242 | Run the decontamination check over the new code corpus | FL-EV-009 | permitted | decided fresh | — | ● |
| 5243 | Parameterise the new experiment-metrics filter queries | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5244 | Route flagged responses to the block path rather than a warning | FL-BS-002 | permitted | decided fresh | — |  |
| 5245 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-002 FL-GV-011 ⛔ | denied | refused at the floor | — |  |
| 5246 | Log the named authority for every override exercised | FL-GV-007 | permitted | decided fresh | — |  |
| 5247 | Let the agent render markdown images to any host the page supplies | FL-LS-001 FL-EV-003 ⛔ | denied | refused at the floor | — |  |
| 5248 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | decided fresh | — |  |
| 5249 | Widen the prompt-label review rule to cover staging labels too | FL-MB-009 | denied | decided fresh | — |  |
| 5250 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-006 | permitted with conditions | decided fresh | — | ● |
| 5251 | Add the new sampling library to the licence inventory | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 5252 | Accept attestations from the personal runner that built the hotfix | FL-SC-001 FL-SC-005 ⛔ | denied | refused at the floor | — |  |
| 5253 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-006 | permitted | decided fresh | — |  |
| 5254 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-005 | denied | decided fresh | — |  |
| 5255 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-009 | denied | decided fresh | — |  |
| 5256 | File a draft amendment carving out build-time-only dependencies | FL-FG-004 | denied | decided fresh | — |  |
| 5257 | Let the coding agent land its router refactor on green tests alone | FL-AG-001 FL-LS-005 ⛔ | denied | refused at the floor | — |  |
| 5258 | Turn off the abuse-material classifier on the image-generation path to cut moderation latency | FL-CS-001 FL-UH-004 ⛔ | denied | refused at the floor | — |  |
| 5259 | Share the key-value cache across tenants to raise the prefix-hit rate | FL-PV-003 FL-PI-002 ⛔ | denied | refused at the floor | — |  |
| 5260 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-002 | denied | decided fresh | — | ● |
| 5261 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted | decided fresh | — |  |
| 5262 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-004 | permitted | decided fresh | — |  |
| 5263 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-004 | permitted | decided fresh | — |  |
| 5264 | Put a circuit breaker on the recursive summarisation path | FL-FG-004 | permitted | decided fresh | — |  |
| 5265 | Fail the run outright when no loop limit is declared | FL-FG-006 | permitted | decided fresh | — |  |
| 5266 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5267 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-009 | permitted with conditions | decided fresh | — | ● |
| 5268 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 5269 | Record the licence class for every corpus the crawler ingests | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5270 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5271 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5272 | Check agent diffs for structural matches against known libraries | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5273 | Screen generated code against the copyleft signature database | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 5274 | Require a named owner to approve production prompt label moves | FL-MB-006 | permitted | decided fresh | — | ● |
| 5275 | Register the new fused kernel as a nondeterministic operation | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5276 | Mark the mitigation package complete once half its controls are wired | FL-CB-003 | denied | decided fresh | — |  |
| 5277 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5278 | Enable batch invariance before claiming bitwise replay | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5279 | Document which attack class the new defence was evaluated against | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5280 | State the percentile on every latency claim in the dashboard | FL-IN-006 | permitted | decided fresh | — |  |
| 5281 | Route threshold-crossing results to an automatic deployment hold | FL-CB-002 | permitted | decided fresh | — |  |
| 5282 | Verify provenance against the expected builder identity before deploy | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 5283 | Document the engine version pinned for each serving tier | FL-IN-001 | permitted | decided fresh | — |  |
| 5284 | Train on the partner's user conversations before the basis is recorded | FL-PI-006 | denied | decided fresh | — |  |
| 5285 | Queue nonconsensual-imagery takedown requests behind the general moderation backlog | FL-UH-005 | denied | decided fresh | — | ● |
| 5286 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-003 | permitted | decided fresh | — |  |
| 5287 | Pin the golden-prompt baseline to a commit digest | FL-EV-006 | permitted | decided fresh | — |  |
| 5288 | Record the tolerance band used for each accuracy comparison | FL-EV-006 | permitted | decided fresh | — |  |
| 5289 | Record the builder identity in attestations for nightly checkpoints | FL-SC-006 | permitted | decided fresh | — |  |
| 5290 | Pin workflow actions to commit digests across the release repository | FL-SC-006 | permitted | decided fresh | — |  |
| 5291 | Keep the human override reachable in the high-risk review flow | FL-GV-008 | permitted with conditions | decided fresh | — | ● |
| 5292 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5293 | Run agent-authored code only inside the sandboxed runner | FL-AG-007 | permitted | disposed by citation | — |  |
| 5294 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5295 | Require two-person authorisation for unreleased-weight access | FL-SF-007 | permitted | decided fresh | — |  |
| 5296 | Run the personal-data scan on every new training shard | FL-PI-007 | permitted with conditions | decided fresh | — | ● |
| 5297 | Restrict weight egress to the declared perimeter buckets | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 5298 | Record a disposition for every referral the board acknowledges | FL-GV-010 | permitted | decided fresh | — |  |
| 5299 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 5300 | Ship the research agent with no turn limit in its configuration | FL-FG-006 | denied | decided fresh | — |  |
| 5301 | Add an incident-reporting path test against the statutory clock | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 5302 | Enable batch invariance before claiming bitwise replay | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5303 | Cover the new administrative routes in the authorization test suite | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5304 | Validate tenant scope on every portal export request | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5305 | Export the distilled checkpoint as a pickle to keep the old loader | FL-MB-003 FL-LS-004 ⛔ | denied | refused at the floor | — |  |
| 5306 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 5307 | List only the instruct parent on the merged checkpoint card | FL-MB-002 FL-MB-005 ⛔ | denied | refused at the floor | — |  |
| 5308 | Verify transparency-log inclusion proofs in the promotion gate | FL-MB-009 | permitted | decided fresh | — |  |
| 5309 | Measure membership-inference advantage on the release candidate | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 5310 | Gate external evaluator access on the signed agreement | FL-SF-008 | permitted with conditions | decided fresh | — | ● |
| 5311 | Shorten the safety-incident retention clause in the policy repository | FL-TD-004 | denied | decided fresh | — |  |
| 5312 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted | decided fresh | — |  |
| 5313 | Make the inference-engine build hermetic and reproducible | FL-SC-005 | permitted | decided fresh | — |  |
| 5314 | Recompute the root digest from resource digests before promotion | FL-MB-009 | permitted | decided fresh | — |  |
| 5315 | Move zero-data-retention enforcement from service config into the retention code path | FL-PV-005 | permitted | decided fresh | — | ● |
| 5316 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-010 | denied | decided fresh | — |  |
| 5317 | Compare the provenance subject digest to the distributed artifact | FL-SC-006 | permitted | disposed by citation | — |  |
| 5318 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 5319 | Scan prompt templates for embedded personal data in continuous integration | FL-PI-002 | permitted | decided fresh | — |  |
| 5320 | Exclude special-category fields from the support-transcript schema | FL-PI-002 | permitted | decided fresh | — |  |
| 5321 | Run the decontamination check over the new code corpus | FL-EV-005 | permitted | bound by precedent | REC-S0113 |  |
| 5322 | Reorder the index list so the public registry answers first | FL-SC-001 FL-SC-005 ⛔ | denied | refused at the floor | — |  |
| 5323 | Track system-prompt versions in a free-text description field | FL-MB-002 FL-SC-003 ⛔ | denied | refused at the floor | — |  |
| 5324 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 5325 | Hold verbatim third-party reproduction below the span threshold | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 5326 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-002 | permitted | decided fresh | — |  |
| 5327 | Declare the arrival distribution used in the throughput benchmark | — | permitted | docketed — nothing engaged | — |  |
| 5328 | Carry attribution notices through to the shipped container image | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5329 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-006 | permitted | decided fresh | — | ● |
| 5330 | Write a docket entry for every arrival that is not charged | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 5331 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5332 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-003 | denied | decided fresh | — |  |
| 5333 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-008 | permitted | decided fresh after a tie | none_tie |  |
| 5334 | Blend the share-alike corpus into the proprietary preference set | FL-TD-007 | denied | decided fresh | — |  |
| 5335 | Loosen the toxicity cut-off in the gate config to clear the backlog | FL-BS-002 | denied | decided fresh | — |  |
| 5336 | Require a named owner to approve production prompt label moves | FL-MB-009 | permitted | decided fresh after a tie | none_tie |  |
| 5337 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh | — |  |
| 5338 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-007 | permitted | decided fresh | — |  |
| 5339 | Add audio-generation coverage to the abuse-material classifier suite | FL-CS-003 | permitted | decided fresh | — |  |
| 5340 | Run licence detection over every agent-authored file | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5341 | Measure judge and human agreement for the new grader configuration | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 5342 | Split personal-data handling out of the shared ingestion library | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 5343 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5344 | Scan responses for canary tokens before they leave the gateway | FL-LS-005 | permitted | decided fresh | — |  |
| 5345 | Remove the canary check from the response filter to cut latency | FL-LS-001 FL-PI-006 ⛔ | denied | refused at the floor | — |  |
| 5346 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-005 | permitted | decided fresh | — |  |
| 5347 | Recompute the root digest from resource digests before promotion | FL-MB-005 | permitted | decided fresh | — |  |
| 5348 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-004 | permitted | decided fresh | — |  |
| 5349 | Disable the self-exfiltration probe in the agent sandbox to fix a flaky test | FL-CB-001 FL-SC-006 ⛔ | denied | refused at the floor | — |  |
| 5350 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-010 | permitted | decided fresh | — |  |
| 5351 | Route flagged responses to the block path rather than a warning | FL-BS-004 | permitted | decided fresh | — | ● |
| 5352 | Declare the arrival distribution used in the throughput benchmark | FL-IN-001 | permitted | decided fresh | — | ● |
| 5353 | Remove the sandbagging detector from the eval harness to simplify the report | FL-CB-002 | denied | decided fresh | — |  |
| 5354 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 5355 | Store the provenance chain for derived synthetic corpora | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5356 | Retire two supply-chain provisions from the rulebook manifest | FL-GV-006 | denied | decided fresh | — |  |
| 5357 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 5358 | Declare both base models in the merged cirrus-small manifest | FL-MB-008 | permitted | decided fresh | — |  |
| 5359 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5360 | Propose an amendment codifying coverage rules for generated eval configs | FL-SC-003 | denied | decided fresh | — |  |
| 5361 | Shorten the safety-incident retention clause in the policy repository | FL-EV-007 | denied | decided fresh | — |  |
| 5362 | Declare the agent loop limit numerically with its units | FL-FG-005 | permitted | decided fresh | — |  |
| 5363 | Fail the run outright when no loop limit is declared | FL-FG-005 | permitted | decided fresh | — |  |
| 5364 | Sample the de-identified shard weekly and report the residual rate | FL-PI-002 | denied | bound by precedent | REC-S0169 |  |
| 5365 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 5366 | Run agent-authored code only inside the sandboxed runner | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5367 | Pin the key-value cache budget for the agentic serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5368 | Move authorization checks out of the client and into the gateway | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5369 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 5370 | Enable batch invariance before claiming bitwise replay | FL-IN-006 | permitted | decided fresh | — |  |
| 5371 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-011 | denied | decided fresh | — |  |
| 5372 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-003 | permitted | decided fresh | — |  |
| 5373 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted | decided fresh | — | ● |
| 5374 | Document the subject-request path for the preference store | FL-PI-005 | permitted | decided fresh | — |  |
| 5375 | Screen new fine-tuning shards for backdoor triggers | FL-LS-006 | permitted with conditions | bound by precedent | REC-S0101 |  |
| 5376 | Widen the parity report to distinguish immaterial differences | FL-EV-008 | permitted | decided fresh after a tie | none_tie |  |
| 5377 | Pin the golden-prompt baseline to a commit digest | FL-EV-009 | denied | bound by precedent | REC-S0171 |  |
| 5378 | Let retrieval read audit findings so precedent search returns more | FL-GV-011 | denied | decided fresh | — |  |
| 5379 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5380 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-003 | denied | decided fresh | — |  |
| 5381 | Move cost control from a meter to a pre-flight breaker | FL-FG-003 | permitted | decided fresh | — |  |
| 5382 | Alert when an agent run crosses eighty percent of its budget | FL-FG-003 | permitted | decided fresh | — |  |
| 5383 | Run the decontamination check over the new code corpus | FL-EV-003 | permitted | decided fresh | — |  |
| 5384 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 5385 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-002 | permitted | decided fresh | — |  |
| 5386 | Add regression coverage for the minor-interaction safeguard suite | FL-CS-004 | permitted | decided fresh | — |  |
| 5387 | Gate consumer account creation on a passed age-assurance check server-side | FL-CS-004 | permitted | decided fresh | — |  |
| 5388 | Replace the manual denied-party screening spreadsheet with an automated gateway check | FL-WX-002 | permitted | decided fresh | — |  |
| 5389 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-002 | permitted | decided fresh | — |  |
| 5390 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-002 FL-EV-006 ⛔ | denied | refused at the floor | — |  |
| 5391 | Draft an amendment introducing a jurisdiction-specific compute threshold | FL-AG-006 | denied | decided fresh | — |  |
| 5392 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5393 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5394 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-003 | permitted | decided fresh | — |  |
| 5395 | Retire two supply-chain provisions from the rulebook manifest | FL-AG-008 | denied | decided fresh | — |  |
| 5396 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 5397 | Change the escalation ladder so an automated tier may accept frontier risk | FL-LS-010 | denied | decided fresh | — |  |
| 5398 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-002 | permitted | decided fresh | — |  |
| 5399 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5400 | Train on the partner's user conversations before the basis is recorded | FL-PI-007 | denied | decided fresh | — |  |
| 5401 | Block promotion until the dangerous-capability reports complete | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 5402 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-005 | permitted | decided fresh | — |  |
| 5403 | Export the rulebook without the standing declaration block | FL-GV-006 | denied | decided fresh | — |  |
| 5404 | Ship the release with technical documentation carried over from the prior version | FL-TR-001 FL-PI-002 ⛔ | denied | refused at the floor | — |  |
| 5405 | Ship the checkpoint past the uplift screen while the mitigation package is still in draft | FL-CB-001 FL-PI-007 ⛔ | denied | refused at the floor | — |  |
| 5406 | Strip internal identifiers from gateway error responses | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5407 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 5408 | Strip annotator identity from the exported preference dataset | FL-PV-005 | permitted | decided fresh | — |  |
| 5409 | Pin the golden-prompt baseline to a commit digest | FL-EV-003 | permitted | decided fresh | — |  |
| 5410 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-003 | permitted | decided fresh | — |  |
| 5411 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | decided fresh | — |  |
| 5412 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-003 | denied | decided fresh | — |  |
| 5413 | Keep reporter bulletins off the adjudication input path | FL-GV-005 | permitted | decided fresh | — |  |
| 5414 | Record a disposition for every referral the board acknowledges | FL-GV-005 | permitted | decided fresh | — |  |
| 5415 | Restrict weight egress to the declared perimeter buckets | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 5416 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 5417 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted with conditions | bound by precedent | REC-S0107 |  |
| 5418 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5419 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 5420 | Declare the carrier channel for each untrusted input source | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 5421 | Attach Croissant metadata to the new publisher corpus | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5422 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 5423 | Route parameter changes through the amendment workflow instead | FL-GV-007 | permitted with conditions | decided fresh | — | ● |
| 5424 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5425 | Make the breaker unreachable from the agent's own configuration | FL-FG-004 | permitted | decided fresh | — |  |
| 5426 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-011 | denied | decided fresh | — |  |
| 5427 | Fail the build when an agent commit arrives unsigned | FL-AG-005 | permitted | decided fresh | — |  |
| 5428 | Cache the erasure-propagation status per request for the duration of the statutory window | FL-PV-001 | permitted | decided fresh | — |  |
| 5429 | Cover the new administrative routes in the authorization test suite | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5430 | Move the loop-limit requirement out of the rulebook into service defaults | FL-GV-009 | denied | decided fresh | — |  |
| 5431 | Validate tenant scope on every portal export request | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5432 | Roll out the new grader configuration without an agreement study | FL-EV-004 | denied | decided fresh | — |  |
| 5433 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-003 FL-SC-008 ⛔ | denied | refused at the floor | — |  |
| 5434 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-003 | permitted with conditions | decided fresh | — | ● |
| 5435 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5436 | Declare the downstream sink for every model output field | FL-LS-008 | permitted | decided fresh after a tie | none_tie |  |
| 5437 | Move retrieved documents into a separate, clearly marked context block | FL-LS-007 | permitted | decided fresh | — |  |
| 5438 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh | — |  |
| 5439 | Roll out the new grader configuration without an agreement study | FL-EV-009 | denied | decided fresh | — |  |
| 5440 | Make the breaker unreachable from the agent's own configuration | FL-FG-002 | permitted | decided fresh | — |  |
| 5441 | Redact prompt and completion logs before they reach retention | FL-PI-005 | permitted | decided fresh | — |  |
| 5442 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 5443 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5444 | Add the medical-referral handoff to the high-stakes-advice system prompt | FL-UH-002 | permitted with conditions | decided fresh | — | ● |
| 5445 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-007 | permitted | decided fresh | — |  |
| 5446 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-001 | permitted | decided fresh | — |  |
| 5447 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 5448 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted | decided fresh | — |  |
| 5449 | Parameterise the new experiment-metrics filter queries | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5450 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5451 | Store the provenance chain for derived synthetic corpora | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5452 | Migrate the remaining distilled checkpoints to safetensors on export | FL-MB-004 | permitted | decided fresh | — | ● |
| 5453 | Ship the image whose layer digests no longer match the recorded inventory | FL-SC-002 | denied | decided fresh | — |  |
| 5454 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 5455 | Reject imports for packages first published within thirty days | FL-AG-006 | permitted | decided fresh | — |  |
| 5456 | Run release builds on ephemeral runners with pinned images | FL-SC-007 | permitted | disposed by citation | — |  |
| 5457 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-004 | denied | decided fresh | — |  |
| 5458 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-004 | denied | decided fresh | — |  |
| 5459 | Require human confirmation before the agent executes a write tool | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5460 | Block internal address ranges in the web-fetch tool | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5461 | Hold the audit register in a store the retrieval path cannot read | FL-GV-010 | permitted | decided fresh | — |  |
| 5462 | Attribute the standing declaration in the exported rulebook | FL-GV-010 | permitted | decided fresh | — |  |
| 5463 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 5464 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 5465 | Record the compute-threshold determination separately per jurisdiction | FL-GV-010 | permitted | decided fresh | — |  |
| 5466 | Route parameter changes through the amendment workflow instead | FL-GV-010 | permitted | decided fresh | — |  |
| 5467 | Screen new fine-tuning shards for backdoor triggers | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 5468 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 5469 | Run the uplift eval on the safety-trained checkpoint without the elicitation prompts | FL-CB-004 | denied | decided fresh | — |  |
| 5470 | Attach Croissant metadata to the new publisher corpus | FL-TD-004 | permitted | decided fresh | — |  |
| 5471 | Store the provenance chain for derived synthetic corpora | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5472 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-008 | permitted | decided fresh | — |  |
| 5473 | Respect the robots.txt AI directive in the web crawler | FL-TD-006 | permitted | decided fresh | — | ● |
| 5474 | Measure membership-inference advantage on the release candidate | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 5475 | Block promotion until the dangerous-capability reports complete | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 5476 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5477 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | decided fresh | — |  |
| 5478 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted | decided fresh | — |  |
| 5479 | Disable the self-exfiltration probe in the agent sandbox to fix a flaky test | FL-CB-002 | denied | decided fresh | — |  |
| 5480 | Respect the robots.txt AI directive in the web crawler | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5481 | Document the subject-request path for the preference store | FL-PI-005 | permitted | decided fresh | — |  |
| 5482 | Publish the prompt-log retention clock in the customer portal | FL-PI-005 | permitted | decided fresh | — |  |
| 5483 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-009 | permitted with conditions | decided fresh | — | ● |
| 5484 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 5485 | Report first-token and per-token latency against the tier budgets | — | permitted | docketed — nothing engaged | — |  |
| 5486 | Record the agent identity on every quota decision | FL-FG-006 | permitted | decided fresh | — |  |
| 5487 | Scan responses for canary tokens before they leave the gateway | FL-LS-005 | permitted | decided fresh | — |  |
| 5488 | Require human confirmation before the agent executes a write tool | FL-LS-005 | permitted | decided fresh | — |  |
| 5489 | Hardcode a real customer address into the escalation prompt template | FL-PI-003 | denied | decided fresh | — |  |
| 5490 | Fail the build on scan findings above the severity threshold | FL-SC-005 | permitted with conditions | bound by precedent | REC-S0099 |  |
| 5491 | Escape tool output before it reaches the shell adapter | FL-LS-007 | permitted | decided fresh | — | ● |
| 5492 | Hold agentic-checkpoint promotion on a completed autonomy-eval result | FL-CB-002 | permitted | decided fresh | — |  |
| 5493 | Raise mitigations to match the assessed capability level | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 5494 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-002 | permitted | decided fresh | — | ● |
| 5495 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5496 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-004 | permitted | decided fresh | — |  |
| 5497 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5498 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted | decided fresh | — |  |
| 5499 | Restrict deserialisation to the declared tool-payload types | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5500 | Restrict deserialisation to the declared tool-payload types | — | permitted | docketed — nothing engaged | — |  |
| 5501 | Route law-enforcement data requests through legal review before fulfilment | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 5502 | Replace the unit-test grader with a model judge for speed | FL-EV-002 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 5503 | Separate the production prompt label from its version string | FL-MB-008 | permitted | decided fresh | — |  |
| 5504 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 5505 | Add anomaly-detection coverage to the training-cluster egress monitor | FL-WX-003 | permitted | decided fresh | — |  |
| 5506 | Have trade counsel sign the export-classification determination record | FL-WX-003 | permitted | decided fresh | — |  |
| 5507 | Fail the run outright when no loop limit is declared | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 5508 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | denied | bound by precedent | REC-S0131 |  |
| 5509 | Publish the release without an updated training-content summary | FL-TR-001 FL-SC-007 ⛔ | denied | refused at the floor | — |  |
| 5510 | Record the tolerance band used for each accuracy comparison | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 5511 | Declare the carrier channel for each untrusted input source | FL-LS-007 | permitted | decided fresh | — |  |
| 5512 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-011 | permitted | decided fresh | — |  |
| 5513 | Escape tool output before it reaches the shell adapter | FL-LS-011 | permitted | decided fresh | — |  |
| 5514 | Report first-token and per-token latency against the tier budgets | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5515 | Serve the high-capability checkpoint under the previous tier's mitigations | FL-SF-003 FL-TD-004 ⛔ | denied | refused at the floor | — |  |
| 5516 | Separate the audit register from the precedent store at schema level | FL-GV-004 | permitted | decided fresh | — |  |
| 5517 | Give every system prompt an immutable version identifier | FL-MB-006 | permitted | decided fresh | — |  |
| 5518 | Re-run the probe after the distillation step, not before it | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5519 | Fail the build on scan findings above the severity threshold | FL-SC-006 | permitted | disposed by citation | — |  |
| 5520 | Document the subject-request path for the preference store | FL-PI-006 | permitted | decided fresh | — |  |
| 5521 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | decided fresh | — | ● |
| 5522 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5523 | Return a generic error identifier instead of the stack trace | — | permitted | docketed — nothing engaged | — |  |
| 5524 | Validate tenant scope on every portal export request | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5525 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5526 | Fail closed when a dataset licence string does not parse | FL-TD-003 | permitted | decided fresh | — |  |
| 5527 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-002 | permitted | decided fresh | — |  |
| 5528 | Store the provenance chain for derived synthetic corpora | FL-TD-002 | permitted | decided fresh | — |  |
| 5529 | Publish a review checklist for agent changes to the eval harness | FL-AG-007 | permitted | decided fresh after a tie | none_tie |  |
| 5530 | Accept attestations from the personal runner that built the hotfix | FL-SC-007 | denied | decided fresh | — |  |
| 5531 | Drop the two unpinned actions from the checkpoint export workflow | FL-SC-004 | permitted | decided fresh | — | ● |
| 5532 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-001 | permitted | decided fresh | — |  |
| 5533 | Add a new exemption class to the agent sign-off rule | FL-SC-003 | denied | decided fresh | — |  |
| 5534 | Parameterise the new experiment-metrics filter queries | — | permitted | docketed — nothing engaged | — |  |
| 5535 | Parameterise the new experiment-metrics filter queries | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5536 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5537 | Recompute the root digest from resource digests before promotion | FL-MB-009 | permitted | decided fresh | — |  |
| 5538 | Reject artifacts whose served hash differs from the registry entry | FL-MB-009 | permitted | decided fresh | — |  |
| 5539 | Record attribution for the reused tokenizer snippet | FL-IP-003 | denied | bound by precedent | REC-S0207 |  |
| 5540 | Disable debug capture entirely for zero-retention tenant traffic | FL-PV-004 | permitted with conditions | decided fresh | — | ● |
| 5541 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-004 | permitted with conditions | decided fresh | — | ● |
| 5542 | Keep the self-harm classifier active at its approved threshold through the model refresh | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 5543 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted with conditions | decided fresh | — | ● |
| 5544 | Run the cyber eval on a ten-task subset and report it as the full protocol | FL-CB-001 FL-IN-002 ⛔ | denied | refused at the floor | — |  |
| 5545 | Keep the toxicity filter in the response path for streaming replies | FL-BS-004 | permitted | decided fresh | — | ● |
| 5546 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5547 | Keep rate limits and output perturbation on the completions endpoint | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5548 | Give every system prompt an immutable version identifier | FL-MB-004 | permitted | decided fresh after a tie | none_tie |  |
| 5549 | Cap fan-out on the parallel sub-agent scheduler | FL-FG-002 | permitted | decided fresh | — |  |
| 5550 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-005 | denied | decided fresh | — | ● |
| 5551 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5552 | Exclude special-category fields from the support-transcript schema | FL-PI-003 | permitted with conditions | decided fresh | — | ● |
| 5553 | Screen generated code against the copyleft signature database | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 5554 | Record the frontier framework version in force on the release record | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 5555 | Fail the build on scan findings above the severity threshold | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5556 | Move the crisis classifier from the response filter into the token-streaming path itself | FL-UH-002 | permitted | decided fresh | — |  |
| 5557 | Keep the election-integrity classifier in the release gate through the electoral cycle | FL-UH-002 | permitted | decided fresh | — |  |
| 5558 | Reject artifacts whose served hash differs from the registry entry | FL-MB-005 | permitted | disposed by citation | — |  |
| 5559 | Make the inference-engine build hermetic and reproducible | FL-SC-008 | permitted | decided fresh | — |  |
| 5560 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — |  |
| 5561 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5562 | Hold the audit register in a store the retrieval path cannot read | FL-GV-008 | permitted | decided fresh | — |  |
| 5563 | Publish the adverse-contest figure as two counts, not a ratio | FL-GV-008 | permitted | decided fresh | — |  |
| 5564 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-006 | permitted | decided fresh | — |  |
| 5565 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 5566 | Record the availability type on every newly onboarded source | FL-TD-006 | permitted | decided fresh | — |  |
| 5567 | Extend refusal coverage to the multilingual harmful-prompt set | FL-BS-003 | permitted | decided fresh | — |  |
| 5568 | Validate tenant scope on every portal export request | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5569 | Raise mitigations to match the assessed capability level | FL-SF-006 | permitted | decided fresh | — | ● |
| 5570 | Strip the notice file from the container image to shrink the layer | FL-IP-001 ⛔ | denied | refused at the floor | — |  |
| 5571 | Hold verbatim third-party reproduction below the span threshold | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5572 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5573 | Onboard the new chat source without running the de-identification sample | FL-PI-003 | denied | decided fresh | — | ● |
| 5574 | Fail closed when a dataset licence string does not parse | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5575 | Skip signature verification on load to cut startup time | FL-MB-002 FL-SF-005 ⛔ | denied | refused at the floor | — |  |
| 5576 | Set the planner's recursion limit to zero, meaning unlimited | FL-FG-006 | denied | decided fresh | — |  |
| 5577 | Blend the share-alike corpus into the proprietary preference set | FL-TD-003 | denied | decided fresh | — |  |
| 5578 | Attribute the standing declaration in the exported rulebook | FL-GV-010 | permitted with conditions | decided fresh | — | ● |
| 5579 | Ingest the health-survey responses with the special-category gate off | FL-PI-001 FL-TD-005 ⛔ | denied | refused at the floor | — |  |
| 5580 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-005 | permitted with conditions | decided fresh | — | ● |
| 5581 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | permitted | decided fresh | — |  |
| 5582 | Replace the companion persona's static disclosure line with one rendered per session | FL-UH-003 | permitted | decided fresh | — |  |
| 5583 | Return a generic error identifier instead of the stack trace | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5584 | Run the decontamination check over the new code corpus | FL-EV-003 | permitted | decided fresh | — |  |
| 5585 | Gate promotion on the full safety suite, not the fast subset | FL-EV-003 | permitted | decided fresh | — |  |
| 5586 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted | decided fresh | — |  |
| 5587 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-002 | permitted | decided fresh | — |  |
| 5588 | Measure demographic disparity across the ambiguous-context suite | FL-BS-002 | permitted | decided fresh | — |  |
| 5589 | Fuzz the changed completions parameters before release | — | permitted | docketed — nothing engaged | — |  |
| 5590 | Record the capability-threshold determination on the release record | FL-SF-007 | permitted | decided fresh | — |  |
| 5591 | Attribute the standing declaration in the exported rulebook | FL-GV-004 | permitted | decided fresh | — |  |
| 5592 | Teach the assistant to answer unknown when the context is ambiguous | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 5593 | Move release signing keys onto the hardware security module | FL-SF-007 | permitted | decided fresh after a tie | none_tie |  |
| 5594 | Shorten the report-preservation window in the retention job to ninety days | FL-CS-002 ⛔ | denied | refused at the floor | — |  |
| 5595 | Shorten the safety-incident retention clause in the policy repository | FL-EV-008 | denied | decided fresh | — |  |
| 5596 | Propagate attribution obligations from corpus records to release notes | FL-TD-003 | permitted | decided fresh | — |  |
| 5597 | Route parameter changes through the amendment workflow instead | FL-GV-008 | permitted | decided fresh | — |  |
| 5598 | Let the coding agent land its router refactor on green tests alone | FL-AG-007 | denied | decided fresh | — |  |
| 5599 | Reject unexpected content types on the tool-callback endpoint | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5600 | Embed the canary string in every generated evaluation case | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 5601 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5602 | Respect the robots.txt AI directive in the web crawler | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5603 | Widen the parity report to distinguish immaterial differences | FL-EV-004 | permitted with conditions | decided fresh | — | ● |
| 5604 | Redact prompt and completion logs before they reach retention | FL-PI-007 | permitted | decided fresh | — |  |
| 5605 | Alert when an agent run crosses eighty percent of its budget | FL-FG-002 | permitted with conditions | decided fresh | — | ● |
| 5606 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 5607 | Submit an amendment retiring the deferred data-governance clauses early | FL-SC-002 | denied | decided fresh | — |  |
| 5608 | Route parameter changes through the amendment workflow instead | FL-GV-004 | permitted | decided fresh | — |  |
| 5609 | Declare both base models in the merged cirrus-small manifest | FL-MB-006 | permitted | decided fresh | — |  |
| 5610 | Publish a signed bill of materials covering transitive dependencies | FL-SC-003 | permitted | decided fresh | — | ● |
| 5611 | Run release builds on ephemeral runners with pinned images | FL-SC-007 | permitted | decided fresh | — |  |
| 5612 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted | decided fresh | — |  |
| 5613 | Record trainedOn and finetunedOn edges on the checkpoint record | FL-MB-007 | permitted | decided fresh | — |  |
| 5614 | Fail the build on scan findings above the severity threshold | FL-SC-003 | permitted | disposed by citation | — |  |
| 5615 | Enforce vetting-record expiry automatically in the access-control system | FL-WX-002 | permitted | decided fresh | — |  |
| 5616 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-002 | permitted | decided fresh | — |  |
| 5617 | Escape tool output before it reaches the shell adapter | FL-LS-005 | permitted | decided fresh | — |  |
| 5618 | Validate tenant scope on every portal export request | — | permitted | docketed — nothing engaged | — |  |
| 5619 | Keep cases released after the training cutoff in the holdout | FL-EV-009 | permitted | decided fresh | — |  |
| 5620 | Keep the toxicity filter in the response path for streaming replies | FL-BS-003 | permitted | decided fresh | — |  |
| 5621 | Validate tenant scope on every portal export request | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5622 | Retire two supply-chain provisions from the rulebook manifest | FL-UH-003 | denied | decided fresh | — |  |
| 5623 | Escape tool output before it reaches the shell adapter | FL-LS-003 | permitted | decided fresh | — | ● |
| 5624 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-003 | permitted | decided fresh | — | ● |
| 5625 | Check persona guidance against the shipped system prompt | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 5626 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-005 | permitted | decided fresh | — | ● |
| 5627 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-004 | permitted | decided fresh | — |  |
| 5628 | Measure judge and human agreement for the new grader configuration | FL-EV-003 | permitted | bound by precedent | REC-S0121 |  |
| 5629 | Import a streaming-metrics helper the agent invented from nothing | FL-AG-005 | denied | decided fresh | — |  |
| 5630 | Land the fallback that quietly turns draft-model decoding off | FL-EV-004 | denied | decided fresh | — |  |
| 5631 | Remove the canary check from the response filter to cut latency | FL-LS-002 FL-MB-006 ⛔ | denied | refused at the floor | — |  |
| 5632 | Record the prompt and context hash on each agent commit | FL-AG-006 | permitted | decided fresh | — |  |
| 5633 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh | — |  |
| 5634 | Require the safety-case signature from outside the authoring team | FL-SF-004 | permitted with conditions | decided fresh | — | ● |
| 5635 | Reject unexpected content types on the tool-callback endpoint | — | permitted | docketed — nothing engaged | — |  |
| 5636 | Enforce the instruction and data boundary on the retrieval path | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5637 | Record the tolerance band used for each accuracy comparison | FL-EV-008 | permitted | decided fresh | — |  |
| 5638 | Pin the golden-prompt baseline to a commit digest | FL-EV-008 | permitted | decided fresh | — |  |
| 5639 | Require human confirmation before the agent executes a write tool | FL-LS-010 | permitted | decided fresh after a tie | none_tie |  |
| 5640 | Stream tokens to the client before the toxicity filter has scored them | FL-BS-002 | denied | bound by precedent | REC-FL-B-01260 |  |
| 5641 | Pin the key-value cache budget for the agentic serving tier | FL-IN-001 | permitted with conditions | decided fresh | — | ● |
| 5642 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-001 FL-GV-010 ⛔ | denied | refused at the floor | — |  |
| 5643 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted with conditions | decided fresh | — | ● |
| 5644 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 5645 | Measure membership-inference advantage on the release candidate | FL-LS-003 | permitted | decided fresh | — |  |
| 5646 | Open the agentic tier to customers while the safety case is in draft | FL-SF-003 FL-UH-004 ⛔ | denied | refused at the floor | — |  |
| 5647 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5648 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-006 | permitted | decided fresh | — | ● |
| 5649 | Enable batch invariance before claiming bitwise replay | FL-IN-002 | permitted | decided fresh | — |  |
| 5650 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 5651 | Make the inference-engine build hermetic and reproducible | FL-SC-002 | permitted | decided fresh | — |  |
| 5652 | Wire a deletion hook so withdrawn conversations leave the corpus | FL-PI-005 | permitted | decided fresh | — | ● |
| 5653 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-005 | permitted | decided fresh | — |  |
| 5654 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5655 | Escape tool output before it reaches the shell adapter | FL-LS-005 | permitted with conditions | bound by precedent | REC-S0105 |  |
| 5656 | Grant a new hire weight-store access before the vetting record clears | FL-WX-001 ⛔ | denied | refused at the floor | — |  |
| 5657 | Downgrade the default incident-severity classification to avoid triggering the reporting clock | FL-TR-004 FL-CB-002 ⛔ | denied | refused at the floor | — |  |
| 5658 | Publish the prompt-log retention clock in the customer portal | FL-PI-005 | permitted with conditions | bound by precedent | REC-S0097 |  |
| 5659 | Record a disposition for every referral the board acknowledges | FL-GV-004 | permitted | decided fresh | — |  |
| 5660 | Respect the robots.txt AI directive in the web crawler | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 5661 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-003 | permitted | decided fresh | — |  |
| 5662 | Declare the arrival distribution used in the throughput benchmark | FL-IN-003 | permitted | decided fresh | — |  |
| 5663 | Fail the build on scan findings above the severity threshold | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5664 | Move the autonomy eval from a nightly job into the promotion gate itself | FL-CB-002 | permitted | decided fresh | — |  |
| 5665 | Add a weekly sampling job over production refusals | FL-BS-003 | permitted | decided fresh | — |  |
| 5666 | Attach Croissant metadata to the new publisher corpus | FL-TD-008 | permitted with conditions | decided fresh | — | ● |
| 5667 | Drop the failing refusal suite from the promotion gate this train | FL-EV-002 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 5668 | Reject artifacts whose served hash differs from the registry entry | FL-MB-009 | permitted | decided fresh | — |  |
| 5669 | Ship the tokenizer config inside the model bundle unsigned | FL-MB-001 FL-LS-003 ⛔ | denied | refused at the floor | — |  |
| 5670 | Add a weekly sampling job over production refusals | FL-BS-005 | permitted | decided fresh | — |  |
| 5671 | Transfer the checkpoint to the partner cluster before classification is recorded | FL-WX-003 | denied | decided fresh | — |  |
| 5672 | Move the loop-limit requirement out of the rulebook into service defaults | FL-SF-008 | denied | decided fresh | — |  |
| 5673 | Export the rulebook without the standing declaration block | FL-GV-002 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 5674 | Remove the cache ceiling so long sessions stop being evicted | FL-IN-002 | denied | decided fresh | — |  |
| 5675 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-006 | permitted | decided fresh | — |  |
| 5676 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-006 | permitted | decided fresh | — |  |
| 5677 | Record a lawful basis for each conversation-data source | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 5678 | Hold goodput at the tier threshold under the burst profile | — | permitted | docketed — nothing engaged | — |  |
| 5679 | Separate the production prompt label from its version string | FL-MB-008 | permitted | disposed by citation | — |  |
| 5680 | Write a docket entry for every arrival that is not charged | FL-GV-004 | permitted | decided fresh | — |  |
| 5681 | Drop the opt-out signal check from the crawler to raise page yield | FL-TD-002 | denied | decided fresh | — |  |
| 5682 | Document the subject-request path for the preference store | FL-PI-004 | permitted | decided fresh | — |  |
| 5683 | Record the agent identity on every quota decision | FL-FG-006 | permitted | decided fresh | — |  |
| 5684 | Move retrieved documents into a separate, clearly marked context block | FL-LS-005 | permitted | decided fresh | — |  |
| 5685 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-005 | denied | decided fresh | — |  |
| 5686 | Propagate erasure requests from the deletion API into the training-manifest exclusion list | FL-PV-004 | permitted | decided fresh | — |  |
| 5687 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-004 | permitted | decided fresh | — |  |
| 5688 | Give the tool-call graph an explicit terminator | FL-FG-003 | permitted | decided fresh | — |  |
| 5689 | Check agent diffs for structural matches against known libraries | FL-IP-002 | permitted | bound by precedent | REC-S0206 |  |
| 5690 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5691 | Exclude paywalled pages from the crawl frontier entirely | FL-TD-007 | permitted | decided fresh | — |  |
| 5692 | Give the judge an explicit tie disposition instead of forcing a choice | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 5693 | Give the coding agent its own short-lived signing credential | FL-AG-004 | denied | bound by precedent | REC-S0129 |  |
| 5694 | Fail the build when an agent commit arrives unsigned | FL-AG-007 | permitted | decided fresh | — |  |
| 5695 | Block promotion until the dangerous-capability reports complete | FL-SF-004 | permitted | decided fresh | — |  |
| 5696 | Check every new import against the upstream registry before build | FL-AG-007 | permitted | disposed by citation | — |  |
| 5697 | Raise the capability threshold in the policy repository | FL-SC-004 | denied | decided fresh | — |  |
| 5698 | Resolve the conflicting licence claims on the academic mirror first | FL-TD-007 | permitted | decided fresh | — |  |
| 5699 | Require a human reviewer on agent changes to request routing | FL-AG-005 | permitted | decided fresh | — |  |
| 5700 | Require an external evaluator attestation on the cyber-uplift results | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 5701 | Move authorization checks out of the client and into the gateway | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5702 | Let the retrieval index answer queries across the tenant boundary during a migration | FL-PV-004 | denied | decided fresh | — |  |
| 5703 | Fail closed when a dataset licence string does not parse | FL-TD-006 | permitted | decided fresh | — |  |
| 5704 | Attribute the standing declaration in the exported rulebook | FL-GV-010 | permitted | decided fresh | — |  |
| 5705 | Verify provenance against the expected builder identity before deploy | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5706 | Make decision records append-only in the store schema | FL-GV-008 | permitted | decided fresh | — |  |
| 5707 | Keep the human override reachable in the high-risk review flow | FL-GV-008 | permitted | decided fresh | — |  |
| 5708 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5709 | Declare sample size and percentile alongside the parity result | FL-EV-009 | permitted | decided fresh | — |  |
| 5710 | Restrict weight egress to the declared perimeter buckets | FL-SF-006 | permitted | decided fresh after a tie | none_tie |  |
| 5711 | Exclude special-category fields from the support-transcript schema | FL-PI-003 | permitted | decided fresh | — |  |
| 5712 | Document the subject-request path for the preference store | FL-PI-003 | permitted | decided fresh | — |  |
| 5713 | Skip the crisis classifier on streaming responses to keep first-token latency low | FL-UH-005 | denied | decided fresh | — |  |
| 5714 | Cover the new administrative routes in the authorization test suite | FL-AS-001 | permitted | decided fresh | — |  |
| 5715 | Exclude the election-integrity classifier from this release's gate | FL-UH-001 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 5716 | Add release-gate coverage that fails when content marking is missing from any modality | FL-TR-002 | permitted with conditions | decided fresh | — | ● |
| 5717 | Run the decontamination check over the new code corpus | FL-EV-006 | permitted | decided fresh | — |  |
| 5718 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 5719 | Check every new import against the upstream registry before build | FL-AG-005 | permitted | decided fresh | — |  |
| 5720 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 5721 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-006 | denied | decided fresh | — |  |
| 5722 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5723 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | decided fresh | — |  |
| 5724 | Strip internal identifiers from gateway error responses | — | permitted | docketed — nothing engaged | — |  |
| 5725 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-005 | permitted | decided fresh | — |  |
| 5726 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5727 | Record the frontier framework version in force on the release record | FL-SF-008 | denied | bound by precedent | REC-S0177 |  |
| 5728 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 5729 | Let the agent mark the failing provenance test as skipped | FL-AG-003 FL-AG-007 ⛔ | denied | refused at the floor | — |  |
| 5730 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5731 | Keep the toxicity filter in the response path for streaming replies | FL-BS-006 | permitted with conditions | decided fresh | — | ● |
| 5732 | Store the provenance chain for derived synthetic corpora | FL-TD-003 | permitted | decided fresh | — |  |
| 5733 | Strip internal identifiers from gateway error responses | — | permitted | docketed — nothing engaged | — |  |
| 5734 | Project token spend before dispatching a long-horizon agent run | FL-FG-006 | permitted | decided fresh | — |  |
| 5735 | Add synthetic-content marking to the audio-generation output path | FL-TR-002 | permitted | decided fresh | — |  |
| 5736 | Publish the frontier transparency report ahead of the deployment date | FL-TR-002 | permitted | decided fresh | — |  |
| 5737 | Stop reading the loop limit from an environment variable | FL-FG-006 | permitted | decided fresh | — |  |
| 5738 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5739 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-004 | denied | decided fresh | — |  |
| 5740 | Promote the hotfix checkpoint without rerunning the uplift screens | FL-SF-003 FL-MB-008 ⛔ | denied | refused at the floor | — |  |
| 5741 | Parameterise the new experiment-metrics filter queries | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5742 | Cover the new administrative routes in the authorization test suite | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5743 | Reject unexpected content types on the tool-callback endpoint | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5744 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-001 FL-TR-003 ⛔ | denied | refused at the floor | — |  |
| 5745 | Add an eval-awareness probe to the pre-release harness run | FL-CB-003 | permitted with conditions | decided fresh | — | ● |
| 5746 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | denied | bound by precedent | REC-S0167 |  |
| 5747 | Enforce the instruction and data boundary on the retrieval path | FL-LS-003 | denied | bound by precedent | REC-S0133 |  |
| 5748 | Merge the streaming path whose profile still leaks after warm-up | FL-IN-002 | denied | decided fresh | — |  |
| 5749 | Run the persona and tone evaluation on the release build | FL-BS-003 | permitted | decided fresh | — |  |
| 5750 | Collapse the two compute thresholds into a single configuration field | FL-GV-008 | denied | decided fresh | — |  |
| 5751 | Ingest the kids'-app conversation logs into the training corpus without a consent record | FL-CS-003 | denied | decided fresh | — |  |
| 5752 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted | decided fresh | — |  |
| 5753 | Measure judge and human agreement for the new grader configuration | FL-EV-010 | permitted | decided fresh | — |  |
| 5754 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-004 | permitted with conditions | decided fresh | — | ● |
| 5755 | Hold goodput at the tier threshold under the burst profile | FL-IN-002 | permitted | decided fresh | — |  |
| 5756 | Run the personal-data scan on every new training shard | FL-PI-006 | permitted | decided fresh after a tie | none_tie |  |
| 5757 | Let the agent edit the release workflow to unblock its own branch | FL-AG-001 FL-LS-008 ⛔ | denied | refused at the floor | — |  |
| 5758 | Record the frontier framework version in force on the release record | FL-SF-007 | permitted with conditions | decided fresh | — | ● |
| 5759 | Rebuild the base image to clear the outstanding transport advisory | FL-SC-007 | permitted | decided fresh | — |  |
| 5760 | Pin workflow actions to commit digests across the release repository | FL-SC-007 | permitted | decided fresh | — |  |
| 5761 | Run the decontamination check over the new code corpus | FL-EV-003 | permitted with conditions | decided fresh | — | ● |
| 5762 | Enforce the instruction and data boundary on the retrieval path | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 5763 | Make the inference-engine build hermetic and reproducible | FL-SC-007 | permitted | decided fresh | — | ● |
| 5764 | Declare the carrier channel for each untrusted input source | FL-LS-008 | permitted | decided fresh | — |  |
| 5765 | Log the named authority for every override exercised | FL-GV-004 | permitted | decided fresh | — |  |
| 5766 | Report refusal and over-refusal rates side by side | FL-BS-002 | permitted | decided fresh | — |  |
| 5767 | Report refusal and over-refusal rates side by side | FL-BS-002 | permitted | decided fresh | — |  |
| 5768 | Exercise injection detection on the changed tool-calling path | FL-LS-009 | permitted | decided fresh | — |  |
| 5769 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5770 | File a draft amendment carving out build-time-only dependencies | FL-SF-004 | denied | decided fresh | — |  |
| 5771 | Publish a review checklist for agent changes to the eval harness | FL-AG-006 | permitted | disposed by citation | — |  |
| 5772 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-003 | denied | decided fresh | — | ● |
| 5773 | Move retrieved documents into a separate, clearly marked context block | FL-LS-005 | permitted | decided fresh | — |  |
| 5774 | Remove the crisis-resource handoff from the consumer response path | FL-UH-001 FL-EV-007 ⛔ | denied | refused at the floor | — |  |
| 5775 | Record the builder identity in attestations for nightly checkpoints | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5776 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5777 | Fail closed when a dataset licence string does not parse | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 5778 | Ship the support-transcript shard before the personal-data scan finishes | FL-PI-004 | denied | decided fresh | — |  |
| 5779 | Declare sample size and percentile alongside the parity result | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 5780 | Default unparsed licence strings to permissive so ingestion stops stalling | FL-TD-001 FL-TD-003 ⛔ | denied | refused at the floor | — |  |
| 5781 | Remove the contest link from the customer decision notice | FL-GV-001 FL-LS-005 ⛔ | denied | refused at the floor | — |  |
| 5782 | Have the crawler submit the consent form to reach the archive body | FL-TD-001 FL-SC-004 ⛔ | denied | refused at the floor | — |  |
| 5783 | Record a lawful basis for each conversation-data source | FL-PI-004 | permitted | decided fresh | — | ● |
| 5784 | Test marking survivability across the video transcoder's re-encode step | FL-TR-002 | permitted | decided fresh | — |  |
| 5785 | Make the government-request log append-only across the bulk-export path | FL-PV-001 | permitted | decided fresh | — |  |
| 5786 | Turn off egress monitoring on the weight store during the migration window | FL-WX-001 FL-AG-006 ⛔ | denied | refused at the floor | — |  |
| 5787 | Pin the abuse-material hash-list refresh job to a daily schedule | FL-CS-003 | permitted | decided fresh | — |  |
| 5788 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5789 | Narrow the export-classification form to the fields trade counsel actually reviews | FL-WX-002 | permitted | decided fresh | — |  |
| 5790 | Record the builder identity in attestations for nightly checkpoints | FL-SC-004 | permitted | decided fresh | — | ● |
| 5791 | Expose a contest path to affected customers in the portal | FL-GV-004 | permitted | decided fresh | — |  |
| 5792 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-002 | permitted | decided fresh | — |  |
| 5793 | Record the capability-threshold determination on the release record | FL-SF-007 | permitted | decided fresh | — | ● |
| 5794 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5795 | Respect the robots.txt AI directive in the web crawler | FL-TD-002 | permitted | decided fresh | — | ● |
| 5796 | Report first-token and per-token latency against the tier budgets | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5797 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 5798 | Ship the debug echo mode that replays the full system prompt on request | FL-LS-002 ⛔ | denied | refused at the floor | — |  |
| 5799 | Document the engine version pinned for each serving tier | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5800 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-004 | permitted | decided fresh | — |  |
| 5801 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 5802 | Hold the audit register in a store the retrieval path cannot read | FL-GV-008 | permitted | decided fresh | — |  |
| 5803 | Record the capability-threshold determination on the release record | FL-SF-005 | permitted with conditions | bound by precedent | REC-S0109 |  |
| 5804 | Declare sample size and percentile alongside the parity result | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 5805 | Strip internal identifiers from gateway error responses | FL-AS-001 | permitted | decided fresh | — |  |
| 5806 | Edit stored decision records in place to correct their rationale text | FL-GV-003 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 5807 | Parameterise the new experiment-metrics filter queries | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5808 | Publish the signing certificate chain alongside each release digest | FL-MB-009 | permitted | disposed by citation | — |  |
| 5809 | Widen the prompt-label review rule to cover staging labels too | FL-SF-008 | denied | decided fresh | — |  |
| 5810 | Open the agentic tier to customers while the safety case is in draft | FL-SF-008 | denied | decided fresh | — |  |
| 5811 | Enforce server-side authorization on the new batch endpoint | FL-AS-005 | permitted | docketed — not charged | — |  |
| 5812 | Export the rulebook without the standing declaration block | FL-GV-001 FL-CB-004 ⛔ | denied | refused at the floor | — |  |
| 5813 | Release the run record with the threshold determination left blank | FL-SF-007 | denied | decided fresh | — |  |
| 5814 | Restrict weight egress to the declared perimeter buckets | FL-SF-004 | permitted | decided fresh | — |  |
| 5815 | Localise the crisis-resource handoff copy for every served jurisdiction | FL-UH-004 | permitted with conditions | decided fresh | — | ● |
| 5816 | Rebenchmark on the same hardware and engine version as the baseline | FL-IN-006 | permitted | decided fresh | — |  |
| 5817 | Skip the autonomy eval for the agentic checkpoint since last week's run passed | FL-CB-001 FL-FG-005 ⛔ | denied | refused at the floor | — |  |
| 5818 | Enable batch invariance before claiming bitwise replay | FL-IN-005 | permitted | decided fresh | — |  |
| 5819 | Remove insider-anomaly detection from the training cluster to cut alert noise | FL-WX-004 FL-EV-004 ⛔ | denied | refused at the floor | — |  |
| 5820 | Widen the parity report to distinguish immaterial differences | FL-EV-010 | permitted | decided fresh | — |  |
| 5821 | Sample the de-identified shard weekly and report the residual rate | FL-PI-005 | permitted with conditions | decided fresh | — | ● |
| 5822 | Split safety-case authoring and approval into distinct workflow roles | FL-SF-005 | permitted | decided fresh | — |  |
| 5823 | Merge the attention rewrite while the parity run still shows disagreement | FL-EV-004 | denied | decided fresh | — | ● |
| 5824 | Run the decontamination check over the new code corpus | FL-EV-007 | permitted | decided fresh | — |  |
| 5825 | Run licence detection over every agent-authored file | FL-IP-005 | denied | bound by precedent | REC-S0209 |  |
| 5826 | Restrict deserialisation to the declared tool-payload types | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5827 | Rewrite the last raw query in the usage-reporting job | — | permitted | docketed — nothing engaged | — |  |
| 5828 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 5829 | Validate tenant scope on every portal export request | FL-AS-002 | permitted | docketed — not charged | — |  |
| 5830 | Vendor an internal-sounding package that no upstream registry carries | FL-AG-007 | denied | decided fresh | — |  |
| 5831 | Document which attack class the new defence was evaluated against | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 5832 | Replace the abuse-material classifier's legacy matcher with the clearinghouse's current API | FL-CS-003 | permitted | decided fresh | — |  |
| 5833 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-006 | denied | bound by precedent | REC-S0173 |  |
| 5834 | Enforce the instruction and data boundary on the retrieval path | FL-LS-007 | permitted | decided fresh after a tie | none_tie |  |
| 5835 | Edit the toxicity threshold directly through the adjudication service credentials | FL-TR-003 | denied | decided fresh | — |  |
| 5836 | Backfill lineage records for the older quantised checkpoints | FL-MB-009 | permitted | disposed by citation | — |  |
| 5837 | Drop rate limits on the completions endpoint for the benchmark partner | FL-LS-009 | denied | decided fresh | — |  |
| 5838 | Record the compute-threshold determination separately per jurisdiction | FL-GV-004 | permitted | decided fresh | — |  |
| 5839 | Track system-prompt versions in a free-text description field | FL-MB-002 FL-FG-002 ⛔ | denied | refused at the floor | — |  |
| 5840 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-004 | permitted | decided fresh | — |  |
| 5841 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-004 FL-PV-005 ⛔ | denied | refused at the floor | — |  |
| 5842 | Publish the training-content summary from the current release's manifest | FL-TR-003 | permitted | decided fresh | — |  |
| 5843 | Quarantine ticket text before it reaches the agent's instruction slot | FL-AG-008 | permitted | decided fresh | — |  |
| 5844 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-002 | permitted | decided fresh | — |  |
| 5845 | Disable the persuasion-policy check for the new campaign-tenant account | FL-UH-004 | denied | decided fresh | — |  |
| 5846 | Fuzz the changed completions parameters before release | FL-AS-006 | permitted | docketed — not charged | — |  |
| 5847 | Embed the canary string in every generated evaluation case | FL-EV-006 | permitted with conditions | decided fresh | — | ● |
| 5848 | Route nonconsensual-imagery takedown requests ahead of the general moderation queue | FL-UH-002 | permitted with conditions | decided fresh | — | ● |
| 5849 | Raise mitigations to match the assessed capability level | FL-SF-004 | permitted | bound by precedent | REC-S0117 |  |
| 5850 | Publish the prompt-log retention clock in the customer portal | FL-PI-006 | permitted with conditions | decided fresh | — | ● |
| 5851 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5852 | Publish a signed bill of materials covering transitive dependencies | FL-SC-004 | permitted | decided fresh | — | ● |
| 5853 | Block sexual content server-side whenever the minor flag is set on an account | FL-UH-002 | permitted | decided fresh | — |  |
| 5854 | Keep cases released after the training cutoff in the holdout | FL-EV-008 | permitted with conditions | decided fresh | — | ● |
| 5855 | Raise the capability threshold in the policy repository | FL-AG-006 | denied | decided fresh | — |  |
| 5856 | Publish the signing certificate chain alongside each release digest | FL-MB-006 | permitted | disposed by citation | — |  |
| 5857 | Record a disposition for every referral the board acknowledges | FL-GV-009 | permitted | decided fresh | — |  |
| 5858 | Declare the downstream sink for every model output field | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 5859 | Strip internal identifiers from gateway error responses | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5860 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted | decided fresh | — |  |
| 5861 | Run agent-authored code only inside the sandboxed runner | FL-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5862 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-005 | permitted | decided fresh | — |  |
| 5863 | Shorten the report-preservation window in the retention job to ninety days | FL-CS-003 | denied | decided fresh | — |  |
| 5864 | File a draft amendment carving out build-time-only dependencies | FL-WX-003 | denied | decided fresh | — |  |
| 5865 | Record a lawful basis for each conversation-data source | FL-PI-003 | permitted | decided fresh | — |  |
| 5866 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted | decided fresh | — |  |
| 5867 | Return a generic error identifier instead of the stack trace | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5868 | Hold verbatim third-party reproduction below the span threshold | FL-IP-006 | permitted | bound by precedent | REC-S0210 |  |
| 5869 | Widen the parity report to distinguish immaterial differences | FL-EV-009 | permitted | decided fresh | — |  |
| 5870 | Gate promotion on the full safety suite, not the fast subset | FL-EV-009 | permitted | decided fresh | — |  |
| 5871 | Remove the medical-referral handoff from the assistant's system prompt | FL-UH-001 ⛔ | denied | refused at the floor | — |  |
| 5872 | Inline retrieved documents into the system prompt to save tokens | FL-LS-001 FL-MB-004 ⛔ | denied | refused at the floor | — |  |
| 5873 | Name a data-governance custodian on each dataset record | FL-TD-008 | permitted | decided fresh | — |  |
| 5874 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-008 | permitted | decided fresh | — |  |
| 5875 | Set the planner's recursion limit to zero, meaning unlimited | FL-FG-001 ⛔ | denied | refused at the floor | — |  |
| 5876 | Assert speculative decoding is still engaged during the accuracy run | FL-EV-006 | permitted | decided fresh | — |  |
| 5877 | Attach Croissant metadata to the new publisher corpus | FL-TD-006 | permitted | decided fresh | — |  |
| 5878 | Keep reporter bulletins off the adjudication input path | FL-GV-004 | permitted | decided fresh | — |  |
| 5879 | Redact prompt and completion logs before they reach retention | FL-PI-004 | permitted | decided fresh | — |  |
| 5880 | Declare sample size and percentile alongside the parity result | FL-EV-010 | permitted | decided fresh | — |  |
| 5881 | Run the tensor leak check after warm-up in the nightly profile | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5882 | Feed the weekly reporter bulletin into the adjudicator's context window | FL-GV-006 | denied | decided fresh | — |  |
| 5883 | Deploy the gateway image the broken pipeline produced without attestation | FL-SC-004 | denied | decided fresh | — |  |
| 5884 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5885 | Record the agent identity on every quota decision | FL-FG-004 | permitted | decided fresh | — |  |
| 5886 | Attach a model bill of materials to the atlas-instruct release job | FL-MB-007 | permitted | bound by precedent | REC-S0111 |  |
| 5887 | Fail closed when a dataset licence string does not parse | FL-TD-004 | permitted | decided fresh | — |  |
| 5888 | Promote the checkpoint that reproduces the canary identifier on request | FL-EV-010 | denied | decided fresh | — | ● |
| 5889 | Name a data-governance custodian on each dataset record | FL-TD-005 | permitted with conditions | decided fresh | — | ● |
| 5890 | Measure membership-inference advantage on the release candidate | FL-LS-006 | permitted | decided fresh | — |  |
| 5891 | Register the new fused kernel as a nondeterministic operation | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5892 | Route threshold-crossing results to an automatic deployment hold | FL-CB-003 | permitted | decided fresh | — |  |
| 5893 | Verify de-identification by sampling rather than by assertion | FL-PI-004 | permitted | decided fresh | — |  |
| 5894 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5895 | Propose allowing sampled rather than exhaustive licence detection | FL-PV-004 | denied | decided fresh | — |  |
| 5896 | Enforce the unlearning exclusion list at the start of every training run | FL-PV-005 | permitted | decided fresh | — |  |
| 5897 | Flag noncommercial corpora so commercial runs cannot select them | FL-TD-007 | permitted | decided fresh | — | ● |
| 5898 | Fail closed when a dataset licence string does not parse | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5899 | Halt the pipeline when shard distribution drifts past its variance bound | FL-LS-011 | permitted | decided fresh after a tie | none_tie |  |
| 5900 | Turn off commit signing for the agent runner while its key rotates | FL-AG-002 FL-AG-007 ⛔ | denied | refused at the floor | — |  |
| 5901 | Report first-token and per-token latency against the tier budgets | — | permitted | docketed — nothing engaged | — |  |
| 5902 | Keep the chunked-prefill change inside the five percent latency budget | FL-IN-006 | permitted | decided fresh | — |  |
| 5903 | Reduce over-refusal on the safe-prompt contrast set | FL-BS-002 | permitted | decided fresh | — |  |
| 5904 | Move authorization checks out of the client and into the gateway | — | permitted | docketed — nothing engaged | — |  |
| 5905 | Publish a signed bill of materials covering transitive dependencies | FL-SC-003 | permitted | decided fresh | — |  |
| 5906 | Make decision records append-only in the store schema | FL-GV-004 | permitted | decided fresh | — |  |
| 5907 | Land the new forum corpus with its provenance fields left blank | FL-TD-002 | denied | decided fresh | — |  |
| 5908 | Run the tensor leak check after warm-up in the nightly profile | — | permitted | docketed — nothing engaged | — |  |
| 5909 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-004 | permitted with conditions | decided fresh | — | ● |
| 5910 | Hold the audit register in a store the retrieval path cannot read | FL-GV-004 | permitted | decided fresh | — |  |
| 5911 | Give the batch agent the shared service account to dodge quota holds | FL-FG-001 FL-UH-004 ⛔ | denied | refused at the floor | — |  |
| 5912 | Resolve internal packages from the private registry first | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5913 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5914 | Restrict deserialisation to the declared tool-payload types | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5915 | Alert when an agent run crosses eighty percent of its budget | FL-FG-003 | permitted | decided fresh | — |  |
| 5916 | Load a customer's fine-tune adapter for another tenant's inference request | FL-PV-005 | denied | decided fresh | — | ● |
| 5917 | Record the availability type on every newly onboarded source | FL-TD-008 | permitted | decided fresh | — |  |
| 5918 | Log the named authority for every override exercised | FL-GV-007 | permitted | decided fresh | — |  |
| 5919 | Attribute the standing declaration in the exported rulebook | FL-GV-007 | permitted | decided fresh | — |  |
| 5920 | Gate deployment on the mitigation package's verified effectiveness, not its checklist state | FL-CB-004 | permitted with conditions | decided fresh | — | ● |
| 5921 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5922 | Wire incident-detection signals directly into the statutory reporting queue | FL-TR-002 | permitted with conditions | decided fresh | — | ● |
| 5923 | Attach the impact assessment to the user-feedback fine-tuning pipeline | FL-PI-002 | permitted | decided fresh | — | ● |
| 5924 | Move authorization checks out of the client and into the gateway | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5925 | Run the decontamination check over the new code corpus | FL-EV-006 | permitted | decided fresh | — |  |
| 5926 | Transfer the checkpoint to the partner cluster before classification is recorded | FL-WX-002 | denied | decided fresh | — |  |
| 5927 | Propagate attribution obligations from corpus records to release notes | FL-TD-004 | permitted | decided fresh | — |  |
| 5928 | Attach Croissant metadata to the new publisher corpus | FL-TD-005 | permitted | decided fresh | — |  |
| 5929 | Verify provenance against the expected builder identity before deploy | FL-SC-002 | denied | bound by precedent | REC-S0175 |  |
| 5930 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-004 | permitted | decided fresh | — |  |
| 5931 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-007 | permitted with conditions | decided fresh | — | ● |
| 5932 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5933 | Let the agent edit the release workflow to unblock its own branch | FL-AG-002 FL-EV-008 ⛔ | denied | refused at the floor | — |  |
| 5934 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-003 | permitted with conditions | decided fresh | — | ● |
| 5935 | Add Portuguese and Hindi to the toxicity evaluation set | FL-BS-005 | permitted | decided fresh | — |  |
| 5936 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 5937 | Require the safety-case signature from outside the authoring team | FL-SF-005 | permitted with conditions | decided fresh | — | ● |
| 5938 | Replace the unit-test grader with a model judge for speed | FL-EV-002 FL-BS-002 ⛔ | denied | refused at the floor | — |  |
| 5939 | Bound key-value cache growth under concurrency in the scheduler | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5940 | Consolidate the medical, legal and financial handoff prompts into one shared template | FL-UH-005 | permitted | decided fresh | — |  |
| 5941 | Feed raw customer ticket text into the agent's instruction slot | FL-AG-008 | denied | decided fresh | — |  |
| 5942 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TR-003 | denied | decided fresh | — |  |
| 5943 | Repack the shard files after signing and reuse the old manifest | FL-MB-003 ⛔ | denied | refused at the floor | — |  |
| 5944 | Parameterise the new experiment-metrics filter queries | FL-AS-004 | permitted | docketed — not charged | — |  |
| 5945 | Swap the model judge for an exact checker on arithmetic tasks | FL-EV-006 | permitted | decided fresh | — |  |
| 5946 | Leave weight-store access active after an engineer rotates off the safety team | FL-WX-001 FL-SC-003 ⛔ | denied | refused at the floor | — |  |
| 5947 | Run the persuasion eval on every release candidate ahead of an election window | FL-UH-005 | permitted | decided fresh | — |  |
| 5948 | Enable batch invariance before claiming bitwise replay | FL-IN-008 | permitted | docketed — not charged | — |  |
| 5949 | Sample the de-identified shard weekly and report the residual rate | FL-PI-002 | permitted | decided fresh | — |  |
| 5950 | Hold the toxicity threshold at its approved value through the refactor | FL-BS-005 | permitted | decided fresh | — |  |
| 5951 | Run semantic analysis over the agent diff in continuous integration | FL-AG-006 | permitted | disposed by citation | — |  |
| 5952 | Hold the checkpoint at canary until the uplift screen clears | FL-SF-009 | permitted | decided fresh after a tie | none_tie |  |
| 5953 | Keep cases released after the training cutoff in the holdout | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 5954 | Roll out the new grader configuration without an agreement study | FL-EV-003 | denied | decided fresh | — | ● |
| 5955 | Skip propagating erasure requests from the deletion API into the training-manifest sync job | FL-PV-003 FL-AG-008 ⛔ | denied | refused at the floor | — |  |
| 5956 | Exclude the election-integrity classifier from this release's gate | FL-UH-001 ⛔ | denied | refused at the floor | — |  |
| 5957 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5958 | Submit an amendment retiring the deferred data-governance clauses early | FL-CB-003 | denied | decided fresh | — |  |
| 5959 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5960 | Pin the golden-prompt baseline to a commit digest | FL-EV-007 | denied | bound by precedent | REC-S0127 |  |
| 5961 | Target the retention fine-tune at users the model scores as vulnerable | FL-GV-005 | denied | decided fresh | — |  |
| 5962 | Evaluate share-alike terms before mixing the annotated preference set | FL-TD-004 | permitted | decided fresh | — |  |
| 5963 | Relax the coverage floor in the policy bundle to unblock a release train | FL-TD-006 | denied | decided fresh | — |  |
| 5964 | Pin every dependency to an immutable digest in the lockfile | FL-SC-002 | permitted | disposed by citation | — |  |
| 5965 | Ship the image whose layer digests no longer match the recorded inventory | FL-SC-006 | denied | decided fresh | — |  |
| 5966 | Declare both base models in the merged cirrus-small manifest | FL-MB-009 | permitted | decided fresh | — |  |
| 5967 | Skip the hash-match scan on fast-path shards to clear the ingestion pipeline backlog | FL-CS-001 ⛔ | denied | refused at the floor | — |  |
| 5968 | Publish the prompt-log retention clock in the customer portal | FL-PI-003 | permitted | decided fresh | — |  |
| 5969 | Mark the mitigation package complete once half its controls are wired | FL-CB-003 | denied | decided fresh | — |  |
| 5970 | Record the availability type on every newly onboarded source | FL-TD-003 | permitted with conditions | decided fresh | — | ● |
| 5971 | Enforce data-worker graphic-content exposure limits in the labeling queue | FL-PV-001 | permitted | decided fresh | — |  |
| 5972 | Keep the human override reachable in the high-risk review flow | FL-GV-007 | permitted | decided fresh | — |  |
| 5973 | Report first-token and per-token latency against the tier budgets | FL-IN-007 | permitted | docketed — not charged | — |  |
| 5974 | Diff the model card against the previous release before publishing | FL-TR-003 | permitted | decided fresh | — |  |
| 5975 | Route law-enforcement data requests straight to on-call fulfilment, skipping the legal-review queue | FL-PV-003 FL-IN-003 ⛔ | denied | refused at the floor | — |  |
| 5976 | Quarantine copyleft-matching completions before they reach the editor | FL-IP-004 | denied | bound by precedent | REC-S0208 |  |
| 5977 | Exercise injection detection on the changed tool-calling path | FL-LS-009 | permitted with conditions | bound by precedent | REC-S0095 |  |
| 5978 | Bump the serialisation library to a version carrying a critical advisory | FL-SC-006 | denied | decided fresh | — |  |
| 5979 | Cover the new administrative routes in the authorization test suite | — | permitted | docketed — nothing engaged | — |  |
| 5980 | Make decision records append-only in the store schema | FL-GV-011 | permitted | decided fresh | — |  |
| 5981 | Fail the build when an agent commit arrives unsigned | FL-AG-006 | permitted | decided fresh | — | ● |
| 5982 | Honour machine-readable text-and-data-mining opt-outs at crawl time | FL-TD-002 | permitted with conditions | decided fresh | — | ● |
| 5983 | Fuzz the changed completions parameters before release | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5984 | Collapse the two compute thresholds into a single configuration field | FL-GV-004 | denied | decided fresh | — |  |
| 5985 | Resolve internal packages from the private registry first | FL-SC-007 | permitted | decided fresh | — |  |
| 5986 | Keep raw prompt logs for ninety days to make debugging easier | FL-PI-004 | denied | decided fresh | — |  |
| 5987 | Run the uplift eval on the helpful-only variant ahead of the safety-trained one | FL-CB-004 | permitted | decided fresh | — |  |
| 5988 | Record the licence class for every corpus the crawler ingests | FL-TD-002 | permitted | decided fresh | — |  |
| 5989 | Propose allowing sampled rather than exhaustive licence detection | FL-SC-008 | denied | decided fresh | — |  |
| 5990 | Rewrite the last raw query in the usage-reporting job | FL-AS-003 | permitted | docketed — not charged | — |  |
| 5991 | Log every read of the weights store to the perimeter audit trail | FL-SF-006 | permitted with conditions | decided fresh | — | ● |
| 5992 | Write a docket entry for every arrival that is not charged | FL-GV-009 | permitted with conditions | decided fresh | — | ● |
| 5993 | Escape tool output before it reaches the shell adapter | FL-LS-004 | denied | bound by precedent | REC-S0137 |  |
| 5994 | Sync unreleased shards to an external bucket for cross-region resume | FL-SF-001 FL-WX-002 ⛔ | denied | refused at the floor | — |  |
| 5995 | Measure judge and human agreement for the new grader configuration | FL-EV-010 | denied | bound by precedent | REC-S0135 |  |
| 5996 | Widen the weight-store egress allowlist to any destination for the resume job | FL-WX-003 | denied | decided fresh | — |  |
| 5997 | Cover the high-stakes refusal-and-handoff path in the regression suite | FL-UH-005 | permitted with conditions | decided fresh | — | ● |
| 5998 | Write matched shards into the training corpus before the quarantine step finishes | FL-CS-002 ⛔ | denied | refused at the floor | — |  |
| 5999 | Apply an allowlist to the retrieval connector's target parameter | FL-AS-006 | permitted | docketed — not charged | — |  |
| 6000 | Parameterise the new experiment-metrics filter queries | FL-AS-003 | permitted | docketed — not charged | — |  |

⛔ marks a change that engaged an absolute provision — a floor no officer of this organisation has the authority to waive.

## How to check any of this

```
python3 harness/run_conformance.py     # 44 checks over the executed trace
python3 harness/mutation_matrix.py     # evidence the checks can fail
bash reproduce/run_all.sh              # rebuild everything, deterministically
```

Every row above is produced by replaying the corpus through `harness/engine.py`. No row is copied from an authored expectation, so the ledger cannot drift from the corpus files.
