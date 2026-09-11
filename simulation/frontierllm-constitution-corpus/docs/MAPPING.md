# Mapping: corpus → theory → risk architecture

Three mappings, so a reader can move between the three vocabularies: the nine axioms of the architectural contract, the seven requirements of the programme's requirements spine, and the sections of *Comprehensive Risk, Security, and Supply Chain Architecture for Frontier LLM Systems*.

---

## 1. Axioms → categories → checks

| Axiom | What it says | Categories that exercise it | Checks | Cases |
| :---- | :---- | :---- | :---- | ----: |
| **A1** Role disjointness | The three authority classes are pairwise disjoint | every category | VC-07 | 5,000 |
| **A2** Distinct output types | A rule change, a decision and a sign-off can never be confused | every category | VC-04 | 5,000 |
| **A3** No direct mutation | Adjudication reads the rulebook; only Legislate writes it | H-control-plane | VC-04 | 125 |
| **A4** Risk acceptance at exhaustion | Only the risk owner accepts risk, and only last | G-riskowner, S-acknowledgement | VC-06 | 417 |
| **A5** Write postcondition | The full rationale trail is written at resolution | every admitted case | VC-07, VC-15 | 743 |
| **A6** Non-overridable short-circuit | Absolute rules always win; no precedent softens them | F-absolute, Y-adversarial (absolute probes) | VC-08 | 335 |
| **A7** Sunset, referral, renewal | A waiver becomes law, runs out, or renews in plain sight | G-riskowner, I-lapsed, U-renewal, S-acknowledgement | VC-09, VC-10, VC-14 | 562 |
| **A8** Bindingness | A precedent is a constraint, not a hint | C-precedent, D-ordering, M-supersession, X-coldstart, Z-inexpressibility, P-pressure | VC-11 | 1,022 |
| **A9** Standing declaration | One-sidedness is a disclosed fact, and so is whether standing was exercised | N-standing | VC-17, VC-26 | 120 |

**What is not covered.** A1 and A2 are exercised by carrying their consequences on every record, not by attempting to violate them: a corpus of cases cannot construct an authority holding two branches, because that is an access-control fact about a deployment. In a frontier lab that means the responsible-scaling council, the adjudicating pipeline and the chief scientist holding genuinely separate credentials — and it is worth naming that this is the separation most often collapsed in practice, because the same small group of senior people tends to write the framework, run the evaluation and sign the release.

**One check does more here than in the sibling packs.** VC-04 additionally asserts that no provision whose status is `deferred` or `advisory` is marked absolute. See `docs/CROSS_PACK.md` for why that clause exists and why the check count stayed at 26.

---

## 2. Requirements spine → what the corpus can and cannot show

| Req | Statement | What the corpus shows | Cases |
| :---- | :---- | :---- | ----: |
| **R1** | Exception authority named and role-keyed | **Shown by construction.** Every record carries `auth_class` and `auth_id`; VC-07 confirms none is missing either. | 5,000 |
| **R2** | Rationale recorded at decision time, in full | **Shown by construction.** VC-07 is Theorem 2's rebuild check over all 936 records. The domain is the admitted set: the 4,211 cases nobody contested leave nothing to read, and nothing is claimed about them. | 743 |
| **R3** | Comparable priors retrievable | **Availability shown; quality not.** Retrieval and the gate run on 3,567 cases. Nothing here says the retrieval is *good* — only that a record the gate would admit is never lost at retrieval. | 3,567 |
| **R4** | Retrieved decisions bind, with a contest path | **Shown.** 1,022 cases are bound; VC-11 confirms each is consistent with its controlling record's holding. | 1,022 |
| **R5** | Enforced lifecycle | **Shown.** Every acceptance carries an expiry and a referral (VC-09); lapsed records are excluded at retrieval (VC-10); renewal is permitted only while a referral is pending and barred after rejection (VC-14). | 562 |
| **R6** | Separation of authorship, adjudication, risk acceptance | **Assumed by the corpus, enforced by a deployment.** | 5,000 |
| **R7** | Deep-reasoning cost scales with contest, not volume | **Not shown, and cannot be.** First-instance adjudication runs on all 5,000 arrivals. Contest-bounded terms: storage — 743 records from 789 contested cases — and human decisions, 417 acceptances against 5,000 arrivals. | 789 |

---

## 3. Risk architecture → provision families → cases

Mapping to *Comprehensive Risk, Security, and Supply Chain Architecture for Frontier LLM Systems*.

| Risk architecture section | Provision family | Provisions | Absolute | Cases |
| :---- | :---- | ----: | ----: | ----: |
| 1.1 SBOM, MBOM and PBOM; model hash approval | MB | 9 | 3 | 424 |
| 1.1 Dependency and provenance management; SLSA | SC | 8 | 1 | 402 |
| 1.2 Human versus agent-authored code verification | AG | 8 | 3 | 361 |
| 2. Security: injection, poisoning, inversion, output handling | LS | 11 | 2 | 379 |
| 2. Traditional AppSec on the serving and tooling surface | AS | 6 | 0 | 223 |
| 3.1 Probabilistic testing and model drift | EV | 10 | 2 | 470 |
| 3.2 Resource and infrastructure checks | IN | 8 | 0 | 313 |
| 4.2 Privacy — GDPR/CCPA data sanitisation | PI | 7 | 1 | 417 |
| 4.2 Sovereign boundaries and training-data provenance | TD | 8 | 1 | 593 |
| 4.2 Copyright and IP contamination | IP | 6 | 1 | 140 |
| 5.1 Financial guardrails | FG | 6 | 1 | 255 |
| 5.2 Reputational and brand safety guardrails | BS | 6 | 1 | 260 |
| 7. Shift-left AI regulation; hard blocks; frontier safety | SF | 9 | 3 | 428 |
| 4.1 Policy-as-code; governance of the judiciary itself | GV | 11 | 3 | 557 |

