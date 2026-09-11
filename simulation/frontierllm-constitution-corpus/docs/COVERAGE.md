# Coverage report

Corpus 2.1.0. 6,000 cases, 139 provisions (31 absolute), opening store 210, final store 1143.

## Axioms of the architectural contract

| Axiom | Name | Cases exercising it |
| :---- | :---- | ----: |
| A1 | Role disjointness | 6,000 |
| A2 | Distinct output types | 6,000 |
| A3 | No direct mutation of the rulebook | 150 |
| A4 | Risk acceptance only at exhaustion | 525 |
| A5 | Write postcondition (full rationale trail) | 933 |
| A6 | Non-overridable short-circuit | 394 |
| A7 | Sunset, referral and renewal | 690 |
| A8 | Bindingness | 1,188 |
| A9 | Standing declaration and realised exercise | 144 |

## Requirements spine

| Req | Statement | Cases touching it |
| :---- | :---- | ----: |
| R1 | Exception authority named and role-keyed | 6,000 |
| R2 | Rationale recorded at decision time, in full | 933 |
| R3 | Comparable prior decisions retrievable | 4,150 |
| R4 | Retrieved decisions bind, with a contest path | 1,188 |
| R5 | Enforced lifecycle: expiry, ratification, visible renewal | 690 |
| R6 | Rule authorship, adjudication and risk acceptance separated | 6,000 |
| R7 | Deep-reasoning cost scales with contest, not with volume | 986 |

## Conformance checks

| Check | Cases exercising it |
| :---- | ----: |
| VC-01 | 1,380 |
| VC-02 | 1,710 |
| VC-03 | 144 |
| VC-04 | 150 |
| VC-05 | 484 |
| VC-06 | 525 |
| VC-07 | 933 |
| VC-08 | 394 |
| VC-09 | 525 |
| VC-10 | 102 |
| VC-11 | 1,188 |
| VC-12 | 48 |
| VC-13 | 222 |
| VC-14 | 156 |
| VC-15 | 933 |
| VC-16 | 480 |
| VC-17 | 144 |
| VC-18 | 180 |
| VC-19 | 198 |
| VC-20 | 198 |
| VC-21 | 180 |
| VC-22 | 312 |
| VC-23 | 312 |
| VC-24 | 108 |
| VC-25 | 96 |
| VC-26 | 144 |

## Provision families

| Family | Title | Provisions | Cases |
| :---- | :---- | ----: | ----: |
| MB | Model, checkpoint and prompt bill of materials | 9 | 419 |
| TD | Training-data provenance, licence and opt-out | 8 | 629 |
| PI | Personal data in training, prompts and logs | 7 | 387 |
| AG | Agent identity and agent-authored code | 8 | 405 |
| LS | LLM-specific security: injection, jailbreak, poisoning, extraction | 11 | 466 |
| EV | Probabilistic evaluation, semantic parity and contamination | 10 | 451 |
| SF | Frontier safety: capability thresholds, safety cases, weight security | 9 | 389 |
| IN | Inference infrastructure, latency budgets and determinism | 8 | 365 |
| FG | Financial guardrails for agentic workloads | 6 | 228 |
| BS | Brand safety, toxicity and persona compliance | 6 | 234 |
| IP | Copyright and intellectual-property contamination | 6 | 158 |
| SC | Classic software supply chain and build integrity | 8 | 421 |
| AS | Application security of the serving and tooling surface | 6 | 272 |
| GV | Governance of the judiciary itself | 11 | 550 |
| CS | Child safety: abuse-material detection, age assurance and minors' data | 4 | 110 |
| CB | Catastrophic-risk evaluations: bio/chem, cyber, autonomy and elicitation integrity | 4 | 152 |
| WX | Weight security, insider threat, export classification and sanctions screening | 4 | 110 |
| TR | Transparency, content provenance, documentation and incident reporting | 4 | 121 |
| UH | User harm: crisis safety, persuasion, high-stakes advice, companion use and abuse | 5 | 179 |
| PV | Privacy operations: erasure, retention commitments, tenant isolation, workers and lawful access | 5 | 221 |

## Risk-framework areas (veterinary risk and test strategy document)

| Area | Cases |
| :---- | ----: |
| 1.1 Dependency and provenance management; SLSA | 421 |
| 1.1 SBOM, MBOM and PBOM; SLSA compliance | 419 |
| 1.2 Human vs agent-authored code verification | 405 |
| 2. Security and vulnerability management (OWASP Top 10 for LLMs) | 466 |
| 2. Traditional AppSec augmented for LLM systems | 272 |
| 3.1 Probabilistic testing and model drift | 451 |
| 3.2 Resource and infrastructure checks | 365 |
| 4.1 Policy-as-code and automated compliance | 550 |
| 4.1 Regulatory transparency and provenance obligations | 121 |
| 4.2 Copyright and IP contamination | 158 |
| 4.2 GDPR/CCPA data sanitization | 387 |
| 4.2 GDPR/CCPA operations and multi-tenant boundaries | 221 |
| 4.2 Privacy, IP and sovereign boundaries | 629 |
| 5.1 Financial guardrails | 228 |
| 5.2 Reputational and brand safety guardrails | 234 |
| 5.2 User-harm and manipulation guardrails | 179 |
| 5.3 Child-safety floors and minors' data (CSAM, age assurance, COPPA) | 110 |
| 7. Shift-left AI regulation; dangerous-capability gates | 152 |
| 7. Shift-left AI regulation; hard blocks | 389 |
| 7. Weight security; 4.2 export and sanctions boundaries | 110 |

## Routes taken

| Route | Cases |
| :---- | ----: |
| decided on a fresh reading of the rulebook | 3,733 |
| bound by a controlling record | 1,188 |
| denied at once on an absolute provision, before any retrieval ran | 394 |
| not charged, and docketed on the declined route | 327 |
| decided fresh after the ordering deadlocked | 146 |
| disposed by direct citation of a consolidation representative | 131 |
| not charged, and docketed on the null route | 81 |

## Provision status

A deferred provision is enacted but not yet applicable; an advisory provision names suggested actions rather than obligations. Neither may be marked absolute, and VC-04 checks it.

| Status | Provisions | Cases engaging one |
| :---- | ----: | ----: |
| in_force | 133 | 6,001 |
| deferred | 3 | 117 |
| advisory | 3 | 149 |
| readiness | 0 | 0 |

## Provisions never exercised

None: every provision in the constitution carries at least one case.

