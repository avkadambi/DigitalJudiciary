"""
DCVigil domain change catalogue — scenario extension (corpus 2.0.0).

Narrative vocabulary for the eight families added by ext_vocab.py: where each
family's work lives in the organisation, and what the pull requests that engage
it actually say. Every title is written as a DCVigil engineer would write it
about their own change — concrete systems, concrete artefacts, no awareness that
anything is adjudicating the change, and no mention of the rule it engages.

Three tables, merged into changes.py by the shim:

  FAMILY_CONTEXT      areas drawn from vocab.AREAS, services from vocab.SERVICES.

  COMPLIANT_CHANGES   per family, changes that ENGAGE the family's provisions and
                      do nothing wrong. Items marked `# guard` are the ones that
                      read like violations to a suspicious reviewer and are not:
                      a permitted exception correctly invoked, a correct-but-
                      unusual implementation, or a removal that is of dead or
                      non-conforming code. They are what lets the corpus measure
                      over-blocking rather than only over-permissiveness.

  VIOLATION_CHANGES   one title per new violate factor, keyed by the exact factor
                      string. The title makes the violation legible on its own
                      terms; the factor name never appears in it.

Every title is a DEVELOPMENT change in the sense of changes.is_development_change:
something a reviewer sees in a pull request — source, configuration, infra,
schema, pipeline, tests, the policy repository, or a document in the tree.

Standard library only. No imports.
"""

# --------------------------------------------------------------------------
# 1. Where each new family's cases live in the org.
# --------------------------------------------------------------------------

FAMILY_CONTEXT = {
    "LA": {
        "areas": ["platform", "org", "security-telemetry", "portal"],
        "services": [
            "svc:tsdb-writer",
            "svc:customer-portal",
            "svc:badge-access-pipeline",
            "svc:telemetry-ingest",
        ],
    },
    "LS": {
        "areas": ["thermal", "remediation", "edge", "escalation"],
        "services": [
            "svc:bms-redfish-poller",
            "svc:remediation-advisor",
            "svc:edge-collector",
            "svc:escalation-router",
            "svc:sensor-gateway-collector",
        ],
    },
    "EN": {
        "areas": ["thermal", "capacity", "platform", "portal", "org"],
        "services": [
            "svc:bms-redfish-poller",
            "svc:capacity-benchmark",
            "svc:tsdb-writer",
            "svc:customer-portal",
            "svc:telemetry-ingest",
        ],
    },
    "CT": {
        "areas": ["platform", "portal", "capacity", "org"],
        "services": [
            "svc:customer-portal",
            "svc:tsdb-writer",
            "svc:telemetry-ingest",
            "svc:capacity-benchmark",
            "svc:escalation-router",
        ],
    },
    "OT": {
        "areas": ["edge", "thermal", "ingestion", "security-telemetry"],
        "services": [
            "svc:sensor-gateway-collector",
            "svc:bms-redfish-poller",
            "svc:edge-collector",
            "svc:telemetry-ingest",
        ],
    },
    "SV": {
        "areas": ["platform", "edge", "portal", "org"],
        "services": [
            "svc:edge-collector",
            "svc:sensor-gateway-collector",
            "svc:customer-portal",
            "svc:telemetry-ingest",
            "svc:log-parser-sandbox",
        ],
    },
    "AX": {
        "areas": ["portal", "alerting", "escalation"],
        "services": [
            "svc:customer-portal",
            "svc:alerting-rule-evaluator",
            "svc:escalation-router",
        ],
    },
    "TC": {
        "areas": ["platform", "edge", "portal", "org"],
        "services": [
            "svc:edge-collector",
            "svc:customer-portal",
            "svc:sensor-gateway-collector",
            "svc:telemetry-ingest",
        ],
    },
}

# --------------------------------------------------------------------------
# 2. Compliant / neutral change titles, per family.
# --------------------------------------------------------------------------

