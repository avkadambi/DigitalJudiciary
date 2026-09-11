# 03 — Policy-as-Code, Software Supply Chain, and Conformance-Suite Design Precedent

Research lane: reusable open-source test data and conformance-suite design conventions for a
compliance test corpus for veterinary software delivery pipelines governed by a "Digital Judiciary"
(constitution of provisions → adjudicated cases → binding precedent).

**Target corpus record shape:** `(case_id, provisions_engaged[], boolean factor facts{}, expected_disposition)`

**Date of verification:** 2026-09-05. All licenses below were checked against the actual LICENSE
file, repository license metadata, or an explicit in-page license statement. Anything not directly
verified is marked **UNVERIFIED** and must not be treated as cleared.

---

## 0. Executive orientation

Three things this lane yields:

1. **Direct-fit corpora** — datasets whose native record shape is already
   *(identifier, provision reference, fact scenario, expected outcome)*. The strongest are
   **openai/model_spec_dataset** (CC0, a constitution + 596 cases keyed to clause IDs), the
   **Gatekeeper library** gator suites, **Cedar integration tests**, and **Kyverno** test manifests.
2. **Factor-fact mines** — corpora that supply realistic boolean predicates about a software delivery
   pipeline (signed? provenance attached? SBOM present? license permissive? dependency malicious?).
   ComplianceAsCode, OSCAL, SLSA/in-toto, Scorecard, SPDX/CycloneDX, ScanCode LicenseDB.
3. **Suite-design precedent** — how mature conformance suites encode identity, expectation, negative
   controls and known-failure. test262, WPT/wptrunner, JSON Schema Test Suite, sqllogictest,
   Jakarta/Bean Validation TCK, sigstore-conformance, and the mutation-testing report schema.

---

## 1. Policy-as-code corpora

| Source | URL | Contents | Format | Verified license | Volume | Reuse for our corpus | Vendor? |
|---|---|---|---|---|---|---|---|
| **OPA Gatekeeper Library** | https://github.com/open-policy-agent/gatekeeper-library | Community Kubernetes admission policies: ConstraintTemplates, Constraints, `suite.yaml` gator test suites, `samples/*/example_allowed.yaml` + `example_disallowed.yaml`, Rego `src.rego` + `src_test.rego` | YAML + Rego | **Apache-2.0** (LICENSE + NOTICE in repo) | ~500+ commits; dozens of policy families each with paired allowed/disallowed samples | The `suite.yaml` → `tests[]` → `cases[]` → `assertions[]` hierarchy is a near-exact structural analogue of *constitution → provision → case → expected disposition*. The paired allowed/disallowed samples are ready-made positive/negative controls. Adapt the policy text to veterinary-pipeline provisions. | **VENDOR** (Apache-2.0, attribution + NOTICE) |
| **OPA / Rego test framework** | https://github.com/open-policy-agent/opa · https://www.openpolicyagent.org/docs/policy-testing | `opa test`; rules prefixed `test_` are tests, `todo_` prefixed are reported SKIPPED; `with` keyword mocks data and functions; `--coverage` emits per-line covered/not-covered with `index_excluded` / `early_exit` annotations; `--format=json` yields structured results with location and duration | Rego, JSON report | **Apache-2.0** (repo license metadata) | n/a (engine, not corpus) | Adopt as the *execution engine* for the corpus if dispositions are computable. Steal three conventions verbatim: `test_` naming discipline, `todo_` as a first-class SKIP marker (better than commenting out a case), and coverage-of-provisions reporting. | **VENDOR** (tool) |
| **Conftest** | https://github.com/open-policy-agent/conftest | Rego policy runner over structured config (K8s, Terraform, Dockerfiles); `deny` / `violation` / `warn` rule families; exceptions; `--combine` for cross-document rules | Rego + YAML/JSON/HCL | **UNVERIFIED** — repo shows a LICENSE file but the type was not readable via the fetches attempted (GitHub API returned 403). Project is CNCF/OPA-adjacent so Apache-2.0 is *likely* but must be confirmed before vendoring. | n/a | The three-tier `deny`/`warn`/`violation` severity split maps cleanly onto dispositions richer than boolean (e.g. `VIOLATION` / `CAUTION` / `COMPLIANT`). The exceptions mechanism is a model for precedent-based carve-outs. | **REFERENCE-ONLY until license confirmed** |
| **Kyverno policy library** | https://github.com/kyverno/policies | ~80+ top-level policy directories (pod security, best practices, AWS, Istio, Linkerd, Velero, Karpenter, Tekton), with `-cel`, `-vpol`, `-mpol`, `-gpol` variants; each ships `.kyverno-test/kyverno-test.yaml` plus `resource.yaml` | YAML | **Apache-2.0** (stated in repo) | 1,599 commits; hundreds of policies, most with test manifests | **The single best format match.** A `kind: Test` manifest lists `policies`, `resources`, and a `results[]` array where each entry is `{policy, rule, kind, resources[], result: pass\|fail\|skip\|warn\|error}`. That is literally *(provision, sub-provision, subject, expected disposition)*. Verbatim example verified from `best-practices/require-labels/.kyverno-test/kyverno-test.yaml`. | **VENDOR** |
| **kyverno-json** | https://github.com/kyverno/kyverno-json | Applies Kyverno assertion policies to *any* JSON/YAML payload — Terraform plans, Dockerfiles, cloud configs, service authorization requests | YAML policies + JSON payloads | **Apache-2.0** ("kyverno-json is licensed under the Apache License 2.0") | early-stage; catalog of sample policies | Lets us keep the Kyverno test-manifest shape while our "resources" are arbitrary pipeline-fact JSON documents rather than Kubernetes objects. This is the most likely off-the-shelf runner for a boolean-factor-fact corpus. | **VENDOR** |
| **Cedar integration tests** | https://github.com/cedar-policy/cedar-integration-tests | Handwritten tests in `tests/`, `sample-data/`, and an auto-generated fuzzing corpus `corpus-tests.tar.gz`; submodules for `cedar` and `cedar-spec` | JSON | **Apache-2.0** ("This project is licensed under the Apache-2.0 License") | Corpus generated from a 6-hour coverage-guided fuzz run of the `abac` target, then reduced with `cmin`; exact case count not published in README (`scripts/get_corpus_stats.py` computes it) | Test schema verified: `policies`, `policyFormat` (`cedar`\|`json`), `entities`, `schema`, `schemaFormat`, `shouldValidate`, and `requests[]` with `description`, `principal`, `action`, `resource`, `context`, `validateRequest`, `decision` (`Allow`\|`Deny`), `reason` (the policies responsible), `errors`. **The `reason` field is the key idea to copy:** the expected result names *which provisions produced the disposition*, not just the disposition. That is exactly "provisions engaged." Also the strongest precedent for *generating* corpus cases by fuzzing rather than hand-authoring. | **VENDOR** |
| **AWS Cedar formal spec (cedar-spec)** | https://github.com/cedar-policy/cedar-spec (submodule of the above) | Lean formal model + differential-testing harness that the corpus is generated against | Lean / Rust | **UNVERIFIED** (not separately fetched) | n/a | Precedent for a *dual-implementation* corpus: an executable spec and an implementation, with the corpus as the differential oracle. Relevant if the Digital Judiciary has both a written constitution and a reference adjudicator. | **REFERENCE-ONLY** |

