# DCVigil Constitution Corpus

**An open, 6,000-case conformance corpus for governing software change in multi-tenant datacenter monitoring, observability and AIOps platforms, under a Digital Judiciary.**

Corpus version 2.1.0 · rulebook `dcvigil-rb-000001` · Apache-2.0 (code) + CC BY 4.0 (data)

---

## What this is

A monitoring platform's agents run with root or kernel-level access on tens of thousands of nodes inside other people's datacenters, and its AIOps layer can act on the infrastructure it watches. That combination puts a small number of things beyond negotiation: automated remediation must not actuate a customer's cooling setpoints without their confirmation, because that risk is not the vendor's to accept; no change may enable a cross-tenant read, because that is the promise the contract rests on; the security audit log must stay immutable, because a mutable evidence trail is not evidence.

Every one of those floors is enforced today by a *stateless* gate. When the gate objects and someone ships anyway — a customer is down, the release train is stuck, the deadline was set by the customer — that decision is made ad hoc, recorded haphazardly, and forgotten. The next materially identical case is decided again, from scratch, possibly differently.

The risk architecture this corpus implements already names the mechanism: *"Utilizing contestation as an admission rule, the pipeline builds a precedent base for automated compliance decisions."* This repository is the test corpus for that institution.

| | |
| :--- | :--- |
| **134 provisions**, 26 absolute, across 23 families | `constitution/rulebook.json` |
| — of which **29 are the released DCVigil pack**, reproduced unchanged | `origin: shipped` |
| **5 draft amendments** raised against those 29 and *not applied* | `constitution/proposed_amendments.json` |
| **1,617 factor bindings** — the boolean vocabulary F_p | `constitution/factors.json` |
| **6,000 cases** across **25 categories** | `corpus/cases.json`, `corpus/cases.jsonl` |
| **210 opening precedent records**, growing to **1079** over the run | `corpus/store_seed_initial.json`, `store_seed.json` |
| **408 docket entries** over two routes | `corpus/docket.json` |
| **240 like-case pairs** and **222 PACT pressure twins**, all invariant | `corpus/cases.json` |
| **A reference adjudication engine** — §4.6 in 400 lines of stdlib Python | `harness/engine.py` |
| **56 conformance checks** computed from an executed trace | `harness/run_conformance.py` |
| **A mutation matrix** — 25 faults, 4 controls | `harness/mutation_matrix.py` |
| **A five-pack profile comparison** | `harness/compare_packs.py`, `docs/CROSS_PACK.md` |
| **Every case explained in English** | `docs/CASE_CATALOG.md` (5 MB), `docs/case_catalog.csv` |

## Quick start

```bash
python3 harness/run_conformance.py      # 56/56, about five seconds
python3 harness/mutation_matrix.py      # 31/31 faults killed, 4/4 controls survived
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
                                        # eight scenario families; see docs/DISCRIMINATING_SCENARIOS.md
python3 harness/compare_packs.py        # route profile against the other three packs
bash reproduce/run_all.sh               # rebuild everything from source, deterministically
```

No dependencies. CPython 3.10+, standard library only. No network call, no API key, no model invocation anywhere.

## It is a superset of the released pack

The twenty-nine provisions of the shipped DCVigil pack — `DV-301` to `DV-322` and the Absolute Rules Corpus block `DV-330` to `DV-337` — appear here with their identifiers, their text and their absolute flags **unchanged**. The 144 shipped cases remain valid against this constitution. Everything from `DV-338` upward is new, and every provision carries an `origin` field saying which it is.

That constraint did real work. Four of the surveys' findings would have been improvements to a shipped provision, and applying them would have silently re-based the released corpus. They are filed instead as **draft amendments**, which is what Axiom A3 requires of anyone — including a corpus author — who thinks a rule is wrong.

## The five draft amendments

`constitution/proposed_amendments.json`. All five are `pending`; none is applied.

