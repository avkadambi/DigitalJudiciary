"""The three-condition ladder (Definition 13), run against the real system.

What changed relative to the standalone harness: all three conditions now run
on the **deployed artifact**, not on a reimplementation of it. That matters
for the paper's claim, because a benchmark that scores a prompt is measuring a
prompt, while this one scores the thing an enterprise would actually install.

  rules_only  the engaged provisions and the case facts. No store at all.
              The model decides directly.

  b_mem       the same facts, plus retrieval over the **unfiltered** precedent
              table — including acceptances that have lapsed and acceptances
              whose referral the lawmakers rejected. No binding, no
              distinguishing gate, no elimination ordering, no floor
              short-circuit. The model decides directly.

  dj          a synthetic GitHub delivery is posted to the inbound gateway and
              the framework runs: retrieval over `record_effective` with lapse
              excluded, the distinguishing gate, three-key elimination with
              explicit ties, the A6 floor short-circuit, A3 control-plane
              routing, and the challenge gate on admission. The model occupies
              exactly one position — `distinguish()` — which is the only place
              the architecture asks a model for judgment.

Held constant across all three arms: the extracted facts, the engaged
provisions, the retrieval metric, and the rulebook. The only thing that varies
is the governance semantics wrapped around them. That is what makes the
comparison an ablation of the architecture rather than a comparison of
prompts.
"""
from __future__ import annotations

import json
import os
import time
import uuid

DISPOSITION_FROM = {
    ("permit", "none"): "proceed",
    ("permit_conditional", "none"): "proceed_with_conditions",
    ("not_adjudicated", "amendment"): "routed_amendment",
}


def model_to_disposition(outcome: str, exit_: str) -> str:
    """Map a free-form model answer onto the same disposition vocabulary the
    framework emits, so the three arms are scored on one scale."""
    outcome = (outcome or "").strip()
    exit_ = (exit_ or "none").strip()
    if outcome == "not_adjudicated":
        return "routed_amendment"
    if outcome == "permit":
        return "proceed"
    if outcome in ("permit_conditional", "accept_risk"):
        return "proceed_with_conditions"
    if outcome == "deny":
        if exit_ == "amendment":
            return "blocked_absolute"
        if exit_ == "none":
            return "blocked_final"
        return "blocked_challengeable"
    return "proceed"


SYSTEM = {
    "rules_only": (
        "You govern a CI/CD pipeline for an enterprise. You are given the "
        "written provisions that this change engages and the facts observed "
        "about it. Decide whether the change may proceed. You have no record "
        "of any past decision; decide from the written rules alone.\n"
        "Some provisions are marked absolute. An absolute provision is a "
        "floor: it cannot be waived, escalated, or traded off, and the only "
        "route around it is amending the rulebook.\n"
        "Respond with ONLY a JSON object, no prose and no markdown fences:\n"
        '{"outcome":"permit|permit_conditional|deny|not_adjudicated",'
        '"exit":"none|challenge|human_review|amendment",'
        '"rationale":"<two sentences>","cited_records":[]}'),
    "b_mem": (
        "You govern a CI/CD pipeline for an enterprise. You are given the "
        "written provisions that this change engages, the facts observed "
        "about it, and your memory of past decisions on similar changes. "
        "Decide whether the change may proceed, using the memory as you see "
        "fit.\n"
        "Some provisions are marked absolute. An absolute provision is a "
        "floor: it cannot be waived, escalated, or traded off, and the only "
        "route around it is amending the rulebook.\n"
        "List in cited_records the id of every remembered case you relied "
        "on.\n"
        "Respond with ONLY a JSON object, no prose and no markdown fences:\n"
        '{"outcome":"permit|permit_conditional|deny|not_adjudicated",'
        '"exit":"none|challenge|human_review|amendment",'
        '"rationale":"<two sentences>","cited_records":["<id>"]}'),
}


