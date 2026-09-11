# Lane 02 — Software Supply Chain Security: reusable open test data & conformance suites

Research date: 2026-09-05. Target: an open compliance test corpus whose cases are
`(case_id, provisions_engaged, boolean_factor_facts, expected_disposition)`, governing software
change in semiconductor supply-chain monitoring software.

**Verification method.** Every licence below was verified by reading the actual `LICENSE`/`COPYING`
file or the explicit licence statement in the repository (shallow `git clone` or raw file fetch),
not inferred from a badge, from SPDX metadata, or from memory. Where a repository has *no* licence
file, that is stated as an unlicensed finding, not guessed. Where a project is *dual*-licensed or
splits code/data/docs, the split is quoted.

Legend: **[VENDOR]** safe to copy into the corpus repo under stated attribution; **[REF]**
reference-only (copyleft, gated, unlicensed, or safety-hazardous — cite and link, do not vendor).

---

## 1. SLSA

### 1.1 SLSA specification — slsa-framework/slsa  **[REF for text, concept-reuse fine]**

- URL: https://github.com/slsa-framework/slsa · https://slsa.dev
- **Verified licence — it is genuinely dual, and neither half is a normal OSS code licence:**
  `LICENSE.md` in the repo root is titled exactly **"Community Specification License 1.0"**. Its
  own preamble states: *"It is not intended for source code."* The README states:
  > "All SLSA specification content contributed following adoption of the Community Specification
  > governance model is provided under the Community Specification License 1.0."
  > "Pre-existing portions of the SLSA specification from contributors who have not subsequently
  > contributed under the Community Specification License 1.0 following its adoption are provided
  > under the Apache License 2.0."

  So: **Community-Spec-1.0 (newer content) + Apache-2.0 (pre-existing content)**, with no
  file-level marker telling you which paragraph is which. Community-Spec-1.0 §1.2 requires
  attribution *including material name, version number and source* in any derivative work, but
  explicitly exempts *implementations* of the specification from the attribution requirement.
- **Consequence for the corpus:** quoting SLSA requirement text verbatim into corpus case files
  drags in Community-Spec-1.0 attribution obligations. **Do not paste requirement prose.** Cite by
  requirement heading + spec version and restate the obligation in your own words. Restating a
  requirement as a factor predicate counts as implementation, which is attribution-exempt.
- **Provision citability — a real defect for our purposes.** Verified against
  https://slsa.dev/spec/v1.1/requirements: SLSA build-track requirements are **not individually
  numbered**. There is no "L2.1" or "REQ-003". Requirements are cited by heading plus level:
  Producer → *Choose an appropriate build platform*, *Follow a consistent build process*,
  *Distribute provenance*; Build platform → *Provenance generation* (sub-levels **Exists**,
  **Authentic**, **Unforgeable**) and *Isolation strength* (sub-levels **Hosted**, **Isolated**).
  The level tables use checkmarks, not provision IDs.
  → The corpus must **mint its own stable provision IDs** and carry a mapping table
  `corpus_provision_id → (slsa_spec_version, track, requirement_heading, level)`. Do not pretend
  SLSA gave you citable identifiers.

### 1.2 SLSA **Source Track** — the org-level track  **[REF]**

- URL: https://slsa.dev/spec/v1.2/source-requirements
- Verified: the Source Track exists and is explicitly written against a *repository and its owning
  organisation*, not an artifact. Levels: **L1 Version controlled**, **L2 History & Provenance**,
  **L3 Continuous technical controls**, **L4 Two-party review**. It carries a section literally
  headed *Organization Requirements* (Choose an appropriate Source Control System; Configure the
  SCS to control access and enforce history; Safe Expunging Process; Continuous technical
  controls) alongside *Source Control System Requirements* (Repositories are uniquely
  identifiable; Revisions are immutable and uniquely identifiable; Human readable changes; Source
  Verification Summary Attestations; History; Continuity; Identity Management; Source Provenance;
  Protected Named References; Two-party review). Spec text is under the same dual licence as §1.1.
- **Why this matters here:** this is the closest published analogue to a corpus that scores a
  *pipeline* rather than an artifact. Its L3 "continuous technical controls" and L4 "two-party
  review" map almost directly onto change-governance provisions for fab monitoring software.

### 1.3 slsa-framework/slsa-verifier — **the single best fixture set in this lane**  **[VENDOR]**

- URL: https://github.com/slsa-framework/slsa-verifier
- **Verified licence:** root `LICENSE` = **Apache License 2.0** (file opens
  `Apache License / Version 2.0, January 2004`).
- **Contents and volume (measured on a fresh clone):**
  | path | files | what |
  |---|---|---|
  | `cli/slsa-verifier/testdata/` | **660** files, **297 MB** | real signed release artifacts + their `*.intoto.jsonl` DSSE provenance, across 29 top-level fixture families |
  | `verifiers/internal/gcb/testdata/` | 53 | Google Cloud Build provenance, valid and systematically corrupted |
  | `verifiers/internal/gha/testdata/` | 21 | GitHub Actions certs / Rekor entries |
  | `verifiers/internal/gcb/slsaprovenance/v0.1|v1.0/testdata/` | 7 | per-version predicate parsing |
- Fixture families under `cli/slsa-verifier/testdata/`: `gha_go`, `gha_generic`, `gha_delegator`,
  `gha_maven`, `gha_gradle`, `gha_container-based`, `gha_generic_container`, `gcb_container`,
  `npm`, `vsa`, `bcr`, `workflow-inputs`, `annotated-tag`, plus deliberately-adversarial single
  artifacts: `binary-linux-amd64-untrusted-builder`, `binary-linux-amd64-expired-cert`,
  `binary-linux-amd64-no-tlog-upload`, `binary-linux-amd64-multi-subject-{first,second}`,
  `binary-linux-amd64-sharded`, `binary-linux-amd64-e2e-builder-repo`. Each builder family is
  further versioned (`v0.0.2`, `v1.0.0` … `v1.10.0`) so you get the *same* logical case across
  many generator versions.
- **Tampered provenance is real and named**, e.g. under `gcb_container/v0.2|v0.3/`:
  `gcloud-container-mismatch-payload-digest.json`,
  `gcloud-container-mismatch-payload-builderid.json`,
  `gcloud-container-mismatch-summary-digest.json`,
  `gcloud-container-mismatch-metadata-urisha256.json`,
  `gcloud-container-mismatch-text-steps.json`, `gcloud-container-invalid-keyid.json`,
  `gcloud-container-invalid-signature-encoding.json`,
  `gcloud-container-multiple-invalid-signatures.json`; and under `npm/gha/`:
  `provenance-npm-test-cli-v1-prega-invalidsigprov.tgz`,
  `gundam-visor-cli-v1-tag-invalidsigprov.tgz`.
- **Format — this is the important part.** `cli/slsa-verifier/main_regression_test.go` (2 157
  lines, ~184 named cases, ~128 of them expecting a specific error) is a Go table test whose row
  shape is *isomorphic to our case tuple*:
  ```go
  {
      name:      "wrong source prepend A",              // case_id
      artifacts: []string{"binary-linux-amd64-..."},    // fixture
      source:    "github.com/laurentsimon/...",         // input fact
      ptag:      pString("v13.0.29"),                   // input fact
      err:       serrors.ErrorMismatchSource,           // expected disposition
  }
  ```
  A row with no `err` field is an expected-PASS case. Nothing else needs inventing.
- **The error taxonomy is a ready-made violation vocabulary** (48 sentinel errors extracted from
  `verifiers/` + `cli/`): `ErrorMismatchBuilderID`, `ErrorUntrustedReusableWorkflow`,
  `ErrorMismatchSource`, `ErrorMismatchBranch`, `ErrorMismatchTag`, `ErrorMismatchVersionedTag`,
  `ErrorMismatchWorkflowInputs`, `ErrorMismatchHash`, `ErrorMismatchCertificate`,
  `ErrorMismatchResourceURI`, `ErrorMismatchPackageName`, `ErrorMismatchPackageVersion`,
  `ErrorMismatchVerifiedLevels`, `ErrorMismatchVerifierID`, `ErrorMismatchIntoto`,
  `ErrorInvalidBuilderID`, `ErrorInvalidBuildType`, `ErrorInvalidCertificate`,
  `ErrorInvalidOIDCIssuer`, `ErrorInvalidRekorEntry`, `ErrorNoValidRekorEntries`,
  `ErrorInvalidSLSALevel`, `ErrorInvalidDssePayload`, `ErrorInvalidSignature`,
  `ErrorNoValidSignature`, `ErrorInvalidSubject`, `ErrorMissingSubjectDigest`,
  `ErrorMutableImage`, `ErrorNonVerifiableClaim`, `ErrorEmptyRequiredField`, `ErrorInvalidRef`, …
- **Reuse path:** (a) vendor a *selected subset* of fixtures — the whole 297 MB is far too heavy,
  take one builder version per family plus the full `gcb_container` tamper set (~5 MB); (b) reuse
  the error taxonomy directly as `violates(c,p)` labels; (c) reuse the table-test row shape as the
  corpus's serialised case schema. Attribution: Apache-2.0 NOTICE + per-file provenance.

### 1.4 slsa-framework/slsa-github-generator  **[VENDOR]**

