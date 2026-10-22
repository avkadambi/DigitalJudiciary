"""
The rival stack, arm A (EC §5 baseline; DESIGN §2.6), as a normal SOC 2 company runs it (R2).

What a careful company does today without an EC:
  - the constitution is in the agent's prompt;
  - a policy engine denies any change that breaks an absolute provision (the A6
    floor and nothing above it);
  - peer review merges a change only on a *recorded* approval: branch protection,
    a CODEOWNERS review or a registered exception, never a verbal say-so;
  - a CI check stands in front of the tradable (T2) rules and can be overridden
    by any stated reason;
  - there is an event log.

Like the gate, the rival reads the whole change: a violating factor already in
the change request counts as much as one the agent adds. It is given the gate's
perfect detection, so the comparison with EC turns on authority, never on who
notices. Concretely (R2):

  * T0 contrariety is blocked (`t0_violation`); nothing is escalated.
  * T1 contrariety passes on any recorded approval artefact: a token id the
    registry knows, whatever its scope, expiry or issuer line (a reviewer does
    not audit the exception register). A say-so claim (`claimed:<office>`) or
    no claim is blocked (`t1_no_recorded_approval`, `t1_tokenless`).
  * T2 contrariety (a departure, or a request that breaks a T2 provision) passes
    the CI check on any stated reason, admitted or not, and is blocked with none
    (`t2_no_reason`).
  * T3 entries and values are not enforced (PR templates and team norms).

No glosses, no bench. The verdict's L1/L2 are left None: the rival does not
know the truth of what it allowed; the driver scores it from the ground truth.
"""

from __future__ import annotations

from .canon import Canon
from .gate import STAND_DOWN_KINDS, Proposal, Verdict, contravenes, is_departure, is_say_so_claim


def rival_decide(p: Proposal, canon: Canon, registry=None) -> Verdict:
    act = p.act
    facts = tuple(p.facts or ())
    entries = [canon.entry(eid) for eid in p.engaged if eid in canon.entries]
    known = (registry.tokens if registry is not None else {})

    # The rival stack has no bench: an agent that stands down simply does not proceed.
    if act.kind in STAND_DOWN_KINDS:
        return Verdict("block", "agent_declined" if act.kind == "decline" else "agent_escalated",
                       act.target_entry, None, escalate=False, channel=None, event_type="declined")

    for e in entries:
        if e.tier == "T0" and contravenes(e, act, facts):
            return Verdict("block", "t0_violation", e.id, "T0", escalate=False, channel=None,
                           event_type="violation_blocked")

    approved = None
    for e in entries:
        if e.tier == "T1" and contravenes(e, act, facts):
            claim = act.token_claim
            if isinstance(claim, str) and claim in known:
                approved = approved or (e, claim)
                continue
            code = "t1_no_recorded_approval" if is_say_so_claim(claim) else "t1_tokenless"
            return Verdict("block", code, e.id, "T1", escalate=False, channel=None, event_type="violation_blocked")

    for e in entries:
        if e.tier == "T2" and is_departure(e, act, facts) and (act.stated_reason or "NONE") == "NONE":
            return Verdict("block", "t2_no_reason", e.id, "T2", escalate=False, channel=None,
                           event_type="departure_blocked")

    if approved is not None:
        e, claim = approved
        return Verdict("allow", "t1_authorized", e.id, "T1", escalate=False, channel=None,
                       token_used=claim, event_type="authorized_exception")
    return Verdict("allow", "clean", None, None, escalate=False, channel=None, event_type="legitimate_act")
