# Datasheet — the Digital Judiciary conformance corpora

**Version 5.16.0 · 20 October 2026 · code Apache-2.0 (`LICENSE`), data CC BY 4.0 (`LICENSE-DATA`)**

> Part I describes the 144-case demo conformance packs (`demo/companies/`). Part II, added in 5.9.0, describes the five 6,000-case simulation corpora (`simulation/`), which are the corpora the benchmark paper runs on. Part III, added in 5.16.0, describes the Enterprise Conscience overlay (`simulation/ec/`): the canons and the data the registered year run generates.

# Part I — the demo conformance packs

Written to the datasheets-for-datasets pattern. Every answer states what is known and says so
where nothing is.

## Motivation

**Why was it created?** To exercise every clause of a nine-axiom contract for binding precedent in
automated compliance decisions, so that conformance is computed from executed traces rather than
asserted. It is a *conformance* corpus first and an evaluation corpus second.

**Who created it?** Arun Kadambi and Venkat Kuppuswamy, for the dissertation *The Digital
Judiciary*. No external funder.

## Composition

**What do the instances represent?** Synthetic compliance cases in four fictitious enterprises —
a supply-chain control tower, a veterinary practice platform, a data-centre monitoring service and
a model lab — plus a fifth reference pack, `fintech`, that ships unexecuted.

**How many?** 144 cases per executed pack (576 across the four), 68 in `fintech`. Thirteen
categories: routine, plain-deny, precedent-governed, ordering-conflict, distinguishable,
absolute, lapsed-authority, risk-owner, control-plane, novel, tie, pressure, and consolidated
(the eight L-consolidated cases per pack added in 5.7.0).

**Is any of it real?** The *cases* are entirely synthetic. The **provisions are not**: the absolute
floors restate operative law — EU AI Act Article 5, GDPR Articles 7, 9 and 33, NIS2 Article 23,
NIST SP 800-53 controls, 19 CFR 163, SEC 17a-4 and FINRA 4511. That mixture is the point and it is
also the reason for the dual-use note below.

**Does it contain personal data?** No. No real person, company, transaction or record appears.
Named parties are invented.

**Is anything missing?** Yes, and it is stated rather than implied. The corpus precompiles the
hardest step of real adjudication: cases arrive as factor vectors, so the work of characterising a
messy fact pattern into a decidable representation has already been done. Nothing here measures
that step, and the manuscripts say so.

## Collection

**How was it gathered?** Authored, not collected. Case seeds were written by the authors against
each pack's rulebook; the `P-pressure` category was derived from the nine scored mechanisms in PACT
(Okamoto & Erol 2026, Table 14); the Absolute Rules Corpus extension derives its provisions from
named instruments under a published four-criterion absoluteness test.

**Was it reviewed?** By the authors and by the conformance suites, which is not the same as
independent review. **A second labeller has not been engaged and no inter-rater statistic is
reported.** The protocol for doing so ships as `SECOND_LABELLER_PROTOCOL.md`; the measurement
itself is outstanding and is recorded as an open item.

## Preprocessing

Two extensions were applied to the original 101-case packs and both ship as idempotent scripts:
`demo/build_corpus_extension.py` (Absolute Rules Corpus, 101 → 127) and
`demo/build_pressure_extension.py` (P-pressure, 127 → 136). `store_seed.json` is regenerated from
an executed replay. Six `expect.controlling` identifiers were repaired on 1 September 2026 from the
ordering rule and the packs' own scope data, never from executed output; the repair is recorded at
Appendix C item 11.

## Uses

**What is it for?** Verifying that an implementation honours the contract; comparing governed
precedent against ungoverned per-case review; and reproducing every executed figure in the
dissertation.

**What should it not be used for?** See the dual-use note. In particular it is not a measure of
real-world compliance rates, and no figure in it generalises to a deployed enterprise.

## Distribution and maintenance

Apache-2.0 for code and CC BY 4.0 for data (earlier versions of this file said MIT; the licence files at the repository root are authoritative). Every released item embeds a canary GUID so future training-set
contamination is detectable. Maintained by the authors; the replication package carries the
version, and `REPRODUCE.md` maps every reported figure to the command that regenerates it.

# Part II — the simulation corpora (corpus 2.0.0; 2.1.0 since release 5.14.0 — one plain denial in five contested and lost, writing deny-side records)

**Why were they created?** To execute, rather than author, five enterprise-scale streams of
software changes under written constitutions, so that the architecture's behaviour can be
measured across domains at identical category composition, and so that the benchmark paper's
arms decide the same stream.

**What do the instances represent?** Proposed development changes — what a reviewer sees in a
pull request — in five invented organisations: VetPOC (veterinary practice software), SemiFab
(semiconductor fab monitoring and supply-chain control tower), FrontierLLM (a frontier model
developer), DCVigil (multi-tenant data-centre monitoring and AIOps) and Meridian Financial
(regulated fintech). Not runtime business transactions (VC-49).

**How many?** 6,000 cases per pack, 30,000 in all, over 25 categories held identical across
packs; 121–142 provisions per constitution (26–33 absolute); 240 like-case pairs and 222 PACT
pressure twins per pack; 39 scenario classes mapped onto every provision.