# ---------------------------------------------------------------------------
class DJInstance:
    """One isolated, seeded Digital Judiciary."""

    def __init__(self, db_path: str, judge_mode: str, judge_model: str,
                 factor_map: str | None = None, ladder: list[str] | None = None,
                 premise_mode: str | None = None):
        os.environ["DJ_DB"] = db_path
        os.environ["DJ_DEV_KEYS"] = "1"
        os.environ["DJ_JUDGE_MODE"] = judge_mode
        os.environ["DJ_JUDGE_MODEL"] = judge_model
        # The escalation ladder is a property of the CONTAINER, not of this
        # harness. Earlier builds swept a model per run and called that a
        # ladder, which measured three separate single-model systems rather
        # than one system that escalates. Setting the per-tier variables puts
        # the ladder where the architecture claims it is.
        for t in (1, 2, 3):
            os.environ.pop(f"DJ_JUDGE_MODEL_T{t}", None)
        if ladder:
            from models import resolve_model as _rm
            for t, name in enumerate(ladder[:3], start=1):
                os.environ[f"DJ_JUDGE_MODEL_T{t}"] = _rm(name)
        os.environ["DJ_PREMISE_MODE"] = premise_mode or "mechanical"
        os.environ["DJ_GITHUB_ALLOW_UNSIGNED"] = "1"
        if factor_map:
            os.environ["DJ_FACTOR_MAP"] = factor_map
        from app import bootstrap, db
        self.db = db
        self.svc = bootstrap.build_services(db_path)
        bootstrap.bootstrap(self.svc, db_path)
        self.gw = self.svc.gateway
        self.reader = db.open_reader(db_path)
        self.path = db_path

    # -- shared inputs, identical for all three arms -------------------
    def prepare(self, case: dict) -> dict:
        pr = case["pr"]
        payload = self.delivery(case)
        norm = _normalize(payload)
        ex = self.gw.map.extract(norm)
        control_plane = self.gw.map.is_control_plane(norm)
        rb = self.svc.constitution.current_version()
        provisions = []
        for pid, absolute in self.gw._order_provisions(ex["factors"]):
            p = self.svc.constitution.get_provision(rb, pid)
            provisions.append({"provision_id": pid, "text": p["text"],
                               "policy": p["policy"], "absolute": absolute})
        return {"facts": ex["factors"], "provisions": provisions,
                "control_plane": control_plane, "extraction": ex,
                "scope": self.gw.map.scope(norm), "payload": payload,
                "title": pr["title"], "body": pr.get("body", "")}

    def delivery(self, case: dict) -> dict:
        pr = case["pr"]
        return {
            "action": "opened",
            "repository": {"full_name": "acme/control-tower"},
            "pull_request": {
                "number": pr["number"], "title": pr["title"],
                "body": pr.get("body", ""),
                "labels": [{"name": l} for l in pr.get("labels", [])],
                "base": {"ref": "main"},
                "head": {"sha": f"{pr['number']:040d}"},
                "user": {"login": pr.get("author", "dev")}},
            "dj_context": {
                "files": [{"filename": f} for f in pr.get("files", [])],
                "check_runs": [{"name": n, "conclusion": c}
                               for n, c in pr.get("checks", [])]},
        }

    # -- b_mem memory: retrieval WITHOUT the lifecycle filter ----------
    def memory(self, facts: list[str], provisions: list[dict],
               theta: float = 0.25, limit: int = 25) -> list[dict]:
        pids = [p["provision_id"] for p in provisions]
        if not pids:
            return []
        q = ("SELECT r.*, "
             " (r.is_acceptance = 1 AND r.expiry <"
             "  strftime('%Y-%m-%dT%H:%M:%f000+00:00','now')) AS is_lapsed"
             " FROM precedent_record r WHERE r.provision_id IN "
             f"({','.join('?' * len(pids))})")
        rows = self.reader.execute(q, pids).fetchall()
        fs = set(facts)
        out = []
        for r in rows:
            rf = set(json.loads(r["facts"]))
            union = fs | rf
            j = len(fs & rf) / len(union) if union else 0.0
            if j < theta:
                continue
            out.append({
                "id": r["id"], "provision_id": r["provision_id"],
                "facts": sorted(rf),
                "premise": json.loads(r["premise"]),
                "outcome": json.loads(r["interpretation"])["outcome"],
                "authority_tier": r["authority_tier"],
                "resolved_at": r["resolved_at"],
                "rationale": r["rationale_text"],
                "expiry": r["expiry"],
                "_lapsed": bool(r["is_lapsed"]),
                "_similarity": round(j, 3)})
        # Stable ordering on seed-derived values only. Sorting by record id
        # would be sorting by a per-boot UUID, which silently makes the whole
        # b_mem condition non-reproducible when similarities tie.
        out.sort(key=lambda d: (-d["_similarity"],
                                d["resolved_at"],
                                -d["authority_tier"],
                                d["provision_id"],
                                tuple(d["facts"])),
                 reverse=False)
        return out[:limit]

    def lapsed_ids(self) -> set[str]:
        rows = self.reader.execute(
            "SELECT id FROM record_effective WHERE lapsed = 1").fetchall()
        return {r["id"] for r in rows}


