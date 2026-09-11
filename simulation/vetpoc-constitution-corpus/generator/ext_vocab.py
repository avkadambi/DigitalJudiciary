"""
VetPOC Constitution Corpus — scenario extension (corpus 2.0.0).

New provision families closing the gaps the architect's scenario survey found in
this pack's constitution: breach notification, DEA reporting and ordering, client
communications and records rights, patient safety and clinical decision support,
public-health and mandated reporting, and accessibility. Everything here is
additive (Axiom A3): no existing provision, factor or title is edited. Findings
about existing provisions are filed below as draft amendments.

Same licensing posture as vocab.py: US CFR and U.S.C. text is a US Government
work; California statutes and regulations are edicts of government; EU texts are
reusable under Decision 2011/833/EU. Provision prose is original drafting (CC BY
4.0). PCI, ISO, W3C and AVMA material is cited by identifier only.

Citations were shelf-life checked on 6 September 2026. Where an instrument's
status could not be confirmed the source_status says so rather than asserting.
"""

# --------------------------------------------------------------------------
# New families. Factor pools are sliced positionally by the generator: the
# n-th provision of a family receives comply[3n:3n+8] and violate[2n:2n+5], so
# each provision's most decisive violate factors sit at 2n and 2n+1 and its
# most characteristic comply factors at 3n..3n+2.
# --------------------------------------------------------------------------

