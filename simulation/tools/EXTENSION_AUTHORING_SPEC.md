# Scenario-extension authoring spec (corpus 2.0.0)

You are writing two pure-data Python modules for ONE pack under
`simulation/<pack>/generator/`:

- `ext_vocab.py` — new families, new provisions, tau, scenario mappings, draft amendments
- `ext_changes.py` — narrative catalogue for the new families

They are merged into the pack's `vocab.py` / `changes.py` by a shim you do not write.
Validate with `python3 simulation/tools/validate_extension.py <pack-dir>`
until it prints `RESULT: OK` with no ERROR lines. Read the pack's existing `generator/vocab.py`
and `generator/changes.py` first and match their register exactly.

## Why this exists

The architect's scenario catalogue is `simulation/scenarios.json`
(39 scenario classes, each with harm classes and the packs it applies to). A survey found each
pack's constitution silent on 15–25 legal, compliance and reputational topics an expert would
refuse to ship without. You close every gap in your pack **by addition**: new provisions in new
families. You never edit an existing provision, factor or title (Axiom A3 — findings about
existing provisions are filed as draft amendments instead).

## Mechanics you must respect (these come from the generator and the checks)

1. **Factor pools are per family and sliced positionally.** The n-th provision of a family
   (0-based, in `PROVISIONS` list order) receives `comply[3n : 3n+8]` and `violate[2n : 2n+5]`
   with wrap-around, plus a synthetic `<slug>_control_evidenced` / `<slug>_control_absent`.
   So a family with k provisions needs ≥ 3k+5 comply factors and ≥ 2k+3 violate factors, and
   you should ORDER the pools so that provision n's most decisive violate factors sit at
   positions 2n and 2n+1, and its most characteristic comply factors at 3n..3n+2. Overlap
   between neighbouring provisions is expected and acceptable (it is how every existing family
   works), but the decisive factor of provision n must read as a violation of provision n.
2. **Every violate factor needs exactly one title** in `VIOLATION_CHANGES` — a pull-request
   title an engineer would write about their own change, that makes the violation legible
   WITHOUT naming the factor, any provision id, any regulation by name, or the word
   "scenario"/"axiom"/"provision"/"factor". Example from the existing catalogue:
   `"screening_served_from_cache_older_than_declared_interval": "Serve screening matches from a week-old cached list to cut latency"`.
3. **Every title must be a development change** — something a reviewer sees in a pull request
   (source, config, infra, schema/migration, pipeline, tests, policy repo, docs in the tree).
   Not an act on live data ("Correct the mis-posted fee by updating the row") and not a process
   with no artefact ("Complete the vendor review"). `changes.is_development_change` rejects a
   closed list of openings; the validator runs it. Prefer openings like "Add", "Remove", "Route",
   "Gate", "Move", "Cache", "Let", "Skip", "Drop", "Wire", "Emit", "Pin", "Make", "Switch", "Allow".
4. `COMPLIANT_CHANGES[fam]` needs ≥ 10 titles: changes that ENGAGE the family's provisions and do
   nothing wrong. Several of these should be **guard items** — compliant changes whose title
   *sounds* like a violation to a suspicious reader (a permitted exception correctly invoked; a
   correct-but-unusual implementation; a removal that is actually of dead code). Mark those in a
   comment. This is what lets the corpus measure over-blocking, not only over-permissiveness.
5. `FAMILY_CONTEXT[fam] = {"areas": [...], "services": [...]}` drawn ONLY from the pack's
   existing `AREAS` / `SERVICES` lists (in `vocab.py`, or in `changes.py` for vetpoc/semifab).
6. **Absolute means "no one below the legislature may decide"** (Definition 1), not "severe".
   Mark a provision absolute only when a statutory or safety floor makes risk acceptance
   impossible; for each absolute give a real instrument in `citation`. Aim for 30–40% of your
   new provisions absolute. An absolute must be `in_force`.
