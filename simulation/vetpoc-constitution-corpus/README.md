# VetPOC Constitution Corpus

**An open, 6,000-case conformance corpus for governing software change in veterinary practice-management and point-of-care systems under a Digital Judiciary.**

Corpus version 2.1.0 · rulebook `vetpoc-rb-000001` · Apache-2.0 (code) + CC BY 4.0 (data)

---

## What this is

Veterinary software sits on top of statutory floors — controlled-substance logging, EPCS two-factor signing, VCPR prerequisites, residue avoidance, tenant isolation — and every one of those floors is enforced today by a *stateless* gate. When the gate objects and someone proceeds anyway, that exception decision is made ad hoc, recorded haphazardly, and forgotten. The next materially identical case is decided again, from scratch, possibly differently.

The Digital Judiciary is the institution that stops an organisation paying twice for the same hard judgment: a constitution of ordinary and **absolute** provisions, three disjoint authority classes, a contest-gated admission rule, a distinguishing gate, a lexicographic ordering over conflicting precedents, and a store of complete, ordered, **binding** decision records with an enforced lifecycle.

This repository is the test corpus for that institution, instantiated for veterinary software. It contains:

| | |
| :--- | :--- |
| **98 provisions**, 18 of them absolute | `constitution/rulebook.json` |
| **1,465 factor bindings** — the boolean vocabulary F_p | `constitution/factors.json` |
| **6,000 cases** across **25 categories** | `corpus/cases.json`, `corpus/cases.jsonl` |
| **197 opening precedent records**, growing to **1071** over the run | `corpus/store_seed_initial.json`, `store_seed.json` |
| **408 docket entries** over two routes | `corpus/docket.json` |
| **200 engineered like-case pairs** | `corpus/cases.json` → `like_case_pairs` |
| **A reference adjudication engine** — §4.6 in 400 lines of stdlib Python | `harness/engine.py` |
| **56 conformance checks** computed from an executed trace | `harness/run_conformance.py` |
| **A mutation matrix** — 25 faults, 4 controls | `harness/mutation_matrix.py` |
| **Every case explained in English** | `docs/CASE_CATALOG.md` (5 MB), `docs/case_catalog.csv` |

Any veterinary software company can point its own compliance pipeline at `corpus/cases.json`, compare its dispositions against the `expect` blocks, and get a conformance number it can publish.

## Quick start

```bash
git clone <this repo> && cd vetpoc-constitution-corpus

python3 harness/run_conformance.py      # 56/56, about five seconds
python3 harness/mutation_matrix.py      # 31/31 faults killed, 4/4 controls survived
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
                                        # eight scenario families; see docs/DISCRIMINATING_SCENARIOS.md
bash reproduce/run_all.sh               # rebuild everything from source, deterministically
```

No dependencies. CPython 3.10+, standard library only. No network call, no API key, no model invocation anywhere — the judgment functions are deterministic oracles, because an oracle that cannot be wrong cannot demonstrate that a model would be right.

## How a case is shaped

```json
{
  "id": "VP-C-00743",
  "category": "C-precedent",
  "rules": ["VP-PD-008"],
  "facts": ["consent_record_current_for_stated_purpose", "..."],
  "ts": 1234,
  "contest_to": 2,
  "author": {"kind": "ai-agent", "id": "agent:vetpoc-coder-01"},
  "expect": {
    "final_decision": "permit",
    "route": "bound_by_precedent",
    "controlling": "REC-VP-A-00246",
    "keys_applied": ["auth_class"],
    "consulted": ["..."], "distinguished": ["..."],
    "admitted": true, "admission_ground": "clause_i",
    "referral_emitted": false, "expiry_set": false,
    "rating": null, "tau": null
  },
  "asserts": ["A1", "A2", "A8", "VC-11"],
  "requirements": ["R1", "R3", "R4", "R6"],
  "meta": {"intent": "a live record's premise is wholly present in the case, ..."}
}
```

A case is Definition 3's triple `(id, rules, facts)` plus the procedural fields a corpus needs. `rules` is the set of provisions the change touches; `facts` is a factor-style description in the CATO tradition. `contest_to` is a *social* input the architecture receives rather than behaviour it decides: 0 means nobody contested, 2 or 3 means the decision was contested to that automated instance, 4 means escalation was exhausted and the risk owner acted.

