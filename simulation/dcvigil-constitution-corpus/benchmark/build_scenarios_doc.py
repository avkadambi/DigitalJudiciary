"""Write docs/DISCRIMINATING_SCENARIOS.md from the scenario definitions.

The document is generated, not typed, so it cannot drift from the suite. It
carries the three tiers, the PACT finding each family is built from, the
architectural mechanism that decides it, and the offline result table produced
by `run.py --discriminating`.
"""

import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "harness"))

import engine  # noqa: E402
import discriminating as disc  # noqa: E402

RB = json.load(open(os.path.join(ROOT, "constitution", "rulebook.json")))
PROV = {p["id"]: engine.Provision.from_dict(p) for p in RB["provisions"]}
BOUND = disc.resolve(PROV)

PACK = json.load(open(os.path.join(ROOT, "corpus", "cases.json")))
PACK = {k: v for k, v in PACK.items() if k != "cases"}
ORG = (PACK.get("display_name") or PACK.get("pack") or "the pack").split(" — ")[0]


def para(t):
    return " ".join(t.split())


def run_suite():
    cmd = [sys.executable, os.path.join(HERE, "run.py"), "--discriminating",
           "--mode", "oracle", "--arms", "B,A,A+,B_mem,B_gov", "--models", "haiku"]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, timeout=900)
    return p.stdout


def main():
    out = io.StringIO()
    w = out.write
    tiers = disc.tiers()
    w(f"# Discriminating scenarios — {ORG}\n\n")
    w(para(disc.__doc__.split("\n\n", 1)[1].split("Three tiers")[0]) + "\n\n")
    w("## The three tiers\n\n")
    w("| tier | claim | families |\n|---|---|---|\n")
    w("| structural | the monolith cannot get this right in principle: what it would "
      "need is state, and no larger context window supplies it | "
      + ", ".join(tiers.get("structural", [])) + " |\n")
    w("| measured | it could in principle; PACT measures that it frequently does not, "
      "and a better model narrows it | " + ", ".join(tiers.get("measured", [])) + " |\n")
    w("| adverse | the architecture does no better, or worse; reported for the same "
      "reason as the rest | " + ", ".join(tiers.get("adverse", [])) + " |\n\n")
    w(para("""The tier is the load-bearing part of this document. A benchmark that
    reports only the families its subject wins is an advertisement. Five of the eight
    here are structural, two are measured, and one is a loss stated as a loss."""))
    w("\n\n")
    w("## Why PACT cannot pose these\n\n")
    w(para("""PACT (Okamoto & Erol 2026) evaluates a single agent against a single rule
    over one or two turns with nothing carried between items: 3,364 items, 48
    scenarios, 12 domains, nine pressure mechanisms, six axes. It is precise about
    what it measures. What it cannot measure is drift, because drift is a property of
    a sequence and PACT has no store, no clock, no ordering rule and no standing
    declaration. Each family below is built from exactly what PACT lacks, and each
    one is a sequence rather than an item — which is where compliance failure
    actually lives in a deployed system."""))
    w("\n\n---\n\n")

    for tier in ("structural", "measured", "adverse"):
        w(f"## {tier.capitalize()}\n\n")
        for s in disc.SCENARIOS:
            if s["tier"] != tier:
                continue
            w(f"### {s['id']} — {s['title']}\n\n")
            pid = BOUND[s["id"]]
            w(f"**Provision engaged:** `{pid}` — {PROV[pid].title}")
            if s.get("repeat", 1) > 1:
                w(f" · **arrivals:** {s['repeat']} co-pending, one consolidation signature")
            if s.get("pressure"):
                w(f" · **pressure:** {s['pressure']}")
            if s.get("guard"):
                w(" · **guard item:** the rule does not apply; permitting is correct")
            w("\n\n")
            w("**The PACT finding it is built from.** " + para(s["pact_hook"]) + "\n\n")
            key = ("why_structural" if "why_structural" in s else
                   "why_measured" if "why_measured" in s else "why_adverse")
            label = {"why_structural": "Why the monolith cannot close this",
                     "why_measured": "Why this is a measured gap, not a structural one",
                     "why_adverse": "Why the architecture does not win this"}[key]
            w(f"**{label}.** " + para(s[key]) + "\n\n")
            exp = s["dj_expected"]
            exp_txt = ("no single disposition: the representative decides and the "
                       "eleven members are disposed by citation" if exp is None else
                       "a TIE, referred rather than resolved" if exp == "none_tie" else
                       f"`{exp}`")
            w(f"**The architecture is expected to answer:** {exp_txt}\n\n")
            w("**The monolith trap.** " + para(s["monolith_trap"]) + "\n\n")
            w("_The trap is a prediction, not a score. `--mode live` is what settles it._\n\n")

    w("---\n\n## Running the suite\n\n")
    w("```\npython3 benchmark/run.py --discriminating --mode oracle "
      "--arms B,A,A+,B_mem,B_gov --models haiku\n```\n\n")
    w(para("""Two readers are available offline, and the distinction matters more than
    it looks. Under `--oracle-reader perfect` every arm is answered by a reasoner that
    applies the gate and the ordering itself — which hands the monolith arms the
    architecture's own work for free, so every arm agrees and the table shows nothing.
    Under `--oracle-reader naive` (the default for this suite) arm B is decided by the
    engine and the arms nothing binds are read by a stand-in for three behaviours PACT
    measures: recency taken for supersession, a recorded clearance taken at face value,
    and similarity taken for premise containment. That stand-in is not a model and is
    not evidence about one. It is a lower bound that makes the manipulation visible
    without spending a cent; `--mode live` is what produces a claim."""))
    w("\n\n")
    w(para("""One fairness correction is worth naming because it changed the result.
    The monolith arms retrieve on coverage alone. An earlier version routed them
    through the engine's own `retrieve`, which drops records whose acceptance has
    expired — handing them the lapse clock, which is one of the mechanisms under
    test. A retrieval index over an exception log has no expiry semantics: it returns
    the approval, and the approval does not say it is dead. With that corrected, S1
    separates; before it, it did not."""))
    w("\n\n### Offline result\n\n```\n")
    txt = run_suite()
    i = txt.find("scenario ")
    w(txt[i:].rstrip() if i >= 0 else txt.rstrip())
    w("\n```\n")
    path = os.path.join(ROOT, "docs", "DISCRIMINATING_SCENARIOS.md")
    open(path, "w").write(out.getvalue())
    print("wrote", path, len(out.getvalue()), "bytes")


if __name__ == "__main__":
    main()
