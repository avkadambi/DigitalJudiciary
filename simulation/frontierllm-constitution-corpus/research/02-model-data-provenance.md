# Lane 02 — Model / Weight / Prompt / Training-Data Provenance (MBOM–PBOM layer)

Reusable open-source standards and test data for an open compliance test corpus governing
software change at a frontier LLM development company.

**Date of verification:** 2026-09-05
**Method:** every licence below was read from the repository's own `LICENSE` / `COPYING` /
`License.md` file after a shallow `git clone`, or from the licence statement on the
specification page itself. Nothing is inferred from a badge, a shields.io image, or a
third-party summary. Where no licence file exists, the entry says so and is marked
REFERENCE-ONLY.

**Out of scope (already verified by the prior survey, not re-derived here):** SLSA,
slsa-verifier testdata, sigstore-conformance, in-toto attestation, CycloneDX specification
(generic), CycloneDX sbom-examples, SPDX examples (generic), ossf/malicious-packages,
OSPS Baseline, sbom-utility drift corpus, OpenSSF Scorecard. This lane extends them into
the ML layer.

**Target corpus case shape** (what every "reuse path" below is aimed at):

```
(case_id, provisions_engaged[], factor_facts{name: bool}, expected_disposition)
```

---

## 0. Executive orientation — what actually exists

The ML provenance layer in September 2026 has **one** genuinely mature, conformance-tested,
permissively licensed standard — the OpenSSF **Open Model Signing (OMS) v1.0** specification
with its 86-case conformance suite. Everything else is either (a) a *schema* with example
documents but no negative cases, (b) a *taxonomy* usable as a factor vocabulary, or (c) a
policy document with no machine-readable artefact.

Three structural gaps worth stating up front, because the corpus has to fill them itself:

1. **SLSA has no ML/model track.** SLSA v1.2 defines exactly two tracks — Build and Source
   (verified at https://slsa.dev/spec/v1.2/tracks). There is no "SLSA for models". The
   model-provenance role that SLSA plays for packages is played by OMS + CycloneDX ML-BOM +
   SPDX 3.0 AI profile, which are not level-graded. Any "SLSA-for-weights" levels in the
   corpus are original work.
2. **There is no standard for prompt / system-prompt versioning.** Microsoft's Prompty — the
   nearest thing to a portable prompt file format — has no first-class `version` field; the
   spec puts version in an untyped `metadata` dict (§ 6 below). Langfuse's monotonic
   integer + mutable label model is the de facto pattern but is a product API, not a standard.
3. **Weight-exfiltration control catalogues are new and thin.** RAND's report is the canonical
   threat model but is **not** openly licensed. The SL5 Standard v0.1 (CC BY 4.0, OSCAL) is the
   first openly licensed control catalogue in this space and is only months old.

---

## 1. AI/ML BOM standards

### 1.1 CycloneDX ML-BOM (`modelCard`) — specification repo

| | |
|---|---|
| **Name** | CycloneDX specification — machine-learning-model component type + `modelCard` |
| **URL** | https://github.com/CycloneDX/specification |
| **Licence** | **Apache-2.0** — VERIFIED, `LICENSE` at repo root reads "Apache License Version 2.0, January 2004" |
| **Format** | JSON Schema (`schema/bom-1.5|1.6|1.7.schema.json`), XSD, protobuf |
| **Volume** | test resources: 155 files (1.5), 190 (1.6), 246 (1.7); 218 `valid-*.json` + 139 `invalid-*.json` across all versions; 5 ML-specific example files per recent version (`valid-machine-learning-{1.5,1.6,1.7}.{json,xml,textproto}` and `valid-machine-learning-considerations-env-{1.6,1.7}.*`) |
| **Vendor?** | **SAFE TO VENDOR** (Apache-2.0, attribution + NOTICE) |

Verified facts:

- `component.type` enum in **both 1.6 and 1.7** is exactly:
  `application, framework, library, container, platform, operating-system, device,
  device-driver, firmware, file, machine-learning-model, data, cryptographic-asset`.
  `machine-learning-model` and `data` are the two ML-relevant members.
- `modelCard` top-level properties (identical 1.6 → 1.7):
  `bom-ref, modelParameters, quantitativeAnalysis, considerations, properties`.
- `modelCard.modelParameters`: `approach{type}, task, architectureFamily, modelArchitecture,
  datasets[], inputs[].format, outputs[].format`.
- `modelCard.considerations`: `users[], useCases[], technicalLimitations[],
  performanceTradeoffs[], ethicalConsiderations[], fairnessAssessments[],
  environmentalConsiderations`.
- `environmentalConsiderations.energyConsumptions[]` carries
  `activity, activityEnergyCost{value,unit}, co2CostEquivalent, co2CostOffset,
  energyProviders[]{energySource, energyProvided, organization}` — the only standardised
  training-compute/energy accounting field found anywhere in this survey.
- `componentData` (the `data` component payload):
  `type, name, contents, classification, sensitiveData, graphics, description, governance`.
  `componentData.type` enum: `source-code, configuration, dataset, definition, other`.
- `dataGovernance` sub-object: `custodians[], stewards[], owners[]` (each a
  `dataGovernanceResponsibleParty`). This is the standardised **named-accountable-party**
  structure for a training dataset.
- `hash-alg` enum: `MD5, SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512,
  BLAKE2b-256, BLAKE2b-384, BLAKE2b-512, BLAKE3`. MD5 and SHA-1 are permitted by the schema —
  a *deliberately useful* negative-case generator for a "weak hash on weights" factor.
- Top-level 1.6/1.7 document keys include `declarations` and `formulation` — `formulation`
  carries `workflows` (the training pipeline as a build graph), which is the CycloneDX
  answer to "how was this checkpoint produced".

**Reuse path.** Two distinct uses.
(a) *Schema shape*: the corpus's MBOM fixture format should be a CycloneDX 1.6 document with
one `machine-learning-model` component + N `data` components, so cases are expressible as
real BOMs a real tool can parse.
(b) *Oracle*: the `valid-*` / `invalid-*` pairs in `tools/src/test/resources/<version>/` are a
ready-made (document, expected disposition) corpus for the "MBOM is well-formed" provision.
357 documents with an unambiguous binary verdict encoded in the filename.

**Caution.** `CycloneDX/bom-examples` (CC0-1.0, verified from its `LICENSE`, first line
"Creative Commons Legal Code / CC0 1.0 Universal") contains **no ML-BOM directory** —
its top level is `CBOM, HBOM, MBOM, OBOM, SBOM, SaaSBOM, VDR, VEX`, and `MBOM` there means
*Manufacturing* BOM, not Model BOM. `grep -rl modelCard` returns nothing. Do not cite
bom-examples as a source of ML-BOM samples; the ML samples live in the `specification` repo.

### 1.2 SPDX 3.0 AI profile and Dataset profile — model definitions

| | |
|---|---|
| **Name** | SPDX 3.0 model — `AI` and `Dataset` profiles |
| **URL** | https://github.com/spdx/spdx-3-model |
| **Licence** | **Community Specification License 1.0** — VERIFIED, `License.md` at repo root; every model file also carries an in-file `SPDX-License-Identifier: Community-Spec-1.0` header |
| **Format** | Markdown class/property/vocabulary definitions + JSON-LD serialisation + OWL/SHACL |
| **Volume** | AI profile: 4 classes, 22 properties, 2 vocabularies. Dataset profile: 1 class, 13 properties, 3 vocabularies. Core RelationshipType vocabulary: 79 entries |
| **Vendor?** | **REFERENCE-ONLY for the prose/model files** — Community-Spec-1.0 requires attribution to the Working Group with name + version + source, and is a specification licence, not a content licence. Cite and implement freely; do not paste the definitions into the corpus as if they were ours. |

Verified contents:

`model/AI/Classes/`: `AIPackage.md`, `EnergyConsumption.md`, `EnergyConsumptionDescription.md`,
**`InteractionTemplate.md`**.

`model/AI/Properties/` (22): `autonomyType, domain, energyConsumption, energyQuantity,
energyUnit, finetuningEnergyConsumption, hyperparameter, inferenceEnergyConsumption,
informationAboutApplication, informationAboutTraining, interactionTemplateDictionary,
interactionTemplateString, limitation, metric, metricDecisionThreshold,
modelDataPreprocessing, modelExplainability, safetyRiskAssessment, standardCompliance,
trainingEnergyConsumption, typeOfModel, useSensitivePersonalInformation`.

`model/Dataset/Properties/` (13): `anonymizationMethodUsed, confidentialityLevel,
dataCollectionProcess, dataPreprocessing, datasetAvailability, datasetNoise, datasetSize,
datasetType, datasetUpdateMechanism, hasSensitivePersonalInformation, intendedUse,
knownBias, sensor`.

`DatasetAvailabilityType` vocabulary (verbatim, 5 entries):
`clickthrough` (accessible only after affirmatively accepting terms) ·
`directDownload` (publicly downloadable) ·
`query` (accessible only through queries returning parts) ·
`registration` (email registration required, no affirmative acceptance) ·
`scrapingScript` (provider does not make the data available; must be reassembled by scraping).

**This is the single most directly reusable factor vocabulary in the whole lane** for
training-data acquisition legitimacy — it is the difference between "we downloaded it" and
"we scraped it around a click-through" expressed as a closed enum in an ISO-track standard.

**`InteractionTemplate` is the only standardised prompt-provenance class found anywhere.**
Its definition (verbatim from `model/AI/Classes/InteractionTemplate.md`): "An artifact that
defines the structure, formatting, and variable placeholders for AI model interactions."
It is a subclass of `/Core/Artifact` — so it inherits `verifiedUsing` (hashes) and full
relationship participation. Its role is set by the relationship used to attach it:

| Role | Relationship | scope |
|---|---|---|
| inference / chat template | `configures` | `runtime` |
| training template | `trainedOn` | `runtime` |
| pretrained template | `pretrainedOn` | `runtime` |
| finetuned template | `finetunedOn` | `runtime` |

Relevant `RelationshipType` entries verified in `model/Core/Vocabularies/RelationshipType.md`
(79 total): `trainedOn, pretrainedOn, finetunedOn, evaluatedOn, testedOn, configures,
hasDataFile, hasInput, hasOutput, hasPrerequisite, usesTool, generates, contains, dependsOn`.
The `hasDataFile` description explicitly routes training datasets to `trainedOn` and test
datasets to `testedOn` — i.e. SPDX has already drawn the train/test boundary the
contamination provisions need.

**Reuse path.** `trainedOn` / `finetunedOn` / `pretrainedOn` / `evaluatedOn` are the
checkpoint-lineage edge vocabulary. Adopt them verbatim as the corpus's lineage predicate
names; they are the only ISO-track set that distinguishes pretrain from finetune from eval.

### 1.3 SPDX 3.0 AI/Dataset example documents

| | |
|---|---|
| **Name** | spdx-examples — `ai/` and `dataset/` profiles |
| **URL** | https://github.com/spdx/spdx-examples |
| **Licence** | **CC0-1.0 for the SPDX documents themselves** — VERIFIED. `README.md` §Licenses: "SPDX documents in this repository are provided under CC0 1.0 Universal (CC0-1.0)". Repo `COPYING` is GPL-3.0 (applies to *source code*); documentation is CC-BY-4.0. In-file headers confirm: 7 files carry `SPDX-License-Identifier: CC0-1.0`, 4 carry `CC-BY-4.0` |
| **Format** | SPDX 3.0.1 JSON-LD |
| **Volume** | 3 documents. `ai/example01` (SimpleHTR, 118 elements), `ai/example02` (37 elements + a full model repo: `model.bin`, `train.py`, `evaluate.py`, `predict.py`, `preprocess.py`, `data/{train,valid,test}.txt`), `dataset/example01` (13 elements + `data.csv` + `codebook.csv`) |
| **Vendor?** | **SAFE TO VENDOR** — the `.spdx3.json` documents are CC0. Vendor the JSON; do **not** vendor `ai/example02/content/*.py` under the assumption it is CC0 (that is source code → GPL-3.0-or-later). |

Verified element composition:

- `ai/example01/spdx3.0/simplehtr-example.spdx3.json` — `profileConformance: [core, software, ai, dataset]`; types: 33 `software_File`, 32 `Relationship`, 21 `Person`, 10 `software_Package`, 10 `CreationInfo`, 5 `simplelicensing_LicenseExpression`, 2 `ai_AIPackage`, 1 `dataset_DatasetPackage`, 1 `software_Sbom`, 1 `expandedlicensing_CustomLicense`, 1 `Organization`, 1 `SpdxDocument`. Relationship mix: `contains`×7, `hasDeclaredLicense`×11, `hasConcludedLicense`×8, `dependsOn`×2, **`trainedOn`×2, `testedOn`×2**.
- `ai/example02/spdx3.0/sbom.spdx3.json` — 37 elements including 2 `LifecycleScopedRelationship`; relationship mix adds `generates`×2, `hasDataFile`, `hasDependencyManifest`, `hasDocumentation`, plus `trainedOn`, `testedOn`.
- AI/dataset package fields actually exercised: `ai_autonomyType, ai_domain,
  ai_energyConsumption, ai_hyperparameter, ai_informationAboutApplication,
  ai_informationAboutTraining, ai_metric, ai_modelDataPreprocessing, ai_safetyRiskAssessment,
  ai_typeOfModel, ai_useSensitivePersonalInformation, dataset_confidentialityLevel,
  dataset_dataCollectionProcess, dataset_dataPreprocessing, dataset_datasetAvailability,
  dataset_datasetSize, dataset_datasetType, dataset_datasetUpdateMechanism,
  dataset_hasSensitivePersonalInformation, dataset_intendedUse, dataset_knownBias`.
- `dataset/example01` uses `verifiedUsing` — i.e. a hash on the dataset package.

**Reuse path.** These are the only complete, valid, openly-licensed AIBOM documents in
existence. Vendor all three as the corpus's **positive fixtures** for "an adequate MBOM was
filed", then mutate them systematically (drop `trainedOn`, drop `hasDeclaredLicense` on the
dataset, set `dataset_datasetAvailability: scrapingScript`, remove `verifiedUsing`) to
generate negative cases with known expected dispositions. The mutation set writes itself
from the field list above.