FAMILIES = {
    "BN": {
        "title": "Breach notification and client-data incidents",
        "risk": "2.3 Patient Data Privacy (PII and PCI); incident response floor",
        "comply": [
            # BN-001 (0..2)
            "breach_clock_constant_sourced_from_jurisdiction_table",
            "notification_deadline_computed_from_discovery_timestamp",
            "breach_clock_override_rejected_by_configuration_loader",
            # BN-002 (3..5)
            "anomalous_bulk_export_alert_routed_to_oncall",
            "incident_runbook_linked_from_detection_alert",
            "detection_signal_retained_beyond_notification_window",
            # BN-003 (6..8)
            "processor_contract_carries_breach_notice_clause",
            "vendor_incident_webhook_feeds_incident_queue",
            "subprocessor_breach_notice_deadline_recorded_at_onboarding",
            # shared tail
            "affected_owner_count_computed_from_access_log",
            "regulator_notice_template_versioned_in_policy_repo",
            "notification_dispatch_evidenced_in_audit_ledger",
            "credential_stuffing_detector_enabled_on_portal_login",
            "breach_drill_result_recorded_with_named_owner",
            "owner_notice_content_meets_statutory_elements",
        ],
        "violate": [
            # BN-001 (0,1)
            "breach_notification_deadline_exposed_as_tenant_setting",
            "notification_clock_started_at_confirmation_not_discovery",
            # BN-002 (2,3)
            "bulk_export_anomaly_alert_disabled_to_cut_noise",
            "incident_runbook_reference_removed_from_alert_payload",
            # BN-003 (4,5)
            "vendor_contract_template_drops_breach_notice_clause",
            "vendor_incident_notices_routed_to_unmonitored_mailbox",
            # shared tail
            "access_log_retention_shorter_than_notification_lookback",
            "breach_scope_computed_from_sampled_logs_only",
            "owner_notice_omits_statutory_content_elements",
            "notification_dispatch_marked_sent_without_delivery_evidence",
        ],
    },
    "DR": {
        "title": "DEA reporting, ordering and diversion controls",
        "risk": "2.2 Controlled Substance Management; DEA registrant duties",
        "comply": [
            # DR-001 (0..2)
            "theft_or_loss_notice_sent_within_one_business_day",
            "form_106_filed_electronically_within_forty_five_days",
            "significant_loss_determination_recorded_with_factors",
            # DR-002 (3..5)
            "schedule_ii_order_placed_through_csos_or_form_222",
            "csos_order_signed_with_dea_issued_certificate",
            "order_form_records_retained_two_years_at_registered_location",
            # DR-003 (6..8)
            "biennial_inventory_scheduled_within_two_year_window",
            "inventory_count_exact_for_schedule_ii_containers",
            "inventory_record_signed_by_named_licensee",
            # DR-004 (9..11)
            "diversion_analytics_run_over_every_dispensing_event",
            "anomalous_dispensing_pattern_flagged_to_medical_director",
            "effective_controls_against_diversion_documented",
            # shared tail
            "discrepancy_investigation_opened_before_closure",
            "form_222_line_items_validated_against_receipt",
            "csos_certificate_expiry_checked_before_order_submit",
            "inventory_held_in_registered_location_only",
            "partial_shipment_recorded_against_original_order",
            "power_of_attorney_for_ordering_recorded",
        ],
        "violate": [
            # DR-001 (0,1)
            "theft_or_loss_report_suppressed_below_configured_threshold",
            "form_106_filing_left_as_manual_optional_step",
            # DR-002 (2,3)
            "schedule_ii_order_submitted_outside_csos_or_form_222",
            "order_form_records_purged_before_two_years",
            # DR-003 (4,5)
            "biennial_inventory_job_disabled_or_skipped",
            "inventory_count_auto_filled_from_ledger_balance",
            # DR-004 (6,7)
            "diversion_analytics_disabled_for_named_practice",
            "anomalous_dispensing_alerts_routed_to_null_sink",
            # shared tail
            "csos_signature_replaced_by_shared_practice_credential",
            "loss_discovery_timestamp_editable_after_the_fact",
            "order_form_line_items_accepted_without_receipt_match",
            "inventory_record_unsigned_by_any_licensee",
        ],
    },
    "CC": {
        "title": "Client communications, consent, subscriptions and records rights",
        "risk": "2.3 Patient Data Privacy; consumer-protection floor",
        "comply": [
            # CC-001 (0..2)
            "prior_express_consent_recorded_before_automated_text",
            "consent_scope_matched_to_message_purpose",
            "wireless_number_consent_captured_with_timestamp_and_source",
            # CC-002 (3..5)
            "auto_renewal_terms_disclosed_before_enrolment",
            "online_cancellation_path_equal_steps_to_enrolment",
            "renewal_reminder_sent_before_annual_charge",
            # CC-003 (6..8)
            "esign_consent_captured_before_electronic_delivery",
            "hardware_and_software_requirements_disclosed_at_consent",
            "paper_copy_option_retained_after_esign_consent",
            # CC-004 (9..11)
            "written_prescription_offered_at_dispensing_decision",
            "prescription_pdf_generated_on_client_request",
            "prescription_portability_rule_encoded_per_state",
            # CC-005 (12..14)
            "records_copy_released_within_state_deadline",
            "records_release_request_tracked_with_due_date",
            "records_release_not_conditioned_on_balance_paid",
            # CC-006 (15..17)
            "account_holder_age_verified_at_portal_signup",
            "guardian_consent_captured_for_minor_account",
            "minor_account_barred_from_payment_agreements",
            # shared tail
            "consent_revocation_honoured_across_all_channels",
            "stop_keyword_processed_within_reasonable_time",
            "marketing_texts_kept_within_quiet_hours",
            "price_change_notice_sent_before_renewal",
            "fee_free_cancellation_confirmed_by_email",
            "records_release_log_entry_written_per_request",
        ],
        "violate": [
            # CC-001 (0,1)
            "automated_text_sent_without_recorded_prior_consent",
            "consent_check_bypassed_for_reactivation_campaign",
            # CC-002 (2,3)
            "auto_renewal_enrolled_by_prechecked_box",
            "cancellation_requires_phone_call_while_signup_is_online",
            # CC-003 (4,5)
            "electronic_records_delivered_without_esign_consent",
            "esign_consent_inferred_from_portal_login",
            # CC-004 (6,7)
            "written_prescription_option_hidden_from_client",
            "prescription_copy_conditioned_on_in_house_purchase",
            # CC-005 (8,9)
            "records_release_delayed_beyond_state_deadline",
            "records_release_blocked_until_balance_paid",
            # CC-006 (10,11)
            "minor_account_created_without_guardian_consent",
            "payment_plan_signed_by_under_eighteen_account",
            # shared tail
            "stop_reply_ignored_by_reminder_engine",
            "renewal_reminder_removed_before_annual_charge",
            "marketing_texts_scheduled_outside_permitted_hours",
            "records_release_charged_above_statutory_copy_fee",
        ],
    },
    "PS": {
        "title": "Patient safety, dosing and clinical decision support",
        "risk": "Clinical safety floor; 2.1 POC integrations; 4. AI features",
        "comply": [
            # PS-001 (0..2)
            "dose_computed_from_current_recorded_weight",
            "weight_unit_declared_and_converted_before_dose",
            "dose_outside_species_range_hard_stops_order",
            # PS-002 (3..5)
            "triage_assistant_discloses_automated_status_on_every_turn",
            "triage_assistant_hands_off_to_licensed_staff_on_red_flag",
            "triage_assistant_output_labelled_not_a_diagnosis",
            # PS-003 (6..8)
            "critical_value_alert_requires_acknowledgement",
            "critical_value_escalates_when_unacknowledged",
            "alert_route_change_reviewed_by_medical_director",
            # PS-004 (9..11)
            "euthanasia_consent_signed_by_verified_owner_or_agent",
            "remains_disposition_choice_recorded_before_procedure",
            "remains_tag_scanned_at_every_custody_transfer",
            # shared tail
            "concentration_and_volume_shown_alongside_dose",
            "stale_weight_prompts_reweigh_before_dose",
            "triage_transcript_attached_to_medical_record",
            "alert_delivery_tested_in_release_pipeline",
            "cremation_return_verified_against_remains_tag",
            "dose_calculator_regression_tests_cover_unit_boundaries",
        ],
        "violate": [
            # PS-001 (0,1)
            "dose_computed_from_stale_or_absent_weight",
            "weight_unit_mismatch_downgraded_to_dismissable_warning",
            # PS-002 (2,3)
            "triage_assistant_presents_as_licensed_veterinarian",
            "triage_assistant_issues_treatment_without_handoff",
            # PS-003 (4,5)
            "critical_value_alert_suppressed_by_quiet_hours_setting",
            "critical_value_alert_downgraded_to_passive_notification",
            # PS-004 (6,7)
            "euthanasia_performed_without_recorded_owner_consent",
            "remains_custody_transfer_recorded_without_tag_scan",
            # shared tail
            "dose_range_hard_stop_replaced_by_override_button",
            "triage_assistant_disclosure_shown_once_per_session_only",
            "alert_acknowledgement_auto_completed_by_timer",
            "remains_disposition_defaulted_without_owner_choice",
        ],
    },
    "PH": {
        "title": "Public health, welfare and mandated reporting",
        "risk": "Domain floor; USDA APHIS, state animal-health and public-health law",
        "comply": [
            # PH-001 (0..2)
            "reportable_condition_matched_against_current_state_list",
            "disease_report_dispatched_to_state_animal_health_official",
            "report_dispatch_evidenced_with_acknowledgement",
            # PH-002 (3..5)
            "rabies_certificate_signed_by_licensed_veterinarian",
            "rabies_certificate_fields_complete_per_state_form",
            "rabies_certificate_issuer_licence_verified_current",
            # PH-003 (6..8)
            "suspected_abuse_report_path_reachable_from_chart",
            "abuse_report_recorded_with_reporter_immunity_notice",
            "abuse_report_visible_only_to_authorised_roles",
            # PH-004 (9..11)
            "microchip_number_validated_against_iso_format",
            "microchip_registry_submission_confirmed_by_registry",
            "microchip_reassignment_requires_verified_ownership",
            # shared tail
            "reportable_list_refreshed_from_versioned_fixture",
            "zoonotic_exposure_flag_shown_to_staff",
            "lab_confirmed_result_triggers_report_workflow",
            "rabies_vaccine_lot_and_expiry_recorded",
            "microchip_scan_recorded_at_intake",
            "report_history_retained_with_medical_record",
        ],
        "violate": [
            # PH-001 (0,1)
            "reportable_disease_report_gated_behind_practice_toggle",
            "reportable_condition_list_pruned_to_reduce_alerts",
            # PH-002 (2,3)
            "rabies_certificate_issued_under_technician_signature",
            "rabies_certificate_signature_auto_applied_from_template",
            # PH-003 (4,5)
            "suspected_abuse_report_option_removed_from_chart",
            "abuse_report_visible_to_client_on_portal",
            # PH-004 (6,7)
            "microchip_number_accepted_without_format_validation",
            "microchip_registry_submission_failures_silently_dropped",
            # shared tail
            "report_dispatch_batched_past_statutory_window",
            "rabies_certificate_issuable_with_expired_licence",
            "microchip_owner_reassigned_from_client_self_service",
            "zoonotic_flag_hidden_from_boarding_staff",
        ],
    },
    "AX": {
        "title": "Accessibility and equal access to client-facing surfaces",
        "risk": "Client-facing surfaces; civil-rights and consumer floor",
        "comply": [
            # AX-001 (0..2)
            "accessibility_regression_suite_runs_on_portal_build",
            "wcag_aa_failure_blocks_portal_release",
            "manual_screen_reader_check_recorded_for_new_flow",
            # AX-002 (3..5)
            "consent_control_operable_by_keyboard_alone",
            "checkin_timeout_extendable_by_client",
            "status_conveyed_by_text_not_colour_alone",
            # shared tail
            "form_errors_announced_to_assistive_technology",
            "accessibility_statement_versioned_in_repo",
            "accessible_name_present_on_every_control",
            "captions_provided_for_discharge_video",
            "focus_order_verified_on_consent_dialog",
            "target_size_meets_minimum_on_mobile_checkin",
        ],
        "violate": [
            # AX-001 (0,1)
            "accessibility_gate_removed_from_portal_pipeline",
            "wcag_failures_downgraded_to_warnings_in_ci",
            # AX-002 (2,3)
            "consent_signature_requires_mouse_drag_only",
            "checkin_session_expires_with_no_extension",
            # shared tail
            "required_field_error_shown_by_colour_only",
            "focus_trapped_in_consent_modal",
            "custom_control_shipped_without_accessible_name",
            "checkin_captcha_lacks_non_visual_alternative",
        ],
    },
}

