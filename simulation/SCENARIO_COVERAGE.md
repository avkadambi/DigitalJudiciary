# Scenario coverage across the five packs

Catalogue 1.0.0; every count ⟦measured⟧ on the corpus version shown. Cells are cases exercising the scenario in that mechanism: A compliant touch (guard), B plain deny, F floor short-circuit, P pressure twin, V like-case, G risk-owner acceptance, W cross-jurisdiction, H control plane. `·` = the scenario does not apply to the pack (no provision maps to it). `req` lists the mechanisms the catalogue demands; VC-50 fails on any demanded cell that is empty.

| pack | corpus | cases | provisions | absolute | classes applicable | required cells empty |
|---|---|---|---|---|---|---|
| vetpoc | 2.1.0 | 6,000 | 121 | 26 | 22 | 0 |
| semifab | 2.1.0 | 6,000 | 126 | 28 | 24 | 0 |
| frontierllm | 2.1.0 | 6,000 | 139 | 31 | 25 | 0 |
| dcvigil | 2.1.0 | 6,000 | 134 | 26 | 26 | 0 |
| meridian | 2.1.0 | 6,000 | 142 | 33 | 26 | 0 |

## S-01 — Sanctions, denied-party and restricted-destination screening is weakened or bypassed

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 15 (8) | **78** | 36 | **101** | **22** | 36 | 6 | 240 | 150 |
| frontierllm | 1 (1) | **2** | 0 | **13** | **1** | 0 | 0 | 0 | 150 |
| dcvigil | 2 (2) | **4** | 0 | **26** | **2** | 0 | 0 | 0 | 150 |
| meridian | 12 (5) | **54** | 31 | **44** | **22** | 40 | 12 | 0 | 150 |

## S-02 — Personal or controlled data leaves its lawful region, boundary or tenant

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B V.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 15 (2) | **119** | **56** | **31** | 42 | **78** | 52 | 0 | 150 |
| semifab | 8 (2) | **47** | **23** | **25** | 13 | **36** | 31 | 0 | 150 |
| frontierllm | 11 (2) | **68** | **39** | **21** | 19 | **46** | 46 | 0 | 150 |
| dcvigil | 14 (6) | **61** | **26** | **79** | 19 | **32** | 22 | 240 | 150 |
| meridian | 13 (2) | **81** | **37** | **19** | 24 | **52** | 36 | 240 | 150 |

## S-03 — A regulated record is destroyed, overwritten, back-dated or its retention shortened

Harm classes: legal, regulatory, financial. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 21 (9) | **112** | **57** | **123** | 36 | 80 | 45 | 0 | 150 |
| semifab | 9 (3) | **53** | **25** | **43** | 21 | 20 | 26 | 0 | 150 |
| frontierllm | 16 (2) | **99** | **53** | **19** | 27 | 66 | 39 | 0 | 150 |
| dcvigil | 7 (3) | **18** | **8** | **51** | 6 | 10 | 2 | 0 | 150 |
| meridian | 26 (5) | **153** | **73** | **59** | 45 | 90 | 72 | 240 | 150 |

## S-04 — A statutory notification or filing clock is disabled, extended or made configurable

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 5 (3) | **21** | **13** | **40** | **8** | 18 | 10 | 0 | 150 |
| semifab | 2 (1) | **7** | **10** | **12** | **2** | 4 | 6 | 0 | 150 |
| frontierllm | 3 (2) | **12** | **4** | **25** | **4** | 2 | 7 | 0 | 150 |
| dcvigil | 9 (2) | **41** | **20** | **30** | **11** | 22 | 13 | 0 | 150 |
| meridian | 18 (6) | **81** | **39** | **50** | **30** | 58 | 29 | 0 | 150 |

## S-05 — A prohibited AI practice or manipulative technique is implemented

Harm classes: legal, reputational. Floor expected: yes. Required mechanisms: F A.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 6 (1) | **48** | 27 | **12** | 14 | 26 | 9 | 0 | 150 |
| semifab | 6 (1) | **46** | 24 | **12** | 16 | 30 | 5 | 0 | 150 |
| frontierllm | 10 (2) | **61** | 29 | **18** | 18 | 42 | 12 | 0 | 150 |
| dcvigil | 11 (4) | **49** | 19 | **46** | 17 | 36 | 28 | 240 | 150 |
| meridian | 11 (2) | **50** | 26 | **24** | 17 | 28 | 24 | 0 | 150 |

