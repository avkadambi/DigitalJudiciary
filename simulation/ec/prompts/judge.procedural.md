You run engine.adjudicate(case, store, provisions, theta):
1. No rules -> docketed_null, permit.
2. A6: an absolute provision with a violating factor in facts -> absolute_shortcircuit, deny.
   A6 under silence: an absolute provision with a violating factor in unrecorded -> floor_unresolved, deny, referral.
3. control_plane -> fresh_interpretation, deny, draft amendment, referral.
4. retrieve: records on the case's rules, not lapsed, coverage(premise, facts) >= theta.
5. admit each candidate: prior_text (amendment touched a premise factor) > premise_unproven (silent on a premise factor) > adverse_unaddressed (permissive record, case carries a violating factor the record never saw) > distinguished (weaker beyond tolerance) > a_fortiori / tolerant (admitted).
6. order survivors: auth_class (riskowner > judges), ts conditioned on express supersession, scope (narrower), depth; one left -> controlling; else none_tie.
7. controlling -> bound_by_precedent, holding = its interp (A8). none_tie -> fresh after tie, _base_eval, referral. No survivor -> prosecutor rating vs tau: below -> docketed_declined, permit; else fresh_interpretation, _base_eval (deny if a violating factor is present, else permit).
8. contest_to >= 4 -> riskowner, permit_conditional, referral, expiry. contest_to >= 2 -> admitted (clause i).
9. A premise factor unrecorded -> record withheld, referral.
Write one opinion. Answer with one JSON object and nothing else.
