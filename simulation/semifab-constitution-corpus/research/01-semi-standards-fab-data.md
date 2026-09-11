# Lane 01 — Semiconductor Manufacturing Standards, Protocols and Fab Datasets

**Purpose.** Identify reusable, licence-verified open source material for an open compliance test
corpus governing software change in semiconductor manufacturing operations monitoring software
(fab monitoring, MES/EDA, yield and supply-chain control tower). Corpus case shape:
`(case id, provisions engaged, boolean factor facts, expected disposition)`.

**Research date:** 2026-09-05. Every licence below was verified by fetching the actual `LICENSE`
file, licence header, or the vendor's own licence/pricing page — never inferred from a badge, a
README claim, or a third-party summary. Where no licence could be verified, the row says
**NOT VERIFIED** and is classified REFERENCE-ONLY. No licence has been guessed.

**Method note.** `api.github.com` is blocked in this environment; `raw.githubusercontent.com` and
`git clone` work. All GitHub findings below come from actual shallow clones inspected on disk, not
from rendered HTML summaries.

---

## 0. Headline legal finding: SEMI standards text is NOT redistributable

Verified against SEMI's own licence agreement
(<https://semi.org/sites/semi.org/files/2020-07/p042447.pdf>), quoted verbatim:

> "non-exclusive, non-transferable license to download a File or Files as appropriate to the fee
> paid, to use these File(s) internally on **a single computer**"

> "You may not copy (except as set forth herein), sell, rent, lease, sublicense, assign, loan,
> time-share, **share through an internal computer network** or otherwise transfer or distribute
> the Files."

The single permitted exception is backup/archival copies retaining SEMI's copyright notices.

Verified prices (SEMI Store, `store-us.semi.org`, 2026-09-05):

| Standard | Member | Non-member |
|---|---|---|
| SEMI E4 (SECS-I) | $148.00 | $193.00 |
| SEMI E5 (SECS-II) | $286.00 | (not displayed) |
| SEMI E30 (GEM) | $286.00 | $380.00 |
| SEMI E30.1 (ISEM) | $148.00 | $193.00 |
| SEMI E32 | $148.00 | $193.00 |
| SEMI E134 (DCM) | $148.00 | $236.00 |

**Consequence for the corpus.** No SEMI specification *text*, table, figure, state diagram, or
message-structure listing may be vendored. However:

- **Identifiers and designations are facts, not expression, and are freely citable.**
  `S7F23`, `S6F11`, `E30`, `E37.1`, `E87`, `CEID`, `PPID`, `ACKC7`, `HSMS Select.req` are names of
  things. A provision reference of the form `SEMI E30 §<n>` is a *citation*, exactly as a case
  citation is; it does not reproduce the provision.
- The corpus must therefore state provisions **by reference** (`"provisions_engaged":
  ["SEMI-E30", "SEMI-E37.1", "SEMI-E5"]`) and carry its **own** paraphrased normative text, or
  none at all — with factor facts doing the work.
- Every fixture, factor value and oracle below is drawn from independently-licensed open source
  implementations, never from the standards.

Verified full official titles (from SEMI's own Information & Control standards index,
<https://www.semi.org/en/products-services/standards/information_and_control>, and the SEMI Store
product names — these titles are citable bibliographic facts):

| Designation | Official title |
|---|---|
| SEMI E4 | Specification for SEMI Equipment Communications Standard 1 Message Transfer (SECS-I) |
| SEMI E5 | Specification for SEMI Equipment Communications Standard 2 Message Content (SECS-II) |
| SEMI E30 | Specification for the Generic Model for Communications and Control of Manufacturing Equipment (GEM) |
| SEMI E37 | Specification for High-Speed SECS Message Services (HSMS) Generic Services |
| SEMI E37.1 | HSMS Single-Session Mode (HSMS-SS) |
| SEMI E39 | Specification for Object Services: Concepts, Behavior, and Services |
| SEMI E40 | Specification for Processing Management |
| SEMI E87 | Specification for Carrier Management (CMS) |
| SEMI E90 | Specification for Substrate Tracking |
| SEMI E94 | Specification for Control Job Management |
| SEMI E116 | Specification for Equipment Performance Tracking (EPT) |
| SEMI E120 | Specification for the Common Equipment Model (CEM) |
| SEMI E125 | Specification for Equipment Self Description (EqSD) |
| SEMI E128 | Specification for XML Message Structures |
| SEMI E132 | Specification for Equipment Client Authentication and Authorization |
| SEMI E134 | Specification for Data Collection Management (DCM) |
| SEMI E138 | Specification for XML Semiconductor Common Components |
| SEMI E157 | Specification for Module Process Tracking |
| SEMI E164 | Specification for EDA Common Metadata |
| SEMI E179 | Specification for Protocol Buffers Common Components (Freeze 3) |
| SEMI E134.1 | Specification for SOAP Binding of DCM |
| SEMI E134.2-1225 | Specification for Protocol Buffers of DCM |

---

## 1. Master source table

Columns: **Name / URL / What it actually is / Format / VERIFIED licence / Volume / Reuse path in
the corpus / Vendor?**

### 1.1 SECS/GEM protocol implementations

| # | Name & URL | What the data actually is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 1 | **go-secs** — <https://github.com/arloliu/go-secs> | Go SECS-I/SECS-II/HSMS/HSMS-SS/GEM library. Critically, ships `sml/testdata/common.sml` — **189 named, hand-written real SECS message fixtures** spanning **140 distinct stream/functions**, including S7F23, S3F17 carrier actions, S16F15 process job create, S14F9 control job create, S4F81–95. Also a real benchmark harness over loopback TCP. | Go source; `.sml` text fixtures; Go benchmarks | **Apache-2.0** — verified: `LICENSE` file opens "Apache License / Version 2.0, January 2004"; also declared Apache-2.0 on pkg.go.dev | 7.5 MB, 320 `.go` files; `common.sml` = 1568 lines / 189 fixtures | **Best single source.** (a) **Message fixtures** — vendor `common.sml` directly as the corpus's canonical wire-artefact set; each named fixture (`CancelCarrier`, `CreateProcessJob`, `FPS`) becomes a case attachment. (b) **Factor vocabulary** — the 140 S/F codes and 189 fixture names. (c) **Oracle** — round-trip encode/decode tests are a ground-truth parser oracle. (d) **Latency budget facts** — verified defaults `T3=45s, T5=10s, T6=5s, T7=10s, T8=5s` in `hsms/connection_config.go`. | **YES — VENDOR** |
| 2 | **secsgem** — <https://github.com/bparzella/secsgem> | Python SECS/GEM. 124 stream/function classes each with the **official message name** ("Event Report Send (ERS)"), direction (`to_host`/`to_equipment`), reply-required and multi-block flags. 128 data-item classes with **enumerated ack/error code values** (e.g. `ACKC7`: ACCEPTED=0, NO_PERMISSION=1, LENGTH_ERROR=2, MATRIX_OVERFLOW=3, PPID_NOT_FOUND=4, MODE_UNSUPPORTED=5, PERFORMED_LATER=6). GEM control/communication state machines. HSMS byte-level test fixtures. | Python; docstring tables; byte-string test fixtures | **LGPL-2.1-or-later** — verified: `LICENSE` = LGPL 2.1 text; `pyproject.toml` `license = "LGPL-2.1-or-later"`; each source file carries the LGPL header | 24 MB; 405 `.py`; 136 function files; 128 data items; 10,003 lines of tests | **Factor vocabulary (primary).** The 124 `(S,F) → name, direction, reply-required, multi-block` tuples are exactly the boolean factor facts a compliance case needs (`msg_requires_reply`, `msg_is_host_to_equipment`, `msg_is_multi_block`). The data-item enumerations are the **expected-disposition vocabulary** (`disposition: ACKC7.PPID_NOT_FOUND`). Extract as data, do not copy code. | **REFERENCE-ONLY for the code.** LGPL-2.1 is incompatible with re-licensing files into an Apache-2.0/CC-BY repo. Safe paths: (i) use unmodified as an *installed dependency* (LGPL permits this without relicensing the corpus); (ii) re-derive the vocabulary table as facts (S/F numbers and standard message names are facts) and cite secsgem as the source. Do **not** copy `.py` files in. |
| 3 | **pysemisecs** — <https://github.com/kenta-shimizu/pysemisecs> | Python 3 SECS-I (E4), SECS-II (E5), GEM (E30, partial), HSMS-SS (E37.1), plus an **SML parser** (PEER Group's SECS Message Language text format). | Python source | **Apache-2.0** — verified: `LICENSE` = Apache 2.0 text; `setup.py` `license="Apache-2.0"` | 796 KB, 20 files | Vendorable second implementation. Use as a **differential oracle**: parse the same SML fixture with go-secs and pysemisecs; a disagreement is a corpus-worthy defect case. Its SML parser lets the corpus stay in a human-readable message format. | **YES — VENDOR** |
| 4 | **semi-rs** — <https://github.com/NathanielHardesty/semi-rs> | Rust crates `semi_e37` (HSMS) and `semi_e5` (SECS-II), incl. a units table. E4/E30/E39/E40/E87/E90/E94/E116/E148/E157 declared as planned, not implemented. | Rust source | **MIT** — verified: `license.md` = MIT text, "Copyright © 2024 Nathaniel Hardesty" | 724 KB; ~7,541 lines across `semi_e5` + `semi_e37` | Third differential-oracle implementation; a memory-safe HSMS framer. `semi_e5/src/units.rs` (240 lines) is a citable **units vocabulary** for metrology factor facts. Author explicitly disclaims SEMI endorsement — good precedent language for the corpus README. | **YES — VENDOR** |
| 5 | **secs-simulator** — <https://github.com/LostCat-Qian/secs-simulator> | SECS simulator GUI built on electron-egg + secs4js. | JS/Electron | **Apache-2.0** — verified via `raw.githubusercontent.com/.../LICENSE` on both `master` and `main`: Apache License 2.0 | (not cloned) | An actual runnable **host/equipment simulator** under a vendorable licence — the "gem-simulator" the brief asked for. Use to *generate* HSMS traffic for cases where no public capture exists (see §5). | **YES — VENDOR** |
| 6 | **hsms (JS)** — <https://github.com/megahoneybadger/hsms> | JavaScript HSMS protocol driver. | JS | **Apache-2.0** — verified via raw `LICENSE` on `master`: "Apache License" | (not cloned) | Fourth implementation for differential testing; browser-side fixture rendering. | **YES — VENDOR** |
| 7 | **go-factory-io** — <https://github.com/seikaikyo/go-factory-io> | Go SECS/GEM driver (E5/E30/E37). | Go | **PROPRIETARY** — verified: `LICENSE` reads "Copyright (c) 2026 SeiKai Kyo. **All rights reserved.**" | — | Cite only. | **REFERENCE-ONLY** |
| 8 | **Wireshark HSMS dissector** — <https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-hsms.c> | Mainline Wireshark dissector for HSMS (E37) carrying SECS-II (E5). 770 lines. Contains the canonical **PType**, **SType** and **SECS-II item format-code** value tables. Exposes **27 display-filter fields** (`hsms.header.stream`, `hsms.header.function`, `hsms.header.wbit`, `hsms.data.item.format`, `hsms.length`, …) — Wireshark 2.4.0 → 4.6.8. | C source; display-filter field registry | **GPL-2.0-or-later** — verified: `SPDX-License-Identifier: GPL-2.0-or-later` in the file header, "Copyright 2016, Benjamin Parzella" | 770 lines | (a) The **27 display-filter field names** are a ready-made, stable, citable **factor namespace** for protocol-level facts — the corpus can name factors `hsms.header.wbit == true` and a reader can verify them in Wireshark. (b) Wireshark itself is a **third-party oracle**: decode a corpus fixture with `tshark` and compare. (c) The SType table is authoritative: `Data.msg(0) Select.req(1) Select.rsp(2) Deselect.req(3) Deselect.rsp(4) Linktest.req(5) Linktest.rsp(6) Reject.req(7) Separate.req(9)`. | **REFERENCE-ONLY for the C source** (GPL-2.0 cannot be relicensed into Apache-2.0). Using `tshark` as an external tool, and citing field names, is unrestricted. |

### 1.2 EDA / Interface A (SEMI E120/E125/E132/E134/E138/E164/E179)

| # | Name & URL | What it is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 9 | **SEMI EDA standards** (E120, E125, E128, E132, E134, E138, E164, E179 + `.1` SOAP and `.2` protobuf bindings) — `store-us.semi.org` | The specifications themselves. | PDF | **PAYWALLED, non-redistributable** — see §0. E134 verified $148 member / $236 non-member. | — | Cite designations only. | **REFERENCE-ONLY** |
| 10 | **Metadata Conformance Analyzer (MCA) v1.2** — <https://www.peergroup.com/resources/metadata-conformance-analyzer-mca-download/> | Free third-party Java tool, developed by **ISMI/NIST**, that imports equipment EDA metadata and evaluates it against the EDA standards and ISMI guidelines, reporting metadata errors and schema conflicts. Targets EDA Freeze 2 (0710). Requires JRE 6u16+. | Java binary | **NO OPEN LICENCE.** Verified terms: distributed free of charge, "AS IS", all warranty disclaimed, user assumes all risk (incl. Log4j exposure). **Source is not published.** Not an OSI licence. | (binary download) | **Conceptually the closest existing artefact to this corpus**: a rule-checker over equipment metadata producing pass/fail findings. Use its *finding taxonomy* as prior art for `expected_disposition` categories. Cannot be vendored or re-hosted; link only. | **REFERENCE-ONLY** |
| 11 | **EDA freeze schema bundles** (E120.1, E125.1, E128, E138.1 XSDs) — distributed from semi.org | XML schemas normatively referenced by the EDA standards, for freeze versions 1105 and 0710. Existence confirmed by SEMI's own SEMICON Japan EDA Workshop deck (<https://www.semi.org/sites/semi.org/files/2025-10/SEMICON_Japan_EDA%20Workshop_December%202024_Fuchigami_Rev%201.1_0.pdf>) and by PDF Solutions/Cimetrix. | XSD | **NOT VERIFIED.** SEMI's general page mentions "auxiliary information documents (No Charge)" and "complementary files required for using standards", but I could **not** locate a stated licence for the schema bundles, and could not retrieve the bundles themselves. **Do not assume they are open.** | unknown | If a licence can later be verified as permissive, the XSD element names would be excellent factor vocabulary. Until then, **do not vendor**. | **REFERENCE-ONLY (licence unverified)** |
| 12 | **EDA performance requirements** — same SEMI workshop deck | Published, citable **latency/throughput budgets** for fab equipment data acquisition: SEMATECH spec **10K VPS (1000 variables @ 10 Hz)**; Asian fab specs requesting **20K VPS** minimum, some **40K VPS**, some **60K VPS**. Freeze 3 moves from HTTP/1.1+SOAP/XML to **HTTP/2 + gRPC + Protocol Buffers**. | Numeric facts in a slide deck | Deck is SEMI-hosted; the **numbers are facts and citable**, the deck is not redistributable. | 3 freeze versions documented (1105 / 0710 / Freeze 3 proposed) | **Directly answers the "latency budget" item.** These become non-functional-requirement provisions in the corpus: a change case can engage `EDA-THROUGHPUT-10K-VPS` with boolean factors `sustains_10k_vps`, `uses_http2_grpc_binding`, `regresses_below_baseline_vps`. | **REFERENCE-ONLY (cite the numbers)** |

### 1.3 OPC UA

| # | Name & URL | What it is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 13 | **OPC Foundation UA-Nodeset** — <https://github.com/OPCFoundation/UA-Nodeset> (branch `latest`) | The normative NodeSet2 XML files released with every OPC UA core and companion specification: **124 `.NodeSet2.xml` files across 79 companion-spec directories**, plus `.Types.xsd`, `.NodeIds.csv`, `.Model.csv`. Includes **ISA-95** (`ISA-95/Opc.ISA95.NodeSet2.xml`) and **ISA95-JOBCONTROL**, MTConnect, PackML, Machinery, MachineTool, Robotics. **No SEMI/semiconductor companion spec exists** (verified by directory listing). Core `Schema/` also ships `StatusCode.csv` — **273 OPC UA status codes** with numeric values and one-line descriptions. | XML, XSD, CSV | **OPC Foundation MIT License 1.00** — verified: embedded verbatim in the XML comment header of `Schema/Opc.Ua.NodeSet2.xml` AND `ISA-95/Opc.ISA95.NodeSet2.xml` ("Permission is hereby granted, free of charge … to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"). Note: there is **no repo-root LICENSE file** — the grant lives in each artefact's header, so **preserve headers when vendoring**. | 146 MB repo; core nodeset alone 4.1 MB; `Schema/` 13 MB | (a) **`StatusCode.csv` is the single best ready-made `expected_disposition` vocabulary in this lane** — 273 machine-readable, tri-severity (`Good`/`Uncertain`/`Bad`) outcome codes with stable numeric IDs: `BadCommunicationError`, `BadEncodingLimitsExceeded`, `BadRequestTooLarge`, `BadOutOfMemory`. Map corpus dispositions onto these instead of inventing a taxonomy. (b) **ISA-95 NodeSet2 is the licence-clean way to get ISA-95 object-model vocabulary** without paying ANSI/ISA (§1.4). (c) NodeSet XML files are ideal *change artefacts*: a case can be "this PR edits `Opc.ISA95.NodeSet2.xml`". | **YES — VENDOR (keep the MIT header)** |
| 14 | **UA-.NETStandard** — <https://github.com/OPCFoundation/UA-.NETStandard> | Reference OPC UA stack: Console Reference **Server**, **Client**, **Publisher**, **Subscriber**; one reference implementation is certified by an OPC Foundation Certification Test Lab, and releases are verified against the official CTT. | C# | **OPC Foundation MIT License 1.00** — verified by fetching `LICENSE.txt`: MIT text, "Copyright (c) 2005-2025 OPC Foundation, Inc." | (not cloned) | A **certified reference server** is a genuine oracle: run a corpus case's client change against it and the certification status backs the expected disposition. | **YES — VENDOR** |
| 15 | **OPC UA Compliance Test Tool (UACTT)** — <https://opcfoundation.org/developer-tools/certification-test-tools/opc-ua-compliance-test-tool-uactt/> | The official conformance test tool: client and server test modes, all test scripts, companion-spec validation scripts, covering OPC UA 1.02–1.05. | Binary + test scripts | **NOT OPEN.** Verified: "exclusively for OPC Foundation Corporate Members", also offered as a paid service to non-members. No open-source component stated. | — | Cite as the industry conformance baseline the corpus is analogous to. Cannot be obtained or vendored. | **REFERENCE-ONLY** |
| 16 | **OPC UA semiconductor companion spec** | **DOES NOT EXIST** in UA-Nodeset. Verified by full directory listing of the `latest` branch (79 directories: ADI, AMB, AML, AdditiveManufacturing, … ISA-95, MTConnect, … Woodworking). Academic work exists on mapping SECS/GEM to OPC UA (IEEE, ResearchGate) but no released "OPC 30xx" semiconductor companion NodeSet. | — | n/a | — | **Report as a gap.** The corpus should not claim a SEMI/OPC companion spec. This absence is itself a useful corpus fact: cross-standard change cases in semiconductor must bridge SECS/GEM ↔ OPC UA by hand. | n/a |

### 1.4 Factory / MES / ISA-95 modelling

| # | Name & URL | What it is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 17 | **B2MML / BatchML** — <https://github.com/MESAInternational/B2MML-BatchML> | MESA International's XML implementation of ANSI/ISA-95 (IEC/ISO 62264): **39 XSD schemas** covering Equipment, Material, Personnel, PhysicalAsset, ProcessSegment, OperationsSchedule/Performance/Definition/Capability/Event/Test, WorkSchedule/Performance/Record/Definition/Capability/Alert/Calendar, MasterDataProfile, plus BatchML General Recipe and Batch Production Record. Includes example XML bundles. | XSD, XML, JSON schema (`AllSchemas.json`) | **PERMISSIVE, verified verbatim** from `LICENSE`: "Permission to use, copy, modify, or redistribute this Work and its documentation, with or without modification, for any purpose and without fee or royalty is hereby granted provided MESA International is acknowledged as the originator of this Work using the following statement: *'The Business To Manufacturing Markup Language (B2MML) is used courtesy of MESA International.'*" (Copyright 2020 MESA International, Version 0700) | 19 MB repo; `Schema/` 2.2 MB, 39 XSDs; 3 example ZIP bundles | **The licence-clean route to ISA-95 vocabulary.** (a) XSD element/attribute names → **factor vocabulary** for MES-layer facts (`WorkRequest`, `JobOrder`, `MaterialLotID`, `EquipmentActualProperty`). (b) The XSDs are realistic **change artefacts** — a schema-evolution case ("add optional element", "tighten a facet", "make an element mandatory") maps cleanly to `(provisions engaged: ISA-95 Part 2; factors: is_breaking_change, adds_required_element; disposition: rejected)`. (c) XSD validation is a free **oracle**. Attribution string is one line — trivially satisfiable. | **YES — VENDOR (must reproduce the exact courtesy statement)** |
| 18 | **ANSI/ISA-95.00.01-2025 (IEC 62264-1 Mod)** — <https://webstore.ansi.org/standards/isa/ansiisa9500012025iec62264mod> | The ISA-95 standard text. | PDF | **PAYWALLED.** Verified: **$541.00** for the PDF on the ANSI Webstore; ANSI sells multi-user access as a separate subscription, so single-purchase use is restricted. | — | Cite by designation only; get the model from B2MML (#17) and the OPC UA ISA-95 NodeSet (#13). | **REFERENCE-ONLY** |
| 19 | **Open-source MES projects** (Spruik/Libre, Mes-Open/OpenMes, crbnos/carbon, jukbot/smart-industry, takacsjd/OSE_MES) | General-purpose MES/ERP platforms. | various | **NOT INDIVIDUALLY VERIFIED** — not investigated in depth because **none is semiconductor-specific** and none implements SECS/GEM, GEM300 or EDA. | — | Low value for this lane. If a generic MES is wanted as a change-target codebase, verify each licence at the point of use. | **REFERENCE-ONLY (unverified)** |

### 1.5 Supply-chain event standards

| # | Name & URL | What it is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 20 | **GS1 EPCIS 2.0** — <https://github.com/gs1/EPCIS> and <https://ref.gs1.org/standards/epcis/> | Full EPCIS 2.0 artefact set: XSD schemas, **JSON Schema** (`EPCIS-JSON-Schema.json`), **JSON-LD contexts** (`epcis-context.jsonld`, simple context), **OWL/Turtle ontology**, SHACL shapes, REST bindings/OpenAPI, WSDL, XSL, conformance requirements, XML and JSON examples. | XSD, JSON Schema, JSON-LD, Turtle, OpenAPI | **NO OPEN LICENCE GRANT.** Verified by reading the repo's `LICENSE` file — it is **a disclaimer, not a licence**: it recites the GS1 IP Policy (participants grant GS1 *members* royalty-free or RAND licences to Necessary Claims) and an "AS IS" warranty disclaimer. There is **no** grant of copying/redistribution rights to the public and **no** OSI/CC licence. | 14 MB; 135 JSON/JSON-LD files | Freely *downloadable* and freely *citable*, but the absence of a redistribution grant means **do not vendor the artefacts**. Reuse the **vocabulary as facts**: EPCIS event types (`ObjectEvent`, `AggregationEvent`, `TransactionEvent`, `TransformationEvent`, `AssociationEvent`) and the `bizStep`/`disposition` CBV vocabularies are a natural model for supply-chain control-tower cases — note EPCIS already has a field literally called **`disposition`**, which is a useful precedent for the corpus's own `expected_disposition`. | **REFERENCE-ONLY** |
| 21 | **RosettaNet PIPs** — <https://www.gs1us.org/resources/rosettanet> | Partner Interface Processes, the high-tech/semiconductor supply-chain B2B standard. **8 clusters (0–7)**: 0 RosettaNet Support, 1 Partner Product & Service Review, 2 Product Information, 3 Order Management, 4 Inventory Management, 5 Marketing Information, 6 Service and Support, 7 **Manufacturing** (segments 7A Design Transfer, 7B Manage Manufacturing WO & WIP, 7C Distribute Manufacturing Information). Verified PIP codes: 3A1 Request Quote, 3A2 Request Price and Availability, 3A3 Request Shopping Cart Transfer, 3A4 Manage Purchase Order, 3A5 Query Order Status, 3A6 Distribute Order Status. | XML/DTD specs | **NOT VERIFIED.** Now stewarded by GS1 US. I could not retrieve a licence statement. | 7 clusters, 3 manufacturing segments; individual Cluster 7 PIP codes not retrieved | **PIP codes are citable identifiers** and are the right vocabulary for outsourced-assembly/foundry supply-chain cases (Cluster 7B WIP is directly on-point for a control tower). Do not vendor spec text. | **REFERENCE-ONLY (licence unverified)** |
| 22 | **ASC X12** — <https://x12.org/licensing> | US EDI transaction sets (~300 sponsored). | spec | **LICENSED / PAYWALLED — verified explicitly.** X12 operates tiered licences: **Commercial Use Partner** (variable annual fee), **Internal Use Partner $3,600/yr**, **Licensed User $180/yr**, **Development Licensing $1,200/yr**. Stated: "Any use of any X12 work product must be compliant with US Copyright laws and X12 Intellectual Property policies." Membership does **not** include a product licence. | — | Transaction-set *numbers* (850, 856, 830, 862) are citable identifiers if needed. Do not vendor anything. | **REFERENCE-ONLY** |
| 23 | **UN/EDIFACT directories** — <https://service.unece.org/trade/untdid/> (e.g. `d15a/trmd/trmdi1.htm`) | UNECE-published message-type directories (D.xxA/B releases) — publicly served, no paywall observed. | HTML/plain text | **NOT VERIFIED.** UNECE serves these openly and `unece.org` returned 403 to automated fetch, so I could not read a terms-of-use page. UN materials are commonly permissive, but **I am not asserting a licence I did not read.** | Many directory releases (D.00A … D.23B) | Message-type mnemonics (`ORDERS`, `DELFOR`, `DESADV`, `INVRPT`) are citable identifiers for logistics factor facts. Verify terms before vendoring. | **REFERENCE-ONLY (licence unverified)** |

### 1.6 Open fab datasets with ground truth

| # | Name & URL | What the data actually is | Format | VERIFIED licence | Volume | Reuse path | Vendor? |
|---|---|---|---|---|---|---|---|
| 24 | **SECOM** (UCI ML Repository #179) — <https://archive.ics.uci.edu/dataset/179/secom> | Real semiconductor manufacturing process **in-line sensor/monitoring signals** with **pass/fail yield ground truth** from in-house line testing. 1,567 examples × 591 features, timestamped; **104 failures** (6.6 %). Donated by Michael McCann & Adrian Johnston, 2008-11-18. Substantial missing values (`NaN`). | Space-separated text: `secom.data` (5.1 MB), `secom_labels.data` (39.7 KB, label + datetime), `secom.names` (4.1 KB) | **CC BY 4.0** — verified verbatim on the UCI page: "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given." | 1.9 MB zip → 5.1 MB data; 1,567 × 591 | **The only genuinely open, ground-truth-labelled real fab dataset in this lane.** (a) **Oracle** — a yield-monitoring code change (feature-selection, imputation, alarm threshold) can be evaluated against the 104 known failures, giving a *verifiable* `expected_disposition`. (b) **Factor facts** — `handles_missing_values`, `changes_alarm_threshold`, `false_negative_rate_increases`. (c) Its `-1 = pass / 1 = fail` convention is a real, citable disposition encoding. | **YES — VENDOR (CC BY 4.0, credit UCI + McCann & Johnston)** |
| 25 | **SMT2020 fab model, bundled in PySCFabSim** — <https://github.com/prosysscience/PySCFabSim-release> | A **complete, realistic 300 mm fab model** in two variants, **HVLM** (high-volume/low-mix) and **LVHM** (low-volume/high-mix). Bundled files per variant: `tool.txt` (**214 tool families** with capacities, dispatch rules, setup groups), `route_*.txt` (**10 routes, 4,023 process steps** in LVHM, with per-step process-time distributions, batch min/max, **CQT critical-queue-time constraints**), `WIP.txt` (initial lots with priority, due date, hot-lot flag), `downcal.txt` (MTTF/MTTR distributions per tool group), `pmcal.txt`, `setup.txt`/`setupgrp.txt`, `attach.txt`, `fromto.txt`, `order.txt`, `part.txt`. Real process areas: Def_Met, Delay, Dielectric, Diffusion, Dry_Etch, Implant, Litho, Litho_Met, Planar, TF, TF_Met, Wet_Etch. Real dispatch rules: `rule_HotLotFIRST`, `rule_LSSU`, `rank_FIFO`, `rank_CR`, `rank_HP`, `rank_RSETUP`, `wake_LeastSetupTime`. | Tab-separated `.txt` + Python simulator | **MIT** — verified: repo-root `LICENSE` = "MIT License / Copyright (c) 2026 Research Group Production Systems". The `datasets/` directory is inside the MIT-licensed repo. | 1.1 MB of datasets (HVLM 368 KB + LVHM 668 KB); LVHM routes = 4,023 step rows; 214 tool rows | **The best fab-domain factor vocabulary and the best executable oracle.** (a) **Factor vocabulary** — process-area names, dispatch-rule names, `CQT`, `HOTLOT`, `BATCHMN/BATCHMX`, `MTTF/MTTR` are genuine fab-monitoring concepts. (b) **Executable oracle** — a change to dispatching/scheduling logic can be *run*, so cycle-time/throughput regression is measurable ground truth, not an opinion. (c) Realistic control-tower cases: "change violates a CQT constraint on route r_1 step 3" → factors `violates_cqt`, `affects_hot_lot`; disposition `rejected`. | **YES — VENDOR (MIT)** |
| 26 | **WM-811K / LSWMD** — <http://mirlab.org/dataSet/public/>, mirrored at <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map> | The largest public **wafer map defect** dataset: **811,457 wafer maps** from real fabrication (TSMC-origin per Wu et al.), from **46,293 lots**; ~**172,950 labelled (21 %)**; 9 classes: **Center, Donut, Edge-Location, Edge-Ring, Random, Location, Near-Full, Scratch, None** (None = 85.2 % of labels — severe imbalance). Arrays encode 0 = no die, 1 = pass die, 2 = fail die. Citation: Wu, Jang & Chen, *IEEE Trans. Semiconductor Manufacturing* 28(1):1–12, 2015. | `.pkl` (numpy arrays); Kaggle image variants | **NOT VERIFIED — no licence stated anywhere.** Checked the MIR Lab public dataset page (says only "prepared by MIR lab for public download" — no permissions, restrictions or legal conditions), the Kaggle mirror, and secondary descriptions. **No licence found. Do not assume open.** | 811,457 maps; ~172,950 labelled | The **9 class names are facts and citable** — use them as defect-classification factor vocabulary (`defect_class == "Edge-Ring"`) without shipping any pixels. To use it as an oracle, have the corpus *fetch* it at evaluation time under the user's own acceptance of MIR Lab / Kaggle terms; never redistribute. | **REFERENCE-ONLY (licence unverified — vocabulary only)** |
| 27 | **MixedWM38** — <https://ieee-dataport.org/documents/mixed-type-wafer-defect-datasets>; code at <https://github.com/Junliangwangdhu/WaferMap> | ~38,000 wafer maps at 52×52 across **38 pattern classes**: 1 normal + 8 single-defect + **29 mixed-type** combinations, multi-label encoded over the 8 basic defect types. Partly GAN-augmented to balance classes. Author: Junliang Wang. | `.npz` (`data_mutil_label.npz`) | **NOT OPEN — verified two ways.** (a) IEEE DataPort page states: "This dataset requires an IEEE DataPort Subscription to access." (b) The GitHub repo has **no LICENSE file** (verified: `LICENSE`, `LICENSE.md`, `LICENSE.txt` all return 404) and does **not contain the data** — only 5 figures and 3 Python files (`deform_conv.py`, `layers_train.py`, `trian_mutil_label.py`). | ~38,000 maps, 38 classes | **The 38-class mixed-defect taxonomy is a citable fact** and is the better factor vocabulary for realistic monitoring (real wafers show *co-occurring* defects, so multi-label factors, not one-hot). GAN augmentation means it is a weaker oracle than WM-811K anyway. | **REFERENCE-ONLY** |
| 28 | **NASA/PHM 2016 CMP dataset** — <https://data.phmsociety.org/nasa/> (entry #21 "Wafer Chemical-Mechanical Planarization"); challenge page <https://phmsociety.org/.../phm-data-challenge-4/> | 2016 PHM Data Challenge: predicting **material removal rate** in wafer **CMP** as polishing pad and dresser degrade. Files `CMP-training-ddd.csv` (25 measurement variables x1–x25), `CMP-training-removalrate.csv` (ground truth), `CMP-test-ddd.csv`. | CSV in a zip | **NOT VERIFIED — no formal licence.** Verified terms on the mirror: "Users employ the data at their own risk. Neither NASA nor the donators of the data sets assume any liability…" plus a *request* (not a condition) to acknowledge the repository and donors. **No CC/MIT/public-domain grant is stated.** The challenge page states no data licence at all. | 25 variables + removal-rate labels (exact row count not retrieved) | **The only public metrology/SPC dataset with a numeric ground-truth target in this lane.** Ideal for virtual-metrology oracle cases (a change to a removal-rate predictor is scored against held-out truth). Because the terms are a disclaimer rather than a grant, **fetch at evaluation time; do not vendor**. | **REFERENCE-ONLY** |
| 29 | **MIMAC datasets** — <https://p2schedgen.fernuni-hagen.de/index.php/downloads/simulation> | The classic JESSI/SEMATECH MIMAC fab simulation testbed datasets, alongside SMT2020, hosted by FernUni Hagen. | (not retrieved) | **NOT VERIFIED** — the download page states no format, size, licence or citation requirement. | unknown | Historical SEMATECH-lineage fab models. Prefer SMT2020-in-PySCFabSim (#25), which is MIT and already bundled. | **REFERENCE-ONLY (licence unverified)** |

---

## 2. Negative findings (important, and worth stating in the corpus README)

1. **There are no public SECS/HSMS packet captures.** Verified by cloning the largest open ICS
   capture collection, ITI/ICS-Security-Tools (`github.com/ITI/ICS-Security-Tools`): **726 pcaps
   across 21 protocol families** — BACnet, C37.118, CIP, DLMS-COSEM, EtherNet/IP, IEC 60870-5-104,
   IEC 61850, MELSEC, Modbus/TCP, OPC, Zigbee, DNP3, HART, PROFINET, S7, omron, modicon, fox,
   beckoff, openics, quickdraw — and **zero** matches for secs/hsms/semi/wafer/fab. The Wireshark
   wiki SampleCaptures page likewise lists none.
   **Implication:** byte-level HSMS fixtures for the corpus must be (a) taken from the
   Apache-2.0 `go-secs` SML testdata and `secsgem` test byte-strings, or (b) **generated** by
   running two Apache-2.0 implementations against each other (e.g. `secs-simulator` #5 vs
   `go-secs` #1) and captured locally. Option (b) yields fixtures the corpus fully owns.
2. **No OPC UA semiconductor companion specification exists** (verified against the full
   UA-Nodeset `latest` branch directory listing).
3. **`secsgem` does not implement S7F23/S7F24** (formatted process program send/ack). Verified by
   listing `secsgem/secs/functions/` — S7 coverage is S7F1–F6 and S7F17–F20 only. `go-secs`
   **does** carry an `S7F23` fixture (`FPS`). If the corpus needs recipe-upload cases, go-secs is
   the source.
4. **The MCA is the closest existing artefact to this corpus** (a free rule-checker producing
   pass/fail metadata findings) but it is closed-source and "AS IS" — good prior art, not a
   dependency.

---

## 3. Recommended factor vocabulary (all identifiers verified against a licensed-open artefact)

Every identifier below was read out of a file I inspected, not recalled. Provenance is given so a
reviewer can re-verify.

### 3.1 SECS-II stream/function codes with official message names
*(source: `secsgem/secs/functions/*.py` class docstrings, LGPL-2.1 — names re-derived as facts;
cross-checked against `go-secs/sml/testdata/common.sml`, Apache-2.0)*

`S1F1` Are You There Request (R) · `S1F13` Establish Communications Request (CR) ·
`S1F15` Request OFF-LINE (ROFL) · `S1F17` Request ON-LINE (RONL) ·
`S2F33` Define Report (DR) · `S2F35` Link Event Report (LER) ·
`S2F37` Enable/Disable Event Report (EDER) · `S2F41` Host Command Send (HCS) ·
`S2F43` Reset Spooling Streams and Functions (RSSF) · `S5F1` Alarm Report Send (ARS) ·
`S6F11` Event Report Send (ERS) · `S6F23` Request Spooled Data (RSD) ·
`S7F1` Process Program Load Inquire (PPI) · `S7F3` Process Program Send (PPS) ·
`S7F17` Delete Process Program Send (DPS) · `S7F23` Formatted Process Program Send (FPS) ·
`S9F1` Unrecognized Device ID (UDN) · `S9F3` Unrecognized Stream Type (USN) ·
`S9F9` Transaction Timer Timeout (TIN) · `S10F3` Terminal Display, Single (VTN) ·
`S14F1` GetAttr Request (GAR) · `S16F15` Create Process Job

Direction and reply-required flags are available for all 124, e.g. `S6F11`: `to_host=True`,
`to_equipment=False`, `has_reply=True`, `is_multi_block=True` — these map one-to-one onto boolean
factor facts.

### 3.2 HSMS SType (session) codes
*(source: `wireshark/epan/dissectors/packet-hsms.c` `stype_names[]`, GPL-2.0 — value table is
fact; identically present in `secsgem/hsms/header.py`, LGPL)*

`Data.msg`(0) · `Select.req`(1) · `Select.rsp`(2) · `Deselect.req`(3) · `Deselect.rsp`(4) ·
`Linktest.req`(5) · `Linktest.rsp`(6) · `Reject.req`(7) · `Separate.req`(9)

### 3.3 HSMS connection states and timers
*(states: `secsgem/hsms/connection_state_machine.py`; timers: `go-secs/hsms/connection_config.go`,
Apache-2.0)*

States: `NOT_CONNECTED` · `CONNECTED` · `CONNECTED_NOT_SELECTED` · `CONNECTED_SELECTED`
Timers (verified defaults): `T3=45s` (reply) · `T5=10s` (connect separation) · `T6=5s` (control
message reply) · `T7=10s` (not-selected) · `T8=5s` (network inter-character)

### 3.4 GEM control and communication state names
*(source: `secsgem/gem/control_state_machine.py`, `communication_state_machine.py`)*

Control: `INIT` · `CONTROL` · `OFFLINE` · `EQUIPMENT_OFFLINE` · `ATTEMPT_ONLINE` ·
`HOST_OFFLINE` · `ONLINE` · `ONLINE_LOCAL` · `ONLINE_REMOTE`
(initial default `ATTEMPT_ONLINE`; online sub-states `LOCAL` / `REMOTE`)
Communication: `DISABLED` · `ENABLED` · `NOT_COMMUNICATING` · `HOST_INITIATED_CONNECT` ·
`WAIT_CR_FROM_HOST` · `EQUIPMENT_INITIATED_CONNECT` · `WAIT_DELAY` · `WAIT_CRA` · `COMMUNICATING`

### 3.5 GEM default collection event IDs and names
*(source: `secsgem/gem/collection_event.py` + `collection_event_capability.py`)*

`CEID 1` = `EquipmentOffline` · `CEID 2` = `ControlStateLocal` · `CEID 3` = `ControlStateRemote` ·
`CEID 20` = `CmdStartDone` · `CEID 21` = `CmdStopDone`

### 3.6 Data-item acknowledgement codes → expected dispositions
*(source: `secsgem/secs/data_items/ackc7.py` etc.)*

`ACKC7`: `ACCEPTED`(0) · `NO_PERMISSION`(1) · `LENGTH_ERROR`(2) · `MATRIX_OVERFLOW`(3) ·
`PPID_NOT_FOUND`(4) · `MODE_UNSUPPORTED`(5) · `PERFORMED_LATER`(6)
128 such data items exist, including `ACKC5`, `ACKC6`, `ACKC10`, `COMMACK`, `DRACK`, `LRACK`,
`ERACK`, `HCACK`, `OFLACK`, `ONLACK`, `PPGNT`, `GRANT6`, `LIMITACK`, `OBJACK`, `TIAACK`.

### 3.7 GEM300 action / job vocabulary
*(source: `go-secs/sml/testdata/common.sml`, Apache-2.0 — 189 named fixtures)*

E87 carrier actions (S3F17): `CancelCarrier` · `CancelCarrierAtPort` · `ProceedWithCarrier` ·
(S3F23) `ChangeAccessMode`
E40 process job (S16Fx): `CreateProcessJob`(S16F15) · `PJCancel`(S16F5) · `PJAbort`(S16F5) ·
`CheckPJDuplicated`(S16F19) · `CheckPJSpace`(S16F21)
E94 control job: `CreateControlJob`(S14F9) · `GetAllCJ`(S1F3) · `CheckCJSpace`(S1F3)
Load port: `QueryLoadPortAccessMode` · `QueryPortStatus` · `QueryOnlineSubStatus`

### 3.8 SEMI E10 equipment states (six-state model)
*(source: INFICON engineering article citing SEMI E10; state names are facts)*
`Productive` · `Standby` · `Engineering` · `Scheduled Downtime` · `Unscheduled Downtime` ·
`Non-Scheduled`. Utilisation = Productive / (Productive + Standby).

### 3.9 OPC UA StatusCodes (disposition vocabulary)
*(source: `UA-Nodeset/Schema/StatusCode.csv`, OPC Foundation MIT 1.00 — 273 codes)*
`Good`(0x00000000) · `Uncertain`(0x40000000) · `Bad`(0x80000000) · `BadUnexpectedError` ·
`BadInternalError` · `BadOutOfMemory` · `BadResourceUnavailable` · `BadCommunicationError` ·
`BadEncodingError` · `BadDecodingError` · `BadEncodingLimitsExceeded` · `BadRequestTooLarge` …

### 3.10 Fab process areas, dispatch rules and constraints
*(source: `PySCFabSim-release/datasets/SMT2020_{HVLM,LVHM}/`, MIT)*
Areas: `Def_Met` `Delay` `Dielectric` `Diffusion` `Dry_Etch` `Implant` `Litho` `Litho_Met`
`Planar` `TF` `TF_Met` `Wet_Etch`
Dispatch: `rule_HotLotFIRST` `rule_LSSU` `rank_FIFO` `rank_CR` `rank_HP` `rank_RSETUP`
`wake_LeastSetupTime`
Constraint columns: `CQT` (critical queue time) `STEP_CQT` `BATCHMN`/`BATCHMX` `HOTLOT`
`MTTF`/`MTTR` `SETUPGRP` `MINRUN`

### 3.11 Defect classes
WM-811K (9): `Center` `Donut` `Edge-Location` `Edge-Ring` `Random` `Location` `Near-Full`
`Scratch` `None`
MixedWM38 (38 = 1 normal + 8 single + 29 mixed combinations of the 8 basic types)

---

## 4. Vendor / reference-only summary

**SAFE TO VENDOR** into an Apache-2.0 / CC-BY-4.0 repository (licence read and verified):

| Source | Licence | Obligation on vendoring |
|---|---|---|
| go-secs (#1) | Apache-2.0 | NOTICE + LICENSE |
| pysemisecs (#3) | Apache-2.0 | NOTICE + LICENSE |
| semi-rs (#4) | MIT | copyright + permission notice |
| secs-simulator (#5) | Apache-2.0 | NOTICE + LICENSE |
| hsms JS (#6) | Apache-2.0 | NOTICE + LICENSE |
| UA-Nodeset (#13) | OPC Foundation MIT 1.00 | **keep the XML comment header** — the grant lives there, not in a root LICENSE |
| UA-.NETStandard (#14) | OPC Foundation MIT 1.00 | copyright + permission notice |
| B2MML/BatchML (#17) | MESA permissive | reproduce the exact courtesy statement |
| SECOM (#24) | CC BY 4.0 | credit UCI + McCann & Johnston |
| SMT2020 in PySCFabSim (#25) | MIT | copyright + permission notice |

**REFERENCE-ONLY** — cite, link, or fetch at evaluation time, never redistribute:
SEMI standards text (all, §0) · secsgem source (LGPL-2.1; usable as an unmodified dependency, and
its vocabulary re-derivable as facts) · Wireshark dissector source (GPL-2.0; `tshark` usable as an
external oracle) · MCA (#10) · EDA schema bundles (#11, licence unverified) · UACTT (#15) ·
ANSI/ISA-95 (#18) · GS1 EPCIS artefacts (#20, disclaimer not a licence) · RosettaNet (#21,
unverified) · ASC X12 (#22, licensed) · UN/EDIFACT (#23, unverified) · WM-811K (#26, **no licence
stated anywhere**) · MixedWM38 (#27, subscription + no LICENSE file) · NASA/PHM CMP (#28,
disclaimer + attribution request, no grant) · MIMAC (#29, unverified) · go-factory-io (#7,
all rights reserved).

---

## 5. Suggested corpus construction path

1. **Vocabulary layer.** Build `factors.yaml` from §3 — every term traceable to a vendored,
   verified-licence artefact. Provisions referenced by designation only (`SEMI-E30`, `SEMI-E37.1`,
   `ISA-95-P2`, `OPC-UA-P4`).
2. **Fixture layer.** Vendor `go-secs/sml/testdata/common.sml` (189 fixtures / 140 S-F codes) as
   the canonical message set. Generate any additional HSMS wire captures locally by running
   `secs-simulator` against `go-secs` — the corpus then owns them outright, which is necessary
   because no public HSMS pcaps exist (§2.1).
3. **Oracle layer.** Four independent, differently-licensed oracles are available and should be
   used together: (a) differential decode across go-secs / pysemisecs / semi-rs / secsgem;
   (b) `tshark` with the HSMS dissector; (c) XSD/JSON-Schema validation against B2MML and
   EPCIS schemas; (d) executable outcomes — PySCFabSim (cycle time, CQT violations) and SECOM
   (the 104 known yield failures).
4. **Disposition layer.** Reuse existing, citable outcome taxonomies rather than inventing one:
   OPC UA `StatusCode.csv` (273 codes, MIT) for protocol-level dispositions, SECS `ACKC*`/`*ACK`
   data-item enumerations for message-level dispositions, and SECOM's `-1 pass / 1 fail` for
   yield-level dispositions.
5. **Non-functional provisions.** Encode the verified EDA throughput budgets (10K / 20K / 40K /
   60K VPS) and the HSMS timers (T3 45s, T5 10s, T6 5s, T7 10s, T8 5s) as real, citable
   performance provisions.
6. **Licence hygiene.** Ship `THIRD_PARTY_NOTICES.md` with the ten vendored licences; state
   prominently that no SEMI, ISA, X12 or GS1 specification text is reproduced and that all
   standard designations and message identifiers appear as citations of fact.
