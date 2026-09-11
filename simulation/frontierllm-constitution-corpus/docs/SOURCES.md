# Sources: what was reusable, what was not, and why

Four independent surveys were run before a line of this corpus was written — LLM security and red-team corpora, model and dataset provenance, AI regulation and frontier safety frameworks, and evaluation/drift/inference infrastructure. The full reports, with URLs and per-source detail, are in `research/`. This document is the decision record.

Every licence below was verified by fetching the repository's own `LICENSE` file, the dataset card, or the primary terms page. Where verification failed, the row says so. **A licence we could not verify is treated as reference-only.**

---

## 1. The seven findings that shaped this corpus

**The AI Act's high-risk regime is deferred.** Regulation (EU) 2026/1744 — the Digital Omnibus on AI, adopted 8 July 2026, in force 27 July 2026 — moved Articles 9–15 to 2 December 2027 for Annex III systems and 2 August 2028 for Annex I. Still in force: Article 5 prohibitions (February 2025), Articles 51–56 GPAI (August 2025), Article 50 transparency and GPAI enforcement (August 2026). A new Article 5 prohibition covering non-consensual intimate imagery and CSAM binds from 2 December 2026. **Any corpus that assumed Articles 9–15 bind today would be wrong**, and that finding is why every provision here carries a `status` field and why the build refuses to mark a deferred provision absolute.

**California SB 53 is the only law anywhere that binds frontier developers directly.** In force 1 January 2026. Thresholds: 10²⁶ FLOP training compute and $500M revenue. It requires a published framework covering unreleased-weight cybersecurity, 15-day incident reporting with a 24-hour path for imminent risk, and carries $1M penalties. It sits beside — and does not align with — the AI Act's 10²⁵ presumption, which is the whole substance of this corpus's W-crossjurisdiction category.

**EO 14110 is rescinded** (by EO 14179, January 2025), so its 10²⁶ trigger is not current federal law. EO 14365 (December 2025) created a litigation task force to challenge state AI laws, so state provisions are under active preemption pressure. Colorado's SB 24-205 was replaced by SB 26-189, effective 1 January 2027.

**All four lab frontier frameworks are all rights reserved.** Google DeepMind's Frontier Safety Framework, Anthropic's Responsible Scaling Policy, OpenAI's Preparedness Framework and Meta's Frontier AI Framework carry no licence notice; Anthropic's terms reserve everything expressly. They are paraphrased here and cited by link, never quoted. **The Seoul Frontier AI Safety Commitments are UK Open Government Licence v3.0** and are the quotable source for the same obligation, which is why FL-SF-001 cites them first.

**RAND's *Securing AI Model Weights* is noncommercial-use-only**, not Creative Commons; reproduction requires permission. Its SL1–SL5 security levels informed FL-SF-002 and FL-SF-003 by paraphrase only. **The openly licensed alternative exists**: the SL5 Standard for AI Security publishes 60 controls across 12 families under CC BY 4.0 prose with an OSCAL profile over NIST SP 800-53r5.

**Judge–human agreement is not one number.** MT-Bench reports above 80% GPT-4–human agreement, equal to human–human; AlpacaEval measures 68.1%; JudgeBench finds GPT-4o "slightly better than random guessing" on its harder split. A provision that says "use an LLM judge" without stating which judge, on which task family, at what measured agreement, is not a provision. FL-EV-006 requires the measurement per configuration and FL-EV-007 requires an objective checker where one exists.

**Agent loop-limit defaults differ by three orders of magnitude.** Verified from source: the OpenAI Agents SDK sets `DEFAULT_MAX_TURNS = 10`; LangGraph sets `DEFAULT_RECURSION_LIMIT = int(getenv("LANGGRAPH_DEFAULT_RECURSION_LIMIT", "10007"))` — environment-overridable without a code change or a review. FL-FG-001 through FL-FG-003 therefore require the value, the units, that it is not disabled, and that it is not environment-overridable.

---

## 2. What this corpus actually reuses

Nothing is redistributed. What was reused is **structure** — schema shapes and threshold vocabularies — and **identifiers**, which are facts.

