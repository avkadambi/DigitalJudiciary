# Sources: what was reusable, what was not, and why

Four independent surveys were run before a line of this corpus was written — observability standards and their conformance suites, AIOps datasets and root-cause benchmarks, privileged-agent and remediation security, and monitoring-specific compliance plus overhead benchmarking. The full reports are in `research/`. This document is the decision record.

Every licence below was verified by fetching the repository's own `LICENSE` file or the primary terms page. Where verification failed, the row says so. **A licence we could not verify is treated as reference-only.**

---

## 1. The six findings that shaped this corpus

**The seven-year retention claim rests on nothing external.** Verified across five instruments: NIST SP 800-53 AU-11 leaves the period organisation-defined; FedRAMP's own 2026 controls reference leaves AU-11 unfilled; PCI DSS says twelve months with three immediately available; HIPAA's six years covers *documentation*, not audit logs; SOC 2 sets no period at all. Immutability, by contrast, is well grounded — AU-9 and AU-9(3), public domain and quotable. The shipped provision fuses the two. That is draft amendment **PA-02**, and it is the single most useful thing these surveys produced.

**All three audit regimes are unusable as provision text.** The AICPA Trust Services Criteria are not paywalled but are account-gated, under AICPA copyright, with no reuse grant found. ISO/IEC 27001 and 27002 are paywalled at CHF 155 and ISO additionally **prohibits use of its content for AI/ML training** — a direct hazard for a corpus meant to evaluate agents. PCI DSS v4.0.1 downloads free under a personal, non-commercial, no-redistribution licence. Only their identifiers are cited here. The open substitute throughout is NIST SP 800-53 via `usnistgov/oscal-content`, verified **CC0**, from which AU-9, AU-9(2), AU-9(3), AU-11, IA-2, IA-2(1)/(2)/(8), SC-8 and SC-8(1) were taken directly.

**No standard governs software that actuates datacenter cooling or power.** IEC 62443-3-3 is paywalled at CHF 380; ASHRAE's Thermal Guidelines are a commercial book; Uptime Institute's Tier terms could not be read (robots.txt); NFPA's free-access scope is unverified. The one freely citable anchor is **OSHA 29 CFR §1910.147**, lockout/tagout — software that can remotely re-energise equipment is a path around it. That is why DV-302's floor is stated on safety grounds and DV-340 extends it to physical access control by analogy rather than by citation.

**NIS2's clock is not one clock.** The transposition deadline was 17 October 2024. Four member states met it; infringement procedures were opened against twenty-three in November 2024; reasoned opinions issued to nineteen in 2026. A provision stating a hard EU 24-hour early-warning deadline is legally wrong in most member states today. That is **PA-05**, and `DV-407` carries the transposed form as a `deferred` provision meanwhile.

**No curated corpus of monitoring-agent vulnerabilities exists.** Searched for specifically; only general datasets were found. The substrate is the **GitHub Advisory Database (CC BY 4.0)**, from which the AP family's factors were built — verified seeds include CVE-2025-61667 (Datadog agent, CWE-276, a writable `__pycache__` executed on upgrade) and CVE-2024-36129 (OpenTelemetry Collector decompression bomb).

**A "<1% CPU" claim is unfalsifiable as usually stated.** No vendor-neutral overhead benchmark exists — only vendor blogs. The claim needs a denominator, a workload, a configuration, a window, a statistic and a mechanism. Two mechanisms matter: cgroup v2 `cpu.stat`, where `throttled_usec > 0` is a monitoring-*integrity* failure and not merely a performance one; and separate accounting for eBPF program time, because **it is charged to the triggering process, not to the agent's cgroup**, which is the commonest way such a claim is wrong. That is the whole RS family.

---

## 2. What this corpus actually reuses

Nothing is redistributed. What was reused is **structure** and **identifiers**, which are facts.

