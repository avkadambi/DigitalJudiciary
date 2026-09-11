# Cross-pack comparison: five domains, one mechanism

Chapter 5 §7.1 poses a domain-parameterisation question as RQ3: when the provision inventory, factor vocabulary, seed records and case content are re-instantiated for a different enterprise — holding the case-category composition fixed by design — do the route, stage and storage profiles remain identical?

It is a claim about the implementation, not a discovery about the world. Matched composition makes matched profiles the *expected* outcome, and a deviation falsifies the implementation rather than the theory.

Four packs now exist, sharing nothing but the mechanism and the category counts:

| Pack | Domain | Provisions | Absolute |
| :--- | :--- | ---: | ---: |
| **VetPOC** | Veterinary practice management and point of care | 98 | 18 |
| **SemiFab** | Semiconductor supply-chain control tower | 103 | 20 |
| **FrontierLLM** | Frontier model development | 113 | 22 |
| **DCVigil** | Multi-tenant data-centre monitoring and AIOps | 108 | 17 |

DCVigil is also the one pack that is a **superset of a released artefact**: the twenty-nine provisions of the shipped DCVigil pack appear in it with their text and absolute flags unchanged, so the 144 shipped cases remain valid against this constitution.

## The comparison

| Quantity | meridian | vetpoc | semifab | frontierllm | dcvigil | | Note |
| :--- | ---: | ---: | ---: | ---: | ---: | :-: | :--- |
| cases | 5000 | 5000 | 5000 | 5000 | 5000 | = | held fixed by design |
| opening store | 194 | 182 | 185 | 193 | 193 | ≠ | one seed record per ordinary provision, plus the fixed conflict, tie, supersession, lapse and seeded sets |
| records written in run | 717 | 713 | 735 | 726 | 731 | ≠ | contest is a social input, not a decision |
| final store | 911 | 895 | 920 | 919 | 924 | ≠ |  |
| docket entries | 340 | 340 | 340 | 340 | 340 | = |  |
| consolidation classes | 54 | 57 | 56 | 55 | 57 | ≠ | class size is drawn, so the count moves |
| like-case pairs | 200 | 200 | 200 | 200 | 200 | = |  |
| construction anomalies | 0 | 0 | 0 | 0 | 0 | = | zero in all packs |
| |  |  |  |  |  | | |
| route: absolute_shortcircuit | 322 | 323 | 332 | 340 | 329 | ≠ |  |
| route: bound_by_precedent | 982 | 996 | 992 | 996 | 1002 | ≠ |  |
| route: consolidated_citation | 111 | 108 | 109 | 110 | 108 | ≠ |  |
| route: docketed_declined | 271 | 272 | 254 | 279 | 270 | ≠ |  |
| route: docketed_null | 69 | 68 | 86 | 61 | 70 | ≠ |  |
| route: fresh_interpretation | 3117 | 3119 | 3109 | 3100 | 3113 | ≠ |  |
| route: fresh_interpretation_after_tie | 128 | 114 | 118 | 114 | 108 | ≠ |  |
| decision: deny | 1201 | 1279 | 1147 | 1274 | 1254 | ≠ |  |
| decision: permit | 3171 | 3085 | 3248 | 3084 | 3082 | ≠ |  |
| decision: permit_conditional | 628 | 636 | 605 | 642 | 664 | ≠ |  |

Category composition identical across 5 packs: True
Largest route-share spread: docketed_declined at 0.50 percentage points of the corpus
Largest decision-share spread: permit at 3.32 percentage points of the corpus

## Reading it

**The route profile carries across four unrelated domains.** Every route cell agrees to within a single percentage point of the corpus. Routes are a property of the mechanism, and the mechanism does not know what domain it is in.

**The decision profile does not, and should not.** The spread on `permit` is 3.20 points, driven by SemiFab. That gap is the constitutions differing — how many violating factors a provision family carries, how the absolute provisions distribute across a fixed case mix. A corpus whose decisions also matched would be evidence that the constitution was doing no work.

