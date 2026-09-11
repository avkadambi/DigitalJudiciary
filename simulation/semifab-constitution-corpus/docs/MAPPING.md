# Mapping: corpus → theory → risk architecture

Three mappings, so a reader can move between the three vocabularies: the nine axioms of the architectural contract, the seven requirements of the programme's requirements spine, and the sections of *Security, Quality, and Risk Architecture for Semiconductor Supply Chain Software*.

---

## 1. Axioms → categories → checks

| Axiom | What it says | Categories that exercise it | Checks | Cases |
| :---- | :---- | :---- | :---- | ----: |
| **A1** Role disjointness | The three authority classes are pairwise disjoint | every category | VC-07 | 5,000 |
| **A2** Distinct output types | A rule change, a decision and a sign-off can never be confused | every category | VC-04 | 5,000 |
| **A3** No direct mutation | Adjudication reads the rulebook; only Legislate writes it | H-control-plane | VC-04 | 125 |
| **A4** Risk acceptance at exhaustion | Only the risk owner accepts risk, and only last | G-riskowner, S-acknowledgement | VC-06 | 425 |
| **A5** Write postcondition | The full rationale trail is written at resolution | every admitted case | VC-07, VC-15 | 750 |
| **A6** Non-overridable short-circuit | Absolute rules always win; no precedent softens them | F-absolute, Y-adversarial (absolute probes) | VC-08 | 334 |
| **A7** Sunset, referral, renewal | A waiver becomes law, runs out, or renews in plain sight | G-riskowner, I-lapsed, U-renewal, S-acknowledgement | VC-09, VC-10, VC-14 | 570 |
| **A8** Bindingness | A precedent is a constraint, not a hint | C-precedent, D-ordering, M-supersession, X-coldstart, Z-inexpressibility, P-pressure | VC-11 | 1,039 |
| **A9** Standing declaration | One-sidedness is a disclosed fact, and so is whether standing was exercised | N-standing | VC-17, VC-26 | 120 |

**What is not covered.** A1 and A2 are exercised by carrying their consequences on every record, not by attempting to violate them: a corpus of cases cannot construct an authority holding two branches, because that is an access-control fact about a deployment. An adopter must check A1 and A2 against their own credential issuance — in a fab that means the export-licensing office, the systems architecture board and the COO holding genuinely separate credentials. The mutation matrix compensates from the other side (inverting the authority key and removing the admission bar are both caught), but the honest statement is that role disjointness is *assumed* here and *enforced* by a deployment.

---

## 2. Requirements spine → what the corpus can and cannot show

| Req | Statement | What the corpus shows | Cases |
| :---- | :---- | :---- | ----: |
| **R1** | Exception authority named and role-keyed | **Shown by construction.** Every record carries `auth_class` and `auth_id`; VC-07 confirms none is missing either. This is also the EAR's own requirement — §762.5(b)(4) wants to know *who* made a change and *when*. | 5,000 |
| **R2** | Rationale recorded at decision time, in full | **Shown by construction.** VC-07 is Theorem 2's rebuild check over all 935 records. The domain is the admitted set and nothing wider: the 4,197 cases nobody contested leave nothing to read, and nothing is claimed about them. | 750 |
| **R3** | Comparable priors retrievable | **Availability shown; quality not.** Retrieval and the gate run on 3,542 cases. Nothing here says the retrieval is *good* — only that a record the gate would admit is never lost at retrieval (control S3 measures exactly that). | 3,542 |
| **R4** | Retrieved decisions bind, with a contest path | **Shown.** 1,039 cases are bound; VC-11 confirms each is consistent with its controlling record's holding. The ladder is exercised at J2, J3 and the risk owner. | 1,039 |
| **R5** | Enforced lifecycle | **Shown.** Every acceptance carries an expiry and a referral (VC-09); lapsed records are excluded at retrieval (VC-10); renewal is permitted only while a referral is pending and barred after rejection (VC-14). There is no fourth path. | 570 |
| **R6** | Separation of authorship, adjudication, risk acceptance | **Assumed by the corpus, enforced by a deployment.** See the note under A1. | 5,000 |
| **R7** | Deep-reasoning cost scales with contest, not volume | **Not shown, and cannot be.** First-instance adjudication runs on all 5,000 arrivals. What is contest-bounded is storage — 750 records from 803 contested cases — and human decisions: 425 acceptances against 5,000 arrivals. The corpus reports those terms; it does not vindicate the requirement. | 803 |

---

## 3. Risk architecture → provision families → cases

Mapping to *Security, Quality, and Risk Architecture for Semiconductor Supply Chain Software*.

| Risk architecture section | Provision family | Provisions | Cases |
| :---- | :---- | ----: | ----: |
| 2. Software supply chain security — dependency confusion, SBOM drift, SLSA, agent code provenance | SS | 11 | 784 |
| 3. Memory and concurrency safety | TQ | 7 | 268 |
| 3. Agent hallucination and logic drift | AG | 8 | 379 |
| 3. Input sanitisation and fuzzing | AS | 7 | 353 |
| 3. Cryptographic standards | CR | 6 | 221 |
| 4. SECS/GEM protocol integrity | SG | 10 | 663 |
| 4. Real-time latency constraints | RT | 7 | 448 |
| 4. WIP data immutability | WI | 7 | 361 |
| 4. Recipe protection and IP leakage | RP | 7 | 330 |
| 5. Export control compliance (EAR/ITAR) | EX | 13 | 642 |
| 5. Data sovereignty and localisation | DS | 7 | 421 |
| 5. CHIPS Act and NIST SP 800-53 / 800-161 | NC | 6 | 127 |
| 7. Policy-as-code for immutable guardrails | GV | 7 | 231 |

