"""
Governance seats: modes, presets, prompts and the dry stand-ins (governance build v3).

Every decision and evaluation in the workflow has a seat. A seat runs in one
of three modes:

    deterministic  today's code; the default; byte-identical to today
    llm            the model decides and its decision binds
    shadow         the answer key decides; the model decides the same question
                   on the same state and is only logged

Seats (§3.2): conscience (`--ec`), offices (`--office`), auditor (`--auditor`),
the judges' ladder with the prosecutor (`--dj`), doctrine (`--doctrine`), and L4
(`--l4 llm-proxy|rule|queue|interactive`). `--governance` presets every seat.

Code keeps only machinery: the calendar and stream, seeded draws, queues,
deadlines, capacity and lapses, counters that trigger a review, token
bookkeeping after a decision, schema validation, the budget, and the answer
keys, which never feed the workflow.

Dry mode (`--mode dry`, or any non-live run) builds every prompt, counts its
tokens (chars/4) and answers with the answer key, flipped at a seeded rate
`--dry-error-rate` so routing and fail-safes are exercised without a model.
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import re

EC_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(EC_DIR, "prompts")
SEATS = ("ec", "office", "auditor", "dj", "doctrine")
MODES = ("deterministic", "llm", "shadow")
L4_MODES = ("llm-proxy", "rule", "queue", "interactive")
PROMPT_STYLES = ("canon", "procedural")
SEAT_ROLES = {"ec": ("ec",), "office": ("office",), "auditor": ("auditor",),
              "dj": ("dj_l1", "dj_l2", "dj_l3", "prosecutor"), "doctrine": ("clerk", "lawmaker")}

# New flags and their defaults. `run_config.json` records a new flag only when it
# differs from its default, so a deterministic run's config is byte-identical.
NEW_FLAG_DEFAULTS = {
    "governance": "deterministic", "ec": None, "office": None, "auditor": None, "dj": None, "doctrine": None,
    "l4": None, "l4_human_cap": 40, "l4_shadow_proxy": None, "prompt_style": "canon", "l2_confidence": 70.0,
    "l2_audit_rate": 0.10, "dj_judge": "full", "arm_b_dj": "deterministic", "roles_config": None,
    "keys_file": None, "human_deadline_days": 10, "human_wait": False, "human_sample": 0.0, "samples": 1,
    "dry_error_rate": 0.0, "project": False, "pair": False,
}

# EC-22: what a canon-style prompt may never contain (procedure or code).
CANON_LEAK_PATTERNS = (
    r"[a-z_]+\.[a-z_]+\(", r"\bregistry\b", r"four_way", r"gate_oracle", r"bench_oracle", r"decide_request_oracle",
    r"label_for", r"gloss_oracle", r"codify_oracle", r"contravenes", r"is_departure", r"evidence_supports",
)
_LEAK_RE = [re.compile(p) for p in CANON_LEAK_PATTERNS]


def canon_leaks(text: str) -> list:
    """Patterns of CANON_LEAK_PATTERNS that `text` matches (EC-22). Empty = clean."""
    return [p.pattern for p in _LEAK_RE if p.search(text or "")]


def add_args(ap) -> None:
    """The governance flags (§4.1) on the driver's argument parser."""
    g = ap.add_argument_group("governance seats (governance build v3)")
    g.add_argument("--governance", choices=MODES, default="deterministic", help="preset for every seat")
    for seat in SEATS:
        g.add_argument(f"--{seat}", choices=MODES, default=None, help=f"mode of the {seat} seat (default: --governance)")
    g.add_argument("--l4", choices=L4_MODES, default=None,
                   help="L4 authority (default: rule under deterministic, llm-proxy otherwise)")
    g.add_argument("--l4-human-cap", type=int, default=40, help="queue/interactive items per run before the proxy takes over")
    g.add_argument("--l4-shadow-proxy", choices=("on", "off"), default=None,
                   help="queue mode: the proxy also decides every human item in shadow (default on in queue mode)")
    g.add_argument("--prompt-style", choices=PROMPT_STYLES, default="canon")
    g.add_argument("--l2-confidence", type=float, default=70.0, help="L1 confidence threshold for trigger ii")
    g.add_argument("--l2-audit-rate", type=float, default=0.10, help="trigger iv audit sample rate")
    g.add_argument("--dj-judge", choices=("full", "distinguish"), default="full")
    g.add_argument("--arm-b-dj", choices=("deterministic", "llm"), default="deterministic")
    g.add_argument("--roles-config", default=None, help="JSON roles file; required when any seat is llm or shadow")
    g.add_argument("--keys-file", default=None, help="KEY=value file outside the repo, mode 600; never echoed")
    g.add_argument("--human-deadline-days", type=int, default=10, help="queue mode lapse (pilots)")
    g.add_argument("--human-wait", action="store_true", help="queue mode: checkpoint and exit 4 when an item is due")
    g.add_argument("--human-sample", type=float, default=0.0, help="fraction of final holdings also sent to L4")
    g.add_argument("--samples", type=int, default=1, help="k reruns on a seeded 5%% sample (sample 0 binds)")
    g.add_argument("--dry-error-rate", type=float, default=0.0, help="dry mode: seeded flips of stand-in answers")
    g.add_argument("--project", action="store_true", help="with --mode dry: print the dollar projection and exit")
    g.add_argument("--pair", action="store_true", help="run each (pack, arm, seed) as a shadow-and-binding pair")


