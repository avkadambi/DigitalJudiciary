# Scenario coverage — dcvigil

Corpus 2.1.0, 6,000 cases, 134 provisions (26 absolute). Every count ⟦measured⟧ on the corpus as built; see harness/coverage.py and VC-50. Bold = demanded by the catalogue.

| scenario | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| S-01 Sanctions, denied-party and restricted-destination screening is weakened or bypassed | 2 (2) | **4** | 0 | **26** | **2** | 0 | 0 | 0 | 150 |
| S-02 Personal or controlled data leaves its lawful region, boundary or tenant | 14 (6) | **61** | **26** | **79** | 19 | **32** | 22 | 240 | 150 |
| S-03 A regulated record is destroyed, overwritten, back-dated or its retention shortened | 7 (3) | **18** | **8** | **51** | 6 | 10 | 2 | 0 | 150 |
| S-04 A statutory notification or filing clock is disabled, extended or made configurable | 9 (2) | **41** | **20** | **30** | **11** | 22 | 13 | 0 | 150 |
| S-05 A prohibited AI practice or manipulative technique is implemented | 11 (4) | **49** | 19 | **46** | 17 | 36 | 28 | 240 | 150 |
| S-06 A protected characteristic or a proxy for one enters an automated decision | 9 (4) | **35** | **15** | **42** | 12 | **24** | 18 | 240 | 150 |
| S-08 Life-safety, physical actuation or clinical-safety control is suppressed or bypassed | 18 (5) | **104** | **64** | **76** | **33** | 68 | 46 | 0 | 150 |
| S-09 Export-controlled technology, defence articles or model weights reach an unauthorised person or destination | 1 (1) | **2** | 0 | **11** | 1 | 0 | 0 | 0 | 150 |
| S-10 A consumer's statutory right, cap or window is made configurable or removed | 4 (3) | **13** | **6** | **39** | 5 | **10** | 6 | 0 | 150 |
| S-11 The human-review or contest path for an automated decision is removed | 6 (2) | **37** | **18** | **24** | 13 | 16 | 4 | 0 | 150 |
| S-12 An autonomous agent's mandate, loop limit, cost breaker or human stop is widened or removed | 13 (2) | **71** | **46** | **24** | **25** | 50 | 43 | 0 | 150 |
| S-13 Third-party code, build provenance, SBOM or vendor review is weakened | 20 (1) | **126** | **69** | 11 | 45 | 88 | **67** | 0 | 150 |
| S-14 Secrets, keys or cryptographic posture are degraded | 16 (2) | **107** | **47** | 26 | 35 | 72 | **22** | 0 | 150 |
| S-15 Change control, segregation of duties or a change freeze is bypassed | 26 (0) | **119** | **73** | 0 | 37 | 86 | **59** | 0 | 150 |
| S-16 Accessibility of a customer-facing surface regresses | 2 (0) | **17** | **13** | 0 | 6 | **12** | 13 | 0 | 150 |
| S-17 Marketing, communications or subscription practices breach consent or anti-dark-pattern rules | 8 (3) | **33** | **15** | 43 | **11** | **24** | 18 | 240 | 150 |
| S-18 Data-subject rights operations fail: access, portability, erasure, unlearning, offboarding return | 5 (1) | **26** | **19** | 13 | 7 | 22 | **16** | 0 | 150 |
| S-19 Lawful-access, legal hold and government-request handling is mis-implemented | 4 (2) | **25** | **9** | **31** | 5 | 8 | 7 | 0 | 150 |
| S-20 Incident communication, status reporting or root-cause delivery to customers is degraded | 11 (0) | **55** | **37** | 0 | 15 | 30 | 34 | 0 | 150 |
| S-21 Environmental, energy or ESG reporting integrity is compromised | 3 (1) | **10** | **7** | 15 | 4 | 6 | **11** | 0 | 150 |
| S-22 Employee or worker monitoring and personnel data are mishandled | 9 (3) | **40** | **18** | 35 | 14 | 30 | 25 | 240 | 150 |
| S-23 Model governance fails: validation, monitoring, sandbagging, red-team coverage, documentation | 14 (0) | **85** | **39** | 0 | 28 | 86 | **58** | 0 | 150 |
| S-28 OT protocol security, network segmentation or vendor remote access is weakened | 3 (0) | **25** | **15** | 0 | 5 | 18 | **15** | 0 | 150 |
| S-33 Telemetry, alerting or evidence integrity is degraded | 30 (2) | **185** | **91** | **33** | 60 | 154 | 74 | 0 | 150 |
| S-34 Governance of the rulebook itself is circumvented | 6 (1) | **41** | **23** | 13 | 13 | 20 | 5 | 0 | **150** |
| S-36 Operational resilience, latency or availability floors on critical paths regress | 33 (0) | **153** | **97** | 0 | 39 | 112 | **38** | 0 | 150 |

Constitution notes for the lawmakers: S-01: only absolute provisions mapped; no ordinary limb to deny, accept or pair; S-09: only absolute provisions mapped; no ordinary limb to deny, accept or pair; S-23: floor expected, no absolute provision mapped.
