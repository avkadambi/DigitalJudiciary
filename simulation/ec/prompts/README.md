# Governance seat prompts

One system text per seat and prompt style (governance build v3, §3.2 R4):

- `<seat>.canon.md` — the registered style. The seat is given the company's
  rules, approvals and precedents in plain language and decides as an office
  holder would. These files never describe the order of the code's checks, a
  data structure or a code identifier; EC-22 fails the build if one does.
- `<seat>.procedural.md` — the upper-bound comparison: the decision procedure
  the deterministic code follows, step by step.
- `stances.md` — the fixed preambles of the three L2 panel seats.

Seats: `conscience`, `office`, `auditor`, `judge` (L1, L2 panel, L3), `prosecutor`,
`clerk`, `lawmaker`, `l4_proxy`. Every file here is covered by the plan hash and
its sha256 is recorded in each governed run's manifest.
