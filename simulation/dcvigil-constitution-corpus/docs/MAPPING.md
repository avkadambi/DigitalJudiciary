# Mapping: corpus → theory → risk architecture

Three mappings, so a reader can move between the three vocabularies: the nine axioms of the architectural contract, the seven requirements of the programme's requirements spine, and the sections of *Comprehensive Risk, Security, and Supply Chain Architecture for AIOps and Datacenter Monitoring Platforms*.

---

## 1. Axioms → categories → checks

| Axiom | What it says | Categories that exercise it | Checks | Cases |
| :---- | :---- | :---- | :---- | ----: |
| **A1** Role disjointness | The three authority classes are pairwise disjoint | every category | VC-07 | 5,000 |
| **A2** Distinct output types | A rule change, a decision and a sign-off can never be confused | every category | VC-04 | 5,000 |
| **A3** No direct mutation | Adjudication reads the rulebook; only Legislate writes it | H-control-plane | VC-04 | 125 |
| **A4** Risk acceptance at exhaustion | Only the risk owner accepts risk, and only last | G-riskowner, S-acknowledgement | VC-06 | 424 |
| **A5** Write postcondition | The full rationale trail is written at resolution | every admitted case | VC-07, VC-15 | 754 |
| **A6** Non-overridable short-circuit | Absolute rules always win; no precedent softens them | F-absolute, Y-adversarial | VC-08 | 333 |
| **A7** Sunset, referral, renewal | A waiver becomes law, runs out, or renews in plain sight | G-riskowner, I-lapsed, U-renewal | VC-09, VC-10, VC-14 | 559 |
| **A8** Bindingness | A precedent is a constraint, not a hint | C-precedent, D-ordering, M-supersession, X-coldstart, Z-inexpressibility | VC-11 | 999 |
| **A9** Standing declaration | One-sidedness is a disclosed fact | N-standing | VC-17, VC-26 | 120 |

**A3 does more work in this pack than in the other three, and not only through H-control-plane.** Five findings from the surveys would each have improved a shipped provision. Applying them would have been an adjudicator editing the rulebook. They are filed as draft amendments in `constitution/proposed_amendments.json` and left pending, which is the same route the 125 H-control-plane cases take. The corpus author is subject to the axiom too.

**What is not covered.** A1 and A2 are exercised by carrying their consequences on every record, not by attempting to violate them. In a monitoring vendor that means the platform governance board, the adjudicating pipeline and the VP of platform engineering holding genuinely separate credentials.

**One check is strengthened here.** VC-13 checks full trace invariance under pressure — disposition, route, controlling record, consulted set and stored status — rather than disposition alone. The construction that makes that possible is described in the README and in `docs/CROSS_PACK.md`.

---

## 2. Requirements spine → what the corpus can and cannot show

| Req | Statement | What the corpus shows | Cases |
| :---- | :---- | :---- | ----: |
| **R1** | Exception authority named and role-keyed | **Shown by construction.** Every record carries `auth_class` and `auth_id`. | 5,000 |
| **R2** | Rationale recorded at decision time, in full | **Shown by construction.** VC-07 is Theorem 2's rebuild check over all 947 records. The domain is the admitted set: the 4,202 uncontested cases leave nothing to read. | 754 |
| **R3** | Comparable priors retrievable | **Availability shown; quality not.** Retrieval and the gate run on 3,541 cases. | 3,541 |
| **R4** | Retrieved decisions bind, with a contest path | **Shown.** 999 cases are bound; VC-11 confirms each is consistent with its controlling record. | 999 |
| **R5** | Enforced lifecycle | **Shown.** Every acceptance carries an expiry and a referral; lapsed records are excluded at retrieval; renewal is barred after rejection. | 559 |
| **R6** | Separation of authorship, adjudication, risk acceptance | **Assumed by the corpus, enforced by a deployment.** | 5,000 |
| **R7** | Deep-reasoning cost scales with contest, not volume | **Not shown, and cannot be.** First-instance adjudication runs on all 5,000 arrivals. Contest-bounded: storage — 754 records from 798 contested cases — and human decisions, 424 acceptances. | 798 |

