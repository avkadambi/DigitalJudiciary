# OSF upload checklist

Exact steps to register this study on the Open Science Framework. Do them in order; each step names the file it uses. The registration is frozen once step 9 completes; after that, any change to a hashed file follows the deviations policy (`PREREG_EC_SIM_v1.md`, Part B, Other).

## Before OSF: freeze the repository

1. Confirm the branch and version. `git -C . status` is clean on `ec-fast-track`; `VERSION` reads `5.16.0`; `CHANGELOG.md` and `docs/releases/RELEASE_NOTES_5.16.md` carry the EC entry; `simulation/MANIFEST.json` pins the five `constitution/canon.json` digests (run `python3 simulation/ec/build_all_canons.py` first; it is deterministic, so a rebuild changes nothing if the canons are current).
2. Fix the LLM model identifier. In `PREREG_EC_SIM_v1.md` replace the line marked `FIXED AT FREEZE` under Design Plan, Study design, with the exact provider model id string that `--agent llm:anthropic:<id>` will receive, and add that id to `PRICES` in `simulation/ec/agents/llm.py` if it is not already a key. Do not fill the DOI line yet.
3. Run the EC tests: `python3 -m pytest tests/test_ec_core.py tests/test_ec_driver.py -q`. All pass.
4. Delete every development results directory that is not disclosed in Part A §1 (`simulation/ec/results/` is git-ignored; the disclosed `pilot30` may stay).
5. Compute the plan hash: `python3 prereg/make_plan_hash.py`. It writes `prereg/PLAN_HASH.md` and `prereg/plan_hash.txt`. Commit everything under `prereg/` and the canons; tag the commit `prereg-ec-sim-v1`. Record the tag's commit id in the OSF project wiki (step 7).
6. Build the upload archives from the tagged commit:
   - `git archive --format=zip -o /tmp/dj-5.16.0-ec-fast-track-prereg.zip prereg-ec-sim-v1` (code, canons, tests, prereg files; public tier);
   - `zip -j /tmp/ec-canons.zip simulation/*/constitution/canon.json` (public tier);
   - `sha256sum /tmp/*.zip > /tmp/archives.sha256`.

## On OSF

7. Create the project, or a component under an existing programme project if you keep one for the Digital Judiciary (a component gets its own registration and keeps this study beside the DMAIL 2026 and Who Decides registrations). osf.io → Create new project → title `Enterprise Conscience fast track in the Digital Judiciary: 365-day five-company simulation`; category Project; description: the first paragraph of Part B, Study Information, Description. Add contributors matching the EC author list (Kadambi, Sha, Kuppuswamy). Add a wiki page `Freeze` with: the git tag, the commit id, the plan hash from `plan_hash.txt`, the VERSION, and the date.
8. Upload files to OSF Storage, in a folder `prereg/`: `PREREG_EC_SIM_v1.md`, `ANALYSIS_PLAN.md`, `DATA_DICTIONARY.md`, `ESTIMAND_MAP.md`, `OSF_UPLOAD_CHECKLIST.md`, `PLAN_HASH.md`, `plan_hash.txt`, `make_plan_hash.py`; in a folder `freeze/`: the two zip archives and `archives.sha256`; in a folder `canons/`: the five `canon.json` files named `<pack>.canon.json`. Set the project licence to CC BY 4.0 (data and documents); the code archive carries Apache-2.0 inside it.
9. Create the registration. Project → Registrations → New registration → template "OSF Preregistration" (it has the Prereg Challenge sections). Fill each section by pasting the matching Part B section of `PREREG_EC_SIM_v1.md`: Study Information (Title, Authors, Description, Hypotheses); Design Plan (Study type, Blinding, Is there any additional blinding, Study design, Randomization); Sampling Plan (Existing data, Explanation of existing data, Data collection procedures, Sample size, Sample size rationale, Stopping rule); Variables (Manipulated, Measured, Indices); Analysis Plan (Statistical models, Transformations, Inference criteria, Data exclusion, Missing data, Exploratory analysis); Other. Where OSF offers the AsPredicted template instead, paste Part A's nine answers; both parts are the same registration. Attach the `prereg/` and `freeze/` folders to the registration. Because the EC article is under double-blind review at AI and Ethics, do **not** make the registration public yet: choose **Embargo** (one year is enough; it can be ended early) and, once the registration is approved, create an **anonymized view-only link** for it (Registration → Settings → View-only links → tick "Anonymize"). That link, which shows "Anonymous Contributors", is what the manuscript cites during review, as the DMAIL 2026 registration (agrz6) does. End the embargo and replace the link with the DOI when the article is accepted or the review is no longer blind. Submit.
10. Record the DOI. When OSF mints the registration DOI, write it into the `| OSF registration DOI |` line of `prereg/PREREG_EC_SIM_v1.md` in the repository and commit that one-line change; the line is excluded from the plan hash, so `plan_hash.txt` is unchanged (re-run `make_plan_hash.py` to confirm it prints the same hash). Add the DOI to the OSF wiki `Freeze` page and to `CITATION.cff` under `preferred-citation`/`identifiers`.

