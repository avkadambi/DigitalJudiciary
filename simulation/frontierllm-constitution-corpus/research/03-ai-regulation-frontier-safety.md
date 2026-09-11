# 03 — AI Regulation, Frontier Safety, Privacy and IP: Source Survey and Provision Recommendations

**Lane:** AI regulation, frontier safety frameworks, privacy, IP/copyright.
**Purpose:** identify regulatory source material reusable in an open compliance test corpus expressing regulation as constitutional "provisions" for software change at a frontier LLM developer.
**Research date:** 2026-09-05. All statuses stated as of this date.
**Verification convention:** every licence and legal status below is marked **VERIFIED** (checked against the primary source or its publisher's own notice the time of this survey) or **UNVERIFIED** (could not be confirmed — do not rely on it). Nothing here is guessed.

**Applied baselines (given, not re-derived):**
- EU legal texts (EUR-Lex, Commission publications): reusable under **Commission Decision 2011/833/EU** (attribution, no distortion).
- US CFR/USC and NIST publications: **public domain, 17 U.S.C. §105**.
- `usnistgov/oscal-content`: **CC0**. ComplianceAsCode: **BSD-3-Clause**.

---

## PART A — EU AI ACT (Regulation (EU) 2024/1689)

### A.0 Critical status change: the Digital Omnibus on AI — **VERIFIED**

**Regulation (EU) 2026/1744** of the European Parliament and of the Council of **8 July 2026**, *amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)*.
- URL (ELI): https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
- HTML: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202601744 · PDF: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202601744
- **Entry into force: 27 July 2026.** Parliament approved 16 June 2026; Council adopted 29 June 2026; signed 8 July 2026.
- **Licence: VERIFIED reusable** under 2011/833/EU (EUR-Lex).
- Format: HTML + PDF + XML (Formex). EUR-Lex XML is the machine-readable form usable for automated provision extraction.

**Effect on application dates — this is the single most important fact for a corpus dated late 2026.** Any corpus that assumes Annex III high-risk obligations bind in 2026 is wrong.

| Obligation block | Applies from | Status at 2026-09-05 |
|---|---|---|
| Art. 5 prohibited practices; Art. 4 AI literacy | 2 Feb 2025 | **IN FORCE** |
| Governance (Ch. VII); Arts. 51–56 GPAI; penalties for GPAI | 2 Aug 2025 | **IN FORCE** |
| Art. 50 transparency (chatbot disclosure, synthetic-content marking) | 2 Aug 2026 | **IN FORCE**; four-month grace to **2 Dec 2026** for watermarking of systems placed on the market before 2 Aug 2026 |
| GPAI enforcement powers (Commission fines) | 2 Aug 2026 | **IN FORCE** |
| New Art. 5 prohibition: AI generating non-consensual intimate imagery / CSAM | added by 2026/1744; transitional period to **2 Dec 2026** | **NOT YET BINDING** |
| Annex III high-risk (Arts. 8–15, 16–27) | **2 Dec 2027** (was 2 Aug 2026) | **DEFERRED — not in force** |
| Annex I product-embedded high-risk | **2 Aug 2028** (was 2 Aug 2027) | **DEFERRED — not in force** |

Sources: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng ; Gibson Dunn (pre-adoption analysis) https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

**Corpus implication:** Articles 9–15 are *deferred law*, not *current law*. In a constitution they are legitimate **Tier 2** provisions (binding design targets with a known commencement date) but cannot be asserted as currently-enforceable ABSOLUTE floors. Article 5 and Articles 50–56 **can**.

### A.1 Article 5 — Prohibited practices — **VERIFIED IN FORCE since 2 Feb 2025**
- URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (authoritative); readable per-article mirror https://artificialintelligenceact.eu/article/5/
- Contents (Art. 5(1)(a)–(h)): (a) subliminal / purposefully manipulative or deceptive techniques materially distorting behaviour causing significant harm; (b) exploitation of vulnerabilities by age, disability, or specific social/economic situation; (c) social scoring producing detrimental treatment in unrelated contexts or disproportionate consequences; (d) predictive policing based *solely* on profiling or personality traits; (e) untargeted scraping of facial images from the internet or CCTV to create/expand facial recognition databases; (f) emotion inference in workplace and education (medical/safety carve-out); (g) biometric categorisation to deduce race, political opinions, trade union membership, religious/philosophical beliefs, sex life or sexual orientation; (h) real-time remote biometric identification in publicly accessible spaces for law enforcement, save three narrow exceptions. Plus the new NCII/CSAM prohibition inserted by 2026/1744.
- Format: HTML/PDF/XML.
- **Licence: VERIFIED — 2011/833/EU.**
- **Reuse: PROVISION TEXT, verbatim.** Art. 5(1)(e) is directly operative against a frontier developer's data pipeline (face scraping); (a), (f), (g) are directly operative against product features. This is the strongest candidate set for non-derogable provisions because the AI Act attaches the highest penalty tier (up to EUR 35m / 7% global turnover) and admits no proportionality defence.

### A.2 Articles 9–15 — High-risk requirements — **VERIFIED text; DEFERRED to 2 Dec 2027**
- Art. 9 risk management system (continuous, iterative, across lifecycle); Art. 10 data and data governance (training/validation/test sets relevant, sufficiently representative, to the best extent possible free of errors and complete; examination for biases; Art. 10(5) permits processing special-category data for bias detection under safeguards); Art. 11 + Annex IV technical documentation; Art. 12 automatic logging over the system's lifetime; Art. 13 transparency and provision of information to deployers; **Art. 14 human oversight**; **Art. 15 accuracy, robustness and cybersecurity**.
- **Art. 14 verbatim hooks (VERIFIED):** 14(1) systems shall be designed so they "can be effectively overseen by natural persons during the period in which they are in use"; 14(4)(b) oversight persons must be able "to remain aware of the possible tendency of automatically relying or over-relying" on output (automation bias); **14(4)(d) "to decide … not to use the … system or to otherwise disregard, override or reverse the output"**; 14(4)(e) "to intervene in the operation … or interrupt the system through a 'stop' button"; **14(5) two-person verification** for Annex III 1(a) remote biometric identification.
- **Art. 15 verbatim hooks (VERIFIED):** 15(3) accuracy levels and metrics declared in instructions for use; 15(4) resilience via redundancy/backup/fail-safe, and mitigation of feedback loops in continuously-learning systems; **15(5) resilience to data poisoning, model poisoning, adversarial examples / model evasion, and confidentiality attacks**.
- **Licence: VERIFIED — 2011/833/EU.**
- **Reuse: PROVISION TEXT (Art. 14(4)(d)–(e) and 15(5) are close to directly executable as change-control assertions) + FACTOR VOCABULARY** (Art. 9's "risk management" verbs, Art. 10's data-quality predicates).

### A.3 Article 50 — Transparency — **VERIFIED IN FORCE since 2 Aug 2026**
- 50(1) disclosure that a person is interacting with an AI system; 50(2) providers of systems generating synthetic audio/image/video/text must mark outputs in a machine-readable format detectable as artificially generated or manipulated; 50(3) emotion recognition / biometric categorisation disclosure; 50(4) deepfake and public-interest-text disclosure.
- Companion: **Code of Practice on Transparency of AI-generated Content** — https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content (Commission-hosted; **licence VERIFIED reusable under 2011/833/EU**).
- **Reuse: PROVISION TEXT + ORACLE.** 50(2) is machine-checkable — a build that ships a generative endpoint without provenance marking fails.

