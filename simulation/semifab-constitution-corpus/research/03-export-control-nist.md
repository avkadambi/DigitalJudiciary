# 03 — Export Control, Trade Compliance, Data Sovereignty & US Federal Cybersecurity Frameworks

Research lane 03 for the SEMIFAB open compliance test corpus (constitutional "provisions" governing
software change in semiconductor manufacturing / supply-chain monitoring software).

**Research date:** 2026-09-05
**Verification standard:** every licence / public-domain claim below is either (a) quoted from a
first-party licence or terms page that was actually fetched during this research, or (b) explicitly
marked **UNVERIFIED**. Nothing is guessed.
**Fetch limitation to be aware of:** direct `curl` egress was blocked in this environment (agent
proxy `connect_rejected`); all verification was done through the WebFetch tool, which renders a page
through a summarising model. Where a first-party terms page could not be rendered (notably
`developer.trade.gov` — DNS failure on `developer.export.gov`, and `law.moj.gov.tw` — robots
disallowed), the item is marked UNVERIFIED and a fallback authority is named.

---

## 0. The governing copyright baseline for US federal material

This is the single most load-bearing licence fact in this lane, so it is stated once up front and
referenced by everything below.

**Source:** GovInfo policies page — <https://www.govinfo.gov/about/policies>
**Verified statement:** GovInfo restates 17 U.S.C. § 105 — *"Copyright protection under this title is
not available for any work of the United States Government"* — and states that US Government works
can generally be reprinted without legal restriction, with two caveats:

1. A government publication may embed **third-party copyrighted material** used with permission;
   publishing it in a government document does not grant onward reuse rights in that embedded material.
2. GovInfo recommends **customary credit** to the originating department or agency.

**Consequence for the corpus:** the *regulatory text itself* — the EAR (15 CFR 730–774), the ITAR
(22 CFR 120–130), 15 CFR Part 231 (CHIPS clawbacks), 15 U.S.C. § 4652 — is a US Government work and
is **not subject to US copyright**. It is therefore **safe to VENDOR** verbatim into the corpus.
Foreign rights are technically reserved in principle but are not asserted for the CFR.

**Caveat that matters operationally:** eCFR/BIS renderings are *unofficial*. BIS's own EAR page
carries the disclaimer: *"This resource is not an official legal edition of the Code of Federal
Regulations or the Federal Register, and it does not replace the official versions of those
publications."* If the corpus vendors provision text, it must record the **retrieval date and the
eCFR/Federal Register citation**, because the EAR changes frequently (see §1.6).

---

## 1. EXPORT CONTROL — Export Administration Regulations (15 CFR 730–774)

### 1.1 EAR § 734.13 — Export / "deemed export"

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.13>
- **Contains (verified quotes):**
  - § 734.13(a)(2): *"Releasing or otherwise transferring 'technology' or source code (but not object
    code) to a foreign person in the United States"* is an **export**.
  - § 734.13(b): *"Any release in the United States of 'technology' or source code to a foreign
    person is a deemed export to the foreign person's most recent country of citizenship or
    permanent residency."*
- **Format:** HTML (eCFR); XML via GovInfo eCFR bulk data.
- **Licence:** US Government work, no US copyright (§0). **VENDOR.**
- **Reuse:** This is the single highest-value provision in the lane. It becomes **Tier 1 ABSOLUTE
  provision P-DEEMED-EXPORT** (see §7). It also supplies factor vocabulary: `foreign_person`,
  `release`, `technology`, `source_code`, `object_code`, `country_of_citizenship`,
  `country_of_permanent_residency`.
- **Why it is the crux for software:** a deemed export needs no border crossing and no shipment. In a
  supply-chain monitoring product, a code review, a screen-share, a Jira attachment, a Grafana panel
  showing recipe parameters, a stack trace, or an on-call rotation that grants a non-US-person
  engineer read access to controlled `technology` is an export event. There is no "no data left the
  country" defence.

### 1.2 EAR § 734.9 — Foreign Direct Product (FDP) rules

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.9>
- **Contains (verified structure, subsection by subsection):**
  - (b) National Security FDP; (c) 9x515 FDP; (d) "600 series" FDP
  - (e) **Entity List FDP rules** — footnote 1, footnote 4, and **footnote 5 / Advanced-Node
    Integrated Circuits FDP** (3B-series items destined to advanced-node IC production facilities in
    Country Group D:5 or Macau)
  - (f) Russia/Belarus/Crimea FDP; (g) Russia/Belarus Military End User FDP (footnote 3)
  - (h) **Advanced Computing FDP** — direct products of 3D001/3D901 etc., items specified in 3A090,
    4A090 or the `.z` paragraphs, destined worldwide or involving D:5/Macau-headquartered entities
  - (i) "Supercomputer" FDP (China/Macau)
  - (j) Iran FDP
  - (k) **Semiconductor Manufacturing Equipment (SME) FDP** — 3B001/3B002 items that are direct
    products of 3D992/3E992 technology, destined to Macau or D:5
  - (l) **AI Model Weights FDP** — ECCN 4E091 produced by plants using specified semiconductor/AI
    computing technology, destined anywhere
  - Common two-part structure: **product scope** + **country/end-user scope**.
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** factor vocabulary (`fdp_rule`, `product_scope`, `country_scope`, `direct_product`,
  `plant_or_major_component`, `footnote_1/3/4/5`), and as an **oracle**: an FDP determination is a
  deterministic two-part predicate, which makes it an excellent machine-checkable test case.
  Provision text for a **Tier 2** provision (defeasible — licences and exceptions exist).