7. `status` ∈ in_force | deferred | advisory | readiness. Use deferred/advisory where the law
   really is (e.g. an instrument with a future application date), and say so in `source_status`.
8. `tau` per new family in 12..40. Families whose floors are strict-liability get low tau
   (15–20); ordinary operational families 22–34. Note a provision in a family with tau ≤ 20 is
   charged even when fully compliant (the prosecutor rates a fully compliant case at 20).
9. Ids continue the pack's convention and never collide (validator enforces the regex).
10. Citations: real instruments, correct pins, shelf-life checked as of 6 September 2026. If you
    are not certain an instrument is still in force, say "directionally supported, not verified"
    in `source_status` rather than asserting. Never invent a regulation. No paywalled text is
    reproduced — identifiers only for PCI DSS, ISO, IEC, SEMI, AICPA, NACHA.
11. **Nothing real and registrable** (no real package names, no real CVE exploit strings).

## `ext_vocab.py` schema

```python
FAMILIES = {
  "BN": {"title": "...", "risk": "<risk-framework label in the pack's style>",
         "comply": [...], "violate": [...]},
}
TAU = {"BN": 24, ...}
PROVISIONS = [
  {"id": "VP-BN-001", "family": "BN",
   "title": "<one sentence, 40-260 chars, drafted like the pack's existing titles>",
   "absolute": True, "citation": "...", "source_status": "...",
   "status": "in_force", "origin": "extension",
   "scenarios": ["S-04"], "harm_classes": ["legal", "reputational"]},
]
# Map EVERY existing family of the pack to scenario ids (the coverage matrix needs it):
FAMILY_SCENARIOS = {"CS": ["S-37", "S-03"], ...}
# Optional per-provision overrides for existing provisions:
PROVISION_SCENARIOS = {"VP-GV-002": ["S-05"], ...}
# Draft amendments: findings about EXISTING provisions (wrong pin, superseded instrument,
# overlap, an absolute that reads as a severity claim, a family whose citation is only
# "practice policy") — filed, not applied. Same dict shape as the pack's PROPOSED_AMENDMENTS
# (id, targets, raised_by, finding, proposed, why_not_applied, disposition="pending").
# Ids continue the pack's sequence (PA-01.. if the pack has none, else after the last).
# Write at least 4, grounded in what you actually read in the rulebook.
PROPOSED_AMENDMENTS = [...]
FLOOR_FACING_FAMILIES = {"BN", ...}   # new families whose cases concern a named service/asset
```

## `ext_changes.py` schema

```python
FAMILY_CONTEXT = {"BN": {"areas": [...], "services": [...]}}
COMPLIANT_CHANGES = {"BN": ["...", ...]}          # >= 10 each; mark guard items with a comment
VIOLATION_CHANGES = {"<violate factor>": "<title>", ...}   # every new violate factor
```

## Per-pack family plan (target 22–26 provisions; adjust family membership if the law demands)

Coverage rule: after your work, every scenario in scenarios.json whose `applies_to` names your
pack must map to at least one provision (new, or existing via FAMILY_SCENARIOS). The validator
enforces this. If a scenario should apply to your pack and does not, note it in your final report
rather than editing scenarios.json.

### vetpoc (ids VP-XX-NNN; existing families CS VC PO PD RB SC AI AS HA RR AW GV)
- BN Breach notification and client-data incidents (3): state breach-notification clock not
  configurable [absolute]; breach-detection telemetry and runbook wiring; vendor breach flow-down.
- DR DEA reporting, ordering and diversion (4): theft-or-loss (Form 106, 21 CFR 1301.76(b))
  filing never suppressed [absolute]; CSOS/Form 222 ordering records; biennial inventory job;
  diversion analytics not disabled.
- CC Client communications, consent, billing and records release (5): TCPA prior express
  consent for automated SMS/calls; wellness-plan auto-renewal and cancellation as easy as
  sign-up; E-SIGN consent before electronic records; client's right to a written prescription
  (portability); records release to owner within the state-board deadline.
