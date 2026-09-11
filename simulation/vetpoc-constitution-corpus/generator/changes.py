"""
VetPOC domain change catalogue.

The corpus generator draws a provision family first and narrative colour second.
Until now the two were drawn independently, so a case could engage a
sanctions-style provision while describing a change to the customer portal. This
module supplies the missing join: for every provision family it names the parts
of the VetPOC org where that family's cases actually arise, and it supplies pull
request titles that a VetPOC engineer would plausibly write for a change that
engages those provisions — one set that engages the family and does nothing
wrong, and one title per violating factor that produces exactly that factor.

Nothing here mentions provision ids, factor names or the adjudicator. These are
engineers describing their own work.

Standard library only; this module imports nothing and must stay importable on
its own so the generator can consume it before the constitution is built.

----------------------------------------------------------------------------
NOTE ON AREAS AND SERVICES
----------------------------------------------------------------------------
`vocab.py` does not (yet) define AREAS or SERVICES. The two vocabularies below
are therefore defined here so this module is self-contained and importable.

AREAS reproduces, verbatim and in full, the `domain` vocabulary of the shipped
144-case VetPOC pack (demo/companies/vetpoc/cases.json), which is the corpus's
own authoritative naming for parts of the org.

SERVICES is a new vocabulary, named from the systems those shipped cases and
the constitution actually describe.

Both lists are intended to be lifted into vocab.py as `vocab.AREAS` and
`vocab.SERVICES` unchanged; FAMILY_CONTEXT below draws only from them.
"""

# --------------------------------------------------------------------------
# Vocabularies (see note above)
# --------------------------------------------------------------------------

AREAS = [
    "platform",
    "emr",
    "portal",
    "billing",
    "labs",
    "scheduling",
    "rx",
    "analytics",
    "org",
    "records",
    "insurance",
    "comms",
    "boarding",
    "staffing",
    "triage",
    "alerting",
    "dispensing",
]

SERVICES = [
    # controlled substances and prescribing
    "dispensing-service",
    "prescription-workflow",
    "epcs-signing-service",
    "pdmp-submitter",
    "controlled-inventory-ledger",
    "vfd-service",
    # clinical record
    "patient-record-store",
    "emr-notes-service",
    # diagnostics and devices
    "hl7-ingest",
    "dicom-router",
    "device-gateway",
    "lab-results-formatter",
    "results-reconciler",
    # money
    "billing-ledger",
    "payment-tokenizer",
    "invoicing-pipeline",
    "claims-connector",
    # client-facing surfaces
    "practice-api-gateway",
    "client-portal-api",
    "mobile-checkin-app",
    # identity and tenancy
    "identity-service",
    "rbac-service",
    "tenant-router",
    # records, audit and privacy
    "audit-ledger",
    "records-export-service",
    "retention-scheduler",
    "consent-service",
    # messaging
    "reminder-engine",
    "notification-pipeline",
    # operations
    "scheduling-engine",
    "boarding-scheduler",
    "triage-assistant",
    "analytics-warehouse",
    "welfare-inspection-tracker",
    # build and governance plane
    "ci-pipeline",
    "artifact-registry",
    "policy-repo",
    "agent-runner",
    "feature-flag-service",
    "adjudication-gateway",
]


# --------------------------------------------------------------------------
# 1. Where each provision family's cases live in the org.
# --------------------------------------------------------------------------

