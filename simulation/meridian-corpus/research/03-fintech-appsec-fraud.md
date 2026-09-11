# Lane 03 — Fintech Application Security + Fraud/AML Test Material

Survey date: 2026-09-05. Scope: reusable open-source test material for an open compliance
test corpus governing **software change at a regulated fintech**. Corpus case shape:
`(case id, provisions engaged, boolean factor facts, expected disposition)`.

**Verification rule applied:** every licence below was read from a primary artefact
(repository `LICENSE` file fetched raw, the publisher's own terms page, or the Kaggle
`api/v1/datasets/view/...` JSON which returns the machine-readable `licenseName`).
Anything that could not be verified that way is marked **UNVERIFIED** and is
REFERENCE-ONLY by default. Nothing here is inferred from convention.

Already covered by earlier surveys and deliberately not re-derived: Juliet/SARD, CWE,
CVEfixes, OWASP Benchmark, OWASP standards documents, crAPI, VAmPI, Wycheproof,
gitleaks (tool), TruffleHog, Mozilla TLS levels, GitHub Advisory Database, Falco.

---

## 0. Verification technique worth recording

Kaggle dataset pages are client-rendered and return only `<meta>` tags to a fetcher, and
`curl` to `kaggle.com` is refused by the egress proxy. The **unauthenticated JSON endpoint
`https://www.kaggle.com/api/v1/datasets/view/{owner}/{slug}` does render**, and returns the
exact `licenseName` string Kaggle displays. Every Kaggle licence in this document was read
from that endpoint. The equivalent **competitions** endpoint
(`/api/v1/competitions/list?search=...`) returns **HTTP 401** — competition terms are
authenticated-only, which is itself the finding for IEEE-CIS (below).

---

## 1. Fraud / AML / credit datasets (the decisive section)

### 1.1 SAFE TO VENDOR

#### IBM synthetic AML transaction datasets ("AMLworld")
- **URL:** https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
- **Licence (VERIFIED):** `"licenseName": "Community Data License Agreement - Sharing - Version 1.0"` (CDLA-Sharing-1.0), read from the Kaggle dataset-view JSON. Corroborated by the NeurIPS 2023 Datasets & Benchmarks supplementary material ("published on Kaggle under a Community Data License Agreement").
- **Commercial use:** permitted. CDLA-Sharing is a *data* copyleft: if you publish the data or a modified version of it, you publish under the same terms. It does **not** reach your models or your analysis results.
- **Contents/volume:** 6 independent synthetic datasets (HI-/LI- × Small/Medium/Large). Small 5–7M transactions / 515K–705K accounts; Medium ~31–32M / ~2.03–2.08M accounts; Large 176–180M / 2.06–2.12M accounts. ~41.6 GB total, v8 (2025-07-08).
- **Format:** CSV transaction edge lists (from-account, to-account, amount, currency, payment format, timestamp) plus per-transaction laundering labels and pattern files.
- **Labels:** yes — binary `Is Laundering` plus explicit **typology labels** for the eight generator patterns: fan-out, fan-in, gather-scatter, scatter-gather, cycle, random, bipartite, stack (verified in arXiv:2306.16424). Laundering base rates ~1:807 (HI-Large) to ~1:1942 (LI-Medium).
- **Corpus reuse:** this is the best single source of *typology-labelled* ground truth. Use it to instantiate cases for the "AML model / rule change" provision family: each of the eight patterns becomes a named detection obligation, and a case asserts factor facts such as `typology_coverage_regression_tested = true/false`. The extreme class imbalance is itself a factor generator (`imbalance_aware_metric_used`, `auprc_reported`).
- **Verdict:** **VENDOR** (attribute + carry CDLA-Sharing-1.0 notice on any redistribution of the data itself).

#### Sparkov simulated credit-card transactions (Kartik Shenoy)
- **URL:** https://www.kaggle.com/datasets/kartik2112/fraud-detection ; generator: Sparkov Data Generation
- **Licence (VERIFIED):** `"licenseName": "CC0: Public Domain"` (Kaggle dataset-view JSON). Independently corroborated by Amazon Science's `fraud-dataset-benchmark` README, which records the source licence as `https://creativecommons.org/publicdomain/zero/1.0/`.
- **Commercial use:** unrestricted. No attribution obligation.
- **Volume:** 501.6 MB; 1,000 customers × 800 merchants, 2019-01-01 → 2020-12-31. Amazon's benchmark split uses 1,296,675 train / 20,000 test rows.
- **Labels:** yes — binary `is_fraud`, plus merchant category, amount, geo, timestamp, customer demographics.
- **Corpus reuse:** the cleanest vendorable card-fraud fixture. CC0 means it can sit directly inside the corpus repository with no notice file. Good for cases about **model retraining / drift / champion-challenger promotion** where the corpus needs a concrete dataset artefact to point at.
- **Verdict:** **VENDOR** — highest-confidence entry in this lane.

