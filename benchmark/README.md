# Paper 3 benchmark — running on the deployed framework

The harness no longer scores a reimplementation of the Digital Judiciary. All
three conditions now run against the same container an enterprise would
install, through the same inbound interface a real pull request arrives on.

## The three conditions

| | Store | Lapse filter | Distinguishing gate | Ordering | Floor short-circuit | Model's job |
|---|---|---|---|---|---|---|
| `rules_only` | none | — | — | — | — | decide |
| `b_mem` | full `precedent_record`, retrieval only | **no** | no | no | no | decide |
| `dj` | `record_effective` | yes | yes | authority → recency → scope | yes | `distinguish()` only |

Held constant across all three: the extracted facts, the engaged provisions,
the retrieval metric (Jaccard, θ = 0.25), the rulebook, and the seeded
jurisprudence — all read from one seeded container. **Only the governance
semantics vary.** That is what makes this an ablation of the architecture
rather than a comparison of prompt wording.

Two consequences worth stating in the paper:

* In `dj` the model never issues the decision. It answers one question per
  retrieved candidate — does this precedent's holding rest on something the
  present case lacks — and the architecture does the rest. Per-case model cost
  is therefore a function of *candidates retrieved*, not of case difficulty.
* In `b_mem` the memory deliberately includes acceptances that have lapsed and
  acceptances whose referral the lawmakers rejected. Nothing in that condition
  tells the model which memories still carry authority. `relied_on_lapsed_rate`
  measures how often it leans on one anyway.

## Running

```bash
python3 tier_benchmark.py --company all --condition rules_only
python3 tier_benchmark.py --company all --condition b_mem
python3 tier_benchmark.py --company all                       # dj (default)
python3 tier_benchmark.py --company all --tiered              # model ladder
```

`--mock` runs the whole pipeline offline with deterministic stand-ins and no
API key. Add `--no-ui` to skip the dashboard.

| Flag | Default | Meaning |
|---|---|---|
| `--condition` | `dj` | `rules_only` \| `b_mem` \| `dj` |
| `--model` | `sonnet` | `haiku`\|`sonnet`\|`opus` or a full model id |
| `--tiered` | off | sweep the model ladder (adds `_<model>` to filenames) |
| `--escalate` | `manual` | `auto` walks the challenge ladder on every denial |
| `--isolation` | `run` | `case` reseeds the store before every case |
| `--pricing` | `pricing.json` | cost metrics stay null until this is filled in |
| `--mock` | off | offline pipeline check |

Outputs: `results_<company>[_condition][_model].csv`,
`summary_<company>[_condition][_model].json`, `dashboard.html`.

### Two knobs that change what the numbers mean

**`--isolation`.** `run` (default) lets precedent accumulate across the corpus
in corpus order, which is what production looks like: case 12 can be resolved
by a record case 4 created. `case` reseeds before every case, which isolates
each decision but destroys the accumulation effect. Report which one you used;
they answer different questions.

**`--escalate`.** `manual` (default) preserves Corollary 2 — a challenge is an
act somebody takes, and an unchallenged tier-1 denial stays a tier-1 denial.
`auto` contests every denial up the ladder, which measures the ladder's ceiling
rather than its realistic behaviour. Auto-escalated challenges are written into
the contest chain with grounds that say so, so a reader of the trace can always
tell simulation from practice.

## Reading the results honestly

**A mock `dj` run proves nothing about judgment.** It puts the deterministic
premise-subset oracle at the judge position, and that oracle cannot be wrong
about its own definition, so agreement near 1.0 is expected and empty. It
checks that the mechanism works. Drop `--mock` to put a real model at the
judge position, which is the measurement the paper actually wants.

**Gold labels are designed, not adjudicated.** Every case in
`companies/*/corpus.jsonl` carries a `why` field arguing the disposition from
the written rulebook and the seeded jurisprudence. That is a defensible
construction, not an expert consensus. Phase 2 replaces the labels with
adjudicated expert judgments and reports κ; until then every agreement number
is a pipeline check. The `gold_source` field in each summary says `designed`
so this cannot quietly be forgotten.

**Fidelity is not accuracy.** `a6_floor_fidelity` and
`a3_control_plane_fidelity` measure whether a condition respected a property
the architecture guarantees by construction. In `dj` both are mechanical and
must read 1.000 — anything else is a defect report, not a finding. In the
baselines they are behavioural, and that gap is the interesting number.

**Split the error direction.** `permissive_errors` (let through what should
have been held) and `restrictive_errors` (held what should have proceeded) are
reported separately because they are not equally costly, and a single accuracy
figure hides which way a condition fails.

## Adding a company

```
companies/<key>/
  company.json     names the rulebook, store seed and factor map to use
  corpus.jsonl     one JSON object per case (see below)
```

A corpus case:

```json
{"id":"XX-C01","class":"covered","provision":"SC-201",
 "gold":{"disposition":"proceed_with_conditions","outcome":"permit_conditional"},
 "why":"the argument for this label, from the rulebook and the store",
 "pr":{"number":1001,"title":"…","body":"…","labels":["…"],
       "files":["path/one.py"],"checks":[["check-name","failure"]],
       "author":"dev-jo"}}
```

`class` drives the by-class breakdown. The classes carried today are
`covered`, `distinguishable`, `novel`, `tie`, `floor`, `floor_adjacent`,
`floor_first`, `control_plane`, `lapsed_trap`, `multi_provision`,
`self_asserted`, `authority_over_scope`, and `clean`.

A company with a different factor vocabulary needs its own factor map; point
`company.json` at it and the harness will load it per run. The rulebook and
store seed are loaded from wherever `company.json` points, so VetPOC and
DCVigil each get their own constitution and jurisprudence without touching the
framework.

## One result the SC corpus surfaced

`SC-C18` was written expecting a denial and the framework permitted. Both
`SP-002` (tier 4, org-wide, community audit) and `SP-003` (tier 3, telematics,
deny) hold their premises on those facts, so neither is distinguished, and
**authority is the first elimination key** — the tier-4 risk-owner holding
outranks the later, narrower domain tightening. That is the declared ordering
working exactly as specified, and it is worth a paragraph in the paper: under
this ordering a broad tier-k acceptance survives a subsequent domain-specific
tightening until someone challenges it or the lawmakers legislate. The case is
kept in the corpus under the class `authority_over_scope` rather than being
quietly retuned.
