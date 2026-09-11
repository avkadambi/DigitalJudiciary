# Sources: what was reusable, what was not, and why

Four independent surveys were run before a line of this corpus was written — financial regulation and its primary instruments, financial-correctness conformance suites and oracles, fintech application security and fraud tooling, and model risk plus fair lending. The full reports are in `research/`. This document is the decision record.

Every licence below was verified by reading the repository's own `LICENSE` file or the primary terms page. Where verification failed, the row says so. **A licence we could not verify is treated as reference-only.**

Meridian differs from the other four packs in one way that shapes everything here. Its thirty-seven shipped provisions cite real instruments, so the surveys were not only looking for reusable data — they were checking whether the constitution was still true. Six times, it was not.

---

## 1. The seven findings that shaped this corpus

**SR 11-7 was superseded on 17 April 2026.** SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026 replaced it. Two consequences cut in opposite directions: the replacement **expressly excludes generative and agentic AI from the definition of a model**, which leaves MF-307 — the agent-provenance provision — anchored on an instrument that disclaims its subject matter; and it states that it sets no enforceable standards, so a provision that reads as a restatement of supervisory requirement is now a firm control wearing a supervisor's name. The shipped section pins are separately wrong: model use is §IV, validation §V, inventory §VI. Five provisions rest on it and two more cite it in support. That is draft amendment **PA-01**, and it is the most consequential thing these surveys produced.

**CFPB Circulars 2022-03 and 2023-03 were withdrawn on 12 May 2025** (90 FR, Doc. 2025-08286). MF-110 and MF-305 both cite them. The duty survives — it is statutory, at 15 U.S.C. §1691(d) and 12 CFR §1002.9(b)(2) — but citing withdrawn guidance for a live obligation is the worst of both positions: it invites a contest that the rule is gone when the rule is not. **PA-02**.

**Reg B lost the effects test.** 91 FR 21620, effective 21 July 2026, amended 12 CFR §1002.6(a) to remove it. The amendment is under APA challenge; no injunction has been sought, so it is in force. Disparate treatment and the prohibition on proxies for a prohibited basis are statutory and untouched. The drafting consequence is sharp and this corpus takes it: **proxy detection is absolute (MF-510); outcome parity is a documented, time-boxed firm control (MF-562)**. **PA-03**.

**12 CFR Part 1033 is enjoined, not vacated.** *Forcht Bank, N.A. v. CFPB*, E.D. Ky., 29 October 2025, and the rule is under CFPB reconsideration. An enjoined rule can be revived; a vacated one cannot. The shipped pack is right to give MF-405 a `readiness` status — the one place in the programme's demo material where that concept appears — and the statutory duty at 12 U.S.C. §5533 is what should be cited. **PA-04**.

**MF-103 is stricter than the rule it cites, and it is absolute.** 31 CFR §1020.220(a)(2)(ii) permits *verification* within a reasonable time after account opening; what must precede opening is the collection of identifying information. §1020.220(a)(2)(iii) supplies an explicit procedure for when identity cannot be verified. As drafted, "no account opened, funded, or raised in limit before CIP completes" will flag conforming behaviour — and because the provision is absolute, that flag cannot be risk-accepted by anyone at any tier. This is the single most likely source of false denials in the shipped constitution. **PA-07**, and the one most tempting to fix in place, which is exactly why it was not.

**Two citation defects, small and worth filing anyway.** NYDFS compensating controls are at **§500.12(b)**; §500.12(a) is the universal MFA requirement itself, in force since 1 November 2025 — so MF-202 as cited points at the obligation and calls it the exception (**PA-05**). And **18 U.S.C. §1510(b) does not reach SARs**; the tipping-off exposure runs through 31 U.S.C. §5318(g)(2) with the penalty at §5322, and 31 CFR §1020.320(e)(1) (**PA-06**).

**Seven missing floors, ranked.** The surveys ranked what a fintech constitution with eleven absolutes still lacks: M1 secrets hard-coded or logged; M2 change control itself; M3 regulatory notification clocks (DORA 4h/24h/72h under RTS (EU) 2025/301, NYDFS 72h, SEC Form 8-K Item 1.05, FTC Safeguards 30 days); M4 blocked-property reporting under 31 CFR §§501.603–604; M5 FCRA furnisher accuracy at §1681s-2(a)(1); M6 ledger immutability as distinct from segregation of duties; M7 the Reg Z §1026.13 billing-error clocks — the credit-side twin of the Reg E clocks MF-109 already protects, whose absence is an asymmetry defect rather than an omission. All seven are added, as MF-501 to MF-507.

