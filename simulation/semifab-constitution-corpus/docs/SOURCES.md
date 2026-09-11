# Sources: what was reusable, what was not, and why

Four independent surveys were run over open test data before a line of this corpus was written — SEMI standards and fab datasets, software supply-chain provenance, export control and NIST, and real-time/concurrency/agent-code. The full reports, with URLs and per-source detail, are in `research/`. This document is the decision record.

Every licence below was verified by fetching the primary terms page or the repository's own `LICENSE` file. Where verification failed, the row says so. **A licence we could not verify is treated as reference-only.**

---

## 1. The five headline findings

**SEMI standards are not redistributable, and the licence is stricter than most people assume.** Verified verbatim from SEMI's own licence document: the grant is to use the files "internally on **a single computer**", and "You may not copy… **share through an internal computer network** or otherwise transfer or distribute the Files." Verified prices: E30 $286–380, E5 $286, E4 $148–193, E134 $148–236. No SEMI text appears anywhere in this repository. Designations and codes — `E30`, `S7F23`, `ACKC7`, `Select.req` — are names of things rather than protected expression, and are used as facts.

**No public SECS/HSMS packet capture exists.** This was checked rather than assumed: the ITI ICS-Security-Tools collection holds 726 pcaps across 21 industrial protocols and contains **zero** SECS or HSMS captures. Anyone needing real message fixtures must generate them. `go-secs` (Apache-2.0) is the way to do it — its `sml/testdata/common.sml` carries **189 named message fixtures across 140 distinct stream/function codes**, including S7F23 formatted process program send and S16F15 create process job, and it ships a loopback benchmark harness with realistic payloads (a 100 kB wafer map, a 1 MiB recipe blob).

**US federal law is public domain and is the backbone of this constitution.** GovInfo restates 17 U.S.C. §105 directly, and NIST publishes its own statement that works authored by NIST employees are not subject to copyright within the United States. That makes 15 CFR (EAR), 22 CFR (ITAR), 15 CFR Part 231 (CHIPS guardrails), 15 U.S.C. §4652, and SP 800-53r5 / 800-161r1 / 800-171r3 / 800-218 / CSF 2.0 all safe to cite and paraphrase. `usnistgov/oscal-content` is **CC0** and is the best single asset in the lane — its catalog/profile split is the model this constitution follows, with the absolute provisions playing the role of a baseline profile.

**The single most useful export-control finding is not an export rule at all.** 15 CFR **762.5(b)(4)** requires that a records system "preserve the initial image … and record all changes, who made them and when they were made", and (b)(8) requires an audit trail of "where, when, by whom, and on what equipment". That is a **statutory append-only-log-with-attribution requirement**, not a security best practice — and it is the same property Chapter 5's A5 secures by construction. SF-EX-003 and SF-WI-001 are drafted straight onto it.

**No open export-control or data-residency policy library exists.** OPA's own policy library has none; Cedar ships none. Both were checked directly. That is a genuine gap, and it is part of what this corpus is for.

---

## 2. What this corpus actually reuses

Nothing is redistributed. What was reused is **structure** — schema shapes and suite conventions — and **identifiers**, which are facts.

