"""
Doctrine by models (governance build v3, §5.6), arm D only.

DC-D1  the clerk writes the gloss for a holding (answer key `gloss_oracle`)
LW-D1  the lawmaker decides codification when a T1 class reaches K_CODIFY
       denies (answer key `codify_oracle`)
LW-D2  the lawmaker answers the court's referrals (logged only)

Whatever the clerk returns goes through `apply_gloss`, which writes the
holding and the class bar and nothing else: a reply that tries to change an
entry's tier, violate factors, kind, office or the canon version is refused
field by field and the attempt is logged (EC-19).

    shadow  the answer keys bind; the models are only logged
    llm     the clerk's gloss and the lawmaker's decision bind

Fail-safes: the clerk's mechanical gloss (the answer key), flagged degraded;
the lawmaker does not codify.
"""

from __future__ import annotations

import json

from . import governance as gov
from .doctrine import FIXED_FIELDS, HOLDING_FIELDS, codify_oracle, gloss_oracle

HOLDINGS = ("permit", "permit_conditional", "deny")
CLERK_SCHEMA = {"holding": "|".join(HOLDINGS), "act_class": "the class of act ruled on", "bars_class": "true|false",
                "gloss": "<= 300 characters: the ruling as one sentence of doctrine"}
LAWMAKER_SCHEMA = {"codify": "true|false", "reasons": "<= 400 characters"}
REFERRAL_SCHEMA = {"response": "<= 400 characters", "action": "none|establish_fact|amend|resolve_conflict"}
GUARDED = FIXED_FIELDS + ("canon_version", "version")


def apply_gloss(canon, entry_id: str, gloss: dict, day: int, base: dict | None = None) -> dict:
    """Write one clerk gloss to `entry_id`. Only the holding and the class bar are
    written; every guarded field the reply carries is refused. Returns
    {"written", "refused_fields"}."""
    e = canon.entry(entry_id)
    refused = sorted(k for k in GUARDED if k in gloss)
    h = {k: (base or {}).get(k) for k in HOLDING_FIELDS}
    h.update(day=day, holding=gloss.get("holding") if gloss.get("holding") in HOLDINGS else h.get("holding"),
             act_class=gloss.get("act_class") or h.get("act_class") or e.act_class)
    h["outcome"] = h["holding"]
    if gloss.get("gloss"):
        h["gloss"] = str(gloss["gloss"])[:300]
    e.gloss.holdings.append(h)
    if gloss.get("bars_class") and e.tier == "T1" and h["act_class"] not in e.gloss.no_waiver_classes:
        e.gloss.no_waiver_classes.append(h["act_class"])
    e.gloss.version += 1
    return {"written": h, "refused_fields": refused}


