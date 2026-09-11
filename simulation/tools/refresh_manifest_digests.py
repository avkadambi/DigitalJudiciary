#!/usr/bin/env python3
"""Recompute the SHA-256 digests simulation/MANIFEST.json pins, and report what moved.

    python3 simulation/tools/refresh_manifest_digests.py            # report only
    python3 simulation/tools/refresh_manifest_digests.py --write    # update MANIFEST.json

A digest moves for exactly two legitimate reasons — a generator was changed and the
corpus rebuilt, or a harness/benchmark source file was edited — and every such move
belongs in the release notes. Archive digests (simulation/zips) are refreshed only if
the archives are present; they are release assets, built by reproduce/make_pack_zips.sh,
and are not committed.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(SIM)
PATH = os.path.join(SIM, "MANIFEST.json")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main(argv=None):
    write = "--write" in (argv or sys.argv[1:])
    m = json.load(open(PATH))
    moved = []

    def refresh(table, base, label):
        for rel, old in list(table.items()):
            p = os.path.join(ROOT, base, rel)
            if not os.path.exists(p):
                moved.append((label, rel, "MISSING"))
                continue
            new = sha(p)
            if new != old:
                moved.append((label, rel, "changed"))
                table[rel] = new

    for pack in m["packs"]:
        refresh(pack["sha256"], pack["directory"], pack["label"])
        arc = pack.get("archive")
        if arc and os.path.exists(os.path.join(ROOT, arc["path"])):
            new = sha(os.path.join(ROOT, arc["path"]))
            if new != arc["sha256"]:
                moved.append((pack["label"], arc["path"], "archive changed"))
                arc["sha256"] = new
                arc["bytes"] = os.path.getsize(os.path.join(ROOT, arc["path"]))
    refresh(m["numerals"]["sha256"], "simulation/numerals", "Numerals")

    for label, rel, what in moved:
        print(f"{label:12} {what:16} {rel}")
    if not moved:
        print("all digests current")
    if write and moved:
        with open(PATH, "w") as fh:
            json.dump(m, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
        print(f"MANIFEST.json updated ({len(moved)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