### 1a. Verified Kyverno test manifest (copy this shape)

```yaml
apiVersion: cli.kyverno.io/v1alpha1
kind: Test
metadata:
  name: require-labels
policies:
- ../require-labels.yaml
resources:
- resource.yaml
results:
- kind: Pod
  policy: require-labels
  resources: [badpod01, badpod02]
  result: fail
  rule: check-for-labels
- kind: Pod
  policy: require-labels
  resources: [goodpod01, goodpod02]
  result: pass
  rule: check-for-labels
```

### 1b. Verified Gatekeeper `gator` suite shape

```yaml
kind: Suite
apiVersion: test.gatekeeper.sh/v1alpha1
tests:
- name: <test name>
  template: <path to ConstraintTemplate>
  constraint: <path to Constraint>
  cases:
  - name: <case name>
    object: <path to object or AdmissionReview>
    inventory: [<paths for data.inventory>]
    assertions:
    - violations: 2                # "yes" (>=1) | "no" (0) | exact integer
    - message: initContainer       # case-sensitive regex over violation text
      violations: 1
```

The `violations: yes | no | <int>` tri-state and the *regex-over-message* assertion are both worth
copying: they let a case assert not merely "violated" but "violated **this** provision **this many
times**," and `violations: "no"` with a `message` filter is a clean negative control.

---

## 2. Security-compliance content corpora (factor-fact mines)

