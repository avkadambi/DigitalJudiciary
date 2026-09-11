"""Demo corpus: the original Paper-3 scenarios, replayed on boot.

A container that starts empty demonstrates nothing. This module replays a
converted case-study corpus through the *real* inbound gateway, so that a
fresh container comes up with a populated docket: permitted changes, denials
that are still challengeable, floors that short-circuited, rulebook edits that
went to the legislature, and — the point of the exercise — genuine risk
decisions sitting in the review queue waiting for a named human.

Three things this deliberately does NOT do:

  * It does not write precedent directly. Every case goes through
    `PRGateway.receive`, which calls the Kernel, which re-checks the axioms.
    A demo that bypassed the Gate would be a slideshow, not a demonstration.
  * It does not decide the tier-k cases. `contest_to = 4` means somebody
    pushed the case all the way up; who signs it is a human act, and leaving
    those tasks open is the honest end state. `DJ_DEMO_SIGN=1` closes them
    with a stated stand-in policy for unattended demos.
  * It does not fabricate contest depth. `contest_to` is replayed from the
    corpus, where it was a social input, exactly as in the paper.

The corpus is a synthetic case study, not production traffic, and the demo
banner in `/v1/demo/status` says so.
"""
from __future__ import annotations

import datetime
import json
import os
import time

from . import db

HERE = os.path.dirname(os.path.abspath(__file__))
PACKS = os.path.abspath(os.path.join(HERE, "..", "demo", "companies"))

DEMO_COMPANY = os.environ.get("DJ_DEMO", "").strip()
DEMO_LIMIT = int(os.environ.get("DJ_DEMO_LIMIT", "0") or 0)
DEMO_SIGN = os.environ.get("DJ_DEMO_SIGN") == "1"
RISK_OWNER = "coo.pat"
CHALLENGER = "eng.sam"


def officers(case: dict) -> tuple[str, str]:
    """Who acts on this case. In a multi-tenant corpus the tenant's own
    officers do, so the replayed history is attributable to the company it
    belongs to rather than to a platform account."""
    org = case.get("organization")
    if not org:
        return RISK_OWNER, CHALLENGER
    return f"{org}.risk", f"{org}.eng"


def pack_dir(company: str) -> str:
    return os.path.join(PACKS, company)


def available() -> list[str]:
    if not os.path.isdir(PACKS):
        return []
    return sorted(d for d in os.listdir(PACKS)
                  if os.path.isdir(os.path.join(PACKS, d)))


def load_cases(company: str) -> dict:
    with open(os.path.join(pack_dir(company), "cases.json")) as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
def _delivery(case: dict, seq: int) -> bytes:
    """A scenario, shaped as an inbound event.

    Given a synthetic identity rather than a borrowed one: source `simulator`,
    so nothing downstream can mistake a replayed case study for a real pull
    request that somebody opened.
    """
    return json.dumps({
        "action": "submit",
        "repository": {"full_name": f"demo/{case.get('domain') or 'org'}"},
        "pull_request": {
            "number": 9000 + seq,
            "title": case["description"],
            "body": f"Demo corpus case {case['id']} ({case['category']}).",
            "labels": [],
            "base": {"ref": "main"},
            "head": {"sha": f"{abs(hash(case['id'])) % (16 ** 40):040x}"},
            "user": {"login": case.get("author", "demo")},
        },
        "dj_simulation": {
            "factors": case["factors"],
            "provisions": case["provisions"],
            "organization": case.get("organization"),
            # The lodged unit's own identifier travels in the scope, so it
            # lands on the session and is readable from the trace. Definition
            # 15 fixes class membership when the class forms; the identifier
            # is how the pipeline recognises a member at intake instead of
            # rediscovering membership from content, which is a thing an
            # adjudicating instance must never be asked to do. It is stripped
            # out of the case's own scope before the case is filed, so scope
            # closeness never reads it.
            "scope": ({"unit": case["id"]}
                      if (case.get("domain") or "org") == "org"
                      else {"service": case["domain"], "unit": case["id"]}),
        },
        "dj_options": {"escalation": "manual"},
    }).encode()