**One cell moved on purpose, and it is the most interesting number here.**

`fresh_interpretation` now spreads 0.98 points where it spread 0.36 across the first three packs, and the reason is a correction rather than noise. Pressure twins bound by the record their own control case created: **0 in VetPOC, 44 in SemiFab, 29 in FrontierLLM, 0 here** — and the zero here is earned rather than lucky.

The PACT round of the programme had already found this and fixed it once: appending pressure twins at the end of a corpus faces them with a Store a hundred cases larger than their controls saw, so some are bound where their controls were not. That is precedent accumulating — the system working — and a confounded experiment. The fix recorded there was adjacency.

Adjacency alone turns out not to close it. A control that is *itself* contested is admitted and writes a record at its own timestamp, which its twin one tick later then retrieves. The confound returns at distance one. DCVigil closes it with two constraints together:

1. the twin is scheduled immediately after its control, with nothing insertable between them, and
2. a control that is about to be twinned is drawn uncontested, so it leaves the Store unchanged.

Under both, **185 of 185 twins are invariant across nine PACT mechanisms on all five recorded properties** — disposition, route, controlling record, consulted set and stored status — not merely on the verdict. VC-13 is strengthened in this pack to check all five; the sibling packs check the disposition only, and pass.

**That makes the earlier three packs' pressure numbers a measurement of store growth, not of pressure.** They are not wrong about what they claim — every twin in every pack decides as its control — but the 44 and the 29 are artefacts of the draw, and re-basing those packs on this construction is the recommended follow-up.

**Three cells move for reasons the generator states rather than hides.**

- *Opening store*: one seed record per ordinary provision, and four constitutions with different provision counts after reservations.
- *Records written in run*: contest is a social input drawn per case.
- *Consolidation classes*: class size is drawn from `{2, 3, 3, 4}`. The invariant that matters — exactly one record admitted per class — holds in all four (VC-19).

## What is not held constant, and why

Two packs strengthen a check beyond the shared baseline, and both are disclosed here rather than buried:

- **FrontierLLM's VC-04** additionally refuses to let a `deferred` or `advisory` provision be marked absolute — a response to Regulation (EU) 2026/1744 deferring the AI Act's high-risk articles.
- **DCVigil's VC-13** checks full trace invariance under pressure rather than disposition invariance, which the construction above makes possible.

The check *count* stays at 26 in every pack so the comparison above stays honest. What differs is the content of one check in each of two packs.

## What would falsify the implementation

A route cell moving by more than a point or two under matched composition, or a category whose executed route set differs between packs. Neither occurs across four packs, and the one cell that did move is accounted for by a named construction change. `corpus/anomalies.json` is empty in all four.


## What changed in this build

Three things moved since the first cut of these packs, and all three tightened
the comparison rather than loosening it.

**The pressure confound is closed in all five.** VetPOC, SemiFab and FrontierLLM
previously drew a pressure twin's control at random from a recent window, so a
twin faced a store its control never saw. Every pack now schedules the twin
immediately after its control *and* forces that control uncontested, so it
leaves the store unchanged. All five report **185 of 185 twins invariant across
nine PACT mechanisms on all five recorded properties** — disposition, route,
controlling record, consulted set, stored status.

**The suites went from 26 checks to 44.** VC-27 to VC-44 execute what the
earlier suites recorded: Chapter 4's admission-rule family over one stream,
Theorems 1, 2, 5, 6, 7 and 8 witnessed on the run, the Reporter and the audit
register as objects rather than descriptions, and B_gov and B_mem executed. The
mutation matrix went from 12 faults to 18 so the new machinery has mutants of
its own.

**Every case now describes a change somebody would file.** Area, owning service
and English description are derived from the provision engaged and from the
decisive violating factor, so a case reads as a pull request against a rule that
would actually govern it. No formal content changed: facts, premises and
ordering never read those fields.
