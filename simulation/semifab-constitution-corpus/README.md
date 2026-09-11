# SemiFab Constitution Corpus

**An open, 6,000-case conformance corpus for governing software change in semiconductor manufacturing operations monitoring and supply-chain control-tower software, under a Digital Judiciary.**

Corpus version 2.1.0 · rulebook `semifab-rb-000001` · Apache-2.0 (code) + CC BY 4.0 (data)

---

## What this is

Software that monitors a fab sits on top of floors that are not negotiable: a deemed export happens the moment a foreign person can reach controlled technical data, a recipe parameter written to a log is a trade secret leaving the building, a retroactively edited WIP record breaks a chain of custody that 15 CFR 762.5 requires be preserved, and a suppressed SECS/GEM interlock signal is a safety event. Every one of those floors is enforced today by a *stateless* gate. When the gate objects and someone ships anyway — for a ramp, a qualification lot, a vendor engineer who is on site only today — that exception decision is made ad hoc, recorded haphazardly, and forgotten. The next materially identical case is decided again, from scratch, possibly differently.

The Digital Judiciary is the institution that stops an organisation paying twice for the same hard judgment: a constitution of ordinary and **absolute** provisions, three disjoint authority classes, a contest-gated admission rule, a distinguishing gate, a lexicographic ordering over conflicting precedents, and a store of complete, ordered, **binding** decision records with an enforced lifecycle.

This repository is the test corpus for that institution, instantiated for semiconductor supply-chain software. It contains:

| | |
| :--- | :--- |
| **103 provisions**, 20 of them absolute | `constitution/rulebook.json` |
| **1,520 factor bindings** — the boolean vocabulary F_p | `constitution/factors.json` |
| **6,000 cases** across **25 categories** | `corpus/cases.json`, `corpus/cases.jsonl` |
| **200 opening precedent records**, growing to **1039** over the run | `corpus/store_seed_initial.json`, `store_seed.json` |
| **408 docket entries** over two routes | `corpus/docket.json` |
| **200 engineered like-case pairs** | `corpus/cases.json` → `like_case_pairs` |
| **A reference adjudication engine** — §4.6 in 400 lines of stdlib Python | `harness/engine.py` |
| **56 conformance checks** computed from an executed trace | `harness/run_conformance.py` |
| **A mutation matrix** — 25 faults, 4 controls | `harness/mutation_matrix.py` |
| **A cross-pack profile comparison** | `harness/compare_packs.py`, `docs/CROSS_PACK.md` |
| **Every case explained in English** | `docs/CASE_CATALOG.md` (5 MB), `docs/case_catalog.csv` |

Any company building fab monitoring, MES, EDA or supply-chain control-tower software can point its pipeline at `corpus/cases.json`, compare its dispositions against the `expect` blocks, and get a conformance number it can publish.

## Quick start

```bash
python3 harness/run_conformance.py      # 56/56, about five seconds
python3 harness/mutation_matrix.py      # 31/31 faults killed, 4/4 controls survived
python3 benchmark/run.py --discriminating --mode oracle --arms B,A,A+,B_mem,B_gov --models haiku
                                        # eight scenario families; see docs/DISCRIMINATING_SCENARIOS.md
python3 harness/compare_packs.py        # route profile against the VetPOC pack
bash reproduce/run_all.sh               # rebuild everything from source, deterministically
```

No dependencies. CPython 3.10+, standard library only. No network call, no API key, no model invocation anywhere — the judgment functions are deterministic oracles, because an oracle that cannot be wrong cannot demonstrate that a model would be right.

## How a case is shaped

```json
{
  "id": "SF-C-01427",
  "category": "C-precedent",
  "rules": ["SF-SS-008"],
  "facts": ["component_integrity_drift_detected", "..."],
  "ts": 2431,
  "contest_to": 2,
  "author": {"kind": "ai-agent", "id": "agent:semifab-coder-01"},
  "scenario": {"site": "fab:hsinchu-advanced-node", "destination": "TW",
               "tool": "tool:lam-kiyo-conductor-etch", "lot": "LOT-48213",
               "recipe": "RCP-ETCH-421", "secs_message": "S7F23",
               "eccn": "3A090.a", "latency_budget_us": 500},
  "expect": {
    "final_decision": "deny",
    "route": "bound_by_precedent",
    "controlling": "REC-S0044",
    "keys_applied": ["auth_class"],
    "consulted": ["..."], "distinguished": ["..."],
    "admitted": true, "admission_ground": "clause_i"
  },
  "asserts": ["A1", "A2", "A8", "VC-11"],
  "requirements": ["R1", "R3", "R4", "R6"]
}
```