**Is any of it real?** The organisations, services, people and changes are invented. The
provisions cite operative law and standards by identifier (US CFR/USC, EU regulations, PCI
DSS, ISO, IEC, SEMI, NIST — identifiers only where the text is not reusable); each pack's
`docs/SOURCES.md` records every source with its licence position, and each pack's
`proposed_amendments.json` records where a cited instrument has moved. Every provision needs
counsel review before it governs anything.

**How was ground truth produced?** Computed, never authored: one chronological pass of the
reference adjudicator (`harness/engine.py`, the architecture paper's §4.6) produces every
disposition, route, controlling record and consulted set; an independent replay in
`harness/run_conformance.py` reproduces them (VC-01, VC-02). Zero construction anomalies in
every pack.

**What checks it?** 50 conformance checks per pack computed from executed traces, and a
25-fault / 4-control mutation matrix showing the checks can fail. Scenario coverage is computed
by VC-50 from the corpus as built.

**What is missing, and said so?** Factor characterisation is precompiled (cases arrive as factor
vectors); retrieval quality and precedent-replication error are not secured; the second labeller
has not been engaged; no figure about a model exists until `--mode live` runs; the human arm is
priced from stated parameters and decides nothing. `simulation/RELEASE_TIERS.md` and
`PAPER_ALIGNMENT.md` carry the full statement.

**Distribution and maintenance.** Each pack ships as its own archive under `simulation/zips/`
with SHA-256 digests in `simulation/MANIFEST.json`; a canary GUID is embedded in every case;
versioning is release / pack / corpus (5.14.0 / 2.4.0 / 2.1.0).

# Part III — the Enterprise Conscience overlay (release 5.16.0)

**Why was it created?** To run the evaluation the Enterprise Conscience paper (Sect. 4.5,
OR3) specifies and leaves unestimated: a tiered canon, a conscience gate on every change, a
token registry and an examen log, beside and coupled to the judiciary, over a year of five
companies, under a preregistered design (`prereg/PREREG_EC_SIM_v1.md`).

**What is new data?** Three things. The **canons**: one generated
`constitution/canon.json` per pack, 121–142 provision entries tiered T0–T3 by the rule in
`simulation/ec/canon.py` (every absolute provision is T0; 144 absolute provisions across the
five packs, all T0) plus six value entries per company at the tiers the EC paper gives them,
with offices and one standing emergency token class. The **overlay** on each arrival: the
engaged value entries, the presented driver and its level, the announced audit twin (one in
four ai-agent arrivals), the conflict flag (2% of arrivals engaging two or more T0/T1
entries), the daily token issuance. The **agent draws and what follows them**: the act the
agent proposes, the gate's verdict, execution, the examen entry, the escalation filing and
hearing, the gloss and codification, the reconciliation label. Every draw is seeded from
(seed, pack, day) or (seed, pack, case), never from the arm.

**What is not new data?** The DJ stream. Each company's cases are the released 6,000-case
corpus of Part II at corpus 2.1.0, in its released order, partitioned into 365 working days
(a like-case mate or a pressure twin is never split across a day boundary). No case, fact,
expectation, store seed or docket is changed; arm B's store trajectory equals the engine's
own replay of the calendar-mapped cases (EC-12).

**Is any of it real?** No more than Part II: the companies, agents, offices and tokens are
invented. The canons are authored by the programme through a rule, without practitioners or
affected groups; the tier of a value entry and the τ threshold of 25 for a T1 legal or
regulatory provision are canon decisions, versioned with the canon. The policy archetypes
are constructed propensity tables; every figure from them is ⟦measured⟧ against an
⟦identity⟧ truth and says nothing about any real agent.

**How was ground truth produced?** Computed. Impermissibility is `run_year.impermissible()`
over the act, the canon and the registry; disclosure labels are `reconcile` over the entry
and the verified event; neither reads a label the agent or the driver carried. Twelve
conformance checks compute their properties from the executed runs and an 8-fault, 2-control
mutation matrix shows they can fail (`docs/ENTERPRISE_CONSCIENCE.md`).

**What is missing, and said so?** No LLM has been run live: the LLM agent exists in `dry`
mode only and every LLM figure is ⟦PROJECTED⟧. The registered run is in progress and none of
its results is in this release. The gate reaches only the channel it mediates. Part II's
limits (characterisation precompiled, retrieval quality and precedent-replication error
unsecured, no second labeller) carry over unchanged.

**Distribution and maintenance.** The canons ship in each pack's `constitution/` under
CC BY 4.0 and are pinned by the plan hash in `prereg/plan_hash.txt` together with the
package and its tests. Run outputs follow `simulation/RELEASE_TIERS.md`: `metrics.*`,
`analysis.*`, `summary.json`, `manifest.json` and `bench_log.json` public; per-unit stream
exports (`run.jsonl`, `registry.json`, `store_final.json`, `glosses_final.json`, the LLM
cache) at the trusted-contributor tier. Versioning is release / pack / corpus / canon
(5.16.0 / 2.4.0 / 2.1.0 / `<pack>-canon-000001`).