### 1.4 OWASP AIBOM

| | |
|---|---|
| **Name** | OWASP AIBOM project (`www-project-aibom`) / OWASP GenAI Security "AI SBOM Initiative" |
| **URL** | https://github.com/OWASP/www-project-aibom · https://genai.owasp.org/owasp-aibom/ |
| **Licence** | **NOT VERIFIED — no licence statement on the workstreams page.** Do not assume CC-BY-SA from other OWASP projects |
| **Format** | Prose workstream index only |
| **Volume** | 10 workstreams (Pre-requisites, Foundational Best Practices, **Formats**, Tools, Sponsorship, Integrity/Quality, Policy, Content, Alliances, Engagement). Page text: "Stay tuned for detailed roadmaps and milestones" |
| **Vendor?** | **REFERENCE-ONLY** |

No published schema, no example corpus, no test data. The Formats workstream is the one to
watch; today it produces nothing machine-readable. Cite as evidence that a community
consensus process exists; do not build on it.

---

## 2. Model signing and transparency

### 2.1 OpenSSF Open Model Signing (OMS) specification + conformance suite — **the best source in this lane**

| | |
|---|---|
| **Name** | `ossf/model-signing-spec` — OMS v1.0 |
| **URL** | https://github.com/ossf/model-signing-spec |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE`; every spec/markdown file carries an in-file "Copyright 2024 The OpenSSF Authors / Licensed under the Apache License, Version 2.0" header |
| **Format** | Normative Markdown spec (`spec/v1.0.md`), 4 JSON Schemas, YAML-declared conformance cases, committed binary test vectors |
| **Volume** | **86 conformance tests** — 37 roundtrip (live sign → verify) + 49 verify (pre-committed offline bundles). Declared in 4 YAML files: `roundtrip.yaml` (37), `policy-negative.yaml` (28), `historical.yaml` (15), `policy-positive.yaml` (6). Plus a 60-row spec-coverage matrix in `conformance/TEST_CASES.md` and an `algorithm-registry.md` |
| **Vendor?** | **SAFE TO VENDOR** |

Spec structure (§ numbering the corpus can cite directly as *provisions engaged*):

```
§4   OMS Bundle Format      §4.1 signing method/verification material  §4.2 key types
§5   OMS Predicate          §5.1 predicateType   §5.2 predicate body (§5.2.1 resources, §5.2.2 serialization)
§6   Signing Procedure      §6.1 file enumeration (§6.1.1 symlinks, §6.1.2 path canonicalisation)
                            §6.2 path exclusion (§6.2.1 matching semantics)
                            §6.3 hashing/serialisation  §6.4 resource descriptors
                            §6.5 subject computation (§6.5.1 root digest)
                            §6.6 statement assembly  §6.7 DSSE signing  §6.8 bundle assembly
§7   Hashing Algorithms
§8   Verification Procedure §8.1 bundle parsing §8.2 signature §8.3 statement §8.4 manifest §8.5 unsigned files
§9   Bundle File Conventions
§10  Conformance
§11  Bundle Version History (§11.1 field differences, §11.2 verifier back-compat, §11.3 schema/conformance testing)
```

The conformance case declaration format is **already the target corpus schema**:

```yaml
- id: certificate-no-code-signing-eku_fail
  description: 'FAIL: Rejection when signing certificate lacks code_signing EKU'
  spec_refs: [ "§4.1" ]              # ← provisions engaged
  method: certificate                 # ← factor facts
  model: simple
  expected_signed_files: [signme-1, signme-2]
  bundle_source: { type: sign, key_group: no-code-signing }
  # file-level default: expect: fail  # ← expected disposition
```

Spec-reference frequency across all 86 cases (i.e. which provisions are most heavily tested):
`§4.1`×26, `§6.2`×19, `§11`×15, `§8.1`×9, `§6.1`×9, `§6.1.2`×9, `§8.2`×8, `§8.4`×6, `§8.5`×5,
`§6.2.1`×5, `§8.3`×3, `§6.4`×3, `§4.2`×3, `§6.1.1`×3, plus singletons.

Named negative cases worth lifting verbatim as factor facts (all verified present in
`policy-negative.yaml` / `TEST_CASES.md`):
`certificate-expired_fail`, `certificate-no-code-signing-eku_fail`,
`key-simple-wrong-key_fail`, `certificate-simple-wrong-ca_fail`,
`key-simple-tampered-content_fail`, `key-simple-missing-file_fail`,
`key-simple-extra-file_fail`, `key-tampered-with-ignore-unsigned_fail`,
`key-missing-file-with-ignore-unsigned_fail`, `malformed-wrong-predicate_fail`,
`key-simple-wrong-mediatype_fail`, `key-simple-wrong-payload-type_fail`,
`key-simple-wrong-statement-type_fail`, `key-simple-empty-resources_fail`,
`key-simple-missing-serialization_fail`, `sigstore-wrong-identity_fail`,
`sigstore-wrong-issuer_fail`, and five method-confusion cases
(`key-verify-as-certificate_fail`, `certificate-verify-as-key_fail`,
`sigstore-verify-as-key_fail`, `key-verify-as-sigstore_fail`,
`certificate-verify-as-sigstore_fail`).

Positive-path invariants (each is a corpus factor in its own right):
`_assert_key_uses_hint`, `_assert_predicate_type`, `_assert_resources_sorted`,
`_assert_no_shard_size_for_files`, `_assert_paths_canonical`, `_assert_algorithm_consistency`,
`_assert_subject_name`, `_assert_root_digest`, `key-simple-deterministic`.

