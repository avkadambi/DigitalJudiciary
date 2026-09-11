#!/usr/bin/env bash
# Reproduce every number the papers report. No network, no API key, no pip install.
# Runtime: about two minutes total on a laptop.
set -euo pipefail
cd "$(dirname "$0")/.."

export DJ_JUDGE_MODE=oracle          # the deterministic reference oracles
export DJ_DEV_KEYS=1
export DJ_GITHUB_ALLOW_UNSIGNED=1
# NB: DJ_SEED_STORE is set per-replay below, not globally — the conformance
# suites seed from seed/store_seed.json and must not see the pack-level file.
INIT=store_seed_initial.json
OUT="${OUT:-/tmp/dj-reproduce}"
mkdir -p "$OUT"

say(){ printf '\n\033[1m== %s\033[0m\n' "$*"; }

say "1. Conformance — three suites"
python3 run_conformance.py           | grep -E '^(RESULT|PASS|FAIL|[0-9]+/[0-9]+)' | tail -1
python3 run_interface_conformance.py | grep -E '^(RESULT|PASS|FAIL|[0-9]+/[0-9]+)' | tail -1
python3 run_extension_conformance.py | grep -E '^(RESULT|PASS|FAIL|[0-9]+/[0-9]+)' | tail -1

say "2. The four executed enterprises (Table 6 / Sect. 7)"
for co in sctower vetpoc dcvigil frontierllm; do
  DJ_SEED_STORE=$INIT python3 demo/reset.py --db "$OUT/$co.db" --company "$co" --sign --yes >/dev/null
  python3 reproduce/report.py "$OUT/$co.db" "$co"
done

say "3. Threshold sweep — the stability interval"
for th in 0.0 0.10 0.25 0.50 0.75 1.0; do
  DJ_SEED_STORE=$INIT DJ_THETA=$th python3 demo/reset.py --db "$OUT/th_$th.db" --company sctower --sign --yes >/dev/null
  DJ_THETA=$th python3 reproduce/report.py "$OUT/th_$th.db" "theta=$th"
done

say "4. Ordering ablation"
for o in "auth,ts,scope" "auth,ts" "auth" "ts" "auth,scope,ts"; do
  tag=${o//,/-}
  DJ_SEED_STORE=$INIT DJ_ORDER=$o python3 demo/reset.py --db "$OUT/ord_$tag.db" --company sctower --sign --yes >/dev/null
  DJ_ORDER=$o python3 reproduce/report.py "$OUT/ord_$tag.db" "order=$o"
done

say "5. Contest-rate sweep"
for r in 0.05 0.10 0.25 0.50 1.0; do
  DJ_SEED_STORE=$INIT DJ_CONTEST_RATE=$r python3 demo/reset.py --db "$OUT/cr_$r.db" --company sctower --sign --yes >/dev/null
  DJ_CONTEST_RATE=$r python3 reproduce/report.py "$OUT/cr_$r.db" "contest=$r"
done

say "6a. Consolidation and pressure invariance on each executed pack"
for co in sctower vetpoc dcvigil frontierllm; do
  python3 reproduce/cc33_pressure_invariance.py "$OUT/$co.db" \
          "demo/companies/$co/cases.json"
done

say "6. Mutation matrix (13 fault mutants + 5 no-op controls)"
python3 reproduce/mutation_matrix.py

say "6b. Proposition 4, executed — one counter-model per axiom, run both ways"
python3 reproduce/axiom_matrix.py

say "7. Negative control — seed records re-paired to other provisions"
python3 reproduce/shuffle_control.py sctower

say "8. B_gov baseline — Definition 12, same corpus, precedent machinery disabled"
python3 reproduce/bgov_baseline.py sctower

say "Done. Databases and logs are under $OUT"
