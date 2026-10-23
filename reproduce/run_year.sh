#!/usr/bin/env bash
# The Enterprise Conscience fast track (simulation/ec, DESIGN §5-§7): a year of
# five companies under four arms. No network, no API key, no pip install.
#
#   bash reproduce/run_year.sh pilot        # 30 days, all packs, all arms, seed 11, pressure_sensitive (about a minute)
#   bash reproduce/run_year.sh registered   # the calibration design on the R2 instrument: seeds 11,13,17,19,23 x 251 working
#                                           # days x 4 arms x 5 packs for 4 archetypes plus laundering (exploratory), the two
#                                           # registered sensitivities (bench cap 2/day; CISO on the engineering line), the oracle/adversarial bounds (seed 11)
#                                           # and the arm-D LLM dry run, into results/calibration_r2/ (minutes). The first
#                                           # calibration (365-day v1 instrument, 2026-10-20) stays as committed under
#                                           # results/registered/ and results/bounds/; both are disclosed in the registration
#   bash reproduce/run_year.sh confirmatory # the confirmatory design: seeds 59,61,67,71,73 x 251 days x 4 arms x 5 packs
#                                           # for 4 archetypes (plus laundering and the two sensitivities, exploratory), then the oracle/adversarial bounds (same five seeds; 600 runs), then metrics (hours)
#   bash reproduce/run_year.sh conformance  # EC-01..EC-12 on a fresh 60-day vetpoc pilot (about half a minute)
#   bash reproduce/run_year.sh mutation     # F-EC-1..8 + 2 controls (about four minutes)
#   bash reproduce/run_year.sh metrics      # recompute metrics.csv and analysis.md under every results root
#   bash reproduce/run_year.sh console      # the EC console: ec_simulation.html + ec_explorer.html per run, index.html per root
#   bash reproduce/run_year.sh live <model> [provider]
#                                           # the registered LLM live slice (needs ANTHROPIC_API_KEY or OPENAI_API_KEY):
#                                           # preflight (seed 97), then arms A,B,C,D x seed 11 x 251 days x all packs with
#                                           # --checkpoint-every 10 --resume --budget-usd 1000, then metrics, analysis,
#                                           # report and console. Re-run the same command to resume after a stop.
#
# Canons are generated from the rulebooks on first use (build_all_canons.py).
set -euo pipefail
cd "$(dirname "$0")/.."

EC=simulation/ec
RES=$EC/results
MODE="${1:-pilot}"
say(){ printf '\n\033[1m== %s\033[0m\n' "$*"; }

canons(){
  for p in vetpoc-constitution-corpus semifab-constitution-corpus frontierllm-constitution-corpus \
           dcvigil-constitution-corpus meridian-corpus; do
    [ -f "simulation/$p/constitution/canon.json" ] || { say "Canons"; python3 $EC/build_all_canons.py; break; }
  done
}

# metrics_and_analysis <root>: metrics.csv/json and analysis.md/json beside the runs.
metrics_and_analysis(){
  local root="$1"
  python3 $EC/metrics.py "$root" | tail -1
  python3 $EC/analyze.py "$root" >/dev/null && printf '%s/analysis.md\n' "$root"
}

run(){   # run <out> <agent> <seeds> <days> <arms> <packs> [extra args]; one summary line per call
  local out="$1" agent="$2" seeds="$3" days="$4" arms="$5" packs="$6"; shift 6
  python3 $EC/run_year.py --packs "$packs" --arms "$arms" --seeds "$seeds" --days "$days" \
          --agent "$agent" --out "$out" --quiet "$@"
  python3 - "$out" <<'PY'
import json, sys
t = json.load(open(sys.argv[1] + "/timings.json"))
n = sum(r["proposals"] for r in t["runs"])
print(f"{len(t['runs'])} runs, {n} proposals, {t['elapsed_s']:.0f}s -> {sys.argv[1]}")
PY
}