FAMILY_CONTEXT = {
    "CS": {
        "areas": ["rx", "dispensing", "records", "platform"],
        "services": [
            "dispensing-service",
            "prescription-workflow",
            "epcs-signing-service",
            "pdmp-submitter",
            "controlled-inventory-ledger",
            "identity-service",
        ],
    },
    "VC": {
        "areas": ["rx", "emr", "dispensing", "records"],
        "services": [
            "prescription-workflow",
            "emr-notes-service",
            "vfd-service",
            "dispensing-service",
            "patient-record-store",
        ],
    },
    "PO": {
        "areas": ["labs", "emr", "platform", "alerting"],
        "services": [
            "hl7-ingest",
            "dicom-router",
            "device-gateway",
            "lab-results-formatter",
            "results-reconciler",
            "notification-pipeline",
        ],
    },
    "PD": {
        "areas": ["billing", "portal", "comms", "analytics", "records"],
        "services": [
            "payment-tokenizer",
            "billing-ledger",
            "client-portal-api",
            "consent-service",
            "records-export-service",
            "reminder-engine",
        ],
    },
    "RB": {
        "areas": ["platform", "emr", "portal", "org", "staffing"],
        "services": [
            "rbac-service",
            "identity-service",
            "tenant-router",
            "practice-api-gateway",
            "client-portal-api",
        ],
    },
    "SC": {
        "areas": ["platform", "org", "labs"],
        "services": [
            "ci-pipeline",
            "artifact-registry",
            "practice-api-gateway",
            "hl7-ingest",
            "client-portal-api",
        ],
    },
    "AI": {
        "areas": ["platform", "emr", "rx", "org"],
        "services": [
            "agent-runner",
            "ci-pipeline",
            "rbac-service",
            "dispensing-service",
            "identity-service",
            "prescription-workflow",
        ],
    },
    "AS": {
        "areas": ["portal", "emr", "platform", "billing"],
        "services": [
            "client-portal-api",
            "practice-api-gateway",
            "emr-notes-service",
            "mobile-checkin-app",
            "invoicing-pipeline",
        ],
    },
    "HA": {
        "areas": ["platform", "emr", "scheduling", "triage", "labs"],
        "services": [
            "emr-notes-service",
            "controlled-inventory-ledger",
            "scheduling-engine",
            "practice-api-gateway",
            "results-reconciler",
            "feature-flag-service",
        ],
    },
    "RR": {
        "areas": ["records", "platform", "org", "billing"],
        "services": [
            "audit-ledger",
            "records-export-service",
            "retention-scheduler",
            "patient-record-store",
            "emr-notes-service",
        ],
    },
    "AW": {
        "areas": ["emr", "staffing", "boarding", "records"],
        "services": [
            "emr-notes-service",
            "patient-record-store",
            "welfare-inspection-tracker",
            "boarding-scheduler",
            "rbac-service",
        ],
    },
    "GV": {
        "areas": ["org", "platform", "records", "portal"],
        "services": [
            "adjudication-gateway",
            "policy-repo",
            "audit-ledger",
            "records-export-service",
            "client-portal-api",
        ],
    },
}


# --------------------------------------------------------------------------
# 2. Compliant / neutral change titles, per family.
#    Each engages the family's subject matter and does nothing wrong.
# --------------------------------------------------------------------------