| Source | URL | Contents | Format | Verified license | Volume | Reuse | Vendor? |
|---|---|---|---|---|---|---|---|
| **ComplianceAsCode / content** | https://github.com/ComplianceAsCode/content | The largest open compliance rule corpus: YAML rule definitions, OVAL checks, XCCDF, CEL content for K8s/OpenShift, Ansible + Bash remediations, control mappings to NIST/PCI-DSS/CIS/STIG/OSPP; `tests/` holds per-rule validation | YAML, OVAL XML, XCCDF, Ansible, Bash | **BSD-3-Clause** — verified verbatim from LICENSE: `SPDX license identifier: BSD-3-Clause / Copyright (c) 2012-2017, Red Hat, Inc.` | 44,047 commits; thousands of rules across RHEL, Fedora, Ubuntu, Debian, SLES + application products; `/linux_os/guide`, `/products`, `/controls`, `/components`, `/shared`, `/tests` | The richest source of *provision text ↔ machine-checkable predicate ↔ pass/fail evidence* triples in open source, and the `controls/` directory is a working example of one control mapping to many rules — the same many-to-many that "provisions engaged" needs. Mine rule descriptions and rationale for veterinary-pipeline analogues; mine `tests/` for the convention of per-rule positive and negative scenario scripts. | **VENDOR** (BSD-3-Clause; retain copyright notice) |
| **NIST OSCAL content** | https://github.com/usnistgov/OSCAL-content | Machine-readable NIST SP 800-53 Rev 4 and Rev 5 catalogs, plus low/moderate/high baselines per SP 800-53B; sample content per OSCAL model | XML, JSON, YAML | **Public domain (US Government work) + CC0-1.0** — verified verbatim: "As a work of the United States government, this project is in the public domain within the United States. Additionally, we waive copyright and related rights in the work worldwide through the CC0 1.0 Universal public domain dedication." | 415 commits; full 800-53 Rev 4 + Rev 5 catalogs and baselines in three serializations | **The model for the constitution itself.** OSCAL's `catalog` → `group` → `control` → `part` → `prop`/`link` hierarchy with stable `id` attributes is a battle-tested schema for a numbered constitution of provisions, and `profile` (with `import`, `include-controls`, `alter`, `set-parameter`) is a proven mechanism for *tailoring* a constitution to a jurisdiction — directly reusable for "which provisions apply to this class of veterinary pipeline." CC0 means the schema and even control text can be lifted freely. | **VENDOR** (CC0) |
| **CIS Benchmarks (the PDFs)** | https://www.cisecurity.org/cis-benchmarks | Prose benchmark documents | PDF | **UNVERIFIED / restrictive** — CIS distributes benchmarks under its own terms of use, not an OSI license. Do not vendor. | — | Use only as conceptual reference. The *open* re-expression of CIS content lives in ComplianceAsCode above; take it from there instead. | **REFERENCE-ONLY** |
| **NIST AI RMF (AI 100-1) + Playbook** | https://www.nist.gov/itl/ai-risk-management-framework · https://airc.nist.gov | Framework, Playbook (Govern/Map/Measure/Manage sub-categories), crosswalks to other frameworks, Generative AI Profile (NIST AI 600-1) | PDF, web; Playbook is structured | **US Government work → public domain** (NIST works; confirm per-artifact) | 4 functions, dozens of categories/subcategories | Subcategory IDs (`GOVERN 1.1`, `MAP 2.3`, …) are a clean precedent for a hierarchical, citable provision identifier space. Crosswalk documents are the model for mapping our provisions onto external regimes. | **VENDOR** (public domain; verify each file) |
| **ISO/IEC 42001** | iso.org | AI management system standard | PDF, paywalled | **PROPRIETARY — paywalled, not reusable** | — | Cite by clause number only. Never copy text. | **REFERENCE-ONLY** |
| **EU AI Act evaluation benchmark** | https://github.com/davidath/ai-act-evaluation-benchmark | `scenarios.json` (Role: Provider/Deployer, Intended Use, System Type, Input Data, Domain, **Related Articles**, **Obligations**) and `qa_pairs.json`; tasks: risk-level classification, article retrieval, obligation generation, QA | JSON | **Data: CC-BY-4.0; code: Apache-2.0** (stated in repo) | Two primary JSON files; exact record counts not stated | The single closest *legal* analogue to our target record: a fact scenario, the articles it engages, and the expected obligations/risk classification. Directly reusable as a template for `(case_id, provisions_engaged, factor facts, expected disposition)` in a regulatory rather than technical register. | **VENDOR** (CC-BY-4.0 attribution) |
| **COMPL-AI** | https://github.com/compl-ai/compl-ai | EU AI Act technical interpretation → benchmark mapping; 6 principles, 8–9 technical-requirement categories, 29+ benchmarks; built on the Inspect eval framework; YAML/JSON task configs, `default_config.yaml` | Python, YAML/JSON | **Apache-2.0** | 29+ benchmarks across 9 requirement categories | The reference implementation of *regulatory-provision → technical-test* mapping. Copy its structure: each requirement category holds N benchmarks, each benchmark reports a normalized score, and the aggregate rolls up per principle. That roll-up is how a Digital Judiciary would report conformance per constitutional chapter. | **VENDOR** |

---

## 3. Software supply chain