`schemas/v1.0/predicate.schema.json` (verbatim, load-bearing):

```
required: [resources, serialization]; additionalProperties: false
resources[].{name, digest (^[0-9a-f]+$), algorithm ∈ {sha256, blake2b, blake3}}
  name: "For 'files' method: relative POSIX path from the model root.
         For 'shards' method: 'path:start:end' (inclusive start, exclusive end)."
serialization.{method ∈ {files, shards}, hash_type, allow_symlinks}  (all required)
```

`algorithm-registry.md`: `sha256` REQUIRED (default); `blake2b` OPTIONAL; `blake3` OPTIONAL.
Signature algorithms delegate to the Sigstore Algorithm Registry.

**Reuse path — highest priority.** Vendor `conformance/test/test-cases/*.yaml` wholesale and
re-key it onto the corpus's own provision numbering. It is 86 pre-validated
(case_id, provisions_engaged, factor_facts, expected_disposition) tuples about model-hash
approval, produced by a standards body, Apache-2.0. This is the backbone of the model-hash
approval provision and should be treated as the reference implementation of the corpus's own
case format.

### 2.2 sigstore/model-transparency (`model_signing` CLI/library)

| | |
|---|---|
| **Name** | sigstore/model-transparency |
| **URL** | https://github.com/sigstore/model-transparency |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` |
| **Format** | Python library + `model_signing` CLI; signature is a Sigstore protobuf Bundle in JSON containing a DSSE envelope containing an in-toto Statement v1 |
| **Volume** | 136 files under `tests/` + `scripts/tests/`; 21 serialization fixtures; 21 signing payload fixtures; **18 cross-version backward-compatibility scripts** over 6 released versions × 3 signing methods (v0.2.0, v0.3.1, v1.0.0, v1.0.1, v1.1.0 × {certificate, elliptic-key, sigstore}), each with a committed golden `model.sig` |
| **Vendor?** | **SAFE TO VENDOR** |

Verified signature payload (decoded from `scripts/tests/v1.1.0-sigstore/model.sig`):

```json
{ "_type": "https://in-toto.io/Statement/v1",
  "subject": [ { "name": "v1.1.0-sigstore",
                 "digest": { "sha256": "61d4849d…d226" } } ],
  "predicateType": "https://model_signing/signature/v1.0",
  "predicate": {
    "resources": [ { "name": "signme-1", "algorithm": "sha256", "digest": "f631…85e1" },
                   { "name": "signme-2", "algorithm": "sha256", "digest": "32dc…0028" } ],
    "serialization": { "method": "files", "hash_type": "sha256", "allow_symlinks": false,
                       "ignore_paths": [".gitignore",".gitattributes",".git",".github",
                                        "ignore-me","model.sig"] } } }
```

Bundle keys: `mediaType`, `verificationMaterial`, `dsseEnvelope`.
`payloadType: application/vnd.in-toto+json`.

Named serialization fixtures (each is a distinct edge case, and each has `_shard` and
`_small_shards` variants — 21 total): `sample_model_file`, `sample_model_folder`,
`empty_model_file`, `empty_model_folder`, `deep_model_folder`,
`model_folder_with_empty_file`, `symlink_model_folder`.

Supported hash identifiers found in source: `sha256`, `sha256-sharded-1024`, `blake2b`,
`blake3`. `_hashing/` module: `hashing.py`, `io.py`, `memory.py`.

Identity/workload model (verified from README, useful as factor values for "who signed"):
OIDC providers `https://accounts.google.com`, `https://github.com/login/oauth`,
`https://token.actions.githubusercontent.com`, `https://login.microsoftonline.com`;
workload identities for GitHub Actions, GitLab CI, GCP service accounts, Buildkite.
Also supports PKCS #11 URIs (RFC 7512) with NIST P-256/384/521 — i.e. **HSM-backed signing
is a first-class, testable factor**, not an aspiration.

**Reuse path.** The 18 historical `test-verify-*.sh` scripts are a *temporal* oracle: they
assert that a verifier built today still accepts bundles produced by six older releases.
That is exactly the "signature format migration must not break attestation continuity"
provision, with committed evidence. Vendor the `scripts/tests/v*/` trees.

### 2.3 in-toto attestation predicates

| | |
|---|---|
| **Name** | in-toto/attestation `spec/predicates/` |
| **URL** | https://github.com/in-toto/attestation |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` ("Copyright 2021 in-toto Developers / Licensed under the Apache License, Version 2.0") |
| **Format** | Markdown predicate definitions + protobuf |
| **Volume** | 14 predicate types: `provenance, link, release, reference, runtime-trace, scai, spdx, spdx2, spdx3, cyclonedx, svr, test-result, vuln, vulns_02` |
| **Vendor?** | **SAFE TO VENDOR** |

**There is no ML/model predicate in in-toto.** OMS defines its own
(`https://model_signing/signature/v1.0`) outside the registry. Note this as a gap.

Directly useful here beyond the prior survey's coverage: `test-result` (a standardised
pass/fail attestation — the natural carrier for "this checkpoint passed the eval gate"),
`vsa` (Verification Summary Attestation — the natural carrier for "policy engine approved
this weight release"), and `scai` (Supply Chain Attribute Assertion — the carrier for
"trained in enclave X on hardware Y").

### 2.4 safetensors — and why pickle is the threat

| | |
|---|---|
| **Name** | huggingface/safetensors, and specifically `attacks/` |
| **URL** | https://github.com/huggingface/safetensors |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` |
| **Format** | Rust + Python; format = 8-byte little-endian header length, JSON header, contiguous tensor data |
| **Volume** | `attacks/` contains **8 working exploit pairs** (create + get_pwned) plus 3 format-abuse attempts: `torch_ace_*`, `paddle_ace_*`, `tf_ace_*`, `tf_safe_ace_*`, `torch_dos_*`, `numpy_dos_*`, `safetensors_abuse_attempt_{1,2,3}.py` |
| **Vendor?** | **SAFE TO VENDOR the code (Apache-2.0)** — but treat as live malware samples: the ACE scripts really do execute code on load. Vendor as *fixtures behind a guard*, never as runnable test steps. |

The threat, stated precisely from `attacks/README.md`: `torch.load` / `pickle` deserialisation
executes arbitrary code via `__reduce__`; the same holds for PaddlePaddle `.pdparams` and
Keras `.h5`. A weights file is therefore *executable content*, and "checkpoint arrived as
`.pt`" is a security-material fact, not a format preference.

The three `safetensors_abuse_attempt_*` scripts document the format's own hardened boundary
and are the clean source of negative cases for a "weights container is well-formed" provision.
Verified proposals from the README:
1. header length larger than the file → out-of-bounds crash;
2. multi-gigabyte JSON header → load-delay DoS (mitigation: header-proportion cap);
3. negative / out-of-file offsets → rejected;
4. **overlapping offsets → NOT ok** — small file declaring many tensors over the same region
   is a memory-amplification DoS; mitigation is a contiguity + non-overlap check;
5. offsets mismatching declared shape+dtype → validated against;
6. mmap'd file modified while open → out of scope (attacker already has the filesystem);
7. serde JSON deserialisation abuse → no known flaw.

**Reuse path.** Factor `weights_format_permits_code_execution` becomes decidable from the file
extension plus loader, with these scripts as the evidence base. Cases 1–5 give five
well-formedness negative cases for the container itself.

### 2.5 Hugging Face Xet — content-defined chunking and hash-based model identity

| | |
|---|---|
| **Name** | huggingface/xet-core + the Xet protocol spec in hub-docs |
| **URL** | https://github.com/huggingface/xet-core · https://github.com/huggingface/hub-docs/tree/main/docs/xet |
| **Licence** | **Apache-2.0** — VERIFIED for both (`xet-core/LICENSE`; `hub-docs/LICENSE`) |
| **Format** | Rust implementation + normative Markdown spec (13 documents: `hashing, chunking, deduplication, shard, xorb, file-id, file-reconstruction, download-protocol, upload-protocol, auth, api, index`) |
| **Vendor?** | **SAFE TO VENDOR** |

Verified mechanics relevant to model identity:

- All Xet hashes are 32 bytes (256 bits).
- **Chunk hash** = BLAKE3 *keyed* hash under a fixed 32-byte `DATA_KEY`
  (`[102,151,245,119,91,149,80,222,49,53,203,172,165,151,24,28,157,228,33,16,155,235,43,88,180,208,176,75,147,173,242,41]`).
- **Xorb hash / file hash** = Merkle root over chunk hashes, where internal nodes hash the
  string `"{chunk_hash:x} : {size}\n"` concatenated in order, under a fixed `INTERNAL_NODE_KEY`.
- **File ID** is retrieved from the `X-Xet-Hash` response header on the Hub `resolve` URL for
  a given `namespace/repository/{branch|commit}/filepath`.

**Reuse path.** Xet gives a *chunk-level* identity that survives partial re-upload, where OMS
gives a *file-level* signed manifest. A frontier lab's real question — "is the 400 GB
checkpoint on the serving host bit-identical to the approved one, and can I tell cheaply?" —
needs both. Factor pair: `approved_model_digest_recorded` (OMS root digest) and
`served_artifact_hash_matches_registry` (Xet file ID). Note in the corpus that the two hash
spaces are *not* interchangeable; a case where a team substitutes one for the other is a
good negative.

### 2.6 OpenSSF AI/ML Security Working Group

| | |
|---|---|
| **Name** | ossf/ai-ml-security |
| **URL** | https://github.com/ossf/ai-ml-security |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` |
| **Format** | Markdown documents |
| **Volume** | `landscape/` (10 docs incl. `AI-related_threats.md`, **`Provenance_and_Legal_Issues.md`**, `Personas.md`, `OpenSSF_Projects.md`); `telemetry/` (18 docs incl. `Understanding_the_AI_Supply_Chain.md`, `AI_Standards_and_Best_Practices.md`, `AI_Regulations.md`) |
| **Vendor?** | **SAFE TO VENDOR** (Apache-2.0), but it is prose |