### A.4 Articles 51–56 — GPAI models — **VERIFIED IN FORCE since 2 Aug 2025**
- **Art. 51 (VERIFIED quote):** a GPAI model has systemic risk if (a) it has high-impact capabilities on appropriate technical tools and methodologies, or (b) by Commission decision. **51(2): presumption of high-impact capabilities "when the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25."** 51(3) delegated acts may amend the threshold.
- **Art. 53 (VERIFIED):** (a) technical documentation per **Annex XI**; (b) information for downstream providers per **Annex XII**; (c) **a policy to comply with Union copyright law, including identifying and respecting Art. 4(3) DSM rights reservations**; (d) **a public sufficiently detailed summary of training content** on the AI Office template. 53(2) exempts free/open-source models from (a)–(b) unless systemic risk.
- **Annex XI (VERIFIED contents):** §1 general description (tasks, acceptable use policy, release date, distribution, architecture, parameter count, modality, licence terms), design specifications and training methodology with rationale, **data provenance/curation/scope/characteristics and bias-detection method**, compute and training time, known/estimated energy consumption. §2 (systemic risk only): evaluation strategy incl. protocols and criteria, **adversarial testing / red-teaming and alignment/fine-tuning measures**, system architecture.
- **Art. 55 (VERIFIED):** systemic-risk providers must (a) perform model evaluation to state-of-the-art protocols **including adversarial testing to identify and mitigate systemic risk**; (b) assess and mitigate possible Union-level systemic risks; (c) **track, document and report serious incidents and corrective measures to the AI Office without undue delay**; (d) **ensure an adequate level of cybersecurity protection for the model and its physical infrastructure**. 55(2) codes of practice give presumption of conformity pending harmonised standards.
- **Art. 56:** the Commission/AI Office facilitates codes of practice.
- **Licence: VERIFIED — 2011/833/EU.**
- **Reuse: PROVISION TEXT (Art. 51(2), 53(1)(c)–(d), 55(1)(a)–(d) are the backbone of a frontier constitution) + ORACLE (10^25 FLOP is a numerically evaluable trigger).**