## S-06 — A protected characteristic or a proxy for one enters an automated decision

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B V.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 6 (1) | **40** | **19** | **6** | 11 | **26** | 5 | 0 | 150 |
| dcvigil | 9 (4) | **35** | **15** | **42** | 12 | **24** | 18 | 240 | 150 |
| meridian | 13 (4) | **65** | **26** | **36** | 19 | **38** | 9 | 0 | 150 |

## S-07 — Child safety: CSAM handling, age assurance, minors' data and interactions

Harm classes: legal, reputational, safety. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 1 (0) | **10** | **5** | 0 | 4 | 6 | 3 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 5 (2) | **24** | **20** | **24** | 9 | 12 | 14 | 0 | 150 |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 1 (0) | **4** | **4** | 0 | 2 | 2 | 2 | 0 | 150 |

## S-08 — Life-safety, physical actuation or clinical-safety control is suppressed or bypassed

Harm classes: safety, legal, reputational. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 13 (3) | **85** | **47** | **43** | **34** | 64 | 46 | 0 | 150 |
| semifab | 13 (5) | **77** | **30** | **63** | **25** | 54 | 47 | 0 | 150 |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 18 (5) | **104** | **64** | **76** | **33** | 68 | 46 | 0 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-09 — Export-controlled technology, defence articles or model weights reach an unauthorised person or destination

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 18 (8) | **101** | **58** | **96** | 26 | 52 | 17 | 240 | 150 |
| frontierllm | 10 (4) | **47** | **20** | **51** | 17 | 30 | 35 | 0 | 150 |
| dcvigil | 1 (1) | **2** | 0 | **11** | 1 | 0 | 0 | 0 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-10 — A consumer's statutory right, cap or window is made configurable or removed

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B V.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 13 (3) | **89** | **47** | **34** | 35 | **62** | 62 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 4 (3) | **13** | **6** | **39** | 5 | **10** | 6 | 0 | 150 |
| meridian | 20 (9) | **87** | **47** | **99** | 31 | **60** | 22 | 0 | 150 |

## S-11 — The human-review or contest path for an automated decision is removed

Harm classes: legal, regulatory, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 5 (1) | **35** | **20** | **9** | 11 | 24 | 4 | 0 | 150 |
| semifab | 6 (1) | **46** | **24** | **12** | 16 | 30 | 5 | 0 | 150 |
| frontierllm | 8 (1) | **49** | **24** | **13** | 14 | 34 | 7 | 0 | 150 |
| dcvigil | 6 (2) | **37** | **18** | **24** | 13 | 16 | 4 | 0 | 150 |
| meridian | 23 (3) | **116** | **60** | **27** | 35 | 94 | 31 | 0 | 150 |

## S-12 — An autonomous agent's mandate, loop limit, cost breaker or human stop is widened or removed

Harm classes: financial, safety, reputational. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 8 (2) | **56** | **31** | **30** | **15** | 32 | 6 | 0 | 150 |
| semifab | 8 (2) | **41** | **23** | **20** | **16** | 44 | 6 | 0 | 150 |
| frontierllm | 14 (3) | **82** | **39** | **34** | **28** | 64 | 13 | 0 | 150 |
| dcvigil | 13 (2) | **71** | **46** | **24** | **25** | 50 | 43 | 0 | 150 |
| meridian | 5 (2) | **22** | **9** | **26** | **7** | 10 | 2 | 0 | 150 |

## S-13 — Third-party code, build provenance, SBOM or vendor review is weakened

Harm classes: regulatory, legal, financial. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 10 (0) | **84** | **37** | 0 | 24 | 68 | **49** | 0 | 150 |
| semifab | 19 (1) | **100** | **46** | 13 | 32 | 72 | **67** | 0 | 150 |
| frontierllm | 23 (6) | **120** | **66** | 68 | 41 | 94 | **17** | 0 | 150 |
| dcvigil | 20 (1) | **126** | **69** | 11 | 45 | 88 | **67** | 0 | 150 |
| meridian | 21 (1) | **97** | **49** | 13 | 30 | 78 | **84** | 0 | 150 |

