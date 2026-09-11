#!/usr/bin/env bash
# Rebuild simulation/zips/ from the extracted packs, and print each archive's
# SHA-256 so a recipient can check what they were sent.
#
#   bash reproduce/make_pack_zips.sh
#
# The archives are redundant with the extracted trees on purpose: the trees are
# what run_all_simulation.sh runs against, the archives are what you forward.
# Excluded from every archive: __pycache__, *.pyc, benchmark/results/*.json, and
# the two API-key files, which are gitignored and must never be packaged.
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="simulation/zips"
mkdir -p "$OUT"
PACKS="vetpoc-constitution-corpus semifab-constitution-corpus frontierllm-constitution-corpus dcvigil-constitution-corpus meridian-corpus numerals"
for p in $PACKS; do
  v=$(cat "simulation/$p/VERSION" | tr -d '[:space:]')
  z="$OUT/$p-$v.zip"
  rm -f "$z"
  ( cd simulation && zip -rq "../$z" "$p" \
      -x "$p/*__pycache__/*" "*.pyc" "$p/benchmark/results/*.json" "$p/corpus/cases.jsonl" "$p/corpus/explorer_data.json" "*.mutation-backup" \
         "$p/benchmark/.env" "$p/benchmark/api_key.txt" )
  printf '%-42s %10s bytes  %s\n' "$(basename "$z")" \
    "$(stat -c%s "$z" 2>/dev/null || stat -f%z "$z")" \
    "$(sha256sum "$z" 2>/dev/null | cut -c1-16 || shasum -a 256 "$z" | cut -c1-16)"
done
