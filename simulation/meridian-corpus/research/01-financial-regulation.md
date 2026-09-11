# 01 — Financial Regulation & Open Compliance Data (Fintech Lane)

**Research date:** 2026-09-05
**Scope:** Financial-crime, payments, consumer-protection and operational-resilience regulation, plus openly available financial compliance datasets, for an open compliance test corpus governing software change at a regulated fintech (card issuing/acquiring, ACH + wire, consumer lending, servicing, internal ledger inside the financial-reporting boundary).

**Baselines applied without re-derivation** (from prior surveys):
- US CFR / USC / NIST publications — public domain, 17 U.S.C. §105.
- EU legal texts (EUR-Lex) — reusable under Commission Decision 2011/833/EU (attribution; no alteration of meaning).
- `usnistgov/oscal-content` — CC0.
- **PCI DSS v4.0.1** — free download, *personal non-commercial licence, no redistribution*.
- AICPA Trust Services Criteria — account-gated, no reuse grant.
- ISO/IEC 27001 — paywalled; content prohibited for AI/ML training.

**Verification convention:** every licence statement below is marked `[VERIFIED]`, `[INFERRED — baseline]` (a US/EU government work covered by the baselines above, with no contrary notice found on the source page), or `[UNVERIFIED]`. Nothing is guessed.

---

## PART 1 — SANCTIONS AND FINANCIAL CRIME

### 1.1 OFAC Sanctions List Service (SLS) — the data files

**Name:** OFAC Sanctions List Service (SDN List and Non-SDN Consolidated Sanctions List)
**URLs:**
- Landing: https://ofac.treasury.gov/sanctions-list-service and https://ofac.treasury.gov/ofac-sanctions-lists
- App: https://sanctionslist.ofac.treas.gov/Home/SdnList , `/Home/ConsolidatedList` , `/Home/CustomizeSanctionsDataset` , `/Home/DeltaFileArchive`
- File endpoints (base `https://sanctionslistservice.ofac.treas.gov`):
  - `/api/PublicationPreview/exports/SDN.CSV`
  - `/api/PublicationPreview/exports/SDN.XML`
  - `/api/PublicationPreview/exports/SDN_ADVANCED.XML`
  - `/api/PublicationPreview/exports/CONS_PRIM.CSV`
  - `/api/PublicationPreview/exports/CONS_ADVANCED.XML`
  - `/api/download/{filename}`, `/api/changes/latest`, `/api/changes/history/{yyyy}/{mm}/{dd}` (delta files)

**Contents:** Blocked persons — individuals, entities, groups, vessels, aircraft — with programme tags, aliases, addresses, DOB/POB, government IDs, vessel/aircraft identifiers. The Consolidated (non-SDN) list carries SSI (Sectoral Sanctions), FSE, NS-MBS, PLC, CAPTA and related non-blocking lists in separate files.

**Format:** Legacy flat files (CSV, fixed-width, legacy XML) **and** the Advanced Sanctions Data Model (ASDM) XML (`SDN_ADVANCED.XML`, `CONS_ADVANCED.XML`). ASDM was designed for a global user base: multi-language/multi-charset names, granular name-part identification for non-Western names, and a distinction between legitimate and fraudulent government-issued IDs. Legacy CSV and fixed-width remain in production alongside ASDM. Delta files are published for incremental sync. **Note:** no XSD/JSON variant of the ASDM was confirmed on OFAC's FAQ page; XML only.

**Licence:** `[INFERRED — baseline]` Work of the US Government, public domain under 17 U.S.C. §105. **Verified absence of restriction:** neither the SLS landing page, the OFAC Sanctions Lists index page, nor the ASDM FAQ carries *any* terms-of-use, copyright, licence or redistribution statement. Treasury's Privacy Act page likewise contains no IP terms. There is no click-through, no attribution requirement, and no anti-redistribution clause anywhere on the OFAC publication surface. Treat as freely redistributable; cite OFAC as source as a matter of good practice, not obligation.

**How to reuse:**
- **Factor vocabulary** — the single strongest asset in this lane. Programme codes (`UKRAINE-EO13662`, `SDGT`, `IRAN`, `RUSSIA-EO14024`, `NS-MBS`, `CAPTA`), entity types (Individual / Entity / Vessel / Aircraft), ID-type taxonomy, alias-type taxonomy (a.k.a. / f.k.a. / n.k.a.), and the ASDM name-part model give a rich, real, non-synthetic vocabulary for screening scenarios.
- **Oracle** — the ASDM XML is a deterministic ground truth. A "did the change bypass screening?" test can be built by replaying a fixed SDN snapshot against a candidate transaction set: the correct hit/no-hit answer is computable. Delta files give a *temporal* oracle: "the list changed on day D; did the system rescreen?"
- **Do NOT** use it as provision text — the files carry no obligation language.

### 1.2 31 CFR Chapter V — OFAC regulations

**URL:** https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V
**Contents:** `[VERIFIED]` Part 501 (Reporting, Procedures and Penalties Regulations — including §501.603 annual report of blocked property and §501.604 reports on rejected transactions) plus programme-specific parts: 510 (North Korea), 515 (Cuba), 525 (Burma), 526 (Hostages/Wrongful Detention), 528 (ICC-related), 535 (Iranian Assets Control), 536 (Narcotics), 539/544 (WMD), 546 (Sudan), 547 (DRC), 548 (Belarus), 549 (Lebanon), 550 (Ethiopia), 551 (Somalia), 552 (Yemen), 553 (CAR), 555 (Mali), 558 (South Sudan), 560 (Iranian Transactions and Sanctions), and others.
**Format:** eCFR HTML/XML/JSON; bulk XML at govinfo.
**Licence:** `[INFERRED — baseline]` PD, 17 U.S.C. §105.
**Reuse:** **Provision text.** §501.603/§501.604 are the reporting-obligation anchors; the programme parts supply the "why this control exists" text.

### 1.3 IEEPA — 50 U.S.C. §1701 et seq.

**URL:** https://www.law.cornell.edu/uscode/text/50/1701 (authoritative: uscode.house.gov / govinfo)
**Contents:** `[VERIFIED]` §1701 authorises presidential action on "any unusual and extraordinary threat, which has its source in whole or substantial part outside the United States, to the national security, foreign policy, or economy of the United States," upon declaration of a national emergency; a new response requires a fresh declaration tied to the specific threat. §1702(a)(1)(B) grants authority to investigate, regulate or prohibit transactions and to **block property interests** in the US or coming within the possession or control of a US person. §1705 provides civil and criminal penalties (criminal liability attaches to *knowing* violation).
**Licence:** `[INFERRED — baseline]` PD.
**Reuse:** **Provision text** — the statutory basis for "sanctions screening is never bypassed." The strict-liability posture of the civil regime (OFAC civil penalties do not require intent) is the doctrinal reason this belongs at the absolute tier.

### 1.4 BSA — SAR confidentiality and tipping-off

**31 U.S.C. §5318(g)** — https://www.law.cornell.edu/uscode/text/31/5318
`[VERIFIED]`
- **(g)(1)** authorises the Secretary to require reporting of "any suspicious transaction relevant to a possible violation of law or regulation."
- **(g)(2) Notification prohibited.** A financial institution and its officers/employees may not "notify any person involved in the transaction that the transaction has been reported or otherwise reveal any information that would reveal that the transaction has been reported." Government employees are separately barred from disclosing to a person involved, other than as necessary to official duties.
- **(g)(3)** safe harbour: no liability under federal, state or contract law for making the disclosure or for failing to notify the person involved.

**31 CFR §1020.320** — https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-C/section-1020.320
`[VERIFIED]`
- **(b)(3)** filing deadline: no later than **30 calendar days** after initial detection; extendable to **60 days** total if no suspect is identified.
- **(e) Confidentiality of SARs.** **(e)(1)(i):** "No bank, and no director, officer, employee, or agent of any bank, shall disclose a SAR or any information that would reveal the existence of a SAR."
- **(e)(1)(ii)** permits disclosure to law enforcement and regulators "provided that no person involved in any reported suspicious transaction is notified that the transaction has been reported."
- **(e)(2)** bars disclosure in private legal proceedings and in response to non-public information requests.

**CORRECTION on the "criminal tipping-off provision."**
`[VERIFIED]` **18 U.S.C. §1510(b) does NOT cover SARs.** §1510(b)(3)(B) defines "subpoena for records" as a **federal grand jury subpoena, a DOJ subpoena, or an order under specified statutes** — SARs are outside its scope. §1510(b)(1) (5 years, notification with intent to obstruct) and §1510(b)(2) (1 year, notifying a customer/person named in a subpoena) reach subpoena tipping-off only.
The criminal exposure for SAR tipping-off runs through **31 U.S.C. §5322** (penalties for wilful violation of a §5318 requirement, up to 5 years; 10 years where part of a pattern of illegal activity involving >$100,000 in a 12-month period), with civil penalties under **31 U.S.C. §5321**. **Cite §5318(g)(2) + §5322 + 31 CFR §1020.320(e), not §1510(b),** for SAR tipping-off.

**31 CFR §1020.220 (CIP)** — https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-B/section-1020.220
`[VERIFIED]`
- **(a)(2)(i)(A)** — the bank "must obtain, at a minimum, the following information from the customer **prior to opening an account**": name; date of birth (individuals); address; identification number (TIN for US persons; TIN, passport number + country, alien ID card, or number and country of issuance of any other government-issued document evidencing nationality or residence, for non-US persons).
- **(a)(2)(i)(B)** — narrow exception permitting account opening before receipt of a TIN where the customer has applied for one.
- **(a)(2)(ii)** — verification "within a reasonable time **after** the account is opened," documentary (A) or non-documentary (B), plus signatory rules for non-individuals (C).
- **(a)(2)(iii)** — procedures for when identity cannot be verified.
- **(a)(3)** — recordkeeping; retention **5 years after account closure** ((a)(3)(ii)).
- **(a)(4)** — comparison against "any list of known or suspected terrorists or terrorist organizations issued by any Federal government agency."

**Precision note for the constitution.** The rule's hard gate is **identity *information* collected before account opening**; *verification* is permitted within a reasonable time after opening. An absolute drafted as "CIP verification complete before funding" is **stricter than the regulation** and will generate false positives against the corpus. Draft it as: *identifying information obtained before account opening; verification within the institution's documented reasonable-time window; no account funded where CIP has failed and the §1020.220(a)(2)(iii) non-verification procedure has not been run.*

