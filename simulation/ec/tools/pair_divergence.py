"""
Compare the two runs of a shadow-and-binding pair (governance build v3, §3.5, R6).

    python3 simulation/ec/tools/pair_divergence.py <shadow-run-dir> <binding-run-dir> [--write]

The divergence day of each state component is the first working day on which
the binding run's end-of-day hash differs from the shadow run's (summary.json
`by_day[].state_hash`: the store, the glosses, the registry, and the agent's
prompts that day). `null` means the two never differed over the days both ran.
`prop` is error propagation: binding minus shadow, per summary total.

With `--write` (and from `run_year.py --pair`) the block is written into the
binding run's summary.json as `divergence`.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

COMPONENTS = ("store", "glosses", "registry", "agent_prompts")


def _summary(run_dir: str) -> dict:
    with open(os.path.join(run_dir, "summary.json")) as fh:
        return json.load(fh)


def divergence(shadow: dict, binding: dict) -> dict:
    """{"day_<component>": first differing day or None, "days_compared", "prop": {...}}."""
    sd = {d["day"]: d.get("state_hash") or {} for d in shadow.get("by_day") or []}
    bd = {d["day"]: d.get("state_hash") or {} for d in binding.get("by_day") or []}
    days = sorted(set(sd) & set(bd))
    out = {f"day_{c}": None for c in COMPONENTS}
    for day in days:
        for c in COMPONENTS:
            if out[f"day_{c}"] is None and sd[day].get(c) != bd[day].get(c):
                out[f"day_{c}"] = day
    first = [v for v in out.values() if v is not None]
    out["day_first"] = min(first) if first else None
    out["days_compared"] = len(days)
    out["hashes_present"] = bool(days) and all(sd[d] and bd[d] for d in days)
    st, bt = shadow.get("totals") or {}, binding.get("totals") or {}
    out["prop"] = {k: round(float(bt[k]) - float(st[k]), 6) for k in sorted(set(st) & set(bt))
                   if isinstance(st[k], (int, float)) and isinstance(bt[k], (int, float))}
    return out


def compare(shadow_dir: str, binding_dir: str) -> dict:
    d = divergence(_summary(shadow_dir), _summary(binding_dir))
    d["shadow_run"] = os.path.basename(os.path.normpath(shadow_dir))
    d["binding_run"] = os.path.basename(os.path.normpath(binding_dir))
    return d


def write_into_summary(shadow_dir: str, binding_dir: str) -> dict:
    d = compare(shadow_dir, binding_dir)
    path = os.path.join(binding_dir, "summary.json")
    s = _summary(binding_dir)
    s["divergence"] = d
    with open(path, "w") as fh:
        json.dump(s, fh, indent=1)
    return d


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Divergence days and error propagation of a shadow-and-binding pair.")
    ap.add_argument("shadow_dir")
    ap.add_argument("binding_dir")
    ap.add_argument("--write", action="store_true", help="write the block into the binding run's summary.json")
    a = ap.parse_args(argv)
    d = write_into_summary(a.shadow_dir, a.binding_dir) if a.write else compare(a.shadow_dir, a.binding_dir)
    print(json.dumps(d, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