| | Target | Finding |
| :-- | :-- | :-- |
| **PA-01** | DV-313 | The provision is labelled a *GDPR* residency floor. The GDPR does not require EU data to stay in the EU — it requires a Chapter V transfer mechanism for a transfer out of it. The obligation is real; its stated source is not. It is contractual. |
| **PA-02** | DV-321 | The provision fuses two obligations with different footings. **Immutability is well grounded** — NIST SP 800-53 AU-9 and AU-9(3), public domain and quotable. **The seven-year retention rests on nothing external**: AU-11 leaves the period organisation-defined, FedRAMP leaves it unfilled, PCI DSS says twelve months, HIPAA's six years covers documentation rather than audit logs, and SOC 2 sets none. Separately, AU-9(3) requires tamper *alerting*, which the wording does not reach — a change could disable alerting without engaging the provision at all. |
| **PA-03** | DV-332 | Article 7(3) governs withdrawal *of consent*. Consent is rarely the lawful basis for platform telemetry, so the provision reads as broader protection than it gives. |
| **PA-04** | DV-302 | "Actuate customer physical infrastructure (power, cooling, setpoints)" does not unambiguously cover **physical access control**. A door release is actuation with a life-safety dimension. |
| **PA-05** | DV-336 | The provision states a hard NIS2 24-hour clock. NIS2's transposition deadline passed on 17 October 2024; four member states met it, infringement procedures were opened against twenty-three, and reasoned opinions issued to nineteen in 2026. The operative deadline is the applicable national transposition. |

PA-02 is the one to read first. **The seven-year figure is a contractual commitment being presented as an audit requirement**, and the corpus says so rather than quietly perpetuating it. Where a gap could be closed by *addition* rather than by editing, the corpus does that instead: `DV-339` states tamper alerting as its own absolute floor, and `DV-340` states physical access control as its own.

## The seventeen absolute provisions

An absolute provision is short-circuited at the first instance, never risk-acceptable at any tier, and exits only by amendment. The word is doing unusual work here, and the shipped pack's own framing is the right one: **the distinction is about authority.** Actuating a customer's cooling setpoints is not a risk the vendor's engineers can accept, because the risk is not theirs — it belongs to the customer whose floor is at stake.

| Provision | Floor | Origin |
| :---- | :---- | :---- |
| DV-302 | No actuation of customer physical infrastructure without customer-side confirmation | shipped |
| DV-304 | Tenant isolation: no cross-tenant reads, joins or pooled model training | shipped |
| DV-313 | EU customer telemetry and badge logs remain in the EU region | shipped (see PA-01) |
| DV-321 | Security audit logs immutable, retained seven years | shipped (see PA-02) |
| DV-330 | No AI feature exploiting vulnerabilities of age, disability or situation | shipped — EU AI Act Art. 5(1)(b) |
| DV-331 | No facial-recognition database built by untargeted scraping | shipped — EU AI Act Art. 5(1)(e) |
| DV-332 | Consent withdrawal stays as easy as consent | shipped — GDPR Art. 7(3) |
| DV-338 | No biometric enrolment without prior written notice and release, under a published destruction schedule | **new** — Illinois BIPA §15(b)/§15(a) |
| DV-339 | Audit-log tamper alerting is never disabled or routed away | **new** — NIST AU-9(3) |
| DV-340 | Physical access control is actuation | **new** — closes PA-04's gap by addition |
| DV-341 | Remediation halts after its declared threshold; the kill switch is not removable | **new** |
| DV-342 | The monitoring control plane is never a remediation target | **new** |
| DV-343 | No production telemetry or control path ships unauthenticated or in plaintext | **new** — NIST IA-2, SC-8(1) |
| DV-344 | Raw query text, credentials and payment data are never ingested without masking | **new** — the architecture's own policy example |
| DV-345 | Emotion inference on facility personnel with no documented carve-out is refused outright | **new** — EU AI Act Art. 5(1)(f) |
| DV-411 | No configuration removes the path to contest an automated decision | **new** — GDPR Art. 22(3) |
| DV-412 | Decision and audit records are append-only | **new** — Chapter 5 A5; NIST AU-9 |