### 1.3 EAR § 744.23 — Advanced computing / supercomputer / advanced-node IC / SME end-use controls

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/section-744.23>
- **Contains (verified):** a licence requirement triggered when the exporter has **"knowledge"** at
  the time of export/reexport/transfer that the item is destined for one of four end uses:
  1. **Supercomputers** in Macau or Country Group D:5
  2. **Advanced-node integrated circuits** — development/production at facilities in restricted
     destinations, *plus ECAD/TCAD software for advanced-node IC design*
  3. **Advanced computing items** destined to entities **headquartered** in Macau or D:5, even when
     physically shipped elsewhere
  4. **Semiconductor manufacturing equipment** production in Macau or D:5
  - Licence review: presumption of denial for D:5/Macau; presumption of approval for US and
    A:5/A:6 entities not majority-owned by restricted entities; case-by-case for some items.
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** the **"knowledge" standard** (EAR § 772.1 defines knowledge to include "awareness of a
  high probability" and conscious disregard / wilful avoidance) is exactly the concept a constitution
  needs for **red-flag escalation** provisions. Item 3 — *headquarters*, not shipping address — is a
  strong Tier 2 provision for any system that resolves counterparties by ship-to address only.

### 1.4 EAR § 734.7 (Published) and § 734.18 (Activities that are not exports)

- **§ 734.7 URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.7>
  - Unclassified technology/software made available to the public without restriction (subscriptions,
    public libraries, unlimited distribution at conferences, internet posting, submission for
    publication) is **"published"** and not subject to the EAR.
  - **Exclusions verified:** published encryption software classified under **ECCN 5D002** remains
    subject to the EAR unless specific source-code criteria are met; firearms-related 3D/AMF/G-code
    technology (0A501, 0A506, 0A507, 0A509) remains controlled.
- **§ 734.18 URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-734/section-734.18>
  - **§ 734.18(a)(5) (verified quote):** sending/taking/storing technology or software that is
    *"(i) Unclassified; (ii) Secured using 'end-to-end encryption;' (iii) Secured using cryptographic
    modules (hardware or 'software') compliant with Federal Information Processing Standards
    Publication 140-2 (FIPS 140-2) or its successors…"* and **not "intentionally stored in a country
    listed in Country Group D:5"** is **not** an export/reexport/transfer.
  - **§ 734.18(b) (verified quote):** *"'End-to-end encryption' means (i) the provision of
    cryptographic protection of data such that the data is not in unencrypted form between an
    originator (or the originator's in-country security boundary) and an intended recipient (or the
    recipient's in-country security boundary), and (ii) the means of decryption are not provided to
    any third party."*
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** § 734.18(a)(5) is the **single most important safe-harbour rule for cloud architecture**
  in this corpus and should become a **Tier 1 ABSOLUTE architectural floor** in its negative form:
  *if you rely on the encryption carve-out, then FIPS-validated end-to-end encryption and no
  intentional D:5 storage and no third-party key escrow are all mandatory and none may be traded
  away.* The "means of decryption are not provided to any third party" clause is directly violated by
  a cloud KMS where the provider holds the keys, and by any log-shipping SaaS that decrypts for
  indexing. This is where most real semiconductor SaaS designs break.

### 1.5 EAR Part 762 — RECORDKEEPING (the record-immutability anchor)

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-762>
- **§ 762.2 Records to be retained:** export control documents, memoranda, notes, correspondence,
  contracts, financial records, boycott documents, BIS notifications, firearm serial numbers, and
  other records pertaining to covered transaction types.
- **§ 762.5 Reproduction of original records — VERIFIED nine system requirements:**
  1. *"The system must be capable of reproducing all records on paper."*
  2. *"The system must record and be able to reproduce all marks, information, and other
     characteristics of the original record, including both obverse and reverse sides of paper
     documents in legible form."*
  3. High degree of legibility and readability when viewed or reproduced.
  4. ***"The system must preserve the initial image (including both obverse and reverse sides of
     paper documents) and record all changes, who made them and when they were made."*** ← the
     immutability + audit-trail clause
  5. Written procedures for operation, identifying responsible individuals.
  6. Written inspection and quality-assurance procedures.
  7. *"The system must be complete and contain all records required"* or provide correlation methods
     for related transactions.
  8. **Audit trail:** records documenting *"where, when, by whom, and on what equipment"* entries
     occurred.
  9. Access and inspection: records, equipment and personnel produced on request.
- **§ 762.6 Period of retention:** **five years** from the latest of export from the United States,
  any reexport, transfer, or termination of the transaction. **Verified prohibition on destruction:**
  *"If the Bureau of Industry and Security or any other government agency makes a formal or informal
  request for a certain record or records, such record or records may not be destroyed or disposed of
  without the written authorization"* of that agency.
- **§ 762.7 Inspection and production:** records made *"available for inspection and copying"*; BIS
  may subpoena when voluntary cooperation is not forthcoming.
- **Licence:** US Government work. **VENDOR.**
- **Reuse — this is the highest-value find in the lane for record immutability.** § 762.5(b)(4) and
  (b)(8) are, in effect, a *statutory append-only-log-with-actor-attribution requirement*, written in
  1990s microfilm language but fully applicable to a database. They give the constitution a real
  statutory floor for immutability rather than a security best practice. § 762.6's litigation/regulatory
  hold provision gives a **Tier 1 non-derogable hold rule**: once BIS asks, retention policy,
  GDPR erasure requests, cost, and storage pressure all lose.

### 1.6 EAR § 764.2 — Violations (the enforcement oracle)

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-764/section-764.2>
- **Verified quotes:**
  - (a) *"No person may engage in any transaction or take any other action prohibited by or contrary
    to … ECRA, the EAR, or any order, license or authorization issued thereunder."*
  - (b) *"No person may cause or aid, abet, counsel, command, induce, procure, permit, or approve the
    doing of any act prohibited … by ECRA, the EAR, or any order, license or authorization."*
  - (c) solicitation and attempt; (d) conspiracy; (e) acting with **knowledge** that a violation has
    occurred, is about to occur, or is intended to occur.
  - (g) *"…false or misleading representation, statement, or certification, or falsify or conceal any
    material fact…"*
  - (h) *"No person may engage in any transaction … with intent to evade the provisions of ECRA, the
    EAR, or any order, license."*
  - (i) **Document alteration:** prohibits altering licences or export control documents *"except as
    specifically authorized in the EAR or in writing by BIS."*
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** § 764.2(b) ("cause or aid, abet … permit, or approve") is the hook that makes a *software
  system* a violator, not merely its users — a monitoring platform that auto-approves a shipment is
  "permitting or approving." § 764.2(i) is a **second, independent statutory basis for record
  immutability**, this time on export control documents specifically. § 764.2(g)/(h) support a Tier 1
  anti-evasion provision (no "route around the check" feature, ever).

### 1.7 Commerce Control List — Part 774 and the semiconductor ECCNs

- **Part 774 URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-774>
  - Verified structure: § 774.1 Introduction; § 774.2 [Reserved]; **Supplement No. 1** = the Commerce
    Control List (Categories 0–9); **Supplement No. 2** = General Technology and Software Notes;
    **Supplement No. 4** = CCL Order of Review; Supplements 5, 6 (Sensitive List), 7 (Very Sensitive
    List).
- **ECCNs in scope for semiconductors:**
  - **3A001** — electronic components/assemblies (includes the `.z` paragraphs).
  - **3A090 / 4A090** — advanced computing ICs and computers. **Thresholds (verified against K&L
    Gates' analysis of the 17 Oct 2023 rule, not against eCFR directly — see caveat):**
    - 3A090.a: **TPP ≥ 4800**, *or* **TPP ≥ 1600 and performance density ≥ 5.92**
    - 3A090.b: **TPP ≥ 2400 and < 4800 with performance density ≥ 1.6 and < 5.92**, *or*
      **TPP ≥ 1600 with performance density ≥ 3.2 and < 5.92**
    - Calculation per the Technical Notes to 3A090.
  - **`.z` paragraphs** — items in other ECCNs that meet/exceed 3A090/4A090 parameters:
    **3A001.z, 4A003.z, 4A004.z, 4A005.z, 5A002.z, 5A004.z, 5A992.z, 5D002.z, 5D992.z.**
  - **3B001 / 3B002** — semiconductor manufacturing equipment and test equipment. The Oct-2023 rule
    folded former **3B090** into **3B001.d.1–4 and 3B001.d.6–8**. (3B993/3B994 are the AT-controlled
    analogues.) **3B001/3B002 status verified via § 734.9(k) and the K&L Gates analysis.**
  - **3D001 / 3D002** — software for the development/production/use of 3A/3B items.
  - **3E001 / 3E002** — technology per the General Technology Note for development or production of
    3A/3B/3C items. **3E001 is the ECCN that most often makes a semiconductor company's *internal
    process recipes and equipment tuning data* controlled technology — which is precisely what a fab
    monitoring product logs.**
  - **4E091** — AI model weights (the object of the § 734.9(l) FDP rule).
- **CAVEAT (honest):** I could **not** render eCFR Supplement No. 1 Category 3 directly (the deep-link
  URL 404s and Cornell's mirror 404s). The ECCN numbers and their subject matter are confirmed from
  eCFR §§ 734.9 and 744.23, which cite them; the **numeric TPP thresholds are from a law-firm
  secondary source and should be re-verified against eCFR before being vendored as provision text.**
  Mark them **UNVERIFIED-AGAINST-PRIMARY** in the corpus until re-checked.
- **Licence:** the CCL text itself is a US Government work → **VENDOR**. The K&L Gates analysis is
  **REFERENCE-ONLY** (law-firm copyright).

### 1.8 The October 2022 / 2023 / 2024 / 2025 semiconductor rules — current status as of 2026

Verified against Miller & Chevalier, *BIS Export Controls 2025 Year-in-Review and 2026 Mid-Year
Update* (**REFERENCE-ONLY**, law-firm copyright) —
<https://www.millerchevalier.com/publication/bis-export-controls-2025-year-review-and-2026-mid-year-update>

| Rule | Date | Status as of mid-2026 |
|---|---|---|
| Oct 7 2022 advanced computing / SME interim final rule | 2022-10-07 | Superseded/absorbed by later rules; foundational for 744.23 and the FDP structure |
| Oct 17 2023 revisions (3A090/4A090 TPP + performance density, `.z`, 3B090→3B001.d) | 2023-10-17 | **In force** |
| Dec 2 2024 SME rule + HBM controls | 2024-12-02 | **In force** |
| **AI Diffusion Rule** (three-tier global licensing for advanced chips + model weights) | published 2025-01-15 | **RESCINDED in policy on 2025-05-13**, but *"has yet to be formally rescinded via an update to the Code of Federal Regulations"*; BIS is on a non-enforcement posture; the 2026 regulatory plan targets formal rescission by end of FY2026 (September 2026) |
| **Due Diligence Rule** for advanced computing ICs (Approved IC Designers / Approved OSAT lists) | 2025-01-16 | **REMAINS IN EFFECT** |
| **Affiliates Rule ("50% rule")** — extends entity-list controls to ≥50%-owned foreign affiliates | published 2025-09-30 | **SUSPENDED November 2025** pending US–China negotiations; implementation pushed to **2025-11-10 → 2026-11-10** |
| Entity List churn | 2025 | +82 (Mar), +32 (Sep), +29 (Oct), −1 (Nov); **no additions/removals in H1 2026** |

**Corpus design consequence — this is important.** The AI Diffusion Rule and the Affiliates Rule are
*live examples of law that exists on paper but is not being enforced*. That is exactly the kind of
fact pattern a constitution with defeasible precedent needs as a **Tier 3 / suspended-provision**
test case: a provision that is textually in the CFR but under a non-enforcement posture. Do **not**
make either of them ABSOLUTE. Do encode them as **Tier 2 with a `status: suspended` attribute** and
use them to test whether precedent can correctly recognise suspension without inventing it.

### 1.9 BIS guidance (as distinct from regulation)

- **URL:** <https://www.bis.gov/regulations/ear> and <https://www.bis.gov/deemed-exports>
- **What is guidance, not law:** "Guidelines for Deemed Export License Applications" (PDF),
  "Don't Let This Happen To You" enforcement casebook, Export Compliance Program (ECP) guidelines,
  Know-Your-Customer / red-flag guidance, advisory opinions, training videos, the CCL Search tool,
  the Commerce Country Chart tool, and the Country Groups tool.
- **BIS's own verified definition of deemed export:** *"the sharing or release of controlled
  technology or source code to a foreign person within the United States."*
- **Licence:** US Government works → **VENDOR** (text is public domain). BIS logos/seals are
  **not** to be reproduced (agency seals are separately restricted under 18 U.S.C. § 701 — noted, not
  independently verified here).
- **Reuse:** BIS guidance is the ideal source for **Tier 3 (advisory / non-binding)** provisions.
  It is exactly the material that a precedent system *should* be allowed to soften, because BIS
  itself does not treat it as binding. Encoding the red-flag list as Tier 3 and § 744.23's knowledge
  standard as Tier 2 creates a clean, realistic gradient in the corpus.

### 1.10 ITAR (22 CFR 120–130)

- **URLs:** <https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C> ;
  § 120.34 <https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-120/subpart-C/section-120.34>
- **§ 120.34 "Public domain" — verified definition:** *"Information which is published and which is
  generally accessible or available to the public"* through eight enumerated channels: newsstand/
  bookstore sales; unrestricted subscriptions; second-class mailing privileges; public libraries;
  patents available at patent offices; unlimited distribution at public conferences/meetings/trade
  shows in the US; *"public release (i.e., unlimited distribution) in any form"* after government
  approval; and fundamental research in science/engineering at accredited US institutions where
  results are *"ordinarily published and shared broadly in the scientific community."* University
  research is excluded from public-domain status if it accepts publication restrictions or takes
  government funding with access controls.
- **Licence:** US Government work. **VENDOR.**
- **Relevance to semiconductors — be precise here.** Commercial semiconductor fab technology is
  overwhelmingly **EAR**, not ITAR. ITAR bites only for **defence-article-specific** microelectronics:
  USML **Category XI** (military electronics, including certain rad-hard and specified ASICs) and
  **Category XV** (spacecraft, including rad-hard microelectronics for space). A trusted-foundry or
  defence-adjacent product line brings ITAR into scope.
- **Why ITAR matters to the constitution even if narrow:** ITAR has **no de minimis rule and no
  "published" safe harbour equivalent to EAR § 734.18(a)(5) for cloud storage** in the same shape,
  and the ITAR deemed-export concept (22 CFR § 120.50 / § 120.33 technical data released to a foreign
  person) has historically been read as strictly as the EAR's. If any corpus scenario touches USML
  XI/XV parts, the ITAR path must be a **Tier 1 hard stop** with a narrower carve-out than the EAR
  path — that asymmetry is itself a good test of whether a precedent engine over-generalises from
  EAR cases to ITAR cases. **Recommend building at least one such trap scenario.**

---

## 2. SCREENING LISTS

### 2.1 Consolidated Screening List (CSL) — trade.gov / ITA

- **Landing:** <https://www.trade.gov/data> · **Data.gov record:**
  <https://catalog.data.gov/dataset/consolidated-screening-list-api> · **API details:**
  `https://developer.trade.gov/api-details#api=consolidated-screening-list&operation=search`
- **Contains:** a single unified feed of the restricted-party lists maintained by Commerce (BIS
  Entity List, Denied Persons List, Unverified List, Military End User List), State (AECA Debarred,
  Nonproliferation Sanctions) and Treasury (OFAC SDN and the Consolidated non-SDN lists).
- **Format:** **JSON** via the search API. trade.gov's own page states *"The output format for this
  API is JSON"* and that the data is *"updated hourly."* (The data.gov record says accrual is daily —
  the discrepancy is in the sources, not introduced here.)
- **LICENCE — VERIFIED:** the data.gov catalog record states the licence field as
  **`http://www.usa.gov/publicdomain/label/1.0/`** — the **U.S. Government Work / public domain
  label**. That is a first-party, machine-readable licence declaration.
  → **Downloadable and redistributable: YES. Safe to VENDOR.**
- **UNVERIFIED:** whether a free API key is required, current rate limits, and the exact
  developer-portal terms of service. `developer.export.gov` failed DNS resolution and
  `developer.trade.gov` was not renderable in this environment. **Do not state "no API key needed" in
  the corpus.** Treat key/rate-limit facts as unverified pending a direct check.
- **Compliance disclaimer that must be carried into the corpus (verified from trade.gov):** *"If a
  party to a user's transaction matches the name of a party on the consolidated list, the user must
  check the official publication of restricted parties in the Federal Register…"* — i.e. **the CSL is
  a convenience aggregation, not the legal list.** This is itself an excellent Tier 1 provision:
  *a screening hit may never be cleared solely on the aggregated feed.*
- **Reuse:** best used as an **oracle** (screening test fixtures with known-positive and
  known-negative names, including transliteration and alias variants), and as **factor vocabulary**
  (`entity_list`, `denied_person`, `unverified_list`, `meu`, `sdn`, `debarred`, `alt_names`,
  `federal_register_notice`).

### 2.2 BIS Entity List — Supplement No. 4 to Part 744

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744>
- **Verified structure:** a table with **Country · Entity name and address (with aliases) · License
  requirement · License review policy · Federal Register citation**. Licence requirements range up to
  *"all items subject to the EAR"*; review policies include *"Presumption of denial," "Policy of
  denial," "Case-by-case review."* Hundreds of entries across many countries (Afghanistan through
  China and beyond).
- **Footnote designations (verified):** footnote 1 → § 734.9(e) FDP; footnote 3 → § 734.9(g)
  Russia/Belarus MEU FDP; footnote 4 → § 744.11-related; footnote 5 → advanced-node IC FDP.
- **Licence:** US Government work (it is CFR text). **VENDOR.**
- **Reuse:** provision text plus a rich **oracle** — the footnote system is a real, machine-checkable
  cascade (entity listed with footnote 5 → § 734.9(e) FDP applies → items that would otherwise be
  outside the EAR become subject to it). This is the best available worked example of *rule chaining*
  in the whole corpus.

### 2.3 BIS Denied Persons List (DPL)

- **URL:** <https://www.bis.gov/denied-persons-list>
- **Format (verified):** downloadable **CSV** ("Export as CSV", e.g. `dpl_04142026.csv`) plus an
  interactive filterable web table. No TSV/text/PDF variants noted on the page. Every entry cites the
  Federal Register notice of denial and any suspension.
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** oracle + factor vocabulary (`denial_order`, `effective_date`, `expiration_date`,
  `standard_order` vs `non_standard_order`). Note that a DPL denial is an **absolute transaction bar
  with essentially no licence path**, which makes it the cleanest Tier 1 screening provision.

### 2.4 OFAC SDN List and Consolidated Sanctions List

- **URLs:** <https://ofac.treasury.gov/ofac-sanctions-lists> ; Sanctions List Service at
  `sanctionslist.ofac.treas.gov`
- **Verified from the OFAC page:** OFAC offers the **SDN List**, the **Consolidated Sanctions List
  (non-SDN lists)**, a **customised dataset tool** (build a dataset from selected lists/programs),
  documentation for the **Advanced Sanctions Data Model**, and legacy flat-file formats with a
  tutorial.
- **UNVERIFIED:** the exact filenames and download URLs (`SDN.CSV`, `SDN.XML`, `SDN_ADVANCED.XML`,
  `CONS_ADVANCED.XML`) could not be confirmed from a first-party page at the time of this survey — the OFAC
  landing page did not enumerate them and the SLS app was not renderable. Search results do reference
  an OFAC technical notice on *"Change to namespace in SDN.XML, CONSOLIDATED.XML, SDN_ADVANCED.XML,
  and CONS_ADVANCED.XML files"* (<https://ofac.treasury.gov/recent-actions/20240507_44>), which
  corroborates those filenames but was not fetched. **Mark filenames UNVERIFIED.**
- **UNVERIFIED:** explicit OFAC terms-of-use / redistribution language. None was found on the pages
  fetched. **However**, the OFAC lists are US Treasury works published in the Federal Register, so the
  §0 baseline (17 U.S.C. § 105, no US copyright) applies to the *content*. Redistribution is in
  practice universal (every sanctions-screening vendor redistributes it). **Assess as VENDOR under
  the §0 baseline, but record the licence as "public domain by 17 U.S.C. § 105; no explicit OFAC
  terms page located."** Do not claim OFAC affirmatively granted a licence.
- **Third-party mirror:** OpenSanctions publishes the US Trade CSL as a dataset
  (<https://www.opensanctions.org/datasets/us_trade_csl/>). **OpenSanctions' own licensing is CC-BY-NC
  for non-commercial use with a commercial licence otherwise — UNVERIFIED at the time of this survey, and
  therefore REFERENCE-ONLY.** Prefer the government originals.

---

## 3. CHIPS ACT

### 3.1 Statute — 15 U.S.C. § 4652 (CHIPS Act of 2022, Pub. L. 117-167 § 103)

- **URL:** <https://www.law.cornell.edu/uscode/text/15/4652>
- **Verified provisions:**
  - **§ 4652(a)(5)(C) technology clawback:** the Secretary shall recover the **full award amount** if
    a covered entity *"knowingly engages in any joint research or technology licensing effort"* with a
    foreign entity of concern involving technology that *"raises national security concerns, as
    determined by the Secretary."*
  - **§ 4652(a)(6)(C) expansion clawback / required agreement:** before receiving assistance, covered
    entities must agree that *"during the 10-year period beginning on the date of the award"* they
    will not engage in *"any significant transaction … involving the material expansion of
    semiconductor manufacturing capacity in the People's Republic of China or any other foreign
    country of concern."*
  - **§ 4652(a)(5)(B):** progressive recovery of up to the full award for missed commencement/
    completion milestones.
  - **§ 4652(a)(6)(E):** on notification of a planned violation, the Secretary must immediately
    request *"tangible proof that the planned significant transaction has ceased"* within a **45-day**
    window, else full recovery.
- **Licence:** US Government work (US Code). **VENDOR.** (Cornell LII's *annotations* are Cornell's;
  the statutory text is not.)

### 3.2 Implementing rule — 15 CFR Part 231, "Clawbacks of CHIPS Funding"

- **URL:** <https://www.ecfr.gov/current/title-15/subtitle-B/chapter-II/subchapter-C/part-231>
- **Federal Register:** final rule *Preventing the Improper Use of CHIPS Act Funding*,
  <https://www.federalregister.gov/documents/2023/09/25/2023-20471/preventing-the-improper-use-of-chips-act-funding> ;
  revised "material expansion" definition,
  <https://www.federalregister.gov/documents/2023/12/28/2023-28627/preventing-the-improper-use-of-chips-act-funding-revised-definition-of-material-expansion>
- **Verified structure:** Subpart A Definitions (§§ 231.101–231.121); Subpart B General
  (§§ 231.201–231.205); Subpart C Notification, Review, Recovery (§§ 231.301–231.308); Subpart D
  Other (§§ 231.401–231.403).
- **Verified definitions:**
  - **§ 231.104 Foreign entity of concern** — includes entities designated as terrorist
    organisations, on Treasury's **SDN list**, controlled by covered-nation governments, convicted of
    espionage or **export control violations**, on the **BIS Entity List**, on China's
    military-industrial complex list, or *"engaged in unauthorized conduct that is detrimental to
    national security."*
  - **§ 231.107 Legacy semiconductor** — 8-inch wafers or smaller; **28 nm generation or older**
    logic; DRAM with half-pitch > 18 nm; or others the Secretary identifies.
  - **§ 231.108 Material expansion** — increasing an existing facility's capacity by **more than 5%**,
    or constructing **any** new semiconductor manufacturing facility.
- **Verified prohibitions:**
  - **§ 231.202 Expansion clawback:** *"During the 10-year period beginning on the date of the award
    of Federal financial assistance, the covered entity and members of the affiliated group may not
    engage in any significant transaction involving the material expansion of semiconductor
    manufacturing capacity in a foreign country of concern."* Exceptions for existing legacy-
    semiconductor facilities and for legacy expansions serving primarily that country's market.
  - **§ 231.203 Technology clawback:** *"During the applicable term of a Federal financial assistance
    award, a covered entity may not knowingly engage in any joint research or technology licensing
    with a foreign entity of concern that relates to a technology or product that raises national
    security concerns."* Narrow exception for ongoing activities memorialised before the Secretary's
    determination.
- **Verified process:** § 231.301 notification of any planned significant transaction within the
  10-year window **regardless of any claimed exception**; § 231.302 **C-suite certification** and
  detailed party/ownership/facility/semiconductor-spec disclosure; § 231.305 Secretary has **90 days**
  to issue an initial determination, reconsideration requested within **14 days**, final determination
  within **60 days**; § 231.308 violation → **full recovery of federal assistance as debt with
  interest** from the final determination date.
- **NIST relationship:** the CHIPS Program Office sits inside **NIST**. NIST hosts the guardrails FAQ
  at <https://www.nist.gov/chips/chips-implementation-strategies/national-security/frequently-asked-questions-preventing>
  (**guidance, Tier 3**). CHIPS award security requirements in practice point at the **NIST
  cybersecurity portfolio** (CSF, SP 800-53, SP 800-171 for CUI, SP 800-161 for C-SCRM) — but note
  honestly: **Part 231 itself does not textually incorporate a named NIST framework**; the framework
  linkage runs through individual award terms and the CHIPS security requirements, which are
  **UNVERIFIED** as a published, citable, machine-readable artefact.
- **Licence:** US Government work. **VENDOR.**
- **Reuse:** Part 231 is the best source in this lane for **numeric, falsifiable thresholds** —
  5% capacity, 28 nm, 18 nm half-pitch, 8-inch wafers, 10 years, 90/14/60 days, 45 days. Numeric
  thresholds are the ideal shape for oracle test cases because they admit no interpretive drift.
  § 231.301's *"regardless of claimed exception"* notification duty is a superb **Tier 1** provision:
  it is a duty that survives even a correct belief that you are exempt.

---

## 4. NIST FRAMEWORKS

### 4.1 The NIST copyright position — VERIFIED

- **URL:** <https://www.nist.gov/open/copyright-fair-use-and-licensing-statements-srd-data-software-and-technical-series-publications>
- **Verified quotes:**
  - Technical Series publications (SP 800 series): *"Works authored by NIST employees are not subject
    to Copyright protection within the United States; foreign rights are reserved."* The public
    receives *"the non-exclusive, perpetual, paid-up, royalty-free, worldwide right to reprint works
    in all formats"* and to make derivative works. Attribution: cite in the recommended format
    followed by *"Republished courtesy of the National Institute of Standards and Technology."*
  - Software: *"The software developed by NIST employees is not subject to copyright protection
    within the United States."* Must *"keep intact this entire notice"* and *"explicitly acknowledge
    the National Institute of Standards and Technology as the source."*
  - Data: *"Works of NIST employees are not subject to copyright protection in the United States.
    This data/work may be subject to foreign copyright."* Must acknowledge NIST's creation and note
    changes with dates.
- **Consequence:** SP 800-53 Rev 5, SP 800-161r1, SP 800-218, SP 800-171r3 and CSF 2.0 are all
  **public domain in the US** and **safe to VENDOR**, subject to attribution and the foreign-rights
  caveat. **Do not use the NIST name or logo in a way implying endorsement** (the licensing page
  makes attribution mandatory but endorsement is separately restricted — treat logo use as
  prohibited).

### 4.2 NIST SP 800-53 Rev 5 / SP 800-53B — and `usnistgov/oscal-content`

- **Repo:** <https://github.com/usnistgov/oscal-content>
- **Verified contents:** OSCAL representations of the **SP 800-53 Rev 4** catalog with low/moderate/
  high baselines, and the **SP 800-53 Rev 5 + SP 800-53B** catalog with low/moderate/high baselines,
  plus other OSCAL examples. CI/CD automatically converts source content into the alternates.
- **Formats:** **XML, JSON, YAML.**
- **LICENCE — VERIFIED by fetching `LICENSE.md` directly:** *"As a work of the United States
  government, this project is in the public domain within the United States."* … *"We waive copyright
  and related rights in the work worldwide through the **CC0 1.0 Universal** public domain
  dedication."* … *"You can copy, modify, distribute and perform the work, even for commercial
  purposes, all without asking permission."* Caveat: *"In no way are the patent or trademark rights
  of any person affected by CC0"*; no warranty. Contributors agree to the same CC0 dedication.
  → **CC0 1.0. Unambiguously safe to VENDOR, including commercially and internationally.**
- **Reuse — highest-value machine-readable asset in the lane.** This is the only source here that is
  simultaneously (a) already structured as a *control catalog with baselines*, which is structurally
  isomorphic to a "constitution with provisions and profiles"; (b) CC0, so no attribution plumbing is
  needed; and (c) already has tooling. **Recommend the corpus adopt OSCAL's catalog/profile split as
  its serialisation model**: `catalog` = the full provision set, `profile` = a tier selection
  (Tier 1 baseline = the ABSOLUTE provisions), `component-definition` = a product's claimed
  implementation, `assessment-results` = the oracle output.

### 4.3 OSCAL itself

- **Repo:** <https://github.com/usnistgov/OSCAL>
- **Verified:** *"a set of hierarchical, XML-, JSON-, and YAML-based formats that provide a
  standardized representations of information pertaining to the publication, implementation, and
  assessment of security controls."* Models include catalog, profile, and (per OSCAL documentation
  generally, not enumerated on the fetched page) component-definition, SSP, assessment plan,
  assessment results, POA&M.
- **LICENCE:** a `LICENSE.md` exists but its text was **not rendered**. Given that `oscal-content`'s
  licence was verified as CC0 and NIST software policy (§4.1) is "not subject to copyright in the US,"
  the OSCAL repo is very likely the same NIST CC0 dedication — but **mark UNVERIFIED** and re-check
  `https://raw.githubusercontent.com/usnistgov/OSCAL/main/LICENSE.md` before relying on it.
- **Status:** VENDOR the *schemas* with the licence flagged unverified; the *content* in
  `oscal-content` is verified CC0.

### 4.4 NIST SP 800-161 Rev 1 (Update 1) — C-SCRM

- **URL:** <https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final> ·
  PDF <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-161r1-upd1.pdf> ·
  DOI <https://doi.org/10.6028/NIST.SP.800-161r1-upd1>
- **Verified:** *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations*,
  May 2022, **updated through 2024-11-01**, final. Covers identifying, assessing and mitigating
  cybersecurity risks throughout the supply chain at all levels — malicious functionality,
  counterfeits, poor manufacturing practices; C-SCRM strategy, implementation plans, policies, risk
  assessments, and integration into enterprise risk management.
- **Machine-readable:** the **SCRM Assessment Scoping Questionnaire (Table 26)** as `.xlsx`. No OSCAL
  catalog of 800-161 exists as such — its controls are 800-53 controls with C-SCRM enhancements, so
  the OSCAL 800-53 catalog is the machine-readable route.
- **Licence:** NIST public domain per §4.1. **VENDOR.**
- **Reuse:** the single best source of **factor vocabulary** for supply-chain provisions: `tier_1/2/3`
  (enterprise / mission / operational), `criticality analysis`, `provenance`, `traceability`,
  `counterfeit`, `supplier tiering`, `foreign ownership control or influence (FOCI)`. Mostly
  **Tier 3 advisory** — 800-161 is guidance, not a mandate, outside contract terms.

### 4.5 NIST SP 800-218 — SSDF v1.1

- **URL:** <https://csrc.nist.gov/pubs/sp/800/218/final> ·
  PDF <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf>
- **Verified:** *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for
  Mitigating the Risk of Software Vulnerabilities*, published **2022-02-03**. Supplemental material
  includes the **SP 800-218 table in Excel (.xlsx)**, delta documents (.docx), and a potential-updates
  spreadsheet. A companion **SP 800-218A** exists (generative-AI profile).
- **Note:** the four practice groups **PO (Prepare the Organization), PS (Protect the Software),
  PW (Produce Well-Secured Software), RV (Respond to Vulnerabilities)** are the standard SSDF
  structure but were **not confirmed from the fetched page** — mark **UNVERIFIED-AGAINST-PRIMARY**
  (they are stated in the PDF itself, which was not fetched).
- **Licence:** NIST public domain per §4.1. **VENDOR.**
- **Reuse:** the SSDF is the natural **Tier 2 / Tier 3 backbone for software-change provisions** — it
  is about *how you change software*, which is precisely the corpus's subject matter. PW.7 (code
  review), PW.8 (testing), PS.1 (protect all forms of code from unauthorised access and tampering),
  PS.3 (archive and protect each software release) map directly onto the export-control record and
  access provisions. **PS.1 is the SSDF practice that intersects deemed exports most directly.**

