# Contributing

Thank you for looking under the hood. This repository is a research artefact
first — every number in the companion papers regenerates from it — so the bar
for a change is that the regeneration still holds, or that the change says
exactly which figure it moves and why.

## Ground rules

1. **Nothing is authored that can be computed.** Ground truth for every corpus
   is the reference engine's chronological pass, never a hand-written label.
   If your change alters a trace, the manifest digests change with it, and the
   release notes must say so.
2. **Every check must be able to fail.** A new conformance check comes with a
   mutant in the pack's `harness/mutation_matrix.py` that it kills. A check
   nothing can fail is not a check.
3. **One engine.** The five simulation packs and Numerals carry byte-identical
   copies of `harness/engine.py` (two header lines excepted). Edit the copy in
   `simulation/vetpoc-constitution-corpus/harness/engine.py` and propagate with
   `python3 simulation/tools/integrate_kernel.py`. `tests/test_engine_kernel.py`
   fails if the copies drift.
4. **Never load a pack while its mutation matrix is running.** The matrix
   swaps mutated files in and out of the tree and leaves a `.mutation-backup`
   sidecar while it does; anything that reads the pack mid-run reads a mutated
   engine. The test suite refuses a tree with a sidecar on disk. If a run is
   interrupted, restore the file from its sidecar **and delete the pack's
   `__pycache__`**: the mutant's bytecode is newer than the restored source and
   Python will keep running the mutant until the cache is cleared (this bit us
   once; the symptom is a suite that suddenly reports 45/56 on an intact engine).
5. **No third-party dependency on the reproduction path.** CPython 3.10+ and
   SQLite. Optional extras (Postgres, model backends for the extraction stage)
   are declared in `pyproject.toml` and imported lazily.

## Before you open a pull request

```
ruff check .                     # lint (correctness rules only)
python -m pytest tests -q        # demo suites, pack suites, Numerals, digests
bash reproduce/run_all.sh        # ~2 min: every demo-pack figure
bash reproduce/run_all_simulation.sh   # ~10 min: the five packs and Numerals
```

If you changed a generator, run `bash reproduce/run_all_simulation.sh --rebuild`
and commit the regenerated corpus files together with the updated digests in
`simulation/MANIFEST.json`. If you changed a check, run the pack's mutation
matrix and paste its `RESULT` line in the pull request.

## What we are looking for

- Corrections to any figure, definition or citation — with the file and line.
- New scenario classes for the constitutions (see
  `simulation/tools/EXTENSION_AUTHORING_SPEC.md`), filed by addition and never
  by editing an existing provision.
- The build list in the benchmark paper's §3.6: the pass^k estimator, the
  citation requirement in the pair test, the ordering/escalation/floor
  switches, a `--tau` override, a strategic-contest policy, a consolidation
  switch, both-branch gold, pair separation strata, adversarial chains.
- Real change descriptions for the characterisation stage, so that its
  figures stop being upper bounds.

## What we will decline

Anything that authors ground truth by hand; anything that makes a check
unfailable; a dependency added to the reproduction path; and generator prompts
or seeds for adversarial-framing strata (see `DUAL_USE.md`).

## Reporting a security issue

See `SECURITY.md`. Please do not open a public issue for a vulnerability.

## Licence

By contributing you agree that your contribution is licensed under Apache-2.0
(code) or CC BY 4.0 (data), as the rest of the repository is. Add yourself to
`NOTICE` if you wish.