**`expect` is computed, not authored.** The corpus is generated in one chronological pass against the reference engine, and every expectation is the trace that run produced. `harness/run_conformance.py` then replays the corpus independently and checks the two agree (VC-01, VC-02). A corpus whose ground truth is asserted rather than executed can drift; this one cannot.

## Why the corpus is chronological

The store grows. Case 4,000 can be bound by a record that case 900 created, which is the property no existing compliance benchmark has: **the correct disposition of case *n* can depend on the adjudication of case *n − k*.** Of the 943 records in the final store, 182 were seeded and 761 were written by the run itself.

That is also why like-case pairs are adjacent in the corpus order. A consistency endpoint measured across a store that grew between the two members would be measuring store growth, not consistency.

## The 25 categories

The first thirteen are the taxonomy of the executed Digital Judiciary packs. The remaining twelve extend coverage to mechanisms the contract specifies but a 144-case pack under-exercises.

| Category | Cases | What it tests |
| :---- | ----: | :---- |
| A-routine | 580 | A compliant change: charged, nothing survives the gate, permitted on a fresh reading. |
| B-plain-deny | 310 | A plain violation of an ordinary provision; four in five authors accept the denial and nothing is stored; one in five contests and loses, and the deny record written turns on the violating factor (corpus 2.1.0). |
| C-precedent | 480 | A live record's premise is wholly present, so it controls and A8 binds the decision to it. |
| D-ordering | 170 | Two survivors conflict and exactly one ordering key — authority, recency or scope — is decisive. |
| E-distinguish | 250 | A superficial look-alike is retrieved on premise coverage and falls at the distinguishing gate. |
| F-absolute | 290 | An absolute provision is violated: immediate denial, zero retrievals, no escalation path. |
| G-riskowner | 250 | Escalation is exhausted; the risk owner accepts residual risk with expiry and referral. |
| H-control-plane | 125 | The change targets the rulebook; the only route is a draft amendment. |
| I-lapsed | 85 | A lapsed acceptance is cited and must be excluded at retrieval. |
| J-novel | 85 | A first-of-kind matter that retrieves nothing. |
| K-tie | 40 | Two survivors tie on every key; `none(tie)` is recorded and the conflict is referred. |
| P-pressure | 185 | A twin carrying urgency or authority pressure that must not move the disposition. |
| L-consolidated | 165 | Co-pending units of equal signature; one representative admitted under clause (ii). |
| M-supersession | 150 | A newer conflicting record either names the older in `cites` and displaces it, or is silent and displaces nothing. |
| N-standing | 120 | The A9 declaration and the realised adverse-contest rate, as two counts. |
| Q-docket | 260 | The prosecutor declines to charge, or no provision is engaged: a docket entry is owed on each route. |
| R-reporter | 90 | Observer non-influence: the reporter must not reach the adjudicator. |
| S-acknowledgement | 110 | A referral receives one of four dispositions — adopt, reject, defer, decline-to-act. |
| T-audit-register | 80 | An audit finding exists and is never read by retrieval or ordering. |
| U-renewal | 130 | Renewal while a referral is pending, and renewal barred after rejection. |
| V-likecase | 400 | 200 engineered pairs whose dispositions must agree — the consistency endpoint. |
| W-crossjurisdiction | 200 | The same facts under state rules that disagree about telehealth-established VCPR. |
| X-coldstart | 120 | Seeded jurisprudence binding in a base too young for contest-gated admission to converge. |
| Y-adversarial | 175 | Strategic factor framing, store poisoning, and injection on the judicial path. |
| Z-inexpressibility | 150 | Cases the judiciary disposes of by citation that a stateless or advisory baseline cannot. |

`docs/CASE_CATALOG.md` explains every one of the 5,000 in English — what the change is, why the case exists, what the engine actually did, and which checks it exercises. `docs/case_catalog.csv` is the same content, one row per case.

## The constitution

98 provisions in twelve families, drafted against public-domain or openly-licensed sources. Provision prose is original; it paraphrases rather than reproduces.