### 4.6 NIST SP 800-171 Rev 3 — CUI

- **URL:** <https://csrc.nist.gov/pubs/sp/800/171/r3/final> ·
  PDF <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171r3.pdf>
- **Verified:** *Protecting Controlled Unclassified Information in Nonfederal Systems and
  Organizations*, final **2024-05-14**, **17 control families** (Access Control; Awareness and
  Training; Audit and Accountability; Assessment, Authorization and Monitoring; Configuration
  Management; Identification and Authentication; Incident Response; Maintenance; Media Protection;
  Physical and Environmental Protection; Planning; Personnel Security; Risk Assessment; System and
  Services Acquisition; System and Communications Protection; System and Information Integrity;
  **Supply Chain Risk Management**).
- **Machine-readable:** **"800-171r3 Dataset on CPRT"**, an HTML version, the CUI Overlay (.xlsx), and
  a Rev2→Rev3 comparison spreadsheet.
- **Companions:** SP 800-171A Rev 3 (assessment), SP 800-172 Rev 3 (enhanced).
- **UNVERIFIED:** the page as fetched did not reference 32 CFR Part 2002, CMMC, or DFARS
  252.204-7012. The CUI-programme and DFARS linkage is real but should be cited to 32 CFR Part 2002
  and DFARS directly, not to this page.
