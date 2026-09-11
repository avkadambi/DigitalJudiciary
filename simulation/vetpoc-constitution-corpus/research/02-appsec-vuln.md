# 02 — AppSec & Vulnerability Test Corpora (Lane 2)

Research date: **2026-09-05**. Every license below was checked by fetching the actual
`LICENSE` file, terms-of-use page, or dataset landing page. Anything I could not
confirm from a primary source is marked **UNVERIFIED** — never treat those as safe.

Target corpus shape (what everything below has to feed):

```
case  ::= (case_id, provisions_engaged[], factor_facts{name -> bool}, expected_disposition)
oracle ::= violates(case, provision) -> bool
```

So the three reuse paths that matter are:

1. **Provision vocabulary** — normative, citable, stably-identified rules (ASVS `V8.2.1`,
   CWE-89, OWASP `A01:2025`, API Top 10 `API1:2023`). These become `provisions`.
2. **Factor vocabulary** — the boolean predicates a case asserts
   (`uses_parameterized_query`, `object_id_from_request_unchecked`,
   `secret_matches_high_entropy_rule`, `crypto_algorithm_in_deprecated_set`).
3. **Oracles / ground truth** — corpora that already say *true vulnerability: yes/no*
   per artifact. These are what you calibrate `violates(c,p)` against.

---

## 0. Verdict table (read this first)

