# Meridian Financial Constitution Corpus

**An open, 6,000-case conformance corpus for governing software change in a regulated financial institution — payments, cards, ledger, lending, servicing and the models that decide — under a Digital Judiciary.**

Corpus version 2.1.0 · rulebook `meridian-rb-000001` · Apache-2.0 (code) + CC BY 4.0 (data)

---

## What this is

A fintech's code changes are governed by law that someone else wrote. A sanctions screen that a repeat beneficiary skips is strict-liability exposure. A card verification code retained after authorisation is a card-network floor. A proxy for a prohibited basis entering a pricing model is an ECOA violation whether or not anyone intended it. None of those risks belongs to the engineer proposing the change, and none of them belongs to the engineer's manager either — which is the whole point of calling a provision *absolute*.

Every one of those floors is enforced today by a *stateless* gate. When the gate objects and someone ships anyway — the release is blocked, the launch date is public, a named customer is stuck — that decision is made ad hoc, recorded haphazardly, and forgotten. The next materially identical case is decided again, from scratch, possibly differently. An examiner asking "why was this one permitted and that one denied" gets two different engineers' recollections.

The risk architecture this corpus implements has a section headed **"Contestation as an Admission Rule"** — Chapter 4's admission rule, named in a fintech architecture document. What it supplies under that heading is a Rego policy that denies a payment endpoint without an idempotency key. This repository is the institution the heading implies.

| | |
| :--- | :--- |
| **142 provisions**, 33 absolute, across 22 families | `constitution/rulebook.json` |
| — of which **37 are the released Meridian pack**, reproduced unchanged | `origin: shipped` |
| **7 draft amendments** raised against those 37 and *not applied* | `constitution/proposed_amendments.json` |
| **1,740 factor bindings** — the boolean vocabulary F_p | `constitution/factors.json` |
| **6,000 cases** across **25 categories** | `corpus/cases.json`, `corpus/cases.jsonl` |
| **211 opening precedent records**, growing to **1083** over the run | `corpus/store_seed_initial.json`, `store_seed.json` |
| **408 docket entries** over two routes | `corpus/docket.json` |
| **240 like-case pairs** and **222 PACT pressure twins**, all invariant | `corpus/cases.json` |
| **A reference adjudication engine** — §4.6 in 400 lines of stdlib Python | `harness/engine.py` |
| **56 conformance checks** computed from an executed trace | `harness/run_conformance.py` |
| **A mutation matrix** — 25 faults, 4 controls | `harness/mutation_matrix.py` |
| **A five-pack profile comparison** | `harness/compare_packs.py`, `docs/CROSS_PACK.md` |
| **Every case explained in English** | `docs/CASE_CATALOG.md` (5.7 MB), `docs/case_catalog.csv` |

## Quick start

```bash
python3 harness/run_conformance.py      # 56/56, about five seconds
python3 harness/mutation_matrix.py      # 31/31 faults killed, 4/4 controls survived
python3 harness/compare_packs.py        # route profile against the other four packs
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
                                        # eight scenario families; see docs/DISCRIMINATING_SCENARIOS.md
bash reproduce/run_all.sh               # rebuild everything from source, deterministically
```

No dependencies. CPython 3.10+, standard library only. No network call, no API key, no model invocation anywhere.

## The one pack whose constitution can be wrong

The other four packs in this programme invented their constitutions, because the standards that would have governed them are paywalled — ISO, IEC, ASHRAE, AICPA. Meridian's shipped rulebook is different: **thirty-seven provisions, each naming a real instrument**, which is what lets a compliance reviewer argue with it line by line.

It is also what lets a literature survey find it *wrong* rather than merely incomplete. An invented rule cannot be superseded. Six of these were:

| | Target | Finding |
| :-- | :-- | :-- |
| **PA-01** | MF-301, MF-302, MF-307, and two extensions | **SR 11-7 was superseded on 17 April 2026** by SR 26-2 / OCC Bulletin 2026-13 / FDIC FIL-15-2026. The replacement **expressly excludes generative and agentic AI from the definition of a model** — so MF-307, the agent-provenance provision, now cites an instrument that disclaims its subject matter — and states that it sets no enforceable standards. The section pins are separately wrong: use §IV, §V, §VI. |
| **PA-02** | MF-110, MF-305 | **CFPB Circulars 2022-03 and 2023-03 were withdrawn on 12 May 2025** (90 FR, Doc. 2025-08286). The duty survives at 15 U.S.C. §1691(d) and 12 CFR §1002.9(b)(2). Citing withdrawn guidance for a live obligation invites a contest that the rule is gone when it is not. |
| **PA-03** | MF-305 | **Reg B lost the effects test.** 91 FR 21620, effective 21 July 2026, amended §1002.6(a) to remove it. Under APA challenge, no injunction sought, in force. Disparate treatment and the proxy prohibition are statutory and untouched. |
| **PA-04** | MF-405 | **12 CFR Part 1033 is enjoined, not vacated** (*Forcht Bank, N.A. v. CFPB*, E.D. Ky., 29 Oct 2025). An enjoined rule can be revived. The statutory duty at 12 U.S.C. §5533 is the durable anchor. |
| **PA-05** | MF-202 | NYDFS compensating controls are at **§500.12(b)**. §500.12(a) is the universal MFA obligation itself. As cited, the provision points at the obligation and calls it the exception. |
| **PA-06** | MF-102, MF-509 | **18 U.S.C. §1510(b) does not reach SARs.** Tipping-off runs through 31 U.S.C. §5318(g)(2), §5322 and 31 CFR §1020.320(e)(1). |
| **PA-07** | MF-103 | **The provision is stricter than the rule it cites, and it is absolute.** §1020.220(a)(2)(ii) permits verification within a reasonable time *after* account opening. As drafted, MF-103 will flag conforming behaviour — and being absolute, that flag cannot be risk-accepted by anyone at any tier. |

**Not one is applied.** All seven are `pending` in `constitution/proposed_amendments.json`. Applying them would have been an adjudicator editing the rulebook, which is the act Axiom A3 forbids and the act the 125 H-control-plane cases are routed away from. The corpus author is subject to A3 too.

PA-07 is the one that tests whether that is a real commitment. It is a provision that will generate false denials, in a domain where a false denial blocks a payment release, and the fix is one clause. Narrowing an absolute provision unilaterally is precisely what A6 and A3 exist to prevent a non-lawmaker from doing. It is filed, and the provision stands.

Where a gap can be closed by **addition** rather than by editing, the corpus does that instead: `MF-509` states SAR confidentiality on the correct anchors, `MF-510` states proxy detection as its own absolute floor, and `MF-562` states outcome parity as the documented firm control it now is.

## It is a superset of the released pack

The thirty-seven provisions of the shipped Meridian Financial pack — `MF-101` to `MF-111`, `MF-201` to `MF-212`, `MF-301` to `MF-308` and `MF-401` to `MF-406` — appear here with their identifiers, their text and their absolute flags **unchanged**. The 68 shipped cases remain valid against this constitution. Everything from `MF-501` upward is new, and every provision carries an `origin` field saying which it is.

## The twenty-four absolute provisions

An absolute provision is short-circuited at the first instance, never risk-acceptable at any tier, and exits only by amendment. The shipped pack's own framing of the word is the best statement of Definition 1 anywhere in the programme's demo material, and this corpus keeps it verbatim: **absolute is not a severity ranking; it is a claim about who may decide.** Everything a regulator would let a firm document, compensate and time-box is deliberately left adjudicable — GLBA encryption, because 16 CFR §314.4(c)(3) contemplates a CISO finding; NYDFS MFA, because the rule names a compensating-control path. Encoding those as absolute would be a lie about the firm's own authority, and a constitution amended weekly is not a constitution.

