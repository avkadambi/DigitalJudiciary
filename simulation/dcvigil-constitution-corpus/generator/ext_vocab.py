"""
DCVigil Constitution Corpus — scenario extension (corpus 2.0.0).

New provision families closing the gaps the architect's scenario survey found in
this pack's constitution: lawful access and legal hold, life-safety systems,
statutory energy and sustainability reporting, customer-trust duties owed to a
tenant (keys, exit, sub-processors, audit rights), OT protocol security,
product-security assurance, accessibility of the operator and customer surfaces,
and trade controls on a product that ships privileged agents worldwide.

Everything here is additive (Axiom A3). No existing provision, factor, title or
absolute flag is edited. Findings about existing provisions are filed below as
draft amendments continuing the pack's sequence at PA-06.

Licensing posture is vocab.py's: EU law is reusable under Commission Decision
2011/833/EU; US statutes, CFR and NIST SP 800-53 are public domain; ISO, IEC,
NFPA, AICPA and PCI material is cited by identifier only, with no text
reproduced. Provision prose is original drafting.

Citations were shelf-life checked on 6 September 2026. Where an instrument's
application date has not yet arrived, or where a status could not be confirmed,
the provision's status and source_status say so rather than asserting.

Factor pools are sliced positionally by the generator: the n-th provision of a
family receives comply[3n:3n+8] and violate[2n:2n+5] with wrap-around, so each
provision's decisive violate factors sit at 2n and 2n+1 and its most
characteristic comply factors at 3n..3n+2. The pools below are ordered for that.
"""

# --------------------------------------------------------------------------
# New families.
# --------------------------------------------------------------------------