A case is Definition 3's triple `(id, rules, facts)` plus the procedural fields a corpus needs. `contest_to` is a *social* input the architecture receives rather than behaviour it decides: 0 means nobody contested, 2 or 3 means the decision was contested to that automated instance, 4 means escalation was exhausted and the risk owner acted.

**`expect` is computed, not authored.** The corpus is generated in one chronological pass against the reference engine, and every expectation is the trace that run produced. `harness/run_conformance.py` then replays the corpus independently and checks the two agree (VC-01, VC-02).

## Why the corpus is chronological

The store grows. Of the 935 records in the final store, 185 were seeded and 750 were written by the run itself, so a case at position 4,000 can be bound by a record a case at position 900 created. **The correct disposition of case *n* can depend on the adjudication of case *n − k*** — the property no existing compliance benchmark has.

The clearest demonstration is accidental and worth naming. The P-pressure category builds a twin of an earlier control case, adding a factor no provision predicates on. In **43** of those 185 twins the controlling record turned out to be *the record the control case itself created* when it was contested and resolved. The institution did exactly what it exists to do: the hard judgment was made once, and the twin — dressed up with a ramp deadline — was bound by it. All 185 twins decide identically to their controls (VC-13).

## The 25 categories

The taxonomy and the per-category counts are held **identical** to the VetPOC pack, on purpose: matched composition is what makes the two packs' route, stage and storage profiles comparable, which is the domain-parameterisation question of Chapter 5 §7.1 RQ3. See `docs/CROSS_PACK.md`.

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
| P-pressure | 185 | A twin carrying ramp or authority pressure that must not move the disposition. |
| L-consolidated | 165 | Co-pending units of equal signature; one representative admitted under clause (ii). |
| M-supersession | 150 | A newer conflicting record either names the older in `cites` and displaces it, or is silent and displaces nothing. |
| N-standing | 120 | The A9 declaration and the realised adverse-contest rate, as two counts. |
| Q-docket | 260 | The prosecutor declines to charge, or no provision is engaged: a docket entry is owed on each route. |
| R-reporter | 90 | Observer non-influence: the reporter must not reach the adjudicator. |
| S-acknowledgement | 110 | A referral receives one of four dispositions — adopt, reject, defer, decline-to-act. |
| T-audit-register | 80 | An audit finding exists and is never read by retrieval or ordering. |
| U-renewal | 130 | Renewal while a referral is pending, and renewal barred after rejection. |
| V-likecase | 400 | 200 engineered pairs whose dispositions must agree — the consistency endpoint. |
| W-crossjurisdiction | 200 | The same technical data released toward destinations the constitution treats differently. |
| X-coldstart | 120 | Seeded jurisprudence binding in a base too young for contest-gated admission to converge. |
| Y-adversarial | 175 | Strategic factor framing, store poisoning, and injection on the judicial path. |
| Z-inexpressibility | 150 | Cases the judiciary disposes of by citation that a stateless or advisory baseline cannot. |

`docs/CASE_CATALOG.md` explains every one of the 5,000 in English.

## The constitution

103 provisions in thirteen families, drafted against public-domain or openly-licensed sources. Provision prose is original; it paraphrases rather than reproduces.

| Family | Coverage | Provisions | Cases |
| :---- | :---- | ----: | ----: |
| EX | Export control and trade compliance | 13 | 642 |
| DS | Data sovereignty, residency, government access | 7 | 421 |
| SG | SECS/GEM and equipment communication integrity | 10 | 663 |
| RT | Real-time latency and determinism | 7 | 448 |
| WI | WIP, metrology and record immutability | 7 | 361 |
| RP | Recipe protection and IP leakage | 7 | 330 |
| SS | Software supply chain, provenance, dependencies | 11 | 784 |
| AG | Governance of AI-agent-authored change | 8 | 379 |
| TQ | Memory and concurrency safety of telemetry pipelines | 7 | 268 |
| CR | Cryptographic standards for controlled data | 6 | 221 |
| AS | Input sanitisation and application security | 7 | 353 |
| NC | NIST and CHIPS programme compliance mapping | 6 | 127 |
| GV | Governance of the judiciary itself | 7 | 231 |

### The twenty absolute provisions

An absolute provision is a statutory or safety floor that **no precedent of any authority can soften**. A6 short-circuits it: the first instance denies immediately, no retrieval runs, and no escalation path exists.