- URL: https://github.com/slsa-framework/slsa-github-generator
- **Verified licence:** root `LICENSE` = **Apache License 2.0**.
- Test fixtures (measured): `internal/builders/go/pkg/testdata` 16 files,
  `internal/builders/go/testdata` 13, `internal/builders/docker/testdata` 4, plus four
  action-level `testdata` dirs (1–2 files each). 34 workflows in `.github/workflows`, of which the
  `pre-submit.e2e.*` / `e2e.*.schedule.yml` set are live end-to-end conformance runs.
- The go-builder fixtures are **valid/invalid-paired build configs** — exactly the shape of a
  change-governance case: `releaser-valid-main.yml`, `releaser-valid-dir.yml`,
  `releaser-valid-envs-no-value.yml`, `releaser-valid-envs-multiple-equal-signs.yml`,
  `releaser-valid-empty-main.yml`, `releaser-valid-no-main.yml` vs
  `release-invalid-dir.yml`, `releaser-invalid-envs.yml`, `releaser-invalid-main.yml`,
  `releaser-invalid-version.yml`, `releaser-noversion.yml`; plus ldflags variants
  (`two-ldflags-emptyenv.yml`, `two-ldflags-noflags.yml`, `emptyldflags.yml`) and GitHub event
  payloads (`push_payload_tag.json`, `push_payload_notag.json`, `workflow_dispatch_payload.json`).
- **Reuse:** small enough to vendor whole. Use as fixtures for "build config declares a
  disallowed/unsanitised parameter" cases. The event payloads are the cleanest open example of
  *trigger-type* facts (`push` w/ tag vs `workflow_dispatch`), which our corpus needs to
  distinguish reviewed from unreviewed change.

---

## 2. in-toto

### 2.1 in-toto/attestation (framework, predicate types)  **[VENDOR]**