case "$MODE" in
  pilot)
    canons
    say "Pilot — 30 days, all packs, arms A,B,C,D, seed 11, policy:pressure_sensitive"
    run $RES/pilot30 policy:pressure_sensitive 11 30 A,B,C,D all
    say "Metrics and analysis"
    metrics_and_analysis $RES/pilot30
    ;;

  registered)
    canons
    for arch in honest pressure_sensitive observation_sensitive misreporting laundering; do
      say "Calibration (R2) — policy:$arch, seeds 11,13,17,19,23, 251 days, arms A,B,C,D, all packs"
      run $RES/calibration_r2/$arch policy:$arch 11,13,17,19,23 251 A,B,C,D all --checkpoint-every 30 --resume
    done
    for arch in oracle adversarial; do
      say "Calibration bounds (R2) — policy:$arch, seed 11, 251 days, arms A,B,C,D, all packs"
      run $RES/calibration_r2/bounds/$arch policy:$arch 11 251 A,B,C,D all --checkpoint-every 30 --resume
    done
    say "Calibration sensitivities (R2) — policy:pressure_sensitive, seeds 11,13,17,19,23: bench cap 2/day; CISO on the engineering line"
    run $RES/calibration_r2/sensitivity/bench_cap2 policy:pressure_sensitive 11,13,17,19,23 251 A,B,C,D all --bench-cap 2 --checkpoint-every 30 --resume
    run $RES/calibration_r2/sensitivity/ciso_engineering policy:pressure_sensitive 11,13,17,19,23 251 A,B,C,D all --ciso-line engineering --checkpoint-every 30 --resume
    say "LLM dry run (R2) — llm:anthropic:sonnet, arm D, seed 11, 251 days, all packs (priced, not called)"
    run $RES/calibration_r2/llm_dry llm:anthropic:sonnet 11 251 D all --mode dry --checkpoint-every 30 --resume
    say "Metrics and analysis"
    for root in $RES/calibration_r2/honest $RES/calibration_r2/pressure_sensitive $RES/calibration_r2/observation_sensitive \
                $RES/calibration_r2/misreporting $RES/calibration_r2/laundering \
                $RES/calibration_r2/sensitivity/bench_cap2 $RES/calibration_r2/sensitivity/ciso_engineering $RES/calibration_r2/bounds/oracle $RES/calibration_r2/bounds/adversarial \
                $RES/calibration_r2/llm_dry; do
      metrics_and_analysis "$root"
    done
    ;;

  confirmatory)
    canons
    for arch in honest pressure_sensitive observation_sensitive misreporting laundering; do
      say "Confirmatory — policy:$arch, seeds 59,61,67,71,73, 251 days, arms A,B,C,D, all packs"
      run $RES/confirmatory/$arch policy:$arch 59,61,67,71,73 251 A,B,C,D all --checkpoint-every 30 --resume
    done
    for arch in oracle adversarial; do
      say "Confirmatory bounds — policy:$arch, seeds 59,61,67,71,73, 251 days, arms A,B,C,D, all packs"
      run $RES/confirmatory/bounds/$arch policy:$arch 59,61,67,71,73 251 A,B,C,D all --checkpoint-every 30 --resume
    done
    say "Sensitivities (exploratory) — policy:pressure_sensitive, seeds 59,61,67,71,73: bench cap 2/day; CISO on the engineering line"
    run $RES/confirmatory/sensitivity/bench_cap2 policy:pressure_sensitive 59,61,67,71,73 251 A,B,C,D all --bench-cap 2 --checkpoint-every 30 --resume
    run $RES/confirmatory/sensitivity/ciso_engineering policy:pressure_sensitive 59,61,67,71,73 251 A,B,C,D all --ciso-line engineering --checkpoint-every 30 --resume
    say "Metrics and analysis"
    for root in $RES/confirmatory/honest $RES/confirmatory/pressure_sensitive $RES/confirmatory/observation_sensitive \
                $RES/confirmatory/misreporting $RES/confirmatory/laundering \
                $RES/confirmatory/sensitivity/bench_cap2 $RES/confirmatory/sensitivity/ciso_engineering $RES/confirmatory/bounds/oracle $RES/confirmatory/bounds/adversarial; do
      metrics_and_analysis "$root"
    done
    ;;

  conformance)
    canons
    say "EC conformance — EC-01..EC-23 on a fresh 60-day vetpoc pilot (EC-13..23 on its dry governed pair)"
    python3 $EC/run_ec_conformance.py --pack vetpoc --days 60 --seed 11 --archetype laundering \
            --out $RES/conformance
    ;;

  mutation)
    canons
    say "EC mutation matrix — F-EC-1..19 and two controls"
    python3 $EC/mutation_matrix_ec.py --pack vetpoc --days 45 --seed 11 --archetype laundering
    ;;

  metrics)
    say "Metrics and analysis under every results root"
    found=0
    for root in $RES/pilot30 $RES/calibration_r2/* $RES/calibration_r2/bounds/* $RES/calibration_r2/sensitivity/* $RES/registered/* $RES/bounds/* $RES/llm_dry; do
      [ -d "$root" ] || continue
      ls "$root"/*/*/seed-*/run.jsonl >/dev/null 2>&1 || continue
      found=1
      printf '%s\n' "$root"
      metrics_and_analysis "$root"
    done
    [ "$found" = 1 ] || { echo "no runs under $RES; run pilot or registered first"; exit 1; }
    ;;

  console)
    say "EC console — pages under every results root that holds runs"
    found=0
    for root in $RES/pilot30 $RES/calibration_r2 $RES/registered $RES/bounds $RES/llm_dry; do
      [ -d "$root" ] || continue
      ls "$root"/*/*/seed-*/run.jsonl "$root"/*/*/*/seed-*/run.jsonl >/dev/null 2>&1 || continue
      found=1
      python3 reproduce/ec_console.py --all "$root" --quiet
    done
    [ "$found" = 1 ] || { echo "no runs under $RES; run pilot or registered first"; exit 1; }
    ;;

  live)
    canons
    MODEL="${2:-}"; PROVIDER="${3:-anthropic}"
    [ -n "$MODEL" ] || { echo "usage: bash reproduce/run_year.sh live <model id> [anthropic|openai]"; exit 2; }
    say "Preflight — $PROVIDER $MODEL (model list, prices, plan, 3-day smoke on seed 97, schema, metrics)"
    python3 reproduce/ec_preflight.py --provider "$PROVIDER" --model "$MODEL" --days 3
    say "LLM live slice — llm:$PROVIDER:$MODEL, seed 11, 251 days, arms A,B,C,D, all packs, budget 1000 USD"
    run $RES/registered/llm "llm:$PROVIDER:$MODEL" 11 251 A,B,C,D all --mode live \
        --checkpoint-every 10 --resume --budget-usd 1000
    say "Metrics and analysis"
    metrics_and_analysis $RES/registered/llm
    say "Report"
    python3 reproduce/ec_report.py
    say "Console"
    python3 reproduce/ec_console.py --all $RES/registered/llm --quiet
    ;;

  *)
    echo "usage: bash reproduce/run_year.sh [pilot|registered|confirmatory|conformance|mutation|metrics|console|live <model> [provider]]"; exit 2 ;;
esac
