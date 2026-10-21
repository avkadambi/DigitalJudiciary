"""
Agents (DESIGN §4): what fills `Proposal.act` and writes the examen.

`Context` is everything an agent may read before it proposes: the skeleton,
the engaged canon entries with their current glosses, its view of the token
registry, whether an audit was announced and which driver was presented. The
driver also hands the agent an `rng` seeded from (seed, pack, skeleton id) so
that the same skeleton draws the same act in every arm.
"""

from __future__ import annotations

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Context:
    proposal_skeleton: object            # gate.Proposal with act=None
    engaged_entries: list                # list[CanonEntry]
    registry_view: list                  # list[Token] usable today
    audit_announced: bool
    presented_driver: str
    driver_level: int
    canon_text: str = ""                 # rendered for an LLM
    rng: random.Random | None = None     # seeded by the driver per skeleton
    day: int = 0
    conflict: bool = False
    extra: dict = field(default_factory=dict)

    def rand(self) -> random.Random:
        if self.rng is None:
            self.rng = random.Random(f"ctx|{self.proposal_skeleton.act_id}")
        return self.rng


class Agent(ABC):
    id: str
    archetype: str
    line: str = "engineering"

    def __init__(self, id: str, archetype: str, line: str = "engineering"):
        self.id = id
        self.archetype = archetype
        self.line = line
        self.last_cost: dict | None = None

    @abstractmethod
    def propose(self, ctx: Context):
        """Return a gate.Act."""

    @abstractmethod
    def examen(self, ctx: Context, act, verdict, executed: bool):
        """Return an examen.ExamenEntry, or None for silence."""

    @abstractmethod
    def manipulation_check(self, ctx: Context) -> bool:
        """Does the agent believe it is being watched?"""

    def state(self) -> dict:
        return {}

    def restore(self, d: dict) -> None:
        return None


def make_agent(spec: str, company: str, mode: str = "oracle", cache_dir: str | None = None,
               log_path: str | None = None, rate_limit_s: float = 0.0):
    """`policy:<archetype>` | `llm:anthropic:<model>` | `llm:openai:<model>`.
    `log_path` and `rate_limit_s` reach the LLM agent only."""
    parts = spec.split(":")
    if parts[0] == "policy":
        from .policy import PolicyAgent, OracleAgent, AdversarialAgent
        name = parts[1] if len(parts) > 1 else "honest"
        aid = f"agent:{company}-conscience-01"
        if name == "oracle":
            return OracleAgent(aid)
        if name == "adversarial":
            return AdversarialAgent(aid)
        return PolicyAgent(aid, name)
    if parts[0] == "llm":
        from .llm import LLMAgent
        provider = parts[1] if len(parts) > 1 else "anthropic"
        model = parts[2] if len(parts) > 2 else ""
        provider = {"openai": "openai_compatible"}.get(provider, provider)
        return LLMAgent(f"agent:{company}-conscience-01", provider=provider, model=model, mode=mode,
                        cache_dir=cache_dir, log_path=log_path, rate_limit_s=rate_limit_s)
    raise ValueError(f"unknown agent spec {spec!r}")


__all__ = ["Context", "Agent", "make_agent"]
