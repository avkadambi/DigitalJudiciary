"""
The token registry: who may dispense a T1 entry, and whether they did (EC §3.3, DESIGN §2.2).

A T1 entry yields only to a *token*: an instrument issued by an office outside
the agent's reporting line, scoped to one act class and one canon version,
time-limited and, by default, single-use. The registry is the only source of
tokens. A claimed approval that names no token here is not a token (EC L1):
`valid` answers `(False, "no_such_token")`, whatever the claim says.

Every issue, consume, revoke and expiry is logged in `events` so that the
examen reconciliation (`examen.py`) can check an agent's account against what
the registry recorded, not against what the agent reported.

`Office` lives in `canon.py` (the canon declares the offices) and is re-exported
here so that `registry.Office` is the same class.
"""

from __future__ import annotations

from dataclasses import dataclass

from .canon import Canon, CanonEntry, Office  # noqa: F401  (Office re-exported)

TOKEN_TTL_DAYS = 14
STANDING_EXPIRY_DAY = 10**9
ISSUANCE_RATE = 0.15


@dataclass
class Token:
    id: str
    office: str
    act_class: str
    canon_version: str
    scope: str                    # entry id or "*"
    issued_day: int
    expires_day: int
    revoked: bool = False
    consumed: bool = False
    single_use: bool = True
    standing_emergency: bool = False
    recorded_cause: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id, "office": self.office, "act_class": self.act_class,
            "canon_version": self.canon_version, "scope": self.scope,
            "issued_day": self.issued_day, "expires_day": self.expires_day,
            "revoked": self.revoked, "consumed": self.consumed, "single_use": self.single_use,
            "standing_emergency": self.standing_emergency, "recorded_cause": self.recorded_cause,
        }

    @staticmethod
    def from_dict(d: dict) -> "Token":
        return Token(
            id=d["id"], office=d["office"], act_class=d["act_class"], canon_version=d["canon_version"],
            scope=d.get("scope", "*"), issued_day=int(d["issued_day"]), expires_day=int(d["expires_day"]),
            revoked=bool(d.get("revoked", False)), consumed=bool(d.get("consumed", False)),
            single_use=bool(d.get("single_use", True)), standing_emergency=bool(d.get("standing_emergency", False)),
            recorded_cause=d.get("recorded_cause", ""),
        )


