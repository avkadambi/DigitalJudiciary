"""
VetPOC domain change catalogue — scenario extension (corpus 2.0.0).

Narrative colour for the six new families in ext_vocab.py (BN DR CC PS PH AX).
Same contract as changes.py: FAMILY_CONTEXT draws areas/services only from
changes.AREAS / changes.SERVICES; COMPLIANT_CHANGES gives >= 12 titles per
family that engage the family and do nothing wrong, several marked as guard
items (titles that read as violations to a suspicious reviewer but are not);
VIOLATION_CHANGES gives exactly one title per new violate factor. Nothing here
names a provision id, a factor, a regulation, or the words scenario/axiom/
provision/factor/judiciary — these are engineers describing their own work.

Standard library only; this module imports nothing.
"""

# --------------------------------------------------------------------------
# 1. Where each new family's cases live in the org (areas/services drawn only
#    from changes.AREAS / changes.SERVICES).
# --------------------------------------------------------------------------

FAMILY_CONTEXT = {
    "BN": {
        "areas": ["platform", "records", "org", "comms"],
        "services": [
            "audit-ledger",
            "records-export-service",
            "notification-pipeline",
            "identity-service",
            "retention-scheduler",
        ],
    },
    "DR": {
        "areas": ["rx", "dispensing", "records"],
        "services": [
            "dispensing-service",
            "prescription-workflow",
            "epcs-signing-service",
            "controlled-inventory-ledger",
            "analytics-warehouse",
        ],
    },
    "CC": {
        "areas": ["comms", "portal", "billing", "records"],
        "services": [
            "reminder-engine",
            "notification-pipeline",
            "consent-service",
            "client-portal-api",
            "records-export-service",
            "invoicing-pipeline",
        ],
    },
    "PS": {
        "areas": ["triage", "alerting", "emr", "dispensing"],
        "services": [
            "triage-assistant",
            "dispensing-service",
            "emr-notes-service",
            "notification-pipeline",
            "patient-record-store",
        ],
    },
    "PH": {
        "areas": ["emr", "records", "boarding", "org"],
        "services": [
            "emr-notes-service",
            "patient-record-store",
            "notification-pipeline",
            "rbac-service",
            "client-portal-api",
        ],
    },
    "AX": {
        "areas": ["portal", "platform"],
        "services": [
            "client-portal-api",
            "mobile-checkin-app",
            "ci-pipeline",
            "consent-service",
        ],
    },
}


# --------------------------------------------------------------------------
# 2. Compliant / neutral change titles, per family. Each engages the family's
#    subject matter and does nothing wrong. Guard items are marked inline:
#    they read as violations to a suspicious reviewer but are correct changes.
# --------------------------------------------------------------------------

