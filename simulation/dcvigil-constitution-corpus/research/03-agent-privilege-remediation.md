# Lane 03 — Privileged-Agent Security, Telemetry Integrity, Remediation Blast Radius, Parser Sandboxing

**Scope owner:** research lane 03 (DCVigil open compliance test corpus)
**Date of verification:** 2026-09-05
**Corpus target shape:** every case is `(case id, provisions engaged, boolean factor facts, expected disposition)`
**Deliberately excluded (covered by prior survey):** Juliet/SARD, CWE, CVEfixes, AgentDojo, garak, PyRIT, Wycheproof, ARVO.

**Licence discipline used here.** Every licence marked VERIFIED was read from the project's own
`LICENSE`/`COPYING`/SPDX header (raw file fetch) or from the artifact's own landing page during this
session. Anything I could not read directly is marked **UNVERIFIED — do not rely on**. Nothing is
inferred from a badge, a package registry field alone, or from "it's a CNCF project".

---

## 0. Executive orientation

Two structural findings dominate this lane.

**(a) There is no curated corpus of monitoring-agent vulnerabilities.** I searched specifically for a
dataset of privileged observability-agent CVEs (Datadog / Splunk UF / Beats / Zabbix / NRPE /
node_exporter / OTel Collector) and found none. The nearest published vulnerability datasets are
general-purpose (CVEfixes, CVE-Bench, HF CVE/CWE dumps) and none of them slices by "agent that runs
as root on customer hardware". **This is a genuine gap the DCVigil corpus can fill**, and the raw
material to fill it exists as per-package advisory records under a verified open licence (GitHub
Advisory Database, CC-BY-4.0).

**(b) The single best-shaped reusable oracles in this lane are not security corpora at all — they are
upstream *unit test tables*.** Three of them are already, literally, `(name, boolean facts, expected
disposition)` tuples:

| Source | Case id | Facts | Disposition |
|---|---|---|---|
| Linux BPF verifier selftests | `__description("...")` | program text + `SEC()` + capability level | `__success` / `__failure` + `__msg("<exact reason>")` |
| PREVAIL YAML test-data | `test-case:` | `pre:` invariants | `post:` invariants + `messages:` |
| k8s `eviction_test.go` | `name:` | `pdbs`, `podPhase`, `podTerminating`, `policies`, `badNameInURL` | `expectError`, `expectedCause`, `expectedDeleteCount` |

These give the corpus a *provenance-backed disposition* rather than an author-asserted one. That is
the scarce ingredient.

---

## 1. Privileged monitoring-agent attack surface

### 1.1 Is there a curated corpus? — **No. Verified absent.**

Searched for: curated monitoring/observability agent CVE datasets; "privileged agent" security
benchmarks; agent-socket privilege-escalation test suites. Results returned only general vulnerability
datasets (CVEfixes, CVE-Bench, `stasvinokur/cve-and-cwe-dataset-1999-2025`) with no agent-specific
slice, plus vendor advisory pages. **Conclusion: build it. The corpus is the contribution.**

### 1.2 GitHub Advisory Database (GHSA) — the substrate to build it from

- **Name / URL:** GitHub Advisory Database — https://github.com/github/advisory-database
- **Contents:** every GHSA record as an OSV-schema JSON file, including the *reviewed* advisories filed
  by vendors against their own agents. Datadog, OpenTelemetry, Elastic all file here.
- **Format:** OSV JSON (`id`, `aliases`, `summary`, `details`, `severity` [CVSS vector], `affected`
  [package + version ranges], `references`, `database_specific.cwe_ids`).
- **Licence:** **VERIFIED — CC-BY-4.0.** Read from `LICENSE.md` at repo root: "Attribution 4.0
  International". (Attribution required; commercial use and redistribution permitted.)
- **Volume:** tens of thousands of advisories; the agent-relevant slice is a query, not a download.
- **Ground truth:** yes — vendor-asserted affected/patched version ranges, CVSS, CWE ids.
- **Reuse path:** for each agent package, query GHSA → emit one corpus case per advisory:
  `case id = GHSA-xxxx`, `provisions engaged = {privileged-component-change, permission-model-change}`,
  `factor facts = {runs_as_root, writable_by_unprivileged, local_attacker_sufficient,
  code_executed_on_upgrade, cwe_class_permission}`, `expected disposition = advisory severity band`.
- **Flag:** **SAFE TO VENDOR** with attribution (CC-BY-4.0). Attribute GitHub + the advisory authors.

### 1.3 OSV / OSV.dev