COMPLIANT_CHANGES = {
    "CS": [
        "Add unit tests for the ASAP 4.2B species-code field mapper",
        "Pin the schedule II refill count to zero in the prescription builder",
        "Backfill prescriber DEA expiry dates onto the credential record",
        "Record the witnessing licensee on every euthanasia-solution dispense",
        "Surface the biennial inventory due date on the dispensing dashboard",
        "Reconcile ketamine vial volumes to the millilitre in the nightly job",
        "Require both administrators to confirm an EPCS signing-privilege grant",
        "Show the six-month validity window on the refill request screen",
        "Route diversion alerts to the medical director's queue within the hour",
        "Log the authenticated prescriber id on each dispensing event",
        "Retry failed PDMP submissions and alert when no acknowledgement arrives",
        "Validate the PDMP payload against the state schema before submit",
        "Block record purges that fall inside the two-year retention term",
        "Capture the medical-purpose note as a required field on Schedule II orders",
    ],
    "VC": [
        "Require a recorded in-person exam date before extralabel orders",
        "Calculate the extended withdrawal interval when the order is saved",
        "Flag food-animal status on the patient banner before dispensing",
        "Make the feed directive expiry date a mandatory field",
        "Attach the clinical-necessity note to bulk compounding orders",
        "Warn when a dose falls outside the labelled species range",
        "Check the jurisdiction table before honouring a telehealth-established VCPR",
        "Prompt for an off-label rationale in the medical record",
        "Record owner counselling on withdrawal periods in the discharge summary",
        "Restrict extralabel ordering to licensed veterinarian accounts",
        "Attach a residue risk assessment to the food-animal order form",
        "Show the premises visit date on the large-animal chart header",
        "Validate species and body weight before computing the dosage",
        "Import the prohibited extralabel substance list from a versioned fixture",
    ],
    "PO": [
        "Bound HL7 segment length before the ORU^R01 parser runs",
        "Reject malformed segments without committing a partial patient write",
        "Match study patient identity on microchip and account number",
        "Populate DICOM species and breed tags from the patient record",
        "Map Catalyst One chemistry results to LOINC codes at ingest",
        "Wrap result-to-patient binding in a single database transaction",
        "Cap analyzer retries at five with exponential backoff",
        "Move the ProCyte Dx onto the isolated device VLAN",
        "Quarantine unmatched analyzer results for technician review",
        "Require acknowledgement before a critical value page clears",
        "Scope modality worklist queries to the requesting practice",
        "Pin the radiography panel firmware version in the device inventory",
        "Add a weekly check over the orphaned-study reconciliation job output",
        "Add contract tests for the pinned HL7 v2 profile",
    ],
    "PD": [
        "Tokenise the card number before the invoice row is written",
        "Hand the checkout redirect to the validated payment processor",
        "Extend the log redaction filter to the new owner phone field",
        "Encrypt the owner address column at rest in the portal store",
        "Check consent currency before the reminder engine sends",
        "Give consent withdrawal the same one-click path as granting it",
        "Honour opt-out state at export time in the marketing job",
        "Bound the data subject export job to the statutory window",
        "Apply the state retention schedule to inactive owner records",
        "Record the lawful basis for the EU-to-US analytics transfer",
        "Link the breach notification runbook from the incident template",
        "Run the DLP scan over changed lines in the billing pipeline",
        "Redact owner email addresses from claims connector debug output",
        "Store payment references, not card numbers, on the retry queue",
    ],
    "RB": [
        "Enforce the tenant scope in the query layer, not the handler",
        "Check object ownership before returning a patient chart",
        "Add permutation tests across the role-permission matrix",
        "Scope the new reporting role to read-only endpoints",
        "Time-box break-glass access to four hours and log the grant",
        "Deny clinical note writes to the receptionist role",
        "Withhold prescription finalisation from technician accounts",
        "Require an explicit share grant for cross-practice referrals",
        "Revalidate the active session after a privilege change",
        "Bind each service account to a single practice id",
        "Require a second approver on admin role assignments",
        "Derive tenant id from the session, never from a request header",
        "Cover the new boarding endpoint with a role check test",
        "Move the authorisation decision out of the portal frontend",
    ],
    "SC": [
        "Verify commit signatures on the protected release branch",
        "Attach build provenance to the practice API release artefact",
        "Pin the build runner image and make each job ephemeral",
        "Point the resolver at the private registry before the public one",
        "Publish a CycloneDX SBOM alongside each release digest",
        "Fail the build when the scanner reports anything above CVSS seven",
        "Add the new charting library licence to the allowlist",
        "Update the manifest and lockfile in the same commit",
        "Record artefact digests in the release ledger on publish",
        "Assign a named reviewer to the vendored DICOM parser",
        "Run the secret scanner over the diff in pre-merge CI",
        "Bump the HL7 parser to the patched upstream release",
        "Replace the unmaintained transitive dependency with a vetted fork",
        "Gate merges on a clean provenance verification step",
    ],
    "AI": [
        "Require a named human reviewer on every agent-authored pull request",
        "Run agent-generated code inside the sandboxed runner only",
        "Restrict agent outbound calls to the allowlisted host set",
        "Split the agent-refactored invoicing function to cut its branching",
        "Run semantic analysis over the agent diff in CI",
        "Record the prompt and context hash on the agent's pull request",
        "Review agent-authored tests for tautological assertions",
        "Verify every imported package resolves in the registry before merge",
        "Keep the agent's scope off authorisation and dispensing paths",
        "Capture the veterinarian's sign-off on clinical logic changes",
        "Strip untrusted ticket text from the agent's instruction context",
        "Publish the agent runner's host allowlist as reviewed configuration",
        "Block agent branches from touching the compliance test suite",
        "Label agent-authored commits so review routing can see them",
    ],
    "AS": [
        "Parameterise the new chart-search query",
        "Encode clinical note text before rendering it in the portal",
        "Tighten the portal CSP by dropping the inline script allowance",
        "Constrain pet-photo uploads by type, size and resolved path",
        "Allowlist microchip identifier formats at the API boundary",
        "Enforce authorisation server-side on the discharge summary route",
        "Restrict claim payload deserialisation to known types",
        "Return a correlation id instead of a stack trace on error",
        "Replace the hand-rolled token hash with the vetted library",
        "Validate webhook destinations against the outbound allowlist",
        "Remove the ORM raw-SQL escape hatch from the billing report",
        "Sanitise filenames in the lab attachment upload handler",
        "Add regression tests for the note-render encoding path",
        "Drop internal identifiers from the public error envelope",
    ],
    "HA": [
        "Check the version token on clinical note writes",
        "Make the note autosave idempotent under client retry",
        "Serialise inventory decrements with a row-level lock",
        "Load test the triage queue at a hundred concurrent clinicians",
        "Move the release outside the emergency-hours freeze window",
        "Document the degraded path when the reference lab is down",
        "Ship a down-migration for the visit-summary table change",
        "Configure a circuit breaker around the external lab client",
        "Bound the results reconciler retry loop",
        "Show a merge dialog instead of overwriting a colleague's note",
        "Prove the backup restore before the vaccine index migration",
        "Queue reminder sends so a retry storm cannot amplify",
        "Add a concurrency test for simultaneous discharge summary saves",
        "Stagger analyzer polling to flatten the morning load peak",
    ],
    "RR": [
        "Make the audit table append-only at the database level",
        "Preserve the original entry when a chart amendment is filed",
        "Assign the daily audit review to the practice manager role",
        "Attach the standing declaration to every audit export",
        "Write the decision rationale at resolution time, not on export",
        "Configure retention periods per jurisdiction in the scheduler",
        "Take record timestamps from the monotonic server clock",
        "Verify the hash chain when an audit bundle is exported",
        "Publish the contest counts in the audit export header",
        "Keep the retention clock unchanged when a record is edited",
        "Add an immutability test for the dispensing log writer",
        "Version chart amendments instead of editing rows in place",
        "Record who exported an audit bundle and when",
        "Store the amendment author alongside the superseded text",
    ],
    "AW": [
        "Require the veterinary care plan on the regulated facility record",
        "Block procedure sign-off by roles outside the delegated scope",
        "Make anaesthesia monitoring intervals mandatory on the record",
        "Prompt for a pain management plan at surgical discharge",
        "Capture the research protocol number on regulated-facility visits",
        "Add the transport welfare checklist to the boarding intake form",
        "Match the required supervision level to the task's risk tier",
        "Warn when an anaesthesia monitoring gap exceeds the protocol",
        "Track welfare inspection findings to a remediation due date",
        "Record the analgesia rationale when a plan is declined",
        "Show the technician's credential status on the surgery board",
        "Attach the anaesthesia record to the procedure summary",
        "Add a job that escalates overdue welfare remediations to the medical director",
        "Validate delegated task lists against the state practice act table",
    ],
    "GV": [
        "Keep the contest link visible on every automated decision notice",
        "Route a human review request from the decision detail page",
        "Attribute the standing declaration to the enacting authority",
        "Publish the contest outcome as granted and refused counts",
        "Record a disposition for every referral acknowledgement",
        "Keep reporter bulletins out of the adjudicator's context builder",
        "Separate the audit register store from the precedent store",
        "Move threshold parameters into the legislated configuration",
        "Write a docket entry for every uncharged arrival",
        "Expose the contest path to the owner, not only to staff",
        "Add tests proving retrieval never reads the audit register",
        "Log the acknowledgement disposition on the referral timeline",
        "Show which record controlled on the decision page",
        "Make the human review queue reachable from the portal",
    ],
}