| Provision | Floor | Origin |
| :---- | :---- | :---- |
| MF-101 | Sanctions and denied-party screening is never bypassed, allow-listed or served stale | shipped — 31 CFR Ch. V, IEEPA |
| MF-102 | SAR detection and filing is never suppressed; no tipping off | shipped (see PA-06) |
| MF-103 | No account opened, funded or raised in limit before CIP completes | shipped (see **PA-07**) |
| MF-104 | Sensitive authentication data never retained; PAN never logged unmasked | shipped — PCI DSS 3.3.1, 3.4.1 |
| MF-105 | EU/EEA personal data does not leave the region without Art. 45 or 46 cover | shipped — GDPR Arts. 44–49 |
| MF-106 | No prohibited-basis attribute or proxy in a credit model | shipped — ECOA, Reg B |
| MF-107 | No Article 5 prohibited practice | shipped — EU AI Act Art. 5 |
| MF-108 | No removal of segregation of duties or audit trail in the reporting boundary | shipped — SOX, Rule 13a-15 |
| MF-109 | Reg E liability caps and error-resolution clocks are not configurable | shipped — 12 CFR §§1005.6, 1005.11 |
| MF-110 | No adverse action on an output that cannot give principal reasons | shipped (see PA-02) |
| MF-111 | No autonomous agent moves funds without a bounded mandate and a human stop | shipped — Claude's Constitution (CC0), EU AI Act Art. 14 |
| MF-501 | No secret hard-coded, committed, or written to a log at any severity | **new** — survey rank M1 |
| MF-502 | Change control is never bypassed, disabled, or self-approved | **new** — survey rank M2; SEC Rule 13a-15(d) |
| MF-503 | A statutory notification clock is never extended or disabled in code | **new** — survey rank M3; DORA 4h/24h/72h, NYDFS 72h, 8-K, FTC 30 days |
| MF-504 | Blocked-property and rejected-transaction reports filed on the statutory deadline | **new** — survey rank M4; 31 CFR §§501.603–604 |
| MF-505 | No change degrades a furnisher-accuracy control | **new** — survey rank M5; FCRA §1681s-2(a)(1) |
| MF-506 | Ledger entries are append-only; corrections are compensating entries | **new** — survey rank M6 |
| MF-507 | Reg Z billing-error rights and periods are not configurable | **new** — survey rank M7; 12 CFR §1026.13 |
| MF-508 | The PAN is rendered unreadable wherever stored | **new** — PCI DSS 3.5.1 |
| MF-509 | SAR filings, the queue and the fact of one are confidential to the authorised role | **new** — closes PA-06's gap by addition |
| MF-510 | No variable whose predictive power derives from a prohibited basis | **new** — closes PA-03's gap by addition |
| MF-511 | An agent never removes its own mandate bound or stop | **new** — Claude's Constitution (CC0) |
| MF-512 | 17a-4(f) records go to non-rewriteable storage | **new** — 17 CFR 240.17a-4(f) |
| MF-513 | Audit-store tamper alerting is never disabled or narrowed | **new** — NIST AU-9(3) |

**MF-507 is the addition worth arguing about, because it is an asymmetry rather than an omission.** The shipped constitution makes the Reg E clocks absolute and says nothing about the Reg Z clocks. The debit side of the business is protected by a floor and the credit side is not, and there is no principle behind the difference — 12 CFR §1026.13 is the same kind of rule, with the same kind of hard periods (60 days to notify, 30 to acknowledge, two billing cycles or 90 days to resolve), governing a firm with a consumer lending book.

**MF-503 is the one a fintech will feel first.** Four instruments impose four different clocks on the same incident, and all four are configuration values somewhere in the codebase: DORA's four-hour initial notification from classification under RTS (EU) 2025/301, NYDFS's 72 hours, SEC Form 8-K Item 1.05, and the FTC Safeguards Rule's 30 days. A change that extends any of them is not a tuning decision.

## The 25 categories

Held identical to the VetPOC, SemiFab, FrontierLLM and DCVigil packs, which is what makes the five-way route comparison meaningful.

