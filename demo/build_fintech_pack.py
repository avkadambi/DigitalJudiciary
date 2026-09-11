#!/usr/bin/env python3
"""Build the `fintech` demo pack: a reference constitution for a large,
multi-jurisdiction fintech, drawn from public-domain regulatory instruments.

    python3 demo/build_fintech_pack.py            # write the pack + rebuild _all

=== What this is ===

Every provision below is traceable to a published instrument: an EU regulation,
a US statute or agency rule, a supervisory guidance letter, a card-network
standard, or Anthropic's CC0-licensed constitution for Claude. The citation
travels IN the provision text, because a rule whose source you cannot look up
is a rule nobody can argue with — and the whole point of the Digital Judiciary
is that provisions get argued with.

=== The one structural decision worth reading ===

`absolute` is not a severity ranking. It is a claim about WHO MAY DECIDE.

An absolute provision cannot be risk-accepted by anyone, at any tier: the
Kernel short-circuits it at tier 1 (A6) and the only exit is an amendment to
the lawmakers. So `absolute` is reserved for obligations where no officer of
the firm actually holds the authority to accept the risk — strict-liability
sanctions exposure, criminal tipping-off liability, statutory prohibitions
with no materiality defence. Everything a regulator would let you document,
compensate, and time-box is deliberately NOT absolute, because encoding it as
absolute would be a lie about the firm's own authority: it would force every
routine exception through a constitutional amendment, and a constitution
amended weekly is not a constitution.

That distinction is the load-bearing one for a compliance reader. If you
disagree with where a line sits, move it — but move it deliberately, because
moving a provision into `absolute` removes a power that real officers have,
and moving one out grants a power they may not have.

=== Trigger / mitigator discipline ===

A factor is either a TRIGGER (listed in deny_if_any) or a MITIGATOR (may appear
in a precedent's premise). Never both. If a mitigating fact were also a
trigger, the distinguishing gate would collapse into the tier-1 predicate and
precedent would stop doing any work. `verify()` enforces this.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "companies")
KEY = "fintech"
DISPLAY = "Meridian Financial"
THETA = 0.25

# ---------------------------------------------------------------------------
# THE CONSTITUTION
# ---------------------------------------------------------------------------
# regime      : which body of law this comes from, for the register
# citation    : the instrument, precise enough to look up
# status      : in force / applies from / contested — as of August 2026
# absolute    : may no officer accept this risk? (see module docstring)
# triggers    : deny_if_any factors
# mitigators  : factors that may appear in a precedent premise
# ---------------------------------------------------------------------------
PROVISIONS = [
    # -- Absolute floors: no officer of the firm may accept these ------------
    dict(
        id="MF-101", absolute=True, regime="Sanctions",
        citation="31 CFR Ch. V (OFAC); IEEPA, 50 U.S.C. §1701",
        status="in force",
        text="Denied-party and sanctions screening is never bypassed, "
             "suppressed, allow-listed, or served from a cache older than 24 "
             "hours on any payment, onboarding, or beneficiary path. "
             "(Sanctions floor — 31 CFR Ch. V; IEEPA, 50 U.S.C. §1701. "
             "Liability is strict: there is no risk appetite to spend.)",
        triggers=["sanctions_screening_bypass", "sanctions_allowlist_path",
                  "screening_cache_stale"],
        mitigators=[],
        why="Strict liability with no materiality defence. No officer holds "
            "authority to accept a sanctions breach, so it cannot be a "
            "risk-acceptance question.",
    ),
    dict(
        id="MF-102", absolute=True, regime="BSA/AML",
        citation="31 U.S.C. §5318(g); 31 CFR §1020.320",
        status="in force",
        text="No change may suppress, delay, or silently degrade "
             "suspicious-activity detection or filing, and no change may "
             "disclose the existence of a SAR to its subject. (BSA floor — "
             "31 U.S.C. §5318(g); 31 CFR §1020.320. Tipping off is a "
             "criminal offence.)",
        triggers=["sar_pipeline_suppression", "sar_subject_disclosure",
                  "aml_alerting_disabled"],
        mitigators=[],
        why="Criminal exposure for individuals, not just the firm. Not an "
            "acceptable risk at any tier.",
    ),
    dict(
        id="MF-103", absolute=True, regime="BSA/AML",
        citation="31 CFR §1020.220 (Customer Identification Program)",
        status="in force",
        text="No account is opened, funded, or raised in limit before the "
             "Customer Identification Program completes. (BSA floor — "
             "31 CFR §1020.220.)",
        triggers=["cip_bypass", "funding_before_kyc"],
        mitigators=[],
        why="A prescriptive precondition with no documented-exception path.",
    ),
    dict(
        id="MF-104", absolute=True, regime="PCI",
        citation="PCI DSS v4.0.1 Req. 3.3.1, 3.4.1",
        status="in force (v4.0.1 mandatory since 31 Mar 2025)",
        text="Sensitive authentication data — full track data, card "
             "verification codes, PINs and PIN blocks — is never retained "
             "after authorization, and the PAN is never written unmasked to a "
             "log. (Card-network floor — PCI DSS v4.0.1 Req. 3.3.1 and "
             "3.4.1.)",
        triggers=["sad_retained_post_auth", "pan_unmasked_log"],
        mitigators=[],
        why="Contractual floor with the card networks; breach risks loss of "
            "the ability to process at all, which is not a risk an officer "
            "can accept on the firm's behalf.",
    ),
    dict(
        id="MF-105", absolute=True, regime="EU data protection",
        citation="GDPR, Reg. (EU) 2016/679 Arts. 44-49",
        status="in force",
        text="EU/EEA personal data does not leave the region without an "
             "Article 45 adequacy decision or an Article 46 safeguard in "
             "force for that destination. (GDPR floor — Reg. (EU) 2016/679 "
             "Arts. 44-49.)",
        triggers=["eu_personal_data_egress", "no_transfer_mechanism"],
        mitigators=[],
        why="Transfers without a mechanism are unlawful on their face; the "
            "remedy is a mechanism, not an acceptance.",
    ),
    dict(
        id="MF-106", absolute=True, regime="Fair lending",
        citation="ECOA, 15 U.S.C. §1691; Reg. B, 12 CFR §1002.6(b)(9)",
        status="in force",
        text="No prohibited-basis attribute, and no proxy for one, enters a "
             "credit underwriting, pricing, or line-assignment model. "
             "(Fair-lending floor — ECOA, 15 U.S.C. §1691; Reg. B, "
             "12 CFR §1002.6(b)(9).)",
        triggers=["prohibited_basis_variable", "protected_class_proxy"],
        mitigators=[],
        why="Discrimination is prohibited outright. A business justification "
            "belongs in the model design, not in a risk acceptance.",
    ),
    dict(
        id="MF-107", absolute=True, regime="EU AI Act",
        citation="Reg. (EU) 2024/1689 Art. 5",
        status="in force since 2 Feb 2025",
        text="No system performs social scoring, deploys subliminal or "
             "purposefully manipulative techniques, infers emotion in the "
             "workplace, or builds facial-recognition databases by untargeted "
             "scraping. (EU AI Act floor — Reg. (EU) 2024/1689 Art. 5, "
             "applicable since 2 February 2025.)",
        triggers=["social_scoring_feature", "manipulative_pattern",
                  "workplace_emotion_inference"],
        mitigators=[],
        why="Art. 5 practices are prohibited, not high-risk: there is no "
            "conformity route that makes them lawful.",
    ),
    dict(
        id="MF-108", absolute=True, regime="SOX",
        citation="15 U.S.C. §7262; SEC Rule 13a-15",
        status="in force",
        text="No change removes segregation of duties or disables the audit "
             "trail on a system inside the financial-reporting boundary. "
             "(SOX floor — 15 U.S.C. §7262; SEC Rule 13a-15.)",
        triggers=["sod_bypass", "ledger_audit_trail_off"],
        mitigators=[],
        why="Personal certification exposure for named officers; the control "
            "is the thing being certified.",
    ),
    dict(
        id="MF-109", absolute=True, regime="Consumer payments",
        citation="Reg. E, 12 CFR §§1005.6, 1005.11",
        status="in force",
        text="Consumer liability caps and error-resolution clocks for "
             "electronic fund transfers are not configurable downward or "
             "extendable by product decision. (Reg. E floor — 12 CFR "
             "§§1005.6, 1005.11.)",
        triggers=["reg_e_clock_extension", "liability_cap_override"],
        mitigators=[],
        why="Statutory consumer entitlements; the firm cannot contract or "
            "configure around them.",
    ),
    dict(
        id="MF-110", absolute=True, regime="Fair lending / AI",
        citation="Reg. B, 12 CFR §1002.9; CFPB Circulars 2022-03, 2023-03",
        status="in force",
        text="No adverse credit action rests on a model output that cannot "
             "produce specific principal reasons, and no change removes the "
             "human-reviewable path to contest one. (ECOA floor — 12 CFR "
             "§1002.9; CFPB Circulars 2022-03 and 2023-03: model complexity "
             "is not a defence.)",
        triggers=["unexplainable_adverse_action", "reason_codes_removed",
                  "human_appeal_removed"],
        mitigators=[],
        why="The CFPB has stated expressly that an unexplainable model is not "
            "an excuse for a missing notice, so there is no exception to "
            "accept.",
    ),
    dict(
        id="MF-111", absolute=True, regime="AI oversight",
        citation="Anthropic, Claude's Constitution (Jan 2026, CC0) — "
                 "'broadly safe'; cf. EU AI Act Art. 14; SR 11-7 §V",
        status="in force (firm policy)",
        text="No autonomous agent moves customer funds, changes a credit "
             "limit, or closes an account without a bounded mandate and a "
             "human-operable stop, and no change removes or degrades that "
             "stop. (Oversight floor — Anthropic, Claude's Constitution "
             "(January 2026, CC0), which places not undermining appropriate "
             "human oversight above helpfulness; cf. EU AI Act Art. 14, "
             "SR 11-7 §V.)",
        triggers=["agent_unbounded_authority", "oversight_stop_removed"],
        mitigators=[],
        why="The firm's own constitutional commitment. Made absolute because "
            "an oversight mechanism that can be waived under delivery "
            "pressure is not an oversight mechanism.",
    ),

    # -- Security and operational resilience --------------------------------
    dict(
        id="MF-201", absolute=False, regime="GLBA",
        citation="GLBA Safeguards Rule, 16 CFR §314.4(c)(3)",
        status="in force",
        text="Customer information is encrypted in transit and at rest; a "
             "change that weakens or removes encryption on a customer-data "
             "path requires the CISO's written finding of an effective "
             "alternative control. (GLBA Safeguards Rule — 16 CFR "
             "§314.4(c)(3), which contemplates exactly this finding.)",
        triggers=["encryption_downgrade", "plaintext_customer_data"],
        mitigators=["ciso_finding_filed", "compensating_control_documented",
                    "internal_network_only"],
        why="The rule itself provides for a documented alternative control, "
            "so the firm does hold the authority to decide — which is what "
            "makes it adjudicable rather than absolute.",
    ),
    dict(
        id="MF-202", absolute=False, regime="NYDFS",
        citation="23 NYCRR §500.12",
        status="in force since 1 Nov 2025 (universal MFA)",
        text="Multi-factor authentication protects every individual's access "
             "to every information system; any exception requires a written, "
             "CISO-approved compensating control reviewed at least annually. "
             "(23 NYCRR §500.12 — universal MFA in force since 1 November "
             "2025; §500.12(a) permits CISO-approved compensating controls.)",
        triggers=["mfa_exception_requested", "shared_service_account"],
        mitigators=["ciso_compensating_control", "phishing_resistant_fallback",
                    "time_boxed_30d"],
        why="Part 500 names the compensating-control path explicitly, so the "
            "CISO holds real authority here.",
    ),
    dict(
        id="MF-203", absolute=False, regime="NYDFS / DORA",
        citation="23 NYCRR §500.17(a); DORA Art. 19 with RTS (EU) 2025/301",
        status="in force",
        text="No change disables or delays the telemetry that feeds "
             "regulatory incident reporting. (23 NYCRR §500.17(a), 72 hours; "
             "DORA Art. 19 with RTS (EU) 2025/301 — initial report 4 hours "
             "from classification, intermediate 72 hours, final one month.)",
        triggers=["incident_telemetry_disabled", "reporting_hook_removed"],
        mitigators=["parallel_feed_verified", "dr_test_passed"],
        why="Reporting must still happen; how it is plumbed is an engineering "
            "judgment the firm may make and defend.",
    ),
    dict(
        id="MF-204", absolute=False, regime="DORA",
        citation="DORA, Reg. (EU) 2022/2554 Art. 28(3); ITS (EU) 2024/2956",
        status="in force since 17 Jan 2025",
        text="No ICT third party enters a critical-or-important function path "
             "without a register-of-information entry, a documented exit "
             "strategy, and disclosure of subcontracting. (DORA Art. 28(3), "
             "Reg. (EU) 2022/2554; register format per ITS (EU) 2024/2956.)",
        triggers=["unregistered_ict_provider", "no_exit_strategy"],
        mitigators=["register_entry_filed", "exit_plan_documented",
                    "non_critical_function"],
        why="Whether a function is critical-or-important is the firm's own "
            "documented assessment, so this is adjudicable by design.",
    ),
    dict(
        id="MF-205", absolute=False, regime="DORA",
        citation="DORA, Reg. (EU) 2022/2554 Arts. 24-26",
        status="in force since 17 Jan 2025",
        text="A change to a critical-or-important function is resilience "
             "tested before release; designated functions additionally carry "
             "threat-led penetration testing every three years. (DORA "
             "Arts. 24-26.)",
        triggers=["resilience_test_skipped", "critical_function_change"],
        mitigators=["dr_test_passed", "canary_staged", "rollback_verified"],
        why="Proportionality is built into Arts. 24-26; the firm chooses the "
            "testing depth and defends it.",
    ),
    dict(
        id="MF-206", absolute=False, regime="GLBA / PCI",
        citation="16 CFR §314.4(c); PCI DSS v4.0.1 Req. 8.6.2",
        status="in force",
        text="No credential, key, or token appears in source, configuration, "
             "or CI logs; secrets live in the vault. (GLBA Safeguards "
             "16 CFR §314.4(c); PCI DSS v4.0.1 Req. 8.6.2.)",
        triggers=["secret_in_source", "credential_in_ci_log"],
        mitigators=["vault_migration_queued", "rotation_enabled",
                    "encrypted_config"],
        why="Migration lag is a real and time-boxable state; the exposure, "
            "not the paperwork, is what the rule targets.",
    ),
    dict(
        id="MF-207", absolute=False, regime="PCI",
        citation="PCI DSS v4.0.1 Req. 6.4.3, 11.6.1",
        status="in force (future-dated reqs mandatory since 31 Mar 2025)",
        text="Every script on a payment page is authorized, inventoried, and "
             "integrity-checked, and a tamper-detection mechanism watches the "
             "page. (PCI DSS v4.0.1 Req. 6.4.3 and 11.6.1 — mandatory since "
             "31 March 2025.)",
        triggers=["unauthorized_payment_script", "no_script_integrity_check"],
        mitigators=["sri_hash_pinned", "script_inventory_updated",
                    "processor_attestation"],
        why="The standard accepts several implementation techniques, "
            "including written confirmation from a compliant processor.",
    ),
    dict(
        id="MF-208", absolute=False, regime="PCI / SOC 2",
        citation="PCI DSS v4.0.1 Req. 6.5.1; SOC 2 CC8.1",
        status="in force",
        text="No production change to a cardholder or ledger system without "
             "documented approval, a tested rollback, and separation between "
             "author and approver. (PCI DSS v4.0.1 Req. 6.5.1; SOC 2 "
             "CC8.1.)",
        triggers=["emergency_change_unapproved", "no_rollback_plan"],
        mitigators=["rollback_verified", "post_hoc_approval_filed",
                    "sev1_incident"],
        why="Emergency change procedures with post-hoc approval are an "
            "expected control design, not a violation.",
    ),
    dict(
        id="MF-209", absolute=False, regime="Operational",
        citation="FFIEC Business Continuity Management Handbook",
        status="in force (supervisory expectation)",
        text="Deploys are blocked on a greater-than-10% p95 latency "
             "regression, or any availability regression, on the "
             "payment-authorization path. (Operational provision; FFIEC "
             "Business Continuity Management Handbook.)",
        triggers=["latency_regression", "availability_regression"],
        mitigators=["canary_staged", "load_test_passed", "off_peak_window"],
        why="A firm-set threshold, so the firm may vary it on the record.",
    ),
    dict(
        id="MF-210", absolute=False, regime="Privacy",
        citation="GDPR Arts. 5(1)(c), 5(1)(e); CCPA/CPRA Cal. Civ. Code "
                 "§1798.100(c)",
        status="in force",
        text="Personal data is collected for a stated purpose and deleted on "
             "schedule; no new personal-data field is retained without a "
             "recorded retention decision. (GDPR Arts. 5(1)(c) and 5(1)(e); "
             "CCPA/CPRA, Cal. Civ. Code §1798.100(c).)",
        triggers=["retention_extension", "new_pii_field"],
        mitigators=["dpia_completed", "purpose_documented",
                    "retention_schedule_set"],
        why="Necessity and proportionality are assessments the controller "
            "makes and documents.",
    ),
    dict(
        id="MF-211", absolute=False, regime="Third-party risk",
        citation="Interagency Guidance on Third-Party Relationships, "
                 "88 FR 37920 (2023); DORA Art. 28",
        status="in force",
        text="No third-party code enters a cardholder-data or personal-data "
             "path without a completed vendor security review. (Interagency "
             "Guidance on Third-Party Relationships, 88 FR 37920 (2023); "
             "DORA Art. 28.)",
        triggers=["vendor_review_pending", "third_party_lib"],
        mitigators=["sbom_provided", "community_audit_complete",
                    "sandboxed_execution"],
        why="The guidance is explicitly risk-based and scales diligence to "
            "criticality.",
    ),
    dict(
        id="MF-212", absolute=False, regime="Operational",
        citation="FFIEC Architecture, Infrastructure and Operations Handbook",
        status="in force (supervisory expectation)",
        text="No production deploy during a designated market-close or "
             "peak-period change freeze except under the emergency protocol. "
             "(Operational provision; FFIEC Architecture, Infrastructure and "
             "Operations Handbook.)",
        triggers=["freeze_deploy"],
        mitigators=["sev1_incident", "regulator_deadline", "rollback_verified"],
        why="The freeze is a firm-imposed control with a firm-defined "
            "emergency path.",
    ),

    # -- AI and model governance --------------------------------------------
    dict(
        id="MF-301", absolute=False, regime="Model risk",
        citation="SR 11-7 / OCC Bulletin 2011-12",
        status="in force (supervisory guidance)",
        text="No model reaches a credit, fraud, or AML decision in production "
             "before independent validation covering conceptual soundness, "
             "outcomes analysis, and ongoing monitoring. (SR 11-7 / OCC "
             "Bulletin 2011-12, Supervisory Guidance on Model Risk "
             "Management.)",
        triggers=["unvalidated_model_deploy", "model_decision_path"],
        mitigators=["independent_validation_complete", "shadow_mode",
                    "champion_challenger_only"],
        why="SR 11-7 scales validation to model risk and expressly "
            "contemplates compensating controls during the interim.",
    ),
    dict(
        id="MF-302", absolute=False, regime="Model risk",
        citation="SR 11-7 §VII; NIST AI RMF 1.0 GOVERN-1",
        status="in force",
        text="Every model in a decision path carries an inventory entry and "
             "current documentation: purpose, training data, known limits, "
             "and a named owner. (SR 11-7 §VII model inventory; NIST AI RMF "
             "1.0, GOVERN-1.)",
        triggers=["missing_model_card", "model_inventory_gap"],
        mitigators=["model_card_filed", "inventory_entry_created"],
        why="Documentation debt is real and time-boxable without customer "
            "exposure.",
    ),
    dict(
        id="MF-303", absolute=False, regime="EU AI Act",
        citation="Reg. (EU) 2024/1689 Art. 50; CFPB UDAAP",
        status="applies from 2 Aug 2026",
        text="A customer interacting with an AI system is told so, and "
             "synthetic content the firm generates is machine-markable. "
             "(EU AI Act Art. 50 transparency obligations, applicable from "
             "2 August 2026; reinforced by CFPB UDAAP.)",
        triggers=["undisclosed_ai_agent", "unmarked_synthetic_content"],
        mitigators=["disclosure_banner_shipped", "content_credentials_attached"],
        why="Art. 50 admits proportionate implementations; the obligation is "
            "disclosure, not a particular banner.",
    ),
    dict(
        id="MF-304", absolute=False, regime="EU AI Act",
        citation="Reg. (EU) 2024/1689 Arts. 9-15, Annex III(5)(b), as amended "
                 "by the AI Omnibus (in force 27 July 2026)",
        status="Annex III obligations deferred to 2 Dec 2027",
        text="Creditworthiness and credit-scoring systems are Annex III "
             "high-risk: risk management, data governance, logging, human "
             "oversight, and accuracy obligations must be in place before the "
             "applicable date. (EU AI Act Arts. 9-15 and Annex III(5)(b). The "
             "AI Omnibus, in force 27 July 2026, moved standalone Annex III "
             "obligations to 2 December 2027 and Annex I to 2 August 2028; "
             "the Art. 5 prohibitions and Art. 50 transparency duties were "
             "NOT deferred.)",
        triggers=["high_risk_ai_gap", "no_conformity_assessment"],
        mitigators=["conformity_dossier_started", "human_oversight_documented",
                    "eu_market_not_served"],
        why="A dated readiness obligation, not a present prohibition — "
            "exactly the shape a time-boxed risk acceptance is for.",
    ),
    dict(
        id="MF-305", absolute=False, regime="Fair lending / AI",
        citation="NIST AI RMF 1.0 MEASURE-2.11; Reg. B effects test, "
                 "12 CFR §1002.6(a); CFPB Circular 2022-03",
        status="in force",
        text="A decisioning model is tested for disparate impact across "
             "protected classes before deployment and monitored afterwards. "
             "(NIST AI RMF 1.0, MEASURE-2.11; Reg. B effects test, 12 CFR "
             "§1002.6(a); CFPB Circular 2022-03.)",
        triggers=["bias_test_missing", "proxy_feature_untested"],
        mitigators=["disparate_impact_tested", "monitoring_plan_filed"],
        why="Testing methodology is a firm judgment; note that MF-106, the "
            "prohibition itself, is absolute — this provision governs the "
            "evidence, not the prohibition.",
    ),
    dict(
        id="MF-306", absolute=False, regime="AI conduct",
        citation="Anthropic, Claude's Constitution (Jan 2026, CC0) — "
                 "'broadly ethical'; Dodd-Frank §1031, 12 U.S.C. §5531",
        status="in force (firm policy + UDAAP)",
        text="An AI-facing surface does not deceive a customer, impersonate a "
             "human, manufacture confidence it does not have, or steer a "
             "customer against their own interest. (Anthropic, Claude's "
             "Constitution (January 2026, CC0), honesty and non-manipulation; "
             "enforceable against the firm through UDAAP, 12 U.S.C. §5531.)",
        triggers=["agent_impersonates_human", "undisclosed_incentive_steering"],
        mitigators=["disclosure_banner_shipped", "honesty_eval_passed"],
        why="Conduct standards are judgment-laden and fact-specific, which is "
            "what adjudication is for.",
    ),
    dict(
        id="MF-307", absolute=False, regime="AI oversight",
        citation="Anthropic Constitution (oversight); SR 11-7 §V; "
                 "NIST AI RMF 1.0 MANAGE-4",
        status="in force (firm policy)",
        text="Every agent-authored change carries a provenance attestation — "
             "agent identity, model version, and a link to the originating "
             "human requirement — and every agent action in production runs "
             "under an explicit value and rate bound. (Firm oversight "
             "provision; SR 11-7 §V on model use controls; NIST AI RMF 1.0, "
             "MANAGE-4.)",
        triggers=["missing_attestation", "unbounded_agent_action"],
        mitigators=["attestation_complete", "value_cap_set",
                    "human_requirement_linked"],
        why="The bound's size is a business decision. Note MF-111 makes the "
            "EXISTENCE of the stop absolute; this provision governs its "
            "calibration.",
    ),
    dict(
        id="MF-308", absolute=False, regime="Privacy / AI",
        citation="GLBA §502, 15 U.S.C. §6802; GDPR Art. 6; DORA Art. 28",
        status="in force",
        text="No customer personal data enters model training, or a third "
             "party model provider's retention window, without a lawful basis "
             "and a contractual carve-out. (GLBA §502, 15 U.S.C. §6802; GDPR "
             "Art. 6; provider relationship governed by DORA Art. 28.)",
        triggers=["customer_data_training", "third_party_model_retention"],
        mitigators=["consent_obtained", "anonymization_verified",
                    "zero_retention_agreement"],
        why="Lawful basis is establishable; anonymization and zero-retention "
            "terms are genuine cures.",
    ),

    # -- Consumer protection -------------------------------------------------
    dict(
        id="MF-401", absolute=False, regime="UDAAP",
        citation="Dodd-Frank §§1031, 1036; 12 U.S.C. §§5531, 5536",
        status="in force",
        text="No dark pattern, no material omission, and no fee or term a "
             "reasonable consumer would not expect from the disclosure given. "
             "(Dodd-Frank §§1031 and 1036, 12 U.S.C. §§5531 and 5536.)",
        triggers=["dark_pattern", "undisclosed_fee", "friction_asymmetry"],
        mitigators=["ux_research_filed", "disclosure_reviewed",
                    "symmetric_cancellation"],
        why="Unfairness and abusiveness are multi-factor standards decided on "
            "the facts.",
    ),
    dict(
        id="MF-402", absolute=False, regime="Credit reporting",
        citation="FCRA, 15 U.S.C. §§1681m, 1681s-2; Reg. V, 12 CFR Part 1022",
        status="in force",
        text="Data furnished to consumer reporting agencies is accurate, "
             "disputes are investigated within the statutory window, and "
             "adverse action notices name both the reasons and the agency. "
             "(FCRA, 15 U.S.C. §§1681m and 1681s-2; Reg. V, 12 CFR Part "
             "1022.)",
        triggers=["furnishing_accuracy_gap", "dispute_sla_breach"],
        mitigators=["reconciliation_job_added", "dispute_queue_staffed"],
        why="Reasonable procedures are the standard, so the adequacy of the "
            "procedure is arguable.",
    ),
    dict(
        id="MF-403", absolute=False, regime="Lending disclosure",
        citation="TILA, 15 U.S.C. §1601; Reg. Z, 12 CFR Part 1026",
        status="in force",
        text="Cost-of-credit disclosures are accurate, timely, and in the "
             "required form before the consumer becomes bound. (TILA, "
             "15 U.S.C. §1601; Reg. Z, 12 CFR Part 1026.)",
        triggers=["disclosure_timing_change", "apr_calculation_change"],
        mitigators=["legal_review_complete", "calculation_test_suite"],
        why="Reg. Z carries tolerances and cure provisions, so not every "
            "variance is a violation.",
    ),
    dict(
        id="MF-404", absolute=False, regime="State privacy",
        citation="CCPA/CPRA, Cal. Civ. Code §1798.100 et seq.",
        status="in force",
        text="Opt-out of sale or sharing, and limits on sensitive personal "
             "information, are honoured on every surface including newly "
             "built ones. (CCPA/CPRA, Cal. Civ. Code §1798.100 et seq., and "
             "analogous state statutes.)",
        triggers=["new_data_sale_path", "opt_out_not_propagated"],
        mitigators=["gpc_signal_honored", "opt_out_wired"],
        why="Whether a disclosure is a 'sale' or 'share' is a contested "
            "characterisation the firm must take a position on.",
    ),
    dict(
        id="MF-405", absolute=False, regime="Open banking",
        citation="Dodd-Frank §1033; 12 CFR Part 1033",
        status="CONTESTED — final rule enjoined and under CFPB "
               "reconsideration as of August 2026",
        text="Consumer-permissioned data access is built to a documented "
             "interface with revocable authorization, whatever shape the rule "
             "finally takes. (Dodd-Frank §1033; 12 CFR Part 1033. The October "
             "2024 final rule was enjoined by the Eastern District of "
             "Kentucky in October 2025 and is under CFPB reconsideration, so "
             "this is a READINESS provision with no live compliance date — "
             "the architecture, not the deadline, is what binds here.)",
        triggers=["screen_scraping_dependency", "non_revocable_token"],
        mitigators=["api_interface_documented", "revocation_endpoint_shipped"],
        why="Deliberately not absolute and deliberately dated in the text: "
            "the rule is enjoined, and a constitution that pretends "
            "otherwise would mislead the officer reading it.",
    ),
    dict(
        id="MF-406", absolute=False, regime="Consumer conduct",
        citation="CFPB supervisory expectations; UDAAP",
        status="in force (supervisory expectation)",
        text="Consumer complaints are logged, routed, and closed within the "
             "stated window, and no change removes a complaint path without "
             "an equivalent replacement. (CFPB supervisory expectations; "
             "UDAAP.)",
        triggers=["complaint_path_removed"],
        mitigators=["alternate_path_shipped"],
        why="Channel design is the firm's, provided the path survives.",
    ),
]

# ---------------------------------------------------------------------------
# SEED JURISPRUDENCE
# ---------------------------------------------------------------------------
# Holdings the firm's own history has already produced. Each rests on a
# premise drawn ONLY from that provision's mitigators, which is what lets a
# later case be distinguished from it when a mitigating fact is absent.
# ---------------------------------------------------------------------------
SEEDS = [
    dict(seed_id="MP-001", provision="MF-206", tier=2, principal="svc:tier2",
         resolved_at="2025-09-12", outcome="permit_conditional",
         facts=["secret_in_source", "encrypted_config", "rotation_enabled",
                "vault_migration_queued"],
         premise=["encrypted_config", "rotation_enabled",
                  "vault_migration_queued"],
         conditions="14-day window; encrypted config with rotation; vault "
                    "ticket linked",
         rationale="MF-206 targets credential EXPOSURE. An encrypted, "
                   "rotating configuration whose vault migration is already "
                   "ticketed presents migration lag, not exposure."),
    dict(seed_id="MP-002", provision="MF-206", tier=3, principal="svc:tier3",
         resolved_at="2026-01-20", outcome="deny",
         facts=["credential_in_ci_log", "rotation_enabled"],
         premise=["credential_in_ci_log", "rotation_enabled"],
         rationale="A credential printed into a CI log is already disclosed "
                   "to everyone who can read the build. Rotation limits the "
                   "window; it does not undo the disclosure."),
    dict(seed_id="MP-003", provision="MF-211", tier=2, principal="svc:tier2",
         resolved_at="2025-11-03", outcome="permit_conditional",
         facts=["third_party_lib", "vendor_review_pending", "sbom_provided",
                "community_audit_complete"],
         premise=["sbom_provided", "community_audit_complete"],
         conditions="proceed pending vendor review; review to close within 30 "
                    "days",
         rationale="A widely used library with a published SBOM and a "
                   "completed community audit carries materially lower "
                   "supply-chain risk; the vendor review may close in "
                   "parallel."),
    dict(seed_id="MP-004", provision="MF-211", tier=4, principal="coo.pat",
         resolved_at="2026-02-11", outcome="deny",
         facts=["third_party_lib", "vendor_review_pending",
                "sbom_provided", "touches_cardholder_path"],
         premise=["touches_cardholder_path"],
         rationale="After the January cardholder-path incident, an SBOM alone "
                   "no longer suffices for code inside the cardholder "
                   "boundary. Reviewed diligence must precede the merge, not "
                   "follow it."),
    dict(seed_id="MP-005", provision="MF-202", tier=2, principal="svc:tier2",
         resolved_at="2025-12-08", outcome="permit_conditional",
         facts=["mfa_exception_requested", "ciso_compensating_control",
                "phishing_resistant_fallback", "time_boxed_30d"],
         premise=["ciso_compensating_control", "phishing_resistant_fallback",
                  "time_boxed_30d"],
         conditions="30 days maximum; CISO control on file; phishing-resistant "
                    "fallback in place",
         rationale="Section 500.12(a) contemplates a CISO-approved "
                   "compensating control. A time-boxed exception with a "
                   "phishing-resistant fallback is the case the rule "
                   "describes, not an evasion of it."),
    dict(seed_id="MP-006", provision="MF-301", tier=3, principal="svc:tier3",
         resolved_at="2026-03-04", outcome="permit_conditional",
         facts=["model_decision_path", "unvalidated_model_deploy",
                "shadow_mode", "independent_validation_complete"],
         premise=["shadow_mode"],
         conditions="shadow mode only; no customer-visible decision until "
                    "validation closes",
         rationale="SR 11-7 scales control to use. A model that only shadows "
                   "the incumbent takes no decision, so the validation "
                   "obligation attaches before promotion rather than before "
                   "deployment."),
    dict(seed_id="MP-007", provision="MF-301", tier=4, principal="coo.pat",
         resolved_at="2025-10-17", outcome="deny",
         facts=["model_decision_path", "unvalidated_model_deploy",
                "champion_challenger_only"],
         premise=["champion_challenger_only"],
         rationale="A challenger model whose output is scored against live "
                   "decisions is already influencing the decision record; "
                   "validation attaches at that point."),
    dict(seed_id="MP-008", provision="MF-307", tier=2, principal="svc:tier2",
         resolved_at="2025-10-29", outcome="permit_conditional",
         facts=["missing_attestation", "attestation_complete",
                "human_requirement_linked"],
         premise=["attestation_complete", "human_requirement_linked"],
         conditions="attestation attached before merge; human requirement "
                    "linked in the ticket",
         rationale="The provision asks who authored the change and on whose "
                   "instruction. A complete attestation linked to a human "
                   "requirement answers exactly that."),
    dict(seed_id="MP-009", provision="MF-307", tier=3, principal="svc:tier3",
         resolved_at="2026-04-08", outcome="deny",
         facts=["unbounded_agent_action", "value_cap_set"],
         premise=["value_cap_set"],
         rationale="A value cap on a single action does not bound an agent "
                   "that may retry. The bound must hold across the session, "
                   "not the call."),
    dict(seed_id="MP-010", provision="MF-210", tier=2, principal="svc:tier2",
         resolved_at="2025-08-19", outcome="permit_conditional",
         facts=["new_pii_field", "dpia_completed", "purpose_documented",
                "retention_schedule_set"],
         premise=["dpia_completed", "purpose_documented",
                  "retention_schedule_set"],
         conditions="retention schedule registered before first write",
         rationale="Arts. 5(1)(c) and 5(1)(e) ask for purpose and a limit. A "
                   "completed DPIA with a registered schedule supplies both."),
    dict(seed_id="MP-011", provision="MF-212", tier=2, principal="svc:tier2",
         resolved_at="2025-12-30", outcome="permit_conditional",
         facts=["freeze_deploy", "sev1_incident", "rollback_verified"],
         premise=["sev1_incident", "rollback_verified"],
         conditions="incident reference recorded; rollback rehearsed",
         rationale="The freeze exists to protect the peak. A change that "
                   "restores the peak, with a rehearsed rollback, serves the "
                   "provision rather than defeating it."),
    dict(seed_id="MP-012", provision="MF-212", tier=2, principal="svc:tier2",
         resolved_at="2026-01-06", outcome="deny",
         facts=["freeze_deploy", "regulator_deadline"],
         premise=["regulator_deadline"],
         rationale="A regulatory deadline known months in advance is a "
                   "planning failure, not an emergency. The freeze holds."),
    dict(seed_id="MP-013", provision="MF-207", tier=2, principal="svc:tier2",
         resolved_at="2026-02-02", outcome="permit_conditional",
         facts=["unauthorized_payment_script", "sri_hash_pinned",
                "script_inventory_updated"],
         premise=["sri_hash_pinned", "script_inventory_updated"],
         conditions="SRI hash pinned; inventory entry updated in the same "
                    "change",
         rationale="Req. 6.4.3 asks that scripts be authorized and their "
                   "integrity assured. A pinned hash plus an inventory entry "
                   "is that assurance, whatever the approval workflow's "
                   "state."),
    dict(seed_id="MP-014", provision="MF-401", tier=3, principal="svc:tier3",
         resolved_at="2026-03-22", outcome="deny",
         facts=["friction_asymmetry", "ux_research_filed"],
         premise=["friction_asymmetry", "ux_research_filed"],
         rationale="Research showing that customers tolerate an asymmetric "
                   "cancellation flow measures tolerance, not fairness. "
                   "Asymmetry between signing up and leaving is the abuse the "
                   "provision names."),
    dict(seed_id="MP-015", provision="MF-401", tier=2, principal="svc:tier2",
         resolved_at="2025-11-25", outcome="permit_conditional",
         facts=["undisclosed_fee", "disclosure_reviewed",
                "symmetric_cancellation"],
         premise=["disclosure_reviewed", "symmetric_cancellation"],
         conditions="fee surfaced on the confirmation screen",
         rationale="A fee disclosed on the screen where the customer commits, "
                   "in a flow they can leave as easily as they entered, is "
                   "disclosed."),
    dict(seed_id="MP-016", provision="MF-204", tier=2, principal="svc:tier2",
         resolved_at="2026-01-14", outcome="permit_conditional",
         facts=["unregistered_ict_provider", "non_critical_function",
                "register_entry_filed"],
         premise=["non_critical_function", "register_entry_filed"],
         conditions="register entry filed; function classified non-critical "
                    "on the record",
         rationale="Art. 28(3) attaches to critical-or-important functions. A "
                   "recorded non-critical classification with a register "
                   "entry meets the obligation as written."),
    dict(seed_id="MP-017", provision="MF-303", tier=2, principal="svc:tier2",
         resolved_at="2026-05-06", outcome="permit_conditional",
         facts=["undisclosed_ai_agent", "disclosure_banner_shipped"],
         premise=["disclosure_banner_shipped"],
         conditions="disclosure visible before the first agent turn",
         rationale="Art. 50 requires that the customer be informed, not that "
                   "the notice take a particular form. A banner shown before "
                   "the first turn informs."),
    dict(seed_id="MP-018", provision="MF-308", tier=3, principal="svc:tier3",
         resolved_at="2026-04-21", outcome="permit_conditional",
         facts=["third_party_model_retention", "zero_retention_agreement",
                "anonymization_verified"],
         premise=["zero_retention_agreement", "anonymization_verified"],
         conditions="zero-retention terms executed; anonymization verified by "
                    "the privacy office",
         rationale="Executed zero-retention terms plus verified anonymization "
                   "remove both the lawful-basis question and the provider "
                   "retention window the provision targets."),
    dict(seed_id="MP-019", provision="MF-205", tier=2, principal="svc:tier2",
         resolved_at="2025-09-30", outcome="permit_conditional",
         facts=["critical_function_change", "dr_test_passed", "canary_staged"],
         premise=["dr_test_passed", "canary_staged"],
         conditions="canary held for one full business day",
         rationale="Arts. 24-26 are proportionate. A passed DR test plus a "
                   "staged canary is proportionate testing for a change of "
                   "this size."),
    dict(seed_id="MP-020", provision="MF-201", tier=4, principal="coo.pat",
         resolved_at="2026-05-19", outcome="permit_conditional",
         facts=["encryption_downgrade", "ciso_finding_filed",
                "internal_network_only", "compensating_control_documented"],
         premise=["ciso_finding_filed", "internal_network_only",
                  "compensating_control_documented"],
         conditions="internal path only; CISO finding on file; revisit at the "
                    "next architecture review",
         rationale="16 CFR 314.4(c)(3) contemplates a CISO finding of an "
                   "effective alternative control. On a wholly internal path "
                   "with the finding filed, that is the case the rule "
                   "describes."),
    dict(seed_id="MP-021", provision="MF-209", tier=2, principal="svc:tier2",
         resolved_at="2026-02-24", outcome="permit_conditional",
         facts=["latency_regression", "canary_staged", "load_test_passed",
                "off_peak_window"],
         premise=["canary_staged", "load_test_passed", "off_peak_window"],
         conditions="off-peak release; canary metrics watched for one hour",
         rationale="The threshold protects the authorization path at peak. "
                   "Load-tested, canaried, off-peak, the regression never "
                   "reaches the traffic the rule protects."),
    dict(seed_id="MP-022", provision="MF-402", tier=2, principal="svc:tier2",
         resolved_at="2026-03-10", outcome="permit_conditional",
         facts=["furnishing_accuracy_gap", "reconciliation_job_added"],
         premise=["reconciliation_job_added"],
         conditions="reconciliation runs before the next furnishing cycle",
         rationale="FCRA asks for reasonable procedures. A reconciliation job "
                   "that closes the gap before the next cycle is a reasonable "
                   "procedure."),
    # A7 in the ledger: an acceptance that has since run out. It is kept, not
    # deleted, because the renewal guard reads it — a later change on
    # materially similar facts must cite it rather than quietly re-accept.
    dict(seed_id="MP-023", provision="MF-304", tier=4, principal="coo.pat",
         resolved_at="2026-01-28", outcome="permit_conditional",
         is_acceptance=True, expiry="2026-06-30",
         facts=["high_risk_ai_gap", "no_conformity_assessment",
                "conformity_dossier_started"],
         premise=["conformity_dossier_started"],
         conditions="expires 30 June 2026; dossier complete before renewal is "
                    "sought",
         rationale="The Annex III obligations are not yet live and the "
                   "conformity dossier is underway, so the risk owner "
                   "accepted a bounded window rather than a permanent "
                   "exception. A7 makes the end date part of the act: when it "
                   "passes, the block returns without anyone deciding again."),
]

# ---------------------------------------------------------------------------
# SCENARIOS
# ---------------------------------------------------------------------------
# (category, description, provision, factors, contest_to, author, domain)
# Expectations are COMPUTED below from the documented semantics, never
# hand-asserted, and then checked against a live replay.
# ---------------------------------------------------------------------------
AGENT = "agent:codegen-1"
HUMAN = "eng.marisa"

CASES = [
    # -- A: routine, nothing engaged -----------------------------------------
    ("A-routine", "Add unit tests for the ACH return-code mapper",
     "MF-208", ["compliant"], 1, AGENT, "payments"),
    ("A-routine", "Refactor the ledger posting service for readability",
     "MF-208", ["compliant"], 1, HUMAN, "ledger"),
    ("A-routine", "Upgrade the observability agent to a patch release",
     "MF-203", ["compliant"], 1, AGENT, "platform"),
    ("A-routine", "Add a dashboard for dispute queue depth",
     "MF-402", ["compliant"], 1, HUMAN, "servicing"),
    ("A-routine", "Document the card tokenization service interfaces",
     "MF-207", ["compliant"], 1, AGENT, "cards"),
    ("A-routine", "Add retry backoff to the statement generator",
     "MF-209", ["compliant"], 1, AGENT, "payments"),
    ("A-routine", "Translate onboarding copy into Spanish",
     "MF-401", ["compliant"], 1, HUMAN, "onboarding"),
    ("A-routine", "Bump the linter and fix the resulting warnings",
     "MF-208", ["compliant"], 1, AGENT, "platform"),
    ("A-routine", "Add an index to the transaction search table",
     "MF-209", ["compliant"], 1, HUMAN, "ledger"),
    ("A-routine", "Extend the model inventory export with an owner column",
     "MF-302", ["compliant"], 1, AGENT, "risk"),

    # -- B: plain denial, not pushed back ------------------------------------
    ("B-plain-deny", "Hardcode the settlement partner API key in the "
     "connector config to unblock a demo",
     "MF-206", ["secret_in_source"], 1, AGENT, "payments"),
    ("B-plain-deny", "Ship a new merchant analytics field without a retention "
     "decision", "MF-210", ["new_pii_field"], 1, HUMAN, "growth"),
    ("B-plain-deny", "Add a vendor charting library straight into the "
     "cardholder console", "MF-211", ["third_party_lib",
                                      "vendor_review_pending"], 1, AGENT,
     "cards"),
    ("B-plain-deny", "Deploy the new fraud scorer directly to the decision "
     "path", "MF-301", ["model_decision_path", "unvalidated_model_deploy"],
     1, HUMAN, "risk"),
    ("B-plain-deny", "Remove the in-app complaint form in the navigation "
     "redesign", "MF-406", ["complaint_path_removed"], 1, HUMAN, "servicing"),
    ("B-plain-deny", "Add a third-party pixel that shares account status with "
     "an ad network", "MF-404", ["new_data_sale_path"], 1, AGENT, "growth"),
    ("B-plain-deny", "Move the APR calculation into the pricing service "
     "without a legal read", "MF-403", ["apr_calculation_change"], 1, AGENT,
     "lending"),
    ("B-plain-deny", "Deploy the collections copilot with no model card",
     "MF-302", ["missing_model_card"], 1, AGENT, "servicing"),

    # -- C: precedent found, followed ----------------------------------------
    ("C-precedent", "Partner credentials in an encrypted connector config "
     "with rotation on, vault migration ticketed",
     "MF-206", ["secret_in_source", "encrypted_config", "rotation_enabled",
                "vault_migration_queued"], 1, HUMAN, "payments"),
    ("C-precedent", "Add an audited open-source decimal library with a "
     "published SBOM to the pricing service",
     "MF-211", ["third_party_lib", "vendor_review_pending", "sbom_provided",
                "community_audit_complete"], 1, AGENT, "lending"),
    ("C-precedent", "Time-boxed MFA exception for the batch settlement "
     "account with a CISO control on file",
     "MF-202", ["mfa_exception_requested", "ciso_compensating_control",
                "phishing_resistant_fallback", "time_boxed_30d"], 1, HUMAN,
     "platform"),
    ("C-precedent", "Deploy the replacement underwriting model in shadow mode "
     "beside the incumbent",
     "MF-301", ["model_decision_path", "unvalidated_model_deploy",
                "shadow_mode", "independent_validation_complete"], 1, HUMAN,
     "lending"),
    ("C-precedent", "Agent-authored migration carrying a full attestation and "
     "a linked human requirement",
     "MF-307", ["missing_attestation", "attestation_complete",
                "human_requirement_linked"], 1, AGENT, "ledger"),
    ("C-precedent", "New merchant-category field with a completed DPIA and a "
     "registered retention schedule",
     "MF-210", ["new_pii_field", "dpia_completed", "purpose_documented",
                "retention_schedule_set"], 1, HUMAN, "growth"),
    ("C-precedent", "Freeze-window deploy to restore the authorization path "
     "after a Sev-1, rollback rehearsed",
     "MF-212", ["freeze_deploy", "sev1_incident", "rollback_verified"], 1,
     HUMAN, "payments"),
    ("C-precedent", "New payment-page script pinned by SRI hash with the "
     "inventory updated in the same change",
     "MF-207", ["unauthorized_payment_script", "sri_hash_pinned",
                "script_inventory_updated"], 1, AGENT, "cards"),
    ("C-precedent", "Register a non-critical reporting vendor with the "
     "register entry filed",
     "MF-204", ["unregistered_ict_provider", "non_critical_function",
                "register_entry_filed"], 1, HUMAN, "platform"),
    ("C-precedent", "Servicing copilot ships with the AI disclosure banner "
     "before the first turn",
     "MF-303", ["undisclosed_ai_agent", "disclosure_banner_shipped"], 1,
     AGENT, "servicing"),
    ("C-precedent", "Off-peak release of the authorization refactor, load "
     "tested and canaried",
     "MF-209", ["latency_regression", "canary_staged", "load_test_passed",
                "off_peak_window"], 1, HUMAN, "payments"),
    ("C-precedent", "Furnishing gap closed by a reconciliation job before the "
     "next cycle",
     "MF-402", ["furnishing_accuracy_gap", "reconciliation_job_added"], 1,
     AGENT, "servicing"),
    ("C-precedent", "Critical-function change with a passed DR test and a "
     "staged canary",
     "MF-205", ["critical_function_change", "dr_test_passed",
                "canary_staged"], 1, HUMAN, "platform"),
    ("C-precedent", "Vendor model moved under executed zero-retention terms "
     "with anonymization verified",
     "MF-308", ["third_party_model_retention", "zero_retention_agreement",
                "anonymization_verified"], 1, HUMAN, "risk"),

    # -- D: two holdings in play; authority and recency decide ---------------
    ("D-ordering", "Audited third-party library, SBOM published, but the code "
     "sits in the cardholder path",
     "MF-211", ["third_party_lib", "vendor_review_pending", "sbom_provided",
                "community_audit_complete", "touches_cardholder_path"], 1,
     AGENT, "cards"),
    ("D-ordering", "Challenger fraud model scored against live decisions "
     "while validation is open",
     "MF-301", ["model_decision_path", "unvalidated_model_deploy",
                "champion_challenger_only", "shadow_mode"], 1, HUMAN, "risk"),
    ("D-ordering", "Freeze-window deploy driven by a regulatory filing "
     "deadline, rollback rehearsed",
     "MF-212", ["freeze_deploy", "regulator_deadline", "rollback_verified",
                "sev1_incident"], 1, HUMAN, "platform"),

    # -- E: precedent retrieved but distinguished ----------------------------
    ("E-distinguish", "Partner credentials in an encrypted config, but no "
     "vault migration ticket exists",
     "MF-206", ["secret_in_source", "encrypted_config", "rotation_enabled"],
     1, AGENT, "payments"),
    ("E-distinguish", "Third-party library with an SBOM but no completed "
     "community audit",
     "MF-211", ["third_party_lib", "vendor_review_pending", "sbom_provided"],
     1, AGENT, "lending"),
    ("E-distinguish", "MFA exception with a CISO control but no "
     "phishing-resistant fallback and no time box",
     "MF-202", ["mfa_exception_requested", "ciso_compensating_control"], 1,
     HUMAN, "platform"),
    ("E-distinguish", "New PII field with a DPIA but no registered retention "
     "schedule", "MF-210", ["new_pii_field", "dpia_completed",
                            "purpose_documented"], 1, HUMAN, "growth"),
    ("E-distinguish", "Payment-page script with an inventory entry but no SRI "
     "hash pinned",
     "MF-207", ["unauthorized_payment_script", "script_inventory_updated"], 1,
     AGENT, "cards"),
    ("E-distinguish", "Agent-authored change with an attestation but no "
     "linked human requirement",
     "MF-307", ["missing_attestation", "attestation_complete"], 1, AGENT,
     "ledger"),
    ("E-distinguish", "Critical-function change with a canary but no DR test",
     "MF-205", ["critical_function_change", "canary_staged"], 1, HUMAN,
     "platform"),

    # -- F: absolute floors, short-circuited at tier 1 -----------------------
    ("F-absolute", "Add an allow-list path that skips sanctions screening for "
     "repeat beneficiaries",
     "MF-101", ["sanctions_allowlist_path", "sanctions_screening_bypass"], 1,
     AGENT, "payments"),
    ("F-absolute", "Raise the AML alert threshold to cut queue volume before "
     "quarter end",
     "MF-102", ["aml_alerting_disabled", "sar_pipeline_suppression"], 1,
     HUMAN, "risk"),
    ("F-absolute", "Let customers fund an account while identity "
     "verification is still pending",
     "MF-103", ["funding_before_kyc", "cip_bypass"], 1, HUMAN, "onboarding"),
    ("F-absolute", "Cache the CVV for one-click repeat checkout",
     "MF-104", ["sad_retained_post_auth"], 1, AGENT, "cards"),
    ("F-absolute", "Route EU customer records to the US analytics warehouse "
     "with no transfer mechanism",
     "MF-105", ["eu_personal_data_egress", "no_transfer_mechanism"], 1, AGENT,
     "growth"),
    ("F-absolute", "Add neighbourhood-level features to the underwriting "
     "model", "MF-106", ["protected_class_proxy"], 1, HUMAN, "lending"),
    ("F-absolute", "Score customers on social media behaviour for the premium "
     "tier", "MF-107", ["social_scoring_feature"], 1, HUMAN, "growth"),
    ("F-absolute", "Let the release engineer approve their own change to the "
     "general ledger", "MF-108", ["sod_bypass"], 1, AGENT, "ledger"),
    ("F-absolute", "Extend the provisional-credit clock for disputed "
     "transfers", "MF-109", ["reg_e_clock_extension"], 1, HUMAN, "servicing"),
    ("F-absolute", "Ship the ensemble declines without reason codes",
     "MF-110", ["unexplainable_adverse_action", "reason_codes_removed"], 1,
     HUMAN, "lending"),
    ("F-absolute", "Remove the manual stop from the automated collections "
     "agent", "MF-111", ["oversight_stop_removed",
                         "agent_unbounded_authority"], 1, AGENT, "servicing"),

    # -- G: pushed all the way to a named human ------------------------------
    ("G-riskowner", "Weaken encryption on an internal customer-data path, "
     "CISO finding filed",
     "MF-201", ["encryption_downgrade", "ciso_finding_filed",
                "internal_network_only"], 4, HUMAN, "platform"),
    ("G-riskowner", "Unregistered ICT provider proposed for a "
     "critical-function path", "MF-204", ["unregistered_ict_provider",
                                          "no_exit_strategy"], 4, HUMAN,
     "platform"),
    ("G-riskowner", "Launch the EU credit-scoring pilot before the "
     "conformity dossier is complete",
     "MF-304", ["high_risk_ai_gap", "no_conformity_assessment"], 4, HUMAN,
     "lending"),
    ("G-riskowner", "Ship the pricing model without the disparate-impact test "
     "run", "MF-305", ["bias_test_missing"], 4, HUMAN, "lending"),
    ("G-riskowner", "Emergency ledger fix with no approver available",
     "MF-208", ["emergency_change_unapproved", "no_rollback_plan"], 4, AGENT,
     "ledger"),
    ("G-riskowner", "Retire the legacy aggregator scraping path before the "
     "API is ready", "MF-405", ["screen_scraping_dependency",
                                "non_revocable_token"], 4, HUMAN, "platform"),
    ("G-riskowner", "Onboarding assistant answers in the voice of a named "
     "human agent", "MF-306", ["agent_impersonates_human"], 4, AGENT,
     "onboarding"),
    ("G-riskowner", "Train the servicing model on customer transcripts",
     "MF-308", ["customer_data_training"], 4, HUMAN, "risk"),

    # -- H: the change targets the rulebook itself ---------------------------
    ("H-control-plane", "Remediation agent lowers the MFA exception window in "
     "the policy repo", "constitution", ["policy_edit"], 1, AGENT,
     "platform"),
    ("H-control-plane", "Proposal to reclassify the open-banking provision as "
     "advisory", "constitution", ["policy_edit"], 1, HUMAN, "platform"),
    ("H-control-plane", "Proposal to add a stablecoin reserve-attestation "
     "clause under MiCA", "constitution", ["policy_edit"], 1, HUMAN,
     "platform"),
    ("H-control-plane", "Edit the deny predicate for the change-freeze "
     "provision", "constitution", ["policy_edit"], 1, AGENT, "platform"),

    # -- J: novel facts, nothing on point ------------------------------------
    ("J-novel", "First quantum-safe key exchange on the settlement link",
     "MF-201", ["encryption_downgrade", "pqc_migration"], 1, HUMAN,
     "payments"),
    ("J-novel", "First agent-to-agent payment negotiation with a counterparty "
     "bot", "MF-307", ["unbounded_agent_action", "counterparty_agent"], 1,
     AGENT, "payments"),
    ("J-novel", "First synthetic-media marketing asset generated in-house",
     "MF-303", ["unmarked_synthetic_content"], 1, HUMAN, "growth"),
]


# ---------------------------------------------------------------------------
# Expectation solver — the documented semantics, applied
# ---------------------------------------------------------------------------
def jaccard(a: set, b: set) -> float:
    u = a | b
    return (len(a & b) / len(u)) if u else 0.0


def solve(provision_id: str, facts: list[str], seeds: list[dict],
          prov_by_id: dict) -> tuple[str, str | None]:
    """Return (tier-1 outcome, controlling seed_id or None).

    Mirrors adjudicate.py: retrieve by Jaccard >= THETA on the same
    provision, distinguish where premise is not contained in the facts,
    then order by authority tier, then recency. A single survivor binds and
    its interpretation is mirrored; otherwise the provision's own predicate
    decides.
    """
    fs = set(facts)
    cands = [s for s in seeds if s["provision"] == provision_id
             and jaccard(fs, set(s["facts"])) >= THETA]
    survivors = [s for s in cands if not (set(s["premise"]) - fs)]
    ctrl = None
    if survivors:
        top = max(s["tier"] for s in survivors)
        pool = [s for s in survivors if s["tier"] == top]
        if len(pool) > 1:
            newest = max(s["resolved_at"] for s in pool)
            pool = [s for s in pool if s["resolved_at"] == newest]
        if len(pool) == 1:
            ctrl = pool[0]
    if ctrl:
        return ctrl["outcome"], ctrl["seed_id"]
    triggers = set(prov_by_id[provision_id]["triggers"])
    return ("deny" if triggers & fs else "permit"), None


def build_case(i: int, spec: tuple, seeds: list[dict],
               prov_by_id: dict) -> dict:
    category, desc, provision, factors, contest_to, author, domain = spec
    cid = f"{category[0]}{i:02d}"

    if provision == "constitution":
        return dict(id=cid, organization=KEY, category=category, author=author,
                    domain=domain, description=desc, provisions=["constitution"],
                    factors=factors, violation=True, contest_to=1,
                    expect=dict(route="draft_amendment", tier1_decision="deny",
                                final_decision="draft_amendment", final_tier=0,
                                controlling=None, stored=False))

    prov = prov_by_id[provision]
    if prov["absolute"]:
        return dict(id=cid, organization=KEY, category=category, author=author,
                    domain=domain, description=desc, provisions=[provision],
                    factors=factors, violation=True, contest_to=1,
                    expect=dict(route="absolute_deny", tier1_decision="deny",
                                final_decision="deny", final_tier=1,
                                controlling=None, stored=False))

    outcome, ctrl = solve(provision, factors, seeds, prov_by_id)
    if contest_to >= 4 and outcome == "deny":
        final_decision, final_tier, stored = "deny", 4, True
    else:
        final_decision, final_tier = outcome, 1
        stored = False
    return dict(id=cid, organization=KEY, category=category, author=author,
                domain=domain, description=desc, provisions=[provision],
                factors=factors, violation=(outcome != "permit"),
                contest_to=(contest_to if outcome != "permit" else 1),
                expect=dict(route="adjudicate", tier1_decision=outcome,
                            final_decision=final_decision,
                            final_tier=final_tier, controlling=ctrl,
                            stored=stored))


# ---------------------------------------------------------------------------
def verify(prov_by_id: dict) -> None:
    """Refuse to build an incoherent constitution."""
    errs = []
    triggers, mitigators = set(), set()
    for p in PROVISIONS:
        triggers |= set(p["triggers"])
        mitigators |= set(p["mitigators"])
        if p["absolute"] and p["mitigators"]:
            errs.append(f"{p['id']}: absolute provisions are short-circuited "
                        f"at tier 1, so their mitigators can never be read")
        if not p["triggers"]:
            errs.append(f"{p['id']}: no deny predicate")
    both = triggers & mitigators
    if both:
        errs.append(f"factors are both trigger and mitigator, which collapses "
                    f"the distinguishing gate: {sorted(both)}")

    seen = set()
    for s in SEEDS:
        if s["provision"] not in prov_by_id:
            errs.append(f"{s['seed_id']}: unknown provision {s['provision']}")
            continue
        if prov_by_id[s["provision"]]["absolute"]:
            errs.append(f"{s['seed_id']}: no precedent can exist on an "
                        f"absolute provision (A6 short-circuits before "
                        f"retrieval)")
        if not set(s["premise"]) <= set(s["facts"]):
            errs.append(f"{s['seed_id']}: Def. 8 — premise contains facts the "
                        f"case never had: "
                        f"{sorted(set(s['premise']) - set(s['facts']))}")
        if s["tier"] == 4 and s["principal"] != "coo.pat":
            errs.append(f"{s['seed_id']}: tier-4 admission needs the "
                        f"risk_owner branch")
        if s.get("is_acceptance") and not s.get("expiry"):
            errs.append(f"{s['seed_id']}: A7 — acceptances carry an expiry")
        if s["seed_id"] in seen:
            errs.append(f"duplicate seed id {s['seed_id']}")
        seen.add(s["seed_id"])

    for spec in CASES:
        pid = spec[2]
        if pid != "constitution" and pid not in prov_by_id:
            errs.append(f"case {spec[1]!r}: unknown provision {pid}")

    if errs:
        for e in errs:
            print(f"  REFUSED: {e}", file=sys.stderr)
        raise SystemExit(1)


def emit() -> dict:
    prov_by_id = {p["id"]: p for p in PROVISIONS}
    verify(prov_by_id)

    d = os.path.join(OUT, KEY)
    os.makedirs(d, exist_ok=True)

    rulebook = {"provisions": [
        {"provision_id": p["id"], "absolute": p["absolute"], "text": p["text"],
         "policy": {"deny_if_any": sorted(p["triggers"])},
         "organization": KEY}
        for p in PROVISIONS]}
    json.dump(rulebook, open(os.path.join(d, "rulebook.json"), "w"), indent=1)

    records = [{
        "seed_id": s["seed_id"], "provision_id": s["provision"],
        "tier": s["tier"], "resolving_principal": s["principal"],
        "resolved_at": f"{s['resolved_at']}T00:00:00.000000+00:00",
        "facts": sorted(s["facts"]), "premise": sorted(s["premise"]),
        "interpretation": {"outcome": s["outcome"]},
        "conditions": ({"note": s["conditions"]} if s.get("conditions")
                       else None),
        "scope": {}, "scope_level": "org", "rationale": s["rationale"],
        "is_acceptance": bool(s.get("is_acceptance")),
        "expiry": s.get("expiry"), "organization": KEY,
    } for s in SEEDS]
    json.dump({"records": records},
              open(os.path.join(d, "store_seed.json"), "w"), indent=1)
    json.dump({"records": records},
              open(os.path.join(d, "store_seed_initial.json"), "w"), indent=1)

    org = {"organizations": [
        {"org_id": KEY, "name": DISPLAY, "principals": [
            {"principal_id": f"{KEY}.risk", "branch": "risk_owner",
             "key": f"devkey-{KEY}-risk", "kind": "human",
             "role": "risk owner", "desk": "/review"},
            {"principal_id": f"{KEY}.grc", "branch": "lawmakers",
             "key": f"devkey-{KEY}-grc", "kind": "human",
             "role": "GRC council", "desk": "/review/amendments"},
            {"principal_id": f"{KEY}.eng", "branch": None,
             "key": f"devkey-{KEY}-eng", "kind": "human",
             "role": "engineer", "desk": "/review/changes"},
            {"principal_id": f"{KEY}.audit", "branch": None,
             "key": f"devkey-{KEY}-audit", "kind": "human",
             "role": "auditor", "desk": "/review/ledger"},
        ]},
        {"org_id": None, "name": "Platform", "principals": [
            {"principal_id": "platform.admin", "branch": None,
             "key": "devkey-platform-admin", "kind": "human",
             "role": "platform administrator — the only account that reads "
                     "across tenants, and it decides nothing"}]},
    ], "founding_scope": KEY}
    json.dump(org, open(os.path.join(d, "organizations.json"), "w"), indent=1)

    counters: dict[str, int] = {}
    cases = []
    for spec in CASES:
        counters[spec[0]] = counters.get(spec[0], 0) + 1
        cases.append(build_case(counters[spec[0]], spec, SEEDS, prov_by_id))
    json.dump({
        "company": KEY, "display_name": DISPLAY, "theta": THETA, "k": 4,
        "source": "authored reference corpus, not a converted case study",
        "provenance":
            "A reference constitution for a large multi-jurisdiction fintech, "
            "assembled from public-domain regulatory instruments (EU and US) "
            "and Anthropic's CC0 constitution for Claude. Provision text "
            "carries its own citation. Scenario expectations are computed "
            "from the documented adjudication semantics and verified against "
            "a live replay; none are hand-asserted.",
        "regulatory_note":
            "Regulatory positions stated as of August 2026. The EU AI Act "
            "Omnibus (in force 27 July 2026) deferred standalone Annex III "
            "high-risk obligations to 2 December 2027; 12 CFR Part 1033 is "
            "enjoined and under CFPB reconsideration. This corpus is an "
            "engineering artifact, not legal advice.",
        "cases": cases,
    }, open(os.path.join(d, "cases.json"), "w"), indent=1)

    return {"provisions": len(PROVISIONS), "records": len(records),
            "cases": len(cases),
            "absolute": sum(1 for p in PROVISIONS if p["absolute"])}


def rebuild_all() -> None:
    """Refuse the merge unless provision namespaces stay disjoint."""
    index_path = os.path.join(OUT, "index.json")
    index = json.load(open(index_path))["companies"]
    if not any(e["key"] == KEY for e in index):
        st = emit_stats
        index.append({"key": KEY, "display_name": DISPLAY,
                      "provisions": st["provisions"], "records": st["records"],
                      "cases": st["cases"]})
    else:
        for e in index:
            if e["key"] == KEY:
                e.update(display_name=DISPLAY,
                         provisions=emit_stats["provisions"],
                         records=emit_stats["records"],
                         cases=emit_stats["cases"])
    json.dump({"companies": index}, open(index_path, "w"), indent=1)

    d = os.path.join(OUT, "_all")
    os.makedirs(d, exist_ok=True)
    provisions, records, cases, orgs = [], [], [], []
    owner: dict[str, str] = {}
    for entry in index:
        key = entry["key"]
        src = os.path.join(OUT, key)
        rb = json.load(open(os.path.join(src, "rulebook.json")))
        st = json.load(open(os.path.join(src, "store_seed.json")))
        cs = json.load(open(os.path.join(src, "cases.json")))
        for prov in rb["provisions"]:
            pid = prov["provision_id"]
            if pid in owner:
                raise SystemExit(
                    f"provision {pid} is claimed by both {owner[pid]} and "
                    f"{key}; the multi-tenant pack cannot be built safely")
            owner[pid] = key
            provisions.append({**prov, "organization": key})
        for r in st["records"]:
            records.append({**r, "organization": key,
                            "seed_id": f"{key}:{r['seed_id']}"})
        for c in cs["cases"]:
            cases.append({**c, "organization": key, "id": f"{key}:{c['id']}"})
        orgs.append({"org_id": key, "name": entry["display_name"],
                     "principals": cast_for(key)})

    json.dump({"provisions": sorted(provisions,
                                    key=lambda p: p["provision_id"])},
              open(os.path.join(d, "rulebook.json"), "w"), indent=1)
    json.dump({"records": records},
              open(os.path.join(d, "store_seed.json"), "w"), indent=1)
    orgs.append({"org_id": None, "name": "Platform",
                 "principals": [
                     {"principal_id": "platform.admin", "branch": None,
                      "key": "devkey-platform-admin", "kind": "human",
                      "role": "platform administrator — the only account that "
                              "reads across tenants, and it decides nothing"}]})
    json.dump({"organizations": [o for o in orgs if o["org_id"]]
               + [o for o in orgs if not o["org_id"]],
               "founding_scope": index[0]["key"]},
              open(os.path.join(d, "organizations.json"), "w"), indent=1)
    json.dump({"company": "_all", "display_name": "All tenants",
               "multi_tenant": True,
               "organizations": [o["org_id"] for o in orgs],
               "provenance": "the four converted case-study corpora plus the "
                             "fintech reference constitution, fused into one "
                             "multi-tenant ledger; provision namespaces "
                             "verified disjoint",
               "cases": cases},
              open(os.path.join(d, "cases.json"), "w"), indent=1)
    print(f"  {'_all':12s} {len(orgs)} tenants, {len(provisions)} provisions,"
          f" {len(records)} records, {len(cases)} cases — namespaces disjoint")


def cast_for(key: str) -> list[dict]:
    return [
        {"principal_id": f"{key}.risk", "branch": "risk_owner",
         "key": f"devkey-{key}-risk", "kind": "human",
         "role": "risk owner", "desk": "/review"},
        {"principal_id": f"{key}.grc", "branch": "lawmakers",
         "key": f"devkey-{key}-grc", "kind": "human",
         "role": "GRC council", "desk": "/review/amendments"},
        {"principal_id": f"{key}.eng", "branch": None,
         "key": f"devkey-{key}-eng", "kind": "human",
         "role": "engineer", "desk": "/review/changes"},
        {"principal_id": f"{key}.audit", "branch": None,
         "key": f"devkey-{key}-audit", "kind": "human",
         "role": "auditor", "desk": "/review/ledger"},
    ]


if __name__ == "__main__":
    emit_stats = emit()
    print(f"  {KEY:12s} {emit_stats['provisions']} provisions "
          f"({emit_stats['absolute']} absolute), {emit_stats['records']} "
          f"records, {emit_stats['cases']} cases")
    rebuild_all()
