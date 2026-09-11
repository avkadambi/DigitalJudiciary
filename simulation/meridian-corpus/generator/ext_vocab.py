"""
Meridian Financial Constitution Corpus — scenario extension (corpus 2.0.0).

Seven new provision families closing the gaps the architect's scenario survey
found in this pack's constitution: payment security and open banking, fraud and
account takeover, consumer notices and communications, deposit fees and account
handling, servicemember and vulnerable-customer protections, data rights and
accessibility, and the virtual-asset limb of the financial-crime programme.

Everything here is additive. Under Axiom A3 no existing provision, factor,
title or citation is edited; findings about existing provisions are filed below
as draft amendments PA-08 to PA-12 and left pending, continuing the sequence
the pack already carries at PA-01 to PA-07.

Licensing posture is vocab.py's. US statutes, the CFR and the Federal Register
are US Government works (17 U.S.C. §105). EU law is reusable under Commission
Decision 2011/833/EU. UK regulatory material is Open Government Licence v3.0.
California statutes and the CPPA regulations are edicts of government. PCI,
ISO, W3C, FFIEC and FATF material is cited by identifier; FATF typologies are
CC BY 4.0. Provision prose is original drafting.

Citations were shelf-life checked on 6 September 2026. Where an instrument's
current status could not be confirmed the source_status says "directionally
supported, not verified" rather than asserting it.
"""

# --------------------------------------------------------------------------
# New families.
#
# Factor pools are sliced positionally by the generator: the n-th provision of
# a family (0-based, in PROVISIONS order) receives comply[3n:3n+8] and
# violate[2n:2n+5] with wrap-around. The pools below are therefore ORDERED so
# that provision n's decisive violate factors sit at 2n and 2n+1 and its most
# characteristic comply factors at 3n..3n+2. Overlap between neighbours is
# expected; it is how every family in vocab.py already works.
# --------------------------------------------------------------------------

