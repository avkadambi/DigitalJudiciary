# Lane 01 — Observability & Datacenter Telemetry Standards: Reusable Conformance Corpora

**Scope:** open-source test data, conformance suites and test fixtures from the observability /
datacenter-telemetry world, assessed for reuse inside an open compliance test corpus whose unit of
work is a **case** = `(case_id, provisions_engaged, boolean factor facts, expected_disposition)`.

**Target system under governance:** multi-tenant datacenter monitoring / observability / AIOps platform —
BMS + sensor-gateway telemetry ingestion, thermal & capacity analytics, alerting and escalation, an
automated remediation advisor, customer-deployed edge collectors, badge/access security telemetry, a
customer portal.

**Out of scope (covered by a prior survey, not re-derived here):** SLSA, in-toto, sigstore, SPDX,
CycloneDX, OSV, OpenSSF Scorecard, OSPS Baseline, CWE, general AppSec corpora.

**Verification method:** every licence below was read from the repository's own LICENSE file, the
licence badge on the repository landing page, or the publisher's own copyright policy page, fetched
during this research pass on 2026-09-05. Where a licence could **not** be verified from a primary
source it is recorded as `UNVERIFIED` — no licence in this document is inferred or guessed.

---

## 0. Executive framing — why these matter for a *change-governance* corpus

Three of the sources below are already, structurally, exactly what this corpus needs:

1. **`promtool` unit-test files** are a native `(input series, expected alert disposition)` format.
   An alerting-rule test is literally: given these boolean/numeric facts over time, the expected
   disposition is "alert X fires with these labels" or "no alert". This maps 1:1 onto a case.
2. **BPF verifier selftests** are a native `(program, expected verdict, expected reason string)`
   corpus. `__success` / `__failure` + `__msg("...")` is an expected-disposition plus a
   machine-readable *ratio decidendi*. This is the single closest analogue in open source to a
   corpus of adjudicated cases with stated grounds.
3. **Redfish interoperability profiles** are a native deontic vocabulary —
   `Mandatory / Recommended / IfImplemented / Supported / Excluded` — evaluated per-property
   against a live service to produce Pass/Fail/Skip/Warning. That is a provision-engagement model
   with a disposition, already in JSON.

Everything else is either a **factor vocabulary donor** (stable identifiers you can cite instead of
inventing names) or a **fixture donor** (realistic telemetry payloads to hang cases on).

---

## 1. Master source table

Legend for the reuse column:
- **VENDOR** — redistributable inside an Apache-2.0 / CC-BY-4.0 corpus repo, subject to notice.
- **VENDOR\*** — redistributable but with a licence-compatibility caveat spelled out in the row.
- **REFERENCE-ONLY** — cite by URL/version; do not copy content into the repo.

