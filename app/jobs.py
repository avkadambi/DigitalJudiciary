"""Job queue façade used by HTTP inbound and the worker plane.

Backends live in ``app.platform.queue``:
  * SQLite (default) — single-process demo / self-host
  * Postgres ``FOR UPDATE SKIP LOCKED`` — multi-worker enterprise

When ``DJ_ASYNC_INBOUND=1``, the webhook handler enqueues and returns 202;
workers run the same ``PRGateway.receive`` path. The ledger and Gate stay
the system of record; the queue is only durable transport.
"""
from __future__ import annotations

import threading
from typing import Any

from . import metrics
from .platform.queue import JobQueue, open_queue

_queue: JobQueue | None = None
_queue_path: str | None = None
_queue_lock = threading.Lock()


def _q(path: str | None = None) -> JobQueue:
    global _queue, _queue_path
    with _queue_lock:
        if _queue is None or (path is not None and path != _queue_path):
            _queue = open_queue(path)
            _queue_path = path
        return _queue


def ensure_schema(path: str | None = None) -> None:
    _q(path).ensure_schema()


def enqueue(kind: str, payload: dict, path: str | None = None) -> str:
    return _q(path).enqueue(kind, payload)


def pending_count(path: str | None = None) -> int:
    return _q(path).pending_count()


def backend_name(path: str | None = None) -> str:
    return _q(path).name


class JobWorker:
    """Daemon thread: reclaim → claim → dispatch → finish."""

    def __init__(self, svc: Any, path: str | None = None,
                 interval_s: float = 0.5):
        self.svc = svc
        self.path = path
        self.interval = interval_s
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        ensure_schema(self.path)
        self._thread = threading.Thread(
            target=self._loop, daemon=True, name="dj-job-worker")
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()

    def _loop(self) -> None:
        q = _q(self.path)
        while not self._stop.wait(self.interval):
            try:
                job = q.claim()
                if not job:
                    continue
                self._run(q, job)
            except Exception:  # noqa: BLE001
                metrics.inc("jobs_worker_errors")

    def _run(self, q: JobQueue, job: dict) -> None:
        kind = job["kind"]
        payload = job["payload"]
        try:
            if kind == "github_inbound":
                headers = payload.get("headers") or {}
                raw = (payload.get("raw") or "").encode("utf-8", "replace")
                self.svc.gateway.receive(headers, raw)
            elif kind == "post_merge_scan":
                from . import enterprise
                enterprise.run_post_merge_scan(self.svc, payload)
            else:
                raise RuntimeError(f"unknown job kind {kind!r}")
            q.finish(job["job_id"], True)
        except Exception as e:  # noqa: BLE001
            q.finish(job["job_id"], False, str(e))
