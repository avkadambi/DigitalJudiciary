"""Live scenario generation — the ONLY part of this system that calls a model
outside adjudication, and the only one that runs on a button press.

Why this exists: the demo corpus is a fixed 100 scenarios per company,
converted from the case study. Anyone watching a second demo has already seen
them. This generates fresh, plausible changes against a company's actual
constitution so the docket is different every time.

=== The one design rule that makes this worth anything ===

The model generates FACTS. It never generates outcomes.

It is shown a company's provisions and its factor vocabulary, and asked to
invent changes an engineer might plausibly submit — a description, the clauses
they touch, the facts true of them, and how hard somebody pushed back. It is
never asked what the disposition should be, and any it volunteers is discarded
unread. Every generated change is then filed through `PRGateway.receive` like
any other, and the architecture decides what happens to it.

Let the model write the expected outcome too and the demo would be measuring
the model's opinion of itself. Written this way, a generated scenario is an
input under test, exactly like a real pull request.

=== Containment ===

* Never runs on boot, on a timer, or as a side effect of any other request.
  The only entry point is `start()`, called from POST /review/admin/generate.
* Off unless DJ_SIMULATOR=1. Absent that, the admin screen does not render
  and the endpoint 404s.
* Requires ANTHROPIC_API_KEY and fails loudly without one; there is no silent
  fallback to the oracle, because a "generated" corpus that quietly wasn't
  would be worse than no feature.
* One job at a time, process-wide.
* Every proposal is validated against the live constitution before it is
  filed. A factor the company has never heard of, or a provision that does not
  exist, is dropped and counted — the model cannot widen the vocabulary, and
  cannot invent a clause to be judged under.
"""
from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.request
import uuid

MODEL = os.environ.get("DJ_SIMULATOR_MODEL", "claude-sonnet-4-6")
BATCH = 10                     # scenarios per model call
MAX_PER_RUN = 200

CATEGORIES = (
    "a routine change that violates nothing",
    "a plain violation of one clause",
    "a violation on facts a past decision already covers",
    "a violation whose facts differ from the nearest precedent in some"
    " material way",
    "a change that trips an ABSOLUTE provision",
    "a change contentious enough to be pushed all the way to a risk owner",
    "a change to the policy repository itself (engages 'constitution')",
)

PROMPT = """You are generating test scenarios for a governance system that \
adjudicates AI-generated code changes at {company}.

Its constitution:
{provisions}

The only facts this company's rulebook knows how to read:
{vocabulary}

Generate exactly {n} DISTINCT, plausible pull requests an engineer at this \
company might open. Vary them across these situations:
{categories}

Rules you must follow:
- "factors" MUST be chosen only from the vocabulary above. Do not invent facts.
- "provisions" MUST be provision ids from the constitution above, or the \
single value "constitution" for a change to the policy repository itself.
- A scenario that should violate a clause must include at least one of that \
clause's trigger factors. One that should not must include "compliant" and no \
trigger factors.
- "contest_to" is how hard a person pushed back: 1 = accepted the first \
answer, 2 or 3 = contested that many times, 4 = pushed to a named risk owner.
- Do NOT state what the decision should be. That is not yours to decide and \
any such field is discarded.

Respond with ONLY a JSON array, no prose and no markdown fences:
[{{"description": "<short PR title>", "domain": "<service name>", \
"provisions": ["<id>"], "factors": ["<fact>"], "contest_to": 1, \
"author": "<a plausible handle>"}}]
"""


# --- job state: one run at a time, process-wide ---------------------------
_lock = threading.Lock()
_job: dict = {"state": "idle"}


def enabled() -> bool:
    return os.environ.get("DJ_SIMULATOR") == "1"


def status() -> dict:
    with _lock:
        return dict(_job)


def _set(**kw) -> None:
    with _lock:
        _job.update(kw)