### 1.1 OpenTelemetry

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 1 | OpenTelemetry Specification | https://github.com/open-telemetry/opentelemetry-specification | Cross-language normative requirements for API/SDK/OTLP; `/specification`, `/oteps`, `/schemas` | Markdown | **Apache-2.0** (repo LICENSE / repo landing page) | 2,503 commits; spec v1.58.0-era | No per-case verdicts; MUST/SHOULD normative statements | Source of **provision text**. Each MUST/SHOULD becomes a provision id (e.g. `otel-spec/trace/span-processor/on-ending`). Quote verbatim under Apache-2.0 with notice. | **VENDOR** |
| 2 | OTel Spec Compliance Matrix | https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md | Feature × language implementation matrix. Rows = spec features ("Create TracerProvider", "Get a Tracer with schema_url", "SpanProcessor.OnEnding", "Metric Exporter configurable temporality preference", "Concurrent sending"); columns = Go, Java, JS, Python, Ruby, Erlang, PHP, Rust, C++, .NET, Swift, Kotlin. Symbols: `+` supported, `-` not supported, `N/A` not applicable, blank = unknown; an `X` in the **Optional** column marks the feature optional, blank = required | Markdown table | **Apache-2.0** | ~12 language columns × several hundred feature rows | **Yes** — per-(feature, implementation) supported/not-supported, plus a required-vs-optional axis | This is a **provision-engagement matrix in the wild**. The Optional column is a *deontic modality* marker: required vs optional. Convert each row to a provision with `modality ∈ {required, optional}`, each cell to a case with `expected_disposition ∈ {conformant, non-conformant, not-applicable, undetermined}`. The `blank = unknown` cell is a genuine **non liquet** exemplar — valuable, because most synthetic corpora forget that a corpus must be able to say "undetermined". | **VENDOR** |
| 3 | OTel Semantic Conventions | https://github.com/open-telemetry/semantic-conventions | `model/` YAML attribute & metric definitions; `docs/` generated registry; `schemas/` | YAML + Markdown | **Apache-2.0** (repo landing page) | Registry v1.43.0, aligned to spec v1.58.0; thousands of attributes | Stability level per attribute is the ground truth (Stable / Release Candidate / Alpha / Development / Deprecated) | **Primary factor-vocabulary donor.** Use attribute names verbatim as factor identifiers so the corpus is citable rather than bespoke. Stability level itself is a usable factor (`attribute.stability == stable`). | **VENDOR** |
| 4 | OTel attribute-naming & stability rules | https://opentelemetry.io/docs/specs/semconv/general/attribute-naming/ and https://opentelemetry.io/docs/specs/otel/versioning-and-stability/ | Naming rules + stability guarantees | Markdown | **Apache-2.0** (opentelemetry.io content, same project licence) | 2 documents | Normative rules, no cases | **Important verified caveat:** OTel defines Development / Stable / Deprecated. Stable = backward-incompatible change requires a major version bump. The naming doc states "Two attributes, two metrics, or two events MUST NOT share the same name" and that conventions "SHOULD NOT be removed … SHOULD be deprecated". So **stable semconv attribute names are safe as long-lived citable identifiers; Development ones are not.** Pin the semconv version in every case. | **VENDOR** |
| 5 | OTel Weaver | https://github.com/open-telemetry/weaver | Registry validation, schema diffing, codegen, **live-check** of an OTLP stream against a semconv registry; embeds Open Policy Agent (Rego) for custom rules | Rust tool + Rego policies + JSON report | **Apache-2.0** (repo landing page) | 1 tool; ~1.4% of repo is Rego policy | **Yes** — emits `PolicyFinding` records with a machine-readable `id` and a severity | **Highest-value structural donor after promtool.** Weaver's finding model is `(sample entity, advice type id, level)` where level ∈ `violation` / `improvement` / `information` and `violation` drives a non-zero exit code. That is a graded disposition ladder. Reuse the advice-type ids as factor names (see §2.3). Weaver can also be *run* over your platform's own telemetry to auto-generate cases. | **VENDOR** |
| 6 | opentelemetry-proto (OTLP) | https://github.com/open-telemetry/opentelemetry-proto | OTLP protobuf definitions for traces/metrics/logs/profiles; `examples/` folder incl. OTLP/JSON wire representations | Protobuf + JSON | **Apache-2.0** (repo landing page) | Core signals (common, resource, metrics, trace, logs) marked **Stable** in binary and JSON; profiles **Development** | Stability guarantee is explicit: "Field types, numbers and names will not change" for Stable components | Use OTLP/JSON example payloads as the **fixture substrate** for cases about ingestion, redaction and tenant isolation. Because the Stable guarantee is written down, an OTLP field name is a durable factor identifier. | **VENDOR** |
| 7 | opentelemetry-collector | https://github.com/open-telemetry/opentelemetry-collector | Core collector; `testdata` golden files, `pdatatest`, `internal/testutil`; implements OTLP v1.10.0 | Go + YAML + golden files | **Apache-2.0** (repo landing page) | 22k+ commits across core+contrib | Golden-file comparisons = expected outputs | Golden-file pattern is directly transferable: a case's expected disposition can be a golden pdata document. Also the component **stability ladder** (development/alpha/beta/stable/unmaintained/deprecated) is a governance vocabulary you can cite for "what maturity may be deployed to production". | **VENDOR** |
| 8 | Collector-contrib **redactionprocessor** | https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/redactionprocessor | PII/secret redaction in attributes and log bodies | Go + YAML config | **Apache-2.0** (contrib repo landing page) | 1 component | Emits **audit summary attributes** that are literally a disposition record | **The single best fit for the badge/access + tenant-PII part of the platform.** Its config keys are a ready deontic vocabulary (allow / ignore / block) and its summary attributes are a machine-readable record of what was redacted. See §2.4. | **VENDOR** |
| 9 | Collector-contrib **attributesprocessor** | https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/attributesprocessor | Attribute mutation | Go + YAML | **Apache-2.0** | 1 component | No | Seven verbs — `insert`, `update`, `upsert`, `delete`, `hash`, `extract`, `convert` — are a compact controlled vocabulary for "what a change did to telemetry". Use as the action taxonomy in change cases. | **VENDOR** |
| 10 | Collector-contrib **transformprocessor** / OTTL | https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/transformprocessor | OTTL statements over contexts `resource, scope, span, spanevent, metric, datapoint, exemplar, log, profile`; functions incl. `set`, `delete_key`, `delete_matching_keys`, `keep_keys`, `replace_pattern`, `replace_all_patterns`, `truncate_all`, `limit`, `SHA256`, `Hash`; config `error_mode` ∈ `ignore`/`silent`/`propagate`, plus `trace_statements`, `metric_statements`, `log_statements`, `conditions`, `flatten_data` | Go + OTTL DSL | **Apache-2.0** | 1 component | No | `error_mode` is a **remediation-posture factor** (does a failed transform drop the payload, log, or pass silently?) — directly relevant to the automated remediation advisor's fail-safe/fail-open governance. | **VENDOR** |

