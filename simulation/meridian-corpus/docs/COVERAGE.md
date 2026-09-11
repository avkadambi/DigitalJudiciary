# Coverage report

Corpus 2.1.0. 6,000 cases, 142 provisions (33 absolute), opening store 211, final store 1136.

## Axioms of the architectural contract

| Axiom | Name | Cases exercising it |
| :---- | :---- | ----: |
| A1 | Role disjointness | 6,000 |
| A2 | Distinct output types | 6,000 |
| A3 | No direct mutation of the rulebook | 150 |
| A4 | Risk acceptance only at exhaustion | 509 |
| A5 | Write postcondition (full rationale trail) | 925 |
| A6 | Non-overridable short-circuit | 397 |
| A7 | Sunset, referral and renewal | 690 |
| A8 | Bindingness | 1,201 |
| A9 | Standing declaration and realised exercise | 144 |

## Requirements spine

| Req | Statement | Cases touching it |
| :---- | :---- | ----: |
| R1 | Exception authority named and role-keyed | 6,000 |
| R2 | Rationale recorded at decision time, in full | 925 |
| R3 | Comparable prior decisions retrievable | 4,031 |
| R4 | Retrieved decisions bind, with a contest path | 1,201 |
| R5 | Enforced lifecycle: expiry, ratification, visible renewal | 690 |
| R6 | Rule authorship, adjudication and risk acceptance separated | 6,000 |
| R7 | Deep-reasoning cost scales with contest, not with volume | 990 |

## Conformance checks

| Check | Cases exercising it |
| :---- | ----: |
| VC-01 | 1,380 |
| VC-02 | 1,710 |
| VC-03 | 144 |
| VC-04 | 150 |
| VC-05 | 509 |
| VC-06 | 509 |
| VC-07 | 925 |
| VC-08 | 397 |
| VC-09 | 509 |
| VC-10 | 102 |
| VC-11 | 1,201 |
| VC-12 | 48 |
| VC-13 | 222 |
| VC-14 | 156 |
| VC-15 | 925 |
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
| FC | Financial crime: sanctions, BSA and customer identification | 11 | 329 |
| PD | Payment card data and the cardholder-data environment | 7 | 229 |
| SS | Secrets, keys and cryptographic posture | 8 | 346 |
| SP | Software supply chain, dependencies and build provenance | 7 | 422 |
| CQ | Change control and quality gates | 7 | 512 |
| LG | Ledger integrity, atomicity and idempotency | 6 | 254 |
| PR | Numeric precision and rounding | 5 | 149 |
| RE | Operational resilience and ICT third-party risk | 9 | 437 |
| DP | Data privacy, residency and retention | 8 | 752 |
| FL | Credit decisioning, fair lending and model risk | 13 | 535 |
| AI | AI governance and the EU AI Act | 8 | 417 |
| AG | Agent-authored change and autonomous action governance | 5 | 194 |
| CP | Consumer protection, disclosure and complaint handling | 9 | 420 |
| EV | Evidence, audit trail and financial-reporting controls | 6 | 201 |
| GV | Judicial architecture and governance of the rulebook itself | 7 | 277 |
| PS | Payment security, strong authentication and open banking | 4 | 107 |
| FR | Fraud, identity theft, account takeover and applicant identity | 5 | 166 |
| CN | Consumer notices, electronic consent and communications | 4 | 165 |
| FP | Deposit fees, funds availability and account handling | 4 | 110 |
| MP | Military, servicemember and vulnerable-customer protections | 3 | 58 |
| DA | Data-subject rights, opt-out signals and accessibility | 3 | 102 |
| VA | Virtual assets and the breadth of the financial-crime programme | 3 | 70 |

## Risk-framework areas (FinTech risk architecture document)

| Area | Cases |
| :---- | ----: |
| 2.1 Data privacy and sovereignty | 752 |
| 2.1 GDPR access and portability; CPRA opt-out signals; accessibility floor | 102 |
| 2.2 AML/KYC/BSA; strict-liability sanctions exposure | 329 |
| 2.2 DORA; 5.1 timeouts and circuit breakers | 437 |
| 2.2 E-SIGN, TCPA, Reg P and Reg F; UDAAP communications | 165 |
| 2.2 ECOA/Reg B, FCRA; SR 11-7 model risk | 535 |
| 2.2 EU AI Act; 4. AI governance | 417 |
| 2.2 MLA and SCRA; elder financial exploitation | 58 |
| 2.2 PCI-DSS; 3.1 cryptography and data protection | 229 |
| 2.2 PSD2 SCA and the Instant Payments Regulation; APP-fraud reimbursement | 107 |
| 2.2 Red Flags / Reg S-ID; FFIEC authentication; FCRA permissible purpose | 166 |
| 2.2 Reg DD, Reg E overdraft, Reg CC; state unclaimed-property law | 110 |
| 2.2 SOC 2 CC8.1; PCI DSS Req. 6.5.1 | 512 |
| 2.2 SOX §404; 6.2 audit log integrity | 201 |
| 2.2 Travel Rule, currency transaction reporting, 314(a), PEP and EDD | 70 |
| 2.2 UDAAP, TILA, Reg E; complaint management | 420 |
| 3.1 Key management; GLBA Safeguards | 346 |
| 4. Software supply chain security; SLSA | 422 |
| 4.3 Agentic code provenance; 1.2 agent verification | 194 |
| 5.2 Precision and mathematical integrity | 149 |
| 6.1 Transaction atomicity; 6.2 ledger immutability | 254 |
| Chapter 5 axioms and definitions | 277 |

## Routes taken

| Route | Cases |
| :---- | ----: |
| decided on a fresh reading of the rulebook | 3,726 |
| bound by a controlling record | 1,201 |
| denied at once on an absolute provision, before any retrieval ran | 397 |
| not charged, and docketed on the declined route | 312 |
| decided fresh after the ordering deadlocked | 135 |
| disposed by direct citation of a consolidation representative | 133 |
| not charged, and docketed on the null route | 96 |

## Provision status

A deferred provision is enacted but not yet applicable; a readiness provision states an architecture the firm must be able to meet when a suspended rule resumes; an advisory provision names suggested actions rather than obligations. None of the three may be marked absolute, and VC-04 checks it.

| Status | Provisions | Cases engaging one |
| :---- | ----: | ----: |
| in_force | 140 | 6,149 |
| deferred | 1 | 48 |
| advisory | 0 | 0 |
| readiness | 1 | 55 |

## Provision origin

The thirty-seven provisions of the released Meridian Financial pack appear here with their text and absolute flags unchanged, so the 68 shipped cases remain valid against this constitution.

| Origin | Provisions | Cases engaging one |
| :---- | ----: | ----: |
| shipped | 37 | 1,865 |
| extension | 105 | 4,387 |

## Provisions never exercised

None: every provision in the constitution carries at least one case.

