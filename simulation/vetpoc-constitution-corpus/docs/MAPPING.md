# Mapping: corpus → theory → risk framework

Three mappings, so that a reader can go from any one of the three vocabularies to the other two: the nine axioms of the architectural contract, the seven requirements of the programme's requirements spine, and the areas of the veterinary security, quality and supply-chain risk framework.

---

## 1. Axioms → categories → checks

| Axiom | What it says | Categories that exercise it | Checks | Cases |
| :---- | :---- | :---- | :---- | ----: |
| **A1** Role disjointness | The three authority classes are pairwise disjoint | every category (the authority fields are carried on every record) | VC-07 | 5,000 |
| **A2** Distinct output types | A rule change, a decision and a sign-off can never be confused | every category | VC-04 | 5,000 |
| **A3** No direct mutation | Adjudication reads the rulebook; only Legislate writes it | H-control-plane | VC-04 | 125 |
| **A4** Risk acceptance at exhaustion | Only the risk owner accepts risk, and only last | G-riskowner, S-acknowledgement | VC-06 | 428 |
| **A5** Write postcondition | The full rationale trail is written at resolution | every admitted case | VC-07, VC-15 | 761 |
| **A6** Non-overridable short-circuit | Absolute rules always win; no precedent softens them | F-absolute, Y-adversarial (absolute probes) | VC-08 | 341 |
| **A7** Sunset, referral, renewal | A waiver becomes law, runs out, or renews in plain sight | G-riskowner, I-lapsed, U-renewal, S-acknowledgement | VC-09, VC-10, VC-14 | 575 |
| **A8** Bindingness | A precedent is a constraint, not a hint | C-precedent, D-ordering, M-supersession, X-coldstart, Z-inexpressibility | VC-11 | 1,031 |
| **A9** Standing declaration | One-sidedness is a disclosed fact, and so is whether standing was exercised | N-standing | VC-17, VC-26 | 120 |

**What is not covered.** The corpus exercises A1 and A2 by carrying their consequences on every record, not by attempting to violate them: a corpus of cases cannot construct an authority holding two branches, because that is an access-control fact about a deployment rather than a property of a case. An adopter must check A1 and A2 against their own credential issuance. The mutation matrix compensates in the other direction — inverting the authority key (M1) and removing the admission bar (M4) are caught — but the honest statement is that role disjointness is *assumed* by this corpus and *enforced* by a deployment.

---

## 2. Requirements spine → what the corpus can and cannot show

The seven requirements are the joint of the four-paper programme. Column three states, without softening, what this corpus establishes about each.

| Req | Statement | What the corpus shows | Cases |
| :---- | :---- | :---- | ----: |
| **R1** | Exception authority named and role-keyed | **Shown by construction.** Every record carries `auth_class` and `auth_id`; VC-07 confirms no record is missing either. | 5,000 |
| **R2** | Rationale recorded at decision time, in full | **Shown by construction.** VC-07 is Theorem 2's rebuild check over all 943 records. The domain is the admitted set and nothing wider — the 4,191 cases that were never contested leave nothing to read, and nothing is claimed about them. | 761 |
| **R3** | Comparable priors retrievable | **Availability shown; quality not.** Retrieval and the gate run on 3,563 cases. The two judgment functions are fixed at their types only, so nothing here says the retrieval is *good* — only that the record the gate would admit is never lost at retrieval (control S3 measures exactly this). | 3,563 |
| **R4** | Retrieved decisions bind, with a contest path | **Shown.** 1,031 cases are bound; VC-11 confirms each is consistent with its controlling record's holding. The contest path is exercised at three rungs and at the risk owner. | 1,031 |
| **R5** | Enforced lifecycle | **Shown.** Every acceptance carries an expiry and a referral (VC-09); lapsed records are excluded at retrieval (VC-10); renewal is permitted only while a referral is pending and barred after rejection (VC-14). There is no fourth path. | 575 |
| **R6** | Separation of authorship, adjudication, risk acceptance | **Assumed by the corpus, enforced by a deployment.** See the note under A1 above. | 5,000 |
| **R7** | Deep-reasoning cost scales with contest, not volume | **Not shown, and cannot be.** First-instance adjudication runs on all 5,000 arrivals. What is contest-bounded is storage — 761 records from 809 contested cases — and human decisions: 428 acceptances against 5,000 arrivals. Those are the terms the claim is true of. The corpus reports them; it does not vindicate the requirement. | 809 |