## S-14 — Secrets, keys or cryptographic posture are degraded

Harm classes: regulatory, financial. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 24 (1) | **164** | **79** | 16 | 52 | 112 | **90** | 0 | 150 |
| semifab | 13 (1) | **68** | **36** | 19 | 23 | 54 | **8** | 0 | 150 |
| frontierllm | 34 (6) | **150** | **78** | 66 | 49 | 130 | **22** | 0 | 150 |
| dcvigil | 16 (2) | **107** | **47** | 26 | 35 | 72 | **22** | 0 | 150 |
| meridian | 16 (3) | **79** | **42** | 35 | 27 | 60 | **44** | 0 | 150 |

## S-15 — Change control, segregation of duties or a change freeze is bypassed

Harm classes: regulatory, financial. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 8 (0) | **15** | **8** | 0 | 5 | 16 | **7** | 0 | 150 |
| semifab | 15 (1) | **55** | **40** | 10 | 18 | 58 | **16** | 0 | 150 |
| frontierllm | 8 (3) | **45** | **20** | 33 | 15 | 26 | **5** | 0 | 150 |
| dcvigil | 26 (0) | **119** | **73** | 0 | 37 | 86 | **59** | 0 | 150 |
| meridian | 14 (1) | **68** | **37** | 10 | 18 | 50 | **56** | 0 | 150 |

## S-16 — Accessibility of a customer-facing surface regresses

Harm classes: legal, reputational. Floor expected: no. Required mechanisms: A B V.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 2 (0) | **14** | **9** | 0 | 4 | **12** | 9 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 2 (0) | **17** | **13** | 0 | 6 | **12** | 13 | 0 | 150 |
| meridian | 1 (0) | **6** | **5** | 0 | 2 | **8** | 4 | 0 | 150 |

## S-17 — Marketing, communications or subscription practices breach consent or anti-dark-pattern rules

Harm classes: legal, reputational. Floor expected: no. Required mechanisms: A B V P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 13 (3) | **87** | **48** | 34 | **34** | **50** | 69 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 8 (3) | **33** | **15** | 43 | **11** | **24** | 18 | 240 | 150 |
| meridian | 14 (1) | **95** | **58** | 12 | **27** | **66** | 45 | 0 | 150 |

## S-18 — Data-subject rights operations fail: access, portability, erasure, unlearning, offboarding return

Harm classes: legal, regulatory, reputational. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 8 (1) | **60** | **32** | 16 | 24 | 42 | **51** | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 8 (1) | **54** | **30** | 9 | 13 | 40 | **32** | 0 | 150 |
| dcvigil | 5 (1) | **26** | **19** | 13 | 7 | 22 | **16** | 0 | 150 |
| meridian | 10 (0) | **75** | **33** | 0 | 20 | 44 | **51** | 240 | 150 |

## S-19 — Lawful-access, legal hold and government-request handling is mis-implemented

Harm classes: legal, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 7 (2) | **38** | **17** | **27** | 12 | 32 | 29 | 0 | 150 |
| frontierllm | 1 (0) | **7** | **3** | 0 | 3 | 6 | 7 | 0 | 150 |
| dcvigil | 4 (2) | **25** | **9** | **31** | 5 | 8 | 7 | 0 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-20 — Incident communication, status reporting or root-cause delivery to customers is degraded

Harm classes: reputational, regulatory. Floor expected: no. Required mechanisms: A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 9 (2) | **56** | **24** | 31 | 18 | 32 | 42 | 0 | 150 |
| dcvigil | 11 (0) | **55** | **37** | 0 | 15 | 30 | 34 | 0 | 150 |
| meridian | 13 (1) | **66** | **30** | 12 | 20 | 54 | 23 | 0 | 150 |

## S-21 — Environmental, energy or ESG reporting integrity is compromised

Harm classes: regulatory, reputational. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 2 (1) | **7** | **10** | 7 | 2 | 4 | **6** | 0 | 150 |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 3 (1) | **10** | **7** | 15 | 4 | 6 | **11** | 0 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-22 — Employee or worker monitoring and personnel data are mishandled

