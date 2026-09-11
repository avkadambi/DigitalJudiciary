# Release 5.14.0 — deny-side jurisprudence (corpus 2.1.0, pack 2.4.0)

11 September 2026. The corpus change that 5.13.0 asked for, and one engine
rule the measurement of it turned up. The five division corpora are
regenerated — every case id, expectation and digest changes — with the
25-category composition unchanged and still identical across the packs; the
constitutions, opening stores and the Numerals package are as they were.

## Contested denials write records (generator, corpus 2.1.0)

Until now every plain denial was accepted and nothing was stored, so no
record in any pack turned on a violating factor: the corpora's binding
jurisprudence was compliant-pattern precedent only, and the violating limb
was enforced by the Evaluator and the prosecutor alone. That is why the
prior-text rung's limb amendments unsettled nothing in 5.13.0, and it was a
limitation worth removing rather than stating. One plain denial in five is
now contested and lost (`PLAIN_DENY_CONTESTED_SHARE = 0.20`); the deny record
it writes has as its premise the violating factor and one compliant factor
the instance named, and later plain violations of the same pattern are
bound by it rather than decided fresh (`B-plain-deny` may now route
`bound_by_precedent`). Per pack: 67–86 contested denials, 82–113 deny
records in the final store, 69–100 binds whose controlling record turned on
a violating factor — 6–8% of binds, against zero before. The violation-pair
coverage queue now gives every ordinary provision one plain denial before
covering the remaining factors, so a provision whose violating factors are
all shared with earlier siblings still reaches its scenario's B cell.

With deny-side records present the 5.13.0 adverse-fact rung has corpus work
to do: 1–8 permit records per pack fall on a violating factor they never
saw, every one within the rung's definition and none of them controlling;
VC-51 and VC-55 are corpus-aware rather than asserting zero.

## What an amendment unsettles, now that there is something to unsettle

`tools/amendment_overlay.py` adopts at the first quartile (the
precedent-heavy categories are scheduled early) and sweeps the most-bound
and the most deny-side-bound provisions. A limb amendment now unsettles
1–4 records and 2–8 binds per deny-side provision; a compliant-factor
amendment unsettles up to 32 binds on a permit-side provision; a
citation-only amendment unsettles nothing. Of the packs' filed draft
amendments, Meridian's twelve would unsettle 12 binds and 4 records if
adopted today; the others target provisions whose records are all
permit-side. Results in `tools/extraction/results/amendments_*.json`.

## No law on facts nobody established (engine)

Re-running the facts round-trip on the new corpora exposed a rule that had
been missing since 5.11.0. When the characterisation stage leaves a factor
unrecorded and the case is then contested and admitted, the record was
written with that factor *dropped from the premise* — a premise narrowed by
silence, which binds cases the instance never decided. On one pack that was
167 cases bound where the reference had abstained. A contested case whose
hinted premise carries an unrecorded factor is now decided but its record
is **withheld** (`trace.record_withheld`, referral emitted) until the fact
is established; the consolidation representative is held to the same rule.
VC-52 gains the probe; M31 removes the rule and dies. Measured on the five
packs with the cued baseline: 42–154 records withheld, bind retention
0.87–0.96, and **zero cases bound where the reference abstained on every
pack** — the property the record stage established for premise, stance and
scope now holds for facts too.

## Suites and measurements

Division packs: 56/56 conformance, 31/31 faults killed and 4/4 controls
survived (M31), zero construction anomalies, deterministic rebuild,
cross-pack composition identical (largest route spread 0.55 pp, decision
spread 2.53 pp). Numerals unchanged at 11/11, 7/7 + 2/2. Every table in
`tools/extraction/README.md` — facts, records, tolerance sweep, amendments —
is regenerated on corpus 2.1.0 and the JSONs in `tools/extraction/results/`
are the ones behind it.

## What moved in the headline figures, and why

Facts ε on precedent: 0.87–0.96 (was 0.93–0.98). The difference is the
withheld records — the honest price of not writing law on silence. The
record stage's held-out-phrasing result is unchanged in kind (binds lost,
never gained). The overlay's exactness price is 8–17% of boolean binds (was
8–18%) and its false-bind bound rises from 2–10% to 6–16% across the sweep
(was 2–7% → 7–19%); the falsifier at magnitude still reads 2–3%.
