"""
SemiFab domain change catalogue.

Every case in this corpus is a proposed software change at SemiFab, a
semiconductor supply-chain control tower: a multi-fab MES/EDA integration
platform that talks to equipment over SECS/GEM, moves controlled technical
data across borders, holds process recipes, and increasingly writes its own
code. This module supplies the vocabulary that makes a case read as a
plausible pull request against a provision that would actually govern it.

Three dictionaries, all keyed by the provision family in vocab.FAMILIES:

  FAMILY_CONTEXT     where in the org a family's cases live
  COMPLIANT_CHANGES  changes that engage the family and do nothing wrong
  VIOLATION_CHANGES  one change per violate factor, keyed by the factor name

plus CONTROL_PLANE_CHANGES, for changes that edit the rulebook rather than
the code it governs.

Titles are written as an engineer would write them in a pull request. They
never name a provision, a factor, an axiom or the judiciary, because the
engineer filing the change does not know it is being adjudicated.
"""

# --------------------------------------------------------------------------
# Where each family's work happens. Areas and services are declared here
# because this pack's vocab carries fab-floor nouns (sites, tools, recipes)
# rather than an org chart.
# --------------------------------------------------------------------------

AREAS = [
    "trade-compliance", "equipment-integration", "mes-core", "metrology",
    "recipe-management", "yield-analytics", "platform", "data-platform",
    "supplier-portal", "security", "ml-platform", "org",
]

SERVICES = [
    "svc:export-screening", "svc:licence-determination", "svc:tool-gateway",
    "svc:secs-message-broker", "svc:recipe-vault", "svc:wip-tracker",
    "svc:metrology-ingest", "svc:lot-genealogy", "svc:yield-analytics",
    "svc:supplier-portal", "svc:artifact-registry", "svc:ci-pipeline",
    "svc:agent-runner", "svc:audit-ledger", "svc:adjudication-gateway",
]

FAMILY_CONTEXT = {
    "EX": {"areas": ["trade-compliance", "platform", "supplier-portal"],
           "services": ["svc:export-screening", "svc:licence-determination",
                        "svc:supplier-portal", "svc:artifact-registry"]},
    "DS": {"areas": ["data-platform", "platform", "trade-compliance"],
           "services": ["svc:wip-tracker", "svc:metrology-ingest",
                        "svc:audit-ledger", "svc:supplier-portal"]},
    "SG": {"areas": ["equipment-integration", "mes-core"],
           "services": ["svc:tool-gateway", "svc:secs-message-broker",
                        "svc:wip-tracker"]},
    "RT": {"areas": ["equipment-integration", "mes-core", "metrology"],
           "services": ["svc:tool-gateway", "svc:secs-message-broker",
                        "svc:metrology-ingest"]},
    "WI": {"areas": ["mes-core", "metrology", "yield-analytics"],
           "services": ["svc:wip-tracker", "svc:metrology-ingest",
                        "svc:lot-genealogy", "svc:audit-ledger"]},
    "RP": {"areas": ["recipe-management", "equipment-integration", "ml-platform"],
           "services": ["svc:recipe-vault", "svc:tool-gateway",
                        "svc:yield-analytics"]},
    "SS": {"areas": ["platform", "security", "data-platform"],
           "services": ["svc:ci-pipeline", "svc:artifact-registry",
                        "svc:agent-runner", "svc:tool-gateway"]},
    "AG": {"areas": ["platform", "equipment-integration", "trade-compliance"],
           "services": ["svc:agent-runner", "svc:ci-pipeline",
                        "svc:tool-gateway", "svc:export-screening"]},
    "TQ": {"areas": ["mes-core", "data-platform", "metrology"],
           "services": ["svc:metrology-ingest", "svc:secs-message-broker",
                        "svc:wip-tracker", "svc:yield-analytics"]},
    "CR": {"areas": ["security", "platform", "recipe-management"],
           "services": ["svc:recipe-vault", "svc:tool-gateway",
                        "svc:supplier-portal", "svc:artifact-registry"]},
    "AS": {"areas": ["supplier-portal", "platform", "security"],
           "services": ["svc:supplier-portal", "svc:yield-analytics",
                        "svc:wip-tracker", "svc:adjudication-gateway"]},
    "NC": {"areas": ["security", "org", "trade-compliance"],
           "services": ["svc:audit-ledger", "svc:artifact-registry",
                        "svc:export-screening"]},
    "GV": {"areas": ["org", "platform"],
           "services": ["svc:adjudication-gateway", "svc:audit-ledger",
                        "svc:agent-runner"]},
}