- URL: https://github.com/in-toto/attestation
- **Verified licence:** root `LICENSE` = **Apache License 2.0** ("Copyright 2021 in-toto
  Developers / Licensed under the Apache License, Version 2.0").
- Contents: `spec/v1/` (Statement, ResourceDescriptor, bundle), `spec/v0.1.0/`, `spec/predicates/`
  with **16 vetted predicate docs** — `provenance.md` (SLSA), `vsa.md`, `svr.md`, `test-result.md`,
  `scai.md`, `link.md`, `reference.md`, `release.md`, `runtime-trace.md`, `spdx2.md`, `spdx3.md`,
  `cyclonedx.md`, `vuln.md`, `vulns_02.md`, plus a `template/`. Language bindings in `go/`,
  `python/`, `rust/`, `java/`, protobufs in `protos/`. Go unit-test vectors live inline in
  `go/v1/statement_test.go`, `go/v1/resource_descriptor_test.go`,
  `go/predicates/provenance/v1/provenance_test.go`; `examples/go/main.go` is a worked example.
  There is **no separate `testdata/` corpus** — this is a spec repo, not a fixture repo.
- **Two predicates are the corpus's natural output format, not just input:**
  - **SVR — Simple Verification Result**, `https://in-toto.io/attestation/svr/v0.2`. Verified
    schema: `predicate.verifier.{id, policies[]}`, `predicate.timeCreated`,
    `predicate.properties[]` (list of verified property strings). Purpose text: *"communicates
    that an artifact has been evaluated against one or more policies, and records the properties
    that were verified, at the point-in-time of the evaluation."* This is precisely
    `(subject, provisions_engaged, factor_facts_that_held, timestamp, oracle_identity)`.
  - **VSA — Verification Summary Attestation**, carrying `verificationResult` and
    `verifiedLevels`. slsa-verifier has a whole `testdata/vsa/` tree and a
    `ErrorMismatchVerifiedLevels` sentinel, so there is a working oracle for VSA disposition.
- **Reuse path:** emit each corpus case's *expected disposition* as an SVR-shaped record.
  `properties[]` = the factor names that must hold; `verifier.policies[]` = provisions engaged.
  This gives the corpus a wire format that existing supply-chain tooling can already consume,
  which is worth far more than a bespoke JSON shape.

### 2.2 in-toto/witness  **[VENDOR]**

- URL: https://github.com/in-toto/witness
- **Verified licence:** root `LICENSE` = **Apache License 2.0**; source headers read
  "Copyright 2022 The Witness Contributors / Licensed under the Apache License, Version 2.0".
- Test material in `test/` (~24 files): `policy.json`, `policy-hello-signed.json`,
  `fulcio-policy-presigned.json`, `cdx-sbom-policy.json`, `spdx-sbom-policy.json`,
  `cdx-att.json`, `spdx-att.json`, `sbom.cdx.json`, `sbom.spdx.json`, key material
  (`testkey.pem`, `testkey2.pem`, `testpub.pem`, `testpub2.pem`, `failkey.pem` — *a deliberate
  wrong-key fixture*), `freetsa.pem`, and declarative run configs `test.yaml`, `test-mac.yaml`.
- `test.yaml` shows the full lifecycle declaratively: `run:` (signer key, `step: build`,
  `attestations: [environment, git]`) → `sign:` → `verify:` (attestations list, policy,
  publickey, artifactfile). Witness policies bind *steps* to *required attestors* and *authorised
  functionaries* — i.e. they constrain the pipeline, not the artifact.
- **Reuse:** witness policy JSON is the best small open example of a machine-checkable
  *change-process* policy (which steps must exist, who may sign them). `failkey.pem` gives a
  free negative case for `signer_identity_in_authorised_functionary_set`.

### 2.3 guacsec/guac  **[VENDOR]**

- URL: https://github.com/guacsec/guac
- **Verified licence:** root `LICENSE` = **Apache License 2.0**.
- `internal/testing/testdata/` = **73 files**, of which `exampledata/` is a broad multi-format
  fixture pile: `alpine-spdx.json`, `alpine-small-spdx.json`, `alpine-cyclonedx.json`,
  `busybox-cyclonedx.json` (+ `.bz2`, `.zst` compressed variants), `big-mongo-cyclonedx.json`,
  `distroless-cyclonedx.json`, `distroless-cyclonedx-invalid-version.json`, `cyclonedx-1.7.json`,
  `cyclonedx-components-flat.json` / `-nested.json`, `cyclonedx-no-top-level.json`,
  `go-spdx-multi-arch_{1,2,3}.json`, VEX set (`cyclonedx-vex.xml`, `cyclonedx-vex-affected.json`,
  `cyclonedx-vex-false-positive.json`, `cyclonedx-vex-no-analysis.json`,
  `cyclonedx-unaffected-vex.json`, `cyclonedx-vex-resolved-with-pedigree.json`), certification
  records (`certify-vuln.json`, `certify-novuln.json`, `-v02` variants), review records
  (`crev-review.json`, `github-review.json`), EOL records, `ingest_predicates.json`, and
  **negative fixtures** `invalid-cyclonedx.json`, `invalid-cyclonedx.xml`,
  `invalid-scorecard.json`, plus `testdata.go`/`models.go` giving the expected parsed graph.
- **Reuse:** `invalid-*.json` + their expected-parse assertions are a free
  `document_parses_against_declared_schema` oracle across both SBOM formats; the multi-arch and
  flat-vs-nested pairs are the best open fixtures for "same software, differently-shaped SBOM",
  which is the false-positive trap any drift detector must survive.

---

## 3. Sigstore

### 3.1 sigstore/sigstore-conformance — **the model to copy for corpus mechanics**  **[VENDOR, with a licence caveat]**

- URL: https://github.com/sigstore/sigstore-conformance
- **Verified licence — read this carefully:** there is **no `LICENSE` file in the repository
  root** (confirmed by `ls -a` on a fresh clone; root contains `.github`, `.gitignore`,
  `.python-version`, `Makefile`, `README.md`, `RELEASE.md`, `action.py`, `action.yml`,
  requirements files, `docs`, `selftest-client`, `setup`, `test`, `tools`, `pyproject.toml`, and
  `mypy.ini` — no `LICENSE`, no `COPYING`). `pyproject.toml` carries **no** `license` field and
  no classifiers. The **only** licence statement anywhere is `README.md` line 141:
  > "`sigstore-conformance` is licensed under the Apache 2.0 License."

  That is a bare prose assertion with no licence text and no copyright line. Treat it as
  **Apache-2.0 asserted-but-not-shipped**. Before vendoring, open an issue asking them to add the
  `LICENSE` file, or record the README assertion + commit SHA in your provenance notes. Do not
  record this as a clean Apache-2.0 the way you would for slsa-verifier.
- **Contents and volume:** `test/assets/bundle-verify/` holds **72 case directories** —
  **49 expect failure, 23 expect success** (counted). Each directory contains
  `bundle.sigstore.json`, usually a `trusted_root.json`, sometimes an `artifact`, and a
  one-paragraph plain-text `README` that *states the case rationale*.
- **Case format — the disposition is in the directory name.** Verified in `test/test_bundle.py`:
  ```python
  def test_verify(client, bundle_verify_dir, verify_bundle):
      path = Path(bundle_verify_dir)
      materials = BundleMaterials.from_dir(path)
      if path.name.endswith("fail"):
          with client.raises():
              verify_bundle(materials)
      else:
          verify_bundle(materials)
  ```
  So `must_fail` ≡ directory suffix `_fail`; `must_pass` ≡ any other suffix. Cases are
  auto-discovered by `pytest_generate_tests` in `conftest.py` — no registry file to keep in sync.
- **Named negative cases** (a partial list, each a distinct provision violation):
  `invalid-ct-key_fail`, `dsse-mismatch-sig_fail`, `rekor2-dsse-mismatch-sig_fail`,
  `rekor2-timestamp-payload-mismatch_fail`, `rekor2-timestamp-with-incorrect-time_fail`,
  `rekor2-timestamp-outside-trust-root-tsa-validity_fail`,
  `intoto-tsa-timestamp-outside-cert-validity_fail`,
  `trust-root-tlog-missing-validity-start_fail`, `bundle-unknown-version_fail`,
  `managed-key-no-key_fail`. Positives: `happy-path-v0.2`, `rekor2-dsse-happy-path`,
  `bundle-with-sct-with-extensions`, `rekor2-timestamp-without-embedded-cert`.
  The `README` files are unusually good — e.g. `dsse-mismatch-sig_fail`:
  *"DSSE signature does not match. This was created by repeating a signing operation over the same
  payload with the same ECDSA key resulting in two valid, but different signatures."* That is a
  written *factor rationale*, which is exactly what a legal-style corpus needs and almost nobody
  else publishes.
- **`xfail` mechanism — directly reusable for "provision not yet in force".** Verified in
  `README.md` §"Configuring `xfail` for optional tests", `action.yml` input `xfail`
  (→ env `GHA_SIGSTORE_CONFORMANCE_XFAIL`), and `test/conftest.py`:
  ```python
  @pytest.fixture(autouse=True)
  def conformance_xfail(request):
      if any(fnmatch(request.node.name, p) for p in _XFAIL_LIST):
          request.node.add_marker(pytest.mark.xfail(reason="skipped by suite runner", strict=True))
  ```
  `xfail` is a **whitespace-separated list of shell-style globs** over test node names, matched
  with `fnmatch`, and marked **`strict=True`** — meaning an xfail case that unexpectedly *passes*
  is itself a failure. The live example in `.github/workflows/conformance.yml`:
  `"test_verify*-intoto-with-custom-trust-root] test_verify*managed-key-happy-path] ..."`.
  `.github/scripts/generate_client_report.py` then renders per-implementation pass/fail/xfail
  tables.
- **Reuse path — the highest-leverage item in this lane after slsa-verifier.** Copy three
  mechanisms wholesale: (1) *disposition-in-the-path* naming so cases are self-describing and
  auto-discovered; (2) per-case `README` rationale as a first-class artifact; (3) **strict glob
  `xfail`** so an implementation can declare which provisions it does not yet claim to satisfy
  without deleting cases — this is exactly how a fab-software vendor would declare
  "provision P-14 not yet applicable to our pipeline", and strictness stops that declaration
  rotting silently.

### 3.2 sigstore/cosign  **[VENDOR]**

- URL: https://github.com/sigstore/cosign — **verified licence:** root `LICENSE` = **Apache 2.0**.
- 47 test-path files. Most relevant: **`pkg/policy/testdata/valid/{custom,vuln}` vs
  `pkg/policy/testdata/malformed/{custom,vuln}`** — CUE/Rego policy fixtures with the disposition
  again encoded in the path. Also `pkg/cosign/testdata/` (`oci-attestation.sigstore.json`,
  `trusted_root_pgi.json`, `letsencrypt-testflume-2021`, `garbage-there-are-limits` — a
  deliberate junk-input fixture), `test/testdata/attestations/vuln-predicate.json`,
  `test/testdata/bom-go-mod.cyclonedx.json`, `test/testdata/bom-go-mod.spdx`.
- **Reuse:** the `valid/` vs `malformed/` policy pairs are a free oracle for
  `policy_document_is_well_formed` — a provision our corpus needs (a change that ships a
  syntactically broken gate policy is a violation even if nothing else is wrong).

### 3.3 sigstore/rekor  **[VENDOR]**

- URL: https://github.com/sigstore/rekor — **verified licence:** root `LICENSE` = **Apache 2.0**.
- 128 test-path files. Transparency-log entry type vectors:
  `pkg/generated/models/testdata/{dsse,hashedrekord,intoto}.json`; signature-scheme fixtures with
  matched good/bogus pairs, e.g. `pkg/pki/pgp/testdata/{armored_private.pgp, binary_private.pgp,
  bogus_armored.pgp, bogus_binary.pgp}`, `pkg/pki/minisign/testdata/{hello_world.txt,
  hello_world.txt.minisig, hello_world.txt.signify, minisign.pub, signify.pub, ...}`.
- **Reuse:** `bogus_*` vs valid pairs give a ready oracle for
  `signature_verifies_under_declared_key`; the entry-type vectors are the canonical shape for
  `transparency_log_entry_present_and_consistent`.

### 3.4 sigstore/fulcio  **[VENDOR]** — **verified licence:** root `LICENSE` = **Apache 2.0**.
Relevant chiefly for OIDC-issuer → certificate-extension mapping; the slsa-verifier
`ErrorInvalidOIDCIssuer` / `ErrorMismatchCertificate` cases already exercise it end to end, so
prefer slsa-verifier's fixtures over building fresh ones from fulcio.

### 3.5 sigstore/model-transparency — **agent/model code provenance**  **[VENDOR]**
- URL: https://github.com/sigstore/model-transparency — **verified licence:** `LICENSE` =
  **Apache 2.0**. Signs and verifies ML model artifacts with Sigstore. This is the nearest open
  analogue for "agent code provenance" — an artifact that is not a build output in the classical
  sense but must still carry a verifiable producer identity. Useful as a *pattern* for corpus
  provisions about AI-generated or agent-generated changes; its fixture set is small.

---

## 4. SBOM: formats, examples, conformance

### 4.1 SPDX specification  **[REF]**

- URL: https://github.com/spdx/spdx-spec
- **Verified licence (dual, and different from SLSA's dual):** `v3.0.1/LICENSE` opens:
  > "The SPDX Specification is provided under the Community Specification License 1.0
  > (Community-Spec-1.0), a copy of which is included below."
  > "Pre-existing portions of the SPDX Specification from copyright holders who have not
  > subsequently contributed under the Community Specification License 1.0 are provided under
  > Creative Commons Attribution 3.0 Unported (CC-BY-3.0), a copy of which is included below."

  So **Community-Spec-1.0 + CC-BY-3.0** — note CC-BY-**3.0**, not 4.0, and not Apache-2.0 (that
  is SLSA's other half). Same consequence as §1.1: cite, restate, do not paste.

### 4.2 spdx/spdx-examples — **the GPL trap, and the CC0 escape hatch**  **[MIXED: docs VENDOR, code REF]**

- URL: https://github.com/spdx/spdx-examples
- **Verified licence — three-way split, quoted from `README.md` §Licenses:**
  > "Unless otherwise specified, source code in this repository is licensed under the GNU General
  > Public License, Version 3 or later (GPL-3.0-or-later). A copy is included in the COPYING file."
  > "Documentation in this repository is licensed under the Creative Commons Attribution 4.0
  > International license (CC-BY-4.0)…"
  > "**SPDX documents in this repository are provided under CC0 1.0 Universal (CC0-1.0)**…"

  `COPYING` in the root is confirmed to be **GNU GPL Version 3**. Per-file
  `SPDX-License-Identifier` tags actually present in the tree, counted: **Apache-2.0 ×16,
  GPL-3.0-or-later ×13, CC0-1.0 ×7, CC-BY-4.0 ×4, BSD-3-Clause ×2**.
- **The operative finding:** the **SBOM documents themselves are CC0-1.0 — public domain, safe to
  vendor with no attribution burden.** The `content/` subtrees (`hello.c`, `hello.go`, `main.rs`,
  `Makefile`s, the `ai/example02` Python scripts) are the GPL-3.0-or-later part. If you vendor
  whole example directories you pull GPL source into a permissive corpus. **Vendor only the
  `spdx2.2/`, `spdx2.3/`, `spdx3.0/` document files; leave `content/` behind and reference it.**
- Volume: **58** SPDX document files across `software/example1…11`, `ai/example01–02`,
  `dataset/example01`, `hardware/`, `conformance/example1`, `semantics/`, plus
  `presentations/`. Both 2.2/2.3 and 3.0 serialisations of several of the same examples — i.e.
  free *format-migration* pairs.

### 4.3 CycloneDX/sbom-examples  **[VENDOR — cleanest licence in the lane]**

- URL: https://github.com/CycloneDX/sbom-examples
- **Verified licence:** root `LICENSE` opens `Creative Commons Legal Code / CC0 1.0 Universal` →
  **CC0-1.0**. Public domain dedication; no attribution obligation at all.
- Volume: **127 files**. Organised by BOM type: `SBOM`, `VEX`, `VDR`, `SaaSBOM`, `OBOM`,
  `HBOM` (PCIe-SATA adapter board — genuinely hardware, relevant to a fab context), `CBOM`
  (crypto: Algorithm / Protocol / Key / Certificate / Example-With-Dependencies), `MBOM`.
- **`VEX/Use-Cases/Case-1 … Case-13` and `VEX/CISA-Use-Cases/Case-1 … Case-9`** — each is a
  directory containing `README.md` + `vex.json`. That is a **numbered, rationale-carrying case
  corpus** already, published by the format owner, under CC0.
- **Reuse:** vendor entire. Use the VEX Use-Cases numbering as a precedent for corpus case IDs,
  and the HBOM/CBOM examples as the semiconductor-adjacent fixtures the corpus otherwise lacks.

### 4.4 CycloneDX/specification — schema test suite  **[VENDOR]**

- URL: https://github.com/CycloneDX/specification — **verified licence:** root `LICENSE` =
  **Apache License 2.0**.
- `tools/src/test/resources/` = **975 files** across spec versions 1.0–1.7 plus `ext/`.
  Disposition is in the filename prefix. Measured per version:
  | version | files | `invalid-*` | `valid-*` |
  |---|---|---|---|
  | 1.4 | 134 | 46 | 88 |
  | 1.5 | 155 | 46 | 109 |
  | 1.6 | 190 | 54 | 136 |
  | 1.7 | 246 | 60 | 184 |
- Every case exists in **both JSON and XML** (`invalid-hash-alg-1.6.json` +
  `invalid-hash-alg-1.6.xml`), so you get serialisation-independence for free. Negative cases are
  named by the violated constraint: `invalid-bomformat`, `invalid-component-ref`,
  `invalid-component-type`, `invalid-component-swid`, `invalid-dependency`,
  `invalid-empty-component`, `invalid-hash-{alg,md5,sha1,sha256,sha512}`, `invalid-issue-type`,
  `invalid-license-choice`, `invalid-license-declared-concluded-mix`, `invalid-license-encoding`,
  `invalid-license-id`, …
- **Reuse:** the single largest ready-made `(fixture, expected boolean disposition)` set in this
  lane, at ~975 cases, Apache-2.0, and small on disk. Vendor 1.6 + 1.7 at minimum. It is the
  natural oracle for `sbom_conforms_to_declared_schema_version`.

### 4.5 CycloneDX/sbom-utility — **the closest thing to an SBOM drift corpus**  **[VENDOR]**

- URL: https://github.com/CycloneDX/sbom-utility — **verified licence:** root `LICENSE` =
  **Apache License 2.0** (also `NOTICE.txt`, `CREDITS.md`).
- `test/` = **211 files** across `config`, `custom`, `cyclonedx`, **`diff`**, `hash`, `normalize`,
  `patch`, `policy`, `spdx`, `stats`, `trim`, `validation`, `vex`.
- **`test/diff/` is a genuine matched-pair set** — the only openly-licensed one I found that is
  purpose-built for BOM comparison:
  `cdx-1-4-mature-example-1-delta.json`, `…-delta2.json`,
  `cdx-1-4-nested-array-order-change-{base,delta}.json`,
  `json-array-order-change-{base,delta}.json`,
  `json-array-order-2-changes-{base,delta}.json`,
  `json-array-order-change-with-add-{base,delta}.json`,
  `json-array-order-change-with-delete-{base,delta}.json`,
  `json-array-order-change-with-add-and-delete-{base,delta}.json`,
  plus `panic/` and `vulnerability/` subdirs.
  Crucially, several pairs are **semantically null diffs** (array order changed, content
  identical) — the false-positive cases a drift oracle must *not* flag.
- **`test/custom/` is organisation-level conformance**, not artifact-level:
  `config-cdx-best-practices-profile.json`, `cdx-1-6-test-bom-best-practices.json`,
  `cdx-1-6-test-bom-metadata.json`, `config-cdx-bom-properties-not-unique.json`,
  `cdx-1-6-test-metedata-properties-disclaimer.json` / `-disclaimer-missing.json` /
  `-disclaimer-mismatch.json`, `-classification-multiple.json`. These encode "does this BOM carry
  the *organisation's* required metadata properties", which is the corpus's actual question.
- **`sbom-validation-tests.md` is a published case register** with columns
  `| Test name | Description | Test input file | Expected results | Notes |` — e.g.
  `TestValidateSyntaxErrorCdx13Test1 | Missing closing } bracket on metadata property |
  "invalid character '{' after object key" | test/cyclonedx/1.3/cdx-1-3-syntax-err-1.json`.
  A worked precedent for a human-readable corpus index derived from machine cases.
- **Reuse:** vendor `test/diff/` and `test/custom/` outright; adopt `sbom-validation-tests.md`'s
  table format as the corpus's human-facing register.

### 4.6 spdx/ntia-conformance-checker — **the best factor-ablation fixture set found**  **[VENDOR]**

- URL: https://github.com/spdx/ntia-conformance-checker
- **Verified licence:** root `LICENSE` = **Apache License 2.0**; `pyproject.toml` line 24:
  `license = "Apache-2.0"`. (Two independent statements agreeing — the cleanest verification in
  this document.)
- `tests/` = **175 files**. `tests/data/` is organised as **one directory per violated NTIA
  minimum element**, which is exactly one-provision-per-case ablation:
  | directory | files | provision ablated |
  |---|---|---|
  | `no_elements_missing/` | 5 | *(control: expect PASS)* |
  | `missing_author_name/` | 5 | SBOM author |
  | `missing_timestamp/` | 5 | SBOM timestamp |
  | `missing_supplier_name/` | 5 | component supplier |
  | `missing_component_name/` | 4 | component name |
  | `missing_component_version/` | 5 | component version |
  | `missing_unique_identifiers/` | 5 | component unique ID |
  | `missing_dependency_relationships/` | 5 | dependency relationships |
  | `missing_concluded_license/` | 5 | concluded licence (FSCT) |
  | `graph_connectivity/` | 4 | dependency-graph reachability |
  | `bsi/` | 8 | German BSI TR-03183 profile |
  | `spdx3/` | 8 | SPDX 3.0 documents |
  | `SPDXSBOMExampleTests/` | 11 | upstream examples |
  | `real_world_sboms/` | 15 | field-collected SBOMs |
  | `other_tests/` | 3 | misc |
- **It is an oracle, not just fixtures.** The JSON report emits `isNtiaConformant`, `isConformant`,
  `complianceStandard`, `conformanceMessages`, `nonconformantComponents`, `parsingError`,
  plus per-element booleans: `authorNameProvided`, `dependencyRelationshipsProvided`,
  `componentNames`, `componentVersions`, `componentSuppliers`, `componentIdentifiers`,
  `componentConcludedLicenses`, `componentCopyrightTexts`, `allProvided`, and a
  `graphValidation` block (`floatingComponents`, `floatingComponentCount`, `hasUnknownPointers`).
  Checker modules present: `ntia_checker.py`, `ntia2026.py`-era CISA update, `bsi_checker.py`,
  `fsct_checker.py`, `graph_utils.py`.
- **Reuse:** vendor `tests/data/` whole (it is small) and use the checker as a `violates(c,p)`
  oracle for every SBOM-completeness provision. The one-directory-per-missing-element layout is
  the single best structural precedent for the corpus.

### 4.7 interlynk-io/sbomqs — **the best ready-made FACTOR VOCABULARY**  **[VENDOR]**

- URL: https://github.com/interlynk-io/sbomqs — **verified licence:** root `LICENSE` =
  **Apache License 2.0** (per-file headers "Copyright 2025 Interlynk.io / Licensed under the
  Apache License, Version 2.0").
- `pkg/scorer/criteria.go` declares a flat `[]check` where each row is
  `{Category, Key (yaml:"feature"), Ignore, Descr, evaluate func}` — i.e. **a named boolean/scored
  predicate with a stable snake_case key and a category**. Categories: `NTIA-minimum-elements`,
  `bsi-v1.1`, `bsi-v2.0`, `Semantic`, `Quality`, `Sharing`, `Structural`. ~60 rows; keys include
  `comp_with_name`, `comp_with_version`, `comp_with_uniq_ids`, `comp_with_supplier`,
  `comp_with_licenses`, `comp_with_checksums_sha256`, `comp_with_source_code_uri`,
  `comp_with_source_code_hash`, `comp_with_executable_uri`, `comp_with_executable_hash`,
  `comp_with_dependencies`, `comp_with_associated_license`, `comp_with_concluded_license`,
  `comp_with_declared_license`, `comp_valid_licenses`, `comp_with_deprecated_licenses`,
  `comp_with_restrictive_licenses`, `comp_with_primary_purpose`,
  `comp_with_any_vuln_lookup_id`, `comp_with_multi_vuln_lookup_id`,
  `sbom_creation_timestamp`, `sbom_authors`, `sbom_dependencies`, `sbom_with_uri`,
  `sbom_with_bomlinks`, `sbom_with_vuln`, **`sbom_with_signature`**, `sbom_build_process`,
  `sbom_required_fields`, `sbom_with_creator_and_version`, `sbom_with_primary_component`,
  `sbom_sharable`, `spec_with_version_compliant`, `sbom_spec`, `sbom_spec_version`,
  `sbom_file_format`, `sbom_parsable`.
- `pkg/compliance/` implements **named external standards as separate scorers**: `ntia.go`,
  `ntia2026.go`, `bsiV11.go`, `bsiV20.go`, `bsiV21.go`, `fsct/`, `oct.go` (OpenChain Telco), each
  with its own `_report.go` and `_score.go`. This is the pattern for "one corpus, several
  regulatory profiles" — which a semiconductor corpus will need (customer contract vs export
  regime vs internal policy).
- **`testdata/policy/` — a 37-file YAML policy DSL that is structurally our case tuple.** Verified
  shape:
  ```yaml
  policy:
    - name: sbom_provenance_info          # provision id
      description: |                      # rationale
        SBOM must have creation timestamp and author information.
      type: required                      # required | whitelist | blacklist
      rules:
        - field: sbom_timestamp           # factor
        - field: sbom_author              # factor
      action: warn                        # pass | warn | fail  → disposition
  ```
  Profiles present: `metadata-provenance.yaml`, `metadata-required.yaml`,
  `metadata-identifiers.yaml`, `enterprise-approved-suppliers.yaml` (a `type: whitelist` over
  `field: supplier` with an explicit approved-vendor list — *exactly* a supply-chain
  qualified-supplier provision), `enterprise-complete-sbom.yaml`,
  `industry-finance-compliance.yaml`, `advanced-comprehensive.yaml`, `community-health.yaml`,
  `license-allowlist.yaml`, `license-block-copyleft.yaml`, `license-block-proprietary.yaml`,
  `license-dual-check.yaml`, `open-source-distribution.yaml`, and per-field
  `policy-comp-{checksum,cpe,copyright,declared-license,concluded-license,downloadlocation}-required.yaml`.
- Other testdata: `bsi/` 173 files, `fixtures/` 74, `sboms/` 24, `validation/` 12,
  `signature-verification/` 9. Root `samples/`: `photon.spdx.json`, `sbom_cdx.json`,
  `sbom.cdx.signed.json`.
- **Reuse:** adopt the `criteria.go` key vocabulary verbatim as corpus factor names for everything
  SBOM-shaped (it is already snake_case, already stable, already documented, already
  Apache-2.0). Adopt the `testdata/policy` YAML as the corpus's provision-definition format —
  `name / description / type / rules[].field / action` needs almost no adaptation.

### 4.8 eBay/sbom-scorecard  **[VENDOR]**

- URL: https://github.com/eBay/sbom-scorecard — **verified licence:** root `LICENSE` =
  **Apache License 2.0**.
- Rubric verified in `pkg/scorecard/`: five weighted dimensions —
  `Compliance` (`IsSpecCompliant`, weight `validPoints`), `PackageIdentification`,
  `PackageVersions`, `PackageLicenses` (each `packageSectionWeight`), `CreationInfo`
  (`generationPoints`) — summed to a percentage via `ReportResult`/`ScoreValue`.
- **Reuse:** a much coarser rubric than sbomqs. Use it as a *second, independent* oracle to
  cross-check corpus grading; agreement between two independently-implemented scorers is decent
  evidence a factor is objectively checkable rather than tool-specific.

### 4.9 protobom/protobom, CycloneDX/cyclonedx-cli  **[VENDOR]**
Both verified **Apache-2.0** (root `LICENSE`). protobom is the neutral in-memory SBOM model
(useful for normalising SPDX↔CycloneDX before diffing); cyclonedx-cli ships a `diff` subcommand.
Neither publishes a drift *corpus* — they are the machinery, not the data.

---

## 5. SBOM DRIFT — direct answer to the question asked

**Is there an open corpus of matched (approved SBOM, drifted SBOM) pairs?** **No — not as such.**
I found no published dataset framed as approved-vs-drifted SBOM pairs with labelled dispositions.
What exists, in descending order of usefulness:

1. **`CycloneDX/sbom-utility` `test/diff/`** (Apache-2.0) — ~14 explicit `*-base.json` /
   `*-delta.json` pairs plus `cdx-1-4-mature-example-1-delta{,2}.json`. Small, but genuinely
   matched, and deliberately includes semantically-null diffs (array reordering) as negative
   controls. **This is the closest open thing to what was asked for.**
2. **`spdx/spdx-examples`** (documents CC0-1.0) — several examples ship *both* SPDX 2.2/2.3 and
   3.0 serialisations of the same software, giving free "same content, different representation"
   pairs; and `software/example10` ships `hello` and `hello-dist` content trees, giving a
   source-vs-distribution pair.
3. **`guacsec/guac` `exampledata/`** (Apache-2.0) — `cyclonedx-components-flat.json` vs
   `cyclonedx-components-nested.json`, `go-spdx-multi-arch_{1,2,3}.json`,
   `busybox-cyclonedx.json` vs its `.bz2`/`.zst` — all "same thing, shaped differently".
4. **`reproducible-builds` / diffoscope fixtures** — see §7; matched binary pairs with *expected
   diffs*, but GPL.

**Is there tooling that defines drift precisely?** Yes — one, and its ontology is worth adopting.

**rezmoss/sbomlyze** — https://github.com/rezmoss/sbomlyze — **verified licence:
Apache License 2.0** (root `LICENSE`). It defines three disjoint drift classes:
- **Version drift** — version number changed.
- **Integrity drift** — *hash changed **without** a version change*; flagged high-severity as
  tamper evidence. ("When an attacker swaps a package without bumping its version, sbomlyze
  flags it.")
- **Metadata drift** — only metadata (licences etc.) changed; low severity.

plus component-level `added` / `removed` / `changed`, dependency added/removed (direct and
transitive), detected **downgrades** and **ecosystem changes**, and a JSON policy file with rules
`max_added`, `deny_licenses`, `deny_integrity_drift`, and a compliance-score threshold. Exit code
1 on violation (and, in bare `diff` mode, on *any* change). Demo repos exist
(`sbomlyze-go-spdx-demo`, `sbomlyze-node-cyclonedx-demo`, `sbomlyze-container-demo`) with a
worked PR showing "a passing dependency update and a blocked same-version hash change".

**Recommendation:** the corpus should adopt sbomlyze's three-way drift taxonomy as its drift
factor family — in particular `integrity_drift` (hash changed, version unchanged) is the single
sharpest, most objectively checkable supply-chain factor I encountered anywhere in this research,
and it is precisely the failure mode a fab monitoring pipeline must not miss. Note also that
Harness documents "SBOM drift detection" as a product feature, but that is commercial
documentation, not open data — cite only as evidence that the concept is industrially recognised.

**Gap to fill ourselves:** matched (approved, drifted) pairs *with an approval record attached*.
Nobody publishes the approval side. The corpus can generate this credibly by taking CC0 CycloneDX
examples as the "approved" baseline and applying scripted mutations (bump version; swap hash only;
add undeclared transitive; remove supplier; change licence) — each mutation is then a case whose
`expected_disposition` is known by construction. Under CC0 (CycloneDX) and CC0 (SPDX documents)
this is unencumbered.

---

## 6. Dependency confusion, typosquatting, malicious packages

### 6.1 ossf/malicious-packages — largest open labelled feed  **[VENDOR]**

- URL: https://github.com/ossf/malicious-packages
- **Verified licence:** root `LICENSE` = **Apache License 2.0**. **Caveat, stated honestly:**
  there is *no separate data licence* declared — `README.md`, `CONTRIBUTING.md` and `docs/*.md`
  contain no licence statement at all (grepped). The Apache-2.0 in the root is therefore the only
  governing instrument for the `osv/` records. That is workable but is a repo-code licence
  applied to data; record the reliance explicitly.
- **Volume (counted on a fresh clone): 237 568 JSON records.**
  | ecosystem | records |
  |---|---|
  | npm | 221 041 |
  | PyPI | 11 695 |
  | RubyGems | 3 627 |
  | NuGet | 779 |
  | crates.io | 19 |
  | Go | 18 |
  | Maven | 2 |
  | VS Code / open-vsx | 20 |
  | Packagist, git | 2 |
  Plus `osv/withdrawn/` and `osv/unmergable/` trees.
- **Record format: OSV Schema 1.5.0** with documented additions (`docs/schema_additions.md`).
  Verified real record:
  ```json
  { "id": "MAL-2025-2925", "schema_version": "1.5.0",
    "summary": "Malicious code in 0-8 (PyPI)",
    "affected": [{ "package": { "ecosystem": "PyPI", "name": "0-8", "purl": "pkg:pypi/0-8" },
                   "versions": ["0.0.0.1"] }],
    "credits": [{ "name": "ReversingLabs", "type": "FINDER" }],
    "database_specific": { "malicious-packages-origins": [
        { "id": "RLMA-2025-01923", "source": "reversing-labs",
          "sha256": "…", "import_time": "…", "versions": ["0.0.0.1"] } ] } }
  ```
  **IDs are stable and citable**: `MAL-YYYY-NNNN` for the canonical record; origin IDs preserved
  (`RLMA-…` ReversingLabs, `GHSA-…` GitHub). `database_specific.iocs` carries
  `{domains, urls, ips, files[{paths, note, source}]}`.
- **Reuse:** the `MAL-` ID is an ideal external anchor for corpus case IDs
  (`case_id → cites → MAL-2025-2925`), and `affected[].package.purl` + `versions[]` is a direct
  oracle for `dependency_purl_and_version_appear_in_known_malicious_set`. **Do not vendor all
  237k records** — the repo is enormous; vendor a curated slice (e.g. all non-npm ecosystems,
  ~16k records) or fetch on demand.

### 6.2 DataDog/malicious-software-packages-dataset  **[metadata VENDOR, samples REF]**

- URL: https://github.com/DataDog/malicious-software-packages-dataset
- **Verified licence:** root `LICENSE` = **Apache License 2.0** (fetched raw and read).
  README additionally states attribution is required.
- **Volume:** the README states **28 266 malicious software packages** across npm, PyPI, IDE
  extensions and AI Skills.
- **Format:** samples are **encrypted ZIPs, password `infected`**, under `samples/<ecosystem>/`,
  each ecosystem carrying a `manifest.json`. Manifest semantics (verified against the live
  `samples/npm/manifest.json` and `samples/pypi/manifest.json`):
  - package **absent** from manifest → inconclusive;
  - value **`null`** → *all* versions malicious (package created with malicious intent);
  - value **a version list** → those versions of an otherwise-benign package were compromised.
  Sample real entries: `"SentinelOne": null`, `"Roblox.-com": null`, `"PaypalOtpBypass": null`,
  `"000webhost-admin": null` — brand-impersonation and typosquat names.
- **Reuse:** the **manifests are metadata, not malware — vendor those**. They are the only open
  source I found that cleanly distinguishes *malicious-by-origin* from *compromised-benign*,
  which is a distinction the corpus needs (a change that pulls in a newly-compromised version of a
  previously-approved dependency is a materially different case from one that adds a package that
  was always hostile). **Never vendor `samples/*.zip`** — live malware in a compliance corpus is
  indefensible regardless of licence.

### 6.3 DataDog/guarddog — heuristic names as factor names  **[VENDOR]**

- URL: https://github.com/DataDog/guarddog — **verified licence:** root `LICENSE` =
  **Apache License 2.0**.
- Its README publishes a **named, per-ecosystem heuristic table**. The *metadata* heuristics are
  the ones useful as compliance factors (the source-code heuristics are malware detection, less
  relevant): `typosquatting`, `npm_metadata_mismatch` ("mismatches between the npm package
  manifest and the package info for some critical fields"), `repository_integrity_mismatch`
  ("linked GitHub repository where the package has extra unexpected files"),
  `direct_url_dependency` ("dependencies fetched this way are not immutable… reduce the
  likelihood of a reproducible install"), `unclaimed_maintainer_email_domain`,
  `potentially_compromised_email_domain`, `deceptive_author`, `bundled_binary`,
  `empty_information`, `release_zero`, `single_python_file`. Code heuristics include
  `npm-install-script`, `cmd-overwrite`, `code-execution`, `download-executable`, `exec-base64`,
  `obfuscation`, `steganography`, `dll-hijacking`, `silent-process-execution`,
  `exfiltrate-sensitive-data`, `shady-links`, `unicode`, `suspicious_passwd_access_linux`.
- **Reuse:** `repository_integrity_mismatch` and `direct_url_dependency` in particular are
  precise, checkable, and directly on-point for change governance. Adopt the names.

### 6.4 ossf/package-analysis  **[VENDOR]** — **verified licence:** root `LICENSE` =
**Apache 2.0**. Dynamic + static analysis of published packages; produces per-package behavioural
records. Useful as a *second* oracle alongside GuardDog.

### 6.5 Backstabber's Knife Collection — **GATED**  **[REF, cannot vendor]**

- URL: https://dasfreak.github.io/Backstabbers-Knife-Collection/ ; paper
  https://arxiv.org/abs/2005.09535 (DIMVA 2020, Ohm et al.).
- **Access is gated.** Verified from the project page: you must email `ohm[at]cs.uni-bonn.de`
  **from an institutional address** (public providers such as Gmail are refused), supplying
  research objectives, methodology, and an institutional GitHub username; access is then granted
  to a private repository. Ecosystems npm, PyPI, RubyGems and others, real-world malicious
  packages from 2015 onward.
- **Licence:** the page says the collection is *"freely available for verified security research
  and academic evaluation purposes"* and **states no specific licence and points to no formal
  terms document.** I will not guess one. Treat as: **no redistribution rights; reference only.**
- The *paper's* attack-vector taxonomy (typosquatting, use-after-free of abandoned names,
  maintainer account takeover, malicious contribution, compromised build system) is citable and
  is a good source of provision categories even without the data.

### 6.6 Dependency-confusion PoC repos — **UNLICENSED**  **[REF, cannot vendor]**

- `snyamathi/dependency-confusion` — **no `LICENSE` file** (verified: raw fetch returns 404 on
  both `main` and `master` paths). All rights reserved by default.
- `Mustafa-Almohsen/Dependency-Confusion-Attack-PoC-Scripts` — **no `LICENSE` file** (verified:
  404). All rights reserved by default.
- **Finding: there is no open, labelled dependency-confusion corpus.** The nearest substitutes are
  §6.1 and §6.2 (which capture the *outcome* — a malicious package in a registry — rather than
  the *confusion mechanism*), and the GuardDog `typosquatting` heuristic. If the corpus needs
  dependency-confusion cases, they must be **synthesised**: the mechanism (internal package name
  resolvable from a public registry; higher public version wins; no scope/namespace pin; no
  registry pinning in `.npmrc`/`pip.conf`) is fully documented in public write-ups and can be
  encoded as factor facts without needing anyone's data.

### 6.7 Commercial feeds (Phylum, Socket) — **REF, licence not verifiable as open**
Neither publishes an openly-licensed bulk dataset that I could verify. Phylum's public research is
blog-form; Socket's public data is API-gated under commercial terms. **Do not plan on these.**
Treat any figure from them as citation-only.

---

## 7. Reproducible builds

### 7.1 diffoscope — matched pairs *with expected diffs*  **[REF — GPL-3.0-or-later]**

- URL: https://diffoscope.org · https://salsa.debian.org/reproducible-builds/diffoscope
  (GitHub mirror `anthraxx/diffoscope` used for verification; salsa.debian.org was not reachable
  through the proxy).
- **Verified licence:** `COPYING` = **GNU GENERAL PUBLIC LICENSE Version 3**; source headers in
  `diffoscope/main.py` read "either version 3 of the License, or (at your option) any later
  version" → **GPL-3.0-or-later**.
- `tests/data/` = **189 entries**, of which **67 are `*_expected_diff` files**. Structure is a
  triple: input A, input B, and the *expected textual difference*. Examples:
  `binary1` / `binary2` / `binary_expected_diff` / `binary_hexdump_expected_diff`;
  `base-files_157-r45695_ar71xx.ipk` / `base-files_157-r45918_ar71xx.ipk`;
  `Samyak-Malayalam1.ttf` / `Samyak-Malayalam2.ttf`; `Test1.class` / `Test2.class` /
  `class_expected_diff`; plus `apk_manifest_expected_diff`, `deb_metadata_expected_diff`,
  `cbfs_listing_expected_diff`, `cpio_listing_expected_diff`, `dex_expected_diffs`,
  `device_expected_diff` (+ `_reverse`).
- **This is the richest matched-pair-with-oracle corpus in the whole lane** — and it is
  **GPL-3.0-or-later, so it must not be vendored into a permissively-licensed corpus.** Reference
  it, cite specific fixture names, and if the corpus genuinely needs binary-diff cases, generate
  equivalents rather than copying.

### 7.2 rebuilderd  **[REF — GPL-3.0]**
- URL: https://github.com/kpcyrd/rebuilderd — **verified licence:** root `LICENSE` = **GNU
  GENERAL PUBLIC LICENSE Version 3**. Independent-rebuild verification service; its
  `GOOD`/`BAD`/`UNKWN` per-package verdicts are the right *model* for a rebuild-attestation
  factor, but GPL means reference-only.
- Related: `tests.reproducible-builds.org` publishes Debian-wide reproducibility status. Treat the
  status data as reference; I could not verify an explicit licence grant on the status database
  and will not assert one.

### 7.3 prefix-dev/reproducible-builds — conda ecosystem rebuild results. Licence not verified in
this pass; **do not rely on it** until checked.

---

## 8. OpenSSF: organisation- and pipeline-level conformance

This section answers the "conformance suite that scores an ORGANISATION rather than an artifact"
question. There are four real ones, and one of them is a near-perfect structural template.

### 8.1 **OpenSSF Security Baseline (OSPS Baseline)** — the best provision catalogue found  **[VENDOR]**

- URL: https://github.com/ossf/security-baseline · https://baseline.openssf.org
- **Verified licence:** root `LICENSE` = **Apache License 2.0**.
- **All controls are maintained as machine-readable YAML** under the **Gemara Layer 2** schema.
  Eight control families, each its own file — **106 controls total** (counted):
  | file | family | controls |
  |---|---|---|
  | `baseline/OSPS-AC.yaml` | Access Control | 10 |
  | `baseline/OSPS-BR.yaml` | **Build & Release** | **20** |
  | `baseline/OSPS-DO.yaml` | Documentation | 15 |
  | `baseline/OSPS-GV.yaml` | Governance | 10 |
  | `baseline/OSPS-LE.yaml` | Legal | 8 |
  | `baseline/OSPS-QA.yaml` | Quality | 20 |
  | `baseline/OSPS-SA.yaml` | Security Assessment | 7 |
  | `baseline/OSPS-VM.yaml` | Vulnerability Management | 16 |
- **Structure is exactly the corpus tuple.** Verified from `OSPS-BR.yaml`:
  ```yaml
  controls:
    - id: OSPS-BR-01                       # provision id — stable, citable
      title: Prevent Untrusted Input When Building & Releasing
      objective: |                          # rationale
        Reduce the risk of code injection … by preventing untrusted input from
        accessing privileged resources.
      group: BR
      assessment-requirements:
        - id: OSPS-BR-01.01                # sub-provision — this is the checkable unit
          text: |
            When a CI/CD pipeline operates on untrusted metadata, those parameters
            MUST be sanitized and validated prior to use in the pipeline.
          applicability: [maturity-1, maturity-2, maturity-3]   # scope / in-force test
          recommendation: | …
        - id: OSPS-BR-01.03
          text: |
            When a CI/CD pipeline operates on untrusted code snapshots, it MUST
            prevent access to privileged CI/CD credentials and assets.
          applicability: [maturity-1, maturity-2, maturity-3]
        - id: OSPS-BR-01.04
          text: … MUST sanitize and validate collaborator input …
          applicability: [maturity-3]      # applies only at highest maturity
        - id: OSPS-BR-01.02
          text: Retired in https://github.com/ossf/security-baseline/pull/443
          state: Retired                   # amendment/repeal tracking, built in
  ```
- **Why this is the template:** it gives you (a) hierarchical, versioned, **citable provision IDs**
  (`OSPS-BR-01.03`) — the thing SLSA conspicuously lacks; (b) explicit **MUST/SHOULD modality** in
  the requirement text; (c) **`applicability`** as a maturity-scoped in-force test, which is how
  you model "this provision binds only pipelines above tier N"; (d) a **`state: Retired`**
  lifecycle with a link to the amending PR — i.e. the catalogue already models legislative
  amendment. Nothing else in this lane does all four.
- **Reuse:** either adopt OSPS IDs directly for the overlapping subject matter (BR + AC + QA cover
  most of a change-governance regime) and add semiconductor-specific families alongside, or mint
  corpus IDs and publish an `OSPS-BR-* → corpus provision` crosswalk. The Build & Release family
  alone is 20 controls that are already about *pipelines*.

### 8.2 ossf/gemara — the schema behind it  **[VENDOR]**
- URL: https://github.com/ossf/gemara — **verified licence:** root `LICENSE` =
  **Apache License 2.0**. "GRC Engineering Model for Automated Risk Assessment"; layered model
  (Layer 2 = controls, Layer 4/5 = evaluation and enforcement). Already used by OSPS Baseline and
  by FINOS Common Cloud Controls (Layer 2), and by `privateerproj/privateer` (Layer 5).
- **Reuse:** if the corpus wants its provisions to be consumable by existing GRC tooling rather
  than bespoke, express them in Gemara Layer 2 and its results in the Layer 4 shape.

### 8.3 ossf/scorecard  **[code VENDOR; data CDLA-Permissive-2.0]**

- URL: https://github.com/ossf/scorecard
- **Verified licences — two distinct ones, do not conflate:**
  - **Code:** root `LICENSE` = **Apache License 2.0**.
  - **Data:** `README.md` line 201 states verbatim:
    > "Data provided by the REST API is licensed under the [CDLA Permissive 2.0](https://cdla.dev/permissive-2-0)."

    **Scope note, stated precisely:** that sentence covers the **REST API** data. The README's
    separate BigQuery paragraph (lines 141–166) names the public dataset
    **`openssf:scorecardcron.scorecard-v2`** and the latest-results view
    `openssf:scorecardcron.scorecard-v2_latest`, with `bq extract` instructions to GCS, but
    **does not itself restate a licence**. Treat CDLA-Permissive-2.0 as the project's stated
    position on its published data and cite the README line; do not silently extend it to the
    BigQuery dataset without asking upstream. CDLA-Permissive-2.0 requires that a recipient who
    redistributes the *Data* also make the agreement text available, and imposes **no**
    obligations on *Results* derived from it — so deriving corpus factor labels is unencumbered;
    republishing rows is the part that carries the obligation.
- **20 checks, each a named repository/organisation-level control** (from `docs/checks.md`):
  `Binary-Artifacts`, `Branch-Protection`, `CI-Tests`, `CII-Best-Practices`, `Code-Review`,
  `Contributors`, `Dangerous-Workflow`, `Dependency-Update-Tool`, `Fuzzing`, `License`,
  `Maintained`, `Packaging`, `Pinned-Dependencies`, `SAST`, `SBOM`, `Security-Policy`,
  `Signed-Releases`, `Token-Permissions`, `Vulnerabilities`, `Webhooks`.
- **Reuse:** `Pinned-Dependencies`, `Dangerous-Workflow`, `Token-Permissions`, `Branch-Protection`,
  `Code-Review` and `Signed-Releases` are directly on-point pipeline-governance factors with
  published, stable names and a working reference implementation. Use Scorecard as an oracle for
  those six; use the CDLA data only for population statistics (how common is each violation),
  which is useful for arguing corpus case-mix realism.

### 8.4 ossf/allstar  **[VENDOR]**
- URL: https://github.com/ossf/allstar — **verified licence:** root `LICENSE` =
  **Apache License 2.0**.
- Explicitly org-scoped: README sections cover **Org-Level Options**, *Org-level Base and Merge
  Configuration Location*, *Repo policy configurations in the Org Repo*, and *Secondary Org-Level
  configuration location*. Policies: **Branch Protection, Binary Artifacts, CODEOWNERS, Outside
  Collaborators, SECURITY.md, Dangerous Workflow, Generic Scorecard Check, GitHub Actions,
  Repository Administrators** (+ Future Policies). Actions are configurable (issue / log / fix).
- **Reuse:** Allstar is the clearest open precedent for *continuous* org-level policy enforcement
  with an org-wide base config that individual repos may merge but not override — which is the
  governance shape a fab's change-control regime actually has. Its `Outside Collaborators` and
  `Repository Administrators` policies are good sources for access-control factors.

### 8.5 OpenSSF Best Practices badge (coreinfrastructure/best-practices-badge)  **[VENDOR — read the split]**

- URL: https://github.com/coreinfrastructure/best-practices-badge · https://www.bestpractices.dev
- **Verified licence — a three-part split, quoted from `README.md` §License:**
  - **Code/repo material:** **MIT** (root `LICENSE` opens "The MIT License (MIT)"). README also
    carries `SPDX-License-Identifier: (MIT OR CC-BY-3.0+)` for non-executable material.
  - **The *data managed by* the application, by update date:**
    > "Data updated on or after 2024-08-23T12:00:00Z is released under the Community Data License
    > Agreement – Permissive, Version 2.0 (CDLA-Permissive-2.0)."
    > "Otherwise, data updated on or after 2017-02-20T12:00:00Z is released under … (CC-BY-3.0+)."
    > "Otherwise, data is released under … (CC-BY-3.0)."
    > "The *complete* collection of data … is thus licensed with the SPDX license expression
    > '(CC-BY-3.0 AND CDLA-Permissive-2.0)'."
  - So: **MIT code; project data = `CC-BY-3.0 AND CDLA-Permissive-2.0`**, reducible to
    `CC-BY-3.0+ AND CDLA-Permissive-2.0` if the oldest entries are dropped. This is a genuinely
    time-sliced licence and must be recorded as such.
- **Criteria: 145** (counted `category:` keys in `criteria/criteria.yml`), each with a stable
  snake_case identifier and a **`category: MUST | SHOULD | SUGGESTED`** modality, plus
  `na_allowed`, `na_justification_required`, `met_justification_required`, `met_url_required`,
  `future`, `obsolete`. Sample IDs: `description_good`, `interact`, `contribution`,
  `contribution_requirements`, `floss_license`, `floss_license_osi`, `license_location`,
  `documentation_basics`, `documentation_interface`, `sites_https`, `discussion`, `english`,
  `maintained`, `repo_public`, `repo_track`, `repo_interim`, `repo_distributed`,
  `version_unique`, `version_semver`, `version_tags`.
- **Reuse:** the `criteria.yml` field set is the best open model for **evidence handling** —
  `met_url_required`, `met_justification_required`, `na_allowed`, `na_justification_required`
  encode *what counts as proof that a provision is satisfied, and when a provision may be
  disapplied*. A compliance corpus that only records true/false will be weaker than one that
  records whether justification/evidence was required and supplied. Steal this field set.
  (Live JSON endpoints on bestpractices.dev were 403 through the research proxy; fetch the data
  dump separately before relying on volume figures.)

### 8.6 NIST SP 800-218 (SSDF) and control mappings  **[public domain, but verify each mapping]**
- SP 800-218 is a US federal government publication; NIST publications are generally not subject
  to copyright in the United States. **State it that way, do not label it with an SPDX ID.**
- Its practice identifiers (`PO.*` Prepare the Organization, `PS.*` Protect the Software,
  `PW.*` Produce Well-Secured Software, `RV.*` Respond to Vulnerabilities) **are** individually
  numbered and citable — unlike SLSA — and `PO.*` is explicitly organisation-level, which is
  what this corpus needs.
- I did **not** find an authoritative, openly-licensed SSDF↔SLSA↔Scorecard crosswalk that I could
  verify in this pass (`ossf/s2c2f` had no `LICENSE` at the path I checked and its README carried
  no licence line I could confirm — **do not cite it as open until verified**). OSPS Baseline
  (§8.1) is the better-verified control catalogue; build the SSDF crosswalk yourself against
  SP 800-218's own numbering.

---

## 9. Recommended factor vocabulary for the corpus

Chosen for being (i) objectively checkable by an existing open tool, (ii) unambiguous as a
boolean, and (iii) traceable to a verified-licence source. Grouped by provision family.

**Build provenance / attestation** — oracle: slsa-verifier (Apache-2.0)
- `provenance_attestation_present_for_artifact_digest`
- `provenance_attestation_verified_against_expected_builder_id`
- `provenance_builder_id_matches_org_allowlisted_builder`
- `provenance_source_uri_matches_declared_repository`
- `provenance_source_ref_matches_released_tag`
- `provenance_versioned_tag_semver_compatible_with_release`
- `provenance_workflow_inputs_match_declared_inputs`
- `provenance_subject_digest_matches_distributed_artifact_digest`
- `provenance_signature_verifies_under_fulcio_certificate`
- `provenance_certificate_oidc_issuer_in_trusted_issuer_set`
- `provenance_certificate_valid_at_signing_time` (not expired — cf. `-expired-cert` fixture)
- `provenance_recorded_in_transparency_log`
- `provenance_predicate_type_matches_expected_predicate_type`
- `reusable_workflow_reference_in_trusted_workflow_set`
- `vsa_verified_levels_meet_or_exceed_required_slsa_level`

**SBOM completeness** — oracle: ntia-conformance-checker + sbomqs (both Apache-2.0)
- `sbom_present_for_release_artifact`
- `sbom_parses_against_declared_spec_version`
- `sbom_declares_creation_timestamp`
- `sbom_declares_author_or_tool`
- `sbom_declares_primary_component`
- `all_components_declare_name`
- `all_components_declare_version`
- `all_components_declare_unique_identifier`
- `all_components_declare_supplier`
- `all_components_declare_checksum_sha256`
- `all_components_declare_concluded_license`
- `dependency_relationships_declared_for_primary_component`
- `dependency_graph_has_no_floating_components`
- `sbom_document_signature_present_and_verifies`

**SBOM drift** — oracle: sbomlyze taxonomy + sbom-utility diff (both Apache-2.0)
- `component_set_matches_approved_baseline_sbom`
- `component_integrity_drift_detected` — *hash changed with version unchanged; the sharpest one*
- `component_version_drift_within_approved_range`
- `component_version_downgrade_detected`
- `undeclared_transitive_dependency_introduced`
- `component_removed_without_approval_record`
- `component_license_changed_from_baseline`
- `component_ecosystem_changed_from_baseline`
- `drift_is_semantically_null` — array reordering only; the false-positive guard

**Dependency intake** — oracle: ossf/malicious-packages, GuardDog, Datadog manifests
- `dependency_purl_in_known_malicious_package_set`
- `dependency_version_in_known_compromised_version_set`
- `dependency_resolved_from_declared_internal_registry_only`
- `dependency_pinned_to_immutable_digest_not_floating_range`
- `dependency_is_direct_url_dependency` (non-immutable fetch)
- `package_name_within_edit_distance_of_popular_package_name` (typosquat)
- `package_repository_integrity_matches_linked_source_repository`
- `maintainer_email_domain_unclaimed_or_recently_expired`
- `dependency_supplier_in_approved_supplier_list`

**Pipeline & change governance** — oracle: OSPS Baseline, Scorecard, Allstar (all Apache-2.0)
- `pipeline_sanitises_untrusted_metadata_before_use` (≈ OSPS-BR-01.01)
- `pipeline_denies_privileged_credentials_to_untrusted_code` (≈ OSPS-BR-01.03)
- `workflow_token_permissions_least_privilege_declared`
- `workflow_actions_pinned_to_commit_sha`
- `no_dangerous_workflow_pattern_present` (untrusted-checkout / script injection)
- `protected_branch_requires_review_before_merge`
- `change_reviewed_by_second_authorised_person` (≈ SLSA Source L4 two-party review)
- `release_artifact_signed_by_authorised_functionary`
- `build_executed_on_hosted_isolated_platform`
- `build_is_independently_reproducible`

**Evidence / disposition metadata** — pattern from best-practices-badge + in-toto SVR
- `provision_applicability_asserted_for_this_pipeline_maturity`
- `justification_supplied_where_required`
- `evidence_url_supplied_where_required`
- `provision_disapplied_with_recorded_justification` (the `na_allowed` case)

---

## 10. Vendor / reference-only summary

| Source | Verified licence | Verdict |
|---|---|---|
| slsa-framework/slsa (spec) | Community-Spec-1.0 + Apache-2.0 (dual) | **REF** — cite, restate; do not paste prose |
| spdx/spdx-spec | Community-Spec-1.0 + CC-BY-3.0 (dual) | **REF** — same |
| slsa-framework/slsa-verifier | Apache-2.0 | **VENDOR** (subset — 297 MB full) |
| slsa-framework/slsa-github-generator | Apache-2.0 | **VENDOR** |
| in-toto/attestation | Apache-2.0 | **VENDOR** |
| in-toto/witness | Apache-2.0 | **VENDOR** |
| guacsec/guac | Apache-2.0 | **VENDOR** |
| sigstore/sigstore-conformance | Apache-2.0 **asserted in README only; no LICENSE file** | **VENDOR with caveat** — record the assertion + SHA |
| sigstore/cosign · rekor · fulcio · model-transparency | Apache-2.0 | **VENDOR** |
| spdx/spdx-examples — SPDX documents | **CC0-1.0** | **VENDOR** |
| spdx/spdx-examples — `content/` source | **GPL-3.0-or-later** | **REF — do not vendor** |
| CycloneDX/sbom-examples | **CC0-1.0** | **VENDOR** (cleanest in lane) |
| CycloneDX/specification (schema suite, 975 files) | Apache-2.0 | **VENDOR** |
| CycloneDX/sbom-utility (incl. `test/diff/`) | Apache-2.0 | **VENDOR** |
| spdx/ntia-conformance-checker | Apache-2.0 (LICENSE + pyproject agree) | **VENDOR** |
| interlynk-io/sbomqs | Apache-2.0 | **VENDOR** |
| eBay/sbom-scorecard | Apache-2.0 | **VENDOR** |
| protobom · cyclonedx-cli · sbomlyze | Apache-2.0 | **VENDOR** |
| ossf/malicious-packages (237 568 records) | Apache-2.0 (repo LICENSE; no separate data licence) | **VENDOR** (curated slice) |
| DataDog dataset — manifests | Apache-2.0 + attribution | **VENDOR** |
| DataDog dataset — sample ZIPs | Apache-2.0 | **REF — never vendor live malware** |
| DataDog/guarddog · ossf/package-analysis | Apache-2.0 | **VENDOR** |
| Backstabber's Knife Collection | **no licence stated; institutional-email gated** | **REF — no redistribution rights** |
| snyamathi/dependency-confusion | **no LICENSE (all rights reserved)** | **REF** |
| Mustafa-Almohsen/…-PoC-Scripts | **no LICENSE (all rights reserved)** | **REF** |
| diffoscope (189 fixtures, 67 expected-diffs) | **GPL-3.0-or-later** | **REF — copyleft** |
| rebuilderd | **GPL-3.0** | **REF — copyleft** |
| ossf/security-baseline (OSPS, 106 controls) | Apache-2.0 | **VENDOR** — best provision catalogue |
| ossf/gemara | Apache-2.0 | **VENDOR** |
| ossf/scorecard — code | Apache-2.0 | **VENDOR** |
| ossf/scorecard — REST API data | **CDLA-Permissive-2.0** (README line 201) | **VENDOR** with agreement text |
| ossf/allstar | Apache-2.0 | **VENDOR** |
| best-practices-badge — code | **MIT** (non-executable also CC-BY-3.0+) | **VENDOR** |
| best-practices-badge — project data | **CC-BY-3.0 AND CDLA-Permissive-2.0** (date-sliced) | **VENDOR** with attribution |
| NIST SP 800-218 (SSDF) | US federal publication, not copyrighted in the US | **REF/VENDOR** — no SPDX ID; state the basis |
| ossf/s2c2f | **not verified — LICENSE not found at checked path** | **DO NOT CITE AS OPEN** until checked |
| Phylum, Socket public data | **no open licence verified** | **REF only** |

## 11. Honest gaps

1. **No open (approved SBOM, drifted SBOM) pair corpus exists.** Nearest is sbom-utility
   `test/diff/`. The corpus must synthesise pairs — legitimate under CC0 CycloneDX/SPDX documents.
2. **No open labelled dependency-confusion corpus exists.** PoC repos are unlicensed;
   Backstabber's is gated; malicious-package feeds capture outcome, not mechanism.
3. **SLSA build-track requirements have no citable provision IDs.** OSPS Baseline does; use it as
   the identifier backbone and crosswalk SLSA by heading + level.
4. **sigstore-conformance ships no LICENSE file** despite a README claim of Apache-2.0.
5. **The richest matched-pair-with-oracle data (diffoscope) is GPL-3.0-or-later** and therefore
   unusable inside a permissive corpus.
6. **No verified open SSDF↔SLSA↔Scorecard crosswalk** was found; `ossf/s2c2f` could not be
   licence-verified in this pass.
7. **bestpractices.dev JSON endpoints returned 403 through the research proxy**, so badge data
   *volume* is unverified (the licence terms and 145 criteria count are verified from the repo).
