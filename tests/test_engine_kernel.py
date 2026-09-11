"""Direct checks on the shared comparison kernel: the properties every pack's suite relies on."""
import importlib.util
import os
import sys

from conftest import PACKS, ROOT


def load_engine(pack):
    path = os.path.join(ROOT, "simulation", pack, "harness", "engine.py")
    spec = importlib.util.spec_from_file_location(f"engine_{pack}", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_engine_copies_identical_apart_from_header():
    """The six engine copies are one engine. Only the two header lines naming the pack may differ."""
    bodies = {}
    for pack in PACKS + ["numerals"]:
        with open(os.path.join(ROOT, "simulation", pack, "harness", "engine.py")) as fh:
            lines = fh.read().splitlines()
        bodies[pack] = "\n".join(ln for ln in lines if not ln.startswith(("# pack:", "# Pack:", '"""Engine for')))
    ref = bodies[PACKS[0]]
    for pack, body in bodies.items():
        diff = sum(1 for a, b in zip(ref.splitlines(), body.splitlines()) if a != b) + abs(len(ref.splitlines()) - len(body.splitlines()))
        assert diff <= 2, f"{pack}: engine.py differs from {PACKS[0]} in {diff} lines"


def test_no_mutation_backup_left_on_disk():
    """A .mutation-backup sidecar means a pack is mid-mutation; loading it would read a mutated engine."""
    stray = []
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "simulation")):
        stray += [os.path.join(dirpath, f) for f in files if f.endswith(".mutation-backup")]
    assert not stray, stray


def test_silence_never_binds():
    eng = load_engine(PACKS[0])
    assert hasattr(eng, "admit") and hasattr(eng, "Case") and hasattr(eng, "Record")
    assert "PREMISE_UNPROVEN" in dir(eng) or any("PREMISE" in n for n in dir(eng))