### 1.2 Prometheus / OpenMetrics

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 11 | **promtool unit tests for rules** | https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/ | The native Prometheus format for testing recording **and alerting** rules | YAML | **Apache-2.0** (Prometheus project) | Format spec + examples; every Prometheus user's rule tests | **Yes — this IS an (input, expected disposition) format** | **Top pick.** Adopt the schema wholesale as the serialisation for alerting/escalation cases. Field names in §2.5. `input_series` = the factor facts; `exp_alerts` (with `exp_labels`, `exp_annotations`) = the expected disposition; `rule_files` = the provisions engaged; `name` = the case id. Zero impedance mismatch. | **VENDOR** |
| 12 | prometheus/compliance — **remote-write sender tester** | https://github.com/prometheus/compliance (`remotewrite/sender`) | Conformance tests for the sender half of Prometheus Remote Write | Go | **Apache-2.0** (repo file listing) | **18 named test scenarios** | **Yes, with published per-implementation scores** | The 18 test names are a compact provision set; the published scores are adjudicated outcomes. See §2.6. | **VENDOR** |
| 13 | Published remote-write compliance results | https://prometheus.io/blog/2021/05/04/prometheus-conformance-remote-write-compliance/ | Per-sender pass scores: Grafana Agent 0.13.1 = 100%, Prometheus 2.26.0 = 100%, VictoriaMetrics Agent 1.59.0 = 76%, Telegraf 1.18.2 = 65%, OpenTelemetry Collector 0.26.0 = 41%, Timber Vector 0.13.1 = 35% | HTML table | **Apache-2.0 / CC-BY-4.0** — Prometheus website content; **UNVERIFIED for the blog post specifically**, treat as REFERENCE-ONLY until the site licence is read | 6 implementations × 18 tests | **Yes — real published verdicts** | Gold-standard exemplar of "a conformance corpus that publishes pass/fail per implementation, by version". Cite the methodology and the shape; do not copy the table without checking the site licence. | **REFERENCE-ONLY** |
| 14 | prometheus/compliance — **PromQL tester** | https://github.com/prometheus/compliance/tree/main/promql | Runs identical queries against reference Prometheus and a vendor implementation, compares results. `promql-test-queries.yml` = the standard suite; `test-<vendor>.yml` = per-vendor target config and query tweaks. Output text/HTML/**JSON**. Exit 0 = compliant, 1 = failure | Go + YAML + JSON | **Apache-2.0** | Reported runs of **529 test queries** ("529 / 529 (100.00%) passed, 0 unsupported") | **Yes** — per-query pass / fail / **unsupported** | The **`unsupported` third outcome** is important: it is neither pass nor fail. Adopt it as a disposition value alongside conformant / non-conformant / not-applicable. Results published 2020-08-06 and 2020-12-01 at promlabs.com/promql-compliance-tests. | **VENDOR** (code+queries); results page REFERENCE-ONLY |
| 15 | prometheus/compliance — **alert_generator** | https://github.com/prometheus/compliance/tree/main/alert_generator | Tests whether an implementation generates and sends alerts to Alertmanager per Prometheus semantics. Config-driven (`test-example.yaml`); pluggable `alert_message_parsers.go` for vendor alert formats. Run takes ~40 min; success prints `Congrats! All tests passed` | Go + YAML | **Apache-2.0** | 1 suite | **Yes** — binary pass/fail with failure descriptions | Directly relevant to the alerting-and-escalation subsystem. Its "pluggable parser per vendor alert format" idea is worth stealing: a corpus case should be able to declare *how* the system-under-test's output is normalised before comparison. | **VENDOR** |
| 16 | OpenMetrics specification | https://github.com/OpenObservability/OpenMetrics | The exposition-format standard; now **moved to the Prometheus project**, with OpenMetrics 2.0 in progress. Repo dirs: `proto`, `specification`, `tests`, `src`, `website`, `legacy` | Markdown + protobuf | **Apache-2.0** — verified from the repo's own LICENSE file (Apache License Version 2.0, January 2004). *Caveat:* the specification markdown is formatted as an IETF Internet-Draft (`draft-richih-opsawg-openmetrics-01`) carrying the IETF **trust200902** IPR boilerplate. The repo LICENSE is Apache-2.0; the I-D boilerplate is a second, narrower grant on the same text. **Legal review recommended before vendoring the spec markdown verbatim**; the surrounding repo is unambiguously Apache-2.0. | 8 metric types, ~2.5k stars | Type/suffix rules are normative | Metric types and required suffixes are a small, exact, citable vocabulary — see §2.7. | **VENDOR\*** (code & tests yes; spec markdown pending review) |
| 17 | OpenMetrics **test suite** (`openmetricstest`) | https://github.com/OpenObservability/OpenMetrics/tree/main/tests and https://pkg.go.dev/github.com/OpenObservability/OpenMetrics/src/cmd/openmetricstest | Directory-based parser conformance harness: **"any directory with `test.json` is a test"**; test type `cmd-parser-text` feeds an OpenMetrics text exposition on stdin to the implementation under test; exit 0 = parsed successfully, non-zero = rejected | JSON manifests + text fixtures | **Apache-2.0** | Directory tree of parse cases | **Yes** — valid/invalid parse cases with expected PASS/FAIL | Beautifully minimal design worth copying: a case is a **directory** containing a manifest plus fixtures, and the harness discovers cases by walking the tree. Adopt this layout for the corpus so cases are addable without touching an index file. | **VENDOR** |
| 18 | avalanche | https://github.com/prometheus-community/avalanche | Load generator producing Prometheus metrics with configurable **series churn** over time; supports scrape and remote-write; used against Thanos, Cortex, M3DB, VictoriaMetrics | Go | **Apache-2.0** (repo landing page) | 1 tool | No expected results — it is a generator | Generate the high-cardinality / churn fixtures for capacity-analytics and ingestion-budget cases. Deterministic-enough load lets a case assert an ingestion budget. | **VENDOR** |

### 1.3 eBPF and kernel safety (edge collectors)

Directly relevant because customer-deployed edge collectors that use eBPF run code inside the
customer's kernel — the highest-consequence change surface on the platform.

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 19 | **BPF verifier selftests** | https://github.com/torvalds/linux/tree/master/tools/testing/selftests/bpf/progs (`verifier_*.c`) | Per-test annotations: `__description("...")`, `__success` / `__failure`, `__msg("<expected verifier message>")`, `__retval(N)`, `__flag(BPF_F_...)`, `__log_level(2)`, and separate unprivileged expectations `__success_unpriv` / `__failure_unpriv` | C with macro annotations | **GPL-2.0** (kernel selftests carry SPDX headers; kselftest docs show `SPDX-License-Identifier: GPL-2.0+`) | Dozens of `verifier_*.c` files, thousands of cases | **Yes — the strongest expected-verdict corpus found in this lane** | **Structural model to imitate, not to vendor.** Note the two-tier expectation (privileged vs unprivileged) — the same program gets *different verdicts under different authority levels*. That is exactly the multi-tenant privilege question this corpus needs to model. Extract the rejection-reason strings as a controlled vocabulary (§2.8); do **not** copy GPL-2.0 C source into an Apache-2.0 repo. | **REFERENCE-ONLY** (GPL-2.0 incompatible with Apache-2.0 redistribution) |
| 20 | BPF selftests harness | https://github.com/torvalds/linux/blob/master/tools/testing/selftests/bpf/README.rst | `test_progs` runner, `vmtest.sh`, per-architecture `DENYLIST.<arch>` files that document *why* a test is excluded on a platform | RST + shell | **GPL-2.0** | 1 harness | Denylists are documented, reasoned exclusions | The **`DENYLIST.<arch>` with a written cause** is an excellent pattern: a corpus needs a first-class way to say "this case does not apply in this environment, and here is the stated reason". Model it as an explicit `not-applicable` disposition carrying a required justification. | **REFERENCE-ONLY** |
| 21 | libbpf | https://github.com/libbpf/libbpf | Mirror of kernel `tools/lib/bpf` | C | **BSD-2-Clause OR LGPL-2.1** — verified dual licence, SPDX `BSD-2-Clause OR LGPL-2.1`; repo states "You can choose between one of them" | Library | No | Under the BSD-2-Clause arm this is **Apache-2.0-compatible** and could be vendored if any fixture required it. Useful mainly as the loader whose error messages the edge collector will surface. | **VENDOR\*** (elect the BSD-2-Clause arm) |
| 22 | bcc | https://github.com/iovisor/bcc | 50+ tracing tools, examples, tests | C/Python/Lua | **Apache-2.0** (repo landing page) | ~88% C, 6.5% Python | No expected-verdict corpus | Source of realistic eBPF programs to use as the *subject* of edge-collector change cases. | **VENDOR** |
| 23 | Linux Test Project (LTP) | https://github.com/linux-test-project/ltp | Kernel reliability/robustness/stability suite maintained by SUSE, Red Hat, Fujitsu, IBM, Cisco, Oracle and others | C + shell | **GPL-2.0 ("or, at your option, any later version")** — verified from the repo COPYING file | Large (thousands of tests) | Result codes per test | Cite as prior art for "what a mature, multi-vendor conformance suite looks like at scale". Not vendorable into Apache-2.0. | **REFERENCE-ONLY** |
| 24 | kselftest | https://docs.kernel.org/dev-tools/kselftest.html | Kernel self-tests under `tools/testing/selftests/`; **output MUST conform to TAP** (Test Anything Protocol); helpers in `kselftest.h` / `kselftest_harness.h` | C + shell, TAP output | **GPL-2.0+** (SPDX headers shown in the kernel docs) | Whole `selftests/` tree | TAP result stream | **Adopt TAP as the corpus's result wire format.** It is a decades-old, tool-agnostic, human-readable pass/fail/skip protocol with a `# SKIP` reason field — an existing, boring, well-supported answer to "how do we emit dispositions". Adopting a format is not copying GPL code. | **REFERENCE-ONLY** (adopt the format, not the code) |

