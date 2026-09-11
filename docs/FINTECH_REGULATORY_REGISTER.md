# Regulatory register — Meridian Financial reference constitution

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


## Absolute floors — no officer may accept these

| Provision | Obligation | Instrument | Status | Decidable by the firm? |
|---|---|---|---|---|
| `MF-101` | Denied-party and sanctions screening is never bypassed, suppressed, allow-listed, or served from a cache older than 24 hours on any payment, onboar... | 31 CFR Ch. V (OFAC); IEEPA, 50 U.S.C. §1701 | in force | **No — absolute** |
| `MF-102` | No change may suppress, delay, or silently degrade suspicious-activity detection or filing, and no change may disclose the existence of a SAR to it... | 31 U.S.C. §5318(g); 31 CFR §1020.320 | in force | **No — absolute** |
| `MF-103` | No account is opened, funded, or raised in limit before the Customer Identification Program completes | 31 CFR §1020.220 (Customer Identification Program) | in force | **No — absolute** |
| `MF-104` | Sensitive authentication data — full track data, card verification codes, PINs and PIN blocks — is never retained after authorization, and the PAN ... | PCI DSS v4.0.1 Req. 3.3.1, 3.4.1 | in force (v4.0.1 mandatory since 31 Mar 2025) | **No — absolute** |
| `MF-105` | EU/EEA personal data does not leave the region without an Article 45 adequacy decision or an Article 46 safeguard in force for that destination | GDPR, Reg. (EU) 2016/679 Arts. 44-49 | in force | **No — absolute** |
| `MF-106` | No prohibited-basis attribute, and no proxy for one, enters a credit underwriting, pricing, or line-assignment model | ECOA, 15 U.S.C. §1691; Reg. B, 12 CFR §1002.6(b)(9) | in force | **No — absolute** |
| `MF-107` | No system performs social scoring, deploys subliminal or purposefully manipulative techniques, infers emotion in the workplace, or builds facial-re... | Reg. (EU) 2024/1689 Art. 5 | in force since 2 Feb 2025 | **No — absolute** |
| `MF-108` | No change removes segregation of duties or disables the audit trail on a system inside the financial-reporting boundary | 15 U.S.C. §7262; SEC Rule 13a-15 | in force | **No — absolute** |
| `MF-109` | Consumer liability caps and error-resolution clocks for electronic fund transfers are not configurable downward or extendable by product decision | Reg. E, 12 CFR §§1005.6, 1005.11 | in force | **No — absolute** |
| `MF-110` | No adverse credit action rests on a model output that cannot produce specific principal reasons, and no change removes the human-reviewable path to... | Reg. B, 12 CFR §1002.9; CFPB Circulars 2022-03, 2023-03 | in force | **No — absolute** |
| `MF-111` | No autonomous agent moves customer funds, changes a credit limit, or closes an account without a bounded mandate and a human-operable stop, and no ... | Anthropic, Claude's Constitution (Jan 2026, CC0) — 'broadly safe'; cf. EU AI Act Art. 14; SR 11-7 §V | in force (firm policy) | **No — absolute** |

### Why each sits where it does

- **`MF-101` — Sanctions.** Strict liability with no materiality defence. No officer holds authority to accept a sanctions breach, so it cannot be a risk-acceptance question.
- **`MF-102` — BSA/AML.** Criminal exposure for individuals, not just the firm. Not an acceptable risk at any tier.
- **`MF-103` — BSA/AML.** A prescriptive precondition with no documented-exception path.
- **`MF-104` — PCI.** Contractual floor with the card networks; breach risks loss of the ability to process at all, which is not a risk an officer can accept on the firm's behalf.
- **`MF-105` — EU data protection.** Transfers without a mechanism are unlawful on their face; the remedy is a mechanism, not an acceptance.
- **`MF-106` — Fair lending.** Discrimination is prohibited outright. A business justification belongs in the model design, not in a risk acceptance.
- **`MF-107` — EU AI Act.** Art. 5 practices are prohibited, not high-risk: there is no conformity route that makes them lawful.
- **`MF-108` — SOX.** Personal certification exposure for named officers; the control is the thing being certified.
- **`MF-109` — Consumer payments.** Statutory consumer entitlements; the firm cannot contract or configure around them.
- **`MF-110` — Fair lending / AI.** The CFPB has stated expressly that an unexplainable model is not an excuse for a missing notice, so there is no exception to accept.
- **`MF-111` — AI oversight.** The firm's own constitutional commitment. Made absolute because an oversight mechanism that can be waived under delivery pressure is not an oversight mechanism.

## Security and operational resilience

