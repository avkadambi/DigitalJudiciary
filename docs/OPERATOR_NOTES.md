# Operator notes — the single-container service, its knobs and its history

*This file is the former README's operating manual, kept whole. For what the
repository is and how to reproduce the papers, start at the root `README.md`
and `REPRODUCE.md`; for release-by-release history, `CHANGELOG.md` and
`docs/releases/`.*

# Digital Judiciary **5.0** (Enterprise Platform)

# The Digital Judiciary — Single-Container MVP (reviewed rebuild)

A working implementation of the Digital Judiciary (Kadambi, *The Digital
Judiciary*, preprint v2.8) per **System Design Specification v3.0**, packaged
as **one container with no external dependency except calls to external AI
services** — and even those are optional (`DJ_JUDGE_MODE=llm`).

The image is CPython 3.12 + the Python standard library. There are **zero
pip installs**: SQLite is the substrate, `http.server` is the API, `urllib`
is the AI client. Supply-chain surface = CPython.

## Documentation

- `PAPERS.md` — how "Chapter 4/5/6" references in the code map to the papers.
- `PAPER_ALIGNMENT.md` — what the benchmark paper registers against what this
  artefact executes, item by item, with the numbers.
- `CITATION.cff` / `.zenodo.json` — how to cite; the Zenodo record metadata.

- `docs/USER_GUIDE.md` — end-user guide: what each screen means, what your role
  can do, and how to read the signals. Assumes no knowledge of the architecture.

## Install

```bash
./install.sh --check     # what is missing; changes nothing
./install.sh             # check, offer to install, verify, build the demo
./install.sh --yes --company _all --sign
```

There are **no third-party Python packages** — the whole system is the
standard library plus SQLite, so there is no pip step and nothing is
downloaded from the internet. Prerequisites are tested by *capability* rather
than version number: the installer runs the actual JSON1 and `DROP COLUMN`
queries the ledger depends on, because a version string says what was
intended and the query says what works. Nothing is installed without an
explicit yes, and the exact command is printed first.


```
docker build -t digital-judiciary .
docker run -p 8080:8080 -v dj-data:/data digital-judiciary
# founding principal keys print once on first boot (the bootstrap ceremony)

# The conformance suite — the paper's Table 11, computed live:
docker run --rm digital-judiciary python3 run_conformance.py
# => RESULT: 49/49 checks hold

# Optional LLM distinguishing gate (the container's only external call):
docker run -p 8080:8080 -v dj-data:/data \
  -e DJ_JUDGE_MODE=llm -e ANTHROPIC_API_KEY=sk-... digital-judiciary
```

No Docker? `DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 python3 serve.py` runs anywhere
Python 3.12 exists.

**Upgrading an existing database.** Schema changes migrate in place on boot —
columns are added, views rebuilt — so pointing `DJ_DB` at an old file is safe.
What cannot migrate is data written *before* a column existed: those rows are
immutable by design and will keep their blanks forever. A demo from an older
build therefore needs rebuilding rather than patching:

```bash
python3 demo/reset.py --check              # what is in there, and is it stale
python3 demo/reset.py                      # rebuild ALL four companies (default)
python3 demo/reset.py --company sctower    # just one

# Stop the server first. A running server holds the old file open and will
# keep serving it, which looks exactly like the reset having done nothing.
# And DJ_DB must be the same path you rebuilt.
```

The old file is moved aside with a timestamp, never deleted in place. The
ledger's own tables refuse DELETE, and the script holds itself to the same
rule.

```
# Boot onto a case-study corpus: 100 scenarios replayed through the real
# inbound gateway, leaving a populated docket and a non-empty review queue.
docker run -p 8080:8080 -e DJ_DEMO=sctower -e DJ_DEV_KEYS=1 digital-judiciary
#   -> /review              the risk owner's queue (10 open decisions)
#   -> /v1/demo/status      what was replayed, and the known caveats
# Companies: sctower | vetpoc | dcvigil | frontierllm — or _all, which boots
# every tenant into ONE multi-tenant ledger (400 scenarios, 4 organizations)
# and scopes every screen by the signed-in principal. See demo/README.md.
docker run -p 8080:8080 -e DJ_DEMO=_all -e DJ_DEV_KEYS=1 digital-judiciary

# The L5 interface suite — inbound, outbound lanes, and the review screen:
docker run --rm digital-judiciary python3 run_interface_conformance.py
# => RESULT: 41/41 interface checks hold

# The L6 suite — tier differentiation, judged premise, judicial referral:
docker run --rm digital-judiciary python3 run_extension_conformance.py
# => RESULT: 45/45 extension checks hold
```