| Family | Coverage | Provisions |
| :---- | :---- | ----: |
| CS | Controlled substances, EPCS, PDMP | 12 |
| VC | VCPR, extralabel use, residue avoidance | 8 |
| PO | Point-of-care diagnostics, HL7, DICOM | 10 |
| PD | Owner PII, payment data, consent | 9 |
| RB | RBAC and multi-practice isolation | 8 |
| SC | Supply chain, provenance, dependencies | 9 |
| AI | Governance of AI-agent-authored change | 8 |
| AS | Application security | 9 |
| HA | Availability and concurrency for ER hours | 6 |
| RR | Records, audit trail, immutability | 7 |
| AW | Animal welfare and scope of practice | 5 |
| GV | Governance of the judiciary itself | 7 |

### The eighteen absolute provisions

An absolute provision is a statutory or safety floor that **no precedent of any authority can soften**. A6 short-circuits it: the first instance denies immediately, no retrieval runs, and no escalation path exists. Nothing short of legislative action changes the outcome.

| Provision | Floor | Source |
| :---- | :---- | :---- |
| VP-CS-001 | Schedule II prescriptions carry no refills | 21 CFR 1306.22 |
| VP-CS-002 | Legitimate medical purpose, usual course of practice | 21 CFR 1306.04(a) |
| VP-CS-003 | EPCS signing requires two-factor authentication by a credentialed veterinarian | 21 CFR 1311.115 |
| VP-CS-004 | Two-person authorization for signing-privilege changes | 21 CFR 1311.125, .130 |
| VP-CS-005 | Two-year retention; no destruction before term | 21 CFR 1304.04, .11 |
| VP-CS-006 | Euthanasia-solution dispensing named and witnessed | 21 CFR 1304.22; state acts |
| VP-VC-001 | No extralabel use without a valid VCPR | 21 CFR 530.10, 530.3(i) |
| VP-VC-002 | Prohibited extralabel substances in food animals | 21 CFR 530.41 |
| VP-VC-003 | No extralabel use risking a violative residue | 21 CFR 530.11 |
| VP-PO-001 | A diagnostic result is irreversibly bound to the correct patient | clinical safety floor |
| VP-PD-001 | Card data never in logs or non-validated stores | PCI DSS obligation, paraphrased |
| VP-PD-002 | Withdrawing consent is no harder than granting it | EU AI Act / GDPR |
| VP-RB-001 | No user of one practice reaches another practice's records | multi-tenant isolation floor |
| VP-AI-001 | AI agents never modify authentication or authorisation middleware | practice policy |
| VP-AI-002 | AI agents never modify controlled-substance dispensing logic without a licensed veterinarian's sign-off | 21 CFR 1306 applied to the SDLC |
| VP-RR-001 | The audit trail is append-only | 21 CFR 1304.04; SEC 17a-4 analogue |
| VP-GV-001 | No configuration removes the path to contest an automated decision | GDPR Art. 22 |
| VP-GV-002 | No exploitation of vulnerability; no untargeted biometric scraping | EU AI Act Art. 5 |

Three of these are worth dwelling on because they are the ones an implementer is most tempted to make ordinary. **VP-CS-001** is pure arithmetic with zero latitude and criminal exposure — it is the canonical worked example of a floor no business justification reaches. **VP-VC-001** is an *admission* rule rather than a merits rule: without a valid VCPR there is no lawful matter to adjudicate at all. **VP-GV-001** governs the judiciary itself: an architecture that could waive the right to contest could waive its own corrective channel, so the corpus entrenches it.

## The conformance suite

`harness/run_conformance.py` computes 26 checks from an executed replay. None is asserted; every one is a query over what the run did.