class Doctrine:
    def __init__(self, mode: str, style: str, clerk, lawmaker, flip):
        if mode not in ("llm", "shadow"):
            raise ValueError("the doctrine seat object is for llm or shadow mode")
        self.mode, self.style, self.clerk, self.lawmaker, self.flip = mode, style, clerk, lawmaker, flip
        self.calls = 0
        self.failures = {"clerk": 0, "lawmaker": 0}
        self.contaminated = 0          # binding glosses that differ from the answer key

    def _flip(self, key: str) -> bool:
        return self.flip is not None and self.flip.flip(key)

    # -- DC-D1 -------------------------------------------------------------
    def clerk_gloss(self, entry, holding: dict, day: int) -> dict:
        self.calls += 1
        oracle = gloss_oracle(entry, holding, day)
        system = gov.load_prompt("clerk", self.style) + "\n\n" + gov.schema_text(CLERK_SCHEMA)
        u = ["THE RULE", gov.render_rule(entry, self.style), "",
             "THE RULING" if self.style == "canon" else "HOLDING",
             f"- case {holding.get('case')}: {holding.get('holding')} on an act of class "
             f"{holding.get('act_class') or entry.act_class}, ruled on working day {day}"]
        user = "\n".join(u)
        if self.clerk.mode != "live":
            self.clerk.account_dry(system, user, gov.DRY_OUT_TOKENS["clerk"])
            out = {"holding": oracle["holding"]["holding"], "act_class": oracle["holding"]["act_class"],
                   "bars_class": oracle["bars_class"], "dry_flipped": False}
            if self._flip("clerk|" + entry.id + "|" + str(holding.get("case")) + "|" + str(day)):
                out["bars_class"] = not out["bars_class"] if entry.tier == "T1" else out["bars_class"]
                out["holding"] = "permit" if out["holding"] == "deny" else "deny"
                out["dry_flipped"] = True
            out["degraded"] = False
            return {"clerk": out, "oracle": oracle}
        parsed, meta = self.clerk.call_json(system, user, validate=lambda o: None if o.get("holding") in HOLDINGS
                                            else f"holding must be one of {HOLDINGS}")
        if parsed is None:
            self.failures["clerk"] += 1
            return {"clerk": {"holding": oracle["holding"]["holding"], "act_class": oracle["holding"]["act_class"],
                              "bars_class": oracle["bars_class"], "degraded": True}, "oracle": oracle}
        parsed["degraded"] = False
        parsed["repaired"] = meta["repaired"]
        return {"clerk": parsed, "oracle": oracle}

    def write(self, canon, entry_id: str, holding: dict, day: int) -> dict:
        """Write the gloss for one holding. Returns the log fields."""
        from .doctrine import write_gloss
        e = canon.entry(entry_id)
        res = self.clerk_gloss(e, holding, day)
        if self.mode == "shadow":
            write_gloss(canon, entry_id, holding, day)
            return {"clerk": res["clerk"], "oracle_gloss": res["oracle"], "binding": "oracle"}
        applied = apply_gloss(canon, entry_id, res["clerk"], day, base=holding)
        o = res["oracle"]
        contaminated = (applied["written"]["holding"] != o["holding"]["holding"]
                        or bool(res["clerk"].get("bars_class")) != o["bars_class"])
        self.contaminated += int(contaminated)
        return {"clerk": res["clerk"], "oracle_gloss": o, "binding": "clerk", "contaminated": contaminated,
                "refused_fields": applied["refused_fields"]}

    # -- LW-D1 -------------------------------------------------------------
    def maybe_codify(self, canon, entry_id: str, k: int, day: int) -> tuple:
        """(codified now?, log fields or None). Asked only when the class has
        reached `k` denies and is not yet codified."""
        e = canon.entry(entry_id)
        oracle = codify_oracle(e, k)
        if not oracle:
            return False, None
        self.calls += 1
        system = gov.load_prompt("lawmaker", self.style) + "\n\n" + gov.schema_text(LAWMAKER_SCHEMA)
        denies = [h for h in e.gloss.holdings if h.get("holding") == "deny" and h.get("act_class") == e.act_class]
        user = "\n".join(["THE RULE", gov.render_rule(e, self.style), "",
                          f"The court has refused this class of act {len(denies)} times, on working days "
                          + ", ".join(str(h.get("day")) for h in denies) + "."])
        if self.lawmaker.mode != "live":
            self.lawmaker.account_dry(system, user, gov.DRY_OUT_TOKENS["lawmaker"])
            dec = {"codify": not self._flip(f"lawmaker|{entry_id}|{day}"), "degraded": False}
            dec["dry_flipped"] = not dec["codify"]
        else:
            parsed, meta = self.lawmaker.call_json(system, user, validate=lambda o: None if isinstance(o.get("codify"), bool)
                                                   else "codify must be true or false")
            if parsed is None:
                self.failures["lawmaker"] += 1
                dec = {"codify": False, "degraded": True, "fail_safe": "no_codification"}
            else:
                dec = {"codify": parsed["codify"], "reasons": str(parsed.get("reasons") or "")[:400],
                       "degraded": False, "repaired": meta["repaired"]}
        binding = oracle if self.mode == "shadow" else dec["codify"]
        if binding:
            e.gloss.codified = True
            e.gloss.version += 1
        return bool(binding), {"lawmaker": dec, "oracle_codify": oracle, "day": day, "entry": entry_id}

    # -- LW-D2 -------------------------------------------------------------
    def answer_referral(self, case_id: str, grounds: dict, day: int) -> dict:
        self.calls += 1
        system = gov.load_prompt("lawmaker", self.style) + "\n\n" + gov.schema_text(REFERRAL_SCHEMA)
        user = "A REFERRAL FROM THE COURT\n" + json.dumps(dict(grounds, case=case_id, day=day), sort_keys=True)
        if self.lawmaker.mode != "live":
            self.lawmaker.account_dry(system, user, gov.DRY_OUT_TOKENS["lawmaker"])
            return {"response": "dry stand-in", "action": "none", "case": case_id, "day": day}
        parsed, meta = self.lawmaker.call_json(system, user)
        if parsed is None:
            self.failures["lawmaker"] += 1
            return {"response": None, "degraded": True, "case": case_id, "day": day}
        return {"response": str(parsed.get("response") or "")[:400], "action": parsed.get("action"),
                "case": case_id, "day": day}

    def state(self) -> dict:
        return {"calls": self.calls, "failures": dict(self.failures), "contaminated": self.contaminated}

    def restore(self, d: dict) -> None:
        self.calls = int(d.get("calls", 0))
        self.failures.update(d.get("failures") or {})
        self.contaminated = int(d.get("contaminated", 0))