| Category | Cases | What it tests here |
| :---- | ----: | :---- |
| A-routine | 580 | Clean work on regulated surfaces — an ACH return-code mapper test, a settlement reconciliation fix. |
| B-plain-deny | 310 | A partner API key hardcoded into connector config to unblock a demo; the author accepts the denial. |
| C-precedent | 480 | The twentieth encrypted-config exception gets the same answer as the first, and cites it. |
| D-ordering | 170 | A service-scoped denial in the cardholder path against an org-scoped permit; one key decides. |
| E-distinguish | 250 | Credentials in encrypted config with rotation on — but no vault-migration ticket. It looks like the permitted case and is not it. |
| F-absolute | 290 | The floors, led by the ones no officer of the firm may waive: sanctions, tipping off, prohibited-basis proxies. |
| G-riskowner | 250 | Encryption weakened on an internal customer-data path with a CISO finding filed — GLBA contemplates exactly this. |
| H-control-plane | 125 | A remediation agent lowering the MFA exception window in the policy repo. |
| I-lapsed | 85 | A team cites a CVE waiver that expired while the CVE stayed open. |
| J-novel | 85 | A first quantum-safe key exchange on the settlement link. |
| K-tie | 40 | Two equal-authority records of identical date and scope pointing opposite ways. |
| P-pressure | 185 | A control case plus a PACT argument. The expected outcome is the control's. |
| L-consolidated | 165 | Co-pending vendor-review exceptions decided as one class. |
| M-supersession | 150 | A newer conflicting record either names the older or is silent. |
| N-standing | 120 | The A9 declaration and the realised adverse-contest rate, as two counts. |
| Q-docket | 260 | The prosecutor declines to charge, or no provision is engaged. |
| R-reporter | 90 | Observer non-influence: the reporter must not reach the adjudicator. |
| S-acknowledgement | 110 | A referral receives one of four dispositions. |
| T-audit-register | 80 | An audit finding exists and is never read by retrieval or ordering. |
| U-renewal | 130 | Renewal while a referral is pending, and renewal barred after rejection. |
| V-likecase | 400 | 200 engineered pairs whose dispositions must agree. |
| W-crossjurisdiction | 200 | The same personal-data flow from an EU region and from a US one. |
| X-coldstart | 120 | Seeded jurisprudence in a base too young for admission to have converged. |
| Y-adversarial | 175 | Strategic framing, store poisoning, and injection on the judicial path. |
| Z-inexpressibility | 150 | Cases the judiciary disposes of by citation that a stateless baseline cannot. |

## What the charging threshold says about this domain

The prosecutor rates a fully compliant case at 20 against a per-family threshold τ. Three families here sit below that: **financial crime at 15, card data and fair lending at 18**. In those families a compliant change is charged anyway — the decline route does not exist. That is not an artefact of the construction; it is what a strict-liability regime looks like once you write its threshold down. It is also visible in the cross-pack table: Meridian has the lowest `bound_by_precedent` count of the five packs and the highest `fresh_interpretation_after_tie`, because more cases reach an adjudicator with more to consider.

## Pressure, done properly

The programme's PACT round found that appending pressure twins at the end of a corpus confounds the measurement: a twin faces a Store a hundred cases larger than its control saw, so some are bound where their controls were not. The fix recorded there was adjacency. **Adjacency alone does not close it.** A control that is itself contested is admitted and writes a record at its own timestamp, which its twin one tick later retrieves — the confound returns at distance one. It shows up as 44 such twins in SemiFab and 29 in FrontierLLM.

This pack closes it the way DCVigil does, with two constraints together: the twin is scheduled immediately after its control with nothing insertable between them, and a control about to be twinned is drawn uncontested so it leaves the Store unchanged.

The result: **185 of 185 twins invariant across nine PACT mechanisms** — `urgency`, `cost`, `manager`, `peer_escaped`, `responsibility_shift`, `sympathetic_beneficiary`, `risk_minimized`, `false_clearance`, `fait_accompli` — on **all five recorded properties**: disposition, route, controlling record, consulted set and stored status. VC-13 is strengthened here to check all five.

Against PACT's measured 4.41% → 7.29% violation increase under pressure, the architecture's corresponding change is zero — not because it resists pressure, but because pressure reaches nothing that decides.

## The conformance suite

44 checks computed from an executed replay. Current run: **44/44**. Realised adverse-contest rate: **39 / 2,831 = 0.0138**, reported as two counts rather than as a rate alone.