#### ULB / Worldline credit-card fraud
- **URL:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
- **Licence (VERIFIED):** `"licenseName": "Database: Open Database, Contents: Database Contents"` — i.e. **ODbL 1.0** on the database + **DbCL 1.0** on the contents. This directly answers the "ODbL question": the database *is* ODbL-licensed. Amazon Science's benchmark records the source licence as `https://opendatacommons.org/licenses/dbcl/1-0/`.
- **Commercial use:** permitted. DbCL 1.0 text (fetched) states the rights "explicitly include commercial use, and do not exclude any field of endeavour". The ODbL side attaches **share-alike + attribution** obligations if you publicly distribute a *derived database*. Using the data to test or train, without republishing a derived database, does not trigger share-alike.
- **Volume:** 284,807 transactions, 492 frauds (0.172%), 150,828,752 bytes.
- **Labels:** yes — binary `Class`. Features are PCA-transformed (V1–V28) plus `Time`, `Amount`. Publisher explicitly instructs using **AUPRC**, not accuracy.
- **Corpus reuse:** the canonical imbalanced-fraud fixture. Because features are PCA'd, it is useless for feature-governance cases but ideal for **evaluation-metric** and **model-validation** provisions (`metric_appropriate_for_imbalance`, `threshold_change_backtested`).
- **Verdict:** **VENDOR**, with an ODbL notice; prefer *linking + a loader script* over committing the CSV if you want to avoid the derived-database question entirely.

#### AMLSim (IBM)
- **URL:** https://github.com/IBM/AMLSim
- **Licence (VERIFIED):** **Apache-2.0** — `LICENSE` fetched raw from `master`.
- **Contents:** a simulator, not a dataset: generates synthetic banking transactions with injected, *known* money-laundering patterns. Outputs accounts CSV, transactions CSV, cash-transactions CSV, alert accounts/transactions, SAR account and transaction logs, party/entity files, plus network statistics.
- **Labels:** yes, and better than a static dataset — you control the ground truth. SAR/alert labels are emitted alongside the transactions.
- **Corpus reuse:** the single most useful item for a *test corpus* as opposed to a *training corpus*. Because you generate the data, you can produce a fixture per case: one AMLSim configuration per typology, deterministic seed, expected alert set as the oracle. That converts "AML detection rule was changed" into a reproducible boolean: `regression_fixture_reproduces_expected_alerts`.
- **Verdict:** **VENDOR**.

#### PaySim — split licence, read carefully
- **Simulator:** https://github.com/EdgarLopezPhD/PaySim — **GPL-3.0** (`LICENSE` fetched raw from `master`). Copyleft; embedding the simulator in a distributed control product carries GPL obligations.
- **Dataset (PaySim1 on Kaggle):** https://www.kaggle.com/datasets/ealaxi/paysim1 — **CC BY-SA 4.0** (verified via dataset-view JSON). ~24M records, 493,534,783 bytes, one simulated month of mobile-money activity across CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER; labelled `isFraud` and `isFlaggedFraud`.
- **Commercial use:** both permit it. The dataset's **CC BY-SA is share-alike**, which is the same incompatibility class already flagged for the OWASP standards in the earlier survey — a corpus that wants a permissive overall licence should not mix CC BY-SA text into its own case files.
- **Corpus reuse:** `isFlaggedFraud` vs `isFraud` gives a free **control-effectiveness** distinction (the rule fired vs. the event was actually fraud) — directly usable as two independent boolean factor facts on the same case.
- **Verdict:** dataset **VENDOR-with-share-alike** (keep in a separate `third_party/` tree with its own LICENSE so SA does not infect the corpus); simulator **REFERENCE-ONLY** unless you are comfortable with GPL-3.0.

