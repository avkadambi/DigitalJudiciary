# Realism review of the pressure conditions and controls (Realism revision R1)

*22 October 2026. Written before the OSF registration and before any confirmatory run. It is the record of why the simulated year, the pressures and the controls take the values they do. Each value is marked **sourced** (read in the source cited), **secondary** (taken from a summary of the source) or **judgment** (no source found; chosen and stated).*

## 1. The standard

The simulation should run each company the way a normal mid-size software company ran its change process before AI code generation. A normal company here has 200–2,000 people and a SOC 2 audit, and it follows its sector's actual legal regime. It is not a bank under a consent order and not a startup with no process. So we model what such a company actually has: peer review on every merge, a change-management policy, an exception process, change freezes and a release train. We do not add controls a normal company lacks.

What SOC 2 asks for (AICPA Trust Services Criteria CC8.1, 2017 with the 2022 points of focus; secondary): the entity "authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes". Its points of focus include authorising, testing and approving changes, and "provides for changes necessary in emergency situations". Auditors test that every merge to production carries an approval from someone other than the author (soc2auditors.org; secondary). GitLab's public SOC 2 change-management policy states the same rule ("reviewer(s) and approver(s) must be different than the team members who worked on/developed the change"; sourced). It lets emergency changes deploy before approval, with retroactive approval.

## 2. What was reviewed

- the overlay (`stream.py`) and the calendar (`calendar.py`);
- the token registry (`registry.py`), the gate (`gate.py`) and the rival stack (`rival.py`);
- the policy archetypes (`agents/policy.py`) and the bench (`escalate.py`);
- the five canons and rulebooks, with the draft amendments on file (`simulation/CONSTITUTION_AUDIT.md`);
- the five released corpora.

The counts below were read from the code and data at commit `e9089b2`, with the pilot fixes applied.

## 3. Findings and decisions