# --- the model call -------------------------------------------------------
def _call(prompt: str, api_key: str, timeout: float) -> list:
    body = json.dumps({
        "model": MODEL, "max_tokens": 4000, "temperature": 1,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=body,
        headers={"content-type": "application/json", "x-api-key": api_key,
                 "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read())
    text = "".join(b.get("text", "") for b in data.get("content", [])
                   if b.get("type") == "text").strip()
    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    out = json.loads(text)
    return out if isinstance(out, list) else []


# --- what the company will actually accept --------------------------------
def constitution_for(svc, org: str | None) -> tuple[list[dict], set[str]]:
    """The live provisions and factor vocabulary for one tenant.

    Read from the enacted constitution rather than from the pack on disk, so
    a generated scenario is measured against the rulebook the container is
    actually running — amendments included.
    """
    rb = svc.constitution.current_version()
    provisions, vocab = [], {"compliant"}
    for p in svc.constitution.list_provisions(rb):
        if org and p.get("organization") not in (None, org):
            continue
        policy = json.loads(p["policy_source"]) if isinstance(
            p["policy_source"], str) else p["policy_source"]
        triggers = list(policy.get("deny_if_any") or [])
        vocab.update(triggers)
        provisions.append({"provision_id": p["provision_id"],
                           "absolute": bool(p["absolute"]),
                           "text": p["text"], "triggers": triggers})
    return provisions, vocab


def _vocabulary(svc, org, provisions) -> set[str]:
    """Trigger facts plus the mitigating facts already seen in this tenant's
    jurisprudence — the premises of its existing holdings."""
    from . import db as dbmod
    vocab = {"compliant"}
    for p in provisions:
        vocab.update(p["triggers"])
    sql = "SELECT premise, facts FROM precedent_record"
    args = ()
    if org:
        sql += " WHERE organization = ?"
        args = (org,)
    for row in dbmod.open_reader().execute(sql, args).fetchall():
        vocab.update(json.loads(row["premise"]))
        vocab.update(json.loads(row["facts"]))
    return vocab


# --- validation: the model may not widen the world ------------------------
def validate(raw: list, provisions: list[dict], vocab: set[str],
             k: int) -> tuple[list[dict], list[str]]:
    known = {p["provision_id"] for p in provisions}
    kept, dropped = [], []
    for i, s in enumerate(raw):
        if not isinstance(s, dict):
            dropped.append(f"item {i}: not an object")
            continue
        provs = [p for p in (s.get("provisions") or [])
                 if p in known or p == "constitution"]
        if not provs:
            dropped.append(f"{s.get('description', i)!r}: no known provision")
            continue
        facts = [f for f in (s.get("factors") or []) if f in vocab]
        if not facts:
            dropped.append(f"{s.get('description', i)!r}: no known facts")
            continue
        try:
            depth = max(1, min(int(s.get("contest_to", 1)), k))
        except (TypeError, ValueError):
            depth = 1
        kept.append({
            "id": f"GEN-{uuid.uuid4().hex[:8]}",
            "category": "generated",
            "description": str(s.get("description") or "generated change")[:160],
            "domain": str(s.get("domain") or "org")[:60],
            "author": str(s.get("author") or "agent:generated")[:60],
            "provisions": provs,
            "factors": sorted(set(facts)),
            "contest_to": depth,
            # Deliberately absent: no `expect`. The architecture decides.
        })
    return kept, dropped


# --- filing a generated change through the real intake --------------------
def _delivery(case: dict, org: str | None, seq: int) -> bytes:
    return json.dumps({
        "action": "submit",
        # A distinct repository prefix so a generated change is never mistaken
        # for a case-study one in the ledger or the change stream.
        "repository": {"full_name": f"generated/{case.get('domain') or 'org'}"},
        "pull_request": {
            "number": 20000 + seq,
            "title": case["description"],
            "body": f"Model-generated scenario {case['id']}. Facts proposed by"
                    f" {MODEL}; the disposition is this system's own.",
            "labels": [], "base": {"ref": "main"},
            "head": {"sha": f"{abs(hash(case['id'])) % (16 ** 40):040x}"},
            "user": {"login": case.get("author", "agent:generated")},
        },
        "dj_simulation": {
            "factors": case["factors"], "provisions": case["provisions"],
            "organization": org,
            "scope": ({} if (case.get("domain") or "org") == "org"
                      else {"service": case["domain"]}),
        },
        "dj_options": {"escalation": "manual"},
    }).encode()


def _run(svc, company: str, org: str | None, n: int, api_key: str,
         challenger: str) -> None:
    from .kernel import KernelError
    from .inbound_github import InboundError

    run_id = uuid.uuid4().hex[:8]
    timeout = float(os.environ.get("DJ_SIMULATOR_TIMEOUT_S", "90"))
    try:
        provisions, _ = constitution_for(svc, org)
        if not provisions:
            raise RuntimeError(f"no provisions found for tenant {company!r}")
        vocab = _vocabulary(svc, org, provisions)
        plist = "\n".join(
            f"  {p['provision_id']}{' [ABSOLUTE]' if p['absolute'] else ''}:"
            f" {p['text']}\n    triggers: {p['triggers'] or 'none'}"
            for p in provisions)
        cats = "\n".join(f"  - {c}" for c in CATEGORIES)

        made, dropped_all, seq = [], [], 0
        while len(made) < n:
            want = min(BATCH, n - len(made))
            _set(state="generating", made=len(made), target=n,
                 phase=f"asking {MODEL} for {want} more")
            raw = _call(PROMPT.format(
                company=company, provisions=plist,
                vocabulary=json.dumps(sorted(vocab)), n=want,
                categories=cats), api_key, timeout)
            kept, dropped = validate(raw, provisions, vocab, 4)
            dropped_all += dropped
            if not kept:
                raise RuntimeError(
                    "the model returned nothing usable — every proposal "
                    "referenced facts or clauses this company does not have")
            made += kept
        made = made[:n]

        _set(state="adjudicating", made=len(made), target=n,
             phase="filing through the real intake")
        filed, tally = 0, {}
        for case in made:
            headers = {"x-github-event": "simulator",
                       "x-github-delivery": f"sim-{run_id}-{case['id']}"}
            try:
                out = svc.gateway.receive(headers,
                                          _delivery(case, org, seq))
                seq += 1
                sid = out.get("session_id")
                if sid:
                    _contest(svc.gateway, sid, case, challenger)
                    view = svc.gateway.session_view(sid)
                    d = view.get("disposition") or "unknown"
                    tally[d] = tally.get(d, 0) + 1
                    filed += 1
            except (InboundError, KernelError) as e:
                dropped_all.append(f"{case['id']}: refused at intake — {e}")
            _set(filed=filed)

        _set(state="done", filed=filed, made=len(made), dispositions=tally,
             dropped=dropped_all[:20], dropped_count=len(dropped_all),
             finished_at=time.strftime("%H:%M:%S"),
             phase=f"{filed} generated changes are now in the docket")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError,
            RuntimeError, KeyError, ValueError) as e:
        _set(state="failed", error=f"{type(e).__name__}: {e}", phase="failed")


def _contest(gw, session_id: str, case: dict, challenger: str) -> None:
    """Replay how hard the generated author pushed back."""
    from .inbound_github import InboundError
    from .kernel import KernelError
    view = gw.session_view(session_id)
    for _ in range(max(0, case.get("contest_to", 1) - 1)):
        if view.get("disposition") != "blocked_challengeable":
            return
        try:
            view = gw.challenge(session_id, challenger,
                                f"generated scenario {case['id']}: contested")
        except (InboundError, KernelError):
            return


def start(svc, company: str, org: str | None, n: int,
          challenger: str) -> dict:
    """Begin a run. Returns immediately; poll `status()`.

    Called from exactly one place: the admin screen's Generate button.
    """
    if not enabled():
        raise RuntimeError("the simulator is disabled (set DJ_SIMULATOR=1)")
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise RuntimeError(
            "live generation needs ANTHROPIC_API_KEY. There is deliberately "
            "no fallback: a corpus labelled 'generated' that was quietly "
            "produced by the oracle would be a lie in the ledger.")
    with _lock:
        if _job.get("state") in ("generating", "adjudicating"):
            raise RuntimeError("a generation run is already in progress")
        _job.clear()
        _job.update({"state": "generating", "company": company, "org": org,
                     "target": n, "made": 0, "filed": 0, "model": MODEL,
                     "phase": "starting"})
    n = max(1, min(int(n), MAX_PER_RUN))
    threading.Thread(target=_run,
                     args=(svc, company, org, n, api_key, challenger),
                     daemon=True).start()
    return status()