### 1.4 Redfish / DMTF (server, chassis, thermal, power, facility)

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 25 | Redfish Schema Bundle (DSP8010) | https://www.dmtf.org/standards/redfish and https://redfish.dmtf.org/schemas/v1/ | JSON Schema + CSDL for every Redfish resource type, all versions | JSON Schema / CSDL XML | **DMTF copyright policy**, verified at https://www.dmtf.org/about/policies/copyright: *"Members and non-members may reproduce DMTF specifications and documents for uses consistent with this purpose, provided that correct attribution is given."* Each schema file carries: *"Copyright 2014-2026 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright"*. **This is NOT an SPDX/OSI open-source licence** — it is a permissive reproduction grant conditioned on attribution and on use consistent with DMTF's purpose. | Hundreds of resource types, each with many versions (e.g. AccountService v1.0.0–v1.18.1) | Schemas encode required properties, enums, numeric ranges | **Primary factor-vocabulary donor for the hardware/thermal/power domain.** Resource names in §2.2. Redistribution is likely permissible **with attribution**, but because the grant is bespoke rather than SPDX, prefer **referencing schemas by canonical URL + version** in cases and vendoring only a small attributed subset if needed. | **VENDOR\*** — attribution-conditioned, non-SPDX; legal review before bulk vendoring |
| 26 | Redfish **Interop Validator** | https://github.com/DMTF/Redfish-Interop-Validator | Validates a live service against an **interoperability profile**. Produces text and HTML logs with **Pass/Fail/Skip/Warning per resource checked** | Python + JSON profiles | **BSD 3-Clause** — verified from the repo's LICENSE.md; "Copyright 2017-2026 DMTF. All rights reserved." | 1 tool + profile schema | **Yes — per-requirement Pass/Fail/Skip/Warning** | **Best deontic-vocabulary donor in this lane.** `ReadRequirement ∈ {Mandatory, Recommended, IfImplemented, Supported, Excluded}` is a five-valued modality — richer than MUST/SHOULD and closer to what a real compliance corpus needs. `ConditionalRequirements` is native support for provisions that engage only when a trigger condition holds. See §2.9. | **VENDOR** (BSD-3-Clause is Apache-2.0-compatible) |
| 27 | Redfish **Service Validator** | https://github.com/DMTF/Redfish-Service-Validator | Checks a live service against Redfish CSDL schema: resource accessibility, type conformance, required properties, data types, valid values, action support, URI patterns, reference integrity, enum compliance, numeric ranges, **deprecated URI/property/value detection**; GET-only, implementation-agnostic | Python | **BSD 3-Clause** (licence badge on repo landing page) | 1 tool | Errors vs warnings per check | The **error/warning split plus deprecation detection** is a graded-severity model. "Uses a deprecated property" is a distinct disposition from "violates the schema" — worth preserving as separate factors. | **VENDOR** |
| 28 | Redfish **Mockup Server** + public mockups (DSP2043) | https://github.com/DMTF/Redfish-Mockup-Server ; mockups at DMTF "All Published Versions of DSP2043" | Python server that serves any Redfish mockup tree over HTTP; ships a built-in `public-rackmount1` mockup | Python + JSON trees | Server: **BSD 3-Clause** (repo). Mockups (DSP2043): **DMTF copyright policy**, same attribution-conditioned grant as DSP8010 | Server + several published mockup bundles | Mockups are ground-truth-shaped inputs, not verdicts | **The fixture substrate for every BMS/chassis case.** Stand up `public-rackmount1`, point the platform's collectors at it, and each case becomes reproducible without real hardware. Server is safely vendorable; mockups need the attribution caveat. | Server **VENDOR**; mockups **VENDOR\*** |

### 1.5 Building / facility protocols — paywall status (stated plainly)