COMPLIANT_CHANGES = {
    "BN": [
        "Add a jurisdiction lookup table that sources the breach-notice clock from statute text",
        "Reject configuration changes that would extend the breach-notice clock",  # guard
        "Wire the bulk owner-data export anomaly detector to the on-call paging rotation",
        "Link the incident runbook from every breach-detection alert payload",
        "Add a breach-notice clause to the standard vendor contract template",
        "Route vendor incident webhooks into the monitored incident queue",
        "Extend access-log retention to cover the full notification lookback window",
        "Compute breach scope from the complete access log instead of a sample",
        "Add the statutory content checklist to the owner breach-notice template",
        "Record delivery confirmation before marking a breach notice as sent",
        "Version the regulator notice template in the policy repo",
        "Remove the discontinued pilot's breach-clock override flag from the config schema",  # guard
        "Enable the portal's credential-stuffing detector on client login",
        "Shorten the vendor breach-notice SLA from five business days to two",  # guard
        "Record a named owner and outcome on every breach-drill result",
    ],
    "DR": [
        "Add a same-day alert when a controlled-substance loss crosses the significant-loss criteria",
        "Wire Form 106 filing into the CI-gated compliance job so it can't be skipped",
        "Route every Schedule II reorder through the CSOS certificate signer",
        "Extend order-form record retention to cover the full two-year floor",
        "Schedule the biennial inventory job with an alert if it does not complete on time",
        "Require an exact physical count entry before the inventory record can be signed",
        "Run diversion analytics over every dispensing event across all practices",  # guard: sounds like a scale change, is actually restoring universal coverage
        "Route anomalous dispensing alerts to the medical director's paging channel",
        "Require the individual CSOS certificate on every Schedule II order signature",
        "Make the loss-discovery timestamp immutable once the theft report is filed",
        "Match every Form 222 line item against the receiving record before closing the order",
        "Block inventory record submission until a named licensee has signed it",
        "Freeze the significant-loss threshold at the DEA's own criteria rather than a local override",  # guard
        "Add a nightly job that reconciles CSOS certificate expiry against active signers",
    ],
    "CC": [
        "Record prior express consent with timestamp and source before an automated text campaign",
        "Gate the reactivation text campaign behind the same consent check as ordinary reminders",
        "Uncheck the wellness-plan auto-renewal box by default at enrolment",
        "Give wellness-plan cancellation the same number of steps as enrolment",
        "Capture e-signature consent before switching a client to electronic invoices",
        "Require a fresh e-signature consent action rather than inferring it from login",
        "Restore the written-prescription button to the dispensing screen after a UI redesign",  # guard
        "Waive the records-copy fee for a client's own written prescription request",
        "Route records-release requests around the monthly billing queue to meet the state deadline",
        "Release medical records regardless of outstanding balance",
        "Require a verified adult guardian before a minor's client account can be created",
        "Block payment-plan enrolment from an account without verified adult status",
        "Suppress reminder sends to any number that has already replied STOP",  # guard
        "Restore the pre-charge renewal reminder that a billing rewrite had dropped",  # guard
        "Cap the records-copy fee at the state's statutory maximum",
    ],
    "PS": [
        "Block dose calculation until a current weight is recorded for the visit",
        "Hard-stop the dose calculator on a declared weight-unit mismatch",
        "Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply",
        "Route every red-flag triage conversation to an on-duty licensed technician",
        "Escalate an unacknowledged critical-value alert to a second on-call contact",
        "Replace the passive critical-value badge with a required acknowledgement dialog",  # guard: name suggests replacing a stronger control, actually strengthens it
        "Require a saved consent record before the euthanasia workflow can proceed",
        "Require a tag scan at every remains custody transfer",
        "Remove the species dose-range override button that predates the current safety gate",  # guard
        "Show the automated-triage disclosure on every turn of the conversation",
        "Require a named response before a critical-value alert can be marked acknowledged",
        "Require an explicit owner choice before remains disposition can be saved",
        "Add regression tests covering the unit-conversion boundaries in the dose calculator",
        "Attach the full triage transcript to the patient's medical record",
    ],
    "PH": [
        "Remove the per-practice toggle that could gate reportable-disease submissions",  # guard
        "Restore the full reportable-condition list after a fixture refresh had trimmed it",  # guard
        "Require a currently licensed veterinarian's credential to sign a rabies certificate",
        "Verify the signer's licence status before a rabies certificate can be issued",
        "Add the suspected-abuse report option back to the chart action menu",
        "Restrict the suspected-abuse report entry to authorised staff roles only",
        "Validate microchip numbers against the ISO 11784 format at intake",
        "Surface an alert when a microchip registry submission fails instead of dropping it",
        "Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch",
        "Block certificate issuance when the signing veterinarian's licence has lapsed",
        "Require staff-verified ownership before a microchip's registered owner can change",
        "Show the zoonotic-exposure flag to boarding staff on the patient banner",
        "Confirm every disease-report dispatch with the receiving official's acknowledgement",
        "Record the rabies vaccine lot and expiry alongside the issued certificate",
    ],
    "AX": [
        "Add an accessibility regression gate to the portal release pipeline",
        "Fail the portal build on any WCAG 2.2 AA violation instead of just warning",
        "Make the consent signature pad completable by keyboard alone",
        "Let the client extend the mobile check-in session before it times out",
        "Pair the required-field error with visible text, not colour alone",
        "Add a keyboard path out of the consent modal's focus trap",
        "Add an accessible name to the new custom toggle control",
        "Offer a non-visual alternative alongside the check-in captcha",
        "Record a manual screen-reader check for every new portal flow",
        "Add captions to the discharge-instructions video on the portal",
        "Verify focus order on the consent dialog before each release",
        "Enforce a minimum touch-target size on the mobile check-in buttons",
        "Version the accessibility statement alongside the portal release notes",
        "Announce form validation errors to assistive technology on submit",
    ],
}


# --------------------------------------------------------------------------
# 3. One title per new violating factor.
# --------------------------------------------------------------------------