---

## 2. What this corpus actually reuses

Nothing is redistributed. What was reused is **structure**, **identifiers** and **regulatory text that is in the public domain**, which are facts.

| Source | Licence (verified) | How it is used here |
| :---- | :---- | :---- |
| US CFR, USC, Federal Register | Public domain, 17 U.S.C. §105 | The FC, PD, CP, EV and FL families take provision text directly. Every absolute in this pack traces to one. |
| EU law via EUR-Lex — GDPR, DORA 2022/2554 and RTS (EU) 2025/301, AI Act 2024/1689, the AI Omnibus | CC BY 4.0 via Decision 2011/833/EU | The DP, RE and AI families; the shipped MF-105, MF-107, MF-303, MF-304 block. |
| **OFAC** SDN and consolidated list files | Public domain by §105 inference — **verified absence** of any terms-of-use, copyright or redistribution statement on the SLS landing page, the sanctions-list index and the ASDM FAQ | The FC family's screening vocabulary. Cite as courtesy, not obligation. |
| **UK OFSI** consolidated list | **Open Government Licence v3.0** — stated on the data.gov.uk record | The most explicitly and permissively licensed sanctions list of the three. |
| EU FSF list | 2011/833 baseline, `[UNVERIFIED]` — no explicit notice on the FSF pages | Fetch from `webgate.ec.europa.eu`. **Not** from OpenSanctions, whose redistribution is CC-BY-NC 4.0 with a commercial-licence condition. |
| **SEC EDGAR** | **Explicit permission** — "considered public information and may be copied or further distributed by users of the web site without the SEC's permission" | The strongest grant of any source surveyed. Access conditions apply (declared User-Agent, ≤10 req/s) but they are access terms, not licence terms. |
| **Anthropic, Claude's Constitution** (January 2026) | **CC0**, verified at `anthropics/claude-constitution` | The oversight anchor for MF-111, MF-306, MF-511 and MF-572 — the shipped pack's own choice, and the only instrument in this constitution that speaks to agent oversight since SR 11-7 disclaimed it. |
| **FATF** typologies and Recommendation 16 | CC BY 4.0 | MF-521's labelled matching set; MF-524's travel-rule fields. |
| **ISO 20022** message definitions | Royalty-free grant in the IPR Policy; **replications must be marked "unofficial copy"** | Message identifiers (`pacs.008`, `camt.053`, …) cited as identifiers only. No schema is replicated, so the marking condition is not engaged. |
| **CLDR** currency data | Unicode Licence v3 | MF-551's minor-unit reference data. Used *instead of* ISO 4217, whose code-list terms could not be established. |
| **rust_decimal** conformance vectors | **MIT** (LICENSE read) | The oracle behind MF-549 and MF-553. 3,430,315 rows with an explicit `Error` disposition column — the largest labelled decimal-arithmetic set with a usable licence. |
| **JSR-354 TCK** | **Apache-2.0** (LICENSE.txt: "Copyright 2012, 2015, Werner Keil, Credit Suisse (Anatole Tresch)") | MF-550's rounding oracle. 245 `@SpecAssertion` annotations, each naming the specification clause it tests — the closest existing analogue to this corpus's own case shape. |
| **PostgreSQL isolation tests** | PostgreSQL Licence | MF-545. 134 specs over 2,768 permutations, each with a declared isolation level and expected outcome. |
| **Hermitage** | **CC BY 4.0** | MF-546. 250 labelled verdict cells across eight anomalies and six engines. |
| **TigerBeetle** status enums | Apache-2.0 | MF-544 and MF-547. 98 named result codes — a double-entry ledger's own taxonomy of what can go wrong, which is a factor vocabulary already. |
| **AMLSim** | Apache-2.0 | The FC family's transaction-pattern vocabulary. |
| **IBM AMLworld** synthetic AML data | CDLA-Sharing-1.0 | Alert-pattern vocabulary. Share-alike, so used as reference rather than vendored. |
| **Sparkov** synthetic card fraud | CC0 | Fraud-scenario vocabulary. |
| **ULB** credit-card fraud dataset | ODbL + DbCL | Reference only; the share-alike terms are incompatible with this pack's CC BY 4.0 data licence. |
| **web-platform-tests** SRI, CSP and WebAuthn subtrees | BSD-3-Clause | MF-527's payment-page script-integrity vocabulary. |
| **Akto** tests-library; **gitleaks** | MIT; MIT | The SS family's secret-pattern vocabulary and MF-501's detector rules. |
| **Fairlearn**; **AIF360**; **Folktables** | MIT; Apache-2.0; MIT | MF-562's parity metrics. Folktables matters specifically because it is the dataset built to replace the flawed UCI Adult benchmark. |
| **NIST SP 800-53** via `usnistgov/oscal-content`; SP 800-52, 800-57, 800-131A, 800-218 | **CC0** / public domain | MF-513, MF-530, MF-531, MF-532, MF-534, MF-576, MF-578. |
| **SLSA v1.0** (OpenSSF) | CC BY 4.0 | MF-535. |
| **SPDX** licence identifiers | CC0 | MF-538. |
| **17 CFR 240.17a-4(f)** | Public domain | MF-512 — the one records-retention duty in this domain with a legally precise storage predicate rather than a period. |
| FFIEC handbooks and IT WorkPrograms | Public domain, no licence encumbrance | The RE and CQ families' factor vocabulary. The examiner checklists are oracle-shaped: they are US regulators' own articulation of what a controlled change looks like. |
| CFPB Consumer Complaint Database | Public domain by §105 inference; no formal statement | The CP family's complaint-handling vocabulary. Note the CFPB's own disclaimers: complaints are not verified before publication and are not a statistical sample. |
| PACT (Okamoto and Erol 2026), Table 14 | cited | The nine pressure mechanisms in the P-pressure category. |

