#!/usr/bin/env python3
"""
Plan hash for the EC simulation preregistration.

    python3 prereg/make_plan_hash.py [--repo <path>] [--check]

Digests (sha256) every file the registration freezes:
  * prereg/*.md except PLAN_HASH.md, and this script;
  * simulation/<pack>/constitution/canon.json for the five packs;
  * every .py and .md file under simulation/ec/ (results/ and __pycache__/ excluded);
  * tests/test_ec_*.py.

The single line of prereg/PREREG_EC_SIM_v1.md that begins "| OSF registration DOI |"
is removed before that file is digested, so the DOI can be filled in after OSF
mints it without moving the hash.

The plan hash is sha256 over the sorted lines "<relpath>  <digest>\n". It is
written to prereg/plan_hash.txt, and with the per-file table, the git commit
and the package VERSION to prereg/PLAN_HASH.md. --check recomputes and exits 1
if plan_hash.txt differs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import hashlib
import os
import subprocess
import sys

PACKS = (
    "vetpoc-constitution-corpus",
    "semifab-constitution-corpus",
    "frontierllm-constitution-corpus",
    "dcvigil-constitution-corpus",
    "meridian-corpus",
)
PREREG_MAIN = "prereg/PREREG_EC_SIM_v1.md"
DOI_LINE_PREFIX = b"| OSF registration DOI |"
EXCLUDED_OUTPUTS = {"prereg/PLAN_HASH.md", "prereg/plan_hash.txt"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(repo: str, rel: str) -> str:
    with open(os.path.join(repo, rel), "rb") as fh:
        data = fh.read()
    if rel == PREREG_MAIN:
        data = b"\n".join(line for line in data.split(b"\n") if not line.startswith(DOI_LINE_PREFIX))
    return sha256_bytes(data)


def registered_files(repo: str) -> dict:
    """relpath -> group, for every frozen file."""
    out = {}
    for p in sorted(glob.glob(os.path.join(repo, "prereg", "*.md"))):
        rel = os.path.relpath(p, repo)
        if rel not in EXCLUDED_OUTPUTS:
            out[rel] = "prereg"
    out["prereg/make_plan_hash.py"] = "prereg"
    for pack in PACKS:
        rel = os.path.join("simulation", pack, "constitution", "canon.json")
        if not os.path.exists(os.path.join(repo, rel)):
            raise SystemExit(f"missing canon: {rel} (run simulation/ec/build_all_canons.py)")
        out[rel] = "canon"
    ec_root = os.path.join(repo, "simulation", "ec")
    for base, dirs, files in os.walk(ec_root):
        dirs[:] = sorted(d for d in dirs if d not in ("results", "__pycache__"))
        for f in sorted(files):
            if f.endswith((".py", ".md")):
                out[os.path.relpath(os.path.join(base, f), repo)] = "ec"
    for p in sorted(glob.glob(os.path.join(repo, "tests", "test_ec_*.py"))):
        out[os.path.relpath(p, repo)] = "tests"
    return dict(sorted(out.items()))


def compute(repo: str) -> tuple:
    files = registered_files(repo)
    digests = {rel: digest_file(repo, rel) for rel in files}
    lines = "".join(f"{rel}  {digests[rel]}\n" for rel in sorted(digests))
    return files, digests, sha256_bytes(lines.encode("utf-8"))


def git(repo: str, *args: str) -> str:
    try:
        return subprocess.check_output(["git", "-C", repo, *args], stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


def render(repo: str, files: dict, digests: dict, plan_hash: str) -> str:
    version = "unknown"
    vp = os.path.join(repo, "VERSION")
    if os.path.exists(vp):
        with open(vp) as fh:
            version = fh.read().strip()
    L = ["# Plan hash", ""]
    L.append(f"**Plan hash (sha256):** `{plan_hash}`")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append(f"| Computed | {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} |")
    L.append(f"| Package VERSION | {version} |")
    L.append(f"| Git branch | {git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')} |")
    L.append(f"| Git commit at computation | {git(repo, 'rev-parse', 'HEAD')} (informational; not a hash input) |")
    L.append(f"| Files | {len(files)} |")
    L.append("")
    L.append("Procedure: sha256 of every file below; the plan hash is the sha256 of the sorted lines "
             "`<path>  <digest>\\n`. The line of `prereg/PREREG_EC_SIM_v1.md` beginning "
             "`| OSF registration DOI |` is removed before that file is digested. "
             "`prereg/PLAN_HASH.md` and `prereg/plan_hash.txt` are outputs and not inputs. "
             "Recompute with `python3 prereg/make_plan_hash.py --check`.")
    L.append("")
    for group, title in (("prereg", "Preregistration files"), ("canon", "Canons"),
                         ("ec", "simulation/ec package"), ("tests", "EC tests")):
        L.append(f"## {title}")
        L.append("")
        L.append("| File | sha256 |")
        L.append("|---|---|")
        for rel in sorted(r for r, g in files.items() if g == group):
            L.append(f"| `{rel}` | `{digests[rel]}` |")
        L.append("")
    L.append("## Amendments")
    L.append("")
    L.append("None. A post-freeze change to any file above is recorded here with its reason, "
             "the previous hash and the new hash, and posted to the OSF registration as an update "
             "before any further registered run.")
    L.append("")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="EC preregistration plan hash")
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--check", action="store_true", help="recompute and compare with plan_hash.txt")
    a = ap.parse_args(argv)
    repo = os.path.abspath(a.repo)
    files, digests, plan_hash = compute(repo)
    txt = os.path.join(repo, "prereg", "plan_hash.txt")
    if a.check:
        if not os.path.exists(txt):
            print("no plan_hash.txt", file=sys.stderr)
            return 1
        with open(txt) as fh:
            recorded = fh.read().strip()
        if recorded != plan_hash:
            print(f"MISMATCH recorded {recorded} computed {plan_hash}", file=sys.stderr)
            return 1
        print(f"ok {plan_hash}")
        return 0
    with open(os.path.join(repo, "prereg", "PLAN_HASH.md"), "w") as fh:
        fh.write(render(repo, files, digests, plan_hash))
    with open(txt, "w") as fh:
        fh.write(plan_hash + "\n")
    print(plan_hash)
    return 0


if __name__ == "__main__":
    sys.exit(main())