### Where this corpus departs from the risk architecture's blueprint

The document proposes a 2,000-case suite in five sequential gates: 800+ SAST and unit, 200+ SCA and SBOM, 500+ domain and integration, 300+ policy-as-code and regulatory simulation, 200+ agent-specific defensive testing.

Those gates are **where a test runs in the pipeline**. This corpus's categories are **which institutional mechanism a case exercises**. A single SemiFab case may correspond to a SAST finding, an SBOM check and a Rego evaluation all at once — the corpus does not care, because what it tests is what the *judiciary* does with the objection those gates raise.

The two are complementary and an adopter needs both:

- The five gates answer *did the gate fire correctly?*
- This corpus answers *when the gate fired and someone wanted to ship anyway — for the ramp, the qualification lot, the vendor engineer who is on site only today — was the decision made once, recorded completely, and made to bind the next materially identical case?*

The document's own §7 sets out the ambition precisely: policy-as-code that rejects a violating merge "with zero human intervention required." That is the right posture for the twenty absolute provisions, and this corpus tests it as A6 — 334 short-circuits with zero retrievals and zero records. But it is the wrong posture for the other eighty-three, because most compliance objections in a fab are not violations of a floor; they are judgments about a floor's edge. Those need an institution, and §7's Rego gate has nowhere to put one. That gap is what the remaining twenty-four categories test.

---

## 4. Category → mechanism → provenance in the theory

| Category | Mechanism | Where it comes from |
| :---- | :---- | :---- |
| A-routine, B-plain-deny | base rule evaluation; the charged population | Ch. 5 §4.4 (the Evaluator and the Prosecutor) |
| C-precedent | retrieval, gate, ordering, bindingness | Ch. 5 §4.6; A8 |
| D-ordering | the lexicographic keys ⟨auth_class, ts, scope, depth⟩ | Ch. 5 §4.6 |
| E-distinguish | `distinguish(r,c)` ⟺ premise(r) ⊄ facts(c) | Ch. 5 §4.6; Horty 2011 |
| F-absolute | A6, conditioned on engagement **and** violation | Ch. 5 §4.7 |
| G-riskowner | Accept_risk; the codomain is a sum type | Ch. 5 Definition 5; A4 |
| H-control-plane | the DraftAmendment channel | Ch. 5 A3 |
| I-lapsed, U-renewal | expiry, lapse, renewal-while-pending, bar-after-rejection | Ch. 5 §4.8; A7 |
| J-novel | Controlling = none; fresh interpretation, flagged | Ch. 5 §4.6 |
| K-tie | `none(tie)` as a distinct value; referral of the unbroken conflict | Ch. 5 §4.6 |
| L-consolidated | Definition 7 clause (ii); signature and class | Ch. 5 Definitions 15, 16 |
| M-supersession | recency conditioned on express supersession | Ch. 5 §4.6 |
| N-standing | the declaration and the realised adverse-contest rate | Ch. 5 A9, both limbs |
| P-pressure | non-predicated factors do not move dispositions | Ch. 5 §7.6 |
| Q-docket | the Docket, declined and ⊥ routes | Ch. 5 Definition 14 |
| R-reporter | observer non-influence | Ch. 5 Definition 17, §4.12.1 |
| S-acknowledgement | adopt / reject / defer / decline-to-act | Ch. 5 Definition 18 |
| T-audit-register | annotation that resolve never reads | Ch. 5 Definition 19 |
| V-likecase | consistency as the primary endpoint | Ch. 6 §3.3 |
| W-crossjurisdiction | federated jurisprudence under heterogeneous constitutions | Ch. 7 §7.5(4) |
| X-coldstart | seeded jurisprudence and its neutrality cost | Ch. 4 admission theory |
| Y-adversarial | strategic framing, store poisoning, injection | Ch. 7 §7.5(3) |
| Z-inexpressibility | B_gov and B_mem cannot express precedential control | Ch. 5 §6, Theorems 3–4, Proposition 3 |

### Two categories that land differently in this domain

**W-crossjurisdiction is sharper here than in a clinic.** In VetPOC the cross-jurisdiction cases turn on whether a state permits a telehealth-established VCPR — a genuine conflict, but one a practice can resolve by not operating in that state. In a fab the same technical data is released toward destinations the constitution treats differently, and a multi-site group cannot avoid the question: the identical artifact, the identical change, is compliant toward one destination and a violation toward another. That is the authority-scope problem the CI/CD setting never posed sharply, and it is why federated jurisprudence under heterogeneous constitutions sits on the future-work list rather than in the contract.

**Y-adversarial has a named legal counterpart here.** 15 CFR 764.2(h) reaches any action taken to evade the regulations, which means the strategic-framing adversary is not merely a research concern in this domain — reframing a case to dodge a gate is itself a violation. SF-EX-005 entrenches that as an absolute provision, so the adversarial probes in this pack test something the constitution has an answer to, rather than only testing whether the mechanism holds.
