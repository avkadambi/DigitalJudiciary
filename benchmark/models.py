"""Model clients for the benchmark. Stdlib only, matching the container.

Two implementations:

  APIModel   the real thing, over the Messages API, temperature 0.
  MockModel  deterministic stand-ins that let the whole pipeline be validated
             offline. Mock numbers are PIPELINE CHECKS, never findings, and
             every artifact the harness writes says so in its own metadata.

The mocks are not strawmen and not oracles. Each one implements the most
plausible thing its condition's information actually supports:

  rules_only  applies the provision predicate to the facts. This is roughly
              the ceiling for a careful model with no case knowledge.
  b_mem       copies the holding of the most similar remembered case,
              including lapsed and overruled ones, because nothing in that
              condition tells it which memories still carry authority. That
              is the failure mode the condition exists to measure.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

ENDPOINT = "https://api.anthropic.com/v1/messages"

MODEL_ALIASES = {
    "haiku": "claude-haiku-4-5-20251001",
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-5",
}


def resolve_model(name: str) -> str:
    return MODEL_ALIASES.get(name, name)


class ModelResult:
    __slots__ = ("text", "input_tokens", "output_tokens", "latency_ms",
                 "degraded", "error")

    def __init__(self, text="", input_tokens=0, output_tokens=0,
                 latency_ms=0, degraded=False, error=""):
        self.text = text
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.latency_ms = latency_ms
        self.degraded = degraded
        self.error = error

    def json(self) -> dict | None:
        t = self.text.strip()
        if t.startswith("```"):
            t = t.strip("`").removeprefix("json").strip()
        start, end = t.find("{"), t.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            return json.loads(t[start:end + 1])
        except json.JSONDecodeError:
            return None


class APIModel:
    kind = "api"

    def __init__(self, model: str, max_tokens: int = 600):
        self.model = resolve_model(model)
        self.max_tokens = max_tokens
        self.api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        self.timeout = float(os.environ.get("DJ_BENCH_TIMEOUT_S", "60"))
        if not self.api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is required for a live run."
                " Use --mock to validate the pipeline offline.")

    def ask(self, system: str, user: str) -> ModelResult:
        body = json.dumps({
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": 0,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }).encode()
        req = urllib.request.Request(
            ENDPOINT, data=body,
            headers={"content-type": "application/json",
                     "x-api-key": self.api_key,
                     "anthropic-version": "2023-06-01"})
        t0 = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                data = json.loads(r.read())
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            return ModelResult(latency_ms=int((time.monotonic() - t0) * 1000),
                               degraded=True, error=str(e))
        text = "".join(b.get("text", "") for b in data.get("content", [])
                       if b.get("type") == "text")
        u = data.get("usage", {})
        return ModelResult(text, u.get("input_tokens", 0),
                           u.get("output_tokens", 0),
                           int((time.monotonic() - t0) * 1000))


class MockModel:
    """Deterministic stand-in. `mode` selects the condition it is imitating."""

    kind = "mock"

    def __init__(self, mode: str, model: str = "mock"):
        self.mode = mode
        self.model = f"mock:{model}"

    def ask(self, system: str, user: str) -> ModelResult:
        payload = json.loads(user[user.find("{"):user.rfind("}") + 1])
        if self.mode == "rules_only":
            out = self._rules_only(payload)
        elif self.mode == "b_mem":
            out = self._b_mem(payload)
        else:
            out = {"distinguished": False, "grounds": "mock"}
        text = json.dumps(out)
        return ModelResult(text, len(user) // 4, len(text) // 4, 1)

    @staticmethod
    def _rules_only(p: dict) -> dict:
        if p.get("control_plane"):
            return {"outcome": "not_adjudicated", "exit": "amendment",
                    "provision": "constitution",
                    "rationale": "this change edits the rulebook itself",
                    "cited_records": []}
        facts = set(p["facts"])
        for prov in p["provisions"]:
            pol = prov.get("policy", {})
            hit = sorted(set(pol.get("deny_if_any", [])) & facts)
            if hit:
                return {"outcome": "deny",
                        "exit": "amendment" if prov.get("absolute")
                                else "challenge",
                        "provision": prov["provision_id"],
                        "rationale": f"factors {hit} violate "
                                     f"{prov['provision_id']}",
                        "cited_records": []}
        return {"outcome": "permit", "exit": "none",
                "provision": (p["provisions"][0]["provision_id"]
                              if p["provisions"] else None),
                "rationale": "no provision predicate is violated",
                "cited_records": []}

    @staticmethod
    def _b_mem(p: dict) -> dict:
        if p.get("control_plane"):
            return MockModel._rules_only(p)
        facts = set(p["facts"])
        absolutes = {pr["provision_id"] for pr in p["provisions"]
                     if pr.get("absolute")}
        best, best_j = None, 0.0
        for rec in p.get("memory", []):
            rf = set(rec["facts"])
            union = facts | rf
            j = len(facts & rf) / len(union) if union else 0.0
            if j > best_j:
                best, best_j = rec, j
        # Ungoverned memory has no notion of a floor that memory cannot
        # override, and no notion of a memory that has expired.
        if best and best_j >= 0.25:
            outcome = best["outcome"]
            return {"outcome": "permit_conditional"
                            if outcome == "accept_risk" else outcome,
                    "exit": "none" if outcome != "deny" else "challenge",
                    "provision": best["provision_id"],
                    "rationale": f"a past case with {best_j:.0%} factor "
                                 f"overlap was resolved this way",
                    "cited_records": [best["id"]]}
        out = MockModel._rules_only(p)
        if out["provision"] in absolutes:
            out["exit"] = "amendment"
        return out


def build_model(condition: str, model: str, mock: bool):
    if mock:
        return MockModel(condition, model)
    return APIModel(model)
