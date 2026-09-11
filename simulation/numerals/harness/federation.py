"""Federated adjudication — one enterprise store, five divisions.

A record written on an enterprise provision by any division is visible to every
division. What differs by division is SCOPE: a record the deciding division
wrote itself is narrower than one another division wrote, so when both survive
the gate the ordering rule's scope key — narrower covering scope preferred,
already in engine.order — prefers the home record. That is Chapter 4 §8's thin
vertical precedent, produced by the existing key and not a new one.

The mechanism is exactly one line: a foreign record is presented to the deciding
division with `scope_width + FOREIGN_SCOPE_OFFSET`. FC-07 checks that a home
record beats a foreign one on the scope key; M-F1 sets the offset to zero and
FC-07 dies, which is how we know the check tests the mechanism and not itself.

Nothing else in the engine changes. Retrieval, the gate, A6, the prosecutor's
threshold, escalation and admission are the engine's own.
"""

from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import engine  # noqa: E402
from engine import Record  # noqa: E402

FOREIGN_SCOPE_OFFSET = 1


def view_for(division: str, store: list, record_division: dict) -> list:
    """The enterprise store as `division` sees it: foreign records widened."""
    out = []
    for r in store:
        home = record_division.get(r.id)
        if home is None or home == division:
            out.append(r)
        else:
            out.append(Record(**{**r.__dict__, "scope_width": r.scope_width + FOREIGN_SCOPE_OFFSET}))
    return out


def adjudicate(case_dict: dict, store: list, provisions: dict, theta: float,
               record_division: dict) -> dict:
    case = engine.case_from_dict(case_dict)
    division = case_dict["division"]
    return engine.adjudicate(case, view_for(division, store, record_division), provisions, theta)


def replay(cases: list, seed_store: list, seed_divisions: dict, provisions: dict,
           theta: float) -> dict:
    """Chronological replay of the enterprise stream, growing one shared store."""
    store = [Record.from_dict(r) if isinstance(r, dict) else r for r in seed_store]
    record_division = dict(seed_divisions)
    traces, docket, written = [], [], []
    for c in cases:
        tr = adjudicate(c, store, provisions, theta, record_division)
        tr["case"] = c["id"]
        if tr["route"] in (engine.ROUTE_DOCKET_DECLINED, engine.ROUTE_DOCKET_NULL):
            docket.append({"case": c["id"], "division": c["division"],
                           "route": "declined" if tr["route"] == engine.ROUTE_DOCKET_DECLINED else "null",
                           "rules": list(c["rules"]), "rating": tr["rating"], "tau": tr["tau"],
                           "ts": c["ts"], "consulted": sorted(tr.get("consulted") or [])})
        if tr["admitted"]:
            rec = engine._record_from(engine.case_from_dict(c), tr, provisions)
            store.append(rec)
            record_division[rec.id] = c["division"]
            written.append(rec)
        traces.append(tr)
    return {"traces": traces, "store": store, "docket": docket,
            "records_written": written, "record_division": record_division}
