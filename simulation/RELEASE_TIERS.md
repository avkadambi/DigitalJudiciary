# Release tiers for the simulation packs

Three tiers, applied to every pack in `simulation/`. The rule behind them is
that **the generator, not the corpus, is the dangerous artefact**: a fixed set
of 5,000 decided cases is a benchmark, while the machinery that mints new
violating changes on demand is closer to a tool. What follows states which of
the three tiers each file in a pack sits in, and what the current release
actually ships.

| Tier | What it holds | Shipped in 5.8.1? |
| :-- | :-- | :-- |
| **Public** | the taxonomy (25 categories and their counts), aggregate statistics, the datasheet, the constitutions, the licences, the conformance and mutation suites, the reference engine, the benchmark harness, every document under `docs/` | yes — all of it |
| **Trusted contributor** | the instance records: `corpus/cases.json`, `cases.jsonl`, the stores, the docket, `docs/CASE_CATALOG.md` and `case_catalog.csv`, `docs/explorer.html` | yes — these packs are released whole, because the corpora are synthetic end to end |
| **Withheld** | generator prompts and seeds for an evasion or adversarial stratum, until the programme's threat-model work executes | **not applicable, and the reason matters** — see below |

## Why nothing is withheld here, stated rather than assumed

The withheld tier exists for a corpus whose adversarial stratum is generated
from real, operationally live material. These packs are not that. Three facts,
each checkable rather than asserted:

- **No real external identifier appears anywhere in any pack.** No CVE, no
  package name from any registry, no exploit, no real vendor, no real person.
  The provisions cite real regulations by name in their `citation` field — a
  reference to `31 CFR Ch. V` is a legal citation, not an artefact — and the
  factor vocabulary is invented for the world it belongs to.
- **The Y-adversarial stratum (150–175 cases per pack) is adversarial toward
  the ADJUDICATOR, not toward a system.** Its cases attempt to obtain a
  disposition the constitution does not license — by mimicking a precedent, by
  asserting an authority, by arriving under pressure. Nothing in it teaches
  anyone to attack software, and the generator that mints it produces change
  *titles* and *factor sets*, never code.
- **The generator is deterministic and closed.** `generator/changes.py` is a
  fixed catalogue of roughly 160 compliant and 104 violating change titles per
  world. It composes; it does not invent. Releasing it lets a reader reproduce
  the corpus, which is the point, and gives them no capability they did not
  already have.

If a future pack draws on live material — a real registry snapshot, a real
vulnerability corpus — the withheld tier binds and the generator for that
stratum does not ship until the threat-model work is done. This file is where
that decision gets recorded.

## What the corpora do NOT secure

Stated here as well as in each pack's README, because a reader who takes only
the aggregate statistics should still meet it:

- **Retrieval quality.** Every case arrives with `rules(c)` already correct. The
  Evaluator that would compute it in a deployed system is modelled at ε = 1.00
  ⟦identity⟧, so the corpus prices its error at nothing and cannot bound it.
  PACT prices the alternative — a model deciding scope for itself — at 19.6%
  over-application ⟦measured⟧ by Okamoto & Erol. The architecture relocates that
  error; it does not remove it. The S8 family exists to keep this visible.
- **Precedent-replication error.** The store is written by the reference engine,
  so records are perfectly faithful to the decisions that made them. A
  deployment where records are written by hand, or by a model, has an error
  channel this corpus does not model.
- **Factor characterisation.** Facts arrive as factors. The step that turns a
  real diff into a factor set is precompiled away, here and in PACT alike.
- **Anything about a model.** Oracle and dry modes make no model call. The
  `monolith_trap` predictions in the discriminating suite are ⟦PROJECTED⟧ until
  `--mode live` runs.

## Licences

Code Apache-2.0; corpora, constitutions and documents CC BY 4.0. Each pack
carries its own `LICENSE`, `LICENSE-DATA` and `NOTICE`, and its
`docs/SOURCES.md` records every external source with its verified licence
position.