# --------------------------------------------------------------------------
# 3. One title per violating factor. The change described is the change that
#    produces that factor; the factor itself is never named.
# --------------------------------------------------------------------------

VIOLATION_CHANGES = {
    # ---- CS ---------------------------------------------------------------
    "epcs_signature_completed_with_single_factor":
        "Let the password alone sign an e-prescription when the token times out",
    "schedule_ii_prescription_carries_refills":
        "Enable the refill button on hydromorphone prescriptions",
    "refill_count_exceeds_five_for_schedule_iii_iv":
        "Raise the tramadol refill cap to twelve for chronic pain clients",
    "prescription_reissued_beyond_six_month_window":
        "Let clients re-order from prescriptions written last year",
    "controlled_inventory_discrepancy_unexplained":
        "Auto-close ketamine count mismatches under two millilitres",
    "dea_registration_expired_at_time_of_issue":
        "Skip the DEA registration lookup when a relief vet is on shift",
    "asap_payload_omits_species_code":
        "Drop the species field from the PDMP payload to clear schema errors",
    "pdmp_submission_silently_dropped_on_error":
        "Swallow PDMP submission errors so checkout never blocks",
    "euthanasia_solution_dispensed_without_witness":
        "Make the second-licensee witness field optional on euthanasia logs",
    "prescriber_identity_inferred_not_authenticated":
        "Infer the prescriber from the last clinician to open the chart",
    "signing_credential_granted_by_single_administrator":
        "Let one admin grant EPCS signing rights from the user screen",
    "controlled_substance_record_deleted_before_retention_expiry":
        "Purge dispensing rows older than ninety days to shrink the table",
    "prescription_lacks_legitimate_medical_purpose":
        "Let staff issue standing scripts without opening the patient record",
    "dispensing_logic_bypassed_by_feature_flag":
        "Add a flag that skips the dispensing checks during demos",

    # ---- VC ---------------------------------------------------------------
    "extralabel_use_without_valid_vcpr":
        "Allow extralabel orders for clients with no recorded exam",
    "prohibited_eldu_substance_in_food_animal":
        "Unblock enrofloxacin ordering for dairy herds",
    "withdrawal_interval_absent_for_food_animal":
        "Make the withdrawal interval optional on food-animal orders",
    "eldu_ordered_by_unlicensed_staff_member":
        "Let assistants submit extralabel orders on the vet's behalf",
    "compounding_from_bulk_without_necessity_record":
        "Remove the necessity note from the bulk compounding form",
    "vfd_expiry_date_missing":
        "Default the feed directive expiry to blank when it is unknown",
    "dose_exceeds_species_maximum_by_more_than_20_percent":
        "Let the calculator accept twice the labelled equine maximum",
    "telehealth_only_vcpr_where_jurisdiction_requires_in_person":
        "Enable video-only exams for prescribing in every state",
    "violative_residue_risk_accepted_without_assessment":
        "Ship beef-herd orders without the residue assessment step",

    # ---- PO ---------------------------------------------------------------
    "hl7_parser_accepts_unbounded_segment_length":
        "Remove the segment length cap so long comment fields parse",
    "malformed_hl7_message_causes_partial_patient_write":
        "Commit parsed HL7 segments as they arrive instead of at the end",
    "diagnostic_result_attached_to_wrong_patient_id":
        "Match analyzer results on patient name alone",
    "result_patient_binding_performed_outside_transaction":
        "Write the result row first and link the patient in a follow-up job",
    "dicom_tag_trusted_without_validation":
        "Trust the modality's patient identifier tag exactly as sent",
    "device_retry_loop_has_no_ceiling":
        "Retry the blood gas analyzer until it answers",
    "poc_device_reachable_from_public_network_segment":
        "Expose the radiography panel to the internet for vendor support",
    "critical_result_delivered_only_by_email":
        "Replace the critical value page with a nightly email digest",
    "analyzer_result_discarded_on_parse_error_without_alert":
        "Drop analyzer messages that fail to parse and move on",
    "patient_identity_reassigned_without_reverification":
        "Let staff reassign a study to another patient in one click",

    # ---- PD ---------------------------------------------------------------
    "primary_account_number_written_to_application_log":
        "Log the full card number on payment retry to debug declines",
    "owner_government_identifier_captured_in_free_text":
        "Add a free-text field for the owner's social security number",
    "consent_withdrawal_requires_phone_call_only":
        "Remove the unsubscribe link and point owners at the clinic phone line",
    "marketing_export_includes_opted_out_owners":
        "Add a campaign endpoint that exports the whole owner list",
    "owner_pii_transferred_without_lawful_basis":
        "Replicate the Dublin clinic's owner tables to the US warehouse",
    "debug_endpoint_returns_unredacted_owner_record":
        "Add a support endpoint that dumps the full owner record",
    "payment_card_stored_in_plaintext_column":
        "Keep the card number in the retry queue until settlement clears",
    "data_subject_request_queue_unbounded":
        "Remove the deadline timer from the data export request queue",
    "consent_currency_not_checked_before_use":
        "Reuse the stored consent flag without rechecking its date",

    # ---- RB ---------------------------------------------------------------
    "patient_id_parameter_trusted_from_client":
        "Load the chart straight from the patient id in the query string",
    "cross_tenant_record_returned_by_endpoint":
        "Drop the practice filter from the referral search endpoint",
    "role_check_omitted_on_new_endpoint":
        "Ship the boarding availability endpoint without a role check",
    "receptionist_granted_controlled_dispensing_right":
        "Give front desk staff the controlled dispensing permission",
    "break_glass_access_never_expires":
        "Remove the expiry from break-glass grants so support keeps access",
    "service_account_shared_across_practices":
        "Reuse one integration account across every clinic in the estate",
    "authorization_decision_made_in_frontend_only":
        "Hide the admin buttons in the UI instead of checking server-side",
    "tenant_id_derived_from_user_supplied_header":
        "Read the practice id from the X-Practice request header",

    # ---- SC ---------------------------------------------------------------
    "unsigned_commit_merged_to_protected_branch":
        "Turn off signature enforcement on main to unblock the release train",
    "dependency_introduces_cve_above_cvss_seven":
        "Pull in the charting library release carrying the open critical advisory",
    "package_name_resolves_to_public_registry_first":
        "Put the public registry ahead of the internal one in the resolver",
    "copyleft_licensed_dependency_added_to_proprietary_service":
        "Vendor the AGPL HL7 parser into the shipped practice API",
    "build_runner_reused_across_jobs":
        "Keep the build runner warm between jobs to cut CI minutes",
    "provenance_attestation_absent_for_release_artifact":
        "Publish the hotfix image straight from a laptop build",
    "api_key_committed_in_diff":
        "Hardcode the reference lab API key in the connector config",
    "lockfile_bypassed_by_direct_install_step":
        "Add a post-install step that pulls the package directly",
    "transitive_dependency_from_unverified_maintainer":
        "Swap the date library for a fork published by an unknown account",

    # ---- AI ---------------------------------------------------------------
    "agent_pr_modifies_authentication_middleware":
        "Let the coding agent rewrite the session authentication middleware",
    "agent_pr_modifies_controlled_dispensing_logic":
        "Have the agent refactor the controlled dispensing rules engine",
    "agent_code_calls_non_allowlisted_external_host":
        "Call an external summarisation API from the agent's new helper",
    "hallucinated_dependency_not_present_in_registry":
        "Add the vetpoc-hl7-utils package the agent's patch imports",
    "cyclomatic_complexity_exceeds_threshold_on_agent_diff":
        "Merge the agent's forty-branch claims eligibility function as written",
    "agent_instruction_sourced_from_untrusted_ticket_text":
        "Feed the customer's ticket body straight into the agent's task prompt",
    "prompt_injection_marker_present_in_issue_body":
        "Run the agent on the issue whose body carries its own instructions",
    "agent_disabled_a_failing_compliance_test":
        "Skip the dispensing audit test the agent could not get passing",
    "agent_change_lacks_any_human_reviewer":
        "Auto-merge agent pull requests once CI is green",

    # ---- AS ---------------------------------------------------------------
    "string_concatenated_sql_introduced":
        "Build the chart-search filter by concatenating the query string",
    "raw_html_rendered_from_owner_supplied_note":
        "Render the owner's intake note as raw HTML to keep their formatting",
    "content_security_policy_relaxed_to_unsafe_inline":
        "Allow inline scripts in the portal CSP so the booking widget loads",
    "path_traversal_reachable_from_upload_handler":
        "Use the client-supplied filename as the attachment storage path",
    "server_side_request_forgery_reachable_from_webhook":
        "Fetch whatever callback URL the practice webhook supplies",
    "unsafe_deserialisation_of_client_payload":
        "Restore session objects by deserialising the client-supplied blob",
    "stack_trace_returned_to_client":
        "Return the full exception text in the API error body",
    "cryptographic_primitive_hand_rolled":
        "Write our own token signing routine to drop the crypto dependency",

    # ---- HA ---------------------------------------------------------------
    "read_modify_write_without_locking_on_shared_row":
        "Read and rewrite the stock row without taking a lock",
    "inventory_decrement_race_reachable_under_load":
        "Move the inventory decrement out of the transaction to cut latency",
    "deploy_freeze_window_overridden_without_approval":
        "Push the config cleanup during Saturday emergency hours",
    "irreversible_migration_shipped_without_backup_proof":
        "Drop the legacy vaccine history columns with no down-migration",
    "unbounded_retry_amplifies_outage":
        "Retry lab submissions every second until the lab responds",
    "clinical_note_last_write_wins_silently":
        "Let the last save win when two clinicians edit the same note",

    # ---- RR ---------------------------------------------------------------
    "audit_row_updated_in_place":
        "Add an admin path that updates the audit row to fix a typo",
    "medical_record_amendment_overwrites_original":
        "Overwrite the original diagnosis text when a chart is amended",
    "audit_logging_disabled_for_performance":
        "Turn off audit writes on the hot dispensing path",
    "retention_clock_reset_by_record_edit":
        "Reset the retention date whenever a record is edited",
    "export_omits_realised_adverse_contest_rate":
        "Trim the contest counts from the audit export header",
    "rationale_summarised_after_the_fact":
        "Generate decision rationales from the outcome at export time",
    "clock_source_client_supplied":
        "Timestamp records from the workstation clock the client sends",

    # ---- AW ---------------------------------------------------------------
    "surgical_task_delegated_to_unqualified_staff":
        "Allow assistants to sign off dental extractions in the procedure log",
    "anaesthesia_monitoring_gap_exceeds_protocol":
        "Widen anaesthesia vitals capture to one entry per hour",
    "welfare_inspection_finding_left_unremediated":
        "Auto-close welfare findings nobody actions within thirty days",
    "procedure_performed_outside_licensed_scope":
        "Let relief staff record procedures their licence does not cover",
    "controlled_analgesia_omitted_without_rationale":
        "Make the post-operative analgesia plan optional at discharge",

    # ---- GV ---------------------------------------------------------------
    "appeal_path_removed_by_configuration":
        "Hide the contest link when the decision is a denial",
    "automated_decision_final_with_no_human_route":
        "Close automated denials without offering a human review request",
    "standing_declaration_absent_from_export":
        "Strip the standing declaration from the audit bundle header",
    "charging_threshold_tuned_by_adjudicating_service":
        "Let the adjudication service tune its own charging threshold at runtime",
    "reporter_bulletin_injected_into_adjudicator_context":
        "Include the weekly reporter bulletin in the adjudicator's context",
    "audit_finding_read_during_retrieval":
        "Rank retrieval candidates using the audit register's findings",
    "vulnerability_of_owner_exploited_by_pricing_logic":
        "Target payment-plan upsells at owners flagged as financially distressed",
    "biometric_scraping_of_untargeted_images_enabled":
        "Build a searchable face gallery from the lobby camera feed",
}


