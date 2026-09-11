# Release 5.7.0 — Consolidation (Definition 7 clause (ii))

**2 September 2026.** One mechanism, one contract change, one corpus category,
and the corpus is frozen at this cut.

## The contract change, stated as one

Until this release the ledger declared

```sql
authority_tier INTEGER NOT NULL CHECK (authority_tier BETWEEN 2 AND 4)
```

so that a first-instance record was unrepresentable, full stop, and probe
`PRB-3` asserted exactly that. Definition 7 as amended admits one other thing —
the designated representative of a consolidation class — and it is admitted at
first instance, so the flat bar could not stand. What replaces it is narrower
rather than looser:

```sql
authority_tier   INTEGER NOT NULL CHECK (authority_tier BETWEEN 1 AND 4),
admission_ground TEXT CHECK (admission_ground IN ('contest','consolidation')),
class_id         TEXT REFERENCES consolidation_class(class_id),
CHECK (
  (COALESCE(admission_ground,'contest') = 'contest'
     AND authority_tier BETWEEN 2 AND 4 AND class_id IS NULL)
  OR
  (admission_ground = 'consolidation'
     AND authority_tier = 1 AND class_id IS NOT NULL)
)
```

**A probe that had passed since the contract was written is retired, and that is
a real loss.** `PRB-3` no longer establishes that first-instance admission is
impossible, only that it is impossible *without a named ground and a class
artefact*. Four probes now carry between them what one carried before —
`PRB-3` (no ground: aborts), `PRB-3b` (any other ground: aborts), `PRB-11` (the
licensed ground with its class: accepted) and `PRB-12` (the licensed ground
without a class: aborts) — and the third is the one the old contract could not
have had, because it asserts that something *is* licensed.

Two hazards were found in writing it and both would have passed silently.
SQLite evaluates a table `CHECK` to `NULL` when a column it reads is `NULL` and
admits the row, so the first form of the clause — without `COALESCE` — accepted
the very row `PRB-3` was written to refuse. And a table-level constraint written
among the column definitions is a syntax error whose message names the following
column rather than the constraint.

`ALTER TABLE` cannot add a table-level `CHECK`, so a database upgraded in place
gets the two columns and the two class tables and **not** the licensing
constraint. Fresh ledgers get all of it. `EX-52` asserts the columns and the
tables; this paragraph is the rest, said rather than implied.

## What is new

* `app/consolidate.py` — Definitions 15 and 16. `Classify` takes no
  `Authorities` argument and returns a type no authority produces. It is a
  separate object with its own writer, holding no branch, because forming a
  class is a power over admission and no authority class holds one.
* `consolidation_class` and `consolidated_disposition` — append-only on both
  backends. The class artefact records the pinned snapshot hash, N₀ and Δ, the
  signature, the **whole docket** and not only the members, the representative,
  and the producing service.
* `L-consolidated` — eight cases per pack. One class forms; five cases are
  refusals. 136 → 144 cases, thirteen categories. Store 44 → 45 (45 → 46 on
  `vetpoc`).
* `CC-19`…`CC-22`, `COR-26`…`COR-29`, `PRB-11`, `PRB-12`, `IF-32`, `IF-33`,
  `IFP-11`, `EX-50`…`EX-53`. Suites move 49/41/49 → **61/44/53**.
* `M10`…`M13` and controls `S4`, `S5`. The matrix moves 12 entries → **18**,
  and runs 13 of 13 killed, 5 of 5 survived.
* `reproduce/report.py` prints the four intake routes and **asserts they sum to
  the session count**.
* `demo/regenerate_store_seed.py` — one command, and the file it writes records
  the corpus size it came from.

## Errata fixed in passing

**The rulebook version hash was computed two different ways.** `enact_version`
hashed the provision dicts as they were handed to it — which for a bootstrap
carried four keys and for an amendment carried five — while `CC-04` recomputed
over four. The two agreed on `rb-000001` and disagreed on every amended version,
and the defect was invisible because no record in the conformance corpus had
ever pinned an amended version. The consolidation corpus put a record on
`rb-000002` and `CC-04` failed the same afternoon. One projection,
`ConstitutionStore.version_digest`, is now used by the writer and by the check.

