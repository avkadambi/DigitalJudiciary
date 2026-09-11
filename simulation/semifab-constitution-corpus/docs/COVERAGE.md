# Coverage report

Corpus 2.1.0. 6,000 cases, 126 provisions (28 absolute), opening store 200, final store 1154.

## Axioms of the architectural contract

| Axiom | Name | Cases exercising it |
| :---- | :---- | ----: |
| A1 | Role disjointness | 6,000 |
| A2 | Distinct output types | 6,000 |
| A3 | No direct mutation of the rulebook | 150 |
| A4 | Risk acceptance only at exhaustion | 515 |
| A5 | Write postcondition (full rationale trail) | 954 |
| A6 | Non-overridable short-circuit | 401 |
| A7 | Sunset, referral and renewal | 690 |
| A8 | Bindingness | 1,182 |
| A9 | Standing declaration and realised exercise | 144 |

## Requirements spine

| Req | Statement | Cases touching it |
| :---- | :---- | ----: |
| R1 | Exception authority named and role-keyed | 6,000 |
| R2 | Rationale recorded at decision time, in full | 954 |
| R3 | Comparable prior decisions retrievable | 4,091 |
| R4 | Retrieved decisions bind, with a contest path | 1,182 |
| R5 | Enforced lifecycle: expiry, ratification, visible renewal | 690 |
| R6 | Rule authorship, adjudication and risk acceptance separated | 6,000 |
| R7 | Deep-reasoning cost scales with contest, not with volume | 993 |

## Conformance checks

| Check | Cases exercising it |
| :---- | ----: |
| VC-01 | 1,380 |
| VC-02 | 1,710 |
| VC-03 | 144 |
| VC-04 | 150 |
| VC-05 | 487 |
| VC-06 | 515 |
| VC-07 | 954 |
| VC-08 | 401 |
| VC-09 | 515 |
| VC-10 | 102 |
| VC-11 | 1,182 |
| VC-12 | 48 |
| VC-13 | 222 |
| VC-14 | 156 |
| VC-15 | 954 |
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
| EX | Export control and trade compliance | 13 | 709 |
| DS | Data sovereignty, residency and government access | 7 | 376 |
| SG | SECS/GEM and equipment communication integrity | 10 | 653 |
| RT | Real-time latency and determinism | 7 | 502 |
| WI | Work-in-progress, metrology and record immutability | 7 | 432 |
| RP | Recipe protection and intellectual-property leakage | 7 | 300 |
| SS | Software supply chain, provenance and dependencies | 11 | 838 |
| AG | Governance of AI-agent-authored change | 8 | 389 |
| TQ | Memory and concurrency safety of telemetry pipelines | 7 | 265 |
| CR | Cryptographic standards for controlled data | 6 | 226 |
| AS | Input sanitisation and application security | 7 | 401 |
| NC | NIST and CHIPS programme compliance mapping | 6 | 149 |
| GV | Governance of the judiciary itself | 7 | 232 |
| IT | ITAR technical data and defence articles | 4 | 113 |
| SO | Sanctions, anti-boycott and investment screening | 3 | 88 |
| RS | Responsible sourcing and part integrity | 4 | 142 |
| EH | Environment, health and safety systems | 4 | 96 |
| QS | Quality system and customer change notification | 4 | 181 |
| OT | OT network segmentation and remote access | 4 | 174 |

## Risk-framework areas (veterinary risk and test strategy document)

| Area | Cases |
| :---- | ----: |
| 2. Software Supply Chain Security (SSCS) | 838 |
| 3. Agent Hallucination and Logic Drift; 6. Agent-Specific Defensive Testing | 389 |
| 3. Cryptographic Standards | 226 |
| 3. Input Sanitization and Fuzzing | 401 |
| 3. Memory and Concurrency Safety | 265 |
| 4. Life-Safety and Environmental Monitoring Integrity | 96 |
| 4. OT Network Security and Vendor Access | 174 |
| 4. Quality System and Customer Commitments | 181 |
| 4. Real-Time Latency Constraints | 502 |
| 4. Recipe Protection and IP Leakage | 300 |
| 4. SECS/GEM Protocol Integrity | 653 |
| 4. WIP Data Immutability | 432 |
| 5. CHIPS Act Security Requirements; NIST SP 800-53 and 800-161 | 149 |
| 5. Data Sovereignty and Localization | 376 |
| 5. Export Control Compliance (EAR/ITAR) | 822 |
| 5. Export Control Compliance (EAR/ITAR); Sanctions and Anti-Boycott | 88 |
| 5. Responsible Sourcing; 2. Hardware Supply Chain Integrity | 142 |
| 7. Policy-as-Code for Immutable Guardrails | 232 |

## Routes taken

| Route | Cases |
| :---- | ----: |
| decided on a fresh reading of the rulebook | 3,731 |
| bound by a controlling record | 1,182 |
| denied at once on an absolute provision, before any retrieval ran | 401 |
| not charged, and docketed on the declined route | 326 |
| decided fresh after the ordering deadlocked | 151 |
| disposed by direct citation of a consolidation representative | 127 |
| not charged, and docketed on the null route | 82 |

## Provisions never exercised

None: every provision in the constitution carries at least one case.

