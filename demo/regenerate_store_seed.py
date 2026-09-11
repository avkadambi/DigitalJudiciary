#!/usr/bin/env python3
"""Rewrite each pack's `store_seed.json` from an executed replay.

`store_seed_initial.json` is the store as of the first case — twenty authored
records, in the seed-import shape the bootstrap reads. `store_seed.json` is a
different object: the store as it stands AFTER the corpus has run, in the
ledger's own row shape. It is documentation of the executed end state, and
nothing in the reproduction path imports it.

Which is exactly why it goes stale silently, and why Appendix C's defect 4 was
a stale index file rather than a wrong result. Regenerating it is one command
and the file records the date and the corpus size it came from, so the next
reader can tell at a glance whether it still describes the corpus in front of
them.

Usage:  python3 demo/regenerate_store_seed.py <db-dir> [<note>]
where <db-dir> holds one executed <pack>.db per pack.
"""
from __future__ import annotations
import json, os, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACKS = ("sctower", "vetpoc", "dcvigil", "frontierllm")


def main(dbdir: str, note: str) -> int:
    for pack in PACKS:
        db = os.path.join(dbdir, f"{pack}.db")
        if not os.path.exists(db):
            print(f"  {pack}: no executed database at {db}", file=sys.stderr)
            return 2
        c = sqlite3.connect(db)
        c.row_factory = sqlite3.Row
        rows = [dict(r) for r in c.execute(
            "SELECT * FROM precedent_record ORDER BY resolved_at, id")]
        cases = json.load(open(os.path.join(
            HERE, "companies", pack, "cases.json")))["cases"]
        c.close()
        out = {"records": rows, "regenerated": note,
               "corpus_cases": len(cases),
               "consolidated": sum(1 for r in rows
                                   if r.get("admission_ground")
                                   == "consolidation")}
        path = os.path.join(HERE, "companies", pack, "store_seed.json")
        json.dump(out, open(path, "w"), indent=1)
        print(f"  {pack}: {len(rows)} records"
              f" ({out['consolidated']} consolidated) from {len(cases)} cases")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else
                  "regenerated from an executed replay"))