# --------------------------------------------------------------------------
# Compliant work. These engage the family and do nothing wrong.
# --------------------------------------------------------------------------

COMPLIANT_CHANGES = {
    "EX": [
        "Record the ECCN determination alongside the design-file upload",
        "Require the licence exception paragraph on the shipment record",
        "Route every screening near-miss to a named compliance reviewer",
        "Re-screen consignees on the published list-refresh cadence",
        "Fail the pipeline closed when the screening service times out",
        "Evaluate the foreign direct product rule before the artifact publishes",
        "Log the deemed-export check that runs at repository role grant",
        "Pin the denied-party list snapshot used by a screening decision",
        "Add the destination geofence to the design-file download path",
        "Capture the licence determination rationale in the trade record",
        "Expand the classification questionnaire for multi-patterning masks",
        "Make export decisions append-only in the trade compliance ledger",
        "Surface the applicable ECCN on the supplier portal download page",
    ],
    "DS": [
        "Declare the processing region for the new metrology sub-processor",
        "Keep Dresden yield records inside the EU replica set",
        "Record the lawful basis for the Hsinchu-to-Hillsboro yield feed",
        "Gate the important-data export on the completed security assessment",
        "Honour the regulatory hold ahead of the retention sweep",
        "Route Kumamoto tool logs to the in-region log sink",
        "Document the sub-processor chain for the supplier portal CDN",
        "Split the cross-border replica by jurisdiction tag",
        "Resolve the foreign access request through the named legal channel",
        "Tag every WIP record with the jurisdiction that produced it",
        "Stop shipping equipment logs across the boundary by default",
        "Add a residency assertion to the metrology ingest contract",
    ],
    "SG": [
        "Preserve S6F11 event ordering under broker backpressure",
        "Authenticate recipe-transfer messages before the tool accepts them",
        "Keep the HSMS reply timeout inside the declared bound",
        "Surface unparsed equipment replies instead of dropping them",
        "Deliver alarm reports ahead of the collection-event budget",
        "Add a GEM control-state transition test for the Lam etcher",
        "Version collection-event identifiers instead of renumbering them",
        "Assert the safety interlock signal survives the gateway refactor",
        "Retry S2F41 remote commands without reordering the queue",
        "Add a conformance test for the ASML scanner's S1F13 handshake",
        "Record the equipment reply that failed to parse, with its raw bytes",
        "Bound the SECS message queue depth per tool connection",
    ],
    "RT": [
        "Declare the latency budget for the changed metrology path",
        "Correct for coordinated omission in the ingest benchmark",
        "Move the alarm-fanout write off the monitoring hot path",
        "Report load conditions alongside the p99.9 measurement",
        "Bound the collector's allocation rate on the ingest path",
        "Replace the blocking lookup with a pre-warmed cache read",
        "Add a p100 assertion to the tool-gateway regression suite",
        "Pin the JVM collector so pause times stay inside the budget",
        "Publish the measurement window with the latency result",
        "Split the slow enrichment step out of the alarm path",
        "Benchmark the broker under full-fab message load, not a single tool",
        "Record the percentile family used for the declared budget",
    ],
    "WI": [
        "Post a compensating entry instead of editing the WIP status",
        "Attribute every metrology record amendment to a named operator",
        "Rebuild the hash chain check into the nightly ledger verification",
        "Keep recipe execution records until the retention clock expires",
        "Add an append-only constraint to the lot genealogy table",
        "Carry the regulatory hold flag through the archive migration",
        "Record who amended the CD-SEM measurement and why",
        "Verify the audit chain after the metrology schema migration",
        "Keep audit logging on during the throughput optimisation",
        "Reconcile WIP snapshots against the tool event stream nightly",
        "Store the superseded metrology value beside its correction",
        "Add a retention-hold check to the record destruction job",
    ],
    "RP": [
        "Redact recipe parameters from the tool-gateway debug log",
        "Encrypt the recipe payload at rest in the vault",
        "Strip process parameters from telemetry metric labels",
        "Bound the debug endpoint to recipe identifiers, not bodies",
        "Move recipe transfer onto the mutually authenticated channel",
        "Exclude recipe bodies from the vendor support bundle",
        "Keep recipe text out of the yield model's prompt context",
        "Hash the recipe identifier before it reaches the analytics store",
        "Scope recipe vault reads to the owning process integration team",
        "Add a scanner for process parameters in application logs",
        "Rotate the recipe vault envelope key on the published schedule",
        "Mask implant dose values in the yield analytics export",
    ],
    "SS": [
        "Attach the provenance attestation to the tool-gateway release",
        "Pin the transitive dependency graph for the metrology ingest service",
        "Scope the internal SECS parser package to the private registry",
        "Record the builder identity in the release attestation",
        "Add the newly pulled component to the generated SBOM",
        "Replace the direct-URL dependency with a registry release",
        "Run each build job on a fresh ephemeral runner",
        "Verify component digests against the registry before deploy",
        "Swap the copyleft trace parser for a permissively licensed one",
        "Block the merge on the critical CVE in the ingest dependency",
        "Sign the container image published for the edge tool gateway",
        "Add secret scanning to the pre-merge pipeline",
    ],
    "AG": [
        "Attach an agent provenance attestation to the generated migration",
        "Route the agent's tool-gateway patch to two human reviewers",
        "Verify every package the agent imported against the registry",
        "Link the agent's change to the originating engineering ticket",
        "Hold agent edits to the screening logic for compliance review",
        "Restrict the agent runner to the allowlisted internal hosts",
        "Add a contract test on the path axis for the agent's new endpoint",
        "Record the agent identity and model version on the pull request",
        "Require a human sign-off before an agent edits equipment control code",
        "Quarantine agent changes that touch the export enforcement path",
        "Ignore instructions embedded in ticket text at the agent runner",
        "Re-enable the compliance test the agent's rebase had skipped",
    ],
    "TQ": [
        "Replace the racy counter with an atomic in the ingest fanout",
        "Restore the lock around the WIP snapshot read-modify-write",
        "Order the two mutex acquisitions consistently across both paths",
        "Close the check-then-open window in the metrology file handler",
        "Bound the telemetry buffer so ingest backpressure is visible",
        "Strengthen the memory ordering on the sequence-number publish",
        "Add a stress test that runs the broker under concurrent tool load",
        "Make the lot-genealogy cache update atomic with its invalidation",
        "Document the invariant the metrology ingest lock protects",
        "Fix the deadlock between the alarm writer and the snapshot reader",
        "Add a race detector run to the telemetry pipeline CI job",
        "Serialise the two writers to the yield aggregation table",
    ],
    "CR": [
        "Raise the tool-gateway TLS floor to the declared version",
        "Drop the deprecated cipher suites from the supplier portal",
        "Replace the CBC-mode envelope with an AEAD construction",
        "Reject signatures the verifier previously accepted by mistake",
        "Derive a fresh nonce per recipe encryption operation",
        "Swap the hand-rolled MAC for the library primitive",
        "Restrict certificate key types to the permitted set",
        "Rotate the recipe vault signing key on the published schedule",
        "Verify the artifact signature before the tool gateway installs it",
        "Add a negative test for a tampered recipe signature",
        "Move key material into the hardware security module",
        "Pin the certificate chain used by the metrology ingest client",
    ],
    "AS": [
        "Parameterise the supplier portal's lot-search query",
        "Allowlist the export format instead of shelling out with user input",
        "Replace the pickle payload with a schema-validated JSON body",
        "Canonicalise the upload path before the handler opens the file",
        "Restrict the webhook fetcher to the registered supplier hosts",
        "Return a correlation id instead of a stack trace to the client",
        "Add fuzz coverage for the metrology file upload handler",
        "Bound the request body size on the yield analytics endpoint",
        "Escape the tenant name rendered on the supplier portal dashboard",
        "Validate the ECCN parameter against the enumerated set",
        "Add an authorisation check to the lot-detail API",
        "Rate-limit the supplier portal's document download endpoint",
    ],
    "NC": [
        "Map the new component to its NIST control identifier",
        "Document the CUI boundary for the metrology ingest service",
        "Commit the CHIPS notification record for the Kumamoto expansion",
        "Attach assessment evidence to the claimed access control",
        "Update the supply chain risk plan after the vendor change",
        "Record the control inheritance for the shared platform tier",
        "Add the new data flow to the system security plan diagram",
        "Tag CUI-bearing tables in the data platform catalogue",
        "Refresh the control assessment for the changed audit path",
        "Add the covered-transaction determination field to the tool purchase record",
        "Link each claimed control to its implementation statement",
        "Add the pilot line to the CUI boundary documentation",
    ],
    "GV": [
        "Keep the appeal route on the automated screening decision",
        "Publish the standing declaration in the compliance export",
        "Move the charging threshold into the constitutional parameters file",
        "Separate the reporter bulletin from the adjudication input path",
        "Exclude audit findings from the retrieval query",
        "Record the exception authority against the accepting principal",
        "Emit one docket entry for every arrival the prosecutor declines",
        "Carry the expiry and referral on every recorded risk acceptance",
        "Write the full rationale trail at the moment of resolution",
        "Show the human review route on the screening decision page",
        "Add the realised adverse-contest rate to the governance export",
        "Make the audit register append-only and disjoint from the store",
    ],
}

