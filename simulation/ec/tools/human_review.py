"""
Human review of L4 items (governance build v3, §5.7), for pilots in
`--l4 queue` mode.

    python3 simulation/ec/tools/human_review.py list   <run-dir>
    python3 simulation/ec/tools/human_review.py show   <run-dir> <item>
    python3 simulation/ec/tools/human_review.py decide <run-dir> <item> <permit|permit_conditional|deny>
                                                        [--overturn-absolute] [--note TEXT]

`list` shows the items in human_queue.jsonl and whether each is decided; `show`
prints an item as the person sees it; `decide` validates and appends one line to
human_decisions.jsonl. A permit that affirms an absolute violation is refused:
overturn the finding explicitly or deny. This tool reads no keys and calls no
model.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HOLDINGS = ("permit", "permit_conditional", "deny")
QUEUE_FILE, DECISIONS_FILE = "human_queue.jsonl", "human_decisions.jsonl"


def _read(path: str) -> list:
    if not os.path.exists(path):
        return []
    with open(path) as fh:
        return [json.loads(x) for x in fh if x.strip()]


def queue(run_dir: str) -> list:
    return _read(os.path.join(run_dir, QUEUE_FILE))


def decisions(run_dir: str) -> dict:
    return {d["item"]: d for d in _read(os.path.join(run_dir, DECISIONS_FILE))}


def decide(run_dir: str, item: str, holding: str, overturn: bool = False, note: str | None = None) -> dict:
    items = {q["item"]: q for q in queue(run_dir)}
    if item not in items:
        raise ValueError(f"no queued item {item}")
    if item in decisions(run_dir):
        raise ValueError(f"item {item} is already decided")
    if holding not in HOLDINGS:
        raise ValueError(f"holding must be one of {HOLDINGS}")
    if items[item].get("a6_found") and holding != "deny" and not overturn:
        raise ValueError("refused: a permit may not affirm an absolute violation (use --overturn-absolute or deny)")
    d = {"item": item, "holding": holding, "absolute_finding_overturned": bool(overturn and holding != "deny"),
         "note": (note or "")[:500] or None}
    with open(os.path.join(run_dir, DECISIONS_FILE), "a") as fh:
        fh.write(json.dumps(d, sort_keys=True) + "\n")
    return d


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Decide L4 items queued by a pilot run (--l4 queue).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").add_argument("run_dir")
    s = sub.add_parser("show")
    s.add_argument("run_dir")
    s.add_argument("item")
    d = sub.add_parser("decide")
    d.add_argument("run_dir")
    d.add_argument("item")
    d.add_argument("holding", choices=HOLDINGS)
    d.add_argument("--overturn-absolute", action="store_true")
    d.add_argument("--note")
    a = ap.parse_args(argv)
    if a.cmd == "list":
        done = decisions(a.run_dir)
        for q in queue(a.run_dir):
            mark = done[q["item"]]["holding"] if q["item"] in done else "PENDING"
            print(f"{q['item']:24} {q.get('case_id') or '':24} {q.get('origin') or '':22} "
                  f"{'A6 ' if q.get('a6_found') else '   '}{mark}")
        return 0
    if a.cmd == "show":
        items = {q["item"]: q for q in queue(a.run_dir)}
        if a.item not in items:
            print(f"no queued item {a.item}", file=sys.stderr)
            return 2
        print(items[a.item]["text"])
        return 0
    try:
        print(json.dumps(decide(a.run_dir, a.item, a.holding, a.overturn_absolute, a.note), sort_keys=True))
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