COMPLIANT_CHANGES = {
    "LA": [
        "Block every deletion path while a preservation flag is set",
        "Resolve preservation scope before the retention job selects rows",
        "Require a named legal approver to release a preservation hold",
        "Route incoming legal process through counsel before any export runs",
        "Extend the preservation flag to derived and aggregated stores",
        "Escalate conflicting cross-border duties before the path is built",
        "Route overseas requests to the treaty channel instead of the export tool",
        "Write one register entry per request with requester and legal basis",
        "Make the disclosure register append-only and exportable",
        "Derive the published request counts from the register",
        "Copy held telemetry into a store outside the expiring tier",
        "Record the after-the-fact review of an emergency disclosure",
        # guard: reads as suppressing notice; it is the statutory carve-out,
        # correctly conditioned on the order actually prohibiting notice
        "Send the customer notice unless the order served forbids it",
        # guard: reads as withholding evidence; narrowing to the terms of the
        # order is the duty, and the wide query was the defect
        "Narrow the disclosure export query to the terms of the order",
        # guard: a skip that is the compliant act, not an evasion
        "Skip the purge step for the records a preservation flag covers",
    ],
    "LS": [
        "Exclude suppression and power-off circuits from the action catalogue",
        "Make the fire and interlock integration read-only end to end",
        "Write generator run records straight from the controller reading",
        "Source the fuel-level series from the tank sensor only",
        "Store the load-bank test trace beside its summary result",
        "Keep the physical-incident reporting step reachable from the runbook",
        "Classify physical incidents against the published criteria",
        "Version the site resilience evidence in the platform repository",
        "Verify the alarm relay path after every collector release",
        "Encode the emergency power test cadence in the scheduler",
        "Link the site walkdown evidence to the asset record",
        # guard: a removal that is the compliant act — the command should never
        # have been in the planner's action set
        "Remove the transfer-switch command from the recovery plan's action set",
        # guard: an exemption correctly invoked; life-safety alarms are the one
        # class the deduplication window must not swallow
        "Exempt panel alarms from the alert deduplication window",
        # guard: reads as giving the advisor reach into the panel; it is the
        # read-only half, which is what the monitoring product is for
        "Let the thermal advisor read panel state without any write path",
    ],
    "EN": [
        "Derive the reported site energy total from the metered series",
        "Run the statutory submission job on its published cadence",
        "Hash and retain the submission payload with the filing record",
        "Declare the efficiency metric's boundary and denominator",
        "Record waste-heat recovery data per site in the export",
        "Trace every sustainability datapoint to its source system",
        "Version the metric lineage alongside the pipeline code",
        "Label modelled cooling values as estimates in the export",
        "Report a missing meter interval as a gap rather than a value",
        "Source the water usage series from the site meter",
        "Record the reporting boundary change with its effective date",
        "Make the assurance export reproducible from the raw series",
        # guard: restating a published series reads like rewriting history; it
        # is what a method change requires so the series stays comparable
        "Restate the published efficiency series when the method changes",
        # guard: a removal that is the compliant act — interpolation had been
        # silently filling regulatory gaps
        "Drop the interpolation step from the meter gap handler",
        # guard: reads as letting an incomplete filing through; the field is
        # optional under the scheme and a blank is the honest value
        "Let a site file with the optional benchmark field left empty",
    ],
    "CT": [
        "Hold each tenant's key material in its own key ring",
        "Resolve the customer-managed key reference on every request",
        "Produce the offboarding export inside the contracted window",
        "Issue a deletion certificate after the final purge run",
        "Align backup expiry with the tenant's deletion commitment",
        "Send the sub-processor notice before any processing starts",
        "Update the sub-processor register with region and purpose",
        "Expose a per-tenant evidence export on the portal",
        "Carry the regulated-regime attribute through every pipeline",
        "Read the retention term from the tenant's contract record",
        "Enumerate residual derived data before the deletion run",
        "Verify key-ring separation with a per-tenant restore drill",
        # guard: reads as an availability bug; failing closed on an unreachable
        # customer key is the whole point of customer-managed keys
        "Fail the read when the customer's own key is unreachable",
        # guard: a deletion that is the compliant act
        "Delete the derived capacity features when a tenant offboards",
        # guard: reads as blocking a customer's migration; the wait is the
        # objection window the contract gives every other tenant
        "Hold the storage cutover until the objection window closes",
    ],
    "OT": [
        "Enumerate every permitted facility flow in the conduit allow-list",
        "Confine building-management traffic to its own zone",
        "Reach baseboard controllers only from the management zone",
        "Move the new device paths onto authenticated SNMPv3",
        "Issue a unique credential per building controller",
        "Wrap the plaintext device protocol in an authenticated tunnel",
        "Verify the gateway firmware signature before flashing",
        "Record firmware version and hash for every polled device",
        "Retain the rollback firmware image for the supported window",
        "Block register writes on the polling service account",
        "Time-box and record the vendor maintenance path",
        "Review the zone boundary change before the merge lands",
        # guard: disabling a capability reads as a regression; write services
        # have no place in a monitoring collector
        "Disable the write service on the building-management collector",
        # guard: narrowing discovery reads as losing coverage; the declared
        # subnets are the ones the customer agreed to
        "Confine device discovery to the declared subnets",
        # guard: a removal of a legacy path that was never conforming
        "Drop the legacy community-string path from the environmental poller",
    ],
    "SV": [
        "Publish a bill of materials with every customer-facing release",
        "Issue an exploitability statement for each reported component finding",
        "Regenerate the bill of materials when a dependency changes",
        "Wire the security reporting hook to the single reporting entry point",
        "Start the incident notification clock at first awareness",
        "Name the reporting owner in the release record",
        "Publish and monitor the security disclosure intake address",
        "Acknowledge researcher reports inside the published window",
        "Ship the mitigation within the deadline for its severity band",
        "Schedule an independent security test for each customer-facing surface",
        "Attach the developer security testing evidence to the release record",
        "Track the remediation deadline per severity band",
        "Move the status page onto infrastructure outside the platform",
        "Deliver the root-cause document inside the contracted window",
        "Declare the severity scoring method in the advisory",
        "Add a regression test for every fixed vulnerability",
        # guard: shipping without an advisory reads as concealment; no released
        # build carried the defect, so there is nothing to advise on
        "Ship the parser fix with no advisory where no release carried the defect",
        # guard: withdrawing a draft advisory reads as suppression; it named a
        # component the product never shipped
        "Withdraw the draft advisory that names a component we never shipped",
        # guard: an exemption correctly invoked — the harness is internal and
        # never reaches a customer
        "Skip the bill of materials step for the internal-only test harness",
    ],
    "AX": [
        "Run the accessibility check on every portal release",
        "Block the release on a Level AA conformance failure",
        "Record a manual screen-reader pass for each new console view",
        "Convey alarm severity with text and shape as well as colour",
        "Pair the audible alert with a visible equivalent",
        "Verify contrast on the operations dashboard",
        "Cover every acknowledgement control with a keyboard path",
        "Give every dashboard control an accessible name",
        "Verify focus order on the incident drawer",
        "Let the operator extend the console session timeout",
        "Version the accessibility statement beside the portal code",
        "Add text labels to the rack heatmap's severity bands",
        # guard: removing a legend reads as losing information; the legend was
        # the colour-only path and text labels replace it
        "Remove the colour-only severity legend from the dashboard",
        # guard: an exemption correctly invoked — the archived demo portal is
        # unreachable by any customer
        "Skip the conformance gate on the archived demo portal",
        # guard: keeping colour reads as keeping the defect; colour alongside
        # text is conformant, colour alone was not
        "Keep the alert list's colour coding now that text labels are there",
    ],
    "TC": [
        "Screen every counterparty against the current restricted-party lists",
        "Refresh the screening list from its published source on each run",
        "Check the ownership chain against the fifty-percent test",
        "Record the cryptography classification before the build publishes",
        "Gate the agent download endpoint on the destination check",
        "Record the licence basis for the shipped collector",
        "Route screening hits to trade compliance for disposition",
        "Retain the screening result with the onboarding record",
        "Run the deemed-export check before granting support access",
        "Derive the destination from verified account data",
        "Review the classification when the cryptography stack changes",
        "Add the restricted-party check to the reseller signup path",
        # guard: blocking a download reads as breaking onboarding; failing
        # closed on an unresolvable destination is the required posture
        "Block the download when the destination check cannot resolve",
        # guard: clearing a match reads as bypassing screening; the ownership
        # check ruled it out and the disposition is recorded
        "Clear the screening match the ownership check ruled out",
        # guard: opening a destination reads as widening exposure; the
        # destination was removed from the list by the issuing authority
        "Open the download endpoint to the newly delisted destination",
    ],
}

