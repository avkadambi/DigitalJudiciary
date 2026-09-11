#!/usr/bin/env bash
# Rebuild and verify the Numerals enterprise constitution and federated stream.
# Requires the five division packs to be unpacked beside this directory
# (bash ../../reproduce/run_all_simulation.sh does that). Standard library only.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "== 1/5  constitution, inheritance map and federated stream (3,000 cases) =="
python3 generator/build_enterprise.py > /tmp/numerals_build.log; head -1 /tmp/numerals_build.log
echo "== 2/5  determinism: rebuild and compare digests =="
A=$(python3 -c "import json;print(json.load(open('corpus/manifest.json'))['sha256']['cases.json'])")
python3 generator/build_enterprise.py >/dev/null
B=$(python3 -c "import json;print(json.load(open('corpus/manifest.json'))['sha256']['cases.json'])")
[ "$A" = "$B" ] && echo "cases.json digest stable: $A" || { echo "DRIFT: $A != $B"; exit 1; }
echo "== 3/5  federation checks =="
python3 harness/run_federation_checks.py | grep -E "^(FC|RESULT)"
echo "== 4/5  mutation matrix =="
python3 harness/mutation_matrix.py | grep -E "^RESULT"
echo "== 5/5  docs and the offline federated benchmark =="
python3 generator/build_docs.py
python3 benchmark/run_federated.py | head -5
echo "done."
