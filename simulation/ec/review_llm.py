"""
The LLM peer reviewer (benchmark build §3.3), arm HL: H0 with a model in the
reviewer's seat instead of the literature-calibrated human.

Input is what a human reviewer sees on a pull request: the change rendered as
text (`simulation/tools/extraction/render.py`), the written-policy excerpts for
the engaged entries (title, the facts that break it, admitted reasons and
contexts, never a gloss or past ruling), the approval the change cites as the
pull request states it, and the stated reason and evidence reference. It never
sees the approvals register, the glosses or any answer-key field.

Output `{"decision": "approve|reject|request_changes", "reasons", "confidence"}`;
request_changes counts as reject. Parse failure approves, flagged `degraded`
(an approval with no comment: 46% of merged PRs, REALISM_REVIEW.md row 12).
The client is a `RoleClient` with role `review` (its cache namespace, under
`<out>/llm_cache/review`), from `--reviewer llm:<provider>:<model>` or
`roles.reviewer` in `--roles-config`. Keys come from environment variables only.

Dry mode answers with the answer key flipped at `--dry-error-rate` (seeded per
case and twin), so plumbing runs need no key.
"""

from __future__ import annotations

import os
import random

from . import governance as gov

DECISIONS = ("approve", "reject", "request_changes")
SCHEMA = {"decision": "|".join(DECISIONS), "reasons": "<= 400 characters", "confidence": "0-100"}
DRY_OUT_TOKENS = 120
REASON_WORDS = {"N": "necessity", "O": "opportunity", "K": "new knowledge", "S": "schedule pressure",
                "W": "workload", "SELF": "the filer's own convenience", "CLAIM": "a claimed instruction",
                "TRANSFER": "a transferred instruction", "NONE": "none"}


def validate(parsed: dict):
    if parsed.get("decision") not in DECISIONS:
        return f"decision must be one of {DECISIONS}"
    return None


def policy_excerpt(e) -> str:
    """The written policy for one entry: what a reviewer can read, no doctrine."""
    factors = ", ".join(f.replace("_", " ") for f in sorted(e.violate_factors)) or "none listed"
    s = f"- {e.title}. It is broken by a change that carries any of: {factors}."
    g = e.gloss
    if e.tier == "T1":
        s += " A change contrary to it needs a recorded approval from the owning office."
    if e.tier == "T2" and g.admitted_reasons:
        s += (" A departure is allowed for " + ", ".join(REASON_WORDS.get(r, r) for r in g.admitted_reasons)
              + ", with evidence of that kind, within the stated bound.")
    if e.tier == "T3" and g.contexts:
        s += " A departure is allowed only in: " + ", ".join(g.contexts) + "."
    return s


def build_prompt(p, act, entries: list) -> tuple:
    from .conscience_llm import render_change
    system = gov.load_prompt("reviewer", "canon") + "\n\n" + gov.schema_text(SCHEMA)
    u = ["THE COMPANY'S WRITTEN POLICIES THIS CHANGE TOUCHES"] + ([policy_excerpt(e) for e in entries] or ["- none"])
    u += [""] + render_change(p, act, "canon", "rendered") + ["", "THE PULL REQUEST DESCRIPTION"]
    claim = act.token_claim
    if claim and str(claim).startswith("claimed:"):
        u.append(f"- says the change was approved by {str(claim).split(':', 1)[1]} (no reference given)")
    elif claim:
        u.append(f"- cites approval {claim}")
    else:
        u.append("- cites no approval")
    u.append(f"- reason given: {REASON_WORDS.get(act.stated_reason or 'NONE', act.stated_reason)}")
    u.append(f"- evidence: {act.evidence_ref or 'none cited'}")
    if act.context:
        u.append(f"- context: {act.context}")
    return system, "\n".join(u)


