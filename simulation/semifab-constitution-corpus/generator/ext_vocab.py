"""
SemiFab Constitution Corpus — scenario extension (corpus 2.0.0), vocabulary.

Six new provision families closing the gaps the scenario survey found in the
shipped constitution: ITAR and defence articles (IT), sanctions / anti-boycott
/ investment screening (SO), responsible sourcing and part integrity (RS),
environment, health and safety (EH), quality system and customer change
notification (QS), and OT network and remote access (OT).

Nothing in the shipped vocab.py is edited (Axiom A3). Findings about existing
provisions are filed below as draft amendments, not applied.

Citation posture follows vocab.py: US CFR and USC text is public domain under
17 U.S.C. §105; SEMI, SAE, IEC, ISO, IATF, JEDEC and ANSI/ESD standards are
named by identifier only and none of their text appears here. Every
`source_status` states what was and was not verified as of 6 September 2026.
Provision prose is original drafting, CC BY 4.0.
"""

# --------------------------------------------------------------------------
# New families. Pools are ORDERED: provision n (0-based, in PROVISIONS order
# within the family) draws comply[3n:3n+8] and violate[2n:2n+5], so its most
# decisive violate factors sit at 2n and 2n+1 and its most characteristic
# comply factors at 3n..3n+2.
# --------------------------------------------------------------------------