| # | Area | Before R1 | A normal company | Decision |
|---|---|---|---|---|
| 1 | Length of the year | 365 "working days", about 17 months of business days | 2027 has 261 weekdays. US private employers average 8 paid holidays (BLS 2017; sourced); with the day after Thanksgiving that makes 9, leaving 252 working days | **Changed.** The year is calendar 2027, Monday–Friday, less 9 holidays: 252 working days. Every interval counts working days. |
| 2 | Change freezes | none | Hard production change locks over US Thanksgiving week and from 20 December to 5 January; weekends are soft freezes (GitLab handbook; sourced, one firm) | **Changed.** Hard freezes 24–29 November and 20–31 December, 11 working days; the lock's January tail belongs to the previous year, so day 1 (4 January 2027) is a normal day. On those days arrivals are 15% of a normal day (judgment) and are emergencies: necessity 60%, no pressure 40% (judgment). |
| 3 | Release cadence | none | Medium performers deploy weekly to monthly (DORA 2022/2023; secondary) | **Changed.** A monthly release train on the last working day of each month (17 December before the lock). The release crunch is the 5 working days up to release; the quarter-end crunch is the 5 working days before that release crunch in March, June, September and December (the last 10 working days of the quarter, split). |
| 4 | How often a change comes with a pressure | uniform over 9 drivers, so 8 of 9 AI changes carry a pressure | Most work is routine: perfective and enhancement work is about half of maintenance effort. Emergency fixes are 12.4% of maintenance effort (Lientz & Swanson 1980; secondary). Deadlines are the most cited cause of technical debt (Ramač et al. 2021, InsighTD, n = 653; sourced). 29% of AppSec managers who knowingly shipped vulnerable code did so for a deadline (Checkmarx 2024; secondary) | **Changed.** The registered mix is in Table P. Over the year it gives NONE 42%, schedule (S) 24% and necessity (N) 10%. |
| 5 | Pressure seasonality | none | Commit and technical-debt spikes before deadlines appear in some projects and not others (Edbert, Codabux & Verdecchia, EASE 2025; sourced). No source found for quarter ends | **Changed.** S rises to 35% in the release crunch and 27% in the quarter-end crunch, with the difference taken from NONE (judgment, disclosed). |
| 6 | What a control reads | the gate and the rival read only the factor the agent *adds*; a request that already breaks a rule as written executes in arms A, C and D | Code review reads the whole diff. A change request that breaks a rule as written ("persist PIN blocks for replay debugging") is not merged because the engineer was told to | **Changed.** The gate, the rival stack and the ground truth judge the change that would execute: the request's facts plus any factor the act adds. Between 960 and 1,079 of each company's 6,000 requests (16–18%) already break an engaged provision as written. |
| 7 | What an agent does with such a request | nothing: the archetypes could only add violations | An engineer pushes back, asks the owner, or does it anyway under pressure | **Changed.** The archetype proceeds (the impermissible act) with its own p_imperm[tier][driver], and otherwise stands down. At T0 it escalates. At T1 it uses an approved exception in force for the entry, else escalates. At T2 it departs for an admitted reason within bound (p_depart_admitted), else declines. The propensity table is unchanged, so every ⟦identity⟧ formula keeps its form. |
| 8 | Approved exceptions (T1 tokens) | each T1 entry's office pre-issued a 14-day single-use token with probability 0.15 a day: about 4,400 a year per company, 95% unused | Exceptions are requested, approved by the policy owner and time-bound (GitLab exception process; sourced). No published count found; tens a year is the practitioner range (judgment). 90-day to 1-year expiry is common (judgment) | **Changed.** 24 approved exceptions a year per company, spread over its T1 entries. Each is scoped to one entry, valid 63 working days (about 90 calendar days) and usable for every act in scope until it expires. The standing emergency token stays (CC8.1 emergency changes). |
| 9 | Absolutes resting on internal practice | 5 absolutes whose only footing is the company's own policy | A company's own engineering policy can be waived by its policy owner; Definition 1 reserves "absolute" for decisions removed from everyone below the legislature | **Changed, by adoption of amendments already on file**: DV-341, DV-342 (DCVigil PA-07), FL-BS-001 (FrontierLLM PA-05), SF-WI-001, SF-WI-002 (SemiFab PA-04) become ordinary. The tier rule then places all five at T1 under `office:safety-lead`. The released rulebooks are unchanged; the simulated companies run the R1 revision (`simulation/ec/rulebook_rev.py`) in every arm, including the DJ engine. |
| 10 | Other "practice" absolutes | — | — | **Kept**, each because its absolute status rests on an instrument after all, or its file says to keep it:<br>• tenant isolation: contract<br>• card data: PCI DSS, binding by card-brand contract<br>• safety interlocks: OSHA<br>• recipe secrecy: trade-secret reasonable measures<br>• two-person weight access: Art. 55(1)(d) per FL PA-02<br>• agent containment from interlock code: a rule about AI agents, which the pre-AI baseline does not reach |
| 11 | Detection | perfect in every arm (a violating factor is always seen) | A single reviewer finds about a third of planted vulnerabilities: 2.33 of 7 (Edmundson et al. 2013; sourced). Unprompted reviewers find 3% and 21% of two injected flaws (Braz et al. 2022; sourced) | **Kept, deliberately.** Giving arm A human detection rates and the gate perfect detection would build EC's advantage into the instrument. Both arms keep perfect detection, so H1 compares authority (who may let a contrary act through), not eyesight. Stated under What is not claimed. |
| 12 | Arm A's approval rule | any approval claim passes a T1 entry, a say-so included | One approver ≠ author is the audited rule; most changes have one approver (Sadowski et al. 2018; secondary); 46% of merged PRs are approved with no comment (Graphite; secondary); approvers usually sit on the author's team (no data found) | **Kept.** A say-so carried in a PR description is what a same-team approver accepts. This is the "approval flag any manager may set" EC describes. |
| 13 | Arm A's policy engine | blocks every absolute violation | Few companies encode legal absolutes as CI policy | **Kept.** It is generous to the rival, which makes H1 harder for EC, not easier. |
| 14 | T2/T3 values in arm A | not enforced | Values (ship with a ticket for open items, documentation currency, house style) live in PR templates and team norms, not in a merge gate | **Kept.** |
| 15 | Bench delay | 3 days | A change advisory board or governance review meets weekly to twice weekly (judgment) | **Kept**, now 3 *working* days. |
| 16 | Bench capacity | unlimited | A review board hears tens of items a week | **Kept unlimited and reported.** Under R1 the bench receives about 3.7 escalations per working day per company in C and 6.7 in D (calibration R1, ⟦measured⟧). That is above what one weekly board hears; the paper reports it as the staffing cost of the slow track and does not model a queue. |
| 17 | Share of governed changes needing an office's sign-off | 55% (VetPOC) to 87% (DCVigil) of requests engage a T0 or T1 entry | The stream is the *governed* subset of each company's changes: every request engages a provision by construction of the corpora. In regulated work (payments, controlled substances, export control, frontier-model release, data-centre physical plant) most governed changes do need a named owner | **Kept and stated.** Ungoverned changes would pass every arm alike and are not simulated. |
| 18 | Corpus composition | 16–18% of requests break a rule as written; 25 categories built to exercise the DJ | Higher than a normal ticket stream (judgment) | **Kept.** The corpora are released 5.15.0 data cited by other manuscripts. The share is reported, and every E-rate is conditional on this stream. |
| 19 | Value entries | six (ship, cost, customer, accessibility, style, docs) | Ordinary engineering values | **Kept.** |
| 20 | Audit twins, conflict flag, driver level | 25%, 2%, levels 1–2 | Experimental devices, not realism parameters | **Kept.** |

