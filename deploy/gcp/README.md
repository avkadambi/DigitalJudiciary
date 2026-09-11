# Deploy on Google Cloud Run

## 1. Config file

Copy and edit:

```bash
cp config/dj.example.toml config/dj.toml
# Set [judges] mode = "llm" and models / api_key_env per tier
```

Mount or bake the file into the image. Cloud Run injects secrets as env vars
named in `api_key_env` (e.g. `DJ_JUDGE_KEY_T1`).

## 2. Secrets

```bash
echo -n "sk-ant-..." | gcloud secrets create dj-judge-key-t1 --data-file=-
echo -n "sk-ant-..." | gcloud secrets create dj-judge-key-t2 --data-file=-
echo -n "sk-ant-..." | gcloud secrets create dj-judge-key-t3 --data-file=-
echo -n "whsec-..."  | gcloud secrets create dj-github-webhook --data-file=-
```

## 3. Deploy

```bash
export PROJECT_ID=my-project
./deploy/gcp/deploy.sh
```

## 4. Constitution

After boot, upload your rulebook (lawmaker bearer token from bootstrap):

```bash
curl -sX POST "$URL/v1/admin/constitution" \
  -H "authorization: Bearer $LAWMAKER_KEY" \
  -H "content-type: application/json" \
  -d @my-company-rulebook.json
```

Format: `{ "provisions": [ { "provision_id", "text", "absolute", "policy" }, ... ] }`

## 5. GitHub webhook

Point the App / webhook at `$URL/v1/inbound/github` with the secret stored above.
Require the check named `digital-judiciary` (or `DJ_CHECK_NAME`) on protected branches.

## Notes

- Default storage remains SQLite on the container filesystem (ephemeral on Cloud Run).
  For durable production, attach a network volume or switch to the Postgres seam
  (`DJ_DATABASE_URL`) documented in ARCHITECTURE.md.
- Demo path locally is unchanged: `python3 serve.py` with no config file.