FAMILIES = {
    "IT": {
        "title": "ITAR technical data and defence articles",
        "risk": "5. Export Control Compliance (EAR/ITAR)",
        "comply": [
            # IT-001
            "itar_technical_data_confined_to_defence_enclave",
            "foreign_person_status_resolved_before_enclave_role_grant",
            "enclave_membership_requires_us_person_attribute",
            # IT-002
            "ddtc_registration_current_and_recorded",
            "itar_licence_or_exemption_cited_by_section_on_transfer",
            "itar_authorisation_check_bound_into_access_grant",
            # IT-003
            "itar_data_end_to_end_encrypted_before_leaving_boundary",
            "fips_validated_module_used_for_itar_data_at_rest",
            "itar_storage_location_excluded_from_proscribed_countries",
            # IT-004
            "jurisdiction_determination_recorded_before_ingest",
            "usml_category_recorded_on_defence_article_record",
            "commodity_jurisdiction_request_referenced_where_unclear",
            # shared tail
            "itar_access_logged_with_principal_and_citizenship",
            "itar_record_retained_for_five_years",
            "defence_enclave_egress_denied_by_default",
            "public_domain_determination_documented_before_release",
            "empowered_official_named_on_itar_authorisation",
        ],
        "violate": [
            # IT-001
            "itar_technical_data_released_to_foreign_person",
            "defence_enclave_boundary_merged_with_commercial_tenant",
            # IT-002
            "itar_transfer_proceeds_without_licence_or_cited_exemption",
            "ddtc_registration_lapse_not_blocking_transfer",
            # IT-003
            "itar_data_stored_in_cloud_region_outside_authorised_boundary",
            "itar_decryption_key_available_to_cloud_provider",
            # IT-004
            "defence_article_data_ingested_without_jurisdiction_determination",
            "usml_item_classified_under_ear_by_default",
            # shared tail
            "foreign_person_attribute_defaulted_to_us_person",
            "itar_export_record_omits_recipient_identity",
            "public_domain_asserted_without_ddtc_approval",
        ],
    },
    "SO": {
        "title": "Sanctions, anti-boycott and investment screening",
        "risk": "5. Export Control Compliance (EAR/ITAR); Sanctions and Anti-Boycott",
        "comply": [
            # SO-001
            "counterparty_screened_against_sdn_and_consolidated_lists",
            "fifty_percent_ownership_aggregation_applied_to_counterparty",
            "sanctions_screening_failure_fails_closed",
            # SO-002
            "boycott_request_language_detected_in_inbound_terms",
            "boycott_request_captured_for_quarterly_report",
            "boycott_related_condition_refused_in_contract_template",
            # SO-003
            "outbound_investment_determination_recorded_before_jv_data_share",
            "covered_foreign_person_status_resolved_for_jv_party",
            "cfius_declaration_status_recorded_on_covered_transaction",
            # shared tail
            "blocked_transaction_reported_within_ten_business_days",
            "sanctions_list_refresh_cadence_enforced",
            "sanctions_match_routed_to_human_reviewer",
            "ownership_data_source_and_date_recorded_on_screening_result",
            "sanctions_screening_record_retained_for_ten_years",
        ],
        "violate": [
            # SO-001
            "sanctions_screening_bypassed_for_counterparty_class",
            "ownership_aggregation_disabled_in_screening_rule",
            # SO-002
            "boycott_request_dropped_without_report",
            "boycott_compliance_clause_accepted_by_contract_parser",
            # SO-003
            "jv_data_share_opened_without_outbound_investment_determination",
            "covered_transaction_closed_without_cfius_analysis",
            # shared tail
            "blocked_property_released_by_configuration",
            "sanctions_list_snapshot_stale_beyond_declared_interval",
            "sanctions_screening_record_purged_before_retention_expiry",
        ],
    },
    "RS": {
        "title": "Responsible sourcing and part integrity",
        "risk": "5. Responsible Sourcing; 2. Hardware Supply Chain Integrity",
        "comply": [
            # RS-001
            "smelter_and_refiner_data_collected_from_supplier",
            "conflict_minerals_inquiry_response_retained",
            "three_tg_content_flag_carried_on_component_record",
            # RS-002
            "supplier_screened_against_forced_labour_entity_list",
            "forced_labour_hit_blocks_receipt_fail_closed",
            "supply_chain_tracing_evidence_attached_to_flagged_lot",
            # RS-003
            "counterfeit_inspection_result_recorded_per_lot",
            "authorised_distributor_status_verified_before_purchase",
            "counterfeit_suspect_part_reported_to_named_quality_owner",
            # RS-004
            "broker_sourced_lot_quarantined_pending_provenance",
            "provenance_chain_verified_before_lot_release",
            "grey_market_lot_flagged_on_genealogy_record",
            # shared tail
            "supplier_declaration_versioned_with_effective_date",
            "sourcing_screen_logged_with_list_snapshot_date",
            "supplier_attestation_expiry_enforced",
            "suspect_part_quarantine_bin_isolated_from_wip",
            "sourcing_record_retained_for_five_years",
        ],
        "violate": [
            # RS-001
            "smelter_data_dropped_from_supplier_onboarding",
            "conflict_minerals_inquiry_marked_complete_without_response",
            # RS-002
            "forced_labour_screening_disabled_for_supplier_tier",
            "forced_labour_match_downgraded_to_advisory",
            # RS-003
            "counterfeit_inspection_step_skipped_for_expedited_lot",
            "suspect_counterfeit_part_released_without_disposition",
            # RS-004
            "broker_sourced_lot_released_without_provenance",
            "grey_market_flag_cleared_by_configuration",
            # shared tail
            "supplier_attestation_expiry_ignored_at_receipt",
            "sourcing_screen_snapshot_date_not_recorded",
            "supplier_declaration_overwritten_without_version",
        ],
    },
    "EH": {
        "title": "Environment, health and safety systems",
        "risk": "4. Life-Safety and Environmental Monitoring Integrity",
        "comply": [
            # EH-001
            "gas_monitoring_alarm_path_unchanged_by_release",
            "toxic_gas_alarm_delivered_to_life_safety_panel_first",
            "gas_alarm_threshold_change_requires_ehs_signoff_record",
            # EH-002
            "lockout_state_read_only_in_software_layer",
            "emergency_stop_state_reflected_without_transformation",
            "interlock_reset_requires_physical_action_at_tool",
            # EH-003
            "effluent_monitoring_result_persisted_before_aggregation",
            "discharge_report_value_traceable_to_raw_measurement",
            "emissions_reporting_job_failure_alerts_named_ehs_owner",
            # EH-004
            "esd_monitor_telemetry_retained_for_declared_period",
            "cleanroom_particle_count_retained_at_native_resolution",
            "environmental_sampling_change_recorded_with_effective_date",
            # shared tail
            "life_safety_signal_path_isolated_from_analytics_pipeline",
            "ehs_alarm_acknowledgement_attributed_to_named_person",
            "chemical_inventory_threshold_check_recorded",
            "gas_detector_calibration_record_bound_to_reading",
            "ehs_record_retention_meets_regulatory_minimum",
        ],
        "violate": [
            # EH-001
            "hazardous_gas_alarm_suppressed_by_software_filter",
            "gas_alarm_rate_limited_below_detection_cadence",
            # EH-002
            "lockout_tagout_state_overridable_from_host_command",
            "emergency_stop_state_masked_in_equipment_status_feed",
            # EH-003
            "effluent_monitoring_result_dropped_before_report",
            "emissions_report_value_rounded_below_permit_limit",
            # EH-004
            "esd_monitor_telemetry_retention_shortened_below_declared",
            "cleanroom_telemetry_downsampled_without_record",
            # shared tail
            "gas_alarm_threshold_raised_without_ehs_signoff",
            "life_safety_signal_routed_through_analytics_queue",
            "pfas_reporting_job_disabled_by_configuration",
        ],
    },
    "QS": {
        "title": "Quality system and customer change notification",
        "risk": "4. Quality System and Customer Commitments",
        "comply": [
            # QS-001
            "change_notice_issued_before_customer_lot_exposure",
            "process_change_classified_as_major_or_minor_with_rationale",
            "customer_notice_period_enforced_by_release_gate",
            # QS-002
            "nonconformance_opens_corrective_action_record",
            "root_cause_and_verification_recorded_before_closure",
            "corrective_action_closure_attributed_to_named_owner",
            # QS-003
            "controller_model_validated_on_held_out_lots_before_promotion",
            "controller_model_promotion_has_rollback_path",
            "controller_model_version_recorded_on_lot_history",
            # QS-004
            "mask_revision_bound_to_lot_and_recipe_record",
            "retired_mask_revision_blocked_at_dispatch",
            "mask_revision_change_traceable_to_approved_ecn",
            # shared tail
            "customer_specific_requirements_checked_at_release",
            "quality_record_retained_for_customer_term",
            "process_change_approval_recorded_before_first_lot",
            "qualification_evidence_attached_to_change_record",
            "customer_acknowledgement_captured_on_change_notice",
        ],
        "violate": [
            # QS-001
            "process_change_reaches_customer_lots_before_notice",
            "change_notice_gate_bypassed_for_minor_classification",
            # QS-002
            "nonconformance_closed_without_corrective_action_record",
            "corrective_action_verification_step_removed",
            # QS-003
            "controller_model_promoted_without_held_out_validation",
            "controller_model_promoted_without_rollback_path",
            # QS-004
            "mask_revision_unbound_from_lot_record",
            "retired_mask_revision_dispatchable_to_tool",
            # shared tail
            "process_change_classification_defaulted_to_minor",
            "quality_record_retention_shortened_below_customer_term",
            "customer_specific_requirement_check_disabled",
        ],
    },
    "OT": {
        "title": "OT network segmentation and remote access",
        "risk": "4. OT Network Security and Vendor Access",
        "comply": [
            # OT-001
            "tool_network_traffic_crosses_only_declared_conduit",
            "zone_boundary_firewall_rule_change_reviewed_by_ot_owner",
            "new_service_placed_in_declared_security_zone",
            # OT-002
            "vendor_remote_session_brokered_through_jump_host",
            "vendor_remote_session_recorded_and_time_boxed",
            "vendor_remote_session_approved_per_session_by_named_owner",
            # OT-003
            "tool_firmware_signature_verified_against_vendor_key",
            "firmware_update_staged_on_non_production_tool_first",
            "firmware_provenance_recorded_on_equipment_record",
            # OT-004
            "equipment_time_source_authenticated",
            "clock_drift_monitored_and_alarmed_on_tool_network",
            "time_server_change_recorded_with_approval",
            # shared tail
            "ot_asset_inventory_updated_with_change",
            "protocol_allowlist_enforced_at_zone_boundary",
            "vendor_account_disabled_between_sessions",
            "ot_change_window_declared_and_honoured",
            "remote_session_least_privilege_scoped_to_named_tool",
        ],
        "violate": [
            # OT-001
            "tool_network_bridged_to_enterprise_network",
            "zone_boundary_rule_opened_to_any_source",
            # OT-002
            "vendor_remote_access_persistent_and_unbrokered",
            "vendor_remote_session_recording_disabled",
            # OT-003
            "tool_firmware_installed_without_signature_verification",
            "firmware_pulled_from_unverified_vendor_mirror",
            # OT-004
            "unauthenticated_time_server_added_to_tool_network",
            "clock_drift_alarm_disabled_on_equipment_path",
            # shared tail
            "vendor_account_left_enabled_after_session_end",
            "ot_protocol_allowlist_removed_at_zone_boundary",
            "firmware_staging_step_skipped_for_production_fleet",
        ],
    },
}