| Source | Licence (verified) | How it is used here |
| :---- | :---- | :---- |
| NIST SP 800-53 via `usnistgov/oscal-content` | **CC0** (LICENSE.md read) | DV-339, DV-343, DV-396, DV-412 take AU-9, AU-9(2), AU-9(3), IA-2, SC-8(1) control text directly. |
| EU AI Act, GDPR, NIS2 Dir. 2022/2555, Data Act | CC BY 4.0 via Decision 2011/833/EU | The DR and EV families; the shipped DV-330 to DV-336 block. |
| Illinois BIPA, 740 ILCS 14/15 | US state statute, public | DV-338, the one new absolute with per-person statutory damages behind it. |
| OSHA 29 CFR 1910.147 | US CFR, public domain | The actuation floor's only freely citable anchor. |
| **promtool rule unit tests** | Apache-2.0 | DV-394, and the format is the closest existing analogue to this corpus's own case shape: `input_series` are factor facts, `alertname` is the provision, `exp_alerts` is the disposition. `promtool test rules` is an executable oracle. |
| OpenTelemetry semantic conventions | Apache-2.0 | The TL family's attribute vocabulary. Stability levels matter: `hw.*` and `system.*` are Development, so DV-347 requires the level to be recorded. |
| OTel `redactionprocessor` counters | Apache-2.0 | DV-399. `redaction.masked.count` and `redaction.redacted.count` are built-in machine-checkable evidence that masking ran. |
| OTel Collector security best practices | Apache-2.0 | DV-353. RFC-2119 normative text, ready to become provisions. |
| OpAMP `DownloadableFile.signature` | Apache-2.0 | DV-359, DV-368. |
| Redfish Interop Validator and its schemas | BSD-3-Clause (validator); DMTF policy (schemas) | Resource names cited as identifiers. Its five-valued modality — Mandatory / Recommended / IfImplemented / Supported / Excluded — informed how provision status is expressed. |
| Linux BPF verifier selftests | GPL-2.0 — **taxonomy only** | The KS family. 1,395 named tests carry 1,084 distinct expected-rejection messages and 492 cases with **separate privileged and unprivileged verdicts** — the multi-tenant pattern DV-364 copies. No code taken. |
| PREVAIL | MIT | The permissive stand-in for the above, and what makes differential verifier testing possible. |
| Kubernetes PDB eviction tests; Argo Rollouts; Chaos Mesh `StatusCheck` | Apache-2.0 | DV-341, DV-383, DV-384, DV-387, DV-388. Argo's `ConsecutiveErrorLimit` and Chaos Mesh's `FailureThreshold` are the only explicit "halt after N" invariants with test suites found anywhere. |
| Davis et al. ReDoS artifact; `redos-detector`; `vuln-regex-detector` | CC BY 4.0; MIT; MIT | DV-350. The ambiguity *score* is what makes a threshold provision possible; a boolean would not. |
| gVisor, moby default seccomp | Apache-2.0 | DV-351. |
| RFC 5848 Signed Syslog Messages | IETF Standards Track | DV-367 — origin authentication, replay resistance and gap detection as four separate properties. |
| SPIFFE/SPIRE | Apache-2.0 | DV-366. Note: **SPIFFE has no conformance suite**. |
| GitHub Advisory Database | CC BY 4.0 | The AP family's factor vocabulary. |
| Falco rules | Apache-2.0 (verified twice) | Detection vocabulary — 95 rules including kernel-module injection and unprofiled BPF programs. |
| RCAEval; PetShop; Azure Public Dataset; NAB | MIT; CC BY 4.0; CC BY 4.0; MIT at HEAD | The AI family. RCAEval's separation of root-cause *service* from root-cause *indicator* is DV-379; NAB's Reward-Low-FP profile is DV-381; Azure's noise dataset is DV-378's noise floor. |
| TSB-AD; Wu and Keogh's benchmark critique | Apache-2.0 code; paper | DV-376 and DV-377. Point-adjusted F1 is discredited; VUS-PR is the threshold-free metric. |
| DeathStarBench, Train Ticket | Apache-2.0 | The licence-clean way to *generate* labelled cases: inject, and the injection record is the label. |
| Microsoft Presidio; gitleaks | MIT; MIT | DV-344's redaction vocabulary. |
| TSBS | MIT | DV-352. Seed-deterministic, so cases pin `(version, use-case, seed, scale)` rather than shipping data. |
| CWE | Royalty-free, attribution required | The AP family's classification. CWE™ is a trademark of The MITRE Corporation. |
| PACT (Okamoto and Erol 2026), Table 14 | cited | The nine pressure mechanisms in the P-pressure category. |

---

## 3. What was deliberately not used

