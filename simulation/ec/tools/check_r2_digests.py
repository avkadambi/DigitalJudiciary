"""
Byte-identity check for the R2 calibration (governance build, H1).

Compares the sha256 of each freshly generated reference file under
`simulation/ec/results/calibration_r2/` with the sha256 of the same path in the
tree at the R2 calibration commit (`git show af83fc8:<path>`). It regenerates
nothing itself: run `bash reproduce/run_year.sh registered` first.

    python3 simulation/ec/tools/check_r2_digests.py [--results DIR] [--ref COMMIT]

Prints `OK` or `DIFF` per file and `RESULT: n/20`; exits 1 on any DIFF or
missing file.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REF_COMMIT = "af83fc8"
REL_DIR = "simulation/ec/results/calibration_r2"
RUN_ROOTS = ("honest", "pressure_sensitive", "observation_sensitive", "misreporting", "laundering",
             "sensitivity/bench_cap2", "sensitivity/ciso_engineering", "bounds/oracle", "bounds/adversarial",
             "llm_dry")
FILES = ("metrics.csv", "analysis.md")


def reference_paths() -> list:
    return [f"{REL_DIR}/{r}/{f}" for r in RUN_ROOTS for f in FILES]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_show(commit: str, path: str) -> bytes:
    return subprocess.run(["git", "-C", ROOT, "show", f"{commit}:{path}"], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def check(results_dir: str, ref: str = REF_COMMIT, out=sys.stdout) -> int:
    """Number of files that match; prints one line per file and the RESULT line."""
    ok = 0
    paths = reference_paths()
    for rel in paths:
        sub = rel[len(REL_DIR) + 1:]
        fresh = os.path.join(results_dir, sub)
        try:
            want = sha256_bytes(git_show(ref, rel))
        except subprocess.CalledProcessError:
            print(f"DIFF  {sub}  (not in {ref})", file=out)
            continue
        if not os.path.exists(fresh):
            print(f"DIFF  {sub}  (missing)", file=out)
            continue
        with open(fresh, "rb") as fh:
            got = sha256_bytes(fh.read())
        if got == want:
            ok += 1
            print(f"OK    {sub}", file=out)
        else:
            print(f"DIFF  {sub}", file=out)
    print(f"RESULT: {ok}/{len(paths)}", file=out)
    return ok


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="R2 calibration byte-identity check against " + REF_COMMIT)
    ap.add_argument("--results", default=os.path.join(ROOT, REL_DIR),
                    help="directory holding the freshly generated calibration_r2 tree")
    ap.add_argument("--ref", default=REF_COMMIT)
    a = ap.parse_args(argv)
    n = check(a.results, a.ref)
    return 0 if n == len(reference_paths()) else 1


if __name__ == "__main__":
    sys.exit(main())
