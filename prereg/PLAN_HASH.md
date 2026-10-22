# Plan hash

**Plan hash (sha256):** `67bb2bb5ed17dcc2e3505ddb9c95027a2e9aefc38c15b118df5afdb0141c0e6f`

| | |
|---|---|
| Computed | 2026-10-22 20:39 UTC |
| Package VERSION | 5.16.0 |
| Git branch | realism |
| Git commit at computation | 8a8f9f00cc318e4249bc572046e348796dc239c1 (informational; not a hash input) |
| Files | 41 |

Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines `<path>  <digest>\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning `| OSF registration DOI |` is removed before that file is digested. `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. Recompute with `python3 prereg/make_plan_hash.py --check`.

## Preregistration files

| File | sha256 |
|---|---|
| `prereg/ANALYSIS_PLAN.md` | `ea46d2fa51392aa8054e75a5997c1ef81feb05c20c6bad5499f3b48ed74b4179` |
| `prereg/DATA_DICTIONARY.md` | `f9335d6b21acbcb8e6cc2c87e2ba07a1ae5c591c8a6ca4ba9a5cc33d3d6ba372` |
| `prereg/ESTIMAND_MAP.md` | `07875215ca675459123ba3a246a0b4586fddf9fc1385e0b9fdb2ac8105c68978` |
| `prereg/OSF_UPLOAD_CHECKLIST.md` | `afb2f54f4e9a78765ef090cffdacaf6f18d493b532021a6ca954078cfeed72c9` |
| `prereg/POLICY_REGISTER.md` | `b0505332a047967339b7f83b8b46a402c1dbd24a6a9cae3d2fa28b9b58f3a0f2` |
| `prereg/PREREG_EC_SIM_v1.md` | `497bd3638243b7b70c272d7c397af85730fb1d7bb018fb4ee1b126d6e0216ff6` |
| `prereg/REALISM_REVIEW.md` | `484b624bd0ba45e958fe8ca6bd1b29735a9a6901bfa3ae46755c86b3cfdde3cc` |
| `prereg/make_plan_hash.py` | `44a5c1bad33a1c6a20d4c1c9e4bdf82ca797d9a0e731bdff3a630501c4003b2f` |

## Canons

| File | sha256 |
|---|---|
| `simulation/dcvigil-constitution-corpus/constitution/canon.json` | `d2c0747cf3e010c6a5d14fe3cf6fcb33a40611e96301ed8d3fd30e854abc949d` |
| `simulation/frontierllm-constitution-corpus/constitution/canon.json` | `a87ebfbc486da064cd1b91d80e9c3b96425eb0af09b5cccc44e16ad9cea2f620` |
| `simulation/meridian-corpus/constitution/canon.json` | `0f88dcb1493dd966767fa243d480941861a64c2ed1d1edb151038486bddf1761` |
| `simulation/semifab-constitution-corpus/constitution/canon.json` | `47305fa1af4604a5e331f4984eae1ecc2cf08388655982de38d80efcdabaff8a` |
| `simulation/vetpoc-constitution-corpus/constitution/canon.json` | `8d674e1784a44929c52f4d1492e5ad7b7f60ea7988cd5ebe64a792d659183535` |

## simulation/ec package

