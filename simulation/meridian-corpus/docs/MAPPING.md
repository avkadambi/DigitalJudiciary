# Mapping: corpus → theory → risk architecture

Three mappings, so a reader can move between the three vocabularies: the nine axioms of the architectural contract, the seven requirements of the programme's requirements spine, and the sections of *Comprehensive Risk Architecture for FinTech Software Development*.

---

## 1. Axioms → categories → checks

| Axiom | What it says | Categories that exercise it | Checks | Cases |
| :---- | :---- | :---- | :---- | ----: |
| **A1** Role disjointness | The three authority classes are pairwise disjoint | every category | VC-07 | 5,000 |
| **A2** Distinct output types | A rule change, a decision and a sign-off can never be confused | every category | VC-04 | 5,000 |
| **A3** No direct mutation | Adjudication reads the rulebook; only Legislate writes it | H-control-plane | VC-04 | 125 |
| **A4** Risk acceptance at exhaustion | Only the risk owner accepts risk, and only last | G-riskowner, S-acknowledgement | VC-06 | 428 |
| **A5** Write postcondition | The full rationale trail is written at resolution | every admitted case | VC-07, VC-15 | 706 |
| **A6** Non-overridable short-circuit | Absolute rules always win; no precedent softens them | F-absolute, Y-adversarial | VC-08 | 338 |
| **A7** Sunset, referral, renewal | A waiver becomes law, runs out, or renews in plain sight | G-riskowner, I-lapsed, U-renewal | VC-09, VC-10, VC-14 | 575 |
| **A8** Bindingness | A precedent is a constraint, not a hint | C-precedent, D-ordering, M-supersession, X-coldstart, Z-inexpressibility | VC-11 | 985 |
| **A9** Standing declaration | One-sidedness is a disclosed fact | N-standing | VC-17, VC-26 | 120 |

**A3 carries more weight in this pack than in any of the other four, and most of it falls outside H-control-plane.** Meridian is the one pack in the programme whose provisions are not invented: each of the thirty-seven shipped provisions cites a real instrument. That makes it the one pack where a literature survey can find the constitution *wrong* rather than merely incomplete — and four surveys did, seven times over. Six of the seven are the consequence of an instrument that moved after the pack was written:

- **SR 11-7 was superseded on 17 April 2026** by SR 26-2, OCC Bulletin 2026-13 and FDIC FIL-15-2026. Five provisions rest on it and two more cite it in support. The replacement expressly excludes generative and agentic AI from the definition of a model, which leaves MF-307 — the agent-provenance provision — citing an instrument that disclaims its subject matter.
- **CFPB Circulars 2022-03 and 2023-03 were withdrawn on 12 May 2025** (90 FR, Doc. 2025-08286). Two provisions cite them for a duty that is in fact statutory and survives.
- **The Reg B effects test was removed** by 91 FR 21620, effective 21 July 2026. MF-305 cites it. Disparate treatment and the proxy prohibition are untouched, so proxy detection stays a floor and outcome parity becomes a documented firm control.
- **12 CFR Part 1033 is enjoined, not vacated** — *Forcht Bank, N.A. v. CFPB*, E.D. Ky., 29 October 2025. MF-405 is right to carry the status `readiness`, and its statutory anchor at 12 U.S.C. §5533 is what should be cited.
- **NYDFS compensating controls are at §500.12(b), not §500.12(a).** As cited, MF-202 points at the obligation and calls it the exception.
- **18 U.S.C. §1510(b) does not reach SARs.** The tipping-off exposure runs through 31 U.S.C. §5318(g)(2), §5322 and 31 CFR §1020.320(e)(1).

The seventh is the sharpest, and it is not about an instrument moving. **MF-103 as drafted is stricter than the rule it cites.** It requires the Customer Identification Program to complete before an account is opened; 31 CFR §1020.220(a)(2)(ii) permits verification within a reasonable time *after* opening, on risk-based procedures. As written the provision will flag conforming behaviour — and because it is absolute, that flag cannot be risk-accepted by anyone.

Not one of the seven is applied. Each is filed in `constitution/proposed_amendments.json` as PA-01 through PA-07 and left pending. Applying them would be an adjudicator editing the rulebook, which is the same act the 125 H-control-plane cases are routed away from. The corpus author is subject to A3 too — and MF-103 is exactly the case that tests whether the author believes it, because narrowing an absolute provision unilaterally is precisely the act A6 and A3 exist to prevent a non-lawmaker from performing.