| # | Name | URL | Access | VERIFIED terms | Verdict |
|---|------|-----|--------|----------------|---------|
| 29 | **BACnet — ASHRAE Standard 135** | https://www.ashrae.org/technical-resources/bookstore/bacnet | **PAYWALLED.** Purchase required via the ASHRAE bookstore / Techstreet. No free read-only version of the standard itself was found. Free adjuncts exist: the "Managed BACnet Guidance, Volume 1: Manufacturer's Guide" (readable online) and the "BACnet Secure Connect" white paper (downloadable). ASHRAE members get ASHRAE Journal access | Commercial standards publishing terms; not open | **REFERENCE-ONLY.** Cite clause numbers; never reproduce text. Object-type and property names may be used as identifiers, but source them from an openly licensed implementation, not from the paywalled standard. |
| 30 | **Modbus** | https://modbus.org/specs.php and https://modbus.org/tech.php | Specifications are downloadable **at no charge but behind a click-through licence agreement** — the site requires reviewing and accepting a licence ("I ACCEPT") before downloading "any MODBUS protocol or related documents". Site carries "Copyright © 2005-2024 Modbus Organization, Inc." Some resources (e.g. the Modbus TCP Toolkit) require corporate membership or purchase | **The full text of the click-through licence agreement could not be read when this survey was compiled.** Recorded as **UNVERIFIED** — no licence assumed | **REFERENCE-ONLY** pending someone actually reading and recording the acceptance terms. Free-of-charge ≠ redistributable. |
| 31 | **SNMP MIBs (IETF RFCs)** — e.g. RFC 3418 SNMPv2-MIB | https://www.rfc-editor.org/rfc/rfc3418.html | **FREE AND PUBLIC** | Verified from the RFC text: "Copyright (C) The Internet Society (2002). All Rights Reserved." The full copyright statement permits copying and derivative works; critically, the **MIB module text specifically** may be copied and distributed *"in whole or in part, without restriction of any kind, provided that the above copyright notice and this paragraph are included on all such copies and derivative works."* The RFC document itself may not be modified except via the Internet Standards process or for translation | **VENDOR** — the MIB modules are the most cleanly redistributable identifier source in the facility layer. Object names in §2.10. |
| 32 | **IPMI v2.0 (Intel)** | https://www.intel.com/content/www/us/en/products/docs/servers/ipmi/ipmi-home.html | Specification PDF is linked for download from Intel's page. **The governing licence/adopter terms are not stated on that page** — recorded as **UNVERIFIED** | Not verified | **REFERENCE-ONLY.** Also note the material governance fact, verified on Intel's page: in **June 2020 the IPMI Promoters (Dell, HPE, NEC, Intel) stated "No further updates to the IPMI specification are planned or should be expected"** and recommended migrating to **DMTF Redfish**. For this corpus that means: build the hardware-management factor vocabulary on **Redfish**, and treat IPMI as legacy/deprecated — which is itself a citable factor (`management_interface.deprecated == true`). |
| 33 | DCIM standards generally | — | No single open DCIM conformance suite was located in this pass. Redfish (§1.4) plus its facility extensions (PowerEquipment, ThermalEquipment, CoolingUnit, CoolingLoop, Outlet, LeakDetection) is the closest thing to an open DCIM data model | See DSP8010 row | Use Redfish as the DCIM model of record. |

### 1.6 TSDB / ingestion benchmarks

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 34 | **TSBS** (Time Series Benchmark Suite) | https://github.com/timescale/tsbs | Go programs that generate datasets and benchmark read/write performance. Use cases: **devops** (9 simulated systems, 100 metrics per reading interval), **cpu-only** (10 metrics per reading), **iot** (trucking fleet telemetry, including deliberately out-of-order data and batch ingestion). Targets 11 databases: Akumuli, Cassandra, ClickHouse, CrateDB, InfluxDB, MongoDB, QuestDB, SiriDB, TimescaleDB, Timestream, VictoriaMetrics | Go; generated CSV/line-protocol | **MIT** — verified from LICENSE: "The MIT License (MIT)", © Timescale, Inc. 2017-2021 and InfluxData 2016 | Configurable to billions of points | **Deterministic**: "By supplying the same PRNG seed to the generation programs, each database is loaded with identical data and queried using identical queries" | **Best-fit fixture generator for this platform.** The `devops` use case is literally datacenter host telemetry, and `iot` gives you out-of-order + batched arrival — the two hardest ingestion-correctness conditions. Determinism via seed means a case can pin its input by `(tsbs version, use-case, seed, scale, time range)` instead of shipping gigabytes. MIT is fully Apache-2.0-compatible. | **VENDOR** |
| 35 | **ClickBench** | https://github.com/ClickHouse/ClickBench | Analytical-database benchmark: **99.9 million anonymised web-analytics records**, **43 SQL queries** covering full scan, filtered scan, index lookups and relational operations. Formats: CSV, TSV, JSONlines, Parquet. Results published for **60+ DBMSs** at benchmark.clickhouse.com (typically AWS c6a.4xlarge, 500 GB) | SQL + data | **CC BY-NC-SA 4.0** — verified from the repo LICENSE file (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International) | 99.9M rows, 43 queries, 60+ published systems | **Yes** — published per-system results | **LICENCE BLOCKER.** NonCommercial + ShareAlike is **incompatible** with an Apache-2.0 or CC-BY-4.0 corpus repo: NC forbids commercial use and SA would force the derivative under CC BY-NC-SA. **Do not vendor.** Cite the methodology and the published-results-per-system pattern only. | **REFERENCE-ONLY (hard blocker)** |
| 36 | Prometheus benchmark tooling / `promtool` | https://github.com/prometheus/prometheus | `promtool` includes rule unit testing, config checking, and TSDB analysis/benchmark subcommands | Go | **Apache-2.0** (Prometheus project) | — | Rule unit tests carry expected results | Use `promtool test rules` as the **executable oracle** for the alerting slice of the corpus: cases are runnable, not just documented. | **VENDOR** |
| 37 | Published ingestion/indexing budgets | — | **Not found as an openly licensed, citable normative source.** TSBS and ClickBench publish *observed* throughput numbers per system and hardware profile; neither publishes a *normative budget*. Prometheus publishes no SLO for ingestion rate | n/a | **No open ingestion-rate or indexing-latency budget standard was located.** Do not fabricate one | Derive budgets internally from TSBS runs on pinned hardware and record them as **platform-local provisions**, clearly marked as self-set rather than externally standardised. This is the honest answer: the budgets must be authored, not cited. |

### 1.7 Workload identity (agent-to-server mTLS)

