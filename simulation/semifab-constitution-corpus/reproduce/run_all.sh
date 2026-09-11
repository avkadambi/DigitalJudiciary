#!/usr/bin/env bash
# Rebuild the SemiFab Constitution Corpus from source and verify it.
#
#   bash reproduce/run_all.sh
#
# Deterministic: two consecutive runs produce byte-identical corpus files.
# No network, no API key, no third-party package.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "== 1/6  constitution =="
python3 generator/build_constitution.py

echo
echo "== 2/6  corpus (6,000 cases, one chronological pass) =="
python3 generator/build_corpus.py | tail -20

echo
echo "== 3/6  determinism: rebuild and compare digests =="
BEFORE=$(python3 -c "import json;print(json.load(open('corpus/manifest.json'))['sha256']['cases.json'])")
python3 generator/build_corpus.py > /dev/null
AFTER=$(python3 -c "import json;print(json.load(open('corpus/manifest.json'))['sha256']['cases.json'])")
if [ "$BEFORE" = "$AFTER" ]; then
  echo "OK  cases.json sha256 stable across runs: ${BEFORE:0:16}..."
else
  echo "FAIL  corpus is not deterministic"; exit 1
fi

echo
echo "== 4/6  conformance =="
python3 harness/run_conformance.py | tail -4

echo
echo "== 5/6  mutation matrix =="
python3 harness/mutation_matrix.py | tail -22

echo
echo "== 6/6  documentation and explorer =="
python3 generator/build_docs.py
python3 generator/build_explorer.py
python3 generator/build_simulation.py

echo
echo "== extra  cross-pack comparison (skipped if the VetPOC pack is absent) =="
python3 harness/compare_packs.py || true

echo
echo "done."
