"""Release hygiene: versions agree, no build-environment residue, placeholders flagged."""
import glob
import json
import os
import re
import warnings

from conftest import ROOT


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def test_versions_agree():
    version = _read("VERSION").strip()
    assert re.fullmatch(r"\d+\.\d+\.\d+", version), version
    assert f'version = "{version}"' in _read("pyproject.toml")
    assert f"version: {version}" in _read("CITATION.cff")
    assert json.loads(_read(".zenodo.json"))["version"] == version
    assert f"Release **{version}**" in _read("README.md")


def test_no_build_environment_paths():
    offenders = []
    for pattern in ("**/*.py", "**/*.md", "**/*.sh", "**/*.json", "**/*.yml", "**/*.toml", "**/*.cff"):
        for f in glob.glob(os.path.join(ROOT, pattern), recursive=True):
            if "/.git/" in f or "/corpus/" in f:
                continue
            try:
                txt = open(f, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            markers = ("/home/" + "claude", "/Users" + "/")   # spelled apart so this file does not match itself
            if any(mk in txt for mk in markers):
                offenders.append(os.path.relpath(f, ROOT))
    assert not offenders, offenders


def test_full_licence_texts_present():
    assert "APPENDIX: How to apply the Apache License to your work" in _read("LICENSE")
    assert "Creative Commons Attribution 4.0" in _read("LICENSE-DATA")
    assert os.path.exists(os.path.join(ROOT, "NOTICE"))
    for pack in glob.glob(os.path.join(ROOT, "simulation", "*", "LICENSE-DATA")):
        assert "CC BY 4.0" in open(pack).read(), pack


def test_placeholders_flagged():
    """Placeholders left for the maintainers before the first public push. Warns, does not fail."""
    found = []
    for rel in ("README.md", "pyproject.toml", "CITATION.cff", ".zenodo.json", "SECURITY.md", ".github/workflows/ci.yml"):
        txt = _read(rel)
        if "OWNER/digital-judiciary" in txt:
            found.append(f"{rel}: repository URL placeholder OWNER/digital-judiciary")
        if "SECURITY-CONTACT@example.org" in txt:
            found.append(f"{rel}: security contact placeholder")
    for item in found:
        warnings.warn(f"release placeholder still present — {item}", stacklevel=1)