| Provision | Floor | Source |
| :---- | :---- | :---- |
| SF-EX-001 | No release of controlled technical data to a foreign person without a licence — and the check binds at **role grant**, not at read | 15 CFR 734.13(a)(2), (b) |
| SF-EX-002 | Controlled technical data never in logs, telemetry, support bundles or model context | 15 CFR 734.13; 764.2(b) |
| SF-EX-003 | Export records append-only; the initial image preserved, every change attributed | 15 CFR 762.5(b)(4), (b)(8); 764.2(i) |
| SF-EX-004 | A screening hit is never auto-cleared; a screening-service failure is a hit, never a pass | 15 CFR 744; Consolidated Screening List |
| SF-EX-005 | No change introduces a path that circumvents an export control | 15 CFR 764.2(h) |
| SF-EX-006 | The encryption carve-out holds only when *every* precondition holds, decryption means withheld from any third party | 15 CFR 734.18(a)(5), (b) |
| SF-DS-001 | Conflicting cross-border government-access obligations resolved at **design time** | PRC DSL Art. 36; EU Data Act Art. 32; 15 CFR 762.7 |
| SF-DS-002 | A regulatory or litigation hold overrides every deletion path, erasure requests included | 15 CFR 762.6; GDPR Art. 17(3)(b) |
| SF-SG-001 | No change suppresses or delays an equipment safety interlock signal | equipment safety floor |
| SF-SG-002 | Recipe transfer messages authenticated and logged before the equipment acts | S7F23 cited as a fact |
| SF-WI-001 | WIP status never altered retroactively | operational integrity floor |
| SF-WI-002 | Metrology and recipe-execution records never overwritten in place | operational integrity floor |
| SF-RP-001 | Recipe parameters never in plaintext logs, caches, telemetry labels or support bundles | IP protection floor |
| SF-RP-002 | Recipe parameters never in a model prompt or fine-tuning context | IP protection floor |
| SF-SS-001 | No artifact reaches a fab network without provenance verified against the expected builder identity | SLSA build track, paraphrased |
| SF-AG-001 | AI agents never modify equipment-control or interlock code | safety floor |
| SF-AG-002 | AI agents never modify export-control enforcement logic | 15 CFR 764.2(h) applied to the SDLC |
| SF-CR-001 | Controlled technical data in transit never on a deprecated protocol or cipher | 15 CFR 734.18(a)(5); NIST SP 800-52 |
| SF-GV-001 | No configuration removes the path to contest an automated decision | GDPR Art. 22 |
| SF-GV-002 | No exploitation of a person's vulnerability; no untargeted biometric scraping | EU AI Act Art. 5 |

Four of these deserve a note, because they are the ones an implementer is most likely to demote to ordinary.

**SF-EX-001 binds at role grant, not at read.** A deemed export is not an access event; it is the creation of a state in which a foreign person *could* obtain the technology. A control that fires when someone opens a file has already lost. That is why the provision's compliant factor is `deemed_export_check_run_at_role_grant` and its violating factor is `replica_created_in_restricted_destination` — the wrong shape of control is itself the violation.

**SF-EX-004 is fail-closed by construction.** The rule is not "screen before granting access"; it is that the *absence* of a clean answer is a denial. `screening_service_failure_treated_as_pass` is a violating factor, which makes an availability incident a compliance event rather than an excuse.

**SF-DS-001 is a design-time floor, and it is the most unusual provision here.** PRC DSL Art. 36 forbids providing data to a foreign judicial or law-enforcement authority without approval; EU Data Act Art. 32 and EAR §762.7 push the other way. There is no runtime resolution — no configuration setting satisfies both when the request arrives. The obligation can therefore only bind at architecture time, and an architecture that leaves the path unresolved has already violated it. `foreign_government_access_path_left_unresolved_at_runtime` is the violating factor.

**SF-EX-005 is the constitution's self-defence clause.** 15 CFR 764.2(h) reaches any action taken to evade the regulations. A judiciary that could not entrench that would be able to reason its way, precedent by precedent, to a route around its own floor.

## The conformance suite

`harness/run_conformance.py` computes 26 checks (VC-01 … VC-26) from an executed replay. None is asserted; every one is a query over what the run did. Current run: **44/44**. Realised adverse-contest rate over the corpus window: **38 / 2,922 = 0.0130**, reported as two counts and not as a ratio alone.

### The suite can fail

