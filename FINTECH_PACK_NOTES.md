# Added: `fintech` — a reference constitution for a large fintech

A fifth demo corpus, different in kind from the other four. `sctower`,
`vetpoc`, `dcvigil`, and `frontierllm` are converted Paper-3 case studies.
`fintech` is an **authored reference constitution** assembled from
public-domain regulatory instruments, intended as a realistic starting
rulebook rather than a simulation artifact.

**37 provisions (11 absolute) · 23 seed holdings · 68 scenarios · 0
expectation mismatches.**

## Read this before treating it as a compliance artifact

This rulebook will not let a fintech stop worrying about compliance, and no
artifact can. It governs **code changes**. It says nothing about capital,
licensing, chartering, examination readiness, or whether a control is
actually operated as designed once merged — and a rulebook that passes review
is not the same thing as a firm that complies. Every provision needs counsel
review before it governs anything real.

What it does give you is a defensible starting position in which every
provision names its source, so a compliance reviewer can argue with it line by
line. That is the useful property, and it is a real one.

## The decision that shapes everything else

`absolute` is **not a severity ranking**. It is a claim about *who may
decide*. An absolute provision is short-circuited at tier 1 (A6), can never be
risk-accepted at any tier, and exits only through an amendment.

So `absolute` is reserved for the 11 obligations where **no officer of the
firm holds the authority to accept the risk**: strict-liability sanctions
(31 CFR Ch. V), criminal tipping-off (31 U.S.C. §5318(g)), EU AI Act Art. 5
prohibitions, ECOA prohibited-basis variables, SOX audit-trail integrity, and
so on.

Everything a regulator would let you document, compensate, and time-box is
deliberately adjudicable — GLBA encryption (16 CFR §314.4(c)(3) contemplates a
CISO finding), NYDFS MFA (§500.12(a) names the compensating-control path),
SR 11-7 validation. Encoding those as absolute would be a lie about the firm's
own authority: it would push routine, defensible exceptions through
constitutional amendment, and a constitution amended weekly is not a
constitution.

`docs/FINTECH_REGULATORY_REGISTER.md` gives the per-provision rationale.

## Three positions that were checked, not remembered

1. **EU AI Act Omnibus, in force 27 July 2026** — standalone Annex III
   high-risk obligations deferred to **2 December 2027**, Annex I to 2 August
   2028. Art. 5 prohibitions (since 2 Feb 2025) and Art. 50 transparency
   (from 2 Aug 2026) were **not** deferred. Hence MF-107 is absolute and in
   force while MF-304 is a dated readiness provision. A single "EU AI Act"
   provision would have flattened that split and got it wrong.
2. **12 CFR Part 1033 is enjoined** (E.D. Ky., October 2025) and under CFPB
   reconsideration. MF-405 states its own contested status in the provision
   text and binds on architecture, not on a date.
3. **PCI DSS v4.0.1 and NYDFS universal MFA are both fully live** — since
   31 March 2025 and 1 November 2025 respectively. Neither is a future
   obligation.

Anthropic's constitution for Claude (January 2026) is CC0, so genuinely public
domain; it supplies MF-111 (human oversight of agents that move money) and
MF-306 (honesty on AI-facing surfaces).

## Generated, not hand-written

```bash
python3 demo/build_fintech_pack.py       # pack + rebuild _all
python3 demo/build_fintech_register.py   # the register doc
```

Both are idempotent. The register is generated from the pack so it cannot
drift from the constitution it describes.

Scenario expectations are **computed** from the documented adjudication
semantics (`build_fintech_pack.py::solve()` mirrors `adjudicate.py`) and then
verified against a live replay through the real inbound gateway. None are
hand-asserted and none are back-filled from engine output, so a drifting
engine surfaces as a mismatch instead of being silently absorbed.

`verify()` refuses to build on: a factor that is both a deny-trigger and a
precedent mitigator (which would collapse the distinguishing gate), a premise
containing facts its case never had (Def. 8), a precedent on an absolute
provision (A6 short-circuits before retrieval, so none can exist), a tier-4
seed without the risk-owner branch, or an acceptance without an expiry (A7).

## Two design defects found and fixed during construction

- `MP-002` bound to ordinary secret-in-source cases at exactly the retrieval
  threshold (Jaccard = 0.25), so the distinguishing demonstration was
  resolving on an unrelated CI-log holding. Premise scoped to its own fact
  pattern.
- `MP-007` lost on authority to a tier-3 shadow-mode holding, so the corpus
  *permitted* an unvalidated model influencing live credit decisions. Moved to
  the risk owner, where that judgment belongs.

`D01`/`D02` now turn on authority tier, `D03` on recency, and all seven
`E-distinguish` cases fall through to the predicate with no controlling
record.

## Deliberately not done

- **`seed/rulebook.json` is untouched.** All three conformance suites pin the
  `SC-2xx` provisions by id; replacing the default seed would break 137 checks
  unrelated to fintech. To boot the platform on this constitution, use
  `DJ_CONSTITUTION_PATH` or run it as a tenant corpus (`DJ_DEMO=fintech`).
  Making it the shipped default is a release decision, not a build step.
- **`VERSION` still reads `5.5.0`** although the archive is labelled 5.6.
  Flagged rather than bumped — version numbering is yours to set.

## Known limits

- **Scope**: change-time governance only.
- **Jurisdiction**: US federal, New York, California, EU. Nothing for FCA,
  MAS, or RBI.
- **The factor vocabulary is the weak joint.** A provision only fires when the
  extractor labels a change with the right factor; mapping these onto real CI
  signals in `seed/github_factor_map.json` is engineering this pack does not
  do.
- **Currency**: checked August 2026, and Part 1033 is actively in flux.

## Verification performed

- `fintech` replay: 68 scenarios, **0 expectation mismatches**, verification
  clean.
- `_all` replay: 468 scenarios across 6 tenants, namespaces verified disjoint.
  **2 mismatches — `dcvigil:D03` and `dcvigil:D04` — confirmed pre-existing**
  in the package as uploaded, byte-identical to the unmodified 5.6 archive.
  This pack adds none.
- Conformance: **47/47 kernel, 41/41 interface, 49/49 extension** (reports
  regenerated; all three came back byte-identical to the shipped ones).
- All 37 provisions render at `/review/rulebook` with citations intact; all
  eight authenticated review routes return 200 for the fintech tenant.
- A7 lifecycle: the seeded lapsed acceptance `MP-023` is marked `lapsed=1`,
  appears in the filtered ledger view, and drives the renewal-guard banner on
  the open `MF-304` review task.
