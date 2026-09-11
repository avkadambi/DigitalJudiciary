"""VCS connectors: translate provider events into Kernel-facing work.

Connectors never write the ledger. They verify, normalize, and hand a
neutral payload to the inbound gateway / job queue.
"""

from .base import ChangeRequest, Connector, ConnectorResult

__all__ = ["ChangeRequest", "Connector", "ConnectorResult"]
