# Inheritance — the enterprise constitution against the five division constitutions

Enterprise rulebook `numerals-rb-000001`, 33 provisions, 6 absolute, 4 proposed floors held ordinary. Rule: minimum harmonisation — a division may tighten, never loosen; an enterprise absolute is a floor in every division. Cells name the division provisions implementing each enterprise provision (`*` = absolute in the division). **tightened** = the division states a floor where the enterprise states an ordinary provision. **gap** = the enterprise provision applies and the division has no implementing provision; a draft amendment is filed. `n/a` = the enterprise provision is stated not to apply to that division.

| enterprise | abs | vetpoc | semifab | frontierllm | dcvigil | meridian |
|---|---|---|---|---|---|---|
| NM-001 No configuration, feature flag or release removes the affected party's… | **yes** | VP-GV-001* | SF-GV-001* | FL-GV-001* | DV-411* | MF-110* |
| NM-002 No Numerals system performs a practice prohibited by EU AI Act Article… | **yes** | VP-GV-002* | SF-GV-002* | FL-GV-002* | DV-330*, DV-331*, DV-345* | MF-107* |
| NM-003 Decision and audit records are append-only in every division; a correc… | **yes** | VP-RR-001* | SF-EX-003*, SF-WI-002* | FL-GV-003* | DV-412* | MF-506*, MF-512* |
| NM-004 Constitutional parameters — thresholds, windows, class sizes — change … | no | VP-GV-004 | SF-GV-004 | FL-GV-006 | DV-413 | MF-593 |
| NM-005 Every division constitution declares whether any party holds contest s… | no | VP-GV-003 | SF-GV-003 | FL-GV-005 | DV-414 | MF-594 |
| NM-006 Reporter output never reaches the adjudication input path and the audi… | no | VP-GV-005, VP-GV-006 | SF-GV-005, SF-GV-006 | FL-GV-007 | DV-415 | MF-595 |
| NM-007 Every arrival that is not charged leaves exactly one docket entry, rat… | no | VP-GV-007 | SF-GV-007 | FL-GV-008 | DV-416 | MF-596 |
| NM-101 No AI agent modifies authentication or authorisation middleware, tenan… | proposed | VP-AI-001* (tightened) | SF-AG-002* (tightened) | FL-AG-002* (tightened) | DV-316 | MF-571 |
| NM-102 An agent-authored change to security policy, guardrails, CI/CD configu… | proposed | VP-AI-008 | SF-AG-008 | FL-AG-001*, FL-AG-002* (tightened) | DV-406 | MF-571 |
| NM-103 An autonomous agent's mandate is declared before execution, is narrowe… | **yes** | n/a | n/a | FL-FG-001* | DV-341* | MF-111*, MF-511* |
| NM-104 Agent-authored code executes only inside a sandboxed runner whose egre… | no | VP-AI-003, VP-AI-004 | SF-AG-004, SF-AG-005 | FL-AG-005, FL-AG-006 | **gap** | **gap** |
| NM-105 Every package an agent imports is verified to exist in an approved reg… | no | VP-AI-006, VP-AI-007 | SF-AG-003, SF-AG-007 | FL-AG-004, FL-AG-008 | DV-405 | MF-536 |
| NM-106 An agent never disables or weakens a failing compliance test, and ever… | no | VP-AI-008 | SF-AG-008 | FL-AG-003* (tightened) | DV-305 | MF-307 |
| NM-201 All new database access uses parameterised queries; no query is built … | no | VP-AS-001 | SF-AS-001 | FL-AS-001 | **gap** | **gap** |
| NM-202 User-controlled text is output-encoded before render and a Content Sec… | no | VP-AS-002, VP-AS-003 | SF-AS-003 | **gap** | **gap** | **gap** |
| NM-203 Deserialisation is restricted to known types and upload handlers const… | no | VP-AS-004, VP-AS-006 | SF-AS-005 | FL-AS-002 | **gap** | **gap** |
| NM-204 Outbound fetches from webhooks and integrations are restricted to an a… | no | VP-AS-005, VP-AS-007 | SF-AS-007 | FL-AS-004, FL-AS-005 | **gap** | **gap** |
| NM-205 Cryptographic primitives come from an approved library; hand-rolled ci… | no | VP-AS-008 | SF-CR-001*, SF-CR-002 (tightened) | **gap** | DV-337, DV-343* (tightened) | MF-530, MF-531 |
| NM-301 No credential, key or token appears in source, configuration or CI log… | proposed | VP-SC-008 | SF-SS-011 | FL-SC-008 | DV-301, DV-310 | MF-206, MF-501* (tightened) |
| NM-302 Commits merged to a protected branch carry a verified signature bound … | no | VP-SC-001 | SF-SS-003 | FL-AG-003* (tightened) | DV-404 | MF-535 |
| NM-303 No artefact deploys to production without provenance verified against … | no | VP-SC-002, VP-SC-003 | SF-SS-001*, SF-SS-002 (tightened) | FL-SC-001*, FL-SC-002, FL-SC-003 (tightened) | DV-403, DV-404 | MF-535 |
| NM-304 Every release publishes a software bill of materials bound to the arte… | no | VP-SC-007 | SF-SS-007 | FL-SC-006 | DV-434 | MF-534 |
| NM-305 No dependency carrying a vulnerability above the declared CVSS thresho… | no | VP-SC-005, VP-SC-006 | SF-SS-009, SF-SS-010 | FL-SC-005, FL-IP-001* (tightened) | DV-308, DV-309 | MF-538, MF-539 |
| NM-306 Dependency resolution prefers the private registry, manifest and lockf… | no | VP-SC-004, VP-SC-009 | SF-SS-005, SF-SS-006 | FL-SC-004 | DV-343* (tightened) | MF-531, MF-536, MF-537 |
| NM-401 Change control is never bypassed, disabled or self-approved in any div… | **yes** | **gap** | **gap** | **gap** | **gap** | MF-208, MF-502* |
| NM-402 A tested rollback or reversible migration exists for every production … | no | VP-HA-004 | **gap** | **gap** | DV-307, DV-318, DV-395 | MF-208, MF-541 |
| NM-403 No production deploy during a designated change-freeze window except u… | no | VP-HA-003 | **gap** | **gap** | DV-311 | MF-212, MF-542 |
| NM-404 Deploys are blocked on a latency or availability regression beyond the… | no | VP-HA-005, VP-HA-006 | SF-RT-002 | FL-IN-003 | DV-317 | MF-209 |
| NM-501 Every statutory notification or filing clock is a legislated constant … | proposed | VP-BN-001*, VP-DR-001* (tightened) | SF-SO-002* (tightened) | FL-TR-004* (tightened) | DV-336, DV-435 | MF-503*, MF-504* (tightened) |
| NM-502 Every customer-facing surface carries an accessibility regression gate… | no | VP-AX-001 | n/a | **gap** | DV-439 | MF-622 |
| NM-503 Personal data is collected for a stated purpose and retained on schedu… | no | VP-PD-005, VP-PD-008, VP-CC-005 | SF-DS-003 | FL-PI-004, FL-PV-001 | DV-315, DV-428* (tightened) | MF-210, MF-558, MF-621 |
| NM-504 Worker and personnel monitoring data — badge, access and productivity … | no | n/a | n/a | FL-PV-004 | DV-338*, DV-345* (tightened) | n/a |
| NM-505 Withdrawing consent is no harder than giving it, in any division and o… | **yes** | VP-PD-002* | n/a | n/a | DV-332* | **gap** |