# Strict-liability floors (statutory clocks, DEA registrant duties, mandated
# reporting) get low tau; ordinary operational families sit in the middle.
TAU = {
    "BN": 20,
    "DR": 18,
    "CC": 26,
    "PS": 22,
    "PH": 20,
    "AX": 30,
}

# --------------------------------------------------------------------------
# New provisions. Ids continue the pack's VP-XX-NNN convention.
# --------------------------------------------------------------------------

PROVISIONS = [
    # ---- BN: breach notification ----------------------------------------
    {"id": "VP-BN-001", "family": "BN",
     "title": "The breach-notification clock for each jurisdiction is a legislated constant that no configuration, feature flag or tenant setting can extend, pause or disable",
     "absolute": True,
     "citation": "Cal. Civ. Code §1798.82(a); Tex. Bus. & Com. Code §521.053; GDPR Art. 33(1) and UK GDPR Art. 33(1) (72 hours)",
     "source_status": "US state statutes are edicts of government; EU/UK texts reusable. All fifty US states have a notification statute; the two named are the pack's US-CA and US-TX jurisdictions. Absolute because the clock is set by the legislature and cannot be accepted away by any officer of the practice.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "VP-BN-002", "family": "BN",
     "title": "Breach-detection telemetry on owner-data stores stays wired to the on-call path and every detection alert carries a reference to the incident runbook",
     "absolute": False,
     "citation": "GDPR Art. 32(1)(d), Art. 33(1) ('aware of'); Cal. Civ. Code §1798.81.5 (reasonable security)",
     "source_status": "EU text reusable; California statute is an edict of government. Detection is the precondition for every notification clock, so the duty is real but its precise form is operational.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04", "S-33", "S-36"], "harm_classes": ["regulatory", "reputational"]},
    {"id": "VP-BN-003", "family": "BN",
     "title": "Every processor and integration vendor that holds owner data is bound to notify the practice of a breach without undue delay, and vendor incident notices land in a monitored incident queue",
     "absolute": False,
     "citation": "Cal. Civ. Code §1798.82(b); GDPR Art. 28(3)(f) and Art. 33(2)",
     "source_status": "California statute is an edict of government; EU text reusable. The maintainer-to-owner notice duty in §1798.82(b) runs 'immediately following discovery'.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04", "S-13"], "harm_classes": ["legal", "regulatory"]},

    # ---- DR: DEA reporting, ordering, diversion --------------------------
    {"id": "VP-DR-001", "family": "DR",
     "title": "A theft or significant loss of a controlled substance is notified to the DEA within one business day of discovery and followed by an electronic Form 106 within forty-five days; no threshold, flag or workflow setting suppresses either filing",
     "absolute": True,
     "citation": "21 CFR 1301.76(b); Reporting Theft or Significant Loss of Controlled Substances, 88 FR 40707 (22 June 2023, effective 24 July 2023)",
     "source_status": "US CFR and Federal Register — public domain. Verified 6 Sept 2026: the 2023 final rule requires the Form 106 to be filed electronically within 45 calendar days of discovery; the one-business-day written notice is unchanged. Absolute because the registrant, not the software vendor or the practice manager, owes the duty and cannot waive it.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-04", "S-37"], "harm_classes": ["legal", "regulatory", "safety"]},
    {"id": "VP-DR-002", "family": "DR",
     "title": "Schedule II orders are placed only through CSOS with a DEA-issued digital certificate or on an official Form 222, and the order records are retained for two years at the registered location",
     "absolute": True,
     "citation": "21 CFR 1305.03, 1305.13, 1305.17 (paper), 1305.21–1305.22, 1305.27 (CSOS)",
     "source_status": "US CFR — public domain. Absolute because an order for a Schedule II substance placed outside Part 1305 is unlawful on its face; there is no registrant-level discretion to accept the risk.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-37", "S-03"], "harm_classes": ["legal", "regulatory"]},
    {"id": "VP-DR-003", "family": "DR",
     "title": "The biennial controlled-substance inventory is taken at least every two years by an actual count, signed by a named licensee, and is never skipped, auto-filled from the ledger balance or left unsigned",
     "absolute": True,
     "citation": "21 CFR 1304.11(c), 1304.11(e)(3) (exact count for Schedule II; estimate permitted only for opened Schedule III–V containers below 1,000 units)",
     "source_status": "US CFR — public domain. Absolute because the inventory is a registrant duty with a fixed statutory cadence; the existing VP-CS-008 covers reconciliation between inventories, this covers the inventory itself.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-37", "S-03"], "harm_classes": ["legal", "regulatory"]},
    {"id": "VP-DR-004", "family": "DR",
     "title": "Diversion analytics over dispensing and inventory events run for every practice and route their findings to the medical director; they are never disabled, sampled or pointed at a null sink for a named tenant",
     "absolute": False,
     "citation": "21 CFR 1301.71(a) (effective controls and procedures to guard against theft and diversion); 21 CFR 1301.76(a)",
     "source_status": "US CFR — public domain. The regulation requires effective controls but leaves their design to the registrant, so the provision is ordinary; VP-CS-011 already sets the triage window for an alert once raised.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-37", "S-33"], "harm_classes": ["legal", "regulatory", "safety"]},

    # ---- CC: client communications, consent, subscriptions, records ------
    {"id": "VP-CC-001", "family": "CC",
     "title": "No autodialed, prerecorded or artificial-voice call and no automated text is sent to a wireless number without recorded prior express consent for that purpose, written where the purpose is marketing, and no campaign path bypasses the consent check",
     "absolute": True,
     "citation": "47 U.S.C. §227(b)(1)(A); 47 CFR 64.1200(a)(1)–(3), (f)(9) (prior express written consent)",
     "source_status": "US statute and CFR — public domain. Verified 6 Sept 2026: the FCC's 2024 one-to-one-consent amendment was vacated (11th Cir., Jan 2025) and does not apply; the 2024 revocation rule is in force except the 'revoke-all' limb, whose effective date the FCC further extended (now April 2027). The HIPAA-based healthcare-message exemption in 64.1200(a)(3)(v) covers covered entities only — veterinary practices are not covered entities and cannot rely on it. Absolute because consent is a statutory element with per-message statutory damages; no officer of the practice can accept the risk on the owner's behalf.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17", "S-10"], "harm_classes": ["legal", "reputational", "financial"]},
    {"id": "VP-CC-002", "family": "CC",
     "title": "Wellness-plan and subscription enrolment discloses the automatic-renewal terms before the charge, takes affirmative consent, sends a renewal reminder, and offers cancellation through the same channel and in no more steps than enrolment",
     "absolute": False,
     "citation": "Cal. Bus. & Prof. Code §17600–17606 (Automatic Renewal Law, as amended by AB 2863 eff. 1 July 2025); ROSCA, 15 U.S.C. §8403; N.Y. Gen. Bus. Law §527-a",
     "source_status": "State statutes are edicts of government; ROSCA is a US statute. Deliberately NOT cited to the FTC Negative Option Rule (16 CFR Part 425, 2024 amendments): the Eighth Circuit vacated that rule in its entirety on 8 July 2025 (Custom Communications v. FTC) and the FTC has since restarted rulemaking. State auto-renewal laws and ROSCA carry the obligation.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17", "S-10"], "harm_classes": ["legal", "reputational"]},
    {"id": "VP-CC-003", "family": "CC",
     "title": "Before any record, invoice or notice that the law requires in writing is delivered electronically in place of paper, the client's informed E-SIGN consent is captured with the required disclosures and can be withdrawn",
     "absolute": False,
     "citation": "E-SIGN, 15 U.S.C. §7001(c)(1)",
     "source_status": "US statute — public domain. §7001(c) is the consumer-consent condition on using electronic records to satisfy a writing requirement; it does not itself require any record to be in writing.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17"], "harm_classes": ["legal", "reputational"]},
    {"id": "VP-CC-004", "family": "CC",
     "title": "Where the governing state so requires, the client is offered a written prescription in place of in-house dispensing and the offer is never hidden, fee-gated or conditioned on a purchase",
     "absolute": False,
     "citation": "Cal. Code Regs. tit. 16, §2032.2 (written prescriptions); state practice acts; AVMA policy on client requests for prescriptions (identifier only)",
     "source_status": "California regulation is an edict of government; other states vary and the provision is keyed to the jurisdiction table. The federal Fairness to Pet Owners Act was introduced in several Congresses and never enacted, so no federal floor exists — say so rather than imply one.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-10"], "harm_classes": ["legal", "reputational"]},
    {"id": "VP-CC-005", "family": "CC",
     "title": "A client's request for a copy or transfer of the patient's medical record is fulfilled within the state board's deadline and is not conditioned on payment of an outstanding balance",
     "absolute": False,
     "citation": "Cal. Code Regs. tit. 16, §2032.3 (records; transfer on request); Cal. Bus. & Prof. Code §4855; state practice acts and board rules",
     "source_status": "California regulation and statute are edicts of government; the deadline and copy-fee rules differ by state and are read from the jurisdiction table. Directionally supported for the pack's other US jurisdictions, not verified state by state.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "VP-CC-006", "family": "CC",
     "title": "A client account whose holder is under eighteen is created only with a parent or guardian's recorded consent and cannot enter a payment plan, wellness subscription or records-release authorisation on its own",
     "absolute": False,
     "citation": "State contract law (infancy doctrine; e.g. Cal. Fam. Code §6710 disaffirmance); COPPA, 15 U.S.C. §6501–6506, cited to state its limit",
     "source_status": "State statute is an edict of government. COPPA does not reach veterinary medical records as such and would apply only if the portal knowingly collected personal information online from a child under thirteen; the operative floor for account and payment consent is state contract law, under which a minor may disaffirm.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-10"], "harm_classes": ["legal", "financial", "reputational"]},

    # ---- PS: patient safety and clinical decision support ----------------
    {"id": "VP-PS-001", "family": "PS",
     "title": "Every weight-based dose is computed from a current recorded weight in a declared unit, and a unit mismatch or a dose outside the species range is a hard stop, never a dismissable warning or an override button",
     "absolute": True,
     "citation": "Clinical safety floor; 21 CFR 530.20 (labelled dosage regime for extralabel use); state practice acts (standard of care)",
     "source_status": "Safety floor in the sense of Definition 1: a tenfold pound/kilogram or mg-per-mL error is irreversible in the patient and no officer of the practice may accept it. The CFR pin gives the labelled-dose regime the check is measured against; the floor itself is safety, not statute.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08", "S-24"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "VP-PS-002", "family": "PS",
     "title": "An AI triage or advice tool discloses on every turn that it is automated, never presents itself as a licensed veterinarian, never issues a diagnosis or treatment instruction, and hands off to licensed staff on any red-flag presentation",
     "absolute": False,
     "citation": "Cal. Bus. & Prof. Code §4825 (unlicensed practice), §4826 (practice of veterinary medicine defined); state practice acts; EU AI Act Art. 50(1) (disclosure of interaction with an AI system, applicable from 2 Aug 2026)",
     "source_status": "California statute is an edict of government; EU text reusable. The Art. 50(1) transparency duty applied from 2 August 2026 and is relevant to the pack's EU-IE jurisdiction. Ordinary rather than absolute because the line between triage information and 'practice' is drawn by each state board.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-30", "S-05"], "harm_classes": ["safety", "legal", "reputational"]},
    {"id": "VP-PS-003", "family": "PS",
     "title": "Critical-value alerting to the attending veterinarian is never suppressed, quiet-houred, auto-acknowledged or downgraded to a passive notification, and any change to an alert route is reviewed by the medical director",
     "absolute": False,
     "citation": "Clinical safety floor; state practice acts (standard of care)",
     "source_status": "Original. Extends VP-PO-009 (which requires an acknowledged channel) to the negative duty not to suppress; kept ordinary to match VP-PO-009 so that the two provisions order consistently.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-08", "S-33", "S-36"], "harm_classes": ["safety", "reputational"]},
    {"id": "VP-PS-004", "family": "PS",
     "title": "Euthanasia is recorded only against a consent signed by a verified owner or authorised agent with the remains disposition chosen beforehand, and every transfer of remains is recorded against a scanned tag through to return or disposal",
     "absolute": True,
     "citation": "State practice acts and board rules on informed consent (e.g. 49 Pa. Code §31.21, Principle 7; Cal. Code Regs. tit. 16, §2032.3 record contents); 21 CFR 1304.22 (dispensing record for the euthanasia solution); AVMA Guidelines for the Euthanasia of Animals 2020 (identifier only)",
     "source_status": "US CFR is public domain; state instruments are edicts of government. The specific state pins are directionally supported, not verified state by state. Absolute because the act is irreversible and a wrong-patient euthanasia or a lost body cannot be cured by any later risk acceptance.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-29", "S-08"], "harm_classes": ["safety", "legal", "reputational"]},

    # ---- PH: public health and mandated reporting -------------------------
    {"id": "VP-PH-001", "family": "PH",
     "title": "Reporting of a reportable or zoonotic disease to the state animal-health official and, where required, USDA APHIS is never gated behind a practice toggle, filtered by a pruned condition list or batched past the statutory window",
     "absolute": True,
     "citation": "9 CFR 161.4(f) (accredited veterinarian's duty to report immediately); USDA APHIS National List of Reportable Animal Diseases; Cal. Food & Agr. Code §9101; state reportable-condition lists",
     "source_status": "US CFR — public domain; California statute is an edict of government. State lists differ and are read from a versioned fixture. Absolute because the duty is placed on the veterinarian by statute and regulation and the harm (undetected spread) falls on third parties who cannot consent.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-29", "S-04"], "harm_classes": ["safety", "legal", "regulatory"]},
    {"id": "VP-PH-002", "family": "PH",
     "title": "A rabies vaccination certificate is issued only under the signature of a currently licensed veterinarian, never a technician's, an expired licence or a signature applied automatically from a template",
     "absolute": False,
     "citation": "State rabies statutes and regulations (e.g. Cal. Health & Safety Code §121690; 25 Tex. Admin. Code §169.29); NASPHV Form 51 (identifier only)",
     "source_status": "State instruments are edicts of government; directionally supported, not verified state by state as of 6 Sept 2026. Ordinary because some states permit issuance under a veterinarian's direct supervision, so the rule is keyed to the jurisdiction table.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-29"], "harm_classes": ["legal", "safety"]},
    {"id": "VP-PH-003", "family": "PH",
     "title": "The path for a clinician to record and file a suspected animal-abuse report stays reachable from the chart, is visible only to authorised roles and is never exposed on the client portal",
     "absolute": False,
     "citation": "State practice acts (e.g. Cal. Bus. & Prof. Code §4830.5, permissive reporting with immunity; mandatory in several states)",
     "source_status": "California statute is an edict of government. Whether reporting is mandatory or permissive varies by state; the software floor is that the path exists and is confidential either way.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-29"], "harm_classes": ["legal", "safety", "reputational"]},
    {"id": "VP-PH-004", "family": "PH",
     "title": "Microchip identifiers are validated against the ISO format, registry submissions are confirmed or surfaced on failure, and ownership on a chip record changes only after verified ownership, never by client self-service",
     "absolute": False,
     "citation": "ISO 11784 / 11785 (identifiers only); Cal. Food & Agr. Code §31108.3 (shelter microchipping); registry terms of service",
     "source_status": "ISO standards cited by identifier only. No federal law governs private microchip registries; the state statute named applies to shelters, and the duty for a private practice is one of data integrity toward the owner and the reunification system.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-29", "S-33"], "harm_classes": ["reputational", "safety"]},

    # ---- AX: accessibility --------------------------------------------------
    {"id": "VP-AX-001", "family": "AX",
     "title": "The client portal and mobile check-in app carry an accessibility regression gate at WCAG 2.2 Level AA in the release pipeline, and a Level A or AA failure blocks release rather than being downgraded to a warning",
     "absolute": False,
     "citation": "ADA Title III, 42 U.S.C. §12182; 28 CFR Part 36; WCAG 2.2 (W3C Recommendation, 5 Oct 2023), Level AA; Directive (EU) 2019/882 (European Accessibility Act, applicable from 28 June 2025) for EU-IE",
     "source_status": "US statute and CFR are public domain; EU text reusable; WCAG cited by identifier. Note: DOJ's 2024 web-accessibility rule is 28 CFR Part 35 and binds state and local governments (Title II) only; no Title III web rule has been issued, so the WCAG 2.2 AA target for a private practice rests on Title III case law and the EAA.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-16"], "harm_classes": ["legal", "reputational"]},
    {"id": "VP-AX-002", "family": "AX",
     "title": "Consent, e-signature and check-in flows are operable with assistive technology: keyboard-only completion, accessible names on every control, errors and status conveyed in text not colour alone, and session timeouts the client can extend",
     "absolute": False,
     "citation": "ADA Title III, 42 U.S.C. §12182(b)(2)(A)(iii) (auxiliary aids and services); WCAG 2.2 SC 1.4.1, 2.1.1, 2.1.2, 2.2.1, 2.5.7, 4.1.2 (identifiers only)",
     "source_status": "US statute is public domain; WCAG cited by success-criterion identifier. Inaccessible consent is also a consent-validity problem (S-17), which is why the family maps to both scenarios.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-16", "S-17"], "harm_classes": ["legal", "reputational"]},
]

