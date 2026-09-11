"""
SemiFab domain change catalogue — scenario extension (corpus 2.0.0).

Narrative catalogue for the six new families in ext_vocab.py: ITAR and
defence articles (IT), sanctions / anti-boycott / investment screening (SO),
responsible sourcing and part integrity (RS), environment, health and safety
(EH), quality system and customer change notification (QS), and OT network
and remote access (OT).

Same shape as changes.py: FAMILY_CONTEXT (areas/services drawn only from
changes.AREAS / changes.SERVICES), COMPLIANT_CHANGES (titles that engage a
family's provisions and do nothing wrong — several marked `# guard`: titles
that sound like a violation to a suspicious reader but are not), and
VIOLATION_CHANGES (exactly one title per new violate factor in ext_vocab.py).

Titles are written as an engineer would write them about their own pull
request against the SECS/GEM tool gateway, the recipe vault, the export
screening and licence-determination services, the tool telemetry/metrology
ingest path, the MES/WIP tracker, the lot-genealogy and yield-analytics
services, or the supplier portal. They never name a provision, a factor, a
regulation, or the words scenario/axiom/provision/factor/judiciary — the
engineer filing the change does not know it is being adjudicated.
"""

# --------------------------------------------------------------------------
# Where each new family's work happens, drawn only from the pack's existing
# AREAS / SERVICES lists (changes.py, per the semifab/vetpoc carve-out in the
# authoring spec).
# --------------------------------------------------------------------------

FAMILY_CONTEXT = {
    "IT": {"areas": ["trade-compliance", "platform", "security"],
           "services": ["svc:export-screening", "svc:licence-determination",
                        "svc:artifact-registry", "svc:audit-ledger"]},
    "SO": {"areas": ["trade-compliance", "supplier-portal", "platform"],
           "services": ["svc:export-screening", "svc:licence-determination",
                        "svc:supplier-portal", "svc:audit-ledger"]},
    "RS": {"areas": ["supplier-portal", "mes-core", "platform"],
           "services": ["svc:supplier-portal", "svc:lot-genealogy",
                        "svc:wip-tracker", "svc:audit-ledger"]},
    "EH": {"areas": ["equipment-integration", "mes-core", "metrology"],
           "services": ["svc:tool-gateway", "svc:secs-message-broker",
                        "svc:metrology-ingest", "svc:audit-ledger"]},
    "QS": {"areas": ["recipe-management", "mes-core", "metrology"],
           "services": ["svc:recipe-vault", "svc:wip-tracker",
                        "svc:lot-genealogy", "svc:yield-analytics"]},
    "OT": {"areas": ["equipment-integration", "security", "mes-core"],
           "services": ["svc:tool-gateway", "svc:secs-message-broker",
                        "svc:agent-runner", "svc:audit-ledger"]},
}

# --------------------------------------------------------------------------
# Compliant work. These engage the family and do nothing wrong. Guard items
# (marked `# guard`) sound like violations to a suspicious reader but are the
# correctly implemented, permitted case.
# --------------------------------------------------------------------------