class Settings:
    """The resolved governance settings of one run."""

    def __init__(self, a):
        preset = getattr(a, "governance", "deterministic") or "deterministic"
        self.preset = preset
        self.modes = {s: (getattr(a, s, None) or preset) for s in SEATS}
        l4 = getattr(a, "l4", None)
        self.l4 = l4 or ("rule" if preset == "deterministic" else "llm-proxy")
        self.l4_human_cap = int(getattr(a, "l4_human_cap", 40))
        sp = getattr(a, "l4_shadow_proxy", None)
        self.l4_shadow_proxy = (sp == "on") if sp is not None else (self.l4 in ("queue", "interactive"))
        self.prompt_style = getattr(a, "prompt_style", "canon") or "canon"
        self.l2_confidence = float(getattr(a, "l2_confidence", 70.0))
        self.l2_audit_rate = float(getattr(a, "l2_audit_rate", 0.10))
        self.dj_judge = getattr(a, "dj_judge", "full") or "full"
        self.arm_b_dj = getattr(a, "arm_b_dj", "deterministic") or "deterministic"
        self.human_deadline_days = int(getattr(a, "human_deadline_days", 10))
        self.human_wait = bool(getattr(a, "human_wait", False))
        self.human_sample = float(getattr(a, "human_sample", 0.0))
        self.samples = max(1, int(getattr(a, "samples", 1) or 1))
        self.dry_error_rate = float(getattr(a, "dry_error_rate", 0.0))
        self.seat_mode = "live" if getattr(a, "requested_mode", getattr(a, "mode", "oracle")) == "live" else "dry"

    @property
    def governed(self) -> bool:
        """Any seat that is not today's code (L4 counts once the ladder hears)."""
        return any(m != "deterministic" for m in self.modes.values()) or self.arm_b_dj != "deterministic"

    def mode(self, seat: str) -> str:
        return self.modes[seat]

    def roles_needed(self) -> list:
        roles = []
        for s in SEATS:
            if self.modes[s] != "deterministic":
                roles += list(SEAT_ROLES[s])
        if self.modes["dj"] != "deterministic" and self.l4 in ("llm-proxy", "queue", "interactive"):
            roles.append("l4_proxy")
        if self.arm_b_dj == "llm" and "dj_l1" not in roles:
            roles.append("dj_l1")
        return roles

    def suffix(self) -> str:
        """The run-directory suffix: empty for a deterministic run."""
        if not self.governed:
            return ""
        modes = set(m for m in self.modes.values() if m != "deterministic") or {"llm"}
        tag = modes.pop() if len(modes) == 1 else "mixed"
        s = f"+gov-{tag}"
        if self.prompt_style != "canon":
            s += f"+{self.prompt_style}"
        return s

    def to_dict(self) -> dict:
        return {"preset": self.preset, "modes": dict(self.modes), "l4": self.l4, "l4_human_cap": self.l4_human_cap,
                "l4_shadow_proxy": self.l4_shadow_proxy, "prompt_style": self.prompt_style,
                "l2_confidence": self.l2_confidence, "l2_audit_rate": self.l2_audit_rate, "dj_judge": self.dj_judge,
                "arm_b_dj": self.arm_b_dj, "human_sample": self.human_sample, "samples": self.samples,
                "dry_error_rate": self.dry_error_rate, "seat_mode": self.seat_mode}


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