---

## Improvements in this build (v3.1-hardened)

Relative to the reviewed single-container baseline:

1. **Constant-time API-key comparison** — `hmac.compare_digest` over the full principal table, so authentication is not timing-sensitive on the hash path.
2. **Non-constant default chain key** — `DJ_CHAIN_KEY` still preferred; if unset, a key is derived from the DB path rather than a published string.
3. **Structured errors + request IDs** — every JSON response carries `request_id`; errors include a stable `code` field; `x-request-id` and `x-content-type-options` headers set.
4. **`GET /v1/admin/status`** — public operator snapshot (rulebook, provision list, precedent/case/principal counts, judge mode). No secrets.
5. **Input validation** — `POST /v1/cases` rejects non-list or non-string `facts` with 422 before any Kernel work.

All 48 conformance checks continue to hold. Zero new dependencies.

---

## Scale envelope (single-container)

This build is deliberately a **single-process, SQLite, zero-dependency**
artifact. It is comfortable for demos, paper conformance, and low-volume
pilots. It is **not** a horizontally scaled production service.

| Signal | Comfortable | Plan migration |
|---|---|---|
| Active holdings (precedent_record) | ≤ ~2 000 | ≥ ~10 000 |
| Concurrent review users | low (single process UI) | many concurrent risk owners |
| PR volume | tens–low hundreds / day | high CI throughput |

**What this release adds inside the constraints**

1. **Process-local active-holdings cache** (`ActiveHoldingsCache` in the
   Kernel). `retrieve()` no longer re-scans `record_effective` on every
   case against the same provision. The Challenge Gate invalidates the
   cache on every admit and on lifecycle events that change lapsed /
   superseded state, so the cache stays coherent with the sole writer.
   Disable with `DJ_HOLDINGS_CACHE=0`.
2. **Composite index** `pr_provision_org` on `(provision_id, organization)`
   so the SQL load that fills the cache is index-backed.
3. **Configurable candidate cap** — `DJ_MAX_CANDIDATES` (default 25)
   bounds the distinguish stage regardless of store size.
4. **SQLite performance pragmas** — larger page cache
   (`DJ_SQLITE_CACHE_KIB`, default 65536 = 64 MiB), `temp_store=MEMORY`,
   `synchronous=NORMAL` (safe with WAL).
5. **Operator visibility** — `GET /v1/admin/status` now reports cache
   stats, process-local metrics (retrieve hits/misses, rows examined,
   admits), config knobs, and soft scale warnings when the ledger grows.

**Knobs (all optional)**

| Env | Default | Meaning |
|---|---|---|
| `DJ_THETA` | `0.25` | Jaccard similarity threshold |
| `DJ_MAX_CANDIDATES` | `25` | Hard cap on candidates per retrieve |
| `DJ_HOLDINGS_CACHE` | `1` | Process-local active-holdings cache |
| `DJ_SQLITE_CACHE_KIB` | `65536` | SQLite page cache size (KiB) |

The axioms, the sole-writer Gate, the immutability triggers, and the
zero-dependency story are unchanged. Authentication hardening remains
out of scope for this pass.

---

## Review decisions (what a distinguished-engineer pass changed, and why)

The single-container goal forces substitutions for the v3.0 substrate
(PostgreSQL, Temporal, Keycloak, OPA). The review rule was: **a substitution
may change the mechanism, never the guarantee** — every axiom keeps a
physical enforcement point, and the conformance suite proves it against
executed traces, not prose.