| Source | Licence (verified) | How it is used here |
| :---- | :---- | :---- |
| 15 CFR 730–774 (EAR), incl. §734.9, §734.13, §734.18, §744.23, §762.5, §762.6, §764.2 | Public domain (17 U.S.C. §105, restated on GovInfo) | Six of the twenty absolute provisions and seven ordinary ones. §762.5(b)(4) is quoted in substance as the record-immutability floor. |
| 15 CFR Part 231; 15 U.S.C. §4652 (CHIPS guardrails) | Public domain | SF-NC-004. §231.301's "regardless of claimed exception" is why the provision is drafted as a notification duty rather than a judgment. |
| NIST SP 800-53r5, 800-161r1, 800-171r3, 800-218 | Public domain within the US, attribution requested | The NC family. |
| `usnistgov/oscal-content` | **CC0 1.0** (verified from LICENSE.md) | The catalog/profile serialisation model for `constitution/rulebook.json`. |
| Consolidated Screening List (trade.gov) | data.gov licence field = `usa.gov/publicdomain/label/1.0` — **verified public domain** | SF-EX-004's factor vocabulary. Its own disclaimer, that the Federal Register must still be checked, is itself modelled as a provision. |
| EU AI Act Art. 5; GDPR Art. 17, 22, 28, Ch. V; EU Data Act Art. 32 | CC BY 4.0 under Commission Decision 2011/833/EU | SF-GV-001, SF-GV-002, SF-DS-002, SF-DS-003. |
| SECS/GEM identifiers via `go-secs` (Apache-2.0) SML testdata | Identifiers are facts; go-secs itself Apache-2.0 | The SG family's factor vocabulary: S1F13, S5F1, S6F11, S7F23, S9F9, S16F15, HSMS T3/T5/T6/T7/T8, `ONLINE_REMOTE`, `CONNECTED_SELECTED`. |
| SEMI E10 equipment-state names | Designations cited as facts | `e10_state_reporting_unchanged_by_change`. |
| `slsa-verifier` testdata and its sentinel error set (Apache-2.0) | Apache-2.0 (LICENSE read) | The SS family's provenance factors: `provenance_attestation_verified_against_expected_builder_id`, `builder_id_mismatch_in_provenance`, `reusable_workflow_reference_in_trusted_workflow_set`. |
| OSPS Baseline (`ossf/security-baseline`) | Apache-2.0 | `pipeline_denies_privileged_credentials_to_untrusted_code` and `pipeline_sanitises_untrusted_metadata_before_use` are OSPS-BR-01.03 and OSPS-BR-01.01 restated. Its MUST/SHOULD modality and `state: Retired` idiom informed how provisions are versioned. |
| `sbom-utility` drift corpus (Apache-2.0) | Apache-2.0 | `component_integrity_drift_detected` — a changed hash under an unchanged version — is the sharpest supply-chain factor in the corpus, and it came from there. Its semantically-null negatives (array reordering) are why `drift_is_semantically_null` exists as a guard. |
| CycloneDX `sbom-examples` | **CC0 1.0** | SBOM factor vocabulary. |
| Project Wycheproof (`C2SP/wycheproof`) | Apache-2.0 | The CR family's failure classes: `invalid_signature_accepted_by_verifier`, `nonce_reuse_possible_under_concurrency`. Its `tcId` / `flags` / `result` / `notes` record shape is close to this corpus's own and was a model for it. |
| NIST CAVP/ACVP vectors | US Government public domain | SF-CR-004, which deliberately separates `known_answer_test_passed` from `algorithm_has_current_validation_certificate` — NIST's own caveat is that using the vectors does not replace validation. |
| HdrHistogram (CC0 / BSD-2-Clause dual) and wrk2 (Apache-2.0) | verified in LICENSE.txt | The RT family's coordinated-omission factor. `measurement_corrects_coordinated_omission` being *false* is itself a violation, which is the point of the methodology. |
| `rtla` interrupt-versus-thread budget split | GPL-2.0 (methodology cited, no code used) | `budget_scope_is_interrupt_context` / `_task_context`. |
| jcstress outcome vocabulary | GPL-2.0 with Classpath exception (vocabulary cited) | SF-TQ-002's requirement that an enumerated expected-outcome set accompany a weakened synchronisation primitive. Binary pass/fail is too coarse for concurrency. |
| JaConTeBe concurrency defect classes | taxonomy cited; corpus itself unverified | `defect_class_is_data_race` / `_atomicity_violation` / `_resource_deadlock` / `_toctou`. |
| Pact specification `testcases/` | MIT | SF-AG-006 and the contract-break axes `api_contract_broken_on_path_axis` / `_body_axis`. |
| CWE (MITRE) | Royalty-free, attribution required | The AS and TQ families cite CWE ids as classification. CWE™ is a trademark of The MITRE Corporation. |
| ComplianceAsCode/content | BSD-3-Clause | The rule-YAML idiom of `identifiers:` and `references:` — why every provision here carries a citation and a source-status field. |
| test262, wpt, sqllogictest, sigstore-conformance, Jakarta EE TCK | various open | Suite-design conventions: declared polarity, expectations separate from cases, computed-not-asserted checks, and a documented route to challenge a case. |

---

## 3. What was deliberately not used

