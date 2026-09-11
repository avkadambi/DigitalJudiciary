#!/usr/bin/env python3
"""Run the demo with a real model at the judge position.

    export ANTHROPIC_API_KEY=sk-ant-...        # once, in your shell profile
    python3 demo/run_live.py                   # sonnet at every tier
    python3 demo/run_live.py --ladder          # haiku / sonnet / opus by tier
    python3 demo/run_live.py --estimate        # what it would cost, no calls

=== The key ===

Read from the environment, never from an argument and never from a file in
the repository. A key on the command line lands in your shell history and in
the process list, where every other user on the machine can read it; a key in
a file gets committed. This script therefore has no --api-key flag, on
purpose. If you want it persistent, put the export in ~/.zshrc or ~/.bashrc.

=== What "live" changes ===

Only one thing: who answers the distinguishing question. Everything else —
retrieval, ordering, the floors, the tiers, the ledger — is unchanged and
still deterministic. The model is asked whether a precedent's holding rests
on something the present case lacks, and nothing else. It never decides an
outcome.

With --ladder, each tier gets its own model, so a challenge is genuinely
re-asked by a more capable judge rather than replaying the tier below.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Rates in dollars per million tokens. Checked against current pricing when
# this was written; they move, so --estimate prints them rather than hiding
# them, and DJ_PRICE_IN / DJ_PRICE_OUT override.
RATES = {
    "claude-haiku-4-5":  (1.00, 5.00),
    "claude-sonnet-4-6": (3.00, 15.00),
    "claude-opus-4-5":   (15.00, 75.00),
}
LADDER = ("claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-5")

# Measured from oracle runs of the sctower corpus: ~1.3 paid judge calls per
# scenario after the verdict cache, at roughly 600 in / 60 out per call.
CALLS_PER_SCENARIO = 1.3
TOK_IN, TOK_OUT = 600, 60


def estimate(scenarios: int, ladder: bool, model: str) -> None:
    print(f"\n  Estimate for {scenarios} scenarios")
    print(f"  {'~calls':>10}  {'model':22s} {'in $/M':>8} {'out $/M':>8}"
          f" {'≈ cost':>9}")
    total = 0.0
    if ladder:
        # Most cases settle at the first look; escalation is rare. These
        # shares come from the demo corpus and are indicative, not a promise.
        shares = ((0, 0.80), (1, 0.14), (2, 0.06))
        for idx, share in shares:
            m = LADDER[idx]
            calls = scenarios * CALLS_PER_SCENARIO * share
            i, o = RATES.get(m, (3.0, 15.0))
            cost = calls * (TOK_IN / 1e6 * i + TOK_OUT / 1e6 * o)
            total += cost
            print(f"  {calls:10.0f}  {m:22s} {i:8.2f} {o:8.2f} {cost:9.4f}")
    else:
        calls = scenarios * CALLS_PER_SCENARIO
        i, o = RATES.get(model, (3.0, 15.0))
        total = calls * (TOK_IN / 1e6 * i + TOK_OUT / 1e6 * o)
        print(f"  {calls:10.0f}  {model:22s} {i:8.2f} {o:8.2f} {total:9.4f}")
    print(f"\n  ≈ ${total:.2f} total. Rough: real prompts vary, the verdict")
    print("  cache absorbs repeats, and a re-run against the same database")
    print("  pays only for questions it has not already asked.\n")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Run the demo with a live model judging. The API key is"
                    " read from ANTHROPIC_API_KEY and is never accepted as an"
                    " argument.")
    ap.add_argument("--company", default="sctower",
                    help="corpus to seed (default sctower; _all is 4x the"
                         " cost)")
    ap.add_argument("--ladder", action="store_true",
                    help="haiku at tier 1, sonnet at tier 2, opus at tier 3 —"
                         " escalation buys a more capable judge")
    ap.add_argument("--model", default="claude-sonnet-4-6",
                    help="single model for every tier (ignored with --ladder)")
    ap.add_argument("--quorum-top", type=int, default=0,
                    help="sample a pivotal verdict N times at tier 3 —"
                         " escalation buys deliberation instead of capability")
    ap.add_argument("--premise", action="store_true",
                    help="also ask the model which facts a holding rests on"
                         " (DJ_PREMISE_MODE=judged)")
    ap.add_argument("--limit", type=int, default=25,
                    help="seed only the first N scenarios. Defaults to 25,"
                         " not the whole corpus: live calls are sequential,"
                         " so 100 scenarios is several minutes of waiting."
                         " Pass --limit 0 for everything")
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--db", default=os.environ.get("DJ_DB", "/tmp/dj.db"))
    ap.add_argument("--estimate", action="store_true",
                    help="print the likely cost and exit without calling"
                         " anything")
    a = ap.parse_args()

    scenarios = a.limit or (400 if a.company == "_all" else 100)
    # Roughly 1.3 paid calls per scenario, each a sequential round trip.
    minutes = scenarios * CALLS_PER_SCENARIO * 3.0 / 60

    if a.estimate:
        estimate(scenarios, a.ladder, a.model)
        return 0

    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("""
  ANTHROPIC_API_KEY is not set.

    export ANTHROPIC_API_KEY=sk-ant-...

  Get one from console.anthropic.com/settings/keys — the Console is a
  separate account from claude.ai, and needs billing set up before a key
  will work. Put the export in your shell profile rather than typing it on
  the command line, where it lands in your shell history.

  There is deliberately no --api-key flag: an argument is visible in the
  process list to every other user on the machine.
