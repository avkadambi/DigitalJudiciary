# 04 — Compliance Obligations for Monitoring/Observability + Agent-Overhead Benchmarking

Research lane 04 for the DCVigil open conformance corpus.
Domain: multi-tenant datacenter monitoring platform. Ingests customer telemetry (logs that may
contain PII/PHI and payment data), badge/physical-access logs, facility CCTV. Operates EU + US.
Audited under SOC 2 and ISO 27001. Can actuate customer physical infrastructure.

Date of research: 2026-09-05. All licence/legal statuses below are either **VERIFIED** against a
primary source read during this survey, or explicitly marked **UNVERIFIED**.

Baselines carried forward from the earlier survey and *not* re-derived here:
- EU legislative texts on EUR-Lex reusable under Commission Decision 2011/833/EU.
- US CFR/USC and NIST publications public domain under 17 U.S.C. §105.
- `usnistgov/oscal-content` is CC0 1.0.
- ComplianceAsCode is BSD-3-Clause.

---

## Part 1 — Audit evidence regimes

### 1.1 AICPA Trust Services Criteria (SOC 2)

| | |
|---|---|
| **Name** | 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (with Revised Points of Focus — 2022). Also cited as TSP section 100. |
| **URL** | https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022 |
| **Contents** | The criteria SOC 2 examinations are conducted against. Common Criteria CC1–CC9 (mapped onto COSO's 17 principles) plus category-specific criteria for Availability (A1), Processing Integrity (PI1), Confidentiality (C1) and Privacy (P1–P8). Directly relevant here: **CC6.1** (logical access), **CC6.6** (boundary protection), **CC6.7** (transmission/movement/removal of information), **CC7.2** (monitoring for anomalies), **CC7.3/CC7.4** (incident evaluation and response), **CC8.1** (change management — this is the criterion an agentic change-management pack sits under), **A1.2** (environmental protections, backup/recovery), **C1.1/C1.2** (confidential information retention and disposal). |
| **Licence status** | **VERIFIED: NOT open, and not paywalled either — it is gated.** The PDF (`Trust-services-criteria.pdf`, ~554 KB) is downloadable at **zero cost** but requires a **free AICPA/CIMA account login**. The download page offers a separate link, "Download the Trust Services Criteria with Copyright Information", confirming AICPA asserts copyright over the document. **No open licence, no reproduction grant, and no CC-style permission was found.** Copyright is held by AICPA (with COSO material inside it separately © 2019 Committee of Sponsoring Organizations of the Treadway Commission, all rights reserved). |
| **How to reuse** | **Do NOT reproduce criterion text in the corpus.** Reuse by *reference only*: cite as "TSC CC8.1" / "TSC CC7.2" as a **factor vocabulary label** on a provision whose normative text you write yourself. This is the same treatment ISO gets (below). A conformance pack can legitimately say "provision P-014 is motivated by SOC 2 CC8.1" without quoting AICPA. |
| **Caveat for the pack** | Because the corpus must be openly redistributable, SOC 2 cannot supply *provision text*. It can only supply *traceability tags*. Anyone building the pack should treat any PR that pastes TSC criterion text as a licence defect. |

**Freely citable proxy that IS open:** NIST publishes an
[AICPA 2017 TSC ↔ NIST Privacy Framework crosswalk](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/american-institute-certified-public-accountants-aicpa).
The crosswalk is a NIST work (public domain, 17 U.S.C. §105) but it *contains* AICPA criterion
identifiers and short descriptors. Safe to use the identifiers; treat the descriptors as
AICPA-derived and do not bulk-copy. **Status of the descriptors specifically: UNVERIFIED** — NIST
does not state whether it licensed that text.

### 1.2 ISO/IEC 27001 and 27002

| | |
|---|---|
| **Name** | ISO/IEC 27001:2022 (ISMS requirements) + Amd 1:2024; ISO/IEC 27002:2022 (information security controls) |
| **URL** | https://www.iso.org/standard/27001 ; https://webstore.ansi.org/standards/iso/isoiec2700220222013security |
| **Contents** | 27001 Annex A lists 93 controls in four themes. Directly relevant: A.5.28 (collection of evidence), A.8.15 (logging), A.8.16 (monitoring activities), A.8.11 (data masking), A.8.32 (change management), A.7.4 (physical security monitoring — this is the CCTV control), A.5.34 (privacy and PII protection). 27002 supplies the implementation guidance for each. |
| **Licence status** | **VERIFIED: PAYWALLED. CHF 155** for ISO/IEC 27001:2022 in PDF+ePub from iso.org. Only an OBP preview is free. ISO states: *"All ISO publications and materials are protected by copyright and are subject to the user's acceptance of ISO's conditions of copyright."* ISO additionally **explicitly prohibits use of its content for machine learning / AI training without authorisation** — a direct hazard for anyone tempted to embed 27002 text into a corpus meant to evaluate AI agents. Amendment 1:2024 is listed at CHF 0 but is only the amendment, not the standard. |
| **How to reuse** | **Reference only.** Use control identifiers (`ISO/IEC 27001:2022 A.8.15`) as **factor vocabulary**. Write your own provision text. Never embed 27002 guidance prose. |
| **Open substitute** | Where you need actual reusable *control text* with the same semantics, use **NIST SP 800-53 Rev. 5 via `usnistgov/oscal-content` (CC0)** and rely on the published NIST-to-ISO mapping. This gives you machine-readable, freely redistributable text covering the same ground. |

### 1.3 The "log immutability + 7-year retention" claim — WHAT IT ACTUALLY RESTS ON

This is the most important negative finding in this lane. **The seven-year figure is not traceable
to any single instrument that binds a datacenter monitoring vendor.** Evidence:

- **NIST SP 800-53 AU-11 (Audit Record Retention)** — verified verbatim from the CC0 OSCAL catalog:
  > "Retain audit records for {{ insert: param, au-11_odp }} to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention requirements."

  The period is an **organisation-defined parameter**. NIST sets no number.
- **FedRAMP** — verified against FedRAMP's own 2026 consolidated controls reference
  (https://www.fedramp.gov/2026/reference/controls/audit-and-accountability/): AU-11 is listed
  with the assignment **left open**, "no pre-defined retention period". So FedRAMP does not supply
  the seven years either. (Operational FedRAMP guidance commonly cites one year online / three
  years total, but this is **UNVERIFIED** against a current authoritative FedRAMP parameter table
  and should not be asserted.)
- **PCI DSS Req. 10.5.1** — the only *hard number* in the neighbourhood: retain audit log history
  for **at least 12 months**, with **at least the most recent 3 months immediately available** for
  analysis. That is 12 months, not 7 years. (Consistently reported across secondary sources;
  primary text is paywalled — see 1.4.)
- **HIPAA 45 C.F.R. §164.316(b)(2)(i)** — **6 years**, and it applies to *the required documentation*
  (policies, procedures, records of required actions/activities/assessments), **not** to audit logs
  as such. The widespread "HIPAA requires 6 years of audit logs" claim is an inference, not the
  regulation's text. Public domain (US CFR).
- **SOC 2 / TSC** — sets **no** retention period. CC7.2 and C1.2 require retention consistent with
  the entity's own commitments and policy. SOC 2 turns your own stated retention policy into the
  audit criterion.
- **SEC 17 C.F.R. §240.17a-4** — this *is* where the WORM/immutability idea comes from (6 years for
  certain broker-dealer records, on non-rewriteable non-erasable media, or an audit-trail
  alternative under the 2022 amendments). It binds **broker-dealers**, not monitoring vendors.
  A DCVigil-type platform inherits it only contractually, if a broker-dealer customer flows it down.

**Conclusion for the pack.** "Security-audit-log immutability with 7-year retention" is a
**contractual/commercial commitment**, most plausibly a customer-flow-down or the vendor's own
published trust commitment, that SOC 2 then *makes auditable*. It is legitimately ABSOLUTE — but the
justification in the provision must say so honestly. Writing "required by SOC 2" or "required by
HIPAA" would be **factually wrong** and would be a defect if a reviewer checked it.

Recommended provision rationale text: *immutability* rests on NIST SP 800-53 **AU-9** (verified
verbatim, CC0): "Protect audit information and audit logging tools from unauthorized access,
modification, and deletion; and Alert [ODP] upon detection of unauthorized access, modification, or
deletion of audit information", reinforced by **AU-9(3)** "Implement cryptographic mechanisms to
protect the integrity of audit information and audit tools." The *seven years* rests on the vendor's
own commitment, floor-set by PCI DSS 10.5.1 (12 months) where cardholder data is in scope.

### 1.4 PCI DSS Requirement 10

| | |
|---|---|
| **Name** | PCI DSS v4.0.1, Requirement 10 — "Log and Monitor All Access to System Components and Cardholder Data" |
| **URL** | https://www.pcisecuritystandards.org/ (Document Library) |
| **Contents** | 10.2 what must be logged (all individual user access to CHD, all admin actions, all access to audit logs, invalid access attempts, identification/authentication changes, initialisation/stopping/pausing of logs, creation/deletion of system-level objects); 10.2.2 the mandatory log record fields (user ID, event type, date/time, success/failure, origination, affected data/component/resource); 10.3 protection of audit logs (10.3.1 read access limited to job-need; **10.3.2 protection from modification**; 10.3.3 write to a secured internal server or media hard to alter; 10.3.4 file integrity monitoring on logs); **10.5.1 retain ≥12 months, ≥3 months immediately available**; 10.6 time synchronisation; 10.7 failure of critical security control systems detected/alerted/responded to. |
| **Licence status** | **VERIFIED: NOT redistributable.** PCI SSC Terms and Conditions (https://www.pcisecuritystandards.org/terms_and_conditions/) grant only: *"You may view, download and print any materials and information owned and made available by the Council on or through the Services … solely for your own personal, non-commercial, review, study and informational purposes."* and expressly prohibit: *"you may not publish, distribute, copy, assign, license, sublicense, transfer, sell, prepare derivative works of, or use for any non-personal purpose, any Content."* Standards documents themselves are free-of-charge downloads from the Document Library but sit under this restrictive licence; a separate **Material License Agreement** exists for other uses. |
| **How to reuse** | **Requirement identifiers only** (`PCI DSS v4.0.1 Req. 10.3.2`, `Req. 10.5.1`) as factor vocabulary and as a numeric **oracle** for the retention floor. Do not quote the requirement text into the corpus; paraphrase into your own provision language. A conformance pack that ships PCI DSS text is redistributing PCI SSC Content for a non-personal purpose and violates the terms. |

---

## Part 2 — EU obligations

All EUR-Lex texts below: reusable under **Commission Decision 2011/833/EU** (baseline). These are
the corpus's best source of **directly reusable provision text**.

### 2.1 GDPR — Regulation (EU) 2016/679

URL: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 (verbatim verified)

- **Art. 5(1)** principles: (a) lawfulness, fairness and transparency; (b) purpose limitation;
  (c) data minimisation; (d) accuracy; (e) storage limitation; (f) integrity and confidentiality.
  Art. 5(2) accountability. → **Storage limitation (5(1)(e)) is in direct tension with the 7-year
  audit-log retention commitment** wherever those logs contain personal data. The corpus should
  contain at least one scenario that forces the agent to resolve that tension (answer: separate the
  security audit trail from customer telemetry; retention justified under Art. 6(1)(f) and
  Art. 32; minimise personal data in the audit trail itself).
- **Art. 9(1)**: processing of special-category data prohibited, including *"biometric data for the
  purpose of uniquely identifying a natural person"* and *"data concerning health"*. → **Badge
  systems that store biometric templates, and CCTV used for facial identification, land here.**
  Health data can arrive incidentally in ingested customer logs (PHI).
- **Art. 32(1)**: appropriate technical and organisational measures including
  "(a) the pseudonymisation and encryption of personal data; (b) the ability to ensure the ongoing
  confidentiality, integrity, availability and resilience of processing systems and services;
  (c) the ability to restore the availability and access to personal data in a timely manner in the
  event of a physical or technical incident; (d) a process for regularly testing, assessing and
  evaluating the effectiveness of technical and organisational measures".
  → **(d) is the hook that makes the change-management pack itself a GDPR obligation.**
- **Art. 33(1)**: *"In the case of a personal data breach, the controller shall without undue delay
  and, where feasible, not later than 72 hours after having become aware of the personal data
  breach, notify the personal data breach to the supervisory authority…"* Art. 33(2): **processor
  must notify the controller without undue delay** — for a monitoring vendor that is usually a
  processor, **33(2) is the operative duty, not 33(1)**. Getting this right is a good corpus
  discriminator: many agents will cite 33(1)/72h at a processor.
- **Art. 7(3)**: *"The data subject shall have the right to withdraw consent at any time. The
  withdrawal of consent shall not affect the lawfulness of processing based on consent before its
  withdrawal."* Plus: withdrawal shall be as easy as giving consent.

**Reuse:** direct **provision text** (verbatim, attributed) and **oracle** (72h / 24h clocks are
checkable numerics).

### 2.2 NIS2 — Directive (EU) 2022/2555

URL: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022L2555 (verbatim verified)

- **In force:** VERIFIED — entered into force **16 January 2023**; published in OJ 27 December 2022.
- **Art. 41(1)** VERIFIED verbatim: *"By 17 October 2024, Member States shall adopt and publish the
  measures necessary to comply with this Directive"* and *"shall apply those measures from
  18 October 2024."*
- **Art. 23(4)** VERIFIED verbatim phrasing: early warning *"without undue delay and in any case not
  later than 24 hours"*; incident notification *"without undue delay and in any case not later than
  72 hours"*; final report *"without undue delay and in any case not later than one month"*.
  (Plus an intermediate report on request, and a progress report where the incident is ongoing at
  the one-month mark.)
- **Transposition variance — the critical practical point.** VERIFIED via the ECSO NIS2
  Transposition Tracker (https://ecs-org.eu/policy/nis2-directive-transposition-tracker/): only
  **four** Member States met the 17 Oct 2024 deadline; the Commission opened **infringement
  procedures against 23 Member States on 28 November 2024**; as of the tracker's 2026 update the
  Commission had issued a **reasoned opinion to 19 Member States** for incomplete transposition.
  ECSO's own count (primary laws only) is ~23/27 transposed; the Commission's stricter count
  (including secondary legislation and communication of measures) is far lower.
- **Consequence for the pack:** NIS2 is **a directive, not a regulation**. There is *no single
  NIS2 obligation text that binds an operator directly*. Compliance is against the national
  transposing law, and those diverge (registration thresholds, sectoral scope, whether "important"
  vs "essential" classification is self-assessed, penalty levels, whether the CSIRT or a sectoral
  regulator receives the report). **Therefore NIS2 Art. 23 should be a TIER-2 provision phrased as
  "the applicable national transposition of NIS2 Art. 23", not an absolute with a hard-coded EU
  clock.** An absolute provision citing "NIS2 Art. 23, 24h" would be legally sloppy and would
  produce false positives in Member States whose law is not yet in force.

**Reuse:** provision text + **oracle** on the 24h/72h/1-month clocks, but scoped as above.

### 2.3 EU AI Act — Regulation (EU) 2024/1689

Verbatim text verified via https://artificialintelligenceact.eu/article/5/ and /article/50/
(mirrors the OJ text; EUR-Lex is the authoritative source and is 2011/833/EU-reusable).

- **Art. 5 applies from 2 February 2025** (Art. 113(a)). VERIFIED.
- **Art. 5(1)(b)** — prohibited: an AI system *"that exploits any of the vulnerabilities of a
  natural person or a specific group of persons due to their age, disability or a specific social or
  economic situation, with the objective, or the effect, of materially distorting the behaviour of
  that person or a person belonging to that group in a manner that causes or is reasonably likely to
  cause that person or another person significant harm."*
- **Art. 5(1)(e)** — prohibited: AI systems *"that create or expand facial recognition databases
  through the untargeted scraping of facial images from the internet or CCTV footage."*
  → **This is the single most on-point AI Act provision for this domain.** A datacenter monitoring
  platform with facility CCTV that builds or enriches a face database from that footage is squarely
  in the prohibition. Note it says *untargeted scraping* — targeted, consented enrolment of a
  specific badge holder is not caught by (e), though it is caught by GDPR Art. 9 and by BIPA.
- **Art. 5(1)(f)** — prohibited: AI systems *"to infer emotions of a natural person in the areas of
  workplace and education institutions, except where the use of the AI system is intended to be put
  in place or into the market for medical or safety reasons."*
  → **A datacenter is a workplace.** Staff emotion inference from facility CCTV is prohibited.
  The "safety reasons" exception is narrow and, per Recital 44, is about detecting e.g. fatigue in
  safety-critical roles — it is not a general licence to run affect analytics on technicians.
- **Art. 50(1)** — transparency: providers shall ensure that AI systems **intended to interact
  directly with natural persons** are designed and developed such that the natural persons concerned
  are **informed that they are interacting with an AI system**, unless obvious to a reasonably
  well-informed observer, and subject to a law-enforcement carve-out.
  **Art. 50 applies from 2 August 2026** (VERIFIED) — i.e. **it is already in application as of the
  date of this research (2026-09-05)**. → binds the customer-facing AI assistant.

**Reuse:** direct **provision text**, and **strong oracle** — (e) and (f) are near-binary tests that
a corpus can score deterministically.

### 2.4 EU Data Act — Regulation (EU) 2023/2854, cloud switching

- **Applies from 12 September 2025.** VERIFIED (Art. 50). Chapter III obligations from that date;
  Chapter IV to contracts concluded after that date, extending to older indefinite/long contracts
  from 12 September 2027; Art. 3(1) to connected products placed on the market after
  12 September 2026.
- **Chapter VI (Arts. 23–31) — Switching between data processing services.** Covers removal of
  pre-commercial, commercial, technical, contractual and organisational obstacles to switching;
  Art. 25 mandatory contractual terms (max 2-month notice; **30-day mandatory transitional period**,
  extendable where technically unfeasible; **30-day retrieval period** after termination before
  erasure); Art. 23 obligation to remove obstacles; Art. 30 technical aspects including
  **functional equivalence** for IaaS and open interoperability specifications for PaaS/SaaS.
- **Art. 29 — gradual withdrawal of switching charges.** VERIFIED: *"From 12 January 2027, providers
  of data processing services shall not impose any"* switching charges. Between 11 January 2024 and
  12 January 2027, charges are capped at the provider's **direct costs** of switching.
- **Relevance:** a multi-tenant monitoring platform is a "data processing service" under the Data
  Act. Exit/egress of ingested telemetry, dashboards, alert rules and retained audit logs is in
  scope. **This is a Tier-2/Tier-3 obligation for this pack, not absolute** — it is a commercial and
  contractual duty, and violating it is not a safety or rights harm.

**Reuse:** provision text + **oracle** on the 12 Jan 2027 zero-charge date and the 30-day windows.

### 2.5 EU telemetry data residency

**Honest finding: there is no general EU data-residency *legal* requirement.** GDPR does not require
EU storage; Chapter V (Arts. 44–49) requires a transfer *mechanism* — adequacy decision, SCCs
(Decision 2021/914), BCRs, or a derogation. Post-*Schrems II* the controller/processor must also run
a transfer impact assessment and apply supplementary measures. The **EU–US Data Privacy Framework**
adequacy decision (July 2023) covers transfers to self-certified US organisations; its durability is
politically contested and its **current status as of 2026-09-05 is UNVERIFIED in this survey** — do
not assert it is or is not still in force without checking.

Where EU residency *is* genuinely binding it comes from: (a) sectoral national law (some Member
States' health, defence, or public-sector rules), (b) **the customer contract / DPA**, or
(c) the vendor's own published commitment. For DCVigil, EU telemetry residency is best understood as
a **contractual absolute** — and that is a perfectly good reason for it to be a Tier-1 provision;
the rationale text just must not claim "GDPR requires EU residency", which is false.

**Reuse:** SCC Decision 2021/914 and GDPR Chapter V as provision text (EUR-Lex, 2011/833/EU).

---

## Part 3 — US obligations

### 3.1 NIST SP 800-53 Rev. 5 — IA-2 and SC-8

| | |
|---|---|
| **Name** | NIST SP 800-53 Rev. 5 (Rev. 5.2.0, released 2025-08-27), Security and Privacy Controls for Information Systems and Organizations |
| **URL** | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final ; machine-readable: https://github.com/usnistgov/oscal-content/tree/main/nist.gov/SP800-53 |
| **Licence status** | **VERIFIED public domain.** `usnistgov/oscal-content` `LICENSE.md` states: *"As a work of the United States government, this project is in the public domain within the United States. Additionally, we waive copyright and related rights in the work worldwide through the CC0 1.0 Universal public domain dedication."* Control text is fully citable, quotable, and redistributable. |
| **Control text — extracted directly from the CC0 OSCAL catalog during this survey (authoritative, not paraphrased)** | |

- **IA-2 Identification and Authentication (Organizational Users):**
  > "Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users."
  - **IA-2(1)** Multi-factor Authentication to Privileged Accounts: *"Implement multi-factor authentication for access to privileged accounts."*
  - **IA-2(2)** Multi-factor Authentication to Non-privileged Accounts: *"Implement multi-factor authentication for access to non-privileged accounts."*
  - **IA-2(8)** Access to Accounts — Replay Resistant: *"Implement replay-resistant authentication mechanisms for access to [Selection: privileged accounts; non-privileged accounts]."*
- **SC-8 Transmission Confidentiality and Integrity:**
  > "Protect the [Selection (one or more): confidentiality; integrity] of transmitted information."
  - **SC-8(1)** Cryptographic Protection: *"Implement cryptographic mechanisms to [Selection (one or more): prevent unauthorized disclosure of information; detect changes to information] during transmission."*
- **AU-9 Protection of Audit Information** and **AU-9(3)**, **AU-11 Audit Record Retention** — quoted in §1.3 above.

**Reuse:** the strongest source in this whole lane. **Provision text (verbatim, redistributable),
factor vocabulary (control IDs), and oracle (OSCAL JSON is machine-checkable — you can
programmatically assert that a provision's cited control ID exists and that its parameters are
bound).** Note that IA-2, SC-8 and AU-11 are all **parameterised** — a corpus can use the
open-parameter structure to generate scenario variants.

### 3.2 FedRAMP

- **URL:** https://www.fedramp.gov/ ; controls reference https://www.fedramp.gov/2026/reference/controls/ ; OSCAL baselines at https://github.com/GSA/fedramp-automation
- **Contents:** Rev. 5 baselines (Low/Moderate/High) as tailored SP 800-53 profiles; continuous
  monitoring (ConMon) obligations — monthly vulnerability scanning and POA&M reporting, significant
  change requests, annual assessment; and the newer **FedRAMP 20x** programme with Key Security
  Indicators (KSIs).
- **Licence status:** FedRAMP documents and baselines are works of the US Government
  (GSA/FedRAMP PMO) and are treated as public domain under 17 U.S.C. §105. **However: the specific
  `LICENSE.md` of `GSA/fedramp-automation` could NOT be retrieved during this survey (404 at the
  path tried, and the GitHub API was unavailable from this environment). Status: UNVERIFIED at the
  repository level.** Do not assert a licence for that repo without checking it directly. The
  underlying 800-53 control text inside those baselines is unambiguously CC0 via NIST.
- **Verified substantive finding:** FedRAMP's own 2026 consolidated controls reference lists
  **AU-11 with the retention period left as an open organisation-defined assignment**, and AU-9
  with `[Assignment: organization-defined personnel or roles]` unfilled. **FedRAMP does not supply
  a 7-year number.**
- **Relevance:** only binding if DCVigil sells to US federal agencies. **Tier 3** for a general pack;
  Tier 1 for a federal-scoped variant. FedRAMP's real value to this corpus is as a source of
  **parameter values** (concrete numbers for otherwise open NIST assignments) that make scenarios
  checkable.

### 3.3 Illinois BIPA (740 ILCS 14) — biometric badge templates

| | |
|---|---|
| **Name** | Biometric Information Privacy Act, 740 ILCS 14 |
| **URL** | https://law.justia.com/codes/illinois/chapter-740/act-740-ilcs-14/ (statute text; Illinois Compiled Statutes are public-record state law) |
| **Contents (VERIFIED)** | **§15(a)** — written, publicly available retention policy and destruction schedule; destroy biometric identifiers when the initial purpose is satisfied or **within 3 years of the individual's last interaction, whichever occurs first**; destruction may be stayed by valid warrant or subpoena. **§15(b)** — before collection, must (1) inform the subject in writing that a biometric identifier is being collected/stored, (2) inform in writing of the **specific purpose and length of term** of collection/storage/use, and (3) obtain **a written release** executed by the subject. §15(c) no sale/lease/trade/profit. §15(d) no disclosure without consent. §15(e) reasonable standard of care, at least as protective as for other confidential/sensitive information. |
| **Private right of action — VERIFIED, and it is real** | **§20**: any person aggrieved may bring an action in state circuit court or as a supplemental claim in federal court, and a prevailing party may recover **$1,000 liquidated damages or actual damages, whichever is greater, for negligent violation**, and **$5,000 or actual damages, whichever is greater, for intentional or reckless violation**, plus **reasonable attorneys' fees and costs, expert witness fees**, and other relief including injunctive relief. **BIPA is the reason biometric badge data is the highest-litigation-risk data class in this platform.** |
| **2024 amendment — VERIFIED** | **P.A. 103-0769 (SB 2979), effective 2024-08-02**, added the per-person accrual limit: repeated collection or repeated disclosure of the same biometric identifier from the same person by the same private entity using the same method of collection constitutes **a single violation**, entitling the aggrieved person to **at most one recovery**. This legislatively overruled *Cothron v. White Castle*'s per-scan accrual. It also expressly permits an **electronic signature** to satisfy the §15(b) "written release". Retroactivity was contested; the Seventh Circuit has held the amendment applies retroactively — **status of that holding as of 2026-09-05: UNVERIFIED in this survey**, treat as unsettled. |
| **How to reuse** | **Provision text** (state statute, freely quotable) and a strong **oracle**: §15(a)'s "3 years from last interaction" and §15(b)'s three-part pre-collection test are deterministic checks. |

### 3.4 CCPA/CPRA

- **URL:** statute https://oag.ca.gov/privacy/ccpa ; CPPA regulations (Cal. Code Regs. tit. 11, div. 6)
  https://cppa.ca.gov/regulations/
- **Contents:** Since **1 January 2023** the CPRA removed the employee/HR and B2B exemptions —
  **employee and contractor personal information is fully in scope**, which is exactly what badge
  and physical-access logs are. **Biometric information is "sensitive personal information"**
  (Civ. Code §1798.140(ae)), triggering the right to limit use and disclosure of SPI (§1798.121),
  purpose-limitation, and notice at collection. Service-provider/contractor contract terms
  (§1798.140(ag)/(j) and the regs) constrain what a monitoring vendor may do with customer data.
  Data-minimisation and retention-disclosure duties under §1798.100(a)(3)/(c).
- **Licence status:** California statutes and the California Code of Regulations are state
  government edicts and freely quotable. **A formal open-licence statement was not located;
  status: reusable as an edict of government, but no explicit licence — UNVERIFIED as to any
  formal dedication.**
- **Relevance:** Tier 2. Overlaps heavily with GDPR; CCPA rarely adds an *absolute* that GDPR does
  not already imply, except SPI-limitation for biometrics.

---

## Part 4 — Physical actuation liability

**Headline finding: there is no standard or regulation that directly governs "software that
actuates datacenter cooling/power". The nearest instruments are all either paywalled, or govern
the equipment/worker rather than the software.** Being explicit about this gap is itself a
research result — it means the absolute provision on physical actuation cannot be traced to an
external authority and must be justified on first-principles harm reasoning plus the analogous
instruments below.

| Source | URL | Freely citable? | Notes |
|---|---|---|---|
| **IEC 62443-3-3:2013** (System security requirements and security levels for IACS) | https://webstore.iec.ch/en/publication/7033 | **NO — VERIFIED PAYWALLED at CHF 380.** IEC asserts "Copyright © IEC. All rights reserved." | Relevant control families: SR 1.x identification/authentication, SR 2.x use control, **SR 3.x system integrity**, SR 7.x resource availability. The IEC 62443 series is the closest thing to a governing standard for control-system actuation. **Identifiers usable as factor vocabulary; text not reusable.** |
| **ASHRAE Thermal Guidelines for Data Processing Environments, 5th ed. (2021, rev./expanded)** | ASHRAE Bookstore / https://webstore.ansi.org/standards/ashrae/ashraedatacombook5thedition | **NO — VERIFIED commercial book, sold by ASHRAE/ANSI/Amazon/MADCAD.** No free full text. | This is the source of the A1–A4 equipment class envelopes and the recommended/allowable temperature-humidity ranges. It is a **guideline, not a regulation** — no legal force. **Numeric envelopes could be used as an oracle if independently restated, but the tables themselves are copyrighted.** Some individual ASHRAE TC 9.9 *white papers* are posted free on ashrae.org (e.g. the 2016 Data Center Power Equipment Thermal Guidelines white paper) — **their reuse terms are UNVERIFIED.** |
| **Uptime Institute Tier Standard: Topology** | https://uptimeinstitute.com/resources/asset/tier-standard-topology | **Zero-cost download behind a registration form; NOT open.** The PDF's own copyright notice could **not** be retrieved (robots.txt disallowed) — **status of its reproduction terms: UNVERIFIED.** "Tier" is a registered Uptime Institute mark and its use is policed. | Tiers I–IV concern site topology redundancy (N, N+1, 2N, 2N+1) and concurrent maintainability / fault tolerance. **It says nothing about software actuation.** Use the Tier vocabulary only as descriptive scenario framing, and do not reproduce the document. |
| **NFPA 75** (Fire Protection of Information Technology Equipment) and **NFPA 76** (Fire Protection of Telecommunications Facilities); **NFPA 70/70E** | https://www.nfpa.org/for-professionals/codes-and-standards/list-of-codes-and-standards/free-access | **PARTIALLY free — "free access" is browser-based read-only viewing after registration.** Whether NFPA 75/76 specifically are in the free-access set, and whether copying/printing/redistribution is permitted, **could not be confirmed from the page fetched — UNVERIFIED.** NFPA codes are copyrighted; they become law where a jurisdiction adopts them by reference. | Relevant where actuation touches fire suppression, emergency power off (EPO), or air-handling interlocks. **NFPA 70E** (electrical safety in the workplace) is the more relevant one for "software energises equipment while a human is working on it." |
| **OSHA 29 C.F.R. §1910.147** — The control of hazardous energy (lockout/tagout) | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1910/subpart-J/section-1910.147 | **YES — US CFR, public domain (17 U.S.C. §105).** | **This is the strongest freely citable hook for the physical-actuation absolute.** LOTO requires that energy isolating devices be locked/tagged out and that equipment cannot be re-energised while servicing personnel are exposed. **Software that can remotely re-energise or restart cooling/power equipment is, functionally, a path around LOTO.** A provision requiring explicit customer-side confirmation before actuation is directly defensible as preserving the customer's LOTO regime. Also relevant: §1910.147(c)(4) energy control procedures, §1910.147(e)(3) verification of isolation. |
| **EU Machinery Regulation (EU) 2023/1230** | https://eur-lex.europa.eu/ (CELEX 32023R1230) | **YES — EUR-Lex, 2011/833/EU.** | Repeals the Machinery Directive; **applies from 20 January 2027**. Notably it brings **software with a safety function**, and **cyber-risk to safety functions**, into the essential health and safety requirements, and treats software performing a safety function as a "safety component". **Status of whether DCVigil-style actuation software falls in scope: UNVERIFIED and genuinely arguable** — it turns on whether the software performs a safety function of machinery. Worth flagging in the corpus as an emerging obligation rather than asserting it. |
| **IEC 61508** (functional safety of E/E/PE safety-related systems) | https://webstore.iec.ch/ | **NO — paywalled.** Price not verified in this survey. | The generic functional-safety standard behind SIL levels. Same treatment as 62443: identifiers only. |

**Net position for the corpus:** the "never actuate customer physical infrastructure without
explicit customer-side confirmation" absolute is **well-founded but externally under-supported**.
Cite **OSHA §1910.147** (public domain) as the concrete harm anchor, **IEC 62443 SR 3.x** as
factor vocabulary (identifier only), and note the **EU Machinery Regulation from 2027** as a
forward-looking hook. Do not claim any of these mandates the confirmation step — none does.

---

## Part 5 — PII scrubbing tooling with test data

### 5.1 Microsoft Presidio

| | |
|---|---|
| **Name / URL** | Presidio — https://github.com/microsoft/presidio ; docs https://microsoft.github.io/presidio/ |
| **Licence** | **VERIFIED MIT** ("The MIT License (MIT)", Copyright Presidio Contributors) — read from the repo LICENSE. |
| **Contents** | `presidio-analyzer` (pattern + NER + checksum recognisers for ~40 entity types incl. `CREDIT_CARD` with Luhn validation, `US_SSN`, `EMAIL_ADDRESS`, `IP_ADDRESS`, `IBAN_CODE`, `PHONE_NUMBER`, `MEDICAL_LICENSE`, `UK_NHS`), `presidio-anonymizer` (replace/redact/mask/hash/encrypt operators), image and structured-data redaction. |
| **Reuse** | **Oracle.** A conformance test can assert "after the change, no `CREDIT_CARD` or `US_SSN` entity survives into the retained log store" and run Presidio as the checker. MIT permits this in a redistributable corpus. |

### 5.2 presidio-research (evaluation)

| | |
|---|---|
| **URL** | https://github.com/microsoft/presidio-research |
| **Licence** | **VERIFIED MIT.** |
| **Contents** | **A synthetic data *generator*, not a shipped labelled corpus.** It builds sentences from templates (`My name is {{name}}`) populated with fake PII, tokenises them, and emits IO/BIO/BILUO tags plus spans — so ground truth is generated, by construction. Also provides `Evaluator`/`ModelError` machinery and precision/recall/F-per-entity scoring, and notebooks for evaluating the Presidio analyzer and spaCy/Flair/transformer models. |
| **Important caveat (VERIFIED)** | Identities come from **Fake Name Generator**, whose data is under **CC BY-SA 3.0 US**. Share-Alike is a *viral* licence — if generated datasets are treated as derivatives of that identity list, redistributing them could pull a share-alike obligation onto that portion of the corpus. **Recommendation: generate PII fixtures from your own name/address lists rather than redistributing FNG-derived data, or isolate any FNG-derived fixture in a clearly-licensed subdirectory.** This is a real, easily-missed licensing trap. |

### 5.3 OpenTelemetry redaction processor

| | |
|---|---|
| **URL** | https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/redactionprocessor |
| **Licence** | opentelemetry-collector-contrib is **Apache-2.0** (repo-level; consistent with all OTel projects). **Verified at repo level by convention, not by reading LICENSE in this survey — treat as VERIFIED-by-strong-inference, confirm before shipping.** |
| **Contents (VERIFIED from README)** | Deletes span/log/metric attributes not on an allow-list and masks values matching a block-list. Config keys: `allow_all_keys`, `allowed_keys`, `ignored_keys`, `ignored_key_patterns`, `blocked_values` (regex), `blocked_key_patterns` (regex), `allowed_values`, `hash_function` (`md5`, `sha1`, `sha3`, `hmac-sha256`, `hmac-sha512`), `redact_all_types`, `summary` (`debug`/`info`/`silent` — emits an audit trail of what was redacted), `url_sanitizer`, `db_sanitizer` (SQL, Redis, MongoDB and others). **Stability: Beta for traces; Alpha for logs and metrics.** |
| **Reuse** | **Both factor vocabulary and oracle.** The Alpha-for-logs stability level is itself corpus-relevant: a change that puts an Alpha component on the *only* path that removes PII from customer logs is a legitimate finding, and a good discriminating scenario. The `summary` audit trail is the mechanism by which redaction becomes *evidenced* rather than merely claimed — worth a provision. |

### 5.4 gitleaks-style detectors for logs

| | |
|---|---|
| **URL** | https://github.com/gitleaks/gitleaks |
| **Licence** | **VERIFIED MIT**, Copyright (c) 2019 Zachary Rice. |
| **Contents** | ~170+ TOML-defined rules with regexes, entropy thresholds, keyword pre-filters and allowlists, for cloud keys, tokens, private keys, and provider-specific credentials. Designed for git history but `gitleaks dir`/`gitleaks stdin` scan arbitrary content. |
| **Reuse** | **Oracle** for the *secrets* half of log hygiene (which is distinct from the PII half — Presidio does not detect API keys well, gitleaks does not detect names/SSNs). A serious log-scrubbing provision needs both. The rule TOML files are directly reusable as **factor vocabulary** under MIT. |

### 5.5 Labelled log corpus with PII ground truth

**Finding: no suitable public corpus exists. This is a genuine gap.**

- **LogHub / logpai** (https://github.com/logpai/loghub) — 23 datasets (HDFS, Hadoop, Spark,
  Zookeeper, OpenStack, BGL, HPC, Thunderbird, Windows, Linux, Mac, Android, HealthApp, Apache,
  OpenSSH, Proxifier), 2.25 MiB to 29.6 GiB. **Terms (VERIFIED from the repo): "freely available for
  research or academic work", with a requirement to reference the repo and cite the papers. That is
  NOT an open licence and NOT clearly commercial-use-safe** — a conformance corpus intended for
  broad redistribution should not vendor LogHub data without checking each dataset's own upstream
  terms. LogHub 2.0 / LogPub adds log-parsing ground truth (event templates).
- **Critically: LogHub states the logs are NOT sanitised or anonymised, and it provides NO PII
  labelling.** Its ground truth is *log-template* ground truth, for parser evaluation — a different
  task entirely.
- **Recommendation:** build a small **synthetic** labelled log corpus for the pack: take real log
  *formats* (syslog/RFC5424, JSON structured logs, nginx/Apache access logs, k8s events, IPMI/BMC
  and Redfish sensor logs, badge-reader CSV) and inject PII/PHI/PAN at known offsets from your own
  generator, so ground truth is exact and the licence is yours. Validate the generator against
  Presidio + gitleaks. This is the only path that yields a redistributable, exactly-labelled oracle.

---

## Part 6 — Agent overhead benchmarking: how a "<1% CPU" claim is actually verified

**Headline finding: there is no vendor-neutral, standardised benchmark for observability-agent
overhead. A bare "<1% CPU" claim is not falsifiable as stated, and the corpus should treat it as
an *unverifiable* claim unless five parameters are pinned.** No CNCF or other neutral body publishes
an overhead benchmark specification; searches for "CNCF observability overhead study" returned only
vendor blogs and non-peer-reviewed marketing comparisons. **Status: no such neutral study located —
report as a gap, not as a source.**

### 6.1 What a defensible "<1% CPU" claim must specify

A claim is only checkable if it states all five of:
1. **Denominator** — 1% of what? One core, or the whole host? On a 128-core host these differ by 128x.
   `cgroup` accounting measures CPU-seconds; converting to a percentage requires a stated core count.
2. **Workload** — telemetry ingest rate (spans/sec, log lines/sec, metric datapoints/sec),
   cardinality, and payload size. Overhead is roughly linear in throughput.
3. **Configuration** — which processors are enabled. Redaction with regex `blocked_values` is
   dramatically more expensive than passthrough. Batch size and compression matter.
4. **Measurement window and statistic** — mean over 10 minutes at steady state, or p99 over a burst?
   Agents are bursty; means hide the spikes that actually cause customer incidents.
5. **Measurement mechanism** — see below.

### 6.2 Measurement mechanisms (all freely usable)

| Mechanism | Source / licence | What it gives you |
|---|---|---|
| **cgroup v2 `cpu.stat`** | Linux kernel (GPL-2.0 for the kernel; the *interface* is not licensable). Documented at https://docs.kernel.org/admin-guide/cgroup-v2.html | `usage_usec`, `user_usec`, `system_usec`, plus `nr_throttled`/`throttled_usec` under a quota. **This is the authoritative denominator-free measurement** — CPU-microseconds attributed to the agent's cgroup by the kernel, not sampled. Delta over a wall-clock window ÷ (window × cores) = the percentage. **The `throttled_usec` counter is the one that matters most for a monitoring agent: an agent that is being CPU-throttled is silently dropping or delaying telemetry, which is a monitoring-integrity failure, not just a performance one.** |
| **`bpftop`** | https://github.com/Netflix/bpftop — **VERIFIED Apache-2.0** | For agents with an eBPF data path. **VERIFIED mechanism:** uses the `BPF_ENABLE_STATS` bpf syscall command to turn on global eBPF runtime statistics (off by default precisely because collecting them costs something), samples every second, and reports average runtime, events/sec and **estimated CPU utilisation per eBPF program**; disables stats on exit by closing the returned fd. This is the right tool to answer "how much CPU does the kernel-side probe cost", which `cgroup` accounting **does not** capture — eBPF program time is charged to whatever process triggered the probe, not to the agent. **This is the single most common way a "<1% CPU" claim is wrong: the eBPF cost is real but invisible in the agent's own cgroup.** |
| **`/proc/[pid]/stat` utime/stime, `getrusage`** | kernel interfaces | Per-process; cruder than cgroup, misses child processes unless summed. |
| **`perf stat`, `pidstat`** | perf is in-tree (GPL-2.0); sysstat is GPL | Sampling profilers; good for attribution, weaker as a total-cost oracle than cgroup counters. |

### 6.3 OpenTelemetry Collector — the closest thing to a published, reusable methodology

| | |
|---|---|
| **Name / URL** | OpenTelemetry Collector benchmarks — https://opentelemetry.io/docs/collector/benchmarks/ ; harness source: `testbed/` in https://github.com/open-telemetry/opentelemetry-collector-contrib |
| **Licence** | Apache-2.0 (OTel project-wide). Docs under CC BY 4.0 per CNCF convention — **CC BY status UNVERIFIED in this survey.** |
| **Contents (VERIFIED from the testbed README)** | A controlled end-to-end harness for reproducible benchmarks, correctness validation, stability assessment and stress testing. Architecture: a **`LoadGenerator`** = `DataProvider` (synthetic data) + `DataSender` (transport), and a **`MockBackend`** = `DataReceiver` + validation. Results flow through `PerfTestValidator`/`PerformanceResults` and `CorrectnessTestValidator`/`CorrectnessResults`, aggregated into a `TestResultsSummary`. |
| **The key reusable idea** | **`ResourceSpec` with `ExpectedMaxCPU` and `ExpectedMaxRAM`** — the harness makes a resource budget a **declarative, asserted pass/fail property of a test**, not a marketing number. Tests fail when a component exceeds its stated CPU/RAM ceiling under a stated load. |
| **How to reuse** | **This is the model the DCVigil pack should adopt for its overhead provisions, and it is the strongest oracle in this section.** A provision should not say "agent CPU overhead must be <1%"; it should say "the agent's declared `ExpectedMaxCPU` under the pack's reference load profile must not be exceeded, measured by cgroup v2 `cpu.stat` delta over a 10-minute steady-state window, with eBPF program time measured separately via `BPF_ENABLE_STATS`". That is falsifiable. The OTel testbed can be cited as prior art for the pattern (Apache-2.0, freely reusable) and `telemetrygen` is the standard load generator. |
| **Caveat (VERIFIED)** | The published benchmarks page does **not** state hardware specs or a full methodology inline — it defers to the repository. So the *published numbers* are not directly comparable across runs; only the *harness pattern* is reusable. Do not cite OTel's published CPU figures as an industry baseline. |

### 6.4 Kernel-panic regression practice across kernel versions

Highly relevant: a monitoring agent with an eBPF or kernel-module data path can panic a host, and
"it works on my kernel" is the classic failure mode for datacenter agents shipped across a fleet
with heterogeneous kernels.

| Source | URL | Licence | Reuse |
|---|---|---|---|
| **KernelCI** (Linux Foundation project) | https://docs.kernelci.org/ | Project code open source; **specific licence UNVERIFIED** | The reference model for **build-and-boot testing a change across many kernel trees, versions, architectures and real hardware**, with automatic bisection of regressions. **Reuse as factor vocabulary and as the justificatory prior art** for a provision requiring multi-kernel-version validation before fleet rollout. |
| **Linux Test Project (LTP)** | https://github.com/linux-test-project/ltp | GPL-2.0 (project convention; **UNVERIFIED in this survey**) | Thousands of syscall/stress/regression tests. Reuse as an **oracle** for "the agent does not destabilise the host under kernel stress". |
| **kselftest** | https://docs.kernel.org/dev-tools/kselftest.html | In-tree, GPL-2.0 | In-kernel developer regression suite; `make kselftest`. Reuse as oracle. |
| **syzkaller** | https://github.com/google/syzkaller | Apache-2.0 (**UNVERIFIED in this survey**) | Coverage-guided kernel fuzzer; the standard tool for finding panics/UAFs reachable from userspace, including through eBPF verifier and helper surfaces. Reuse as an oracle for "the agent's kernel-facing surface does not crash the host". |
| **Kernel Testing Guide** | https://docs.kernel.org/dev-tools/testing-overview.html | GPL-2.0 / kernel docs | Overview of KUnit, kselftest, KASAN/UBSAN/KCSAN, and the 0-Day/kernel test robot pipeline. Good source for **factor vocabulary** on what "adequately tested against a kernel" means. |

**Recommended provision shape:** a change to an agent component with a kernel-facing data path
(eBPF program, kernel module, or a dependency on a kernel interface) must be validated by
boot-and-smoke across the **declared supported kernel matrix**, with the matrix itself declared and
version-pinned, before any fleet rollout. KernelCI is the citable prior art for the pattern.

---

## Part 7 — Recommendation: which obligations should be ABSOLUTE

### 7.1 Assessment of the seven existing absolutes

| # | Existing absolute | Verdict | Reasoning |
|---|---|---|---|
| 1 | **Automated remediation may never actuate customer physical infrastructure without explicit customer-side confirmation** | **KEEP — strongest absolute in the pack** | Irreversible physical harm; can injure people; crosses a tenancy boundary. Externally under-supported (see Part 4) but defensible via OSHA §1910.147 (public domain). **Fix the rationale:** cite LOTO, not a nonexistent "datacenter actuation standard." **Tighten the scope:** "actuate" must be defined to include power, cooling, fire/EPO, and door/access control — door release is actuation of physical infrastructure and is currently ambiguous. |
| 2 | **Tenant isolation** | **KEEP — the load-bearing absolute** | Multi-tenancy is the platform's defining risk. A cross-tenant leak is unrecoverable, breaches every customer DPA simultaneously, and is a GDPR Art. 32(1)(b) failure plus a SOC 2 CC6.1/CC6.6 failure. No plausible business justification for an exception. |
| 3 | **EU telemetry residency** | **KEEP, but FIX THE RATIONALE** | Correct as an absolute — but it is a **contractual** absolute, not a GDPR one. GDPR requires a transfer *mechanism*, not EU storage. If the provision's justification says "required by GDPR", that is wrong and a reviewer will catch it. Restate as: customer contractual commitment, with GDPR Chapter V as the fallback constraint on any transfer. |
| 4 | **Security-audit-log immutability with 7-year retention** | **KEEP the immutability; SPLIT OFF the retention period** | **Immutability** is well-grounded (NIST AU-9 / AU-9(3), CC0, verbatim citable) and is a genuine absolute — a system that can silently rewrite its own audit trail cannot be audited at all. **7 years is not traceable to any binding instrument** (Part 1.3): PCI says 12 months, HIPAA says 6 years for *documentation*, NIST and FedRAMP leave it open, SOC 2 sets none. Recommendation: **immutability = Tier 1 absolute; the specific 7-year figure = Tier 1 as a contractual commitment with an honest rationale, or Tier 2 with a PCI-derived 12-month hard floor.** Do not let the pack assert a regulatory basis it does not have. |
| 5 | **EU AI Act Art. 5(1)(b) — vulnerability exploitation** | **KEEP but DOWNGRADE PRIORITY / question the fit** | It is genuinely a prohibition (in application since 2 Feb 2025) so it *belongs* at absolute tier legally. But the **domain fit is weak**: it is hard to construct a realistic datacenter-monitoring scenario in which an agent exploits age/disability/socio-economic vulnerability to distort behaviour causing significant harm. The nearest real case is the customer-facing AI assistant using dark patterns on a distressed on-call engineer, which is a stretch. **Risk: this provision will never fire, adding noise without discriminating power.** Keep it for legal completeness but expect near-zero scenario coverage — and consider whether **Art. 5(1)(a)** (subliminal/manipulative techniques) would not serve the same completeness role more plausibly. |
| 6 | **EU AI Act Art. 5(1)(e) — untargeted facial scraping** | **KEEP — excellent fit** | Directly on point: the platform holds facility CCTV. Prohibition in application. Near-binary and therefore a clean oracle. |
| 7 | **GDPR Art. 7(3) — consent withdrawal** | **KEEP, but check it is the right hook** | Correct as an absolute where consent is the lawful basis. **However:** for a *processor* handling *customer* telemetry, the lawful basis is usually the customer-controller's, and it is usually legitimate interests or contract, **not consent**. Where consent genuinely applies here is **employee biometric badge enrolment and CCTV** — and in the employment context, EDPB/WP29 guidance is that consent is rarely freely given. **Recommendation: keep Art. 7(3), and pair it with Art. 17 (erasure) and Art. 9 (special categories), which are the provisions that will actually fire in this domain.** As written, Art. 7(3) alone may under-cover. |

**Overall verdict on the seven: six are right, one (Art. 5(1)(b)) is legally correct but a poor
domain fit, and three (residency, 7-year retention, Art. 7(3)) have rationales that need repair
even though the provisions themselves should stay.**

### 7.2 What is MISSING from Tier 1

Three gaps, in priority order:

1. **EU AI Act Art. 5(1)(f) — emotion inference in the workplace.** This is a striking omission.
   The pack includes 5(1)(b) (poor fit) and 5(1)(e) (good fit) but **not 5(1)(f), which is the
   best fit of the three.** A datacenter is a workplace; the platform has CCTV; staff-affect
   analytics on that footage is *prohibited outright*, in application since Feb 2025, with only a
   narrow medical/safety carve-out. It is at least as absolute as 5(1)(e) and far more likely to
   arise. **Recommendation: add to Tier 1.**
2. **Biometric badge template collection without prior written notice, purpose/term disclosure, and
   a written release (Illinois BIPA §15(b)), plus the §15(a) destruction schedule.** BIPA carries a
   **private right of action** with statutory damages ($1,000 / $5,000 per person) and fee-shifting
   — the only instrument in this entire survey that creates direct, uninsurable-scale liability from
   a single engineering decision. Enrolling a biometric template without a §15(b) release is not
   remediable after the fact. **Recommendation: add to Tier 1.**
3. **Audit-log integrity alerting (NIST AU-9), as distinct from immutability.** Immutability without
   detection is incomplete: AU-9 requires *both* protection from modification *and* an alert on
   detected unauthorised modification/deletion. A change that disables the tamper alert while
   leaving storage nominally immutable would pass the current absolute. **Recommendation: fold into
   absolute #4 rather than adding a separate provision.**

**Considered and rejected for Tier 1:** NIS2 Art. 23 (transposition varies too much for a hard
clock — Tier 2); GDPR Art. 33 72h (a *controller* duty; the vendor is usually a processor under
33(2) — Tier 2); EU Data Act switching (commercial, reversible — Tier 3); FedRAMP (scope-conditional
— Tier 3); ISO 27001 / SOC 2 criteria (not directly citable, and they are audit frameworks rather
than substantive prohibitions — they should tag Tier-2 provisions, not be provisions).

### 7.3 The three tiers

**TIER 1 — ABSOLUTE. Never satisfiable by a business justification; an agent proposing these must
refuse. Characterised by: irreversible harm, an outright legal prohibition, or a cross-boundary
breach that cannot be undone.**

1. No actuation of customer physical infrastructure (power, cooling, fire/EPO, physical access
   control) without explicit customer-side confirmation. *[OSHA 29 CFR §1910.147; IEC 62443 SR 3.x
   as vocabulary]*
2. Tenant isolation — no code path may allow one tenant's telemetry, credentials, or derived data
   to reach another. *[GDPR Art. 32(1)(b); NIST SC-4, AC-4; SOC 2 CC6.1/CC6.6 as tags]*
3. EU telemetry residency per the customer commitment; no transfer outside the committed region
   absent a valid GDPR Chapter V mechanism. *[contractual + GDPR Arts. 44–49, Decision 2021/914]*
4. Security audit log immutability **and** tamper-detection alerting; retention per the published
   commitment, with a hard floor of 12 months where CHD is in scope.
   *[NIST AU-9, AU-9(3), AU-11 (verbatim, CC0); PCI DSS 10.3.2, 10.5.1 as floor]*
5. EU AI Act **Art. 5(1)(e)** — no creation or expansion of facial recognition databases by
   untargeted scraping of facility CCTV. *[Reg. (EU) 2024/1689, in application since 2025-02-02]*
6. **[ADD]** EU AI Act **Art. 5(1)(f)** — no inference of emotions of natural persons in the
   workplace from facility CCTV or any other source, outside the narrow medical/safety exception.
7. **[ADD]** No collection or storage of biometric identifiers/templates (badge, face) without prior
   written notice of the fact, the specific purpose and the term, plus a written release; and a
   published retention/destruction schedule capped at 3 years from last interaction.
   *[740 ILCS 14/15(a), 15(b); GDPR Art. 9(1)]*
8. GDPR **Art. 7(3)** consent withdrawal must be honoured and be as easy as giving consent, with
   downstream deletion propagated. *[pair with Art. 17 and Art. 9]*
9. EU AI Act **Art. 5(1)(b)** vulnerability exploitation. *[retain for legal completeness; expect
   low scenario yield]*

**TIER 2 — STRONG DEFAULT. Overridable only by a documented, named-approver, time-bounded exception
that is itself logged to the immutable audit trail. Characterised by: real legal duty, but
jurisdiction-dependent, deadline-shaped, or remediable.**

- Incident reporting clocks: GDPR Art. 33(2) (processor → controller, without undue delay);
  GDPR Art. 33(1) 72h where acting as controller; **the applicable national transposition of NIS2
  Art. 23** (24h early warning / 72h notification / 1-month final report) — phrased against national
  law, not the Directive directly.
- EU AI Act **Art. 50(1)** — the customer-facing AI assistant must disclose that it is an AI system.
  *(in application since 2026-08-02)*
- PII/PHI/PAN must not reach durable storage un-redacted; redaction must be evidenced (an audit
  trail of what was redacted, per the OTel redaction processor `summary` pattern), and the
  redaction path may not depend solely on an Alpha-stability component.
  *[PCI DSS Req. 3 and 10.2.2; GDPR Art. 5(1)(c), Art. 32(1)(a)]*
- MFA on all privileged access to the telemetry plane; TLS with cryptographic integrity protection
  on all telemetry in transit. *[NIST IA-2(1), IA-2(2), SC-8, SC-8(1) — verbatim, CC0]*
- Change validation across the declared supported kernel matrix for any kernel-facing agent
  component, before fleet rollout. *[KernelCI/LTP/syzkaller as prior art]*
- Declared agent resource budget (`ExpectedMaxCPU`/`ExpectedMaxRAM`-style) asserted under a stated
  reference load, measured by cgroup v2 `cpu.stat` with eBPF program time accounted separately via
  `BPF_ENABLE_STATS`; `throttled_usec` > 0 treated as a monitoring-integrity failure, not merely a
  performance one. *[OTel Collector testbed as prior art, Apache-2.0]*
- CCPA/CPRA sensitive-personal-information limits on employee/contractor badge and biometric data.
- Storage limitation: GDPR Art. 5(1)(e) reconciliation between the retention commitment and
  personal data in telemetry.

**TIER 3 — REQUIRES JUSTIFICATION. The agent may proceed with a recorded rationale; these generate
review findings rather than blocks. Characterised by: commercial, framework-tagging, or
scope-conditional duties.**

- EU Data Act Chapter VI switching duties: export completeness, 30-day transitional and 30-day
  retrieval windows, and zero switching charges from 12 January 2027.
- FedRAMP ConMon obligations (monthly scanning, POA&M, significant-change process) — applicable only
  in a federal-scoped deployment.
- SOC 2 TSC and ISO/IEC 27001 Annex A control tagging (CC8.1 change management, CC7.2 monitoring,
  A.8.15 logging, A.8.16 monitoring, A.7.4 physical security monitoring) — used as **traceability
  labels on other provisions**, never as provision text, because neither is redistributable.
- ASHRAE thermal envelope and Uptime Institute Tier vocabulary — descriptive scenario framing only;
  neither is legally binding and neither is redistributable.
- EU Machinery Regulation (EU) 2023/1230 from 20 January 2027 — flag as an emerging obligation whose
  applicability to actuation software is genuinely unsettled.

---

## Appendix — Licence status summary

| Source | Status | Confidence |
|---|---|---|
| EUR-Lex texts (GDPR, NIS2, AI Act, Data Act, Machinery Reg., SCC Decision 2021/914) | Reusable, Decision 2011/833/EU | VERIFIED (baseline) |
| NIST SP 800-53 Rev. 5 control text via `usnistgov/oscal-content` | Public domain + CC0 1.0 | **VERIFIED** (read LICENSE.md) |
| US CFR (29 CFR 1910.147, 45 CFR 164.316, 17 CFR 240.17a-4) | Public domain, 17 U.S.C. §105 | VERIFIED (baseline) |
| Illinois 740 ILCS 14 (BIPA) | State statute, freely quotable | VERIFIED (text read) |
| California CCPA/CPRA + CPPA regs | Edict of government; no formal open licence located | Partly UNVERIFIED |
| Microsoft Presidio | **MIT** | **VERIFIED** (read LICENSE) |
| microsoft/presidio-research | **MIT**; but FNG identity data is **CC BY-SA 3.0 US** — share-alike trap | **VERIFIED** |
| gitleaks | **MIT**, © 2019 Zachary Rice | **VERIFIED** (read LICENSE) |
| Netflix/bpftop | **Apache-2.0** | **VERIFIED** |
| opentelemetry-collector-contrib (redactionprocessor, testbed) | Apache-2.0 by project convention | VERIFIED-by-inference; confirm LICENSE |
| OTel docs / benchmarks pages | CC BY 4.0 assumed (CNCF convention) | **UNVERIFIED** |
| GSA/fedramp-automation repo | US Gov work presumed; repo LICENSE not retrievable | **UNVERIFIED** |
| AICPA Trust Services Criteria | Free-of-charge but **account-gated**; AICPA © ; **no reuse grant** | **VERIFIED — not redistributable** |
| ISO/IEC 27001:2022 / 27002:2022 | **Paywalled, CHF 155**; ISO prohibits AI-training use | **VERIFIED — not redistributable** |
| PCI DSS v4.0.1 | Free download under a **personal, non-commercial, no-redistribution** licence | **VERIFIED — not redistributable** |
| IEC 62443-3-3:2013 | **Paywalled, CHF 380** | **VERIFIED — not redistributable** |
| ASHRAE Thermal Guidelines 5th ed. | Commercial book, no free full text | **VERIFIED — not redistributable** |
| Uptime Institute Tier Standard: Topology | Registration-gated; PDF terms not retrievable (robots.txt) | **UNVERIFIED** |
| NFPA 70/70E/75/76 | Registration-gated read-only "free access"; scope & copy terms unconfirmed | **UNVERIFIED** |
| logpai/loghub | "freely available for research or academic work" — **not an open licence**; no PII labels | **VERIFIED as restrictive** |
| KernelCI / LTP / syzkaller | Open source, specific licences not read | **UNVERIFIED** |
| CNCF vendor-neutral observability overhead study | **Does not appear to exist** | Searched; not found |
| EU–US Data Privacy Framework current status | Not checked | **UNVERIFIED** |
| Seventh Circuit retroactivity of BIPA P.A. 103-0769 | Reported but not verified as current | **UNVERIFIED** |