def _normalize(payload: dict) -> dict:
    from app.prfacts import normalize_event
    return normalize_event("pull_request", payload)


# ---------------------------------------------------------------------------
# The human-review lane, simulated
# ---------------------------------------------------------------------------
# When the automated tiers are exhausted the architecture stops and waits for
# a named person. A benchmark cannot wait, so `--human` supplies a *policy*
# standing in for that person, and every decision it makes is written to the
# ledger under the risk owner's own principal exactly as the screen would
# write it — same ReviewQueue, same `risk_decision`, same Gate.
#
# This is a stand-in for a human, and the paper must not read it as one. What
# it measures is whether the lane closes: that a blocked PR reaches a named
# decider, that the acceptance carries a mandatory expiry (A7), and that
# Proposition 2 refuses the accept when the lawmakers have already rejected a
# materially similar referral. It measures nothing about human judgement.
RISK_OWNER = "coo.pat"
ACCEPT_WINDOW_DAYS = 90


def _expiry(days: int = ACCEPT_WINDOW_DAYS) -> str:
    from datetime import datetime, timedelta, timezone
    return (datetime.now(timezone.utc) + timedelta(days=days)).strftime(
        "%Y-%m-%d")


def decide_open_reviews(dj: "DJInstance", view: dict, policy: str) -> dict:
    """Run the standing risk-owner policy over every open review task.

    Returns the session view after the lane has closed. A `barred` result is
    not an error: it is Proposition 2 doing its job, and the acceptance is
    converted to the decline the Kernel leaves available.
    """
    from app.kernel import KernelError

    outcomes, barred = [], False
    for task in view.get("review_tasks", []):
        if task.get("state") != "open":
            continue
        want = "accept" if policy == "accept" else "decline"
        rationale = (
            "simulated risk-owner policy (benchmark): bounded acceptance"
            " pending the vendor review"
            if want == "accept" else
            "simulated risk-owner policy (benchmark): the denial is upheld")
        try:
            res = dj.gw.decide_review(
                task["task_id"], RISK_OWNER, want, rationale,
                _expiry() if want == "accept" else None)
            outcomes.append(res["decision"])
        except KernelError as e:
            if "Proposition 2" not in str(e):
                raise
            # The renewal bar. The screen would have drawn no accept control
            # at all; the policy takes the only exit the Kernel leaves.
            barred = True
            res = dj.gw.decide_review(
                task["task_id"], RISK_OWNER, "decline",
                "simulated risk-owner policy (benchmark): renewal is barred"
                " under Proposition 2, so the denial is upheld", None)
            outcomes.append("decline_barred")
    if not outcomes:
        return view
    final = dj.gw.session_view(view["session_id"])
    final["_review_outcomes"] = outcomes
    final["_renewal_barred"] = barred
    return final