FAMILIES = {
    "PS": {
        "title": "Payment security, strong authentication and open banking",
        "risk": "2.2 PSD2 SCA and the Instant Payments Regulation; APP-fraud reimbursement",
        "comply": [
            # MF-601 (0..2)
            "sca_applied_on_every_remote_payment_initiation",
            "sca_exemption_taken_only_from_the_declared_list",
            "dynamic_linking_binds_amount_and_payee_to_the_code",
            # MF-602 (3..5)
            "payee_name_verified_before_the_transfer_is_confirmed",
            "verification_result_shown_to_the_payer_before_confirmation",
            "payee_matching_response_returned_within_the_declared_time",
            # MF-603 (6..8)
            "reimbursement_assessment_runs_on_every_reported_scam_claim",
            "reimbursement_decision_recorded_within_the_required_window",
            "vulnerable_customer_flag_suppresses_the_claim_excess",
            # MF-604 (9..11)
            "request_for_payment_sender_verified_before_delivery",
            "instant_payment_fraud_score_evaluated_before_settlement",
            "payment_recall_path_available_on_the_instant_rail",
            # shared tail
            "authentication_element_independence_tested_before_release",
            "exemption_fraud_rate_monitored_against_the_declared_threshold",
            "account_access_consent_re_authenticated_on_expiry",
            "third_party_provider_certificate_validated_at_the_interface",
            "payer_notified_of_a_mismatch_before_funds_leave",
            "strong_authentication_outcome_recorded_in_the_payment_record",
        ],
        "violate": [
            # MF-601 (0,1)
            "strong_authentication_skipped_outside_the_declared_exemptions",
            "dynamic_linking_removed_from_the_authentication_code",
            # MF-602 (2,3)
            "payee_name_check_bypassed_for_bulk_transfers",
            "payee_mismatch_warning_hidden_from_the_payer",
            # MF-603 (4,5)
            "scam_reimbursement_threshold_made_a_product_setting",
            "reimbursement_claim_window_shortened_by_configuration",
            # MF-604 (6,7)
            "request_for_payment_sender_verification_disabled",
            "instant_payment_fraud_scoring_bypassed_under_load",
            # shared tail
            "authentication_elements_drawn_from_the_same_category",
            "exemption_fraud_rate_monitoring_removed",
            "account_access_consent_renewed_without_re_authentication",
            "third_party_certificate_validation_made_advisory",
        ],
    },
    "FR": {
        "title": "Fraud, identity theft, account takeover and applicant identity",
        "risk": "2.2 Red Flags / Reg S-ID; FFIEC authentication; FCRA permissible purpose",
        "comply": [
            # MF-605 (0..2)
            "identity_theft_red_flag_rules_evaluated_on_every_application",
            "red_flag_detection_triggers_the_documented_response",
            "red_flag_programme_updated_on_the_declared_review_cycle",
            # MF-606 (3..5)
            "step_up_challenge_required_on_high_risk_account_changes",
            "device_and_behaviour_signals_feed_the_risk_decision",
            "authentication_bypass_route_removed_from_the_recovery_flow",
            # MF-607 (6..8)
            "identity_attributes_verified_against_an_authoritative_source",
            "synthetic_identity_indicators_scored_before_funding",
            "applicant_identity_element_reuse_checked_across_accounts",
            # MF-608 (9..11)
            "permissible_purpose_recorded_before_the_consumer_report_pull",
            "permissible_purpose_certification_bound_to_the_requesting_role",
            "soft_pull_and_hard_pull_distinguished_in_the_request",
            # MF-609 (12..14)
            "applicant_date_of_birth_verified_before_account_opening",
            "adult_custodian_verified_on_a_minor_account",
            "parental_consent_captured_before_a_child_record_is_created",
            # shared tail
            "account_takeover_alert_routed_to_the_fraud_queue",
            "credential_stuffing_detection_enabled_on_the_login_path",
            "change_of_address_followed_by_a_notice_to_the_prior_address",
            "fraud_model_thresholds_reviewed_against_recorded_outcomes",
            "identity_document_check_result_retained_with_the_application",
        ],
        "violate": [
            # MF-605 (0,1)
            "identity_theft_red_flag_rules_switched_off_for_a_channel",
            "red_flag_detection_left_without_a_response_path",
            # MF-606 (2,3)
            "step_up_challenge_dropped_from_high_risk_account_changes",
            "account_recovery_flow_reintroduces_an_authentication_bypass",
            # MF-607 (4,5)
            "synthetic_identity_screening_skipped_for_thin_file_applicants",
            "identity_attributes_accepted_without_authoritative_verification",
            # MF-608 (6,7)
            "consumer_report_pulled_without_a_recorded_permissible_purpose",
            "permissible_purpose_defaulted_to_a_blanket_value",
            # MF-609 (8,9)
            "minor_account_opened_without_a_verified_adult_custodian",
            "child_personal_information_collected_without_parental_consent",
            # shared tail
            "account_takeover_alerts_routed_to_an_unmonitored_queue",
            "change_of_address_notice_removed_from_the_servicing_flow",
            "credential_stuffing_detection_disabled_on_the_login_path",
        ],
    },
    "CN": {
        "title": "Consumer notices, electronic consent and communications",
        "risk": "2.2 E-SIGN, TCPA, Reg P and Reg F; UDAAP communications",
        "comply": [
            # MF-610 (0..2)
            "esign_consent_captured_before_electronic_delivery",
            "hardware_and_software_requirements_disclosed_at_consent",
            "paper_copy_route_retained_after_electronic_consent",
            # MF-611 (3..5)
            "prior_express_consent_recorded_before_an_automated_message",
            "written_consent_required_where_the_message_is_marketing",
            "opt_out_keyword_processed_on_the_next_send",
            # MF-612 (6..8)
            "privacy_notice_delivered_before_information_is_shared",
            "sharing_opt_out_propagated_to_every_disclosure_path",
            "annual_notice_exception_conditions_checked_before_relying_on_it",
            # MF-613 (9..11)
            "collection_contact_attempts_counted_against_the_weekly_cap",
            "consumer_contact_suppressed_after_a_cease_request",
            "validation_information_delivered_before_collection_activity",
            # shared tail
            "consent_revocation_honoured_across_every_channel",
            "message_send_window_kept_within_permitted_hours",
            "disclosure_delivery_evidenced_with_a_timestamp",
            "consent_scope_matched_to_the_message_purpose",
            "servicing_notice_available_in_the_channel_the_consumer_chose",
            "electronic_consent_withdrawable_from_the_same_surface",
        ],
        "violate": [
            # MF-610 (0,1)
            "electronic_disclosure_delivered_without_electronic_consent",
            "electronic_consent_inferred_from_a_portal_login",
            # MF-611 (2,3)
            "automated_message_sent_without_recorded_prior_consent",
            "opt_out_keyword_left_unprocessed_by_the_campaign_sender",
            # MF-612 (4,5)
            "privacy_notice_skipped_before_a_new_sharing_flow",
            "sharing_opt_out_not_propagated_to_a_new_disclosure_path",
            # MF-613 (6,7)
            "collection_contact_cap_removed_from_the_dialer",
            "cease_communication_request_ignored_by_the_dialer",
            # shared tail
            "consent_revocation_honoured_on_one_channel_only",
            "messages_scheduled_outside_the_permitted_hours",
            "validation_information_delivered_after_collection_begins",
            "disclosure_delivery_recorded_without_any_evidence",
        ],
    },
    "FP": {
        "title": "Deposit fees, funds availability and account handling",
        "risk": "2.2 Reg DD, Reg E overdraft, Reg CC; state unclaimed-property law",
        "comply": [
            # MF-614 (0..2)
            "fee_schedule_and_yield_disclosed_before_account_opening",
            "fee_change_notice_sent_before_the_change_takes_effect",
            "advertised_yield_matches_the_declared_computation_method",
            # MF-615 (3..5)
            "overdraft_opt_in_recorded_before_any_overdraft_fee",
            "overdraft_service_defaults_to_declined_without_opt_in",
            "opt_in_confirmation_delivered_in_the_required_form",
            # MF-616 (6..8)
            "funds_availability_schedule_read_from_the_regulated_table",
            "next_business_day_availability_applied_to_qualifying_deposits",
            "exception_hold_notice_issued_when_a_hold_is_placed",
            # MF-617 (9..11)
            "dormancy_period_read_from_the_state_property_table",
            "owner_due_diligence_notice_sent_before_remittance",
            "unclaimed_property_report_filed_on_the_state_schedule",
            # shared tail
            "closing_balance_returned_or_escheated_rather_than_absorbed",
            "fee_waiver_rules_applied_consistently_across_portfolios",
            "statement_shows_every_fee_charged_in_the_period",
            "hold_reason_recorded_against_the_deposit",
            "dormant_account_fee_limits_read_from_the_state_table",
            "posting_order_documented_and_applied_as_disclosed",
        ],
        "violate": [
            # MF-614 (0,1)
            "account_fee_omitted_from_the_pre_opening_disclosure",
            "yield_advertised_on_a_method_other_than_the_declared_one",
            # MF-615 (2,3)
            "overdraft_fee_charged_without_a_recorded_opt_in",
            "overdraft_service_defaulted_to_enabled_at_account_opening",
            # MF-616 (4,5)
            "funds_availability_hold_extended_beyond_the_regulated_schedule",
            "exception_hold_placed_without_a_notice_to_the_depositor",
            # MF-617 (6,7)
            "dormancy_clock_reset_by_an_internal_system_event",
            "unclaimed_property_remittance_deferred_past_the_state_deadline",
            # shared tail
            "due_diligence_notice_dropped_from_the_dormancy_job",
            "dormant_account_fees_applied_beyond_the_state_limit",
            "posting_order_changed_to_maximise_fee_events",
            "fee_change_applied_before_the_notice_period_elapses",
        ],
    },
    "MP": {
        "title": "Military, servicemember and vulnerable-customer protections",
        "risk": "2.2 MLA and SCRA; elder financial exploitation",
        "comply": [
            # MF-618 (0..2)
            "covered_borrower_status_checked_before_consummation",
            "military_annual_percentage_rate_computed_with_every_charge",
            "prohibited_loan_terms_refused_for_a_covered_borrower",
            # MF-619 (3..5)
            "service_member_rate_cap_applied_on_valid_notice",
            "repossession_gated_on_a_court_order_during_service",
            "protected_status_flag_persisted_across_servicing_transfers",
            # MF-620 (6..8)
            "suspected_elder_exploitation_escalated_to_the_named_team",
            "transaction_hold_available_where_state_law_permits_one",
            "trusted_contact_recorded_and_used_on_escalation",
            # shared tail
            "covered_borrower_check_result_retained_with_the_loan_file",
            "oral_and_written_military_disclosures_delivered_before_consummation",
            "interest_refunded_where_the_rate_cap_applied_retroactively",
            "exploitation_response_playbook_versioned_in_the_policy_repo",
            "exploitation_reporting_path_reachable_from_the_servicing_case",
            "vulnerability_flag_suppresses_the_aggressive_collection_paths",
        ],
        "violate": [
            # MF-618 (0,1)
            "covered_borrower_check_skipped_to_shorten_the_application",
            "military_annual_percentage_rate_computed_without_all_charges",
            # MF-619 (2,3)
            "service_member_rate_cap_left_unapplied_after_valid_notice",
            "repossession_executed_without_the_required_court_order",
            # MF-620 (4,5)
            "elder_exploitation_escalation_path_removed_from_servicing",
            "suspected_exploitation_alerts_downgraded_to_a_report_only",
            # shared tail
            "protected_status_flag_dropped_on_a_servicing_transfer",
            "prohibited_loan_term_offered_to_a_covered_borrower",
            "trusted_contact_field_dropped_from_the_account_record",
            "vulnerability_flag_ignored_by_the_collections_router",
        ],
    },
    "DA": {
        "title": "Data-subject rights, opt-out signals and accessibility",
        "risk": "2.1 GDPR access and portability; CPRA opt-out signals; accessibility floor",
        "comply": [
            # MF-621 (0..2)
            "access_request_fulfilled_within_the_statutory_month",
            "portable_export_produced_in_a_structured_machine_readable_form",
            "extension_of_the_response_period_notified_with_reasons",
            # MF-622 (3..5)
            "accessibility_regression_suite_runs_on_the_portal_build",
            "conformance_failure_blocks_the_customer_surface_release",
            "status_and_errors_conveyed_in_text_not_colour_alone",
            # MF-623 (6..8)
            "opt_out_preference_signal_detected_on_page_load",
            "signal_derived_opt_out_applied_without_further_prompting",
            "opt_out_state_linked_to_the_known_customer_record",
            # shared tail
            "requester_identity_verified_before_any_disclosure",
            "third_party_data_redacted_from_the_access_response",
            "keyboard_only_completion_verified_for_the_payment_flow",
            "accessible_name_present_on_every_interactive_control",
            "rights_request_intake_reachable_from_the_customer_portal",
            "rights_requests_logged_with_their_due_dates",
        ],
        "violate": [
            # MF-621 (0,1)
            "access_request_left_unanswered_past_the_statutory_month",
            "portable_export_returned_only_as_a_rendered_document",
            # MF-622 (2,3)
            "accessibility_gate_removed_from_the_portal_pipeline",
            "conformance_failures_downgraded_to_warnings_in_the_pipeline",
            # MF-623 (4,5)
            "opt_out_preference_signal_ignored_by_the_new_surface",
            "signal_derived_opt_out_overridden_by_a_banner_choice",
            # shared tail
            "requester_identity_check_dropped_from_the_access_path",
            "third_party_data_returned_unredacted_in_an_access_response",
            "dispute_status_conveyed_by_colour_alone",
            "payment_flow_completable_only_with_a_pointing_device",
        ],
    },
    "VA": {
        "title": "Virtual assets and the breadth of the financial-crime programme",
        "risk": "2.2 Travel Rule, currency transaction reporting, 314(a), PEP and EDD",
        "comply": [
            # MF-624 (0..2)
            "counterparty_wallet_provider_identified_before_the_transfer",
            "originator_and_beneficiary_records_transmitted_with_the_transfer",
            "unhosted_wallet_transfer_recorded_with_the_declared_evidence",
            # MF-625 (3..5)
            "currency_transaction_aggregation_runs_across_the_business_day",
            "currency_transaction_report_emitted_within_the_statutory_window",
            "reporting_exemption_supported_by_a_filed_designation",
            # MF-626 (6..8)
            "information_request_list_matched_across_every_account_system",
            "politically_exposed_person_screening_runs_at_onboarding_and_refresh",
            "enhanced_due_diligence_file_completed_before_the_relationship_opens",
            # shared tail
            "blockchain_analytics_risk_score_evaluated_before_settlement",
            "sanctioned_wallet_addresses_refreshed_from_the_published_list",
            "information_request_search_results_retained_for_the_required_period",
            "relationship_risk_rating_refreshed_on_the_declared_cycle",
            "correspondent_relationship_due_diligence_recorded_before_opening",
            "report_filing_evidence_retained_with_the_transaction_record",
        ],
        "violate": [
            # MF-624 (0,1)
            "virtual_asset_transfer_sent_without_the_originator_record",
            "counterparty_wallet_provider_left_unidentified_before_transfer",
            # MF-625 (2,3)
            "currency_transaction_report_suppressed_by_a_threshold_setting",
            "same_day_currency_transactions_left_unaggregated",
            # MF-626 (4,5)
            "information_request_search_narrowed_to_open_accounts_only",
            "politically_exposed_person_screening_dropped_from_refresh",
            # shared tail
            "enhanced_due_diligence_file_deferred_until_after_funding",
            "sanctioned_wallet_address_list_left_unrefreshed",
            "blockchain_analytics_scoring_bypassed_for_priority_partners",
            "correspondent_due_diligence_recorded_after_the_first_payment",
        ],
    },
}

