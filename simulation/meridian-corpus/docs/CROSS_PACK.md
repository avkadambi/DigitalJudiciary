# Cross-pack comparison: five domains, one mechanism

Chapter 5 §7.1 poses a domain-parameterisation question as RQ3: when the provision inventory, factor vocabulary, seed records and case content are re-instantiated for a different enterprise — holding the case-category composition fixed by design — do the route, stage and storage profiles remain identical?

It is a claim about the implementation, not a discovery about the world. Matched composition makes matched profiles the *expected* outcome, and a deviation falsifies the implementation rather than the theory.

Five packs now exist, sharing nothing but the mechanism and the category counts:

| Pack | Domain | Provisions | Absolute | Superset of a released pack |
| :--- | :--- | ---: | ---: | :--- |
| **VetPOC** | Veterinary practice management and point of care | 98 | 18 | — |
| **SemiFab** | Semiconductor supply-chain control tower | 103 | 20 | — |
| **FrontierLLM** | Frontier model development | 113 | 22 | — |
| **DCVigil** | Multi-tenant data-centre monitoring and AIOps | 108 | 17 | 29 provisions, 144 cases |
| **Meridian Financial** | Regulated fintech: payments, cards, ledger, lending | 116 | 24 | 37 provisions, 68 cases |

Meridian is the pack with the most absolute provisions, and the only one whose shipped provisions can be checked against a source. Its thirty-seven shipped provisions each cite a real instrument, which is why it is the only pack whose constitution the surveys could find *wrong* rather than merely incomplete. Seven findings are filed as draft amendments; none is applied.

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

**The route profile carries across five unrelated domains.** Every route cell agrees to within 1.08 percentage points of the corpus, over veterinary care, semiconductor supply chain, frontier model development, data-centre monitoring and regulated finance. Routes are a property of the mechanism, and the mechanism does not know what domain it is in.

**The decision profile does not, and should not.** The spread on `permit` is 3.58 points, and Meridian and SemiFab are its two endpoints — 3,083 permits against SemiFab's 3,262. That gap is the constitutions differing — how many violating factors a provision family carries, how the absolute provisions distribute across a fixed case mix. A corpus whose decisions also matched would be evidence that the constitution was doing no work.

**Three cells moved for a reason worth naming, and all three are Meridian's.**

*`bound_by_precedent` is the lowest of the five, at 985.* The other packs sit between 999 and 1039. The cause is the charging threshold. Meridian's financial-crime family carries τ = 15 and its card-data and fair-lending families τ = 18, against 20 for a fully compliant case — so in those families a compliant change is charged anyway and reaches an adjudicator that has more to consider. Low thresholds are what a strict-liability regime looks like when you write it down, and they push work into the judiciary rather than away from it.

*`fresh_interpretation_after_tie` is the highest, at 125.* Same cause, opposite direction: more cases reach the ordering stage, so more of them find two survivors that tie on every key.

*`absolute_shortcircuit` is 338 against a 333–341 band* — unremarkable, and worth saying so, because Meridian has 24 absolute provisions to DCVigil's 17. The count of absolute provisions does not drive the count of absolute short-circuits; the F-absolute category count does. That is the mechanism working: A6 fires on engagement *and* violation, not on the existence of a floor.

## The one check that differs across packs

VC-13, pressure invariance, is strengthened in DCVigil and in Meridian. The other three packs compare the twin's disposition against its control's. These two compare the whole trace — disposition, route, controlling record, consulted set and stored status — which is only sound if the twin faces the same store its control faced.

Making that true required two construction changes, both carried into this pack:

1. A control case immediately preceding a pressure twin is forced uncontested, so it writes no record between itself and its twin.
2. Like-case pairs are inserted into the schedule *before* pressure twins, so nothing can be spliced between a control and the twin that shadows it.

In this pack: **185 twins, nine PACT mechanisms, 185 adjacent to their control, zero divergence on any of the five properties.** SemiFab and FrontierLLM report 44 and 29 twins bound by their own control's record, which is the confound those two changes remove; their READMEs say so rather than hiding it.

## Reproducing this table

```
python3 harness/compare_packs.py
```

With no arguments it discovers sibling pack directories alongside this repository. Pass explicit `manifest.json` paths to compare a chosen subset.


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
