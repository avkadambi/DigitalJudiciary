# Release 5.15.0 — the publication cut

11 September 2026. No trace, corpus, expectation or published figure changes in
this release. It makes the tree a repository: the things a first-time visitor,
a licence reviewer or a CI runner needs, none of which a replication zip did.

## Licensing

- `LICENSE` is the full Apache-2.0 text (it had been a two-paragraph summary
  pointing at the URL). `NOTICE` is new: copyright, the code/data licence
  split, and every third-party acknowledgement in one place.
- `LICENSE-DATA` at the root now covers all the data in the tree — demo packs,
  seeds, the five simulation packs, Numerals, the manifest and audit documents,
  the extraction results — with one attribution string at the current versions.
  It had been a copy of Meridian's own file, attributing everything to
  "Meridian Financial Constitution Corpus v1.0.0". The six per-pack copies are
  brought to pack 2.4.0 / corpus 2.1.0 (Numerals: federation 1.3.0).

## Packaging and repository hygiene

- `pyproject.toml`: metadata, `requires-python >= 3.10` (the sources use
  `match`), no dependencies on the reproduction path, optional extras
  `postgres`, `extraction` and `dev`, a `dj-serve` entry point, and the ruff
  and pytest configuration. `app/__main__.py` makes `python -m app` start the
  service.
- `.gitignore` and `.gitattributes` are new. Two derived files per pack —
  `corpus/cases.jsonl` and `corpus/explorer_data.json` — are no longer
  committed (they are views of `cases.json` and `--rebuild` regenerates them);
  the pack archives under `simulation/zips/` are release assets rather than
  tree contents. The checkout is about 160 MB.
- Every shipped result file and generated document carried the build
  machine's absolute path. The benchmark runners now record pack-relative
  paths (`_portable_config`), the scenario documents are regenerated, and
  `tests/test_release_hygiene.py` fails if a build path ever comes back.
- Sources are lint-clean under ruff's correctness rules (pyflakes plus the
  always-a-bug pycodestyle errors): 71 findings fixed, all cosmetic — unused
  imports and locals, f-strings without placeholders — plus one real one, a
  duplicated dictionary key in VetPOC's `ext_vocab.py` whose first value was
  silently overridden (the second, which the corpus was built from, is kept).
- `app/reviewui_v54_legacy.py` (2,793 unreferenced lines) and
  `docs/DJ_User_Guide.docx` (a binary twin of `docs/USER_GUIDE.md`) are removed.
- The two code fragments `integrate_kernel.py` splices into packs are renamed
  `*.py.frag` so nothing tries to compile them.

## Tests and continuous integration

- `tests/` wires the conformance suites into pytest: the three demo suites
  (61/44/53), each pack's 56 checks, Numerals' 11, every digest in
  `simulation/MANIFEST.json`, cross-pack composition identity, engine-copy
  identity, and the `.mutation-backup` guard. Mutation matrices run under
  `--runslow`.
- `.github/workflows/ci.yml`: lint and byte-compile; the test suite and the
  full demo reproduction on Python 3.10, 3.12 and 3.13; the mutation matrices
  on pushes to `main`; a Docker build.
- `simulation/tools/refresh_manifest_digests.py` recomputes the manifest's
  digests and reports what moved, so a digest change is a deliberate act.

## Documentation

- `README.md` is rewritten for a public repository — what it is, three
  commands, the layout, the documents a reviewer should read, the design
  commitments, status, citing and licence. The former README's operating
  manual is kept whole as `docs/OPERATOR_NOTES.md`.
- `CHANGELOG.md` summarises every release since 5.0; the release notes move to
  `docs/releases/`. `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, issue and pull
  request templates are new.
- Three stale passages corrected: `REPRODUCE.md`'s "which build" section
  (a lineage table replaces the superseded 101-case figures and the three
  inconsistent seed counts); `DATASHEET.md` Part I (144 cases, thirteen
  categories); `PAPER_ALIGNMENT.md` (Paper 4 v2.1; the structural mismatch it
  led with is settled).
- `CITATION.cff` gains repository URLs and a preferred-citation block;
  `.zenodo.json` is at 5.15.0.
- `simulation/LIKEWISE_INTEGRATION.md` and the optional bridge state that
  Likewise is a separate project nothing here depends on.

## Two hazards found on the way

The verification run of this cut was killed twice, once mid-matrix, and both
interruptions taught something now written down. A
mutation matrix killed mid-run leaves the mutant in place with the original
beside it as `*.mutation-backup`; the test suite already refuses such a tree.
Less obviously, after restoring the source the pack's `__pycache__` still holds
the mutant's bytecode with a newer timestamp, and CPython keeps executing the
mutant — the suite reported 45/56 on a byte-identical engine until the cache
was cleared. `CONTRIBUTING.md` now says so, and every matrix run in CI starts
from a clean checkout.

## One correction found on the way

Numerals' shipped `constitution/rulebook.json` still recorded the five
divisions at corpus 2.0.0; the generator had written 2.1.0 since 5.14.0 but the
file had not been regenerated. It is regenerated (nothing else in it moves) and
the manifest digest updated.

## Two placeholders for the maintainers

`OWNER/digital-judiciary` in `README.md`, `pyproject.toml`, `CITATION.cff`,
`.zenodo.json` and the CI badge, and `SECURITY-CONTACT@example.org` in
`SECURITY.md`. `tests/test_release_hygiene.py` warns while either remains.
