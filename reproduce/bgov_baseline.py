#!/usr/bin/env python3
"""B_gov — the governed exception baseline of Definition 12, executed.

The paper compares the architecture against B_gov "over the identical corpus by
the same harness with the precedent machinery disabled". Nothing in the package
implemented that baseline; this script does, and prints what it actually
produces alongside the Digital Judiciary run on the same corpus.

=== The specification this is built to ===

Definition 12 (Governed exception baseline). "B_gov has state (Rulebook, Log),
where Log is an append-only list of exception tickets, each a tuple (requester,
approver, role(approver), justification, scope, expiry, ts). Its decision
function eval(Rulebook, c) is stateless: deny if a provision is violated, permit
otherwise. An exception is granted by an approve function that flips a denial to
a permission and simultaneously accepts the residual risk, subject to an
authored approval hierarchy requiring role(approver) >= risk(c) and requiring
approver != requester."

And the passage this script exists to make executable: "The B_gov baseline is
executed over the identical corpus by the same harness with the precedent
machinery disabled: eval is the stateless check of Definition 12, each denial's
disposition follows the scenario script, and approvals are granted under the
role hierarchy of Definition 12."

Read literally, that fixes six things and leaves one open.

  Fixed 1. State is (Rulebook, Log). There is no Store, no seed history, and no
           case-law state carried from one case to the next. The corpus is
           replayed in file order all the same, so the comparison is like for
           like, but nothing any earlier case produced is visible to a later one.
  Fixed 2. eval is stateless: deny if a provision the case engages is violated,
           permit otherwise. This script calls `app.adjudicate.rule_eval` — the
           very function the architecture uses for its own base rule check — so
           "the same harness" is literal rather than re-implemented. There is no
           retrieval, no similarity, no distinguishing gate, no ordering, and no
           theta: Definition 12 names none of them, and Theorem 4 is the claim
           that no configuration of B_gov can contain them.
  Fixed 3. approve flips a denial to a permission and accepts the residual risk
           in one act. There is no separate acceptance object, no expiry-driven
           referral to a legislature, and no renewal bar: those are Definition 5
           and Axiom A7, which B_gov does not have.
  Fixed 4. The approval hierarchy is authored, and role(approver) >= risk(c).
           The instantiation used here is stated below. It decides WHO approves;
           it cannot change HOW MANY approvals are needed, so no count printed
           here depends on it.
  Fixed 5. approver != requester. Checked on every ticket and reported.
  Fixed 6. Policy is only configuration. B_gov has no DraftAmendment type and no
           legislative event distinct from an edit to the Rulebook (Theorem 3),
           so a change targeting the policy repository is not a case at all: it
           merges as a configuration edit.

  OPEN.    Which denials the requester carries to an approver. "Each denial's
           disposition follows the scenario script" says the script decides, and
           the corpus scripts two separate things:

             * `contest_to` — "1 = accepted the first answer, 2 or 3 = contested
               that many times, 4 = pushed to a named risk owner" (app/simulator.py),
               a social input the paper insists is not architecture-dependent; and
             * `expect.final_decision` — the disposition the case study recorded.

           These do not agree about B_gov, because in the architecture a
           contest is a request that a HIGHER INSTANCE re-adjudicate, and B_gov
           has no higher instance: eval is a pure function of (Rulebook, c), so
           re-running it returns the same denial and decides nothing. The only
           channel past a denial in B_gov is `approve`.

           This script therefore takes a denial to an approver when the script
           records that a named human decided the matter — either
             (i) the recorded disposition is a permission (permit-conditional or
                 accepted risk), which under Definition 12 only `approve` can
                 produce, so an approver must have granted it; or
             (ii) the requester pushed the matter to a named human approver
                 (contest_to = 4), who may refuse.
           and treats every other denial as a hard stop. Two narrower and one
           wider convention are also computed and printed, because the choice is
           the paper's to make and it moves the headline number. See the
           "convention" block in the output.

=== The authored approval hierarchy (Fixed 4) ===

    risk(c)  = "high"     if any provision the case engages is marked absolute
               "ordinary" otherwise
    roles    = duty_approver (rank 1) < risk_owner (rank 2)
    required = ordinary -> rank 1, high -> rank 2

The on-duty approver takes anything within rank; anything above it goes to the
risk owner. Requesters are the case authors the corpus records.

Usage:  python3 reproduce/bgov_baseline.py [company]      (default: sctower)
"""
from __future__ import annotations