---

## 3. What was deliberately not used

| Source | Why not |
| :---- | :---- |
| **FRED** (Federal Reserve Bank of St. Louis) | **Terms of Use forbid use in machine-learning training.** The public-domain carve-out for individual series does not displace the prohibition. Excluded outright — this is the clearest disqualification in the survey. |
| **NACHA Operating Rules** | "May not be reproduced, downloaded, disseminated, published, or transferred, in any form or by any means." Sold through the Nacha Store. ACH return codes are referred to by number; no rule text appears. |
| **IBM / Cowlishaw `decTest`** vectors | No OSI licence and no explicit redistribution grant in the file headers. CPython's own licence file carries no grant for them either; GCC relicensed the *code* but not the vectors. The schema is imitated; no file is vendored. |
| **Elliptic** bitcoin dataset | CC BY-NC-ND — non-commercial and no-derivatives, both fatal here. |
| **IEEE-CIS fraud** | Competition terms only. |
| **COMPAS** | No LICENSE file, and the benchmark's own documented flaws make it a poor fair-lending oracle regardless. |
| **Fannie Mae / Freddie Mac** loan performance data | Commercial-use restrictions. |
| **PaySim** simulator | GPL-3.0 — incompatible with an Apache-2.0 corpus intended for vendor reuse. |
| **Jube**, **k6** | AGPL. Same reason. |
| **PCI DSS v4.0.1** | Free download under a personal, non-commercial, no-redistribution licence. Requirement numbers and stated compliance dates are cited as facts; no requirement text appears anywhere in this repository. |
| **ISO/IEC 27001, 27002**; **ISO 4217** code-list files | Paywalled, or no licence statement published with the free code lists. Currency data comes from CLDR instead. |
| **SWIFT** standards documentation | Restricted to SWIFT users; the legal notice could not be read. The corpus frames payment scenarios in ISO 20022, which is the openly licensed path. |
| **Visa** and **Mastercard** operating rules | Publicly readable, no reuse grant stated; technical specifications are licensee-only. |
| **OWASP API Top 10** text | CC BY-SA. Identifiers only. |
| **AICPA Trust Services Criteria** | Account-gated, no reuse grant. SOC 2 criteria identifiers only. |
| FIDO tooling, PCI test tooling | Agreement-gated. Identifiers only. |

---

## 4. Two structural observations the surveys produced

**The best oracles in this domain are conformance suites, not datasets.** Fraud datasets are abundant and mostly unusable — non-commercial, competition-bound, or share-alike. Conformance suites are the opposite: `rust_decimal`'s 3.4 million labelled vectors, the JSR-354 TCK's 245 specification assertions, PostgreSQL's 2,768 isolation permutations and Hermitage's 250 verdict cells are all permissively licensed, all carry an expected result per row, and all test a property a provision can state. The precision and ledger families of this constitution are built on that observation.

**Public-domain regulation is the richest source of provision text anywhere in the programme.** The other four packs had to invent most of their constitutions because the governing standards were paywalled — ISO, IEC, ASHRAE, AICPA. In regulated finance the primary instruments are US Government works and EU documents under Decision 2011/833/EU, which means a provision can quote its source. That is what makes Meridian's constitution checkable, and it is also what makes it falsifiable: an invented rule cannot be superseded, and six of these were.
