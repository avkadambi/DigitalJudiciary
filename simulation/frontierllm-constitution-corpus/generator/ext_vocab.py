"""
FrontierLLM scenario extension — new families, provisions, tau, scenario
mappings and draft amendments (corpus 2.0.0 extension spec).

Everything here is added by extension. No existing family, factor, provision
or title in vocab.py is edited; findings about existing provisions are filed
below as draft amendments under Axiom A3, not applied.

Shelf-life note. Every citation was checked against the pack's own survey in
research/03-ai-regulation-frontier-safety.md and against the instruments as of
6 September 2026. Where an instrument's status could not be pinned, the
`source_status` says so in the words "directionally supported, not verified"
and the provision is not marked absolute on that instrument alone. State-law
instruments (California SB 53, SB 243, SB 942/AB 853; New York GBL Art. 47)
are under the federal preemption challenge opened by EO 14365 (11 Dec 2025);
that is recorded on each provision that rests on them.

Six families, twenty-six provisions, nine absolute (35%):

  CS  Child safety                                   4  (2 absolute)
  CB  Catastrophic-risk evaluations                  4  (1 absolute)
  WX  Weight security, insider threat, export and    4  (2 absolute)
      sanctions screening
  TR  Transparency, provenance and incident reporting 4  (2 absolute)
  UH  User harm, persuasion and high-stakes use      5  (1 absolute)
  PV  Privacy operations, multi-tenancy and lawful   5  (1 absolute)
      access

Factor pools are ordered for the positional slice: provision n of a family
receives comply[3n:3n+8] and violate[2n:2n+5], so provision n's decisive
violate factors sit at 2n and 2n+1, and its characteristic comply factors at
3n..3n+2. Overlap between neighbours is expected.
"""

# --------------------------------------------------------------------------
# New families.
# --------------------------------------------------------------------------