| Source | Licence (verified) | How it is used here |
| :---- | :---- | :---- |
| EU AI Act (Reg. 2024/1689), Reg. 2026/1744, DSM Directive 2019/790, GDPR | CC BY 4.0 via Commission Decision 2011/833/EU | FL-GV-001, FL-GV-002, the three deferred Article 9/10/15 provisions, FL-TD-001, FL-TD-003, the PI family. |
| GPAI Code of Practice chapters | Commission-hosted, 2011/833/EU | The GPAI documentation posture behind FL-MB-006 and FL-MB-009. |
| California SB 53; SB 942 / AB 853; CPPA ADMT regulations | US public domain | FL-SF-001, FL-SF-002, FL-SF-007, FL-GV-001, FL-GV-004. |
| Seoul Frontier AI Safety Commitments | **UK OGL v3.0** — quotable | FL-SF-001 and FL-SF-004, the only openly licensed statement of the deployment-gate obligation. |
| NIST AI RMF 1.0, AI 600-1 Generative AI Profile, AI 100-2 | US Government, public domain (17 U.S.C. §105) | FL-EV-010, marked **advisory**: AI 600-1 action ids (`GV-1.1-001`) are stable and citable and name *suggested actions*, never mandates. |
| UK AISI safety-case templates (arXiv 2411.08088, 2503.04744) | **CC BY 4.0** | FL-SF-006 — a safety case is not signed by the team that authored it. |
| UK AISI `Inspect` / `inspect_evals` | MIT | Scorer vocabulary behind the EV family. |
| OpenSSF Model Signing spec (OMS) v1.0 + conformance suite | Apache-2.0 | FL-MB-001 through FL-MB-004. Its 86 conformance cases carry `id` / `description` / `spec_refs` / `expect: fail` — the closest existing analogue anywhere to this corpus's own case shape, and a model for it. |
| `sigstore/model-transparency` | Apache-2.0 | The signing predicate and root-digest recomputation behind FL-MB-002. |
| `safetensors` `attacks/` | Apache-2.0 | FL-MB-003. The exploits themselves are **not** vendored — they execute. |
| Data Provenance Initiative Collection | Apache-2.0 | The licence lattice behind FL-TD-002, FL-TD-005, FL-TD-006, FL-IP-003: use-class × attribution × share-alike as three separate factors rather than one "licence ok" boolean. |
| Croissant / Croissant-RAI | Apache-2.0 | FL-TD-008. Its 30 negative validator cases each carry an expected *error string* — expected reasoning, not just a verdict. |
| CycloneDX ML-BOM; SPDX 3.0 AI and Dataset profiles | Apache-2.0; Community-Spec-1.0 (implemented, not republished) | FL-MB-006, FL-MB-009, FL-TD-004. |
| Hugging Face `hub-docs` model-index | Apache-2.0 | FL-MB-005 (`base_model` list for merges) and FL-EV attestation-versus-self-report. |
| Microsoft `prompty` | MIT | FL-MB-007 — a prompt version must be typed, not a freeform metadata string. |
| SL5 Standard for AI Security | CC BY 4.0 prose / Apache-2.0 code | The weight-access control family, as the openly licensed substitute for RAND. |
| MLPerf Inference rules | Apache-2.0 | The published TTFT/TPOT budgets behind FL-IN-001 and FL-IN-002, and its verbatim definition of acceptable nondeterminism. |
| vLLM accuracy CI and batch-invariance tests | Apache-2.0 | FL-EV-003 (`rtol` 0.08), FL-EV-005 (accuracy alone passes even when every draft is rejected), FL-IN-004, FL-IN-007. |
| OpenAI `evals` `fact.yaml` | MIT | The five-valued semantic-parity enum: identical / subset / superset / disagreement / immaterial. Binary parity is too coarse. |
| `promptfoo` assertion vocabulary | MIT | The threshold idiom behind FL-EV-003. Note the hazard it documents: `weight: 0` auto-passes. |
| MT-Bench human judgments | CC BY 4.0 | FL-EV-006's agreement threshold. |
| RewardBench 2 | code Apache-2.0, data ODC-BY | The explicit `Ties` subset informed FL-EV-007's tie disposition. |
| BIG-bench canary mechanism | Apache-2.0 | FL-EV-001 and FL-LS-010. A deterministic contamination test needing no reference model. Mint your own GUID. |
| PyTorch | BSD-3-Clause | FL-IN-005 (`CudaMemoryLeakCheck`) and FL-IN-008 — its governance pattern that every nondeterministic op must be declared, registered and carry a named alert test. |
| MLCommons AILuminate v1.0 DEMO; BBQ; XSTest; Do-Not-Answer; SafetyBench; RealToxicityPrompts | CC BY 4.0 / CC BY 4.0 / CC BY 4.0 / Apache-2.0 / MIT / Apache-2.0 | The BS family's factor vocabulary. BBQ's ambiguous-versus-disambiguated design gives FL-BS-005 its "answered as unknown" disposition, which is a third value between right and wrong. |
| LLMail-Inject | MIT | FL-LS-003 and FL-LS-004. Its 13 boolean `objectives` map one-to-one onto factor facts, and its separation of *defence undetected* from *exfiltration sent* is why those are two provisions here, not one. |
| Tensor Trust (code BSD-2-Clause; **data licence unverified**) | code only | The integrity-versus-confidentiality split behind FL-LS-002. No data used. |
| BackdoorLLM | Apache-2.0 | FL-LS-006 — the only permissively licensed poisoned-fine-tuning corpus found. |
| `garak`, `PyRIT` | Apache-2.0 / MIT | FL-LS-011, FL-AG-004. Both *fetch* rather than bundle their probe data, which is the licence-clean pattern. |
| ScanCode Toolkit | Apache-2.0 code, CC BY 4.0 reference data | FL-IP-002. |
| CWE (MITRE) | Royalty-free, attribution required | The AS family. CWE™ is a trademark of The MITRE Corporation. |
| OSPS Baseline; SLSA build track; in-toto; OSV / GitHub Advisory Database; Gitleaks | Apache-2.0 / dual CSL-1.0+Apache-2.0 / Apache-2.0 / CC BY 4.0 / MIT | The SC family, carried over from the SemiFab survey. |