**Licence (all four):** `[INFERRED — baseline]` PD.
**Reuse:** **Provision text** and **oracle**. §1020.320(e) is the cleanest possible absolute: a binary, textual prohibition with no balancing test. The 30/60-day and 5-year clocks are directly testable numeric obligations.

### 1.5 FinCEN advisories and the SAR form/schema

**Advisories:** https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets
`[VERIFIED]` Four document classes — Alerts, Advisories, Notices, Bulletins/Fact Sheets — identified as `FIN-YYYY-Txx` (e.g. `FIN-2026-A002`, `FIN-2026-Alert005`). Primarily PDF; some fact sheets in HTML. `[VERIFIED]` no copyright or terms-of-use statement appears on the advisories index; site policies are linked separately.
**Section 314(a)/(b):** https://www.fincen.gov/resources/section-314a ; 314(b) Fact Sheet https://www.fincen.gov/system/files/shared/314bfactsheet.pdf (reissued 12 June 2026 with updated guidance encouraging broader fraud-related information sharing).

**SAR form/schema:** BSA E-Filing System.
- FinCEN SAR XML User Guide: https://bsaefiling.fincen.gov/docs/XMLUserGuide_FinCENSAR.pdf
- Filing instructions: https://bsaefiling.fincen.gov/resources/FinCENSARFilingInstructions.pdf
- Schema validation guidance: https://bsaefiling.fincen.gov/docs/XMLSchemaGuidance_SchemaValidation.pdf
- Companion guides exist for CTR, 8300 and DOEP.
`[VERIFIED]` XML Schema 2.0 batch filing; documented element structure and validation rules. Form: FinCEN Form 111 (FinCEN SAR).
**Licence:** `[INFERRED — baseline]` PD.
**Reuse:** **Factor vocabulary — very high value.** The FinCEN SAR XML schema's suspicious-activity category and subcategory enumerations (structuring, terrorist financing, fraud, casinos, money laundering, identity theft, cyber-event, insurance, securities/futures, mortgage fraud, and the cyber-event indicator fields) are a ready-made, authoritative taxonomy of financial-crime factors. Advisories supply **red-flag indicator lists** that map cleanly onto detection-rule test cases. Advisory text is also usable as **provision text** for "what the institution was on notice of."

### 1.6 EU consolidated sanctions list (FSF)

**Name:** Consolidated list of persons, groups and entities subject to EU financial sanctions (Financial Sanctions Files, FSF)
**Publisher:** European Commission, DG FISMA
**URL:** https://webgate.ec.europa.eu/fsd/fsf/public/rss (public feed listing the current files)
**Contents:** `[VERIFIED]` roughly 16,000 listed targets across ~43 EU sanctions regimes, spanning persons, organisations, addresses and vessels.
**Format:** `[VERIFIED]` PDF (~18 MB), CSV (v1.0 and v1.1, ~19–25 MB), and XML against a published XSD (v1.0 and v1.1, ~26 MB). Download links carry a fixed `token=dG9rZW4tMjAxNw` query parameter — this is a *static public token embedded in the published feed*, not per-user authentication, so the files are effectively openly retrievable; but it is a stable-URL hazard for automated fetching.
**Licence:** `[INFERRED — baseline]` Commission document, reusable under Commission Decision 2011/833/EU. **`[UNVERIFIED]`** — the FSF pages and the RSS feed carry **no explicit legal notice or reuse statement**; I could not locate an FSF-specific licence declaration. Treat as 2011/833-reusable with attribution, but flag the absence in the corpus provenance record.
**Do not source this from OpenSanctions.** `[VERIFIED]` OpenSanctions' redistribution of `eu_fsf` is under **CC-BY-NC 4.0** with an explicit "businesses must acquire a data license" condition. That is OpenSanctions' aggregation licence, not the Commission's, and it is **incompatible with an open corpus intended for commercial reuse**. Fetch from `webgate.ec.europa.eu` directly.
**Reuse:** **Factor vocabulary** (EU regime identifiers, EU-specific listing-reason fields) and a **second-jurisdiction oracle** for multi-list screening scenarios.

### 1.7 UK OFSI consolidated list

**Name:** UK Consolidated List of Financial Sanctions Targets
**Publisher:** HM Treasury / OFSI
**URLs:** https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets ; search app https://sanctionssearchapp.ofsi.hmtreasury.gov.uk/ ; data.gov.uk record https://www.data.gov.uk/dataset/a424169b-a2c9-4809-9ccd-a68411e5cf51/financialsanctions
**Format:** CSV, XML (ODT/HTML on the publication page); a published Consolidated List Format Guide documents the column structure.
**Licence:** `[VERIFIED]` **UK Open Government Licence (OGL)** — stated on the data.gov.uk record for this dataset, publisher HM Treasury. OGL v3 permits copying, publishing, distributing, adapting and commercial exploitation with attribution. **This is the most permissively and explicitly licensed sanctions list of the three.**
**Reuse:** **Factor vocabulary + oracle**, and the one sanctions dataset that can be redistributed inside the corpus with a clean, citable grant rather than an inference.

---

## PART 2 — PAYMENTS

### 2.1 PCI DSS v4.0.1 — requirement identifiers

**URL:** https://www.pcisecuritystandards.org/document_library/ (PCI DSS v4.0.1, June 2024; also "Summary of Changes v4.0 to v4.0.1")
**Licence:** `[VERIFIED — baseline confirmed]` Document front matter carries "©2006 - 2024 PCI Security Standards Council, LLC. All Rights Reserved." The Document Library page shows no click-through licence at download, but the Council's separate Terms and Conditions and IPR Policy govern. **The prior survey's position stands: free download, personal non-commercial licence, no redistribution.**
**⇒ Corpus rule: cite requirement *identifiers and paraphrases only*. Do not embed PCI DSS requirement text, testing procedures or guidance columns in the corpus.**

Requirement content (verified from secondary sources; identifiers confirmed against v4.x structure):

| ID | Substance | Corpus role |
|---|---|---|
| **3.3.1** | Sensitive Authentication Data (SAD) is not retained after authorization, even if encrypted; all SAD rendered unrecoverable on completion of authorization. Sub-reqs **3.3.1.1** full track data, **3.3.1.2** card verification code, **3.3.1.3** PIN/PIN block. | **Absolute.** Binary, no balancing test. |
| **3.4.1** | PAN is masked when displayed; only personnel with a legitimate business need may see more than BIN and last four. | **Absolute** for logs/displays; the "legitimate business need" clause is a graded factor. |
| **6.4.3** | Payment-page scripts loaded/executed in the consumer browser are managed: methods to confirm each script is authorized; methods to assure each script's integrity; an inventory with written business/technical justification. | Change-control gate (e-skimming / Magecart). |
| **6.5.1** | Changes to all system components in the production environment are made according to established change-control procedures: documented reason and description, documented approval by authorized parties, testing to verify the change does not adversely impact system security, back-out procedures. | **The load-bearing requirement for a software-change corpus.** This is the PCI hook for "no unreviewed change to production." |
| **8.6.2** | Passwords/passphrases for any application and system accounts are not hard-coded in scripts, configuration or property files, or bespoke and custom source code. | **Absolute-adjacent**; directly testable against a diff. |
| **11.6.1** | A change- and tamper-detection mechanism alerts personnel to unauthorized modification of security-impacting HTTP headers and payment-page script content; evaluated at least weekly or at a risk-analysis-determined frequency. | Detection obligation paired with 6.4.3. |

6.4.3 and 11.6.1 were future-dated requirements that became mandatory **31 March 2025**.

### 2.2 ISO 20022

**URL:** https://www.iso20022.org/iso-20022-message-definitions
**Contents:** `[VERIFIED]` a catalogue of ~800 message definitions across payments, securities, trade, cards and FX, each with downloadable **XSD schema**, Message Definition Report (MDR), and where applicable Message Usage Guides.
**Format:** XSD, PDF MDRs, plus the ISO 20022 Financial Repository (e-Repository, business model).
**Licence:** `[VERIFIED — partial]` Two statements, both on iso20022.org:
- **IPR Policy:** "The contributing organisation grants third parties a **non-exclusive, royalty-free license** to use the published information." Contributors retain their own IPR and warrant they have sufficient rights to publish.
- **Terms of Use:** the material "is intended to be **used and reproduced freely by all interested users** under the ISO 20022 Intellectual Property Right Policy." The site is "the sole source of up-to-date materials"; **any replication must state that it is unofficial**. Provided "as is," warranties disclaimed. Footer: "© Copyright ISO 20022."
**Assessment:** freely downloadable and freely reproducible under a royalty-free grant, **with a mandatory "unofficial copy" marking on any replication**. This is materially more permissive than ISO/IEC 27001 or PCI DSS and is safe for corpus inclusion **provided replicated schemas carry the unofficial-copy notice**. `[UNVERIFIED]` — no formal SPDX-style licence identifier exists; the grant is prose, not a standard licence.
**Reuse:** **Factor vocabulary of the highest quality.** `pain.001` / `pacs.008` / `camt.053` element names, the external code sets (purpose codes, return-reason codes, charge-bearer, category-purpose), and the structured party/account model give a precise, real vocabulary for payment-change scenarios. Also usable as an **oracle** — an XSD is a machine-checkable contract, so "did this change break the message contract?" is decidable.

### 2.3 NACHA ACH Rules

**URL:** https://www.nacha.org/content/legal-information
**Licence:** `[VERIFIED]` **Paywalled and closed.** Nacha states: "The entire contents of this Site are copyrighted, unless otherwise indicated, by Nacha. All rights are reserved and content **may not be reproduced, downloaded, disseminated, published, or transferred, in any form or by any means**, except with the prior written agreement of Nacha or as indicated below." Permitted use is limited to download/print "for their personal, noncommercial use on a single computer," with a required "© 2020 Nacha, All rights reserved." marking. The Operating Rules & Guidelines are sold through the Nacha Store; "Nacha Operating Rules Online" is a separate subscription product.
**⇒ Corpus rule: NACHA rule text is EXCLUDED. Reference by rule-section identifier and neutral paraphrase only.**
**Reuse:** **Factor vocabulary only, and only the parts that are independently public** — SEC codes (PPD, CCD, WEB, TEL, IAT, CTX, ARC, BOC, POP, RCK) and ACH **return reason codes** (R01 insufficient funds, R02 account closed, R03 no account, R07 authorization revoked, R10 customer advises not authorized, R11 customer advises entry not in accordance with terms, R29 corporate customer advises not authorized, R
) appear throughout federal regulatory text (Reg E commentary, FFIEC handbooks) and ODFI/RDFI public documentation. Use those; do not lift Nacha's rule prose.

