"""The LLM governance build (EC_LLM_GOVERNANCE_BUILD_PLAYBOOK v3): every governance
seat can be deterministic (today's code), llm (the model binds) or shadow (the
answer key binds and the model is only logged). Nothing here calls a network
except the local mock server."""
from __future__ import annotations

import io
import os
import shutil
import sys

import pytest

from conftest import ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec import run_year                                   # noqa: E402
from simulation.ec.tools import check_r2_digests                     # noqa: E402

R2_DIR = os.path.join(ROOT, check_r2_digests.REL_DIR)


# ---------------------------------------------------------------------------
# H1: the R2 digest check
# ---------------------------------------------------------------------------


def _ref_available() -> bool:
    import subprocess
    r = subprocess.run(["git", "-C", ROOT, "cat-file", "-e", check_r2_digests.REF_COMMIT + "^{commit}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return r.returncode == 0


needs_ref = pytest.mark.skipif(not _ref_available() or not os.path.isdir(R2_DIR),
                               reason="R2 reference commit or calibration_r2 tree not available")


@needs_ref
def test_h1_reference_files_match():
    out = io.StringIO()
    assert check_r2_digests.check(R2_DIR, out=out) == 20
    assert "RESULT: 20/20" in out.getvalue()


@needs_ref
def test_h1_modified_copy_fails(tmp_path):
    copy = tmp_path / "calibration_r2"
    shutil.copytree(R2_DIR, copy)
    with open(copy / "honest" / "metrics.csv", "a") as fh:
        fh.write("tampered\n")
    out = io.StringIO()
    assert check_r2_digests.check(str(copy), out=out) == 19
    assert "DIFF  honest/metrics.csv" in out.getvalue()
    assert check_r2_digests.main(["--results", str(copy)]) == 1


# ---------------------------------------------------------------------------
# H2: Python 3.9 or later
# ---------------------------------------------------------------------------


def test_h2_python_check_rejects_38():
    with pytest.raises(SystemExit) as ei:
        run_year.check_python((3, 8, 18))
    assert "Python 3.9 or later is required (found 3.8)" in str(ei.value)


def test_h2_python_check_accepts_39_and_later():
    run_year.check_python((3, 9, 0))
    run_year.check_python(sys.version_info)
