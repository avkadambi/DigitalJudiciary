# VetPOC Constitution — the simulation, read end to end

Corpus 2.1.0 · rulebook vetpoc-rb-000001 · 6,000 proposed code changes · Apache-2.0 (code) + CC BY 4.0 (data)

## What this document is

This is the whole run in plain English. A simulated engineering organisation proposed five thousand code changes, one after another, and an adjudicator governed by a written constitution decided every one of them. Nothing here is an intention or a specification: every disposition below is what the reference engine actually did when the corpus was replayed, and the ledger at the end lists all five thousand changes with the answer each one got.

Read it as you would read a docket. The interesting part is not that the adjudicator said no to bad changes — a linter does that. It is that when a change was contested and resolved, the decision was written down, and the next materially identical change was **bound** by it.

## The firm and its constitution

An open constitution for veterinary practice-management and point-of-care software, expressed as ordinary and absolute provisions in the sense of Chapter 5, Definition 1 of the Digital Judiciary programme.

| | |
| :--- | ---: |
| Provisions | 121 |
| — of them absolute | 26 |
| Provision families | 18 |
| Opening precedent records | 197 |
| Records written during the run | 922 |
| Final store | 1119 |
| Retrieval threshold θ | 0.25 |


## The run in numbers

| The answer given | Changes |
| :--- | ---: |
| permitted | 3,655 |
| denied | 1,578 |
| permitted with conditions | 767 |

| How the answer was reached | Changes |
| :--- | ---: |
| decided fresh | 3,729 |
| bound by precedent | 1,189 |
| refused at the floor | 398 |
| docketed — not charged | 345 |
| decided fresh after a tie | 145 |
| disposed by citation | 131 |
| docketed — nothing engaged | 63 |

## How the run unfolded

The case base starts almost empty and grows only when a decision is contested and resolved above the first instance. That is the whole mechanism, and its consequence is visible in the run: early changes are mostly decided fresh, and later ones are increasingly decided by citing a decision the organisation already made.

| Fifth of the run | Changes | Bound by precedent | Share | New records | Refused at a floor |
| :--- | :--- | ---: | ---: | ---: | ---: |
| 1 | 1–1,200 | 198 | 16.5% | 173 | 77 |
| 2 | 1,201–2,400 | 523 | 43.6% | 173 | 48 |
| 3 | 2,401–3,600 | 270 | 22.5% | 190 | 87 |
| 4 | 3,601–4,800 | 97 | 8.1% | 203 | 84 |
| 5 | 4,801–6,000 | 101 | 8.4% | 183 | 102 |

Precedent goes from **16.5%** of changes in the first fifth to **8.4%** in the last. Nothing was tuned to produce that: it is what contest-gated admission does to a stream of changes over time.

## Twelve changes, read in full

One of each kind, taken from the run rather than chosen for effect — the first case of each category, whatever it happens to be.

### VP-A-00002 — *Configure retention periods per jurisdiction in the scheduler*

**Why this kind of change is in the run.** An ordinary change that engages a provision and breaks nothing.

**What it touched.** The records export service in the records area, filed by an AI coding agent. It engaged `VP-RR-007`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### VP-B-00013 — *Cut access-log retention to thirty days to save storage costs*

**Why this kind of change is in the run.** An unarguable violation nobody contests.

**What it touched.** The audit ledger in the records area, filed by an AI coding agent. It engaged `VP-BN-002`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### VP-C-00939 — *Configure retention periods per jurisdiction in the scheduler*

**Why this kind of change is in the run.** The case that makes this a judiciary: a prior decision controls.

**What it touched.** The retention scheduler in the records area, filed by an AI coding agent. It engaged `VP-RR-004`.

**What happened.** The change was bound by precedent and permitted, controlled by record `REC-VP-A-00285`. Nothing was stored: the decision is final and leaves no precedent.

### VP-E-00023 — *Record the witnessing licensee on every euthanasia-solution dispense*

**Why this kind of change is in the run.** The near-miss the system must refuse to follow.

**What it touched.** The identity service in the records area, filed by a named engineer. It engaged `VP-CS-012`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### VP-D-00015 — *Scope modality worklist queries to the requesting practice*

**Why this kind of change is in the run.** Two prior decisions disagree and one ordering key decides.

**What it touched.** The lab results formatter in the alerting area, filed by an AI coding agent. It engaged `VP-PO-005`.

**What happened.** The change was bound by precedent and denied, controlled by record `REC-S0118`. Nothing was stored: the decision is final and leaves no precedent.

### VP-F-00003 — *Add a per-tenant slider for the breach-notification deadline*

**Why this kind of change is in the run.** A floor: refused before any retrieval happens.

**What it touched.** The audit ledger in the org area, filed by an AI coding agent. It engaged `VP-BN-001`, `VP-GV-003`.

**What happened.** The change was refused at the floor. Nothing was stored: the decision is final and leaves no precedent.

### VP-G-00012 — *Bound HL7 segment length before the ORU^R01 parser runs*

**Why this kind of change is in the run.** The automated tiers are exhausted and a named human accepts the risk.

**What it touched.** The dicom router in the alerting area, filed by an AI coding agent. It engaged `VP-PO-010`.

**What happened.** The change was decided fresh and permitted with conditions; escalation was exhausted and the named risk owner accepted the residual risk. The decision was written into the case base and binds later materially identical changes.

### VP-H-00005 — *Register the new agent runner in the allowlist policy bundle*

**Why this kind of change is in the run.** A change to the rulebook itself, routed to an amendment.

**What it touched.** The client portal api in the records area, filed by an AI coding agent. It engaged `VP-PD-007`.

**What happened.** The change was decided fresh and denied. Nothing was stored: the decision is final and leaves no precedent.

### VP-K-00054 — *Check consent currency before the reminder engine sends*

**Why this kind of change is in the run.** Two records tie on every key and the trail says so.

**What it touched.** The billing ledger in the analytics area, filed by an AI coding agent. It engaged `VP-PD-007`.

**What happened.** The change was decided fresh after a tie and permitted, controlled by record `none_tie`, with the trail recording none(tie) rather than an absence of authority. Nothing was stored: the decision is final and leaves no precedent.

### VP-P-00009 — *Populate DICOM species and breed tags from the patient record*

**Why this kind of change is in the run.** The twin of a control case, carrying a pressure argument.

**What it touched.** The hl7 ingest in the alerting area, filed by a named engineer. It engaged `VP-PO-009`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

### VP-L-00024 — *Attach build provenance to the practice API release artefact*

**Why this kind of change is in the run.** Co-pending changes decided once and cited.

**What it touched.** The client portal api in the platform area, filed by a named engineer. It engaged `VP-SC-001`.

**What happened.** The change was decided fresh and permitted. The decision was written into the case base and binds later materially identical changes.

### VP-I-00058 — *Record the lawful basis for the EU-to-US analytics transfer*

**Why this kind of change is in the run.** An expired acceptance is cited and must not be followed.

**What it touched.** The payment tokenizer in the portal area, filed by a named engineer. It engaged `VP-PD-004`.

**What happened.** The change was decided fresh and permitted. Nothing was stored: the decision is final and leaves no precedent.

## What happened to each kind of change

| Kind of change | Changes | Permitted | Denied | With conditions | Bound by precedent | Became precedent |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| A-routine | 696 | 696 | 0 | 0 | 0 | 88 |
| B-plain-deny | 372 | 0 | 372 | 0 | 2 | 67 |
| C-precedent | 576 | 267 | 182 | 127 | 576 | 134 |
| D-ordering | 204 | 68 | 69 | 67 | 204 | 0 |
| E-distinguish | 300 | 296 | 4 | 0 | 0 | 0 |
| F-absolute | 348 | 0 | 348 | 0 | 0 | 0 |
| G-riskowner | 300 | 0 | 0 | 300 | 0 | 300 |
| H-control-plane | 150 | 0 | 150 | 0 | 0 | 0 |
| I-lapsed | 102 | 102 | 0 | 0 | 0 | 0 |
| J-novel | 102 | 102 | 0 | 0 | 0 | 0 |
| K-tie | 48 | 48 | 0 | 0 | 0 | 0 |
| P-pressure | 222 | 222 | 0 | 0 | 0 | 0 |
| L-consolidated | 198 | 198 | 0 | 0 | 0 | 67 |
| M-supersession | 180 | 97 | 83 | 0 | 83 | 0 |
| N-standing | 144 | 144 | 0 | 0 | 0 | 46 |
| Q-docket | 312 | 312 | 0 | 0 | 0 | 0 |
| R-reporter | 108 | 108 | 0 | 0 | 0 | 0 |
| S-acknowledgement | 132 | 0 | 0 | 132 | 0 | 132 |
| T-audit-register | 96 | 96 | 0 | 0 | 0 | 0 |
| U-renewal | 156 | 68 | 0 | 88 | 0 | 88 |
| V-likecase | 480 | 480 | 0 | 0 | 0 | 0 |
| W-crossjurisdiction | 240 | 128 | 112 | 0 | 0 | 0 |
| X-coldstart | 144 | 51 | 93 | 0 | 144 | 0 |
| Y-adversarial | 210 | 45 | 165 | 0 | 0 | 0 |
| Z-inexpressibility | 180 | 127 | 0 | 53 | 180 | 0 |

## The ledger — every change, and how it was treated

All five thousand, in the order they arrived. **Answer** is what the change got; **how** is the route that produced it; **controlling** names the record that decided it, where one did; **precedent** marks the changes whose decision entered the case base.

| # | Change | Engages | Answer | How | Controlling | Precedent |
| ---: | :--- | :--- | :--- | :--- | :--- | :-: |
| 1 | Track welfare inspection findings to a remediation due date | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2 | Configure retention periods per jurisdiction in the scheduler | VP-RR-007 | permitted | decided fresh | — |  |
| 3 | Add a per-tenant slider for the breach-notification deadline | VP-BN-001 VP-GV-003 ⛔ | denied | refused at the floor | — |  |
| 4 | Serialise inventory decrements with a row-level lock | VP-HA-003 | permitted | decided fresh | — |  |
| 5 | Register the new agent runner in the allowlist policy bundle | VP-PD-007 | denied | decided fresh | — |  |
| 6 | Enforce authorisation server-side on the discharge summary route | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 7 | Publish the contest outcome as granted and refused counts | VP-GV-007 | permitted | decided fresh | — |  |
| 8 | Match study patient identity on microchip and account number | VP-PO-009 | permitted | decided fresh | — |  |
| 9 | Populate DICOM species and breed tags from the patient record | VP-PO-009 | permitted | decided fresh | — |  |
| 10 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted | decided fresh | — |  |
| 11 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 12 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-010 | permitted with conditions | decided fresh | — | ● |
| 13 | Cut access-log retention to thirty days to save storage costs | VP-BN-002 | denied | decided fresh | — |  |
| 14 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-009 | permitted | decided fresh | — |  |
| 15 | Scope modality worklist queries to the requesting practice | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 16 | Configure retention periods per jurisdiction in the scheduler | VP-RR-006 | permitted | decided fresh | — |  |
| 17 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted | decided fresh | — |  |
| 18 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-009 | permitted with conditions | decided fresh | — | ● |
| 19 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-002 | permitted | decided fresh | — |  |
| 20 | Add a concurrency test for simultaneous discharge summary saves | — | permitted | docketed — nothing engaged | — |  |
| 21 | Link the breach notification runbook from the incident template | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 22 | Attach build provenance to the practice API release artefact | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 23 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-012 | permitted | decided fresh | — |  |
| 24 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | decided fresh | — | ● |
| 25 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 26 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-004 | permitted | decided fresh | — |  |
| 27 | Restrict the suspected-abuse report entry to authorised staff roles only | VP-PH-004 | permitted | decided fresh | — |  |
| 28 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted | decided fresh | — |  |
| 29 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 30 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 31 | Parameterise the new chart-search query | VP-AS-005 | permitted | decided fresh | — |  |
| 32 | Parameterise the new chart-search query | VP-AS-004 | permitted with conditions | decided fresh | — | ● |
| 33 | Flag food-animal status on the patient banner before dispensing | VP-VC-005 | permitted | decided fresh | — |  |
| 34 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 35 | Let staff issue standing scripts without opening the patient record | VP-CS-007 | denied | decided fresh | — | ● |
| 36 | Drop the practice filter from the referral search endpoint | VP-RB-004 | denied | decided fresh | — |  |
| 37 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-004 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 38 | Store payment references, not card numbers, on the retry queue | VP-PD-009 | permitted | decided fresh | — |  |
| 39 | Quarantine unmatched analyzer results for technician review | VP-PO-002 | permitted | decided fresh | — |  |
| 40 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-002 | permitted | decided fresh | — |  |
| 41 | Route diversion alerts to the medical director's queue within the hour | VP-CS-010 | permitted | decided fresh | — |  |
| 42 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-003 | permitted | decided fresh | — |  |
| 43 | Bind each service account to a single practice id | VP-RB-005 | permitted with conditions | decided fresh | — | ● |
| 44 | Require a second approver on admin role assignments | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 45 | Track welfare inspection findings to a remediation due date | VP-AW-005 | permitted | decided fresh | — |  |
| 46 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 47 | Add permutation tests across the role-permission matrix | VP-RB-008 | permitted | disposed by citation | — |  |
| 48 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 49 | Write the result row first and link the patient in a follow-up job | VP-PO-001 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 50 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 51 | Add permutation tests across the role-permission matrix | VP-RB-008 | permitted | decided fresh | — |  |
| 52 | Require an explicit share grant for cross-practice referrals | VP-RB-008 | permitted | decided fresh | — |  |
| 53 | Release medical records regardless of outstanding balance | VP-CC-006 | permitted | decided fresh | — |  |
| 54 | Check consent currency before the reminder engine sends | VP-PD-007 | permitted | decided fresh after a tie | none_tie |  |
| 55 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-009 | permitted | decided fresh | — |  |
| 56 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 57 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | permitted | decided fresh | — |  |
| 58 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 59 | Warn when a dose falls outside the labelled species range | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 60 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | decided fresh | — |  |
| 61 | Apply the state retention schedule to inactive owner records | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 62 | Match study patient identity on microchip and account number | VP-PO-004 | permitted | decided fresh | — |  |
| 63 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-003 | denied | decided fresh | — | ● |
| 64 | Assign a named reviewer to the vendored DICOM parser | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 65 | Remove the necessity note from the bulk compounding form | VP-VC-003 VP-CS-007 ⛔ | denied | refused at the floor | — |  |
| 66 | Allowlist microchip identifier formats at the API boundary | VP-AS-007 | permitted | docketed — not charged | — |  |
| 67 | Expose the contest path to the owner, not only to staff | VP-GV-005 | permitted with conditions | decided fresh | — | ● |
| 68 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 69 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 70 | Validate species and body weight before computing the dosage | VP-VC-004 | permitted | decided fresh | — |  |
| 71 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-004 | permitted | decided fresh | — |  |
| 72 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 73 | Load the chart straight from the patient id in the query string | VP-RB-001 VP-GV-006 ⛔ | denied | refused at the floor | — |  |
| 74 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 75 | Log the acknowledgement disposition on the referral timeline | VP-GV-003 | permitted | decided fresh | — |  |
| 76 | Apply the state retention schedule to inactive owner records | VP-PD-003 | permitted | decided fresh | — |  |
| 77 | Tokenise the card number before the invoice row is written | VP-PD-003 | permitted | decided fresh | — |  |
| 78 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | decided fresh | — |  |
| 79 | Require a phone call to cancel the wellness plan clients enrolled in online | VP-CC-001 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 80 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | decided fresh | — | ● |
| 81 | Scope modality worklist queries to the requesting practice | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 82 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 83 | Add regression tests for the note-render encoding path | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 84 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-004 | permitted | decided fresh | — |  |
| 85 | Encode clinical note text before rendering it in the portal | VP-AS-004 | permitted | decided fresh | — |  |
| 86 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | decided fresh | — |  |
| 87 | Log the full card number on payment retry to debug declines | VP-PD-004 | denied | decided fresh | — |  |
| 88 | Take record timestamps from the monotonic server clock | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 89 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted | decided fresh | — | ● |
| 90 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-008 | permitted | bound by precedent | REC-S0100 |  |
| 91 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-003 | permitted | decided fresh | — | ● |
| 92 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh | — |  |
| 93 | Record artefact digests in the release ledger on publish | VP-SC-007 | permitted | decided fresh | — |  |
| 94 | Gate merges on a clean provenance verification step | VP-SC-005 | permitted | disposed by citation | — |  |
| 95 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 96 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-008 | permitted | decided fresh | — |  |
| 97 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted | decided fresh | — |  |
| 98 | Write our own token signing routine to drop the crypto dependency | VP-AS-005 | denied | decided fresh | — |  |
| 99 | Enable the refill button on hydromorphone prescriptions | VP-CS-007 | denied | decided fresh | — |  |
| 100 | Add regression tests for the note-render encoding path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 101 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted | decided fresh | — |  |
| 102 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted | decided fresh | — |  |
| 103 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted | decided fresh | — |  |
| 104 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-004 | permitted | decided fresh | — |  |
| 105 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh | — |  |
| 106 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh | — |  |
| 107 | Keep the retention clock unchanged when a record is edited | VP-RR-005 | permitted | decided fresh | — |  |
| 108 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | permitted | decided fresh | — |  |
| 109 | Record the analgesia rationale when a plan is declined | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 110 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | decided fresh | — | ● |
| 111 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 112 | Parameterise the new chart-search query | VP-AS-006 | permitted | docketed — not charged | — |  |
| 113 | Run the secret scanner over the diff in pre-merge CI | VP-SC-007 | permitted | decided fresh | — |  |
| 114 | Sanitise filenames in the lab attachment upload handler | VP-AS-007 | permitted | docketed — not charged | — |  |
| 115 | Give consent withdrawal the same one-click path as granting it | VP-PD-005 | permitted | decided fresh | — |  |
| 116 | Queue reminder sends so a retry storm cannot amplify | VP-HA-004 | permitted | docketed — not charged | — |  |
| 117 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 118 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | decided fresh | — |  |
| 119 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — | ● |
| 120 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-AI-005 | denied | decided fresh | — |  |
| 121 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 122 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted | decided fresh | — |  |
| 123 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 124 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 125 | Run semantic analysis over the agent diff in CI | VP-AI-008 | permitted | decided fresh | — |  |
| 126 | Add the new charting library licence to the allowlist | VP-SC-004 | permitted | decided fresh | — |  |
| 127 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — |  |
| 128 | Derive tenant id from the session, never from a request header | VP-RB-004 | permitted | decided fresh | — |  |
| 129 | Store the amendment author alongside the superseded text | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 130 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-002 | denied | decided fresh | — |  |
| 131 | Block agent branches from touching the compliance test suite | VP-AI-005 | permitted | decided fresh | — |  |
| 132 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 133 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-009 | permitted with conditions | decided fresh | — | ● |
| 134 | Revalidate the active session after a privilege change | VP-RB-005 | permitted | decided fresh | — |  |
| 135 | Require an explicit share grant for cross-practice referrals | VP-RB-005 | permitted | decided fresh | — |  |
| 136 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 137 | Serialise inventory decrements with a row-level lock | VP-HA-005 | permitted | docketed — not charged | — |  |
| 138 | Add the suspected-abuse report option back to the chart action menu | VP-PH-004 | permitted | decided fresh | — |  |
| 139 | Block record purges that fall inside the two-year retention term | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 140 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 141 | Attach the full triage transcript to the patient's medical record | VP-PS-003 | permitted | decided fresh | — |  |
| 142 | Default the feed directive expiry to blank when it is unknown | VP-VC-002 ⛔ | denied | refused at the floor | — |  |
| 143 | Validate webhook destinations against the outbound allowlist | VP-AS-006 | permitted | docketed — not charged | — |  |
| 144 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 145 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | permitted | disposed by citation | — |  |
| 146 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-006 | permitted | docketed — not charged | — |  |
| 147 | Write a docket entry for every uncharged arrival | VP-GV-004 | permitted | decided fresh | — |  |
| 148 | Publish the contest outcome as granted and refused counts | VP-GV-004 | permitted | decided fresh | — |  |
| 149 | Build a searchable face gallery from the lobby camera feed | VP-GV-003 | denied | decided fresh | — |  |
| 150 | Configure retention periods per jurisdiction in the scheduler | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 151 | Restrict the suspected-abuse report entry to authorised staff roles only | VP-PH-003 | permitted | decided fresh | — |  |
| 152 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | decided fresh | — |  |
| 153 | Prompt for an off-label rationale in the medical record | VP-VC-007 | permitted | decided fresh | — |  |
| 154 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 155 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | disposed by citation | — |  |
| 156 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-008 | permitted | decided fresh | — |  |
| 157 | Hide the contest link when the decision is a denial | VP-GV-005 | denied | decided fresh | — |  |
| 158 | Block procedure sign-off by roles outside the delegated scope | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 159 | Assign a named reviewer to the vendored DICOM parser | VP-SC-007 | permitted | decided fresh | — |  |
| 160 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | permitted | decided fresh | — |  |
| 161 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 162 | Add the boarding service to the critical-service list in policy | VP-AS-003 | denied | decided fresh | — |  |
| 163 | Enable video-only exams for prescribing in every state | VP-VC-003 VP-CS-012 ⛔ | denied | refused at the floor | — |  |
| 164 | Lower the changed-line coverage threshold in the policy repo | VP-PO-010 | denied | decided fresh | — |  |
| 165 | Label agent-authored commits so review routing can see them | VP-AI-004 | permitted with conditions | decided fresh | — | ● |
| 166 | Redact owner email addresses from claims connector debug output | VP-PD-007 | permitted | decided fresh | — |  |
| 167 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 168 | Let the calculator accept twice the labelled equine maximum | VP-VC-004 | denied | decided fresh | — |  |
| 169 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 170 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-002 | permitted | decided fresh | — |  |
| 171 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-004 | permitted | decided fresh | — |  |
| 172 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 173 | Mute the bulk owner-data export alert to quiet the on-call pager | VP-BN-002 | denied | decided fresh | — | ● |
| 174 | Move the release outside the emergency-hours freeze window | VP-HA-002 | permitted | decided fresh | — |  |
| 175 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted | decided fresh | — | ● |
| 176 | Bump the HL7 parser to the patched upstream release | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 177 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | permitted | decided fresh | — |  |
| 178 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted | decided fresh | — |  |
| 179 | Add an accessibility regression gate to the portal release pipeline | VP-AX-002 | permitted | decided fresh | — |  |
| 180 | Record a manual screen-reader check for every new portal flow | VP-AX-002 | permitted | decided fresh | — |  |
| 181 | Record artefact digests in the release ledger on publish | VP-SC-001 | permitted | decided fresh | — | ● |
| 182 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-001 VP-PO-005 ⛔ | denied | refused at the floor | — |  |
| 183 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 184 | Mute the bulk owner-data export alert to quiet the on-call pager | VP-BN-001 VP-AI-008 ⛔ | denied | refused at the floor | — |  |
| 185 | Record artefact digests in the release ledger on publish | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 186 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 187 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 188 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 189 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted | decided fresh | — | ● |
| 190 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-009 | permitted | decided fresh | — | ● |
| 191 | Honour opt-out state at export time in the marketing job | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 192 | Make the audit table append-only at the database level | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 193 | Treat a portal login as e-signature consent for electronic records | VP-CC-002 | denied | decided fresh | — |  |
| 194 | Validate delegated task lists against the state practice act table | VP-AW-001 | permitted | decided fresh | — |  |
| 195 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 196 | Record artefact digests in the release ledger on publish | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 197 | Tokenise the card number before the invoice row is written | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 198 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — | ● |
| 199 | Change the escalation ladder so the third tier is final | VP-GV-005 | denied | decided fresh | — |  |
| 200 | Show the technician's credential status on the surgery board | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 201 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | disposed by citation | — |  |
| 202 | Add a campaign endpoint that exports the whole owner list | VP-PD-005 | denied | decided fresh | — |  |
| 203 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | decided fresh | — |  |
| 204 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-009 | permitted | decided fresh | — |  |
| 205 | Strip the standing declaration from the audit bundle header | VP-GV-001 ⛔ | denied | refused at the floor | — |  |
| 206 | Return the full exception text in the API error body | VP-AS-001 | denied | decided fresh | — |  |
| 207 | Strip the standing declaration from the audit bundle header | VP-GV-004 | denied | decided fresh | — |  |
| 208 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | decided fresh | — | ● |
| 209 | Capture the research protocol number on regulated-facility visits | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 210 | Replace the hand-rolled token hash with the vetted library | — | permitted | docketed — nothing engaged | — |  |
| 211 | Reject malformed segments without committing a partial patient write | VP-PO-009 | permitted | decided fresh | — |  |
| 212 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | decided fresh | — |  |
| 213 | Require the veterinary care plan on the regulated facility record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 214 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-006 | permitted | docketed — not charged | — |  |
| 215 | Run agent-generated code inside the sandboxed runner only | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 216 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 217 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-002 | permitted | decided fresh | — |  |
| 218 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-002 | permitted | decided fresh | — |  |
| 219 | Pin the radiography panel firmware version in the device inventory | VP-PO-010 | permitted | decided fresh | — |  |
| 220 | Drop analyzer messages that fail to parse and move on | VP-PO-008 | denied | decided fresh | — |  |
| 221 | Match study patient identity on microchip and account number | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 222 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-012 | permitted | decided fresh | — |  |
| 223 | Make the note autosave idempotent under client retry | VP-HA-005 | permitted | docketed — not charged | — |  |
| 224 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 225 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 226 | Sanitise filenames in the lab attachment upload handler | VP-AS-008 | permitted | docketed — not charged | — |  |
| 227 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-009 | permitted with conditions | decided fresh | — | ● |
| 228 | Quarantine unmatched analyzer results for technician review | VP-PO-010 | permitted | decided fresh | — |  |
| 229 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | permitted | decided fresh | — |  |
| 230 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted | decided fresh | — |  |
| 231 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 232 | Add the transport welfare checklist to the boarding intake form | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 233 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 234 | Block agent branches from touching the compliance test suite | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 235 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted | decided fresh | — | ● |
| 236 | Add permutation tests across the role-permission matrix | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 237 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 238 | Separate the audit register store from the precedent store | VP-GV-004 | permitted with conditions | decided fresh | — | ● |
| 239 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-008 | denied | decided fresh | — |  |
| 240 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-007 | denied | decided fresh | — |  |
| 241 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 242 | Check the version token on clinical note writes | VP-HA-002 | permitted | decided fresh | — |  |
| 243 | Deny clinical note writes to the receptionist role | VP-RB-004 | permitted | decided fresh | — |  |
| 244 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | permitted | decided fresh | — |  |
| 245 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-002 | permitted with conditions | decided fresh | — | ● |
| 246 | Enforce authorisation server-side on the discharge summary route | VP-AS-001 | permitted | disposed by citation | — |  |
| 247 | Validate the PDMP payload against the state schema before submit | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 248 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | decided fresh | — |  |
| 249 | Strip the standing declaration from the audit bundle header | VP-GV-001 VP-BN-003 ⛔ | denied | refused at the floor | — |  |
| 250 | Strip untrusted ticket text from the agent's instruction context | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 251 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 252 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh | — |  |
| 253 | Reject malformed segments without committing a partial patient write | VP-PO-007 | permitted | decided fresh | — |  |
| 254 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh | — |  |
| 255 | Version the accessibility statement alongside the portal release notes | VP-AX-002 | permitted | decided fresh | — |  |
| 256 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-002 | permitted | decided fresh | — |  |
| 257 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted with conditions | decided fresh | — | ● |
| 258 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 259 | Reject malformed segments without committing a partial patient write | VP-PO-005 | permitted | decided fresh | — |  |
| 260 | Run the secret scanner over the diff in pre-merge CI | VP-SC-001 | permitted | decided fresh | — |  |
| 261 | Point the resolver at the private registry before the public one | VP-SC-005 | permitted | decided fresh | — |  |
| 262 | Prove the backup restore before the vaccine index migration | VP-HA-004 | permitted | docketed — not charged | — |  |
| 263 | Route a human review request from the decision detail page | VP-GV-007 | permitted | decided fresh | — |  |
| 264 | Show which record controlled on the decision page | VP-GV-007 | permitted | decided fresh | — |  |
| 265 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 266 | Label agent-authored commits so review routing can see them | VP-AI-008 | permitted with conditions | decided fresh | — | ● |
| 267 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted | decided fresh | — | ● |
| 268 | Configure retention periods per jurisdiction in the scheduler | VP-RR-006 | permitted | decided fresh | — |  |
| 269 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-002 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 270 | Require acknowledgement before a critical value page clears | VP-PO-006 | permitted | decided fresh | — |  |
| 271 | Ship a down-migration for the visit-summary table change | VP-HA-002 | permitted | decided fresh | — |  |
| 272 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 273 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 274 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 275 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 276 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 277 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted | decided fresh | — |  |
| 278 | Verify the hash chain when an audit bundle is exported | VP-RR-003 | permitted | decided fresh | — |  |
| 279 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted | decided fresh | — |  |
| 280 | Record who exported an audit bundle and when | VP-RR-005 | permitted | decided fresh | — |  |
| 281 | Stagger analyzer polling to flatten the morning load peak | VP-HA-002 | permitted | decided fresh | — |  |
| 282 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 283 | Remove the segment length cap so long comment fields parse | VP-PO-001 VP-PS-002 ⛔ | denied | refused at the floor | — |  |
| 284 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted | decided fresh | — |  |
| 285 | Configure retention periods per jurisdiction in the scheduler | VP-RR-004 | permitted | decided fresh | — | ● |
| 286 | Enforce the tenant scope in the query layer, not the handler | VP-RB-006 | permitted | disposed by citation | — |  |
| 287 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 288 | Route every Schedule II reorder through the CSOS certificate signer | VP-DR-004 | permitted | decided fresh | — |  |
| 289 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 290 | Serialise inventory decrements with a row-level lock | VP-HA-004 | permitted | docketed — not charged | — |  |
| 291 | Move the release outside the emergency-hours freeze window | VP-HA-005 | permitted | docketed — not charged | — |  |
| 292 | Add permutation tests across the role-permission matrix | VP-RB-002 | permitted | decided fresh | — |  |
| 293 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 294 | Cover the new boarding endpoint with a role check test | VP-RB-004 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 295 | Verify commit signatures on the protected release branch | VP-SC-005 | permitted | decided fresh | — |  |
| 296 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted | decided fresh | — |  |
| 297 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted with conditions | decided fresh | — | ● |
| 298 | Require a named human reviewer on every agent-authored pull request | VP-AI-006 | permitted | decided fresh | — |  |
| 299 | Add contract tests for the pinned HL7 v2 profile | VP-PO-005 | permitted | decided fresh | — |  |
| 300 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-005 | permitted | decided fresh | — |  |
| 301 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-003 | denied | decided fresh | — |  |
| 302 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — |  |
| 303 | Add an admin path that updates the audit row to fix a typo | VP-RR-001 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 304 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-006 | permitted | decided fresh | — |  |
| 305 | Validate species and body weight before computing the dosage | VP-VC-006 | permitted | decided fresh | — |  |
| 306 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 307 | Configure a circuit breaker around the external lab client | VP-HA-005 | permitted | docketed — not charged | — |  |
| 308 | Send automated appointment texts to numbers with no recorded consent on file | VP-CC-001 VP-SC-002 ⛔ | denied | refused at the floor | — |  |
| 309 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 310 | Let clients reassign a microchip's registered owner from the self-service portal | VP-PH-004 | denied | decided fresh | — |  |
| 311 | Point the resolver at the private registry before the public one | VP-SC-007 | permitted | decided fresh | — |  |
| 312 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-002 | permitted | decided fresh | — |  |
| 313 | Show which record controlled on the decision page | VP-GV-004 | permitted | decided fresh | — |  |
| 314 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 315 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted | decided fresh | — |  |
| 316 | Keep the card number in the retry queue until settlement clears | VP-PD-003 | denied | decided fresh | — |  |
| 317 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — |  |
| 318 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 319 | Remove the deadline timer from the data export request queue | VP-PD-007 | denied | decided fresh | — |  |
| 320 | Assign a named reviewer to the vendored DICOM parser | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 321 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 322 | Add the boarding service to the critical-service list in policy | VP-PD-009 | denied | decided fresh | — |  |
| 323 | Waive the records-copy fee for a client's own written prescription request | VP-CC-006 | permitted | decided fresh | — |  |
| 324 | Require a currently licensed veterinarian's credential to sign a rabies certificate | VP-PH-003 | permitted | decided fresh | — |  |
| 325 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-003 | permitted | decided fresh | — |  |
| 326 | Hardcode the reference lab API key in the connector config | VP-SC-004 | denied | decided fresh | — |  |
| 327 | Withhold prescription finalisation from technician accounts | VP-RB-006 | permitted | decided fresh | — |  |
| 328 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 329 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 330 | Scope modality worklist queries to the requesting practice | VP-PO-009 | permitted | decided fresh | — |  |
| 331 | Show the six-month validity window on the refill request screen | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 332 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 333 | Publish the hotfix image straight from a laptop build | VP-SC-005 | denied | decided fresh | — |  |
| 334 | Scope modality worklist queries to the requesting practice | VP-PO-002 | permitted | decided fresh | — |  |
| 335 | Validate webhook destinations against the outbound allowlist | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 336 | Require an explicit owner choice before remains disposition can be saved | VP-PS-002 | permitted with conditions | decided fresh | — | ● |
| 337 | Require a second approver on admin role assignments | VP-RB-008 | permitted | decided fresh | — |  |
| 338 | Deny clinical note writes to the receptionist role | VP-RB-008 | permitted | decided fresh | — |  |
| 339 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 340 | Time-box break-glass access to four hours and log the grant | VP-RB-004 | permitted | decided fresh | — |  |
| 341 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 342 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 343 | Drop internal identifiers from the public error envelope | VP-AS-009 | permitted | docketed — not charged | — |  |
| 344 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | decided fresh | — |  |
| 345 | Allow payment-plan enrolment from an unverified under-eighteen account | VP-CC-005 | denied | decided fresh | — |  |
| 346 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-004 | permitted | decided fresh | — |  |
| 347 | Extend the log redaction filter to the new owner phone field | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 348 | Make the feed directive expiry date a mandatory field | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 349 | Redact owner email addresses from claims connector debug output | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 350 | Submit an amendment adding a welfare-inspection remediation window | VP-AI-003 | denied | decided fresh | — |  |
| 351 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-RR-004 | denied | decided fresh | — |  |
| 352 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 353 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted | decided fresh | — |  |
| 354 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-005 | permitted | decided fresh | — |  |
| 355 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-005 | permitted | decided fresh | — |  |
| 356 | Propose a sunset clause for the analytics pilot exception | VP-RR-002 | denied | decided fresh | — |  |
| 357 | Make Form 106 filing a manual checklist item instead of an automatic submission | VP-DR-001 VP-AI-003 ⛔ | denied | refused at the floor | — |  |
| 358 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 359 | Attach the standing declaration to every audit export | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 360 | Add a flag that skips the dispensing checks during demos | VP-CS-007 | denied | decided fresh | — |  |
| 361 | Allowlist microchip identifier formats at the API boundary | VP-AS-003 | permitted | decided fresh | — | ● |
| 362 | Cap analyzer retries at five with exponential backoff | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 363 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 364 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh | — |  |
| 365 | Cap analyzer retries at five with exponential backoff | VP-PO-007 | permitted | decided fresh | — |  |
| 366 | Block payment-plan enrolment from an account without verified adult status | VP-CC-003 | permitted | decided fresh | — |  |
| 367 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | decided fresh | — |  |
| 368 | Batch reportable-disease dispatches into a weekly job to cut API calls | VP-PH-003 | denied | decided fresh | — |  |
| 369 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-008 | permitted | decided fresh | — |  |
| 370 | Rank retrieval candidates using the audit register's findings | VP-GV-002 VP-GV-004 ⛔ | denied | refused at the floor | — |  |
| 371 | Enforce authorisation server-side on the discharge summary route | VP-AS-003 | permitted with conditions | decided fresh | — | ● |
| 372 | Bound the results reconciler retry loop | VP-HA-003 | permitted | decided fresh | — |  |
| 373 | Move the release outside the emergency-hours freeze window | VP-HA-003 | permitted | decided fresh | — |  |
| 374 | Bound the results reconciler retry loop | VP-HA-003 | permitted | decided fresh | — |  |
| 375 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-004 | permitted | decided fresh | — |  |
| 376 | Block payment-plan enrolment from an account without verified adult status | VP-CC-004 | permitted | decided fresh | — |  |
| 377 | Take record timestamps from the monotonic server clock | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 378 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 379 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 380 | Bump the HL7 parser to the patched upstream release | VP-SC-009 | permitted | decided fresh | — |  |
| 381 | Assign a named reviewer to the vendored DICOM parser | VP-SC-009 | permitted | decided fresh | — |  |
| 382 | Publish the contest counts in the audit export header | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 383 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 384 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted | decided fresh | — |  |
| 385 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 386 | Infer the prescriber from the last clinician to open the chart | VP-CS-011 | denied | decided fresh | — |  |
| 387 | Capture the research protocol number on regulated-facility visits | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 388 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 389 | Capture the research protocol number on regulated-facility visits | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 390 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 391 | Let the triage chatbot introduce itself as Dr. Assistant | VP-PS-001 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 392 | Warn when a dose falls outside the labelled species range | VP-VC-004 | permitted | decided fresh | — |  |
| 393 | Pin the radiography panel firmware version in the device inventory | VP-PO-003 | permitted | decided fresh | — |  |
| 394 | Validate webhook destinations against the outbound allowlist | VP-AS-009 | permitted | docketed — not charged | — |  |
| 395 | Check consent currency before the reminder engine sends | VP-PD-006 | permitted | decided fresh | — |  |
| 396 | Require a second approver on admin role assignments | VP-RB-007 | permitted | disposed by citation | — |  |
| 397 | Verify the hash chain when an audit bundle is exported | VP-RR-004 | permitted | decided fresh | — |  |
| 398 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 399 | Add a free-text field for the owner's social security number | VP-PD-004 | denied | decided fresh | — |  |
| 400 | Register the new agent runner in the allowlist policy bundle | VP-PO-008 | denied | decided fresh | — |  |
| 401 | Update the manifest and lockfile in the same commit | VP-SC-008 | permitted | decided fresh | — |  |
| 402 | Hardcode the reference lab API key in the connector config | VP-SC-003 | denied | decided fresh | — |  |
| 403 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-006 | permitted with conditions | decided fresh | — | ● |
| 404 | Honour opt-out state at export time in the marketing job | VP-PD-005 | permitted | decided fresh | — |  |
| 405 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted | decided fresh | — |  |
| 406 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 407 | Write the decision rationale at resolution time, not on export | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 408 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-005 | permitted | decided fresh after a tie | none_tie |  |
| 409 | Prove the backup restore before the vaccine index migration | VP-HA-005 | permitted | docketed — not charged | — |  |
| 410 | Validate webhook destinations against the outbound allowlist | VP-AS-001 | permitted | decided fresh | — |  |
| 411 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | decided fresh | — |  |
| 412 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | decided fresh | — |  |
| 413 | Keep the card number in the retry queue until settlement clears | VP-PD-002 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 414 | Wrap result-to-patient binding in a single database transaction | VP-PO-004 | permitted with conditions | decided fresh | — | ● |
| 415 | Require a verified adult guardian before a minor's client account can be created | VP-CC-005 | permitted | decided fresh | — |  |
| 416 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | decided fresh | — |  |
| 417 | Make the note autosave idempotent under client retry | — | permitted | docketed — nothing engaged | — |  |
| 418 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 419 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 420 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | decided fresh | — | ● |
| 421 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted with conditions | decided fresh | — | ● |
| 422 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted | decided fresh | — |  |
| 423 | Close automated denials without offering a human review request | VP-GV-001 VP-AX-001 ⛔ | denied | refused at the floor | — |  |
| 424 | Lower the changed-line coverage threshold in the policy repo | VP-RB-002 | denied | decided fresh | — |  |
| 425 | Enforce authorisation server-side on the discharge summary route | VP-AS-009 | permitted | docketed — not charged | — |  |
| 426 | Cover the new boarding endpoint with a role check test | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 427 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 428 | Remove the segment length cap so long comment fields parse | VP-PO-004 | denied | decided fresh | — |  |
| 429 | Add an immutability test for the dispensing log writer | VP-RR-002 | permitted | decided fresh | — |  |
| 430 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted | decided fresh | — |  |
| 431 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 432 | Track welfare inspection findings to a remediation due date | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 433 | Record the analgesia rationale when a plan is declined | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 434 | Add the transport welfare checklist to the boarding intake form | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 435 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 436 | Add regression tests for the note-render encoding path | VP-AS-005 | permitted | decided fresh | — | ● |
| 437 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-010 | denied | decided fresh | — |  |
| 438 | Bind each service account to a single practice id | VP-RB-002 | permitted | decided fresh | — |  |
| 439 | Verify focus order on the consent dialog before each release | VP-AX-001 | permitted with conditions | decided fresh | — | ● |
| 440 | Stagger analyzer polling to flatten the morning load peak | VP-HA-002 | permitted | decided fresh | — |  |
| 441 | Attach the standing declaration to every audit export | VP-RR-006 | permitted | decided fresh | — |  |
| 442 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-002 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 443 | Version chart amendments instead of editing rows in place | VP-RR-003 | permitted | decided fresh | — |  |
| 444 | Publish the contest counts in the audit export header | VP-RR-004 | permitted | decided fresh | — |  |
| 445 | Publish the contest counts in the audit export header | VP-RR-004 | permitted | decided fresh | — |  |
| 446 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 447 | Switch invoice delivery to email before capturing e-signature consent | VP-CC-001 VP-CS-010 ⛔ | denied | refused at the floor | — |  |
| 448 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh | — |  |
| 449 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted | decided fresh | — |  |
| 450 | Replace the species dose-range hard stop with an override button | VP-PS-004 ⛔ | denied | refused at the floor | — |  |
| 451 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 452 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted | decided fresh | — |  |
| 453 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-003 | permitted | decided fresh | — |  |
| 454 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-004 | permitted | decided fresh | — |  |
| 455 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-004 | permitted | decided fresh | — |  |
| 456 | Require a second approver on admin role assignments | VP-RB-008 | permitted | decided fresh | — |  |
| 457 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | disposed by citation | — |  |
| 458 | Add a keyboard path out of the consent modal's focus trap | VP-AX-002 | permitted | decided fresh | — | ● |
| 459 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 460 | Add the boarding service to the critical-service list in policy | VP-PO-002 | denied | decided fresh | — |  |
| 461 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 462 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 463 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-RR-002 | denied | decided fresh | — |  |
| 464 | Add a flag that skips the dispensing checks during demos | VP-CS-006 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 465 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-005 | denied | decided fresh | — | ● |
| 466 | Document the degraded path when the reference lab is down | VP-HA-003 | permitted | decided fresh | — |  |
| 467 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | disposed by citation | — |  |
| 468 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 469 | Link the breach notification runbook from the incident template | VP-PD-006 | permitted | decided fresh | — |  |
| 470 | Extend the log redaction filter to the new owner phone field | VP-PD-006 | permitted | decided fresh | — |  |
| 471 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 472 | Scope modality worklist queries to the requesting practice | VP-PO-006 | permitted | decided fresh | — |  |
| 473 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh | — |  |
| 474 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 475 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | decided fresh | — | ● |
| 476 | Renumber the point-of-care provisions after the device policy merge | VP-PD-009 | denied | decided fresh | — |  |
| 477 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 478 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 479 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-008 | permitted | decided fresh | — |  |
| 480 | Show the six-month validity window on the refill request screen | VP-CS-008 | permitted | decided fresh | — |  |
| 481 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | decided fresh | — |  |
| 482 | Record the prompt and context hash on the agent's pull request | VP-AI-005 | permitted | decided fresh after a tie | none_tie |  |
| 483 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-010 | permitted | decided fresh | — |  |
| 484 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted | decided fresh | — |  |
| 485 | Renumber the point-of-care provisions after the device policy merge | VP-CS-008 | denied | decided fresh | — |  |
| 486 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | decided fresh | — | ● |
| 487 | Parameterise the new chart-search query | VP-AS-009 | permitted | docketed — not charged | — |  |
| 488 | Enforce the tenant scope in the query layer, not the handler | VP-RB-002 | permitted | disposed by citation | — |  |
| 489 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted | disposed by citation | — |  |
| 490 | Record artefact digests in the release ledger on publish | VP-SC-008 | permitted | decided fresh | — |  |
| 491 | Add regression tests for the note-render encoding path | VP-AS-003 | permitted | decided fresh after a tie | none_tie |  |
| 492 | Link the breach notification runbook from the incident template | VP-PD-006 | permitted | decided fresh | — |  |
| 493 | Add the boarding service to the critical-service list in policy | VP-PS-002 | denied | decided fresh | — |  |
| 494 | Attach build provenance to the practice API release artefact | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 495 | Deny clinical note writes to the receptionist role | VP-RB-008 | permitted | decided fresh | — |  |
| 496 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-007 | permitted | decided fresh | — | ● |
| 497 | Configure a circuit breaker around the external lab client | VP-HA-006 | permitted | docketed — not charged | — |  |
| 498 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-005 | denied | decided fresh | — |  |
| 499 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 500 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 501 | Label agent-authored commits so review routing can see them | VP-AI-005 | permitted | decided fresh after a tie | none_tie |  |
| 502 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-002 | permitted | decided fresh | — |  |
| 503 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-002 | permitted | decided fresh | — |  |
| 504 | Tokenise the card number before the invoice row is written | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 505 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh | — |  |
| 506 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — |  |
| 507 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-005 | permitted | decided fresh | — |  |
| 508 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | decided fresh | — |  |
| 509 | Register the new agent runner in the allowlist policy bundle | VP-RR-003 | denied | decided fresh | — |  |
| 510 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | decided fresh | — |  |
| 511 | Remove the breach-notice clause from the standard vendor contract template | VP-BN-002 | denied | decided fresh | — |  |
| 512 | Return a correlation id instead of a stack trace on error | VP-AS-002 | permitted | disposed by citation | — |  |
| 513 | Disable the biennial inventory job during the systems migration | VP-DR-003 ⛔ | denied | refused at the floor | — |  |
| 514 | Reuse the stored consent flag without rechecking its date | VP-PD-003 | denied | decided fresh | — |  |
| 515 | Vendor the AGPL HL7 parser into the shipped practice API | VP-SC-005 | denied | decided fresh | — |  |
| 516 | Cap the records-copy fee at the state's statutory maximum | VP-CC-002 | permitted | decided fresh | — | ● |
| 517 | Add regression tests for the note-render encoding path | VP-AS-002 | permitted | decided fresh | — |  |
| 518 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 519 | Assign a named reviewer to the vendored DICOM parser | VP-SC-009 | permitted | decided fresh | — |  |
| 520 | Pin the build runner image and make each job ephemeral | VP-SC-009 | permitted | decided fresh | — |  |
| 521 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | decided fresh | — |  |
| 522 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | permitted with conditions | decided fresh | — | ● |
| 523 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh | — |  |
| 524 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | decided fresh after a tie | none_tie |  |
| 525 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | decided fresh | — |  |
| 526 | Take record timestamps from the monotonic server clock | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 527 | Apply the state retention schedule to inactive owner records | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 528 | Bound the data subject export job to the statutory window | VP-PD-009 | permitted | decided fresh | — |  |
| 529 | Remove the necessity note from the bulk compounding form | VP-VC-001 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 530 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-007 | permitted | decided fresh | — |  |
| 531 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | permitted | decided fresh | — |  |
| 532 | Parameterise the new chart-search query | VP-AS-003 | permitted | decided fresh | — |  |
| 533 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-002 | denied | decided fresh | — |  |
| 534 | Time-box break-glass access to four hours and log the grant | VP-RB-007 | permitted | decided fresh | — |  |
| 535 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — |  |
| 536 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 537 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-006 | permitted | docketed — not charged | — |  |
| 538 | Preserve the original entry when a chart amendment is filed | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 539 | Let staff log a remains custody transfer without scanning the tag | VP-PS-003 | denied | decided fresh | — |  |
| 540 | Block procedure sign-off by roles outside the delegated scope | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 541 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 542 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-PO-008 | denied | decided fresh | — |  |
| 543 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 544 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 545 | Sanitise filenames in the lab attachment upload handler | VP-AS-008 | permitted | docketed — not charged | — |  |
| 546 | Require a second approver on admin role assignments | VP-RB-005 | permitted | decided fresh | — |  |
| 547 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 548 | Add the transport welfare checklist to the boarding intake form | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 549 | Block agent branches from touching the compliance test suite | VP-AI-007 | permitted | decided fresh | — |  |
| 550 | Auto-merge agent pull requests once CI is green | VP-AI-004 | denied | decided fresh | — |  |
| 551 | Record artefact digests in the release ledger on publish | VP-SC-004 | permitted | decided fresh | — |  |
| 552 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — |  |
| 553 | Encode clinical note text before rendering it in the portal | VP-AS-001 | permitted | decided fresh | — |  |
| 554 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | decided fresh | — | ● |
| 555 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 556 | Encode clinical note text before rendering it in the portal | VP-AS-005 | permitted | decided fresh | — |  |
| 557 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 558 | Accept any microchip number the intake form receives without a format check | VP-PH-004 | denied | decided fresh | — |  |
| 559 | Configure retention periods per jurisdiction in the scheduler | VP-RR-003 | permitted | decided fresh | — |  |
| 560 | Record who exported an audit bundle and when | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 561 | Record a disposition for every referral acknowledgement | VP-GV-006 | permitted | decided fresh | — |  |
| 562 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — |  |
| 563 | Enforce authorisation server-side on the discharge summary route | VP-AS-003 | permitted | decided fresh | — |  |
| 564 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 565 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 566 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 567 | Check object ownership before returning a patient chart | VP-RB-002 | permitted | decided fresh | — | ● |
| 568 | Check consent currency before the reminder engine sends | VP-PD-003 | permitted | decided fresh | — |  |
| 569 | Gate merges on a clean provenance verification step | VP-SC-009 | permitted | disposed by citation | — |  |
| 570 | Block record purges that fall inside the two-year retention term | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 571 | Allowlist microchip identifier formats at the API boundary | VP-AS-006 | permitted | docketed — not charged | — |  |
| 572 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 573 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 574 | Record who exported an audit bundle and when | VP-RR-005 | permitted | decided fresh | — |  |
| 575 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 576 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-008 | denied | decided fresh | — |  |
| 577 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 578 | Stagger analyzer polling to flatten the morning load peak | VP-HA-002 | permitted | decided fresh | — |  |
| 579 | Make the audit table append-only at the database level | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 580 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 581 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-008 | permitted | decided fresh | — |  |
| 582 | Quarantine unmatched analyzer results for technician review | VP-PO-008 | permitted | decided fresh | — |  |
| 583 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh | — |  |
| 584 | Match the required supervision level to the task's risk tier | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 585 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 586 | Allowlist microchip identifier formats at the API boundary | VP-AS-006 | permitted | docketed — not charged | — |  |
| 587 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted | disposed by citation | — |  |
| 588 | Prompt for a pain management plan at surgical discharge | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 589 | Move threshold parameters into the legislated configuration | VP-GV-005 | permitted | decided fresh | — |  |
| 590 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-008 | permitted | decided fresh | — |  |
| 591 | Gate reportable-disease submissions behind a per-practice enable toggle | VP-PH-001 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 592 | Route vendor incident webhooks into the monitored incident queue | VP-BN-003 | permitted | decided fresh | — |  |
| 593 | Ship beef-herd orders without the residue assessment step | VP-VC-004 | denied | decided fresh | — |  |
| 594 | Rank retrieval candidates using the audit register's findings | VP-GV-006 | denied | decided fresh | — |  |
| 595 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-008 | permitted | decided fresh | — |  |
| 596 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-008 | permitted | decided fresh | — |  |
| 597 | Generate decision rationales from the outcome at export time | VP-RR-002 | denied | decided fresh | — |  |
| 598 | Block procedure sign-off by roles outside the delegated scope | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 599 | Replace the hand-rolled token hash with the vetted library | VP-AS-001 | permitted | decided fresh | — |  |
| 600 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | permitted | decided fresh | — |  |
| 601 | Replace the hand-rolled token hash with the vetted library | VP-AS-007 | permitted | docketed — not charged | — |  |
| 602 | Check the version token on clinical note writes | VP-HA-006 | permitted | docketed — not charged | — |  |
| 603 | Remove the extend-session option from the mobile check-in timeout | VP-AX-002 | denied | decided fresh | — | ● |
| 604 | Document the degraded path when the reference lab is down | VP-HA-006 | permitted | docketed — not charged | — |  |
| 605 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted with conditions | decided fresh | — | ● |
| 606 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 607 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-004 | permitted | decided fresh | — |  |
| 608 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-009 | permitted | docketed — not charged | — |  |
| 609 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 610 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-009 | permitted | docketed — not charged | — |  |
| 611 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 612 | Start the breach-notice timer at confirmed root cause instead of first detection | VP-BN-001 VP-GV-004 ⛔ | denied | refused at the floor | — |  |
| 613 | Populate DICOM species and breed tags from the patient record | VP-PO-010 | permitted | decided fresh after a tie | none_tie |  |
| 614 | Lower the changed-line coverage threshold in the policy repo | VP-RB-006 | denied | decided fresh | — |  |
| 615 | Point the resolver at the private registry before the public one | VP-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 616 | Tokenise the card number before the invoice row is written | VP-PD-008 | permitted | decided fresh | — |  |
| 617 | Cap analyzer retries at five with exponential backoff | VP-PO-010 | permitted | decided fresh | — |  |
| 618 | Scope modality worklist queries to the requesting practice | VP-PO-010 | permitted | decided fresh | — |  |
| 619 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | decided fresh | — | ● |
| 620 | Let a technician account sign the rabies certificate when the vet is busy | VP-PH-001 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 621 | Scope modality worklist queries to the requesting practice | VP-PO-003 | permitted | decided fresh | — |  |
| 622 | File a draft amendment codifying module-level coverage for generated code | VP-SC-004 | denied | decided fresh | — |  |
| 623 | Run agent-generated code inside the sandboxed runner only | VP-AI-003 | permitted | decided fresh | — |  |
| 624 | Reject malformed segments without committing a partial patient write | VP-PO-010 | permitted | decided fresh | — |  |
| 625 | Pin the build runner image and make each job ephemeral | VP-SC-004 | permitted | decided fresh | — |  |
| 626 | Pin the build runner image and make each job ephemeral | VP-SC-004 | permitted | decided fresh | — |  |
| 627 | Require acknowledgement before a critical value page clears | VP-PO-010 | permitted | decided fresh | — |  |
| 628 | Cover the new boarding endpoint with a role check test | VP-RB-003 | permitted | decided fresh | — |  |
| 629 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 630 | Block procedure sign-off by roles outside the delegated scope | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 631 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 632 | Remove the discontinued pilot's breach-clock override flag from the config schema | VP-BN-003 | permitted | decided fresh | — |  |
| 633 | Wire the bulk owner-data export anomaly detector to the on-call paging rotation | VP-BN-003 | permitted | decided fresh | — |  |
| 634 | Validate webhook destinations against the outbound allowlist | VP-AS-006 | permitted | docketed — not charged | — |  |
| 635 | Validate delegated task lists against the state practice act table | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 636 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 637 | Make the human review queue reachable from the portal | VP-GV-003 | permitted with conditions | decided fresh | — | ● |
| 638 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-001 | permitted | disposed by citation | — |  |
| 639 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 640 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted | decided fresh | — |  |
| 641 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 642 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 643 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 644 | Remove the discontinued pilot's breach-clock override flag from the config schema | VP-BN-002 | permitted | decided fresh | — |  |
| 645 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 646 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-001 | permitted | decided fresh | — |  |
| 647 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 648 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-002 | permitted | decided fresh | — |  |
| 649 | Drop the runbook link from the detection alert payload to shorten it | VP-BN-001 VP-CS-008 ⛔ | denied | refused at the floor | — |  |
| 650 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-003 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 651 | Restrict claim payload deserialisation to known types | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 652 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 653 | Match study patient identity on microchip and account number | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 654 | Show the technician's credential status on the surgery board | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 655 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 656 | Verify commit signatures on the protected release branch | VP-SC-005 | permitted | decided fresh | — |  |
| 657 | Update the manifest and lockfile in the same commit | VP-SC-005 | permitted | decided fresh | — |  |
| 658 | Allow extralabel orders for clients with no recorded exam | VP-VC-001 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 659 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 660 | Remove the two-person rule for EPCS grants from the policy repo | VP-CS-011 | denied | decided fresh | — |  |
| 661 | Make the audit table append-only at the database level | VP-RR-002 | permitted | decided fresh | — |  |
| 662 | Make the audit table append-only at the database level | VP-RR-002 | permitted | decided fresh | — |  |
| 663 | Hide the contest link when the decision is a denial | VP-GV-001 ⛔ | denied | refused at the floor | — |  |
| 664 | Capture the research protocol number on regulated-facility visits | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 665 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted | decided fresh | — |  |
| 666 | Require a second approver on admin role assignments | VP-RB-006 | permitted | decided fresh | — |  |
| 667 | Cap analyzer retries at five with exponential backoff | VP-PO-003 | permitted with conditions | decided fresh | — | ● |
| 668 | Let clients re-order from prescriptions written last year | VP-CS-002 ⛔ | denied | refused at the floor | — |  |
| 669 | Require the veterinary care plan on the regulated facility record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 670 | Surface the suspected-abuse report entry on the client-facing portal timeline | VP-PH-003 | denied | decided fresh | — |  |
| 671 | Allowlist microchip identifier formats at the API boundary | VP-AS-006 | permitted | docketed — not charged | — |  |
| 672 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 673 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted | decided fresh | — | ● |
| 674 | Drop the practice filter from the referral search endpoint | VP-RB-001 ⛔ | denied | refused at the floor | — |  |
| 675 | Extend the log redaction filter to the new owner phone field | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 676 | Close automated denials without offering a human review request | VP-GV-004 | denied | decided fresh | — |  |
| 677 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 678 | Add an admin path that updates the audit row to fix a typo | VP-RR-003 | denied | decided fresh | — |  |
| 679 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 680 | Require a named human reviewer on every agent-authored pull request | VP-AI-003 | permitted | decided fresh | — |  |
| 681 | Review agent-authored tests for tautological assertions | VP-AI-003 | permitted | decided fresh | — |  |
| 682 | Log the authenticated prescriber id on each dispensing event | VP-CS-012 | permitted | decided fresh | — |  |
| 683 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted | decided fresh | — |  |
| 684 | Check consent currency before the reminder engine sends | VP-PD-005 | permitted | decided fresh | — | ● |
| 685 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted | decided fresh | — |  |
| 686 | Log the authenticated prescriber id on each dispensing event | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 687 | Add the boarding service to the critical-service list in policy | VP-CS-012 | denied | decided fresh | — |  |
| 688 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 689 | Ship a down-migration for the visit-summary table change | VP-HA-006 | permitted | docketed — not charged | — |  |
| 690 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-004 | permitted | decided fresh | — |  |
| 691 | Allow staff to edit the recorded loss-discovery timestamp after filing | VP-DR-004 | denied | decided fresh | — |  |
| 692 | Reject malformed segments without committing a partial patient write | VP-PO-010 | permitted | decided fresh | — |  |
| 693 | Match study patient identity on microchip and account number | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 694 | Capture the research protocol number on regulated-facility visits | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 695 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-004 | permitted | docketed — not charged | — |  |
| 696 | Allowlist microchip identifier formats at the API boundary | VP-AS-002 | permitted | decided fresh | — | ● |
| 697 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 698 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-PS-002 ⛔ | denied | refused at the floor | — |  |
| 699 | Restrict the suspected-abuse report entry to authorised staff roles only | VP-PH-002 | permitted | decided fresh | — |  |
| 700 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-002 | denied | decided fresh | — |  |
| 701 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-002 | permitted with conditions | decided fresh | — | ● |
| 702 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh | — |  |
| 703 | Bind each service account to a single practice id | VP-RB-002 | permitted | decided fresh | — |  |
| 704 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 705 | Gate merges on a clean provenance verification step | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 706 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 707 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-006 | permitted | decided fresh | — |  |
| 708 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-006 | permitted | decided fresh | — |  |
| 709 | Restrict agent outbound calls to the allowlisted host set | VP-AI-004 | permitted | decided fresh | — |  |
| 710 | Require acknowledgement before a critical value page clears | VP-PO-004 | permitted | decided fresh | — |  |
| 711 | Let the dose calculator run on last year's recorded weight when today's is missing | VP-PS-001 VP-CS-007 ⛔ | denied | refused at the floor | — |  |
| 712 | Auto-merge agent pull requests once CI is green | VP-AI-008 | denied | decided fresh | — |  |
| 713 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | decided fresh | — |  |
| 714 | Update the manifest and lockfile in the same commit | VP-SC-007 | permitted | decided fresh | — |  |
| 715 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 716 | Require an explicit share grant for cross-practice referrals | VP-RB-008 | permitted with conditions | decided fresh | — | ● |
| 717 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 718 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-001 | permitted | decided fresh | — |  |
| 719 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-001 | denied | decided fresh | — | ● |
| 720 | Redact owner email addresses from claims connector debug output | VP-PD-004 | permitted | decided fresh | — | ● |
| 721 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | decided fresh | — | ● |
| 722 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 723 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-001 VP-CS-008 ⛔ | denied | refused at the floor | — |  |
| 724 | Gate merges on a clean provenance verification step | VP-SC-007 | permitted with conditions | decided fresh | — | ● |
| 725 | Derive tenant id from the session, never from a request header | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 726 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 727 | Serialise inventory decrements with a row-level lock | VP-HA-006 | permitted | docketed — not charged | — |  |
| 728 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted | decided fresh | — |  |
| 729 | Review agent-authored tests for tautological assertions | VP-AI-003 | permitted | decided fresh | — |  |
| 730 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted | decided fresh | — |  |
| 731 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-006 | permitted | decided fresh | — |  |
| 732 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted | decided fresh | — |  |
| 733 | Separate the audit register store from the precedent store | VP-GV-003 | permitted | decided fresh | — |  |
| 734 | Separate the audit register store from the precedent store | VP-GV-003 | permitted | decided fresh | — |  |
| 735 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 736 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — |  |
| 737 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 738 | Block agent branches from touching the compliance test suite | VP-AI-006 | permitted with conditions | decided fresh | — | ● |
| 739 | Encode clinical note text before rendering it in the portal | VP-AS-003 | permitted | decided fresh | — |  |
| 740 | Enforce authorisation server-side on the discharge summary route | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 741 | Gate merges on a clean provenance verification step | VP-SC-001 | permitted | disposed by citation | — |  |
| 742 | Attach the standing declaration to every audit export | VP-RR-005 | permitted | decided fresh | — |  |
| 743 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 744 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | decided fresh | — |  |
| 745 | Write the decision rationale at resolution time, not on export | VP-RR-003 | permitted | decided fresh | — |  |
| 746 | Calculate the extended withdrawal interval when the order is saved | VP-VC-007 | permitted | decided fresh | — |  |
| 747 | Point the resolver at the private registry before the public one | VP-SC-008 | permitted | disposed by citation | — |  |
| 748 | Pin the radiography panel firmware version in the device inventory | VP-PO-008 | permitted | decided fresh | — |  |
| 749 | Require acknowledgement before a critical value page clears | VP-PO-010 | permitted | decided fresh | — |  |
| 750 | Shorten the break-glass expiry constant in the rulebook | VP-CC-004 | denied | decided fresh | — |  |
| 751 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-011 | permitted | decided fresh | — |  |
| 752 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 753 | Swap the date library for a fork published by an unknown account | VP-SC-003 | denied | decided fresh | — |  |
| 754 | Drop internal identifiers from the public error envelope | VP-AS-006 | permitted | docketed — not charged | — |  |
| 755 | Add permutation tests across the role-permission matrix | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 756 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted | decided fresh | — |  |
| 757 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 758 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 759 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 760 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-001 VP-PS-002 ⛔ | denied | refused at the floor | — |  |
| 761 | Enforce authorisation server-side on the discharge summary route | VP-AS-004 | permitted | decided fresh | — | ● |
| 762 | Match study patient identity on microchip and account number | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 763 | Configure retention periods per jurisdiction in the scheduler | VP-RR-003 | permitted | decided fresh | — |  |
| 764 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted | decided fresh | — |  |
| 765 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted | decided fresh | — |  |
| 766 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-BN-002 | denied | decided fresh | — |  |
| 767 | Calculate the extended withdrawal interval when the order is saved | VP-VC-006 | permitted | decided fresh | — |  |
| 768 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — |  |
| 769 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 770 | Scope the new reporting role to read-only endpoints | VP-RB-003 | permitted | decided fresh | — |  |
| 771 | Withhold prescription finalisation from technician accounts | VP-RB-008 | permitted | disposed by citation | — |  |
| 772 | Attach the full triage transcript to the patient's medical record | VP-PS-002 | permitted | decided fresh | — |  |
| 773 | Preserve the original entry when a chart amendment is filed | VP-RR-004 | permitted | decided fresh | — |  |
| 774 | Track welfare inspection findings to a remediation due date | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 775 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-002 | permitted | decided fresh | — |  |
| 776 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-002 | permitted | decided fresh | — |  |
| 777 | Schedule marketing texts for six in the morning to beat inbox competition | VP-CC-006 | denied | decided fresh | — |  |
| 778 | Pre-check the wellness-plan auto-renewal box at checkout | VP-CC-002 | denied | decided fresh | — |  |
| 779 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted | decided fresh | — | ● |
| 780 | Add the new charting library licence to the allowlist | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 781 | Treat a portal login as e-signature consent for electronic records | VP-CC-002 | denied | decided fresh | — |  |
| 782 | Attribute the standing declaration to the enacting authority | VP-GV-004 | permitted | decided fresh | — |  |
| 783 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | decided fresh | — |  |
| 784 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted | decided fresh | — |  |
| 785 | Require a second approver on admin role assignments | VP-RB-004 | permitted | decided fresh | — |  |
| 786 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-004 | denied | decided fresh | — |  |
| 787 | Prompt for an off-label rationale in the medical record | VP-VC-002 ⛔ | permitted | decided fresh | — |  |
| 788 | Restrict claim payload deserialisation to known types | VP-AS-008 | permitted | docketed — not charged | — |  |
| 789 | Stagger analyzer polling to flatten the morning load peak | VP-HA-005 | permitted | docketed — not charged | — |  |
| 790 | Enable video-only exams for prescribing in every state | VP-VC-007 | denied | decided fresh | — |  |
| 791 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 792 | Configure retention periods per jurisdiction in the scheduler | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 793 | Make the note autosave idempotent under client retry | VP-HA-002 | permitted | decided fresh | — |  |
| 794 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 795 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 796 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-RB-003 | denied | decided fresh | — |  |
| 797 | Run the agent on the issue whose body carries its own instructions | VP-AI-002 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 798 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 799 | Drop internal identifiers from the public error envelope | VP-AS-001 | permitted | disposed by citation | — |  |
| 800 | Calculate the extended withdrawal interval when the order is saved | VP-VC-004 | permitted | decided fresh | — |  |
| 801 | Downgrade WCAG failures to warnings so the portal build stays green | VP-AX-001 | denied | decided fresh | — |  |
| 802 | Reset the retention date whenever a record is edited | VP-RR-001 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 803 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | decided fresh | — |  |
| 804 | Submit an amendment adding a welfare-inspection remediation window | VP-AI-008 | denied | decided fresh | — |  |
| 805 | Run agent-generated code inside the sandboxed runner only | VP-AI-004 | permitted | decided fresh | — |  |
| 806 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted | decided fresh | — |  |
| 807 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-002 | permitted | decided fresh | — |  |
| 808 | Quarantine unmatched analyzer results for technician review | VP-PO-002 | permitted | decided fresh | — |  |
| 809 | Require a second approver on admin role assignments | VP-RB-006 | permitted | decided fresh | — |  |
| 810 | Cover the new boarding endpoint with a role check test | VP-RB-006 | permitted | decided fresh | — |  |
| 811 | Require a second approver on admin role assignments | VP-RB-004 | permitted | disposed by citation | — |  |
| 812 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 813 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-001 ⛔ | denied | refused at the floor | — |  |
| 814 | Require a named response before a critical-value alert can be marked acknowledged | VP-PS-004 ⛔ | permitted | decided fresh | — |  |
| 815 | Expose the contest path to the owner, not only to staff | VP-GV-001 ⛔ | permitted | decided fresh | — |  |
| 816 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 817 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted | disposed by citation | — |  |
| 818 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 819 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — | ● |
| 820 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-010 | denied | decided fresh | — |  |
| 821 | Strip untrusted ticket text from the agent's instruction context | VP-AI-008 | permitted | decided fresh | — |  |
| 822 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | decided fresh | — |  |
| 823 | Freeze the significant-loss threshold at the DEA's own criteria rather than a local override | VP-DR-002 ⛔ | permitted | decided fresh | — |  |
| 824 | Log the full card number on payment retry to debug declines | VP-PD-001 VP-RB-007 ⛔ | denied | refused at the floor | — |  |
| 825 | Hardcode the reference lab API key in the connector config | VP-SC-002 | denied | decided fresh | — |  |
| 826 | Flag food-animal status on the patient banner before dispensing | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 827 | Run the secret scanner over the diff in pre-merge CI | VP-SC-009 | permitted with conditions | decided fresh | — | ● |
| 828 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | decided fresh | — |  |
| 829 | Sanitise filenames in the lab attachment upload handler | VP-AS-008 | permitted | docketed — not charged | — |  |
| 830 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted | decided fresh | — |  |
| 831 | Cut access-log retention to thirty days to save storage costs | VP-BN-003 | denied | decided fresh | — |  |
| 832 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-002 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 833 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | decided fresh | — |  |
| 834 | Verify commit signatures on the protected release branch | VP-SC-002 | permitted | decided fresh | — |  |
| 835 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-005 | denied | decided fresh | — |  |
| 836 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted | decided fresh | — |  |
| 837 | Reject malformed segments without committing a partial patient write | VP-PO-010 | permitted | decided fresh | — |  |
| 838 | Show the technician's credential status on the surgery board | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 839 | Bind each service account to a single practice id | VP-RB-002 | permitted | disposed by citation | — |  |
| 840 | Strip the standing declaration from the audit bundle header | VP-GV-005 | denied | decided fresh | — |  |
| 841 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-002 | permitted | decided fresh | — |  |
| 842 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-004 ⛔ | permitted | decided fresh | — |  |
| 843 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 844 | Schedule the biennial inventory job with an alert if it does not complete on time | VP-DR-004 | permitted | decided fresh | — |  |
| 845 | Show the six-month validity window on the refill request screen | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 846 | Check the version token on clinical note writes | VP-HA-002 | permitted | decided fresh | — |  |
| 847 | Drop internal identifiers from the public error envelope | VP-AS-002 | permitted | decided fresh | — |  |
| 848 | Tokenise the card number before the invoice row is written | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 849 | Have the agent refactor the controlled dispensing rules engine | VP-AI-001 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 850 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | decided fresh | — | ● |
| 851 | Extend order-form record retention to cover the full two-year floor | VP-DR-003 ⛔ | permitted | decided fresh | — |  |
| 852 | Version the regulator notice template in the policy repo | VP-BN-001 ⛔ | permitted | decided fresh | — |  |
| 853 | Publish the contest counts in the audit export header | VP-RR-007 | permitted | decided fresh | — |  |
| 854 | Keep the retention clock unchanged when a record is edited | VP-RR-007 | permitted | decided fresh | — |  |
| 855 | Attach a residue risk assessment to the food-animal order form | VP-VC-001 ⛔ | permitted | decided fresh | — |  |
| 856 | Store the amendment author alongside the superseded text | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 857 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-001 ⛔ | permitted | decided fresh | — |  |
| 858 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | permitted | decided fresh | — |  |
| 859 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-010 | permitted | decided fresh | — |  |
| 860 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-010 | permitted | decided fresh | — |  |
| 861 | Drop analyzer messages that fail to parse and move on | VP-PO-010 | denied | decided fresh | — |  |
| 862 | Route every Schedule II reorder through the CSOS certificate signer | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 863 | Show which record controlled on the decision page | VP-GV-007 | permitted with conditions | decided fresh | — | ● |
| 864 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | disposed by citation | — |  |
| 865 | Configure retention periods per jurisdiction in the scheduler | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 866 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 867 | Record the prompt and context hash on the agent's pull request | VP-AI-003 | permitted | decided fresh | — |  |
| 868 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-RB-002 | denied | decided fresh | — |  |
| 869 | Withhold prescription finalisation from technician accounts | VP-RB-005 | permitted | decided fresh | — | ● |
| 870 | Validate webhook destinations against the outbound allowlist | — | permitted | docketed — nothing engaged | — |  |
| 871 | Require a recorded in-person exam date before extralabel orders | VP-VC-006 | permitted | decided fresh | — |  |
| 872 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | permitted | decided fresh | — |  |
| 873 | Verify every imported package resolves in the registry before merge | VP-AI-005 | permitted | decided fresh | — |  |
| 874 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 875 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted | decided fresh | — |  |
| 876 | Check object ownership before returning a patient chart | VP-RB-007 | permitted | decided fresh | — |  |
| 877 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | permitted | disposed by citation | — |  |
| 878 | Load the chart straight from the patient id in the query string | VP-RB-007 | denied | decided fresh | — |  |
| 879 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 880 | Honour opt-out state at export time in the marketing job | VP-PD-005 | permitted | decided fresh | — |  |
| 881 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | decided fresh | — |  |
| 882 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 883 | Let staff log a remains custody transfer without scanning the tag | VP-PS-004 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 884 | Expose the contest path to the owner, not only to staff | VP-GV-006 | permitted | decided fresh | — |  |
| 885 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted | decided fresh | — |  |
| 886 | Bind each service account to a single practice id | VP-RB-001 ⛔ | permitted | decided fresh | — |  |
| 887 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 888 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted with conditions | decided fresh | — | ● |
| 889 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-002 | permitted | decided fresh | — |  |
| 890 | Scope the new reporting role to read-only endpoints | VP-RB-003 | permitted | decided fresh after a tie | none_tie |  |
| 891 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 892 | Reset the retention date whenever a record is edited | VP-RR-001 ⛔ | denied | refused at the floor | — |  |
| 893 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 894 | Remove the necessity note from the bulk compounding form | VP-VC-002 VP-RB-003 ⛔ | denied | refused at the floor | — |  |
| 895 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-003 | denied | decided fresh | — |  |
| 896 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted with conditions | decided fresh | — | ● |
| 897 | Quarantine unmatched analyzer results for technician review | VP-PO-001 ⛔ | permitted | decided fresh | — |  |
| 898 | Restrict claim payload deserialisation to known types | VP-AS-002 | permitted | disposed by citation | — |  |
| 899 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 900 | Make the audit table append-only at the database level | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 901 | Raise the p95 latency budget from ten to twenty-five percent | VP-RR-002 | denied | decided fresh | — |  |
| 902 | Disable the biennial inventory job during the systems migration | VP-DR-001 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 903 | Register the new agent runner in the allowlist policy bundle | VP-RR-004 | denied | decided fresh | — |  |
| 904 | Verify commit signatures on the protected release branch | VP-SC-008 | permitted | disposed by citation | — |  |
| 905 | Block agent branches from touching the compliance test suite | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 906 | Hide the contest link when the decision is a denial | VP-GV-007 | denied | decided fresh | — |  |
| 907 | Label agent-authored commits so review routing can see them | VP-AI-005 | permitted with conditions | decided fresh | — | ● |
| 908 | Require a tag scan at every remains custody transfer | VP-PS-003 | permitted | decided fresh | — |  |
| 909 | Remove the species dose-range override button that predates the current safety gate | VP-PS-003 | permitted | decided fresh | — |  |
| 910 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | decided fresh | — | ● |
| 911 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-009 | permitted | decided fresh | — |  |
| 912 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 913 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-001 VP-GV-005 ⛔ | denied | refused at the floor | — |  |
| 914 | Pin the radiography panel firmware version in the device inventory | VP-PO-002 | permitted | decided fresh | — |  |
| 915 | Commit parsed HL7 segments as they arrive instead of at the end | VP-PO-001 VP-GV-003 ⛔ | denied | refused at the floor | — |  |
| 916 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-003 | permitted | decided fresh | — | ● |
| 917 | Drop analyzer messages that fail to parse and move on | VP-PO-008 | denied | decided fresh | — |  |
| 918 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-004 | permitted | decided fresh | — |  |
| 919 | Route anomalous dispensing alerts to the medical director's paging channel | VP-DR-001 ⛔ | permitted | decided fresh | — |  |
| 920 | Assign the daily audit review to the practice manager role | VP-RR-001 ⛔ | permitted | decided fresh | — |  |
| 921 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 922 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted | decided fresh after a tie | none_tie |  |
| 923 | Remove the pre-charge renewal reminder to simplify the billing job | VP-CC-006 | denied | decided fresh | — |  |
| 924 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 925 | Revalidate the active session after a privilege change | VP-RB-008 | permitted | disposed by citation | — |  |
| 926 | Record a named owner and outcome on every breach-drill result | VP-BN-003 | permitted | decided fresh | — |  |
| 927 | Link the incident runbook from every breach-detection alert payload | VP-BN-003 | permitted | decided fresh | — |  |
| 928 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 929 | Block record purges that fall inside the two-year retention term | VP-CS-002 ⛔ | permitted | decided fresh | — |  |
| 930 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-004 | permitted | docketed — not charged | — |  |
| 931 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-001 VP-PO-009 ⛔ | denied | refused at the floor | — |  |
| 932 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-001 VP-PD-008 ⛔ | denied | refused at the floor | — |  |
| 933 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-SC-001 | denied | decided fresh | — |  |
| 934 | Require acknowledgement before a critical value page clears | VP-PO-005 | permitted | decided fresh | — |  |
| 935 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted | decided fresh | — |  |
| 936 | Cap analyzer retries at five with exponential backoff | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 937 | Publish the contest outcome as granted and refused counts | VP-GV-004 | permitted | decided fresh | — |  |
| 938 | Submit an amendment adding a welfare-inspection remediation window | VP-BN-003 | denied | decided fresh | — |  |
| 939 | Configure retention periods per jurisdiction in the scheduler | VP-RR-004 | permitted | bound by precedent | REC-VP-A-00285 |  |
| 940 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 941 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted with conditions | bound by precedent | REC-VP-G-00928 |  |
| 942 | Auto-fill the physical inventory count from the running ledger balance | VP-DR-002 VP-RB-004 ⛔ | denied | refused at the floor | — |  |
| 943 | Move the authorisation decision out of the portal frontend | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 944 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | decided fresh | — |  |
| 945 | Run agent-generated code inside the sandboxed runner only | VP-AI-008 | permitted | bound by precedent | REC-S0048 |  |
| 946 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 947 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-B-00554 | ● |
| 948 | Strip untrusted ticket text from the agent's instruction context | VP-AI-005 | permitted | decided fresh after a tie | none_tie |  |
| 949 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | denied | bound by precedent | REC-S0031 |  |
| 950 | Make the human review queue reachable from the portal | VP-GV-002 ⛔ | permitted | decided fresh | — |  |
| 951 | Add contract tests for the pinned HL7 v2 profile | VP-PO-008 | permitted | bound by precedent | REC-S0017 |  |
| 952 | Let the password alone sign an e-prescription when the token times out | VP-CS-001 VP-CS-009 ⛔ | denied | refused at the floor | — |  |
| 953 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 954 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-003 VP-PO-008 ⛔ | denied | refused at the floor | — |  |
| 955 | Check consent currency before the reminder engine sends | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-U-00848 | ● |
| 956 | Match study patient identity on microchip and account number | VP-PO-002 | permitted with conditions | decided fresh | — | ● |
| 957 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 958 | Attach build provenance to the practice API release artefact | VP-SC-007 | permitted | decided fresh | — |  |
| 959 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-007 | permitted | decided fresh | — |  |
| 960 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 961 | Encrypt the owner address column at rest in the portal store | VP-PD-008 | permitted | bound by precedent | REC-VP-N-00089 | ● |
| 962 | Restrict agent outbound calls to the allowlisted host set | VP-AI-004 | permitted | decided fresh | — |  |
| 963 | Record the prompt and context hash on the agent's pull request | VP-AI-004 | permitted | decided fresh | — |  |
| 964 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 |  |
| 965 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh | — |  |
| 966 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | denied | bound by precedent | REC-S0019 |  |
| 967 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | decided fresh | — | ● |
| 968 | Update the manifest and lockfile in the same commit | VP-SC-001 | denied | bound by precedent | REC-S0034 |  |
| 969 | Store payment references, not card numbers, on the retry queue | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 970 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-B-00910 |  |
| 971 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-006 | permitted | docketed — not charged | — |  |
| 972 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | bound by precedent | REC-S0036 | ● |
| 973 | Check object ownership before returning a patient chart | VP-RB-005 | permitted | disposed by citation | — |  |
| 974 | Validate webhook destinations against the outbound allowlist | VP-AS-006 | permitted | docketed — not charged | — |  |
| 975 | Add a breach-notice clause to the standard vendor contract template | VP-BN-002 | permitted with conditions | decided fresh | — | ● |
| 976 | Remove the extend-session option from the mobile check-in timeout | VP-AX-002 | denied | bound by precedent | REC-VP-B-00603 |  |
| 977 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-002 ⛔ | permitted | decided fresh | — |  |
| 978 | Auto-merge agent pull requests once CI is green | VP-AI-005 | denied | decided fresh | — |  |
| 979 | Make the audit table append-only at the database level | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 980 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | permitted | decided fresh | — |  |
| 981 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted | decided fresh | — |  |
| 982 | Call an external summarisation API from the agent's new helper | VP-AI-002 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 983 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 984 | Prove the backup restore before the vaccine index migration | VP-HA-005 | permitted | docketed — not charged | — |  |
| 985 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | bound by precedent | REC-VP-L-00475 |  |
| 986 | Wire the bulk owner-data export anomaly detector to the on-call paging rotation | VP-BN-003 | permitted | decided fresh | — |  |
| 987 | Require an explicit owner choice before remains disposition can be saved | VP-PS-003 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 988 | Check consent currency before the reminder engine sends | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 989 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 990 | Suppress the theft-and-loss alert when the missing count is under a configurable threshold | VP-DR-001 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 991 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | bound by precedent | REC-S0036 |  |
| 992 | Show the six-month validity window on the refill request screen | VP-CS-003 ⛔ | permitted | decided fresh | — |  |
| 993 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 994 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 995 | Update the manifest and lockfile in the same commit | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 996 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 997 | Attach build provenance to the practice API release artefact | VP-SC-009 | permitted with conditions | bound by precedent | REC-VP-G-00827 |  |
| 998 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 999 | Scope modality worklist queries to the requesting practice | VP-PO-008 | permitted | bound by precedent | REC-S0017 |  |
| 1000 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-009 | permitted | decided fresh | — |  |
| 1001 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-009 | permitted | decided fresh | — |  |
| 1002 | Cap analyzer retries at five with exponential backoff | VP-PO-008 | permitted | bound by precedent | REC-S0017 |  |
| 1003 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 1004 | Store payment references, not card numbers, on the retry queue | VP-PD-004 | permitted | bound by precedent | REC-VP-N-00720 |  |
| 1005 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | decided fresh | — |  |
| 1006 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | decided fresh | — |  |
| 1007 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — |  |
| 1008 | Make the human review queue reachable from the portal | VP-GV-006 | permitted with conditions | decided fresh | — | ● |
| 1009 | Wrap result-to-patient binding in a single database transaction | VP-PO-002 | permitted with conditions | bound by precedent | REC-VP-G-00956 |  |
| 1010 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1011 | Check object ownership before returning a patient chart | VP-RB-007 | denied | bound by precedent | REC-S0032 | ● |
| 1012 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1013 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-003 | permitted | decided fresh | — | ● |
| 1014 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted with conditions | bound by precedent | REC-VP-G-01008 |  |
| 1015 | Encrypt the owner address column at rest in the portal store | VP-PD-001 ⛔ | permitted | decided fresh | — |  |
| 1016 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted | bound by precedent | REC-VP-A-00458 |  |
| 1017 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted | decided fresh | — | ● |
| 1018 | Enforce the tenant scope in the query layer, not the handler | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 1019 | Block record purges that fall inside the two-year retention term | VP-CS-008 | permitted | decided fresh | — |  |
| 1020 | Route a human review request from the decision detail page | VP-GV-006 | permitted with conditions | bound by precedent | REC-VP-G-01008 |  |
| 1021 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 1022 | Withhold prescription finalisation from technician accounts | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 1023 | Require a recorded in-person exam date before extralabel orders | VP-VC-003 ⛔ | permitted | decided fresh | — |  |
| 1024 | Prompt for a pain management plan at surgical discharge | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 1025 | Run the secret scanner over the diff in pre-merge CI | VP-SC-008 | permitted | bound by precedent | REC-VP-N-00850 |  |
| 1026 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-001 | permitted | decided fresh | — |  |
| 1027 | Verify focus order on the consent dialog before each release | VP-AX-001 | permitted | decided fresh | — |  |
| 1028 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-003 | permitted | decided fresh | — |  |
| 1029 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-003 | permitted | decided fresh | — |  |
| 1030 | Warn when a dose falls outside the labelled species range | VP-VC-006 | denied | bound by precedent | REC-S0009 |  |
| 1031 | Remove the breach-notice clause from the standard vendor contract template | VP-BN-001 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 1032 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 |  |
| 1033 | Bump the HL7 parser to the patched upstream release | VP-SC-009 | permitted | decided fresh | — |  |
| 1034 | Flag food-animal status on the patient banner before dispensing | VP-VC-006 | denied | bound by precedent | REC-S0009 |  |
| 1035 | Check the version token on clinical note writes | VP-HA-001 | permitted | decided fresh | — |  |
| 1036 | Move the release outside the emergency-hours freeze window | — | permitted | docketed — nothing engaged | — |  |
| 1037 | Cap analyzer retries at five with exponential backoff | VP-PO-002 | permitted with conditions | bound by precedent | REC-VP-G-00956 | ● |
| 1038 | Trim the contest counts from the audit export header | VP-RR-001 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 1039 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-B-00420 | ● |
| 1040 | Require a phone call to cancel the wellness plan clients enrolled in online | VP-CC-002 | denied | decided fresh | — |  |
| 1041 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 |  |
| 1042 | Let Schedule II reorders go through the general purchasing API instead of CSOS | VP-DR-001 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 1043 | Record a disposition for every referral acknowledgement | VP-GV-003 | denied | bound by precedent | REC-S0060 |  |
| 1044 | Auto-close ketamine count mismatches under two millilitres | VP-CS-001 VP-CS-011 ⛔ | denied | refused at the floor | — |  |
| 1045 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted | bound by precedent | REC-VP-C-00961 |  |
| 1046 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 1047 | Give front desk staff the controlled dispensing permission | VP-RB-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 1048 | Encode clinical note text before rendering it in the portal | VP-AS-003 | permitted | decided fresh | — |  |
| 1049 | Parameterise the new chart-search query | VP-AS-003 | permitted | decided fresh | — |  |
| 1050 | Bound the data subject export job to the statutory window | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 1051 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 1052 | Remove the expiry from break-glass grants so support keeps access | VP-RB-005 | denied | decided fresh | — |  |
| 1053 | Hand the checkout redirect to the validated payment processor | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1054 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | decided fresh | — |  |
| 1055 | Remove the species dose-range override button that predates the current safety gate | VP-PS-002 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 1056 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1057 | Quarantine unmatched analyzer results for technician review | VP-PO-010 | denied | bound by precedent | REC-S0019 |  |
| 1058 | Drop analyzer messages that fail to parse and move on | VP-PO-005 | denied | decided fresh | — |  |
| 1059 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-002 | denied | bound by precedent | REC-S0068 | ● |
| 1060 | Restrict claim payload deserialisation to known types | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 1061 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | permitted | bound by precedent | REC-VP-L-00235 |  |
| 1062 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 1063 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 1064 | Record the prompt and context hash on the agent's pull request | VP-AI-002 ⛔ | permitted | decided fresh | — |  |
| 1065 | Change the escalation ladder so the third tier is final | VP-CS-007 | denied | decided fresh | — |  |
| 1066 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1067 | Withhold prescription finalisation from technician accounts | VP-RB-007 | denied | bound by precedent | REC-S0032 |  |
| 1068 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted | decided fresh | — |  |
| 1069 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-B-00910 | ● |
| 1070 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted | decided fresh | — |  |
| 1071 | Redact owner email addresses from claims connector debug output | VP-PD-007 | permitted | decided fresh | — |  |
| 1072 | Enforce authorisation server-side on the discharge summary route | — | permitted | docketed — nothing engaged | — |  |
| 1073 | Require acknowledgement before a critical value page clears | VP-PO-003 | permitted | bound by precedent | REC-VP-A-00091 |  |
| 1074 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted | decided fresh | — |  |
| 1075 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 1076 | Remove the suspected-abuse report option from the chart menu | VP-PH-002 | denied | decided fresh | — |  |
| 1077 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00189 | ● |
| 1078 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-005 ⛔ | permitted | decided fresh | — |  |
| 1079 | Sign CSOS orders with a shared practice login instead of the individual certificate | VP-DR-003 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 1080 | Validate species and body weight before computing the dosage | VP-VC-006 | denied | bound by precedent | REC-S0009 |  |
| 1081 | Skip the dispensing audit test the agent could not get passing | VP-AI-007 | denied | decided fresh | — |  |
| 1082 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | bound by precedent | REC-S0036 |  |
| 1083 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1084 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 1085 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted | decided fresh | — |  |
| 1086 | Route diversion alerts to the medical director's queue within the hour | VP-CS-007 | permitted | bound by precedent | REC-VP-A-00496 |  |
| 1087 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 1088 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | denied | bound by precedent | REC-S0005 | ● |
| 1089 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-007 | permitted | decided fresh | — |  |
| 1090 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 1091 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 | ● |
| 1092 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-001 ⛔ | permitted | decided fresh | — |  |
| 1093 | Attach build provenance to the practice API release artefact | VP-SC-006 | permitted | decided fresh | — |  |
| 1094 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted | decided fresh | — |  |
| 1095 | Replace the passive critical-value badge with a required acknowledgement dialog | VP-PS-001 ⛔ | permitted | decided fresh | — |  |
| 1096 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-011 | denied | bound by precedent | REC-VP-C-01088 |  |
| 1097 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 1098 | Restrict the suspected-abuse report entry to authorised staff roles only | VP-PH-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 1099 | Rebuild the consent signature pad as a mouse-only drag gesture | VP-AX-001 | denied | decided fresh | — |  |
| 1100 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 |  |
| 1101 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-001 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 1102 | Honour opt-out state at export time in the marketing job | VP-PD-003 | permitted | decided fresh | — |  |
| 1103 | Make the audit table append-only at the database level | VP-RR-004 | denied | bound by precedent | REC-S0056 | ● |
| 1104 | Check the version token on clinical note writes | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1105 | Match study patient identity on microchip and account number | VP-PO-006 | permitted | bound by precedent | REC-S0015 |  |
| 1106 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1107 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1108 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-003 | permitted | decided fresh | — |  |
| 1109 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | denied | bound by precedent | REC-S0016 |  |
| 1110 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 1111 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | denied | bound by precedent | REC-S0054 |  |
| 1112 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-002 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 1113 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 1114 | Raise the tramadol refill cap to twelve for chronic pain clients | VP-CS-001 VP-VC-005 ⛔ | denied | refused at the floor | — |  |
| 1115 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-011 | denied | bound by precedent | REC-S0005 |  |
| 1116 | Block agent branches from touching the compliance test suite | VP-AI-006 | permitted | decided fresh | — |  |
| 1117 | Record the prompt and context hash on the agent's pull request | VP-AI-006 | permitted | decided fresh | — |  |
| 1118 | Configure a circuit breaker around the external lab client | VP-HA-002 | permitted | decided fresh | — |  |
| 1119 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-004 | denied | bound by precedent | REC-S0070 |  |
| 1120 | Point the resolver at the private registry before the public one | VP-SC-002 | permitted | decided fresh | — |  |
| 1121 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-002 | permitted | decided fresh | — |  |
| 1122 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | bound by precedent | REC-VP-C-00972 | ● |
| 1123 | Hold medical-record releases until the client's balance is paid | VP-CC-004 | denied | decided fresh | — |  |
| 1124 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | denied | bound by precedent | REC-S0057 |  |
| 1125 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-AI-003 | denied | decided fresh | — |  |
| 1126 | Block procedure sign-off by roles outside the delegated scope | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1127 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | bound by precedent | REC-VP-N-00198 | ● |
| 1128 | Move the CVSS threshold from seven to eight in the dependency policy | VP-PH-003 | denied | decided fresh | — |  |
| 1129 | Submit an amendment adding a welfare-inspection remediation window | VP-SC-004 | denied | decided fresh | — |  |
| 1130 | Remove the expiry from break-glass grants so support keeps access | VP-RB-001 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 1131 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | bound by precedent | REC-S0023 |  |
| 1132 | Disable the biennial inventory job during the systems migration | VP-DR-003 ⛔ | denied | refused at the floor | — |  |
| 1133 | Add regression tests for the note-render encoding path | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1134 | Return a correlation id instead of a stack trace on error | VP-AS-002 | permitted | bound by precedent | REC-S0050 |  |
| 1135 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-002 | denied | decided fresh | — |  |
| 1136 | Pin the radiography panel firmware version in the device inventory | VP-PO-004 | permitted | decided fresh | — |  |
| 1137 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | permitted | decided fresh | — |  |
| 1138 | Show the technician's credential status on the surgery board | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 1139 | Hard-stop the dose calculator on a declared weight-unit mismatch | VP-PS-002 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 1140 | Drop internal identifiers from the public error envelope | VP-AS-005 | permitted | decided fresh | — |  |
| 1141 | Add an accessible name to the new custom toggle control | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 1142 | Show the six-month validity window on the refill request screen | VP-CS-007 | denied | bound by precedent | REC-S0126 |  |
| 1143 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted with conditions | decided fresh | — | ● |
| 1144 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-007 | permitted | bound by precedent | REC-VP-A-00496 |  |
| 1145 | Time-box break-glass access to four hours and log the grant | VP-RB-004 | permitted | decided fresh | — | ● |
| 1146 | Show which record controlled on the decision page | VP-GV-005 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1147 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-001 ⛔ | permitted | decided fresh | — |  |
| 1148 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | denied | bound by precedent | REC-S0022 |  |
| 1149 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 1150 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-004 | denied | decided fresh | — |  |
| 1151 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00181 |  |
| 1152 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-005 | permitted with conditions | decided fresh | — | ● |
| 1153 | Allowlist microchip identifier formats at the API boundary | VP-AS-005 | permitted | bound by precedent | REC-VP-L-00436 |  |
| 1154 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 1155 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-B-00420 |  |
| 1156 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 1157 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — |  |
| 1158 | Scope the new reporting role to read-only endpoints | VP-RB-007 | permitted | decided fresh | — |  |
| 1159 | Restrict claim payload deserialisation to known types | VP-AS-001 | permitted with conditions | decided fresh | — | ● |
| 1160 | Tokenise the card number before the invoice row is written | VP-PD-008 | permitted | bound by precedent | REC-VP-N-00089 |  |
| 1161 | Link the breach notification runbook from the incident template | VP-PD-009 | permitted | decided fresh | — |  |
| 1162 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 1163 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-002 VP-VC-006 ⛔ | denied | refused at the floor | — |  |
| 1164 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 1165 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-001 ⛔ | permitted | decided fresh | — |  |
| 1166 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | decided fresh | — |  |
| 1167 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — |  |
| 1168 | Shorten the vendor breach-notice SLA from five business days to two | VP-BN-002 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1169 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-002 | permitted | disposed by citation | — |  |
| 1170 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01013 | ● |
| 1171 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 1172 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | bound by precedent | REC-S0041 |  |
| 1173 | Bound the data subject export job to the statutory window | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 1174 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-006 ⛔ | permitted | decided fresh | — |  |
| 1175 | Store the amendment author alongside the superseded text | VP-RR-002 | permitted with conditions | bound by precedent | REC-VP-U-01087 |  |
| 1176 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | disposed by citation | — |  |
| 1177 | Require a second approver on admin role assignments | VP-RB-003 | permitted | bound by precedent | REC-VP-C-01127 |  |
| 1178 | Block payment-plan enrolment from an account without verified adult status | VP-CC-002 | permitted | decided fresh | — |  |
| 1179 | Waive the records-copy fee for a client's own written prescription request | VP-CC-002 | permitted | decided fresh | — |  |
| 1180 | Trim the contest counts from the audit export header | VP-RR-002 | denied | decided fresh | — |  |
| 1181 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 1182 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-B-00910 | ● |
| 1183 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 1184 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted with conditions | bound by precedent | REC-VP-G-01143 |  |
| 1185 | Validate species and body weight before computing the dosage | VP-VC-004 | permitted | decided fresh | — |  |
| 1186 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00819 | ● |
| 1187 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted | decided fresh | — |  |
| 1188 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 |  |
| 1189 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 1190 | Add an immutability test for the dispensing log writer | VP-RR-006 | denied | bound by precedent | REC-S0058 |  |
| 1191 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 1192 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-007 | denied | bound by precedent | REC-S0010 |  |
| 1193 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1194 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 |  |
| 1195 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 1196 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 1197 | Pair the required-field error with visible text, not colour alone | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 | ● |
| 1198 | Strip untrusted ticket text from the agent's instruction context | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 1199 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 1200 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 1201 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | bound by precedent | REC-VP-U-01097 | ● |
| 1202 | Restrict agent outbound calls to the allowlisted host set | VP-AI-008 | permitted | decided fresh | — |  |
| 1203 | Run semantic analysis over the agent diff in CI | VP-AI-008 | permitted | decided fresh | — |  |
| 1204 | Move threshold parameters into the legislated configuration | VP-GV-003 | permitted | decided fresh | — |  |
| 1205 | Verify every imported package resolves in the registry before merge | VP-AI-005 | permitted | decided fresh | — |  |
| 1206 | Verify every imported package resolves in the registry before merge | VP-AI-003 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1207 | Retry the blood gas analyzer until it answers | VP-PO-007 | denied | decided fresh | — |  |
| 1208 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | denied | bound by precedent | REC-S0051 |  |
| 1209 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 1210 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 | ● |
| 1211 | Cap analyzer retries at five with exponential backoff | VP-PO-003 | permitted | decided fresh | — |  |
| 1212 | Check object ownership before returning a patient chart | VP-RB-003 | permitted | bound by precedent | REC-VP-N-00198 |  |
| 1213 | Bump the HL7 parser to the patched upstream release | VP-SC-009 | permitted | decided fresh | — |  |
| 1214 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted with conditions | bound by precedent | REC-VP-S-01149 | ● |
| 1215 | Route vendor incident webhooks into the monitored incident queue | VP-BN-003 | permitted with conditions | decided fresh | — | ● |
| 1216 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | bound by precedent | REC-VP-N-00850 |  |
| 1217 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-007 | permitted | decided fresh | — |  |
| 1218 | Cap analyzer retries at five with exponential backoff | VP-PO-003 | permitted | bound by precedent | REC-VP-A-00091 |  |
| 1219 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 1220 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted | bound by precedent | REC-S0006 | ● |
| 1221 | Store the amendment author alongside the superseded text | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 1222 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted with conditions | bound by precedent | REC-S0004 | ● |
| 1223 | Scope modality worklist queries to the requesting practice | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 1224 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-003 | permitted | decided fresh | — |  |
| 1225 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-003 | permitted | decided fresh | — |  |
| 1226 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | decided fresh | — |  |
| 1227 | Attach build provenance to the practice API release artefact | VP-SC-008 | permitted | decided fresh | — |  |
| 1228 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-008 | permitted | bound by precedent | REC-VP-N-00850 |  |
| 1229 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 1230 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00189 |  |
| 1231 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1232 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 |  |
| 1233 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-004 | permitted | decided fresh | — | ● |
| 1234 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-002 | permitted | bound by precedent | REC-S0050 |  |
| 1235 | Match analyzer results on patient name alone | VP-PO-006 | denied | decided fresh | — |  |
| 1236 | Add permutation tests across the role-permission matrix | VP-RB-004 | permitted | bound by precedent | REC-S0029 |  |
| 1237 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 1238 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | bound by precedent | REC-VP-L-00361 |  |
| 1239 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-005 | permitted | decided fresh | — |  |
| 1240 | Let one admin grant EPCS signing rights from the user screen | VP-CS-004 VP-SC-008 ⛔ | denied | refused at the floor | — |  |
| 1241 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-C-01069 |  |
| 1242 | Revalidate the active session after a privilege change | VP-RB-007 | permitted with conditions | decided fresh | — | ● |
| 1243 | Route a human review request from the decision detail page | VP-GV-005 | permitted | decided fresh | — |  |
| 1244 | Route a human review request from the decision detail page | VP-GV-005 | permitted | decided fresh | — |  |
| 1245 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | bound by precedent | REC-VP-B-00110 |  |
| 1246 | Have the agent refactor the controlled dispensing rules engine | VP-AI-004 | denied | decided fresh | — |  |
| 1247 | Record the prompt and context hash on the agent's pull request | VP-AI-003 | permitted | decided fresh | — |  |
| 1248 | Run agent-generated code inside the sandboxed runner only | VP-AI-003 | permitted | decided fresh | — |  |
| 1249 | Run semantic analysis over the agent diff in CI | VP-AI-003 | permitted | decided fresh after a tie | none_tie |  |
| 1250 | Have the agent refactor the controlled dispensing rules engine | VP-AI-007 | denied | decided fresh | — |  |
| 1251 | Store payment references, not card numbers, on the retry queue | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1252 | Add the statutory content checklist to the owner breach-notice template | VP-BN-002 | permitted | decided fresh | — |  |
| 1253 | Bind each service account to a single practice id | VP-RB-007 | permitted | bound by precedent | REC-VP-A-00080 |  |
| 1254 | Record artefact digests in the release ledger on publish | VP-SC-009 | permitted | decided fresh | — |  |
| 1255 | Link the breach notification runbook from the incident template | VP-PD-003 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 1256 | Make the withdrawal interval optional on food-animal orders | VP-VC-005 | denied | decided fresh | — | ● |
| 1257 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-010 | permitted with conditions | bound by precedent | REC-VP-C-01222 |  |
| 1258 | Record who exported an audit bundle and when | VP-RR-004 | permitted | decided fresh | — |  |
| 1259 | Add a keyboard path out of the consent modal's focus trap | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 | ● |
| 1260 | Link the breach notification runbook from the incident template | VP-PD-009 | permitted | decided fresh | — | ● |
| 1261 | Add permutation tests across the role-permission matrix | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 | ● |
| 1262 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted | decided fresh | — |  |
| 1263 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | bound by precedent | REC-VP-C-01170 | ● |
| 1264 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 1265 | Sanitise filenames in the lab attachment upload handler | VP-AS-003 | permitted | bound by precedent | REC-VP-L-00361 |  |
| 1266 | Gate merges on a clean provenance verification step | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 1267 | Write a docket entry for every uncharged arrival | VP-GV-004 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 1268 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 1269 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-005 | permitted | bound by precedent | REC-S0045 |  |
| 1270 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-004 | permitted | decided fresh | — |  |
| 1271 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-004 | permitted | decided fresh | — |  |
| 1272 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-003 | permitted | decided fresh | — | ● |
| 1273 | Split the agent-refactored invoicing function to cut its branching | VP-AI-004 | denied | bound by precedent | REC-S0044 |  |
| 1274 | Point vendor incident notifications at a shared inbox nobody monitors | VP-BN-002 | denied | decided fresh | — |  |
| 1275 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 1276 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted with conditions | bound by precedent | REC-VP-U-01097 |  |
| 1277 | Serialise inventory decrements with a row-level lock | VP-HA-001 | permitted | decided fresh | — |  |
| 1278 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-004 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 1279 | Cap the records-copy fee at the state's statutory maximum | VP-CC-004 | permitted with conditions | decided fresh | — | ● |
| 1280 | Serialise inventory decrements with a row-level lock | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1281 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-001 | denied | bound by precedent | REC-S0034 | ● |
| 1282 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted | decided fresh | — |  |
| 1283 | Wrap result-to-patient binding in a single database transaction | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 1284 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-001 | denied | bound by precedent | REC-VP-B-00719 | ● |
| 1285 | Default the feed directive expiry to blank when it is unknown | VP-VC-002 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 1286 | Publish the contest counts in the audit export header | VP-RR-005 | permitted with conditions | bound by precedent | REC-VP-U-01221 |  |
| 1287 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — | ● |
| 1288 | Make the consent signature pad completable by keyboard alone | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01197 |  |
| 1289 | Publish the contest outcome as granted and refused counts | VP-GV-004 | permitted | decided fresh | — |  |
| 1290 | Keep the contest link visible on every automated decision notice | VP-GV-004 | permitted | decided fresh | — |  |
| 1291 | Drop analyzer messages that fail to parse and move on | VP-PO-003 | denied | decided fresh | — |  |
| 1292 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted | decided fresh | — | ● |
| 1293 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-005 | permitted | decided fresh | — |  |
| 1294 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-005 | permitted | decided fresh | — |  |
| 1295 | Attach build provenance to the practice API release artefact | VP-SC-009 | permitted | bound by precedent | REC-VP-L-01287 |  |
| 1296 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh | — |  |
| 1297 | Block record purges that fall inside the two-year retention term | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 1298 | Version the regulator notice template in the policy repo | VP-BN-003 | denied | bound by precedent | REC-S0066 |  |
| 1299 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | decided fresh after a tie | none_tie |  |
| 1300 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-004 | permitted with conditions | bound by precedent | REC-VP-G-01279 |  |
| 1301 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 1302 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 1303 | Split the agent-refactored invoicing function to cut its branching | VP-AI-004 | denied | bound by precedent | REC-S0044 |  |
| 1304 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 1305 | Route a human review request from the decision detail page | VP-GV-007 | permitted | bound by precedent | REC-S0064 | ● |
| 1306 | Add permutation tests across the role-permission matrix | VP-RB-002 | permitted | disposed by citation | — |  |
| 1307 | Make the withdrawal interval optional on food-animal orders | VP-VC-005 | denied | bound by precedent | REC-VP-B-01256 |  |
| 1308 | Switch invoice delivery to email before capturing e-signature consent | VP-CC-003 | denied | decided fresh | — |  |
| 1309 | Assign the daily audit review to the practice manager role | VP-RR-004 | permitted | bound by precedent | REC-VP-A-00285 |  |
| 1310 | Drop internal identifiers from the public error envelope | VP-AS-002 | permitted | decided fresh | — |  |
| 1311 | Restrict claim payload deserialisation to known types | VP-AS-002 | permitted | decided fresh | — |  |
| 1312 | Bound the results reconciler retry loop | VP-HA-003 | permitted | decided fresh | — |  |
| 1313 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | bound by precedent | REC-S0015 |  |
| 1314 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 1315 | Record the prompt and context hash on the agent's pull request | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 1316 | Require a named human reviewer on every agent-authored pull request | VP-AI-003 | permitted with conditions | decided fresh | — | ● |
| 1317 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | bound by precedent | REC-VP-C-01186 | ● |
| 1318 | Replace the hand-rolled token hash with the vetted library | VP-AS-003 | permitted | decided fresh | — |  |
| 1319 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-007 | permitted with conditions | bound by precedent | REC-VP-G-01143 |  |
| 1320 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted | decided fresh | — |  |
| 1321 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 |  |
| 1322 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-003 | permitted | decided fresh | — | ● |
| 1323 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | bound by precedent | REC-VP-L-00475 |  |
| 1324 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | disposed by citation | — |  |
| 1325 | Record artefact digests in the release ledger on publish | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 1326 | Make the withdrawal interval optional on food-animal orders | VP-VC-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 1327 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1328 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-008 | denied | bound by precedent | REC-S0002 | ● |
| 1329 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-006 | permitted | decided fresh | — |  |
| 1330 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-006 | permitted | decided fresh | — |  |
| 1331 | Bind each service account to a single practice id | VP-RB-007 | denied | bound by precedent | REC-VP-C-01011 |  |
| 1332 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 1333 | Require a second approver on admin role assignments | VP-RB-003 | permitted | bound by precedent | REC-VP-C-01127 |  |
| 1334 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-009 | permitted | decided fresh | — |  |
| 1335 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-009 | permitted | decided fresh | — |  |
| 1336 | Parameterise the new chart-search query | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 1337 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted | bound by precedent | REC-VP-A-01292 |  |
| 1338 | Enforce authorisation server-side on the discharge summary route | — | permitted | docketed — nothing engaged | — |  |
| 1339 | Honour opt-out state at export time in the marketing job | VP-PD-003 | permitted with conditions | bound by precedent | REC-VP-G-01302 |  |
| 1340 | Raise the tramadol refill cap to twelve for chronic pain clients | VP-CS-007 | denied | decided fresh | — |  |
| 1341 | Attach the standing declaration to every audit export | VP-RR-003 | permitted | bound by precedent | REC-VP-A-00175 | ● |
| 1342 | Encode clinical note text before rendering it in the portal | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1343 | Add an accessibility regression gate to the portal release pipeline | VP-AX-001 | permitted | bound by precedent | REC-S0078 | ● |
| 1344 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 1345 | Check consent currency before the reminder engine sends | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1346 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | decided fresh | — |  |
| 1347 | Match study patient identity on microchip and account number | VP-PO-002 | denied | bound by precedent | REC-S0011 |  |
| 1348 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-012 | permitted | decided fresh | — |  |
| 1349 | Enforce the tenant scope in the query layer, not the handler | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 |  |
| 1350 | Make the audit table append-only at the database level | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 1351 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | bound by precedent | REC-VP-B-00110 |  |
| 1352 | Make the human review queue reachable from the portal | VP-GV-004 | permitted | decided fresh | — |  |
| 1353 | Replace the hand-rolled token hash with the vetted library | VP-AS-003 | denied | bound by precedent | REC-S0051 |  |
| 1354 | Match analyzer results on patient name alone | VP-PO-001 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 1355 | Verify focus order on the consent dialog before each release | VP-AX-002 | permitted | bound by precedent | REC-VP-A-00458 |  |
| 1356 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | disposed by citation | — |  |
| 1357 | Route a human review request from the decision detail page | VP-GV-003 | denied | bound by precedent | REC-S0060 |  |
| 1358 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 1359 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted | decided fresh | — |  |
| 1360 | Auto-close ketamine count mismatches under two millilitres | VP-CS-008 | denied | decided fresh | — |  |
| 1361 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted | bound by precedent | REC-VP-C-01077 | ● |
| 1362 | Publish the contest counts in the audit export header | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 1363 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | bound by precedent | REC-S0078 |  |
| 1364 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 1365 | Block record purges that fall inside the two-year retention term | VP-CS-008 | denied | bound by precedent | REC-S0002 |  |
| 1366 | Calculate the extended withdrawal interval when the order is saved | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 1367 | Withhold prescription finalisation from technician accounts | VP-RB-008 | permitted | bound by precedent | REC-VP-L-00119 | ● |
| 1368 | Call an external summarisation API from the agent's new helper | VP-AI-001 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 1369 | Drop internal identifiers from the public error envelope | VP-AS-002 | permitted | bound by precedent | REC-S0050 |  |
| 1370 | Require a saved consent record before the euthanasia workflow can proceed | VP-PS-003 | permitted | decided fresh | — |  |
| 1371 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | bound by precedent | REC-VP-L-00436 |  |
| 1372 | Ship the new custom toggle control without an accessible name attribute | VP-AX-002 | denied | decided fresh | — |  |
| 1373 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | bound by precedent | REC-VP-A-01292 |  |
| 1374 | Add the suspected-abuse report option back to the chart action menu | VP-PH-004 | permitted | decided fresh | — |  |
| 1375 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-004 | permitted | decided fresh | — |  |
| 1376 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | bound by precedent | REC-VP-C-01361 |  |
| 1377 | Render the owner's intake note as raw HTML to keep their formatting | VP-AS-001 | denied | decided fresh | — |  |
| 1378 | Populate DICOM species and breed tags from the patient record | VP-PO-002 | permitted | decided fresh | — |  |
| 1379 | Enable the refill button on hydromorphone prescriptions | VP-CS-001 ⛔ | denied | refused at the floor | — |  |
| 1380 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-003 | permitted | bound by precedent | REC-VP-L-00916 |  |
| 1381 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-002 | permitted | decided fresh | — |  |
| 1382 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-002 | permitted | decided fresh | — |  |
| 1383 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 1384 | Record artefact digests in the release ledger on publish | VP-SC-006 | permitted | bound by precedent | REC-S0039 | ● |
| 1385 | Skip the dispensing audit test the agent could not get passing | VP-AI-003 | denied | decided fresh | — |  |
| 1386 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 | ● |
| 1387 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1388 | Add regression tests for the note-render encoding path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1389 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-004 | denied | bound by precedent | REC-S0052 |  |
| 1390 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | disposed by citation | — |  |
| 1391 | Require a second approver on admin role assignments | VP-RB-004 | permitted | bound by precedent | REC-VP-C-01317 |  |
| 1392 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted | decided fresh | — |  |
| 1393 | Populate DICOM species and breed tags from the patient record | VP-PO-007 | permitted | decided fresh | — |  |
| 1394 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-007 | denied | bound by precedent | REC-S0001 | ● |
| 1395 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 1396 | Update the manifest and lockfile in the same commit | VP-SC-003 | permitted | bound by precedent | REC-VP-C-01170 | ● |
| 1397 | Update the manifest and lockfile in the same commit | VP-SC-003 | permitted | decided fresh | — | ● |
| 1398 | Revalidate the active session after a privilege change | VP-RB-005 | denied | bound by precedent | REC-S0030 |  |
| 1399 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | decided fresh | — | ● |
| 1400 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | bound by precedent | REC-S0029 | ● |
| 1401 | Assign the daily audit review to the practice manager role | VP-RR-002 | permitted | decided fresh | — |  |
| 1402 | Time-box break-glass access to four hours and log the grant | VP-RB-007 | permitted with conditions | bound by precedent | REC-VP-G-01242 |  |
| 1403 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | decided fresh | — |  |
| 1404 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | decided fresh | — |  |
| 1405 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 1406 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-007 | permitted | bound by precedent | REC-VP-A-00496 |  |
| 1407 | Register the new agent runner in the allowlist policy bundle | VP-CS-010 | denied | decided fresh | — |  |
| 1408 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | bound by precedent | REC-S0028 |  |
| 1409 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 1410 | Require a tag scan at every remains custody transfer | VP-PS-003 | permitted with conditions | bound by precedent | REC-S0074 | ● |
| 1411 | Return a correlation id instead of a stack trace on error | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1412 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | bound by precedent | REC-VP-C-00961 |  |
| 1413 | Verify commit signatures on the protected release branch | VP-SC-009 | permitted | decided fresh | — | ● |
| 1414 | Attach the full triage transcript to the patient's medical record | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01410 |  |
| 1415 | Restrict claim payload deserialisation to known types | VP-AS-002 | permitted | decided fresh | — |  |
| 1416 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | permitted | decided fresh | — |  |
| 1417 | Scope modality worklist queries to the requesting practice | VP-PO-003 | permitted | bound by precedent | REC-S0012 |  |
| 1418 | Let a technician account sign the rabies certificate when the vet is busy | VP-PH-002 | denied | decided fresh | — |  |
| 1419 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-007 | permitted | bound by precedent | REC-VP-A-00496 |  |
| 1420 | Pin the radiography panel firmware version in the device inventory | VP-PO-004 | permitted | decided fresh | — |  |
| 1421 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-004 | denied | bound by precedent | REC-S0052 |  |
| 1422 | Let one admin grant EPCS signing rights from the user screen | VP-CS-011 | denied | decided fresh | — |  |
| 1423 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1424 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 1425 | Renumber the point-of-care provisions after the device policy merge | VP-GV-003 | denied | decided fresh | — |  |
| 1426 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | bound by precedent | REC-S0041 |  |
| 1427 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted | decided fresh | — |  |
| 1428 | Link the incident runbook from every breach-detection alert payload | VP-BN-002 | permitted | decided fresh | — |  |
| 1429 | Move the release outside the emergency-hours freeze window | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1430 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | bound by precedent | REC-VP-C-01367 |  |
| 1431 | Unblock enrofloxacin ordering for dairy herds | VP-VC-001 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 1432 | Configure a circuit breaker around the external lab client | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1433 | Tokenise the card number before the invoice row is written | VP-PD-008 | denied | bound by precedent | REC-S0025 |  |
| 1434 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1435 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1436 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh | — | ● |
| 1437 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1438 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | decided fresh | — |  |
| 1439 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted | bound by precedent | REC-S0023 |  |
| 1440 | Add the new charting library licence to the allowlist | VP-SC-004 | permitted | decided fresh | — |  |
| 1441 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-002 | denied | bound by precedent | REC-S0011 |  |
| 1442 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-003 | denied | decided fresh | — |  |
| 1443 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-003 | permitted | decided fresh | — |  |
| 1444 | Require a saved consent record before the euthanasia workflow can proceed | VP-PS-003 | permitted | decided fresh | — |  |
| 1445 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00189 |  |
| 1446 | Assign a named reviewer to the vendored DICOM parser | VP-SC-007 | permitted | decided fresh | — |  |
| 1447 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1448 | Verify commit signatures on the protected release branch | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 1449 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted with conditions | bound by precedent | REC-S0063 |  |
| 1450 | Block dose calculation until a current weight is recorded for the visit | VP-PS-002 | permitted | decided fresh | — |  |
| 1451 | Attach the full triage transcript to the patient's medical record | VP-PS-002 | permitted | decided fresh | — |  |
| 1452 | Match study patient identity on microchip and account number | VP-PO-006 | permitted | decided fresh | — |  |
| 1453 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted | bound by precedent | REC-S0012 |  |
| 1454 | Verify commit signatures on the protected release branch | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 1455 | Write a docket entry for every uncharged arrival | VP-GV-005 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 1456 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 1457 | Ship the boarding availability endpoint without a role check | VP-RB-001 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 1458 | Add permutation tests across the role-permission matrix | VP-RB-007 | denied | bound by precedent | REC-VP-C-01011 |  |
| 1459 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 1460 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-B-00910 |  |
| 1461 | Validate delegated task lists against the state practice act table | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 1462 | Allowlist microchip identifier formats at the API boundary | VP-AS-002 | permitted | bound by precedent | REC-VP-L-00696 |  |
| 1463 | Ship a down-migration for the visit-summary table change | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1464 | Log the acknowledgement disposition on the referral timeline | VP-GV-007 | permitted | bound by precedent | REC-S0064 |  |
| 1465 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 1466 | Pin the build runner image and make each job ephemeral | VP-SC-009 | permitted | bound by precedent | REC-VP-A-01413 |  |
| 1467 | Move threshold parameters into the legislated configuration | VP-GV-006 | permitted | decided fresh | — |  |
| 1468 | Show which record controlled on the decision page | VP-GV-006 | permitted | decided fresh | — |  |
| 1469 | Bind each service account to a single practice id | VP-RB-007 | permitted | bound by precedent | REC-VP-A-00080 |  |
| 1470 | Enforce authorisation server-side on the discharge summary route | VP-AS-003 | permitted | decided fresh | — | ● |
| 1471 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00181 |  |
| 1472 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 1473 | Hand the checkout redirect to the validated payment processor | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1474 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted | decided fresh | — |  |
| 1475 | Verify the hash chain when an audit bundle is exported | VP-RR-006 | permitted | decided fresh | — |  |
| 1476 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | decided fresh | — |  |
| 1477 | Assign a named reviewer to the vendored DICOM parser | VP-SC-005 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 1478 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | decided fresh | — | ● |
| 1479 | Require a named human reviewer on every agent-authored pull request | VP-AI-005 | permitted | bound by precedent | REC-S0045 |  |
| 1480 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1481 | Turn the pound-kilogram mismatch error into a dismissable warning | VP-PS-001 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 1482 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | denied | bound by precedent | REC-S0009 |  |
| 1483 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-003 | permitted | decided fresh | — |  |
| 1484 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-003 | permitted | decided fresh | — |  |
| 1485 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-B-00420 |  |
| 1486 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1487 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | bound by precedent | REC-S0053 | ● |
| 1488 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-010 | permitted | decided fresh | — | ● |
| 1489 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1490 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted | decided fresh | — |  |
| 1491 | Split the agent-refactored invoicing function to cut its branching | VP-AI-005 | permitted | decided fresh | — |  |
| 1492 | Review agent-authored tests for tautological assertions | VP-AI-005 | permitted | decided fresh | — |  |
| 1493 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | bound by precedent | REC-S0023 |  |
| 1494 | Make the withdrawal interval optional on food-animal orders | VP-VC-005 | denied | decided fresh | — |  |
| 1495 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 1496 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-006 | permitted | decided fresh | — |  |
| 1497 | Mute the bulk owner-data export alert to quiet the on-call pager | VP-BN-002 | denied | bound by precedent | REC-VP-B-00173 |  |
| 1498 | Add an immutability test for the dispensing log writer | VP-RR-007 | permitted | decided fresh | — |  |
| 1499 | Assign the daily audit review to the practice manager role | VP-RR-007 | permitted | decided fresh | — |  |
| 1500 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | decided fresh | — | ● |
| 1501 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | bound by precedent | REC-S0029 |  |
| 1502 | Point the resolver at the private registry before the public one | VP-SC-008 | permitted | decided fresh | — |  |
| 1503 | Derive tenant id from the session, never from a request header | VP-RB-004 | permitted | bound by precedent | REC-VP-C-01317 |  |
| 1504 | Validate webhook destinations against the outbound allowlist | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 1505 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | bound by precedent | REC-VP-C-01367 |  |
| 1506 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-003 | permitted with conditions | decided fresh | — | ● |
| 1507 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | bound by precedent | REC-VP-N-01145 |  |
| 1508 | Renumber the point-of-care provisions after the device policy merge | VP-RR-004 | denied | decided fresh | — |  |
| 1509 | Enforce the tenant scope in the query layer, not the handler | VP-RB-006 | denied | bound by precedent | REC-S0031 |  |
| 1510 | Add the boarding service to the critical-service list in policy | VP-CS-010 | denied | decided fresh | — |  |
| 1511 | Reject malformed segments without committing a partial patient write | VP-PO-002 | denied | bound by precedent | REC-S0011 |  |
| 1512 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 1513 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00181 |  |
| 1514 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1515 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-002 | denied | bound by precedent | REC-VP-C-01059 |  |
| 1516 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — | ● |
| 1517 | Route diversion alerts to the medical director's queue within the hour | VP-CS-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1518 | Add the new charting library licence to the allowlist | VP-SC-003 | permitted | decided fresh | — |  |
| 1519 | Block record purges that fall inside the two-year retention term | VP-CS-010 | permitted | bound by precedent | REC-VP-A-01488 |  |
| 1520 | Move the authorisation decision out of the portal frontend | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 1521 | Make the human review queue reachable from the portal | VP-GV-005 | permitted with conditions | bound by precedent | REC-S0062 | ● |
| 1522 | Require an explicit share grant for cross-practice referrals | VP-RB-005 | permitted | decided fresh | — |  |
| 1523 | Require a second approver on admin role assignments | VP-RB-005 | permitted | decided fresh | — |  |
| 1524 | Drop internal identifiers from the public error envelope | VP-AS-003 | permitted | decided fresh | — |  |
| 1525 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01261 |  |
| 1526 | Restrict claim payload deserialisation to known types | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1527 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 1528 | Add the transport welfare checklist to the boarding intake form | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1529 | Mute the bulk owner-data export alert to quiet the on-call pager | VP-BN-002 | denied | bound by precedent | REC-VP-B-00173 |  |
| 1530 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | decided fresh | — |  |
| 1531 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-003 | permitted | decided fresh | — |  |
| 1532 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | bound by precedent | REC-VP-C-01384 |  |
| 1533 | Bump the HL7 parser to the patched upstream release | VP-SC-006 | permitted with conditions | decided fresh | — | ● |
| 1534 | Preserve the original entry when a chart amendment is filed | VP-RR-007 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 1535 | Serialise inventory decrements with a row-level lock | VP-HA-003 | permitted | decided fresh | — |  |
| 1536 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 1537 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1538 | Give consent withdrawal the same one-click path as granting it | VP-PD-008 | permitted | bound by precedent | REC-VP-N-00089 |  |
| 1539 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 1540 | Pin the radiography panel firmware version in the device inventory | VP-PO-005 | denied | bound by precedent | REC-S0014 |  |
| 1541 | Add contract tests for the pinned HL7 v2 profile | VP-PO-010 | permitted | decided fresh | — |  |
| 1542 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-012 | permitted | bound by precedent | REC-S0006 |  |
| 1543 | Prove the backup restore before the vaccine index migration | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1544 | Derive tenant id from the session, never from a request header | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00779 |  |
| 1545 | Stagger analyzer polling to flatten the morning load peak | VP-HA-002 | permitted | decided fresh | — |  |
| 1546 | Pin the radiography panel firmware version in the device inventory | VP-PO-007 | denied | bound by precedent | REC-S0016 | ● |
| 1547 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted | decided fresh | — |  |
| 1548 | Verify the hash chain when an audit bundle is exported | VP-RR-003 | permitted | decided fresh | — |  |
| 1549 | Route diversion alerts to the medical director's queue within the hour | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 1550 | Add the new charting library licence to the allowlist | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 |  |
| 1551 | Wrap result-to-patient binding in a single database transaction | VP-PO-009 | permitted | decided fresh | — |  |
| 1552 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01272 |  |
| 1553 | Cap analyzer retries at five with exponential backoff | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 1554 | Show the premises visit date on the large-animal chart header | VP-VC-005 | permitted with conditions | bound by precedent | REC-S0008 |  |
| 1555 | Bound the data subject export job to the statutory window | VP-PD-008 | permitted | decided fresh | — |  |
| 1556 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 1557 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1558 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-C-00947 |  |
| 1559 | Deny clinical note writes to the receptionist role | VP-RB-005 | permitted | decided fresh | — | ● |
| 1560 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted | bound by precedent | REC-VP-N-00720 |  |
| 1561 | Enforce authorisation server-side on the discharge summary route | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 1562 | Make the consent signature pad completable by keyboard alone | VP-AX-001 | permitted | bound by precedent | REC-S0078 |  |
| 1563 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | decided fresh | — |  |
| 1564 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-002 | permitted | bound by precedent | REC-S0075 |  |
| 1565 | Widen the deploy freeze exception list in the governance repo | VP-GV-005 | denied | decided fresh | — |  |
| 1566 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-003 | permitted | bound by precedent | REC-VP-L-01322 |  |
| 1567 | Let the calculator accept twice the labelled equine maximum | VP-VC-003 ⛔ | denied | refused at the floor | — |  |
| 1568 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 1569 | Attach a residue risk assessment to the food-animal order form | VP-VC-004 | permitted | decided fresh | — |  |
| 1570 | Attach a residue risk assessment to the food-animal order form | VP-VC-004 | permitted | decided fresh | — |  |
| 1571 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1572 | Enforce authorisation server-side on the discharge summary route | VP-AS-005 | permitted | bound by precedent | REC-S0053 |  |
| 1573 | Encode clinical note text before rendering it in the portal | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 1574 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-011 | denied | bound by precedent | REC-S0005 |  |
| 1575 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 1576 | Block dose calculation until a current weight is recorded for the visit | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01410 | ● |
| 1577 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 1578 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1579 | Let the coding agent rewrite the session authentication middleware | VP-AI-001 VP-GV-003 ⛔ | denied | refused at the floor | — |  |
| 1580 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1581 | Check consent currency before the reminder engine sends | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 1582 | Prove the backup restore before the vaccine index migration | VP-HA-002 | permitted | decided fresh | — |  |
| 1583 | Assign a named reviewer to the vendored DICOM parser | VP-SC-006 | permitted | bound by precedent | REC-S0039 |  |
| 1584 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted | decided fresh | — |  |
| 1585 | Give front desk staff the controlled dispensing permission | VP-RB-002 | denied | decided fresh | — |  |
| 1586 | Serialise inventory decrements with a row-level lock | VP-HA-001 | permitted | decided fresh | — |  |
| 1587 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00819 |  |
| 1588 | Require a named response before a critical-value alert can be marked acknowledged | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 1589 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — |  |
| 1590 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-001 | permitted | decided fresh | — |  |
| 1591 | Add the boarding service to the critical-service list in policy | VP-RR-002 | denied | decided fresh | — |  |
| 1592 | Require the veterinary care plan on the regulated facility record | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 1593 | Record artefact digests in the release ledger on publish | VP-SC-001 | permitted | decided fresh | — |  |
| 1594 | Bind each service account to a single practice id | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 | ● |
| 1595 | Link the breach notification runbook from the incident template | VP-PD-008 | permitted | decided fresh | — |  |
| 1596 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | decided fresh | — |  |
| 1597 | Drop internal identifiers from the public error envelope | VP-AS-005 | permitted | bound by precedent | REC-VP-L-00436 | ● |
| 1598 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 1599 | Add the new charting library licence to the allowlist | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 1600 | Revalidate the active session after a privilege change | VP-RB-003 | permitted with conditions | decided fresh | — | ● |
| 1601 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | bound by precedent | REC-VP-L-00436 | ● |
| 1602 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1603 | Add an immutability test for the dispensing log writer | VP-RR-002 | denied | bound by precedent | REC-S0054 |  |
| 1604 | Show the technician's credential status on the surgery board | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1605 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 1606 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01013 |  |
| 1607 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-005 | permitted with conditions | decided fresh | — | ● |
| 1608 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-B-00721 |  |
| 1609 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | disposed by citation | — |  |
| 1610 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-003 | permitted | decided fresh | — |  |
| 1611 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-003 | permitted | decided fresh | — |  |
| 1612 | Return a correlation id instead of a stack trace on error | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 1613 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | decided fresh | — | ● |
| 1614 | Prompt for a pain management plan at surgical discharge | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 1615 | Cover the new boarding endpoint with a role check test | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 1616 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | decided fresh | — |  |
| 1617 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 1618 | Purge Form 222 order records after one year to shrink the archive | VP-DR-001 VP-PO-008 ⛔ | denied | refused at the floor | — |  |
| 1619 | Restrict agent outbound calls to the allowlisted host set | VP-AI-008 | permitted | bound by precedent | REC-S0048 |  |
| 1620 | Overwrite the original diagnosis text when a chart is amended | VP-RR-001 VP-GV-005 ⛔ | denied | refused at the floor | — |  |
| 1621 | Populate DICOM species and breed tags from the patient record | VP-PO-007 | denied | bound by precedent | REC-VP-C-01546 |  |
| 1622 | Assign a named reviewer to the vendored DICOM parser | VP-SC-005 | permitted | decided fresh | — |  |
| 1623 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted | decided fresh | — |  |
| 1624 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01594 |  |
| 1625 | Add the new charting library licence to the allowlist | VP-SC-007 | permitted | disposed by citation | — |  |
| 1626 | Allowlist microchip identifier formats at the API boundary | VP-AS-002 | permitted | bound by precedent | REC-S0050 |  |
| 1627 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1628 | Withhold prescription finalisation from technician accounts | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 1629 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01343 |  |
| 1630 | Write the decision rationale at resolution time, not on export | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 1631 | Deny clinical note writes to the receptionist role | VP-RB-004 | permitted | bound by precedent | REC-VP-N-01145 | ● |
| 1632 | Log the acknowledgement disposition on the referral timeline | VP-GV-005 | permitted | decided fresh | — |  |
| 1633 | Route a human review request from the decision detail page | VP-GV-005 | permitted | decided fresh | — |  |
| 1634 | Release medical records regardless of outstanding balance | VP-CC-004 | permitted | decided fresh | — |  |
| 1635 | Flag food-animal status on the patient banner before dispensing | VP-VC-007 | permitted with conditions | bound by precedent | REC-VP-S-01456 | ● |
| 1636 | Return a correlation id instead of a stack trace on error | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1637 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — | ● |
| 1638 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | bound by precedent | REC-VP-C-00961 | ● |
| 1639 | Pin the radiography panel firmware version in the device inventory | VP-PO-008 | permitted with conditions | decided fresh | — | ● |
| 1640 | Check object ownership before returning a patient chart | VP-RB-008 | permitted | decided fresh | — |  |
| 1641 | Populate DICOM species and breed tags from the patient record | VP-PO-002 | permitted with conditions | bound by precedent | REC-VP-C-01037 |  |
| 1642 | Drop internal identifiers from the public error envelope | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 1643 | Make the feed directive expiry date a mandatory field | VP-VC-005 | permitted with conditions | bound by precedent | REC-S0008 |  |
| 1644 | Restrict claim payload deserialisation to known types | VP-AS-004 | permitted | decided fresh | — | ● |
| 1645 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00819 | ● |
| 1646 | Block payment-plan enrolment from an account without verified adult status | VP-CC-005 | permitted | decided fresh | — |  |
| 1647 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00181 |  |
| 1648 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-002 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 1649 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 1650 | Restore session objects by deserialising the client-supplied blob | VP-AS-002 | denied | decided fresh | — |  |
| 1651 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-003 | permitted | bound by precedent | REC-S0069 |  |
| 1652 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | decided fresh | — |  |
| 1653 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh | — |  |
| 1654 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 1655 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | bound by precedent | REC-VP-A-00080 |  |
| 1656 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1657 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-C-00947 |  |
| 1658 | Review agent-authored tests for tautological assertions | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 1659 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-B-00721 |  |
| 1660 | Make the feed directive expiry date a mandatory field | VP-VC-005 | permitted | decided fresh | — |  |
| 1661 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-005 | permitted | decided fresh | — |  |
| 1662 | Reuse the stored consent flag without rechecking its date | VP-PD-009 | denied | decided fresh | — |  |
| 1663 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted with conditions | bound by precedent | REC-S0037 |  |
| 1664 | Restrict claim payload deserialisation to known types | VP-AS-001 | permitted | decided fresh | — | ● |
| 1665 | Let the client extend the mobile check-in session before it times out | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 | ● |
| 1666 | Quarantine unmatched analyzer results for technician review | VP-PO-009 | permitted | decided fresh | — | ● |
| 1667 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1668 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | disposed by citation | — |  |
| 1669 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-001 | permitted | decided fresh | — |  |
| 1670 | Run the secret scanner over the diff in pre-merge CI | VP-SC-001 | permitted | decided fresh | — |  |
| 1671 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 1672 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-003 | permitted | decided fresh | — | ● |
| 1673 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-004 | permitted | decided fresh | — |  |
| 1674 | Allowlist microchip identifier formats at the API boundary | VP-AS-004 | permitted | decided fresh | — |  |
| 1675 | Add a flag that skips the dispensing checks during demos | VP-CS-007 | denied | decided fresh | — |  |
| 1676 | Require a verified adult guardian before a minor's client account can be created | VP-CC-002 | permitted | bound by precedent | REC-VP-A-00516 |  |
| 1677 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted | decided fresh | — |  |
| 1678 | Separate the audit register store from the precedent store | VP-GV-007 | permitted | bound by precedent | REC-VP-C-01305 |  |
| 1679 | Add captions to the discharge-instructions video on the portal | VP-AX-002 | permitted | decided fresh | — |  |
| 1680 | Withhold prescription finalisation from technician accounts | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01594 |  |
| 1681 | Require a second approver on admin role assignments | VP-RB-004 | permitted | decided fresh | — |  |
| 1682 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-B-00554 |  |
| 1683 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | decided fresh | — |  |
| 1684 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted | bound by precedent | REC-VP-A-00673 | ● |
| 1685 | Replace the hand-rolled token hash with the vetted library | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1686 | Add a free-text field for the owner's social security number | VP-PD-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 1687 | Restrict claim payload deserialisation to known types | VP-AS-001 | permitted | bound by precedent | REC-VP-A-01664 |  |
| 1688 | Disable the biennial inventory job during the systems migration | VP-DR-002 VP-PD-003 ⛔ | denied | refused at the floor | — |  |
| 1689 | Add a support endpoint that dumps the full owner record | VP-PD-002 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 1690 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted | decided fresh | — |  |
| 1691 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 1692 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | decided fresh | — |  |
| 1693 | Hard-stop the dose calculator on a declared weight-unit mismatch | VP-PS-002 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 1694 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted | decided fresh | — |  |
| 1695 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | decided fresh | — |  |
| 1696 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | decided fresh | — |  |
| 1697 | Route vendor incident webhooks into the monitored incident queue | VP-BN-003 | denied | bound by precedent | REC-S0066 |  |
| 1698 | Return a correlation id instead of a stack trace on error | VP-AS-006 | permitted | docketed — not charged | — |  |
| 1699 | Require acknowledgement before a critical value page clears | VP-PO-007 | denied | bound by precedent | REC-VP-C-01546 |  |
| 1700 | Ship beef-herd orders without the residue assessment step | VP-VC-004 | denied | decided fresh | — |  |
| 1701 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted | decided fresh | — |  |
| 1702 | Route diversion alerts to the medical director's queue within the hour | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 1703 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-G-01577 |  |
| 1704 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted | decided fresh | — |  |
| 1705 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-002 | permitted | bound by precedent | REC-VP-A-00516 | ● |
| 1706 | Let staff reassign a study to another patient in one click | VP-PO-004 | denied | decided fresh | — |  |
| 1707 | Encode clinical note text before rendering it in the portal | VP-AS-004 | permitted | bound by precedent | REC-VP-L-00761 | ● |
| 1708 | Build the chart-search filter by concatenating the query string | VP-AS-005 | denied | decided fresh | — |  |
| 1709 | Gate merges on a clean provenance verification step | VP-SC-006 | permitted | bound by precedent | REC-VP-C-01384 |  |
| 1710 | Let the triage chatbot introduce itself as Dr. Assistant | VP-PS-002 | denied | decided fresh | — |  |
| 1711 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | denied | bound by precedent | REC-S0001 |  |
| 1712 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1713 | Require a named human reviewer on every agent-authored pull request | VP-AI-003 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 1714 | Add regression tests for the note-render encoding path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1715 | Release medical records regardless of outstanding balance | VP-CC-002 | permitted | bound by precedent | REC-VP-A-00516 |  |
| 1716 | Strip untrusted ticket text from the agent's instruction context | VP-AI-004 | permitted | decided fresh | — |  |
| 1717 | Review agent-authored tests for tautological assertions | VP-AI-004 | permitted | decided fresh | — |  |
| 1718 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted | decided fresh | — |  |
| 1719 | Move the authorisation decision out of the portal frontend | VP-RB-003 | permitted | bound by precedent | REC-VP-N-00198 |  |
| 1720 | Derive tenant id from the session, never from a request header | VP-RB-006 | permitted | decided fresh after a tie | none_tie |  |
| 1721 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1722 | Vendor the AGPL HL7 parser into the shipped practice API | VP-SC-007 | denied | decided fresh | — |  |
| 1723 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | bound by precedent | REC-VP-L-01322 | ● |
| 1724 | Check the version token on clinical note writes | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1725 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-007 | denied | bound by precedent | REC-VP-C-01394 |  |
| 1726 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 1727 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-002 | permitted | bound by precedent | REC-S0075 |  |
| 1728 | Serialise inventory decrements with a row-level lock | VP-HA-003 | permitted | decided fresh | — |  |
| 1729 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted | bound by precedent | REC-VP-A-01613 |  |
| 1730 | Stagger analyzer polling to flatten the morning load peak | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1731 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-007 | permitted | decided fresh | — |  |
| 1732 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 1733 | Queue reminder sends so a retry storm cannot amplify | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1734 | Bump the HL7 parser to the patched upstream release | VP-SC-002 | permitted | bound by precedent | REC-VP-L-01017 |  |
| 1735 | Sanitise filenames in the lab attachment upload handler | — | permitted | docketed — nothing engaged | — |  |
| 1736 | Block record purges that fall inside the two-year retention term | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 1737 | Make the feed directive expiry date a mandatory field | VP-VC-005 | permitted | decided fresh | — |  |
| 1738 | Require a recorded in-person exam date before extralabel orders | VP-VC-005 | permitted | decided fresh | — |  |
| 1739 | Trim the owner breach-notice template down to a one-line summary | VP-BN-003 | denied | decided fresh | — |  |
| 1740 | Cap analyzer retries at five with exponential backoff | VP-PO-009 | permitted | bound by precedent | REC-VP-A-01666 |  |
| 1741 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted | decided fresh | — |  |
| 1742 | Bound the data subject export job to the statutory window | VP-PD-007 | denied | bound by precedent | REC-S0024 | ● |
| 1743 | Fetch whatever callback URL the practice webhook supplies | VP-AS-003 | denied | decided fresh | — |  |
| 1744 | Expose the contest path to the owner, not only to staff | VP-GV-004 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 1745 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | permitted | decided fresh | — |  |
| 1746 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-010 | permitted with conditions | bound by precedent | REC-S0004 |  |
| 1747 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-002 ⛔ | denied | refused at the floor | — |  |
| 1748 | Derive tenant id from the session, never from a request header | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01478 |  |
| 1749 | Match study patient identity on microchip and account number | VP-PO-010 | permitted | decided fresh | — |  |
| 1750 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-B-00721 | ● |
| 1751 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted | decided fresh | — |  |
| 1752 | Match study patient identity on microchip and account number | VP-PO-008 | permitted with conditions | bound by precedent | REC-VP-G-01639 |  |
| 1753 | Gate merges on a clean provenance verification step | VP-SC-008 | permitted | disposed by citation | — |  |
| 1754 | Keep the retention clock unchanged when a record is edited | VP-RR-005 | permitted | decided fresh | — |  |
| 1755 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted | decided fresh | — |  |
| 1756 | Compute breach scope from the complete access log instead of a sample | VP-BN-002 | permitted | decided fresh | — |  |
| 1757 | Update the manifest and lockfile in the same commit | VP-SC-004 | permitted with conditions | bound by precedent | REC-S0037 | ● |
| 1758 | Require a second approver on admin role assignments | VP-RB-004 | permitted | decided fresh | — | ● |
| 1759 | Store payment references, not card numbers, on the retry queue | VP-PD-009 | denied | bound by precedent | REC-S0026 |  |
| 1760 | Withhold prescription finalisation from technician accounts | VP-RB-003 | permitted | decided fresh | — |  |
| 1761 | Cover the new boarding endpoint with a role check test | VP-RB-003 | permitted | decided fresh | — |  |
| 1762 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1763 | Enforce the tenant scope in the query layer, not the handler | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 1764 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 1765 | Cap analyzer retries at five with exponential backoff | VP-PO-004 | denied | bound by precedent | REC-S0013 |  |
| 1766 | Extend access-log retention to cover the full notification lookback window | VP-BN-003 | permitted | decided fresh | — |  |
| 1767 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | bound by precedent | REC-VP-L-00475 | ● |
| 1768 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-006 | denied | decided fresh | — |  |
| 1769 | Attribute the standing declaration to the enacting authority | VP-GV-003 | denied | bound by precedent | REC-S0060 |  |
| 1770 | Check the version token on clinical note writes | VP-HA-002 | permitted | decided fresh | — |  |
| 1771 | Gate merges on a clean provenance verification step | VP-SC-001 | denied | bound by precedent | REC-S0034 | ● |
| 1772 | Show the technician's credential status on the surgery board | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1773 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | bound by precedent | REC-VP-C-01767 |  |
| 1774 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1775 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted with conditions | bound by precedent | REC-VP-G-01726 |  |
| 1776 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-004 | permitted | docketed — not charged | — |  |
| 1777 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | bound by precedent | REC-VP-C-01723 |  |
| 1778 | Drop the practice filter from the referral search endpoint | VP-RB-001 VP-PD-008 ⛔ | denied | refused at the floor | — |  |
| 1779 | Add the new charting library licence to the allowlist | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 1780 | Validate webhook destinations against the outbound allowlist | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 1781 | Honour opt-out state at export time in the marketing job | VP-PD-009 | denied | bound by precedent | REC-S0026 |  |
| 1782 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh | — |  |
| 1783 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh | — |  |
| 1784 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-007 | permitted | bound by precedent | REC-VP-C-01305 |  |
| 1785 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | permitted | decided fresh | — |  |
| 1786 | Honour opt-out state at export time in the marketing job | VP-PD-004 | permitted | decided fresh | — |  |
| 1787 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1788 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | denied | bound by precedent | REC-S0002 |  |
| 1789 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-PD-006 | denied | decided fresh | — |  |
| 1790 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted | bound by precedent | REC-S0041 |  |
| 1791 | Verify commit signatures on the protected release branch | VP-SC-008 | permitted | decided fresh | — | ● |
| 1792 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 1793 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-C-00947 | ● |
| 1794 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-001 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 1795 | Attach build provenance to the practice API release artefact | VP-SC-002 | permitted | bound by precedent | REC-VP-A-01292 |  |
| 1796 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 1797 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | bound by precedent | REC-S0023 |  |
| 1798 | Require a recorded in-person exam date before extralabel orders | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 1799 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 |  |
| 1800 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | decided fresh | — |  |
| 1801 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-004 | denied | bound by precedent | REC-S0007 |  |
| 1802 | Validate delegated task lists against the state practice act table | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 1803 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 1804 | Bind each service account to a single practice id | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 1805 | Hide the contest link when the decision is a denial | VP-GV-001 VP-GV-007 ⛔ | denied | refused at the floor | — |  |
| 1806 | Attach build provenance to the practice API release artefact | VP-SC-001 | denied | bound by precedent | REC-VP-C-01771 |  |
| 1807 | Keep the contest link visible on every automated decision notice | VP-GV-007 | permitted | decided fresh | — |  |
| 1808 | Keep the contest link visible on every automated decision notice | VP-GV-007 | permitted | decided fresh | — |  |
| 1809 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-005 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 1810 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 1811 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | bound by precedent | REC-S0023 |  |
| 1812 | Withhold prescription finalisation from technician accounts | VP-RB-002 | permitted | decided fresh | — |  |
| 1813 | Require the veterinary care plan on the regulated facility record | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 1814 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | decided fresh | — | ● |
| 1815 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 1816 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted with conditions | bound by precedent | REC-VP-U-01671 | ● |
| 1817 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | decided fresh | — | ● |
| 1818 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01272 | ● |
| 1819 | Swallow PDMP submission errors so checkout never blocks | VP-CS-010 | denied | decided fresh | — | ● |
| 1820 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1821 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01594 |  |
| 1822 | Verify the hash chain when an audit bundle is exported | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 1823 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | bound by precedent | REC-VP-L-01287 |  |
| 1824 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-008 | permitted with conditions | decided fresh | — | ● |
| 1825 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | bound by precedent | REC-VP-L-01644 |  |
| 1826 | Label agent-authored commits so review routing can see them | VP-AI-005 | permitted | decided fresh | — |  |
| 1827 | Require a named human reviewer on every agent-authored pull request | VP-AI-005 | permitted | decided fresh | — |  |
| 1828 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 1829 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | bound by precedent | REC-VP-A-01613 |  |
| 1830 | Record the prompt and context hash on the agent's pull request | VP-AI-008 | permitted | decided fresh | — |  |
| 1831 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-C-01750 | ● |
| 1832 | Block payment-plan enrolment from an account without verified adult status | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 1833 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | denied | bound by precedent | REC-S0051 | ● |
| 1834 | Enable the refill button on hydromorphone prescriptions | VP-CS-001 VP-CS-007 ⛔ | denied | refused at the floor | — |  |
| 1835 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 1836 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 1837 | Return a correlation id instead of a stack trace on error | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 1838 | Retry the blood gas analyzer until it answers | VP-PO-002 | denied | decided fresh | — |  |
| 1839 | Add an accessible name to the new custom toggle control | VP-AX-001 | permitted | decided fresh | — |  |
| 1840 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | decided fresh | — |  |
| 1841 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-004 | permitted | decided fresh | — |  |
| 1842 | Record a manual screen-reader check for every new portal flow | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01259 |  |
| 1843 | Match the required supervision level to the task's risk tier | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 1844 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | bound by precedent | REC-VP-B-01500 |  |
| 1845 | Ship the boarding availability endpoint without a role check | VP-RB-006 | denied | decided fresh | — |  |
| 1846 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | permitted | bound by precedent | REC-VP-C-01386 |  |
| 1847 | Version chart amendments instead of editing rows in place | VP-RR-004 | permitted | decided fresh | — |  |
| 1848 | Add an immutability test for the dispensing log writer | VP-RR-004 | permitted | decided fresh | — |  |
| 1849 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-002 | permitted | decided fresh | — |  |
| 1850 | Link the breach notification runbook from the incident template | VP-PD-007 | permitted | decided fresh | — |  |
| 1851 | Return a correlation id instead of a stack trace on error | VP-AS-004 | permitted | bound by precedent | REC-VP-L-01644 |  |
| 1852 | Add regression tests for the note-render encoding path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1853 | Make the note autosave idempotent under client retry | VP-HA-005 | permitted | docketed — not charged | — |  |
| 1854 | Route every Schedule II reorder through the CSOS certificate signer | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1855 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 1856 | Label agent-authored commits so review routing can see them | VP-AI-006 | permitted | decided fresh | — |  |
| 1857 | Add a campaign endpoint that exports the whole owner list | VP-PD-001 VP-VC-005 ⛔ | denied | refused at the floor | — |  |
| 1858 | Verify the hash chain when an audit bundle is exported | VP-RR-006 | permitted | decided fresh | — |  |
| 1859 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-009 | permitted | bound by precedent | REC-VP-N-01260 | ● |
| 1860 | Release medical records regardless of outstanding balance | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 1861 | Extend order-form record retention to cover the full two-year floor | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1862 | Update the manifest and lockfile in the same commit | VP-SC-006 | permitted | decided fresh | — |  |
| 1863 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 1864 | Add regression tests covering the unit-conversion boundaries in the dose calculator | VP-PS-002 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 1865 | Add permutation tests across the role-permission matrix | VP-RB-006 | permitted | decided fresh | — |  |
| 1866 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted with conditions | bound by precedent | REC-VP-G-01828 |  |
| 1867 | Make the human review queue reachable from the portal | VP-GV-003 | permitted | decided fresh | — |  |
| 1868 | Move threshold parameters into the legislated configuration | VP-GV-003 | permitted | decided fresh | — |  |
| 1869 | Publish the contest counts in the audit export header | VP-RR-005 | permitted | decided fresh | — |  |
| 1870 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1871 | Add the suspected-abuse report option back to the chart action menu | VP-PH-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1872 | Amend the retention schedule for controlled-substance records in the rulebook | VP-CC-002 | denied | decided fresh | — |  |
| 1873 | Prompt for an off-label rationale in the medical record | VP-VC-007 | permitted | bound by precedent | REC-VP-A-00673 |  |
| 1874 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1875 | Add a keyboard path out of the consent modal's focus trap | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01197 |  |
| 1876 | Record artefact digests in the release ledger on publish | VP-SC-008 | permitted | decided fresh | — |  |
| 1877 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted | bound by precedent | REC-VP-A-01488 |  |
| 1878 | Show which record controlled on the decision page | VP-GV-006 | permitted | decided fresh | — | ● |
| 1879 | Enable the portal's credential-stuffing detector on client login | VP-BN-003 | denied | bound by precedent | REC-S0066 |  |
| 1880 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | decided fresh after a tie | none_tie |  |
| 1881 | Cover the new boarding endpoint with a role check test | VP-RB-008 | denied | bound by precedent | REC-S0033 | ● |
| 1882 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 1883 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-008 | permitted with conditions | bound by precedent | REC-VP-G-01824 |  |
| 1884 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1885 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted | bound by precedent | REC-VP-N-00089 | ● |
| 1886 | Encode clinical note text before rendering it in the portal | VP-AS-006 | permitted | docketed — not charged | — |  |
| 1887 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01576 | ● |
| 1888 | Turn off audit writes on the hot dispensing path | VP-RR-004 | denied | decided fresh | — |  |
| 1889 | Run semantic analysis over the agent diff in CI | VP-AI-006 | denied | bound by precedent | REC-S0046 |  |
| 1890 | Add contract tests for the pinned HL7 v2 profile | VP-PO-008 | permitted | decided fresh | — |  |
| 1891 | Add contract tests for the pinned HL7 v2 profile | VP-PO-008 | permitted | decided fresh | — |  |
| 1892 | Build the chart-search filter by concatenating the query string | VP-AS-001 | denied | decided fresh | — |  |
| 1893 | Attribute the standing declaration to the enacting authority | VP-GV-007 | permitted | bound by precedent | REC-VP-C-01305 |  |
| 1894 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-002 | permitted | decided fresh | — |  |
| 1895 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted | decided fresh | — |  |
| 1896 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 |  |
| 1897 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 1898 | Enforce the tenant scope in the query layer, not the handler | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01436 |  |
| 1899 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 1900 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | bound by precedent | REC-VP-B-01814 |  |
| 1901 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 1902 | Pre-check the wellness-plan auto-renewal box at checkout | VP-CC-001 VP-AI-003 ⛔ | denied | refused at the floor | — |  |
| 1903 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-C-01750 |  |
| 1904 | Run agent-generated code inside the sandboxed runner only | VP-AI-003 | permitted | decided fresh | — |  |
| 1905 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | bound by precedent | REC-VP-B-00110 |  |
| 1906 | Call an external summarisation API from the agent's new helper | VP-AI-006 | denied | decided fresh | — |  |
| 1907 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | bound by precedent | REC-VP-C-01859 |  |
| 1908 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1909 | Withhold prescription finalisation from technician accounts | VP-RB-008 | denied | bound by precedent | REC-S0033 |  |
| 1910 | Return the full exception text in the API error body | VP-AS-002 | denied | decided fresh | — |  |
| 1911 | Parameterise the new chart-search query | VP-AS-004 | permitted | bound by precedent | REC-VP-C-01707 |  |
| 1912 | Link the incident runbook from every breach-detection alert payload | VP-BN-002 | permitted | decided fresh | — |  |
| 1913 | Add the statutory content checklist to the owner breach-notice template | VP-BN-002 | permitted | decided fresh | — |  |
| 1914 | Add a campaign endpoint that exports the whole owner list | VP-PD-006 | denied | decided fresh | — |  |
| 1915 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | bound by precedent | REC-VP-L-00235 |  |
| 1916 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted | decided fresh | — |  |
| 1917 | Show the automated-triage disclosure only on the first message of a session | VP-PS-004 VP-RR-005 ⛔ | denied | refused at the floor | — |  |
| 1918 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00189 |  |
| 1919 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 1920 | Cover the new boarding endpoint with a role check test | VP-RB-008 | denied | bound by precedent | REC-VP-C-01881 | ● |
| 1921 | Enforce authorisation server-side on the discharge summary route | VP-AS-006 | permitted | docketed — not charged | — |  |
| 1922 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 1923 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 1924 | Require the veterinary care plan on the regulated facility record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 1925 | Require an explicit share grant for cross-practice referrals | VP-RB-003 | permitted | bound by precedent | REC-VP-C-01127 |  |
| 1926 | Sanitise filenames in the lab attachment upload handler | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 1927 | Record artefact digests in the release ledger on publish | VP-SC-001 | denied | bound by precedent | REC-VP-C-01281 |  |
| 1928 | Enforce authorisation server-side on the discharge summary route | VP-AS-005 | permitted | decided fresh | — |  |
| 1929 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | bound by precedent | REC-VP-B-01500 | ● |
| 1930 | Amend the retention schedule for controlled-substance records in the rulebook | VP-CS-007 | denied | decided fresh | — |  |
| 1931 | Pull in the charting library release carrying the open critical advisory | VP-SC-009 | denied | decided fresh | — |  |
| 1932 | Allowlist microchip identifier formats at the API boundary | VP-AS-005 | permitted | bound by precedent | REC-VP-C-01597 |  |
| 1933 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted | decided fresh | — |  |
| 1934 | Extend the log redaction filter to the new owner phone field | VP-PD-003 | permitted | decided fresh | — |  |
| 1935 | Remove the suspected-abuse report option from the chart menu | VP-PH-001 VP-CC-003 ⛔ | denied | refused at the floor | — |  |
| 1936 | Let the calculator accept twice the labelled equine maximum | VP-VC-002 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 1937 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-B-00721 |  |
| 1938 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-001 ⛔ | denied | refused at the floor | — |  |
| 1939 | Restrict claim payload deserialisation to known types | VP-AS-006 | permitted | docketed — not charged | — |  |
| 1940 | Make the loss-discovery timestamp immutable once the theft report is filed | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 1941 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-006 VP-AS-002 ⛔ | denied | refused at the floor | — |  |
| 1942 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-001 | denied | bound by precedent | REC-VP-C-01284 |  |
| 1943 | Keep the retention clock unchanged when a record is edited | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 1944 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | decided fresh | — |  |
| 1945 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — |  |
| 1946 | Link the incident runbook from every breach-detection alert payload | VP-BN-002 | permitted with conditions | bound by precedent | REC-S0065 |  |
| 1947 | Turn off audit writes on the hot dispensing path | VP-RR-007 | denied | decided fresh | — |  |
| 1948 | Propose a sunset clause for the analytics pilot exception | VP-CS-007 | denied | decided fresh | — |  |
| 1949 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-005 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 1950 | Auto-merge agent pull requests once CI is green | VP-AI-005 | denied | decided fresh | — |  |
| 1951 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-005 | permitted with conditions | bound by precedent | REC-S0008 |  |
| 1952 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 1953 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | bound by precedent | REC-VP-C-01859 |  |
| 1954 | Move the authorisation decision out of the portal frontend | VP-RB-008 | permitted | decided fresh | — |  |
| 1955 | Require an explicit share grant for cross-practice referrals | VP-RB-008 | permitted | decided fresh | — |  |
| 1956 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-003 | permitted | decided fresh | — | ● |
| 1957 | Scope modality worklist queries to the requesting practice | VP-PO-009 | permitted | bound by precedent | REC-VP-A-01666 | ● |
| 1958 | Attach build provenance to the practice API release artefact | VP-SC-002 | permitted | decided fresh | — |  |
| 1959 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-010 | permitted | bound by precedent | REC-VP-A-01488 |  |
| 1960 | Restrict claim payload deserialisation to known types | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1961 | Require a second approver on admin role assignments | VP-RB-002 | permitted | bound by precedent | REC-S0027 | ● |
| 1962 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-BN-003 ⛔ | denied | refused at the floor | — |  |
| 1963 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 1964 | Require a second approver on admin role assignments | VP-RB-007 | denied | bound by precedent | REC-S0032 |  |
| 1965 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-011 | permitted | decided fresh | — |  |
| 1966 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-005 | permitted with conditions | bound by precedent | REC-VP-S-01798 | ● |
| 1967 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | decided fresh | — | ● |
| 1968 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 1969 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 1970 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-004 | permitted with conditions | bound by precedent | REC-S0077 |  |
| 1971 | Replace the critical value page with a nightly email digest | VP-PO-003 | denied | decided fresh | — |  |
| 1972 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-005 | permitted | bound by precedent | REC-VP-C-01487 | ● |
| 1973 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 1974 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-B-00420 |  |
| 1975 | Add a support endpoint that dumps the full owner record | VP-PD-003 | denied | decided fresh | — | ● |
| 1976 | Record artefact digests in the release ledger on publish | VP-SC-006 | permitted | bound by precedent | REC-S0039 |  |
| 1977 | Store the amendment author alongside the superseded text | VP-RR-002 | permitted | decided fresh | — |  |
| 1978 | Store the amendment author alongside the superseded text | VP-RR-002 | permitted | decided fresh | — |  |
| 1979 | Check object ownership before returning a patient chart | VP-RB-005 | permitted | disposed by citation | — |  |
| 1980 | Strip untrusted ticket text from the agent's instruction context | VP-AI-003 | permitted | decided fresh after a tie | none_tie |  |
| 1981 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted | decided fresh | — |  |
| 1982 | Honour opt-out state at export time in the marketing job | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 1983 | Add contract tests for the pinned HL7 v2 profile | VP-PO-002 | permitted | decided fresh | — |  |
| 1984 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | bound by precedent | REC-VP-B-00110 |  |
| 1985 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-009 | permitted | docketed — not charged | — |  |
| 1986 | Enforce the tenant scope in the query layer, not the handler | VP-RB-007 | permitted | bound by precedent | REC-VP-C-01767 |  |
| 1987 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted | decided fresh | — |  |
| 1988 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 1989 | Queue reminder sends so a retry storm cannot amplify | VP-HA-006 | permitted | docketed — not charged | — |  |
| 1990 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | bound by precedent | REC-VP-A-01817 |  |
| 1991 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 1992 | Enforce authorisation server-side on the discharge summary route | VP-AS-002 | permitted | bound by precedent | REC-VP-L-00696 |  |
| 1993 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 1994 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-002 | permitted | bound by precedent | REC-S0075 |  |
| 1995 | Trust the modality's patient identifier tag exactly as sent | VP-PO-001 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 1996 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-007 | permitted | bound by precedent | REC-VP-A-00496 |  |
| 1997 | Ship a down-migration for the visit-summary table change | VP-HA-006 | permitted | docketed — not charged | — |  |
| 1998 | Drop internal identifiers from the public error envelope | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 1999 | Add regression tests for the note-render encoding path | VP-AS-002 | permitted | decided fresh | — |  |
| 2000 | Restrict claim payload deserialisation to known types | VP-AS-002 | permitted | decided fresh | — |  |
| 2001 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-007 | permitted | decided fresh | — |  |
| 2002 | Block record purges that fall inside the two-year retention term | VP-CS-007 | permitted | decided fresh | — |  |
| 2003 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-C-01039 |  |
| 2004 | Verify commit signatures on the protected release branch | VP-SC-002 | permitted | decided fresh | — |  |
| 2005 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | bound by precedent | REC-VP-N-01145 |  |
| 2006 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2007 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00819 |  |
| 2008 | Shorten the break-glass expiry constant in the rulebook | VP-RR-002 | denied | decided fresh | — |  |
| 2009 | Time-box break-glass access to four hours and log the grant | VP-RB-007 | denied | bound by precedent | REC-VP-C-01011 | ● |
| 2010 | Replace the species dose-range hard stop with an override button | VP-PS-004 VP-GV-004 ⛔ | denied | refused at the floor | — |  |
| 2011 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | bound by precedent | REC-VP-B-01399 | ● |
| 2012 | Reject malformed segments without committing a partial patient write | VP-PO-005 | permitted | decided fresh | — |  |
| 2013 | Make the audit table append-only at the database level | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 2014 | Point the resolver at the private registry before the public one | VP-SC-005 | permitted with conditions | bound by precedent | REC-S0038 | ● |
| 2015 | Validate webhook destinations against the outbound allowlist | VP-AS-003 | permitted | decided fresh | — |  |
| 2016 | Add captions to the discharge-instructions video on the portal | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01259 |  |
| 2017 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 2018 | Add contract tests for the pinned HL7 v2 profile | VP-PO-009 | denied | bound by precedent | REC-S0018 |  |
| 2019 | Wrap result-to-patient binding in a single database transaction | VP-PO-006 | permitted | decided fresh | — |  |
| 2020 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | bound by precedent | REC-VP-B-01814 |  |
| 2021 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 2022 | Withhold prescription finalisation from technician accounts | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01436 |  |
| 2023 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-009 | permitted | decided fresh | — |  |
| 2024 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-009 | permitted | decided fresh | — |  |
| 2025 | Prove the backup restore before the vaccine index migration | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2026 | Attach build provenance to the practice API release artefact | VP-SC-006 | permitted | bound by precedent | REC-S0039 |  |
| 2027 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted | decided fresh | — |  |
| 2028 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted | decided fresh | — |  |
| 2029 | Warn when a dose falls outside the labelled species range | VP-VC-007 | permitted | decided fresh | — |  |
| 2030 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-C-01793 |  |
| 2031 | Store the amendment author alongside the superseded text | VP-RR-006 | permitted | decided fresh | — |  |
| 2032 | Make the audit table append-only at the database level | VP-RR-004 | denied | bound by precedent | REC-S0056 | ● |
| 2033 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-007 | permitted | decided fresh | — |  |
| 2034 | Add the new charting library licence to the allowlist | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 2035 | Scope modality worklist queries to the requesting practice | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 2036 | Suppress reminder sends to any number that has already replied STOP | VP-CC-002 | permitted with conditions | bound by precedent | REC-VP-G-01860 | ● |
| 2037 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-002 | permitted | decided fresh | — |  |
| 2038 | Add an immutability test for the dispensing log writer | VP-RR-004 | permitted | bound by precedent | REC-VP-A-00285 |  |
| 2039 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 VP-SC-003 ⛔ | denied | refused at the floor | — |  |
| 2040 | Bump the HL7 parser to the patched upstream release | VP-SC-005 | permitted with conditions | bound by precedent | REC-S0038 |  |
| 2041 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 2042 | Pin the radiography panel firmware version in the device inventory | VP-PO-003 | permitted | bound by precedent | REC-VP-A-00091 |  |
| 2043 | Raise the p95 latency budget from ten to twenty-five percent | VP-RB-005 | denied | decided fresh | — |  |
| 2044 | Run semantic analysis over the agent diff in CI | VP-AI-006 | permitted | decided fresh | — |  |
| 2045 | Run semantic analysis over the agent diff in CI | VP-AI-006 | permitted | decided fresh | — |  |
| 2046 | Encrypt the owner address column at rest in the portal store | VP-PD-006 | permitted | decided fresh | — |  |
| 2047 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted | decided fresh | — |  |
| 2048 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-008 | permitted | docketed — not charged | — |  |
| 2049 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 2050 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 |  |
| 2051 | Publish the contest counts in the audit export header | VP-RR-003 | permitted | decided fresh | — |  |
| 2052 | Update the manifest and lockfile in the same commit | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 2053 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-004 | permitted | decided fresh | — |  |
| 2054 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | bound by precedent | REC-S0080 |  |
| 2055 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2056 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 2057 | Widen the deploy freeze exception list in the governance repo | VP-PH-002 | denied | decided fresh | — |  |
| 2058 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | bound by precedent | REC-S0048 |  |
| 2059 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2060 | Run the secret scanner over the diff in pre-merge CI | VP-SC-001 | permitted | decided fresh | — |  |
| 2061 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-001 | denied | bound by precedent | REC-VP-B-00719 |  |
| 2062 | Let clients re-order from prescriptions written last year | VP-CS-006 ⛔ | denied | refused at the floor | — |  |
| 2063 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 2064 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-004 | permitted | decided fresh | — |  |
| 2065 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-010 | permitted with conditions | bound by precedent | REC-VP-C-01222 |  |
| 2066 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-011 | permitted | decided fresh | — |  |
| 2067 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-011 | permitted | decided fresh | — |  |
| 2068 | Add a jurisdiction lookup table that sources the breach-notice clock from statute text | VP-BN-002 | permitted | decided fresh | — |  |
| 2069 | Add the statutory content checklist to the owner breach-notice template | VP-BN-002 | permitted | decided fresh | — |  |
| 2070 | Publish the hotfix image straight from a laptop build | VP-SC-002 | denied | decided fresh | — |  |
| 2071 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01436 |  |
| 2072 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | decided fresh | — |  |
| 2073 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | bound by precedent | REC-VP-B-01500 |  |
| 2074 | Match study patient identity on microchip and account number | VP-PO-004 | permitted with conditions | decided fresh | — | ● |
| 2075 | Pin the radiography panel firmware version in the device inventory | VP-PO-010 | denied | bound by precedent | REC-S0019 |  |
| 2076 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 2077 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 2078 | Write the decision rationale at resolution time, not on export | VP-RR-003 | permitted | decided fresh | — |  |
| 2079 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-004 | permitted with conditions | bound by precedent | REC-VP-G-02074 |  |
| 2080 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-008 | permitted | decided fresh | — |  |
| 2081 | Allowlist microchip identifier formats at the API boundary | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 2082 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-C-01069 | ● |
| 2083 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2084 | Replace the hand-rolled token hash with the vetted library | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 2085 | Derive tenant id from the session, never from a request header | VP-RB-008 | permitted | disposed by citation | — |  |
| 2086 | Bump the HL7 parser to the patched upstream release | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01967 |  |
| 2087 | Skip the consent check for the lapsed-client reactivation text campaign | VP-CC-001 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 2088 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted | bound by precedent | REC-VP-A-00091 |  |
| 2089 | Add a post-install step that pulls the package directly | VP-SC-003 | denied | decided fresh | — |  |
| 2090 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | bound by precedent | REC-VP-L-01559 |  |
| 2091 | Route anomalous dispensing alerts to the medical director's paging channel | VP-DR-004 | permitted | decided fresh | — |  |
| 2092 | Freeze the significant-loss threshold at the DEA's own criteria rather than a local override | VP-DR-004 | permitted | decided fresh | — |  |
| 2093 | Give consent withdrawal the same one-click path as granting it | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 2094 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01478 | ● |
| 2095 | Make the note autosave idempotent under client retry | VP-HA-003 | permitted | decided fresh | — |  |
| 2096 | Block agent branches from touching the compliance test suite | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2097 | Take record timestamps from the monotonic server clock | VP-RR-003 | permitted | decided fresh | — |  |
| 2098 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01576 |  |
| 2099 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2100 | Scope modality worklist queries to the requesting practice | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 2101 | Withhold prescription finalisation from technician accounts | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01961 |  |
| 2102 | Cap analyzer retries at five with exponential backoff | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 2103 | Revalidate the active session after a privilege change | VP-RB-007 | permitted | bound by precedent | REC-VP-A-00080 |  |
| 2104 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | permitted | decided fresh | — |  |
| 2105 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-004 | permitted | decided fresh | — |  |
| 2106 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | bound by precedent | REC-VP-A-00080 |  |
| 2107 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-003 VP-PD-007 ⛔ | denied | refused at the floor | — |  |
| 2108 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-005 | denied | bound by precedent | REC-VP-B-00465 |  |
| 2109 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | decided fresh | — |  |
| 2110 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-B-00420 |  |
| 2111 | Prompt for a pain management plan at surgical discharge | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2112 | Make the feed directive expiry date a mandatory field | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 2113 | Route diversion alerts to the medical director's queue within the hour | VP-CS-011 | denied | bound by precedent | REC-S0005 | ● |
| 2114 | Check object ownership before returning a patient chart | VP-RB-005 | permitted | decided fresh | — |  |
| 2115 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | permitted | decided fresh | — |  |
| 2116 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | decided fresh | — |  |
| 2117 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 2118 | Allowlist microchip identifier formats at the API boundary | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2119 | Restrict claim payload deserialisation to known types | VP-AS-003 | permitted | decided fresh | — | ● |
| 2120 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted | bound by precedent | REC-VP-A-01878 |  |
| 2121 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 2122 | Verify the hash chain when an audit bundle is exported | VP-RR-004 | denied | bound by precedent | REC-VP-C-01103 | ● |
| 2123 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-004 | permitted | decided fresh | — |  |
| 2124 | Add a keyboard path out of the consent modal's focus trap | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01343 |  |
| 2125 | Check object ownership before returning a patient chart | VP-RB-007 | permitted | decided fresh | — |  |
| 2126 | Tokenise the card number before the invoice row is written | VP-PD-008 | permitted | bound by precedent | REC-VP-C-01885 |  |
| 2127 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-004 | denied | decided fresh | — |  |
| 2128 | Check consent currency before the reminder engine sends | VP-PD-003 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 2129 | Disable the biennial inventory job during the systems migration | VP-DR-003 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 2130 | Add an admin path that updates the audit row to fix a typo | VP-RR-006 | denied | decided fresh | — |  |
| 2131 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-001 ⛔ | permitted | decided fresh | — |  |
| 2132 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-001 ⛔ | permitted | decided fresh | — |  |
| 2133 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | disposed by citation | — |  |
| 2134 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | bound by precedent | REC-VP-A-01666 |  |
| 2135 | Record who exported an audit bundle and when | VP-RR-002 | permitted | decided fresh | — |  |
| 2136 | Record who exported an audit bundle and when | VP-RR-002 | permitted | decided fresh | — |  |
| 2137 | Drop internal identifiers from the public error envelope | — | permitted | docketed — nothing engaged | — |  |
| 2138 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted with conditions | bound by precedent | REC-S0043 |  |
| 2139 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 2140 | Publish the contest counts in the audit export header | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 2141 | Encode clinical note text before rendering it in the portal | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2142 | Replace the passive critical-value badge with a required acknowledgement dialog | VP-PS-002 | permitted with conditions | bound by precedent | REC-S0073 |  |
| 2143 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | decided fresh | — |  |
| 2144 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | bound by precedent | REC-VP-B-01399 | ● |
| 2145 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 2146 | Add permutation tests across the role-permission matrix | VP-RB-008 | permitted | disposed by citation | — |  |
| 2147 | Bump the HL7 parser to the patched upstream release | VP-SC-004 | permitted with conditions | bound by precedent | REC-VP-C-01757 |  |
| 2148 | Let Schedule II reorders go through the general purchasing API instead of CSOS | VP-DR-001 VP-PO-010 ⛔ | denied | refused at the floor | — |  |
| 2149 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | bound by precedent | REC-S0080 |  |
| 2150 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted | decided fresh | — |  |
| 2151 | Reuse the stored consent flag without rechecking its date | VP-PD-005 | denied | bound by precedent | REC-VP-B-00110 |  |
| 2152 | Quarantine unmatched analyzer results for technician review | VP-PO-003 | permitted | decided fresh | — |  |
| 2153 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | decided fresh | — |  |
| 2154 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2155 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 2156 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | bound by precedent | REC-VP-A-01758 | ● |
| 2157 | Compute breach scope from the complete access log instead of a sample | VP-BN-003 | permitted | decided fresh | — |  |
| 2158 | Enable the portal's credential-stuffing detector on client login | VP-BN-003 | permitted | decided fresh | — |  |
| 2159 | Bump the HL7 parser to the patched upstream release | VP-SC-007 | permitted | decided fresh | — |  |
| 2160 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-C-02082 |  |
| 2161 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-004 | denied | decided fresh | — |  |
| 2162 | Return a correlation id instead of a stack trace on error | VP-AS-004 | permitted | bound by precedent | REC-VP-C-01707 |  |
| 2163 | Document the degraded path when the reference lab is down | VP-HA-002 | permitted | decided fresh | — |  |
| 2164 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | permitted | bound by precedent | REC-VP-A-01613 |  |
| 2165 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-004 | permitted | decided fresh | — |  |
| 2166 | Prompt for an off-label rationale in the medical record | VP-VC-007 | permitted | bound by precedent | REC-VP-A-00673 |  |
| 2167 | Match study patient identity on microchip and account number | VP-PO-001 ⛔ | permitted | decided fresh | — |  |
| 2168 | Match study patient identity on microchip and account number | VP-PO-001 ⛔ | permitted | decided fresh | — |  |
| 2169 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | denied | bound by precedent | REC-S0013 |  |
| 2170 | Match study patient identity on microchip and account number | VP-PO-008 | permitted | decided fresh | — |  |
| 2171 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00024 |  |
| 2172 | Ship a down-migration for the visit-summary table change | VP-HA-001 | permitted | decided fresh | — |  |
| 2173 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2174 | Keep the retention clock unchanged when a record is edited | VP-RR-005 | denied | bound by precedent | REC-S0057 |  |
| 2175 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-002 | permitted | decided fresh | — |  |
| 2176 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | bound by precedent | REC-VP-A-00175 |  |
| 2177 | Return a correlation id instead of a stack trace on error | VP-AS-003 | permitted | decided fresh | — |  |
| 2178 | Infer the prescriber from the last clinician to open the chart | VP-CS-005 VP-RB-002 ⛔ | denied | refused at the floor | — |  |
| 2179 | Run the secret scanner over the diff in pre-merge CI | VP-SC-001 | permitted | decided fresh | — |  |
| 2180 | Pin the build runner image and make each job ephemeral | VP-SC-001 | permitted | decided fresh | — |  |
| 2181 | Attach the anaesthesia record to the procedure summary | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 2182 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 2183 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted | decided fresh | — | ● |
| 2184 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-002 | denied | decided fresh | — |  |
| 2185 | Verify every imported package resolves in the registry before merge | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 2186 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | bound by precedent | REC-VP-C-01341 |  |
| 2187 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | decided fresh | — |  |
| 2188 | Run semantic analysis over the agent diff in CI | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 | ● |
| 2189 | Drop analyzer messages that fail to parse and move on | VP-PO-009 | denied | decided fresh | — |  |
| 2190 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | bound by precedent | REC-VP-C-01767 |  |
| 2191 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 2192 | Run the secret scanner over the diff in pre-merge CI | VP-SC-009 | permitted | bound by precedent | REC-VP-A-01413 |  |
| 2193 | Add a breach-notice clause to the standard vendor contract template | VP-BN-003 | permitted with conditions | decided fresh | — | ● |
| 2194 | Waive the records-copy fee for a client's own written prescription request | VP-CC-002 | permitted with conditions | bound by precedent | REC-VP-C-02036 |  |
| 2195 | Change the escalation ladder so the third tier is final | VP-RR-002 | denied | decided fresh | — |  |
| 2196 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | bound by precedent | REC-S0028 |  |
| 2197 | Purge Form 222 order records after one year to shrink the archive | VP-DR-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 2198 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | bound by precedent | REC-VP-L-00567 |  |
| 2199 | Parameterise the new chart-search query | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2200 | Pin the radiography panel firmware version in the device inventory | VP-PO-008 | permitted | decided fresh | — |  |
| 2201 | Quarantine unmatched analyzer results for technician review | VP-PO-008 | permitted | decided fresh | — |  |
| 2202 | Verify commit signatures on the protected release branch | VP-SC-004 | permitted | decided fresh | — |  |
| 2203 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | bound by precedent | REC-VP-L-00761 |  |
| 2204 | Encode clinical note text before rendering it in the portal | — | permitted | docketed — nothing engaged | — |  |
| 2205 | Require a saved consent record before the euthanasia workflow can proceed | VP-PS-003 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 2206 | Load the chart straight from the patient id in the query string | VP-RB-003 | denied | decided fresh | — |  |
| 2207 | Version chart amendments instead of editing rows in place | VP-RR-006 | denied | bound by precedent | REC-S0058 |  |
| 2208 | Validate the PDMP payload against the state schema before submit | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 2209 | Add regression tests for the note-render encoding path | VP-AS-002 | permitted | bound by precedent | REC-VP-L-00696 |  |
| 2210 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2211 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-004 | permitted | decided fresh | — |  |
| 2212 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | bound by precedent | REC-VP-C-01818 | ● |
| 2213 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — | ● |
| 2214 | Cover the new boarding endpoint with a role check test | VP-RB-003 | permitted | decided fresh | — |  |
| 2215 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | bound by precedent | REC-VP-B-01500 |  |
| 2216 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-001 ⛔ | permitted | decided fresh | — |  |
| 2217 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-001 ⛔ | permitted | decided fresh | — |  |
| 2218 | Move the authorisation decision out of the portal frontend | VP-RB-008 | permitted | bound by precedent | REC-VP-A-01817 |  |
| 2219 | Withhold prescription finalisation from technician accounts | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 2220 | Make the human review queue reachable from the portal | VP-GV-006 | permitted | bound by precedent | REC-VP-A-01878 |  |
| 2221 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 2222 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 | ● |
| 2223 | Publish the contest counts in the audit export header | VP-RR-004 | permitted | decided fresh | — |  |
| 2224 | Version chart amendments instead of editing rows in place | VP-RR-004 | permitted | decided fresh | — |  |
| 2225 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2226 | Validate the PDMP payload against the state schema before submit | VP-CS-011 | denied | bound by precedent | REC-VP-C-01088 | ● |
| 2227 | Honour opt-out state at export time in the marketing job | VP-PD-006 | permitted | decided fresh | — | ● |
| 2228 | Let staff issue standing scripts without opening the patient record | VP-CS-006 VP-GV-007 ⛔ | denied | refused at the floor | — |  |
| 2229 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | bound by precedent | REC-VP-C-01186 |  |
| 2230 | Record artefact digests in the release ledger on publish | VP-SC-007 | permitted | decided fresh | — |  |
| 2231 | Separate the audit register store from the precedent store | VP-GV-005 | permitted with conditions | bound by precedent | REC-VP-C-01521 |  |
| 2232 | Let staff log a remains custody transfer without scanning the tag | VP-PS-004 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 2233 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | bound by precedent | REC-VP-C-00961 |  |
| 2234 | Ship a down-migration for the visit-summary table change | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2235 | Enforce authorisation server-side on the discharge summary route | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 2236 | Time-box break-glass access to four hours and log the grant | VP-RB-006 | permitted | decided fresh after a tie | none_tie |  |
| 2237 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | permitted | bound by precedent | REC-VP-C-01386 |  |
| 2238 | Pin the radiography panel firmware version in the device inventory | VP-PO-010 | permitted | decided fresh | — |  |
| 2239 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 |  |
| 2240 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 2241 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | bound by precedent | REC-VP-N-00720 |  |
| 2242 | Write the result row first and link the patient in a follow-up job | VP-PO-002 | denied | decided fresh | — |  |
| 2243 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-005 | permitted | decided fresh | — |  |
| 2244 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | bound by precedent | REC-VP-A-00190 |  |
| 2245 | Run the secret scanner over the diff in pre-merge CI | VP-SC-007 | permitted | decided fresh | — |  |
| 2246 | Gate merges on a clean provenance verification step | VP-SC-007 | permitted | decided fresh | — |  |
| 2247 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2248 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted | bound by precedent | REC-VP-A-01878 |  |
| 2249 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 2250 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted | bound by precedent | REC-S0039 |  |
| 2251 | Review agent-authored tests for tautological assertions | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 2252 | Point the resolver at the private registry before the public one | VP-SC-002 | permitted | bound by precedent | REC-VP-A-01292 |  |
| 2253 | Add a concurrency test for simultaneous discharge summary saves | — | permitted | docketed — nothing engaged | — |  |
| 2254 | Extend order-form record retention to cover the full two-year floor | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 | ● |
| 2255 | Propose reclassifying the residency provision as ordinary in policy metadata | VP-SC-008 | denied | decided fresh | — |  |
| 2256 | Add regression tests for the note-render encoding path | VP-AS-001 | denied | bound by precedent | REC-S0049 |  |
| 2257 | Serialise inventory decrements with a row-level lock | VP-HA-002 | permitted | decided fresh | — |  |
| 2258 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | bound by precedent | REC-S0042 |  |
| 2259 | Change the escalation ladder so the third tier is final | VP-PD-005 | denied | decided fresh | — |  |
| 2260 | Bound the results reconciler retry loop | VP-HA-005 | permitted | docketed — not charged | — |  |
| 2261 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 |  |
| 2262 | Encrypt the owner address column at rest in the portal store | VP-PD-002 ⛔ | permitted | decided fresh | — |  |
| 2263 | Give consent withdrawal the same one-click path as granting it | VP-PD-002 ⛔ | permitted | decided fresh | — |  |
| 2264 | Route anomalous dispensing alerts to the medical director's paging channel | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 |  |
| 2265 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 2266 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01197 | ● |
| 2267 | Serialise inventory decrements with a row-level lock | VP-HA-005 | permitted | docketed — not charged | — |  |
| 2268 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-002 | denied | bound by precedent | REC-S0068 |  |
| 2269 | Wire the bulk owner-data export anomaly detector to the on-call paging rotation | VP-BN-003 | permitted | decided fresh | — |  |
| 2270 | Link the incident runbook from every breach-detection alert payload | VP-BN-003 | permitted | decided fresh | — |  |
| 2271 | Encrypt the owner address column at rest in the portal store | VP-PD-009 | permitted | decided fresh | — |  |
| 2272 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted with conditions | bound by precedent | REC-S0035 | ● |
| 2273 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 2274 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | bound by precedent | REC-VP-C-01386 |  |
| 2275 | Block procedure sign-off by roles outside the delegated scope | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 2276 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | bound by precedent | REC-VP-C-01859 |  |
| 2277 | Require the veterinary care plan on the regulated facility record | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2278 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | bound by precedent | REC-S0041 |  |
| 2279 | Bind each service account to a single practice id | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 2280 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 2281 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-006 | denied | decided fresh | — |  |
| 2282 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | disposed by citation | — |  |
| 2283 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 2284 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | decided fresh | — |  |
| 2285 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | bound by precedent | REC-VP-C-01767 |  |
| 2286 | Encrypt the owner address column at rest in the portal store | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 2287 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | decided fresh | — |  |
| 2288 | Bump the HL7 parser to the patched upstream release | VP-SC-002 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 2289 | Match study patient identity on microchip and account number | VP-PO-009 | permitted | decided fresh | — |  |
| 2290 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 2291 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-001 ⛔ | permitted | decided fresh | — |  |
| 2292 | Require a recorded in-person exam date before extralabel orders | VP-VC-001 ⛔ | permitted | decided fresh | — |  |
| 2293 | Separate the audit register store from the precedent store | VP-GV-007 | permitted | bound by precedent | REC-VP-C-01305 |  |
| 2294 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | disposed by citation | — |  |
| 2295 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-004 | permitted | bound by precedent | REC-VP-A-01233 |  |
| 2296 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-002 VP-GV-006 ⛔ | denied | refused at the floor | — |  |
| 2297 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | denied | bound by precedent | REC-VP-C-01088 |  |
| 2298 | Point the resolver at the private registry before the public one | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 2299 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | permitted | bound by precedent | REC-VP-L-02119 | ● |
| 2300 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 2301 | Expose the radiography panel to the internet for vendor support | VP-PO-002 | denied | decided fresh | — |  |
| 2302 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-006 | denied | decided fresh | — |  |
| 2303 | Parameterise the new chart-search query | VP-AS-002 | permitted | bound by precedent | REC-VP-L-00696 |  |
| 2304 | Overwrite the original diagnosis text when a chart is amended | VP-RR-003 | denied | decided fresh | — |  |
| 2305 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-008 | permitted | bound by precedent | REC-S0017 | ● |
| 2306 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-001 | permitted | decided fresh | — |  |
| 2307 | Allowlist microchip identifier formats at the API boundary | VP-AS-002 | permitted | bound by precedent | REC-VP-L-00696 |  |
| 2308 | Show the six-month validity window on the refill request screen | VP-CS-011 | permitted | decided fresh | — |  |
| 2309 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted with conditions | bound by precedent | REC-VP-C-02188 |  |
| 2310 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-002 | permitted | decided fresh | — |  |
| 2311 | Store payment references, not card numbers, on the retry queue | VP-PD-006 | permitted | decided fresh | — |  |
| 2312 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-006 | permitted | decided fresh | — |  |
| 2313 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-004 | permitted | decided fresh | — | ● |
| 2314 | Bind each service account to a single practice id | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01436 |  |
| 2315 | Record the analgesia rationale when a plan is declined | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2316 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00024 |  |
| 2317 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted | decided fresh | — | ● |
| 2318 | Make the withdrawal interval optional on food-animal orders | VP-VC-005 | denied | bound by precedent | REC-VP-B-01256 | ● |
| 2319 | Move the authorisation decision out of the portal frontend | VP-RB-001 ⛔ | permitted | decided fresh | — |  |
| 2320 | Add permutation tests across the role-permission matrix | VP-RB-001 ⛔ | permitted | decided fresh | — |  |
| 2321 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00684 |  |
| 2322 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 2323 | Sanitise filenames in the lab attachment upload handler | VP-AS-003 | permitted | bound by precedent | REC-VP-C-02299 |  |
| 2324 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 2325 | Bind each service account to a single practice id | VP-RB-004 | permitted | bound by precedent | REC-VP-N-01145 |  |
| 2326 | Keep the retention clock unchanged when a record is edited | VP-RR-007 | permitted | decided fresh | — |  |
| 2327 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 2328 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-007 | permitted with conditions | bound by precedent | REC-VP-S-02322 |  |
| 2329 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted | decided fresh | — |  |
| 2330 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | bound by precedent | REC-VP-A-01470 |  |
| 2331 | Encode clinical note text before rendering it in the portal | VP-AS-002 | permitted | decided fresh | — |  |
| 2332 | Check consent currency before the reminder engine sends | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00684 |  |
| 2333 | Extend the log redaction filter to the new owner phone field | VP-PD-008 | permitted | decided fresh | — |  |
| 2334 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted | decided fresh | — |  |
| 2335 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-008 | permitted | decided fresh | — |  |
| 2336 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted | decided fresh | — |  |
| 2337 | Match the required supervision level to the task's risk tier | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2338 | Store payment references, not card numbers, on the retry queue | VP-PD-007 | denied | bound by precedent | REC-VP-C-01742 | ● |
| 2339 | Trust the modality's patient identifier tag exactly as sent | VP-PO-002 | denied | decided fresh | — |  |
| 2340 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted with conditions | bound by precedent | REC-VP-C-02188 |  |
| 2341 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 2342 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted | bound by precedent | REC-VP-N-00089 |  |
| 2343 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 2344 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-008 | permitted | bound by precedent | REC-S0048 |  |
| 2345 | Require a named response before a critical-value alert can be marked acknowledged | VP-PS-004 ⛔ | permitted | decided fresh | — |  |
| 2346 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-004 ⛔ | permitted | decided fresh | — |  |
| 2347 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | bound by precedent | REC-VP-A-01413 |  |
| 2348 | Strip untrusted ticket text from the agent's instruction context | VP-AI-008 | permitted | decided fresh | — |  |
| 2349 | Return a correlation id instead of a stack trace on error | VP-AS-004 | permitted | bound by precedent | REC-VP-C-01707 |  |
| 2350 | Pin the build runner image and make each job ephemeral | VP-SC-009 | permitted | decided fresh | — |  |
| 2351 | Reuse the stored consent flag without rechecking its date | VP-PD-004 | denied | decided fresh | — | ● |
| 2352 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 2353 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 2354 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01091 |  |
| 2355 | Enforce authorisation server-side on the discharge summary route | VP-AS-005 | permitted | decided fresh | — |  |
| 2356 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | denied | bound by precedent | REC-S0034 | ● |
| 2357 | Require a verified adult guardian before a minor's client account can be created | VP-CC-005 | permitted | decided fresh | — |  |
| 2358 | Suppress reminder sends to any number that has already replied STOP | VP-CC-005 | permitted | decided fresh | — |  |
| 2359 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | disposed by citation | — |  |
| 2360 | Encode clinical note text before rendering it in the portal | VP-AS-005 | permitted | bound by precedent | REC-VP-L-00436 |  |
| 2361 | Block record purges that fall inside the two-year retention term | VP-CS-012 | permitted | decided fresh | — | ● |
| 2362 | Block dose calculation until a current weight is recorded for the visit | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01410 |  |
| 2363 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-002 ⛔ | permitted | decided fresh | — |  |
| 2364 | Record the prompt and context hash on the agent's pull request | VP-AI-002 ⛔ | permitted | decided fresh | — |  |
| 2365 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-RB-007 | denied | decided fresh | — |  |
| 2366 | Bind each service account to a single practice id | VP-RB-008 | denied | bound by precedent | REC-VP-C-01920 |  |
| 2367 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-003 | permitted | decided fresh | — |  |
| 2368 | Add captions to the discharge-instructions video on the portal | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-02266 |  |
| 2369 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2370 | Encode clinical note text before rendering it in the portal | VP-AS-003 | permitted | decided fresh after a tie | none_tie |  |
| 2371 | Add an accessible name to the new custom toggle control | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01665 |  |
| 2372 | Validate delegated task lists against the state practice act table | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2373 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | bound by precedent | REC-VP-N-01145 |  |
| 2374 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted with conditions | decided fresh | — | ● |
| 2375 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | denied | bound by precedent | REC-S0057 |  |
| 2376 | Cap analyzer retries at five with exponential backoff | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 2377 | Bound the data subject export job to the statutory window | VP-PD-008 | permitted with conditions | bound by precedent | REC-VP-G-02353 |  |
| 2378 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 2379 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | permitted with conditions | bound by precedent | REC-VP-S-02322 |  |
| 2380 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | decided fresh | — |  |
| 2381 | Record artefact digests in the release ledger on publish | VP-SC-004 | permitted | decided fresh | — |  |
| 2382 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted | decided fresh | — |  |
| 2383 | Hand the checkout redirect to the validated payment processor | VP-PD-008 | permitted | bound by precedent | REC-VP-C-01885 |  |
| 2384 | Bound the data subject export job to the statutory window | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 2385 | Require a second approver on admin role assignments | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 2386 | Wrap result-to-patient binding in a single database transaction | VP-PO-006 | permitted | decided fresh | — |  |
| 2387 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 2388 | Record the prompt and context hash on the agent's pull request | VP-AI-008 | permitted | bound by precedent | REC-S0048 |  |
| 2389 | Call an external summarisation API from the agent's new helper | VP-AI-002 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 2390 | Derive tenant id from the session, never from a request header | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01637 |  |
| 2391 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh | — |  |
| 2392 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-003 | permitted with conditions | bound by precedent | REC-S0076 | ● |
| 2393 | Prompt for a pain management plan at surgical discharge | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2394 | Enforce authorisation server-side on the discharge summary route | VP-AS-005 | permitted | bound by precedent | REC-VP-C-01601 |  |
| 2395 | Suppress reminder sends to any number that has already replied STOP | VP-CC-005 | permitted | decided fresh | — |  |
| 2396 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted | bound by precedent | REC-VP-A-00175 |  |
| 2397 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-002 ⛔ | permitted | decided fresh | — |  |
| 2398 | Flag food-animal status on the patient banner before dispensing | VP-VC-002 ⛔ | permitted | decided fresh | — |  |
| 2399 | Preserve the original entry when a chart amendment is filed | VP-RR-004 | denied | bound by precedent | REC-VP-C-02032 |  |
| 2400 | Record the analgesia rationale when a plan is declined | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2401 | Version the accessibility statement alongside the portal release notes | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01091 |  |
| 2402 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 2403 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted with conditions | bound by precedent | REC-VP-C-02188 |  |
| 2404 | Check object ownership before returning a patient chart | VP-RB-007 | permitted | decided fresh | — |  |
| 2405 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | decided fresh | — |  |
| 2406 | Version chart amendments instead of editing rows in place | VP-RR-007 | permitted | decided fresh | — |  |
| 2407 | Announce form validation errors to assistive technology on submit | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-02266 | ● |
| 2408 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-002 | denied | decided fresh | — |  |
| 2409 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | permitted | decided fresh | — |  |
| 2410 | Reject malformed segments without committing a partial patient write | VP-PO-009 | permitted | decided fresh | — |  |
| 2411 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | bound by precedent | REC-VP-C-01127 |  |
| 2412 | Timestamp records from the workstation clock the client sends | VP-RR-005 | denied | decided fresh | — |  |
| 2413 | Attach build provenance to the practice API release artefact | VP-SC-008 | permitted | bound by precedent | REC-S0041 |  |
| 2414 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted | decided fresh | — |  |
| 2415 | File a draft amendment codifying module-level coverage for generated code | VP-BN-003 | denied | decided fresh | — |  |
| 2416 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01272 |  |
| 2417 | Reuse one integration account across every clinic in the estate | VP-RB-002 | denied | decided fresh | — |  |
| 2418 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-005 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 2419 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 2420 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01397 |  |
| 2421 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2422 | Add an accessibility regression gate to the portal release pipeline | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01665 | ● |
| 2423 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted | decided fresh | — |  |
| 2424 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | decided fresh | — |  |
| 2425 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | decided fresh | — |  |
| 2426 | Make the withdrawal interval optional on food-animal orders | VP-VC-001 ⛔ | denied | refused at the floor | — |  |
| 2427 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01594 |  |
| 2428 | Configure retention periods per jurisdiction in the scheduler | VP-RR-005 | permitted | decided fresh | — |  |
| 2429 | Require a named human reviewer on every agent-authored pull request | VP-AI-001 ⛔ | permitted | decided fresh | — |  |
| 2430 | Verify every imported package resolves in the registry before merge | VP-AI-001 ⛔ | permitted | decided fresh | — |  |
| 2431 | Require a second approver on admin role assignments | VP-RB-003 | permitted | bound by precedent | REC-VP-N-00198 | ● |
| 2432 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-003 | permitted | decided fresh | — |  |
| 2433 | Write the decision rationale at resolution time, not on export | VP-RR-007 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 2434 | Reject malformed segments without committing a partial patient write | VP-PO-002 | permitted | decided fresh | — |  |
| 2435 | Point the resolver at the private registry before the public one | VP-SC-006 | permitted | bound by precedent | REC-S0039 | ● |
| 2436 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 2437 | Prompt for an off-label rationale in the medical record | VP-VC-006 | permitted with conditions | bound by precedent | REC-VP-G-02378 |  |
| 2438 | Restrict claim payload deserialisation to known types | VP-AS-004 | permitted | decided fresh | — |  |
| 2439 | Let the password alone sign an e-prescription when the token times out | VP-CS-006 ⛔ | denied | refused at the floor | — |  |
| 2440 | Quarantine unmatched analyzer results for technician review | VP-PO-010 | denied | bound by precedent | REC-S0019 | ● |
| 2441 | Cap analyzer retries at five with exponential backoff | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 2442 | Add an immutability test for the dispensing log writer | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 2443 | Validate webhook destinations against the outbound allowlist | VP-AS-001 | permitted | bound by precedent | REC-VP-A-01664 |  |
| 2444 | Version chart amendments instead of editing rows in place | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 2445 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted with conditions | bound by precedent | REC-S0067 | ● |
| 2446 | Write the decision rationale at resolution time, not on export | VP-RR-002 | permitted | decided fresh | — |  |
| 2447 | Record who exported an audit bundle and when | VP-RR-002 | permitted | decided fresh | — |  |
| 2448 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2449 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-003 | permitted | bound by precedent | REC-VP-A-01956 |  |
| 2450 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2451 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted | decided fresh | — |  |
| 2452 | Add regression tests for the note-render encoding path | VP-AS-003 | permitted | decided fresh after a tie | none_tie |  |
| 2453 | Make the withdrawal interval optional on food-animal orders | VP-VC-001 VP-RR-007 ⛔ | denied | refused at the floor | — |  |
| 2454 | Withhold prescription finalisation from technician accounts | VP-RB-007 | denied | bound by precedent | REC-S0032 | ● |
| 2455 | Make the note autosave idempotent under client retry | VP-HA-003 | permitted | decided fresh | — |  |
| 2456 | Add an accessibility regression gate to the portal release pipeline | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 2457 | Bump the HL7 parser to the patched upstream release | VP-SC-006 | permitted | decided fresh | — | ● |
| 2458 | Make the consent signature pad completable by keyboard alone | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01091 |  |
| 2459 | Derive tenant id from the session, never from a request header | VP-RB-002 | permitted | decided fresh | — | ● |
| 2460 | Link the breach notification runbook from the incident template | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 2461 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 2462 | Sanitise filenames in the lab attachment upload handler | — | permitted | docketed — nothing engaged | — |  |
| 2463 | Check consent currency before the reminder engine sends | VP-PD-009 | permitted | bound by precedent | REC-VP-C-01859 |  |
| 2464 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-PD-006 ⛔ | denied | refused at the floor | — |  |
| 2465 | Match study patient identity on microchip and account number | VP-PO-002 | permitted | decided fresh | — |  |
| 2466 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-002 | permitted | decided fresh | — |  |
| 2467 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh | — |  |
| 2468 | Validate the PDMP payload against the state schema before submit | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 2469 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | bound by precedent | REC-VP-C-00947 |  |
| 2470 | Parameterise the new chart-search query | VP-AS-001 | permitted | decided fresh | — |  |
| 2471 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted | bound by precedent | REC-VP-L-00475 |  |
| 2472 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 2473 | Deny clinical note writes to the receptionist role | VP-RB-007 | denied | bound by precedent | REC-VP-C-02454 |  |
| 2474 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | permitted | decided fresh | — |  |
| 2475 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 2476 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 2477 | Record who exported an audit bundle and when | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 2478 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-002 | permitted | bound by precedent | REC-VP-C-01705 | ● |
| 2479 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2480 | Drop internal identifiers from the public error envelope | VP-AS-004 | permitted | bound by precedent | REC-VP-C-01707 |  |
| 2481 | Register the new agent runner in the allowlist policy bundle | VP-PD-007 | denied | decided fresh | — |  |
| 2482 | Verify the hash chain when an audit bundle is exported | VP-RR-003 | permitted with conditions | bound by precedent | REC-VP-S-02436 |  |
| 2483 | Make the note autosave idempotent under client retry | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2484 | Remove the extend-session option from the mobile check-in timeout | VP-AX-002 | denied | bound by precedent | REC-VP-B-00603 |  |
| 2485 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | decided fresh | — |  |
| 2486 | Validate webhook destinations against the outbound allowlist | VP-AS-003 | permitted | decided fresh | — |  |
| 2487 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2488 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-008 | permitted | bound by precedent | REC-VP-C-02305 |  |
| 2489 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2490 | Write the decision rationale at resolution time, not on export | VP-RR-003 | permitted with conditions | bound by precedent | REC-S0055 |  |
| 2491 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-001 ⛔ | permitted | decided fresh | — |  |
| 2492 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-001 ⛔ | permitted | decided fresh | — |  |
| 2493 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01410 |  |
| 2494 | Require a recorded in-person exam date before extralabel orders | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 2495 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-002 | permitted | decided fresh | — |  |
| 2496 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | denied | bound by precedent | REC-S0022 | ● |
| 2497 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 2498 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 2499 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | bound by precedent | REC-VP-L-00119 |  |
| 2500 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2501 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-003 | permitted | bound by precedent | REC-VP-N-01272 | ● |
| 2502 | Attach build provenance to the practice API release artefact | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 2503 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2504 | Extend the log redaction filter to the new owner phone field | VP-PD-006 | permitted | decided fresh | — |  |
| 2505 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | bound by precedent | REC-VP-B-01814 |  |
| 2506 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 2507 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01637 |  |
| 2508 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-002 | permitted | decided fresh | — |  |
| 2509 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-002 | permitted | decided fresh | — |  |
| 2510 | Encode clinical note text before rendering it in the portal | VP-AS-008 | permitted | docketed — not charged | — |  |
| 2511 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-010 | permitted | bound by precedent | REC-VP-A-01488 |  |
| 2512 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted | decided fresh | — |  |
| 2513 | Remove the accessibility regression gate from the portal release pipeline | VP-AX-001 | denied | decided fresh | — |  |
| 2514 | Take record timestamps from the monotonic server clock | VP-RR-006 | permitted with conditions | bound by precedent | REC-VP-S-02442 |  |
| 2515 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 2516 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | bound by precedent | REC-VP-C-02094 |  |
| 2517 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-CC-004 ⛔ | denied | refused at the floor | — |  |
| 2518 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted with conditions | bound by precedent | REC-VP-G-02353 |  |
| 2519 | Gate merges on a clean provenance verification step | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 2520 | Hard-stop the dose calculator on a declared weight-unit mismatch | VP-PS-003 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 2521 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | decided fresh | — | ● |
| 2522 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | denied | bound by precedent | REC-VP-C-02226 |  |
| 2523 | Record who exported an audit bundle and when | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 2524 | Run agent-generated code inside the sandboxed runner only | VP-AI-003 | permitted with conditions | bound by precedent | REC-S0043 | ● |
| 2525 | Make the audit table append-only at the database level | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 2526 | Let the client extend the mobile check-in session before it times out | VP-AX-002 | permitted with conditions | bound by precedent | REC-S0079 |  |
| 2527 | Scope modality worklist queries to the requesting practice | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 2528 | Validate species and body weight before computing the dosage | VP-VC-003 ⛔ | permitted | decided fresh | — |  |
| 2529 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-003 ⛔ | permitted | decided fresh | — |  |
| 2530 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 2531 | Record who exported an audit bundle and when | VP-RR-003 | permitted | decided fresh | — |  |
| 2532 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-002 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 2533 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | bound by precedent | REC-VP-N-00486 |  |
| 2534 | Route diversion alerts to the medical director's queue within the hour | VP-CS-010 | permitted | decided fresh | — |  |
| 2535 | Pin the build runner image and make each job ephemeral | VP-SC-005 | permitted with conditions | bound by precedent | REC-VP-C-02014 |  |
| 2536 | Require an explicit share grant for cross-practice referrals | VP-RB-008 | permitted | decided fresh | — |  |
| 2537 | Prompt for an off-label rationale in the medical record | VP-VC-006 | permitted with conditions | bound by precedent | REC-VP-G-02378 |  |
| 2538 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-009 | permitted with conditions | decided fresh | — | ● |
| 2539 | Configure retention periods per jurisdiction in the scheduler | VP-RR-003 | permitted with conditions | bound by precedent | REC-VP-S-02436 |  |
| 2540 | Take record timestamps from the monotonic server clock | VP-RR-004 | permitted | decided fresh | — |  |
| 2541 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | bound by precedent | REC-S0020 |  |
| 2542 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | permitted | decided fresh | — |  |
| 2543 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-003 | permitted with conditions | bound by precedent | REC-VP-G-02374 | ● |
| 2544 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-006 | permitted | decided fresh | — |  |
| 2545 | Hand the checkout redirect to the validated payment processor | VP-PD-007 | permitted with conditions | bound by precedent | REC-VP-C-00955 |  |
| 2546 | Auto-merge agent pull requests once CI is green | VP-AI-002 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 2547 | Block agent branches from touching the compliance test suite | VP-AI-003 | permitted with conditions | bound by precedent | REC-VP-C-02524 |  |
| 2548 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-011 | denied | decided fresh | — |  |
| 2549 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 2550 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-005 | permitted | docketed — not charged | — |  |
| 2551 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | denied | bound by precedent | REC-VP-C-02032 |  |
| 2552 | Cap analyzer retries at five with exponential backoff | VP-PO-005 | permitted | decided fresh | — |  |
| 2553 | Show the premises visit date on the large-animal chart header | VP-VC-007 | permitted with conditions | bound by precedent | REC-VP-G-02498 |  |
| 2554 | Require a named response before a critical-value alert can be marked acknowledged | VP-PS-003 | permitted | decided fresh | — |  |
| 2555 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-003 | permitted | decided fresh | — |  |
| 2556 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | permitted | decided fresh | — |  |
| 2557 | Match study patient identity on microchip and account number | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 2558 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-004 | permitted with conditions | bound by precedent | REC-S0077 | ● |
| 2559 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted | decided fresh | — |  |
| 2560 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-006 | permitted | decided fresh | — | ● |
| 2561 | Revalidate the active session after a privilege change | VP-RB-005 | permitted | bound by precedent | REC-VP-L-01559 |  |
| 2562 | Accept Form 222 line items without matching them against the receiving record | VP-DR-004 | denied | decided fresh | — | ● |
| 2563 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 2564 | Register the new agent runner in the allowlist policy bundle | VP-AI-003 | denied | decided fresh | — |  |
| 2565 | Sanitise filenames in the lab attachment upload handler | VP-AS-005 | permitted | bound by precedent | REC-VP-A-01516 |  |
| 2566 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2567 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-004 | denied | bound by precedent | REC-S0013 |  |
| 2568 | Reuse the stored consent flag without rechecking its date | VP-PD-008 | denied | decided fresh | — | ● |
| 2569 | Deny clinical note writes to the receptionist role | VP-RB-007 | denied | bound by precedent | REC-S0032 |  |
| 2570 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-004 ⛔ | permitted | decided fresh | — |  |
| 2571 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-004 ⛔ | permitted | decided fresh | — |  |
| 2572 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-012 | permitted | bound by precedent | REC-VP-C-01220 |  |
| 2573 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2574 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 2575 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — |  |
| 2576 | Cover the new boarding endpoint with a role check test | VP-RB-003 | permitted | decided fresh | — |  |
| 2577 | Keep sending reminder texts to numbers that already replied STOP | VP-CC-005 | denied | decided fresh | — |  |
| 2578 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-005 | permitted | bound by precedent | REC-S0053 |  |
| 2579 | Attach build provenance to the practice API release artefact | VP-SC-008 | permitted | decided fresh | — |  |
| 2580 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | bound by precedent | REC-VP-L-01322 | ● |
| 2581 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 2582 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-002 | permitted | bound by precedent | REC-VP-A-00458 |  |
| 2583 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2584 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | permitted with conditions | bound by precedent | REC-VP-G-02581 |  |
| 2585 | Drop the runbook link from the detection alert payload to shorten it | VP-BN-002 | denied | decided fresh | — | ● |
| 2586 | Require a phone call to cancel the wellness plan clients enrolled in online | VP-CC-001 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 2587 | Add a keyboard path out of the consent modal's focus trap | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01197 |  |
| 2588 | Quarantine unmatched analyzer results for technician review | VP-PO-010 | permitted | decided fresh | — |  |
| 2589 | Bump the HL7 parser to the patched upstream release | VP-SC-002 | permitted with conditions | bound by precedent | REC-S0035 |  |
| 2590 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 2591 | Extend the log redaction filter to the new owner phone field | VP-PD-009 | permitted | bound by precedent | REC-VP-N-01260 |  |
| 2592 | Require a named response before a critical-value alert can be marked acknowledged | VP-PS-002 | permitted with conditions | decided fresh | — | ● |
| 2593 | Scope the new reporting role to read-only endpoints | VP-RB-008 | denied | bound by precedent | REC-VP-C-01920 |  |
| 2594 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-004 | permitted | decided fresh | — |  |
| 2595 | Wrap result-to-patient binding in a single database transaction | VP-PO-008 | permitted | bound by precedent | REC-S0017 |  |
| 2596 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2597 | Assign the daily audit review to the practice manager role | VP-RR-005 | permitted with conditions | bound by precedent | REC-VP-U-02525 |  |
| 2598 | Quarantine unmatched analyzer results for technician review | VP-PO-009 | permitted | decided fresh | — |  |
| 2599 | Cap analyzer retries at five with exponential backoff | VP-PO-009 | permitted | decided fresh | — |  |
| 2600 | Make the human review queue reachable from the portal | VP-GV-001 ⛔ | permitted | decided fresh | — |  |
| 2601 | Move threshold parameters into the legislated configuration | VP-GV-001 ⛔ | permitted | decided fresh | — |  |
| 2602 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-004 | denied | bound by precedent | REC-S0013 | ● |
| 2603 | Bind each service account to a single practice id | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 2604 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | decided fresh | — |  |
| 2605 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-007 | permitted | bound by precedent | REC-VP-A-00673 |  |
| 2606 | Revalidate the active session after a privilege change | VP-RB-006 | permitted | decided fresh after a tie | none_tie |  |
| 2607 | Link the breach notification runbook from the incident template | VP-PD-003 | permitted | bound by precedent | REC-VP-A-00267 |  |
| 2608 | Queue reminder sends so a retry storm cannot amplify | VP-HA-001 | permitted | decided fresh | — |  |
| 2609 | Configure retention periods per jurisdiction in the scheduler | VP-RR-006 | permitted | decided fresh | — |  |
| 2610 | Move the authorisation decision out of the portal frontend | VP-RB-006 | permitted | bound by precedent | REC-VP-N-01478 |  |
| 2611 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | disposed by citation | — |  |
| 2612 | Revalidate the active session after a privilege change | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 2613 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2614 | Update the manifest and lockfile in the same commit | VP-SC-004 | permitted with conditions | bound by precedent | REC-VP-C-01757 |  |
| 2615 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted | decided fresh | — |  |
| 2616 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-010 | permitted | decided fresh | — |  |
| 2617 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-002 VP-GV-004 ⛔ | denied | refused at the floor | — |  |
| 2618 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | denied | bound by precedent | REC-S0022 |  |
| 2619 | Scope modality worklist queries to the requesting practice | VP-PO-003 | permitted | decided fresh | — |  |
| 2620 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-003 | permitted | decided fresh | — |  |
| 2621 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 2622 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 2623 | Scope the new reporting role to read-only endpoints | VP-RB-007 | denied | bound by precedent | REC-S0032 | ● |
| 2624 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-003 | permitted | decided fresh | — |  |
| 2625 | Revalidate the active session after a privilege change | VP-RB-008 | permitted | disposed by citation | — |  |
| 2626 | Withhold prescription finalisation from technician accounts | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 |  |
| 2627 | Preserve the original entry when a chart amendment is filed | VP-RR-001 ⛔ | permitted | decided fresh | — |  |
| 2628 | Store the amendment author alongside the superseded text | VP-RR-001 ⛔ | permitted | decided fresh | — |  |
| 2629 | Publish the contest counts in the audit export header | VP-RR-004 | permitted | bound by precedent | REC-VP-A-00285 |  |
| 2630 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-003 | permitted with conditions | decided fresh | — | ● |
| 2631 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | bound by precedent | REC-VP-C-01601 |  |
| 2632 | Replace the hand-rolled token hash with the vetted library | VP-AS-008 | permitted | docketed — not charged | — |  |
| 2633 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | denied | bound by precedent | REC-S0057 | ● |
| 2634 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 2635 | Honour opt-out state at export time in the marketing job | VP-PD-006 | permitted | decided fresh | — |  |
| 2636 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-008 | permitted | bound by precedent | REC-VP-N-00850 |  |
| 2637 | Publish the contest outcome as granted and refused counts | VP-GV-003 | permitted | decided fresh | — |  |
| 2638 | Announce form validation errors to assistive technology on submit | VP-AX-002 | permitted | bound by precedent | REC-VP-A-00458 |  |
| 2639 | Let the password alone sign an e-prescription when the token times out | VP-CS-001 VP-CC-003 ⛔ | denied | refused at the floor | — |  |
| 2640 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | bound by precedent | REC-VP-C-01957 |  |
| 2641 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | decided fresh | — |  |
| 2642 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | permitted | decided fresh | — |  |
| 2643 | Attach a residue risk assessment to the food-animal order form | VP-VC-004 | permitted | decided fresh | — |  |
| 2644 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-001 ⛔ | permitted | decided fresh | — |  |
| 2645 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-001 ⛔ | permitted | decided fresh | — |  |
| 2646 | Encode clinical note text before rendering it in the portal | VP-AS-004 | permitted | bound by precedent | REC-VP-C-01707 |  |
| 2647 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2648 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | bound by precedent | REC-VP-B-00910 |  |
| 2649 | Log the acknowledgement disposition on the referral timeline | VP-GV-003 | permitted | decided fresh | — |  |
| 2650 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | bound by precedent | REC-VP-L-02459 |  |
| 2651 | Link the breach notification runbook from the incident template | VP-PD-008 | permitted | decided fresh | — |  |
| 2652 | Run semantic analysis over the agent diff in CI | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2653 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-002 VP-CS-012 ⛔ | denied | refused at the floor | — |  |
| 2654 | Remove the extend-session option from the mobile check-in timeout | VP-AX-002 | denied | bound by precedent | REC-VP-B-00603 |  |
| 2655 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 2656 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | bound by precedent | REC-VP-C-02501 | ● |
| 2657 | Extend the log redaction filter to the new owner phone field | VP-PD-009 | permitted | decided fresh | — |  |
| 2658 | Require an explicit share grant for cross-practice referrals | VP-RB-002 | permitted | bound by precedent | REC-S0027 |  |
| 2659 | Ship the boarding availability endpoint without a role check | VP-RB-002 | denied | decided fresh | — |  |
| 2660 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | permitted | bound by precedent | REC-VP-A-01488 |  |
| 2661 | Remove the written-prescription button from the dispensing screen | VP-CC-002 | denied | decided fresh | — |  |
| 2662 | Require a second approver on admin role assignments | VP-RB-004 | permitted | decided fresh | — |  |
| 2663 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-001 | permitted | decided fresh | — |  |
| 2664 | Add an accessible name to the new custom toggle control | VP-AX-001 | permitted | decided fresh | — |  |
| 2665 | Log the full card number on payment retry to debug declines | VP-PD-001 VP-PO-009 ⛔ | denied | refused at the floor | — |  |
| 2666 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | bound by precedent | REC-VP-B-00721 |  |
| 2667 | Show the technician's credential status on the surgery board | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 2668 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-003 | permitted with conditions | bound by precedent | REC-S0076 |  |
| 2669 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 2670 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-001 ⛔ | permitted | decided fresh | — |  |
| 2671 | Link the breach notification runbook from the incident template | VP-PD-001 ⛔ | permitted | decided fresh | — |  |
| 2672 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted | bound by precedent | REC-VP-A-02361 |  |
| 2673 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-009 | permitted | docketed — not charged | — |  |
| 2674 | Pin the radiography panel firmware version in the device inventory | VP-PO-010 | denied | bound by precedent | REC-VP-C-02440 |  |
| 2675 | Store the amendment author alongside the superseded text | VP-RR-005 | permitted | decided fresh | — |  |
| 2676 | Pin the build runner image and make each job ephemeral | VP-SC-001 | permitted | bound by precedent | REC-VP-L-00181 |  |
| 2677 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | permitted | decided fresh | — |  |
| 2678 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted with conditions | bound by precedent | REC-S0004 | ● |
| 2679 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | decided fresh | — |  |
| 2680 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 2681 | Run semantic analysis over the agent diff in CI | VP-AI-004 | permitted | decided fresh | — |  |
| 2682 | Validate the PDMP payload against the state schema before submit | VP-CS-003 ⛔ | permitted | decided fresh | — |  |
| 2683 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-003 ⛔ | permitted | decided fresh | — |  |
| 2684 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | bound by precedent | REC-VP-B-01814 | ● |
| 2685 | Make the note autosave idempotent under client retry | VP-HA-004 | permitted | docketed — not charged | — |  |
| 2686 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-002 | permitted | bound by precedent | REC-VP-C-02478 |  |
| 2687 | Extend the log redaction filter to the new owner phone field | VP-PD-006 | permitted | decided fresh | — |  |
| 2688 | Encrypt the owner address column at rest in the portal store | VP-PD-006 | permitted | decided fresh | — |  |
| 2689 | Let the signup form create a client account without checking the applicant's age | VP-CC-005 | denied | decided fresh | — |  |
| 2690 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted | bound by precedent | REC-S0003 |  |
| 2691 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2692 | Deny clinical note writes to the receptionist role | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01961 |  |
| 2693 | Hide the contest link when the decision is a denial | VP-GV-001 VP-CS-010 ⛔ | denied | refused at the floor | — |  |
| 2694 | Wrap result-to-patient binding in a single database transaction | VP-PO-009 | permitted with conditions | bound by precedent | REC-VP-G-02538 |  |
| 2695 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | permitted | decided fresh | — | ● |
| 2696 | Update the manifest and lockfile in the same commit | VP-SC-003 | permitted | bound by precedent | REC-S0036 |  |
| 2697 | Version chart amendments instead of editing rows in place | VP-RR-004 | permitted | decided fresh | — |  |
| 2698 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-002 ⛔ | permitted | decided fresh | — |  |
| 2699 | Route diversion alerts to the medical director's queue within the hour | VP-CS-002 ⛔ | permitted | decided fresh | — |  |
| 2700 | Add captions to the discharge-instructions video on the portal | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01259 |  |
| 2701 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 2702 | Serialise inventory decrements with a row-level lock | VP-HA-002 | permitted | decided fresh | — |  |
| 2703 | Release medical records regardless of outstanding balance | VP-CC-005 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 2704 | Write the result row first and link the patient in a follow-up job | VP-PO-001 VP-CC-003 ⛔ | denied | refused at the floor | — |  |
| 2705 | Attach the standing declaration to every audit export | VP-RR-004 | permitted | bound by precedent | REC-VP-A-00285 | ● |
| 2706 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-002 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 2707 | Label agent-authored commits so review routing can see them | VP-AI-006 | denied | bound by precedent | REC-S0046 |  |
| 2708 | Encrypt the owner address column at rest in the portal store | VP-PD-009 | permitted | decided fresh | — |  |
| 2709 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | bound by precedent | REC-VP-B-00619 |  |
| 2710 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | permitted | decided fresh | — |  |
| 2711 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | permitted | decided fresh | — |  |
| 2712 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | decided fresh | — |  |
| 2713 | Swallow PDMP submission errors so checkout never blocks | VP-CS-010 | denied | bound by precedent | REC-VP-B-01819 |  |
| 2714 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted | bound by precedent | REC-S0100 |  |
| 2715 | Check consent currency before the reminder engine sends | VP-PD-009 | permitted | bound by precedent | REC-VP-N-01260 | ● |
| 2716 | Validate webhook destinations against the outbound allowlist | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 2717 | Pin the radiography panel firmware version in the device inventory | VP-PO-002 | permitted with conditions | bound by precedent | REC-VP-C-01037 |  |
| 2718 | Require a tag scan at every remains custody transfer | VP-PS-003 | permitted | decided fresh | — |  |
| 2719 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | bound by precedent | REC-S0015 |  |
| 2720 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 2721 | Make the consent signature pad completable by keyboard alone | VP-AX-001 | permitted | bound by precedent | REC-VP-A-00208 |  |
| 2722 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — |  |
| 2723 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted with conditions | bound by precedent | REC-S0047 |  |
| 2724 | Auto-close ketamine count mismatches under two millilitres | VP-CS-002 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 2725 | Add tests proving retrieval never reads the audit register | VP-GV-004 | permitted with conditions | bound by precedent | REC-S0061 |  |
| 2726 | Add permutation tests across the role-permission matrix | VP-RB-004 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 2727 | Validate webhook destinations against the outbound allowlist | VP-AS-003 | permitted | bound by precedent | REC-VP-C-02299 |  |
| 2728 | Stagger analyzer polling to flatten the morning load peak | VP-HA-001 | permitted | decided fresh | — |  |
| 2729 | Update the manifest and lockfile in the same commit | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 2730 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 2731 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01197 |  |
| 2732 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-003 | permitted | decided fresh | — |  |
| 2733 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | bound by precedent | REC-VP-A-01664 |  |
| 2734 | Cap the records-copy fee at the state's statutory maximum | VP-CC-005 | permitted | decided fresh | — |  |
| 2735 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-005 | permitted | decided fresh | — |  |
| 2736 | Enforce the tenant scope in the query layer, not the handler | VP-RB-003 | permitted | disposed by citation | — |  |
| 2737 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 2738 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | bound by precedent | REC-VP-C-02156 | ● |
| 2739 | Record delivery confirmation before marking a breach notice as sent | VP-BN-001 ⛔ | permitted | decided fresh | — |  |
| 2740 | Compute breach scope from the complete access log instead of a sample | VP-BN-001 ⛔ | permitted | decided fresh | — |  |
| 2741 | Assign a named reviewer to the vendored DICOM parser | VP-SC-009 | permitted with conditions | decided fresh | — | ● |
| 2742 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2743 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted | bound by precedent | REC-VP-C-01077 | ● |
| 2744 | Write the decision rationale at resolution time, not on export | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 2745 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-005 | permitted with conditions | bound by precedent | REC-S0071 |  |
| 2746 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | decided fresh | — |  |
| 2747 | Make the consent signature pad completable by keyboard alone | VP-AX-001 | permitted | bound by precedent | REC-VP-C-01259 |  |
| 2748 | Serialise inventory decrements with a row-level lock | VP-HA-005 | permitted | docketed — not charged | — |  |
| 2749 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-004 | permitted | decided fresh | — |  |
| 2750 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01261 |  |
| 2751 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted | decided fresh | — |  |
| 2752 | Mark required check-in fields with a red border and no error text | VP-AX-001 | denied | decided fresh | — |  |
| 2753 | Block dose calculation until a current weight is recorded for the visit | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01576 |  |
| 2754 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-004 | permitted | decided fresh | — |  |
| 2755 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-004 | permitted | decided fresh | — |  |
| 2756 | Flag food-animal status on the patient banner before dispensing | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 2757 | Add tests proving retrieval never reads the audit register | VP-GV-004 | permitted with conditions | bound by precedent | REC-S0061 | ● |
| 2758 | Gate merges on a clean provenance verification step | VP-SC-005 | permitted | decided fresh | — | ● |
| 2759 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-003 | permitted with conditions | bound by precedent | REC-VP-C-02543 |  |
| 2760 | Give consent withdrawal the same one-click path as granting it | VP-PD-005 | permitted | decided fresh after a tie | none_tie |  |
| 2761 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted | bound by precedent | REC-VP-L-00819 |  |
| 2762 | Switch invoice delivery to email before capturing e-signature consent | VP-CC-001 ⛔ | denied | refused at the floor | — |  |
| 2763 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2764 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-004 | permitted with conditions | bound by precedent | REC-VP-S-02756 |  |
| 2765 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 2766 | Show which record controlled on the decision page | VP-GV-005 | permitted with conditions | bound by precedent | REC-S0062 |  |
| 2767 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 2768 | Bind each service account to a single practice id | VP-RB-007 | denied | bound by precedent | REC-VP-C-02623 | ● |
| 2769 | Update the manifest and lockfile in the same commit | VP-SC-009 | permitted | disposed by citation | — |  |
| 2770 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | permitted | bound by precedent | REC-VP-A-02695 |  |
| 2771 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-002 ⛔ | permitted | decided fresh | — |  |
| 2772 | Run diversion analytics over every dispensing event across all practices | VP-DR-002 ⛔ | permitted | decided fresh | — |  |
| 2773 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-002 | permitted | bound by precedent | REC-S0075 | ● |
| 2774 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | decided fresh | — | ● |
| 2775 | Keep the retention clock unchanged when a record is edited | VP-RR-007 | permitted with conditions | bound by precedent | REC-S0059 |  |
| 2776 | Publish the contest counts in the audit export header | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2777 | Pin the radiography panel firmware version in the device inventory | VP-PO-004 | denied | bound by precedent | REC-VP-C-02602 |  |
| 2778 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted | decided fresh | — |  |
| 2779 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted | decided fresh | — |  |
| 2780 | Assign the daily audit review to the practice manager role | VP-RR-005 | permitted | decided fresh | — | ● |
| 2781 | Bind each service account to a single practice id | VP-RB-007 | denied | bound by precedent | REC-VP-C-02454 |  |
| 2782 | Auto-merge agent pull requests once CI is green | VP-AI-003 | denied | decided fresh | — | ● |
| 2783 | Add an accessible name to the new custom toggle control | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 2784 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-002 | denied | decided fresh | — |  |
| 2785 | Point the resolver at the private registry before the public one | VP-SC-005 | permitted with conditions | bound by precedent | REC-VP-G-02669 |  |
| 2786 | Run the agent on the issue whose body carries its own instructions | VP-AI-003 | denied | decided fresh | — | ● |
| 2787 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-010 | permitted with conditions | bound by precedent | REC-VP-C-01222 |  |
| 2788 | Validate webhook destinations against the outbound allowlist | VP-AS-002 | permitted | disposed by citation | — |  |
| 2789 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-006 | denied | decided fresh | — |  |
| 2790 | Add an accessible name to the new custom toggle control | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 2791 | Attach a residue risk assessment to the food-animal order form | VP-VC-004 | permitted with conditions | bound by precedent | REC-VP-S-02756 |  |
| 2792 | Run diversion analytics over every dispensing event across all practices | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 2793 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | bound by precedent | REC-VP-L-00967 |  |
| 2794 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 2795 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | permitted | bound by precedent | REC-VP-C-02299 |  |
| 2796 | Check the version token on clinical note writes | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2797 | Withhold prescription finalisation from technician accounts | VP-RB-005 | permitted | bound by precedent | REC-VP-L-00869 | ● |
| 2798 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted | decided fresh | — |  |
| 2799 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-008 | permitted | decided fresh | — |  |
| 2800 | Require the veterinary care plan on the regulated facility record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 2801 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | denied | bound by precedent | REC-S0001 |  |
| 2802 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2803 | Separate the audit register store from the precedent store | VP-GV-004 | permitted with conditions | bound by precedent | REC-VP-C-02757 |  |
| 2804 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted | decided fresh | — |  |
| 2805 | Require a verified adult guardian before a minor's client account can be created | VP-CC-006 | permitted | bound by precedent | REC-S0072 |  |
| 2806 | Remove the necessity note from the bulk compounding form | VP-VC-006 | denied | decided fresh | — |  |
| 2807 | Scope the new reporting role to read-only endpoints | VP-RB-008 | denied | bound by precedent | REC-S0033 | ● |
| 2808 | Stagger analyzer polling to flatten the morning load peak | — | permitted | docketed — nothing engaged | — |  |
| 2809 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-005 | permitted | bound by precedent | REC-VP-C-01972 |  |
| 2810 | Block procedure sign-off by roles outside the delegated scope | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2811 | Parameterise the new chart-search query | VP-AS-004 | permitted | bound by precedent | REC-VP-L-01644 |  |
| 2812 | Lower the changed-line coverage threshold in the policy repo | VP-GV-004 | denied | decided fresh | — |  |
| 2813 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted with conditions | bound by precedent | REC-VP-C-02188 |  |
| 2814 | Require a phone call to cancel the wellness plan clients enrolled in online | VP-CC-002 | denied | decided fresh | — | ● |
| 2815 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted | decided fresh | — |  |
| 2816 | Change the escalation ladder so the third tier is final | VP-GV-007 | denied | decided fresh | — |  |
| 2817 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-003 | permitted | bound by precedent | REC-VP-C-02299 |  |
| 2818 | Check object ownership before returning a patient chart | VP-RB-007 | permitted | decided fresh | — |  |
| 2819 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | decided fresh | — |  |
| 2820 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | decided fresh | — |  |
| 2821 | Ship a down-migration for the visit-summary table change | VP-HA-003 | permitted | decided fresh | — |  |
| 2822 | Encode clinical note text before rendering it in the portal | — | permitted | docketed — nothing engaged | — |  |
| 2823 | Expose the contest path to the owner, not only to staff | VP-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2824 | Publish the contest outcome as granted and refused counts | VP-GV-002 ⛔ | permitted | decided fresh | — |  |
| 2825 | Derive tenant id from the session, never from a request header | VP-RB-006 | permitted | bound by precedent | REC-VP-C-02094 |  |
| 2826 | Run the secret scanner over the diff in pre-merge CI | VP-SC-009 | permitted | decided fresh | — |  |
| 2827 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-003 | denied | bound by precedent | REC-VP-B-00063 |  |
| 2828 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2829 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | bound by precedent | REC-VP-C-02144 |  |
| 2830 | Move the authorisation decision out of the portal frontend | VP-RB-006 | permitted | decided fresh | — |  |
| 2831 | Require an explicit share grant for cross-practice referrals | VP-RB-002 | permitted | bound by precedent | REC-VP-C-01961 |  |
| 2832 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted | decided fresh | — | ● |
| 2833 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | bound by precedent | REC-VP-N-00189 |  |
| 2834 | Pin the radiography panel firmware version in the device inventory | VP-PO-005 | permitted with conditions | decided fresh | — | ● |
| 2835 | Add permutation tests across the role-permission matrix | VP-RB-008 | denied | bound by precedent | REC-VP-C-01881 |  |
| 2836 | Point the resolver at the private registry before the public one | VP-SC-001 | permitted | decided fresh | — |  |
| 2837 | Cover the new boarding endpoint with a role check test | VP-RB-005 | permitted | decided fresh | — |  |
| 2838 | Require an explicit owner choice before remains disposition can be saved | VP-PS-003 | permitted with conditions | bound by precedent | REC-VP-C-01410 |  |
| 2839 | Turn off signature enforcement on main to unblock the release train | VP-SC-001 | denied | decided fresh | — |  |
| 2840 | Return a correlation id instead of a stack trace on error | VP-AS-004 | permitted | decided fresh | — |  |
| 2841 | Sanitise filenames in the lab attachment upload handler | VP-AS-004 | permitted | decided fresh | — |  |
| 2842 | Remove the species dose-range override button that predates the current safety gate | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 2843 | Give consent withdrawal the same one-click path as granting it | VP-PD-009 | permitted | decided fresh | — |  |
| 2844 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-002 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 2845 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | bound by precedent | REC-VP-C-02011 |  |
| 2846 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 2847 | Record who exported an audit bundle and when | VP-RR-005 | denied | bound by precedent | REC-S0057 |  |
| 2848 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 2849 | Replace the passive critical-value badge with a required acknowledgement dialog | VP-PS-003 | permitted with conditions | bound by precedent | REC-S0074 |  |
| 2850 | Verify commit signatures on the protected release branch | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 2851 | Assign a named reviewer to the vendored DICOM parser | VP-SC-002 | permitted | bound by precedent | REC-VP-A-01292 |  |
| 2852 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2853 | Return a correlation id instead of a stack trace on error | VP-AS-006 | permitted | docketed — not charged | — |  |
| 2854 | Quarantine unmatched analyzer results for technician review | VP-PO-008 | permitted | bound by precedent | REC-S0017 |  |
| 2855 | Check object ownership before returning a patient chart | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 2856 | Point the resolver at the private registry before the public one | VP-SC-005 | permitted | bound by precedent | REC-VP-L-02758 |  |
| 2857 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted | decided fresh | — |  |
| 2858 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | bound by precedent | REC-VP-L-02459 |  |
| 2859 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | decided fresh | — |  |
| 2860 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted | bound by precedent | REC-VP-A-02361 |  |
| 2861 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted | decided fresh | — |  |
| 2862 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted | decided fresh | — |  |
| 2863 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-004 | permitted | decided fresh | — |  |
| 2864 | Require a second approver on admin role assignments | VP-RB-003 | permitted | bound by precedent | REC-VP-C-02431 | ● |
| 2865 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2866 | Auto-close ketamine count mismatches under two millilitres | VP-CS-003 VP-PO-008 ⛔ | denied | refused at the floor | — |  |
| 2867 | Default the feed directive expiry to blank when it is unknown | VP-VC-006 | denied | bound by precedent | REC-VP-C-01039 |  |
| 2868 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted | decided fresh | — | ● |
| 2869 | Make the withdrawal interval optional on food-animal orders | VP-VC-005 | denied | bound by precedent | REC-VP-B-01256 |  |
| 2870 | Prove the backup restore before the vaccine index migration | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2871 | Route a human review request from the decision detail page | VP-GV-006 | permitted | bound by precedent | REC-VP-A-01878 | ● |
| 2872 | Enforce the tenant scope in the query layer, not the handler | VP-RB-006 | permitted | disposed by citation | — |  |
| 2873 | Take record timestamps from the monotonic server clock | VP-RR-005 | permitted | bound by precedent | REC-VP-A-02780 |  |
| 2874 | Load the chart straight from the patient id in the query string | VP-RB-001 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 2875 | Require an explicit share grant for cross-practice referrals | VP-RB-002 | permitted | bound by precedent | REC-VP-L-02459 |  |
| 2876 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 2877 | Add permutation tests across the role-permission matrix | VP-RB-003 | permitted | bound by precedent | REC-VP-N-00198 |  |
| 2878 | Flag food-animal status on the patient banner before dispensing | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 2879 | Write a docket entry for every uncharged arrival | VP-GV-005 | permitted with conditions | bound by precedent | REC-VP-C-01521 |  |
| 2880 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 2881 | Gate merges on a clean provenance verification step | VP-SC-009 | permitted | bound by precedent | REC-VP-A-01413 |  |
| 2882 | Redact owner email addresses from claims connector debug output | VP-PD-009 | permitted | decided fresh | — |  |
| 2883 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted with conditions | bound by precedent | REC-VP-C-01665 |  |
| 2884 | Update the manifest and lockfile in the same commit | VP-SC-003 | permitted | decided fresh | — |  |
| 2885 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | decided fresh | — |  |
| 2886 | Bind each service account to a single practice id | VP-RB-004 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 2887 | Lower the changed-line coverage threshold in the policy repo | VP-AI-004 | denied | decided fresh | — |  |
| 2888 | Bump the HL7 parser to the patched upstream release | VP-SC-006 | permitted | bound by precedent | REC-VP-A-02457 |  |
| 2889 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-001 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 2890 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted with conditions | bound by precedent | REC-VP-C-02543 |  |
| 2891 | Waive the records-copy fee for a client's own written prescription request | VP-CC-006 | permitted with conditions | decided fresh | — | ● |
| 2892 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | bound by precedent | REC-S0029 |  |
| 2893 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | permitted | decided fresh | — |  |
| 2894 | Verify the hash chain when an audit bundle is exported | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 2895 | Match study patient identity on microchip and account number | VP-PO-008 | permitted | bound by precedent | REC-VP-C-02305 | ● |
| 2896 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-006 | denied | decided fresh | — | ● |
| 2897 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | bound by precedent | REC-VP-C-01929 |  |
| 2898 | Match the required supervision level to the task's risk tier | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 2899 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2900 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | bound by precedent | REC-VP-A-02832 |  |
| 2901 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 2902 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted | decided fresh | — | ● |
| 2903 | Block record purges that fall inside the two-year retention term | VP-CS-011 | permitted | decided fresh | — |  |
| 2904 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-011 | permitted | decided fresh | — |  |
| 2905 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 2906 | Shorten the break-glass expiry constant in the rulebook | VP-SC-002 | denied | decided fresh | — |  |
| 2907 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — |  |
| 2908 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 2909 | Add a campaign endpoint that exports the whole owner list | VP-PD-005 | denied | decided fresh | — |  |
| 2910 | Validate the PDMP payload against the state schema before submit | VP-CS-009 | permitted with conditions | decided fresh | — | ● |
| 2911 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-005 ⛔ | permitted | decided fresh | — |  |
| 2912 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-005 ⛔ | permitted | decided fresh | — |  |
| 2913 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2914 | Enable the refill button on hydromorphone prescriptions | VP-CS-001 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 2915 | Timestamp records from the workstation clock the client sends | VP-RR-002 | denied | decided fresh | — |  |
| 2916 | Store payment references, not card numbers, on the retry queue | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 2917 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-002 | permitted | decided fresh | — | ● |
| 2918 | Match analyzer results on patient name alone | VP-PO-001 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 2919 | Block record purges that fall inside the two-year retention term | VP-CS-012 | permitted | decided fresh | — | ● |
| 2920 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted with conditions | decided fresh | — | ● |
| 2921 | Show the six-month validity window on the refill request screen | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 2922 | Stagger analyzer polling to flatten the morning load peak | VP-HA-003 | permitted | decided fresh | — |  |
| 2923 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-004 | denied | decided fresh | — |  |
| 2924 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-004 | permitted | decided fresh | — |  |
| 2925 | Block payment-plan enrolment from an account without verified adult status | VP-CC-003 | permitted | decided fresh | — |  |
| 2926 | Make the note autosave idempotent under client retry | VP-HA-001 | permitted | decided fresh | — |  |
| 2927 | Make the note autosave idempotent under client retry | VP-HA-003 | permitted | decided fresh | — |  |
| 2928 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | decided fresh | — |  |
| 2929 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — |  |
| 2930 | Require a saved consent record before the euthanasia workflow can proceed | VP-PS-003 | permitted | decided fresh | — |  |
| 2931 | Bump the HL7 parser to the patched upstream release | VP-SC-008 | permitted | decided fresh | — |  |
| 2932 | Require acknowledgement before a critical value page clears | VP-PO-009 | permitted | decided fresh | — |  |
| 2933 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | decided fresh | — | ● |
| 2934 | Show the technician's credential status on the surgery board | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 2935 | Make the note autosave idempotent under client retry | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2936 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-006 ⛔ | permitted | decided fresh | — |  |
| 2937 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-006 ⛔ | permitted | decided fresh | — |  |
| 2938 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-012 | denied | decided fresh | — |  |
| 2939 | Make the feed directive expiry date a mandatory field | VP-VC-005 | permitted | decided fresh | — |  |
| 2940 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-CS-011 ⛔ | denied | refused at the floor | — |  |
| 2941 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 2942 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | decided fresh | — | ● |
| 2943 | Pin the build runner image and make each job ephemeral | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 2944 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | decided fresh | — | ● |
| 2945 | Let the calculator accept twice the labelled equine maximum | VP-VC-003 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 2946 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | decided fresh | — |  |
| 2947 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 2948 | Enable video-only exams for prescribing in every state | VP-VC-004 | denied | decided fresh | — | ● |
| 2949 | Enforce the tenant scope in the query layer, not the handler | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 2950 | Bind each service account to a single practice id | VP-RB-003 | permitted | disposed by citation | — |  |
| 2951 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2952 | Serialise inventory decrements with a row-level lock | VP-HA-005 | permitted | docketed — not charged | — |  |
| 2953 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted | decided fresh | — |  |
| 2954 | Keep the contest link visible on every automated decision notice | VP-GV-006 | permitted | decided fresh | — |  |
| 2955 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2956 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 2957 | Bound the results reconciler retry loop | — | permitted | docketed — nothing engaged | — |  |
| 2958 | Lower the changed-line coverage threshold in the policy repo | VP-PO-004 | denied | decided fresh | — |  |
| 2959 | Estimate breach scope from a ten-percent log sample to finish the report faster | VP-BN-003 | denied | decided fresh | — |  |
| 2960 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-GV-007 ⛔ | denied | refused at the floor | — |  |
| 2961 | Add a same-day alert when a controlled-substance loss crosses the significant-loss criteria | VP-DR-001 ⛔ | permitted | decided fresh | — |  |
| 2962 | Make the loss-discovery timestamp immutable once the theft report is filed | VP-DR-001 ⛔ | permitted | decided fresh | — |  |
| 2963 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 2964 | Hide the contest link when the decision is a denial | VP-GV-001 VP-PD-007 ⛔ | denied | refused at the floor | — |  |
| 2965 | Populate DICOM species and breed tags from the patient record | VP-PO-009 | permitted | decided fresh | — |  |
| 2966 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-001 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 2967 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted | decided fresh | — |  |
| 2968 | Parameterise the new chart-search query | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2969 | Version the accessibility statement alongside the portal release notes | VP-AX-001 | permitted | decided fresh | — |  |
| 2970 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 2971 | Show the premises visit date on the large-animal chart header | VP-VC-007 | permitted | decided fresh | — | ● |
| 2972 | Point the resolver at the private registry before the public one | VP-SC-004 | denied | bound by precedent | REC-S0124 |  |
| 2973 | Move the release outside the emergency-hours freeze window | VP-HA-006 | permitted | docketed — not charged | — |  |
| 2974 | Hide the contest link when the decision is a denial | VP-GV-004 | denied | decided fresh | — |  |
| 2975 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 2976 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-003 | denied | decided fresh | — |  |
| 2977 | Add the transport welfare checklist to the boarding intake form | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 2978 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-009 | permitted | decided fresh | — |  |
| 2979 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 2980 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | decided fresh | — |  |
| 2981 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 2982 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-004 | permitted | disposed by citation | — |  |
| 2983 | Require the individual CSOS certificate on every Schedule II order signature | VP-DR-003 ⛔ | permitted | decided fresh | — |  |
| 2984 | Route every Schedule II reorder through the CSOS certificate signer | VP-DR-003 ⛔ | permitted | decided fresh | — |  |
| 2985 | Shorten the break-glass expiry constant in the rulebook | VP-CS-009 | denied | decided fresh | — |  |
| 2986 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 2987 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 2988 | Deny clinical note writes to the receptionist role | VP-RB-004 | permitted | decided fresh | — |  |
| 2989 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 2990 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-002 | permitted | decided fresh | — |  |
| 2991 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 2992 | Make the loss-discovery timestamp immutable once the theft report is filed | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 2993 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 2994 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 2995 | Record a named owner and outcome on every breach-drill result | VP-BN-002 | permitted | decided fresh | — |  |
| 2996 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-002 VP-VC-004 ⛔ | denied | refused at the floor | — |  |
| 2997 | Link the breach notification runbook from the incident template | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 2998 | Prove the backup restore before the vaccine index migration | — | permitted | docketed — nothing engaged | — |  |
| 2999 | Trim the contest counts from the audit export header | VP-RR-001 VP-CC-003 ⛔ | denied | refused at the floor | — |  |
| 3000 | Write the decision rationale at resolution time, not on export | VP-RR-004 | permitted | decided fresh | — |  |
| 3001 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 3002 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-003 | denied | decided fresh | — |  |
| 3003 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted | decided fresh | — |  |
| 3004 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-007 | permitted | decided fresh | — |  |
| 3005 | Validate webhook destinations against the outbound allowlist | VP-AS-002 | permitted | decided fresh | — | ● |
| 3006 | Keep the contest link visible on every automated decision notice | VP-GV-005 | permitted | decided fresh | — |  |
| 3007 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 3008 | Reject malformed segments without committing a partial patient write | VP-PO-008 | permitted | decided fresh | — |  |
| 3009 | Verify every imported package resolves in the registry before merge | VP-AI-004 | permitted | decided fresh | — |  |
| 3010 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-003 | denied | decided fresh | — |  |
| 3011 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | permitted | disposed by citation | — |  |
| 3012 | Queue reminder sends so a retry storm cannot amplify | VP-HA-001 | permitted | decided fresh | — |  |
| 3013 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-009 | denied | decided fresh | — |  |
| 3014 | Populate DICOM species and breed tags from the patient record | VP-PO-009 | permitted | decided fresh | — |  |
| 3015 | Allow certificate issuance to proceed without checking the signer's licence expiry | VP-PH-004 | denied | decided fresh | — | ● |
| 3016 | Restrict claim payload deserialisation to known types | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3017 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-003 | permitted | decided fresh | — |  |
| 3018 | Add regression tests for the note-render encoding path | VP-AS-005 | permitted | decided fresh | — |  |
| 3019 | Propose reclassifying the residency provision as ordinary in policy metadata | VP-PO-004 | denied | decided fresh | — |  |
| 3020 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 3021 | Version chart amendments instead of editing rows in place | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 3022 | Surface the suspected-abuse report entry on the client-facing portal timeline | VP-PH-002 | denied | decided fresh | — |  |
| 3023 | Return a correlation id instead of a stack trace on error | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 3024 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3025 | Verify commit signatures on the protected release branch | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 3026 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3027 | Update the manifest and lockfile in the same commit | VP-SC-003 | permitted | decided fresh | — |  |
| 3028 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh | — |  |
| 3029 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | permitted | decided fresh | — |  |
| 3030 | Charge a release fee for a written prescription unless the client buys in-house | VP-CC-003 | denied | decided fresh | — |  |
| 3031 | Publish the contest counts in the audit export header | VP-RR-003 | permitted | decided fresh | — |  |
| 3032 | Record artefact digests in the release ledger on publish | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 3033 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-004 | permitted | decided fresh | — |  |
| 3034 | Honour opt-out state at export time in the marketing job | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 3035 | Turn off audit writes on the hot dispensing path | VP-RR-002 | denied | decided fresh | — | ● |
| 3036 | Populate DICOM species and breed tags from the patient record | VP-PO-002 | permitted with conditions | decided fresh | — | ● |
| 3037 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 3038 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 3039 | Change the escalation ladder so the third tier is final | VP-PH-002 | denied | decided fresh | — |  |
| 3040 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 3041 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | decided fresh | — |  |
| 3042 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-AI-008 ⛔ | denied | refused at the floor | — |  |
| 3043 | Require acknowledgement before a critical value page clears | VP-PO-006 | permitted | decided fresh | — |  |
| 3044 | Verify every imported package resolves in the registry before merge | VP-AI-004 | permitted | decided fresh | — | ● |
| 3045 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — | ● |
| 3046 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | disposed by citation | — |  |
| 3047 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-002 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 3048 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted | decided fresh | — |  |
| 3049 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-008 | permitted | decided fresh | — |  |
| 3050 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 3051 | Require a verified adult guardian before a minor's client account can be created | VP-CC-002 | permitted | decided fresh | — |  |
| 3052 | Allowlist microchip identifier formats at the API boundary | VP-AS-003 | permitted | decided fresh | — |  |
| 3053 | Parameterise the new chart-search query | VP-AS-003 | permitted | decided fresh | — |  |
| 3054 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 3055 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted | decided fresh | — |  |
| 3056 | Widen the deploy freeze exception list in the governance repo | VP-AX-002 | denied | decided fresh | — |  |
| 3057 | Add permutation tests across the role-permission matrix | VP-RB-005 | permitted | decided fresh | — | ● |
| 3058 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 3059 | Prove the backup restore before the vaccine index migration | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3060 | Drop analyzer messages that fail to parse and move on | VP-PO-001 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 3061 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | decided fresh | — |  |
| 3062 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | decided fresh | — |  |
| 3063 | Pin the build runner image and make each job ephemeral | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 3064 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3065 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 3066 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 3067 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 3068 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-003 | permitted | decided fresh | — |  |
| 3069 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | decided fresh | — |  |
| 3070 | Widen the deploy freeze exception list in the governance repo | VP-CS-007 | denied | decided fresh | — |  |
| 3071 | Configure a circuit breaker around the external lab client | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3072 | Auto-close ketamine count mismatches under two millilitres | VP-CS-002 VP-PD-006 ⛔ | denied | refused at the floor | — |  |
| 3073 | Take record timestamps from the monotonic server clock | VP-RR-003 | permitted | decided fresh | — |  |
| 3074 | Remove the expiry from break-glass grants so support keeps access | VP-RB-007 | denied | decided fresh | — |  |
| 3075 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 3076 | Require acknowledgement before a critical value page clears | VP-PO-003 | permitted | decided fresh | — |  |
| 3077 | Require a recorded in-person exam date before extralabel orders | VP-VC-005 | permitted | decided fresh | — |  |
| 3078 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-005 | permitted | decided fresh | — |  |
| 3079 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 3080 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 VP-SC-006 ⛔ | denied | refused at the floor | — |  |
| 3081 | Freeze the significant-loss threshold at the DEA's own criteria rather than a local override | VP-DR-004 | permitted | decided fresh | — |  |
| 3082 | Release medical records regardless of outstanding balance | VP-CC-003 | permitted | decided fresh | — |  |
| 3083 | Cap the records-copy fee at the state's statutory maximum | VP-CC-003 | permitted | decided fresh | — |  |
| 3084 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3085 | Add the transport welfare checklist to the boarding intake form | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3086 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 3087 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted with conditions | decided fresh | — | ● |
| 3088 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted | decided fresh | — |  |
| 3089 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-009 | permitted | decided fresh | — | ● |
| 3090 | Stagger analyzer polling to flatten the morning load peak | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3091 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-007 | denied | decided fresh | — |  |
| 3092 | Restrict claim payload deserialisation to known types | — | permitted | docketed — nothing engaged | — |  |
| 3093 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3094 | Restrict claim payload deserialisation to known types | VP-AS-001 | permitted | decided fresh | — |  |
| 3095 | Quarantine unmatched analyzer results for technician review | VP-PO-007 | permitted | decided fresh | — |  |
| 3096 | Quarantine unmatched analyzer results for technician review | VP-PO-007 | permitted | decided fresh | — |  |
| 3097 | Attach the full triage transcript to the patient's medical record | VP-PS-002 | permitted | decided fresh | — |  |
| 3098 | Strip the standing declaration from the audit bundle header | VP-GV-002 VP-RR-003 ⛔ | denied | refused at the floor | — |  |
| 3099 | Document the degraded path when the reference lab is down | VP-HA-001 | permitted | decided fresh | — |  |
| 3100 | Show the technician's credential status on the surgery board | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 3101 | Scope modality worklist queries to the requesting practice | VP-PO-007 | permitted | decided fresh | — |  |
| 3102 | Add a flag that skips the dispensing checks during demos | VP-CS-006 VP-CC-006 ⛔ | denied | refused at the floor | — |  |
| 3103 | Assign a named reviewer to the vendored DICOM parser | VP-SC-009 | permitted | decided fresh | — |  |
| 3104 | Pin the build runner image and make each job ephemeral | VP-SC-009 | permitted | decided fresh | — |  |
| 3105 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3106 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 3107 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 3108 | Write the decision rationale at resolution time, not on export | VP-RR-007 | permitted | decided fresh | — |  |
| 3109 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3110 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-010 | permitted | decided fresh | — |  |
| 3111 | Validate the PDMP payload against the state schema before submit | VP-CS-010 | permitted | decided fresh | — |  |
| 3112 | Let the password alone sign an e-prescription when the token times out | VP-CS-007 | denied | decided fresh | — |  |
| 3113 | Prompt for a pain management plan at surgical discharge | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 3114 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-004 | permitted | decided fresh | — |  |
| 3115 | Scope modality worklist queries to the requesting practice | VP-PO-006 | permitted | decided fresh | — |  |
| 3116 | Return the full exception text in the API error body | VP-AS-004 | denied | decided fresh | — |  |
| 3117 | Link the breach notification runbook from the incident template | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 3118 | Document the degraded path when the reference lab is down | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3119 | Publish the contest counts in the audit export header | VP-RR-006 | permitted | decided fresh | — |  |
| 3120 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-008 | permitted | decided fresh | — |  |
| 3121 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | decided fresh | — |  |
| 3122 | Verify the signer's licence status before a rabies certificate can be issued | VP-PH-002 | permitted | decided fresh | — |  |
| 3123 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 3124 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 3125 | Capture the research protocol number on regulated-facility visits | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3126 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 3127 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh | — |  |
| 3128 | Release medical records regardless of outstanding balance | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 3129 | Verify the hash chain when an audit bundle is exported | VP-RR-003 | permitted | decided fresh | — |  |
| 3130 | Configure retention periods per jurisdiction in the scheduler | VP-RR-003 | permitted | decided fresh | — |  |
| 3131 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — |  |
| 3132 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh | — |  |
| 3133 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | decided fresh | — |  |
| 3134 | Widen the deploy freeze exception list in the governance repo | VP-PS-003 | denied | decided fresh | — |  |
| 3135 | Review agent-authored tests for tautological assertions | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 3136 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-005 | permitted | decided fresh | — |  |
| 3137 | Shorten the break-glass expiry constant in the rulebook | VP-VC-007 | denied | decided fresh | — |  |
| 3138 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-001 | denied | decided fresh | — | ● |
| 3139 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | decided fresh | — |  |
| 3140 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 3141 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | decided fresh | — |  |
| 3142 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3143 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted | disposed by citation | — |  |
| 3144 | Derive tenant id from the session, never from a request header | VP-RB-008 | permitted | decided fresh | — |  |
| 3145 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 3146 | Add a same-day alert when a controlled-substance loss crosses the significant-loss criteria | VP-DR-004 | permitted | decided fresh | — |  |
| 3147 | Run the secret scanner over the diff in pre-merge CI | VP-SC-005 | permitted | decided fresh | — |  |
| 3148 | Bind each service account to a single practice id | VP-RB-008 | permitted | decided fresh | — |  |
| 3149 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 3150 | Extend access-log retention to cover the full notification lookback window | VP-BN-002 | permitted | decided fresh | — | ● |
| 3151 | Bump the HL7 parser to the patched upstream release | VP-SC-003 | permitted | decided fresh | — |  |
| 3152 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 3153 | Replace the species dose-range hard stop with an override button | VP-PS-003 | denied | decided fresh | — |  |
| 3154 | Pin the build runner image and make each job ephemeral | VP-SC-007 | permitted | decided fresh | — |  |
| 3155 | Update the manifest and lockfile in the same commit | VP-SC-007 | permitted | decided fresh | — |  |
| 3156 | Require a recorded in-person exam date before extralabel orders | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 3157 | Cap analyzer retries at five with exponential backoff | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 3158 | Allow extralabel orders for clients with no recorded exam | VP-VC-004 | denied | decided fresh | — |  |
| 3159 | Drop analyzer messages that fail to parse and move on | VP-PO-004 | denied | decided fresh | — | ● |
| 3160 | Update the manifest and lockfile in the same commit | VP-SC-002 | permitted | decided fresh | — |  |
| 3161 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-002 | permitted | decided fresh | — |  |
| 3162 | Hardcode the reference lab API key in the connector config | VP-SC-007 | denied | decided fresh | — |  |
| 3163 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3164 | Purge Form 222 order records after one year to shrink the archive | VP-DR-001 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 3165 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted | decided fresh | — |  |
| 3166 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh | — | ● |
| 3167 | Match study patient identity on microchip and account number | VP-PO-010 | permitted | decided fresh | — |  |
| 3168 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3169 | Waive the records-copy fee for a client's own written prescription request | VP-CC-006 | permitted | decided fresh | — |  |
| 3170 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-006 | permitted | decided fresh | — |  |
| 3171 | Bound the results reconciler retry loop | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3172 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 3173 | Honour opt-out state at export time in the marketing job | VP-PD-006 | permitted | decided fresh | — |  |
| 3174 | Remove the necessity note from the bulk compounding form | VP-VC-007 | denied | decided fresh | — |  |
| 3175 | Let staff reassign a study to another patient in one click | VP-PO-008 | denied | decided fresh | — |  |
| 3176 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | disposed by citation | — |  |
| 3177 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | decided fresh | — |  |
| 3178 | Disable the biennial inventory job during the systems migration | VP-DR-002 VP-PD-006 ⛔ | denied | refused at the floor | — |  |
| 3179 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3180 | Require a verified adult guardian before a minor's client account can be created | VP-CC-003 | permitted | decided fresh | — |  |
| 3181 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-003 | permitted | decided fresh | — |  |
| 3182 | Require a second approver on admin role assignments | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 3183 | Allowlist microchip identifier formats at the API boundary | — | permitted | docketed — nothing engaged | — |  |
| 3184 | Cap the records-copy fee at the state's statutory maximum | VP-CC-005 | permitted | decided fresh | — |  |
| 3185 | Validate webhook destinations against the outbound allowlist | VP-AS-001 | permitted | disposed by citation | — |  |
| 3186 | Drop internal identifiers from the public error envelope | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3187 | Add permutation tests across the role-permission matrix | VP-RB-005 | permitted | decided fresh | — |  |
| 3188 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 3189 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 3190 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-009 | permitted | decided fresh | — |  |
| 3191 | Pin the build runner image and make each job ephemeral | VP-SC-007 | permitted | decided fresh | — | ● |
| 3192 | Queue records-release requests behind the monthly billing run | VP-CC-003 | denied | decided fresh | — |  |
| 3193 | Match analyzer results on patient name alone | VP-PO-001 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 3194 | Sanitise filenames in the lab attachment upload handler | VP-AS-004 | permitted | disposed by citation | — |  |
| 3195 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted | decided fresh | — |  |
| 3196 | Verify commit signatures on the protected release branch | VP-SC-007 | permitted | decided fresh | — | ● |
| 3197 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3198 | Add permutation tests across the role-permission matrix | VP-RB-005 | permitted | decided fresh | — |  |
| 3199 | Move the authorisation decision out of the portal frontend | VP-RB-005 | permitted | decided fresh | — |  |
| 3200 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 3201 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-005 VP-SC-002 ⛔ | denied | refused at the floor | — |  |
| 3202 | Ship a down-migration for the visit-summary table change | VP-HA-002 | permitted | decided fresh | — |  |
| 3203 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | disposed by citation | — |  |
| 3204 | Add permutation tests across the role-permission matrix | VP-RB-005 | permitted | disposed by citation | — |  |
| 3205 | Link the incident runbook from every breach-detection alert payload | VP-BN-002 | permitted with conditions | decided fresh | — | ● |
| 3206 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | permitted | decided fresh | — |  |
| 3207 | Record who exported an audit bundle and when | VP-RR-005 | permitted | decided fresh | — |  |
| 3208 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 3209 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 3210 | Show the six-month validity window on the refill request screen | VP-CS-011 | permitted | decided fresh | — |  |
| 3211 | Move the release outside the emergency-hours freeze window | VP-HA-002 | permitted | decided fresh | — |  |
| 3212 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 3213 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3214 | Parameterise the new chart-search query | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3215 | Put the public registry ahead of the internal one in the resolver | VP-SC-001 | denied | decided fresh | — |  |
| 3216 | Turn off signature enforcement on main to unblock the release train | VP-SC-008 | denied | decided fresh | — |  |
| 3217 | Cap analyzer retries at five with exponential backoff | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 3218 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-003 | permitted | decided fresh | — | ● |
| 3219 | Let one admin grant EPCS signing rights from the user screen | VP-CS-006 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 3220 | Ship a down-migration for the visit-summary table change | VP-HA-003 | permitted | decided fresh | — |  |
| 3221 | Attach the anaesthesia record to the procedure summary | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3222 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — | ● |
| 3223 | Unblock enrofloxacin ordering for dairy herds | VP-VC-004 | denied | decided fresh | — |  |
| 3224 | File a draft amendment codifying module-level coverage for generated code | VP-PD-008 | denied | decided fresh | — |  |
| 3225 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-001 | permitted | decided fresh | — |  |
| 3226 | Honour opt-out state at export time in the marketing job | VP-PD-003 | permitted | decided fresh | — |  |
| 3227 | Add the boarding service to the critical-service list in policy | VP-VC-006 | denied | decided fresh | — |  |
| 3228 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 3229 | Add regression tests for the note-render encoding path | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3230 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | permitted | decided fresh | — |  |
| 3231 | Populate DICOM species and breed tags from the patient record | VP-PO-010 | permitted | decided fresh | — |  |
| 3232 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-005 | permitted | decided fresh | — | ● |
| 3233 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — |  |
| 3234 | Preserve the original entry when a chart amendment is filed | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 3235 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3236 | Enable the portal's credential-stuffing detector on client login | VP-BN-002 | permitted | decided fresh | — |  |
| 3237 | Wire the bulk owner-data export anomaly detector to the on-call paging rotation | VP-BN-002 | permitted | decided fresh | — |  |
| 3238 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 3239 | Require a verified adult guardian before a minor's client account can be created | VP-CC-003 | permitted | decided fresh | — |  |
| 3240 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-003 VP-AI-003 ⛔ | denied | refused at the floor | — |  |
| 3241 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | denied | bound by precedent | REC-S0124 |  |
| 3242 | Verify commit signatures on the protected release branch | VP-SC-004 | permitted | disposed by citation | — |  |
| 3243 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted | decided fresh | — |  |
| 3244 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh | — |  |
| 3245 | Replace the hand-rolled token hash with the vetted library | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3246 | Change the escalation ladder so the third tier is final | VP-AS-001 | denied | decided fresh | — |  |
| 3247 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-006 | permitted | decided fresh | — | ● |
| 3248 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3249 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 3250 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 3251 | Encode clinical note text before rendering it in the portal | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3252 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 3253 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 3254 | Attach the full triage transcript to the patient's medical record | VP-PS-002 | permitted with conditions | decided fresh | — | ● |
| 3255 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-002 | permitted | decided fresh | — |  |
| 3256 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-002 | permitted | decided fresh | — |  |
| 3257 | Match the required supervision level to the task's risk tier | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 3258 | Show a merge dialog instead of overwriting a colleague's note | — | permitted | docketed — nothing engaged | — |  |
| 3259 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-002 | permitted | decided fresh | — |  |
| 3260 | Record who exported an audit bundle and when | VP-RR-005 | permitted | decided fresh | — |  |
| 3261 | Reject malformed segments without committing a partial patient write | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 3262 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted | disposed by citation | — |  |
| 3263 | Pin the build runner image and make each job ephemeral | VP-SC-002 | permitted | decided fresh | — |  |
| 3264 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3265 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3266 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | decided fresh | — |  |
| 3267 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | decided fresh | — |  |
| 3268 | Prove the backup restore before the vaccine index migration | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3269 | Submit an amendment adding a welfare-inspection remediation window | VP-SC-001 | denied | decided fresh | — |  |
| 3270 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 3271 | Validate delegated task lists against the state practice act table | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3272 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3273 | Sanitise filenames in the lab attachment upload handler | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3274 | Replace the hand-rolled token hash with the vetted library | VP-AS-003 | permitted | decided fresh | — |  |
| 3275 | Hide the contest link when the decision is a denial | VP-GV-003 | denied | decided fresh | — |  |
| 3276 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 3277 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3278 | Store payment references, not card numbers, on the retry queue | VP-PD-006 | permitted | decided fresh | — |  |
| 3279 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted | decided fresh | — |  |
| 3280 | Wire the bulk owner-data export anomaly detector to the on-call paging rotation | VP-BN-002 | permitted | decided fresh | — |  |
| 3281 | Record delivery confirmation before marking a breach notice as sent | VP-BN-002 | permitted | decided fresh | — |  |
| 3282 | Add an accessibility regression gate to the portal release pipeline | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 3283 | Take record timestamps from the monotonic server clock | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 3284 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 3285 | Serialise inventory decrements with a row-level lock | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3286 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 3287 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-004 | permitted | decided fresh | — |  |
| 3288 | Record artefact digests in the release ledger on publish | VP-SC-003 | permitted | decided fresh | — |  |
| 3289 | Check the version token on clinical note writes | VP-HA-001 | permitted | decided fresh | — |  |
| 3290 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted | decided fresh | — | ● |
| 3291 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-001 | permitted | decided fresh | — |  |
| 3292 | Wrap result-to-patient binding in a single database transaction | VP-PO-010 | permitted | decided fresh | — |  |
| 3293 | Propose reclassifying the residency provision as ordinary in policy metadata | VP-RR-005 | denied | decided fresh | — |  |
| 3294 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3295 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — |  |
| 3296 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-005 | denied | decided fresh | — | ● |
| 3297 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-003 | permitted | decided fresh | — |  |
| 3298 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-009 | denied | decided fresh | — |  |
| 3299 | Allowlist microchip identifier formats at the API boundary | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3300 | Add a same-day alert when a controlled-substance loss crosses the significant-loss criteria | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 3301 | Ship the consent modal without a keyboard path out of it | VP-AX-002 | denied | decided fresh | — | ● |
| 3302 | Scope the new reporting role to read-only endpoints | VP-RB-007 | permitted | decided fresh | — |  |
| 3303 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | decided fresh | — |  |
| 3304 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted | decided fresh | — |  |
| 3305 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-004 | permitted | decided fresh | — |  |
| 3306 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-004 | permitted | decided fresh | — |  |
| 3307 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 3308 | Raise the p95 latency budget from ten to twenty-five percent | VP-AI-008 | denied | decided fresh | — |  |
| 3309 | Let a technician account sign the rabies certificate when the vet is busy | VP-PH-001 VP-SC-005 ⛔ | denied | refused at the floor | — |  |
| 3310 | Configure a circuit breaker around the external lab client | VP-HA-001 | permitted | decided fresh | — |  |
| 3311 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3312 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 3313 | Restrict claim payload deserialisation to known types | — | permitted | docketed — nothing engaged | — |  |
| 3314 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 3315 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3316 | Load the chart straight from the patient id in the query string | VP-RB-001 VP-PO-005 ⛔ | denied | refused at the floor | — |  |
| 3317 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 3318 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3319 | Move the release outside the emergency-hours freeze window | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3320 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted | decided fresh | — |  |
| 3321 | Encode clinical note text before rendering it in the portal | VP-AS-002 | permitted | disposed by citation | — |  |
| 3322 | Renumber the point-of-care provisions after the device policy merge | VP-PD-007 | denied | decided fresh | — |  |
| 3323 | Require acknowledgement before a critical value page clears | VP-PO-002 | permitted | decided fresh | — |  |
| 3324 | Turn the pound-kilogram mismatch error into a dismissable warning | VP-PS-001 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 3325 | Cap analyzer retries at five with exponential backoff | VP-PO-009 | permitted | decided fresh | — |  |
| 3326 | Fetch whatever callback URL the practice webhook supplies | VP-AS-001 | denied | decided fresh | — |  |
| 3327 | Redact owner email addresses from claims connector debug output | VP-PD-007 | permitted | decided fresh after a tie | none_tie |  |
| 3328 | Label agent-authored commits so review routing can see them | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 3329 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | decided fresh | — |  |
| 3330 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | decided fresh | — |  |
| 3331 | Let the coding agent rewrite the session authentication middleware | VP-AI-004 | denied | decided fresh | — |  |
| 3332 | Document the degraded path when the reference lab is down | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3333 | Extend the log redaction filter to the new owner phone field | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 3334 | Let clients re-order from prescriptions written last year | VP-CS-002 VP-AI-004 ⛔ | denied | refused at the floor | — |  |
| 3335 | Restrict agent outbound calls to the allowlisted host set | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 3336 | Write our own token signing routine to drop the crypto dependency | VP-AS-003 | denied | decided fresh | — |  |
| 3337 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-002 VP-RB-003 ⛔ | denied | refused at the floor | — |  |
| 3338 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 3339 | Configure retention periods per jurisdiction in the scheduler | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 3340 | Suppress the theft-and-loss alert when the missing count is under a configurable threshold | VP-DR-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 3341 | Commit parsed HL7 segments as they arrive instead of at the end | VP-PO-005 | denied | decided fresh | — |  |
| 3342 | Allowlist microchip identifier formats at the API boundary | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 3343 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 3344 | Sign CSOS orders with a shared practice login instead of the individual certificate | VP-DR-004 | denied | decided fresh | — | ● |
| 3345 | Configure retention periods per jurisdiction in the scheduler | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 3346 | Raise the tramadol refill cap to twelve for chronic pain clients | VP-CS-001 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 3347 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — |  |
| 3348 | Scope the new reporting role to read-only endpoints | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 3349 | Restrict claim payload deserialisation to known types | VP-AS-003 | permitted | decided fresh | — | ● |
| 3350 | Prompt for a pain management plan at surgical discharge | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 3351 | Require an explicit share grant for cross-practice referrals | VP-RB-005 | permitted | decided fresh | — |  |
| 3352 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — |  |
| 3353 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 3354 | Make the human review queue reachable from the portal | VP-GV-007 | permitted | decided fresh | — |  |
| 3355 | Keep the contest link visible on every automated decision notice | VP-GV-007 | permitted | decided fresh | — |  |
| 3356 | Derive tenant id from the session, never from a request header | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 3357 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 3358 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 3359 | Block agent branches from touching the compliance test suite | VP-AI-004 | permitted | decided fresh | — |  |
| 3360 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — | ● |
| 3361 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3362 | Unblock enrofloxacin ordering for dairy herds | VP-VC-004 | denied | decided fresh | — |  |
| 3363 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-002 ⛔ | denied | refused at the floor | — |  |
| 3364 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3365 | Block payment-plan enrolment from an account without verified adult status | VP-CC-006 | permitted | decided fresh | — |  |
| 3366 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3367 | Pair the required-field error with visible text, not colour alone | VP-AX-001 | permitted | decided fresh | — |  |
| 3368 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-003 VP-DR-004 ⛔ | denied | refused at the floor | — |  |
| 3369 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-001 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 3370 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted | decided fresh | — |  |
| 3371 | Stagger analyzer polling to flatten the morning load peak | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3372 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | disposed by citation | — |  |
| 3373 | Attach a residue risk assessment to the food-animal order form | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 3374 | Keep the contest link visible on every automated decision notice | VP-GV-005 | permitted | decided fresh | — |  |
| 3375 | Write a docket entry for every uncharged arrival | VP-GV-005 | permitted | decided fresh | — |  |
| 3376 | Require acknowledgement before a critical value page clears | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 3377 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-003 | permitted | decided fresh | — |  |
| 3378 | Add a campaign endpoint that exports the whole owner list | VP-PD-001 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 3379 | Validate the PDMP payload against the state schema before submit | VP-CS-007 | permitted | decided fresh | — |  |
| 3380 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-007 | permitted | decided fresh | — |  |
| 3381 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted | decided fresh | — |  |
| 3382 | Store the amendment author alongside the superseded text | VP-RR-004 | permitted | decided fresh | — |  |
| 3383 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-008 | denied | decided fresh | — |  |
| 3384 | Separate the audit register store from the precedent store | VP-GV-003 | permitted | decided fresh | — |  |
| 3385 | Hardcode the reference lab API key in the connector config | VP-SC-008 | denied | decided fresh | — |  |
| 3386 | Default the feed directive expiry to blank when it is unknown | VP-VC-003 VP-BN-003 ⛔ | denied | refused at the floor | — |  |
| 3387 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-002 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 3388 | Validate the PDMP payload against the state schema before submit | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 3389 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3390 | Register the new agent runner in the allowlist policy bundle | VP-PO-004 | denied | decided fresh | — |  |
| 3391 | Apply the state retention schedule to inactive owner records | VP-PD-004 | permitted | decided fresh | — |  |
| 3392 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | permitted | decided fresh | — |  |
| 3393 | Disable the biennial inventory job during the systems migration | VP-DR-002 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 3394 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | permitted | disposed by citation | — |  |
| 3395 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3396 | Let clients re-order from prescriptions written last year | VP-CS-008 | denied | decided fresh | — | ● |
| 3397 | Remove the segment length cap so long comment fields parse | VP-PO-006 | denied | decided fresh | — |  |
| 3398 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 3399 | Require a second approver on admin role assignments | VP-RB-003 | permitted | decided fresh | — | ● |
| 3400 | Replace the hand-rolled token hash with the vetted library | VP-AS-001 | permitted | decided fresh | — |  |
| 3401 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 3402 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-011 | denied | decided fresh | — |  |
| 3403 | Attach build provenance to the practice API release artefact | VP-SC-006 | permitted with conditions | decided fresh | — | ● |
| 3404 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | permitted | decided fresh | — |  |
| 3405 | Publish the contest counts in the audit export header | VP-RR-004 | permitted | decided fresh | — |  |
| 3406 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-006 | permitted | decided fresh | — |  |
| 3407 | Return a correlation id instead of a stack trace on error | VP-AS-002 | permitted | decided fresh | — |  |
| 3408 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | permitted | decided fresh | — |  |
| 3409 | Validate species and body weight before computing the dosage | VP-VC-004 | permitted | decided fresh | — |  |
| 3410 | Add an admin path that updates the audit row to fix a typo | VP-RR-001 VP-RB-002 ⛔ | denied | refused at the floor | — |  |
| 3411 | Hardcode the reference lab API key in the connector config | VP-SC-003 | denied | decided fresh | — |  |
| 3412 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 3413 | Encode clinical note text before rendering it in the portal | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3414 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 3415 | Release medical records regardless of outstanding balance | VP-CC-005 | permitted | decided fresh | — |  |
| 3416 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 3417 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-007 | denied | decided fresh | — |  |
| 3418 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 ⛔ | denied | refused at the floor | — |  |
| 3419 | Infer the prescriber from the last clinician to open the chart | VP-CS-012 | denied | decided fresh | — | ● |
| 3420 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-001 VP-GV-005 ⛔ | denied | refused at the floor | — |  |
| 3421 | Escalate an unacknowledged critical-value alert to a second on-call contact | VP-PS-003 | permitted | decided fresh | — |  |
| 3422 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-003 | permitted | decided fresh | — |  |
| 3423 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-003 VP-PO-009 ⛔ | denied | refused at the floor | — |  |
| 3424 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3425 | Drop internal identifiers from the public error envelope | VP-AS-001 | permitted | decided fresh | — |  |
| 3426 | Require acknowledgement before a critical value page clears | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 3427 | Populate DICOM species and breed tags from the patient record | VP-PO-009 | permitted | decided fresh | — |  |
| 3428 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 3429 | Let the dose calculator run on last year's recorded weight when today's is missing | VP-PS-004 ⛔ | denied | refused at the floor | — |  |
| 3430 | Add an accessible name to the new custom toggle control | VP-AX-001 | permitted | decided fresh | — |  |
| 3431 | Make the consent signature pad completable by keyboard alone | VP-AX-001 | permitted | decided fresh | — |  |
| 3432 | Validate delegated task lists against the state practice act table | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3433 | Have the agent refactor the controlled dispensing rules engine | VP-AI-005 | denied | decided fresh | — |  |
| 3434 | Require a verified adult guardian before a minor's client account can be created | VP-CC-004 | permitted with conditions | decided fresh | — | ● |
| 3435 | Cover the new boarding endpoint with a role check test | VP-RB-007 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 3436 | Vendor the AGPL HL7 parser into the shipped practice API | VP-SC-001 | denied | decided fresh | — |  |
| 3437 | Trim the contest counts from the audit export header | VP-RR-002 | denied | decided fresh | — |  |
| 3438 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3439 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-SC-003 ⛔ | denied | refused at the floor | — |  |
| 3440 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3441 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 3442 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted | decided fresh | — |  |
| 3443 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | decided fresh | — | ● |
| 3444 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted | decided fresh | — |  |
| 3445 | Default the feed directive expiry to blank when it is unknown | VP-VC-002 VP-SC-002 ⛔ | denied | refused at the floor | — |  |
| 3446 | Encode clinical note text before rendering it in the portal | — | permitted | docketed — nothing engaged | — |  |
| 3447 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | decided fresh | — |  |
| 3448 | Link the breach notification runbook from the incident template | VP-PD-009 | permitted | decided fresh | — |  |
| 3449 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — |  |
| 3450 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-002 | permitted | decided fresh | — |  |
| 3451 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-002 | permitted | decided fresh | — |  |
| 3452 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | decided fresh | — |  |
| 3453 | Match analyzer results on patient name alone | VP-PO-007 | denied | decided fresh | — |  |
| 3454 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3455 | Match study patient identity on microchip and account number | VP-PO-008 | permitted | decided fresh | — |  |
| 3456 | Populate DICOM species and breed tags from the patient record | VP-PO-008 | permitted | decided fresh | — |  |
| 3457 | Record artefact digests in the release ledger on publish | VP-SC-004 | permitted with conditions | decided fresh | — | ● |
| 3458 | Remove the segment length cap so long comment fields parse | VP-PO-005 | denied | decided fresh | — | ● |
| 3459 | Populate DICOM species and breed tags from the patient record | VP-PO-006 | permitted | decided fresh | — |  |
| 3460 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-PS-002 ⛔ | denied | refused at the floor | — |  |
| 3461 | Parameterise the new chart-search query | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 3462 | Prompt for a pain management plan at surgical discharge | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 3463 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 3464 | Point the resolver at the private registry before the public one | VP-SC-006 | permitted | decided fresh | — |  |
| 3465 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-009 | permitted | decided fresh | — |  |
| 3466 | Point the resolver at the private registry before the public one | VP-SC-001 | permitted | decided fresh | — |  |
| 3467 | Verify commit signatures on the protected release branch | VP-SC-001 | permitted | decided fresh | — |  |
| 3468 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-007 | permitted | decided fresh | — |  |
| 3469 | Change the escalation ladder so the third tier is final | VP-CS-008 | denied | decided fresh | — |  |
| 3470 | Queue reminder sends so a retry storm cannot amplify | VP-HA-003 | permitted | decided fresh | — |  |
| 3471 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | decided fresh | — | ● |
| 3472 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3473 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3474 | Add a post-install step that pulls the package directly | VP-SC-004 | denied | decided fresh | — |  |
| 3475 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted | decided fresh | — |  |
| 3476 | Verify commit signatures on the protected release branch | VP-SC-004 | permitted | decided fresh | — |  |
| 3477 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-001 VP-PD-005 ⛔ | denied | refused at the floor | — |  |
| 3478 | Block procedure sign-off by roles outside the delegated scope | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3479 | Batch reportable-disease dispatches into a weekly job to cut API calls | VP-PH-003 | denied | decided fresh | — |  |
| 3480 | Attach the standing declaration to every audit export | VP-RR-004 | permitted | decided fresh | — |  |
| 3481 | Take record timestamps from the monotonic server clock | VP-RR-004 | permitted | decided fresh | — |  |
| 3482 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted | decided fresh | — |  |
| 3483 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | decided fresh | — |  |
| 3484 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-003 | permitted | decided fresh | — |  |
| 3485 | Restore session objects by deserialising the client-supplied blob | VP-AS-002 | denied | decided fresh | — |  |
| 3486 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | decided fresh after a tie | none_tie |  |
| 3487 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted | decided fresh | — |  |
| 3488 | Take record timestamps from the monotonic server clock | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 3489 | Write the result row first and link the patient in a follow-up job | VP-PO-006 | denied | decided fresh | — |  |
| 3490 | Log the acknowledgement disposition on the referral timeline | VP-GV-005 | permitted | decided fresh | — |  |
| 3491 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 3492 | Queue reminder sends so a retry storm cannot amplify | VP-HA-002 | permitted | decided fresh | — |  |
| 3493 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 3494 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-004 | permitted | decided fresh | — |  |
| 3495 | Review agent-authored tests for tautological assertions | VP-AI-004 | permitted | decided fresh | — |  |
| 3496 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-PS-003 ⛔ | denied | refused at the floor | — |  |
| 3497 | Tokenise the card number before the invoice row is written | VP-PD-007 | permitted | decided fresh | — |  |
| 3498 | Bound the results reconciler retry loop | VP-HA-003 | permitted | decided fresh | — |  |
| 3499 | Record the prompt and context hash on the agent's pull request | VP-AI-003 | permitted | decided fresh | — |  |
| 3500 | Strip the standing declaration from the audit bundle header | VP-GV-002 VP-SC-006 ⛔ | denied | refused at the floor | — |  |
| 3501 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3502 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-003 | permitted | decided fresh | — |  |
| 3503 | Allowlist microchip identifier formats at the API boundary | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3504 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3505 | Bind each service account to a single practice id | VP-RB-007 | permitted | disposed by citation | — |  |
| 3506 | Validate species and body weight before computing the dosage | VP-VC-007 | permitted | decided fresh | — |  |
| 3507 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 3508 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 3509 | Let a technician account sign the rabies certificate when the vet is busy | VP-PH-001 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 3510 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 3511 | Track welfare inspection findings to a remediation due date | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3512 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-005 | permitted | decided fresh | — | ● |
| 3513 | Infer the prescriber from the last clinician to open the chart | VP-CS-011 | denied | decided fresh | — |  |
| 3514 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh | — |  |
| 3515 | Propose a sunset clause for the analytics pilot exception | VP-GV-004 | denied | decided fresh | — |  |
| 3516 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-002 | permitted | decided fresh | — |  |
| 3517 | Add a post-install step that pulls the package directly | VP-SC-003 | denied | decided fresh | — | ● |
| 3518 | Honour opt-out state at export time in the marketing job | VP-PD-009 | permitted | decided fresh | — |  |
| 3519 | Match every Form 222 line item against the receiving record before closing the order | VP-DR-004 | permitted | decided fresh | — |  |
| 3520 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 3521 | Attach the standing declaration to every audit export | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 3522 | Sanitise filenames in the lab attachment upload handler | VP-AS-005 | permitted | decided fresh | — |  |
| 3523 | Expose the radiography panel to the internet for vendor support | VP-PO-004 | denied | decided fresh | — |  |
| 3524 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3525 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 3526 | Publish the contest outcome as granted and refused counts | VP-GV-007 | permitted | decided fresh | — |  |
| 3527 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted | decided fresh | — |  |
| 3528 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | disposed by citation | — |  |
| 3529 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | decided fresh | — |  |
| 3530 | Time-box break-glass access to four hours and log the grant | VP-RB-004 | permitted | decided fresh | — |  |
| 3531 | Verify the signer's licence status before a rabies certificate can be issued | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 3532 | Record delivery confirmation before marking a breach notice as sent | VP-BN-003 | permitted | decided fresh | — |  |
| 3533 | Record delivery confirmation before marking a breach notice as sent | VP-BN-003 | permitted | decided fresh | — |  |
| 3534 | Default the feed directive expiry to blank when it is unknown | VP-VC-002 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 3535 | Enforce authorisation server-side on the discharge summary route | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 3536 | Check the version token on clinical note writes | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3537 | Propose a sunset clause for the analytics pilot exception | VP-CC-005 | denied | decided fresh | — |  |
| 3538 | Run the secret scanner over the diff in pre-merge CI | VP-SC-009 | permitted | decided fresh | — |  |
| 3539 | Link the breach notification runbook from the incident template | VP-PD-004 | permitted | decided fresh | — |  |
| 3540 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | decided fresh | — | ● |
| 3541 | Require an explicit share grant for cross-practice referrals | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 3542 | Enforce authorisation server-side on the discharge summary route | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3543 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 3544 | Raise the p95 latency budget from ten to twenty-five percent | VP-CC-004 | denied | decided fresh | — |  |
| 3545 | Reuse one integration account across every clinic in the estate | VP-RB-007 | denied | decided fresh | — |  |
| 3546 | Serialise inventory decrements with a row-level lock | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3547 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3548 | Require an explicit share grant for cross-practice referrals | VP-RB-003 | permitted | disposed by citation | — |  |
| 3549 | Validate webhook destinations against the outbound allowlist | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3550 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3551 | Route a human review request from the decision detail page | VP-GV-005 | permitted | decided fresh | — |  |
| 3552 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-001 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 3553 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 3554 | Sign CSOS orders with a shared practice login instead of the individual certificate | VP-DR-003 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 3555 | Let the password alone sign an e-prescription when the token times out | VP-CS-006 VP-AI-003 ⛔ | denied | refused at the floor | — |  |
| 3556 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 3557 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 3558 | Link the incident runbook from every breach-detection alert payload | VP-BN-003 | permitted with conditions | decided fresh | — | ● |
| 3559 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 3560 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 3561 | Check the version token on clinical note writes | VP-HA-003 | permitted | decided fresh | — |  |
| 3562 | Add an immutability test for the dispensing log writer | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3563 | Stagger analyzer polling to flatten the morning load peak | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3564 | Reuse the stored consent flag without rechecking its date | VP-PD-004 | denied | decided fresh | — |  |
| 3565 | Make the note autosave idempotent under client retry | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3566 | Cap analyzer retries at five with exponential backoff | VP-PO-002 | permitted | decided fresh | — |  |
| 3567 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 3568 | Separate the audit register store from the precedent store | VP-GV-006 | permitted | decided fresh | — |  |
| 3569 | Enforce the tenant scope in the query layer, not the handler | VP-RB-002 | permitted | decided fresh | — |  |
| 3570 | Let the signup form create a client account without checking the applicant's age | VP-CC-005 | denied | decided fresh | — |  |
| 3571 | Write the result row first and link the patient in a follow-up job | VP-PO-006 | denied | decided fresh | — |  |
| 3572 | Replace the passive critical-value badge with a required acknowledgement dialog | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 3573 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 3574 | Honour opt-out state at export time in the marketing job | VP-PD-004 | permitted | decided fresh | — |  |
| 3575 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 VP-CS-007 ⛔ | denied | refused at the floor | — |  |
| 3576 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 3577 | Log the full card number on payment retry to debug declines | VP-PD-009 | denied | decided fresh | — |  |
| 3578 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-002 VP-PO-005 ⛔ | denied | refused at the floor | — |  |
| 3579 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 3580 | Remove the necessity note from the bulk compounding form | VP-VC-003 VP-PS-003 ⛔ | denied | refused at the floor | — |  |
| 3581 | Split the agent-refactored invoicing function to cut its branching | VP-AI-005 | permitted | decided fresh | — |  |
| 3582 | Block agent branches from touching the compliance test suite | VP-AI-005 | permitted | decided fresh | — |  |
| 3583 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3584 | Attach build provenance to the practice API release artefact | VP-SC-007 | permitted | decided fresh | — |  |
| 3585 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | decided fresh | — |  |
| 3586 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-004 | permitted | decided fresh | — |  |
| 3587 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-004 | permitted | decided fresh | — |  |
| 3588 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3589 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | decided fresh | — |  |
| 3590 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 3591 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3592 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted | decided fresh | — | ● |
| 3593 | Make the audit table append-only at the database level | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 3594 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | decided fresh | — |  |
| 3595 | Validate the PDMP payload against the state schema before submit | VP-CS-007 | permitted | decided fresh | — |  |
| 3596 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-002 VP-PD-008 ⛔ | denied | refused at the floor | — |  |
| 3597 | Parameterise the new chart-search query | VP-AS-003 | permitted | decided fresh | — |  |
| 3598 | Restrict agent outbound calls to the allowlisted host set | VP-AI-004 | permitted | decided fresh | — |  |
| 3599 | Reset the retention date whenever a record is edited | VP-RR-001 VP-PO-003 ⛔ | denied | refused at the floor | — |  |
| 3600 | Bind each service account to a single practice id | VP-RB-004 | permitted | decided fresh | — |  |
| 3601 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | decided fresh | — |  |
| 3602 | Add regression tests covering the unit-conversion boundaries in the dose calculator | VP-PS-003 | permitted | decided fresh | — |  |
| 3603 | Remove the species dose-range override button that predates the current safety gate | VP-PS-002 | permitted | decided fresh | — |  |
| 3604 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3605 | Bump the HL7 parser to the patched upstream release | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 3606 | Require a recorded in-person exam date before extralabel orders | VP-VC-005 | permitted | decided fresh | — | ● |
| 3607 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh | — |  |
| 3608 | Extend the log redaction filter to the new owner phone field | VP-PD-008 | permitted | decided fresh | — |  |
| 3609 | Attach build provenance to the practice API release artefact | VP-SC-008 | permitted | decided fresh | — |  |
| 3610 | Point the resolver at the private registry before the public one | VP-SC-008 | permitted | decided fresh | — |  |
| 3611 | Validate the PDMP payload against the state schema before submit | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 3612 | Shorten the vendor breach-notice SLA from five business days to two | VP-BN-002 | permitted | decided fresh | — |  |
| 3613 | Hardcode the reference lab API key in the connector config | VP-SC-008 | denied | decided fresh | — |  |
| 3614 | Enforce the tenant scope in the query layer, not the handler | VP-RB-003 | permitted | disposed by citation | — |  |
| 3615 | Match the required supervision level to the task's risk tier | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3616 | Bound the data subject export job to the statutory window | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 3617 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-005 | permitted | decided fresh | — | ● |
| 3618 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3619 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | disposed by citation | — |  |
| 3620 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted | decided fresh | — |  |
| 3621 | Encode clinical note text before rendering it in the portal | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3622 | Check the version token on clinical note writes | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3623 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3624 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 3625 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-003 | permitted | decided fresh | — |  |
| 3626 | Withhold prescription finalisation from technician accounts | VP-RB-008 | permitted | decided fresh | — |  |
| 3627 | Restrict claim payload deserialisation to known types | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 3628 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-SC-005 | denied | decided fresh | — |  |
| 3629 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | decided fresh | — |  |
| 3630 | Deny clinical note writes to the receptionist role | VP-RB-003 | permitted | decided fresh | — | ● |
| 3631 | Move the CVSS threshold from seven to eight in the dependency policy | VP-SC-002 | denied | decided fresh | — |  |
| 3632 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-002 | permitted with conditions | decided fresh | — | ● |
| 3633 | Deny clinical note writes to the receptionist role | VP-RB-008 | permitted | decided fresh | — |  |
| 3634 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — |  |
| 3635 | Add regression tests covering the unit-conversion boundaries in the dose calculator | VP-PS-002 | permitted | decided fresh | — |  |
| 3636 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-004 | denied | decided fresh | — |  |
| 3637 | Require acknowledgement before a critical value page clears | VP-PO-009 | denied | bound by precedent | REC-S0116 |  |
| 3638 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 3639 | Unblock enrofloxacin ordering for dairy herds | VP-VC-001 ⛔ | denied | refused at the floor | — |  |
| 3640 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-GV-005 ⛔ | denied | refused at the floor | — |  |
| 3641 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 3642 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 3643 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-001 | permitted | disposed by citation | — |  |
| 3644 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh | — |  |
| 3645 | Encode clinical note text before rendering it in the portal | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 3646 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — |  |
| 3647 | Cover the new boarding endpoint with a role check test | VP-RB-004 | permitted | decided fresh | — |  |
| 3648 | Enable the portal's credential-stuffing detector on client login | VP-BN-003 | permitted | decided fresh | — |  |
| 3649 | Tokenise the card number before the invoice row is written | VP-PD-008 | permitted | decided fresh | — |  |
| 3650 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 3651 | Reject malformed segments without committing a partial patient write | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 3652 | Move the release outside the emergency-hours freeze window | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3653 | Attach a residue risk assessment to the food-animal order form | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 3654 | Require a second approver on admin role assignments | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 3655 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 3656 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-003 | denied | decided fresh | — |  |
| 3657 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-002 | permitted | decided fresh | — | ● |
| 3658 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-008 | permitted | decided fresh | — |  |
| 3659 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-008 | permitted | decided fresh | — |  |
| 3660 | Require acknowledgement before a critical value page clears | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 3661 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted | decided fresh after a tie | none_tie |  |
| 3662 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3663 | Swap the date library for a fork published by an unknown account | VP-SC-004 | denied | decided fresh | — |  |
| 3664 | Capture the research protocol number on regulated-facility visits | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 3665 | Show the automated-triage disclosure only on the first message of a session | VP-PS-004 VP-PD-009 ⛔ | denied | refused at the floor | — |  |
| 3666 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 3667 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 3668 | Log the authenticated prescriber id on each dispensing event | VP-CS-008 | permitted | bound by precedent | REC-S0100 |  |
| 3669 | Match study patient identity on microchip and account number | VP-PO-010 | permitted | decided fresh after a tie | none_tie |  |
| 3670 | Run agent-generated code inside the sandboxed runner only | VP-AI-004 | permitted | decided fresh | — |  |
| 3671 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-003 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 3672 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted | decided fresh | — |  |
| 3673 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | decided fresh | — |  |
| 3674 | Lower the changed-line coverage threshold in the policy repo | VP-GV-003 | denied | decided fresh | — |  |
| 3675 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 3676 | Add a keyboard path out of the consent modal's focus trap | VP-AX-002 | permitted | decided fresh | — |  |
| 3677 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | decided fresh | — |  |
| 3678 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted | decided fresh | — |  |
| 3679 | Let the signup form create a client account without checking the applicant's age | VP-CC-001 VP-AS-002 ⛔ | denied | refused at the floor | — |  |
| 3680 | Call an external summarisation API from the agent's new helper | VP-AI-005 | denied | decided fresh | — |  |
| 3681 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 3682 | Disable the biennial inventory job during the systems migration | VP-DR-003 ⛔ | denied | refused at the floor | — |  |
| 3683 | Show which record controlled on the decision page | VP-GV-006 | permitted | decided fresh | — |  |
| 3684 | Separate the audit register store from the precedent store | VP-GV-006 | permitted | decided fresh | — |  |
| 3685 | Point the resolver at the private registry before the public one | VP-SC-007 | permitted | decided fresh | — |  |
| 3686 | Restore session objects by deserialising the client-supplied blob | VP-AS-003 | denied | decided fresh | — |  |
| 3687 | Submit an amendment adding a welfare-inspection remediation window | VP-GV-005 | denied | decided fresh | — |  |
| 3688 | Tokenise the card number before the invoice row is written | VP-PD-008 | permitted | decided fresh | — |  |
| 3689 | Add regression tests for the note-render encoding path | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3690 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | permitted | decided fresh | — |  |
| 3691 | Require acknowledgement before a critical value page clears | VP-PO-002 | permitted | decided fresh | — |  |
| 3692 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 3693 | Version chart amendments instead of editing rows in place | VP-RR-006 | permitted | decided fresh | — |  |
| 3694 | Write the decision rationale at resolution time, not on export | VP-RR-006 | permitted | decided fresh | — |  |
| 3695 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted | decided fresh | — | ● |
| 3696 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | permitted | decided fresh | — |  |
| 3697 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh | — |  |
| 3698 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-012 | permitted | decided fresh | — |  |
| 3699 | Let the password alone sign an e-prescription when the token times out | VP-CS-008 | denied | decided fresh | — |  |
| 3700 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-001 | permitted | decided fresh | — |  |
| 3701 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-006 | permitted | decided fresh | — |  |
| 3702 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-006 | permitted | decided fresh | — |  |
| 3703 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3704 | Submit an amendment adding a welfare-inspection remediation window | VP-PO-008 | denied | decided fresh | — |  |
| 3705 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 3706 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3707 | Encode clinical note text before rendering it in the portal | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3708 | Queue reminder sends so a retry storm cannot amplify | — | permitted | docketed — nothing engaged | — |  |
| 3709 | Write a docket entry for every uncharged arrival | VP-GV-005 | permitted | decided fresh | — |  |
| 3710 | Attribute the standing declaration to the enacting authority | VP-GV-005 | permitted | decided fresh | — |  |
| 3711 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 3712 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 3713 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-003 | denied | decided fresh | — | ● |
| 3714 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3715 | Trim the owner breach-notice template down to a one-line summary | VP-BN-003 | denied | decided fresh | — |  |
| 3716 | Parameterise the new chart-search query | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3717 | Run the agent on the issue whose body carries its own instructions | VP-AI-002 VP-PO-008 ⛔ | denied | refused at the floor | — |  |
| 3718 | Compute breach scope from the complete access log instead of a sample | VP-BN-002 | permitted | decided fresh | — |  |
| 3719 | Store payment references, not card numbers, on the retry queue | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 3720 | Bump the HL7 parser to the patched upstream release | VP-SC-009 | permitted with conditions | decided fresh | — | ● |
| 3721 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3722 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3723 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 3724 | Render the owner's intake note as raw HTML to keep their formatting | VP-AS-005 | denied | decided fresh | — |  |
| 3725 | Restrict claim payload deserialisation to known types | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 3726 | Revalidate the active session after a privilege change | VP-RB-008 | permitted | decided fresh | — | ● |
| 3727 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — |  |
| 3728 | Queue records-release requests behind the monthly billing run | VP-CC-006 | denied | decided fresh | — | ● |
| 3729 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted | decided fresh | — |  |
| 3730 | Move the authorisation decision out of the portal frontend | VP-RB-006 | permitted | disposed by citation | — |  |
| 3731 | Add a support endpoint that dumps the full owner record | VP-PD-002 VP-DR-004 ⛔ | denied | refused at the floor | — |  |
| 3732 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted | decided fresh after a tie | none_tie |  |
| 3733 | Freeze the significant-loss threshold at the DEA's own criteria rather than a local override | VP-DR-004 | permitted | decided fresh | — |  |
| 3734 | Block inventory record submission until a named licensee has signed it | VP-DR-004 | permitted | decided fresh | — |  |
| 3735 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 3736 | Update the manifest and lockfile in the same commit | VP-SC-006 | permitted with conditions | decided fresh | — | ● |
| 3737 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | permitted | decided fresh | — |  |
| 3738 | Tokenise the card number before the invoice row is written | VP-PD-003 | permitted | decided fresh | — | ● |
| 3739 | Add the transport welfare checklist to the boarding intake form | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3740 | Verify commit signatures on the protected release branch | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 3741 | Reuse one integration account across every clinic in the estate | VP-RB-006 | denied | decided fresh | — | ● |
| 3742 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 3743 | Auto-merge agent pull requests once CI is green | VP-AI-002 ⛔ | denied | refused at the floor | — |  |
| 3744 | Tokenise the card number before the invoice row is written | VP-PD-007 | permitted | decided fresh after a tie | none_tie |  |
| 3745 | Require acknowledgement before a critical value page clears | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 3746 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-002 | permitted | decided fresh | — |  |
| 3747 | Escalate an unacknowledged critical-value alert to a second on-call contact | VP-PS-002 | permitted | decided fresh | — |  |
| 3748 | Call an external summarisation API from the agent's new helper | VP-AI-002 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 3749 | Enforce authorisation server-side on the discharge summary route | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 3750 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-005 | permitted | decided fresh | — |  |
| 3751 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — |  |
| 3752 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | decided fresh | — |  |
| 3753 | Move the CVSS threshold from seven to eight in the dependency policy | VP-RB-008 | denied | decided fresh | — |  |
| 3754 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-003 | permitted | decided fresh | — |  |
| 3755 | Scope the new reporting role to read-only endpoints | VP-RB-004 | permitted | disposed by citation | — |  |
| 3756 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | permitted | decided fresh | — |  |
| 3757 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-010 | permitted | decided fresh | — |  |
| 3758 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-005 | permitted | decided fresh | — |  |
| 3759 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-005 | permitted | decided fresh | — |  |
| 3760 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-010 | denied | decided fresh | — |  |
| 3761 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-007 | permitted with conditions | decided fresh | — | ● |
| 3762 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | decided fresh | — |  |
| 3763 | Review agent-authored tests for tautological assertions | VP-AI-006 | permitted | decided fresh | — |  |
| 3764 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3765 | Link the breach notification runbook from the incident template | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 3766 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3767 | Add regression tests for the note-render encoding path | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3768 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted | decided fresh | — | ● |
| 3769 | Add an immutability test for the dispensing log writer | VP-RR-002 | permitted | decided fresh | — |  |
| 3770 | Store the amendment author alongside the superseded text | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3771 | Verify commit signatures on the protected release branch | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 3772 | Link the breach notification runbook from the incident template | VP-PD-007 | permitted | decided fresh | — |  |
| 3773 | Gate merges on a clean provenance verification step | VP-SC-007 | permitted | decided fresh | — | ● |
| 3774 | Sanitise filenames in the lab attachment upload handler | VP-AS-001 | permitted | decided fresh | — |  |
| 3775 | Drop internal identifiers from the public error envelope | — | permitted | docketed — nothing engaged | — |  |
| 3776 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-002 | permitted | decided fresh | — |  |
| 3777 | Separate the audit register store from the precedent store | VP-GV-005 | permitted | decided fresh | — |  |
| 3778 | Route diversion alerts to the medical director's queue within the hour | VP-CS-009 | permitted | decided fresh | — |  |
| 3779 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — |  |
| 3780 | Require a recorded in-person exam date before extralabel orders | VP-VC-007 | permitted | decided fresh | — |  |
| 3781 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3782 | Document the degraded path when the reference lab is down | — | permitted | docketed — nothing engaged | — |  |
| 3783 | Route diversion alerts to the medical director's queue within the hour | VP-CS-012 | permitted | decided fresh | — |  |
| 3784 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted | decided fresh | — |  |
| 3785 | Gate merges on a clean provenance verification step | VP-SC-009 | permitted | decided fresh | — |  |
| 3786 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | decided fresh | — | ● |
| 3787 | Have the agent refactor the controlled dispensing rules engine | VP-AI-001 ⛔ | denied | refused at the floor | — |  |
| 3788 | Assign the daily audit review to the practice manager role | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 3789 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3790 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 3791 | Serialise inventory decrements with a row-level lock | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3792 | Bound the data subject export job to the statutory window | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 3793 | Reset the retention date whenever a record is edited | VP-RR-002 | denied | decided fresh | — |  |
| 3794 | Extend the log redaction filter to the new owner phone field | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 3795 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 3796 | Parameterise the new chart-search query | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3797 | Trust the modality's patient identifier tag exactly as sent | VP-PO-005 | denied | decided fresh | — |  |
| 3798 | Show the six-month validity window on the refill request screen | VP-CS-008 | permitted | decided fresh | — |  |
| 3799 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted | decided fresh | — |  |
| 3800 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 3801 | Move the release outside the emergency-hours freeze window | VP-HA-001 | permitted | decided fresh | — |  |
| 3802 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3803 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 3804 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-005 | permitted | decided fresh | — |  |
| 3805 | Expose the contest path to the owner, not only to staff | VP-GV-007 | permitted | decided fresh | — |  |
| 3806 | Replace the critical value page with a nightly email digest | VP-PO-004 | denied | decided fresh | — |  |
| 3807 | Attach the standing declaration to every audit export | VP-RR-003 | permitted | decided fresh | — |  |
| 3808 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | permitted | decided fresh | — |  |
| 3809 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-007 | permitted | decided fresh | — |  |
| 3810 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 3811 | Make the note autosave idempotent under client retry | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3812 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-007 | denied | bound by precedent | REC-S0126 |  |
| 3813 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 3814 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3815 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-002 | permitted | decided fresh | — | ● |
| 3816 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 3817 | Assign a named reviewer to the vendored DICOM parser | VP-SC-002 | permitted with conditions | decided fresh | — | ● |
| 3818 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 3819 | Split the agent-refactored invoicing function to cut its branching | VP-AI-006 | permitted | decided fresh | — |  |
| 3820 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 3821 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | decided fresh after a tie | none_tie |  |
| 3822 | Swallow PDMP submission errors so checkout never blocks | VP-CS-012 | denied | decided fresh | — | ● |
| 3823 | Require an explicit share grant for cross-practice referrals | VP-RB-002 | permitted | decided fresh | — |  |
| 3824 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-SC-005 ⛔ | denied | refused at the floor | — |  |
| 3825 | Tokenise the card number before the invoice row is written | VP-PD-004 | permitted | decided fresh | — |  |
| 3826 | Prompt for an off-label rationale in the medical record | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 3827 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 3828 | Scope modality worklist queries to the requesting practice | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 3829 | Quarantine unmatched analyzer results for technician review | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 3830 | Scope modality worklist queries to the requesting practice | VP-PO-005 | permitted | decided fresh | — |  |
| 3831 | Pin the radiography panel firmware version in the device inventory | VP-PO-005 | permitted | decided fresh | — |  |
| 3832 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 3833 | Cover the new boarding endpoint with a role check test | VP-RB-005 | permitted | decided fresh | — |  |
| 3834 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — |  |
| 3835 | Run the secret scanner over the diff in pre-merge CI | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 3836 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-004 | denied | decided fresh | — |  |
| 3837 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-001 VP-PD-004 ⛔ | denied | refused at the floor | — |  |
| 3838 | Encode clinical note text before rendering it in the portal | VP-AS-002 | permitted | decided fresh | — |  |
| 3839 | Auto-merge agent pull requests once CI is green | VP-AI-003 | denied | decided fresh | — |  |
| 3840 | Remove the expiry from break-glass grants so support keeps access | VP-RB-005 | denied | decided fresh | — |  |
| 3841 | Drop internal identifiers from the public error envelope | VP-AS-003 | permitted | disposed by citation | — |  |
| 3842 | Assign the daily audit review to the practice manager role | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3843 | Move the authorisation decision out of the portal frontend | VP-RB-005 | permitted | disposed by citation | — |  |
| 3844 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | permitted | decided fresh | — |  |
| 3845 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted | decided fresh | — |  |
| 3846 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3847 | Make the note autosave idempotent under client retry | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3848 | Quarantine unmatched analyzer results for technician review | VP-PO-003 | permitted | decided fresh | — |  |
| 3849 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3850 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 3851 | Require the veterinary care plan on the regulated facility record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3852 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 3853 | Enable the refill button on hydromorphone prescriptions | VP-CS-001 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 3854 | Run the secret scanner over the diff in pre-merge CI | VP-SC-007 | permitted | decided fresh | — | ● |
| 3855 | Point the resolver at the private registry before the public one | VP-SC-001 | permitted | decided fresh | — |  |
| 3856 | Add the new charting library licence to the allowlist | VP-SC-009 | permitted | decided fresh | — | ● |
| 3857 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 3858 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 3859 | Add the new charting library licence to the allowlist | VP-SC-001 | permitted | disposed by citation | — |  |
| 3860 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted | decided fresh | — |  |
| 3861 | Trim the contest counts from the audit export header | VP-RR-001 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 3862 | Block agent branches from touching the compliance test suite | VP-AI-003 | permitted | decided fresh | — |  |
| 3863 | Cap the records-copy fee at the state's statutory maximum | VP-CC-002 | permitted | decided fresh | — |  |
| 3864 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-002 | permitted | decided fresh | — |  |
| 3865 | Let one admin grant EPCS signing rights from the user screen | VP-CS-004 ⛔ | denied | refused at the floor | — |  |
| 3866 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-008 | permitted | decided fresh | — |  |
| 3867 | Load the chart straight from the patient id in the query string | VP-RB-001 VP-PD-003 ⛔ | denied | refused at the floor | — |  |
| 3868 | Hardcode the reference lab API key in the connector config | VP-SC-004 | denied | decided fresh | — |  |
| 3869 | Remove the two-person rule for EPCS grants from the policy repo | VP-PS-003 | denied | decided fresh | — |  |
| 3870 | Drop the practice filter from the referral search endpoint | VP-RB-001 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 3871 | Add a post-install step that pulls the package directly | VP-SC-007 | denied | decided fresh | — |  |
| 3872 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-008 | denied | decided fresh | — |  |
| 3873 | Let staff issue standing scripts without opening the patient record | VP-CS-012 | denied | decided fresh | — |  |
| 3874 | Configure retention periods per jurisdiction in the scheduler | VP-RR-007 | permitted | decided fresh | — |  |
| 3875 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-008 | permitted | decided fresh after a tie | none_tie |  |
| 3876 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | disposed by citation | — |  |
| 3877 | Replace the critical value page with a nightly email digest | VP-PO-003 | denied | decided fresh | — |  |
| 3878 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 3879 | Drop analyzer messages that fail to parse and move on | VP-PO-005 | denied | decided fresh | — |  |
| 3880 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 3881 | Gate merges on a clean provenance verification step | VP-SC-001 | permitted | decided fresh | — |  |
| 3882 | Match study patient identity on microchip and account number | VP-PO-009 | permitted | decided fresh | — |  |
| 3883 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 3884 | Verify commit signatures on the protected release branch | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 3885 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3886 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-001 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 3887 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 3888 | Encrypt the owner address column at rest in the portal store | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 3889 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted | disposed by citation | — |  |
| 3890 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3891 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted | decided fresh | — |  |
| 3892 | Return a correlation id instead of a stack trace on error | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 3893 | Bound the results reconciler retry loop | VP-HA-005 | permitted | docketed — not charged | — |  |
| 3894 | Attach the anaesthesia record to the procedure summary | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 3895 | Strip the standing declaration from the audit bundle header | VP-GV-006 | denied | decided fresh | — |  |
| 3896 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 3897 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-004 | permitted | decided fresh | — |  |
| 3898 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 3899 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted | decided fresh | — |  |
| 3900 | Write the decision rationale at resolution time, not on export | VP-RR-003 | permitted | decided fresh | — |  |
| 3901 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | decided fresh | — |  |
| 3902 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-003 | permitted | decided fresh | — | ● |
| 3903 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-003 | permitted | decided fresh | — |  |
| 3904 | Allowlist microchip identifier formats at the API boundary | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3905 | Attach the standing declaration to every audit export | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3906 | Write the decision rationale at resolution time, not on export | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3907 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-006 | permitted | decided fresh | — |  |
| 3908 | Require a recorded in-person exam date before extralabel orders | VP-VC-006 | permitted | decided fresh | — |  |
| 3909 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 3910 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | decided fresh | — |  |
| 3911 | Reuse the stored consent flag without rechecking its date | VP-PD-004 | denied | decided fresh | — |  |
| 3912 | Version chart amendments instead of editing rows in place | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 3913 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted with conditions | decided fresh | — | ● |
| 3914 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh | — | ● |
| 3915 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 3916 | Verify commit signatures on the protected release branch | VP-SC-009 | permitted | decided fresh | — |  |
| 3917 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 3918 | Configure a circuit breaker around the external lab client | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3919 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-004 | permitted | decided fresh | — |  |
| 3920 | Validate delegated task lists against the state practice act table | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 3921 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-004 | denied | decided fresh | — | ● |
| 3922 | Let the calculator accept twice the labelled equine maximum | VP-VC-004 | denied | decided fresh | — | ● |
| 3923 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-006 | denied | decided fresh | — |  |
| 3924 | Pin the radiography panel firmware version in the device inventory | VP-PO-007 | permitted | decided fresh | — |  |
| 3925 | Time-box break-glass access to four hours and log the grant | VP-RB-004 | permitted | decided fresh | — | ● |
| 3926 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | permitted | decided fresh | — |  |
| 3927 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted | decided fresh | — |  |
| 3928 | Scope modality worklist queries to the requesting practice | VP-PO-007 | permitted | decided fresh | — |  |
| 3929 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-001 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 3930 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3931 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 3932 | Require a verified adult guardian before a minor's client account can be created | VP-CC-006 | permitted | decided fresh | — |  |
| 3933 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-006 | permitted | decided fresh | — |  |
| 3934 | Redact owner email addresses from claims connector debug output | VP-PD-004 | permitted | decided fresh | — |  |
| 3935 | Hide the contest link when the decision is a denial | VP-GV-003 | denied | decided fresh | — |  |
| 3936 | Block record purges that fall inside the two-year retention term | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 3937 | Cap analyzer retries at five with exponential backoff | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 3938 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted | decided fresh | — |  |
| 3939 | Require acknowledgement before a critical value page clears | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 3940 | Move the release outside the emergency-hours freeze window | VP-HA-006 | permitted | docketed — not charged | — |  |
| 3941 | Commit parsed HL7 segments as they arrive instead of at the end | VP-PO-007 | denied | decided fresh | — |  |
| 3942 | Take record timestamps from the monotonic server clock | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 3943 | Keep the retention clock unchanged when a record is edited | VP-RR-005 | permitted | decided fresh | — |  |
| 3944 | Move threshold parameters into the legislated configuration | VP-GV-004 | permitted | decided fresh | — |  |
| 3945 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3946 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 3947 | Validate webhook destinations against the outbound allowlist | VP-AS-001 | permitted | decided fresh | — |  |
| 3948 | Serialise inventory decrements with a row-level lock | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3949 | Tokenise the card number before the invoice row is written | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 3950 | Drop internal identifiers from the public error envelope | VP-AS-006 | permitted | docketed — not charged | — |  |
| 3951 | Make the human review queue reachable from the portal | VP-GV-006 | permitted | decided fresh | — | ● |
| 3952 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-AS-005 | denied | decided fresh | — |  |
| 3953 | Match study patient identity on microchip and account number | VP-PO-008 | permitted | decided fresh | — |  |
| 3954 | Require acknowledgement before a critical value page clears | VP-PO-008 | permitted | decided fresh | — |  |
| 3955 | Let the coding agent rewrite the session authentication middleware | VP-AI-001 VP-CC-005 ⛔ | denied | refused at the floor | — |  |
| 3956 | Run the secret scanner over the diff in pre-merge CI | VP-SC-002 | permitted | decided fresh | — | ● |
| 3957 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-009 | permitted | decided fresh | — |  |
| 3958 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-009 | permitted | decided fresh | — |  |
| 3959 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 3960 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-004 | permitted | decided fresh | — | ● |
| 3961 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-PO-009 ⛔ | denied | refused at the floor | — |  |
| 3962 | Validate webhook destinations against the outbound allowlist | — | permitted | docketed — nothing engaged | — |  |
| 3963 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 3964 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 3965 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 3966 | Add the new charting library licence to the allowlist | VP-SC-006 | permitted with conditions | decided fresh | — | ● |
| 3967 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3968 | Let the client extend the mobile check-in session before it times out | VP-AX-001 | permitted with conditions | decided fresh | — | ● |
| 3969 | Add the transport welfare checklist to the boarding intake form | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 3970 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | permitted | decided fresh | — |  |
| 3971 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-009 | permitted with conditions | decided fresh | — | ● |
| 3972 | Configure a circuit breaker around the external lab client | VP-HA-004 | permitted | docketed — not charged | — |  |
| 3973 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 3974 | Parameterise the new chart-search query | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 3975 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 3976 | Allowlist microchip identifier formats at the API boundary | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3977 | Trust the modality's patient identifier tag exactly as sent | VP-PO-005 | denied | decided fresh | — | ● |
| 3978 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-003 | permitted | disposed by citation | — |  |
| 3979 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | permitted | decided fresh | — |  |
| 3980 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | decided fresh | — |  |
| 3981 | Show the six-month validity window on the refill request screen | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 3982 | Require a currently licensed veterinarian's credential to sign a rabies certificate | VP-PH-002 | permitted | decided fresh | — |  |
| 3983 | Remove the per-practice toggle that could gate reportable-disease submissions | VP-PH-002 | permitted | decided fresh | — |  |
| 3984 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-002 | permitted | decided fresh | — |  |
| 3985 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | decided fresh | — |  |
| 3986 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 3987 | Prove the backup restore before the vaccine index migration | — | permitted | docketed — nothing engaged | — |  |
| 3988 | Disable the biennial inventory job during the systems migration | VP-DR-003 VP-PO-008 ⛔ | denied | refused at the floor | — |  |
| 3989 | Write the decision rationale at resolution time, not on export | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 3990 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-002 ⛔ | denied | refused at the floor | — |  |
| 3991 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | disposed by citation | — |  |
| 3992 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 3993 | Match the required supervision level to the task's risk tier | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 3994 | Let clients re-order from prescriptions written last year | VP-CS-009 | denied | decided fresh | — |  |
| 3995 | Preserve the original entry when a chart amendment is filed | VP-RR-004 | permitted | decided fresh | — |  |
| 3996 | Block agent branches from touching the compliance test suite | VP-AI-003 | permitted | decided fresh | — |  |
| 3997 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted | decided fresh | — |  |
| 3998 | Verify commit signatures on the protected release branch | VP-SC-009 | permitted | decided fresh | — |  |
| 3999 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 4000 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4001 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4002 | Write the decision rationale at resolution time, not on export | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4003 | Store payment references, not card numbers, on the retry queue | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 4004 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-GV-007 | denied | decided fresh | — |  |
| 4005 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4006 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted | decided fresh | — |  |
| 4007 | Record artefact digests in the release ledger on publish | VP-SC-008 | permitted | decided fresh | — |  |
| 4008 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-SC-008 ⛔ | denied | refused at the floor | — |  |
| 4009 | Constrain pet-photo uploads by type, size and resolved path | — | permitted | docketed — nothing engaged | — |  |
| 4010 | Validate the PDMP payload against the state schema before submit | VP-CS-007 | permitted | decided fresh | — |  |
| 4011 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | permitted | decided fresh | — |  |
| 4012 | Auto-close ketamine count mismatches under two millilitres | VP-CS-001 VP-PD-007 ⛔ | denied | refused at the floor | — |  |
| 4013 | Call an external summarisation API from the agent's new helper | VP-AI-001 VP-PO-003 ⛔ | denied | refused at the floor | — |  |
| 4014 | Bump the HL7 parser to the patched upstream release | VP-SC-006 | permitted | decided fresh | — |  |
| 4015 | Let staff issue standing scripts without opening the patient record | VP-CS-006 VP-RR-007 ⛔ | denied | refused at the floor | — |  |
| 4016 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-004 | permitted | decided fresh | — |  |
| 4017 | Expose the contest path to the owner, not only to staff | VP-GV-003 | permitted | decided fresh | — | ● |
| 4018 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-002 | permitted with conditions | decided fresh | — | ● |
| 4019 | Charge a release fee for a written prescription unless the client buys in-house | VP-CC-003 | denied | decided fresh | — |  |
| 4020 | Flag food-animal status on the patient banner before dispensing | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 4021 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4022 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | decided fresh | — |  |
| 4023 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — |  |
| 4024 | Stagger analyzer polling to flatten the morning load peak | VP-HA-003 | permitted | decided fresh | — |  |
| 4025 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-006 | permitted | decided fresh | — |  |
| 4026 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-006 | permitted | decided fresh | — |  |
| 4027 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted | decided fresh | — |  |
| 4028 | Ship a down-migration for the visit-summary table change | VP-HA-001 | permitted | decided fresh | — |  |
| 4029 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — |  |
| 4030 | Tokenise the card number before the invoice row is written | VP-PD-003 | permitted | decided fresh | — |  |
| 4031 | Review agent-authored tests for tautological assertions | VP-AI-003 | permitted | decided fresh after a tie | none_tie |  |
| 4032 | Require acknowledgement before a critical value page clears | VP-PO-002 | permitted | decided fresh | — |  |
| 4033 | Populate DICOM species and breed tags from the patient record | VP-PO-002 | permitted | decided fresh | — |  |
| 4034 | Add a post-install step that pulls the package directly | VP-SC-004 | denied | decided fresh | — |  |
| 4035 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4036 | Stagger analyzer polling to flatten the morning load peak | VP-HA-001 | permitted | decided fresh | — |  |
| 4037 | Make the note autosave idempotent under client retry | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4038 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 4039 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 4040 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 4041 | Send automated appointment texts to numbers with no recorded consent on file | VP-CC-001 VP-RR-003 ⛔ | denied | refused at the floor | — |  |
| 4042 | Update the manifest and lockfile in the same commit | VP-SC-008 | permitted | decided fresh | — |  |
| 4043 | Run the secret scanner over the diff in pre-merge CI | VP-SC-008 | permitted | decided fresh | — |  |
| 4044 | Sanitise filenames in the lab attachment upload handler | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4045 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 4046 | Cap analyzer retries at five with exponential backoff | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 4047 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted | decided fresh | — | ● |
| 4048 | Let the calculator accept twice the labelled equine maximum | VP-VC-002 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 4049 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4050 | Auto-merge agent pull requests once CI is green | VP-AI-003 | denied | decided fresh | — | ● |
| 4051 | Add a breach-notice clause to the standard vendor contract template | VP-BN-002 | permitted with conditions | decided fresh | — | ● |
| 4052 | Add regression tests for the note-render encoding path | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4053 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | decided fresh | — |  |
| 4054 | Configure retention periods per jurisdiction in the scheduler | VP-RR-005 | permitted | decided fresh | — |  |
| 4055 | Route diversion alerts to the medical director's queue within the hour | VP-CS-007 | permitted | decided fresh | — |  |
| 4056 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-007 | permitted | decided fresh | — |  |
| 4057 | Make the audit table append-only at the database level | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 4058 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-005 | permitted | decided fresh | — |  |
| 4059 | Parameterise the new chart-search query | VP-AS-005 | permitted | decided fresh | — |  |
| 4060 | Add permutation tests across the role-permission matrix | VP-RB-007 | permitted | disposed by citation | — |  |
| 4061 | Configure a circuit breaker around the external lab client | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4062 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 4063 | Add permutation tests across the role-permission matrix | VP-RB-002 | permitted | decided fresh | — | ● |
| 4064 | Record who exported an audit bundle and when | VP-RR-004 | permitted | decided fresh | — |  |
| 4065 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 4066 | Serialise inventory decrements with a row-level lock | VP-HA-002 | permitted | decided fresh | — |  |
| 4067 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted | decided fresh | — |  |
| 4068 | Return a correlation id instead of a stack trace on error | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4069 | Attach build provenance to the practice API release artefact | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 4070 | Show the technician's credential status on the surgery board | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4071 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4072 | Bump the HL7 parser to the patched upstream release | VP-SC-002 | permitted | disposed by citation | — |  |
| 4073 | Prove the backup restore before the vaccine index migration | — | permitted | docketed — nothing engaged | — |  |
| 4074 | Scope modality worklist queries to the requesting practice | VP-PO-009 | permitted | decided fresh | — |  |
| 4075 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh | — |  |
| 4076 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted | decided fresh | — |  |
| 4077 | Verify commit signatures on the protected release branch | VP-SC-002 | permitted | decided fresh | — | ● |
| 4078 | Hard-stop the dose calculator on a declared weight-unit mismatch | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 4079 | Version the regulator notice template in the policy repo | VP-BN-003 | permitted | decided fresh | — |  |
| 4080 | Record delivery confirmation before marking a breach notice as sent | VP-BN-003 | permitted | decided fresh | — |  |
| 4081 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4082 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-003 | permitted | decided fresh | — |  |
| 4083 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh | — |  |
| 4084 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted | decided fresh | — |  |
| 4085 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 4086 | Serialise inventory decrements with a row-level lock | VP-HA-003 | permitted | decided fresh | — |  |
| 4087 | Honour opt-out state at export time in the marketing job | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 4088 | Require acknowledgement before a critical value page clears | VP-PO-004 | permitted | decided fresh | — |  |
| 4089 | Restrict claim payload deserialisation to known types | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4090 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-007 | permitted | decided fresh | — |  |
| 4091 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-011 | permitted | decided fresh | — |  |
| 4092 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 4093 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 4094 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 4095 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | permitted | decided fresh | — |  |
| 4096 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-004 | permitted | decided fresh | — | ● |
| 4097 | Allow payment-plan enrolment from an unverified under-eighteen account | VP-CC-005 | denied | decided fresh | — |  |
| 4098 | Require a second approver on admin role assignments | VP-RB-008 | permitted | decided fresh | — | ● |
| 4099 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-002 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 4100 | Configure retention periods per jurisdiction in the scheduler | VP-RR-006 | permitted | decided fresh | — |  |
| 4101 | Keep the retention clock unchanged when a record is edited | VP-RR-006 | permitted | decided fresh | — |  |
| 4102 | Add regression tests for the note-render encoding path | — | permitted | docketed — nothing engaged | — |  |
| 4103 | Generate decision rationales from the outcome at export time | VP-RR-005 | denied | decided fresh | — |  |
| 4104 | Gate merges on a clean provenance verification step | VP-SC-001 | permitted | decided fresh | — |  |
| 4105 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4106 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4107 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-005 | permitted | decided fresh | — |  |
| 4108 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted | decided fresh | — |  |
| 4109 | Publish the contest outcome as granted and refused counts | VP-GV-006 | permitted | decided fresh | — |  |
| 4110 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh | — |  |
| 4111 | Cover the new boarding endpoint with a role check test | VP-RB-004 | permitted | disposed by citation | — |  |
| 4112 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 4113 | Scope the new reporting role to read-only endpoints | VP-RB-007 | permitted | disposed by citation | — |  |
| 4114 | Require an explicit owner choice before remains disposition can be saved | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 4115 | Reject malformed segments without committing a partial patient write | VP-PO-009 | permitted | decided fresh | — |  |
| 4116 | Sanitise filenames in the lab attachment upload handler | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4117 | Parameterise the new chart-search query | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 4118 | Enforce the tenant scope in the query layer, not the handler | VP-RB-003 | permitted | decided fresh | — |  |
| 4119 | Give consent withdrawal the same one-click path as granting it | VP-PD-006 | permitted | decided fresh | — |  |
| 4120 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-006 | permitted | decided fresh | — |  |
| 4121 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — |  |
| 4122 | Apply the state retention schedule to inactive owner records | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 4123 | Record the analgesia rationale when a plan is declined | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 4124 | Add a jurisdiction lookup table that sources the breach-notice clock from statute text | VP-BN-002 | permitted | decided fresh | — |  |
| 4125 | Check object ownership before returning a patient chart | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4126 | Amend the retention schedule for controlled-substance records in the rulebook | VP-SC-006 | denied | decided fresh | — |  |
| 4127 | Restrict the suspected-abuse report entry to authorised staff roles only | VP-PH-002 | permitted | decided fresh | — |  |
| 4128 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4129 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 4130 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-005 | permitted | decided fresh | — |  |
| 4131 | Check consent currency before the reminder engine sends | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 4132 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-005 | permitted | decided fresh | — |  |
| 4133 | Log the acknowledgement disposition on the referral timeline | VP-GV-006 | permitted | decided fresh | — |  |
| 4134 | Keep reporter bulletins out of the adjudicator's context builder | VP-GV-006 | permitted | decided fresh | — |  |
| 4135 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-006 | permitted | decided fresh | — |  |
| 4136 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh | — |  |
| 4137 | Render the owner's intake note as raw HTML to keep their formatting | VP-AS-001 | denied | decided fresh | — |  |
| 4138 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4139 | Take record timestamps from the monotonic server clock | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4140 | Preserve the original entry when a chart amendment is filed | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4141 | Match analyzer results on patient name alone | VP-PO-001 ⛔ | denied | refused at the floor | — |  |
| 4142 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 4143 | Start the breach-notice timer at confirmed root cause instead of first detection | VP-BN-001 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 4144 | Add a persistent 'automated, not a veterinarian' banner to every triage assistant reply | VP-PS-002 | permitted with conditions | decided fresh | — | ● |
| 4145 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 4146 | Let the calculator accept twice the labelled equine maximum | VP-VC-003 VP-AI-005 ⛔ | denied | refused at the floor | — |  |
| 4147 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4148 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4149 | Add a campaign endpoint that exports the whole owner list | VP-PD-007 | denied | decided fresh | — |  |
| 4150 | Sign CSOS orders with a shared practice login instead of the individual certificate | VP-DR-003 VP-PO-003 ⛔ | denied | refused at the floor | — |  |
| 4151 | Check the version token on clinical note writes | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4152 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-006 | denied | decided fresh | — | ● |
| 4153 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-002 | denied | decided fresh | — |  |
| 4154 | Time-box break-glass access to four hours and log the grant | VP-RB-007 | permitted | decided fresh | — |  |
| 4155 | Assign the daily audit review to the practice manager role | VP-RR-002 | permitted | decided fresh | — |  |
| 4156 | Reset the retention date whenever a record is edited | VP-RR-001 VP-GV-006 ⛔ | denied | refused at the floor | — |  |
| 4157 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 4158 | Block record purges that fall inside the two-year retention term | VP-CS-007 | permitted | decided fresh | — |  |
| 4159 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-007 | permitted | decided fresh | — |  |
| 4160 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-004 | permitted | decided fresh | — |  |
| 4161 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 4162 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-007 | permitted | decided fresh | — |  |
| 4163 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted | decided fresh | — |  |
| 4164 | Queue reminder sends so a retry storm cannot amplify | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4165 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 4166 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-006 | permitted | decided fresh | — |  |
| 4167 | Restrict claim payload deserialisation to known types | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4168 | Pair the required-field error with visible text, not colour alone | VP-AX-002 | permitted | decided fresh | — |  |
| 4169 | Quarantine unmatched analyzer results for technician review | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 4170 | Pin the build runner image and make each job ephemeral | VP-SC-002 | permitted | decided fresh | — | ● |
| 4171 | Keep the contest link visible on every automated decision notice | VP-GV-003 | permitted | decided fresh | — |  |
| 4172 | Write a docket entry for every uncharged arrival | VP-GV-003 | permitted | decided fresh | — |  |
| 4173 | Add regression tests for the note-render encoding path | VP-AS-001 | permitted | disposed by citation | — |  |
| 4174 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | decided fresh | — | ● |
| 4175 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-010 | permitted | decided fresh after a tie | none_tie |  |
| 4176 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 4177 | Show the six-month validity window on the refill request screen | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 4178 | Encode clinical note text before rendering it in the portal | VP-AS-003 | permitted | disposed by citation | — |  |
| 4179 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 4180 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | denied | bound by precedent | REC-S0116 |  |
| 4181 | Check the version token on clinical note writes | VP-HA-002 | permitted | decided fresh | — |  |
| 4182 | Add contract tests for the pinned HL7 v2 profile | VP-PO-007 | permitted | decided fresh | — |  |
| 4183 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | disposed by citation | — |  |
| 4184 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-003 | permitted | decided fresh | — |  |
| 4185 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-003 | permitted | decided fresh | — |  |
| 4186 | Link the incident runbook from every breach-detection alert payload | VP-BN-003 | permitted with conditions | decided fresh | — | ● |
| 4187 | Store the amendment author alongside the superseded text | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 4188 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-002 VP-GV-004 ⛔ | denied | refused at the floor | — |  |
| 4189 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 4190 | Widen the deploy freeze exception list in the governance repo | VP-SC-005 | denied | decided fresh | — |  |
| 4191 | Assign a named reviewer to the vendored DICOM parser | VP-SC-002 | permitted | decided fresh | — |  |
| 4192 | Remove the necessity note from the bulk compounding form | VP-VC-002 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 4193 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | decided fresh | — |  |
| 4194 | Write the decision rationale at resolution time, not on export | VP-RR-005 | permitted | decided fresh | — |  |
| 4195 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 4196 | Hard-stop the dose calculator on a declared weight-unit mismatch | VP-PS-002 | permitted | decided fresh | — |  |
| 4197 | Publish the contest counts in the audit export header | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 4198 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 4199 | Restrict claim payload deserialisation to known types | — | permitted | docketed — nothing engaged | — |  |
| 4200 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh after a tie | none_tie |  |
| 4201 | Withhold prescription finalisation from technician accounts | VP-RB-004 | permitted | decided fresh | — |  |
| 4202 | Run the secret scanner over the diff in pre-merge CI | VP-SC-001 | permitted | decided fresh | — |  |
| 4203 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 4204 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 4205 | Propose a sunset clause for the analytics pilot exception | VP-PD-007 | denied | decided fresh | — |  |
| 4206 | Verify the hash chain when an audit bundle is exported | VP-RR-005 | permitted | decided fresh | — |  |
| 4207 | Add contract tests for the pinned HL7 v2 profile | VP-PO-009 | permitted | decided fresh | — |  |
| 4208 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-008 | permitted | decided fresh | — |  |
| 4209 | Run semantic analysis over the agent diff in CI | VP-AI-008 | permitted | decided fresh | — |  |
| 4210 | Run the secret scanner over the diff in pre-merge CI | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 4211 | Strip the standing declaration from the audit bundle header | VP-GV-002 VP-CS-010 ⛔ | denied | refused at the floor | — |  |
| 4212 | Store payment references, not card numbers, on the retry queue | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 4213 | Write the decision rationale at resolution time, not on export | VP-RR-007 | permitted | decided fresh | — |  |
| 4214 | Purge Form 222 order records after one year to shrink the archive | VP-DR-002 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 4215 | Track welfare inspection findings to a remediation due date | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4216 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 4217 | Verify commit signatures on the protected release branch | VP-SC-002 | permitted | decided fresh | — | ● |
| 4218 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted | disposed by citation | — |  |
| 4219 | Record the analgesia rationale when a plan is declined | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4220 | Version the regulator notice template in the policy repo | VP-BN-003 | permitted | decided fresh | — |  |
| 4221 | Shorten the break-glass expiry constant in the rulebook | VP-CC-004 | denied | decided fresh | — |  |
| 4222 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 4223 | Check the version token on clinical note writes | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4224 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | disposed by citation | — |  |
| 4225 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4226 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 4227 | Make the feed directive expiry date a mandatory field | VP-VC-004 | permitted | decided fresh | — |  |
| 4228 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-002 | denied | decided fresh | — |  |
| 4229 | Publish the contest counts in the audit export header | VP-RR-003 | permitted | decided fresh | — |  |
| 4230 | Return a correlation id instead of a stack trace on error | VP-AS-003 | permitted | decided fresh | — |  |
| 4231 | Unblock enrofloxacin ordering for dairy herds | VP-VC-001 VP-CC-003 ⛔ | denied | refused at the floor | — |  |
| 4232 | Cap the records-copy fee at the state's statutory maximum | VP-CC-002 | permitted | decided fresh | — |  |
| 4233 | Suppress reminder sends to any number that has already replied STOP | VP-CC-002 | permitted | decided fresh | — |  |
| 4234 | Populate DICOM species and breed tags from the patient record | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 4235 | Swap the date library for a fork published by an unknown account | VP-SC-009 | denied | decided fresh | — |  |
| 4236 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh | — |  |
| 4237 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted | decided fresh | — |  |
| 4238 | Put the public registry ahead of the internal one in the resolver | VP-SC-009 | denied | decided fresh | — |  |
| 4239 | Let the coding agent rewrite the session authentication middleware | VP-AI-008 | denied | decided fresh | — | ● |
| 4240 | Attach build provenance to the practice API release artefact | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 4241 | Pin the build runner image and make each job ephemeral | VP-SC-004 | permitted | decided fresh | — |  |
| 4242 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 4243 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | decided fresh | — |  |
| 4244 | Drop internal identifiers from the public error envelope | VP-AS-003 | permitted | decided fresh after a tie | none_tie |  |
| 4245 | Quarantine unmatched analyzer results for technician review | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 4246 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-004 | denied | decided fresh | — |  |
| 4247 | Point the resolver at the private registry before the public one | VP-SC-003 | permitted | decided fresh | — |  |
| 4248 | Match study patient identity on microchip and account number | VP-PO-002 | permitted | decided fresh | — |  |
| 4249 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | disposed by citation | — |  |
| 4250 | Log the authenticated prescriber id on each dispensing event | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 4251 | Encode clinical note text before rendering it in the portal | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4252 | Record artefact digests in the release ledger on publish | VP-SC-006 | permitted | decided fresh | — |  |
| 4253 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 4254 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-010 | permitted | decided fresh | — |  |
| 4255 | Review agent-authored tests for tautological assertions | VP-AI-005 | permitted | decided fresh | — |  |
| 4256 | Make the human review queue reachable from the portal | VP-GV-004 | permitted | decided fresh | — |  |
| 4257 | Expose the contest path to the owner, not only to staff | VP-GV-004 | permitted | decided fresh | — |  |
| 4258 | Make the human review queue reachable from the portal | VP-GV-007 | permitted | decided fresh | — |  |
| 4259 | Move threshold parameters into the legislated configuration | VP-GV-007 | permitted | decided fresh | — |  |
| 4260 | Amend the retention schedule for controlled-substance records in the rulebook | VP-SC-009 | denied | decided fresh | — |  |
| 4261 | Use the client-supplied filename as the attachment storage path | VP-AS-001 | denied | decided fresh | — |  |
| 4262 | Let the dose calculator run on last year's recorded weight when today's is missing | VP-PS-004 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 4263 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 4264 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-008 | permitted | decided fresh | — |  |
| 4265 | Require a verified adult guardian before a minor's client account can be created | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 4266 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh | — |  |
| 4267 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-AI-004 ⛔ | denied | refused at the floor | — |  |
| 4268 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — |  |
| 4269 | Capture the research protocol number on regulated-facility visits | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4270 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-006 | permitted | decided fresh | — |  |
| 4271 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-006 | permitted | decided fresh | — |  |
| 4272 | Populate DICOM species and breed tags from the patient record | VP-PO-007 | permitted | decided fresh | — |  |
| 4273 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-003 | permitted | decided fresh | — |  |
| 4274 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 4275 | Verify focus order on the consent dialog before each release | VP-AX-002 | permitted | decided fresh | — |  |
| 4276 | Fail the portal build on any WCAG 2.2 AA violation instead of just warning | VP-AX-002 | permitted | decided fresh | — |  |
| 4277 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 4278 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | decided fresh | — |  |
| 4279 | Unblock enrofloxacin ordering for dairy herds | VP-VC-001 ⛔ | denied | refused at the floor | — |  |
| 4280 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | decided fresh | — |  |
| 4281 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 4282 | Extend access-log retention to cover the full notification lookback window | VP-BN-003 | permitted with conditions | decided fresh | — | ● |
| 4283 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4284 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | decided fresh | — |  |
| 4285 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | decided fresh | — |  |
| 4286 | Add a support endpoint that dumps the full owner record | VP-PD-002 VP-SC-001 ⛔ | denied | refused at the floor | — |  |
| 4287 | Check consent currency before the reminder engine sends | VP-PD-007 | permitted | decided fresh | — |  |
| 4288 | Deny clinical note writes to the receptionist role | VP-RB-004 | permitted | decided fresh | — |  |
| 4289 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh | — |  |
| 4290 | Add the new charting library licence to the allowlist | VP-SC-001 | permitted | decided fresh | — | ● |
| 4291 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-002 ⛔ | denied | refused at the floor | — |  |
| 4292 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-001 | permitted | decided fresh | — |  |
| 4293 | Encrypt the owner address column at rest in the portal store | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 4294 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4295 | Document the degraded path when the reference lab is down | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4296 | Tokenise the card number before the invoice row is written | VP-PD-007 | permitted | decided fresh | — |  |
| 4297 | Publish the hotfix image straight from a laptop build | VP-SC-008 | denied | decided fresh | — |  |
| 4298 | Record the analgesia rationale when a plan is declined | VP-AW-004 | permitted | decided fresh | — |  |
| 4299 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-001 ⛔ | denied | refused at the floor | — |  |
| 4300 | Record the analgesia rationale when a plan is declined | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 4301 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-009 | denied | decided fresh | — |  |
| 4302 | Remove the necessity note from the bulk compounding form | VP-VC-002 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 4303 | Swap the date library for a fork published by an unknown account | VP-SC-003 | denied | decided fresh | — |  |
| 4304 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 4305 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4306 | Uncheck the wellness-plan auto-renewal box by default at enrolment | VP-CC-003 | permitted | decided fresh | — |  |
| 4307 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 4308 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-007 | permitted | decided fresh | — |  |
| 4309 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-007 | permitted | decided fresh | — |  |
| 4310 | Replace the hand-rolled token hash with the vetted library | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4311 | Keep the retention clock unchanged when a record is edited | VP-RR-004 | permitted | decided fresh | — |  |
| 4312 | Skip the dispensing audit test the agent could not get passing | VP-AI-003 | denied | decided fresh | — |  |
| 4313 | Point the resolver at the private registry before the public one | VP-SC-007 | permitted | decided fresh | — | ● |
| 4314 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-AI-006 ⛔ | denied | refused at the floor | — |  |
| 4315 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4316 | Raise the p95 latency budget from ten to twenty-five percent | VP-AS-003 | denied | decided fresh | — |  |
| 4317 | Cap analyzer retries at five with exponential backoff | VP-PO-002 | permitted | decided fresh | — |  |
| 4318 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 4319 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted | decided fresh | — |  |
| 4320 | Let one admin grant EPCS signing rights from the user screen | VP-CS-006 VP-DR-004 ⛔ | denied | refused at the floor | — |  |
| 4321 | Rank retrieval candidates using the audit register's findings | VP-GV-006 | denied | decided fresh | — |  |
| 4322 | Update the manifest and lockfile in the same commit | VP-SC-009 | permitted | disposed by citation | — |  |
| 4323 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 4324 | Remove the necessity note from the bulk compounding form | VP-VC-006 | denied | decided fresh | — |  |
| 4325 | Queue reminder sends so a retry storm cannot amplify | VP-HA-003 | permitted | decided fresh | — |  |
| 4326 | Remove the deadline timer from the data export request queue | VP-PD-008 | denied | decided fresh | — |  |
| 4327 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | decided fresh | — |  |
| 4328 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — |  |
| 4329 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | decided fresh | — |  |
| 4330 | Block dose calculation until a current weight is recorded for the visit | VP-PS-002 | permitted | decided fresh | — |  |
| 4331 | Attach a residue risk assessment to the food-animal order form | VP-VC-005 | permitted | decided fresh | — |  |
| 4332 | Attach the standing declaration to every audit export | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4333 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | decided fresh | — |  |
| 4334 | Add an accessible name to the new custom toggle control | VP-AX-001 | permitted | decided fresh | — |  |
| 4335 | Wrap result-to-patient binding in a single database transaction | VP-PO-009 | permitted | decided fresh | — |  |
| 4336 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-CS-008 | denied | decided fresh | — |  |
| 4337 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4338 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | disposed by citation | — |  |
| 4339 | Timestamp records from the workstation clock the client sends | VP-RR-002 | denied | decided fresh | — |  |
| 4340 | Trust the modality's patient identifier tag exactly as sent | VP-PO-005 | denied | decided fresh | — | ● |
| 4341 | Require the veterinary care plan on the regulated facility record | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4342 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted with conditions | decided fresh | — | ● |
| 4343 | Drop internal identifiers from the public error envelope | — | permitted | docketed — nothing engaged | — |  |
| 4344 | Route diversion alerts to the medical director's queue within the hour | VP-CS-009 | permitted | decided fresh | — |  |
| 4345 | Log the authenticated prescriber id on each dispensing event | VP-CS-009 | permitted | decided fresh | — |  |
| 4346 | Give consent withdrawal the same one-click path as granting it | VP-PD-005 | permitted | decided fresh | — |  |
| 4347 | Cap analyzer retries at five with exponential backoff | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 4348 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4349 | Reject malformed segments without committing a partial patient write | VP-PO-007 | permitted | decided fresh | — |  |
| 4350 | Encode clinical note text before rendering it in the portal | VP-AS-001 | permitted | decided fresh | — |  |
| 4351 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-001 VP-AI-003 ⛔ | denied | refused at the floor | — |  |
| 4352 | Send automated appointment texts to numbers with no recorded consent on file | VP-CC-001 VP-RB-003 ⛔ | denied | refused at the floor | — |  |
| 4353 | Require acknowledgement before a critical value page clears | VP-PO-009 | permitted | decided fresh | — |  |
| 4354 | Assign a named reviewer to the vendored DICOM parser | VP-SC-007 | permitted | decided fresh | — |  |
| 4355 | Point the resolver at the private registry before the public one | VP-SC-007 | permitted | decided fresh | — |  |
| 4356 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4357 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 4358 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted | decided fresh | — |  |
| 4359 | Verify commit signatures on the protected release branch | VP-SC-008 | permitted | decided fresh | — |  |
| 4360 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | decided fresh | — |  |
| 4361 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | decided fresh | — | ● |
| 4362 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 4363 | Extend the log redaction filter to the new owner phone field | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 4364 | Make the audit table append-only at the database level | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4365 | Make the audit table append-only at the database level | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4366 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4367 | Let the calculator accept twice the labelled equine maximum | VP-VC-002 ⛔ | denied | refused at the floor | — |  |
| 4368 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-SC-001 | denied | decided fresh | — |  |
| 4369 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 4370 | Scope modality worklist queries to the requesting practice | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4371 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-007 | denied | decided fresh | — |  |
| 4372 | Prove the backup restore before the vaccine index migration | VP-HA-002 | permitted | decided fresh | — |  |
| 4373 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | decided fresh | — |  |
| 4374 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted | decided fresh | — |  |
| 4375 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 4376 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | decided fresh | — |  |
| 4377 | Start the breach-notice timer at confirmed root cause instead of first detection | VP-BN-001 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 4378 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | decided fresh | — | ● |
| 4379 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 4380 | Wrap result-to-patient binding in a single database transaction | VP-PO-004 | permitted | decided fresh | — |  |
| 4381 | Add contract tests for the pinned HL7 v2 profile | VP-PO-004 | permitted | decided fresh | — |  |
| 4382 | Drop analyzer messages that fail to parse and move on | VP-PO-005 | denied | decided fresh | — |  |
| 4383 | Announce form validation errors to assistive technology on submit | VP-AX-001 | permitted | decided fresh | — |  |
| 4384 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted | decided fresh | — |  |
| 4385 | Check consent currency before the reminder engine sends | VP-PD-009 | permitted | decided fresh | — |  |
| 4386 | Add a campaign endpoint that exports the whole owner list | VP-PD-007 | denied | decided fresh | — | ● |
| 4387 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4388 | Renumber the point-of-care provisions after the device policy merge | VP-AS-001 | denied | decided fresh | — |  |
| 4389 | Check the version token on clinical note writes | — | permitted | docketed — nothing engaged | — |  |
| 4390 | Build the chart-search filter by concatenating the query string | VP-AS-003 | denied | decided fresh | — | ● |
| 4391 | Record the prompt and context hash on the agent's pull request | VP-AI-008 | permitted | decided fresh | — |  |
| 4392 | Drop internal identifiers from the public error envelope | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 4393 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | permitted | decided fresh | — |  |
| 4394 | Hold medical-record releases until the client's balance is paid | VP-CC-005 | denied | decided fresh | — |  |
| 4395 | Deny clinical note writes to the receptionist role | VP-RB-004 | permitted | disposed by citation | — |  |
| 4396 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-003 | permitted with conditions | decided fresh | — | ● |
| 4397 | Block agent branches from touching the compliance test suite | VP-AI-006 | permitted | decided fresh | — |  |
| 4398 | Attach the standing declaration to every audit export | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 4399 | Encode clinical note text before rendering it in the portal | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 4400 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-006 | permitted | decided fresh | — |  |
| 4401 | Purge Form 222 order records after one year to shrink the archive | VP-DR-002 VP-CS-007 ⛔ | denied | refused at the floor | — |  |
| 4402 | Require a second approver on admin role assignments | VP-RB-004 | permitted | disposed by citation | — |  |
| 4403 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 4404 | Let the dose calculator run on last year's recorded weight when today's is missing | VP-PS-004 VP-SC-006 ⛔ | denied | refused at the floor | — |  |
| 4405 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-001 | permitted | decided fresh | — |  |
| 4406 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 4407 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 4408 | Record the prompt and context hash on the agent's pull request | VP-AI-007 | permitted | decided fresh | — |  |
| 4409 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 4410 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4411 | Encode clinical note text before rendering it in the portal | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4412 | Update the manifest and lockfile in the same commit | VP-SC-009 | permitted with conditions | decided fresh | — | ● |
| 4413 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted | decided fresh | — |  |
| 4414 | Verify commit signatures on the protected release branch | VP-SC-008 | permitted | decided fresh | — | ● |
| 4415 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted | decided fresh | — |  |
| 4416 | Timestamp records from the workstation clock the client sends | VP-RR-006 | denied | decided fresh | — |  |
| 4417 | Drop internal identifiers from the public error envelope | VP-AS-005 | permitted | decided fresh | — |  |
| 4418 | Time-box break-glass access to four hours and log the grant | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4419 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — |  |
| 4420 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 4421 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 4422 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4423 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted | decided fresh | — |  |
| 4424 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-003 | permitted | decided fresh | — |  |
| 4425 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-003 | permitted | decided fresh | — |  |
| 4426 | Route diversion alerts to the medical director's queue within the hour | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 4427 | Encode clinical note text before rendering it in the portal | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4428 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | permitted | decided fresh | — |  |
| 4429 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-004 | permitted | decided fresh | — |  |
| 4430 | Block dose calculation until a current weight is recorded for the visit | VP-PS-003 | permitted | decided fresh | — |  |
| 4431 | Apply the state retention schedule to inactive owner records | VP-PD-004 | permitted | decided fresh | — |  |
| 4432 | Let the dose calculator run on last year's recorded weight when today's is missing | VP-PS-001 VP-RR-002 ⛔ | denied | refused at the floor | — |  |
| 4433 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | permitted | decided fresh | — |  |
| 4434 | Reject malformed segments without committing a partial patient write | VP-PO-004 | permitted | decided fresh | — |  |
| 4435 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4436 | Add a jurisdiction lookup table that sources the breach-notice clock from statute text | VP-BN-002 | permitted with conditions | decided fresh | — | ● |
| 4437 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 4438 | Enforce the tenant scope in the query layer, not the handler | VP-RB-007 | permitted | decided fresh | — |  |
| 4439 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4440 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4441 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 4442 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-004 VP-SC-005 ⛔ | denied | refused at the floor | — |  |
| 4443 | Preserve the original entry when a chart amendment is filed | VP-RR-004 | permitted | decided fresh | — |  |
| 4444 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 4445 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4446 | Keep the retention clock unchanged when a record is edited | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4447 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | decided fresh | — |  |
| 4448 | Attribute the standing declaration to the enacting authority | VP-GV-007 | permitted | decided fresh | — |  |
| 4449 | Attribute the standing declaration to the enacting authority | VP-GV-007 | permitted | decided fresh | — |  |
| 4450 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 4451 | Allowlist microchip identifier formats at the API boundary | VP-AS-005 | permitted | disposed by citation | — |  |
| 4452 | Tokenise the card number before the invoice row is written | VP-PD-005 | permitted | decided fresh | — |  |
| 4453 | Log the authenticated prescriber id on each dispensing event | VP-CS-011 | permitted | decided fresh | — |  |
| 4454 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 4455 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4456 | Route diversion alerts to the medical director's queue within the hour | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 4457 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-002 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 4458 | Record artefact digests in the release ledger on publish | VP-SC-009 | permitted | decided fresh | — |  |
| 4459 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — |  |
| 4460 | Quarantine unmatched analyzer results for technician review | VP-PO-007 | permitted | decided fresh | — |  |
| 4461 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4462 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | permitted | decided fresh | — |  |
| 4463 | Preserve the original entry when a chart amendment is filed | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 4464 | Scope the new reporting role to read-only endpoints | VP-RB-006 | permitted | decided fresh | — |  |
| 4465 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-001 | permitted | decided fresh | — |  |
| 4466 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | disposed by citation | — |  |
| 4467 | Sanitise filenames in the lab attachment upload handler | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 4468 | Record who exported an audit bundle and when | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 4469 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 4470 | Bind each service account to a single practice id | VP-RB-007 | permitted | decided fresh | — |  |
| 4471 | Give consent withdrawal the same one-click path as granting it | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 4472 | Warn when a dose falls outside the labelled species range | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 4473 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh | — |  |
| 4474 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh | — |  |
| 4475 | Label agent-authored commits so review routing can see them | VP-AI-003 | permitted | decided fresh | — |  |
| 4476 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 4477 | Parameterise the new chart-search query | VP-AS-002 | permitted | decided fresh | — | ● |
| 4478 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 4479 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-003 | permitted | decided fresh | — |  |
| 4480 | Block agent branches from touching the compliance test suite | VP-AI-007 | permitted | decided fresh | — |  |
| 4481 | Prove the backup restore before the vaccine index migration | VP-HA-001 | permitted | decided fresh | — |  |
| 4482 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-004 | permitted with conditions | decided fresh | — | ● |
| 4483 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted | decided fresh | — |  |
| 4484 | Run diversion analytics over every dispensing event across all practices | VP-DR-004 | permitted | decided fresh | — |  |
| 4485 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 4486 | Let Schedule II reorders go through the general purchasing API instead of CSOS | VP-DR-001 VP-RB-007 ⛔ | denied | refused at the floor | — |  |
| 4487 | Verify every imported package resolves in the registry before merge | VP-AI-003 | permitted | decided fresh | — |  |
| 4488 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted | decided fresh | — |  |
| 4489 | Move the CVSS threshold from seven to eight in the dependency policy | VP-PD-005 | denied | decided fresh | — |  |
| 4490 | Remove the suspected-abuse report option from the chart menu | VP-PH-001 VP-VC-004 ⛔ | denied | refused at the floor | — |  |
| 4491 | Bump the HL7 parser to the patched upstream release | VP-SC-004 | permitted | decided fresh | — |  |
| 4492 | Block procedure sign-off by roles outside the delegated scope | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 4493 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 4494 | Let the signup form create a client account without checking the applicant's age | VP-CC-004 | denied | decided fresh | — |  |
| 4495 | Drop analyzer messages that fail to parse and move on | VP-PO-001 VP-CC-004 ⛔ | denied | refused at the floor | — |  |
| 4496 | Add a free-text field for the owner's social security number | VP-PD-006 | denied | decided fresh | — |  |
| 4497 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 4498 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted | decided fresh | — |  |
| 4499 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-011 | denied | decided fresh | — |  |
| 4500 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-003 | permitted | decided fresh | — |  |
| 4501 | Add the transport welfare checklist to the boarding intake form | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 4502 | Run the secret scanner over the diff in pre-merge CI | VP-SC-006 | permitted | decided fresh | — |  |
| 4503 | Gate merges on a clean provenance verification step | VP-SC-006 | permitted | decided fresh | — |  |
| 4504 | Label agent-authored commits so review routing can see them | VP-AI-003 | permitted | decided fresh | — |  |
| 4505 | Parameterise the new chart-search query | — | permitted | docketed — nothing engaged | — |  |
| 4506 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4507 | Record the analgesia rationale when a plan is declined | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4508 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4509 | Split the agent-refactored invoicing function to cut its branching | VP-AI-008 | permitted | decided fresh | — |  |
| 4510 | Block agent branches from touching the compliance test suite | VP-AI-008 | permitted | decided fresh | — |  |
| 4511 | Read the practice id from the X-Practice request header | VP-RB-007 | denied | decided fresh | — |  |
| 4512 | Write the decision rationale at resolution time, not on export | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4513 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 4514 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 4515 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-004 | permitted | disposed by citation | — |  |
| 4516 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 4517 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 4518 | Parameterise the new chart-search query | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4519 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | permitted | decided fresh | — |  |
| 4520 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 4521 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | decided fresh | — |  |
| 4522 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-004 | permitted | decided fresh | — |  |
| 4523 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-004 | permitted | decided fresh | — |  |
| 4524 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 4525 | Cut access-log retention to thirty days to save storage costs | VP-BN-002 | denied | decided fresh | — | ● |
| 4526 | Quarantine unmatched analyzer results for technician review | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4527 | Redact owner email addresses from claims connector debug output | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 4528 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4529 | Expose the contest path to the owner, not only to staff | VP-GV-006 | permitted | decided fresh | — |  |
| 4530 | Update the manifest and lockfile in the same commit | VP-SC-005 | permitted | disposed by citation | — |  |
| 4531 | Add a post-install step that pulls the package directly | VP-SC-003 | denied | decided fresh | — |  |
| 4532 | Separate the audit register store from the precedent store | VP-GV-003 | permitted | decided fresh | — |  |
| 4533 | Bump the HL7 parser to the patched upstream release | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 4534 | Require a second approver on admin role assignments | VP-RB-006 | permitted | decided fresh | — |  |
| 4535 | Check object ownership before returning a patient chart | VP-RB-006 | permitted | decided fresh | — |  |
| 4536 | Return a correlation id instead of a stack trace on error | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4537 | Raise the p95 latency budget from ten to twenty-five percent | VP-AI-007 | denied | decided fresh | — |  |
| 4538 | Validate delegated task lists against the state practice act table | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 4539 | Return the full exception text in the API error body | VP-AS-004 | denied | decided fresh | — |  |
| 4540 | Check the version token on clinical note writes | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4541 | Add a support endpoint that dumps the full owner record | VP-PD-002 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 4542 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 4543 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-009 | permitted | decided fresh | — |  |
| 4544 | Expose the radiography panel to the internet for vendor support | VP-PO-008 | denied | decided fresh | — |  |
| 4545 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-001 VP-AS-003 ⛔ | denied | refused at the floor | — |  |
| 4546 | Configure a circuit breaker around the external lab client | VP-HA-003 | permitted | decided fresh | — |  |
| 4547 | Write the result row first and link the patient in a follow-up job | VP-PO-002 | denied | decided fresh | — |  |
| 4548 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4549 | Overwrite the original diagnosis text when a chart is amended | VP-RR-004 | denied | decided fresh | — |  |
| 4550 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4551 | Add a concurrency test for simultaneous discharge summary saves | — | permitted | docketed — nothing engaged | — |  |
| 4552 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted | decided fresh | — |  |
| 4553 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 4554 | Hide the contest link when the decision is a denial | VP-GV-003 | denied | decided fresh | — |  |
| 4555 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 4556 | Time-box break-glass access to four hours and log the grant | VP-RB-006 | permitted | decided fresh | — | ● |
| 4557 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-005 | permitted | disposed by citation | — |  |
| 4558 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-006 | permitted | decided fresh | — |  |
| 4559 | Release medical records regardless of outstanding balance | VP-CC-006 | permitted | decided fresh | — |  |
| 4560 | Add contract tests for the pinned HL7 v2 profile | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 4561 | Let the coding agent rewrite the session authentication middleware | VP-AI-001 VP-GV-007 ⛔ | denied | refused at the floor | — |  |
| 4562 | Pin the build runner image and make each job ephemeral | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 4563 | Honour opt-out state at export time in the marketing job | VP-PD-007 | permitted | decided fresh | — |  |
| 4564 | Encrypt the owner address column at rest in the portal store | VP-PD-007 | permitted | decided fresh | — |  |
| 4565 | Enable video-only exams for prescribing in every state | VP-VC-004 | denied | decided fresh | — |  |
| 4566 | Take record timestamps from the monotonic server clock | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 4567 | Apply the state retention schedule to inactive owner records | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 4568 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 4569 | Add the boarding service to the critical-service list in policy | VP-PO-010 | denied | decided fresh | — |  |
| 4570 | Add an admin path that updates the audit row to fix a typo | VP-RR-001 VP-RB-002 ⛔ | denied | refused at the floor | — |  |
| 4571 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | decided fresh | — |  |
| 4572 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-004 VP-PH-002 ⛔ | denied | refused at the floor | — |  |
| 4573 | Build a searchable face gallery from the lobby camera feed | VP-GV-004 | denied | decided fresh | — | ● |
| 4574 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | decided fresh | — |  |
| 4575 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-006 | permitted | decided fresh | — | ● |
| 4576 | Lower the changed-line coverage threshold in the policy repo | VP-RB-006 | denied | decided fresh | — |  |
| 4577 | Block dose calculation until a current weight is recorded for the visit | VP-PS-002 | permitted | decided fresh | — |  |
| 4578 | Require a tag scan at every remains custody transfer | VP-PS-002 | permitted | decided fresh | — |  |
| 4579 | Restrict claim payload deserialisation to known types | VP-AS-003 | permitted | decided fresh | — | ● |
| 4580 | Let clients re-order from prescriptions written last year | VP-CS-001 VP-AS-003 ⛔ | denied | refused at the floor | — |  |
| 4581 | Enable video-only exams for prescribing in every state | VP-VC-003 VP-SC-008 ⛔ | denied | refused at the floor | — |  |
| 4582 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | decided fresh | — |  |
| 4583 | Drop analyzer messages that fail to parse and move on | VP-PO-010 | denied | decided fresh | — |  |
| 4584 | Match study patient identity on microchip and account number | VP-PO-004 | permitted | decided fresh | — |  |
| 4585 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | permitted | decided fresh | — |  |
| 4586 | Waive the records-copy fee for a client's own written prescription request | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 4587 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-004 | permitted | decided fresh | — |  |
| 4588 | Track welfare inspection findings to a remediation due date | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4589 | Parameterise the new chart-search query | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4590 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted | disposed by citation | — |  |
| 4591 | Require a named human reviewer on every agent-authored pull request | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 4592 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | decided fresh | — |  |
| 4593 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | decided fresh | — |  |
| 4594 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-007 | permitted with conditions | decided fresh | — | ● |
| 4595 | Add the new charting library licence to the allowlist | VP-SC-004 | permitted | decided fresh | — | ● |
| 4596 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — | ● |
| 4597 | Gate merges on a clean provenance verification step | VP-SC-007 | permitted with conditions | decided fresh | — | ● |
| 4598 | Allow inline scripts in the portal CSP so the booking widget loads | VP-AS-004 | denied | decided fresh | — |  |
| 4599 | Serialise inventory decrements with a row-level lock | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4600 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | permitted | decided fresh | — |  |
| 4601 | Keep the contest link visible on every automated decision notice | VP-GV-005 | permitted | decided fresh | — |  |
| 4602 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — |  |
| 4603 | Cover the new boarding endpoint with a role check test | VP-RB-006 | permitted | decided fresh | — |  |
| 4604 | Record the prompt and context hash on the agent's pull request | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 4605 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-006 | permitted | decided fresh | — |  |
| 4606 | Add a free-text field for the owner's social security number | VP-PD-009 | denied | decided fresh | — | ● |
| 4607 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | decided fresh | — |  |
| 4608 | Label agent-authored commits so review routing can see them | VP-AI-007 | permitted | decided fresh | — |  |
| 4609 | Record the prompt and context hash on the agent's pull request | VP-AI-007 | permitted | decided fresh | — |  |
| 4610 | Add the transport welfare checklist to the boarding intake form | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4611 | Add permutation tests across the role-permission matrix | VP-RB-006 | permitted | decided fresh | — |  |
| 4612 | Deny clinical note writes to the receptionist role | VP-RB-006 | permitted | decided fresh | — |  |
| 4613 | Pin the build runner image and make each job ephemeral | VP-SC-004 | permitted | decided fresh | — |  |
| 4614 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 4615 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-004 | permitted with conditions | decided fresh | — | ● |
| 4616 | Point the resolver at the private registry before the public one | VP-SC-001 | permitted | decided fresh | — |  |
| 4617 | Honour opt-out state at export time in the marketing job | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 4618 | Show which record controlled on the decision page | VP-GV-005 | permitted | decided fresh | — |  |
| 4619 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4620 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-010 | denied | bound by precedent | REC-S0114 |  |
| 4621 | Close automated denials without offering a human review request | VP-GV-004 | denied | decided fresh | — |  |
| 4622 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted | decided fresh | — |  |
| 4623 | Return a correlation id instead of a stack trace on error | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4624 | Store the amendment author alongside the superseded text | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 4625 | Capture the research protocol number on regulated-facility visits | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 4626 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 4627 | Make the withdrawal interval optional on food-animal orders | VP-VC-002 ⛔ | denied | refused at the floor | — |  |
| 4628 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-SC-003 | denied | decided fresh | — |  |
| 4629 | Amend the retention schedule for controlled-substance records in the rulebook | VP-PO-007 | denied | decided fresh | — |  |
| 4630 | Wrap result-to-patient binding in a single database transaction | VP-PO-006 | permitted with conditions | decided fresh | — | ● |
| 4631 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-007 | permitted | decided fresh | — |  |
| 4632 | Show the six-month validity window on the refill request screen | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 4633 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | decided fresh | — |  |
| 4634 | Give consent withdrawal the same one-click path as granting it | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 4635 | Deny clinical note writes to the receptionist role | VP-RB-007 | permitted | decided fresh | — |  |
| 4636 | Require a second approver on admin role assignments | VP-RB-007 | permitted | decided fresh | — |  |
| 4637 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 4638 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 4639 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted | decided fresh | — |  |
| 4640 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted | decided fresh | — |  |
| 4641 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4642 | Remove the expiry from break-glass grants so support keeps access | VP-RB-005 | denied | decided fresh | — |  |
| 4643 | Time-box break-glass access to four hours and log the grant | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 4644 | Cap analyzer retries at five with exponential backoff | VP-PO-010 | permitted | decided fresh | — |  |
| 4645 | Charge a release fee for a written prescription unless the client buys in-house | VP-CC-003 | denied | decided fresh | — |  |
| 4646 | Queue reminder sends so a retry storm cannot amplify | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4647 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 4648 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-006 | permitted | decided fresh | — |  |
| 4649 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-003 | permitted with conditions | decided fresh | — | ● |
| 4650 | Propose a sunset clause for the analytics pilot exception | VP-PH-003 | denied | decided fresh | — |  |
| 4651 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | decided fresh | — |  |
| 4652 | Verify commit signatures on the protected release branch | VP-SC-005 | permitted | decided fresh | — |  |
| 4653 | Require acknowledgement before a critical value page clears | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 4654 | Route a human review request from the decision detail page | VP-GV-003 | permitted | decided fresh | — |  |
| 4655 | Prove the backup restore before the vaccine index migration | VP-HA-001 | permitted | decided fresh | — |  |
| 4656 | Submit an amendment adding a welfare-inspection remediation window | VP-GV-003 | denied | decided fresh | — |  |
| 4657 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 4658 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4659 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-006 | permitted | decided fresh | — |  |
| 4660 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted | decided fresh | — |  |
| 4661 | Block record purges that fall inside the two-year retention term | VP-CS-012 | permitted | decided fresh | — |  |
| 4662 | Bump the HL7 parser to the patched upstream release | VP-SC-008 | permitted | decided fresh after a tie | none_tie |  |
| 4663 | Take record timestamps from the monotonic server clock | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 4664 | Apply the state retention schedule to inactive owner records | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 4665 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 4666 | Hide the admin buttons in the UI instead of checking server-side | VP-RB-008 | denied | decided fresh | — |  |
| 4667 | Match study patient identity on microchip and account number | VP-PO-007 | permitted | decided fresh | — |  |
| 4668 | Match study patient identity on microchip and account number | VP-PO-005 | permitted with conditions | decided fresh | — | ● |
| 4669 | Withhold prescription finalisation from technician accounts | VP-RB-008 | permitted | disposed by citation | — |  |
| 4670 | Add an immutability test for the dispensing log writer | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4671 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted | decided fresh after a tie | none_tie |  |
| 4672 | Add a keyboard path out of the consent modal's focus trap | VP-AX-001 | permitted with conditions | decided fresh | — | ● |
| 4673 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 4674 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-004 | permitted | decided fresh | — |  |
| 4675 | Block record purges that fall inside the two-year retention term | VP-CS-010 | permitted | decided fresh | — |  |
| 4676 | Pin the build runner image and make each job ephemeral | VP-SC-001 | permitted | decided fresh | — |  |
| 4677 | Bound the results reconciler retry loop | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4678 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted | decided fresh | — |  |
| 4679 | Drop internal identifiers from the public error envelope | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 4680 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-008 | permitted | decided fresh | — |  |
| 4681 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 4682 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | denied | bound by precedent | REC-S0124 |  |
| 4683 | Prompt for an off-label rationale in the medical record | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 4684 | Record who exported an audit bundle and when | VP-RR-004 | permitted | decided fresh | — |  |
| 4685 | Preserve the original entry when a chart amendment is filed | VP-RR-004 | permitted | decided fresh | — |  |
| 4686 | Parameterise the new chart-search query | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4687 | Make the audit table append-only at the database level | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4688 | Take record timestamps from the monotonic server clock | VP-RR-005 | permitted | decided fresh | — |  |
| 4689 | Record a manual screen-reader check for every new portal flow | VP-AX-002 | permitted | decided fresh | — |  |
| 4690 | Assign the daily audit review to the practice manager role | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4691 | Route anomalous dispensing alerts to a queue with no configured recipient | VP-DR-003 VP-PD-007 ⛔ | denied | refused at the floor | — |  |
| 4692 | Allowlist microchip identifier formats at the API boundary | VP-AS-005 | permitted | decided fresh | — |  |
| 4693 | Auto-close ketamine count mismatches under two millilitres | VP-CS-009 | denied | decided fresh | — |  |
| 4694 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 4695 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4696 | Replace the hand-rolled token hash with the vetted library | VP-AS-002 | permitted | disposed by citation | — |  |
| 4697 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4698 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-005 | permitted | decided fresh | — |  |
| 4699 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 4700 | Validate the PDMP payload against the state schema before submit | VP-CS-010 | permitted | decided fresh | — |  |
| 4701 | Attach build provenance to the practice API release artefact | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 4702 | Enable video-only exams for prescribing in every state | VP-VC-001 ⛔ | denied | refused at the floor | — |  |
| 4703 | Propose a sunset clause for the analytics pilot exception | VP-CS-008 | denied | decided fresh | — |  |
| 4704 | Quarantine unmatched analyzer results for technician review | VP-PO-009 | denied | bound by precedent | REC-S0116 |  |
| 4705 | Trim the owner breach-notice template down to a one-line summary | VP-BN-003 | denied | decided fresh | — |  |
| 4706 | Record artefact digests in the release ledger on publish | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 4707 | Add contract tests for the pinned HL7 v2 profile | VP-PO-010 | permitted with conditions | decided fresh | — | ● |
| 4708 | Redact owner email addresses from claims connector debug output | VP-PD-005 | permitted | decided fresh | — |  |
| 4709 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted | decided fresh | — |  |
| 4710 | Drop analyzer messages that fail to parse and move on | VP-PO-008 | denied | decided fresh | — |  |
| 4711 | Attach the standing declaration to every audit export | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 4712 | Let staff reassign a study to another patient in one click | VP-PO-009 | denied | decided fresh | — |  |
| 4713 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | decided fresh | — |  |
| 4714 | Bump the HL7 parser to the patched upstream release | VP-SC-008 | permitted | decided fresh | — |  |
| 4715 | Gate merges on a clean provenance verification step | VP-SC-007 | permitted | decided fresh | — | ● |
| 4716 | Bound the results reconciler retry loop | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4717 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 4718 | Validate species and body weight before computing the dosage | VP-VC-005 | permitted | decided fresh | — |  |
| 4719 | Pin the radiography panel firmware version in the device inventory | VP-PO-002 | permitted | decided fresh | — |  |
| 4720 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-002 | permitted | decided fresh | — |  |
| 4721 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4722 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-002 VP-SC-001 ⛔ | denied | refused at the floor | — |  |
| 4723 | Validate the PDMP payload against the state schema before submit | VP-CS-008 | permitted | decided fresh | — |  |
| 4724 | Assign the daily audit review to the practice manager role | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 4725 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-001 | permitted | decided fresh | — | ● |
| 4726 | Publish the contest counts in the audit export header | VP-RR-006 | permitted | decided fresh | — |  |
| 4727 | Fetch whatever callback URL the practice webhook supplies | VP-AS-002 | denied | decided fresh | — |  |
| 4728 | Have the agent refactor the controlled dispensing rules engine | VP-AI-006 | denied | decided fresh | — |  |
| 4729 | Derive tenant id from the session, never from a request header | VP-RB-007 | permitted | decided fresh | — |  |
| 4730 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-002 | permitted | decided fresh | — |  |
| 4731 | Attach the standing declaration to every audit export | VP-RR-007 | permitted | decided fresh | — |  |
| 4732 | Take record timestamps from the monotonic server clock | VP-RR-007 | permitted | decided fresh | — |  |
| 4733 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4734 | Link the breach notification runbook from the incident template | VP-PD-006 | permitted | decided fresh | — | ● |
| 4735 | Restrict agent outbound calls to the allowlisted host set | VP-AI-006 | permitted | decided fresh | — |  |
| 4736 | Strip untrusted ticket text from the agent's instruction context | VP-AI-006 | permitted | decided fresh | — |  |
| 4737 | Require staff-verified ownership before a microchip's registered owner can change | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 4738 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 4739 | Bind each service account to a single practice id | VP-RB-005 | permitted | disposed by citation | — |  |
| 4740 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4741 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted | decided fresh | — |  |
| 4742 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted with conditions | decided fresh | — | ● |
| 4743 | Match study patient identity on microchip and account number | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 4744 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-007 | permitted | decided fresh | — |  |
| 4745 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4746 | Verify the signer's licence status before a rabies certificate can be issued | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 4747 | Bump the HL7 parser to the patched upstream release | VP-SC-004 | permitted | decided fresh | — |  |
| 4748 | Block record purges that fall inside the two-year retention term | VP-CS-010 | permitted | decided fresh | — |  |
| 4749 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | permitted | decided fresh | — |  |
| 4750 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-GV-007 | denied | decided fresh | — |  |
| 4751 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-002 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 4752 | Let the password alone sign an e-prescription when the token times out | VP-CS-008 | denied | decided fresh | — |  |
| 4753 | Scope the new reporting role to read-only endpoints | VP-RB-007 | permitted | decided fresh | — |  |
| 4754 | Drop internal identifiers from the public error envelope | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 4755 | Require an explicit share grant for cross-practice referrals | VP-RB-005 | permitted | decided fresh | — | ● |
| 4756 | Let the coding agent rewrite the session authentication middleware | VP-AI-005 | denied | decided fresh | — |  |
| 4757 | Return a correlation id instead of a stack trace on error | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 4758 | Expose the radiography panel to the internet for vendor support | VP-PO-004 | denied | decided fresh | — |  |
| 4759 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — |  |
| 4760 | Record the prompt and context hash on the agent's pull request | VP-AI-008 | permitted | decided fresh | — |  |
| 4761 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-008 | permitted | decided fresh | — |  |
| 4762 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-007 | permitted | decided fresh | — | ● |
| 4763 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 4764 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 4765 | Check consent currency before the reminder engine sends | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 4766 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-006 | permitted | decided fresh | — |  |
| 4767 | Take record timestamps from the monotonic server clock | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 4768 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-001 VP-SC-008 ⛔ | denied | refused at the floor | — |  |
| 4769 | Auto-fill the physical inventory count from the running ledger balance | VP-DR-003 VP-PH-004 ⛔ | denied | refused at the floor | — |  |
| 4770 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 4771 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-VC-005 ⛔ | denied | refused at the floor | — |  |
| 4772 | Assign a named reviewer to the vendored DICOM parser | VP-SC-003 | permitted | disposed by citation | — |  |
| 4773 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | permitted | decided fresh | — | ● |
| 4774 | Enable video-only exams for prescribing in every state | VP-VC-007 | denied | decided fresh | — |  |
| 4775 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted | decided fresh | — |  |
| 4776 | Match study patient identity on microchip and account number | VP-PO-008 | permitted with conditions | decided fresh | — | ● |
| 4777 | Make the loss-discovery timestamp immutable once the theft report is filed | VP-DR-004 | permitted | decided fresh | — |  |
| 4778 | Allowlist microchip identifier formats at the API boundary | VP-AS-004 | permitted | decided fresh | — |  |
| 4779 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 4780 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-007 | permitted | decided fresh | — |  |
| 4781 | Gate merges on a clean provenance verification step | VP-SC-004 | permitted | decided fresh | — |  |
| 4782 | Pin the radiography panel firmware version in the device inventory | VP-PO-004 | permitted with conditions | decided fresh | — | ● |
| 4783 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 4784 | Require a verified adult guardian before a minor's client account can be created | VP-CC-002 | permitted | decided fresh | — |  |
| 4785 | Waive the records-copy fee for a client's own written prescription request | VP-CC-002 | permitted | decided fresh | — |  |
| 4786 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — |  |
| 4787 | Pin the build runner image and make each job ephemeral | VP-SC-007 | permitted with conditions | decided fresh | — | ● |
| 4788 | Publish the contest counts in the audit export header | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4789 | Attach build provenance to the practice API release artefact | VP-SC-004 | permitted | decided fresh | — |  |
| 4790 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-011 | permitted | decided fresh | — |  |
| 4791 | Cap analyzer retries at five with exponential backoff | VP-PO-009 | permitted | decided fresh | — |  |
| 4792 | Move the release outside the emergency-hours freeze window | VP-HA-003 | permitted | decided fresh | — |  |
| 4793 | Renumber the point-of-care provisions after the device policy merge | VP-PO-008 | denied | decided fresh | — |  |
| 4794 | Give wellness-plan cancellation the same number of steps as enrolment | VP-CC-002 | permitted | decided fresh | — |  |
| 4795 | Prove the backup restore before the vaccine index migration | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4796 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 4797 | Let the password alone sign an e-prescription when the token times out | VP-CS-006 VP-RB-004 ⛔ | denied | refused at the floor | — |  |
| 4798 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted | decided fresh | — |  |
| 4799 | Bound the data subject export job to the statutory window | VP-PD-003 | permitted | decided fresh | — |  |
| 4800 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 4801 | Remove the expiry from break-glass grants so support keeps access | VP-RB-005 | denied | decided fresh | — |  |
| 4802 | Check object ownership before returning a patient chart | VP-RB-006 | permitted | decided fresh | — |  |
| 4803 | Require the veterinary care plan on the regulated facility record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 4804 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-002 | permitted | decided fresh | — |  |
| 4805 | Write a docket entry for every uncharged arrival | VP-GV-003 | permitted | decided fresh | — |  |
| 4806 | Drop internal identifiers from the public error envelope | VP-AS-005 | permitted | decided fresh | — |  |
| 4807 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-003 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 4808 | Scope modality worklist queries to the requesting practice | VP-PO-007 | permitted | decided fresh | — |  |
| 4809 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted | decided fresh | — |  |
| 4810 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | decided fresh | — |  |
| 4811 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-RR-002 | denied | decided fresh | — |  |
| 4812 | Turn off signature enforcement on main to unblock the release train | VP-SC-004 | denied | decided fresh | — |  |
| 4813 | Cover the new boarding endpoint with a role check test | VP-RB-006 | permitted | decided fresh | — |  |
| 4814 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 4815 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 4816 | Populate DICOM species and breed tags from the patient record | VP-PO-002 | permitted with conditions | bound by precedent | REC-S0096 |  |
| 4817 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted with conditions | decided fresh | — | ● |
| 4818 | Cap the records-copy fee at the state's statutory maximum | VP-CC-002 | permitted | decided fresh | — |  |
| 4819 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-002 | permitted | decided fresh | — |  |
| 4820 | Tokenise the card number before the invoice row is written | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 4821 | Block procedure sign-off by roles outside the delegated scope | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 4822 | Add an immutability test for the dispensing log writer | VP-RR-007 | permitted | decided fresh | — |  |
| 4823 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 4824 | Infer the prescriber from the last clinician to open the chart | VP-CS-004 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 4825 | Sanitise filenames in the lab attachment upload handler | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 4826 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4827 | Flag food-animal status on the patient banner before dispensing | VP-VC-007 | permitted | decided fresh | — |  |
| 4828 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 4829 | Revalidate the active session after a privilege change | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 4830 | Move threshold parameters into the legislated configuration | VP-GV-006 | permitted | decided fresh | — |  |
| 4831 | Add an immutability test for the dispensing log writer | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4832 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4833 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 4834 | Log the authenticated prescriber id on each dispensing event | VP-CS-009 | permitted | decided fresh | — |  |
| 4835 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-009 | permitted | decided fresh | — |  |
| 4836 | Store the amendment author alongside the superseded text | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4837 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted | decided fresh | — |  |
| 4838 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-001 VP-SC-007 ⛔ | denied | refused at the floor | — |  |
| 4839 | Raise the p95 latency budget from ten to twenty-five percent | VP-PD-006 | denied | decided fresh | — |  |
| 4840 | Attach build provenance to the practice API release artefact | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 4841 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted | decided fresh | — |  |
| 4842 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-008 | permitted | decided fresh | — |  |
| 4843 | Treat a portal login as e-signature consent for electronic records | VP-CC-003 | denied | decided fresh | — | ● |
| 4844 | Strip the standing declaration from the audit bundle header | VP-GV-001 ⛔ | denied | refused at the floor | — |  |
| 4845 | Suppress reminder sends to any number that has already replied STOP | VP-CC-005 | permitted | decided fresh | — |  |
| 4846 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted | decided fresh | — |  |
| 4847 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4848 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4849 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4850 | Drop the practice filter from the referral search endpoint | VP-RB-008 | denied | decided fresh | — |  |
| 4851 | Match study patient identity on microchip and account number | VP-PO-003 | permitted | decided fresh | — |  |
| 4852 | Require an explicit share grant for cross-practice referrals | VP-RB-003 | permitted | decided fresh | — |  |
| 4853 | Require acknowledgement before a critical value page clears | VP-PO-009 | permitted | decided fresh | — |  |
| 4854 | Restrict claim payload deserialisation to known types | VP-AS-001 | permitted | decided fresh | — |  |
| 4855 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-002 | permitted | decided fresh | — |  |
| 4856 | Quarantine unmatched analyzer results for technician review | VP-PO-002 | permitted | decided fresh | — |  |
| 4857 | Run the secret scanner over the diff in pre-merge CI | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 4858 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4859 | Scope modality worklist queries to the requesting practice | VP-PO-007 | permitted | decided fresh | — |  |
| 4860 | Check object ownership before returning a patient chart | VP-RB-006 | permitted | decided fresh | — |  |
| 4861 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh | — |  |
| 4862 | Add the boarding service to the critical-service list in policy | VP-RB-008 | denied | decided fresh | — |  |
| 4863 | Require a named human reviewer on every agent-authored pull request | VP-AI-003 | permitted | decided fresh | — | ● |
| 4864 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 4865 | Cap analyzer retries at five with exponential backoff | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 4866 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-009 | denied | decided fresh | — |  |
| 4867 | Generate decision rationales from the outcome at export time | VP-RR-001 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 4868 | Add regression tests for the note-render encoding path | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4869 | Hand the checkout redirect to the validated payment processor | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 4870 | Prove the backup restore before the vaccine index migration | VP-HA-001 | permitted | decided fresh | — |  |
| 4871 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-005 | permitted | decided fresh | — |  |
| 4872 | Verify commit signatures on the protected release branch | VP-SC-004 | permitted | decided fresh | — |  |
| 4873 | Call an external summarisation API from the agent's new helper | VP-AI-003 | denied | decided fresh | — | ● |
| 4874 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 4875 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-002 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 4876 | Point the resolver at the private registry before the public one | VP-SC-007 | permitted | decided fresh | — |  |
| 4877 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-GV-005 ⛔ | denied | refused at the floor | — |  |
| 4878 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4879 | Hand the checkout redirect to the validated payment processor | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 4880 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 4881 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | permitted | decided fresh | — | ● |
| 4882 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-008 | permitted | decided fresh | — |  |
| 4883 | Require a currently licensed veterinarian's credential to sign a rabies certificate | VP-PH-002 | permitted | decided fresh | — |  |
| 4884 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted | decided fresh | — |  |
| 4885 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted | decided fresh | — |  |
| 4886 | Allow payment-plan enrolment from an unverified under-eighteen account | VP-CC-002 | denied | decided fresh | — |  |
| 4887 | Add an immutability test for the dispensing log writer | VP-RR-003 | permitted | decided fresh | — |  |
| 4888 | Publish the contest counts in the audit export header | VP-RR-003 | permitted | decided fresh | — |  |
| 4889 | Prove the backup restore before the vaccine index migration | VP-HA-006 | permitted | docketed — not charged | — |  |
| 4890 | Drop failed microchip registry submissions without surfacing an error | VP-PH-003 | denied | decided fresh | — |  |
| 4891 | Replicate the Dublin clinic's owner tables to the US warehouse | VP-PD-002 VP-PO-009 ⛔ | denied | refused at the floor | — |  |
| 4892 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 4893 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 4894 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4895 | Attach build provenance to the practice API release artefact | VP-SC-004 | permitted | decided fresh | — | ● |
| 4896 | Hardcode the reference lab API key in the connector config | VP-SC-008 | denied | decided fresh | — |  |
| 4897 | Pin the build runner image and make each job ephemeral | VP-SC-001 | permitted | decided fresh | — |  |
| 4898 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-009 | permitted | decided fresh | — | ● |
| 4899 | Scope modality worklist queries to the requesting practice | VP-PO-004 | permitted | decided fresh | — |  |
| 4900 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 4901 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted | decided fresh | — |  |
| 4902 | Parameterise the new chart-search query | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4903 | Add the boarding service to the critical-service list in policy | VP-AS-002 | denied | decided fresh | — |  |
| 4904 | Auto-fill the physical inventory count from the running ledger balance | VP-DR-002 VP-VC-005 ⛔ | denied | refused at the floor | — |  |
| 4905 | Trim the reportable-condition list to cut down on staff alert fatigue | VP-PH-001 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 4906 | Release medical records regardless of outstanding balance | VP-CC-003 | permitted | decided fresh | — |  |
| 4907 | Add an accessible name to the new custom toggle control | VP-AX-002 | permitted | decided fresh | — |  |
| 4908 | Attach the standing declaration to every audit export | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 4909 | Bump the HL7 parser to the patched upstream release | VP-SC-003 | permitted | decided fresh | — |  |
| 4910 | Gate merges on a clean provenance verification step | VP-SC-003 | permitted | decided fresh | — |  |
| 4911 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 4912 | Raise the p95 latency budget from ten to twenty-five percent | VP-AS-003 | denied | decided fresh | — |  |
| 4913 | Replace the hand-rolled token hash with the vetted library | VP-AS-004 | permitted | decided fresh | — | ● |
| 4914 | Require the veterinary care plan on the regulated facility record | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4915 | Show the technician's credential status on the surgery board | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 4916 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | disposed by citation | — |  |
| 4917 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4918 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted | disposed by citation | — |  |
| 4919 | Lower the changed-line coverage threshold in the policy repo | VP-RB-005 | denied | decided fresh | — |  |
| 4920 | Run the secret scanner over the diff in pre-merge CI | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 4921 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | decided fresh | — |  |
| 4922 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4923 | Apply the state retention schedule to inactive owner records | VP-PD-005 | permitted | decided fresh | — |  |
| 4924 | Redact owner email addresses from claims connector debug output | VP-PD-005 | permitted | decided fresh | — |  |
| 4925 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 4926 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-002 | permitted | decided fresh | — |  |
| 4927 | Restrict claim payload deserialisation to known types | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4928 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | decided fresh | — |  |
| 4929 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-002 VP-CS-012 ⛔ | denied | refused at the floor | — |  |
| 4930 | Stagger analyzer polling to flatten the morning load peak | VP-HA-003 | permitted | decided fresh | — |  |
| 4931 | Add contract tests for the pinned HL7 v2 profile | VP-PO-010 | permitted | decided fresh | — |  |
| 4932 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-006 | permitted | docketed — not charged | — |  |
| 4933 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | decided fresh | — | ● |
| 4934 | Pin the radiography panel firmware version in the device inventory | VP-PO-002 | permitted | decided fresh | — |  |
| 4935 | Pin the radiography panel firmware version in the device inventory | VP-PO-002 | permitted | decided fresh | — |  |
| 4936 | Move the release outside the emergency-hours freeze window | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4937 | Allowlist microchip identifier formats at the API boundary | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4938 | Ship a down-migration for the visit-summary table change | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4939 | Reject malformed segments without committing a partial patient write | VP-PO-007 | permitted | decided fresh | — |  |
| 4940 | Enforce authorisation server-side on the discharge summary route | VP-AS-009 | permitted | docketed — not charged | — |  |
| 4941 | Version chart amendments instead of editing rows in place | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 4942 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-SC-001 ⛔ | denied | refused at the floor | — |  |
| 4943 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 4944 | Run semantic analysis over the agent diff in CI | VP-AI-003 | permitted | decided fresh | — |  |
| 4945 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-007 | permitted | decided fresh | — |  |
| 4946 | Add an immutability test for the dispensing log writer | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 4947 | Let a technician account sign the rabies certificate when the vet is busy | VP-PH-001 VP-RB-004 ⛔ | denied | refused at the floor | — |  |
| 4948 | Replace the hand-rolled token hash with the vetted library | — | permitted | docketed — nothing engaged | — |  |
| 4949 | Add regression tests for the note-render encoding path | VP-AS-008 | permitted | docketed — not charged | — |  |
| 4950 | Block agent branches from touching the compliance test suite | VP-AI-004 | permitted | decided fresh | — |  |
| 4951 | Verify every imported package resolves in the registry before merge | VP-AI-004 | permitted | decided fresh | — |  |
| 4952 | Attach the full triage transcript to the patient's medical record | VP-PS-002 | permitted | decided fresh | — |  |
| 4953 | Strip untrusted ticket text from the agent's instruction context | VP-AI-007 | permitted | decided fresh | — |  |
| 4954 | Warn when a dose falls outside the labelled species range | VP-VC-008 | permitted | decided fresh | — |  |
| 4955 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 4956 | Pin the build runner image and make each job ephemeral | VP-SC-007 | permitted with conditions | decided fresh | — | ● |
| 4957 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-007 | denied | bound by precedent | REC-S0126 |  |
| 4958 | Show the technician's credential status on the surgery board | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 4959 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-005 | permitted | decided fresh | — |  |
| 4960 | Replace the hand-rolled token hash with the vetted library | VP-AS-005 | permitted | decided fresh | — |  |
| 4961 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-008 | permitted | decided fresh | — |  |
| 4962 | Redact owner email addresses from claims connector debug output | VP-PD-008 | permitted | decided fresh | — |  |
| 4963 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-006 | permitted | decided fresh | — | ● |
| 4964 | Sanitise filenames in the lab attachment upload handler | VP-AS-007 | permitted | docketed — not charged | — |  |
| 4965 | Revalidate the active session after a privilege change | VP-RB-006 | permitted | decided fresh | — |  |
| 4966 | Accept any microchip number the intake form receives without a format check | VP-PH-003 | denied | decided fresh | — |  |
| 4967 | Add tests proving retrieval never reads the audit register | VP-GV-003 | permitted | decided fresh | — |  |
| 4968 | Stagger analyzer polling to flatten the morning load peak | VP-HA-001 | permitted | decided fresh | — |  |
| 4969 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted | decided fresh | — |  |
| 4970 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-011 | permitted | decided fresh | — |  |
| 4971 | Block procedure sign-off by roles outside the delegated scope | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 4972 | Drop internal identifiers from the public error envelope | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 4973 | Add the new charting library licence to the allowlist | VP-SC-003 | permitted | decided fresh | — |  |
| 4974 | Gate merges on a clean provenance verification step | VP-SC-001 | permitted | decided fresh | — | ● |
| 4975 | Require a verified adult guardian before a minor's client account can be created | VP-CC-003 | permitted | decided fresh | — | ● |
| 4976 | Let the coding agent rewrite the session authentication middleware | VP-AI-001 ⛔ | denied | refused at the floor | — |  |
| 4977 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 4978 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-012 | permitted | decided fresh | — |  |
| 4979 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | decided fresh | — |  |
| 4980 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-007 | permitted | decided fresh | — |  |
| 4981 | Cap analyzer retries at five with exponential backoff | VP-PO-007 | permitted | decided fresh | — |  |
| 4982 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 4983 | Allowlist microchip identifier formats at the API boundary | VP-AS-004 | permitted | decided fresh | — |  |
| 4984 | Record a named owner and outcome on every breach-drill result | VP-BN-003 | permitted | decided fresh | — |  |
| 4985 | Document the degraded path when the reference lab is down | VP-HA-005 | permitted | docketed — not charged | — |  |
| 4986 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | decided fresh | — |  |
| 4987 | Time-box break-glass access to four hours and log the grant | VP-RB-004 | permitted | decided fresh | — |  |
| 4988 | Enable the portal's credential-stuffing detector on client login | VP-BN-002 | permitted | decided fresh | — |  |
| 4989 | Offer a non-visual alternative alongside the check-in captcha | VP-AX-001 | permitted | decided fresh | — |  |
| 4990 | Cap analyzer retries at five with exponential backoff | VP-PO-007 | permitted | decided fresh | — |  |
| 4991 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh | — |  |
| 4992 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 4993 | Cap the records-copy fee at the state's statutory maximum | VP-CC-004 | permitted | decided fresh | — |  |
| 4994 | Move the authorisation decision out of the portal frontend | VP-RB-007 | permitted | disposed by citation | — |  |
| 4995 | Derive tenant id from the session, never from a request header | VP-RB-002 | permitted | decided fresh | — |  |
| 4996 | Record artefact digests in the release ledger on publish | VP-SC-008 | permitted | decided fresh | — |  |
| 4997 | Drop the runbook link from the detection alert payload to shorten it | VP-BN-001 VP-PD-009 ⛔ | denied | refused at the floor | — |  |
| 4998 | Block agent branches from touching the compliance test suite | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 4999 | Use the client-supplied filename as the attachment storage path | VP-AS-002 | denied | decided fresh | — |  |
| 5000 | Confirm every disease-report dispatch with the receiving official's acknowledgement | VP-PH-004 | permitted | decided fresh | — |  |
| 5001 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-004 | permitted | decided fresh | — |  |
| 5002 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | decided fresh | — |  |
| 5003 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted | decided fresh | — |  |
| 5004 | Document the degraded path when the reference lab is down | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5005 | Serialise inventory decrements with a row-level lock | VP-HA-001 | permitted | decided fresh | — |  |
| 5006 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 5007 | Pin the radiography panel firmware version in the device inventory | VP-PO-010 | permitted | decided fresh | — |  |
| 5008 | Validate delegated task lists against the state practice act table | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5009 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5010 | Add contract tests for the pinned HL7 v2 profile | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 5011 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 5012 | Match study patient identity on microchip and account number | VP-PO-003 | permitted | decided fresh | — |  |
| 5013 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 5014 | Block procedure sign-off by roles outside the delegated scope | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 5015 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5016 | Let the adjudication service tune its own charging threshold at runtime | VP-GV-002 VP-CC-005 ⛔ | denied | refused at the floor | — |  |
| 5017 | Match the required supervision level to the task's risk tier | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 5018 | Include the weekly reporter bulletin in the adjudicator's context | VP-GV-003 | denied | decided fresh | — |  |
| 5019 | Write the decision rationale at resolution time, not on export | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5020 | Require an explicit share grant for cross-practice referrals | VP-RB-003 | permitted | decided fresh | — |  |
| 5021 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-005 | permitted | decided fresh | — |  |
| 5022 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 5023 | Require an explicit owner choice before remains disposition can be saved | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 5024 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-008 | permitted | decided fresh | — |  |
| 5025 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 5026 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5027 | Add permutation tests across the role-permission matrix | VP-RB-006 | permitted | decided fresh | — |  |
| 5028 | Update the manifest and lockfile in the same commit | VP-SC-004 | permitted | decided fresh | — |  |
| 5029 | Replace the hand-rolled token hash with the vetted library | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5030 | Raise the p95 latency budget from ten to twenty-five percent | VP-RB-004 | denied | decided fresh | — |  |
| 5031 | Release medical records regardless of outstanding balance | VP-CC-003 | permitted | decided fresh | — |  |
| 5032 | Require acknowledgement before a critical value page clears | VP-PO-007 | permitted | decided fresh | — |  |
| 5033 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-PO-002 | denied | decided fresh | — |  |
| 5034 | Skip the consent check for the lapsed-client reactivation text campaign | VP-CC-001 ⛔ | denied | refused at the floor | — |  |
| 5035 | Pin the build runner image and make each job ephemeral | VP-SC-003 | permitted | decided fresh | — |  |
| 5036 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | permitted | decided fresh | — |  |
| 5037 | Bump the HL7 parser to the patched upstream release | VP-SC-001 | permitted | decided fresh | — |  |
| 5038 | Start the breach-notice timer at confirmed root cause instead of first detection | VP-BN-001 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 5039 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5040 | Calculate the extended withdrawal interval when the order is saved | VP-VC-008 | permitted | decided fresh | — |  |
| 5041 | Remove the necessity note from the bulk compounding form | VP-VC-003 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 5042 | Load test the triage queue at a hundred concurrent clinicians | — | permitted | docketed — nothing engaged | — |  |
| 5043 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted | decided fresh | — |  |
| 5044 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted | decided fresh | — |  |
| 5045 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5046 | Warn when a dose falls outside the labelled species range | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 5047 | Return a correlation id instead of a stack trace on error | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5048 | Move the release outside the emergency-hours freeze window | VP-HA-003 | permitted | decided fresh | — |  |
| 5049 | Make the feed directive expiry date a mandatory field | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 5050 | Store payment references, not card numbers, on the retry queue | VP-PD-005 | permitted | decided fresh | — |  |
| 5051 | Drop the practice filter from the referral search endpoint | VP-RB-006 | denied | decided fresh | — |  |
| 5052 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-009 | denied | decided fresh | — |  |
| 5053 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted | decided fresh | — | ● |
| 5054 | Update the manifest and lockfile in the same commit | VP-SC-001 | permitted with conditions | decided fresh | — | ● |
| 5055 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 5056 | Add the boarding service to the critical-service list in policy | VP-AS-003 | denied | decided fresh | — |  |
| 5057 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-002 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 5058 | Track welfare inspection findings to a remediation due date | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5059 | Populate DICOM species and breed tags from the patient record | VP-PO-003 | permitted with conditions | decided fresh | — | ● |
| 5060 | Make the audit table append-only at the database level | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 5061 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-003 | permitted | decided fresh | — |  |
| 5062 | Replace the hand-rolled token hash with the vetted library | VP-AS-003 | permitted | decided fresh | — |  |
| 5063 | Raise the tramadol refill cap to twelve for chronic pain clients | VP-CS-002 VP-AS-005 ⛔ | denied | refused at the floor | — |  |
| 5064 | Trust the modality's patient identifier tag exactly as sent | VP-PO-003 | denied | decided fresh | — |  |
| 5065 | Remove the species dose-range override button that predates the current safety gate | VP-PS-002 | permitted | decided fresh | — |  |
| 5066 | Drop analyzer messages that fail to parse and move on | VP-PO-008 | denied | decided fresh | — |  |
| 5067 | Scope modality worklist queries to the requesting practice | VP-PO-004 | permitted | decided fresh | — |  |
| 5068 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-010 | permitted | decided fresh | — |  |
| 5069 | Review agent-authored tests for tautological assertions | VP-AI-003 | permitted | decided fresh | — |  |
| 5070 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-007 | permitted | decided fresh | — |  |
| 5071 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-004 ⛔ | denied | refused at the floor | — |  |
| 5072 | Generate decision rationales from the outcome at export time | VP-RR-001 VP-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5073 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5074 | Drop internal identifiers from the public error envelope | VP-AS-003 | permitted | disposed by citation | — |  |
| 5075 | Validate delegated task lists against the state practice act table | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 5076 | Show the six-month validity window on the refill request screen | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 5077 | Check object ownership before returning a patient chart | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 5078 | Serialise inventory decrements with a row-level lock | VP-HA-002 | permitted | decided fresh | — |  |
| 5079 | Expose the contest path to the owner, not only to staff | VP-GV-006 | permitted | decided fresh | — |  |
| 5080 | Publish the contest outcome as granted and refused counts | VP-GV-006 | permitted | decided fresh | — |  |
| 5081 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5082 | Remove the two-person rule for EPCS grants from the policy repo | VP-PO-004 | denied | decided fresh | — |  |
| 5083 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 5084 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-002 VP-AI-008 ⛔ | denied | refused at the floor | — |  |
| 5085 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-012 | permitted | decided fresh | — | ● |
| 5086 | Record who exported an audit bundle and when | VP-RR-002 | permitted | decided fresh | — |  |
| 5087 | Record who exported an audit bundle and when | VP-RR-002 | permitted | decided fresh | — |  |
| 5088 | Allow payment-plan enrolment from an unverified under-eighteen account | VP-CC-005 | denied | decided fresh | — | ● |
| 5089 | Move the CVSS threshold from seven to eight in the dependency policy | VP-PD-004 | denied | decided fresh | — |  |
| 5090 | Add an immutability test for the dispensing log writer | VP-RR-004 | permitted | decided fresh | — |  |
| 5091 | Add the new charting library licence to the allowlist | VP-SC-008 | permitted | disposed by citation | — |  |
| 5092 | Add an immutability test for the dispensing log writer | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5093 | Extend order-form record retention to cover the full two-year floor | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 5094 | Let staff issue standing scripts without opening the patient record | VP-CS-005 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 5095 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 5096 | Scope modality worklist queries to the requesting practice | VP-PO-003 | permitted | decided fresh | — | ● |
| 5097 | Shorten the break-glass expiry constant in the rulebook | VP-VC-006 | denied | decided fresh | — |  |
| 5098 | Record the analgesia rationale when a plan is declined | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 5099 | Let the signup form create a client account without checking the applicant's age | VP-CC-006 | denied | decided fresh | — |  |
| 5100 | Suppress the theft-and-loss alert when the missing count is under a configurable threshold | VP-DR-001 ⛔ | denied | refused at the floor | — |  |
| 5101 | Rank retrieval candidates using the audit register's findings | VP-GV-006 | denied | decided fresh | — |  |
| 5102 | Capture the research protocol number on regulated-facility visits | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5103 | Tokenise the card number before the invoice row is written | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 5104 | Match study patient identity on microchip and account number | VP-PO-005 | permitted | decided fresh | — |  |
| 5105 | Scope modality worklist queries to the requesting practice | VP-PO-005 | permitted | decided fresh | — |  |
| 5106 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-007 | permitted | decided fresh | — |  |
| 5107 | Quarantine unmatched analyzer results for technician review | VP-PO-006 | permitted | decided fresh | — |  |
| 5108 | Stagger analyzer polling to flatten the morning load peak | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5109 | Release medical records regardless of outstanding balance | VP-CC-004 | permitted | decided fresh | — |  |
| 5110 | Move the authorisation decision out of the portal frontend | VP-RB-002 | permitted | decided fresh | — |  |
| 5111 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | decided fresh | — |  |
| 5112 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — |  |
| 5113 | Add the new charting library licence to the allowlist | VP-SC-009 | permitted | decided fresh | — |  |
| 5114 | Run the secret scanner over the diff in pre-merge CI | VP-SC-004 | permitted | decided fresh | — |  |
| 5115 | Overwrite the original diagnosis text when a chart is amended | VP-RR-005 | denied | decided fresh | — |  |
| 5116 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 5117 | Enforce authorisation server-side on the discharge summary route | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5118 | Update the manifest and lockfile in the same commit | VP-SC-002 | permitted | decided fresh | — |  |
| 5119 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5120 | Give consent withdrawal the same one-click path as granting it | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 5121 | Keep the retention clock unchanged when a record is edited | VP-RR-006 | permitted | decided fresh | — |  |
| 5122 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | decided fresh | — |  |
| 5123 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted | decided fresh | — |  |
| 5124 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-PD-005 | denied | decided fresh | — |  |
| 5125 | Add a breach-notice clause to the standard vendor contract template | VP-BN-003 | permitted | decided fresh | — | ● |
| 5126 | Point the resolver at the private registry before the public one | VP-SC-001 | permitted | decided fresh | — |  |
| 5127 | Attach the standing declaration to every audit export | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 5128 | Check the version token on clinical note writes | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5129 | Block record purges that fall inside the two-year retention term | VP-CS-011 | permitted | decided fresh | — |  |
| 5130 | Ship the boarding availability endpoint without a role check | VP-RB-001 VP-VC-006 ⛔ | denied | refused at the floor | — |  |
| 5131 | Warn when an anaesthesia monitoring gap exceeds the protocol | VP-AW-004 | permitted | decided fresh | — |  |
| 5132 | Let staff proceed with euthanasia before the consent form is saved | VP-PS-004 VP-PD-009 ⛔ | denied | refused at the floor | — |  |
| 5133 | Withhold prescription finalisation from technician accounts | VP-RB-003 | permitted | decided fresh | — |  |
| 5134 | Change the escalation ladder so the third tier is final | VP-CC-003 | denied | decided fresh | — |  |
| 5135 | Quarantine unmatched analyzer results for technician review | VP-PO-004 | permitted with conditions | decided fresh | — | ● |
| 5136 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-006 VP-RB-006 ⛔ | denied | refused at the floor | — |  |
| 5137 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | decided fresh | — |  |
| 5138 | Review agent-authored tests for tautological assertions | VP-AI-006 | permitted | decided fresh | — |  |
| 5139 | Add an immutability test for the dispensing log writer | VP-RR-004 | permitted | decided fresh | — |  |
| 5140 | Restore session objects by deserialising the client-supplied blob | VP-AS-003 | denied | decided fresh | — |  |
| 5141 | Rank retrieval candidates using the audit register's findings | VP-GV-006 | denied | decided fresh | — |  |
| 5142 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-PO-010 | denied | decided fresh | — |  |
| 5143 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-005 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 5144 | Let the password alone sign an e-prescription when the token times out | VP-CS-006 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 5145 | Drop the practice filter from the referral search endpoint | VP-RB-001 VP-VC-006 ⛔ | denied | refused at the floor | — |  |
| 5146 | Replace the critical-value acknowledgement page with a passive dashboard badge | VP-PS-003 | denied | decided fresh | — |  |
| 5147 | Add contract tests for the pinned HL7 v2 profile | VP-PO-006 | permitted | decided fresh | — |  |
| 5148 | Scope modality worklist queries to the requesting practice | VP-PO-006 | permitted | decided fresh | — |  |
| 5149 | Honour opt-out state at export time in the marketing job | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5150 | Extend the log redaction filter to the new owner phone field | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 5151 | Point the resolver at the private registry before the public one | VP-SC-005 | denied | bound by precedent | REC-S0154 |  |
| 5152 | Add the transport welfare checklist to the boarding intake form | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5153 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-005 ⛔ | denied | refused at the floor | — |  |
| 5154 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5155 | Encode clinical note text before rendering it in the portal | VP-AS-002 | permitted | disposed by citation | — |  |
| 5156 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5157 | Generate decision rationales from the outcome at export time | VP-RR-001 ⛔ | denied | refused at the floor | — |  |
| 5158 | Read the practice id from the X-Practice request header | VP-RB-004 | denied | decided fresh | — |  |
| 5159 | Stagger analyzer polling to flatten the morning load peak | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5160 | Enforce authorisation server-side on the discharge summary route | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5161 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 5162 | Run agent-generated code inside the sandboxed runner only | VP-AI-007 | permitted | decided fresh | — |  |
| 5163 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 5164 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 5165 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-009 | permitted | decided fresh | — |  |
| 5166 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted with conditions | bound by precedent | REC-S0092 |  |
| 5167 | Enforce the tenant scope in the query layer, not the handler | VP-RB-004 | permitted | decided fresh | — |  |
| 5168 | Drop the practice filter from the referral search endpoint | VP-RB-008 | denied | decided fresh | — |  |
| 5169 | Trim the contest counts from the audit export header | VP-RR-003 | denied | decided fresh | — |  |
| 5170 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 5171 | Add the new charting library licence to the allowlist | VP-SC-001 | permitted | decided fresh | — |  |
| 5172 | Pin the build runner image and make each job ephemeral | VP-SC-001 | permitted | decided fresh | — |  |
| 5173 | Block record purges that fall inside the two-year retention term | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 5174 | Swap the date library for a fork published by an unknown account | VP-SC-003 | denied | decided fresh | — |  |
| 5175 | Bind each service account to a single practice id | VP-RB-005 | permitted | decided fresh | — | ● |
| 5176 | Sanitise filenames in the lab attachment upload handler | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5177 | Quarantine unmatched analyzer results for technician review | VP-PO-003 | permitted | decided fresh | — |  |
| 5178 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 5179 | Redact owner email addresses from claims connector debug output | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 5180 | Prompt for an off-label rationale in the medical record | VP-VC-004 | permitted | decided fresh | — |  |
| 5181 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-009 | permitted | decided fresh | — |  |
| 5182 | Unblock enrofloxacin ordering for dairy herds | VP-VC-005 | denied | decided fresh | — |  |
| 5183 | Attach a residue risk assessment to the food-animal order form | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 5184 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5185 | Parameterise the new chart-search query | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5186 | Turn off audit writes on the hot dispensing path | VP-RR-001 ⛔ | denied | refused at the floor | — |  |
| 5187 | Restrict agent outbound calls to the allowlisted host set | VP-AI-005 | permitted | decided fresh | — |  |
| 5188 | Capture the veterinarian's sign-off on clinical logic changes | VP-AI-005 | permitted | decided fresh | — |  |
| 5189 | Serialise inventory decrements with a row-level lock | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5190 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-PH-003 ⛔ | denied | refused at the floor | — |  |
| 5191 | Remove the necessity note from the bulk compounding form | VP-VC-002 VP-AS-002 ⛔ | denied | refused at the floor | — |  |
| 5192 | Drop the practice filter from the referral search endpoint | VP-RB-001 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 5193 | Record the analgesia rationale when a plan is declined | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 5194 | Add the new charting library licence to the allowlist | VP-SC-004 | denied | bound by precedent | REC-S0124 |  |
| 5195 | Attach the standing declaration to every audit export | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 5196 | Raise the p95 latency budget from ten to twenty-five percent | VP-AI-008 | denied | decided fresh | — |  |
| 5197 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | decided fresh | — |  |
| 5198 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-005 | permitted | decided fresh | — |  |
| 5199 | Swallow PDMP submission errors so checkout never blocks | VP-CS-010 | denied | bound by precedent | REC-VP-B-01819 |  |
| 5200 | Point the resolver at the private registry before the public one | VP-SC-006 | permitted | disposed by citation | — |  |
| 5201 | Pin the radiography panel firmware version in the device inventory | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 5202 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-008 | permitted | decided fresh | — |  |
| 5203 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted | decided fresh | — |  |
| 5204 | Time-box break-glass access to four hours and log the grant | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 5205 | Let clients re-order from prescriptions written last year | VP-CS-006 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 5206 | Block payment-plan enrolment from an account without verified adult status | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 5207 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 5208 | Verify the hash chain when an audit bundle is exported | VP-RR-003 | permitted | decided fresh | — |  |
| 5209 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5210 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 5211 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | decided fresh | — |  |
| 5212 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | decided fresh | — |  |
| 5213 | Run the secret scanner over the diff in pre-merge CI | VP-SC-006 | permitted | decided fresh | — |  |
| 5214 | Take record timestamps from the monotonic server clock | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 5215 | Bound the data subject export job to the statutory window | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5216 | Encrypt the owner address column at rest in the portal store | VP-PD-007 | permitted | decided fresh after a tie | none_tie |  |
| 5217 | Mark required check-in fields with a red border and no error text | VP-AX-001 | denied | decided fresh | — |  |
| 5218 | Reuse the stored consent flag without rechecking its date | VP-PD-008 | denied | decided fresh | — |  |
| 5219 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 5220 | Suppress reminder sends to any number that has already replied STOP | VP-CC-002 | permitted | decided fresh | — | ● |
| 5221 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 5222 | Bump the HL7 parser to the patched upstream release | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 5223 | Reject malformed segments without committing a partial patient write | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 5224 | Queue reminder sends so a retry storm cannot amplify | — | permitted | docketed — nothing engaged | — |  |
| 5225 | Prompt for an off-label rationale in the medical record | VP-VC-007 | permitted | decided fresh | — |  |
| 5226 | Allow extralabel orders for clients with no recorded exam | VP-VC-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 5227 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-010 | permitted | decided fresh | — |  |
| 5228 | Add contract tests for the pinned HL7 v2 profile | VP-PO-010 | permitted | decided fresh | — |  |
| 5229 | Take record timestamps from the monotonic server clock | VP-RR-006 | permitted | decided fresh | — |  |
| 5230 | Start the breach-notice timer at confirmed root cause instead of first detection | VP-BN-001 VP-RB-006 ⛔ | denied | refused at the floor | — |  |
| 5231 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | permitted | decided fresh | — |  |
| 5232 | Match study patient identity on microchip and account number | VP-PO-004 | permitted | decided fresh | — | ● |
| 5233 | Keep the contest link visible on every automated decision notice | VP-GV-005 | permitted | decided fresh | — | ● |
| 5234 | Keep the build runner warm between jobs to cut CI minutes | VP-SC-009 | denied | decided fresh | — |  |
| 5235 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted | bound by precedent | REC-S0108 |  |
| 5236 | Match study patient identity on microchip and account number | VP-PO-007 | permitted | decided fresh | — |  |
| 5237 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-004 | permitted | decided fresh | — |  |
| 5238 | Cap the records-copy fee at the state's statutory maximum | VP-CC-004 | permitted | decided fresh | — |  |
| 5239 | Submit an amendment adding a welfare-inspection remediation window | VP-SC-009 | denied | decided fresh | — |  |
| 5240 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-002 | permitted with conditions | decided fresh | — | ● |
| 5241 | Record prior express consent with timestamp and source before an automated text campaign | VP-CC-005 | permitted | decided fresh | — |  |
| 5242 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5243 | Propose a sunset clause for the analytics pilot exception | VP-PO-002 | denied | decided fresh | — |  |
| 5244 | Amend the retention schedule for controlled-substance records in the rulebook | VP-PO-006 | denied | decided fresh | — |  |
| 5245 | Require a second approver on admin role assignments | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 5246 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5247 | Reject malformed segments without committing a partial patient write | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 5248 | Ship a down-migration for the visit-summary table change | — | permitted | docketed — nothing engaged | — |  |
| 5249 | Restrict claim payload deserialisation to known types | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5250 | Keep the retention clock unchanged when a record is edited | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 5251 | Make the note autosave idempotent under client retry | VP-HA-001 | permitted | decided fresh | — |  |
| 5252 | Allow payment-plan enrolment from an unverified under-eighteen account | VP-CC-006 | denied | decided fresh | — |  |
| 5253 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-004 | permitted | decided fresh | — |  |
| 5254 | Assign a named reviewer to the vendored DICOM parser | VP-SC-008 | permitted | decided fresh | — |  |
| 5255 | Require an explicit share grant for cross-practice referrals | VP-RB-006 | permitted | decided fresh | — |  |
| 5256 | Record the witnessing licensee on every euthanasia-solution dispense | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 5257 | Cap analyzer retries at five with exponential backoff | VP-PO-010 | permitted | decided fresh after a tie | none_tie |  |
| 5258 | Validate webhook destinations against the outbound allowlist | VP-AS-002 | denied | bound by precedent | REC-S0158 |  |
| 5259 | Add an admin path that updates the audit row to fix a typo | VP-RR-004 | denied | decided fresh | — | ● |
| 5260 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5261 | Add the new charting library licence to the allowlist | VP-SC-002 | permitted | decided fresh | — |  |
| 5262 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-002 | permitted | decided fresh | — |  |
| 5263 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | decided fresh | — |  |
| 5264 | Route vendor incident webhooks into the monitored incident queue | VP-BN-003 | permitted | decided fresh | — |  |
| 5265 | Add a jurisdiction lookup table that sources the breach-notice clock from statute text | VP-BN-003 | permitted | decided fresh | — |  |
| 5266 | Return a correlation id instead of a stack trace on error | VP-AS-001 | permitted | decided fresh | — |  |
| 5267 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — | ● |
| 5268 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-004 | permitted | decided fresh | — |  |
| 5269 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-004 | permitted | decided fresh | — |  |
| 5270 | Swallow PDMP submission errors so checkout never blocks | VP-CS-004 VP-VC-006 ⛔ | denied | refused at the floor | — |  |
| 5271 | Propose a sunset clause for the analytics pilot exception | VP-PO-007 | denied | decided fresh | — |  |
| 5272 | Move the release outside the emergency-hours freeze window | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5273 | Prompt for a pain management plan at surgical discharge | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 5274 | Log the authenticated prescriber id on each dispensing event | VP-CS-011 | permitted | decided fresh | — |  |
| 5275 | Change the escalation ladder so the third tier is final | VP-AS-002 | denied | decided fresh | — |  |
| 5276 | Auto-merge agent pull requests once CI is green | VP-AI-002 ⛔ | denied | refused at the floor | — |  |
| 5277 | Propose a sunset clause for the analytics pilot exception | VP-CS-007 | denied | decided fresh | — |  |
| 5278 | Restrict agent outbound calls to the allowlisted host set | VP-AI-008 | permitted | decided fresh | — | ● |
| 5279 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 5280 | Bound the data subject export job to the statutory window | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 5281 | Add contract tests for the pinned HL7 v2 profile | VP-PO-007 | permitted | decided fresh | — |  |
| 5282 | Hide the contest link when the decision is a denial | VP-GV-007 | denied | decided fresh | — |  |
| 5283 | Reuse the stored consent flag without rechecking its date | VP-PD-001 VP-AS-002 ⛔ | denied | refused at the floor | — |  |
| 5284 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-001 VP-AX-002 ⛔ | denied | refused at the floor | — |  |
| 5285 | Ship a down-migration for the visit-summary table change | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5286 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-006 | permitted | bound by precedent | REC-S0106 |  |
| 5287 | Pin the build runner image and make each job ephemeral | VP-SC-008 | permitted | decided fresh | — |  |
| 5288 | Run the secret scanner over the diff in pre-merge CI | VP-SC-008 | permitted | decided fresh | — |  |
| 5289 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh | — |  |
| 5290 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | decided fresh | — |  |
| 5291 | Verify focus order on the consent dialog before each release | VP-AX-001 | permitted | decided fresh | — |  |
| 5292 | Check consent currency before the reminder engine sends | VP-PD-008 | permitted | decided fresh | — |  |
| 5293 | Auto-stamp the veterinarian's signature onto the rabies certificate template | VP-PH-002 | denied | decided fresh | — |  |
| 5294 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-011 | permitted with conditions | decided fresh | — | ● |
| 5295 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5296 | Store payment references, not card numbers, on the retry queue | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 5297 | Add contract tests for the pinned HL7 v2 profile | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 5298 | Require both administrators to confirm an EPCS signing-privilege grant | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 5299 | Link the breach notification runbook from the incident template | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5300 | Version chart amendments instead of editing rows in place | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 5301 | Populate DICOM species and breed tags from the patient record | VP-PO-006 | permitted | decided fresh | — |  |
| 5302 | Hide the contest link when the decision is a denial | VP-GV-003 | denied | decided fresh | — |  |
| 5303 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-008 | permitted | decided fresh | — |  |
| 5304 | Capture the medical-purpose note as a required field on Schedule II orders | VP-CS-012 | permitted | decided fresh | — |  |
| 5305 | Check the version token on clinical note writes | — | permitted | docketed — nothing engaged | — |  |
| 5306 | Add the boarding service to the critical-service list in policy | VP-RB-006 | denied | decided fresh | — |  |
| 5307 | Check the version token on clinical note writes | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5308 | Unblock enrofloxacin ordering for dairy herds | VP-VC-006 | denied | decided fresh | — |  |
| 5309 | Auto-close ketamine count mismatches under two millilitres | VP-CS-003 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 5310 | Require a tag scan at every remains custody transfer | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 5311 | Ship a down-migration for the visit-summary table change | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5312 | Route vendor incident webhooks into the monitored incident queue | VP-BN-002 | permitted | decided fresh | — |  |
| 5313 | Reject configuration changes that would extend the breach-notice clock | VP-BN-002 | permitted | decided fresh | — |  |
| 5314 | Derive tenant id from the session, never from a request header | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 5315 | Timestamp records from the workstation clock the client sends | VP-RR-002 | denied | decided fresh | — |  |
| 5316 | Store the amendment author alongside the superseded text | VP-RR-004 | permitted | decided fresh | — |  |
| 5317 | Disable the biennial inventory job during the systems migration | VP-DR-001 ⛔ | denied | refused at the floor | — |  |
| 5318 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5319 | Publish the contest counts in the audit export header | VP-RR-003 | permitted with conditions | decided fresh | — | ● |
| 5320 | Take record timestamps from the monotonic server clock | VP-RR-002 | permitted | decided fresh | — |  |
| 5321 | Move the release outside the emergency-hours freeze window | VP-HA-002 | permitted | decided fresh | — |  |
| 5322 | Enforce the tenant scope in the query layer, not the handler | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 5323 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-001 | permitted | decided fresh | — |  |
| 5324 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5325 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-006 | permitted | decided fresh | — |  |
| 5326 | Make the feed directive expiry date a mandatory field | VP-VC-005 | permitted with conditions | decided fresh | — | ● |
| 5327 | Gate merges on a clean provenance verification step | VP-SC-006 | permitted | disposed by citation | — |  |
| 5328 | Let clients reassign a microchip's registered owner from the self-service portal | VP-PH-002 | denied | decided fresh | — |  |
| 5329 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-010 | permitted with conditions | decided fresh | — | ● |
| 5330 | Gate merges on a clean provenance verification step | VP-SC-006 | permitted | decided fresh | — |  |
| 5331 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | decided fresh | — | ● |
| 5332 | Generate decision rationales from the outcome at export time | VP-RR-002 | denied | decided fresh | — |  |
| 5333 | Add a support endpoint that dumps the full owner record | VP-PD-007 | denied | decided fresh | — |  |
| 5334 | Require acknowledgement before a critical value page clears | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 5335 | Constrain pet-photo uploads by type, size and resolved path | — | permitted | docketed — nothing engaged | — |  |
| 5336 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-010 | permitted | decided fresh | — |  |
| 5337 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-010 | permitted | decided fresh | — |  |
| 5338 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5339 | Honour opt-out state at export time in the marketing job | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 5340 | Populate DICOM species and breed tags from the patient record | VP-PO-008 | permitted | decided fresh | — |  |
| 5341 | Require acknowledgement before a critical value page clears | VP-PO-008 | permitted | decided fresh | — |  |
| 5342 | Bound the data subject export job to the statutory window | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5343 | Encrypt the owner address column at rest in the portal store | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5344 | Have the agent refactor the controlled dispensing rules engine | VP-AI-004 | denied | decided fresh | — |  |
| 5345 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted | decided fresh | — |  |
| 5346 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 5347 | Version chart amendments instead of editing rows in place | VP-RR-005 | permitted | decided fresh | — |  |
| 5348 | Make the audit table append-only at the database level | VP-RR-006 | permitted | decided fresh | — | ● |
| 5349 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 5350 | Publish the contest counts in the audit export header | VP-RR-004 | permitted with conditions | decided fresh | — | ● |
| 5351 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5352 | Add regression tests for the note-render encoding path | VP-AS-003 | permitted | decided fresh | — |  |
| 5353 | Reject malformed segments without committing a partial patient write | VP-PO-010 | permitted | decided fresh | — |  |
| 5354 | Hold medical-record releases until the client's balance is paid | VP-CC-004 | denied | decided fresh | — |  |
| 5355 | Publish the contest counts in the audit export header | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 5356 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-007 | permitted | decided fresh | — |  |
| 5357 | Add unit tests for the ASAP 4.2B species-code field mapper | VP-CS-007 | permitted | decided fresh | — |  |
| 5358 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5359 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 5360 | Require a second approver on admin role assignments | VP-RB-004 | permitted | decided fresh | — |  |
| 5361 | Add regression tests for the note-render encoding path | — | permitted | docketed — nothing engaged | — |  |
| 5362 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-003 | permitted | decided fresh | — |  |
| 5363 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-003 | permitted | decided fresh | — |  |
| 5364 | Record artefact digests in the release ledger on publish | VP-SC-004 | denied | bound by precedent | REC-S0124 |  |
| 5365 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-006 | permitted | decided fresh | — |  |
| 5366 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-005 | permitted | decided fresh | — |  |
| 5367 | Verify the hash chain when an audit bundle is exported | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 5368 | Enforce the tenant scope in the query layer, not the handler | VP-RB-003 | permitted | decided fresh | — |  |
| 5369 | Disable the biennial inventory job during the systems migration | VP-DR-003 ⛔ | denied | refused at the floor | — |  |
| 5370 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5371 | Parameterise the new chart-search query | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5372 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh | — | ● |
| 5373 | Validate webhook destinations against the outbound allowlist | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5374 | Sanitise filenames in the lab attachment upload handler | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5375 | Disable the biennial inventory job during the systems migration | VP-DR-001 VP-CC-002 ⛔ | denied | refused at the floor | — |  |
| 5376 | Reject malformed segments without committing a partial patient write | VP-PO-006 | permitted | decided fresh | — |  |
| 5377 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 5378 | Add permutation tests across the role-permission matrix | VP-RB-005 | permitted | decided fresh | — |  |
| 5379 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | decided fresh | — |  |
| 5380 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 5381 | Close automated denials without offering a human review request | VP-GV-001 ⛔ | denied | refused at the floor | — |  |
| 5382 | Pin the radiography panel firmware version in the device inventory | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 5383 | Add a free-text field for the owner's social security number | VP-PD-001 VP-SC-006 ⛔ | denied | refused at the floor | — |  |
| 5384 | Require a verified adult guardian before a minor's client account can be created | VP-CC-003 | permitted with conditions | decided fresh | — | ● |
| 5385 | Quarantine unmatched analyzer results for technician review | VP-PO-003 | permitted | decided fresh | — |  |
| 5386 | Queue reminder sends so a retry storm cannot amplify | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5387 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-002 | permitted | decided fresh | — |  |
| 5388 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-002 | permitted | decided fresh | — |  |
| 5389 | Mute the bulk owner-data export alert to quiet the on-call pager | VP-BN-001 VP-PD-003 ⛔ | denied | refused at the floor | — |  |
| 5390 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5391 | Apply the state retention schedule to inactive owner records | VP-PD-008 | permitted | decided fresh | — |  |
| 5392 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 5393 | Apply the state retention schedule to inactive owner records | VP-PD-006 | permitted | decided fresh | — | ● |
| 5394 | Surface an alert when a microchip registry submission fails instead of dropping it | VP-PH-003 | permitted | decided fresh | — |  |
| 5395 | Validate delegated task lists against the state practice act table | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 5396 | Constrain pet-photo uploads by type, size and resolved path | — | permitted | docketed — nothing engaged | — |  |
| 5397 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5398 | Show the premises visit date on the large-animal chart header | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 5399 | Make the audit table append-only at the database level | VP-RR-005 | permitted | decided fresh | — |  |
| 5400 | Keep the retention clock unchanged when a record is edited | VP-RR-007 | permitted | decided fresh | — |  |
| 5401 | Assign the daily audit review to the practice manager role | VP-RR-007 | permitted | decided fresh | — |  |
| 5402 | Run agent-generated code inside the sandboxed runner only | VP-AI-003 | permitted | decided fresh after a tie | none_tie |  |
| 5403 | Let staff issue standing scripts without opening the patient record | VP-CS-007 | denied | bound by precedent | REC-VP-B-00035 | ● |
| 5404 | Enforce authorisation server-side on the discharge summary route | VP-AS-004 | permitted | disposed by citation | — |  |
| 5405 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — |  |
| 5406 | Keep the retention clock unchanged when a record is edited | VP-RR-003 | permitted | decided fresh | — |  |
| 5407 | Edit the CI workflow to skip the secret-scan gate on this branch | VP-AS-005 | denied | decided fresh | — |  |
| 5408 | Queue reminder sends so a retry storm cannot amplify | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5409 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5410 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 5411 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted with conditions | decided fresh | — | ● |
| 5412 | Scope modality worklist queries to the requesting practice | VP-PO-005 | permitted | decided fresh | — |  |
| 5413 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | permitted | decided fresh | — |  |
| 5414 | Validate microchip numbers against the ISO 11784 format at intake | VP-PH-004 | permitted with conditions | decided fresh | — | ● |
| 5415 | Give consent withdrawal the same one-click path as granting it | VP-PD-008 | permitted with conditions | decided fresh | — | ● |
| 5416 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-003 | permitted with conditions | decided fresh | — | ● |
| 5417 | Turn off audit writes on the hot dispensing path | VP-RR-001 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 5418 | Split the agent-refactored invoicing function to cut its branching | VP-AI-005 | permitted | decided fresh | — |  |
| 5419 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-005 ⛔ | denied | refused at the floor | — |  |
| 5420 | Block agent branches from touching the compliance test suite | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 5421 | Assign a named reviewer to the vendored DICOM parser | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 5422 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-009 | permitted | decided fresh | — |  |
| 5423 | Add a free-text field for the owner's social security number | VP-PD-006 | denied | decided fresh | — | ● |
| 5424 | Configure retention periods per jurisdiction in the scheduler | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 5425 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5426 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5427 | Bind each service account to a single practice id | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 5428 | Deny clinical note writes to the receptionist role | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 5429 | Record a disposition for every referral acknowledgement | VP-GV-006 | permitted | decided fresh | — |  |
| 5430 | Log the acknowledgement disposition on the referral timeline | VP-GV-006 | permitted | decided fresh | — |  |
| 5431 | Parameterise the new chart-search query | VP-AS-002 | permitted | disposed by citation | — |  |
| 5432 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-009 | permitted | decided fresh | — |  |
| 5433 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-002 | permitted | decided fresh | — |  |
| 5434 | Attach a residue risk assessment to the food-animal order form | VP-VC-008 | permitted | decided fresh | — |  |
| 5435 | Check the version token on clinical note writes | VP-HA-003 | permitted | decided fresh | — |  |
| 5436 | Attach the standing declaration to every audit export | VP-RR-003 | permitted | decided fresh | — |  |
| 5437 | Write the decision rationale at resolution time, not on export | VP-RR-004 | permitted | decided fresh | — |  |
| 5438 | Take record timestamps from the monotonic server clock | VP-RR-004 | permitted | decided fresh | — |  |
| 5439 | Encrypt the owner address column at rest in the portal store | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 5440 | Allowlist microchip identifier formats at the API boundary | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5441 | Match study patient identity on microchip and account number | VP-PO-008 | permitted | decided fresh | — | ● |
| 5442 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh | — |  |
| 5443 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5444 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 5445 | Estimate breach scope from a ten-percent log sample to finish the report faster | VP-BN-003 | denied | decided fresh | — |  |
| 5446 | Show the six-month validity window on the refill request screen | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 5447 | Drop analyzer messages that fail to parse and move on | VP-PO-001 VP-AS-004 ⛔ | denied | refused at the floor | — |  |
| 5448 | Timestamp records from the workstation clock the client sends | VP-RR-002 | denied | decided fresh | — | ● |
| 5449 | Drop the runbook link from the detection alert payload to shorten it | VP-BN-002 | denied | decided fresh | — |  |
| 5450 | Validate the PDMP payload against the state schema before submit | VP-CS-012 | permitted with conditions | decided fresh | — | ● |
| 5451 | Allow extralabel orders for clients with no recorded exam | VP-VC-001 VP-PO-006 ⛔ | denied | refused at the floor | — |  |
| 5452 | Verify commit signatures on the protected release branch | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 5453 | Populate DICOM species and breed tags from the patient record | VP-PO-010 | permitted | decided fresh | — |  |
| 5454 | Require a second approver on admin role assignments | VP-RB-007 | permitted | decided fresh | — |  |
| 5455 | Show a merge dialog instead of overwriting a colleague's note | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5456 | Require a second approver on admin role assignments | VP-RB-006 | permitted | decided fresh | — |  |
| 5457 | Move the authorisation decision out of the portal frontend | VP-RB-006 | permitted | decided fresh | — |  |
| 5458 | Encode clinical note text before rendering it in the portal | — | permitted | docketed — nothing engaged | — |  |
| 5459 | Label agent-authored commits so review routing can see them | VP-AI-004 | permitted | decided fresh | — |  |
| 5460 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5461 | Apply the state retention schedule to inactive owner records | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5462 | Pin the build runner image and make each job ephemeral | VP-SC-007 | permitted | decided fresh | — |  |
| 5463 | Update the manifest and lockfile in the same commit | VP-SC-007 | permitted | decided fresh | — |  |
| 5464 | Store payment references, not card numbers, on the retry queue | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 5465 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5466 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5467 | Renumber the point-of-care provisions after the device policy merge | VP-SC-009 | denied | decided fresh | — |  |
| 5468 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted | decided fresh | — |  |
| 5469 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted | decided fresh | — | ● |
| 5470 | Read the practice id from the X-Practice request header | VP-RB-003 | denied | decided fresh | — |  |
| 5471 | Queue reminder sends so a retry storm cannot amplify | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5472 | Flag food-animal status on the patient banner before dispensing | VP-VC-007 | permitted with conditions | decided fresh | — | ● |
| 5473 | Wrap result-to-patient binding in a single database transaction | VP-PO-006 | permitted | decided fresh | — |  |
| 5474 | Write the decision rationale at resolution time, not on export | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 5475 | Apply the state retention schedule to inactive owner records | VP-PD-009 | permitted with conditions | decided fresh | — | ● |
| 5476 | Bind each service account to a single practice id | VP-RB-004 | permitted | decided fresh | — |  |
| 5477 | Publish the contest counts in the audit export header | VP-RR-005 | permitted with conditions | decided fresh | — | ● |
| 5478 | File a draft amendment codifying module-level coverage for generated code | VP-CS-007 | denied | decided fresh | — |  |
| 5479 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5480 | Match study patient identity on microchip and account number | VP-PO-009 | permitted | decided fresh | — |  |
| 5481 | Derive tenant id from the session, never from a request header | VP-RB-005 | permitted | decided fresh | — | ● |
| 5482 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-007 | permitted | decided fresh | — |  |
| 5483 | Record artefact digests in the release ledger on publish | VP-SC-009 | permitted | disposed by citation | — |  |
| 5484 | Assign a named reviewer to the vendored DICOM parser | VP-SC-007 | permitted | decided fresh | — | ● |
| 5485 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-004 | permitted | decided fresh | — |  |
| 5486 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | decided fresh | — |  |
| 5487 | Cover the new boarding endpoint with a role check test | VP-RB-008 | permitted | decided fresh | — |  |
| 5488 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5489 | Restore session objects by deserialising the client-supplied blob | VP-AS-003 | denied | decided fresh | — |  |
| 5490 | Block agent branches from touching the compliance test suite | VP-AI-008 | permitted | decided fresh | — |  |
| 5491 | Run agent-generated code inside the sandboxed runner only | VP-AI-008 | permitted | decided fresh | — |  |
| 5492 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-007 | permitted | decided fresh | — |  |
| 5493 | Allowlist microchip identifier formats at the API boundary | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5494 | Shorten the break-glass expiry constant in the rulebook | VP-RR-006 | denied | decided fresh | — |  |
| 5495 | Restrict agent outbound calls to the allowlisted host set | VP-AI-004 | permitted | decided fresh | — |  |
| 5496 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | decided fresh | — |  |
| 5497 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 5498 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-001 | permitted | decided fresh | — |  |
| 5499 | Revalidate the active session after a privilege change | VP-RB-004 | permitted | decided fresh | — |  |
| 5500 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted with conditions | bound by precedent | REC-S0086 |  |
| 5501 | Reuse one integration account across every clinic in the estate | VP-RB-007 | denied | decided fresh | — |  |
| 5502 | Add a free-text field for the owner's social security number | VP-PD-005 | denied | decided fresh | — |  |
| 5503 | Rank retrieval candidates using the audit register's findings | VP-GV-002 VP-AI-004 ⛔ | denied | refused at the floor | — |  |
| 5504 | Show the six-month validity window on the refill request screen | VP-CS-007 | permitted | decided fresh | — | ● |
| 5505 | Hand the checkout redirect to the validated payment processor | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 5506 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5507 | Gate merges on a clean provenance verification step | VP-SC-001 | denied | bound by precedent | REC-S0162 |  |
| 5508 | Apply the state retention schedule to inactive owner records | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 5509 | Swallow PDMP submission errors so checkout never blocks | VP-CS-012 | denied | decided fresh | — |  |
| 5510 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted with conditions | decided fresh | — | ● |
| 5511 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted | decided fresh | — |  |
| 5512 | Require an exact physical count entry before the inventory record can be signed | VP-DR-004 | permitted | decided fresh | — |  |
| 5513 | Log the full card number on payment retry to debug declines | VP-PD-001 VP-RR-004 ⛔ | denied | refused at the floor | — |  |
| 5514 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 5515 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 5516 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted | decided fresh | — |  |
| 5517 | Auto-merge agent pull requests once CI is green | VP-AI-002 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 5518 | Show the six-month validity window on the refill request screen | VP-CS-008 | permitted with conditions | decided fresh | — | ● |
| 5519 | Hand the checkout redirect to the validated payment processor | VP-PD-006 | permitted | decided fresh | — |  |
| 5520 | Cap analyzer retries at five with exponential backoff | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 5521 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | decided fresh | — |  |
| 5522 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-006 | permitted | decided fresh | — |  |
| 5523 | Add an admin path that updates the audit row to fix a typo | VP-RR-007 | denied | decided fresh | — |  |
| 5524 | Bound the results reconciler retry loop | VP-HA-001 | permitted | decided fresh | — |  |
| 5525 | Add a keyboard path out of the consent modal's focus trap | VP-AX-002 | permitted with conditions | decided fresh | — | ● |
| 5526 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-003 | permitted with conditions | bound by precedent | REC-S0082 |  |
| 5527 | Match the required supervision level to the task's risk tier | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5528 | Make the second-licensee witness field optional on euthanasia logs | VP-CS-004 VP-PO-005 ⛔ | denied | refused at the floor | — |  |
| 5529 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 5530 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5531 | Revalidate the active session after a privilege change | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 5532 | Return a correlation id instead of a stack trace on error | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 5533 | Sanitise filenames in the lab attachment upload handler | VP-AS-001 | permitted | decided fresh | — |  |
| 5534 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-001 | permitted | decided fresh | — |  |
| 5535 | Bound the data subject export job to the statutory window | VP-PD-007 | permitted with conditions | decided fresh | — | ● |
| 5536 | Move threshold parameters into the legislated configuration | VP-GV-004 | permitted | decided fresh | — |  |
| 5537 | Route a human review request from the decision detail page | VP-GV-004 | permitted | decided fresh | — |  |
| 5538 | Record who exported an audit bundle and when | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5539 | Auto-acknowledge critical-value alerts if no one responds within five minutes | VP-PS-001 VP-PD-007 ⛔ | denied | refused at the floor | — |  |
| 5540 | Attach build provenance to the practice API release artefact | VP-SC-002 | permitted | decided fresh | — |  |
| 5541 | Let staff log a remains custody transfer without scanning the tag | VP-PS-004 VP-SC-008 ⛔ | denied | refused at the floor | — |  |
| 5542 | Block record purges that fall inside the two-year retention term | VP-CS-010 | permitted | decided fresh | — | ● |
| 5543 | Drop the practice filter from the referral search endpoint | VP-RB-005 | denied | decided fresh | — |  |
| 5544 | Add the boarding service to the critical-service list in policy | VP-AX-002 | denied | decided fresh | — |  |
| 5545 | Call an external summarisation API from the agent's new helper | VP-AI-001 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 5546 | Remove the deadline timer from the data export request queue | VP-PD-003 | denied | decided fresh | — |  |
| 5547 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-009 | permitted | decided fresh | — |  |
| 5548 | Restore the written-prescription button to the dispensing screen after a UI redesign | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 5549 | Drop internal identifiers from the public error envelope | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5550 | Deny clinical note writes to the receptionist role | VP-RB-005 | permitted | decided fresh | — | ● |
| 5551 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 5552 | Block procedure sign-off by roles outside the delegated scope | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 5553 | Attach build provenance to the practice API release artefact | VP-SC-003 | permitted | decided fresh | — |  |
| 5554 | Warn when a dose falls outside the labelled species range | VP-VC-005 | permitted | decided fresh | — |  |
| 5555 | Warn when a dose falls outside the labelled species range | VP-VC-005 | permitted | decided fresh | — |  |
| 5556 | Turn off audit writes on the hot dispensing path | VP-RR-005 | denied | decided fresh | — |  |
| 5557 | Turn off signature enforcement on main to unblock the release train | VP-SC-004 | denied | decided fresh | — |  |
| 5558 | Pin the radiography panel firmware version in the device inventory | VP-PO-006 | permitted | decided fresh | — |  |
| 5559 | Add a concurrency test for simultaneous discharge summary saves | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5560 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted | decided fresh | — |  |
| 5561 | Assign a named reviewer to the vendored DICOM parser | VP-SC-009 | permitted | decided fresh | — |  |
| 5562 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-009 | permitted | decided fresh | — |  |
| 5563 | Require an explicit share grant for cross-practice referrals | VP-RB-007 | permitted with conditions | bound by precedent | REC-S0084 |  |
| 5564 | Bump the HL7 parser to the patched upstream release | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5565 | Check consent currency before the reminder engine sends | VP-PD-009 | permitted | decided fresh | — |  |
| 5566 | Attribute the standing declaration to the enacting authority | VP-GV-006 | permitted | decided fresh | — |  |
| 5567 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-002 | permitted | disposed by citation | — |  |
| 5568 | Amend the retention schedule for controlled-substance records in the rulebook | VP-CS-012 | denied | decided fresh | — |  |
| 5569 | Redact owner email addresses from claims connector debug output | VP-PD-007 | permitted | decided fresh | — |  |
| 5570 | Match the required supervision level to the task's risk tier | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5571 | Document the degraded path when the reference lab is down | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5572 | Remove the necessity note from the bulk compounding form | VP-VC-005 | denied | decided fresh | — |  |
| 5573 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5574 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — |  |
| 5575 | Validate webhook destinations against the outbound allowlist | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 5576 | Scope the new reporting role to read-only endpoints | VP-RB-002 | permitted | decided fresh | — | ● |
| 5577 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5578 | Assign a named reviewer to the vendored DICOM parser | VP-SC-006 | permitted | decided fresh | — |  |
| 5579 | Honour opt-out state at export time in the marketing job | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 5580 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-006 | denied | decided fresh | — |  |
| 5581 | Prove the backup restore before the vaccine index migration | VP-HA-001 | permitted | decided fresh | — |  |
| 5582 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 VP-PO-002 ⛔ | denied | refused at the floor | — |  |
| 5583 | Take record timestamps from the monotonic server clock | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5584 | Populate DICOM species and breed tags from the patient record | VP-PO-004 | permitted | decided fresh | — |  |
| 5585 | Quarantine unmatched analyzer results for technician review | VP-PO-004 | permitted | decided fresh | — |  |
| 5586 | Add captions to the discharge-instructions video on the portal | VP-AX-001 | permitted | decided fresh | — |  |
| 5587 | Version the accessibility statement alongside the portal release notes | VP-AX-001 | permitted | decided fresh | — |  |
| 5588 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5589 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 5590 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5591 | Expose the radiography panel to the internet for vendor support | VP-PO-004 | denied | decided fresh | — |  |
| 5592 | Add the transport welfare checklist to the boarding intake form | VP-AW-002 | permitted | bound by precedent | REC-S0194 |  |
| 5593 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted | decided fresh | — |  |
| 5594 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5595 | Add the new charting library licence to the allowlist | VP-SC-009 | permitted | decided fresh | — |  |
| 5596 | Record the analgesia rationale when a plan is declined | VP-AW-005 | permitted | bound by precedent | REC-S0197 |  |
| 5597 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 5598 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-002 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 5599 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 5600 | Write the decision rationale at resolution time, not on export | VP-RR-004 | permitted | decided fresh | — |  |
| 5601 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-008 | permitted | decided fresh | — |  |
| 5602 | Tighten the portal CSP by dropping the inline script allowance | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5603 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | decided fresh | — |  |
| 5604 | Bound the data subject export job to the statutory window | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5605 | Attach the clinical-necessity note to bulk compounding orders | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 5606 | Expose the radiography panel to the internet for vendor support | VP-PO-002 | denied | decided fresh | — | ● |
| 5607 | Remove the unsubscribe link and point owners at the clinic phone line | VP-PD-002 VP-AI-007 ⛔ | denied | refused at the floor | — |  |
| 5608 | Replace the hand-rolled token hash with the vetted library | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5609 | Bound the results reconciler retry loop | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5610 | Write the decision rationale at resolution time, not on export | VP-RR-006 | permitted | decided fresh | — |  |
| 5611 | Assign the daily audit review to the practice manager role | VP-RR-006 | permitted | decided fresh | — |  |
| 5612 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5613 | Ship the boarding availability endpoint without a role check | VP-RB-001 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 5614 | Record the rabies vaccine lot and expiry alongside the issued certificate | VP-PH-002 | permitted with conditions | decided fresh | — | ● |
| 5615 | Wrap result-to-patient binding in a single database transaction | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 5616 | Reconcile ketamine vial volumes to the millilitre in the nightly job | VP-CS-012 | permitted with conditions | bound by precedent | REC-S0094 |  |
| 5617 | Have the agent refactor the controlled dispensing rules engine | VP-AI-006 | denied | decided fresh | — | ● |
| 5618 | Run the DLP scan over changed lines in the billing pipeline | VP-PD-003 | permitted | decided fresh | — |  |
| 5619 | Auto-merge agent pull requests once CI is green | VP-AI-005 | denied | decided fresh | — |  |
| 5620 | Tokenise the card number before the invoice row is written | VP-PD-005 | permitted | decided fresh | — |  |
| 5621 | Make the human review queue reachable from the portal | VP-GV-007 | permitted | decided fresh | — |  |
| 5622 | Store the amendment author alongside the superseded text | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5623 | Hand the checkout redirect to the validated payment processor | VP-PD-007 | permitted | decided fresh | — |  |
| 5624 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted | decided fresh after a tie | none_tie |  |
| 5625 | Enable video-only exams for prescribing in every state | VP-VC-001 VP-RR-003 ⛔ | denied | refused at the floor | — |  |
| 5626 | Publish the contest counts in the audit export header | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5627 | Configure retention periods per jurisdiction in the scheduler | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5628 | Quarantine unmatched analyzer results for technician review | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 5629 | Point the resolver at the private registry before the public one | VP-SC-002 | permitted | disposed by citation | — |  |
| 5630 | Make the feed directive expiry date a mandatory field | VP-VC-007 | permitted | decided fresh | — |  |
| 5631 | Validate species and body weight before computing the dosage | VP-VC-008 | permitted | decided fresh | — |  |
| 5632 | Assign the daily audit review to the practice manager role | VP-RR-005 | permitted | decided fresh | — | ● |
| 5633 | Require a fresh e-signature consent action rather than inferring it from login | VP-CC-004 | permitted | decided fresh | — |  |
| 5634 | Pin the radiography panel firmware version in the device inventory | VP-PO-003 | permitted | decided fresh | — |  |
| 5635 | Reject malformed segments without committing a partial patient write | VP-PO-003 | permitted | decided fresh | — |  |
| 5636 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5637 | Lower the changed-line coverage threshold in the policy repo | VP-SC-001 | denied | decided fresh | — |  |
| 5638 | Encode clinical note text before rendering it in the portal | VP-AS-003 | permitted | decided fresh | — | ● |
| 5639 | Target payment-plan upsells at owners flagged as financially distressed | VP-GV-003 | denied | decided fresh | — |  |
| 5640 | Validate webhook destinations against the outbound allowlist | VP-AS-003 | permitted | decided fresh | — |  |
| 5641 | Reuse the stored consent flag without rechecking its date | VP-PD-001 VP-AI-004 ⛔ | denied | refused at the floor | — |  |
| 5642 | Enforce the tenant scope in the query layer, not the handler | VP-RB-005 | denied | bound by precedent | REC-S0164 |  |
| 5643 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-003 | permitted with conditions | decided fresh | — | ● |
| 5644 | Add an immutability test for the dispensing log writer | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5645 | Expose the radiography panel to the internet for vendor support | VP-PO-003 | denied | decided fresh | — |  |
| 5646 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5647 | Suppress critical-value alerts during the clinic's configured quiet hours | VP-PS-001 VP-PO-007 ⛔ | denied | refused at the floor | — |  |
| 5648 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-003 VP-SC-004 ⛔ | denied | refused at the floor | — |  |
| 5649 | Tokenise the card number before the invoice row is written | VP-PD-006 | permitted | decided fresh | — |  |
| 5650 | Prompt for an off-label rationale in the medical record | VP-VC-005 | permitted | decided fresh | — |  |
| 5651 | Show the premises visit date on the large-animal chart header | VP-VC-005 | permitted | decided fresh | — |  |
| 5652 | Turn off signature enforcement on main to unblock the release train | VP-SC-004 | denied | decided fresh | — |  |
| 5653 | Assign the daily audit review to the practice manager role | VP-RR-003 | permitted | decided fresh | — |  |
| 5654 | Let clients re-order from prescriptions written last year | VP-CS-006 VP-PO-010 ⛔ | denied | refused at the floor | — |  |
| 5655 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted | decided fresh | — |  |
| 5656 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 5657 | Write a docket entry for every uncharged arrival | VP-GV-006 | permitted | decided fresh | — |  |
| 5658 | Route a human review request from the decision detail page | VP-GV-006 | permitted | decided fresh | — |  |
| 5659 | Pin the build runner image and make each job ephemeral | VP-SC-005 | permitted | disposed by citation | — |  |
| 5660 | Derive tenant id from the session, never from a request header | VP-RB-003 | permitted | decided fresh | — |  |
| 5661 | Time-box break-glass access to four hours and log the grant | VP-RB-003 | permitted | decided fresh | — |  |
| 5662 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 5663 | Run semantic analysis over the agent diff in CI | VP-AI-005 | permitted | decided fresh | — | ● |
| 5664 | Strip untrusted ticket text from the agent's instruction context | VP-AI-006 | permitted | decided fresh | — |  |
| 5665 | Prompt for an off-label rationale in the medical record | VP-VC-008 | permitted | decided fresh | — |  |
| 5666 | Add a nightly job that reconciles CSOS certificate expiry against active signers | VP-DR-004 | permitted | decided fresh | — |  |
| 5667 | Route every Schedule II reorder through the CSOS certificate signer | VP-DR-004 | permitted | decided fresh | — |  |
| 5668 | Constrain pet-photo uploads by type, size and resolved path | — | permitted | docketed — nothing engaged | — |  |
| 5669 | Reuse the stored consent flag without rechecking its date | VP-PD-009 | denied | decided fresh | — |  |
| 5670 | Queue reminder sends so a retry storm cannot amplify | VP-HA-003 | permitted | decided fresh | — |  |
| 5671 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5672 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5673 | Bump the HL7 parser to the patched upstream release | VP-SC-002 | permitted | decided fresh | — |  |
| 5674 | Stagger analyzer polling to flatten the morning load peak | — | permitted | docketed — nothing engaged | — |  |
| 5675 | Retry failed PDMP submissions and alert when no acknowledgement arrives | VP-CS-008 | permitted | decided fresh | — |  |
| 5676 | Sanitise filenames in the lab attachment upload handler | VP-AS-001 | denied | bound by precedent | REC-S0122 |  |
| 5677 | Run the secret scanner over the diff in pre-merge CI | VP-SC-003 | permitted with conditions | decided fresh | — | ● |
| 5678 | Queue reminder sends so a retry storm cannot amplify | VP-HA-003 | permitted | decided fresh | — |  |
| 5679 | Let the password alone sign an e-prescription when the token times out | VP-CS-006 VP-SC-005 ⛔ | denied | refused at the floor | — |  |
| 5680 | Drop internal identifiers from the public error envelope | VP-AS-004 | permitted | disposed by citation | — |  |
| 5681 | Propose a sunset clause for the analytics pilot exception | VP-AX-001 | denied | decided fresh | — |  |
| 5682 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-008 | denied | decided fresh | — |  |
| 5683 | Add regression tests for the note-render encoding path | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5684 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-001 ⛔ | denied | refused at the floor | — |  |
| 5685 | Flag food-animal status on the patient banner before dispensing | VP-VC-005 | permitted | decided fresh | — |  |
| 5686 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-005 | permitted | decided fresh | — |  |
| 5687 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-PO-010 ⛔ | denied | refused at the floor | — |  |
| 5688 | Remove the deadline timer from the data export request queue | VP-PD-009 | denied | decided fresh | — |  |
| 5689 | Surface the biennial inventory due date on the dispensing dashboard | VP-CS-008 | permitted | decided fresh | — |  |
| 5690 | Flag food-animal status on the patient banner before dispensing | VP-VC-006 | permitted with conditions | decided fresh | — | ● |
| 5691 | Load test the triage queue at a hundred concurrent clinicians | VP-HA-001 | permitted | decided fresh | — |  |
| 5692 | Skip the DEA registration lookup when a relief vet is on shift | VP-CS-003 VP-DR-004 ⛔ | denied | refused at the floor | — |  |
| 5693 | Let the password alone sign an e-prescription when the token times out | VP-CS-001 VP-PO-004 ⛔ | denied | refused at the floor | — |  |
| 5694 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-004 | permitted | decided fresh | — |  |
| 5695 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-004 | permitted | decided fresh | — |  |
| 5696 | Validate species and body weight before computing the dosage | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 5697 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | decided fresh | — |  |
| 5698 | Swallow PDMP submission errors so checkout never blocks | VP-CS-010 | denied | decided fresh | — |  |
| 5699 | Withhold prescription finalisation from technician accounts | VP-RB-007 | permitted | decided fresh | — |  |
| 5700 | Make anaesthesia monitoring intervals mandatory on the record | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5701 | Parameterise the new chart-search query | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5702 | Prove the backup restore before the vaccine index migration | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5703 | Check consent currency before the reminder engine sends | VP-PD-006 | permitted | decided fresh | — |  |
| 5704 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 5705 | Run semantic analysis over the agent diff in CI | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |
| 5706 | Record the lawful basis for the EU-to-US analytics transfer | VP-PD-005 | permitted | decided fresh | — |  |
| 5707 | Split the agent-refactored invoicing function to cut its branching | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 5708 | Give consent withdrawal the same one-click path as granting it | VP-PD-008 | permitted | decided fresh after a tie | none_tie |  |
| 5709 | Propose a sunset clause for the analytics pilot exception | VP-RB-004 | denied | decided fresh | — |  |
| 5710 | Keep the contest link visible on every automated decision notice | VP-GV-005 | permitted | decided fresh | — |  |
| 5711 | Make the human review queue reachable from the portal | VP-GV-005 | permitted | decided fresh | — |  |
| 5712 | Attach build provenance to the practice API release artefact | VP-SC-001 | permitted | disposed by citation | — |  |
| 5713 | Log the full card number on payment retry to debug declines | VP-PD-004 | denied | decided fresh | — |  |
| 5714 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5715 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-002 VP-PO-010 ⛔ | denied | refused at the floor | — |  |
| 5716 | Match study patient identity on microchip and account number | VP-PO-010 | permitted | decided fresh | — |  |
| 5717 | Log the full card number on payment retry to debug declines | VP-PD-001 VP-AS-001 ⛔ | denied | refused at the floor | — |  |
| 5718 | Require staff-verified ownership before a microchip's registered owner can change | VP-PH-004 | permitted | decided fresh | — |  |
| 5719 | Dispatch reportable-disease notices as each case is confirmed rather than in a weekly batch | VP-PH-004 | permitted | decided fresh | — |  |
| 5720 | Swallow PDMP submission errors so checkout never blocks | VP-CS-003 ⛔ | denied | refused at the floor | — |  |
| 5721 | Enforce authorisation server-side on the discharge summary route | VP-AS-005 | permitted | decided fresh | — |  |
| 5722 | Withhold prescription finalisation from technician accounts | VP-RB-006 | permitted | decided fresh | — |  |
| 5723 | Run agent-generated code inside the sandboxed runner only | VP-AI-006 | permitted | decided fresh | — |  |
| 5724 | Ship a down-migration for the visit-summary table change | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5725 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 5726 | Attach build provenance to the practice API release artefact | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 5727 | Require acknowledgement before a critical value page clears | VP-PO-004 | permitted | bound by precedent | REC-S0102 |  |
| 5728 | Show the zoonotic-exposure flag to boarding staff on the patient banner | VP-PH-002 | permitted with conditions | decided fresh | — | ● |
| 5729 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 5730 | Bind each service account to a single practice id | VP-RB-007 | permitted | decided fresh | — | ● |
| 5731 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh | — |  |
| 5732 | Route every red-flag triage conversation to an on-duty licensed technician | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 5733 | Raise the p95 latency budget from ten to twenty-five percent | VP-AX-001 | denied | decided fresh | — |  |
| 5734 | Replace the unmaintained transitive dependency with a vetted fork | VP-SC-002 | permitted | disposed by citation | — |  |
| 5735 | Populate DICOM species and breed tags from the patient record | VP-PO-010 | permitted | decided fresh | — |  |
| 5736 | Require acknowledgement before a critical value page clears | VP-PO-010 | permitted | decided fresh | — |  |
| 5737 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | decided fresh | — |  |
| 5738 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-004 | permitted | decided fresh | — |  |
| 5739 | Honour opt-out state at export time in the marketing job | VP-PD-007 | permitted | decided fresh | — |  |
| 5740 | Stagger analyzer polling to flatten the morning load peak | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5741 | Redact owner email addresses from claims connector debug output | VP-PD-006 | permitted | decided fresh | — |  |
| 5742 | Sanitise filenames in the lab attachment upload handler | VP-AS-004 | denied | bound by precedent | REC-S0156 |  |
| 5743 | Release medical records regardless of outstanding balance | VP-CC-005 | permitted | decided fresh | — |  |
| 5744 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5745 | Propose a sunset clause for the analytics pilot exception | VP-AS-003 | denied | decided fresh | — |  |
| 5746 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted | decided fresh | — |  |
| 5747 | Point the resolver at the private registry before the public one | VP-SC-006 | permitted | decided fresh | — | ● |
| 5748 | Drop internal identifiers from the public error envelope | — | permitted | docketed — nothing engaged | — |  |
| 5749 | Record the analgesia rationale when a plan is declined | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5750 | Pin the radiography panel firmware version in the device inventory | VP-PO-009 | permitted | decided fresh | — |  |
| 5751 | Restore the full reportable-condition list after a fixture refresh had trimmed it | VP-PH-003 | permitted | decided fresh | — |  |
| 5752 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5753 | Let the calculator accept twice the labelled equine maximum | VP-VC-002 VP-RB-005 ⛔ | denied | refused at the floor | — |  |
| 5754 | Match study patient identity on microchip and account number | VP-PO-007 | permitted | decided fresh | — |  |
| 5755 | Point the resolver at the private registry before the public one | VP-SC-004 | permitted | decided fresh | — |  |
| 5756 | Add the new charting library licence to the allowlist | VP-SC-005 | permitted | decided fresh | — |  |
| 5757 | Restrict agent outbound calls to the allowlisted host set | VP-AI-007 | permitted | decided fresh | — |  |
| 5758 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5759 | Derive tenant id from the session, never from a request header | VP-RB-006 | permitted | decided fresh | — |  |
| 5760 | Add regression tests for the note-render encoding path | VP-AS-001 | permitted | decided fresh | — |  |
| 5761 | Add regression tests for the note-render encoding path | VP-AS-001 | permitted | decided fresh | — |  |
| 5762 | Log the acknowledgement disposition on the referral timeline | VP-GV-006 | permitted | decided fresh | — |  |
| 5763 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5764 | Merge the agent's forty-branch claims eligibility function as written | VP-AI-007 | denied | decided fresh | — |  |
| 5765 | Skip the dispensing audit test the agent could not get passing | VP-AI-004 | denied | decided fresh | — |  |
| 5766 | Check the jurisdiction table before honouring a telehealth-established VCPR | VP-VC-008 | permitted | decided fresh | — |  |
| 5767 | Flag food-animal status on the patient banner before dispensing | VP-VC-007 | permitted | decided fresh | — |  |
| 5768 | Route diversion alerts to the medical director's queue within the hour | VP-CS-011 | permitted | bound by precedent | REC-S0104 |  |
| 5769 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5770 | Default the feed directive expiry to blank when it is unknown | VP-VC-007 | denied | decided fresh | — |  |
| 5771 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5772 | Publish the agent runner's host allowlist as reviewed configuration | VP-AI-003 | permitted | decided fresh | — | ● |
| 5773 | Restrict claim payload deserialisation to known types | VP-AS-006 | permitted | docketed — not charged | — |  |
| 5774 | Withhold prescription finalisation from technician accounts | VP-RB-003 | permitted | decided fresh | — |  |
| 5775 | Bound the data subject export job to the statutory window | VP-PD-006 | permitted | decided fresh | — |  |
| 5776 | Drop internal identifiers from the public error envelope | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5777 | Raise the p95 latency budget from ten to twenty-five percent | VP-AI-003 | denied | decided fresh | — |  |
| 5778 | Check object ownership before returning a patient chart | VP-RB-004 | permitted | decided fresh | — |  |
| 5779 | Tokenise the card number before the invoice row is written | VP-PD-009 | permitted | decided fresh | — | ● |
| 5780 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted with conditions | decided fresh | — | ● |
| 5781 | Encrypt the owner address column at rest in the portal store | VP-PD-003 | denied | bound by precedent | REC-S0160 |  |
| 5782 | Turn off diversion analytics for the pilot practice to cut false positives | VP-DR-002 VP-RB-008 ⛔ | denied | refused at the floor | — |  |
| 5783 | Sanitise filenames in the lab attachment upload handler | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5784 | Prove the backup restore before the vaccine index migration | VP-HA-001 | permitted | decided fresh | — |  |
| 5785 | Link the breach notification runbook from the incident template | VP-PD-005 | permitted | decided fresh | — |  |
| 5786 | Make the note autosave idempotent under client retry | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5787 | Block payment-plan enrolment from an account without verified adult status | VP-CC-002 | permitted | decided fresh | — |  |
| 5788 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 5789 | Remove the suspected-abuse report option from the chart menu | VP-PH-003 | denied | decided fresh | — |  |
| 5790 | Add regression tests for the note-render encoding path | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5791 | Add an immutability test for the dispensing log writer | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5792 | Flag food-animal status on the patient banner before dispensing | VP-VC-008 | permitted | decided fresh | — |  |
| 5793 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-001 VP-SC-005 ⛔ | denied | refused at the floor | — |  |
| 5794 | Populate DICOM species and breed tags from the patient record | VP-PO-006 | permitted | decided fresh after a tie | none_tie |  |
| 5795 | Require a recorded in-person exam date before extralabel orders | VP-VC-008 | permitted | decided fresh | — |  |
| 5796 | Enforce authorisation server-side on the discharge summary route | — | permitted | docketed — nothing engaged | — |  |
| 5797 | Publish the contest counts in the audit export header | VP-RR-003 | permitted | decided fresh | — |  |
| 5798 | Auto-merge agent pull requests once CI is green | VP-AI-004 | denied | decided fresh | — |  |
| 5799 | Encrypt the owner address column at rest in the portal store | VP-PD-009 | permitted | decided fresh | — |  |
| 5800 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted | decided fresh | — |  |
| 5801 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-002 | permitted | decided fresh | — |  |
| 5802 | Require a verified adult guardian before a minor's client account can be created | VP-CC-006 | permitted with conditions | decided fresh | — | ● |
| 5803 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5804 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-005 | permitted with conditions | decided fresh | — | ● |
| 5805 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5806 | Verify commit signatures on the protected release branch | VP-SC-004 | permitted | decided fresh | — |  |
| 5807 | Queue reminder sends so a retry storm cannot amplify | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5808 | Honour opt-out state at export time in the marketing job | VP-PD-007 | permitted | decided fresh | — |  |
| 5809 | Load the chart straight from the patient id in the query string | VP-RB-007 | denied | decided fresh | — |  |
| 5810 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-010 | permitted | decided fresh | — |  |
| 5811 | Store payment references, not card numbers, on the retry queue | VP-PD-003 | permitted | decided fresh | — |  |
| 5812 | Add regression tests for the note-render encoding path | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 5813 | Route records-release requests around the monthly billing queue to meet the state deadline | VP-CC-003 | permitted | decided fresh | — |  |
| 5814 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-003 | permitted with conditions | decided fresh | — | ● |
| 5815 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5816 | Drop the species field from the PDMP payload to clear schema errors | VP-CS-004 VP-PD-003 ⛔ | denied | refused at the floor | — |  |
| 5817 | Redact owner email addresses from claims connector debug output | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5818 | Hand the checkout redirect to the validated payment processor | VP-PD-009 | permitted | decided fresh | — |  |
| 5819 | Let clients re-order from prescriptions written last year | VP-CS-002 VP-GV-003 ⛔ | denied | refused at the floor | — |  |
| 5820 | Route diversion alerts to the medical director's queue within the hour | VP-CS-007 | permitted with conditions | decided fresh | — | ● |
| 5821 | Purge dispensing rows older than ninety days to shrink the table | VP-CS-006 VP-VC-006 ⛔ | denied | refused at the floor | — |  |
| 5822 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5823 | Map Catalyst One chemistry results to LOINC codes at ingest | VP-PO-010 | permitted | decided fresh | — | ● |
| 5824 | Move the ProCyte Dx onto the isolated device VLAN | VP-PO-006 | permitted | decided fresh | — |  |
| 5825 | Draft an amendment permitting telehealth-established VCPR in two more states | VP-PO-002 | denied | decided fresh | — |  |
| 5826 | Add contract tests for the pinned HL7 v2 profile | VP-PO-006 | permitted | decided fresh | — |  |
| 5827 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5828 | Wire Form 106 filing into the CI-gated compliance job so it can't be skipped | VP-DR-004 | permitted | decided fresh | — |  |
| 5829 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-VC-007 ⛔ | denied | refused at the floor | — |  |
| 5830 | Attach build provenance to the practice API release artefact | VP-SC-002 | permitted | decided fresh | — |  |
| 5831 | Move the release outside the emergency-hours freeze window | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5832 | Verify commit signatures on the protected release branch | VP-SC-003 | permitted | decided fresh | — | ● |
| 5833 | Validate webhook destinations against the outbound allowlist | VP-AS-003 | permitted | decided fresh | — |  |
| 5834 | Update the manifest and lockfile in the same commit | VP-SC-002 | permitted | disposed by citation | — |  |
| 5835 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted | decided fresh after a tie | none_tie |  |
| 5836 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 5837 | Publish the hotfix image straight from a laptop build | VP-SC-003 | denied | decided fresh | — |  |
| 5838 | Let one admin grant EPCS signing rights from the user screen | VP-CS-004 VP-CC-006 ⛔ | denied | refused at the floor | — |  |
| 5839 | Show the premises visit date on the large-animal chart header | VP-VC-005 | permitted | decided fresh | — |  |
| 5840 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5841 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-AS-001 | denied | decided fresh | — |  |
| 5842 | Make the feed directive expiry date a mandatory field | VP-VC-008 | permitted | decided fresh | — |  |
| 5843 | Cap analyzer retries at five with exponential backoff | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 5844 | Trust the modality's patient identifier tag exactly as sent | VP-PO-003 | denied | decided fresh | — |  |
| 5845 | Encrypt the owner address column at rest in the portal store | VP-PD-008 | permitted | decided fresh | — |  |
| 5846 | Submit an amendment adding a welfare-inspection remediation window | VP-PD-004 | denied | decided fresh | — |  |
| 5847 | Record artefact digests in the release ledger on publish | VP-SC-008 | permitted | decided fresh | — | ● |
| 5848 | Remove the written-prescription button from the dispensing screen | VP-CC-003 | denied | decided fresh | — | ● |
| 5849 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted | decided fresh | — |  |
| 5850 | Let Schedule II reorders go through the general purchasing API instead of CSOS | VP-DR-001 ⛔ | denied | refused at the floor | — |  |
| 5851 | Drop internal identifiers from the public error envelope | VP-AS-001 | permitted | decided fresh | — |  |
| 5852 | Enable the refill button on hydromorphone prescriptions | VP-CS-008 | denied | decided fresh | — |  |
| 5853 | Make the audit table append-only at the database level | VP-RR-004 | permitted | decided fresh | — |  |
| 5854 | Link the incident runbook from every breach-detection alert payload | VP-BN-003 | permitted | decided fresh | — |  |
| 5855 | Wrap result-to-patient binding in a single database transaction | VP-PO-003 | permitted | decided fresh | — | ● |
| 5856 | Stagger analyzer polling to flatten the morning load peak | VP-HA-005 | permitted | docketed — not charged | — |  |
| 5857 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5858 | Remove the necessity note from the bulk compounding form | VP-VC-001 VP-RR-006 ⛔ | denied | refused at the floor | — |  |
| 5859 | Add a job that escalates overdue welfare remediations to the medical director | VP-AW-004 | denied | bound by precedent | REC-S0196 |  |
| 5860 | Encrypt the owner address column at rest in the portal store | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 5861 | Read the practice id from the X-Practice request header | VP-RB-008 | denied | decided fresh | — |  |
| 5862 | Return a correlation id instead of a stack trace on error | — | permitted | docketed — nothing engaged | — |  |
| 5863 | Show the automated-triage disclosure on every turn of the conversation | VP-PS-002 | permitted | decided fresh | — |  |
| 5864 | Restrict claim payload deserialisation to known types | VP-AS-002 | permitted | disposed by citation | — |  |
| 5865 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 5866 | Configure a circuit breaker around the external lab client | — | permitted | docketed — nothing engaged | — |  |
| 5867 | Restrict extralabel ordering to licensed veterinarian accounts | VP-VC-008 | permitted | decided fresh | — |  |
| 5868 | Commit parsed HL7 segments as they arrive instead of at the end | VP-PO-010 | denied | decided fresh | — |  |
| 5869 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 5870 | Block certificate issuance when the signing veterinarian's licence has lapsed | VP-PH-004 | permitted | decided fresh | — |  |
| 5871 | Rewrite the Rego role-check rule using the adjudication service credentials | VP-RR-003 | denied | decided fresh | — |  |
| 5872 | Serialise inventory decrements with a row-level lock | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5873 | Record owner counselling on withdrawal periods in the discharge summary | VP-VC-004 | permitted with conditions | decided fresh | — | ● |
| 5874 | Configure retention periods per jurisdiction in the scheduler | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5875 | Review agent-authored tests for tautological assertions | VP-AI-006 | permitted | bound by precedent | REC-S0110 |  |
| 5876 | Turn the pound-kilogram mismatch error into a dismissable warning | VP-PS-001 VP-RB-007 ⛔ | denied | refused at the floor | — |  |
| 5877 | Publish a CycloneDX SBOM alongside each release digest | VP-SC-007 | denied | bound by precedent | REC-S0120 |  |
| 5878 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5879 | Extend the log redaction filter to the new owner phone field | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5880 | Let the triage assistant recommend a treatment plan without escalating to staff | VP-PS-002 | denied | decided fresh | — |  |
| 5881 | Parameterise the new chart-search query | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5882 | Replace the hand-rolled token hash with the vetted library | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5883 | Route diversion alerts to the medical director's queue within the hour | VP-CS-010 | permitted with conditions | decided fresh | — | ● |
| 5884 | Enforce authorisation server-side on the discharge summary route | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5885 | Import the prohibited extralabel substance list from a versioned fixture | VP-VC-008 | permitted | decided fresh | — |  |
| 5886 | Enforce a minimum touch-target size on the mobile check-in buttons | VP-AX-001 | permitted | decided fresh | — |  |
| 5887 | Validate webhook destinations against the outbound allowlist | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5888 | Assign a named reviewer to the vendored DICOM parser | VP-SC-007 | permitted | decided fresh | — |  |
| 5889 | Let assistants submit extralabel orders on the vet's behalf | VP-VC-001 VP-GV-007 ⛔ | denied | refused at the floor | — |  |
| 5890 | Add an admin path that updates the audit row to fix a typo | VP-RR-007 | denied | decided fresh | — |  |
| 5891 | Apply the state retention schedule to inactive owner records | VP-PD-004 | permitted | decided fresh | — |  |
| 5892 | Quarantine unmatched analyzer results for technician review | VP-PO-005 | permitted | decided fresh | — |  |
| 5893 | Hand the checkout redirect to the validated payment processor | VP-PD-005 | permitted | decided fresh | — |  |
| 5894 | Constrain pet-photo uploads by type, size and resolved path | VP-AS-005 | permitted | decided fresh after a tie | none_tie |  |
| 5895 | Expose the radiography panel to the internet for vendor support | VP-PO-003 | denied | decided fresh | — |  |
| 5896 | Bind each service account to a single practice id | VP-RB-002 | permitted | decided fresh | — |  |
| 5897 | Log the authenticated prescriber id on each dispensing event | VP-CS-010 | permitted | decided fresh | — |  |
| 5898 | Verify commit signatures on the protected release branch | VP-SC-009 | permitted with conditions | bound by precedent | REC-S0088 |  |
| 5899 | Restore the pre-charge renewal reminder that a billing rewrite had dropped | VP-CC-003 | permitted | decided fresh | — |  |
| 5900 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-006 | denied | decided fresh | — |  |
| 5901 | Tokenise the card number before the invoice row is written | VP-PD-005 | permitted with conditions | decided fresh | — | ● |
| 5902 | Move the release outside the emergency-hours freeze window | VP-HA-001 | permitted | decided fresh | — |  |
| 5903 | Make the consent signature pad completable by keyboard alone | VP-AX-002 | permitted | decided fresh | — |  |
| 5904 | Add a support endpoint that dumps the full owner record | VP-PD-006 | denied | decided fresh | — |  |
| 5905 | Scope the new reporting role to read-only endpoints | VP-RB-008 | permitted | bound by precedent | REC-S0112 |  |
| 5906 | Bind each service account to a single practice id | VP-RB-007 | permitted | decided fresh | — |  |
| 5907 | Preserve the original entry when a chart amendment is filed | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5908 | Attach the anaesthesia record to the procedure summary | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5909 | Gate the reactivation text campaign behind the same consent check as ordinary reminders | VP-CC-002 | permitted with conditions | decided fresh | — | ● |
| 5910 | Rank retrieval candidates using the audit register's findings | VP-GV-007 | denied | decided fresh | — | ● |
| 5911 | Sanitise filenames in the lab attachment upload handler | VP-AS-003 | permitted | disposed by citation | — |  |
| 5912 | Ship a down-migration for the visit-summary table change | VP-HA-001 | permitted | decided fresh | — |  |
| 5913 | Require an explicit share grant for cross-practice referrals | VP-RB-004 | permitted | decided fresh | — |  |
| 5914 | Ship beef-herd orders without the residue assessment step | VP-VC-003 VP-CC-005 ⛔ | denied | refused at the floor | — |  |
| 5915 | Bound HL7 segment length before the ORU^R01 parser runs | VP-PO-004 | permitted | decided fresh | — |  |
| 5916 | Withhold prescription finalisation from technician accounts | VP-RB-006 | permitted | disposed by citation | — |  |
| 5917 | Move the authorisation decision out of the portal frontend | VP-RB-004 | permitted | decided fresh | — |  |
| 5918 | Remove the ORM raw-SQL escape hatch from the billing report | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5919 | Derive tenant id from the session, never from a request header | VP-RB-004 | permitted | decided fresh | — |  |
| 5920 | Capture the research protocol number on regulated-facility visits | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5921 | Pin the schedule II refill count to zero in the prescription builder | VP-CS-009 | permitted | decided fresh | — |  |
| 5922 | Move the release outside the emergency-hours freeze window | VP-HA-003 | permitted | decided fresh | — |  |
| 5923 | Auto-close ketamine count mismatches under two millilitres | VP-CS-002 VP-BN-002 ⛔ | denied | refused at the floor | — |  |
| 5924 | Propose a sunset clause for the analytics pilot exception | VP-GV-004 | denied | decided fresh | — |  |
| 5925 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5926 | Warn when a dose falls outside the labelled species range | VP-VC-005 | permitted | decided fresh | — |  |
| 5927 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted | decided fresh | — | ● |
| 5928 | Enforce the tenant scope in the query layer, not the handler | VP-RB-003 | permitted | decided fresh | — |  |
| 5929 | Give consent withdrawal the same one-click path as granting it | VP-PD-004 | permitted with conditions | decided fresh | — | ● |
| 5930 | Pull in the charting library release carrying the open critical advisory | VP-SC-001 | denied | decided fresh | — |  |
| 5931 | Cover the new boarding endpoint with a role check test | VP-RB-002 | permitted | decided fresh | — |  |
| 5932 | Derive tenant id from the session, never from a request header | VP-RB-002 | permitted | decided fresh after a tie | none_tie |  |
| 5933 | Fail the build when the scanner reports anything above CVSS seven | VP-SC-008 | permitted with conditions | decided fresh | — | ● |
| 5934 | Point the resolver at the private registry before the public one | VP-SC-009 | permitted | decided fresh | — |  |
| 5935 | Add the transport welfare checklist to the boarding intake form | VP-AW-003 | denied | bound by precedent | REC-S0195 |  |
| 5936 | Let clients re-order from prescriptions written last year | VP-CS-006 VP-RR-003 ⛔ | denied | refused at the floor | — |  |
| 5937 | Separate the audit register store from the precedent store | VP-GV-006 | permitted | decided fresh | — |  |
| 5938 | Drop internal identifiers from the public error envelope | VP-AS-008 | permitted | docketed — not charged | — |  |
| 5939 | Add the new charting library licence to the allowlist | VP-SC-001 | permitted | disposed by citation | — |  |
| 5940 | Keep the retention clock unchanged when a record is edited | VP-RR-002 | permitted with conditions | decided fresh | — | ● |
| 5941 | Gate merges on a clean provenance verification step | VP-SC-002 | permitted | disposed by citation | — |  |
| 5942 | Add regression tests for the note-render encoding path | VP-AS-004 | permitted | decided fresh | — | ● |
| 5943 | Add a post-install step that pulls the package directly | VP-SC-003 | denied | decided fresh | — |  |
| 5944 | Redact owner email addresses from claims connector debug output | VP-PD-004 | denied | bound by precedent | REC-S0128 |  |
| 5945 | Hold medical-record releases until the client's balance is paid | VP-CC-004 | denied | decided fresh | — |  |
| 5946 | Populate DICOM species and breed tags from the patient record | VP-PO-005 | denied | bound by precedent | REC-S0118 |  |
| 5947 | Bound the results reconciler retry loop | VP-HA-004 | permitted | docketed — not charged | — |  |
| 5948 | Feed the customer's ticket body straight into the agent's task prompt | VP-AI-007 | denied | decided fresh | — |  |
| 5949 | Pin the radiography panel firmware version in the device inventory | VP-PO-008 | permitted with conditions | bound by precedent | REC-S0090 |  |
| 5950 | Overwrite the original diagnosis text when a chart is amended | VP-RR-007 | denied | decided fresh | — |  |
| 5951 | Wrap result-to-patient binding in a single database transaction | VP-PO-007 | permitted with conditions | decided fresh | — | ● |
| 5952 | Record artefact digests in the release ledger on publish | VP-SC-004 | permitted | decided fresh | — |  |
| 5953 | Switch invoice delivery to email before capturing e-signature consent | VP-CC-002 | denied | decided fresh | — |  |
| 5954 | Capture e-signature consent before switching a client to electronic invoices | VP-CC-003 | permitted | decided fresh | — |  |
| 5955 | Bound the results reconciler retry loop | VP-HA-002 | permitted | decided fresh | — |  |
| 5956 | Strip untrusted ticket text from the agent's instruction context | VP-AI-008 | permitted | decided fresh after a tie | none_tie |  |
| 5957 | Record artefact digests in the release ledger on publish | VP-SC-005 | permitted with conditions | decided fresh | — | ● |
| 5958 | Add the vetpoc-hl7-utils package the agent's patch imports | VP-AI-006 | denied | decided fresh | — | ● |
| 5959 | Write the decision rationale at resolution time, not on export | VP-RR-005 | permitted | decided fresh | — |  |
| 5960 | Assign a named reviewer to the vendored DICOM parser | VP-SC-004 | permitted | decided fresh | — |  |
| 5961 | Make Form 106 filing a manual checklist item instead of an automatic submission | VP-DR-001 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 5962 | Scope the new reporting role to read-only endpoints | VP-RB-005 | permitted | decided fresh | — |  |
| 5963 | Deny clinical note writes to the receptionist role | VP-RB-005 | permitted | decided fresh | — | ● |
| 5964 | Bind each service account to a single practice id | VP-RB-006 | permitted | disposed by citation | — |  |
| 5965 | Cover the new boarding endpoint with a role check test | VP-RB-003 | permitted | decided fresh | — |  |
| 5966 | Add the boarding service to the critical-service list in policy | VP-PO-004 | denied | decided fresh | — |  |
| 5967 | Revalidate the active session after a privilege change | VP-RB-003 | permitted | decided fresh after a tie | none_tie |  |
| 5968 | Serialise inventory decrements with a row-level lock | VP-HA-006 | permitted | docketed — not charged | — |  |
| 5969 | Encode clinical note text before rendering it in the portal | VP-AS-004 | permitted | decided fresh | — | ● |
| 5970 | Add the new charting library licence to the allowlist | VP-SC-003 | permitted | decided fresh | — |  |
| 5971 | Verify every imported package resolves in the registry before merge | VP-AI-006 | permitted | decided fresh | — | ● |
| 5972 | Mark required check-in fields with a red border and no error text | VP-AX-002 | denied | decided fresh | — |  |
| 5973 | Add a concurrency test for simultaneous discharge summary saves | — | permitted | docketed — nothing engaged | — |  |
| 5974 | Wrap result-to-patient binding in a single database transaction | VP-PO-009 | permitted with conditions | decided fresh | — | ● |
| 5975 | Publish the contest outcome as granted and refused counts | VP-GV-005 | permitted | decided fresh | — |  |
| 5976 | Add a weekly check over the orphaned-study reconciliation job output | VP-PO-009 | permitted | decided fresh | — |  |
| 5977 | Extend the log redaction filter to the new owner phone field | VP-PD-005 | permitted | decided fresh | — |  |
| 5978 | Record the analgesia rationale when a plan is declined | VP-AW-001 | denied | bound by precedent | REC-S0193 |  |
| 5979 | Publish the contest counts in the audit export header | VP-RR-006 | permitted with conditions | decided fresh | — | ● |
| 5980 | Record artefact digests in the release ledger on publish | VP-SC-001 | permitted | decided fresh | — | ● |
| 5981 | Remove the expiry from break-glass grants so support keeps access | VP-RB-001 VP-RB-007 ⛔ | denied | refused at the floor | — |  |
| 5982 | Backfill prescriber DEA expiry dates onto the credential record | VP-CS-009 | permitted | bound by precedent | REC-S0098 |  |
| 5983 | Pin the radiography panel firmware version in the device inventory | VP-PO-003 | permitted | decided fresh | — |  |
| 5984 | File a draft amendment codifying module-level coverage for generated code | VP-BN-002 | denied | decided fresh | — |  |
| 5985 | Remove the necessity note from the bulk compounding form | VP-VC-003 VP-SC-009 ⛔ | denied | refused at the floor | — |  |
| 5986 | Check object ownership before returning a patient chart | VP-RB-007 | permitted | disposed by citation | — |  |
| 5987 | Configure retention periods per jurisdiction in the scheduler | VP-RR-004 | permitted | decided fresh | — |  |
| 5988 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5989 | Version chart amendments instead of editing rows in place | VP-RR-007 | permitted with conditions | decided fresh | — | ● |
| 5990 | Enable video-only exams for prescribing in every state | VP-VC-008 | denied | decided fresh | — |  |
| 5991 | Show the premises visit date on the large-animal chart header | VP-VC-008 | permitted | decided fresh | — |  |
| 5992 | Call an external summarisation API from the agent's new helper | VP-AI-002 VP-PD-005 ⛔ | denied | refused at the floor | — |  |
| 5993 | Auto-fill the physical inventory count from the running ledger balance | VP-DR-003 VP-VC-005 ⛔ | denied | refused at the floor | — |  |
| 5994 | Restrict claim payload deserialisation to known types | VP-AS-007 | permitted | docketed — not charged | — |  |
| 5995 | Validate webhook destinations against the outbound allowlist | VP-AS-009 | permitted | docketed — not charged | — |  |
| 5996 | Replace the hand-rolled token hash with the vetted library | VP-AS-002 | permitted | decided fresh | — | ● |
| 5997 | Drop the practice filter from the referral search endpoint | VP-RB-001 VP-PO-005 ⛔ | denied | refused at the floor | — |  |
| 5998 | Check object ownership before returning a patient chart | VP-RB-003 | permitted | decided fresh | — |  |
| 5999 | Update the manifest and lockfile in the same commit | VP-SC-008 | permitted | decided fresh | — |  |
| 6000 | Keep the agent's scope off authorisation and dispensing paths | VP-AI-007 | permitted | decided fresh after a tie | none_tie |  |

⛔ marks a change that engaged an absolute provision — a floor no officer of this organisation has the authority to waive.

## How to check any of this

```
python3 harness/run_conformance.py     # 44 checks over the executed trace
python3 harness/mutation_matrix.py     # evidence the checks can fail
bash reproduce/run_all.sh              # rebuild everything, deterministically
```

Every row above is produced by replaying the corpus through `harness/engine.py`. No row is copied from an authored expectation, so the ledger cannot drift from the corpus files.