Harm classes: legal, reputational. Floor expected: no. Required mechanisms: A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 7 (2) | **48** | **24** | 24 | 17 | 30 | 5 | 0 | 150 |
| frontierllm | 2 (0) | **12** | **16** | 0 | 3 | 8 | 10 | 0 | 150 |
| dcvigil | 9 (3) | **40** | **18** | 35 | 14 | 30 | 25 | 240 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-23 — Model governance fails: validation, monitoring, sandbagging, red-team coverage, documentation

Harm classes: regulatory, reputational, safety. Floor expected: yes. Required mechanisms: F A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 1 (0) | **8** | **7** | 0 | 1 | 8 | **5** | 0 | 150 |
| frontierllm | 24 (5) | **137** | **80** | **63** | 47 | 88 | **101** | 240 | 150 |
| dcvigil | 14 (0) | **85** | **39** | 0 | 28 | 86 | **58** | 0 | 150 |
| meridian | 16 (2) | **83** | **37** | **12** | 25 | 54 | **25** | 0 | 150 |

## S-24 — Quality-system and customer-change-notification duties are skipped

Harm classes: financial, legal, reputational. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 8 (2) | **56** | **31** | 29 | 15 | 32 | **6** | 0 | 150 |
| semifab | 4 (0) | **33** | **20** | 0 | 9 | 26 | **26** | 0 | 150 |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-25 — Financial-crime programme breadth: CTR, PEP/EDD, 314(a), Travel Rule, fraud and identity-theft controls

Harm classes: legal, regulatory, financial. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 22 (9) | **99** | **65** | **81** | **37** | 70 | 29 | 0 | 150 |

## S-26 — Tax, escheat, dormant-account and reporting obligations are broken

Harm classes: legal, financial. Floor expected: no. Required mechanisms: A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 1 (0) | **5** | **5** | 0 | 2 | 4 | 5 | 0 | 150 |

## S-27 — Insider threat, exfiltration detection or personnel vetting for crown-jewel assets is weakened

Harm classes: safety, legal, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 9 (3) | **49** | **21** | **31** | 15 | 20 | 10 | 0 | 150 |
| frontierllm | 10 (4) | **49** | **23** | **49** | 17 | 32 | 35 | 0 | 150 |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-28 — OT protocol security, network segmentation or vendor remote access is weakened

Harm classes: safety, regulatory. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 4 (0) | **27** | **18** | 0 | 11 | 18 | **26** | 0 | 150 |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | 3 (0) | **25** | **15** | 0 | 5 | 18 | **15** | 0 | 150 |
| meridian | · | · | · | · | · | · | · | · | · |

## S-29 — Public-health, welfare and mandated-reporting duties are disabled

Harm classes: legal, safety, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 10 (2) | **27** | **16** | **33** | 8 | 18 | 16 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-30 — An AI assistant or generated content harms users: harmful advice, self-harm, persuasion, unmarked synthetic media

Harm classes: reputational, legal, safety. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 1 (0) | **13** | **7** | 0 | **3** | 2 | 5 | 0 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 13 (3) | **83** | **47** | **27** | **25** | 54 | 34 | 0 | 150 |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 7 (0) | **38** | **19** | 0 | **13** | 30 | 26 | 0 | 150 |

## S-31 — Responsible sourcing and part integrity: conflict minerals, forced labour, counterfeit and grey-market parts

Harm classes: legal, reputational, safety. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 4 (1) | **28** | **24** | 12 | 7 | 14 | **17** | 0 | 150 |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-32 — Ledger, numeric or financial-reporting integrity is compromised

Harm classes: financial, regulatory, legal. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 17 (4) | **68** | **34** | **44** | 21 | 36 | 8 | 0 | 150 |

## S-33 — Telemetry, alerting or evidence integrity is degraded

Harm classes: regulatory, safety, financial. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 20 (1) | **153** | **87** | **18** | 53 | 126 | 106 | 0 | 150 |
| semifab | 11 (4) | **58** | **34** | **48** | 26 | 30 | 34 | 0 | 150 |
| frontierllm | 14 (4) | **80** | **44** | **49** | 31 | 40 | 64 | 0 | 150 |
| dcvigil | 30 (2) | **185** | **91** | **33** | 60 | 154 | 74 | 0 | 150 |
| meridian | 7 (1) | **45** | **32** | **10** | 15 | 28 | 14 | 0 | 150 |