| File | sha256 |
|---|---|
| `simulation/ec/COMPANY_PROFILES.md` | `018270e552d5805aaf1c4057b0f84048aa3f9c10c2bbd44e4eec3737734efd11` |
| `simulation/ec/DESIGN.md` | `c865820e7237ffd9b991b1e6f0ab1401f0d39beb9ec1a5c685dc7944cbc6aa6c` |
| `simulation/ec/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `simulation/ec/agents/__init__.py` | `b03e02b5f73e25ef26940edf70e6e5413ecec2119afd199b94d3c8a3e8d4af04` |
| `simulation/ec/agents/llm.py` | `c6f6dc198d23338f1f0ab94db2ea27053100357f7e7106caa5cce9570956c513` |
| `simulation/ec/agents/policy.py` | `fad6a3faed82c0bb2691277bf37c851d806bbc2e7b481e01e8f42b766afda6fb` |
| `simulation/ec/analyze.py` | `35437414ea22154b8bd857735339cfe497c08891d0e9a943353a8e2be3512d10` |
| `simulation/ec/authority.py` | `70851223fb667347e334b6c6c5d118f8b72f704a7989c5a5bf51fa35bc940e21` |
| `simulation/ec/build_all_canons.py` | `214a8849fb5a15a91df0890cd6fb5f7cce82352565cd27ec92f5a6d42242ed77` |
| `simulation/ec/build_policy_register.py` | `60c65446775b2a19ee11c9087ad1a0e122d6403650ebf0c942a1ab0334bc5679` |
| `simulation/ec/calendar.py` | `9d0e86a1a1f25efc2d1ceb4bb5b84fd9a8edab7e41484683ef498660b87f2958` |
| `simulation/ec/canon.py` | `4a67d18fd9e9af0e121878bf18bf38036586435b2d3c9940717d569a8ec52c2a` |
| `simulation/ec/doctrine.py` | `91c9715c2012a6e325a49b93910ff32f88b0eef4bf5d7c0cb124541f64662b0e` |
| `simulation/ec/escalate.py` | `072fafd8af9b00ae95fab66f6b4ab4cb2b44f614bb2284f43b92558011089ea3` |
| `simulation/ec/examen.py` | `d0669f6c8db1495d66e838513acc7b24fc1774433e523d87c4b9adb6ba56b730` |
| `simulation/ec/gate.py` | `b9423307f350d53675284f94d93e4af42c61fa194005049fdec90c0764728c5b` |
| `simulation/ec/metrics.py` | `06164d0a6970984a3b05d16ece6ce372085b7ea59eeebeadef0ac27e5a5eb89b` |
| `simulation/ec/mutation_matrix_ec.py` | `9f6944e5b1df9017f03e9ba2d31525070dc67fa540ef05b720a8559003e79f5e` |
| `simulation/ec/registry.py` | `3627828dee8d0c53d5520d98934589e40acee9e5a3cccb2e0eb68aea33a6441e` |
| `simulation/ec/rival.py` | `b74c90be858103cb72bf49a26a998a20f1cf02c3cf066a9f55f49ae759cb7a84` |
| `simulation/ec/rulebook_rev.py` | `83ae13d2b70c119b5eb76c8255f3c32bbba80c5d7b0383d13779df2609673887` |
| `simulation/ec/run_ec_conformance.py` | `262fa540b4b43a5eaa2e4e2b11a52ebdf110f1678388916a546acbe0067aa195` |
| `simulation/ec/run_year.py` | `39f95da97540706d9211ad9842237de545f5aced5ca9bf2b488e86512d441641` |
| `simulation/ec/stream.py` | `24621e5a72eb749791102fed2ec6b78935e3d037efac8c426e74669937a91468` |

## EC tests

| File | sha256 |
|---|---|
| `tests/test_ec_conformance.py` | `b9543553e424aeaa7316d6dfbe742b3f5de3e45452c880e0ab33c67a8ce75ac4` |
| `tests/test_ec_core.py` | `78ca8a51bab0ca9a69d3d416c31451082a2b63e61cfe77d265a8704b91bcb777` |
| `tests/test_ec_driver.py` | `ac5013a83951ce7b2746e26d2456ea73c3e637d9d393226178c00d6c2d601153` |
| `tests/test_ec_llm_live.py` | `d7022f854ead2a5673f51ba8bfd9509e0325fdec2493420f360c5ba41f42ebb1` |

## Amendments

None. A post-freeze change to any file above is recorded here with its reason, the previous hash and the new hash, and posted to the OSF registration as an update before any further registered run.