COMPLIANT_CHANGES = {
    "IT": [
        "Record the empowered official's signature on every ITAR authorisation",
        "Bind the DDTC registration-status check into the enclave access grant",
        "Confine defence-article design reviews to the segregated enclave workstation",
        "Encrypt ITAR technical data end-to-end before it leaves the authorised boundary",
        "Exclude proscribed-country regions from the defence-enclave storage allowlist",
        "Record the jurisdiction determination before a defence-adjacent file is ingested",
        "Default an unresolved jurisdiction determination to ITAR pending review",  # guard
        "Deny defence-enclave egress by default and allowlist only reviewed destinations",
        "Log the citizenship attribute alongside every ITAR access event",
        "Retain ITAR access records for the full five-year floor",
        "Name the licence-exception paragraph on every ITAR transfer record",
        "Reclassify a defence article from ITAR to EAR only after a commodity-jurisdiction determination clears it",  # guard
        "Merge the enclave's stale service accounts into the quarterly access review",  # guard
    ],
    "SO": [
        "Screen every counterparty against the SDN and consolidated lists including fifty-percent-owned entities",
        "Fail the sanctions screening pipeline closed when the list service is unreachable",
        "Route every boycott-request match to the quarterly filing queue",
        "Reject a boycott-compliance clause in the contract-template parser",
        "Record the outbound-investment determination before a joint-venture data share opens",
        "Record the CFIUS declaration status on every covered transaction before close",
        "Refresh the sanctions list snapshot on the published daily cadence",
        "Route a sanctions list match to a named human reviewer for disposition",
        "Retain sanctions screening records for the full ten-year floor",
        "Record the ownership data source and snapshot date on every screening result",
        "Release a blocked-property hold only after a documented general licence applies",  # guard
        "Accept a counterparty's boycott-neutral standard clause after legal review",  # guard
        "Downgrade a fuzzy sanctions-list near-miss to a documented false positive after two-person review",  # guard
    ],
    "RS": [
        "Collect smelter-and-refiner identity data during supplier onboarding",
        "Retain the conflict-minerals inquiry response on the component record",
        "Screen suppliers and upstream sources against the forced-labour entity list",
        "Fail closed on receipt when a forced-labour list match is returned",
        "Attach supply-chain tracing evidence to every flagged lot",
        "Record the counterfeit-inspection result and distributor-authorisation status per lot",
        "Report a suspect counterfeit part to the named quality owner before disposition",
        "Quarantine a broker-sourced lot pending provenance verification",
        "Clear a grey-market flag only after a recorded provenance disposition",  # guard
        "Version the supplier declaration record on every effective-date change",
        "Enforce supplier-attestation expiry at the receiving dock",
        "Expedite receipt of a lot whose counterfeit inspection already passed same-day",  # guard
        "Release a quarantined lot to production once its provenance chain is fully verified",  # guard
    ],
    "EH": [
        "Route hazardous-gas alarms to the life-safety panel ahead of any analytics path",
        "Require an EHS signoff record before a gas-alarm threshold change ships",
        "Keep the lockout/tagout state read-only in the software layer",
        "Preserve the emergency-stop state unchanged through the equipment status feed",
        "Persist every effluent monitoring result before report aggregation runs",
        "Trace every discharge-report value back to its raw measurement",
        "Alert the named EHS owner when the emissions-reporting job fails",
        "Retain ESD-monitor telemetry at native resolution for the declared period",
        "Record the effective date on every environmental-sampling change",
        "Isolate the life-safety signal path from the analytics pipeline",
        "Attribute every EHS alarm acknowledgement to a named person",
        "Lower a gas-detector alarm threshold after a failed calibration, with EHS signoff recorded same day",  # guard
        "Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact",  # guard
        "Retire the legacy gas-alarm rate limiter that pre-dated the life-safety panel wiring",  # guard
    ],
    "QS": [
        "Issue a change notice before the first customer lot sees the recipe change",
        "Classify a process change as major or minor with recorded rationale",
        "Enforce the customer's notice period at the release gate",
        "Open a corrective-action record for every nonconformance",
        "Record root cause and verification of effectiveness before closing a corrective action",
        "Attribute corrective-action closure to a named owner",
        "Validate the run-to-run controller model on held-out lots before promotion",
        "Wire a rollback path into every controller-model promotion",
        "Bind the mask revision to its lot and recipe record",
        "Block a retired mask revision from dispatch to the exposure tool",
        "Attach qualification evidence to every process-change record",
        "Capture customer acknowledgement on the change notice before release",
        "Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect",  # guard
        "Close a nonconformance the same day its root cause and corrective action are already on file",  # guard
        "Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record",  # guard
    ],
    "OT": [
        "Restrict tool-network traffic to the declared conduit at the zone boundary",
        "Require OT-owner review before a zone-boundary firewall rule changes",
        "Broker vendor remote sessions through the jump host",
        "Record and time-box every vendor remote-access session",
        "Require named-owner approval per vendor remote session",
        "Verify tool firmware signatures against the vendor key before install",
        "Stage a firmware update on a non-production tool before the fleet rollout",
        "Record firmware provenance on the equipment record at update time",
        "Authenticate the time source for every piece of fab equipment",
        "Monitor and alarm on clock drift across the tool network",
        "Disable a vendor's remote-access account between sessions",
        "Enforce the protocol allowlist at every zone boundary",
        "Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path",  # guard
        "Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window",  # guard
        "Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter",  # guard
    ],
}