WG status: OpenSSF **sandbox** level, chartered 2023-09-05. Co-chairs Jay White (GitHub) and
Mihai Maruseac (Google — also the model-transparency lead). Scope list from the README names
the threat classes the corpus's provisions must map to: adversarial attacks, model inversion,
**poisoning**, evasion, data extraction/jailbreaking, point-in-time datasets, social
engineering, threat democratisation, accidental threats (secret leakage), prompt injection,
**membership inference**, model vulnerability management, **model integrity**.

**Reuse path.** Provision taxonomy source, not test data. `Provenance_and_Legal_Issues.md` is
the closest thing to a rationale document for why an MBOM provision exists at all — useful for
the corpus's commentary field, quotable under Apache-2.0 with attribution.

---

## 3. Model metadata and cards

### 3.1 Hugging Face model card / dataset card metadata spec

| | |
|---|---|
| **Name** | huggingface/hub-docs — `modelcard.md`, `datasetcard.md`, `eval_results.yaml` |
| **URL** | https://github.com/huggingface/hub-docs |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` |
| **Format** | YAML front-matter spec, validated server-side by the Hub on `git push` |
| **Volume** | `modelcard.md` 56 lines, `datasetcard.md` 101 lines, `eval_results.yaml` 30 lines |
| **Vendor?** | **SAFE TO VENDOR** |

Machine-readable? **Yes, in effect** — `modelcard.md` states: "Properties will be validated by
the Hub when git pushing changes to your README.md file." There is no published JSON Schema,
but the field set is normative and enforced.

Model card fields (verified): `language[], license, license_name, license_link, library_name,
tags[], datasets[], buckets[], metrics[], base_model, model-index[]`.

`model-index[].results[]` structure — this is the **checkpoint-lineage + eval-provenance**
shape worth adopting:

```
task:    {type (req), name}
dataset: {type (req), name (req), config, split, revision, args{}}
metrics: [{type (req), value (req), name, config, args{}, verifyToken}]
source:  {name, url (req if source present)}
```

`revision` on the dataset is a commit SHA — the only place in any model-metadata standard
where the *exact* evaluation dataset commit is a first-class field. `verifyToken` is
described as "a signature that can be used to prove that evaluation was generated by Hugging
Face (vs. self-reported)" — a standardised **self-reported vs. attested** distinction.