| Source | URL | Contents | Format | Verified license | Volume | Reuse | Vendor? |
|---|---|---|---|---|---|---|---|
| **SLSA framework** | https://github.com/slsa-framework/slsa | Specification (`spec/`, release branches `releases/v1.0`, `releases/v1.2`), website sources; build levels L1–L3 and requirement tables | Markdown | **Dual: Community Specification License 1.0** for content contributed under the Community Specification governance model, **Apache-2.0** for pre-existing portions from contributors who have not re-contributed under CSL 1.0 | Spec + track requirements | The Build/Source track requirement tables are a ready-made hierarchy of provisions with levels — an excellent template for a graded disposition ("meets L2 but not L3") rather than a boolean. **Caution:** the CSL-1.0 half carries patent and attribution obligations distinct from Apache-2.0; treat mixed-license text carefully. | **REFERENCE-ONLY** for spec text (dual-license complexity); concepts freely reusable |
| **slsa-verifier** | https://github.com/slsa-framework/slsa-verifier | Provenance verification CLI; `testdata/` including VSA test data at `cli/slsa-verifier/testdata/vsa/gce/v1/` (example attestations + public keys) and GitHub attestation examples | Go, JSON | **Apache-2.0** | Moderate `testdata` corpus | Real signed/unsigned provenance documents = ready-made boolean factor facts (`provenance_present`, `builder_id_matches`, `source_repo_matches`, `signature_valid`). Good negative fixtures. | **VENDOR** |
| **in-toto attestation** | https://github.com/in-toto/attestation | Attestation framework spec (`spec/v1`), vetted predicate types (`spec/predicates`), protobuf definitions with Go/Python/Rust/Java bindings, `examples/go` | Markdown, Protobuf, JSON | **Apache-2.0** — verified from LICENSE ("Licensed under the Apache License, Version 2.0") | Spec + several predicate types + language bindings | The Statement/Predicate split (`subject` + `predicateType` + `predicate`) is the right envelope for evidence attached to a case: our factor facts become predicate fields on a subject artifact. Predicate type URIs are also a good identifier-space precedent for *typed* evidence. | **VENDOR** |
| **sigstore-conformance** | https://github.com/sigstore/sigstore-conformance | Client conformance suite: clients implement a documented CLI protocol; workflow-focused signing + verification tests against production and staging Rekor/Fulcio | Python (pytest) | **Apache-2.0** ("Apache 2.0 License") | 257 commits, 29 releases (latest v0.0.29, June 2026); verification + signing suites with parametrized tests | **Best precedent for expected-failure handling in this lane.** It whitelists tests expected to fail via whitespace-separated **`xfail` patterns with shell-style wildcards**, explicitly to accommodate optional features (managed keys, deprecated in-toto types). Copy this: a corpus for a *young* constitution needs an expected-fail list keyed by glob over case IDs, so partial adopters can still run the suite. Also copy the `must_pass` / `must_fail` helper split — the suite forces every case to declare its polarity. | **VENDOR** (harness design) |
| **OpenSSF malicious-packages** | https://github.com/ossf/malicious-packages | Reports of malicious packages in OSS registries, consumable as OSV records; `osv/malicious/<ecosystem>/<package>/`, withdrawn reports under `osv/withdrawn/` | JSON (OSV schema) | **Apache-2.0** (repo license metadata) | 11,844 commits; daily-updated stats at ossf.github.io/malicious-packages/stats (exact count not read) | Report IDs follow `MAL-0000-[name].json` at contribution time, with the real `id` **assigned automatically** on ingest — a good two-phase ID pattern (author-supplied slug → registry-assigned canonical ID) worth copying for community-contributed cases. Required fields: `affected[0].package.ecosystem` + `.name`, `affected[0].ranges` or `.versions`, `details` (why malicious), and at least one of `credits`/`references`. Provides thousands of real dependency-level boolean facts (`dependency_is_known_malicious`). | **VENDOR** |
| **Backstabber's Knife Collection** | https://dasfreak.github.io/Backstabbers-Knife-Collection/ | Curated dataset of real malicious OSS packages observed since 2015 across npm, PyPI, RubyGems and others | Package archives + metadata | **NO OPEN LICENSE — gated access.** Requires emailing `ohm[at]cs.uni-bonn.de` from an *institutional* address with research objectives and GitHub institutional identity; public email providers refused. Access limited to "verified security research and academic evaluation purposes." | Not published on the landing page | Cite the paper and the taxonomy of attack vectors as a source of *factor-fact vocabulary* (install-hook execution, typosquatting, dependency confusion). Do not attempt to vendor. | **REFERENCE-ONLY** (gated, non-redistributable) |
| **OpenSSF Scorecard** | https://github.com/ossf/scorecard | 16+ default checks (Binary-Artifacts, Branch-Protection, CI-Tests, Code-Review, Dependency-Update-Tool, Fuzzing, Maintained, Pinned-Dependencies, SAST, Security-Policy, Signed-Releases, Token-Permissions, Vulnerabilities …), each scored 0–10 | Go; text/JSON output | **Code: Apache-2.0. REST API data: CDLA-Permissive-2.0** (both stated in repo) | Weekly scan of ~1M critical OSS projects; public BigQuery dataset `openssf:scorecardcron.scorecard-v2`, latest view `scorecard-v2_latest` (weekly-scan scores omit CI-Tests, Contributors, Dependency-Update-Tool) | An enormous, ready-made population of *real* boolean/graded factor facts about delivery pipelines. Sample repositories from BigQuery, threshold the check scores into booleans, and you have realistic fact patterns to attach to synthetic cases. The 0–10 per-check score is also a precedent for graded rather than boolean dispositions. | **VENDOR** (Apache-2.0 code; CDLA-Permissive-2.0 for API data — attribution-light but confirm the specific export you use) |
| **OpenSSF Best Practices badge** | https://www.bestpractices.dev | Criteria set (passing/silver/gold) with per-criterion IDs and self-attestation records for thousands of projects | Web + JSON API | **UNVERIFIED** (project code is MIT; criteria and project data terms not separately verified in this pass) | Thousands of enrolled projects | The passing/silver/gold tiering with stable criterion IDs is another graded-disposition precedent. | **REFERENCE-ONLY until license confirmed** |

---

## 4. SBOM and license-compliance data

