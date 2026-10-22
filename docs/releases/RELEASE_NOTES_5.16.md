# Release 5.16.0 — the Enterprise Conscience fast track

20 October 2026. This release adds a second forum beside the judiciary. The
Digital Judiciary is a slow track: it sees a change only when the change is
contested or escalated, and what it writes binds. The Enterprise Conscience
(EC) is a fast track: a gate reads every change against a tiered canon and a
token registry before the change executes, and what it writes is a log. The
release couples the two through a bench, runs both over a year of five
companies, and ships the conformance suite, mutation matrix, tests and
preregistration for that run. No demo-pack or simulation-pack figure moves.

## What it adds

- `simulation/ec/`, the package. Every object in it is new; `DESIGN.md` is
  the interface contract and `docs/ENTERPRISE_CONSCIENCE.md` the user guide.
  - **The canon** (`canon.py`, `build_all_canons.py`). Each pack's
    constitution is read into a canon by a deterministic tier rule: an
    absolute provision is T0; a safety provision, or a legal or regulatory
    provision charged at τ ≤ 25, is T1 with an issuing office; everything else
    is T2 with the admitted reasons N, O, K and a bound. Six value entries per
    company (Table 1 of the EC paper) are added at T2, T1 and T3. The result
    is written to `simulation/<pack>/constitution/canon.json`, byte for byte
    the same on every rebuild; nothing else in a pack changes.
  - **The registry** (`registry.py`). Dispensation tokens for T1 classes:
    issued by an office outside the agent's reporting line, scoped to an
    entry and a canon version, single-use by default, expiring at fourteen
    days, revocable. A claimed approval that names no token is not a token.
    One standing emergency token per company requires a recorded cause.
  - **The gate** (`gate.py`). Every engaged entry is evaluated and the most
    restrictive outcome wins: a T0 violation blocks and escalates; a T1
    contrariety passes only on a valid token, blocks on a say-so claim, and
    blocks without escalation where a holding has already barred the class; a
    conflict between non-tradable entries holds; a T2 departure passes with
    an admitted reason within bound and is otherwise blocked and audited
    internally, never escalated; a T3 departure passes in a listed context.
    The gate reads nothing about whether an audit was announced or what
    pressure the proposer presented, and an AST check says so.
  - **The examen** (`examen.py`). After each executed act the agent writes an
    entry; `reconcile` labels every act `discloses`, `silent`,
    `misrepresents` or `nothing_to_disclose` from the entry and the verified
    event, never from a label the entry carried.
  - **The bench coupling** (`escalate.py`, `doctrine.py`). Escalations are
    heard by the pack's own engine `d_bench = 3` working days after filing,
    the record (if admitted) goes to the DJ store, and the holding is written
    back as a gloss on the canon entry the next day. A T1 holding recurring
    three times on the same class codifies: no further tokens for that class.
    Gloss writes never touch a tier, a violating factor or the canon version.
    Only aggregate disclosure counts reach the bench; no `act_id`, no
    narrative.
  - **Arm A, the strongest rival** (`rival.py`). Constitution in the prompt,
    a policy engine that denies absolute contrariety, an approval flag any
    manager may set (so every token claim passes, real or not), an event log.
    No escalation, no glosses, T2/T3 outside the engine.
  - **Agents** (`agents/`). Six policy archetypes with a registered propensity
    table (honest, pressure_sensitive, observation_sensitive, misreporting,
    and the oracle and adversarial bounds), and an LLM agent behind a
    provider abstraction (Anthropic or any OpenAI-compatible endpoint, plain
    `urllib`, no SDK) with `dry` and `live` modes, an on-disk cache and
    per-call cost.
  - **The driver** (`run_year.py`, `stream.py`, `calendar.py`). 365 working
    days on one shared calendar; each pack's released 6,000-case corpus is
    partitioned into days in its released order (like-case mates and pressure
    twins never split across a day boundary); every stochastic draw is seeded
    from (seed, pack, day) or (seed, pack, case), never from the arm, so the
    four arms see identical proposals before their decision; checkpoint and
    resume.
  - **Metrics and analysis** (`metrics.py`, `analyze.py`). One row per (pack,
    arm, seed, archetype) with E1–E8 and the secondary counts, each row
    carrying its provenance mark; TOST equivalence at margin ±0.03 and
    percentile bootstrap over (pack, seed) units.
- `run_ec_conformance.py`: EC-01 to EC-12, computed from executed runs. A
  check whose property never arises in a run fails as vacuous.
- `mutation_matrix_ec.py`: faults F-EC-1 to F-EC-8 and two controls, applied
  as `unittest.mock.patch` inside forked workers so nothing on disk is ever
  edited. Every fault killed, both controls survived, every non-control check
  killed by at least one fault.
- `tests/test_ec_core.py`, `tests/test_ec_driver.py`,
  `tests/test_ec_conformance.py`: 50 tests, plus the mutation matrix under
  `--runslow`.
