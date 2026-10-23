"""
Model clients for every governance seat (governance build v3, §5.1).

`RoleClient` is the transport the coding agent has always used (`agents/llm.py`:
urllib, no SDK, an on-disk cache, retries with backoff, a rate limit and money
accounting), lifted out so that every seat — conscience, offices, auditor, the
judges' ladder, the prosecutor, the clerk, the lawmaker and the L4 proxy — calls
a model the same way. `RoleRegistry` builds one client per role from the JSON
roles config and owns the budget view (`usage_by_role`, `spend_usd`). `Panel`
is the L2 bench: three clients from three families, or one client sampled with
fixed per-seat seeds (the fallback).

Keys come from environment variables only. A client stores the *name* of its
key variable, never the value; errors carry status and body text, never request
headers.

Cache key (non-agent roles):
    sha256(role | level | model | temperature | seed | max_tokens | reasoning-json
           | sample_index | system | user)
The coding agent keeps its legacy key, sha256(model + "\\n" + prompt), so its
existing caches stay valid (`legacy_agent_key=True`).
"""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.request

ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1"
OPENAI_BASE_URL = "https://api.openai.com/v1"
ANTHROPIC_VERSION = "2023-06-01"
CHARS_PER_TOKEN = 4.0
RETRIES = 5
BACKOFF_S = 2.0
BACKOFF_MAX_S = 60.0
TIMEOUT_S = 120
CACHE_READ_MULT = 0.10
CACHE_WRITE_MULT = 1.25
RETRY_STATUS = {408, 409, 429, 500, 502, 503, 504, 529}
PROVIDER_KINDS = ("anthropic", "openai_compatible")
DEFAULT_KEY_ENV = {"anthropic": "ANTHROPIC_API_KEY", "openai_compatible": "OPENAI_API_KEY"}


class LLMTransportError(RuntimeError):
    """The provider could not be reached or kept failing after the retries."""


class ConfigError(ValueError):
    """The roles config is malformed or unsafe."""


def estimate_tokens(text: str) -> int:
    return max(1, int(len(text) / CHARS_PER_TOKEN))


def new_usage() -> dict:
    return {"calls": 0, "cached": 0, "input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0,
            "spend_usd": 0.0, "cache_read_tokens": 0, "cache_write_tokens": 0, "http_calls": 0,
            "retries": 0, "parse_failures": 0, "reasoning_tokens": 0, "failures": 0}