| Source | URL | Contents | Format | Verified license | Volume | Reuse | Vendor? |
|---|---|---|---|---|---|---|---|
| **SPDX license-list-data** | https://github.com/spdx/license-list-data | Machine-readable SPDX License List: `licenses.json`, `exceptions.json`, per-license JSON, JSON-LD, RDFa, RDF (NT/Turtle/XML), HTML, text. (No YAML.) | JSON / JSON-LD / RDF / HTML / text | **UNVERIFIED — DO NOT ASSUME.** The repo has **no LICENSE file** (probed `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` — all 404) and GitHub reports `spdx_id: NOASSERTION`. The README defers licensing to license-list-XML, which also has no readable LICENSE file. **Legal review required before vendoring.** | Full SPDX list (count not verified in this pass) | Canonical license identifiers are the natural vocabulary for a `license_is_spdx_approved` / `license_is_copyleft` factor fact. Given the licensing ambiguity, prefer ScanCode LicenseDB below as the vendored source and use SPDX IDs as *identifiers only* (identifiers are facts, not creative content). | **REFERENCE-ONLY pending legal review** |
| **SPDX license-list-XML** | https://github.com/spdx/license-list-XML | Authoritative XML source plus a `test/` directory of test text files and a `schema/` directory | XML | **UNVERIFIED** (same as above; README warns the XML format "is internal to the SPDX legal team and is subject to change") | — | The `test/` directory of license *text variants* that must match each license template is a genuinely useful precedent: it is a matching-tolerance test suite (does this text still count as that license?). Analogous to "does this pipeline configuration still satisfy this provision?" | **REFERENCE-ONLY** |
| **ScanCode LicenseDB** | https://scancode-licensedb.aboutcode.org · https://github.com/nexB/scancode-licensedb | Free database of "mostly all" software licenses; index + per-license records; includes all SPDX and OSI licenses plus a broader curated set; updated daily | JSON API, YAML API, plain-text license texts, web UI, git history | **CC-BY-4.0 AND Apache-2.0** — data under CC-BY-4.0, software under Apache-2.0 (both stated) | **2,000+ curated license texts with metadata** | The vendorable license-metadata source, with an unambiguous license. Use for `license_*` factor facts and for a provision family covering license obligations in the veterinary pipeline. | **VENDOR** (CC-BY-4.0 attribution required) |
| **OSI license metadata** | https://opensource.org/licenses | ~180+ OSI-approved licenses with statuses (approved, Superseded, Voluntarily retired, Redundant with more popular) | Web table | **Site content CC-BY-4.0** ("The content on this website, of which Opensource.org is the author, is licensed under a Creative Commons Attribution 4.0 International License") — but note this covers OSI-authored site content, not third-party license texts, and **no machine-readable API was found** on the licenses page | ~180+ licenses | The *status* taxonomy (approved / superseded / retired / redundant) is a good precedent for provision lifecycle states in a constitution that evolves — superseded provisions must remain addressable so historical cases stay valid. | **REFERENCE-ONLY** (no clean machine-readable export located) |
| **SPDX examples** | https://github.com/spdx/spdx-examples | Example SPDX documents organized by profile: AI, Dataset, Hardware, **Regulatory Conformance**, Software | Multiple SPDX serializations | **Documents: CC0-1.0. Source code: GPL-3.0-or-later. Documentation: CC-BY-4.0** (all stated) | 217 commits; profile-organized example set | The SPDX 3 **Regulatory Conformance profile** is directly on-point: it is an existing attempt to express regulatory conformance claims in an SBOM. The CC0 documents are freely vendorable as fixtures. **Watch the GPL-3.0-or-later on the code** — do not mix the tooling into a permissively licensed corpus repo. | **VENDOR the CC0 documents; avoid the GPL-3.0 code** |
| **CycloneDX sbom-examples** | https://github.com/CycloneDX/sbom-examples | Real-world example BOMs across SBOM, CBOM (cryptography), HBOM (hardware), OBOM (operations), SaaSBOM, VDR, VEX | JSON / XML CycloneDX | **CC0-1.0** | 127 commits; 238 stars; examples drawn from various OSS projects, conforming to the latest CycloneDX spec | CC0 makes this the cleanest vendorable SBOM fixture set. VEX documents in particular are a precedent for *adjudicated* statements: a VEX record says "this vulnerability is/isn't exploitable here, and here is the justification" — structurally identical to a case disposition with reasoning. | **VENDOR** (CC0) |
| **cyclonedx-core-java** | https://github.com/CycloneDX/cyclonedx-core-java | Reference Java library including schema validation | Java | **Apache-2.0** (repo footer) | 1,789 commits | Valid/invalid document test resources were not confirmed in this pass; treat as unverified for fixture-mining purposes. | **REFERENCE-ONLY** (unconfirmed test resources) |

---

## 5. Conformance-suite design precedent