---

## 3. What was deliberately not used

| Source | Why not |
| :---- | :---- |
| DeepMind FSF, Anthropic RSP, OpenAI Preparedness Framework, Meta FAIF | **All rights reserved.** No licence notice on any of the PDFs; Anthropic's terms reserve expressly. Paraphrased, cited by link. |
| RAND RR-A2849-1 (model weight security) | **Noncommercial use only**, reproduction by permission. Cited by link only; SL5 Standard used instead. |
| `artificialintelligenceact.eu`, `code-of-practice.ai` | Third-party copyright / unofficial with no licence. The Commission-hosted originals were used. |
| AGORA legislative dataset | CC BY-**NC**-4.0. |
| **SORRY-Bench** data | Custom dataset licence: research-only, third-party redistribution prohibited. Its 20-mutation taxonomy is reusable as an idea; its 9,240 prompts are not. |
| BeaverTails, BackdoorBench | CC BY-**NC**-4.0. |
| DecodingTrust, HolisticBias dataset, BOLD, CrowS-Pairs, StereoSet, OWASP LLM Top 10 | CC BY-**SA** — ShareAlike is incompatible with a CC BY 4.0 corpus. Identifiers cited; no text or data. |
| WildJailbreak, WildGuardMix | ODC-BY but gated behind acceptance of a responsible-use agreement. |
| ToxiGen, HackAPrompt, TrustLLM dataset, TrojAI, NIST ARIA | Form-gated, contact-sharing, or licence never declared. |
| AgentHarm | MIT **plus** a safety-purposes-only field-of-use restriction — not a plain permissive licence. |
| Tensor Trust **data**, MASK, AdvPromptSet, Jigsaw, Perspective API terms | No LICENSE file located on either branch, or terms unverified. |
| `lm-contamination`, `detect-pretrain-code-contamination`, JudgeBench, LiveBench data, LangGraph | **Licence not verified.** Schemas and findings used; no data. |
| Chatbot Arena model outputs, AlpacaEval human data, LLM-AggreFact (CC BY-**ND**), `ml-engineering` (CC BY-SA) | NC, ND or SA. |
| **Harmful content, regardless of licence** | HarmBench's chem/bio behaviours (56 of 400), JailbreakBench artifacts (working jailbreak strings), the in-the-wild DAN collections, AdvBench affirmative-target strings, AILuminate's `cse` slice, Anthropic red-team attempts, DecodingTrust's Enron PII. Several of these are permissively licensed. None ships here. A compliance corpus needs the *taxonomy* of an attack, not a working instance of it. |
| `semgrep-rules` | Not open source: use permitted only for internal business purposes, distribution forbidden. (Carried over from the SemiFab survey; the finding is why `policy_rule_source_is_redistributable` exists as a factor there.) |
| SPDX `spdx-examples` `content/` | Documents are CC0; the source code in `content/` is GPL-3.0-or-later. Take the documents. |
| OWASP AIBOM | No licence statement, no schema, no corpus — ten workstreams and a "stay tuned". |
| Datasheets for Datasets | arXiv `nonexclusive-distrib/1.0`, not CC BY, and not machine-readable. |
| IBM AI FactSheets 360 | Licence unverified — the site's TLS certificate had expired. |