# --------------------------------------------------------------------------
# Scenario coverage for the pack's EXISTING families.
# --------------------------------------------------------------------------

FAMILY_SCENARIOS = {
    "CS": ["S-37", "S-03"],
    "VC": ["S-37"],
    "PO": ["S-08", "S-33"],
    "PD": ["S-02", "S-18", "S-14", "S-10", "S-17"],
    "RB": ["S-02"],
    "SC": ["S-13", "S-14"],
    "AI": ["S-12", "S-24"],
    "AS": ["S-14"],
    "HA": ["S-36", "S-15"],
    "RR": ["S-03", "S-33"],
    "AW": ["S-29"],
    "GV": ["S-34", "S-11", "S-05"],
}

# Per-provision overrides where a single existing provision is the real hook.
PROVISION_SCENARIOS = {
    # S-15 and S-36 would otherwise map only to HA, whose six provisions are
    # all reserved for the novel and docket mechanics and so never receive a
    # compliant touch, a plain violation or a risk-owner acceptance.
    "VP-SC-001": ["S-13", "S-14", "S-15"],
    "VP-SC-009": ["S-13", "S-15"],
    "VP-CS-005": ["S-03", "S-37"],
    "VP-PD-002": ["S-10", "S-17"],
    "VP-PD-007": ["S-17"],
    "VP-PO-001": ["S-08"],
    "VP-PO-009": ["S-08", "S-33"],
    "VP-AI-002": ["S-12", "S-37"],
    "VP-AI-008": ["S-12", "S-24"],
    "VP-HA-003": ["S-15"],
    "VP-GV-001": ["S-11"],
    "VP-GV-002": ["S-05"],
    "VP-GV-004": ["S-34"],
}

