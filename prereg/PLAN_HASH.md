# Plan hash

**Plan hash (sha256):** `5118699e061d06f8388a42b50bfb30c43fab0d9be5242bc7d6bc57263aea4acb`

| | |
|---|---|
| Computed | 2026-10-22 03:21 UTC |
| Package VERSION | 5.16.0 |
| Git branch | HEAD |
| Git commit at computation | a9bd0882973675405f643d09c92d2cc2d49d41b4 (informational; not a hash input) |
| Files | 35 |

Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines `<path>  <digest>\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning `| OSF registration DOI |` is removed before that file is digested. `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. Recompute with `python3 prereg/make_plan_hash.py --check`.

## Preregistration files

| File | sha256 |
|---|---|
| `prereg/ANALYSIS_PLAN.md` | `bcbcefb842b09db2bdd6e0a551246ae57dffc62d394010f533d90d357a1270ec` |
| `prereg/DATA_DICTIONARY.md` | `7fcc421f30536c216fd6f35c29fbc370e0b3181f3d9eafb5cda5d38770f0709f` |
| `prereg/ESTIMAND_MAP.md` | `07875215ca675459123ba3a246a0b4586fddf9fc1385e0b9fdb2ac8105c68978` |
| `prereg/OSF_UPLOAD_CHECKLIST.md` | `0fb2e43cfda1380342af3547b301e3a16ecaebb0a5abd596d063ad48279190ec` |
| `prereg/PREREG_EC_SIM_v1.md` | `af7df98d3449f818042a32f5c8cb00226c3c59d443fb15fb61abd864a63d952c` |
| `prereg/make_plan_hash.py` | `44a5c1bad33a1c6a20d4c1c9e4bdf82ca797d9a0e731bdff3a630501c4003b2f` |

## Canons

| File | sha256 |
|---|---|
| `simulation/dcvigil-constitution-corpus/constitution/canon.json` | `5dd9676c6c8065e3cf1cec8cfb2601517bdfde13221f4c24513ec45b3c138bdb` |
| `simulation/frontierllm-constitution-corpus/constitution/canon.json` | `ed324358170c35f9441a8d346f70d1055b43e3781460bb797ed6c672700b42f1` |
| `simulation/meridian-corpus/constitution/canon.json` | `ab9d5132fda2162548a0b8341d6263060a1621a68ecae04a1d17b012d9baaff1` |
| `simulation/semifab-constitution-corpus/constitution/canon.json` | `7db8c57b5d08e5b9181f8cade7df960fa41fe80013b6e9d957264d5c73205989` |
| `simulation/vetpoc-constitution-corpus/constitution/canon.json` | `70c11fe859ee214009cbd4c7232439e4c5337bad6a647a61638e1f95cd26541f` |

## simulation/ec package

| File | sha256 |
|---|---|
| `simulation/ec/DESIGN.md` | `7ef6519cc9953d9aa5803d89196dca888e1de782299bf70c53e015f583ede4fd` |
| `simulation/ec/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `simulation/ec/agents/__init__.py` | `b03e02b5f73e25ef26940edf70e6e5413ecec2119afd199b94d3c8a3e8d4af04` |
| `simulation/ec/agents/llm.py` | `fd183cbbadb106f21fba64047d336eb5c3495e94a9faa6f80e5976cde7c6a3da` |
| `simulation/ec/agents/policy.py` | `dc07377b5240f81a69f07be2a62eee53707d95f959dd4d7cff0858ee35f9a6a4` |
| `simulation/ec/analyze.py` | `35437414ea22154b8bd857735339cfe497c08891d0e9a943353a8e2be3512d10` |
| `simulation/ec/build_all_canons.py` | `214a8849fb5a15a91df0890cd6fb5f7cce82352565cd27ec92f5a6d42242ed77` |
| `simulation/ec/calendar.py` | `d67f8ed92eb3553ab913440892a6cd293961b266db7eefd840510ea70f3f8a0d` |
| `simulation/ec/canon.py` | `6ea25de5ecf1a55fa32736b96f19df29c7c9e38a7ce6da83a395ed2866268af3` |
| `simulation/ec/doctrine.py` | `91c9715c2012a6e325a49b93910ff32f88b0eef4bf5d7c0cb124541f64662b0e` |
| `simulation/ec/escalate.py` | `f732f092fc5da077fa2bd072fd77a649420cf91647c9b72dfb343fbf0715b1b0` |
| `simulation/ec/examen.py` | `d0669f6c8db1495d66e838513acc7b24fc1774433e523d87c4b9adb6ba56b730` |
| `simulation/ec/gate.py` | `c77cb62920eeb9374dd8c070dd7b8f84584b1e2399de0117d2067a4986c44e2d` |
| `simulation/ec/metrics.py` | `8c4eea2c03c564ca056bc0400db6acf3f1e0236511a6a7780bb18db11e848ff6` |
| `simulation/ec/mutation_matrix_ec.py` | `a7b77d737fbd6c359b4559a61e94d7ef99fa4d6fc6a61a06374be79888629f3c` |
| `simulation/ec/registry.py` | `a2b395007b1c2a2a335b74f3406e537efe68d0c00d56ba4abdc6cf9ef6f0d880` |
| `simulation/ec/rival.py` | `6ecc43bcba6f64f0460344bd12645d1dff30a95f5d3c78ffe1c66fbddc610fdb` |
| `simulation/ec/run_ec_conformance.py` | `02701fb6d363a874718b9932a5636036830f42b57ea708995ae6bf5359c4b72c` |
| `simulation/ec/run_year.py` | `900c179f28e25e1f789e230e81bdc4bc25569d579f89c9948210eee8a83a5576` |
| `simulation/ec/stream.py` | `24e462e612872548dd0f14f8c0011bfa2c3be98b4fa5af01bdbe98ae17607a5f` |

## EC tests

| File | sha256 |
|---|---|
| `tests/test_ec_conformance.py` | `095aa63bd1ca6cb870e195f5c6bb0bbd3ca2475bf9fe72ee16cdeedb8325974f` |
| `tests/test_ec_core.py` | `7dc083077ae9bdefad7d78b8d62e7e6ac7ca5ce6e794e61547baaa6656c2f8d5` |
| `tests/test_ec_driver.py` | `79d0dd63c068853efb9ffa7e5740de11b15853ba713df758a927c7b1fd04f2e3` |
| `tests/test_ec_llm_live.py` | `1659a970d252ce3348987f205e2eec030e1c352d638376118c7d92540d2ae810` |

## Amendments

None. A post-freeze change to any file above is recorded here with its reason, the previous hash and the new hash, and posted to the OSF registration as an update before any further registered run.