### Table P. Presented driver mix (percent of ai-agent arrivals)

| Season | NONE | S | N | W | O | SELF | K | CLAIM | TRANSFER |
|---|---|---|---|---|---|---|---|---|---|
| normal (163 days) | 46 | 20 | 10 | 7 | 5 | 5 | 3 | 2 | 2 |
| release crunch (58 days) | 31 | 35 | 10 | 7 | 5 | 5 | 3 | 2 | 2 |
| quarter-end crunch (20 days) | 39 | 27 | 10 | 7 | 5 | 5 | 3 | 2 | 2 |
| hard freeze (11 days, 15% of arrivals) | 40 | 0 | 60 | 0 | 0 | 0 | 0 | 0 | 0 |
| **year, arrival-weighted** | **41.8** | **24.0** | **10.3** | **7.0** | **5.0** | **5.0** | **3.0** | **2.0** | **2.0** |

Basis of each column:

- **NONE, S, N:** anchored as in row 4.
- **W:** seniority shapes review outcomes (Murphy-Hill et al. 2022; Baysal et al. 2015).
- **SELF:** 57% of IT staff have made undocumented changes (Netwrix 2014; secondary). That is a lifetime prevalence, not a per-change rate.
- **O, K, CLAIM, TRANSFER:** judgment; no source found.

The year-level excluded-driver share is 39.9% and the admitted share (N, O, K) is 18.3%.

## 4. What R1 does not change

R1 leaves the following as they were:

- the hypotheses and the margin δ = 0.03;
- the seed sets, apart from the five EC-07 seeds added below;
- the archetype propensity table and the tier rule;
- the six value entries and the canon structure;
- the gate's step order, and the examen and reconciliation;
- the DJ engine (`harness/engine.py`, six byte-identical copies) and the released corpora and rulebooks;
- the LLM prompt, apart from the pilot fixes and one clause aligning its breach sentence with R1 (proceeding under a token covering the entry, or departing for an admitted reason within bound, is not a violation).

Two identity values move with the driver mix:

- **E2 for pressure_sensitive:** 0.149 at T0/T1 and 0.297 at T2/T3 (was 0.144 / 0.288).
- **E2 and E4 denominators:** now about 40% excluded-driver, 42% NONE and 18% admitted (were 5/9, 1/9 and 3/9).

## 5. The calibration design rerun on the R1 instrument

