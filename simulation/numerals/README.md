# Numerals — an enterprise constitution over five divisions

**Federation 1.3.0 · release 5.13.0 · Apache-2.0 (code) + CC BY 4.0 (data)**

Numerals is the invented parent of the five division packs — VetPOC, SemiFab,
FrontierLLM, DCVigil and Meridian. Each division keeps its own constitution
(the five packs, **byte-identical to 5.9.0**) and every division inherits this
one. The package adds what the five packs cannot show on their own: one
constitution applied across domains, one shared store, and precedent that
crosses divisional lines.

| | |
| :-- | :-- |
| **33 enterprise provisions** in 6 families, 6 absolute, 4 proposed floors held ordinary | `constitution/rulebook.json` (every provision carries `level: enterprise` and `implemented_by`) |
| **The inheritance map** — 165 (provision × division) cells, curated by id against the five rulebooks as shipped | `constitution/inheritance.json`, `docs/INHERITANCE.md` |
| **26 draft amendments** the enterprise files against division constitutions, none applied | `constitution/proposed_amendments.json` |
| **3,000-case federated stream**, five divisions filing against one store | `corpus/cases.json` (each case carries `division`) |
| **10 federation checks**, 6 faults + 2 controls | `harness/run_federation_checks.py`, `harness/mutation_matrix.py` |
| **The federated benchmark**, offline | `benchmark/run_federated.py` |

```bash
bash reproduce/run_all.sh          # build, determinism, 10/10, 6/6 + 2/2, docs, offline benchmark (~30 s)
```

## The three rules

**Inheritance is minimum harmonisation.** A division may *tighten* an enterprise
provision — state as absolute what the enterprise states as ordinary, add factors,
narrow a window — and may never *loosen* one. An enterprise absolute is a floor in
every division. This is the only rule consistent with A6, and it is the rule EU
directives and US federal floors use. FC-02 checks it against the six rulebooks.

**The enterprise cannot impose a floor over a frozen division constitution.**
Where the author asked for an enterprise floor and a division states the same duty
ordinarily, the build refuses to declare the floor: the provision is stated
ordinarily with `proposed_absolute: true` and a draft amendment is filed against the
loosening division provisions. Four of the ten requested floors are held that way
(agents never touching authentication middleware; multiparty review of
agent-authored security changes; no secrets in source; change control never
self-approved). That is A3 across levels — the enterprise proposes, each
division's lawmakers dispose — and it is why the number of enterprise absolutes is
six rather than ten.

**Records on enterprise provisions bind enterprise-wide, and vertical precedent is
thin.** A holding written when Meridian contested a change controls a materially
identical change FrontierLLM files later. A division's own record on the same
provision is presented to that division one step narrower in scope than any
foreign record (`harness/federation.py`, one line), so when both survive the gate
the ordering rule's existing scope key prefers the home record — Chapter 4 §8's
thin vertical precedent, produced by a key the engine already had. FC-06 and FC-07
check both directions on executed traces; MF1 sets the offset to zero and FC-07
dies.

## What the checks say

```
FC-01  replay reproduces every decision, route and controlling record       3,000 / 0 differ
FC-02  no division states an enterprise floor ordinarily                     6 floors, 0 loosened
FC-03  inheritance map complete; every gap filed as a draft amendment        165 cells, 22 gaps, 22 filed
FC-04  A1 per level — enterprise and division rosters disjoint               7 principals, 0 clashes
FC-05  cross-division like-case pairs agree on disposition AND citation      200 / 0 disagree
FC-06  every C-cross case is bound by another division's record              400 / 400
FC-07  home record beats foreign record on the scope key                     100 / 100
FC-08  cross-division pressure twins do not move the trace                   250 / 0 moved
FC-09  enterprise floors short-circuit in every division                     300 across 5 divisions
FC-10  canary, division and level on every case                              3,000 / 0 malformed
```

All ⟦measured⟧ on the corpus as built. Mutation matrix: 6/6 faults killed, 2/2
controls survived.

## What the inheritance survey found

Two things worth reading before anything else. **Change control is under-provisioned
outside Meridian**: no other division has a provision forbidding self-approval or
requiring an approver other than the author (NM-401 gaps in four divisions), and
SemiFab and FrontierLLM have no rollback or freeze-window provision at all. And
**application security is a two-division family**: DCVigil and Meridian carry no
CWE-level provisions (parameterised queries, output encoding, deserialisation,
SSRF), so four enterprise provisions have no implementation there. Both are filed as
amendments to those divisions; neither is a defect in this package.