- **Licence:** NIST public domain per §4.1. **VENDOR.**
- **Reuse:** **CUI is the bridge concept** between export control and cybersecurity for this corpus.
  The CUI registry contains the category **"Export Controlled" (CUI//SP-EXPT)** — the marking that
  appears on the leaked BIS draft in one of the search results above. Once ECCN-controlled technical
  data lands in a log, that log is CUI//SP-EXPT and 800-171's audit, media-protection and
  access-control families attach to it. That chain — *3E001 technology → written to log → log is
  CUI//SP-EXPT → 800-171 AU/MP/AC families apply → and a non-US-person with log read access is a
  deemed export* — is the **spine of the whole constitution**. Build it explicitly.

### 4.7 NIST CSF 2.0 and its machine-readable forms

- **Informative references:** <https://www.nist.gov/cyberframework/informative-references>
- **Verified:** all informative references downloadable as **Excel** from
  `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all` (note the URL path
  says `json` but the page describes the download as Excel — both may be served); translations in
  11+ languages; the **CSF 2.0 Reference Tool** at
  <https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters>; the **Informative
  Reference Catalog (OLIR)** at <https://csrc.nist.gov/projects/olir/informative-reference-catalog#/>;
  comparison reports at <https://csrc.nist.gov/Projects/olir/Coverage-Report#/olir/coverage-report>.
- **CPRT:** <https://csrc.nist.gov/projects/cprt> — verified as *"a simple way to access reference
  data from various NIST cybersecurity and privacy standards, guidelines, and Frameworks"*,
  **downloadable in XLSX and JSON**. The specific catalog list was not enumerated on the overview
  page (**UNVERIFIED** which exact publications are in CPRT beyond 800-171r3, which its own page
  confirms).
- **OSCAL form of CSF 2.0:** **UNVERIFIED / likely does not exist officially.** The NIST informative-
  references page did not mention OSCAL, and `usnistgov/oscal-content` contains 800-53 catalogs, not
  CSF. A community project (CyberESI's "OSCAL CPRT Catalog Project") appeared in search results but
  is **third-party, licence UNVERIFIED → REFERENCE-ONLY.** **Do not claim an official CSF 2.0 OSCAL
  catalog exists.**
- **Licence:** NIST public domain per §4.1 for NIST-authored CSF content. **CAUTION:** OLIR
  informative references frequently **map to third-party copyrighted frameworks** (CIS Controls,
  ISO/IEC 27001, COBIT). The *mapping* is NIST's; the *mapped-to control text* is not. **Vendor the
  CSF core and NIST-authored mappings; do NOT vendor ISO/CIS/COBIT control text.** This is exactly
  the §0 third-party-material caveat biting.
- **Reuse:** CSF 2.0 Functions (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) are the best
  available **top-level taxonomy** for organising provisions. **Tier 3 advisory** — CSF is explicitly
  voluntary.

---

## 5. DATA SOVEREIGNTY

### 5.1 GDPR — Regulation (EU) 2016/679

- **URL:** <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng> · CELEX `32016R0679` · ELI
  `eli/reg/2016/679/oj/eng` · Document date 2016-04-27, OJ publication 2016-05-04.
- **Formats:** HTML, PDF, and XML (Formex) via EUR-Lex; all 24 official languages.
- **LICENCE — VERIFIED, with an important nuance:**
  - The **European Commission's** legal notice (<https://commission.europa.eu/legal-notice_en>)
    states: *"The Commission's reuse policy is implemented by the Commission Decision of 12 December
    2011 on the reuse of Commission documents"* (i.e. **Decision 2011/833/EU**) and that EU-owned
    content *"is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0)
    licence"* requiring that *"appropriate credit is given and changes are indicated."* Commercial
    reuse is permitted. Excluded: content depicting identifiable individuals, third-party works, and
    **industrial property rights — patents, trademarks, registered designs, logos and names.**
  - The **Publications Office** notice
    (<https://op.europa.eu/en/web/about-us/legal-notices/publications-office-of-the-european-union-copyright>)
    states *"© European Union, 2026"*, that editorial content is *"licensed under the Creative
    Commons Attribution 4.0 International licence"* with the obligation to *"acknowledge the source
    and indicate any changes"*, and excludes third-party IP, industrial-property-protected material,
    logos and names.
  - **HONEST CAVEAT:** the Publications Office page as rendered **did not itself cite Decision
    2011/833/EU**, and the **EUR-Lex-specific legal notice could not be rendered** (both
    `eur-lex.europa.eu/content/legal-notice/legal-notice.html` and the `/content/help/...` variant
    returned only navigation chrome). So: *the CC BY 4.0 + 2011/833/EU basis is verified for
    Commission documents and for Publications Office editorial content; it is **not** independently
    verified from the EUR-Lex page that OJ legislative text specifically carries CC BY 4.0.*
  - **Separate and important:** under **Article 5 of the Berne Convention as implemented in EU
    Member State law and Article 2(4) of the Copyright Directive tradition, official legislative
    texts are generally excluded from copyright altogether.** In practice EU legislation is reused
    freely and universally. **Recommendation for the corpus: record GDPR's status as "CC BY 4.0 per
    Decision 2011/833/EU (Commission/OP notices verified; EUR-Lex-specific notice unrendered) —
    attribute '© European Union, <year>, https://eur-lex.europa.eu' and note that only the OJ
    version is authentic." Treat as safe to VENDOR with attribution.**
- **Reuse for this corpus:** GDPR Art. 5 (principles), Art. 15 (access), **Art. 17 (erasure)**,
  Art. 25 (data protection by design), Art. 30 (records of processing), Art. 32 (security), Art. 33/34
  (breach notification), **Chapter V Arts 44–49 (transfers)**, and **Art. 48 (transfers not authorised
  by Union law — the anti-foreign-order provision)**.
- **The provision that makes this corpus interesting:** **GDPR Art. 17 erasure vs EAR § 762.6
  five-year retention and litigation hold.** These genuinely conflict for personal data embedded in
  export records (the names of the foreign persons who accessed controlled technology — which
  § 762.5(b)(4) *requires* you to log). This is the corpus's best **hard-case generator**: two Tier 1
  obligations from two jurisdictions pointing opposite ways. GDPR Art. 17(3)(b) (compliance with a
  legal obligation) resolves it in the EU's own terms only for EU-law obligations, not US ones — so
  the conflict is real, not merely apparent. **Build at least three scenarios on this seam.**

### 5.2 China — Data Security Law (DSL), PIPL, "important data", state secrets

- **Translation used:** DigiChina (Stanford), *Translation: Data Security Law of the People's
  Republic of China (Effective Sept. 1, 2021)* —
  <https://digichina.stanford.edu/work/translation-data-security-law-of-the-peoples-republic-of-china/>
  and *Translation: Outbound Data Transfer Security Assessment Measures (Effective Sept. 1, 2022)* —
  <https://digichina.stanford.edu/work/translation-outbound-data-transfer-security-assessment-measures-effective-sept-1-2022/>
- **Verified key articles (from the DigiChina translation):**
  - **Art. 21** — data classification/grading by importance to economic and social development and
    the harm from compromise; **"core national data"** covering *"national security, the lifelines of
    the national economy, important aspects of people's livelihoods"* receives stricter protection.
  - **Art. 30** — important-data handlers must conduct periodic risk assessments and report to
    authorities.
  - **Art. 31** — cross-border transfer: CIIOs follow the Cybersecurity Law's outbound rules; rules
    for other important-data handlers are *"jointly formulated by the national cybersecurity and
    informatization department and relevant departments"* (i.e. CAC).
  - **Art. 36 (verbatim):** *"Domestic organizations and individuals must not provide data stored
    within the mainland territory of the PRC to the justice or law enforcement institutions of
    foreign countries without the approval of the competent authorities."*
- **LICENCE — UNVERIFIED AND THIS ONE MATTERS.** The DigiChina page carries **no visible Creative
  Commons licence, copyright notice, or reprint policy** — only the standard Stanford footer
  (Terms of Use / Privacy / Copyright / Trademarks) and a contact address `digichina@stanford.edu`.
  → **REFERENCE-ONLY.** Do **not** vendor DigiChina translation text into the corpus without written
  permission. Cite and paraphrase; link out.
- **The official Chinese text** (NPC Observer / `npc.gov.cn`) is a PRC state work. PRC Copyright Law
  Art. 5 excludes *"laws; regulations; resolutions, decisions and orders of State organs"* and their
  official translations from copyright — **UNVERIFIED here** (not fetched), so mark it as such.
  **Practical recommendation: vendor no Chinese-law text at all. Use paraphrased obligations as
  provisions, cite the article number, and mark the source REFERENCE-ONLY.**
- **Reuse:** Art. 36 is a genuine **Tier 1 ABSOLUTE** for any product with a PRC deployment, and it
  sits in direct conflict with a US subpoena or a BIS § 762.7 production demand — a second
  irreducible cross-jurisdiction conflict, and the mirror image of EU Data Act Art. 32 (§5.4).
- **"Important data" / state secrets:** the *catalogue* of important data is sector- and
  province-specific and much of it is itself non-public; the **Law on Guarding State Secrets**
  (revised 2024) adds a "work secrets" concept. **UNVERIFIED / largely unpublished.** For the corpus,
  encode "important data" as a **factor with an unknowable extension** — which is itself a valuable
  test: can the constitution behave correctly when a factor's membership is not determinable?

### 5.3 Taiwan and South Korea — semiconductor technology protection

**Taiwan — National Security Act (as amended 2022) and related**
- **Primary text:** Laws & Regulations Database of the ROC,
  <https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=A0030028> — **could not be fetched
  (robots.txt disallowed).** Licence and the standard "translation for reference only, Chinese
  governs" disclaimer are therefore **UNVERIFIED.**
- **Verified via secondary source** (law.asia, *Taiwan's cross-border semiconductor controls*,
  <https://law.asia/taiwan-semiconductor-export-controls/> — **REFERENCE-ONLY**):
  - **National Security Act Art. 3** prohibits conduct involving **"national core critical technology
    trade secrets"** for foreign benefit — obtaining by improper means, unauthorised use/disclosure,
    or acquiring unlawfully obtained secrets. (Penalties under the amended NSA are substantially
    higher than ordinary trade-secret penalties; the exact figures were **not verified** — the
    law.asia piece cites a different act's NTD 3 million / 5-year figure, which should not be
    attributed to NSA Art. 3.)
  - **The Executive Yuan's list of National Core Key Technologies** (first published 2023-12-05 with
    **22 items** across national defence, space, agriculture, semiconductors, and information/
    communications security — verified via Formosa Transnational,
    <https://www.fblaw.com.tw/insights-en/legal-news-2024-1-22>, **REFERENCE-ONLY**; expanded to
    **32 items as of end-2024** per law.asia) **includes semiconductors: sub-14 nm chip manufacturing
    processes, advanced heterogeneous integration packaging, high-performance AI chip design, and
    low-temperature semiconductor circuit design/fabrication.**
  - **Industrial Innovation Act Art. 22** (amended April 2025) requires prior approval for outbound
    investments involving designated countries/regions or specified industries/technologies;
    **Art. 67-3** provides administrative fines and rectify/withdraw orders.
  - **NOT VERIFIED:** NSA Art. 8 extraterritoriality, and the Act Governing Relations between the
    People of the Taiwan Area and the Mainland Area Art. 9 travel/employment approval for persons
    involved in national core key technologies. Both are real but were not confirmed when this survey was compiled.
- **Live enforcement signal (2026):** English CommonWealth reports a landmark NSA conviction of former
  TSMC engineers over 2 nm trade secrets (<https://english.cw.com.tw/article/article.action?id=4737>,
  2026-04-27) — **REFERENCE-ONLY, news copyright.** Useful as scenario inspiration, not as text.
- **Verdict:** **REFERENCE-ONLY.** Encode Taiwan obligations as paraphrased provisions citing article
  numbers. **The sub-14 nm line is the most operationally useful fact:** it is a bright-line numeric
  threshold, like § 231.107's 28 nm, and the two thresholds *differ*, which is a wonderful trap for a
  precedent engine that over-generalises "the node threshold."

**South Korea — Act on Prevention of Divulgence and Protection of Industrial Technology**
- **Primary English text:** Korea Legislation Research Institute,
  <https://elaw.klri.re.kr/eng_service/lawTwoView.do?hseq=24351> ; also the Korean Law Information
  Center, <https://law.go.kr/LSW/lsInfoP.do?lsiSeq=210175&chrClsCd=010203&urlMode=engLsInfoR&viewCls=engLsInfoR>
- **Verified provisions (from the KLRI English text):**
  - **Art. 2 definition of "national core technology" (verbatim):** *"technology designated under
    Article 9, which has high technological and economic values in the Korean and overseas markets or
    brings high growth potential to its related industries and is feared as a technology to exert a
    significantly adverse effect on the national security and the development of the national economy
    in the event that it is divulged abroad."*
  - **Art. 11(1)** — institutions must **obtain approval** from the responsible Minister before
    exporting national core technology **developed with state subsidies**.
  - **Art. 11(4)** — possessors of core technology developed **without** government support must
    **report in advance** to the Minister.
  - **Art. 14 prohibited acts** — acquiring technology by *"theft, deception, threat and other unjust
    methods"*; divulging by persons under confidentiality obligations; acquiring/using while knowing
    of illegal acquisition; **exporting without proper approval**; failing to comply with ministerial
    orders.
- **LICENCE — UNVERIFIED.** No explicit translation-status disclaimer or copyright/terms statement was
  visible on the fetched KLRI page. KLRI translations conventionally carry a "for reference only, the
  Korean original governs" disclaimer. **REFERENCE-ONLY.**
- **CSET (Georgetown)** publishes its own original English translation of the Jan-2023 amended act
  (<https://cset.georgetown.edu/publication/act-on-prevention-of-divulgence-and-protection-of-industrial-technology-abbreviated-act-on-protection-of-industrial-technology/>).
  **Verified: no licensing statement is visible on that page either → REFERENCE-ONLY.** Semiconductors
  are not named in the excerpted portion; the semiconductor entries live in the MOTIE **designation
  notice** of national core technologies, not in the act.
- **Reuse:** the **approval vs report** distinction (Art. 11(1) vs 11(4), keyed on whether the
  technology was state-funded) is a superb **provenance-dependent obligation** — the same technical
  data carries a different legal duty depending on its funding history. That maps exactly onto a
  software system that must track *data lineage*, and it is the Korean analogue of the ITAR
  fundamental-research funding carve-out (§1.10). **Strongly recommend a scenario on this.**

### 5.4 EU Data Act — Regulation (EU) 2023/2854, Article 32

- **URLs:** <https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng> ;
  readable article view (third-party, **REFERENCE-ONLY**) <https://www.eu-data-act.com/Data_Act_Article_32.html>
- **Verified content of Art. 32 (international governmental access and transfer of non-personal
  data):**
  - **(1)** Providers of data processing services must take *"technical, organisational and legal
    measures, including contracts"* to prevent third-country governmental access/transfer of
    non-personal data held in the Union where that would conflict with Union or Member State law.
  - **(2)** A third-country court order or administrative decision is enforceable only if *"based on
    an international agreement, such as a mutual legal assistance treaty"* between the requesting
    country and the Union or a Member State.
  - **(3)** Absent a treaty, the provider may comply only if **three cumulative conditions** hold:
    (i) the third-country system requires reasons and proportionality and the decision is *"specific
    in character"* (linked to identified persons or violations); (ii) the addressee's objection is
    *"subject to a review by a competent third-country court or tribunal"*; (iii) that court is
    empowered to *"take duly into account the relevant legal interests"* protected by Union or
    Member State law. Providers may consult national authorities on national-security, trade-secret
    or IP concerns.
- **Licence:** EU CC BY 4.0 per §5.1 (same caveat). **VENDOR with attribution.**
- **Reuse — this is the sharpest conflict in the corpus.** EU Data Act Art. 32 and PRC DSL Art. 36 are
  *structurally identical anti-foreign-order provisions pointing in opposite directions*, and both
  collide with **EAR § 762.7** (BIS inspection/production and subpoena power). A semiconductor
  supply-chain monitoring platform with EU, PRC and US footprints is subject to all three
  simultaneously and there is no compliant configuration that satisfies all three for the same data.
  **This is the corpus's canonical impossible case — and the correct constitutional answer is not
  "pick one" but "the architecture must never create the data-location state in which all three
  attach at once."** That is a *design-time* Tier 1 provision, not a runtime one. It is the most
  intellectually interesting provision in the lane and should be authored deliberately.

### 5.5 EU Chips Act — Regulation (EU) 2023/1781

- **URL:** <https://eur-lex.europa.eu/eli/reg/2023/1781/oj/eng> · full text
  <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1781>
- **Verified (partly from recitals — the article-numbered detail below the recitals did not render
  fully, so article numbers are approximate and flagged):**
  - Chips for Europe Initiative: virtual design platform; **advanced pilot lines**; quantum chip
    development; at least one **competence centre per Member State**; the **Chips Fund** under
    InvestEU.
  - **Chapter IV monitoring and crisis response:** strategic mapping of supply-chain dependencies and
    bottlenecks; **early-warning indicators** including *"atypical increases in lead time"* and price
    fluctuations; Commission monitoring of semiconductor value chains minimising administrative
    burden; *"standardised and secure means"* for confidential data collection; Member States maintain
    **contact lists** of undertakings for **voluntary** information requests; **priority-rated orders**
    obligations for Integrated Production Facilities and Open EU Foundries during a crisis.
  - **Art. 27** governs sensitive information: ownership, protection, security, exploitation and
    dissemination of results per Horizon Europe / Digital Europe; handling of sensitive information,
    security, confidentiality, trade-secret and IP protection governed by Union law including
    **Directive (EU) 2016/943** (trade secrets) and **Directive 2004/48/EC** (IP enforcement).
    Recital 43 targets *"IP theft, unauthorised copying, forced technology transfers, economic
    espionage."*
  - **Verified negative finding:** the Regulation imposes **no direct software-implementation
    obligation** and mandates no particular monitoring software. Undertakings face **voluntary**
    information requests, contact-list registration, and confidentiality duties.
- **Licence:** EU CC BY 4.0 per §5.1. **VENDOR with attribution.**
- **Reuse:** mostly **Tier 3 advisory**, with one genuine **Tier 2**: the priority-rated-order
  obligation for IPF/Open-EU-Foundry-designated undertakings during a declared crisis. The
  early-warning indicators (`lead_time_anomaly`, `price_volatility`, `inventory_days`) are directly
  usable **factor vocabulary for a supply-chain monitoring product** — arguably the most
  domain-specific vocabulary in the whole lane.

---

## 6. OPEN POLICY-AS-CODE IMPLEMENTATIONS

**Headline finding, stated plainly: there is no mature open-source policy-as-code library for export
control or data residency.** I searched specifically for OPA/Rego export-control and trade-compliance
policy libraries and found none of substance. This is a **gap the corpus can fill**, and it is worth
saying so in the paper: the compliance-as-code ecosystem has thoroughly covered *host hardening* and
*cloud configuration* and has essentially **not** covered *trade law*.

| Project | URL | What it is | Format | Licence (verified?) | Use |
|---|---|---|---|---|---|
| **usnistgov/oscal-content** | <https://github.com/usnistgov/oscal-content> | SP 800-53 r4/r5 + 800-53B catalogs and low/mod/high baselines | XML, JSON, YAML | **CC0 1.0 — VERIFIED** by fetching `LICENSE.md` | **VENDOR.** Serialisation model + provision text |
| **usnistgov/OSCAL** | <https://github.com/usnistgov/OSCAL> | The OSCAL schemas/models themselves | XML/JSON/YAML schemas | `LICENSE.md` exists but **UNVERIFIED** (not rendered) | VENDOR schemas, re-verify licence |
| **ComplianceAsCode/content** | <https://github.com/ComplianceAsCode/content> | Security policy content for RHEL, Fedora, Ubuntu, Debian, SLES, Firefox; profiles incl. NIST, OSPP, PCI-DSS, CIS, STIG, HIPAA, USGCB | SCAP (XCCDF, OVAL, source data streams), Ansible playbooks, Bash remediation, CEL for Kubernetes/OpenShift | **BSD-3-Clause — VERIFIED** by fetching `LICENSE`: *"SPDX license identifier: BSD-3-Clause / Copyright (c) 2012-2017, Red Hat, Inc."* | **VENDOR** with BSD notice. Best available **oracle**: machine-checkable rules with known-good/known-bad states. Note: it has **no CUI/800-171-specific profile confirmed** on the fetched page — the NIST logo appears but the named profiles are OSPP/PCI-DSS/CIS/STIG/HIPAA/USGCB. **Mark 800-171 profile presence UNVERIFIED.** |
| **Open Policy Agent (OPA)** | <https://github.com/open-policy-agent/opa> | General-purpose policy engine; Rego | Rego | Apache-2.0 (**UNVERIFIED in-session** — not fetched, but it is the well-known OPA licence) | **VENDOR the engine.** No relevant policy content exists |
| **open-policy-agent/library** | <https://github.com/open-policy-agent/library> | The OPA "standard library" of example policies | Rego | **UNVERIFIED** | Reference. Contains no export-control or data-residency policies |
| **Cedar** | <https://github.com/cedar-policy/cedar> | Authorisation policy language (RBAC/ABAC), with a validator against a declared schema | Cedar policy language | **Apache-2.0 — VERIFIED** from the repo page | **VENDOR the engine.** Verified: ships **no** compliance or data-residency policy libraries; `cedar-examples` contains only app-integration demos (TinyTodo). Cedar's *schema validator* is nonetheless the closest existing analogue to "typed provisions with a checkable factor vocabulary" |
| **oscal-compass/compliance-trestle** | <https://github.com/oscal-compass/compliance-trestle> | Python tooling to author, validate and govern OSCAL documents in git, with CI/CD integration; markdown and drawio authoring; format conversion into OSCAL | JSON/YAML (XML planned) | **Apache-2.0 — VERIFIED** from the repo page | **VENDOR.** A **CNCF sandbox project**; independent of NIST though originally contributed by IBM. The natural toolchain if the corpus adopts OSCAL |
| **OpenSanctions US Trade CSL** | <https://www.opensanctions.org/datasets/us_trade_csl/> | Third-party normalised mirror of the CSL | JSON/CSV/FtM | **UNVERIFIED** (OpenSanctions uses CC-BY-NC + commercial licensing) | **REFERENCE-ONLY.** Use the government original |
| CyberESI "OSCAL CPRT Catalog Project" | <https://cyberesi-cg.com/oscal-cprt-catalog-project/> | Third-party OSCAL renderings of CPRT catalogs (incl. CSF) | OSCAL | **UNVERIFIED** | **REFERENCE-ONLY** |
| Secure Controls Framework (SCF) | <https://securecontrolsframework.com/free-content/scf-download> | Third-party crosswalk incl. NIST OSCAL JSON & Excel | JSON/XLSX | **UNVERIFIED** (SCF uses a custom "free but attribution/no-resale" licence) | **REFERENCE-ONLY** |

---

## 7. RECOMMENDED PROVISION TIERING FOR THE SEMICONDUCTOR SUPPLY-CHAIN SOFTWARE CONSTITUTION

### Design principle for what makes a provision ABSOLUTE

A provision belongs in Tier 1 only if **all four** hold:

1. **Statutory, not guidance** — it is in the CFR, U.S. Code, or an equivalent foreign statute, not in
   an agency FAQ, a NIST SP, or a framework.
2. **No business-justification defence exists in the source law** — the statute admits licences and
   exceptions *ex ante*, but admits no *ex post* "we had a good reason" defence.
3. **Violation is strict or near-strict liability, or is criminal** — the EAR's "knowledge" standard
   includes conscious disregard, so *deliberate ignorance is itself the violation*; this is the
   opposite of a balancing test.
4. **It is architecturally decidable** — a software system can be built so the violation is
   *impossible*, not merely *detected*. If a provision can only be checked after the fact, it is
   Tier 2 at best.

Criterion 4 is the one that matters most for a *software* constitution and it is what justifies
treating some provisions as design-time floors rather than runtime checks.

---

### TIER 1 — ABSOLUTE / NON-DEROGABLE

No business justification, no cost argument, no schedule pressure, and **no accumulated precedent**
may soften these. A precedent line that erodes any of them is, by construction, wrongly decided.

**T1-A. Deemed-export access control on ECCN-controlled technology.**
*Source:* EAR § 734.13(a)(2) and (b) (verbatim, §1.1); reinforced by § 764.2(b) and (e).
*Provision:* No foreign person shall obtain access to, or be placed in a position permitting access
to, "technology" or source code classified under a controlled ECCN (3D001, 3E001, and any `.z`
paragraph among others) absent a licence or a documented licence exception. Access includes read
access to any store, view, index, cache, replica, backup, screen-share, or support session.
*Why ABSOLUTE:* it is a strict-liability export the instant access is *possible*, with no border
crossing required and no post-hoc justification available. Criminal exposure under 50 U.S.C. § 4819.
And it is architecturally decidable — you can build a system in which a non-licensed foreign person
*cannot* be granted the role. A "we needed the on-call coverage" argument is not a defence; it is the
violation. **This is the provision the entire lane exists to establish.**

**T1-B. ECCN-controlled technical data must not enter general-purpose logs, telemetry or error
reporting.**
*Source:* § 734.13 combined with § 764.2(b) ("permit, or approve"); CUI//SP-EXPT handling under
SP 800-171r3 media protection and audit families.
*Provision:* Process recipes, equipment tuning parameters, yield-defect signatures, and any other data
classified under 3E001/3D001 shall never be written to a log, trace, metric label, exception payload,
crash dump, analytics event, or LLM prompt/context that is readable by a principal not cleared for
that ECCN, or that is replicated outside the controlled boundary.
*Why ABSOLUTE:* this is the single most common real-world failure mode and the least visible.
Logs are the default-permissive surface of every system: they are read by the widest audience, shipped
to the most third parties, retained the longest, and reviewed by the fewest lawyers. A stack trace
containing a chamber recipe, forwarded to a SaaS observability vendor and read by an offshore SRE, is
a completed deemed export *and* an unlicensed export, with no remediation available — you cannot
un-export. Because there is no rollback, detection is worthless and only prevention counts, which
makes it Tier 1 rather than Tier 2. **Corollary that must be stated in the provision: no exception may
be granted "temporarily for debugging."**

**T1-C. Export-record immutability and actor attribution.**
*Source:* EAR § 762.5(b)(4) — *"The system must preserve the initial image … and record all changes,
who made them and when they were made"* — plus § 762.5(b)(8) (*"where, when, by whom, and on what
equipment"*), § 762.6 (five-year retention), § 764.2(i) (no alteration of export control documents),
§ 764.2(g) (no falsification or concealment of material fact).
*Provision:* Records within § 762.2 scope shall be append-only. Corrections shall be recorded as new
entries preserving the prior state; no destructive update or hard delete of a retained export record
is permitted by any code path, migration, admin tool, or operator. Every write shall carry actor
identity, timestamp, and originating system.
*Why ABSOLUTE:* this is a rare case where the statute *itself* mandates the data structure, not merely
the outcome. § 764.2(i) makes alteration an independent violation regardless of intent to deceive, and
§ 762.5(b)(4)'s "preserve the initial image and record all changes" is, read literally, an append-only
log with attribution. Business justifications for mutability — storage cost, GDPR erasure, "the record
was wrong", schema migration convenience — are all foreseeable and all insufficient. **Note the
interaction with T1-F: the tension with GDPR Art. 17 is real and is resolved by never putting
erasable-by-right personal data in the immutable store in the first place, i.e. by design, not by
adjudication.**

**T1-D. Litigation / regulatory hold overrides every retention and deletion policy.**
*Source:* EAR § 762.6 — records subject to a formal or informal BIS (or other agency) request
*"may not be destroyed or disposed of without the written authorization"* of that agency; § 762.7.
*Provision:* On receipt of a hold, all automated expiry, retention-policy deletion, anonymisation,
and erasure-request processing for the covered records shall halt and shall not resume without written
authorisation.
*Why ABSOLUTE:* it is a duty that attaches on an *informal* request, and the only lawful release is
written agency authorisation. There is no proportionality test, no cost defence, and precedent cannot
create one. Its absoluteness is textual.

**T1-E. Screening hits shall not be cleared on the aggregated feed alone; and DPL denials are
transaction-fatal.**
*Source:* trade.gov CSL disclaimer (verified, §2.1) requiring the user to check the official Federal
Register publication; Supplement No. 4 to Part 744; the DPL.
*Provision:* A positive or possible match against a restricted-party list shall block the transaction
until resolved against the official Federal Register / CFR publication by a human with recorded
identity and rationale. No auto-clear, no confidence-threshold bypass, no "the API was down so we
proceeded" path.
*Why ABSOLUTE:* § 764.2(b) makes the *system* an aider and abettor if it permits or approves the
transaction. A denied-person transaction has essentially no licence path. Fail-open on a screening
check is a design defect that no business justification cures — the correct behaviour when the feed is
unavailable is to **stop**, and that must not be negotiable, because "the feed was down and the
shipment was urgent" is exactly the justification that will otherwise be accepted every time.

**T1-F. No circumvention path, ever.**
*Source:* EAR § 764.2(h) (intent to evade), (g) (false or misleading representation, falsification or
concealment of material fact), (c) (solicitation and attempt).
*Provision:* No feature, configuration, admin override, feature flag, emergency mode, or documented
workaround shall exist whose effect is to complete a transaction that a control would otherwise block,
or to represent a control as having run when it did not.
*Why ABSOLUTE:* evasion is a standalone violation independent of whether the underlying transaction
would have been licensable. A break-glass path *is* the evasion mechanism, however well-intentioned.
This provision is what prevents precedent from hollowing out every other provision by accretion of
"just this once" exceptions — it is the constitution's self-defence clause.

**T1-G. Encryption-carve-out integrity (conditional Tier 1).**
*Source:* EAR § 734.18(a)(5) and (b), verbatim in §1.4.
*Provision:* Where the system relies on the § 734.18(a)(5) carve-out to move or store controlled
technology, then all three conditions are simultaneously non-negotiable: FIPS 140-2/140-3-validated
modules, genuine end-to-end encryption with **no third party holding the means of decryption**
(explicitly excluding provider-managed KMS, escrow, and any decrypt-to-index pipeline), and no
intentional storage in a Country Group D:5 country.
*Why ABSOLUTE despite being conditional:* the carve-out is all-or-nothing. Partial compliance does not
yield partial protection — it yields an unlicensed export. "We used the cloud provider's default
encryption" is the standard, and standardly fatal, failure. A constitution should express this as a
**precondition lock**: invoking the carve-out asserts all three conditions, and asserting falsely is a
§ 764.2(g) violation on top of the export violation.

**T1-H. Cross-border government-access architecture (design-time floor).**
*Source:* PRC DSL Art. 36 (verbatim, §5.2); EU Data Act Art. 32(1)–(3) (§5.4); EAR § 762.7.
*Provision:* The system shall not be architected such that a single data store is simultaneously
subject to PRC DSL Art. 36, EU Data Act Art. 32, and EAR § 762.7 production. Data location and
replication topology shall be constrained so that no lawful order from one jurisdiction compels an act
unlawful in another.
*Why ABSOLUTE and why design-time:* this is the one obligation in the lane that **cannot be satisfied
at runtime at all**. Once the data is in the conflicted state, every available action is unlawful
somewhere; adjudication cannot produce a compliant outcome, only a choice of which law to break.
Therefore the only place the obligation can bind is at design time, and it must bind absolutely,
because the entire cost of compliance is front-loaded into architecture decisions that business
pressure will otherwise defer. **This is the most novel Tier 1 provision in the lane and the one most
worth writing about.**

---

### TIER 2 — DEFEASIBLE

Binding by default; may be overcome by a documented licence, exception, or a recorded and reviewable
justification. These are where precedent legitimately does work.

- **T2-1. FDP determination** (§ 734.9, all subsections) — genuinely admits licences and exceptions;
  the two-part product/country test is a defeasible classification, not a floor.
- **T2-2. § 744.23 end-use licence requirement** — the "knowledge" standard is defeasible by a
  documented, reasonable, contemporaneous due-diligence record. Note the *headquarters* test for
  advanced computing items (not ship-to) as a factor.
- **T2-3. ECCN classification itself** — classification is a judgement; a reasoned CCATS or
  self-classification rationale is a legitimate defeater. But the *consequences* of the classification,
  once made, are Tier 1.
- **T2-4. CHIPS Part 231 notification of significant transactions** (§ 231.301) — defeasible only as
  to *analysis*, never as to *notification*: the duty to notify applies *"regardless of claimed
  exception."* Encode as Tier 2 with a Tier 1 notification kernel.
- **T2-5. Korea Art. 11 export approval / report** — approval vs report depends on the funding
  provenance of the technology; the obligation is defeasible by ministerial approval.
- **T2-6. Taiwan NSA Art. 3 / national core key technologies (sub-14 nm)** — jurisdiction-conditional.
- **T2-7. GDPR Chapter V transfer obligations** (Arts 44–49) — the whole Chapter is a structured
  system of defeaters (adequacy, SCCs, BCRs, derogations). Textbook Tier 2.
- **T2-8. EU Chips Act priority-rated orders** for designated IPF/Open EU Foundry undertakings during a
  declared crisis.
- **T2-9. SP 800-171r3 control families** where CUI is present — binding via contract (DFARS/CMMC),
  and contractual obligations are defeasible by the contract itself.
- **T2-10. EU Data Act Art. 32(3)'s three cumulative conditions** — literally a defeasibility test with
  enumerated conditions; ideal Tier 2 exemplar.
- **T2-11. Affiliates Rule and AI Diffusion Rule** — encode with `status: suspended` /
  `status: non-enforced` and the dates from §1.8. These test whether a system can represent *law that
  is on the books but not in force*, which is a real and under-modelled state.

---

### TIER 3 — ADVISORY / NON-BINDING

Should inform decisions; may be departed from with reasons; precedent may legitimately narrow them.

- BIS guidance: red flags / Know Your Customer, "Don't Let This Happen To You", Export Compliance
  Program guidelines, deemed-export application guidelines, advisory opinions.
- NIST CSF 2.0 (explicitly voluntary) — best used as the **organising taxonomy** (GOVERN, IDENTIFY,
  PROTECT, DETECT, RESPOND, RECOVER) rather than as obligations.
- NIST SP 800-161r1 C-SCRM practices — guidance absent contract incorporation; excellent factor
  vocabulary.
- NIST SP 800-218 SSDF practices — guidance; the natural Tier 3 backbone for *software-change*
  provisions specifically, with **PS.1 (protect code from unauthorised access and tampering)** as the
  practice that most directly serves T1-A and T1-B.
- NIST SP 800-53 Rev 5 control catalog — Tier 3 as a catalog, but individual controls become Tier 2
  when a baseline (800-53B low/moderate/high) is contractually imposed. The OSCAL profile mechanism
  models exactly this tier promotion, which is a strong argument for adopting it.
- NIST CHIPS guardrails FAQ.
- EU Chips Act monitoring/early-warning indicators — voluntary information requests; use as factor
  vocabulary (`lead_time_anomaly`, `price_volatility`, `inventory_days`).

---

### The three cross-cutting themes the brief asked me to weight

**Deemed exports.** The decisive insight is that in a software system the deemed export is a
*permissions* event, not a *transfer* event. The violation completes when access becomes possible, not
when data is read. Therefore the provision must bind at the point of **role grant, group membership,
replica creation, and index build** — not at the point of read. Any constitution that phrases the
deemed-export provision as "do not send controlled technology to a foreign person" has already lost;
the correct phrasing is "do not create a state in which a foreign person could obtain it." This is also
why it must be Tier 1: a "could" obligation cannot be adjudicated after the fact.

**ECCN-controlled technical data in logs.** Logs are where export control and observability engineering
collide, and observability wins by default in every organisation. The provision must therefore be
*prohibitive and categorical* (T1-B) rather than *procedural*, because any procedural formulation
("review logs for controlled data") will be satisfied on paper and violated in practice. The
supporting mechanism should be a **typed taint on controlled fields** carried through the code, so
that writing a tainted value to a log sink is a compile-time or lint-time failure — this is the
concrete sense in which T1-B is "architecturally decidable" per criterion 4.

**Record immutability.** This lane found an unusually strong result: **EAR § 762.5(b)(4) and (b)(8)
constitute an actual statutory append-only-with-attribution requirement**, and § 764.2(i) independently
criminalises alteration of export control documents. Most compliance corpora justify immutability by
appeal to security best practice, which is soft and therefore defeasible. Here it is statutory,
specific, and phrased in terms of system behaviour. That makes T1-C one of the best-grounded ABSOLUTE
provisions available anywhere in this corpus — and it should be cited to § 762.5(b)(4) verbatim,
because the verbatim text is more persuasive than any paraphrase.

---

## 8. VENDOR / REFERENCE-ONLY SUMMARY

### SAFE TO VENDOR (verified)

| Source | Basis |
|---|---|
| EAR 15 CFR 730–774 (all sections cited above) | US Govt work, 17 U.S.C. § 105 (GovInfo policy, verified) |
| ITAR 22 CFR 120–130 incl. § 120.34 | same |
| 15 CFR Part 231 (CHIPS clawbacks) | same |
| 15 U.S.C. § 4652 | same |
| BIS Entity List (Supp. 4 to Part 744), DPL CSV | same |
| Consolidated Screening List data | **data.gov licence field = `usa.gov/publicdomain/label/1.0` (verified)** |
| OFAC SDN / Consolidated lists (content) | 17 U.S.C. § 105 baseline; **no explicit OFAC terms page located — record as such** |
| NIST SP 800-53 r5, 800-53B, 800-161r1, 800-171r3, 800-218, CSF 2.0 core | **NIST licensing page verified**: not subject to US copyright; attribution + *"Republished courtesy of NIST"*; foreign rights reserved; no logo |
| `usnistgov/oscal-content` catalogs & baselines | **CC0 1.0 — verified from `LICENSE.md`** |
| `ComplianceAsCode/content` | **BSD-3-Clause — verified from `LICENSE`** |
| Cedar | **Apache-2.0 — verified** |
| compliance-trestle | **Apache-2.0 — verified** |
| GDPR, EU Data Act, EU Chips Act text | **CC BY 4.0 per Decision 2011/833/EU — verified from Commission + Publications Office notices**; attribute "© European Union"; only the OJ version is authentic; **EUR-Lex-specific notice unrendered — note the caveat** |

### REFERENCE-ONLY (cite and paraphrase; do not vendor text)

| Source | Reason |
|---|---|
| DigiChina/Stanford translations of PRC DSL and CAC measures | **No licence found on the page (verified absence)** |
| PRC official legal texts | PRC Copyright Law Art. 5 exclusion **UNVERIFIED** — do not rely |
| Taiwan Laws & Regulations Database (`law.moj.gov.tw`) | **robots.txt disallowed; terms UNVERIFIED**; translations conventionally "for reference only" |
| Korea KLRI / law.go.kr English translations | **No terms statement visible (verified absence)** |
| CSET (Georgetown) translations | **No licensing statement visible (verified absence)** |
| All law-firm analyses (K&L Gates, Miller & Chevalier, Morgan Lewis, Dechert, Akin, Wiley, WilmerHale, Freshfields, law.asia, Formosa Transnational, Lexology, IAM) | Firm copyright |
| OpenSanctions datasets | Licence **UNVERIFIED**; CC-BY-NC + commercial licensing model |
| Secure Controls Framework | Licence **UNVERIFIED** |
| CyberESI OSCAL CPRT catalogs | Licence **UNVERIFIED** |
| News (CommonWealth, The Register) | Publisher copyright |

### ITEMS TO RE-VERIFY BEFORE PUBLICATION

1. **3A090/4A090 numeric TPP and performance-density thresholds** against eCFR Supplement No. 1 to
   Part 774, Category 3 (currently from a law-firm secondary source).
2. **CSL API key requirement, rate limits, and developer-portal ToS** (`developer.trade.gov`).
3. **OFAC file names and download URLs**; whether OFAC publishes any terms-of-use page.
4. **`usnistgov/OSCAL` `LICENSE.md`** text.
5. **EUR-Lex's own legal notice** (both URL variants returned chrome only) to confirm CC BY 4.0
   applies specifically to OJ legislative text.
6. **SSDF PO/PS/PW/RV practice groups** against the SP 800-218 PDF.
7. **ComplianceAsCode 800-171/CUI profile** existence.
8. **Taiwan NSA Art. 8** extraterritoriality and **Act Governing Relations with the Mainland Area
   Art. 9** travel/employment approval.
9. **Formal CFR rescission of the AI Diffusion Rule** (expected by end of FY2026) and the **Affiliates
   Rule** implementation date (currently 2026-11-10).