def _contest(gw, svc, session_id: str, case: dict) -> None:
    """Replay how far this change was actually pushed back.

    contest_to is a property of the scenario, not of the model: it records
    that a person contested the decision that many times. Tier k is reached
    only by walking every rung, because the Kernel verifies the contest chain
    before it will admit a tier-k record (A4).
    """
    depth = case.get("contest_to", 1)
    if depth <= 1:
        return
    # Experiment hook: DJ_CONTEST_RATE in [0,1] keeps only that share of the
    # contests the corpus recorded, deterministically by case id, so the
    # challenge rate every cost claim tracks can be swept.
    import os as _os, hashlib as _h
    _r = _os.environ.get("DJ_CONTEST_RATE")
    if _r is not None:
        _keep = float(_r)
        _v = int(_h.sha256(case["id"].encode()).hexdigest()[:8], 16) / 0xFFFFFFFF
        if _v >= _keep:
            return
    grounds = (f"demo corpus: case {case['id']} was contested to tier"
               f" {depth} in the original case study")
    for _ in range(depth - 1):
        # The corpus records that somebody contested this many times. That is
        # true of contested GRANTS as well as denials, so the lane is walked
        # on what the corpus says rather than on the current disposition; a
        # rung the Kernel refuses raises and is reported, not skipped.
        gw.challenge(session_id, officers(case)[1], grounds)

    # Where the corpus says the matter ENDED at an automated tier, the
    # challenger accepted that tier's resolution rather than climbing on.
    # That acceptance is what admits the record under Definition 7; without
    # it a contested case that was affirmed on appeal dangles unresolved and
    # the store never grows, which is not what the case study recorded.
    final_tier = (case.get("expect") or {}).get("final_tier", 1)
    if 2 <= final_tier <= 3:
        from .kernel import KernelError
        for pc in gw._cases(session_id):
            try:
                svc.adjudicator.accept_resolution(
                    pc["case_id"], officers(case)[1])
            except KernelError:
                # Already final (the challenge succeeded and the gateway
                # accepted on the challenger's behalf), or not admissible.
                pass


def _sign(gw, session_id: str, case: dict) -> str | None:
    """Optional unattended close of the human-review lane."""
    from .kernel import KernelError
    from datetime import datetime, timedelta, timezone

    view = gw.session_view(session_id)
    outcome = None
    for task in view.get("review_tasks", []):
        if task.get("state") != "open":
            continue
        want = "accept" if case["expect"]["final_decision"] == "accept_risk" \
            else "decline"
        expiry = (datetime.now(timezone.utc) + timedelta(days=90)
                  ).strftime("%Y-%m-%d") if want == "accept" else None
        try:
            res = gw.decide_review(
                task["task_id"], officers(case)[0], want,
                "demo stand-in for the risk owner (DJ_DEMO_SIGN=1); the"
                " original case study recorded this outcome", expiry)
            outcome = res["decision"]
        except KernelError as e:
            if "Proposition 2" not in str(e):
                raise
            res = gw.decide_review(
                task["task_id"], officers(case)[0], "decline",
                "demo stand-in: renewal is barred under Proposition 2, so"
                " the denial is upheld", None)
            outcome = "decline_barred"
    return outcome