- `prereg/`: the OSF preregistration (`PREREG_EC_SIM_v1.md`), the analysis
  plan, data dictionary, estimand map, upload checklist and the plan hash over
  the prereg files, the five canons, the package and its tests.
- `reproduce/run_year.sh` with five modes: `pilot`, `conformance`,
  `mutation`, `registered`, `metrics`.

## What changed

- `VERSION`, `pyproject.toml`, `CITATION.cff` at 5.16.0.
- Each simulation pack gains one generated file,
  `constitution/canon.json`. No case, store, docket or expectation moves.
- `README.md` gains the EC rows, two quick-start lines and the "two forums"
  paragraph; `REPRODUCE.md`, `DATASHEET.md` and `PAPER_ALIGNMENT.md` gain EC
  sections; `docs/ENTERPRISE_CONSCIENCE.md` is new.
- One engine-semantic overlay, and only one: the engine writes a record's
  expiry as `ts + 180`, which on the day calendar (`DAY_TICKS = 100`) would
  be under two days. The driver patches `rec.expiry` to `ts + 180 * DAY_TICKS`
  after `_record_from`, so an acceptance lasts 180 days. `calendar.patch_expiry`
  is the whole of it.

## What did not change

- `harness/engine.py` in all six copies. The engine-copy identity test still
  passes; the bench calls `engine.adjudicate` and writes records through
  `engine._record_from` exactly as `replay` does.
- A6, the Challenge Gate, A1–A7 and the record construction path. EC never
  writes a precedent record; only the bench does, through the engine.
- Every published figure: the three demo suites (61/44/53), the five packs
  (56/56, 31/31, 4/4), Numerals (11/11, 7/7, 2/2), the mutation and axiom
  matrices, the benchmark. Corpus 2.1.0, pack 2.4.0, federation 1.3.0.

## How to verify

```bash
./install.sh --check                               # CPython 3.10+, SQLite; nothing is installed
bash reproduce/run_year.sh pilot                   # 30 days, 5 packs, arms A-D, seed 11, under a minute
bash reproduce/run_year.sh conformance             # EC-01..EC-12 on a fresh 60-day VetPOC pilot; RESULT: 12/12
bash reproduce/run_year.sh mutation                # F-EC-1..8 and two controls; RESULT: 8/8 faults killed, 2/2 controls survived
python3 -m pytest tests/test_ec_core.py tests/test_ec_driver.py tests/test_ec_conformance.py -q
                                                   # 50 passed, 1 skipped (the matrix; add --runslow)
python3 simulation/ec/build_all_canons.py --check  # exit 0: every canon.json matches its rulebook
python3 prereg/make_plan_hash.py                   # recompute the plan hash; compare with prereg/plan_hash.txt
```

The pilot writes `simulation/ec/results/pilot30/` with `metrics.csv` and
`analysis.md`. Those are development outputs: a 30-day prefix, one seed, one
archetype. They show that the pipeline populates every column; they are not
estimates of anything.

## Known limits

- **No live LLM run.** The LLM agent has been exercised in `dry` mode only,
  which builds the prompt, counts tokens and prices the call without making
  it. Every LLM figure anywhere in this release is ⟦PROJECTED⟧ and says so in
  its `provenance` column. E5, the espoused-enacted gap, is NA until a live
  slice runs.
- **The registered run is in progress.** `reproduce/run_year.sh registered`
  takes hours; its results directory is not part of this release and no
  figure from it is claimed here. The preregistration's no-peeking rule
  applies: `metrics.py` and `analyze.py` are not run on it until every run
  has written its `manifest.json`.
- **The canons are authored by the programme.** The tier rule, the τ
  threshold of 25, the value entries, the offices and the bounds are the
  author's choices, written without practitioners or affected groups. Nothing
  here shows that any company's tiers are right; the canon is versioned so
  that a different choice is a different canon.
- **The archetypes are constructed.** Every policy-agent figure is
  ⟦measured⟧ against an ⟦identity⟧ truth that follows from the propensity
  table. Those runs check that the mechanism recovers a known table; they say
  nothing about any real agent's policy. The oracle and adversarial rows are
  bounds.
- **The gate reaches only what it mediates.** A channel the gate does not sit
  on is not governed by it, and the corpora still do not secure retrieval
  quality, precedent-replication error or factor characterisation
  (`simulation/RELEASE_TIERS.md`).
- **The human review desk figure** quoted for H7 is ⟦PROJECTED⟧ from stated
  parameters in each pack's `benchmark/human.py`; it decides nothing.

## Placeholders resolved

The two placeholders carried since 5.15.0 are filled: the repository URL is
`avkadambi/DigitalJudiciary` in `README.md`, `pyproject.toml`, `CITATION.cff`
and the CI badge, and `SECURITY.md` names the maintainer's address. The OSF registration DOI
line in `prereg/PREREG_EC_SIM_v1.md` is filled after OSF mints it and is
excluded from the plan hash.