| Suite | URL | What it does | Verified license | Volume | Conventions worth copying |
|---|---|---|---|---|---|
| **ECMAScript test262** | https://github.com/tc39/test262 | Official conformance suite for ECMA-262/402/404 | **BSD (3-clause style), Ecma International** — verified from LICENSE; non-Ecma-member contributors must sign the Test262 CLA | **>50,000 individual test files** (as of May 2025) | Every test carries a **YAML frontmatter metadata block**: `esid` (the spec clause the test targets), `description`, `info` (verbatim spec quote), `negative: {phase, type}` (**declares the test must fail, and at which phase, with which error class**), `flags`, `features`, `includes`. This is the single richest per-test metadata model available and maps almost field-for-field onto our needs: `esid` → `provisions_engaged`, `negative` → `expected_disposition: VIOLATION` with a violation *type*, `features` → factor facts, `flags` → execution modes. |
| **web-platform-tests (WPT)** | https://github.com/web-platform-tests/wpt | Cross-browser conformance across WHATWG/W3C specs | **The 3-Clause BSD License** — verified verbatim from LICENSE.md | 74,089 commits; tens of thousands of tests across `dom/`, `css/`, `fetch/`, etc. | Four test *kinds* (testharness.js, reftests, wdspec, manual) coexisting in one suite with a generated `MANIFEST.json` for discovery. **Test identity is the URL path** — stable, hierarchical, human-readable, and dereferenceable. Copy that: our case IDs should be paths, not opaque integers. |
| **wptrunner metadata (`.ini`)** | https://chromium.googlesource.com/chromium/src/+/refs/tags/112.0.5590.0/docs/testing/web_platform_tests_wptrunner.md | Expected-result files layered over WPT | (part of Chromium/WPT tooling) | — | The **expectation file is separate from the test**. `[test-id.html]` sections with nested `[Subtest name]` sections, `expected: FAIL`, lists of acceptable outcomes `expected: [PASS, FAIL]` for flaky cases, and **conditional expectations** in Python-like syntax (`if os == "linux": FAIL`, `if product == "chrome": [FAIL, PASS]`) keyed on `os`, `version`, `product`, `processor`, `flag_specific`, `debug`. `__dir__.ini` applies directory-wide defaults with nearest-file-wins precedence. `blink_tool.py update-metadata` regenerates expectations from CI. **This is the model for jurisdiction/version-conditional dispositions** — the same case can have a different expected disposition under a different constitutional revision or a different implementing organization. |
| **JSON Schema Test Suite** | https://github.com/json-schema-org/JSON-Schema-Test-Suite | Cross-implementation validator conformance | **MIT** | ~1,490 commits; tests for Draft-2020-12, 2019-09, 07, 06, 04, 03 | The minimal, near-perfect shape: a file is an array of `{description, schema, tests: [{description, data, valid: bool}]}`. **Directory-per-spec-version with a `latest/` symlink** is exactly how to version a constitution while keeping older cases runnable. `optional/` segregates non-mandatory tests (so a partial implementation can still claim conformance on the mandatory core), and `proposals/` holds tests for provisions not yet enacted. Self-check invariants: all schemas are valid, all files are valid JSON. |
| **sqllogictest** | https://www.sqlite.org/sqllogictest/doc/trunk/about.wiki | Cross-engine SQL correctness | **UNVERIFIED** — no license/public-domain statement in the documentation page (SQLite core is public domain, but that does not automatically extend to this sub-project). Verify before vendoring. | **Millions of test vectors**, machine-generated | Line-oriented records: `statement ok` / `statement error` (declared polarity), `query <type-string> <sort-mode> <label>` where type-string is one char per column (`T`/`I`/`R`) and sort-mode is `nosort`/`rowsort`/`valuesort`. **`hash-threshold N`**: results longer than N are stored as an MD5 hash instead of verbatim — a compact way to pin large expected outputs (recommended 10–20 in production, 0 while debugging). **`skipif <db>` / `onlyif <db>` prefixes** are the cleanest known applicability mechanism: a case declares which implementations it applies to, and skipped queries still participate in label validation. The optional **`label`** stores a hash so that *logically equivalent* cases can be asserted to produce identical results — directly useful for "these two fact patterns must reach the same disposition," i.e. precedent consistency. |
| **Jakarta EE TCK process** | https://jakarta.ee/committees/specification/tckprocess/ | Certification process for Jakarta EE implementations | **Dual: an EPL/Apache-licensed open-source build for unofficial testing, and an EFTL-licensed final candidate** required for compatibility claims and brand use | — | **Exclude lists** are a formal artifact, reconsidered at every major release. **TCK challenges**: an implementer may challenge a test as conflicting with the spec or imposing non-portable requirements; challenges cite spec sections, test coordinates and TCK version, are filed with a `challenge` label, and resolve in ≤2 weeks — accepted challenges immediately exclude the test, rejected ones are marked `invalid`. A separate **`challenge-appeal`** path reviews *due process only*, not technical merit. **This is the governance model a Digital Judiciary needs**: a corpus that adjudicates must have a documented route for disputing a case's expected disposition, and a distinction between appealing the outcome and appealing the procedure. Certification requires publishing results (total run / total passed) without a paywall, plus a SHA-256 fingerprint of the exact TCK version. |
| **Bean Validation TCK** | https://docs.hibernate.org/beanvalidation/tck/2.0/reference/html_single/ | Reference TCK implementation | **Apache License 2.0** ("The Jakarta Bean Validation TCK is provided under the Apache Public License 2.0") | — | **The best assertion-traceability model found.** `tck-audit.xml` is a master inventory of every assertion extracted from the specification, organized hierarchically by section and paragraph. Assertion IDs combine a section identifier with a paragraph letter (e.g. `CONSTRAINTSDEFINITIONIMPLEMENTATION_CONSTRAINTDEFINITION_PROPERTIES_MESSAGE` + `"a"`). Tests carry `@SpecAssertion(section=…, id=…)`, **repeatable** so one test can cover several assertions. A generated coverage report classifies every assertion as **Covered / Not covered / Unimplemented / Untestable**. Copy all of it: extract the constitution into an audit file of atomic provisions, tag each case with the provisions it engages, and publish a provision-coverage report with an explicit "untestable" category. |
| **sigstore-conformance** | https://github.com/sigstore/sigstore-conformance | Sigstore client conformance | **Apache-2.0** | 257 commits, 29 releases | `must_pass` / `must_fail` helpers force declared polarity; **`xfail` glob patterns** whitelist known failures for optional features. Explicitly workflow-focused rather than coverage- or fuzz-driven. |
| **Mutation testing — PIT** | https://pitest.org/quickstart/mutators/ | Java mutation testing | **Website content: CC BY-NC-SA 3.0** (stated on pitest.org). The PIT *code* license was not verified in this pass — **do not copy mutator descriptions verbatim** (NC clause). | ~30 mutators | Mutator catalogue as a template for **negative-control generation**: Conditionals Boundary, Increments, Invert Negatives, Math, Negate Conditionals, Void Method Calls, Empty/False/True/Null/Primitive Returns (defaults); Constructor Calls, Inline Constants, Non-Void Method Calls, Remove Conditionals, Remove Increments (optional); plus experimental operators. Mutators are grouped into named tiers: `OLD_DEFAULTS`, `DEFAULTS`, `STRONGER`, `ALL`. **Adopt the tiering idea for mutation strength of negative cases.** |
| **Mutation testing — Stryker** | https://github.com/stryker-mutator/stryker-js · https://github.com/stryker-mutator/mutation-testing-elements | JS mutation testing + a standard report schema | **Apache-2.0** (both repos) | — | `mutation-testing-report-schema` is a **published JSON schema for mutation results**, decoupled from any one tool, with synchronized versioning and a stated backward-compatibility policy. That decoupling is the lesson: publish the *corpus result schema* as a versioned artifact independent of the runner, so third parties can report conformance in a comparable form. |
| **mutmut** | https://pypi.org/project/mutmut/ | Python mutation testing | **BSD-3-Clause** (PyPI metadata) | — | Same negative-control-generation role for Python. Specific status vocabulary not confirmed in this pass. |
| **OpenAPI Specification** | https://github.com/OAI/OpenAPI-Specification | Spec sources; a `tests/` directory exists | **Apache-2.0** | — | Contents of `tests/` not verified; treat as a lead, not a confirmed corpus. |

