# Sources: what was reusable, what was not, and why

Four independent surveys were run over open test data before a line of this corpus was written — clinical interoperability, application security, policy-as-code and supply chain, and computational legal reasoning. The full reports, with URLs and per-source detail, are in `research/`. This document is the decision record: what we reused, what we deliberately did not, and what a later maintainer should reopen.

Every licence below was verified by fetching the primary terms page or the repository's own `LICENSE` file. Where verification failed, the row says so. **A licence we could not verify is treated as reference-only.**

---

## 1. The four headline findings

**No factor-annotated legal case base is downloadable under any licence.** The CATO/HYPO US Trade Secret factor base — the corpus every formal precedent paper cites — exists only inside copyrighted papers. Liverpool's repository, van Woerkom's and Prakken's repositories, and the ICAIL/JURIX proceedings were all checked. Recent work has fallen back to *generating* synthetic factor triples, which is what this corpus does too. The factor vocabulary here is built, not acquired, and that is a finding about the field rather than a shortcut.

**No veterinary FHIR implementation guide exists.** There is the `patient-animal` extension, HL7 Europe's ballot lab profile, and exactly one regulatory-context veterinary fixture in the world: `Patient-pdmp-patient-2-veterinary` in the HL7 US PDMP guide, under CC0. The FHIR `animal-species` value set contains ten livestock codes and neither dog nor cat, and is example-binding only. Veterinary software's interoperability substrate is thinner than its regulatory exposure.

**The most tempting security corpora are the least reusable.** OWASP Benchmark is **GPL-2.0**, not permissive, despite being the standard structural model for expected-result test suites. Every OWASP *standard* — ASVS, Top 10, API Top 10, WSTG, LLM Top 10 — is **CC BY-SA 4.0**, whose ShareAlike term is incompatible with a CC BY 4.0 corpus. NVD is not public domain: its terms forbid attributing modified content to NVD, which is exactly what a corpus that transforms records into cases would be doing.

**Conformance-suite design is a solved problem elsewhere and we borrowed from it.** test262's per-case metadata with a declared `negative: {phase, type}` block; the Bean Validation TCK's four-state coverage report including an explicit *untestable* category; web-platform-tests' separation of expectations from cases; sqllogictest's `label` (two fact patterns must reach the same disposition — which is precisely our like-case pair); sigstore-conformance's `must_pass`/`must_fail` polarity and `xfail` globs; and the Jakarta EE TCK's challenge process, which distinguishes appealing a case's *outcome* from appealing the *procedure*. All five shaped this repository.

---

## 2. What this corpus actually reuses

Nothing is redistributed. What was reused is **structure** — schema shapes and suite conventions — and **identifiers**, which are facts.

| Source | Licence (verified) | How it is used here |
| :---- | :---- | :---- |
| US CFR (21 CFR 530, 558, 1300–1321; 9 CFR 1–4; 45 CFR 160.103) | Public domain (US Government work) | The regulatory backbone of the constitution. Cited per provision in `constitution/rulebook.json`; prose is original paraphrase. |
| EU AI Act Art. 5; GDPR Art. 22, 32 | CC BY 4.0 via Commission Decision 2011/833/EU | Two absolute provisions (VP-GV-001, VP-GV-002) and three ordinary ones. |
| CWE / CAPEC (MITRE) | Royalty-free, attribution required | Nine AppSec and RBAC provisions cite CWE ids as classification. Identifiers only; no CWE text is copied. |
| Gitleaks rule schema | MIT | Informed the secret-scanning factor vocabulary (VP-SC-008). |
| ASAP 4.2B field identifiers (`PAT20` species code, `PAT23` animal name) | Field identifiers are facts; the standard document is $500 and is not redistributed | The PDMP factor vocabulary (VP-CS-009). Montana and Louisiana genuinely disagree on PAT23 format — that disagreement is the seed of the W-crossjurisdiction category. |
| DICOM veterinary attributes (0010,2201 / 2202 / 2292–2299, from CP-643 and CP-1478) | Verified in DICOM PS3.3 §C.7; freely citable | The POC diagnostics factor vocabulary (VP-PO-004). |
| LOINC veterinary panel codes | Royalty-free with a mandatory verbatim notice | Referenced by name only in VP-PO-005. The real compliance fact — that IDEXX, Heska and Abaxis analyzers do not natively emit LOINC — is modelled as `analyzer_result_mapped_to_loinc_code`. |
| openFDA Animal & Veterinary adverse events | CC0 1.0 | Informed realistic species / drug / route distributions. No records are vendored. |
| DEA schedules (21 CFR 1308) | Public domain | The controlled-substance list in `generator/vocab.py`. |
| test262, wpt, sqllogictest, sigstore-conformance, Jakarta EE TCK | various open | Suite-design conventions: declared polarity, path-shaped ids, computed-not-asserted checks, a documented challenge route. |
| OPA/Gatekeeper `suite.yaml`, Kyverno `kyverno-test.yaml`, Cedar integration tests | Apache-2.0 | The shape of the `expect` block, especially Cedar's `reason` field — expected results that name *which provisions fired*, which is what makes an expectation auditable. |
| OSCAL catalog/profile model | US public domain + CC0 | The constitution's catalog → family → provision → factor structure. |

