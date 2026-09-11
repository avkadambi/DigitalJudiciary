# Coverage report

Corpus 2.1.0. 6,000 cases, 121 provisions (26 absolute), opening store 197, final store 1119.

## Axioms of the architectural contract

| Axiom | Name | Cases exercising it |
| :---- | :---- | ----: |
| A1 | Role disjointness | 6,000 |
| A2 | Distinct output types | 6,000 |
| A3 | No direct mutation of the rulebook | 150 |
| A4 | Risk acceptance only at exhaustion | 520 |
| A5 | Write postcondition (full rationale trail) | 922 |
| A6 | Non-overridable short-circuit | 398 |
| A7 | Sunset, referral and renewal | 690 |
| A8 | Bindingness | 1,189 |
| A9 | Standing declaration and realised exercise | 144 |

## Requirements spine

| Req | Statement | Cases touching it |
| :---- | :---- | ----: |
| R1 | Exception authority named and role-keyed | 6,000 |
| R2 | Rationale recorded at decision time, in full | 922 |
| R3 | Comparable prior decisions retrievable | 4,117 |
| R4 | Retrieved decisions bind, with a contest path | 1,189 |
| R5 | Enforced lifecycle: expiry, ratification, visible renewal | 690 |
| R6 | Rule authorship, adjudication and risk acceptance separated | 6,000 |
| R7 | Deep-reasoning cost scales with contest, not with volume | 953 |

## Conformance checks

| Check | Cases exercising it |
| :---- | ----: |
| VC-01 | 1,380 |
| VC-02 | 1,710 |
| VC-03 | 144 |
| VC-04 | 150 |
| VC-05 | 474 |
| VC-06 | 520 |
| VC-07 | 922 |
| VC-08 | 398 |
| VC-09 | 520 |
| VC-10 | 102 |
| VC-11 | 1,189 |
| VC-12 | 48 |
| VC-13 | 222 |
| VC-14 | 156 |
| VC-15 | 922 |
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
| CS | Controlled substances, EPCS and PDMP reporting | 12 | 455 |
| VC | VCPR, extralabel drug use and residue avoidance | 8 | 492 |
| PO | Point-of-care diagnostics, HL7 and DICOM integration | 10 | 604 |
| PD | Owner PII, payment data and consent | 9 | 611 |
| RB | Role-based access control and multi-practice isolation | 8 | 590 |
| SC | Software supply chain, provenance and dependencies | 9 | 696 |
| AI | Governance of AI-agent-authored changes | 8 | 375 |
| AS | Application security and defensive coding | 9 | 562 |
| HA | High availability and concurrency for emergency operations | 6 | 239 |
| RR | Records, audit trail and immutability | 7 | 441 |
| AW | Animal welfare, practice acts and scope of practice | 5 | 150 |
| GV | Governance of the judiciary itself | 7 | 223 |
| BN | Breach notification and client-data incidents | 3 | 104 |
| DR | DEA reporting, ordering and diversion controls | 4 | 106 |
| CC | Client communications, consent, subscriptions and records rights | 6 | 235 |
| PS | Patient safety, dosing and clinical decision support | 4 | 138 |
| PH | Public health, welfare and mandated reporting | 4 | 152 |
| AX | Accessibility and equal access to client-facing surfaces | 2 | 112 |

## Risk-framework areas (veterinary risk and test strategy document)

| Area | Cases |
| :---- | ----: |
| 2.1 Point-of-Care (POC) Diagnostics and IoT Integrations | 604 |
| 2.2 Controlled Substance Management and e-Prescribing (EPCS) | 455 |
| 2.2 Controlled Substance Management; DEA registrant duties | 106 |
| 2.2 Controlled Substance Management; clinical practice floor | 492 |
| 2.2 Inventory Auditing; 3. Pipeline Integrity | 441 |
| 2.3 Patient Data Privacy (PII and PCI) | 611 |
| 2.3 Patient Data Privacy (PII and PCI); incident response floor | 104 |
| 2.3 Patient Data Privacy; consumer-protection floor | 235 |
| 2.3 RBAC; 5.1 Insecure Direct Object References | 590 |
| 3. Software Supply Chain and Pipeline Integrity | 696 |
| 4. Securing AI-Agent Generated Code | 375 |
| 5.1 OWASP and Defensive Coding | 562 |
| 5.2 High Availability and Concurrency for ER Operations | 239 |
| Client-facing surfaces; civil-rights and consumer floor | 112 |
| Clinical safety floor; 2.1 POC integrations; 4. AI features | 138 |
| Constitutional meta-provisions (A9, GDPR Art. 22, EU AI Act Art. 5) | 223 |
| Domain floor; USDA APHIS and state practice acts | 150 |
| Domain floor; USDA APHIS, state animal-health and public-health law | 152 |

## Routes taken

| Route | Cases |
| :---- | ----: |
| decided on a fresh reading of the rulebook | 3,729 |
| bound by a controlling record | 1,189 |
| denied at once on an absolute provision, before any retrieval ran | 398 |
| not charged, and docketed on the declined route | 345 |
| decided fresh after the ordering deadlocked | 145 |
| disposed by direct citation of a consolidation representative | 131 |
| not charged, and docketed on the null route | 63 |

## Provisions never exercised

None: every provision in the constitution carries at least one case.