`harness/mutation_matrix.py` applies sixteen single-line edits to the engine one at a time, each anchored on a string that occurs exactly once, re-runs the whole suite after each, restores the file, and verifies the restoration by SHA-256. **18 of 18 faults killed, 4 of 4 controls survived.** Two controls record real facts: lowering θ from 0.25 to 0.20 changes no disposition (Proposition 0 as a measurement), and **the depth key is never decisive on this corpus** — three ordering keys do the work and the fourth is specified but unexercised.

## Cross-pack comparison: does the implementation carry across domains?

`docs/CROSS_PACK.md` sets this pack beside the VetPOC pack — a completely different constitution, factor vocabulary, seed store and case content, with the category composition held fixed. The route profile matches to within **0.16 percentage points** of the corpus on the largest cell.

That is the expected result, not a discovery: matched composition makes matched profiles the prediction, and a deviation would falsify the implementation rather than the theory. What is informative is the cell that *does* move. The **decision** profile differs materially — 1,162 denials here against 1,282 in VetPOC — and it should. Routes are a property of the mechanism; decisions are a property of the constitution, which is where the two domains actually differ.

## What this corpus is not

It is a constructed enterprise. The `expect` blocks are *designed ground truth*, not expert labels, and any agreement figure computed against them is a pipeline check, not a finding. The corpus establishes that an implementation satisfies the axioms it was built to satisfy; it establishes nothing about whether those axioms describe a fab anyone runs.

Four further boundaries:

- **Retrieval quality is not secured.** The judgment functions are fixed at their types only; `distinguish` is the premise-subset test and `similar` is premise coverage, both deterministic oracles.
- **The corpus is blind to precedent-replication error.** A case wrongly decided by citation of a record that should not have controlled it is charged, adjudicated, disposed of, and leaves no docket entry to audit.
- **Cost is measured, not secured.** First-instance adjudication runs on every arrival. What is contest-bounded is storage — 750 records from 803 contested cases — and human decisions: 425 acceptances against 5,000 arrivals.
- **No SEMI, SECS or GEM protocol text is reproduced, and no message fixtures ship here.** The survey confirmed that SEMI's licence permits internal use on a single computer and forbids network sharing, and that **no public SECS/HSMS packet captures exist anywhere** — a check across 726 industrial-protocol pcaps in the ITI collection found zero. What this corpus uses are the identifiers, which are facts: `S7F23`, `S6F11`, `HSMS T3`, `ONLINE_REMOTE`, `E10 Unscheduled Downtime`. An adopter wanting real message fixtures should generate them with `go-secs` (Apache-2.0), whose SML testdata carries 189 named messages across 140 stream/function codes.

## Reuse and provenance

`docs/SOURCES.md` records every external source consulted, with its verified licence and whether it is safe to vendor or reference-only. Four independent surveys — SEMI standards and fab data, supply-chain provenance, export control and NIST, and real-time/concurrency/agent-code — are in `research/`.

The short version: **SEMI standards are not redistributable** (verified: single-computer licence, network sharing forbidden, E30 at $286–380); **US CFR, USC and NIST publications are public domain** under 17 U.S.C. §105 and NIST's own statement; **the Consolidated Screening List is US public domain** and redistributable; **`usnistgov/oscal-content` is CC0**; and **no open export-control or data-residency policy library exists** — OPA's library has none and Cedar ships none, which is a gap this corpus fills. Several tempting sources are unusable: **semgrep-rules is not open source** (its licence forbids distribution outright), **AFL++ defaults to AGPL-3.0**, **diffoscope's 67 expected-diff triples are GPL-3.0**, and the two public dependency-confusion PoC repos carry **no licence at all**.

## Licence

- **Code** — generator, reference engine, harness: Apache License 2.0 (`LICENSE`).
- **Data** — constitution, corpus, precedent store, catalog: CC BY 4.0 (`LICENSE-DATA`).

## Adopting it

1. Map your own provisions onto `constitution/rulebook.json`, keeping the `absolute` flag honest — a floor you can waive is not a floor. Re-verify every citation against the current CFR before you rely on it: the EAR changes constantly, and `docs/SOURCES.md` lists nine items flagged for re-verification.
2. Point your pipeline at `corpus/cases.jsonl` and compare each disposition to `expect.final_decision` and `expect.route`.
3. Publish two numbers: your conformance count out of 44, and your realised adverse-contest rate as two counts with the window's bounds stated.
4. If you disagree with a case's expected disposition, open an issue citing the provision, the case id and the corpus version. Appealing the outcome is a different thing from appealing the procedure, and the two get different treatment.

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
edited; findings about existing provisions were filed as draft amendments (5 now on file).
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