# Charging thresholds. IT and SO floors are strict-liability regimes (ITAR
# civil penalties under 22 U.S.C. 2778; IEEPA civil penalties under 50 U.S.C.
# 1705 need no knowledge element), so they sit with EX at the low end. EH is
# low because OSHA floors are not risk-acceptable. RS, OT and QS are ordinary
# operational families.
TAU = {"IT": 18, "SO": 18, "RS": 26, "EH": 20, "QS": 30, "OT": 28}

_CFR = "US CFR — public domain (17 U.S.C. 105)"

PROVISIONS = [
    # ---- ITAR ---------------------------------------------------------------
    {"id": "SF-IT-001", "family": "IT",
     "title": "ITAR technical data is never released to a foreign person and lives only inside the segregated defence enclave; there is no de minimis threshold, no group-A carve-out and no risk acceptance",
     "absolute": True,
     "citation": "22 CFR 120.33 (technical data); 22 CFR 120.50(a)(2), 120.56 (release); 22 CFR 120.62 (foreign person); 22 CFR 127.1(a)",
     "source_status": _CFR + "; section numbers follow the 2022 ITAR reorganisation (87 FR 16396) and were checked against eCFR as of 6 Sept 2026. Absolute because unlicensed release is a strict-liability violation under 22 U.S.C. 2778 and 22 CFR 127.10 that no officer below the legislature may accept.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-27"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "SF-IT-002", "family": "IT",
     "title": "Access to or transfer of a defence article or ITAR technical data proceeds only while DDTC registration is current and a licence or a section-cited exemption is bound into the grant",
     "absolute": False,
     "citation": "22 CFR 122.1 (registration); 22 CFR 123.1 (licence requirement); 22 CFR 125.4 (exemptions for technical data); 22 CFR 120.67 (empowered official)",
     "source_status": _CFR + "; registration and licensing sections checked against eCFR as of 6 Sept 2026.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-15"], "harm_classes": ["legal", "regulatory"]},
    {"id": "SF-IT-003", "family": "IT",
     "title": "ITAR technical data is never stored or transmitted outside the authorised boundary unless every condition of the encryption carve-out holds: end-to-end encryption with a validated module, no storage in a proscribed country or Russia, and no decryption means held by a third party",
     "absolute": True,
     "citation": "22 CFR 120.54(a)(5) (activities that are not exports); 22 CFR 126.1 (proscribed destinations)",
     "source_status": _CFR + "; 120.54(a)(5) added by 84 FR 70887 (effective 25 March 2020) and retained through the 2022 reorganisation; checked as of 6 Sept 2026. Absolute because outside the carve-out the storage is itself an export under 120.50 and the same strict-liability floor as SF-IT-001 applies.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-02"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "SF-IT-004", "family": "IT",
     "title": "A jurisdiction determination — USML category or CCL classification — is recorded for every defence-adjacent artifact before ingest, and an unresolved item is treated as ITAR until a determination says otherwise",
     "absolute": False,
     "citation": "22 CFR 120.4 (commodity jurisdiction); 22 CFR 121.1 (USML, Categories XI and XV); 15 CFR 774 Supplement 4 (order of review)",
     "source_status": _CFR + "; the fail-toward-ITAR default is corpus drafting, not a regulatory text, and is stated as such.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09"], "harm_classes": ["legal", "regulatory"]},

    # ---- Sanctions / anti-boycott / investment --------------------------------
    {"id": "SF-SO-001", "family": "SO",
     "title": "Counterparty screening against the SDN and consolidated sanctions lists, with fifty-percent ownership aggregation, is never bypassed for any counterparty class, and blocked-property handling is not configurable",
     "absolute": True,
     "citation": "31 CFR Part 501 (Reporting, Procedures and Penalties Regulations), 31 CFR 501.603, 501.604; OFAC Revised Guidance on Entities Owned by Blocked Persons (13 Aug 2014); 50 U.S.C. 1705",
     "source_status": _CFR + "; OFAC guidance is a US Treasury work, public domain, no explicit terms page located (research/03 §2.4). Absolute because IEEPA civil liability is strict and dealing in blocked property is prohibited regardless of intent; no officer may accept that risk.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-01"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "SF-SO-002", "family": "SO",
     "title": "A request to take a boycott-related action is never acted on and never dropped from the quarterly report, whether it arrives in a purchase order, a letter of credit or a portal form",
     "absolute": True,
     "citation": "15 CFR 760.2 (prohibitions), 15 CFR 760.5 (reporting requirements); 50 U.S.C. 4842; 26 U.S.C. 999 (Form 5713)",
     "source_status": _CFR + "; Part 760 checked against eCFR as of 6 Sept 2026. Absolute because the reporting duty is statutory and quarterly; a dropped request is a failure to report that no risk owner may waive.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04", "S-01"], "harm_classes": ["legal", "regulatory"]},
    {"id": "SF-SO-003", "family": "SO",
     "title": "Before covered technology or data is shared with a joint-venture or investee party, the outbound-investment and CFIUS determinations are recorded against the counterparty and the transaction",
     "absolute": False,
     "citation": "31 CFR Part 850 (850.217, 850.224, 850.405); 31 CFR Part 800 (800.401 mandatory declarations)",
     "source_status": _CFR + "; Part 850 effective 2 Jan 2025 and checked as of 6 Sept 2026. Directionally supported, not verified: the COINS Act (FY2026 NDAA, Dec 2025) expands the outbound regime and Treasury's implementing amendments to Part 850 were not confirmed as final.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-09", "S-02"], "harm_classes": ["legal", "regulatory"]},

    # ---- Responsible sourcing --------------------------------------------------
    {"id": "SF-RS-001", "family": "RS",
     "title": "Conflict-minerals inquiry data — smelter and refiner identity and country of origin — is collected from suppliers, retained and carried on the component record that feeds the annual Form SD",
     "absolute": False,
     "citation": "17 CFR 240.13p-1 and Form SD; 15 U.S.C. 78m(p) (Dodd-Frank §1502); Regulation (EU) 2017/821 for Union importers",
     "source_status": "US CFR and USC public domain; EU text reusable under 2011/833/EU. Rule 13p-1 remains in force as of 6 Sept 2026 subject to the SEC's 2017 partial-enforcement statement on the due-diligence portion.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-31", "S-04", "S-21"], "harm_classes": ["legal", "reputational"]},
    {"id": "SF-RS-002", "family": "RS",
     "title": "Forced-labour screening of suppliers and their upstream sources is never disabled or downgraded, and a match against the UFLPA Entity List blocks receipt until the presumption is rebutted",
     "absolute": True,
     "citation": "Pub. L. 117-78 §3 (rebuttable presumption); 19 U.S.C. 1307; UFLPA Entity List (DHS/FLETF)",
     "source_status": "US statute — public domain; Entity List is a US Government work. Absolute because the statute prohibits import of the covered goods outright; the presumption can be rebutted only before CBP, not by a risk owner accepting exposure.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-31", "S-01"], "harm_classes": ["legal", "reputational", "regulatory"]},
    {"id": "SF-RS-003", "family": "RS",
     "title": "Counterfeit-part avoidance records — inspection result, distributor authorisation status and suspect-part disposition — are recorded per lot and never skipped for expedite",
     "absolute": False,
     "citation": "SAE AS5553, SAE AS6171 (identifiers only); DFARS 252.246-7007 where a covered contract applies; 10 U.S.C. 3252",
     "source_status": "SAE text not reproduced; DFARS and USC public domain. 10 U.S.C. 3252 is the post-2021 renumbering of former §2319.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-31"], "harm_classes": ["safety", "legal", "financial"]},
    {"id": "SF-RS-004", "family": "RS",
     "title": "A broker-sourced or grey-market lot is quarantined until its provenance chain is verified, and the grey-market flag on the genealogy record is cleared only by a recorded disposition",
     "absolute": False,
     "citation": "SAE AS6081 (identifier only); practice policy",
     "source_status": "original; SAE text not reproduced.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-31", "S-13"], "harm_classes": ["safety", "financial", "reputational"]},

    # ---- Environment, health and safety ----------------------------------------
    {"id": "SF-EH-001", "family": "EH",
     "title": "Hazardous-gas monitoring alarms are never suppressed, filtered, rate-limited or re-thresholded by software, and reach the life-safety panel before any analytics path",
     "absolute": True,
     "citation": "29 U.S.C. 654(a)(1); 29 CFR 1910.119(d), (j), (l) where a covered process exists; 29 CFR 1910.1000; SEMI S2 (identifier only)",
     "source_status": "USC and CFR public domain; SEMI text not reproduced. Absolute because it is a life-safety floor: an employer duty under §654(a)(1) cannot be accepted as risk by a COO, and PSM management-of-change (1910.119(l)) forbids a software change to alarm behaviour outside the documented process.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08", "S-33"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "SF-EH-002", "family": "EH",
     "title": "Lockout/tagout, emergency-off and interlock states are read-only to software: no host command, status transformation or configuration can override, mask or reset them",
     "absolute": True,
     "citation": "29 CFR 1910.147(c)(4), 1910.147(d), 1910.147(e); 29 CFR 1910.212(a); SEMI S2, SEMI S8 (identifiers only)",
     "source_status": "US CFR public domain; SEMI text not reproduced. Absolute because the energy-control floor exists to protect the person at the tool; a software override is not a risk any owner may accept. Overlaps SF-SG-001 deliberately: that provision governs the signal path, this one the state semantics.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08"], "harm_classes": ["safety", "legal"]},
    {"id": "SF-EH-003", "family": "EH",
     "title": "Effluent, emissions and chemical-reporting pipelines never drop, round or alter a monitoring result between measurement and the reported value, and a reporting job is never disabled by configuration",
     "absolute": True,
     "citation": "40 CFR 469 Subpart A; 40 CFR 122.41(j)(1), (j)(4), (l)(4); 33 U.S.C. 1319(c)(4); 42 U.S.C. 7413(c)(2); 40 CFR 63 Subpart BBBBB; 40 CFR 98 Subpart I; 40 CFR Part 705 (TSCA §8(a)(7) PFAS reporting)",
     "source_status": "US CFR and USC public domain. Absolute because knowingly false or omitted monitoring records are criminal under CWA §309(c)(4) and CAA §113(c)(2); integrity of the reported value is not risk-acceptable. Directionally supported, not verified: the Part 705 PFAS submission window was moved by EPA's May 2025 interim final rule and a Nov 2025 proposed rule; confirm 40 CFR 705.20 dates before relying on the PFAS clause.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-21", "S-33"], "harm_classes": ["regulatory", "legal", "reputational"]},
    {"id": "SF-EH-004", "family": "EH",
     "title": "ESD-monitor and cleanroom environmental telemetry is retained at native resolution for the declared period, and any change to sampling or aggregation is recorded with an effective date",
     "absolute": False,
     "citation": "ANSI/ESD S20.20; ISO 14644-1, ISO 14644-2 (identifiers only); practice policy",
     "source_status": "original; standards named by identifier only, no text reproduced.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-33"], "harm_classes": ["financial", "regulatory"]},

    # ---- Quality system ---------------------------------------------------------
    {"id": "SF-QS-001", "family": "QS",
     "title": "A process, recipe or material change is classified and a customer change notice issued before the first affected lot is exposed, and the release gate enforces the customer's notice period",
     "absolute": False,
     "citation": "JEDEC JESD46 (identifier only); ISO 9001:2015 §8.5.6, IATF 16949:2016 (identifiers only); customer PCN agreements",
     "source_status": "standards named by identifier only; the notice period is contractual and varies by customer, so the provision binds to the customer record rather than a fixed number of days.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-24"], "harm_classes": ["financial", "legal", "reputational"]},
    {"id": "SF-QS-002", "family": "QS",
     "title": "Every nonconformance opens a corrective-action record; root cause and verification of effectiveness are recorded, and closure carries a named owner",
     "absolute": False,
     "citation": "ISO 9001:2015 §10.2; IATF 16949:2016 (identifiers only); 8D methodology",
     "source_status": "standards named by identifier only, no text reproduced.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-24"], "harm_classes": ["financial", "reputational"]},
    {"id": "SF-QS-003", "family": "QS",
     "title": "An advanced-process-control or run-to-run controller model is promoted to production only after validation on held-out lots, with a recorded version on lot history and a tested rollback path",
     "absolute": False,
     "citation": "ISO 9001:2015 §8.5.1 (identifier only); practice policy",
     "source_status": "original; standard named by identifier only.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-23", "S-24", "S-15"], "harm_classes": ["financial", "safety"]},
    {"id": "SF-QS-004", "family": "QS",
     "title": "Reticle and photomask revisions are bound to the lot and recipe record, traceable to an approved engineering change, and a retired revision cannot be dispatched to a tool",
     "absolute": False,
     "citation": "practice policy; ISO 9001:2015 §8.5.2 (identifier only)",
     "source_status": "original; standard named by identifier only.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-24", "S-03"], "harm_classes": ["financial", "reputational"]},

    # ---- OT network -------------------------------------------------------------
    {"id": "SF-OT-001", "family": "OT",
     "title": "The fab-floor tool network is a distinct security zone: traffic to enterprise or cloud crosses only a declared conduit, and no change bridges the zones or opens a boundary rule to any source",
     "absolute": False,
     "citation": "IEC 62443-3-2, IEC 62443-3-3 (identifiers only); NIST SP 800-82 Rev 3 §5",
     "source_status": "IEC text not reproduced; NIST public domain.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28"], "harm_classes": ["safety", "regulatory"]},
    {"id": "SF-OT-002", "family": "OT",
     "title": "Vendor remote access to equipment is brokered through a jump host, approved per session by a named owner, recorded, time-boxed and scoped to the named tool",
     "absolute": False,
     "citation": "IEC 62443-2-4, IEC 62443-4-2 (identifiers only); NIST SP 800-82 Rev 3; NIST SP 800-53 Rev 5 AC-17, MA-4",
     "source_status": "IEC text not reproduced; NIST public domain.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-27"], "harm_classes": ["safety", "regulatory", "reputational"]},
    {"id": "SF-OT-003", "family": "OT",
     "title": "Tool firmware and equipment software updates carry vendor-signed provenance verified before install, are staged on a non-production tool first, and are recorded on the equipment record",
     "absolute": False,
     "citation": "IEC 62443-2-3, IEC 62443-4-1 (identifiers only); NIST SP 800-82 Rev 3; NIST SP 800-161 Rev 1",
     "source_status": "IEC text not reproduced; NIST public domain.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-13"], "harm_classes": ["safety", "financial", "regulatory"]},
    {"id": "SF-OT-004", "family": "OT",
     "title": "Equipment time comes from an authenticated source; clock drift on the tool network is monitored and alarmed, and no unauthenticated time server is added to an equipment path",
     "absolute": False,
     "citation": "IEEE 1588 (identifier only); RFC 8915 (Network Time Security); NIST SP 800-82 Rev 3",
     "source_status": "IEEE text not reproduced; RFC reusable under the IETF Trust licence; NIST public domain.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-28", "S-33"], "harm_classes": ["regulatory", "financial"]},
]

