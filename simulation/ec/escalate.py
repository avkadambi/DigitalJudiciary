"""
Escalation to the slow track (EC §3.5; DESIGN §2.5).

A gate block at T0 or T1, and a hold on a conflict, is not the end of the
matter: it is *filed*. The Bench hears it `d_bench` days later with the pack's
own DJ engine, unmodified, as a contested case (`contest_to` set by
`contest_policy`). If the engine admits the trace, the record it constructs is
written to the DJ store exactly as `replay` would write it, with one overlay:
the record's expiry is patched from 180 ticks to 180 days (DESIGN §0).

The engine is passed in, not imported: each pack carries its own copy of
`harness/engine.py` and the caller loads the right one by path.

`Bench(internal=True)` is arm C's internal review office. It hears with the
same engine but writes no record and no gloss; its holdings go to `log` only.
"""

from __future__ import annotations

from dataclasses import dataclass

from .gate import Proposal, Verdict

from .calendar import D_BENCH, DAY_TICKS, EXPIRY_DAYS as RECORD_EXPIRY_DAYS  # working days


@dataclass
class Escalation:
    act_id: str
    case_id: str
    company: str
    day_filed: int
    hear_day: int
    entry: str | None
    tier: str | None
    reason_code: str
    contest_to: int

    def to_dict(self) -> dict:
        return {
            "act_id": self.act_id, "case_id": self.case_id, "company": self.company,
            "day_filed": self.day_filed, "hear_day": self.hear_day, "entry": self.entry, "tier": self.tier,
            "reason_code": self.reason_code, "contest_to": self.contest_to,
        }

    @staticmethod
    def from_dict(d: dict) -> "Escalation":
        return Escalation(
            act_id=d["act_id"], case_id=d["case_id"], company=d["company"], day_filed=int(d["day_filed"]),
            hear_day=int(d["hear_day"]), entry=d.get("entry"), tier=d.get("tier"),
            reason_code=d["reason_code"], contest_to=int(d.get("contest_to", 0)),
        )


def contest_policy(v: Verdict) -> int:
    """How far up a verdict is contested: a floor violation or a tokenless T1
    contrariety to the second instance; a conflict hold to the third; the rest
    not at all."""
    if v.reason_code in ("t0_violation", "t1_tokenless", "t1_claimed_no_token", "agent_escalated"):
        return 2
    if v.reason_code == "conflict_hold":
        return 3
    return 0


def escalation_from(p: Proposal, v: Verdict, day: int, d_bench: int = D_BENCH) -> Escalation:
    return Escalation(
        act_id=p.act_id, case_id=p.case_id, company=p.company, day_filed=day, hear_day=day + d_bench,
        entry=v.entry, tier=v.tier, reason_code=v.reason_code, contest_to=contest_policy(v),
    )


def patch_expiry(rec) -> None:
    """The one engine-semantic overlay: the engine writes `ts + 180`; a day is
    DAY_TICKS ticks, so an acceptance lasts RECORD_EXPIRY_DAYS working days."""
    if rec.expiry is not None:
        rec.expiry = rec.ts + RECORD_EXPIRY_DAYS * DAY_TICKS


class EngineHearer:
    """Today's hearing, moved verbatim (governance build §5.8): the pack's
    engine on the case as contested; an external bench writes the record on an
    admitted trace."""

    kind = "engine"

    def hear(self, bench: "Bench", esc: Escalation, case_dict: dict, store: list, provisions: dict, theta,
             engine_module) -> dict:
        d = dict(case_dict)
        d["contest_to"] = esc.contest_to
        case = engine_module.case_from_dict(d)
        trace = engine_module.adjudicate(case, store, provisions, theta)
        rec = None
        if not bench.internal and trace.get("admitted"):
            rec = engine_module._record_from(case, trace, provisions)
            patch_expiry(rec)
            store.append(rec)
        return {"holding": trace["decision"], "record": rec, "trace": trace}

    def to_dict(self) -> dict:
        return {"kind": self.kind}