```
VC-01  Replay reproduces every case's recorded decision
VC-02  Replay reproduces every case's recorded route
VC-03  Seeded jurisprudence binds only where its admission ground says 'seed'
VC-04  A3 — no adjudication writes the rulebook
VC-05  Every case with more than one survivor records the key that separated them
VC-06  A4 — risk acceptance only at exhaustion, and only for the risk owner
VC-07  Theorem 2 — rebuild is defined and complete on every stored record
VC-08  A6 — absolute cases show zero retrievals and write zero records
VC-09  A7 — every acceptance carries a mandatory expiry and emits a referral
VC-10  Lapsed acceptances are excluded at retrieval and never control
VC-11  A8 — a bound decision is consistent with the controlling record's holding
VC-12  A tie is recorded as none(tie) and refers the conflict to the lawmakers
VC-13  Pressure invariance
VC-14  Renewal cites what it renews; none issues after a rejection
VC-15  Definition 7 — the store is exactly the admitted set
VC-16  Like-case consistency — every engineered pair agrees
VC-17  A9 first limb — a standing declaration exists, attributed and dated
VC-18  Express supersession — a silent conflicting record displaces nothing
VC-19  Consolidation admits exactly one record per class, under clause (ii)
VC-20  Consolidation members are disposed by citation, with no retrieval
VC-21  Inexpressibility — differential cases resolve by citation at first instance
VC-22  Docket completeness
VC-23  The two docket routes are kept apart
VC-24  Observer non-influence
VC-25  The audit register is disjoint from the store
VC-26  A9 second limb — the realised adverse-contest rate is computable as two counts
```

Current run: **44/44**. Realised adverse-contest rate over the corpus window: **38 / 2,762 = 0.0138**, reported as two counts and not as a ratio alone, because a positive declaration standing beside a realised rate of zero is a dormancy finding and not a contradiction.

### The suite can fail

`harness/mutation_matrix.py` applies sixteen single-line edits to the engine one at a time, each anchored on a string that occurs exactly once, re-runs the whole suite after each, restores the file and verifies the restoration by SHA-256.

**18 of 18 faults killed, 4 of 4 controls survived.** Two of the controls are not filler:

- Lowering the retrieval threshold θ from 0.25 to 0.20 changes no disposition. That is Proposition 0 showing up as a measurement: premise coverage retrieves a superset of what the gate would admit, so θ governs cost and precision only and cannot cost a controlling record.
- Rewriting the depth key as a list comprehension changes nothing, which records the fact that **the depth key is never decisive on this corpus.** Three keys do the work; the fourth is specified and unexercised, and this README says so rather than letting a reader assume otherwise.

## What this corpus is not

It is a constructed enterprise. The four packs of the Digital Judiciary programme were author-built and so is this one: the `expect` blocks are *designed ground truth*, not expert labels, and any agreement figure computed against them is a pipeline check, not a finding. The corpus establishes that an implementation satisfies the axioms it was built to satisfy. It establishes nothing about whether those axioms describe a clinic anyone runs — that is the field study, and it is future work.

Three further boundaries:

- **Retrieval quality is not secured.** The two judgment functions are fixed at their types only. `distinguish` here is the premise-subset test and `similar` is premise coverage; both are deterministic oracles. A deployment substituting a learned retriever reopens the question and forfeits the guarantee Proposition 0 attaches to coverage.
- **The corpus is blind to precedent-replication error.** A case wrongly decided by citation of a record that should not have controlled it is charged, adjudicated, disposed of, and leaves no docket entry to audit. That is a structural blind spot, not an oversight.
- **Cost is measured, not secured.** No axiom can make deep-reasoning cost track contest rather than volume in a real deployment. First-instance adjudication runs on every arrival.

## Reuse and provenance

Every external source consulted during construction is recorded in `docs/SOURCES.md`, with its verified licence and whether it is safe to vendor or reference-only. Four independent surveys of open test data — clinical interoperability, application security, policy-as-code and supply chain, and legal case-based reasoning — are in `research/`.

The short version: **no factor-annotated legal case base is downloadable under any licence**, so the factor vocabulary here is built rather than acquired; **no veterinary FHIR implementation guide exists**, though the US PDMP guide carries the one veterinary patient fixture in existence (CC0); and several of the most tempting sources — OWASP Benchmark (GPL-2.0), all OWASP standards (CC BY-**SA**), PCI DSS, SNOMED CT, AAHA Diagnostic Terms, ASAP 4.2B, Plumb's — are **not** redistributable into a CC BY 4.0 corpus. Where they appear here at all, it is as cited identifiers, which are facts.

## Licence

- **Code** — the generator, the reference engine, the harness: Apache License 2.0. See `LICENSE`.
- **Data** — the constitution, the corpus, the precedent store, the catalog: Creative Commons Attribution 4.0 International. See `LICENSE-DATA`.

Attribution: cite the Digital Judiciary programme papers listed in `CITATION.cff`.

## Repository layout