FAMILIES = {
    "LA": {
        "title": "Lawful access, legal hold and government requests",
        "risk": "4. Customer contractual floor; litigation-hold and lawful-access duties",
        "comply": [
            # LA-001 (0..2)
            "legal_hold_flag_blocks_every_deletion_path",
            "hold_scope_resolved_before_retention_job_runs",
            "hold_release_requires_named_legal_approver",
            # LA-002 (3..5)
            "legal_process_reviewed_by_counsel_before_disclosure",
            "customer_notice_sent_unless_notice_is_prohibited",
            "disclosure_scope_narrowed_to_the_order_terms",
            # LA-003 (6..8)
            "conflicting_disclosure_duty_escalated_before_build",
            "foreign_order_routed_through_the_treaty_channel",
            "blocking_statute_conflict_recorded_in_design_record",
            # LA-004 (9..11)
            "disclosure_register_entry_written_per_request",
            "disclosure_register_append_only_and_exportable",
            "published_request_counts_derived_from_the_register",
            # shared tail
            "hold_notice_acknowledged_by_the_named_custodian",
            "preservation_copy_stored_outside_the_expiring_tier",
            "hold_covers_derived_and_aggregated_stores",
            "requester_identity_and_legal_basis_recorded",
            "emergency_disclosure_reviewed_after_the_fact",
        ],
        "violate": [
            # LA-001 (0,1)
            "retention_job_deletes_records_under_an_open_hold",
            "legal_hold_flag_ignored_by_the_new_purge_path",
            # LA-002 (2,3)
            "customer_content_disclosed_without_legal_review",
            "customer_notice_suppressed_where_notice_is_permitted",
            # LA-003 (4,5)
            "foreign_order_answered_directly_from_the_export_tool",
            "conflicting_disclosure_duty_left_unresolved_at_design",
            # LA-004 (6,7)
            "disclosure_register_entry_omitted_for_urgent_requests",
            "disclosure_register_made_editable_by_support_role",
            # shared tail
            "hold_release_automated_without_legal_approval",
            "preservation_copy_stored_in_the_expiring_tier",
            "requester_identity_not_recorded_on_the_request",
        ],
    },
    "LS": {
        "title": "Life-safety systems and physical resilience",
        "risk": "Life-safety floor; 5.1 blast radius at the physical boundary",
        "comply": [
            # LS-001 (0..2)
            "suppression_and_epo_circuits_excluded_from_action_planner",
            "life_safety_interlock_integration_is_read_only",
            "ups_transfer_command_absent_from_the_action_catalogue",
            # LS-002 (3..5)
            "generator_run_record_written_from_the_controller_reading",
            "fuel_level_series_sourced_from_the_tank_sensor",
            "load_bank_test_result_stored_with_its_raw_trace",
            # LS-003 (6..8)
            "physical_incident_report_path_kept_reachable",
            "physical_incident_classified_against_published_criteria",
            "resilience_measure_evidence_versioned_in_the_repo",
            # shared tail
            "alarm_relay_path_verified_after_every_release",
            "fire_panel_integration_is_monitoring_only",
            "life_safety_alarm_never_deduplicated_away",
            "site_walkdown_evidence_linked_to_the_asset_record",
            "emergency_power_test_cadence_encoded_in_the_scheduler",
        ],
        "violate": [
            # LS-001 (0,1)
            "suppression_release_reachable_from_the_action_planner",
            "emergency_power_off_wired_into_automated_recovery",
            # LS-002 (2,3)
            "generator_test_result_back_filled_from_the_schedule",
            "fuel_level_series_synthesised_when_the_sensor_is_silent",
            # LS-003 (4,5)
            "physical_incident_report_path_removed_from_the_runbook",
            "resilience_evidence_kept_only_in_a_personal_export",
            # shared tail
            "fire_panel_integration_given_a_write_endpoint",
            "life_safety_alarm_folded_into_the_deduplication_window",
            "ups_transfer_added_to_the_automated_recovery_plan",
        ],
    },
    "EN": {
        "title": "Energy, water and sustainability reporting integrity",
        "risk": "4. Regulatory reporting; facility efficiency and ESG disclosure",
        "comply": [
            # EN-001 (0..2)
            "reported_energy_figure_derived_from_metered_series",
            "statutory_submission_job_runs_on_the_published_cadence",
            "submission_payload_hashed_and_retained_with_the_filing",
            # EN-002 (3..5)
            "efficiency_metric_boundary_and_denominator_declared",
            "metric_method_change_restates_the_published_series",
            "waste_heat_recovery_data_recorded_per_site",
            # EN-003 (6..8)
            "sustainability_datapoint_traceable_to_its_source_system",
            "esg_metric_lineage_versioned_alongside_the_pipeline",
            "estimated_values_labelled_as_estimates_in_the_export",
            # shared tail
            "water_usage_series_sourced_from_the_site_meter",
            "renewable_share_evidenced_by_supplier_records",
            "missing_interval_reported_as_a_gap_not_interpolated",
            "reporting_boundary_change_recorded_with_effective_date",
            "assurance_export_reproducible_from_the_raw_series",
        ],
        "violate": [
            # EN-001 (0,1)
            "statutory_energy_submission_disabled_for_a_named_site",
            "reported_energy_figure_overridden_by_a_manual_constant",
            # EN-002 (2,3)
            "efficiency_denominator_changed_without_restating_series",
            "waste_heat_data_dropped_from_the_site_export",
            # EN-003 (4,5)
            "sustainability_datapoint_sourced_from_an_untracked_sheet",
            "estimated_value_published_without_an_estimate_label",
            # shared tail
            "missing_meter_interval_interpolated_into_the_filing",
            "water_usage_series_replaced_by_a_design_figure",
            "reporting_boundary_narrowed_without_an_effective_date",
        ],
    },
    "CT": {
        "title": "Customer trust: tenant keys, exit, sub-processors and audit rights",
        "risk": "4. Multi-tenant contractual floor; processor duties owed to the controller",
        "comply": [
            # CT-001 (0..2)
            "tenant_key_material_held_in_a_per_tenant_key_ring",
            "customer_managed_key_reference_resolved_per_request",
            "key_revocation_renders_only_that_tenant_unreadable",
            # CT-002 (3..5)
            "offboarding_export_produced_within_contracted_window",
            "deletion_certificate_issued_after_the_final_purge",
            "backup_expiry_aligned_with_the_deletion_commitment",
            # CT-003 (6..8)
            "sub_processor_notice_sent_before_processing_starts",
            "objection_window_honoured_before_traffic_cuts_over",
            "sub_processor_register_updated_with_region_and_purpose",
            # CT-004 (9..11)
            "per_tenant_evidence_export_available_to_the_customer",
            "regulated_regime_flag_carried_through_every_pipeline",
            "audit_right_request_tracked_with_a_named_owner",
            # shared tail
            "key_ring_separation_verified_by_a_restore_drill",
            "residual_derived_data_enumerated_before_deletion",
            "exit_export_format_documented_in_the_agreement",
            "processing_register_updated_with_the_change",
            "tenant_retention_term_read_from_the_contract_record",
        ],
        "violate": [
            # CT-001 (0,1)
            "tenant_keys_pooled_into_one_platform_key_ring",
            "customer_managed_key_replaced_by_a_platform_default",
            # CT-002 (2,3)
            "offboarding_export_deferred_past_contracted_window",
            "deleted_tenant_data_left_in_the_derived_feature_store",
            # CT-003 (4,5)
            "sub_processor_added_before_any_customer_notice",
            "objection_window_skipped_for_an_urgent_cutover",
            # CT-004 (6,7)
            "per_tenant_evidence_export_removed_from_the_portal",
            "regulated_regime_flag_dropped_by_the_new_writer",
            # shared tail
            "backup_retention_outlives_the_deletion_commitment",
            "tenant_retention_term_hardcoded_across_all_customers",
            "sub_processor_register_left_unchanged_after_the_move",
        ],
    },
    "OT": {
        "title": "OT protocols, zoning and device firmware",
        "risk": "2. Facility network exposure; OT segmentation and device integrity",
        "comply": [
            # OT-001 (0..2)
            "conduit_allow_list_enumerates_every_permitted_flow",
            "building_management_traffic_confined_to_its_zone",
            "ipmi_endpoints_reachable_only_from_management_zone",
            # OT-002 (3..5)
            "authenticated_snmp_v3_used_on_new_device_paths",
            "device_credentials_unique_per_controller",
            "plaintext_device_protocol_wrapped_in_a_tunnel",
            # OT-003 (6..8)
            "gateway_firmware_signature_verified_before_flash",
            "firmware_version_and_hash_recorded_per_device",
            "firmware_rollback_image_retained_for_the_window",
            # shared tail
            "modbus_write_registers_blocked_on_the_poller_role",
            "bacnet_write_service_disabled_on_the_collector",
            "zone_boundary_change_reviewed_before_merge",
            "device_discovery_confined_to_the_declared_subnets",
            "vendor_maintenance_path_time_boxed_and_recorded",
        ],
        "violate": [
            # OT-001 (0,1)
            "conduit_allow_list_replaced_by_a_flat_route",
            "building_management_network_bridged_to_corporate_zone",
            # OT-002 (2,3)
            "snmp_v2c_community_string_used_on_a_new_device_path",
            "ipmi_credentials_shared_across_the_rack_fleet",
            # OT-003 (4,5)
            "gateway_firmware_flashed_without_signature_check",
            "firmware_version_left_unrecorded_after_the_flash",
            # shared tail
            "bacnet_write_service_enabled_on_the_polling_service",
            "modbus_writes_opened_to_the_shared_collector_role",
            "device_discovery_widened_to_the_whole_site_range",
        ],
    },
    "SV": {
        "title": "Product security assurance and vulnerability handling",
        "risk": "1.1 Product security; customer-deployed agent under a disclosure duty",
        "comply": [
            # SV-001 (0..2)
            "sbom_published_with_every_customer_facing_release",
            "exploitability_statement_issued_for_each_finding",
            "sbom_regenerated_when_a_dependency_changes",
            # SV-002 (3..5)
            "exploited_vulnerability_report_path_wired_to_intake",
            "severe_incident_clock_started_at_first_awareness",
            "reporting_owner_named_in_the_release_record",
            # SV-003 (6..8)
            "disclosure_intake_address_published_and_monitored",
            "researcher_report_acknowledged_within_the_window",
            "fix_or_mitigation_shipped_within_severity_deadline",
            # SV-004 (9..11)
            "penetration_test_scheduled_for_each_customer_surface",
            "developer_security_testing_evidence_on_the_release",
            "flaw_remediation_deadline_tracked_per_severity_band",
            # SV-005 (12..14)
            "customer_incident_notice_published_on_the_status_page",
            "root_cause_analysis_delivered_within_the_window",
            "status_page_hosted_independently_of_the_platform",
            # shared tail
            "advisory_identifier_assigned_before_publication",
            "component_provenance_recorded_in_the_release_manifest",
            "regression_test_added_for_every_fixed_vulnerability",
            "severity_scoring_method_declared_in_the_advisory",
            "incident_timeline_reconstructed_from_recorded_events",
        ],
        "violate": [
            # SV-001 (0,1)
            "sbom_generation_dropped_from_the_release_pipeline",
            "exploitability_statement_omitted_for_known_finding",
            # SV-002 (2,3)
            "exploited_vulnerability_report_left_without_an_owner",
            "severe_incident_clock_started_at_triage_not_awareness",
            # SV-003 (4,5)
            "disclosure_intake_address_removed_from_the_site",
            "patch_deadline_extended_without_a_recorded_decision",
            # SV-004 (6,7)
            "penetration_test_dropped_for_the_portal_release_train",
            "security_testing_evidence_omitted_from_the_release",
            # SV-005 (8,9)
            "status_page_hosted_on_the_platform_it_reports_on",
            "root_cause_analysis_reduced_to_a_one_line_summary",
            # shared tail
            "advisory_published_without_a_severity_method",
            "fixed_vulnerability_shipped_without_a_regression_test",
            "component_provenance_left_out_of_release_manifest",
        ],
    },
    "AX": {
        "title": "Accessibility of the operator console and customer portal",
        "risk": "Customer-facing and operator surfaces; civil-rights floor",
        "comply": [
            # AX-001 (0..2)
            "accessibility_gate_runs_on_every_portal_release",
            "conformance_failure_blocks_the_portal_release",
            "manual_screen_reader_pass_recorded_for_new_views",
            # AX-002 (3..5)
            "alarm_severity_conveyed_by_text_and_shape",
            "audible_alert_paired_with_a_visible_equivalent",
            "contrast_ratio_verified_on_the_operations_dashboard",
            # shared tail
            "keyboard_path_covers_every_acknowledgement_control",
            "accessible_name_present_on_every_dashboard_control",
            "focus_order_verified_on_the_incident_drawer",
            "session_timeout_extendable_by_the_operator",
            "accessibility_statement_versioned_beside_the_code",
        ],
        "violate": [
            # AX-001 (0,1)
            "accessibility_gate_removed_from_the_portal_pipeline",
            "conformance_failures_downgraded_to_build_warnings",
            # AX-002 (2,3)
            "alarm_severity_conveyed_by_colour_alone",
            "audible_alert_shipped_with_no_visible_equivalent",
            # shared tail
            "acknowledgement_control_reachable_only_by_pointer",
            "dashboard_control_shipped_without_accessible_name",
            "operator_session_expires_with_no_extension_path",
        ],
    },
    "TC": {
        "title": "Trade controls: restricted-party screening and export classification",
        "risk": "4. Regulatory floor on a product distributed to customer estates worldwide",
        "comply": [
            # TC-001 (0..2)
            "counterparty_screened_against_current_restricted_lists",
            "screening_list_refreshed_from_the_published_source",
            "ownership_chain_checked_against_the_fifty_percent_rule",
            # TC-002 (3..5)
            "encryption_classification_recorded_before_publication",
            "restricted_destination_check_gates_the_download",
            "licence_exception_basis_recorded_for_the_agent",
            # shared tail
            "screening_hit_routed_to_trade_compliance",
            "screening_result_retained_with_the_onboarding_record",
            "deemed_export_check_run_before_support_access",
            "destination_derived_from_verified_account_data",
            "classification_reviewed_when_the_crypto_stack_changes",
        ],
        "violate": [
            # TC-001 (0,1)
            "restricted_party_screening_bypassed_for_fast_onboarding",
            "screening_list_pinned_to_a_stale_local_copy",
            # TC-002 (2,3)
            "agent_download_endpoint_opened_to_every_destination",
            "encryption_classification_left_unrecorded_at_release",
            # shared tail
            "ownership_chain_check_skipped_for_a_subsidiary_account",
            "screening_hit_auto_cleared_by_the_onboarding_job",
            "support_access_granted_without_deemed_export_check",
        ],
    },
}

