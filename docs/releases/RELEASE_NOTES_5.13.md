# Release 5.13.0 — what the record did not see (pack 2.3.0, federation 1.3.0)

11 September 2026. Two rungs are added to the admission ladder of the
distinguishing gate, both about the *record's* blind spots rather than the
case's shortfalls. On the five division packs every constitution, corpus,
opening store, docket, generator digest and every pre-existing trace is
byte-identical (VC-55 and VC-56 count the changes at zero); the release
adds two checks and two mutants per pack, a ninth discriminating family, and
a measurement tool. Numerals is different: its D-vertical construction had
been hiding the first blind spot, and its corpus is rebuilt (federation
corpus 1.3.0) — see below.

## Rung 1 — the unaddressed adverse fact (VC-55, M29, S9)

Distinguishing was one-directional. `distinguish(r, c)` asked whether the
case *lacked* a premise factor and never whether it *carried* one that cuts
against the holding; a record that permitted on {a, b} bound a case doing
{a, b, v} a-fortiori, v being a violating factor of the same provision. A6
caught this only for absolute provisions. Now a permissive holding falls
with status `adverse_unaddressed` on any violating factor of any engaged
provision that the record's facts never contained, and the case goes to
fresh interpretation, where the violation is read. The rule is asymmetric
on purpose — a deny record is not cured by the case's extra compliance —
and a record that *saw* the violation (a risk acceptance, an interpretive
permit) still governs the case that repeats it.

The five division corpora draw their noise factors from the compliant pool
and never build this pattern; VC-55 measures zero adverse admissions and
zero changed traces on each, and its probe fires on the synthetic case,
checks the asymmetry, the acceptance-that-saw-v, and a violation of a
*second* engaged provision. The discriminating suite gains
**S9-unaddressed-adverse-fact** (tier: measured): under the oracle reader
the retrieval-only arm A+ follows the permit and answers `permit`; arm B
falls the record and answers `deny`. Nine families, four of which now
separate B from at least one other arm.

**Numerals had the hole live.** Its D-vertical category (100 cases) built
the home-versus-foreign conflict from a permitting seed that had never seen
the violating factor the denying seed turned on; the case carried it, the
5.12.0 gate let the home permit win on the scope key, and 55 cases were
decided `permit` on a change that, for instance, added a personal-data
field without a stated purpose. Under the new rung the permit falls and the
foreign deny governs — the right outcome, and a corrected construction
rather than a corrected engine: the permitting seed now carries v0 too, as
an interpretive holding that v0 does not offend the provision in that
division's setting, which is the conflict the category was always meant to
stage. Rebuilt deterministically; 11/11; FC-07 (vertical precedent is thin)
passes on the corrected pairs. One federated-benchmark figure moves: C-cross
cases can now carry a violation that enterprise precedent held permissible,
so the monolith and the division-local judiciary — which cannot see the
enterprise record — re-derive a denial on 111 and 93 of 400 (against
400/400 in 1.2.0) while the federated arms keep 400/400 with the foreign
record cited. That is the first place the enterprise store changes an
*outcome* rather than a citation, which is what vertical precedent is for.

## Rung 2 — decided under prior text (VC-56, M30, `tools/amendment_overlay.py`)

Records were tied to a provision *id*, not a provision *text*. A rulebook
provision may now carry `version` and an `amendment_history` of
`{version, touched_factors}` (coherence at load: distinct, ascending, ≥ 2,
matching `version`); records carry `prov_version`, the text version the
holding was decided under. A record whose premise an adopted amendment
touched falls with status `decided_under_prior_text`; a citation-only
amendment touches nothing and unsettles nothing; a record written under the
new text binds. Every released provision is at version 1 and no record is
stale (VC-56 counts zero), so the measurement is an overlay:
`amendment_overlay.py` adopts amendments in memory at the stream's midpoint
and replays. On every pack a **limb** amendment (redefining the violating
factors) unsettles *nothing* — not one of the 1,039–1,071 records in any
final store turned on a violating factor; the corpora's binding
jurisprudence is entirely compliant-pattern precedent, and the violating
limb is enforced by the Evaluator and the prosecutor, never by a record. A
**compliant-factor** amendment unsettles up to half the records on a
provision and 5–25 binds each. The packs' own filed draft amendments (5–12
per pack, mostly status and limb changes) would unsettle no bind if adopted
today, for the same reason.

## Also in this release

`engine.gate` and `engine.admit` take an optional `provisions` argument and
otherwise read the provisions the last `adjudicate` or `load_constitution`
call registered, so every caller — the arms, the generators, the checks —
applies the two rungs consistently. The silence oracles of VC-52 and FC-11
now use the engine's own per-record admission rather than raw containment.
The discriminating suite's seed records for S1, S2 and S5 now carry the
violation they excused, which is what those acceptances always meant.

## Suites

Division packs: 56/56 conformance (VC-55, VC-56), 30/30 faults killed and
4/4 controls survived (M29, M30). Numerals: 11/11 on the rebuilt stream,
7/7 + 2/2. Generator digests of the five packs unchanged; Numerals' corpus
digest changes and is recorded in its manifest.

## Evaluated and not built (this release)

Concurrence on ties (bind when tied survivors agree): 134–145 ties per pack,
none unanimous, so no observable effect today; correct rule, deferred.
Near-miss reporting and stance propagation: trail and research
respectively; deferred with the reasoning in the project note.