---

## 6. AI-governance / constitutional-conformance material (closest analogues)

| Source | URL | Contents | Format | Verified license | Volume | Reuse | Vendor? |
|---|---|---|---|---|---|---|---|
| **OpenAI Model Spec** | https://github.com/openai/model_spec | The spec itself (`model_spec.md`), plus archived rendered HTML versions from 2025-02-12 onward | Markdown + HTML | **CC0-1.0** — "dedicated to the public domain and marked with the Creative Commons CC0 1.0 deed" | Versioned releases (2025-02-12, 2025-10-27, 2025-12-18, 2026-08-18 …) | **This is a constitution with stable clause IDs, dated revisions, and a public-domain dedication.** Study how it numbers and nests provisions, how examples of compliant vs. non-compliant behavior sit inline with the provision text, and how revisions are archived so older cases remain interpretable. | **VENDOR** (CC0) |
| **OpenAI Model Spec dataset** | https://github.com/openai/model_spec_dataset | "A public-domain dataset of prompts and scenarios for evaluating compliance with the OpenAI Model Spec" (as of the 2025-12-18 spec) | JSON in a `dataset/` folder | **CC0-1.0** | **596 prompts** (9 marked `skip` because they need system-message control unavailable via the public API) | **The single closest structural match to the target corpus.** Per-record fields: `target` (the rubric defining compliance — i.e. the expected disposition, expressed as a rubric rather than a boolean), **`focus_id`** (the specific focus area of the spec engaged), **`section_id`** (immediate containing section), **`sections`** (the full hierarchical chain of containing sections — a materialized provision ancestry path), and **`skip`** (technical exclusion flag with a stated reason). Map directly: `case_id` ← record key, `provisions_engaged` ← `focus_id` + `sections`, factor facts ← the scenario prompt (ours are boolean rather than free text), `expected_disposition` ← `target`. CC0 means the *schema and the cases* can both be lifted. | **VENDOR** (CC0) |
| **OpenAI Model Spec evals** | https://github.com/openai/model_spec_evals | Harness: filters by `section_filter` (e.g. `chain_of_command`, `avoid_errors`) and `focus_filter` (e.g. `8ep1`, `adau`); model-based grading — grader sampled 5× per response, median taken; reports compliance rate per top-level section (`style`, `chain_of_command`, `best_work`, `seek_truth`, `stay_in_bounds`, `all`) | Python | **MIT** | ~587 runnable samples | Copy the **roll-up-by-top-level-section reporting** and the **short opaque focus IDs** (`8ep1`, `adau`) paired with human-readable section names. Also copy the median-of-N grading discipline where dispositions are judgment calls rather than mechanical. | **VENDOR** |
| **Bloom (Anthropic / safety-research)** | https://github.com/safety-research/bloom | Generates evaluation suites for a named behavior: builds diverse scenarios, runs conversations, scores results (sycophancy, self-preservation, political bias, etc.); behavior definitions in `bloom-data/behaviors.json` with `behavior.name` and optional `behavior.examples` (seed transcripts), plus required variation-dimension descriptions | JSON + Python | **MIT** | Bundled behavior set | Precedent for **generating** a case corpus from a provision plus a handful of seed examples and a set of declared *variation dimensions*. Our variation dimensions are the boolean factor facts — the combinatorial cross-product of factors is exactly what Bloom formalizes. Strong candidate for bootstrapping corpus volume. | **VENDOR** |
| **EU AI Act (Regulation 2024/1689) text** | eur-lex.europa.eu | The regulation itself, article/recital numbered | HTML/PDF | EUR-Lex reuse policy (© European Union; reuse generally permitted with source acknowledgement) — **verify the current EUR-Lex legal notice before vendoring** | 113 articles + annexes | Article/paragraph/point numbering is the reference model for a citable provision identifier space in a legal register. | **REFERENCE-ONLY pending EUR-Lex notice check** |

---

## 7. License summary (safe-to-vendor vs reference-only)

### Safe to VENDOR (license verified, permissive)