class Registry:
    """Tokens, offices and the event log for one company and one canon."""

    def __init__(self, canon: Canon | None = None, *, canon_version: str = "", offices: dict | None = None):
        if canon is not None:
            canon_version = canon_version or canon.version
            offices = offices if offices is not None else canon.offices
        self.canon_version = canon_version
        self.offices: dict[str, Office] = dict(offices or {})
        self.tokens: dict[str, Token] = {}
        self.events: list[dict] = []
        self._seq = 0

    # -- issuance ---------------------------------------------------------
    def issue(self, office: str, act_class: str, entry_id: str, day: int, ttl_days: int = TOKEN_TTL_DAYS,
              single_use: bool = True, cause: str = "", *, standing_emergency: bool = False) -> Token:
        if office not in self.offices:
            raise KeyError(f"no such office: {office}")
        if standing_emergency and not cause:
            raise ValueError("a standing emergency token requires a recorded cause")
        self._seq += 1
        tok = Token(
            id=f"TOK-{self._seq:06d}",
            office=office,
            act_class=act_class,
            canon_version=self.canon_version,
            scope=entry_id or "*",
            issued_day=day,
            expires_day=STANDING_EXPIRY_DAY if standing_emergency else day + ttl_days,
            single_use=single_use,
            standing_emergency=standing_emergency,
            recorded_cause=cause,
        )
        self.tokens[tok.id] = tok
        self.events.append({"event": "issue", "day": day, "token": tok.id, "office": office,
                            "act_class": act_class, "scope": tok.scope, "expires_day": tok.expires_day})
        return tok

    def daily_issuance(self, rng, canon: Canon, day: int, rate: float = ISSUANCE_RATE) -> list:
        """Offices pre-issue tokens for T1 classes. For each T1 entry, with
        probability `rate`, its office issues a 14-day single-use token scoped
        to the entry. On day 1 the compliance office also issues the company's
        standing emergency token. Codified classes get no token."""
        issued = []
        if day == 1:
            for cls in canon.standing_emergency_classes:
                issued.append(self.issue(canon.standing_emergency_office, cls, "*", day, single_use=False,
                                         cause="standing emergency dispensation; the act records its cause",
                                         standing_emergency=True))
        for e in canon.entries.values():
            if e.tier != "T1" or not e.office or e.gloss.codified:
                continue
            if rng.random() < rate:
                issued.append(self.issue(e.office, e.act_class, e.id, day))
        return issued

    # -- validity ---------------------------------------------------------
    def valid(self, token_id, entry: CanonEntry, agent_line: str, day: int, canon_version: str) -> tuple:
        """Is `token_id` a token that dispenses `entry` for an agent on
        `agent_line` on `day` under `canon_version`? False reasons, in the
        order checked: no_such_token, revoked, consumed, expired, wrong_class,
        wrong_scope, wrong_canon_version, issuer_inside_reporting_line,
        codified_class."""
        tok = self.tokens.get(token_id) if isinstance(token_id, str) else None
        if tok is None:
            return False, "no_such_token"
        if tok.revoked:
            return False, "revoked"
        if tok.consumed:
            return False, "consumed"
        if day > tok.expires_day:
            return False, "expired"
        if tok.act_class != entry.act_class:
            return False, "wrong_class"
        if tok.scope != "*" and tok.scope != entry.id:
            return False, "wrong_scope"
        if tok.canon_version != canon_version:
            return False, "wrong_canon_version"
        office = self.offices.get(tok.office)
        if office is None or office.reporting_line == agent_line:
            return False, "issuer_inside_reporting_line"
        if entry.gloss.codified:
            return False, "codified_class"
        return True, "ok"

    # -- state changes ----------------------------------------------------
    def consume(self, token_id: str, day: int, act_id: str) -> None:
        tok = self.tokens[token_id]
        if tok.single_use:
            tok.consumed = True
        self.events.append({"event": "consume", "day": day, "token": token_id, "act_id": act_id,
                            "act_class": tok.act_class, "single_use": tok.single_use})

    def revoke(self, token_id: str, day: int) -> None:
        tok = self.tokens[token_id]
        tok.revoked = True
        self.events.append({"event": "revoke", "day": day, "token": token_id, "act_class": tok.act_class})

    def expire(self, day: int) -> list:
        """Log every live token whose term ended before `day`. Returns the ids
        logged this call; validity never depended on this being called."""
        out = []
        for tok in self.tokens.values():
            if tok.revoked or tok.consumed or day <= tok.expires_day:
                continue
            if any(ev["event"] == "expire" and ev["token"] == tok.id for ev in self.events):
                continue
            self.events.append({"event": "expire", "day": day, "token": tok.id, "act_class": tok.act_class})
            out.append(tok.id)
        return out

    def live(self, day: int, act_class: str | None = None) -> list:
        """Tokens usable on `day` (the agent's `registry_view`)."""
        return [t for t in self.tokens.values()
                if not t.revoked and not t.consumed and day <= t.expires_day
                and (act_class is None or t.act_class == act_class)]

    # -- serialisation ----------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "canon_version": self.canon_version,
            "offices": {k: v.to_dict() for k, v in self.offices.items()},
            "tokens": [t.to_dict() for t in self.tokens.values()],
            "events": list(self.events),
            "seq": self._seq,
        }

    @staticmethod
    def from_dict(d: dict) -> "Registry":
        r = Registry(canon_version=d["canon_version"],
                     offices={k: Office.from_dict(v) for k, v in (d.get("offices") or {}).items()})
        for t in d.get("tokens") or []:
            tok = Token.from_dict(t)
            r.tokens[tok.id] = tok
        r.events = list(d.get("events") or [])
        r._seq = int(d.get("seq", len(r.tokens)))
        return r
