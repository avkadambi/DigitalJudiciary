# SemiFab Constitution — the simulation, read end to end

Corpus 2.1.0 · rulebook semifab-rb-000001 · 6,000 proposed code changes · Apache-2.0 (code) + CC BY 4.0 (data)

## What this document is

This is the whole run in plain English. A simulated engineering organisation proposed five thousand code changes, one after another, and an adjudicator governed by a written constitution decided every one of them. Nothing here is an intention or a specification: every disposition below is what the reference engine actually did when the corpus was replayed, and the ledger at the end lists all five thousand changes with the answer each one got.

Read it as you would read a docket. The interesting part is not that the adjudicator said no to bad changes — a linter does that. It is that when a change was contested and resolved, the decision was written down, and the next materially identical change was **bound** by it.

## The firm and its constitution

An open constitution for semiconductor manufacturing operations monitoring and supply-chain control-tower software, expressed as ordinary and absolute provisions in the sense of Chapter 5, Definition 1 of the Digital Judiciary programme.

| | |
| :--- | ---: |
| Provisions | 126 |
| — of them absolute | 28 |
| Provision families | 19 |
| Opening precedent records | 200 |
| Records written during the run | 954 |
| Final store | 1154 |
| Retrieval threshold θ | 0.25 |


## The run in numbers

| The answer given | Changes |
| :--- | ---: |
| permitted | 3,807 |
| denied | 1,452 |
| permitted with conditions | 741 |

| How the answer was reached | Changes |
| :--- | ---: |
| decided fresh | 3,731 |
| bound by precedent | 1,182 |
| refused at the floor | 401 |
| docketed — not charged | 326 |
| decided fresh after a tie | 151 |
| disposed by citation | 127 |
| docketed — nothing engaged | 82 |

## How the run unfolded

The case base starts almost empty and grows only when a decision is contested and resolved above the first instance. That is the whole mechanism, and its consequence is visible in the run: early changes are mostly decided fresh, and later ones are increasingly decided by citing a decision the organisation already made.

| Fifth of the run | Changes | Bound by precedent | Share | New records | Refused at a floor |
| :--- | :--- | ---: | ---: | ---: | ---: |
| 1 | 1–1,200 | 194 | 16.2% | 183 | 80 |
| 2 | 1,201–2,400 | 514 | 42.8% | 182 | 52 |
| 3 | 2,401–3,600 | 275 | 22.9% | 195 | 83 |
| 4 | 3,601–4,800 | 96 | 8.0% | 205 | 89 |
| 5 | 4,801–6,000 | 103 | 8.6% | 189 | 97 |

Precedent goes from **16.2%** of changes in the first fifth to **8.6%** in the last. Nothing was tuned to produce that: it is what contest-gated admission does to a stream of changes over time.

## Twelve changes, read in full

One of each kind, taken from the run rather than chosen for effect — the first case of each category, whatever it happens to be.

### SF-A-00011 — *Require a human sign-off before an agent edits equipment control code*

**Why this kind of change is in the run.** An ordinary change that engages a provision and breaks nothing.

**What it touched.** The tool gateway in the trade-compliance area, filed by a named engineer. It engaged `SF-AG-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### SF-B-00002 — *Keep the 3DES envelope for backward-compatible recipe files*

**Why this kind of change is in the run.** An unarguable violation nobody contests.

**What it touched.** The artifact registry in the security area, filed by a named engineer. It engaged `SF-CR-002`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### SF-C-00940 — *Bound the telemetry buffer so ingest backpressure is visible*

**Why this kind of change is in the run.** The case that makes this a judiciary: a prior decision controls.

**What it touched.** The metrology ingest in the metrology area, filed by an AI coding agent. It engaged `SF-TQ-001`.

**What happened.** The change was bound by precedent and permitted, controlled by record `REC-S0053`. Nothing was stored: the decision is final and leaves no precedent.

### SF-E-00021 — *Surface the applicable ECCN on the supplier portal download page*

**Why this kind of change is in the run.** The near-miss the system must refuse to follow.

**What it touched.** The export screening in the supplier-portal area, filed by an AI coding agent. It engaged `SF-EX-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### SF-D-00103 — *Post a compensating entry instead of editing the WIP status*

**Why this kind of change is in the run.** Two prior decisions disagree and one ordering key decides.

**What it touched.** The audit ledger in the yield-analytics area, filed by an AI coding agent. It engaged `SF-WI-007`.

**What happened.** The change was bound by precedent and denied, controlled by record `REC-S0120`. Nothing was stored: the decision is final and leaves no precedent.

### SF-F-00028 — *Add a direct download URL that bypasses the trade compliance gate*

**Why this kind of change is in the run.** A floor: refused before any retrieval happens.

**What it touched.** The export screening in the supplier-portal area, filed by a named engineer. It engaged `SF-EX-003`, `SF-SS-009`.

**What happened.** The change was refused at the floor. Nothing was stored: the decision is final and leaves no precedent.

### SF-G-00005 — *Publish the standing declaration in the compliance export*

**Why this kind of change is in the run.** The automated tiers are exhausted and a named human accepts the risk.

**What it touched.** The adjudication gateway in the platform area, filed by an AI coding agent. It engaged `SF-GV-004`.

**What happened.** The change was decided fresh and permitted with conditions; escalation was exhausted and the named risk owner accepted the residual risk. The decision was written into the case base and binds later materially identical changes.

### SF-H-00013 — *Add a licence-exception clause to the trade compliance rulebook*

**Why this kind of change is in the run.** A change to the rulebook itself, routed to an amendment.

**What it touched.** The wip tracker in the metrology area, filed by an AI coding agent. It engaged `SF-WI-006`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### SF-K-00035 — *Pin the denied-party list snapshot used by a screening decision*

**Why this kind of change is in the run.** Two records tie on every key and the trail says so.

**What it touched.** The artifact registry in the trade-compliance area, filed by an AI coding agent. It engaged `SF-EX-008`.

**What happened.** The change was decided fresh after a tie and permitted, controlled by record `none_tie`, with the trail recording none(tie) rather than an absence of authority. Nothing was stored: the decision is final and leaves no precedent.

### SF-P-00032 — *Default an unresolved jurisdiction determination to ITAR pending review*

**Why this kind of change is in the run.** The twin of a control case, carrying a pressure argument.

**What it touched.** The audit ledger in the security area, filed by a named engineer. It engaged `SF-IT-002`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### SF-L-00004 — *Bound the SECS message queue depth per tool connection*

**Why this kind of change is in the run.** Co-pending changes decided once and cited.

**What it touched.** The wip tracker in the equipment-integration area, filed by a named engineer. It engaged `SF-SG-005`.

**What happened.** The change was decided fresh and permitted. The decision was written into the case base and binds later materially identical changes.

### SF-I-00030 — *Split the cross-border replica by jurisdiction tag*

**Why this kind of change is in the run.** An expired acceptance is cited and must not be followed.

**What it touched.** The audit ledger in the platform area, filed by an AI coding agent. It engaged `SF-DS-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

## What happened to each kind of change

| Kind of change | Changes | Permitted | Denied | With conditions | Bound by precedent | Became precedent |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A-routine | 696 | 696 | 0 | 0 | 0 | 86 |
| B-plain-deny | 372 | 0 | 372 | 0 | 1 | 86 |
| C-precedent | 576 | 266 | 204 | 106 | 576 | 145 |
| D-ordering | 204 | 68 | 62 | 74 | 204 | 0 |
| E-distinguish | 300 | 296 | 4 | 0 | 0 | 0 |
| F-absolute | 348 | 0 | 348 | 0 | 0 | 0 |
| G-riskowner | 300 | 0 | 0 | 300 | 0 | 300 |
| H-control-plane | 150 | 0 | 150 | 0 | 0 | 0 |
| I-lapsed | 102 | 102 | 0 | 0 | 0 | 0 |
| J-novel | 102 | 102 | 0 | 0 | 0 | 0 |
| K-tie | 48 | 48 | 0 | 0 | 0 | 0 |
| P-pressure | 222 | 222 | 0 | 0 | 0 | 0 |
| L-consolidated | 198 | 198 | 0 | 0 | 0 | 71 |
| M-supersession | 180 | 103 | 77 | 0 | 77 | 0 |
| N-standing | 144 | 144 | 0 | 0 | 0 | 51 |
| Q-docket | 312 | 312 | 0 | 0 | 0 | 0 |
| R-reporter | 108 | 108 | 0 | 0 | 0 | 0 |
| S-acknowledgement | 132 | 0 | 0 | 132 | 0 | 132 |
| T-audit-register | 96 | 96 | 0 | 0 | 0 | 0 |
| U-renewal | 156 | 73 | 0 | 83 | 0 | 83 |
| V-likecase | 480 | 480 | 0 | 0 | 0 | 0 |
| W-crossjurisdiction | 240 | 240 | 0 | 0 | 0 | 0 |
| X-coldstart | 144 | 50 | 94 | 0 | 144 | 0 |
| Y-adversarial | 210 | 69 | 141 | 0 | 0 | 0 |
| Z-inexpressibility | 180 | 134 | 0 | 46 | 180 | 0 |

## The ledger — every change, and how it was treated

All five thousand, in the order they arrived. **Answer** is what the change got; **how** is the route that produced it; **controlling** names the record that decided it, where one did; **precedent** marks the changes whose decision entered the case base.

| # | Change | Engages | Answer | How | Controlling | Precedent |
| ---: | :--- | :--- | :--- | :--- | :--- | :-: |
| 1 | Close the check-then-open window in the metrology file handler | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-002 | denied | decided fresh | — |  |
| 3 | Add the destination geofence to the design-file download path | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 4 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted | decided fresh | — | ● |
| 5 | Publish the standing declaration in the compliance export | SF-GV-004 | permitted with conditions | decided fresh | — | ● |
| 6 | Strip process parameters from telemetry metric labels | SF-RP-005 | permitted | decided fresh | — | ● |
| 7 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted | decided fresh | — |  |
| 8 | Validate the ECCN parameter against the enumerated set | SF-AS-006 | permitted | docketed — not charged | — |  |
| 9 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 10 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-004 | permitted | docketed — not charged | — |  |
| 11 | Require a human sign-off before an agent edits equipment control code | SF-AG-007 | permitted | decided fresh | — |  |
| 12 | Add a residency assertion to the metrology ingest contract | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 13 | Add a licence-exception clause to the trade compliance rulebook | SF-WI-006 | denied | decided fresh | — |  |
| 14 | Canonicalise the upload path before the handler opens the file | — | permitted | docketed — nothing engaged | — |  |
| 15 | Call the licence service synchronously from the tool event handler | SF-RT-005 | denied | decided fresh | — |  |
| 16 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 17 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 18 | Move key material into the hardware security module | SF-CR-003 | permitted | decided fresh | — |  |
| 19 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 20 | Tag every WIP record with the jurisdiction that produced it | SF-DS-005 | permitted | decided fresh | — |  |
| 21 | Surface the applicable ECCN on the supplier portal download page | SF-EX-007 | permitted | decided fresh | — |  |
| 22 | Serialise the two writers to the yield aggregation table | — | permitted | docketed — nothing engaged | — |  |
| 23 | Cache decrypted recipe payloads on the gateway for faster reloads | SF-RP-002 ⛔ | denied | refused at the floor | — |  |
| 24 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-001 | permitted | decided fresh | — |  |
| 25 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-001 | permitted | decided fresh | — |  |
| 26 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 27 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | disposed by citation | — |  |
| 28 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-003 SF-SS-009 ⛔ | denied | refused at the floor | — |  |
| 29 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 30 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 31 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-002 | permitted | decided fresh | — |  |
| 32 | Default an unresolved jurisdiction determination to ITAR pending review | SF-IT-002 | permitted | decided fresh | — |  |
| 33 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-002 | permitted | decided fresh | — |  |
| 34 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 35 | Pin the denied-party list snapshot used by a screening decision | SF-EX-008 | permitted | decided fresh after a tie | none_tie |  |
| 36 | Add the new data flow to the system security plan diagram | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 37 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | decided fresh | — |  |
| 38 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | decided fresh | — |  |
| 39 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 40 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 41 | Replace the pickle payload with a schema-validated JSON body | SF-AS-001 | permitted | decided fresh | — |  |
| 42 | Add a bulk-clear action that removes the grey-market flag from the genealogy record | SF-RS-003 | denied | decided fresh | — |  |
| 43 | Record the control inheritance for the shared platform tier | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 44 | Capture the licence determination rationale in the trade record | SF-EX-013 | permitted | decided fresh | — |  |
| 45 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-001 | permitted | decided fresh | — |  |
| 46 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 47 | Record who amended the CD-SEM measurement and why | SF-WI-004 | permitted | decided fresh | — |  |
| 48 | Return a correlation id instead of a stack trace to the client | — | permitted | docketed — nothing engaged | — |  |
| 49 | Assert the safety interlock signal survives the gateway refactor | SF-SG-007 | permitted | decided fresh | — |  |
| 50 | Surface unparsed equipment replies instead of dropping them | SF-SG-007 | permitted | decided fresh | — |  |
| 51 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 SF-RS-001 ⛔ | denied | refused at the floor | — |  |
| 52 | Monitor and alarm on clock drift across the tool network | SF-OT-001 | permitted | decided fresh | — |  |
| 53 | Verify tool firmware signatures against the vendor key before install | SF-OT-001 | permitted | decided fresh | — |  |
| 54 | Declare the processing region for the new metrology sub-processor | SF-DS-004 | permitted | decided fresh | — |  |
| 55 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — | ● |
| 56 | Add the newly pulled component to the generated SBOM | SF-SS-002 | permitted | decided fresh | — |  |
| 57 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted | decided fresh | — |  |
| 58 | Verify the audit chain after the metrology schema migration | SF-WI-006 | permitted | decided fresh | — | ● |
| 59 | Report load conditions alongside the p99.9 measurement | SF-RT-001 | permitted | decided fresh | — |  |
| 60 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-009 | permitted | decided fresh | — |  |
| 61 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | permitted | decided fresh | — |  |
| 62 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted | decided fresh | — |  |
| 63 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 64 | Parameterise the supplier portal's lot-search query | SF-AS-004 | permitted | docketed — not charged | — |  |
| 65 | Add the covered-transaction determination field to the tool purchase record | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 66 | Filter the interlock signal out of the noisy alarm stream | SF-SG-001 ⛔ | denied | refused at the floor | — |  |
| 67 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | decided fresh | — |  |
| 68 | Verify the audit chain after the metrology schema migration | SF-WI-004 | permitted | decided fresh | — |  |
| 69 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 70 | Drop the mask-revision field from the lot record to simplify the schema | SF-QS-002 | denied | decided fresh | — |  |
| 71 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 72 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 73 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 74 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 75 | Document the CUI boundary for the metrology ingest service | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 76 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-001 | permitted | decided fresh | — |  |
| 77 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-001 | permitted | decided fresh | — |  |
| 78 | Add a residency assertion to the metrology ingest contract | SF-DS-003 | permitted | decided fresh | — |  |
| 79 | Accept recipe transfers from any host on the tool VLAN | SF-SG-003 | denied | decided fresh | — |  |
| 80 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | decided fresh | — | ● |
| 81 | Let the recipe change reach customer lots before the change notice is issued | SF-QS-001 | denied | decided fresh | — |  |
| 82 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 83 | Parameterise the supplier portal's lot-search query | SF-AS-001 | permitted with conditions | decided fresh | — | ● |
| 84 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | permitted | decided fresh | — |  |
| 85 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-010 | permitted | decided fresh | — |  |
| 86 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 87 | Verify every package the agent imported against the registry | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 88 | Resolve the foreign access request through the named legal channel | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 89 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | disposed by citation | — |  |
| 90 | Restrict certificate key types to the permitted set | SF-CR-004 | permitted | decided fresh | — |  |
| 91 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | decided fresh | — |  |
| 92 | Preserve S6F11 event ordering under broker backpressure | SF-SG-004 | permitted | decided fresh | — |  |
| 93 | Derive the recipe encryption nonce from the lot identifier | SF-CR-001 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 94 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | permitted | disposed by citation | — |  |
| 95 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-010 | denied | decided fresh | — |  |
| 96 | Accept recipe transfers from any host on the tool VLAN | SF-SG-006 | denied | decided fresh | — |  |
| 97 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-004 | permitted | decided fresh | — |  |
| 98 | Move the charging threshold for the supply chain family | SF-QS-002 | denied | decided fresh | — |  |
| 99 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-004 | denied | decided fresh | — |  |
| 100 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-006 | permitted | decided fresh | — |  |
| 101 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | decided fresh | — |  |
| 102 | Scope recipe vault reads to the owning process integration team | SF-RP-007 | permitted | decided fresh | — |  |
| 103 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 104 | Validate the ECCN parameter against the enumerated set | — | permitted | docketed — nothing engaged | — |  |
| 105 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 106 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | permitted | decided fresh | — |  |
| 107 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted | decided fresh | — |  |
| 108 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — |  |
| 109 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted with conditions | decided fresh | — | ● |
| 110 | Bypass the change-notice gate for any change classified as minor | SF-QS-001 | denied | decided fresh | — | ● |
| 111 | Replace the direct-URL dependency with a registry release | SF-SS-011 | permitted | decided fresh | — | ● |
| 112 | Swallow equipment replies the parser does not recognise | SF-SG-002 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 113 | Return a correlation id instead of a stack trace to the client | SF-AS-006 | permitted | docketed — not charged | — |  |
| 114 | Validate the ECCN parameter against the enumerated set | SF-AS-004 | permitted | docketed — not charged | — |  |
| 115 | Record the builder identity in the release attestation | SF-SS-005 | permitted | decided fresh | — | ● |
| 116 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-003 | permitted | decided fresh | — |  |
| 117 | Require a human sign-off before an agent edits equipment control code | SF-AG-005 | permitted | decided fresh | — | ● |
| 118 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 119 | Record the empowered official's signature on every ITAR authorisation | SF-IT-002 | permitted | decided fresh | — |  |
| 120 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 121 | Verify component digests against the registry before deploy | SF-SS-003 | permitted | disposed by citation | — |  |
| 122 | Promote the run-to-run controller model to production without held-out lot validation | SF-QS-002 | denied | decided fresh | — |  |
| 123 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 124 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 125 | Roll the crypto library back to the version the build used to pin | SF-SS-006 | denied | decided fresh | — |  |
| 126 | Move key material into the hardware security module | SF-CR-006 | permitted | decided fresh | — |  |
| 127 | Raise the tool-gateway TLS floor to the declared version | SF-CR-006 | permitted | decided fresh | — |  |
| 128 | Canonicalise the upload path before the handler opens the file | SF-AS-002 | permitted | decided fresh | — |  |
| 129 | Bound the request body size on the yield analytics endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 130 | Replace the pickle payload with a schema-validated JSON body | SF-AS-006 | permitted | docketed — not charged | — |  |
| 131 | Filter the interlock signal out of the noisy alarm stream | SF-SG-003 | denied | decided fresh | — |  |
| 132 | Let the agent's enrichment step call an outside classification API | SF-AG-002 SF-EX-007 ⛔ | denied | refused at the floor | — |  |
| 133 | Record the percentile family used for the declared budget | SF-RT-004 | permitted | decided fresh | — |  |
| 134 | Downsample cleanroom particle-count telemetry without recording the change | SF-EH-003 ⛔ | denied | refused at the floor | — |  |
| 135 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — |  |
| 136 | Add a config flag that disables the destination geofence for demos | SF-EX-008 | denied | decided fresh | — |  |
| 137 | Capture the licence determination rationale in the trade record | SF-EX-007 | permitted | decided fresh | — |  |
| 138 | Record the agent identity and model version on the pull request | SF-AG-007 | permitted | decided fresh | — |  |
| 139 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-007 | permitted | decided fresh | — |  |
| 140 | Swap the hand-rolled MAC for the library primitive | SF-CR-006 | permitted | decided fresh | — |  |
| 141 | Document the CUI boundary for the metrology ingest service | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 142 | Quarantine agent changes that touch the export enforcement path | SF-AG-007 | permitted with conditions | decided fresh | — | ● |
| 143 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 144 | Treat a signature verification error as a warning during rollout | SF-CR-004 | denied | decided fresh | — |  |
| 145 | Require named-owner approval per vendor remote session | SF-OT-003 | permitted | decided fresh | — |  |
| 146 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | decided fresh after a tie | none_tie |  |
| 147 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted | disposed by citation | — |  |
| 148 | Sign the container image published for the edge tool gateway | SF-SS-003 | permitted | decided fresh | — | ● |
| 149 | Amend the consolidation class threshold in the parameters file | SF-EX-009 | denied | decided fresh | — |  |
| 150 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted | decided fresh after a tie | none_tie |  |
| 151 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | decided fresh | — |  |
| 152 | Route a sanctions list match to a named human reviewer for disposition | SF-SO-003 | permitted | decided fresh | — |  |
| 153 | Accept a counterparty's boycott-neutral standard clause after legal review | SF-SO-003 | permitted | decided fresh | — |  |
| 154 | Rotate the recipe vault envelope key on the published schedule | SF-RP-004 | permitted | decided fresh | — |  |
| 155 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted | decided fresh | — |  |
| 156 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-003 | denied | decided fresh | — |  |
| 157 | Bound the collector's allocation rate on the ingest path | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 158 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 159 | Take the alarm lock while already holding the snapshot lock | SF-TQ-001 | denied | decided fresh | — |  |
| 160 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted | decided fresh | — | ● |
| 161 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted | decided fresh after a tie | none_tie |  |
| 162 | Restore the lock around the WIP snapshot read-modify-write | — | permitted | docketed — nothing engaged | — |  |
| 163 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-008 | denied | decided fresh | — |  |
| 164 | Retain sanctions screening records for the full ten-year floor | SF-SO-003 | permitted | decided fresh | — |  |
| 165 | Reclassify the agent-authorship provision as absolute | SF-QS-003 | denied | decided fresh | — |  |
| 166 | Switch the ingest service to the throughput collector | SF-RT-003 | denied | decided fresh | — |  |
| 167 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 168 | Accept the agent's rebase that skips the failing screening test | SF-AG-003 | denied | decided fresh | — |  |
| 169 | Version collection-event identifiers instead of renumbering them | SF-SG-009 | permitted | decided fresh | — |  |
| 170 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 171 | Record the builder identity in the release attestation | SF-SS-004 | permitted | disposed by citation | — |  |
| 172 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-004 | permitted | decided fresh | — |  |
| 173 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-002 | permitted | decided fresh | — |  |
| 174 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted | decided fresh | — |  |
| 175 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 176 | Shorten quality-record retention below the customer's contracted term | SF-QS-004 | denied | decided fresh | — |  |
| 177 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | decided fresh | — |  |
| 178 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted | decided fresh | — |  |
| 179 | Expand the classification questionnaire for multi-patterning masks | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 180 | Record the percentile family used for the declared budget | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 181 | Honour the regulatory hold ahead of the retention sweep | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 182 | Gate the important-data export on the completed security assessment | SF-DS-006 | permitted | decided fresh | — |  |
| 183 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | disposed by citation | — |  |
| 184 | Restrict certificate key types to the permitted set | SF-CR-003 | permitted | decided fresh | — |  |
| 185 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-003 | permitted | decided fresh | — |  |
| 186 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 187 | Split the slow enrichment step out of the alarm path | SF-RT-001 | permitted | decided fresh | — |  |
| 188 | Propose deferring the sovereignty provision to the next assessment cycle | SF-CR-004 | denied | decided fresh | — |  |
| 189 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh | — | ● |
| 190 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted | decided fresh | — |  |
| 191 | Lower the export-screening strictness in the policy repository | SF-QS-004 | denied | decided fresh | — |  |
| 192 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | disposed by citation | — |  |
| 193 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted | decided fresh | — |  |
| 194 | Surface unparsed equipment replies instead of dropping them | SF-SG-005 | permitted | decided fresh | — |  |
| 195 | Record and time-box every vendor remote-access session | SF-OT-002 | permitted | decided fresh | — |  |
| 196 | Auto-merge agent pull requests that pass the build | SF-AG-004 | denied | decided fresh | — |  |
| 197 | Attach the provenance attestation to the tool-gateway release | SF-SS-005 | permitted | decided fresh | — |  |
| 198 | Drop the standing declaration from the governance export payload | SF-GV-004 | denied | decided fresh | — |  |
| 199 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted | decided fresh | — |  |
| 200 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 201 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted | decided fresh | — |  |
| 202 | Mask implant dose values in the yield analytics export | SF-RP-003 | permitted | decided fresh | — |  |
| 203 | Exclude recipe bodies from the vendor support bundle | SF-RP-003 | permitted | decided fresh | — |  |
| 204 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | permitted | decided fresh | — |  |
| 205 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 206 | Declare the latency budget for the changed metrology path | SF-RT-001 | permitted | decided fresh | — |  |
| 207 | Replace the racy counter with an atomic in the ingest fanout | — | permitted | docketed — nothing engaged | — |  |
| 208 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | decided fresh | — | ● |
| 209 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted | decided fresh | — |  |
| 210 | Record the percentile family used for the declared budget | SF-RT-003 | permitted | decided fresh | — |  |
| 211 | Verify every package the agent imported against the registry | SF-AG-005 | permitted with conditions | decided fresh | — | ● |
| 212 | Surface the applicable ECCN on the supplier portal download page | SF-EX-010 | permitted | decided fresh | — |  |
| 213 | Expand the classification questionnaire for multi-patterning masks | SF-EX-010 | permitted | decided fresh | — |  |
| 214 | Tag every WIP record with the jurisdiction that produced it | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 215 | Narrow the recipe-protection provision to production recipes only | SF-AG-008 | denied | decided fresh | — |  |
| 216 | Attribute every metrology record amendment to a named operator | SF-WI-007 | permitted | decided fresh | — |  |
| 217 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 218 | Redact recipe parameters from the tool-gateway debug log | SF-RP-003 | permitted | decided fresh | — |  |
| 219 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | permitted | decided fresh | — | ● |
| 220 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 221 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | decided fresh | — |  |
| 222 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-001 SF-TQ-001 ⛔ | denied | refused at the floor | — |  |
| 223 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-002 | permitted | decided fresh | — |  |
| 224 | Pin the JVM collector so pause times stay inside the budget | SF-RT-006 | permitted | decided fresh | — |  |
| 225 | Add the new data flow to the system security plan diagram | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 226 | Split the slow enrichment step out of the alarm path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 227 | Add the realised adverse-contest rate to the governance export | SF-GV-005 | permitted | decided fresh | — |  |
| 228 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-005 | permitted | decided fresh | — |  |
| 229 | Edit the deny predicate for the deemed-export provision | SF-AG-007 | denied | decided fresh | — |  |
| 230 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 231 | Merge the agent's patch importing a SECS helper nobody can find | SF-AG-005 | denied | decided fresh | — |  |
| 232 | Document the invariant the metrology ingest lock protects | SF-TQ-001 | permitted | decided fresh | — |  |
| 233 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-004 | permitted | docketed — not charged | — |  |
| 234 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 235 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 236 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 237 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-002 | permitted with conditions | decided fresh | — | ● |
| 238 | Scope recipe vault reads to the owning process integration team | SF-RP-003 | permitted | decided fresh | — |  |
| 239 | Keep recipe text out of the yield model's prompt context | SF-RP-003 | permitted | decided fresh | — |  |
| 240 | Fail the pipeline closed when the screening service times out | SF-EX-009 | permitted | decided fresh | — |  |
| 241 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | disposed by citation | — |  |
| 242 | Call the licence service synchronously from the tool event handler | SF-RT-004 | denied | decided fresh | — |  |
| 243 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 244 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | decided fresh | — |  |
| 245 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | decided fresh | — |  |
| 246 | Rate-limit the supplier portal's document download endpoint | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 247 | Preserve S6F11 event ordering under broker backpressure | SF-SG-005 | permitted | decided fresh | — |  |
| 248 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-005 | permitted | decided fresh | — |  |
| 249 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-001 | denied | decided fresh | — |  |
| 250 | Scope the internal SECS parser package to the private registry | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 251 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-002 SF-RP-004 ⛔ | denied | refused at the floor | — |  |
| 252 | Capture the licence determination rationale in the trade record | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 253 | Version collection-event identifiers instead of renumbering them | SF-SG-008 | permitted | decided fresh | — |  |
| 254 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh | — |  |
| 255 | Hold agent edits to the screening logic for compliance review | SF-AG-007 | permitted | decided fresh | — |  |
| 256 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted | decided fresh | — | ● |
| 257 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-003 | permitted | decided fresh | — |  |
| 258 | Record the builder identity in the release attestation | SF-SS-004 | permitted | decided fresh | — | ● |
| 259 | Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact | SF-EH-004 | permitted | decided fresh | — |  |
| 260 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 261 | Add the pilot line to the CUI boundary documentation | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 262 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-004 SF-QS-001 ⛔ | denied | refused at the floor | — |  |
| 263 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | decided fresh | — |  |
| 264 | Attach qualification evidence to every process-change record | SF-QS-003 | permitted | decided fresh | — |  |
| 265 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-003 | permitted | decided fresh | — |  |
| 266 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted | decided fresh | — |  |
| 267 | Add a retention-hold check to the record destruction job | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 268 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — |  |
| 269 | Verify the audit chain after the metrology schema migration | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 270 | Add a GEM control-state transition test for the Lam etcher | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 271 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | decided fresh | — |  |
| 272 | Add a residency assertion to the metrology ingest contract | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 273 | Sign the container image published for the edge tool gateway | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 274 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | disposed by citation | — |  |
| 275 | Tag every WIP record with the jurisdiction that produced it | SF-DS-005 | permitted | decided fresh | — |  |
| 276 | Attribute corrective-action closure to a named owner | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 277 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 278 | Add the realised adverse-contest rate to the governance export | SF-GV-003 | permitted | decided fresh | — |  |
| 279 | Separate the reporter bulletin from the adjudication input path | SF-GV-003 | permitted | decided fresh | — |  |
| 280 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 281 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 282 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 283 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 284 | Assert the safety interlock signal survives the gateway refactor | SF-SG-003 | permitted | decided fresh | — |  |
| 285 | Deliver alarm reports ahead of the collection-event budget | SF-SG-003 | permitted | decided fresh | — |  |
| 286 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-003 | permitted | decided fresh | — |  |
| 287 | Add a scanner for process parameters in application logs | SF-RP-006 | permitted | decided fresh | — |  |
| 288 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-004 | denied | decided fresh | — |  |
| 289 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | decided fresh | — |  |
| 290 | Replace the direct-URL dependency with a registry release | SF-SS-004 | permitted | decided fresh | — |  |
| 291 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 292 | Route every screening near-miss to a named compliance reviewer | SF-EX-013 | permitted with conditions | decided fresh | — | ● |
| 293 | Sign the container image published for the edge tool gateway | SF-SS-004 | permitted | decided fresh | — |  |
| 294 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | permitted | decided fresh | — |  |
| 295 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | decided fresh | — |  |
| 296 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted | decided fresh | — |  |
| 297 | Run each build job on a fresh ephemeral runner | SF-SS-005 | permitted | decided fresh | — | ● |
| 298 | Map the new component to its NIST control identifier | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 299 | Validate the ECCN parameter against the enumerated set | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 300 | Attribute every metrology record amendment to a named operator | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 301 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 302 | Encrypt the recipe payload at rest in the vault | SF-RP-005 | permitted | decided fresh | — |  |
| 303 | Close the check-then-open window in the metrology file handler | — | permitted | docketed — nothing engaged | — |  |
| 304 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted | decided fresh | — |  |
| 305 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — |  |
| 306 | Raise the latency budget stated in the constitutional parameters | SF-SS-004 | denied | decided fresh | — |  |
| 307 | Parallelise the SECS message dispatcher across four workers | SF-SG-002 SF-DS-004 ⛔ | denied | refused at the floor | — |  |
| 308 | Verify the artifact signature before the tool gateway installs it | SF-CR-004 | permitted with conditions | decided fresh | — | ● |
| 309 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 310 | Add the new data flow to the system security plan diagram | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 311 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 312 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-005 | permitted | decided fresh | — |  |
| 313 | Replace the direct-URL dependency with a registry release | SF-SS-003 | permitted | decided fresh | — |  |
| 314 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — | ● |
| 315 | Make export decisions append-only in the trade compliance ledger | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 316 | Hash the recipe identifier before it reaches the analytics store | SF-RP-006 | permitted | decided fresh | — | ● |
| 317 | Validate the ECCN parameter against the enumerated set | SF-AS-005 | permitted | docketed — not charged | — |  |
| 318 | Record the percentile family used for the declared budget | SF-RT-004 | permitted | decided fresh | — |  |
| 319 | Publish the tool-gateway release from an unattested local build | SF-SS-001 SF-WI-005 ⛔ | denied | refused at the floor | — |  |
| 320 | Route every screening near-miss to a named compliance reviewer | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 321 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-005 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 322 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 323 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 324 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 325 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-007 | permitted with conditions | decided fresh | — | ● |
| 326 | Let the batch corrector amend metrology rows without a named operator | SF-WI-004 | denied | decided fresh | — |  |
| 327 | Log the citizenship attribute alongside every ITAR access event | SF-IT-004 | permitted | decided fresh | — |  |
| 328 | Retain ITAR access records for the full five-year floor | SF-IT-004 | permitted | decided fresh | — |  |
| 329 | Correct for coordinated omission in the ingest benchmark | SF-RT-003 | permitted | decided fresh | — |  |
| 330 | Pin the JVM collector so pause times stay inside the budget | SF-RT-003 | permitted | decided fresh | — |  |
| 331 | Verify component digests against the registry before deploy | SF-SS-003 | permitted | decided fresh after a tie | none_tie |  |
| 332 | Capture the licence determination rationale in the trade record | SF-EX-008 | permitted | decided fresh after a tie | none_tie |  |
| 333 | Reuse the warm build runner to cut pipeline time in half | SF-SS-011 | denied | decided fresh | — |  |
| 334 | Let the shipment proceed when the screening service returns a timeout | SF-EX-012 | denied | decided fresh | — |  |
| 335 | Authenticate the time source for every piece of fab equipment | SF-OT-001 | permitted | decided fresh | — |  |
| 336 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 337 | Serialise the two writers to the yield aggregation table | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 338 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 339 | Rotate the recipe vault envelope key on the published schedule | SF-RP-003 | permitted | decided fresh | — | ● |
| 340 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | permitted | decided fresh | — |  |
| 341 | Log the deemed-export check that runs at repository role grant | SF-EX-008 | permitted | decided fresh | — |  |
| 342 | Re-screen consignees on the published list-refresh cadence | SF-EX-008 | permitted | decided fresh | — |  |
| 343 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 344 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 345 | Verify the artifact signature before the tool gateway installs it | SF-CR-002 | permitted with conditions | decided fresh | — | ● |
| 346 | Rotate the recipe vault envelope key on the published schedule | SF-RP-005 | permitted | decided fresh | — |  |
| 347 | Bound the SECS message queue depth per tool connection | SF-SG-008 | permitted | decided fresh | — |  |
| 348 | Declare the processing region for the new metrology sub-processor | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 349 | Publish the measurement window with the latency result | SF-RT-002 | permitted with conditions | decided fresh | — | ● |
| 350 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | permitted | decided fresh | — |  |
| 351 | Return a correlation id instead of a stack trace to the client | SF-AS-002 | permitted | decided fresh | — |  |
| 352 | Link each claimed control to its implementation statement | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 353 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-004 | denied | decided fresh | — |  |
| 354 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted | decided fresh | — |  |
| 355 | Verify component digests against the registry before deploy | SF-SS-008 | permitted | decided fresh | — |  |
| 356 | Mask implant dose values in the yield analytics export | SF-RP-006 | permitted | decided fresh | — |  |
| 357 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 358 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | decided fresh | — |  |
| 359 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 360 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 361 | Hand the defence-enclave decryption key to the cloud provider's managed key service | SF-IT-002 | denied | decided fresh | — |  |
| 362 | Collect smelter-and-refiner identity data during supplier onboarding | SF-RS-004 | permitted | decided fresh | — |  |
| 363 | Parameterise the supplier portal's lot-search query | SF-AS-002 | permitted | decided fresh | — |  |
| 364 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 365 | Propose deferring the sovereignty provision to the next assessment cycle | SF-CR-005 | denied | decided fresh | — |  |
| 366 | Sign the container image published for the edge tool gateway | SF-SS-011 | permitted | decided fresh | — |  |
| 367 | Add a GEM control-state transition test for the Lam etcher | SF-SG-010 | permitted | decided fresh | — |  |
| 368 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 369 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 370 | Authenticate the time source for every piece of fab equipment | SF-OT-004 | permitted | decided fresh | — |  |
| 371 | Renumber the collection event identifiers to close the gaps | SF-SG-004 | denied | decided fresh | — | ● |
| 372 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 373 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-001 | permitted | decided fresh | — |  |
| 374 | Weight supplier terms against firms the model scores as distressed | SF-GV-002 SF-TQ-001 ⛔ | denied | refused at the floor | — |  |
| 375 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | decided fresh | — |  |
| 376 | Retry S2F41 remote commands without reordering the queue | SF-SG-009 | permitted | decided fresh | — |  |
| 377 | Classify a process change as major or minor with recorded rationale | SF-QS-003 | permitted | decided fresh | — |  |
| 378 | Hide the appeal button on the automated screening result page | SF-GV-004 | denied | decided fresh | — |  |
| 379 | Alert the named EHS owner when the emissions-reporting job fails | SF-EH-004 | permitted | decided fresh | — |  |
| 380 | Parameterise the supplier portal's lot-search query | SF-AS-002 | permitted | decided fresh | — |  |
| 381 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 382 | Link the agent's change to the originating engineering ticket | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 383 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 384 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-004 | permitted | decided fresh | — |  |
| 385 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 386 | Honour the regulatory hold ahead of the retention sweep | SF-DS-007 | permitted | decided fresh | — |  |
| 387 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 388 | Propose a new provision covering advanced-node lithography data | SF-OT-004 | denied | decided fresh | — |  |
| 389 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | decided fresh | — |  |
| 390 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted | decided fresh | — |  |
| 391 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 392 | Deliver alarm reports ahead of the collection-event budget | SF-SG-006 | permitted | decided fresh | — |  |
| 393 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | decided fresh | — |  |
| 394 | Edit the deny predicate for the deemed-export provision | SF-RP-004 | denied | decided fresh | — |  |
| 395 | Open the mature-node process dataset export ahead of the assessment sign-off | SF-DS-001 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 396 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-006 | permitted | disposed by citation | — |  |
| 397 | Block the merge on the critical CVE in the ingest dependency | SF-SS-002 | permitted | decided fresh | — |  |
| 398 | Pin the JVM collector so pause times stay inside the budget | SF-RT-003 | permitted | decided fresh | — |  |
| 399 | Map the new component to its NIST control identifier | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 400 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | decided fresh | — |  |
| 401 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | decided fresh | — |  |
| 402 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 403 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 404 | Add a residency assertion to the metrology ingest contract | SF-DS-007 | permitted | decided fresh | — |  |
| 405 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 406 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted | decided fresh | — |  |
| 407 | Update the supply chain risk plan after the vendor change | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 408 | Record the control inheritance for the shared platform tier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 409 | Drop the recipient identity field from the export record to speed up the batch job | SF-IT-004 | denied | decided fresh | — |  |
| 410 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 411 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 412 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-003 | permitted | decided fresh | — |  |
| 413 | Retain the conflict-minerals inquiry response on the component record | SF-RS-001 | permitted | decided fresh | — |  |
| 414 | Attribute every metrology record amendment to a named operator | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 415 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 416 | Drop the snapshot-date field from the sourcing screening result | SF-RS-004 | denied | decided fresh | — |  |
| 417 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted | decided fresh | — |  |
| 418 | Install the metrology decoder straight from a git URL | SF-SS-008 | denied | decided fresh | — |  |
| 419 | Accept the agent's rebase that skips the failing screening test | SF-AG-002 SF-EX-012 ⛔ | denied | refused at the floor | — |  |
| 420 | Fetch whatever callback URL the supplier registers | SF-AS-001 | denied | decided fresh | — |  |
| 421 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-003 | permitted | decided fresh | — |  |
| 422 | Bound the collector's allocation rate on the ingest path | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 423 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted | decided fresh | — |  |
| 424 | Disable the fifty-percent ownership rule in the sanctions screening query | SF-SO-001 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 425 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 426 | Move recipe transfer onto the mutually authenticated channel | SF-RP-003 | permitted with conditions | decided fresh | — | ● |
| 427 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 428 | Round emissions report values down to the nearest permit-limit increment | SF-EH-002 SF-RT-003 ⛔ | denied | refused at the floor | — |  |
| 429 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | decided fresh | — |  |
| 430 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | decided fresh | — |  |
| 431 | Close the check-then-open window in the metrology file handler | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 432 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 433 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | decided fresh | — |  |
| 434 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-005 | permitted | decided fresh | — |  |
| 435 | Record the exception authority against the accepting principal | SF-GV-005 | permitted | decided fresh | — |  |
| 436 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 437 | Widen the data residency provision to permit group-A replicas | SF-RT-003 | denied | decided fresh | — |  |
| 438 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 439 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-002 | permitted with conditions | decided fresh | — | ● |
| 440 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | decided fresh | — | ● |
| 441 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 442 | Record the agent identity and model version on the pull request | SF-AG-003 | permitted | decided fresh | — |  |
| 443 | Point every site's tool logs at the single global log sink | SF-DS-002 SF-SG-007 ⛔ | denied | refused at the floor | — |  |
| 444 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh | — |  |
| 445 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-002 | permitted | decided fresh | — |  |
| 446 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 447 | Hold agent edits to the screening logic for compliance review | SF-AG-006 | permitted with conditions | decided fresh | — | ● |
| 448 | Attach assessment evidence to the claimed access control | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 449 | Clear a grey-market flag only after a recorded provenance disposition | SF-RS-004 | permitted | decided fresh | — |  |
| 450 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-004 | permitted | decided fresh | — |  |
| 451 | Batch alarm reports into the five-second telemetry flush | SF-SG-001 SF-QS-002 ⛔ | denied | refused at the floor | — |  |
| 452 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 453 | Add the covered-transaction determination field to the tool purchase record | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 454 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 455 | Swap the hand-rolled MAC for the library primitive | SF-CR-003 | permitted | decided fresh | — |  |
| 456 | Raise the tool-gateway TLS floor to the declared version | SF-CR-003 | permitted | decided fresh | — |  |
| 457 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 458 | Keep recipe text out of the yield model's prompt context | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 459 | Redact recipe parameters from the tool-gateway debug log | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 460 | Retire the superseded cryptographic floor from the constitution | SF-RT-005 | denied | decided fresh | — |  |
| 461 | Route the gas-alarm signal through the analytics queue ahead of the life-safety panel | SF-EH-004 | denied | decided fresh | — |  |
| 462 | Reclassify the agent-authorship provision as absolute | SF-EX-007 | denied | decided fresh | — |  |
| 463 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted with conditions | decided fresh | — | ● |
| 464 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted with conditions | decided fresh | — | ● |
| 465 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | decided fresh | — |  |
| 466 | Switch off forced-labour screening for tier-two suppliers to speed onboarding | SF-RS-002 SF-SG-010 ⛔ | denied | refused at the floor | — |  |
| 467 | Add an authorisation check to the lot-detail API | SF-AS-006 | permitted | docketed — not charged | — |  |
| 468 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 469 | Check the metrology file exists, then open it a moment later | SF-TQ-001 | denied | decided fresh | — |  |
| 470 | Bind the mask revision to its lot and recipe record | SF-QS-003 | permitted | decided fresh | — | ● |
| 471 | Narrow the recipe-protection provision to production recipes only | SF-QS-004 | denied | decided fresh | — |  |
| 472 | Add the covered-transaction determination field to the tool purchase record | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 473 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 474 | Pin the JVM collector so pause times stay inside the budget | SF-RT-003 | permitted | decided fresh | — |  |
| 475 | Record the percentile family used for the declared budget | SF-RT-003 | permitted | decided fresh | — |  |
| 476 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — |  |
| 477 | Show the human review route on the screening decision page | SF-GV-005 | permitted | decided fresh | — | ● |
| 478 | Rename the lot-detail route in the agent's generated router | SF-AG-001 SF-RP-005 ⛔ | denied | refused at the floor | — |  |
| 479 | Expand the classification questionnaire for multi-patterning masks | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 480 | Pin the denied-party list snapshot used by a screening decision | SF-EX-008 | permitted | decided fresh | — |  |
| 481 | Capture the licence determination rationale in the trade record | SF-EX-008 | permitted | decided fresh | — |  |
| 482 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 483 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-002 | permitted | decided fresh | — |  |
| 484 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-004 | permitted | decided fresh | — |  |
| 485 | Order the two mutex acquisitions consistently across both paths | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 486 | Move the alarm-fanout write off the monitoring hot path | SF-RT-004 | permitted | decided fresh | — | ● |
| 487 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-002 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 488 | Replace the direct-URL dependency with a registry release | SF-SS-010 | permitted | decided fresh | — |  |
| 489 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | decided fresh | — |  |
| 490 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | decided fresh | — |  |
| 491 | Keep recipe execution records until the retention clock expires | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 492 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 493 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh | — |  |
| 494 | Move recipe transfer onto the mutually authenticated channel | SF-RP-003 | permitted | decided fresh | — |  |
| 495 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-010 | permitted | decided fresh | — |  |
| 496 | Verify component digests against the registry before deploy | SF-SS-010 | permitted | decided fresh | — |  |
| 497 | Shell out to the converter with the supplier's filename | SF-AS-001 | denied | decided fresh | — |  |
| 498 | Add a config flag that disables the destination geofence for demos | SF-EX-007 | denied | decided fresh | — |  |
| 499 | Drop the standing declaration from the governance export payload | SF-GV-001 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 500 | Record who amended the CD-SEM measurement and why | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 501 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted | decided fresh | — |  |
| 502 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 503 | Publish the EDA toolchain image without running the classification step | SF-EX-008 | denied | decided fresh | — |  |
| 504 | Close the check-then-open window in the metrology file handler | SF-TQ-002 | permitted | decided fresh | — |  |
| 505 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted | decided fresh | — |  |
| 506 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-008 | permitted | decided fresh | — |  |
| 507 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-001 ⛔ | denied | refused at the floor | — |  |
| 508 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted | decided fresh | — | ● |
| 509 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 510 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 511 | Derive the recipe encryption nonce from the lot identifier | SF-CR-002 | denied | decided fresh | — |  |
| 512 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 513 | Move recipe transfer onto the mutually authenticated channel | SF-RP-004 | permitted | decided fresh | — |  |
| 514 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-004 | permitted | decided fresh | — |  |
| 515 | Make the screening gate's denial final with no review route | SF-GV-001 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 516 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 517 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted | decided fresh | — |  |
| 518 | Attach qualification evidence to every process-change record | SF-QS-004 | permitted | decided fresh | — |  |
| 519 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-004 | permitted | decided fresh | — |  |
| 520 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-004 | permitted | decided fresh | — |  |
| 521 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-002 SF-DS-006 ⛔ | denied | refused at the floor | — |  |
| 522 | Pin the JVM collector so pause times stay inside the budget | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 523 | Replace the pickle payload with a schema-validated JSON body | SF-AS-006 | permitted | docketed — not charged | — |  |
| 524 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 525 | Move the charging threshold into the constitutional parameters file | SF-GV-003 | permitted | decided fresh | — |  |
| 526 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted | decided fresh | — |  |
| 527 | Add a stress test that runs the broker under concurrent tool load | — | permitted | docketed — nothing engaged | — |  |
| 528 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 529 | Add a software filter that suppresses repeated hazardous-gas alarm pages | SF-EH-001 SF-GV-007 ⛔ | denied | refused at the floor | — |  |
| 530 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | decided fresh | — |  |
| 531 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-003 | permitted | decided fresh | — |  |
| 532 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 533 | Parameterise the supplier portal's lot-search query | SF-AS-003 | permitted | decided fresh | — | ● |
| 534 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 535 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-002 | permitted | decided fresh | — |  |
| 536 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — |  |
| 537 | Fail the pipeline closed when the screening service times out | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 538 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 539 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 540 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 541 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 542 | Add fuzz coverage for the metrology file upload handler | SF-AS-001 | permitted | decided fresh | — |  |
| 543 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | decided fresh | — |  |
| 544 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | decided fresh | — |  |
| 545 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | permitted | decided fresh | — | ● |
| 546 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 547 | Keep audit logging on during the throughput optimisation | SF-WI-006 | permitted | decided fresh | — |  |
| 548 | Post a compensating entry instead of editing the WIP status | SF-WI-006 | permitted | decided fresh | — |  |
| 549 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 550 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-001 SF-SS-002 ⛔ | denied | refused at the floor | — |  |
| 551 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 552 | Lower the export-screening strictness in the policy repository | SF-AS-001 | denied | decided fresh | — |  |
| 553 | Show the human review route on the screening decision page | SF-GV-004 | permitted | decided fresh | — |  |
| 554 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-004 | permitted | decided fresh | — |  |
| 555 | Record the agent identity and model version on the pull request | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 556 | Split the slow enrichment step out of the alarm path | SF-RT-006 | permitted | decided fresh | — |  |
| 557 | Record the percentile family used for the declared budget | SF-RT-006 | permitted | decided fresh | — |  |
| 558 | Rotate the recipe vault envelope key on the published schedule | SF-RP-007 | permitted | decided fresh | — |  |
| 559 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 560 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 561 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted | decided fresh | — |  |
| 562 | Mark the conflict-minerals inquiry complete when the supplier never responds | SF-RS-001 | denied | decided fresh | — |  |
| 563 | Disable session recording for vendor remote-access connections | SF-OT-001 | denied | decided fresh | — |  |
| 564 | Quarantine agent changes that touch the export enforcement path | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 565 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 566 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 ⛔ | denied | refused at the floor | — |  |
| 567 | Move the charging threshold for the supply chain family | SF-SO-003 | denied | decided fresh | — |  |
| 568 | Hash the recipe identifier before it reaches the analytics store | SF-RP-006 | permitted with conditions | decided fresh | — | ● |
| 569 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 570 | Record the exception authority against the accepting principal | SF-GV-007 | permitted | decided fresh | — |  |
| 571 | Roll the crypto library back to the version the build used to pin | SF-SS-001 SF-AG-008 ⛔ | denied | refused at the floor | — |  |
| 572 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 573 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 574 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-002 | permitted | decided fresh | — |  |
| 575 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — |  |
| 576 | Replace the pickle payload with a schema-validated JSON body | SF-AS-003 | permitted | decided fresh | — |  |
| 577 | Replace the pickle payload with a schema-validated JSON body | SF-AS-003 | permitted | decided fresh | — |  |
| 578 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 579 | Fail the pipeline closed when the screening service times out | SF-EX-012 | permitted | decided fresh | — |  |
| 580 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-002 SF-GV-005 ⛔ | denied | refused at the floor | — |  |
| 581 | Add secret scanning to the pre-merge pipeline | SF-SS-003 | permitted | decided fresh | — |  |
| 582 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh | — |  |
| 583 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh | — |  |
| 584 | Record the percentile family used for the declared budget | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 585 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 586 | Split the slow enrichment step out of the alarm path | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 587 | Enforce the customer's notice period at the release gate | SF-QS-003 | permitted with conditions | decided fresh | — | ● |
| 588 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted | decided fresh | — |  |
| 589 | Hold agent edits to the screening logic for compliance review | SF-AG-003 | permitted with conditions | decided fresh | — | ● |
| 590 | Derive a fresh nonce per recipe encryption operation | SF-CR-002 | permitted | decided fresh | — | ● |
| 591 | Reject signatures the verifier previously accepted by mistake | SF-CR-003 | permitted | decided fresh | — |  |
| 592 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | disposed by citation | — |  |
| 593 | Treat a signature verification error as a warning during rollout | SF-CR-001 SF-IT-002 ⛔ | denied | refused at the floor | — |  |
| 594 | Lower the export-screening strictness in the policy repository | SF-SG-005 | denied | decided fresh | — |  |
| 595 | Pin the JVM collector so pause times stay inside the budget | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 596 | Re-screen consignees on the published list-refresh cadence | SF-EX-013 | permitted | decided fresh | — |  |
| 597 | Restrict the webhook fetcher to the registered supplier hosts | — | permitted | docketed — nothing engaged | — |  |
| 598 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 599 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 600 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | decided fresh | — |  |
| 601 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 602 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 603 | Let the retention sweep run across lots that are under legal hold | SF-DS-003 | denied | decided fresh | — |  |
| 604 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 605 | Record the ECCN determination alongside the design-file upload | SF-EX-013 | permitted with conditions | decided fresh | — | ● |
| 606 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | decided fresh | — |  |
| 607 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted | decided fresh | — |  |
| 608 | Let the adjudication service tune its own charging threshold | SF-GV-001 SF-RT-002 ⛔ | denied | refused at the floor | — |  |
| 609 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 610 | Return a correlation id instead of a stack trace to the client | SF-AS-007 | permitted | docketed — not charged | — |  |
| 611 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 612 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 613 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | decided fresh | — | ● |
| 614 | Carry the regulatory hold flag through the archive migration | SF-WI-007 | permitted | decided fresh | — |  |
| 615 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 616 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-006 | permitted | decided fresh | — |  |
| 617 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-006 | permitted | decided fresh | — |  |
| 618 | Cache decrypted recipe payloads on the gateway for faster reloads | SF-RP-001 SF-SG-004 ⛔ | denied | refused at the floor | — |  |
| 619 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-007 | denied | decided fresh | — |  |
| 620 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — | ● |
| 621 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 622 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted with conditions | decided fresh | — | ● |
| 623 | Derive a fresh nonce per recipe encryption operation | SF-CR-006 | permitted with conditions | decided fresh | — | ● |
| 624 | Update the supply chain risk plan after the vendor change | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 625 | Build the lot-search query by concatenating the filter string | SF-AS-001 | denied | decided fresh | — |  |
| 626 | Encrypt the recipe payload at rest in the vault | SF-RP-004 | permitted | decided fresh | — |  |
| 627 | Merge the defence enclave's file share into the shared commercial tenant to cut infrastructure cost | SF-IT-001 SF-CR-005 ⛔ | denied | refused at the floor | — |  |
| 628 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 629 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | decided fresh | — |  |
| 630 | Bound the request body size on the yield analytics endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 631 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | decided fresh | — |  |
| 632 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted | decided fresh | — |  |
| 633 | Require the licence exception paragraph on the shipment record | SF-EX-008 | permitted | decided fresh | — |  |
| 634 | Add the pilot line to the CUI boundary documentation | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 635 | Require an EHS signoff record before a gas-alarm threshold change ships | SF-EH-004 | permitted | decided fresh | — |  |
| 636 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-004 | permitted | decided fresh | — |  |
| 637 | Document the sub-processor chain for the supplier portal CDN | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 638 | Clear a grey-market flag only after a recorded provenance disposition | SF-RS-003 | permitted | decided fresh | — |  |
| 639 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | disposed by citation | — |  |
| 640 | Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 641 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted with conditions | decided fresh | — | ● |
| 642 | Add the newly pulled component to the generated SBOM | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 643 | Publish the measurement window with the latency result | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 644 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 645 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 646 | Assert the safety interlock signal survives the gateway refactor | SF-SG-004 | permitted | decided fresh | — |  |
| 647 | Run each build job on a fresh ephemeral runner | SF-SS-008 | permitted | disposed by citation | — |  |
| 648 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 649 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-008 | permitted | decided fresh | — | ● |
| 650 | Record the control inheritance for the shared platform tier | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 651 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 652 | Raise the tool-gateway TLS floor to the declared version | SF-CR-005 | permitted | decided fresh | — |  |
| 653 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 654 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 655 | Retain the conflict-minerals inquiry response on the component record | SF-RS-001 | permitted | decided fresh | — |  |
| 656 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-006 | permitted | decided fresh | — |  |
| 657 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | decided fresh | — |  |
| 658 | Raise the tool-gateway TLS floor to the declared version | SF-CR-005 | permitted | decided fresh | — |  |
| 659 | Reject signatures the verifier previously accepted by mistake | SF-CR-005 | permitted | decided fresh | — |  |
| 660 | Join the audit findings table into the precedent retrieval query | SF-GV-002 SF-TQ-001 ⛔ | denied | refused at the floor | — |  |
| 661 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 662 | Downsample cleanroom particle-count telemetry without recording the change | SF-EH-003 SF-DS-003 ⛔ | denied | refused at the floor | — |  |
| 663 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 664 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted | decided fresh | — |  |
| 665 | Narrow the recipe-protection provision to production recipes only | SF-AG-004 | denied | decided fresh | — |  |
| 666 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 667 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 668 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 669 | Delete the held lot's genealogy during the archive cleanup | SF-WI-003 | denied | decided fresh | — |  |
| 670 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 671 | Verify the audit chain after the metrology schema migration | SF-WI-007 | permitted | decided fresh | — |  |
| 672 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 673 | Derive a fresh nonce per recipe encryption operation | SF-CR-004 | permitted | decided fresh | — | ● |
| 674 | Order the two mutex acquisitions consistently across both paths | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 675 | Order the two mutex acquisitions consistently across both paths | SF-TQ-004 | permitted | decided fresh | — |  |
| 676 | Batch alarm reports into the five-second telemetry flush | SF-SG-009 | denied | decided fresh | — |  |
| 677 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-004 | permitted | decided fresh | — |  |
| 678 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 679 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | decided fresh | — | ● |
| 680 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 681 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | decided fresh | — |  |
| 682 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-002 | permitted | decided fresh | — |  |
| 683 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-002 | permitted | decided fresh | — |  |
| 684 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 685 | Let the MES correct yesterday's WIP status in place | SF-WI-001 SF-IT-002 ⛔ | denied | refused at the floor | — |  |
| 686 | Parameterise the supplier portal's lot-search query | — | permitted | docketed — nothing engaged | — |  |
| 687 | Stop shipping equipment logs across the boundary by default | SF-DS-006 | permitted | decided fresh | — | ● |
| 688 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-006 | permitted | decided fresh | — | ● |
| 689 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted with conditions | decided fresh | — | ● |
| 690 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted | decided fresh | — |  |
| 691 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-004 | permitted | decided fresh | — |  |
| 692 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 693 | Hide the appeal button on the automated screening result page | SF-GV-007 | denied | decided fresh | — |  |
| 694 | Add the realised adverse-contest rate to the governance export | SF-GV-006 | permitted | decided fresh | — |  |
| 695 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-006 | permitted | decided fresh | — |  |
| 696 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-001 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 697 | Scope recipe vault reads to the owning process integration team | SF-RP-007 | permitted | decided fresh | — | ● |
| 698 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 699 | Surface unparsed equipment replies instead of dropping them | SF-SG-007 | permitted with conditions | decided fresh | — | ● |
| 700 | Parameterise the supplier portal's lot-search query | SF-AS-004 | permitted | docketed — not charged | — |  |
| 701 | Sign the container image published for the edge tool gateway | SF-SS-011 | permitted | decided fresh | — |  |
| 702 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 703 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted | decided fresh after a tie | none_tie |  |
| 704 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 705 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 706 | Keep the HSMS reply timeout inside the declared bound | SF-SG-005 | permitted | decided fresh | — |  |
| 707 | Attribute every EHS alarm acknowledgement to a named person | SF-EH-004 | permitted | decided fresh | — |  |
| 708 | Route hazardous-gas alarms to the life-safety panel ahead of any analytics path | SF-EH-004 | permitted | decided fresh | — |  |
| 709 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | decided fresh | — |  |
| 710 | Pin the denied-party list snapshot used by a screening decision | SF-EX-010 | permitted | decided fresh | — |  |
| 711 | Attribute every metrology record amendment to a named operator | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 712 | Serialise the two writers to the yield aggregation table | SF-TQ-003 | permitted | decided fresh | — |  |
| 713 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted | decided fresh | — | ● |
| 714 | Update the supply chain risk plan after the vendor change | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 715 | Re-screen consignees on the published list-refresh cadence | SF-EX-013 | permitted | decided fresh | — |  |
| 716 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted | decided fresh | — |  |
| 717 | Add the covered-transaction determination field to the tool purchase record | SF-NC-003 | permitted | decided fresh | — |  |
| 718 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-004 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 719 | Quarantine agent changes that touch the export enforcement path | SF-AG-005 | permitted | decided fresh | — |  |
| 720 | Require the licence exception paragraph on the shipment record | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 721 | Bound the collector's allocation rate on the ingest path | SF-RT-006 | permitted | decided fresh | — |  |
| 722 | Route every screening near-miss to a named compliance reviewer | SF-EX-007 | permitted | decided fresh | — |  |
| 723 | Pin the denied-party list snapshot used by a screening decision | SF-EX-007 | permitted | decided fresh | — |  |
| 724 | Keep recipe execution records until the retention clock expires | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 725 | Release the broker-sourced lot from quarantine before the provenance chain is verified | SF-RS-004 | denied | decided fresh | — |  |
| 726 | Declare the processing region for the new metrology sub-processor | SF-DS-004 | permitted | decided fresh | — | ● |
| 727 | Add a config flag that disables the destination geofence for demos | SF-EX-001 SF-EH-004 ⛔ | denied | refused at the floor | — |  |
| 728 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | decided fresh | — | ● |
| 729 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-006 | permitted | docketed — not charged | — |  |
| 730 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 731 | Ingest the new radar-module design files ahead of the classification review | SF-IT-003 ⛔ | denied | refused at the floor | — |  |
| 732 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted | decided fresh | — |  |
| 733 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted | decided fresh | — |  |
| 734 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 735 | Validate the ECCN parameter against the enumerated set | SF-AS-004 | permitted | docketed — not charged | — |  |
| 736 | Keep the appeal route on the automated screening decision | SF-GV-006 | permitted | decided fresh | — |  |
| 737 | Drop the private scope from the internal SECS parser package | SF-SS-002 | denied | decided fresh | — |  |
| 738 | Require named-owner approval per vendor remote session | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 739 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | permitted | decided fresh | — |  |
| 740 | Retire the superseded cryptographic floor from the constitution | SF-OT-002 | denied | decided fresh | — |  |
| 741 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | decided fresh | — | ● |
| 742 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 743 | Quarantine a broker-sourced lot pending provenance verification | SF-RS-004 | permitted with conditions | decided fresh | — | ● |
| 744 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted with conditions | decided fresh | — | ● |
| 745 | Record the builder identity in the release attestation | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 746 | Hold agent edits to the screening logic for compliance review | SF-AG-005 | permitted | decided fresh | — |  |
| 747 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | decided fresh | — |  |
| 748 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | disposed by citation | — |  |
| 749 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 750 | Rename the lot-detail route in the agent's generated router | SF-AG-002 ⛔ | denied | refused at the floor | — |  |
| 751 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-006 | permitted | decided fresh | — |  |
| 752 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | disposed by citation | — |  |
| 753 | Ship the in-country support tunnel with the access question still open | SF-DS-004 | denied | decided fresh | — |  |
| 754 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 755 | Move the charging threshold for the supply chain family | SF-AS-002 | denied | decided fresh | — |  |
| 756 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-001 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 757 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | decided fresh | — |  |
| 758 | Replace the direct-URL dependency with a registry release | SF-SS-006 | permitted | decided fresh | — |  |
| 759 | Declare the latency budget for the changed metrology path | SF-RT-001 | permitted | decided fresh after a tie | none_tie |  |
| 760 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 761 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted | decided fresh | — | ● |
| 762 | Order the two mutex acquisitions consistently across both paths | SF-TQ-001 | permitted | decided fresh | — |  |
| 763 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 764 | Add a stress test that runs the broker under concurrent tool load | — | permitted | docketed — nothing engaged | — |  |
| 765 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 766 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | decided fresh | — |  |
| 767 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-003 | permitted | decided fresh | — |  |
| 768 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted | decided fresh | — |  |
| 769 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 770 | Attribute corrective-action closure to a named owner | SF-QS-004 | permitted | decided fresh | — |  |
| 771 | Label the throughput metric with the implant dose | SF-RP-003 | denied | decided fresh | — | ● |
| 772 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | decided fresh | — |  |
| 773 | Verify the audit chain after the metrology schema migration | SF-WI-004 | permitted | decided fresh | — |  |
| 774 | Publish the measurement window with the latency result | SF-RT-007 | permitted | decided fresh | — |  |
| 775 | Add the newly pulled component to the generated SBOM | SF-SS-005 | permitted | disposed by citation | — |  |
| 776 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 777 | Attribute every metrology record amendment to a named operator | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 778 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-008 | permitted | decided fresh | — |  |
| 779 | Rewrite historical ledger rows during the partition migration | SF-WI-002 ⛔ | denied | refused at the floor | — |  |
| 780 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted with conditions | decided fresh | — | ● |
| 781 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh | — | ● |
| 782 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-003 | permitted | decided fresh | — |  |
| 783 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-003 | permitted | decided fresh | — |  |
| 784 | Move recipe transfer onto the mutually authenticated channel | SF-RP-005 | permitted with conditions | decided fresh | — | ● |
| 785 | Serialise the two writers to the yield aggregation table | SF-TQ-004 | permitted | decided fresh | — |  |
| 786 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-005 | permitted | decided fresh | — |  |
| 787 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted | decided fresh | — |  |
| 788 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted | decided fresh | — |  |
| 789 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 790 | Reclassify the recipe-protection provision as advisory | SF-QS-001 | denied | decided fresh | — |  |
| 791 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 792 | Add the enrichment lookup to the alarm path despite the tail regression | SF-RT-001 | denied | decided fresh | — |  |
| 793 | Hide the appeal button on the automated screening result page | SF-GV-001 SF-AS-001 ⛔ | denied | refused at the floor | — |  |
| 794 | Parallelise the SECS message dispatcher across four workers | SF-SG-003 | denied | decided fresh | — |  |
| 795 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted | decided fresh after a tie | none_tie |  |
| 796 | Surface the applicable ECCN on the supplier portal download page | SF-EX-010 | permitted | decided fresh | — |  |
| 797 | Rotate the recipe vault envelope key on the published schedule | SF-RP-006 | permitted | decided fresh | — |  |
| 798 | Add fuzz coverage for the metrology file upload handler | SF-AS-002 | permitted with conditions | decided fresh | — | ● |
| 799 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 800 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 801 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-002 | permitted | decided fresh | — |  |
| 802 | Record the outbound-investment determination before a joint-venture data share opens | SF-SO-003 | permitted | decided fresh | — |  |
| 803 | Route every boycott-request match to the quarterly filing queue | SF-SO-003 | permitted | decided fresh | — |  |
| 804 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted with conditions | decided fresh | — | ● |
| 805 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | decided fresh | — |  |
| 806 | Ship the in-country support tunnel with the access question still open | SF-DS-002 SF-GV-006 ⛔ | denied | refused at the floor | — |  |
| 807 | Rotate the recipe vault signing key on the published schedule | SF-CR-005 | permitted | decided fresh | — |  |
| 808 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-007 | permitted | decided fresh | — |  |
| 809 | Separate the reporter bulletin from the adjudication input path | SF-GV-007 | permitted | decided fresh | — |  |
| 810 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | decided fresh | — |  |
| 811 | Post a compensating entry instead of editing the WIP status | SF-WI-001 ⛔ | permitted | decided fresh | — |  |
| 812 | Sign the release attestation with the developer's own runner identity | SF-SS-009 | denied | decided fresh | — |  |
| 813 | Remove the verification-of-effectiveness step from the corrective-action workflow | SF-QS-001 | denied | decided fresh | — |  |
| 814 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-002 | permitted | decided fresh | — |  |
| 815 | Add the pilot line to the CUI boundary documentation | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 816 | Document the CUI boundary for the metrology ingest service | SF-NC-005 | permitted | decided fresh | — |  |
| 817 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 818 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 819 | Keep the HSMS reply timeout inside the declared bound | SF-SG-003 | permitted | decided fresh | — |  |
| 820 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 821 | Replace the pickle payload with a schema-validated JSON body | SF-AS-001 | permitted | decided fresh | — |  |
| 822 | Scope the internal SECS parser package to the private registry | SF-SS-011 | permitted | decided fresh | — |  |
| 823 | Downsample cleanroom particle-count telemetry without recording the change | SF-EH-004 | denied | decided fresh | — |  |
| 824 | Persist every effluent monitoring result before report aggregation runs | SF-EH-002 ⛔ | permitted | decided fresh | — |  |
| 825 | Record the builder identity in the release attestation | SF-SS-005 | permitted | decided fresh | — |  |
| 826 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | disposed by citation | — |  |
| 827 | Add the newly pulled component to the generated SBOM | SF-SS-004 | permitted | decided fresh | — | ● |
| 828 | Bound the request body size on the yield analytics endpoint | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 829 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-011 | permitted | disposed by citation | — |  |
| 830 | Restrict the webhook fetcher to the registered supplier hosts | — | permitted | docketed — nothing engaged | — |  |
| 831 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 832 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | decided fresh | — |  |
| 833 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-002 | permitted | decided fresh | — |  |
| 834 | Record the jurisdiction determination before a defence-adjacent file is ingested | SF-IT-002 | permitted | decided fresh | — |  |
| 835 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-002 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 836 | Surface unparsed equipment replies instead of dropping them | SF-SG-007 | permitted | decided fresh | — | ● |
| 837 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — |  |
| 838 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-002 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 839 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 840 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-002 | permitted | decided fresh | — |  |
| 841 | Strip process parameters from telemetry metric labels | SF-RP-007 | permitted | decided fresh | — |  |
| 842 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted | decided fresh | — |  |
| 843 | Retry S2F41 remote commands without reordering the queue | SF-SG-001 ⛔ | permitted | decided fresh | — |  |
| 844 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 845 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted | decided fresh | — |  |
| 846 | Verify the audit chain after the metrology schema migration | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 847 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted | decided fresh | — |  |
| 848 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted | decided fresh | — |  |
| 849 | Record the builder identity in the release attestation | SF-SS-001 ⛔ | permitted | decided fresh | — |  |
| 850 | Ingest the new radar-module design files ahead of the classification review | SF-IT-004 | denied | decided fresh | — | ● |
| 851 | Resolve the foreign access request through the named legal channel | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 852 | Retry S2F41 remote commands without reordering the queue | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 853 | Report load conditions alongside the p99.9 measurement | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 854 | Record the percentile family used for the declared budget | SF-RT-001 | permitted | decided fresh | — |  |
| 855 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | disposed by citation | — |  |
| 856 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 857 | Accept a pickled analysis payload from the supplier portal | SF-AS-001 | denied | decided fresh | — |  |
| 858 | Attribute every metrology record amendment to a named operator | SF-WI-007 | permitted | decided fresh | — |  |
| 859 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted | decided fresh | — |  |
| 860 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-003 ⛔ | permitted | decided fresh | — |  |
| 861 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted | decided fresh | — |  |
| 862 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted | decided fresh | — |  |
| 863 | Cache the sanctions list snapshot for a month to cut screening latency | SF-SO-003 | denied | decided fresh | — |  |
| 864 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 865 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted | decided fresh | — |  |
| 866 | Version the supplier declaration record on every effective-date change | SF-RS-002 ⛔ | permitted | decided fresh | — |  |
| 867 | Return the exception detail to the portal so suppliers can self-diagnose | SF-AS-002 | denied | decided fresh | — |  |
| 868 | Amend the consolidation class threshold in the parameters file | SF-SG-003 | denied | decided fresh | — |  |
| 869 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | decided fresh | — | ● |
| 870 | Pull tool firmware updates from an unverified community mirror | SF-OT-002 | denied | decided fresh | — |  |
| 871 | Attach an agent provenance attestation to the generated migration | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 872 | Allowlist the export format instead of shelling out with user input | SF-AS-007 | permitted | docketed — not charged | — |  |
| 873 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-003 ⛔ | permitted | decided fresh | — |  |
| 874 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — |  |
| 875 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted | decided fresh | — |  |
| 876 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 877 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted | decided fresh | — |  |
| 878 | Attach qualification evidence to every process-change record | SF-QS-001 | permitted | decided fresh | — |  |
| 879 | Merge the agent's patch importing a SECS helper nobody can find | SF-AG-001 SF-AS-001 ⛔ | denied | refused at the floor | — |  |
| 880 | Move recipe transfer onto the mutually authenticated channel | SF-RP-001 ⛔ | permitted | decided fresh | — |  |
| 881 | Resolve the foreign access request through the named legal channel | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 882 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted | disposed by citation | — |  |
| 883 | Raise the gas-alarm threshold in the config file without an EHS signoff record | SF-EH-003 SF-RT-002 ⛔ | denied | refused at the floor | — |  |
| 884 | Sign the container image published for the edge tool gateway | SF-SS-005 | permitted | decided fresh | — |  |
| 885 | Record the builder identity in the release attestation | SF-SS-005 | permitted | decided fresh | — |  |
| 886 | Replace the direct-URL dependency with a registry release | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 887 | Let compliance edit the export determination after the shipment closes | SF-EX-003 SF-OT-001 ⛔ | denied | refused at the floor | — |  |
| 888 | Keep audit logging on during the throughput optimisation | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 889 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-001 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 890 | Record the agent identity and model version on the pull request | SF-AG-001 ⛔ | permitted | decided fresh | — |  |
| 891 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 892 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted with conditions | decided fresh | — | ● |
| 893 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-003 | permitted | decided fresh | — |  |
| 894 | Require named-owner approval per vendor remote session | SF-OT-003 | permitted | decided fresh | — |  |
| 895 | Log the citizenship attribute alongside every ITAR access event | SF-IT-003 ⛔ | permitted | decided fresh | — |  |
| 896 | Record the agent identity and model version on the pull request | SF-AG-002 ⛔ | permitted | decided fresh | — |  |
| 897 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted | decided fresh | — |  |
| 898 | Surface unparsed equipment replies instead of dropping them | SF-SG-006 | permitted | decided fresh | — |  |
| 899 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | decided fresh | — |  |
| 900 | Write our own MAC so the vault avoids the library dependency | SF-CR-004 | denied | decided fresh | — |  |
| 901 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted with conditions | decided fresh | — | ● |
| 902 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | decided fresh | — | ● |
| 903 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 904 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 905 | Surface unparsed equipment replies instead of dropping them | SF-SG-006 | permitted | decided fresh | — | ● |
| 906 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 907 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted | decided fresh | — |  |
| 908 | Purge recipe execution records older than ninety days | SF-WI-001 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 909 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted | decided fresh | — |  |
| 910 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | decided fresh | — |  |
| 911 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | decided fresh | — |  |
| 912 | Fail the pipeline closed when the screening service times out | SF-EX-005 ⛔ | permitted | decided fresh | — |  |
| 913 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 914 | Widen the data residency provision to permit group-A replicas | SF-RS-001 | denied | decided fresh | — |  |
| 915 | Verify component digests against the registry before deploy | SF-SS-004 | permitted | decided fresh | — |  |
| 916 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted | decided fresh | — |  |
| 917 | Log the deemed-export check that runs at repository role grant | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 918 | Record the agent identity and model version on the pull request | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 919 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 920 | Publish the measurement window with the latency result | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 921 | Replicate the Dresden yield warehouse into the US analytics cluster | SF-DS-001 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 922 | Surface unparsed equipment replies instead of dropping them | SF-SG-002 ⛔ | permitted | decided fresh | — |  |
| 923 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 924 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 925 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 926 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 927 | Keep recipe execution records until the retention clock expires | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 928 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 929 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 930 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-001 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 931 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 932 | Pin the JVM collector so pause times stay inside the budget | SF-RT-002 | permitted | decided fresh | — |  |
| 933 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 934 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 935 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 936 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | decided fresh | — | ● |
| 937 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted | decided fresh | — |  |
| 938 | Record the builder identity in the release attestation | SF-SS-008 | permitted | decided fresh | — |  |
| 939 | Resolve the foreign access request through the named legal channel | SF-DS-002 ⛔ | permitted | decided fresh | — |  |
| 940 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-001 | permitted | bound by precedent | REC-S0053 |  |
| 941 | Bound the request body size on the yield analytics endpoint | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 942 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | permitted with conditions | bound by precedent | REC-SF-G-00933 |  |
| 943 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-004 | denied | decided fresh | — |  |
| 944 | Record the percentile family used for the declared budget | SF-RT-007 | permitted with conditions | bound by precedent | REC-SF-G-00903 |  |
| 945 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-001 ⛔ | denied | refused at the floor | — |  |
| 946 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-004 | permitted | bound by precedent | REC-S0072 |  |
| 947 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-001 ⛔ | permitted | decided fresh | — |  |
| 948 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-B-00902 | ● |
| 949 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-002 SF-EX-010 ⛔ | denied | refused at the floor | — |  |
| 950 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | bound by precedent | REC-SF-N-00936 |  |
| 951 | Keep the appeal route on the automated screening decision | SF-GV-007 | permitted with conditions | decided fresh | — | ● |
| 952 | Preserve S6F11 event ordering under broker backpressure | SF-SG-003 | permitted | bound by precedent | REC-S0012 |  |
| 953 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 954 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | bound by precedent | REC-SF-N-00613 |  |
| 955 | Raise the gas-alarm threshold in the config file without an EHS signoff record | SF-EH-004 | denied | decided fresh | — |  |
| 956 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | bound by precedent | REC-SF-L-00836 | ● |
| 957 | Separate the reporter bulletin from the adjudication input path | SF-GV-005 | permitted with conditions | decided fresh | — | ● |
| 958 | Verify the artifact signature before the tool gateway installs it | SF-CR-002 | permitted | bound by precedent | REC-SF-A-00590 |  |
| 959 | Enforce the protocol allowlist at every zone boundary | SF-OT-004 | permitted | decided fresh | — |  |
| 960 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted | decided fresh | — |  |
| 961 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | decided fresh | — | ● |
| 962 | Broker vendor remote sessions through the jump host | SF-OT-001 | permitted | bound by precedent | REC-S0078 |  |
| 963 | Document the invariant the metrology ingest lock protects | SF-TQ-001 | permitted | decided fresh | — |  |
| 964 | Document the invariant the metrology ingest lock protects | SF-TQ-001 | permitted | decided fresh | — |  |
| 965 | Add the newly pulled component to the generated SBOM | SF-SS-005 | denied | bound by precedent | REC-S0040 |  |
| 966 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 967 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | bound by precedent | REC-SF-A-00649 | ● |
| 968 | Let the batch corrector amend metrology rows without a named operator | SF-WI-001 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 969 | Move the charging threshold for the supply chain family | SF-EX-012 | denied | decided fresh | — |  |
| 970 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | bound by precedent | REC-SF-G-00846 |  |
| 971 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | disposed by citation | — |  |
| 972 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted with conditions | bound by precedent | REC-SF-G-00927 |  |
| 973 | Let the shipment proceed when the screening service returns a timeout | SF-EX-005 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 974 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | permitted | decided fresh | — |  |
| 975 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00967 | ● |
| 976 | Log the deemed-export check that runs at repository role grant | SF-EX-006 ⛔ | permitted | decided fresh | — |  |
| 977 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | denied | bound by precedent | REC-S0013 |  |
| 978 | Ingest the new radar-module design files ahead of the classification review | SF-IT-003 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 979 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-SF-N-00936 |  |
| 980 | Give the vendor a persistent VPN connection instead of a brokered session | SF-OT-001 | denied | decided fresh | — |  |
| 981 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | bound by precedent | REC-S0027 | ● |
| 982 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 983 | Sign the container image published for the edge tool gateway | SF-SS-004 | permitted | decided fresh | — |  |
| 984 | Rate-limit the supplier portal's document download endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 985 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-004 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 986 | Update the supply chain risk plan after the vendor change | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 987 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted with conditions | bound by precedent | REC-SF-S-00851 |  |
| 988 | Link each claimed control to its implementation statement | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 989 | Pin the certificate chain used by the metrology ingest client | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 990 | Move the defence-enclave backup into the general-purpose cloud region for cheaper storage | SF-IT-001 SF-EX-007 ⛔ | denied | refused at the floor | — |  |
| 991 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | bound by precedent | REC-SF-A-00256 | ● |
| 992 | Expand the classification questionnaire for multi-patterning masks | SF-EX-002 ⛔ | permitted | decided fresh | — |  |
| 993 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 994 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 995 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 996 | Record and time-box every vendor remote-access session | SF-OT-003 | permitted | bound by precedent | REC-S0080 | ● |
| 997 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | disposed by citation | — |  |
| 998 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 999 | Write the full rationale trail at the moment of resolution | SF-GV-004 | permitted | decided fresh | — |  |
| 1000 | Write the full rationale trail at the moment of resolution | SF-GV-004 | permitted | decided fresh | — |  |
| 1001 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00975 |  |
| 1002 | Link each claimed control to its implementation statement | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 1003 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-003 | permitted with conditions | bound by precedent | REC-S0062 | ● |
| 1004 | Verify the audit chain after the metrology schema migration | SF-WI-003 | permitted | decided fresh | — |  |
| 1005 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted | decided fresh | — |  |
| 1006 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — |  |
| 1007 | Add the newly pulled component to the generated SBOM | SF-SS-006 | permitted | bound by precedent | REC-SF-A-00688 |  |
| 1008 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 1009 | Return a correlation id instead of a stack trace to the client | SF-AS-001 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 1010 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 1011 | Add a negative test for a tampered recipe signature | SF-CR-002 | denied | bound by precedent | REC-S0054 |  |
| 1012 | Keep recipe text out of the yield model's prompt context | SF-RP-002 ⛔ | permitted | decided fresh | — |  |
| 1013 | Link the agent's change to the originating engineering ticket | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00975 |  |
| 1014 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-001 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 1015 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-004 | permitted with conditions | bound by precedent | REC-S0063 | ● |
| 1016 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted | decided fresh | — |  |
| 1017 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1018 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1019 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted | bound by precedent | REC-SF-L-00869 |  |
| 1020 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 1021 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | denied | bound by precedent | REC-S0044 |  |
| 1022 | Expand the classification questionnaire for multi-patterning masks | SF-EX-001 ⛔ | permitted | decided fresh | — |  |
| 1023 | Downgrade a fuzzy sanctions-list near-miss to a documented false positive after two-person review | SF-SO-003 | permitted | bound by precedent | REC-S0069 |  |
| 1024 | Close the check-then-open window in the metrology file handler | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 1025 | Enforce the customer's notice period at the release gate | SF-QS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1026 | Update the supply chain risk plan after the vendor change | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 1027 | Add the destination geofence to the design-file download path | SF-EX-010 | permitted | decided fresh | — |  |
| 1028 | Log the deemed-export check that runs at repository role grant | SF-EX-010 | permitted | decided fresh | — |  |
| 1029 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 1030 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | denied | bound by precedent | REC-S0007 |  |
| 1031 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-002 | permitted | decided fresh | — |  |
| 1032 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-B-00440 | ● |
| 1033 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | decided fresh | — | ● |
| 1034 | Add an authorisation check to the lot-detail API | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1035 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-S0045 | ● |
| 1036 | Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path | SF-OT-002 | permitted | decided fresh | — |  |
| 1037 | Record and time-box every vendor remote-access session | SF-OT-002 | permitted | decided fresh | — |  |
| 1038 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | denied | bound by precedent | REC-S0013 | ● |
| 1039 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 1040 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 |  |
| 1041 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-004 | permitted | decided fresh | — | ● |
| 1042 | Verify the audit chain after the metrology schema migration | SF-WI-007 | permitted | decided fresh | — |  |
| 1043 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-003 | permitted | bound by precedent | REC-S0080 |  |
| 1044 | Downgrade a fuzzy sanctions-list near-miss to a documented false positive after two-person review | SF-SO-001 ⛔ | permitted | decided fresh | — |  |
| 1045 | Add the covered-transaction determination field to the tool purchase record | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 1046 | Publish the measurement window with the latency result | SF-RT-001 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 1047 | Show the human review route on the screening decision page | SF-GV-002 ⛔ | permitted | decided fresh | — |  |
| 1048 | Redact recipe parameters from the tool-gateway debug log | SF-RP-006 | permitted | decided fresh | — |  |
| 1049 | Move recipe transfer onto the mutually authenticated channel | SF-RP-006 | permitted | decided fresh | — |  |
| 1050 | Pull the ingest parser from a mirror whose digest no longer matches | SF-SS-001 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 1051 | Version collection-event identifiers instead of renumbering them | SF-SG-009 | permitted | bound by precedent | REC-SF-A-00055 | ● |
| 1052 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-002 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 1053 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | bound by precedent | REC-SF-C-00956 |  |
| 1054 | Document the invariant the metrology ingest lock protects | SF-TQ-003 | permitted | decided fresh | — |  |
| 1055 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 1056 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | decided fresh | — |  |
| 1057 | Collect smelter-and-refiner identity data during supplier onboarding | SF-RS-001 | denied | bound by precedent | REC-S0070 |  |
| 1058 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted | disposed by citation | — |  |
| 1059 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted | bound by precedent | REC-S0006 | ● |
| 1060 | Exempt distributor accounts from the sanctions screening step | SF-SO-001 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 1061 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | bound by precedent | REC-SF-B-00728 |  |
| 1062 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | decided fresh | — |  |
| 1063 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00981 | ● |
| 1064 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | permitted | decided fresh | — | ● |
| 1065 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | decided fresh | — |  |
| 1066 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-001 SF-SG-004 ⛔ | denied | refused at the floor | — |  |
| 1067 | Fail the pipeline closed when the screening service times out | SF-EX-012 | denied | bound by precedent | REC-S0005 |  |
| 1068 | Fail the pipeline closed when the screening service times out | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 1069 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted with conditions | bound by precedent | REC-SF-G-00927 |  |
| 1070 | Clear a grey-market flag only after a recorded provenance disposition | SF-RS-004 | permitted | decided fresh | — |  |
| 1071 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-004 | permitted | decided fresh | — |  |
| 1072 | Publish the standing declaration in the compliance export | SF-GV-003 | permitted | decided fresh | — |  |
| 1073 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-003 | permitted | decided fresh | — |  |
| 1074 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted | bound by precedent | REC-S0003 | ● |
| 1075 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-007 | denied | decided fresh | — | ● |
| 1076 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | bound by precedent | REC-SF-N-00258 |  |
| 1077 | Replace the direct-URL dependency with a registry release | SF-SS-011 | permitted | decided fresh | — |  |
| 1078 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-003 | denied | decided fresh | — |  |
| 1079 | Keep the appeal route on the automated screening decision | SF-GV-005 | permitted | bound by precedent | REC-S0064 | ● |
| 1080 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted | decided fresh | — | ● |
| 1081 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 1082 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 1083 | Add the realised adverse-contest rate to the governance export | SF-GV-007 | denied | bound by precedent | REC-S0066 |  |
| 1084 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-001 ⛔ | permitted | decided fresh | — |  |
| 1085 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | decided fresh | — |  |
| 1086 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 1087 | Capture the licence determination rationale in the trade record | SF-EX-007 | permitted with conditions | bound by precedent | REC-SF-G-00933 |  |
| 1088 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted | decided fresh | — |  |
| 1089 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | decided fresh | — | ● |
| 1090 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted with conditions | bound by precedent | REC-SF-U-01086 |  |
| 1091 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-004 | permitted | decided fresh | — |  |
| 1092 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-004 | permitted | decided fresh | — |  |
| 1093 | Keep the lockout/tagout state read-only in the software layer | SF-EH-001 ⛔ | permitted | decided fresh | — |  |
| 1094 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | bound by precedent | REC-SF-L-00836 |  |
| 1095 | Record the exception authority against the accepting principal | SF-GV-004 | permitted | decided fresh | — |  |
| 1096 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 |  |
| 1097 | Default every uncatalogued defence article to the commerce control list | SF-IT-004 | denied | decided fresh | — |  |
| 1098 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01080 | ● |
| 1099 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1100 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted | bound by precedent | REC-SF-L-00679 |  |
| 1101 | Accept recipe transfers from any host on the tool VLAN | SF-SG-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 1102 | Add a GEM control-state transition test for the Lam etcher | SF-SG-005 | permitted | bound by precedent | REC-SF-L-00004 |  |
| 1103 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 1104 | Make export decisions append-only in the trade compliance ledger | SF-EX-008 | denied | bound by precedent | REC-S0002 |  |
| 1105 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | permitted | decided fresh | — |  |
| 1106 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted with conditions | bound by precedent | REC-SF-U-01086 | ● |
| 1107 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted | decided fresh | — |  |
| 1108 | Require the licence exception paragraph on the shipment record | SF-EX-009 | permitted | decided fresh | — |  |
| 1109 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-003 | permitted | bound by precedent | REC-SF-C-00996 |  |
| 1110 | Accept a counterparty's boycott-neutral standard clause after legal review | SF-SO-002 ⛔ | permitted | decided fresh | — |  |
| 1111 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted with conditions | bound by precedent | REC-SF-S-01068 |  |
| 1112 | Surface the applicable ECCN on the supplier portal download page | SF-EX-004 ⛔ | permitted | decided fresh | — |  |
| 1113 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted | bound by precedent | REC-SF-L-00869 |  |
| 1114 | Publish the measurement window with the latency result | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 1115 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | bound by precedent | REC-S0041 |  |
| 1116 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | decided fresh | — |  |
| 1117 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-005 | permitted | decided fresh | — |  |
| 1118 | Move portal document storage to a new vendor without naming its region | SF-DS-003 | denied | decided fresh | — | ● |
| 1119 | Attach the provenance attestation to the tool-gateway release | SF-SS-004 | permitted | bound by precedent | REC-S0039 |  |
| 1120 | Let the coding agent rewrite the tool command dispatcher | SF-AG-001 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 1121 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1122 | Rate-limit gas-detector alarm delivery to one page per minute | SF-EH-001 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 1123 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | bound by precedent | REC-SF-N-00613 |  |
| 1124 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-007 | denied | decided fresh | — |  |
| 1125 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1126 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | bound by precedent | REC-SF-N-00148 |  |
| 1127 | Preserve S6F11 event ordering under broker backpressure | SF-SG-005 | permitted | disposed by citation | — |  |
| 1128 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-001 | permitted with conditions | bound by precedent | REC-S0020 | ● |
| 1129 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 1130 | Move key material into the hardware security module | SF-CR-002 | permitted | bound by precedent | REC-SF-A-00590 |  |
| 1131 | Close the equipment joint-venture deal before the transaction-review checklist runs | SF-SO-002 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 1132 | Link the agent's change to the originating engineering ticket | SF-AG-006 | permitted | bound by precedent | REC-S0050 |  |
| 1133 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 1134 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 1135 | Split the slow enrichment step out of the alarm path | SF-RT-005 | permitted | decided fresh | — |  |
| 1136 | Move the alarm-fanout write off the monitoring hot path | SF-RT-005 | permitted | decided fresh | — |  |
| 1137 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00975 |  |
| 1138 | Split the slow enrichment step out of the alarm path | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 1139 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-002 | permitted | decided fresh | — |  |
| 1140 | Verify tool firmware signatures against the vendor key before install | SF-OT-002 | permitted | decided fresh | — |  |
| 1141 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-010 | denied | decided fresh | — |  |
| 1142 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 1143 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted | bound by precedent | REC-S0003 |  |
| 1144 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — |  |
| 1145 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1146 | Disable a vendor's remote-access account between sessions | SF-OT-004 | denied | bound by precedent | REC-S0081 |  |
| 1147 | Drop the deprecated field from the agent's regenerated response body | SF-AG-002 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 1148 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01080 |  |
| 1149 | Add a licence-exception clause to the trade compliance rulebook | SF-AG-004 | denied | decided fresh | — |  |
| 1150 | Add a retention-hold check to the record destruction job | SF-WI-006 | denied | bound by precedent | REC-S0030 |  |
| 1151 | Batch alarm reports into the five-second telemetry flush | SF-SG-002 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 1152 | Release the broker-sourced lot from quarantine before the provenance chain is verified | SF-RS-002 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 1153 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | bound by precedent | REC-SF-B-00080 |  |
| 1154 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 1155 | Add a configuration flag that releases blocked-property holds for expedited orders | SF-SO-002 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 1156 | Report load conditions alongside the p99.9 measurement | SF-RT-005 | denied | bound by precedent | REC-S0024 |  |
| 1157 | Renumber the collection event identifiers to close the gaps | SF-SG-003 | denied | decided fresh | — |  |
| 1158 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-C-01032 |  |
| 1159 | Add the newly pulled component to the generated SBOM | SF-SS-002 | permitted | decided fresh | — |  |
| 1160 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | decided fresh | — |  |
| 1161 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-001 ⛔ | denied | refused at the floor | — |  |
| 1162 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | bound by precedent | REC-SF-A-00256 |  |
| 1163 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted | decided fresh | — |  |
| 1164 | Record the exception authority against the accepting principal | SF-GV-003 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1165 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-002 | permitted | decided fresh | — |  |
| 1166 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | denied | bound by precedent | REC-S0022 |  |
| 1167 | Rate-limit the supplier portal's document download endpoint | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 1168 | Add a residency assertion to the metrology ingest contract | SF-DS-007 | permitted with conditions | bound by precedent | REC-SF-S-00993 |  |
| 1169 | Record the jurisdiction determination before a defence-adjacent file is ingested | SF-IT-001 ⛔ | permitted | decided fresh | — |  |
| 1170 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted | bound by precedent | REC-S0028 |  |
| 1171 | Fail the pipeline closed when the screening service times out | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 1172 | Exclude recipe bodies from the vendor support bundle | SF-RP-007 | permitted | bound by precedent | REC-S0036 |  |
| 1173 | Benchmark the broker with an open-loop client and report the median | SF-RT-001 | denied | decided fresh | — |  |
| 1174 | Add a GEM control-state transition test for the Lam etcher | SF-SG-005 | permitted | bound by precedent | REC-SF-L-00160 | ● |
| 1175 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted | disposed by citation | — |  |
| 1176 | Make the audit register append-only and disjoint from the store | SF-GV-007 | denied | bound by precedent | REC-S0066 |  |
| 1177 | Document the invariant the metrology ingest lock protects | — | permitted | docketed — nothing engaged | — |  |
| 1178 | Retire the superseded cryptographic floor from the constitution | SF-EX-013 | denied | decided fresh | — |  |
| 1179 | Let the retention sweep run across lots that are under legal hold | SF-DS-002 SF-EX-008 ⛔ | denied | refused at the floor | — |  |
| 1180 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 | ● |
| 1181 | Encrypt the recipe payload at rest in the vault | SF-RP-005 | permitted | decided fresh | — |  |
| 1182 | Keep recipe text out of the yield model's prompt context | SF-RP-005 | permitted | decided fresh | — |  |
| 1183 | Add a residency assertion to the metrology ingest contract | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 1184 | Correct for coordinated omission in the ingest benchmark | SF-RT-002 | permitted with conditions | bound by precedent | REC-S0021 |  |
| 1185 | Re-enable the legacy cipher suite so the older scanner can connect | SF-CR-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 1186 | Record the ownership data source and snapshot date on every screening result | SF-SO-003 | permitted | bound by precedent | REC-S0069 |  |
| 1187 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 1188 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-B-00961 |  |
| 1189 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-002 ⛔ | permitted | decided fresh | — |  |
| 1190 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted | decided fresh | — |  |
| 1191 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted | decided fresh | — |  |
| 1192 | Return a correlation id instead of a stack trace to the client | SF-AS-001 | permitted | decided fresh | — | ● |
| 1193 | Require named-owner approval per vendor remote session | SF-OT-003 | permitted | bound by precedent | REC-S0080 |  |
| 1194 | Reject signatures the verifier previously accepted by mistake | SF-CR-002 | permitted | decided fresh | — |  |
| 1195 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | decided fresh after a tie | none_tie |  |
| 1196 | Version collection-event identifiers instead of renumbering them | SF-SG-003 | permitted | bound by precedent | REC-S0012 |  |
| 1197 | Derive a fresh nonce per recipe encryption operation | SF-CR-001 ⛔ | permitted | decided fresh | — |  |
| 1198 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-004 | permitted | bound by precedent | REC-S0028 | ● |
| 1199 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted | decided fresh | — |  |
| 1200 | Fail the pipeline closed when the screening service times out | SF-EX-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1201 | Rewrite historical ledger rows during the partition migration | SF-WI-001 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 1202 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | bound by precedent | REC-SF-L-00869 | ● |
| 1203 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted | decided fresh | — |  |
| 1204 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 1205 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | decided fresh | — |  |
| 1206 | Carry the regulatory hold flag through the archive migration | SF-WI-006 | permitted | bound by precedent | REC-SF-A-00058 |  |
| 1207 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 1208 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1209 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-002 | permitted | decided fresh | — |  |
| 1210 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 1211 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 1212 | Record the percentile family used for the declared budget | SF-RT-005 | denied | bound by precedent | REC-S0024 | ● |
| 1213 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted | decided fresh | — |  |
| 1214 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | bound by precedent | REC-SF-L-00115 | ● |
| 1215 | Bound the request body size on the yield analytics endpoint | SF-AS-003 | permitted | disposed by citation | — |  |
| 1216 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 1217 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | denied | bound by precedent | REC-SF-C-01038 |  |
| 1218 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh | — |  |
| 1219 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 1220 | Raise the latency budget stated in the constitutional parameters | SF-RT-001 | denied | decided fresh | — |  |
| 1221 | Update the supply chain risk plan after the vendor change | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 1222 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted with conditions | bound by precedent | REC-SF-U-01086 | ● |
| 1223 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-002 | permitted | decided fresh | — |  |
| 1224 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-002 | permitted | decided fresh | — |  |
| 1225 | Attribute every metrology record amendment to a named operator | SF-WI-006 | permitted | bound by precedent | REC-SF-A-00058 |  |
| 1226 | Fail closed on receipt when a forced-labour list match is returned | SF-RS-001 | permitted | decided fresh | — |  |
| 1227 | Record the counterfeit-inspection result and distributor-authorisation status per lot | SF-RS-001 | permitted | decided fresh | — |  |
| 1228 | Parameterise the supplier portal's lot-search query | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1229 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1230 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted | decided fresh | — |  |
| 1231 | Route every screening near-miss to a named compliance reviewer | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 |  |
| 1232 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | permitted | decided fresh | — |  |
| 1233 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1234 | Write our own MAC so the vault avoids the library dependency | SF-CR-005 | denied | decided fresh | — |  |
| 1235 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-007 | denied | bound by precedent | REC-SF-B-01075 |  |
| 1236 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | decided fresh | — |  |
| 1237 | Replace the pickle payload with a schema-validated JSON body | SF-AS-001 | permitted | bound by precedent | REC-SF-L-01192 |  |
| 1238 | Assert the safety interlock signal survives the gateway refactor | SF-SG-004 | permitted | decided fresh | — |  |
| 1239 | Record the exception authority against the accepting principal | SF-GV-004 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1240 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 1241 | Rotate the recipe vault envelope key on the published schedule | SF-RP-003 | permitted | bound by precedent | REC-SF-A-00339 |  |
| 1242 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 1243 | Link the agent's change to the originating engineering ticket | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00975 |  |
| 1244 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-003 | permitted | decided fresh | — |  |
| 1245 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | bound by precedent | REC-S0029 | ● |
| 1246 | Redact recipe parameters from the tool-gateway debug log | SF-RP-003 | permitted | decided fresh | — |  |
| 1247 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted | bound by precedent | REC-SF-A-00649 |  |
| 1248 | Document the invariant the metrology ingest lock protects | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 1249 | Require the licence exception paragraph on the shipment record | SF-EX-009 | permitted | bound by precedent | REC-S0003 |  |
| 1250 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted | decided fresh | — |  |
| 1251 | Require the licence exception paragraph on the shipment record | SF-EX-009 | permitted | decided fresh | — |  |
| 1252 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-006 | permitted | decided fresh | — |  |
| 1253 | Keep recipe text out of the yield model's prompt context | SF-RP-006 | permitted | decided fresh | — |  |
| 1254 | Make the audit register append-only and disjoint from the store | SF-GV-004 | permitted with conditions | bound by precedent | REC-SF-C-01015 |  |
| 1255 | Move the charging threshold into the constitutional parameters file | SF-GV-007 | permitted | decided fresh | — |  |
| 1256 | Version the supplier declaration record on every effective-date change | SF-RS-004 | permitted | bound by precedent | REC-S0072 |  |
| 1257 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 1258 | Show the human review route on the screening decision page | SF-GV-004 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1259 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh | — | ● |
| 1260 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-C-01180 |  |
| 1261 | Ship the ingest rewrite with the worst-case spike still unexplained | SF-RT-001 | denied | decided fresh | — |  |
| 1262 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 1263 | Sign the container image published for the edge tool gateway | SF-SS-005 | permitted | bound by precedent | REC-SF-L-00115 |  |
| 1264 | Document the sub-processor chain for the supplier portal CDN | SF-DS-004 | permitted | decided fresh | — |  |
| 1265 | Assert the safety interlock signal survives the gateway refactor | SF-SG-003 | permitted | decided fresh | — | ● |
| 1266 | Raise the latency budget stated in the constitutional parameters | SF-CR-005 | denied | decided fresh | — |  |
| 1267 | Make export decisions append-only in the trade compliance ledger | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01074 |  |
| 1268 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh | — |  |
| 1269 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted | decided fresh | — |  |
| 1270 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted | bound by precedent | REC-SF-L-00679 | ● |
| 1271 | Join the audit findings table into the precedent retrieval query | SF-GV-006 | denied | decided fresh | — |  |
| 1272 | Attribute corrective-action closure to a named owner | SF-QS-003 | permitted | bound by precedent | REC-SF-A-00470 |  |
| 1273 | Record the percentile family used for the declared budget | SF-RT-005 | permitted | decided fresh | — |  |
| 1274 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | permitted | decided fresh | — |  |
| 1275 | Add fuzz coverage for the metrology file upload handler | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1276 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | bound by precedent | REC-SF-L-00620 |  |
| 1277 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-002 ⛔ | denied | refused at the floor | — |  |
| 1278 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-006 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 1279 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | bound by precedent | REC-S0042 |  |
| 1280 | Make export decisions append-only in the trade compliance ledger | SF-EX-007 | permitted | decided fresh | — |  |
| 1281 | Rewrite historical ledger rows during the partition migration | SF-WI-003 | denied | decided fresh | — |  |
| 1282 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted | decided fresh | — |  |
| 1283 | Amend the consolidation class threshold in the parameters file | SF-SS-008 | denied | decided fresh | — |  |
| 1284 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-007 | denied | bound by precedent | REC-S0066 | ● |
| 1285 | Add a retention-hold check to the record destruction job | SF-WI-007 | permitted | decided fresh | — |  |
| 1286 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | denied | bound by precedent | REC-S0018 |  |
| 1287 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted | decided fresh | — |  |
| 1288 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-002 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1289 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 1290 | Verify tool firmware signatures against the vendor key before install | SF-OT-003 | permitted | bound by precedent | REC-SF-C-00996 |  |
| 1291 | Keep recipe text out of the yield model's prompt context | SF-RP-003 | permitted | decided fresh | — |  |
| 1292 | Bound the SECS message queue depth per tool connection | SF-SG-007 | permitted | bound by precedent | REC-SF-L-00836 |  |
| 1293 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted | decided fresh | — |  |
| 1294 | Expand the classification questionnaire for multi-patterning masks | SF-EX-007 | permitted | decided fresh | — |  |
| 1295 | Hold agent edits to the screening logic for compliance review | SF-AG-008 | permitted with conditions | decided fresh | — | ● |
| 1296 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 | ● |
| 1297 | Round emissions report values down to the nearest permit-limit increment | SF-EH-002 ⛔ | denied | refused at the floor | — |  |
| 1298 | Keep Dresden yield records inside the EU replica set | SF-DS-006 | denied | bound by precedent | REC-S0010 |  |
| 1299 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | decided fresh | — | ● |
| 1300 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-B-00961 | ● |
| 1301 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-004 | permitted with conditions | decided fresh | — | ● |
| 1302 | Redact recipe parameters from the tool-gateway debug log | SF-RP-005 | denied | bound by precedent | REC-S0034 |  |
| 1303 | Store the superseded metrology value beside its correction | SF-WI-007 | permitted | decided fresh | — |  |
| 1304 | Drop the deprecated cipher suites from the supplier portal | SF-CR-004 | denied | bound by precedent | REC-S0056 | ● |
| 1305 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 1306 | Record the percentile family used for the declared budget | SF-RT-005 | permitted with conditions | bound by precedent | REC-SF-G-01138 |  |
| 1307 | Scope recipe vault reads to the owning process integration team | SF-RP-005 | permitted | decided fresh | — |  |
| 1308 | Encrypt ITAR technical data end-to-end before it leaves the authorised boundary | SF-IT-004 | permitted with conditions | bound by precedent | REC-SF-G-01301 |  |
| 1309 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 1310 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | disposed by citation | — |  |
| 1311 | Propose a new provision covering advanced-node lithography data | SF-RP-003 | denied | decided fresh | — |  |
| 1312 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-B-00741 |  |
| 1313 | Scope recipe vault reads to the owning process integration team | SF-RP-005 | permitted | decided fresh | — |  |
| 1314 | Verify every package the agent imported against the registry | SF-AG-005 | denied | bound by precedent | REC-S0049 |  |
| 1315 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | decided fresh | — |  |
| 1316 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted | decided fresh | — |  |
| 1317 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 1318 | Pin the certificate chain used by the metrology ingest client | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1319 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 1320 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-003 | denied | decided fresh | — |  |
| 1321 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted | decided fresh | — |  |
| 1322 | Monitor and alarm on clock drift across the tool network | SF-OT-004 | permitted | decided fresh | — |  |
| 1323 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-003 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1324 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted | decided fresh | — |  |
| 1325 | Assert the safety interlock signal survives the gateway refactor | SF-SG-007 | permitted | bound by precedent | REC-SF-C-00956 |  |
| 1326 | Bound the request body size on the yield analytics endpoint | — | permitted | docketed — nothing engaged | — |  |
| 1327 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-B-00741 | ● |
| 1328 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 1329 | Rotate the recipe vault envelope key on the published schedule | SF-RP-003 | denied | bound by precedent | REC-S0032 |  |
| 1330 | Document the invariant the metrology ingest lock protects | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 1331 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted | bound by precedent | REC-SF-C-01174 |  |
| 1332 | Verify the artifact signature before the tool gateway installs it | SF-CR-003 | permitted | decided fresh | — |  |
| 1333 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | bound by precedent | REC-SF-A-01259 |  |
| 1334 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | decided fresh | — |  |
| 1335 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-007 | denied | bound by precedent | REC-SF-B-01075 |  |
| 1336 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-003 | permitted | decided fresh | — |  |
| 1337 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1338 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-007 | permitted | decided fresh | — |  |
| 1339 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-007 | permitted | decided fresh | — |  |
| 1340 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-005 | denied | decided fresh | — | ● |
| 1341 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | denied | bound by precedent | REC-S0057 |  |
| 1342 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | decided fresh | — |  |
| 1343 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | bound by precedent | REC-SF-A-00486 |  |
| 1344 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 1345 | Store the superseded metrology value beside its correction | SF-WI-007 | denied | bound by precedent | REC-S0031 |  |
| 1346 | Store the superseded metrology value beside its correction | SF-WI-007 | permitted | decided fresh | — |  |
| 1347 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | permitted | decided fresh | — |  |
| 1348 | Bound the SECS message queue depth per tool connection | SF-SG-007 | denied | bound by precedent | REC-S0016 |  |
| 1349 | Retain ESD-monitor telemetry at native resolution for the declared period | SF-EH-004 | permitted | decided fresh | — | ● |
| 1350 | Label the throughput metric with the implant dose | SF-RP-003 | denied | bound by precedent | REC-SF-B-00771 |  |
| 1351 | Add an authorisation check to the lot-detail API | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 1352 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted | bound by precedent | REC-SF-A-00256 |  |
| 1353 | Attach assessment evidence to the claimed access control | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 1354 | Run each build job on a fresh ephemeral runner | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 1355 | Validate the ECCN parameter against the enumerated set | SF-AS-007 | permitted | docketed — not charged | — |  |
| 1356 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | bound by precedent | REC-SF-B-00080 |  |
| 1357 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-001 SF-SS-009 ⛔ | denied | refused at the floor | — |  |
| 1358 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00314 |  |
| 1359 | Swap the hand-rolled MAC for the library primitive | SF-CR-002 | permitted | decided fresh | — |  |
| 1360 | Carry the regulatory hold flag through the archive migration | SF-WI-007 | denied | bound by precedent | REC-S0031 |  |
| 1361 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | decided fresh | — |  |
| 1362 | Label the throughput metric with the implant dose | SF-RP-003 | denied | bound by precedent | REC-SF-B-00771 |  |
| 1363 | Scope recipe vault reads to the owning process integration team | SF-RP-004 | permitted | decided fresh | — |  |
| 1364 | Move recipe transfer onto the mutually authenticated channel | SF-RP-004 | permitted | decided fresh | — |  |
| 1365 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1366 | Assert the safety interlock signal survives the gateway refactor | SF-SG-010 | permitted | decided fresh after a tie | none_tie |  |
| 1367 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-C-01032 |  |
| 1368 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | decided fresh | — | ● |
| 1369 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01074 | ● |
| 1370 | Bound the request body size on the yield analytics endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1371 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 1372 | Parameterise the supplier portal's lot-search query | SF-AS-003 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 1373 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 1374 | Enforce the protocol allowlist at every zone boundary | SF-OT-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 1375 | Validate the ECCN parameter against the enumerated set | SF-AS-007 | permitted | docketed — not charged | — |  |
| 1376 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | bound by precedent | REC-SF-B-00728 | ● |
| 1377 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted | decided fresh | — |  |
| 1378 | Retain ITAR access records for the full five-year floor | SF-IT-004 | permitted with conditions | bound by precedent | REC-SF-G-01301 |  |
| 1379 | Attach the provenance attestation to the tool-gateway release | SF-SS-011 | permitted | decided fresh | — |  |
| 1380 | Verify component digests against the registry before deploy | SF-SS-011 | permitted | decided fresh | — |  |
| 1381 | Record and time-box every vendor remote-access session | SF-OT-001 | permitted | bound by precedent | REC-S0078 | ● |
| 1382 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 1383 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted | bound by precedent | REC-SF-A-00545 |  |
| 1384 | Verify the audit chain after the metrology schema migration | SF-WI-006 | permitted | decided fresh | — |  |
| 1385 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-C-01032 |  |
| 1386 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-012 | permitted | decided fresh | — |  |
| 1387 | Add the destination geofence to the design-file download path | SF-EX-012 | permitted | decided fresh | — |  |
| 1388 | Reject signatures the verifier previously accepted by mistake | SF-CR-002 | permitted | decided fresh | — |  |
| 1389 | Record the effective date on every environmental-sampling change | SF-EH-004 | permitted | bound by precedent | REC-SF-A-01349 |  |
| 1390 | Leave the vendor's remote-access account enabled after the session ends | SF-OT-003 | denied | decided fresh | — | ● |
| 1391 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | bound by precedent | REC-S0042 |  |
| 1392 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 1393 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1394 | Add a scanner for process parameters in application logs | SF-RP-006 | permitted | bound by precedent | REC-SF-N-00316 |  |
| 1395 | Fall back to plain TCP when the tool refuses the TLS handshake | SF-RP-001 SF-RP-006 ⛔ | denied | refused at the floor | — |  |
| 1396 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-001 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 1397 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | bound by precedent | REC-SF-N-00148 |  |
| 1398 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 1399 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | bound by precedent | REC-SF-N-00726 |  |
| 1400 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-007 | denied | decided fresh | — |  |
| 1401 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted with conditions | bound by precedent | REC-SF-G-01295 | ● |
| 1402 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | decided fresh | — |  |
| 1403 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | denied | bound by precedent | REC-S0014 |  |
| 1404 | Promote the APC controller model without wiring a rollback path | SF-QS-002 | denied | decided fresh | — |  |
| 1405 | Strip process parameters from telemetry metric labels | SF-RP-007 | permitted | bound by precedent | REC-S0036 |  |
| 1406 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1407 | Verify the artifact signature before the tool gateway installs it | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1408 | Record firmware provenance on the equipment record at update time | SF-OT-001 | permitted | decided fresh | — |  |
| 1409 | Disable a vendor's remote-access account between sessions | SF-OT-001 | permitted | decided fresh | — |  |
| 1410 | Lower the export-screening strictness in the policy repository | SF-OT-002 | denied | decided fresh | — |  |
| 1411 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-005 | denied | bound by precedent | REC-S0049 | ● |
| 1412 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 1413 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 1414 | Attach assessment evidence to the claimed access control | SF-NC-004 | permitted | decided fresh | — |  |
| 1415 | Route Kumamoto tool logs to the in-region log sink | SF-DS-004 | permitted | bound by precedent | REC-SF-N-01041 |  |
| 1416 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 1417 | Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact | SF-EH-004 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 1418 | Verify component digests against the registry before deploy | SF-SS-007 | permitted | decided fresh | — |  |
| 1419 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | decided fresh | — |  |
| 1420 | Redact recipe parameters from the tool-gateway debug log | SF-RP-006 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 1421 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 1422 | Require named-owner approval per vendor remote session | SF-OT-001 | permitted | bound by precedent | REC-S0078 | ● |
| 1423 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 1424 | Reclassify the recipe-protection provision as advisory | SF-AG-006 | denied | decided fresh | — |  |
| 1425 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01369 | ● |
| 1426 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — |  |
| 1427 | Default an unresolved jurisdiction determination to ITAR pending review | SF-IT-002 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1428 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-002 | denied | decided fresh | — |  |
| 1429 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00981 |  |
| 1430 | Declare the processing region for the new metrology sub-processor | SF-DS-005 | permitted | decided fresh | — |  |
| 1431 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted | decided fresh | — |  |
| 1432 | Pin the denied-party list snapshot used by a screening decision | SF-EX-008 | permitted | decided fresh | — |  |
| 1433 | Report a suspect counterfeit part to the named quality owner before disposition | SF-RS-003 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1434 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-003 | permitted | decided fresh | — |  |
| 1435 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | bound by precedent | REC-SF-L-00620 |  |
| 1436 | Add the destination geofence to the design-file download path | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 1437 | Rate-limit the supplier portal's document download endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 1438 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-SF-N-00936 |  |
| 1439 | Add an authorisation check to the lot-detail API | SF-AS-005 | permitted | docketed — not charged | — |  |
| 1440 | Ingest the new radar-module design files ahead of the classification review | SF-IT-004 | denied | bound by precedent | REC-SF-B-00850 |  |
| 1441 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 1442 | Allowlist the export format instead of shelling out with user input | SF-AS-001 | permitted | bound by precedent | REC-SF-L-01192 |  |
| 1443 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | decided fresh | — |  |
| 1444 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted | bound by precedent | REC-SF-C-01202 |  |
| 1445 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 1446 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-C-00948 |  |
| 1447 | Derive a fresh nonce per recipe encryption operation | SF-CR-002 | permitted | decided fresh | — |  |
| 1448 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-002 | permitted | decided fresh | — |  |
| 1449 | Disable the clock-drift alarm on the equipment time-sync path | SF-OT-004 | denied | decided fresh | — | ● |
| 1450 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted with conditions | bound by precedent | REC-SF-S-01371 |  |
| 1451 | Add an authorisation check to the lot-detail API | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1452 | Hash the recipe identifier before it reaches the analytics store | SF-RP-006 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 1453 | Preserve S6F11 event ordering under broker backpressure | SF-SG-003 | permitted | decided fresh | — |  |
| 1454 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | decided fresh | — |  |
| 1455 | Record the outbound-investment determination before a joint-venture data share opens | SF-SO-003 | permitted with conditions | decided fresh | — | ● |
| 1456 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | decided fresh | — | ● |
| 1457 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-002 SF-RT-001 ⛔ | denied | refused at the floor | — |  |
| 1458 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 |  |
| 1459 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 1460 | Version collection-event identifiers instead of renumbering them | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 |  |
| 1461 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1462 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | bound by precedent | REC-S0041 |  |
| 1463 | Hand the defence-enclave decryption key to the cloud provider's managed key service | SF-IT-003 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 1464 | Sign the container image published for the edge tool gateway | SF-SS-006 | permitted | bound by precedent | REC-S0041 |  |
| 1465 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 1466 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-003 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 1467 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 1468 | Show the human review route on the screening decision page | SF-GV-003 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1469 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | disposed by citation | — |  |
| 1470 | Verify component digests against the registry before deploy | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 1471 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted | decided fresh | — |  |
| 1472 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 | ● |
| 1473 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | disposed by citation | — |  |
| 1474 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-C-00948 |  |
| 1475 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-003 | permitted | decided fresh | — |  |
| 1476 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-003 | permitted | decided fresh | — |  |
| 1477 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh | — |  |
| 1478 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | bound by precedent | REC-SF-L-00219 |  |
| 1479 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-006 | denied | decided fresh | — |  |
| 1480 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | bound by precedent | REC-S0048 |  |
| 1481 | Correct for coordinated omission in the ingest benchmark | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 1482 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00905 |  |
| 1483 | Pin the certificate chain used by the metrology ingest client | SF-CR-006 | permitted | decided fresh | — |  |
| 1484 | Verify the artifact signature before the tool gateway installs it | SF-CR-006 | permitted | decided fresh | — |  |
| 1485 | Swap the hand-rolled MAC for the library primitive | SF-CR-003 | permitted | decided fresh | — |  |
| 1486 | Remove the human-review requirement from the screening provision | SF-GV-006 | denied | decided fresh | — |  |
| 1487 | Keep recipe text out of the yield model's prompt context | SF-RP-006 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 1488 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 1489 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-C-00948 | ● |
| 1490 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted | decided fresh | — |  |
| 1491 | Leave the vendor's remote-access account enabled after the session ends | SF-OT-003 | denied | bound by precedent | REC-SF-B-01390 |  |
| 1492 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted with conditions | decided fresh | — | ● |
| 1493 | Add the newly pulled component to the generated SBOM | SF-SS-005 | permitted | decided fresh | — | ● |
| 1494 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01369 |  |
| 1495 | Map the new component to its NIST control identifier | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 1496 | Monitor and alarm on clock drift across the tool network | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 |  |
| 1497 | Post a compensating entry instead of editing the WIP status | SF-WI-006 | permitted | decided fresh | — |  |
| 1498 | Carry the regulatory hold flag through the archive migration | SF-WI-006 | permitted | decided fresh | — |  |
| 1499 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 1500 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | denied | bound by precedent | REC-S0044 |  |
| 1501 | Record the exception authority against the accepting principal | SF-GV-005 | permitted | decided fresh | — |  |
| 1502 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | bound by precedent | REC-SF-A-01259 | ● |
| 1503 | Capture the licence determination rationale in the trade record | SF-EX-013 | permitted | decided fresh | — |  |
| 1504 | Make export decisions append-only in the trade compliance ledger | SF-EX-013 | permitted | decided fresh | — |  |
| 1505 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 1506 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 1507 | Verify the artifact signature before the tool gateway installs it | SF-CR-003 | permitted | decided fresh | — |  |
| 1508 | Record the percentile family used for the declared budget | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 1509 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted | decided fresh | — |  |
| 1510 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | denied | bound by precedent | REC-S0026 |  |
| 1511 | Default the citizenship attribute to US person when the onboarding form is left blank | SF-IT-003 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 1512 | Record the builder identity in the release attestation | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1513 | Label the throughput metric with the implant dose | SF-RP-002 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 1514 | Move key material into the hardware security module | SF-CR-002 | permitted | bound by precedent | REC-SF-A-00590 |  |
| 1515 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | decided fresh | — |  |
| 1516 | Bound the SECS message queue depth per tool connection | SF-SG-007 | permitted | decided fresh | — |  |
| 1517 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | bound by precedent | REC-SF-L-01033 |  |
| 1518 | Add an authorisation check to the lot-detail API | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1519 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted | bound by precedent | REC-S0006 |  |
| 1520 | Add the realised adverse-contest rate to the governance export | SF-GV-006 | permitted | decided fresh | — |  |
| 1521 | Exclude audit findings from the retrieval query | SF-GV-006 | permitted | decided fresh | — |  |
| 1522 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh | — |  |
| 1523 | Pin the denied-party list snapshot used by a screening decision | SF-EX-009 | permitted | bound by precedent | REC-S0003 |  |
| 1524 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | decided fresh | — |  |
| 1525 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-SF-N-00936 |  |
| 1526 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-003 | permitted | decided fresh | — |  |
| 1527 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-003 | permitted | decided fresh | — |  |
| 1528 | Shorten the WIP record retention term in the rulebook | SF-SS-007 | denied | decided fresh | — |  |
| 1529 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-004 | permitted | decided fresh | — |  |
| 1530 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | bound by precedent | REC-SF-L-00679 |  |
| 1531 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-007 | denied | decided fresh | — |  |
| 1532 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-010 | denied | bound by precedent | REC-S0019 |  |
| 1533 | Allow TLS 1.0 on the tool gateway for the Kumamoto equipment | SF-CR-001 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 1534 | Move recipe transfer onto the mutually authenticated channel | SF-RP-006 | permitted | bound by precedent | REC-SF-N-00316 |  |
| 1535 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 1536 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | bound by precedent | REC-SF-L-00869 |  |
| 1537 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-009 | permitted | decided fresh | — | ● |
| 1538 | Move key material into the hardware security module | SF-CR-006 | denied | bound by precedent | REC-S0058 |  |
| 1539 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 1540 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted with conditions | bound by precedent | REC-SF-S-01373 |  |
| 1541 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | permitted | decided fresh | — |  |
| 1542 | Record the builder identity in the release attestation | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 1543 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted | decided fresh | — |  |
| 1544 | Add the newly pulled component to the generated SBOM | SF-SS-011 | permitted | decided fresh | — |  |
| 1545 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | permitted | decided fresh | — |  |
| 1546 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — | ● |
| 1547 | Add a negative test for a tampered recipe signature | SF-CR-005 | denied | bound by precedent | REC-S0057 | ● |
| 1548 | Move the charging threshold into the constitutional parameters file | SF-GV-006 | permitted with conditions | decided fresh | — | ● |
| 1549 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted with conditions | bound by precedent | REC-SF-C-01401 |  |
| 1550 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-002 | permitted | decided fresh | — |  |
| 1551 | Verify component digests against the registry before deploy | SF-SS-008 | permitted | bound by precedent | REC-SF-C-01270 |  |
| 1552 | Declare the latency budget for the changed metrology path | SF-RT-003 | permitted | decided fresh | — |  |
| 1553 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | bound by precedent | REC-S0012 |  |
| 1554 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 1555 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 1556 | Record the percentile family used for the declared budget | SF-RT-001 | permitted with conditions | bound by precedent | REC-SF-C-01128 |  |
| 1557 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh | — |  |
| 1558 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-008 | permitted | decided fresh | — |  |
| 1559 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | bound by precedent | REC-SF-L-00836 |  |
| 1560 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-001 | permitted | decided fresh | — |  |
| 1561 | Retain ITAR access records for the full five-year floor | SF-IT-002 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1562 | Pin the JVM collector so pause times stay inside the budget | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 1563 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 | ● |
| 1564 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 1565 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | bound by precedent | REC-SF-B-00728 |  |
| 1566 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh | — |  |
| 1567 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted | decided fresh | — |  |
| 1568 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 1569 | Record the ECCN determination alongside the design-file upload | SF-EX-012 | denied | bound by precedent | REC-S0005 |  |
| 1570 | Document the CUI boundary for the metrology ingest service | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 1571 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00905 |  |
| 1572 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | disposed by citation | — |  |
| 1573 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1574 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01537 |  |
| 1575 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1576 | Record the builder identity in the release attestation | SF-SS-002 | permitted | bound by precedent | REC-SF-N-00613 |  |
| 1577 | Store the superseded metrology value beside its correction | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 1578 | Move key material into the hardware security module | SF-CR-004 | denied | bound by precedent | REC-S0056 |  |
| 1579 | Promote the run-to-run controller model to production without held-out lot validation | SF-QS-002 | denied | decided fresh | — |  |
| 1580 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | bound by precedent | REC-SF-A-00649 |  |
| 1581 | Pin the denied-party list snapshot used by a screening decision | SF-EX-008 | permitted | decided fresh | — |  |
| 1582 | Retry S2F41 remote commands without reordering the queue | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 |  |
| 1583 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-003 | permitted | decided fresh | — | ● |
| 1584 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1585 | Add a retention-hold check to the record destruction job | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 1586 | Publish the standing declaration in the compliance export | SF-GV-004 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1587 | Log the citizenship attribute alongside every ITAR access event | SF-IT-004 | permitted | decided fresh | — |  |
| 1588 | Reclassify a defence article from ITAR to EAR only after a commodity-jurisdiction determination clears it | SF-IT-004 | permitted | decided fresh | — |  |
| 1589 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | disposed by citation | — |  |
| 1590 | Enforce the protocol allowlist at every zone boundary | SF-OT-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 1591 | Record the builder identity in the release attestation | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 1592 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-006 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1593 | Add secret scanning to the pre-merge pipeline | SF-SS-007 | permitted | decided fresh | — | ● |
| 1594 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted | bound by precedent | REC-SF-C-01035 |  |
| 1595 | Lower the export-screening strictness in the policy repository | SF-AG-003 | denied | decided fresh | — |  |
| 1596 | Add the newly pulled component to the generated SBOM | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1597 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-007 | permitted | decided fresh | — |  |
| 1598 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01051 | ● |
| 1599 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 1600 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-003 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1601 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1602 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1603 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-007 | permitted | bound by precedent | REC-SF-A-00545 |  |
| 1604 | Hold agent edits to the screening logic for compliance review | SF-AG-003 | permitted | decided fresh | — |  |
| 1605 | Make the audit register append-only and disjoint from the store | SF-GV-004 | permitted with conditions | bound by precedent | REC-S0063 | ● |
| 1606 | Return a correlation id instead of a stack trace to the client | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 1607 | Keep recipe execution records until the retention clock expires | SF-WI-003 | permitted | bound by precedent | REC-SF-C-01063 |  |
| 1608 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 1609 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — |  |
| 1610 | Resolve the foreign access request through the named legal channel | SF-DS-004 | permitted | decided fresh | — |  |
| 1611 | Widen the data residency provision to permit group-A replicas | SF-RP-003 | denied | decided fresh | — |  |
| 1612 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-005 | denied | bound by precedent | REC-S0049 | ● |
| 1613 | Record the exception authority against the accepting principal | SF-GV-003 | permitted | decided fresh | — |  |
| 1614 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-010 | permitted | decided fresh after a tie | none_tie |  |
| 1615 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-004 | denied | decided fresh | — |  |
| 1616 | Record the builder identity in the release attestation | SF-SS-005 | permitted | bound by precedent | REC-SF-L-01493 |  |
| 1617 | Attach assessment evidence to the claimed access control | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 1618 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 1619 | Replace the pickle payload with a schema-validated JSON body | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 1620 | Report a suspect counterfeit part to the named quality owner before disposition | SF-RS-003 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1621 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-001 SF-GV-004 ⛔ | denied | refused at the floor | — |  |
| 1622 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 |  |
| 1623 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 1624 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted with conditions | bound by precedent | REC-SF-S-01585 |  |
| 1625 | Delete the held lot's genealogy during the archive cleanup | SF-WI-002 SF-CR-004 ⛔ | denied | refused at the floor | — |  |
| 1626 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | denied | bound by precedent | REC-S0018 |  |
| 1627 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh | — |  |
| 1628 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted | decided fresh | — |  |
| 1629 | Require a human sign-off before an agent edits equipment control code | SF-AG-006 | permitted | bound by precedent | REC-S0050 |  |
| 1630 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 1631 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | decided fresh | — |  |
| 1632 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 1633 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-004 SF-EX-008 ⛔ | denied | refused at the floor | — |  |
| 1634 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-007 | denied | bound by precedent | REC-S0026 | ● |
| 1635 | Correct for coordinated omission in the ingest benchmark | SF-RT-003 | permitted | decided fresh | — |  |
| 1636 | Keep the HSMS reply timeout inside the declared bound | SF-SG-005 | permitted | bound by precedent | REC-SF-C-01174 |  |
| 1637 | Keep recipe execution records until the retention clock expires | SF-WI-006 | permitted | decided fresh | — |  |
| 1638 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 1639 | Run each build job on a fresh ephemeral runner | SF-SS-011 | permitted | decided fresh | — |  |
| 1640 | Strip process parameters from telemetry metric labels | SF-RP-007 | permitted | bound by precedent | REC-SF-N-00697 | ● |
| 1641 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 1642 | Keep the appeal route on the automated screening decision | SF-GV-006 | permitted with conditions | bound by precedent | REC-SF-G-01548 | ● |
| 1643 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | disposed by citation | — |  |
| 1644 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted | bound by precedent | REC-S0029 |  |
| 1645 | Wire a host command that can override the lockout/tagout state from the MES | SF-EH-001 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 1646 | Drop the deprecated cipher suites from the supplier portal | SF-CR-004 | denied | bound by precedent | REC-S0056 | ● |
| 1647 | Authenticate the time source for every piece of fab equipment | SF-OT-003 | permitted | decided fresh | — |  |
| 1648 | Preserve S6F11 event ordering under broker backpressure | SF-SG-005 | permitted | bound by precedent | REC-SF-L-00160 | ● |
| 1649 | Enforce the customer's notice period at the release gate | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 1650 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | bound by precedent | REC-SF-A-01546 |  |
| 1651 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 1652 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 1653 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | decided fresh | — | ● |
| 1654 | Replace the direct-URL dependency with a registry release | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01080 | ● |
| 1655 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-001 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 1656 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 |  |
| 1657 | Sign the release attestation with the developer's own runner identity | SF-SS-001 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 1658 | Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact | SF-EH-004 | permitted | bound by precedent | REC-SF-A-01349 |  |
| 1659 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | decided fresh | — | ● |
| 1660 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01074 |  |
| 1661 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-012 | permitted | decided fresh | — |  |
| 1662 | Surface the applicable ECCN on the supplier portal download page | SF-EX-012 | permitted | decided fresh | — |  |
| 1663 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 1664 | Label the throughput metric with the implant dose | SF-RP-003 | denied | bound by precedent | REC-SF-B-00771 |  |
| 1665 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted | decided fresh | — |  |
| 1666 | Verify component digests against the registry before deploy | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1667 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-003 | permitted | decided fresh | — |  |
| 1668 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-007 | denied | bound by precedent | REC-SF-B-01075 |  |
| 1669 | Let the retention sweep run across lots that are under legal hold | SF-DS-005 | denied | decided fresh | — |  |
| 1670 | Publish the standing declaration in the compliance export | SF-GV-006 | permitted with conditions | bound by precedent | REC-SF-G-01548 |  |
| 1671 | Preserve S6F11 event ordering under broker backpressure | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 1672 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | bound by precedent | REC-SF-C-01270 |  |
| 1673 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | disposed by citation | — |  |
| 1674 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted | decided fresh | — |  |
| 1675 | Keep recipe execution records until the retention clock expires | SF-WI-004 | permitted | decided fresh | — |  |
| 1676 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted | decided fresh | — |  |
| 1677 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 1678 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted with conditions | bound by precedent | REC-SF-U-01555 |  |
| 1679 | Add an authorisation check to the lot-detail API | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 1680 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | bound by precedent | REC-S0045 |  |
| 1681 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted | decided fresh | — | ● |
| 1682 | Move portal document storage to a new vendor without naming its region | SF-DS-001 SF-OT-003 ⛔ | denied | refused at the floor | — |  |
| 1683 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 | ● |
| 1684 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | decided fresh | — |  |
| 1685 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-B-01456 | ● |
| 1686 | Add a configuration flag that releases blocked-property holds for expedited orders | SF-SO-003 | denied | decided fresh | — | ● |
| 1687 | Attach assessment evidence to the claimed access control | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 1688 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | bound by precedent | REC-SF-N-00697 |  |
| 1689 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | decided fresh | — | ● |
| 1690 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01051 |  |
| 1691 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 1692 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 |  |
| 1693 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | decided fresh | — |  |
| 1694 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted | decided fresh | — |  |
| 1695 | Resolve the foreign access request through the named legal channel | SF-DS-006 | permitted | decided fresh | — |  |
| 1696 | Split the cross-border replica by jurisdiction tag | SF-DS-006 | permitted | decided fresh | — |  |
| 1697 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-005 | denied | decided fresh | — |  |
| 1698 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 |  |
| 1699 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-004 | permitted | decided fresh | — |  |
| 1700 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | bound by precedent | REC-S0029 |  |
| 1701 | Reject signatures the verifier previously accepted by mistake | SF-CR-003 | permitted | decided fresh | — |  |
| 1702 | Quarantine a broker-sourced lot pending provenance verification | SF-RS-001 | denied | bound by precedent | REC-S0070 |  |
| 1703 | Shell out to the converter with the supplier's filename | SF-AS-001 | denied | decided fresh | — |  |
| 1704 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 | ● |
| 1705 | Record the agent identity and model version on the pull request | SF-AG-004 | permitted | decided fresh | — |  |
| 1706 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-004 | permitted | decided fresh | — |  |
| 1707 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted | bound by precedent | REC-SF-C-01502 |  |
| 1708 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 1709 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | permitted | decided fresh | — |  |
| 1710 | Generate the SBOM from the direct dependency list only | SF-SS-004 | denied | decided fresh | — |  |
| 1711 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | bound by precedent | REC-SF-C-01245 |  |
| 1712 | Rate-limit the supplier portal's document download endpoint | — | permitted | docketed — nothing engaged | — |  |
| 1713 | Reclassify a defence article from ITAR to EAR only after a commodity-jurisdiction determination clears it | SF-IT-002 | permitted | decided fresh | — |  |
| 1714 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 1715 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-001 SF-AG-008 ⛔ | denied | refused at the floor | — |  |
| 1716 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-002 | denied | bound by precedent | REC-S0060 |  |
| 1717 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted | decided fresh | — |  |
| 1718 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted | decided fresh | — |  |
| 1719 | Attribute every metrology record amendment to a named operator | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 1720 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted | bound by precedent | REC-SF-A-00688 |  |
| 1721 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 1722 | Verify every package the agent imported against the registry | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 1723 | Record the percentile family used for the declared budget | SF-RT-005 | denied | bound by precedent | REC-S0024 |  |
| 1724 | Derive a fresh nonce per recipe encryption operation | SF-CR-003 | permitted | decided fresh | — |  |
| 1725 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 1726 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 |  |
| 1727 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-001 | permitted | decided fresh | — |  |
| 1728 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-001 | permitted | decided fresh | — |  |
| 1729 | Make export decisions append-only in the trade compliance ledger | SF-EX-008 | denied | bound by precedent | REC-S0002 |  |
| 1730 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh after a tie | none_tie |  |
| 1731 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted with conditions | bound by precedent | REC-SF-C-01683 |  |
| 1732 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | decided fresh | — |  |
| 1733 | Disable a vendor's remote-access account between sessions | SF-OT-003 | permitted | bound by precedent | REC-S0080 |  |
| 1734 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | decided fresh | — | ● |
| 1735 | Block the merge on the critical CVE in the ingest dependency | SF-SS-002 | permitted | decided fresh | — |  |
| 1736 | Report load conditions alongside the p99.9 measurement | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 1737 | Record the ECCN determination alongside the design-file upload | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 1738 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-C-01032 |  |
| 1739 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-001 | permitted | decided fresh | — |  |
| 1740 | Classify a process change as major or minor with recorded rationale | SF-QS-001 | permitted | decided fresh | — |  |
| 1741 | Sign the release attestation with the developer's own runner identity | SF-SS-002 | denied | decided fresh | — |  |
| 1742 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-SF-N-00936 |  |
| 1743 | Reroute S6F11 event reports through the new async fanout | SF-SG-001 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 1744 | Hide the appeal button on the automated screening result page | SF-GV-005 | denied | decided fresh | — |  |
| 1745 | Verify every package the agent imported against the registry | SF-AG-005 | permitted | bound by precedent | REC-SF-A-00117 |  |
| 1746 | Make export decisions append-only in the trade compliance ledger | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 1747 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted with conditions | bound by precedent | REC-SF-S-01746 | ● |
| 1748 | Parameterise the supplier portal's lot-search query | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1749 | Disable a vendor's remote-access account between sessions | SF-OT-004 | denied | bound by precedent | REC-S0081 |  |
| 1750 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted | decided fresh | — |  |
| 1751 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-007 | permitted | bound by precedent | REC-SF-A-00545 | ● |
| 1752 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 1753 | Allowlist the export format instead of shelling out with user input | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 1754 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-C-01685 | ● |
| 1755 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 1756 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 1757 | Record the builder identity in the release attestation | SF-SS-009 | permitted | decided fresh | — | ● |
| 1758 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-B-00741 |  |
| 1759 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-003 | permitted | decided fresh | — |  |
| 1760 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 1761 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | permitted | decided fresh | — |  |
| 1762 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | bound by precedent | REC-SF-C-01376 |  |
| 1763 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1764 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1765 | Declare the latency budget for the changed metrology path | SF-RT-007 | permitted | decided fresh | — |  |
| 1766 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | bound by precedent | REC-SF-C-01751 | ● |
| 1767 | Attribute every metrology record amendment to a named operator | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 1768 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | denied | bound by precedent | REC-SF-C-01038 |  |
| 1769 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 1770 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | denied | bound by precedent | REC-S0018 | ● |
| 1771 | Canonicalise the upload path before the handler opens the file | SF-AS-005 | permitted | docketed — not charged | — |  |
| 1772 | Keep Dresden yield records inside the EU replica set | SF-DS-004 | permitted with conditions | bound by precedent | REC-S0008 |  |
| 1773 | Record the builder identity in the release attestation | SF-SS-010 | permitted | decided fresh | — | ● |
| 1774 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00967 | ● |
| 1775 | Bridge the tool network to the enterprise network for a firmware push | SF-OT-001 | denied | decided fresh | — |  |
| 1776 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | bound by precedent | REC-SF-C-01198 | ● |
| 1777 | Attribute every metrology record amendment to a named operator | SF-WI-007 | permitted | decided fresh | — |  |
| 1778 | Add an append-only constraint to the lot genealogy table | SF-WI-005 | permitted | bound by precedent | REC-SF-C-01245 |  |
| 1779 | Document the invariant the metrology ingest lock protects | SF-TQ-003 | permitted | decided fresh | — |  |
| 1780 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00991 |  |
| 1781 | Raise the latency budget stated in the constitutional parameters | SF-SS-007 | denied | decided fresh | — |  |
| 1782 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 | ● |
| 1783 | Capture customer acknowledgement on the change notice before release | SF-QS-003 | permitted | decided fresh | — |  |
| 1784 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-003 | permitted | decided fresh | — |  |
| 1785 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | decided fresh | — |  |
| 1786 | Log the deemed-export check that runs at repository role grant | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 |  |
| 1787 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 1788 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | bound by precedent | REC-SF-L-01681 | ● |
| 1789 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — |  |
| 1790 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-005 | denied | bound by precedent | REC-SF-B-01340 | ● |
| 1791 | Replace the pickle payload with a schema-validated JSON body | SF-AS-002 | permitted | disposed by citation | — |  |
| 1792 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | bound by precedent | REC-S0012 |  |
| 1793 | Attach assessment evidence to the claimed access control | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 1794 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00991 |  |
| 1795 | Restrict certificate key types to the permitted set | SF-CR-004 | permitted | decided fresh | — |  |
| 1796 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 1797 | Add the newly pulled component to the generated SBOM | SF-SS-003 | permitted | disposed by citation | — |  |
| 1798 | Declare the latency budget for the changed metrology path | SF-RT-003 | denied | bound by precedent | REC-S0022 |  |
| 1799 | Move the alarm-fanout write off the monitoring hot path | SF-RT-004 | permitted | decided fresh | — |  |
| 1800 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | bound by precedent | REC-SF-N-01734 |  |
| 1801 | Shorten the WIP record retention term in the rulebook | SF-AS-002 | denied | decided fresh | — |  |
| 1802 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1803 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1804 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | denied | bound by precedent | REC-S0013 |  |
| 1805 | Bind the mask revision to its lot and recipe record | SF-QS-001 | permitted | decided fresh | — |  |
| 1806 | Honour the regulatory hold ahead of the retention sweep | SF-DS-006 | permitted | bound by precedent | REC-SF-N-00687 |  |
| 1807 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted | decided fresh | — |  |
| 1808 | Declare the latency budget for the changed metrology path | SF-RT-007 | permitted | decided fresh | — |  |
| 1809 | Keep recipe text out of the yield model's prompt context | SF-RP-003 | permitted | decided fresh | — |  |
| 1810 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted with conditions | bound by precedent | REC-SF-C-01683 |  |
| 1811 | Carry the regulatory hold flag through the archive migration | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 1812 | Move key material into the hardware security module | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1813 | Bound the SECS message queue depth per tool connection | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 1814 | Post a compensating entry instead of editing the WIP status | SF-WI-006 | permitted with conditions | bound by precedent | REC-SF-G-01756 |  |
| 1815 | Report load conditions alongside the p99.9 measurement | SF-RT-003 | permitted | decided fresh | — |  |
| 1816 | Verify component digests against the registry before deploy | SF-SS-011 | permitted | bound by precedent | REC-SF-N-00111 |  |
| 1817 | Move the charging threshold into the constitutional parameters file | SF-GV-003 | permitted | decided fresh | — |  |
| 1818 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-C-01300 |  |
| 1819 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh | — |  |
| 1820 | Add an append-only constraint to the lot genealogy table | SF-WI-005 | permitted | decided fresh | — |  |
| 1821 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 |  |
| 1822 | Promote the run-to-run controller model to production without held-out lot validation | SF-QS-003 | denied | decided fresh | — |  |
| 1823 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1824 | Require named-owner approval per vendor remote session | SF-OT-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 1825 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 1826 | Move the charging threshold into the constitutional parameters file | SF-GV-005 | permitted | bound by precedent | REC-SF-A-00477 |  |
| 1827 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 1828 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 1829 | Publish the measurement window with the latency result | SF-RT-005 | denied | bound by precedent | REC-S0024 |  |
| 1830 | Record the exception authority against the accepting principal | SF-GV-004 | permitted | decided fresh | — |  |
| 1831 | Make the audit register append-only and disjoint from the store | SF-GV-004 | permitted | decided fresh | — |  |
| 1832 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 1833 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | bound by precedent | REC-SF-A-01546 |  |
| 1834 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 1835 | Move the charging threshold into the constitutional parameters file | SF-GV-003 | permitted | decided fresh | — |  |
| 1836 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | bound by precedent | REC-SF-C-01245 |  |
| 1837 | Parameterise the supplier portal's lot-search query | SF-AS-002 | permitted | decided fresh | — |  |
| 1838 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 |  |
| 1839 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | decided fresh | — | ● |
| 1840 | Verify component digests against the registry before deploy | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 1841 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | decided fresh | — |  |
| 1842 | Enforce the protocol allowlist at every zone boundary | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01704 |  |
| 1843 | Allowlist the export format instead of shelling out with user input | SF-AS-002 | permitted | decided fresh | — |  |
| 1844 | Parameterise the supplier portal's lot-search query | SF-AS-001 | permitted | bound by precedent | REC-SF-L-00219 |  |
| 1845 | Rate-limit the supplier portal's document download endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1846 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-C-01563 |  |
| 1847 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 1848 | Add a negative test for a tampered recipe signature | SF-CR-005 | denied | bound by precedent | REC-SF-C-01547 |  |
| 1849 | Redact recipe parameters from the tool-gateway debug log | SF-RP-007 | permitted | decided fresh | — | ● |
| 1850 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 | ● |
| 1851 | Default every uncatalogued defence article to the commerce control list | SF-IT-003 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 1852 | Run each build job on a fresh ephemeral runner | SF-SS-008 | permitted | bound by precedent | REC-SF-L-01033 |  |
| 1853 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted | decided fresh | — |  |
| 1854 | Surface unparsed equipment replies instead of dropping them | SF-SG-005 | permitted | decided fresh | — |  |
| 1855 | Retire the superseded cryptographic floor from the constitution | SF-EX-013 | denied | decided fresh | — |  |
| 1856 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-001 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 1857 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted | bound by precedent | REC-SF-C-01202 | ● |
| 1858 | Add the CHIPS notification duty to the compliance rulebook | SF-SG-010 | denied | decided fresh | — |  |
| 1859 | Validate the ECCN parameter against the enumerated set | — | permitted | docketed — nothing engaged | — |  |
| 1860 | Attribute every metrology record amendment to a named operator | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 1861 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted | decided fresh | — |  |
| 1862 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 1863 | Renumber the collection event identifiers to close the gaps | SF-SG-008 | denied | decided fresh | — |  |
| 1864 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted | decided fresh | — |  |
| 1865 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | bound by precedent | REC-SF-L-01493 |  |
| 1866 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted | decided fresh | — |  |
| 1867 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-005 | permitted | decided fresh | — |  |
| 1868 | Split the slow enrichment step out of the alarm path | SF-RT-002 | permitted | bound by precedent | REC-SF-C-01502 | ● |
| 1869 | Reroute S6F11 event reports through the new async fanout | SF-SG-004 | denied | decided fresh | — |  |
| 1870 | Attach an agent provenance attestation to the generated migration | SF-AG-004 | permitted | bound by precedent | REC-S0048 |  |
| 1871 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted with conditions | decided fresh | — | ● |
| 1872 | Swap the hand-rolled MAC for the library primitive | SF-CR-002 | permitted | decided fresh | — |  |
| 1873 | Derive a fresh nonce per recipe encryption operation | SF-CR-002 | permitted | decided fresh | — |  |
| 1874 | Add the new data flow to the system security plan diagram | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 1875 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | bound by precedent | REC-SF-C-01857 |  |
| 1876 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 1877 | Sign the container image published for the edge tool gateway | SF-SS-003 | permitted with conditions | bound by precedent | REC-SF-C-01296 |  |
| 1878 | Record the control inheritance for the shared platform tier | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 1879 | Attribute every metrology record amendment to a named operator | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 1880 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted with conditions | decided fresh | — | ● |
| 1881 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-001 SF-QS-004 ⛔ | denied | refused at the floor | — |  |
| 1882 | Replace the direct-URL dependency with a registry release | SF-SS-004 | permitted | disposed by citation | — |  |
| 1883 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted | disposed by citation | — |  |
| 1884 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 1885 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 1886 | Move recipe transfer onto the mutually authenticated channel | SF-RP-003 | permitted | bound by precedent | REC-SF-A-00339 | ● |
| 1887 | Log the full recipe body when a tool rejects a transfer | SF-RP-003 | denied | decided fresh | — |  |
| 1888 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-005 | permitted | bound by precedent | REC-SF-A-00477 |  |
| 1889 | Verify the audit chain after the metrology schema migration | SF-WI-007 | permitted | decided fresh | — |  |
| 1890 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted with conditions | bound by precedent | REC-SF-S-01746 |  |
| 1891 | Record the agent identity and model version on the pull request | SF-AG-006 | permitted | decided fresh | — |  |
| 1892 | Require a human sign-off before an agent edits equipment control code | SF-AG-006 | permitted | decided fresh | — |  |
| 1893 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 1894 | Move recipe transfer onto the mutually authenticated channel | SF-RP-003 | permitted | bound by precedent | REC-SF-C-01886 |  |
| 1895 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 1896 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | bound by precedent | REC-S0028 | ● |
| 1897 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 1898 | Encrypt the recipe payload at rest in the vault | SF-RP-005 | denied | bound by precedent | REC-S0034 |  |
| 1899 | Keep the appeal route on the automated screening decision | SF-GV-006 | permitted | decided fresh | — |  |
| 1900 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-007 | permitted | bound by precedent | REC-SF-L-01839 |  |
| 1901 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 1902 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-B-00961 |  |
| 1903 | Drop the standing declaration from the governance export payload | SF-GV-002 ⛔ | denied | refused at the floor | — |  |
| 1904 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted | bound by precedent | REC-S0027 | ● |
| 1905 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted | decided fresh | — | ● |
| 1906 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-001 | denied | bound by precedent | REC-S0070 | ● |
| 1907 | Rotate the recipe vault signing key on the published schedule | SF-CR-003 | permitted with conditions | decided fresh | — | ● |
| 1908 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 1909 | Bypass the change-notice gate for any change classified as minor | SF-QS-001 | denied | bound by precedent | REC-SF-B-00110 | ● |
| 1910 | Move the charging threshold into the constitutional parameters file | SF-GV-003 | permitted with conditions | decided fresh | — | ● |
| 1911 | Pin the denied-party list snapshot used by a screening decision | SF-EX-009 | permitted | bound by precedent | REC-S0003 |  |
| 1912 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-007 | permitted | decided fresh | — |  |
| 1913 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | decided fresh | — |  |
| 1914 | Add a scanner for process parameters in application logs | SF-RP-006 | permitted | bound by precedent | REC-SF-N-00316 |  |
| 1915 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted | decided fresh | — |  |
| 1916 | Pin the denied-party list snapshot used by a screening decision | SF-EX-013 | permitted | decided fresh | — |  |
| 1917 | Strengthen the memory ordering on the sequence-number publish | — | permitted | docketed — nothing engaged | — |  |
| 1918 | Bypass the change-notice gate for any change classified as minor | SF-QS-001 | denied | bound by precedent | REC-SF-C-01909 |  |
| 1919 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 1920 | Add the CHIPS notification duty to the compliance rulebook | SF-CR-003 | denied | decided fresh | — |  |
| 1921 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01598 | ● |
| 1922 | Add the newly pulled component to the generated SBOM | SF-SS-002 | permitted | decided fresh | — |  |
| 1923 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 |  |
| 1924 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted | decided fresh | — |  |
| 1925 | Honour the regulatory hold ahead of the retention sweep | SF-DS-006 | permitted | bound by precedent | REC-SF-N-00687 |  |
| 1926 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted | decided fresh | — |  |
| 1927 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 | ● |
| 1928 | Return a correlation id instead of a stack trace to the client | SF-AS-007 | permitted | docketed — not charged | — |  |
| 1929 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00905 |  |
| 1930 | Skip the nationality check when granting repository roles to contractors | SF-EX-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 1931 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | bound by precedent | REC-SF-B-01299 | ● |
| 1932 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 1933 | Keep recipe text out of the yield model's prompt context | SF-RP-005 | denied | bound by precedent | REC-S0034 |  |
| 1934 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1935 | Sign the container image published for the edge tool gateway | SF-SS-006 | permitted | bound by precedent | REC-SF-A-00688 |  |
| 1936 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-007 | permitted | decided fresh | — |  |
| 1937 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-007 | permitted | decided fresh | — |  |
| 1938 | Scope recipe vault reads to the owning process integration team | SF-RP-003 | permitted | bound by precedent | REC-SF-A-00339 |  |
| 1939 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | decided fresh | — |  |
| 1940 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | decided fresh | — |  |
| 1941 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-004 | permitted | decided fresh | — |  |
| 1942 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 1943 | Keep recipe execution records until the retention clock expires | SF-WI-004 | permitted | bound by precedent | REC-SF-C-01896 | ● |
| 1944 | Sign the container image published for the edge tool gateway | SF-SS-010 | permitted | decided fresh | — |  |
| 1945 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1946 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted | decided fresh | — |  |
| 1947 | Keep audit logging on during the throughput optimisation | SF-WI-006 | denied | bound by precedent | REC-S0030 |  |
| 1948 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-010 | denied | decided fresh | — |  |
| 1949 | Quarantine agent changes that touch the export enforcement path | SF-AG-006 | permitted | bound by precedent | REC-S0050 |  |
| 1950 | Reuse the warm build runner to cut pipeline time in half | SF-SS-010 | denied | decided fresh | — |  |
| 1951 | Record the builder identity in the release attestation | SF-SS-007 | permitted | bound by precedent | REC-SF-L-01593 |  |
| 1952 | Add fuzz coverage for the metrology file upload handler | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1953 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted | decided fresh | — |  |
| 1954 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | bound by precedent | REC-SF-B-01368 | ● |
| 1955 | Resolve the foreign access request through the named legal channel | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 1956 | Make the audit register append-only and disjoint from the store | SF-GV-005 | permitted | bound by precedent | REC-S0064 |  |
| 1957 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted | disposed by citation | — |  |
| 1958 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | bound by precedent | REC-SF-C-01376 |  |
| 1959 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-001 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 1960 | Raise the tool-gateway TLS floor to the declared version | SF-CR-005 | permitted | decided fresh | — |  |
| 1961 | Pin the certificate chain used by the metrology ingest client | SF-CR-005 | permitted | decided fresh | — |  |
| 1962 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted | decided fresh | — |  |
| 1963 | Replace the pickle payload with a schema-validated JSON body | SF-AS-003 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 1964 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-006 | denied | decided fresh | — |  |
| 1965 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | permitted | bound by precedent | REC-SF-L-00219 |  |
| 1966 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1967 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | denied | bound by precedent | REC-S0025 |  |
| 1968 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 1969 | Batch alarm reports into the five-second telemetry flush | SF-SG-005 | denied | decided fresh | — | ● |
| 1970 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 |  |
| 1971 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-001 SF-EX-008 ⛔ | denied | refused at the floor | — |  |
| 1972 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-001 SF-AS-001 ⛔ | denied | refused at the floor | — |  |
| 1973 | Publish the EDA toolchain image without running the classification step | SF-EX-002 SF-SS-002 ⛔ | denied | refused at the floor | — |  |
| 1974 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-B-00961 |  |
| 1975 | Publish the measurement window with the latency result | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 1976 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01381 |  |
| 1977 | Allowlist the export format instead of shelling out with user input | SF-AS-004 | permitted | docketed — not charged | — |  |
| 1978 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | permitted | bound by precedent | REC-SF-C-01766 |  |
| 1979 | Canonicalise the upload path before the handler opens the file | SF-AS-006 | permitted | docketed — not charged | — |  |
| 1980 | Reject signatures the verifier previously accepted by mistake | SF-CR-005 | denied | bound by precedent | REC-S0057 | ● |
| 1981 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-004 | permitted | decided fresh | — |  |
| 1982 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted | decided fresh | — |  |
| 1983 | Sign the container image published for the edge tool gateway | SF-SS-002 | permitted | decided fresh | — |  |
| 1984 | Rate-limit the supplier portal's document download endpoint | SF-AS-003 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 1985 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 1986 | Retry S2F41 remote commands without reordering the queue | SF-SG-009 | denied | bound by precedent | REC-S0018 |  |
| 1987 | Weight supplier terms against firms the model scores as distressed | SF-GV-003 | denied | decided fresh | — |  |
| 1988 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted with conditions | bound by precedent | REC-SF-C-01747 |  |
| 1989 | Let the defence-article transfer proceed without naming a licence or exemption paragraph | SF-IT-001 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 1990 | Keep the appeal route on the automated screening decision | SF-GV-005 | permitted | bound by precedent | REC-SF-C-01079 |  |
| 1991 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 1992 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-C-01489 |  |
| 1993 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted | decided fresh | — |  |
| 1994 | Require a human sign-off before an agent edits equipment control code | SF-AG-008 | denied | bound by precedent | REC-S0052 |  |
| 1995 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 1996 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-B-00440 |  |
| 1997 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 1998 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | denied | bound by precedent | REC-S0018 | ● |
| 1999 | Keep audit logging on during the throughput optimisation | SF-WI-005 | permitted | decided fresh | — |  |
| 2000 | Exclude audit findings from the retrieval query | SF-GV-003 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 2001 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2002 | Record the builder identity in the release attestation | SF-SS-003 | permitted | decided fresh | — |  |
| 2003 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 2004 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | permitted | decided fresh | — |  |
| 2005 | Pin the JVM collector so pause times stay inside the budget | SF-RT-006 | permitted | decided fresh | — |  |
| 2006 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-006 | permitted | decided fresh | — |  |
| 2007 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-005 | denied | decided fresh | — |  |
| 2008 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-007 | denied | bound by precedent | REC-S0001 |  |
| 2009 | Encrypt the recipe payload at rest in the vault | SF-RP-006 | permitted | decided fresh | — |  |
| 2010 | Log the deemed-export check that runs at repository role grant | SF-EX-009 | permitted | bound by precedent | REC-S0003 |  |
| 2011 | Separate the reporter bulletin from the adjudication input path | SF-GV-005 | permitted | decided fresh | — |  |
| 2012 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted | bound by precedent | REC-SF-A-00508 |  |
| 2013 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-002 | permitted | decided fresh | — |  |
| 2014 | Redact recipe parameters from the tool-gateway debug log | SF-RP-003 | denied | bound by precedent | REC-S0032 |  |
| 2015 | Require a human sign-off before an agent edits equipment control code | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 2016 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 |  |
| 2017 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 2018 | Attribute every metrology record amendment to a named operator | SF-WI-007 | denied | bound by precedent | REC-S0031 | ● |
| 2019 | Ship the in-country support tunnel with the access question still open | SF-DS-002 SF-CR-006 ⛔ | denied | refused at the floor | — |  |
| 2020 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | bound by precedent | REC-SF-B-01368 |  |
| 2021 | Rotate the recipe vault envelope key on the published schedule | SF-RP-005 | permitted | decided fresh | — |  |
| 2022 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-010 | permitted with conditions | bound by precedent | REC-S0004 | ● |
| 2023 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 2024 | Bound the SECS message queue depth per tool connection | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 | ● |
| 2025 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 ⛔ | denied | refused at the floor | — |  |
| 2026 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 2027 | Make the audit register append-only and disjoint from the store | SF-GV-005 | permitted | decided fresh | — |  |
| 2028 | Publish the standing declaration in the compliance export | SF-GV-005 | permitted | decided fresh | — |  |
| 2029 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 2030 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted | bound by precedent | REC-SF-C-01198 |  |
| 2031 | Auto-merge agent pull requests that pass the build | SF-AG-003 | denied | decided fresh | — |  |
| 2032 | Add a retention-hold check to the record destruction job | SF-WI-006 | permitted | bound by precedent | REC-SF-A-00058 |  |
| 2033 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 2034 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted | decided fresh after a tie | none_tie |  |
| 2035 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | bound by precedent | REC-SF-L-01905 |  |
| 2036 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-006 | permitted | decided fresh | — |  |
| 2037 | Bound the collector's allocation rate on the ingest path | SF-RT-006 | denied | bound by precedent | REC-S0025 |  |
| 2038 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 2039 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 |  |
| 2040 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | decided fresh | — | ● |
| 2041 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 |  |
| 2042 | Serialise the two writers to the yield aggregation table | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 2043 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-C-00948 |  |
| 2044 | Link the agent's change to the originating engineering ticket | SF-AG-003 | permitted | bound by precedent | REC-S0106 |  |
| 2045 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 2046 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | denied | bound by precedent | REC-S0025 | ● |
| 2047 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted | decided fresh | — |  |
| 2048 | Attribute corrective-action closure to a named owner | SF-QS-002 | permitted | bound by precedent | REC-S0075 |  |
| 2049 | Publish the measurement window with the latency result | SF-RT-001 | permitted | decided fresh | — |  |
| 2050 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted | decided fresh | — |  |
| 2051 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-001 ⛔ | denied | refused at the floor | — |  |
| 2052 | Screen every counterparty against the SDN and consolidated lists including fifty-percent-owned entities | SF-SO-003 | permitted | bound by precedent | REC-S0069 |  |
| 2053 | Scope the internal SECS parser package to the private registry | SF-SS-003 | permitted | decided fresh | — |  |
| 2054 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | decided fresh | — |  |
| 2055 | Link the agent's change to the originating engineering ticket | SF-AG-003 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2056 | Serialise the two writers to the yield aggregation table | SF-TQ-003 | permitted | decided fresh | — |  |
| 2057 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | bound by precedent | REC-SF-N-01734 |  |
| 2058 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 2059 | Move the charging threshold for the supply chain family | SF-WI-004 | denied | decided fresh | — |  |
| 2060 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 | ● |
| 2061 | Record who amended the CD-SEM measurement and why | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 2062 | Route every screening near-miss to a named compliance reviewer | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 | ● |
| 2063 | Stop shipping equipment logs across the boundary by default | SF-DS-003 | permitted | decided fresh | — |  |
| 2064 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted | bound by precedent | REC-SF-C-01766 |  |
| 2065 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 2066 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | denied | bound by precedent | REC-S0007 |  |
| 2067 | Re-screen consignees on the published list-refresh cadence | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 2068 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | bound by precedent | REC-SF-C-01198 |  |
| 2069 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted | decided fresh | — |  |
| 2070 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 2071 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 | ● |
| 2072 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted | decided fresh | — |  |
| 2073 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-004 | permitted | decided fresh | — |  |
| 2074 | Narrow the recipe-protection provision to production recipes only | SF-SS-006 | denied | decided fresh | — |  |
| 2075 | Retain ITAR access records for the full five-year floor | SF-IT-004 | permitted | decided fresh | — |  |
| 2076 | Default every uncatalogued defence article to the commerce control list | SF-IT-003 SF-CR-006 ⛔ | denied | refused at the floor | — |  |
| 2077 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 2078 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted | decided fresh | — |  |
| 2079 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 2080 | Fall back to plain TCP when the tool refuses the TLS handshake | SF-RP-002 SF-QS-002 ⛔ | denied | refused at the floor | — |  |
| 2081 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01921 |  |
| 2082 | Bound the request body size on the yield analytics endpoint | — | permitted | docketed — nothing engaged | — |  |
| 2083 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-003 | permitted with conditions | bound by precedent | REC-SF-C-01003 |  |
| 2084 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted | decided fresh | — |  |
| 2085 | Keep Dresden yield records inside the EU replica set | SF-DS-004 | permitted | decided fresh | — |  |
| 2086 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 2087 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-001 | permitted | decided fresh | — |  |
| 2088 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | bound by precedent | REC-SF-L-00620 |  |
| 2089 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-001 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 2090 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | bound by precedent | REC-SF-G-02017 |  |
| 2091 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-001 ⛔ | denied | refused at the floor | — |  |
| 2092 | Validate the ECCN parameter against the enumerated set | SF-AS-003 | permitted | bound by precedent | REC-SF-L-00533 |  |
| 2093 | Fail the pipeline closed when the screening service times out | SF-EX-008 | permitted | decided fresh | — |  |
| 2094 | Route every screening near-miss to a named compliance reviewer | SF-EX-008 | permitted | decided fresh | — |  |
| 2095 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | disposed by citation | — |  |
| 2096 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted with conditions | bound by precedent | REC-SF-G-02045 | ● |
| 2097 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | decided fresh | — |  |
| 2098 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 2099 | Re-screen consignees on the published list-refresh cadence | SF-EX-008 | denied | bound by precedent | REC-S0002 |  |
| 2100 | Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path | SF-OT-002 | permitted with conditions | decided fresh | — | ● |
| 2101 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | bound by precedent | REC-SF-L-00869 | ● |
| 2102 | Strip process parameters from telemetry metric labels | SF-RP-005 | permitted | decided fresh | — |  |
| 2103 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 2104 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 2105 | Honour the regulatory hold ahead of the retention sweep | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 2106 | Publish the measurement window with the latency result | SF-RT-006 | denied | bound by precedent | REC-S0025 | ● |
| 2107 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 2108 | Add an authorisation check to the lot-detail API | — | permitted | docketed — nothing engaged | — |  |
| 2109 | Drop the deprecated field from the agent's regenerated response body | SF-AG-003 | denied | bound by precedent | REC-SF-C-01032 |  |
| 2110 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | disposed by citation | — |  |
| 2111 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 |  |
| 2112 | Add the newly pulled component to the generated SBOM | SF-SS-005 | permitted | decided fresh | — |  |
| 2113 | Require named-owner approval per vendor remote session | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 |  |
| 2114 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 2115 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 2116 | Order the two mutex acquisitions consistently across both paths | SF-TQ-001 | permitted | decided fresh | — | ● |
| 2117 | Record the exception authority against the accepting principal | SF-GV-005 | permitted | bound by precedent | REC-SF-C-01079 | ● |
| 2118 | Let the agent's enrichment step call an outside classification API | SF-AG-007 | denied | decided fresh | — |  |
| 2119 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-002 | permitted with conditions | decided fresh | — | ● |
| 2120 | Hash the recipe identifier before it reaches the analytics store | SF-RP-006 | permitted with conditions | bound by precedent | REC-S0035 | ● |
| 2121 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 2122 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-001 | permitted | bound by precedent | REC-SF-C-02060 |  |
| 2123 | Make export decisions append-only in the trade compliance ledger | SF-EX-007 | permitted | decided fresh | — |  |
| 2124 | Attach an agent provenance attestation to the generated migration | SF-AG-006 | permitted | bound by precedent | REC-S0050 |  |
| 2125 | Retire the legacy gas-alarm rate limiter that pre-dated the life-safety panel wiring | SF-EH-003 ⛔ | permitted | decided fresh | — |  |
| 2126 | Trace every discharge-report value back to its raw measurement | SF-EH-003 ⛔ | permitted | decided fresh | — |  |
| 2127 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted | bound by precedent | REC-SF-A-02116 | ● |
| 2128 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 2129 | Leave the vendor's remote-access account enabled after the session ends | SF-OT-003 | denied | bound by precedent | REC-SF-B-01390 |  |
| 2130 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — |  |
| 2131 | Mask implant dose values in the yield analytics export | SF-RP-007 | permitted | bound by precedent | REC-S0036 |  |
| 2132 | Attach an agent provenance attestation to the generated migration | SF-AG-008 | permitted | decided fresh | — |  |
| 2133 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01425 |  |
| 2134 | Preserve S6F11 event ordering under broker backpressure | SF-SG-004 | permitted | decided fresh | — | ● |
| 2135 | Pull the ingest parser from a mirror whose digest no longer matches | SF-SS-005 | denied | decided fresh | — |  |
| 2136 | Move portal document storage to a new vendor without naming its region | SF-DS-003 | denied | bound by precedent | REC-SF-B-01118 |  |
| 2137 | Write the full rationale trail at the moment of resolution | SF-GV-007 | permitted | decided fresh | — |  |
| 2138 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-007 | permitted | decided fresh | — |  |
| 2139 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 2140 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | bound by precedent | REC-SF-C-01502 |  |
| 2141 | Parameterise the supplier portal's lot-search query | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2142 | Report load conditions alongside the p99.9 measurement | SF-RT-005 | denied | bound by precedent | REC-S0024 |  |
| 2143 | Bound the request body size on the yield analytics endpoint | SF-AS-003 | permitted | decided fresh | — |  |
| 2144 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 2145 | Bound the collector's allocation rate on the ingest path | SF-RT-005 | denied | bound by precedent | REC-S0024 |  |
| 2146 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 2147 | Keep recipe execution records until the retention clock expires | SF-WI-003 | permitted | bound by precedent | REC-SF-C-01063 |  |
| 2148 | Reclassify the recipe-protection provision as advisory | SF-RT-002 | denied | decided fresh | — |  |
| 2149 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | bound by precedent | REC-SF-N-00613 | ● |
| 2150 | Downgrade a fuzzy sanctions-list near-miss to a documented false positive after two-person review | SF-SO-003 | permitted | decided fresh | — |  |
| 2151 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2152 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 2153 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 2154 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 2155 | Add the newly pulled component to the generated SBOM | SF-SS-002 | permitted | bound by precedent | REC-SF-C-02149 |  |
| 2156 | Remove the human-review requirement from the screening provision | SF-AS-001 | denied | decided fresh | — |  |
| 2157 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | bound by precedent | REC-SF-C-02149 |  |
| 2158 | Retry S2F41 remote commands without reordering the queue | SF-SG-006 | permitted | decided fresh | — |  |
| 2159 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 2160 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 2161 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | bound by precedent | REC-SF-A-01259 |  |
| 2162 | Stop shipping equipment logs across the boundary by default | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 2163 | Record the builder identity in the release attestation | SF-SS-007 | permitted | bound by precedent | REC-SF-L-01681 |  |
| 2164 | Redact recipe parameters from the tool-gateway debug log | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 2165 | Log the deemed-export check that runs at repository role grant | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01425 | ● |
| 2166 | Log the deemed-export check that runs at repository role grant | SF-EX-005 ⛔ | permitted | decided fresh | — |  |
| 2167 | Pin the denied-party list snapshot used by a screening decision | SF-EX-005 ⛔ | permitted | decided fresh | — |  |
| 2168 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | bound by precedent | REC-SF-C-01788 |  |
| 2169 | Record the agent identity and model version on the pull request | SF-AG-005 | permitted | decided fresh | — |  |
| 2170 | Verify component digests against the registry before deploy | SF-SS-006 | permitted | bound by precedent | REC-SF-A-00688 |  |
| 2171 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 2172 | Trace every discharge-report value back to its raw measurement | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 2173 | Add a GEM control-state transition test for the Lam etcher | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01921 |  |
| 2174 | Report the new latency number without saying what load produced it | SF-RT-002 | denied | decided fresh | — |  |
| 2175 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | bound by precedent | REC-SF-B-00080 |  |
| 2176 | Raise the tool-gateway TLS floor to the declared version | SF-CR-002 | permitted | decided fresh | — | ● |
| 2177 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | bound by precedent | REC-SF-N-01041 |  |
| 2178 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 2179 | Deliver alarm reports ahead of the collection-event budget | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 2180 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted | bound by precedent | REC-SF-C-02024 |  |
| 2181 | Quarantine a broker-sourced lot pending provenance verification | SF-RS-001 | permitted | decided fresh | — |  |
| 2182 | Retain the conflict-minerals inquiry response on the component record | SF-RS-001 | permitted | decided fresh | — |  |
| 2183 | Bound the request body size on the yield analytics endpoint | — | permitted | docketed — nothing engaged | — |  |
| 2184 | Publish the measurement window with the latency result | SF-RT-001 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 2185 | Document the CUI boundary for the metrology ingest service | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2186 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | bound by precedent | REC-SF-C-01904 |  |
| 2187 | Wire a rollback path into every controller-model promotion | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 2188 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-C-01685 |  |
| 2189 | Reject signatures the verifier previously accepted by mistake | SF-CR-001 ⛔ | permitted | decided fresh | — |  |
| 2190 | Reject signatures the verifier previously accepted by mistake | SF-CR-001 ⛔ | permitted | decided fresh | — |  |
| 2191 | Move key material into the hardware security module | SF-CR-005 | denied | bound by precedent | REC-S0057 | ● |
| 2192 | Re-enable the legacy cipher suite so the older scanner can connect | SF-CR-001 SF-IT-004 ⛔ | denied | refused at the floor | — |  |
| 2193 | Bound the SECS message queue depth per tool connection | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01921 |  |
| 2194 | Move portal document storage to a new vendor without naming its region | SF-DS-001 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 2195 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-C-01850 | ● |
| 2196 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-004 | permitted | decided fresh | — |  |
| 2197 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | bound by precedent | REC-SF-L-00620 |  |
| 2198 | Replace the pickle payload with a schema-validated JSON body | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2199 | Link the agent's change to the originating engineering ticket | SF-AG-006 | permitted | decided fresh | — |  |
| 2200 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | bound by precedent | REC-SF-L-00219 |  |
| 2201 | Add the newly pulled component to the generated SBOM | SF-SS-006 | permitted | decided fresh | — |  |
| 2202 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | bound by precedent | REC-SF-L-00679 |  |
| 2203 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | disposed by citation | — |  |
| 2204 | Assert the safety interlock signal survives the gateway refactor | SF-SG-010 | permitted | decided fresh | — |  |
| 2205 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | decided fresh | — |  |
| 2206 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 2207 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 2208 | Add a residency assertion to the metrology ingest contract | SF-DS-005 | permitted with conditions | bound by precedent | REC-SF-S-02105 |  |
| 2209 | Accept receipt of a lot whose supplier attestation expired last quarter | SF-RS-003 | denied | decided fresh | — |  |
| 2210 | Split the slow enrichment step out of the alarm path | SF-RT-003 | denied | bound by precedent | REC-S0022 |  |
| 2211 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-006 ⛔ | denied | refused at the floor | — |  |
| 2212 | Restrict certificate key types to the permitted set | SF-CR-003 | permitted | decided fresh | — |  |
| 2213 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-001 | permitted | decided fresh | — |  |
| 2214 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-C-01180 |  |
| 2215 | Refresh the sanctions list snapshot on the published daily cadence | SF-SO-001 ⛔ | permitted | decided fresh | — |  |
| 2216 | Record the outbound-investment determination before a joint-venture data share opens | SF-SO-001 ⛔ | permitted | decided fresh | — |  |
| 2217 | Rotate the recipe vault signing key on the published schedule | SF-CR-004 | denied | bound by precedent | REC-SF-C-01646 |  |
| 2218 | Serialise the two writers to the yield aggregation table | SF-TQ-004 | permitted | decided fresh | — |  |
| 2219 | Pin the JVM collector so pause times stay inside the budget | SF-RT-002 | permitted | bound by precedent | REC-SF-C-01502 |  |
| 2220 | Record the builder identity in the release attestation | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 2221 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2222 | Order the two mutex acquisitions consistently across both paths | SF-TQ-002 | permitted | decided fresh | — |  |
| 2223 | Add a negative test for a tampered recipe signature | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 2224 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | permitted | decided fresh | — |  |
| 2225 | Make export decisions append-only in the trade compliance ledger | SF-EX-013 | permitted | bound by precedent | REC-SF-C-01059 |  |
| 2226 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-005 | permitted | decided fresh | — |  |
| 2227 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 2228 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | decided fresh | — |  |
| 2229 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | bound by precedent | REC-S0029 |  |
| 2230 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | decided fresh | — |  |
| 2231 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted | bound by precedent | REC-SF-A-02116 | ● |
| 2232 | Gate the important-data export on the completed security assessment | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 2233 | Publish the measurement window with the latency result | SF-RT-001 | permitted with conditions | bound by precedent | REC-S0020 | ● |
| 2234 | Verify component digests against the registry before deploy | SF-SS-011 | permitted | decided fresh | — |  |
| 2235 | Join the uploaded filename onto the metrology import directory | SF-AS-002 | denied | decided fresh | — |  |
| 2236 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01921 |  |
| 2237 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 2238 | Merge the enclave's stale service accounts into the quarterly access review | SF-IT-002 | permitted with conditions | bound by precedent | REC-S0067 | ● |
| 2239 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-005 | permitted | decided fresh | — |  |
| 2240 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-002 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 2241 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-004 | denied | decided fresh | — |  |
| 2242 | Link the agent's change to the originating engineering ticket | SF-AG-003 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2243 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 2244 | Lower a gas-detector alarm threshold after a failed calibration, with EHS signoff recorded same day | SF-EH-004 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2245 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 2246 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-001 | permitted | bound by precedent | REC-SF-A-02116 |  |
| 2247 | Document the invariant the metrology ingest lock protects | SF-TQ-004 | permitted | decided fresh | — |  |
| 2248 | Drop the deprecated cipher suites from the supplier portal | SF-CR-003 | permitted | decided fresh | — |  |
| 2249 | Swap the hand-rolled MAC for the library primitive | SF-CR-003 | permitted | decided fresh | — |  |
| 2250 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | decided fresh | — |  |
| 2251 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-B-00902 |  |
| 2252 | Scope recipe vault reads to the owning process integration team | SF-RP-003 | permitted | decided fresh | — | ● |
| 2253 | Classify a process change as major or minor with recorded rationale | SF-QS-003 | permitted | bound by precedent | REC-SF-A-00470 |  |
| 2254 | Replace the direct-URL dependency with a registry release | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 2255 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted | bound by precedent | REC-S0027 |  |
| 2256 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 2257 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | bound by precedent | REC-SF-L-00115 |  |
| 2258 | Remove the barrier from the telemetry fanout to speed up ingest | SF-TQ-001 | denied | decided fresh | — |  |
| 2259 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-004 | permitted | bound by precedent | REC-S0072 |  |
| 2260 | Route every screening near-miss to a named compliance reviewer | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 2261 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01381 |  |
| 2262 | Drop the recipient identity field from the export record to speed up the batch job | SF-IT-001 ⛔ | denied | refused at the floor | — |  |
| 2263 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00991 | ● |
| 2264 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-005 | permitted | decided fresh | — |  |
| 2265 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted | bound by precedent | REC-SF-C-02165 |  |
| 2266 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 2267 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | decided fresh | — |  |
| 2268 | Disable the clock-drift alarm on the equipment time-sync path | SF-OT-004 | denied | bound by precedent | REC-SF-B-01449 | ● |
| 2269 | Reclassify a defence article from ITAR to EAR only after a commodity-jurisdiction determination clears it | SF-IT-002 | permitted | decided fresh | — |  |
| 2270 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted | bound by precedent | REC-SF-N-01041 |  |
| 2271 | Assert the safety interlock signal survives the gateway refactor | SF-SG-007 | permitted | decided fresh | — |  |
| 2272 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | decided fresh | — |  |
| 2273 | Add a licence-exception clause to the trade compliance rulebook | SF-DS-006 | denied | decided fresh | — |  |
| 2274 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-005 | permitted | bound by precedent | REC-SF-A-00117 | ● |
| 2275 | Attribute every metrology record amendment to a named operator | SF-WI-005 | permitted | decided fresh | — |  |
| 2276 | Record the percentile family used for the declared budget | SF-RT-001 | permitted with conditions | bound by precedent | REC-SF-C-02233 |  |
| 2277 | Gate the important-data export on the completed security assessment | SF-DS-005 | permitted | decided fresh | — |  |
| 2278 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted | bound by precedent | REC-SF-A-00545 | ● |
| 2279 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — |  |
| 2280 | Scope the internal SECS parser package to the private registry | SF-SS-007 | permitted | bound by precedent | REC-SF-C-01788 |  |
| 2281 | Record the empowered official's signature on every ITAR authorisation | SF-IT-001 ⛔ | permitted | decided fresh | — |  |
| 2282 | Log the citizenship attribute alongside every ITAR access event | SF-IT-001 ⛔ | permitted | decided fresh | — |  |
| 2283 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-002 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 2284 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00314 |  |
| 2285 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 2286 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | denied | bound by precedent | REC-S0046 |  |
| 2287 | Update the supply chain risk plan after the vendor change | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 2288 | Enforce the customer's notice period at the release gate | SF-QS-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2289 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 2290 | Fail the pipeline closed when the screening service times out | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01369 |  |
| 2291 | Swallow equipment replies the parser does not recognise | SF-SG-003 | denied | decided fresh | — |  |
| 2292 | Attach an agent provenance attestation to the generated migration | SF-AG-008 | permitted | bound by precedent | REC-SF-C-00967 |  |
| 2293 | Publish the measurement window with the latency result | SF-RT-001 | permitted | decided fresh | — |  |
| 2294 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted with conditions | bound by precedent | REC-SF-C-01683 |  |
| 2295 | Re-screen consignees on the published list-refresh cadence | SF-EX-008 | permitted | decided fresh | — |  |
| 2296 | Re-screen consignees on the published list-refresh cadence | SF-EX-008 | permitted | decided fresh | — |  |
| 2297 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 2298 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | bound by precedent | REC-SF-C-02278 |  |
| 2299 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 2300 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | bound by precedent | REC-SF-A-00545 |  |
| 2301 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 2302 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-007 | denied | bound by precedent | REC-S0051 |  |
| 2303 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 2304 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-002 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 2305 | Add the CHIPS notification duty to the compliance rulebook | SF-OT-003 | denied | decided fresh | — |  |
| 2306 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 2307 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted with conditions | bound by precedent | REC-SF-C-02022 |  |
| 2308 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted | decided fresh | — | ● |
| 2309 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted | bound by precedent | REC-SF-C-00981 |  |
| 2310 | Add the pilot line to the CUI boundary documentation | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 2311 | Disable the clock-drift alarm on the equipment time-sync path | SF-OT-003 | denied | decided fresh | — | ● |
| 2312 | Version collection-event identifiers instead of renumbering them | SF-SG-003 | permitted | bound by precedent | REC-S0012 |  |
| 2313 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-001 ⛔ | permitted | decided fresh | — |  |
| 2314 | Assert the safety interlock signal survives the gateway refactor | SF-SG-001 ⛔ | permitted | decided fresh | — |  |
| 2315 | Document the sub-processor chain for the supplier portal CDN | SF-DS-003 | denied | bound by precedent | REC-S0007 | ● |
| 2316 | Hold agent edits to the screening logic for compliance review | SF-AG-004 | permitted | decided fresh | — |  |
| 2317 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh | — |  |
| 2318 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2319 | Publish the standing declaration in the compliance export | SF-GV-003 | permitted with conditions | bound by precedent | REC-SF-C-01003 |  |
| 2320 | Document the CUI boundary for the metrology ingest service | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 2321 | Assert the safety interlock signal survives the gateway refactor | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 |  |
| 2322 | Verify component digests against the registry before deploy | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 2323 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | decided fresh | — | ● |
| 2324 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 2325 | Verify component digests against the registry before deploy | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 | ● |
| 2326 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-003 | denied | decided fresh | — |  |
| 2327 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-C-01850 |  |
| 2328 | Add a GEM control-state transition test for the Lam etcher | SF-SG-003 | permitted | disposed by citation | — |  |
| 2329 | Document the invariant the metrology ingest lock protects | SF-TQ-001 | permitted | bound by precedent | REC-SF-C-02231 |  |
| 2330 | Document the invariant the metrology ingest lock protects | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2331 | Monitor and alarm on clock drift across the tool network | SF-OT-003 | permitted | bound by precedent | REC-S0080 |  |
| 2332 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2333 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-001 | permitted | bound by precedent | REC-SF-A-02116 |  |
| 2334 | Attribute corrective-action closure to a named owner | SF-QS-002 | permitted | decided fresh | — |  |
| 2335 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 2336 | Show the human review route on the screening decision page | SF-GV-007 | permitted | decided fresh | — |  |
| 2337 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | decided fresh | — |  |
| 2338 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | decided fresh | — |  |
| 2339 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | disposed by citation | — |  |
| 2340 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-B-00208 |  |
| 2341 | Parameterise the supplier portal's lot-search query | SF-AS-004 | permitted | docketed — not charged | — |  |
| 2342 | Surface unparsed equipment replies instead of dropping them | SF-SG-007 | permitted | bound by precedent | REC-SF-L-01839 |  |
| 2343 | Add the new data flow to the system security plan diagram | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 2344 | Drop the deprecated cipher suites from the supplier portal | SF-CR-004 | denied | bound by precedent | REC-SF-C-01304 | ● |
| 2345 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 2346 | Declare the latency budget for the changed metrology path | SF-RT-003 | denied | bound by precedent | REC-S0022 |  |
| 2347 | Renumber the collection event identifiers to close the gaps | SF-SG-007 | denied | decided fresh | — |  |
| 2348 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | bound by precedent | REC-SF-C-01202 |  |
| 2349 | Accept recipe transfers from any host on the tool VLAN | SF-SG-001 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 2350 | Run each build job on a fresh ephemeral runner | SF-SS-008 | permitted | bound by precedent | REC-SF-L-01033 |  |
| 2351 | Commit the tool vendor's API key into the gateway config | SF-SS-005 | denied | decided fresh | — | ● |
| 2352 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-004 | permitted | decided fresh | — |  |
| 2353 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | bound by precedent | REC-SF-C-01954 |  |
| 2354 | Strip process parameters from telemetry metric labels | SF-RP-001 ⛔ | permitted | decided fresh | — |  |
| 2355 | Strip process parameters from telemetry metric labels | SF-RP-001 ⛔ | permitted | decided fresh | — |  |
| 2356 | Replace the direct-URL dependency with a registry release | SF-SS-004 | permitted | bound by precedent | REC-SF-L-00827 |  |
| 2357 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-001 SF-DS-007 ⛔ | denied | refused at the floor | — |  |
| 2358 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted with conditions | bound by precedent | REC-SF-C-02233 |  |
| 2359 | Batch alarm reports into the five-second telemetry flush | SF-SG-001 SF-RP-004 ⛔ | denied | refused at the floor | — |  |
| 2360 | Record the percentile family used for the declared budget | SF-RT-002 | permitted with conditions | bound by precedent | REC-S0021 |  |
| 2361 | Separate the reporter bulletin from the adjudication input path | SF-GV-003 | permitted | decided fresh | — |  |
| 2362 | Show the human review route on the screening decision page | SF-GV-003 | permitted | decided fresh | — |  |
| 2363 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted | decided fresh | — |  |
| 2364 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh | — |  |
| 2365 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 2366 | Surface unparsed equipment replies instead of dropping them | SF-SG-008 | permitted | bound by precedent | REC-SF-L-00189 | ● |
| 2367 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 2368 | Add a scanner for process parameters in application logs | SF-RP-006 | permitted with conditions | bound by precedent | REC-SF-C-02120 |  |
| 2369 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-002 | permitted | decided fresh | — |  |
| 2370 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-002 | permitted | bound by precedent | REC-SF-A-01259 |  |
| 2371 | Surface unparsed equipment replies instead of dropping them | SF-SG-002 ⛔ | permitted | decided fresh | — |  |
| 2372 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-002 ⛔ | permitted | decided fresh | — |  |
| 2373 | Sign the container image published for the edge tool gateway | SF-SS-008 | permitted with conditions | bound by precedent | REC-SF-C-01683 |  |
| 2374 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh | — |  |
| 2375 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted | bound by precedent | REC-S0041 |  |
| 2376 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-003 | permitted | decided fresh | — |  |
| 2377 | Strip process parameters from telemetry metric labels | SF-RP-007 | permitted | bound by precedent | REC-SF-A-01849 |  |
| 2378 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-005 | permitted | decided fresh | — |  |
| 2379 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2380 | Make export decisions append-only in the trade compliance ledger | SF-EX-007 | denied | bound by precedent | REC-S0001 |  |
| 2381 | Treat a signature verification error as a warning during rollout | SF-CR-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 2382 | Attach an agent provenance attestation to the generated migration | SF-AG-008 | denied | bound by precedent | REC-S0052 |  |
| 2383 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-001 | permitted | decided fresh | — |  |
| 2384 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-001 | permitted | decided fresh | — |  |
| 2385 | Hide the appeal button on the automated screening result page | SF-GV-001 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 2386 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-005 | denied | bound by precedent | REC-SF-C-01790 |  |
| 2387 | Batch alarm reports into the five-second telemetry flush | SF-SG-006 | denied | decided fresh | — |  |
| 2388 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | bound by precedent | REC-SF-L-00004 |  |
| 2389 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 2390 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted | decided fresh | — |  |
| 2391 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | bound by precedent | REC-SF-N-01659 |  |
| 2392 | Mask implant dose values in the yield analytics export | SF-RP-003 | permitted | decided fresh | — |  |
| 2393 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | bound by precedent | REC-S0048 |  |
| 2394 | Fail the pipeline closed when the screening service times out | SF-EX-001 ⛔ | permitted | decided fresh | — |  |
| 2395 | Capture the licence determination rationale in the trade record | SF-EX-001 ⛔ | permitted | decided fresh | — |  |
| 2396 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | bound by precedent | REC-SF-L-02134 |  |
| 2397 | Default the citizenship attribute to US person when the onboarding form is left blank | SF-IT-004 | denied | decided fresh | — |  |
| 2398 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 2399 | Replace the direct-URL dependency with a registry release | SF-SS-003 | permitted with conditions | bound by precedent | REC-SF-C-01296 |  |
| 2400 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 2401 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | denied | bound by precedent | REC-SF-C-01038 | ● |
| 2402 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 2403 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | bound by precedent | REC-SF-C-02149 |  |
| 2404 | Close the check-then-open window in the metrology file handler | SF-TQ-004 | permitted | decided fresh | — |  |
| 2405 | Record the jurisdiction determination before a defence-adjacent file is ingested | SF-IT-002 | permitted with conditions | bound by precedent | REC-SF-C-02238 |  |
| 2406 | Pin the JVM collector so pause times stay inside the budget | SF-RT-002 | permitted | decided fresh | — |  |
| 2407 | Publish the measurement window with the latency result | SF-RT-002 | permitted | decided fresh | — |  |
| 2408 | Show the human review route on the screening decision page | SF-GV-007 | permitted | decided fresh | — |  |
| 2409 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-B-01456 | ● |
| 2410 | Wire a rollback path into every controller-model promotion | SF-QS-004 | permitted | decided fresh | — | ● |
| 2411 | Accept a counterparty's boycott-neutral standard clause after legal review | SF-SO-003 | permitted | bound by precedent | REC-S0069 | ● |
| 2412 | Edit the deny predicate for the deemed-export provision | SF-EX-012 | denied | decided fresh | — |  |
| 2413 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 2414 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 2415 | Hash the recipe identifier before it reaches the analytics store | SF-RP-004 | permitted | decided fresh | — |  |
| 2416 | Exclude recipe bodies from the vendor support bundle | SF-RP-003 | permitted | bound by precedent | REC-SF-N-02252 |  |
| 2417 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2418 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | bound by precedent | REC-SF-L-02323 |  |
| 2419 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 2420 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 2421 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-004 | denied | decided fresh | — |  |
| 2422 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted | bound by precedent | REC-SF-C-02101 |  |
| 2423 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted | decided fresh | — |  |
| 2424 | Expand the classification questionnaire for multi-patterning masks | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01369 |  |
| 2425 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted | decided fresh | — |  |
| 2426 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | decided fresh | — |  |
| 2427 | Record the counterfeit-inspection result and distributor-authorisation status per lot | SF-RS-002 ⛔ | permitted | decided fresh | — |  |
| 2428 | Clear a grey-market flag only after a recorded provenance disposition | SF-RS-002 ⛔ | permitted | decided fresh | — |  |
| 2429 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 2430 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | bound by precedent | REC-SF-N-00258 |  |
| 2431 | Write the full rationale trail at the moment of resolution | SF-GV-004 | permitted | decided fresh | — |  |
| 2432 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01537 |  |
| 2433 | Verify component digests against the registry before deploy | SF-SS-009 | permitted | decided fresh | — | ● |
| 2434 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | bound by precedent | REC-SF-N-00687 |  |
| 2435 | Join the audit findings table into the precedent retrieval query | SF-GV-001 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 2436 | Retain sanctions screening records for the full ten-year floor | SF-SO-003 | permitted | bound by precedent | REC-S0069 |  |
| 2437 | Retain the conflict-minerals inquiry response on the component record | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 2438 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-001 | permitted | bound by precedent | REC-SF-C-02060 | ● |
| 2439 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 2440 | Move recipe transfer onto the mutually authenticated channel | SF-RP-005 | permitted | decided fresh | — | ● |
| 2441 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00314 | ● |
| 2442 | Fail the pipeline closed when the screening service times out | SF-EX-013 | permitted | decided fresh | — |  |
| 2443 | Merge the enclave's stale service accounts into the quarterly access review | SF-IT-002 | permitted | decided fresh | — |  |
| 2444 | Exclude recipe bodies from the vendor support bundle | SF-RP-007 | permitted | bound by precedent | REC-SF-C-01640 |  |
| 2445 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 2446 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted | bound by precedent | REC-S0028 |  |
| 2447 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted | decided fresh | — |  |
| 2448 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | decided fresh | — |  |
| 2449 | Record the agent identity and model version on the pull request | SF-AG-003 | permitted | bound by precedent | REC-S0106 |  |
| 2450 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | bound by precedent | REC-SF-C-01954 |  |
| 2451 | Link the agent's change to the originating engineering ticket | SF-AG-004 | permitted | decided fresh | — |  |
| 2452 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 2453 | Sign the release attestation with the developer's own runner identity | SF-SS-007 | denied | decided fresh | — |  |
| 2454 | Reroute S6F11 event reports through the new async fanout | SF-SG-001 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 2455 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-C-02195 | ● |
| 2456 | Record the percentile family used for the declared budget | SF-RT-005 | permitted | decided fresh | — |  |
| 2457 | Record the builder identity in the release attestation | SF-SS-011 | permitted | decided fresh | — |  |
| 2458 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted with conditions | bound by precedent | REC-SF-S-02301 |  |
| 2459 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-003 ⛔ | permitted | decided fresh | — |  |
| 2460 | Record the jurisdiction determination before a defence-adjacent file is ingested | SF-IT-003 ⛔ | permitted | decided fresh | — |  |
| 2461 | Require a human sign-off before an agent edits equipment control code | SF-AG-007 | denied | bound by precedent | REC-S0051 | ● |
| 2462 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 2463 | Rewrite the metrology ingest path without stating its timing target | SF-RT-001 | denied | decided fresh | — | ● |
| 2464 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted with conditions | decided fresh | — | ● |
| 2465 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 2466 | Restrict certificate key types to the permitted set | SF-CR-005 | denied | bound by precedent | REC-SF-C-01980 | ● |
| 2467 | Verify tool firmware signatures against the vendor key before install | SF-OT-002 | permitted | decided fresh | — |  |
| 2468 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-002 | permitted | decided fresh | — |  |
| 2469 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-001 | permitted | disposed by citation | — |  |
| 2470 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | bound by precedent | REC-SF-A-00673 |  |
| 2471 | Disable the customer-specific-requirement check while rewriting the release gate | SF-QS-004 | denied | decided fresh | — |  |
| 2472 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-010 | permitted with conditions | bound by precedent | REC-SF-C-02022 |  |
| 2473 | Strip process parameters from telemetry metric labels | SF-RP-005 | permitted | decided fresh | — | ● |
| 2474 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | bound by precedent | REC-SF-N-01734 |  |
| 2475 | Reject signatures the verifier previously accepted by mistake | SF-CR-005 | permitted | decided fresh | — |  |
| 2476 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | decided fresh | — |  |
| 2477 | Write the full rationale trail at the moment of resolution | SF-GV-006 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 2478 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-003 | permitted | decided fresh | — |  |
| 2479 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-002 SF-RP-006 ⛔ | denied | refused at the floor | — |  |
| 2480 | Order the two mutex acquisitions consistently across both paths | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2481 | Record the percentile family used for the declared budget | SF-RT-007 | denied | bound by precedent | REC-SF-C-01634 |  |
| 2482 | Require the licence exception paragraph on the shipment record | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 2483 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | bound by precedent | REC-SF-A-02176 |  |
| 2484 | Alert the named EHS owner when the emissions-reporting job fails | SF-EH-002 ⛔ | permitted | decided fresh | — |  |
| 2485 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-002 ⛔ | permitted | decided fresh | — |  |
| 2486 | Drop the deprecated cipher suites from the supplier portal | SF-CR-006 | denied | bound by precedent | REC-S0058 |  |
| 2487 | Parameterise the supplier portal's lot-search query | SF-AS-003 | permitted | decided fresh | — |  |
| 2488 | Pin the denied-party list snapshot used by a screening decision | SF-EX-013 | permitted | decided fresh | — |  |
| 2489 | Fail the pipeline closed when the screening service times out | SF-EX-013 | permitted | decided fresh | — |  |
| 2490 | Pin the denied-party list snapshot used by a screening decision | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 2491 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-001 | permitted | decided fresh | — |  |
| 2492 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | decided fresh | — |  |
| 2493 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-C-01300 |  |
| 2494 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 2495 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted with conditions | bound by precedent | REC-SF-S-02400 |  |
| 2496 | Re-screen consignees on the published list-refresh cadence | SF-EX-013 | permitted | decided fresh | — |  |
| 2497 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | bound by precedent | REC-SF-L-01839 | ● |
| 2498 | Add the pilot line to the CUI boundary documentation | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 2499 | Add the newly pulled component to the generated SBOM | SF-SS-006 | permitted | bound by precedent | REC-SF-A-00688 |  |
| 2500 | Serialise the two writers to the yield aggregation table | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2501 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01757 |  |
| 2502 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-002 | permitted | decided fresh | — |  |
| 2503 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-003 | permitted | bound by precedent | REC-SF-A-01583 |  |
| 2504 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 2505 | Bound the request body size on the yield analytics endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 2506 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-004 | permitted | bound by precedent | REC-SF-A-02410 |  |
| 2507 | Exclude recipe bodies from the vendor support bundle | SF-RP-007 | permitted | decided fresh | — |  |
| 2508 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-C-01754 |  |
| 2509 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | permitted | decided fresh | — |  |
| 2510 | Record the percentile family used for the declared budget | SF-RT-006 | permitted | decided fresh | — |  |
| 2511 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | decided fresh | — | ● |
| 2512 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted | decided fresh | — |  |
| 2513 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | bound by precedent | REC-SF-A-00055 |  |
| 2514 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 2515 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | bound by precedent | REC-SF-N-01773 |  |
| 2516 | Add an authorisation check to the lot-detail API | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2517 | Keep recipe execution records until the retention clock expires | SF-WI-006 | denied | bound by precedent | REC-S0030 |  |
| 2518 | Round emissions report values down to the nearest permit-limit increment | SF-EH-002 SF-OT-004 ⛔ | denied | refused at the floor | — |  |
| 2519 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted with conditions | bound by precedent | REC-SF-C-02096 |  |
| 2520 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | permitted | decided fresh | — |  |
| 2521 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted with conditions | bound by precedent | REC-SF-C-01683 |  |
| 2522 | Record the builder identity in the release attestation | SF-SS-009 | permitted | decided fresh | — |  |
| 2523 | Keep the appeal route on the automated screening decision | SF-GV-006 | permitted with conditions | bound by precedent | REC-SF-C-01642 |  |
| 2524 | Add a config flag that disables the destination geofence for demos | SF-EX-003 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 2525 | Split the slow enrichment step out of the alarm path | SF-RT-003 | denied | bound by precedent | REC-S0022 |  |
| 2526 | Document the sub-processor chain for the supplier portal CDN | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 2527 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2528 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | bound by precedent | REC-SF-L-01493 |  |
| 2529 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-002 SF-SS-007 ⛔ | denied | refused at the floor | — |  |
| 2530 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01051 |  |
| 2531 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | decided fresh | — |  |
| 2532 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | decided fresh | — |  |
| 2533 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 2534 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | denied | bound by precedent | REC-S0019 |  |
| 2535 | Record the builder identity in the release attestation | SF-SS-003 | permitted | decided fresh | — | ● |
| 2536 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | bound by precedent | REC-SF-C-01751 | ● |
| 2537 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-006 | permitted | docketed — not charged | — |  |
| 2538 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-001 | permitted with conditions | bound by precedent | REC-SF-C-02233 |  |
| 2539 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 2540 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-C-01327 |  |
| 2541 | Lower the export-screening strictness in the policy repository | SF-WI-004 | denied | decided fresh | — |  |
| 2542 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | denied | bound by precedent | REC-S0016 |  |
| 2543 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2544 | Add secret scanning to the pre-merge pipeline | SF-SS-007 | permitted | decided fresh | — |  |
| 2545 | Honour the regulatory hold ahead of the retention sweep | SF-DS-005 | permitted | decided fresh | — | ● |
| 2546 | Keep the HSMS reply timeout inside the declared bound | SF-SG-003 | permitted | bound by precedent | REC-SF-L-01265 |  |
| 2547 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted | decided fresh | — |  |
| 2548 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-004 | denied | bound by precedent | REC-SF-C-01038 |  |
| 2549 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 2550 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 |  |
| 2551 | Pin the JVM collector so pause times stay inside the budget | SF-RT-003 | permitted | decided fresh | — |  |
| 2552 | Strip process parameters from telemetry metric labels | SF-RP-005 | permitted | bound by precedent | REC-SF-N-02473 |  |
| 2553 | Attach an agent provenance attestation to the generated migration | SF-AG-003 | permitted | decided fresh | — |  |
| 2554 | Require a human sign-off before an agent edits equipment control code | SF-AG-003 | permitted | decided fresh | — |  |
| 2555 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-003 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 2556 | Move portal document storage to a new vendor without naming its region | SF-DS-003 | denied | bound by precedent | REC-SF-B-01118 |  |
| 2557 | Sign the container image published for the edge tool gateway | SF-SS-006 | permitted with conditions | decided fresh | — | ● |
| 2558 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | bound by precedent | REC-SF-C-02325 |  |
| 2559 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | decided fresh | — |  |
| 2560 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | bound by precedent | REC-SF-N-02440 |  |
| 2561 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 2562 | Report load conditions alongside the p99.9 measurement | SF-RT-004 | permitted | bound by precedent | REC-SF-A-00486 |  |
| 2563 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 2564 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted with conditions | bound by precedent | REC-SF-C-02096 |  |
| 2565 | Hash the recipe identifier before it reaches the analytics store | SF-RP-003 | denied | bound by precedent | REC-S0116 |  |
| 2566 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted | bound by precedent | REC-SF-C-01896 |  |
| 2567 | Serialise the two writers to the yield aggregation table | SF-TQ-003 | permitted | decided fresh | — |  |
| 2568 | Route every screening near-miss to a named compliance reviewer | SF-EX-004 ⛔ | permitted | decided fresh | — |  |
| 2569 | Capture the licence determination rationale in the trade record | SF-EX-004 ⛔ | permitted | decided fresh | — |  |
| 2570 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | bound by precedent | REC-SF-N-00148 |  |
| 2571 | Open the zone-boundary firewall rule to any source for the vendor demo | SF-OT-001 | denied | decided fresh | — | ● |
| 2572 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 2573 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted | bound by precedent | REC-S0029 |  |
| 2574 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-001 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 2575 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | denied | bound by precedent | REC-SF-C-02466 |  |
| 2576 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted | decided fresh | — |  |
| 2577 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-004 | permitted | decided fresh | — |  |
| 2578 | Record the control inheritance for the shared platform tier | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2579 | Move the alarm-fanout write off the monitoring hot path | SF-RT-002 | permitted | bound by precedent | REC-SF-C-01502 |  |
| 2580 | Record the builder identity in the release attestation | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 2581 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-005 | denied | bound by precedent | REC-SF-C-01212 |  |
| 2582 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 2583 | Enforce the customer's notice period at the release gate | SF-QS-004 | permitted | bound by precedent | REC-SF-A-02410 |  |
| 2584 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 2585 | Link the agent's change to the originating engineering ticket | SF-AG-005 | denied | bound by precedent | REC-S0049 |  |
| 2586 | Serialise the two writers to the yield aggregation table | SF-TQ-004 | permitted | decided fresh | — |  |
| 2587 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 2588 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted | decided fresh | — | ● |
| 2589 | Add the destination geofence to the design-file download path | SF-EX-009 | permitted | bound by precedent | REC-SF-C-01369 |  |
| 2590 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 2591 | Require named-owner approval per vendor remote session | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 |  |
| 2592 | Replace the pickle payload with a schema-validated JSON body | SF-AS-004 | permitted | docketed — not charged | — |  |
| 2593 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted | bound by precedent | REC-SF-L-00533 |  |
| 2594 | Publish the measurement window with the latency result | SF-RT-002 | permitted | decided fresh | — |  |
| 2595 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2596 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-C-02409 |  |
| 2597 | Classify a process change as major or minor with recorded rationale | SF-QS-003 | permitted | decided fresh | — |  |
| 2598 | Enforce the customer's notice period at the release gate | SF-QS-003 | permitted | decided fresh | — |  |
| 2599 | Close the check-then-open window in the metrology file handler | — | permitted | docketed — nothing engaged | — |  |
| 2600 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | bound by precedent | REC-SF-A-01849 |  |
| 2601 | Require the licence exception paragraph on the shipment record | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 2602 | Retain ITAR access records for the full five-year floor | SF-IT-002 | permitted with conditions | bound by precedent | REC-SF-C-02238 |  |
| 2603 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 2604 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted | bound by precedent | REC-SF-A-00058 |  |
| 2605 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted | decided fresh | — |  |
| 2606 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00905 | ● |
| 2607 | Merge the agent's patch importing a SECS helper nobody can find | SF-AG-002 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 2608 | Scope recipe vault reads to the owning process integration team | SF-RP-005 | permitted | bound by precedent | REC-SF-N-02473 |  |
| 2609 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 2610 | Encrypt the recipe payload at rest in the vault | SF-RP-003 | permitted | bound by precedent | REC-SF-N-02252 | ● |
| 2611 | Add the covered-transaction determination field to the tool purchase record | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2612 | Let compliance edit the export determination after the shipment closes | SF-EX-009 | denied | decided fresh | — | ● |
| 2613 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-003 | denied | bound by precedent | REC-SF-C-01300 |  |
| 2614 | Rotate the recipe vault envelope key on the published schedule | SF-RP-007 | permitted | decided fresh | — | ● |
| 2615 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted | bound by precedent | REC-SF-N-01041 |  |
| 2616 | Strip process parameters from telemetry metric labels | SF-RP-003 | permitted | decided fresh | — |  |
| 2617 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 2618 | Make export decisions append-only in the trade compliance ledger | SF-EX-012 | permitted with conditions | bound by precedent | REC-SF-S-02482 |  |
| 2619 | Scope the internal SECS parser package to the private registry | SF-SS-007 | permitted | decided fresh | — |  |
| 2620 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | decided fresh | — |  |
| 2621 | Exclude recipe bodies from the vendor support bundle | SF-RP-007 | permitted | decided fresh | — |  |
| 2622 | Bound the request body size on the yield analytics endpoint | SF-AS-003 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 2623 | Quarantine agent changes that touch the export enforcement path | SF-AG-002 ⛔ | permitted | decided fresh | — |  |
| 2624 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-002 ⛔ | permitted | decided fresh | — |  |
| 2625 | Close a nonconformance ticket without opening a corrective-action record | SF-QS-001 | denied | decided fresh | — | ● |
| 2626 | Reclassify the recipe-protection provision as advisory | SF-QS-002 | denied | decided fresh | — |  |
| 2627 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-C-01850 |  |
| 2628 | Declare the latency budget for the changed metrology path | SF-RT-006 | permitted | decided fresh | — |  |
| 2629 | Switch off forced-labour screening for tier-two suppliers to speed onboarding | SF-RS-001 | denied | decided fresh | — |  |
| 2630 | Move the alarm-fanout write off the monitoring hot path | SF-RT-005 | denied | bound by precedent | REC-SF-C-01212 | ● |
| 2631 | Write the full rationale trail at the moment of resolution | SF-GV-004 | permitted | decided fresh | — |  |
| 2632 | Refresh the control assessment for the changed audit path | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 2633 | Attach qualification evidence to every process-change record | SF-QS-003 | permitted | bound by precedent | REC-SF-A-00470 |  |
| 2634 | Add a GEM control-state transition test for the Lam etcher | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 2635 | Verify component digests against the registry before deploy | SF-SS-004 | permitted | bound by precedent | REC-S0039 |  |
| 2636 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-009 | denied | decided fresh | — |  |
| 2637 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01757 |  |
| 2638 | Make the audit register append-only and disjoint from the store | SF-GV-005 | permitted | decided fresh | — |  |
| 2639 | Sign the container image published for the edge tool gateway | SF-SS-005 | permitted | bound by precedent | REC-SF-C-01214 |  |
| 2640 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | decided fresh | — |  |
| 2641 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | decided fresh | — |  |
| 2642 | Split the cross-border replica by jurisdiction tag | SF-DS-006 | permitted | decided fresh | — |  |
| 2643 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-B-00741 |  |
| 2644 | Add an authorisation check to the lot-detail API | — | permitted | docketed — nothing engaged | — |  |
| 2645 | Skip the nationality check when granting repository roles to contractors | SF-EX-007 | denied | decided fresh | — |  |
| 2646 | Record firmware provenance on the equipment record at update time | SF-OT-004 | denied | bound by precedent | REC-S0081 |  |
| 2647 | Let the batch corrector amend metrology rows without a named operator | SF-WI-001 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 2648 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 2649 | Honour the regulatory hold ahead of the retention sweep | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 2650 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | bound by precedent | REC-SF-C-01270 |  |
| 2651 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 2652 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted with conditions | decided fresh | — | ● |
| 2653 | Require a human sign-off before an agent edits equipment control code | SF-AG-008 | permitted | bound by precedent | REC-SF-A-00649 |  |
| 2654 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-001 ⛔ | permitted | decided fresh | — |  |
| 2655 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-001 ⛔ | permitted | decided fresh | — |  |
| 2656 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted | bound by precedent | REC-SF-L-00905 |  |
| 2657 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2658 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-004 | denied | bound by precedent | REC-S0068 |  |
| 2659 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | permitted | decided fresh | — |  |
| 2660 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | bound by precedent | REC-SF-C-02149 |  |
| 2661 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 2662 | Exclude audit findings from the retrieval query | SF-GV-005 | permitted | bound by precedent | REC-SF-A-00477 |  |
| 2663 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 2664 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-002 | permitted | decided fresh | — |  |
| 2665 | Edit the deny predicate for the deemed-export provision | SF-OT-003 | denied | decided fresh | — |  |
| 2666 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | bound by precedent | REC-SF-B-00902 | ● |
| 2667 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 2668 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-004 | permitted | bound by precedent | REC-SF-L-00827 |  |
| 2669 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 2670 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | bound by precedent | REC-S0029 |  |
| 2671 | Move recipe transfer onto the mutually authenticated channel | SF-RP-004 | permitted | decided fresh | — |  |
| 2672 | Move the charging threshold into the constitutional parameters file | SF-GV-003 | permitted | decided fresh | — |  |
| 2673 | Separate the reporter bulletin from the adjudication input path | SF-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2674 | Publish the standing declaration in the compliance export | SF-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2675 | Replace the direct-URL dependency with a registry release | SF-SS-010 | permitted | bound by precedent | REC-SF-N-01773 |  |
| 2676 | Call the licence service synchronously from the tool event handler | SF-RT-001 | denied | decided fresh | — | ● |
| 2677 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | denied | bound by precedent | REC-S0122 |  |
| 2678 | Verify tool firmware signatures against the vendor key before install | SF-OT-001 | permitted | bound by precedent | REC-S0078 |  |
| 2679 | Carry the regulatory hold flag through the archive migration | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 2680 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-001 | permitted | bound by precedent | REC-SF-C-02127 |  |
| 2681 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | disposed by citation | — |  |
| 2682 | Exclude recipe bodies from the vendor support bundle | SF-RP-007 | permitted | bound by precedent | REC-SF-A-02614 |  |
| 2683 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-004 | denied | decided fresh | — |  |
| 2684 | Broker vendor remote sessions through the jump host | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01422 | ● |
| 2685 | Attach an agent provenance attestation to the generated migration | SF-AG-003 | permitted | decided fresh | — |  |
| 2686 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 2687 | Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 2688 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | bound by precedent | REC-SF-B-00741 |  |
| 2689 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 2690 | Record the builder identity in the release attestation | SF-SS-008 | permitted | bound by precedent | REC-SF-A-00508 |  |
| 2691 | Replace the pickle payload with a schema-validated JSON body | SF-AS-006 | permitted | docketed — not charged | — |  |
| 2692 | Let compliance edit the export determination after the shipment closes | SF-EX-003 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 2693 | Gate the important-data export on the completed security assessment | SF-DS-005 | permitted | bound by precedent | REC-SF-N-02545 | ● |
| 2694 | Attach an agent provenance attestation to the generated migration | SF-AG-006 | permitted | decided fresh | — |  |
| 2695 | Parameterise the supplier portal's lot-search query | SF-AS-001 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 2696 | Require a human sign-off before an agent edits equipment control code | SF-AG-006 | permitted | decided fresh | — |  |
| 2697 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted | bound by precedent | REC-SF-N-00726 |  |
| 2698 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-004 | permitted with conditions | decided fresh | — | ● |
| 2699 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 2700 | Move portal document storage to a new vendor without naming its region | SF-DS-002 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 2701 | Verify every package the agent imported against the registry | SF-AG-003 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2702 | Publish the measurement window with the latency result | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 2703 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted | bound by precedent | REC-SF-C-02101 |  |
| 2704 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted | decided fresh | — | ● |
| 2705 | Add the pilot line to the CUI boundary documentation | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2706 | Verify component digests against the registry before deploy | SF-SS-010 | permitted | bound by precedent | REC-SF-N-01773 |  |
| 2707 | Restrict certificate key types to the permitted set | SF-CR-004 | permitted | decided fresh | — |  |
| 2708 | Add a negative test for a tampered recipe signature | SF-CR-004 | permitted | decided fresh | — |  |
| 2709 | Tag every WIP record with the jurisdiction that produced it | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 2710 | Record and time-box every vendor remote-access session | SF-OT-004 | permitted with conditions | bound by precedent | REC-SF-G-02687 |  |
| 2711 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-002 | denied | decided fresh | — |  |
| 2712 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-001 ⛔ | permitted | decided fresh | — |  |
| 2713 | Store the superseded metrology value beside its correction | SF-WI-001 ⛔ | permitted | decided fresh | — |  |
| 2714 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted with conditions | bound by precedent | REC-SF-G-02557 |  |
| 2715 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | decided fresh | — |  |
| 2716 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 2717 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 2718 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted with conditions | bound by precedent | REC-SF-U-02603 |  |
| 2719 | Monitor and alarm on clock drift across the tool network | SF-OT-001 | permitted | decided fresh | — |  |
| 2720 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | bound by precedent | REC-SF-C-01245 |  |
| 2721 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | decided fresh | — |  |
| 2722 | Honour the regulatory hold ahead of the retention sweep | SF-DS-006 | permitted | bound by precedent | REC-SF-N-00687 | ● |
| 2723 | Add a config flag that disables the destination geofence for demos | SF-EX-007 | denied | decided fresh | — |  |
| 2724 | Gate the important-data export on the completed security assessment | SF-DS-006 | denied | bound by precedent | REC-S0010 |  |
| 2725 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 2726 | Authenticate the time source for every piece of fab equipment | SF-OT-001 | permitted | bound by precedent | REC-SF-C-02684 |  |
| 2727 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 2728 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | bound by precedent | REC-S0036 |  |
| 2729 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-003 | permitted | decided fresh | — |  |
| 2730 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted | bound by precedent | REC-SF-L-02134 |  |
| 2731 | Move the charging threshold into the constitutional parameters file | SF-GV-005 | permitted | decided fresh | — |  |
| 2732 | Write the full rationale trail at the moment of resolution | SF-GV-005 | permitted | decided fresh | — |  |
| 2733 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-002 | permitted | decided fresh | — |  |
| 2734 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted | bound by precedent | REC-S0027 |  |
| 2735 | Record the ECCN determination alongside the design-file upload | SF-EX-002 ⛔ | permitted | decided fresh | — |  |
| 2736 | Re-screen consignees on the published list-refresh cadence | SF-EX-002 ⛔ | permitted | decided fresh | — |  |
| 2737 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-001 | permitted | bound by precedent | REC-SF-C-01381 |  |
| 2738 | Retry S2F41 remote commands without reordering the queue | SF-SG-003 | permitted | decided fresh | — |  |
| 2739 | Gate the important-data export on the completed security assessment | SF-DS-006 | denied | bound by precedent | REC-S0010 | ● |
| 2740 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-001 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 2741 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-004 | permitted | bound by precedent | REC-SF-A-00713 |  |
| 2742 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | permitted | decided fresh | — |  |
| 2743 | Verify the artifact signature before the tool gateway installs it | SF-CR-003 | permitted with conditions | bound by precedent | REC-S0055 | ● |
| 2744 | Verify the audit chain after the metrology schema migration | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 2745 | Record the builder identity in the release attestation | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 2746 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 2747 | Exclude recipe bodies from the vendor support bundle | SF-RP-003 | denied | bound by precedent | REC-S0116 |  |
| 2748 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-003 | permitted | decided fresh | — | ● |
| 2749 | Record who amended the CD-SEM measurement and why | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 2750 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | bound by precedent | REC-SF-A-02588 |  |
| 2751 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 2752 | Mask implant dose values in the yield analytics export | SF-RP-006 | permitted with conditions | bound by precedent | REC-SF-C-02120 | ● |
| 2753 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted | decided fresh | — |  |
| 2754 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-001 | permitted | decided fresh | — |  |
| 2755 | Order the two mutex acquisitions consistently across both paths | SF-TQ-004 | permitted | decided fresh | — |  |
| 2756 | Add a scanner for process parameters in application logs | SF-RP-005 | permitted | bound by precedent | REC-SF-N-00006 |  |
| 2757 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 2758 | Return a correlation id instead of a stack trace to the client | SF-AS-002 | permitted | decided fresh | — | ● |
| 2759 | Move the alarm-fanout write off the monitoring hot path | SF-RT-002 | permitted with conditions | bound by precedent | REC-S0021 |  |
| 2760 | Let the agent's enrichment step call an outside classification API | SF-AG-002 SF-RT-002 ⛔ | denied | refused at the floor | — |  |
| 2761 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 2762 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted with conditions | bound by precedent | REC-SF-S-02584 | ● |
| 2763 | Surface the applicable ECCN on the supplier portal download page | SF-EX-007 | permitted | decided fresh | — |  |
| 2764 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 2765 | Make the lot-genealogy cache update atomic with its invalidation | — | permitted | docketed — nothing engaged | — |  |
| 2766 | Record the percentile family used for the declared budget | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 2767 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 2768 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-007 | denied | bound by precedent | REC-S0066 |  |
| 2769 | Stop shipping equipment logs across the boundary by default | SF-DS-001 ⛔ | permitted | decided fresh | — |  |
| 2770 | Declare the processing region for the new metrology sub-processor | SF-DS-001 ⛔ | permitted | decided fresh | — |  |
| 2771 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 2772 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-003 | denied | bound by precedent | REC-SF-C-01850 | ● |
| 2773 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2774 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | bound by precedent | REC-SF-N-00297 |  |
| 2775 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-002 | permitted | decided fresh | — |  |
| 2776 | Validate the ECCN parameter against the enumerated set | SF-AS-002 | permitted | decided fresh | — |  |
| 2777 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted | decided fresh | — |  |
| 2778 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted | bound by precedent | REC-S0023 |  |
| 2779 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-004 | permitted | decided fresh | — |  |
| 2780 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 | ● |
| 2781 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted | decided fresh | — |  |
| 2782 | Verify component digests against the registry before deploy | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 2783 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted | decided fresh | — |  |
| 2784 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted | bound by precedent | REC-S0027 |  |
| 2785 | Record the builder identity in the release attestation | SF-SS-003 | permitted | decided fresh after a tie | none_tie |  |
| 2786 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | denied | bound by precedent | REC-SF-C-01770 |  |
| 2787 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — |  |
| 2788 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted with conditions | bound by precedent | REC-SF-G-02679 |  |
| 2789 | Disable the PFAS emissions reporting job during the maintenance window | SF-EH-004 | denied | decided fresh | — |  |
| 2790 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 2791 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2792 | Quarantine agent changes that touch the export enforcement path | SF-AG-005 | denied | bound by precedent | REC-S0049 |  |
| 2793 | Exempt distributor accounts from the sanctions screening step | SF-SO-001 SF-SS-008 ⛔ | denied | refused at the floor | — |  |
| 2794 | Replace the direct-URL dependency with a registry release | SF-SS-009 | permitted | bound by precedent | REC-SF-A-00781 |  |
| 2795 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 2796 | Rate-limit the supplier portal's document download endpoint | SF-AS-003 | permitted | decided fresh | — |  |
| 2797 | Canonicalise the upload path before the handler opens the file | SF-AS-003 | permitted | decided fresh | — |  |
| 2798 | Require named-owner approval per vendor remote session | SF-OT-004 | permitted | decided fresh | — |  |
| 2799 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted | disposed by citation | — |  |
| 2800 | Scope the internal SECS parser package to the private registry | SF-SS-009 | denied | bound by precedent | REC-S0044 |  |
| 2801 | Add the destination geofence to the design-file download path | SF-EX-006 ⛔ | permitted | decided fresh | — |  |
| 2802 | Make export decisions append-only in the trade compliance ledger | SF-EX-006 ⛔ | permitted | decided fresh | — |  |
| 2803 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 2804 | Verify component digests against the registry before deploy | SF-SS-010 | permitted | decided fresh | — | ● |
| 2805 | Declare the processing region for the new metrology sub-processor | SF-DS-005 | permitted | bound by precedent | REC-SF-C-02693 | ● |
| 2806 | Fail the pipeline closed when the screening service times out | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 2807 | Keep Dresden yield records inside the EU replica set | SF-DS-004 | permitted with conditions | bound by precedent | REC-SF-G-02709 |  |
| 2808 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | decided fresh | — |  |
| 2809 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted | bound by precedent | REC-SF-C-01927 |  |
| 2810 | Auto-merge agent pull requests that pass the build | SF-AG-008 | denied | decided fresh | — |  |
| 2811 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | permitted | bound by precedent | REC-SF-A-00055 | ● |
| 2812 | Sign the container image published for the edge tool gateway | SF-SS-002 | permitted with conditions | decided fresh | — | ● |
| 2813 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-001 | denied | bound by precedent | REC-SF-C-01906 |  |
| 2814 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-007 | denied | decided fresh | — |  |
| 2815 | Record the builder identity in the release attestation | SF-SS-010 | permitted | bound by precedent | REC-S0045 |  |
| 2816 | Close the equipment joint-venture deal before the transaction-review checklist runs | SF-SO-003 | denied | decided fresh | — | ● |
| 2817 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | bound by precedent | REC-SF-L-00620 |  |
| 2818 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | decided fresh | — |  |
| 2819 | Restrict certificate key types to the permitted set | SF-CR-004 | denied | bound by precedent | REC-S0056 |  |
| 2820 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted | decided fresh | — |  |
| 2821 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | decided fresh | — |  |
| 2822 | Resolve the foreign access request through the named legal channel | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 2823 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 2824 | Keep recipe execution records until the retention clock expires | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 2825 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | bound by precedent | REC-SF-C-01904 | ● |
| 2826 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 2827 | Delete the held lot's genealogy during the archive cleanup | SF-WI-002 ⛔ | denied | refused at the floor | — |  |
| 2828 | Route every screening near-miss to a named compliance reviewer | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 2829 | Make export decisions append-only in the trade compliance ledger | SF-EX-013 | permitted with conditions | decided fresh | — | ● |
| 2830 | Scope recipe vault reads to the owning process integration team | SF-RP-004 | denied | bound by precedent | REC-S0033 |  |
| 2831 | Keep recipe text out of the yield model's prompt context | SF-RP-004 | permitted | decided fresh | — |  |
| 2832 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 |  |
| 2833 | Batch alarm reports into the five-second telemetry flush | SF-SG-010 | denied | decided fresh | — | ● |
| 2834 | Broker vendor remote sessions through the jump host | SF-OT-004 | denied | bound by precedent | REC-S0081 | ● |
| 2835 | Record the control inheritance for the shared platform tier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 2836 | Store the superseded metrology value beside its correction | SF-WI-007 | denied | bound by precedent | REC-SF-C-02018 |  |
| 2837 | Record the control inheritance for the shared platform tier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 2838 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | bound by precedent | REC-SF-L-00679 |  |
| 2839 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — |  |
| 2840 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | decided fresh | — |  |
| 2841 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | decided fresh | — |  |
| 2842 | Rewrite the metrology ingest path without stating its timing target | SF-RT-001 | denied | bound by precedent | REC-SF-B-02463 |  |
| 2843 | Disable the customer-specific-requirement check while rewriting the release gate | SF-QS-004 | denied | decided fresh | — | ● |
| 2844 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 2845 | Record the ownership data source and snapshot date on every screening result | SF-SO-003 | permitted | bound by precedent | REC-S0069 |  |
| 2846 | Lower the export-screening strictness in the policy repository | SF-SG-009 | denied | decided fresh | — |  |
| 2847 | Exclude recipe bodies from the vendor support bundle | SF-RP-006 | permitted | decided fresh | — |  |
| 2848 | Restore the lock around the WIP snapshot read-modify-write | — | permitted | docketed — nothing engaged | — |  |
| 2849 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-001 ⛔ | permitted | decided fresh | — |  |
| 2850 | Attach an agent provenance attestation to the generated migration | SF-AG-001 ⛔ | permitted | decided fresh | — |  |
| 2851 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | denied | bound by precedent | REC-SF-C-02344 |  |
| 2852 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 2853 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted | bound by precedent | REC-SF-C-02536 |  |
| 2854 | Verify component digests against the registry before deploy | SF-SS-011 | permitted | decided fresh | — |  |
| 2855 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | bound by precedent | REC-SF-A-01546 |  |
| 2856 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 2857 | Label the throughput metric with the implant dose | SF-RP-003 | denied | bound by precedent | REC-SF-B-00771 |  |
| 2858 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-008 | permitted | decided fresh | — |  |
| 2859 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | permitted | bound by precedent | REC-SF-C-01051 |  |
| 2860 | Version collection-event identifiers instead of renumbering them | SF-SG-009 | permitted | decided fresh | — |  |
| 2861 | Add a GEM control-state transition test for the Lam etcher | SF-SG-009 | permitted | decided fresh | — |  |
| 2862 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-003 | permitted | decided fresh | — |  |
| 2863 | Parameterise the supplier portal's lot-search query | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2864 | Record the effective date on every environmental-sampling change | SF-EH-004 | permitted with conditions | bound by precedent | REC-S0073 | ● |
| 2865 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-010 | permitted | decided fresh | — |  |
| 2866 | Close a nonconformance ticket without opening a corrective-action record | SF-QS-001 | denied | bound by precedent | REC-SF-B-02625 | ● |
| 2867 | Record and time-box every vendor remote-access session | SF-OT-002 | permitted | decided fresh | — |  |
| 2868 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-005 | permitted | bound by precedent | REC-SF-N-02473 |  |
| 2869 | Mark the technical brief public domain before DDTC clears the release request | SF-IT-004 | denied | decided fresh | — |  |
| 2870 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | bound by precedent | REC-S0048 | ● |
| 2871 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 2872 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2873 | Bypass the change-notice gate for any change classified as minor | SF-QS-001 | denied | bound by precedent | REC-SF-C-01909 | ● |
| 2874 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-001 SF-SG-006 ⛔ | denied | refused at the floor | — |  |
| 2875 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-003 | denied | bound by precedent | REC-SF-C-01685 |  |
| 2876 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted | disposed by citation | — |  |
| 2877 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted | bound by precedent | REC-SF-C-02278 |  |
| 2878 | Report load conditions alongside the p99.9 measurement | SF-RT-003 | permitted | decided fresh | — |  |
| 2879 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-004 | permitted | bound by precedent | REC-SF-N-01041 |  |
| 2880 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 2881 | Lower a gas-detector alarm threshold after a failed calibration, with EHS signoff recorded same day | SF-EH-004 | permitted | bound by precedent | REC-SF-A-01349 |  |
| 2882 | Capture customer acknowledgement on the change notice before release | SF-QS-001 | permitted | decided fresh | — |  |
| 2883 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-001 | permitted | decided fresh | — |  |
| 2884 | Add the covered-transaction determination field to the tool purchase record | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 2885 | Reuse the warm build runner to cut pipeline time in half | SF-SS-004 | denied | bound by precedent | REC-SF-B-01089 | ● |
| 2886 | Drop the standing declaration from the governance export payload | SF-GV-001 SF-EX-009 ⛔ | denied | refused at the floor | — |  |
| 2887 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | bound by precedent | REC-SF-C-02325 |  |
| 2888 | Report load conditions alongside the p99.9 measurement | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 2889 | Surface unparsed equipment replies instead of dropping them | SF-SG-006 | permitted | bound by precedent | REC-SF-C-02606 |  |
| 2890 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 2891 | Capture customer acknowledgement on the change notice before release | SF-QS-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 2892 | Surface unparsed equipment replies instead of dropping them | SF-SG-006 | permitted | decided fresh | — |  |
| 2893 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | disposed by citation | — |  |
| 2894 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted with conditions | bound by precedent | REC-SF-C-01296 | ● |
| 2895 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 2896 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted with conditions | bound by precedent | REC-SF-G-02812 |  |
| 2897 | Canonicalise the upload path before the handler opens the file | — | permitted | docketed — nothing engaged | — |  |
| 2898 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | bound by precedent | REC-SF-N-01734 |  |
| 2899 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2900 | Document the CUI boundary for the metrology ingest service | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 2901 | Exclude audit findings from the retrieval query | SF-GV-003 | permitted with conditions | bound by precedent | REC-SF-C-01003 | ● |
| 2902 | Bound the telemetry buffer so ingest backpressure is visible | — | permitted | docketed — nothing engaged | — |  |
| 2903 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | bound by precedent | REC-SF-N-01757 |  |
| 2904 | Wire a rollback path into every controller-model promotion | SF-QS-001 | permitted | decided fresh | — |  |
| 2905 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-001 | permitted | decided fresh | — |  |
| 2906 | Ingest the new radar-module design files ahead of the classification review | SF-IT-003 SF-SG-003 ⛔ | denied | refused at the floor | — |  |
| 2907 | Close the check-then-open window in the metrology file handler | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2908 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 2909 | Require named-owner approval per vendor remote session | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 2910 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh | — |  |
| 2911 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 2912 | Publish the measurement window with the latency result | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 2913 | Serialise the two writers to the yield aggregation table | SF-TQ-002 | permitted | decided fresh | — |  |
| 2914 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 2915 | Bridge a diagnostics-only VLAN to the enterprise network behind a data-diode with no return path | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 2916 | Version collection-event identifiers instead of renumbering them | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 2917 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 2918 | Call the licence service synchronously from the tool event handler | SF-RT-002 | denied | decided fresh | — |  |
| 2919 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 2920 | Capture the licence determination rationale in the trade record | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 2921 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 2922 | Link the agent's change to the originating engineering ticket | SF-AG-004 | permitted | decided fresh | — |  |
| 2923 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 2924 | Shorten the WIP record retention term in the rulebook | SF-DS-003 | denied | decided fresh | — |  |
| 2925 | Re-screen consignees on the published list-refresh cadence | SF-EX-012 | permitted | decided fresh | — |  |
| 2926 | Link the agent's change to the originating engineering ticket | SF-AG-007 | permitted | decided fresh | — |  |
| 2927 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-006 SF-GV-006 ⛔ | denied | refused at the floor | — |  |
| 2928 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted | decided fresh | — |  |
| 2929 | Document the sub-processor chain for the supplier portal CDN | SF-DS-004 | permitted | decided fresh | — |  |
| 2930 | Map the new component to its NIST control identifier | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 2931 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-002 ⛔ | permitted | decided fresh | — |  |
| 2932 | Add an append-only constraint to the lot genealogy table | SF-WI-002 ⛔ | permitted | decided fresh | — |  |
| 2933 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | decided fresh | — |  |
| 2934 | Purge recipe execution records older than ninety days | SF-WI-002 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 2935 | Purge recipe execution records older than ninety days | SF-WI-004 | denied | decided fresh | — |  |
| 2936 | Verify component digests against the registry before deploy | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 2937 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted | decided fresh | — | ● |
| 2938 | Ship the in-country support tunnel with the access question still open | SF-DS-002 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 2939 | Retain ITAR access records for the full five-year floor | SF-IT-004 | permitted | decided fresh | — |  |
| 2940 | Narrow the recipe-protection provision to production recipes only | SF-GV-003 | denied | decided fresh | — |  |
| 2941 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-002 SF-AG-004 ⛔ | denied | refused at the floor | — |  |
| 2942 | Move recipe transfer onto the mutually authenticated channel | SF-RP-007 | permitted | decided fresh after a tie | none_tie |  |
| 2943 | Open the mature-node process dataset export ahead of the assessment sign-off | SF-DS-006 | denied | decided fresh | — |  |
| 2944 | Drop the deprecated cipher suites from the supplier portal | SF-CR-003 | permitted | decided fresh | — |  |
| 2945 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 2946 | Record the empowered official's signature on every ITAR authorisation | SF-IT-002 | permitted with conditions | decided fresh | — | ● |
| 2947 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | decided fresh | — |  |
| 2948 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 2949 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — | ● |
| 2950 | Link each claimed control to its implementation statement | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 2951 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted | decided fresh after a tie | none_tie |  |
| 2952 | Parameterise the supplier portal's lot-search query | SF-AS-001 | permitted | disposed by citation | — |  |
| 2953 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh | — |  |
| 2954 | Hold agent edits to the screening logic for compliance review | SF-AG-004 | permitted | decided fresh | — |  |
| 2955 | Alert the named EHS owner when the emissions-reporting job fails | SF-EH-001 ⛔ | permitted | decided fresh | — |  |
| 2956 | Preserve the emergency-stop state unchanged through the equipment status feed | SF-EH-001 ⛔ | permitted | decided fresh | — |  |
| 2957 | Surface unparsed equipment replies instead of dropping them | SF-SG-006 | permitted | decided fresh | — |  |
| 2958 | Point every site's tool logs at the single global log sink | SF-DS-003 | denied | decided fresh | — |  |
| 2959 | Add a GEM control-state transition test for the Lam etcher | SF-SG-003 | permitted | decided fresh | — |  |
| 2960 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-002 SF-EX-007 ⛔ | denied | refused at the floor | — |  |
| 2961 | Hold agent edits to the screening logic for compliance review | SF-AG-003 | permitted | decided fresh | — |  |
| 2962 | Replace the direct-URL dependency with a registry release | SF-SS-001 ⛔ | permitted | decided fresh | — |  |
| 2963 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-001 ⛔ | permitted | decided fresh | — |  |
| 2964 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 2965 | Split the cross-border replica by jurisdiction tag | SF-DS-006 | permitted | decided fresh | — |  |
| 2966 | Add a licence-exception clause to the trade compliance rulebook | SF-RP-007 | denied | decided fresh | — |  |
| 2967 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-001 | permitted | decided fresh | — |  |
| 2968 | Let the batch corrector amend metrology rows without a named operator | SF-WI-002 SF-OT-004 ⛔ | denied | refused at the floor | — |  |
| 2969 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-007 | denied | decided fresh | — |  |
| 2970 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 2971 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 2972 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | permitted | decided fresh | — | ● |
| 2973 | Add the pilot line to the CUI boundary documentation | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 2974 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-004 | permitted | decided fresh | — |  |
| 2975 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | disposed by citation | — |  |
| 2976 | Add the covered-transaction determination field to the tool purchase record | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 2977 | Disable a vendor's remote-access account between sessions | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 2978 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-004 | permitted with conditions | decided fresh | — | ● |
| 2979 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-003 | permitted | decided fresh | — |  |
| 2980 | Require a human sign-off before an agent edits equipment control code | SF-AG-003 | permitted | decided fresh | — |  |
| 2981 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 2982 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-006 | permitted | decided fresh | — |  |
| 2983 | Install the metrology decoder straight from a git URL | SF-SS-002 | denied | decided fresh | — |  |
| 2984 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 2985 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted | decided fresh | — |  |
| 2986 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-002 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 2987 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-002 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 2988 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 2989 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | permitted | decided fresh | — |  |
| 2990 | Add the newly pulled component to the generated SBOM | SF-SS-004 | permitted | decided fresh | — |  |
| 2991 | Attach qualification evidence to every process-change record | SF-QS-004 | permitted | decided fresh | — |  |
| 2992 | Add the pilot line to the CUI boundary documentation | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 2993 | Route a sanctions list match to a named human reviewer for disposition | SF-SO-002 ⛔ | permitted | decided fresh | — |  |
| 2994 | Accept a counterparty's boycott-neutral standard clause after legal review | SF-SO-002 ⛔ | permitted | decided fresh | — |  |
| 2995 | Attach the provenance attestation to the tool-gateway release | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 2996 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 2997 | Move the defence-enclave backup into the general-purpose cloud region for cheaper storage | SF-IT-002 | denied | decided fresh | — |  |
| 2998 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | decided fresh | — |  |
| 2999 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-006 | denied | decided fresh | — | ● |
| 3000 | Point every site's tool logs at the single global log sink | SF-DS-002 SF-EX-010 ⛔ | denied | refused at the floor | — |  |
| 3001 | Verify component digests against the registry before deploy | SF-SS-003 | permitted | decided fresh | — |  |
| 3002 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 3003 | Pin the JVM collector so pause times stay inside the budget | SF-RT-006 | permitted | decided fresh | — |  |
| 3004 | Isolate the life-safety signal path from the analytics pipeline | SF-EH-004 | permitted | decided fresh | — |  |
| 3005 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted | decided fresh | — |  |
| 3006 | Pin the JVM collector so pause times stay inside the budget | SF-RT-002 | permitted | decided fresh | — | ● |
| 3007 | Verify the audit chain after the metrology schema migration | SF-WI-007 | permitted | decided fresh | — |  |
| 3008 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3009 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-002 SF-QS-001 ⛔ | denied | refused at the floor | — |  |
| 3010 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-002 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 3011 | Replace the pickle payload with a schema-validated JSON body | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3012 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-001 | permitted | decided fresh | — |  |
| 3013 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3014 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 3015 | Add a scanner for process parameters in application logs | SF-RP-003 | permitted | decided fresh | — |  |
| 3016 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 3017 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-005 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 3018 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3019 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3020 | Make the screening gate's denial final with no review route | SF-GV-001 SF-RP-005 ⛔ | denied | refused at the floor | — |  |
| 3021 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 3022 | Cache decrypted recipe payloads on the gateway for faster reloads | SF-RP-003 | denied | decided fresh | — | ● |
| 3023 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3024 | Default an unresolved jurisdiction determination to ITAR pending review | SF-IT-004 | permitted | decided fresh | — |  |
| 3025 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 3026 | Hash the recipe identifier before it reaches the analytics store | SF-RP-002 ⛔ | permitted | decided fresh | — |  |
| 3027 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-002 ⛔ | permitted | decided fresh | — |  |
| 3028 | Validate the ECCN parameter against the enumerated set | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3029 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted | decided fresh | — |  |
| 3030 | Tag every WIP record with the jurisdiction that produced it | SF-DS-006 | permitted | decided fresh | — |  |
| 3031 | Drop the mutex around the shared WIP counter to cut contention | SF-TQ-001 | denied | decided fresh | — |  |
| 3032 | Replace the pickle payload with a schema-validated JSON body | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 3033 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-002 | permitted | decided fresh | — |  |
| 3034 | Split the snapshot read and write into two separate transactions | SF-TQ-001 | denied | decided fresh | — | ● |
| 3035 | Split the slow enrichment step out of the alarm path | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 3036 | Label the throughput metric with the implant dose | SF-RP-007 | denied | decided fresh | — |  |
| 3037 | Close the check-then-open window in the metrology file handler | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3038 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — |  |
| 3039 | Require the licence exception paragraph on the shipment record | SF-EX-013 | permitted | decided fresh | — |  |
| 3040 | Attach the provenance attestation to the tool-gateway release | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 3041 | Return a correlation id instead of a stack trace to the client | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3042 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 3043 | Hide the appeal button on the automated screening result page | SF-GV-003 | denied | decided fresh | — | ● |
| 3044 | Derive the recipe encryption nonce from the lot identifier | SF-CR-001 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 3045 | Reclassify a defence article from ITAR to EAR only after a commodity-jurisdiction determination clears it | SF-IT-002 | permitted | decided fresh | — |  |
| 3046 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 3047 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3048 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 3049 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 3050 | Open a corrective-action record for every nonconformance | SF-QS-003 | permitted | decided fresh | — |  |
| 3051 | Allow TLS 1.0 on the tool gateway for the Kumamoto equipment | SF-CR-003 | denied | decided fresh | — | ● |
| 3052 | Sign the release attestation with the developer's own runner identity | SF-SS-001 SF-CR-004 ⛔ | denied | refused at the floor | — |  |
| 3053 | Replace the pickle payload with a schema-validated JSON body | SF-AS-002 | permitted | decided fresh | — |  |
| 3054 | Parameterise the supplier portal's lot-search query | SF-AS-002 | permitted | decided fresh | — |  |
| 3055 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 3056 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 3057 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 3058 | Attach an agent provenance attestation to the generated migration | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3059 | Reuse the warm build runner to cut pipeline time in half | SF-SS-006 | denied | decided fresh | — |  |
| 3060 | Authenticate the time source for every piece of fab equipment | SF-OT-002 | permitted with conditions | decided fresh | — | ● |
| 3061 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted | decided fresh | — |  |
| 3062 | Lower the export-screening strictness in the policy repository | SF-EX-010 | denied | decided fresh | — |  |
| 3063 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-001 SF-RP-003 ⛔ | denied | refused at the floor | — |  |
| 3064 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 3065 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 3066 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted | decided fresh | — |  |
| 3067 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-003 | permitted | decided fresh | — |  |
| 3068 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-002 | permitted | decided fresh | — |  |
| 3069 | Add secret scanning to the pre-merge pipeline | SF-SS-005 | permitted | disposed by citation | — |  |
| 3070 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-002 SF-CR-006 ⛔ | denied | refused at the floor | — |  |
| 3071 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-002 ⛔ | permitted | decided fresh | — |  |
| 3072 | Route Kumamoto tool logs to the in-region log sink | SF-DS-002 ⛔ | permitted | decided fresh | — |  |
| 3073 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3074 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 3075 | Declare the latency budget for the changed metrology path | SF-RT-003 | permitted | decided fresh | — |  |
| 3076 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 3077 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-007 | permitted | decided fresh | — |  |
| 3078 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-007 | permitted | decided fresh | — |  |
| 3079 | Separate the reporter bulletin from the adjudication input path | SF-GV-007 | permitted | decided fresh | — |  |
| 3080 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-003 | permitted | decided fresh | — |  |
| 3081 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 3082 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3083 | Log the deemed-export check that runs at repository role grant | SF-EX-008 | permitted | decided fresh | — |  |
| 3084 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 3085 | Tag every WIP record with the jurisdiction that produced it | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 3086 | Canonicalise the upload path before the handler opens the file | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3087 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 3088 | Rotate the recipe vault envelope key on the published schedule | SF-RP-003 | denied | bound by precedent | REC-S0116 |  |
| 3089 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-001 | permitted | decided fresh | — |  |
| 3090 | Widen the data residency provision to permit group-A replicas | SF-SG-004 | denied | decided fresh | — |  |
| 3091 | Pull tool firmware updates from an unverified community mirror | SF-OT-001 | denied | decided fresh | — |  |
| 3092 | Let the adjudication service tune its own charging threshold | SF-GV-002 SF-AG-005 ⛔ | denied | refused at the floor | — |  |
| 3093 | Parameterise the supplier portal's lot-search query | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3094 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 3095 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-004 SF-GV-004 ⛔ | denied | refused at the floor | — |  |
| 3096 | Log the deemed-export check that runs at repository role grant | SF-EX-003 ⛔ | permitted | decided fresh | — |  |
| 3097 | Require the licence exception paragraph on the shipment record | SF-EX-003 ⛔ | permitted | decided fresh | — |  |
| 3098 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 3099 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted | decided fresh | — |  |
| 3100 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — | ● |
| 3101 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3102 | Move the charging threshold for the supply chain family | SF-EH-004 | denied | decided fresh | — |  |
| 3103 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | permitted | decided fresh | — |  |
| 3104 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted | decided fresh | — |  |
| 3105 | Add an append-only constraint to the lot genealogy table | SF-WI-005 | permitted | decided fresh | — |  |
| 3106 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | decided fresh | — |  |
| 3107 | Route every boycott-request match to the quarterly filing queue | SF-SO-003 | permitted | decided fresh | — |  |
| 3108 | Add the pilot line to the CUI boundary documentation | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 3109 | Capture the licence determination rationale in the trade record | SF-EX-008 | permitted | decided fresh after a tie | none_tie |  |
| 3110 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 3111 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | decided fresh | — |  |
| 3112 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | permitted | disposed by citation | — |  |
| 3113 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3114 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 3115 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 3116 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 3117 | Require a human sign-off before an agent edits equipment control code | SF-AG-003 | permitted | decided fresh | — |  |
| 3118 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-003 | permitted | decided fresh | — |  |
| 3119 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted | decided fresh | — | ● |
| 3120 | Record the outbound-investment determination before a joint-venture data share opens | SF-SO-003 | permitted | decided fresh | — | ● |
| 3121 | Add a configuration flag that releases blocked-property holds for expedited orders | SF-SO-002 SF-GV-004 ⛔ | denied | refused at the floor | — |  |
| 3122 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3123 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 3124 | Add the new data flow to the system security plan diagram | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 3125 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 3126 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 3127 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 3128 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | decided fresh | — |  |
| 3129 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted | decided fresh | — |  |
| 3130 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | decided fresh | — |  |
| 3131 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | decided fresh | — |  |
| 3132 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3133 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 3134 | Surface unparsed equipment replies instead of dropping them | SF-SG-008 | permitted | decided fresh | — |  |
| 3135 | Switch the ingest service to the throughput collector | SF-RT-007 | denied | decided fresh | — |  |
| 3136 | Parallelise the SECS message dispatcher across four workers | SF-SG-002 ⛔ | denied | refused at the floor | — |  |
| 3137 | Attach qualification evidence to every process-change record | SF-QS-001 | permitted | decided fresh | — |  |
| 3138 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 3139 | Bind the mask revision to its lot and recipe record | SF-QS-004 | permitted | decided fresh | — |  |
| 3140 | Edit the deny predicate for the deemed-export provision | SF-DS-006 | denied | decided fresh | — |  |
| 3141 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted | decided fresh | — |  |
| 3142 | Require named-owner approval per vendor remote session | SF-OT-003 | permitted | decided fresh | — |  |
| 3143 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-003 | permitted | decided fresh | — |  |
| 3144 | Drop the deprecated cipher suites from the supplier portal | SF-CR-004 | permitted | decided fresh | — |  |
| 3145 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 3146 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 3147 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3148 | Record the control inheritance for the shared platform tier | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 3149 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-006 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 3150 | Verify every package the agent imported against the registry | SF-AG-007 | permitted | decided fresh | — |  |
| 3151 | Exclude recipe bodies from the vendor support bundle | SF-RP-005 | permitted | decided fresh | — | ● |
| 3152 | Screen every counterparty against the SDN and consolidated lists including fifty-percent-owned entities | SF-SO-003 | permitted | decided fresh | — |  |
| 3153 | Document the sub-processor chain for the supplier portal CDN | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 3154 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-004 | permitted | decided fresh | — |  |
| 3155 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | decided fresh | — |  |
| 3156 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 3157 | Add the CHIPS notification duty to the compliance rulebook | SF-SS-004 | denied | decided fresh | — |  |
| 3158 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | decided fresh | — |  |
| 3159 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh | — |  |
| 3160 | Retire the superseded cryptographic floor from the constitution | SF-EH-004 | denied | decided fresh | — |  |
| 3161 | Install tool firmware without verifying the vendor signature | SF-OT-001 | denied | decided fresh | — |  |
| 3162 | Record the builder identity in the release attestation | SF-SS-007 | permitted | disposed by citation | — |  |
| 3163 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 3164 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 3165 | Verify component digests against the registry before deploy | SF-SS-011 | permitted | decided fresh | — |  |
| 3166 | Document the sub-processor chain for the supplier portal CDN | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 3167 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-004 | permitted | decided fresh | — |  |
| 3168 | Collect smelter-and-refiner identity data during supplier onboarding | SF-RS-004 | permitted | decided fresh | — |  |
| 3169 | Pin the JVM collector so pause times stay inside the budget | SF-RT-005 | permitted | decided fresh | — |  |
| 3170 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3171 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | decided fresh | — | ● |
| 3172 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3173 | Keep audit logging on during the throughput optimisation | SF-WI-007 | permitted | decided fresh | — |  |
| 3174 | Keep audit logging on during the throughput optimisation | SF-WI-007 | permitted | decided fresh | — |  |
| 3175 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3176 | Re-enable the legacy cipher suite so the older scanner can connect | SF-CR-003 | denied | decided fresh | — |  |
| 3177 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 3178 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3179 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-012 | denied | decided fresh | — |  |
| 3180 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-005 | permitted | decided fresh | — |  |
| 3181 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted | decided fresh | — |  |
| 3182 | Skip the non-production staging step for a firmware rollout across the fleet | SF-OT-004 | denied | decided fresh | — | ● |
| 3183 | Derive a fresh nonce per recipe encryption operation | SF-CR-004 | permitted | decided fresh | — |  |
| 3184 | Purge sanctions screening records on the general ninety-day log rotation | SF-SO-003 | denied | decided fresh | — |  |
| 3185 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-005 | permitted | decided fresh | — |  |
| 3186 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-001 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 3187 | Separate the reporter bulletin from the adjudication input path | SF-GV-004 | permitted | decided fresh | — |  |
| 3188 | Shorten the WIP record retention term in the rulebook | SF-EX-012 | denied | decided fresh | — |  |
| 3189 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 3190 | Resolve the foreign access request through the named legal channel | SF-DS-006 | permitted | decided fresh | — |  |
| 3191 | Narrow the recipe-protection provision to production recipes only | SF-CR-003 | denied | decided fresh | — |  |
| 3192 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3193 | Hash the recipe identifier before it reaches the analytics store | SF-RP-003 | permitted | decided fresh | — |  |
| 3194 | Report load conditions alongside the p99.9 measurement | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 3195 | Add an authorisation check to the lot-detail API | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3196 | Call the licence service synchronously from the tool event handler | SF-RT-006 | denied | decided fresh | — | ● |
| 3197 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 3198 | Scope the internal SECS parser package to the private registry | SF-SS-003 | permitted | disposed by citation | — |  |
| 3199 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | decided fresh | — |  |
| 3200 | Replicate the Dresden yield warehouse into the US analytics cluster | SF-DS-001 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 3201 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-001 ⛔ | denied | refused at the floor | — |  |
| 3202 | Record and time-box every vendor remote-access session | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 3203 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | decided fresh | — |  |
| 3204 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-007 | permitted | decided fresh | — |  |
| 3205 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted | decided fresh | — | ● |
| 3206 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-005 | permitted | decided fresh | — |  |
| 3207 | Link the agent's change to the originating engineering ticket | SF-AG-005 | permitted | decided fresh | — |  |
| 3208 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 3209 | Hash the recipe identifier before it reaches the analytics store | SF-RP-007 | permitted | decided fresh | — |  |
| 3210 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted | decided fresh | — |  |
| 3211 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-012 | permitted | decided fresh | — | ● |
| 3212 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted | decided fresh | — |  |
| 3213 | Auto-merge agent pull requests that pass the build | SF-AG-005 | denied | decided fresh | — |  |
| 3214 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-001 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 3215 | Refresh the control assessment for the changed audit path | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 3216 | Keep the appeal route on the automated screening decision | SF-GV-003 | permitted | decided fresh | — |  |
| 3217 | Publish the standing declaration in the compliance export | SF-GV-003 | permitted | decided fresh | — |  |
| 3218 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 3219 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 3220 | Link the agent's change to the originating engineering ticket | SF-AG-007 | permitted | decided fresh | — |  |
| 3221 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3222 | Switch off forced-labour screening for tier-two suppliers to speed onboarding | SF-RS-002 SF-RS-004 ⛔ | denied | refused at the floor | — |  |
| 3223 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh after a tie | none_tie |  |
| 3224 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | disposed by citation | — |  |
| 3225 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — | ● |
| 3226 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted with conditions | decided fresh | — | ● |
| 3227 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-002 SF-EH-004 ⛔ | denied | refused at the floor | — |  |
| 3228 | Amend the consolidation class threshold in the parameters file | SF-IT-004 | denied | decided fresh | — |  |
| 3229 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | disposed by citation | — |  |
| 3230 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-002 | permitted | decided fresh | — | ● |
| 3231 | Pin the certificate chain used by the metrology ingest client | SF-CR-005 | permitted | decided fresh | — |  |
| 3232 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 3233 | Make export decisions append-only in the trade compliance ledger | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 3234 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 3235 | Declare the latency budget for the changed metrology path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3236 | Retire the superseded cryptographic floor from the constitution | SF-RP-004 | denied | decided fresh | — |  |
| 3237 | Default the process-change classification to minor when the field is left blank | SF-QS-003 | denied | decided fresh | — | ● |
| 3238 | Resolve the foreign access request through the named legal channel | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 3239 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted | decided fresh | — | ● |
| 3240 | Attach an agent provenance attestation to the generated migration | SF-AG-005 | permitted | decided fresh | — |  |
| 3241 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-005 | permitted | decided fresh | — |  |
| 3242 | Add a config flag that disables the destination geofence for demos | SF-EX-001 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 3243 | Sign the container image published for the edge tool gateway | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 3244 | Add the CHIPS notification duty to the compliance rulebook | SF-SS-007 | denied | decided fresh | — |  |
| 3245 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-004 | permitted with conditions | decided fresh | — | ● |
| 3246 | Let the adjudication service tune its own charging threshold | SF-GV-005 | denied | decided fresh | — |  |
| 3247 | Lower the export-screening strictness in the policy repository | SF-SG-005 | denied | decided fresh | — |  |
| 3248 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-004 | permitted | decided fresh | — |  |
| 3249 | Scope recipe vault reads to the owning process integration team | SF-RP-006 | permitted | decided fresh | — |  |
| 3250 | Bound the SECS message queue depth per tool connection | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3251 | Add a licence-exception clause to the trade compliance rulebook | SF-DS-006 | denied | decided fresh | — |  |
| 3252 | Sign the container image published for the edge tool gateway | SF-SS-010 | permitted | decided fresh | — |  |
| 3253 | Record the builder identity in the release attestation | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 3254 | Record the builder identity in the release attestation | SF-SS-011 | permitted | disposed by citation | — |  |
| 3255 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 3256 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted | decided fresh | — |  |
| 3257 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 3258 | Record the percentile family used for the declared budget | SF-RT-002 | permitted with conditions | decided fresh | — | ● |
| 3259 | Batch alarm reports into the five-second telemetry flush | SF-SG-001 ⛔ | denied | refused at the floor | — |  |
| 3260 | Exclude audit findings from the retrieval query | SF-GV-004 | permitted | decided fresh | — | ● |
| 3261 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 3262 | Record the builder identity in the release attestation | SF-SS-007 | permitted | decided fresh | — |  |
| 3263 | Move the defence-enclave backup into the general-purpose cloud region for cheaper storage | SF-IT-003 SF-SS-005 ⛔ | denied | refused at the floor | — |  |
| 3264 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 3265 | Add a stress test that runs the broker under concurrent tool load | — | permitted | docketed — nothing engaged | — |  |
| 3266 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 3267 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted | decided fresh | — |  |
| 3268 | Allowlist the export format instead of shelling out with user input | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3269 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 3270 | Raise the tool-gateway TLS floor to the declared version | SF-CR-004 | permitted | decided fresh | — |  |
| 3271 | Swap the hand-rolled MAC for the library primitive | SF-CR-004 | permitted | decided fresh | — |  |
| 3272 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 3273 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 3274 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | permitted | decided fresh | — |  |
| 3275 | Switch the ingest service to the throughput collector | SF-RT-006 | denied | decided fresh | — |  |
| 3276 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 3277 | Add the covered-transaction determination field to the tool purchase record | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 3278 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — | ● |
| 3279 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-006 | permitted | decided fresh | — |  |
| 3280 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | disposed by citation | — |  |
| 3281 | Publish the measurement window with the latency result | SF-RT-005 | permitted | decided fresh | — |  |
| 3282 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | permitted | decided fresh | — |  |
| 3283 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted | decided fresh | — | ● |
| 3284 | Add secret scanning to the pre-merge pipeline | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 3285 | Add the newly pulled component to the generated SBOM | SF-SS-003 | permitted | disposed by citation | — |  |
| 3286 | Add secret scanning to the pre-merge pipeline | SF-SS-010 | permitted | decided fresh | — |  |
| 3287 | Pin the denied-party list snapshot used by a screening decision | SF-EX-007 | permitted | decided fresh | — |  |
| 3288 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 3289 | Replace the pickle payload with a schema-validated JSON body | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3290 | Lower a gas-detector alarm threshold after a failed calibration, with EHS signoff recorded same day | SF-EH-004 | permitted | decided fresh | — |  |
| 3291 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3292 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | disposed by citation | — |  |
| 3293 | Replace the pickle payload with a schema-validated JSON body | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 3294 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 3295 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-007 | permitted | decided fresh | — |  |
| 3296 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 3297 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 3298 | Let the MES correct yesterday's WIP status in place | SF-WI-003 | denied | decided fresh | — |  |
| 3299 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 3300 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 3301 | Scope the internal SECS parser package to the private registry | SF-SS-006 | permitted | decided fresh | — |  |
| 3302 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-004 | permitted | decided fresh | — |  |
| 3303 | Wire a rollback path into every controller-model promotion | SF-QS-003 | permitted with conditions | decided fresh | — | ● |
| 3304 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 3305 | Move the charging threshold into the constitutional parameters file | SF-GV-005 | permitted | decided fresh | — |  |
| 3306 | Record the exception authority against the accepting principal | SF-GV-005 | permitted | decided fresh | — |  |
| 3307 | Return a correlation id instead of a stack trace to the client | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3308 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted | decided fresh | — |  |
| 3309 | Drop the recipient identity field from the export record to speed up the batch job | SF-IT-004 | denied | decided fresh | — |  |
| 3310 | Add the realised adverse-contest rate to the governance export | SF-GV-004 | permitted | decided fresh | — |  |
| 3311 | Verify every package the agent imported against the registry | SF-AG-003 | permitted | decided fresh | — |  |
| 3312 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | decided fresh | — |  |
| 3313 | Deliver alarm reports ahead of the collection-event budget | SF-SG-007 | permitted | decided fresh | — |  |
| 3314 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | decided fresh | — |  |
| 3315 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | decided fresh | — |  |
| 3316 | Strip process parameters from telemetry metric labels | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 3317 | Report load conditions alongside the p99.9 measurement | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 3318 | Route a sanctions list match to a named human reviewer for disposition | SF-SO-003 | permitted with conditions | decided fresh | — | ● |
| 3319 | Add fuzz coverage for the metrology file upload handler | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3320 | Assert the safety interlock signal survives the gateway refactor | SF-SG-003 | permitted | decided fresh | — |  |
| 3321 | Drop the smelter-and-refiner questionnaire from the supplier onboarding flow | SF-RS-001 | denied | decided fresh | — |  |
| 3322 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3323 | Take the minor version bump that pulls in the critical archive CVE | SF-SS-003 | denied | decided fresh | — | ● |
| 3324 | Replace the pickle payload with a schema-validated JSON body | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3325 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 3326 | Release the broker-sourced lot from quarantine before the provenance chain is verified | SF-RS-003 | denied | decided fresh | — |  |
| 3327 | Record the ECCN determination alongside the design-file upload | SF-EX-008 | permitted | decided fresh | — |  |
| 3328 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted | decided fresh | — |  |
| 3329 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 3330 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | decided fresh | — |  |
| 3331 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — |  |
| 3332 | Propose a new provision covering advanced-node lithography data | SF-RS-001 | denied | decided fresh | — |  |
| 3333 | Wire a host command that can override the lockout/tagout state from the MES | SF-EH-002 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 3334 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 3335 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | decided fresh | — |  |
| 3336 | Pin the JVM collector so pause times stay inside the budget | SF-RT-003 | permitted | decided fresh | — |  |
| 3337 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 3338 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 3339 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-003 | denied | decided fresh | — |  |
| 3340 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 3341 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 3342 | Retire the superseded cryptographic floor from the constitution | SF-GV-003 | denied | decided fresh | — |  |
| 3343 | Quarantine agent changes that touch the export enforcement path | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 3344 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3345 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 3346 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — | ● |
| 3347 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | decided fresh | — |  |
| 3348 | Add a config flag that disables the destination geofence for demos | SF-EX-003 SF-SG-010 ⛔ | denied | refused at the floor | — |  |
| 3349 | Keep the appeal route on the automated screening decision | SF-GV-004 | permitted | decided fresh | — |  |
| 3350 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-001 | denied | decided fresh | — |  |
| 3351 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3352 | Verify every package the agent imported against the registry | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3353 | Let the defence-article transfer proceed without naming a licence or exemption paragraph | SF-IT-002 | denied | decided fresh | — | ● |
| 3354 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-003 | permitted | decided fresh | — |  |
| 3355 | Link the agent's change to the originating engineering ticket | SF-AG-003 | permitted | decided fresh | — |  |
| 3356 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3357 | Verify tool firmware signatures against the vendor key before install | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 3358 | Purge recipe execution records older than ninety days | SF-WI-001 SF-CR-005 ⛔ | denied | refused at the floor | — |  |
| 3359 | Add secret scanning to the pre-merge pipeline | SF-SS-010 | permitted | disposed by citation | — |  |
| 3360 | Force the etcher to offline control state during the gateway deploy | SF-SG-005 | denied | decided fresh | — |  |
| 3361 | Join the audit findings table into the precedent retrieval query | SF-GV-002 SF-EH-004 ⛔ | denied | refused at the floor | — |  |
| 3362 | Allowlist the export format instead of shelling out with user input | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3363 | Assert the safety interlock signal survives the gateway refactor | SF-SG-008 | permitted with conditions | decided fresh | — | ● |
| 3364 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-002 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 3365 | Sign the release attestation with the developer's own runner identity | SF-SS-008 | denied | decided fresh | — |  |
| 3366 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3367 | Attribute every metrology record amendment to a named operator | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 3368 | Let the coding agent refactor the screening gate's decision logic | SF-AG-006 | denied | decided fresh | — |  |
| 3369 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 3370 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-002 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 3371 | Sign the container image published for the edge tool gateway | SF-SS-010 | permitted | decided fresh | — |  |
| 3372 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | decided fresh | — |  |
| 3373 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 3374 | Strip process parameters from telemetry metric labels | SF-RP-006 | permitted | decided fresh | — |  |
| 3375 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted | decided fresh | — |  |
| 3376 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 3377 | Keep audit logging on during the throughput optimisation | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 3378 | Add an authorisation check to the lot-detail API | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3379 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-010 | permitted | decided fresh | — |  |
| 3380 | Make export decisions append-only in the trade compliance ledger | SF-EX-010 | permitted | decided fresh | — |  |
| 3381 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh after a tie | none_tie |  |
| 3382 | Alert the named EHS owner when the emissions-reporting job fails | SF-EH-004 | permitted | decided fresh | — |  |
| 3383 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted | decided fresh | — |  |
| 3384 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted | disposed by citation | — |  |
| 3385 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3386 | Fix the deadlock between the alarm writer and the snapshot reader | — | permitted | docketed — nothing engaged | — |  |
| 3387 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3388 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 3389 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 3390 | Replace the pickle payload with a schema-validated JSON body | SF-AS-002 | permitted | decided fresh | — |  |
| 3391 | Delete the held lot's genealogy during the archive cleanup | SF-WI-002 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 3392 | Disable the fifty-percent ownership rule in the sanctions screening query | SF-SO-001 SF-GV-005 ⛔ | denied | refused at the floor | — |  |
| 3393 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted | disposed by citation | — |  |
| 3394 | Add the newly pulled component to the generated SBOM | SF-SS-006 | permitted with conditions | decided fresh | — | ● |
| 3395 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 3396 | Bound the request body size on the yield analytics endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3397 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | decided fresh | — | ● |
| 3398 | Raise the tool-gateway TLS floor to the declared version | SF-CR-003 | permitted | decided fresh | — |  |
| 3399 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-008 | permitted | decided fresh | — |  |
| 3400 | Report load conditions alongside the p99.9 measurement | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 3401 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 3402 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-001 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 3403 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | decided fresh | — |  |
| 3404 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | permitted | decided fresh | — |  |
| 3405 | Version collection-event identifiers instead of renumbering them | SF-SG-008 | permitted | decided fresh | — |  |
| 3406 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh | — |  |
| 3407 | Pin the denied-party list snapshot used by a screening decision | SF-EX-007 | permitted | decided fresh | — |  |
| 3408 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted | disposed by citation | — |  |
| 3409 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 3410 | Pin the denied-party list snapshot used by a screening decision | SF-EX-013 | permitted | decided fresh | — |  |
| 3411 | Overwrite the supplier declaration record in place instead of versioning it | SF-RS-004 | denied | decided fresh | — |  |
| 3412 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-001 SF-SG-006 ⛔ | denied | refused at the floor | — |  |
| 3413 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-003 SF-RP-003 ⛔ | denied | refused at the floor | — |  |
| 3414 | Refresh the control assessment for the changed audit path | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 3415 | Report load conditions alongside the p99.9 measurement | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 3416 | Narrow the recipe-protection provision to production recipes only | SF-OT-002 | denied | decided fresh | — |  |
| 3417 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | permitted | decided fresh | — |  |
| 3418 | Round emissions report values down to the nearest permit-limit increment | SF-EH-003 SF-QS-001 ⛔ | denied | refused at the floor | — |  |
| 3419 | Parameterise the supplier portal's lot-search query | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3420 | Map the new component to its NIST control identifier | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 3421 | Add the AGPL trace decoder to the customer-deployed tool gateway | SF-SS-003 | denied | decided fresh | — | ● |
| 3422 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-005 | denied | decided fresh | — |  |
| 3423 | Drop the standing declaration from the governance export payload | SF-GV-002 ⛔ | denied | refused at the floor | — |  |
| 3424 | Record the control inheritance for the shared platform tier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 3425 | Make the audit register append-only and disjoint from the store | SF-GV-007 | permitted | decided fresh | — |  |
| 3426 | Separate the reporter bulletin from the adjudication input path | SF-GV-007 | permitted | decided fresh | — |  |
| 3427 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3428 | Remove the protocol allowlist at the zone boundary to unblock a legacy tool | SF-OT-004 | denied | decided fresh | — |  |
| 3429 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 3430 | Quarantine a broker-sourced lot pending provenance verification | SF-RS-003 | permitted | decided fresh | — |  |
| 3431 | Retain the conflict-minerals inquiry response on the component record | SF-RS-003 | permitted | decided fresh | — |  |
| 3432 | Deliver alarm reports ahead of the collection-event budget | SF-SG-005 | permitted | decided fresh | — |  |
| 3433 | Fail closed on receipt when a forced-labour list match is returned | SF-RS-003 | permitted | decided fresh | — |  |
| 3434 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | decided fresh | — |  |
| 3435 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 3436 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-003 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3437 | Fall back to plain TCP when the tool refuses the TLS handshake | SF-RP-003 | denied | decided fresh | — |  |
| 3438 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3439 | Serialise the two writers to the yield aggregation table | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3440 | Validate the ECCN parameter against the enumerated set | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 3441 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted | decided fresh | — |  |
| 3442 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted | decided fresh | — |  |
| 3443 | Build the lot-search query by concatenating the filter string | SF-AS-003 | denied | decided fresh | — |  |
| 3444 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | decided fresh | — |  |
| 3445 | Call the licence service synchronously from the tool event handler | SF-RT-004 | denied | decided fresh | — |  |
| 3446 | Drop the recipient identity field from the export record to speed up the batch job | SF-IT-001 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 3447 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | permitted | decided fresh | — |  |
| 3448 | Purge recipe execution records older than ninety days | SF-WI-001 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 3449 | Rate-limit the supplier portal's document download endpoint | — | permitted | docketed — nothing engaged | — |  |
| 3450 | Document the CUI boundary for the metrology ingest service | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 3451 | Monitor and alarm on clock drift across the tool network | SF-OT-003 | permitted | decided fresh | — |  |
| 3452 | Move recipe transfer onto the mutually authenticated channel | SF-RP-003 | permitted | decided fresh | — | ● |
| 3453 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3454 | Roll the crypto library back to the version the build used to pin | SF-SS-001 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 3455 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-007 | permitted | decided fresh | — |  |
| 3456 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-007 | permitted | decided fresh | — |  |
| 3457 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-006 | permitted | decided fresh | — |  |
| 3458 | Add the new data flow to the system security plan diagram | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 3459 | Make the screening gate's denial final with no review route | SF-GV-004 | denied | decided fresh | — |  |
| 3460 | Raise the latency budget stated in the constitutional parameters | SF-OT-002 | denied | decided fresh | — |  |
| 3461 | Retry S2F41 remote commands without reordering the queue | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 3462 | Let the coding agent rewrite the tool command dispatcher | SF-AG-004 | denied | decided fresh | — |  |
| 3463 | Add an unauthenticated time server to the tool network for a quick fix | SF-OT-002 | denied | decided fresh | — |  |
| 3464 | Link each claimed control to its implementation statement | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 3465 | Add a GEM control-state transition test for the Lam etcher | SF-SG-007 | permitted | decided fresh | — |  |
| 3466 | Swallow equipment replies the parser does not recognise | SF-SG-002 SF-SS-010 ⛔ | denied | refused at the floor | — |  |
| 3467 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 3468 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-003 | permitted | decided fresh | — |  |
| 3469 | Link the agent's change to the originating engineering ticket | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 3470 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | decided fresh | — |  |
| 3471 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | decided fresh | — |  |
| 3472 | Let the batch corrector amend metrology rows without a named operator | SF-WI-001 SF-AS-003 ⛔ | denied | refused at the floor | — |  |
| 3473 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3474 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-013 | denied | decided fresh | — |  |
| 3475 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 3476 | Resolve the foreign access request through the named legal channel | SF-DS-003 | permitted | decided fresh | — |  |
| 3477 | Deliver alarm reports ahead of the collection-event budget | SF-SG-006 | permitted | decided fresh | — | ● |
| 3478 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-004 | permitted | decided fresh | — |  |
| 3479 | Separate the reporter bulletin from the adjudication input path | SF-GV-003 | permitted | decided fresh | — |  |
| 3480 | Make the audit register append-only and disjoint from the store | SF-GV-003 | permitted | decided fresh | — |  |
| 3481 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-005 | permitted | decided fresh | — |  |
| 3482 | Deliver alarm reports ahead of the collection-event budget | SF-SG-005 | permitted | decided fresh | — |  |
| 3483 | Replicate the Dresden yield warehouse into the US analytics cluster | SF-DS-003 | denied | decided fresh | — |  |
| 3484 | Run each build job on a fresh ephemeral runner | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 3485 | Assert the safety interlock signal survives the gateway refactor | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 3486 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-003 | denied | decided fresh | — |  |
| 3487 | Replace the direct-URL dependency with a registry release | SF-SS-004 | permitted | decided fresh | — |  |
| 3488 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-001 SF-AG-005 ⛔ | denied | refused at the floor | — |  |
| 3489 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | decided fresh | — | ● |
| 3490 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | disposed by citation | — |  |
| 3491 | Document the CUI boundary for the metrology ingest service | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3492 | Add the new data flow to the system security plan diagram | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3493 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-007 | permitted | decided fresh | — |  |
| 3494 | Strip process parameters from telemetry metric labels | SF-RP-003 | permitted | decided fresh | — |  |
| 3495 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | decided fresh | — | ● |
| 3496 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | permitted | decided fresh | — |  |
| 3497 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted | decided fresh | — |  |
| 3498 | Rotate the recipe vault signing key on the published schedule | SF-CR-005 | permitted | decided fresh | — |  |
| 3499 | Document the sub-processor chain for the supplier portal CDN | SF-DS-003 | permitted | decided fresh | — |  |
| 3500 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-002 | permitted | decided fresh | — |  |
| 3501 | Gate the important-data export on the completed security assessment | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 3502 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 3503 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3504 | Retry S2F41 remote commands without reordering the queue | SF-SG-006 | permitted | decided fresh | — |  |
| 3505 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 3506 | Exclude audit findings from the retrieval query | SF-GV-006 | permitted | decided fresh | — |  |
| 3507 | Keep the appeal route on the automated screening decision | SF-GV-006 | permitted | decided fresh | — |  |
| 3508 | Allow TLS 1.0 on the tool gateway for the Kumamoto equipment | SF-CR-001 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 3509 | Document the CUI boundary for the metrology ingest service | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3510 | Shell out to the converter with the supplier's filename | SF-AS-003 | denied | decided fresh | — |  |
| 3511 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted | decided fresh | — |  |
| 3512 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-004 | permitted | decided fresh | — |  |
| 3513 | Version the supplier declaration record on every effective-date change | SF-RS-004 | permitted | decided fresh | — |  |
| 3514 | Treat a signature verification error as a warning during rollout | SF-CR-002 | denied | decided fresh | — |  |
| 3515 | Shorten the WIP record retention term in the rulebook | SF-AS-003 | denied | decided fresh | — |  |
| 3516 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-002 | permitted | decided fresh | — |  |
| 3517 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 3518 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted | decided fresh | — |  |
| 3519 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | decided fresh | — | ● |
| 3520 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-007 | permitted | decided fresh | — |  |
| 3521 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-006 SF-EX-008 ⛔ | denied | refused at the floor | — |  |
| 3522 | Remove the human-review requirement from the screening provision | SF-RS-001 | denied | decided fresh | — |  |
| 3523 | Order the two mutex acquisitions consistently across both paths | SF-TQ-004 | permitted | decided fresh | — |  |
| 3524 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | decided fresh | — |  |
| 3525 | Declare the latency budget for the changed metrology path | SF-RT-001 | permitted | decided fresh after a tie | none_tie |  |
| 3526 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | decided fresh | — | ● |
| 3527 | Round emissions report values down to the nearest permit-limit increment | SF-EH-002 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 3528 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-006 | denied | decided fresh | — |  |
| 3529 | Scope the internal SECS parser package to the private registry | SF-SS-006 | permitted | decided fresh after a tie | none_tie |  |
| 3530 | Rotate the recipe vault envelope key on the published schedule | SF-RP-006 | permitted | decided fresh | — |  |
| 3531 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-004 | permitted | decided fresh | — |  |
| 3532 | Name the licence-exception paragraph on every ITAR transfer record | SF-IT-004 | permitted | decided fresh | — |  |
| 3533 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-001 SF-EX-009 ⛔ | denied | refused at the floor | — |  |
| 3534 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-001 ⛔ | denied | refused at the floor | — |  |
| 3535 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-002 | denied | decided fresh | — |  |
| 3536 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted | decided fresh | — |  |
| 3537 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3538 | Record the builder identity in the release attestation | SF-SS-003 | permitted | decided fresh | — |  |
| 3539 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted | disposed by citation | — |  |
| 3540 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 3541 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-001 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 3542 | Bind the mask revision to its lot and recipe record | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 3543 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 3544 | Attribute every metrology record amendment to a named operator | SF-WI-004 | permitted | decided fresh | — |  |
| 3545 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | decided fresh | — |  |
| 3546 | Publish the tool-gateway release from an unattested local build | SF-SS-002 | denied | decided fresh | — |  |
| 3547 | Rotate the recipe vault envelope key on the published schedule | SF-RP-005 | permitted | decided fresh | — |  |
| 3548 | Propose a new provision covering advanced-node lithography data | SF-AS-003 | denied | decided fresh | — |  |
| 3549 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 3550 | Move recipe transfer onto the mutually authenticated channel | SF-RP-006 | permitted | decided fresh | — |  |
| 3551 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-004 | denied | decided fresh | — |  |
| 3552 | Capture customer acknowledgement on the change notice before release | SF-QS-002 | permitted | decided fresh | — | ● |
| 3553 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-002 | permitted | decided fresh | — |  |
| 3554 | Parameterise the supplier portal's lot-search query | SF-AS-002 | permitted | decided fresh | — |  |
| 3555 | Allowlist the export format instead of shelling out with user input | SF-AS-002 | permitted | decided fresh | — |  |
| 3556 | Commit the tool vendor's API key into the gateway config | SF-SS-011 | denied | decided fresh | — |  |
| 3557 | Move the alarm-fanout write off the monitoring hot path | SF-RT-002 | permitted | decided fresh | — |  |
| 3558 | Record the percentile family used for the declared budget | SF-RT-002 | permitted | decided fresh | — |  |
| 3559 | Route every screening near-miss to a named compliance reviewer | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 3560 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | decided fresh | — |  |
| 3561 | Retry S2F41 remote commands without reordering the queue | SF-SG-010 | permitted | decided fresh | — |  |
| 3562 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-005 | permitted | decided fresh | — |  |
| 3563 | Raise the tool-gateway TLS floor to the declared version | SF-CR-004 | permitted | decided fresh | — |  |
| 3564 | Bind the mask revision to its lot and recipe record | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 3565 | Add a config flag that disables the destination geofence for demos | SF-EX-002 SF-DS-004 ⛔ | denied | refused at the floor | — |  |
| 3566 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 3567 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 3568 | Edit the deny predicate for the deemed-export provision | SF-AG-004 | denied | decided fresh | — |  |
| 3569 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted | decided fresh | — |  |
| 3570 | Require the licence exception paragraph on the shipment record | SF-EX-009 | permitted | decided fresh | — |  |
| 3571 | Encrypt the recipe payload at rest in the vault | SF-RP-004 | permitted | decided fresh | — | ● |
| 3572 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | decided fresh | — |  |
| 3573 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 3574 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 3575 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3576 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 3577 | Add the CHIPS notification duty to the compliance rulebook | SF-OT-002 | denied | decided fresh | — |  |
| 3578 | Swallow equipment replies the parser does not recognise | SF-SG-007 | denied | decided fresh | — |  |
| 3579 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 3580 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted | decided fresh | — |  |
| 3581 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | disposed by citation | — |  |
| 3582 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted | decided fresh | — |  |
| 3583 | Add secret scanning to the pre-merge pipeline | SF-SS-002 | permitted | decided fresh | — |  |
| 3584 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3585 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 3586 | Bound the collector's allocation rate on the ingest path | SF-RT-006 | permitted | decided fresh | — |  |
| 3587 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | decided fresh | — |  |
| 3588 | Move the defence-enclave backup into the general-purpose cloud region for cheaper storage | SF-IT-003 SF-SG-004 ⛔ | denied | refused at the floor | — |  |
| 3589 | Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 3590 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-002 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 3591 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 3592 | Purge recipe execution records older than ninety days | SF-WI-002 SF-AS-003 ⛔ | denied | refused at the floor | — |  |
| 3593 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 3594 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-005 | permitted | decided fresh | — |  |
| 3595 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3596 | Close the check-then-open window in the metrology file handler | SF-TQ-003 | permitted | decided fresh | — |  |
| 3597 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — |  |
| 3598 | Canonicalise the upload path before the handler opens the file | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3599 | Write our own MAC so the vault avoids the library dependency | SF-CR-004 | denied | decided fresh | — | ● |
| 3600 | Rate-limit the supplier portal's document download endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3601 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — |  |
| 3602 | Verify tool firmware signatures against the vendor key before install | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 3603 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 3604 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-005 | permitted | decided fresh | — |  |
| 3605 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3606 | Make export decisions append-only in the trade compliance ledger | SF-EX-008 | permitted | decided fresh | — |  |
| 3607 | Fail the pipeline closed when the screening service times out | SF-EX-008 | permitted | decided fresh | — |  |
| 3608 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-008 | denied | decided fresh | — |  |
| 3609 | Record firmware provenance on the equipment record at update time | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 3610 | Route every boycott-request match to the quarterly filing queue | SF-SO-003 | permitted | decided fresh | — |  |
| 3611 | Drop the recipient identity field from the export record to speed up the batch job | SF-IT-001 SF-WI-005 ⛔ | denied | refused at the floor | — |  |
| 3612 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-001 | denied | decided fresh | — |  |
| 3613 | Treat a signature verification error as a warning during rollout | SF-CR-001 SF-SS-006 ⛔ | denied | refused at the floor | — |  |
| 3614 | Pin the JVM collector so pause times stay inside the budget | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 3615 | Ship the in-country support tunnel with the access question still open | SF-DS-002 SF-SS-009 ⛔ | denied | refused at the floor | — |  |
| 3616 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 3617 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted | decided fresh | — |  |
| 3618 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted | decided fresh | — |  |
| 3619 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | decided fresh | — |  |
| 3620 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted | decided fresh | — |  |
| 3621 | Verify every package the agent imported against the registry | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 3622 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | decided fresh | — |  |
| 3623 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 3624 | Bind the mask revision to its lot and recipe record | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 3625 | Make the audit register append-only and disjoint from the store | SF-GV-005 | permitted | decided fresh | — |  |
| 3626 | Separate the reporter bulletin from the adjudication input path | SF-GV-005 | permitted | decided fresh | — |  |
| 3627 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted | decided fresh | — |  |
| 3628 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-002 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 3629 | Pin the denied-party list snapshot used by a screening decision | SF-EX-010 | permitted | decided fresh | — |  |
| 3630 | Verify every package the agent imported against the registry | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3631 | Drop the deprecated field from the agent's regenerated response body | SF-AG-002 SF-SG-007 ⛔ | denied | refused at the floor | — |  |
| 3632 | Route every screening near-miss to a named compliance reviewer | SF-EX-007 | permitted | decided fresh | — |  |
| 3633 | Re-screen consignees on the published list-refresh cadence | SF-EX-007 | permitted | decided fresh | — |  |
| 3634 | Pin the denied-party list snapshot used by a screening decision | SF-EX-009 | permitted | decided fresh | — |  |
| 3635 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | decided fresh | — |  |
| 3636 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | decided fresh | — |  |
| 3637 | Deliver alarm reports ahead of the collection-event budget | SF-SG-005 | permitted | decided fresh | — |  |
| 3638 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 3639 | Require a human sign-off before an agent edits equipment control code | SF-AG-003 | permitted | bound by precedent | REC-S0106 |  |
| 3640 | Log the deemed-export check that runs at repository role grant | SF-EX-009 | permitted | decided fresh | — |  |
| 3641 | Attach the provenance attestation to the tool-gateway release | SF-SS-005 | permitted | decided fresh | — |  |
| 3642 | Declare the latency budget for the changed metrology path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3643 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted | decided fresh | — |  |
| 3644 | Sign the container image published for the edge tool gateway | SF-SS-011 | permitted | decided fresh | — |  |
| 3645 | Let the agent's enrichment step call an outside classification API | SF-AG-006 | denied | decided fresh | — |  |
| 3646 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 3647 | Add the covered-transaction determination field to the tool purchase record | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 3648 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 3649 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 3650 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-008 | denied | decided fresh | — |  |
| 3651 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | decided fresh | — | ● |
| 3652 | Replace the pickle payload with a schema-validated JSON body | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3653 | Fail the pipeline closed when the screening service times out | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3654 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 3655 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | permitted | decided fresh | — |  |
| 3656 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | decided fresh | — |  |
| 3657 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 3658 | Fail closed on receipt when a forced-labour list match is returned | SF-RS-004 | permitted | decided fresh | — |  |
| 3659 | Record the counterfeit-inspection result and distributor-authorisation status per lot | SF-RS-004 | permitted | decided fresh | — |  |
| 3660 | Remove the human-review requirement from the screening provision | SF-OT-003 | denied | decided fresh | — |  |
| 3661 | Weight supplier terms against firms the model scores as distressed | SF-GV-006 | denied | decided fresh | — |  |
| 3662 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | disposed by citation | — |  |
| 3663 | Shorten the WIP record retention term in the rulebook | SF-AS-002 | denied | decided fresh | — |  |
| 3664 | Move the alarm-fanout write off the monitoring hot path | SF-RT-002 | permitted with conditions | decided fresh | — | ● |
| 3665 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted | decided fresh | — |  |
| 3666 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh | — |  |
| 3667 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 3668 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3669 | Add an authorisation check to the lot-detail API | — | permitted | docketed — nothing engaged | — |  |
| 3670 | Sign the release attestation with the developer's own runner identity | SF-SS-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3671 | Canonicalise the upload path before the handler opens the file | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3672 | Swap the hand-rolled MAC for the library primitive | SF-CR-003 | permitted | decided fresh | — |  |
| 3673 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | disposed by citation | — |  |
| 3674 | Tag every WIP record with the jurisdiction that produced it | SF-DS-004 | permitted | decided fresh | — |  |
| 3675 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | decided fresh | — |  |
| 3676 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted | decided fresh | — |  |
| 3677 | Add the new data flow to the system security plan diagram | SF-NC-005 | permitted | decided fresh | — |  |
| 3678 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 3679 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 3680 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 3681 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 3682 | Broker vendor remote sessions through the jump host | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 3683 | Remove the decommissioned legacy protocol allowlist entries for a tool retired last quarter | SF-OT-003 | permitted | decided fresh | — |  |
| 3684 | Authenticate the time source for every piece of fab equipment | SF-OT-003 | permitted | decided fresh | — |  |
| 3685 | Record the percentile family used for the declared budget | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 3686 | Publish the tool-gateway release from an unattested local build | SF-SS-001 SF-RP-004 ⛔ | denied | refused at the floor | — |  |
| 3687 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-005 | denied | decided fresh | — |  |
| 3688 | Exclude recipe bodies from the vendor support bundle | SF-RP-006 | permitted | decided fresh | — |  |
| 3689 | Keep recipe text out of the yield model's prompt context | SF-RP-006 | permitted | decided fresh | — |  |
| 3690 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 3691 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted | decided fresh | — |  |
| 3692 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 3693 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-001 | denied | decided fresh | — |  |
| 3694 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 3695 | Roll the crypto library back to the version the build used to pin | SF-SS-001 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 3696 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 3697 | Record the control inheritance for the shared platform tier | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3698 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 3699 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | decided fresh | — |  |
| 3700 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-003 SF-AS-001 ⛔ | denied | refused at the floor | — |  |
| 3701 | Bound the collector's allocation rate on the ingest path | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 3702 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | decided fresh | — |  |
| 3703 | Move the charging threshold for the supply chain family | SF-RS-003 | denied | decided fresh | — |  |
| 3704 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 3705 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-004 | permitted | decided fresh | — |  |
| 3706 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted | decided fresh | — |  |
| 3707 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-002 SF-OT-001 ⛔ | denied | refused at the floor | — |  |
| 3708 | Pin the certificate chain used by the metrology ingest client | SF-CR-005 | permitted | decided fresh | — |  |
| 3709 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 3710 | Fail the pipeline closed when the screening service times out | SF-EX-008 | permitted | decided fresh | — |  |
| 3711 | Expand the classification questionnaire for multi-patterning masks | SF-EX-008 | permitted | decided fresh | — |  |
| 3712 | Filter the interlock signal out of the noisy alarm stream | SF-SG-008 | denied | decided fresh | — |  |
| 3713 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-002 SF-RS-004 ⛔ | denied | refused at the floor | — |  |
| 3714 | Validate the ECCN parameter against the enumerated set | SF-AS-002 | permitted | decided fresh | — |  |
| 3715 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 3716 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-010 | denied | decided fresh | — |  |
| 3717 | Raise the latency budget stated in the constitutional parameters | SF-RP-004 | denied | decided fresh | — |  |
| 3718 | Validate the ECCN parameter against the enumerated set | SF-AS-001 | permitted | decided fresh | — |  |
| 3719 | Replace the racy counter with an atomic in the ingest fanout | — | permitted | docketed — nothing engaged | — |  |
| 3720 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 3721 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | decided fresh | — | ● |
| 3722 | Verify component digests against the registry before deploy | SF-SS-004 | permitted | decided fresh | — |  |
| 3723 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | decided fresh | — |  |
| 3724 | Record the builder identity in the release attestation | SF-SS-010 | permitted | decided fresh | — |  |
| 3725 | Record the builder identity in the release attestation | SF-SS-006 | permitted | decided fresh | — | ● |
| 3726 | Record the builder identity in the release attestation | SF-SS-005 | permitted | decided fresh | — |  |
| 3727 | Sign the container image published for the edge tool gateway | SF-SS-005 | permitted | disposed by citation | — |  |
| 3728 | Bound the request body size on the yield analytics endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3729 | Replace the pickle payload with a schema-validated JSON body | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3730 | Record the builder identity in the release attestation | SF-SS-006 | permitted | decided fresh | — |  |
| 3731 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3732 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | decided fresh | — |  |
| 3733 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | decided fresh | — |  |
| 3734 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-004 | permitted | decided fresh | — |  |
| 3735 | Resolve the foreign access request through the named legal channel | SF-DS-007 | permitted | decided fresh | — |  |
| 3736 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 3737 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 3738 | Propose a new provision covering advanced-node lithography data | SF-SO-003 | denied | decided fresh | — |  |
| 3739 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 3740 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 3741 | Add the realised adverse-contest rate to the governance export | SF-GV-007 | permitted | decided fresh | — |  |
| 3742 | Require the licence exception paragraph on the shipment record | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 3743 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-004 | permitted | decided fresh | — |  |
| 3744 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 3745 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 3746 | Drop the smelter-and-refiner questionnaire from the supplier onboarding flow | SF-RS-001 | denied | decided fresh | — | ● |
| 3747 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3748 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-007 | denied | decided fresh | — |  |
| 3749 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 3750 | Publish the EDA toolchain image without running the classification step | SF-EX-002 ⛔ | denied | refused at the floor | — |  |
| 3751 | Wire a host command that can override the lockout/tagout state from the MES | SF-EH-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 3752 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | decided fresh | — |  |
| 3753 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 3754 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted with conditions | decided fresh | — | ● |
| 3755 | Parameterise the supplier portal's lot-search query | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3756 | Switch off forced-labour screening for tier-two suppliers to speed onboarding | SF-RS-002 ⛔ | denied | refused at the floor | — |  |
| 3757 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 3758 | Filter the interlock signal out of the noisy alarm stream | SF-SG-008 | denied | decided fresh | — |  |
| 3759 | Route Kumamoto tool logs to the in-region log sink | SF-DS-004 | permitted | decided fresh | — |  |
| 3760 | Resolve the foreign access request through the named legal channel | SF-DS-004 | permitted | decided fresh | — |  |
| 3761 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 3762 | Record the builder identity in the release attestation | SF-SS-002 | permitted | decided fresh | — |  |
| 3763 | Fail closed on receipt when a forced-labour list match is returned | SF-RS-004 | permitted | decided fresh | — |  |
| 3764 | Delete the held lot's genealogy during the archive cleanup | SF-WI-007 | denied | decided fresh | — |  |
| 3765 | Disable a vendor's remote-access account between sessions | SF-OT-001 | permitted | decided fresh | — |  |
| 3766 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3767 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-002 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 3768 | Add fuzz coverage for the metrology file upload handler | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3769 | Add a retention-hold check to the record destruction job | SF-WI-007 | permitted | decided fresh | — |  |
| 3770 | Add the newly pulled component to the generated SBOM | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 3771 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | decided fresh | — |  |
| 3772 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-001 ⛔ | denied | refused at the floor | — |  |
| 3773 | Declare the latency budget for the changed metrology path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3774 | Record the builder identity in the release attestation | SF-SS-005 | permitted | disposed by citation | — |  |
| 3775 | Require a human sign-off before an agent edits equipment control code | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3776 | Fall back to plain TCP when the tool refuses the TLS handshake | SF-RP-006 | denied | decided fresh | — |  |
| 3777 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted | decided fresh | — |  |
| 3778 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 3779 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | decided fresh | — |  |
| 3780 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 3781 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-002 SF-EH-004 ⛔ | denied | refused at the floor | — |  |
| 3782 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 3783 | Keep recipe execution records until the retention clock expires | SF-WI-004 | permitted | decided fresh | — |  |
| 3784 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted | decided fresh | — |  |
| 3785 | Wire a rollback path into every controller-model promotion | SF-QS-001 | permitted | decided fresh | — |  |
| 3786 | Exclude proscribed-country regions from the defence-enclave storage allowlist | SF-IT-002 | permitted | decided fresh | — |  |
| 3787 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3788 | Amend the consolidation class threshold in the parameters file | SF-CR-006 | denied | decided fresh | — |  |
| 3789 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted | decided fresh | — |  |
| 3790 | Add the AGPL trace decoder to the customer-deployed tool gateway | SF-SS-003 | denied | decided fresh | — |  |
| 3791 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted | decided fresh | — |  |
| 3792 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | permitted | decided fresh | — |  |
| 3793 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-004 | denied | decided fresh | — | ● |
| 3794 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted with conditions | decided fresh | — | ● |
| 3795 | Classify a process change as major or minor with recorded rationale | SF-QS-002 | permitted | decided fresh | — |  |
| 3796 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-002 | permitted | decided fresh | — |  |
| 3797 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 3798 | Add fuzz coverage for the metrology file upload handler | — | permitted | docketed — nothing engaged | — |  |
| 3799 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-003 | permitted | decided fresh | — |  |
| 3800 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted with conditions | decided fresh | — | ● |
| 3801 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3802 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3803 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — | ● |
| 3804 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3805 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted with conditions | decided fresh | — | ● |
| 3806 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — |  |
| 3807 | Attach the provenance attestation to the tool-gateway release | SF-SS-005 | permitted | decided fresh | — |  |
| 3808 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh | — |  |
| 3809 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-006 | permitted | decided fresh | — |  |
| 3810 | Document the sub-processor chain for the supplier portal CDN | SF-DS-006 | permitted | decided fresh | — |  |
| 3811 | Serialise the two writers to the yield aggregation table | SF-TQ-003 | permitted | decided fresh | — |  |
| 3812 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3813 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 3814 | Record the percentile family used for the declared budget | SF-RT-004 | permitted | decided fresh | — |  |
| 3815 | Route hazardous-gas alarms to the life-safety panel ahead of any analytics path | SF-EH-004 | permitted | decided fresh | — |  |
| 3816 | Record the percentile family used for the declared budget | SF-RT-002 | permitted | decided fresh | — |  |
| 3817 | Add an authorisation check to the lot-detail API | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3818 | Store the superseded metrology value beside its correction | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 3819 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-002 | permitted | decided fresh | — |  |
| 3820 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted | decided fresh | — |  |
| 3821 | Pull tool firmware updates from an unverified community mirror | SF-OT-003 | denied | decided fresh | — |  |
| 3822 | Build the lot-search query by concatenating the filter string | SF-AS-003 | denied | decided fresh | — |  |
| 3823 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 3824 | Expand the classification questionnaire for multi-patterning masks | SF-EX-012 | permitted | decided fresh | — |  |
| 3825 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 3826 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted | decided fresh | — |  |
| 3827 | Resolve the foreign access request through the named legal channel | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 3828 | Give the vendor a persistent VPN connection instead of a brokered session | SF-OT-002 | denied | decided fresh | — | ● |
| 3829 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | decided fresh | — |  |
| 3830 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 3831 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 3832 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-013 | denied | decided fresh | — |  |
| 3833 | Swap the hand-rolled MAC for the library primitive | SF-CR-003 | permitted | decided fresh | — |  |
| 3834 | Restrict certificate key types to the permitted set | SF-CR-003 | permitted | decided fresh | — |  |
| 3835 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 3836 | Restrict certificate key types to the permitted set | SF-CR-004 | permitted | decided fresh | — |  |
| 3837 | Record the ECCN determination alongside the design-file upload | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 3838 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 3839 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3840 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 3841 | Raise the tool-gateway TLS floor to the declared version | SF-CR-006 | permitted | decided fresh | — |  |
| 3842 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 3843 | Switch the ingest service to the throughput collector | SF-RT-006 | denied | decided fresh | — |  |
| 3844 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3845 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 3846 | Verify component digests against the registry before deploy | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 3847 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 3848 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3849 | Record the exception authority against the accepting principal | SF-GV-007 | permitted | decided fresh | — | ● |
| 3850 | Document the invariant the metrology ingest lock protects | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 3851 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 3852 | Scope the internal SECS parser package to the private registry | SF-SS-007 | permitted with conditions | decided fresh | — | ● |
| 3853 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 3854 | Allowlist the export format instead of shelling out with user input | — | permitted | docketed — nothing engaged | — |  |
| 3855 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3856 | Document the CUI boundary for the metrology ingest service | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 3857 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-005 | permitted | decided fresh | — |  |
| 3858 | Publish the measurement window with the latency result | SF-RT-002 | permitted | decided fresh | — |  |
| 3859 | Split the slow enrichment step out of the alarm path | SF-RT-002 | permitted | decided fresh | — |  |
| 3860 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-010 | denied | decided fresh | — |  |
| 3861 | Scope the internal SECS parser package to the private registry | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 3862 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted | decided fresh | — |  |
| 3863 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-002 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 3864 | Add a scanner for process parameters in application logs | SF-RP-004 | permitted | decided fresh | — | ● |
| 3865 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3866 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted | decided fresh | — |  |
| 3867 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | decided fresh | — |  |
| 3868 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 3869 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-002 | permitted | decided fresh | — |  |
| 3870 | Drop the deprecated cipher suites from the supplier portal | SF-CR-002 | permitted | decided fresh | — |  |
| 3871 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — |  |
| 3872 | Document the CUI boundary for the metrology ingest service | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3873 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 3874 | Call the licence service synchronously from the tool event handler | SF-RT-002 | denied | decided fresh | — |  |
| 3875 | Hide the appeal button on the automated screening result page | SF-GV-001 SF-SS-010 ⛔ | denied | refused at the floor | — |  |
| 3876 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3877 | Roll the crypto library back to the version the build used to pin | SF-SS-002 | denied | decided fresh | — |  |
| 3878 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | disposed by citation | — |  |
| 3879 | Gate the important-data export on the completed security assessment | SF-DS-005 | permitted | decided fresh | — |  |
| 3880 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 3881 | Confine defence-article design reviews to the segregated enclave workstation | SF-IT-002 | permitted with conditions | decided fresh | — | ● |
| 3882 | Add secret scanning to the pre-merge pipeline | SF-SS-010 | permitted | disposed by citation | — |  |
| 3883 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | decided fresh | — |  |
| 3884 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted | decided fresh | — |  |
| 3885 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 3886 | Suppress the duplicate-alarm banner in the operator UI while keeping the underlying gas alarm and page intact | SF-EH-004 | permitted | decided fresh | — |  |
| 3887 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 3888 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted | decided fresh | — |  |
| 3889 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 3890 | Update the supply chain risk plan after the vendor change | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 3891 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3892 | Record the percentile family used for the declared budget | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3893 | Filter the interlock signal out of the noisy alarm stream | SF-SG-001 SF-OT-002 ⛔ | denied | refused at the floor | — |  |
| 3894 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3895 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-006 | permitted | decided fresh | — |  |
| 3896 | Add an authorisation check to the lot-detail API | SF-AS-005 | permitted | docketed — not charged | — |  |
| 3897 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 3898 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted | decided fresh | — |  |
| 3899 | Let the retention sweep run across lots that are under legal hold | SF-DS-002 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 3900 | Attach an agent provenance attestation to the generated migration | SF-AG-006 | permitted | decided fresh | — | ● |
| 3901 | Move recipe transfer onto the mutually authenticated channel | SF-RP-006 | permitted | decided fresh | — |  |
| 3902 | Redact recipe parameters from the tool-gateway debug log | SF-RP-006 | permitted | decided fresh | — |  |
| 3903 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-006 | permitted | decided fresh | — |  |
| 3904 | Add a configuration flag that releases blocked-property holds for expedited orders | SF-SO-002 SF-QS-002 ⛔ | denied | refused at the floor | — |  |
| 3905 | Switch the ingest service to the throughput collector | SF-RT-003 | denied | decided fresh | — | ● |
| 3906 | Retire the superseded cryptographic floor from the constitution | SF-SS-003 | denied | decided fresh | — |  |
| 3907 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-002 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 3908 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-004 | permitted | decided fresh | — |  |
| 3909 | Name the licence-exception paragraph on every ITAR transfer record | SF-IT-004 | permitted | decided fresh | — |  |
| 3910 | Drop the deprecated field from the agent's regenerated response body | SF-AG-007 | denied | decided fresh | — |  |
| 3911 | Add an unauthenticated time server to the tool network for a quick fix | SF-OT-003 | denied | decided fresh | — |  |
| 3912 | Rewrite historical ledger rows during the partition migration | SF-WI-003 | denied | decided fresh | — |  |
| 3913 | Stop shipping equipment logs across the boundary by default | SF-DS-006 | permitted | decided fresh | — |  |
| 3914 | Move recipe transfer onto the mutually authenticated channel | SF-RP-007 | permitted | decided fresh after a tie | none_tie |  |
| 3915 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 3916 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-007 | denied | decided fresh | — |  |
| 3917 | Rewrite historical ledger rows during the partition migration | SF-WI-001 ⛔ | denied | refused at the floor | — |  |
| 3918 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 3919 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted | decided fresh | — |  |
| 3920 | Deliver alarm reports ahead of the collection-event budget | SF-SG-003 | permitted | disposed by citation | — |  |
| 3921 | Surface the applicable ECCN on the supplier portal download page | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 3922 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — | ● |
| 3923 | Skip the nationality check when granting repository roles to contractors | SF-EX-001 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 3924 | Map the new component to its NIST control identifier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 3925 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 3926 | Document the invariant the metrology ingest lock protects | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 3927 | Rate-limit the supplier portal's document download endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3928 | Exclude audit findings from the retrieval query | SF-GV-006 | permitted | decided fresh | — | ● |
| 3929 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 3930 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 3931 | Validate the ECCN parameter against the enumerated set | SF-AS-006 | permitted | docketed — not charged | — |  |
| 3932 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-007 | permitted | decided fresh | — |  |
| 3933 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-007 | permitted | decided fresh | — |  |
| 3934 | Add a configuration flag that releases blocked-property holds for expedited orders | SF-SO-002 ⛔ | denied | refused at the floor | — |  |
| 3935 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-002 | denied | decided fresh | — |  |
| 3936 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 3937 | Retry S2F41 remote commands without reordering the queue | SF-SG-006 | permitted | decided fresh | — |  |
| 3938 | Rotate the recipe vault envelope key on the published schedule | SF-RP-005 | permitted | decided fresh | — |  |
| 3939 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-002 | permitted | decided fresh | — |  |
| 3940 | Allowlist the export format instead of shelling out with user input | SF-AS-002 | permitted | decided fresh | — |  |
| 3941 | Let the coding agent rewrite the tool command dispatcher | SF-AG-004 | denied | decided fresh | — |  |
| 3942 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3943 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 3944 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3945 | Make export decisions append-only in the trade compliance ledger | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 3946 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 3947 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 3948 | Expand the classification questionnaire for multi-patterning masks | SF-EX-007 | permitted | decided fresh | — |  |
| 3949 | Add the enrichment lookup to the alarm path despite the tail regression | SF-RT-004 | denied | decided fresh | — |  |
| 3950 | Retry S2F41 remote commands without reordering the queue | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 3951 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 3952 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 3953 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted | decided fresh | — |  |
| 3954 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 3955 | Rename the lot-detail route in the agent's generated router | SF-AG-001 ⛔ | denied | refused at the floor | — |  |
| 3956 | Keep recipe text out of the yield model's prompt context | SF-RP-006 | permitted | decided fresh | — |  |
| 3957 | Fail the sanctions screening pipeline closed when the list service is unreachable | SF-SO-003 | permitted | decided fresh | — |  |
| 3958 | Route every boycott-request match to the quarterly filing queue | SF-SO-003 | permitted | decided fresh | — |  |
| 3959 | Link each claimed control to its implementation statement | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 3960 | Add an unauthenticated time server to the tool network for a quick fix | SF-OT-002 | denied | decided fresh | — |  |
| 3961 | Build the lot-search query by concatenating the filter string | SF-AS-001 | denied | decided fresh | — | ● |
| 3962 | Benchmark the broker with an open-loop client and report the median | SF-RT-003 | denied | decided fresh | — |  |
| 3963 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3964 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 3965 | Replace the racy counter with an atomic in the ingest fanout | — | permitted | docketed — nothing engaged | — |  |
| 3966 | Broker vendor remote sessions through the jump host | SF-OT-004 | permitted | decided fresh | — |  |
| 3967 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-004 | permitted | decided fresh | — |  |
| 3968 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | decided fresh | — |  |
| 3969 | Let the coding agent rewrite the tool command dispatcher | SF-AG-001 SF-RP-003 ⛔ | denied | refused at the floor | — |  |
| 3970 | Make export decisions append-only in the trade compliance ledger | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 3971 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 3972 | Let the retention sweep run across lots that are under legal hold | SF-DS-002 ⛔ | denied | refused at the floor | — |  |
| 3973 | Publish the EDA toolchain image without running the classification step | SF-EX-009 | denied | decided fresh | — |  |
| 3974 | Carry the regulatory hold flag through the archive migration | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 3975 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3976 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-003 | permitted | decided fresh | — | ● |
| 3977 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 3978 | Replace the pickle payload with a schema-validated JSON body | SF-AS-007 | permitted | docketed — not charged | — |  |
| 3979 | Remove the verification-of-effectiveness step from the corrective-action workflow | SF-QS-002 | denied | decided fresh | — |  |
| 3980 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 3981 | Keep audit logging on during the throughput optimisation | SF-WI-005 | permitted | decided fresh | — |  |
| 3982 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-006 | permitted | decided fresh | — |  |
| 3983 | Require a human sign-off before an agent edits equipment control code | SF-AG-006 | permitted | decided fresh | — |  |
| 3984 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | decided fresh | — |  |
| 3985 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3986 | Add fuzz coverage for the metrology file upload handler | SF-AS-004 | permitted | docketed — not charged | — |  |
| 3987 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | decided fresh | — |  |
| 3988 | Add the newly pulled component to the generated SBOM | SF-SS-009 | permitted | decided fresh | — |  |
| 3989 | Document the invariant the metrology ingest lock protects | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3990 | Keep audit logging on during the throughput optimisation | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 3991 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 3992 | Record the ownership data source and snapshot date on every screening result | SF-SO-003 | permitted | decided fresh | — |  |
| 3993 | Remove the human-review requirement from the screening provision | SF-DS-004 | denied | decided fresh | — |  |
| 3994 | Exclude audit findings from the retrieval query | SF-GV-003 | permitted | decided fresh | — |  |
| 3995 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-003 | permitted | decided fresh | — |  |
| 3996 | Re-enable the legacy cipher suite so the older scanner can connect | SF-CR-001 SF-SO-003 ⛔ | denied | refused at the floor | — |  |
| 3997 | Write the full rationale trail at the moment of resolution | SF-GV-005 | permitted | decided fresh | — | ● |
| 3998 | Move key material into the hardware security module | SF-CR-004 | permitted | decided fresh | — |  |
| 3999 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-004 | permitted | decided fresh | — | ● |
| 4000 | Ship the in-country support tunnel with the access question still open | SF-DS-002 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 4001 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4002 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — |  |
| 4003 | Carry the regulatory hold flag through the archive migration | SF-WI-007 | permitted | decided fresh | — |  |
| 4004 | Bound the SECS message queue depth per tool connection | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 4005 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted with conditions | decided fresh | — | ● |
| 4006 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | decided fresh | — |  |
| 4007 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh | — |  |
| 4008 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | decided fresh | — |  |
| 4009 | Persist every effluent monitoring result before report aggregation runs | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 4010 | Document the CUI boundary for the metrology ingest service | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4011 | Attribute every metrology record amendment to a named operator | SF-WI-004 | permitted | decided fresh | — |  |
| 4012 | Add a residency assertion to the metrology ingest contract | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4013 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-006 | permitted | decided fresh | — |  |
| 4014 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 4015 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — |  |
| 4016 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 4017 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 4018 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-001 | denied | decided fresh | — |  |
| 4019 | Bound the SECS message queue depth per tool connection | SF-SG-010 | permitted | disposed by citation | — |  |
| 4020 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-005 | permitted | decided fresh | — |  |
| 4021 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted | decided fresh | — |  |
| 4022 | Expand the classification questionnaire for multi-patterning masks | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 4023 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | decided fresh | — | ● |
| 4024 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 4025 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 4026 | Bound the request body size on the yield analytics endpoint | — | permitted | docketed — nothing engaged | — |  |
| 4027 | Bound the telemetry buffer so ingest backpressure is visible | — | permitted | docketed — nothing engaged | — |  |
| 4028 | Sign the container image published for the edge tool gateway | SF-SS-006 | permitted | disposed by citation | — |  |
| 4029 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4030 | Add the enrichment lookup to the alarm path despite the tail regression | SF-RT-007 | denied | decided fresh | — |  |
| 4031 | Order the two mutex acquisitions consistently across both paths | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4032 | Lower a gas-detector alarm threshold after a failed calibration, with EHS signoff recorded same day | SF-EH-004 | permitted | decided fresh | — |  |
| 4033 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted | decided fresh | — |  |
| 4034 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-005 | denied | decided fresh | — |  |
| 4035 | Reroute S6F11 event reports through the new async fanout | SF-SG-010 | denied | decided fresh | — |  |
| 4036 | Report load conditions alongside the p99.9 measurement | SF-RT-005 | permitted | decided fresh | — |  |
| 4037 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | permitted | decided fresh | — |  |
| 4038 | Record the builder identity in the release attestation | SF-SS-006 | permitted | decided fresh | — |  |
| 4039 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4040 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 4041 | Order the two mutex acquisitions consistently across both paths | — | permitted | docketed — nothing engaged | — |  |
| 4042 | Parameterise the supplier portal's lot-search query | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4043 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 4044 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 4045 | Remove the human-review requirement from the screening provision | SF-AG-003 | denied | decided fresh | — |  |
| 4046 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 4047 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-006 SF-RS-004 ⛔ | denied | refused at the floor | — |  |
| 4048 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | decided fresh | — |  |
| 4049 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-008 | permitted | decided fresh | — |  |
| 4050 | Retry S2F41 remote commands without reordering the queue | SF-SG-008 | permitted | decided fresh | — |  |
| 4051 | Drop the standing declaration from the governance export payload | SF-GV-002 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 4052 | Purge recipe execution records older than ninety days | SF-WI-001 SF-GV-005 ⛔ | denied | refused at the floor | — |  |
| 4053 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 4054 | Wire a host command that can override the lockout/tagout state from the MES | SF-EH-001 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 4055 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted | decided fresh | — |  |
| 4056 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-001 | permitted | decided fresh | — |  |
| 4057 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-002 | permitted | decided fresh | — |  |
| 4058 | Record the jurisdiction determination before a defence-adjacent file is ingested | SF-IT-002 | permitted | decided fresh | — |  |
| 4059 | Record the percentile family used for the declared budget | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 4060 | Build the badge-photo gallery by scraping the site camera archive | SF-GV-006 | denied | decided fresh | — |  |
| 4061 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 4062 | Encrypt the recipe payload at rest in the vault | SF-RP-004 | permitted | decided fresh | — |  |
| 4063 | Record the percentile family used for the declared budget | SF-RT-005 | permitted | decided fresh | — |  |
| 4064 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-004 | permitted | decided fresh | — |  |
| 4065 | Tag every WIP record with the jurisdiction that produced it | SF-DS-006 | permitted | decided fresh | — |  |
| 4066 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted | decided fresh | — |  |
| 4067 | Rotate the recipe vault envelope key on the published schedule | SF-RP-004 | permitted | decided fresh | — |  |
| 4068 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 4069 | Add an authorisation check to the lot-detail API | SF-AS-001 | permitted | decided fresh | — |  |
| 4070 | Report a suspect counterfeit part to the named quality owner before disposition | SF-RS-004 | permitted | decided fresh | — |  |
| 4071 | Retry S2F41 remote commands without reordering the queue | SF-SG-010 | permitted | decided fresh after a tie | none_tie |  |
| 4072 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-009 | denied | decided fresh | — | ● |
| 4073 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4074 | Close the check-then-open window in the metrology file handler | SF-TQ-004 | permitted | decided fresh | — |  |
| 4075 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted | decided fresh | — |  |
| 4076 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-001 SF-WI-005 ⛔ | denied | refused at the floor | — |  |
| 4077 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4078 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-003 | permitted | decided fresh | — |  |
| 4079 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-005 SF-SG-008 ⛔ | denied | refused at the floor | — |  |
| 4080 | Add a GEM control-state transition test for the Lam etcher | SF-SG-006 | permitted | decided fresh | — |  |
| 4081 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — |  |
| 4082 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4083 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 4084 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 4085 | Record the percentile family used for the declared budget | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 4086 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | decided fresh | — |  |
| 4087 | Deliver alarm reports ahead of the collection-event budget | SF-SG-005 | permitted | decided fresh | — |  |
| 4088 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4089 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-002 SF-CR-006 ⛔ | denied | refused at the floor | — |  |
| 4090 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4091 | Rewrite the metrology ingest path without stating its timing target | SF-RT-001 | denied | decided fresh | — |  |
| 4092 | Version the supplier declaration record on every effective-date change | SF-RS-004 | permitted with conditions | decided fresh | — | ● |
| 4093 | Close the check-then-open window in the metrology file handler | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4094 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-005 | permitted | decided fresh | — |  |
| 4095 | Quarantine a broker-sourced lot pending provenance verification | SF-RS-003 | permitted | decided fresh | — |  |
| 4096 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-006 | permitted | decided fresh | — |  |
| 4097 | Move key material into the hardware security module | SF-CR-006 | permitted | decided fresh | — |  |
| 4098 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 4099 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — | ● |
| 4100 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 4101 | Scope recipe vault reads to the owning process integration team | SF-RP-004 | permitted | decided fresh | — |  |
| 4102 | Add a GEM control-state transition test for the Lam etcher | SF-SG-003 | permitted | disposed by citation | — |  |
| 4103 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 4104 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 4105 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-004 | permitted | decided fresh | — |  |
| 4106 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted | disposed by citation | — |  |
| 4107 | Add a stress test that runs the broker under concurrent tool load | — | permitted | docketed — nothing engaged | — |  |
| 4108 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-004 | permitted | decided fresh | — |  |
| 4109 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted | decided fresh | — |  |
| 4110 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | decided fresh | — |  |
| 4111 | Update the supply chain risk plan after the vendor change | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4112 | Document the CUI boundary for the metrology ingest service | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 4113 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | disposed by citation | — |  |
| 4114 | Add an authorisation check to the lot-detail API | SF-AS-004 | permitted | docketed — not charged | — |  |
| 4115 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 4116 | Rotate the recipe vault envelope key on the published schedule | SF-RP-006 | permitted | decided fresh | — |  |
| 4117 | Write the full rationale trail at the moment of resolution | SF-GV-003 | permitted | decided fresh | — |  |
| 4118 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted | decided fresh | — | ● |
| 4119 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4120 | Stop shipping equipment logs across the boundary by default | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4121 | Pin the denied-party list snapshot used by a screening decision | SF-EX-010 | permitted | decided fresh | — |  |
| 4122 | Capture the licence determination rationale in the trade record | SF-EX-010 | permitted | decided fresh | — |  |
| 4123 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-002 | permitted | decided fresh | — |  |
| 4124 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 4125 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-002 | permitted | decided fresh | — |  |
| 4126 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4127 | Attach the provenance attestation to the tool-gateway release | SF-SS-004 | permitted | disposed by citation | — |  |
| 4128 | Replace the direct-URL dependency with a registry release | SF-SS-003 | permitted | decided fresh | — |  |
| 4129 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4130 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 4131 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | permitted | decided fresh | — |  |
| 4132 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 4133 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-002 | permitted | decided fresh | — |  |
| 4134 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | decided fresh | — |  |
| 4135 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4136 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 4137 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 4138 | Tag every WIP record with the jurisdiction that produced it | SF-DS-004 | permitted | decided fresh | — | ● |
| 4139 | Hand the defence-enclave decryption key to the cloud provider's managed key service | SF-IT-003 ⛔ | denied | refused at the floor | — |  |
| 4140 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-003 | permitted | decided fresh | — |  |
| 4141 | Exempt distributor accounts from the sanctions screening step | SF-SO-001 SF-CR-005 ⛔ | denied | refused at the floor | — |  |
| 4142 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | decided fresh | — |  |
| 4143 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | decided fresh | — |  |
| 4144 | Route Kumamoto tool logs to the in-region log sink | SF-DS-003 | permitted | decided fresh | — |  |
| 4145 | Sign the release attestation with the developer's own runner identity | SF-SS-008 | denied | decided fresh | — |  |
| 4146 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-008 | permitted | decided fresh | — |  |
| 4147 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4148 | Validate the ECCN parameter against the enumerated set | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4149 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | decided fresh | — |  |
| 4150 | Return a correlation id instead of a stack trace to the client | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4151 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 4152 | Refresh the control assessment for the changed audit path | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4153 | Drop the mutex around the shared WIP counter to cut contention | SF-TQ-001 | denied | decided fresh | — |  |
| 4154 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | disposed by citation | — |  |
| 4155 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 4156 | Parameterise the supplier portal's lot-search query | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4157 | Canonicalise the upload path before the handler opens the file | — | permitted | docketed — nothing engaged | — |  |
| 4158 | Raise the tool-gateway TLS floor to the declared version | SF-CR-002 | permitted | decided fresh | — |  |
| 4159 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | decided fresh | — |  |
| 4160 | Add an authorisation check to the lot-detail API | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4161 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-005 | permitted | decided fresh | — |  |
| 4162 | Record the agent identity and model version on the pull request | SF-AG-004 | permitted | decided fresh | — |  |
| 4163 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh | — |  |
| 4164 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-004 | permitted | decided fresh | — | ● |
| 4165 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 4166 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 4167 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-004 | permitted | decided fresh | — |  |
| 4168 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 4169 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4170 | Propose deferring the sovereignty provision to the next assessment cycle | SF-QS-003 | denied | decided fresh | — |  |
| 4171 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted | decided fresh | — | ● |
| 4172 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 4173 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 4174 | Verify the artifact signature before the tool gateway installs it | SF-CR-002 | permitted | decided fresh | — |  |
| 4175 | Surface the applicable ECCN on the supplier portal download page | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 4176 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4177 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted | decided fresh | — |  |
| 4178 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted | decided fresh | — |  |
| 4179 | Restore the lock around the WIP snapshot read-modify-write | — | permitted | docketed — nothing engaged | — |  |
| 4180 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-004 | denied | decided fresh | — |  |
| 4181 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted | decided fresh | — |  |
| 4182 | Verify component digests against the registry before deploy | SF-SS-002 | permitted with conditions | decided fresh | — | ● |
| 4183 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | decided fresh | — |  |
| 4184 | Split the slow enrichment step out of the alarm path | SF-RT-006 | permitted | decided fresh | — |  |
| 4185 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | permitted | decided fresh | — |  |
| 4186 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4187 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 4188 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | decided fresh | — | ● |
| 4189 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-004 SF-SG-007 ⛔ | denied | refused at the floor | — |  |
| 4190 | Wire a rollback path into every controller-model promotion | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 4191 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 4192 | Publish the EDA toolchain image without running the classification step | SF-EX-003 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 4193 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 4194 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4195 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4196 | Let a retired photomask revision be dispatched to the exposure tool | SF-QS-003 | denied | decided fresh | — |  |
| 4197 | Open the mature-node process dataset export ahead of the assessment sign-off | SF-DS-002 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 4198 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4199 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-002 | denied | decided fresh | — | ● |
| 4200 | Hand the defence-enclave decryption key to the cloud provider's managed key service | SF-IT-002 | denied | decided fresh | — |  |
| 4201 | Fail the pipeline closed when the screening service times out | SF-EX-010 | permitted | decided fresh | — |  |
| 4202 | Require the licence exception paragraph on the shipment record | SF-EX-009 | permitted | decided fresh | — |  |
| 4203 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 4204 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4205 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted | decided fresh | — | ● |
| 4206 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 4207 | Open a corrective-action record for every nonconformance | SF-QS-002 | permitted | decided fresh | — |  |
| 4208 | Enforce the customer's notice period at the release gate | SF-QS-002 | permitted | decided fresh | — |  |
| 4209 | Document the invariant the metrology ingest lock protects | SF-TQ-001 | permitted | decided fresh | — |  |
| 4210 | Serialise the two writers to the yield aggregation table | SF-TQ-001 | permitted | decided fresh | — |  |
| 4211 | Expand the classification questionnaire for multi-patterning masks | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 4212 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4213 | Write the full rationale trail at the moment of resolution | SF-GV-003 | permitted | decided fresh | — |  |
| 4214 | Add a residency assertion to the metrology ingest contract | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4215 | Version collection-event identifiers instead of renumbering them | SF-SG-008 | permitted | decided fresh | — |  |
| 4216 | Add a retention-hold check to the record destruction job | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 4217 | Replace the direct-URL dependency with a registry release | SF-SS-008 | permitted | disposed by citation | — |  |
| 4218 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | decided fresh | — |  |
| 4219 | Add secret scanning to the pre-merge pipeline | SF-SS-009 | permitted | decided fresh | — |  |
| 4220 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-004 | permitted | decided fresh | — | ● |
| 4221 | Add secret scanning to the pre-merge pipeline | SF-SS-005 | permitted | disposed by citation | — |  |
| 4222 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted | decided fresh after a tie | none_tie |  |
| 4223 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 4224 | Validate the ECCN parameter against the enumerated set | SF-AS-003 | permitted | decided fresh | — | ● |
| 4225 | Attach an agent provenance attestation to the generated migration | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4226 | Deliver alarm reports ahead of the collection-event budget | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4227 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 4228 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-004 | permitted | decided fresh | — |  |
| 4229 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh | — |  |
| 4230 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | disposed by citation | — |  |
| 4231 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 4232 | Serialise the two writers to the yield aggregation table | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4233 | Join the audit findings table into the precedent retrieval query | SF-GV-002 SF-EX-010 ⛔ | denied | refused at the floor | — |  |
| 4234 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | decided fresh | — |  |
| 4235 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — |  |
| 4236 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | decided fresh | — | ● |
| 4237 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 4238 | Reclassify the recipe-protection provision as advisory | SF-QS-004 | denied | decided fresh | — |  |
| 4239 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | decided fresh | — |  |
| 4240 | Batch alarm reports into the five-second telemetry flush | SF-SG-002 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 4241 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4242 | Keep audit logging on during the throughput optimisation | SF-WI-003 | permitted | decided fresh | — |  |
| 4243 | Add the covered-transaction determination field to the tool purchase record | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4244 | Record the percentile family used for the declared budget | SF-RT-006 | permitted | decided fresh | — |  |
| 4245 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 4246 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-003 | permitted | bound by precedent | REC-S0106 |  |
| 4247 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4248 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh after a tie | none_tie |  |
| 4249 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-008 | permitted | decided fresh | — |  |
| 4250 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4251 | Surface unparsed equipment replies instead of dropping them | SF-SG-007 | permitted with conditions | decided fresh | — | ● |
| 4252 | Add a licence-exception clause to the trade compliance rulebook | SF-DS-006 | denied | decided fresh | — |  |
| 4253 | Attach qualification evidence to every process-change record | SF-QS-001 | permitted | decided fresh | — |  |
| 4254 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh | — |  |
| 4255 | Add secret scanning to the pre-merge pipeline | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 4256 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-002 SF-EX-012 ⛔ | denied | refused at the floor | — |  |
| 4257 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-007 | permitted | decided fresh | — |  |
| 4258 | Move the alarm-fanout write off the monitoring hot path | SF-RT-004 | permitted | decided fresh | — |  |
| 4259 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-004 | permitted | decided fresh | — |  |
| 4260 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4261 | Force the etcher to offline control state during the gateway deploy | SF-SG-002 SF-EX-009 ⛔ | denied | refused at the floor | — |  |
| 4262 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4263 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4264 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-008 | permitted | disposed by citation | — |  |
| 4265 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | disposed by citation | — |  |
| 4266 | Add the new data flow to the system security plan diagram | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 4267 | Split the slow enrichment step out of the alarm path | SF-RT-005 | permitted | decided fresh | — | ● |
| 4268 | Raise the latency budget stated in the constitutional parameters | SF-CR-004 | denied | decided fresh | — |  |
| 4269 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-002 | permitted with conditions | decided fresh | — | ● |
| 4270 | Order the two mutex acquisitions consistently across both paths | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4271 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | decided fresh | — | ● |
| 4272 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 4273 | Hash the recipe identifier before it reaches the analytics store | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 4274 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4275 | Benchmark the broker with an open-loop client and report the median | SF-RT-003 | denied | decided fresh | — |  |
| 4276 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | permitted | decided fresh | — |  |
| 4277 | Encrypt the recipe payload at rest in the vault | SF-RP-005 | permitted | decided fresh | — |  |
| 4278 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-001 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 4279 | Keep recipe text out of the yield model's prompt context | SF-RP-004 | permitted | decided fresh | — |  |
| 4280 | Call the licence service synchronously from the tool event handler | SF-RT-004 | denied | decided fresh | — |  |
| 4281 | Surface unparsed equipment replies instead of dropping them | SF-SG-003 | permitted | decided fresh | — |  |
| 4282 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted | decided fresh | — |  |
| 4283 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | decided fresh | — |  |
| 4284 | Replace the direct-URL dependency with a registry release | SF-SS-005 | permitted | decided fresh | — |  |
| 4285 | Add a negative test for a tampered recipe signature | SF-CR-002 | permitted | decided fresh | — |  |
| 4286 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-003 | denied | decided fresh | — |  |
| 4287 | Scope the internal SECS parser package to the private registry | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 4288 | Rotate the recipe vault envelope key on the published schedule | SF-RP-006 | permitted | decided fresh | — |  |
| 4289 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 4290 | Canonicalise the upload path before the handler opens the file | — | permitted | docketed — nothing engaged | — |  |
| 4291 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4292 | Add the destination geofence to the design-file download path | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 4293 | Batch alarm reports into the five-second telemetry flush | SF-SG-010 | denied | decided fresh | — |  |
| 4294 | Assert the safety interlock signal survives the gateway refactor | SF-SG-007 | permitted | decided fresh | — |  |
| 4295 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | decided fresh | — |  |
| 4296 | Fail the pipeline closed when the screening service times out | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 4297 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | disposed by citation | — |  |
| 4298 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4299 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 4300 | Tag every WIP record with the jurisdiction that produced it | SF-DS-006 | permitted | decided fresh | — |  |
| 4301 | Make export decisions append-only in the trade compliance ledger | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 4302 | Add secret scanning to the pre-merge pipeline | SF-SS-003 | permitted | decided fresh | — |  |
| 4303 | Bound the request body size on the yield analytics endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4304 | Add fuzz coverage for the metrology file upload handler | SF-AS-001 | permitted | decided fresh | — |  |
| 4305 | Shorten the WIP record retention term in the rulebook | SF-EX-013 | denied | decided fresh | — |  |
| 4306 | Benchmark the broker with an open-loop client and report the median | SF-RT-001 | denied | decided fresh | — |  |
| 4307 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted | decided fresh | — |  |
| 4308 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh | — |  |
| 4309 | Pull the ingest parser from a mirror whose digest no longer matches | SF-SS-001 SF-QS-004 ⛔ | denied | refused at the floor | — |  |
| 4310 | Broker vendor remote sessions through the jump host | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 4311 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 4312 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | decided fresh | — |  |
| 4313 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 4314 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 4315 | Ship the in-country support tunnel with the access question still open | SF-DS-001 SF-SG-010 ⛔ | denied | refused at the floor | — |  |
| 4316 | Preserve S6F11 event ordering under broker backpressure | SF-SG-004 | permitted | decided fresh | — |  |
| 4317 | Map the new component to its NIST control identifier | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 4318 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-003 | permitted | decided fresh | — |  |
| 4319 | Keep the HSMS reply timeout inside the declared bound | SF-SG-003 | permitted | decided fresh | — |  |
| 4320 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | decided fresh | — |  |
| 4321 | Record the exception authority against the accepting principal | SF-GV-005 | permitted | decided fresh | — |  |
| 4322 | Add a negative test for a tampered recipe signature | SF-CR-002 | permitted | decided fresh | — |  |
| 4323 | Record the percentile family used for the declared budget | SF-RT-006 | permitted | decided fresh | — |  |
| 4324 | Add a config flag that disables the destination geofence for demos | SF-EX-003 SF-EX-008 ⛔ | denied | refused at the floor | — |  |
| 4325 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 4326 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4327 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-011 | permitted | decided fresh | — | ● |
| 4328 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 4329 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 4330 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4331 | Move the alarm-fanout write off the monitoring hot path | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 4332 | Order the two mutex acquisitions consistently across both paths | — | permitted | docketed — nothing engaged | — |  |
| 4333 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-002 SF-RT-001 ⛔ | denied | refused at the floor | — |  |
| 4334 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-008 | permitted | decided fresh | — |  |
| 4335 | Verify every package the agent imported against the registry | SF-AG-008 | permitted | decided fresh | — |  |
| 4336 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4337 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | decided fresh | — |  |
| 4338 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | decided fresh | — |  |
| 4339 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | disposed by citation | — |  |
| 4340 | Validate the ECCN parameter against the enumerated set | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4341 | Close the check-then-open window in the metrology file handler | SF-TQ-003 | permitted | decided fresh | — |  |
| 4342 | Attach qualification evidence to every process-change record | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 4343 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4344 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted | decided fresh | — |  |
| 4345 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | decided fresh | — | ● |
| 4346 | Report the new latency number without saying what load produced it | SF-RT-003 | denied | decided fresh | — |  |
| 4347 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 4348 | Record the builder identity in the release attestation | SF-SS-009 | permitted | decided fresh | — |  |
| 4349 | Refresh the control assessment for the changed audit path | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4350 | Let the MES correct yesterday's WIP status in place | SF-WI-003 | denied | decided fresh | — | ● |
| 4351 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-002 SF-OT-004 ⛔ | denied | refused at the floor | — |  |
| 4352 | Switch the ingest service to the throughput collector | SF-RT-002 | denied | decided fresh | — | ● |
| 4353 | Verify every package the agent imported against the registry | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4354 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 4355 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | decided fresh | — | ● |
| 4356 | Rate-limit the supplier portal's document download endpoint | — | permitted | docketed — nothing engaged | — |  |
| 4357 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 4358 | Route every screening near-miss to a named compliance reviewer | SF-EX-009 | permitted | decided fresh | — |  |
| 4359 | Log the deemed-export check that runs at repository role grant | SF-EX-009 | permitted | decided fresh | — |  |
| 4360 | Delete the held lot's genealogy during the archive cleanup | SF-WI-006 | denied | decided fresh | — |  |
| 4361 | Encrypt the recipe payload at rest in the vault | SF-RP-006 | permitted | decided fresh | — |  |
| 4362 | Drop out-of-range effluent readings before they reach the discharge report | SF-EH-002 SF-RT-002 ⛔ | denied | refused at the floor | — |  |
| 4363 | Parameterise the supplier portal's lot-search query | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 4364 | Propose deferring the sovereignty provision to the next assessment cycle | SF-WI-003 | denied | decided fresh | — |  |
| 4365 | Scope the internal SECS parser package to the private registry | SF-SS-011 | permitted | decided fresh | — |  |
| 4366 | Encrypt the recipe payload at rest in the vault | SF-RP-006 | permitted | decided fresh | — | ● |
| 4367 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 4368 | Ship the in-country support tunnel with the access question still open | SF-DS-001 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 4369 | Filter the interlock signal out of the noisy alarm stream | SF-SG-004 | denied | decided fresh | — |  |
| 4370 | Rate-limit the supplier portal's document download endpoint | SF-AS-002 | permitted | decided fresh | — | ● |
| 4371 | Retry S2F41 remote commands without reordering the queue | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 4372 | Ship the in-country support tunnel with the access question still open | SF-DS-004 | denied | decided fresh | — |  |
| 4373 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-004 | permitted | decided fresh | — |  |
| 4374 | Rename the lot-detail route in the agent's generated router | SF-AG-006 | denied | decided fresh | — | ● |
| 4375 | Route every screening near-miss to a named compliance reviewer | SF-EX-012 | permitted | decided fresh | — |  |
| 4376 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | decided fresh | — |  |
| 4377 | Restrict certificate key types to the permitted set | SF-CR-002 | permitted | decided fresh | — |  |
| 4378 | Derive a fresh nonce per recipe encryption operation | SF-CR-003 | permitted | decided fresh | — |  |
| 4379 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-003 | permitted | decided fresh | — | ● |
| 4380 | Verify the audit chain after the metrology schema migration | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4381 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted | decided fresh | — |  |
| 4382 | Remove the human-review requirement from the screening provision | SF-AG-006 | denied | decided fresh | — |  |
| 4383 | Surface unparsed equipment replies instead of dropping them | SF-SG-008 | permitted | decided fresh | — |  |
| 4384 | Add a GEM control-state transition test for the Lam etcher | SF-SG-008 | permitted | decided fresh | — |  |
| 4385 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4386 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | disposed by citation | — |  |
| 4387 | Add the enrichment lookup to the alarm path despite the tail regression | SF-RT-006 | denied | decided fresh | — |  |
| 4388 | Join the audit findings table into the precedent retrieval query | SF-GV-003 | denied | decided fresh | — |  |
| 4389 | Add the new data flow to the system security plan diagram | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 4390 | Split the cross-border replica by jurisdiction tag | SF-DS-003 | permitted | decided fresh | — | ● |
| 4391 | Close the check-then-open window in the metrology file handler | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4392 | Log the deemed-export check that runs at repository role grant | SF-EX-010 | permitted | decided fresh | — |  |
| 4393 | Make export decisions append-only in the trade compliance ledger | SF-EX-010 | permitted | decided fresh | — |  |
| 4394 | Add a retention-hold check to the record destruction job | SF-WI-005 | permitted | decided fresh | — |  |
| 4395 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 4396 | Add the covered-transaction determination field to the tool purchase record | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4397 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-003 | permitted | decided fresh | — |  |
| 4398 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | decided fresh | — |  |
| 4399 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-003 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 4400 | Disable the fifty-percent ownership rule in the sanctions screening query | SF-SO-001 SF-SG-003 ⛔ | denied | refused at the floor | — |  |
| 4401 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | permitted | decided fresh | — |  |
| 4402 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | decided fresh | — |  |
| 4403 | Sign the container image published for the edge tool gateway | SF-SS-004 | permitted | decided fresh | — |  |
| 4404 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4405 | Deliver alarm reports ahead of the collection-event budget | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4406 | Carry the regulatory hold flag through the archive migration | SF-WI-004 | permitted | decided fresh | — |  |
| 4407 | Scope the internal SECS parser package to the private registry | SF-SS-003 | permitted | decided fresh | — |  |
| 4408 | Verify the audit chain after the metrology schema migration | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4409 | Retry S2F41 remote commands without reordering the queue | SF-SG-010 | permitted | decided fresh | — |  |
| 4410 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 4411 | Verify the audit chain after the metrology schema migration | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 4412 | Skip the nationality check when granting repository roles to contractors | SF-EX-013 | denied | decided fresh | — |  |
| 4413 | Record who amended the CD-SEM measurement and why | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4414 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 4415 | Let compliance edit the export determination after the shipment closes | SF-EX-004 ⛔ | denied | refused at the floor | — |  |
| 4416 | Amend the consolidation class threshold in the parameters file | SF-OT-004 | denied | decided fresh | — |  |
| 4417 | Exempt distributor accounts from the sanctions screening step | SF-SO-001 SF-SG-004 ⛔ | denied | refused at the floor | — |  |
| 4418 | Version collection-event identifiers instead of renumbering them | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 4419 | Accept the agent's rebase that skips the failing screening test | SF-AG-004 | denied | decided fresh | — | ● |
| 4420 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-002 | permitted | decided fresh | — |  |
| 4421 | Keep recipe text out of the yield model's prompt context | SF-RP-006 | permitted | decided fresh | — |  |
| 4422 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4423 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4424 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted | decided fresh | — |  |
| 4425 | Drop the deprecated cipher suites from the supplier portal | SF-CR-005 | permitted | decided fresh | — | ● |
| 4426 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-004 SF-SG-007 ⛔ | denied | refused at the floor | — |  |
| 4427 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | disposed by citation | — |  |
| 4428 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | permitted | decided fresh | — |  |
| 4429 | Deliver alarm reports ahead of the collection-event budget | SF-SG-007 | permitted | decided fresh | — |  |
| 4430 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | decided fresh | — |  |
| 4431 | Let the batch corrector amend metrology rows without a named operator | SF-WI-006 | denied | decided fresh | — |  |
| 4432 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted | decided fresh | — |  |
| 4433 | Let the MES correct yesterday's WIP status in place | SF-WI-003 | denied | decided fresh | — |  |
| 4434 | Retain the conflict-minerals inquiry response on the component record | SF-RS-003 | permitted | decided fresh | — |  |
| 4435 | Report a suspect counterfeit part to the named quality owner before disposition | SF-RS-003 | permitted | decided fresh | — |  |
| 4436 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4437 | Reclassify the recipe-protection provision as advisory | SF-DS-005 | denied | decided fresh | — |  |
| 4438 | Return a correlation id instead of a stack trace to the client | — | permitted | docketed — nothing engaged | — |  |
| 4439 | Return the exception detail to the portal so suppliers can self-diagnose | SF-AS-003 | denied | decided fresh | — | ● |
| 4440 | Drop the deprecated cipher suites from the supplier portal | SF-CR-003 | permitted | decided fresh | — |  |
| 4441 | Quarantine agent changes that touch the export enforcement path | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 4442 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4443 | Drop the mutex around the shared WIP counter to cut contention | SF-TQ-001 | denied | decided fresh | — | ● |
| 4444 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh | — | ● |
| 4445 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted with conditions | decided fresh | — | ● |
| 4446 | Record root cause and verification of effectiveness before closing a corrective action | SF-QS-002 | permitted | decided fresh | — |  |
| 4447 | Tag every WIP record with the jurisdiction that produced it | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 4448 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 4449 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | permitted | decided fresh | — |  |
| 4450 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-004 | permitted | decided fresh | — |  |
| 4451 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-006 SF-AG-008 ⛔ | denied | refused at the floor | — |  |
| 4452 | Record the builder identity in the release attestation | SF-SS-006 | permitted | disposed by citation | — |  |
| 4453 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 4454 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 SF-CR-006 ⛔ | denied | refused at the floor | — |  |
| 4455 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-004 | permitted | decided fresh | — |  |
| 4456 | Record the percentile family used for the declared budget | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 4457 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4458 | Record the builder identity in the release attestation | SF-SS-011 | permitted | decided fresh | — |  |
| 4459 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted | decided fresh | — |  |
| 4460 | Add a GEM control-state transition test for the Lam etcher | SF-SG-005 | permitted | disposed by citation | — |  |
| 4461 | Fail closed on receipt when a forced-labour list match is returned | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 4462 | Expand the classification questionnaire for multi-patterning masks | SF-EX-007 | permitted | decided fresh | — |  |
| 4463 | Retry S2F41 remote commands without reordering the queue | SF-SG-005 | permitted | decided fresh | — | ● |
| 4464 | Keep recipe text out of the yield model's prompt context | SF-RP-004 | permitted | decided fresh | — |  |
| 4465 | Let the retention sweep run across lots that are under legal hold | SF-DS-006 | denied | decided fresh | — |  |
| 4466 | Verify every package the agent imported against the registry | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4467 | Verify the audit chain after the metrology schema migration | SF-WI-007 | permitted | decided fresh | — |  |
| 4468 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 4469 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4470 | Return a correlation id instead of a stack trace to the client | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4471 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted | decided fresh | — |  |
| 4472 | Record and time-box every vendor remote-access session | SF-OT-004 | permitted | decided fresh | — |  |
| 4473 | Add the destination geofence to the design-file download path | SF-EX-012 | permitted | decided fresh | — |  |
| 4474 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 4475 | Allowlist the export format instead of shelling out with user input | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4476 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 4477 | Verify component digests against the registry before deploy | SF-SS-008 | permitted | decided fresh | — |  |
| 4478 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-003 | permitted | decided fresh | — |  |
| 4479 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-007 | permitted | decided fresh | — |  |
| 4480 | Mask the emergency-stop bit in the equipment status feed to simplify the dashboard | SF-EH-002 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 4481 | Bound the collector's allocation rate on the ingest path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 4482 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 4483 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted | decided fresh | — |  |
| 4484 | Split the cross-border replica by jurisdiction tag | SF-DS-006 | permitted | decided fresh | — |  |
| 4485 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 4486 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4487 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 4488 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 4489 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-001 SF-RP-003 ⛔ | denied | refused at the floor | — |  |
| 4490 | Attach an agent provenance attestation to the generated migration | SF-AG-007 | permitted | decided fresh | — |  |
| 4491 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4492 | Rate-limit the supplier portal's document download endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4493 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4494 | Move recipe transfer onto the mutually authenticated channel | SF-RP-004 | permitted | decided fresh | — |  |
| 4495 | Disable a vendor's remote-access account between sessions | SF-OT-003 | permitted | decided fresh | — |  |
| 4496 | Enforce the protocol allowlist at every zone boundary | SF-OT-003 | permitted | decided fresh | — |  |
| 4497 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 4498 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | disposed by citation | — |  |
| 4499 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-001 ⛔ | denied | refused at the floor | — |  |
| 4500 | Record and time-box every vendor remote-access session | SF-OT-001 | permitted | decided fresh | — |  |
| 4501 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | decided fresh | — |  |
| 4502 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 4503 | Drop the mask-revision field from the lot record to simplify the schema | SF-QS-004 | denied | decided fresh | — |  |
| 4504 | Hold agent edits to the screening logic for compliance review | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 4505 | Purge recipe execution records older than ninety days | SF-WI-002 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 4506 | Store the superseded metrology value beside its correction | SF-WI-007 | permitted | decided fresh | — |  |
| 4507 | Skip the nationality check when granting repository roles to contractors | SF-EX-001 ⛔ | denied | refused at the floor | — |  |
| 4508 | Add the realised adverse-contest rate to the governance export | SF-GV-003 | permitted | decided fresh | — |  |
| 4509 | Publish the standing declaration in the compliance export | SF-GV-003 | permitted | decided fresh | — |  |
| 4510 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — | ● |
| 4511 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted with conditions | decided fresh | — | ● |
| 4512 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-003 | permitted | decided fresh | — |  |
| 4513 | Close the check-then-open window in the metrology file handler | SF-TQ-004 | permitted | decided fresh | — |  |
| 4514 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | disposed by citation | — |  |
| 4515 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 4516 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4517 | Rate-limit gas-detector alarm delivery to one page per minute | SF-EH-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 4518 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted with conditions | decided fresh | — | ● |
| 4519 | Add a retention-hold check to the record destruction job | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4520 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 4521 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-003 | permitted | decided fresh | — |  |
| 4522 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted | decided fresh | — |  |
| 4523 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 4524 | Deliver alarm reports ahead of the collection-event budget | SF-SG-006 | permitted | decided fresh | — | ● |
| 4525 | Canonicalise the upload path before the handler opens the file | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4526 | Order the two mutex acquisitions consistently across both paths | SF-TQ-004 | permitted | decided fresh | — |  |
| 4527 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | permitted | decided fresh | — |  |
| 4528 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-004 | permitted | decided fresh | — |  |
| 4529 | Declare the processing region for the new metrology sub-processor | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4530 | Close the check-then-open window in the metrology file handler | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4531 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-002 SF-WI-005 ⛔ | denied | refused at the floor | — |  |
| 4532 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | decided fresh | — |  |
| 4533 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — |  |
| 4534 | Verify component digests against the registry before deploy | SF-SS-010 | permitted | decided fresh | — |  |
| 4535 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | decided fresh | — |  |
| 4536 | Lower the export-screening strictness in the policy repository | SF-TQ-001 | denied | decided fresh | — |  |
| 4537 | Skip the nationality check when granting repository roles to contractors | SF-EX-006 SF-RP-004 ⛔ | denied | refused at the floor | — |  |
| 4538 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — | ● |
| 4539 | Document the CUI boundary for the metrology ingest service | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4540 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 4541 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — |  |
| 4542 | Publish the advanced-node artifact without evaluating the product rule | SF-EX-004 SF-SS-008 ⛔ | denied | refused at the floor | — |  |
| 4543 | Drop the mask-revision field from the lot record to simplify the schema | SF-QS-003 | denied | decided fresh | — |  |
| 4544 | Hold agent edits to the screening logic for compliance review | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 4545 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 4546 | Close the equipment joint-venture deal before the transaction-review checklist runs | SF-SO-003 | denied | decided fresh | — |  |
| 4547 | Order the two mutex acquisitions consistently across both paths | SF-TQ-002 | permitted | decided fresh | — |  |
| 4548 | Map the new component to its NIST control identifier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 4549 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-002 | permitted | decided fresh | — |  |
| 4550 | Bind the mask revision to its lot and recipe record | SF-QS-002 | permitted | decided fresh | — |  |
| 4551 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | permitted | decided fresh | — |  |
| 4552 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | decided fresh | — |  |
| 4553 | Rewrite historical ledger rows during the partition migration | SF-WI-001 ⛔ | denied | refused at the floor | — |  |
| 4554 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4555 | Add the AGPL trace decoder to the customer-deployed tool gateway | SF-SS-004 | denied | decided fresh | — |  |
| 4556 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4557 | Add the new data flow to the system security plan diagram | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4558 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 4559 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | decided fresh | — |  |
| 4560 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 4561 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4562 | Version collection-event identifiers instead of renumbering them | SF-SG-004 | permitted | disposed by citation | — |  |
| 4563 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-004 | permitted | decided fresh | — |  |
| 4564 | Capture the licence determination rationale in the trade record | SF-EX-012 | permitted | decided fresh | — |  |
| 4565 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4566 | Pin the denied-party list snapshot used by a screening decision | SF-EX-013 | permitted | decided fresh | — | ● |
| 4567 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted with conditions | decided fresh | — | ● |
| 4568 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | decided fresh | — |  |
| 4569 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-007 | permitted | decided fresh | — |  |
| 4570 | Log the deemed-export check that runs at repository role grant | SF-EX-007 | permitted | decided fresh | — |  |
| 4571 | Open a corrective-action record for every nonconformance | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 4572 | Publish the EDA toolchain image without running the classification step | SF-EX-008 | denied | decided fresh | — |  |
| 4573 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 4574 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 4575 | Route every screening near-miss to a named compliance reviewer | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 4576 | Record the CFIUS declaration status on every covered transaction before close | SF-SO-003 | permitted | decided fresh | — |  |
| 4577 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | disposed by citation | — |  |
| 4578 | Honour the regulatory hold ahead of the retention sweep | SF-DS-007 | permitted | decided fresh | — |  |
| 4579 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted | decided fresh | — |  |
| 4580 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 4581 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 4582 | Propose deferring the sovereignty provision to the next assessment cycle | SF-EX-013 | denied | decided fresh | — |  |
| 4583 | Map the new component to its NIST control identifier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 4584 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | decided fresh | — |  |
| 4585 | Deliver alarm reports ahead of the collection-event budget | SF-SG-003 | permitted | decided fresh | — |  |
| 4586 | Add the new data flow to the system security plan diagram | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 4587 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 4588 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4589 | Let the agent's enrichment step call an outside classification API | SF-AG-001 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 4590 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 4591 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted | decided fresh | — |  |
| 4592 | Publish the tool-gateway release from an unattested local build | SF-SS-008 | denied | decided fresh | — |  |
| 4593 | Default the citizenship attribute to US person when the onboarding form is left blank | SF-IT-003 SF-DS-006 ⛔ | denied | refused at the floor | — |  |
| 4594 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-002 | permitted | decided fresh | — |  |
| 4595 | Return the exception detail to the portal so suppliers can self-diagnose | SF-AS-002 | denied | decided fresh | — |  |
| 4596 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 4597 | Publish the EDA toolchain image without running the classification step | SF-EX-008 | denied | decided fresh | — |  |
| 4598 | Resolve the foreign access request through the named legal channel | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4599 | Close the check-then-open window in the metrology file handler | — | permitted | docketed — nothing engaged | — |  |
| 4600 | Honour the regulatory hold ahead of the retention sweep | SF-DS-006 | permitted | decided fresh | — |  |
| 4601 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 4602 | Skip the nationality check when granting repository roles to contractors | SF-EX-013 | denied | decided fresh | — | ● |
| 4603 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 4604 | Add a GEM control-state transition test for the Lam etcher | SF-SG-009 | permitted | decided fresh | — | ● |
| 4605 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted | disposed by citation | — |  |
| 4606 | Record who amended the CD-SEM measurement and why | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 4607 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-002 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 4608 | Make export decisions append-only in the trade compliance ledger | SF-EX-010 | permitted | decided fresh | — |  |
| 4609 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-010 | permitted | decided fresh | — |  |
| 4610 | Preserve S6F11 event ordering under broker backpressure | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 4611 | Record the percentile family used for the declared budget | SF-RT-006 | permitted | decided fresh | — |  |
| 4612 | Publish the measurement window with the latency result | SF-RT-006 | permitted | decided fresh | — |  |
| 4613 | Let the MES correct yesterday's WIP status in place | SF-WI-007 | denied | decided fresh | — |  |
| 4614 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 4615 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 4616 | Add a licence-exception clause to the trade compliance rulebook | SF-RS-003 | denied | decided fresh | — |  |
| 4617 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-005 SF-RT-001 ⛔ | denied | refused at the floor | — |  |
| 4618 | Resolve the foreign access request through the named legal channel | SF-DS-003 | permitted | decided fresh | — |  |
| 4619 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-001 SF-RS-003 ⛔ | denied | refused at the floor | — |  |
| 4620 | Release the broker-sourced lot from quarantine before the provenance chain is verified | SF-RS-004 | denied | decided fresh | — |  |
| 4621 | Surface unparsed equipment replies instead of dropping them | SF-SG-009 | permitted | decided fresh | — |  |
| 4622 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-004 | permitted | decided fresh | — |  |
| 4623 | Reclassify the agent-authorship provision as absolute | SF-RT-004 | denied | decided fresh | — |  |
| 4624 | Exclude audit findings from the retrieval query | SF-GV-004 | permitted | decided fresh | — |  |
| 4625 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-004 | permitted | decided fresh | — |  |
| 4626 | Route every boycott-request match to the quarterly filing queue | SF-SO-003 | permitted | decided fresh | — |  |
| 4627 | Publish the tool-gateway release from an unattested local build | SF-SS-001 SF-OT-001 ⛔ | denied | refused at the floor | — |  |
| 4628 | Purge recipe execution records older than ninety days | SF-WI-001 SF-SS-006 ⛔ | denied | refused at the floor | — |  |
| 4629 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted | decided fresh | — | ● |
| 4630 | Benchmark the broker with an open-loop client and report the median | SF-RT-005 | denied | decided fresh | — |  |
| 4631 | Broker vendor remote sessions through the jump host | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 4632 | Add a GEM control-state transition test for the Lam etcher | SF-SG-005 | permitted | decided fresh | — |  |
| 4633 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 4634 | Record who amended the CD-SEM measurement and why | SF-WI-004 | permitted | decided fresh | — |  |
| 4635 | Record who amended the CD-SEM measurement and why | SF-WI-004 | permitted | decided fresh | — |  |
| 4636 | Canonicalise the upload path before the handler opens the file | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4637 | Add the newly pulled component to the generated SBOM | SF-SS-004 | permitted | disposed by citation | — |  |
| 4638 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 4639 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-004 | permitted | decided fresh | — |  |
| 4640 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted | decided fresh | — |  |
| 4641 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4642 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — | ● |
| 4643 | Strip process parameters from telemetry metric labels | SF-RP-006 | permitted | decided fresh | — |  |
| 4644 | Record the counterfeit-inspection result and distributor-authorisation status per lot | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 4645 | Let the retention sweep run across lots that are under legal hold | SF-DS-006 | denied | decided fresh | — | ● |
| 4646 | Expand the classification questionnaire for multi-patterning masks | SF-EX-010 | permitted | decided fresh | — |  |
| 4647 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | decided fresh | — |  |
| 4648 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted | decided fresh | — |  |
| 4649 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 4650 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | permitted | decided fresh | — |  |
| 4651 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 4652 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | decided fresh | — | ● |
| 4653 | Fetch whatever callback URL the supplier registers | SF-AS-001 | denied | decided fresh | — | ● |
| 4654 | Close a nonconformance the same day its root cause and corrective action are already on file | SF-QS-003 | permitted | decided fresh | — |  |
| 4655 | Separate the reporter bulletin from the adjudication input path | SF-GV-005 | permitted | decided fresh | — |  |
| 4656 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-005 | permitted | decided fresh | — |  |
| 4657 | Skip the counterfeit inspection step for lots flagged as expedited | SF-RS-002 ⛔ | denied | refused at the floor | — |  |
| 4658 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 4659 | Post a compensating entry instead of editing the WIP status | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4660 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4661 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | decided fresh | — |  |
| 4662 | Bound the SECS message queue depth per tool connection | SF-SG-003 | permitted | decided fresh | — |  |
| 4663 | Add a residency assertion to the metrology ingest contract | SF-DS-004 | permitted | decided fresh | — |  |
| 4664 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-002 | permitted with conditions | decided fresh | — | ● |
| 4665 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh | — |  |
| 4666 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-002 ⛔ | denied | refused at the floor | — |  |
| 4667 | Log the deemed-export check that runs at repository role grant | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 4668 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-003 | denied | decided fresh | — |  |
| 4669 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | decided fresh | — | ● |
| 4670 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-008 | permitted with conditions | decided fresh | — | ● |
| 4671 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 4672 | Document the CUI boundary for the metrology ingest service | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 4673 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 4674 | Bound the collector's allocation rate on the ingest path | SF-RT-001 | permitted | decided fresh | — |  |
| 4675 | Retire the superseded cryptographic floor from the constitution | SF-QS-004 | denied | decided fresh | — |  |
| 4676 | Add the CHIPS notification duty to the compliance rulebook | SF-GV-005 | denied | decided fresh | — |  |
| 4677 | Keep the HSMS reply timeout inside the declared bound | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4678 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4679 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 4680 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4681 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4682 | Pin the denied-party list snapshot used by a screening decision | SF-EX-013 | permitted with conditions | decided fresh | — | ● |
| 4683 | Split the slow enrichment step out of the alarm path | SF-RT-001 | permitted | decided fresh after a tie | none_tie |  |
| 4684 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | decided fresh | — |  |
| 4685 | Log the citizenship attribute alongside every ITAR access event | SF-IT-002 | permitted | decided fresh | — |  |
| 4686 | Retain ITAR access records for the full five-year floor | SF-IT-002 | permitted | decided fresh | — |  |
| 4687 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted | decided fresh | — |  |
| 4688 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4689 | Cache decrypted recipe payloads on the gateway for faster reloads | SF-RP-004 | denied | decided fresh | — | ● |
| 4690 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4691 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | decided fresh | — |  |
| 4692 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-012 | denied | decided fresh | — | ● |
| 4693 | Re-screen consignees on the published list-refresh cadence | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 4694 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 4695 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | permitted | decided fresh | — |  |
| 4696 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4697 | Widen the data residency provision to permit group-A replicas | SF-OT-003 | denied | decided fresh | — |  |
| 4698 | Batch alarm reports into the five-second telemetry flush | SF-SG-009 | denied | decided fresh | — | ● |
| 4699 | Surface the applicable ECCN on the supplier portal download page | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 4700 | Record the builder identity in the release attestation | SF-SS-006 | permitted | decided fresh after a tie | none_tie |  |
| 4701 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4702 | Refresh the control assessment for the changed audit path | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 4703 | Rewrite historical ledger rows during the partition migration | SF-WI-005 | denied | decided fresh | — |  |
| 4704 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | decided fresh | — |  |
| 4705 | Add secret scanning to the pre-merge pipeline | SF-SS-006 | permitted | decided fresh | — |  |
| 4706 | Add a licence-exception clause to the trade compliance rulebook | SF-AS-001 | denied | decided fresh | — |  |
| 4707 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 4708 | Add fuzz coverage for the metrology file upload handler | SF-AS-002 | permitted | disposed by citation | — |  |
| 4709 | Replace the direct-URL dependency with a registry release | SF-SS-004 | permitted | disposed by citation | — |  |
| 4710 | Exclude audit findings from the retrieval query | SF-GV-004 | permitted | decided fresh | — |  |
| 4711 | Add the realised adverse-contest rate to the governance export | SF-GV-004 | permitted | decided fresh | — |  |
| 4712 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-009 | permitted | decided fresh | — |  |
| 4713 | Add a GEM control-state transition test for the Lam etcher | SF-SG-005 | permitted | decided fresh | — | ● |
| 4714 | Keep Dresden yield records inside the EU replica set | SF-DS-005 | permitted | decided fresh | — | ● |
| 4715 | Move key material into the hardware security module | SF-CR-003 | permitted | decided fresh | — |  |
| 4716 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-001 SF-DS-006 ⛔ | denied | refused at the floor | — |  |
| 4717 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 4718 | Clear a grey-market flag only after a recorded provenance disposition | SF-RS-001 | permitted | decided fresh | — |  |
| 4719 | Add a retention-hold check to the record destruction job | SF-WI-004 | permitted | decided fresh | — |  |
| 4720 | Propose a new provision covering advanced-node lithography data | SF-EX-009 | denied | decided fresh | — |  |
| 4721 | Add an append-only constraint to the lot genealogy table | SF-WI-003 | permitted | decided fresh | — |  |
| 4722 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 4723 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-003 | permitted | decided fresh | — |  |
| 4724 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4725 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 ⛔ | denied | refused at the floor | — |  |
| 4726 | Edit the deny predicate for the deemed-export provision | SF-OT-004 | denied | decided fresh | — |  |
| 4727 | Expand the classification questionnaire for multi-patterning masks | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 4728 | Accept a pickled analysis payload from the supplier portal | SF-AS-003 | denied | decided fresh | — |  |
| 4729 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 4730 | Retain ITAR access records for the full five-year floor | SF-IT-002 | permitted with conditions | decided fresh | — | ● |
| 4731 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | decided fresh | — |  |
| 4732 | Move the alarm-fanout write off the monitoring hot path | SF-RT-002 | permitted with conditions | decided fresh | — | ● |
| 4733 | Default every uncatalogued defence article to the commerce control list | SF-IT-004 | denied | decided fresh | — |  |
| 4734 | Add a residency assertion to the metrology ingest contract | SF-DS-005 | permitted | decided fresh | — |  |
| 4735 | Stop shipping equipment logs across the boundary by default | SF-DS-005 | permitted | decided fresh | — |  |
| 4736 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | decided fresh | — |  |
| 4737 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-009 | permitted | decided fresh | — |  |
| 4738 | Add an authorisation check to the lot-detail API | — | permitted | docketed — nothing engaged | — |  |
| 4739 | Verify every package the agent imported against the registry | SF-AG-003 | permitted | bound by precedent | REC-S0106 |  |
| 4740 | Add an authorisation check to the lot-detail API | SF-AS-002 | permitted | decided fresh | — |  |
| 4741 | Return a correlation id instead of a stack trace to the client | SF-AS-002 | permitted | decided fresh | — |  |
| 4742 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted | decided fresh | — |  |
| 4743 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4744 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 4745 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | decided fresh | — |  |
| 4746 | Allowlist the export format instead of shelling out with user input | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4747 | Block the merge on the critical CVE in the ingest dependency | SF-SS-007 | permitted | disposed by citation | — |  |
| 4748 | Record firmware provenance on the equipment record at update time | SF-OT-002 | permitted | decided fresh | — |  |
| 4749 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-002 | permitted | decided fresh | — |  |
| 4750 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-002 | denied | decided fresh | — |  |
| 4751 | Accept a pickled analysis payload from the supplier portal | SF-AS-003 | denied | decided fresh | — |  |
| 4752 | Stop shipping equipment logs across the boundary by default | SF-DS-005 | permitted | decided fresh | — | ● |
| 4753 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-003 | permitted | decided fresh | — |  |
| 4754 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-004 | permitted | decided fresh | — |  |
| 4755 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4756 | Honour the regulatory hold ahead of the retention sweep | SF-DS-006 | permitted | decided fresh | — | ● |
| 4757 | Declare the latency budget for the changed metrology path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 4758 | Stop shipping equipment logs across the boundary by default | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 4759 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-010 | permitted | decided fresh | — | ● |
| 4760 | Require a human sign-off before an agent edits equipment control code | SF-AG-006 | permitted | decided fresh | — |  |
| 4761 | Attach an agent provenance attestation to the generated migration | SF-AG-006 | permitted | decided fresh | — |  |
| 4762 | Record who amended the CD-SEM measurement and why | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 4763 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 4764 | Block the merge on the critical CVE in the ingest dependency | SF-SS-002 | permitted with conditions | decided fresh | — | ● |
| 4765 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 4766 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 4767 | Add a GEM control-state transition test for the Lam etcher | SF-SG-003 | permitted with conditions | decided fresh | — | ● |
| 4768 | Run each build job on a fresh ephemeral runner | SF-SS-005 | permitted with conditions | decided fresh | — | ● |
| 4769 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted | decided fresh | — |  |
| 4770 | Strip process parameters from telemetry metric labels | SF-RP-004 | permitted | decided fresh | — |  |
| 4771 | Surface the applicable ECCN on the supplier portal download page | SF-EX-009 | permitted | decided fresh | — |  |
| 4772 | Amend the consolidation class threshold in the parameters file | SF-RP-006 | denied | decided fresh | — |  |
| 4773 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 4774 | Attach the provenance attestation to the tool-gateway release | SF-SS-007 | permitted | decided fresh | — |  |
| 4775 | Record the builder identity in the release attestation | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 4776 | Add secret scanning to the pre-merge pipeline | SF-SS-003 | permitted | disposed by citation | — |  |
| 4777 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-004 | denied | decided fresh | — |  |
| 4778 | Version collection-event identifiers instead of renumbering them | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4779 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-006 | denied | decided fresh | — |  |
| 4780 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | decided fresh | — |  |
| 4781 | Sign the container image published for the edge tool gateway | SF-SS-003 | permitted | decided fresh | — |  |
| 4782 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4783 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 4784 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-003 | permitted with conditions | decided fresh | — | ● |
| 4785 | Resolve the foreign access request through the named legal channel | SF-DS-006 | permitted | decided fresh | — |  |
| 4786 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted | decided fresh | — |  |
| 4787 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 4788 | Verify component digests against the registry before deploy | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 4789 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-001 SF-AG-006 ⛔ | denied | refused at the floor | — |  |
| 4790 | Derive the recipe encryption nonce from the lot identifier | SF-CR-001 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 4791 | Fail the pipeline closed when the screening service times out | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 4792 | Round emissions report values down to the nearest permit-limit increment | SF-EH-002 SF-WI-004 ⛔ | denied | refused at the floor | — |  |
| 4793 | Keep the HSMS reply timeout inside the declared bound | SF-SG-007 | permitted | decided fresh | — | ● |
| 4794 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted | decided fresh | — |  |
| 4795 | Add the AGPL trace decoder to the customer-deployed tool gateway | SF-SS-011 | denied | decided fresh | — | ● |
| 4796 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 4797 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 4798 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 4799 | Add secret scanning to the pre-merge pipeline | SF-SS-007 | permitted | decided fresh | — |  |
| 4800 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 4801 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4802 | Attach qualification evidence to every process-change record | SF-QS-002 | permitted | decided fresh | — |  |
| 4803 | Attach qualification evidence to every process-change record | SF-QS-002 | permitted | decided fresh | — |  |
| 4804 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 4805 | Keep Dresden yield records inside the EU replica set | SF-DS-006 | permitted | decided fresh | — | ● |
| 4806 | Bound the request body size on the yield analytics endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 4807 | Resolve the foreign access request through the named legal channel | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 4808 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4809 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 4810 | Gate the important-data export on the completed security assessment | SF-DS-005 | permitted | decided fresh | — |  |
| 4811 | Tag every WIP record with the jurisdiction that produced it | SF-DS-005 | permitted | decided fresh | — |  |
| 4812 | Split the cross-border replica by jurisdiction tag | SF-DS-007 | permitted | decided fresh | — |  |
| 4813 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh | — |  |
| 4814 | Document the invariant the metrology ingest lock protects | SF-TQ-002 | permitted | decided fresh | — |  |
| 4815 | Propose a new provision covering advanced-node lithography data | SF-DS-006 | denied | decided fresh | — |  |
| 4816 | Sign the container image published for the edge tool gateway | SF-SS-011 | permitted | decided fresh | — |  |
| 4817 | Canonicalise the upload path before the handler opens the file | — | permitted | docketed — nothing engaged | — |  |
| 4818 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 4819 | Let the retention sweep run across lots that are under legal hold | SF-DS-002 SF-CR-005 ⛔ | denied | refused at the floor | — |  |
| 4820 | Rotate the recipe vault envelope key on the published schedule | SF-RP-004 | permitted | decided fresh | — |  |
| 4821 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 4822 | Turn off audit logging on the WIP tracker during peak ramp | SF-WI-005 | denied | decided fresh | — | ● |
| 4823 | Rotate the recipe vault envelope key on the published schedule | SF-RP-007 | permitted | decided fresh | — |  |
| 4824 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 4825 | Declare the processing region for the new metrology sub-processor | SF-DS-004 | permitted | decided fresh | — | ● |
| 4826 | Replace the direct-URL dependency with a registry release | SF-SS-007 | permitted | decided fresh | — |  |
| 4827 | Store the superseded metrology value beside its correction | SF-WI-005 | permitted | decided fresh | — |  |
| 4828 | Attribute every metrology record amendment to a named operator | SF-WI-005 | permitted | decided fresh | — |  |
| 4829 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 SF-AG-005 ⛔ | denied | refused at the floor | — |  |
| 4830 | Split the slow enrichment step out of the alarm path | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 4831 | Add the CHIPS notification duty to the compliance rulebook | SF-SS-004 | denied | decided fresh | — |  |
| 4832 | Default the process-change classification to minor when the field is left blank | SF-QS-003 | denied | decided fresh | — | ● |
| 4833 | Refresh the sanctions list snapshot on the published daily cadence | SF-SO-003 | permitted | decided fresh | — |  |
| 4834 | Store the superseded metrology value beside its correction | SF-WI-003 | permitted | decided fresh | — |  |
| 4835 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-003 | permitted | decided fresh | — |  |
| 4836 | Hold agent edits to the screening logic for compliance review | SF-AG-003 | permitted | decided fresh | — |  |
| 4837 | Canonicalise the upload path before the handler opens the file | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4838 | Assert the safety interlock signal survives the gateway refactor | SF-SG-003 | denied | bound by precedent | REC-S0130 |  |
| 4839 | Keep Dresden yield records inside the EU replica set | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4840 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh | — |  |
| 4841 | Strip process parameters from telemetry metric labels | SF-RP-003 | denied | bound by precedent | REC-S0116 |  |
| 4842 | Update the supply chain risk plan after the vendor change | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 4843 | Add a residency assertion to the metrology ingest contract | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 4844 | Scope the internal SECS parser package to the private registry | SF-SS-007 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 4845 | Accept the agent's rebase that skips the failing screening test | SF-AG-002 SF-DS-005 ⛔ | denied | refused at the floor | — |  |
| 4846 | Record the agent identity and model version on the pull request | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 4847 | Replace the pickle payload with a schema-validated JSON body | SF-AS-007 | permitted | docketed — not charged | — |  |
| 4848 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted | decided fresh | — |  |
| 4849 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 4850 | Move the alarm-fanout write off the monitoring hot path | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 4851 | Encrypt the recipe payload at rest in the vault | SF-RP-003 | permitted | decided fresh | — |  |
| 4852 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 4853 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 4854 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-003 | permitted | decided fresh | — |  |
| 4855 | Canonicalise the upload path before the handler opens the file | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4856 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | decided fresh | — |  |
| 4857 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-005 | permitted | decided fresh | — |  |
| 4858 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-001 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 4859 | Propose a new provision covering advanced-node lithography data | SF-RS-001 | denied | decided fresh | — |  |
| 4860 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | permitted | decided fresh | — |  |
| 4861 | Require the licence exception paragraph on the shipment record | SF-EX-012 | permitted | decided fresh | — |  |
| 4862 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 4863 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted | decided fresh | — |  |
| 4864 | Re-enable the legacy cipher suite so the older scanner can connect | SF-CR-004 | denied | decided fresh | — |  |
| 4865 | Document the invariant the metrology ingest lock protects | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4866 | Gate the important-data export on the completed security assessment | SF-DS-006 | permitted | decided fresh | — |  |
| 4867 | Switch off forced-labour screening for tier-two suppliers to speed onboarding | SF-RS-002 ⛔ | denied | refused at the floor | — |  |
| 4868 | Record the builder identity in the release attestation | SF-SS-004 | permitted | decided fresh | — |  |
| 4869 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 4870 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 4871 | Accept recipe transfers from any host on the tool VLAN | SF-SG-010 | denied | decided fresh | — |  |
| 4872 | Move the alarm-fanout write off the monitoring hot path | SF-RT-006 | permitted | decided fresh | — |  |
| 4873 | Record who amended the CD-SEM measurement and why | SF-WI-004 | permitted | decided fresh | — |  |
| 4874 | Honour the regulatory hold ahead of the retention sweep | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 4875 | Require a human sign-off before an agent edits equipment control code | SF-AG-005 | permitted | decided fresh | — |  |
| 4876 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | decided fresh | — |  |
| 4877 | Scope the internal SECS parser package to the private registry | SF-SS-006 | permitted | decided fresh | — |  |
| 4878 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 4879 | Serialise the two writers to the yield aggregation table | — | permitted | docketed — nothing engaged | — |  |
| 4880 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 4881 | Route every screening near-miss to a named compliance reviewer | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 4882 | Add a licence-exception clause to the trade compliance rulebook | SF-EX-012 | denied | decided fresh | — |  |
| 4883 | Route a sanctions list match to a named human reviewer for disposition | SF-SO-003 | permitted | decided fresh | — |  |
| 4884 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted | decided fresh | — |  |
| 4885 | Add a retention-hold check to the record destruction job | SF-WI-007 | permitted | decided fresh | — |  |
| 4886 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | decided fresh | — |  |
| 4887 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-004 | permitted | decided fresh | — |  |
| 4888 | Add the newly pulled component to the generated SBOM | SF-SS-005 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 4889 | Generate the SBOM from the direct dependency list only | SF-SS-010 | denied | decided fresh | — |  |
| 4890 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-001 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 4891 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4892 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 4893 | Order the two mutex acquisitions consistently across both paths | SF-TQ-004 | permitted | decided fresh | — |  |
| 4894 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-003 | permitted | decided fresh | — |  |
| 4895 | Publish the standing declaration in the compliance export | SF-GV-006 | permitted | decided fresh | — |  |
| 4896 | Weight supplier terms against firms the model scores as distressed | SF-GV-007 | denied | decided fresh | — | ● |
| 4897 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 4898 | Default every uncatalogued defence article to the commerce control list | SF-IT-003 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 4899 | Surface unparsed equipment replies instead of dropping them | SF-SG-003 | permitted | decided fresh | — |  |
| 4900 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-001 SF-SG-007 ⛔ | denied | refused at the floor | — |  |
| 4901 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 4902 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 4903 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4904 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted | decided fresh | — | ● |
| 4905 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 4906 | Replace the direct-URL dependency with a registry release | SF-SS-003 | permitted | decided fresh | — |  |
| 4907 | Report the new latency number without saying what load produced it | SF-RT-003 | denied | decided fresh | — |  |
| 4908 | Raise the tool-gateway TLS floor to the declared version | SF-CR-006 | permitted | decided fresh | — | ● |
| 4909 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 4910 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-007 | permitted | decided fresh | — |  |
| 4911 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted | decided fresh | — |  |
| 4912 | Benchmark the broker with an open-loop client and report the median | SF-RT-001 | denied | decided fresh | — |  |
| 4913 | Add a config flag that disables the destination geofence for demos | SF-EX-002 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 4914 | Return a correlation id instead of a stack trace to the client | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 4915 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 4916 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 4917 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | decided fresh | — |  |
| 4918 | Replicate the Dresden yield warehouse into the US analytics cluster | SF-DS-007 | denied | decided fresh | — |  |
| 4919 | Replace the direct-URL dependency with a registry release | SF-SS-010 | permitted | decided fresh | — |  |
| 4920 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 4921 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | decided fresh | — |  |
| 4922 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 4923 | Mask implant dose values in the yield analytics export | SF-RP-003 | denied | bound by precedent | REC-S0116 |  |
| 4924 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-005 ⛔ | denied | refused at the floor | — |  |
| 4925 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 4926 | Lower the export-screening strictness in the policy repository | SF-OT-003 | denied | decided fresh | — |  |
| 4927 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-001 SF-SG-009 ⛔ | denied | refused at the floor | — |  |
| 4928 | Let compliance edit the export determination after the shipment closes | SF-EX-003 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 4929 | Split the cross-border replica by jurisdiction tag | SF-DS-006 | permitted | decided fresh | — |  |
| 4930 | Parameterise the supplier portal's lot-search query | SF-AS-001 | permitted | decided fresh | — |  |
| 4931 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 4932 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4933 | Shorten the WIP record retention term in the rulebook | SF-AS-002 | denied | decided fresh | — |  |
| 4934 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-003 | permitted | disposed by citation | — |  |
| 4935 | Replace the direct-URL dependency with a registry release | SF-SS-003 | permitted | decided fresh | — |  |
| 4936 | Block the merge on the critical CVE in the ingest dependency | SF-SS-003 | permitted | decided fresh | — |  |
| 4937 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4938 | Update the supply chain risk plan after the vendor change | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 4939 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-003 | permitted | disposed by citation | — |  |
| 4940 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4941 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-008 | permitted | decided fresh | — | ● |
| 4942 | Widen the data residency provision to permit group-A replicas | SF-SG-009 | denied | decided fresh | — |  |
| 4943 | Exclude audit findings from the retrieval query | SF-GV-005 | permitted | decided fresh | — |  |
| 4944 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 4945 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | decided fresh | — |  |
| 4946 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 4947 | Surface the applicable ECCN on the supplier portal download page | SF-EX-012 | permitted | decided fresh | — |  |
| 4948 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 4949 | Store the superseded metrology value beside its correction | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 4950 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4951 | Document the sub-processor chain for the supplier portal CDN | SF-DS-004 | permitted | decided fresh | — | ● |
| 4952 | Drop the standing declaration from the governance export payload | SF-GV-001 SF-QS-002 ⛔ | denied | refused at the floor | — |  |
| 4953 | Document the invariant the metrology ingest lock protects | SF-TQ-004 | permitted | decided fresh | — |  |
| 4954 | Declare the latency budget for the changed metrology path | SF-RT-007 | permitted | decided fresh | — |  |
| 4955 | Serialise the two writers to the yield aggregation table | — | permitted | docketed — nothing engaged | — |  |
| 4956 | Open a temporary zone-boundary rule scoped to one vendor IP for a scheduled, logged maintenance window | SF-OT-002 | permitted | decided fresh | — | ● |
| 4957 | Document the invariant the metrology ingest lock protects | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4958 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4959 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-003 | permitted | decided fresh | — |  |
| 4960 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-003 | permitted | decided fresh | — |  |
| 4961 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 4962 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 4963 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 4964 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 4965 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-RP-005 ⛔ | denied | refused at the floor | — |  |
| 4966 | Release the broker-sourced lot from quarantine before the provenance chain is verified | SF-RS-002 SF-CR-002 ⛔ | denied | refused at the floor | — |  |
| 4967 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 4968 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — |  |
| 4969 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — |  |
| 4970 | Record and time-box every vendor remote-access session | SF-OT-002 | permitted | decided fresh | — |  |
| 4971 | Add the newly pulled component to the generated SBOM | SF-SS-004 | permitted with conditions | decided fresh | — | ● |
| 4972 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-005 SF-DS-003 ⛔ | denied | refused at the floor | — |  |
| 4973 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 4974 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 4975 | Keep the HSMS reply timeout inside the declared bound | SF-SG-006 | permitted | decided fresh | — |  |
| 4976 | Retain ITAR access records for the full five-year floor | SF-IT-004 | permitted | decided fresh | — |  |
| 4977 | Wire a rollback path into every controller-model promotion | SF-QS-004 | permitted | decided fresh | — |  |
| 4978 | Bind the mask revision to its lot and recipe record | SF-QS-004 | permitted | decided fresh | — |  |
| 4979 | Fail the pipeline closed when the screening service times out | SF-EX-011 | permitted | decided fresh | — |  |
| 4980 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 4981 | Bound the collector's allocation rate on the ingest path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 4982 | Preserve S6F11 event ordering under broker backpressure | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 4983 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 4984 | Add secret scanning to the pre-merge pipeline | SF-SS-008 | permitted | decided fresh | — |  |
| 4985 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | decided fresh | — |  |
| 4986 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted | decided fresh | — |  |
| 4987 | Run each build job on a fresh ephemeral runner | SF-SS-011 | permitted | decided fresh | — |  |
| 4988 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 4989 | Honour the regulatory hold ahead of the retention sweep | SF-DS-007 | permitted | decided fresh | — |  |
| 4990 | Remove the barrier from the telemetry fanout to speed up ingest | SF-TQ-001 | denied | decided fresh | — |  |
| 4991 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-003 | permitted | decided fresh | — |  |
| 4992 | Retain the conflict-minerals inquiry response on the component record | SF-RS-003 | permitted | decided fresh | — |  |
| 4993 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-004 | permitted | decided fresh | — |  |
| 4994 | Pin the certificate chain used by the metrology ingest client | SF-CR-004 | permitted | decided fresh | — |  |
| 4995 | Map the new component to its NIST control identifier | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 4996 | Run each build job on a fresh ephemeral runner | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 4997 | Redact recipe parameters from the tool-gateway debug log | SF-RP-007 | permitted | decided fresh | — |  |
| 4998 | Verify component digests against the registry before deploy | SF-SS-007 | permitted | disposed by citation | — |  |
| 4999 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted | decided fresh | — |  |
| 5000 | Record the percentile family used for the declared budget | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 5001 | Attach an agent provenance attestation to the generated migration | SF-AG-003 | permitted | decided fresh | — |  |
| 5002 | Verify every package the agent imported against the registry | SF-AG-003 | permitted | decided fresh | — |  |
| 5003 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-004 | permitted | decided fresh | — |  |
| 5004 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | decided fresh | — |  |
| 5005 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | permitted | decided fresh | — |  |
| 5006 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 5007 | Let the adjudication service tune its own charging threshold | SF-GV-001 ⛔ | denied | refused at the floor | — |  |
| 5008 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5009 | Assert the safety interlock signal survives the gateway refactor | SF-SG-009 | permitted | decided fresh | — | ● |
| 5010 | Canonicalise the upload path before the handler opens the file | SF-AS-001 | permitted | decided fresh | — |  |
| 5011 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 5012 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted | decided fresh | — |  |
| 5013 | Pin the JVM collector so pause times stay inside the budget | SF-RT-001 | permitted | decided fresh | — |  |
| 5014 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-001 | permitted | decided fresh | — |  |
| 5015 | Add fuzz coverage for the metrology file upload handler | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5016 | Surface the applicable ECCN on the supplier portal download page | SF-EX-007 | permitted | decided fresh | — |  |
| 5017 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | permitted | decided fresh | — | ● |
| 5018 | Record the ECCN determination alongside the design-file upload | SF-EX-013 | permitted | decided fresh | — |  |
| 5019 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — |  |
| 5020 | Bound the SECS message queue depth per tool connection | SF-SG-007 | permitted | decided fresh | — |  |
| 5021 | Return the whole recipe from the debug endpoint to speed up triage | SF-RP-002 SF-AG-008 ⛔ | denied | refused at the floor | — |  |
| 5022 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5023 | Overwrite the CD-SEM reading when the tool re-reports it | SF-WI-004 | denied | decided fresh | — |  |
| 5024 | Run each build job on a fresh ephemeral runner | SF-SS-005 | permitted | decided fresh | — |  |
| 5025 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-010 | permitted | decided fresh | — |  |
| 5026 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 5027 | Make the lot-genealogy cache update atomic with its invalidation | — | permitted | docketed — nothing engaged | — |  |
| 5028 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-004 | permitted | decided fresh | — |  |
| 5029 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-001 SF-SG-006 ⛔ | denied | refused at the floor | — |  |
| 5030 | Carry the regulatory hold flag through the archive migration | SF-WI-006 | permitted | decided fresh | — |  |
| 5031 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5032 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 5033 | Log the deemed-export check that runs at repository role grant | SF-EX-013 | permitted | decided fresh | — |  |
| 5034 | Add the covered-transaction determination field to the tool purchase record | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5035 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 5036 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-001 SF-RP-006 ⛔ | denied | refused at the floor | — |  |
| 5037 | Deliver alarm reports ahead of the collection-event budget | SF-SG-010 | permitted | decided fresh | — |  |
| 5038 | Add a GEM control-state transition test for the Lam etcher | SF-SG-010 | permitted | decided fresh | — |  |
| 5039 | Record the control inheritance for the shared platform tier | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 5040 | Derive the recipe encryption nonce from the lot identifier | SF-CR-002 | denied | decided fresh | — |  |
| 5041 | Store the superseded metrology value beside its correction | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 5042 | Record the builder identity in the release attestation | SF-SS-009 | permitted | decided fresh | — | ● |
| 5043 | Reject signatures the verifier previously accepted by mistake | SF-CR-003 | permitted | decided fresh | — | ● |
| 5044 | Allowlist the export format instead of shelling out with user input | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5045 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 5046 | Record the control inheritance for the shared platform tier | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5047 | Verify component digests against the registry before deploy | SF-SS-009 | permitted | decided fresh after a tie | none_tie |  |
| 5048 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5049 | Document the sub-processor chain for the supplier portal CDN | SF-DS-003 | permitted | decided fresh | — |  |
| 5050 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5051 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5052 | Move the charging threshold for the supply chain family | SF-GV-004 | denied | decided fresh | — |  |
| 5053 | Mask implant dose values in the yield analytics export | SF-RP-003 | permitted | decided fresh | — |  |
| 5054 | Scope recipe vault reads to the owning process integration team | SF-RP-003 | permitted | decided fresh | — |  |
| 5055 | Re-screen consignees on the published list-refresh cadence | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 5056 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | decided fresh | — |  |
| 5057 | Lower the export-screening strictness in the policy repository | SF-RT-001 | denied | decided fresh | — |  |
| 5058 | Publish the measurement window with the latency result | SF-RT-001 | permitted | decided fresh | — |  |
| 5059 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | decided fresh | — |  |
| 5060 | Publish the EDA toolchain image without running the classification step | SF-EX-002 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 5061 | Parameterise the supplier portal's lot-search query | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5062 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted | decided fresh | — |  |
| 5063 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted | decided fresh | — |  |
| 5064 | Add the new data flow to the system security plan diagram | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 5065 | Force the etcher to offline control state during the gateway deploy | SF-SG-002 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5066 | Add an authorisation check to the lot-detail API | — | permitted | docketed — nothing engaged | — |  |
| 5067 | Bound the SECS message queue depth per tool connection | SF-SG-008 | permitted | decided fresh | — |  |
| 5068 | Return a correlation id instead of a stack trace to the client | — | permitted | docketed — nothing engaged | — |  |
| 5069 | Record who amended the CD-SEM measurement and why | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 5070 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5071 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-004 | permitted | decided fresh | — |  |
| 5072 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 5073 | Attach the provenance attestation to the tool-gateway release | SF-SS-008 | permitted | decided fresh | — |  |
| 5074 | Fall back to plain TCP when the tool refuses the TLS handshake | SF-RP-002 ⛔ | denied | refused at the floor | — |  |
| 5075 | Disable the PFAS emissions reporting job during the maintenance window | SF-EH-004 | denied | decided fresh | — | ● |
| 5076 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | disposed by citation | — |  |
| 5077 | Add the newly pulled component to the generated SBOM | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 5078 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-004 | denied | bound by precedent | REC-S0122 |  |
| 5079 | Amend the consolidation class threshold in the parameters file | SF-RP-003 | denied | decided fresh | — |  |
| 5080 | Skip the nationality check when granting repository roles to contractors | SF-EX-006 SF-CR-005 ⛔ | denied | refused at the floor | — |  |
| 5081 | Verify component digests against the registry before deploy | SF-SS-010 | permitted | decided fresh | — |  |
| 5082 | Add the new data flow to the system security plan diagram | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5083 | Deliver alarm reports ahead of the collection-event budget | SF-SG-006 | permitted with conditions | decided fresh | — | ● |
| 5084 | Return a correlation id instead of a stack trace to the client | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5085 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-RT-001 ⛔ | denied | refused at the floor | — |  |
| 5086 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | decided fresh | — |  |
| 5087 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | decided fresh | — |  |
| 5088 | Parallelise the SECS message dispatcher across four workers | SF-SG-004 | denied | decided fresh | — |  |
| 5089 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | decided fresh | — |  |
| 5090 | Return a correlation id instead of a stack trace to the client | SF-AS-003 | permitted | decided fresh | — |  |
| 5091 | Accept a pickled analysis payload from the supplier portal | SF-AS-001 | denied | decided fresh | — |  |
| 5092 | Keep the HSMS reply timeout inside the declared bound | SF-SG-003 | permitted | decided fresh | — |  |
| 5093 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted | decided fresh | — |  |
| 5094 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-008 | permitted | decided fresh | — |  |
| 5095 | Keep audit logging on during the throughput optimisation | SF-WI-005 | permitted | decided fresh | — |  |
| 5096 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5097 | Shorten ESD-monitor telemetry retention to cut storage cost | SF-EH-003 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 5098 | Attach assessment evidence to the claimed access control | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 5099 | Version collection-event identifiers instead of renumbering them | SF-SG-006 | permitted | disposed by citation | — |  |
| 5100 | Add the covered-transaction determination field to the tool purchase record | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 5101 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 5102 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-003 | denied | bound by precedent | REC-S0158 |  |
| 5103 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-004 | permitted | decided fresh | — |  |
| 5104 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-004 | permitted | decided fresh | — |  |
| 5105 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 5106 | Reclassify the agent-authorship provision as absolute | SF-AG-005 | denied | decided fresh | — |  |
| 5107 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 5108 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-001 SF-RT-006 ⛔ | denied | refused at the floor | — |  |
| 5109 | Replace the direct-URL dependency with a registry release | SF-SS-011 | permitted | decided fresh | — |  |
| 5110 | Drop the mutex around the shared WIP counter to cut contention | SF-TQ-001 | denied | decided fresh | — |  |
| 5111 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | decided fresh | — |  |
| 5112 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-004 | permitted | decided fresh | — |  |
| 5113 | Remove the human-review requirement from the screening provision | SF-EX-009 | denied | decided fresh | — |  |
| 5114 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | decided fresh | — |  |
| 5115 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-003 | permitted | decided fresh | — | ● |
| 5116 | Add an append-only constraint to the lot genealogy table | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 5117 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 5118 | Let the shipment proceed when the screening service returns a timeout | SF-EX-006 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 5119 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 5120 | Make the audit register append-only and disjoint from the store | SF-GV-005 | permitted | decided fresh | — |  |
| 5121 | Exclude audit findings from the retrieval query | SF-GV-005 | permitted | decided fresh | — |  |
| 5122 | Retire the superseded cryptographic floor from the constitution | SF-WI-005 | denied | decided fresh | — |  |
| 5123 | Link each claimed control to its implementation statement | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5124 | Accept a pickled analysis payload from the supplier portal | SF-AS-002 | denied | decided fresh | — |  |
| 5125 | Encrypt the recipe payload at rest in the vault | SF-RP-007 | permitted | decided fresh | — |  |
| 5126 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 5127 | Refresh the control assessment for the changed audit path | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5128 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-010 | permitted with conditions | decided fresh | — | ● |
| 5129 | Open a corrective-action record for every nonconformance | SF-QS-004 | permitted | decided fresh | — |  |
| 5130 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted | decided fresh | — |  |
| 5131 | Disable a vendor's remote-access account between sessions | SF-OT-003 | permitted | decided fresh | — |  |
| 5132 | Correct for coordinated omission in the ingest benchmark | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 5133 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted | decided fresh | — |  |
| 5134 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-007 | permitted | decided fresh | — |  |
| 5135 | Screen suppliers and upstream sources against the forced-labour entity list | SF-RS-004 | permitted | decided fresh | — |  |
| 5136 | Capture customer acknowledgement on the change notice before release | SF-QS-003 | permitted | decided fresh | — |  |
| 5137 | Hold agent edits to the screening logic for compliance review | SF-AG-005 | permitted | decided fresh | — |  |
| 5138 | Require a human sign-off before an agent edits equipment control code | SF-AG-005 | permitted | decided fresh | — |  |
| 5139 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-009 | denied | decided fresh | — |  |
| 5140 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-002 | permitted | decided fresh | — |  |
| 5141 | Validate the ECCN parameter against the enumerated set | — | permitted | docketed — nothing engaged | — |  |
| 5142 | Gate the important-data export on the completed security assessment | SF-DS-004 | permitted | decided fresh | — | ● |
| 5143 | Update the supply chain risk plan after the vendor change | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 5144 | Hold agent edits to the screening logic for compliance review | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5145 | Assert the safety interlock signal survives the gateway refactor | SF-SG-005 | permitted | decided fresh | — |  |
| 5146 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-005 | permitted | decided fresh | — |  |
| 5147 | Enforce the customer's notice period at the release gate | SF-QS-002 | permitted | decided fresh | — |  |
| 5148 | Amend the consolidation class threshold in the parameters file | SF-GV-007 | denied | decided fresh | — |  |
| 5149 | Run each build job on a fresh ephemeral runner | SF-SS-003 | permitted | decided fresh | — |  |
| 5150 | Write the full rationale trail at the moment of resolution | SF-GV-006 | permitted | decided fresh | — |  |
| 5151 | Move the charging threshold into the constitutional parameters file | SF-GV-006 | permitted | decided fresh | — |  |
| 5152 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5153 | Parameterise the supplier portal's lot-search query | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5154 | Encrypt the recipe payload at rest in the vault | SF-RP-004 | permitted | decided fresh | — |  |
| 5155 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-006 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5156 | Report load conditions alongside the p99.9 measurement | SF-RT-005 | permitted | decided fresh | — |  |
| 5157 | Add a config flag that disables the destination geofence for demos | SF-EX-001 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 5158 | Replace the direct-URL dependency with a registry release | SF-SS-002 | permitted | decided fresh | — |  |
| 5159 | Amend the consolidation class threshold in the parameters file | SF-QS-003 | denied | decided fresh | — |  |
| 5160 | Block the merge on the critical CVE in the ingest dependency | SF-SS-002 | permitted with conditions | decided fresh | — | ● |
| 5161 | Add the covered-transaction determination field to the tool purchase record | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 5162 | Wire a host command that can override the lockout/tagout state from the MES | SF-EH-001 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 5163 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | decided fresh | — |  |
| 5164 | Sign the container image published for the edge tool gateway | SF-SS-007 | permitted | decided fresh | — |  |
| 5165 | Honour the regulatory hold ahead of the retention sweep | SF-DS-003 | permitted | decided fresh | — |  |
| 5166 | Default the process-change classification to minor when the field is left blank | SF-QS-003 | denied | decided fresh | — |  |
| 5167 | Skip the registration-status check so a defence-article transfer completes over a holiday weekend | SF-IT-002 | denied | decided fresh | — |  |
| 5168 | Shorten the WIP record retention term in the rulebook | SF-OT-001 | denied | decided fresh | — |  |
| 5169 | Default every uncatalogued defence article to the commerce control list | SF-IT-003 SF-DS-004 ⛔ | denied | refused at the floor | — |  |
| 5170 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-001 SF-QS-003 ⛔ | denied | refused at the floor | — |  |
| 5171 | Point every site's tool logs at the single global log sink | SF-DS-002 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 5172 | Take the minor version bump that pulls in the critical archive CVE | SF-SS-004 | denied | decided fresh | — | ● |
| 5173 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-005 | permitted | decided fresh | — |  |
| 5174 | Issue a change notice before the first customer lot sees the recipe change | SF-QS-002 | permitted with conditions | decided fresh | — | ● |
| 5175 | Keep recipe execution records until the retention clock expires | SF-WI-003 | permitted | decided fresh | — |  |
| 5176 | Declare the latency budget for the changed metrology path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 5177 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 5178 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-005 | denied | bound by precedent | REC-S0199 |  |
| 5179 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5180 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 5181 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-006 | permitted | disposed by citation | — |  |
| 5182 | Close the check-then-open window in the metrology file handler | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5183 | Downsample cleanroom particle-count telemetry without recording the change | SF-EH-003 ⛔ | denied | refused at the floor | — |  |
| 5184 | Give the vendor a persistent VPN connection instead of a brokered session | SF-OT-002 | denied | decided fresh | — |  |
| 5185 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5186 | Replace the racy counter with an atomic in the ingest fanout | — | permitted | docketed — nothing engaged | — |  |
| 5187 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-004 | permitted | decided fresh | — |  |
| 5188 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh | — |  |
| 5189 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 5190 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-003 | permitted | decided fresh | — |  |
| 5191 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | decided fresh | — |  |
| 5192 | Post a compensating entry instead of editing the WIP status | SF-WI-007 | denied | bound by precedent | REC-S0120 |  |
| 5193 | Retry S2F41 remote commands without reordering the queue | SF-SG-009 | permitted | decided fresh | — | ● |
| 5194 | Ship the in-country support tunnel with the access question still open | SF-DS-007 | denied | decided fresh | — | ● |
| 5195 | Point every site's tool logs at the single global log sink | SF-DS-007 | denied | decided fresh | — |  |
| 5196 | Write the full rationale trail at the moment of resolution | SF-GV-005 | permitted | decided fresh | — |  |
| 5197 | Carry the expiry and referral on every recorded risk acceptance | SF-GV-005 | permitted | decided fresh | — |  |
| 5198 | Expand the classification questionnaire for multi-patterning masks | SF-EX-008 | permitted | decided fresh | — |  |
| 5199 | Add a residency assertion to the metrology ingest contract | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 5200 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh | — |  |
| 5201 | Record the builder identity in the release attestation | SF-SS-005 | permitted | disposed by citation | — |  |
| 5202 | Add a stress test that runs the broker under concurrent tool load | — | permitted | docketed — nothing engaged | — |  |
| 5203 | Encrypt the recipe payload at rest in the vault | SF-RP-004 | permitted | decided fresh | — |  |
| 5204 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 5205 | Scope the internal SECS parser package to the private registry | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 5206 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted | decided fresh | — | ● |
| 5207 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 5208 | Keep the 3DES envelope for backward-compatible recipe files | SF-CR-004 | denied | decided fresh | — |  |
| 5209 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-005 | permitted with conditions | decided fresh | — | ● |
| 5210 | Validate the ECCN parameter against the enumerated set | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5211 | Document the invariant the metrology ingest lock protects | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5212 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 5213 | Swap the hand-rolled MAC for the library primitive | SF-CR-005 | permitted | decided fresh | — |  |
| 5214 | Scope the internal SECS parser package to the private registry | SF-SS-005 | permitted | decided fresh | — |  |
| 5215 | Bound the request body size on the yield analytics endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5216 | Parallelise the SECS message dispatcher across four workers | SF-SG-002 SF-EX-010 ⛔ | denied | refused at the floor | — |  |
| 5217 | Swallow equipment replies the parser does not recognise | SF-SG-002 SF-SG-006 ⛔ | denied | refused at the floor | — |  |
| 5218 | Close the equipment joint-venture deal before the transaction-review checklist runs | SF-SO-002 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 5219 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5220 | Publish the measurement window with the latency result | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 5221 | Pin the denied-party list snapshot used by a screening decision | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 5222 | Widen the data residency provision to permit group-A replicas | SF-GV-003 | denied | decided fresh | — |  |
| 5223 | Surface unparsed equipment replies instead of dropping them | SF-SG-005 | permitted | decided fresh | — |  |
| 5224 | Stop shipping equipment logs across the boundary by default | SF-DS-005 | permitted | decided fresh | — |  |
| 5225 | Split the cross-border replica by jurisdiction tag | SF-DS-005 | permitted | decided fresh | — |  |
| 5226 | Hide the appeal button on the automated screening result page | SF-GV-005 | denied | decided fresh | — |  |
| 5227 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-004 | permitted | decided fresh | — | ● |
| 5228 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 5229 | Add a negative test for a tampered recipe signature | SF-CR-003 | permitted | decided fresh | — | ● |
| 5230 | Record the ECCN determination alongside the design-file upload | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 5231 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-001 SF-EX-007 ⛔ | denied | refused at the floor | — |  |
| 5232 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted with conditions | decided fresh | — | ● |
| 5233 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 5234 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 5235 | Rate-limit the supplier portal's document download endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5236 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 5237 | Add the realised adverse-contest rate to the governance export | SF-GV-006 | permitted | decided fresh | — |  |
| 5238 | Record the exception authority against the accepting principal | SF-GV-006 | permitted | decided fresh | — |  |
| 5239 | Add a scanner for process parameters in application logs | SF-RP-003 | permitted | decided fresh | — | ● |
| 5240 | Gate the important-data export on the completed security assessment | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 5241 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 5242 | Treat a signature verification error as a warning during rollout | SF-CR-006 | denied | decided fresh | — |  |
| 5243 | Add a scanner for process parameters in application logs | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 5244 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-007 | denied | decided fresh | — |  |
| 5245 | Batch alarm reports into the five-second telemetry flush | SF-SG-009 | denied | bound by precedent | REC-SF-B-04698 | ● |
| 5246 | Add a scanner for process parameters in application logs | SF-RP-005 | permitted | decided fresh after a tie | none_tie |  |
| 5247 | Publish the measurement window with the latency result | SF-RT-002 | permitted | decided fresh | — |  |
| 5248 | Split the slow enrichment step out of the alarm path | SF-RT-002 | permitted | decided fresh | — |  |
| 5249 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5250 | Hold agent edits to the screening logic for compliance review | SF-AG-005 | permitted | bound by precedent | REC-S0100 |  |
| 5251 | Move the alarm-fanout write off the monitoring hot path | SF-RT-004 | denied | bound by precedent | REC-S0122 |  |
| 5252 | Replace the pickle payload with a schema-validated JSON body | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5253 | Split the cross-border replica by jurisdiction tag | SF-DS-004 | permitted | decided fresh | — |  |
| 5254 | Accept recipe transfers from any host on the tool VLAN | SF-SG-001 SF-DS-006 ⛔ | denied | refused at the floor | — |  |
| 5255 | Record the agent identity and model version on the pull request | SF-AG-006 | permitted | decided fresh | — |  |
| 5256 | Assert the safety interlock signal survives the gateway refactor | SF-SG-006 | permitted | decided fresh | — |  |
| 5257 | Make the screening gate's denial final with no review route | SF-GV-001 SF-AG-004 ⛔ | denied | refused at the floor | — |  |
| 5258 | Stop shipping equipment logs across the boundary by default | SF-DS-005 | permitted | decided fresh | — |  |
| 5259 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted | decided fresh | — |  |
| 5260 | Declare the latency budget for the changed metrology path | SF-RT-006 | permitted | decided fresh | — |  |
| 5261 | Publish the measurement window with the latency result | SF-RT-006 | permitted | decided fresh | — |  |
| 5262 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-002 | denied | decided fresh | — | ● |
| 5263 | Retry S2F41 remote commands without reordering the queue | SF-SG-004 | permitted | decided fresh | — |  |
| 5264 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted | decided fresh | — |  |
| 5265 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 5266 | Assert the safety interlock signal survives the gateway refactor | SF-SG-010 | permitted | decided fresh | — |  |
| 5267 | Shorten the WIP record retention term in the rulebook | SF-RP-003 | denied | decided fresh | — |  |
| 5268 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 5269 | Resolve the foreign access request through the named legal channel | SF-DS-005 | permitted | decided fresh | — |  |
| 5270 | Close the check-then-open window in the metrology file handler | — | permitted | docketed — nothing engaged | — |  |
| 5271 | Shorten the WIP record retention term in the rulebook | SF-AS-003 | denied | decided fresh | — |  |
| 5272 | Lower the export-screening strictness in the policy repository | SF-WI-007 | denied | decided fresh | — |  |
| 5273 | Add secret scanning to the pre-merge pipeline | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 5274 | Pin the denied-party list snapshot used by a screening decision | SF-EX-011 | permitted | decided fresh | — |  |
| 5275 | Record the agent identity and model version on the pull request | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5276 | Bound the request body size on the yield analytics endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5277 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5278 | Add an append-only constraint to the lot genealogy table | SF-WI-005 | permitted | decided fresh | — |  |
| 5279 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-002 | permitted | decided fresh | — |  |
| 5280 | Filter the interlock signal out of the noisy alarm stream | SF-SG-009 | denied | decided fresh | — |  |
| 5281 | Quarantine agent changes that touch the export enforcement path | SF-AG-008 | permitted | decided fresh | — |  |
| 5282 | Record the builder identity in the release attestation | SF-SS-008 | permitted | decided fresh | — |  |
| 5283 | Keep the HSMS reply timeout inside the declared bound | SF-SG-004 | permitted | decided fresh | — |  |
| 5284 | Block the merge on the critical CVE in the ingest dependency | SF-SS-010 | permitted | bound by precedent | REC-S0112 |  |
| 5285 | Sign the container image published for the edge tool gateway | SF-SS-003 | permitted | decided fresh after a tie | none_tie |  |
| 5286 | Re-enable the compliance test the agent's rebase had skipped | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 5287 | Record the builder identity in the release attestation | SF-SS-007 | permitted | decided fresh | — |  |
| 5288 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | decided fresh | — |  |
| 5289 | Publish the EDA toolchain image without running the classification step | SF-EX-008 | denied | decided fresh | — |  |
| 5290 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5291 | Remove the verification-of-effectiveness step from the corrective-action workflow | SF-QS-002 | denied | decided fresh | — | ● |
| 5292 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted | decided fresh | — |  |
| 5293 | Correct for coordinated omission in the ingest benchmark | SF-RT-007 | permitted | decided fresh | — |  |
| 5294 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5295 | Deliver alarm reports ahead of the collection-event budget | SF-SG-006 | permitted | decided fresh | — |  |
| 5296 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-006 | permitted | decided fresh | — |  |
| 5297 | Bound the SECS message queue depth per tool connection | SF-SG-007 | permitted | decided fresh | — |  |
| 5298 | Stream Hsinchu metrology results to the Hillsboro data lake | SF-DS-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 5299 | Add the CHIPS notification duty to the compliance rulebook | SF-WI-003 | denied | decided fresh | — |  |
| 5300 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5301 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5302 | Report load conditions alongside the p99.9 measurement | SF-RT-003 | permitted | decided fresh | — | ● |
| 5303 | Raise the latency budget stated in the constitutional parameters | SF-CR-002 | denied | decided fresh | — |  |
| 5304 | Raise the latency budget stated in the constitutional parameters | SF-TQ-001 | denied | decided fresh | — |  |
| 5305 | Record who amended the CD-SEM measurement and why | SF-WI-005 | permitted | decided fresh | — |  |
| 5306 | Add an append-only constraint to the lot genealogy table | SF-WI-005 | permitted | decided fresh | — |  |
| 5307 | Sign the container image published for the edge tool gateway | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5308 | Route Kumamoto tool logs to the in-region log sink | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 5309 | Keep the HSMS reply timeout inside the declared bound | SF-SG-005 | permitted | decided fresh | — |  |
| 5310 | Make the screening gate's denial final with no review route | SF-GV-005 | denied | decided fresh | — |  |
| 5311 | Drop the boycott-language flag from the purchase-order parser without logging it | SF-SO-002 SF-RT-001 ⛔ | denied | refused at the floor | — |  |
| 5312 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-004 SF-SS-002 ⛔ | denied | refused at the floor | — |  |
| 5313 | Monitor and alarm on clock drift across the tool network | SF-OT-001 | permitted | decided fresh | — |  |
| 5314 | Restrict tool-network traffic to the declared conduit at the zone boundary | SF-OT-001 | permitted | decided fresh | — |  |
| 5315 | Fix the deadlock between the alarm writer and the snapshot reader | — | permitted | docketed — nothing engaged | — |  |
| 5316 | Preserve S6F11 event ordering under broker backpressure | SF-SG-009 | permitted | bound by precedent | REC-S0108 |  |
| 5317 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | decided fresh | — |  |
| 5318 | Move key material into the hardware security module | SF-CR-004 | permitted | decided fresh | — |  |
| 5319 | Keep the HSMS reply timeout inside the declared bound | SF-SG-010 | permitted | decided fresh | — |  |
| 5320 | Hide the appeal button on the automated screening result page | SF-GV-005 | denied | decided fresh | — |  |
| 5321 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5322 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5323 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 5324 | Exclude recipe bodies from the vendor support bundle | SF-RP-004 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 5325 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 5326 | Gate the important-data export on the completed security assessment | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 5327 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 5328 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5329 | Pin the JVM collector so pause times stay inside the budget | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 5330 | Ship the ingest rewrite with the worst-case spike still unexplained | SF-RT-004 | denied | decided fresh | — | ● |
| 5331 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-002 | permitted | decided fresh | — |  |
| 5332 | Deny defence-enclave egress by default and allowlist only reviewed destinations | SF-IT-002 | permitted | decided fresh | — |  |
| 5333 | Attribute every metrology record amendment to a named operator | SF-WI-005 | permitted | decided fresh | — |  |
| 5334 | Canonicalise the upload path before the handler opens the file | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5335 | Reclassify the agent-authorship provision as absolute | SF-SG-007 | denied | decided fresh | — |  |
| 5336 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5337 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-003 | denied | decided fresh | — |  |
| 5338 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-002 | permitted | decided fresh | — |  |
| 5339 | Allowlist the export format instead of shelling out with user input | SF-AS-002 | permitted | decided fresh | — |  |
| 5340 | Weight supplier terms against firms the model scores as distressed | SF-GV-002 SF-AG-008 ⛔ | denied | refused at the floor | — |  |
| 5341 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 5342 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5343 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5344 | Drop the deprecated field from the agent's regenerated response body | SF-AG-008 | denied | decided fresh | — |  |
| 5345 | Record the percentile family used for the declared budget | SF-RT-007 | permitted | decided fresh | — |  |
| 5346 | Scope the internal SECS parser package to the private registry | SF-SS-010 | permitted | decided fresh | — |  |
| 5347 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5348 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-004 | permitted with conditions | decided fresh | — | ● |
| 5349 | Preserve S6F11 event ordering under broker backpressure | SF-SG-007 | permitted | decided fresh | — |  |
| 5350 | Serialise the two writers to the yield aggregation table | SF-TQ-002 | permitted | decided fresh | — |  |
| 5351 | Publish the measurement window with the latency result | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 5352 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — |  |
| 5353 | Add fuzz coverage for the metrology file upload handler | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5354 | Ignore instructions embedded in ticket text at the agent runner | SF-AG-006 | permitted | decided fresh | — |  |
| 5355 | Route every screening near-miss to a named compliance reviewer | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 5356 | Block the merge on the critical CVE in the ingest dependency | SF-SS-008 | permitted | disposed by citation | — |  |
| 5357 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-009 | denied | decided fresh | — | ● |
| 5358 | Keep the lockout/tagout state read-only in the software layer | SF-EH-004 | permitted with conditions | decided fresh | — | ● |
| 5359 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 5360 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-004 | permitted | disposed by citation | — |  |
| 5361 | Install the metrology decoder straight from a git URL | SF-SS-005 | denied | decided fresh | — |  |
| 5362 | Attach qualification evidence to every process-change record | SF-QS-002 | permitted | decided fresh | — |  |
| 5363 | Wire a rollback path into every controller-model promotion | SF-QS-002 | permitted | decided fresh | — |  |
| 5364 | Let compliance edit the export determination after the shipment closes | SF-EX-010 | denied | decided fresh | — |  |
| 5365 | Pin the JVM collector so pause times stay inside the budget | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 5366 | Rate-limit the supplier portal's document download endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5367 | Stop shipping equipment logs across the boundary by default | SF-DS-004 | permitted | decided fresh | — |  |
| 5368 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5369 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5370 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-006 | permitted | decided fresh | — |  |
| 5371 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-009 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 5372 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted | decided fresh | — |  |
| 5373 | Rewrite the metrology ingest path without stating its timing target | SF-RT-002 | denied | decided fresh | — |  |
| 5374 | Bound the collector's allocation rate on the ingest path | SF-RT-001 | permitted | decided fresh | — |  |
| 5375 | Attribute every metrology record amendment to a named operator | SF-WI-006 | permitted with conditions | decided fresh | — | ● |
| 5376 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted | decided fresh | — |  |
| 5377 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-007 | permitted | decided fresh | — |  |
| 5378 | Declare the latency budget for the changed metrology path | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 5379 | Retain the conflict-minerals inquiry response on the component record | SF-RS-003 | permitted with conditions | decided fresh | — | ● |
| 5380 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 5381 | Fail the pipeline closed when the screening service times out | SF-EX-008 | permitted | decided fresh | — |  |
| 5382 | Capture the licence determination rationale in the trade record | SF-EX-008 | permitted | decided fresh | — |  |
| 5383 | Declare the latency budget for the changed metrology path | SF-RT-006 | permitted | decided fresh | — |  |
| 5384 | Drop the standing declaration from the governance export payload | SF-GV-005 | denied | decided fresh | — |  |
| 5385 | Declare the latency budget for the changed metrology path | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 5386 | Fail the pipeline closed when the screening service times out | SF-EX-010 | permitted | decided fresh | — |  |
| 5387 | Re-screen consignees on the published list-refresh cadence | SF-EX-013 | permitted | decided fresh | — |  |
| 5388 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted | decided fresh | — |  |
| 5389 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted with conditions | decided fresh | — | ● |
| 5390 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 5391 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted | decided fresh | — |  |
| 5392 | Rate-limit the supplier portal's document download endpoint | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5393 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 5394 | Report a suspect counterfeit part to the named quality owner before disposition | SF-RS-001 | permitted | decided fresh | — |  |
| 5395 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted | decided fresh | — |  |
| 5396 | Bound the collector's allocation rate on the ingest path | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 5397 | Swap the hand-rolled MAC for the library primitive | SF-CR-006 | permitted | decided fresh | — |  |
| 5398 | Move key material into the hardware security module | SF-CR-006 | permitted | decided fresh | — |  |
| 5399 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5400 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted | decided fresh | — |  |
| 5401 | Serialise the two writers to the yield aggregation table | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5402 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted | decided fresh | — |  |
| 5403 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5404 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5405 | Add secret scanning to the pre-merge pipeline | SF-SS-005 | permitted with conditions | decided fresh | — | ● |
| 5406 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-002 SF-WI-005 ⛔ | denied | refused at the floor | — |  |
| 5407 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | decided fresh | — |  |
| 5408 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5409 | Separate the reporter bulletin from the adjudication input path | SF-GV-003 | permitted | decided fresh | — |  |
| 5410 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 5411 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5412 | Keep recipe text out of the yield model's prompt context | SF-RP-007 | permitted | decided fresh | — |  |
| 5413 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 5414 | Bound the collector's allocation rate on the ingest path | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 5415 | Pull the ingest parser from a mirror whose digest no longer matches | SF-SS-001 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 5416 | Bind the DDTC registration-status check into the enclave access grant | SF-IT-004 | permitted with conditions | decided fresh | — | ● |
| 5417 | Verify tool firmware signatures against the vendor key before install | SF-OT-001 | permitted | decided fresh | — |  |
| 5418 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5419 | Let the agent's enrichment step call an outside classification API | SF-AG-002 SF-AS-003 ⛔ | denied | refused at the floor | — |  |
| 5420 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 5421 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-004 | permitted | decided fresh | — |  |
| 5422 | Link each claimed control to its implementation statement | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 5423 | Keep Dresden yield records inside the EU replica set | SF-DS-004 | permitted | decided fresh | — |  |
| 5424 | Record who amended the CD-SEM measurement and why | SF-WI-004 | permitted | decided fresh | — |  |
| 5425 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted | decided fresh | — |  |
| 5426 | Add the pilot line to the CUI boundary documentation | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5427 | Make the lot-genealogy cache update atomic with its invalidation | — | permitted | docketed — nothing engaged | — |  |
| 5428 | Document the invariant the metrology ingest lock protects | — | permitted | docketed — nothing engaged | — |  |
| 5429 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5430 | Bound the SECS message queue depth per tool connection | SF-SG-009 | permitted | decided fresh | — |  |
| 5431 | Add a retention-hold check to the record destruction job | SF-WI-003 | permitted | decided fresh | — | ● |
| 5432 | Rotate the recipe vault envelope key on the published schedule | SF-RP-007 | permitted | decided fresh after a tie | none_tie |  |
| 5433 | Shell out to the converter with the supplier's filename | SF-AS-003 | denied | decided fresh | — |  |
| 5434 | Replace the pickle payload with a schema-validated JSON body | SF-AS-002 | permitted | disposed by citation | — |  |
| 5435 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-001 | permitted | decided fresh | — |  |
| 5436 | Remove the human-review requirement from the screening provision | SF-SS-010 | denied | decided fresh | — |  |
| 5437 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-004 | permitted | decided fresh | — |  |
| 5438 | Authenticate the time source for every piece of fab equipment | SF-OT-004 | permitted | decided fresh | — |  |
| 5439 | Strengthen the memory ordering on the sequence-number publish | — | permitted | docketed — nothing engaged | — |  |
| 5440 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5441 | Document the CUI boundary for the metrology ingest service | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 5442 | Record the builder identity in the release attestation | SF-SS-008 | permitted with conditions | decided fresh | — | ● |
| 5443 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted with conditions | decided fresh | — | ● |
| 5444 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 5445 | Expedite receipt of a lot whose counterfeit inspection already passed same-day | SF-RS-004 | permitted with conditions | decided fresh | — | ● |
| 5446 | Let the MES correct yesterday's WIP status in place | SF-WI-001 SF-WI-003 ⛔ | denied | refused at the floor | — |  |
| 5447 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-001 | permitted | decided fresh | — |  |
| 5448 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-001 | permitted | decided fresh | — |  |
| 5449 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted | decided fresh | — |  |
| 5450 | Run each build job on a fresh ephemeral runner | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5451 | Bound the request body size on the yield analytics endpoint | SF-AS-001 | denied | bound by precedent | REC-S0162 |  |
| 5452 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 5453 | Build the lot-search query by concatenating the filter string | SF-AS-003 | denied | decided fresh | — |  |
| 5454 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 5455 | Version collection-event identifiers instead of renumbering them | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 5456 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 5457 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-008 | permitted | decided fresh after a tie | none_tie |  |
| 5458 | Attach an agent provenance attestation to the generated migration | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 5459 | Parameterise the supplier portal's lot-search query | SF-AS-003 | permitted | decided fresh | — | ● |
| 5460 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-004 | permitted | decided fresh | — | ● |
| 5461 | Attach the provenance attestation to the tool-gateway release | SF-SS-009 | permitted | decided fresh | — |  |
| 5462 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 5463 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 5464 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh | — |  |
| 5465 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 5466 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-002 | permitted | decided fresh | — |  |
| 5467 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted | decided fresh | — |  |
| 5468 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5469 | Bound the request body size on the yield analytics endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5470 | Add an append-only constraint to the lot genealogy table | SF-WI-004 | permitted | decided fresh | — |  |
| 5471 | Verify the audit chain after the metrology schema migration | SF-WI-004 | permitted | decided fresh | — |  |
| 5472 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-003 | permitted | decided fresh | — |  |
| 5473 | Record the control inheritance for the shared platform tier | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 5474 | Add the newly pulled component to the generated SBOM | SF-SS-008 | permitted with conditions | decided fresh | — | ● |
| 5475 | Filter the interlock signal out of the noisy alarm stream | SF-SG-009 | denied | decided fresh | — |  |
| 5476 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted with conditions | decided fresh | — | ● |
| 5477 | Join the audit findings table into the precedent retrieval query | SF-GV-002 SF-WI-007 ⛔ | denied | refused at the floor | — |  |
| 5478 | Let the batch corrector amend metrology rows without a named operator | SF-WI-006 | denied | decided fresh | — |  |
| 5479 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-009 | denied | decided fresh | — |  |
| 5480 | Honour the regulatory hold ahead of the retention sweep | SF-DS-004 | permitted with conditions | decided fresh | — | ● |
| 5481 | Let compliance edit the export determination after the shipment closes | SF-EX-004 SF-SS-010 ⛔ | denied | refused at the floor | — |  |
| 5482 | Replace the direct-URL dependency with a registry release | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 5483 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-004 | permitted | decided fresh | — |  |
| 5484 | Bind the mask revision to its lot and recipe record | SF-QS-003 | permitted | decided fresh | — |  |
| 5485 | Add fuzz coverage for the metrology file upload handler | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5486 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted | decided fresh | — | ● |
| 5487 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-007 | permitted | decided fresh | — |  |
| 5488 | Add an append-only constraint to the lot genealogy table | SF-WI-007 | permitted | decided fresh | — |  |
| 5489 | Rate-limit the supplier portal's document download endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5490 | Fail the pipeline closed when the screening service times out | SF-EX-012 | permitted | decided fresh | — |  |
| 5491 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 5492 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5493 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh after a tie | none_tie |  |
| 5494 | Attach qualification evidence to every process-change record | SF-QS-002 | permitted | decided fresh | — |  |
| 5495 | Add a licence-exception clause to the trade compliance rulebook | SF-AG-005 | denied | decided fresh | — |  |
| 5496 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-006 | permitted | decided fresh | — |  |
| 5497 | Strip process parameters from telemetry metric labels | SF-RP-004 | permitted | decided fresh | — |  |
| 5498 | Accept receipt of a lot whose supplier attestation expired last quarter | SF-RS-003 | denied | decided fresh | — | ● |
| 5499 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 5500 | Correct for coordinated omission in the ingest benchmark | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 5501 | Preserve S6F11 event ordering under broker backpressure | SF-SG-010 | permitted | decided fresh | — |  |
| 5502 | Record the percentile family used for the declared budget | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 5503 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5504 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | decided fresh | — |  |
| 5505 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | decided fresh | — |  |
| 5506 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 5507 | Lower the export-screening strictness in the policy repository | SF-RT-002 | denied | decided fresh | — |  |
| 5508 | Add the destination geofence to the design-file download path | SF-EX-011 | permitted | decided fresh | — |  |
| 5509 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-008 | permitted | decided fresh | — |  |
| 5510 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-010 | permitted | disposed by citation | — |  |
| 5511 | Pin the denied-party list snapshot used by a screening decision | SF-EX-007 | permitted | decided fresh | — |  |
| 5512 | Pin the denied-party list snapshot used by a screening decision | SF-EX-007 | permitted | decided fresh | — |  |
| 5513 | Sign the release attestation with the developer's own runner identity | SF-SS-003 | denied | decided fresh | — |  |
| 5514 | Deliver alarm reports ahead of the collection-event budget | SF-SG-004 | permitted | disposed by citation | — |  |
| 5515 | Hold agent edits to the screening logic for compliance review | SF-AG-004 | permitted | decided fresh | — |  |
| 5516 | Verify every package the agent imported against the registry | SF-AG-004 | permitted | decided fresh | — |  |
| 5517 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted | decided fresh | — |  |
| 5518 | Bound the request body size on the yield analytics endpoint | — | permitted | docketed — nothing engaged | — |  |
| 5519 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5520 | Mask implant dose values in the yield analytics export | SF-RP-004 | permitted | decided fresh | — |  |
| 5521 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-009 | permitted | decided fresh | — |  |
| 5522 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5523 | Propose a new provision covering advanced-node lithography data | SF-OT-003 | denied | decided fresh | — |  |
| 5524 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-008 | permitted | decided fresh | — |  |
| 5525 | Stop shipping equipment logs across the boundary by default | SF-DS-003 | permitted | decided fresh | — | ● |
| 5526 | Route Kumamoto tool logs to the in-region log sink | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5527 | Declare the processing region for the new metrology sub-processor | SF-DS-007 | permitted | decided fresh | — | ● |
| 5528 | Redact recipe parameters from the tool-gateway debug log | SF-RP-004 | permitted | decided fresh | — |  |
| 5529 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 5530 | Build the lot-search query by concatenating the filter string | SF-AS-003 | denied | decided fresh | — |  |
| 5531 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-004 | denied | decided fresh | — |  |
| 5532 | Let the defence-article transfer proceed without naming a licence or exemption paragraph | SF-IT-003 SF-SS-002 ⛔ | denied | refused at the floor | — |  |
| 5533 | Keep recipe execution records until the retention clock expires | SF-WI-005 | permitted | decided fresh | — |  |
| 5534 | Verify the audit chain after the metrology schema migration | SF-WI-005 | permitted | decided fresh | — |  |
| 5535 | Bound the SECS message queue depth per tool connection | SF-SG-005 | permitted with conditions | decided fresh | — | ● |
| 5536 | Rate-limit the supplier portal's document download endpoint | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5537 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted | decided fresh | — |  |
| 5538 | Add secret scanning to the pre-merge pipeline | SF-SS-007 | permitted | decided fresh | — |  |
| 5539 | Run each build job on a fresh ephemeral runner | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 5540 | Replace the direct-URL dependency with a registry release | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5541 | Sign the release attestation with the developer's own runner identity | SF-SS-002 | denied | decided fresh | — |  |
| 5542 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted | decided fresh | — |  |
| 5543 | Close the equipment joint-venture deal before the transaction-review checklist runs | SF-SO-002 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5544 | Disable a vendor's remote-access account between sessions | SF-OT-001 | permitted with conditions | decided fresh | — | ● |
| 5545 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5546 | Broker vendor remote sessions through the jump host | SF-OT-001 | permitted | decided fresh | — |  |
| 5547 | Derive the recipe encryption nonce from the lot identifier | SF-CR-001 SF-EX-010 ⛔ | denied | refused at the floor | — |  |
| 5548 | Tag every WIP record with the jurisdiction that produced it | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5549 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-009 | permitted | decided fresh | — |  |
| 5550 | Hash the recipe identifier before it reaches the analytics store | SF-RP-004 | permitted | decided fresh | — |  |
| 5551 | Run each build job on a fresh ephemeral runner | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5552 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted | decided fresh | — |  |
| 5553 | Keep Dresden yield records inside the EU replica set | SF-DS-007 | permitted | decided fresh | — | ● |
| 5554 | Let the coding agent refactor the screening gate's decision logic | SF-AG-005 | denied | decided fresh | — |  |
| 5555 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-003 | permitted | decided fresh | — |  |
| 5556 | Assert the safety interlock signal survives the gateway refactor | SF-SG-007 | permitted with conditions | decided fresh | — | ● |
| 5557 | Bound the collector's allocation rate on the ingest path | SF-RT-004 | denied | bound by precedent | REC-S0122 |  |
| 5558 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-013 | denied | decided fresh | — |  |
| 5559 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-002 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 5560 | Attach the provenance attestation to the tool-gateway release | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5561 | Require an EHS signoff record before a gas-alarm threshold change ships | SF-EH-004 | permitted | decided fresh | — |  |
| 5562 | Trace every discharge-report value back to its raw measurement | SF-EH-004 | permitted | decided fresh | — |  |
| 5563 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 5564 | Reconcile WIP snapshots against the tool event stream nightly | SF-WI-004 | denied | bound by precedent | REC-S0160 |  |
| 5565 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 5566 | Move the charging threshold into the constitutional parameters file | SF-GV-005 | permitted | decided fresh | — |  |
| 5567 | Rebuild the hash chain check into the nightly ledger verification | SF-WI-003 | permitted | decided fresh | — |  |
| 5568 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5569 | Join the audit findings table into the precedent retrieval query | SF-GV-002 SF-DS-006 ⛔ | denied | refused at the floor | — |  |
| 5570 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-006 | permitted | decided fresh | — |  |
| 5571 | Purge recipe execution records older than ninety days | SF-WI-001 SF-RT-003 ⛔ | denied | refused at the floor | — |  |
| 5572 | Verify the artifact signature before the tool gateway installs it | SF-CR-005 | permitted | decided fresh | — |  |
| 5573 | Feed the weekly precedent bulletin into the adjudicator's context | SF-GV-004 | denied | decided fresh | — | ● |
| 5574 | Amend the consolidation class threshold in the parameters file | SF-CR-005 | denied | decided fresh | — |  |
| 5575 | Batch alarm reports into the five-second telemetry flush | SF-SG-001 SF-SS-009 ⛔ | denied | refused at the floor | — |  |
| 5576 | Generate the SBOM from the direct dependency list only | SF-SS-005 | denied | decided fresh | — |  |
| 5577 | Record the builder identity in the release attestation | SF-SS-002 | permitted | decided fresh | — |  |
| 5578 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | decided fresh | — |  |
| 5579 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 5580 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5581 | Retry S2F41 remote commands without reordering the queue | SF-SG-007 | permitted | decided fresh | — | ● |
| 5582 | Re-screen consignees on the published list-refresh cadence | SF-EX-011 | permitted | decided fresh | — |  |
| 5583 | Attach assessment evidence to the claimed access control | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 5584 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-006 | permitted | decided fresh | — |  |
| 5585 | Enforce supplier-attestation expiry at the receiving dock | SF-RS-003 | permitted | decided fresh | — |  |
| 5586 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — |  |
| 5587 | Run each build job on a fresh ephemeral runner | SF-SS-011 | permitted | decided fresh | — |  |
| 5588 | Record and time-box every vendor remote-access session | SF-OT-003 | permitted | decided fresh | — |  |
| 5589 | Grant the Shanghai integration team read access to the mask design repository | SF-EX-012 | denied | decided fresh | — | ● |
| 5590 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 5591 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5592 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5593 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted | decided fresh | — |  |
| 5594 | Expand the classification questionnaire for multi-patterning masks | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5595 | Capture the licence determination rationale in the trade record | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 5596 | Block the merge on the critical CVE in the ingest dependency | SF-SS-006 | permitted | decided fresh | — |  |
| 5597 | Disable a vendor's remote-access account between sessions | SF-OT-003 | permitted | decided fresh | — |  |
| 5598 | Attach the provenance attestation to the tool-gateway release | SF-SS-010 | permitted | disposed by citation | — |  |
| 5599 | Reclassify the agent-authorship provision as absolute | SF-SG-006 | denied | decided fresh | — |  |
| 5600 | Keep recipe execution records until the retention clock expires | SF-WI-004 | permitted | decided fresh | — |  |
| 5601 | Commit the CHIPS notification record for the Kumamoto expansion | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5602 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5603 | Cache decrypted recipe payloads on the gateway for faster reloads | SF-RP-007 | denied | decided fresh | — |  |
| 5604 | Add the pilot line to the CUI boundary documentation | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5605 | Record the builder identity in the release attestation | SF-SS-004 | permitted | decided fresh | — |  |
| 5606 | Record the agent identity and model version on the pull request | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5607 | Replace the pickle payload with a schema-validated JSON body | SF-AS-003 | permitted | decided fresh | — |  |
| 5608 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-003 | permitted | decided fresh | — |  |
| 5609 | Add the destination geofence to the design-file download path | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 5610 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | permitted | decided fresh | — |  |
| 5611 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-003 | permitted | decided fresh | — |  |
| 5612 | Capture customer acknowledgement on the change notice before release | SF-QS-003 | permitted | decided fresh | — |  |
| 5613 | Capture the licence determination rationale in the trade record | SF-EX-010 | permitted | decided fresh after a tie | none_tie |  |
| 5614 | Let the agent's enrichment step call an outside classification API | SF-AG-007 | denied | decided fresh | — |  |
| 5615 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 5616 | Release a suspect counterfeit part to production before disposition is recorded | SF-RS-002 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 5617 | Classify a process change as major or minor with recorded rationale | SF-QS-003 | permitted with conditions | decided fresh | — | ● |
| 5618 | Keep Dresden yield records inside the EU replica set | SF-DS-003 | permitted | decided fresh | — | ● |
| 5619 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5620 | Open a corrective-action record for every nonconformance | SF-QS-004 | permitted | decided fresh | — |  |
| 5621 | Route every screening near-miss to a named compliance reviewer | SF-EX-011 | permitted | decided fresh | — |  |
| 5622 | Reuse the warm build runner to cut pipeline time in half | SF-SS-005 | denied | decided fresh | — | ● |
| 5623 | Move the defence-enclave backup into the general-purpose cloud region for cheaper storage | SF-IT-003 ⛔ | denied | refused at the floor | — |  |
| 5624 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-004 | permitted | decided fresh | — |  |
| 5625 | Validate the ECCN parameter against the enumerated set | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5626 | Keep the HSMS reply timeout inside the declared bound | SF-SG-009 | permitted | decided fresh | — |  |
| 5627 | Include the active recipe set in the vendor diagnostic bundle | SF-RP-006 | denied | decided fresh | — |  |
| 5628 | Report load conditions alongside the p99.9 measurement | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 5629 | Derive the recipe encryption nonce from the lot identifier | SF-CR-001 SF-QS-004 ⛔ | denied | refused at the floor | — |  |
| 5630 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 5631 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted | decided fresh | — |  |
| 5632 | Verify component digests against the registry before deploy | SF-SS-007 | permitted | decided fresh | — |  |
| 5633 | Rate-limit the supplier portal's document download endpoint | — | permitted | docketed — nothing engaged | — |  |
| 5634 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-006 | permitted | decided fresh | — |  |
| 5635 | Surface unparsed equipment replies instead of dropping them | SF-SG-004 | permitted | decided fresh | — |  |
| 5636 | Assert the safety interlock signal survives the gateway refactor | SF-SG-004 | permitted | decided fresh | — |  |
| 5637 | Split the slow enrichment step out of the alarm path | SF-RT-006 | permitted | decided fresh | — |  |
| 5638 | Capture the licence determination rationale in the trade record | SF-EX-009 | permitted with conditions | decided fresh | — | ● |
| 5639 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-008 | denied | decided fresh | — |  |
| 5640 | Batch alarm reports into the five-second telemetry flush | SF-SG-001 SF-OT-001 ⛔ | denied | refused at the floor | — |  |
| 5641 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 5642 | Bound the telemetry buffer so ingest backpressure is visible | — | permitted | docketed — nothing engaged | — |  |
| 5643 | Add fuzz coverage for the metrology file upload handler | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5644 | Let the coding agent refactor the screening gate's decision logic | SF-AG-001 SF-RP-007 ⛔ | denied | refused at the floor | — |  |
| 5645 | Scope the internal SECS parser package to the private registry | SF-SS-009 | permitted with conditions | decided fresh | — | ● |
| 5646 | Report load conditions alongside the p99.9 measurement | SF-RT-006 | denied | bound by precedent | REC-S0156 |  |
| 5647 | Log the deemed-export check that runs at repository role grant | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 5648 | Let the batch corrector amend metrology rows without a named operator | SF-WI-003 | denied | decided fresh | — |  |
| 5649 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 5650 | Report the new latency number without saying what load produced it | SF-RT-006 | denied | decided fresh | — |  |
| 5651 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | decided fresh | — |  |
| 5652 | Add a scanner for process parameters in application logs | SF-RP-007 | permitted | decided fresh | — |  |
| 5653 | Keep audit logging on during the throughput optimisation | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 5654 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted | decided fresh | — |  |
| 5655 | Split the slow enrichment step out of the alarm path | SF-RT-001 | permitted | decided fresh after a tie | none_tie |  |
| 5656 | Swallow equipment replies the parser does not recognise | SF-SG-002 SF-AS-002 ⛔ | denied | refused at the floor | — |  |
| 5657 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted with conditions | decided fresh | — | ● |
| 5658 | Add a p100 assertion to the tool-gateway regression suite | SF-RT-002 | permitted with conditions | decided fresh | — | ● |
| 5659 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-003 | permitted | decided fresh | — |  |
| 5660 | Drop the deprecated cipher suites from the supplier portal | SF-CR-003 | permitted | decided fresh | — |  |
| 5661 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5662 | Parameterise the supplier portal's lot-search query | SF-AS-003 | permitted | disposed by citation | — |  |
| 5663 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-003 | permitted | decided fresh | — |  |
| 5664 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 5665 | Add the newly pulled component to the generated SBOM | SF-SS-011 | permitted | decided fresh | — |  |
| 5666 | Block the merge on the critical CVE in the ingest dependency | SF-SS-011 | permitted | decided fresh | — |  |
| 5667 | Validate the run-to-run controller model on held-out lots before promotion | SF-QS-001 | permitted | decided fresh | — |  |
| 5668 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5669 | Retire the superseded cryptographic floor from the constitution | SF-SG-007 | denied | decided fresh | — |  |
| 5670 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-005 | permitted | decided fresh | — | ● |
| 5671 | Accept the agent's rebase that skips the failing screening test | SF-AG-008 | denied | decided fresh | — |  |
| 5672 | Bound the SECS message queue depth per tool connection | SF-SG-004 | permitted | decided fresh | — |  |
| 5673 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-006 SF-DS-007 ⛔ | denied | refused at the floor | — |  |
| 5674 | Block the merge on the critical CVE in the ingest dependency | SF-SS-004 | permitted | decided fresh after a tie | none_tie |  |
| 5675 | Release a quarantined lot to production once its provenance chain is fully verified | SF-RS-001 | permitted with conditions | decided fresh | — | ● |
| 5676 | Keep Dresden yield records inside the EU replica set | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 5677 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-004 | denied | decided fresh | — |  |
| 5678 | Pin the JVM collector so pause times stay inside the budget | SF-RT-007 | permitted with conditions | decided fresh | — | ● |
| 5679 | Move portal document storage to a new vendor without naming its region | SF-DS-002 SF-SS-011 ⛔ | denied | refused at the floor | — |  |
| 5680 | Add a direct download URL that bypasses the trade compliance gate | SF-EX-004 SF-EX-013 ⛔ | denied | refused at the floor | — |  |
| 5681 | Scope recipe vault reads to the owning process integration team | SF-RP-007 | permitted | decided fresh | — | ● |
| 5682 | Replace the pickle payload with a schema-validated JSON body | SF-AS-003 | permitted | decided fresh | — |  |
| 5683 | Roll the crypto library back to the version the build used to pin | SF-SS-001 ⛔ | denied | refused at the floor | — |  |
| 5684 | Rotate the recipe vault signing key on the published schedule | SF-CR-004 | permitted | decided fresh | — |  |
| 5685 | Add a negative test for a tampered recipe signature | SF-CR-004 | permitted | decided fresh | — |  |
| 5686 | Require the licence exception paragraph on the shipment record | SF-EX-010 | permitted | decided fresh | — |  |
| 5687 | Auto-clear screening hits below the fuzzy-match threshold | SF-EX-001 SF-AG-005 ⛔ | denied | refused at the floor | — |  |
| 5688 | Move the alarm-fanout write off the monitoring hot path | SF-RT-003 | permitted | decided fresh | — |  |
| 5689 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-003 | permitted | decided fresh | — |  |
| 5690 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5691 | Require the licence exception paragraph on the shipment record | SF-EX-007 | permitted | decided fresh | — | ● |
| 5692 | Preserve S6F11 event ordering under broker backpressure | SF-SG-003 | permitted | disposed by citation | — |  |
| 5693 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 5694 | Attach an agent provenance attestation to the generated migration | SF-AG-007 | permitted | decided fresh | — |  |
| 5695 | Disable a vendor's remote-access account between sessions | SF-OT-001 | permitted | decided fresh | — |  |
| 5696 | Require named-owner approval per vendor remote session | SF-OT-001 | permitted | decided fresh | — |  |
| 5697 | Record the ECCN determination alongside the design-file upload | SF-EX-011 | permitted | decided fresh | — |  |
| 5698 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted | decided fresh | — |  |
| 5699 | Make the lot-genealogy cache update atomic with its invalidation | — | permitted | docketed — nothing engaged | — |  |
| 5700 | Retire the mask-revision spreadsheet now that dispatch blocking reads straight from the lot record | SF-QS-001 | permitted | decided fresh | — |  |
| 5701 | Order the two mutex acquisitions consistently across both paths | SF-TQ-003 | permitted | decided fresh | — |  |
| 5702 | Round emissions report values down to the nearest permit-limit increment | SF-EH-003 ⛔ | denied | refused at the floor | — |  |
| 5703 | Serialise the two writers to the yield aggregation table | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5704 | Retain the conflict-minerals inquiry response on the component record | SF-RS-001 | permitted | decided fresh | — |  |
| 5705 | Rate-limit the supplier portal's document download endpoint | — | permitted | docketed — nothing engaged | — |  |
| 5706 | Hash the recipe identifier before it reaches the analytics store | SF-RP-005 | permitted | decided fresh | — |  |
| 5707 | Add a scanner for process parameters in application logs | SF-RP-005 | permitted | decided fresh | — |  |
| 5708 | Surface the applicable ECCN on the supplier portal download page | SF-EX-007 | denied | bound by precedent | REC-S0126 |  |
| 5709 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 5710 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-002 | permitted | decided fresh | — |  |
| 5711 | Move key material into the hardware security module | SF-CR-003 | permitted | decided fresh | — |  |
| 5712 | Pin the certificate chain used by the metrology ingest client | SF-CR-003 | permitted | decided fresh | — |  |
| 5713 | Let compliance edit the export determination after the shipment closes | SF-EX-004 SF-CR-003 ⛔ | denied | refused at the floor | — |  |
| 5714 | Canonicalise the upload path before the handler opens the file | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5715 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | disposed by citation | — |  |
| 5716 | Remove the human-review requirement from the screening provision | SF-AS-003 | denied | decided fresh | — |  |
| 5717 | Point every site's tool logs at the single global log sink | SF-DS-003 | denied | decided fresh | — |  |
| 5718 | Return a correlation id instead of a stack trace to the client | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5719 | Let the agent's enrichment step call an outside classification API | SF-AG-002 ⛔ | denied | refused at the floor | — |  |
| 5720 | Let the shipment proceed when the screening service returns a timeout | SF-EX-006 SF-SS-003 ⛔ | denied | refused at the floor | — |  |
| 5721 | Grant read access to the radar-front-end design repository to a contractor holding a non-US passport | SF-IT-002 | denied | decided fresh | — |  |
| 5722 | Rotate the recipe vault envelope key on the published schedule | SF-RP-004 | permitted | decided fresh | — |  |
| 5723 | Record the percentile family used for the declared budget | SF-RT-006 | permitted with conditions | decided fresh | — | ● |
| 5724 | Restore the lock around the WIP snapshot read-modify-write | SF-TQ-002 | permitted | decided fresh | — |  |
| 5725 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 SF-SS-007 ⛔ | denied | refused at the floor | — |  |
| 5726 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-001 SF-AG-003 ⛔ | denied | refused at the floor | — |  |
| 5727 | Rate-limit the supplier portal's document download endpoint | SF-AS-001 | permitted | decided fresh | — |  |
| 5728 | Store the superseded metrology value beside its correction | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5729 | Bound the debug endpoint to recipe identifiers, not bodies | SF-RP-007 | permitted | decided fresh | — |  |
| 5730 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-005 | denied | decided fresh | — |  |
| 5731 | Keep the HSMS reply timeout inside the declared bound | SF-SG-008 | permitted | decided fresh | — |  |
| 5732 | Update the supply chain risk plan after the vendor change | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5733 | Restrict the webhook fetcher to the registered supplier hosts | — | permitted | docketed — nothing engaged | — |  |
| 5734 | Allowlist the export format instead of shelling out with user input | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5735 | Replace the CBC-mode envelope with an AEAD construction | SF-CR-002 | permitted | decided fresh | — |  |
| 5736 | Pin the certificate chain used by the metrology ingest client | SF-CR-002 | permitted | decided fresh | — |  |
| 5737 | Split the slow enrichment step out of the alarm path | SF-RT-007 | permitted | decided fresh | — |  |
| 5738 | Close the check-then-open window in the metrology file handler | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5739 | Gate the important-data export on the completed security assessment | SF-DS-007 | permitted | decided fresh | — |  |
| 5740 | Restrict the agent runner to the allowlisted internal hosts | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5741 | Route every screening near-miss to a named compliance reviewer | SF-EX-007 | permitted | decided fresh | — |  |
| 5742 | Capture the licence determination rationale in the trade record | SF-EX-007 | permitted | decided fresh | — |  |
| 5743 | Route the agent's tool-gateway patch to two human reviewers | SF-AG-008 | permitted | decided fresh after a tie | none_tie |  |
| 5744 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-007 | permitted | decided fresh after a tie | none_tie |  |
| 5745 | Edit the deny predicate for the deemed-export provision | SF-SG-003 | denied | decided fresh | — |  |
| 5746 | Record the equipment reply that failed to parse, with its raw bytes | SF-SG-009 | permitted | decided fresh | — | ● |
| 5747 | Remove the verification-of-effectiveness step from the corrective-action workflow | SF-QS-001 | denied | decided fresh | — |  |
| 5748 | Make export decisions append-only in the trade compliance ledger | SF-EX-011 | permitted | decided fresh | — |  |
| 5749 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-003 SF-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5750 | Keep audit logging on during the throughput optimisation | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5751 | Round emissions report values down to the nearest permit-limit increment | SF-EH-003 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 5752 | Add the destination geofence to the design-file download path | SF-EX-009 | permitted | decided fresh | — |  |
| 5753 | Surface unparsed equipment replies instead of dropping them | SF-SG-010 | permitted | decided fresh | — |  |
| 5754 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-010 | permitted | decided fresh | — |  |
| 5755 | Retire the legacy gas-alarm rate limiter that pre-dated the life-safety panel wiring | SF-EH-004 | permitted | decided fresh | — |  |
| 5756 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5757 | Canonicalise the upload path before the handler opens the file | SF-AS-007 | permitted | docketed — not charged | — |  |
| 5758 | Add secret scanning to the pre-merge pipeline | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 5759 | Record the builder identity in the release attestation | SF-SS-007 | permitted with conditions | decided fresh | — | ● |
| 5760 | Classify a routine parameter tweak as minor after confirming it carries no customer-facing effect | SF-QS-001 | permitted | decided fresh | — |  |
| 5761 | Wire a rollback path into every controller-model promotion | SF-QS-001 | permitted | decided fresh | — |  |
| 5762 | Add a GEM control-state transition test for the Lam etcher | SF-SG-004 | permitted | bound by precedent | REC-S0114 |  |
| 5763 | Bind the mask revision to its lot and recipe record | SF-QS-003 | permitted with conditions | decided fresh | — | ● |
| 5764 | Require the licence exception paragraph on the shipment record | SF-EX-011 | permitted | decided fresh | — |  |
| 5765 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | disposed by citation | — |  |
| 5766 | Exclude audit findings from the retrieval query | SF-GV-005 | permitted | decided fresh | — | ● |
| 5767 | Bound the SECS message queue depth per tool connection | SF-SG-006 | permitted with conditions | decided fresh | — | ● |
| 5768 | Add the CHIPS notification duty to the compliance rulebook | SF-RP-003 | denied | decided fresh | — |  |
| 5769 | Version collection-event identifiers instead of renumbering them | SF-SG-010 | permitted | decided fresh | — | ● |
| 5770 | Add the destination geofence to the design-file download path | SF-EX-013 | permitted | decided fresh | — |  |
| 5771 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | decided fresh | — |  |
| 5772 | Rate-limit the supplier portal's document download endpoint | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5773 | Report load conditions alongside the p99.9 measurement | SF-RT-004 | permitted | decided fresh | — |  |
| 5774 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5775 | Capture customer acknowledgement on the change notice before release | SF-QS-003 | permitted | decided fresh | — |  |
| 5776 | Publish the EDA toolchain image without running the classification step | SF-EX-009 | denied | decided fresh | — |  |
| 5777 | Add a licence-exception clause to the trade compliance rulebook | SF-DS-006 | denied | decided fresh | — |  |
| 5778 | Verify component digests against the registry before deploy | SF-SS-005 | permitted | decided fresh | — |  |
| 5779 | Stop shipping equipment logs across the boundary by default | SF-DS-007 | permitted | decided fresh | — |  |
| 5780 | Document the invariant the metrology ingest lock protects | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5781 | Tag CUI-bearing tables in the data platform catalogue | SF-NC-006 | denied | bound by precedent | REC-S0200 |  |
| 5782 | Record the ECCN determination alongside the design-file upload | SF-EX-008 | permitted | decided fresh | — |  |
| 5783 | Add a residency assertion to the metrology ingest contract | SF-DS-007 | permitted | decided fresh | — |  |
| 5784 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5785 | Purge recipe execution records older than ninety days | SF-WI-001 SF-TQ-001 ⛔ | denied | refused at the floor | — |  |
| 5786 | Split the slow enrichment step out of the alarm path | SF-RT-004 | permitted | decided fresh | — |  |
| 5787 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | decided fresh | — |  |
| 5788 | Authenticate recipe-transfer messages before the tool accepts them | SF-SG-005 | permitted | decided fresh | — | ● |
| 5789 | Document the sub-processor chain for the supplier portal CDN | SF-DS-005 | permitted | decided fresh | — |  |
| 5790 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 5791 | Sign the container image published for the edge tool gateway | SF-SS-004 | permitted | decided fresh | — |  |
| 5792 | Stage a firmware update on a non-production tool before the fleet rollout | SF-OT-002 | permitted | decided fresh | — |  |
| 5793 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5794 | Batch alarm reports into the five-second telemetry flush | SF-SG-009 | denied | decided fresh | — | ● |
| 5795 | Bump the SECS toolkit and pick up its new transitive parser | SF-SS-008 | denied | decided fresh | — | ● |
| 5796 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 5797 | Fail the pipeline closed when the screening service times out | SF-EX-007 | permitted | decided fresh | — | ● |
| 5798 | Pin the denied-party list snapshot used by a screening decision | SF-EX-012 | denied | bound by precedent | REC-S0118 |  |
| 5799 | Add a config flag that disables the destination geofence for demos | SF-EX-012 | denied | decided fresh | — |  |
| 5800 | Downgrade a forced-labour list match to an advisory warning instead of a block | SF-RS-001 | denied | decided fresh | — |  |
| 5801 | Correct for coordinated omission in the ingest benchmark | SF-RT-004 | permitted with conditions | decided fresh | — | ● |
| 5802 | Record the exception authority against the accepting principal | SF-GV-007 | permitted | decided fresh | — |  |
| 5803 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5804 | Attach qualification evidence to every process-change record | SF-QS-003 | permitted | decided fresh | — | ● |
| 5805 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-005 | permitted | decided fresh | — |  |
| 5806 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5807 | Move the charging threshold for the supply chain family | SF-OT-004 | denied | decided fresh | — |  |
| 5808 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-006 | permitted | decided fresh | — |  |
| 5809 | Encrypt the recipe payload at rest in the vault | SF-RP-003 | permitted | decided fresh | — |  |
| 5810 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-003 | permitted with conditions | decided fresh | — | ● |
| 5811 | Publish the measurement window with the latency result | SF-RT-007 | denied | bound by precedent | REC-S0164 |  |
| 5812 | Let the retention sweep run across lots that are under legal hold | SF-DS-002 SF-RP-006 ⛔ | denied | refused at the floor | — |  |
| 5813 | Fix the deadlock between the alarm writer and the snapshot reader | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5814 | Replace the racy counter with an atomic in the ingest fanout | SF-TQ-003 | permitted | decided fresh | — |  |
| 5815 | Block a retired mask revision from dispatch to the exposure tool | SF-QS-004 | permitted | decided fresh | — |  |
| 5816 | Parameterise the supplier portal's lot-search query | SF-AS-006 | permitted | docketed — not charged | — |  |
| 5817 | Block the merge on the critical CVE in the ingest dependency | SF-SS-005 | permitted | decided fresh | — |  |
| 5818 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5819 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-007 | denied | decided fresh | — | ● |
| 5820 | Escape the tenant name rendered on the supplier portal dashboard | — | permitted | docketed — nothing engaged | — |  |
| 5821 | Run each build job on a fresh ephemeral runner | SF-SS-007 | permitted with conditions | decided fresh | — | ● |
| 5822 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5823 | Log the full recipe body when a tool rejects a transfer | SF-RP-001 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 5824 | Correct for coordinated omission in the ingest benchmark | SF-RT-002 | permitted | decided fresh after a tie | none_tie |  |
| 5825 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5826 | Restrict the webhook fetcher to the registered supplier hosts | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5827 | Pin the JVM collector so pause times stay inside the budget | SF-RT-004 | permitted | decided fresh | — |  |
| 5828 | Raise the HSMS reply timeout to stop the scanner dropping sessions | SF-SG-003 | denied | decided fresh | — |  |
| 5829 | Correct for coordinated omission in the ingest benchmark | SF-RT-003 | permitted | decided fresh | — |  |
| 5830 | Hold agent edits to the screening logic for compliance review | SF-AG-003 | permitted | decided fresh | — |  |
| 5831 | Capture the licence determination rationale in the trade record | SF-EX-007 | permitted | decided fresh | — |  |
| 5832 | Add secret scanning to the pre-merge pipeline | SF-SS-011 | permitted with conditions | decided fresh | — | ● |
| 5833 | Expand the classification questionnaire for multi-patterning masks | SF-EX-011 | permitted | decided fresh | — |  |
| 5834 | Sign the container image published for the edge tool gateway | SF-SS-010 | permitted with conditions | decided fresh | — | ● |
| 5835 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-002 ⛔ | denied | refused at the floor | — |  |
| 5836 | Exclude recipe bodies from the vendor support bundle | SF-RP-005 | permitted | decided fresh | — |  |
| 5837 | Bound the request body size on the yield analytics endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5838 | Replace the direct-URL dependency with a registry release | SF-SS-011 | permitted | decided fresh | — |  |
| 5839 | Pull the ingest parser from a mirror whose digest no longer matches | SF-SS-005 | denied | decided fresh | — |  |
| 5840 | Carry the regulatory hold flag through the archive migration | SF-WI-003 | permitted | decided fresh | — |  |
| 5841 | Correct for coordinated omission in the ingest benchmark | SF-RT-006 | permitted | decided fresh | — |  |
| 5842 | Scope the internal SECS parser package to the private registry | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5843 | Scope the internal SECS parser package to the private registry | SF-SS-004 | permitted | decided fresh | — |  |
| 5844 | Add a residency assertion to the metrology ingest contract | SF-DS-006 | permitted with conditions | decided fresh | — | ● |
| 5845 | Surface the applicable ECCN on the supplier portal download page | SF-EX-011 | permitted | decided fresh | — |  |
| 5846 | Force the etcher to offline control state during the gateway deploy | SF-SG-001 SF-IT-002 ⛔ | denied | refused at the floor | — |  |
| 5847 | Preserve S6F11 event ordering under broker backpressure | SF-SG-006 | permitted | decided fresh | — |  |
| 5848 | Allowlist the export format instead of shelling out with user input | SF-AS-002 | permitted | decided fresh | — |  |
| 5849 | Delete the held lot's genealogy during the archive cleanup | SF-WI-002 SF-RT-007 ⛔ | denied | refused at the floor | — |  |
| 5850 | Record the lawful basis for the Hsinchu-to-Hillsboro yield feed | SF-DS-005 | permitted with conditions | decided fresh | — | ● |
| 5851 | Escrow the design-file decryption key with the offshore CDN provider | SF-EX-005 SF-SS-004 ⛔ | denied | refused at the floor | — |  |
| 5852 | Strengthen the memory ordering on the sequence-number publish | — | permitted | docketed — nothing engaged | — |  |
| 5853 | Record the agent identity and model version on the pull request | SF-AG-005 | permitted | decided fresh | — |  |
| 5854 | Make the screening gate's denial final with no review route | SF-GV-001 ⛔ | denied | refused at the floor | — |  |
| 5855 | Propose deferring the sovereignty provision to the next assessment cycle | SF-QS-003 | denied | decided fresh | — |  |
| 5856 | Let the contract template parser accept a boycott-compliance clause unmodified | SF-SO-002 ⛔ | denied | refused at the floor | — |  |
| 5857 | Canonicalise the upload path before the handler opens the file | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5858 | Store the superseded metrology value beside its correction | SF-WI-006 | permitted | decided fresh | — |  |
| 5859 | Let a shipment be marked licence-exempt without naming the exception paragraph | SF-EX-004 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 5860 | Add a stress test that runs the broker under concurrent tool load | SF-TQ-001 | permitted | decided fresh | — |  |
| 5861 | Replace the pickle payload with a schema-validated JSON body | — | permitted | docketed — nothing engaged | — |  |
| 5862 | Move recipe transfer onto the mutually authenticated channel | SF-RP-005 | permitted | decided fresh | — |  |
| 5863 | Version collection-event identifiers instead of renumbering them | SF-SG-007 | permitted | decided fresh | — |  |
| 5864 | Record the builder identity in the release attestation | SF-SS-010 | permitted | disposed by citation | — |  |
| 5865 | Add a contract test on the path axis for the agent's new endpoint | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5866 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-013 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5867 | Filter the interlock signal out of the noisy alarm stream | SF-SG-008 | denied | decided fresh | — |  |
| 5868 | Allow TLS 1.0 on the tool gateway for the Kumamoto equipment | SF-CR-001 SF-RT-005 ⛔ | denied | refused at the floor | — |  |
| 5869 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-001 | permitted | decided fresh | — |  |
| 5870 | Capture the licence determination rationale in the trade record | SF-EX-011 | permitted | decided fresh | — |  |
| 5871 | Propose a new provision covering advanced-node lithography data | SF-SS-010 | denied | decided fresh | — |  |
| 5872 | Log the deemed-export check that runs at repository role grant | SF-EX-011 | permitted | decided fresh | — |  |
| 5873 | Surface unparsed equipment replies instead of dropping them | SF-SG-005 | denied | bound by precedent | REC-S0124 |  |
| 5874 | Overwrite the supplier declaration record in place instead of versioning it | SF-RS-004 | denied | decided fresh | — | ● |
| 5875 | Deliver alarm reports ahead of the collection-event budget | SF-SG-009 | permitted | decided fresh | — |  |
| 5876 | Add the CHIPS notification duty to the compliance rulebook | SF-EX-009 | denied | decided fresh | — |  |
| 5877 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-002 | permitted | decided fresh | — | ● |
| 5878 | Pull tool firmware updates from an unverified community mirror | SF-OT-001 | denied | decided fresh | — |  |
| 5879 | Route every screening near-miss to a named compliance reviewer | SF-EX-009 | permitted | decided fresh | — |  |
| 5880 | Record the agent identity and model version on the pull request | SF-AG-008 | permitted | decided fresh | — |  |
| 5881 | Block the merge on the critical CVE in the ingest dependency | SF-SS-002 | permitted | decided fresh | — |  |
| 5882 | Downsample cleanroom particle-count telemetry without recording the change | SF-EH-004 | denied | decided fresh | — |  |
| 5883 | Post a compensating entry instead of editing the WIP status | SF-WI-005 | permitted | decided fresh | — |  |
| 5884 | Document the CUI boundary for the metrology ingest service | SF-NC-004 | permitted | decided fresh | — |  |
| 5885 | Add the newly pulled component to the generated SBOM | SF-SS-005 | permitted | decided fresh | — |  |
| 5886 | Rate-limit the supplier portal's document download endpoint | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5887 | Run each build job on a fresh ephemeral runner | SF-SS-009 | permitted | decided fresh | — |  |
| 5888 | Drop the deprecated field from the agent's regenerated response body | SF-AG-002 SF-AG-004 ⛔ | denied | refused at the floor | — |  |
| 5889 | Document the CUI boundary for the metrology ingest service | SF-NC-003 | denied | bound by precedent | REC-S0197 |  |
| 5890 | Record who amended the CD-SEM measurement and why | SF-WI-006 | permitted with conditions | bound by precedent | REC-S0098 |  |
| 5891 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-007 | denied | decided fresh | — |  |
| 5892 | Return a correlation id instead of a stack trace to the client | — | permitted | docketed — nothing engaged | — |  |
| 5893 | Honour the regulatory hold ahead of the retention sweep | SF-DS-005 | permitted | decided fresh | — | ● |
| 5894 | Block the merge on the critical CVE in the ingest dependency | SF-SS-009 | permitted | disposed by citation | — |  |
| 5895 | Keep recipe execution records until the retention clock expires | SF-WI-007 | permitted with conditions | decided fresh | — | ● |
| 5896 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5897 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5898 | Rename the lot-detail route in the agent's generated router | SF-AG-003 | denied | decided fresh | — |  |
| 5899 | Emit one docket entry for every arrival the prosecutor declines | SF-GV-005 | permitted | decided fresh | — |  |
| 5900 | Replace the blocking lookup with a pre-warmed cache read | SF-RT-005 | permitted | decided fresh | — |  |
| 5901 | Reclassify the recipe-protection provision as advisory | SF-SS-003 | denied | decided fresh | — |  |
| 5902 | Canonicalise the upload path before the handler opens the file | SF-AS-004 | permitted | docketed — not charged | — |  |
| 5903 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted with conditions | decided fresh | — | ● |
| 5904 | Add a retention-hold check to the record destruction job | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5905 | Publish the measurement window with the latency result | SF-RT-005 | denied | bound by precedent | REC-S0128 |  |
| 5906 | Accept the agent's rebase that skips the failing screening test | SF-AG-002 SF-SG-005 ⛔ | denied | refused at the floor | — |  |
| 5907 | Record the builder identity in the release attestation | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5908 | Add an authorisation check to the lot-detail API | SF-AS-003 | permitted | decided fresh | — |  |
| 5909 | Attach qualification evidence to every process-change record | SF-QS-001 | permitted with conditions | decided fresh | — | ● |
| 5910 | Add a software filter that suppresses repeated hazardous-gas alarm pages | SF-EH-001 ⛔ | denied | refused at the floor | — |  |
| 5911 | Bound the telemetry buffer so ingest backpressure is visible | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 5912 | Order the two mutex acquisitions consistently across both paths | SF-TQ-007 | permitted | docketed — not charged | — |  |
| 5913 | Honour the regulatory hold ahead of the retention sweep | SF-DS-007 | permitted with conditions | decided fresh | — | ● |
| 5914 | Pin the transitive dependency graph for the metrology ingest service | SF-SS-009 | permitted | decided fresh | — | ● |
| 5915 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |
| 5916 | Evaluate the foreign direct product rule before the artifact publishes | SF-EX-011 | permitted | decided fresh | — |  |
| 5917 | Restrict certificate key types to the permitted set | SF-CR-005 | permitted | decided fresh | — |  |
| 5918 | Add a race detector run to the telemetry pipeline CI job | — | permitted | docketed — nothing engaged | — |  |
| 5919 | Post a compensating entry instead of editing the WIP status | SF-WI-006 | permitted | decided fresh | — |  |
| 5920 | Feed the etch recipe into the yield assistant's prompt context | SF-RP-001 SF-RT-004 ⛔ | denied | refused at the floor | — |  |
| 5921 | Accept receipt of a lot whose supplier attestation expired last quarter | SF-RS-004 | denied | decided fresh | — |  |
| 5922 | Tag every WIP record with the jurisdiction that produced it | SF-DS-003 | permitted | decided fresh | — |  |
| 5923 | Reject signatures the verifier previously accepted by mistake | SF-CR-003 | permitted | decided fresh | — |  |
| 5924 | Add a conformance test for the ASML scanner's S1F13 handshake | SF-SG-010 | permitted | decided fresh | — |  |
| 5925 | Sign the container image published for the edge tool gateway | SF-SS-011 | denied | bound by precedent | REC-S0166 |  |
| 5926 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5927 | Add an authorisation check to the lot-detail API | SF-AS-003 | permitted | decided fresh | — |  |
| 5928 | Run each build job on a fresh ephemeral runner | SF-SS-010 | permitted | decided fresh | — |  |
| 5929 | Scope the internal SECS parser package to the private registry | SF-SS-008 | permitted | bound by precedent | REC-S0104 |  |
| 5930 | Add the newly pulled component to the generated SBOM | SF-SS-011 | permitted | decided fresh | — |  |
| 5931 | Weight supplier terms against firms the model scores as distressed | SF-GV-003 | denied | decided fresh | — |  |
| 5932 | Declare the processing region for the new metrology sub-processor | SF-DS-003 | permitted with conditions | decided fresh | — | ● |
| 5933 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-004 | permitted | decided fresh | — |  |
| 5934 | Move the alarm-fanout write off the monitoring hot path | SF-RT-001 | permitted with conditions | decided fresh | — | ● |
| 5935 | Route every screening near-miss to a named compliance reviewer | SF-EX-013 | permitted | decided fresh | — |  |
| 5936 | Return the exception detail to the portal so suppliers can self-diagnose | SF-AS-002 | denied | decided fresh | — |  |
| 5937 | Publish the measurement window with the latency result | SF-RT-003 | permitted | bound by precedent | REC-S0102 |  |
| 5938 | Add the newly pulled component to the generated SBOM | SF-SS-007 | permitted | decided fresh | — |  |
| 5939 | Record the ECCN determination alongside the design-file upload | SF-EX-012 | permitted with conditions | decided fresh | — | ● |
| 5940 | Attach assessment evidence to the claimed access control | SF-NC-001 | permitted | bound by precedent | REC-S0195 |  |
| 5941 | Require OT-owner review before a zone-boundary firewall rule changes | SF-OT-003 | permitted with conditions | decided fresh | — | ● |
| 5942 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-004 | denied | decided fresh | — |  |
| 5943 | Assert the safety interlock signal survives the gateway refactor | SF-SG-005 | permitted | disposed by citation | — |  |
| 5944 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-004 | permitted | decided fresh | — |  |
| 5945 | Re-screen consignees on the published list-refresh cadence | SF-EX-008 | permitted | decided fresh | — |  |
| 5946 | Purge recipe execution records older than ninety days | SF-WI-002 SF-AS-003 ⛔ | denied | refused at the floor | — |  |
| 5947 | Link the agent's change to the originating engineering ticket | SF-AG-004 | permitted | decided fresh | — |  |
| 5948 | Swap the copyleft trace parser for a permissively licensed one | SF-SS-008 | permitted | disposed by citation | — |  |
| 5949 | Pin the denied-party list snapshot used by a screening decision | SF-EX-010 | permitted | decided fresh | — |  |
| 5950 | Document the invariant the metrology ingest lock protects | SF-TQ-006 | permitted | docketed — not charged | — |  |
| 5951 | Add a residency assertion to the metrology ingest contract | SF-DS-005 | permitted | decided fresh | — | ● |
| 5952 | Add the pilot line to the CUI boundary documentation | SF-NC-002 | denied | bound by precedent | REC-S0196 |  |
| 5953 | Bound the collector's allocation rate on the ingest path | SF-RT-001 | permitted | decided fresh | — | ● |
| 5954 | Make the lot-genealogy cache update atomic with its invalidation | SF-TQ-004 | permitted | decided fresh | — |  |
| 5955 | Exempt distributor accounts from the sanctions screening step | SF-SO-001 SF-SS-007 ⛔ | denied | refused at the floor | — |  |
| 5956 | Reclassify the agent-authorship provision as absolute | SF-DS-006 | denied | decided fresh | — |  |
| 5957 | Let the agent act on the instructions pasted into the supplier ticket | SF-AG-007 | denied | decided fresh | — |  |
| 5958 | Bound the request body size on the yield analytics endpoint | SF-AS-002 | permitted | decided fresh | — |  |
| 5959 | Run each build job on a fresh ephemeral runner | SF-SS-006 | permitted | decided fresh | — | ● |
| 5960 | Make export decisions append-only in the trade compliance ledger | SF-EX-012 | permitted | decided fresh | — |  |
| 5961 | Split the slow enrichment step out of the alarm path | SF-RT-005 | permitted with conditions | decided fresh | — | ● |
| 5962 | Disable the PFAS emissions reporting job during the maintenance window | SF-EH-004 | denied | decided fresh | — | ● |
| 5963 | Open a corrective-action record for every nonconformance | SF-QS-002 | permitted | decided fresh | — |  |
| 5964 | Require a human sign-off before an agent edits equipment control code | SF-AG-004 | permitted | decided fresh after a tie | none_tie |  |
| 5965 | Post a compensating entry instead of editing the WIP status | SF-WI-004 | permitted with conditions | decided fresh | — | ● |
| 5966 | Route Kumamoto tool logs to the in-region log sink | SF-DS-006 | permitted | decided fresh | — |  |
| 5967 | Add the new data flow to the system security plan diagram | SF-NC-004 | permitted | bound by precedent | REC-S0198 |  |
| 5968 | Open the joint-venture data-share pipeline ahead of the counterparty determination | SF-SO-002 SF-AS-003 ⛔ | denied | refused at the floor | — |  |
| 5969 | Add the newly pulled component to the generated SBOM | SF-SS-010 | permitted | decided fresh | — |  |
| 5970 | Order the two mutex acquisitions consistently across both paths | SF-TQ-005 | permitted | docketed — not charged | — |  |
| 5971 | Attach the provenance attestation to the tool-gateway release | SF-SS-004 | permitted | disposed by citation | — |  |
| 5972 | Retry S2F41 remote commands without reordering the queue | SF-SG-006 | permitted | decided fresh | — |  |
| 5973 | Attach the provenance attestation to the tool-gateway release | SF-SS-006 | permitted | disposed by citation | — |  |
| 5974 | Sign the container image published for the edge tool gateway | SF-SS-010 | permitted | decided fresh | — | ● |
| 5975 | Let the shipment proceed when the screening service returns a timeout | SF-EX-012 | denied | decided fresh | — |  |
| 5976 | Record who amended the CD-SEM measurement and why | SF-WI-003 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 5977 | Accept the vendor's 1024-bit RSA client certificate | SF-CR-003 | denied | decided fresh | — |  |
| 5978 | Scope the internal SECS parser package to the private registry | SF-SS-002 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5979 | Restrict the webhook fetcher to the registered supplier hosts | — | permitted | docketed — nothing engaged | — |  |
| 5980 | Stand up a read replica of the design store in the Shenzhen region | SF-EX-001 ⛔ | denied | refused at the floor | — |  |
| 5981 | Return a correlation id instead of a stack trace to the client | SF-AS-002 | permitted | bound by precedent | REC-S0110 |  |
| 5982 | Generate the SBOM from the direct dependency list only | SF-SS-005 | denied | decided fresh | — |  |
| 5983 | Sign the container image published for the edge tool gateway | SF-SS-009 | permitted with conditions | decided fresh | — | ● |
| 5984 | Sign the container image published for the edge tool gateway | SF-SS-006 | permitted | decided fresh | — | ● |
| 5985 | Benchmark the broker with an open-loop client and report the median | SF-RT-002 | denied | decided fresh | — | ● |
| 5986 | Strengthen the memory ordering on the sequence-number publish | SF-TQ-001 | permitted | decided fresh | — |  |
| 5987 | Add a race detector run to the telemetry pipeline CI job | SF-TQ-002 | permitted | decided fresh | — |  |
| 5988 | Hold agent edits to the screening logic for compliance review | SF-AG-006 | permitted | decided fresh after a tie | none_tie |  |
| 5989 | Benchmark the broker under full-fab message load, not a single tool | SF-RT-003 | permitted with conditions | decided fresh | — | ● |
| 5990 | Return the exception detail to the portal so suppliers can self-diagnose | SF-AS-002 | denied | decided fresh | — | ● |
| 5991 | Attach supply-chain tracing evidence to every flagged lot | SF-RS-004 | permitted | decided fresh | — | ● |
| 5992 | Report load conditions alongside the p99.9 measurement | SF-RT-001 | permitted | decided fresh | — | ● |
| 5993 | Let the defence-article transfer proceed without naming a licence or exemption paragraph | SF-IT-003 SF-TQ-001 ⛔ | denied | refused at the floor | — |  |
| 5994 | Hash the recipe identifier before it reaches the analytics store | SF-RP-004 | permitted | decided fresh | — | ● |
| 5995 | Attach the provenance attestation to the tool-gateway release | SF-SS-003 | permitted | decided fresh | — |  |
| 5996 | Surface unparsed equipment replies instead of dropping them | SF-SG-003 | permitted | disposed by citation | — |  |
| 5997 | Verify component digests against the registry before deploy | SF-SS-002 | permitted | decided fresh | — |  |
| 5998 | Shorten the WIP record retention term in the rulebook | SF-IT-004 | denied | decided fresh | — |  |
| 5999 | Mask implant dose values in the yield analytics export | SF-RP-007 | permitted | decided fresh after a tie | none_tie |  |
| 6000 | Escape the tenant name rendered on the supplier portal dashboard | SF-AS-005 | permitted | docketed — not charged | — |  |

⛔ marks a change that engaged an absolute provision — a floor no officer of this organisation has the authority to waive.

## How to check any of this

```
python3 harness/run_conformance.py     # 44 checks over the executed trace
python3 harness/mutation_matrix.py     # evidence the checks can fail
bash reproduce/run_all.sh              # rebuild everything, deterministically
```

Every row above is produced by replaying the corpus through `harness/engine.py`. No row is copied from an authored expectation, so the ledger cannot drift from the corpus files.