| Source | Why not |
| :---- | :---- |
| AICPA Trust Services Criteria | Account-gated, AICPA copyright, no reuse grant. Identifiers only. |
| ISO/IEC 27001 / 27002 | Paywalled (CHF 155) and **ISO prohibits use of its content for AI/ML training**. Identifiers only. |
| PCI DSS v4.0.1 | Personal, non-commercial, no-redistribution licence. Requirement 10 identifiers and the 12-month figure as an oracle; no text. |
| IEC 62443-3-3, ASHRAE Thermal Guidelines, Uptime Institute Tier | Paywalled or terms unverified. |
| BACnet / ASHRAE 135 | Genuinely paywalled. |
| Modbus | Free download behind a click-through whose text could not be read. **Unverified — treated as non-redistributable.** |
| IPMI | Terms not stated; also frozen — the promoters stated in 2020 that no further updates should be expected, recommending Redfish. |
| **Yahoo S5 / Webscope** | Request-gated and academic-only; Webscope explicitly excludes commercial entities *and* employees of commercial entities holding university appointments. A vendor is categorically ineligible. |
| **LEMMA-RCA** | The site says CC BY-**ND** 4.0 and the repo LICENSE says CC BY-**NC** 4.0. Either clause blocks it. |
| Exathlon data, UCR Anomaly Archive, AIOps Challenge 2020 | Non-commercial or research-only. |
| **Loghub and Loghub-2.0** | Three README-versus-LICENSE conflicts were found and none is trivial: Loghub-2.0's GitHub badge shows MIT while the raw LICENSE is a custom research-or-academic text; Loghub's repo LICENSE says research-only while its Zenodo deposit says CC BY 4.0; GAIA ships GPL-2.0 while its README claims Apache-2.0. All three are reference-only. Loghub is also explicitly **not anonymised**. |
| Alibaba cluster traces | **No LICENSE file at all** (404); README prose only, survey-gated. |
| SMAP/MSL | Code Apache-2.0; **data licence unstated**. Also pre-scaled using test-set min/max, which leaks. |
| ClickBench | CC BY-**NC-SA** 4.0 — both clauses conflict. |
| **ReDoSHunter** | No LICENSE file on either branch, **and** the README demands CVE co-ownership and profit-sharing. |
| **Sigma rules** | The spec is public domain; the rules are DRL 1.1, under which attribution must survive **into runtime alert output**, not merely into the repository. Falco's plain Apache-2.0 was used instead. |
| `danluu/post-mortems`; The VOID | No LICENSE; terms unreadable. |
| OSV.dev data | Data licence unverified; GHSA pulled from `github/advisory-database` directly instead. |
| Copyleft: LTP, tlsfuzzer, systemd, polkit, libseccomp, Vector, diffoscope | GPL/LGPL/MPL — methodology referenced, no code. |
| Presidio's `presidio-research` corpus | It generates synthetic data; its identities come from Fake Name Generator under **CC BY-SA 3.0 US**, a share-alike trap. |

---

## 4. Gaps this corpus had to author around

1. **No monitoring-agent vulnerability corpus.** Built from GHSA.
2. **No spoofed-telemetry test suite.** RFC 5848 supplies the vocabulary; the fixtures do not exist.
3. **No labelled alert corpus for IT operations** anywhere — only security-SOC survey literature. That is why DV-380 requires a labelling protocol registered *before* the change rather than a target precision number.
4. **No labelled log corpus with PII ground truth.** Generate your own; Loghub is research-only and unanonymised.
5. **No CO-RE multi-kernel compatibility matrix**, though the tooling exists to build one.
6. **No unprivileged↔privileged agent-socket suite.** The factor space is small enough to enumerate by hand, and DV-354 through DV-356 do.
7. **No ingestion-rate or indexing-latency budget** is published anywhere. TSBS and ClickBench publish observations, not budgets. Any budget in a deployment is self-set and should be labelled as such.

## 5. A design finding worth carrying to the other packs

Three independent sources converged on the same shape: the OpenTelemetry compliance matrix leaves a cell **blank** for genuinely unknown, the Prometheus PromQL compliance tester reports **`unsupported`** as distinct from fail, and kselftest's TAP output carries **`SKIP` with a reason**. A conformance surface that cannot record *undetermined* forces false verdicts.

This corpus has one such value already — `none(tie)`, which Chapter 5 §4.6 keeps deliberately distinct from `none` so that a deadlock between incompatible authorities is recorded as a deadlock rather than as an absence of authority. The convergence is worth noting because it arrived from three unrelated engineering communities that had no theory of adjudication in view.
