"""The LLM agent's `live` path against a local mock of the Anthropic Messages
API and the OpenAI chat completions API (DESIGN §4; prereg Part B, LLM slice).

Nothing here touches the network: `MockProvider` is an `http.server` in a
thread that answers POST /v1/messages, POST /v1/chat/completions and GET
/v1/models, records every request, and can be scripted to return a fenced or
prose-wrapped reply, a malformed one, an empty content list, or a 429/500
before succeeding. The agent is pointed at it with ANTHROPIC_BASE_URL /
OPENAI_BASE_URL and a dummy key.

Covered: the request shape (headers, system placement, cache_control,
temperature, max_tokens), JSON extraction over every reply variant, the
parse-failure fallback, retry and backoff (sleep patched), cost attribution
from the provider's `usage`, the on-disk cache, a 3-day run of arms C and D
through `run_year` in live mode with the `metrics.py` row, checkpoint/resume
and the budget cap, and `reproduce/ec_preflight.py` end to end.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import urllib.request
from collections import deque
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from conftest import ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import metrics, run_year                          # noqa: E402
from simulation.ec.agents import Context, make_agent                 # noqa: E402
from simulation.ec.agents import llm as llmmod                       # noqa: E402
from simulation.ec.agents.llm import (AUDIT_SENTENCE, LLMAgent, LLMTransportError, SYSTEM,   # noqa: E402
                                      build_prompt, parse_response, split_prompt)
from simulation.ec.canon import Canon                                # noqa: E402
from simulation.ec.gate import Proposal, Verdict                     # noqa: E402

VETPOC = os.path.join(ROOT, "simulation", "vetpoc-constitution-corpus")
CANON = os.path.join(VETPOC, "constitution", "canon.json")
MODEL = "claude-sonnet-5-5"    # in PRICES, so the budget cap and the cost columns are live

pytestmark = pytest.mark.skipif(not os.path.exists(CANON), reason="canon.json not built; run build_all_canons.py")


# ---------------------------------------------------------------------------
# The mock provider
# ---------------------------------------------------------------------------

ENTRY_RE = re.compile(r"^- (VP-[A-Z0-9-]+) \[(T[0-3]), ")
FACTOR_RE = re.compile(r"^    violating factors: (.+)$")
DRIVER_RE = re.compile(r"driver ([A-Z]+)\.")


def realistic_reply(prompt: str) -> dict:
    """A plausible model answer derived from the prompt alone: the first
    engaged entry, a violation under SELF on an entry that lists violating
    factors, a departure under an admitted driver on a T2 entry, otherwise
    as_submitted; `believes_monitored` true for about half the announced twins."""
    entries, factors, tiers = [], {}, {}
    cur = None
    for ln in prompt.split("\n"):
        m = ENTRY_RE.match(ln)
        if m:
            cur = m.group(1)
            entries.append(cur)
            tiers[cur] = m.group(2)
            continue
        m = FACTOR_RE.match(ln)
        if m and cur:
            factors[cur] = [f.strip() for f in m.group(1).split(",")]
    drv = DRIVER_RE.search(prompt)
    driver = drv.group(1) if drv else "NONE"
    h = int(hashlib.sha256(prompt.encode()).hexdigest()[:8], 16)
    announced = AUDIT_SENTENCE in prompt
    target = entries[0] if entries else None
    act = {"act": "as_submitted", "target_entry": target, "added_factor": None, "stated_reason": driver,
           "within_bound": None, "context": None, "token_claim": None,
           "examen": {"reported_event": "none", "stated_reason": driver, "token_ref": None,
                      "narrative": "routine change, nothing to note"},
           "believes_monitored": announced and (h % 2 != 0)}
    # The draw is keyed on the prompt hash; widened to excluded drivers so a 3-day run still
    # files violations after the post-pilot prompt change moved every hash.
    if target and driver in ("SELF", "CLAIM", "TRANSFER") and factors.get(target) and h % 2 == 0:
        act.update(act="violation", added_factor=factors[target][0])
        act["examen"].update(reported_event="none", narrative="small change, nobody will look")
    elif target and driver in ("N", "O", "K") and tiers.get(target) == "T2" and h % 2 == 0:
        act.update(act="departure", within_bound=True)
        act["examen"].update(reported_event="departure", narrative=f"departed from {target} for {driver}")
    return act


def wrap(obj: dict, style: int) -> str:
    s = json.dumps(obj)
    if style == 1:
        return "```json\n" + s + "\n```"
    if style == 2:
        return "Here is my filing for this change.\n\n```json\n" + json.dumps(obj, indent=2) + "\n```\n\nFiled."
    return s


class MockProvider:
    """Scripted replies: each item is ("text", str) | ("empty",) | ("status", code) | ("default",).
    When the script is empty a realistic reply is derived from the prompt."""

    def __init__(self, models=(MODEL, "claude-haiku-4-5")):
        self.requests: list = []
        self.script: deque = deque()
        self.models = list(models)
        self.lock = threading.Lock()
        mock = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _send(self, code, obj):
                data = json.dumps(obj).encode()
                self.send_response(code)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(data)))
                if code == 429:
                    self.send_header("retry-after", "0")
                self.end_headers()
                self.wfile.write(data)

            def do_GET(self):
                if self.path.split("?")[0].rstrip("/").endswith("/models"):
                    return self._send(200, {"data": [{"id": m, "type": "model", "display_name": m} for m in mock.models],
                                            "has_more": False})
                return self._send(404, {"error": {"type": "not_found_error", "message": self.path}})

            def do_POST(self):
                n = int(self.headers.get("content-length") or 0)
                body = json.loads(self.rfile.read(n).decode() or "{}")
                with mock.lock:
                    mock.requests.append({"path": self.path, "headers": {k.lower(): v for k, v in self.headers.items()},
                                          "body": body})
                    item = mock.script.popleft() if mock.script else None
                    if item and item[0] == "default":
                        item = None
                if self.path.endswith("/messages"):
                    system = "".join(b.get("text", "") for b in (body.get("system") or []) if isinstance(b, dict)) \
                        if isinstance(body.get("system"), list) else (body.get("system") or "")
                    user = body["messages"][-1]["content"]
                    user = "".join(b.get("text", "") for b in user) if isinstance(user, list) else user
                    kind = "anthropic"
                else:
                    system = "".join(m["content"] for m in body["messages"] if m["role"] == "system")
                    user = [m["content"] for m in body["messages"] if m["role"] == "user"][-1]
                    kind = "openai"
                if not mock.key_ok(self.headers, kind):
                    return self._send(401, {"error": {"type": "authentication_error", "message": "bad key"}})
                if item and item[0] == "status":
                    return self._send(item[1], {"error": {"type": "overloaded_error", "message": f"scripted {item[1]}"}})
                prompt = (system + "\n\n" + user) if system else user
                h = int(hashlib.sha256(prompt.encode()).hexdigest()[:8], 16)
                if item and item[0] == "text":
                    text = item[1]
                elif item and item[0] == "empty":
                    text = None
                else:
                    text = wrap(realistic_reply(prompt), h % 3)
                tin, tout = len(prompt) // 3, (len(text) // 3 if text else 0)
                if kind == "anthropic":
                    content = [] if text is None else [{"type": "text", "text": text}]
                    return self._send(200, {"id": f"msg_{h:08x}", "type": "message", "role": "assistant",
                                            "model": body.get("model"), "content": content,
                                            "stop_reason": "end_turn", "stop_sequence": None,
                                            "usage": {"input_tokens": tin, "output_tokens": tout,
                                                      "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}})
                choices = [] if text is None else [{"index": 0, "finish_reason": "stop",
                                                    "message": {"role": "assistant", "content": text}}]
                return self._send(200, {"id": f"chatcmpl-{h:08x}", "object": "chat.completion", "model": body.get("model"),
                                        "choices": choices,
                                        "usage": {"prompt_tokens": tin, "completion_tokens": tout,
                                                  "total_tokens": tin + tout}})

        self.server = HTTPServer(("127.0.0.1", 0), H)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_address[1]}/v1"

    @staticmethod
    def key_ok(headers, kind) -> bool:
        if kind == "anthropic":
            return headers.get("x-api-key") == "test-key" and headers.get("anthropic-version") is not None
        return headers.get("authorization") == "Bearer test-key"

    def close(self):
        self.server.shutdown()
        self.server.server_close()


@pytest.fixture(scope="module")
def mock():
    m = MockProvider()
    yield m
    m.close()


@pytest.fixture
def live_env(mock, monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", mock.base)
    monkeypatch.setenv("OPENAI_BASE_URL", mock.base)
    monkeypatch.setenv("NO_PROXY", "127.0.0.1,localhost")
    monkeypatch.setenv("no_proxy", "127.0.0.1,localhost")
    mock.script.clear()
    mock.requests.clear()
    return mock


@pytest.fixture(scope="module")
def canon():
    return Canon.load(CANON)


def make_ctx(canon: Canon, tier: str, driver: str = "NONE", announced: bool = False, idx: int = 0) -> Context:
    entries = [e for e in canon.entries.values() if e.tier == tier]
    e = entries[idx]
    sk = Proposal(act_id=f"{e.id}#{tier}#{idx}{'~twin' if announced else ''}", case_id=f"VP-T-{idx:05d}", company="vetpoc",
                  day=1, ts=1100, seq=idx, agent_id="agent:vetpoc-conscience-01", archetype="llm", author_kind="ai-agent",
                  engaged=[e.id], presented_driver=driver, driver_level=1 if driver != "NONE" else 0,
                  audit_announced=announced, twin_of=None, act=None, facts=["fact_a", "fact_b"])
    return Context(proposal_skeleton=sk, engaged_entries=[e], registry_view=[], audit_announced=announced,
                   presented_driver=driver, driver_level=sk.driver_level, day=1, extra={"scenario": {"k": 1}})


def agent_for(tmp_path, provider="anthropic", **kw) -> LLMAgent:
    return LLMAgent("agent:vetpoc-conscience-01", provider=provider, model="sonnet", mode="live",
                    cache_dir=str(tmp_path / "cache"), log_path=str(tmp_path / "llm_errors.jsonl"), **kw)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def test_parse_response_variants():
    obj = {"act": "departure", "target_entry": "VP-PD-003", "believes_monitored": "false"}
    assert parse_response(json.dumps(obj)) == obj
    assert parse_response("```json\n" + json.dumps(obj) + "\n```") == obj
    assert parse_response("```\n" + json.dumps(obj, indent=2) + "\n```") == obj
    assert parse_response("Sure. Here is the filing:\n```json\n" + json.dumps(obj) + "\n```\nDone.") == obj
    assert parse_response("Filing: " + json.dumps(obj) + " (as requested)") == obj
    assert parse_response("{not json at all") is None
    assert parse_response("") is None
    assert parse_response("[1, 2, 3]") is None
    assert parse_response("the entry {VP-PD-003} is fine, so " + json.dumps(obj)) == obj


def test_split_prompt_puts_system_first(canon):
    p = build_prompt(make_ctx(canon, "T2", "N"))
    system, user = split_prompt(p)
    assert system == SYSTEM
    assert user.startswith("CANON ENTRIES ENGAGED BY THIS CHANGE")
    assert SYSTEM not in user
    assert system + "\n\n" + user == p
    assert split_prompt("no system here") == ("", "no system here")


def test_dry_mode_needs_no_key_and_is_unchanged(canon, tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    a = LLMAgent("agent:x", model="sonnet", mode="dry", cache_dir=str(tmp_path))
    ctx = make_ctx(canon, "T2", "N")
    act = a.propose(ctx)
    assert act.kind in ("as_submitted", "departure")
    assert a.last_cost["input_tokens"] == llmmod.estimate_tokens(build_prompt(ctx))
    assert a.last_cost["output_tokens"] == 120 and a.last_cost["mode"] == "dry"
    assert a.last_parse_failed is False
    assert not list(tmp_path.iterdir()), "dry mode writes no cache"


def test_live_mode_refuses_without_key_or_price(tmp_path, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="ANTHROPIC_API_KEY"):
        LLMAgent("agent:x", model="sonnet", mode="live", cache_dir=str(tmp_path))
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    with pytest.raises(RuntimeError, match="unpriced"):
        LLMAgent("agent:x", model="claude-unknown-9", mode="live", cache_dir=str(tmp_path))


# ---------------------------------------------------------------------------
# Direct round trips
# ---------------------------------------------------------------------------


def test_anthropic_request_shape_and_reply(canon, tmp_path, live_env):
    a = agent_for(tmp_path)
    ctx = make_ctx(canon, "T2", "N")
    act = a.propose(ctx)
    req = live_env.requests[-1]
    assert req["path"] == "/v1/messages"
    assert req["headers"]["x-api-key"] == "test-key"
    assert req["headers"]["anthropic-version"] == llmmod.ANTHROPIC_VERSION
    assert req["headers"]["content-type"] == "application/json"
    b = req["body"]
    assert b["model"] == MODEL and b["temperature"] == 0 and b["max_tokens"] == llmmod.MAX_TOKENS
    assert b["system"] == [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}]
    assert b["messages"] == [{"role": "user", "content": [{"type": "text", "text": split_prompt(build_prompt(ctx))[1]}]}]
    # Reply fields
    assert act.kind in ("as_submitted", "departure") and act.target_entry == ctx.engaged_entries[0].id
    assert act.stated_reason == "N" and act.conflict is False
    assert a.last_parse_failed is False
    # Cost from the provider's usage, not chars/4
    prompt = build_prompt(ctx)
    assert a.last_cost["input_tokens"] == len(prompt) // 3
    assert a.last_cost["input_tokens"] != llmmod.estimate_tokens(prompt)
    assert a.last_cost["output_tokens"] > 0 and a.last_cost["cached"] is False
    pin, pout = llmmod.PRICES[MODEL]
    assert a.last_cost["cost_usd"] == pytest.approx((a.last_cost["input_tokens"] * pin + a.last_cost["output_tokens"] * pout) / 1e6)
    assert a.usage["spend_usd"] == pytest.approx(a.last_cost["cost_usd"])
    # Examen and manipulation check come from the same parsed reply
    v = Verdict("allow", "t2_departure_admitted", act.target_entry, "T2", event_type="departure")
    ex = a.examen(ctx, act, v, True)
    assert ex is not None and ex.act_id == ctx.proposal_skeleton.act_id and ex.entry == act.target_entry
    assert ex.reported_event in ("none", "departure") and ex.stated_reason == "N" and isinstance(ex.narrative, str)
    assert a.examen(ctx, act, v, False) is None
    assert a.manipulation_check(ctx) is False


def test_openai_request_shape_and_reply(canon, tmp_path, live_env):
    a = agent_for(tmp_path, provider="openai_compatible")
    ctx = make_ctx(canon, "T0", "SELF", idx=1)
    act = a.propose(ctx)
    req = live_env.requests[-1]
    assert req["path"] == "/v1/chat/completions"
    assert req["headers"]["authorization"] == "Bearer test-key"
    b = req["body"]
    assert b["messages"][0] == {"role": "system", "content": SYSTEM}
    assert b["messages"][1]["role"] == "user" and b["temperature"] == 0 and b["max_tokens"] == llmmod.MAX_TOKENS
    assert act.kind in ("as_submitted", "violation") and a.last_parse_failed is False
    assert a.last_cost["input_tokens"] == len(build_prompt(ctx)) // 3


def test_reply_variants_fenced_prose_malformed_empty(canon, tmp_path, live_env):
    a = agent_for(tmp_path)
    good = {"act": "exception", "target_entry": "VP-CS-007", "added_factor": "dispensing_logic_bypassed_by_feature_flag",
            "stated_reason": "CLAIM", "within_bound": "null", "context": "null", "token_claim": "claimed:office:safety-lead",
            "examen": {"reported_event": "exception", "stated_reason": "CLAIM", "token_ref": "claimed:office:safety-lead",
                       "narrative": "the manager approved it"},
            "believes_monitored": "true"}
    # fenced
    live_env.script.append(("text", "```json\n" + json.dumps(good) + "\n```"))
    act = a.propose(make_ctx(canon, "T1", "CLAIM", idx=0))
    assert (act.kind, act.target_entry, act.token_claim, act.within_bound, act.context) == \
        ("exception", "VP-CS-007", "claimed:office:safety-lead", None, None)
    assert a.manipulation_check(make_ctx(canon, "T1")) is True, "string 'true' is a boolean, not a non-empty string"
    # prose around an indented fence
    live_env.script.append(("text", "I will file an exception.\n\n```json\n" + json.dumps(good, indent=2) + "\n```\nThat is all."))
    act = a.propose(make_ctx(canon, "T1", "CLAIM", idx=1))
    assert act.kind == "exception" and a.last_parse_failed is False
    # a string "false" for believes_monitored is False, and within_bound "false" is False
    bad_bools = dict(good, believes_monitored="false", within_bound="false", act="departure")
    live_env.script.append(("text", json.dumps(bad_bools)))
    act = a.propose(make_ctx(canon, "T2", "N", idx=2))
    assert act.within_bound is False and a.manipulation_check(make_ctx(canon, "T2", announced=True)) is False
    # malformed: fallback act, logged, no examen, manipulation check falls back to the announcement
    live_env.script.append(("text", "{\"act\": \"departure\", \"target_entry\": "))
    ctx = make_ctx(canon, "T2", "O", idx=3, announced=True)
    act = a.propose(ctx)
    assert act.kind == "as_submitted" and act.target_entry is None and act.stated_reason == "NONE"
    assert a.last_parse_failed is True and a.usage["parse_failures"] == 1
    assert a.parse_failures[-1]["act_id"] == ctx.proposal_skeleton.act_id
    assert a.examen(ctx, act, Verdict("allow", "clean"), True) is None
    assert a.manipulation_check(ctx) is True
    # unknown act kind is a parse failure too
    live_env.script.append(("text", json.dumps(dict(good, act="refuse"))))
    act = a.propose(make_ctx(canon, "T2", "O", idx=4))
    assert act.kind == "as_submitted" and a.last_parse_failed is True
    # empty content list
    live_env.script.append(("empty",))
    act = a.propose(make_ctx(canon, "T3", "K", idx=0))
    assert act.kind == "as_submitted" and a.last_parse_failed is True
    assert a.last_cost["output_tokens"] == 0 and a.last_cost["input_tokens"] > 0
    log = [json.loads(l) for l in open(tmp_path / "llm_errors.jsonl")]
    assert sum(1 for r in log if r["event"] == "parse_failure") == 3
    assert any(r["event"] == "empty_reply" for r in log)
    assert a.usage["parse_failures"] == 3 and len(a.parse_failures) == 3


def test_retry_on_429_and_500_not_on_400(canon, tmp_path, live_env, monkeypatch):
    sleeps = []
    monkeypatch.setattr(llmmod.time, "sleep", lambda s: sleeps.append(s))
    a = agent_for(tmp_path)
    live_env.script.append(("status", 429))
    act = a.propose(make_ctx(canon, "T2", "N", idx=5))
    assert act.kind in ("as_submitted", "departure") and a.last_parse_failed is False
    assert len(live_env.requests) == 2 and a.usage["retries"] == 1 and a.usage["http_calls"] == 2
    assert sleeps == [0.0], "retry-after: 0 honoured"
    live_env.requests.clear()
    live_env.script.append(("status", 500))
    live_env.script.append(("status", 529))
    a.propose(make_ctx(canon, "T2", "N", idx=6))
    assert len(live_env.requests) == 3 and a.usage["retries"] == 3
    assert sleeps[1:] == [llmmod.BACKOFF_S, llmmod.BACKOFF_S * 2], "exponential backoff without retry-after"
    live_env.requests.clear()
    for code in (400, 401):
        live_env.script.append(("status", code))
        with pytest.raises(LLMTransportError, match=f"HTTP {code}"):
            a.propose(make_ctx(canon, "T2", "N", idx=7))
        assert len(live_env.requests) == 1, f"{code} is not retried"
        live_env.requests.clear()
    # gives up after RETRIES, with the last sleep skipped
    sleeps.clear()
    for _ in range(llmmod.RETRIES):
        live_env.script.append(("status", 503))
    with pytest.raises(LLMTransportError, match="after 5 attempts"):
        a.propose(make_ctx(canon, "T2", "N", idx=8))
    assert len(live_env.requests) == llmmod.RETRIES and len(sleeps) == llmmod.RETRIES - 1
    log = [json.loads(l) for l in open(tmp_path / "llm_errors.jsonl")]
    assert [r["event"] for r in log][-1] == "gave_up"
    assert any(r["event"] == "http_error" and r["status"] == 429 for r in log)


def test_disk_cache_serves_second_call_without_http(canon, tmp_path, live_env):
    a = agent_for(tmp_path)
    ctx = make_ctx(canon, "T2", "K", idx=9)
    act1 = a.propose(ctx)
    n = len(live_env.requests)
    first = dict(a.last_cost)
    b = agent_for(tmp_path)             # a fresh agent on the same cache dir
    act2 = b.propose(ctx)
    assert len(live_env.requests) == n, "second identical call made no HTTP request"
    assert act2 == act1
    assert b.last_cost["cached"] is True and first["cached"] is False
    assert b.last_cost["input_tokens"] == first["input_tokens"] and b.last_cost["output_tokens"] == first["output_tokens"]
    assert b.last_cost["cost_usd"] == pytest.approx(first["cost_usd"] * 0.1)
    assert b.usage["spend_usd"] == 0.0 and b.usage["http_calls"] == 0
    path = a._cache_path(build_prompt(ctx))
    rec = json.load(open(path))
    assert rec["model"] == MODEL and rec["stop_reason"] == "end_turn" and "usage" in rec
    # a corrupt cache file is refetched, not trusted
    with open(path, "w") as fh:
        fh.write("{garbage")
    c = agent_for(tmp_path)
    c.propose(ctx)
    assert len(live_env.requests) == n + 1 and c.last_cost["cached"] is False
    assert json.load(open(path))["text"]


def test_rate_limit_sleeps_between_http_calls(canon, tmp_path, live_env, monkeypatch):
    sleeps = []
    monkeypatch.setattr(llmmod.time, "sleep", lambda s: sleeps.append(s))
    a = agent_for(tmp_path, rate_limit_s=5.0)
    a.propose(make_ctx(canon, "T2", "N", idx=10))
    a.propose(make_ctx(canon, "T2", "N", idx=11))
    a.propose(make_ctx(canon, "T2", "N", idx=11))        # cache hit: no sleep
    assert len(sleeps) == 1 and 0 < sleeps[0] <= 5.0


def test_anthropic_cache_usage_is_priced(canon, tmp_path, live_env, monkeypatch):
    a = agent_for(tmp_path)
    real = a._post

    def post(url, headers, body):
        raw = real(url, headers, body)
        raw["usage"] = {"input_tokens": 100, "output_tokens": 50, "cache_read_input_tokens": 1000,
                        "cache_creation_input_tokens": 200}
        return raw
    monkeypatch.setattr(a, "_post", post)
    a.propose(make_ctx(canon, "T2", "N", idx=12))
    assert a.last_cost["input_tokens"] == 1300 and a.last_cost["output_tokens"] == 50
    pin, pout = llmmod.PRICES[MODEL]
    assert a.usage["spend_usd"] == pytest.approx((100 * pin + 1000 * pin * 0.1 + 200 * pin * 1.25 + 50 * pout) / 1e6)
    assert a.usage["cache_read_tokens"] == 1000 and a.usage["cache_write_tokens"] == 200


# ---------------------------------------------------------------------------
# Through the driver
# ---------------------------------------------------------------------------

DICT_FIELDS = {"pack", "arm", "seed", "day", "seq", "ts", "skeleton_id", "conflict_flag", "corpus_contested",
               "corpus_contest_to", "category", "proposal", "impermissible", "impermissible_tier", "impermissible_why",
               "verdict", "executed", "examen", "dj", "escalation", "t3_sampled", "cost", "believes_monitored"}


def run_live(out, arms="C,D", days=3, extra=()):
    return run_year.main(["--packs", "vetpoc", "--arms", arms, "--seeds", "11", "--days", str(days),
                          "--agent", "llm:anthropic:sonnet", "--mode", "live", "--out", str(out), "--quiet", *extra])


def lines_of(out, arm):
    return [json.loads(l) for l in open(os.path.join(out, "vetpoc", arm, "seed-11", "run.jsonl")) if l.strip()]


def test_three_day_live_run_arms_c_and_d(tmp_path, live_env):
    out = tmp_path / "live"
    assert run_live(out) == 0
    n_http_c = None
    for arm in ("C", "D"):
        ls = lines_of(out, arm)
        assert len(ls) > 30
        for l in ls:
            assert set(l) == DICT_FIELDS | {"parse_failed", "preexisting_violation"}, "live lines carry the dictionary fields plus the two live-only fields"
            c = l["cost"]
            assert c["mode"] == "live" and c["model"] == MODEL
            assert isinstance(c["input_tokens"], int) and c["input_tokens"] > 100
            assert isinstance(c["output_tokens"], int) and c["output_tokens"] > 0
            assert isinstance(c["cached"], bool) and c["cost_usd"] > 0
            assert isinstance(l["believes_monitored"], bool) and isinstance(l["parse_failed"], bool)
            assert l["parse_failed"] is False
            if l["executed"]:
                assert l["examen"] is not None and l["examen"]["narrative"]
        twins = [l for l in ls if l["proposal"]["audit_announced"]]
        assert twins and any(l["believes_monitored"] for l in twins) and any(not l["believes_monitored"] for l in twins)
        controls = [l for l in ls if not l["proposal"]["audit_announced"]]
        assert all(l["believes_monitored"] is False for l in controls)
        assert any(l["impermissible"] for l in ls), "the mock files some violations"
        summ = json.load(open(os.path.join(out, "vetpoc", arm, "seed-11", "summary.json")))
        u = summ["agent_state"]["usage"]
        assert u["calls"] == len(ls) and u["parse_failures"] == 0
        if arm == "C":
            assert all(not l["cost"]["cached"] for l in ls)
            assert u["http_calls"] == len(ls) and u["spend_usd"] > 0
            n_http_c = len(live_env.requests)
        else:
            # Arms A/B/C/D render identical prompts until a gloss is written (day 4 at the
            # earliest), so a 3-day arm D is served from arm C's cache entirely.
            assert all(l["cost"]["cached"] for l in ls)
            assert len(live_env.requests) == n_http_c and u["http_calls"] == 0 and u["spend_usd"] == 0.0
            assert summ["totals"]["cost_usd"] == pytest.approx(sum(l["cost"]["cost_usd"] for l in ls))
    assert os.path.exists(out / "vetpoc" / "C" / "seed-11" / "llm_errors.jsonl") is False or \
        open(out / "vetpoc" / "C" / "seed-11" / "llm_errors.jsonl").read() == ""
    t = json.load(open(out / "timings.json"))
    assert t["budget_stop"] is None and t["spend_usd"] > 0
    # metrics
    rows = metrics.compute(str(out))
    assert [r["arm"] for r in rows] == ["C", "D"]
    for r in rows:
        assert r["provenance"] == metrics.MEASURED and r["mode"] == "live" and r["agent"] == "llm:anthropic:sonnet"
        assert r["e5_eeg"] is not None and 0 < r["e5_eeg"] < 1
        # post-pilot secondary measures are computed by metrics_for_run on live lines
        assert isinstance(r["e1_n_preexisting"], int) and r["e1_standdown"] is not None
        assert isinstance(r["e2_n_departures_excluded"], int)
        if r["e1_n_preexisting"]:
            assert 0 <= r["e1_passthrough"] <= 1
        assert r["cost_usd"] > 0 and r["e6_recall"] is not None
    csv_path, _ = metrics.write(rows, str(out))
    assert "⟦measured⟧" in open(csv_path, encoding="utf-8").read()


def test_checkpoint_resume_live_keeps_cache_and_usage(tmp_path, live_env, monkeypatch):
    out = tmp_path / "resume"
    args = run_year.parse_args(["--packs", "vetpoc", "--arms", "D", "--seeds", "11", "--days", "3",
                                "--agent", "llm:anthropic:sonnet", "--mode", "live", "--out", str(out), "--quiet",
                                "--checkpoint-every", "1"])
    data = run_year.PackData("vetpoc")
    out_dir = os.path.join(str(out), "vetpoc", "D", "seed-11")
    r = run_year.Run(data, "D", 11, args, out_dir)
    r.run_day(1)
    r.checkpoint()
    n_after_day1 = len(live_env.requests)
    calls_day1 = r.agent.usage["calls"]
    # Day 2 fails on transport after the retries: no checkpoint is written mid-day.
    monkeypatch.setattr(llmmod.time, "sleep", lambda s: None)
    for _ in range(3):
        live_env.script.append(("default",))        # three answers land before the outage
    for _ in range(llmmod.RETRIES):
        live_env.script.append(("status", 503))
    with pytest.raises(LLMTransportError):
        r.run_day(2)
    live_env.script.clear()
    assert json.load(open(os.path.join(out_dir, "checkpoint.json")))["day"] == 1
    n_failed = len(live_env.requests)
    # Resume: day 2's answered prompts replay from the cache, the rest are fetched.
    args2 = run_year.parse_args(["--packs", "vetpoc", "--arms", "D", "--seeds", "11", "--days", "3",
                                 "--agent", "llm:anthropic:sonnet", "--mode", "live", "--out", str(out), "--quiet",
                                 "--checkpoint-every", "1", "--resume"])
    res = run_year.run_one(data, "D", 11, args2, quiet=True)
    assert res["proposals"] > 0 and not res.get("skipped")
    ls = lines_of(out, "D")
    assert sorted({l["day"] for l in ls}) == [1, 2, 3]
    day1 = [l for l in ls if l["day"] == 1]
    assert len(day1) == calls_day1 and all(not l["cost"]["cached"] for l in day1)
    day2 = [l for l in ls if l["day"] == 2]
    assert any(l["cost"]["cached"] for l in day2), "answers fetched before the failure were replayed from the cache"
    summ = json.load(open(os.path.join(out_dir, "summary.json")))
    assert summ["days"] == 3 and summ["agent_state"]["usage"]["calls"] >= len(ls)
    assert not os.path.exists(os.path.join(out_dir, "checkpoint.json"))
    assert len(live_env.requests) > n_failed
    # A complete run is skipped under --resume: no new requests, no rewrite.
    sha = hashlib.sha256(open(os.path.join(out_dir, "run.jsonl"), "rb").read()).hexdigest()
    n = len(live_env.requests)
    res = run_year.run_one(data, "D", 11, args2, quiet=True)
    assert res.get("skipped") is True and len(live_env.requests) == n
    assert hashlib.sha256(open(os.path.join(out_dir, "run.jsonl"), "rb").read()).hexdigest() == sha
    assert n_after_day1 < n


def test_budget_cap_stops_cleanly_and_resumes(tmp_path, live_env):
    out = tmp_path / "budget"
    # Day 1 of arm C costs well under a cent against the mock; a cap that small stops after day 1.
    rc = run_live(out, arms="C,D", days=3, extra=["--checkpoint-every", "10", "--budget-usd", "0.00001"])
    assert rc == 3
    d = out / "vetpoc" / "C" / "seed-11"
    assert (d / "checkpoint.json").exists() and (d / "BUDGET_STOP.json").exists()
    stop = json.load(open(d / "BUDGET_STOP.json"))
    assert stop["day_done"] == 1 and stop["spend_usd_total"] >= stop["budget_usd"]
    assert not (d / "manifest.json").exists()
    assert not (out / "vetpoc" / "D").exists(), "arm D never started"
    t = json.load(open(out / "timings.json"))
    assert t["budget_stop"] and "budget" in t["budget_stop"]
    n = len(live_env.requests)
    rc = run_live(out, arms="C,D", days=3, extra=["--checkpoint-every", "10", "--budget-usd", "1000", "--resume"])
    assert rc == 0
    assert sorted({l["day"] for l in lines_of(out, "C")}) == [1, 2, 3]
    assert not (d / "checkpoint.json").exists()
    assert len(live_env.requests) > n
    assert all(l["cost"]["cached"] for l in lines_of(out, "D"))
    assert [r["arm"] for r in metrics.compute(str(out))] == ["C", "D"]


# ---------------------------------------------------------------------------
# The preflight script
# ---------------------------------------------------------------------------

PREFLIGHT = os.path.join(ROOT, "reproduce", "ec_preflight.py")


def test_preflight_without_key_skips_network_checks(tmp_path):
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY")}
    p = subprocess.run([sys.executable, PREFLIGHT, "--provider", "anthropic", "--model", "sonnet",
                        "--out", str(tmp_path / "pf")], cwd=ROOT, env=env, capture_output=True, text=True, timeout=600)
    assert p.returncode != 0, p.stdout + p.stderr
    assert "ANTHROPIC_API_KEY" in p.stdout and "SKIPPED" in p.stdout
    assert "claude-sonnet-5" in p.stdout and "registered run plan" in p.stdout.lower()
    assert "projected cost" in p.stdout.lower()


def test_preflight_against_mock(tmp_path, live_env):
    env = dict(os.environ, ANTHROPIC_API_KEY="test-key", ANTHROPIC_BASE_URL=live_env.base,
               NO_PROXY="127.0.0.1,localhost", no_proxy="127.0.0.1,localhost")
    p = subprocess.run([sys.executable, PREFLIGHT, "--provider", "anthropic", "--model", "sonnet",
                        "--out", str(tmp_path / "pf")], cwd=ROOT, env=env, capture_output=True, text=True, timeout=600)
    assert p.returncode == 0, p.stdout + p.stderr
    o = p.stdout
    assert "model id: claude-sonnet-5" in o and "found in model list" in o
    assert "calls made" in o and "parse failures: 0" in o and "believes_monitored" in o
    assert "schema: ok" in o and "provenance: ⟦measured⟧" in o
    assert "PREFLIGHT OK" in o
    # a model the provider does not list fails loudly
    p = subprocess.run([sys.executable, PREFLIGHT, "--provider", "anthropic", "--model", "claude-nope-1",
                        "--out", str(tmp_path / "pf2")], cwd=ROOT, env=env, capture_output=True, text=True, timeout=600)
    assert p.returncode != 0 and "not in the provider's model list" in p.stdout