# Strict-liability floors (spoliation, life safety, sanctions) take low tau;
# ordinary operational families sit in the middle. A family at tau <= 20 is
# charged even when fully compliant, which is the intended posture for LA, LS,
# CT and TC: their cases should reach an adjudicator rather than a gate.
TAU = {
    "LA": 16,
    "LS": 15,
    "EN": 26,
    "CT": 20,
    "OT": 24,
    "SV": 28,
    "AX": 30,
    "TC": 15,
}

# --------------------------------------------------------------------------
# New provisions. Ids continue the pack's DV-NNN sequence after DV-416.
# --------------------------------------------------------------------------

PROVISIONS = [
    # ---- LA: lawful access, legal hold and government requests -----------
    {"id": "DV-417", "family": "LA",
     "title": "A preservation hold overrides every deletion, expiry, purge and anonymisation path, including derived and aggregated stores, and is released only by a named legal approver",
     "absolute": True,
     "citation": "Fed. R. Civ. P. 37(e) (loss of electronically stored information that should have been preserved); GDPR Art. 17(3)(b) (erasure does not apply where processing is necessary for compliance with a legal obligation)",
     "source_status": "US Federal Rules and EU text are both reusable. Absolute in the sense of Definition 1: once the duty to preserve has attached, no engineer, manager or risk owner at the provider may accept the risk of deleting the material — the sanction under Rule 37(e)(2) reaches intent to deprive, and the countervailing erasure duty is expressly disapplied by Art. 17(3)(b).",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-19", "S-03"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "DV-418", "family": "LA",
     "title": "No path discloses customer content to a government or law-enforcement requester without recorded legal review of the process served, disclosure narrowed to its terms, and notice to the customer unless notice is prohibited",
     "absolute": True,
     "citation": "Stored Communications Act, 18 U.S.C. §2702–2703 (disclosure prohibited except as provided; §2705(b) non-disclosure orders); 18 U.S.C. §2713 (CLOUD Act, records within possession, custody or control)",
     "source_status": "US statute — public domain. Absolute because voluntary disclosure outside the §2702(b)–(c) exceptions is unlawful on its face and exposes the provider to §2707 civil liability; it is not a risk anyone below the legislature may accept. The customer-notice limb is a contractual commitment and is expressly conditioned on notice not being prohibited.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-19", "S-02"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "DV-419", "family": "LA",
     "title": "Where a disclosure duty in one jurisdiction conflicts with a prohibition in another, the conflict is resolved before the pipeline is built, and no code path answers a foreign order directly out of the export tooling",
     "absolute": False,
     "citation": "GDPR Art. 48 (third-country judgments and orders enforceable only through a mutual legal assistance treaty or international agreement); 18 U.S.C. §2703(h) (comity motion to quash for a qualifying foreign government); EU–US Data Privacy Framework adequacy decision of 10 July 2023",
     "source_status": "EU and US texts reusable. Ordinary rather than absolute because the resolution is a design and legal judgement rather than a fixed floor; the floor itself is stated by DV-418. The DPF adequacy decision was upheld by the General Court in September 2025 (Latombe); an appeal is possible, so treat adequacy as current but not permanent.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-19", "S-02"], "harm_classes": ["legal", "regulatory"]},
    {"id": "DV-420", "family": "LA",
     "title": "Every request for customer data and every disclosure made in answer to one is written to an append-only register carrying the requester, the legal basis and the scope, from which the published request counts are derived",
     "absolute": False,
     "citation": "NIST SP 800-53 AU-9 (protection of audit information); GDPR Art. 30(2) (processor records of processing); 18 U.S.C. §2702(b)(8) emergency disclosures, which the register must also capture",
     "source_status": "NIST text is public domain (CC0 via oscal-content); EU text reusable. Ordinary: the duty to keep the record is well grounded, the reporting cadence is a contractual and voluntary-transparency commitment.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-19", "S-33"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- LS: life-safety systems and physical resilience ------------------
    {"id": "DV-421", "family": "LS",
     "title": "Fire detection and suppression, emergency power off, and UPS or transfer-switch operation are never actuated, inhibited or silenced by monitoring or remediation software; the integration to these systems is monitoring-only",
     "absolute": True,
     "citation": "Life-safety floor; NFPA 72, NFPA 75 and NFPA 76 (identifiers only — no text reproduced); OSHA 29 CFR 1910.147 by analogy for the de-energisation case",
     "source_status": "US CFR is public domain; NFPA documents are cited by identifier only and their text is not reproduced. Absolute in the sense of Definition 1: an unintended suppression discharge, a wrongly asserted emergency power off, or a silenced alarm can kill someone in the room, and there is no officer of the provider who may accept that risk on the occupants' behalf. Distinct from the shipped DV-302 and from DV-340, whose enumerations reach power, cooling, setpoints and physical access control but not the fire and emergency-power chain — see proposed amendment PA-09.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "DV-422", "family": "LS",
     "title": "Generator run records, transfer-switch events, fuel-level series and load-bank test results are written from the controller or sensor reading, never back-filled from a schedule, interpolated across a silent sensor or reconstructed after the fact",
     "absolute": False,
     "citation": "NIST SP 800-53 AU-9 and SI-7 (integrity of recorded evidence); NFPA 110 and NFPA 72 test-record identifiers (identifiers only); customer resilience commitments",
     "source_status": "NIST text is public domain; NFPA is cited by identifier only. Ordinary rather than absolute: the record's integrity is an evidence duty, and the standards that set the test cadence bind the facility operator rather than this platform. Directionally supported for the pack's colocation customers, not verified against any single customer's contract.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08", "S-33"], "harm_classes": ["safety", "regulatory", "financial"]},
    {"id": "DV-423", "family": "LS",
     "title": "The path by which a physical-resilience incident at a customer site is classified and reported to the designated authority stays reachable, and the evidence of the resilience measures it rests on is versioned in the repository",
     "absolute": False,
     "citation": "Directive (EU) 2022/2557 (Critical Entities Resilience) Art. 13 (resilience measures) and Art. 15 (incident notification, 24-hour initial notification where transposed)",
     "source_status": "EU text reusable under 2011/833/EU. Marked deferred rather than in force: the transposition deadline was 17 October 2024 and Member States were to identify critical entities by 17 July 2026, but transposition and designation remain incomplete across the Union as of 6 September 2026, so the operative duty is the applicable national law and does not yet bind at every site the pack models. Same posture as the shipped DV-407 takes for NIS2.",
     "status": "deferred", "origin": "extension",
     "scenarios": ["S-36", "S-04"], "harm_classes": ["regulatory", "safety"]},

    # ---- EN: energy, water and sustainability reporting -------------------
    {"id": "DV-424", "family": "EN",
     "title": "A figure submitted under a statutory energy or facility-reporting scheme is derived from the metered series, is never overridden by a manual constant or a design value, and no change disables, delays or narrows the submission job for a named site",
     "absolute": True,
     "citation": "Directive (EU) 2023/1791 (Energy Efficiency Directive) Art. 12 and Annex VII; Commission Delegated Regulation (EU) 2024/1364 of 14 March 2024 on the first phase of the common Union rating scheme for data centres; Energiedienstleistungsgesetz and Energieeffizienzgesetz (EnEfG) §11–§12 for German sites",
     "source_status": "EU text reusable under 2011/833/EU; German federal statute is an edict of government. Absolute in the sense of Definition 1: a knowingly untrue submission to a public register is a matter for the legislature and the supervisory authority, not for a risk owner at the provider. Reporting under 2024/1364 runs annually by 15 May for data centres at or above the 500 kW installed IT power demand threshold; sites below it are out of scope and a change that turns off the job for such a site does not engage this rule.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-21", "S-04"], "harm_classes": ["regulatory", "legal", "reputational"]},
    {"id": "DV-425", "family": "EN",
     "title": "Efficiency and water metrics declare their boundary, denominator and measurement interval; a change to the method restates the published series rather than creating a silent discontinuity, and waste-heat data is recorded per site",
     "absolute": False,
     "citation": "Delegated Regulation (EU) 2024/1364 Annex (reported indicators, including power usage effectiveness and water usage effectiveness); EnEfG §11 (avoidance and use of waste heat) and §12 (information on waste heat)",
     "source_status": "EU text reusable; German statute is an edict of government. Ordinary because the choice of boundary is legitimately the operator's — the duty is to declare it and to keep the series comparable. The ASHRAE and Uptime Institute vocabulary the pack's DV-410 gestures at remains advisory and paywalled, and is not relied on here.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-21"], "harm_classes": ["regulatory", "reputational"]},
    {"id": "DV-426", "family": "EN",
     "title": "Every sustainability datapoint the platform produces for a customer's disclosure is traceable to its source system, its lineage is versioned with the pipeline, and estimated values are labelled as estimates in the export",
     "absolute": False,
     "citation": "Directive (EU) 2022/2464 (CSRD) Art. 19a and 29b; ESRS E1 (Commission Delegated Regulation (EU) 2023/2772) climate-change disclosure identifiers, cited by identifier only",
     "source_status": "EU text reusable under 2011/833/EU. Marked deferred: Directive (EU) 2025/794 (the 'stop the clock' Directive of 14 April 2025) postponed the reporting obligations of the second and third waves of undertakings by two years, and the Omnibus simplification of the substantive requirements was still in negotiation when this was checked on 6 September 2026. The final scope and the ESRS set that will apply to the pack's customers are therefore not settled — directionally supported, not verified.",
     "status": "deferred", "origin": "extension",
     "scenarios": ["S-21"], "harm_classes": ["regulatory", "reputational"]},

    # ---- CT: customer trust -----------------------------------------------
    {"id": "DV-427", "family": "CT",
     "title": "Tenant key material lives in a per-tenant key ring and is never pooled into a platform key ring; where a customer supplies its own key, the platform reads nothing for that tenant when the key is revoked or unreachable",
     "absolute": True,
     "citation": "Customer contractual key-separation commitment; GDPR Art. 32(1)(a) (encryption as a measure appropriate to the risk); AICPA Trust Services Criteria CC6.1 (identifier only, no text reproduced)",
     "source_status": "EU text reusable; AICPA material cited by identifier only. Absolute on the same footing as the shipped DV-304: the separation is the substance of the multi-tenant bargain, and no officer of the provider may accept the risk of collapsing it on the customers' behalf. The source is the customer contract, and the source_status says so rather than dressing it as a statutory floor — the failure mode PA-01 records for DV-313.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-14", "S-02"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "DV-428", "family": "CT",
     "title": "At the end of a customer relationship the tenant's data is returned in the documented format and then deleted within the contracted window, including derived features, caches and backups, and a deletion certificate is issued",
     "absolute": True,
     "citation": "GDPR Art. 28(3)(g) (at the controller's choice, delete or return all personal data at the end of the provision of services, and delete existing copies); Regulation (EU) 2023/2854 (Data Act) Art. 25 and Art. 30 on switching and erasure, applicable since 12 September 2025",
     "source_status": "EU text reusable under 2011/833/EU. Absolute because Art. 28(3)(g) puts the choice with the controller and leaves the processor no discretion to keep the data; the contracted window is a parameter read from the customer record rather than a constant in code.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "DV-429", "family": "CT",
     "title": "A sub-processor is engaged only after the customer has been given notice of the intended change and the contracted objection window has run; no cutover, however urgent, starts processing ahead of that notice",
     "absolute": True,
     "citation": "GDPR Art. 28(2) (no other processor engaged without prior specific or general written authorisation; under a general authorisation the processor informs the controller of intended changes and gives it the chance to object); Art. 28(4)",
     "source_status": "EU text reusable under 2011/833/EU. Absolute because the authorisation belongs to the controller: the provider cannot grant itself permission to add a sub-processor, and an urgency argument is precisely the argument Art. 28(2) forecloses.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-13", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "DV-430", "family": "CT",
     "title": "The per-tenant evidence export that serves a customer's audit and inspection rights stays available, and a customer's declared regulatory regime travels with its data through every pipeline that touches it",
     "absolute": False,
     "citation": "GDPR Art. 28(3)(h) (information and audits); Regulation (EU) 2022/2554 (DORA) Art. 30(3) on contractual access, inspection and audit rights, applicable since 17 January 2025; 45 CFR §164.314(a) (HIPAA business associate contracts); PCI DSS v4.0.1 Requirement 12 identifiers (identifier only)",
     "source_status": "EU text reusable; US CFR public domain; PCI DSS cited by identifier only under its personal, non-commercial download licence. Ordinary because the form the evidence takes is negotiable even though the right itself is not.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-13"], "harm_classes": ["legal", "regulatory", "financial"]},

    # ---- OT: operational-technology protocols and devices ------------------
    {"id": "DV-431", "family": "OT",
     "title": "Flows between the facility network and the monitoring platform are enumerated in a conduit allow-list with the zone boundary each crosses; building-management and baseboard-management endpoints are never reachable outside their zone",
     "absolute": False,
     "citation": "IEC 62443-3-2 (zone and conduit risk assessment) and IEC 62443-3-3 system requirements, cited by identifier only; BACnet (ISO 16484-5) and IPMI v2.0 protocol identifiers",
     "source_status": "IEC and ISO standards are paywalled and cited by identifier only, with no text reproduced. Ordinary rather than absolute: the zone model is an engineering standard rather than a statutory floor, and its application to a colocation estate is a design judgement.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-14"], "harm_classes": ["safety", "regulatory"]},
    {"id": "DV-432", "family": "OT",
     "title": "New device paths use authenticated protocols with a credential unique to the controller; SNMPv1 and SNMPv2c community strings, unauthenticated BACnet writes and plaintext IPMI are not introduced on any path a change creates",
     "absolute": False,
     "citation": "NIST SP 800-53 IA-2 and SC-8 (public domain, CC0 via oscal-content); IEC 62443-4-2 component requirements (identifier only); Modbus Application Protocol and BACnet (ISO 16484-5) identifiers",
     "source_status": "NIST text is public domain; IEC and ISO cited by identifier only. Ordinary here, and deliberately so: the shipped DV-343 already states the absolute floor for production telemetry and control paths, and this provision is the OT-specific ordinary rule that reaches read-only device polling as well. The overlap is filed as proposed amendment PA-06 rather than resolved by editing DV-343.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-14"], "harm_classes": ["safety", "regulatory"]},
    {"id": "DV-433", "family": "OT",
     "title": "Gateway and edge-device firmware is signature-verified before it is flashed, its version and hash are recorded against the device, and a rollback image is retained for the supported window",
     "absolute": False,
     "citation": "NIST SP 800-53 SI-7 and CM-14 (public domain, CC0); Regulation (EU) 2024/2847 (Cyber Resilience Act) Annex I Part I(2)(c) on secure-by-default update delivery",
     "source_status": "NIST text is public domain; EU text reusable. The CRA limb is stated as an obligation the provider is building toward rather than one already binding — its main obligations apply from 11 December 2027 — and this provision rests in the meantime on the NIST controls and on customer contract.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-13"], "harm_classes": ["safety", "regulatory", "financial"]},

    # ---- SV: product security assurance -----------------------------------
    {"id": "DV-434", "family": "SV",
     "title": "Every customer-facing release publishes a software bill of materials covering at least the top-level dependencies, regenerated when a dependency changes, with an exploitability statement for each reported component finding",
     "absolute": False,
     "citation": "Regulation (EU) 2024/2847 (Cyber Resilience Act) Art. 13 and Annex I Part II(1) (software bill of materials for top-level dependencies); CISA Minimum Elements for an SBOM (US Government work)",
     "source_status": "EU text reusable; the US guidance is a Government work. Marked deferred: the CRA entered into force on 10 December 2024 but its main obligations, including the SBOM duty, apply from 11 December 2027. The provision is enacted here so that the platform builds toward it, and it is not yet an obligation a change can be denied under.",
     "status": "deferred", "origin": "extension",
     "scenarios": ["S-13"], "harm_classes": ["regulatory", "legal"]},
    {"id": "DV-435", "family": "SV",
     "title": "The path that reports an actively exploited vulnerability or a severe incident to the designated authority stays wired to the single reporting entry point, its clock starts at first awareness, and a named owner is recorded on the release",
     "absolute": False,
     "citation": "Regulation (EU) 2024/2847 (Cyber Resilience Act) Art. 14 (early warning within 24 hours, notification within 72 hours, via the single reporting platform) and Art. 16",
     "source_status": "EU text reusable under 2011/833/EU. Marked readiness rather than in force by five days: the CRA's vulnerability and incident reporting obligations apply from 11 September 2026, and this was checked on 6 September 2026. The clock and the routing are built and evidenced now so that the obligation is met on the day it attaches; the rest of the Regulation applies from 11 December 2027.",
     "status": "readiness", "origin": "extension",
     "scenarios": ["S-04", "S-20"], "harm_classes": ["regulatory", "legal", "reputational"]},
    {"id": "DV-436", "family": "SV",
     "title": "A published disclosure intake address is monitored, a researcher's report is acknowledged within the published window, and a fix or mitigation ships inside the deadline for its severity band or the extension is recorded with its approver",
     "absolute": False,
     "citation": "ISO/IEC 29147 (vulnerability disclosure) and ISO/IEC 30111 (vulnerability handling processes), cited by identifier only; NIST SP 800-53 SI-2 (flaw remediation), public domain",
     "source_status": "ISO/IEC standards are paywalled and cited by identifier only, with no text reproduced; NIST text is public domain (CC0). Ordinary: the cadence is a commitment rather than a statutory clock until the CRA reporting duties bite.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-20", "S-13"], "harm_classes": ["regulatory", "reputational"]},
    {"id": "DV-437", "family": "SV",
     "title": "Each customer-facing surface carries a scheduled independent security test, developer security testing evidence is attached to the release record, and the remediation deadline for each finding is tracked against its severity band",
     "absolute": False,
     "citation": "NIST SP 800-53 CA-8 (penetration testing), SA-11 (developer testing and evaluation) and SI-2 (flaw remediation), public domain (CC0 via oscal-content); AICPA Trust Services Criteria CC4.1 and CC7.1 (identifiers only)",
     "source_status": "NIST text is public domain; AICPA material cited by identifier only. Ordinary: the cadence is set by contract and by the audit programme rather than by statute.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-13", "S-15"], "harm_classes": ["regulatory", "financial"]},
    {"id": "DV-438", "family": "SV",
     "title": "Customer incident communication is served from infrastructure independent of the platform it reports on, and the root-cause document promised in the service agreement is delivered in full within its window rather than reduced to a summary line",
     "absolute": False,
     "citation": "Customer service-level agreements; AICPA Trust Services Criteria CC7.4 and CC7.5 (identifiers only); Regulation (EU) 2022/2554 (DORA) Art. 19(3) on intermediate and final incident reports where the customer is a financial entity",
     "source_status": "EU text reusable; AICPA cited by identifier only. Ordinary: the obligation is contractual for most customers, and the DORA limb binds the financial-entity customer rather than this provider directly, though the provider must feed it.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-20", "S-36"], "harm_classes": ["reputational", "regulatory", "financial"]},

    # ---- AX: accessibility ------------------------------------------------
    {"id": "DV-439", "family": "AX",
     "title": "The customer portal carries an accessibility regression gate at WCAG 2.2 Level AA in its release pipeline, and a Level A or AA conformance failure blocks the release rather than being downgraded to a build warning",
     "absolute": False,
     "citation": "Directive (EU) 2019/882 (European Accessibility Act), applicable since 28 June 2025, Annex I on services; ADA Title III, 42 U.S.C. §12182; WCAG 2.2 Level AA (W3C Recommendation, 5 October 2023), cited by identifier",
     "source_status": "EU text reusable; US statute public domain; WCAG cited by identifier. Note the limit honestly: the US Department of Justice's 2024 web rule is 28 CFR Part 35 and binds state and local government under Title II only, so for a private provider the WCAG 2.2 AA target rests on the EAA for EU customers and on Title III case law in the US.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-16"], "harm_classes": ["legal", "reputational"]},
    {"id": "DV-440", "family": "AX",
     "title": "Alarm state, severity and acknowledgement on the operator console and the customer portal are conveyed in text or shape as well as colour, every control carries an accessible name and a keyboard path, and the session timeout can be extended",
     "absolute": False,
     "citation": "WCAG 2.2 SC 1.4.1 (use of colour), 1.4.3, 2.1.1 (keyboard), 2.2.1 (timing adjustable), 4.1.2 (name, role, value), cited by success-criterion identifier; Directive (EU) 2019/882 Annex I §III",
     "source_status": "WCAG cited by identifier only; EU text reusable. Ordinary, and worth stating separately from DV-439 because the operator console is not a customer-facing service under the EAA and would otherwise fall outside the gate entirely.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-16", "S-20"], "harm_classes": ["legal", "reputational", "safety"]},

    # ---- TC: trade controls ------------------------------------------------
    {"id": "DV-441", "family": "TC",
     "title": "A customer, reseller or sub-processor is screened against the current restricted-party lists before an account, licence or telemetry endpoint is enabled, the ownership chain is tested, and no path clears its own screening hit",
     "absolute": True,
     "citation": "50 U.S.C. §1701 et seq. (IEEPA) and the OFAC sanctions regulations at 31 CFR Chapter V, including the reporting and penalties rules at 31 CFR Part 501; OFAC's 50 Percent Rule guidance on entities owned by blocked persons; Council Regulation (EU) No 269/2014 and Regulation (EU) No 833/2014",
     "source_status": "US CFR and statute are public domain; EU text reusable. Absolute because OFAC civil liability is strict: a dealing with a blocked person is a violation without regard to knowledge or intent, so there is no risk for anyone below the legislature to accept. The 50 percent rule is Treasury guidance rather than a codified rule, and is cited as such.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-01"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "DV-442", "family": "TC",
     "title": "The agent's cryptographic functionality carries a recorded export classification before a build is published, the download and licence paths are gated on the destination derived from verified account data, and support access to controlled build material runs a deemed-export check",
     "absolute": True,
     "citation": "Export Administration Regulations, 15 CFR Parts 730–774: §734.13(b) (deemed export), ECCN 5D002 and 5A002 for encryption items, License Exception ENC at §740.17 and its self-classification and reporting requirements, and the embargoed and sanctioned destinations at 15 CFR Part 746",
     "source_status": "US CFR — public domain. Absolute because an export to a Part 746 destination without authorisation is a criminal and civil violation of the EAR and is outside anyone's authority at the provider to accept. The classification itself is ordinary work; what is absolute is that a build does not leave without one and does not reach a prohibited destination.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-01"], "harm_classes": ["legal", "regulatory", "financial"]},
]