## The federated benchmark (offline)

Four arms over the enterprise stream: the monolith (`A`), advisory memory
(`B_mem`), the judiciary with a **division-local** store (`B_div` — five
judiciaries that do not talk to each other) and the **federated** judiciary (`B`).

```
arm     cross-division pairs   C-cross: disposition / cites the foreign record   no-call
A            200/200                    400/400   /   0                            0.0%
B_mem        200/200                    400/400   / 400                            0.0%
B_div        200/200                    397/400   /   0                           14.9%
B            200/200                    400/400   / 400                           26.7%
```

Oracle mode is a perfect reader of what each arm is shown — an upper bound on the
arm, never a prediction about a model — so the dispositions agree everywhere and
the columns that separate the arms are structural: only an arm holding the
enterprise store can *cite* the record another division wrote, and only the
federated judiciary does so without a model call. `--mode live` is what produces
a claim.

## One harness defect this package found

`benchmark/arms.py` in every division pack rated an arrival against τ *before*
retrieving; the engine retrieves first and rates only when nothing survives. Two
cross-division cases that the reference bound to a live record were docketed by
arm B as a result. Fixed in all six copies (release 5.10.0); no corpus or
conformance figure depends on it.

## What is not secured

Everything the division packs' `RELEASE_TIERS.md` lists, plus: the inheritance
map is curated by the authors from provision titles and is only as good as that
reading — FC-02 and FC-03 check its consistency with the rulebooks, not its
semantics; the enterprise factor vocabulary is its own, so no enterprise record
binds a *division-pack* case (the packs are unchanged and their stores are
separate); and the federated stream is a corpus of enterprise-provision cases,
not a merger of the five division streams.


## 1.1.0 (release 5.11.0)

The enterprise engine is the 5.11.0 comparison kernel (see any division pack's README, 2.1.0). **FC-11** silences one premise factor of the foreign controlling record on every one of the 400 cross-division binds and checks, through `harness/binding_gate.py`, that no bind survives on silence: 346 abstain with cause `premise_not_established`, 54 re-bind on an untouched record, zero false binds. **MF7** makes silence bind and FC-11 kills it. 11/11, 7/7 and 2/2. Cases, stores, constitution, inheritance map and every 1.0.0 figure are unchanged.


## 1.2.0 (release 5.12.0)

The enterprise engine is the 5.12.0 engine: citation stance in the ordering rule (a legacy citation with no stance is superseded, so every 1.1.0 trace is reproduced) and record-construction provenance. 11/11, 7/7 and 2/2; cases, stores, constitution and inheritance map unchanged.


## 1.3.0 (release 5.13.0) — a corrected corpus

The 5.13.0 gate falls a permissive record on a violating factor its facts never contained, and that exposed a defect in this package's D-vertical construction: the permitting seed of an even-indexed division was written on a compliant premise while the denying seed of an odd-indexed division turned on a violating factor v0, so the D-vertical case — the union of the two premises — presented the home permit with a violation it had never seen. The 5.12.0 gate let it win on the scope key; 55 of the 100 D-vertical cases were decided `permit` on a change that, for instance, added a personal-data field without a stated purpose. The construction is corrected, not the rule: the permitting seed now carries v0 as well, an interpretive holding that v0 does not offend the provision in that division's setting, which is the conflict the category was meant to stage. The stream is rebuilt deterministically (corpus 1.3.0; cases.json digest changes and is recorded in `corpus/manifest.json`); 11/11 checks, FC-07 passes on the corrected pairs, 7/7 + 2/2 mutants. Every other category's construction is unchanged.

One benchmark figure moves, and it is the more honest one. Because a C-cross case is built from a foreign seed's premise and the permitting seeds now carry v0, a C-cross case can arrive carrying a violation that enterprise precedent has held permissible in that pattern. The federated arms (B, B_mem) still reach 400/400 dispositions with the foreign record cited; the monolith A and the division-local judiciary B_div, which cannot see the enterprise record, re-derive a denial on 111 and 93 of the 400 respectively (289/400 and 307/400 disposition agreement, against 400/400 in 1.2.0). Under 1.2.0 the four arms agreed on every disposition and differed only in citation and cost; the corrected construction is the first place the enterprise store changes an *outcome*, which is what vertical precedent is for.