# --------------------------------------------------------------------------
# 4. Changes that edit the rulebook itself rather than the code.
# --------------------------------------------------------------------------

CONTROL_PLANE_CHANGES = [
    "Lower the changed-line coverage threshold in the policy repo",
    "Raise the p95 latency budget from ten to twenty-five percent",
    "Edit the CI workflow to skip the secret-scan gate on this branch",
    "Propose reclassifying the residency provision as ordinary in policy metadata",
    "File a draft amendment codifying module-level coverage for generated code",
    "Shorten the break-glass expiry constant in the rulebook",
    "Widen the deploy freeze exception list in the governance repo",
    "Amend the retention schedule for controlled-substance records in the rulebook",
    "Add the boarding service to the critical-service list in policy",
    "Rewrite the Rego role-check rule using the adjudication service credentials",
    "Draft an amendment permitting telehealth-established VCPR in two more states",
    "Move the CVSS threshold from seven to eight in the dependency policy",
    "Remove the two-person rule for EPCS grants from the policy repo",
    "Propose a sunset clause for the analytics pilot exception",
    "Register the new agent runner in the allowlist policy bundle",
    "Renumber the point-of-care provisions after the device policy merge",
    "Change the escalation ladder so the third tier is final",
    "Submit an amendment adding a welfare-inspection remediation window",
]