# Families whose floors are strict-liability filings, statutory caps or
# statutory clocks sit low; the ordinary operational families sit in the middle
# of the pack's existing range (FC 15 .. PR 34).
TAU = {
    "PS": 18,
    "FR": 20,
    "CN": 26,
    "FP": 22,
    "MP": 16,
    "DA": 28,
    "VA": 16,
}

# --------------------------------------------------------------------------
# New provisions. Ids continue the pack's MF-NNN sequence from MF-596.
# --------------------------------------------------------------------------

PROVISIONS = [
    # ---- PS: payment security, strong authentication, open banking -------
    {"id": "MF-601", "family": "PS",
     "title": "Strong customer authentication is applied to every remote electronic payment and every access to payment account information, with dynamic linking to the amount and the payee, and an exemption is taken only from the exhaustive list the technical standard allows",
     "absolute": True,
     "citation": "PSD2, Dir. (EU) 2015/2366 Art. 97; Commission Delegated Reg. (EU) 2018/389 (RTS on SCA and common and secure communication), Arts. 4-5 (dynamic linking) and 10-20 (exemptions)",
     "source_status": "EU texts reusable under Decision 2011/833/EU. The exemption list in the RTS is exhaustive and is set by the Commission, not by the payment service provider; a firm may not invent an exemption or accept the risk of skipping authentication, which is what makes this a who-may-decide floor rather than a severity claim. The PSD3 Directive and Payment Services Regulation proposals were still in the legislative procedure at the last check and are not relied on here — directionally supported, not verified as of 6 September 2026.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-10"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-602", "family": "PS",
     "title": "A credit transfer in euro is checked against the payee's name before the payer confirms it, the match result is shown to the payer, and no batch, bulk or retry path skips the check",
     "absolute": False,
     "citation": "Instant Payments Regulation, Reg. (EU) 2024/886, inserting Art. 5c into Reg. (EU) 260/2012 (verification of payee), applicable from 9 October 2025",
     "source_status": "EU text reusable. Ordinary rather than absolute: the regulation gives the payer the right to be told of a mismatch and to proceed anyway, so the duty is to run the check and surface the result, not to block the payment — a duty whose implementation the firm may legitimately shape.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-10"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-603", "family": "PS",
     "title": "Mandatory reimbursement of an authorised push-payment scam victim, its assessment window and its treatment of vulnerable customers are read from the regulator's direction and are never product settings",
     "absolute": True,
     "citation": "UK Payment Systems Regulator, Faster Payments APP scams reimbursement requirement in force from 7 October 2024 (Policy Statement PS24/7; Specific Direction 20 for Faster Payments, Specific Direction 21 for CHAPS), made under the Financial Services (Banking Reform) Act 2013",
     "source_status": "UK regulatory material under Open Government Licence v3.0. Absolute because the reimbursement obligation, the maximum level and the claim-excess treatment are set by the regulator's direction; a product owner who tunes them is exercising a legislative power. Note the announced consolidation of the PSR into the FCA: the direction remains the operative instrument, but the naming of the issuing body is directionally supported, not verified as of 6 September 2026.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-10", "S-25"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-604", "family": "PS",
     "title": "A request for payment carries a verified sender, and an instant-rail transfer is fraud-scored before settlement with a recall path that survives a change to the rail integration",
     "absolute": False,
     "citation": "The Clearing House RTP operating rules and FedNow Service operating procedures (identifiers only); Reg. E, 12 CFR §1005.11 for the consumer limb; Reg. (EU) 2024/886 Art. 5d on fraud-risk measures",
     "source_status": "Rail operating rules are cited by identifier and no text is reproduced; US regulation is public domain and EU text is reusable. Ordinary: the rails require fraud controls without prescribing their shape, so the firm's design is its own.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-33"], "harm_classes": ["financial", "regulatory", "reputational"]},

    # ---- FR: fraud, identity theft, account takeover, applicant identity --
    {"id": "MF-605", "family": "FR",
     "title": "The identity-theft prevention programme's red-flag rules run on every covered account and application, each detection has a documented response, and no channel is exempted by configuration",
     "absolute": False,
     "citation": "FTC Red Flags Rule, 16 CFR §681.1 and Appendix A; SEC Reg. S-ID, 17 CFR §§248.201-248.202; FACT Act §114, 15 U.S.C. §1681m(e)",
     "source_status": "US regulation and statute, public domain. Ordinary because the rule requires a programme appropriate to the institution's size and risk and leaves the red flags themselves to the firm's identification.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-33"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-606", "family": "FR",
     "title": "High-risk actions — credential reset, payee addition, limit increase, address change — require a step-up challenge whose strength matches the risk, and no recovery path reintroduces a bypass",
     "absolute": False,
     "citation": "FFIEC, Authentication and Access to Financial Institution Services and Systems (August 2021), superseding the 2005 and 2011 guidance (handbook title cited as a fact); GLBA Safeguards Rule, 16 CFR §314.4(c)(5)",
     "source_status": "US regulation public domain; the FFIEC guidance is cited by title. Ordinary: the 2021 guidance is expressly risk-based and does not mandate a specific control, so this is a firm control informed by supervisory expectation.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-14"], "harm_classes": ["regulatory", "financial", "reputational"]},
    {"id": "MF-607", "family": "FR",
     "title": "Applicant identity elements are verified against an authoritative source and scored for synthetic-identity indicators before an account is funded, including thin-file and no-file applicants",
     "absolute": False,
     "citation": "31 CFR §1020.220 (customer identification); Federal Reserve, Synthetic Identity Fraud in the U.S. Payment System (2019-2020 white-paper series) and the SSA electronic Consent Based Social Security Number Verification service, 42 U.S.C. §405(c)(2)(I)",
     "source_status": "US regulation and statute, public domain; the Federal Reserve papers are US Government works cited by title. Ordinary: no rule prescribes a synthetic-identity control, and MF-103 already carries the absolute CIP duty, so this provision states the firm's own detection duty without competing with it.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25"], "harm_classes": ["financial", "regulatory", "reputational"]},
    {"id": "MF-608", "family": "FR",
     "title": "No consumer report is obtained or used without a permissible purpose recorded before the request, certified by the requesting role and specific to that request; no blanket or defaulted purpose is accepted",
     "absolute": True,
     "citation": "FCRA, 15 U.S.C. §1681b(a) (permissible purposes) and §1681b(f) (prohibition on obtaining or using a report without one); §1681e(a) (user certification)",
     "source_status": "US statute, public domain. Absolute because §1681b(f) is a flat statutory prohibition carrying civil and, for knowing violations under §1681q, criminal liability; the permissible purposes are enumerated by Congress and no officer of the firm may add to them or accept the risk of proceeding without one.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "MF-609", "family": "FR",
     "title": "An account for an applicant the record shows to be under eighteen is opened only with a verified adult custodian, and personal information is not collected online from a child under thirteen without verifiable parental consent",
     "absolute": False,
     "citation": "COPPA, 15 U.S.C. §§6501-6506 and the FTC Children's Online Privacy Protection Rule, 16 CFR Part 312; state contract law on the infancy doctrine (e.g. Cal. Fam. Code §6710, disaffirmance)",
     "source_status": "US statute and regulation, public domain; state statute is an edict of government. COPPA reaches an online service directed to children or with actual knowledge it collects from an under-13, which a general-purpose banking product usually is not — the operative floor for opening and for payment obligations is state contract law, under which a minor may disaffirm. The 2025 amendments to Part 312 and their compliance date are directionally supported, not verified as of 6 September 2026.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-07", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- CN: consumer notices, e-consent and communications --------------
    {"id": "MF-610", "family": "CN",
     "title": "Before a disclosure the law requires in writing is delivered electronically instead of on paper, the consumer's informed consent is captured with the hardware and software statement, and the consent stays withdrawable",
     "absolute": False,
     "citation": "E-SIGN, 15 U.S.C. §7001(c)(1)(B) and (c)(1)(C)",
     "source_status": "US statute, public domain. §7001(c) is a condition on using an electronic record to satisfy a writing requirement; it does not itself make any record a writing. Ordinary because the statute prescribes the consent's content, not the surface, and a defective consent is cured by re-consenting rather than by an irreversible harm.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17", "S-10"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "MF-611", "family": "CN",
     "title": "No autodialed call, prerecorded or artificial-voice message, or automated text reaches a wireless number without recorded prior express consent for that purpose, written where the purpose is marketing, and revocation is honoured on every channel",
     "absolute": False,
     "citation": "TCPA, 47 U.S.C. §227(b)(1)(A); 47 CFR §64.1200(a)(1)-(3), (f)(9) (prior express written consent) and (a)(10) (revocation)",
     "source_status": "US statute and regulation, public domain. Verified 6 September 2026: the FCC's one-to-one-consent amendment was vacated by the Eleventh Circuit in January 2025 and is not relied on; the 2024 revocation rule is in force except the limb extending a revocation across all messages, whose effective date the FCC deferred — that deferral date is directionally supported, not verified. Kept ordinary rather than absolute because MF-401's UDAAP floor and the existing CP family already carry the consumer-facing absolutes, and a consent defect here is remediable.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17"], "harm_classes": ["legal", "financial", "reputational"]},
    {"id": "MF-612", "family": "CN",
     "title": "A privacy notice is delivered before nonpublic personal information is shared outside the exceptions, the opt-out reaches every disclosure path, and reliance on the annual-notice exception is checked against its conditions",
     "absolute": False,
     "citation": "GLBA, 15 U.S.C. §6802-6803; Reg. P, 12 CFR §§1016.4 (initial notice), 1016.5 and 1016.5(e) (annual notice and its exception), 1016.7 (opt-out) and 1016.10 (limits on disclosure)",
     "source_status": "US statute and regulation, public domain. Ordinary: the sharing itself is lawful when the notice and opt-out are given, so the duty is procedural rather than prohibitory. Distinct from MF-308, which governs data reaching a model or a provider's retention window.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-17", "S-18"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "MF-613", "family": "CN",
     "title": "Debt-collection contact frequency stays inside the presumptive seven-calls-in-seven-days limit and the seven-day post-conversation limit, a cease request stops the channel, and validation information precedes collection activity",
     "absolute": False,
     "citation": "FDCPA, 15 U.S.C. §1692c and §1692d; Reg. F, 12 CFR §1006.14(b)(2)(i)-(ii) (presumptive contact-frequency limits) and §1006.34 (validation information)",
     "source_status": "US statute and regulation, public domain. Ordinary because §1006.14(b)(2) sets a rebuttable presumption rather than a flat prohibition, so a documented exception can exist — which is exactly the distinction Definition 1 turns on.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-35", "S-17"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- FP: fees, deposits, funds availability, dormancy ----------------
    {"id": "MF-614", "family": "FP",
     "title": "Deposit account fees, the annual percentage yield and its computation method are disclosed before the account is opened, and a change in terms that reduces the yield or adds a fee is noticed before it takes effect",
     "absolute": False,
     "citation": "Truth in Savings Act, 12 U.S.C. §4301 et seq.; Reg. DD, 12 CFR §§1030.4 (account disclosures), 1030.5 (change-in-terms notice) and 1030.11 (advertising the annual percentage yield)",
     "source_status": "US statute and regulation, public domain. Ordinary: Reg. DD prescribes content and timing, and a late or incomplete disclosure is curable, so a risk owner can meaningfully accept a residual here.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-10", "S-17"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-615", "family": "FP",
     "title": "No fee is assessed for paying an ATM or one-time debit card overdraft unless the consumer's affirmative opt-in is recorded first, and the service defaults to declining the transaction until it is",
     "absolute": True,
     "citation": "Reg. E, 12 CFR §1005.17(b) (affirmative consent before assessing an overdraft fee on an ATM or one-time debit card transaction) and §1005.17(d) (segregated notice content)",
     "source_status": "US regulation, public domain. Absolute because §1005.17(b) makes the consumer's own affirmative consent the condition precedent: only the consumer may supply it, so no officer of the firm — however senior — is competent to decide the fee may be charged without it. That is Definition 1's who-may-decide test, not a claim about severity.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-10"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-616", "family": "FP",
     "title": "The funds-availability schedule, including next-business-day availability and the exception holds that may extend it, is read from the regulated table and is never lengthened, tuned or defaulted by a service setting",
     "absolute": True,
     "citation": "Expedited Funds Availability Act, 12 U.S.C. §4001 et seq.; Reg. CC, 12 CFR §§229.10, 229.12, 229.13 (exceptions) and 229.13(g) (exception notice)",
     "source_status": "US statute and regulation, public domain. Absolute because the schedule and the permitted exceptions are fixed by the regulation and its dollar amounts are set by the Bureau's inflation adjustments; a firm that lengthens a hold is legislating. The current adjusted dollar thresholds are directionally supported, not verified as of 6 September 2026, which is why the provision binds to the regulated table rather than to a number.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-10", "S-32"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-617", "family": "FP",
     "title": "Dormancy periods, owner due-diligence notices and remittance deadlines are read from the governing state's unclaimed-property table, and no internal system event resets an account's dormancy clock",
     "absolute": False,
     "citation": "State unclaimed-property acts, most of them variants of the Revised Uniform Unclaimed Property Act (2016) model; priority rules from Texas v. New Jersey, 379 U.S. 674 (1965)",
     "source_status": "State statutes are edicts of government; the RUUPA model is cited by identifier. There is no federal escheat statute — say so rather than imply one: escheat is entirely a matter of state law, which is why the provision binds to a jurisdiction table and is ordinary rather than absolute. Periods and due-diligence thresholds differ state by state and are directionally supported, not verified state by state.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-26", "S-03"], "harm_classes": ["legal", "financial", "regulatory"]},

    # ---- MP: military, servicemember, vulnerable customers ---------------
    {"id": "MF-618", "family": "MP",
     "title": "Covered-borrower status is determined before consummation, the military annual percentage rate stays at or below thirty-six per cent with every included charge counted, and the prohibited terms are refused",
     "absolute": True,
     "citation": "Military Lending Act, 10 U.S.C. §987; 32 CFR §§232.3 (military annual percentage rate), 232.4 (the thirty-six per cent limit and prohibited terms), 232.5 (covered-borrower identification and safe harbour) and 232.6 (oral and written disclosures)",
     "source_status": "US statute and regulation, public domain. Absolute because §987(f)(3) makes a credit agreement that violates the section void from inception — a consequence Congress attached to the transaction itself, which no risk owner can accept away.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-35", "S-10"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-619", "family": "MP",
     "title": "On valid notice of military service the interest rate on a pre-service obligation is reduced to six per cent with the excess forgiven, and no repossession or foreclosure of protected property proceeds without a court order",
     "absolute": True,
     "citation": "Servicemembers Civil Relief Act, 50 U.S.C. §3937 (six per cent maximum rate, excess interest forgiven), §3952 (instalment contracts: no rescission or repossession without a court order) and §3953 (mortgages and trust deeds)",
     "source_status": "US statute, public domain. Absolute because §3952 and §3953 reserve the decision to a court: the relief is granted or withheld by a judge, not by the creditor, and §3937 forgives rather than defers the excess. A firm officer who overrides either is exercising a power the statute placed elsewhere.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-35", "S-10"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-620", "family": "MP",
     "title": "The path by which suspected financial exploitation of an older or vulnerable customer is escalated, held where state law permits, and reported stays reachable from the servicing case and is never downgraded to a passive report",
     "absolute": False,
     "citation": "Senior Safe Act, Pub. L. 115-174 §303 (2018), 12 U.S.C. §3423 (immunity for trained employees of a covered financial institution); FinCEN Advisory FIN-2022-A002, Elder Financial Exploitation (15 June 2022); state mandatory-reporting statutes (e.g. Cal. Welf. & Inst. Code §15630.1)",
     "source_status": "US statute and FinCEN advisory are public domain; state statutes are edicts of government. Ordinary rather than absolute: the federal instrument grants immunity for reporting rather than compelling it, and whether reporting is mandatory varies by state, so the software floor is that the path exists and is confidential either way.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-35", "S-25"], "harm_classes": ["legal", "reputational", "financial"]},

    # ---- DA: data rights, opt-out signals and accessibility --------------
    {"id": "MF-621", "family": "DA",
     "title": "A data-subject access request is answered within one month and a portability request produces a structured, commonly used, machine-readable export; an extension is notified with its reasons rather than taken silently",
     "absolute": False,
     "citation": "GDPR, Reg. (EU) 2016/679 Arts. 15 (access) and 20 (portability), with the deadline and the two-month extension at Art. 12(3)",
     "source_status": "EU text reusable under Decision 2011/833/EU. Ordinary because Art. 12(3) itself contemplates an extension for complex requests, so the period is a bounded discretion rather than a fixed floor; the existing MF-105 and MF-558 carry the transfer and erasure duties.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18"], "harm_classes": ["legal", "regulatory", "reputational"]},
    {"id": "MF-622", "family": "DA",
     "title": "Customer-facing surfaces carry an accessibility regression gate at WCAG 2.2 Level AA in the release pipeline, and a Level A or AA failure blocks the release rather than being downgraded to a warning",
     "absolute": False,
     "citation": "ADA Title III, 42 U.S.C. §12182 and 28 CFR Part 36; WCAG 2.2 (W3C Recommendation, 5 October 2023), Level AA, cited by identifier; European Accessibility Act, Dir. (EU) 2019/882, applicable from 28 June 2025, whose Annex I covers consumer banking services",
     "source_status": "US statute and regulation public domain; EU text reusable; W3C material cited by identifier only. Note the DOJ web-accessibility rule of 2024 sits at 28 CFR Part 35 and binds Title II public entities only, so a private firm's WCAG 2.2 AA target rests on Title III case law and, in the EU, on the EAA — which is why this is ordinary rather than absolute.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-16"], "harm_classes": ["legal", "reputational"]},
    {"id": "MF-623", "family": "DA",
     "title": "An opt-out preference signal is detected and treated as a valid request to stop sale and sharing without any further prompt, and is linked to the known customer record where one exists",
     "absolute": False,
     "citation": "CCPA/CPRA, Cal. Civ. Code §1798.135(b); California Privacy Protection Agency regulations, 11 CCR §7025 (opt-out preference signals)",
     "source_status": "California statute and regulations are edicts of government. Ordinary and deliberately narrower than MF-404, which states the substantive opt-out duty: this provision governs the automated signal specifically, so a change that ignores the header is charged here rather than competing with MF-404.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-18", "S-17"], "harm_classes": ["legal", "regulatory", "reputational"]},

    # ---- VA: virtual assets and financial-crime programme breadth --------
    {"id": "MF-624", "family": "VA",
     "title": "A transfer involving convertible virtual currency carries the originator and beneficiary records the rule requires, the counterparty wallet provider is identified beforehand, and an unhosted-wallet transfer is recorded with the declared evidence",
     "absolute": True,
     "citation": "31 CFR §1010.410(f) (the Travel Rule) read with §1010.410(e) (recordkeeping) and FinCEN Guidance FIN-2019-G001 treating convertible virtual currency as 'funds'; FATF Recommendation 16",
     "source_status": "US regulation and FinCEN guidance, public domain; FATF material CC BY 4.0. Absolute because the transmittal-of-records duty attaches to the transfer itself with strict liability under 31 U.S.C. §5318(a)(2), and only FinCEN may set the threshold. Note the overlap with MF-524, which states the same duty for funds transfers generally — filed as PA-08 rather than resolved here.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-01"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-625", "family": "VA",
     "title": "Currency transactions above the reporting threshold are aggregated across the business day and reported within the statutory window; no threshold setting, exemption flag or batch schedule suppresses or defers a filing",
     "absolute": True,
     "citation": "31 U.S.C. §5313; 31 CFR §1010.311 (reports of transactions in currency), §1010.306(a)(1) (filing within fifteen days), §1010.313 (aggregation) and §1010.315 (exemptions); structuring prohibited by 31 U.S.C. §5324",
     "source_status": "US statute and regulation, public domain. Absolute because the filing duty and its threshold are set by statute and regulation, the failure to file is itself the offence, and assisting a customer to fall below the threshold is separately criminal under §5324 — none of which any officer of the firm may accept as a residual risk.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-04"], "harm_classes": ["legal", "regulatory", "financial"]},
    {"id": "MF-626", "family": "VA",
     "title": "Information requests from the financial-intelligence unit are matched across every account system and retained, and politically exposed person screening and enhanced due diligence run before a relationship opens and again on the declared refresh cycle",
     "absolute": False,
     "citation": "31 CFR §1010.520 (information sharing between government agencies and financial institutions, the fourteen-day search); §1010.610 (correspondent account due diligence); FFIEC BSA/AML Examination Manual, politically exposed persons and enhanced due diligence sections (title cited as a fact)",
     "source_status": "US regulation, public domain; the FFIEC manual is cited by title with no text reproduced. Ordinary because there is no US rule that defines a politically exposed person or mandates a specific screening design — the expectation is supervisory, so this is a firm control informed by the manual rather than a restatement of a rule.",
     "status": "in_force", "origin": "extension",
     "scenarios": ["S-25", "S-01"], "harm_classes": ["regulatory", "legal", "financial"]},
]

