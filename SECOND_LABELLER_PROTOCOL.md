# Second-labeller protocol

**Written 1 September 2026. Not yet executed — the measurement it specifies is an open item.**

## What needs a second labeller, and what does not

Most of this corpus needs none. Dispositions are produced by a deterministic oracle, conformance is
computed from traces, and the mutation matrix is mechanical. **One thing is authored judgement: the
`expect` blocks** — the route, tier-1 and final decision, controlling record and stored status that
each case asserts *before* the run. Those are the oracle, and they were written by the same authors
who wrote the implementation.

## The sample

Draw **60 cases**, stratified by category, from the 544 across the four executed packs — five from
each of the twelve categories, drawn with a published seed. Sixty is chosen so that a κ of 0.70 has
a 95% interval of roughly ±0.12, which is enough to separate substantial agreement from moderate.

## The instrument

The second labeller receives, per case: the pack's rulebook, the opening store, the case's facts and
provisions, and the scope data. They receive **neither** the `expect` block **nor** any executed
output. They are asked for four fields: route, final decision, the controlling record if any, and
whether the case should be stored.

## The statistic

Report Cohen's κ **per field**, not pooled, with a Wilson interval on each; report the raw agreement
beside it; and publish the confusion matrix. Per-field matters because the fields are not equally
hard — route is nearly mechanical, controlling record is not — and a pooled figure would hide that.

## The tripwire, registered in advance

**If κ on the controlling-record field falls below 0.60, the oracle is not reproducible by an
independent reader and the conformance claims are reported as author-internal.** That is a real
tripwire with a real consequence, and it is registered here so that it cannot be renegotiated after
the number is known.

## Who

Not a co-author. Someone competent to read a rulebook and apply an ordering rule, who has not seen
the implementation. Anyone assessing the work — a reviewer, an examiner — is not the right pool, since
they are assessing it rather than labelling for it.
