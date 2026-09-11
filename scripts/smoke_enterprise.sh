#!/usr/bin/env bash
# EV1 smoke: boot → health → constitution → unsigned rejected → status → break-glass
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

DB="${DJ_DB:-/tmp/dj-smoke-$$.db}"
PORT="${DJ_SMOKE_PORT:-18765}"
export DJ_DB="$DB" DJ_DEV_KEYS=1 DJ_DEMO=off DJ_JUDGE_MODE=oracle
export DJ_PROFILE=demo DJ_GITHUB_ALLOW_UNSIGNED=0 DJ_PORT="$PORT"
export DJ_LEDGER_BACKEND=sqlite DJ_LEDGER_ON_PG=0
export DJ_OUTBOUND_RETRY=0
unset DJ_DATABASE_URL || true
rm -f "$DB" /tmp/dj-smoke-serve.log

python3 serve.py > /tmp/dj-smoke-serve.log 2>&1 &
PID=$!
cleanup() { kill "$PID" 2>/dev/null || true; wait "$PID" 2>/dev/null || true; rm -f "$DB"; }
trap cleanup EXIT

for i in $(seq 1 80); do
  if curl -sf "http://127.0.0.1:${PORT}/v1/healthz" >/dev/null 2>&1; then
    break
  fi
  sleep 0.1
done
curl -sf "http://127.0.0.1:${PORT}/v1/healthz" >/dev/null

KEY=$(grep 'alice.grc' /tmp/dj-smoke-serve.log | awk '{print $NF}' | head -1 || true)
KEY=${KEY:-devkey-alice}
EKEY=$(grep 'eng.sam' /tmp/dj-smoke-serve.log | awk '{print $NF}' | head -1 || true)
EKEY=${EKEY:-devkey-sam}

CODE=$(curl -s -o /tmp/dj-smoke-const.json -w '%{http_code}' \
  -X POST "http://127.0.0.1:${PORT}/v1/admin/constitution" \
  -H "authorization: Bearer ${KEY}" \
  -H "content-type: application/json" \
  -d '{"provisions":[{"provision_id":"SMK-1","text":"smoke rule","absolute":false,"policy":{"deny_if_any":["smoke_factor"]}}]}')
if [[ "$CODE" != "200" ]]; then
  echo "FAIL constitution HTTP $CODE $(cat /tmp/dj-smoke-const.json)" >&2
  exit 1
fi

CODE=$(curl -s -o /tmp/dj-smoke-in.json -w '%{http_code}' \
  -X POST "http://127.0.0.1:${PORT}/v1/inbound/github" \
  -H "content-type: application/json" \
  -H "x-github-event: pull_request" \
  -H "x-github-delivery: smoke-1" \
  -d '{"action":"opened","repository":{"full_name":"acme/api"},"pull_request":{"number":1,"title":"t","body":"","labels":[],"base":{"ref":"main"},"head":{"sha":"abc"},"user":{"login":"x"}}}')
if [[ "$CODE" != "400" && "$CODE" != "401" && "$CODE" != "403" && "$CODE" != "503" ]]; then
  echo "FAIL inbound expected 4xx got $CODE $(cat /tmp/dj-smoke-in.json)" >&2
  exit 1
fi

curl -sf "http://127.0.0.1:${PORT}/v1/admin/status" | grep -q '"ok"'

CODE=$(curl -s -o /tmp/dj-smoke-bg.json -w '%{http_code}' \
  -X POST "http://127.0.0.1:${PORT}/v1/admin/break-glass" \
  -H "authorization: Bearer ${EKEY}" \
  -H "content-type: application/json" \
  -d '{"reason":"should fail"}')
if [[ "$CODE" != "403" ]]; then
  echo "FAIL break-glass expected 403 got $CODE $(cat /tmp/dj-smoke-bg.json)" >&2
  exit 1
fi

echo "SMOKE OK (port=$PORT)"
