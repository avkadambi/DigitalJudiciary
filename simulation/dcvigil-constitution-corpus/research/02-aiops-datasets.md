# Lane 02 — AIOps / Anomaly-Detection / RCA Datasets and Benchmarks

Research for the DCVigil open compliance test corpus (multi-tenant datacenter monitoring / AIOps
platform). Verified against primary sources on 2026-09-05. Every licence below was read either
from the repository's raw `LICENSE` file, the dataset host's licence field, or the programme's
terms page. Where two authoritative sources disagree, both are recorded and the item is
downgraded to REFERENCE-ONLY.

Corpus case shape assumed throughout:
`(case id, provisions engaged, boolean factor facts, expected disposition)`.
So a dataset can enter the corpus in exactly one of four ways:

- **F — factor vocabulary**: the dataset's taxonomy supplies the *names* of boolean factor facts.
- **D — realistic distributions**: the dataset supplies plausible magnitudes/priors so that
  synthetic case fixtures are not arbitrary.
- **O — regression oracle**: the dataset is actually executed to decide a boolean fact such as
  `detector_regression_demonstrated_on_held_out_corpus`.
- **P — procedure precedent**: the paper/benchmark defines an evaluation *protocol* the corpus
  can cite as the standard of care, without shipping any data.

Vendoring verdicts: **VENDOR** = redistributable inside an openly-licensed corpus (attribution
obligations noted). **REFERENCE-ONLY** = cite/link, run locally, never redistribute.

---

## 1. Log datasets

### 1.1 Loghub (logpai)

- URL: https://github.com/logpai/loghub — data mirrored on Zenodo (e.g. record 8196385).
- Contents: 22 log sources across distributed systems (HDFS v1/v2/v3, Hadoop, Spark, Zookeeper,
  OpenStack), supercomputers (BGL, HPC, Thunderbird), OS (Windows, Linux, Mac), mobile
  (Android v1/v2, HealthApp), server apps (Apache, OpenSSH) and standalone software (Proxifier).
  Roughly **117+ GiB** across the full collection; the 18-dataset Zenodo bundle is 6.0 GB.
- Format: raw `.log` text plus, for several systems, preprocessed `*_templates.csv`,
  `anomaly_label.csv`, `Event_traces.csv`, `Event_occurrence_matrix.csv`, `.npz`.
- Ground truth: labelled sets flagged in the README are HDFS_v1, HDFS_v3, Hadoop, OpenStack,
  BGL, Thunderbird, Windows, Linux, Mac, Android_v1, Android_v2, HealthApp, Apache, OpenSSH,
  Proxifier. HDFS_v1 is the canonical anomaly-detection set: logs are **sliced into traces by
  block id, and each block-id trace carries a normal/anomaly ground-truth label**. HDFS_v3
  (TraceBench) records 364 files / >370,000 traces over 180 hours with **17 injected faults**
  (function faults, performance faults, real system bugs). HDFS_v2 is >16 GB and explicitly
  **unlabelled** ("without further modification or labelling").
- **Licence — CONFLICTING, verified both ways:**
  - Repo `LICENSE` (verbatim): *"The datasets are freely available for research or academic work,
    subject to the following condition: For any usage or distribution of the loghub datasets,
    please refer to the loghub repository URL (https://github.com/logpai/loghub) and cite the
    following loghub paper where applicable. … The above license notice shall be included in all
    copies of the datasets."*
  - Zenodo record 8196385 licence field: *"Creative Commons Attribution 4.0 International"*.
  - The repo text restricts to *research or academic work*; the Zenodo field does not. This is a
    real, unresolved discrepancy. **Treat as REFERENCE-ONLY for a corpus intended for commercial
    conformance testing** until logpai clarifies in writing. Do not rely on the Zenodo field
    alone — it is metadata, not a signed grant, and it is contradicted by the file the authors
    ship with the data.
- Citation required: Zhu et al., "Loghub: A Large Collection of System Log Datasets for AI-driven
  Log Analytics", ISSRE 2023.
- Reuse: **F, D, O**. The block-level normal/anomaly labelling of HDFS_v1 is the cleanest
  available oracle for "did the log anomaly detector regress"; the 17-fault taxonomy of HDFS_v3
  is a ready-made factor vocabulary for injected-fault classes.

### 1.2 Loghub-2.0 / LogPub (logpai)

- URL: https://github.com/logpai/loghub-2.0 — data at https://zenodo.org/records/8275861 (965.6 MB
  of zips: Apache, BGL, Hadoop, HDFS, HealthApp, HPC, Linux, Mac, OpenSSH, OpenStack, Proxifier,
  Spark, Thunderbird, Zookeeper).
- Contents: **14 systems, average 3,601,187 annotated log lines each (~50M lines total)**, average
  **249 templates per system** (vs 82 in the older Loghub-2k sampled variant). This is the
  large-scale, template-annotated successor used for log parsing evaluation.
- **Licence — CONFLICTING, verified both ways:** the GitHub page's sidebar reports MIT, but the
  actual raw `LICENSE` file is the same custom text as Loghub: *"The datasets are freely available
  for research or academic work, subject to the following condition: For any usage or distribution
  of the loghub-2.0 datasets, please refer to the loghub repository URL … and cite the following
  loghub papers where applicable."* Zenodo 8275861 states *"Creative Commons Attribution 4.0
  International"*. **The GitHub MIT badge is wrong for the data — do not rely on it.**
  Verdict: **REFERENCE-ONLY** pending written clarification.