# --------------------------------------------------------------------------
# Every change in this corpus is a DEVELOPMENT change: something a developer or
# a coding agent proposes, and a reviewer sees, before the code is built and
# packaged. It is what a pull request contains — source, configuration,
# infrastructure, schema and migrations, pipeline definitions, tests, the policy
# repository, and documents that live in the tree beside them.
#
# It is NOT a runtime business transaction, and it is not a process act with no
# artefact. The corpus adjudicates proposed changes; it does not adjudicate
# payments, shipments, prescriptions, or the act of completing a review. An
# audit of all five catalogues on 2026-09-06 found forty-eight titles that had
# drifted across that line in one of two ways:
#
#   an act on live data      "Correct the mis-posted interchange fee by
#                             updating the ledger row" — a data edit, not a diff
#   a process with no diff   "Complete the vendor security review for the
#                             statement PDF renderer" — a thing that happens in
#                             a meeting, not in a tree
#
# Both were rewritten as the change that would actually appear in the pull
# request: the admin action that edits the row, the review attached to the
# dependency. The guard below is what stops them coming back. It is a LEXICAL
# guard over the catalogue, not a proof that a title is well formed — a check
# that claims more than it tests is its own defect — so it is stated as what it
# is: a closed list of openings that name an act rather than an edit.
# --------------------------------------------------------------------------