---

## 3. Risk framework → provision families → cases

Mapping to *Comprehensive Security, Quality, and Supply Chain Risk Framework for Veterinary Software Development*.

| Risk framework section | Provision family | Provisions | Cases |
| :---- | :---- | ----: | ----: |
| 2.1 Point-of-Care diagnostics and IoT integrations | PO | 10 | 666 |
| 2.2 Controlled substance management and e-prescribing (EPCS) | CS | 12 | 437 |
| 2.2 (clinical floor) VCPR, extralabel use, residues | VC | 8 | 535 |
| 2.3 Patient data privacy (PII and PCI) | PD | 9 | 509 |
| 2.3 Role-based access control; 5.1 IDOR | RB | 8 | 488 |
| 3. Software supply chain and pipeline integrity | SC | 9 | 739 |
| 4. Securing AI-agent generated code | AI | 8 | 364 |
| 5.1 OWASP and defensive coding | AS | 9 | 475 |
| 5.2 High availability and concurrency for ER operations | HA | 6 | 190 |
| Records, audit trail, immutability | RR | 7 | 441 |
| Animal welfare, practice acts, scope of practice | AW | 5 | 126 |
| Constitutional meta-provisions | GV | 7 | 255 |

*(Counts are per engaged provision and are regenerated into `docs/COVERAGE.md` on every build; the table above is a snapshot.)*

### Where this corpus departs from the risk framework's blueprint

The risk framework proposes a 2,000-case suite distributed across a testing pyramid: ~1,200 unit, ~400 integration, ~200 security, ~100 policy-as-code, ~100 end-to-end. This corpus is not that suite, and the difference is worth stating plainly.

The pyramid's layers are **where a test runs**. This corpus's categories are **which institutional mechanism a case exercises**. A single VetPOC case may correspond to a unit test of a dosage calculation, an integration test of an HL7 parse, and a policy-as-code evaluation of the resulting PR — the corpus does not care, because what it tests is what the *judiciary* does with the objection those tests raise.

The two are complementary, and an adopter needs both:

- The pyramid answers *did the gate fire correctly?*
- This corpus answers *when the gate fired and someone wanted to proceed anyway, was the decision made once, recorded completely, and made to bind the next materially identical case?*

Detection tooling is a crowded, well-funded field. The second question is the one nothing currently answers.

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
| P-pressure | non-predicated factors do not move dispositions | Ch. 5 §7.6 (the pressure category) |
| Q-docket | the Docket, declined and ⊥ routes | Ch. 5 Definition 14 |
| R-reporter | observer non-influence | Ch. 5 Definition 17, §4.12.1 |
| S-acknowledgement | adopt / reject / defer / decline-to-act | Ch. 5 Definition 18 |
| T-audit-register | annotation that resolve never reads | Ch. 5 Definition 19 |
| V-likecase | consistency as the primary endpoint | Ch. 6 §3.3 |
| W-crossjurisdiction | federated jurisprudence under heterogeneous constitutions | Ch. 7 §7.4, §7.5(4) |
| X-coldstart | seeded jurisprudence and its neutrality cost | Ch. 7 §7.4; Ch. 4 admission theory |
| Y-adversarial | strategic framing, store poisoning, injection | Ch. 7 §7.5(3) |
| Z-inexpressibility | B_gov and B_mem cannot express precedential control | Ch. 5 §6, Theorems 3–4, Proposition 3 |