**What is not covered.** A1 and A2 are exercised by carrying their consequences on every record, not by attempting to violate them. In a regulated financial institution that means the board risk committee, the adjudicating pipeline and the chief risk officer holding genuinely separate credentials — a control an examiner tests directly and a corpus cannot.

**One check is strengthened here,** as in DCVigil. VC-13 checks full trace invariance under pressure — disposition, route, controlling record, consulted set and stored status — rather than disposition alone.

---

## 2. Requirements spine → what the corpus can and cannot show

| Req | Statement | What the corpus shows | Cases |
| :---- | :---- | :---- | ----: |
| **R1** | Exception authority named and role-keyed | **Shown by construction.** Every record carries `auth_class` and `auth_id`. | 5,000 |
| **R2** | Rationale recorded at decision time, in full | **Shown by construction.** VC-07 is Theorem 2's rebuild check over all 900 records. The domain is the admitted set: the 4,250 uncontested cases leave nothing to read. | 706 |
| **R3** | Comparable priors retrievable | **Availability shown; quality not.** Retrieval and the gate run on 3,418 cases. Whether the retrieved prior is the one a compliance officer would have reached for is not a question this corpus can answer. | 3,418 |
| **R4** | Retrieved decisions bind, with a contest path | **Shown.** 985 cases are bound; VC-11 confirms each is consistent with its controlling record's holding. | 985 |
| **R5** | Enforced lifecycle | **Shown.** All 428 acceptances carry an expiry and emit a referral; lapsed records are excluded at retrieval; renewal is barred after rejection. | 575 |
| **R6** | Separation of authorship, adjudication, risk acceptance | **Assumed by the corpus, enforced by a deployment.** This is the SOX segregation-of-duties question and it is tested by an examiner, not by a test corpus. | 5,000 |
| **R7** | Deep-reasoning cost scales with contest, not volume | **Not shown, and cannot be.** First-instance adjudication runs on all 5,000 arrivals. What is contest-bounded is storage — 706 records from 750 contested cases — and human decisions, 428 acceptances. | 750 |

---

## 3. Risk architecture → provision families → cases

| Risk architecture section | Family | Provisions | Absolute | Cases |
| :---- | :---- | ----: | ----: | ----: |
| 2.2 AML/KYC/BSA; strict-liability sanctions | FC | 11 | 5 | 344 |
| 2.2 PCI-DSS; cardholder data | PD | 7 | 2 | 211 |
| 3.1 Cryptography and key management; GLBA Safeguards | SS | 8 | 1 | 364 |
| 4. Software supply chain security; SLSA | SP | 7 | 0 | 420 |
| 2.2 SOC 2 CC8.1; change control | CQ | 7 | 1 | 478 |
| 6.1 Transaction atomicity; 6.2 ledger immutability | LG | 6 | 1 | 206 |
| 5.2 Precision and mathematical integrity | PR | 5 | 0 | 123 |
| 2.2 DORA; 5.1 timeouts and circuit breakers | RE | 9 | 1 | 436 |
| 2.1 Data privacy and sovereignty | DP | 8 | 1 | 671 |
| 2.2 ECOA/Reg B, FCRA; model risk | FL | 13 | 4 | 520 |
| 2.2 EU AI Act; AI governance | AI | 8 | 1 | 401 |
| 4.3 Agentic code provenance | AG | 5 | 2 | 208 |
| 2.2 UDAAP, TILA, Reg E; complaints | CP | 9 | 2 | 349 |
| 2.2 SOX §404; audit log integrity | EV | 6 | 3 | 221 |
| 7.1 Policy-as-code; governance of the judiciary | GV | 7 | 0 | 252 |

### Where this corpus departs from the architecture's blueprint

The document proposes a 2,000-case matrix in four layers: ~600 static analysis and policy-as-code, ~800 unit tests for logic and precision, ~400 integration and component tests, ~200 DAST and chaos.

Those four are **execution stages in a pipeline**, ordered by mean-time-to-feedback. This corpus's categories are **which institutional mechanism a case exercises**. A single Meridian case may be a Rego evaluation, a BigDecimal assertion and an idempotency integration test at once; the corpus does not care, because what it tests is what the *judiciary* does with the objection those stages raise.