_PROMPT_CACHE: dict = {}


def load_prompt(seat: str, style: str) -> str:
    key = (seat, style)
    if key not in _PROMPT_CACHE:
        with open(os.path.join(PROMPTS_DIR, f"{seat}.{style}.md"), encoding="utf-8") as fh:
            _PROMPT_CACHE[key] = fh.read().strip()
    return _PROMPT_CACHE[key]


def load_stances() -> dict:
    if "stances" not in _PROMPT_CACHE:
        with open(os.path.join(PROMPTS_DIR, "stances.md"), encoding="utf-8") as fh:
            txt = fh.read()
        out, cur, buf = {}, None, []
        for line in txt.splitlines():
            if line.startswith("## "):
                if cur:
                    out[cur] = "\n".join(buf).strip()
                cur, buf = line[3:].strip(), []
            elif cur:
                buf.append(line)
        if cur:
            out[cur] = "\n".join(buf).strip()
        _PROMPT_CACHE["stances"] = out
    return _PROMPT_CACHE["stances"]


def prompt_digests() -> dict:
    """sha256 of every prompt file (manifest)."""
    out = {}
    for f in sorted(os.listdir(PROMPTS_DIR)):
        if f.endswith(".md"):
            with open(os.path.join(PROMPTS_DIR, f), "rb") as fh:
                out[f] = hashlib.sha256(fh.read()).hexdigest()
    return out


def schema_text(schema: dict) -> str:
    return "REPLY FORMAT (one JSON object): " + json.dumps(schema, sort_keys=True)


# ---------------------------------------------------------------------------
# Plain-language rendering (canon style) and the code view (procedural)
# ---------------------------------------------------------------------------

REASON_WORDS = {"N": "necessity (an incident)", "O": "opportunity (a customer ticket)",
                "K": "new knowledge (a measurement)"}