### Where this corpus departs from the architecture's blueprint

The document proposes a 2,000-case matrix in four parallel domains: ~500 static code and policy analysis, ~800 deterministic unit tests, ~400 probabilistic model evaluation, ~300+ adversarial and red-team scenarios.

Those four are **what a test executes against** — source, code paths, model outputs, adversarial inputs. This corpus's categories are **which institutional mechanism a case exercises**. A single FrontierLLM case may correspond to a Rego evaluation, a unit test and a probabilistic eval all at once; the corpus does not care, because what it tests is what the *judiciary* does with the objection those tests raise.

The two are complementary and a lab needs both:

- The four domains answer *did the gate fire correctly?*
- This corpus answers *when the gate fired and someone wanted to ship anyway — launch announced, compute reservation expiring, an executive asking before the review board meets — was the decision made once, recorded completely, and made to bind the next materially identical case?*

**§4.1 and §7 are where the document reaches for this corpus's subject and stops one step short.** §4.1 says every PR must be evaluated "against a codified precedent base representing legal and corporate risk definitions", and that "the admission rule for any code into the mainline is binary compliance with these automated policies." Two of those words are load-bearing and are used differently here.

- A **precedent base** in the document is a policy file: a set of Rego rules, authored centrally, applied uniformly. In the Digital Judiciary a precedent base is a store of *adjudicated decisions with their reasons*, which accumulates from contested cases and binds later ones. The difference is not terminological. A policy file cannot answer "what did we decide last time, and why"; §6 of Chapter 5 proves that a stateless evaluator plus a log has no relation that binds, so `Controlling(c)` has no referent in it. The 150 Z-inexpressibility cases in this corpus are exactly the cases that separate the two.
- An **admission rule** in the document is the merge gate. In Chapter 4 it is the procedural predicate deciding which adjudicated decisions become *citable*. Using the same phrase for both is a live source of confusion in this domain, and this corpus keeps them apart: the merge gate is the Prosecutor's charging decision plus A6, and the admission rule is Definition 7.

**§7's "precedent base evolution" is the right instinct with no mechanism under it.** The document says new rules are added "without requiring manual pipeline reconfiguration". That describes legislation — the slow, reviewed path — and says nothing about the fast path, which is what actually happens when a novel case arrives on a Friday. This corpus supplies the missing half: 480 C-precedent cases where a prior decision binds, 250 E-distinguish cases where a superficially similar one does not, 150 M-supersession cases where a newer holding either names what it departs from or fails to, and 40 K-tie cases where two holdings deadlock and the conflict is referred back to the legislators rather than silently resolved.

**One genuine tension the document creates, and this corpus makes visible.** §7 divides everything into hard blocks and soft warnings, with soft warnings "requiring executive override". That is a two-state world: a rule either cannot be waived or is waived by whoever is senior enough. The G-riskowner category tests what the third state costs — 250 cases in which escalation is exhausted, a named risk owner accepts residual risk, and the acceptance carries a mandatory expiry and a referral back to the legislature. All 417 acceptances across the corpus expire; none becomes permanent by inattention (VC-09, VC-10, VC-14). An executive override with no expiry is how a soft warning becomes, in practice, a repealed rule.

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

### Three categories that land differently in this domain

**W-crossjurisdiction is arithmetic here, and that makes it sharper.** In the veterinary pack it turns on whether a state accepts a telehealth-established VCPR; in the semiconductor pack, on a destination's export posture. Here it is a single number: a training run at 4×10²⁵ FLOP crosses the EU AI Act's Article 51(2) presumption for a general-purpose model with systemic risk and does *not* cross California SB 53's 10²⁶ frontier-developer threshold. The same run, one number, two answers. FL-GV-004 requires the determination to be recorded per jurisdiction, and the violating factor is `compute_threshold_determination_conflates_jurisdictions` — because a single "are we above the threshold" boolean is not a simplification, it is a loss of the fact that the two regimes ask different questions.

**Y-adversarial has a native attack surface here that the other packs do not have.** Store poisoning in a fab is hypothetical. In a lab whose pipeline reads issue text, retrieved documents and tool output into an agent's context, injection on the judicial path is the same class of attack the product is built to resist. FL-AG-008 and FL-LS-003 are the provisions, and the corpus's own R-reporter category tests the structurally identical property from the other side: the observer that reports on the store must not be on the input path of the thing it observes.

**Z-inexpressibility is the category this domain most needs.** Every one of the 150 cases is disposed of by citation at first instance with no human in the loop. Under the governed exception baseline of Chapter 5 Definition 12 — which is what §4.1's Rego gate is — each becomes an exception ticket for a named approver, because nothing in that baseline binds. Under the advisory baseline of Definition 13 — retrieval-augmented policy lookup, which is where a lot of current tooling is heading — the same record is retrieved and shown to the approver, and still nothing binds. Proposition 3 is the result: there is no fact of precedential control for a selector to compute. That is a claim about representations, not about retrieval quality, and it is why "add RAG to the policy engine" does not reach the property.