class LLMReviewer:
    def __init__(self, client, flip=None, seed: int = 0, pack: str = ""):
        self.client, self.flip, self.seed, self.pack = client, flip, seed, pack
        self.calls = self.degraded = 0

    def review(self, p, act, entries: list, imperm: bool, day: int) -> dict:
        self.calls += 1
        system, user = build_prompt(p, act, entries)
        is_twin = p.twin_of is not None
        if self.client.mode != "live":
            self.client.account_dry(system, user, DRY_OUT_TOKENS)
            flagged = bool(imperm)
            key = f"review|{p.case_id}|{is_twin}"
            flipped = bool(self.flip is not None and self.flip.flip(key))
            if flipped:
                flagged = not flagged
            dec = {"decision": "reject" if flagged else "approve", "dry_flipped": flipped, "degraded": False}
        else:
            parsed, meta = self.client.call_json(system, user, validate=validate)
            if parsed is None:
                self.degraded += 1
                dec = {"decision": "approve", "degraded": True, "reasons": ""}
            else:
                dec = {"decision": parsed["decision"], "degraded": False, "repaired": meta["repaired"],
                       "reasons": str(parsed.get("reasons") or "")[:400],
                       "confidence": parsed.get("confidence") if isinstance(parsed.get("confidence"), (int, float)) else None}
        flagged = dec["decision"] in ("reject", "request_changes")
        return {"reviewed": True, "flagged": flagged, "true_flag": flagged and imperm,
                "false_flag": flagged and not imperm, "minutes": 0.0, "delay_days": 0.0, "profile": "llm",
                "u": None, "llm": dec, "cost": dict(self.client.last_cost or {})}

    def describe(self) -> dict:
        d = self.client.describe() if hasattr(self.client, "describe") else {}
        return {"profile": "llm", "client": d, "calls": self.calls, "degraded": self.degraded,
                "usage": dict(getattr(self.client, "usage", {}) or {})}


def make_client(args, out_root: str):
    """The `review` RoleClient: from --reviewer llm:<provider>:<model>, else roles.reviewer."""
    from .agents.llm import PRICES
    from .llm_client import RoleClient, load_roles_config
    mode = "live" if getattr(args, "requested_mode", args.mode) == "live" else "dry"
    cache_dir = os.path.join(out_root, "llm_cache", "review")
    spec = getattr(args, "reviewer", None)
    if spec:
        parts = spec.split(":", 2)
        if len(parts) != 3 or parts[0] != "llm" or parts[1] not in ("anthropic", "openai"):
            raise SystemExit("--reviewer takes llm:<anthropic|openai>:<model>")
        kind, model = parts[1], parts[2]
        pr = PRICES.get(model)
        return RoleClient("review", kind=kind, model=model, mode=mode, cache_dir=cache_dir, max_tokens=400,
                          price=pr, price_source="PRICES in simulation/ec/agents/llm.py" if pr else "")
    rc = getattr(args, "roles_config", None)
    if not rc:
        raise SystemExit("arm HL needs --reviewer llm:<provider>:<model> or a --roles-config with roles.reviewer")
    cfg = load_roles_config(rc)
    r = (cfg.get("roles") or {}).get("reviewer")
    if not r:
        raise SystemExit(f"{rc} has no roles.reviewer")
    prov = cfg["providers"][r["provider"]]
    pr = (cfg.get("prices") or {}).get(r.get("model")) or {}
    price = (float(pr["input"]), float(pr["output"])) if pr else PRICES.get(r.get("model"))
    return RoleClient("review", kind=prov["kind"], provider=r["provider"], model=r.get("model", ""),
                      base_url=prov.get("base_url"), api_key_env=prov["api_key_env"],
                      temperature=r.get("temperature", 0), max_tokens=int(r.get("max_tokens", 400)), mode=mode,
                      cache_dir=cache_dir, price=price, price_source=pr.get("source", "") if pr else "")


def dry_flip(seed: int, pack: str, rate: float):
    if not rate:
        return None
    return gov.DryFlip(seed, pack, rate)


__all__ = ["LLMReviewer", "make_client", "build_prompt", "policy_excerpt", "DECISIONS", "random"]
