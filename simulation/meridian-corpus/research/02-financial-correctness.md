# 02 — Financial Correctness: reusable open-source test corpora

Lane: mathematical precision, transaction correctness, concurrency/resilience for a regulated
fintech (payments, ledger, lending). Target shape of the compliance corpus:
`(case id, provisions engaged, boolean factor facts, expected disposition)`.

**Method note.** Every licence below was read at source — either the `LICENSE`/`COPYRIGHT` file in a
cloned repository, the file header of the artefact itself, or the publisher's own terms page. Where
the licence could not be established from an authoritative source it is written as
**UNVERIFIED / NO EXPLICIT GRANT** and never guessed. Volumes marked "counted" were derived by
cloning the repository and counting; volumes marked "stated" come from the publisher.

Working copies used for counting live under `meridian-corpus/research/`:
`cpy/` (CPython sparse), `pg/` (PostgreSQL sparse), `herm/`, `elle/`, `hsim/`, `jtb/`, `tck/`,
`rd/`, `jm/`, plus `cldr.xml`, `tb.zig`, `sm.zig`, `kafka_tx.py`.

---

## A. Decimal and floating-point correctness

### A1. IBM / Cowlishaw `decTest` — General Decimal Arithmetic testcases  REFERENCE-ONLY (licence)

* **URL (canonical):** https://speleotrove.com/decimal/dtintro.html ,
  https://speleotrove.com/decimal/dectest.html (`dectest.zip`, `dectest0.zip`)
* **URL (most convenient live copy):** CPython `Lib/test/decimaltestdata/`
  https://github.com/python/cpython/tree/main/Lib/test/decimaltestdata
* **Contents:** the reference conformance corpus for IEEE 754-2008 *decimal* arithmetic
  (decimal32/64/128 and arbitrary-precision), used by CPython's `decimal`, libmpdec, GCC
  `libdecnumber`, ICU, Shopify's mruby-mpdecimal, `alkis/decimal` and others.
* **Format:** line-oriented, language- and representation-independent. Directives set context
  (`precision:`, `rounding:`, `maxExponent:`, `minExponent:`, `extended:`), then one case per line:

  ```
  addx001 add 1 1 -> 2
  addx613 add 1E+3 -1    -> 999          Inexact Rounded      -- (with precision: 3)
  ```

  i.e. `id  operation  operand… -> expected-result  [condition flags]`. Flags are the IEEE
  exceptional conditions: `Inexact`, `Rounded`, `Overflow`, `Underflow`, `Subnormal`,
  `Division_by_zero`, `Invalid_operation`, `Clamped`, `Division_impossible`,
  `Division_undefined`, `Insufficient_storage`, `Conversion_syntax`.
* **Volume (counted, CPython `main`, 2026-09-05):**
  * **143** `.decTest` files, **4,421,743 bytes**
  * **67,060** test cases (non-comment lines containing ` -> `)
  * **62 distinct operations.** Top: `add` 5,677 · `fma` 5,417 · `power` 5,337 · `squareroot`
    3,586 · `tosci` 3,298 · `divide` 3,047 · `compare` 2,757 · `subtract` 2,605 · `multiply`
    2,506 · `remainder` 2,324 · `quantize` 2,164 · `divideint` 1,936 · `comparetotal` 1,905 ·
    `comparetotmag` 1,891 · `remaindernear` 1,504
  * **Rounding-mode coverage** (cases attributed to the `rounding:` directive in force):
    `half_even` **39,940** · `half_up` **23,512** · `down` **1,459** · `up` **531** ·
    `ceiling` **444** · `floor` **436** · `half_down` **374** · `05up` **364**.
    All eight modes of the General Decimal Arithmetic spec are exercised.
* **Ground truth:** yes — every line carries the expected result *and* the expected condition flags.
* **Licence — VERIFIED, and it is the problem.** Every file header reads verbatim:

  > `-- Copyright (c) IBM Corporation, 1981, 2008.  All rights reserved.`
  > `-- These testcases are experimental ('beta' versions), and they may contain errors. They are`
  > `-- offered on an as-is basis. In particular, achieving the same results as the tests here is`
  > `-- not a guarantee that an implementation complies with any Standard or specification.`

  The speleotrove download page adds only: *"Reproduced with permission from IBM © Copyright 1997,
  2009 by International Business Machines Corporation."*
  **There is no OSI licence and no explicit redistribution grant in the files.** I checked
  CPython's `Doc/license.rst` ("Licenses and Acknowledgements for Incorporated Software"):
  it carries entries for libmpdec (BSD-2-Clause, Stefan Krah) and for the W3C C14N test suite
  (BSD-3-Clause) but **no entry for `decimaltestdata`** — so CPython does not assert a separate
  grant for it either. GCC's copy of the *code* (`libdecnumber/decNumber.c`) is relicensed:
  header verified as **GPLv3-or-later with the GCC Runtime Library Exception 3.1**, "Contributed by
  IBM Corporation. Author Mike Cowlishaw" — but that covers decNumber the library, not the testcases.
* **Verdict: REFERENCE-ONLY.** Cite it, derive from it, regenerate equivalent cases from the spec —
  do not vendor the files into a corpus you redistribute under your own licence without counsel
  clearing the IBM permission. (De facto it is vendored by CPython, GCC, ICU and several crates;
  that is evidence of tolerance, not a grant.)
* **Reuse path:** the decTest line format is already `(case id, operation + context = provisions
  engaged, operands = factor facts, expected result + flags = expected disposition)`. A one-to-one
  mapping exists:
  `case id` ← `addx613`; `provisions engaged` ← the operation plus the in-force context directives
  (`precision`, `rounding`, `maxExponent`); `boolean factor facts` ← the condition flags treated as
  predicates (`inexact=true`, `rounded=true`, `overflow=false`, …); `expected disposition` ← the
  result string. If the licence blocks vendoring, keep the *schema* and regenerate values with a
  cleanroom generator validated against decNumber.

### A2. `rust_decimal` generated arithmetic corpus  SAFE TO VENDOR — the single best decimal find

* **URL:** https://github.com/paupino/rust-decimal — directory `tests/generated/`
* **Contents:** exhaustively generated expected-result tables for 96-bit fixed-scale decimal
  arithmetic (the .NET/COM `DECIMAL` shape used by most ledger and money types).