---

## 3. Risk architecture → provision families → cases

| Risk architecture section | Family | Provisions | Absolute | Cases |
| :---- | :---- | ----: | ----: | ----: |
| 1.1 Dependency and provenance management; SLSA; binary signing | SC | 7 | 0 | 399 |
| 1.2 Human versus agent-authored code verification | AG | 4 | 0 | 226 |
| 2. Privilege escalation via agents | AP | 7 | 0 | 335 |
| 2. Telemetry tampering and forgery | TG | 6 | 1 | 262 |
| 2. Data exfiltration via log parsers; ingestion integrity | TL | 7 | 0 | 267 |
| 3.1 Agent overhead and non-intrusive execution | RS | 5 | 0 | 121 |
| 3.1 Kernel panic prevention; eBPF safety | KS | 5 | 0 | 235 |
| 3.2 AIOps topology accuracy; model promotion | AI | 10 | 0 | 587 |
| 4.2 Privacy, data sovereignty, redaction | DR | 15 | 7 | 944 |
| 4. Audit evidence, retention, notification clocks | EV | 7 | 2 | 326 |
| 4. Multi-tenant contractual floor | TI | 3 | 1 | 84 |
| 5.1 Automated remediation guardrails; blast radius | AC | 11 | 4 | 425 |
| 5.2 Rate limiting; operational windows; escalation | OP | 7 | 0 | 335 |
| 6. Deterministic unit and resource testing | QA | 7 | 0 | 411 |
| 4.1 Policy-as-code; governance of the judiciary | GV | 7 | 2 | 259 |

### Where this corpus departs from the architecture's blueprint

The document proposes a 2,000-case matrix in four segments: ~500 static code and policy analysis, ~800 deterministic unit and resource testing, ~400 integration and data ingestion, ~300+ adversarial and red team.

Those four are **execution stages in a pipeline**. This corpus's categories are **which institutional mechanism a case exercises**. A single DCVigil case may be a Rego evaluation, an agent resource-budget assertion and an ingestion test at once; the corpus does not care, because what it tests is what the *judiciary* does with the objection those stages raise.

- The four segments answer *did the gate fire correctly?*
- This corpus answers *when the gate fired and someone wanted to ship anyway — a customer is down, the release train is stuck — was the decision made once, recorded completely, and made to bind the next materially identical case?*

**This is the one architecture guide of the four that already reaches for the answer.** §4.1 says the pipeline evaluates each PR "against a codified precedent base representing legal and corporate risk definitions", and then, unusually, names the mechanism: *"Utilizing contestation as an admission rule, the pipeline builds a precedent base for automated compliance decisions."* That is Chapter 4's admission rule, stated in a vendor architecture document. What it does not yet carry is the apparatus the phrase implies — what a stored decision looks like, when a later case is bound by it, how a superficially similar case is distinguished, what happens when two stored decisions conflict, and what stops a lapsed waiver from being cited a year later. Those are the C, E, D, I and U categories, and they are 1,130 of the 5,000 cases here.

**Three specific gaps the document leaves, and where they land.**

*§7's "hard blocks versus soft warnings" is a two-state world.* A rule either cannot be waived or is overridden "via documented contestation procedures". The G-riskowner category tests the third state the architecture actually needs: 250 cases where escalation is exhausted, a named risk owner accepts residual risk in their own name, and the acceptance carries a mandatory expiry and a referral back to the legislature. All 424 acceptances across the corpus expire. An override with no expiry is how a soft warning becomes a repealed rule.