def render_rule(e, style: str) -> str:
    """One canon entry for a seat prompt: tier, rule text, admitted reasons,
    bound, contexts and doctrine (canon style in words; procedural as fields)."""
    g = e.gloss
    if style == "procedural":
        d = {"id": e.id, "tier": e.tier, "kind": e.kind, "title": e.title, "act_class": e.act_class,
             "office": e.office, "violate_factors": list(e.violate_factors), "admitted_reasons": list(g.admitted_reasons),
             "bound": dict(g.bound), "contexts": list(g.contexts), "no_waiver_classes": list(g.no_waiver_classes),
             "codified": bool(g.codified), "holdings": [{k: h.get(k) for k in ("day", "holding", "act_class")}
                                                        for h in g.holdings[-5:]]}
        return "- " + json.dumps(d, sort_keys=True)
    tier_words = {"T0": "Tier 0 (absolute)", "T1": "Tier 1 (yields only to an approval)",
                  "T2": "Tier 2 (may be departed from for an admitted reason, within bound)",
                  "T3": "Tier 3 (may be departed from in listed contexts)"}
    lines = [f"Rule {e.id}, {tier_words.get(e.tier, e.tier)}: {e.title}."]
    if e.kind == "provision" and e.violate_factors:
        lines.append("  It is broken by a change that carries any of: " + ", ".join(e.violate_factors) + ".")
    elif e.kind == "value":
        lines.append("  It is a value of the company: an act aimed at it that does something other than the change "
                     "as submitted goes against it.")
    if e.tier == "T1" and e.office:
        lines.append(f"  Owner: {e.office}; class of act: {e.act_class}.")
    if g.admitted_reasons:
        lines.append("  Admitted reasons: " + ", ".join(REASON_WORDS.get(r, r) for r in g.admitted_reasons) + ".")
    if g.bound:
        lines.append("  Bound: " + ", ".join(f"{k.replace('_', ' ')} {v}" for k, v in sorted(g.bound.items())) + ".")
    if g.contexts:
        lines.append("  Listed contexts: " + ", ".join(g.contexts) + ".")
    for h in g.holdings[-5:]:
        lines.append(f"  Doctrine: on day {h.get('day')} the court ruled {h.get('holding')} on {h.get('act_class')} "
                     f"acts under this rule.")
    if g.no_waiver_classes:
        lines.append("  Doctrine: the owners will not waive " + ", ".join(g.no_waiver_classes)
                     + " acts under this rule without an approval.")
    if g.codified:
        lines.append("  The lawmakers have closed this rule to any further exception.")
    return "\n".join(lines)


def render_approval(tok, offices: dict, day: int, style: str) -> str:
    """An approval the act names, as words (canon) or its fields (procedural)."""
    if style == "procedural":
        return "- " + json.dumps(tok.to_dict(), sort_keys=True)
    office = offices.get(tok.office)
    line = office.reporting_line if office is not None else "unknown"
    status = []
    if tok.revoked:
        status.append("withdrawn")
    if tok.consumed:
        status.append("already used")
    if day > tok.expires_day:
        status.append("out of date")
    scope = "any rule" if tok.scope == "*" else f"rule {tok.scope}"
    until = "with no end date" if tok.standing_emergency else f"until day {tok.expires_day}"
    return (f"- Approval {tok.id}: issued by {tok.office} (reporting to {line}) on day {tok.issued_day} for "
            f"{tok.act_class} acts on {scope}, under canon edition {tok.canon_version}, valid {until}, "
            + ("single use" if tok.single_use else "reusable within its term")
            + (("; " + ", ".join(status)) if status else "; not used") + ".")


# ---------------------------------------------------------------------------
# Dry stand-ins
# ---------------------------------------------------------------------------


class DryFlip:
    """Seeded flips of the stand-in answers: `flip(key)` is True with
    probability `rate`, drawn from (seed, pack, key) only, so every arm and
    every rerun flips the same decisions."""

    def __init__(self, seed: int, pack: str, rate: float):
        self.seed, self.pack, self.rate = seed, pack, float(rate or 0.0)

    def flip(self, key: str) -> bool:
        if self.rate <= 0:
            return False
        return random.Random(f"{self.seed}|{self.pack}|{key}|dryflip").random() < self.rate

    def choice(self, key: str, options: list):
        opts = list(options)
        return opts[random.Random(f"{self.seed}|{self.pack}|{key}|dryflip-choice").randrange(len(opts))]


DRY_OUT_TOKENS = {"ec": 500, "office": 120, "auditor": 400, "dj_l1": 900, "dj_l2": 1000, "dj_l3": 2500,
                  "prosecutor": 80, "clerk": 150, "lawmaker": 150, "l4_proxy": 1500}


# ---------------------------------------------------------------------------
# State hash (pairs, §3.5)
# ---------------------------------------------------------------------------


def sha_json(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode("utf-8")).hexdigest()


def state_hashes(store: list, canon, registry) -> dict:
    return {"store": sha_json([r.to_dict() for r in store]),
            "glosses": sha_json({eid: e.gloss.to_dict() for eid, e in canon.entries.items()}),
            "registry": sha_json(registry.to_dict())}
