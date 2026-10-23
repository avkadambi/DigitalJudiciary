"""
The LLM offices (governance build v3, §5.6): OF-D1, the owner's decision on a
due exception request, made by a model.

    shadow  the answer key (`Registry.decide_request_oracle`) binds; the model
            is only logged
    llm     the model binds; a grant over the yearly cap is issued and counted
            as a measured error (`grants_over_cap`)

The decision is taken in the arm-invariant shadow registry, so every arm sees
the same grants. Parse failure: deny.
"""

from __future__ import annotations

import json

from . import governance as gov
from .registry import ADMITTED_REASONS, EXCEPTIONS_PER_YEAR

OUTCOMES = ("granted", "covered", "denied_codified", "denied_reason", "denied_cap")
SCHEMA = {"decision": "|".join(OUTCOMES), "reasons": "<= 400 characters", "confidence": "0-100"}
REASON_WORDS = {"N": "necessity", "O": "opportunity", "K": "new knowledge", "NONE": "no reason stated"}


def validate(parsed: dict):
    if parsed.get("decision") not in OUTCOMES:
        return f"decision must be one of {OUTCOMES}"
    return None


def build_prompt(r: dict, registry, canon, day: int, style: str, cap: int = EXCEPTIONS_PER_YEAR) -> tuple:
    system = gov.load_prompt("office", style) + "\n\n" + gov.schema_text(SCHEMA)
    e = canon.entries.get(r["entry"])
    in_force = [t for t in registry.tokens.values()
                if t.scope == r["entry"] and not t.revoked and not t.consumed and day <= t.expires_day]
    u = ["THE RULE" if style == "canon" else "ENTRY"]
    u.append(gov.render_rule(e, style) if e is not None else f"- {r['entry']}: not a rule of the canon in force")
    u.append("")
    if style == "canon":
        reason = REASON_WORDS.get(r["reason"], r["reason"])
        admitted = ", ".join(REASON_WORDS[x] for x in ADMITTED_REASONS)
        u += ["THE REQUEST",
              f"- filed on working day {r['day']}; today is working day {day}",
              f"- reason given: {reason} (the admitted reasons are {admitted})",
              f"- evidence of that kind on file for the change: {'yes' if r['evidence_ok'] else 'no'}",
              "",
              "THE OFFICE'S BOOKS",
              f"- exceptions for this rule now in force: {len(in_force)}",
              f"- exceptions granted this year: {registry.granted} of at most {cap}"]
    else:
        u += ["REQUEST", "- " + json.dumps(r, sort_keys=True),
              f"- tokens in force for entry: {[t.id for t in in_force]}",
              f"- registry.granted={registry.granted} EXCEPTIONS_PER_YEAR={cap} ADMITTED_REASONS={list(ADMITTED_REASONS)}",
              f"- day={day}"]
    return system, "\n".join(u)


class Offices:
    def __init__(self, mode: str, style: str, client, flip):
        if mode not in ("llm", "shadow"):
            raise ValueError("the office seat object is for llm or shadow mode")
        self.mode, self.style, self.client, self.flip = mode, style, client, flip
        self.calls = self.failures = self.grants_over_cap = 0
        self.log: list = []

    def _ask(self, r, registry, canon, day, oracle) -> dict:
        self.calls += 1
        system, user = build_prompt(r, registry, canon, day, self.style)
        if self.client.mode != "live":
            self.client.account_dry(system, user, gov.DRY_OUT_TOKENS["office"])
            key = "office|" + r["act_id"] + "|" + r["entry"] + "|" + str(day)
            dec, flipped = oracle, False
            if self.flip is not None and self.flip.flip(key):
                dec, flipped = self.flip.choice(key, [x for x in OUTCOMES if x != oracle]), True
            return {"decision": dec, "reasons": "dry stand-in: the answer key", "confidence": 100,
                    "dry_flipped": flipped, "parse_failed": False}
        parsed, meta = self.client.call_json(system, user, validate=validate)
        if parsed is None:
            self.failures += 1
            return {"decision": "denied_reason", "reasons": "", "confidence": None, "parse_failed": True,
                    "fail_safe": "deny", "repaired": meta["repaired"]}
        return {"decision": parsed["decision"], "reasons": str(parsed.get("reasons") or "")[:400],
                "confidence": parsed.get("confidence") if isinstance(parsed.get("confidence"), (int, float)) else None,
                "parse_failed": False, "repaired": meta["repaired"]}

    def decider(self, r: dict, oracle: str, registry, canon, day: int) -> tuple:
        """(binding outcome, log fields) for one due request (`Registry.decide_requests`)."""
        dec = self._ask(r, registry, canon, day, oracle)
        dec["cost"] = dict(self.client.last_cost or {})
        binding = oracle if self.mode == "shadow" else dec["decision"]
        if binding == "granted" and oracle == "denied_cap":
            self.grants_over_cap += 1
        fields = {"office_llm": dec, "oracle_office": oracle, "office_mode": self.mode}
        self.log.append({"day": day, "act_id": r["act_id"], "entry": r["entry"], "oracle": oracle,
                         "decision": dec["decision"], "binding": binding})
        return binding, fields

    def state(self) -> dict:
        return {"calls": self.calls, "failures": self.failures, "grants_over_cap": self.grants_over_cap,
                "log": self.log}

    def restore(self, d: dict) -> None:
        self.calls = int(d.get("calls", 0))
        self.failures = int(d.get("failures", 0))
        self.grants_over_cap = int(d.get("grants_over_cap", 0))
        self.log = list(d.get("log") or [])