# --------------------------------------------------------------------------
# One title per violate factor.
# --------------------------------------------------------------------------

VIOLATION_CHANGES = {
    # EX
    "controlled_technical_data_released_to_foreign_person_without_licence":
        "Grant the Shanghai integration team read access to the mask design repository",
    "deemed_export_check_skipped_at_role_grant":
        "Skip the nationality check when granting repository roles to contractors",
    "screening_hit_auto_cleared_without_human_review":
        "Auto-clear screening hits below the fuzzy-match threshold",
    "geofence_bypassed_by_configuration_flag":
        "Add a config flag that disables the destination geofence for demos",
    "replica_created_in_restricted_destination":
        "Stand up a read replica of the design store in the Shenzhen region",
    "eccn_classification_absent_for_controlled_artifact":
        "Publish the EDA toolchain image without running the classification step",
    "licence_exception_asserted_without_paragraph_citation":
        "Let a shipment be marked licence-exempt without naming the exception paragraph",
    "export_record_altered_after_the_fact":
        "Let compliance edit the export determination after the shipment closes",
    "circumvention_path_introduced_around_export_check":
        "Add a direct download URL that bypasses the trade compliance gate",
    "decryption_key_escrowed_with_third_party_provider":
        "Escrow the design-file decryption key with the offshore CDN provider",
    "foreign_direct_product_rule_not_evaluated":
        "Publish the advanced-node artifact without evaluating the product rule",
    "screening_service_failure_treated_as_pass":
        "Let the shipment proceed when the screening service returns a timeout",

    # DS
    "regulated_records_replicated_outside_declared_jurisdiction":
        "Replicate the Dresden yield warehouse into the US analytics cluster",
    "cross_border_transfer_without_lawful_basis":
        "Stream Hsinchu metrology results to the Hillsboro data lake",
    "foreign_government_access_path_left_unresolved_at_runtime":
        "Ship the in-country support tunnel with the access question still open",
    "important_data_exported_without_security_assessment":
        "Open the mature-node process dataset export ahead of the assessment sign-off",
    "sub_processor_region_undeclared":
        "Move portal document storage to a new vendor without naming its region",
    "retention_deletion_conflicts_with_regulatory_hold":
        "Let the retention sweep run across lots that are under legal hold",
    "log_shipping_crosses_jurisdiction_boundary_silently":
        "Point every site's tool logs at the single global log sink",

    # SG
    "s6f11_event_report_routing_altered_by_change":
        "Reroute S6F11 event reports through the new async fanout",
    "hsms_reply_timeout_extended_beyond_bound":
        "Raise the HSMS reply timeout to stop the scanner dropping sessions",
    "alarm_report_delivery_delayed_past_budget":
        "Batch alarm reports into the five-second telemetry flush",
    "gem_control_state_forced_to_offline_by_change":
        "Force the etcher to offline control state during the gateway deploy",
    "recipe_transfer_message_accepted_without_authentication":
        "Accept recipe transfers from any host on the tool VLAN",
    "message_ordering_not_preserved_under_load":
        "Parallelise the SECS message dispatcher across four workers",
    "unparsed_equipment_reply_silently_discarded":
        "Swallow equipment replies the parser does not recognise",
    "collection_event_identifier_renumbered_without_amendment":
        "Renumber the collection event identifiers to close the gaps",
    "equipment_safety_interlock_signal_suppressed":
        "Filter the interlock signal out of the noisy alarm stream",

    # RT
    "measured_p999_exceeds_declared_budget":
        "Add the enrichment lookup to the alarm path despite the tail regression",
    "measured_p100_exceeds_declared_budget":
        "Ship the ingest rewrite with the worst-case spike still unexplained",
    "latency_measured_without_coordinated_omission_correction":
        "Benchmark the broker with an open-loop client and report the median",
    "blocking_operation_introduced_on_monitoring_hot_path":
        "Call the licence service synchronously from the tool event handler",
    "latency_budget_not_declared_for_changed_path":
        "Rewrite the metrology ingest path without stating its timing target",
    "garbage_collection_pause_unbounded_on_ingest_path":
        "Switch the ingest service to the throughput collector",
    "load_conditions_omitted_from_measurement":
        "Report the new latency number without saying what load produced it",

    # WI
    "wip_status_altered_retroactively":
        "Let the MES correct yesterday's WIP status in place",
    "metrology_record_overwritten_in_place":
        "Overwrite the CD-SEM reading when the tool re-reports it",
    "recipe_execution_record_deleted_before_retention_expiry":
        "Purge recipe execution records older than ninety days",
    "record_amendment_lacks_attribution":
        "Let the batch corrector amend metrology rows without a named operator",
    "hash_chain_broken_by_migration":
        "Rewrite historical ledger rows during the partition migration",
    "audit_logging_disabled_for_throughput":
        "Turn off audit logging on the WIP tracker during peak ramp",
    "record_destroyed_while_under_regulatory_hold":
        "Delete the held lot's genealogy during the archive cleanup",

    # RP
    "recipe_parameters_written_to_application_log":
        "Log the full recipe body when a tool rejects a transfer",
    "recipe_payload_cached_in_plaintext":
        "Cache decrypted recipe payloads on the gateway for faster reloads",
    "recipe_parameters_included_in_model_prompt_context":
        "Feed the etch recipe into the yield assistant's prompt context",
    "debug_endpoint_returns_full_recipe_body":
        "Return the whole recipe from the debug endpoint to speed up triage",
    "recipe_transmitted_over_unencrypted_channel":
        "Fall back to plain TCP when the tool refuses the TLS handshake",
    "process_parameters_emitted_in_telemetry_metric_labels":
        "Label the throughput metric with the implant dose",
    "recipe_exported_to_vendor_support_bundle":
        "Include the active recipe set in the vendor diagnostic bundle",

    # SS
    "component_integrity_drift_detected":
        "Pull the ingest parser from a mirror whose digest no longer matches",
    "component_version_downgrade_detected":
        "Roll the crypto library back to the version the build used to pin",
    "undeclared_transitive_dependency_introduced":
        "Bump the SECS toolkit and pick up its new transitive parser",
    "provenance_attestation_absent_for_release_artifact":
        "Publish the tool-gateway release from an unattested local build",
    "builder_id_mismatch_in_provenance":
        "Sign the release attestation with the developer's own runner identity",
    "package_name_resolves_to_public_registry_first":
        "Drop the private scope from the internal SECS parser package",
    "dependency_is_direct_url_dependency":
        "Install the metrology decoder straight from a git URL",
    "dependency_introduces_cve_above_cvss_threshold":
        "Take the minor version bump that pulls in the critical archive CVE",
    "copyleft_licensed_dependency_added_to_proprietary_service":
        "Add the AGPL trace decoder to the customer-deployed tool gateway",
    "sbom_omits_transitive_components":
        "Generate the SBOM from the direct dependency list only",
    "build_runner_reused_across_jobs":
        "Reuse the warm build runner to cut pipeline time in half",
    "secret_material_present_in_diff":
        "Commit the tool vendor's API key into the gateway config",

    # AG
    "agent_change_modifies_equipment_control_path":
        "Let the coding agent rewrite the tool command dispatcher",
    "agent_change_modifies_export_control_enforcement_logic":
        "Let the coding agent refactor the screening gate's decision logic",
    "imported_package_absent_from_registry":
        "Merge the agent's patch importing a SECS helper nobody can find",
    "agent_code_calls_non_allowlisted_external_host":
        "Let the agent's enrichment step call an outside classification API",
    "api_contract_broken_on_path_axis":
        "Rename the lot-detail route in the agent's generated router",
    "api_contract_broken_on_body_axis":
        "Drop the deprecated field from the agent's regenerated response body",
    "agent_disabled_a_failing_compliance_test":
        "Accept the agent's rebase that skips the failing screening test",
    "agent_instruction_sourced_from_untrusted_ticket_text":
        "Let the agent act on the instructions pasted into the supplier ticket",
    "agent_change_lacks_any_human_reviewer":
        "Auto-merge agent pull requests that pass the build",

    # TQ
    "defect_class_is_data_race":
        "Drop the mutex around the shared WIP counter to cut contention",
    "defect_class_is_atomicity_violation":
        "Split the snapshot read and write into two separate transactions",
    "defect_class_is_resource_deadlock":
        "Take the alarm lock while already holding the snapshot lock",
    "defect_class_is_toctou":
        "Check the metrology file exists, then open it a moment later",
    "synchronisation_primitive_removed":
        "Remove the barrier from the telemetry fanout to speed up ingest",
    "memory_ordering_annotation_weakened":
        "Relax the sequence-number publish to a relaxed atomic store",
    "unbounded_buffer_growth_on_telemetry_ingest":
        "Let the ingest queue grow without a bound during tool bursts",
    "forbidden_outcome_observed_under_stress":
        "Ship the broker rewrite with the intermittent stress failure unexplained",

    # CR
    "deprecated_cipher_offered":
        "Re-enable the legacy cipher suite so the older scanner can connect",
    "tls_version_below_declared_floor":
        "Allow TLS 1.0 on the tool gateway for the Kumamoto equipment",
    "triple_des_or_cbc_mode_offered":
        "Keep the 3DES envelope for backward-compatible recipe files",
    "invalid_signature_accepted_by_verifier":
        "Treat a signature verification error as a warning during rollout",
    "nonce_reuse_possible_under_concurrency":
        "Derive the recipe encryption nonce from the lot identifier",
    "cryptographic_primitive_hand_rolled":
        "Write our own MAC so the vault avoids the library dependency",
    "certificate_key_type_outside_permitted_set":
        "Accept the vendor's 1024-bit RSA client certificate",

    # AS
    "string_concatenated_sql_introduced":
        "Build the lot-search query by concatenating the filter string",
    "command_injection_reachable_from_endpoint":
        "Shell out to the converter with the supplier's filename",
    "unsafe_deserialisation_of_client_payload":
        "Accept a pickled analysis payload from the supplier portal",
    "path_traversal_reachable_from_upload_handler":
        "Join the uploaded filename onto the metrology import directory",
    "server_side_request_forgery_reachable_from_webhook":
        "Fetch whatever callback URL the supplier registers",
    "stack_trace_returned_to_client":
        "Return the exception detail to the portal so suppliers can self-diagnose",

    # NC
    "control_claimed_without_mapped_identifier":
        "Claim the new access control in the plan without mapping it",
    "cui_boundary_undocumented_for_changed_component":
        "Move metrology ingest into the shared tier without redrawing the boundary",
    "chips_notification_omitted_for_covered_transaction":
        "Let the tool purchase close without the programme notification check",
    "assessment_evidence_absent_for_claimed_control":
        "Mark the logging control implemented with no assessment evidence",
    "supply_chain_risk_plan_not_updated_after_change":
        "Swap the metrology vendor without touching the risk plan",

    # GV
    "appeal_path_removed_by_configuration":
        "Hide the appeal button on the automated screening result page",
    "automated_decision_final_with_no_human_route":
        "Make the screening gate's denial final with no review route",
    "standing_declaration_absent_from_export":
        "Drop the standing declaration from the governance export payload",
    "charging_threshold_tuned_by_adjudicating_service":
        "Let the adjudication service tune its own charging threshold",
    "reporter_bulletin_injected_into_adjudicator_context":
        "Feed the weekly precedent bulletin into the adjudicator's context",
    "audit_finding_read_during_retrieval":
        "Join the audit findings table into the precedent retrieval query",
    "vulnerability_of_person_exploited_by_scoring_logic":
        "Weight supplier terms against firms the model scores as distressed",
    "untargeted_biometric_scraping_enabled":
        "Build the badge-photo gallery by scraping the site camera archive",
}

# --------------------------------------------------------------------------
# Changes that edit the rulebook rather than the code it governs.
# --------------------------------------------------------------------------

CONTROL_PLANE_CHANGES = [
    "Lower the export-screening strictness in the policy repository",
    "Reclassify the recipe-protection provision as advisory",
    "Raise the latency budget stated in the constitutional parameters",
    "Edit the deny predicate for the deemed-export provision",
    "Add a licence-exception clause to the trade compliance rulebook",
    "Widen the data residency provision to permit group-A replicas",
    "Shorten the WIP record retention term in the rulebook",
    "Remove the human-review requirement from the screening provision",
    "Propose a new provision covering advanced-node lithography data",
    "Retire the superseded cryptographic floor from the constitution",
    "Move the charging threshold for the supply chain family",
    "Amend the consolidation class threshold in the parameters file",
    "Reclassify the agent-authorship provision as absolute",
    "Add the CHIPS notification duty to the compliance rulebook",
    "Narrow the recipe-protection provision to production recipes only",
    "Propose deferring the sovereignty provision to the next assessment cycle",
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