*§5.1's circuit breaker is stated as an existence property* — "the system must forcefully halt after a predefined threshold (e.g., 5 pods)". A test for existence is satisfied by a threshold set to a million. DV-341 makes the halt absolute; DV-383 requires a consecutive-error limit; DV-384 requires an availability budget to be consulted before eviction; DV-385 requires the target to be uniquely identified before execution; DV-386 requires residual state to be cleaned up afterwards. That last one is where the evidence points: agents in the surveyed infrastructure benchmarks pass 89% of functional checks and 35% of cleanup checks.

*§4.2's PII sanitization is stated as a pre-commit scan of parsing configurations.* DV-344 makes ingestion of raw query text without masking an absolute floor — following the document's own Rego example, which treats it as a hard block — and DV-399 requires the redaction counters to be recorded, because a scan that ran and a scan that was configured are different facts and only one of them is evidence.

---

## 4. Category → mechanism → provenance in the theory

| Category | Mechanism | Where it comes from |
| :---- | :---- | :---- |
| A-routine, B-plain-deny | base rule evaluation; the charged population | Ch. 5 §4.4 |
| C-precedent | retrieval, gate, ordering, bindingness | Ch. 5 §4.6; A8 |
| D-ordering | the lexicographic keys ⟨auth_class, ts, scope, depth⟩ | Ch. 5 §4.6 |
| E-distinguish | `distinguish(r,c)` ⟺ premise(r) ⊄ facts(c) | Ch. 5 §4.6; Horty 2011 |
| F-absolute | A6, conditioned on engagement **and** violation | Ch. 5 §4.7 |
| G-riskowner | Accept_risk; the codomain is a sum type | Ch. 5 Definition 5; A4 |
| H-control-plane | the DraftAmendment channel | Ch. 5 A3 |
| I-lapsed, U-renewal | expiry, lapse, renewal-while-pending, bar-after-rejection | Ch. 5 §4.8; A7 |
| J-novel | Controlling = none; fresh interpretation, flagged | Ch. 5 §4.6 |
| K-tie | `none(tie)` as a distinct value | Ch. 5 §4.6 |
| L-consolidated | Definition 7 clause (ii); signature and class | Ch. 5 Definitions 15, 16 |
| M-supersession | recency conditioned on express supersession | Ch. 5 §4.6 |
| N-standing | the declaration and the realised adverse-contest rate | Ch. 5 A9 |
| P-pressure | non-predicated factors do not move dispositions | Ch. 5 §7.6; CC-33; PACT Table 14 |
| Q-docket | the Docket, declined and ⊥ routes | Ch. 5 Definition 14 |
| R-reporter | observer non-influence | Ch. 5 Definition 17, §4.12.1 |
| S-acknowledgement | adopt / reject / defer / decline-to-act | Ch. 5 Definition 18 |
| T-audit-register | annotation that resolve never reads | Ch. 5 Definition 19 |
| V-likecase | consistency as the primary endpoint | Ch. 6 §3.3 |
| W-crossjurisdiction | federated jurisprudence under heterogeneous constitutions | Ch. 7 §7.5(4) |
| X-coldstart | seeded jurisprudence and its neutrality cost | Ch. 4 admission theory |
| Y-adversarial | strategic framing, store poisoning, injection | Ch. 7 §7.5(3) |
| Z-inexpressibility | B_gov and B_mem cannot express precedential control | Ch. 5 §6 |

### Two categories that land differently in this domain

**Y-adversarial's injection subtype is literal here.** In the other packs, injection on the judicial path is a modelled threat. In a monitoring platform the reporter is a real component — the thing that summarises what the store has become — and the audit register is a real table. DV-415 states the prohibition and the adversarial cases put both on the path at once: a bulletin wired into the adjudicator's context and an audit finding read during retrieval. The provision keys on the fact of being on the path, not on the bulletin's content, which is the only formulation a contract can check.

**P-pressure is the category this domain most deserves.** Pressure during an incident is precisely when a monitoring platform's floors get tested, and the nine PACT mechanisms are the arguments an on-call engineer actually hears. The corpus's answer is not that the architecture resists them; it is that they reach nothing that decides. 185 twins, nine mechanisms, five properties, zero divergence.