The calibration design (seeds 11, 13, 17, 19, 23; 400 archetype runs; the bounds and the arm-D dry run) was rerun on the R1 instrument into `simulation/ec/results/calibration_r1/`. The purpose was to check that the mechanics still behave, before the registration. It is disclosed beside the first (v1) calibration. Calibration seeds are not confirmatory seeds, and no confirmatory seed was run. ⟦measured⟧:

| | honest | pressure_sensitive | observation_sensitive | misreporting |
|---|---|---|---|---|
| E7 blind spot, A / B / C / D | 0.679 / 0.647 / 0 / 0 | 0.771 / 0.657 / 0 / 0 | 0.714 / 0.655 / 0 / 0 | 0.679 / 0.647 / 0 / 0 |
| E2, A/B/C (D) | 0.003 (0.004) | 0.225 (0.227) | −0.002 (−0.001) | 0.003 (0.004) |
| E3 (all arms) | 0 | 0 | −0.149 | 0 |
| E4 (all arms) | 0.448 | 0.381 | 0.354 | 0.448 |
| gloss_bar blocks, fewest in any D run | 26 | 115 | 194 | 26 |
| E8 return, largest D run | −0.64 | −0.90 | −1.04 | −0.64 |
| throughput per working day, A / C / D | 22.1 / 21.5 / 21.4 | 21.9 / 20.0 / 19.9 | 21.5 / 18.4 / 18.3 | 22.1 / 21.5 / 21.4 |

Results against the hypotheses:

- Executed impermissible acts in arms C and D are 0 in all 200 runs.
- H6c's every-run gloss-bar condition, which the v1 calibration missed, is now met in every arm-D run.
- H5a's per-run ±0.03 disclosure tolerance still fails for the archetypes with misreporting and pressure. The cause is the same as in v1, and the hypothesis stands as written.
- E1 is identical across arms A, B and C. In D it is 0.004 to 0.005 higher for every archetype. Doctrine codifies classes in D, and a fresh exception token on a codified class is revoked at issue in D's registry. The agent's arm-invariant view still shows the token, so the same act is impermissible in D (`t1_revoked`). The registration states this.
- Arm B under rulebook revision R1 differs from the released 5.15.0 replay only in routes (33, 8 and 25 cases in SemiFab, FrontierLLM and DCVigil) and admissions (4, 1 and 7 records) on cases engaging the five reclassified provisions; no decision changes.

## 6. Sources

- AICPA, 2017 Trust Services Criteria (revised points of focus 2022), CC8.1 — via KirkpatrickPrice and Cloudaware summaries (secondary).
- soc2auditors.org, "SOC 2 change management controls" (auditor practice guide; secondary).
- GitLab Handbook: Change Management Policy; Security and Technology Policy Exceptions; Production change locks (sourced).
- GitHub Docs: About code owners; About protected branches (sourced).
- U.S. BLS, "Workers in private industry received an average of 8 paid holidays in 2017" (sourced).
- DORA, Accelerate State of DevOps 2021 (sourced); 2022–2023 cluster summaries via Octopus (secondary).
- Lientz & Swanson 1980, *Software Maintenance Management* (secondary).
- Ramač et al. 2021, "Prevalence, common causes, and effects of technical debt" (InsighTD), arXiv 2109.13771 (sourced).
- Kuutila et al. 2020, "Time pressure in software engineering: a systematic review", IST, arXiv 1901.05771 (sourced).
- Checkmarx 2024 survey, via Help Net Security (secondary).
- Edbert, Codabux & Verdecchia 2025, EASE, arXiv 2505.04027 (sourced).
- Edmundson et al. 2013, ESSoS, "An empirical study on the effectiveness of security code review" (sourced).
- Braz et al. 2022, ICSE, "Less is more: supporting developers in vulnerability detection during code review", arXiv 2202.04586 (sourced).
- Sadowski et al. 2018, ICSE-SEIP, "Modern code review: a case study at Google" (secondary).
- Graphite, "PRs merged after minimal review" (vendor data; secondary).
- Murphy-Hill et al. 2022, Google code review pushback (sourced, blog); Baysal et al. 2015, EMSE (sourced).
- Netwrix 2014, State of IT Changes (secondary).