## S-34 — Governance of the rulebook itself is circumvented

Harm classes: regulatory. Floor expected: no. Required mechanisms: A B H.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 5 (0) | **37** | **27** | 0 | 12 | 28 | 5 | 0 | **150** |
| semifab | 5 (0) | **44** | **24** | 0 | 15 | 30 | 5 | 0 | **150** |
| frontierllm | 7 (0) | **47** | **24** | 0 | 13 | 34 | 7 | 0 | **150** |
| dcvigil | 6 (1) | **41** | **23** | 13 | 13 | 20 | 5 | 0 | **150** |
| meridian | 7 (0) | **38** | **26** | 0 | 12 | 46 | 7 | 0 | **150** |

## S-35 — Vulnerable-customer and servicemember protections are removed

Harm classes: legal, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | 4 (2) | **16** | **16** | **20** | 4 | 4 | 16 | 0 | 150 |

## S-36 — Operational resilience, latency or availability floors on critical paths regress

Harm classes: financial, safety, regulatory. Floor expected: no. Required mechanisms: A B G.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 7 (0) | **13** | **14** | 0 | 4 | 14 | **14** | 0 | 150 |
| semifab | 31 (2) | **152** | **89** | 28 | 48 | 120 | **82** | 0 | 150 |
| frontierllm | 8 (0) | **30** | **16** | 0 | 8 | 28 | **18** | 0 | 150 |
| dcvigil | 33 (0) | **153** | **97** | 0 | 39 | 112 | **38** | 0 | 150 |
| meridian | 7 (0) | **31** | **13** | 0 | 9 | 26 | **20** | 0 | 150 |

## S-37 — Controlled substances, prescribing and dispensing controls are weakened

Harm classes: legal, safety, reputational. Floor expected: yes. Required mechanisms: F A B P.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | 25 (13) | **109** | **55** | **176** | **39** | 68 | 34 | 240 | 150 |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | · | · | · | · | · | · | · | · | · |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-38 — Training-data provenance, licensing, copyright and opt-out are breached

Harm classes: legal, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | · | · | · | · | · | · | · | · | · |
| frontierllm | 16 (3) | **59** | **30** | **36** | 18 | 32 | 40 | 0 | 150 |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## S-39 — Recipe, process and design IP leaks through logs, caches, telemetry or model context

Harm classes: legal, financial, reputational. Floor expected: yes. Required mechanisms: F A B.

| pack | provisions (abs) | A | B | F | P | V | G | W | H |
|---|---|---|---|---|---|---|---|---|---|
| vetpoc | · | · | · | · | · | · | · | · | · |
| semifab | 7 (2) | **43** | **16** | **20** | 12 | 16 | 5 | 0 | 150 |
| frontierllm | 18 (3) | **71** | **28** | **33** | 21 | 60 | 9 | 0 | 150 |
| dcvigil | · | · | · | · | · | · | · | · | · |
| meridian | · | · | · | · | · | · | · | · | · |

## Constitution notes for the lawmakers

Findings about the rulebooks, not the corpora: where the catalogue expects a floor and a pack maps no absolute provision, or where a class has no ordinary limb. Each is a candidate draft amendment; none is applied here (A3).

- vetpoc: S-07: floor expected, no absolute provision mapped
- vetpoc: S-30: floor expected, no absolute provision mapped
- semifab: S-23: floor expected, no absolute provision mapped
- frontierllm: S-01: only absolute provisions mapped; no ordinary limb to deny, accept or pair
- frontierllm: S-19: floor expected, no absolute provision mapped
- dcvigil: S-01: only absolute provisions mapped; no ordinary limb to deny, accept or pair
- dcvigil: S-09: only absolute provisions mapped; no ordinary limb to deny, accept or pair
- dcvigil: S-23: floor expected, no absolute provision mapped
- meridian: S-07: floor expected, no absolute provision mapped
- meridian: S-30: floor expected, no absolute provision mapped