- PS Patient safety, dosing and clinical decision support (4): weight-based dose check and unit
  confusion floor [absolute]; AI triage/advice tool never presents as a licensed vet and always
  hands off; critical-value alerting never suppressed; euthanasia consent and remains chain of
  custody [absolute].
- PH Public health, welfare and mandated reporting (4): reportable/zoonotic disease reporting
  never disabled [absolute]; rabies certificate requires licensee signature; suspected-abuse
  reporting path preserved; microchip registry data integrity.
- AX Accessibility and equal access (2): client portal WCAG 2.2 AA regression gate; assistive-
  technology-compatible consent and check-in flows.
- Consider one CS/AI-adjacent floor for minors (S-07): under-18 client accounts and consent by a
  parent for payment/records (COPPA does not apply to vet records; state contract law does — say so).

### semifab (ids SF-XX-NNN; existing EX DS SG RT WI RP SS AG TQ CR AS NC GV)
- IT ITAR and defence articles (4): ITAR technical data never to a foreign person, enclave
  segregation [absolute]; DDTC registration and licence check bound into access grant; ITAR data
  never on cloud outside the authorised boundary [absolute]; USML-vs-CCL classification recorded
  before ingest.
- SO Sanctions, anti-boycott and investment screening (3): OFAC SDN/50%-rule counterparty
  screening never bypassed [absolute]; anti-boycott request reporting (15 CFR 760); CFIUS /
  outbound-investment (31 CFR 850) checks before JV data sharing.
- RS Responsible sourcing and part integrity (4): conflict-minerals (3TG) supplier data
  pipeline; UFLPA/forced-labour supplier screening never disabled; counterfeit-part detection
  (AS5553/AS6171 identifiers) records; grey-market lot quarantine.
- EH Environment, health and safety (4): hazardous-gas monitoring alarms never suppressed
  [absolute]; lockout/tagout and E-stop states never overridden in software [absolute];
  effluent/PFAS/emissions reporting pipeline integrity; ESD and cleanroom telemetry retention.
- QS Quality system and customer change notification (4): PCN before a recipe change reaches
  customer lots; CAPA/8D records; APC/R2R model promotion gate; reticle/photomask revision
  traceability.
- OT OT network and remote access (4): IEC 62443 zone/conduit segmentation not bypassed; vendor
  remote sessions brokered, recorded, time-boxed; tool firmware patch provenance; PTP/NTP time
  integrity on equipment paths.

### frontierllm (ids FL-XX-NNN; existing MB TD PI AG LS EV SF IN FG BS IP SC AS GV)
- CS Child safety (4): CSAM detection and §2258A reporting never disabled [absolute]; known-CSAM
  hash-match pipeline in training ingest [absolute]; age-assurance and minor-interaction
  safeguards not removed; under-13 data excluded from training (COPPA).
- CB Catastrophic-risk evaluations (4): no release above the bio/chem uplift threshold without
  the mitigation package [absolute]; cyber-offence uplift eval gating; autonomous-replication /
  self-exfiltration eval; sandbagging and eval-awareness detection in the harness.
- WX Weight security and insider threat (3): egress/DLP monitoring on weight stores never
  disabled [absolute]; personnel vetting bound to weight access; export classification of
  weights (EAR advanced-computing rules) before transfer.
- TR Transparency and content provenance (4): synthetic-content marking (EU AI Act Art. 50(2),
  applicable 2 Aug 2026 — verify) never removed [absolute]; model/system card and GPAI
  documentation (Art. 53) current before release; SB 53 transparency report and whistleblower
  channel preserved; critical-incident reporting clock.
- UH User harm, persuasion and high-stakes use (5): crisis/self-harm safety classifier never
  weakened [absolute]; political-persuasion and election-influence policy enforcement; high-
  stakes advice (medical/legal/financial) handoffs and disclaimers; companion-dependence
  safeguards for minors; usage-policy enforcement and abuse monitoring pipeline.
