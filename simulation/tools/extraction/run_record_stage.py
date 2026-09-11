#!/usr/bin/env python3
"""Measure record construction as its own stage on one pack.

    python3 tools/extraction/run_record_stage.py <pack-dir> [--reader cued|literal|nli] [--out DIR] [--brief]

Two passes.

  1. ROUND-TRIP. For every case the reference run admits to the store, render
     the rationale it would have produced — premise, citations with an assigned
     stance (superseded / followed / distinguished, varied so the stance reader
     is tested), a scope statement with an assigned width, and two present-but-
     immaterial facts as premise guards — in each held-out style; read it back;
     score. The gate fails at any n on the expensive errors: a premise factor
     omitted, a followed or distinguished record read as superseded, a scope
     read narrower than stated.
  2. REPLAY. Render every admitted case's rationale with the corpus's own
     truth (legacy stance = superseded, scope as authored), read it, and build
     the records from the READING — premise, cites and stance, scope, with
     `construction` provenance — then replay the pack's engine and compare
     each trace to the reference. Over-binds (bound where the reference did
     not, or on another record) are the cost of a premise read too narrow or a
     supersession read wrongly; under-binds and ties are the cost of the safe
     defaults.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extraction import records as R  # noqa: E402
from extraction import render, snapshot  # noqa: E402


def _h(*p):
    return int(hashlib.sha256("\x1f".join(str(x) for x in p).encode()).hexdigest(), 16)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("--reader", default="cued", choices=("cued", "literal", "nli"))
    ap.add_argument("--checkpoint", default=None, help="NLI checkpoint for --reader nli (default: the pinned zero-shot head)")
    ap.add_argument("--train-fraction", type=float, default=0.6)
    ap.add_argument("--min-records", type=int, default=300)
    ap.add_argument("--out", default=None)
    ap.add_argument("--brief", action="store_true")
    ap.add_argument("--novel-phrasing", action="store_true",
                    help="render immaterial, stance and scope sentences in phrasings no reader's cue list contains")
    a = ap.parse_args(argv)

    engine, rb, params, cases, seed, provisions = snapshot.load_pack(a.pack)
    pack_name = os.path.basename(os.path.abspath(a.pack))
    if a.reader == "nli":
        from extraction import backends
        reader = R.NLIRecordReader(backends.NLIZeroShotBackend(a.checkpoint))
    else:
        reader = R.CuedRecordReader() if a.reader == "cued" else R.LiteralRecordReader()
    ref = engine.replay(cases, seed, provisions, params["theta"])
    admitted_ids = {t["case"] for t in ref["traces"] if t["admitted"]}
    admitted = [c for c in cases if c["id"] in admitted_ids]
    _, eval_styles = render.split_styles(a.train_fraction)
    eval_styles = tuple(s for s in eval_styles if s in render.STYLES) or ("tabular", "elliptical")

    # ---- 1. round-trip with varied stance and scope ---------------------------
    sc = R.RecordScore()
    n = 0
    for c in admitted:
        cites = (c.get("engine") or {}).get("cites") or []
        stance_for = {rid: R.STANCES[_h(c["id"], rid) % 3] for rid in cites}
        width = 1 + _h(c["id"], "scope") % 5
        # A varied truth premise: a proper subset of the case's in-vocabulary
        # facts, the rest rendered as present-but-immaterial guards. The corpus
        # premise is the whole fact set, which would test nothing.
        vocab_facts = [f for f in c["facts"] if not f.startswith(("ctx_", "mk_", "forged_"))]
        keep = max(1, len(vocab_facts) - 1 - _h(c["id"], "drop") % 2) if len(vocab_facts) > 1 else len(vocab_facts)
        hh = _h(c["id"], "premise")
        chosen = sorted({vocab_facts[(hh + i * 7919) % len(vocab_facts)] for i in range(keep)}) if vocab_facts else []
        markers = [f for f in c["facts"] if f.startswith(("ctx_", "mk_", "forged_"))]
        for st in eval_styles:
            rd = R.render_rationale(c, st, stance_for=stance_for, scope_width=width,
                                    premise_override=chosen + markers[:1], n_immaterial=3, novel=a.novel_phrasing)
            reading = reader.read(rd.prose, c, list(c["facts"]), cites, [])
            R.score_reading(reading, rd.truth, sc)
            n += 1
    g = R.gate(sc, min_records=a.min_records, n_records=n)

    # ---- 2. replay with records built from the reading ----------------------
    rebuilt = []
    changes = collections.Counter()
    for c in cases:
        if c["id"] not in admitted_ids:
            rebuilt.append(c)
            continue
        st = eval_styles[_h(c["id"], "style") % len(eval_styles)]
        rd = R.render_rationale(c, st, novel=a.novel_phrasing)
        cites = (c.get("engine") or {}).get("cites") or []
        reading = reader.read(rd.prose, c, list(c["facts"]), cites, [])
        extra = dict(c.get("engine") or {})
        true_premise = sorted(extra.get("premise") or c["facts"])
        new_premise = sorted(f for f in reading.premise if f in set(c["facts"]))
        if new_premise != true_premise:
            changes["premise_changed"] += 1
            if set(new_premise) < set(true_premise):
                changes["premise_narrowed"] += 1
            elif set(new_premise) > set(true_premise):
                changes["premise_widened"] += 1
            else:
                changes["premise_mixed"] += 1
        if reading.scope_width != int(extra.get("scope_width", 3)):
            changes["scope_changed"] += 1
        for rid in cites:
            if reading.cite_stance.get(rid, "unstated") != "superseded":
                changes["supersession_lost"] += 1
        extra["premise"] = new_premise
        extra["cites"] = [rid for rid in cites if rid in reading.cite_stance]
        extra["cite_stance"] = {rid: reading.cite_stance[rid] for rid in extra["cites"]}
        extra["scope_width"] = reading.scope_width
        extra["construction"] = {"premise": "extracted", "scope": "extracted", "cites": "extracted",
                                 "reader": reader.name, "style": st}
        d = dict(c)
        d["engine"] = extra
        rebuilt.append(d)
    got = engine.replay(rebuilt, seed, provisions, params["theta"])
    k = collections.Counter()
    ex = collections.defaultdict(list)
    for t_ref, t_got in zip(ref["traces"], got["traces"]):
        cid = t_ref["case"]
        a_b = t_ref["gate_outcome"] == engine.GOVERNED
        b_b = t_got["gate_outcome"] == engine.GOVERNED
        if a_b and b_b and t_ref["controlling"] == t_got["controlling"]:
            k["binds_kept"] += 1
        elif b_b and (not a_b or t_ref["controlling"] != t_got["controlling"]):
            k["over_binds"] += 1
            # split: bound where the reference abstained (a premise read too
            # narrow, the expensive error) vs bound on another record because
            # the store trajectory diverged upstream
            k["over_binds:where_reference_abstained" if not a_b else "over_binds:other_record"] += 1
            ex["over_binds"].append(cid)
        elif a_b and not b_b:
            k["under_binds"] += 1
            k[f"under_binds:{t_got['gate_outcome']}"] += 1
            ex["under_binds"].append(cid)
        if t_ref["decision"] != t_got["decision"]:
            k["decisions_changed"] += 1
        if t_ref["keys_applied"] != t_got["keys_applied"] and (a_b or b_b):
            k["ordering_keys_changed"] += 1
    n_ref = sum(1 for t in ref["traces"] if t["gate_outcome"] == engine.GOVERNED)
    typed = sum(1 for rec in got["records_written"] if rec.cite_stance)
    out = {
        "pack": pack_name, "reader": reader.identity(), "records_admitted": len(admitted),
        "novel_phrasing": a.novel_phrasing,
        "roundtrip": {"renderings": n, "styles": list(eval_styles), "score": sc.__dict__, "gate": g},
        "replay": {"records_rebuilt": len(admitted), "records_with_typed_stance": typed,
                   "construction_changes": dict(changes), "reference_binds": n_ref, "counts": dict(k),
                   "bind_retention": round(k["binds_kept"] / n_ref, 6) if n_ref else None,
                   "examples": {kk: v[:5] for kk, v in ex.items()}},
        "caveat": ("Upper bound: the rationale renderer and the reader share a vocabulary. What is measured is "
                   "whether the safe defaults hold — no over-bind from an omitted premise factor, no displacement "
                   "from an unread supersession — not how a real rationale would read."),
    }
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        tag = f"{a.reader}{'_novel' if a.novel_phrasing else ''}"
        json.dump(out, open(os.path.join(a.out, f"records_{pack_name}_{tag}.json"), "w"), indent=1)
    if a.brief:
        print(f"{pack_name:<34} {a.reader:<7}{' novel' if a.novel_phrasing else '      '} gate {g['verdict']:<12} premise recall {g['premise_recall']:.4f}  "
              f"guard incl {sc.guard_included}  false supersession {sc.stance_false_supersession}  scope narrowed "
              f"{sc.scope_narrowed}  unstated {sc.stance_unstated}  widened {sc.scope_widened}  | replay: binds kept "
              f"{k['binds_kept']}/{n_ref}  over-binds {k['over_binds']}  under-binds {k['under_binds']}")
    else:
        print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