## After the registered run

11. Upload the datasets zip. Build `ec-registered-results.zip` from `simulation/ec/results/registered/` with the two tiers separated:
    - `public/`: every `metrics.csv`, `metrics.json`, `analysis.md`, `analysis.json`, `summary.json`, `manifest.json`, `bench_log.json`, `run_config.json`, `timings.json`;
    - `trusted/`: every `run.jsonl`, `registry.json`, `store_final.json`, `glosses_final.json`, and `llm_cache/`.
    Upload `public/` as an OSF Storage folder `results-public/` on the project (not the registration, which is frozen). Upload `trusted/` as a separate OSF component `EC simulation: per-unit stream exports` with view access restricted to contributors; grant access on request as `simulation/RELEASE_TIERS.md` describes for the trusted-contributor tier. Record both archive digests in the wiki.
12. Link the results. Add the registered-extension note (the analysis write-up) to the project as `results-public/REGISTERED_EXTENSION_NOTE.md`, with every figure marked ⟦measured⟧, ⟦derived⟧, ⟦PROJECTED⟧ or ⟦identity⟧, and cite the registration DOI in it and in the EC revision's Sect. 4.5.

## Tier assignment per file (per `simulation/RELEASE_TIERS.md`)

| File | Tier | Reason |
|---|---|---|
| `prereg/*.md`, `prereg/plan_hash.txt`, `prereg/make_plan_hash.py` | public | registration text and procedure |
| `simulation/<pack>/constitution/canon.json` (5) | public | constitutions and canons are public in every release |
| `simulation/ec/*.py`, `simulation/ec/agents/*.py`, `simulation/ec/DESIGN.md`, `tests/test_ec_*.py` | public | reference engine, harness, conformance and tests are public; the archetype table (six numbers per row) and the eight one-line driver sentences name no real system |
| `metrics.csv`, `metrics.json`, `analysis.md`, `analysis.json` | public | aggregate statistics |
| `summary.json`, `manifest.json`, `bench_log.json`, `run_config.json`, `timings.json` | public | counts, digests and hearing logs; `bench_log` carries act ids but no narrative |
| `run.jsonl` | trusted-contributor | per-unit stream export: every proposal, act, verdict and examen narrative |
| `registry.json`, `store_final.json`, `glosses_final.json` | trusted-contributor | per-unit instance records (tokens with act ids; DJ records; glossed canon) |
| `llm_cache/` | trusted-contributor | raw model replies keyed by prompt digest |
| withheld | none | plan v0.1 §3.6 provisionally placed the misreporting and adversarial archetype rows and the pressure-driver prompts in the withheld tier; this registration places them in the public tier for the reason `RELEASE_TIERS.md` gives (closed, synthetic, no real identifier, no capability conferred); the author's sign-off on this placement is recorded by the act of registering |