# --------------------------------------------------------------------------
# Scenario coverage for the pack's EXISTING families.
# --------------------------------------------------------------------------

FAMILY_SCENARIOS = {
    "TL": ["S-33", "S-36"],
    "AC": ["S-08", "S-12"],
    "TI": ["S-02", "S-18"],
    "AP": ["S-14", "S-13"],
    "KS": ["S-36", "S-08"],
    "TG": ["S-14", "S-33"],
    "QA": ["S-15", "S-36"],
    "RS": ["S-36"],
    "AI": ["S-23", "S-33"],
    "SC": ["S-13", "S-15"],
    "AG": ["S-12", "S-23", "S-15"],
    "DR": ["S-02", "S-05", "S-06", "S-17", "S-22"],
    "EV": ["S-03", "S-04", "S-33"],
    "OP": ["S-15", "S-36", "S-20"],
    "GV": ["S-34", "S-11"],
}

# Per-provision overrides where one existing provision is the real hook.
PROVISION_SCENARIOS = {
    "DV-302": ["S-08"],
    "DV-304": ["S-02"],
    "DV-313": ["S-02"],
    "DV-321": ["S-03", "S-33"],
    "DV-330": ["S-05"],
    "DV-331": ["S-05", "S-06"],
    "DV-332": ["S-10", "S-17"],
    "DV-333": ["S-22", "S-05"],
    "DV-334": ["S-05"],
    "DV-336": ["S-04"],
    "DV-338": ["S-22", "S-06"],
    "DV-340": ["S-08"],
    "DV-343": ["S-14"],
    "DV-408": ["S-10", "S-18"],
    "DV-411": ["S-11"],
    "DV-413": ["S-34"],
}

