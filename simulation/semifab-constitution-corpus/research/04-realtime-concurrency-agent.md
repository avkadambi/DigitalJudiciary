# Lane 04 — Reusable Open-Source Test Data: Real-Time/Latency, Memory & Concurrency Safety, Protocol Fuzzing, Cryptographic Policy, AI-Agent Code Defence

Research date: 2026-09-05. Target: an open compliance test corpus for software change in **semiconductor fab monitoring software**, whose cases have the shape:

    (case_id, provisions_engaged[], factor_facts{bool}, expected_disposition)

Out of scope here (already covered by the general AppSec survey): Juliet/SARD, CWE, CVEfixes, CyberSecEval, crAPI, AgentDojo/InjecAgent, OWASP Benchmark, OWASP standards.

**Licence discipline:** every licence below was read from the project's own LICENSE file, README licence statement, or repository licence metadata, and the source of the statement is named. Where a licence could not be verified it says **UNVERIFIED** and the source is marked REFERENCE-ONLY.

**Vendor/reference key**
- **VENDOR** — permissive or public-domain; safe to copy case data into the corpus with attribution/notice.
- **VENDOR (copyleft)** — redistributable, but the corpus (or at least that partition) inherits copyleft. Keep in a separately-licensed partition.
- **REFERENCE-ONLY** — cite, link, mirror structure/schema, or re-derive; do not copy the artefacts.

---

## 1. REAL-TIME / LATENCY

### 1.1 rt-tests (cyclictest, signaltest, pi_stress, hackbench, ptsematest, cyclicdeadline)
- **URL:** https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git — mirror: https://kernel.googlesource.com/pub/scm/utils/rt-tests/rt-tests.git
- **Contents:** the canonical POSIX real-time latency measurement harness. `cyclictest` measures wake-up latency of a periodic timer thread in microseconds and reports `Min/Act/Avg/Max` per CPU.
- **Format:** C source + CLI. Text summary, `-h/--histogram=US` emits a per-microsecond-bucket histogram; `-q/--quiet` prints "a summary only on exit. Useful for automated tests, where only the summary output needs to be captured" (Debian cyclictest(8) man page, verified).
- **Licence (VERIFIED):** **GPL-2.0**. The `COPYING` file at kernel.googlesource.com mirror is "GNU GENERAL PUBLIC LICENSE Version 2, June 1991".
- **Volume:** ~15 tools; no fixed case count — it is a harness, not a case set.
- **Ground truth:** none intrinsic. The oracle is supplied by the *budget*: `-b/--breaktrace=USEC` — "Send break trace command when latency > USEC" (man page, verified). That is the pass/fail predicate a provision can bind to.
- **Reuse path:** do **not** vendor the code. Vendor the *predicate shape*. Each corpus case becomes: factor `latency_budget_declared = true`, `measured_p100_exceeds_budget = true/false`, disposition `NONCONFORMING/CONFORMING`. cyclictest supplies the standard, citable definition of "wake-up latency, microseconds, max over N cycles" so the corpus does not have to invent one.
- **Flag:** **REFERENCE-ONLY** for code (GPL-2.0, and vendoring a measurement tool adds nothing). The measurement *definition* is a fact, not copyrightable.

### 1.2 rtla — Real-Time Linux Analysis (timerlat, osnoise) — the best threshold oracle in this lane
- **URL:** https://docs.kernel.org/tools/rtla/rtla-timerlat-top.html (source: `linux/tools/tracing/rtla`)
- **Contents:** in-kernel-tools latency analyser. `rtla timerlat` measures **IRQ timer latency** and **thread timer latency** separately, in microseconds, per CPU.
- **Format:** C, part of the Linux kernel tree. Text + tracing output.
- **Licence (VERIFIED):** **GPL-2.0** — documentation states rtla is "Free Software licensed under the GNU GPLv2" and it ships in the Linux kernel tree.
- **Volume:** n/a (tool).
- **Ground truth:** **explicit thresholds with a defined stop action**: `-i/--irq us` = "Stop trace if the IRQ latency is higher than the argument in us"; `-T/--thread us` = same for thread latency (verified in kernel docs). This gives a two-level budget — *interrupt* budget vs *task* budget — which is exactly the distinction fab monitoring software needs (sensor ISR vs control loop).
- **Reuse path:** the IRQ/thread split is the single most useful structural import for latency provisions. Model two separate factor facts rather than one, and two separate budgets.
- **Flag:** **REFERENCE-ONLY** (GPL-2.0 tool); import the *taxonomy*.

### 1.3 jitterdebugger
- **URL:** https://github.com/igaw/jitterdebugger
- **Contents:** a reimplementation of cyclictest with simplified options; starts a thread per CPU, programs a timer, measures wake-up duration. Ships `jitterplot` (histograms) and `jittersamples` (raw sample export). Source contains `jd_samples_csv.c` and `jd_samples_hdf5.c`.
- **Format:** C; **JSON by default** (per-CPU histograms with count/min/max/avg); CSV and HDF5 sample export; `jittersamples` emits semicolon-delimited `CPU;timestamp;latency`.
- **Licence (VERIFIED):** **MIT** — `LICENSE` reads "MIT License", Copyright 2018 Siemens AG.
- **Volume:** n/a (tool). No built-in threshold/break-on-threshold documented.
- **Reuse path:** **this is the vendorable latency harness.** MIT + JSON output means the corpus can ship a reference measurement runner and a machine-readable result schema without licence contamination. Its JSON histogram is a clean serialisation for `measured_latency_us` factor facts.
- **Flag:** **VENDOR** (MIT, retain Siemens AG notice).

### 1.4 HdrHistogram
- **URL:** https://github.com/HdrHistogram/HdrHistogram
- **Contents:** high dynamic range histogram; records counts of observed integer values at configurable significant-digit precision; percentile iteration; `.hlog` histogram log format via `HistogramLogProcessor`. Ports for C, C#/.NET, Python, JavaScript, Rust, Erlang, Go in sibling repos.
- **Format:** library + `.hlog` interval log format.
- **Licence (VERIFIED):** **dual CC0-1.0 / BSD-2-Clause.** `LICENSE.txt` states the code "is released to the public domain" under CC0 1.0 and "is also provided under the following license (commonly referred to as the BSD 2-Clause License)", and that the BSD grant "does not detract from the above stated release of the code into the public domain".
- **Volume:** n/a (library).
- **Ground truth:** n/a, but it **is** the citable open artefact for **coordinated omission**: `recordValueWithExpectedInterval()` — when a recorded value exceeds the expected sampling interval, the histogram "will reflect an appropriate number of additional values, linearly decreasing in steps" (README, verified).
- **Reuse path:** adopt `.hlog` as the corpus's latency evidence format; cite `recordValueWithExpectedInterval` as the normative correction. Provisions can then require *corrected* percentiles, making "uncorrected tail latency submitted as evidence" a distinct violation.
- **Flag:** **VENDOR** (CC0 — the cleanest licence in the whole lane).

### 1.5 wrk2 — the citable coordinated-omission artifact
- **URL:** https://github.com/giltene/wrk2
- **Contents:** Gil Tene's fork of `wrk`. Generates load at a **constant configured rate** (`-R/--rate`, default 1000 rps) and measures latency "from when a request *should* have been sent according to the constant throughput plan", not from when it was actually sent. README documents cases where correction reveals 99th-percentile latency ~200× larger than the uncorrected figure. Uses HdrHistogram for lossless recording.
- **Format:** C + Lua scripting; HdrHistogram percentile output.
- **Licence (VERIFIED):** **Apache-2.0** — `LICENSE` file is the Apache License, Version 2.0, January 2004.
- **Volume:** n/a.
- **Answer to the brief's question:** *yes* — **wrk2 (Apache-2.0) + HdrHistogram (CC0/BSD-2) together are the citable open artifact for coordinated omission.** Gil Tene's "How NOT to Measure Latency" talk is the informal source; these two repos are the licensable ones.
- **Flag:** **VENDOR** (Apache-2.0; NOTICE file must be carried).

### 1.6 LMbench
- **URL:** https://sourceforge.net/projects/lmbench/ ; mirror https://github.com/intel/lmbench
- **Contents:** "a suite of simple, portable, ANSI/C microbenchmarks for UNIX/POSIX... measures two key features: latency and bandwidth" (SourceForge project page, verified). Includes context-switch, memory-read and syscall latency micro-benchmarks.
- **Licence (VERIFIED, on the intel/lmbench mirror):** the mirror's `COPYING` is plain **GPL-2.0**, with no extra clause about publishing results. **Caveat:** historical lmbench distributions carried an additional non-standard restriction on publishing modified results; that clause is **not** present in the mirror's COPYING. **Verify the specific tarball you use.**
- **Reuse path:** low value here — its microbenchmarks measure the machine, not the software change under review. Mention only as prior art for microsecond-budget methodology.
- **Flag:** **REFERENCE-ONLY**.

### 1.7 OSADL QA Farm real-time latency data
- **URL:** https://www.osadl.org/OSADL-QA-Farm-Real-time.linux-real-time.0.html
- **Contents:** continuous worst-case latency monitoring; cyclictest-generated latency histograms and long-term latency plots per rack/slot system.
- **Licence (VERIFIED as NOT open):** the page carries "Open Source Automation Development Lab, (c) 2007-2024. **All rights reserved**". No open licence found for the data.
- **Flag:** **REFERENCE-ONLY.** Cite as evidence that long-term worst-case latency monitoring is established industry practice; do not copy the data.