```
constitution/     rulebook.json, factors.json, parameters.json
corpus/           cases.json, cases.jsonl, store_seed_initial.json,
                  store_seed.json, docket.json, manifest.json, anomalies.json
generator/        vocab.py, build_constitution.py, build_corpus.py, build_docs.py
harness/          engine.py, run_conformance.py, mutation_matrix.py
schema/           case.schema.json, record.schema.json, provision.schema.json
docs/             CASE_CATALOG.md, case_catalog.csv, COVERAGE.md, MAPPING.md, SOURCES.md
research/         the four open-source data surveys
reproduce/        run_all.sh
```

## Adopting it

1. Map your own provisions onto `constitution/rulebook.json`, keeping the `absolute` flag honest — a floor you can waive is not a floor.
2. Point your pipeline at `corpus/cases.jsonl` and compare each disposition to `expect.final_decision` and `expect.route`.
3. Publish two numbers: your conformance count out of 44, and your realised adverse-contest rate as two counts with the window's bounds stated. The second is the one that says whether your store was built under scrutiny from both directions or under contest by one side only.
4. If you disagree with a case's expected disposition, open an issue citing the provision, the case id and the corpus version. A corpus that adjudicates needs a documented route to dispute a case — and appealing the outcome is a different thing from appealing the procedure.

## Pack version history

**2.4.0 · corpus 2.1.0** — **deny-side jurisprudence** (release 5.14.0). One plain denial in five is now contested and lost (`PLAIN_DENY_CONTESTED_SHARE = 0.20`), writing a deny record whose premise is the violating factor and one compliant factor the instance named; later plain violations of the same pattern are bound by it. Before this, no record in any pack turned on a violating factor and the violating limb was enforced by the Evaluator and prosecutor alone, so the prior-text rung and limb amendments had nothing to act on. The violation-pair coverage queue now gives every ordinary provision one plain denial before covering the remaining factors. The 25-category composition is unchanged and still identical across the five packs; every case id, digest and expectation is regenerated. Also in 5.14.0: a contested case whose hinted premise carries an unrecorded factor is decided but its **record is withheld** (`record_withheld`, referral) — no law on facts nobody established; VC-52 probes it and M31 removes it.

**2.3.0** — **what the record did not see** (release 5.13.0). Two rungs on the admission ladder: `adverse_unaddressed` — a permissive holding does not govern a case carrying a violating factor of any engaged provision that the record's facts never contained (the gate had been one-directional; a permit on {a, b} bound a case doing {a, b, v} a-fortiori) — and `decided_under_prior_text` — records carry `prov_version`, provisions may carry `version` and an `amendment_history`, and a holding falls once an adopted amendment touched a factor it turned on. VC-55 and VC-56 measure zero changed traces on this corpus and fire on their probes; M29 and M30 added; the discriminating suite gains S9. Constitution, corpus, stores, docket and generator digests byte-identical to 2.2.0. `simulation/tools/amendment_overlay.py` measures what an adoption would unsettle.

**2.2.0** — **citation stance and record construction** (release 5.12.0). `Record.cite_stance` (superseded / followed / distinguished / unstated) and `Record.construction` provenance; `_displaces` displaces only on a superseded citation, a legacy citation with no stance being read as superseded so every 2.1.0 ordering is reproduced (VC-54, 0 of ~1,340 executed orderings differ). M28 added. The record stage that reads premise, stance, scope and magnitude from a rationale — with the safe default inverted per field — and the tolerance sweep on a synthetic magnitude overlay live in `simulation/tools/extraction/`. Constitution, corpus, stores, docket and generator digests byte-identical to 2.1.0.

**2.1.0** — the **comparison kernel** (release 5.11.0). `harness/engine.py`'s distinguishing gate is now a comparison kernel with three-valued facts (a factor may be *unrecorded*, which gives a record the status `premise_unproven` and never binds), magnitude factors with declared tolerances (`constitution/dimensions.json`, shipped empty), named gate outcomes on every trace, and A6 under silence (`floor_unresolved`: an unrecorded violating factor of an absolute provision refuses and refers). VC-51 proves on every (record, case) admission that the kernel reduces to `set(premise) <= facts` here; VC-52 silences one premise factor of every controlling record and checks that no bind survives on silence; VC-53 applies the new `harness/binding_gate.py` (exact one-sided false-bind bound, guard items, self-authored-oracle refusal) to the engine's own trace. `benchmark/score.py` gains a `binding_gate` endpoint and a `falsebind` column. M26 and M27 added; M2 re-anchored. Constitution, corpus, stores, docket, generator digests and every earlier figure are byte-identical to 2.0.1. The shared offline characterisation stage lives in `simulation/tools/extraction/`.