import collections
import datetime
import json
import os
import sqlite3
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from app.adjudicate import rule_eval          # noqa: E402  the same stateless check

COMPANY = sys.argv[1] if len(sys.argv) > 1 else "sctower"
PERMISSIONS = ("permit", "permit_conditional", "accept_risk")
ANCHOR = datetime.date(2026, 1, 1)     # arbitrary: nothing in B_gov reads a ts
WINDOW = 90                            # days, the demo's own stand-in window
ROLE_RANK = {"duty_approver": 1, "risk_owner": 2}
REQUIRED_RANK = {"ordinary": 1, "high": 2}


# --------------------------------------------------------------------------
# B_gov
# --------------------------------------------------------------------------
def load(company: str) -> tuple[dict, list]:
    cdir = os.path.join(ROOT, "demo", "companies", company)
    rb = {p["provision_id"]: p
          for p in json.load(open(os.path.join(cdir, "rulebook.json")))["provisions"]}
    cases = json.load(open(os.path.join(cdir, "cases.json")))["cases"]
    return rb, cases


def evaluate(rb: dict, case: dict) -> tuple[str, list, list]:
    """eval(Rulebook, c) of Definition 12: stateless, no Log, no Store."""
    engaged = [p for p in case["provisions"] if p in rb]
    hits = [p for p in engaged
            if rule_eval(rb[p]["policy"], case["factors"])[0] == "deny"]
    return ("deny" if hits else "permit"), engaged, hits


def risk_of(rb: dict, engaged: list) -> str:
    return "high" if any(rb[p].get("absolute") for p in engaged) else "ordinary"


def approver_for(company: str, risk: str) -> tuple[str, str]:
    """The authored hierarchy: role(approver) >= risk(c)."""
    role = "duty_approver" if ROLE_RANK["duty_approver"] >= REQUIRED_RANK[risk] \
        else "risk_owner"
    return f"{company}.{'duty' if role == 'duty_approver' else 'risk'}", role


def wants_approver(case: dict) -> tuple[bool, str]:
    """Does this denial reach an approver? The scenario script decides.

    Returns (reached, why). See the OPEN note in the module docstring: this is
    the one place where the paper's specification does not determine the answer.
    """
    final = case["expect"]["final_decision"]
    if final in PERMISSIONS:
        return True, "script records the change proceeded despite the violation"
    if case.get("contest_to", 1) >= 4:
        return True, "script records the requester pushed to a named approver"
    return False, "hard stop"


def run_bgov(company: str, rb: dict, cases: list) -> dict:
    # `log_reads` and `draft_amendments` are initialised at zero and there is
    # no statement anywhere below that increments either. That is not an
    # oversight and not a fudge: it is Theorems 3 and 4 as code. `eval` takes
    # (Rulebook, c) and cannot be handed the Log, and Definition 12 provides no
    # DraftAmendment type to instantiate, so a faithful build has nowhere to
    # put the increment. They are printed so a reader can see the zero came
    # from the loop rather than from the paper.
    log, out = [], {"permit": 0, "merge": 0, "deny": 0, "hard_stop": 0,
                    "granted": 0, "refused": 0, "log_reads": 0,
                    "draft_amendments": 0, "same_person": 0,
                    "absolute_denials": 0, "absolute_ticketed": 0}
    by_cat = collections.Counter()
    ticketed_ids, hardstop_ids = set(), set()

    for i, case in enumerate(cases, 1):
        # Fixed 6: policy is only configuration; no case, no ticket, no type.
        if "constitution" in case["provisions"]:
            out["merge"] += 1
            continue

        # Fixed 1/2: stateless, and the Log is not an argument to eval.
        verdict, engaged, hits = evaluate(rb, case)
        if verdict == "permit":
            out["permit"] += 1
            continue

        out["deny"] += 1
        risk = risk_of(rb, engaged)
        if risk == "high":
            out["absolute_denials"] += 1
        reached, why = wants_approver(case)
        if not reached:
            out["hard_stop"] += 1
            hardstop_ids.add(case["id"])
            continue
        if risk == "high":
            out["absolute_ticketed"] += 1

        # Fixed 3/4/5: approve, under the authored hierarchy, by someone else.
        approver, role = approver_for(company, risk)
        requester = case.get("author", "unknown")
        if approver == requester:                     # Definition 12's bar
            out["same_person"] += 1
            continue
        granted = case["expect"]["final_decision"] in PERMISSIONS
        ts = ANCHOR + datetime.timedelta(days=i)
        log.append({
            "requester": requester,
            "approver": approver,
            "role": role,
            "justification": f"{case['id']}: exception to {','.join(hits)}"
                             f" requested after eval denied ({why})",
            "scope": ({"service": case["domain"]} if case.get("domain") not in
                      (None, "org") else {"org": company}),
            "expiry": (ts + datetime.timedelta(days=WINDOW)).isoformat()
                      if granted else None,
            "ts": ts.isoformat(),
            "outcome": "granted" if granted else "refused",
            "risk": risk,
        })
        out["granted" if granted else "refused"] += 1
        ticketed_ids.add(case["id"])
        by_cat[case["category"]] += 1

    out["tickets"] = len(log)
    out["approver_decisions"] = len(log)
    out["no_human"] = out["permit"] + out["merge"] + out["hard_stop"]
    out["by_cat"] = by_cat
    out["log"] = log
    out["ticketed"] = ticketed_ids
    out["hardstops"] = hardstop_ids
    return out