| # | Name | URL | Contains | Format | VERIFIED licence | Volume | Ground truth? | Reuse path | Flag |
|---|------|-----|----------|--------|------------------|--------|---------------|-----------|------|
| 38 | SPIFFE specifications | https://github.com/spiffe/spiffe | `/standards` containing: *The SPIFFE Identity and Verifiable Identity Document*, *The X.509 SPIFFE Verifiable Identity Document*, *The JWT SPIFFE Verifiable Identity Document*, *The SPIFFE Workload API*. Repo also states it includes "example code, and tests" | Markdown + examples | **Apache-2.0** (repo landing page) | 4 core standards | Spec-level normative requirements; example code and tests present, but **no formal branded conformance programme was found** | Provision source for edge-collector → server identity. SPIFFE ID format (`spiffe://trust-domain/path`) is a clean, citable identifier scheme for per-tenant collector identity — well suited to boolean factors about whether a collector presented a valid SVID for its own tenant's trust domain. | **VENDOR** |
| 39 | SPIRE | https://github.com/spiffe/spire | Reference implementation: exposes the SPIFFE Workload API, attests workloads, issues SPIFFE IDs and SVIDs; supports mTLS and JWT | Go | **Apache-2.0** (repo landing page) | Large Go codebase | **No conformance suite for SPIFFE implementations was found** in this pass — the repo references security audits and CNCF TAG assessments, but not a conformance programme | Use SPIRE as the reference identity provider when constructing agent-to-server mTLS fixtures. Record explicitly that SPIFFE has **no conformance suite**, so identity cases must be authored rather than imported. | **VENDOR** |

---

## 2. Real, verified identifiers for the factor vocabulary

Everything in this section was read from a primary source during this pass. Nothing is invented.

### 2.1 OTel semantic conventions — **stable** (safe as long-lived identifiers)

Verified from https://opentelemetry.io/docs/specs/semconv/registry/attributes/service/ :

- `service.name` — **Stable**
- `service.namespace` — **Stable**
- `service.instance.id` — **Stable**
- `service.version` — **Stable**
- `service.criticality` — **Alpha**
- `service.peer.name`, `service.peer.namespace` — **Development**

### 2.1b OTel semconv — hardware & host (datacenter-relevant, currently **Development**)

Verified from the `hw` and `host` registries:

- Metrics: `hw.power` (gauge, W), `hw.energy` (counter, J), `hw.temperature`, `hw.errors` (counter), `hw.status` (UpDownCounter, `1`/`0` per state) — all **Development**
- Attributes: `hw.id` (required), `hw.type` (required; values include `battery`, `cpu`, `disk_controller`, `fan`, `gpu`, `memory`, `network`), `hw.name`, `hw.parent`
- Host: `host.id`, `host.name`, `host.type`, `host.arch`, `host.ip`, `host.mac`, `host.image.id`, `host.image.name`, `host.image.version`, `host.cpu.vendor.id`, `host.cpu.family`, `host.cpu.model.id`, `host.cpu.model.name`, `host.cpu.stepping`, `host.cpu.cache.l2.size` — **all 15 are Development**

> **Governance consequence:** the thermal/power vocabulary this platform most needs (`hw.*`) is **not
> yet Stable**. Every case citing an `hw.*` name must pin the semconv version (e.g. v1.43.0), because
> OTel's stability policy only guarantees names for Stable conventions.

### 2.1c OTel semconv — system metrics (all **Development**)

`system.cpu.utilization`, `system.cpu.time`, `system.cpu.frequency`, `system.cpu.physical.count`,
`system.cpu.logical.count`, `system.memory.usage`, `system.memory.limit`, `system.memory.utilization`,
`system.paging.usage`, `system.paging.utilization`, `system.paging.faults`, `system.paging.operations`,
`system.disk.io`, `system.disk.operations`, `system.disk.io_time`, `system.disk.operation_time`,
`system.disk.merged`, `system.disk.limit`, `system.filesystem.usage`, `system.filesystem.utilization`,
`system.filesystem.limit`, `system.filesystem.lock.count`, `system.network.io`,
`system.network.errors`, `system.network.packet.dropped`, `system.network.packet.count`,
`system.network.connection.count`, `system.uptime`, `system.process.count`, `system.process.created`,
`system.process.limit`.

### 2.1d OTel semconv — CI/CD (**Release Candidate**) — the change-management namespace

Verified from https://opentelemetry.io/docs/specs/semconv/registry/attributes/cicd/ — all **rc**:

`cicd.pipeline.name`, `cicd.pipeline.action.name`, `cicd.pipeline.result`, `cicd.pipeline.run.id`,
`cicd.pipeline.run.state`, `cicd.pipeline.run.url.full`, `cicd.pipeline.task.name`,
`cicd.pipeline.task.run.id`, `cicd.pipeline.task.run.result`, `cicd.pipeline.task.run.url.full`,
`cicd.pipeline.task.type`, `cicd.system.component`, `cicd.worker.id`, `cicd.worker.name`,
`cicd.worker.state`, `cicd.worker.url.full`.

Enumerations worth reusing verbatim:
- `cicd.pipeline.run.state` ∈ `pending` (queue/provisioning), `executing`, `finalizing` (cleanup)
- `cicd.pipeline.result` and `cicd.pipeline.task.run.result` ∈ `success`, `failure`, `timeout`, `skip`, `error`, `cancellation`

> This is the **single most directly reusable enumeration** for a corpus governing software change:
> a six-valued result vocabulary that already distinguishes `failure` from `error` from `timeout`
> from `cancellation` from `skip` — distinctions a hand-rolled disposition enum usually collapses.

### 2.2 Redfish resource names (verified from https://redfish.dmtf.org/redfish/schema_index)

**Thermal & cooling:** `Thermal`, `ThermalSubsystem`, `ThermalMetrics`, `ThermalEquipment`, `Fan`,
`Filter`, `Heater`, `HeaterMetrics`, `CoolingUnit`, `CoolingLoop`, `CoolantConnector`, `Pump`,
`Reservoir`, `LeakDetection`, `LeakDetector`, `Battery`, `BatteryMetrics`

**Power:** `Power`, `PowerSubsystem`, `PowerSupply`, `PowerSupplyMetrics`, `PowerDistribution`,
`PowerDistributionMetrics`, `PowerDomain`, `PowerEquipment`, `Outlet`, `OutletGroup`

**Sensors & environment:** `Sensor`, `EnvironmentMetrics`

**Telemetry:** `TelemetryService`, `MetricDefinition`, `MetricReport`, `MetricReportDefinition`,
`TelemetryData`, `Triggers`

**Events:** `Event`, `EventService`, `EventDestination`

**Identity & access:** `AccountService`, `ManagerAccount`, `Session`, `SessionService`, `Role`,
`Certificate`, `AllowDeny`

