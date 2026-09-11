# Digital Judiciary 5.0 — User Guide

This guide is for **operators** (who run the service) and **risk owners /
lawmakers** (who use the review screens). Engineers integrating GitHub only
need the inbound and check-run sections.

---

## 1. What this system does

Digital Judiciary adjudicates **code changes** against a written **constitution**
(rulebook of provisions). Automated tiers can permit, deny, or escalate.
Absolute floors cannot be waived by engineers. Contested denials climb a
ladder; exhausted automated tiers open a **human review** task for a named
**risk owner**.

Every binding decision is written through the **Challenge Gate** into an
append-only ledger. That record is the system of truth—not the GitHub UI.

---

## 2. Quick start (demo)

```bash
unzip Digital_Judiciary_5.0.zip
cd Digital_Judiciary_5.0   # or the extracted folder name
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=off python3 serve.py
```

Open:

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8080/review | Human review queue (sign in with a dev key) |
| http://127.0.0.1:8080/v1/healthz | Liveness |
| http://127.0.0.1:8080/v1/admin/status | Operator snapshot |

On first boot the process prints **API keys** for founding principals
(`alice.grc` lawmaker, `coo.pat` risk owner, `eng.sam` engineer). Store them.

Smoke test:

```bash
./scripts/smoke_enterprise.sh
```

---

## 3. Configuration

### File: `config/dj.toml`

Copy from `config/dj.example.toml`. Important sections:

```toml
[project]
profile = "demo"          # demo | selfhost | enterprise | gcp

[constitution]
path = "seed/rulebook.json"

[judges]
mode = "oracle"           # oracle (deterministic) | llm

[judges.tier1]
provider = "anthropic"
model = "claude-haiku-4-5-20251001"
api_key_env = "DJ_JUDGE_KEY_T1"

[judges.tier2]
# ...
[judges.tier3]
# ...
```

Or set `DJ_CONFIG=/path/to/dj.toml`.

### Environment variables (common)

| Variable | Meaning |
|----------|---------|
| `DJ_DB` | SQLite path (default `/data/judiciary.db`) |
| `DJ_JUDGE_MODE` | `oracle` or `llm` |
| `DJ_DEV_KEYS` | Fixed demo API keys (local only) |
| `DJ_GITHUB_WEBHOOK_SECRET` | HMAC secret for `/v1/inbound/github` |
| `DJ_CHECK_NAME` | GitHub check run name (default `digital-judiciary`) |
| `DJ_ASYNC_INBOUND` | `1` = webhook returns 202, worker adjudicates |
| `DJ_DATABASE_URL` | Postgres URL for **job queue** (optional) |
| `DJ_LEDGER_BACKEND` | `postgres` to put Kernel ledger on Postgres (opt-in) |
| `DJ_PROFILE` | `demo` / `selfhost` / `enterprise` / `gcp` |

**Enterprise/gcp profiles:** do not put API keys inline in the toml; inject via env / Secret Manager. Missing LLM keys cause a **boot failure**.

---

## 4. Constitution (rulebook)

A rulebook is JSON:

```json
{
  "provisions": [
    {
      "provision_id": "SC-202",
      "absolute": true,
      "text": "Sanctions screening is never bypassed.",
      "policy": { "deny_if_any": ["screening_bypass"] }
    }
  ]
}
```

- **Boot:** `[constitution] path = "..."` or `DJ_CONSTITUTION_PATH`
- **Live upload** (lawmaker Bearer token):

```bash
curl -X POST http://127.0.0.1:8080/v1/admin/constitution \
  -H "Authorization: Bearer $LAWMAKER_KEY" \
  -H "Content-Type: application/json" \
  -d @my-rulebook.json
```

Uploading enacts a **new version**; it does not erase history. In-flight cases
keep the version they were filed under.

---

## 5. GitHub integration (pre-merge)

1. Point a GitHub App or webhook at `https://<host>/v1/inbound/github`
2. Set `DJ_GITHUB_WEBHOOK_SECRET`
3. Protect the default branch: require check **`digital-judiciary`** (or your `DJ_CHECK_NAME`)
4. Optional outbound token: `DJ_GITHUB_TOKEN` or GitHub App credentials

**Flow:** PR opened/synced → factors extracted → floor-first adjudication →
check run + optional PR comment → challenge / human-review actions when offered.

Unsigned webhooks are rejected unless you explicitly allow local unsigned mode.

Generic (non-GitHub) webhooks: `POST /v1/inbound/generic` with optional
`X-DJ-Webhook-Secret`.

---

## 6. Review UI (risk owners & lawmakers)

Sign in at `/review` with your API key (pilot). The queue lists tasks that
reached a human after the automated ladder.

**Status strip** (top of queue) shows:

- how many decisions are open  
- judge mode (`oracle` / `llm`)  
- ledger backend (`sqlite` / `postgres`)  
- job queue backend  
- deploy profile  

**On a task page you will see:**

- the provision and opinion  
- facts of the case  
- the tier ladder (A4 — every rung that was contested)  
- the instrument you sign (accept with **mandatory expiry**, or uphold denial)

Rules of the product (reflected in the UI):

- Absolute denials cannot be accepted here  
- If renewal is barred (Prop. 2), the accept control is **absent**, not greyed out  
- Acceptances are dispensations with expiry—not new law  

Other desks: **Ledger**, **Changes**, **Rulebook**, **Legislature** (amendments).

---

## 7. Operator endpoints

| Method | Path | Notes |
|--------|------|-------|
| GET | `/v1/healthz` | Liveness |
| GET | `/v1/admin/status` | Metrics, cache, enterprise block |
| POST | `/v1/admin/lifecycle-sweep` | Lapse expired acceptances |
| POST | `/v1/admin/outbound-retry` | Retry failed GitHub deliveries |
| POST | `/v1/admin/break-glass` | Risk owner/lawmaker emergency override (no precedent) |
| POST | `/v1/admin/constitution` | Enact rulebook |
| POST | `/v1/admin/post-merge-scan` | Secondary compliance scan |

All mutating admin routes (except inbound webhooks) require a Bearer principal.

---

## 8. Docker

```bash
docker compose up --build
# optional Postgres job queue:
docker compose -f docker-compose.yml -f docker-compose.postgres.yml up --build
```

GCP sketch: `deploy/gcp/README.md` and `./deploy/gcp/deploy.sh`.

---

## 9. Safety & security

- Report issues per `SECURITY.md`
- Webhook secrets and judge API keys are secrets — never commit them
- Break-glass is audited and does **not** invent tier-1 law
- The inbound gateway cannot resolve or accept risk (no branch)

---

## 10. Where to read next

| Document | Audience |
|----------|----------|
| `docs/releases/RELEASE_NOTES_5.0.md` | Upgraders |
| `ENTERPRISE_V1.md` | Scope / non-goals |
| `ARCHITECTURE.md` | Kernel vs platform |
| `docs/CONNECTION_POOLING.md` | Postgres operators |
| `config/dj.example.toml` | Full config reference |

---

*Digital Judiciary 5.0 — decisions are permanent records.*
