# Plan hash

**Plan hash (sha256):** `214e0424b2a2b7a4f0cb3763daddc61da35e68db824801281f9ab6988e177d7c`

| | |
|---|---|
| Computed | 2026-10-22 15:09 UTC |
| Package VERSION | 5.16.0 |
| Git branch | realism |
| Git commit at computation | a177dd039f29debcd22e2a5bf0a42d49ae5fbefa (informational; not a hash input) |
| Files | 37 |

Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines `<path>  <digest>\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning `| OSF registration DOI |` is removed before that file is digested. `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. Recompute with `python3 prereg/make_plan_hash.py --check`.

## Preregistration files

| File | sha256 |
|---|---|
| `prereg/ANALYSIS_PLAN.md` | `76d1a4feafdc44aef7044a9e8d9f8a504ad0dbadcc444442f4c0d8bd9cd83069` |
| `prereg/DATA_DICTIONARY.md` | `151c7b34bbf2c0c725cc1b91a10952a06db3265c73892504a1b1e61536ce27d7` |
| `prereg/ESTIMAND_MAP.md` | `07875215ca675459123ba3a246a0b4586fddf9fc1385e0b9fdb2ac8105c68978` |
| `prereg/OSF_UPLOAD_CHECKLIST.md` | `25d49e6e176a14bf254346b7fb590ea5fa8147470cc61975a478996c03d198a6` |
| `prereg/PREREG_EC_SIM_v1.md` | `389e2ca40862f1f79cd59c4fd053d2c66d26ed676552a4be622e67f065b9c836` |
| `prereg/REALISM_REVIEW.md` | `39cdec4f93c9f3d95b0a71ddc808cfa1434f599caa4bdd5cebe42804efa48cff` |
| `prereg/make_plan_hash.py` | `44a5c1bad33a1c6a20d4c1c9e4bdf82ca797d9a0e731bdff3a630501c4003b2f` |

## Canons

| File | sha256 |
|---|---|
| `simulation/dcvigil-constitution-corpus/constitution/canon.json` | `ced4b5637e08c661d4c712983a81f653a857cdf85c06763af66b4b1ad37802ab` |
| `simulation/frontierllm-constitution-corpus/constitution/canon.json` | `7bb8e3274d0a845a35b484270244162b2b349ed765450f67caa55fc5b8d4e25b` |
| `simulation/meridian-corpus/constitution/canon.json` | `ab9d5132fda2162548a0b8341d6263060a1621a68ecae04a1d17b012d9baaff1` |
| `simulation/semifab-constitution-corpus/constitution/canon.json` | `2c135a47e3a3a61c985bdb81ec3ba7647a4bf56153ef2500b5aa895d382097fc` |
| `simulation/vetpoc-constitution-corpus/constitution/canon.json` | `70c11fe859ee214009cbd4c7232439e4c5337bad6a647a61638e1f95cd26541f` |

## simulation/ec package

| File | sha256 |
|---|---|
| `simulation/ec/DESIGN.md` | `6c3e591a8ca1a6216188d4e54a4040f48885b71f7cd8a50fbfe86f30710ce179` |
| `simulation/ec/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `simulation/ec/agents/__init__.py` | `b03e02b5f73e25ef26940edf70e6e5413ecec2119afd199b94d3c8a3e8d4af04` |
| `simulation/ec/agents/llm.py` | `1d6136228c8ef11dd0fef3ce1a7c38043f1e738ee9b36ff62b3716486139f20a` |
| `simulation/ec/agents/policy.py` | `c3a75fddb0b22db35153efb0764990fffd540912aa720fd86340949dd9ee484c` |
| `simulation/ec/analyze.py` | `35437414ea22154b8bd857735339cfe497c08891d0e9a943353a8e2be3512d10` |
| `simulation/ec/build_all_canons.py` | `214a8849fb5a15a91df0890cd6fb5f7cce82352565cd27ec92f5a6d42242ed77` |
| `simulation/ec/calendar.py` | `a8285839e0d6fd4d7fc1d4018e39f910756406798853c8197e516ae843dcae55` |
| `simulation/ec/canon.py` | `382c123f021882225b97318fa9cd7a3336648cd248ad55f21fe793f4fe1a5083` |
| `simulation/ec/doctrine.py` | `91c9715c2012a6e325a49b93910ff32f88b0eef4bf5d7c0cb124541f64662b0e` |
| `simulation/ec/escalate.py` | `24ebc1a0947cfcc43d569ed83e30ceda81d1364fb046ad6527167cf9692bdc18` |
| `simulation/ec/examen.py` | `d0669f6c8db1495d66e838513acc7b24fc1774433e523d87c4b9adb6ba56b730` |
| `simulation/ec/gate.py` | `550b8b45ac3bb301cd2121be19c42983e602c3712b706fd96c58cf6f5e0690a0` |
| `simulation/ec/metrics.py` | `c0f17d7f957f932864535f7131e86469eb769397f41ae112563dc9f42fbc3b8e` |
| `simulation/ec/mutation_matrix_ec.py` | `88cae170c7a2b04ba5a224565d09a3288b8adc432fb2ec06b0ca56658b71e15d` |
| `simulation/ec/registry.py` | `4a7b471c911baec5d8160d12eb76fdf45f5d40faaa9ba42a66ee37a11e163da7` |
| `simulation/ec/rival.py` | `d9347c44f47e402a15db3d793ec537c51aca288040d4963fa45d93ffa2bdff68` |
| `simulation/ec/rulebook_rev.py` | `f42f06eaeddfd0d89262f6c8397f65b11c44b978dde3d4bcd2a2d8f895053a8f` |
| `simulation/ec/run_ec_conformance.py` | `7e4832e06e014b3eb8734c895fa010b269af629389937c1a429accd9eec5a19f` |
| `simulation/ec/run_year.py` | `90a058eee4d2eedb2e6c7f9dac7af4ac88c57fe654a6259292f0d94be92efec4` |
| `simulation/ec/stream.py` | `c286e5e9339e889ceb8c4dde4a2a06f8bfb9fee2e6ad324547ca3cc89d86a0b1` |

## EC tests

| File | sha256 |
|---|---|
| `tests/test_ec_conformance.py` | `84ed589b3e5b52f1c3d5826c0df4a8b98c4c4eb365a4b01c930cbe59a0dcfc47` |
| `tests/test_ec_core.py` | `39dabc41607069f05e6c94db155bd9edaf810df4c8ebe1d70d0a93462a9b2ed1` |
| `tests/test_ec_driver.py` | `0ccdfe4ceb7c39bb7bb5d8671448200edff30eb1d7ee2f6813b89570e3dd0163` |
| `tests/test_ec_llm_live.py` | `c496346a6b837a287977d4e88d9784e0c1f5c8c97d6753da584badf440e4fa91` |

## Amendments

None. A post-freeze change to any file above is recorded here with its reason, the previous hash and the new hash, and posted to the OSF registration as an update before any further registered run.