def _strip_fence(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        nl = s.find("\n")
        s = s[nl + 1:] if nl >= 0 else s[3:]
        if s.rstrip().endswith("```"):
            s = s.rstrip()[:-3]
    return s.strip()


def parse_json_object(text):
    """The first JSON object in a reply, or None (a bare object, a fenced block,
    or prose around either)."""
    if not text:
        return None
    s = _strip_fence(str(text))
    try:
        v = json.loads(s)
        return v if isinstance(v, dict) else None
    except Exception:
        pass
    i = s.find("{")
    while i >= 0:
        try:
            v, _end = json.JSONDecoder().raw_decode(s, i)
            if isinstance(v, dict):
                return v
        except Exception:
            pass
        i = s.find("{", i + 1)
    return None


class RoleClient:
    """One role's model: transport, cache, retries, rate limit and accounting.

    `mode` is "dry" (no network: the caller accounts an estimate with
    `account_dry` and answers with its stand-in) or "live"."""

    def __init__(self, role: str, *, kind: str = "anthropic", model: str = "", base_url: str | None = None,
                 api_key_env: str | None = None, api_key: str | None = None, temperature=0.0,
                 max_tokens: int = 400, reasoning: dict | None = None, seed=None, stance: str | None = None,
                 mode: str = "dry", cache_dir: str | None = None, log_path: str | None = None,
                 rate_limit_s: float = 0.0, prompt_cache: bool = True, legacy_agent_key: bool = False,
                 price: tuple | None = None, price_source: str = "", reasoning_billed_separately: bool = False,
                 provider: str | None = None, usage: dict | None = None):
        if kind not in PROVIDER_KINDS:
            raise ConfigError(f"role {role}: unknown provider kind {kind!r}")
        if mode not in ("dry", "live"):
            raise ConfigError(f"role {role}: unknown mode {mode!r}")
        self.role = role
        self.kind = kind
        self.provider = provider or kind
        self.model = model
        self.base_url = base_url or (os.environ.get("ANTHROPIC_BASE_URL", ANTHROPIC_BASE_URL) if kind == "anthropic"
                                     else os.environ.get("OPENAI_BASE_URL", OPENAI_BASE_URL))
        self.api_key_env = api_key_env or DEFAULT_KEY_ENV[kind]
        self._api_key = api_key          # tests and the legacy agent constructor only; never serialised
        self.temperature = temperature
        self.max_tokens = int(max_tokens)
        self.reasoning = dict(reasoning or {})
        self.seed = seed
        self.stance = stance
        self.mode = mode
        self.cache_dir = cache_dir or os.path.join("simulation", "ec", "results", "llm_cache")
        self.log_path = log_path
        self.rate_limit_s = float(rate_limit_s or 0.0)
        self.prompt_cache = bool(prompt_cache)
        self.legacy_agent_key = bool(legacy_agent_key)
        self.price = tuple(price) if price else (0.0, 0.0)
        self.price_source = price_source
        self.reasoning_billed_separately = bool(reasoning_billed_separately)
        self.usage = usage if usage is not None else new_usage()
        self.last_spend = 0.0
        self.last_cost: dict | None = None
        self.last_raw_usage: dict | None = None
        self.temperature_sent = None
        self._last_http_t = 0.0
        self.post_fn = self._post        # the legacy agent routes this through its own `_post` (tests patch it)

    # -- description (manifest) --------------------------------------------
    def describe(self) -> dict:
        return {"role": self.role, "provider": self.provider, "kind": self.kind, "model": self.model,
                "temperature": self.temperature, "seed": self.seed, "max_tokens": self.max_tokens,
                "reasoning": self.reasoning or None, "stance": self.stance,
                "price_per_mtok": list(self.price), "price_source": self.price_source,
                "api_key_env": self.api_key_env}

    # -- keys --------------------------------------------------------------
    def key(self) -> str | None:
        if self._api_key:
            return self._api_key
        return os.environ.get(self.api_key_env)

    def has_key(self) -> bool:
        return bool(self.key())

    # -- logging -----------------------------------------------------------
    def _log(self, event: str, **kw) -> None:
        if not self.log_path:
            return
        rec = {"t": round(time.time(), 3), "event": event, "model": self.model, **kw}
        if not self.legacy_agent_key:
            rec["role"] = self.role
        try:
            os.makedirs(os.path.dirname(self.log_path) or ".", exist_ok=True)
            with open(self.log_path, "a") as fh:
                fh.write(json.dumps(rec, sort_keys=True) + "\n")
        except OSError:
            pass

    # -- transport ---------------------------------------------------------
    @staticmethod
    def _retry_after(e: urllib.error.HTTPError, attempt: int) -> float:
        ra = e.headers.get("retry-after") if e.headers is not None else None
        try:
            if ra is not None:
                return min(BACKOFF_MAX_S, max(0.0, float(ra)))
        except ValueError:
            pass
        return min(BACKOFF_MAX_S, BACKOFF_S * (2 ** attempt))

    def _post(self, url: str, headers: dict, body: dict) -> dict:
        data = json.dumps(body).encode("utf-8")
        last = None
        for attempt in range(RETRIES):
            if attempt:
                self.usage["retries"] += 1
            if self.rate_limit_s > 0:
                wait = self.rate_limit_s - (time.time() - self._last_http_t)
                if wait > 0:
                    time.sleep(wait)
            req = urllib.request.Request(url, data=data, headers={"content-type": "application/json", **headers},
                                         method="POST")
            self._last_http_t = time.time()
            self.usage["http_calls"] += 1
            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                try:
                    detail = e.read().decode("utf-8", "replace")[:500]
                except Exception:
                    detail = ""
                last = f"HTTP {e.code}: {detail}"
                self._log("http_error", status=e.code, attempt=attempt, detail=detail, url=url)
                if e.code not in RETRY_STATUS:
                    raise LLMTransportError(f"model call refused ({last}); not retried") from e
                delay = self._retry_after(e, attempt)
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
                last = f"{type(e).__name__}: {e}"
                self._log("transport_error", attempt=attempt, detail=str(e)[:500], url=url)
                delay = min(BACKOFF_MAX_S, BACKOFF_S * (2 ** attempt))
            if attempt + 1 < RETRIES:
                time.sleep(delay)
        self._log("gave_up", attempts=RETRIES, detail=str(last)[:500], url=url)
        raise LLMTransportError(f"model call failed after {RETRIES} attempts: {last}")

    def _get(self, url: str, headers: dict) -> dict:
        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise LLMTransportError(f"model list refused (HTTP {e.code})") from e
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            raise LLMTransportError(f"model list failed: {type(e).__name__}") from e

    def _auth_headers(self) -> dict:
        if self.kind == "anthropic":
            return {"x-api-key": self.key() or "", "anthropic-version": ANTHROPIC_VERSION}
        return {"authorization": f"Bearer {self.key() or ''}"}

    def list_models(self) -> list:
        """Model ids the provider lists (for the dry-run confirmation, §4.2)."""
        raw = self._get(self.base_url.rstrip("/") + "/models", self._auth_headers())
        data = raw.get("data") if isinstance(raw, dict) else raw
        out = []
        for m in data or []:
            if isinstance(m, dict) and m.get("id"):
                out.append(str(m["id"]))
        return sorted(out)

    def body(self, system: str, user: str, seed=None) -> dict:
        """The request body this role sends. The legacy agent body is exactly the
        agent's historical one (temperature 0, its max_tokens, system with
        cache_control for Anthropic)."""
        seed = self.seed if seed is None else seed
        if self.kind == "anthropic":
            b = {"model": self.model, "max_tokens": self.max_tokens}
            budget = (self.reasoning or {}).get("anthropic_thinking_budget")
            if budget:
                if self.max_tokens <= int(budget):
                    raise ConfigError(f"role {self.role}: max_tokens must exceed the thinking budget")
                b["thinking"] = {"type": "enabled", "budget_tokens": int(budget)}
                self.temperature_sent = None          # the provider fixes the temperature with thinking
            elif self.temperature is not None:
                b["temperature"] = self.temperature
                self.temperature_sent = self.temperature
            b["messages"] = [{"role": "user", "content": [{"type": "text", "text": user}]}]
            if system:
                blk = {"type": "text", "text": system}
                if self.prompt_cache:
                    blk["cache_control"] = {"type": "ephemeral"}
                b["system"] = [blk]
            return b
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": user})
        b = {"model": self.model, "max_tokens": self.max_tokens}
        if self.temperature is not None:
            b["temperature"] = self.temperature
        self.temperature_sent = self.temperature
        b["messages"] = msgs
        if seed is not None:
            b["seed"] = int(seed)
        extra = (self.reasoning or {}).get("extra_body")
        if isinstance(extra, dict):
            b.update(extra)
        return b

    def _request(self, system: str, user: str, seed=None) -> tuple:
        """(text, usage, stop_reason, raw_usage) from one provider call."""
        body = self.body(system, user, seed)
        if self.kind == "anthropic":
            raw = self.post_fn(self.base_url.rstrip("/") + "/messages", self._auth_headers(), body)
            content = raw.get("content") or []
            text = "".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
            u = raw.get("usage") or {}
            usage = {"input_tokens": int(u.get("input_tokens", 0) or 0),
                     "output_tokens": int(u.get("output_tokens", 0) or 0),
                     "cache_read_tokens": int(u.get("cache_read_input_tokens", 0) or 0),
                     "cache_write_tokens": int(u.get("cache_creation_input_tokens", 0) or 0),
                     "reasoning_tokens": 0,
                     "reported": "input_tokens" in u}
            return text, usage, raw.get("stop_reason"), u
        raw = self.post_fn(self.base_url.rstrip("/") + "/chat/completions", self._auth_headers(), body)
        choice = (raw.get("choices") or [{}])[0] or {}
        msg = choice.get("message") or {}
        text = msg.get("content") or ""
        if isinstance(text, list):
            text = "".join(p.get("text", "") for p in text if isinstance(p, dict))
        u = raw.get("usage") or {}
        det = u.get("prompt_tokens_details") or {}
        cached = int(det.get("cached_tokens", 0) or 0)
        rdet = u.get("completion_tokens_details") or {}
        reasoning = int(rdet.get("reasoning_tokens", 0) or 0) if self.reasoning_billed_separately else 0
        usage = {"input_tokens": max(0, int(u.get("prompt_tokens", 0) or 0) - cached),
                 "output_tokens": int(u.get("completion_tokens", 0) or 0) + reasoning,
                 "cache_read_tokens": cached, "cache_write_tokens": 0, "reasoning_tokens": reasoning,
                 "reported": "prompt_tokens" in u}
        return text, usage, choice.get("finish_reason"), u

    # -- cache -------------------------------------------------------------
    def cache_path(self, system: str, user: str, *, level=None, sample_index: int = 0, seed=None,
                   legacy_prompt: str | None = None) -> str:
        if self.legacy_agent_key:
            prompt = legacy_prompt if legacy_prompt is not None else ((system + "\n\n" + user) if system else user)
            h = hashlib.sha256((self.model + "\n" + prompt).encode("utf-8")).hexdigest()
        else:
            seed = self.seed if seed is None else seed
            parts = [self.role, "" if level is None else str(level), self.model, json.dumps(self.temperature),
                     json.dumps(seed), str(self.max_tokens), json.dumps(self.reasoning or {}, sort_keys=True),
                     str(int(sample_index)), system, user]
            h = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()
        return os.path.join(self.cache_dir, h[:2], h + ".json")

    # -- calls -------------------------------------------------------------
    def call(self, system: str, user: str, *, level=None, sample_index: int = 0, seed=None,
             legacy_prompt: str | None = None) -> tuple:
        """(text, input_tokens, output_tokens, cached). Live mode only."""
        if self.mode != "live":
            raise RuntimeError(f"role {self.role}: call() in dry mode; use account_dry")
        path = self.cache_path(system, user, level=level, sample_index=sample_index, seed=seed,
                               legacy_prompt=legacy_prompt)
        if os.path.exists(path):
            try:
                with open(path) as fh:
                    c = json.load(fh)
                self.last_spend = 0.0
                self.last_raw_usage = c.get("raw_usage")
                return c["text"], int(c["input_tokens"]), int(c["output_tokens"]), True
            except (OSError, ValueError, KeyError) as e:
                self._log("cache_corrupt", path=path if self.legacy_agent_key else os.path.basename(path),
                          detail=str(e)[:200])
        text, u, stop, raw_u = self._request(system, user, seed)
        if not u["reported"]:
            prompt = (system + "\n\n" + user) if system else user
            u["input_tokens"], u["output_tokens"] = estimate_tokens(prompt), estimate_tokens(text)
            self._log("usage_missing", detail="provider reported no usage; chars/4 estimate used")
        tin = u["input_tokens"] + u["cache_read_tokens"] + u["cache_write_tokens"]
        tout = u["output_tokens"]
        pin, pout = self.price
        self.last_spend = (u["input_tokens"] * pin + u["cache_read_tokens"] * pin * CACHE_READ_MULT
                           + u["cache_write_tokens"] * pin * CACHE_WRITE_MULT + tout * pout) / 1e6
        self.usage["cache_read_tokens"] += u["cache_read_tokens"]
        self.usage["cache_write_tokens"] += u["cache_write_tokens"]
        if not self.legacy_agent_key:
            self.usage["reasoning_tokens"] = self.usage.get("reasoning_tokens", 0) + u.get("reasoning_tokens", 0)
        self.last_raw_usage = raw_u
        if stop in ("max_tokens", "length"):
            self._log("truncated", stop_reason=stop, output_tokens=tout, text=(text or "")[:300])
        if not text:
            self._log("empty_reply", stop_reason=stop)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        rec = {"model": self.model, "text": text, "input_tokens": tin, "output_tokens": tout,
               "stop_reason": stop, "usage": {k: v for k, v in u.items() if k not in ("reported", "reasoning_tokens")}}
        if not self.legacy_agent_key:
            rec["role"] = self.role
            rec["raw_usage"] = raw_u
            rec["temperature_sent"] = self.temperature_sent
        with open(tmp, "w") as fh:
            json.dump(rec, fh)
        os.replace(tmp, path)
        return text, tin, tout, False

    def account(self, tin: int, tout: int, cached: bool) -> dict:
        """Book one call (live or dry) and return the cost line."""
        pin, pout = self.price
        cost = (tin * pin + tout * pout) / 1e6 * (0.1 if cached else 1.0)
        self.usage["calls"] += 1
        self.usage["cached"] += int(cached)
        self.usage["input_tokens"] += tin
        self.usage["output_tokens"] += tout
        self.usage["cost_usd"] += cost
        if self.mode == "live":
            self.usage["spend_usd"] += 0.0 if cached else float(self.last_spend)
        self.last_cost = {"cost_usd": cost, "input_tokens": tin, "output_tokens": tout, "cached": cached,
                          "model": self.model, "mode": self.mode}
        return self.last_cost

    def account_dry(self, system: str, user: str, out_tokens: int) -> dict:
        tin = estimate_tokens((system + "\n\n" + user) if system else user)
        return self.account(tin, int(out_tokens), False)

    def call_json(self, system: str, user: str, *, validate=None, level=None, sample_index: int = 0,
                  seed=None) -> tuple:
        """(parsed dict or None, meta). One repair retry when the reply does not
        parse or `validate(parsed)` returns an error string. Live mode only."""
        meta = {"repaired": False, "error": None, "cost": []}
        text, tin, tout, cached = self.call(system, user, level=level, sample_index=sample_index, seed=seed)
        meta["cost"].append(self.account(tin, tout, cached))
        meta["text"] = text
        parsed = parse_json_object(text)
        err = None if isinstance(parsed, dict) else "reply was not one JSON object"
        if err is None and validate is not None:
            err = validate(parsed)
        if err is None:
            return parsed, meta
        self._log("repair", detail=str(err)[:300], level=level)
        repair = (user + "\n\nYOUR PREVIOUS REPLY WAS REJECTED: " + str(err)
                  + "\nReply again with one JSON object in the required format and nothing else.")
        text2, tin2, tout2, cached2 = self.call(system, repair, level=level, sample_index=sample_index, seed=seed)
        meta["cost"].append(self.account(tin2, tout2, cached2))
        meta["repaired"] = True
        parsed2 = parse_json_object(text2)
        err2 = None if isinstance(parsed2, dict) else "reply was not one JSON object"
        if err2 is None and validate is not None:
            err2 = validate(parsed2)
        if err2 is None:
            return parsed2, meta
        self.usage["parse_failures"] = self.usage.get("parse_failures", 0) + 1
        meta["error"] = str(err2)
        self._log("parse_failure", detail=str(err2)[:300], text=(text2 or "")[:500], level=level)
        return None, meta

    # -- state -------------------------------------------------------------
    def state(self) -> dict:
        return {"usage": dict(self.usage)}

    def restore(self, d: dict) -> None:
        self.usage.update((d or {}).get("usage") or {})


class Panel:
    """The L2 bench (§3.4, R3): `seats` clients, one opinion each. A mixed panel
    is three clients of three families at temperature 0; the fallback is one
    client sampled at temperature 0.7 with a fixed seed per seat."""

    def __init__(self, seats: list, seeds: list | None = None, fallback: bool = False):
        self.seats = list(seats)
        self.seeds = list(seeds or [None] * len(self.seats))
        self.fallback = bool(fallback)

    def __len__(self) -> int:
        return len(self.seats)

    def seat(self, i: int) -> tuple:
        """(client, seed, stance) for seat i."""
        return self.seats[i], self.seeds[i], self.seats[i].stance

    def describe(self) -> dict:
        return {"fallback": self.fallback,
                "seats": [dict(c.describe(), seed=s) for c, s in zip(self.seats, self.seeds)]}


ROLES = ("agent", "ec", "office", "auditor", "dj_l1", "dj_l2", "dj_l3", "prosecutor", "clerk", "lawmaker", "l4_proxy")
STANCES = ("textualist", "purposive", "risk_weighted")


def _find_literal_keys(obj, path="") -> list:
    """Paths of any `api_key` field (a literal key in the config is fatal)."""
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else str(k)
            if str(k).lower() == "api_key":
                out.append(p)
            out += _find_literal_keys(v, p)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out += _find_literal_keys(v, f"{path}[{i}]")
    return out


def load_roles_config(path: str) -> dict:
    with open(path) as fh:
        cfg = json.load(fh)
    lit = _find_literal_keys(cfg)
    if lit:
        raise ConfigError("the roles config must not carry a literal api_key (found at "
                          + ", ".join(lit) + "); name an environment variable in api_key_env")
    if not isinstance(cfg.get("providers"), dict) or not isinstance(cfg.get("roles"), dict):
        raise ConfigError("the roles config needs 'providers' and 'roles' objects")
    for name, p in cfg["providers"].items():
        if p.get("kind") not in PROVIDER_KINDS:
            raise ConfigError(f"provider {name}: kind must be one of {PROVIDER_KINDS}")
        if not p.get("api_key_env"):
            raise ConfigError(f"provider {name}: api_key_env is required")
    for model, pr in (cfg.get("prices") or {}).items():
        if not pr.get("source"):
            raise ConfigError(f"price for {model}: a 'source' is required")
    return cfg


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def load_keys_file(path: str, repo_root: str) -> list:
    """Load KEY=value lines into the environment (names only are returned).
    Refused inside the repository and unless the file is private (mode 600)."""
    ap = os.path.realpath(path)
    root = os.path.realpath(repo_root)
    if ap == root or ap.startswith(root + os.sep):
        raise ConfigError("--keys-file must live outside the repository")
    st = os.stat(ap)
    if st.st_mode & 0o077:
        raise ConfigError("--keys-file must be private (chmod 600)")
    names = []
    with open(ap) as fh:
        for line in fh:
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, v = s.split("=", 1)
            k = k.strip()
            if k.startswith("export "):
                k = k[len("export "):].strip()
            if k and v.strip():
                os.environ[k] = v.strip().strip('"').strip("'")
                names.append(k)
    return names


class RoleRegistry:
    """One client per role, built from the roles config."""

    def __init__(self, cfg: dict, *, mode: str, cache_dir: str, log_path: str | None = None,
                 rate_limit_s: float = 0.0, anthropic_prices: dict | None = None, roles=None):
        self.cfg = cfg
        self.mode = mode
        self.clients: dict = {}
        self.panel: Panel | None = None
        prices = {m: (float(p["input"]), float(p["output"]), p.get("source", ""))
                  for m, p in (cfg.get("prices") or {}).items()}
        for m, (pin, pout) in (anthropic_prices or {}).items():
            prices.setdefault(m, (pin, pout, "PRICES in simulation/ec/agents/llm.py"))
        self._prices = prices
        wanted = set(roles) if roles is not None else None
        for role, spec in cfg["roles"].items():
            if role not in ROLES:
                raise ConfigError(f"unknown role {role!r}; known {ROLES}")
            if role == "agent" or (wanted is not None and role not in wanted):
                continue
            if role == "dj_l2" and isinstance(spec, dict) and "panel" in spec:
                seats = [self._client(f"dj_l2#{i + 1}", s, cache_dir, log_path, rate_limit_s)
                         for i, s in enumerate(spec["panel"])]
                self.clients["dj_l2"] = seats[0]
                self.panel = Panel(seats)
                fb = spec.get("fallback")
                self._fallback_spec = fb
                continue
            self.clients[role] = self._client(role, spec, cache_dir, log_path, rate_limit_s)

    def _client(self, role, spec, cache_dir, log_path, rate_limit_s) -> RoleClient:
        prov = self.cfg["providers"].get(spec.get("provider"))
        if prov is None:
            raise ConfigError(f"role {role}: unknown provider {spec.get('provider')!r}")
        model = spec.get("model") or ""
        pr = self._prices.get(model)
        if self.mode == "live" and pr is None:
            raise ConfigError(f"role {role}: model {model!r} has no price (add it to 'prices' with a source)")
        return RoleClient(role, kind=prov["kind"], provider=spec.get("provider"), model=model,
                          base_url=prov.get("base_url"), api_key_env=prov["api_key_env"],
                          temperature=spec.get("temperature", 0) if "reasoning" not in spec or
                          not (spec.get("reasoning") or {}).get("anthropic_thinking_budget") else None,
                          max_tokens=int(spec.get("max_tokens", 1000)), reasoning=spec.get("reasoning"),
                          seed=spec.get("seed"), stance=spec.get("stance"), mode=self.mode, cache_dir=cache_dir,
                          log_path=log_path, rate_limit_s=rate_limit_s,
                          price=(pr[0], pr[1]) if pr else None, price_source=pr[2] if pr else "",
                          reasoning_billed_separately=bool(prov.get("reasoning_billed_separately", False)))

    def use_fallback_panel(self, cache_dir: str, log_path: str | None = None, rate_limit_s: float = 0.0) -> Panel:
        """One family only: one client at temperature 0.7, a fixed seed per seat."""
        fb = getattr(self, "_fallback_spec", None)
        if not fb:
            raise ConfigError("dj_l2 has no fallback")
        seats, seeds = [], list(fb.get("seeds") or [11, 12, 13])
        for i, stance in enumerate(STANCES):
            spec = dict(fb, stance=stance, seed=seeds[i])
            seats.append(self._client(f"dj_l2#{i + 1}", spec, cache_dir, log_path, rate_limit_s))
        self.panel = Panel(seats, seeds=seeds, fallback=True)
        self.clients["dj_l2"] = seats[0]
        return self.panel

    def client(self, role: str) -> RoleClient | None:
        return self.clients.get(role)

    def all_clients(self) -> list:
        out = [c for r, c in sorted(self.clients.items()) if r != "dj_l2"]
        if self.panel is not None:
            out += self.panel.seats
        return out

    def missing_keys(self) -> list:
        """Names of key variables that are unset (never their values)."""
        return sorted({c.api_key_env for c in self.all_clients() if not c.has_key()})

    def usage_by_role(self) -> dict:
        return {c.role: dict(c.usage) for c in self.all_clients()}

    def spend_usd(self) -> float:
        return float(sum(c.usage.get("spend_usd", 0.0) for c in self.all_clients()))

    def cost_usd(self) -> float:
        return float(sum(c.usage.get("cost_usd", 0.0) for c in self.all_clients()))

    def describe(self) -> dict:
        d = {r: c.describe() for r, c in sorted(self.clients.items()) if r != "dj_l2"}
        if self.panel is not None:
            d["dj_l2"] = self.panel.describe()
        return d

    def state(self) -> dict:
        return {c.role: c.state() for c in self.all_clients()}

    def restore(self, st: dict) -> None:
        for c in self.all_clients():
            c.restore((st or {}).get(c.role) or {})