| # | Decision | Replaces | Guarantee preserved by |
|---|----------|----------|------------------------|
| R1 | **SQLite, WAL, in-process** | PostgreSQL + pgvector | Same CHECKs; `RAISE(ABORT)` triggers for immutability; an insert-trigger replays the `EXCLUDE`-constraint semantics for A1; **read-only connections** (`mode=ro`) are the physical form of the §11.2 SELECT-only roles — probed live (PRB-7) |
| R2 | **Stdlib only, zero pip** | FastAPI/uvicorn stack | ~50 MB image; no supply chain beyond CPython; the API is 10 routes and a framework buys nothing at that size |
| R3 | **Sole-writer as object capability** | DB role grants | The ledger writer connection is created inside `ChallengeGate.__init__` under a name-mangled attribute and never escapes; nothing else in the process can insert a precedent (Def. 7) |
| R4 | **HMAC hash-chained contest events** | Signed Temporal histories | The Gate verifies chain integrity + tier coverage before any tier-k admission (A4 / CC-06); the chain key lives in `DJ_CHAIN_KEY` |
| R5 | **Durable artifact, then idempotent admit** | Temporal activity boundary | Stage-2 artifacts persist to `case_state` before admission; a crash replays admission (idempotent on `content_hash`), never re-adjudication (A5) |
| R6 | **Daemon-thread sweep, event-sourced lapse** | Temporal Schedule | Lapse is a **view over the event log + clock**, so the sweep is idempotent by construction; emitting `lapsed` twice is harmless |
| R7 | **Declarative factor predicates** | OPA/Rego, Cedar | `deny_if_any` / `deny_if_missing` over the factor set; deterministic, versioned with the rulebook; swap OPA back in behind `rule_eval()` unchanged |
| R8 | **Deterministic oracles by default** | LLM judges | The paper's §11.5 reference oracles (Jaccard θ=0.25; premise-subset). Bit-for-bit reproducible — the only mode the conformance suite certifies. `DJ_JUDGE_MODE=llm` swaps in the real gate behind the same provenance-recording interface, with the §12 degradation policy (miss ⇒ NOT distinguished + degraded; pivotal degraded ⇒ escalate) |
| R9 | **Errata to v3.0 schema** | `CHECK (tier<4 OR expiry NOT NULL)` | That check forbade the paper's own "RiskOwner upholds the denial" record. Corrected: the expiry obligation attaches to **acceptances** (`is_acceptance ⇒ tier=4 ∧ expiry NOT NULL`), and the corpus exercises the decline path (GB) |
| R10 | **Fixed in test: none-state collapse** | — | When every candidate was distinguished, `order()` reported `none_empty`. The empty/all-distinguished distinction is now made where candidates are still visible — two causes the auditor must be able to tell apart (Def. 11) |

**What did not change:** every axiom, the challenge gate, the elimination
ordering with explicit ties, binding-not-advisory consult, pivotal-verdict
quorum, the renewal bar, control-plane routing, and pinning of the rulebook
version at intake.

## Layout

```
serve.py               entrypoint: schema → bootstrap ceremony → sweep → API
run_conformance.py     corpus + violation probes + CC checks; exit 0 iff green
app/db.py              L1: schema, CHECKs, triggers, ro/rw connections
app/kernel.py          L2: Registry, Constitution, Ledger, Gate, Provenance, chain
app/judges.py          the two black boxes: oracle (default) and LLM
app/adjudicate.py      L3: intake, tier-1, resolve(), escalation, risk acceptance
app/lifecycle.py       A7 sweep + referral-outcome mirroring
app/httpapi.py         L4: REST surface (SDD §10.2)
app/prfacts.py         L5: PR signals -> facts, versioned and pinned
app/inbound_github.py  L5: a pull request becomes cases (HMAC-authenticated)
app/outbound.py        L5: resolution -> disposition + the exits that remain
app/review.py          L5: the human-review task; ui | jira | servicenow sinks
app/reviewui.py        L5: the server-rendered docket the risk owner signs
app/demo.py            replays a case-study corpus on boot (DJ_DEMO)
run_interface_conformance.py   the L5 suite: 41 checks from executed traces
seed/rulebook.json     SC Control Tower provisions (2 absolutes) + A9 standing declaration
seed/store_seed.json   seed jurisprudence incl. conflicting pairs + 2 lapsed waivers
demo/companies/<co>/   four converted case-study corpora, 100 scenarios each
```

## The interface (L5)

A pull request arrives at `POST /v1/inbound/github`, authenticated by GitHub's
HMAC rather than a bearer key, and filed as `svc:github` — a principal that
holds **no branch**, so a compromised gateway can file bad cases and lie to
GitHub but cannot decide one. The answer back is a disposition plus *the exits
that remain open*, which is the mechanical form of Corollary 2:

```
POST /v1/inbound/github                     # webhook (HMAC; no bearer)
GET  /v1/pr/{session}                       # the read model
POST /v1/pr/{session}/challenge             # lane 1: climb a tier
POST /v1/pr/{session}/human-review          # lane 2: reach a named person
GET  /review , /review/{task}               # the screen where they sign
GET  /review/changes                        # the change stream, by tenant
GET  /review/change/{session}               # one change: clauses, facts, lanes open
POST /review/change/{session}/challenge     # contest it, from the screen
GET  /review/amendments                     # the legislature: proposals + referrals
GET  /review/impact                         # what governance cost and bought
GET  /review/analytics                      # cost per level of escalation
GET  /review/activity?kind=&q=&tenant=&since= # everything the system has done
GET  /review/rulebook                       # the rules in force, in plain English
GET  /review/rulebook/history               # every proposal to change them
GET  /review/ledger?status=&provision=    # the precedent register: census, filters, keyset paging
GET  /review/ledger/{id}                    # one record's holding, premise and lifecycle
GET  /review/login   POST /review/login     # sign in, or switch principal
POST /review/logout                         # clear the session credential
GET  /v1/demo/status                        # demo corpus state
```

An absolute denial offers neither lane, because neither exists (A6/CC-08); the
only exit is the amendment channel. Jira and ServiceNow are written as real
payload builders that record what they would send and go live when their base
URL and token are set, so adopting them is a deployment change, not a code
change.

## API (Bearer = principal API key; branch resolved at the point of action)

```
POST /v1/cases                          {provision_id, facts[], case_scope?}
POST /v1/decisions/{case}/challenge     {grounds}          # tiers 2..k−1, then RiskOwner
POST /v1/decisions/{case}/accept                            # finalize; depth≥2 ⇒ stored
POST /v1/cases/{case}/risk-decision     {decision: accept|decline, rationale, expiry?}
GET  /v1/decisions/{case}
GET  /v1/records/{id}     GET /v1/records/{id}/dossier      # rebuild(): fields only
GET  /v1/constitution/current
POST /v1/amendments        POST /v1/amendments/{id}/decision # Lawmakers only
POST /v1/admin/lifecycle-sweep
```

