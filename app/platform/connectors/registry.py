"""Plugin registry for VCS connectors.

To add a connector:
  1. Implement ``Connector`` in ``app/platform/connectors/<name>.py``
  2. Register it below (or via ``register()`` at import time)
  3. Enable it in ``config/dj.toml`` under ``[[connectors]]``

The HTTP layer resolves connectors by ``type`` and webhook path.
"""
from __future__ import annotations

from typing import Callable

from .base import Connector
from .github import GitHubConnector
from .generic import GenericWebhookConnector

_REGISTRY: dict[str, Callable[..., Connector]] = {}


def register(type_name: str, factory: Callable[..., Connector]) -> None:
    _REGISTRY[type_name] = factory


def get(type_name: str, **kwargs) -> Connector:
    if type_name not in _REGISTRY:
        raise KeyError(
            f"unknown connector {type_name!r}; known: {sorted(_REGISTRY)}")
    return _REGISTRY[type_name](**kwargs)


def known() -> list[str]:
    return sorted(_REGISTRY)


# Built-in plugins
register("github", lambda **kw: GitHubConnector(**kw))

# Placeholders document the extension point without requiring implementation.
class _StubConnector:
    name = "stub"

    def __init__(self, type_name: str, **_kw):
        self.type_name = type_name

    def accept(self, headers, raw_body):
        from .base import ConnectorResult
        return ConnectorResult(
            ok=False,
            error=f"connector {self.type_name!r} is not implemented yet; "
                  f"add app/platform/connectors/{self.type_name}.py",
            status=501,
        )


def _stub(type_name: str):
    return lambda **kw: _StubConnector(type_name, **kw)


register("gitlab", _stub("gitlab"))
register("azure_devops", _stub("azure_devops"))
register("bitbucket", _stub("bitbucket"))
register("generic", lambda **kw: GenericWebhookConnector(**kw))
