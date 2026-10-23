You run Registry.decide_requests for one due request, in this order:
1. If a token scoped to the request's entry is in force (not revoked, not consumed, day <= expires_day) -> covered.
2. If the entry does not exist or gloss.codified -> denied_codified.
3. If the reason is not in ADMITTED_REASONS (N, O, K) or evidence_ok is false -> denied_reason.
4. If granted >= EXCEPTIONS_PER_YEAR -> denied_cap.
5. Else granted (an entry-scoped token valid TOKEN_TTL_DAYS).
Answer with one JSON object and nothing else.