---

## 3. What was deliberately not used

| Source | Why not |
| :---- | :---- |
| OWASP Benchmark (2,740 cases, 1,415 true / 1,325 false) | **GPL-2.0.** The `expectedresults` CSV is the best structural model available and we copied the *schema idea* and nothing else. |
| OWASP ASVS, Top 10, API Top 10, WSTG, LLM Top 10 | **CC BY-SA 4.0.** ShareAlike is viral and incompatible with CC BY 4.0. Requirement ids are cited as facts; all provision prose here is original. |
| NVD / CVE Records | NVD's terms forbid attributing modified content to NVD. CVE's `cvelistV5` has no `LICENSE` file at all. Use the GitHub Advisory Database (CC BY 4.0) instead if vulnerability data is ever needed. |
| TruffleHog | AGPL-3.0. Its detected-versus-*verified* distinction is worth modelling as two factors; the code is not vendorable. |
| SecretBench (97,479 labelled secrets) | Repository MIT, **data gated behind a signed agreement**. |
| SecurityEval, LLMSecEval, DiverseVul | No `LICENSE` file located, including on Hugging Face. Unverified means reference-only. |
| PCI DSS | Terms explicitly forbid distributing, copying or making derivative works. VP-PD-001 states the obligation in original words. |
| SNOMED CT and the veterinary extension; AAHA Diagnostic Terms; VeNom | Affiliate licence, gated agreement, and signed letter agreement respectively. AAHA's ~5,600 companion-animal terms are the single highest-value unresolved item — worth an approach to AAHA. |
| Plumb's Veterinary Drugs | Proprietary. DailyMed's ~3,550 animal SPL labels are the open substitute and are arguably the better compliance oracle, since label doses are what conformance is measured against. |
| OpenVPMS | Custom licence that charges practices a subscription; not Apache-compatible. |
| Abaxis VetScan ASTM specification | Marked confidential. |
| COLIEE; Pile of Law; LePaRD; FairLex; AUEB `ecthr_cases` | Gated registration, or non-commercial terms. |
| OpenFisca | AGPL-3.0. |
| CIS Benchmarks; ISO/IEC 42001; Backstabber's Knife Collection | Non-redistributable or gated. |
| SPDX `license-list-data` | **No licence file at all** (LICENSE, .md, .txt, COPYING all 404; GitHub reports NOASSERTION). ScanCode LicenseDB (CC BY 4.0 data / Apache-2.0 code) is the licensed alternative. |
| van Woerkom & Prakken's COMPAS case-base inconsistency implementation | No licence in the repository. Their inconsistency *criterion* is the only formal, empirically applied definition we found; it should be re-implemented from the published definition, not copied. |

---

## 4. Open items for a maintainer

1. **AAHA Diagnostic Terms.** Claims "reciprocal open-source licenses" but is gated behind an AAHA agreement plus a UMLS/SNOMED licence number. Resolving this would give the corpus a real clinical terminology instead of a constructed one.
2. **SecurityEval.** 121 prompts across 69 CWEs, high quality, small, no licence file. Worth emailing the authors for an explicit grant; it is the best fit for the `VP-AI-*` family.
3. **SARA (statutory reasoning).** The closest existing analogue to a machine-checkable constitution, and it states no licence. Worth an approach to the authors.
4. **State veterinary board disciplinary registers.** The only real veterinary adjudications with facts, charges and dispositions anywhere. Scattered across fifty sites with inconsistent copyright postures; a per-state review would unlock the highest-value precedent seeds in the domain and would let the seeded jurisprudence of the X-coldstart category be real rather than constructed.
5. **`pydicom-data`.** Its `LICENSE` 404s on both branches and it carries 97 external files. Do not vendor until resolved.
6. **A consistency benchmark does not exist.** Nothing in the legal-NLP literature measures decision consistency as a primary endpoint. The 200 like-case pairs here are, as far as these four surveys could establish, the first open set engineered for that measurement in a compliance setting. That is a claim about what we found, and it invites correction.