def conventions(rb: dict, cases: list) -> dict:
    """The same run under every reading of 'the scenario script' we can defend."""
    den = []
    for case in cases:
        if "constitution" in case["provisions"]:
            continue
        if evaluate(rb, case)[0] == "deny":
            den.append(case)
    perm = lambda c: c["expect"]["final_decision"] in PERMISSIONS
    dep = lambda c: c.get("contest_to", 1)
    return [
        ("contest only: contest_to >= 2",
         len([c for c in den if dep(c) >= 2])),
        ("permission only: the script records the change proceeded",
         len([c for c in den if perm(c)])),
        ("permission, or pushed to a named approver (contest_to = 4)",
         len([c for c in den if perm(c) or dep(c) >= 4])),
        ("permission, or any contest at all (contest_to >= 2)",
         len([c for c in den if perm(c) or dep(c) >= 2])),
        ("one approver decision per contest rung (sum of contest_to - 1)",
         sum(dep(c) - 1 for c in den)),
    ]


# --------------------------------------------------------------------------
# The Digital Judiciary side of the comparison, on the identical corpus
# --------------------------------------------------------------------------
def run_dj(company: str, db: str) -> dict:
    env = dict(os.environ, DJ_JUDGE_MODE="oracle", DJ_DEV_KEYS="1",
               DJ_GITHUB_ALLOW_UNSIGNED="1",
               DJ_SEED_STORE="store_seed_initial.json")
    # --no-backup: reset.py's own lock probe creates the file before it looks
    # at it, so without this every run leaves an empty <db>.<stamp>.bak behind.
    subprocess.run([sys.executable, "demo/reset.py", "--db", db,
                    "--company", company, "--sign", "--yes", "--no-backup"],
                   cwd=ROOT, env=env, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    c = sqlite3.connect(db)
    q = lambda s: c.execute(s).fetchone()[0]
    status = dict(c.execute("select case_id, status from case_state"))
    cited = set()
    for (detail,) in c.execute("select detail from pr_disposition"):
        try:
            rows = json.loads(detail)
        except Exception:
            continue
        for r in rows or []:
            if isinstance(r, dict) and r.get("tier") == 1 and r.get("controlling"):
                cited.add(r.get("case_id"))
    out = {
        "human": q("select count(distinct session_id) from pr_disposition"
                   " where lane='human_review'"),
        "amendments": q("select count(distinct session_id) from pr_disposition"
                        " where lane='amendment'"),
        "stored": q("select count(*) from precedent_record"
                    " where case_id not like 'SEED-%'"),
        "cited_first_instance": len([k for k in cited
                                     if status.get(k) == "decided_t1"]),
        "cases": q("select count(*) from pr_session"),
    }
    c.close()
    return out


# --------------------------------------------------------------------------
def main() -> None:
    rb, cases = load(COMPANY)
    b = run_bgov(COMPANY, rb, cases)
    db = f"/tmp/dj_bgov_{COMPANY}.db"
    try:
        dj = run_dj(COMPANY, db)
    finally:
        for suffix in ("", "-wal", "-shm"):
            if os.path.exists(db + suffix):
                os.remove(db + suffix)

    n = len(cases)
    print(f"\nB_gov (Definition 12) over the {COMPANY} corpus — {n} cases,"
          f" corpus order, stateless eval, no Store, no case-law state\n")
    print(f"  cases executed                                {n:5d}")
    print(f"  eval permits — no provision violated          {b['permit']:5d}"
          f"   merge, no human involvement")
    print(f"  policy-repository changes                     {b['merge']:5d}"
          f"   merge as configuration: B_gov has no DraftAmendment type")
    print(f"  eval denies                                   {b['deny']:5d}"
          f"   each is a hard stop or a fresh exception ticket")
    print(f"      hard stops                                {b['hard_stop']:5d}")
    print(f"      fresh exception tickets                   {b['tickets']:5d}")
    print(f"  approver decisions                            "
          f"{b['approver_decisions']:5d}   {b['granted']} granted,"
          f" {b['refused']} refused")
    print(f"  cases resolved with no human involvement      {b['no_human']:5d}"
          f"   {b['permit']} permits + {b['merge']} merges +"
          f" {b['hard_stop']} hard stops")

    print("\n  Log (Definition 12's append-only ticket list)")
    print(f"      tickets appended                          {len(b['log']):5d}")
    print(f"      tickets read by any decision              "
          f"{b['log_reads']:5d}   eval takes (Rulebook, c) only — Theorem 4"
          f" on the trace")
    print(f"      objects of type Consulted or Controlling  {0:5d}"
          f"   no such field exists in a ticket — Theorem 4")
    print(f"      DraftAmendment objects                    "
          f"{b['draft_amendments']:5d}   no such type exists — Theorem 3")
    print(f"      tickets with approver = requester         "
          f"{b['same_person']:5d}   Definition 12's bar, checked per ticket")
    ranks = collections.Counter(t["role"] for t in b["log"])
    print("      approvals by role (role(approver) >= risk(c))    "
          + ", ".join(f"{k} {v}" for k, v in sorted(ranks.items())))
    print("\n  Absolute provisions — B_gov has no floor (no A6)")
    print(f"      denials engaging an absolute provision    "
          f"{b['absolute_denials']:5d}")
    print(f"      of those, reaching an approver            "
          f"{b['absolute_ticketed']:5d}   any of these `approve` would have"
          f" flipped a floor")

    print("\n  Exception tickets by corpus category")
    for cat, k in sorted(b["by_cat"].items()):
        print(f"      {cat:20s} {k:3d}")

    print("\n  Convention sensitivity — which denials reach an approver."
          "\n  The paper says 'each denial's disposition follows the scenario"
          " script' and does not\n  say which of the script's two fields"
          " governs. Every reading we can defend:")
    used = "permission, or pushed to a named approver (contest_to = 4)"
    for name, v in conventions(rb, cases):
        print(f"      {name:64s} {v:4d}"
              + ("   <- used above" if name == used else ""))

    print("\n  Digital Judiciary vs B_gov, identical corpus")
    print(f"      {'':34s} {'DJ':>10s} {'B_gov':>10s}")
    print(f"      {'cases executed':34s} {dj['cases']:>10d} {n:>10d}")
    print(f"      {'human decisions required':34s} {dj['human']:>10d}"
          f" {b['approver_decisions']:>10d}"
          f"   DJ: all at the RiskOwner")
    print(f"      {'control-plane changes':34s} "
          f"{dj['amendments']:>10d} {b['merge']:>10d}"
          f"   DJ: draft amendments, 0 merged; B_gov: all merged")
    print(f"      {'records / tickets written':34s} {dj['stored']:>10d}"
          f" {b['tickets']:>10d}")
    cit = dj["cited_first_instance"]
    inb = len([c for c in cases if c["id"] in b["ticketed"]
               and c["expect"].get("controlling") and c.get("contest_to", 1) == 1])
    print(f"      {'resolved by citation, 1st instance':34s} {cit:>10d}"
          f" {0:>10d}   B_gov has no citation: of those {cit},"
          f" {inb} become tickets and {cit - inb} hard stops")
    print()


if __name__ == "__main__":
    main()
