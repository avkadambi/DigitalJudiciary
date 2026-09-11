#!/usr/bin/env python3
"""Generate docs/FINTECH_REGULATORY_REGISTER.md from the pack definition.

Generated rather than written, so the register cannot drift from the
constitution it describes. `build_fintech_pack.py` is the single source: if a
provision moves between absolute and adjudicable, or its citation changes,
this file changes with it on the next run.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from build_fintech_pack import PROVISIONS, SEEDS, CASES, KEY, DISPLAY  # noqa

BANDS = [
    ("Absolute floors — no officer may accept these", lambda p: p["absolute"]),
    ("Security and operational resilience",
     lambda p: not p["absolute"] and p["id"].startswith("MF-2")),
    ("AI and model governance",
     lambda p: not p["absolute"] and p["id"].startswith("MF-3")),
    ("Consumer protection",
     lambda p: not p["absolute"] and p["id"].startswith("MF-4")),
]

PREAMBLE = f"""# Regulatory register — {DISPLAY} reference constitution

*Generated from `demo/build_fintech_pack.py`. Do not edit by hand; edit the
pack and re-run `python3 demo/build_fintech_register.py`.*

**Positions stated as of August 2026. This is an engineering artifact, not
legal advice, and not a compliance opinion.** It encodes obligations a firm
can evaluate a *code change* against. It does not cover capital, licensing,
examination readiness, or whether the controls are operated as designed —
and a rulebook that passes review is not the same as a firm that complies.
Have counsel review every provision before it governs anything real.

## How to read the `Decidable by the firm?` column

This is the load-bearing distinction in the whole document, and it is **not**
a severity ranking.

An **absolute** provision is short-circuited at tier 1 by the Kernel (A6). It
can never be risk-accepted, by anyone, at any tier; the only exit is an
amendment passed by the lawmakers. So `absolute` is reserved for obligations
where **no officer of the firm actually holds the authority to accept the
risk** — strict liability, criminal exposure, or a flat statutory
prohibition with no materiality defence.

Everything a regulator would let you document, compensate, and time-box is
deliberately **adjudicable**. Encoding those as absolute would be a lie about
the firm's own authority: it would force routine, defensible exceptions
through constitutional amendment, and a constitution amended weekly is not a
constitution.

If you disagree with where a line sits, move it — but move it deliberately.
Moving a provision *into* absolute removes a power that real officers have.
Moving one *out* grants a power they may not have.

## Sources

Public-domain and publicly published instruments only:

- **EU**: GDPR (Reg. 2016/679), DORA (Reg. 2022/2554) with RTS (EU) 2025/301
  and ITS (EU) 2024/2956, AI Act (Reg. 2024/1689) as amended by the AI
  Omnibus.
- **US federal**: BSA (31 U.S.C. §5318; 31 CFR Part 1020), OFAC (31 CFR
  Ch. V), GLBA Safeguards (16 CFR Part 314), ECOA/Reg. B (12 CFR Part 1002),
  Reg. E (12 CFR Part 1005), TILA/Reg. Z (12 CFR Part 1026), FCRA/Reg. V
  (12 CFR Part 1022), Dodd-Frank §§1031/1033/1036, SOX (15 U.S.C. §7262).
- **Supervisory guidance**: SR 11-7 / OCC 2011-12, Interagency Guidance on
  Third-Party Relationships (88 FR 37920), FFIEC handbooks, CFPB Circulars
  2022-03 and 2023-03.
- **State**: NYDFS 23 NYCRR Part 500, CCPA/CPRA.
- **Standards and industry**: PCI DSS v4.0.1, NIST AI RMF 1.0.
- **AI conduct**: Anthropic, *Claude's Constitution* (January 2026), released
  under CC0 and therefore genuinely public domain.

## Dates that moved recently, and why they matter here

Three positions would be wrong if taken from memory rather than checked:

1. **EU AI Act Omnibus, in force 27 July 2026.** Standalone Annex III
   high-risk obligations moved to **2 December 2027**, and Annex I embedded
   systems to **2 August 2028**. The Art. 5 prohibitions (applicable since
   2 February 2025) and the Art. 50 transparency duties (from 2 August 2026)
   were **not** deferred. This is why MF-107 is absolute and in force while
   MF-304 is a dated readiness provision — and it is exactly the kind of
   split a single "EU AI Act" provision would have flattened and got wrong.
2. **12 CFR Part 1033 is enjoined.** The October 2024 final rule was enjoined
   by the Eastern District of Kentucky in October 2025 and is under CFPB
   reconsideration. MF-405 therefore states its own contested status in the
   provision text and binds on architecture, not on a compliance date.