""", file=sys.stderr)
        return 2
    if not key.startswith("sk-ant-"):
        print(f"  ANTHROPIC_API_KEY does not look like an Anthropic key"
              f" (starts {key[:7]!r}). Check for a stray copy-paste.",
              file=sys.stderr)
        return 2

    env = dict(os.environ)
    env["DJ_JUDGE_MODE"] = "llm"
    if a.ladder:
        for i, m in enumerate(LADDER, start=1):
            env[f"DJ_JUDGE_MODEL_T{i}"] = m
        env.pop("DJ_JUDGE_MODEL", None)
    else:
        env["DJ_JUDGE_MODEL"] = a.model
        for i in (1, 2, 3):
            env.pop(f"DJ_JUDGE_MODEL_T{i}", None)
    if a.quorum_top:
        env["DJ_QUORUM_T3"] = str(a.quorum_top)
    if a.premise:
        env["DJ_PREMISE_MODE"] = "judged"
    # A live call is slower than the oracle by orders of magnitude; the
    # default 20s starts timing out under a full corpus replay, and a
    # timeout degrades silently rather than failing.
    env.setdefault("DJ_JUDGE_TIMEOUT_S", "60")

    print(f"\n  Live judging — key ending {key[-4:]}, {scenarios} scenarios")
    if a.ladder:
        for i, m in enumerate(LADDER, start=1):
            print(f"    tier {i}: {m}")
        print("    tier 4: a named person — no model")
    else:
        print(f"    every tier: {a.model}")
    if a.quorum_top:
        print(f"    tier 3 samples each pivotal verdict"
              f" {a.quorum_top} times")
    if a.premise:
        print("    the model also proposes what each holding rests on")
    estimate(scenarios, a.ladder, a.model)
    print(f"  Seeding calls the API once per candidate, sequentially, so"
          f" expect roughly\n  {minutes:.0f} minute(s) before the server"
          f" starts. Progress prints every 5 scenarios;\n  if it stops"
          f" moving for more than a minute, that is a real stall.\n")
    print("  Ctrl-C is safe: the ledger is written as it goes.\n")

    cmd = [sys.executable, os.path.join(HERE, "relaunch.py"),
           "--company", a.company, "--port", str(a.port), "--db", a.db]
    if a.limit:
        cmd += ["--limit", str(a.limit)]
    rc = subprocess.call(cmd, cwd=ROOT, env=env)
    if rc != 0:
        return rc

    print(f"""
  Check what actually judged — do not trust the flag:

    sqlite3 {a.db} "SELECT tier, judge_version, COUNT(*), SUM(degraded)
                     FROM judgment_invocation GROUP BY 1,2"

  You want llm:<model>, not oracle-premise-subset-1.0. Watch the degraded
  column: a timeout or a parse failure falls back rather than failing, so a
  network problem looks like a clean run with quietly worse verdicts.

  Analytics now shows real tokens and real cost per tier, which the oracle
  reports as zero by construction.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
