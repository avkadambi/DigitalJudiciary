# The Digital Judiciary

**Binding, contest-gated precedent for automated compliance decisions — the reference
implementation, five executed simulation corpora, and the benchmark harness.**

[![ci](https://github.com/OWNER/digital-judiciary/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/digital-judiciary/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey.svg)](LICENSE-DATA)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

When an automated gate decides whether a software change may proceed, it decides the
same question thousands of times. The Digital Judiciary treats those decisions as a
court would: a **constitution** of provisions (some absolute), an **evaluator** that
characterises each change into facts, a **prosecutor** that retrieves and gates
precedent and decides whether there is a case, a **judge** that decides it, and a
**store** of records that bind later decisions — entered only when a decision was
**contested** and resolved above first instance. Precedent is distinguished on the
record's own recorded reasons, ordered by authority, recency and scope, and can never
override an absolute provision. Everything the institution does leaves a trail a
reader can reconstruct.

This repository is the artefact behind the programme's papers (see
[`PAPERS.md`](PAPERS.md)). Every figure they report regenerates from it, offline, with
no third-party dependency.

## Quick start

```bash
git clone https://github.com/OWNER/digital-judiciary && cd digital-judiciary

# 1. Every demo-pack figure the architecture and case-base papers report (~2 min)
DJ_JUDGE_MODE=oracle DJ_DEV_KEYS=1 DJ_GITHUB_ALLOW_UNSIGNED=1 bash reproduce/run_all.sh

# 2. The five 6,000-case simulation packs and the Numerals federation (~10 min)
bash reproduce/run_all_simulation.sh

# 3. The benchmark harness, offline (no API key; exercises the harness, not a model)
bash reproduce/run_benchmark.sh

# 4. The Enterprise Conscience fast track: a 30-day pilot of five companies under four arms (~1 min),
#    then its twelve conformance checks on a fresh 60-day pilot (~30 s)
bash reproduce/run_year.sh pilot
bash reproduce/run_year.sh conformance

# 5. The same, as a test suite
pip install pytest && python -m pytest tests -q
```

Requirements: CPython 3.10 or later and SQLite (both ship with Python). Nothing is
downloaded. `./install.sh --check` verifies the capabilities the ledger relies on.

To run the service itself — a single-container adjudicator with a REST API and a
review screen — see [`docs/OPERATOR_NOTES.md`](docs/OPERATOR_NOTES.md):

```bash
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=_all python3 serve.py     # or: docker compose up
```

## What is here

| Path | What it holds |
| :-- | :-- |
| `app/` | The contract as code: schema and immutability triggers, kernel (registry, constitution, ledger, challenge gate, provenance chain), the two judgment functions (`similar`, `distinguish`) with deterministic oracles and an optional model mode, adjudication and escalation, the A7 lifecycle sweep, the REST surface, the GitHub inbound lane, the review UI. |
| `demo/companies/` | The four frozen 144-case demo conformance packs the architecture papers report on (sctower, vetpoc, dcvigil, frontierllm) and the fintech pack. Their figures are unchanged since 5.7.1. |
| `run_conformance.py`, `run_interface_conformance.py`, `run_extension_conformance.py` | The three demo suites: 61, 44 and 53 checks computed from executed traces. |
| `reproduce/` | The scripts that regenerate every published number: `run_all.sh` (demo), `run_all_simulation.sh` (packs), `run_benchmark.sh`, `run_year.sh` (the EC year: pilot, conformance, mutation, registered, metrics), the θ sweep, ordering ablation, shuffle control, mutation and axiom matrices, the B_gov baseline. |
| `simulation/` | Five 6,000-case simulation corpora — **VetPOC**, **SemiFab**, **DCVigil**, **FrontierLLM**, **Meridian Financial** — each with its constitution, generator, reference engine, 56-check conformance suite, 31-fault mutation matrix, benchmark, case explorer and datasheet; **Numerals**, the enterprise constitution over the five with a 3,000-case federated stream; the scenario catalogue; `MANIFEST.json` with per-pack SHA-256 digests. Start at [`simulation/README.md`](simulation/README.md). |
| `simulation/ec/` | The Enterprise Conscience fast track (5.16.0): the tiered canon T0–T3 generated into each pack's `constitution/canon.json`, the dispensation-token registry, the conscience gate (allow / block / hold), the examen log and its reconciliation, the bench coupling to the judiciary (escalation, glosses, codification), the strongest-rival arm A, policy / oracle / adversarial / LLM agents, the 365-working-day five-company driver, metrics E1–E8 and the TOST / bootstrap analysis; `run_ec_conformance.py` (12 checks) and `mutation_matrix_ec.py` (8 faults, 2 controls). `DESIGN.md` is the interface contract; the user guide is [`docs/ENTERPRISE_CONSCIENCE.md`](docs/ENTERPRISE_CONSCIENCE.md). |
| `prereg/` | The OSF preregistration of the EC year run: hypotheses H1–H7, estimands E1–E8, analysis plan, data dictionary, estimand map, and the plan hash over the prereg files, the five canons, the package and its tests. |
| `simulation/tools/` | Cross-pack tooling: engine propagation, scenario extension, coverage matrix, the amendment overlay, and `extraction/` — the characterisation and record-construction stages that measure the Evaluator's fidelity rather than assume it. |
| `benchmark/`, `bench/` | The root-level tier benchmark over the demo packs (harness, models, pricing snapshot, report) and its scoring; the five-arm benchmark over the simulation packs lives in each pack's `benchmark/`. |
| `seed/`, `config/`, `deploy/`, `examples/`, `scripts/` | The default seed constitution and opening store, example configuration files (`dj.example.toml`, `dj.llm.example.toml`), a GCP deployment recipe, a Postgres advisory-lock example, and the enterprise smoke test. |
| `tests/` | pytest wiring over the conformance suites, the digests and the engine invariants; what CI runs. |
| `docs/` | The user guide, the Enterprise Conscience guide, operator notes, release notes, connection pooling, the fintech regulatory register. |

## The documents a reviewer should read

- [`REPRODUCE.md`](REPRODUCE.md) — one command per published figure, and the things
  about this artefact we would rather you read from us than discover yourself.
- [`PAPER_ALIGNMENT.md`](PAPER_ALIGNMENT.md) — what the benchmark paper registers
  against what this artefact executes, item by item.
- [`DATASHEET.md`](DATASHEET.md) — the datasheet for the corpora, with the EC overlay
  addendum.
- [`docs/ENTERPRISE_CONSCIENCE.md`](docs/ENTERPRISE_CONSCIENCE.md) — the fast track:
  concepts, how to run each mode, how to read the outputs, how to change a canon, and
  what is not claimed. [`prereg/PREREG_EC_SIM_v1.md`](prereg/PREREG_EC_SIM_v1.md) is the
  registration of its year run.
- [`DUAL_USE.md`](DUAL_USE.md) — what is released, what is withheld, and why.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — the layered design and the review decisions
  behind the single-container substitution.
- [`CHANGELOG.md`](CHANGELOG.md) and [`docs/releases/`](docs/releases/) — every release
  since 5.0, with what it added and what it changed.

## Design commitments, in one paragraph each

**Ground truth is computed, never authored.** Every corpus's expectations are the
reference engine's own chronological pass; the generator writes cases, not answers, and
the digests in `simulation/MANIFEST.json` pin exactly what was run. **Every check can
fail.** Each conformance check has an injected fault in the pack's mutation matrix that
kills it; a check nothing can fail is not a check, and the matrices are part of the
release. **Silence never binds.** Facts are three-valued; an unrecorded fact abstains
with a named cause, refers rather than clears a floor, and withholds a record whose
premise it could not establish. **A permit that never saw the violation decided nothing
about it.** The distinguishing gate falls a permissive precedent on any violating factor
of an engaged provision its facts never contained, and falls any record decided under
since-amended text where the amendment touched its premise. **One engine.** The six
copies of `harness/engine.py` are byte-identical apart from two header lines, and the
test suite says so.

**Two forums, two speeds.** The judiciary is the slow track: it sees a change only when
the change is contested or escalated, it hears the case against the record, and what it
writes binds later cases. The Enterprise Conscience (`simulation/ec/`) is the fast track:
a gate reads every change, before it executes, against a tiered canon generated from the
same constitution (T0 absolute; T1 dispensable only by a token from an office outside the
proposer's reporting line; T2 tradable within a bound for an admitted reason; T3
customary within listed contexts) and against the token registry, and the agent writes an
examen entry after each executed act that is reconciled against what verifiably happened.
What the gate writes is a log, never a record. The two meet through four channels: the
gate escalates T0 violations, tokenless T1 contrarieties and conflicts to the bench, which
hears them with the pack's own engine three working days later; a holding is written back
as a gloss on the canon entry; a holding recurring three times codifies and closes the
token channel for that class; and only aggregate disclosure counts, never an act or a
narrative, reach the bench. Arm B runs the slow track alone, arm C the fast track alone,
arm D both; arm A is the strongest stack an enterprise can field today without either.
The fast track covers the slow track's blind spot, the impermissible act nobody contests,
and the slow track returns doctrine to the gate. The engine is not edited to do any of it.

## Status

Release **5.16.0** — simulation pack 2.4.0, corpus data 2.1.0, federation 1.3.0. Five
packs at 56/56 checks, 31/31 faults killed and 4/4 controls surviving; Numerals 11/11,
7/7 and 2/2; demo suites 61/61, 44/44, 53/53; mutation matrix 13/13 and 5/5; axiom
matrix 8/8. The Enterprise Conscience suite at 12/12 checks, 8/8 faults killed and 2/2
controls surviving, 50 tests passing plus the matrix under `--runslow`; its registered
365-day run is in progress and none of its results is claimed here. The benchmark and the
EC LLM agent have been exercised offline only: **every model-facing figure in the papers
and every LLM figure in the EC preregistration is a pre-data projection until the live
run**, and the offline mode is not evidence about any model.

## Citing

Cite the release and the corpus version together — the software record is in
[`CITATION.cff`](CITATION.cff) and the Zenodo metadata in `.zenodo.json`; the papers
are listed in [`PAPERS.md`](PAPERS.md).

## Licence

Code is licensed under [Apache-2.0](LICENSE); constitutions, corpora, stores, dockets
and generated documents under [CC BY 4.0](LICENSE-DATA). See [`NOTICE`](NOTICE) for
third-party acknowledgements. The enterprises, products and people in every corpus are
fictitious; the regulators and standards they cite are real.

Contributions are welcome — read [`CONTRIBUTING.md`](CONTRIBUTING.md) first, and
[`SECURITY.md`](SECURITY.md) for how to report a vulnerability.
