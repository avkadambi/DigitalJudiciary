#!/usr/bin/env bash
# Chapter 6's benchmark: governed precedent against a monolithic model.
#
#   bash reproduce/run_benchmark.sh                 # offline pilot, no API key
#   bash reproduce/run_benchmark.sh cost            # price the full design
#   bash reproduce/run_benchmark.sh check           # is my API key working?
#   bash reproduce/run_benchmark.sh live sonnet     # real calls; needs a key
#   bash reproduce/run_benchmark.sh discriminating  # the eight-family suite, offline
#   bash reproduce/run_benchmark.sh disclosure      # the author-justification axis
#   bash reproduce/run_benchmark.sh human           # arm C, the priced human desk (estimation-only)
#   bash reproduce/run_benchmark.sh discriminating-live sonnet
set -euo pipefail
cd "$(dirname "$0")/.."
if [ ! -d simulation/meridian-corpus ]; then
  ( cd simulation && unzip -q zips/meridian-corpus-*.zip )   # the packs ship as archives; unpack on first use
fi
cd simulation/meridian-corpus
case "${1:-pilot}" in
  pilot) python3 benchmark/run.py --cases 500 --k 3 --mode oracle --models sonnet ;;
  check) python3 benchmark/run.py --check --models "${2:-sonnet}" ;;
  cost)  python3 benchmark/run.py --cases 6000 --runs 3 --k 8 --mode dry \
                 --models opus,sonnet,haiku ;;
  live)  python3 benchmark/run.py --cases "${3:-500}" --k 3 --mode live \
                 --models "${2:-sonnet}" ;;
  discriminating)
         python3 benchmark/run.py --discriminating --mode oracle \
                 --arms B,A,A+,B_mem,B_gov --models haiku ;;
  human)
         python3 benchmark/run.py --cases 6000 --k 1 --mode oracle --human \
                 --arms B,A,B_mem,B_gov --models haiku ;;
  disclosure)
         python3 benchmark/run.py --cases 400 --k 1 --justify 60 --mode oracle \
                 --oracle-reader naive --arms B,A,A+,B_mem,B_gov --models haiku ;;
  discriminating-live)
         python3 benchmark/run.py --discriminating --mode live \
                 --arms B,A,A+,B_mem,B_gov --models "${2:-sonnet}" --k "${3:-5}" ;;
  *) echo "usage: $0 [pilot|check|cost|live [model] [cases]|discriminating|discriminating-live [model] [k]|disclosure|human]"; exit 2 ;;
esac