Submitting `provision_id: "constitution"` is never a case — it routes to the
amendment channel (A3; the paper's Example 3).

## Conformance

`run_conformance.py` boots the container process on a fresh DB and computes
48 checks from executed traces: a mechanism-complete corpus (routine,
violation, citation, all three ordering keys, the distinguishing gate,
absolute short-circuit, tie ⇒ none, lapse, renewal-while-pending, the
Proposition-2 renewal **bar**, upheld denial at tier k, control-plane
routing, novelty ⇒ new precedent ⇒ citation of it, amendment adoption);
ten **violation probes** where each guarantee must *fail correctly when
attacked*; and the CC checks of SDD §4 (CC-01/02/04/06/07/08/09/10/11/14/15/16/17,
CC-17 being the A9 standing-declaration check).
Wire it into CI as the merge gate for this repo.

## Configuration

| Env | Default | Meaning |
|-----|---------|---------|
| `DJ_DB` | `/data/judiciary.db` | SQLite path (mount a volume) |
| `DJ_PORT` / `DJ_HOST` | `8080` / `0.0.0.0` | API bind |
| `DJ_JUDGE_MODE` | `oracle` | `oracle` (deterministic) or `llm` |
| `ANTHROPIC_API_KEY` | — | required iff `llm` |
| `DJ_JUDGE_MODEL` | `claude-sonnet-4-6` | LLM judge model (all tiers) |
| `DJ_JUDGE_MODEL_T1/T2/T3` | — | per-tier model; makes escalation a real ladder |
| `DJ_SIMULATOR` | unset | `1` ⇒ the live scenario generator at `/review/admin` |
| `DJ_PRICE_IN` / `DJ_PRICE_OUT` | `3.00` / `15.00` | $ per million tokens, for `/review/analytics` |
| `DJ_SIMULATOR_MODEL` | `claude-sonnet-4-6` | model that proposes new scenarios |
| `DJ_QUORUM_T1/T2/T3` | `3` | samples per pivotal verdict, per tier |
| `DJ_PREMISE_MODE` | `mechanical` | `judged` ⇒ the model proposes what the holding rests on |
| `DJ_JUDICIAL_REFERRAL` | `1` | file a DraftAmendment on an unbroken conflict |
| `DJ_REFERRAL_ACCEPTANCE_N` | `3` | acceptances on one provision before referral |
| `DJ_THETA` | `0.25` | similarity threshold θ |
| `DJ_CHAIN_KEY` | dev value | HMAC key for contest chains — **set in prod** |
| `DJ_DEV_KEYS` | unset | `1` ⇒ deterministic dev principal keys **and the review sign-in roster** |
| `DJ_GITHUB_WEBHOOK_SECRET` | — | HMAC secret; unsigned intake needs `DJ_GITHUB_ALLOW_UNSIGNED=1` |
| `DJ_GITHUB_TOKEN` | — | unset ⇒ outbound is recorded, not transmitted |
| `DJ_REVIEW_SINK` | `ui` | `ui`, `jira`, `servicenow` (comma-separated) |
| `DJ_DEMO` | unset | `sctower`\|`vetpoc`\|`dcvigil`\|`frontierllm`\|`_all` |
| | | `_all` creates 4 users per tenant (risk owner, GRC, engineer, auditor) |
| `DJ_DEMO_SIGN` | unset | `1` ⇒ close the demo's tier-k reviews with a stand-in |
| `DJ_SEED_DIR` / `DJ_SEED_STORE` | `seed/` / `store_seed.json` | which corpus to enact |

## Where a model actually sits

Two positions, and it is worth being exact, because the architecture's claim
is that there are so few:

| Stage of `resolve()` | Who decides | Model? |
|---|---|---|
| retrieve | Jaccard, θ = 0.25 | no — deterministic in every mode |
| **distinguish** | does the holding rest on something absent here? | **yes**, once per candidate |
| order | authority → recency → scope | no — declared elimination |
| outcome | mirrored from the controlling record, else `rule_eval` | no |
| **premise** | which facts was the holding material to? | **opt-in** (`DJ_PREMISE_MODE=judged`) |

The decision itself is never asked of a model. `similar()` is not a model
position despite older comments implying it.

**Tiers are judges, not labels.** Each tier builds its own judge and the
verdict cache is keyed by tier, so a challenge genuinely re-asks the question
instead of replaying the rung below. Set `DJ_JUDGE_MODEL_T1=claude-haiku-4-5`,
`_T2=claude-sonnet-4-6`, `_T3=claude-opus-4-5` to run the paper's escalation
ladder inside the container rather than in a harness beside it.

**The premise is a decision, not bookkeeping.** With nothing controlling, the
mechanical rule records every case fact as material — a holding so broad any
later case can distinguish it away. `judged` asks the model which facts
mattered; the Gate then refuses any premise containing a fact the case did not
have (Def. 8), so a model may narrow a holding and never invent one.

**Judicial referral.** When a tier resolves an unbroken conflict
(`none_tie`), or a provision has been risk-accepted `DJ_REFERRAL_ACCEPTANCE_N`
times, it files a `DraftAmendment` with origin `judicial_referral` citing the
record that exposed the problem. A3 is untouched: proposing is not enacting,
`decide_amendment` still requires the lawmakers branch, and the tier that
referred cannot dispose of its own referral. Referrals fire only on *recorded*
resolutions, so the unchallenged tier-1 mass cannot flood the legislature.

## Honest boundaries (unchanged from the paper and SDD)

Challenge coverage remains social (Corollary 2): a wrong, unchallenged
tier-1 decision is neither recorded nor corrected. Oracle mode proves
mechanism, not judgment quality — measuring real models at the judge
positions is the benchmark companion's task, and this package's provenance
tables (`judgment_invocation`) are its substrate. Single-process SQLite is
an MVP posture: the v3.0 PostgreSQL/Temporal substrate is the scale-out
path, and every interface here (`rule_eval`, `Judge`, the Gate API) was
shaped so that migration changes the substrate, not the contract.

---

## Enterprise (single-container)

Pre-merge is the primary control. Post-merge scanning is secondary.

### GitHub connector (pre-merge)

1. Create a GitHub App (or use a PAT for pilots).
2. Webhook URL: `https://<host>/v1/inbound/github`
3. Secret → `DJ_GITHUB_WEBHOOK_SECRET`
4. Required status check name → `DJ_CHECK_NAME` (default `digital-judiciary`)
5. Protect the default branch: require that check to be green before merge

Token for outbound check runs / comments (first match wins):

| Env | Use |
|---|---|
| `DJ_GITHUB_TOKEN` | PAT / fine-grained token |
| `DJ_GITHUB_INSTALLATION_TOKEN` | Pre-minted installation token |
| `DJ_GITHUB_APP_ID` + `DJ_GITHUB_APP_INSTALLATION_ID` + `DJ_GITHUB_APP_KEY_PATH` | App JWT via openssl inside the container |

### Async inbound

```bash
DJ_ASYNC_INBOUND=1   # webhook returns 202; worker adjudicates from job_queue
```

### Tenant mapping (never from the webhook body)

```bash
DJ_REPO_ORG_MAP='{"acme/api":"acme","acme/*":"acme"}'
DJ_DEFAULT_ORG=acme
```

### Break-glass (audited; no precedent)

```http
POST /v1/admin/break-glass
Authorization: Bearer <risk_owner_or_lawmaker>
{"reason":"SEV-1 rollback","session_id":"PRS-...","expiry_hours":24}
```

### Post-merge compliance scan

```http
POST /v1/admin/post-merge-scan
{"repo":"acme/api","sha":"abc123","factors":["..."],"provisions":["SC-201"]}
```

### Rate limit

`DJ_INBOUND_RATE_PER_S` (default 20), `DJ_INBOUND_BURST` (default 40).

### Docker Compose

```bash
docker compose up --build
```

Still one container, one volume, zero pip packages.

---

## Architecture (Kernel vs platform)

See **[ARCHITECTURE.md](ARCHITECTURE.md)** for the enterprise / open-source
target shape: Kernel (formal core) vs platform (connectors, tenancy, workers).

```bash
# Demo path (SQLite, zero deps) — always supported
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=off python3 serve.py

# Self-host profile (async inbound + workers, still one container)
DJ_PROFILE=selfhost DJ_ASYNC_INBOUND=1 DJ_WORKER_THREADS=2 \
  DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 python3 serve.py
```

## Enterprise V1 (pilot)

See **[ENTERPRISE_V1.md](ENTERPRISE_V1.md)** for scope, non-goals, and boot rules.

## Running the conformance suites against Postgres

The suites default to SQLite so a local run is deterministic, but the default
is a `setdefault` — an explicit backend wins:

```bash
DJ_LEDGER_BACKEND=postgres DJ_DATABASE_URL=postgres://... python3 run_conformance.py
DJ_LEDGER_BACKEND=postgres DJ_DATABASE_URL=postgres://... python3 run_interface_conformance.py
DJ_LEDGER_BACKEND=postgres DJ_DATABASE_URL=postgres://... python3 run_extension_conformance.py
```

**Run both backends in CI.** A guarantee that holds on SQLite and not on
Postgres is not a guarantee — it is a deployment-dependent accident. EX-47
compares the two schemas statically on every run and needs no server, but it
only proves the triggers are *declared*; running the suites against a live
Postgres is what proves they *fire*.

## Speeding up a live run

Distinguishing questions within one case are independent, so they are asked
concurrently:

| Variable | Default | Meaning |
|---|---|---|
| `DJ_JUDGE_CONCURRENCY` | `6` | candidates asked at once; `1` disables |

Mean batch is ~2.5 candidates, so the ceiling is ~2.5x, and a live run gets
essentially all of it because API latency dominates everything else. The
oracle ignores this setting — threads gain nothing against a local rule.

**What is not parallel, deliberately.** Cases are adjudicated in order: case
*n* can be bound by a precedent case *n-1* wrote, so running them together
would change what the ledger says rather than only how fast it says it. The
cache lookups and ledger writes also stay on the calling thread, in candidate
order, which is why a concurrent run produces byte-identical decisions to a
sequential one.

## Your desk

Every role has one, and each shows different work — the desk answers "what
needs me?", which has a different answer per branch:

| Role | Their desk |
|---|---|
| **Risk owner** | Decisions awaiting their signature · risks they accepted that are still live · what expires within 30 days |
| **GRC council** | Proposals awaiting their decision · rules under strain (repeatedly waived) · what the council recently settled |
| **Engineer / auditor** | Their blocked changes with routes still open · what is waiting on a named person · what hit a floor and cannot be appealed |

Nothing on a desk grants authority: every item is one the Kernel would let
that principal act on, so a desk can never offer work somebody cannot do. The
risk owner's queue is still at `/review/queue` for anyone who wants only that.
