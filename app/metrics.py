"""Process-local operational metrics for the single-container deployment.

No external dependencies. Counters and gauges live in this process only;
they reset on restart, which is the honest behaviour for a single-container
artifact. Exposed via GET /v1/admin/status so operators can see whether the
active-holdings cache is helping and whether the ledger is approaching the
documented scale envelope.

These numbers are diagnostic, not a substitute for an external monitoring
system. They deliberately do not attempt to survive process death.
"""
from __future__ import annotations

import threading
import time
from collections import defaultdict

_lock = threading.Lock()
_counters: dict[str, int] = defaultdict(int)
_gauges: dict[str, float] = {}
_started = time.monotonic()


def inc(name: str, n: int = 1) -> None:
    with _lock:
        _counters[name] += n


def set_gauge(name: str, value: float) -> None:
    with _lock:
        _gauges[name] = float(value)


def snapshot() -> dict:
    with _lock:
        return {
            "uptime_s": round(time.monotonic() - _started, 1),
            "counters": dict(_counters),
            "gauges": dict(_gauges),
        }


def reset() -> None:
    """Test helper only."""
    with _lock:
        _counters.clear()
        _gauges.clear()
