# Scenario coverage — frontierllm

Corpus 2.1.0, 6,000 cases, 139 provisions (31 absolute). Every count ⟦measured⟧ on the corpus as built; see harness/coverage.py and VC-50. Bold = demanded by the catalogue.

| scenario | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| S-01 Sanctions, denied-party and restricted-destination screening is weakened or bypassed | 1 (1) | **2** | 0 | **13** | **1** | 0 | 0 | 0 | 150 |
| S-02 Personal or controlled data leaves its lawful region, boundary or tenant | 11 (2) | **68** | **39** | **21** | 19 | **46** | 46 | 0 | 150 |
| S-03 A regulated record is destroyed, overwritten, back-dated or its retention shortened | 16 (2) | **99** | **53** | **19** | 27 | 66 | 39 | 0 | 150 |
| S-04 A statutory notification or filing clock is disabled, extended or made configurable | 3 (2) | **12** | **4** | **25** | **4** | 2 | 7 | 0 | 150 |
| S-05 A prohibited AI practice or manipulative technique is implemented | 10 (2) | **61** | 29 | **18** | 18 | 42 | 12 | 0 | 150 |
| S-06 A protected characteristic or a proxy for one enters an automated decision | 6 (1) | **40** | **19** | **6** | 11 | **26** | 5 | 0 | 150 |
| S-07 Child safety: CSAM handling, age assurance, minors' data and interactions | 5 (2) | **24** | **20** | **24** | 9 | 12 | 14 | 0 | 150 |
| S-09 Export-controlled technology, defence articles or model weights reach an unauthorised person or destination | 10 (4) | **47** | **20** | **51** | 17 | 30 | 35 | 0 | 150 |
| S-11 The human-review or contest path for an automated decision is removed | 8 (1) | **49** | **24** | **13** | 14 | 34 | 7 | 0 | 150 |
| S-12 An autonomous agent's mandate, loop limit, cost breaker or human stop is widened or removed | 14 (3) | **82** | **39** | **34** | **28** | 64 | 13 | 0 | 150 |
| S-13 Third-party code, build provenance, SBOM or vendor review is weakened | 23 (6) | **120** | **66** | 68 | 41 | 94 | **17** | 0 | 150 |
| S-14 Secrets, keys or cryptographic posture are degraded | 34 (6) | **150** | **78** | 66 | 49 | 130 | **22** | 0 | 150 |
| S-15 Change control, segregation of duties or a change freeze is bypassed | 8 (3) | **45** | **20** | 33 | 15 | 26 | **5** | 0 | 150 |
| S-18 Data-subject rights operations fail: access, portability, erasure, unlearning, offboarding return | 8 (1) | **54** | **30** | 9 | 13 | 40 | **32** | 0 | 150 |
| S-19 Lawful-access, legal hold and government-request handling is mis-implemented | 1 (0) | **7** | **3** | 0 | 3 | 6 | 7 | 0 | 150 |
| S-20 Incident communication, status reporting or root-cause delivery to customers is degraded | 9 (2) | **56** | **24** | 31 | 18 | 32 | 42 | 0 | 150 |
| S-22 Employee or worker monitoring and personnel data are mishandled | 2 (0) | **12** | **16** | 0 | 3 | 8 | 10 | 0 | 150 |
| S-23 Model governance fails: validation, monitoring, sandbagging, red-team coverage, documentation | 24 (5) | **137** | **80** | **63** | 47 | 88 | **101** | 240 | 150 |
| S-27 Insider threat, exfiltration detection or personnel vetting for crown-jewel assets is weakened | 10 (4) | **49** | **23** | **49** | 17 | 32 | 35 | 0 | 150 |
| S-30 An AI assistant or generated content harms users: harmful advice, self-harm, persuasion, unmarked synthetic media | 13 (3) | **83** | **47** | **27** | **25** | 54 | 34 | 0 | 150 |
| S-33 Telemetry, alerting or evidence integrity is degraded | 14 (4) | **80** | **44** | **49** | 31 | 40 | 64 | 0 | 150 |
| S-34 Governance of the rulebook itself is circumvented | 7 (0) | **47** | **24** | 0 | 13 | 34 | 7 | 0 | **150** |
| S-36 Operational resilience, latency or availability floors on critical paths regress | 8 (0) | **30** | **16** | 0 | 8 | 28 | **18** | 0 | 150 |
| S-38 Training-data provenance, licensing, copyright and opt-out are breached | 16 (3) | **59** | **30** | **36** | 18 | 32 | 40 | 0 | 150 |
| S-39 Recipe, process and design IP leaks through logs, caches, telemetry or model context | 18 (3) | **71** | **28** | **33** | 21 | 60 | 9 | 0 | 150 |

Constitution notes for the lawmakers: S-01: only absolute provisions mapped; no ordinary limb to deny, accept or pair; S-19: floor expected, no absolute provision mapped.