- **URL:** https://osv.dev, https://github.com/google/osv.dev, https://github.com/ossf/osv-schema
- **Licence:** the **code** of `google/osv.dev` and `ossf/osv-schema` is **VERIFIED Apache-2.0**
  (read from each repo's `LICENSE`). The **vulnerability data** licence is **UNVERIFIED** — I could
  not find any licence statement on osv.dev's home page or FAQ; OSV aggregates from upstream feeds
  each with their own terms. **Do not vendor OSV-aggregated records as a bloc.** Pull GHSA records
  from `github/advisory-database` directly (CC-BY-4.0, verified) instead.
- **Flag:** tooling SAFE TO VENDOR; **aggregated data REFERENCE-ONLY pending per-source licence check.**

### 1.4 Concrete verified agent advisories (seed cases)

| Advisory | Product | Class | Verified detail |
|---|---|---|---|
| GHSA-6852-76c5-6cmg / **CVE-2025-61667** | Datadog Linux Host Agent 7.65.0–7.70.2 (fixed 7.71.0) | **CWE-276 Incorrect Default Permissions**, CVSS 7.0 High | `__pycache__` directory writable by low-privileged local user; injected code executes during Agent **upgrade**. Verified from the advisory page. |
| GHSA-h8qx-4jh5-pf43 | Datadog SSI Injector | Local privilege escalation "in certain conditions" | Verified as an existing DataDog/datadog-agent advisory. |
| GHSA-c74f-6mfw-mm4v / **CVE-2024-36129** | OpenTelemetry Collector (`configgrpc`/`confighttp`) | Decompression-bomb DoS over HTTP **and** gRPC | Verified as an open-telemetry/opentelemetry-collector security advisory. |
| **CVE-2025-27237** | Zabbix Agent | Privilege escalation | Found via search; **CVSS/CWE UNVERIFIED — confirm against Zabbix's own advisory before use.** |
| SP-CAAAP3M | Splunk (run-as-non-root guidance) | LPE arising from the vendor's *own hardening instructions* | Splunk advisory. Notable because the *documentation* is the defect — a good corpus case for "guidance-as-control". |
| **CVE-2025-20298**, **CVE-2025-20387** | Splunk Universal Forwarder | Incorrect file permissions → LPE (Windows) | Seen only in third-party vuln databases; **UNVERIFIED against Splunk's advisory portal.** |

`SplunkWhisperer2` (https://github.com/cnotin/SplunkWhisperer2) is the canonical *exploit* for
UF misconfiguration (LPE/RCE via the forwarder's own bundle-deployment path). **Licence UNVERIFIED.**
Treat as **REFERENCE-ONLY**: cite the technique, do not vendor the code.

### 1.5 "Unprivileged user interacts with a privileged agent socket" — is there an open test suite?

**No single-purpose suite exists.** The closest reusable material, in descending order of fit:

1. **D-Bus policy + polkit authorisation.** This is the closest thing in open source to a *declarative
   rule language for "may an unprivileged caller invoke this privileged method over this socket"*,
   with an allow/deny disposition. polkit licence **VERIFIED — GNU Library GPL v2** (read from
   `polkit-org/polkit/COPYING`). D-Bus reference implementation `COPYING` fetch failed at the time of this survey
   → **licence UNVERIFIED** (commonly AFL-2.1 OR GPL-2.0+; confirm).
   **Flag: REFERENCE-ONLY for the vocabulary** (LGPL/GPL copyleft on any vendored fixtures).
2. **systemd integration tests** (`test/TEST-*`) exercise socket activation, `SO_PEERCRED`-based
   authorisation and varlink privilege boundaries. Licence **VERIFIED — LGPL-2.1** (from
   `systemd/systemd/LICENSE.LGPL2.1`). **Flag: REFERENCE-ONLY** (copyleft).
3. **LTP** `testcases/kernel/security/` and the CVE reproducers — see §2.3.
4. **CyberArk PipeViewer** (https://github.com/cyberark/PipeViewer) — Windows named-pipe DACL
   enumeration; the analogue for the Windows agent case (Splunk UF, Datadog Windows agent).
   **Licence UNVERIFIED. REFERENCE-ONLY.**

**Recommended synthesis for DCVigil:** author the socket cases yourself as a small factor-based
matrix. The factor space is small and fully enumerable, which is exactly what a compliance corpus
wants. Do not try to vendor a suite that does not exist.

---

## 2. eBPF and kernel safety

### 2.1 Linux BPF verifier selftests — **the highest-value source in this entire lane**

- **Name / URL:** `tools/testing/selftests/bpf/progs/verifier_*.c` in the Linux kernel tree —
  https://github.com/torvalds/linux/tree/master/tools/testing/selftests/bpf/progs
- **Contents (all counts measured when this survey was compiled by downloading every file):**
  - **125** `verifier_*.c` modules, enumerated from the `#include "verifier_*.skel.h"` list in
    `prog_tests/verifier.c`.
  - **1,395** named test cases (`__description("...")`).
  - **1,169** `__success` and **687** `__failure` annotations.
  - **1,644** `__msg(...)` assertions carrying **1,084 distinct expected verifier messages**.
  - **238** `__failure_unpriv` and **254** `__success_unpriv` — i.e. **492 cases whose disposition is
    explicitly a function of the actor's privilege level**.
- **Format:** C with annotation macros. Worked example (`verifier_netfilter_retcode.c`):
  ```c
  SEC("netfilter")
  __description("bpf_exit with invalid return code. test1")
  __failure __msg("R0 is not a known value")
  __naked void with_invalid_return_code_test1(void) { ... }
  ```
  and from `verifier_bounds.c`, the dual-privilege form:
  ```c
  __description("subtraction bounds (map value) variant 1")
  __failure __msg("R0 max value is outside of the allowed memory range")
  __failure_unpriv
  ```
- **Licence:** **VERIFIED — GPL-2.0.** SPDX headers read directly: 124 files
  `// SPDX-License-Identifier: GPL-2.0`, 1 file `GPL-2.0-only`. No dual-licensed files in this set.
- **Ground truth:** yes, and unusually strong — the expected *reason string* is asserted, not just
  pass/fail, and CI-enforced upstream on every kernel commit.
- **Reuse path — this is a near-exact structural match:**
  - `case id` ← `__description` string (unique, stable, human-readable)
  - `provisions engaged` ← the `SEC()` program type (`socket`, `netfilter`, `lsm`, `xdp`, `tc`,
    `cgroup/*`) mapped to your provision taxonomy for "which kernel-attachment surface is engaged"
  - `boolean factor facts` ← `{unprivileged_load, direct_packet_access, map_value_arith,
    pointer_leak_to_scalar, unbounded_loop, spill_fill_of_pointer, ...}` derived from the module name
    and body
  - `expected disposition` ← `__success` / `__failure`, **plus** `__msg` as the required rationale,
    **plus** the `_unpriv` variant as a second disposition under a different actor privilege
  - The 1,084 distinct `__msg` strings are effectively a **published rejection taxonomy** — the exact
    artefact the brief asked whether existed. It does: it just lives in test annotations rather than
    in documentation. Top recurring classes measured: memory-range violations (32), invalid context
    access (31), invalid packet access (22), unreleased reference (16), unbounded min value (12),
    invalid mem access (12), div-by-zero (12), negative-register (10+), precision-tracking traces,
    "infinite loop detected", "same insn cannot be used with different pointers".
- **Flag:** **REFERENCE-ONLY for vendoring into a permissive corpus** (GPL-2.0 copyleft). The
  *derived metadata* — case names, expected dispositions, expected message strings — should be treated
  conservatively: extract the taxonomy and re-author your own minimal reproducers rather than copying
  the C bodies. If DCVigil is willing to publish the eBPF sub-corpus under GPL-2.0, it becomes
  SAFE TO VENDOR wholesale.

### 2.2 PREVAIL (vbpf/prevail, formerly vbpf/ebpf-verifier) — **safe-to-vendor equivalent**

- **URL:** https://github.com/vbpf/prevail (PLDI paper: "Simple and Precise Static Analysis of
  Untrusted Linux Kernel Extensions")
- **Contents:** an independent, polynomial-time eBPF verifier built on abstract interpretation, plus
  **`test-data/*.yaml`** — a declarative test corpus.
- **Format — verified sample from `test-data/jump.yaml`:**
  ```yaml
  test-case: jump to fallthrough
  pre: []
  code:
    <start>: |
      r0 = 0
      if r0 != 0 goto <exit>
    <exit>: |
      exit
  post:
    - r0.type=number
    - r0.svalue=0
  messages: []
  ```
- **Licence:** **VERIFIED — MIT.** Both the repo `LICENSE.txt` ("MIT License") and per-file SPDX
  headers in `test-data/*.yaml` (`# SPDX-License-Identifier: MIT`).
- **Ground truth:** yes — `post` invariants and `messages` are the asserted oracle; also an
  `elf_inventory.json` driving `test_verify_samples.cpp` over real ELF objects.
- **Reuse path:** the YAML *is* the corpus row. `test-case` → case id; `pre` → factor facts;
  `messages` → expected disposition + rationale. Also supports differential testing: same program,
  two verifiers (kernel vs PREVAIL), disagreement = a case worth adjudicating.
- **Flag:** **SAFE TO VENDOR (MIT).** This is the permissively-licensed stand-in for §2.1.

### 2.3 Linux Test Project (LTP)

- **URL:** https://github.com/linux-test-project/ltp
- **Contents:** the `runtest/cve` scenario file maps CVE ids to concrete reproducer binaries —
  **verified: 103 non-comment entries**, e.g. `cve-2016-5195 dirtyc0w`, `cve-2017-16995 bpf_prog03`,
  `cve-2018-18445 bpf_prog04`, `cve-2017-1000364 stack_clash`, `cve-2017-5754 meltdown`. Plus
  `testcases/kernel/security/` (SMACK, IMA integrity), controllers/cgroups, and the syscall suite.
- **Format:** C test binaries + shell scenario files; results are TCONF/TPASS/TFAIL/TBROK.
- **Licence:** **VERIFIED — GPL-2.0** (GitHub licence metadata resolves the repo `LICENSE` to
  "GNU General Public License v2.0"; `runtest/Makefile` header restates GPL-2.0-or-later).
- **Ground truth:** yes — pass/fail per CVE, and the `bpf_prog03`/`bpf_prog04` entries are exactly
  the eBPF-privilege-escalation regression cases relevant here.
- **Reuse path:** the `runtest/cve` mapping is a ready-made **provision→case index**: one corpus row
  per CVE, `factor facts = {kernel_version_in_range, unprivileged_bpf_enabled, agent_loads_bpf,
  module_load_permitted}`, disposition = reproducer pass/fail. Also the *canonical demonstration*
  that "kernel-panic regression practice" is a real, maintained discipline with a CVE-indexed suite.
- **Flag:** **REFERENCE-ONLY for vendoring into a permissive corpus (GPL-2.0).** The
  CVE→test-name *index* is a fact table and can be cited/rebuilt freely.

### 2.4 Kernel-panic regression at scale — syzkaller / syzbot

- **URL:** https://github.com/google/syzkaller
- **Contents:** coverage-guided kernel fuzzer; syzbot publishes crash reports with **syz-reproducers
  and C reproducers**, bisected to the introducing and fixing commits, per kernel branch.
- **Licence:** **VERIFIED — Apache-2.0** (repo `LICENSE`).
- **Ground truth:** yes — crash signature + reproducer + fix commit. This is the closest thing to a
  labelled kernel-panic regression corpus that exists.
- **Reuse path:** for the "agent loads a kernel module / eBPF program that panics the host" provision,
  syzbot's fixed-bug list gives `(reproducer, affected kernel range, fix commit)` — a defensible
  ground truth for "would this change have panicked node kernels in the fleet?".
- **Flag:** tooling **SAFE TO VENDOR (Apache-2.0)**. Individual reproducers carry kernel-derived
  provenance — cite, don't bulk-vendor.

### 2.5 bpf_conformance

- **URL:** https://github.com/Alan-Jowett/bpf_conformance
- **Contents:** a portable conformance suite for BPF *runtimes* (instruction-semantics tests as
  `.data` files: input program, memory, expected result). Used by PREVAIL/uBPF/PREVAIL-adjacent
  runtimes; PREVAIL links `bpf_conformance_core` in its own test target (verified in its CMakeLists).
- **Licence:** **VERIFIED — MIT** (`LICENSE`, "MIT License, Copyright (c) 2022 Alan Jowett").
- **Reuse path:** semantics-level oracle for "does our eBPF probe mean the same thing on every node".
- **Flag:** **SAFE TO VENDOR (MIT).**

### 2.6 CO-RE portability and multi-kernel matrices

- **libbpf** — https://github.com/libbpf/libbpf. **Licence: VERIFIED —
  `LGPL-2.1-only OR BSD-2-Clause`** (the repo `LICENSE` file contains exactly that SPDX expression).
  The BSD-2-Clause arm makes libbpf-derived material **SAFE TO VENDOR** if you elect that arm.
- **libbpf-bootstrap** — https://github.com/libbpf/libbpf-bootstrap. **Licence: VERIFIED —
  BSD 3-Clause** (`LICENSE`, "Copyright (c) 2020, Andrii Nakryiko"). Canonical CO-RE skeleton
  examples; **SAFE TO VENDOR.**
- **cilium/little-vm-helper (LVH)** — https://github.com/cilium/little-vm-helper. **Licence: VERIFIED —
  Apache-2.0.** This is the practical tool for the multi-kernel-version matrix: boot the same eBPF
  object under a grid of kernel images in CI. **SAFE TO VENDOR.**
- **cilium/ebpf** (Go loader) — **Licence: VERIFIED — MIT** (`LICENSE`, Nathan Sweet / Cloudflare).
- **bcc** — **Licence: VERIFIED — Apache-2.0** (`LICENSE.txt`).
- **bpftrace** — https://github.com/bpftrace/bpftrace. **Licence: VERIFIED — Apache-2.0** (`LICENSE`).
  Its `tests/` tree is a large gtest suite (verified: `tests/CMakeLists.txt` lists ~40+ unit-test
  translation units incl. `btf.cpp`, `attached_probe.cpp`, `bpfbytecode.cpp`, `field_analyser.cpp`,
  `globalvars.cpp`) plus codegen and runtime tests. **SAFE TO VENDOR.**
- **aquasecurity/tracee** — **Licence: VERIFIED — Apache-2.0.** Ships CO-RE eBPF probes plus a
  signature/rule layer; useful as a second detection vocabulary alongside Falco.
- **bpfvet** (https://github.com/boratanrikulu/bpfvet) — analyses a compiled eBPF object and reports
  minimum kernel version + CO-RE coverage. **Licence UNVERIFIED. REFERENCE-ONLY** (but the *idea* —
  "minimum kernel version is a computable property of the artefact" — is directly a factor fact).

**No published, maintained CO-RE compatibility *matrix* document exists.** What exists is the
*tooling* to generate one per-project (LVH + libbpf + BTF). For DCVigil, "the change ships an eBPF
object whose BTF relocations were not exercised against kernel range X" is a factor fact you compute,
not one you look up.

---

## 3. Telemetry integrity

### 3.1 SPIFFE / SPIRE

- **URL:** https://github.com/spiffe/spire, https://spiffe.io
- **Contents:** workload identity (SVIDs as X.509 or JWT), node attestation + workload attestation.
  The workload-attestation model — the SPIRE agent derives caller identity from the *kernel's* view of
  the peer on a Unix socket — is precisely the mechanism that closes the §1.5 gap.
- **Licence:** **VERIFIED — Apache-2.0** (`spiffe/spire/main/LICENSE`).
- **Test material:** SPIRE runs a sharded **integration test suite** (`test/integration/suites/...`)
  across x64+arm64 in CI (verified in `.github/workflows/pr_build.yaml`: 10 parallel runners per arch,
  45-min timeout, `make load-images` then "Run integration tests"). I confirmed at least the
  `suites/upstream-authority-ejbca` suite by name; the full suite list was not enumerable via raw
  fetch — **suite count UNVERIFIED**.
- **Reuse path:** SPIFFE gives you the *vocabulary* for telemetry-identity factor facts:
  `{svid_present, svid_expired, trust_domain_match, attestation_selector_satisfied,
  federated_bundle_used}`. Disposition: accept / reject the telemetry stream.
- **Flag:** **SAFE TO VENDOR (Apache-2.0).**

### 3.2 OpenTelemetry Collector security guidance — **verified normative text**

- **URL:** https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/security-best-practices.md
- **Verified normative statements** (these are quotable *provisions*, with RFC-2119 keywords, which is
  unusually convenient for a compliance corpus):
  - Configuration **MUST** come from the central configuration file; **SHOULD** use configuration
    helpers. "The Collector binary does not contain an embedded or default configuration and **MUST
    NOT** start without a configuration file... If an invalid configuration is detected, the Collector
    **MUST** fail to start as a protective mechanism."
  - Permissions: **SHOULD** minimize privileged access; **MUST** document what requires privileged
    access and why. "The Collector... **SHOULD NOT** be run as a root/admin user."
  - Receivers/Exporters: **MUST** default to encrypted connections; **SHOULD** leverage helpers.
  - Extensions: **SHOULD NOT** expose sensitive health or telemetry data by default.
  - Sensitive config fields **MUST** use `configopaque.String` so they are masked on serialisation.
- **Licence:** **VERIFIED — Apache-2.0** (repo `LICENSE`). Same for
  `opentelemetry-collector-contrib` (**VERIFIED Apache-2.0**) and `opentelemetry-specification`
  (**VERIFIED Apache-2.0**).
- **Reuse path:** **this is your provision text.** Each MUST/SHOULD maps 1:1 to a provision id; each
  becomes a case family with factor facts like `{runs_as_root, tls_disabled_on_receiver,
  config_embedded_in_binary, opaque_type_not_used, healthcheck_extension_public}`.
- **Flag:** **SAFE TO VENDOR (Apache-2.0)**, with attribution.

### 3.3 OpAMP — agent↔server management protocol (the mTLS/rotation story)

- **URL:** https://github.com/open-telemetry/opamp-spec (spec), https://github.com/open-telemetry/opamp-go
- **Licence:** **VERIFIED — Apache-2.0** (both repos).
- **Verified content** (from `specification.md` section index and body): client-side TLS certificate
  management; a `CertificateRequest`/`TLSCertificate` message pair carrying `cert`, `private_key`,
  `ca_cert`; a **CSR-based certificate-signing flow** where the agent obtains a client cert from the
  server; an explicit **Trust On First Use (TOFU)** bootstrap flow; certificate registration,
  revocation and rotation; per-destination `OpAMPConnectionSettings.certificate`,
  `TelemetryConnectionSettings.certificate`, `OtherConnectionSettings.certificate`; a
  `DownloadableFile.signature` field for **code signing of agent packages**; and dedicated
  "Security Considerations" sections. It also warns that clients with only ephemeral storage
  **SHOULD reject certificate offers** or risk losing access after restart.
- **Why it matters for DCVigil:** OpAMP is the closest thing to a *standard* for the exact system
  under governance — a fleet of privileged agents that receive remote configuration and signed package
  updates from a server. `DownloadableFile.signature` + the CSR/TOFU flows give you concrete,
  standards-anchored factor facts for **agent-update integrity** and **remediation-channel authenticity**.
- **Flag:** **SAFE TO VENDOR (Apache-2.0).**

### 3.4 Signed logs/metrics — is there a standard? **Yes for logs; effectively no for metrics.**

- **RFC 5848, "Signed Syslog Messages" — VERIFIED.** Status: **Standards Track** (IESG-approved).
  Specifies `syslog-sign`: **Signature Blocks** (detached signatures over batches of previously sent
  RFC 5424 messages), **Hash Blocks** (SHA-1 or SHA-256 hash of each covered message, ordered), and
  **Certificate Blocks** (delivering PKIX certificates or OpenPGP keys). Explicitly provides
  "origin authentication, message integrity, replay resistance, message sequencing, and detection of
  missing messages". IETF RFC text is freely redistributable under the IETF Trust Legal Provisions
  (BSD-style for code components); **treat the prose as citable, the ABNF/code components as reusable.**
  - **This is the precise answer to "is there a standard for signed logs?"** — and the five properties
    it names are an off-the-shelf factor vocabulary: `{origin_authenticated, integrity_verified,
    replay_resistant, sequence_intact, gap_detected}`.
- **Metrics:** no equivalent standard. OTLP has no payload-signature field; OpAMP signs *artefacts*
  (`DownloadableFile.signature`), not *telemetry*. The practical substitutes are transport-level
  (mTLS + SPIFFE identity) and supply-chain attestation:
  - **in-toto** — https://github.com/in-toto/in-toto (**VERIFIED Apache-2.0**, "Copyright 2018 New
    York University") and **in-toto/attestation** (**VERIFIED Apache-2.0**). The attestation format
    (`subject` + `predicate` + signed envelope, DSSE) *can* carry telemetry-provenance predicates, but
    **no published in-toto predicate type for telemetry exists** — this would be novel work.
  - **sigstore/rekor** — **VERIFIED Apache-2.0**. Transparency log; the natural place to anchor
    signed-telemetry-batch digests if you build the mechanism.
- **Flag:** RFC 5848 **SAFE TO CITE/VENDOR-AS-PROVISION**; in-toto/Rekor **SAFE TO VENDOR (Apache-2.0)**
  as mechanism, but **there is no existing test material for detecting spoofed or unsigned telemetry
  payloads.** That is a second genuine gap DCVigil can fill.

### 3.5 mTLS test material

- **Netflix BetterTLS** — https://github.com/Netflix/bettertls. "A collection of test suites for TLS
  clients", covering **name constraints** and **certificate path building** — exactly the failure modes
  that bite agent↔server mTLS at scale. Go-based harness (`go run ./cmd/bettertls`), each test is a
  generated cert chain with an expected accept/reject.
  **Licence: VERIFIED — Apache-2.0** (`master` branch `LICENSE`; note the default branch is `master`,
  not `main`). **Test-case count UNVERIFIED** (the suites are generated, not a fixed file list).
  **Flag: SAFE TO VENDOR (Apache-2.0).** Best-fit external suite for §3 by a wide margin.
- **tlsfuzzer** — https://github.com/tlsfuzzer/tlsfuzzer. **Licence: VERIFIED — GPLv2** (`LICENSE`,
  "GNU GENERAL PUBLIC LICENSE Version 2"). Server-side TLS conformance/fuzzing scripts.
  **Flag: REFERENCE-ONLY** for a permissive corpus (copyleft).

---

## 4. Automated remediation guardrails and blast radius

### 4.1 Kubernetes PodDisruptionBudget eviction tests — **the best blast-radius oracle available**

- **URL:** https://github.com/kubernetes/kubernetes/blob/master/pkg/registry/core/pod/storage/eviction_test.go
- **Contents (verified by fetching the file):** 1,091 lines, **39 named table-driven cases** across
  four test functions, each with an explicitly declared fact/disposition struct:
  ```go
  func TestEviction(t *testing.T) {
      testcases := []struct {
          name     string
          pdbs     []runtime.Object
          policies []*policyv1.UnhealthyPodEvictionPolicyType
          eviction *policy.Eviction
          expectError         string
          podPhase            api.PodPhase
          podName             string
          expectedCause       metav1.CauseType
          expectedDeleteCount int
          podTerminating      bool
          prc                 *api.PodCondition
      }{ ... }
  }
  ```
  and `TestEvictionPDBStatus` carries `expectedDisruptionsAllowed int32` + `expectedReason string`.
  Verified case names read like corpus rows already:
  - "matching pdbs with no disruptions allowed, pod running"
  - "matching pdbs with disruptions allowed"
  - "non-matching pdbs"
  - "matching pdbs with no disruptions allowed, pod terminating"
  - "matching pdbs with no disruptions allowed, pod running, pod unhealthy, unhealthy pod ours, skips the PDB check and deletes"
  - "pdbs No disruptions allowed, pod pending, first delete conflict, pod becomes running, continueToPDBs"
- **Licence:** **VERIFIED — Apache-2.0** (file header: "Copyright 2019 The Kubernetes Authors.
  Licensed under the Apache License, Version 2.0"; repo `LICENSE` likewise Apache-2.0).
- **Ground truth:** yes — `expectError` (the 429 `TooManyRequests` / `DisruptionBudget` cause) and
  `expectedDeleteCount`.
- **Companion:** `pkg/controller/disruption/disruption_test.go` — **verified 24 `func Test*`** covering
  `disruptionsAllowed` computation. `test/e2e/apps/disruption.go` adds e2e coverage.
- **Reuse path — near-verbatim:**
  `case id` ← `name`; `provisions engaged` ← `{availability-budget, eviction-api}`;
  `boolean factor facts` ← `{pdb_matches_target, disruptions_allowed_gt_zero, pod_terminating,
  pod_unhealthy, pod_owned_by_workload, policy_allows_unhealthy_eviction}`;
  `expected disposition` ← allow-delete / **deny with `DisruptionBudget` cause** / conflict-retry.
  **This is the canonical encoding of "the automated remediator must not exceed the availability
  budget", with an upstream-maintained oracle.**
- **Flag:** **SAFE TO VENDOR (Apache-2.0).** Top pick for the remediation lane.

### 4.2 "Halt after N actions" invariants — where they actually exist

I checked each candidate's API types directly. **Verified findings:**

| Project | Verified field(s) | Semantics | Licence |
|---|---|---|---|
| **Argo Rollouts** (`pkg/apis/rollouts/v1alpha1/analysis_types.go`) | `FailureLimit`, `InconclusiveLimit`, `ConsecutiveErrorLimit`, `Count`, `SuccessCondition`, `FailureCondition` | "**FailureLimit is the maximum number of times the measurement is allowed to fail, before the** [analysis run is considered failed]"; `ConsecutiveErrorLimit` = max consecutive *errors*. Test coverage: **62 `func Test*` in `analysis/analysis_test.go`** (verified). | **VERIFIED Apache-2.0** |
| **Flagger** (`pkg/apis/flagger/v1beta1/canary.go`) | `Threshold` ("returns the canary threshold (default 1)"), `MaxWeight`, `StepWeight`, `StepWeights`, `StepWeightPromotion`, `Iterations`, `PrimaryReadyThreshold` (=100), `CanaryReadyThreshold` (=100), `ThresholdRange` | Max failed checks before automated rollback; step-wise traffic ceiling. | **VERIFIED Apache-2.0** |
| **Chaos Mesh** (`api/v1alpha1/statuscheck_types.go`) | `FailureThreshold` ("minimum consecutive failure"), `SuccessThreshold`, `IntervalSeconds`, `RecordsHistoryLimit`, modes `Synchronous`/`Continuous`, conditions `FailureThresholdExceed`/`SuccessThresholdExceed`, reason `StatusCheckFailureThresholdExceed` | **A first-class "abort the experiment once N consecutive checks fail" object** — the closest thing in open source to an explicit halt invariant with a named condition. | **VERIFIED Apache-2.0** |
| **LitmusChaos** (`chaos-operator` `chaosengine_types.go`) | `Probe []ProbeAttributes` with `k8sProbe`, `httpProbe`, `cmdProbe`, `promProbe`, `sloProbe`, each with `RunProperty` (timeout, **retry**, interval) and a `mode` | Probe outcome gates experiment verdict. Retry counts are the halt knob. | Litmus repo **VERIFIED Apache-2.0**; `chaos-operator` licence **UNVERIFIED** separately |
| **Chaos Toolkit** (`chaoslib/hypothesis.py`) | **steady-state hypothesis** with per-probe `tolerance` (bool / int / list / str / dict; dict types: `probe`, `regex`, `jsonpath`, `range`) | If the steady-state hypothesis deviates, the experiment is aborted. Declarative, JSON/YAML-authored. | `chaostoolkit` **VERIFIED Apache-2.0**; `chaostoolkit-lib` **VERIFIED Apache-2.0** |
| **resilience4j** | `CircuitBreakerStateMachineTest` — **36 `@Test`** methods (verified); config `failureRateThreshold`, `slidingWindowSize`, `minimumNumberOfCalls`, `permittedNumberOfCallsInHalfOpenState` | Classic CLOSED→OPEN→HALF_OPEN state machine with an explicit "N calls then trip" contract. | **VERIFIED Apache-2.0** (`LICENSE.txt`) |
| **Polly** (.NET) | Circuit breaker `handledEventsAllowedBeforeBreaking`; rate limiter, retry, timeout, bulkhead strategies | Same shape in .NET. | **VERIFIED BSD-3-Clause** (`LICENSE`, "Copyright (c) 2015-2025, App vNext") |
| **Hystrix** (legacy/maintenance) | `circuitBreaker.requestVolumeThreshold`, `errorThresholdPercentage` | Historical reference only; project is not maintained. | **VERIFIED Apache-2.0** (`LICENSE-2.0.txt`) |
| **AWS FIS** | Stop conditions bound to CloudWatch alarms | Proprietary managed service; documentation only. | **Not open source. REFERENCE-ONLY.** |

**Answer to the brief's question:** yes — **Chaos Mesh's `StatusCheck.FailureThreshold` /
`StatusCheckFailureThresholdExceed`** and **Argo Rollouts' `FailureLimit` / `ConsecutiveErrorLimit`**
are genuine, testable, Apache-2.0 encodings of a "halt after N" invariant, and both ship with their
own test suites. Use Argo Rollouts' 62 analysis tests as the oracle; use Chaos Mesh's condition
vocabulary for naming.

### 4.3 Detection vocabularies

- **Falco rules** — https://github.com/falcosecurity/rules. **Licence: VERIFIED — Apache-2.0**, both
  at repo root (`LICENSE`) and as a per-file SPDX header inside the rules YAML itself
  (`# SPDX-License-Identifier: Apache-2.0 / Copyright (C) 2025 The Falco Authors`). **Permissive —
  this is the important licence difference from Sigma.**
  **Volume (verified by counting `^- rule:`):** `falco_rules.yaml` **25** (stable),
  `falco-incubating_rules.yaml` **31**, `falco-sandbox_rules.yaml` **39** — **95 rules total** across
  the three maturity tiers.
  **Directly on-scope rules (verified present):** `Linux Kernel Module Injection Detected`,
  `BPF Program Not Profiled`, `Launch Privileged Container`, `Launch Excessively Capable Container`,
  `Change thread namespace`, `Change namespace privileges via unshare`,
  `Detect release_agent File Container Escapes`, `Debugfs Launched in Privileged Container`,
  `Set Setuid or Setgid bit`, `Non sudo setuid`, `PTRACE attached to process`,
  `Potential Local Privilege Escalation via Environment Variables Misuse`,
  `Read sensitive file trusted after startup` / `untrusted`, `Clear Log Activities`,
  `Delete or rename shell history`, `Create Symlink/Hardlink Over Sensitive Files`,
  `Fileless execution via memfd_create`, `Contact cloud metadata service from container`,
  `Backdoored library loaded into SSHD (CVE-2024-3094)`.
  **Reuse path:** each rule's `condition` is already a boolean expression over syscall-level facts —
  i.e. **an executable factor-fact definition**. Map rule → provision; rule condition → factor facts;
  rule `priority` → disposition severity. **Flag: SAFE TO VENDOR (Apache-2.0).**
- **Sigma rules** — https://github.com/SigmaHQ/sigma. **Licence: VERIFIED, and it is NOT a standard
  OSI licence.** The repo `LICENSE` states: the **specification and logo are public domain**; the
  **rules are released under the Detection Rule License (DRL) 1.1**. I read DRL 1.1 in full from
  https://github.com/SigmaHQ/Detection-Rule-License: it is MIT-like (use, copy, modify, merge,
  publish, distribute, sublicense, sell) **with two additional obligations**: (1) on redistribution
  you must retain the `author` field, a URI/hyperlink to the rule set, and an indication that the
  rules are DRL-licensed; (2) **when you *use* the rules on data, alert messages produced by matches
  must retain the author attribution** if supplied in the rule.
  **Volume:** README states "more than 3000 detection rules"; categories are
  `rules/`, `rules-threat-hunting/`, `rules-emerging-threats/`, `rules-compliance/`,
  `rules-placeholder/`. Exact count UNVERIFIED (GitHub tree listing was blocked at the time of this survey).
  **Flag: VENDORABLE BUT WITH A NON-STANDARD OBLIGATION.** The "attribution must survive into runtime
  alert output" clause (2) is unusual and has to be honoured by the *product*, not just the repo.
  Legal should sign off before Sigma rules go into a shipped corpus. Falco's plain Apache-2.0 is the
  lower-friction choice if you only need one vocabulary.
- **aquasecurity/tracee** signatures — **VERIFIED Apache-2.0**; a third, eBPF-native vocabulary.

---

## 5. Log-parser sandboxing and ReDoS

### 5.1 Labelled ReDoS corpora

- **Davis et al., "The Impact of ReDoS in Practice: an Empirical Study at the Ecosystem Scale"
  (ESEC/FSE 2018) artifact** — https://zenodo.org/records/1294301
  - **Contents (verified from the Zenodo record):** code for analysing regexes along four dimensions
    (super-linear performance detection, vulnerability assessment, semantics, anti-patterns); a dataset
    of **unique regexes collected from npm and PyPI modules**, released raw without source attribution
    for security reasons; and the `vuln-regex-detector` tool.
  - **Licence: VERIFIED — CC-BY-4.0** (stated on the Zenodo record page).
  - **Volume:** artifact archive 15.5 MB; 2.8 GB across all versions. Exact regex count not stated on
    the record page — **UNVERIFIED**.
  - **Ground truth:** partial — regexes are labelled super-linear/not by the paper's detectors, and
    the pipeline includes a **validation stage** that confirms detector output by actually running the
    "evil input" in the target language. That validation step is what makes the labels defensible.
  - **Flag: SAFE TO VENDOR (CC-BY-4.0)** with attribution to Davis, Coghlan, Servant, Lee (Virginia Tech).
    **This is the labelled catastrophic-backtracking corpus the brief asked for.**
- **davisjam/vuln-regex-detector** — https://github.com/davisjam/vuln-regex-detector.
  **Licence: VERIFIED — MIT** (`LICENSE`, "Copyright (c) 2018-present Jamie Davis"). Three-stage
  pipeline: *extract* regexes from source → *detect* vulnerability (ensemble of detectors) → *validate*
  by executing the generated evil input in the target language. Each detector emits the attack string
  it believes triggers catastrophic backtracking — **so every positive case comes with a witness.**
  **Flag: SAFE TO VENDOR (MIT).** The witness string is your `expected disposition` evidence.
- **ReDoSHunter** (USENIX Security '21) — https://github.com/yetingli/ReDoSHunter.
  **Licence: VERIFIED ABSENT — there is no LICENSE file** (checked both `main` and `master`), and the
  README imposes bespoke terms: new CVEs found with the tool "**need to be co-owned by the major
  author**" and "the **profit** from exposing new CVEs using ReDoSHunter should also [be]
  half-preserved by ReDoSHunter authors."
  **Flag: REFERENCE-ONLY — DO NOT VENDOR, DO NOT USE IN A COMMERCIAL PIPELINE.** Cite the paper's
  taxonomy (NQ, EOD, POA, SLQ, NSQ vulnerability patterns) only. This is the one trap in this lane.
- **s2e-lab/RegexEval** (ICSE-NIER'24, "Re(gEx|DoS)Eval") — **licence UNVERIFIED** (no `LICENSE` at
  `main`). **REFERENCE-ONLY** pending check.

### 5.2 ReDoS detectors with reusable test material

| Tool | URL | Licence | Notes |
|---|---|---|---|
| **recheck** | github.com/makenowjust-labs/recheck | **VERIFIED MIT** (`LICENSE` + README "License: MIT License. 2020-2025 (C) TSUYUSATO Kitsune") | "The trustworthy ReDoS checker"; hybrid automaton + fuzzing; Scala core with JS/npm bindings. Best-maintained. **SAFE TO VENDOR.** |
| **redos-detector** | github.com/tjenkinson/redos-detector | **VERIFIED MIT** (`LICENSE`, "Copyright (c) 2020 Tom Jenkinson") | Produces a **numeric score** = max number of ambiguous paths, not a boolean. Score `1` ⇒ provably no backtracking. ECMA-262 semantics only. **SAFE TO VENDOR.** A numeric score is a *better* corpus disposition than a boolean — it supports a threshold provision ("reject regexes with score > N"). |
| **safe-regex** (davisjam fork, the maintained one) | github.com/davisjam/safe-regex | **VERIFIED MIT** (`package.json` `"license": "MIT"` and `LICENSE` "released under the MIT license") | Star-height heuristic. Fast, high false-positive rate. **SAFE TO VENDOR.** |
| **safe-regex** (fastify fork) | github.com/fastify/safe-regex | **VERIFIED MIT** (`package.json`) | Maintained variant. |
| **regexploit** (Doyensec) | github.com/doyensec/regexploit | **VERIFIED Apache-2.0** (`LICENSE`) | Finds inputs causing exponential backtracking; strong at generating the attack string. **SAFE TO VENDOR.** |

**Ensemble insight:** the detectors disagree, and their disagreements are labelled by
`vuln-regex-detector`'s validation stage. A corpus case of the form "regex R, detectors {safe-regex:
unsafe, recheck: safe, redos-detector: score 3}, validated: not exploitable in Go's RE2" is a
*genuinely hard* adjudication case — exactly what a compliance corpus needs to be non-trivial.

### 5.3 Sandbox isolation for user-supplied parsing scripts

| Source | URL | Licence | Test material |
|---|---|---|---|
| **gVisor** | github.com/google/gvisor | **VERIFIED Apache-2.0** | **`test/syscalls/` — verified 251 `syscall_test(` targets** in `test/syscalls/BUILD`, and ~562 `cc_binary`/`name =` entries in `test/syscalls/linux/BUILD`. This is a large, independent Linux-syscall-compatibility oracle: each test asserts the *expected kernel behaviour* that the sandbox must reproduce. **SAFE TO VENDOR.** Best-in-class for "does the sandbox faithfully and safely emulate the syscall surface the parser needs?" |
| **Docker/moby default seccomp profile** | github.com/moby/moby (`profiles/seccomp/default.json`) | **VERIFIED Apache-2.0** (repo `LICENSE`) | A concrete, widely-deployed allowlist: ~`SCMP_ACT_ERRNO` default with an explicit allowed-syscall set. **SAFE TO VENDOR.** Directly usable as the reference "what a log-parser sandbox should permit". |
| **libseccomp** | github.com/seccomp/libseccomp | **VERIFIED LGPL-2.1** (`LICENSE`, "GNU LESSER GENERAL PUBLIC LICENSE Version 2.1") | Extensive `tests/` tree. **REFERENCE-ONLY for a permissive corpus** (copyleft), though LGPL linking is usually fine for the *library*; the test fixtures are the copyleft concern. |
| **Wasmtime** | github.com/bytecodealliance/wasmtime | **VERIFIED Apache-2.0 WITH LLVM-exception** — the `LICENSE` file contains the Apache 2.0 text plus, at line 205, `--- LLVM Exceptions to the Apache 2.0 License ----`. **Record the exception; it is not plain Apache-2.0.** | Wasm is the strongest isolation story for user-supplied parsing logic (deterministic, no ambient authority, capability-based via WASI). **SAFE TO VENDOR** (note the exception in your SPDX manifest as `Apache-2.0 WITH LLVM-exception`). |
| **wasi-testsuite** | github.com/WebAssembly/wasi-testsuite | **VERIFIED Apache-2.0** (`LICENSE`) | Conformance tests for WASI runtimes, with per-test JSON manifests of expected exit codes/stdout. Clean `(case, facts, expected)` shape. **SAFE TO VENDOR.** |

### 5.4 Real log-parser implementations worth mining for parser-hardening provisions

- **Vector** — github.com/vectordotdev/vector. **Licence: VERIFIED — MPL-2.0** (`LICENSE`, "Mozilla
  Public License, version 2.0"). File-level copyleft. **REFERENCE-ONLY** for vendoring test fixtures
  into a permissive corpus; fine to cite. Its VRL (Vector Remap Language) is a purpose-built,
  *deliberately non-Turing-complete* parsing DSL — the strongest existing argument that "user-supplied
  parsing logic must be expressed in a total language" is a shippable control, not an aspiration.
- **Fluent Bit** — github.com/fluent/fluent-bit. **Licence: VERIFIED — Apache-2.0.** Its regex parser
  is Onigmo-based (backtracking) — i.e. **ReDoS-exposed by construction**, which makes it the canonical
  worked example for the corpus's regex-complexity provision. **SAFE TO VENDOR.**

---

## 6. Rate limiting / self-inflicted DDoS

### 6.1 Incident write-ups (all REFERENCE-ONLY unless noted)

- **danluu/post-mortems** — https://github.com/danluu/post-mortems. Large curated index of public
  postmortems including retry-storm and cascading-failure incidents.
  **Licence: VERIFIED ABSENT — no `LICENSE` file at `master` (404).** **REFERENCE-ONLY: cite links,
  do not vendor text.**
- **Google Cloud CRE Life Lessons, "How to avoid a self-inflicted DDoS attack"** —
  https://cloud.google.com/blog/products/gcp/how-to-avoid-a-self-inflicted-ddos-attack-cre-life-lessons/
  Canonical vendor-authored treatment. **Proprietary blog content — REFERENCE-ONLY.**
- **Cloudflare, 12 Sept 2025 dashboard/API outage deep dive** —
  https://blog.cloudflare.com/deep-dive-into-cloudflares-sept-12-dashboard-and-api-outage/
  A dashboard component's retry behaviour amplified into an API outage — i.e. **the control plane
  DoS'd its own API**, which is precisely the DCVigil scenario. **REFERENCE-ONLY.**
- **RetryGuard: Preventing Self-Inflicted and Attack-Driven Retry Storms in Cloud Applications** —
  arXiv:2511.23278. Recent academic treatment with a defined threat model. **Licence per arXiv
  posting — UNVERIFIED; check the paper's licence line before quoting at length.**
- **Google SRE Book/Workbook**, "Addressing Cascading Failures" and **AWS Builders' Library**,
  "Timeouts, retries, and backoff with jitter" — free to read, **not openly licensed. REFERENCE-ONLY.**

### 6.2 Reusable *test* material for rate limiting

| Source | Licence | What it gives you |
|---|---|---|
| **k8s `client-go` `util/workqueue/default_rate_limiters_test.go`** | **VERIFIED Apache-2.0** (k8s repo) | **Verified 5 tests:** `TestItemExponentialFailureRateLimiter`, `TestItemExponentialFailureRateLimiterOverFlow`, `TestItemFastSlowRateLimiter`, `TestMaxOfRateLimiter`, `TestWithMaxWaitRateLimiter`. Each asserts the **exact backoff delay sequence** for a given failure sequence — a deterministic `(facts → disposition)` table for "does the remediation controller back off correctly?" **SAFE TO VENDOR.** The `OverFlow` test is the one that matters: it pins the behaviour when the exponential counter saturates, which is exactly the retry-storm boundary. |
| **k8s API Priority and Fairness (APF)**, `staging/src/k8s.io/apiserver/pkg/util/flowcontrol/` | **VERIFIED Apache-2.0** | Server-side fair queuing + concurrency shares; `apf_filter_test.go` (verified 1 top-level `func Test`, heavily parameterised) plus the `fairqueuing` package's own tests. This is the **upstream answer to "a fleet of agents must not starve the control plane"** — PriorityLevelConfiguration / FlowSchema are literally the provisions. **SAFE TO VENDOR.** |
| **Envoy `ratelimit`** service | **VERIFIED Apache-2.0** (`LICENSE`) | Reference gRPC rate-limit service with a descriptor-based config language (domain → descriptors → `requests_per_unit`). Config is declarative and testable. **SAFE TO VENDOR.** |
| **resilience4j** RateLimiter + CircuitBreaker + Retry | **VERIFIED Apache-2.0** | 36 verified `@Test` in the circuit-breaker state-machine test alone; RateLimiter and Retry have parallel suites. **SAFE TO VENDOR.** |
| **Polly** | **VERIFIED BSD-3-Clause** | .NET equivalent; rate limiter, circuit breaker, retry with jitter, bulkhead isolation. **SAFE TO VENDOR.** |

**Alert-webhook amplification** specifically: no open test corpus found. Alertmanager's grouping /
inhibition / silence semantics (`prometheus/alertmanager`, licence UNVERIFIED at the time of this survey — check
before use) are the mechanism, but there is no published suite for "did the alerting layer amplify a
single fault into N thousand webhook calls". **Third genuine gap.**

---

## 7. Safe-to-vendor vs reference-only — consolidated

### SAFE TO VENDOR (permissive, licence read when this survey was compiled)

| Source | Licence (VERIFIED) |
|---|---|
| PREVAIL `test-data/*.yaml` | MIT |
| bpf_conformance | MIT |
| recheck | MIT |
| redos-detector | MIT |
| safe-regex (davisjam / fastify) | MIT |
| vuln-regex-detector | MIT |
| cilium/ebpf | MIT |
| Kubernetes (eviction/PDB/APF/workqueue tests) | Apache-2.0 |
| Argo Rollouts | Apache-2.0 |
| Flagger | Apache-2.0 |
| Chaos Mesh | Apache-2.0 |
| LitmusChaos | Apache-2.0 |
| Chaos Toolkit + chaostoolkit-lib | Apache-2.0 |
| resilience4j | Apache-2.0 |
| Hystrix (legacy) | Apache-2.0 |
| Falco + falcosecurity/rules | Apache-2.0 |
| Tracee | Apache-2.0 |
| bpftrace | Apache-2.0 |
| bcc | Apache-2.0 |
| little-vm-helper | Apache-2.0 |
| syzkaller | Apache-2.0 |
| gVisor (`test/syscalls`) | Apache-2.0 |
| moby default seccomp profile | Apache-2.0 |
| wasi-testsuite | Apache-2.0 |
| Envoy ratelimit | Apache-2.0 |
| SPIRE | Apache-2.0 |
| OTel Collector (+contrib, spec) | Apache-2.0 |
| OpAMP spec + opamp-go | Apache-2.0 |
| in-toto + in-toto/attestation | Apache-2.0 |
| sigstore/rekor | Apache-2.0 |
| Netflix BetterTLS | Apache-2.0 |
| regexploit | Apache-2.0 |
| Fluent Bit | Apache-2.0 |
| Wasmtime | **Apache-2.0 WITH LLVM-exception** (record the exception) |
| Polly | BSD-3-Clause |
| libbpf-bootstrap | BSD-3-Clause |
| libbpf | LGPL-2.1-only **OR** BSD-2-Clause (elect BSD-2-Clause) |
| GitHub Advisory Database | CC-BY-4.0 (attribution required) |
| Davis et al. ReDoS Zenodo artifact | CC-BY-4.0 (attribution required) |
| Sigma rules | **DRL 1.1** — vendorable but carries a *runtime* attribution obligation; get legal sign-off |

### REFERENCE-ONLY

| Source | Reason |
|---|---|
| Linux BPF verifier selftests | GPL-2.0 (extract taxonomy, re-author reproducers) |
| LTP | GPL-2.0 |
| tlsfuzzer | GPL-2.0 |
| systemd tests | LGPL-2.1 |
| polkit | GNU Library GPL v2 |
| libseccomp tests | LGPL-2.1 |
| Vector | MPL-2.0 (file-level copyleft) |
| **ReDoSHunter** | **No licence + author-imposed CVE co-ownership and profit-sharing terms — do not use commercially** |
| SplunkWhisperer2 | Licence unverified; offensive tooling |
| PipeViewer | Licence unverified |
| bpfvet, RegexEval | Licence unverified |
| OSV.dev *aggregated data* | Data licence unverified (code is Apache-2.0) |
| danluu/post-mortems | No licence file |
| Google CRE blog, AWS Builders' Library, SRE Book, Cloudflare blog | Proprietary |
| AWS FIS | Proprietary service |
| D-Bus reference implementation | Licence unverified at the time of this survey |
| Prometheus Alertmanager | Licence unverified at the time of this survey |

---

## 8. Proposed factor names

Factors are named so that each is a **boolean fact about the change under review**, phrased so that
`true` leans toward *non-conformance*. Provision ids are suggestions.

### 8.1 Privilege escalation via agent (`PROV-AGT-PRIV-*`)

- `agent_runs_as_root`
- `agent_holds_dangerous_capability` (CAP_SYS_ADMIN / CAP_BPF / CAP_SYS_MODULE / CAP_SYS_PTRACE)
- `agent_loads_kernel_module`
- `agent_loads_bpf_program`
- `change_widens_agent_capability_set`
- `agent_ipc_endpoint_added` (unix socket, named pipe, TCP loopback)
- `ipc_endpoint_world_writable` (**CWE-732** Incorrect Permission Assignment)
- `ipc_peer_identity_unverified` (no `SO_PEERCRED`/token check — **CWE-269** Improper Privilege Management)
- `privileged_action_reachable_from_unprivileged_caller`
- `agent_directory_writable_by_unprivileged_user` (**CWE-276** — the CVE-2025-61667 shape)
- `code_from_writable_path_executed_on_upgrade`
- `setuid_or_setgid_bit_introduced`
- `agent_execs_helper_with_inherited_privilege` (**CWE-250** Execution with Unnecessary Privileges)
- `privilege_not_dropped_after_bootstrap`
- `symlink_or_hardlink_target_unvalidated` (TOCTOU on agent-owned paths)
- `config_or_plugin_path_attacker_controlled`
- `windows_named_pipe_dacl_permissive`

### 8.2 Telemetry forgery (`PROV-TEL-INTEG-*`)

- `telemetry_transport_unencrypted`
- `server_certificate_not_verified`
- `client_certificate_not_presented` (no mTLS)
- `agent_identity_not_attested` (no SPIFFE/SPIRE-style node+workload attestation)
- `svid_or_credential_long_lived` (no rotation)
- `credential_shared_across_nodes` (a fleet-wide bearer token)
- `trust_on_first_use_without_pinning` (OpAMP TOFU without subsequent pinning)
- `telemetry_payload_unsigned`
- `payload_origin_unauthenticated` (RFC 5848 property 1)
- `payload_integrity_unverified` (RFC 5848 property 2)
- `payload_replay_possible` (RFC 5848 property 3)
- `sequence_gap_undetectable` (RFC 5848 properties 4–5)
- `ingest_accepts_unauthenticated_source`
- `tenant_attribution_derived_from_client_supplied_field` (cross-tenant spoofing)
- `clock_skew_unbounded_on_ingest`
- `agent_package_signature_unverified` (OpAMP `DownloadableFile.signature`)
- `remote_config_channel_unauthenticated`

### 8.3 Remediation blast radius (`PROV-REM-BLAST-*`)

- `remediation_executes_without_human_approval`
- `action_scope_unbounded_by_node_count`
- `action_scope_unbounded_by_tenant`
- `availability_budget_not_consulted` (no PDB / equivalent check)
- `eviction_proceeds_when_disruptions_allowed_is_zero`
- `unhealthy_pod_policy_bypasses_budget`
- `no_halt_after_n_actions` (**the core invariant** — no `FailureLimit` / `FailureThreshold` analogue)
- `no_consecutive_error_limit`
- `no_rate_ceiling_on_actions_per_interval`
- `no_canary_or_staged_rollout` (no `StepWeight` / `MaxWeight` analogue)
- `no_automatic_rollback_on_analysis_failure`
- `steady_state_hypothesis_absent` (Chaos Toolkit shape)
- `success_criteria_not_machine_checkable`
- `action_not_idempotent`
- `action_irreversible`
- `remediation_can_target_the_monitoring_control_plane_itself` (reflexive blast radius)
- `concurrent_remediations_uncoordinated`
- `dry_run_path_absent`
- `kill_switch_absent`

### 8.4 Regex and parser sandboxing (`PROV-PARSE-SBX-*`)

- `user_supplied_regex_accepted`
- `regex_engine_is_backtracking` (Onigmo/PCRE/RE2-absent — true for Fluent Bit's default)
- `regex_ambiguity_score_above_threshold` (redos-detector score > N)
- `regex_flagged_superlinear_by_validated_detector` (vuln-regex-detector, with witness input)
- `regex_star_height_exceeds_one` (nested quantifier — safe-regex heuristic)
- `regex_complexity_unbounded` (no static complexity budget)
- `input_length_unbounded_before_match`
- `match_execution_deadline_absent`
- `parser_runs_in_agent_address_space` (no process/namespace boundary)
- `parser_not_seccomp_confined`
- `parser_syscall_allowlist_absent`
- `parser_has_filesystem_access`
- `parser_has_network_access`
- `parser_language_is_turing_complete` (VRL-style totality argument fails)
- `parser_memory_limit_absent`
- `parser_cpu_quota_absent`
- `malformed_input_can_crash_agent` (the CVE-2026-44902 / CVE-2024-36129 shape)
- `decompression_ratio_unbounded` (zip-bomb — CVE-2024-36129)

### 8.5 Rate limiting and self-inflicted DoS (`PROV-RATE-SELFDOS-*`)

- `retry_without_bounded_attempts`
- `retry_backoff_absent`
- `retry_backoff_lacks_jitter`
- `retry_budget_absent` (no global cap on retry share of traffic)
- `exponential_backoff_saturation_unbounded` (the `...OverFlow` test's failure mode)
- `client_side_circuit_breaker_absent`
- `server_side_concurrency_limit_absent` (no APF/PriorityLevelConfiguration analogue)
- `no_priority_separation_between_agent_and_control_traffic`
- `synchronized_schedule_without_jitter` (thundering herd on a cron boundary)
- `reconnect_storm_on_server_restart`
- `cache_stampede_possible_on_expiry`
- `alert_fanout_unbounded`
- `webhook_amplification_factor_unbounded`
- `alert_grouping_or_inhibition_absent`
- `load_shedding_absent`
- `degraded_mode_absent`
- `failure_of_dependency_increases_request_rate` (the defining retry-storm signature)
- `internal_api_shares_quota_with_customer_traffic`

---

## 9. Gaps DCVigil should expect to author itself

1. **A monitoring-agent CVE corpus.** Does not exist. Build from GHSA (CC-BY-4.0).
2. **Test material for spoofed/unsigned telemetry.** No suite exists. RFC 5848's five properties give
   the factor vocabulary; the cases must be authored.
3. **Alert-webhook amplification tests.** No open suite.
4. **A CO-RE multi-kernel compatibility matrix.** Tooling exists (LVH + libbpf); the matrix does not.
5. **An "unprivileged caller ↔ privileged agent socket" suite.** Only adjacent material (polkit/D-Bus
   semantics, SPIRE attestation); the factor space is small enough to enumerate by hand.

---

## 10. Verification log (what was read, not inferred)

Raw `LICENSE`/`COPYING`/SPDX reads: linux-test-project/ltp, bpftrace, spire, opentelemetry-collector,
opentelemetry-collector-contrib, opentelemetry-specification, opamp-spec, opamp-go, SigmaHQ/sigma
(+ Detection-Rule-License full text), resilience4j, Polly, Netflix/Hystrix, litmuschaos/litmus,
chaos-mesh, chaostoolkit, chaostoolkit-lib, argo-rollouts, flagger, gvisor, in-toto, in-toto/attestation,
sigstore/rekor, makenowjust-labs/recheck, tjenkinson/redos-detector, davisjam/safe-regex,
fastify/safe-regex, davisjam/vuln-regex-detector, doyensec/regexploit, vbpf/prevail (+ per-file SPDX in
test-data), Alan-Jowett/bpf_conformance, cilium/ebpf, cilium/little-vm-helper, libbpf, libbpf-bootstrap,
iovisor/bcc, aquasecurity/tracee, falcosecurity/falco, falcosecurity/rules (+ in-file SPDX),
google/syzkaller, bytecodealliance/wasmtime (+ LLVM-exception at line 205), WebAssembly/wasi-testsuite,
seccomp/libseccomp, moby/moby, vectordotdev/vector, fluent/fluent-bit, envoyproxy/ratelimit,
kubernetes/kubernetes, polkit-org/polkit, systemd/systemd, Netflix/bettertls, tlsfuzzer,
github/advisory-database.

Verified-absent licences: ReDoSHunter (`main` and `master` 404), danluu/post-mortems (404),
s2e-lab/RegexEval (404), kernelci-core (404), kernel-patches/vmtest (404).

Measured counts (by fetching and counting, not by citation): 125 BPF verifier modules; 1,395
`__description`; 687 `__failure`; 1,169 `__success`; 238 `__failure_unpriv`; 254 `__success_unpriv`;
1,644 `__msg` with 1,084 distinct strings; 124+1 SPDX headers. 103 LTP `runtest/cve` entries.
39 named cases + 1,091 lines in k8s `eviction_test.go`; 24 tests in `disruption_test.go`; 5 tests in
`default_rate_limiters_test.go`. 62 tests in Argo Rollouts `analysis_test.go`. 36 tests in
resilience4j `CircuitBreakerStateMachineTest`. Falco 25 + 31 + 39 = 95 rules. gVisor 251
`syscall_test(` targets.

Not verified (flagged inline): OSV data licence; SPIRE integration-suite count; Sigma exact rule count;
BetterTLS case count; Davis artifact exact regex count; Splunk UF CVE details against the vendor portal;
CVE-2025-27237 CVSS/CWE; D-Bus and Alertmanager licences; chaos-operator licence separate from litmus.
