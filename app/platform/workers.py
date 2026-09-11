"""Background workers for the platform plane.

Demo profile: one in-process JobWorker (app.jobs).
Self-host / enterprise: same worker, optionally more threads via
DJ_WORKER_THREADS. The Kernel is never opened from random threads for
writes — jobs call into PRGateway / enterprise which already serialise
through Gate connections.
"""
from __future__ import annotations

import os
from typing import Any

from .. import jobs


class WorkerPlane:
    def __init__(self, svc: Any, path: str | None = None):
        self.svc = svc
        self.path = path
        self._workers: list[jobs.JobWorker] = []

    def start(self) -> None:
        jobs.ensure_schema(self.path)
        n = max(1, int(os.environ.get("DJ_WORKER_THREADS", "1")))
        for i in range(n):
            w = jobs.JobWorker(self.svc, self.path)
            w.start()
            self._workers.append(w)

    def stop(self) -> None:
        for w in self._workers:
            w.stop()
        self._workers.clear()

    @property
    def worker_count(self) -> int:
        return len(self._workers)