# --------------------------------------------------------------------------
# Scenario coverage for the EXISTING families (scenarios.json ids).
# --------------------------------------------------------------------------

FAMILY_SCENARIOS = {
    "EX": ["S-09", "S-01"],
    "DS": ["S-02", "S-19"],
    "SG": ["S-08", "S-36"],
    "RT": ["S-36"],
    "WI": ["S-03", "S-33"],
    "RP": ["S-39", "S-27"],
    "SS": ["S-13"],
    "AG": ["S-12", "S-15"],
    "TQ": ["S-36"],
    "CR": ["S-14"],
    "AS": ["S-14", "S-36"],
    "NC": ["S-13", "S-15"],
    "GV": ["S-34", "S-11", "S-05", "S-22"],
}

# Per-provision overrides where an existing provision reaches a scenario its
# family label does not suggest.
PROVISION_SCENARIOS = {
    # citizenship and residency attributes on principals are personnel data
    "SF-EX-001": ["S-09", "S-22"],
    # the badge-photo scraping factor is a worker-monitoring case as well as an Art. 5 one
    "SF-GV-002": ["S-05", "S-22"],
    "SF-GV-001": ["S-11"],
    "SF-DS-002": ["S-19", "S-03"],
    "SF-AG-001": ["S-12", "S-08"],
}