**The three checked-in conformance reports are regenerated from live output.**
`CONFORMANCE_REPORT.txt` had been one row stale since the `PRB-8` strengthening.

## Two checks that could not have failed, and now can

`M10` empties the class artefact's store snapshot. `CC-19` was written for
exactly that and the mutant survived, because the check recomputed the digest by
calling the same function the writer calls. It now computes the digest from the
definition, inline.

`M12` deletes clause (e). It survived because nothing in the conformance corpus
was covered by a live record, so removing the guard changed nothing. The corpus
now runs a **second docket boundary** after the first class's record is live
(`COR-29`), and the mutant dies at `CC-21`.

Neither was a bug in the implementation. Both were a check or a corpus that
could not have failed.

## Three things stated rather than left to be found

1. **A consolidated record never outranks a contested one — and does not rank
   below one either.** `authority_rank` has two levels, so a first-instance
   consolidated record is EQUAL to a contested tier-2 or tier-3 record at the
   `auth` key and strictly below a risk acceptance. Where both survive the gate,
   recency separates them. `EX-50` asserts the property that holds.
2. **Consolidation is a precedent-manufacturing mechanism as well as a cost
   mechanism.** Under clause (i) minting a favourable precedent means winning a
   contest; under clause (ii) it means having volume, which is what an agentic
   author has by definition. Four containments apply and all four are detection
   rather than prevention. See `REPRODUCE.md`.
3. **Consolidation buys a constant twice** — a constant width of admission and a
   constant factor on the quadratic — and it is not a repair for the
   one-sidedness the standing theorems establish.

---

# 5.7.1 — Proposition 4, executed

**2 September 2026.** No change to the corpus, which stays frozen at 144 cases
per pack, and no change to any executed figure. What changes is that a proof
stops citing a run that never happened.

Sect. 7.8 has always described eight axiom mutants and an expected-failure map,
and Proposition 4's proof cited one of them in terms — "the mutant Sect. 7.8
builds". `reproduce/mutation_matrix.py` executes a different list: mechanism
mutants, anchored on the code that implements the contract. The two lists
barely overlap, so the axiom map had never been run.

`reproduce/axiom_matrix.py` and `reproduce/axiom_probes.py` now run it, and run
it **both ways**. For each of A1 to A8 a single-line relaxation drops that
axiom's enforcement, and the guarantee Proposition 4 names must **hold** with
the axiom in place and **fail** without it. A probe that fails in both
directions witnesses nothing; one that holds in both has not dropped the axiom.
**Eight of eight counter-models are witnessed.** The file is separate from the
mechanism matrix on purpose: the two ask different questions, one about whether
the checks notice a fault and one about whether anything is lost when an axiom
goes.

Two findings came out of running it.

**A6's relaxation is the same edit as mechanism mutant M3, and the duplication
is kept.** M3 asks whether the conformance surface notices the absolute
short-circuit being disabled. A6 asks whether the contract loses anything when
the axiom goes. Collapsing them would answer one question twice.

**The bootstrap's own seed import depends on A7 holding.** It writes two lapsed
risk acceptances and reads back the referral each of them emits, so dropping A7
against the ordinary opening store stops the container booting before any
observation is possible — and "bootstrap crashed" is not the guarantee
Proposition 4 names. The A7 counter-model runs against a new empty opening
store, `seed/store_seed_empty.json`, and the coupling is recorded because no
check states it.

Also in this release: the record unit is ruled to be the **(case, provision)
pair** rather than the case, which is what `pr_case`, the retrieval log and
admission were already keyed on. Chapter 5's Fact 1 and §5.2.3 now say so,
Appendix C item 10 is closed as a settled convention rather than an open
modelling question, and Definition 7's second clause depends on it: a class is
formed over units, and refuses any unit whose case engages more than one
provision.