| Source | License | Obligation |
|---|---|---|
| openai/model_spec + model_spec_dataset | CC0-1.0 | none |
| NIST OSCAL-content | US public domain + CC0-1.0 | none |
| CycloneDX/sbom-examples | CC0-1.0 | none |
| spdx/spdx-examples (documents only) | CC0-1.0 | none; **exclude the GPL-3.0-or-later code** |
| openai/model_spec_evals | MIT | notice |
| safety-research/bloom | MIT | notice |
| JSON-Schema-Test-Suite | MIT | notice |
| ComplianceAsCode/content | BSD-3-Clause | notice + no-endorsement |
| web-platform-tests/wpt | BSD-3-Clause | notice + no-endorsement |
| tc39/test262 | BSD (Ecma) | notice + no-endorsement; CLA to *contribute* |
| mutmut | BSD-3-Clause | notice |
| gatekeeper-library, kyverno/policies, kyverno-json, cedar-integration-tests, in-toto/attestation, sigstore-conformance, slsa-verifier, ossf/malicious-packages, ossf/scorecard (code), compl-ai, stryker/mutation-testing-elements, OpenAPI-Specification, Bean Validation TCK | Apache-2.0 | notice + NOTICE file + change statement |
| ScanCode LicenseDB (data) | CC-BY-4.0 | attribution |
| ai-act-evaluation-benchmark (data) | CC-BY-4.0 (code Apache-2.0) | attribution |
| OpenSSF Scorecard REST API data | CDLA-Permissive-2.0 | light attribution; confirm per-export |

### REFERENCE-ONLY

| Source | Reason |
|---|---|
| SPDX license-list-data / license-list-XML | **No LICENSE file; GitHub reports NOASSERTION.** Legal review required. Use SPDX *identifiers* (facts) only. |
| Conftest | License type not confirmed by this pass. |
| OpenSSF Best Practices criteria/data | License not confirmed by this pass. |
| sqllogictest | No license/public-domain statement located; SQLite core's public-domain status does not automatically extend. |
| SLSA spec text | Dual CSL-1.0 / Apache-2.0; mixed obligations. Concepts reusable, text is not clean. |
| PIT website mutator docs | CC BY-**NC**-SA 3.0 — non-commercial clause. Do not copy text. |
| CIS Benchmarks (PDFs) | CIS terms of use, not an OSI license. |
| ISO/IEC 42001 | Paywalled, proprietary. |
| Backstabber's Knife Collection | Gated institutional access, non-redistributable. |
| cedar-spec | Not separately verified. |
| EU AI Act text | Verify current EUR-Lex reuse notice. |
| OSI license page | CC-BY-4.0 site content but no machine-readable export located. |
| cyclonedx-core-java test resources | Existence/shape unconfirmed. |

---

## 8. Recommended corpus schema, synthesized

Drawing the verified conventions together:

```yaml
# cases/supply-chain/provenance/unsigned-build-artifact.case.yaml
id: vetpoc/supply-chain/provenance/unsigned-build-artifact   # WPT: path-shaped, dereferenceable
schema_version: 1                                            # mutation-testing-elements: versioned independently
constitution_version: "2026-09-01"                           # JSON Schema Test Suite: dir-per-version

provisions_engaged:                                          # Bean Validation TCK @SpecAssertion (repeatable)
  - id: DJ-SUPPLY-3.2
    paragraph: b
  - id: DJ-SUPPLY-4.1
    paragraph: a
sections: [supply_chain, provenance, signing]                # model_spec_dataset: ancestry chain

description: "Release artifact published with no in-toto provenance attestation."
info: |                                                      # test262: verbatim provision quote
  DJ-SUPPLY-3.2(b): "Every artifact promoted to a production veterinary
  environment SHALL carry a verifiable provenance attestation."

facts:                                                       # boolean factor facts
  artifact_signed: false
  provenance_present: false
  builder_id_matches: false
  sbom_present: true
  dependency_known_malicious: false

expected:
  disposition: VIOLATION                                     # sigstore: declared polarity
  reason: [DJ-SUPPLY-3.2]                                    # Cedar `reason`: WHICH provisions fired
  severity: 2                                                # gator: exact violation count / grade

applicability:                                               # sqllogictest skipif/onlyif
  onlyif: [jurisdiction/eu, jurisdiction/us-fda]
conditional_expected:                                        # wptrunner conditional expectations
  - if: jurisdiction == "us-fda" and constitution_version < "2026-06"
    disposition: CAUTION

negative_control_of: vetpoc/supply-chain/provenance/signed-build-artifact
mutation_tier: DEFAULTS                                      # PIT tiering
tags: [optional]                                             # JSON Schema Test Suite optional/
skip: null                                                   # model_spec_dataset: reason string or null
```

Expected-fail lists live **outside** the case files, in wptrunner-style layered `.ini`/YAML keyed by
glob over case IDs (sigstore `xfail` patterns), so an implementer can declare known gaps without
editing the corpus.

---

## 9. Open items

- Obtain a definitive license determination for the SPDX license list data and license-list-XML.
- Confirm Conftest's and OpenSSF Best Practices' licenses.
- Locate a license statement for sqllogictest, or re-derive the format from the public documentation
  (which is fine — formats are not copyrightable) without copying the corpus.
- Read `scripts/get_corpus_stats.py` output to get the actual Cedar corpus case count.
- Pull the malicious-packages stats JSON/CSV for per-ecosystem report counts.
- Verify whether `CycloneDX/cyclonedx-core-java` ships valid/invalid document fixtures.
- Check EUR-Lex's current reuse notice for the EU AI Act text.