- PV Privacy operations and multi-tenancy (4): erasure/unlearning requests propagate to training
  sets; zero-data-retention commitments enforced in retention code; tenant isolation of KV/prompt
  caches and fine-tune adapters [absolute]; annotator/data-worker data handling.

### dcvigil (ids DV-NNN continuing after DV-416; existing SC AC TI AG QA OP DR EV AI TG TL AP KS RS GV)
- LA Lawful access, legal hold and government requests (4): legal hold overrides every deletion
  path [absolute]; law-enforcement request path requires legal review and customer notice where
  lawful; conflicting cross-border disclosure duties resolved at design time; request-response
  export logging.
- LS Life-safety systems (3): fire suppression / EPO / UPS never actuated or suppressed by
  remediation [absolute]; generator and fuel test telemetry integrity; CER Directive physical-
  resilience reporting.
- EN Energy, water and ESG reporting (4): EED Delegated Reg. (EU) 2024/1364 reporting pipeline
  integrity; PUE/WUE computation method changes recorded; CSRD data lineage; waste-heat (EnEfG)
  reporting.
- CT Customer trust: tenant keys, offboarding, sub-processors (5): per-tenant keys / BYOK never
  pooled [absolute]; data return and deletion at contract end within SLA; sub-processor change
  notice before onboarding; customer audit-right evidence export; regulated-customer regime
  flags (DORA, HIPAA, PCI) honoured.
- OT OT protocols and segmentation (3): BACnet/Modbus/IPMI allow-list and zoning; SNMPv1/v2 and
  plaintext OT banned on new paths; edge-collector firmware provenance.
- SV Security assurance and product security (4): SBOM/VEX per release (CRA); PSIRT disclosure
  and patch SLA; penetration-test cadence evidence; status page / incident comms / RCA SLA.
- AX Accessibility (2): portal WCAG 2.2 AA gate; alerting never colour-only.

### meridian (ids MF-NNN continuing after MF-596, i.e. MF-601..; existing FC PD SS SP CQ LG PR RE DP FL AI AG CP EV GV)
- PS Payment security and open banking (4): SCA never bypassed outside RTS exemptions
  [absolute]; Verification of Payee on SEPA instant (Reg. (EU) 2024/886); UK APP-fraud
  reimbursement rules not configurable; RTP/FedNow request-for-payment fraud controls.
- FR Fraud, identity theft and account takeover (4): Red Flags programme (16 CFR 681) rules not
  disabled; step-up authentication on high-risk actions (FFIEC); synthetic-identity checks at
  onboarding; FCRA permissible purpose recorded before every pull [absolute].
- CN Consumer notices, e-consent and communications (5): E-SIGN consent before electronic
  disclosures; TCPA consent for autodialed/SMS; Reg P privacy notice and opt-out; FDCPA/Reg F
  contact caps in collections; Reg E provisional credit within ten business days.
- FP Fees, deposits and account handling (4): Reg DD fee disclosure; overdraft opt-in (Reg E
  §1005.17) [absolute]; Reg CC funds availability schedule not configurable [absolute]; escheat
  and dormant-account reporting.
- MP Military, servicemember and vulnerable-customer protections (3): MLA 36% MAPR and covered-
  borrower check [absolute]; SCRA rate cap and repossession protections; elder financial-
  exploitation reporting.
- DA Data rights and accessibility (3): GDPR Art. 15/20 access and portability; ADA/WCAG 2.2 AA
  and European Accessibility Act gate; CPRA opt-out preference signals honoured.
- VA Virtual assets and expanded financial-crime programme (3): Travel Rule for VASP transfers
  [absolute]; CTR filing (31 CFR 1010.311) never suppressed [absolute]; PEP/EDD and 314(a)
  screening pipeline.

## Deliverable

The two files, passing the validator, plus a short final message: counts, the absolutes you
chose and why each is a floor, any scenario you think should apply to the pack but is not in
`applies_to`, and any citation you could not verify (marked as such in `source_status`).