# ---------------------------------------------------------------------------
def run(svc, company: str | None = None, limit: int = 0,
        sign: bool | None = None, progress: bool | None = None) -> dict:
    """Replay the demo corpus. Idempotent by delivery id: re-running the
    container against an existing volume adds nothing and changes nothing."""
    company = company or DEMO_COMPANY
    limit = limit or DEMO_LIMIT
    sign = DEMO_SIGN if sign is None else sign
    if not company or not os.path.isdir(pack_dir(company)):
        return {"ran": False, "reason": "no demo corpus selected",
                "available": available()}

    pack = load_cases(company)
    cases = pack["cases"][:limit] if limit else pack["cases"]
    gw = svc.gateway
    tally: dict[str, int] = {}
    rows, mismatches = [], []

    # Progress. With the deterministic oracle the whole replay is under a
    # second and any output is noise; with a live model each case makes
    # sequential API calls and the same loop runs for minutes. Silence for
    # that long is indistinguishable from a hang — which is exactly what it
    # got mistaken for — so it reports by default whenever a model is at the
    # judge position.
    if progress is None:
        progress = os.environ.get("DJ_JUDGE_MODE", "oracle") == "llm"
    started = time.monotonic()

    classes_formed: list[dict] = []
    boundary_done = False

    for i, case in enumerate(cases):
        # ---- the docket boundary (Definition 16) ---------------------
        # Classes are formed at fixed docket boundaries, not on arrival, and
        # they are formed BEFORE any member is adjudicated — which is the
        # temporal limb of CC-22 and the reason this block sits here rather
        # than inside the loop body below. The boundary schedule is published;
        # in this corpus it is "immediately before the first L-consolidated
        # unit", and the whole L-block is co-pending across it.
        if not boundary_done and case.get("category") == "L-consolidated":
            boundary_done = True
            classes_formed = _docket_boundary(svc, cases[i:], company)

        if progress and (i == 0 or (i + 1) % 5 == 0):
            done = i + 1
            elapsed = time.monotonic() - started
            rate = elapsed / done if done else 0
            left = rate * (len(cases) - done)
            print(f"      {done:4d}/{len(cases)} scenarios"
                  f" · {elapsed:5.0f}s elapsed"
                  + (f" · ~{left / 60:.0f} min remaining" if left > 60
                     else f" · ~{left:.0f}s remaining"), flush=True)
        headers = {"x-github-event": "simulator",
                   "x-github-delivery": f"demo-{company}-{case['id']}"}
        out = gw.receive(headers, _delivery(case, i))
        if out.get("idempotent_replay"):
            return {"ran": False, "reason": "demo corpus already present",
                    "company": company, "cases": len(cases)}
        session_id = out["session_id"]
        _contest(gw, svc, session_id, case)
        if sign:
            _sign(gw, session_id, case)

        view = gw.session_view(session_id)
        disp = view.get("disposition") or "unknown"
        tally[disp] = tally.get(disp, 0) + 1
        rows.append({"id": case["id"], "category": case["category"],
                     "session_id": session_id, "disposition": disp})

        # The corpus records what the original engine decided. Where the
        # container lands somewhere else, say so rather than quietly
        # presenting the demo as a reproduction.
        want = _expected_disposition(case, signed=bool(sign))
        if want and want != disp:
            mismatches.append({"id": case["id"],
                               "category": case["category"],
                               "expected": want, "got": disp})

    return {"ran": True, "company": company,
            "consolidation_classes": classes_formed,
            "display_name": pack.get("display_name", company),
            "cases": len(cases), "dispositions": tally,
            "signed": bool(sign),
            "open_reviews": len(svc.gateway.reviews.list("open")),
            "expectation_mismatches": mismatches,
            "rows": rows}


