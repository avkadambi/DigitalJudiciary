"""Neutral change-request model produced by any VCS connector."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass
class ChangeRequest:
    """Provider-agnostic description of a change under adjudication.

    The Kernel and PRGateway consume sessions built from these fields; they
    do not import GitHub or GitLab types.
    """
    provider: str                       # github | gitlab | azure_devops | generic
    delivery_id: str                    # idempotency key from the provider
    event_type: str                     # e.g. pull_request, merge_request
    action: str                         # opened, synchronize, submit, …
    repo: str                           # owner/name or project path
    number: int                         # PR / MR number
    title: str = ""
    body: str = ""
    head_sha: str = ""
    base_ref: str = "main"
    author_login: str = ""
    labels: list[str] = field(default_factory=list)
    paths: list[str] = field(default_factory=list)
    checks: list[dict[str, Any]] = field(default_factory=list)
    organization: str | None = None     # resolved by tenancy registry
    installation_id: str | None = None
    raw_headers: dict[str, str] = field(default_factory=dict)
    raw_body: bytes = b""


@dataclass
class ConnectorResult:
    ok: bool
    change: ChangeRequest | None = None
    ignore_reason: str | None = None
    error: str | None = None
    status: int = 200


@runtime_checkable
class Connector(Protocol):
    """Inbound connector contract.

    Implementations must be side-effect free with respect to the ledger:
    verify → parse → resolve tenant → return ChangeRequest (or ignore).
    """

    name: str

    def accept(self, headers: dict[str, str], raw_body: bytes) -> ConnectorResult:
        """Verify signature and parse into a ChangeRequest."""
        ...