VIOLATION_CHANGES = {
    # ---- BN -----------------------------------------------------------
    "breach_notification_deadline_exposed_as_tenant_setting":
        "Add a per-tenant slider for the breach-notification deadline",
    "notification_clock_started_at_confirmation_not_discovery":
        "Start the breach-notice timer at confirmed root cause instead of first detection",
    "bulk_export_anomaly_alert_disabled_to_cut_noise":
        "Mute the bulk owner-data export alert to quiet the on-call pager",
    "incident_runbook_reference_removed_from_alert_payload":
        "Drop the runbook link from the detection alert payload to shorten it",
    "vendor_contract_template_drops_breach_notice_clause":
        "Remove the breach-notice clause from the standard vendor contract template",
    "vendor_incident_notices_routed_to_unmonitored_mailbox":
        "Point vendor incident notifications at a shared inbox nobody monitors",
    "access_log_retention_shorter_than_notification_lookback":
        "Cut access-log retention to thirty days to save storage costs",
    "breach_scope_computed_from_sampled_logs_only":
        "Estimate breach scope from a ten-percent log sample to finish the report faster",
    "owner_notice_omits_statutory_content_elements":
        "Trim the owner breach-notice template down to a one-line summary",
    "notification_dispatch_marked_sent_without_delivery_evidence":
        "Mark breach notices sent as soon as the job enqueues them",

    # ---- DR -----------------------------------------------------------
    "theft_or_loss_report_suppressed_below_configured_threshold":
        "Suppress the theft-and-loss alert when the missing count is under a configurable threshold",
    "form_106_filing_left_as_manual_optional_step":
        "Make Form 106 filing a manual checklist item instead of an automatic submission",
    "schedule_ii_order_submitted_outside_csos_or_form_222":
        "Let Schedule II reorders go through the general purchasing API instead of CSOS",
    "order_form_records_purged_before_two_years":
        "Purge Form 222 order records after one year to shrink the archive",
    "biennial_inventory_job_disabled_or_skipped":
        "Disable the biennial inventory job during the systems migration",
    "inventory_count_auto_filled_from_ledger_balance":
        "Auto-fill the physical inventory count from the running ledger balance",
    "diversion_analytics_disabled_for_named_practice":
        "Turn off diversion analytics for the pilot practice to cut false positives",
    "anomalous_dispensing_alerts_routed_to_null_sink":
        "Route anomalous dispensing alerts to a queue with no configured recipient",
    "csos_signature_replaced_by_shared_practice_credential":
        "Sign CSOS orders with a shared practice login instead of the individual certificate",
    "loss_discovery_timestamp_editable_after_the_fact":
        "Allow staff to edit the recorded loss-discovery timestamp after filing",
    "order_form_line_items_accepted_without_receipt_match":
        "Accept Form 222 line items without matching them against the receiving record",
    "inventory_record_unsigned_by_any_licensee":
        "Let the inventory count save without a licensee signature field",

    # ---- CC -----------------------------------------------------------
    "automated_text_sent_without_recorded_prior_consent":
        "Send automated appointment texts to numbers with no recorded consent on file",
    "consent_check_bypassed_for_reactivation_campaign":
        "Skip the consent check for the lapsed-client reactivation text campaign",
    "auto_renewal_enrolled_by_prechecked_box":
        "Pre-check the wellness-plan auto-renewal box at checkout",
    "cancellation_requires_phone_call_while_signup_is_online":
        "Require a phone call to cancel the wellness plan clients enrolled in online",
    "electronic_records_delivered_without_esign_consent":
        "Switch invoice delivery to email before capturing e-signature consent",
    "esign_consent_inferred_from_portal_login":
        "Treat a portal login as e-signature consent for electronic records",
    "written_prescription_option_hidden_from_client":
        "Remove the written-prescription button from the dispensing screen",
    "prescription_copy_conditioned_on_in_house_purchase":
        "Charge a release fee for a written prescription unless the client buys in-house",
    "records_release_delayed_beyond_state_deadline":
        "Queue records-release requests behind the monthly billing run",
    "records_release_blocked_until_balance_paid":
        "Hold medical-record releases until the client's balance is paid",
    "minor_account_created_without_guardian_consent":
        "Let the signup form create a client account without checking the applicant's age",
    "payment_plan_signed_by_under_eighteen_account":
        "Allow payment-plan enrolment from an unverified under-eighteen account",
    "stop_reply_ignored_by_reminder_engine":
        "Keep sending reminder texts to numbers that already replied STOP",
    "renewal_reminder_removed_before_annual_charge":
        "Remove the pre-charge renewal reminder to simplify the billing job",
    "marketing_texts_scheduled_outside_permitted_hours":
        "Schedule marketing texts for six in the morning to beat inbox competition",
    "records_release_charged_above_statutory_copy_fee":
        "Raise the records-copy fee above the state's statutory cap",

    # ---- PS -----------------------------------------------------------
    "dose_computed_from_stale_or_absent_weight":
        "Let the dose calculator run on last year's recorded weight when today's is missing",
    "weight_unit_mismatch_downgraded_to_dismissable_warning":
        "Turn the pound-kilogram mismatch error into a dismissable warning",
    "triage_assistant_presents_as_licensed_veterinarian":
        "Let the triage chatbot introduce itself as Dr. Assistant",
    "triage_assistant_issues_treatment_without_handoff":
        "Let the triage assistant recommend a treatment plan without escalating to staff",
    "critical_value_alert_suppressed_by_quiet_hours_setting":
        "Suppress critical-value alerts during the clinic's configured quiet hours",
    "critical_value_alert_downgraded_to_passive_notification":
        "Replace the critical-value acknowledgement page with a passive dashboard badge",
    "euthanasia_performed_without_recorded_owner_consent":
        "Let staff proceed with euthanasia before the consent form is saved",
    "remains_custody_transfer_recorded_without_tag_scan":
        "Let staff log a remains custody transfer without scanning the tag",
    "dose_range_hard_stop_replaced_by_override_button":
        "Replace the species dose-range hard stop with an override button",
    "triage_assistant_disclosure_shown_once_per_session_only":
        "Show the automated-triage disclosure only on the first message of a session",
    "alert_acknowledgement_auto_completed_by_timer":
        "Auto-acknowledge critical-value alerts if no one responds within five minutes",
    "remains_disposition_defaulted_without_owner_choice":
        "Default remains disposition to cremation when the owner form field is blank",

    # ---- PH -----------------------------------------------------------
    "reportable_disease_report_gated_behind_practice_toggle":
        "Gate reportable-disease submissions behind a per-practice enable toggle",
    "reportable_condition_list_pruned_to_reduce_alerts":
        "Trim the reportable-condition list to cut down on staff alert fatigue",
    "rabies_certificate_issued_under_technician_signature":
        "Let a technician account sign the rabies certificate when the vet is busy",
    "rabies_certificate_signature_auto_applied_from_template":
        "Auto-stamp the veterinarian's signature onto the rabies certificate template",
    "suspected_abuse_report_option_removed_from_chart":
        "Remove the suspected-abuse report option from the chart menu",
    "abuse_report_visible_to_client_on_portal":
        "Surface the suspected-abuse report entry on the client-facing portal timeline",
    "microchip_number_accepted_without_format_validation":
        "Accept any microchip number the intake form receives without a format check",
    "microchip_registry_submission_failures_silently_dropped":
        "Drop failed microchip registry submissions without surfacing an error",
    "report_dispatch_batched_past_statutory_window":
        "Batch reportable-disease dispatches into a weekly job to cut API calls",
    "rabies_certificate_issuable_with_expired_licence":
        "Allow certificate issuance to proceed without checking the signer's licence expiry",
    "microchip_owner_reassigned_from_client_self_service":
        "Let clients reassign a microchip's registered owner from the self-service portal",
    "zoonotic_flag_hidden_from_boarding_staff":
        "Hide the zoonotic-exposure flag from the boarding staff view",

    # ---- AX -----------------------------------------------------------
    "accessibility_gate_removed_from_portal_pipeline":
        "Remove the accessibility regression gate from the portal release pipeline",
    "wcag_failures_downgraded_to_warnings_in_ci":
        "Downgrade WCAG failures to warnings so the portal build stays green",
    "consent_signature_requires_mouse_drag_only":
        "Rebuild the consent signature pad as a mouse-only drag gesture",
    "checkin_session_expires_with_no_extension":
        "Remove the extend-session option from the mobile check-in timeout",
    "required_field_error_shown_by_colour_only":
        "Mark required check-in fields with a red border and no error text",
    "focus_trapped_in_consent_modal":
        "Ship the consent modal without a keyboard path out of it",
    "custom_control_shipped_without_accessible_name":
        "Ship the new custom toggle control without an accessible name attribute",
    "checkin_captcha_lacks_non_visual_alternative":
        "Add an image-only captcha to the mobile check-in form",
}
