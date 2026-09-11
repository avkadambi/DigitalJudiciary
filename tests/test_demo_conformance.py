"""The three demo-pack suites the architecture and case-base papers report (61 / 44 / 53)."""
import re

import pytest

from conftest import result_line, run


@pytest.mark.parametrize("script,expected", [
    ("run_conformance.py", 61),
    ("run_interface_conformance.py", 44),
    ("run_extension_conformance.py", 53),
])
def test_demo_suite_holds(script, expected):
    line = result_line(run([script]))
    m = re.search(r"(\d+)/(\d+)", line)
    assert m, line
    held, total = int(m.group(1)), int(m.group(2))
    assert held == total == expected, line
