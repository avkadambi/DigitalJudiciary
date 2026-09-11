"""Arm C — human review, priced. Estimation-only.

Chapter 6 scopes the human comparison as estimation-only and this module
keeps to that: it makes NO decisions, so it can never be scored on
consistency, floors or accuracy, and it consumes no model call. What it
produces is a cost and a workload for a human exception-review desk that
adjudicates every arrival on its own merits with the rulebook in hand and
no case base — the third arm the simulation is asked to price, beside the
judiciary (arm B) and the monolith (arm A).

Every number here is a PARAMETER with a stated basis, not a measurement.
The programme's provenance marks apply: the per-1,000 figure this module
prints is ⟦derived⟧ from ⟦PROJECTED⟧ inputs, and it is replaced wholesale
when the SECOND_LABELLER_PROTOCOL runs on a stratified subsample and gives a
measured minutes-per-decision. Presenting the output as an observed cost of
human review is fabrication under the programme's standing rule; the JSON
carries the whole assumption register beside the number so that no reader
can take one without the other.

The model, in one paragraph. A first-line reviewer reads every arrival:
base minutes plus a per-rule and per-fact increment. A change that touches an
absolute provision, or that edits the policy repository, gets a supervisor's
second read because in a real desk those are the ones nobody signs alone. A
contested arrival (contest_to >= 2) goes to a senior reviewer; one that
exhausts the ladder (contest_to >= 4) reaches the risk owner. A sampled
fraction of first-line decisions is re-read for quality. Minutes are priced
at loaded hourly rates per tier. Turnaround is queue time, not work time,
and is reported separately because the two are routinely conflated.

What it deliberately does NOT model: a human with a searchable precedent
index (that is B_mem with a person in the loop, not arm C), learning effects
across the stream, fatigue, or any consistency figure. The dissertation's
projected like-case consistency for a human panel (91.2% on 60 intact pairs,
⟦PROJECTED⟧) is quoted in the register as a prior and nothing more.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# The assumption register. Change these; the code will not stop you, but
# the JSON will say what you used.
# --------------------------------------------------------------------------

DEFAULT_PARAMS = {
    "minutes": {
        # first-line read of any arrival, before rules and facts are counted
        "base": 12.0,
        # per engaged provision the reviewer has to read and apply
        "per_rule": 4.0,
        # per recorded factor the reviewer has to check against the change
        "per_fact": 1.5,
        # supervisor second read when an absolute provision is engaged or the
        # change is to the policy repository
        "second_read_floor_or_control_plane": 15.0,
        # senior reviewer on a contested arrival (contest_to >= 2)
        "senior_on_contest": 25.0,
        # risk owner on an exhausted ladder (contest_to >= 4)
        "riskowner_on_exhaustion": 30.0,
        # rationale write-up, every arrival (R2: rationale at decision time)
        "write_up": 6.0,
    },
    # fraction of first-line decisions re-read by a second first-line reviewer
    "qa_sample_fraction": 0.10,
    # loaded hourly cost, USD, by tier
    "hourly_usd": {
        "first_line": 55.0,
        "senior": 95.0,
        "riskowner": 160.0,
    },
    # median queue turnaround per arrival, business hours; work time is separate
    "turnaround_hours": {
        "uncontested": 8.0,
        "contested": 30.0,
        "exhausted": 72.0,
    },
    "basis": {
        "hourly_usd": ("Loaded cost = wage x 1.4 overhead. Wage anchors: US BLS OES "
                       "compliance officers (SOC 13-1041) and compliance managers "
                       "(11-9199 subset) median annual wages, May 2025 release, and a "
                       "senior risk officer at a regulated firm. Directionally "
                       "supported, not verified against a 2026 release. ⟦PROJECTED⟧"),
        "minutes": ("Protocol expectation for a compliance exception desk reading a "
                    "pull request against a written rulebook; no measured "
                    "minutes-per-decision exists in the programme yet. The "
                    "SECOND_LABELLER_PROTOCOL's timed subsample replaces these. "
                    "⟦PROJECTED⟧"),
        "turnaround_hours": ("Queue time, business hours. The dissertation's projected "
                             "median for the expert panel is 3.1 days per case "
                             "(Chapter 6, ⟦PROJECTED⟧); a staffed desk is faster than a "
                             "panel and slower than a model. ⟦PROJECTED⟧"),
        "consistency_prior": ("Not simulated. Dissertation Chapter 6 projects 91.2% "
                              "like-case consistency for a human panel on 60 intact "
                              "pairs, ⟦PROJECTED⟧, with the caveat that cross-expert "
                              "figures are inter-rater agreement, not consistency."),
        "comparison": ("Dissertation Chapter 6 projects ~$18,000 per 1,000 cases for the "
                       "expert panel, extrapolated with no stated rate or minutes basis; the "
                       "desk model here lands higher because it prices a rationale write-up, a "
                       "supervisor second read on floors, and QA sampling, none of which the panel "
                       "figure includes. Neither is a measurement."),
        "tripwire": ("Replace every minutes and hourly figure with the measured values "
                     "from the timed labelling subsample before any per-1,000 cost is "
                     "quoted beside a measured machine-arm cost."),
    },
}


def _tier_minutes(case, params, provisions):
    m = params["minutes"]
    rules = case.get("rules", [])
    facts = [f for f in case.get("facts", []) if not f.startswith(("ctx_observation_", "mk_rec_"))]
    first = m["base"] + m["per_rule"] * len(rules) + m["per_fact"] * len(facts) + m["write_up"]
    touches_floor = any(pid in provisions and provisions[pid].absolute for pid in rules)
    second = m["second_read_floor_or_control_plane"] if (touches_floor or case.get("control_plane")) else 0.0
    contest = int(case.get("contest_to", 0) or 0)
    senior = m["senior_on_contest"] if contest >= 2 else 0.0
    risk = m["riskowner_on_exhaustion"] if contest >= 4 else 0.0
    return first, second, senior, risk, contest


def estimate(stream, ref_traces, provisions, params=None):
    """Price a human desk over the stream. Returns a dict for the results JSON."""
    p = params or DEFAULT_PARAMS
    tot = {"first_line": 0.0, "senior": 0.0, "riskowner": 0.0}
    decisions = {"first_line": 0, "senior": 0, "riskowner": 0}
    turnaround = []
    n = 0
    for case in stream:
        first, second, senior, risk, contest = _tier_minutes(case, p, provisions)
        qa = first * p["qa_sample_fraction"]
        tot["first_line"] += first + second + qa
        decisions["first_line"] += 1
        if senior:
            tot["senior"] += senior
            decisions["senior"] += 1
        if risk:
            tot["riskowner"] += risk
            decisions["riskowner"] += 1
        t = p["turnaround_hours"]
        turnaround.append(t["exhausted"] if contest >= 4 else t["contested"] if contest >= 2 else t["uncontested"])
        n += 1
    cost = sum(tot[k] / 60.0 * p["hourly_usd"][k] for k in tot)
    per_k = cost / n * 1000 if n else 0.0
    minutes_per_arrival = sum(tot.values()) / n if n else 0.0
    turnaround.sort()
    med = turnaround[len(turnaround) // 2] if turnaround else 0.0
    # B7: human decisions per 1,000 under the judiciary are the risk-owner
    # acceptances the reference run actually produced; under arm C every
    # arrival is a human decision.
    b_human = sum(1 for t in ref_traces.values() if t.get("escalated_to") == "riskowner")
    return {
        "arm": "C",
        "label": "Human review desk — every arrival read against the rulebook, no case base (estimation-only)",
        "mode": "estimation",
        "provenance": "⟦derived⟧ from ⟦PROJECTED⟧ parameters; see basis",
        "arrivals": n,
        "cost_usd": round(cost, 2),
        "cost_per_1000_usd": round(per_k, 2),
        "minutes_per_arrival": round(minutes_per_arrival, 1),
        "reviewer_hours": {k: round(v / 60.0, 1) for k, v in tot.items()},
        "human_decisions": decisions,
        "human_decisions_per_1000": round(sum(decisions.values()) / n * 1000, 1) if n else 0.0,
        "arm_B_human_decisions_per_1000_reference": round(b_human / n * 1000, 1) if n else 0.0,
        "median_turnaround_hours": med,
        "consistency": None,
        "consistency_note": p["basis"]["consistency_prior"],
        "params": {k: v for k, v in p.items() if k != "basis"},
        "basis": p["basis"],
    }


def summarise(est):
    return (f"  {'human':20} {'C':6} decisions {sum(est['human_decisions'].values()):>7,}  "
            f"min/arrival {est['minutes_per_arrival']:5.1f}  "
            f"${est['cost_usd']:>10,.2f}   (estimation-only; ⟦PROJECTED⟧ inputs)")
