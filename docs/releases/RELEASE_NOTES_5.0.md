# Digital Judiciary 5.0 — Major Release

**Release name:** Enterprise Platform  
**Date:** 2026-07-27  
**Baseline:** Release 4.7 research kernel + enterprise platform layer  

This is a **major** release: platform architecture, deploy profiles, and the
risk-owner UX change in ways that operators and integrators should read
before upgrading.

---

## Highlights

### Judiciary core (unchanged guarantees)

- Challenge Gate remains the sole writer of precedent (Def. 7)
- Axioms A1–A7, floor-first (A6), contest ladder (A4), risk acceptance (A7)
- Conformance: **47/47** contract checks; interface suite green
- Demo path: `python3 serve.py` + SQLite, **zero pip installs**

### Platform (new since 4.x research drops)

- Kernel vs platform package split (`app/platform/`)
- Config file `config/dj.toml` — per-tier judge model + API key env names
- Constitution path + `POST /v1/admin/constitution` upload
- Async inbound jobs; Postgres **SKIP LOCKED** job queue (optional)
- Optional **Postgres Kernel ledger** (`DJ_LEDGER_BACKEND=postgres`)
- GitHub App token helper; generic webhook connector plugin
- Break-glass (audited, non-precedential); post-merge scan
- Outbound delivery retry reaper
- EV1 boot validation (LLM keys required; no inline keys on enterprise/gcp)
- GCP Cloud Run sketch under `deploy/gcp/`

### UX (5.0)

- Cleaner review UI theme with **light/dark** system preference
- Sticky masthead, clearer docket instrument cards, improved mobile layout
- **Status strip** on `/review`: open count · judge mode · ledger · queue · profile
- Safer HTML headers (`X-Frame-Options`, `Cache-Control: no-store`)
- Request body size limit (`DJ_MAX_BODY_BYTES`, default 2 MB)

---

## Breaking / upgrade notes

| Change | Action |
|--------|--------|
| `DJ_LEDGER_BACKEND=postgres` stores the **Kernel ledger** on Postgres | Opt-in only; default remains SQLite. Conformance forces SQLite. |
| `profile=enterprise\|gcp` rejects inline `api_key` in toml | Use Secret Manager / env (`api_key_env`) |
| `DJ_JUDGE_MODE=llm` without tier keys | Process **exits** at boot |
| Review UI CSS tokens | Cosmetic only; no API break |
| Generic inbound | New route `/v1/inbound/generic` (does not replace GitHub) |

---

## Deferred (documented, not blockers for 5.0 pilot)

- OIDC/SAML (use API keys / local review credentials for pilot)
- Hard Postgres RLS multi-tenant isolation
- First-class GitLab/Azure DevOps connectors (generic plugin available)
- Full SaaS multi-region

See `ENTERPRISE_V1.md` and `ARCHITECTURE.md`.

---

## Verify

```bash
./scripts/smoke_enterprise.sh
DJ_DB=/tmp/dj.db DJ_DEV_KEYS=1 DJ_DEMO=off python3 run_conformance.py
```

## Package contents

- Application source (`app/`, `serve.py`, `seed/`, `demo/`)
- `docs/USER_GUIDE.md` — operator & risk-owner guide
- `ENTERPRISE_V1.md`, `ARCHITECTURE.md`, `RELEASE_NOTES_5.0.md`
- `LICENSE` (Apache-2.0), `SECURITY.md`
- `config/dj.example.toml`, `deploy/gcp/`, Docker assets
