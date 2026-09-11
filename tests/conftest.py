"""pytest wiring for the Digital Judiciary.

The repository's tests ARE its conformance suites: the three demo suites at the
root, the 56-check suite each simulation pack carries, and the manifest digests
that pin every released corpus. These files run them under pytest so that a CI
runner, or `pytest`, gives one answer. Nothing here needs a network, an API key
or a third-party package.

Slow items (the mutation matrices, the full reproduction scripts) are marked
`slow` and skipped unless `--runslow` is given.
"""
from __future__ import annotations

import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = [
    "vetpoc-constitution-corpus",
    "semifab-constitution-corpus",
    "frontierllm-constitution-corpus",
    "dcvigil-constitution-corpus",
    "meridian-corpus",
]
ORACLE_ENV = {"DJ_JUDGE_MODE": "oracle", "DJ_DEV_KEYS": "1", "DJ_GITHUB_ALLOW_UNSIGNED": "1"}


def run(args, cwd=ROOT, env=None, timeout=1800):
    e = dict(os.environ)
    e.update(ORACLE_ENV)
    if env:
        e.update(env)
    return subprocess.run([sys.executable, *args], cwd=cwd, env=e, capture_output=True, text=True, timeout=timeout)


def result_line(proc):
    lines = [ln for ln in proc.stdout.splitlines() if ln.startswith("RESULT")]
    assert lines, f"no RESULT line\n--- stdout ---\n{proc.stdout[-2000:]}\n--- stderr ---\n{proc.stderr[-2000:]}"
    return lines[-1]


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", default=False, help="run the mutation matrices and full reproductions")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mutation matrices and full reproduction scripts")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        return
    skip = pytest.mark.skip(reason="needs --runslow")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip)