#### FATF typologies and Official Texts
- **URL:** https://www.fatf-gafi.org/en/pages/terms-conditions.html ; publications at https://www.fatf-gafi.org/en/publications.html
- **Licence (VERIFIED, from FATF's own terms page):** **Creative Commons Attribution BY 4.0** for FATF written content — you may "reproduce, distribute and adapt (including translate) such content for any purpose without seeking authorisation". Official Texts may be reproduced free of charge without permission provided they are not altered.
- **Commercial-use nuance (VERIFIED):** publications "may not be sold but may be used in the context of commercial activities such as … consulting or training services." Attribution format is prescribed: `FATF (month, year), Title, URL`.
- **Corpus reuse:** this is the **licence-clean source of money-laundering typology text**, and it is a genuine find — CC BY 4.0 is compatible with a permissive corpus, unlike the OWASP/ACAMS/Wolfsberg material. Use FATF typology names as the controlled vocabulary for the `typology` dimension of AML cases, and cross-map them to the eight AMLSim/IBM generator patterns.
- **Verdict:** **VENDOR** (attribute; do not sell the reproduced text as a product in itself).

### 1.2 REFERENCE-ONLY — do not put in a production control

#### Elliptic Data Set (bitcoin AML) — **NON-COMMERCIAL AND NO-DERIVATIVES**
- **URL:** https://www.kaggle.com/datasets/ellipticco/elliptic-data-set
- **Licence (VERIFIED):** `"licenseName": "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)"` from the Kaggle dataset-view JSON.
- **This is the hardest stop in the lane.** NC forbids use in a commercial firm's production control. ND forbids distributing a modified/derived version — which forbids exactly the reshaping a corpus would need.
- Volume: 203,769 nodes, 234,355 edges, 166 features, 49 time steps; 4,545 illicit (2%), 42,019 licit (21%), remainder unknown.
- A Hugging Face mirror (`yhoma/elliptic-bitcoin-dataset`) declares **MIT**. That mirror's declaration **cannot override the upstream CC BY-NC-ND** and must not be relied on. Treat the MIT mirror as a licensing hazard, not an escape hatch.
- **Verdict:** **REFERENCE-ONLY.** Cite the dataset and the Weber et al. KDD'19 paper; never vendor; never use in a control.

#### Elliptic++
- **URL:** https://github.com/git-disl/EllipticPlusPlus
- **Licence (VERIFIED ABSENT):** no `LICENSE`, `LICENSE.md` or `LICENSE.txt` at `main` or `master` (all HTTP 404). Data is distributed via a Google Drive link with a "let us know by email" note and no terms.
- Volume: 203,769 transaction nodes / 234,355 edges; 822,942 wallet addresses, 1,268,260 temporal nodes, 4,183,205 edges; 49 time steps; classes illicit / licit / unknown; CSV.
- **No licence = no grant.** Additionally it is derived from the Elliptic set, so the upstream NC-ND plausibly reaches it.
- **Verdict:** **REFERENCE-ONLY.**

#### Elliptic2
- **URL:** https://github.com/MITIBMxGraph/Elliptic2 ; paper arXiv:2404.19109
- **Licence:** repository **code** is **Apache-2.0** (`LICENSE` fetched raw from `main`). The **dataset** licence is **UNVERIFIED** — the README defers to `http://elliptic.co/elliptic2`, and elliptic.co surfaces no dataset terms page.
- **Verdict:** code **VENDOR**; data **REFERENCE-ONLY** pending written terms from Elliptic.

#### IEEE-CIS Fraud Detection (Vesta) — **KAGGLE-COMPETITION-TERMS-ONLY**
- **URL:** https://www.kaggle.com/competitions/ieee-fraud-detection ; rules at `/rules`
- **Licence status:** the competition-rules page is client-rendered and the Kaggle competitions API returns **HTTP 401** unauthenticated — the terms are **not machine-verifiable and are gated behind acceptance**. Amazon Science's benchmark records the source licence simply as the rules URL, and documents that the data **403s until you join the competition from your Kaggle account**. The IEEE DataPort mirror is worse: it sits behind an **IEEE DataPort subscription** and states no licence at all.
- Volume: 590,540 training transactions, ~3.5% fraud, 393 original features (Amazon reduced to 67); binary `isFraud`.
- **Verdict:** **REFERENCE-ONLY, competition-terms-only.** Do not vendor, do not use in a control, do not assume the usual "non-commercial research" reading without a lawyer reading the accepted rules. Cite it as a named external dataset in a case description only.

#### LendingClub loan data
- **Status (VERIFIED):** *not* withdrawn — https://www.lendingclub.com/info/download-data.action still lists historical CSVs (2007-2011, 2012-2013, 2014-…), but the page states "Sign in to download the full version of the files." Access is **account-gated** and governed by LendingClub's site terms, not an open licence. No open licence is asserted anywhere on the page.
- A Kaggle mirror `wordsforthewise/lending-club` declares **CC0: Public Domain** (verified via dataset-view JSON, 648,053,013 bytes, accepted + rejected loans with FICO). As with Elliptic, **a third-party uploader's CC0 declaration does not clear the upstream terms.**
- **Verdict:** **REFERENCE-ONLY.** Flag the CC0 mirror explicitly as a provenance risk.

#### Freddie Mac Single-Family Loan-Level Dataset
- **URL:** https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset
- **Terms (VERIFIED from the publisher's page):** access requires registering and signing in to **Clarity Data Intelligence**. Use is "free for non-commercial, academic/research and for limited use, subject to the applicable terms and conditions"; **commercial redistribution requires a licensing agreement** with Freddie Mac.
- Volume: ~56 million mortgages, 1999 → 2026, monthly performance through 2026-03-31, including actual-loss data.
- **Verdict:** **REFERENCE-ONLY** for a regulated firm's production control (a bank's use is commercial). Obtain the commercial licence if the data is genuinely needed.

#### Fannie Mae Single-Family Loan Performance Data
- **URL:** https://capitalmarkets.fanniemae.com/credit-risk-transfer/single-family-credit-risk-transfer/fannie-mae-single-family-loan-performance-data
- **Terms (VERIFIED from the publisher's page):** registration + acceptance of terms on **Data Dynamics**; users are prohibited from "distributing data to third parties or using it in support of external commercial purposes without the express written consent of Fannie Mae."
- Volume: fixed-rate acquisitions 2000-01 → 2012-03 with quarterly performance updates through Q1 2026, plus a ~1M-loan HARP dataset.
- **Verdict:** **REFERENCE-ONLY / consent-required.**

#### HMDA public LAR
- **URLs:** https://ffiec.cfpb.gov/data-publication/ (JS-rendered), historic files at https://www.consumerfinance.gov/data-research/hmda/historic-data/ (2007–2017 LAR CSV, transmittal sheets, panel, data dictionaries)
- **Licence status: UNVERIFIED.** Neither the CFPB historic-data page nor the FFIEC page carries any licence, public-domain declaration, or terms-of-use statement, and the CFPB source-code-policy URL 404s. It is a statutorily mandated federal publication, which in practice means it is a public record — but **no explicit grant was located, so do not label it CC0 or public domain in the corpus manifest**.
- **Verdict:** **REFERENCE-ONLY pending legal sign-off.** Useful in the corpus as a *named public data source* for fair-lending / model-fairness cases rather than as vendored bytes.

### 1.3 Aggregator worth vendoring for its licence bookkeeping

#### Amazon Science — Fraud Dataset Benchmark
- **URL:** https://github.com/amazon-science/fraud-dataset-benchmark
- **Licence (VERIFIED, from README §License):** **MIT-0** (MIT No Attribution).
- **Contents:** loader code that standardises 9 public fraud datasets into train/test splits, and — the valuable part — a per-dataset "Source license" line for each. It records IEEE-CIS as competition-rules-gated, ULB as DbCL, Sparkov/Twitter-bots/malicious-URLs/fake-jobs as CC0, and `fraud-ecommerce` and `vehicle-loan-default` as **licence "None"/"Unknown"** (do not use those two).
- **Corpus reuse:** vendor the loader (MIT-0 needs no notice) and cite its licence table as corroboration in the corpus provenance file. It does **not** redistribute the data — it downloads via the Kaggle CLI at runtime, which means each dataset's own terms still bind the user.
- **Verdict:** **VENDOR** (code only).

### 1.4 AML rule engines (open transaction-monitoring rule sets)

| Project | URL | Licence (verified) | Reuse |
|---|---|---|---|
| **ezrules** | https://github.com/sofeikov/ezrules | **Apache-2.0** | **VENDOR.** Rule authoring workspace with versioned rule revisions, **backtesting against historical events before release**, shadow deployment and staged rollout. This is a near-perfect fixture for "rule change" provisions: the tool's own artefacts (rule revision, backtest result, shadow run) map one-to-one onto boolean factor facts. |
| **Jube** | https://github.com/jube-home/aml-fraud-transaction-monitoring | **AGPL-3.0-or-later** (stated by project as "fully open-source (AGPLv3), all features, no vendor lock-in") | **REFERENCE-ONLY** for embedding. AGPL network-copyleft is disqualifying for most bank-internal SaaS controls. Its *feature taxonomy* — thresholds, velocity/aggregation checks, TTL counters, suppression, sanctions screening, case management with audit trail and document versioning — is excellent free input to the factor vocabulary. |

### 1.5 Industry AML material — terms

- **FATF** — CC BY 4.0. See §1.1. The only licence-clean typology corpus found.
- **Wolfsberg Group** — no open licence located; documents are published as PDFs with conventional all-rights-reserved copyright and no reuse grant found. **REFERENCE-ONLY, cite by title only.**
- **ACAMS** — commercial training/certification body; material is behind membership and copyright. **REFERENCE-ONLY, cite by title only.** No licence text was located, so no claim is made about the terms.

---

## 2. BOLA / IDOR in financial APIs

### Beyond crAPI and VAmPI

| Source | URL | Licence (verified) | Contents | Verdict |
|---|---|---|---|---|
| **Akto tests-library** | https://github.com/akto-api-security/tests-library | **MIT** (`master/LICENSE`) | YAML test templates organised by vulnerability class, including a **`Broken-Object-Level-Authorization`** folder and sibling folders for `Broken-Function-Level-Authorization`, `Broken-User-Authentication`, `Mass-Assignment`, `Lack-of-Resources-and-Rate-Limiting`, `CORS-Misconfiguration`, `Server-Side-Request-Forgery`, `Security-Misconfiguration`, `Misconfigured-HTTP-Headers`, `Verbose-Error-Messages`, `Threat-Protection`, `Input-Validation`. Individual YAML filenames could not be enumerated (GitHub tree pages are robots-disallowed here and `codeload` zip is proxy-blocked at 403), so only the folder taxonomy is verified. | **VENDOR** — the richest MIT-licensed, declarative, machine-readable authorization test set found. Each YAML is already an executable predicate, which is exactly the shape a factor fact needs. |
| **Akto platform** | https://github.com/akto-api-security/akto | **MIT** (`master/LICENSE.md`) | The engine that runs the above templates. | **VENDOR** |
| **Damn Vulnerable Bank** | https://github.com/rewanthtammana/Damn-Vulnerable-Bank | **MIT** (`master/LICENSE`) | Intentionally vulnerable Android **banking** app + backend. Financial-domain BOLA/IDOR targets. | **VENDOR** — fills the "financial" gap that crAPI (automotive) and VAmPI (generic) leave open. |
| **vuln-bank** | https://github.com/Commando-X/vuln-bank | **MIT** (`main/LICENSE.md`) | Deliberately vulnerable web banking app. | **VENDOR** |
| **vuln-bank-mobile** | https://github.com/Commando-X/vuln-bank-mobile | **NO LICENCE FILE** (verified absent on `main` and `master`) | Mobile banking target. | **REFERENCE-ONLY** |
| **dvws-node** | https://github.com/snoopysecurity/dvws-node | **GPL-3.0** (`master/LICENSE`) | Vulnerable node web-services target. | **REFERENCE-ONLY** (copyleft) |
| **RESTler** | https://github.com/microsoft/restler-fuzzer | **MIT** (`main/LICENSE`) | Stateful REST API fuzzer driven from OpenAPI; produces sequences that exercise resource-ownership transitions. | **VENDOR** — the most credible open harness for *generating* BOLA-adjacent sequences. |

### BOLA test generation with ground truth — **negative finding**

There is **no open BOLA benchmark with published ground truth** comparable to Juliet/OWASP-Benchmark in the SAST world.

- **BOLABuster** (Palo Alto Unit 42, LLM-driven BOLA detection) is described in a Unit 42 write-up and a BSidesLV 2024 talk but **no public repository, licence, or ground-truth corpus was located**. REFERENCE-ONLY.
- **arXiv:2201.10833** ("Automatic detection of access control vulnerabilities via API") describes a Python tool doing static analysis over OpenAPI 3.0 specs, validated on seven microservice specifications. **Verified from the paper itself: no public implementation, no repository, no benchmark, no ground-truth dataset is released.** REFERENCE-ONLY.

**Consequence for the corpus:** ground truth for BOLA must be *manufactured*, not imported. The practical route is Damn Vulnerable Bank / vuln-bank (MIT, financial domain) as the system under test, with the known-vulnerable endpoints as the oracle, driven by Akto's MIT BOLA templates or RESTler.

### OWASP API Security Top 10 (2023) — identifiers only
Project licence **VERIFIED**: `OWASP/API-Security` `master/LICENSE` is the **Creative Commons Attribution-ShareAlike 4.0 International Public License** — share-alike, therefore **incompatible with a permissive corpus; cite identifiers only, copy no prose.**

Identifiers (safe to cite as provision references): `API1:2023` Broken Object Level Authorization · `API2:2023` Broken Authentication · `API3:2023` Broken Object Property Level Authorization · `API4:2023` Unrestricted Resource Consumption · `API5:2023` Broken Function Level Authorization · `API6:2023` Unrestricted Access to Sensitive Business Flows · `API7:2023` Server Side Request Forgery · `API8:2023` Security Misconfiguration · `API9:2023` Improper Inventory Management · `API10:2023` Unsafe Consumption of APIs.

---

## 3. Payment-page script integrity (PCI DSS 6.4.3 / 11.6.1)

### The conformance suite that actually exists: web-platform-tests

- **URL:** https://github.com/web-platform-tests/wpt
- **Licence (VERIFIED):** **3-Clause BSD** (`master/LICENSE.md`, "The 3-Clause BSD License", © web-platform-tests contributors). Permissive, commercial use fine, notice required.
- **Verified present:**
  - `subresource-integrity/subresource-integrity.html` — fetched (15,359 bytes). Uses `SRIScriptTest` and `SRIStyleTest` harness constructors over same-origin and cross-origin cases with correct `sha256-…` digests, deliberately wrong digests (`sha256-deadbeef…`), and CORS variations. Helper files `sri-test-helpers.sub.js` and `/resources/sriharness.js`.
  - `content-security-policy/META.yml` and `content-security-policy/script-src/script-src-1_1.html` — fetched (HTTP 200). A large, structured CSP conformance tree.
- **Corpus reuse:** this is the **only real conformance suite for the browser-side primitives PCI DSS 6.4.3/11.6.1 depend on**. It does not test "is my payment page compliant"; it tests that SRI and CSP behave to spec. Use it as the *mechanism-level* evidence layer beneath a compliance case: a case asserting `sri_enforced_on_all_payment_page_scripts = true` is only meaningful if SRI enforcement itself is known-good, and WPT is the artefact that establishes that.
- **Verdict:** **VENDOR** (BSD-3, take only the `subresource-integrity/`, `content-security-policy/` and `webauthn/` subtrees plus `/resources` harness).

### Supporting tools

| Tool | URL | Licence (verified) | Verdict |
|---|---|---|---|
| **Google CSP Evaluator** | https://github.com/google/csp-evaluator | **Apache-2.0** (`master/LICENSE`) | **VENDOR** — programmatic CSP policy grading; turns "is the CSP restrictive enough" into a scriptable boolean. |
| **Mozilla HTTP Observatory** | https://github.com/mozilla/http-observatory | **MPL-2.0** (`main/LICENSE`) | **VENDOR with care** — MPL-2.0 is file-level copyleft; fine to use as a tool, keep modifications separate. Scores CSP/SRI/headers. |
| **srihash.org** | https://github.com/mozilla/srihash.org | **MPL-2.0** (`master/LICENSE`) | **VENDOR with care** — SRI digest generation, useful for building the expected-hash side of a tamper-detection fixture. |
| **OWASP PCI DSS Toolkit** | https://owasp.org/www-project-pci-dss-toolkit/ | Content stated as **CC BY-SA 4.0** | **REFERENCE-ONLY.** Verified status: **Incubator, version 0.0.0**, with the script-inventory collection still an open issue. Explicitly scoped at "inventory and protection of payment page scripts" and "detection of unauthorised script modifications with real-time alerts" — i.e. exactly 6.4.3/11.6.1 — but there is **no shipped code yet**. Track it; do not depend on it. |
| **PCI DSS standard itself** | https://www.pcisecuritystandards.org/document_library/ | **UNVERIFIED / restricted.** The library page surfaces a "Request Material License Agreement" process; no open reuse grant was located. | **REFERENCE-ONLY — cite requirement numbers (6.4.3, 11.6.1) only, never the prose.** |

**Negative finding:** there is **no open conformance suite for PCI DSS 6.4.3/11.6.1 as such**. Every product that claims to cover it (Feroot, Jscrambler, c/side, DataStealth, CentralCSP) is commercial. The corpus must construct these cases from WPT primitives + CSP Evaluator + a hand-built script-inventory fixture.

---

## 4. Step-up authentication / MFA enforcement

- **FIDO Alliance conformance tooling** — https://fidoalliance.org/certification/functional-certification/conformance/. **Terms (VERIFIED from FIDO's page):** the UAF, U2F and FIDO2 Conformance Test Tools are provided "upon successful completion of registration", gated behind a **Tool Request Agreement** with the Certification Secretariat; UAF authenticator implementers additionally need a registered Vendor ID. The page does not state an open-source licence. **Verdict: REFERENCE-ONLY / membership-and-agreement-gated. Not vendorable.**
- **web-platform-tests `webauthn/`** — verified present (`webauthn/META.yml` and `webauthn/helpers.js` both HTTP 200), under WPT's **BSD-3-Clause**. This is the **open substitute** for FIDO's gated tooling at the protocol-behaviour level. **VENDOR.**
- **SimpleWebAuthn** — https://github.com/MasterKale/SimpleWebAuthn — **MIT** (`master/LICENSE.md`). Server + browser libraries with test fixtures for registration/authentication ceremonies. **VENDOR.**
- **py_webauthn (Duo Labs)** — https://github.com/duo-labs/py_webauthn — **BSD-style** licence (`master/LICENSE`, "Copyright (c) 2017-2021 Duo Security, Inc. All rights reserved. Redistribution and use in source and binary forms…"). **VENDOR** (retain notice).

**Negative finding:** **no open test vectors exist for "step-up on high-risk actions".** WebAuthn conformance covers the ceremony; it says nothing about *when* a ceremony must be demanded. The trigger condition (transaction value, beneficiary newness, device change) is business logic, and no open corpus encodes it. This must be authored — and it is arguably the single highest-value original contribution this corpus can make in the fintech lane.

---

## 5. Secrets in financial connectors

Source of truth: `https://raw.githubusercontent.com/gitleaks/gitleaks/master/config/gitleaks.toml`, **222 rules** total, fetched and parsed. Licence **VERIFIED MIT** (Zachary Rice, 2019).

**Payment/fintech rule ids that DO exist (exact ids, verified):**

| Rule id | Notes |
|---|---|
| `stripe-access-token` | regex `\b((?:sk\|rk)_(?:test\|live\|prod)_[a-zA-Z0-9]{10,99})…`, entropy 2, keywords `sk_test`, `sk_live`, `sk_prod`, `rk_test`, … |
| `plaid-api-token` | matches `access-(sandbox\|development\|production)-<uuid>` in a `plaid`-keyed assignment |
| `plaid-client-id` | 24-char lowercase alnum near a `plaid` key, entropy 3.5 |
| `plaid-secret-key` | 30-char lowercase alnum near a `plaid` key, entropy 3.5 |
| `square-access-token` | |
| `squarespace-access-token` | |
| `shopify-access-token`, `shopify-custom-access-token`, `shopify-private-app-access-token`, `shopify-shared-secret` | |
| `coinbase-access-token` | |
| `finicity-api-token`, `finicity-client-secret` | data-aggregation connector |

**Verified gap — Adyen is not covered anywhere in open scanning:**
- `grep -i adyen` over the full 3,209-line `gitleaks.toml`: **zero matches.**
- `grep -i adyen` over TruffleHog's `pkg/engine/defaults/defaults.go` (90,183 bytes, the authoritative detector registry): **zero matches**; `pkg/detectors/adyen/adyen.go` returns **404**.
- TruffleHog (AGPL, therefore REFERENCE-ONLY per the earlier survey) *does* carry `braintreepayments`, `checkout`, `dwolla`, `plaidkey`, `stripe`, `stripepaymentintent`.

**Corpus reuse:** a fintech corpus should ship a small, original, MIT-compatible **Adyen rule** contributed back to gitleaks, and cite the gap as a factor (`connector_credential_pattern_covered_by_scanner`). The existing rule ids above are the enumerable, machine-checkable vocabulary for `secret_scanning_rule_coverage`.

---

## 6. Chaos, DAST and resilience for payment paths

| Tool | URL | Licence (verified) | Corpus use |
|---|---|---|---|
| **Toxiproxy** | https://github.com/Shopify/toxiproxy | **MIT** (`main/LICENSE`, © 2014 Shopify) | **VENDOR.** Built by a payments-adjacent company for exactly this: deterministic latency/bandwidth/timeout/reset injection between an app and its dependencies. The best fit for **database-failover and payment-gateway-degradation** cases because failures are scripted and repeatable — a chaos test that is reproducible can be an oracle. |
| **Chaos Mesh** | https://github.com/chaos-mesh/chaos-mesh | **Apache-2.0** (`master/LICENSE`) | **VENDOR.** Kubernetes-native fault injection incl. network partition and pod/IO faults. |
| **LitmusChaos** | https://github.com/litmuschaos/litmus | **Apache-2.0** (`master/LICENSE`) | **VENDOR.** Experiment hub with declarative experiment CRDs — declarative experiments map cleanly to corpus cases. |
| **ChaosBlade** | https://github.com/chaosblade-io/chaosblade | **Apache-2.0** (`master/LICENSE`) | **VENDOR.** |
| **Chaos Toolkit** | https://github.com/chaostoolkit/chaostoolkit | **Apache-2.0** (`master/LICENSE`) | **VENDOR.** JSON/YAML experiment definitions with explicit **steady-state hypotheses** — the hypothesis is directly reusable as the `expected_disposition` of a resilience case. |
| **Chaos Monkey** | https://github.com/Netflix/chaosmonkey | **Apache-2.0** (`master/LICENSE`) | **VENDOR** (instance termination only; narrow). |
| **Simian Army** | https://github.com/Netflix-Skunkworks/simianarmy | **NO LICENCE FILE** (verified absent) | **REFERENCE-ONLY.** |
| **k6** | https://github.com/grafana/k6 | **AGPL-3.0** (`master/LICENSE.md`) | **REFERENCE-ONLY** for embedding. Usable as an external CLI for **rate-limit validation** (429 behaviour under burst), but AGPL means do not link or redistribute inside a control product. |
| **RESTler** | https://github.com/microsoft/restler-fuzzer | **MIT** (`main/LICENSE`) | **VENDOR.** Doubles as the rate-limiting/resource-consumption prober (`API4:2023`). |
| **Akto `Lack-of-Resources-and-Rate-Limiting`** | see §2 | **MIT** | **VENDOR.** Declarative rate-limit test templates. |

**Negative finding:** **no financial-services-specific open chaos suite exists.** There is no "payments chaos" equivalent of Falco's fintech rules. Payment-path resilience cases must be authored on top of the generic Apache-2.0/MIT engines above, with Toxiproxy as the determinism layer.

---

## 7. Consolidated vendor / reference table

**SAFE TO VENDOR (permissive or clean):** AMLSim (Apache-2.0) · Sparkov CC0 · fraud-dataset-benchmark (MIT-0) · FATF typologies (CC BY 4.0) · WPT SRI/CSP/WebAuthn (BSD-3) · gitleaks config (MIT) · Akto + tests-library (MIT) · RESTler (MIT) · Damn Vulnerable Bank (MIT) · vuln-bank (MIT) · SimpleWebAuthn (MIT) · py_webauthn (BSD) · Toxiproxy (MIT) · Chaos Mesh / Litmus / ChaosBlade / Chaos Toolkit / Chaos Monkey (Apache-2.0) · CSP Evaluator (Apache-2.0) · ezrules (Apache-2.0) · Elliptic2 *code* (Apache-2.0).

**VENDOR WITH SHARE-ALIKE / WEAK-COPYLEFT CARE:** ULB creditcardfraud (ODbL 1.0 + DbCL 1.0) · IBM AML datasets (CDLA-Sharing-1.0) · PaySim1 dataset (CC BY-SA 4.0) · http-observatory and srihash.org (MPL-2.0).

**REFERENCE-ONLY — NON-COMMERCIAL:** Elliptic Data Set (**CC BY-NC-ND 4.0**) · Freddie Mac SFLLD (non-commercial free tier only).

**REFERENCE-ONLY — COMPETITION / GATED TERMS:** IEEE-CIS Fraud Detection (Kaggle competition rules, 401 to the API, 403 to the data until you join; IEEE DataPort mirror is subscription-gated) · FIDO conformance tools (Tool Request Agreement) · PCI DSS documents (Material License Agreement).

**REFERENCE-ONLY — CONSENT REQUIRED:** Fannie Mae SF Loan Performance (no external commercial use without written consent) · LendingClub (account-gated site terms; the CC0 Kaggle mirror does not clear them).

**REFERENCE-ONLY — NO LICENCE FOUND:** Elliptic++ · Elliptic2 *data* · vuln-bank-mobile · Simian Army · HMDA public LAR (no explicit grant located) · Wolfsberg · ACAMS · `fraud-ecommerce` and `vehicle-loan-default` Kaggle sets (recorded as "None"/"Unknown" by Amazon Science).

**REFERENCE-ONLY — COPYLEFT UNSUITABLE FOR EMBEDDING:** PaySim simulator (GPL-3.0) · Jube (AGPL-3.0) · k6 (AGPL-3.0) · dvws-node (GPL-3.0) · TruffleHog (AGPL, prior survey).

**CITE-IDENTIFIERS-ONLY (CC BY-SA, incompatible):** OWASP API Security Top 10 2023 · OWASP PCI DSS Toolkit.

---

## 8. Factor vocabulary

Boolean factor facts, phrased so each is independently observable from an artefact and
so that the negation is meaningful. Grouped by provision family.

### 8.1 BOLA / object-level authorization (`API1:2023`, `API3:2023`, `API5:2023`; CWE-639, CWE-284)
- `object_identifier_is_unguessable`
- `ownership_check_present_at_data_access_layer`
- `ownership_check_independent_of_client_supplied_identifier`
- `cross_tenant_access_test_present_in_ci`
- `cross_tenant_access_test_passed`
- `authorization_test_covers_every_new_or_changed_endpoint`
- `object_property_level_authorization_enforced` (API3 — field-level, distinct from row-level)
- `function_level_authorization_enforced_for_privileged_operations` (API5)
- `enumeration_of_account_or_transaction_ids_returns_404_not_403`
- `bola_regression_fixture_reproduces_known_vulnerable_case`

### 8.2 Payment-page script integrity (PCI DSS 6.4.3, 11.6.1)
- `payment_page_script_inventory_maintained`
- `every_inventoried_script_has_documented_business_justification`
- `every_inventoried_script_has_recorded_authorization`
- `sri_integrity_attribute_present_on_all_third_party_payment_page_scripts`
- `sri_digest_algorithm_is_sha256_or_stronger`
- `csp_present_on_payment_page`
- `csp_script_src_excludes_unsafe_inline_and_unsafe_eval`
- `csp_report_uri_or_report_to_configured_and_monitored`
- `script_tamper_detection_mechanism_deployed`
- `script_tamper_detection_alerts_at_least_weekly_or_on_change`
- `script_inventory_reviewed_on_this_change`
- `new_or_modified_payment_page_script_introduced_by_this_change`

### 8.3 Step-up authentication / MFA enforcement
- `high_risk_action_classified_in_change_record`
- `step_up_authentication_required_for_high_risk_action`
- `step_up_challenge_is_phishing_resistant` (FIDO2/WebAuthn vs OTP)
- `step_up_binds_challenge_to_transaction_details` (dynamic linking / transaction confirmation)
- `step_up_cannot_be_bypassed_by_direct_api_call`
- `step_up_enforced_server_side_not_client_side`
- `authenticator_attestation_verified`
- `user_verification_flag_required_and_checked`
- `step_up_exemption_documented_and_time_bounded`
- `step_up_regression_test_present_for_changed_high_risk_flow`

### 8.4 Secrets in financial connectors
- `secret_scanning_runs_on_every_commit_and_pull_request`
- `scanner_ruleset_covers_each_payment_provider_in_use`
- `connector_credential_pattern_covered_by_scanner` (the Adyen gap makes this non-trivial)
- `payment_provider_credential_present_in_source_history`
- `detected_secret_rotated_within_defined_window`
- `live_key_distinguishable_from_test_key_by_pattern` (Stripe `sk_live` vs `sk_test`)
- `production_credential_absent_from_non_production_configuration`
- `secret_stored_in_managed_vault_not_in_repository_or_ci_variable`
- `scanner_finding_triaged_before_merge`

### 8.5 Fraud / AML model and rule change
- `change_alters_fraud_or_aml_detection_logic`
- `change_is_model_retrain_versus_rule_edit` (mutually exclusive pair; record both)
- `typology_coverage_regression_tested` (against the eight AMLSim/IBM patterns)
- `backtest_against_historical_transactions_performed_before_release`
- `backtest_shows_no_material_regression_in_recall_at_fixed_alert_volume`
- `imbalance_appropriate_metric_used` (AUPRC, not accuracy)
- `alert_volume_impact_estimated_and_within_operational_capacity`
- `shadow_or_champion_challenger_run_completed_before_promotion`
- `model_validation_independent_of_model_development`
- `threshold_change_documented_with_rationale`
- `rule_change_versioned_and_revertible`
- `training_data_licence_permits_production_use` ← *the factor this survey exists to make checkable*
- `training_data_provenance_recorded_in_model_documentation`
- `false_positive_rate_change_disclosed_to_financial_crime_operations`
- `sar_filing_pathway_unaffected_or_change_approved_by_mlro`

---

## 9. Explicit negative findings (record so they are not re-derived)

1. **No open BOLA benchmark with ground truth exists.** BOLABuster has no public repo; arXiv:2201.10833 releases neither tool nor data.
2. **No open conformance suite for PCI DSS 6.4.3/11.6.1.** The OWASP PCI DSS Toolkit is Incubator v0.0.0 with script inventory still an open issue; everything else is commercial.
3. **No open test vectors for step-up-on-high-risk-action.** WebAuthn conformance covers the ceremony, not the trigger.
4. **Adyen key formats are covered by neither gitleaks nor TruffleHog.**
5. **No financial-services-specific open chaos suite.**
6. **Elliptic is CC BY-NC-ND** — the most cited AML graph dataset in the literature is the one a regulated firm may least use. Its MIT-declared Hugging Face mirror is a trap.
7. **Third-party Kaggle mirrors declaring CC0 over gated upstream data** (LendingClub `wordsforthewise`, Elliptic on Hugging Face) recur in this lane and must be treated as provenance defects, not licences.
8. **Kaggle competition terms are not machine-readable** — `/api/v1/competitions/...` returns 401. Any competition dataset is therefore, on evidence, un-clearable without a human accepting the rules.