The newer `eval_results.yaml` format tightens this: `dataset.{id, task_id, revision}`,
`value`, `verifyToken` ("proof that evaluation is provably auditable and reproducible … was
run in a HF Job using inspect-ai or lighteval"), `date`, `source.{url, name, user, org}`,
`notes`.

`base_model` is documented as possibly a **list** (for merges) — the corpus needs a
multi-parent lineage factor, not a single-parent one.

Dataset card fields relevant to training-data provenance: `license, license_name,
license_link, license_details, source_datasets[], annotations_creators[]
(crowdsourced|found|expert-generated|machine-generated), language_creators[],
size_categories[], task_categories[], task_ids[], configs[].data_files[].{split, path},
dataset_info.features[]`.

**Reuse path.** Adopt `base_model` (list), `datasets[]`, and `model-index.results[].dataset.revision`
as the corpus's lineage factor names. Adopt the `verifyToken` present/absent distinction as
the `eval_result_attested_not_self_reported` factor — it is the cleanest existing expression
of that idea.

### 3.2 Google Model Card Toolkit

| | |
|---|---|
| **Name** | tensorflow/model-card-toolkit |
| **URL** | https://github.com/tensorflow/model-card-toolkit |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE` ("Copyright 2019 The TensorFlow Authors") |
| **Format** | JSON Schema (draft-07) at `model_card_toolkit/schema/v0.0.1|v0.0.2/model_card.schema.json` + protobuf `model_card.proto` |
| **Volume** | 2 schema versions, 1 proto |
| **Status** | **Unmaintained** — last commit verified 2023-07-26 |
| **Vendor?** | **SAFE TO VENDOR** (Apache-2.0), but do not depend on the package |

Machine-readable? **Yes** — this is the original JSON Schema for model cards and the direct
ancestor of the CycloneDX `modelCard`. Verified top-level properties:
`schema_version, model_details, model_parameters, quantitative_analysis, considerations`.

```
model_details:        {name, overview, owners, version, licenses, references,
                       citations, documentation, path}
model_parameters:     {model_architecture, data, input_format, input_format_map,
                       output_format, output_format_map}
quantitative_analysis:{performance_metrics, graphics}
considerations:       {users, use_cases, limitations, tradeoffs, ethical_considerations}
```

**Reuse path.** Historical justification for the CycloneDX field names, and a drop-in
JSON Schema if a lighter-weight validation target than a full CycloneDX BOM is wanted.
Prefer CycloneDX 1.6 `modelCard` for anything new.

### 3.3 Datasheets for Datasets (Gebru et al.)

| | |
|---|---|
| **Name** | Datasheets for Datasets |
| **URL** | https://arxiv.org/abs/1803.09010 |
| **Licence** | **arXiv perpetual non-exclusive licence (`nonexclusive-distrib/1.0`)** — VERIFIED from the arXiv abstract page licence link. **Not** CC BY |
| **Format** | Prose questionnaire in a PDF. **Not machine-readable. No schema.** |
| **Vendor?** | **REFERENCE-ONLY** — the arXiv non-exclusive licence permits distribution of the paper, not the creation of derivative schemas presented as ours |

The section structure (motivation, composition, collection process, preprocessing/cleaning/
labeling, uses, distribution, maintenance) is the conceptual ancestor of the SPDX Dataset
profile and the Croissant RAI extension. **Use those instead** — they say the same things in
a schema, under licences that permit implementation.

### 3.4 IBM AI FactSheets 360

| | |
|---|---|
| **Name** | IBM AI FactSheets 360 |
| **URL** | https://aifs360.res.ibm.com/ (methodology paper: https://arxiv.org/abs/2006.13796) |
| **Licence** | **NOT VERIFIED** — the site was unreachable at verification time (expired TLS certificate on `aifs360.res.ibm.com`, robots fetch failed). No licence was established |
| **Vendor?** | **REFERENCE-ONLY, and cite with care** |

FactSheets is a *methodology* (elicit facts per role per lifecycle stage) rather than a fixed
schema — by design it has no universal field list, which makes it a poor oracle source. Its
one transferable idea is **per-lifecycle-stage, per-role fact ownership**, which SPDX 3.0
already encodes better via `dataGovernance` custodians/stewards/owners and CycloneDX's
equivalent. Do not block on this source.

---

## 4. Dataset provenance

### 4.1 Data Provenance Initiative — the largest verified licence audit

| | |
|---|---|
| **Name** | Data Provenance Collection |
| **URL** | https://github.com/Data-Provenance-Initiative/Data-Provenance-Collection · https://www.dataprovenance.org/ |
| **Licence** | **Apache-2.0 for the repository and its summaries** — VERIFIED, root `LICENSE`. (The *underlying* datasets keep their own licences; the audit records those.) |
| **Format** | JSON, one file per collection, dict keyed by dataset identifier |
| **Volume** | **VERIFIED BY COUNT:** text — 111 files, **3,719 dataset records**; speech — 95 files, 95 records; video — 105 files, 105 records. **3,919 records total.** Plus 15 controlled-vocabulary files in `constants/` |
| **Vendor?** | **SAFE TO VENDOR** |

Every record carries exactly these 26 fields (verified frequency across all 3,719 text
records — the first 23 are on 100% of records):
`Unique Dataset Identifier, Dataset Name, Paper Title, Dataset URL, GitHub URL,
Hugging Face URL, Papers with Code URL, ArXiv URL, Semantic Scholar Corpus ID, Collection,
Collection URL, Languages, Task Categories, Text Sources, Model Generated, Format,
Human Annotation, Derived from Datasets, Bibtex, Creators, Licenses, License Verified By,
Dataset Filter IDs` (3719 each), plus `Inferred Metadata` (3693), `License Notes` (3636),
`Text Metrics` (3633).

The load-bearing structure is `constants/license_classes.json` — **66 entries** mapping a
licence name to a 3-tuple:

```
"Apache License 2.0"                → ["All",  "1", "0"]
"Academic Research Purposes Only"   → ["Acad", "1", "1"]
"AI2 ImpACT License - Low Risk"     → ["All",  "1", "1"]
```

i.e. `[permitted-use-class ∈ {All, Acad, NC, ?}, attribution-required ∈ {0,1},
share-alike ∈ {0,1}]`. `constants/custom_license_classes.json` adds **79** URL-keyed entries
for bespoke terms-of-use pages, including explicit `["?","?","?"]` unknowns.

Also verified as directly reusable: `Licenses` is an *array* of
`{License, License URL}` — the audit records that a single dataset can be under **conflicting**
licences (Alpaca: "OpenAI" terms AND "CC BY-NC 4.0"), and `License Notes` records licence
*changes over time* ("License formerly Apache 2.0, switched"). `Model Generated` records which
model produced synthetic data (Alpaca: `["OpenAI GPT-3"]`) — the raw material for a
model-terms-of-service-contamination factor.

`License Verified By` is a first-class field: the audit distinguishes *self-reported* from
*human-verified* licence claims. That distinction is a factor.

**Reuse path — highest priority for the data lane.** Adopt `license_classes.json` verbatim as
the corpus's training-data licence lattice, giving three orthogonal, decidable booleans per
dataset (`permits_commercial_use`, `attribution_required`, `share_alike_required`) plus an
explicit `unknown` state. Then use the 3,719 real records as case *seeds*: any dataset whose
`Licenses` array contains two entries with different use-classes is an automatic
`conflicting_licence_claims` positive.

### 4.2 Croissant (MLCommons) + Croissant-RAI

| | |
|---|---|
| **Name** | mlcommons/croissant |
| **URL** | https://github.com/mlcommons/croissant · spec at https://docs.mlcommons.org/croissant/docs/croissant-spec-1.1.html |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE.md` |
| **Format** | JSON-LD over schema.org; RDF vocabularies in `docs/croissant.ttl`, `croissant_rai.ttl`, `croissant_geo.ttl` |
| **Volume** | **63 example dataset descriptions** (`datasets/0.8` 15, `datasets/1.0` 33, `datasets/1.1` 15); **30 validator test cases with expected error text** (`python/mlcroissant/.../tests/graphs/{0.8:15, 1.0:12, 1.1:3}`); **13 valid/invalid task JSON-LD fixtures** in `tasks/testdata` |
| **Vendor?** | **SAFE TO VENDOR** |

Verified negative-case structure — each case directory holds `metadata.json` **plus
`output.txt` containing the expected validator error**, e.g.
`python/mlcroissant/mlcroissant/_src/tests/graphs/1.0/mlfield_bad_type/output.txt`:

```
Found the following 1 error(s) during the validation:
  -  "a-record-set/first-field" should have an attribute "@type":
     "http://mlcommons.org/croissant/Field". Got https://schema.org/WRONG_TYPE instead.
```

This is a (input, expected disposition, expected reasoning) triple — the closest match in the
whole survey to a corpus case with a *stated ground for the decision*, not just a verdict.
Case names are self-describing and map to provisions:
`distribution_missing_property_content_url`, `distribution_missing_encoding_format`,
`distribution_bad_contained_in`, `distribution_bad_id`, `mlfield_missing_source`,
`mlfield_bad_source`, `mlfield_bad_type`, `mlfield_bad_array_shape`,
`mlfield_bad_array_definition`, `metadata_bad_type`, `recordset_wrong_join`,
`recordset_bad_type`, `recordset_missing_context_for_datatype`,
`recordset_missing_property_name`, `multilingual_fields`.

Metadata level (verified from a real 1.1 example): `@context, @type, name, description,
alternateName, conformsTo ("http://mlcommons.org/croissant/1.1"), creator, url, keywords,
distribution, recordSet`. The spec recommends the licence be "the URL of a known license,
e.g., one of the licenses listed at https://spdx.org/licenses/" — Croissant explicitly binds
dataset licensing to the SPDX identifier list.

**Croissant-RAI** (`docs/croissant-rai-spec.md` + `croissant_rai.ttl`) adds a
**29-term responsible-AI provenance vocabulary**, verified verbatim:
`rai:dataCollection, rai:dataCollectionType, rai:dataCollectionRawData,
rai:dataCollectionTimeframe (+Start/End), rai:dataCollectionMissingData,
rai:dataPreprocessingProtocol, rai:dataManipulationProtocol, rai:dataImputationProtocol,
rai:dataAnnotationProtocol, rai:dataAnnotationPlatform, rai:dataAnnotationAnalysis,
rai:annotationsPerItem, rai:annotatorDemographics, rai:machineAnnotationTools,
rai:dataUseCases, rai:dataBiases, rai:dataLimitations, rai:dataSocialImpact,
rai:personalSensitiveInformation, rai:dataReleaseMaintenancePlan`.

**Reuse path.** Croissant is the dataset-side counterpart to CycloneDX ML-BOM. Use it as the
fixture format for "a dataset was properly described", vendor the 30 negative cases as the
oracle, and use `rai:personalSensitiveInformation` and `rai:dataCollectionType` as factor
names. `conformsTo` gives a version-pinning factor for free.

### 4.3 Common Pile — the licence-permissiveness lattice

| | |
|---|---|
| **Name** | r-three/common-pile (The Common Pile v0.1) |
| **URL** | https://github.com/r-three/common-pile |
| **Licence** | **MIT** — VERIFIED, root `LICENSE` ("MIT License / Copyright (c) 2023 r-three") |
| **Format** | Python; `common_pile/licenses.py` is a string enum |
| **Vendor?** | **SAFE TO VENDOR** |

Verified from `common_pile/licenses.py`, docstring verbatim:

> "By 'Permissive' we mean licenses that are in the Gold, Silver, or Bronze lists of the
> Blue Oak Countil (https://blueoakcouncil.org/list), even if they have copyleft requirements."

Enum members: `PD, CC0, CC_PDM, CC_BY (+ /3.0, /2.5, /2.0), CC_BY_SA (+ /3.0, /2.5, /2.1,
/1.0), APACHE_2, GFDL`, with a regex normaliser that **raises `ValueError` on any
unrecognised licence string** — i.e. fail-closed licence classification, which is exactly the
behaviour a compliance provision should require.

**Reuse path.** Two things. (1) The Blue Oak Council Gold/Silver/Bronze rating is the
ready-made ordinal for `training_data_licence_permissiveness`. (2) The fail-closed
`ValueError` is the correct *expected disposition* for the `unrecognised_licence_string`
case — vendor the normaliser as an executable oracle.

### 4.4 Dolma

| | |
|---|---|
| **Name** | allenai/dolma (toolkit) |
| **URL** | https://github.com/allenai/dolma |
| **Licence** | **Apache-2.0** — VERIFIED, root `LICENSE`. (The *dataset* on the HF Hub is separately licensed under the AI2 ImpACT licence — do not conflate.) |
| **Format** | Rust + Python; document format documented in `docs/data-format.md` |
| **Vendor?** | **SAFE TO VENDOR the toolkit.** REFERENCE-ONLY for the dataset |

Verified per-document provenance fields from `docs/data-format.md`:
`"source"` — **MANDATORY**, "source of the data, such as peS2o, common-crawl, etc.";
`"added"` — OPTIONAL, "timestamp ai2 acquired this data";
`"created"` — OPTIONAL, "timestamp when orig document was created (best-guess if not
available)".

Also ships `docs/deduplication.md` and `docs/taggers.md` — the tagger framework is the
mechanism by which per-document provenance/quality attributes are attached and later filtered
on, which is structurally the same operation as evaluating a boolean factor over a corpus.

**Reuse path.** `source` (mandatory) / `added` / `created` is the minimum viable
per-document provenance triple. Adopt it as the schema for
`training_document_source_recorded`. The mandatory/optional split is itself the factor
boundary.

### 4.5 C2PA and the CAWG training/data-mining assertion

| | |
|---|---|
| **Name** | C2PA specification; CAWG "Training and Data Mining Assertion" v1.1 |
| **URL** | https://spec.c2pa.org/ · https://cawg.io/training-and-data-mining/1.1/ |
| **Licence (C2PA spec)** | **CC BY 4.0** — VERIFIED, stated on the C2PA 2.2 specification index page: content "licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license" |
| **Licence (CAWG spec)** | **W3C Patent Policy (2004) governance; sample/reference code under Apache-2.0** — VERIFIED from the spec's own statement. Terms derive from the Decentralized Identity Foundation Project Charter. This is *not* a content licence for the prose — treat prose as REFERENCE-ONLY, reference code as SAFE TO VENDOR |
| **Vendor?** | C2PA spec: **SAFE TO VENDOR with attribution** (CC BY 4.0). CAWG: **REFERENCE-ONLY for prose** |

**Important correction to a common misconception:** the training/data-mining assertion is
**not** in the C2PA core standard — it lives in the CAWG spec, and C2PA has published a
clarification to that effect ("C2PA Clarifies: No TDM Assertions in the Standard").
Get the label right or the corpus cites a provision that does not exist.

Verified assertion label: **`cawg.training-mining`**. Four pre-defined entry keys, each with a
`use` value drawn from `allowed | notAllowed | constrained`:

| Key | Meaning |
|---|---|
| `cawg.data_mining` | text/data extraction for pattern analysis |
| `cawg.ai_inference` | asset used as input to a trained model |
| `cawg.ai_training` | training **non-generative** models |
| `cawg.ai_generative_training` | training **generative** models |

Custom keys are permitted if they conform to C2PA label syntax; the `cawg.` prefix is reserved.

**Reuse path.** This is the most precise available vocabulary for asset-level training
permission, and it makes a distinction (generative vs. non-generative training) that no other
source makes. Adopt the four keys as factor names directly, with the tri-state value
(`constrained` is not a boolean — the corpus needs either a third state or a
`permission_is_conditional` companion factor).

### 4.6 Machine-readable training-data opt-out signals

Four mechanisms exist. They are at very different maturity levels and the corpus should say so.

**(a) IETF AIPREF working group — the standards track.**

| | |
|---|---|
| **URL** | https://datatracker.ietf.org/wg/aipref/documents/ |
| **Licence** | **BCP 78 / IETF Trust Legal Provisions; code components under the Revised BSD License** — VERIFIED from the draft's own boilerplate |
| **Status** | 2 WG documents at **-05 / -07, both dated 2026-08-18, both Proposed Standard**, plus 8 related individual drafts |
| **Vendor?** | **REFERENCE-ONLY for the drafts; code components SAFE TO VENDOR (Revised BSD)** |

- `draft-ietf-aipref-vocab-07` — *A Vocabulary For Expressing AI Usage Preferences*.
  Verified: only **two** concrete categories are defined —
  **`train-ai`** ("Using an asset to modify the learned parameters of an AI model that is used
  to generate synthetic content in one or more modalities") and
  **`search`** ("Use of an asset in an application where the primary purpose … is to select
  assets and direct users to the location of those assets"). Extension is via
  standards-track RFC. **The published draft text still carries the warning that it reflects
  "NO CONSENSUS of the Working Group either in whole or part."** Do not present this
  vocabulary as settled.
- `draft-ietf-aipref-attach-05` — *Associating AI Usage Preferences with Content in HTTP*.
  Verified: defines the HTTP header field **`Content-Usage`** (a structured-field dictionary),
  e.g. `Content-Usage: train-ai=n`; and a new **`Content-Usage` rule in robots.txt**, e.g.
  `Content-Usage: train-ai=n` or `Content-Usage: /ai-ok/ train-ai=y`. **No well-known URI is
  defined.**
- Related individual drafts (names verified, all pre-adoption): `draft-illyes-aipref-cbcp`,
  `draft-zehta-aipref-exclusions`, `draft-zehta-aipref-parameters`,
  `draft-wallace-aipref-grant-binding`, `draft-reilly-aipref-compliance`,
  `draft-hood-aipref-earmark`, `draft-madhavan-aipref-displaybasedpref`,
  `draft-altanai-aipref-realtime-protocol-bindings`, `draft-farzdusa-aipref-enduser`.

**(b) W3C TDM Reservation Protocol (TDMRep).**

| | |
|---|---|
| **URL** | https://www.w3.org/community/reports/tdmrep/CG-FINAL-tdmrep-20240510/ |
| **Licence/status** | **Final Community Group Report under the W3C Community Final Specification Agreement (FSA)**, copyright 2021–2024 the TDMRep CG contributors. **Not a W3C Standard.** VERIFIED from the report itself |
| **Vendor?** | **REFERENCE-ONLY** (implement freely under the FSA; do not republish as ours) |

Verified fields: `tdm-reservation` — boolean, `1` = rights reserved (consult the policy),
`0` = not reserved (may be mined without contacting the rightsholder); `tdm-policy` — a URL to
a machine- or human-readable TDM policy document.

Four delivery mechanisms, with a **normative precedence order**:
`/.well-known/tdmrep.json` (JSON array of location-pattern rules) → HTTP headers (currently
the preferred method) → HTML `<meta>` in `<head>` → embedded metadata in EPUB 2 / EPUB 3 / PDF.
"Later findings supersede earlier ones."

**That precedence order is itself a corpus case family**: a site that declares `0` in
`.well-known` and `1` in an HTTP header has a defined answer, and getting it wrong is a
compliance failure with a citable provision.

**(c) robots.txt AI directives (`GPTBot`, `Google-Extended`, `CCBot`, etc.).**
**No standard, no licence, no normative document.** These are per-vendor user-agent tokens
documented only in vendor product pages. The AIPREF `Content-Usage` robots.txt rule in (a) is
the attempt to standardise this. Treat vendor tokens as **de facto factor values with no
authority behind them** — a case can turn on whether a crawl respected `GPTBot: Disallow`, but
the corpus should not cite a "standard" for it, because there is none.

**(d) `ai.txt`.** No IETF/W3C track, no normative specification located. **REFERENCE-ONLY;
do not build provisions on it.**

---

## 5. Eval / benchmark contamination

### 5.1 LLMSanitize

| | |
|---|---|
| **Name** | ntunlp/LLMSanitize |
| **URL** | https://github.com/ntunlp/LLMSanitize |
| **Licence** | **Apache-2.0** — VERIFIED, `LICENSE.txt` ("Apache License Version 2.0 / Copyright (c) 2023 Salesforce, Inc.") |
| **Format** | Python library, methods split into `open_data_methods/` and `closed_data_methods/` |
| **Volume** | **12 implemented detection methods** |
| **Vendor?** | **SAFE TO VENDOR** |

Verified method table (`Method | Use Case | Method Type | Model Access`):

| Method | Use case | Type | Access |
|---|---|---|---|
| `gpt-2` | Open-data | string matching | – |
| `gpt-3` | Open-data | string matching | – |
| `exact` | Open-data | string matching | – |
| `palm` | Open-data | string matching | – |
| `gpt-4` | Open-data | string matching | – |
| `platypus` | Open-data | embeddings similarity | – |
| `guided-prompting` | Closed-data | prompt engineering / LLM-based | black-box |
| `sharded-likelihood` | Closed-data | model likelihood | white-box |
| `min-prob` | Closed-data | model likelihood | white-box |
| `cdd` | Closed-data | memorisation / likelihood | black-box |
| `ts-guessing-question-based` | Closed-data | model completion | black-box |
| `ts-guessing-question-multichoice` | Closed-data | model completion | black-box |

**Reuse path.** The `open-data` vs `closed-data` × `white-box` vs `black-box` split is the
right factor decomposition for a contamination provision: *what evidence was available to the
checker* determines what disposition is reachable. A case where a team asserts "no
contamination" using only a black-box method against an open-data benchmark is a
methodological failure with a citable ground. Vendor the library as an executable oracle for
the `exact` / `gpt-3` / `palm` n-gram overlap definitions, which are otherwise scattered
across five papers' appendices.

### 5.2 LM Contamination Index

| | |
|---|---|
| **Name** | hitz-zentroa/lm-contamination |
| **URL** | https://github.com/hitz-zentroa/lm-contamination |
| **Licence** | **NO LICENCE FILE IN THE REPOSITORY** — VERIFIED by inspection (`LICENSE`, `LICENSE.md`, `COPYING` all absent). Default: all rights reserved |
| **Format** | `data.json`, a flat JSON array |
| **Volume** | **375 records**, VERIFIED by count |
| **Vendor?** | **REFERENCE-ONLY — DO NOT VENDOR** |

Record shape (all 375 carry these; `models` appears on 236, `source` on 374):
`{corpus, dataset, train_split, dev_split, test_split, train_percent, dev_percent,
test_percent, guidelines, source, models?}`.

The verdict vocabulary is a **three-valued ordinal per split**: `clean` / `suspicious` /
`contaminated`. Example verified record:
`{"corpus":"ChatGPT","dataset":"CoNLL03","train_split":"contaminated",
"dev_split":"contaminated","test_split":"contaminated","guidelines":null}`.

**Reuse path — schema only, not data.** Adopt the per-split three-valued verdict shape:
a contamination factor must be evaluated separately for train / dev / test, and must admit a
`suspicious` middle state, because the underlying detection methods cannot produce a clean
boolean. Do not copy the 375 records; they are unlicensed and the verdicts are hand-curated
against a moving target.

### 5.3 Contamination_Detector

| | |
|---|---|
| **Name** | liyucheng09/Contamination_Detector |
| **Licence** | **NO LICENCE FILE** — VERIFIED by inspection |
| **Vendor?** | **REFERENCE-ONLY — DO NOT VENDOR** |

Ships `reports/` with per-benchmark contamination reports and an internet-search-based method.
Methodologically interesting, legally unusable.

---

## 6. Prompt / system-prompt versioning

**Finding: there is no standard.** No SDO has published one. What exists is one file format
and several product APIs. The relevant partial exception is SPDX 3.0's `InteractionTemplate`
(§ 1.2 above), which is the only *standard* class for a prompt artifact — but it defines
identity and lineage relationships, not versioning.

### 6.1 Microsoft Prompty

| | |
|---|---|
| **Name** | microsoft/prompty |
| **URL** | https://github.com/microsoft/prompty |
| **Licence** | **MIT** — VERIFIED, root `LICENSE` ("MIT License / Copyright (c) Microsoft Corporation") |
| **Format** | `.prompty` = YAML front-matter + Markdown body. Types defined in **TypeSpec** (`schema/model/*.tsp`), emitted to 7 runtimes |
| **Volume** | **180 machine-readable conformance vectors** with `input` / `expected` pairs, VERIFIED by count from `schema/tsp-output/.typra-generated/vectors.json` |
| **Status** | **v2 alpha** — README states "The API, file format, and tooling are under active development and may change" |
| **Vendor?** | **SAFE TO VENDOR (MIT)** — but pin a commit; the format is explicitly unstable |

Verified conformance vector distribution:

| by contract | n | | by stage | n |
|---|---|---|---|---|
| TurnConformance | 38 | | load | 28 |
| LoadConformance | 28 | | agent | 28 |
| Renderer | 28 | | wire | 28 |
| WireConformance | 28 | | render | 23 |
| Processor | 23 | | process | 21 |
| Parser | 19 | | parse | 19 |
| DiscoveryConformance | 16 | | enrichment | 9 |
| | | | discovery | 7 |
| | | | render_segments, replay, turn, processStream | 5,5,5,2 |

Vector shape (verified sample): `{contract, namespace, group, operation, params, returns,
sync, vector:{name, stage, provider, input, expected}}`.

**The versioning gap, stated precisely.** Verified from `spec/spec.md` §, the `.prompty`
front-matter properties are `name, displayName, description, metadata`, where `metadata` is
documented as "**Arbitrary metadata (authors, tags, version, etc.)**" typed as a bare `dict`.
There is **no typed `version` field**. A pipeline five stages deep (LOAD → RENDER → PARSE →
EXECUTE → PROCESS) with a formal TypeSpec schema and 180 conformance vectors nevertheless
leaves prompt version identity untyped and unvalidated.

**Reuse path.** (a) Vendor the 180 vectors as the structural exemplar for machine-readable
conformance cases — they are the cleanest `{input, expected}` corpus in this lane after OMS.
(b) Cite the untyped `metadata.version` as the *justification* for a corpus provision
requiring prompt version identity: the leading open prompt format does not enforce it, so the
lab must.

### 6.2 Langfuse

| | |
|---|---|
| **Name** | langfuse/langfuse |
| **URL** | https://github.com/langfuse/langfuse |
| **Licence** | **MIT ("MIT Expat") for everything outside `ee/`, `web/src/ee/`, `worker/src/ee/`; those directories are under `ee/LICENSE` (enterprise)** — VERIFIED, root `LICENSE`, "Copyright (c) 2023-2026 ClickHouse, Inc." |
| **Format** | Fern API definitions (`fern/apis/server/definition/prompts.yml`, `prompt-version.yml`) → OpenAPI |
| **Vendor?** | **SAFE TO VENDOR the MIT-licensed API definitions.** Check `ee/` provenance before touching anything else |

Verified prompt data model from `fern/apis/server/definition/prompts.yml`:

```
PromptMeta: { name, type ∈ {text, chat}, versions: list<integer>,
              labels: list<string>, tags: list<string>, lastUpdatedAt, lastConfig }
GET  /api/public/v2/prompts/{promptName}?version=<int>&label=<str>&resolve=<bool>
     "Label of the prompt to be retrieved. Defaults to 'production' if no label or version is set."
POST /api/public/v2/prompts       — "Create a new version for the prompt with the given name"
DELETE /api/public/v2/prompts/{promptName}?label=&version=
```

The semantics (verified from the docs data-model page): **versions are immutable and
auto-increment** (1, 2, 3…); **labels are mutable pointers** to a version; `production` is the
default resolution label; `latest` always points at the newest version. There is also a
`resolve` flag for **prompt dependencies** — composed prompts with dependency tags, which
means prompt composition is itself a lineage graph.

**Reuse path.** This is the de facto prompt-versioning model and the right shape for the
corpus's factors: separate the immutable content identity (`version`) from the mutable
deployment pointer (`label`). Almost every real incident in this space is a *label* moving
without review, not a *version* changing. The corpus factors must distinguish them.

### 6.3 promptfoo

| | |
|---|---|
| **Name** | promptfoo/promptfoo |
| **URL** | https://github.com/promptfoo/promptfoo |
| **Licence** | **MIT** — VERIFIED, root `LICENSE` ("Copyright (c) Promptfoo 2025", full MIT grant text) |
| **Vendor?** | **SAFE TO VENDOR** |

Eval-configuration and assertion framework; useful as a *harness* for running corpus cases
that need an LLM in the loop, not as a source of provenance schema. Its assertion vocabulary
(`equals`, `contains`, `llm-rubric`, `javascript`, …) is a reasonable model for expressing
expected dispositions that are not simple booleans.

### 6.4 PromptLayer, LangSmith

Commercial SaaS. **No open licence located for either's prompt schema.**
**REFERENCE-ONLY.** Do not model corpus factors on undocumented proprietary semantics.

---

## 7. Weight-exfiltration and model-security control catalogues

### 7.1 RAND, *Securing AI Model Weights*

| | |
|---|---|
| **Name** | RAND RR-A2849-1, *Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models* |
| **URL** | https://www.rand.org/pubs/research_reports/RRA2849-1.html |
| **Licence** | **PROPRIETARY — NOT open, NOT Creative Commons.** VERIFIED, quoting the report's own statement: *"This document and trademark(s) contained herein are protected by law. This representation of RAND intellectual property is provided for noncommercial use only. Unauthorized posting of this publication online is prohibited; linking directly to this product page is encouraged. Permission is required from RAND to reproduce, or reuse in another form, any of its research documents for commercial purposes."* |
| **Volume** | **38 meaningfully distinct attack vectors**; five security levels (SL1–SL5) |
| **Vendor?** | **REFERENCE-ONLY — DO NOT VENDOR, DO NOT REPRODUCE.** Cite by link only. A frontier lab is a commercial context; even internal reuse of the text needs RAND permission |

This is the canonical threat model and the origin of the SL1–SL5 vocabulary that the rest of
the field now uses. The corpus can and should *reference* SL levels as an external frame, and
can build its own factor set covering the same attack surface, but must not lift RAND's text
or tables.

### 7.2 SL5 Standard for AI Security — **the openly licensed successor**

| | |
|---|---|
| **Name** | SL5 Standard for AI Security, v0.1 |
| **URL** | https://standard.sl5.org/ (paper: https://arxiv.org/abs/2605.08449) |
| **Publisher** | Security Level 5, a registered 501(c)(3), developed with frontier AI labs, government partners and security experts |
| **Licence** | **CC BY 4.0 for the standard prose, figures, and the SL5-authored OSCAL selections / parameter assignments / supplemental guidance; Apache-2.0 for the repository code; incorporated NIST material is US-government public domain** — VERIFIED from https://standard.sl5.org/license, which states "SL5-authored prose and figures are licensed under CC BY 4.0" and applies the same to the OSCAL artifacts |
| **Format** | **OSCAL profile** importing NIST SP 800-53 Rev. 5 controls, plus a separately published local catalog for SR-13 from NIST SP 800-161 Rev. 1 Upd. 1 |
| **Volume** | **60 controls across 12 families**, VERIFIED: AC 7, CM 2, IA 1, IR 1, PE 6, PM 1, PS 3, RA 1, SA 5, SR 11, SC 15, SI 7 |
| **Scope** | Five security streams: network, physical, machine, personnel, supply chain. Includes ICD 705-derived physical facility requirements |
| **Vendor?** | **SAFE TO VENDOR with attribution** (CC BY 4.0 + Apache-2.0). Note v0.1 maturity |

**Reuse path — this is the answer for weight-access control.** It is (a) openly licensed,
(b) machine-readable OSCAL, (c) anchored in NIST SP 800-53 Rev. 5 so it composes with any
existing control mapping the lab already has, and (d) scoped precisely to frontier model
weight protection. Import the OSCAL profile and use control IDs as **provisions engaged**
directly — `SC-*` and `AC-*` control IDs become citable provisions in corpus cases about
weight access, and the SR family (11 controls) covers the supply-chain side that this lane's
MBOM provisions attach to.

Caveat to record in the corpus: **v0.1, months old, explicitly focused on "long lead-time
controls".** Pin the version in every citation.

---

## 8. Safe-to-vendor vs reference-only — consolidated

### SAFE TO VENDOR

| Source | Verified licence | What to take |
|---|---|---|
| `ossf/model-signing-spec` | Apache-2.0 | 86 conformance cases + 4 JSON Schemas + spec § numbering |
| `sigstore/model-transparency` | Apache-2.0 | 18 cross-version verify scripts + golden bundles + 21 serialization fixtures |
| `CycloneDX/specification` | Apache-2.0 | ML-BOM schemas + 357 valid/invalid documents |
| `spdx/spdx-examples` (**documents only**) | CC0-1.0 | 3 SPDX 3.0 AI/dataset JSON-LD documents |
| `Data-Provenance-Initiative/Data-Provenance-Collection` | Apache-2.0 | 3,919 records + 66-entry + 79-entry licence class tables |
| `mlcommons/croissant` | Apache-2.0 | 30 negative cases with expected error text + 63 examples + RAI vocabulary |
| `r-three/common-pile` | MIT | Blue Oak permissiveness lattice + fail-closed normaliser |
| `allenai/dolma` (toolkit) | Apache-2.0 | document provenance format |
| `huggingface/hub-docs` | Apache-2.0 | model-index + eval_results schemas, Xet protocol spec |
| `huggingface/xet-core` | Apache-2.0 | chunk/file hashing reference |
| `huggingface/safetensors` (`attacks/`) | Apache-2.0 | 8 exploit pairs + 3 format-abuse cases — **guard them** |
| `microsoft/prompty` | MIT | 180 conformance vectors (pin the commit; v2 alpha) |
| `langfuse/langfuse` (outside `ee/`) | MIT Expat | prompt version/label API schema |
| `promptfoo/promptfoo` | MIT | assertion harness |
| `ntunlp/LLMSanitize` | Apache-2.0 | 12 contamination detection methods |
| `in-toto/attestation` | Apache-2.0 | `test-result`, `vsa`, `scai` predicates |
| `ossf/ai-ml-security` | Apache-2.0 | threat taxonomy prose |
| `tensorflow/model-card-toolkit` | Apache-2.0 | model card JSON Schema (unmaintained) |
| SL5 Standard v0.1 | CC BY 4.0 (+ Apache-2.0 code) | OSCAL profile, 60 controls / 12 families |
| C2PA specification | CC BY 4.0 | manifest/assertion model |

### REFERENCE-ONLY

| Source | Reason |
|---|---|
| RAND RR-A2849-1 | Proprietary; noncommercial use only; commercial reuse needs permission |
| `spdx/spdx-3-model` (AI/Dataset profile definitions) | Community-Spec-1.0 — spec licence with mandatory WG attribution; implement, don't republish |
| CAWG training-mining spec prose | W3C Patent Policy governance, no content licence (reference code is Apache-2.0) |
| W3C TDMRep CG report | W3C Community Final Specification Agreement; not a W3C Standard |
| IETF AIPREF drafts | BCP 78 / TLP; drafts, no WG consensus; code components Revised BSD |
| `hitz-zentroa/lm-contamination` | **No LICENSE file** — schema idea only, not the 375 records |
| `liyucheng09/Contamination_Detector` | **No LICENSE file** |
| Datasheets for Datasets | arXiv `nonexclusive-distrib/1.0`, not CC BY; not machine-readable |
| IBM AI FactSheets 360 | Licence could not be verified (site TLS certificate expired) |
| OWASP AIBOM | No licence statement located; no schema or corpus published |
| robots.txt AI directives, `ai.txt` | No normative specification exists |
| PromptLayer, LangSmith | Proprietary, no open schema |

---

## 9. Recommended factor names

Derived from verified field names and enums above. Each is a boolean unless marked. Provenance
of each name is given so it is auditable.

### 9.1 Model-hash approval

| Factor | Source of the name |
|---|---|
| `model_signature_bundle_present` | OMS §4 bundle |
| `model_signature_verifies_against_trusted_identity` | OMS §8.2 + model-transparency identity/provider |
| `signing_method_matches_declared_verification_material` | OMS §4.1, the 5 method-confusion `_fail` cases |
| `signing_certificate_within_validity_period` | OMS `certificate-expired_fail` |
| `signing_certificate_has_code_signing_eku` | OMS `certificate-no-code-signing-eku_fail` |
| `signing_key_backed_by_hsm_or_pkcs11` | model-transparency PKCS #11 (RFC 7512) support |
| `predicate_type_matches_oms_v1_0` | OMS §5.1, `malformed-wrong-predicate_fail` |
| `resource_manifest_nonempty` | OMS §5.2.1 `minItems: 1`, `key-simple-empty-resources_fail` |
| `resource_manifest_sorted_by_name` | OMS §6.4, `_assert_resources_sorted` |
| `resource_paths_canonical_posix_relative` | OMS §6.1.2, `_assert_paths_canonical` |
| `hash_algorithm_is_required_sha256` | OMS §7 / `algorithm-registry.md` |
| `hash_algorithm_matches_serialization_hash_type` | OMS §6.3.1, `_assert_algorithm_consistency` |
| `root_digest_recomputes_from_resource_digests` | OMS §6.5.1, `_assert_root_digest` |
| `all_signed_files_present_unmodified` | OMS §8.4 (`tampered`, `missing-file` cases) |
| `no_unsigned_files_in_model_scope` | OMS §8.5, `key-simple-extra-file_fail` |
| `symlinks_disallowed_or_explicitly_permitted` | OMS §6.1.1, `serialization.allow_symlinks` |
| `signing_is_deterministic_across_runs` | OMS `key-simple-deterministic` |
| `weak_hash_algorithm_used_on_weights` | CycloneDX `hash-alg` enum admitting MD5/SHA-1 |
| `served_artifact_hash_matches_registry_hash` | HF Xet `X-Xet-Hash` file ID |
| `weights_format_permits_code_execution` | safetensors `attacks/` (pickle/`.pt`/`.h5`/`.pdparams`) |
| `weights_container_offsets_contiguous_nonoverlapping` | safetensors abuse proposals 3–5 |

### 9.2 Checkpoint lineage

| Factor | Source of the name |
|---|---|
| `base_model_declared` | HF `base_model` |
| `base_model_list_complete_for_merges` | HF `base_model` "can also be a list (for merges)" |
| `trained_on_relationship_declared` | SPDX `trainedOn` |
| `pretrained_on_relationship_declared` | SPDX `pretrainedOn` |
| `finetuned_on_relationship_declared` | SPDX `finetunedOn` |
| `evaluated_on_relationship_declared` | SPDX `evaluatedOn` |
| `tested_on_distinct_from_trained_on` | SPDX `hasDataFile` guidance separating `trainedOn` / `testedOn` |
| `training_workflow_recorded_as_formulation` | CycloneDX `formulation.workflows` |
| `hyperparameters_recorded` | SPDX `ai_hyperparameter` / CycloneDX `modelCard.properties` |
| `training_energy_consumption_recorded` | SPDX `trainingEnergyConsumption` / CycloneDX `energyConsumptions[].activity` |
| `lineage_edges_resolve_to_hashed_artifacts` | SPDX `/Core/Artifact.verifiedUsing` |
| `eval_result_attested_not_self_reported` | HF `verifyToken` |
| `eval_dataset_revision_pinned` | HF `model-index…dataset.revision` |

### 9.3 Prompt versioning

| Factor | Source of the name |
|---|---|
| `prompt_artifact_has_immutable_version_identity` | Langfuse immutable auto-increment `version` |
| `prompt_deployment_label_distinct_from_version` | Langfuse `labels[]` vs `versions[]` |
| `production_label_move_reviewed` | Langfuse `production` default-resolution label |
| `prompt_version_typed_not_freeform_metadata` | Prompty gap — `metadata` is an untyped dict |
| `prompt_artifact_hashed_and_attested` | SPDX `InteractionTemplate` ⊂ `/Core/Artifact` → `verifiedUsing` |
| `prompt_role_declared_inference_vs_training` | SPDX `configures` (runtime) vs `trainedOn` / `finetunedOn` |
| `prompt_dependencies_resolved_and_pinned` | Langfuse `resolve` flag / dependency tags |
| `system_prompt_change_bound_to_model_version` | composition of the above two |

### 9.4 Training-data licence / opt-out compliance

| Factor | Source of the name |
|---|---|
| `dataset_licence_recorded` | DPI `Licenses[]`, Croissant `license`, HF `license` |
| `dataset_licence_identifier_is_spdx` | Croissant spec recommendation to use spdx.org/licenses |
| `dataset_licence_human_verified` | DPI `License Verified By` |
| `dataset_licence_permits_commercial_use` | DPI `license_classes` element 1 (`All` vs `Acad` vs `NC` vs `?`) |
| `dataset_licence_requires_attribution` | DPI `license_classes` element 2 |
| `dataset_licence_requires_share_alike` | DPI `license_classes` element 3 |
| `dataset_licence_class_unknown` | DPI `["?","?","?"]` state |
| `conflicting_licence_claims_on_dataset` | DPI multi-entry `Licenses[]` (Alpaca precedent) |
| `dataset_licence_changed_since_acquisition` | DPI `License Notes` |
| `licence_string_unrecognised_fail_closed` | Common Pile `ValueError` |
| `licence_permissiveness_blue_oak_rated` | Common Pile Gold/Silver/Bronze (ordinal) |
| `dataset_availability_type` | SPDX `DatasetAvailabilityType` (enum: `directDownload`, `query`, `registration`, `clickthrough`, `scrapingScript`) |
| `acquired_by_scraping_around_clickthrough` | SPDX `scrapingScript` + `clickthrough` |
| `training_document_source_recorded` | Dolma mandatory `source` |
| `training_document_acquisition_timestamp_recorded` | Dolma `added` |
| `robots_txt_content_usage_train_ai_respected` | AIPREF `Content-Usage: train-ai=n` (robots.txt rule) |
| `http_content_usage_header_respected` | AIPREF `Content-Usage` HTTP field |
| `tdm_reservation_flag_respected` | TDMRep `tdm-reservation` = 1/0 |
| `tdm_policy_consulted_when_reserved` | TDMRep `tdm-policy` URL |
| `tdmrep_precedence_order_applied_correctly` | TDMRep well-known → header → meta → embedded |
| `cawg_ai_generative_training_permission` | CAWG `cawg.ai_generative_training` (tri-state) |
| `cawg_ai_training_permission` | CAWG `cawg.ai_training` (tri-state) |
| `cawg_data_mining_permission` | CAWG `cawg.data_mining` (tri-state) |
| `cawg_ai_inference_permission` | CAWG `cawg.ai_inference` (tri-state) |
| `asset_permission_is_constrained_not_binary` | CAWG `constrained` value |
| `vendor_crawler_optout_token_respected` | de facto `GPTBot` / `Google-Extended` (**no standard**) |
| `dataset_contains_personal_sensitive_information` | Croissant `rai:personalSensitiveInformation`, SPDX `hasSensitivePersonalInformation` |
| `dataset_governance_owner_named` | CycloneDX `dataGovernance.owners[]` |
| `dataset_governance_steward_named` | CycloneDX `dataGovernance.stewards[]` |
| `dataset_governance_custodian_named` | CycloneDX `dataGovernance.custodians[]` |
| `synthetic_data_generating_model_declared` | DPI `Model Generated` |
| `contamination_checked_per_split` | LM Contamination Index `{train,dev,test}_split` |
| `contamination_verdict` | LM Contamination Index `clean|suspicious|contaminated` (ternary) |
| `contamination_method_matches_data_access` | LLMSanitize open/closed × white/black-box |

### 9.5 Weight-access control

Prefer **SL5 OSCAL control IDs as the provisions**, with these as the factor layer:

| Factor | Source of the name |
|---|---|
| `weight_store_access_control_enforced` | SL5 AC family (7 controls) |
| `weight_access_authentication_enforced` | SL5 IA family (1 control) |
| `weight_store_communications_protected` | SL5 SC family (15 controls) |
| `weight_egress_path_restricted` | SL5 SC family / network stream |
| `weight_integrity_monitored` | SL5 SI family (7 controls) |
| `weight_supply_chain_controls_applied` | SL5 SR family (11 controls), incl. NIST SR-13 |
| `weight_facility_physical_controls_applied` | SL5 PE family (6 controls), ICD 705-derived |
| `personnel_screening_applied_to_weight_access` | SL5 PS family (3 controls) |
| `weight_config_baseline_managed` | SL5 CM family (2 controls) |
| `weight_incident_response_plan_exercised` | SL5 IR family (1 control) |
| `signing_identity_is_workload_not_human` | model-transparency workload identity list |
| `private_sigstore_trust_config_pinned` | model-transparency `--trust-config` |
| `transparency_log_inclusion_proof_checked` | Sigstore Rekor inclusion proof (model-transparency README) |
| `signing_identity_monitored_in_transparency_log` | `sigstore/rekor-monitor` |

---

## 10. Priority build order

1. **Vendor `ossf/model-signing-spec` conformance cases** and adopt its YAML case shape as
   the corpus's canonical serialisation. 86 cases, Apache-2.0, already provision-referenced.
2. **Vendor DPI `license_classes.json` + `custom_license_classes.json`** as the training-data
   licence lattice (145 mappings total), and Common Pile's fail-closed normaliser as its oracle.
3. **Vendor the 3 CC0 SPDX 3.0 AI/dataset documents** as positive MBOM fixtures; generate
   negatives by mutation against the verified field list.
4. **Vendor Croissant's 30 negative validator cases** — the only source with expected
   *reasoning text*, not just verdicts.
5. **Import the SL5 OSCAL profile** and use its control IDs as weight-access provisions.
6. **Adopt SPDX `trainedOn`/`pretrainedOn`/`finetunedOn`/`evaluatedOn`** as the lineage
   predicate vocabulary and CAWG's four `cawg.*` keys as the opt-out vocabulary.
7. **Write the prompt-versioning provisions from scratch**, citing Prompty's untyped
   `metadata.version` and Langfuse's version/label split as the evidence that no standard
   covers it.