---

## 4. Structural gaps this corpus had to work around

1. **SLSA has no ML track.** v1.2 defines Build and Source only. "SLSA for models" does not exist as a specification, and OpenSSF Model Signing defines its own predicate outside the in-toto registry. FL-SC-001 and FL-MB-002 are therefore two provisions rather than one, because the artifact track and the model track are genuinely different objects with different verification stories.
2. **There is no prompt-versioning standard.** Prompty has 180 conformance vectors and a TypeSpec schema, and still leaves version in an untyped metadata dictionary. FL-MB-007 states the obligation the ecosystem has not yet standardised.
3. **No open corpus of (approved MBOM, drifted MBOM) pairs exists**, and none of (golden prompt, expected behaviour) regression suites either. Both had to be synthesised.
4. **No standalone insecure-output-handling corpus exists.** Only taxonomies — garak's `xss` / `packagehallucination` / `latentinjection` probes and promptfoo's SQL/shell/SSRF plugins. FL-LS-001's factor vocabulary is built from those taxonomies with fixtures generated here.
5. **The copyright question is unresolved and this corpus takes no position on it.** Bartz v. Anthropic settled ($1.5bn, final approval July 2026) and so sets no precedent; NYT v. OpenAI has no merits ruling; Thomson Reuters v. ROSS was argued in the Third Circuit in June 2026 and is undecided. Germany splits — OLG Hamburg found the TDM exception applies in *LAION* (December 2025, machine-readable opt-out required) while LG München rejected it in *GEMA* (November 2025, memorisation as reproduction), both under appeal. So the IP family here contains only the procedural provisions — provenance recorded, opt-out honoured, licence conflict resolved before ingestion, attribution surviving to release — which hold whichever way the merits land.

---

## 5. Open items for a maintainer

1. **Re-check the AI Act application dates before relying on the `status` field.** The Digital Omnibus is recent and the Commission has signalled further adjustments. The rulebook records a version; a maintainer should record a retrieval date beside it.
2. **Carry the `status` field back into the VetPOC and SemiFab packs.** SemiFab has two export-control rules that are on the books and not in force — the AI Diffusion Rule (rescinded in policy, still in the CFR under non-enforcement) and the Affiliates Rule (suspended to November 2026) — and they are currently modelled as ordinary provisions with no marker.
3. **The GPAI Code of Practice signature status is a fact worth modelling.** Meta declined to sign. A constitution that treats the Code as binding on all GPAI providers would be wrong for at least one major lab, which makes it a natural W-crossjurisdiction extension.
4. **Judge agreement should be a per-deployment declaration, not a corpus constant.** FL-EV-006 requires the measurement; the corpus cannot supply the number, because it depends on the judge and the task family. An adopter publishing a conformance figure should publish that number beside it.
5. **A shared, openly licensed catalogue of frontier-safety obligations does not exist.** The Seoul Commitments are the only OGL-licensed statement, and they are short. The four lab frameworks are the substance and none is reusable. That gap is worth filling, and it is exactly the kind of thing a consortium could publish under CC BY without any lab giving up anything it currently protects.
