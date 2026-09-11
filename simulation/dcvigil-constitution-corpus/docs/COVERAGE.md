# Coverage report

Corpus 2.1.0. 6,000 cases, 134 provisions (26 absolute), opening store 210, final store 1160.

## Axioms of the architectural contract

| Axiom | Name | Cases exercising it |
| :---- | :---- | ----: |
| A1 | Role disjointness | 6,000 |
| A2 | Distinct output types | 6,000 |
| A3 | No direct mutation of the rulebook | 150 |
| A4 | Risk acceptance only at exhaustion | 512 |
| A5 | Write postcondition (full rationale trail) | 950 |
| A6 | Non-overridable short-circuit | 400 |
| A7 | Sunset, referral and renewal | 690 |
| A8 | Bindingness | 1,189 |
| A9 | Standing declaration and realised exercise | 144 |

## Requirements spine

| Req | Statement | Cases touching it |
| :---- | :---- | ----: |
| R1 | Exception authority named and role-keyed | 6,000 |
| R2 | Rationale recorded at decision time, in full | 950 |
| R3 | Comparable prior decisions retrievable | 4,154 |
| R4 | Retrieved decisions bind, with a contest path | 1,189 |
| R5 | Enforced lifecycle: expiry, ratification, visible renewal | 690 |
| R6 | Rule authorship, adjudication and risk acceptance separated | 6,000 |
| R7 | Deep-reasoning cost scales with contest, not with volume | 1,005 |

## Conformance checks

| Check | Cases exercising it |
| :---- | ----: |
| VC-01 | 1,380 |
| VC-02 | 1,710 |
| VC-03 | 144 |
| VC-04 | 150 |
| VC-05 | 482 |
| VC-06 | 512 |
| VC-07 | 950 |
| VC-08 | 400 |
| VC-09 | 512 |
| VC-10 | 102 |
| VC-11 | 1,189 |
| VC-12 | 48 |
| VC-13 | 222 |
| VC-14 | 156 |
| VC-15 | 950 |
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
| TL | Telemetry ingestion and collector integrity | 7 | 304 |
| AC | Automated remediation, blast radius and physical actuation | 11 | 447 |
| TI | Tenant isolation and multi-tenancy | 3 | 99 |
| AP | Privileged agent security | 7 | 254 |
| KS | Kernel and eBPF safety | 5 | 218 |
| TG | Telemetry integrity and agent identity | 6 | 245 |
| QA | Change quality gates | 7 | 478 |
| RS | Agent resource budgets and non-intrusive execution | 5 | 146 |
| AI | AIOps model governance and alert quality | 10 | 547 |
| SC | Supply chain, dependencies and build provenance | 7 | 429 |
| AG | AI-agent-authored change governance | 4 | 236 |
| DR | Data residency, privacy and redaction | 15 | 946 |
| EV | Audit evidence, retention and notification | 7 | 371 |
| OP | Operational windows and escalation control | 7 | 388 |
| GV | Governance of the judiciary itself | 7 | 250 |
| LA | Lawful access, legal hold and government requests | 4 | 119 |
| LS | Life-safety systems and physical resilience | 3 | 125 |
| EN | Energy, water and sustainability reporting integrity | 3 | 96 |
| CT | Customer trust: tenant keys, exit, sub-processors and audit rights | 4 | 105 |
| OT | OT protocols, zoning and device firmware | 3 | 117 |
| SV | Product security assurance and vulnerability handling | 5 | 192 |
| AX | Accessibility of the operator console and customer portal | 2 | 117 |
| TC | Trade controls: restricted-party screening and export classification | 2 | 32 |

## Risk-framework areas (veterinary risk and test strategy document)

| Area | Cases |
| :---- | ----: |
| 1.1 Dependency and provenance management; SLSA | 429 |
| 1.1 Product security; customer-deployed agent under a disclosure duty | 192 |
| 1.2 Human versus agent-authored code verification | 236 |
| 2. Data exfiltration via log parsers; 3.2 high-volume telemetry | 304 |
| 2. Facility network exposure; OT segmentation and device integrity | 117 |
| 2. Privilege escalation via agents | 254 |
| 2. Telemetry tampering and forgery | 245 |
| 3.1 Agent overhead and non-intrusive execution | 146 |
| 3.1 Kernel panic prevention | 218 |
| 3.2 AIOps topology accuracy; 4.1 predictive-model promotion | 547 |
| 4. Customer contractual floor; litigation-hold and lawful-access duties | 119 |
| 4. Multi-tenant contractual floor | 99 |
| 4. Multi-tenant contractual floor; processor duties owed to the controller | 105 |
| 4. Regulatory floor on a product distributed to customer estates worldwide | 32 |
| 4. Regulatory reporting; facility efficiency and ESG disclosure | 96 |
| 4. SOC 2 / ISO 27001 evidence; GDPR and NIS2 clocks | 371 |
| 4.1 Policy-as-code and contestation rules | 250 |
| 4.2 Privacy, data sovereignty and IP | 946 |
| 5. Enterprise risk management; on-call practice | 388 |
| 5.1 Automated remediation guardrails; physical-safety floor | 447 |
| 6. Deterministic unit and resource testing | 478 |
| Customer-facing and operator surfaces; civil-rights floor | 117 |
| Life-safety floor; 5.1 blast radius at the physical boundary | 125 |

## Routes taken

| Route | Cases |
| :---- | ----: |
| decided on a fresh reading of the rulebook | 3,728 |
| bound by a controlling record | 1,189 |
| denied at once on an absolute provision, before any retrieval ran | 400 |
| not charged, and docketed on the declined route | 321 |
| decided fresh after the ordering deadlocked | 147 |
| disposed by direct citation of a consolidation representative | 128 |
| not charged, and docketed on the null route | 87 |

## Provision status

A deferred provision is enacted but not yet applicable; an advisory provision names suggested actions rather than obligations. Neither may be marked absolute, and VC-04 checks it.

| Status | Provisions | Cases engaging one |
| :---- | ----: | ----: |
| in_force | 126 | 5,856 |
| deferred | 5 | 298 |
| advisory | 2 | 81 |
| readiness | 1 | 26 |

## Provision origin

The twenty-nine provisions of the released DCVigil pack appear here with their text and absolute flags unchanged, so the 144 shipped cases remain valid against this constitution.

| Origin | Provisions | Cases engaging one |
| :---- | ----: | ----: |
| shipped | 29 | 1,721 |
| extension | 105 | 4,540 |

## Provisions never exercised

The following provisions carry no case. They are reachable and are left in the constitution deliberately, so that an adopter can see what the corpus does not yet cover:

- DV-402 — Cross-tenant correlation isolation is verified when topology inference changes