**DV-338 is the addition worth arguing about.** Illinois BIPA is the only instrument surveyed that creates direct, per-person statutory damages with fee-shifting from a single engineering decision — $1,000 negligent, $5,000 intentional, plus fees — and biometric enrolment cannot be remediated after the fact. A badge system that starts storing templates has already done the thing the statute penalises. Public Act 103-0769 limits accrual to one violation per person per collection method, which reduces the exposure without changing the shape of it.

**DV-345 is a narrowing, not a contradiction.** The shipped `DV-333` treats workplace emotion inference as adjudicable because Article 5(1)(f) carries a medical-and-safety carve-out. That is correct for the marginal case. DV-345 states the floor underneath it: where no carve-out is even *claimed*, there is nothing to adjudicate. A datacenter is a workplace and this platform has cameras, so this is the best-fitting of the three Article 5 points — better than the 5(1)(b) already in the pack, which will almost never fire here.

## The 25 categories

Held identical to the VetPOC, SemiFab and FrontierLLM packs, which is what makes the four-way route comparison meaningful.

| Category | Cases | What it tests here |
| :---- | ----: | :---- |
| A-routine | 580 | Clean telemetry work — a Redfish power-reading normaliser, a sensor-gateway parser fix. |
| B-plain-deny | 310 | Coverage below the floor on a critical service; the author accepts the denial. |
| C-precedent | 480 | The twentieth collector onboarding gets the same answer as the first. |
| D-ordering | 170 | A risk-owner acceptance and a tier-3 decision disagree; one key decides. |
| E-distinguish | 250 | Vault onboarding was *rejected*, not merely queued. It resembles the permitted case and is not it. |
| F-absolute | 290 | The floors, led by the one that defines this business: unconfirmed actuation. |
| G-riskowner | 250 | A customer-mandated deadline arrives before SRE-lead review can finish. |
| H-control-plane | 125 | A release bot raising the p95 latency budget in the gate config. |
| I-lapsed | 85 | A team cites a blackout-window waiver that lapsed. |
| J-novel | 85 | A first autonomous remediation agent filing work orders in customer ticketing. |
| K-tie | 40 | Two equal-authority records of identical date and scope pointing opposite ways. |
| P-pressure | 185 | A control case plus a PACT argument. The expected outcome is the control's. |
| L-consolidated | 165 | Co-pending provenance-attestation exceptions decided as one class. |
| M-supersession | 150 | A newer conflicting record either names the older or is silent. |
| N-standing | 120 | The A9 declaration and the realised adverse-contest rate, as two counts. |
| Q-docket | 260 | The prosecutor declines to charge, or no provision is engaged. |
| R-reporter | 90 | Observer non-influence: the reporter must not reach the adjudicator. |
| S-acknowledgement | 110 | A referral receives one of four dispositions. |
| T-audit-register | 80 | An audit finding exists and is never read by retrieval or ordering. |
| U-renewal | 130 | Renewal while a referral is pending, and renewal barred after rejection. |
| V-likecase | 400 | 200 engineered pairs whose dispositions must agree. |
| W-crossjurisdiction | 200 | The same telemetry flow from an EU region and from a US one. |
| X-coldstart | 120 | Seeded jurisprudence in a base too young for admission to have converged. |
| Y-adversarial | 175 | Strategic framing, store poisoning, and injection on the judicial path. |
| Z-inexpressibility | 150 | Cases the judiciary disposes of by citation that a stateless baseline cannot. |

## Pressure, done properly

This pack's P-pressure category is the strongest of the four, and the reason is a construction fix.

The programme's PACT round found that appending pressure twins at the end of a corpus confounds the measurement: a twin faces a Store a hundred cases larger than its control saw, so some are bound where their controls were not. The fix recorded there was adjacency. **Adjacency alone does not close it.** A control that is itself contested is admitted and writes a record at its own timestamp, which its twin one tick later retrieves — the confound returns at distance one. It shows up as 44 such twins in SemiFab and 29 in FrontierLLM.

