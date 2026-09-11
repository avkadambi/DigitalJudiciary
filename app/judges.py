"""The model-facing positions of the architecture.

There are two, and it is worth being exact about which, because the paper's
claim rests on how few there are:

  distinguish(candidate, case)   does this precedent's holding rest on
                                 something the present case lacks?
  propose_premise(case, ...)     which of these facts was the holding
                                 MATERIAL to? (opt-in; see below)

similar() is NOT one of them. It is deterministic Jaccard in every mode:
retrieval must be snapshot-deterministic for CC-16, and the paper treats the
retrieval metric as replaceable infrastructure rather than judgment. The
decision itself is never asked of a model — it is either mirrored from the
controlling precedent or produced by rule_eval().

Two implementations, selected by DJ_JUDGE_MODE:

  oracle (default) — the paper's deterministic reference oracles (§11.5):
    similar    = Jaccard factor overlap, theta = 0.25
    distinguish= premise-subset test: a candidate is distinguished exactly
                 when some element of its recorded premise is absent from
                 the present case's facts.
    Bit-for-bit reproducible; this is the Phase-1 conformance posture, and
    the only mode the conformance harness certifies.

  llm — distinguish is delegated to an external AI service (the container's
    ONLY external dependency). The prompt asks the paper's question verbatim
    and demands a strict JSON verdict. Failure follows §12: the candidate is
    treated as NOT distinguished (conservative — it stays in the pool), the
    verdict is marked degraded, and pivotal degraded verdicts escalate.

**Per-tier judges.** A judge is built per tier, so escalation can put a
different model (or a wider quorum) at each rung. Without this the ladder is
a relabeling: the same model answering the same question gives the same
answer, and a challenge changes nothing but the name on the record.

**propose_premise** is opt-in via DJ_PREMISE_MODE=judged and is the one
position where a model contributes durable content. When a case is decided
without a controlling precedent, the mechanical fallback records the premise
as ALL of the case's facts, which is a maximally broad holding and therefore
maximally easy to distinguish later. Asking which facts were material is the
question a judge actually answers when writing an opinion. The Gate
constrains the answer to a subset of the case's own facts, so a model cannot
invent a premise, only narrow one.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

THETA = float(os.environ.get("DJ_THETA", "0.25"))
# Hard cap on candidates returned by retrieve(). Keeps the distinguish
# stage bounded even if a provision accumulates a large active store.
# Override with DJ_MAX_CANDIDATES; values below 1 are clamped to 1.
MAX_CANDIDATES = max(1, int(os.environ.get("DJ_MAX_CANDIDATES", "25")))

PROMPT_TEMPLATE = (
    "You are the distinguishing gate of a precedent system for CI/CD "
    "compliance.\n"
    "A stored precedent's holding rested on the following premise "
    "(facts that were material to its holding):\n"
    "  premise: {premise}\n"
    "The present case has these facts:\n"
    "  facts: {facts}\n"
    "Question (answer exactly this): does the precedent's holding rest on "
    "something the present case lacks? If yes, the precedent is "
    "distinguished and must not control.\n"
    "Respond with ONLY a JSON object, no prose, no markdown fences:\n"
    '{{"distinguished": true|false, "grounds": "<one sentence>"}}'
)
PROMPT_VERSION = "distinguish-v1"

PREMISE_TEMPLATE = (
    "You are recording the holding of a precedent in a CI/CD compliance "
    "system.\n"
    "A case with these facts was decided '{outcome}' under provision "
    "{provision}:\n"
    "  facts: {facts}\n"
    "  reasoning: {reason}\n"
    "Question: which of those facts was the decision MATERIAL to — that is, "
    "which facts, had they been absent, would have changed the outcome? "
    "Future cases will be distinguished from this one exactly when they lack "
    "a fact you list here, so listing everything makes the holding "
    "worthless, and listing too little makes it overreach.\n"
    "Choose only from the facts given. Respond with ONLY a JSON object, no "
    "prose, no markdown fences:\n"
    '{{"premise": ["<fact>"], "grounds": "<one sentence>"}}'
)
PREMISE_VERSION = "premise-v1"


def model_for_tier(tier: int) -> str:
    """Per-tier model from config file or env."""
    try:
        from .platform.dj_config import get_config
        return get_config().model_for_tier(tier)
    except Exception:
        return (os.environ.get(f"DJ_JUDGE_MODEL_T{tier}")
                or os.environ.get("DJ_JUDGE_MODEL", "claude-sonnet-4-6"))


def provider_for_tier(tier: int) -> str:
    try:
        from .platform.dj_config import get_config
        return get_config().provider_for_tier(tier)
    except Exception:
        return os.environ.get(f"DJ_JUDGE_PROVIDER_T{tier}", "anthropic")


def api_key_for_tier(tier: int) -> str:
    try:
        from .platform.dj_config import get_config
        return get_config().api_key_for_tier(tier)
    except Exception:
        return (os.environ.get(f"DJ_JUDGE_KEY_T{tier}")
                or os.environ.get("ANTHROPIC_API_KEY")
                or os.environ.get("OPENAI_API_KEY")
                or "")


def quorum_width(tier: int) -> int:
    """How many samples a pivotal verdict costs at this tier."""
    try:
        from .platform.dj_config import get_config
        cfg = get_config()
        if tier in cfg.tiers:
            return cfg.quorum_for_tier(tier)
    except Exception:
        pass
    raw = (os.environ.get(f"DJ_QUORUM_T{tier}")
           or os.environ.get("DJ_QUORUM", "3"))
    try:
        return max(1, int(raw))
    except ValueError:
        return 3


def judge_concurrency() -> int:
    """How many distinguishing questions to ask at once.

    1 disables it. The default is deliberately modest: these are independent
    questions and could all go at once, but a concurrency that earns 429s is
    slower than sequential, and the oracle gains nothing from threads.
    """
    if os.environ.get("DJ_JUDGE_MODE", "oracle") != "llm":
        return 1
    try:
        return max(1, int(os.environ.get("DJ_JUDGE_CONCURRENCY", "6")))
    except ValueError:
        return 6


def premise_mode() -> str:
    return os.environ.get("DJ_PREMISE_MODE", "mechanical")


class OracleJudge:
    """The paper's deterministic premise-subset oracle. Cannot be wrong
    about its own definition, and therefore proves nothing about model
    quality — exactly as §11.5 of the paper intends."""

    version = "oracle-premise-subset-1.0"
    prompt_version = "n/a"
    params = {"theta": THETA, "kind": "premise_subset"}

    def distinguish(self, candidate: dict, case: dict):
        premise = set(candidate["premise"])
        facts = set(case["facts"])
        missing = sorted(premise - facts)
        verdict = {
            "distinguished": bool(missing),
            "grounds": (f"holding rested on {missing}, absent here"
                        if missing else
                        "premise fully contained in the present facts"),
        }
        return verdict, 0, False        # verdict, latency_ms, degraded

    def propose_premise(self, case: dict, outcome: str, provision: str,
                        reason: str):
        """The mechanical rule: the holding rested on everything true.

        Deliberately unchanged as the default, because it is what the
        conformance corpus was computed against. It is also the weakest part
        of the record, which is why DJ_PREMISE_MODE=judged exists.
        """
        return (sorted(case["facts"]), "mechanical: all case facts", 0, False)


class LLMJudge:
    """distinguish() via the Anthropic Messages API — the container's only
    external call. Timeout and parse failures degrade per §12."""

    def __init__(self, tier: int = 0):
        self.tier = tier
        self.model = model_for_tier(tier) if tier else os.environ.get(
            "DJ_JUDGE_MODEL", "claude-sonnet-4-6")
        self.provider = provider_for_tier(tier) if tier else "anthropic"
        self.version = f"llm:{self.provider}:{self.model}"
        self.prompt_version = PROMPT_VERSION
        self.params = {"theta": THETA, "temperature": 0, "max_tokens": 200,
                       "tier": tier, "quorum": quorum_width(tier),
                       "provider": self.provider}
        self.api_key = api_key_for_tier(tier) if tier else (
            os.environ.get("ANTHROPIC_API_KEY")
            or os.environ.get("OPENAI_API_KEY")
            or "")
        self.timeout = float(os.environ.get("DJ_JUDGE_TIMEOUT_S", "20"))
        self.last_usage = (None, None)   # set per call, read by provenance

    def distinguish(self, candidate: dict, case: dict):
        prompt = PROMPT_TEMPLATE.format(
            premise=json.dumps(sorted(candidate["premise"])),
            facts=json.dumps(sorted(case["facts"])))
        t0 = time.monotonic()
        try:
            verdict = self._call(prompt, 200)
            assert isinstance(verdict.get("distinguished"), bool)
            verdict.setdefault("grounds", "")
            return verdict, int((time.monotonic() - t0) * 1000), False
        except (urllib.error.URLError, TimeoutError, ValueError,
                AssertionError, KeyError, RuntimeError) as e:
            return ({"distinguished": False,
                     "grounds": f"DEGRADED: judge unavailable ({e})"},
                    int((time.monotonic() - t0) * 1000), True)

    def _call(self, prompt: str, max_tokens: int):
        """Provider-aware chat completion (Anthropic Messages or OpenAI)."""
        if not self.api_key:
            raise RuntimeError("no API key configured for this tier")
        provider = (self.provider or "anthropic").lower()
        if provider in ("openai", "openai_compatible"):
            return self._call_openai(prompt, max_tokens)
        return self._call_anthropic(prompt, max_tokens)

    def _call_anthropic(self, prompt: str, max_tokens: int):
        body = json.dumps({
            "model": self.model, "max_tokens": max_tokens, "temperature": 0,
            "messages": [{"role": "user", "content": prompt}],
        }).encode()
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages", data=body,
            headers={"content-type": "application/json",
                     "x-api-key": self.api_key,
                     "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            data = json.loads(resp.read())
        text = "".join(b.get("text", "") for b in data.get("content", [])
                       if b.get("type") == "text").strip()
        if text.startswith("```"):
            text = text.strip("`").removeprefix("json").strip()
        u = data.get("usage") or {}
        self.last_usage = (u.get("input_tokens"), u.get("output_tokens"))
        return json.loads(text)

    def _call_openai(self, prompt: str, max_tokens: int):
        base = os.environ.get("DJ_OPENAI_BASE", "https://api.openai.com/v1")
        body = json.dumps({
            "model": self.model, "max_tokens": max_tokens, "temperature": 0,
            "messages": [{"role": "user", "content": prompt}],
        }).encode()
        req = urllib.request.Request(
            f"{base.rstrip('/')}/chat/completions", data=body,
            headers={"content-type": "application/json",
                     "authorization": f"Bearer {self.api_key}"})
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            data = json.loads(resp.read())
        text = (data.get("choices") or [{}])[0].get("message", {}).get(
            "content", "").strip()
        if text.startswith("```"):
            text = text.strip("`").removeprefix("json").strip()
        u = data.get("usage") or {}
        self.last_usage = (u.get("prompt_tokens"), u.get("completion_tokens"))
        return json.loads(text)

    def propose_premise(self, case: dict, outcome: str, provision: str,
                        reason: str):
        """Ask which facts were material. The answer is advisory: the Gate
        intersects it with the case's own facts, and any failure falls back
        to the mechanical premise marked degraded rather than guessing."""
        facts = sorted(case["facts"])
        prompt = PREMISE_TEMPLATE.format(
            outcome=outcome, provision=provision, reason=reason,
            facts=json.dumps(facts))
        t0 = time.monotonic()
        try:
            out = self._call(prompt, 300)
            proposed = [f for f in out.get("premise", []) if f in facts]
            if not proposed:
                raise ValueError("empty or out-of-vocabulary premise")
            return (sorted(set(proposed)), out.get("grounds", ""),
                    int((time.monotonic() - t0) * 1000), False)
        except (urllib.error.URLError, TimeoutError, ValueError,
                AssertionError, KeyError) as e:
            return (facts, f"DEGRADED: premise judge unavailable ({e})",
                    int((time.monotonic() - t0) * 1000), True)


def make_judge(tier: int = 0):
    mode = os.environ.get("DJ_JUDGE_MODE", "oracle")
    if mode == "llm":
        key = api_key_for_tier(tier) if tier else (
            os.environ.get("ANTHROPIC_API_KEY")
            or os.environ.get("OPENAI_API_KEY") or "")
        if not key:
            raise RuntimeError(
                "DJ_JUDGE_MODE=llm requires a per-tier key "
                "(DJ_JUDGE_KEY_T{n} / config api_key_env) or ANTHROPIC_API_KEY")
        return LLMJudge(tier)
    return OracleJudge()


def make_judges(k: int = 4) -> dict:
    """One judge per tier. In oracle mode they are the same object, which is
    correct: a deterministic oracle cannot deliberate harder. In llm mode each
    tier gets its own model, so DJ_JUDGE_MODEL_T1=haiku, _T2=sonnet,
    _T3=opus reproduces the paper's escalation ladder inside the container
    rather than in a benchmark harness bolted alongside it."""
    if os.environ.get("DJ_JUDGE_MODE", "oracle") != "llm":
        shared = OracleJudge()
        return {t: shared for t in range(1, k + 1)}
    return {t: make_judge(t) for t in range(1, k + 1)}