| Source | Why not |
| :---- | :---- |
| SEMI E4, E5, E30, E37, E87, E90, E116, E134, E157 | Single-computer licence; network sharing forbidden. Designations cited, no text reproduced. |
| `secsgem` | LGPL-2.1-or-later. Its 124 stream/function classes with official names are the richest vocabulary in the lane, but the files cannot be copied into an Apache-2.0 tree. Use it as an unmodified dependency, or re-derive the code list as facts (which is what this corpus does). |
| Wireshark `packet-hsms.c` | GPL-2.0. Its 27 display-filter field names are a citable namespace and `tshark` is a free oracle; the code is not vendorable. |
| **semgrep-rules** | **Not open source.** The Semgrep Rules License v1.0 permits use "only for your own internal business purposes" and "does not allow you to distribute the rules". The fork `opengrep-rules` is LGPL-2.1 **plus Commons Clause**. Use CodeQL (MIT) instead. This finding is why `policy_rule_source_is_redistributable` exists as a factor: a disposition resting on a non-redistributable rule is not independently reproducible. |
| AFL++ | Defaults to **AGPL-3.0-or-later**; `testcases/` carries no separate statement. |
| diffoscope | GPL-3.0-or-later. Its 189 fixtures and 67 `*_expected_diff` triples are the richest matched-pair data in the supply-chain lane, and unusable here. |
| `spdx-examples` `content/` | The SPDX documents are CC0, but the source code in `content/` is **GPL-3.0-or-later**. Take the documents, leave the code. |
| Both public dependency-confusion PoC repositories | **No LICENSE file at all** — all rights reserved. |
| Backstabber's Knife Collection | Institutional-email gated, no licence stated. |
| OSS-Fuzz corpora | **Not public** — access requires being listed in the project's own `project.yaml`. ARVO (BSD-2-Clause, 6,138 reproducible vulns with vulnerable/fixed pairs) is the open substitute. |
| WM-811K, MixedWM38, NASA/PHM CMP | No licence stated / IEEE DataPort subscription / attribution request without a grant. Vocabulary only. |
| ASC X12 | Verified tiered fees, $180–$3,600/yr. |
| EPCIS | Its `LICENSE` file is a disclaimer, not a grant. |
| OPC UA Compliance Test Tool (UACTT) | Members-only. The UA-Nodeset XMLs are usable under the OPC Foundation MIT 1.00 header — keep the headers, there is no root LICENSE file. |
| PRC DSL, Taiwan National Security Act, Korea Industrial Technology Protection Act | Official texts are not published under a reuse licence reachable from here; `law.moj.gov.tw` is robots-blocked. Obligations are paraphrased in original words and marked reference-only. |
| PCI DSS, ISO/IEC 42001, CIS Benchmarks | Non-redistributable. |
| SV-Benchmarks task data | The BenchExec **task-definition format** is Apache-2.0 and was adopted as a model. The 34,700-task corpus is heterogeneous per directory with an unfinished licence audit — vendor per-directory or not at all. |
| OSADL latency data | "All rights reserved". |
| `depscope-hallucinations-dataset` | CC BY-**NC**-SA — disqualifying. |

---

## 4. Open items for a maintainer

1. **Nine citations need re-verification against primary sources before anyone relies on them**, chiefly the 3A090 total-processing-performance thresholds (currently from a law-firm secondary source), the Consolidated Screening List developer terms of service, OFAC file names and terms, and EUR-Lex's own legal notice, which would not render during the survey. The EAR changes constantly and this constitution records a retrieval date for that reason.
2. **Two rules are on the books but not in force.** The AI Diffusion Rule was rescinded in policy in May 2025 but remains in the CFR under non-enforcement; the Affiliates Rule is suspended to November 2026. Both are modelled as ordinary provisions rather than absolute, and a maintainer should re-check their status. "Law on the books, not in force" is a genuinely hard case class and deserves its own category in a later revision.
3. **The GDPR Art. 17 versus 15 CFR 762.6 collision is a real two-floor conflict**, and it is the best hard-case generator in this domain: an erasure request against a record under an export-control retention duty. SF-DS-002 resolves it by making the hold win, which is a defensible reading and not the only one. It is exactly the kind of provision a deployment should expect to be contested.
4. **No open (approved SBOM, drifted SBOM) pair corpus exists**, and no open labelled dependency-confusion corpus exists. Both had to be synthesised here. Building them from CC0 CycloneDX documents would be a genuinely useful contribution to the wider ecosystem.
5. **AAHA-style terminology gating has a semiconductor analogue.** SEMI's paywall means the richest vocabulary in the domain — the full stream/function table with official names — cannot be shipped openly by anyone. `go-secs` and `pysemisecs` between them make it re-derivable, and that is worth doing once, properly, as a standalone Apache-2.0 dataset.