### 2.4 SWIFT MT / MX

**URL:** SWIFT Knowledge Centre, e.g. https://www2.swift.com/knowledgecentre/rest/v1/publications/usgi_20250718/2.0/usgi_20250718.pdf (Standards MT November 2025 General Information)
**Status:** `[UNVERIFIED]` — the Knowledge Centre PDF returned a 500 error on fetch and the copyright/legal-notices page could not be read directly. Some Standards MT General Information PDFs are reachable without login via the Knowledge Centre REST path; the full Standards MT/MX message reference guides and the FIN network specifications are behind SWIFT customer authentication.
**Working assumption (flag as unverified in the corpus):** SWIFT standards documentation is **SWIFT-copyright, restricted-distribution, licensed to SWIFT users**. Treat as closed on the same footing as NACHA until a verified notice is obtained.
**Reuse:** **Factor vocabulary only** — MT message type numbers (MT103 single customer credit transfer, MT202 general financial institution transfer, MT202COV, MT940/MT942 statements) are ubiquitous in public regulatory and academic literature and are safe as identifiers. Do not embed field specifications or tag definitions.
**Note:** the MT→ISO 20022 CBPR+ migration means new corpus scenarios should be framed in ISO 20022 (`pacs.008` / `pacs.009` / `camt.05x`), which is the openly licensed path.

### 2.5 ISO 4217 currency codes

**Publisher:** SIX Group (ISO 4217 Maintenance Agency, on behalf of ISO and SNV)
**URL:** https://www.six-group.com/en/products-services/financial-information/market-reference-data/data-standards.html
- Current: `.../dam/download/financial-information/data-center/iso-currrency/lists/list-one.xls` and `list-one.xml`
- Historical: `.../lists/list-three.xls` and `list-three.xml`
- Amendments: `.../amendments/dl-currency-iso-amendment-NNN.pdf`
**Contents:** `[VERIFIED]` alphabetic code, numeric code, currency name, entity/country, minor unit. Historical list covers withdrawn codes.
**Format:** `[VERIFIED]` XLS and XML, free of charge. SIX states it maintains the lists and makes them "available online and free of charge" on behalf of ISO and SNV.
**Licence:** `[UNVERIFIED]` — **no explicit terms-of-use, licence or copyright statement is published alongside the ISO 4217 code lists.** The *standard* ISO 4217 itself is a paid ISO deliverable; the *code lists* are given away. Practical position: the three-letter codes are facts and are reproduced without objection across public datasets (including EU regulatory reporting, which mandates ISO 4217 codes as a controlled vocabulary in ITS (EU) 2024/2956), so the **codes** are safe as a vocabulary. **Do not redistribute SIX's XML/XLS files verbatim as a corpus artefact** without a verified grant; derive the code set instead.
**Reuse:** **Factor vocabulary** — currency dimension for ledger, FX and multi-region scenarios.

### 2.6 Visa and Mastercard

**Visa Core Rules and Visa Product and Service Rules** — https://www.visa.com/en-us/support/visa-rules
`[VERIFIED]` Visa publishes the rules publicly as PDF, but explicitly states it has "omitted proprietary and competitive information, as well as certain details from the rules relating to the security of the network." **No licence or reuse grant is stated on the page.**
**Mastercard Rules** — https://www.mastercard.com/us/en/business/support/rules.html
`[VERIFIED]` Publicly downloadable PDFs (Mastercard Rules, Transaction Processing Rules, Security Rules and Procedures, Chargeback Guide, subscription-billing guidance). Copyright notice "© 1994-2026 Mastercard." **No reuse or redistribution grant is stated.** The page adds that "the official rules and standards will apply" where the published version diverges.
**Both:** technical specifications (VisaNet/BASE II interface specs, Mastercard Customer Interface Specification, chip/EMV kernel specs) are **restricted to licensed customers** — not on the public pages.
**Licence conclusion:** `[VERIFIED]` **publicly readable, not licensed for redistribution.** Same treatment as PCI DSS.
**Reuse:** **Factor vocabulary and rule-section identifiers only** — chargeback reason codes (Visa 10.x fraud, 11.x authorization, 12.x processing errors, 13.x consumer disputes; Mastercard 4837, 4853, 4863, 4870), MCC codes, and the settlement/interchange concept vocabulary. **Do not embed rule text.**
**Better substitute:** EMVCo publishes EMV specifications publicly at emvco.com under its own terms — worth a separate check if card-present scenarios are needed. `[UNVERIFIED]` in this survey.

---

## PART 3 — CONSUMER PROTECTION

### 3.1 ECOA and Regulation B

**15 U.S.C. §1691** (ECOA) — prohibits discrimination in any aspect of a credit transaction on the basis of race, color, religion, national origin, sex, marital status, age (provided the applicant has capacity), because all or part of income derives from a public assistance programme, or because the applicant has in good faith exercised rights under the Consumer Credit Protection Act. §1691(d) requires notification of action taken and, on adverse action, a statement of reasons.
`[INFERRED — baseline]` PD.

**12 CFR §1002.6(b)(9)** — https://www.law.cornell.edu/cfr/text/12/1002.6
`[VERIFIED]` "a creditor shall not consider race, color, religion, national origin, or sex (or an applicant's or other person's decision not to provide the information) in any aspect of a credit transaction." §1002.6(b) more broadly bars incorporating prohibited characteristics into a creditworthiness evaluation: identical standards for married and unmarried applicants (b)(8); age and public-assistance restrictions with a narrow demonstrably-and-statistically-sound credit-scoring carve-out that must not penalise elderly applicants (b)(2); no assumptions about childbearing/childrearing (b)(3); no discounting of part-time income, pensions, annuities, or alimony/child support by source (b)(5).

**12 CFR §1002.9** — https://www.law.cornell.edu/cfr/text/12/1002.9
`[VERIFIED]`
- **(a)(1)** — notify the applicant of action taken within **30 days** of receiving a completed application; 30-day clocks also apply to adverse action on incomplete applications and on existing accounts.
- **(a)(2)** — on adverse action, written notification containing **either** a statement of specific reasons **or** disclosure of the right to request reasons within 30 days.
- **(b)(2)** — "the statement of reasons... must be **specific and indicate the principal reason(s) for the adverse action**." Statements that the adverse action was based on **internal standards or policies**, or that the applicant **failed to achieve a qualifying score** on the creditor's credit scoring system, are **insufficient**.

**Reuse:** **Provision text and oracle.** §1002.6(b)(9) is a flat prohibition — ideal absolute. §1002.9(b)(2) is the anchor for "no adverse action without principal reasons," and its explicit rejection of "failed to achieve a qualifying score" is precisely the failure mode of an unexplainable model.

### 3.2 CFPB Circulars 2022-03 and 2023-03 — WITHDRAWN

**Circular 2022-03** (Adverse action notification requirements in connection with credit decisions based on complex algorithms), 87 FR 35864, 14 June 2022 — https://www.federalregister.gov/documents/2022/06/14/2022-12729/...
Held: "A creditor cannot justify noncompliance with ECOA and Regulation B's requirements based on the mere fact that the technology it employs to evaluate applications is too complicated or opaque to understand"; "Whether a creditor is using a sophisticated machine learning algorithm or more conventional methods... the legal requirement is the same"; a creditor's lack of understanding of its own methods "is not a cognizable defense."

