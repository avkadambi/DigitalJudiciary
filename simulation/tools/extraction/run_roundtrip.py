#!/usr/bin/env python3
"""Measure characterisation as its own stage on one pack.

    python3 tools/extraction/run_roundtrip.py <pack-dir> [--backend cued|literal|deterministic|modernbert|nli]
        [--checkpoint DIR] [--target-precision 0.98] [--train-fraction 0.6] [--out DIR]

Three passes, in this order and for these reasons:

  1. CALIBRATE on the training styles. Render every gate-relevant case in each
     training style, extract with a floor low enough that nothing abstains,
     collect (confidence, correct) over the assertions, and fit the lowest
     floor whose precision meets the target. The floor is fitted on styles the
     evaluation never sees.
  2. EVALUATE on the held-out styles, guard styles included, with the fitted
     floor. Report assertion precision, recall of carried factors, the seven
     verdicts by style, and the acceptance gate (guard assertions fail at any
     n; too few assertions is inconclusive).
  3. SNAPSHOT and REPLAY. Give every case one held-out style (deterministic),
     extract it into three-valued facts, replay the pack's engine over the
     snapshot and compare each trace to the reference. This is epsilon: the
     share of reference binds the extracted facts still reach, and the share
     that break with cause premise_not_established rather than silently.

Nothing here needs torch unless --backend modernbert is asked for.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extraction import abstain, backends, render, roundtrip, snapshot  # noqa: E402


def _style_for(case_id: str, styles) -> str:
    h = int(hashlib.sha256(case_id.encode()).hexdigest(), 16)
    return styles[h % len(styles)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("--backend", default="cued", choices=("cued", "literal", "deterministic", "modernbert", "nli"))
    ap.add_argument("--checkpoint", default=None)
    ap.add_argument("--backbone", default=None)
    ap.add_argument("--target-precision", type=float, default=0.98)
    ap.add_argument("--train-fraction", type=float, default=0.6)
    ap.add_argument("--min-assertions", type=int, default=300)
    ap.add_argument("--limit", type=int, default=None, help="first N gate-relevant cases (smoke runs)")
    ap.add_argument("--out", default=None, help="directory for report, readings and snapshot")
    ap.add_argument("--brief", action="store_true", help="one summary line instead of the JSON report")
    a = ap.parse_args(argv)

    engine, rb, params, cases, seed, provisions = snapshot.load_pack(a.pack)
    by_id = {p["id"]: p for p in rb["provisions"]}
    pack_name = os.path.basename(os.path.abspath(a.pack))
    if a.backend == "literal":
        be = backends.LiteralMatchBackend()
    elif a.backend == "deterministic":
        be = backends.DeterministicBackend()
    elif a.backend == "modernbert":
        if not a.checkpoint:
            ap.error("--backend modernbert needs --checkpoint (a fine-tuned head; see train_modernbert.py)")
        be = backends.ModernBERTBackend(a.checkpoint, a.backbone or backends.BB.DEFAULT_BACKBONE)
    elif a.backend == "nli":
        be = backends.NLIZeroShotBackend(a.checkpoint, a.backbone or "modernbert-large-zeroshot-v2.0")
    else:
        be = backends.CuedLiteralBackend()

    relevant = [c for c in cases if c.get("rules")]
    if a.limit:
        relevant = relevant[: a.limit]
    train_styles, eval_styles = render.split_styles(a.train_fraction)

    # ---- 1. calibrate -------------------------------------------------------
    permissive = abstain.Calibration(pack_name, 1.0, abstain.MIN, {"*": 1e-6}, a.target_precision, 0)
    scored_train = []
    for c in relevant:
        vocab = snapshot.vocabulary_for(c, by_id)
        for st in train_styles:
            rd = render.render(c, vocab, st)
            ex = snapshot.extract_case(rd.prose, c, vocab, be, permissive)
            scored_train += roundtrip.score(ex, rd)
    rows = roundtrip.readings(scored_train)
    floor, prec_at, rec_at = abstain.floor_for_precision([(r["confidence"], r["correct"]) for r in rows],
                                                         a.target_precision)
    refused = prec_at < a.target_precision
    cal = abstain.Calibration(pack_name, 1.0, abstain.MIN, {"*": max(floor, 1e-6)}, a.target_precision, len(rows))

    # ---- 2. evaluate on held-out styles -------------------------------------
    scored_eval = []
    for c in relevant:
        vocab = snapshot.vocabulary_for(c, by_id)
        for st in eval_styles:
            rd = render.render(c, vocab, st)
            ex = snapshot.extract_case(rd.prose, c, vocab, be, cal)
            scored_eval += roundtrip.score(ex, rd)
    rep = roundtrip.report(scored_eval, train_styles=train_styles, min_assertions=a.min_assertions,
                           target_precision=a.target_precision)

    # ---- 3. snapshot + replay -----------------------------------------------
    extracted = {}
    style_used = {}
    for c in relevant:
        vocab = snapshot.vocabulary_for(c, by_id)
        st = _style_for(c["id"], eval_styles)
        rd = render.render(c, vocab, st)
        extracted[c["id"]] = snapshot.extract_case(rd.prose, c, vocab, be, cal, {"style": st, "pack": pack_name})
        style_used[st] = style_used.get(st, 0) + 1
    replay = snapshot.replay_with_snapshot(engine, cases, extracted, seed, provisions, params["theta"])
    cov = {}
    for e in extracted.values():
        for f in e.fields:
            cov[f.status] = cov.get(f.status, 0) + 1

    out = {
        "pack": pack_name, "backend": be.identity(), "cases_extracted": len(relevant),
        "calibration": {"train_styles": list(train_styles), "readings": len(rows), "floor": floor,
                        "precision_at_floor": round(prec_at, 6), "recall_at_floor": round(rec_at, 6),
                        "target_precision": a.target_precision,
                        "refused": refused,
                        "note": ("no floor reaches the target on the training styles; the extractor is "
                                 "refused, and the figures below are reported for diagnosis only") if refused else ""},
        "roundtrip": rep.as_dict(),
        "snapshot": {"styles": style_used, "status_counts": cov},
        "replay_against_reference": replay,
        "epsilon": {
            "definition": ("The Evaluator's characterisation fidelity, measured rather than assumed: the share of "
                           "reference binds the extracted facts still reach (bind_retention), and of the binds that "
                           "break, the share that break with the cause named (premise_not_established) rather than "
                           "by a changed disposition."),
            "bind_retention": replay["bind_retention"],
            "decision_agreement": replay["decision_agreement"],
            "broken_binds_named_as_silence": (
                round(replay["counts"].get("binds_broken_by_silence", 0) /
                      max(1, replay["counts"].get("binds_broken_by_silence", 0) + replay["counts"].get("binds_broken_otherwise", 0)), 6)),
            "false_binds": replay["counts"].get("false_binds", 0),
            "floors_missed": replay["counts"].get("floors_missed", 0),
            "floors_referred_on_silence": replay["counts"].get("floors_referred_on_silence", 0),
        },
        "caveat": roundtrip.UPPER_BOUND_CAVEAT,
    }
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        json.dump(out, open(os.path.join(a.out, f"roundtrip_{pack_name}_{a.backend}.json"), "w"), indent=1)
        roundtrip.write_readings(scored_train, os.path.join(a.out, f"readings_{pack_name}_{a.backend}.jsonl"))
        snapshot.write_snapshot(os.path.join(a.out, f"facts_extracted_{pack_name}_{a.backend}.json"), extracted,
                                {"pack": pack_name, "backend": be.identity(), "calibration": cal.as_dict(),
                                 "styles": style_used, "facts_source": "extracted"})
    if a.brief:
        e = out["epsilon"]
        c = replay["counts"]
        print(f"{pack_name:<34} {a.backend:<7} gate {rep.gate['verdict']:<12} precision "
              f"{(rep.assertion_precision or 0):.4f}  bind retention {e['bind_retention']:.3f}  "
              f"floors missed {e['floors_missed']}  referred on silence {e['floors_referred_on_silence']}  "
              f"records withheld {c.get('records_withheld', 0)}  bound where reference abstained "
              f"{c.get('false_binds:where_reference_abstained', 0)}")
        return 0
    print(json.dumps({k: out[k] for k in ("pack", "backend", "calibration", "epsilon")}, indent=1))
    print(json.dumps({"roundtrip_gate": rep.gate, "assertion_precision": rep.as_dict()["assertion_precision"],
                      "recall": rep.as_dict()["recall_of_carried_factors"], "by_verdict": rep.by_verdict,
                      "replay_counts": replay["counts"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
