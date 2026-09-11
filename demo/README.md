# Demo corpus — the original Paper-3 scenarios, replayed on boot

A container that starts empty demonstrates nothing. `DJ_DEMO=<company>` boots
onto one of the four converted case-study corpora and replays its 100 scenarios
through the **real inbound gateway**, so the container comes up with a populated
docket and a review queue that has actual work in it.

```bash
docker run -p 8080:8080 -e DJ_DEMO=sctower -e DJ_DEV_KEYS=1 digital-judiciary
# or locally:
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=dcvigil python3 serve.py
```

Then: `http://localhost:8080/review` (sign in with the `coo.pat` key) and
`GET /v1/demo/status`.

| Company | key | provisions | seed records | cases |
|---|---|---|---|---|
| SC Control Tower | `sctower` | 21 | 37 | 100 |
| VetPOC | `vetpoc` | 20 | 37 | 100 |
| DCVigil | `dcvigil` | 21 | 37 | 100 |
| FrontierLLM | `frontierllm` | 21 | 37 | 100 |
| Meridian Financial | `fintech` | 37 | 23 | 68 |

The first four are converted Paper-3 case studies. **`fintech` is different in
kind**: it is an authored reference constitution for a large multi-jurisdiction
fintech, assembled from public-domain regulatory instruments (EU and US) and
Anthropic's CC0 constitution for Claude, with the citation carried in each
provision's own text. See `docs/FINTECH_REGULATORY_REGISTER.md` for the
provision-to-instrument mapping and — more importantly — for why each provision
is or is not `absolute`.

It is regenerated, never hand-edited:

```bash
python3 demo/build_fintech_pack.py       # pack + rebuild _all
python3 demo/build_fintech_register.py   # docs/FINTECH_REGULATORY_REGISTER.md
```

Its scenario expectations are computed from the documented adjudication
semantics and verified against a live replay, so a drifting engine shows up as
a mismatch rather than being silently absorbed.

To boot the platform on this constitution rather than the default SC seed,
point the constitution path at it (`DJ_CONSTITUTION_PATH`) or run it as a
tenant corpus (`DJ_DEMO=fintech`). The shipped `seed/rulebook.json` is
deliberately left alone: all three conformance suites pin the `SC-2xx`
provisions by id, and replacing the default seed would break 137 checks that
have nothing to do with fintech.

A representative boot (identical shape for all four):

```
blocked_challengeable   35      proceed                 20
proceed_with_conditions 21      blocked_absolute         8
human_review            10      routed_amendment         6
open review tasks       10   -> /review
```

## Configuration

| Env | Default | Meaning |
|---|---|---|
| `DJ_DEMO` | unset | company key; unset means no demo, default SC seed |
| `DJ_DEMO_LIMIT` | `0` | replay only the first N scenarios |
| `DJ_DEMO_SIGN` | unset | `1` closes the tier-k reviews with a stand-in policy |
| `DJ_SEED_STORE` | `store_seed.json` | `store_seed_initial.json` for the pre-run store |

The demo is **idempotent by delivery id**: restarting against an existing
volume adds nothing and changes nothing.

## Nothing here bypasses the Kernel

Every scenario is posted to `PRGateway.receive`, which files cases through
`Adjudicator`, which is checked by the Challenge Gate. The demo cannot and does
not write precedent directly. It also does not decide the tier-k cases:
`contest_to = 4` means somebody pushed the case all the way up, and who signs it
is a human act, so those tasks are **left open** in the queue. That is the point
of the demo, not a gap in it.

## What the conversion had to decide, and how it was checked

The original simulation (`groundtruth_<company>.json`) ran against a standalone
formal engine. Re-expressing it in the container's vocabulary needed three
judgement calls. All three are recorded rather than buried, and
`demo/build_packs.py` regenerates the packs from the original at any time.

**1. Deny predicates were derived, then verified.** The original provisions
carry text and an `absolute` flag but no fact-predicate: whether a case violated
its provision was a declared scenario property, exactly like `contest_to`. The
container's tier-1 evaluation needs a real predicate, so one is derived as

```
deny_if_any(P) = {factors of violating cases engaging P}
               - {factors appearing in any premise of a record on P}
               - {"compliant"}
```

Subtracting premise factors matters: a premise factor is a *mitigating* fact,
and promoting it to a trigger would collapse the distinguishing gate into the
predicate. The derivation is then checked case by case against the original's
own `tier1_decision`, and the build fails loudly on any disagreement. It
currently **reproduces the original tier-1 decision on all 404 cases**.

**2. Every timestamp is shifted by one constant.** The corpus has an implicit
as-of date it never states: all ten of its acceptances carry a
`referral_status`, which is only true at an instant later than the latest expiry
in the file. Replayed against today's clock, seven of those ten would still be
live and the lapse, renewal, and Proposition-2 scenarios would silently not
fire. So the whole corpus is shifted by a single declared offset
(`date_offset_days`, currently −89) that puts the latest expiry a week in the
past. A constant offset preserves every relative ordering, which is what the
recency elimination key reads.

**3. Provision engagement is replayed, not inferred.** Which provisions a change
engages was a scenario property in the original (`prov`). The demo replays it
rather than fabricating a GitHub factor map for four companies × ~21 provisions.
Floor-first ordering is still read from the live constitution at replay time, so
**A6 is enforced by the container, not by the corpus** — a scenario cannot
declare itself non-absolute.

## The one known divergence

The corpus is a *sequence*: 17 records existed at the first case and the other
22 were created by the run itself. `store_seed.json` seeds all 39 up front,
which makes every mechanism demonstrable immediately but is slightly
anachronistic — an early case can be controlled by a record the original
narrative created later.

This affects exactly the cases listed in `anachronism_cases` (visible in
`/v1/demo/status`): `G04`, where the container retrieves a same-provision record
with Jaccard 1.0 that did not yet exist at that point. **All 404 cases reproduce
the recorded disposition on the full store**, and the four packs mismatch a
uniform two cases each on the initial store, which are reported at boot rather
than smoothed over.

`D03` and `D04` were formerly listed here as DCVigil-only anachronisms. They
were not: they were a corpus-authoring divergence, and separately the ordering's
authority key ranked three tiers where the specification states two. The key was
corrected to two levels on 24 August 2026 and the three packs whose `expect`
blocks had been written against the three-tier behaviour were updated to match.
All four packs now agree.

Set `DJ_SEED_STORE=store_seed_initial.json` to seed only the original 15 and let
the run regrow the store, which is narratively faithful. Note the trade-off: 8
of the 10 acceptances were created mid-run by risk-owner decisions, so with the
initial store the lapse and renewal scenarios only populate if you also set
`DJ_DEMO_SIGN=1`.

## Honest framing

This is a **synthetic case study replayed through the interface**. It is not
production traffic, and it is not a benchmark result. Ground truth is the
original formal engine applying the papers' procedure with the deliberately
simple `similar`/`distinguish`; agreement with it is procedure-agreement, not
correctness. For measurement, use `benchmark/` — which scores three conditions
against the same deployed artifact — and keep the two apart in any write-up.