**2.0.1** — `benchmark/arms.py`: arm B now retrieves, gates and orders *before* the prosecutor rates against τ, as `engine.adjudicate` does; the earlier order docketed a fully compliant arrival that a live record controlled (found by the Numerals federated stream, release 5.10.0). Constitution, corpus, stores, docket and every conformance figure are byte-identical to 2.0.0.

**2.0.0** — the **scenario extension**. An architect's catalogue of 39 legal,
compliance, reputational and safety scenario classes (`constitution/scenarios.json`,
shared by all five packs) was written first; every provision now carries the classes it
instantiates and a computed `harm_classes` tag. A survey of this constitution against the
catalogue found the topics it was silent on, and they were closed **by addition**: 23 new
provisions (8 absolute) in 6 new families, `origin: extension`, nothing existing
edited; findings about existing provisions were filed as draft amendments (6 now on file).
The corpus was regenerated at **6,000 cases** with the 25-category composition scaled
identically in all five packs, and the generator now guarantees coverage by construction:
every provision receives a compliant touch (the guard item), a plain violation of every
titled factor, a pressure twin and a like-case anchor; every absolute a floor case and a
compliant touch (A6's conjunction); every ordinary provision a risk-owner acceptance draw.
**VC-50** computes the scenario × mechanism matrix from the executed corpus and fails on any
demanded cell that is empty; **M25** breaks the checker and VC-50's self-test kills it.
`docs/SCENARIO_COVERAGE.md` is the matrix; `benchmark/human.py` adds arm C, a priced human
review desk (`--human`, estimation-only, every input a stated ⟦PROJECTED⟧ parameter). One
generator defect was fixed in place: a pressure control is no longer accepted when a record
it consulted lapses at the twin's timestamp, a confound the 5,000-case build avoided by
luck. Figures elsewhere in this file that quote 1.x counts (opening store, records written,
acceptances) are superseded by `corpus/manifest.json`.

**1.3.0** — every case is a **development change**, not a runtime business
transaction. An audit of all five catalogues found forty-eight titles that had
drifted across that line in one of two ways: an act on live data ("Correct the
mis-posted interchange fee by updating the ledger row" is a data edit, not a
diff) or a process with no artefact ("Complete the vendor security review for
the statement PDF renderer" happens in a meeting, not in a tree). Each was
rewritten as the change that would actually appear in the pull request. VC-49
and M24 stop them coming back. Corpus version 1.2.0: **only the change
descriptions moved** — every disposition, route, controlling record, consulted
set, store entry, docket entry and published count is byte-identical to 1.1.0,
verified field by field. 49 conformance checks, 24 mutants.


**1.2.0** — adds the disclosure overlay: `benchmark/justification.py` and
`--justify N`, which files the same change twice with different author notes and
scores whether the disposition moves on the strength of prose. For the
adjudicator it cannot — §4.6 takes factors — so VC-48 checks the whole trace
across every pair and M22 exists to break it. Corpus version unchanged at 1.1.0.
48 conformance checks, 23 mutants.


**1.1.0** — adds the discriminating suite: `benchmark/discriminating.py`,
`benchmark/build_scenarios_doc.py` and the generated
`docs/DISCRIMINATING_SCENARIOS.md`. Eight scenario families, each built from a
PACT finding and sorted into three tiers — five structural, two measured, one
adverse. Run it with

```bash
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
```

The **corpus version stays 1.0.0**, because the corpus did not change: the
constitution, the 5,000 cases, the stores and the docket are byte-identical to
1.0.0, and the 44 checks and 18 mutants give the same result. What changed is
tooling and documentation, plus one fairness correction inside the benchmark's
retrieval for the non-binding arms (they were being handed the engine's lapse
filter, which is one of the mechanisms under test).

**1.0.0** — first release: the 5,000-case executed simulation.