| Provision | Obligation | Instrument | Status | Decidable by the firm? |
|---|---|---|---|---|
| `MF-201` | Customer information is encrypted in transit and at rest; a change that weakens or removes encryption on a customer-data path requires the CISO's w... | GLBA Safeguards Rule, 16 CFR §314.4(c)(3) | in force | Yes |
| `MF-202` | Multi-factor authentication protects every individual's access to every information system; any exception requires a written, CISO-approved compens... | 23 NYCRR §500.12 | in force since 1 Nov 2025 (universal MFA) | Yes |
| `MF-203` | No change disables or delays the telemetry that feeds regulatory incident reporting | 23 NYCRR §500.17(a); DORA Art. 19 with RTS (EU) 2025/301 | in force | Yes |
| `MF-204` | No ICT third party enters a critical-or-important function path without a register-of-information entry, a documented exit strategy, and disclosure... | DORA, Reg. (EU) 2022/2554 Art. 28(3); ITS (EU) 2024/2956 | in force since 17 Jan 2025 | Yes |
| `MF-205` | A change to a critical-or-important function is resilience tested before release; designated functions additionally carry threat-led penetration te... | DORA, Reg. (EU) 2022/2554 Arts. 24-26 | in force since 17 Jan 2025 | Yes |
| `MF-206` | No credential, key, or token appears in source, configuration, or CI logs; secrets live in the vault | 16 CFR §314.4(c); PCI DSS v4.0.1 Req. 8.6.2 | in force | Yes |
| `MF-207` | Every script on a payment page is authorized, inventoried, and integrity-checked, and a tamper-detection mechanism watches the page | PCI DSS v4.0.1 Req. 6.4.3, 11.6.1 | in force (future-dated reqs mandatory since 31 Mar 2025) | Yes |
| `MF-208` | No production change to a cardholder or ledger system without documented approval, a tested rollback, and separation between author and approver | PCI DSS v4.0.1 Req. 6.5.1; SOC 2 CC8.1 | in force | Yes |
| `MF-209` | Deploys are blocked on a greater-than-10% p95 latency regression, or any availability regression, on the payment-authorization path | FFIEC Business Continuity Management Handbook | in force (supervisory expectation) | Yes |
| `MF-210` | Personal data is collected for a stated purpose and deleted on schedule; no new personal-data field is retained without a recorded retention decision | GDPR Arts. 5(1)(c), 5(1)(e); CCPA/CPRA Cal. Civ. Code §1798.100(c) | in force | Yes |
| `MF-211` | No third-party code enters a cardholder-data or personal-data path without a completed vendor security review | Interagency Guidance on Third-Party Relationships, 88 FR 37920 (2023); DORA Art. 28 | in force | Yes |
| `MF-212` | No production deploy during a designated market-close or peak-period change freeze except under the emergency protocol | FFIEC Architecture, Infrastructure and Operations Handbook | in force (supervisory expectation) | Yes |

### Why each sits where it does

- **`MF-201` — GLBA.** The rule itself provides for a documented alternative control, so the firm does hold the authority to decide — which is what makes it adjudicable rather than absolute.
- **`MF-202` — NYDFS.** Part 500 names the compensating-control path explicitly, so the CISO holds real authority here.
- **`MF-203` — NYDFS / DORA.** Reporting must still happen; how it is plumbed is an engineering judgment the firm may make and defend.
- **`MF-204` — DORA.** Whether a function is critical-or-important is the firm's own documented assessment, so this is adjudicable by design.
- **`MF-205` — DORA.** Proportionality is built into Arts. 24-26; the firm chooses the testing depth and defends it.
- **`MF-206` — GLBA / PCI.** Migration lag is a real and time-boxable state; the exposure, not the paperwork, is what the rule targets.
- **`MF-207` — PCI.** The standard accepts several implementation techniques, including written confirmation from a compliant processor.
- **`MF-208` — PCI / SOC 2.** Emergency change procedures with post-hoc approval are an expected control design, not a violation.
- **`MF-209` — Operational.** A firm-set threshold, so the firm may vary it on the record.
- **`MF-210` — Privacy.** Necessity and proportionality are assessments the controller makes and documents.
- **`MF-211` — Third-party risk.** The guidance is explicitly risk-based and scales diligence to criticality.
- **`MF-212` — Operational.** The freeze is a firm-imposed control with a firm-defined emergency path.

## AI and model governance