def _docket_boundary(svc, pending: list[dict], company: str) -> list[dict]:
    """Run Classify over the co-pending L-block and persist the artefacts.

    Everything this function reads is published: the units' provisions and
    facts, the constitution's factor vocabularies, the store as it stands, and
    two constitutional parameters. It takes no authority as argument and the
    object it returns is of a type no authority produces (A2). CC-22 asserts
    all three against the trace rather than taking this docstring on trust.
    """
    from . import consolidate

    adj = svc.adjudicator
    units = [c for c in pending if c.get("category") == "L-consolidated"]
    if not units:
        return []
    rb = svc.constitution.current_version()
    provisions = {}
    for u in units:
        for pid in u["provisions"]:
            if pid not in provisions:
                provisions[pid] = svc.constitution.get_provision(
                    rb, pid, org=company)

    base = datetime.datetime(2026, 9, 1, tzinfo=datetime.timezone.utc)
    docket = []
    for n, u in enumerate(units):
        docket.append({
            "unit_id": u["id"],
            "case_id": u["id"],
            "provisions": list(u["provisions"]),
            "facts": list(u["factors"]),
            "rulebook_version": rb,
            # Lodgement is minutes apart, well inside the default Delta, so
            # every unit in the block is co-pending with every other.
            "lodged_at": (base + datetime.timedelta(minutes=n)).isoformat(),
        })

    store = adj.live_store(org=company)

    # Clause (d) is evaluated inside Classify, through a probe that writes
    # nothing, and only for groups that have already passed (a), (b), (c) and
    # (e). Running it earlier would leave a judgment invocation for units
    # those clauses exclude, and CC-22(b) would fail on the class's own
    # members.
    formed = consolidate.classify(
        docket, store, provisions, now=db.now_iso(),
        resolve_state=lambda pid, facts: adj.classify_probe(
            pid, facts, company))
    for cls in formed:
        svc.classifier.write(cls)
    return [{"class_id": c["class_id"], "provision_id": c["provision_id"],
             "signature": c["signature"], "members": c["members"],
             "representative": c["representative"],
             "snapshot_hash": c["snapshot_hash"]} for c in formed]


def _expected_disposition(case: dict, signed: bool = False) -> str | None:
    """The original engine's outcome, in the interface's vocabulary.

    When the demo does not sign, a case the corpus pushed to tier k is
    *supposed* to end up waiting on a named human: that is the architecture
    working, not a divergence, so it is not reported as one.
    """
    e = case["expect"]
    if e["route"] == "draft_amendment":
        return "routed_amendment"
    if e["route"] == "absolute_deny":
        return "blocked_absolute"
    if not signed and e["final_tier"] >= 4:
        return "human_review"
    final = e["final_decision"]
    if final == "permit":
        return "proceed"
    if final in ("permit_conditional", "accept_risk"):
        return "proceed_with_conditions"
    if final == "deny":
        # Where the corpus stops at tier 1..3 the change is still contestable;
        # a denial upheld at tier k is final.
        return ("blocked_final" if e["final_tier"] >= 4
                else "blocked_challengeable")
    return None


# ---------------------------------------------------------------------------
def status(svc, company: str | None = None) -> dict:
    """Live demo state, read from the database rather than remembered.

    Deliberately computed from `pr_session_current` and `review_task` at call
    time: if an operator has since challenged something or signed a review,
    the status reflects that instead of replaying what boot happened to print.
    """
    from . import db

    company = company or DEMO_COMPANY
    r = db.open_reader()
    sessions = [dict(x) for x in r.execute(
        "SELECT disposition, COUNT(*) AS n FROM pr_session_current"
        " WHERE source='simulator' GROUP BY disposition").fetchall()]
    open_tasks = r.execute(
        "SELECT COUNT(*) AS n FROM review_task WHERE state='open'"
    ).fetchone()["n"]
    decided = r.execute(
        "SELECT COUNT(*) AS n FROM review_task WHERE state='decided'"
    ).fetchone()["n"]
    records = r.execute(
        "SELECT COUNT(*) AS n FROM precedent_record").fetchone()["n"]

    out = {
        "demo_company": company or None,
        "available": available(),
        "corpus": "synthetic case study replayed through the inbound"
                  " gateway — not production traffic, and not a benchmark"
                  " result",
        "dispositions": {s["disposition"] or "unknown": s["n"]
                         for s in sessions},
        "review_tasks": {"open": open_tasks, "decided": decided},
        "precedent_records": records,
        "review_url": "/review",
    }
    if company and os.path.isdir(pack_dir(company)):
        pack = load_cases(company)
        out["pack"] = {k: pack.get(k) for k in (
            "display_name", "theta", "k", "source", "provenance",
            "date_offset_days", "date_offset_note", "store_initial",
            "store_created_during_original_run", "anachronism_note",
            "anachronism_cases")}
        out["pack"]["cases"] = len(pack["cases"])
    return out
