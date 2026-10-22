#!/usr/bin/env bash
# Deploy Digital Judiciary to Google Cloud Run (one-shot helper).
set -euo pipefail

PROJECT_ID="${PROJECT_ID:-$(gcloud config get-value project 2>/dev/null)}"
REGION="${REGION:-us-central1}"
SERVICE="${SERVICE:-digital-judiciary}"
REPO="${REPO:-dj}"

if [[ -z "$PROJECT_ID" || "$PROJECT_ID" == "(unset)" ]]; then
  echo "Set PROJECT_ID or run: gcloud config set project YOUR_PROJECT"
  exit 1
fi

echo "== project=$PROJECT_ID region=$REGION service=$SERVICE =="

gcloud services enable run.googleapis.com cloudbuild.googleapis.com \
  secretmanager.googleapis.com artifactregistry.googleapis.com \
  --project "$PROJECT_ID"

# Artifact Registry repo (idempotent)
gcloud artifacts repositories describe "$REPO" \
  --location="$REGION" --project="$PROJECT_ID" 2>/dev/null \
  || gcloud artifacts repositories create "$REPO" \
       --repository-format=docker --location="$REGION" --project="$PROJECT_ID"

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

gcloud builds submit --project "$PROJECT_ID" \
  --config deploy/gcp/cloudbuild.yaml \
  --substitutions=_REGION="$REGION",_SERVICE="$SERVICE"

URL=$(gcloud run services describe "$SERVICE" --region="$REGION" \
  --project="$PROJECT_ID" --format='value(status.url)')
echo ""
echo "Deployed: $URL"
echo "Health:   $URL/v1/healthz"
echo "Review:   $URL/review"
echo "Webhook:  $URL/v1/inbound/github"
echo ""
echo "Upload a constitution (lawmaker key from bootstrap logs / secrets):"
echo "  curl -sX POST \$URL/v1/admin/constitution \\"
echo "    -H 'authorization: Bearer <lawmaker-key>' \\"
echo "    -H 'content-type: application/json' \\"
echo "    -d @seed/rulebook.json"