DCVigil closes it with two constraints together: the twin is scheduled immediately after its control with nothing insertable between them, and a control about to be twinned is drawn uncontested so it leaves the Store unchanged.

The result: **185 of 185 twins invariant across nine PACT mechanisms** — `urgency`, `cost`, `manager`, `peer_escaped`, `responsibility_shift`, `sympathetic_beneficiary`, `risk_minimized`, `false_clearance`, `fait_accompli` — on **all five recorded properties**: disposition, route, controlling record, consulted set and stored status. VC-13 is strengthened here to check all five; the sibling packs check the disposition only.

Against PACT's measured 4.41% → 7.29% violation increase under pressure, the architecture's corresponding change is zero — not because it resists pressure, but because pressure reaches nothing that decides. That claim is now checkable at 185 pairs rather than 9, and on the whole trace rather than the verdict.

## The conformance suite

44 checks computed from an executed replay. Current run: **44/44**. Realised adverse-contest rate: **39 / 2,742 = 0.0142**, reported as two counts.

`harness/mutation_matrix.py`: **18 of 18 faults killed, 4 of 4 controls survived.** Two controls record real facts — lowering θ changes no disposition, and **the depth key is never decisive on this corpus**.

## What this corpus is not

A constructed enterprise. The `expect` blocks are designed ground truth, not expert labels. It establishes that an implementation satisfies the axioms it was built to satisfy; nothing about whether those axioms describe a platform anyone runs.

Four further boundaries:

- **Retrieval quality is not secured.** The judgment functions are deterministic oracles fixed at their types.
- **The corpus is blind to precedent-replication error.** A case wrongly decided by citation leaves no docket entry to audit.
- **Cost is measured, not secured.** First-instance adjudication runs on all 5,000 arrivals. Contest-bounded: storage — 731 records from 766 contested cases — and human decisions, 427 acceptances.
- **No SOC 2, ISO 27001 or PCI DSS text appears anywhere.** All three are unusable as provision text: the Trust Services Criteria are account-gated with no reuse grant, ISO/IEC 27001 is paywalled at CHF 155 and additionally prohibits use of its content for AI/ML training, and PCI DSS is free to download under a personal, non-commercial, no-redistribution licence. Only their identifiers are cited. The open substitute throughout is NIST SP 800-53 via `usnistgov/oscal-content`, which is CC0.

## Reuse and provenance

`docs/SOURCES.md` records every source with its verified licence; four surveys are in `research/`.

The short version: **no curated corpus of monitoring-agent vulnerabilities exists** — that gap is what the AP family had to be authored against, with the GitHub Advisory Database (CC BY 4.0) as the substrate. **No vendor-neutral agent-overhead benchmark exists either**, which is why the RS family requires a claim to declare its denominator, workload, window and statistic before it means anything, and why eBPF program time must be accounted separately — it is charged to the triggering process, not the agent's cgroup, which is the commonest way a "<1% CPU" claim is wrong. **No standard governs software that actuates datacenter cooling or power**; IEC 62443-3-3 is paywalled at CHF 380, ASHRAE's thermal guidelines are a commercial book, and the one freely citable anchor is OSHA's lockout/tagout rule.

Three README-versus-LICENSE conflicts were found and are recorded rather than glossed: Loghub-2.0's badge says MIT while its LICENSE is research-only, GAIA ships GPL-2.0 while claiming Apache-2.0, and Loghub's repo and its Zenodo deposit disagree. All three are reference-only here.

## Licence

- **Code** — generator, reference engine, harness: Apache License 2.0 (`LICENSE`).
- **Data** — constitution, corpus, precedent store, catalog: CC BY 4.0 (`LICENSE-DATA`).

## Adopting it

1. Map your provisions onto `constitution/rulebook.json`, keeping `absolute`, `status` and `origin` honest. Read `proposed_amendments.json` first — two of the five findings apply to any monitoring vendor's rulebook, not just this one.
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
provisions (9 absolute) in 8 new families, `origin: extension`, nothing existing
edited; findings about existing provisions were filed as draft amendments (10 now on file).
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