## Draft amendments filed by the enterprise (26)

None is applied. Under A3 the enterprise proposes and each division's lawmakers dispose.

- **NPA-01** (NM-101) → dcvigil: DV-316; meridian: MF-571. The enterprise states NM-101 as a floor and the division provision(s) named state the same duty as an ordinary provision that a division risk owner may accept. Under minimum harmonisation a division may not be looser than the enterprise.
- **NPA-02** (NM-102) → vetpoc: VP-AI-008; semifab: SF-AG-008; dcvigil: DV-406; meridian: MF-571. The enterprise states NM-102 as a floor and the division provision(s) named state the same duty as an ordinary provision that a division risk owner may accept. Under minimum harmonisation a division may not be looser than the enterprise.
- **NPA-03** (NM-104) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-104 (Agent-authored code executes only inside a sandboxed runner whose egress is rest...).
- **NPA-04** (NM-104) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-104 (Agent-authored code executes only inside a sandboxed runner whose egress is rest...).
- **NPA-05** (NM-201) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-201 (All new database access uses parameterised queries; no query is built by string ...).
- **NPA-06** (NM-201) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-201 (All new database access uses parameterised queries; no query is built by string ...).
- **NPA-07** (NM-202) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-202 (User-controlled text is output-encoded before render and a Content Security Poli...).
- **NPA-08** (NM-202) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-202 (User-controlled text is output-encoded before render and a Content Security Poli...).
- **NPA-09** (NM-202) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-202 (User-controlled text is output-encoded before render and a Content Security Poli...).
- **NPA-10** (NM-203) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-203 (Deserialisation is restricted to known types and upload handlers constrain type,...).
- **NPA-11** (NM-203) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-203 (Deserialisation is restricted to known types and upload handlers constrain type,...).
- **NPA-12** (NM-204) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-204 (Outbound fetches from webhooks and integrations are restricted to an allow-list,...).
- **NPA-13** (NM-204) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-204 (Outbound fetches from webhooks and integrations are restricted to an allow-list,...).
- **NPA-14** (NM-205) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-205 (Cryptographic primitives come from an approved library; hand-rolled ciphers and ...).
- **NPA-15** (NM-301) → vetpoc: VP-SC-008; semifab: SF-SS-011; frontierllm: FL-SC-008; dcvigil: DV-301, DV-310. The enterprise states NM-301 as a floor and the division provision(s) named state the same duty as an ordinary provision that a division risk owner may accept. Under minimum harmonisation a division may not be looser than the enterprise.
- **NPA-16** (NM-401) → vetpoc: (no provision). vetpoc has no provision implementing enterprise provision NM-401 (Change control is never bypassed, disabled or self-approved in any division, and...).
- **NPA-17** (NM-401) → semifab: (no provision). semifab has no provision implementing enterprise provision NM-401 (Change control is never bypassed, disabled or self-approved in any division, and...).
- **NPA-18** (NM-401) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-401 (Change control is never bypassed, disabled or self-approved in any division, and...).
- **NPA-19** (NM-401) → dcvigil: (no provision). dcvigil has no provision implementing enterprise provision NM-401 (Change control is never bypassed, disabled or self-approved in any division, and...).
- **NPA-20** (NM-402) → semifab: (no provision). semifab has no provision implementing enterprise provision NM-402 (A tested rollback or reversible migration exists for every production change on ...).
- **NPA-21** (NM-402) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-402 (A tested rollback or reversible migration exists for every production change on ...).
- **NPA-22** (NM-403) → semifab: (no provision). semifab has no provision implementing enterprise provision NM-403 (No production deploy during a designated change-freeze window except under the e...).
- **NPA-23** (NM-403) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-403 (No production deploy during a designated change-freeze window except under the e...).
- **NPA-24** (NM-501) → dcvigil: DV-336, DV-435. The enterprise states NM-501 as a floor and the division provision(s) named state the same duty as an ordinary provision that a division risk owner may accept. Under minimum harmonisation a division may not be looser than the enterprise.
- **NPA-25** (NM-502) → frontierllm: (no provision). frontierllm has no provision implementing enterprise provision NM-502 (Every customer-facing surface carries an accessibility regression gate at WCAG 2...).
- **NPA-26** (NM-505) → meridian: (no provision). meridian has no provision implementing enterprise provision NM-505 (Withdrawing consent is no harder than giving it, in any division and on any chan...).