| Provision | Obligation | Instrument | Status | Decidable by the firm? |
|---|---|---|---|---|
| `MF-301` | No model reaches a credit, fraud, or AML decision in production before independent validation covering conceptual soundness, outcomes analysis, and... | SR 11-7 / OCC Bulletin 2011-12 | in force (supervisory guidance) | Yes |
| `MF-302` | Every model in a decision path carries an inventory entry and current documentation: purpose, training data, known limits, and a named owner | SR 11-7 §VII; NIST AI RMF 1.0 GOVERN-1 | in force | Yes |
| `MF-303` | A customer interacting with an AI system is told so, and synthetic content the firm generates is machine-markable | Reg. (EU) 2024/1689 Art. 50; CFPB UDAAP | applies from 2 Aug 2026 | Yes |
| `MF-304` | Creditworthiness and credit-scoring systems are Annex III high-risk: risk management, data governance, logging, human oversight, and accuracy oblig... | Reg. (EU) 2024/1689 Arts. 9-15, Annex III(5)(b), as amended by the AI Omnibus (in force 27 July 2026) | Annex III obligations deferred to 2 Dec 2027 | Yes |
| `MF-305` | A decisioning model is tested for disparate impact across protected classes before deployment and monitored afterwards | NIST AI RMF 1.0 MEASURE-2.11; Reg. B effects test, 12 CFR §1002.6(a); CFPB Circular 2022-03 | in force | Yes |
| `MF-306` | An AI-facing surface does not deceive a customer, impersonate a human, manufacture confidence it does not have, or steer a customer against their o... | Anthropic, Claude's Constitution (Jan 2026, CC0) — 'broadly ethical'; Dodd-Frank §1031, 12 U.S.C. §5531 | in force (firm policy + UDAAP) | Yes |
| `MF-307` | Every agent-authored change carries a provenance attestation — agent identity, model version, and a link to the originating human requirement — and... | Anthropic Constitution (oversight); SR 11-7 §V; NIST AI RMF 1.0 MANAGE-4 | in force (firm policy) | Yes |
| `MF-308` | No customer personal data enters model training, or a third party model provider's retention window, without a lawful basis and a contractual carve... | GLBA §502, 15 U.S.C. §6802; GDPR Art. 6; DORA Art. 28 | in force | Yes |

### Why each sits where it does

- **`MF-301` — Model risk.** SR 11-7 scales validation to model risk and expressly contemplates compensating controls during the interim.
- **`MF-302` — Model risk.** Documentation debt is real and time-boxable without customer exposure.
- **`MF-303` — EU AI Act.** Art. 50 admits proportionate implementations; the obligation is disclosure, not a particular banner.
- **`MF-304` — EU AI Act.** A dated readiness obligation, not a present prohibition — exactly the shape a time-boxed risk acceptance is for.
- **`MF-305` — Fair lending / AI.** Testing methodology is a firm judgment; note that MF-106, the prohibition itself, is absolute — this provision governs the evidence, not the prohibition.
- **`MF-306` — AI conduct.** Conduct standards are judgment-laden and fact-specific, which is what adjudication is for.
- **`MF-307` — AI oversight.** The bound's size is a business decision. Note MF-111 makes the EXISTENCE of the stop absolute; this provision governs its calibration.
- **`MF-308` — Privacy / AI.** Lawful basis is establishable; anonymization and zero-retention terms are genuine cures.

## Consumer protection

| Provision | Obligation | Instrument | Status | Decidable by the firm? |
|---|---|---|---|---|
| `MF-401` | No dark pattern, no material omission, and no fee or term a reasonable consumer would not expect from the disclosure given | Dodd-Frank §§1031, 1036; 12 U.S.C. §§5531, 5536 | in force | Yes |
| `MF-402` | Data furnished to consumer reporting agencies is accurate, disputes are investigated within the statutory window, and adverse action notices name b... | FCRA, 15 U.S.C. §§1681m, 1681s-2; Reg. V, 12 CFR Part 1022 | in force | Yes |
| `MF-403` | Cost-of-credit disclosures are accurate, timely, and in the required form before the consumer becomes bound | TILA, 15 U.S.C. §1601; Reg. Z, 12 CFR Part 1026 | in force | Yes |
| `MF-404` | Opt-out of sale or sharing, and limits on sensitive personal information, are honoured on every surface including newly built ones | CCPA/CPRA, Cal. Civ. Code §1798.100 et seq. | in force | Yes |
| `MF-405` | Consumer-permissioned data access is built to a documented interface with revocable authorization, whatever shape the rule finally takes | Dodd-Frank §1033; 12 CFR Part 1033 | CONTESTED — final rule enjoined and under CFPB reconsideration as of August 2026 | Yes |
| `MF-406` | Consumer complaints are logged, routed, and closed within the stated window, and no change removes a complaint path without an equivalent replacement | CFPB supervisory expectations; UDAAP | in force (supervisory expectation) | Yes |

### Why each sits where it does

- **`MF-401` — UDAAP.** Unfairness and abusiveness are multi-factor standards decided on the facts.
- **`MF-402` — Credit reporting.** Reasonable procedures are the standard, so the adequacy of the procedure is arguable.
- **`MF-403` — Lending disclosure.** Reg. Z carries tolerances and cure provisions, so not every variance is a violation.
- **`MF-404` — State privacy.** Whether a disclosure is a 'sale' or 'share' is a contested characterisation the firm must take a position on.
- **`MF-405` — Open banking.** Deliberately not absolute and deliberately dated in the text: the rule is enjoined, and a constitution that pretends otherwise would mislead the officer reading it.
- **`MF-406` — Consumer conduct.** Channel design is the firm's, provided the path survives.


## Seed jurisprudence

23 holdings ship with the pack, covering 17 of the
26 adjudicable provisions.
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
contesting: `MF-203`, `MF-208`, `MF-302`, `MF-305`, `MF-306`, `MF-403`, `MF-404`, `MF-405`, `MF-406`.

## Scenario corpus

68 scenarios exercise the constitution end to end. Expectations are
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