# --------------------------------------------------------------------------
# Draft amendments (Axiom A3): findings about EXISTING provisions, filed not
# applied. The pack carries no prior amendments, so numbering starts at PA-01.
# --------------------------------------------------------------------------

PROPOSED_AMENDMENTS = [
    {"id": "PA-01", "targets": ["SF-EX-004"],
     "raised_by": "corpus scenario extension survey 2026-09-06",
     "finding": "The provision cites '15 CFR 744; Consolidated Screening List'. The CSL is a convenience aggregation published by ITA, not a legal instrument; the screening duties it bundles arise under 15 CFR 744 Supplement 4 (Entity List), 15 CFR 764.3 and the Denied Persons List, 15 CFR 744.21 (MEU List), the AECA Debarred List under 22 CFR 127.7, and OFAC's lists under 31 CFR Chapter V. The OFAC piece is a sanctions obligation with its own strict-liability regime and is now carried by SF-SO-001.",
     "proposed": "Retain the provision and its absolute status. Restate the citation to name the underlying lists and their instruments, and cross-reference SF-SO-001 so that a screening case involving a blocked person is charged under both.",
     "why_not_applied": "Restating a citation changes what a later adjudicator reasons from; that is a legislative act under A3.",
     "disposition": "pending"},
    {"id": "PA-02", "targets": ["SF-SG-001"],
     "raised_by": "corpus scenario extension survey 2026-09-06",
     "finding": "SF-SG-001 is absolute and is cited to 'equipment safety floor; SEMI S2 practice'. Definition 1 requires an absolute to rest on an instrument that removes the decision from everyone below the legislature; a practice label reads as a severity claim. The instrument exists: 29 U.S.C. 654(a)(1) and 29 CFR 1910.147 / 1910.212, which SF-EH-002 now cites for the state semantics of the same interlocks.",
     "proposed": "Retain absolute status. Restate the citation as '29 U.S.C. 654(a)(1); 29 CFR 1910.147, 1910.212; SEMI S2 (identifier only)' and note the intended overlap with SF-EH-002 (signal path versus state semantics).",
     "why_not_applied": "The provision is cited by executed corpora and figures; its text is frozen at this revision.",
     "disposition": "pending"},
    {"id": "PA-03", "targets": ["SF-EX-001", "SF-EX-002"],
     "raised_by": "corpus scenario extension survey 2026-09-06; research/03 §1.10",
     "finding": "Both provisions say 'controlled technical data' and 'foreign person' but cite only the EAR (15 CFR 734.13). ITAR technical data (22 CFR 120.33, 120.50) has no de minimis rule, no group-A treatment and a narrower encryption carve-out (22 CFR 120.54(a)(5) versus 15 CFR 734.18(a)(5)). As drafted, a precedent engine may generalise an EAR licence-exception outcome onto an ITAR case. The research file recommended a separate ITAR path for exactly this reason.",
     "proposed": "Scope SF-EX-001 and SF-EX-002 expressly to EAR-controlled technical data and add a cross-reference to SF-IT-001 and SF-IT-003 for defence articles, so that the distinguishing gate has a textual hook.",
     "why_not_applied": "Narrowing a provision's scope is a rule change; filed for the legislature.",
     "disposition": "pending"},
    {"id": "PA-04", "targets": ["SF-WI-001", "SF-WI-002"],
     "raised_by": "corpus scenario extension survey 2026-09-06",
     "finding": "Both provisions are absolute and cite 'operational integrity floor' (SF-WI-001 adds '15 CFR 762.5(b)(4) analogue'). An analogue is not an instrument. For records within 15 CFR 762 (export records) the floor is real and already carried by SF-EX-003; for customer quality records the source is the customer contract and IATF 16949 retention clauses; for other WIP records no statutory floor was found.",
     "proposed": "Either restate the citation to the records actually covered by a statutory or contractual floor, or demote the provisions to ordinary and let SF-EX-003 and SF-QS-002 carry the absolute and contractual cases respectively.",
     "why_not_applied": "Changing absolute status alters A6 short-circuit behaviour in the F-absolute category, which is reported in existing figures.",
     "disposition": "pending"},
    {"id": "PA-05", "targets": ["SF-RP-001", "SF-RP-002"],
     "raised_by": "corpus scenario extension survey 2026-09-06",
     "finding": "Both provisions are absolute and cite 'IP protection floor; trade-secret exposure'. The instrument that makes this a who-may-decide floor rather than a severity claim is the reasonable-measures element of the trade-secret definition, 18 U.S.C. 1839(3)(A) (Defend Trade Secrets Act) and the corresponding state UTSA enactments: a single unprotected disclosure path can forfeit trade-secret status for the recipe as a whole, which is not a risk a COO may accept for one change.",
     "proposed": "Retain absolute status and restate the citation as '18 U.S.C. 1839(3)(A), 1836; state UTSA enactments', with the forfeiture rationale in source_status.",
     "why_not_applied": "Citation restatement is legislative under A3; the provision text is frozen at this revision.",
     "disposition": "pending"},
]

# New families whose cases concern a named tool, lot, mask or supplier lot on
# the fab floor. IT and SO are infrastructural; naming a lot there is noise.
FLOOR_FACING_FAMILIES = {"RS", "EH", "QS", "OT"}