# --------------------------------------------------------------------------
# Scenario coverage for the pack's EXISTING families.
# --------------------------------------------------------------------------

FAMILY_SCENARIOS = {
    "FC": ["S-01", "S-25", "S-04"],
    "PD": ["S-14", "S-02"],
    "SS": ["S-14", "S-13"],
    "SP": ["S-13", "S-15"],
    "CQ": ["S-15", "S-03"],
    "LG": ["S-32", "S-03"],
    "PR": ["S-32"],
    "RE": ["S-36", "S-04", "S-20", "S-13"],
    "DP": ["S-02", "S-18", "S-03"],
    "FL": ["S-06", "S-11", "S-23"],
    "AI": ["S-05", "S-30", "S-23", "S-11"],
    "AG": ["S-12", "S-05"],
    "CP": ["S-10", "S-17", "S-20"],
    "EV": ["S-33", "S-03", "S-32"],
    "GV": ["S-34", "S-11"],
}

# Per-provision overrides where a single existing provision, rather than its
# whole family, is the real hook for a scenario.
PROVISION_SCENARIOS = {
    "MF-101": ["S-01"],
    "MF-102": ["S-04", "S-25"],
    "MF-104": ["S-14"],
    "MF-105": ["S-02"],
    "MF-106": ["S-06"],
    "MF-107": ["S-05"],
    "MF-108": ["S-03", "S-32"],
    "MF-109": ["S-10"],
    "MF-110": ["S-11", "S-06"],
    "MF-111": ["S-12"],
    "MF-203": ["S-04", "S-33"],
    "MF-209": ["S-36"],
    "MF-303": ["S-30", "S-05"],
    "MF-306": ["S-30"],
    "MF-401": ["S-17", "S-10"],
    "MF-404": ["S-18"],
    "MF-503": ["S-04"],
    "MF-506": ["S-32", "S-03"],
    "MF-512": ["S-03"],
    "MF-524": ["S-25", "S-01"],
    "MF-593": ["S-34"],
}