| # | Source | License (verified) | Vendor into Apache-2.0 / CC-BY-4.0 repo? |
|---|--------|--------------------|------------------------------------------|
| 1 | NIST SARD / Juliet (C/C++, Java, C#) | Public domain + CC0 1.0 | **VENDOR — safest single source in this lane** |
| 2 | CWE (MITRE) | MITRE royalty-free license, attribution required | **VENDOR** (reproduce MITRE copyright + license) |
| 3 | CAPEC (MITRE) | MITRE royalty-free license, attribution required | **VENDOR** (same conditions) |
| 4 | GitHub Advisory Database | CC-BY-4.0 | **VENDOR** |
| 5 | CVEfixes *data* | CC-BY-4.0 (code MIT) | **VENDOR** |
| 6 | OSV.dev code + OSV schema | Apache-2.0 | **VENDOR** (schema/tooling; per-record data varies) |
| 7 | Gitleaks rules (`config/gitleaks.toml`) | MIT | **VENDOR** |
| 8 | OWASP Juice Shop `challenges.yml` | MIT | **VENDOR** |
| 9 | OWASP crAPI | Apache-2.0 | **VENDOR** |
| 10 | VAmPI | MIT | **VENDOR** |
| 11 | CodeQL queries (`github/codeql`) | MIT (CLI licensed separately) | **VENDOR** (queries only, not the CLI) |
| 12 | CyberSecEval (`CybersecurityBenchmarks/`) | MIT (dir-local; repo root is Llama 3.2 CL) | **VENDOR the subdir only — read note** |
| 13 | AgentDojo | MIT | **VENDOR** |
| 14 | InjecAgent | MIT | **VENDOR** |
| 15 | CVSS v4.0 / v3.1 (FIRST) | Free use w/ attribution + conformance | **VENDOR the vector grammar**, cite FIRST |
| 16 | SecretBench (repo) | MIT (repo) — **data is access-gated** | **REFERENCE-ONLY** for the data |
| 17 | OWASP ASVS | CC-BY-**SA**-4.0 | **REFERENCE-ONLY** (SA is viral, incompatible w/ CC-BY-4.0) |
| 18 | OWASP Top 10 / API Top 10 / WSTG / LLM Top 10 | CC-BY-SA-4.0 | **REFERENCE-ONLY** (cite IDs, don't copy prose) |
| 19 | OWASP Benchmark (Java) | GPL-2.0 | **REFERENCE-ONLY** (regenerate ground truth, don't copy code) |
| 20 | OWASP Benchmark (Python) | GPL-3.0 | **REFERENCE-ONLY** |
| 21 | OWASP WebGoat | GPL-2.0-or-later | **REFERENCE-ONLY** |
| 22 | TruffleHog | AGPL-3.0 | **REFERENCE-ONLY** |
| 23 | Tiredful-API, OWASP Vulnerable-Web-Application | GPL-3.0 | **REFERENCE-ONLY** |
| 24 | NVD API data | NVD API Terms of Use (not public domain; attribution notice) | **REFERENCE-ONLY / attribute** |
| 25 | CVE Records (cvelistV5) | CVE Program Terms of Use — **UNVERIFIED verbatim** | **REFERENCE-ONLY until counsel reads ToU** |
| 26 | SecurityEval | **UNVERIFIED** (no LICENSE file) | **REFERENCE-ONLY** |
| 27 | LLMSecEval | **UNVERIFIED** ("Other (Open)" on Zenodo) | **REFERENCE-ONLY** |
| 28 | DiverseVul | **UNVERIFIED** (no LICENSE file) | **REFERENCE-ONLY** |
| 29 | Damn Vulnerable RESTful API (DVRA) | **UNVERIFIED** (no LICENSE file) | **REFERENCE-ONLY** |
| 30 | Devign mirror / Big-Vul mirror | MIT on the mirrors; upstream data UNVERIFIED | **REFERENCE-ONLY** |
| 31 | SCTBench | MIT | **VENDOR** (small; concurrency oracle) |

---

## 1. OWASP Benchmark — the closest thing to a ready-made oracle

| Field | Value |
|---|---|
| Name | OWASP Benchmark for Java (v1.2) |
| URL | https://github.com/OWASP-Benchmark/BenchmarkJava |
| Contains | A runnable Java web app with deliberately planted true and false vulnerability instances, one per `BenchmarkTestNNNNN` servlet |
| Format | Java source + `expectedresults-1.2.csv` (`test name, category, real vulnerability, cwe`) |
| **License (verified)** | **GPL-2.0** (`LICENSE` file fetched; plain GPLv2 text) |
| Volume (verified by download) | **2,740 test cases**; **1,415 true / 1,325 false** |
| Ground truth | **Yes — explicit boolean per case, plus a CWE id** |

Verified category / CWE / count breakdown (I downloaded and tallied the CSV):

| Category | CWE | Cases |
|---|---|---|
| sqli | CWE-89 | 504 |
| weakrand | CWE-330 | 493 |
| xss | CWE-79 | 455 |
| pathtraver | CWE-22 | 268 |
| cmdi | CWE-78 | 251 |
| crypto | CWE-327 | 246 |
| hash | CWE-328 | 236 |
| trustbound | CWE-501 | 126 |
| securecookie | CWE-614 | 67 |
| ldapi | CWE-90 | 59 |
| xpathi | CWE-643 | 35 |

**OWASP Benchmark for Python (v0.1)** — https://github.com/OWASP-Benchmark/BenchmarkPython —
**License verified: GPL-3.0**. `expectedresults-0.1.csv` has **1,230 test cases**, same
four-column schema, 14 vulnerability types (adds code injection, deserialization,
unchecked redirects, XXE).

**Reuse path.** This is the single best *structural* model for the vet corpus: it is
literally `(case_id, cwe, boolean expected_disposition)`. Adopt the schema. Do **not**
vendor: GPL-2.0/3.0 would infect an Apache-2.0 repo. Two safe options:

* **Reference by id** — a vet case can carry `derived_from: "OWASP-BM-1.2/BenchmarkTest00542"`
  without copying the Java. Facts and CSV rows (id, category, bool, CWE number) are thin
  factual data, but the surrounding code is not — keep the code out.
* **Re-derive** — write vet-domain equivalents (a `PatientRecordServlet` that concatenates
  a `patient_id` into SQL) using the Benchmark's *taxonomy* of source/sink/sanitizer
  variants, which is an idea, not copyrightable expression.

The true/false ratio (~52/48) is also worth copying as a design target: a compliance
corpus with only violations trains nothing about `not violates(c,p)`.

---

## 2. NIST SARD / Juliet — the volume play, and it is CC0

| Field | Value |
|---|---|
| Name | NIST Software Assurance Reference Dataset (SARD) / Juliet Test Suites |
| URL | https://samate.nist.gov/SARD/ ; suites at `/SARD/test-suites/{id}` |
| **License (verified)** | Suite pages state: *"This software is not subject to copyright protection and is in the public domain"*, plus **CC0 1.0** for international use |
| Ground truth | **Yes** — every case is a paired `good`/`bad` variant with the flaw location and CWE encoded in the filename and directory structure |

Verified suite inventory:

| Suite | SARD id | Language | Test cases | CWEs |
|---|---|---|---|---|
| Juliet C/C++ 1.3 | 112 | C/C++ | **64,099** | **118** |
| Juliet C/C++ 1.3.1 (extra support) | 116 | C/C++ | 64,099 (28 cases corrected: CWE-476, CWE-457) | ~118 |
| Juliet Java 1.3 | 111 | Java | **28,881** | **112** |
| Juliet C# 1.3 | 110 | C# | **28,942** | not stated on index |
| IARPA STONESOUP Phase 3 | 113 | C | 7,770 | — |
| SATE6 Sakai 11.2 | 120 | Java | 60 | — |
| SARD overall | — | C, C++, Java, PHP, C# | **>450,000** | — |

Downloads are ZIPs (Juliet C/C++ 1.3 = 146 MB; Java 1.3 = 73.2 MB; C/C++ 1.3.1 = 671 MB),
each with a published SHA-256.

**Reuse path — this is the workhorse.**

* **Vendor freely.** CC0/public domain is compatible with anything. No attribution
  legally required (attribute anyway).
* **Factor vocabulary.** Juliet's naming convention *is* a factor grammar. A filename like
  `CWE89_SQL_Injection__connect_tcp_execute_01.java` decomposes into
  `{cwe: 89, source: connect_tcp, sink: execute, flow_variant: 01}`. That maps directly onto
  boolean factor facts: `taint_source_is_network = true`, `sink_is_sql_execute = true`,
  `sanitizer_present = false`. The `good*`/`bad*` method pairs give you a *matched pair* of
  cases differing in exactly one factor — the ideal shape for testing whether a compliance
  rule engine keys on the right fact rather than on surface features.
* **Provision keying.** 112–118 distinct CWEs is enough to populate a CWE-keyed provision
  table covering essentially every technical control a vet-software policy would name.
* **Caveat.** Juliet is synthetic, C/C++-heavy, and frozen at 2017. Use it for *coverage and
  matched pairs*, not for realism. Pair it with CVEfixes (§6) for realism.

---

## 3. OWASP ASVS — the best provision vocabulary, but CC-BY-SA

| Field | Value |
|---|---|
| Name | OWASP Application Security Verification Standard |
| URL | https://github.com/OWASP/ASVS |
| **License (verified)** | **CC-BY-SA-4.0** (`LICENSE.md` = Attribution-ShareAlike 4.0 International) |
| Formats | Markdown, **JSON**, **CSV**, XML, per language, under `4.0/docs_en/` and `5.0/docs_en/` |

Verified by downloading and parsing both releases:

| Release | Requirements | CWE-mapped | Schema |
|---|---|---|---|
| ASVS 4.0.3 | **286** | **268** | `Shortcode` (`V1.1.1`), `Description`, `L1`/`L2`/`L3` `{Required, Requirement}`, `CWE[]`, `NIST[]` |
| ASVS 5.0.0 | **345** across 17 chapters | CWE removed from the core JSON | `chapter_id, chapter_name, section_id, section_name, req_id, req_description, L` |

ASVS 5.0.0 chapters: Encoding and Sanitization; Validation and Business Logic; Web Frontend
Security; API and Web Service; File Handling; Authentication; Session Management;
**Authorization**; Self-contained Tokens; OAuth and OIDC; Cryptography; Secure Communication;
Configuration; Data Protection; Secure Coding and Architecture; Security Logging and Error
Handling; WebRTC.

A salvaged CWE mapping survives at `5.0/mappings/v5.0.be_cwe_mapping.json` — **212 entries**
of `requirement_id -> CWE number` (verified: `{"v5.0.be-1.2.4": "306", ...}`). There are also
`mapping_v4.0.3_to_v5.0.0.yml` and the reverse, so 4.0.3's CWE mappings can be forward-ported.

**Reuse path.** ASVS requirement IDs are the single best off-the-shelf **provision
identifiers**: stable, hierarchical, levelled (L1/L2/L3 ≈ tiers of obligation), and CWE-linked.
A vet provision can be authored as *"VET-AUTHZ-3, aligned to ASVS V8.2.1 / CWE-639"*.

**But CC-BY-SA-4.0 is viral.** Copying ASVS *requirement text* into a CC-BY-4.0 or Apache-2.0
corpus forces the derivative under CC-BY-SA. The safe pattern:

* **Reference the IDs, don't copy the prose.** `V8.2.1` is a fact, not expression.
* Write your own provision language and record `aligned_to: ["ASVS-5.0:V8.2.1", "CWE-639"]`.
* If you want the text verbatim, isolate it in a clearly-scoped `third_party/asvs/`
  directory under CC-BY-SA-4.0 with its own LICENSE, and keep the corpus itself from being a
  derivative work. Get counsel to sign off — this is the highest-risk license in the lane
  precisely because ASVS is the most tempting thing to copy.

---

## 4. OWASP taxonomies — Top 10, API Top 10, LLM Top 10, WSTG

All four verified as **CC-BY-SA-4.0** (`LICENSE`/`LICENSE.md` fetched from each repo).
Same ShareAlike caution as §3: **cite IDs, do not copy prose**.

**OWASP Top 10:2025** (https://owasp.org/Top10/2025/): A01 Broken Access Control ·
A02 Security Misconfiguration · A03 Software Supply Chain Failures · A04 Cryptographic
Failures · A05 Injection · A06 Insecure Design · A07 Authentication Failures ·
A08 Software or Data Integrity Failures · A09 Security Logging and Alerting Failures ·
A10 Mishandling of Exceptional Conditions.

**OWASP API Security Top 10:2023** — the most relevant list for a vet-practice SaaS, because
practice-management systems are multi-tenant CRUD APIs over animal/owner records:

| ID | Name |
|---|---|
| API1:2023 | Broken Object Level Authorization |
| API2:2023 | Broken Authentication |
| API3:2023 | Broken Object Property Level Authorization |
| API4:2023 | Unrestricted Resource Consumption |
| API5:2023 | Broken Function Level Authorization |
| API6:2023 | Unrestricted Access to Sensitive Business Flows |
| API7:2023 | Server Side Request Forgery |
| API8:2023 | Security Misconfiguration |
| API9:2023 | Improper Inventory Management |
| API10:2023 | Unsafe Consumption of APIs |

**OWASP Top 10 for LLM Applications 2025** (relevant to AI-agent-authored changes):
LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Supply Chain ·
LLM04 Data and Model Poisoning · LLM05 Improper Output Handling · LLM06 Excessive Agency ·
LLM07 System Prompt Leakage · LLM08 Vector and Embedding Weaknesses · LLM09 Misinformation ·
LLM10 Unbounded Consumption. No machine-readable release found — HTML/PDF only.

**OWASP WSTG** (https://github.com/OWASP/wstg) — CC-BY-SA-4.0. Value here is the `WSTG-xxxx-nn`
test IDs (e.g. the authorization chapter's IDOR test), which give you **verification-procedure
identifiers** to hang alongside provisions: a provision says what must hold, a WSTG id says how
you'd check it.

**Reuse path.** These are your top-level `provisions_engaged` buckets. A vet case engaging
"a clinician can read another practice's patient record" engages
`{VET-AUTHZ-1, API1:2023, A01:2025, CWE-639, ASVS-5.0:V8.x}` — one case, five provision
citations at different granularities. That layering is exactly what a compliance corpus needs
to test: does the engine fire the right provisions, not merely *a* provision?

---

## 5. CWE and CAPEC (MITRE)

### CWE

| Field | Value |
|---|---|
| URL | https://cwe.mitre.org/data/downloads.html |
| Current version (verified) | **CWE 4.20** |
| Formats (verified) | **XML (.zip)** and **CSV (.zip)** per view. No JSON. |
| Views | 1000 (Research Concepts), 699 (Software Development), 1194 (Hardware Design), 1400 (Comprehensive Categorization), 1003, 1435 (Top 25), 658/659/660/661 (C/C++/Java/PHP), 2000 (full dictionary), and others |
| **License (verified)** | MITRE grants *"a non-exclusive, royalty-free license to use CWE for research, development, and commercial purposes"*, conditioned on reproducing *"MITRE's copyright designation and this license in any such copy."* CWE is a MITRE trademark. |

### CAPEC

| Field | Value |
|---|---|
| URL | https://capec.mitre.org/data/downloads.html |
| Current version (verified) | **CAPEC 3.9 — 559 attack patterns** |
| Formats (verified) | XML (`capec_latest.xml`), CSV zips, XSD schema |
| Views | 1000 Mechanisms of Attack, 3000 Domains of Attack, 658/659 (ATT&CK / OWASP related), 683 Supply Chain, 703 ICS, 2000 full dictionary |
| **License (verified)** | Same MITRE royalty-free grant for *"research, development, and commercial purposes"*; provided "AS IS" |

**Reuse path.** CWE is the **canonical join key** for the entire corpus. Everything else in
this lane — Benchmark, Juliet, CyberSecEval, CVEfixes, ASVS, CodeQL, OWASP Top 10 — carries CWE
ids, so CWE is what lets a vet provision written once bind to test material from five sources.

Concretely, vendor the CSV for view 1000 and derive:

* `provisions[cwe-89] = {id, name, description, parents[], children[], mitigations[]}` —
  the `Potential_Mitigations` column is almost literally a list of compliant behaviours, i.e.
  candidate **factor names** (`uses_parameterized_query`, `input_validated_against_allowlist`).
* The CWE **hierarchy** gives free provision subsumption: if a case violates CWE-89, it also
  violates its parent CWE-943 / CWE-74 / CWE-707. That's a ready-made consistency oracle for
  testing whether the engine's provision closure is correct.
* CAPEC supplies the **attacker-side** vocabulary and `CAPEC -> CWE` links, useful if any vet
  provisions are phrased as threat obligations rather than code properties.

Attribution: ship MITRE's copyright + license text in `third_party/mitre/`. This is a hard
condition of the grant, not a courtesy.

**Access note.** In this sandbox, direct `curl` to `cwe.mitre.org` / `capec.mitre.org` was
refused by the egress proxy (`connect_rejected`); the pages resolve fine through WebFetch.
Anyone reproducing the download needs unrestricted egress.

---

## 6. Vulnerability data — CVE, NVD, OSV, GHSA, CVSS, CVEfixes

### CVE Records (cvelistV5)

* URL: https://github.com/CVEProject/cvelistV5 — the official CVE List, refreshed ~every 7 min.
* Format: CVE Record Format JSON, **schema 5.2.0** (Oct 2025), multi-container
  (CNA container + CVE Program container + ADP containers).
* Legacy CSV/HTML/XML/CVRF downloads **retired 30 June 2024** — this repo is the only
  supported bulk download.
* **License: UNVERIFIED.** The repo has **no root LICENSE file** (I fetched it: empty). The
  README says content may be used *"per the CVE Program Terms of Use"* at
  https://www.cve.org/Legal/TermsOfUse, which is JS-rendered and did not yield text to
  WebFetch. **Do not vendor until someone reads the actual ToU.**

### NVD

* API: NVD CVE API 2.0 (https://nvd.nist.gov/developers/vulnerabilities). Rate-limited;
  API key raises the limit and is non-transferable.
* **License (verified via ScanCode LicenseDB's record of the NVD API ToU):** *not* an
  explicit public-domain dedication. Conditions: display *"This product uses the NVD API but
  is not endorsed or certified by the NVD"*; may reference the NVD name to identify sources but
  not to imply endorsement; **if you modify the content you may not attribute the source as the
  NVD**; provided "as is".
* That last clause matters here — a compliance corpus *transforms* CVE/NVD records into cases.
  Transformed records must not be labelled as NVD data.

### OSV.dev

* URL: https://osv.dev — front page showed **875,340 vulnerabilities** across npm, PyPI,
  Debian, Go, Maven, crates.io, etc.
* Bulk: **`gs://osv-vulnerabilities`** GCS bucket, publicly browsable, per-ecosystem zips plus
  `modified_id.csv` for incremental sync.
* **License (verified):** `google/osv.dev` = **Apache-2.0**; `ossf/osv-schema` = **Apache-2.0**.
  The *aggregated records* carry the licenses of their upstream sources — check per ecosystem.
* Note: `api.osv.dev` was blocked by this sandbox's egress proxy; the GCS/docs paths resolved.

### GitHub Advisory Database

* URL: https://github.com/github/advisory-database
* **License (verified): CC-BY-4.0** (`LICENSE.md` = Attribution 4.0 International; README
  confirms "CC-BY 4.0").
* Format: one **OSV-format JSON file per advisory**, `GHSA-xxxx-xxxx-xxxx` ids.
* Sources: GitHub-reported advisories, NVD, npm, FriendsOfPHP, Go vuln DB, PyPA, RubySec, RustSec.
* **This is the cleanest-licensed vulnerability feed in the lane. Vendor this one.**

### CVSS (FIRST)

* v4.0 spec: https://www.first.org/cvss/v4.0/specification-document
* **License (verified):** FIRST *"licenses it to the public freely for use"*, conditioned on
  attributing CVSS ownership to FIRST and conforming to the spec's guidelines — including
  publishing **both** the numeric score and the vector string.
* v4.0 base metrics (verified): `AV:{N,A,L,P}` `AC:{L,H}` `AT:{N,P}` `PR:{N,L,H}` `UI:{N,P,A}`
  `VC/VI/VA:{H,L,N}` `SC/SI/SA:{H,L,N}`.

**Reuse path for CVSS — this is the sleeper.** A CVSS vector is *already* the exact data
structure the vet corpus needs: a fixed set of enumerated facts about a case, combined by a
published deterministic function into a disposition. Steal the *design*:

* Every CVSS metric is a candidate boolean/enum **factor** with a controlled vocabulary
  (`attack_vector_is_network`, `privileges_required_none`, `user_interaction_required`).
* CVSS's severity bands (None/Low/Medium/High/Critical) are a precedent for mapping
  factor facts to a graded **expected_disposition** rather than a bare boolean.
* CVSS conformance test vectors (score ↔ vector pairs) are a precedent for how to publish an
  oracle: publish both the inputs and the expected output, so any implementation can self-check.

### CVEfixes — realism with a clean license

| Field | Value |
|---|---|
| URL | https://github.com/secureIT-project/CVEfixes ; data DOI 10.5281/zenodo.4476563 |
| **License (verified)** | **code MIT** (`LICENSE.txt`), **data CC-BY-4.0** (badge in README + Zenodo record for v1.0.8) |
| Version | v1.0.8, CVEs through 23 July 2024 |
| Volume (verified, README + Zenodo agree) | **11,873 CVEs**, **272 CWE types**, **12,107 fix commits**, **4,249 projects**, **51,342 changed files**, **138,974 functions** |
| Format | Relational database (SQLite), interlinked at CVE / repo / commit / file / method levels |
| Ground truth | **Yes** — before/after code for each fixing commit, CWE- and CVSS-labelled |

**Reuse path.** This is the best **realistic** oracle in the lane and its data license
(CC-BY-4.0) is directly compatible with the target repo. Each `(file_before, file_after, CWE)`
triple is a natural compliance case: the *before* state is `violates(c, p_cwe) = true`, the
*after* state is `false`, and the diff is exactly the factor that flipped. That's a matched
pair drawn from real production code rather than a synthetic template — which is what makes it
complementary to Juliet.

### Other vulnerability datasets (all REFERENCE-ONLY)

| Dataset | URL | License | Note |
|---|---|---|---|
| Big-Vul (MSR'20) | `ZeoVan/MSR_20_Code_vulnerability_CSV_Dataset` | **MIT** on the repo | C/C++ CVEs 2002–2019, 21 features per entry incl. `cwe_id`, `cve_id`, CVSS sub-scores, `files_changed` patches, `version_before_fix`/`version_after_fix`. Upstream data provenance unverified. |
| Devign | `epicosy/devign` (mirror) | **MIT** on that mirror | Original NeurIPS'19 dataset is Google-Drive hosted; **original license UNVERIFIED** |
| DiverseVul | `wagner-group/diversevul` | **UNVERIFIED — no LICENSE file** | Do not vendor |
| VulRepair | `awsm-research/VulRepair` | **MIT** | Repair-oriented; ground truth = fix diffs |

---

## 7. Secret scanning

### Gitleaks — **VENDOR THIS**

| Field | Value |
|---|---|
| URL | https://github.com/gitleaks/gitleaks — rules at `config/gitleaks.toml` |
| **License (verified)** | **MIT** |
| Volume (verified by download) | **222 rules**, ~98 KB TOML |
| Schema (verified) | `id`, `description`, `regex`, `entropy`, `keywords[]` |

Sample verified entries: `1password-secret-key` (entropy 3.8), `1password-service-account-token`,
`adafruit-api-key`, `adobe-client-id` (entropy 2), `adobe-client-secret`…

**Reuse path.** The 222 `id` strings are a ready-made, MIT-licensed, machine-readable
**factor vocabulary** for the "no secrets in source" provision family:
`factor: secret_detected["aws-access-token"] = true`. The `description` fields are already
written as consequences ("could lead to unauthorized access to … and sensitive data exposure"),
which reads like provision rationale. The `entropy` thresholds are a precedent for
factors that are *derived* rather than asserted.

### TruffleHog — REFERENCE-ONLY

* URL: https://github.com/trufflesecurity/trufflehog
* **License (verified): AGPL-3.0.** AGPL is incompatible with vendoring into Apache-2.0.
* Vendor page claims **800+ detectors** with live provider verification.
* The *concept* worth borrowing: TruffleHog distinguishes **detected** from **verified**
  (the credential was actually live). That is a two-factor structure —
  `secret_matched_pattern` vs `secret_confirmed_active` — and a compliance corpus should
  model that distinction because it changes the disposition.

### SecretBench — REFERENCE-ONLY (data is gated)

| Field | Value |
|---|---|
| URL | https://github.com/setu1421/SecretBench |
| **License** | Repo **MIT** (verified) — **but the data is access-controlled** |
| Volume (from README) | **97,479 manually labeled secrets**, of which **15,084 are true secrets**, from **818 public GitHub repos**, 49 languages, 311 file types; built from 761 regexes |
| Ground truth | **Yes — manual true/false labels** |
| Blocker (quoted from README) | *"a data protection agreement has to be signed with us"*; data lives in Google BigQuery `dev-range-332204.secretbench.secrets` and a GCS bucket |

This is the best-labelled secrets corpus that exists, and the ~15% true-positive rate is itself
a useful calibration fact. But the DPA requirement means **it cannot be vendored** and probably
should not be depended on at all for an open corpus. Its *companion*,
`setu1421/FPSecretBench` (MIT, verified) — false positives reported by nine secret-detection
tools — is worth chasing for a false-positive factor set.

---

## 8. IDOR / broken access control / multi-tenant isolation

This is the highest-value category for veterinary software, because vet PMS platforms are
multi-tenant systems holding owner PII, payment data, and controlled-substance records. Every
one of these is an intentionally-vulnerable app, not a labelled dataset — so the reuse path is
**scenario templates**, not ground-truth rows.

| App | URL | License (verified) | Content |
|---|---|---|---|
| **OWASP crAPI** | https://github.com/OWASP/crAPI | **Apache-2.0** | **18 documented challenges + "3 secret challenges"** |
| **VAmPI** | https://github.com/erev0s/VAmPI | **MIT** | Flask API, 8 vuln classes, **OpenAPI 3 spec + Postman collection**, global vulnerable-on/off switch |
| OWASP Juice Shop | https://github.com/juice-shop/juice-shop | **MIT** | **116 challenges** in `data/static/challenges.yml` |
| OWASP WebGoat | https://github.com/WebGoat/WebGoat | **GPL-2.0-or-later** (SPDX in `LICENSE.txt`) | Lesson-based Java app |
| Tiredful-API | https://github.com/payatu/Tiredful-API | **GPL-3.0** | REST API training app |
| OWASP Vulnerable-Web-Application | https://github.com/OWASP/Vulnerable-Web-Application | **GPL-3.0** | — |
| Damn Vulnerable RESTful API (DVRA) | `ethicalhackingplayground/DVRA` | **UNVERIFIED — no LICENSE file** | Do not use |

**crAPI challenge inventory (verified from `docs/challenges.md`)** — this maps almost
one-to-one onto vet-practice scenarios:

| # | Challenge | Category | Vet analogue |
|---|---|---|---|
| 1 | Access details of another user's vehicle | BOLA | Another practice's patient record |
| 2 | Access mechanic reports of other users | BOLA | Another clinic's lab results |
| 3 | Reset the password of a different user | Broken Auth | Staff account takeover |
| 4 | API endpoint leaks sensitive info of other users | Excessive Data Exposure | Owner PII in a list endpoint |
| 5 | API endpoint leaks an internal property | Excessive Data Exposure | Internal flags on a record |
| 6 | Layer-7 DoS via "contact mechanic" | Rate Limiting | Appointment-request flood |
| 7 | Delete a video of another user | BFLA | Cross-tenant record deletion |
| 8 | Get an item for free | Mass Assignment | Invoice/refund manipulation |
| 9 | Increase your balance by $1,000+ | Mass Assignment | Billing tampering |
| 10 | Update internal video properties | Mass Assignment | Setting internal flags via API |
| 11 | Make crAPI call an external URL | SSRF | Outbound integration abuse |
| 12 | Free coupons without the code | NoSQL Injection | — |
| 13 | Redeem an already-claimed coupon | SQL Injection | Duplicate-claim via injection |
| 14 | Endpoint with no authentication check | Unauthenticated Access | Unprotected clinical endpoint |
| 15 | Forge valid JWT tokens | JWT | Token forgery |
| 16 | Prompt-inject the chatbot | **LLM** | AI assistant in the product |
| 17 | Extract another user's credentials via chatbot | **LLM** | — |
| 18 | Make the chatbot act on another user's behalf | **LLM** | Excessive agency |

Challenges 16–18 are directly on-point for an AI-authored-change regime and crAPI is
**Apache-2.0** — the only vulnerable-app in this set that can be vendored outright.

**VAmPI's on/off switch is the underrated feature.** Running the same API in vulnerable and
non-vulnerable modes yields matched pairs with identical surface and opposite disposition —
the cleanest possible test of whether a compliance rule is keying on the actual factor. Its
OpenAPI 3 spec also means endpoint/method/parameter names can be lifted mechanically into
factor names.

**Juice Shop `challenges.yml` (verified: 116 entries)** — schema is
`name, category, description, difficulty (1–6), hints[], mitigationUrl, key, tags[], disabledEnv[]`.
Verified category distribution:

| Category | n | | Category | n |
|---|---|---|---|---|
| Sensitive Data Exposure | 17 | | Security Misconfiguration | 5 |
| Injection | 14 | | Cryptographic Issues | 5 |
| Improper Input Validation | 12 | | Observability Failures | 4 |
| Broken Access Control | 12 | | Broken Anti Automation | 4 |
| XSS | 9 | | Security through Obscurity | 3 |
| Vulnerable Components | 9 | | Insecure Deserialization | 3 |
| Broken Authentication | 9 | | XXE | 2 |
| Miscellaneous | 6 | | Unvalidated Redirects | 2 |

Tags include `Danger Zone`, `Code Analysis`, `Brute Force`, `Good Practice`, `Prerequisite`.

**Reuse path.** `challenges.yml` is the closest existing analogue to the vet case file itself:
MIT-licensed, YAML, stable `key` identifiers, a graded `difficulty`, a `category` acting as a
provision bucket, and `mitigationUrl` pointing at the normative rule. **Adopt this file format
for the vet corpus** and vendor the file itself as a worked example.

---

## 9. SAST/DAST evaluation and AI-generated-code security

### CodeQL query suites — **VENDOR (queries only)**

* URL: https://github.com/github/codeql
* **License (verified): MIT** for the repository. README explicitly notes the **CodeQL CLI is
  in a separate repo and licensed separately**, and analyzing closed-source code with the CLI
  needs a commercial license. So: vendor the `.ql` sources and their metadata; do not bundle
  the CLI, and do not assume the vet company can run it commercially without a license.
* Structure: per-language `ql/src` query packs (`codeql/java-queries`, etc.) with
  `codeql-suites/*.qls` suite definitions; queries carry `@id`, `@tags security`, and
  `@security-severity`, and are organised by CWE directory (`CWE-089`, `CWE-079`, …).
  Each query ships with unit tests under `ql/test/query-tests/security/CWE-nnn/`
  containing `.expected` files.

**Reuse path.** CodeQL's `.expected` files are literally *expected-disposition oracles* for a
static analysis over a fixed input — the same contract the vet corpus wants. And the query
metadata block (`@id`, `@problem.severity`, `@security-severity`, `@tags`) is a good model for
provision metadata. The CWE-per-directory layout is a ready-made provision→test-case index.

### CyberSecEval / PurpleLlama — **VENDOR the subdirectory, read the note**

| Field | Value |
|---|---|
| URL | https://github.com/meta-llama/PurpleLlama, `CybersecurityBenchmarks/` |
| **License (verified)** | Repo root `LICENSE` = **Llama 3.2 Community License**. But **`CybersecurityBenchmarks/LICENSE` = MIT** (fetched and confirmed: "MIT License / Copyright (c) Meta Platforms, Inc."). The directory-local MIT governs the benchmark. |

Verified dataset inventory (downloaded and parsed):

| Dataset | Records | Fields |
|---|---|---|
| `datasets/instruct/instruct.json` | **1,916** | `prompt_id, file_path, pattern_desc, cwe_identifier, rule, analyzer, pattern_id, line_number, line_text, test_case_prompt, origin_code, language, variant, repo` |
| `datasets/autocomplete/autocomplete.json` | **1,916** | same schema |
| `datasets/prompt_injection/prompt_injection.json` | **251** | `prompt_id, test_case_prompt, user_input, judge_question, injection_variant, injection_type, risk_category, speaking_language` |
| `datasets/mitre/mitre_benchmark_100_per_category_with_augmentation.json` | **1,000** | `base_prompt, mutated_prompt_base, mutated_prompt, mitre_category, ttp_id_name_mapping` |

Verified language distribution for instruct/autocomplete: python 351, cpp 259, javascript 249,
csharp 235, java 229, c 227, rust 204, php 162. **50 distinct CWEs**; top: CWE-338 (183),
CWE-78 (166), CWE-120 (158), CWE-327 (131), CWE-807 (113), CWE-328 (105), CWE-680 (100),
CWE-502 (88), CWE-798 (78), CWE-95 (78), CWE-89 (70), CWE-94 (65).

**Reuse path — this is the best single source for the AI-authored-change angle.**

* Each record already binds `(natural-language prompt) -> (insecure code) -> (CWE) -> (detector
  rule that fires)`. That is a four-tuple a compliance case can be built from directly, with the
  `analyzer`/`rule`/`pattern_id` fields acting as the oracle: *this specific rule fires on this
  specific line*.
* `pattern_desc` is a corpus of ~50 CWEs' worth of plain-English violation statements — good raw
  material for provision text that doesn't inherit anyone's ShareAlike.
* The prompt-injection set's `judge_question` field is a precedent for storing the *evaluation
  question* alongside the case, which is worth copying if some vet dispositions need a rubric
  rather than a boolean.
* MIT means all of this can be vendored, with the caveat that you must vendor
  `CybersecurityBenchmarks/LICENSE` alongside it and be explicit that you are **not** taking the
  Llama-licensed parts of the parent repo.

### SecurityEval — REFERENCE-ONLY (license unverified)

* URL: https://github.com/s2e-lab/SecurityEval — also on HF as `s2e-lab/SecurityEval`.
* Volume: **121 prompts covering 69 CWEs** (v2.1, per README); HF page shows **121 rows**.
* Format: `dataset.jsonl` with `ID`, `Prompt`, `Insecure_code`; plus `Testcases_Prompt/`,
  `Testcases_Insecure_Code/`, and CodeQL/Bandit evaluation results.
* **License: UNVERIFIED.** No LICENSE file at repo root on `main` or `master`; no license shown
  on the HuggingFace dataset card. **Do not vendor.** Worth an email to the authors — it is a
  small, high-quality, CWE-keyed prompt set and a license grant would make it usable.

### LLMSecEval — REFERENCE-ONLY (license unverified)

* URL: https://github.com/tuhh-softsec/LLMSecEval ; Zenodo record 7581664 (v1.3, 8.1 MB zip).
* **License: UNVERIFIED.** No LICENSE file in the repo; Zenodo lists **"Other (Open)"** with no
  terms specified. Ambiguous "open" is not a license. **Do not vendor.**

---

## 10. Prompt injection / agent attack benchmarks

### AgentDojo — **VENDOR**

| Field | Value |
|---|---|
| URL | https://github.com/ethz-spylab/agentdojo ; https://agentdojo.spylab.ai/ ; arXiv 2406.13352 |
| **License (verified)** | **MIT** |
| Volume (verified from the paper abstract) | **97 realistic tasks** + **629 security test cases** |
| Environments | email/workspace, e-banking, travel booking, Slack |
| Ground truth | **Yes, two-dimensional** — a *utility* check (did the agent do the legitimate task?) and a *security* check (did the injection succeed?) |

**Reuse path — the two-axis oracle is the important idea.** AgentDojo does not ask "was the
agent safe"; it asks two independent questions and reports both. A compliance corpus for
AI-authored changes needs exactly that shape: a change can be *compliant but useless* or
*useful but non-compliant*, and collapsing them to one boolean hides the interesting failures.
Model `expected_disposition` as at least `(task_completed, provisions_violated[])`.

### InjecAgent — **VENDOR**

| Field | Value |
|---|---|
| URL | https://github.com/uiuc-kang-lab/InjecAgent ; arXiv 2403.02691 |
| **License (verified)** | **MIT** (`LICENCE`, British spelling) |
| Volume (README) | **1,054 test cases**, **17 user tools**, **62 attacker tools** |
| Verified by download | `data/test_cases_dh_base.json` = **510 cases** (direct-harm, base setting); `data/user_cases.jsonl` also present |
| Schema (verified) | `Attacker Tools, Modifed, Attacker Instruction, Expected Achievements, Attack Type, User Tool, User Instruction, Tool Parameters, Tool Response Template, Thought, Tool Response` |
| Attack types | e.g. `Physical Harm`, plus data-stealing variants |
| Ground truth | **Yes** — `Expected Achievements` states what a successful attack accomplishes |

**Reuse path.** `Expected Achievements` is a natural-language *disposition oracle* per case, and
`Attack Type` is a small controlled vocabulary that could seed a `harm_category` factor. The
`(User Instruction, Tool Response containing injection, Attacker Instruction)` triple is the
canonical structure for an indirect-prompt-injection case — reusable verbatim for
"agent reads a vet clinic's ticket queue and the ticket contains instructions".

### OWASP LLM Top 10 test material

No machine-readable test corpus found — the project ships prose/PDF under CC-BY-SA-4.0.
Use the LLM01–LLM10 ids as provision labels only.

---

## 11. Concurrency / race conditions

| Field | Value |
|---|---|
| Name | SCTBench |
| URL | https://github.com/mc-imperial/sctbench |
| **License (verified)** | **MIT** (`LICENSE.txt`, Imperial College London, 2021) |
| Contains | C/C++ pthread benchmarks + tooling for evaluating systematic concurrency testing (schedule bounding, PCT) |
| Ground truth | Partial — known concurrency bugs, but the README explicitly warns the *race-detection phase is nondeterministic* and results vary with compiler version |
| Volume | **UNVERIFIED** — not stated in the README I fetched |

Also noted but not verified in depth: `marchartung/DataRaceBenchmark` (C++ pthread cases for
benchmarking concurrency testing) and `wcventure/PERIOD` (ICSE 2022).

**Reuse path — limited, and be honest about why.** SCTBench is MIT so it can be vendored, but
its own authors say the evaluation is non-deterministic. That makes it a poor *oracle* and a
good *cautionary provision*: it is direct evidence for a corpus design rule that concurrency
provisions must be expressed as properties of the code (`shared_state_mutated_without_lock`)
rather than as observed test outcomes, because the observation is flaky. Juliet's concurrency
CWEs (CWE-362 and relatives) are a better-behaved source for actual cases, and they're CC0.

---

## 12. Recommended composition for the vet corpus

**Vendor tier (safe in an Apache-2.0 / CC-BY-4.0 repo):**

```
third_party/
  sard-juliet/        CC0 1.0 / public domain   -> matched-pair cases, factor grammar
  mitre-cwe/          MITRE license + copyright -> provision table, hierarchy, mitigations
  mitre-capec/        MITRE license + copyright -> attacker-side vocabulary
  ghsa/               CC-BY-4.0                 -> real advisories in OSV format
  cvefixes/           CC-BY-4.0                 -> realistic before/after matched pairs
  gitleaks-rules/     MIT                       -> 222 secret-detection factor names
  juiceshop-yml/      MIT                       -> case-file format exemplar (116 cases)
  crapi/              Apache-2.0                -> 18 multi-tenant/BOLA/LLM scenarios
  vampi/              MIT                       -> vulnerable/non-vulnerable matched pairs
  cyberseceval/       MIT (dir-local)           -> 1,916 AI-code cases + 251 injection cases
  agentdojo/          MIT                       -> two-axis utility/security oracle
  injecagent/         MIT                       -> 1,054 indirect-injection cases
  codeql-queries/     MIT                       -> .expected files as disposition oracles
  sctbench/           MIT                       -> concurrency (weak oracle; see §11)
```

**Reference tier (cite ids, never copy text):** ASVS, OWASP Top 10 / API Top 10 / LLM Top 10 /
WSTG (all CC-BY-SA-4.0); OWASP Benchmark and WebGoat (GPL); TruffleHog (AGPL); NVD and CVE
(terms-restricted or unverified).

**Do-not-touch until licensed:** SecurityEval, LLMSecEval, DiverseVul, DVRA, SecretBench data.

**Suggested provision skeleton** — layering the citations so each case exercises several
granularities at once:

| Vet provision | Aligned to | Oracle source |
|---|---|---|
| VET-AUTHZ-1 cross-practice record access | API1:2023, A01:2025, CWE-639, ASVS V8 | crAPI 1–2, VAmPI BOLA, Juliet CWE-639 |
| VET-INJ-1 clinical query construction | A05:2025, CWE-89 | Juliet CWE-89, Benchmark sqli (504 cases), CVEfixes |
| VET-SECRET-1 no credentials in source | CWE-798 | Gitleaks 222 rules, CyberSecEval CWE-798 (78) |
| VET-CRYPTO-1 approved algorithms only | A04:2025, CWE-327/328 | Benchmark crypto+hash (482), CyberSecEval CWE-327/328 (236) |
| VET-AI-1 agent-authored change review | LLM01, LLM06 | AgentDojo (629), InjecAgent (1,054), CyberSecEval PI (251) |
| VET-LOG-1 audit trail for clinical records | A09:2025, CWE-778 | ASVS V16, Juice Shop "Observability Failures" (4) |

---

## Sources

- [OWASP Benchmark for Java](https://github.com/OWASP-Benchmark/BenchmarkJava)
- [OWASP Benchmark for Python](https://github.com/OWASP-Benchmark/BenchmarkPython)
- [OWASP Benchmark project page](https://owasp.org/www-project-benchmark/)
- [OWASP Juice Shop](https://github.com/juice-shop/juice-shop)
- [OWASP WebGoat](https://github.com/WebGoat/WebGoat)
- [OWASP ASVS](https://github.com/OWASP/ASVS)
- [OWASP WSTG](https://github.com/OWASP/wstg)
- [OWASP Top 10](https://github.com/OWASP/Top10) / [Top 10:2025](https://owasp.org/Top10/2025/)
- [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [OWASP crAPI](https://github.com/OWASP/crAPI) / [challenges](https://github.com/OWASP/crAPI/blob/develop/docs/challenges.md)
- [VAmPI](https://github.com/erev0s/VAmPI)
- [NIST SARD](https://samate.nist.gov/SARD/) — [Juliet C/C++ 1.3](https://samate.nist.gov/SARD/test-suites/112), [Juliet Java 1.3](https://samate.nist.gov/SARD/test-suites/111), [Juliet C/C++ 1.3.1](https://samate.nist.gov/SARD/test-suites/116)
- [CWE Terms of Use](https://cwe.mitre.org/about/termsofuse.html) / [CWE Downloads](https://cwe.mitre.org/data/downloads.html)
- [CAPEC Terms of Use](https://capec.mitre.org/about/termsofuse.html) / [CAPEC Downloads](https://capec.mitre.org/data/downloads.html)
- [CVE List V5](https://github.com/CVEProject/cvelistV5) / [CVE Terms of Use](https://www.cve.org/Legal/TermsOfUse)
- [NVD CVE API 2.0](https://nvd.nist.gov/developers/vulnerabilities) / [NVD API ToU as recorded by ScanCode LicenseDB](https://scancode-licensedb.aboutcode.org/nist-nvd-api-tou.html)
- [OSV.dev](https://osv.dev/) / [FAQ](https://google.github.io/osv.dev/faq/) / [osv-schema](https://github.com/ossf/osv-schema)
- [GitHub Advisory Database](https://github.com/github/advisory-database)
- [CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document)
- [CVEfixes](https://github.com/secureIT-project/CVEfixes) / [Zenodo v1.0.8](https://zenodo.org/records/13118970)
- [Big-Vul](https://github.com/ZeoVan/MSR_20_Code_vulnerability_CSV_Dataset)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) / [detectors](https://trufflesecurity.com/detectors)
- [SecretBench](https://github.com/setu1421/SecretBench) / [FPSecretBench](https://github.com/setu1421/FPSecretBench)
- [CodeQL](https://github.com/github/codeql)
- [PurpleLlama / CyberSecEval](https://github.com/meta-llama/PurpleLlama)
- [SecurityEval](https://github.com/s2e-lab/SecurityEval) / [HuggingFace](https://huggingface.co/datasets/s2e-lab/SecurityEval)
- [LLMSecEval](https://github.com/tuhh-softsec/LLMSecEval) / [Zenodo](https://zenodo.org/records/7581664)
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) / [paper](https://arxiv.org/abs/2406.13352)
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)
- [SCTBench](https://github.com/mc-imperial/sctbench)