class Bench:
    """The slow track's queue. `file` on the day of the verdict, `due` on each
    later day, `hear` each due escalation. Who hears is the `hearer`: the
    engine (today, the default) or the judges' ladder (governance build)."""

    def __init__(self, internal: bool = False, d_bench: int = D_BENCH, cap_per_day: int = 0,
                 lapse_days: int = 20, hearer=None):
        self.internal = internal
        self.d_bench = d_bench
        self.hearer = hearer if hearer is not None else EngineHearer()
        # R2 registered sensitivity: at most `cap_per_day` hearings a working day (0 = unlimited),
        # first filed first heard; an escalation unheard `lapse_days` after its hearing day lapses.
        self.cap_per_day = int(cap_per_day or 0)
        self.lapse_days = int(lapse_days)
        self.lapsed: list[dict] = []
        self.queue: list[Escalation] = []
        self.heard: list[dict] = []
        self.log: list[dict] = []

    def file(self, esc: Escalation) -> None:
        self.queue.append(esc)

    def due(self, day: int) -> list:
        """Escalations whose hearing day has come, removed from the queue in
        filing order. With a daily cap, the rest wait; one unheard `lapse_days`
        after its hearing day lapses (logged in `lapsed`, never heard)."""
        ready = [e for e in self.queue if e.hear_day <= day]
        waiting = [e for e in self.queue if e.hear_day > day]
        if not self.cap_per_day:
            self.queue = waiting
            return ready
        keep, out = [], []
        for e in ready:
            if day - e.hear_day > self.lapse_days:
                self.lapsed.append({"act_id": e.act_id, "case_id": e.case_id, "hear_day": e.hear_day,
                                    "lapsed_day": day, "entry": e.entry})
            elif len(out) < self.cap_per_day:
                out.append(e)
            else:
                keep.append(e)
        self.queue = keep + waiting
        return out

    def hear(self, esc: Escalation, case_dict: dict, store: list, provisions: dict, theta, engine_module) -> dict:
        """Hear one escalation through the hearer. Returns {"holding", "record",
        "trace"} (plus the ladder's fields when the ladder heard it); the record
        is appended to `store` only by an external bench on an admitted trace."""
        res = self.hearer.hear(self, esc, case_dict, store, provisions, theta, engine_module)
        trace, rec = res["trace"], res["record"]
        entry = {"act_id": esc.act_id, "case_id": esc.case_id, "company": esc.company, "day": esc.hear_day,
                 "entry": esc.entry, "tier": esc.tier, "reason_code": esc.reason_code,
                 "contest_to": esc.contest_to, "holding": res["holding"], "route": trace.get("route"),
                 "record": rec.id if rec is not None else None, "internal": self.internal}
        self.heard.append(entry)
        if self.internal:
            self.log.append(entry)
        return res

    def to_dict(self) -> dict:
        d = {"internal": self.internal, "d_bench": self.d_bench, "cap_per_day": self.cap_per_day,
             "lapse_days": self.lapse_days, "lapsed": list(self.lapsed),
             "queue": [e.to_dict() for e in self.queue], "heard": list(self.heard), "log": list(self.log)}
        if self.hearer.kind != "engine":        # the engine hearer keeps today's layout byte for byte
            d["hearer"] = self.hearer.to_dict()
        return d

    @staticmethod
    def from_dict(d: dict, hearer=None) -> "Bench":
        """`hearer` is rebuilt by the caller (it holds clients); its state, if any,
        is restored from `d["hearer"]`."""
        b = Bench(internal=bool(d.get("internal", False)), d_bench=int(d.get("d_bench", D_BENCH)),
                  cap_per_day=int(d.get("cap_per_day", 0) or 0), lapse_days=int(d.get("lapse_days", 20)),
                  hearer=hearer)
        if hearer is not None and hasattr(hearer, "restore"):
            hearer.restore(d.get("hearer") or {})
        b.lapsed = list(d.get("lapsed") or [])
        b.queue = [Escalation.from_dict(e) for e in d.get("queue") or []]
        b.heard = list(d.get("heard") or [])
        b.log = list(d.get("log") or [])
        return b
