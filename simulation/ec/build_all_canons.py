"""
Write `simulation/<pack>/constitution/canon.json` for the five packs (DESIGN §1).

    python3 simulation/ec/build_all_canons.py [--packs vetpoc,semifab,...] [--check]

The canon is generated, not authored: the same rulebook produces the same
canon.json byte for byte, so re-running is a no-op and `--check` fails when a
checked-in canon.json no longer matches its rulebook (EC-01). Nothing else in
a pack changes.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from simulation.ec.canon import TIERS, build_canon  # noqa: E402

PACKS = {
    "vetpoc": "vetpoc-constitution-corpus",
    "semifab": "semifab-constitution-corpus",
    "frontierllm": "frontierllm-constitution-corpus",
    "dcvigil": "dcvigil-constitution-corpus",
    "meridian": "meridian-corpus",
}


def resolve_pack(name: str) -> str:
    return PACKS.get(name, name)


def build_one(pack_dir: str, check: bool = False) -> tuple[dict, bool]:
    """Build the canon and write it unless the file already matches. Returns
    (tier counts, changed)."""
    canon = build_canon(pack_dir)
    out = os.path.join(pack_dir, "constitution", "canon.json")
    new_text = json.dumps(canon.to_dict(), indent=2, sort_keys=True) + "\n"
    old_text = None
    if os.path.exists(out):
        with open(out) as fh:
            old_text = fh.read()
    changed = old_text != new_text
    if changed and not check:
        with open(out, "w") as fh:
            fh.write(new_text)
    counts = canon.by_tier()
    counts["version"] = canon.version
    return counts, changed


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--packs", default="all", help="comma list of pack short names or directories; default all five")
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if any canon.json is stale")
    args = ap.parse_args(argv)

    names = list(PACKS) if args.packs == "all" else [p.strip() for p in args.packs.split(",") if p.strip()]
    rows, stale = [], []
    for name in names:
        pack_dir = os.path.join(ROOT, "simulation", resolve_pack(name))
        if not os.path.isdir(pack_dir):
            print(f"no such pack: {pack_dir}", file=sys.stderr)
            return 2
        counts, changed = build_one(pack_dir, check=args.check)
        rows.append((resolve_pack(name), counts, changed))
        if changed:
            stale.append(resolve_pack(name))

    width = max(len(r[0]) for r in rows)
    print(f"{'pack':<{width}}  " + "  ".join(f"{t:>4}" for t in TIERS) + "  total  status")
    for pack, counts, changed in rows:
        total = sum(counts[t] for t in TIERS)
        status = ("stale" if args.check else "written") if changed else "unchanged"
        print(f"{pack:<{width}}  " + "  ".join(f"{counts[t]:>4}" for t in TIERS) + f"  {total:>5}  {status}")
    if args.check and stale:
        print(f"RESULT: stale canon.json for {', '.join(stale)}")
        return 1
    print(f"RESULT: {len(rows)}/{len(rows)} canons built")
    return 0


if __name__ == "__main__":
    sys.exit(main())
