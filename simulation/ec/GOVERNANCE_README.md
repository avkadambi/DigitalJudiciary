# LLM governance seats — how to run

Every governance decision of the Enterprise Conscience (the conscience, the
offices, the auditor, the judges' ladder, the doctrine clerk and lawmaker, and
L4) can be made by a model, with a human final authority above the court. The
design is `DESIGN.md` §9. With no new flag nothing changes: every seat is the
deterministic code and every registered output is byte-identical
(`python3 simulation/ec/tools/check_r2_digests.py` → `RESULT: 20/20`).

## Dry first (no keys, no network)

```
python3 simulation/ec/run_year.py --packs vetpoc --arms C,D --seeds 97 --days 30 --mode dry --project \
  --agent llm:anthropic:claude-sonnet-5-5 --governance llm --l4 llm-proxy --dry-error-rate 0.1 \
  --roles-config simulation/ec/config/llm_roles.example.json --out /tmp/gov_dry --quiet
```

Dry mode builds every prompt, counts tokens (chars/4) and answers with the
answer key, flipped at `--dry-error-rate`. `--project` prints the dollar
projection per seat and level for one company-year (arms C and D as a
shadow-and-binding pair) and for the registered set (five companies), with L3
reasoning at its upper bound (`max_tokens`), two agent lines (with and without
the v1 cache), L4 items per company-month by origin, and the routing shares
with the EC-21 warnings. Every figure is an estimate.

`bash reproduce/run_year.sh e2e <roles-config> [l4-mode]` runs the whole chain
dry on all five packs (a seed-97 pair, metrics with the governance columns,
the projection).

## Flags

| Flag | Values (default first) |
|---|---|
| `--governance` | `deterministic`, `llm`, `shadow` — preset for every seat |
| `--ec`, `--office`, `--auditor`, `--dj`, `--doctrine` | override one seat |
| `--l4` | `llm-proxy` (registered), `rule`, `queue`, `interactive` |
| `--l4-human-cap`, `--l4-shadow-proxy`, `--human-wait`, `--human-deadline-days`, `--human-sample` | L4 pilots |
| `--prompt-style` | `canon` (registered), `procedural` |
| `--l2-confidence`, `--l2-audit-rate` | routing triggers ii and iv (70, 0.10) |
| `--dj-judge` | `full` (the ladder), `distinguish` |
| `--arm-b-dj` | `deterministic`, `llm` |
| `--pair` | run shadow then binding into sibling directories |
| `--roles-config`, `--keys-file` | the roles file; a key file outside the repo, mode 600 |
| `--dry-error-rate`, `--project`, `--samples` | dry stand-ins, the projection |

A governed run writes to `<out>/<pack>/<arm>/seed-<n>+gov-<mode>[…]`.

## The roles config

Copy `simulation/ec/config/llm_roles.example.json` and edit it. Each role names
a provider, a model, temperature, `max_tokens` and optional reasoning; `dj_l2`
is a panel of three seats with stances, plus a fallback. Each provider names
the environment variable that holds its key (`api_key_env`). A literal
`api_key` anywhere in the file is refused; so is a price without a source.
Confirm every model id against its provider before a live run.

## Keys

Keys come from environment variables only, never as a command-line value, and
are never written to any file, log, cache, manifest or commit, or printed.
Keep them in a file outside the repository, readable only by you:

```
umask 077; cat > ~/dj_keys.env <<'KEYS'
ANTHROPIC_API_KEY=...
DEEPINFRA_API_KEY=...
NOVITA_API_KEY=...
KEYS
```

and pass `--keys-file ~/dj_keys.env`. Check that a key is present with
`test -n "$ANTHROPIC_API_KEY" && echo set` and nothing else. A live start-up
names any missing variable and exits; error logs never carry request headers.

## Human review (L4 queue mode, pilots)

```
python3 simulation/ec/run_year.py ... --l4 queue --l4-human-cap 40 --human-wait ...   # exits 4 at the first item
python3 simulation/ec/tools/human_review.py list   <run-dir>
python3 simulation/ec/tools/human_review.py show   <run-dir> <item>
python3 simulation/ec/tools/human_review.py decide <run-dir> <item> permit|permit_conditional|deny [--overturn-absolute] [--note TEXT]
python3 simulation/ec/run_year.py ... --resume                                        # continues from the start of that day
```

A permit that affirms an absolute violation is refused: overturn the finding
explicitly or deny. Beyond the cap the proxy decides, labelled; the proxy also
decides every human item in shadow, for the agreement measure. Without
`--human-wait` an undecided item lapses to deny and is counted.

## Pilots

Seed 97 only; seed 11 is registered. No live pilot starts before the owner has
seen and approved the dry projection. The pilot design (both prompt styles, a
pair, L4 in queue mode with at least 30 owner decisions, `--budget-usd`) is in
the build playbook §11.4. Delete pilot output after reporting; it is
trusted-tier data and is never committed (`run.jsonl`, `registry.json`,
`store_final.json`, `glosses_final.json`, `bench_log.json`, `llm_errors.jsonl`,
`llm_cache/`, `checkpoint.json`, `human_queue.jsonl`, `human_decisions.jsonl`).

## Projection (dry, vetpoc, seed 97, 30 days, `--dry-error-rate 0.1`, example roles)

| Role / level | Model | USD per company-year, pair |
|---|---|---|
| conscience `ec` | Qwen3 235B | 9.4 |
| office, auditor, clerk | Qwen3 235B | 0.5 |
| L1 + prosecutor | Llama 3.3 70B | 2.2 |
| L2 panel | Sonnet 5.5, Qwen3 235B, Kimi K2 | 31.1 |
| L3 | Opus 5 (reasoning, upper bound) | 381.7 |
| L4 proxy | Opus 5 | 2.5 |
| lawmaker | Sonnet 5.5 | 2.3 |
| agent | Sonnet 5.5 | 28.2 (56.4 without the v1 cache) |
| **per company-year** | | **about 458** (486 without the cache) |
| **registered set, five companies** | | **about 2,289** (2,430) |

Routing in that dry run: 48.6% of hearings reach L2, 18.5% L3, 2.9% L4 (both
EC-21 warnings fire); panel Fleiss κ 0.71. L3 dominates the cost: its
reasoning is priced at the `max_tokens` upper bound, and at a 10% error rate
the conscience's false escalations (which the bench then permits) feed trigger
i. These are estimates from a dry run, not measurements; rerun `--project`
after any change to the roles file.