* **Format:** CSV, header `D1,D2,Result,Error`. Empty `Error` = success; otherwise the failure mode.
* **Volume (counted, `master`, 2026-09-05):**
  * **316 CSV files**, **251 MB**, **3,430,315 rows**
  * 63 files each for **Add, Sub, Mul, Div, Rem** (file naming `Op_<scale-bucket>_<sign-bucket>.csv`)
  * **270,924 rows carry an expected error**: `divide_by_zero` **140,000**, `overflow` **130,924**
  * plus `tests/decimal_tests/` with 463 hand-written cases, incl. `rounding.rs` covering
    **7 rounding strategies**: `MidpointNearestEven` (bankers'), `MidpointAwayFromZero`,
    `MidpointTowardZero`, `AwayFromZero`, `ToZero`, `ToPositiveInfinity`, `ToNegativeInfinity`
* **Ground truth:** yes — result and error class per row.
* **Licence — VERIFIED:** `LICENSE` reads `MIT License / Copyright (c) 2016 Paul Mason`.
* **Verdict: SAFE TO VENDOR** (MIT; retain the notice).
* **Reuse path:** near-zero-effort mapping. `case id` ← `<file>#<row>`;
  `provisions engaged` ← the operation and the arithmetic-precision provision;
  `factor facts` ← `operand_exceeds_representable_range`, `divisor_is_zero`,
  `result_requires_rounding`, `operands_differ_in_scale`;
  `expected disposition` ← `Result` value, or `REJECT(divide_by_zero)` / `REJECT(overflow)`.
  The `Error` column is exactly a disposition label. **This is the corpus to start with.**

### A3. Berkeley TestFloat (John Hauser / UC Berkeley)  SAFE TO VENDOR

* **URL:** http://www.jhauser.us/arithmetic/TestFloat.html ,
  docs http://www.jhauser.us/arithmetic/TestFloat-3/doc/TestFloat-general.html
* **Contents:** the reference conformance harness for **binary** IEEE 754 — the counterpart to
  decTest. Tests conversions among 16/32/64/80/128-bit formats and integers; add, sub, mul, div,
  sqrt; **fused multiply-add**; remainder; round-to-integer; and the comparison predicates.
* **Ground truth:** yes, and unusually strict — verified quote: *"TestFloat verifies not only that
  the numeric results of an operation are correct, but also that the proper floating-point exception
  flags are raised. All five exception flags are tested, including the inexact flag."* It tests
  *"all five rounding modes defined by the IEEE Floating-Point Standard, plus possibly a sixth mode,
  round to odd."*
* **Format:** cases are *generated* by `testfloat_gen` (deterministic, seeded) rather than shipped as
  a static table; `testfloat_ver` verifies. Volume is therefore parameterised, not fixed.
* **Licence — VERIFIED, quoted from the project documentation:**
  > "Copyright 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018 The Regents of the University of
  > California. All rights reserved. Redistribution and use in source and binary forms, with or
  > without modification, are permitted provided that the following conditions are met: 1. …
  > 2. … 3. Neither the name of the University nor the names of its contributors may be used to
  > endorse or promote products derived from this software without specific prior written
  > permission."
  → **BSD-3-Clause.**
* **Verdict: SAFE TO VENDOR.**
* **Reuse path:** use it as the *generator* behind a "binary floating-point must not be used for
  money" control. The strongest compliance case is negative: run TestFloat-generated binary64 cases
  through a money type and assert the disposition `REJECT(non_exact_decimal_representation)`.
  Factor: `monetary_amount_held_in_binary_floating_point`.

### A4. JSR-354 Money & Currency TCK (JavaMoney)  SAFE TO VENDOR — best "provision → case" structure

* **URL:** https://github.com/JavaMoney/jsr354-tck (API: `jsr354-api`, RI "Moneta": `jsr354-ri`)
* **Contents:** the Technology Compatibility Kit for JSR-354. Test classes:
  `ModellingMonetaryAmountsTest`, `ModellingCurrenciesTest`, `CreatingMonetaryAmountsTest`,
  `AccessingCurrenciesAmountsRoundingsTest`, `ExternalizingNumericValueTest`,
  `FunctionalExtensionPointsTest`, plus `conversion/`, `format/`, `spi/`.
* **Volume (counted, `master`, 2026-09-05):** 41 Java files, **246 `@Test` methods**, and —
  the important number — **245 `@SpecAssertion` annotations across 17 spec sections**
  (`0`, `4.2.1–4.2.4`, `4.2.6`, `4.2.7`, `4.3.1–4.3.4`, `4.4.1–4.4.3`, `4.5.1–4.5.3`).
  Each is `@SpecAssertion(section = "4.2.1", id = "421-A1")`.
* **Ground truth:** yes — each test asserts required behaviour, and the annotation names the
  normative clause it enforces.
* **Licence — VERIFIED:** `LICENSE.txt`: *"Copyright 2012, 2015, Werner Keil, Credit Suisse
  (Anatole Tresch). Licensed under the Apache License, Version 2.0"*; the same header appears
  in each test source file. → **Apache-2.0.**
* **Verdict: SAFE TO VENDOR.**
* **Reuse path:** this is *already* the target schema. `case id` ← the `@SpecAssertion` `id`
  (`421-A1`); **`provisions engaged` ← the `section` value — a literal, machine-readable
  provision reference**; `expected disposition` ← pass/fail of the assertion. Adopt the
  `@SpecAssertion(section, id)` convention wholesale for the fintech corpus: it is the cleanest
  existing precedent for binding a test case to a numbered normative clause.

### A5. Money libraries with unit tests but no separable case corpus

* **joda-money** — https://github.com/JodaOrg/joda-money. Licence **VERIFIED Apache-2.0**
  (`LICENSE.txt`). Counted: 15 test source files, **995 `@Test` methods**; `src/test/resources`
  contains only `META-INF`. **No standalone case table.** *SAFE TO VENDOR (Apache-2.0) but low
  yield — REFERENCE for its rounding/`CurrencyUnit` semantics, not a corpus.*
* **dinero.js** — https://github.com/dinerojs/dinero.js. Licence **VERIFIED MIT**
  (`LICENSE`: *"The MIT License (MIT) Copyright (c) 2018-present Sarah Dayan"*). Useful as a
  worked model of scaled-integer money and its rounding functions; **no separable corpus.**
  *REFERENCE.*
* **libmpdec / mpdecimal (Stefan Krah)** — vendored in CPython as `_decimal`. Licence **VERIFIED**
  from CPython `Doc/license.rst`: *"Copyright (c) 2008-2020 Stefan Krah. All rights reserved."*
  followed by the two-clause redistribution conditions → **BSD-2-Clause**. It re-ships the decTest
  data, so the A1 caveat still governs the data itself. *Code SAFE TO VENDOR; data REFERENCE-ONLY.*

---

## B. Rounding mode and currency minor units

### B1. Unicode CLDR `currencyData`  SAFE TO VENDOR — the rounding-rules ground truth

* **URL:** https://github.com/unicode-org/cldr — `common/supplemental/supplementalData.xml`,
  element `<currencyData>`
* **Contents:** the authoritative machine-readable table of **currency minor units and rounding
  increments**, including the *cash* variants that ISO 4217 alone does not give you.
* **Format:** XML, e.g.
  ```xml
  <info iso4217="JPY" digits="0" rounding="0"/>
  <info iso4217="KWD" digits="3" rounding="0"/>
  <info iso4217="CHF" digits="2" rounding="0" cashRounding="5"/>
  <info iso4217="HUF" digits="0" rounding="0" cashRounding="5"/>
  ```
* **Volume (counted, `main`, 2026-09-05, 394,860-byte file):**
  **76** `<info iso4217=…>` entries; **53** deviate from the `digits="2" rounding="0"` default;
  **14** currencies carry `cashDigits="0"`, 1 carries `cashDigits="2"`;
  **cashRounding** values present: `0` ×14, `5` ×3, `20` ×1, `50` ×1.
  Also **266** `<region iso3166=…>` currency-history blocks.
* **Ground truth:** yes — this *is* the expected value for "how many minor units, and to what
  increment does cash round".
* **Licence — VERIFIED from the repo `LICENSE`:** the LDML *specification prose* is restricted
  ("you may not make copies of or modifications to this publication for public distribution"), but
  the file then states verbatim: **"All other content in this repo is released under UNICODE
  LICENSE V3"**, granting *"permission … to deal in the Data Files or Software without restriction,
  including without limitation the rights to use, copy, modify, merge, publish, distribute, and/or
  sell copies"* subject to the notice. `supplementalData.xml` is a data file, not the LDML prose.
  → **Unicode License v3 — permissive.**
* **Verdict: SAFE TO VENDOR** (reproduce the Unicode notice; do **not** vendor UTS #35 prose).
* **Reuse path:** generate one case per currency per rounding mode.
  `provisions engaged` ← "amounts must be stored and settled at the currency's minor unit";
  `factor facts` ← `currency_has_zero_minor_units`, `currency_has_three_minor_units`,
  `currency_has_cash_rounding_increment`, `amount_scale_exceeds_currency_minor_units`;
  `expected disposition` ← the rounded value / `REJECT(scale_exceeds_minor_units)`.
  The 53 non-default currencies are precisely the adversarial cases (JPY 0, KWD/BHD/JOD 3,
  CHF/HUF cash-rounds to 5, CLF 4).

### B2. ISO 4217 (SIX Group, maintenance agency)  REFERENCE-ONLY (licence not established)

* **URL:** https://www.six-group.com/en/products-services/financial-information/data-standards.html
  (List One current currencies XLS/XML; List Three historical XLS/XML; amendments as PDF).
* **Contents:** currency code, numeric code, and **minor unit** per currency/territory.
* **Licence — NOT ESTABLISHED.** The SIX page states the files are made available
  *"free of charge"* on behalf of ISO and SNV, but **publishes no copyright grant, licence, or
  terms-of-use statement on that page**. "Free of charge" is a price, not a licence.
  → **UNVERIFIED. Do not vendor.** Use **CLDR (B1)** instead — it carries the same minor-unit facts
  under a verified permissive licence, plus the cash-rounding increments ISO 4217 omits.

### B3. Round-half-even test vectors — where they actually are

There is **no dedicated open "bankers' rounding corpus"**. The three verified sources that
collectively cover it:

1. **decTest** (A1) — 39,940 cases under `rounding: half_even`, plus 374 `half_down`, 23,512
   `half_up`, and the `quantize` operation (2,164 cases) which is the money-rounding primitive.
   *REFERENCE-ONLY licence.*
2. **rust_decimal** `tests/decimal_tests/rounding.rs` (A2) — 35 assertions across all
   7 strategies including `MidpointNearestEven`. *MIT, vendorable.*
3. **CLDR `currencyData`** (B1) — the increments to round *to*. *Unicode v3, vendorable.*

---

## C. Transaction correctness and isolation

### C1. PostgreSQL `src/test/isolation`  SAFE TO VENDOR — the largest executable isolation corpus

* **URL:** https://github.com/postgres/postgres/tree/master/src/test/isolation
* **Contents:** the isolation regression suite. Purpose-built concurrency scenarios driven by
  `isolationtester`, each a declarative spec with `setup` / `session` / `step` / `permutation` and a
  byte-exact expected output file.
* **Volume (counted, `master`, 2026-09-05):**
  * **134 `.spec` files**, **143 `.out` expected-output files**
  * **2,768 explicit `permutation` lines** — each is one executable, expected-result case
  * **1,779** expected-output lines asserting `ERROR: could not serialize access …` — i.e. 1,779
    ground-truth *serialization-failure dispositions*
  * **52 specs** mention `bank_account` / `balance` / write skew / lost update / serializable /
    deadlock; the explicitly monetary ones are `read-only-anomaly{,-2,-3}.spec`, `total-cash.spec`,
    `simple-write-skew.spec`, `matview-write-skew.spec`, `serializable-parallel{,-2,-3}.spec`,
    `eval-plan-qual.spec`, `merge-match-recheck.spec`, `timeouts.spec`, plus 6 `deadlock-*.spec`,
    `fk-deadlock{,2}.spec`, 4 `skip-locked*.spec`, `predicate-lock-hot-tuple.spec`,
    `multiple-row-versions.spec`, `classroom-scheduling.spec`
* **Format example** (`read-only-anomaly.spec`, verbatim excerpt) — note it is literally a bank
  ledger:
  ```
  setup { CREATE TABLE bank_account (id TEXT PRIMARY KEY, balance DECIMAL NOT NULL);
          INSERT INTO bank_account (id, balance) VALUES ('X', 0), ('Y', 0); }
  session s1  setup { BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ; }
    step s1ry { SELECT balance FROM bank_account WHERE id = 'Y'; }
    step s1wy { UPDATE bank_account SET balance = 20 WHERE id = 'Y'; }
  permutation s2rx s2ry s1ry s1wy s1c s3r s2wx s2c s3c
  ```
* **Ground truth:** yes, and it is *exact* — the `.out` file is the required output byte for byte,
  including the error text and SQLSTATE-bearing messages.
* **Licence — VERIFIED** from `COPYRIGHT` in the repo root: *"Portions Copyright (c) 1996-2026,
  PostgreSQL Global Development Group. Portions Copyright (c) 1994, The Regents of the University of
  California. Permission to use, copy, modify, and distribute this software and its documentation
  for any purpose, without fee, and without a written agreement is hereby granted…"*
  → **PostgreSQL Licence** (permissive, BSD/MIT-class).
* **Verdict: SAFE TO VENDOR.**
* **Reuse path:** the mapping is direct and mechanical.
  `case id` ← `<spec-name>#<permutation index>`;
  `provisions engaged` ← the declared isolation level in the session `setup` (READ COMMITTED /
  REPEATABLE READ / SERIALIZABLE) mapped to your isolation control;
  `boolean factor facts` ← `two_transactions_write_same_row`, `read_then_write_on_predicate`,
  `transaction_reads_uncommitted_value`, `concurrent_update_after_snapshot`;
  `expected disposition` ← `COMMIT_SUCCEEDS` vs `ABORT(serialization_failure)` vs
  `ABORT(deadlock_detected)`, read off the `.out` file.
  Because the fixture table is already `bank_account(id, balance DECIMAL)`, the finance re-skin is
  cosmetic. **This is the transaction-isolation corpus to start with.**

### C2. Hermitage (Martin Kleppmann)  SAFE TO VENDOR (attribution) — the ground-truth *matrix*

* **URL:** https://github.com/ept/hermitage
* **Contents:** per-anomaly, per-DBMS SQL transcripts plus a summary matrix of which isolation
  levels prevent which anomalies.
* **Anomalies — the exact ten:** **G0** (write cycles / dirty write), **G1a** (aborted read),
  **G1b** (intermediate read), **G1c** (circular information flow), **OTV** (observed transaction
  vanishes), **PMP** (predicate-many-preceders), **P4** (lost update), **G-single** (read skew /
  single anti-dependency cycle), **G2-item** (write skew), **G2** (anti-dependency cycles).
* **Volume (counted, `master`, 2026-09-05):**
  * 9 DBMS files: PostgreSQL, MySQL/InnoDB, Oracle, MS SQL Server, FoundationDB, CockroachDB,
    YugabyteDB, TiDB, Memgraph
  * **25 (DBMS × isolation-level) configurations × 10 anomalies = 250 verdict cells** in the README
    matrix, with a four-valued verdict vocabulary: `✓` prevented, `—` can occur, `R/O` prevented
    only for read-only, `some` prevented in some cases
  * scripted `BEGIN` blocks per file: sqlserver 88, mysql 55, postgres/cockroachdb/yugabytedb 42
    each, tidb 31 (oracle, foundationdb, memgraph are prose/narrative)
* **Ground truth:** yes — the 250-cell matrix *is* the expected-disposition table.
* **Format:** Markdown with inline SQL; tests are run by hand across parallel sessions.
* **Licence — VERIFIED** from `README.md`: *"Copyright Martin Kleppmann, 2014. This work is licensed
  under a Creative Commons Attribution 4.0 International License."* → **CC BY 4.0.**
* **Verdict: SAFE TO VENDOR** with attribution (CC BY 4.0 suits a documentation-shaped corpus well;
  note it is a *content* licence, so keep it in a clearly-attributed corpus directory).
* **Reuse path:** the highest-value single import in this lane.
  `case id` ← `hermitage/<dbms>/<isolation-level>/<anomaly>`;
  `provisions engaged` ← "the ledger's declared isolation guarantee";
  `boolean factor facts` ← one boolean per anomaly (`anomaly_G2_item_possible = true`, …) plus
  `declared_isolation_level_is_repeatable_read`;
  `expected disposition` ← `PREVENTED` / `POSSIBLE` / `PREVENTED_READ_ONLY_ONLY` / `PARTIAL`.
  250 cases, already labelled, zero derivation work.

### C3. Elle — transactional consistency checker (Jepsen)  SAFE TO VENDOR (copyleft-aware)

* **URL:** https://github.com/jepsen-io/elle
* **Paper (citable):** Kyle Kingsbury and Peter Alvaro, *"Elle: Inferring Isolation Anomalies from
  Experimental Observations"*, arXiv:2003.10554 (2020); VLDB'21 copy at
  https://people.ucsc.edu/~palvaro/elle_vldb21.pdf. The abstract states Elle *"can detect every
  anomaly in Adya et al's formalism (except for predicates), discriminate between them, and provide
  concise explanations of each"* — so **yes, the taxonomy is citable, and it is citable *through*
  Adya**, which is the right primary reference for a compliance document.
* **Contents & volume (counted, `main`, 2026-09-05):**
  * `src/elle/consistency_model.clj`: **33 consistency models** in the `models` implication graph,
    **33** entries in `implied-anomalies`, **25** entries in `direct-proscribed-anomalies`,
    **18** entries in `canonical-model-names` (mapping friendly names to Adya's PL-1, PL-2,
    PL-2.99, PL-3, PL-SI, PL-SS, PL-CS, PL-FCV, PL-MSR, PL-2L, PL-3U…), and ~**68 distinct anomaly
    names** referenced
  * the anomaly vocabulary includes `G0, G1a, G1b, G1c, G2, G2-item, G-single, G-SI, G-nonadjacent,
    GSIa, GSIb, lost-update, dirty-update, cyclic-versions, duplicate-elements, future-read,
    incompatible-order, predicate-read-miss`, each also in `-process` and `-realtime` variants
  * `proof/`: **18 Isabelle/HOL `.thy` files** (`Anomaly.thy`, `DSG.thy`, `IDSG.thy`,
    `InferredAnomaly.thy`, `VersionOrder.thy`, …) — a mechanised formalisation of the taxonomy
  * `histories/`: 5 named example histories (`paper-example.edn`, `cyclic-versions.edn`,
    `si-without-g-single.edn`, `huge-scc.edn`, `small-slow-scc.edn`), **51 MB**
  * `test/`: 11 Clojure test namespaces, 4,540 lines
* **The reusable oracle:** `(anomalies-prohibited-by [models])` returns, for any set of consistency
  models, the closed set of anomalies that must not occur — and `anomalies->impossible-models` runs
  it backwards. **That is an executable provisions→disposition function.**
* **Ground truth:** yes — deterministic, and generatable at scale (see C4).
* **Licence — VERIFIED:** `project.clj` declares
  `:license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"}`; `LICENSE` is the
  Eclipse Public License v2.0 text. → **EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0.**
* **Verdict: SAFE TO VENDOR under the EPL-2.0 arm** — but EPL-2.0 is file-level weak copyleft:
  keep Elle's files in their own directory with their notices, do not paste its source into
  differently-licensed files. The *derived data* (a table of model → prohibited anomalies) is a
  fact table and is the cleaner thing to import.
* **Reuse path:** run `anomalies-prohibited-by` over the 33 models to emit a
  `(model, anomaly) → prohibited?` table. `provisions engaged` ← the consistency model your ledger
  claims; `factor facts` ← observed anomaly booleans; `expected disposition` ← `NON_COMPLIANT` when
  an observed anomaly is in the prohibited set.

### C4. `jepsen.history.sim` — generator of ground-truth-labelled histories  SAFE TO VENDOR

* **URL:** https://github.com/jepsen-io/history.sim
* **Contents:** verbatim from its README — *"Generates Jepsen histories from simulated databases,
  for testing safety checkers… These histories should exhibit certain classes of anomalies, so that
  you can test whether the checker is correct. They should be deterministic, so you can build
  regression tests."*
* **Volume:** unbounded, parameterised by `:db`, `:generator`, `:concurrency`, `:limit`. Counted
  **4 simulated concurrency-control models** in `src/jepsen/history/sim/db.clj`:
  `:brat` (read-atomic), `:prefix`, `:si` (snapshot isolation), `:ssi` (snapshot serializable).
* **Format:** EDN or JSON to stdout (so usable from non-JVM harnesses).
* **Ground truth:** yes *by construction* — you know which model produced the history, hence which
  anomalies are admissible.
* **Licence — VERIFIED:** `project.clj`
  `:license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"}`.
* **Verdict: SAFE TO VENDOR** (same EPL caveat as C3), and better: run it once, vendor only the
  emitted JSON, which is data you generated.
* **Reuse path:** the answer to "we need thousands of isolation cases, not 250". Emit N histories
  per model, label each with the model that produced it, and let the corpus assert
  `expected_disposition = COMPLIANT` iff the checker's inferred anomalies ⊆
  `anomalies-permitted-by(model)`.

### C5. Jepsen (framework) and its published analyses  SPLIT VERDICT

* **Framework:** https://github.com/jepsen-io/jepsen — licence **VERIFIED** from
  `jepsen/project.clj`: `:license {:name "Eclipse Public License"}` → **EPL.** *SAFE TO VENDOR
  (EPL, file-level).*
* **Per-target test suites**, e.g. https://github.com/jepsen-io/tigerbeetle — `LICENSE` **VERIFIED**
  as **Eclipse Public License v2.0**. Contains `model.clj` (1,691 lines: a full state-machine model
  of a financial ledger, with a `permanent-errors` set including `:exceeds-credits` and
  `:exceeds-debits`), `checker.clj`, `explainer.clj`, `lifecycle_map.clj`, `nemesis.clj`
  (5,190 lines total). *SAFE TO VENDOR (EPL-2.0). This is a ready-made reference ledger model.*
* **The written analyses at jepsen.io/analyses:** **REFERENCE-ONLY.** Footer verified verbatim:
  *"Copyright © Jepsen, LLC. We do our best to provide accurate information, but if you see a
  mistake, please let us know."* — **no licence grant.** Cite and link; do not reproduce.
* **Worth citing:** *Jepsen: TigerBeetle 0.16.11* (https://jepsen.io/analyses/tigerbeetle-0.16.11)
  is directly on-point for a fintech ledger. Verified content: faults injected were SIGKILL/SIGSTOP,
  transitive and non-transitive network partitions, delays/drops/duplicates/corruption, clock jumps
  and oscillation, storage bit-flips, chunk misplacement, snapshot restoration, rolling upgrades,
  and "helical" cross-node corruption. Invariants checked: strong serializability via Elle cycle
  detection, a custom ledger state-machine model, durability under disk corruption, exact query
  results, and **idempotence — "no divergent values from duplicate writes."** Findings: 2 safety
  issues, 7 crashes, plus availability/latency issues.

### C6. TPC-C consistency conditions  REFERENCE-ONLY, but *quotable* — licence better than expected

* **URL:** https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-c_v5.11.0.pdf (free PDF)
* **Contents:** Clause 3 "Transaction and System Properties (ACID)"; Clause 3.3 Consistency, whose
  §3.3.2 enumerates consistency conditions (3.3.2.1 …) as arithmetic invariants over the warehouse /
  district / order tables — the canonical "the books must balance" checks.
* **Licence — VERIFIED verbatim from the specification title page:**
  > "© 2010 Transaction Processing Performance Council. Permission to copy without fee all or part
  > of this material is granted provided that the TPC copyright notice, the title of the
  > publication, and its date appear, and notice is given that copying is by permission of the
  > Transaction Processing Performance Council."

  So it is **not paywalled and not un-copyable**: verbatim reproduction with the notice is expressly
  permitted. Use of the *benchmark* and its results is separately governed by the TPC Fair Use
  Policies and EULA (linked from the same page).
* **Caveat — do not take a count on trust:** I could not retrieve §3.3.2 itself from any accessible
  copy (tpc.org is blocked from this environment's egress; the Brown mirror truncates before
  Clause 3). **The number of consistency conditions is therefore UNVERIFIED** — read the PDF
  directly before citing a count.
* **Verdict: REFERENCE-ONLY for the benchmark; the consistency-condition text is quotable** under
  the copy permission above, with the TPC notice attached.
* **Reuse path:** TPC-C's conditions are the archetype for a fintech "ledger balances" provision:
  each is of the form *aggregate over child rows must equal a denormalised parent field*. Restate
  them as `provisions engaged = ledger_totals_must_reconcile`,
  `factor facts = {denormalised_total_maintained_in_separate_row,
  aggregate_recomputed_under_concurrency}`, `expected disposition = BALANCED / IMBALANCED`.

### C7. pgjdbc  LOW YIELD

* https://github.com/pgjdbc/pgjdbc — licence **VERIFIED** from `LICENSE`:
  *"Copyright (c) 1997, PostgreSQL Global Development Group. All rights reserved. Redistribution and
  use in source and binary forms… 1. … 2. …"* → **BSD-2-Clause.**
* Its isolation-related tests exercise the JDBC driver, not the isolation semantics; C1 supersedes
  it. *SAFE TO VENDOR licence-wise, but not worth importing.*

### C8. Anomaly names — the citable literature

The standard names your factor vocabulary should use, and where they come from:

* **Berenson, Bernstein, Gray, Melton, O'Neil, O'Neil, "A Critique of ANSI SQL Isolation Levels"**
  (SIGMOD 1995) — introduces P0 dirty write, P1 dirty read, P2 fuzzy read, P3 phantom, **P4 lost
  update**, A5A read skew, A5B write skew, and snapshot isolation.
* **Adya, Liskov, O'Neil, "Generalized Isolation Level Definitions"** (ICDE 2000) / Adya's MIT PhD
  thesis — the implementation-independent **G0/G1a/G1b/G1c/G2** phenomena and the **PL-1 / PL-2 /
  PL-2.99 / PL-3 / PL-SI / PL-SS** level names. This is the formalism Elle mechanises and the one to
  cite normatively.
* **Fekete, Liarokapis, O'Neil, O'Neil, Shasha**, serializable snapshot isolation — the source of
  the *dangerous structure* / write-skew analysis.
* **Elle** (C3) — the modern, machine-checked restatement; cite for the checker, cite Adya for the
  definitions.

---

## D. Idempotency and exactly-once

### D1. IETF `Idempotency-Key` HTTP header  REFERENCE-ONLY, and note the status

* **URL:** https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
* **Status — VERIFIED:** `draft-ietf-httpapi-idempotency-key-header-07`, HTTPAPI working group,
  latest revision **2025-10-15**, **EXPIRED**, intended status "(None)". **It is not an RFC and it
  is not currently an active draft.**
* **Verdict:** cite as the *de facto* interoperability reference and as evidence that the semantics
  are contested/unsettled — **do not cite it as a standard**. IETF documents are governed by the
  IETF Trust Legal Provisions; code components carry a BSD-style licence, prose does not.
* **Practical consequence for the corpus:** because there is no ratified standard, the normative
  content for an idempotency provision must come from vendor contracts (D2, D3), which is exactly
  what a fintech's own change-control regime would rely on.

### D2. Stripe idempotency semantics  REFERENCE-ONLY (documentation, no licence) — but precise

Verified from https://docs.stripe.com/api/idempotent_requests and
https://docs.stripe.com/error-low-level :

* Header `Idempotency-Key`, client-generated, **up to 255 characters**, UUIDv4 recommended.
* **Key lifetime: 24 hours.** *"You can remove keys from the system automatically after they're at
  least 24 hours old. We generate a new request if a key is reused after the original is pruned."*
* Replay returns the **saved status code and body of the first request, regardless of whether it
  succeeded or failed — including 500s.** A request that returned 400 returns the same 400 on
  replay.
* **Parameter mismatch:** *"The idempotency layer compares incoming parameters to those of the
  original request and errors if they're not the same to prevent accidental misuse."*
* **Concurrency:** **HTTP 409 Conflict** — *"The request conflicts with another request (perhaps due
  to using the same idempotent key)."*
* **Not saved:** results are saved *"only after the execution of an endpoint begins"* — so parameter
  validation failures and concurrent conflicts are **not** cached and are safely retryable.
  429 rate-limits and 401s bypass the idempotency layer entirely.
* **Replay detection:** response header `Idempotent-Replayed: true`.
* Retry advice signalled by `Stripe-Should-Retry: true|false|absent`.
* All `POST`s accept keys; `GET`/`DELETE` are idempotent by definition.

### D3. Adyen idempotency semantics  REFERENCE-ONLY (documentation) — the useful contrast

Verified from https://docs.adyen.com/development-resources/api-idempotency :

* Header `idempotency-key`, **max 64 characters**, UUID recommended, **scoped to the company
  account**.
* **Key lifetime: "valid for a period of 7 to 14 days after first submission"** — 7–14× Stripe's
  24 hours. The divergence between two major PSPs is itself the point: an idempotency provision must
  state its own retention window, because there is no industry constant.
* Replay returns the first response without duplication, echoing the `idempotency-key` header.
* **Concurrency: HTTP 422 or HTTP 409 with error code 704 "request already processed or in
  progress."** Error 703 = "required resource temporarily unavailable" (transient).
* A `transient-error: true` response header means the request may be safely retried with the same
  key.

### D4. TigerBeetle create-transfer / create-account status enums  SAFE TO VENDOR — best idempotency factor list

See E1 — the enum contains `exists`, `exists_with_different_amount`,
`exists_with_different_debit_account_id`, `exists_with_different_flags`, `id_already_failed`, etc.
That is a **machine-readable, Apache-2.0 enumeration of idempotency-key outcomes** — precisely the
"same key, different parameters" case that Stripe and Adyen describe only in prose.

### D5. Apache Kafka transactional / exactly-once system test  SAFE TO VENDOR

* **URL:** https://github.com/apache/kafka/blob/trunk/tests/kafkatest/tests/core/transactions_test.py
  (and `transactions_mixed_versions_test.py`)
* **Contents (verified, 263 lines):** *"Tests transactions by transactionally copying data from a
  source topic to a destination topic and killing the copy process as well as the broker randomly
  through the process. In the end we verify that the final output topic contains exactly one
  committed copy of each message in the input topic."*
* **Parameters (verified):** 100,000 seed messages, transaction size 750, 3 brokers,
  2 input / 3 output partitions.
* **Assertions (verified, the disposition oracle):**
  * `num_dups == 0` — "Detected %d duplicates in the output stream"
  * `input_message_set == output_message_set`
  * `num_dups_in_concurrent_consumer == 0`
  * `concurrently_consumed_message_set == input_message_set`
  * under `check_order=True`: `output_messages == input_messages` (order preserved)
* **Volume:** a `@matrix` over `failure_mode ∈ {hard_bounce, clean_bounce}` ×
  `bounce_target ∈ {brokers, clients}` × `check_order ∈ {T,F}` × `use_group_metadata ∈ {T,F}` ×
  `use_transactions_v2 ∈ {T,F}` × `metadata_quorum` × `group_protocol` — i.e. **≥32 parametrised
  runs before the quorum/protocol dimensions multiply out.** (I did not resolve the cardinality of
  `quorum.all_kraft` and `consumer_group.all_group_protocols`, so no total is asserted.)
* **Ground truth:** yes — set equality against the seeded input, plus a zero-duplicates invariant.
* **Licence — VERIFIED:** repo `LICENSE` is the **Apache License 2.0**.
* **Verdict: SAFE TO VENDOR.**
* **Reuse path:** this is the *exactly-once delivery* case family.
  `provisions engaged` ← "payment events must be delivered exactly once end-to-end";
  `boolean factor facts` ← `producer_crashed_mid_transaction`, `broker_hard_bounced`,
  `consumer_group_rebalanced`, `ordering_required`;
  `expected disposition` ← `NO_DUPLICATES ∧ NO_LOSS ∧ (ORDER_PRESERVED if ordering_required)`.

---

## E. Double-spend, concurrent withdrawal, ledger invariants

### E1. TigerBeetle  SAFE TO VENDOR — the richest single invariant vocabulary in this lane

* **URL:** https://github.com/tigerbeetle/tigerbeetle ; docs https://docs.tigerbeetle.com
* **Licence — VERIFIED:** repo `LICENSE` is the **Apache License, Version 2.0**.
* **The corpus-grade artefact:** the result enums in `src/tigerbeetle.zig`, counted at `main`
  on 2026-09-05:
  * **`CreateAccountStatus`: 28 variants**
  * **`CreateTransferStatus`: 70 variants**

  These are a complete, machine-readable, versioned enumeration of *every way a ledger write can be
  rejected*. Grouped by the compliance concern they serve:

  | Concern | Status codes (verbatim) |
  |---|---|
  | **Double-spend / overdraft** | `exceeds_credits`, `exceeds_debits`, `debit_account_already_closed`, `credit_account_already_closed` |
  | **Arithmetic overflow** | `overflows_debits_pending`, `overflows_credits_pending`, `overflows_debits_posted`, `overflows_credits_posted`, `overflows_debits`, `overflows_credits`, `overflows_timeout` |
  | **Idempotency** | `exists`, `exists_with_different_amount`, `exists_with_different_flags`, `exists_with_different_debit_account_id`, `exists_with_different_credit_account_id`, `exists_with_different_ledger`, `exists_with_different_code`, `exists_with_different_pending_id`, `exists_with_different_timeout`, `exists_with_different_user_data_128/64/32`, `id_already_failed` |
  | **Atomicity of linked chains** | `linked_event_failed`, `linked_event_chain_open` |
  | **Two-phase (pending) transfers** | `pending_transfer_not_found`, `pending_transfer_not_pending`, `pending_transfer_already_posted`, `pending_transfer_already_voided`, `pending_transfer_expired`, `exceeds_pending_transfer_amount`, `pending_transfer_has_different_amount/ledger/code/debit_account_id/credit_account_id`, `timeout_reserved_for_pending_transfer`, `closing_transfer_must_be_pending` |
  | **Referential / ledger integrity** | `debit_account_not_found`, `credit_account_not_found`, `accounts_must_be_different`, `accounts_must_have_the_same_ledger`, `transfer_must_have_the_same_ledger_as_accounts`, `ledger_must_not_be_zero`, `code_must_not_be_zero` |
  | **Immutability / append-only import** | `imported_event_expected`, `imported_event_not_expected`, `imported_event_timestamp_out_of_range`, `imported_event_timestamp_must_not_advance`, `imported_event_timestamp_must_not_regress`, `imported_event_timestamp_must_postdate_debit_account`, `imported_event_timestamp_must_postdate_credit_account`, `timestamp_must_be_zero` |
  | **Opening-balance integrity** | `debits_pending_must_be_zero`, `debits_posted_must_be_zero`, `credits_pending_must_be_zero`, `credits_posted_must_be_zero` |

* **Documented invariants** (verified at https://docs.tigerbeetle.com/coding/data-modeling/):
  * `flags.credits_must_not_exceed_debits` and `flags.debits_must_not_exceed_credits` — the
    non-negative-balance / overdraft controls
  * *"The primary purpose of an `id` is to serve as an 'idempotency key' — to avoid executing an
    event twice."*
  * *"Accounts and transfers are immutable once created."*
  * every transfer is single-debit / single-credit; multi-party movements use **atomically linked
    transfers** or the **two-phase pending/post/void** protocol
* **VOPR (deterministic simulator)** — https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/internals/vopr.md.
  Verified: reproducible from `(seed, git commit)`; injects packet drops, reordering, network
  partitions, and disk read/write corruption; asserts thousands of in-code assertions plus
  cluster-level checkers, including that data files are **"byte-for-byte identical"** across
  caught-up replicas. *"One minute of VOPR time is equivalent to days of real-world testing."*
  No published seed corpus was found; the value is the **methodology**, not a downloadable corpus.
* **Verdict: SAFE TO VENDOR** (Apache-2.0). Note: `src/state_machine.zig` (5,161 lines) has only
  **one** `test` block (`sum_overflows`) — the assertions live in the simulator, not in a table of
  cases. **Vendor the enums, not the tests.**
* **Reuse path:** take the 98 status codes as your **factor-and-disposition vocabulary** for ledger
  writes. Each becomes a `expected disposition = REJECT(<status>)` with the corresponding boolean
  factor, e.g. `factor: transfer_would_make_debits_exceed_credits` → `REJECT(exceeds_credits)`.
  This is the fastest route to a defensible, complete-looking double-spend factor list.

### E2. `jepsen-io/tigerbeetle` ledger model  SAFE TO VENDOR (EPL-2.0)

Already noted in C5. The specific value here: `src/jepsen/tigerbeetle/model.clj` (1,691 lines) is an
independent, executable **reference model of a financial ledger** — including a `permanent-errors`
set that treats `:exceeds-credits` and `:exceeds-debits` as sticky (a rejected transfer stays
rejected on retry with the same id). That single design decision is the crisp statement of
"idempotency must preserve *failures*, not only successes" — worth lifting into a provision.

### E3. Formance Ledger  SAFE TO VENDOR

* **URL:** https://github.com/formancehq/ledger
* **Licence — VERIFIED:** `LICENSE` reads `MIT License / Copyright (c) 2021-present Formance
  Solutions`. → **MIT.**
* **Contents:** a production double-entry ledger with a scripting language (Numscript) for
  multi-posting atomic transactions and explicit insufficient-funds handling.
* **Verdict: SAFE TO VENDOR.** *REFERENCE* for the API/behaviour surface; it does not ship a
  standalone case corpus comparable to E1's enums.

### E4. Plain-text accounting: hledger, Beancount  COPYLEFT — REFERENCE-ONLY for a permissive corpus

* **hledger** — https://github.com/simonmichael/hledger. Licence **VERIFIED:** `LICENSE` is the
  **GNU General Public License, Version 3**.
* **Beancount** — https://github.com/beancount/beancount. Licence **VERIFIED:** `COPYING` is the
  **GNU General Public License, Version 2**.
* **Why they matter anyway:** both implement, and test, the fundamental accounting invariants —
  **every transaction's postings must sum to zero** (double-entry balance), balance assertions
  (`assert` / `balance` directives) that fail loudly when a computed balance diverges from a
  declared one, and strict-mode account/commodity declaration checks. These are the *provisions*
  your ledger-integrity cases enforce.
* **Verdict: REFERENCE-ONLY** if the compliance corpus ships under a permissive licence — GPL-2/3
  test data would infect it. **Restate the invariants in your own words; do not copy their test
  files.** (If the corpus is itself GPL-compatible, they become vendorable.)

### E5. Is there an open benchmark for *simultaneous debits on one account*?

**No dedicated one was found.** The nearest verified substitutes, in order of usefulness:

1. **PostgreSQL `read-only-anomaly.spec` / `total-cash.spec` / `simple-write-skew.spec`** (C1) —
   literally `bank_account(id, balance DECIMAL)` with concurrent balance updates and exact expected
   outputs. PostgreSQL Licence.
2. **Hermitage P4 (Lost Update) and G2-item (Write Skew)** (C2) — the canonical two-concurrent-
   withdrawals shape, with per-database expected verdicts. CC BY 4.0.
3. **TigerBeetle `exceeds_credits` / `exceeds_debits`** (E1) — the disposition names.
4. **`jepsen.history.sim`** (C4) — to generate thousands more.

Compose these: PostgreSQL supplies the executable scenario, Hermitage the labelled verdict matrix,
TigerBeetle the disposition vocabulary, history.sim the volume.

---

## F. Event sourcing, append-only ledgers, WORM

### F1. SEC Rule 17a-4(f) — 17 CFR 240.17a-4(f)  PUBLIC DOMAIN (US federal regulation)

* **URL:** https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 (eCFR;
  intermittently 503) — mirror used for verification:
  https://www.law.cornell.edu/cfr/text/17/240.17a-4
* **Status:** US federal regulation — **no copyright, freely reproducible.** Materially amended by
  the SEC in October 2022 (Release 34-96034; 87 FR 66412, 2022-11-03), which added the audit-trail
  alternative alongside WORM.
* **Verified structure — the two permitted alternatives:**
  * **(f)(2)(i)(A) audit-trail alternative** — preserve the record for its retention period
    *"in a manner that maintains a complete time-stamped audit trail"* of modifications and
    deletions, with dates/times, the identity of individuals making changes, and the information
    needed to maintain security and authenticity.
  * **(f)(2)(i)(B) WORM alternative** — *"preserve the records exclusively in a non-rewriteable,
    non-erasable format."*
* **Verified conditions applying to the electronic recordkeeping system, (f)(2):**
  1. verify automatically the completeness and accuracy of the storage and retention processes;
  2. serialise the original and duplicate units of storage media and time-date the retention period;
  3. have the capacity to readily download and transfer copies in both human-readable and reasonably
     usable electronic formats;
  4. maintain a backup electronic recordkeeping system meeting the same requirements, or equivalent
     redundancy.
* **Verified operational requirements, (f)(3):** facilities for immediate production of records;
  ready access; **for WORM systems, an audit system tracking all inputting and changes**;
  organisation and maintenance of access/location information; and a filed **undertaking** with the
  designated examining authority.
* **Reuse path:** this is a genuine *provision* for the corpus, not merely a source.
  `provisions engaged` ← `17_CFR_240.17a-4(f)(2)(i)(A)` vs `…(f)(2)(i)(B)`;
  `boolean factor facts` ← `records_stored_non_rewriteable_non_erasable`,
  `complete_time_stamped_audit_trail_maintained`, `modifying_actor_identity_recorded`,
  `deletion_recorded_rather_than_applied`, `duplicate_media_serialised`,
  `records_downloadable_in_human_readable_form`, `redundant_backup_system_present`;
  `expected disposition` ← `COMPLIANT` iff (A) **or** (B) holds *and* all (f)(2)/(f)(3) conditions
  hold. Note the disjunction — a change that replaces WORM storage with a mutable store *plus* a
  complete audit trail is compliant post-2022 and non-compliant pre-2022. That is an excellent
  hard case.

### F2. Is there an open conformance suite for immutability / compensating transactions?

**No.** I found no open conformance corpus for event-sourcing immutability or compensating-
transaction (saga) semantics. The verified partial substitutes:

* **TigerBeetle's `imported_event_*` status codes** (E1) — 8 codes that are precisely an
  append-only/monotonic-timestamp conformance vocabulary, Apache-2.0.
* **TigerBeetle two-phase pending/post/void** (E1) — `pending_transfer_already_posted`,
  `pending_transfer_already_voided`, `pending_transfer_expired` are exactly compensating-transaction
  dispositions.
* **Beancount/hledger balance assertions** (E4) — the "recompute from the log and compare" check,
  GPL, restate rather than copy.

This is a genuine gap and a place where the corpus can contribute something new.

---

## G. Circuit breakers and resilience on payment paths

### G1. resilience4j  SAFE TO VENDOR — but no financial variant exists

* **URL:** https://github.com/resilience4j/resilience4j
* **Licence — VERIFIED:** `LICENSE.txt` is the **Apache License, Version 2.0**.
* **Searched for a financial/payments-specific variant or test suite: none found.** The tests are
  generic (state transitions CLOSED → OPEN → HALF_OPEN, failure-rate and slow-call-rate thresholds,
  bulkhead, rate limiter, retry, time limiter). *Extend only via the published timeout budgets
  below, which supply the numbers a generic circuit-breaker suite lacks.*

### G2. Published payment-path timeout budgets  REFERENCE-ONLY (vendor documentation) — but exact

Verified from https://docs.adyen.com/point-of-sale/error-scenarios/pos-timeouts — the only
*published, numeric* payment timeout budget found:

* **Processing timeout: 120 s (local integration), 150 s (cloud integration).** Verbatim: *"If you
  do not receive either a payment result or a time-out after 120 seconds (local integration) or 150
  seconds (cloud integration), your integration should automatically send a transaction status
  request to verify if the payment has been processed."*
* Device-interaction timeouts: card insertion/swipe/tap **120 s**; QR scan **120 s**; account-type
  selection **120 s**; application selection **120 s**; DCC acknowledgement **120 s**;
  **PIN entry 60 s**; signature capture **60 s**; signature review **900 s**; manual card entry
  **60 s**; **authorisation in progress 200 s**; receipt confirmation **120 s**; donations **30 s**;
  tipping **60 s**; gift-card balance **10 s**; final-state display **4 s**.
* Recovery behaviour: on timeout, issue a **transaction status request** — never a blind retry of
  the payment.
* Stripe's corresponding published number is the **24-hour idempotency-key window** (D2), plus
  `Stripe-Should-Retry` as the retry oracle. Stripe does not publish a request timeout budget;
  it is client-configurable (see stripe/stripe-python#186).

* **Reuse path:** `provisions engaged` ← "a payment request that times out must be resolved by
  status enquiry, not by retry, within the gateway's stated budget";
  `boolean factor facts` ← `elapsed_exceeds_gateway_processing_timeout`,
  `status_enquiry_issued_before_retry`, `retry_carries_original_idempotency_key`,
  `client_timeout_shorter_than_gateway_timeout` (the classic orphaned-authorisation bug);
  `expected disposition` ← `RESOLVED_BY_STATUS_ENQUIRY` / `VIOLATION(blind_retry)` /
  `VIOLATION(client_timeout_below_gateway_budget)`.

---

## H. Licence summary table

| # | Source | Licence (verified how) | Volume | Ground truth | Verdict |
|---|---|---|---|---|---|
| A1 | IBM/Cowlishaw `decTest` | IBM copyright, "reproduced with permission", **no OSI grant** (file headers + speleotrove page + CPython `Doc/license.rst` has no entry) | 143 files, 67,060 cases, 4.4 MB | yes (result + flags) | **REFERENCE-ONLY** |
| A2 | `rust_decimal` `tests/generated` | **MIT** (`LICENSE`) | 316 CSV, 3,430,315 rows, 251 MB | yes (result + error class) | **VENDOR** |
| A3 | Berkeley TestFloat | **BSD-3-Clause** (project docs, quoted) | generator, unbounded | yes (result + 5 exception flags) | **VENDOR** |
| A4 | JSR-354 TCK | **Apache-2.0** (`LICENSE.txt` + file headers) | 246 `@Test`, 245 `@SpecAssertion`, 17 sections | yes | **VENDOR** |
| A5a | joda-money | **Apache-2.0** (`LICENSE.txt`) | 995 `@Test`, no data files | yes (in-code) | VENDOR (low yield) |
| A5b | dinero.js | **MIT** (`LICENSE`) | — | — | REFERENCE |
| A5c | libmpdec | **BSD-2-Clause** (CPython `Doc/license.rst`) | — | — | VENDOR (code) |
| A5d | GCC libdecnumber | **GPLv3+ with GCC Runtime Library Exception 3.1** (file header) | — | — | REFERENCE |
| B1 | CLDR `currencyData` | **Unicode License v3** (repo `LICENSE`: "All other content in this repo is released under UNICODE LICENSE V3") | 76 currency entries, 53 non-default, 266 regions | yes | **VENDOR** |
| B2 | ISO 4217 (SIX) | **NOT ESTABLISHED** — "free of charge", no terms published | ~180 currencies | yes | **DO NOT VENDOR** |
| C1 | PostgreSQL `src/test/isolation` | **PostgreSQL Licence** (`COPYRIGHT`) | 134 specs, 143 `.out`, 2,768 permutations, 1,779 serialization-failure assertions | yes (byte-exact) | **VENDOR** |
| C2 | Hermitage | **CC BY 4.0** (`README.md`) | 25 configs × 10 anomalies = 250 verdicts | yes (matrix) | **VENDOR (attrib.)** |
| C3 | Elle | **EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0** (`project.clj` + `LICENSE`) | 33 models, ~68 anomalies, 18 Isabelle theories, 51 MB histories | yes (executable oracle) | **VENDOR (EPL-aware)** |
| C4 | `jepsen.history.sim` | **EPL-2.0 OR GPL-2.0-or-later WITH CP-exception** (`project.clj`) | 4 CC models, unbounded output | yes by construction | **VENDOR** |
| C5a | Jepsen framework | **EPL** (`jepsen/project.clj`) | — | — | VENDOR |
| C5b | `jepsen-io/tigerbeetle` | **EPL-2.0** (`LICENSE`) | 5,190 lines; `model.clj` 1,691 | yes (state-machine model) | **VENDOR** |
| C5c | jepsen.io analyses (prose) | **"Copyright © Jepsen, LLC"**, no grant | — | — | **REFERENCE-ONLY** |
| C6 | TPC-C Clause 3.3 | **Free download; verbatim copy permitted with TPC notice** (title-page notice, quoted). Benchmark use under Fair Use Policies + EULA. §3.3.2 contents **UNVERIFIED** | — | yes | **REFERENCE (quotable)** |
| C7 | pgjdbc | **BSD-2-Clause** (`LICENSE`) | — | — | VENDOR (low yield) |
| D1 | IETF Idempotency-Key draft | IETF Trust; **draft-07 EXPIRED, rev 2025-10-15, not an RFC** | — | — | **REFERENCE-ONLY** |
| D2 | Stripe idempotency docs | no licence grant | — | prose | **REFERENCE-ONLY** |
| D3 | Adyen idempotency docs | no licence grant | — | prose | **REFERENCE-ONLY** |
| D5 | Kafka `transactions_test.py` | **Apache-2.0** (repo `LICENSE`) | ≥32 parametrised runs, 100k seed msgs | yes (set equality, zero dups) | **VENDOR** |
| E1 | TigerBeetle status enums | **Apache-2.0** (`LICENSE`) | **28 + 70 = 98 status codes** | yes (per-code disposition) | **VENDOR** |
| E3 | Formance Ledger | **MIT** (`LICENSE`) | — | — | VENDOR (reference) |
| E4a | hledger | **GPL-3.0** (`LICENSE`) | — | yes | **REFERENCE-ONLY** (copyleft) |
| E4b | Beancount | **GPL-2.0** (`COPYING`) | — | yes | **REFERENCE-ONLY** (copyleft) |
| F1 | 17 CFR 240.17a-4(f) | **US federal regulation — public domain** | 2 alternatives + ~9 conditions | n/a (it *is* the provision) | **VENDOR** |
| G1 | resilience4j | **Apache-2.0** (`LICENSE.txt`) | generic only | yes | VENDOR (no fin. variant) |
| G2 | Adyen POS timeout budgets | vendor docs, no grant | 15 named budgets | numeric | **REFERENCE-ONLY** |

---

## I. Recommended factor vocabulary

Names chosen to be (a) unambiguous, (b) boolean, (c) traceable to a verified source.

**Decimal precision** (sources: A1 flags, A2 `Error` column, B1)
`monetary_amount_held_in_binary_floating_point` ·
`arithmetic_result_inexact` · `arithmetic_result_rounded` ·
`arithmetic_result_overflows_representable_range` · `divisor_is_zero` ·
`operand_scale_exceeds_declared_precision` · `intermediate_precision_below_operand_precision` ·
`amount_scale_exceeds_currency_minor_units` · `currency_conversion_applied_before_rounding`

**Rounding mode** (sources: A1 `rounding:` directives, A2 `RoundingStrategy`, B1)
`rounding_mode_declared` · `rounding_mode_is_half_even` (bankers') · `rounding_mode_is_half_up` ·
`rounding_mode_is_half_down` · `rounding_mode_is_toward_zero` · `rounding_mode_is_away_from_zero` ·
`rounding_mode_is_ceiling` · `rounding_mode_is_floor` · `rounding_mode_is_half_even_05up` ·
`rounding_applied_at_currency_minor_unit` · `cash_rounding_increment_applied` ·
`rounding_applied_more_than_once_in_pipeline` (double-rounding) ·
`rounding_direction_favours_institution`

**Transaction atomicity** (sources: C1, E1, E2)
`operation_spans_multiple_ledger_writes` · `writes_committed_as_single_atomic_unit` ·
`linked_event_chain_left_open` · `partial_effect_observable_after_failure` ·
`compensating_transaction_required_on_failure` · `two_phase_pending_transfer_used` ·
`pending_transfer_expired_without_resolution`

**Isolation anomalies** — use the Adya/Hermitage names verbatim; they are the citable standard
(sources: C2, C3, C8)
`anomaly_G0_dirty_write` · `anomaly_G1a_aborted_read` · `anomaly_G1b_intermediate_read` ·
`anomaly_G1c_circular_information_flow` · `anomaly_OTV_observed_transaction_vanishes` ·
`anomaly_PMP_predicate_many_preceders` · `anomaly_P4_lost_update` ·
`anomaly_G_single_read_skew` · `anomaly_G2_item_write_skew` ·
`anomaly_G2_anti_dependency_cycle` · `anomaly_G_SI_snapshot_isolation_violation` ·
`anomaly_dirty_update` · `anomaly_cyclic_versions`
plus the declared-level factors:
`declared_isolation_read_uncommitted` · `declared_isolation_read_committed` ·
`declared_isolation_repeatable_read` · `declared_isolation_snapshot` ·
`declared_isolation_serializable` · `declared_isolation_strict_serializable` ·
`isolation_level_downgraded_by_change`

**Idempotency** (sources: D2, D3, D4)
`idempotency_key_accepted_on_mutating_request` · `idempotency_key_client_generated` ·
`idempotency_key_retention_window_declared` ·
`replay_returns_original_response_including_failure` ·
`replay_with_different_parameters_rejected` ·
`concurrent_request_with_same_key_rejected` ·
`replayed_response_labelled_as_replay` ·
`failed_outcome_is_permanently_remembered` (TigerBeetle `id_already_failed`) ·
`retry_issued_without_idempotency_key` · `idempotency_key_reused_across_distinct_operations` ·
`idempotency_key_derived_from_sensitive_data`

**Double-spend prevention** (sources: E1, C1, C2)
`concurrent_debits_against_same_account` ·
`balance_check_and_debit_not_atomic` (check-then-act) ·
`debit_would_make_debits_exceed_credits` (→ `REJECT(exceeds_credits)`) ·
`credit_would_make_credits_exceed_debits` (→ `REJECT(exceeds_debits)`) ·
`overdraft_permitted_by_account_flag` · `account_closed_at_time_of_posting` ·
`balance_read_from_stale_snapshot` · `write_skew_across_two_accounts` ·
`aggregate_balance_denormalised_without_serialisation`

**Ledger immutability** (sources: E1 `imported_event_*`, E4 invariants, F1)
`ledger_entries_immutable_after_commit` · `correction_recorded_as_reversing_entry` ·
`existing_entry_updated_in_place` · `existing_entry_deleted` ·
`entry_timestamps_monotonic_non_regressing` · `backdated_entry_predates_account_creation` ·
`postings_of_transaction_sum_to_zero` (double-entry) ·
`declared_balance_assertion_reconciles_with_computed_balance` ·
`records_stored_non_rewriteable_non_erasable` (17a-4(f)(2)(i)(B)) ·
`complete_time_stamped_audit_trail_maintained` (17a-4(f)(2)(i)(A)) ·
`modifying_actor_identity_recorded` · `duplicate_storage_media_serialised` ·
`records_downloadable_in_human_readable_form` · `redundant_backup_system_present`

**Exactly-once delivery** (source: D5)
`duplicate_message_emitted` · `message_lost` · `ordering_preserved_within_partition` ·
`producer_crashed_mid_transaction` · `broker_hard_bounced` · `consumer_group_rebalanced` ·
`consumer_offsets_committed_in_same_transaction`

**Resilience on payment paths** (sources: G1, G2)
`elapsed_exceeds_gateway_processing_timeout` ·
`client_timeout_shorter_than_gateway_timeout` ·
`status_enquiry_issued_before_retry` · `retry_carries_original_idempotency_key` ·
`circuit_breaker_present_on_payment_dependency` ·
`fallback_path_can_double_post`

---

## J. Gaps found (candidates for original contribution)

1. **No open corpus for idempotency-key semantics.** Stripe and Adyen document incompatible
   retention windows (24 h vs 7–14 days) and different conflict codes (409 vs 422/704); the IETF
   draft has expired. TigerBeetle's `exists_with_different_*` enum is the only machine-readable
   artefact. A small, licence-clean idempotency corpus would be genuinely new.
2. **No open conformance suite for event-sourcing immutability or compensating transactions.**
3. **No open benchmark for simultaneous debits on a single account** as such — it has to be
   composed from PostgreSQL specs + Hermitage verdicts + TigerBeetle dispositions.
4. **No financial variant of resilience4j/Polly**, and no vendor publishes an end-to-end payment
   timeout *budget* (Adyen publishes device and processing timeouts; Stripe publishes none).
5. **The decTest licence problem is unsolved industry-wide** — the reference corpus for decimal
   money arithmetic has no redistribution grant, and every downstream project vendors it anyway.
   A cleanroom, permissively-licensed decimal corpus (generated and cross-validated against
   decNumber, mpdecimal and rust_decimal) would be a real contribution. `rust_decimal`'s
   3.43 M-row MIT tables are the closest existing substitute.
