"""Lifecycle Manager: the A7 sweep. Idempotent by construction — emitting a
lapse event twice is harmless, which is exactly why lapse is an event and
not a boolean. Runs as a daemon thread (the in-process stand-in for a
Temporal Schedule)."""
from __future__ import annotations

import threading

from . import db
from .kernel import ChallengeGate


class LifecycleManager:
    def __init__(self, gate: ChallengeGate, path: str | None = None,
                 interval_s: float = 60.0):
        self._r = db.open_reader(path)
        self._gate = gate
        self._interval = interval_s
        self._stop = threading.Event()

    def sweep_once(self) -> int:
        """Emit 'lapsed' for every acceptance past expiry lacking both an
        adoption and a lapse event. Returns the number emitted."""
        rows = self._r.execute(
            "SELECT id FROM record_effective"
            " WHERE lapsed = 1"
            "   AND NOT EXISTS (SELECT 1 FROM precedent_lifecycle_event e"
            "                   WHERE e.record_id = record_effective.id"
            "                     AND e.event_type = 'lapsed')").fetchall()
        for r in rows:
            self._gate.emit_lifecycle(r["id"], "lapsed",
                                      {"swept": True}, "lifecycle_manager")
        # Backstop: every acceptance must have its referral (A7).
        missing = self._r.execute(
            "SELECT id FROM precedent_record p WHERE p.is_acceptance = 1"
            "  AND NOT EXISTS (SELECT 1 FROM precedent_lifecycle_event e"
            "                  WHERE e.record_id = p.id"
            "                    AND e.event_type = 'referral_emitted')"
        ).fetchall()
        for r in missing:  # unreachable if the Gate is sound; belt+braces
            self._gate.emit_lifecycle(r["id"], "referral_emitted",
                                      {"backstop": True}, "lifecycle_manager")
        return len(rows)

    def start(self) -> None:
        def loop():
            while not self._stop.wait(self._interval):
                try:
                    self.sweep_once()
                except Exception:
                    pass  # sweep is idempotent; the next tick retries
        threading.Thread(target=loop, daemon=True,
                         name="lifecycle-manager").start()

    def stop(self) -> None:
        self._stop.set()


def mirror_referral_outcomes(reader, gate: ChallengeGate) -> None:
    """Mirror decided referrals into the lifecycle log so record_effective
    and the dossier read from one place. Idempotent."""
    rows = reader.execute(
        "SELECT a.id AS amendment_id, a.status, a.source_record"
        " FROM draft_amendment a"
        " WHERE a.origin = 'risk_acceptance_referral'"
        "   AND a.status IN ('adopted','rejected','withdrawn')"
        "   AND a.source_record IS NOT NULL"
        "   AND NOT EXISTS (SELECT 1 FROM precedent_lifecycle_event e"
        "        WHERE e.record_id = a.source_record"
        "          AND e.event_type = 'referral_' || a.status)").fetchall()
    for r in rows:
        gate.emit_lifecycle(r["source_record"], f"referral_{r['status']}",
                            {"amendment_id": r["amendment_id"]},
                            "referral_service")