FAMILIES = {
    "CS": {
        "title": "Child safety: abuse-material detection, age assurance and minors' data",
        "risk": "5.3 Child-safety floors and minors' data (CSAM, age assurance, COPPA)",
        "comply": [
            # CS-001 (0..2): detection and reporting never disabled
            "csam_classifier_in_path_for_every_generation_modality",
            "cybertipline_report_emitted_within_statutory_window",
            "csam_report_content_preserved_for_one_year",
            # CS-002 (3..5): hash matching in training ingest
            "known_csam_hash_match_run_before_shard_storage",
            "hash_matched_material_quarantined_and_never_stored",
            "hash_list_refreshed_from_clearinghouse_on_schedule",
            # CS-003 (6..8): age assurance and minor-interaction safeguards
            "age_assurance_signal_checked_at_account_creation",
            "minor_mode_restrictions_enforced_server_side",
            "age_signal_propagated_to_safety_filter_context",
            # CS-004 (9..11): under-13 data out of training
            "under_13_sources_excluded_from_training_manifest",
            "verifiable_parental_consent_recorded_for_child_data_use",
            "child_directed_service_data_carries_no_training_flag",
            # shared tail
            "csam_detection_coverage_tested_in_release_gate",
            "child_safety_escalation_path_staffed_and_exercised",
            "age_assurance_vendor_result_bound_to_session",
            "child_data_retention_limited_to_declared_purpose",
            "csam_detection_thresholds_change_only_by_legislation",
            "minor_interaction_safeguards_covered_by_regression_suite",
        ],
        "violate": [
            # CS-001 (0,1)
            "csam_classifier_disabled_on_generation_path",
            "cybertipline_report_path_suppressed_or_batched",
            # CS-002 (2,3)
            "known_csam_hash_match_skipped_at_ingest",
            "hash_matched_shard_written_to_corpus_before_quarantine",
            # CS-003 (4,5)
            "age_assurance_check_removed_from_consumer_signup",
            "minor_mode_restrictions_bypassable_by_client_flag",
            # CS-004 (6,7)
            "under_13_personal_data_ingested_without_parental_consent",
            "child_directed_service_logs_retained_for_training",
            # shared tail
            "csam_preservation_window_shortened_below_one_year",
            "known_csam_hash_list_pinned_to_stale_snapshot",
            "age_signal_dropped_from_request_context_before_safety_filter",
        ],
    },
    "CB": {
        "title": "Catastrophic-risk evaluations: bio/chem, cyber, autonomy and elicitation integrity",
        "risk": "7. Shift-left AI regulation; dangerous-capability gates",
        "comply": [
            # CB-001 (0..2): bio/chem uplift threshold gate
            "bio_chem_uplift_screen_completed_below_threshold",
            "mitigation_package_for_assessed_level_fully_applied",
            "deployment_held_until_threshold_mitigations_verified",
            # CB-002 (3..5): cyber-offence uplift eval
            "cyber_uplift_eval_in_promotion_gate",
            "cyber_uplift_result_attested_by_external_evaluator",
            "cyber_eval_task_set_matches_declared_protocol",
            # CB-003 (6..8): autonomous replication / self-exfiltration
            "autonomous_replication_eval_completed_for_agentic_checkpoint",
            "self_exfiltration_probe_active_in_agent_sandbox",
            "agentic_checkpoint_release_gated_on_autonomy_results",
            # CB-004 (9..11): sandbagging and eval-awareness
            "sandbagging_detector_active_in_eval_harness",
            "eval_awareness_probe_results_included_in_report",
            "elicitation_effort_declared_with_uplift_result",
            # shared tail
            "threshold_determination_made_by_independent_reviewer",
            "uplift_eval_run_on_helpful_only_variant",
            "risk_report_shared_with_governance_body_before_release",
            "mitigation_effectiveness_measured_not_asserted",
            "threshold_crossing_triggers_automatic_deployment_hold",
            "catastrophic_risk_eval_versions_pinned_in_release_record",
        ],
        "violate": [
            # CB-001 (0,1)
            "bio_uplift_threshold_crossed_without_mitigation_package",
            "bio_chem_uplift_screen_result_overridden_by_release_owner",
            # CB-002 (2,3)
            "cyber_uplift_eval_removed_from_promotion_gate",
            "cyber_uplift_eval_run_on_reduced_task_subset_without_disclosure",
            # CB-003 (4,5)
            "autonomous_replication_eval_skipped_for_agentic_checkpoint",
            "self_exfiltration_probe_disabled_in_agent_sandbox",
            # CB-004 (6,7)
            "sandbagging_detector_removed_from_eval_harness",
            "eval_awareness_probe_results_excluded_from_report",
            # shared tail
            "mitigation_package_partially_applied_and_recorded_as_complete",
            "uplift_eval_run_with_safety_training_but_without_elicitation",
            "threshold_determination_made_by_the_team_seeking_release",
        ],
    },
    "WX": {
        "title": "Weight security, insider threat, export classification and sanctions screening",
        "risk": "7. Weight security; 4.2 export and sanctions boundaries",
        "comply": [
            # WX-001 (0..2): egress / DLP on weight stores
            "weight_store_egress_monitoring_active",
            "dlp_alert_on_weights_blocks_transfer",
            "egress_allowlist_limited_to_declared_perimeter",
            # WX-002 (3..5): personnel vetting bound to access
            "weight_access_bound_to_current_vetting_record",
            "weight_access_revoked_on_role_change",
            "insider_anomaly_detection_active_on_training_cluster",
            # WX-003 (6..8): export classification before transfer
            "export_classification_recorded_before_transfer",
            "foreign_national_access_reviewed_under_deemed_export_rule",
            "controlled_technology_boundary_declared_for_cluster",
            # WX-004 (9..11): denied-party / sanctioned-destination screening
            "denied_party_screening_run_at_account_enablement",
            "sanctioned_destination_requests_blocked_at_gateway",
            "screening_hit_held_for_named_reviewer",
            # shared tail
            "weight_store_access_logged_to_tamper_evident_trail",
            "two_person_rule_covers_egress_allowlist_changes",
            "screening_list_refreshed_within_declared_interval",
            "classification_determination_signed_by_trade_counsel",
            "egress_monitoring_coverage_tested_in_drill",
            "vetting_record_expiry_enforced_by_access_system",
        ],
        "violate": [
            # WX-001 (0,1)
            "weight_store_egress_monitoring_disabled",
            "dlp_alert_on_weights_downgraded_to_advisory",
            # WX-002 (2,3)
            "weight_access_granted_without_vetting_record",
            "weight_access_retained_after_role_change",
            # WX-003 (4,5)
            "weights_transferred_without_export_classification_record",
            "foreign_national_access_to_controlled_weights_unreviewed",
            # WX-004 (6,7)
            "denied_party_screening_bypassed_on_account_enablement",
            "sanctioned_destination_blocklist_replaced_by_allow_by_default",
            # shared tail
            "weight_store_egress_allowlist_widened_to_any_destination",
            "insider_anomaly_detection_removed_from_training_cluster",
            "screening_hit_auto_cleared_without_reviewer",
        ],
    },
    "TR": {
        "title": "Transparency, content provenance, documentation and incident reporting",
        "risk": "4.1 Regulatory transparency and provenance obligations",
        "comply": [
            # TR-001 (0..2): synthetic-content marking
            "synthetic_content_marking_present_on_every_modality",
            "marking_survives_downstream_transcoding",
            "marking_detectable_by_public_detection_tool",
            # TR-002 (3..5): GPAI documentation
            "gpai_technical_documentation_current_at_release",
            "training_content_summary_published_on_template",
            "downstream_provider_information_delivered",
            # TR-003 (6..8): transparency report and whistleblower channel
            "transparency_report_published_before_deployment",
            "whistleblower_channel_anonymous_and_reachable",
            "frontier_framework_published_and_reviewed_annually",
            # TR-004 (9..11): incident reporting clock
            "incident_reporting_clock_hardcoded_to_statute",
            "incident_detection_signal_reaches_reporting_queue",
            "incident_severity_assigned_by_named_reviewer",
            # shared tail
            "marking_removal_requires_legislative_change",
            "model_card_diffed_against_previous_release",
            "documentation_ownership_named_on_release_record",
            "reporting_path_exercised_in_drill_within_quarter",
            "redaction_indicators_present_in_public_report",
            "marking_coverage_tested_in_release_gate",
        ],
        "violate": [
            # TR-001 (0,1)
            "synthetic_content_marking_removed_from_output_path",
            "provenance_metadata_stripped_by_downstream_transcoder",
            # TR-002 (2,3)
            "gpai_technical_documentation_stale_at_release",
            "training_content_summary_omitted_from_release",
            # TR-003 (4,5)
            "transparency_report_published_after_deployment",
            "whistleblower_channel_removed_or_deanonymised",
            # TR-004 (6,7)
            "incident_reporting_deadline_made_configurable",
            "incident_detection_signal_routed_away_from_reporting_queue",
            # shared tail
            "marking_made_opt_out_per_tenant",
            "downstream_provider_information_withheld",
            "incident_severity_downgraded_to_avoid_clock",
        ],
    },
    "UH": {
        "title": "User harm: crisis safety, persuasion, high-stakes advice, companion use and abuse",
        "risk": "5.2 User-harm and manipulation guardrails",
        "comply": [
            # UH-001 (0..2): crisis / self-harm classifier
            "self_harm_classifier_active_at_approved_threshold",
            "crisis_resource_handoff_present_in_response_path",
            "self_harm_classifier_covers_streaming_responses",
            # UH-002 (3..5): political persuasion and elections
            "political_persuasion_policy_check_active_for_all_tenants",
            "election_integrity_classifier_in_release_gate",
            "political_content_labelled_per_transparency_rule",
            # UH-003 (6..8): high-stakes advice
            "medical_legal_financial_handoff_present_in_prompt",
            "regulated_profession_disclosure_present_on_request",
            "high_stakes_advice_routed_to_qualified_referral",
            # UH-004 (9..11): companion safeguards for minors
            "minor_break_reminder_active_in_companion_mode",
            "companion_persona_blocks_sexual_content_for_minors",
            "ai_disclosure_present_in_companion_persona",
            # UH-005 (12..14): usage-policy enforcement and abuse monitoring
            "abuse_monitoring_pipeline_at_declared_sample_rate",
            "nonconsensual_intimate_imagery_removed_within_clock",
            "usage_policy_enforcement_actions_active_on_all_tiers",
            # shared tail
            "safety_classifier_threshold_change_reviewed_by_policy_counsel",
            "crisis_handoff_localised_for_served_jurisdictions",
            "persuasion_eval_run_on_release_candidate",
            "dependence_signals_monitored_for_minor_accounts",
            "abuse_reports_routed_to_staffed_trust_and_safety_queue",
            "high_stakes_refusal_and_handoff_covered_by_regression_suite",
        ],
        "violate": [
            # UH-001 (0,1)
            "self_harm_classifier_threshold_raised_to_cut_false_positives",
            "crisis_resource_handoff_removed_from_response_path",
            # UH-002 (2,3)
            "political_persuasion_policy_check_disabled_for_campaign_tenant",
            "election_integrity_classifier_excluded_from_gate",
            # UH-003 (4,5)
            "medical_advice_handoff_removed_from_system_prompt",
            "regulated_profession_disclosure_suppressed_for_brand_voice",
            # UH-004 (6,7)
            "minor_break_reminder_disabled_in_companion_mode",
            "companion_persona_permitted_sexual_content_with_minor_flag",
            # UH-005 (8,9)
            "abuse_monitoring_pipeline_sampled_below_declared_rate",
            "nonconsensual_intimate_imagery_removal_clock_exceeded",
            # shared tail
            "self_harm_classifier_bypassed_for_streaming_responses",
            "ai_disclosure_removed_from_companion_persona",
            "usage_policy_enforcement_actions_disabled_for_enterprise_tier",
        ],
    },
    "PV": {
        "title": "Privacy operations: erasure, retention commitments, tenant isolation, workers and lawful access",
        "risk": "4.2 GDPR/CCPA operations and multi-tenant boundaries",
        "comply": [
            # PV-001 (0..2): erasure / unlearning propagation
            "erasure_request_propagated_to_training_manifest",
            "unlearning_exclusion_list_enforced_at_run_start",
            "erasure_completed_within_statutory_window",
            # PV-002 (3..5): zero-data-retention in code
            "zero_retention_tenant_prompts_never_persisted",
            "retention_policy_enforced_in_code_not_config",
            "debug_capture_disabled_for_zero_retention_tenants",
            # PV-003 (6..8): tenant isolation
            "kv_cache_partitioned_per_tenant",
            "fine_tune_adapter_bound_to_owning_tenant",
            "retrieval_index_scoped_to_tenant_boundary",
            # PV-004 (9..11): annotators and data workers
            "annotator_identity_stripped_from_preference_dataset",
            "data_worker_exposure_limits_enforced_in_queue",
            "annotator_personal_data_processed_under_recorded_basis",
            # PV-005 (12..14): lawful access
            "law_enforcement_request_routed_through_legal_review",
            "government_request_log_append_only_and_complete",
            "customer_notified_of_request_where_lawful",
            # shared tail
            "cross_border_disclosure_conflict_resolved_at_design_time",
            "tenant_isolation_covered_by_regression_suite",
            "erasure_propagation_verified_by_sampling",
            "zero_retention_commitment_tested_in_release_gate",
            "worker_wellbeing_controls_documented_on_pipeline_record",
            "request_response_export_logged_with_scope",
        ],
        "violate": [
            # PV-001 (0,1)
            "erasure_request_not_propagated_to_training_manifest",
            "unlearning_exclusion_list_ignored_by_next_training_run",
            # PV-002 (2,3)
            "zero_retention_tenant_prompts_written_to_debug_store",
            "retention_override_flag_exposed_in_service_config",
            # PV-003 (4,5)
            "kv_cache_shared_across_tenants_for_hit_rate",
            "fine_tune_adapter_loadable_by_another_tenant",
            # PV-004 (6,7)
            "annotator_identity_retained_in_preference_dataset",
            "data_worker_exposure_limits_removed_from_queue_config",
            # PV-005 (8,9)
            "law_enforcement_request_fulfilled_without_legal_review",
            "government_request_log_disabled_for_bulk_export",
            # shared tail
            "retrieval_index_queryable_across_tenant_boundary",
            "erasure_window_extended_beyond_statutory_month",
            "customer_notice_of_request_suppressed_where_lawful",
        ],
    },
}