**Circular 2023-03** (Adverse action notification requirements and the proper use of the CFPB's sample forms provided in Regulation B), 89 FR 27361, 17 April 2024 — https://www.federalregister.gov/documents/2024/04/17/2024-08003/...
Held: creditors "may not rely on the checklist of reasons provided in the sample forms... if those reasons do not specifically and accurately indicate the principal reason(s) for the adverse action"; no "closest identifiable factor" approach; where the sample form does not fit, modify it or use "other" with an explanation; the actual factors must be disclosed even if they are surprising or non-intuitive.

**STATUS — VERIFIED WITHDRAWN.** https://www.federalregister.gov/documents/2025/05/12/2025-08286/interpretive-rules-policy-statements-and-advisory-opinions-withdrawal
`[VERIFIED]` The CFPB's mass withdrawal notice, **applicable as of 12 May 2025**, withdraws **67 guidance documents including 16 Consumer Financial Protection Circulars (2022-01 through 2024-06)**. **Both 2022-03 and 2023-03 are on the withdrawal list**, cited by their FR numbers.

**Implication for the corpus — important.** The *reasoning* in these circulars is no longer live CFPB guidance, but **the underlying obligation is unchanged**: it lives in 15 U.S.C. §1691(d) and 12 CFR §1002.9(b)(2), which the withdrawal did not and could not touch. Withdrawal of an interpretation is not repeal of the rule it interpreted (a point the NCLC and several firm analyses make expressly). **Anchor the "adverse action must state principal reasons, model opacity is no defence" absolute on §1002.9(b)(2) and the Official Interpretations to §1002.9, and cite the circulars only as withdrawn historical interpretation, clearly labelled.** Building the absolute on a withdrawn circular would be a live defect in the corpus.

### 3.3 FCRA and Regulation V

**15 U.S.C. §1681m** — https://www.law.cornell.edu/uscode/text/15/1681m
`[VERIFIED]` **(a)** on adverse action based in whole or in part on a consumer report: notify the consumer; disclose "a numerical credit score as defined in section 1681g(f)(2)(A)... used by such person in taking any adverse action"; identify the CRA and state that the CRA did not make the decision and cannot explain it; disclose the right to a free copy of the report within 60 days and the right to dispute. **(b)** adverse action based on information from affiliates/third parties that are not CRAs — disclose the nature of that information on written request within 60 days. **(h)** risk-based pricing notice where terms are materially less favourable than those available to a substantial proportion of consumers.

**15 U.S.C. §1681s-2** — https://www.law.cornell.edu/uscode/text/15/1681s-2
`[VERIFIED]` **(a)(1)** furnishers may not report information they know or have reasonable cause to believe is inaccurate ("specific knowledge... that would cause a reasonable person to have substantial doubts about the accuracy"), and may not continue reporting after consumer notice that specific information is inaccurate where it is in fact inaccurate. **(a)(2)** duty to promptly notify the CRA and provide corrections when previously furnished information is found incomplete or inaccurate. **(a)(8)** direct-dispute regime. **(b)** on notice of dispute from a CRA: investigate, review all relevant information, report results, and notify other CRAs of inaccuracies — all before expiry of the §1681i(a)(1) period (**30 days**, extendable to 45).

**Regulation V** — 12 CFR Part 1022 (CFPB), including §1022.42 (accuracy and integrity policies and procedures for furnishers) and Appendix E interagency guidelines; risk-based pricing at Subpart H (§§1022.70–1022.75); identity-theft Red Flags at Subpart J (§§1022.120–1022.123, Appendix J).
`[INFERRED — baseline]` PD.
**Reuse:** **Provision text** (furnisher-accuracy duties are the cleanest hook for "servicing/ledger changes must not corrupt what is furnished") and **oracle** (the 30-day dispute clock is numerically testable).

### 3.4 TILA and Regulation Z

**15 U.S.C. §§1601 et seq.**; **12 CFR Part 1026.**
Key provisions for a fintech-change corpus:
- **§1026.13 (billing error resolution)** — https://www.law.cornell.edu/cfr/text/12/1026.13 `[VERIFIED]` **(b)** written notice from the consumer no later than **60 days** after the creditor transmitted the first periodic statement containing the alleged error; **(c)(1)** acknowledge within **30 days** unless resolved sooner; **(c)(2)** resolve "within 2 complete billing cycles (but in no event later than **90 days**)"; **(d)** during the dispute the consumer may withhold payment of the disputed amount, and the creditor may not attempt collection, may not "make or threaten to make an adverse report" as to the disputed amount ((d)(2)), and may not accelerate or close the account solely because the consumer exercised these rights in good faith.
- §1026.6 / §1026.7 (open-end disclosures), §1026.17–1026.24 (closed-end), §1026.19(e)/(f) and §1026.37/§1026.38 (TRID Loan Estimate / Closing Disclosure), §1026.36 (loan-originator compensation), §1026.41 (periodic statements for residential mortgages), §1026.51 (CARD Act ability-to-pay).
`[INFERRED — baseline]` PD.
**Reuse:** **Provision text and oracle.** §1026.13 clocks are directly testable; note the structural symmetry with Reg E §1005.11 and the *different* numbers — a good corpus discriminator (a system that conflates the two clocks fails).

### 3.5 Regulation E

**12 CFR §1005.6** — https://www.law.cornell.edu/cfr/text/12/1005.6
`[VERIFIED]`
- **(b)(1) Timely notice given** (within 2 business days of learning of loss/theft): liability "shall not exceed the lesser of **$50** or the amount of unauthorized transfers that occur before notice to the financial institution."
- **(b)(2) Timely notice not given**: liability "shall not exceed the lesser of **$500**" — comprising up to $50 for transfers in the first two business days plus transfers after that period and up to notice, **only if the institution establishes** they would not have occurred had the consumer given timely notice.
- **(b)(3) Periodic statement; timely notice not given**: the consumer must report an unauthorized EFT appearing on a periodic statement within **60 days** of transmittal to avoid **unlimited** liability for subsequent transfers.
- **(b)(4)** extenuating circumstances extend these periods to a reasonable time.

**12 CFR §1005.11** — https://www.law.cornell.edu/cfr/text/12/1005.11
`[VERIFIED]`
- **(b)(1)(i)** consumer notice of error within **60 days** after the institution sends the periodic statement (oral or written notice suffices).
- **(c)(1)** investigate promptly and determine whether an error occurred within **10 business days**; report results within **3 business days** thereafter.
- **(c)(2)** up to **45 days** if the institution provisionally credits the amount of the alleged error (with interest where applicable) within 10 business days and gives full use of the funds.
- **(c)(3)(i)** **20 business days** in place of 10 for errors on transfers within 30 days after the first deposit to a new account.
- **(c)(3)(ii)** **90 days** in place of 45 for errors involving non-domestic-initiated transfers, POS debit card transactions, or transfers within 30 days of account opening.
`[INFERRED — baseline]` PD.
**Reuse:** **Provision text and oracle — the single best numerically testable obligation set in this lane.** $50/$500/unlimited and 2/60/10/3/45/20/90 form a small, complete, decidable rule system.

### 3.6 Dodd-Frank §§1031, 1036, 1033 and 12 CFR Part 1033

**12 U.S.C. §5531 (§1031 UDAAP)** — https://www.law.cornell.edu/uscode/text/12/5531
`[VERIFIED]` **(c) unfairness**: conduct is unfair only if it "causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers" and "is not outweighed by countervailing benefits to consumers or to competition"; public policy may be evidence but not the primary basis. **(d) abusiveness**: materially interferes with the consumer's ability to understand a term or condition, **or** takes unreasonable advantage of (1) a lack of understanding of material risks/costs/conditions, (2) an inability to protect their interests in selecting or using the product, or (3) reasonable reliance on the covered person to act in the consumer's interests.
**12 U.S.C. §5536 (§1036)** — prohibited acts: offering or providing a consumer financial product not in conformity with federal consumer financial law; engaging in any UDAAP; failing to permit access for supervision; knowingly or recklessly providing substantial assistance to another's UDAAP.
**12 U.S.C. §5533 (§1033)** — https://www.law.cornell.edu/uscode/text/12/5533
`[VERIFIED]` **(a)** a covered person shall make available "information in the control or possession of the covered person concerning the consumer financial product or service" in an electronic form usable by consumers. **(b)** four exceptions: confidential commercial information **including an algorithm used to derive credit scores or other risk scores**; information collected for preventing fraud or money laundering, or for detecting or making a report on unlawful conduct; information required to be kept confidential by other law; information the covered person cannot retrieve in the ordinary course. **(c)** no duty to retain records beyond ordinary course. **(d)** CFPB to prescribe standardized machine-readable formats. **(e)** consultation with the banking agencies and FTC; no mandating of specific technology.

**12 CFR Part 1033 — CURRENT STATUS, VERIFIED.**
- **October 2024**: CFPB finalises the Personal Financial Data Rights rule (12 CFR Part 1033), with a tiered compliance schedule beginning **1 April 2026** for depositories ≥$250B and running to 2030 for the smallest.
- **May 2025**: the CFPB itself moved to have the rule set aside, siding with the bank plaintiffs.
- **August 2025**: CFPB issues an **ANPR** reopening the rule, including whether data providers may **charge fees** for access (the original rule had effectively barred fees).
- **29 October 2025**: `[VERIFIED]` **Forcht Bank, N.A. v. CFPB**, E.D. Ky., **Judge Danny Reeves**, grants a **preliminary injunction** barring the CFPB from enforcing the 1033 final rule, finding plaintiffs "likely to succeed on all four of their claims." Co-plaintiffs include the Kentucky Bankers Association and the Bank Policy Institute.
- **Status:** the rule is **ENJOINED, NOT VACATED**. The codified text of Part 1033 remains in the CFR and the compliance dates remain formally on the books, but the CFPB cannot enforce it.
- **August 2026**: `[VERIFIED — headline level]` the CFPB sent a new Section 1033 proposal to OIRA for review; reporting indicates an **interim final rule** approach. The substance of the replacement rule is not yet final.

**⇒ Corpus rule:** an absolute anchored on Part 1033 is currently **unenforceable and about to be rewritten**. Do not put "1033 data-access obligations" at the absolute tier. Anchor data-portability/data-access obligations on **§5533 (the statute, which is unaffected)** and treat Part 1033's operational detail as a **contingent/graded** obligation with an explicit "status: enjoined pending reconsideration as of 2026-09" provenance note.

---

## PART 4 — SECURITY AND OPERATIONAL RESILIENCE

### 4.1 GLBA Safeguards Rule — 16 CFR §314.4

**URL:** https://www.law.cornell.edu/cfr/text/16/314.4
`[VERIFIED]` A written information security program with a designated **Qualified Individual** (§314.4(a)); a written **risk assessment** (b); safeguards (c):
- **(c)(1)** access controls, technical and physical, limiting authorised users and limiting authorised users' access to only what they need;
- **(c)(2)** inventory and classify data, personnel, devices, systems and facilities by criticality;
- **(c)(3)** **"Protect by encryption all customer information held or transmitted by you both in transit over external networks and at rest."** Where encryption of customer information at rest is infeasible, the Qualified Individual may approve **effective alternative compensating controls** — reviewed and approved in writing;
- **(c)(4)** secure development practices for in-house applications and procedures for evaluating externally developed apps;
- **(c)(5)** **multi-factor authentication for any individual accessing any information system**, unless the Qualified Individual has approved in writing the use of reasonably equivalent or more secure access controls;
- **(c)(6)** secure disposal of customer information no later than **two years** after the last date the information is used, unless retention is otherwise required or infeasible;
- **(c)(7)** change management procedures;
- **(c)(8)** monitoring and logging of authorised user activity and detection of unauthorised access to or use of customer information.
Plus **(d)** continuous monitoring, or annual penetration testing and **vulnerability assessments at least every six months** and after material change; **(e)** security awareness training and qualified security personnel; **(f)** service-provider selection, contractual safeguards, and periodic reassessment; **(g)** programme adjustment; **(h)** a **written incident response plan**; **(i)** an **annual written report from the Qualified Individual to the board**.
Note the FTC's separate **§314.4(j) / §314.5 notification rule**: notify the FTC as soon as possible and no later than **30 days** after discovery of a security event involving unencrypted customer information of **500 or more consumers** (in force since 13 May 2024).
`[INFERRED — baseline]` PD.
**Reuse:** **Provision text.** (c)(3) and (c)(5) are the two clauses with an explicit written-compensating-control escape hatch — structurally identical to NYDFS §500.12(b). That symmetry is worth exploiting: it is a good discriminator between "absolute" and "absolute-with-a-documented-exception."

### 4.2 23 NYCRR Part 500 — CORRECTION on the section letter

**URL:** https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf
`[VERIFIED]`
- **§500.12(a) Multi-factor authentication** — "Multi-factor authentication shall be utilized for **any individual accessing any information systems** of a covered entity," unless the covered entity qualifies for a limited exemption under §500.19(a), with specific requirements for remote access to the network, remote access to third-party applications from which nonpublic information is accessible, and **all privileged accounts** other than service accounts that prohibit interactive login.
- **§500.12(b)** — "**If the covered entity has a CISO, the CISO may approve in writing the use of reasonably equivalent or more secure compensating controls.** Such controls shall be reviewed periodically, but at a minimum annually."
- **Universal MFA transitional date: two years from 1 November 2023 → 1 November 2025.** `[VERIFIED]` The final tranche of Second Amendment requirements (universal MFA under §500.12, and the asset inventory under §500.13(a)) took effect **1 November 2025**.
- **§500.17(a)** — "Each covered entity shall notify the superintendent electronically in the form set forth on the department's website as promptly as possible but **in no event later than 72 hours** after determining that a cybersecurity incident has occurred."
- **§500.17(c)** — extortion payment: notice within **24 hours** of the payment; within **30 days**, a written description of why payment was necessary, the alternatives considered, and the diligence performed (including as to sanctions compliance — the OFAC intersection).

**CORRECTION.** The compensating-control path is at **§500.12(b)**, not §500.12(a). §500.12(a) is the MFA mandate itself. A corpus citation to "§500.12(a) compensating-control path" is wrong and should be fixed to **§500.12(b)**.

`[INFERRED — baseline]` NY State regulation; New York State law and regulations are not subject to copyright as government edicts, and DFS publishes the text openly. `[UNVERIFIED]` — no explicit reuse grant on the DFS site.
**Reuse:** **Provision text** and a **jurisdictional discriminator**: NYDFS MFA is universal with a CISO-approved compensating control; GLBA (c)(5) is universal with a Qualified-Individual-approved equivalent; PCI DSS 8.4/8.5 is scoped to the CDE. A corpus scenario that changes an MFA control must resolve all three, and they resolve differently.

### 4.3 DORA — Regulation (EU) 2022/2554 and its technical standards

**All instrument numbers VERIFIED.**

**Regulation (EU) 2022/2554 (DORA)** — applicable **17 January 2025**.
- **Article 19** — "Reporting of major ICT-related incidents and voluntary notification of significant cyber threats." `[VERIFIED]` **19(1)** "Financial entities shall report major ICT-related incidents to the relevant competent authority as referred to in Article 46." **19(4)** three reports: an **initial notification**; **intermediate reports** "as soon as the status of the original incident has changed significantly"; and a **final report** when root-cause analysis is complete. **19(5)** reporting may be outsourced to a third-party service provider, but "the financial entity remains fully responsible for the fulfilment of the incident reporting requirements."
- **Article 24** — "General requirements for the performance of digital operational resilience testing." `[VERIFIED]`
- **Article 25** — "Testing of ICT tools and systems." `[VERIFIED]`
- **Article 26** — "Advanced testing of ICT tools, systems and processes based on TLPT" (threat-led penetration testing). `[VERIFIED]`
- **Article 28** — "General principles" for ICT third-party risk. `[VERIFIED]` **28(1)** the entity remains fully responsible for compliance notwithstanding use of third parties, proportionate to the nature and importance of the dependency. **28(2)** a written strategy on ICT third-party risk, regularly reviewed. **28(3)** `[VERIFIED]` **maintain and update a register of information on all contractual arrangements for ICT services at entity, sub-consolidated and consolidated level**, distinguishing those supporting **critical or important functions** from those that do not; report at least yearly to the competent authority on new arrangements, provider categories and services; make the full register available on request; and notify the authority in a timely manner of any planned arrangement covering a critical or important function. **28(4)** pre-contractual assessment, due diligence and conflict-of-interest identification. **28(8)** exit strategies for critical/important functions. **28(9)** ESAs to develop the ITS for the register template.

**Commission Delegated Regulation (EU) 2025/301** of 23 October 2024 — RTS on the content and time limits for reporting major ICT-related incidents. `[VERIFIED — instrument number and dates]` https://eur-lex.europa.eu/eli/reg_del/2025/301/oj/eng
- **Article 5 time limits, VERIFIED:**
  - **Initial notification:** "within **four hours** from the classification of the ICT-related incident as a major ICT-related incident and **no later than 24 hours** from the moment the financial entity has become aware of the ICT-related incident."
  - **Intermediate report:** "at the latest within **72 hours** from the submission of the initial notification," and resubmitted without undue delay whenever regular activities have been recovered.
  - **Final report:** "**no later than one month** after either the submission of the intermediate report or, where applicable, after the latest updated intermediate report."
  - **Weekend/bank-holiday extension** to noon of the next working day — **not available** to credit institutions, CCPs, trading-venue operators, or NIS2 essential/important entities.

**Commission Implementing Regulation (EU) 2024/2956** of **29 November 2024** — ITS laying down standard templates for the **register of information** under DORA Art. 28(9). `[VERIFIED]` https://eur-lex.europa.eu/eli/reg_impl/2024/2956/oj/eng — in force **22 December 2024**.
- `[VERIFIED]` **15 inter-linked templates** across six layers: entity, provider, contractual arrangement, ICT service, function/asset, sub-outsourcing.
- **Submission format: xBRL-CSV** — a `report-package.json` metadata file plus one CSV per template, referencing the published ESA taxonomy. Coded fields require controlled vocabularies: **ISO 3166-1 alpha-2** country codes, **ISO 4217** currency codes, **20-character LEI**, and the ESA service-type taxonomy. Free text is not accepted.
- First reporting cycle: entity deadline **30 April 2025**; subsequent cycles typically end-Q1 (e.g. 31 March 2026) with ESA consolidation by 30 April.

**Licence (all DORA instruments):** `[VERIFIED — baseline]` EUR-Lex, reusable under Commission Decision 2011/833/EU with source acknowledgement.
**Reuse:** **Provision text** (Arts 19, 24–26, 28), **oracle** (the 4h/24h/72h/1-month cascade is the most precisely testable incident clock in any regime surveyed), and **factor vocabulary of exceptional quality** — the ITS 2024/2956 register schema is a *ready-made, machine-readable, legally mandated ontology of third-party ICT dependency*: provider identity, service type, criticality designation, sub-outsourcing chain, substitutability, exit-plan presence. For a corpus about *software change* at a fintech, this is the closest thing that exists to an official schema for "what the change touches."

### 4.4 SOX and SEC

**15 U.S.C. §7262 (SOX §404)** — https://www.law.cornell.edu/uscode/text/15/7262
`[VERIFIED]` **(a)** SEC shall require each annual report to contain an internal control report stating management's responsibility for establishing and maintaining an adequate internal control structure and procedures for financial reporting, and containing management's assessment of their effectiveness as of the end of the fiscal year. **(b)** the registered public accounting firm shall attest to and report on management's assessment (not as a separate engagement), for non-EGC issuers. **(c)** attestation does not apply to issuers that are neither large accelerated filers nor accelerated filers.
Related: **15 U.S.C. §7241 (SOX §302)** officer certifications; **18 U.S.C. §1519** (destruction/alteration of records — 20 years); **§802/§1520** audit record retention.

**SEC Rule 13a-15 (17 CFR §240.13a-15)** — https://www.law.cornell.edu/cfr/text/17/240.13a-15
`[VERIFIED]` **(a)** maintain disclosure controls and procedures **and** internal control over financial reporting. **(b)** management, including the principal executive and principal financial officers, evaluate DCP effectiveness as of the end of **each fiscal quarter** (annually for foreign private issuers). **(c)** annual management evaluation of ICFR effectiveness **using a suitable, recognized control framework established by a body with due-process procedures** (i.e. COSO). **(d)** evaluate any change in ICFR occurring during the quarter that materially affected, or is reasonably likely to materially affect, ICFR. **(f)** ICFR is "a process designed by, or under the supervision of, the issuer's principal executive and principal financial officers... to provide reasonable assurance regarding the reliability of financial reporting and the preparation of financial statements for external purposes in accordance with generally accepted accounting principles."
Rule 15d-15 mirrors this for §15(d) filers.

**SEC cybersecurity disclosure rules (2023)** — https://www.sec.gov/newsroom/press-releases/2023-139
`[VERIFIED]` **Form 8-K Item 1.05:** disclose a material cybersecurity incident within **four business days of determining that the incident is material**, describing "the material aspects of the incident's nature, scope, and timing" and its material impact or reasonably likely material impact. **National security / public safety delay** available on written determination by the **US Attorney General**. **Regulation S-K Item 106** (Form 10-K): describe processes for assessing, identifying and managing material risks from cybersecurity threats; material effects of risks and prior incidents; board oversight and management's role and expertise. Foreign private issuers: **Form 6-K** and **Form 20-F**. Compliance: 10-K/20-F for fiscal years ending on or after **15 December 2023**; 8-K/6-K from **18 December 2023** (smaller reporting companies +180 days); Inline XBRL tagging one year after initial compliance.

`[INFERRED — baseline]` all PD.
**Reuse:** **Provision text** for the financial-reporting-boundary absolute. §240.13a-15(d) — "evaluate any change in ICFR occurring during the quarter that materially affected or is reasonably likely to materially affect ICFR" — is the *exact regulatory hook* for a software-change corpus: it makes a code change inside the ledger a reportable control event. This is the strongest single citation for the "segregation of duties and audit trail inside the financial-reporting boundary" absolute.

### 4.5 FFIEC IT Examination Handbook

**URL:** https://ithandbook.ffiec.gov/ and https://ithandbook.ffiec.gov/it-booklets
`[VERIFIED]` Thirteen booklets: Architecture Infrastructure and Operations, Audit, Business Continuity Management, Development and Acquisition, E-Banking, Information Security, Management, Operations, Outsourcing Technology Services, Retail Payment Systems, Supervision of Technology Service Providers, Wholesale Payment Systems, plus archived superseded booklets. Available as HTML, per-booklet PDF, and downloadable **IT WorkPrograms** (examiner procedures); single and bulk download offered.
`[VERIFIED]` **No copyright, disclaimer or terms-of-use notice appears on the InfoBase pages.** `[INFERRED — baseline]` PD as a work of a federal interagency body (17 U.S.C. §105).
**Note:** the **FFIEC Cybersecurity Assessment Tool (CAT) was sunset on 31 August 2025** (announced 29 September 2024; OCC Bulletin 2024-25). Do not build corpus controls on the CAT maturity model.
**Reuse:** **Provision text (supervisory expectation, not law)** and **factor vocabulary**. The Development and Acquisition booklet and the Information Security booklet's change-management sections are unusually well suited to a software-change corpus — they are US regulators' own articulation of what a controlled change looks like, in prose, in the public domain, and free of any licence encumbrance. **The IT WorkPrograms are effectively free examiner checklists — a strong source of oracle-shaped assertions.**

---

## PART 5 — OPEN DATASETS A FINTECH CORPUS COULD REUSE

### 5.1 CFPB Consumer Complaint Database — MATERIALLY CHANGED IN 2026

**URL:** https://www.consumerfinance.gov/data-research/consumer-complaints/ ; API docs https://cfpb.github.io/api/ccdb/api.html ; field reference https://cfpb.github.io/api/ccdb/fields.html
**Contents:** complaints sent to companies for response, from 2011; product/sub-product, issue/sub-issue, company, state, ZIP prefix, date received, company response, timely response, consumer disputed, and (historically) the consumer narrative.
**Format:** full CSV (ZIP), filtered CSV, and an open Socrata-style API. Generally updates daily.
**STATUS CHANGE — VERIFIED.** https://www.consumerfinance.gov/about-us/newsroom/the-cfpb-to-cease-discretionary-publication-of-complaint-narratives-and-visualizations/
On **14 August 2026** the CFPB announced it is **ceasing publication of unverified complaint narratives and data visualizations**, characterising that publication as "entirely discretionary" and citing the risk of publishing "confusing or misleading information." The Bureau continues to collect, monitor and respond to complaints, to review company responses, to share data with other regulators, and to disclose under FOIA; **previously published narratives move to the FOIA Reading Room**.
**Implication:** the free-text narrative field — by far the most useful part of this dataset for a language-model corpus — is **no longer being published going forward**. Historical narratives obtained before August 2026 remain PD and usable; new complaints will arrive without narrative.
**Licence:** `[INFERRED — baseline]` PD, 17 U.S.C. §105. The page states the data is "freely available for anyone to use, analyze, and build on" but carries **no formal licence statement**. `[VERIFIED]` disclaimers: complaints are **not verified** before publication, are "not a statistical sample," and are "not necessarily representative."
**Reuse:** **Factor vocabulary** — the product/sub-product and issue/sub-issue taxonomies are an authoritative, regulator-authored ontology of consumer-harm types, and they survive the narrative change. **Weak oracle only** — the unverified-complaint disclaimer means this dataset can never establish that a violation occurred; it establishes only that a complaint of type X was made. Use it to generate realistic scenario *surfaces*, never as ground truth on liability. **Snapshot the historical narratives now if they are wanted.**

### 5.2 HMDA Loan Application Register public data

**URLs:** https://ffiec.cfpb.gov/data-publication/ ; Snapshot National Loan Level Dataset https://ffiec.cfpb.gov/data-publication/snapshot-national-loan-level-dataset/ ; Dynamic National Loan-Level Dataset `/dynamic-national-loan-level-dataset/` ; Data Browser https://ffiec.cfpb.gov/data-browser/ ; historic data https://www.consumerfinance.gov/data-research/hmda/historic-data/ ; field docs https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields/
**Contents:** loan-level mortgage application records — application/origination outcome, loan amount, loan type/purpose, occupancy, property type, action taken and **denial reasons**, applicant and co-applicant **ethnicity, race, sex, age**, income, debt-to-income band, combined LTV, interest rate, rate spread, total loan costs, lender credits, term, AUS result, and census-tract geography. Modified LAR (per-institution, privacy-modified) plus national Snapshot and Dynamic files and aggregate/disclosure reports.
**Format:** pipe-delimited text / CSV in ZIP, published annually (Snapshot) and refreshed (Dynamic); browser-based filtered downloads and an API.
`[UNVERIFIED — page is a JS SPA]` I could not read the terms text directly; the publication pages render client-side. `[INFERRED — baseline]` PD as a CFPB/FFIEC work under 17 U.S.C. §105; HMDA public data is disclosed under statutory mandate (12 U.S.C. §2803) subject to the Bureau's privacy-modification balancing test.
**Reuse:** **Factor vocabulary and oracle — the highest-value dataset in this lane for fair-lending scenarios.** It carries *both* protected-class attributes *and* the credit outcome *and* the denial reason, in real records, at national scale. This is exactly what is needed to test "did the model change introduce a prohibited-basis effect?" — the disparate-impact question becomes computable on real data rather than synthetic. Note the corresponding hazard: HMDA data must not itself be used to *train* a scoring model in a way that would violate §1002.6(b)(9); it is a **test** asset, not a training asset.

### 5.3 FFIEC data (Call Reports / CDR / UBPR)

**URLs:** https://www.ffiec.gov/ ; Central Data Repository Public Data Distribution https://cdr.ffiec.gov/public/ ; UBPR; the FFIEC CDR REST API (an R client, `ffiec`, exists on CRAN).
**Contents:** quarterly Call Report (FFIEC 031/041/051) and Uniform Bank Performance Report data for all US insured depositories; also the FFIEC geocoding/census and rate-spread tools.
**Format:** tab-delimited/XBRL bulk downloads, SOAP/REST web service (free registration for an API key).
**Licence:** `[INFERRED — baseline]` PD. `[UNVERIFIED]` — no explicit licence statement located; API access requires a free account, which is a registration gate, not a licence gate.
**Reuse:** **Factor vocabulary** (regulatory report line items, MDRM codes) and a **scale/materiality oracle** for scenarios that need a realistic institution profile.

### 5.4 SEC EDGAR — full-text search, submissions, XBRL, and financial statement data sets

**URLs:** https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data ; full-text search https://efts.sec.gov/LATEST/search-index?q= (UI at https://www.sec.gov/cgi-bin/srqsb) ; `https://data.sec.gov/submissions/CIK##########.json` ; `https://data.sec.gov/api/xbrl/companyfacts/...`, `/companyconcept/...`, `/frames/...` ; Financial Statement Data Sets https://www.sec.gov/data-research/sec-markets-data/financial-statement-data-sets
**Contents:**
- **Financial Statement Data Sets** `[VERIFIED]` — numeric data extracted from XBRL exhibits to corporate financial reports, "flattened" for cross-registrant and cross-period comparison. Coverage **2009 Q1 through 2026 Q2**, quarterly ZIPs containing `sub.txt`, `num.txt`, `pre.txt`, `tag.txt`. File sizes from ~13 KB (2009 Q1) to ~122 MB (2025 Q3). As of December 2024 the sets were reprocessed to include only primary financial-statement submissions (dimensional data excluded) and `num.txt` gained a `segments` field. **Explicit disclaimer:** the SEC "cannot guarantee the accuracy of the data sets"; errors may have been introduced during extraction; "the data sets are not a substitute for such filings."
- **Full-text search** covers filing documents from 2001 forward.
- **Submissions / XBRL frames APIs** return JSON.
**Licence:** `[VERIFIED]` **The strongest explicit statement of any source in this survey.** The SEC states: "Information presented on sec.gov is **considered public information and may be copied or further distributed by users of the web site without the SEC's permission**." Citation to the SEC as source is *requested*, not required. Excluded from the grant: the SEC seal, logos and artwork; and the registered trademarks "SEC," "EDGAR," "EDGARLink" may not be used in business names without licence.
**Access conditions (not licence conditions):** `[VERIFIED]` "Current max request rate: **10 requests/second**," regardless of the number of machines used. A declared **User-Agent** header is required in the form `Sample Company Name AdminContact@<domain>.com`, plus `Accept-Encoding: gzip, deflate` and `Host`. Unclassified bots and unauthorised crawling are prohibited; violators are throttled.
**Reuse:** **Oracle and provision text.** Item 1.05 8-K filings and Item 106 10-K disclosures are a real corpus of how issuers describe cybersecurity incidents and controls — directly reusable as scenario material for the SOX/SEC absolute. Item 9A "Controls and Procedures" sections, and disclosed **material weaknesses in ICFR**, are ground truth for what a control failure inside the financial-reporting boundary actually looks like in practice.

### 5.5 FDIC and NCUA

**FDIC** — https://www.fdic.gov/open-government/open-data/ ; BankFind Suite https://banks.data.fdic.gov/bankfind-suite/ ; API https://banks.data.fdic.gov/docs/
`[VERIFIED]` BankFind Suite covers institution search, annual historical bank data, financial reports by institution, **bank failures and assistance transactions**, peer-group comparison, events and structure changes, and a documented REST API for "data miners and developers." Formats: JSON/CSV via API, plus bulk downloads.
`[VERIFIED absence]` no terms-of-use, licence or public-domain statement is published on the FDIC open-data page. `[INFERRED — baseline]` PD, 17 U.S.C. §105.

**NCUA** — https://ncua.gov/data ; https://catalog.data.gov/organization/ncua
Quarterly Call Report and financial performance data for federally insured credit unions; bulk downloads and a data.gov catalogue presence. `[INFERRED — baseline]` PD. `[UNVERIFIED]` no explicit licence statement located on ncua.gov/data. Datasets catalogued on **data.gov** carry the federal open-data convention that federal works are not copyrighted; note that data.gov records for federal datasets typically show licence `U.S. Government Work` / no restrictions.
**Reuse:** **Factor vocabulary and institution-profile grounding.** The FDIC failed-bank and enforcement-action data is a genuine **outcome oracle** for "what happens when controls fail," which is rare and valuable.

### 5.6 FRED — EXCLUDE

**URL:** https://fred.stlouisfed.org/ ; legal terms https://fred.stlouisfed.org/legal/
**Licence:** `[VERIFIED]` **FRED must be excluded from an AI training or evaluation corpus.** The FRED Terms of Use state, in terms:
- Users may not "use the FRED® Services or FRED® Content **in connection with the development or training of any software program or system or machine learning, including large language models [or] generative artificial intelligence**."
- "**BEFORE USING DATA SERIES OWNED BY THIRD PARTIES FOR ANYTHING OTHER THAN YOUR OWN PERSONAL USE, YOU MUST CONTACT THE DATA OWNER TO OBTAIN PERMISSION**" — the Federal Reserve cannot grant permission on behalf of copyright holders. FRED aggregates many third-party copyrighted series alongside PD ones.
- Users may not "take all the data on FRED or related services and claim it is a unique product or service."
- Data mining, mirroring, robots and scraping are prohibited except as expressly allowed by the API terms.
- Series tagged "Public Domain: Citation requested" or "Copyrighted: Citation required" may be used for internal commercial purposes and displayed in textbooks/newsletters/client reports with attribution — but this carve-out does **not** displace the AI/ML training prohibition.
**⇒ Corpus rule: DO NOT INGEST FRED.** Where macro series are needed, source them from the **originating agency** (BLS, BEA, Census, Federal Reserve Board H.15/H.8 releases), which are PD under §105 and carry no such restriction. This is a clean substitution — FRED is a convenience aggregator, not a primary source.

---

## PART 6 — SOURCE SUMMARY TABLE

| # | Source | Licence status | Corpus role |
|---|---|---|---|
| 1 | OFAC SDN / Consolidated (CSV, XML, ASDM) | PD (inferred, no contrary notice — verified absence) | Factor vocab + **oracle** |
| 2 | 31 CFR Ch. V | PD | Provision text |
| 3 | IEEPA 50 USC §1701–1705 | PD | Provision text |
| 4 | 31 USC §5318(g), §5322 | PD | Provision text |
| 5 | 31 CFR §1020.320, §1020.220 | PD | Provision text + oracle |
| 6 | FinCEN advisories; SAR XML schema | PD (verified absence of notice) | **Factor vocab (top tier)** |
| 7 | EU FSF consolidated list | 2011/833 inferred; **no explicit notice — UNVERIFIED** | Factor vocab + oracle |
| 8 | UK OFSI consolidated list | **OGL — VERIFIED, cleanest grant** | Factor vocab + oracle |
| 9 | PCI DSS v4.0.1 | Non-commercial, **no redistribution** | **Identifiers only** |
| 10 | ISO 20022 XSDs + repository | **Royalty-free, freely reproducible; replications must be marked unofficial — VERIFIED** | Factor vocab + oracle |
| 11 | NACHA Operating Rules | **Closed, all rights reserved — VERIFIED** | **Excluded**; SEC/return codes only |
| 12 | SWIFT MT/MX | **UNVERIFIED — treat as closed** | Message-type identifiers only |
| 13 | ISO 4217 (SIX) | Free of charge; **no licence statement — UNVERIFIED** | Codes as vocab; don't redistribute files |
| 14 | Visa / Mastercard rules | Public read, **no reuse grant — VERIFIED** | Identifiers + reason codes only |
| 15 | ECOA / Reg B §1002.6, §1002.9 | PD | Provision text + oracle |
| 16 | CFPB Circulars 2022-03, 2023-03 | PD — but **WITHDRAWN 12 May 2025** | Historical only, must be labelled |
| 17 | FCRA §1681m, §1681s-2; Reg V | PD | Provision text + oracle |
| 18 | TILA / Reg Z §1026.13 | PD | Provision text + oracle |
| 19 | Reg E §1005.6, §1005.11 | PD | **Provision text + best oracle** |
| 20 | DFA §§1031/1036/1033 (12 USC 5531/5536/5533) | PD | Provision text |
| 21 | 12 CFR Part 1033 | PD — but **ENJOINED (Forcht Bank, E.D. Ky., 29 Oct 2025)** | Contingent tier only |
| 22 | 16 CFR §314.4 | PD | Provision text |
| 23 | 23 NYCRR Part 500 | PD/edict inferred; **UNVERIFIED** grant | Provision text + discriminator |
| 24 | DORA + RTS 2025/301 + ITS 2024/2956 | **2011/833 — VERIFIED** | Provision text + oracle + **schema ontology** |
| 25 | SOX §404 / Rule 13a-15 / SEC cyber rules | PD | **Provision text (ICFR-change hook)** |
| 26 | FFIEC IT Handbook + WorkPrograms | PD (verified absence of notice) | Provision text + oracle-shaped checklists |
| 27 | CFPB Complaint DB | PD inferred; **narratives discontinued 14 Aug 2026** | Factor vocab; weak oracle |
| 28 | HMDA LAR | PD inferred; **UNVERIFIED** (JS SPA) | **Factor vocab + fair-lending oracle** |
| 29 | FFIEC CDR / UBPR | PD inferred; registration gate | Factor vocab |
| 30 | SEC EDGAR (FTS, XBRL, FSDS) | **Explicit "may be copied or further distributed without permission" — VERIFIED** | Oracle + provision text |
| 31 | FDIC BankFind / NCUA | PD inferred | Factor vocab + outcome oracle |
| 32 | FRED | **AI/ML training PROHIBITED — VERIFIED** | **EXCLUDE** |

---

## PART 7 — THE THREE TIERS

### Design principle

An **ABSOLUTE** should satisfy four tests:
1. **Bright-line.** The rule is binary in its own text, not the output of a balancing test. §1002.6(b)(9) qualifies; §5531(c) unfairness (which has an express cost-benefit balance) does not.
2. **No documented-exception escape hatch.** Where the rule itself provides a written-compensating-control path (GLBA §314.4(c)(3)/(c)(5); NYDFS §500.12(b)), the *control* is not absolute — but the *obligation to have an approved exception on record before deviating* can be.
3. **Currently in force.** A withdrawn circular or an enjoined rule cannot carry an absolute.
4. **Detectable from a software change.** The corpus is about change; an absolute that cannot be violated by a diff, a config change, a model swap, or a deployment belongs at a lower tier.

### TIER 1 — ABSOLUTE (non-negotiable; the change is blocked)

| # | Absolute | Primary anchor |
|---|---|---|
| A1 | **Sanctions screening is never bypassed, disabled, or degraded** — no change may remove a screening step, widen a whitelist, defer rescreening after a list update, or route value around the screen. | 50 USC §1702(a)(1)(B), §1705; 31 CFR Ch. V; strict civil liability |
| A2 | **A SAR, or any information that would reveal its existence, is never disclosed to a person involved** — no logging, no customer-facing status, no notification, no support-tool exposure, no model output. | 31 USC §5318(g)(2) + §5322; 31 CFR §1020.320(e)(1) |
| A3 | **CIP identifying information is obtained before account opening; no account is funded where CIP has failed and the non-verification procedure has not been executed.** | 31 CFR §1020.220(a)(2)(i)(A), (a)(2)(iii) |
| A4 | **Sensitive authentication data is never retained post-authorization; PAN is never written to logs or displayed beyond BIN + last four absent legitimate business need.** | PCI DSS 3.3.1, 3.4.1 (identifiers only) |
| A5 | **EU personal data never leaves the EEA without a live Art. 45 adequacy decision or an Art. 46 safeguard in place.** | GDPR Arts 44–46 |
| A6 | **Prohibited-basis attributes and their close proxies are never inputs to a credit decision model or rule.** | 12 CFR §1002.6(b)(9); 15 USC §1691 |
| A7 | **No Art. 5 EU AI Act prohibited practice is deployed** — in a fintech, principally social scoring (5(1)(c)), workplace emotion recognition (5(1)(f)), and biometric categorisation by protected characteristic (5(1)(g)). | Reg (EU) 2024/1689 Art. 5 (applicable 2 Feb 2025) |
| A8 | **Inside the financial-reporting boundary, segregation of duties and the immutable audit trail are never removed, weakened, or bypassed** — including no self-approval, no shared privileged credentials, no ability to alter or delete ledger history. | 15 USC §7262; 17 CFR §240.13a-15(a),(c),(d); 18 USC §1519 |
| A9 | **Reg E consumer liability caps and error-resolution clocks are never exceeded** — $50/$500/unlimited tiers and the 10/3/45/20/90-business-day cascade are hard limits, and provisional credit is never withheld where the 45-day extension is used. | 12 CFR §§1005.6, 1005.11 |
| A10 | **No adverse action without a specific statement of the principal reasons actually driving the decision** — an unexplainable model is a blocked model, not an excused one. | 12 CFR §1002.9(a)(2), (b)(2); 15 USC §1681m(a) |
| A11 | **No autonomous agent moves funds outside a bounded, pre-authorised mandate with a working human stop** — bounded by counterparty, amount, velocity, and jurisdiction, with a stop that halts in-flight execution. | Derived: 12 USC §5531(d)(2)(C) reasonable reliance; 17 CFR §240.13a-15; DORA Art. 28(1) |
| **A12** | **NEW — Credentials, keys and secrets are never hard-coded or committed** to source, scripts, configuration or property files, and no production secret is ever written to a log or a model context. | PCI DSS 8.6.2 (identifier); 16 CFR §314.4(c)(1); 23 NYCRR §500.12(a) |
| **A13** | **NEW — Production changes inside the cardholder-data environment and the financial-reporting boundary never reach production without documented approval by an authorised party other than the author, evidence of security testing, and a back-out procedure.** | PCI DSS 6.5.1 (identifier); 16 CFR §314.4(c)(7); 17 CFR §240.13a-15(d); FFIEC D&A booklet |
| **A14** | **NEW — Regulatory notification clocks are never silently missed.** A change that degrades the ability to detect, classify, or report an incident within the applicable window is blocked. Windows: DORA 4h/24h initial, 72h intermediate, 1 month final; NYDFS 72h (24h for extortion payment); SEC 8-K Item 1.05 four business days from materiality determination; FTC Safeguards 30 days / 500 consumers; SAR 30 (60) days. | Reg (EU) 2025/301 Art. 5; 23 NYCRR §500.17(a),(c); 17 CFR §229.106 / Form 8-K Item 1.05; 16 CFR §314.4(j); 31 CFR §1020.320(b)(3) |

### TIER 2 — GATED (the change proceeds only with a named, recorded, competent approval)

- **G1** MFA weakening anywhere — requires a **written compensating-control approval** by the CISO (23 NYCRR §500.12(b)) or the Qualified Individual (16 CFR §314.4(c)(5)), reviewed at least annually.
- **G2** Reduction of encryption at rest or in transit for customer information — written approval of alternative compensating controls (16 CFR §314.4(c)(3)).
- **G3** New or materially changed ICT third-party dependency supporting a critical or important function — pre-contractual assessment, due diligence, exit strategy, and **register-of-information update in the ITS 2024/2956 xBRL-CSV format** (DORA Arts 28(3),(4),(8)).
- **G4** Any change to a credit decision model — fair-lending disparate-impact testing, reason-code mapping revalidation, and model documentation refresh before deployment.
- **G5** Changes to consumer disclosures, adverse-action notices, error-resolution correspondence, or periodic statements — compliance review against Reg B/E/Z/V.
- **G6** Payment-page script changes — authorisation, integrity assurance, inventory with written justification, and tamper-detection coverage confirmed (PCI DSS 6.4.3, 11.6.1).
- **G7** Data-retention or deletion schedule changes — GLBA two-year disposal rule, CIP five-year rule, SOX/§1519 retention, GDPR storage limitation. These pull in opposite directions and must be reconciled explicitly.
- **G8** Consumer data access/portability interface changes — currently a **contingent** obligation given the Part 1033 injunction; gate on §5533 and the FDX de facto standard, and re-tier when the replacement rule lands.
- **G9** Resilience-testing scope changes and TLPT scope (DORA Arts 24–26).
- **G10** Changes to what is furnished to consumer reporting agencies (15 USC §1681s-2(a)(1)) and to dispute-investigation workflow (§1681s-2(b), 30 days).

### TIER 3 — GRADED (documented judgement; proportionality applies)

- Risk-based tuning of transaction-monitoring and fraud thresholds (false-positive/false-negative trade-off is expressly a judgement call).
- UDAAP assessment of new product flows and dark-pattern review — §5531(c)'s balancing test makes this graded by construction.
- Vendor concentration and substitutability judgements below the critical/important threshold.
- Vulnerability remediation prioritisation and SLA setting (16 CFR §314.4(d) six-month cadence is the floor, not the answer).
- Logging verbosity and retention tuning outside the audit-trail core.
- Data-minimisation and purpose-limitation judgements for analytics.
- Accessibility, plain-language, and disclosure-comprehension improvements.
- Business-continuity RTO/RPO calibration.

---

## PART 8 — ASSESSMENT OF THE EXISTING ELEVEN

### Verdict

**The eleven are well chosen. All eleven survive, none should be demoted, and every one of them can be anchored on a currently-in-force primary instrument.** But **four of the eleven need their citation or their wording corrected**, and there are **material gaps**.

### Corrections required to the existing eleven

**(a) "CIP before funding" is drafted stricter than the rule.**
31 CFR §1020.220 requires identifying *information* before account opening but permits *verification* within a reasonable time **after** opening, and provides an explicit procedure (a)(2)(iii) for when identity cannot be verified. As drafted, "CIP before funding" will flag conforming behaviour. Reword per A3 above. This is the single most likely source of false positives in the current list.

**(b) The tipping-off citation is wrong if it points at 18 U.S.C. §1510(b).**
§1510(b) reaches **subpoenas**, not SARs (§1510(b)(3)(B) defines the term). Use **31 U.S.C. §5318(g)(2) + §5322** and **31 CFR §1020.320(e)(1)**.

**(c) "Adverse action without principal reasons" must not be anchored on the CFPB circulars.**
Circulars 2022-03 and 2023-03 were **withdrawn effective 12 May 2025** in the CFPB's 67-document withdrawal notice. The obligation is intact — it lives in 15 U.S.C. §1691(d) and 12 CFR §1002.9(b)(2), whose text independently rejects "failed to achieve a qualifying score" as a sufficient reason. Anchor there; cite the circulars only as labelled, withdrawn historical interpretation.

**(d) The NYDFS compensating-control cite is §500.12(b), not §500.12(a).**
§500.12(a) is the universal MFA mandate (effective 1 November 2025); §500.12(b) is the CISO written-approval path.

### What is missing — ranked

**M1 (highest). Secrets and credentials in code.** Reviewed as A12 above. This is the most frequently *actually violated* control in real fintech change, it is trivially detectable from a diff, and it is required by PCI DSS 8.6.2, GLBA §314.4(c)(1), and NYDFS §500.7 privileged-access management. Its absence from a *software-change* constitution is the largest gap in the list.

**M2. Change control itself.** Reviewed as A13. The existing eleven contain no absolute about *how a change reaches production* — only about what the changed system must not do. PCI DSS 6.5.1 (documented reason, approval by an authorised party, security testing, back-out) and SEC Rule 13a-15(d) (evaluate ICFR changes each quarter) make unreviewed production change a regulatory event in its own right. A corpus governing software change that has no absolute about the change process has a hole at its centre.

**M3. Regulatory notification clocks.** Reviewed as A14. The list has no incident-reporting absolute at all, despite four independent regimes imposing hard, short, numerically specific windows (DORA 4h/24h/72h/1mo; NYDFS 72h/24h; SEC 4 business days; FTC 30 days) plus the SAR 30/60-day clock. These are the most testable obligations in the entire survey and the easiest to break with a change that degrades detection or classification.

**M4. Blocked-property and rejected-transaction reporting.** A1 covers screening but not the *consequence* of a hit. 31 CFR §501.603 (annual report of blocked property) and §501.604 (reports on rejected transactions) impose reporting duties that a change to the hit-handling path can silently break. Fold into A1 or add as a Tier-1 sub-clause.

**M5. Furnisher accuracy.** For a lender/servicer, 15 U.S.C. §1681s-2(a)(1) — do not report information you know or have reasonable cause to believe is inaccurate — is a strict, bright-line duty that a ledger or servicing change can violate wholesale and silently, at scale, across every borrower. It is at least as consequential as the Reg E clocks and is absent from the eleven. Recommend Tier 1 or high Tier 2.

**M6. Ledger integrity as a distinct absolute.** A8 covers segregation of duties and audit trail; it does not state that **the ledger must balance and its history must be immutable**. Double-entry integrity, no retroactive mutation of posted entries, and no unreconciled suspense are the substrate on which ICFR assertions rest. Consider splitting A8 into (i) access/SoD and (ii) ledger immutability and reconciliation.

**M7. Reg Z billing-error clocks are absent while Reg E's are present.** A9 covers Reg E. The credit-side twin — 12 CFR §1026.13's 60-day notice / 30-day acknowledgment / 2-cycle-or-90-day resolution, and the §1026.13(d)(2) bar on adverse credit reporting during a dispute — is equally hard-edged and equally breakable. For a card issuer, this is a symmetric obligation and its omission is an asymmetry defect.

**M8. Consider whether A5 should be broadened.** As drafted, A5 is a GDPR transfer rule. In practice the corpus will also need a **data-residency/localisation** absolute that is not GDPR-specific (state privacy laws, DORA's location requirements for critical functions, and contractual residency commitments). Keep A5 as the Art. 45/46 absolute; add residency as a Tier-2 gate.

### On the eleventh (autonomous agent moving funds)

This one is the most forward-looking and the least well anchored — there is no instrument that says "an agent must have a bounded mandate and a human stop." It is a **derived** absolute. That is defensible and I would keep it, but its provenance record should say so honestly and cite the three obligations it is derived from: §5531(d)(2)(C) (unreasonable advantage of a consumer's reasonable reliance on the covered person to act in their interest), Rule 13a-15 (controls over transactions affecting the financial statements), and DORA Art. 28(1) (full responsibility retained notwithstanding delegation). It should **not** be presented as a direct reading of any single instrument.

---

## PART 9 — CORPUS BUILD RULES (consolidated)

1. **Exclude entirely:** FRED (explicit AI/ML training prohibition), NACHA Operating Rules text (all rights reserved), ISO/IEC 27001 (baseline), AICPA TSC (baseline).
2. **Identifiers and paraphrase only, never text:** PCI DSS v4.0.1, Visa Core Rules, Mastercard Rules, SWIFT standards.
3. **Do not source EU sanctions data via OpenSanctions** (CC-BY-NC + commercial licence requirement). Fetch from `webgate.ec.europa.eu` under 2011/833.
4. **Prefer UK OFSI** where a sanctions dataset must be *redistributed inside* the corpus — it is the only one with an explicit, verified, commercially permissive grant (OGL).
5. **Mark ISO 20022 replications "unofficial"** — required by the ISO 20022 Terms of Use.
6. **Derive ISO 4217 codes; do not redistribute SIX's files** absent a verified grant.
7. **Respect SEC EDGAR access conditions** — declared User-Agent, ≤10 req/s. These are access terms, not licence terms; the licence itself is maximally permissive.
8. **Snapshot CFPB complaint narratives now** — publication ceased 14 August 2026; historical narratives remain PD but are moving to the FOIA Reading Room.
9. **Record status flags in provenance** for: Part 1033 (enjoined, Forcht Bank, 29 Oct 2025; replacement rule at OIRA Aug 2026); CFPB Circulars 2022-03 / 2023-03 (withdrawn 12 May 2025); FFIEC CAT (sunset 31 Aug 2025).
10. **Never cite HMDA data as a training input for a scoring model** — it is a fair-lending *test* asset only.

---

## PART 10 — OPEN ITEMS (explicitly unverified)

| Item | Why unverified | Suggested next step |
|---|---|---|
| EU FSF explicit reuse notice | No legal notice on FSF pages or RSS feed | Query DG FISMA; or rely on 2011/833 with a documented inference |
| SWIFT standards documentation licence | Knowledge Centre PDF returned HTTP 500; legal notice unreadable | Fetch a Standards MT General Information PDF's front matter directly |
| SIX ISO 4217 file terms | No licence statement published with the code lists | Contact SIX; meanwhile derive codes rather than redistribute files |
| HMDA publication terms | ffiec.cfpb.gov pages are client-rendered SPAs | Fetch via the HMDA API or the static docs subdomain |
| 23 NYCRR Part 500 reuse grant | No explicit statement on dfs.ny.gov | Rely on the government-edicts doctrine; note the inference |
| NCUA / FFIEC CDR explicit licence | No statement located | Check the data.gov catalogue records for a stated `U.S. Government Work` licence |
| EMVCo specification terms | Not surveyed | Check emvco.com terms if card-present scenarios are needed |
| FinCEN site policies page | Advisories index carries no notice; the linked site-policies page was not read | Fetch fincen.gov site policies |