- The four layers answer *did the gate fire correctly?*
- This corpus answers *when the gate fired and someone wanted to ship anyway — the release is blocked, a launch date is public, a named customer is stuck — was the decision made once, recorded completely, and made to bind the next materially identical case?*

**§7.1 of the guide is headed "Contestation as an Admission Rule",** and that is Chapter 4's admission rule named in a vendor architecture document. What §7.1 then supplies is a Rego policy that denies a payment endpoint without an idempotency key — a gate, not a judiciary. The apparatus the heading implies is missing: what a stored decision looks like, when a later case is bound by it, how a superficially similar case is distinguished, what happens when two stored decisions conflict, and what stops a lapsed waiver from being cited a year later. Those are the C, E, D, I and U categories, and they are 1,115 of the 5,000 cases here.

**Three specific gaps the document leaves, and where they land.**

*The guide has no third state.* §7 of the DCVigil guide at least names hard blocks and soft warnings; this one has policy gates that deny and a "time-bound risk acceptance waiver" mentioned once, in §4.2, attached to a CVE. The G-riskowner category tests the state a risk function actually operates in: 250 cases where the automated tiers are exhausted, a named officer accepts residual risk in their own name, and the acceptance carries a mandatory expiry and a referral back to the legislature. All 428 acceptances in this corpus expire. A waiver with no expiry is how a documented exception becomes a repealed rule.

*§4.2's CVE waiver is the one place the guide reaches for an exception, and it is under-specified in exactly the way that matters.* "Unless an explicit, time-bound risk acceptance waiver is attached" names the expiry and stops. It does not say who may attach one, whether attaching one to the same dependency twice is renewal or a new decision, or what happens when the waiver expires and the CVE is still open. MF-539 states the rule; the I-lapsed and U-renewal categories — 215 cases — are what the rule needs behind it.

*§5.2's floating-point prohibition is stated as a SAST rule.* "Test suites must aggressively scan for the use of standard floating-point data types" is a scan, and a scan is a fact about the code, not about the money. MF-549 states the prohibition, MF-550 requires the rounding mode to be declared per currency, MF-551 requires minor units to come from reference data rather than a constant, and MF-553 requires aggregate slippage to be bounded and monitored. The oracle for all four is external and reusable: 3.4 million labelled decimal vectors from `rust_decimal` (MIT) and 245 `@SpecAssertion` annotations from the JSR-354 TCK (Apache-2.0). Banker's rounding stated in a policy and banker's rounding demonstrated against a conformance vector set are different claims.

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

### Three categories that land differently in this domain

**F-absolute means something narrower here, and the shipped pack says so.** Its own commentary is worth restating because it is the clearest statement of Definition 1 anywhere in the programme's demo material: *absolute is not a severity ranking, it is a claim about who may decide.* Strict-liability sanctions exposure and criminal tipping-off are absolute because no officer of the firm holds the authority to accept that risk. GLBA encryption is adjudicable because 16 CFR §314.4(c)(3) contemplates a CISO finding. Encoding the second as absolute would be a lie about the firm's own authority — and a constitution amended weekly is not a constitution. The corpus preserves that discipline in its extension provisions: the thirteen new floors are drawn from the surveys' M1–M7 ranking of duties the firm demonstrably cannot waive, and nothing was promoted to absolute because it sounded serious.

**Q-docket exposes a domain fact the other packs cannot.** The prosecutor rates a fully compliant case at 20 against a per-family threshold τ. Three families here carry τ below that: financial crime at 15, card data and fair lending at 18. In those families a compliant change is *charged anyway* — the decline route does not exist. That is not a defect in the construction; it is what a strict-liability regime looks like when you write its threshold down. The seven provisions reserved for the docket categories are therefore drawn from families where τ exceeds 20, and the reservation comment in `generator/build_corpus.py` says why.

**W-crossjurisdiction is a smaller claim here than its name suggests.** The 200 cases put the same personal-data flow under an EU region and a US one. GDPR Arts. 44–49 do not forbid the transfer; they forbid the *unrecorded* transfer, and MF-561 states the recording duty in a region-neutral form so that the US arm of each pair engages a retention duty instead. What the category does not model is the harder federation question — two constitutions that disagree — which Chapter 7 §7.5(4) leaves open and this corpus does not close.