# --------------------------------------------------------------------------
# Draft amendments: findings about EXISTING provisions, filed not applied.
# The pack carries PA-01..PA-05, so the sequence continues at PA-06.
# --------------------------------------------------------------------------

PROPOSED_AMENDMENTS = [
    {
        "id": "PA-06",
        "targets": ["DV-343", "DV-337"],
        "raised_by": "corpus survey 2.0.0 scenario extension (dcvigil)",
        "finding": (
            "DV-343 makes 'no production telemetry or control path ships "
            "unauthenticated or in plaintext' absolute and cites NIST SP 800-53 "
            "IA-2 and SC-8(1). Verified: SP 800-53 is a control catalogue. It "
            "binds federal information systems through FISMA and OMB A-130, and "
            "binds a private vendor only through a contract that adopts it — "
            "FedRAMP, a customer's security schedule, or an audit programme. As "
            "an absolute, DV-343 therefore rests on a source that does not itself "
            "make it a who-may-decide floor, which is the defect Definition 1 "
            "warns against. Separately, DV-343 and the ordinary DV-337 state "
            "overlapping duties at different strengths, and the new DV-432 adds a "
            "third statement of the same idea for OT device paths, so one change "
            "that polls a PDU with an SNMPv2c community string can be charged "
            "under all three and will tie on every ordering key."),
        "proposed": (
            "Keep DV-343 absolute but re-cite it to the customer security "
            "schedule and to the platform's own transport commitment, with the "
            "NIST identifiers retained as the control mapping rather than as the "
            "source of obligation. Then state the boundary between the three "
            "expressly: DV-337 for principal identification, DV-343 for "
            "production telemetry and control transport, DV-432 for device "
            "polling paths inside a facility zone."),
        "why_not_applied": (
            "Re-anchoring an absolute changes what a later adjudicator reasons "
            "from and changes which cases short-circuit under A6. That is a "
            "legislative act, not an editorial one."),
        "disposition": "pending",
    },
    {
        "id": "PA-07",
        "targets": ["DV-342", "DV-341"],
        "raised_by": "corpus survey 2.0.0 scenario extension (dcvigil)",
        "finding": (
            "DV-342 ('the monitoring control plane is never a target of automated "
            "remediation') is absolute and cited to 'practice policy'; DV-341 "
            "(halt threshold and kill switch) is absolute and cited to the risk "
            "architecture. Both duties are sound engineering, and both are "
            "severe. Neither is a floor in the sense of Definition 1: nothing "
            "outside the organisation forbids the risk owner from accepting a "
            "self-remediating control plane on a named service for a named "
            "window. As drafted they are severity claims wearing the absolute "
            "label, which is precisely the confusion Definition 1 exists to "
            "prevent, and they make every such case an F-absolute that never "
            "reaches an escalation the corpus wants to exercise."),
        "proposed": (
            "Either reclassify both as ordinary provisions in AC with a high "
            "family tau, or keep them absolute and record in source_status that "
            "the deciding authority is the platform governance board acting as "
            "legislature, not an external instrument — so a reader can see which "
            "kind of absolute it is."),
        "why_not_applied": (
            "Reclassifying an absolute invalidates every F-absolute record built "
            "on it and is reserved to the legislature under A3."),
        "disposition": "pending",
    },
    {
        "id": "PA-08",
        "targets": ["DV-338"],
        "raised_by": "corpus survey 2.0.0 scenario extension (dcvigil)",
        "finding": (
            "DV-338 states the biometric notice-and-written-release floor and "
            "cites 740 ILCS 14/15(a) and 15(b). Verified: BIPA is an Illinois "
            "statute and reaches conduct with a sufficient Illinois nexus. The "
            "provision as drafted is jurisdiction-blind, so a badge-reader change "
            "at a site in eu-central-1 or ap-southeast-1 is charged under an "
            "Illinois statute that does not apply to it, while the instruments "
            "that do apply there — GDPR Art. 9(2)(a) explicit consent, and the "
            "Texas CUBI and Washington biometric statutes for other US sites — "
            "are not cited. Note also that BIPA was amended in August 2024 (SB "
            "2979) so that repeated collection by the same means is a single "
            "violation, which changes the exposure figure a risk owner would "
            "weigh but not the duty."),
        "proposed": (
            "Key the provision to the site's jurisdiction and give it a citation "
            "per jurisdiction: 740 ILCS 14/15 for Illinois, Tex. Bus. & Com. Code "
            "§503.001 for Texas, RCW 19.375 for Washington, GDPR Art. 9(2)(a) "
            "with Art. 4(14) for EU sites. Keep the absolute status: written "
            "release before enrolment is a floor in every one of them."),
        "why_not_applied": (
            "Narrowing or keying a provision's scope changes which arrivals are "
            "charged. That is a rule change."),
        "disposition": "pending",
    },
    {
        "id": "PA-09",
        "targets": ["DV-302", "DV-340"],
        "raised_by": "corpus survey 2.0.0 scenario extension (dcvigil)",
        "finding": (
            "PA-04 already records that DV-302's enumeration ('power, cooling, "
            "setpoints') does not clearly reach physical access control, and "
            "DV-340 closes that gap by addition. The same reading shows a second "
            "gap the extension has had to close the same way: fire detection and "
            "suppression, emergency power off, and UPS or transfer-switch "
            "operation are not 'power, cooling, setpoints' as an engineer would "
            "read that list, and they carry a life-safety dimension the other "
            "items do not. The new DV-421 states them as a separate absolute. The "
            "constitution now has three absolutes covering one idea — do not let "
            "software actuate the physical plant — with three different "
            "enumerations and no stated ordering between them."),
        "proposed": (
            "Consolidate at the legislative level: one absolute stating that "
            "monitoring and remediation software never actuates, inhibits or "
            "silences any physical or life-safety system, with the enumeration "
            "moved to a named parameter list the lawmakers maintain, and DV-302, "
            "DV-340 and DV-421 restated as instances of it."),
        "why_not_applied": (
            "Consolidation renumbers what the 144 shipped cases cite and would "
            "re-base every F-absolute record on DV-302. Only the legislature may "
            "do it, and the gap is closed by addition in the meantime."),
        "disposition": "pending",
    },
    {
        "id": "PA-10",
        "targets": ["DV-407", "DV-336"],
        "raised_by": "corpus survey 2.0.0 scenario extension (dcvigil)",
        "finding": (
            "DV-407 is deferred because NIS2 transposition is incomplete, and "
            "PA-05 records the same finding against DV-336. The extension has now "
            "had to take the identical posture twice more — DV-423 for the CER "
            "Directive, whose transposition and critical-entity designation are "
            "likewise incomplete, and DV-426 for CSRD, whose scope was moved by "
            "the stop-the-clock Directive (EU) 2025/794. Four provisions are "
            "using the 'deferred' status to express something it does not mean. "
            "Deferred means enacted but not yet applicable; what is actually true "
            "of these four is that the duty is in force in some jurisdictions the "
            "platform serves and not in others. The constitution has no "
            "jurisdiction parameter, so the status field is carrying a load it "
            "was not designed for, and a case at a German site is treated exactly "
            "like a case at a site in a member state that has not transposed."),
        "proposed": (
            "Add a jurisdiction dimension to the constitution — a per-site "
            "jurisdiction attribute and a per-provision applicability map read at "
            "charging time — and restore DV-407, DV-423 and DV-426 to in_force "
            "for the jurisdictions where the transposing instrument is in force. "
            "Until then the deferred status is the honest reading and should stay."),
        "why_not_applied": (
            "Adding a dimension to the charging inputs is a change to the "
            "constitution's own machinery and belongs to the legislature under "
            "A3, not to a corpus author."),
        "disposition": "pending",
    },
]

# New families whose cases concern a named service, device, site or tenant
# estate rather than an organisational process. LA, EN, SV and AX concern
# processes and published artefacts and stay outside the set, matching the
# posture of the existing DR, EV, GV, SC and AI families.
FLOOR_FACING_FAMILIES = {"LS", "OT", "CT"}