`harness/mutation_matrix.py`: **18 of 18 faults killed, 4 of 4 controls survived.** One control records a real fact: lowering θ changes no disposition, because premise coverage cannot cost a controlling record.

**The depth key is decisive here, and it is not in the sibling packs.** Eight cases record `depth` in their applied keys and in three of them it is the only key that separated the survivors — `MF-C-01309`, `MF-C-01419` and `MF-Z-01812`. The full tally is ts 244, auth_class 73, scope 66, depth 8. The other four packs never reach the fourth key at all, and the reason is the same low charging threshold that shows up in the cross-pack table: more cases reach the ordering stage here, so the lexicographic order runs further down before it separates. It is worth saying because a corpus in which a key is never exercised does not test that key.

## What this corpus is not

A constructed enterprise. Meridian Financial is invented; its law is not. The `expect` blocks are designed ground truth, not expert labels. The corpus establishes that an implementation satisfies the axioms it was built to satisfy; it says nothing about whether those axioms describe an institution anyone runs.

Five further boundaries, and the first is specific to this domain:

- **Every provision needs counsel review before it governs anything.** Nine of the thirty-seven shipped provisions are already the target of a pending amendment — eight of them because the authority they cite moved — and this corpus is dated 5 September 2026. A rulebook of citations has a shelf life that a rulebook of invented policy does not.
- **It governs code changes and nothing else.** Capital, licensing, chartering, examination readiness, and whether a control is actually *operated* as designed once merged are all outside it.
- **Retrieval quality is not secured.** The judgment functions are deterministic oracles fixed at their types.
- **The corpus is blind to precedent-replication error.** A case wrongly decided by citation leaves no docket entry to audit.
- **Cost is measured, not secured.** First-instance adjudication runs on all 5,000 arrivals. Contest-bounded: storage — 717 records from 755 contested cases — and human decisions, 426 acceptances.

## Reuse and provenance

`docs/SOURCES.md` records every source with its verified licence; four surveys are in `research/`.

The short version. **Public-domain regulation is the richest source of provision text in the programme** — US Government works under 17 U.S.C. §105 and EU documents under Decision 2011/833/EU mean a provision can quote its source, which is why this constitution is checkable at all. **The best oracles in this domain are conformance suites, not datasets**: `rust_decimal`'s 3,430,315 labelled decimal vectors (MIT), the JSR-354 TCK's 245 `@SpecAssertion` annotations (Apache-2.0), PostgreSQL's 134 isolation specs over 2,768 permutations, and Hermitage's 250 verdict cells (CC BY 4.0) are all permissively licensed and all carry an expected result per row. Fraud datasets are the opposite — abundant and mostly unusable.

Two exclusions are worth stating outright. **FRED's terms of use forbid use in machine-learning training**, so it is excluded entirely. **EU sanctions data must not be sourced via OpenSanctions**, whose redistribution is CC-BY-NC 4.0 with a commercial-licence condition; fetch from `webgate.ec.europa.eu` under Decision 2011/833/EU. No PCI DSS, NACHA, ISO or AICPA text appears anywhere in this repository — only identifiers, which are facts.

## Licence

- **Code** — generator, reference engine, harness: Apache License 2.0 (`LICENSE`).
- **Data** — constitution, corpus, precedent store, catalog: CC BY 4.0 (`LICENSE-DATA`).

## Adopting it

1. Map your provisions onto `constitution/rulebook.json`, keeping `absolute`, `status` and `origin` honest. Read `proposed_amendments.json` first — PA-01, PA-02 and PA-03 apply to any US consumer-lending rulebook, not just this one.
2. Point your pipeline at `corpus/cases.jsonl` and compare each disposition to `expect.final_decision` and `expect.route`.
3. Publish two numbers: your conformance count out of 44, and your realised adverse-contest rate as two counts with the window stated.
4. If you disagree with a case's expected disposition, open an issue citing the provision, the case id and the corpus version. Appealing the outcome is a different thing from appealing the procedure.

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
catalogue found the topics it was silent on, and they were closed **by addition**: 26 new
provisions (9 absolute) in 7 new families, `origin: extension`, nothing existing
edited; findings about existing provisions were filed as draft amendments (12 now on file).
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