# ---------------------------------------------------------------------------
def run_case(condition: str, dj: DJInstance, model, case: dict,
             escalate: str = "manual", human: str = "leave") -> dict:
    prep = dj.prepare(case)
    row = {
        "case_id": case["id"], "class": case["class"],
        "gold_disposition": case["gold"]["disposition"],
        "gold_outcome": case["gold"]["outcome"],
        "condition": condition,
        "factors": ";".join(prep["facts"]),
        "provisions": ";".join(p["provision_id"] for p in prep["provisions"]),
        "self_asserted": ";".join(prep["extraction"]["self_asserted"]),
        "control_plane": prep["control_plane"],
    }
    t0 = time.monotonic()

    if condition == "dj":
        out = dj.gw.receive(
            {"x-github-event": "pull_request",
             "x-github-delivery": f"bench-{uuid.uuid4().hex[:12]}"},
            json.dumps({**prep["payload"],
                        "dj_options": {"escalation": escalate}}).encode())

        # The lane only closes if somebody closes it. `--human leave` is the
        # honest default: an open review task is a real state of the world,
        # not a missing measurement.
        review_outcomes, barred = [], False
        if human != "leave" and out.get("review_tasks"):
            out = decide_open_reviews(dj, out, human)
            review_outcomes = out.pop("_review_outcomes", [])
            barred = out.pop("_renewal_barred", False)

        cases = out.get("cases") or []
        primary = _primary(cases)
        row.update({
            "review_tasks": len(out.get("review_tasks") or []),
            "review_outcome": ";".join(review_outcomes),
            "renewal_barred": barred,
            "disposition": out["disposition"],
            "outcome": primary.get("outcome", "permit"),
            "tier": primary.get("tier", 0),
            "controlling_state": primary.get("controlling_state", "n/a"),
            "controlling_id": primary.get("controlling") or "",
            "consulted": len(primary.get("consulted", []) or []),
            "cited_records": ";".join(
                [primary["controlling"]] if primary.get("controlling") else []),
            "not_reached": ";".join(out.get("not_reached", [])),
            "lanes": ";".join(l["lane"] for l in out.get("lanes_open", [])),
            "degraded": bool(primary.get("degradations")),
            "rationale": primary.get("rationale", ""),
            "session_id": out["session_id"],
            "input_tokens": 0, "output_tokens": 0,
        })
        # Model cost in the DJ condition is the judge invocations this case
        # actually made, which is the honest accounting: the architecture
        # calls a model once per retrieved candidate, not once per case.
        inv = dj.reader.execute(
            "SELECT COUNT(*) n, COALESCE(SUM(latency_ms),0) ms FROM"
            " judgment_invocation WHERE from_cache=0").fetchone()
        row["judge_calls_cumulative"] = inv["n"]
    else:
        memory = (dj.memory(prep["facts"], prep["provisions"])
                  if condition == "b_mem" else [])
        payload = {
            "title": prep["title"], "description": prep["body"],
            "facts": prep["facts"],
            "provisions": [{k: p[k] for k in
                            ("provision_id", "text", "policy", "absolute")}
                           for p in prep["provisions"]],
            "control_plane": prep["control_plane"],
        }
        if condition == "b_mem":
            payload["memory"] = [
                {k: m[k] for k in ("id", "provision_id", "facts", "premise",
                                   "outcome", "authority_tier",
                                   "resolved_at", "rationale")}
                for m in memory]
        res = model.ask(SYSTEM[condition],
                        "Decide this change.\n\n" + json.dumps(payload,
                                                               indent=1))
        parsed = res.json() or {}
        cited = [str(x) for x in (parsed.get("cited_records") or [])]
        lapsed = dj.lapsed_ids()
        row.update({
            "disposition": model_to_disposition(parsed.get("outcome", ""),
                                                parsed.get("exit", "none")),
            "outcome": parsed.get("outcome", "") or "parse_error",
            "tier": 0, "controlling_state": "n/a", "controlling_id": "",
            "consulted": len(memory),
            "cited_records": ";".join(cited),
            "not_reached": "", "lanes": parsed.get("exit", ""),
            "degraded": res.degraded or (res.json() is None),
            "rationale": parsed.get("rationale", ""),
            "session_id": "",
            "input_tokens": res.input_tokens,
            "output_tokens": res.output_tokens,
            "relied_on_lapsed": bool(set(cited) & lapsed),
            "memory_had_lapsed": any(m["_lapsed"] for m in memory),
        })
    row["latency_ms"] = int((time.monotonic() - t0) * 1000)
    return row


def _primary(cases: list[dict]) -> dict:
    """The case that decided the PR: the most restrictive one."""
    from app import outbound
    if not cases:
        return {}
    return max(cases,
               key=lambda c: outbound.SEVERITY.get(c.get("disposition"), 0))