# --------------------------------------------------------------------------
# Draft amendments: findings about EXISTING provisions, filed and not applied.
# The sequence continues after the pack's PA-01 to PA-07.
#
# PA-10 is deliberately numbered: MF-109's source_status already forward-
# references "proposed amendment PA-10", which no amendment in the shipped
# rulebook supplies. The dangling reference is itself one of the findings.
# --------------------------------------------------------------------------

PROPOSED_AMENDMENTS = [
    {
        "id": "PA-08",
        "targets": ["MF-524"],
        "raised_by": "corpus survey 2.0.0 scenario extension (meridian)",
        "finding": (
            "MF-524 states the travel-rule duty on the citation '31 CFR "
            "§1010.410(e)-(f); FATF Recommendation 16'. Two problems. First, the "
            "two subsections are different obligations bundled into one pin: "
            "§1010.410(e) is the Recordkeeping Rule, which requires the "
            "transmittor's institution to obtain and retain records for a "
            "transmittal of funds at or above the threshold, and §1010.410(f) is "
            "the Travel Rule, which requires those records to be forwarded to the "
            "next institution in the chain. A change can breach one and comply "
            "with the other, and as drafted the provision cannot say which. "
            "Second, the provision speaks only of 'a qualifying funds transfer'. "
            "That convertible virtual currency is 'funds' for these purposes rests "
            "on FinCEN Guidance FIN-2019-G001, not on the text of §1010.410, and "
            "the guidance is not cited — so a change that drops originator data "
            "from a virtual-asset transfer is charged, if at all, on an "
            "unstated interpretive step."),
        "proposed": (
            "Split MF-524 into a recordkeeping limb pinned to §1010.410(e) and a "
            "transmittal limb pinned to §1010.410(f), and add FIN-2019-G001 to the "
            "citation so that the virtual-asset reading is on the face of the rule. "
            "The new MF-624 states the virtual-asset duty on its own authority, "
            "which closes the gap by addition; whether MF-524 should also be split "
            "is for the lawmakers."),
        "why_not_applied": (
            "MF-524 is an extension provision, not a shipped one, but A3 draws no "
            "distinction: the corpus author's route to a rule change is a draft "
            "amendment either way. Splitting a provision also changes which "
            "arrivals are charged and under how many counts, which is a "
            "legislative act and not an editorial one."),
        "disposition": "pending",
    },
    {
        "id": "PA-09",
        "targets": ["MF-574"],
        "raised_by": "corpus survey 2.0.0 scenario extension (meridian)",
        "finding": (
            "MF-574 — cancellation at least as easy as sign-up — cites 'Dodd-Frank "
            "§1031 UDAAP; FTC Negative Option Rule, 16 CFR Part 425'. Verified: "
            "the Eighth Circuit vacated the FTC's 2024 Negative Option Rule in its "
            "entirety on 8 July 2025 in Custom Communications, Inc. v. FTC, for a "
            "failure to issue a preliminary regulatory analysis. The provision "
            "therefore names a vacated instrument as one of its two anchors. The "
            "duty itself survives — through ROSCA, 15 U.S.C. §8403, and through "
            "state automatic-renewal statutes — so the consequence is not that the "
            "rule is gone but that the citation invites a contest that it is."),
        "proposed": (
            "Re-anchor MF-574 on ROSCA, 15 U.S.C. §8403, and on the governing "
            "state's automatic-renewal statute read from the jurisdiction table, "
            "retaining the Dodd-Frank §1031 UDAAP limb and deleting the reference "
            "to Part 425. No change to the operative text is needed."),
        "why_not_applied": (
            "Identical in kind to PA-02: a citation is what a later adjudicator "
            "reasons from, and re-anchoring it under a frozen revision moves the "
            "ground beneath every record that interprets the provision as cited."),
        "disposition": "pending",
    },
    {
        "id": "PA-10",
        "targets": ["MF-109"],
        "raised_by": "corpus survey 2.0.0 scenario extension (meridian)",
        "finding": (
            "Two findings, one of them about the rulebook's own bookkeeping. "
            "First, MF-109's source_status reads 'see proposed amendment PA-10' "
            "and no PA-10 exists: the shipped sequence stops at PA-07. A provision "
            "that points at an amendment which is not there is worse than one that "
            "points at nothing, because a reader concludes the finding was "
            "considered and resolved. This amendment takes that id so the "
            "reference resolves. Second, the substantive point the reference "
            "presumably meant: MF-109 makes 'error-resolution clocks' absolute on "
            "the pins '12 CFR §§1005.6, 1005.11'. §1005.11 does contain the "
            "investigation periods, but the ten-business-day provisional-credit "
            "duty that a product decision is most likely to erode sits "
            "specifically at §1005.11(c)(2)(i), and §1005.11(c)(3) provides the "
            "extension to forty-five days that a compliant firm may take. Pinned "
            "at section level, the provision cannot distinguish a lawful extension "
            "from an unlawful one, and because it is absolute the distinction "
            "cannot be made by risk acceptance either."),
        "proposed": (
            "Register this amendment id against MF-109 so the forward reference "
            "resolves, and pin the provision to '12 CFR §§1005.6, 1005.11(b), "
            "1005.11(c)(2)(i) and 1005.11(c)(3)', naming the provisional-credit "
            "duty and its lawful extension on the face of the rule."),
        "why_not_applied": (
            "MF-109 is one of the eleven shipped absolutes; narrowing or "
            "elaborating it changes which arrivals short-circuit under A6. The "
            "extension declined to add a competing provisional-credit provision in "
            "the CN family for the same reason: two provisions stating one duty "
            "would tie on every ordering key, and the honest route is to file the "
            "finding rather than to legislate around it."),
        "disposition": "pending",
    },
    {
        "id": "PA-11",
        "targets": ["MF-303", "MF-569"],
        "raised_by": "corpus survey 2.0.0 scenario extension (meridian)",
        "finding": (
            "MF-303 states two duties in one sentence — tell the customer they are "
            "talking to an AI system, and make generated content machine-markable "
            "— and cites 'EU AI Act Art. 50, applicable from 2 August 2026'. Two "
            "consequences. First, the date phrasing has gone stale: as of this "
            "build the applicability date has passed, so a provision drafted in "
            "the future tense now reads as if the obligation were still ahead. "
            "Second, MF-569 states the marking limb again, on the narrower and "
            "more accurate pin Art. 50(2). The two provisions overlap on their "
            "face: a change that ships unmarked synthetic content is chargeable "
            "under either, and they will tie on every ordering key more often than "
            "the K-tie budget contemplates. The precise scope of the Art. 50 "
            "transparency duties after the AI Omnibus package the pack already "
            "notes at MF-304 is directionally supported, not verified."),
        "proposed": (
            "Split MF-303: keep the Art. 50(1) disclosure duty in MF-303 with the "
            "tense corrected to the present, and let MF-569 carry the Art. 50(2) "
            "marking duty alone, so the distinguishing gate can separate them. "
            "Re-verify both against the AI Omnibus as adopted before the split is "
            "enacted."),
        "why_not_applied": (
            "MF-303 is a shipped provision whose text is reproduced unchanged by "
            "construction, and the pack's whole claim to comparability with the "
            "released cases rests on that. Deciding which of two overlapping "
            "provisions survives is the legislature's, not the editor's."),
        "disposition": "pending",
    },
    {
        "id": "PA-12",
        "targets": ["MF-406", "MF-575"],
        "raised_by": "corpus survey 2.0.0 scenario extension (meridian)",
        "finding": (
            "MF-406 rests on 'CFPB supervisory expectations; UDAAP' with the "
            "source_status conceding it is 'stated as firm policy', and MF-575 "
            "restates the same duty with a window and adds the pin 'Dodd-Frank "
            "§1034(c) 15-day response'. Verified: 12 U.S.C. §5534(c) requires a "
            "timely response to a consumer complaint or inquiry, but it is "
            "addressed to covered persons subject to supervision under §5515 or "
            "§5516 — the larger depositories, their affiliates and the defined "
            "larger participants — not to every covered person. As drafted MF-575 "
            "states a statutory deadline of general application that the statute "
            "does not impose, and the two provisions between them charge one duty "
            "twice, once on policy and once on a pin that may not reach the firm."),
        "proposed": (
            "Qualify MF-575's citation with the §5515/§5516 supervisory scope and "
            "state the fifteen-day window as a firm control where the statute does "
            "not reach, then merge MF-406 into it or mark MF-406 as the "
            "path-existence rule and MF-575 as the timeliness rule so the two "
            "order rather than compete."),
        "why_not_applied": (
            "The same overlap logic as PA-11, with an added reason: MF-406 is "
            "shipped and MF-575 is an extension, so a merge would silently move a "
            "shipped provision's duty into an extension one. Only the legislature "
            "may decide which text survives."),
        "disposition": "pending",
    },
]

# New families whose cases concern a named service, rail or counterparty rather
# than an org-wide posture. DA is org-wide (surfaces and rights operations) and
# CN is programme-wide, so neither is floor-facing.
FLOOR_FACING_FAMILIES = {"PS", "FR", "FP", "MP", "VA"}