NON_DEVELOPMENT_OPENINGS = (
    "complete the", "complete vendor", "rehearse the", "rehearse regional",
    "exercise the", "exercise failover", "retro-approve", "notify the",
    "escalate overdue", "issue the", "cite the", "get sre", "have the safety",
    "have the external", "sample production", "audit the orphaned",
    "close complaints", "close last", "close the tool", "correct the mis",
    "correct the mistyped", "export the whole", "export the quarterly",
    "export the mature", "provision external", "review the benchmark",
    "review alert", "mark the shipment", "send the capacity",
    "run the retention sweep", "file the ", "file blocked",
)

# "File a draft amendment ..." is the A3 route and is an edit to the policy
# repository, so it is exempt by name rather than by accident.
DEVELOPMENT_EXEMPTIONS = ("file a draft amendment", "file an amendment")


def is_development_change(title: str) -> bool:
    t = " ".join(title.lower().split())
    if any(t.startswith(x) for x in DEVELOPMENT_EXEMPTIONS):
        return True
    return not any(t.startswith(x) for x in NON_DEVELOPMENT_OPENINGS)


def non_development_titles():
    """Every catalogue title that reads as an act rather than an edit."""
    out = []
    for t in VIOLATION_CHANGES.values():
        if not is_development_change(t):
            out.append(t)
    for lst in COMPLIANT_CHANGES.values():
        out.extend(t for t in lst if not is_development_change(t))
    out.extend(t for t in CONTROL_PLANE_CHANGES if not is_development_change(t))
    return sorted(set(out))

# --- scenario extension (corpus 2.0.0) ---
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import ext_changes as _ext  # noqa: E402
FAMILY_CONTEXT.update(_ext.FAMILY_CONTEXT)
COMPLIANT_CHANGES.update(_ext.COMPLIANT_CHANGES)
VIOLATION_CHANGES.update(_ext.VIOLATION_CHANGES)