**Logs:** `LogService`, `LogEntry`

**Change/update:** `UpdateService`, `UpdateServiceCapabilities`, `SoftwareInventory`

**Tasks/jobs:** `Task`, `TaskService`, `Job`, `JobService`, `JobDocument`, `JobExecutor`

**Aggregation (multi-tenant):** `AggregationService`, `AggregationSource`

### 2.3 Weaver live-check advice types (verified from the weaver_live_check README)

Severity levels, in precedence order: **`violation`** (drives non-zero exit), **`improvement`**,
**`information`**.

Builtin advisors: `missing_attribute` ("Attribute does not exist in the registry"), `type_mismatch`.

From the default OTel semconv Rego rules: `extends_namespace`, `illegal_namespace`, `invalid_format`,
`missing_namespace`, `stability`, `undefined_enum_variant`, `not_stable`, `deprecated`.

Findings are returned as a list of `PolicyFinding` per sample entity, each with an `id` that is
"a simple machine readable string to group findings of a particular kind or type".

### 2.4 Redaction processor — config vocabulary and audit attributes

Config: `allow_all_keys`, `allowed_keys`, `ignored_keys`, `ignored_key_patterns`,
`blocked_key_patterns`, `blocked_values`, `allowed_values`, `redact_all_types`, `hash_function`
(∈ `md5`, `sha1`, `sha3`, `hmac-sha256`, `hmac-sha512`), `hmac_key`, `summary` (∈ `debug`, `info`,
`silent`), plus `url_sanitizer.{enabled, attributes, sanitize_span_name}` and
`db_sanitizer.{sanitize_span_name, [sql|redis|memcached|mongo|opensearch|es].{enabled, attributes}}`.

Audit summary attributes emitted (span/log/datapoint level):
`redaction.redacted.keys`, `redaction.redacted.count`, `redaction.masked.keys`,
`redaction.masked.count`, `redaction.allowed.keys`, `redaction.allowed.count`,
`redaction.ignored.count` (`.keys` variants debug-only; `.count` at info and debug).
Log body map level: `redaction.body.redacted.keys/.count`, `redaction.body.masked.keys/.count`,
`redaction.body.allowed.keys/.count`, `redaction.body.ignored.count`.

> These count attributes are a **built-in machine-checkable expected disposition** for privacy cases:
> "given this badge-telemetry payload and this redaction config, expect
> `redaction.masked.count == 3` and `redaction.allowed.count == 12`."

### 2.5 promtool rule unit test fields (verified from the Prometheus docs)

Top level: `rule_files`, `evaluation_interval`, `group_eval_order`, `fuzzy_compare`, `tests`.

Per test: `name`, `interval`, `input_series`, `start_timestamp`, `external_labels`, `external_url`,
`alert_rule_test`, `promql_expr_test`.

Series: `series`, `values` (expanding notation).

PromQL expression tests: `expr`, `eval_time`, `exp_samples` → `labels`, `value`.

Alerting rule tests: `alertname`, `eval_time`, `exp_alerts` → `exp_labels`, `exp_annotations`.

**Mapping onto a corpus case:**

| Corpus concept | promtool field |
|---|---|
| case id | `tests[].name` |
| provisions engaged | `rule_files` (+ the specific `alertname`) |
| boolean/numeric factor facts | `input_series` (`series` + `values`) |
| evaluation point | `eval_time` |
| expected disposition | `exp_alerts` (empty list = "no alert" — a genuine negative case) |
| expected reasoning/labels | `exp_labels`, `exp_annotations` |
| environment context | `external_labels`, `external_url` |

### 2.6 Remote-write conformance test names (18, verified)

`Counter`, `Gauge`, `Histogram`, `Summary`, `EmptyLabels`, `HonorLabels`, `InstanceLabel`,
`JobLabel`, `NameLabel`, `RepeatedLabels`, `SortedLabels`, `Headers`, `Invalid`, `Ordering`,
`Staleness`, `Timestamp`, `Up`.

### 2.7 OpenMetrics types, suffixes and terminator (verified)

Types: `counter`, `gauge`, `histogram`, `gaugehistogram`, `summary`, `info`, `stateset`, `unknown`.

Required suffixes: counter → `_total`, `_created`; histogram → `_bucket`, `_count`, `_sum`,
`_created`; gaugehistogram → `_bucket`, `_gcount`, `_gsum`; summary → `_count`, `_sum`, `_created`;
info → `_info`; gauge/stateset/unknown → none.

Terminator: expositions **MUST end with `EOF`** and SHOULD end with `EOF\n`.

### 2.8 BPF verifier rejection reasons (verbatim `__msg(...)` strings, verified)

From `progs/verifier_bounds.c`:
- `"R0 max value is outside of the allowed memory range"`
- `"R0 min value is negative, either use unsigned index or do a if (index >=0) check."`
- `"R9 pointer -= pointer prohibited"`
- `"map_value pointer and 4294967295"`
- `"map_value pointer offset 1073741822 is not allowed"`
- `"value -4294967168 makes map_value pointer be out of bounds"`
- `"R0 unbounded memory access"`
- `"math between map_value pointer and 4294967294 is not allowed"`
- `"invalid access to map value"`

From `progs/verifier_scalar_ids.c`:
- `"register with unbounded min value"`
- `"div by zero"`
- `"R0 max value is outside of the allowed memory range"`
- log-level-2 precision traces such as `"frame0: regs=r0 stack= before 4: (25) if r1 > 0x7 goto pc+0"` and `"frame0: parent state regs=r0,r1,r2 stack=:"`

Annotation macros: `__description`, `__success`, `__failure`, `__msg`, `__retval`, `__flag`,
`__log_level`, `__success_unpriv`, `__failure_unpriv`.

> The privileged/unprivileged split is the reusable insight: **the same input yields different
> verdicts at different authority levels.** A multi-tenant platform needs exactly this — a case
> should be able to carry `expected_disposition_by_role`, not one global verdict.

### 2.9 Redfish interop profile requirement vocabulary (verified)