# --------------------------------------------------------------------------
# Draft amendments: findings about EXISTING provisions, filed not applied.
# The pack carries no amendments yet, so the sequence starts at PA-01.
# --------------------------------------------------------------------------

PROPOSED_AMENDMENTS = [
    {
        "id": "PA-01",
        "targets": ["VP-CS-005"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "The two-year retention floor is cited to 21 CFR 1304.04 and 1304.11. "
            "Verified: 1304.04(a) is the retention provision; 1304.11 is the "
            "inventory-requirements section and says nothing about how long a "
            "record is kept. The statutory root, 21 U.S.C. §827(b), is not cited "
            "at all. The obligation is real and the absolute status is sound; the "
            "second pin points a later adjudicator at the wrong section."),
        "proposed": (
            "Restate the citation as '21 U.S.C. §827(b); 21 CFR 1304.04(a)' and "
            "leave the provision text and its absolute status unchanged. The "
            "inventory cadence 1304.11 actually governs is now carried by VP-DR-003."),
        "why_not_applied": (
            "A citation is what the adjudicator reasons from; changing it under a "
            "frozen revision would move the ground beneath seed records that "
            "interpret the provision as cited. That is a legislative act."),
        "disposition": "pending",
    },
    {
        "id": "PA-02",
        "targets": ["VP-CS-006"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "The provision makes second-licensee witnessing of euthanasia-solution "
            "dispensing an absolute and cites 21 CFR 1304.22. Verified: 1304.22(c) "
            "requires a dispensing record (date, quantity, patient, dispenser) but "
            "contains no witness requirement. The witness rule comes from state "
            "board regulations and practice policy, and its scope varies by state. "
            "As written the absolute rests on a federal source that does not state "
            "it, which is a severity claim wearing a statutory label (Definition 1)."),
        "proposed": (
            "Split the provision: keep 'recorded against a named licensee' absolute "
            "on 21 CFR 1304.22(c) and 21 U.S.C. §827; move 'and witnessed' into an "
            "ordinary provision cited to state board rules and keyed to the "
            "jurisdiction table, so a state that does not require a witness does not "
            "produce an F-absolute case against a compliant practice."),
        "why_not_applied": (
            "Reclassifying an absolute changes which cases short-circuit under A6 and "
            "invalidates every F-absolute record built on it. Only the legislature "
            "may do that."),
        "disposition": "pending",
    },
    {
        "id": "PA-03",
        "targets": ["VP-PD-002"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "'Withdrawing consent is no harder than granting it' is absolute and "
            "cited to 'EU AI Act and GDPR principles'. Verified: the operative text "
            "is GDPR Art. 7(3), final sentence ('It shall be as easy to withdraw as "
            "to give consent'); the AI Act contains no such rule. The provision is "
            "correct and the absolute status defensible for EU-IE and UK-ENG (UK "
            "GDPR Art. 7(3)), but for the six US jurisdictions the source is the "
            "FCC revocation rule (47 CFR 64.1200(a)(10), partly in force) and state "
            "auto-renewal law, none of which is cited."),
        "proposed": (
            "Re-pin to 'GDPR Art. 7(3); UK GDPR Art. 7(3); 47 CFR 64.1200(a)(10) "
            "for US jurisdictions' and drop the AI Act reference. Note the overlap "
            "with the new VP-CC-002 (cancellation as easy as sign-up) so the two "
            "provisions order rather than compete."),
        "why_not_applied": (
            "Re-anchoring a shipped absolute is a legislative act under A3; the "
            "overlap note is for the legislature, not the editor."),
        "disposition": "pending",
    },
    {
        "id": "PA-04",
        "targets": ["VP-RR-001"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "The append-only audit trail is cited to '21 CFR 1304.04 record "
            "integrity; SEC Rule 17a-4 analogue'. Verified: 1304.04 is a retention "
            "and availability rule and does not speak to in-place update; SEC Rule "
            "17a-4 governs broker-dealers and has no bearing on a veterinary "
            "practice. The nearest instrument that actually binds this software is "
            "21 CFR 1311.120(b)(...) and 1311.150 (the EPCS application's internal "
            "audit trail and its daily review), which are not cited."),
        "proposed": (
            "Restate the citation as '21 CFR 1311.120(b) and 1311.150 (EPCS audit "
            "trail); 21 CFR 1304.04 (availability)' and delete the SEC analogue. "
            "Keep the absolute: immutability of the controlled-substance audit "
            "trail is a registrant duty."),
        "why_not_applied": (
            "Citation changes to an absolute alter what later adjudicators reason "
            "from and are reserved to legislation."),
        "disposition": "pending",
    },
    {
        "id": "PA-05",
        "targets": ["VP-AW-003", "VP-AW-005"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "Both provisions cite 9 CFR Part 2 without stating its scope. Verified: "
            "Part 2 implements the Animal Welfare Act for USDA-licensed dealers, "
            "exhibitors and registered research facilities. A private companion- or "
            "large-animal practice is not, as such, a regulated facility, and the "
            "'adequate veterinary care' programme of 9 CFR 2.33 and 2.40 attaches to "
            "the licensee, with the attending veterinarian as its instrument. As "
            "drafted the provisions can charge an ordinary clinic with a duty it "
            "does not owe."),
        "proposed": (
            "Add the scope qualifier 'for a patient or premises that is a "
            "USDA-licensed or registered facility' to both titles and pin the "
            "citations to 9 CFR 2.33 (research facilities) and 2.40 (dealers and "
            "exhibitors) and 2.126 (access to records)."),
        "why_not_applied": (
            "Narrowing a provision's scope changes which arrivals are charged; that "
            "is a rule change, not an edit."),
        "disposition": "pending",
    },
    {
        "id": "PA-06",
        "targets": ["VP-PO-009"],
        "raised_by": "corpus survey 2.0.0 scenario extension (vetpoc)",
        "finding": (
            "VP-PO-009 (critical values surfaced through an acknowledged channel) "
            "and the new VP-PS-003 (critical-value alerting never suppressed) "
            "approach the same floor from the positive and the negative side. Both "
            "are ordinary and cited to 'clinical safety floor'. A change that "
            "suppresses the alert can now be charged under either, and the two "
            "will tie on every ordering key (K-tie) more often than the corpus "
            "designers intended."),
        "proposed": (
            "The legislature should either merge the two into one provision under "
            "PS with both duties stated, or mark VP-PO-009 as the delivery-channel "
            "rule and VP-PS-003 as the non-suppression rule in their titles so that "
            "the distinguishing gate can separate them."),
        "why_not_applied": (
            "The extension adds and never edits (A3). The overlap is filed so the "
            "legislature can decide which text survives."),
        "disposition": "pending",
    },
]

# New families whose cases concern a named service or asset rather than a
# patient (the clinical families remain CS VC PO AW; PS is added to the
# clinical set by the merge shim where it honours CLINICAL_FAMILIES).
FLOOR_FACING_FAMILIES = {"BN", "DR", "CC", "PH", "AX"}