# Per-family charging threshold. CS and WX carry strict-liability floors
# (18 U.S.C. §2258A; OFAC), so they sit at the low end; CB is a safety family
# with the same character as SF (18); TR, UH and PV are ordinary operational
# families. Note a family at tau <= 20 is charged even when fully compliant.
TAU = {"CS": 16, "CB": 20, "WX": 18, "TR": 24, "UH": 24, "PV": 22}

# --------------------------------------------------------------------------
# New provisions. Dict shape per the extension spec; the merge shim maps
# these onto the pack's tuple convention.
# --------------------------------------------------------------------------

_SB53_PREEMPTION = ("California statute; public domain. Under the federal preemption challenge opened by "
                    "EO 14365 (11 Dec 2025); section pins directionally supported, not verified")

PROVISIONS = [
    # ---- CS: child safety ---------------------------------------------------
    {"id": "FL-CS-001", "family": "CS",
     "title": "Child sexual abuse material detection on uploads, generations and model outputs, and the CyberTipline report and preservation path, are never disabled, sampled down or made configurable",
     "absolute": True,
     "citation": "18 U.S.C. §2258A as amended by the REPORT Act (Pub. L. 118-59, 7 May 2024: one-year preservation, expanded reportable conduct); 18 U.S.C. §2252A; NIST AI 600-1 §2.10 obscene, degrading and abusive content",
     "source_status": "US statute, public domain. Absolute because §2258A(a) is a mandatory reporting duty with criminal penalties for knowing and wilful failure (§2258A(e)); no one below the legislature may accept the risk. The EU AI Act Art. 5 limb on AI-generated CSAM added by Reg. (EU) 2026/1744 is in transition to 2 Dec 2026 and is noted, not relied on",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-04"], "harm_classes": ["legal", "safety", "reputational"]},
    {"id": "FL-CS-002", "family": "CS",
     "title": "Every training-ingest path runs known-abuse-material hash matching before a shard is stored, and a matched shard is quarantined and never enters a corpus",
     "absolute": True,
     "citation": "18 U.S.C. §2252A(a)(2) and (a)(5) (knowing receipt and possession); 18 U.S.C. §2258A; Thorn / All Tech Is Human 'Safety by Design' generative-AI principles (April 2024)",
     "source_status": "US statute, public domain; Safety by Design is a voluntary industry commitment cited as practice, not as law. Absolute because possession of known material in a corpus is a strict criminal exposure with no risk-acceptance route; ingest-time is the only control point that avoids it",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-38"], "harm_classes": ["legal", "safety", "reputational"]},
    {"id": "FL-CS-003", "family": "CS",
     "title": "Age-assurance signals and minor-interaction safeguards on consumer surfaces are enforced server-side and are not removed or made bypassable by a client",
     "absolute": False,
     "citation": "UK Online Safety Act 2023 s.12 and Ofcom Protection of Children Codes (in force 25 July 2025); EU Digital Services Act Art. 28 and Commission Art. 28 guidelines (14 July 2025); California SB 243 companion-chatbot minor safeguards (eff. 1 Jan 2026)",
     "source_status": "UK and EU instruments in force and reusable (OGL v3.0 / 2011/833/EU); SB 243 " + _SB53_PREEMPTION,
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-30"], "harm_classes": ["legal", "safety", "reputational"]},
    {"id": "FL-CS-004", "family": "CS",
     "title": "Personal information from users known to be under thirteen, or from child-directed services, is excluded from training and fine-tuning corpora unless verifiable parental consent covering that use is recorded",
     "absolute": False,
     "citation": "COPPA Rule, 16 CFR Part 312, as amended (90 FR 16918, 22 Apr 2025; effective 23 June 2025; compliance date 22 Apr 2026) — §312.5 verifiable parental consent, §312.10 retention limits",
     "source_status": "US regulation, public domain. Ordinary rather than absolute because the Rule permits the use with separate verifiable parental consent; the provision requires the consent record, not a prohibition",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-38"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- CB: catastrophic-risk evaluations ----------------------------------
    {"id": "FL-CB-001", "family": "CB",
     "title": "No model assessed at or above the biological or chemical uplift threshold is deployed, internally or externally, until the full mitigation package for that level is applied and verified",
     "absolute": True,
     "citation": "Frontier AI Safety Commitments (Seoul, May 2024) Outcome II (OGL v3.0); EU AI Act Art. 55(1)(a)–(b); California SB 53 frontier AI framework (catastrophic-risk assessment and mitigation); NIST AI 600-1 §2.1 CBRN information or capabilities",
     "source_status": "Seoul text quotable under OGL; EU text reusable; SB 53 public domain (under EO 14365 preemption challenge). Absolute because the Seoul commitment and Art. 55(1)(b) leave no derogation route: if mitigations cannot hold risk below the threshold the model is not deployed, and deployment is not reversible",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "FL-CB-002", "family": "CB",
     "title": "A cyber-offence uplift evaluation on the declared task protocol gates every promotion, and its result is attested rather than self-reported",
     "absolute": False,
     "citation": "EU AI Act Art. 55(1)(a) (state-of-the-art model evaluation including adversarial testing); GPAI Code of Practice (10 July 2025) Safety and Security chapter, Measure 3.2; lab frontier frameworks (cyber thresholds), paraphrased",
     "source_status": "EU text reusable; Code of Practice chapter reusable from the Commission PDF, voluntary in status; lab frameworks all rights reserved, paraphrased only",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23"], "harm_classes": ["safety", "regulatory"]},
    {"id": "FL-CB-003", "family": "CB",
     "title": "An autonomous-replication and self-exfiltration evaluation is completed for every agentic checkpoint before release, with the sandbox probes that detect it left active",
     "absolute": False,
     "citation": "EU AI Act Art. 55(1)(a)–(b); GPAI Code of Practice Safety and Security chapter, Appendix 1 (loss-of-control systemic-risk sources); California SB 53 critical-safety-incident definition (loss of control; deceptive evasion of safeguards); lab frontier frameworks (autonomy and AI R&D thresholds), paraphrased",
     "source_status": "EU text reusable; SB 53 public domain (under EO 14365 preemption challenge); lab frameworks paraphrased only. Code of Practice appendix numbering directionally supported, not verified",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23", "S-12"], "harm_classes": ["safety", "regulatory"]},
    {"id": "FL-CB-004", "family": "CB",
     "title": "The evaluation harness carries sandbagging and evaluation-awareness detection, and every uplift result declares the elicitation effort behind it",
     "absolute": False,
     "citation": "GPAI Code of Practice Safety and Security chapter, Measure 3.2 (appropriate elicitation); lab frontier frameworks (Anthropic RSP, OpenAI Preparedness Framework research category 'Sandbagging', DeepMind FSF), paraphrased; METR common elements — full capability elicitation",
     "source_status": "advisory — the detection methods are research practice; the Code is voluntary and the lab frameworks are all rights reserved and self-amendable. Names suggested practice, not a mandate",
     "status": "advisory", "origin": "extension",
     "scenarios": ["S-23", "S-33"], "harm_classes": ["safety", "regulatory"]},

    # ---- WX: weight security, insider threat, export, sanctions -------------
    {"id": "FL-WX-001", "family": "WX",
     "title": "Egress monitoring and data-loss prevention on weight stores and training clusters are never disabled, downgraded to advisory or widened to arbitrary destinations",
     "absolute": True,
     "citation": "EU AI Act Art. 55(1)(d) (cybersecurity of the model and physical infrastructure); GPAI Code of Practice Safety and Security chapter, Commitment 6, Measure 6.2 and Appendix 4 (protect unreleased weights until public or deleted); California SB 53 frontier AI framework (cybersecurity practices for unreleased weights); RAND RR-A2849-1 security levels, cited by link only",
     "source_status": "EU text and Commission-hosted Code PDF reusable; SB 53 public domain (under EO 14365 preemption challenge); RAND noncommercial-use-only, not reproduced. Absolute because weight exfiltration voids every other control at once and has no remediation path; the monitoring is the detection floor for a binding duty",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-27", "S-33", "S-09"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "FL-WX-002", "family": "WX",
     "title": "Access to unreleased weights is bound to a current personnel-vetting record and is revoked automatically on role change or vetting expiry",
     "absolute": False,
     "citation": "GPAI Code of Practice Safety and Security chapter, Commitment 6 (insider threat); California SB 53 frontier AI framework (internal-use and insider-threat governance); RAND RR-A2849-1 SL3+ personnel controls, paraphrased; lab frontier frameworks (security standards), paraphrased",
     "source_status": "Code reusable from Commission PDF, voluntary; SB 53 public domain (under EO 14365 preemption challenge); RAND and lab frameworks cited and paraphrased only",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-27", "S-22"], "harm_classes": ["safety", "legal"]},
    {"id": "FL-WX-003", "family": "WX",
     "title": "An export-classification determination is recorded before model weights or training technology are transferred outside the declared boundary or released to a foreign national",
     "absolute": False,
     "citation": "EAR 15 CFR §734.13(b) (deemed export) and §744.6 (U.S. persons); ECCN 4E091 (closed model weights) as introduced by the AI Diffusion IFR, 90 FR 4544 (15 Jan 2025) — rescinded by BIS in May 2025, status uncertain; ECCNs 3A090 / 4A090 advanced-computing hardware remain in force",
     "source_status": "US regulation, public domain. The AI Diffusion rule was rescinded before its 15 May 2025 compliance date; 4E091 is cited as the identifier for the weight-control concept with status uncertain, and the provision rests on the deemed-export rule and the classification-before-transfer duty, which are in force. Ordinary because classification outcome may be 'EAR99' and counsel may decide; not a floor",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-02"], "harm_classes": ["legal", "regulatory"]},
    {"id": "FL-WX-004", "family": "WX",
     "title": "Denied-party and sanctioned-destination screening on account enablement, enterprise counterparties and weight-transfer recipients is never bypassed, allow-by-default or auto-cleared without a reviewer",
     "absolute": True,
     "citation": "OFAC regulations, 31 CFR Part 501 and the country programmes (strict civil liability; 50 Percent Rule guidance); EAR Entity List, 15 CFR Part 744 Supp. No. 4, and General Prohibition Ten (§736.2(b)(10)); EU restrictive measures under Art. 215 TFEU as applicable to the served jurisdictions",
     "source_status": "US regulations public domain; EU measures reusable. Absolute because OFAC liability is strict: a single shipment of service or weights to a blocked person is a violation regardless of intent, so no risk owner may accept the exposure",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-01", "S-09"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- TR: transparency, provenance, documentation, incident reporting ----
    {"id": "FL-TR-001", "family": "TR",
     "title": "Machine-readable synthetic-content marking on every generative output modality is never removed, made opt-out per tenant or stripped by a downstream stage the provider controls",
     "absolute": True,
     "citation": "EU AI Act Art. 50(2) (applicable from 2 Aug 2026); Commission Code of Practice on Transparency of AI-generated Content; California SB 942 (AI Transparency Act) as amended by AB 853 (operative 2 Aug 2026) latent disclosures; C2PA content-credentials specification, identifier only",
     "source_status": "EU text reusable; in force for systems placed on the market from 2 Aug 2026, with the Reg. (EU) 2026/1744 grace period to 2 Dec 2026 for systems already on the market — this pack's releases are new placements. SB 942/AB 853 public domain (under EO 14365 preemption challenge). Absolute because Art. 50(2) admits no proportionality defence and marking removed at source cannot be restored downstream",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-23"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "FL-TR-002", "family": "TR",
     "title": "General-purpose model technical documentation, downstream-provider information and the public training-content summary are current at release, not carried over from the previous one",
     "absolute": False,
     "citation": "EU AI Act Art. 53(1)(a)–(d) with Annexes XI and XII (applicable 2 Aug 2025; Commission enforcement powers from 2 Aug 2026); Commission training-content summary template (July 2025); GPAI Code of Practice Transparency chapter Model Documentation Form",
     "source_status": "EU text, template and Commission-hosted Code reusable under 2011/833/EU. Ordinary because a documentation gap is correctable after the fact and Art. 53(2) carves out open-source models below systemic risk",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23"], "harm_classes": ["regulatory", "reputational"]},
    {"id": "FL-TR-003", "family": "TR",
     "title": "The frontier transparency report is published at or before deployment, and the anonymous internal safety-concern channel is preserved with its anti-retaliation notice",
     "absolute": False,
     "citation": "California SB 53 (Transparency in Frontier AI Act, signed 29 Sept 2025, eff. 1 Jan 2026) — transparency report and frontier AI framework (Bus. & Prof. Code §22757.12), whistleblower protections (Lab. Code §1107 et seq.); Directive (EU) 2019/1937 whistleblower protection; GPAI Code of Practice Measure 8.3",
     "source_status": _SB53_PREEMPTION + ". Ordinary because the report duty attaches at deployment and is remediable; the channel duty is real but the statute names the employer, not a code path, as the obligor",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23", "S-20"], "harm_classes": ["regulatory", "reputational", "legal"]},
    {"id": "FL-TR-004", "family": "TR",
     "title": "Critical safety incident detection signals reach the reporting queue, and the statutory reporting clock is fixed in code, never configurable, extended or avoided by severity defaults",
     "absolute": True,
     "citation": "California SB 53 critical safety incident reporting to Cal OES within 15 days, 24 hours where imminent risk of death or serious injury (Bus. & Prof. Code §22757.13); EU AI Act Art. 55(1)(c) (serious incidents to the AI Office without undue delay); GPAI Code of Practice Safety and Security chapter, Commitment 9",
     "source_status": _SB53_PREEMPTION + "; EU text reusable and binding since 2 Aug 2025 independent of the state law. Absolute because a statutory notification clock is set by the legislature and no operator may lengthen it; the provision governs the clock's configurability, not the reporting act (which FL-SF-007 already covers)",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04", "S-20", "S-33"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- UH: user harm ------------------------------------------------------
    {"id": "FL-UH-001", "family": "UH",
     "title": "The crisis and self-harm safety classifier and its crisis-resource handoff are never weakened, bypassed for streaming or removed from a consumer response path",
     "absolute": True,
     "citation": "California SB 243 companion-chatbot protocol for suicidal ideation and crisis referral (Bus. & Prof. Code §22601 et seq., eff. 1 Jan 2026); New York Gen. Bus. Law Art. 47 companion-AI safeguards (eff. 5 Nov 2025); NIST AI 600-1 §2.7 human–AI configuration; EU AI Act Art. 5(1)(b) exploitation of vulnerability",
     "source_status": "State statutes public domain, under EO 14365 preemption challenge; EU Art. 5 reusable and in force. Absolute as a safety floor: the harm is irreversible and the protocol duty is set by statute, so a release owner cannot accept the risk to clear false positives",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-05"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "FL-UH-002", "family": "UH",
     "title": "Political-persuasion and election-influence policy checks run for every tenant, and the election-integrity classifier stays in the release gate through an electoral cycle",
     "absolute": False,
     "citation": "Regulation (EU) 2024/900 on transparency and targeting of political advertising (applicable 10 Oct 2025); EU AI Act Art. 50(4) deepfake and public-interest text disclosure; Digital Services Act Arts. 34–35 (systemic risks to electoral processes); NIST AI 600-1 §2.8 information integrity",
     "source_status": "EU texts reusable and in force; NIST public domain and advisory. Ordinary because the persuasion threshold is a policy parameter the governance board sets; the floor is that the check exists and applies uniformly",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-05"], "harm_classes": ["reputational", "legal"]},
    {"id": "FL-UH-003", "family": "UH",
     "title": "High-stakes medical, legal and financial responses keep their qualified-professional handoff and their automated-assistant disclosure in every served persona",
     "absolute": False,
     "citation": "Utah Artificial Intelligence Policy Act, Utah Code §13-72-101 et seq. (disclosure in regulated occupations, as amended 2025); FTC Act §5 (15 U.S.C. §45) deception authority; EU AI Act Art. 50(1) interaction disclosure; Illinois Wellness and Oversight for Psychological Resources Act (2025)",
     "source_status": "Utah code section renumbering and Illinois act text directionally supported, not verified; FTC Act and EU text in force. State instruments under EO 14365 preemption challenge",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "FL-UH-004", "family": "UH",
     "title": "Companion-mode safeguards for accounts flagged as minors — periodic break reminders, sexual-content blocking and an explicit non-human disclosure — are enforced and not persona-configurable",
     "absolute": False,
     "citation": "California SB 243 (Bus. & Prof. Code §22601 et seq.: three-hour break reminders and sexual-content restrictions for minors); New York Gen. Bus. Law Art. 47; FTC Section 6(b) inquiry into AI companions (Sept 2025); NIST AI 600-1 §2.7 emotional entanglement",
     "source_status": "State statutes public domain, under EO 14365 preemption challenge; FTC 6(b) inquiry is advisory signal only. Ordinary because the reminder cadence and blocking scope are parameters the policy board may set within the statute",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-07"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "FL-UH-005", "family": "UH",
     "title": "The usage-policy enforcement and abuse-monitoring pipeline runs at its declared sample rate on every tier, and non-consensual intimate imagery removal completes within the statutory clock",
     "absolute": False,
     "citation": "TAKE IT DOWN Act (Pub. L. 119-12, 19 May 2025; 48-hour notice-and-removal, platform compliance from 19 May 2026); EU AI Act Art. 55(1)(b) systemic-risk mitigation; Digital Services Act Art. 16 notice-and-action; GPAI Code of Practice Measure 5 (safety mitigations, usage monitoring)",
     "source_status": "US statute public domain; EU texts reusable. Ordinary because the sample rate is a governed parameter; the 48-hour removal clock is statutory and a change that made it configurable would engage S-04 through FL-TR-004's reasoning",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-33"], "harm_classes": ["legal", "reputational", "safety"]},

    # ---- PV: privacy operations ---------------------------------------------
    {"id": "FL-PV-001", "family": "PV",
     "title": "Erasure and unlearning requests propagate to training manifests, derived corpora and the next-run exclusion list, and complete within the statutory window",
     "absolute": False,
     "citation": "GDPR Art. 17 with Art. 12(3) (one month, extendable with notice) and Art. 17(2) downstream notification; EDPB Opinion 28/2024 (unlawful development taints deployment unless the model is demonstrably anonymous)",
     "source_status": "EU text reusable; EDPB opinion licence unverified, paraphrased. Ordinary because Art. 17(3) carries exemptions and the technical remedy against trained weights is unsettled; the floor is propagation, not retraining",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-02"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "FL-PV-002", "family": "PV",
     "title": "Zero-data-retention commitments are enforced in the retention code path itself, with no debug capture and no service-level override flag",
     "absolute": False,
     "citation": "GDPR Art. 5(1)(e) storage limitation and Art. 28(3)(a) processing on documented instructions; customer data-processing agreements as the source of the commitment",
     "source_status": "EU text reusable; the zero-retention term itself is contractual, stated as a parameter. Ordinary because the privacy office may vary the commitment by contract; the floor is that code, not configuration, carries it",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-03"], "harm_classes": ["legal", "reputational"]},
    {"id": "FL-PV-003", "family": "PV",
     "title": "Prefix and key-value caches, fine-tune adapters and retrieval indexes are partitioned per tenant and never shared, loadable or queryable across a tenant boundary",
     "absolute": True,
     "citation": "GDPR Art. 5(1)(f) and Art. 32 (integrity, confidentiality, security of processing); Art. 33–34 (a cross-tenant disclosure is a personal-data breach); EU AI Act Art. 55(1)(d) cybersecurity of the model and infrastructure",
     "source_status": "EU text reusable and in force. Absolute because a cross-tenant read is a notifiable breach on first occurrence and a disclosure of one customer's confidential data to another; there is no risk owner with standing to accept it on the disclosed tenant's behalf",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-02", "S-39"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "FL-PV-004", "family": "PV",
     "title": "Annotator and data-worker personal data is processed under a recorded basis, stripped from exported preference datasets, and the workers' graphic-content exposure limits stay enforced in the queue",
     "absolute": False,
     "citation": "GDPR Art. 88 (employment context) and Art. 32; Directive (EU) 2024/2831 on platform work (transposition by 2 Dec 2026 — deferred, noted); Partnership on AI Responsible Sourcing of Data Enrichment Services guidelines (advisory)",
     "source_status": "EU text reusable and in force for the GDPR limbs; the Platform Work Directive is deferred until transposition and is cited as context, not relied on; PAI guidance advisory",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-22"], "harm_classes": ["legal", "reputational"]},
    {"id": "FL-PV-005", "family": "PV",
     "title": "Government and law-enforcement requests for user data pass legal review before disclosure, are logged append-only with their scope, and trigger customer notice where the law allows",
     "absolute": False,
     "citation": "Stored Communications Act, 18 U.S.C. §§2702–2703; CLOUD Act, 18 U.S.C. §2713; GDPR Art. 48 (transfers or disclosures not authorised by Union law); EU–US Data Privacy Framework adequacy decision (10 July 2023)",
     "source_status": "US statute public domain; EU text reusable. Ordinary because disclosure without notice is lawful under a non-disclosure order and legal review may lawfully approve; the floor is that review and logging happen",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-19", "S-02"], "harm_classes": ["legal", "reputational"]},
]

# --------------------------------------------------------------------------
# Scenario mapping for every EXISTING family (coverage matrix, VC-50).
# --------------------------------------------------------------------------

FAMILY_SCENARIOS = {
    "MB": ["S-13", "S-14"],
    "TD": ["S-38"],
    "PI": ["S-02", "S-18", "S-03"],
    "AG": ["S-15", "S-12", "S-13"],
    "LS": ["S-39", "S-14"],
    "EV": ["S-23", "S-33"],
    "SF": ["S-09", "S-23", "S-27", "S-20"],
    "IN": ["S-36"],
    "FG": ["S-12"],
    "BS": ["S-06", "S-30"],
    "IP": ["S-38"],
    "SC": ["S-13", "S-14"],
    "AS": ["S-39", "S-14"],
    "GV": ["S-34", "S-11", "S-05", "S-03"],
}

# Per-provision overrides where an existing provision maps more precisely
# than its family.
PROVISION_SCENARIOS = {
    "FL-GV-001": ["S-11"],
    "FL-GV-002": ["S-05"],
    "FL-GV-003": ["S-03"],
    "FL-GV-004": ["S-23"],
    "FL-SF-002": ["S-09", "S-27"],
    "FL-SF-003": ["S-27"],
    "FL-SF-007": ["S-04", "S-20"],
    "FL-PI-005": ["S-03", "S-02"],
    "FL-LS-002": ["S-39", "S-14"],
    "FL-SC-008": ["S-14"],
    "FL-EV-002": ["S-23", "S-33"],
    "FL-AG-002": ["S-15"],
}

# --------------------------------------------------------------------------
# Draft amendments: findings about EXISTING provisions, filed under A3 and
# not applied. The pack has none on file, so the sequence starts at PA-01.
# --------------------------------------------------------------------------

PROPOSED_AMENDMENTS = [
    {
        "id": "PA-01",
        "targets": ["FL-SF-007"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "The provision cites only 'California SB 53 (15-day / 24-hour)'. Verified: EU AI Act Art. 55(1)(c) has bound systemic-risk GPAI providers since 2 Aug 2025 to report serious incidents to the AI Office without undue delay, and it attaches at the 10^25 FLOP presumption, not SB 53's 10^26 — so a run can owe an EU report and no Californian one. Separately, SB 53 is under the EO 14365 preemption challenge and the pack carries no instability flag on it.",
        "proposed": "Restate the citation as 'California SB 53 §22757.13 (15-day / 24-hour; under EO 14365 preemption challenge); EU AI Act Art. 55(1)(c); GPAI Code of Practice Commitment 9'. Leave the provision ordinary; the extension's FL-TR-004 carries the configurability floor for the clock itself, and the two should be read together.",
        "why_not_applied": "Changing a provision's stated source changes what a later adjudicator reasons from. That is a legislative act under A3, not an editorial one.",
        "disposition": "pending",
    },
    {
        "id": "PA-02",
        "targets": ["FL-SF-002", "FL-SF-003"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "Both weight-security absolutes rest on 'California SB 53' plus RAND security levels (FL-SF-002) and on 'practice policy; RAND SL3+ paraphrased' (FL-SF-003). The strongest binding source — EU AI Act Art. 55(1)(d), in force since 2 Aug 2025, with GPAI Code of Practice Commitment 6 / Measure 6.2 / Appendix 4 as the presumption-of-conformity route — is cited by neither. FL-SF-003 is an absolute whose only external authority is a noncommercial-use-only report; as written it reads as a severity claim rather than a who-may-decide floor.",
        "proposed": "Add Art. 55(1)(d) and Code of Practice Commitment 6 to both citations. Keep both absolute: the two-person rule is the access-control floor that Measure 6.2 names, and the citation change gives it the statutory footing its absolute status needs.",
        "why_not_applied": "The 290 F-absolute cases in the shipped corpus cite these provisions as they stand; re-grounding a floor is for the responsible-scaling council, not the corpus author.",
        "disposition": "pending",
    },
    {
        "id": "PA-03",
        "targets": ["FL-GV-001"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "The provision cites 'EU AI Act Art. 14(4)–(5)' alongside GDPR Art. 22(3) and the CPPA ADMT regulations as if all three bound now. Verified: Art. 14 sits in the Annex III high-risk block that Reg. (EU) 2026/1744 deferred to 2 Dec 2027 — the same deferral the pack itself records on FL-GV-009, FL-GV-010 and FL-GV-011 for Arts. 9, 10 and 15. The absolute status still stands on GDPR Art. 22(3) (in force) and the CPPA ADMT rules (effective 1 Jan 2026, compliance 1 Jan 2027).",
        "proposed": "Restate the citation as 'GDPR Art. 22(3); CPPA ADMT regulations; EU AI Act Art. 14(4)–(5) (deferred to 2 Dec 2027 by Reg. (EU) 2026/1744)'. Keep absolute on the in-force limbs.",
        "why_not_applied": "A citation that mis-states an instrument's application date is a defect in the rulebook, and the rulebook changes only by enactment (A3, FL-GV-006).",
        "disposition": "pending",
    },
    {
        "id": "PA-04",
        "targets": ["FL-GV-002"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "The provision cites 'EU AI Act Art. 5' as of the original Regulation. Reg. (EU) 2026/1744 inserted a new Art. 5 prohibition on AI systems generating non-consensual intimate imagery and child sexual abuse material, with a transitional period to 2 Dec 2026. The pack's Art. 5 floor therefore has a limb that is enacted but not yet binding, and the provision text ('practices prohibited under Article 5') will silently widen on that date.",
        "proposed": "Add to the citation 'as amended by Reg. (EU) 2026/1744 — NCII/CSAM limb binding from 2 Dec 2026', and record in source_status that until then the CSAM limb is carried by the extension's FL-CS-001 under 18 U.S.C. §2252A rather than by Art. 5.",
        "why_not_applied": "Widening an absolute's scope, even by acknowledging an amendment to its source, is a legislative act; the responsible-scaling council should decide whether the limb becomes absolute on 2 Dec 2026 or stays deferred in a separate provision.",
        "disposition": "pending",
    },
    {
        "id": "PA-05",
        "targets": ["FL-BS-001"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "The only absolute in the brand-safety family cites 'risk architecture §5.2' alone. Under Definition 1 an absolute means no one below the legislature may decide, not that the harm is severe. A toxicity threshold is, by the pack's own FL-BS-006 and the 'toxicity_threshold_relaxed_without_approval' factor, a governed parameter with an approval route — which is the signature of an ordinary provision. The provision reads as a severity claim.",
        "proposed": "Either ground the floor in an external instrument (EU AI Act Art. 55(1)(b) systemic-risk mitigation for the flagged-content classes; DSA Art. 16 for illegal content) and narrow it to illegal-content classes, or reclassify it as ordinary with the policy board as the named exception authority.",
        "why_not_applied": "Reclassifying an absolute rewrites which cases short-circuit under A6 and would re-base every F-absolute case that cites it.",
        "disposition": "pending",
    },
    {
        "id": "PA-06",
        "targets": ["FL-TD-001"],
        "raised_by": "scenario-extension survey 2026-09 (frontierllm)",
        "finding": "The absolute provenance floor cites 'DSM Directive 2019/790 Art. 4; EDPB Opinion 28/2024'. Verified: Art. 4 of the DSM Directive is the text-and-data-mining exception with its opt-out — it is the source for FL-TD-003, not for a prohibited-provenance bar. The instruments that actually make provenance a floor are EU AI Act Art. 5(1)(e) (untargeted facial-image scraping, in force since 2 Feb 2025) and the EDPB's holding (4) on unlawful development tainting deployment; the LAION appeal (BGH hearing 3 Sept 2026) may also move the Art. 4 contours.",
        "proposed": "Restate the citation as 'EU AI Act Art. 5(1)(e); EDPB Opinion 28/2024 holding (4); DSM Directive 2019/790 Art. 4(3) for the opt-out limb only', and flag the LAION appeal as an instability marker.",
        "why_not_applied": "Changing the grounding of an absolute is a legislative act; the finding is filed for the privacy-and-data-stewardship office.",
        "disposition": "pending",
    },
]

# New families whose cases concern a named model line, checkpoint or asset
# (the pack's MODEL_FACING_FAMILIES semantics). PV is infrastructural.
FLOOR_FACING_FAMILIES = {"CS", "CB", "WX", "TR", "UH"}