# --------------------------------------------------------------------------
# 3. One title per new violate factor.
# --------------------------------------------------------------------------

VIOLATION_CHANGES = {
    # ---- LA: lawful access, legal hold and government requests ----
    "retention_job_deletes_records_under_an_open_hold":
        "Let the nightly retention sweep run over records under an open matter",
    "legal_hold_flag_ignored_by_the_new_purge_path":
        "Skip the preservation flag lookup in the new tenant purge path",
    "customer_content_disclosed_without_legal_review":
        "Let the support export tool answer subpoenas straight from the queue",
    "customer_notice_suppressed_where_notice_is_permitted":
        "Drop the customer notification step from the request-handling workflow",
    "foreign_order_answered_directly_from_the_export_tool":
        "Add an overseas request form that exports tenant content on submission",
    "conflicting_disclosure_duty_left_unresolved_at_design":
        "Ship the disclosure pipeline and settle the cross-border conflict later",
    "disclosure_register_entry_omitted_for_urgent_requests":
        "Skip the register write when a request comes in flagged urgent",
    "disclosure_register_made_editable_by_support_role":
        "Give the support role update rights on the disclosure register",
    "hold_release_automated_without_legal_approval":
        "Auto-release preservation holds once the matter ticket closes",
    "preservation_copy_stored_in_the_expiring_tier":
        "Keep preserved snapshots in the ninety-day expiring bucket",
    "requester_identity_not_recorded_on_the_request":
        "Drop the requester and legal-basis fields from the intake form",

    # ---- LS: life-safety systems and physical resilience ----
    "suppression_release_reachable_from_the_action_planner":
        "Add the suppression-system release command to the action catalogue",
    "emergency_power_off_wired_into_automated_recovery":
        "Wire the emergency power-off circuit into the automated recovery flow",
    "generator_test_result_back_filled_from_the_schedule":
        "Back-fill missing generator test results from the maintenance calendar",
    "fuel_level_series_synthesised_when_the_sensor_is_silent":
        "Carry the last fuel reading forward while the tank sensor is silent",
    "physical_incident_report_path_removed_from_the_runbook":
        "Remove the physical-incident reporting step from the site runbook",
    "resilience_evidence_kept_only_in_a_personal_export":
        "Keep the site resilience evidence in the lead engineer's own workbook",
    "fire_panel_integration_given_a_write_endpoint":
        "Add a silence-command endpoint to the fire panel integration",
    "life_safety_alarm_folded_into_the_deduplication_window":
        "Fold panel alarms into the five-minute deduplication window",
    "ups_transfer_added_to_the_automated_recovery_plan":
        "Let the recovery plan switch the UPS to bypass during a thermal event",

    # ---- EN: energy, water and sustainability reporting ----
    "statutory_energy_submission_disabled_for_a_named_site":
        "Turn off the annual energy submission job for the Kestrel campus",
    "reported_energy_figure_overridden_by_a_manual_constant":
        "Let an operator pin the reported site energy total to a fixed value",
    "efficiency_denominator_changed_without_restating_series":
        "Move the efficiency metric's boundary and leave the published series",
    "waste_heat_data_dropped_from_the_site_export":
        "Drop the waste-heat recovery fields from the site reporting export",
    "sustainability_datapoint_sourced_from_an_untracked_sheet":
        "Pull the emissions datapoint from the finance team's untracked workbook",
    "estimated_value_published_without_an_estimate_label":
        "Publish modelled cooling energy beside metered values with no marker",
    "missing_meter_interval_interpolated_into_the_filing":
        "Interpolate missing meter intervals straight into the regulatory filing",
    "water_usage_series_replaced_by_a_design_figure":
        "Substitute the design water figure where the site meter is unavailable",
    "reporting_boundary_narrowed_without_an_effective_date":
        "Narrow the reporting boundary to owned halls with no effective date",

    # ---- CT: tenant keys, exit, sub-processors, audit rights ----
    "tenant_keys_pooled_into_one_platform_key_ring":
        "Move every tenant's encryption keys onto one platform key ring",
    "customer_managed_key_replaced_by_a_platform_default":
        "Fall back to the platform key when the customer key endpoint times out",
    "offboarding_export_deferred_past_contracted_window":
        "Queue offboarding exports behind the quarterly migration backlog",
    "deleted_tenant_data_left_in_the_derived_feature_store":
        "Leave derived capacity features in place when a tenant is deleted",
    "sub_processor_added_before_any_customer_notice":
        "Route telemetry through the new storage vendor ahead of the notice batch",
    "objection_window_skipped_for_an_urgent_cutover":
        "Cut over to the new queue vendor before the objection window closes",
    "per_tenant_evidence_export_removed_from_the_portal":
        "Remove the per-tenant evidence export from the portal compliance page",
    "regulated_regime_flag_dropped_by_the_new_writer":
        "Drop the customer's regulatory-regime attribute in the new writer path",
    "backup_retention_outlives_the_deletion_commitment":
        "Keep tenant backups three years past the agreed deletion window",
    "tenant_retention_term_hardcoded_across_all_customers":
        "Hardcode one retention term for every customer in the writer",
    "sub_processor_register_left_unchanged_after_the_move":
        "Move the queue to the new region and leave the vendor register as is",

    # ---- OT: protocols, zoning and device firmware ----
    "conduit_allow_list_replaced_by_a_flat_route":
        "Replace the facility allow-list with a flat route to the ingest tier",
    "building_management_network_bridged_to_corporate_zone":
        "Bridge the building-management network onto the corporate office subnet",
    "snmp_v2c_community_string_used_on_a_new_device_path":
        "Poll the new PDU fleet with a shared SNMPv2c community string",
    "ipmi_credentials_shared_across_the_rack_fleet":
        "Bake one baseboard-controller password into the rack imaging profile",
    "gateway_firmware_flashed_without_signature_check":
        "Flash gateway firmware straight from the vendor's download link",
    "firmware_version_left_unrecorded_after_the_flash":
        "Skip the firmware version and hash write after a field upgrade",
    "bacnet_write_service_enabled_on_the_polling_service":
        "Enable write-property calls on the building-management poller",
    "modbus_writes_opened_to_the_shared_collector_role":
        "Open holding-register writes to the shared collector service account",
    "device_discovery_widened_to_the_whole_site_range":
        "Widen device discovery from the declared subnets to the whole site",

    # ---- SV: product security assurance ----
    "sbom_generation_dropped_from_the_release_pipeline":
        "Drop the bill-of-materials step from the collector release pipeline",
    "exploitability_statement_omitted_for_known_finding":
        "Ship the release with no exploitability note on the known finding",
    "exploited_vulnerability_report_left_without_an_owner":
        "Point the security reporting hook at a mailbox nobody owns",
    "severe_incident_clock_started_at_triage_not_awareness":
        "Start the incident reporting clock when triage opens the ticket",
    "disclosure_intake_address_removed_from_the_site":
        "Remove the security contact page and its intake address from the site",
    "patch_deadline_extended_without_a_recorded_decision":
        "Push the critical patch deadline out a quarter in the tracker config",
    "penetration_test_dropped_for_the_portal_release_train":
        "Take the portal out of the scheduled security test scope",
    "security_testing_evidence_omitted_from_the_release":
        "Ship the release record without the developer security testing evidence",
    "status_page_hosted_on_the_platform_it_reports_on":
        "Serve the customer status page from the platform it reports on",
    "root_cause_analysis_reduced_to_a_one_line_summary":
        "Replace the customer root-cause document with a one-line summary field",
    "advisory_published_without_a_severity_method":
        "Publish advisories with a severity label and no scoring method",
    "fixed_vulnerability_shipped_without_a_regression_test":
        "Ship the sandbox escape fix with no test covering the reported input",
    "component_provenance_left_out_of_release_manifest":
        "Leave the component origin fields out of the release manifest",

    # ---- AX: accessibility ----
    "accessibility_gate_removed_from_the_portal_pipeline":
        "Take the accessibility check out of the portal build pipeline",
    "conformance_failures_downgraded_to_build_warnings":
        "Downgrade accessibility conformance failures to build warnings",
    "alarm_severity_conveyed_by_colour_alone":
        "Show alarm severity on the operator dashboard with colour alone",
    "audible_alert_shipped_with_no_visible_equivalent":
        "Signal the new escalation state with a chime and nothing on screen",
    "acknowledgement_control_reachable_only_by_pointer":
        "Make the alert acknowledgement control drag-only on the console",
    "dashboard_control_shipped_without_accessible_name":
        "Ship the custom rack-heatmap control with no accessible name",
    "operator_session_expires_with_no_extension_path":
        "Expire the operator console session with no way to extend it",

    # ---- TC: trade controls ----
    "restricted_party_screening_bypassed_for_fast_onboarding":
        "Skip the restricted-party check on the expedited onboarding path",
    "screening_list_pinned_to_a_stale_local_copy":
        "Pin the restricted-party list to the copy committed last year",
    "agent_download_endpoint_opened_to_every_destination":
        "Open the agent download endpoint to every country and region",
    "encryption_classification_left_unrecorded_at_release":
        "Publish the collector release before its cryptography review lands",
    "ownership_chain_check_skipped_for_a_subsidiary_account":
        "Screen only the signing entity and skip its parent ownership chain",
    "screening_hit_auto_cleared_by_the_onboarding_job":
        "Let the onboarding job clear its own restricted-party matches",
    "support_access_granted_without_deemed_export_check":
        "Grant the offshore support rota access to the controlled build tree",
}