### 1.8 PREEMPT_RT test suites
No separate, independently-licensed "PREEMPT_RT conformance suite" with pass/fail thresholds was found. In practice the RT community's conformance test *is* rt-tests + rtla run against a declared budget, plus the OSADL farm. **There is no published microsecond-budget conformance corpus with expected verdicts.** This is a genuine gap — and therefore the strongest argument for the corpus being novel in this lane.

---

## 2. MEMORY & CONCURRENCY SAFETY WITH GROUND TRUTH

### 2.1 SV-COMP / SV-Benchmarks — the flagship of this lane
- **URL (live):** https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks — archived GitHub mirror: https://github.com/sosy-lab/sv-benchmarks (archived Oct 2021, do not use) — **archived competition set:** https://zenodo.org/records/15012096 (DOI 10.5281/zenodo.15012096, version `svcomp25`)
- **Contents:** verification tasks: a C or Java program **plus** a `.yml` task definition **plus** a property file (`.prp`), with an **expected verdict**.
- **Format (VERIFIED against the normative BenchExec example, `doc/task-definition-example.yml`, Apache-2.0):**
  ```yaml
  format_version: "2.0"
  input_files: [ ... ]
  properties:
    - property_file: ../test/tasks/test.prp
      expected_verdict: false
      subproperty: valid-deref
    - property_file: ../test/tasks/other.prp
      expected_verdict: true
  ```
  BenchExec "will compare expected verdicts against actual verdicts". SV-COMP 2025 used **task-definition format version 2.1**.
- **Volume (VERIFIED from the SV-COMP 2025 TACAS report):** **34,700 total tasks** (33,353 C + 674 Java, plus a demo category ⇒ 34,027 non-demo). **ConcurrencySafety: 3,175 tasks, max score 5,733.** Subcategories: ConcurrencySafety-Main, ConcurrencySafety-MemSafety, ConcurrencySafety-NoOverflows, **NoDataRace-Main** (4 subcategories, from the SV-COMP 2025 benchmarks page). Other lanes of interest: MemSafety (5 subcategories), NoOverflows (2), SoftwareSystems (9).
- **Ground truth:** **yes — every task carries an `expected_verdict` boolean per property.** This is the single richest source of `(case, provision, expected disposition)` triples that exists.
- **Licence — READ CAREFULLY:**
  - **VERIFIED:** the Zenodo archive of the SV-COMP 2025 verification tasks is deposited under **CC-BY-4.0** (Zenodo record 15012096 licence field).
  - **VERIFIED:** the GitLab project page displays **Apache License 2.0** as the repository licence file.
  - **VERIFIED (policy):** the SV-COMP 2025 report states each task's licence must permit viewing/understanding/reverse engineering, modification, redistribution under the same terms, compilation and execution, and must "not exclude developers of commercial verifiers" — i.e. commercial use.
  - **UNVERIFIED and important:** the repository is a *heterogeneous* collection assembled over ~15 years (Linux device-driver derived tasks, `ntdrivers`, `ldv-*`, `systemc`, etc.). GitHub issue sosy-lab/sv-benchmarks#165 shows a 57-directory licence-review checklist that was still partly unchecked when that mirror was archived. **Do not treat "Apache-2.0" or "CC-BY-4.0" as covering every file.** GitLab raw/API access is blocked from this environment, so per-directory SPDX headers could not be enumerated.
- **Reuse path:** **the highest-value structural import in the entire study.** The `.yml` task-definition schema maps 1:1 onto the corpus case schema:
  | SV-COMP | corpus |
  |---|---|
  | task directory + `input_files` | `case_id` + artefact |
  | `properties[].property_file` (`.prp`) | `provisions_engaged` |
  | `properties[].subproperty` (e.g. `valid-deref`) | sub-provision / factor refinement |
  | `properties[].expected_verdict: true/false` | `expected_disposition` |
  Adopt this schema verbatim. It is already tool-supported (BenchExec), already versioned (2.0/2.1), and already has a normative spec at gitlab.com/sosy-lab/benchmarking/task-definition-format.
- **Flag:** **schema — VENDOR** (BenchExec doc file is Apache-2.0, SPDX header verified). **Task data — VENDOR ONLY PER-DIRECTORY after reading that directory's own licence headers.** Start with the crafted concurrency directories (`pthread`, `pthread-atomic`, `pthread-wmm`, `pthread-ext`), which are small, self-contained, and the most relevant to fab monitoring; avoid the Linux-driver-derived (`ldv-*`, `ntdrivers`) trees until licences are individually confirmed.

### 2.2 Linux Kernel Memory Model (LKMM) litmus tests — best matched pairs in the lane
- **URL:** https://github.com/torvalds/linux/tree/master/tools/memory-model/litmus-tests (+ README) and the large auto-generated set at https://github.com/paulmckrcu/litmus
- **Contents:** small C-language litmus tests for the Linux kernel memory model. ~30 curated tests in-tree; the paulmckrcu repo holds an automatically generated collection ("Automatically generated litmus tests for validation LISA-language Linux-kernel memory models") with `BPF`, `RCUlitmusGen`, `auto`, `manual`, `models` directories.
- **Format (VERIFIED verbatim from `MP+fencewmbonceonce+fencermbonceonce.litmus`):**
  ```
  C MP+fencewmbonceonce+fencermbonceonce
  (*
   * Result: Never
   * ...
   *)
  {}
  P0(int *buf, int *flag) { WRITE_ONCE(*buf, 1); smp_wmb(); WRITE_ONCE(*flag, 1); }
  P1(int *buf, int *flag) { int r0; int r1;
    r0 = READ_ONCE(*flag); smp_rmb(); r1 = READ_ONCE(*buf); }
  exists (1:r0=1 /\ 1:r1=0) (* Bad outcome. *)
  ```
- **Ground truth:** **yes — an explicit `Result: Never | Sometimes | Always` annotation plus a machine-checkable `exists` predicate labelled "Bad outcome".** This is a three-valued expected disposition, already written down.
- **Licence (VERIFIED):** in-tree files are part of the Linux kernel — **GPL-2.0**; paulmckrcu/litmus is **GPL-2.0** per its repository licence metadata.
- **Volume:** ~30 curated in-tree; thousands in paulmckrcu/litmus (exact count not enumerable from here — **UNVERIFIED**).
- **MATCHED PAIRS — this is the point.** The naming convention *is* the pair structure: `MP+fencewmbonceonce+fencermbonceonce` (Result: Never) differs from the barrier-free `MP` (Result: Sometimes) **in exactly one property — the presence of the memory barrier.** Likewise `SB+*`, `LB+*`, `ISA2+*`, `R+*`, `S+*` families. For a corpus that must test like-case consistency, a naming scheme that encodes *which single synchronisation primitive was changed* is precisely the right model.
- **Reuse path:** copy the **naming discipline** and the `Result:`/`exists` two-part oracle. Vendor the in-tree tests themselves only in a GPL-2.0-labelled partition.
- **Flag:** **VENDOR (copyleft, GPL-2.0)** for the artefacts; **VENDOR** the convention (not copyrightable).

### 2.3 jcstress (OpenJDK Java Concurrency Stress) — best expected-outcome vocabulary
- **URL:** https://github.com/openjdk/jcstress
- **Contents:** "the experimental harness and a suite of tests to aid the research in the correctness of concurrency support in the JVM, class libraries, and hardware" (README, verified). Tests organised in chapters 0a–2b plus custom tests; "the vast majority of jcstress tests are auto-generated".
- **Format:** annotated Java. Each test declares its permitted observable outcomes with `@Outcome(id=..., expect=Expect.X, desc=...)`.
- **Ground truth (VERIFIED verbatim from `Expect.java`):**
  ```java
  ACCEPTABLE("Acceptable"),              // "Acceptable result. Acceptable results are not required to be present."
  ACCEPTABLE_INTERESTING("Interesting"), // "Same as ACCEPTABLE, but this result will be highlighted in reports."
  FORBIDDEN("Forbidden"),                // "Forbidden result. Should never be present."
  UNKNOWN("Unknown");                    // internal, no grading
  ```
  README requires test authors to "provide thorough explanation why particular test outcome is acceptable/forbidden/special".
- **Licence (VERIFIED from the file header of `Expect.java`):** **GPL-2.0 only, WITH the Oracle "Classpath" exception** — "This code is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 only... Oracle designates this particular file as subject to the 'Classpath' exception".
- **Volume:** not stated in the README (**UNVERIFIED**); the suite is large and mostly generated.
- **Reuse path:** **adopt the four-valued expectation vocabulary.** A binary conforming/nonconforming disposition is too coarse for concurrency provisions: real cases need "permitted but noteworthy" (ACCEPTABLE_INTERESTING — e.g. a reordering that is legal but should be reviewed) and "must never be observed" (FORBIDDEN). Also adopt the requirement that every expected outcome carries a written *justification* — that is precisely a "reasons" field in a compliance corpus.
- **Flag:** **VENDOR (copyleft, GPLv2+CPE)** for artefacts; the vocabulary itself is free to reuse.

