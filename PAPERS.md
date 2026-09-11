# How the code refers to the papers

The checks, docstrings and documents in this repository cite the programme's
papers by the chapter numbers of the dissertation they were written for. This
table maps those references to the papers a reader outside the programme will
have.

| Reference in the code and docs | Paper | What it covers |
| :-- | :-- | :-- |
| Chapter 3, "Paper 1", the survey | *Governed Precedent in Practice* (survey) — Kadambi & Kuppuswamy 2026a | Practitioner survey; requirements R1–R7 |
| Chapter 4, "Paper 2", Definitions 1–12, Theorems 1–8, Propositions 0–7, admission rules A_all / A_contest / A_conf / A_ed | *Case-Base Formation for Precedential Constraint* — Kadambi & Kuppuswamy 2026b | The theory of which decisions become precedent |
| Chapter 5, "Paper 3", Axioms A1–A9, Definitions 1–19, §4.6 (the reference adjudicator), conformance checks CC-01…CC-33 | *The Digital Judiciary: an architecture for governed precedent* — Kadambi & Kuppuswamy 2026c | The architecture, the reference engine `harness/engine.py` implements, and the demo packs |
| Chapter 6, "Paper 4", arms A / A+ / B_mem / B_gov / B, endpoints B1–B8, pass^k | *Benchmarking Governed Precedent* — Kadambi & Kuppuswamy 2026d | The benchmark `simulation/*/benchmark/` executes; see `PAPER_ALIGNMENT.md` for what is and is not implemented |
| Chapter 7 | The dissertation's synthesis | Not needed to use anything here |

The provenance marks used throughout — ⟦measured⟧, ⟦derived⟧, ⟦PROJECTED⟧,
⟦identity⟧ — are defined in `simulation/RELEASE_TIERS.md`. A ⟦PROJECTED⟧ figure
is a pre-data estimate and is never evidence; the papers' results sections are
marked the same way until the benchmark has been run live.
