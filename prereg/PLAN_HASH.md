# Plan hash

**Plan hash (sha256):** `4205dc894dd5c4a3cb594e9c3e852e40749de1f088f6dae3143263e4b02dc4e5`

| | |
|---|---|
| Computed | 2026-10-20 20:30 UTC |
| Package VERSION | 5.16.0 |
| Git branch | ec-fast-track |
| Git commit at computation | 710b7339525d5129ad33dd8d0ca0cbc5ab62cf09 (informational; not a hash input) |
| Files | 34 |

Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines `<path>  <digest>\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning `| OSF registration DOI |` is removed before that file is digested. `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. Recompute with `python3 prereg/make_plan_hash.py --check`.

## Preregistration files

| File | sha256 |
|---|---|
| `prereg/ANALYSIS_PLAN.md` | `bcbcefb842b09db2bdd6e0a551246ae57dffc62d394010f533d90d357a1270ec` |
| `prereg/DATA_DICTIONARY.md` | `cc0e30cc26b04138fb910e1754c41b4ac5202b9593a42002c087b273e381d8b3` |
| `prereg/ESTIMAND_MAP.md` | `07875215ca675459123ba3a246a0b4586fddf9fc1385e0b9fdb2ac8105c68978` |
| `prereg/OSF_UPLOAD_CHECKLIST.md` | `1f609ae6aa792fb8bb76d1c1d1a012fad49de4eb71719b345c8f78d83cb4e7ac` |
| `prereg/PREREG_EC_SIM_v1.md` | `8c2ad0fc33bd97699a5e06dd900c3201932b8df53dfe557249481a2d6cb91a5f` |
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
| `simulation/ec/DESIGN.md` | `6ce4f3e18095edd398e7198b3b19639967de617c6f85b3d0b336eb15502da2d9` |
| `simulation/ec/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `simulation/ec/agents/__init__.py` | `46e82bca04ea9753f62d029d62223245d76fc0f7f1da359a2cd3f92b0daf1e20` |
| `simulation/ec/agents/llm.py` | `5ffbfc3d3d73b436dd6585006d2456d3d9a6c31da2413e1edcc6fa50c92d5a8d` |
| `simulation/ec/agents/policy.py` | `dc07377b5240f81a69f07be2a62eee53707d95f959dd4d7cff0858ee35f9a6a4` |
| `simulation/ec/analyze.py` | `35437414ea22154b8bd857735339cfe497c08891d0e9a943353a8e2be3512d10` |
| `simulation/ec/build_all_canons.py` | `214a8849fb5a15a91df0890cd6fb5f7cce82352565cd27ec92f5a6d42242ed77` |
| `simulation/ec/calendar.py` | `4d2008f3cb5ee6d80a33b73b3927b3c1122cc69a752d5181dd16ec310541fdd3` |
| `simulation/ec/canon.py` | `6ea25de5ecf1a55fa32736b96f19df29c7c9e38a7ce6da83a395ed2866268af3` |
| `simulation/ec/doctrine.py` | `91c9715c2012a6e325a49b93910ff32f88b0eef4bf5d7c0cb124541f64662b0e` |
| `simulation/ec/escalate.py` | `f732f092fc5da077fa2bd072fd77a649420cf91647c9b72dfb343fbf0715b1b0` |
| `simulation/ec/examen.py` | `d0669f6c8db1495d66e838513acc7b24fc1774433e523d87c4b9adb6ba56b730` |
| `simulation/ec/gate.py` | `c77cb62920eeb9374dd8c070dd7b8f84584b1e2399de0117d2067a4986c44e2d` |
| `simulation/ec/metrics.py` | `329d65865539fa6d04424210d4134fb4b8767f2f2e433dfb7d80e7c747818424` |
| `simulation/ec/mutation_matrix_ec.py` | `a7b77d737fbd6c359b4559a61e94d7ef99fa4d6fc6a61a06374be79888629f3c` |
| `simulation/ec/registry.py` | `a2b395007b1c2a2a335b74f3406e537efe68d0c00d56ba4abdc6cf9ef6f0d880` |
| `simulation/ec/rival.py` | `6ecc43bcba6f64f0460344bd12645d1dff30a95f5d3c78ffe1c66fbddc610fdb` |
| `simulation/ec/run_ec_conformance.py` | `02701fb6d363a874718b9932a5636036830f42b57ea708995ae6bf5359c4b72c` |
| `simulation/ec/run_year.py` | `d16404f2bd75dc34aabf1bfabc5495e6330c0edf884d605d58505765d4fccfcf` |
| `simulation/ec/stream.py` | `24e462e612872548dd0f14f8c0011bfa2c3be98b4fa5af01bdbe98ae17607a5f` |

## EC tests

| File | sha256 |
|---|---|
| `tests/test_ec_conformance.py` | `095aa63bd1ca6cb870e195f5c6bb0bbd3ca2475bf9fe72ee16cdeedb8325974f` |
| `tests/test_ec_core.py` | `7dc083077ae9bdefad7d78b8d62e7e6ac7ca5ce6e794e61547baaa6656c2f8d5` |
| `tests/test_ec_driver.py` | `11c50a5406fc8607fa728782b9b90cafc74dbc2761deddf66fa8a0c2879dbc41` |

## Amendments

None. A post-freeze change to any file above is recorded here with its reason, the previous hash and the new hash, and posted to the OSF registration as an update before any further registered run.
