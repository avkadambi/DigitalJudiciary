# Plan hash

**Plan hash (sha256):** `68bc9b2b4db5ab654341cccb30c63229378dc1c7984eb7ce932042f17f9c3f9c`

| | |
|---|---|
| Computed | 2026-10-22 03:52 UTC |
| Package VERSION | 5.16.0 |
| Git branch | work |
| Git commit at computation | ebf776c4a0a0e11e3ee032456a292f4e9e6fef88 (informational; not a hash input) |
| Files | 35 |

Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines `<path>  <digest>\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning `| OSF registration DOI |` is removed before that file is digested. `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. Recompute with `python3 prereg/make_plan_hash.py --check`.

## Preregistration files

| File | sha256 |
|---|---|
| `prereg/ANALYSIS_PLAN.md` | `a6bdf61ad607da1844dc93ef66b392e42dae77788e147538eddbb43c55084f78` |
| `prereg/DATA_DICTIONARY.md` | `1f3df19b735cb98b70feeb1045c1d4794fff44e9171f7d4c871fb851e11f8819` |
| `prereg/ESTIMAND_MAP.md` | `07875215ca675459123ba3a246a0b4586fddf9fc1385e0b9fdb2ac8105c68978` |
| `prereg/OSF_UPLOAD_CHECKLIST.md` | `0fb2e43cfda1380342af3547b301e3a16ecaebb0a5abd596d063ad48279190ec` |
| `prereg/PREREG_EC_SIM_v1.md` | `99280eb93f00ebae1212c2fc369067de40d86c4ea924cdaacde282023d957636` |
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
| `simulation/ec/agents/llm.py` | `20e28285aa7f652348502012bd99435b41ed60839c1e915abf9acf1adb903095` |
| `simulation/ec/agents/policy.py` | `dc07377b5240f81a69f07be2a62eee53707d95f959dd4d7cff0858ee35f9a6a4` |
| `simulation/ec/analyze.py` | `35437414ea22154b8bd857735339cfe497c08891d0e9a943353a8e2be3512d10` |
| `simulation/ec/build_all_canons.py` | `214a8849fb5a15a91df0890cd6fb5f7cce82352565cd27ec92f5a6d42242ed77` |
| `simulation/ec/calendar.py` | `d67f8ed92eb3553ab913440892a6cd293961b266db7eefd840510ea70f3f8a0d` |
| `simulation/ec/canon.py` | `6ea25de5ecf1a55fa32736b96f19df29c7c9e38a7ce6da83a395ed2866268af3` |
| `simulation/ec/doctrine.py` | `91c9715c2012a6e325a49b93910ff32f88b0eef4bf5d7c0cb124541f64662b0e` |
| `simulation/ec/escalate.py` | `c94286cdecfe5e7baf15aaa7da1310e88d0fafcb62ea85c95f7a913f830bd4e7` |
| `simulation/ec/examen.py` | `d0669f6c8db1495d66e838513acc7b24fc1774433e523d87c4b9adb6ba56b730` |
| `simulation/ec/gate.py` | `f9bf3b9660afc622bb0cfe7dd9deefd339bcc9b13898029fc8fc22869b317581` |
| `simulation/ec/metrics.py` | `12ac0d2cc07d6254cc0de0131189bb6c7606777c169f58745272798f16b6bace` |
| `simulation/ec/mutation_matrix_ec.py` | `a7b77d737fbd6c359b4559a61e94d7ef99fa4d6fc6a61a06374be79888629f3c` |
| `simulation/ec/registry.py` | `a2b395007b1c2a2a335b74f3406e537efe68d0c00d56ba4abdc6cf9ef6f0d880` |
| `simulation/ec/rival.py` | `75307b0366cd2a318a71412c51255c07b52cf26d21615e1ba6fc3da40e200472` |
| `simulation/ec/run_ec_conformance.py` | `02701fb6d363a874718b9932a5636036830f42b57ea708995ae6bf5359c4b72c` |
| `simulation/ec/run_year.py` | `5d1690fb121184b9c08578fa702f7d72d01fca17d68cd44731de331f845876b6` |
| `simulation/ec/stream.py` | `24e462e612872548dd0f14f8c0011bfa2c3be98b4fa5af01bdbe98ae17607a5f` |

## EC tests

| File | sha256 |
|---|---|
| `tests/test_ec_conformance.py` | `095aa63bd1ca6cb870e195f5c6bb0bbd3ca2475bf9fe72ee16cdeedb8325974f` |
| `tests/test_ec_core.py` | `ea7272896d6e8886a3855cf0867cf66198c7eb92b0d07a2039e5d16101a58980` |
| `tests/test_ec_driver.py` | `32a4d730ddba7c0440e291327d175ad6711ebadee9f7b56e9ed6c5e4dc477329` |
| `tests/test_ec_llm_live.py` | `a2bae95a589231372a243ba3add366e594843e3df670917817fb00b627298a59` |

## Amendments

None. A post-freeze change to any file above is recorded here with its reason, the previous hash and the new hash, and posted to the OSF registration as an update before any further registered run.