3. **PCI DSS v4.0.1 and NYDFS MFA are both fully live** — the 51 future-dated
   PCI requirements since 31 March 2025, universal MFA under §500.12 since
   1 November 2025. Neither is a future obligation any more.
"""


def table(rows: list[dict]) -> str:
    out = ["| Provision | Obligation | Instrument | Status | Decidable by "
           "the firm? |",
           "|---|---|---|---|---|"]
    for p in rows:
        short = p["text"].split(" (")[0].rstrip(".")
        if len(short) > 150:
            short = short[:147] + "..."
        verdict = "**No — absolute**" if p["absolute"] else "Yes"
        out.append(f"| `{p['id']}` | {short} | {p['citation']} | "
                   f"{p['status']} | {verdict} |")
    return "\n".join(out)


def rationale_block(rows: list[dict]) -> str:
    out = []
    for p in rows:
        out.append(f"- **`{p['id']}` — {p['regime']}.** {p['why']}")
    return "\n".join(out)


def main() -> None:
    parts = [PREAMBLE]
    for title, pred in BANDS:
        rows = [p for p in PROVISIONS if pred(p)]
        parts.append(f"\n## {title}\n")
        parts.append(table(rows))
        parts.append("\n### Why each sits where it does\n")
        parts.append(rationale_block(rows))

    seeded = sorted({s["provision"] for s in SEEDS})
    unseeded = [p["id"] for p in PROVISIONS
                if not p["absolute"] and p["id"] not in seeded]

    parts.append(f"""

## Seed jurisprudence

{len(SEEDS)} holdings ship with the pack, covering {len(seeded)} of the
{sum(1 for p in PROVISIONS if not p['absolute'])} adjudicable provisions.
Each rests on a **premise** — the facts the holding actually turned on — so a
later change missing one of those facts is *distinguished* rather than
silently permitted. That is the mechanism that stops a precedent from
sprawling beyond the case that produced it.

No holding exists on an absolute provision, and none can: A6 short-circuits
before retrieval ever runs, so there is nothing for a precedent to attach to.

One holding, `MP-023`, is a **lapsed risk acceptance** on `MF-304`. It is
retained rather than deleted because the A7 renewal guard reads it: a later
change on materially similar facts must cite the expired exception instead of
quietly re-accepting the same risk.

Adjudicable provisions with no seeded holding yet — the first case on each
will be decided on the provision text alone, and is the most worth
contesting: {', '.join(f'`{p}`' for p in unseeded) if unseeded else 'none'}.

## Scenario corpus

{len(CASES)} scenarios exercise the constitution end to end. Expectations are
**computed from the documented adjudication semantics** in
`build_fintech_pack.py::solve()` and then verified against a live replay
through the real inbound gateway — none are hand-asserted, and none are
back-filled from whatever the engine happened to do.

| Category | What it demonstrates |
|---|---|
| `A-routine` | Nothing engaged; permitted at tier 1 with no precedent written |
| `B-plain-deny` | Predicate denies, nobody pushes back |
| `C-precedent` | A prior holding is retrieved and followed |
| `D-ordering` | Two holdings apply; authority tier, then recency, decides |
| `E-distinguish` | A holding is retrieved but its premise is not satisfied |
| `F-absolute` | Floor short-circuits at tier 1; amendment is the only exit |
| `G-riskowner` | Contested to tier k; waits for a named human |
| `H-control-plane` | The change targets the rulebook, so it is never judged |
| `J-novel` | Nothing on point; provision applied directly |

## Known limits

- **Scope.** Change-time governance only. Nothing here addresses capital
  adequacy, licensing, chartering, examination management, or whether a
  control is operated as designed once merged.
- **Jurisdiction.** US federal, New York, California, and EU. A firm
  operating under the FCA, MAS, or RBI needs provisions this pack does not
  carry.
- **The factor vocabulary is the weak joint.** A provision only fires when
  the extractor labels a change with the right factor. The rules are only as
  good as `seed/github_factor_map.json`, and mapping these provisions onto
  real CI signals is engineering work this pack does not do.
- **Currency.** Regulation moves. The three dated positions above were
  checked in August 2026 and at least one — Part 1033 — is actively in flux.
""")

    path = os.path.join(ROOT, "docs", "FINTECH_REGULATORY_REGISTER.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write("\n".join(parts) + "\n")
    print(f"  wrote {os.path.relpath(path, ROOT)} "
          f"({len(PROVISIONS)} provisions, {len(SEEDS)} holdings)")


if __name__ == "__main__":
    main()