- `ReadRequirement` ∈ `Mandatory`, `Recommended`, `IfImplemented`, `Supported`, `Excluded`
- `WriteRequirement`
- `MinCount`, `MinSupportedValues`, `MinVersion`
- `Comparison` ∈ `AnyOf`, `AllOf`, `Equal`, `NotEqual`, `GreaterThan`, `LessThan`, `Absent`, `Present`
- `ConditionalRequirements` — requirements triggered by other conditions
- `ActionRequirements`, `Members` (with `MinCount`)
- Report outcomes: **Pass / Fail / Skip / Warning** per resource checked

### 2.10 SNMPv2-MIB objects (RFC 3418, freely redistributable)

System group: `sysDescr`, `sysObjectID`, `sysUpTime`, `sysContact`, `sysName`, `sysLocation`,
`sysServices`. SNMP group: `snmpInPkts`, `snmpInBadVersions`, `snmpEnableAuthenTraps`.
Notifications: `coldStart`, `warmStart`, `authenticationFailure`.

### 2.11 Attributes-processor action verbs (verified)

`insert`, `update`, `upsert`, `delete`, `hash`, `extract`, `convert`.
Field requirements: insert/update/upsert need `key` + one of `value` / `from_attribute` /
`from_context` / `default_value`; delete/hash take `key` and/or `pattern`; extract needs `key` +
`pattern`; convert needs `key` + `converted_type`.

---

## 3. Licence risk register

| Source | Licence | Vendorable into Apache-2.0 / CC-BY-4.0 repo? | Note |
|---|---|---|---|
| OTel spec, semconv, proto, collector, contrib, Weaver | Apache-2.0 | **Yes** | Preserve NOTICE. |
| Prometheus, promtool, prometheus/compliance, OpenMetrics repo, avalanche | Apache-2.0 | **Yes** | OpenMetrics *spec markdown* carries additional IETF trust200902 boilerplate — review before verbatim reuse. |
| TSBS | MIT | **Yes** | Retain both copyright lines (Timescale 2017-2021; InfluxData 2016). |
| SPIFFE / SPIRE | Apache-2.0 | **Yes** | No conformance suite exists — cases must be authored. |
| bcc | Apache-2.0 | **Yes** | |
| libbpf | BSD-2-Clause **OR** LGPL-2.1 | **Yes, electing BSD-2-Clause** | Record the election explicitly in NOTICE. |
| Redfish Interop Validator, Service Validator, Mockup Server | BSD 3-Clause | **Yes** | Reproduce DMTF copyright notice and the non-endorsement clause. |
| Redfish schemas DSP8010, mockups DSP2043 | DMTF copyright policy (reproduction permitted "for uses consistent with this purpose, provided that correct attribution is given") | **Conditionally** — not an SPDX/OSI licence | Prefer URL+version references; vendor only an attributed subset after legal review. |
| SNMP MIB modules (RFC 3418 and peers) | Internet Society / IETF; **MIB module text copyable "without restriction of any kind"** with notice | **Yes** | Include the copyright paragraph verbatim alongside any copied MIB. |
| BPF selftests, LTP, kselftest | GPL-2.0 / GPL-2.0-or-later | **No** | Reference and imitate structure; do not copy source. |
| **ClickBench** | **CC BY-NC-SA 4.0** | **No — hard blocker** | NonCommercial and ShareAlike both conflict. Cite only. |
| BACnet / ASHRAE 135 | Paywalled, commercial | **No** | Cite clause numbers only. |
| Modbus specs | Free download behind an unread click-through agreement | **Unknown — treat as no** | Terms UNVERIFIED. |
| IPMI v2.0 | Terms not stated on Intel's page | **Unknown — treat as no** | Also frozen since June 2020; prefer Redfish. |

---

## 4. Recommended construction path

1. **Adopt promtool's YAML schema** as the native serialisation for alerting/escalation cases, and
   `promtool test rules` as the executable oracle. Cases become runnable, not merely documented.
2. **Adopt the openmetricstest layout** — a case is a directory containing a manifest; the harness
   discovers cases by walking the tree. No central index to conflict on.
3. **Adopt TAP** (from kselftest) as the result wire format, including its `# SKIP <reason>` form.
4. **Adopt a five-valued modality** from Redfish interop profiles — `Mandatory`, `Recommended`,
   `IfImplemented`, `Supported`, `Excluded` — instead of a two-valued MUST/SHOULD, plus
   `ConditionalRequirements` for provisions that engage only on a trigger.
5. **Adopt a disposition enum that admits non-liquet.** Three independent sources converge on this:
   the OTel compliance matrix's blank "unknown" cell, the PromQL tester's `unsupported`, and
   kselftest's `SKIP`. A corpus that cannot say "undetermined" will be forced into false verdicts.
6. **Carry per-role dispositions**, following the BPF verifier's privileged/unprivileged split.
7. **Name factors with cited identifiers**: OTel semconv attributes (pinned to a version, with the
   stability level recorded), Redfish resource names, `cicd.*` result enums, redaction summary
   attributes, and SNMPv2-MIB object names.
8. **Generate fixtures, don't ship them**: TSBS with a pinned seed for host/IoT telemetry, avalanche
   for churn and cardinality, the Redfish Mockup Server's `public-rackmount1` for BMS/chassis.
9. **Author the ingestion budgets yourself and label them as self-set** — no open normative
   ingestion-rate or indexing-latency budget was located, and none should be invented from thin air.
10. **Author identity cases yourself** — SPIFFE has specifications and example tests but no
    conformance programme was found.

---

## 5. Explicit negative findings

- **No open normative ingestion-rate or indexing-latency budget** exists in TSBS, ClickBench or the
  Prometheus project. They publish observed measurements per system and hardware, not budgets.
- **No SPIFFE conformance suite** was found. SPIRE references audits and CNCF TAG assessments only.
- **No open DCIM conformance suite** was found; Redfish's facility resources are the nearest model.
- **ClickBench cannot be vendored** — CC BY-NC-SA 4.0.
- **BACnet is genuinely paywalled**; Modbus and IPMI terms remain **UNVERIFIED** and are therefore
  treated as non-redistributable.

---

*Compiled 2026-09-05. Every licence above was read from a primary source; items that could not be
verified are marked UNVERIFIED rather than guessed.*