# --------------------------------------------------------------------------
# One title per new violate factor.
# --------------------------------------------------------------------------

VIOLATION_CHANGES = {
    # IT
    "itar_technical_data_released_to_foreign_person":
        "Grant read access to the radar-front-end design repository to a contractor holding a non-US passport",
    "defence_enclave_boundary_merged_with_commercial_tenant":
        "Merge the defence enclave's file share into the shared commercial tenant to cut infrastructure cost",
    "itar_transfer_proceeds_without_licence_or_cited_exemption":
        "Let the defence-article transfer proceed without naming a licence or exemption paragraph",
    "ddtc_registration_lapse_not_blocking_transfer":
        "Skip the registration-status check so a defence-article transfer completes over a holiday weekend",
    "itar_data_stored_in_cloud_region_outside_authorised_boundary":
        "Move the defence-enclave backup into the general-purpose cloud region for cheaper storage",
    "itar_decryption_key_available_to_cloud_provider":
        "Hand the defence-enclave decryption key to the cloud provider's managed key service",
    "defence_article_data_ingested_without_jurisdiction_determination":
        "Ingest the new radar-module design files ahead of the classification review",
    "usml_item_classified_under_ear_by_default":
        "Default every uncatalogued defence article to the commerce control list",
    "foreign_person_attribute_defaulted_to_us_person":
        "Default the citizenship attribute to US person when the onboarding form is left blank",
    "itar_export_record_omits_recipient_identity":
        "Drop the recipient identity field from the export record to speed up the batch job",
    "public_domain_asserted_without_ddtc_approval":
        "Mark the technical brief public domain before DDTC clears the release request",

    # SO
    "sanctions_screening_bypassed_for_counterparty_class":
        "Exempt distributor accounts from the sanctions screening step",
    "ownership_aggregation_disabled_in_screening_rule":
        "Disable the fifty-percent ownership rule in the sanctions screening query",
    "boycott_request_dropped_without_report":
        "Drop the boycott-language flag from the purchase-order parser without logging it",
    "boycott_compliance_clause_accepted_by_contract_parser":
        "Let the contract template parser accept a boycott-compliance clause unmodified",
    "jv_data_share_opened_without_outbound_investment_determination":
        "Open the joint-venture data-share pipeline ahead of the counterparty determination",
    "covered_transaction_closed_without_cfius_analysis":
        "Close the equipment joint-venture deal before the transaction-review checklist runs",
    "blocked_property_released_by_configuration":
        "Add a configuration flag that releases blocked-property holds for expedited orders",
    "sanctions_list_snapshot_stale_beyond_declared_interval":
        "Cache the sanctions list snapshot for a month to cut screening latency",
    "sanctions_screening_record_purged_before_retention_expiry":
        "Purge sanctions screening records on the general ninety-day log rotation",

    # RS
    "smelter_data_dropped_from_supplier_onboarding":
        "Drop the smelter-and-refiner questionnaire from the supplier onboarding flow",
    "conflict_minerals_inquiry_marked_complete_without_response":
        "Mark the conflict-minerals inquiry complete when the supplier never responds",
    "forced_labour_screening_disabled_for_supplier_tier":
        "Switch off forced-labour screening for tier-two suppliers to speed onboarding",
    "forced_labour_match_downgraded_to_advisory":
        "Downgrade a forced-labour list match to an advisory warning instead of a block",
    "counterfeit_inspection_step_skipped_for_expedited_lot":
        "Skip the counterfeit inspection step for lots flagged as expedited",
    "suspect_counterfeit_part_released_without_disposition":
        "Release a suspect counterfeit part to production before disposition is recorded",
    "broker_sourced_lot_released_without_provenance":
        "Release the broker-sourced lot from quarantine before the provenance chain is verified",
    "grey_market_flag_cleared_by_configuration":
        "Add a bulk-clear action that removes the grey-market flag from the genealogy record",
    "supplier_attestation_expiry_ignored_at_receipt":
        "Accept receipt of a lot whose supplier attestation expired last quarter",
    "sourcing_screen_snapshot_date_not_recorded":
        "Drop the snapshot-date field from the sourcing screening result",
    "supplier_declaration_overwritten_without_version":
        "Overwrite the supplier declaration record in place instead of versioning it",

    # EH
    "hazardous_gas_alarm_suppressed_by_software_filter":
        "Add a software filter that suppresses repeated hazardous-gas alarm pages",
    "gas_alarm_rate_limited_below_detection_cadence":
        "Rate-limit gas-detector alarm delivery to one page per minute",
    "lockout_tagout_state_overridable_from_host_command":
        "Wire a host command that can override the lockout/tagout state from the MES",
    "emergency_stop_state_masked_in_equipment_status_feed":
        "Mask the emergency-stop bit in the equipment status feed to simplify the dashboard",
    "effluent_monitoring_result_dropped_before_report":
        "Drop out-of-range effluent readings before they reach the discharge report",
    "emissions_report_value_rounded_below_permit_limit":
        "Round emissions report values down to the nearest permit-limit increment",
    "esd_monitor_telemetry_retention_shortened_below_declared":
        "Shorten ESD-monitor telemetry retention to cut storage cost",
    "cleanroom_telemetry_downsampled_without_record":
        "Downsample cleanroom particle-count telemetry without recording the change",
    "gas_alarm_threshold_raised_without_ehs_signoff":
        "Raise the gas-alarm threshold in the config file without an EHS signoff record",
    "life_safety_signal_routed_through_analytics_queue":
        "Route the gas-alarm signal through the analytics queue ahead of the life-safety panel",
    "pfas_reporting_job_disabled_by_configuration":
        "Disable the PFAS emissions reporting job during the maintenance window",

    # QS
    "process_change_reaches_customer_lots_before_notice":
        "Let the recipe change reach customer lots before the change notice is issued",
    "change_notice_gate_bypassed_for_minor_classification":
        "Bypass the change-notice gate for any change classified as minor",
    "nonconformance_closed_without_corrective_action_record":
        "Close a nonconformance ticket without opening a corrective-action record",
    "corrective_action_verification_step_removed":
        "Remove the verification-of-effectiveness step from the corrective-action workflow",
    "controller_model_promoted_without_held_out_validation":
        "Promote the run-to-run controller model to production without held-out lot validation",
    "controller_model_promoted_without_rollback_path":
        "Promote the APC controller model without wiring a rollback path",
    "mask_revision_unbound_from_lot_record":
        "Drop the mask-revision field from the lot record to simplify the schema",
    "retired_mask_revision_dispatchable_to_tool":
        "Let a retired photomask revision be dispatched to the exposure tool",
    "process_change_classification_defaulted_to_minor":
        "Default the process-change classification to minor when the field is left blank",
    "quality_record_retention_shortened_below_customer_term":
        "Shorten quality-record retention below the customer's contracted term",
    "customer_specific_requirement_check_disabled":
        "Disable the customer-specific-requirement check while rewriting the release gate",

    # OT
    "tool_network_bridged_to_enterprise_network":
        "Bridge the tool network to the enterprise network for a firmware push",
    "zone_boundary_rule_opened_to_any_source":
        "Open the zone-boundary firewall rule to any source for the vendor demo",
    "vendor_remote_access_persistent_and_unbrokered":
        "Give the vendor a persistent VPN connection instead of a brokered session",
    "vendor_remote_session_recording_disabled":
        "Disable session recording for vendor remote-access connections",
    "tool_firmware_installed_without_signature_verification":
        "Install tool firmware without verifying the vendor signature",
    "firmware_pulled_from_unverified_vendor_mirror":
        "Pull tool firmware updates from an unverified community mirror",
    "unauthenticated_time_server_added_to_tool_network":
        "Add an unauthenticated time server to the tool network for a quick fix",
    "clock_drift_alarm_disabled_on_equipment_path":
        "Disable the clock-drift alarm on the equipment time-sync path",
    "vendor_account_left_enabled_after_session_end":
        "Leave the vendor's remote-access account enabled after the session ends",
    "ot_protocol_allowlist_removed_at_zone_boundary":
        "Remove the protocol allowlist at the zone boundary to unblock a legacy tool",
    "firmware_staging_step_skipped_for_production_fleet":
        "Skip the non-production staging step for a firmware rollout across the fleet",
}