### 2.4 SCTBench
- **URL:** https://github.com/mc-imperial/sctbench
- **Contents:** "a set of C/C++ pthread benchmarks and tools for evaluating concurrency testing techniques" (README, verified). Includes CHESS-derived benchmarks (e.g. `InterlockedWorkStealQueue`). Ships a VirtualBox artifact and logs for reproducing the published results.
- **Format:** C/C++ pthread sources under `benchmarks/`, results under `benchmarks/__results/`, analysis scripts under `scripts/`.
- **Licence (VERIFIED):** **MIT** (repository licence metadata).
- **Volume:** total not stated in README (**UNVERIFIED**; the associated PPoPP'14 study is commonly cited as ~49 benchmarks — treat as unverified).
- **Ground truth:** **partially — `benchmarks/buggy.txt` explicitly enumerates the buggy benchmarks**, so the suite is split into a labelled buggy set and the remainder.
- **Reuse path:** the `buggy.txt` list is a ready-made boolean label file. Vendor the buggy/non-buggy split as `has_known_concurrency_defect` factor facts; MIT makes the sources directly vendorable.
- **Flag:** **VENDOR** (MIT).

### 2.5 JaConTeBe
- **URL:** paper https://mir.cs.illinois.edu/~marinov/publications/LinETAL15JaConTeBe.pdf ; suite submitted to the SIR repository at http://sir.unl.edu/portal/bios/JaConTeBe.php
- **Contents (VERIFIED from the paper):** **47 real-world Java concurrency bugs from 8 open-source projects** (Apache DBCP, Derby, Groovy, OpenJDK, Log4j, Lucene, Pool). Each bug ships **a test case and a description of the bug**, with documented root causes.
- **Bug-type labels (VERIFIED):** races & atomicity violations **19**; deadlocks **25** (16 resource, 9 communication); memory-model related **3** (2 inconsistent synchronisation, 1 sequential-consistency violation).
- **Reproducibility label (VERIFIED):** **36 of 47** reproduce the bug deterministically on every run; 11 need multiple runs; the SC-violation bug needs many more.
- **Licence:** **UNVERIFIED.** No licence is stated in the paper, and the suite is distributed via the SIR repository, which imposes its own registration/usage terms.
- **Reuse path:** the **bug-type taxonomy** (race / atomicity violation / resource deadlock / communication deadlock / inconsistent synchronisation / SC violation) is the most precise concurrency-defect vocabulary found, and it is a *fact set*, freely reusable. The **flakiness label** (deterministic vs non-deterministic reproduction) is an unusually valuable factor fact for a compliance corpus: a provision can distinguish "defect demonstrated deterministically" from "defect observed intermittently".
- **Flag:** **REFERENCE-ONLY** (licence unverified, SIR distribution terms).

### 2.6 ThreadSanitizer regression tests (LLVM compiler-rt)
- **URL:** https://github.com/llvm/llvm-project/tree/main/compiler-rt/test/tsan (the old https://github.com/google/sanitizers is **archived**; core code lives in LLVM)
- **Contents:** the TSan regression suite — small C/C++ programs each with an expected diagnostic.
- **Format (VERIFIED verbatim, `simple_race.cpp`):**
  ```
  // RUN: %clangxx_tsan -O1 %s -o %t && %deflake %run %t 2>&1 | FileCheck %s
  ... two threads racing on `Global` ...
  // CHECK: WARNING: ThreadSanitizer: data race
  // CHECK: SUMMARY: ThreadSanitizer: data race{{.*}}Thread
  ```
- **Ground truth:** **yes — the `CHECK:` / `CHECK-NOT:` lines are the expected disposition, machine-checked by FileCheck.** `%deflake` re-runs to handle non-determinism, which itself encodes a flakiness policy.
- **Licence (VERIFIED at project level):** LLVM is **Apache-2.0 WITH LLVM-exception**. (Individual test files in `compiler-rt/test` frequently omit a per-file header; the project-wide LICENSE.TXT governs.)
- **Volume:** several hundred tests in `compiler-rt/test/tsan` (**exact count UNVERIFIED**).
- **MATCHED PAIRS:** the suite systematically pairs racing programs with their correctly-synchronised counterparts (`CHECK-NOT: data race`) — same program, one mutex/atomic changed.
- **Reuse path:** vendor pairs directly. The `RUN:`/`CHECK:` idiom is a clean, tool-independent way to serialise "expected disposition + how to check it" into the corpus.
- **Flag:** **VENDOR** (Apache-2.0 with LLVM-exception; keep the exception text).

### 2.7 Miri (Rust)
- **URL:** https://github.com/rust-lang/miri
- **Contents:** "an Undefined Behavior detection tool for Rust" — detects out-of-bounds/use-after-free, uninitialised data, intrinsic precondition violations, alignment and type-invariant breaches, **data races and weak-memory effects**, and aliasing-rule (Stacked Borrows / Tree Borrows) violations, plus leaks.
- **Format:** `tests/fail/**` (each with a `.stderr` file recording the exact expected diagnostic) vs `tests/pass/**`.
- **Ground truth:** **yes** — presence in `tests/fail` + the byte-exact `.stderr` is the expected disposition; `tests/pass` is the negative control.
- **Licence (VERIFIED):** **dual MIT / Apache-2.0** (user's choice).
- **Volume:** **UNVERIFIED** (large; the repo has ~23k commits).
- **Notable:** `-Zmiri-deterministic-concurrency` — a documented flag for making concurrent executions reproducible. That maps to a corpus factor about whether a submitted test is deterministic.
- **MATCHED PAIRS:** the `tests/fail` ↔ `tests/pass` split is the pair structure, and Stacked/Tree Borrows tests are frequently one-line variants.
- **Flag:** **VENDOR** (MIT/Apache-2.0 — the cleanest concurrency-safety corpus to vendor wholesale).

### 2.8 Loom (Rust)
- **URL:** https://github.com/tokio-rs/loom
- **Contents:** exhaustive permutation testing — "runs a test many times, permuting the possible concurrent executions of that test under the C11 memory model", with state reduction to avoid combinatorial explosion. Ships `tests/`, including **`tests/litmus.rs`**.
- **Licence (VERIFIED):** **MIT**.
- **Ground truth:** yes, via `#[should_panic]` on deliberately-buggy tests (the README quickstart shows exactly this) and the litmus tests' assertions.
- **Documented limitation (important for a compliance corpus):** Loom "doesn't fully implement the C11 memory model" — `SeqCst` accesses are treated as the weaker `AcqRel`, and load buffering is unsupported, so **false alarms and missed bugs are both possible.** A corpus provision on "tool used as evidence" should require the tool's known-unsoundness envelope to be declared. Loom is the canonical citable example.
- **Flag:** **VENDOR** (MIT).

### 2.9 herdtools7 (herd7 / litmus7 / diy7)
- **URL:** https://github.com/herd/herdtools7
- **Contents:** "a tool suite to test weak memory models": `herd7` (simulator), `litmus7` (runs litmus tests on real Power/ARM/AArch64/x86 hardware), `diy7` (generates litmus tests from concise specifications), `mcompare7`, `klitmus7`. Repo contains a `catalogue/` directory.
- **Licence (VERIFIED):** **CeCILL-B** — "released under the terms of the CeCILL-B free software license agreement", © INRIA and Jade Alglave / Luc Maranget, 2010–present. CeCILL-B is a French BSD-style permissive licence with a strong attribution obligation, but it is **not** one of the common SPDX permissive licences and is not widely reviewed by corporate counsel.
- **Ground truth:** the `catalogue/` contents and their expected-outcome annotations could not be enumerated (**UNVERIFIED**).
- **Notable:** `diy7` **generates** litmus tests from a specification. For a corpus that needs *systematically varied* matched pairs, a generator is more valuable than a fixed set.
- **Flag:** **REFERENCE-ONLY** pending a CeCILL-B legal review; but note `diy7` as the mechanism for synthesising like-cases at scale.

### 2.10 GoBench
- **URL:** https://github.com/timmyyuan/gobench
- **Contents:** "the first benchmark suite for Go concurrency bugs" — **82 real bugs** from 9 popular open-source Go applications, plus **103 bug kernels** extracted/simplified from 67 of those bugs and 36 further reported bugs. Bugs categorised by type, covering "traditional and Go-specific" concurrency issues; code references (e.g. `gobench.GoKerNonBlocking`) indicate **blocking vs non-blocking** labelling.
- **Licence:** **UNVERIFIED — no licence file or licence metadata found on the repository page.** Absent a licence, default copyright applies: not redistributable.
- **Flag:** **REFERENCE-ONLY.** Its **blocking / non-blocking** split is a useful factor distinction (a deadlocked monitoring agent fails differently from one that corrupts a reading), and Go is a realistic language for fab telemetry agents.

### 2.11 RADBench
- **URL (paper):** https://people.eecs.berkeley.edu/~ksen/papers/radbench.pdf (USENIX HotPar 2011)
- **Contents:** an early concurrency-bug benchmark suite of real bugs in large real applications.
- **Licence / current hosting:** **UNVERIFIED** — no maintained repository with a licence file was located. Largely superseded by SCTBench (which absorbed benchmarks from it), JaConTeBe, and GoBench.
- **Flag:** **REFERENCE-ONLY** (historical citation).

### 2.12 Juliet CWE-362 / CWE-366 / CWE-367 families
Out of scope per the brief (Juliet/SARD already covered, CC0). Noted here only because these three CWEs are the *concurrency* slice: CWE-362 race condition, CWE-366 race within a thread, CWE-367 TOCTOU. Juliet's `_bad()`/`_good()` function-pair convention is itself a canonical matched-pair structure and remains the CC0-licensed fallback when everything else in this section is copyleft or unverified.

---

## 3. FUZZING WITH CORPORA

### 3.1 OSS-Fuzz — structure yes, corpora NO
- **URL:** https://github.com/google/oss-fuzz
- **Contents:** integration harnesses for **~1,000 projects** (README, May 2025: "helped identify and fix over 13,000 vulnerabilities and 50,000 bugs across 1,000 projects"). Structure is `projects/<name>/` with project metadata, Dockerfile and build script.
- **Licence (VERIFIED):** **Apache-2.0** (repository licence).
- **Corpora licence — CRITICAL VERIFIED FINDING:** **the corpora are not publicly downloadable.** The OSS-Fuzz documentation states: "To get access to a project's corpora, you must be listed as the primary contact or as an auto cc in the project's `project.yaml` file." Access is via authenticated Google Cloud Storage. **There is therefore no "OSS-Fuzz corpus licence" to rely on** — plan around ARVO instead.
- **Reuse path:** vendor the *harness/project layout convention* (Apache-2.0); reference the corpora only.
- **Flag:** harness/repo **VENDOR** (Apache-2.0); corpora **REFERENCE-ONLY (inaccessible)**.

### 3.2 ARVO — Atlas of Reproducible Vulnerabilities from Open-source software
- **URL:** https://github.com/n132/ARVO and https://github.com/n132/ARVO-Meta
- **Contents:** **6,138 security issues** (release v3.0.0, October 2025), each reproducible end-to-end: build at the vulnerable revision, trigger with the fuzzer-found PoC input, build at the patched revision, verify the patch. Ships Docker images (vulnerable and fixed), PoC inputs, expected crash outputs, and patch/fix commits, with OSS-Fuzz source metadata.
- **Format:** Docker images on Docker Hub + an `arvo.db` database downloadable from releases.
- **Licence (VERIFIED):** **BSD-2-Clause** (ARVO repository licence metadata). *(The ARVO-Meta repo page did not display a licence — verify separately if you use the metadata repo directly.)*
- **Ground truth:** **yes, and unusually strong — expected crash output at the vulnerable revision AND expected non-crash at the patched revision.**
- **MATCHED PAIRS:** this is the best-scaled matched-pair source in the fuzzing lane — **6,138 pairs** each differing by exactly one patch commit.
- **Reuse path:** the natural template for a corpus case is: `case_id = ARVO issue id`; factor facts `{poc_input_available, sanitizer_report_class, patch_applied}`; expected disposition flips from NONCONFORMING to CONFORMING across the pair. Because the pair differs by exactly one commit, it directly tests like-case consistency.
- **Flag:** **VENDOR** (BSD-2-Clause) — but the artefacts are Docker images; vendor the *metadata and labels*, reference the images.

### 3.3 Magma
- **URL:** https://github.com/HexHive/magma ; https://hexhive.epfl.ch/magma/
- **Contents:** "a ground-truth fuzzing benchmark suite based on real programs with real bugs" across **9 target libraries**: libpng, libsndfile, libtiff, libxml2, lua, poppler, openssl, sqlite3, php.
- **Ground truth mechanism (VERIFIED):** in-line source-level instrumentation collecting whether a bug was **reached** (buggy code executed) vs **triggered** (fault condition satisfied by the input). **Two-level ground truth**, not just crash/no-crash.
- **Volume:** total bug count **UNVERIFIED** (not stated on the repo page or the project homepage as fetched).
- **Licence:** **UNVERIFIED** — no LICENSE file was retrievable at `master/LICENSE`, and the homepage states no licence for Magma itself (it notes only that the *included libraries* are open source).
- **Reuse path:** import the **reached vs triggered** distinction. For a compliance corpus this is exactly the difference between "the change introduced an exposure" and "the change caused a failure", and it deserves two separate factor facts.
- **Flag:** **REFERENCE-ONLY** until the licence is confirmed with the authors.

### 3.4 FuzzBench
- **URL:** https://github.com/google/fuzzbench
- **Contents:** "a free service that evaluates fuzzers on a wide variety of real-world benchmarks, at Google scale". Benchmarks are drawn from OSS-Fuzz projects — "FuzzBench can use any OSS-Fuzz project as a benchmark". The sample report uses **24 real-world benchmarks**; the full standard set size is **UNVERIFIED**.
- **Licence (VERIFIED):** **Apache-2.0**.
- **Ground truth:** the metric is coverage/bug-finding rate over time, not per-case expected verdicts. **Weaker fit** for this corpus than Magma or ARVO.
- **Flag:** **VENDOR** (Apache-2.0), but low priority — use for the *experimental protocol* (fair-comparison methodology, 20+ trials, statistical reporting) rather than for cases.

### 3.5 ProFuzzBench — the stateful/protocol benchmark
- **URL:** https://github.com/profuzzbench/profuzzbench
- **Contents:** "a benchmark for stateful fuzzing of network protocols" (ISSTA 2021 tool demo, arXiv 2101.05102). Automates AFLNet / AFLnwe / StateAFL against representative open-source servers. Protocols include FTP (LightFTP), RTSP, TLS, SSH, SMTP, SIP.
- **Seed corpora:** **yes** — each target has an `in-<protocol>` folder of seed inputs (e.g. `ftp_requests_full_anonymous.raw`, `ftp_requests_full_normal.raw`).
- **Licence (VERIFIED):** **Apache-2.0**.
- **Ground truth:** pre-documented bugs are not enumerated in the repo (**UNVERIFIED**); the labelling is at the level of subject + seed.
- **Reuse path:** **the closest public analogue to fab-floor protocol fuzzing.** Fab monitoring speaks SECS/GEM, OPC UA, MQTT and Modbus, none of which have a public labelled corpus. ProFuzzBench provides the *containerised subject + seed corpus + fuzzer harness* template to clone for an industrial-protocol partition.
- **Flag:** **VENDOR** (Apache-2.0).

### 3.6 boofuzz
- **URL:** https://github.com/jtpereyda/boofuzz
- **Contents:** network protocol fuzzing framework, "a fork and successor of the Sulley Fuzzing Framework". Ships a `request_definitions/` directory of protocol grammars and an `examples/` directory. Features "Better recording of test data — consistent, thorough, clear", **test result CSV export**, and extensible instrumentation for failure detection.
- **Licence (VERIFIED):** **GPL-2.0**.
- **Ground truth:** crashes are recorded, but not pre-labelled with expected verdicts.
- **Reuse path:** its **CSV test-result export** is a usable evidence serialisation. GPL-2.0 means the grammars go in a copyleft partition.
- **Flag:** **VENDOR (copyleft, GPL-2.0)**.

### 3.7 fuzzysully — OPC UA (the one real ICS-protocol find)
- **URL:** https://github.com/ANSSI-FR/fuzzysully — released by ANSSI (the French national cybersecurity agency).
- **Contents:** an OPC UA fuzzer built on **Fuzzowski** (NCC Group), with some fuzzing logic derived from boofuzz-based scripts by Claroty and Fraunhofer FKIE. Ships **built-in protocol specifications covering 25+ OPC UA services** (ReadSession, Browse, SecureChannel, …) across three modes: server, reverse, GDS.
- **Licence (VERIFIED):** **GPL-2.0**; it redistributes modified `opcua-asyncio` (**LGPL-3.0**) and Fuzzowski (**GPL-2.0**).
- **Ground truth:** **no CVEs or labelled crashes published** in the repo.
- **Reuse path:** the **OPC UA service-level grammar** is the key asset — it enumerates which OPC UA services exist and what a malformed message for each looks like. That enumeration is what lets a corpus write provisions like "change touches an OPC UA `SecureChannel` handler ⇒ protocol-robustness provision engaged".
- **Flag:** **VENDOR (copyleft, GPL-2.0 + LGPL-3.0 components)**. Attractive additional property: an ANSSI-published tool is a *governmental* reference point, which carries weight in a compliance corpus.

### 3.8 AFL++
- **URL:** https://github.com/AFLplusplus/AFLplusplus
- **Contents:** the mainstream coverage-guided fuzzer; ships a `testcases/` directory of seed corpora.
- **Licence — VERIFIED AND AWKWARD:** **AGPL-3.0-or-later is the default**; individual files carry their own SPDX identifiers, both `AGPL-3.0-or-later` and `Apache-2.0`. The README states "Everything compiled into a fuzzing harness is and will stay Apache 2.0 licensed", but the combined binary is AGPL. **No licence statement specific to `testcases/` was found (UNVERIFIED).**
- **Reuse path:** the seed files themselves are mostly minimal format exemplars; if you want them, check per-file SPDX headers first. AGPL contamination risk makes wholesale vendoring inadvisable.
- **Flag:** **REFERENCE-ONLY** (default AGPL-3.0-or-later; per-file verification required for anything you copy).

---

## 4. CRYPTOGRAPHIC POLICY

### 4.1 Project Wycheproof — the single best "expected disposition" corpus anywhere in this study
- **URL (current home):** https://github.com/C2SP/wycheproof (moved from Google to the **C2SP** community organisation; the google/wycheproof repo mirrors it and states the project "is in the process of revitalizing development and maintenance of Project Wycheproof as a C2SP project with a renewed focus on the test vector data").
- **Contents:** "a community managed repository of test vectors that can be used by cryptography library developers to test against known attacks, specification inconsistencies, and other various implementation bugs". Covers **30+ algorithms** including AES-GCM/EAX/SIV, ChaCha20-Poly1305, AEGIS, DSA, ECDSA, EdDSA, RSA, HMAC, PBKDF2, and the post-quantum **ML-KEM** and **ML-DSA**. The README states over 80 test-case classes detecting issues such as invalid-curve attacks and biased nonces.
- **Format (VERIFIED against `testvectors_v1/aes_gcm_test.json` and `doc/formats.md`):**
  - top level: `algorithm`, `schema`, `generatorVersion` (0.9), `numberOfTests`, `header[]`, `notes{}`, `testGroups[]`
  - each test: `tcId`, `comment`, `flags[]`, algorithm parameters (`key`, `iv`, `aad`, `msg`, `ct`, `tag`, …), **`result`**
  - `notes` maps each flag name to `{description, bugType, effect, links, cves}`. `bugType` values seen include `BASIC`, `AUTH_BYPASS`, `CONFIDENTIALITY`.
  - `aes_gcm_test.json` alone has `numberOfTests: 316`, with the header stating: 'Test vectors with "result" : "valid" are valid encryptions. Test vectors with "result" : "invalid" are using invalid parameters or contain an invalid ciphertext or tag.'
  - Schemas live in `schemas/` and are **CI-enforced**: they are "tested in CI to ensure vector file contents match their advertised schema".
- **Volume:** 30+ algorithms; per-file counts in the hundreds (AES-GCM = 316). Total file count could not be enumerated (GitHub tree listings are robots-blocked from this environment) — **UNVERIFIED**, but the order of magnitude is tens of files and tens of thousands of vectors.
- **Ground truth:** **yes — `result` is literally the expected disposition, per case, with a `flags`→`bugType`→`cves` provenance chain.**
- **Licence (VERIFIED):** **Apache-2.0** — the C2SP README states the project "is offered under the Apache License 2.0", copyright 2016–2026.
- **Reuse path — near-perfect structural fit:**
  | Wycheproof | corpus |
  |---|---|
  | `tcId` | `case_id` |
  | `flags[]` → `notes[flag].bugType` | `provisions_engaged` |
  | algorithm parameters + flags | boolean `factor_facts` |
  | `result: valid / invalid` | `expected_disposition` |
  | `notes[flag].description` / `.effect` | the reason/rationale field |
  | `notes[flag].cves` | authority citation |
  Additionally, the **CI schema-enforcement discipline** is worth copying wholesale: publish a JSON Schema for the corpus and enforce it in CI so every case is machine-valid.
- **Flag:** **VENDOR** (Apache-2.0). Highest priority in this lane.

### 4.2 NIST ACVP-Server (and CAVP test vectors)
- **URL:** https://github.com/usnistgov/ACVP-Server ; CAVP: https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program
- **Contents:** generation and validation code for NIST-approved algorithms, organised per algorithm. **`~/gen-val/json-files/` contains example JSON files for all supported algorithms**: `registration`, `prompt`, `internalProjection`, and **`expectedResults`** files, generated by integration tests, usable "for quick testing without regenerating vectors".
- **Format:** JSON — `prompt.json` (inputs), `internalProjection.json`, `expectedResults.json` (the oracle). Note the caveat in the README: expected-results files are "not always the case when `isSample` is false".
- **CAVP legacy vectors (VERIFIED):** downloadable ZIPs remain published for block ciphers — **KAT vectors, MCT sample vectors, MCT intermediate values, MMT sample vectors** for AES and TDES, in `.req` / `.rsp` / `.fax` format ("Response files (.rsp): the test vectors are properly formatted in response (.rsp) files"). NIST attaches a usage caveat: "Use of these test vectors does not replace validation obtained through the CAVP." CAVP is **not** replaced by ACVP — "The CAVP offers two Automated Cryptographic Validation Test Systems (ACVTS)".
- **Licence (VERIFIED from the repository's own licence statement):** **US Government public domain** — the repository states that "software developed by NIST employees is not subject to copyright protection within the United States", and is "expressly provided 'AS IS'". *(The exact LICENSE.md file text could not be fetched directly — the statement above is quoted from the repository's displayed licence/README content. Treat the file itself as worth a final read before shipping.)*
- **Ground truth:** **yes** — `expectedResults.json` for ACVP; `.rsp` known-answer files for CAVP.
- **Reuse path:** ACVP is the *authority anchor* for crypto provisions in a regulated setting. A corpus case can cite the ACVP algorithm registration as the provision and the `expectedResults` entry as the expected disposition — no licensing friction at all for US-origin material.
- **Flag:** **VENDOR** (US public domain; note the CAVP "does not replace validation" caveat verbatim in the corpus so no case implies certification).

### 4.3 Mozilla TLS configuration levels
- **URL (data):** https://ssl-config.mozilla.org/guidelines/5.7.json ; generator repo: https://github.com/mozilla/ssl-config-generator
- **Contents (VERIFIED from 5.7.json):** three named configurations under `configurations`:
  - **modern** — TLSv1.3 only; ciphers `TLS_AES_128_GCM_SHA256`, `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`; curves X25519, prime256v1, secp384r1; **ECDSA certificates only**; HSTS ≥ 63,072,000 s; oldest clients Firefox 63 / Android 10.0 / Chrome 70.
  - **intermediate** — TLSv1.2 + TLSv1.3; ECDHE/DHE with AES-GCM and ChaCha20-Poly1305; RSA and ECDSA; oldest clients Firefox 27 / Android 4.4.2 / Chrome 31.
  - **old** — TLSv1 through TLSv1.3; **includes legacy CBC modes and 3DES**; RSA only; oldest clients Firefox 1 / Android 2.3 / Chrome 1.
- **Licence (VERIFIED):** the mozilla/ssl-config-generator repository is **MPL-2.0**. **The JSON carries no embedded licence or attribution statement (UNVERIFIED for the data specifically).** Note also: **the mozilla/ssl-config-generator repo is ARCHIVED**; active development has moved to https://github.com/tlsref/configurator — re-verify the licence at the new home before relying on it.
- **Volume:** 3 configuration levels per guideline version; many versioned JSON files.
- **Ground truth:** **implicit but excellent** — the three levels are a *ready-made ordinal disposition scale*, and the `old` level's inclusion of 3DES and CBC is precisely the "deprecated cipher accepted" oracle. Comparing `modern` vs `old` gives an automatically-derivable set of **matched pairs**: identical server, one cipher-suite line changed, disposition flips.
- **Reuse path:** derive `deprecated_cipher_offered` / `tls_version_below_floor` / `certificate_type_permitted` factor facts mechanically by diffing the levels. The `oldest_clients` field is the *justification* — it converts a bare rule into a documented compatibility trade-off, which is exactly what a compliance corpus needs to explain a disposition.
- **Flag:** **VENDOR** (MPL-2.0, file-level copyleft only — safe for data reuse with notice); confirm the tlsref/configurator licence.

### 4.4 testssl.sh
- **URL:** https://github.com/testssl/testssl.sh
- **Contents:** "checks a server's service on any port for the support of TLS/SSL ciphers, protocols as well as some cryptographic flaws". Ships an `etc/` directory of cipher/TLS reference data (cipher mapping, TLS data, CA hashes).
- **Format:** bash; outputs **CSV, two JSON formats, and HTML**.
- **Licence (VERIFIED):** **GPL-2.0**.
- **Ground truth:** per-check severity ratings are produced ("you can tell easily whether anything is good or bad"), but whether every check has a stable unique ID is **UNVERIFIED**.
- **Reuse path:** its JSON output is a ready evidence format for crypto-policy cases; the `etc/` cipher database is a vendorable (GPL-2.0) mapping from cipher suite → properties, which is what a `deprecated_cipher` factor fact needs to be computed from.
- **Flag:** **VENDOR (copyleft, GPL-2.0)**.

### 4.5 TLS-Attacker and TLS-Scanner
- **URLs:** https://github.com/tls-attacker/TLS-Attacker ; https://github.com/tls-attacker/TLS-Scanner
- **Contents:** TLS-Attacker is "a Java-based framework for analyzing TLS libraries" supporting SSL 3 and TLS 1.0–1.3, letting you send arbitrary protocol messages in custom orders; workflows are defined in Java or **XML**. TLS-Scanner "assist[s] pentesters and security researchers in the evaluation of TLS server and client configurations", outputs **JSON** (`-outputFile`) at four detail levels (QUICK/NORMAL/DETAILED/ALL), and includes **guideline-based assessment** (`-reportDetail ALL` shows "more details about the Guidelines").
- **Licence (VERIFIED):** **Apache-2.0** for both.
- **Ground truth:** TLS-Attacker's README is explicit that it is "a research tool intended for TLS developers and pentesters. There is no GUI and **no green/red lights**" — i.e. it deliberately does *not* supply a disposition. TLS-Scanner's guideline engine does. **Which guidelines ship in-repo (BSI TR-02102, NIST SP 800-52, …) is UNVERIFIED.**
- **Reuse path:** TLS-Attacker's **XML workflow format** is a good serialisation for "the exact protocol interaction this case is about". TLS-Scanner's guideline model — named guideline → per-check result → aggregate rating — is close to the corpus's provision→disposition model and is Apache-2.0.
- **Flag:** **VENDOR** (Apache-2.0). Verify the shipped guideline set before claiming BSI/NIST coverage.

### 4.6 ComplianceAsCode / content
- **URL:** https://github.com/ComplianceAsCode/content
- **Contents:** the largest open corpus of machine-checkable system security policy. "Write once, generate multiple formats": an OpenControl-inspired **YAML rule format** combined with **OVAL checks**, Ansible task snippets, bash remediations, and **security identifiers (CCE, NIST ID, STIG)**. Generates XCCDF and SCAP source data streams, Ansible playbooks, bash fix scripts, and CEL for Kubernetes/OpenShift. Profiles referenced include **CIS, STIG, PCI-DSS, OSPP**. Covers RHEL, Fedora, Ubuntu, Debian, SUSE, plus applications (Firefox, JBoss) and containers. ~44,000 commits.
- **Licence (VERIFIED):** **BSD-3-Clause**.
- **Volume:** exact rule count not stated on the repository page (**UNVERIFIED**); it is in the thousands across products.
- **Ground truth:** each rule pairs a **normative statement** with an **automated check (OVAL)** and a **remediation** — and crucially with **authority identifiers (CCE / NIST 800-53 control / STIG ID)**. Crypto-policy rules (FIPS mode, system crypto-policies, sshd cipher/MAC/KEX allow-lists) exist in the RHEL/Fedora products, though the repo page did not itemise them (**UNVERIFIED at the individual-rule level**).
- **Reuse path — the closest existing thing to the target corpus.** Its rule YAML already carries: identifier, description, rationale, severity, per-product applicability, and a mapping to external authorities. **Model the corpus's provision records on ComplianceAsCode rule YAML** and reuse its authority-mapping idiom (`identifiers:` / `references:` blocks) so fab provisions can cite SEMI standards the same way its rules cite NIST controls.
- **Flag:** **VENDOR** (BSD-3-Clause — permissive, no practical friction). Highest-value *schema* import for the compliance-modelling side.

---

## 5. AI-AGENT CODE DEFENCE (beyond the already-surveyed set)

### 5.1 Hallucinated / non-existent package imports

**PackageHallucination (USENIX Security 2025, Spracklen et al.)**
- **URL:** https://github.com/Spracks/PackageHallucination ; paper https://www.usenix.org/system/files/usenixsecurity25-spracklen.pdf
- **Contents:** code and data for "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs". **576,000 generated code samples** across **Python/PyPI and JavaScript/npm**, from which **205,474 unique hallucinated package names** were identified.
- **Format:** JSON prompt datasets under `Data/Python/` and `Data/JavaScript/` (`LLM_AT.json`, `LLM_LY.json`, `SO_AT.json`, `SO_LY.json`), plus **master lists of valid package names**.
- **Licence (VERIFIED):** **MIT**.
- **Ground truth — IMPORTANT LIMITATION (VERIFIED):** the authors **deliberately withhold** the full hallucinated-package list and per-prompt results, stating that "releasing these could enable package confusion attacks at scale". Verified researchers may request the full datasets for academic purposes. **What ships publicly is the prompts + the valid-package master lists + the reproduction pipeline — not the labelled hallucination list.**
- **Reuse path:** the *master lists of valid package names* are the reusable oracle: `package_exists_in_registry ∈ {true,false}` is a decidable factor fact computed against them. The corpus does not need the hallucinated names — it needs the negative oracle, and that is what is released. This is also a genuinely new provision class ("slopsquatting"): an AI-authored change that imports a non-existent dependency.
- **Flag:** **VENDOR** (MIT) for what is public; **REFERENCE-ONLY** for the withheld list (and do not attempt to reconstruct it — the authors withheld it for a stated safety reason).

**depscope-hallucinations-dataset**
- **URL:** https://github.com/cuttalo/depscope-hallucinations-dataset
- **Contents:** self-described as a public corpus of LLM-hallucinated package names observed in production AI coding-agent traffic across 19 ecosystems, updated daily.
- **Licence (as stated in the repository's own description, NOT independently verified against a LICENSE file):** **CC-BY-NC-SA-4.0**. The **NC** clause makes this unusable in a corpus intended for industrial/commercial compliance use, and **SA** would force the whole corpus share-alike.
- **Flag:** **REFERENCE-ONLY — do not vendor.** The NC term is disqualifying for a fab-industry corpus.

### 5.2 API contract / contract-testing corpora

**Pact specification test cases — a ready-made matched-pair corpus**
- **URL:** https://github.com/pact-foundation/pact-specification (versions live in branches: `version-1`, `version-1.1`, `version-2`, `version-3`, `version-4`)
- **Contents:** the normative cross-language conformance corpus for consumer-driven contract matching, "to ensure consistent matching logic across 10+ programming language implementations". Test cases sit under `testcases/` and are partitioned by what is being matched — `request/` and `response/`, each further split by `method`, `path`, `query`, `headers`, `body`.
- **Format (VERIFIED verbatim from `testcases/request/method/different method.json`):**
  ```json
  {
    "match": false,
    "comment": "Methods is incorrect",
    "expected": { "method": "POST", "path": "/", "query": {}, "headers": {} },
    "actual":   { "method": "GET",  "path": "/", "query": {}, "headers": {} }
  }
  ```
- **Licence (VERIFIED):** **MIT**.
- **Volume:** hundreds of JSON cases across 4–5 specification versions (**exact count UNVERIFIED**).
- **Ground truth:** **`"match": true | false` is the expected disposition, with `comment` as the stated reason and `expected`/`actual` as the fact pair.**
- **MATCHED PAIRS — the best-formed in the study.** Every case is *already* a minimal pair: `expected` and `actual` differ in exactly one attribute, and the directory path names which attribute. `request/method/different method.json` (match: false) sits beside `request/method/matches.json` (match: true). Directory = provision, filename = factor, `match` = disposition.
- **Reuse path:** **adopt this file layout directly.** `testcases/<provision>/<factor>/<case name>.json` with `{match, comment, expected, actual}` is very nearly the target schema already; rename `match` → `expected_disposition`, `comment` → `reason`, and add `provisions_engaged` derived from the path. It is MIT, small, human-readable, and battle-tested across ten language implementations — which is itself proof that the format supports like-case consistency across independent implementers.
- **Flag:** **VENDOR** (MIT). Top-3 pick.

**Schemathesis**
- **URL:** https://github.com/schemathesis/schemathesis
- **Contents:** property-based API testing driven by OpenAPI and GraphQL schemas; generates inputs from the schema, adapts to responses, chains operations. Detects "500 errors that crash your API on edge case inputs", "schema violations where your API returns different data than documented", and "validation bypasses where invalid data gets accepted".
- **Licence (VERIFIED):** **MIT**.
- **Ground truth:** the named-check set (`not_a_server_error`, `status_code_conformance`, `content_type_conformance`, `response_schema_conformance`) could **not be confirmed from the current README (UNVERIFIED)** — the three failure categories above are what is documented.
- **Reuse path:** those three documented categories are directly usable as contract-provision names; the tool itself supplies the oracle (the schema) so no hand-labelling is needed.
- **Flag:** **VENDOR** (MIT).

### 5.3 AST-level policy tools

**Semgrep rule registry — VERIFIED NOT OPEN SOURCE**
- **URL:** https://github.com/semgrep/semgrep-rules ; licence text at https://semgrep.dev/legal/rules-license
- **Licence (VERIFIED, and this is a significant negative finding):** the rules are under the **Semgrep Rules License v1.0**, a **proprietary licence, not OSI-approved**. Verified terms: *"You may use the rules only for your own internal business purposes"* and *"This license does not allow you to distribute the rules, or to make them available to others as a service."* There is also a patent-termination provision.
- **Consequence:** **the Semgrep rule registry cannot be vendored into an open corpus, and cannot be redistributed at all.** Any prior assumption that semgrep-rules is LGPL-2.1 is wrong.
- **Flag:** **REFERENCE-ONLY — redistribution expressly prohibited.**

**opengrep-rules (the fork)**
- **URL:** https://github.com/opengrep/opengrep-rules — "a fork of semgrep-rules (December 13, 2024)", explicitly "not affiliated with or endorsed by Semgrep Inc.", stated as "intended for research, testing & benchmarking".
- **Licence (VERIFIED from the LICENSE file):** **LGPL-2.1 with the Commons Clause License Condition v1.0.** Redistribution is permitted under LGPL-2.1; the Commons Clause prohibits "Sell" — providing to third parties for a fee a product or service whose value derives substantially from the software's functionality.
- **Flag:** **REFERENCE-ONLY / restricted.** Redistributable, but Commons Clause is not an open-source licence and would contaminate a corpus meant for commercial industrial use. Only usable if the corpus itself is never sold and the partition is clearly quarantined. **Recommend avoiding.**

**CodeQL — the vendorable AST-policy option**
- **URL:** https://github.com/github/codeql
- **Contents:** CodeQL **queries and libraries** for cpp, csharp, go, java, javascript, python, ruby, rust, swift; query suites; query help documentation.
- **Licence (VERIFIED, dual structure):** the **libraries and queries in this repository are MIT-licensed** by GitHub. The CodeQL **CLI/engine is separately licensed** — "If you'd like to use the CodeQL CLI to analyze closed-source code, you will need a separate commercial license."
- **Ground truth:** CodeQL query tests use `.ql`/`.qlref` inputs with **`.expected` result files** — a per-query expected-output oracle. *(Present in the repo but not itemised on the landing page — treat the `.expected` convention as **UNVERIFIED** at file level and confirm in a language subdirectory before relying on it.)*
- **Reuse path:** **this is the AST-policy source to use instead of Semgrep.** MIT queries + `.expected` result files give (rule = provision, test case = facts, expected results = disposition). Note the engine/query licence split in the corpus documentation so users are not misled about running the queries on closed-source fab code.
- **Flag:** **VENDOR** (MIT for queries/libraries); **flag the CLI licence separately.**

**Bandit**
- **URL:** https://github.com/PyCQA/bandit
- **Contents:** Python security linter — builds an AST and runs security plugins against AST nodes. Ships both an `examples/` directory and a `tests/` directory (confirmed present).
- **Licence (VERIFIED):** **Apache-2.0**.
- **Ground truth:** Bandit's functional tests associate each `examples/*.py` file with expected issue counts bucketed by SEVERITY and CONFIDENCE (HIGH/MEDIUM/LOW). **The exact encoding could not be fetched (`tests/test_functional.py` 404'd at the guessed path) — UNVERIFIED.**
- **Reuse path:** a small, wholly-permissive, Python-specific corpus where each example file already has a numeric expected-findings vector. Good for the "AI wrote Python telemetry glue code" partition, which is realistic for fab monitoring.
- **Flag:** **VENDOR** (Apache-2.0), pending confirmation of the expected-count encoding.

### 5.4 AI-generated / vulnerability-labelled code datasets

**PrimeVul — best matched-pair vulnerability dataset**
- **URL:** https://github.com/DLVulDet/PrimeVul (data on Google Drive, linked from the README)
- **Contents:** ~**7,000 vulnerable functions** and ~**229,000 benign functions** from real-world C/C++ projects, covering **140+ CWEs**. Built for accurate labelling and minimal data contamination.
- **Paired data:** the release includes **`primevul_test_paired.jsonl`** and the documentation describes "Paired Samples" analysis. **The exact number of pairs is UNVERIFIED.**
- **Licence (VERIFIED):** **MIT**.
- **Ground truth:** yes — per-function vulnerable/benign labels with CWE.
- **Reuse path:** the paired split is the matched-pair engine for code-level provisions: same function, one fix commit apart, disposition flips. C/C++ is the right language profile for fab equipment interface code.
- **Flag:** **VENDOR** (MIT). Top-5 pick.

**BaxBench**
- **URL:** https://baxbench.com/ ; repo https://github.com/logic-star-ai/baxbench ; data https://huggingface.co/datasets/LogicStar/BaxBench ; paper arXiv:2502.11844 (ICML 2025)
- **Contents:** **392 security-critical backend coding tasks** = **28 scenarios × 14 backend frameworks across 6 languages**. Each task ships **functional correctness tests AND security exploits**: "black-box exploits that attack the application using malicious queries, e.g. SQL injections or path traversal, and white-box exploits, e.g. checking for passwords or unencrypted secrets".
- **Licence (VERIFIED):** **MIT** (repository LICENSE / badge). *(HuggingFace dataset licence not separately confirmed — **UNVERIFIED**.)*
- **Ground truth:** **two-dimensional and explicitly labelled — "correct & secure", "correct (but potentially insecure)", and the fraction of correct solutions containing vulnerabilities.**
- **Reuse path:** **the two-axis disposition is the key import.** A change can be functionally correct and still non-conforming. Model `functionally_correct` and `security_conforming` as *separate* factor facts with a composite disposition, rather than collapsing them. The 28×14 grid also gives free like-case structure: the same scenario across 14 frameworks is 14 like-cases that should be decided consistently on the security axis.
- **Flag:** **VENDOR** (MIT); confirm the HF dataset licence.

**SecurityEval**
- **URL:** https://github.com/s2e-lab/SecurityEval (MSR4P&S '22)
- **Contents:** v2.1 covers **121 prompts for 69 CWEs** (the original paper described 130 samples over 75 CWE-mapped vulnerability types). Also on HuggingFace.
- **Format:** JSONL with `ID`, `Prompt`, `Insecure_code`.
- **Licence:** **UNVERIFIED — no licence stated on the repository page.**
- **Flag:** **REFERENCE-ONLY** until the LICENSE file is read. Its prompt→CWE mapping is useful as a cross-reference even if the data is not vendored.

---

## 6. MATCHED PAIRS — CONSOLIDATED (the most valuable structure for like-case consistency)

Ranked by fitness for a corpus that must decide like cases alike, with verified licence:

| # | Source | Pair axis (the *one* thing that differs) | Volume | Licence (verified) | Flag |
|---|---|---|---|---|---|
| 1 | **Pact specification `testcases/`** | one request/response attribute (method, path, query, header, body) | hundreds | MIT | VENDOR |
| 2 | **ARVO** | one patch commit (vulnerable rev → fixed rev) | 6,138 | BSD-2-Clause | VENDOR (metadata) |
| 3 | **LKMM litmus tests** | one memory barrier / synchronisation primitive | ~30 in-tree + thousands generated | GPL-2.0 | VENDOR (copyleft) |
| 4 | **TSan `compiler-rt/test/tsan`** | one mutex/atomic added | hundreds | Apache-2.0 WITH LLVM-exception | VENDOR |
| 5 | **Miri `tests/fail` vs `tests/pass`** | one UB-inducing operation / aliasing step | large | MIT / Apache-2.0 | VENDOR |
| 6 | **PrimeVul paired split** | one vulnerability fix in the same function | ~7k vuln / 229k benign | MIT | VENDOR |
| 7 | **Mozilla TLS levels (modern/intermediate/old)** | one cipher suite or protocol version | 3 levels × N versions | MPL-2.0 (repo) | VENDOR |
| 8 | **Wycheproof `result: valid` vs `invalid`** | one malformed field/parameter, same key material | 30+ algorithms, hundreds per file | Apache-2.0 | VENDOR |
| 9 | **BaxBench 28 scenarios × 14 frameworks** | the framework, holding the scenario fixed | 392 | MIT | VENDOR |
| 10 | **jcstress `@Outcome` sets** | one memory-ordering annotation | large | GPL-2.0 + Classpath | VENDOR (copyleft) |
| 11 | **Juliet `_bad()`/`_good()`** (out of lane scope) | one sink/sanitiser | ~64k | CC0 | VENDOR |

---

## 7. PROPOSED FACTOR NAMES (derived from the verified sources)

Naming convention: `snake_case`, boolean-valued, phrased so that `true` is the fact-as-found, not a conclusion.

### Latency / real-time provisions
Derived from cyclictest `-b USEC`, rtla `-i`/`-T`, HdrHistogram `recordValueWithExpectedInterval`, wrk2 constant-rate model.
- `latency_budget_declared` — a numeric microsecond budget exists for the changed path
- `budget_scope_is_interrupt_context` / `budget_scope_is_task_context` — the rtla IRQ vs thread split; a fab sensor ISR and a control task must not share one budget
- `measured_p999_exceeds_budget`, `measured_p100_exceeds_budget` — separate facts; tail and worst-case are different obligations
- `measurement_corrects_coordinated_omission` — evidence used the corrected recording path (HdrHistogram expected-interval, or wrk2 constant-rate). **`false` should itself engage a provision:** uncorrected tail latency is not admissible evidence
- `measurement_duration_meets_minimum` — worst-case latency claims need long-run data (the OSADL long-term-monitoring practice)
- `load_conditions_declared` — the measurement states the concurrent load
- `histogram_evidence_retained` — a full distribution was kept, not just a summary statistic
- `change_touches_realtime_scheduled_path` — the changed code runs under a real-time scheduling class
- `priority_inversion_protection_present` — mutexes on the RT path use priority inheritance

### Concurrency / memory-safety provisions
Derived from SV-COMP subproperties, JaConTeBe bug taxonomy, LKMM `Result:`, jcstress `Expect`, Miri, Loom.
- `shared_state_introduced` — the change adds state reachable from more than one thread
- `synchronisation_primitive_removed` / `synchronisation_primitive_weakened` — the LKMM pair axis; "weakened" covers seq_cst→acquire/release
- `memory_ordering_annotation_changed`
- `defect_class_is_data_race` / `_atomicity_violation` / `_resource_deadlock` / `_communication_deadlock` / `_inconsistent_synchronisation` / `_sequential_consistency_violation` — **the JaConTeBe six-way taxonomy, verified**
- `defect_class_is_toctou` — CWE-367; the fab-relevant file/permission race
- `defect_reproduces_deterministically` — JaConTeBe's 36-of-47 distinction; separates a demonstrated defect from an intermittent observation
- `race_detector_clean` (TSan/Helgrind) and `race_detector_run_under_representative_load`
- `exhaustive_interleaving_check_performed` (Loom / jcstress / CBMC-style)
- `analysis_tool_unsoundness_declared` — **cite Loom's own README** (SeqCst treated as AcqRel, no load buffering): evidence from a tool with a known unsoundness envelope must declare it
- `expected_outcome_set_enumerated` — jcstress discipline: every permitted observable outcome was written down in advance
- `forbidden_outcome_observed` — jcstress `FORBIDDEN`
- `interesting_outcome_observed` — jcstress `ACCEPTABLE_INTERESTING`: legal but must be reviewed. **Do not collapse this into "pass".**
- `undefined_behaviour_detected` (Miri), `aliasing_rule_violated` (Stacked/Tree Borrows)
- `blocking_defect` vs `non_blocking_defect` — GoBench axis; a hung monitor and a lying monitor are different fab hazards

### Cryptographic-policy provisions
Derived from Wycheproof `result`/`flags`/`bugType`, Mozilla TLS levels, ACVP `expectedResults`, ComplianceAsCode.
- `deprecated_cipher_offered` — computable by diffing Mozilla `old` against `intermediate`
- `cbc_mode_offered`, `triple_des_offered` — the two concrete `old`-only items, verified
- `tls_version_below_floor` — floor named by the declared configuration level
- `configuration_level_declared` — `modern` / `intermediate` / `old`; **plus** `compatibility_justification_recorded` (Mozilla's `oldest_clients` is the model: a permissive level is only defensible with a stated client-compatibility reason)
- `invalid_ciphertext_accepted`, `invalid_signature_accepted`, `invalid_curve_point_accepted`, `malformed_parameter_accepted` — the Wycheproof `result: invalid` family
- `authentication_bypass_class` / `confidentiality_class` — **Wycheproof `bugType` values, verified** (`AUTH_BYPASS`, `CONFIDENTIALITY`, `BASIC`)
- `nonce_reuse_possible`, `nonce_bias_present` — Wycheproof biased-nonce class
- `known_answer_test_passed` — ACVP/CAVP KAT oracle
- `algorithm_has_current_acvp_validation` — the authority anchor; keep separate from `known_answer_test_passed`, since passing a KAT is not validation (NIST's own caveat: "Use of these test vectors does not replace validation obtained through the CAVP")
- `post_quantum_algorithm_used` — ML-KEM / ML-DSA now have Wycheproof vectors; a forward-looking provision
- `certificate_key_type_permitted` — Mozilla `modern` is ECDSA-only
- `crypto_policy_enforced_at_system_level` — ComplianceAsCode system crypto-policies / FIPS-mode rules

### AI-agent code provisions
Derived from PackageHallucination, Pact, BaxBench, CodeQL, the Semgrep licence finding.
- `change_authored_by_ai_agent`, `human_review_recorded` — the gating facts
- `imported_package_exists_in_registry` — **the slopsquatting oracle**; computable against PackageHallucination's released master lists of valid package names
- `imported_package_newly_created` — registry age heuristic; a package created after the model's cutoff that the model "knew about" is the attack signature
- `dependency_pinned_to_verified_version`, `dependency_addition_declared`
- `api_contract_broken` — Pact `match: false`
- `contract_break_axis_is_method` / `_path` / `_query` / `_header` / `_body` — **the Pact directory taxonomy, verified**; naming *which* attribute broke is what makes like-case comparison possible
- `schema_conformance_violated`, `undocumented_response_returned`, `invalid_input_accepted` — the three Schemathesis categories
- `functionally_correct` **and** `security_conforming` — **BaxBench's two axes, kept separate**; the composite disposition is the interesting part
- `exploit_demonstrated_black_box` / `exploit_demonstrated_white_box` — BaxBench's own split (malicious query vs secret-in-source inspection)
- `static_policy_rule_violated`, `policy_rule_source_is_redistributable` — **a licence-provenance fact for the evidence itself.** The Semgrep finding makes this necessary: if a disposition rests on a Semgrep registry rule, the corpus cannot ship the rule that justifies it, and the case is not independently reproducible. Prefer CodeQL (MIT) for any rule a case depends on.
- `finding_has_expected_result_file` — CodeQL `.expected` discipline: the rule's own behaviour is pinned by a test

---

## 8. RECOMMENDED SCHEMA (synthesised from the verified formats)

Four verified formats independently converge on the same shape. Combine them:

```yaml
# structure and expected-verdict semantics: BenchExec task-definition v2.x (Apache-2.0)
# provision metadata and authority mapping: ComplianceAsCode rule YAML (BSD-3-Clause)
# expectation vocabulary: jcstress Expect (GPL-2.0+CPE — vocabulary only)
# pair layout and reason field: Pact specification testcases (MIT)

case_id: SEMIFAB-LAT-0142
format_version: "1.0"
input_files: [ changes/0142.patch ]
provisions_engaged:
  - provision: RT-BUDGET-IRQ
    expected_disposition: NONCONFORMING   # BenchExec expected_verdict
    subprovision: worst_case_exceeded     # BenchExec subproperty
factor_facts:
  latency_budget_declared: true
  budget_scope_is_interrupt_context: true
  measured_p100_exceeds_budget: true
  measurement_corrects_coordinated_omission: false
expectation: FORBIDDEN                     # jcstress: ACCEPTABLE | ACCEPTABLE_INTERESTING | FORBIDDEN
reason: >                                  # Pact "comment"; jcstress requires a written justification
  Worst-case IRQ latency exceeded the declared 50 us budget, and the
  submitted evidence was recorded without coordinated-omission correction.
authorities:                               # ComplianceAsCode identifiers/references idiom
  - { source: wycheproof, ref: null }
pair_of: SEMIFAB-LAT-0141                  # matched-pair link; differs only in the barrier/budget fact
```

Two disciplines worth copying alongside the schema:
1. **Wycheproof's CI schema enforcement** — schemas are "tested in CI to ensure vector file contents match their advertised schema". Publish a JSON Schema for the corpus and gate every PR on it.
2. **jcstress's justification requirement** — every expected outcome must carry a written explanation of *why* it is acceptable or forbidden. In a compliance corpus this is the reasons field, and making it mandatory at schema level is what prevents unexplained dispositions.

---

## 9. LICENCE SUMMARY TABLE

| Source | Licence (verified) | Verified from | Flag |
|---|---|---|---|
| HdrHistogram | CC0-1.0 / BSD-2-Clause (dual) | LICENSE.txt text | VENDOR |
| Wycheproof (C2SP) | Apache-2.0 | README licence statement | VENDOR |
| wrk2 | Apache-2.0 | LICENSE file text | VENDOR |
| BenchExec task-definition format doc | Apache-2.0 | SPDX header in the file | VENDOR |
| SV-Benchmarks (Zenodo svcomp25) | CC-BY-4.0 (deposit metadata) | Zenodo record 15012096 | VENDOR per-directory |
| SV-Benchmarks (GitLab repo) | Apache-2.0 (repo-level) + heterogeneous per-file | GitLab project page | verify per-directory |
| ARVO | BSD-2-Clause | repo licence metadata | VENDOR |
| ProFuzzBench | Apache-2.0 | repo licence metadata | VENDOR |
| FuzzBench | Apache-2.0 | repo licence metadata | VENDOR |
| OSS-Fuzz (repo) | Apache-2.0 | repo licence metadata | VENDOR (repo) / corpora inaccessible |
| LLVM compiler-rt TSan tests | Apache-2.0 WITH LLVM-exception | LLVM project licence | VENDOR |
| Miri | MIT / Apache-2.0 (dual) | README | VENDOR |
| Loom | MIT | repo licence metadata | VENDOR |
| SCTBench | MIT | repo licence metadata | VENDOR |
| jitterdebugger | MIT | LICENSE (MIT, © Siemens AG) | VENDOR |
| Pact specification | MIT | repo licence metadata | VENDOR |
| Schemathesis | MIT | repo licence metadata | VENDOR |
| PrimeVul | MIT | repo licence metadata | VENDOR |
| BaxBench | MIT | LICENSE / badge | VENDOR |
| PackageHallucination | MIT | repo licence metadata | VENDOR (public part only) |
| CodeQL queries & libraries | MIT (CLI licensed separately) | README | VENDOR (queries) |
| Bandit | Apache-2.0 | repo badge/licence | VENDOR |
| TLS-Attacker / TLS-Scanner | Apache-2.0 | repo licence metadata | VENDOR |
| ComplianceAsCode/content | BSD-3-Clause | repo licence metadata | VENDOR |
| NIST ACVP-Server / CAVP vectors | US Govt public domain (not subject to US copyright) | repo licence statement | VENDOR |
| Mozilla ssl-config-generator | MPL-2.0 (repo **archived**) | repo licence metadata | VENDOR (recheck at tlsref/configurator) |
| rt-tests | GPL-2.0 | COPYING on kernel.googlesource mirror | REFERENCE-ONLY |
| rtla | GPL-2.0 | kernel docs | REFERENCE-ONLY |
| LKMM litmus tests / paulmckrcu/litmus | GPL-2.0 | Linux kernel / repo metadata | VENDOR (copyleft) |
| jcstress | GPL-2.0 only WITH Classpath exception | file header of Expect.java | VENDOR (copyleft) |
| testssl.sh | GPL-2.0 | repo licence metadata | VENDOR (copyleft) |
| boofuzz | GPL-2.0 | repo licence metadata | VENDOR (copyleft) |
| fuzzysully (ANSSI) | GPL-2.0 (+LGPL-3.0 components) | repo licence statement | VENDOR (copyleft) |
| lmbench (intel mirror) | GPL-2.0 (plain, in that mirror's COPYING) | COPYING text | REFERENCE-ONLY |
| herdtools7 | CeCILL-B | README licence statement | REFERENCE-ONLY |
| AFL++ | AGPL-3.0-or-later default; some files Apache-2.0 | README licence section | REFERENCE-ONLY |
| opengrep-rules | LGPL-2.1 + Commons Clause | LICENSE file | REFERENCE-ONLY (restricted) |
| **semgrep-rules** | **Semgrep Rules License v1.0 — proprietary, no redistribution** | semgrep.dev/legal/rules-license | **REFERENCE-ONLY — cannot redistribute** |
| depscope-hallucinations-dataset | CC-BY-NC-SA-4.0 (per repo description) | repo description | REFERENCE-ONLY (NC disqualifying) |
| OSADL QA Farm data | "All rights reserved" | site footer | REFERENCE-ONLY |
| Magma | UNVERIFIED | — | REFERENCE-ONLY |
| JaConTeBe | UNVERIFIED (SIR distribution terms) | — | REFERENCE-ONLY |
| GoBench | UNVERIFIED (no licence file found) | — | REFERENCE-ONLY |
| RADBench | UNVERIFIED (no maintained repo found) | — | REFERENCE-ONLY |
| SecurityEval | UNVERIFIED | — | REFERENCE-ONLY |

---

## 10. GAPS FOUND (arguments for the corpus's novelty)

1. **No public microsecond-budget conformance corpus with expected verdicts exists.** rt-tests and rtla give the measurement and the threshold mechanism; OSADL has the data but reserves all rights. Nobody publishes `(change, budget, expected disposition)` triples.
2. **No public labelled corpus for SECS/GEM, and none for Modbus.** OPC UA has exactly one credible open fuzzer (ANSSI fuzzysully, GPL-2.0, no published CVEs). ProFuzzBench covers IT protocols only. This is the largest hole for fab monitoring specifically.
3. **OSS-Fuzz corpora are not public** — ARVO (BSD-2-Clause, 6,138 issues) is the only viable public substitute.
4. **The dominant AST-policy rule registry is proprietary.** Semgrep's registry cannot be redistributed; a corpus whose dispositions depend on it is not independently reproducible. This is a strong reason to standardise on CodeQL (MIT) and to record rule-licence provenance as a factor fact.
5. **The full hallucinated-package list is deliberately withheld** for safety, so the corpus must build the oracle from the *positive* direction (valid-registry master lists), not from a list of bad names.
