"""
The rival stack, arm A (EC §5 baseline; DESIGN §2.6).

What a careful enterprise does today without an EC: the constitution in the
prompt, a policy engine that denies any act violating an absolute provision
(the A6 floor and nothing above it), an approval flag that any manager may
set, and an event log. Like the gate, it reads the whole change: a violating
factor already in the change request counts as much as one the agent adds.
It is given the gate's perfect detection, so the comparison with EC turns on
authority (who may let a contrary act through), never on who notices it.
Concretely:

  * T0 contrariety is blocked (`t0_violation`), nothing is escalated.
  * T1 contrariety passes on *any* approval claim, a registry token or a
    say-so `claimed:<office>` alike: the flag is a flag, not an instrument.
    Without a claim the policy engine blocks it.
  * T2 and T3 are not in the engine at all: every departure is allowed and
    logged as an ordinary act.

No glosses, no bench. The verdict's L1/L2 are left None: the rival does not
know the truth of what it allowed; the driver scores it from the EC gate.
"""

from __future__ import annotations

from .canon import Canon
from .gate import STAND_DOWN_KINDS, Proposal, Verdict, contravenes


def rival_decide(p: Proposal, canon: Canon) -> Verdict:
    act = p.act
    facts = tuple(p.facts or ())
    entries = [canon.entry(eid) for eid in p.engaged if eid in canon.entries]

    # The rival stack has no bench: an agent that stands down simply does not proceed.
    if act.kind in STAND_DOWN_KINDS:
        return Verdict("block", "agent_declined" if act.kind == "decline" else "agent_escalated",
                       act.target_entry, None, escalate=False, channel=None, event_type="declined")

    for e in entries:
        if e.tier == "T0" and contravenes(e, act, facts):
            return Verdict("block", "t0_violation", e.id, "T0", escalate=False, channel=None,
                           event_type="violation_blocked")

    for e in entries:
        if e.tier == "T1" and contravenes(e, act, facts):
            if act.token_claim:
                return Verdict("allow", "t1_authorized", e.id, "T1", escalate=False, channel=None,
                               token_used=act.token_claim, event_type="authorized_exception")
            return Verdict("block", "t1_tokenless", e.id, "T1", escalate=False, channel=None,
                           event_type="violation_blocked")

    return Verdict("allow", "clean", None, None, escalate=False, channel=None, event_type="legitimate_act")