- Metrics defined by the accompanying ISSTA 2024 paper (Jiang et al., *A Large-Scale Evaluation
  for Log Parsing Techniques: How Far Are We?*, https://arxiv.org/abs/2308.10828), verbatim
  definitions from the camera-ready PDF:
  - **GA (Grouping Accuracy)** — "the proportion of correctly grouped log messages to the total
    number of log messages. A log message is regarded as correctly grouped if and only if its
    template corresponds to the same set of log messages as the ground truth does."
  - **PA (Parsing Accuracy)** — "the ratio of correctly parsed log messages over the total number
    of log messages, where a log message is considered to be correctly parsed if and only if all
    tokens of static templates and dynamic variables are correctly identified."
  - **FGA (F1 of Grouping Accuracy)** — harmonic mean of PGA = Nc/Np (correctly grouped templates
    over parser-generated templates) and RGA = Nc/Ng (correctly grouped templates over
    ground-truth templates). FGA = 2·PGA·RGA/(PGA+RGA). Template-level, so it is *not* dominated
    by high-frequency templates the way GA is.
  - **FTA (F1 of Template Accuracy)** — same precision/recall construction, but a template counts
    as correct only if (1) its message set matches ground truth **and** (2) every token matches
    exactly.
  - Why this matters for the corpus: GA is message-weighted and therefore insensitive to failures
    on rare templates — exactly the templates that carry incidents. A compliance provision that
    only requires "grouping accuracy above X" is gameable; the corpus should require FGA/FTA
    reporting alongside GA. This is a **P** (procedure precedent) contribution regardless of the
    data licence.

### 1.3 GAIA / MicroSS (CloudWise)

- URL: https://github.com/CloudWise-OpenSource/GAIA-DataSet
- Contents: MicroSS — a microservice system trace with **>6,500 metrics, ~7,000,000 log items**
  and trace data over two weeks (July 2021, extended with August 2021 in v1.10), plus companion
  data of **406 anomaly-detection/metric-prediction series (279 labelled)** and 218,736 log items
  for log parsing / semantic anomaly detection / NER.
- Ground truth: full **anomaly injection records** (so cases are reproducible), binary point
  labels (0 normal / 1 anomalous), and labelled series categories including changepoint, periodic,
  and concept drift.
- **Licence — CONFLICTING:** the raw `LICENSE` file in the repo is **GNU GPL v2**, while the
  README text states Apache 2.0. A GPL-2.0 file governing a dataset is almost certainly a
  packaging mistake, but it is the licence actually shipped. **REFERENCE-ONLY.** Do not vendor.
- Reuse: **F, D**. The changepoint / periodic / concept-drift label taxonomy is a good source of
  factor names distinguishing *drift* from *incident*.

---

## 2. Time-series anomaly benchmarks with labels

### 2.1 NAB — Numenta Anomaly Benchmark

- URL: https://github.com/numenta/NAB
- Contents: **58 time-series data files** (~365k data points total across real and artificial
  streams: AWS CloudWatch server metrics, ad click-through, traffic, tweet volume, machine
  temperature, plus synthetic streams).
- Ground truth: **anomaly windows**, not points — `labels/combined_windows.json` gives a window
  per anomaly; the scoring function gives full credit for the earliest detection inside a window
  and applies a decaying reward across it, with explicit false-positive penalties. Three
  application profiles: Standard, Reward Low FP, Reward Low FN. Score normalised so a perfect
  detector = 100.0 and the null detector = 0.0.
- **Licence — VERIFIED and CHANGED over time:** `LICENSE.txt` at HEAD is **MIT, "Copyright
  2014-2024 Numenta Inc."** Historically NAB was AGPLv3; anyone working from an older checkout or
  an older paper's claim will have the wrong licence. Verify the licence at the exact commit you
  vendor. At current HEAD: **VENDOR (MIT)**.
- Caveat: NAB is one of the four benchmarks explicitly criticised by Wu & Keogh (see 2.6). Its
  *scoring model* is more defensible than its *data*.
- Reuse: **P (strong), O (weak), D**. The three application profiles are the single best precedent
  for a compliance provision that says "the alerting change must not degrade under a
  cost-of-false-positive weighting chosen in advance." Cite the profile mechanism; do not treat
  NAB scores as evidence of detector quality.

### 2.2 Yahoo Webscope S5 (A1–A4)

- URL: https://webscope.sandbox.yahoo.com/catalog.php?datatype=s&did=70
- Contents: real Yahoo service traffic (A1) plus synthetic series (A2–A4) with tagged anomaly
  points, covering outliers and change-points. Distribution size 16 MB.
- **Licence — VERIFIED REQUEST-GATED AND NON-COMMERCIAL.** From the Webscope programme page:
  datasets are *"only available for academic use by faculty and university researchers who agree
  to the Data Sharing Agreement."* Requests must come from an accredited institutional address
  (.edu or international equivalent). The programme explicitly **cannot** share data with
  "Commercial entities", "Employees of commercial entities with university appointment", or
  "Research institutions not affiliated with a research university."
- Verdict: **REFERENCE-ONLY — HARD BLOCK.** A commercial datacenter-monitoring vendor is
  categorically ineligible. Do not vendor, do not depend on it in CI, do not cite it as a corpus
  oracle. Cite only the *critiques* of it.
- Reuse: **P only** (as the negative example in a provision about benchmark provenance).

### 2.3 SMD — Server Machine Dataset (OmniAnomaly)

- URL: https://github.com/NetManAIOps/OmniAnomaly (folder `ServerMachineDataset/`)
- Contents: **28 machines from a large Internet company, 38 dimensions each, 5 weeks**, split
  into three entity groups; for each machine the first half is train, the second half is test.
- Ground truth: `test_label` (point-level anomaly boolean) **plus `interpretation_label` — the
  list of dimensions that contributed to each anomaly.** The dimension-level attribution is the
  most useful thing here and is rare among public sets.
- **Licence:** repo `LICENSE` is **MIT (Copyright (c) 2021 NetManAIOps-OmniAnomaly)**. There is
  **no separate data licence statement**, and the data originates from an unnamed third-party
  Internet company. The MIT file nominally covers the repository contents; a conservative reading
  is that MIT was intended for the code. Verdict: **VENDOR WITH CAUTION** — MIT is the only stated
  licence and it covers the repository, but flag the provenance ambiguity in the corpus
  provenance record rather than asserting a clean grant.
- Caveat: SMD is criticised in the TSB-AD line of work for label noise and trivially-detectable
  anomalies.
- Reuse: **F (strong), O, D**. `interpretation_label` maps directly onto a boolean factor like
  `contributing_dimensions_identified` / `attribution_evidence_retained` — i.e. the corpus can
  demand not just "the detector fired" but "the detector named the right signal."

### 2.4 SMAP / MSL (NASA, via telemanom)

- URL: https://github.com/khundman/telemanom
- Contents: **SMAP** — 55 telemetry channels, 69 labelled anomaly sequences, 429,735 evaluated
  telemetry values. **MSL (Curiosity)** — 27 channels, 36 anomaly sequences, 66,709 values.
- Ground truth: anomaly sequences (intervals), each categorised **point (SMAP 43/62%, MSL 19/53%)
  vs contextual (SMAP 26/38%, MSL 17/47%)**.
- Format: `.npy`, shape `(n_timesteps, n_inputs)`, values pre-scaled to (−1,1) using **test-set**
  min/max, time-anonymised.
- **Licence:** repo code is **Apache 2.0**. The repository **does not state a licence for the
  telemetry data itself** and does not assert public-domain status. Verdict: **REFERENCE-ONLY for
  the data**; Apache 2.0 for the code only. Never guess "NASA therefore public domain" — it is not
  stated here.
- Additional defect worth recording: pre-scaling by test-set statistics is test-set leakage baked
  into the distribution.
- Reuse: **F (point vs contextual anomaly distinction is a clean boolean factor pair), P**.

### 2.5 Exathlon

- URL: https://github.com/exathlonbenchmark/exathlon
- Contents: real traces from repeated executions of large-scale Spark streaming jobs on a real
  cluster, with **six types of anomalous events** injected during execution.
- Ground truth: labels supporting both **anomaly detection (AD) and explanation discovery (ED)** —
  i.e. root-cause/explanation ground truth, not just detection ground truth.
- **Licence — VERIFIED SPLIT:** code **Apache 2.0** (repo `LICENSE`); **dataset CC BY-NC-SA 4.0**.
  Verdict: **REFERENCE-ONLY / NON-COMMERCIAL.** The NC clause blocks use inside a commercial
  vendor's conformance corpus, and the SA clause would additionally attempt to relicense
  derivatives. Do not vendor.
- Reuse: **F, P**. The AD-vs-ED separation is the right shape for factor facts that distinguish
  "detected" from "explained".

### 2.6 The critique: Wu & Keogh, and the UCR Anomaly Archive

- Paper: Renjie Wu & Eamonn Keogh, *"Current Time Series Anomaly Detection Benchmarks are Flawed
  and are Creating the Illusion of Progress"* — https://arxiv.org/abs/2009.13807 (also IEEE TKDE).
  Author page: https://wu.renjie.im/research/anomaly-benchmarks-are-flawed/
- Four named flaws, applying to Yahoo, Numenta/NAB, NASA (SMAP/MSL) and OMNI/SMD:
  1. **Triviality** — many exemplars are solved by a one-line brute-force method. Reported:
     **65.7%–98% of Yahoo A1–A4 solvable by elementary techniques (86.1% figure in their Table 1).**
  2. **Run-to-failure bias** — anomalies cluster non-randomly at the end of the series, so a
     detector that simply flags late timestamps scores well.
  3. **Mislabelled ground truth** — incorrect annotations in the source datasets.
  4. **Unrealistic anomaly density** — anomaly concentration does not match production.
- Their replacement: the **UCR Time Series Anomaly Archive**, ~200 datasets (train/test split for
  the SIGKDD 2021 contest; commonly cited as 250 in later releases), spanning medicine, industry,
  human and animal behaviour, with **exactly one anomaly location to be identified per series**.
  **Licence: Creative Commons BY-NC 4.0 (non-commercial).** Verdict: **REFERENCE-ONLY /
  NON-COMMERCIAL.**
- **Why this matters for the corpus, stated plainly:** a compliance corpus that cites a flawed
  benchmark inherits the flaw. If a provision says "the release must not regress detection recall
  on benchmark B," and B has run-to-failure bias, then a change that biases the detector toward
  late-window firing *passes* the provision while degrading production behaviour. The corpus
  should therefore carry an explicit boolean factor about benchmark provenance (see factor list),
  and should never treat "score improved on NAB/Yahoo/SMAP/SMD" as sufficient evidence.
- Reuse: **P — the single highest-value item in this lane.** It is a paper, not data; free to cite.

### 2.7 TSB-AD (successor benchmark, NeurIPS 2024 D&B)

- URL: https://github.com/TheDatumOrg/TSB-AD — homepage https://thedatumorg.github.io/TSB-AD/
  Paper: Liu & Paparrizos, *"The Elephant in the Room: Towards A Reliable Time-Series Anomaly
  Detection Benchmark"*, NeurIPS 2024 Datasets & Benchmarks.
- Contents: **1,070 curated high-quality time series drawn from 40 datasets**, split into
  TSB-AD-U (univariate) and TSB-AD-M (multivariate). Built specifically to remove the flaws above
  by combining "human perception and model interpretation" to re-curate labels.
- Evaluation: **40 detectors** — 17 statistical, 12 neural, 5 foundation-model (Chronos, TimesFM
  and similar). Headline methodological finding for us: **VUS-PR is recommended as the most
  reliable measure**; point-adjusted F1, the metric most AIOps papers report, is the one that
  manufactures the illusion of progress.
- **Licence:** code **Apache 2.0** (verified raw LICENSE). **Data: no blanket grant** — the repo's
  disclaimer states the datasets are "released for reproducibility purposes" and directs users to
  "refer to the original data source"; per-dataset licences are listed on the project homepage.
  Verdict: **VENDOR the code (Apache 2.0); REFERENCE-ONLY for the aggregated data**, and if any
  subset is vendored it must be cleared dataset-by-dataset at the original source.
- Reuse: **P (strong), O**. If the corpus needs a named metric for "did the anomaly detector
  regress", VUS-PR with TSB-AD's protocol is the most defensible current choice, and it is
  citable without redistributing anything.

### 2.8 Supporting evaluation frameworks (code, not data)

- **TimeEval** — https://github.com/HPI-Information-Systems/TimeEval — **MIT** (verified).
  Distributed evaluation harness for TSAD algorithms; useful as the execution shell for an
  in-house regression oracle. **VENDOR.**
- **TODS** — https://github.com/datamllab/tods — **Apache 2.0** (verified). Automated
  outlier-detection system for multivariate time series. **VENDOR.**
  (Note: "TODS" and "UCR archive" are distinct things and are sometimes conflated; TODS is a
  library, the UCR archive is data.)

---

## 3. Cluster, VM and trace datasets

### 3.1 Google cluster traces

- URL: https://github.com/google/cluster-data
- Contents: **ClusterData2011 (v2)** — one 12.5k-machine Borg cell, May 2011.
  **ClusterData2019 (v3)** — eight Borg cells over May 2019 (protobuf schema
  `clusterdata_trace_format_v3.proto`, distributed via BigQuery). **Power traces** — 57 power
  domains for May 2019, time-synchronised with ClusterData2019. Plus an ETA (Exploratory Testing
  Architecture) execution trace. v1 (2009) deprecated.
- **Licence — VERIFIED:** *"The data and trace documentation are made available under the CC-BY
  license. By downloading it or using them, you agree to the terms of this license."* The page
  says "CC-BY" without pinning a version number; treat as CC BY (record the ambiguity, and if a
  version must be asserted, ask Google rather than assuming 4.0).
- Verdict: **VENDOR (CC-BY, attribution required)** — the most permissively licensed large-scale
  datacenter workload data available.
- Ground truth: **none for anomalies.** These are workload traces, not labelled incident data.
  The 2019 power traces are directly relevant to the platform's thermal/capacity analytics lane.
- Reuse: **D (primary), F**. Use for realistic machine counts, task churn rates, resource-request
  distributions, and power-domain granularity so that corpus fixtures ("a change affecting 8 cells
  / 12,500 machines") are grounded rather than invented.

### 3.2 Alibaba cluster traces

- URL: https://github.com/alibaba/clusterdata
- Contents (verified list): v2017 (~1,300 machines, 12 h, online services + batch collocation);
  v2018 (~4,000 machines, 8 days, with batch DAG information); cluster-trace-gpu-v2020 (6,500+
  GPUs / ~1,800 machines, 2 months, PAI MLaaS); **cluster-trace-microservices-v2021 (20,000+
  microservices, 12 h, with call dependencies, response time, call rates)**;
  cluster-trace-microarchitecture-v2022 (AMTrace, fine-grained microarchitectural metrics);
  cluster-trace-gpu-v2023 (6,200+ GPUs, heterogeneous); cluster-trace-gpu-v2025 (150+ inference
  services, 20k+ instances, disaggregated DLRM serving); cluster-trace-gpu-v2026 (155,410 GPUs,
  37,707 servers, 6 months, serverless infrastructure); cluster-trace-v2026-GenAI (top-down view
  of diffusion-model serving across application/middleware/infrastructure layers).
- **Licence — VERIFIED RESTRICTIVE, NO LICENCE FILE.** There is **no `LICENSE` file** in the
  repository (confirmed 404). The README states: *"You may use trace however you want as long as
  it is for research or study purpose"* and *"We encourage anyone to use the traces for study or
  research purposes."* v2017 and v2018 additionally require **completing a short survey** before
  the download link is released.
- Verdict: **REFERENCE-ONLY.** "Research or study purpose" excludes a commercial vendor's
  shipped conformance corpus, and there is no licence instrument to rely on.
- Reuse: **D, F** — but only as *knowledge* informing plausible distributions, not as bytes. The
  microservices-v2021 call-dependency structure is the best public reference for realistic
  microservice topology fan-out, which is what the topology-correlation factors need to be
  calibrated against.

### 3.3 Azure Public Dataset (Microsoft)

- URL: https://github.com/Azure/AzurePublicDataset
- Contents: **AzurePublicDatasetV1 (2017)** ~2M VMs / 1.2B utilisation readings;
  **V2 (2019)** ~2.6M VMs / 1.9B readings; **AzureTracesForPacking2020** (VM requests with
  priority, lifetime, normalised resource allocations); **AzureFunctionsDataset2019**
  (per-minute invocation frequency, function→application grouping, execution-time and memory
  distributions); **AzureFunctionsInvocationTrace2021** (2-week arrival/departure timestamps);
  **AzureFunctionsBlobDataset2020**; **AzureLLMInferenceDataset2023 / 2024**;
  **AzureLMMInferenceDataset2025**; **AzureVMNoiseDataset2024** (performance-variability
  benchmarks, May 2023–Sep 2024).
- **Licence — VERIFIED:** the repository's raw `LICENSE` is **Creative Commons Attribution 4.0
  International (CC BY 4.0)**; the repo also carries MIT for code. Per-dataset citation of the
  associated paper is requested.
- Verdict: **VENDOR (CC BY 4.0)** — the cleanest large-scale licence in this lane.
- Ground truth: none for anomalies. **AzureVMNoiseDataset2024 is quietly the most useful item
  here for us**: it is a published measurement of *performance variability under nominally
  identical conditions*, which is exactly the noise floor a "did the detector regress" provision
  must sit above.
- Reuse: **D (primary), O (for noise-floor calibration)**.

### 3.4 Microservice benchmark applications (systems under test, not datasets)

- **DeathStarBench** — https://github.com/delimitrou/DeathStarBench — **Apache 2.0** (verified).
  Social Network, Media Service, Hotel Reservation, and other end-to-end microservice suites with
  distributed tracing instrumentation. It is the substrate for AIOpsLab and much RCA work.
  **VENDOR.**
- **Train Ticket** — https://github.com/FudanSELab/train-ticket — **Apache 2.0** (verified).
  ~40-service railway ticketing system, the standard fault-replication testbed; used as one of
  the three systems in RCAEval. **VENDOR.**
- Reuse: **O**. These are the only components in this lane that let the corpus *generate* its own
  ground truth under a licence that permits commercial redistribution — inject a fault into
  Train Ticket or Hotel Reservation, and the injection record *is* the label. This is the
  recommended path for any case that needs an executable oracle.

---

## 4. Root-cause analysis benchmarks

### 4.1 RCAEval

- URL: https://github.com/phamquiluan/RCAEval — data on Figshare
  (https://figshare.com/articles/dataset/RCAEval_A_Benchmark_for_Root_Cause_Analysis_of_Microservice_Systems/31048672)
  and Zenodo (DOI 10.5281/zenodo.14590730).
- Contents: **nine datasets, 735 real failure cases**, plus an evaluation framework and **15
  reproducible baselines** (metric-, trace- and multi-source RCA).
  - **RE1** — 375 cases, metrics only, three microservice systems.
  - **RE2** — 270 cases, multi-source (metrics + logs + traces).
  - **RE3** — 90 cases, code-level faults.
  - Plus a further 270-case set associated with the TORAI method.
  - Systems: **Online Boutique, Sock Shop, Train Ticket**.
- Ground truth: per case, the **root-cause service** *and* the **root-cause indicator** (the
  specific metric or log identifying the cause). **11 fault types**: CPU, memory, disk, delay,
  packet loss, socket, and others.
- **Licence — VERIFIED:** *"For the code implemented by us and for our datasets, we distribute
  them under the MIT LICENSE."* Integrated third-party baselines keep their own licences
  (MIT / BSD-3-Clause / Apache-2.0).
- Verdict: **VENDOR (MIT)** — this is the strongest RCA item in the lane: large, labelled,
  permissively licensed, and explicitly covering the datasets as well as the code.
- Reuse: **F, D, O — all three.** The 11-fault-type taxonomy is the best available factor
  vocabulary for injected-fault classes; the 735 labelled cases are a directly usable oracle for
  topology/RCA regression; the split between "root-cause service" and "root-cause indicator"
  maps onto two separate boolean factors (service correctly localised vs signal correctly named).

### 4.2 PetShop (Amazon Science)

- URL: https://github.com/amazon-science/petshop-root-cause-analysis
- Contents: metrics from a distributed application of **41 components** (databases, load
  balancers, queues, storage, containerised microservices), with **68 injected performance
  issues** — request overload, memory leaks, CPU hog, latency-increasing and
  availability-reducing misconfigurations.
- Data: three metric families — **latency, requests, availability** — annotated with the
  corresponding issue as ground truth.
- **Licence — VERIFIED SPLIT AND FAVOURABLE:** code **Apache-2.0**; **dataset CC BY 4.0**.
- Verdict: **VENDOR (attribution)** — one of only two RCA datasets here with an unambiguous
  commercial-friendly data grant.
- Reuse: **F, D, O**. The latency/requests/availability triple is a natural, small, and
  well-motivated boolean factor family for golden-signal coverage.

### 4.3 AIOpsLab (Microsoft)

- URL: https://github.com/microsoft/AIOpsLab — paper https://arxiv.org/abs/2501.06706
- Contents: a *framework* — deploys microservice environments, injects faults, generates workload,
  exports telemetry, and provides an agent-environment interface. Built-in suite of **48 problems**
  (evaluated over 6 agents = 288 cases in the paper). Applications: **DeathStarBench
  HotelReservation and SocialNetwork**, extensible via Helm charts and metadata JSON.
- Task taxonomy and per-task metrics — this is the important part:
  - **L1 Detection** — accuracy, **Time-to-Detect (TTD)**.
  - **L2 Localization** — top-1 / top-3 accuracy, steps taken.
  - **L3 Root-cause analysis** — accuracy on system layer and fault type.
  - **L4 Mitigation** — success rate, **Time-to-Mitigate (TTM)**, steps.
  - Plus token consumption and number of agent-environment interactions.
- Fault taxonomy: **symptomatic faults** (levels 1–2: performance degradation, crash failures,
  network loss, pod failure) vs **functional faults** (levels 1–4: auth issues, Kubernetes
  misconfiguration, revoked credentials, buggy application images, incorrect scaling operations).
- **Licence:** the README states *"Licensed under the MIT license."* Note: a raw `LICENSE` /
  `LICENSE.md` fetch at `main` returned 404 in this check, so the MIT claim is from the README
  rather than a licence file at the path tried. The arXiv preprint itself is **CC BY-NC-ND 4.0**
  (paper text only, not the code). Verdict: **VENDOR the code as MIT, but confirm the licence
  file location before shipping**; cite the paper rather than reproducing its text.
- Reuse: **F (strongest source of task-level factor names in the whole lane), P, O**.

### 4.4 ITBench (IBM)

- URL: https://github.com/IBM/ITBench
- Contents: agent-evaluation scenarios on **Kubernetes-based environments**, across three domains:
  **SRE** (availability/resiliency) — 6 scenarios, 21 mechanisms; **CISO** (compliance and
  security enforcement) — 4 scenario categories; **FinOps** (cost efficiency) — 1 scenario.
  Provides deployment tooling to "replicate real-world incidents in Kubernetes environments" and
  a managed leaderboard.
- **Licence — VERIFIED: Apache 2.0** (raw LICENSE confirmed). **VENDOR.**
- Reuse: **F, P.** ITBench is the only benchmark found that puts *compliance enforcement* and
  *incident response* in the same agent-evaluation frame — directly analogous to what DCVigil's
  corpus is doing, and worth citing as prior art for the corpus's own structure.

### 4.5 LEMMA-RCA

- URL: https://lemma-rca.github.io/ — data hosted on Hugging Face.
- Contents: multi-modal datasets (metrics + logs) with real system faults, spanning IT operations
  (Product Review, Cloud Computing / OnlineBoutique) and OT operations (water treatment and
  distribution).
- **Licence — CONFLICTING AND NON-COMMERCIAL EITHER WAY.** The project website states the datasets
  are released under **CC BY-ND 4.0**; the repository `LICENSE` file states **CC BY-NC 4.0**
  ("The LEMMA-RCA benchmark dataset is released under a CC BY-NC 4.0 International License").
  ND forbids derivatives; NC forbids commercial use. Either clause independently blocks the
  intended use.
- Verdict: **REFERENCE-ONLY — HARD BLOCK.** Do not vendor, do not derive.
- Reuse: **P only.**

### 4.6 AIOps Challenge datasets (2020–2022, NetManAIOps)

- URL: https://github.com/NetManAIOps/AIOps-Challenge-2020-Data
- Contents (2020): three metric families — **business metrics, platform/infrastructure metrics,
  and traces** (span id / parent span id, OpenTracing-conformant) — organised as daily ZIPs,
  distributed via Tsinghua Cloud and Google Drive. Stage-one data available; stage-two not.
- Ground truth: a fault CSV (`故障整理（预赛）.csv`) giving **time, fault type, and fault location**
  per injected incident. Exact fault count not stated on the page.
- **Licence — VERIFIED RESTRICTIVE:** restricted to *"non-commercial purposes such as scientific
  research or classroom teaching"*, with users accepting full responsibility and indemnifying the
  organiser. Verdict: **REFERENCE-ONLY / NON-COMMERCIAL.**
- Reuse: **F, D.** The `(time, fault type, fault location)` triple is the minimal ground-truth
  schema an internal incident corpus should adopt.

### 4.7 Nezha

- URL: https://github.com/IntelligentDDS/Nezha — FSE 2023, interpretable fine-grained RCA.
- **Licence — VERIFIED: MIT** (raw LICENSE, Copyright (c) 2023 IntelligentDDS). **VENDOR.**
- Contents: multi-modal (metrics, logs, traces) data from Online Boutique and Train Ticket with
  fault injection records; produces *fine-grained* root causes (code/config level, not just
  service level).
- Reuse: **F, O.** Useful when a factor needs to distinguish "localised to a service" from
  "localised to a specific code/config element".

---

## 5. Incident management, alert fatigue and false positives

This is the **weakest-supplied area of the lane** and should be recorded as a gap in the corpus's
provenance notes.

- **danluu/post-mortems** — https://github.com/danluu/post-mortems — a widely-used curated
  collection of public postmortems. **No `LICENSE` file exists in the repository** (verified 404
  on both `LICENSE` and `LICENSE.md`). The entries are largely links to third-party postmortems
  each with its own terms. Verdict: **REFERENCE-ONLY.** Usable as a reading list for deriving
  factor names; not vendorable, and the underlying postmortems are individually copyrighted.
- **Operations-Incident-Board / Postmortem-Report-Reviews** —
  https://github.com/Operations-Incident-Board/Postmortem-Report-Reviews — **CC0 1.0 Universal**
  (verified raw LICENSE). Structured *reviews* of published postmortem reports. Verdict:
  **VENDOR (CC0)** — small, but it is the only public-domain incident-analysis artefact found,
  and its review dimensions are a legitimate source of factor names for incident-record quality.
- **The VOID (Verica Open Incident Database)** — https://www.thevoid.community/ — described as
  "the leading community-contributed collection of software-related incident reports." **Access
  terms, report counts and download availability could not be verified** from the site's fetched
  content; the page returned only metadata. Verdict: **UNVERIFIED — do not rely on it** until
  someone reads the actual terms. Its published annual reports (notably the finding that MTTR is
  a poor and statistically unstable metric) are citable as **P**.
- **Alert fatigue / false-positive rates:** no open corpus with published per-alert ground truth
  was found in the IT-operations domain. The available literature is survey-grade — e.g.
  *"Alert Fatigue in Security Operations Centres: Research Challenges and Opportunities"*, ACM
  Computing Surveys (https://dl.acm.org/doi/10.1145/3723158) — and is security-SOC rather than
  datacenter-monitoring. Vendor-published false-positive percentages are marketing material with
  no released data and **must not** be cited as a baseline in the corpus.
- **Practical consequence:** the corpus's alert-precision provisions cannot be grounded in a
  public labelled alert corpus. They must instead be grounded in a *procedure* — a pre-registered
  labelling protocol on the tenant's own alert stream, with the labelling done before the change
  ships. Note this explicitly so the corpus does not appear to have skipped the question.

---

## 6. Remediation / autonomous-operations benchmarks (blast radius and safety)

- **AIOpsLab L4 Mitigation** (see 4.3) — success rate, TTM, step count. MIT (per README).
  The only mitigation benchmark here with a permissive licence and released code.
- **ITBench SRE scenarios** (see 4.4) — Apache 2.0, Kubernetes-based, agents actually act.
- **InfraBench** — https://arxiv.org/html/2608.11234, benchmark at infraben.ch. **12 seed tasks**
  across four infrastructure layers (L1 hardware/power, L2 local systems, L3 distributed systems
  such as Ceph/Slurm/Cassandra, L4 containerised applications), run on Docker, libvirt/KVM
  three-node clusters, and **three-node bare-metal clusters with IPMI/BMC control** on the
  CloudLab Wisconsin testbed. Its contribution is the **lifecycle gate structure**:
  **Functional** (the fix works) → **Durability** (the fix survives restart) → **Cleanup** (no
  residual state). Reported result: **agents pass 89% of functional checks but only 35.2% of
  cleanup checks.** It also runs an LLM-judge over recorded commands against a **seven-category
  danger taxonomy** including destructive operations, safety bypasses, and evaluator-harness
  probing, and names recurring failure modes: post-repair cleanup gaps, incomplete deployment
  residue, non-persistent fixes, hidden configuration drift, destructive side effects.
  **Licence: the paper is CC BY 4.0; the platform is described as open-source but the code
  licence was not verified.** Verdict: **cite as P; verify the code licence before vendoring.**
- **UnderSpecBench** — https://arxiv.org/html/2607.02294v1, *"Coding Agents Are Guessing:
  Measuring Action-Boundary Violations in Underspecified DevOps Instructions."* Defines
  **action-boundary violations** as two distinct failure classes: **Wrong Target** (acting on an
  unintended resource) and **OverScope** (exceeding authorised operational breadth — i.e. blast
  radius). **69 task families** across four DevOps lifecycle phases and nine operational control
  surfaces, expanded to **2,208 prompt variants** (69 × 4 × 4 × 2) by systematically varying
  instruction clarity, target certainty, and blast radius while holding the environment and the
  safe action fixed. Outcomes are scored by **deterministic side-effect-based oracles** into
  Safe Success / Wrong Target / OverScope. **Data and code release status and licence are not
  stated in the paper** — verdict: **REFERENCE-ONLY / UNVERIFIED**, but the *Wrong-Target vs
  OverScope* distinction is the most precise public formulation of blast radius found, and is
  free to adopt as vocabulary.

---

## 7. Consolidated licence table

| Source | Data licence (verified) | Vendor? |
|---|---|---|
| Google cluster traces | CC-BY (version unpinned on page) | **VENDOR** |
| Azure Public Dataset | CC BY 4.0 (raw LICENSE) | **VENDOR** |
| RCAEval (code + data) | MIT (explicit for datasets) | **VENDOR** |
| PetShop | code Apache-2.0; **data CC BY 4.0** | **VENDOR** |
| ITBench | Apache 2.0 | **VENDOR** |
| DeathStarBench | Apache 2.0 | **VENDOR** |
| Train Ticket | Apache 2.0 | **VENDOR** |
| Nezha | MIT | **VENDOR** |
| NAB | MIT at HEAD (was AGPLv3 historically — pin the commit) | **VENDOR, pin commit** |
| TimeEval | MIT | **VENDOR** |
| TODS | Apache 2.0 | **VENDOR** |
| Postmortem-Report-Reviews | CC0 1.0 | **VENDOR** |
| AIOpsLab | MIT per README; LICENSE file not found at path tried | VENDOR after confirming file |
| TSB-AD | code Apache 2.0; **data: no blanket grant, per-source** | code only |
| SMD / OmniAnomaly | MIT (repo-wide); no separate data grant; third-party provenance | caution |
| SMAP / MSL (telemanom) | code Apache 2.0; **data licence unstated** | **REFERENCE-ONLY** |
| Loghub | repo LICENSE: research/academic only; Zenodo: CC BY 4.0 — **conflict** | **REFERENCE-ONLY** |
| Loghub-2.0 | same conflict; GitHub MIT badge is wrong for data | **REFERENCE-ONLY** |
| GAIA / MicroSS | LICENSE file GPL-2.0; README says Apache 2.0 — **conflict** | **REFERENCE-ONLY** |
| Alibaba cluster traces | no LICENSE file; "research or study purpose"; survey-gated (v2017/18) | **REFERENCE-ONLY** |
| Exathlon | code Apache 2.0; **data CC BY-NC-SA 4.0** | **REFERENCE-ONLY (NC)** |
| UCR Anomaly Archive | CC BY-NC 4.0 | **REFERENCE-ONLY (NC)** |
| LEMMA-RCA | CC BY-ND 4.0 (site) vs CC BY-NC 4.0 (LICENSE) — **conflict, NC/ND either way** | **HARD BLOCK** |
| AIOps Challenge 2020 | non-commercial (research/teaching) only | **REFERENCE-ONLY (NC)** |
| Yahoo Webscope S5 | **request-gated, academic-only, commercial entities ineligible** | **HARD BLOCK** |
| danluu/post-mortems | **no licence file** | **REFERENCE-ONLY** |
| The VOID | **unverified** | do not rely on |
| InfraBench | paper CC BY 4.0; platform licence unverified | cite only |
| UnderSpecBench | release status unstated | cite only |

---

## 8. Proposed factor names

Boolean factor facts, phrased so each is decidable from a release record. Grouped by the four
areas named in the brief.

### 8.1 Anomaly-detection regression

- `detector_evaluated_on_pinned_held_out_corpus`
- `evaluation_corpus_version_and_hash_recorded`
- `benchmark_provenance_reviewed_for_known_flaws` — the Wu & Keogh factor; true only if the
  benchmark was checked for triviality, run-to-failure bias, mislabelled ground truth and
  unrealistic anomaly density.
- `benchmark_is_sole_evidence_of_non_regression` — a *disqualifying* factor; a corpus provision
  should fire when this is true.
- `recall_regression_within_prespecified_tolerance`
- `precision_regression_within_prespecified_tolerance`
- `threshold_free_metric_reported` (VUS-PR or AUC-PR, per TSB-AD)
- `point_adjusted_f1_used_as_primary_metric` — disqualifying; point-adjustment inflates scores.
- `per_entity_results_reported_not_only_aggregate` — SMD's 28 machines make aggregate-only
  reporting hide per-tenant regressions.
- `contributing_dimensions_identified` — SMD `interpretation_label` analogue: the detector names
  the signal, not just the timestamp.
- `rare_template_performance_reported` — the FGA/FTA lesson applied to detection.
- `regression_evaluated_above_measured_noise_floor` — grounded in AzureVMNoiseDataset2024.
- `detection_latency_ttd_recorded` (AIOpsLab L1)
- `seasonal_and_drift_cases_included_in_evaluation` (GAIA changepoint / concept-drift categories)

### 8.2 Alert precision / recall and false positives

- `alert_labelling_protocol_preregistered_before_change`
- `alert_ground_truth_labelled_by_independent_reviewer`
- `false_positive_rate_measured_on_labelled_sample`
- `false_negative_rate_measured_on_labelled_sample`
- `alert_volume_delta_per_tenant_recorded`
- `cost_weighting_of_false_positives_declared_in_advance` — NAB's Reward-Low-FP / Reward-Low-FN
  profiles as precedent; the weighting must be fixed before results are seen.
- `alert_suppression_change_reviewed_for_silent_coverage_loss`
- `paging_alerts_separated_from_ticketing_alerts_in_metrics`
- `vendor_published_fp_rate_used_as_baseline` — disqualifying; no released data exists behind
  such figures.

### 8.3 Topology correlation accuracy

- `root_cause_service_localisation_accuracy_measured` (RCAEval root-cause service)
- `root_cause_indicator_identified_not_only_service` (RCAEval root-cause indicator)
- `top1_and_top3_localisation_reported` (AIOpsLab L2)
- `correlation_evaluated_across_service_dependency_edges`
- `topology_snapshot_version_recorded_with_result` — topology drifts; a correlation score without
  the topology it was computed against is unfalsifiable.
- `fault_type_coverage_declared` — against a named taxonomy (RCAEval's 11 types: CPU, memory,
  disk, delay, packet loss, socket, …; or AIOpsLab's symptomatic vs functional split).
- `symptomatic_and_functional_faults_both_covered` (AIOpsLab)
- `multi_source_signals_used_metrics_logs_traces` (RCAEval RE2)
- `cross_tenant_correlation_isolation_verified` — multi-tenant-specific; correlation must not
  leak topology or incident signal across tenant boundaries.
- `golden_signal_coverage_latency_requests_availability` (PetShop's three metric families)

### 8.4 Shadow evaluation before live scoring

- `model_run_in_shadow_before_live_scoring`
- `shadow_duration_meets_minimum_declared_window`
- `shadow_traffic_representative_of_production_mix`
- `shadow_outputs_not_routed_to_paging_or_remediation`
- `shadow_vs_incumbent_disagreement_rate_recorded`
- `shadow_evaluation_covers_peak_and_seasonal_window`
- `promotion_criteria_declared_before_shadow_started`
- `rollback_path_verified_during_shadow`
- `shadow_results_reviewed_by_someone_other_than_author`

### 8.5 Remediation safety / blast radius

(Adjacent to the lane but directly supplied by InfraBench and UnderSpecBench, and worth carrying.)

- `action_target_uniquely_identified_before_execution` (UnderSpecBench: Wrong Target)
- `action_scope_bounded_to_minimum_necessary` (UnderSpecBench: OverScope)
- `blast_radius_declared_before_action`
- `fix_verified_durable_across_restart` (InfraBench Durability gate)
- `post_remediation_residual_state_cleaned_up` (InfraBench Cleanup gate — the gate agents fail
  64.8% of the time)
- `destructive_operation_gated_by_human_confirmation`
- `time_to_mitigate_recorded` (AIOpsLab L4 TTM)

---

## 9. Recommended posture

1. **Build the executable oracle on Train Ticket / DeathStarBench / RCAEval / PetShop.** These
   four are Apache-2.0 or MIT or CC BY 4.0 with *explicit* data grants, and together they give
   735 + 68 labelled failure cases plus two deployable systems for generating more. Everything
   the corpus needs as an executed oracle can come from here, cleanly.
2. **Take Loghub, Alibaba, GAIA, UCR, Exathlon, LEMMA-RCA and Yahoo as knowledge, not bytes.**
   Their taxonomies, protocols and findings are free to use; their files are not.
3. **Treat the Wu & Keogh critique as a corpus provision, not a footnote.** The corpus should
   require a positive assertion that the benchmark's provenance was reviewed. This is the single
   highest-value idea in the lane and costs nothing to adopt.
4. **Record the alert-fatigue gap explicitly.** There is no public labelled alert corpus for IT
   operations. Ground those provisions in a pre-registered labelling procedure instead.
5. **Re-verify every licence at the commit/version you vendor.** NAB has already changed
   (AGPLv3 → MIT), three of these repositories carry a licence file that contradicts their own
   README or GitHub badge, and one (Alibaba) has no licence file at all.
