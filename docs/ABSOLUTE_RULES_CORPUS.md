# Absolute Rules Corpus — Annotation Schema v0.1

*Digital Judiciary Research Program — statutes vs. absolutes classification*

## 1. Purpose

This corpus classifies individual normative clauses drawn from binding EU law (AI Act, GDPR, NIS2, DORA) and U.S. federal guidance (NIST SP 800-53 rev 5) into two tiers:

- **absolute** — a rule that applies unconditionally: it admits no derogation, requires no balancing exercise to determine what conduct it demands, is invariant under national transposition or agency tailoring, and binds by force of the instrument itself.
- **statute** — a rule that is real law (or binding-in-context guidance) but whose application is conditional: it carries derogations or exceptions, is proportionality- or risk-qualified, leaves discretion to member states or implementing bodies, or binds only through an attachment mechanism external to the text.

The binary is kept honest by recording *why* each clause landed where it did, via a four-criterion test scored per clause.

## 2. The four-criterion absoluteness test

A clause is classified **absolute** if and only if it passes ALL four criteria. Each criterion is recorded as `true` (passes) or `false` (fails), with a note.

| # | Criterion | Passes when… | Fails when… |
|---|-----------|--------------|-------------|
| C1 | `derogation_free` | No exception, derogation, or carve-out attaches to the rule, anywhere in the instrument (not just in the same sentence). | An "unless / except where / shall not apply to" clause exists, or another article (e.g. GDPR Art. 23, AI Act Art. 5(2)–(7)) can disapply or restrict it. |
| C2 | `determinate_conduct` | The rule specifies conduct or a result directly; a compliance decision does not require a balancing exercise. | The rule is qualified by "appropriate", "proportionate", "where necessary", "taking into account the state of the art / costs", or by organization-defined parameters (OSCAL ODPs). |
| C3 | `transposition_invariant` | The rule's content is fixed by the instrument itself, identical in every jurisdiction where it applies. | Content depends on member-state transposition (directives), member-state options (e.g. GDPR Art. 8(1) age of consent), or delegated/implementing acts that fill in essential terms (e.g. DORA Art. 20 RTS deadlines). |
| C4 | `context_independent_bindingness` | The rule binds addressees by force of the instrument (EU regulations; directives once transposed count as binding at the obligation level, but see C3). | Bindingness arises only through attachment: contract, certification, or a separate legal hook (NIST frameworks via FISMA / FedRAMP / DFARS). |

**Derived field:** `strictness` = number of criteria passed (0–4). This preserves a spectrum inside the binary: a strictness-3 statute is "near-absolute"; a strictness-1 statute is deeply conditional.

## 3. Key annotation rulings (edge cases)

**3.1 Scope-defining elements are not derogations.** A prohibition's own definitional threshold ("…in a manner that causes significant harm", "…leading to detrimental treatment that is unjustified") narrows what the rule *is*; it does not create a path to lawfully do the prohibited thing. Such clauses can still pass C1. By contrast, an explicit "this prohibition shall not apply to…" or "except where…" is a carve-out and fails C1. Example: AI Act Art. 5(1)(a) passes C1 (harm threshold is definitional); Art. 5(1)(f) fails C1 (medical/safety exception).

**3.2 Cross-instrument restrictability counts.** GDPR Art. 23 lets Union or member-state law restrict Arts. 12–22 (and Art. 5 insofar as it corresponds to those rights). Clauses within that reach fail C1 even if their own text is clean. Art. 7(3) (withdrawal of consent) sits outside Art. 23's list — one reason it survives as an absolute.

**3.3 Directives fail C3 at the member-state-facing layer.** NIS2 obligations are addressed to member states ("Member States shall ensure…"); the entity-facing rule exists only in national transposition, which may gold-plate or vary. All NIS2 clauses therefore fail C3, even determinate ones like the 24-hour early-warning deadline.

**3.4 Deferred essential terms fail C3.** Where the operative content (e.g. DORA incident-reporting time limits) is set by RTS/delegated acts, the clause fails C3 until those acts are in force and then must be re-annotated against the consolidated stack.

**3.5 NIST controls always fail C4** (voluntary framework; binding only via FISMA/OMB A-130, FedRAMP, DFARS 252.204-7012, or contract), and any control containing an OSCAL organization-defined parameter (`{{ insert: param, … }}`) fails C2. The `bindingness_context` field records the attachment mechanisms.

## 4. Entry fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Stable ID, e.g. `EU-AIACT-A5.1.a`, `US-NIST80053-AC-6` |
| `instrument` | string | Short instrument name (`EU AI Act`, `GDPR`, `NIS2`, `DORA`, `NIST SP 800-53r5`) |
| `reference` | string | CELEX number or NIST catalog version |
| `jurisdiction` | string | `EU` or `US` |
| `legal_nature` | enum | `regulation` \| `directive` \| `framework_guidance` |
| `locus` | string | Article/paragraph/point or control ID |
| `actor` | string | Addressee (provider, deployer, controller, member_state→entities, financial_entity, organization…) |
| `modality` | enum | `prohibition` \| `obligation` |
| `text` | string | Clause text |
| `text_fidelity` | enum | `verbatim_verified` (checked against source this build) \| `verbatim_unverified` (from model knowledge of the official text; verify before citation) \| `condensed` (faithful abridgement) |
| `criteria` | object | `{derogation_free, determinate_conduct, transposition_invariant, context_independent_bindingness}` each `{pass: bool, note: string}` |
| `strictness` | int | 0–4, derived |
| `classification` | enum | `absolute` (strictness = 4) \| `statute` |
| `conditionality` | object | `exceptions` (refs), `qualifiers` (balancing language found), `bindingness_context` (attachment mechanism, if any) |
| `notes` | string | Free text |

## 5. Known limitations of v0.1

Verification of quoted text used secondary mirrors for some clauses (EUR-Lex full-text pages exceed fetch limits); entries marked `verbatim_unverified` should be re-checked against the consolidated EUR-Lex texts before use in any adjudicative pipeline. Case law (CJEU) and delegated acts are not yet layered in; both can move a clause between tiers. National transpositions of NIS2 are not represented. Penalty tiers are noted but not modeled.