### A.5 GPAI Code of Practice — **status and licence: partly VERIFIED**
- Official page: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai (chapters as PDF + a DOCX Model Documentation Form).
- **Published 10 July 2025.** Three independently drafted chapters: **Transparency**, **Copyright**, **Safety and Security**.
- **Legal status (VERIFIED): voluntary.** The Commission and the AI Board confirmed it is an *adequate* voluntary tool to demonstrate compliance with Arts. 53 and 55. Signature yields a presumption-of-conformity route and reduced administrative burden under Art. 55(2); non-signatories must demonstrate compliance by other adequate means. **It is not itself binding law.** 26 signatories including Amazon, Anthropic, Google, IBM, Microsoft, Mistral, OpenAI; **Meta declined to sign**.
- **Safety & Security chapter — 10 Commitments (VERIFIED via https://code-of-practice.ai/):** 1 Safety and Security Framework; 2 systemic-risk identification; 3 systemic-risk analysis (Measure 3.2 state-of-the-art model evaluations incl. open-ended testing and red-teaming; 3.4 risk estimation); 4 risk acceptance determination; 5 safety mitigations; **6 security mitigations (Measure 6.2 + Appendix 4: protect unreleased model weights against unauthorised release, access and theft, until parameters are public or deleted)**; 7 Safety and Security Model Reports before market placement; 8 responsibility allocation (8.3 healthy risk culture, without prejudice to Directive (EU) 2019/1937 whistleblower protection); 9 serious incident reporting without undue delay; 10 additional documentation and public summaries.
- **Licence: the Commission-hosted chapter PDFs are VERIFIED reusable under 2011/833/EU** (Commission publication). The **unofficial** mirrors are not: `code-of-practice.ai` states no licence and self-describes as unofficial; `artificialintelligenceact.eu` carries "© Future of Life Institute" with no reuse grant — **UNVERIFIED, do not ingest either as corpus text**. Cite EUR-Lex / digital-strategy.ec.europa.eu only.
- **Reuse: PROVISION TEXT (from the Commission PDFs) + FACTOR VOCABULARY.** Commitment 6 is the cleanest existing regulatory articulation of **model-weight security** anywhere in binding-adjacent EU material.

### A.6 Training-content summary template — **VERIFIED**
- Commission template adopted July 2025 for Art. 53(1)(d) public summaries. Announcement/analysis: https://www.mayerbrown.com/en/insights/publications/2025/08/eu-ai-act-news-rules-on-general-purpose-ai-start-applying-guidelines-and-template-for-summary-of-training-data-finalized
- Official template is a Commission document — **licence VERIFIED 2011/833/EU**.
- **Reuse: ORACLE.** The template's fields (data sources, scraped domains, licensed data, opt-out handling) are a ready-made schema for a "training data provenance record" artefact a corpus can require a change to produce.

---

## PART B — NIST

### B.1 NIST AI RMF 1.0 — **VERIFIED public domain**
- URL: https://www.nist.gov/itl/ai-risk-management-framework ; PDF https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf ; DOI 10.6028/NIST.AI.100-1. Published 26 Jan 2023.
- Contents: four functions — **GOVERN, MAP, MEASURE, MANAGE** — with categories and subcategories (e.g. GV-1.1, MS-2.7), plus seven trustworthiness characteristics.
- **Status change (VERIFIED):** NIST's own page states "The AI RMF 1.0 is being revised as part of the White House AI Action Plan." A revision is in progress; the 1.0 text remains published. A **Critical Infrastructure Profile** concept note was released 7 Apr 2026.
- Companions: **AI RMF Playbook**, **Roadmap**, **Crosswalks** (to ISO/IEC 42001, EU AI Act, etc.) at https://airc.nist.gov/. Crosswalks are the most directly reusable artefact for a mapping corpus. **No OSCAL/JSON serialisation of the AI RMF was found — UNVERIFIED whether one exists.**
- **Licence: VERIFIED public domain (17 U.S.C. §105).**
- **Reuse: FACTOR VOCABULARY + PROVISION IDENTIFIERS.** Subcategory IDs are stable citable anchors.

### B.2 NIST AI 600-1 — Generative AI Profile — **VERIFIED public domain**
- URL: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; DOI 10.6028/NIST.AI.600-1. Published **July 2024**.
- **12 GAI risk categories (VERIFIED):** CBRN Information or Capabilities; Confabulation; Dangerous, Violent, or Hateful Content; Data Privacy; Environmental Impacts; Harmful Bias or Homogenization; Human-AI Configuration; Information Integrity; Information Security; Intellectual Property; Obscene, Degrading and/or Abusive Content; Value Chain and Component Integration.
- **Action ID format (VERIFIED):** `<FUNCTION>-<Category>.<Subcategory>-<NNN>`, e.g. **GV-1.1-001**, MP-2.3-002, MS-2.7-004, MG-4.1-003, where GV=Govern, MP=Map, MS=Measure, MG=Manage. Each row carries **Suggested Action**, **GAI Risks** tags, and **AI Actor Tasks**.
- **Can the action IDs be cited as identifiers? YES — VERIFIED.** They are stable, unique within the document, and the document is public domain; NIST itself and third-party crosswalks (e.g. https://airc.nist.gov/documents/1/20250527-Crosswalk_NIST_600-1_IMDA_AI_Verify.pdf) use them as citation anchors. The only caveat is that they identify *suggested actions*, not requirements — a corpus must not present `GV-1.1-001` as a mandate.
- **Reuse: FACTOR VOCABULARY + PROVISION IDENTIFIERS.** This is the best public-domain, granularly-identified action vocabulary available for generative-AI controls, and the natural spine for mapping corpus provisions to a neutral ID scheme.
- **Caution:** the AI Action Plan directs revision of NIST AI frameworks; some risk framings (misinformation, DEI, climate) are politically contested and a revision may drop or reword them. **Whether AI 600-1 specifically will be withdrawn or amended is UNVERIFIED.** Pin the July-2024 version by DOI.

### B.3 NIST AI 100-2 E2025 — Adversarial ML taxonomy — **VERIFIED public domain**
- URL: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf ; announcement https://csrc.nist.gov/news/2025/nist-ai-100-2-adversarial-machine-learning-taxonom (March 2025 final).
- Contents: taxonomy and terminology of attacks and mitigations across predictive and generative AI — availability, integrity, privacy attacks; evasion, poisoning, model extraction, membership inference; and for GenAI: **direct and indirect prompt injection, supply-chain poisoning, RAG-corpus poisoning, agent/tool abuse**.
- **Licence: VERIFIED public domain (17 U.S.C. §105).**
- **Reuse: FACTOR VOCABULARY (attack-class terms with stable definitions) + ORACLE (the attack taxonomy is the natural checklist against which an Art. 15(5) / RSP security assertion is tested).**

---

## PART C — FRONTIER SAFETY FRAMEWORKS (corporate publications, **not law**)

**Blanket licence finding — VERIFIED and material.** None of the five documents below carries a licence grant or copyright notice permitting redistribution. Anthropic's Terms of Service, checked when this survey was compiled, state: *"We and our Providers retain all of our respective rights, title, and interest, including intellectual property rights, in and to the Services. Other than the rights of access and use expressly granted in our Terms, our Terms do not grant you any right, title, or interest in or to our Services"* (https://www.anthropic.com/legal/terms). The DeepMind FSF PDF, the OpenAI Preparedness Framework PDF and Meta's framework carry **no licence notice at all** — which under Berne means **all rights reserved by default**.

> **Rule for the corpus: these documents may be PARAPHRASED and CITED, and short passages quoted under fair use / the Art. 5(3)(d) InfoSoc quotation exception, but their text MUST NOT be ingested verbatim as provision text or redistributed as corpus content.** Encode them as *derived factor vocabulary* — capability-threshold names, mitigation classes, review-gate names — with a citation to the source, never as copied clauses.

### C.1 Google DeepMind — Frontier Safety Framework **v3.1, 17 April 2026** — **VERIFIED**
- URL: https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf (v3.0 at `frontier-safety-framework_3.pdf`); blog https://deepmind.google/blog/strengthening-our-frontier-safety-framework/ ; per-model reports e.g. https://deepmind.google/models/fsf-reports/gemini-3-pro/
- **Critical Capability Levels (CCLs) and required security levels (VERIFIED):**
  - *CBRN uplift level 1* — uplift to moderately-resourced actors producing severe-scale harm → **Security Level 2+** (insider-threat and well-resourced-non-state-actor resistance).
  - *Cyber uplift level 1* — sufficient uplift for high-impact cyber attacks → **Security Level 2+**.
  - *Harmful manipulation level 1* (exploratory) — systematic alteration of beliefs/behaviours in high-stakes contexts → **Security Level 2+**.
  - *ML R&D acceleration level 1* — demonstrable acceleration of AI development beyond historical rates → **Security Level 3**.
  - *ML R&D automation level 1* — full automation of a capability-improvement research team → **Security Level 4** (explicitly flagged as requiring industry-wide adoption).
  - **Tracked Capability Levels (TCLs):** a lower CBRN TCL, and a *Stealth and Situational Awareness* TCL where instrumental reasoning defeats assured human control absent added mitigations.
- **Process (VERIFIED):** three-step — safeguard development and assessment (safety post-training, monitoring, account moderation, jailbreak detection, user verification, bug bounties; robustness tested by automated evals and red-teaming) → **pre-deployment review by a governance function determining residual-risk acceptability, with deployment only when evidence shows harm likelihood is acceptable** → post-deployment monitoring and safety-case update, material updates requiring governance review.
- **Safety case definition (VERIFIED quote-worthy but short):** "an assessable argument showing how severe risks associated with a model's CCLs have been reduced to an acceptable level."
- **Licence: VERIFIED — no notice; all rights reserved. Paraphrase only.**
- **Reuse: FACTOR VOCABULARY (CCL/TCL names, security-level tiers) + ORACLE (the pre-deployment-review gate maps to a change-control assertion).**

### C.2 Anthropic — Responsible Scaling Policy **v3.4, effective 8 July 2026** — **VERIFIED**
- URLs: https://www.anthropic.com/responsible-scaling-policy ; version history https://www.anthropic.com/rsp-updates
- **Verified version history:** 1.0 (19 Sep 2023) → 2.0 (15 Oct 2024) → 2.1 (31 Mar 2025, added a CBRN threshold, split AI R&D into two thresholds) → 2.2 (14 May 2025, sophisticated insiders excluded from ASL-3 scope) → **3.0 (24 Feb 2026, comprehensive rewrite introducing Frontier Safety Roadmaps and quantified Risk Reports)** → 3.1 (2 Apr 2026) → 3.2 (29 Apr 2026, LTBT external review authority) → 3.3 (26 May 2026, updated CBW threshold) → **3.4 (8 Jul 2026, refined automated-R&D threshold; Risk Report sharing to 200+ employees; coverage-date reports; redaction indicators in public reports; multiple external reviewers)**.
- **Capability thresholds (VERIFIED as named):** CBRN-3, CBRN-4; AI R&D-4, AI R&D-5; cyber. **Standards:** ASL-2 baseline; **ASL-3 Deployment Standard** (prompt/completion classifiers, asynchronous monitoring, jailbreak bounty and rapid remediation) and **ASL-3 Security Standard** (weight-access control, software supply-chain security, endpoint patching, red-teaming, deception technology); ASL-4 for higher thresholds.
- **Licence: VERIFIED all rights reserved** (Terms of Service quoted above). **Paraphrase only.**
- **Reuse: FACTOR VOCABULARY + ORACLE.** The RSP's structure — *capability threshold → required standard → if the standard cannot be met, do not deploy / pause scaling* — is the cleanest available template for a Tier 1 deployment-gate provision.

### C.3 OpenAI — Preparedness Framework **v2, 15 April 2025** — **VERIFIED**
- URL: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf ; announcement https://openai.com/index/updating-our-preparedness-framework/
- **Tracked Categories (VERIFIED):** Biological and Chemical; Cybersecurity; AI Self-improvement. **Research Categories:** Long-range Autonomy; Sandbagging; Autonomous Replication and Adaptation; Undermining Safeguards; Nuclear and Radiological.
- **Thresholds (VERIFIED quotes):** *High* = capabilities that "significantly increase existing risk vectors for severe harm"; *Critical* = capabilities presenting "a meaningful risk of a qualitatively new threat vector for severe harm with no ready precedent."
- **Safeguards (VERIFIED):** against malicious users — robustness, usage monitoring, trust-based access; against misaligned models — lack of autonomous capability, value alignment, instruction alignment, reliable system oversight, system architecture constraints; plus security controls (threat modelling, defence in depth, access management, secure development, operational security, auditing).
- **Governance (VERIFIED):** a **Capabilities Report** and a **Safeguards Report**, both reviewed by the **Safety Advisory Group**, which recommends a deployment decision to OpenAI Leadership.
- **Licence: VERIFIED — no notice in the document; all rights reserved. Paraphrase only.**
- **Reuse: FACTOR VOCABULARY + ORACLE (two-report + independent-review gate).**

### C.4 Meta — Frontier AI Framework **v1.1** — **VERIFIED existence, partly**
- URLs: https://about.fb.com/news/2025/02/meta-approach-frontier-ai/ ; catalogued at https://agora.eto.tech/instrument/1970
- Contents: an outcomes-led approach defining *critical* and *high* risk outcomes across cyber and CBRN threat scenarios; where risk is *critical*, development is halted and the model is not released; where *high*, release is restricted pending mitigation. **Precise threshold wording UNVERIFIED at the time of this survey** (primary PDF not fetched).
- **Licence: UNVERIFIED — no licence grant located; assume all rights reserved. Paraphrase only.**
- Note: **Meta is not a signatory to the GPAI Code of Practice** (VERIFIED), which is itself a useful corpus fact: signature is not universal, so a constitution cannot treat CoP adherence as an industry given.

### C.5 Frontier AI Safety Commitments (Seoul, 21–22 May 2024) — **VERIFIED, and the ONE openly licensed lab-facing commitment text**
- URL: https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024
- Contents: three outcomes — (I) effectively identify, assess and manage risks, including publishing a safety framework with thresholds at which severe risks would be deemed intolerable; (II) be accountable for safely developing and deploying frontier models, including **not developing or deploying a model at all if mitigations cannot keep risks below the thresholds**; (III) provide appropriate transparency to external actors including governments. Sixteen (later twenty) organisations signed.
- **Licence: VERIFIED — Open Government Licence v3.0** ("All content is available under the Open Government Licence v3.0"). **This text CAN be ingested verbatim** with the OGL attribution statement.
- **Reuse: PROVISION TEXT.** Because it is OGL-licensed and expresses the same "intolerable threshold → do not deploy" norm that the proprietary lab frameworks state, **it is the correct vehicle for putting the capability-threshold-gate norm into the corpus as quotable text**, with the lab frameworks cited as corroborating practice rather than copied.
- Related: METR's cross-lab comparison https://metr.org/common-elements identifies nine common elements across twelve developers' policies — capability thresholds; **model weight security**; deployment mitigations; conditions for halting deployment; conditions for halting development; full capability elicitation; evaluation timing and frequency; accountability; policy updates. **Licence UNVERIFIED — cite, do not copy.** These nine element names are an excellent neutral factor vocabulary and are, as short factual labels, safe to reuse as terminology.

---

## PART D — UK AI SECURITY INSTITUTE (AISI)

### D.1 `Inspect` — **VERIFIED MIT**
- URL: https://github.com/UKGovernmentBEIS/inspect_ai ; docs https://inspect.aisi.org.uk/
- Contents: a Python framework for LLM evaluations — prompt engineering, tool use, multi-turn dialogue, model-graded evals, solvers/scorers/datasets abstractions, extensible via third-party packages.
- Format: Python package (PyPI `inspect-ai`), source on GitHub, eval logs as structured JSON.
- **Licence: VERIFIED MIT.**
- **Reuse: ORACLE — the strongest one in this lane.** A compliance corpus that needs to assert "a required evaluation was actually run before deployment" can express that as an Inspect eval log artefact. MIT permits unrestricted embedding.

### D.2 `inspect_evals` — **VERIFIED MIT**
- URL: https://github.com/UKGovernmentBEIS/inspect_evals (UK AISI with Arcadia Impact and the Vector Institute).
- Contents: 100+ community-contributed evaluations. Safety-relevant: **cyber** — Cybench (39 CTF challenges), CVE-Bench, CyberGym (1,507 vulnerability-analysis instances), CyberSecEval 1–4 (MITRE ATT&CK mapping, malware analysis, prompt injection), CTI-REALM; **agentic safety** — AgentDojo (prompt injection on agents), AgentHarm, AgentThreatBench (OWASP agentic threats), b3 Backbone Breaker Benchmark, MCPTox (tool poisoning); **safeguards** — jailbreak susceptibility, bias, honesty, moral reasoning. **No dedicated CBRN proxy benchmarks were found (VERIFIED absent from the visible listing)** — expected, since CBRN evals are typically withheld.
- **Licence: VERIFIED MIT.**
- **Reuse: ORACLE.** Directly usable as the evidence layer behind an "evaluations completed" provision, and as the concrete referent for evaluation-set contamination controls.

### D.3 AISI safety-case templates — **VERIFIED CC BY 4.0 (the papers)**
- *Safety case template for frontier AI: A cyber inability argument* — https://arxiv.org/abs/2411.08088 — Goemans, Buhl, Schuett, Korbak, Wang, Hilton, Irving. Uses **Claims-Arguments-Evidence (CAE)** to decompose an inability claim into risk models, proxy tasks and evaluation protocols. **arXiv licence: VERIFIED CC BY 4.0.**
- *Safety Cases: A Scalable Approach to Frontier AI Safety* — https://arxiv.org/pdf/2503.04744.
- AISI blog: https://www.aisi.gov.uk/blog/safety-cases-at-aisi
- **Licence caution:** gov.uk-published AISI content is **VERIFIED OGL v3.0**; content on the separate `aisi.gov.uk` domain shows **no copyright or licence statement at all — UNVERIFIED**. Prefer the arXiv CC BY 4.0 versions for anything ingested.
- **Reuse: PROVISION TEXT (CC BY, with attribution) + the CAE structure as the schema for a "completed safety case" artefact.** This is the only open, structured safety-case template found in this lane and is the natural formal object behind a Tier 1 deployment gate.

---

## PART E — UNITED STATES

### E.1 EO 14110 — **VERIFIED RESCINDED**
- EO 14110 ("Safe, Secure, and Trustworthy Development and Use of AI", 30 Oct 2023) was **rescinded in January 2025** by **EO 14179, "Removing Barriers to American Leadership in Artificial Intelligence."** Reference: https://oecd.ai/en/dashboards/policy-initiatives/executive-order-14179-removing-barriers-to-american-leadership-in-ai
- **Corpus implication: EO 14110's 10^26 FLOP reporting trigger is NOT current US law.** Any provision citing it must be marked historical. The surviving 10^26 threshold in US law is **California SB 53's**, not the federal EO's.

### E.2 OMB memoranda — **VERIFIED**
- **M-25-21** (April 2025) supersedes **M-24-10** — federal agency use of AI; retains Chief AI Officer structure, agency AI use-case inventories, and a risk-management regime for high-impact AI.
- **M-25-22** (April 2025) supersedes **M-24-18** — federal AI acquisition; documentation and risk evaluation in procurement.
- **Licence: VERIFIED public domain** (US Government works).
- **Reuse: PROVISION TEXT (for any federal-facing deployment) + FACTOR VOCABULARY ("high-impact AI", "minimum risk management practices").** Note these bind *agencies*, not private developers — in a frontier-lab constitution they are Tier 3 unless the lab sells to the federal government, in which case they become contractually Tier 2.

### E.3 America's AI Action Plan — **VERIFIED**
- URL: https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf (July 2025), with three accompanying EOs (infrastructure, exports, federal procurement).
- **Licence: VERIFIED public domain.**
- Relevant directives: revise the NIST AI RMF; build evaluation ecosystems; biosecurity screening for nucleic-acid synthesis; federal procurement neutrality requirements.
- **Reuse: FACTOR VOCABULARY only.** It is policy, not obligation.

### E.4 EO 14365 — federal preemption of state AI law — **VERIFIED, and destabilising**
- **Executive Order 14365, "Ensuring a National Policy Framework for Artificial Intelligence," 11 December 2025** — https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/
- Directives (VERIFIED): AG to stand up an **AI Litigation Task Force** within 30 days to challenge state AI laws; Commerce to identify "onerous" state laws within 90 days, singling out laws that require models to "alter their truthful outputs"; **BEAD funding conditioned** on states not maintaining conflicting AI laws; FCC to open a proceeding on a preemptive federal AI reporting standard; FTC policy guidance on deception as applied to AI; a legislative proposal with carve-outs for child safety, compute infrastructure and state procurement. Follow-on White House legislative recommendations issued **25 March 2026**.
- **Corpus implication: state-law provisions must be marked as under active preemption challenge.** They are defeasible in a way EU provisions are not.

### E.5 California **SB 53 — Transparency in Frontier Artificial Intelligence Act (TFAIA)** — **VERIFIED IN FORCE**
- Signed **29 September 2025**; **effective 1 January 2026**. Bill text: https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53 ; analyses: https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/ and https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251001-transparency-in-frontier-artificial-intelligence-act-sb-53-california-requires-new-standardized-ai-safety-disclosures
- **Definitions (VERIFIED):** *frontier model* = a foundation model trained using **more than 10^26 integer or floating-point operations**, counting cumulative compute including fine-tuning and modification; *frontier developer* = one who trained or initiated training of such a model; ***large frontier developer*** = a frontier developer with **annual gross revenue exceeding $500,000,000** (with affiliates) in the preceding calendar year.
- **Obligations (VERIFIED):**
  1. **Frontier AI Framework** — large frontier developers must publish and annually review a framework covering: incorporation of national/international standards and industry-consensus best practices; how catastrophic-risk capability is assessed; mitigations and how their effectiveness is measured; governance structures; and **cybersecurity practices to secure unreleased model weights**.
  2. **Transparency report** — published at or before deployment: release date, modalities, intended uses, restrictions, and a summary of catastrophic-risk assessments including any third-party evaluator involvement.
  3. **Critical safety incident reporting** to the **California Office of Emergency Services within 15 days**, or **within 24 hours** where there is imminent risk of death or serious injury. Reportable incidents include unauthorised access/tampering causing serious harm, materialised catastrophic risk, **loss of control resulting in injury or property damage, and a model deceptively evading developer safeguards**.
  4. **Whistleblower protections** — anti-retaliation, mandatory notice of rights, and an anonymous internal reporting channel at large frontier developers.
  5. **Penalties** up to **$1,000,000 per violation**, AG enforcement; **CDT** must annually recommend updates to the definitions.
  - **Codification into specific Health & Safety Code sections: UNVERIFIED** (leginfo blocks automated fetch; secondary sources did not state the section numbers).
- **Licence: VERIFIED public domain** — California statutes are not subject to copyright as government edicts; leginfo text is freely reproducible.
- **Reuse: PROVISION TEXT — the single best-fitting statute for this corpus.** SB 53 is the only *binding law anywhere* that directly regulates frontier-model developers on safety frameworks, weight security, and incident reporting. Its 10^26 threshold, 15-day reporting clock, and weight-security duty are all machine-checkable.

### E.6 California SB 942 (AI Transparency Act), as amended by AB 853 — **VERIFIED IN FORCE since 2 August 2026**
- https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853 ; analysis https://www.morganlewis.com/pubs/2026/08/new-california-ai-disclosure-rules-become-operative
- **Operative 2 August 2026** (delayed from 1 Jan 2026). Covered provider = a publicly-accessible GenAI system with **more than 1,000,000 monthly visitors or users** in California. Requires **latent disclosures** (durable, detection-tool-compatible metadata identifying system, version and creation date in all AI-generated content), optional **manifest disclosures**, and a **free public AI-detection tool** that must not retain personal information beyond feedback needs. Penalty **$5,000 per violation per day**; AG enforcement, no private right of action. Phase-in: **large online platforms 1 Jan 2027**, **capture-device manufacturers 1 Jan 2028**.
- **Reuse: PROVISION TEXT + ORACLE** (provenance metadata presence is directly testable).

### E.7 Colorado — **VERIFIED: SB 24-205 replaced**
- SB 24-205 (Colorado AI Act) enforcement was postponed from 1 Feb 2026 to 30 June 2026, then **replaced by SB 26-189, signed 14 May 2026, effective 1 January 2027**, reframed around **automated decision-making technology (ADMT)** in consequential decisions: developer disclosure to deployers (intended uses, known risks and limitations, categories of training data), advance notice before ADMT use in employment decisions, **a plain-language explanation of an adverse decision and the ADMT's role within 30 days**, three-year record retention, and **meaningful human review of contested decisions**. Source: https://www.seyfarth.com/news-insights/colorado-enacts-artificial-intelligence-replacement-law.html
- **Whether SB 24-205 is formally repealed vs superseded: UNVERIFIED.**
- **Reuse: FACTOR VOCABULARY.** The "meaningful human review" and "explanation within 30 days" duties are useful for the human-oversight provision family.

### E.8 Texas TRAIGA (HB 149) and Illinois — **partly UNVERIFIED**
- Texas Responsible AI Governance Act (HB 149): widely reported effective **1 January 2026**, intent-based prohibitions (behavioural manipulation, unlawful discrimination with an intent requirement, social scoring, biometric identification from scraped data), a regulatory sandbox and an AG-enforced cure period. **Effective date and text not fetched when this survey was compiled — UNVERIFIED.**
- Illinois: HB 3773 amends the Human Rights Act on AI in employment decisions (effective 1 Jan 2026); a separate AI-therapy restriction (WOPR Act) was enacted in 2025. **UNVERIFIED at the time of this survey.**
- Both are on the EO 14365 preemption target list. Treat as Tier 3 pending verification.

---

## PART F — PRIVACY

### F.1 GDPR (Regulation (EU) 2016/679) as applied to training data — **VERIFIED reusable**
- URL: https://eur-lex.europa.eu/eli/reg/2016/679/oj ; **licence VERIFIED 2011/833/EU**; XML available.
- **Art. 5** principles — lawfulness/fairness/transparency, purpose limitation, **data minimisation**, accuracy, storage limitation, integrity and confidentiality, and **5(2) accountability**. Data minimisation and purpose limitation are the two that bite hardest on indiscriminate web-scale training corpora.
- **Art. 6** lawful bases — in practice **6(1)(f) legitimate interests** is the only viable basis for scraped training data; consent is impracticable at web scale.
- **Art. 9** special categories — scraped corpora inevitably contain health, sexual-orientation, religious, biometric and political data; **Art. 9(2)(e) "manifestly made public by the data subject"** is narrow and does not cover everything merely findable online.
- **Art. 17** erasure — the hardest to satisfy against model weights, since retraining is the only reliable remedy; the EDPB's anonymity route (below) is the practical alternative.
- **Art. 22** automated individual decision-making — right not to be subject to solely-automated decisions with legal or similarly significant effects; **22(3) safeguards include the right to obtain human intervention, to express a point of view and to contest the decision**. This is the EU-law twin of AI Act Art. 14.
- **Art. 35** DPIA — mandatory for systematic and extensive evaluation based on automated processing, large-scale special-category processing, and large-scale systematic monitoring; **35(7)(d) requires the measures to address the risks**.
- **Reuse: PROVISION TEXT, verbatim.**

### F.2 EDPB Opinion 28/2024 — **VERIFIED content; licence UNVERIFIED**
- URL: https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf (adopted 17 December 2024).
- **Four questions and holdings (VERIFIED):**
  1. **Anonymity is not automatic.** AI models trained on personal data "cannot, in all cases, be considered anonymous"; anonymity requires a case-by-case demonstration that both (i) the likelihood of *extracting* personal data from the model and (ii) the likelihood of *obtaining* it via queries are **insignificant**, assessed against all means reasonably likely to be used. The EDPB lists assessable factors: model design and source selection, testing and resistance to regurgitation/membership-inference/extraction attacks, and documentation.
  2–3. **Legitimate interest** requires a cumulative three-step test — a real, lawful, articulated interest; strict necessity with no less-intrusive alternative and proportionality to data volume; and a balancing test weighing nature of data, context, scale, categories of data subjects, **reasonable expectations**, and consequences. The EDPB stresses that mere transparency compliance does not by itself create reasonable expectations.
  4. **Unlawful development taints deployment**, with three scenarios: same controller retaining personal data (case-by-case); a different deploying controller (must conduct an appropriate assessment of the development phase's lawfulness); and a model genuinely anonymised before deployment (GDPR does not apply to the model's operation, so the earlier unlawfulness does not carry over — but any deployment-phase personal-data processing is assessed independently).
- **Licence: UNVERIFIED.** The EDPB legal-notice page 404'd at the time of this survey. Commission Decision 2011/833/EU formally covers Commission documents; whether it extends to EDPB outputs was not confirmed. **Cite and paraphrase; do not assume verbatim redistribution rights until the EDPB legal notice is checked.**
- **Reuse: FACTOR VOCABULARY + ORACLE.** Holding (4) is the sharpest available rule for the corpus: *training-data provenance defects propagate forward into deployment unless the model is demonstrably anonymous.* That is exactly the kind of rule a change-control constitution needs.

### F.3 CCPA/CPRA and the CPPA ADMT regulations — **VERIFIED**
- Regulations approved by OAL **23 September 2025**, effective **1 January 2026**. https://cppa.ca.gov/regulations/ccpa_updates.html ; analysis https://www.whitecase.com/insight-alert/cppa-finalizes-rules-admt-risk-assessments-and-cybersecurity-audits-requirements
- **ADMT definition (VERIFIED):** "any technology that processes personal information and uses computation to replace human decision-making or substantially replace human decision-making" — *substantially replace* meaning the output is used without **meaningful human review**.
- **"Significant decision"** scope: financial or lending services, housing, education enrolment or opportunity, employment or independent contracting opportunity or compensation, and healthcare services.
- **Duties:** pre-use notice (purpose, how the ADMT works, what personal information affects outputs, how outputs inform the decision, alternatives, non-retaliation); opt-out via at least two methods, with an exception where a human-reviewed appeal is offered; access rights giving a plain-language explanation of logic and outcome.
- **Deadlines (VERIFIED):** ADMT compliance **1 January 2027**; risk assessments required for processing conducted from **1 January 2026**, with first documentation submission to the CPPA by **1 April 2028** and annually thereafter; cybersecurity audits phased — >$100m revenue by **1 April 2028**, $50–100m by **1 April 2029**, <$50m by **1 April 2030**.
- **Licence: VERIFIED public domain** (California regulations, CCR Title 11 Div. 6).
- **Reuse: PROVISION TEXT + ORACLE.** The *meaningful human review* test is the US analogue of AI Act Art. 14 and GDPR Art. 22, and it is defined operationally enough to test.

---

## PART G — COPYRIGHT / IP CONTAMINATION

### G.1 EU: DSM Directive (EU) 2019/790 Art. 4 TDM opt-out — **VERIFIED**
- URL: https://eur-lex.europa.eu/eli/dir/2019/790/oj — **licence VERIFIED 2011/833/EU.**
- Art. 3: TDM for scientific research by research organisations/cultural heritage institutions, non-overridable. **Art. 4: general TDM exception for lawfully accessible works, subject to Art. 4(3) — the exception applies "on condition that the use … has not been expressly reserved by their rightholders in an appropriate manner, such as machine-readable means in the case of content made publicly available online."**
- AI Act **Art. 53(1)(c)** converts this into an affirmative GPAI-provider duty: put in place a policy to identify and respect Art. 4(3) reservations, **including for training conducted outside the EU where the model is placed on the EU market**.
- **Reuse: PROVISION TEXT + ORACLE.** "Did the crawler honour robots.txt / TDM Reservation Protocol / `tdm-reservation` signals for every domain in this training shard?" is directly testable.

### G.2 Verified EU/German case law on TDM and memorisation
- **LAION v. Kneschke** — **Higher Regional Court Hamburg, 10 December 2025, 5 U 104/24 (VERIFIED):** dismissal upheld; downloading and processing the photograph to build the dataset was a reproduction but was **justified by the TDM exception**; **natural-language opt-outs are insufficient — a machine-readable reservation is required**; broader TDM latitude for non-profit research. **Appeal pending before the Bundesgerichtshof, I ZR 281/25, hearing scheduled 3 September 2026 — outcome UNKNOWN as of 2026-09-05.**
- **GEMA v. OpenAI** — **Munich Regional Court I, 11 November 2025, 42 O 14139/24 (VERIFIED):** song lyrics **memorised in model parameters constitute an unauthorised reproduction**; the court **rejected the TDM exception for model training**, reasoning the exception covers analysis, not storage/memorisation; outputs also infringed. **Appeal pending, OLG München 6 U 3662/25 e — not final.**
- Source: https://www.morganlewis.com/pubs/2026/06/ai-and-copyright-judicial-landscape-in-germany
- **Corpus implication:** memorisation is now a *litigated legal risk category*, not merely a technical curiosity. A provision requiring memorisation/regurgitation testing before release is supportable on current EU authority — but must be marked as resting on a **non-final first-instance judgment under appeal**.

### G.3 US fair-use litigation — **VERIFIED status only**
- **Bartz v. Anthropic (N.D. Cal., Alsup)** — June 2025 order held training on lawfully acquired books was fair use but that building a library from pirated copies was not; the piracy class settled for **$1.5 billion**, and the settlement **received FINAL APPROVAL in July 2026**. Sources: https://www.jurist.org/news/2026/07/judge-approves-record-1-5-billion-settlement-involving-anthropic/ ; https://www.authorsalliance.org/2026/07/21/bartz-v-anthropic-settlement-receives-final-approval/ **Note: the settlement means there is no appellate ruling — Bartz sets no binding precedent on fair use.**
- **NYT v. OpenAI & Microsoft (S.D.N.Y., consolidated with Authors Guild and Daily News)** — March 2025: motion to dismiss granted in part; **direct and contributory infringement claims survived**; DMCA §1202 and common-law unfair competition dismissed. **November 2025:** Magistrate Judge Wang ordered production of **20 million de-identified ChatGPT conversation logs**; **affirmed by Judge Stein 5 January 2026**. Output-log preservation order (13 May 2025) remains a live data-governance constraint. **NO merits ruling on fair use has issued.** Summary-judgment briefing closed 2 April 2026; **no trial date set.** Source: https://ailawsuittracker.com/cases/new-york-times-v-openai/
- **Thomson Reuters v. ROSS Intelligence (D. Del. → 3d Cir.)** — February 2025: Judge Bibas granted summary judgment for Thomson Reuters, holding the use of Westlaw headnotes was **not fair use** (not transformative; same purpose of helping lawyers find case law). Two questions certified for interlocutory appeal: originality of the headnotes, and fair use. **Oral argument held 11 June 2026** before Judges Restrepo, Montgomery-Reeves and Bove. **NO Third Circuit decision as of 2026-09-05; a ruling is expected late 2026.** Sources: https://www.bakerbotts.com/thought-leadership/publications/2026/july/third-circuit-hears-oral-argument ; https://www.lawnext.com/2026/06/at-3rd-circuit-judges-press-ross-and-thomson-reuters-on-fair-use-ai-training-and-market-harm.html
- **Corpus implication: US fair use for AI training is UNRESOLVED at the appellate level.** No provision may assert that training on copyrighted material is or is not lawful in the US. The defensible provisions are **procedural**: do not acquire from known pirate sources; record provenance; test for regurgitation.

### G.4 Licence-detection and clone-detection ground truth
| Source | URL | Contents | Format | Licence | Reuse |
|---|---|---|---|---|---|
| **ScanCode Toolkit** | https://github.com/aboutcode-org/scancode-toolkit | Licence, copyright and dependency detection; thousands of licence texts and detection rules | Python; JSON/YAML/HTML/SPDX/CycloneDX output | **VERIFIED: Apache-2.0 overall; CC-BY-4.0 for the reference datasets** (licence texts and rules) | **ORACLE** — the reference implementation for "what licence is this file under" |
| **ScanCode LicenseDB** | https://scancode-licensedb.aboutcode.org/ · https://github.com/aboutcode-org/scancode-licensedb | Open database of all known licences with SPDX keys | JSON/YAML/HTML | **VERIFIED: CC-BY-4.0 data** (per the toolkit's dataset statement) | **FACTOR VOCABULARY** — canonical licence identifiers |
| **google/licensecheck** | https://github.com/google/licensecheck | Heuristic classifier matching text against known OSS licences; conservative, false-positive-averse | Go library | **VERIFIED: BSD-3-Clause** (repo); licence of the bundled `licenses/` texts **UNVERIFIED** | **ORACLE** — a fast second opinion; disagreement with ScanCode is a useful test signal |
| **Zacchiroli et al., licence text variants dataset** | https://arxiv.org/pdf/2204.00256 | Large-scale dataset of OSS licence text variants mined from Software Heritage | Dataset + paper | **UNVERIFIED** | Ground truth for detector evaluation, pending licence check |

### G.5 BigCode `The Stack` — the reference opt-out regime — **VERIFIED**
- The Stack v1: https://huggingface.co/datasets/bigcode/the-stack (3TB/30 languages → v1.1 6TB/358 languages → v1.2 with additional opt-outs and malicious-file filtering). v1.1 **removed MPL/EPL/LGPL copyleft** and expanded to 193 approved permissive licences.
- **The Stack v2:** https://huggingface.co/datasets/bigcode/the-stack-v2 — **3.28 billion unique files, 658 programming languages, 104.2 million GitHub repositories**, with **Software Heritage SWHIDs as per-file provenance identifiers**. `the-stack-v2-dedup` is the near-deduplicated variant.
- **Licence detection method (VERIFIED):** repository-level licence from GH Archive where available; **ScanCode Toolkit at file level for 96.93% of cases**, filtered against Blue Oak Council-approved permissive licences and ScanCode's own categorisation.
- **Dataset licence (VERIFIED): "other" — there is no single licence over the collection.** Terms of use require: a separate agreement with **Software Heritage / INRIA** for bulk download; adherence to the Software Heritage principles for language-model training; **respect for each file's original licence including attribution clauses**; and using the most recent version so that removal requests take effect.
- **Opt-out (VERIFIED):** https://github.com/bigcode-project/opt-out-v2 (per-repository, per-commit, per-issue removal requests, retained so removed content does not reappear) and the **"Am I in The Stack?"** lookup at https://huggingface.co/spaces/bigcode/in-the-stack.
- **Reuse: ORACLE + PROCESS TEMPLATE — but NOT as corpus text.** The Stack itself must not be redistributed under the corpus's own licence. What *is* reusable is the *mechanism*: SWHID-anchored per-file provenance, ScanCode-based licence classification, permissive-only filtering, a public opt-out register, and a monotonic removal guarantee. That five-part mechanism is exactly what a "no GPL/AGPL contamination in generated code" provision needs as its compliance evidence.
- `codeparrot` near-deduplication / clone-detection utilities exist within the BigCode/HF ecosystem but **their specific repository licences were not verified when this survey was compiled — UNVERIFIED.**

### G.6 Evaluation-set contamination — **no regulatory source; research literature only**
- No binding instrument in this lane regulates benchmark contamination. The nearest normative hooks are **GPAI CoP Measure 3.2** (state-of-the-art evaluations, open-ended testing, red-teaming), **AI Act Annex XI §2** (evaluation strategy, criteria, limitations), and **METR's "full capability elicitation"** common element — all of which are defeated by a contaminated eval set.
- Research base (survey material, licences vary; several arXiv items are **CC BY 4.0 — VERIFIED for arXiv/2510.02386**): contamination taxonomies at https://arxiv.org/html/2608.29463 and https://arxiv.org/html/2605.19999v1 ; detection surveys at https://arxiv.org/pdf/2406.19314.
- **Reuse: FACTOR VOCABULARY + ORACLE.** Canary-string checks, n-gram overlap between training shards and held-out evals, and held-out-set access logging are all testable. Because contamination invalidates the evidence on which every capability-threshold gate depends, it deserves an ABSOLUTE provision even though no statute names it.

---

## PART H — RECOMMENDED PROVISIONS FOR A FRONTIER-LLM CONSTITUTION

### Design principle for the ABSOLUTE marking

A provision should be marked **ABSOLUTE** only when all four hold:

1. **A statutory or safety floor exists** — it is grounded in text that is binding *now*, or it is a physical-irreversibility floor where the cost of being wrong is unrecoverable.
2. **No precedent should be able to soften it** — the harm is not the sort that accumulates gradually and can be corrected on discovery; a single wrong decision is terminal or near-terminal.
3. **It is decidable at change-review time** — a reviewer can determine compliance from the artefacts in front of them, without predicting the future.
4. **Softening it would corrupt the evidence base for other provisions.** This fourth criterion is why evaluation-set contamination belongs in Tier 1 despite having no statute behind it: a contaminated eval set silently converts every other safety gate into theatre.

Tier 2 covers obligations that are real and enforceable but admit **structured, recorded, accountable derogation** — a named approver, a documented rationale, a time limit, and a remediation plan. Tier 3 is advisory: it shapes review and generates findings but never blocks a change.

---

### TIER 1 — NON-DEROGABLE (ABSOLUTE)

**T1-1 — Prohibited practices bar.** No change may introduce, enable or restore a capability falling within AI Act Art. 5(1)(a)–(h) or the NCII/CSAM prohibition added by Reg. (EU) 2026/1744, in any product surface reachable from the EU. **Grounding:** AI Act Art. 5, in force since 2 Feb 2025, EUR 35m/7% penalty tier, no proportionality defence in the text. **Why absolute:** the AI Act itself admits no derogation; Art. 5(1)(e) (untargeted facial-image scraping) additionally binds the *data pipeline*, not just the product, and so is directly a software-change concern. A precedent softening this would be a precedent to break the law.

**T1-2 — Human oversight override for high-risk features.** Any feature classified high-risk must preserve, in the shipped build, the operator's ability to (i) disregard, override or reverse the output and (ii) interrupt operation via a stop function; and where the feature performs biometric identification, the two-natural-person verification. **Grounding:** AI Act Art. 14(4)(d)–(e) and 14(5) (verbatim); GDPR Art. 22(3) right to human intervention; CPPA ADMT "meaningful human review"; Colorado SB 26-189 meaningful human review of contested decisions. **Why absolute despite the Art. 14 deferral to 2 Dec 2027:** the *norm* is triple-sourced — GDPR Art. 22(3) and the CPPA ADMT regulations bind now, and the AI Act binds on a fixed date. More importantly, an override path is the last line of defence when every earlier gate has failed; a "we removed the stop button for latency" precedent is precisely the kind of local optimisation that a constitution exists to make unavailable. Note the layering: Art. 14(4)(b)'s automation-bias awareness duty means an override that exists but is never realistically exercisable does not satisfy this provision.

**T1-3 — No deployment above a capability threshold without a completed safety case.** Where evaluations indicate a model has reached or plausibly reached a defined capability threshold, deployment (internal or external) is barred until a safety case has been completed, independently reviewed, and accepted by the designated governance body — and if the required mitigations cannot be met, the model is not deployed. **Grounding:** Frontier AI Safety Commitments Outcome II (**OGL v3.0 — quotable verbatim**), the only openly-licensed statement of this norm; corroborated by AI Act Art. 55(1)(a)–(b) for systemic-risk GPAI, California SB 53's framework and transparency-report duties, and the convergent practice of DeepMind FSF v3.1 (pre-deployment governance review of residual risk), Anthropic RSP v3.4 (ASL standard must be met or deployment does not proceed), and OpenAI PF v2 (Capabilities Report + Safeguards Report → Safety Advisory Group). **Why absolute:** this is the one gate whose failure is not correctable after the fact. Deployment is irreversible in the way that matters — weights and capabilities, once released or exposed, cannot be recalled. **Threshold anchors, and a warning:** the corpus should carry *both* the AI Act's **10^25 FLOP** presumption (Art. 51(2), in force) and California SB 53's **10^26 FLOP** definition (in force), and must not conflate them; the rescinded EO 14110's 10^26 trigger must be marked historical. Compute thresholds are proxies, not the provision — the provision is the *gate*, and a model below threshold that evaluates as capable still triggers it.

**T1-4 — Model-weight security.** Unreleased model weights must remain under the access-control, supply-chain and egress protections specified for the model's tier; no change may lower those protections, widen weight access, or create an unlogged egress path, without the change itself being treated as a Tier 1 review. **Grounding:** AI Act Art. 55(1)(d) (adequate cybersecurity for the model and its physical infrastructure — **in force**); GPAI CoP Commitment 6 / Measure 6.2 / Appendix 4 (protection until parameters are public or deleted); **California SB 53's express requirement that a frontier AI framework describe cybersecurity practices securing unreleased model weights** — this is binding statute, not aspiration; METR's cross-lab finding that weight security is one of nine universal elements; DeepMind's security levels 2–4 tied to CCLs; RAND RR-A2849-1's five security levels (**cite only — VERIFIED all rights reserved, noncommercial-use-only representation; do not copy the SL definitions into the corpus**). **Why absolute:** weight exfiltration is the single failure mode that voids every other control simultaneously — deployment gates, refusal training, monitoring, and rate limits are all properties of *serving infrastructure*, and none survives the weights leaving it. It is also the only failure with no remediation path whatsoever.

**T1-5 — Evaluation-set integrity.** No change may cause held-out evaluation data to enter a training corpus, nor may a model be evaluated for a threshold determination on data it may have trained on. Contamination checks must be run and their results recorded before any evaluation result is used in a deployment decision. **Grounding:** no statute names contamination; it is derived from AI Act Annex XI §2 (evaluation strategy, criteria, limitations), Art. 55(1)(a) (state-of-the-art evaluation protocols), GPAI CoP Measure 3.2, and METR's "full capability elicitation" element — every one of which is silently defeated by a contaminated benchmark. **Why absolute despite having no statutory hook:** this is the fourth-criterion case. T1-3 is only as good as the evidence it consumes. A contaminated eval does not merely produce a wrong number; it produces a *confidently* wrong number that passes review, and it does so invisibly. A defeasible contamination rule is functionally no rule at all, because the pressure to soften it always arrives at exactly the moment — a release deadline with a marginal eval result — when softening it is most dangerous. Enforceable with Inspect (**MIT**) eval logs plus canary-string and n-gram overlap checks.

**T1-6 — No prohibited-provenance training data; PII floor.** Training corpora must not include data from known-unlawful acquisition sources, untargeted facial-image scrapes, or datasets whose provenance cannot be attested. Special-category personal data (GDPR Art. 9) must not be deliberately collected or retained for training outside the Art. 10(5) bias-detection safeguard. **Grounding:** AI Act Art. 5(1)(e) (facial scraping — in force); GDPR Arts. 5(1)(c) and 9; **EDPB Opinion 28/2024 holding (4) — unlawfulness in the development phase propagates into deployment unless the model is demonstrably anonymous**; Bartz v. Anthropic, where the $1.5bn liability attached specifically to *pirated acquisition*, not to training. **Why absolute:** the EDPB's propagation holding and Bartz together establish that a provenance defect is not a contained defect. It is not curable downstream — Art. 17 erasure against model weights has no reliable technical remedy short of retraining, which means the only effective control point is *before* the data enters the corpus. Once trained, the violation is baked into the artefact.

*A deliberate exclusion:* the general question of whether training on copyrighted material is lawful is **not** a Tier 1 provision, because it is unresolved — Thomson Reuters v. ROSS is undecided at the Third Circuit, NYT v. OpenAI has no merits ruling, Bartz settled without precedent, and LAION and GEMA point in opposite directions and are both under appeal. A constitution that asserted an answer here would be asserting something no court has held. The *procedural* pieces of it (T1-6's provenance floor, T2-4's opt-out honouring) are what can be stated with integrity.

---

### TIER 2 — DEFEASIBLE (binding, but overridable with recorded justification, named approver, expiry and remediation)

**T2-1 — High-risk lifecycle requirements.** Risk management (Art. 9), data governance (Art. 10), technical documentation (Art. 11/Annex IV), automatic logging (Art. 12), deployer transparency (Art. 13), and accuracy/robustness/cybersecurity (Art. 15) for Annex III features. **Tier 2 not Tier 1 because these are deferred to 2 December 2027** by Reg. (EU) 2026/1744 — they are known future law, so a change may proceed with a recorded gap and a remediation date, but the gap must be tracked against a fixed deadline. Art. 15(5)'s poisoning/adversarial-example resilience should be graded against the NIST AI 100-2 E2025 taxonomy (public domain).

**T2-2 — GPAI documentation and transparency.** Annex XI technical documentation, Annex XII downstream information, the Art. 53(1)(d) public training-content summary on the Commission template, Art. 50 synthetic-content marking, and California SB 942/AB 853 latent disclosures and detection tooling. **In force**, but defeasible in the narrow sense that a documentation gap is *correctable after the fact* — the harm accrues gradually and is remediable, which is exactly what Tier 1 excludes. Machine-checkable, so it makes a good oracle even at Tier 2.

**T2-3 — Serious incident reporting.** AI Act Art. 55(1)(c) (AI Office, without undue delay) and California SB 53 (Cal OES, 15 days; 24 hours where imminent risk of death or serious injury). Tier 2 rather than Tier 1 only because the reporting duty attaches *after* the incident — it does not gate a change. Any change that degrades incident detection or the reporting path, however, should escalate to Tier 1 review, since it removes the trigger for the duty.

**T2-4 — Copyright policy and TDM opt-out honouring.** AI Act Art. 53(1)(c) plus DSM Art. 4(3): crawlers must honour machine-readable reservations, and the corpus should record per-domain reservation state. Supported by LAION (machine-readable reservations required; natural-language ones insufficient) — but that case is **under appeal to the BGH with a hearing on 3 September 2026**, so the rule's exact contours may move. Defeasible because the legal standard is genuinely unsettled; a documented, good-faith, reviewed deviation is defensible in a way that a T1 breach never is.

**T2-5 — Memorisation and regurgitation testing.** Before release, test for verbatim reproduction of training data — copyrighted text, code carrying copyleft licences, and personal data. **Grounding:** GEMA v. OpenAI (memorisation as reproduction) — **first-instance, under appeal**; EDPB Opinion 28/2024's extraction-and-query-based anonymity test; NIST AI 600-1's Intellectual Property and Data Privacy risk categories. Tier 2 because the legal basis is non-final, but this is the provision most likely to be promoted to Tier 1 if the OLG München affirms.

**T2-6 — No GPL/AGPL contamination in generated or shipped code.** Where a model generates code, or where model outputs are incorporated into shipped software, run licence detection (ScanCode, **Apache-2.0** / **CC-BY-4.0** data) and clone detection against known copyleft corpora, and block incorporation of matched copyleft-derived material into permissively-licensed products. Provenance evidence modelled on The Stack v2's mechanism — SWHID anchoring, ScanCode classification, permissive-only filtering, a public opt-out register, monotonic removal. Tier 2 because the underlying legal question (whether model output derived from copyleft training data is itself a derivative work) is unresolved everywhere.

**T2-7 — DPIA and legitimate-interest assessment for training.** GDPR Art. 35 DPIA and the EDPB three-step legitimate-interest test, refreshed whenever the data mix, scale, or purpose materially changes. Tier 2 because it is an assessment duty, not a prohibition — but a *missing* assessment where one is mandatory should block release.

**T2-8 — ADMT notice, opt-out and explanation.** CPPA ADMT regulations for significant decisions (compliance date 1 January 2027), Colorado SB 26-189 (1 January 2027), Illinois HB 3773. Tier 2 with an explicit annotation that these are **under active federal preemption challenge** via EO 14365's AI Litigation Task Force — a corpus that presents state AI law as settled would be misleading.

---

### TIER 3 — ADVISORY (shapes review, generates findings, never blocks)

**T3-1 — NIST AI RMF 1.0 and AI 600-1 suggested actions**, cited by action ID (GV-*, MP-*, MS-*, MG-*). Advisory by construction: NIST publishes *suggested actions*, not requirements, and the AI RMF is **currently under revision under the AI Action Plan** — so specific action text may change. Public domain, so ideal as the corpus's neutral cross-reference spine, mapping each Tier 1/2 provision to one or more NIST action IDs.

**T3-2 — GPAI Code of Practice commitments** beyond what Arts. 53/55 themselves require. **Voluntary by the Commission's own characterisation**; a non-signatory (Meta) can comply by other means. Advisory, with the caveat that for a signatory these become contractually self-binding and effectively rise to Tier 2.

**T3-3 — Corporate frontier safety frameworks** (DeepMind FSF v3.1, Anthropic RSP v3.4, OpenAI PF v2, Meta FAIF v1.1) as comparative practice. Advisory because they are unilateral, self-amendable — the RSP changed four times between February and July 2026 — and, critically, **all-rights-reserved**, so the corpus can only encode paraphrased structure and cite the source. METR's nine common elements are the right neutral vocabulary for this row.

**T3-4 — OMB M-25-21 / M-25-22.** Advisory for a private developer; rises to Tier 2 contractually on federal sale.

**T3-5 — AI Action Plan and EO 14365 policy directions.** Advisory: they are policy and preemption strategy, not obligations on a developer, but they are the best available signal of which Tier 2 state provisions may become unenforceable.

---

### Two cautions for whoever builds the corpus

**Do not ingest text you have no licence to.** The corpus can safely carry: EU legal texts and Commission publications (2011/833/EU), US federal and California statutes and regulations (public domain / government edicts), NIST publications (17 U.S.C. §105), the Seoul Frontier AI Safety Commitments (OGL v3.0), the AISI safety-case template papers (CC BY 4.0 via arXiv), Inspect and inspect_evals (MIT), and ScanCode (Apache-2.0 code / CC-BY-4.0 data). It must **not** carry verbatim: any lab frontier safety framework, RAND RR-A2849-1's security-level definitions, the artificialintelligenceact.eu or code-of-practice.ai renderings, or The Stack's contents.

**Version-pin everything, and record the as-of date.** This lane moved substantially in the twelve months to September 2026: the AI Act's high-risk regime was deferred by an amending regulation, the RSP went through five versions, EO 14365 opened a preemption front against the state laws several provisions rest on, Colorado repealed and replaced its statute, and two of the three US copyright anchors are still undecided. Every provision should carry the instrument's version, its in-force date, and — where a case is on appeal or a framework is under revision — an explicit instability flag.
