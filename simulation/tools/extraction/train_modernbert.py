#!/usr/bin/env python3
"""Fine-tune a ModernBERT multi-label head over a pack's factor vocabulary.

    python3 tools/extraction/train_modernbert.py <pack-dir> --out runs/vetpoc-mbl
        [--backbone modernbert-large] [--control] [--epochs 3] [--train-fraction 0.6]

Runs in the MODEL environment, never the packs':

    python3 -m venv .venv-extract && .venv-extract/bin/pip install -r tools/extraction/requirements-model.txt

Training data is rendered from the pack's own cases in the TRAINING styles
only (`render.split_styles`); the guard styles and the held-out styles are
never seen, so `run_roundtrip.py --backend modernbert --checkpoint <out>` is a
measurement and not a memory test. Each document is labelled with the factors
the case carries; the guard sentences in the same document are therefore
negatives for the factors they name, which is how the head learns that a
factor's words are not the factor.

Two things a stock recipe does not do, both because they were measured:
`add_prefix_space` comes from the backbone (the ModernBERT tokenizer prepends
whitespace on a plain call, costing ~1.7 F1 on token tasks; recorded per
backbone and applied here for consistency with the extraction path), and
`--control` trains modernbert-base identically so that any gain from scale is
a difference, not a citation. The backbone revision is a pinned commit and is
written into the checkpoint's `dj_extraction.json` beside the label map.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extraction import backbones as BB  # noqa: E402
from extraction import render, snapshot  # noqa: E402


def build_rows(pack_dir: str, train_fraction: float, limit: int | None, task: str = "facts"):
    """Training rows for one of four heads, all rendered from computed truth in
    the TRAINING styles and the cue phrasings only.

      facts    multi-label over the pack vocabulary; text = change description
      premise  multi-label over the pack vocabulary; text = rationale; label =
               the factors the holding turned on (inclusion-biased at inference)
      stance   single-label {superseded, followed, distinguished}; text = the
               citing sentence
      scope    single-label {1..5}; text = rationale
    """
    import hashlib
    from extraction import records as R
    engine, rb, params, cases, seed, provisions = snapshot.load_pack(pack_dir)
    by_id = {p["id"]: p for p in rb["provisions"]}
    vocab_all = sorted({f for p in rb["provisions"] for k in ("comply", "violate") for f in p["factors"][k]})
    train_styles, _ = render.split_styles(train_fraction)
    rows = []

    def h(*p):
        return int(hashlib.sha256("\x1f".join(str(x) for x in p).encode()).hexdigest(), 16)

    if task == "facts":
        relevant = [c for c in cases if c.get("rules")]
        if limit:
            relevant = relevant[:limit]
        for c in relevant:
            vocab = snapshot.vocabulary_for(c, by_id)
            for st in train_styles:
                rd = render.render(c, vocab, st)
                rows.append({"id": f"{c['id']}:{st}", "text": rd.prose,
                             "labels": sorted(f for f, v in rd.truth.items() if v)})
        return vocab_all, rows, list(train_styles)

    ref = engine.replay(cases, seed, provisions, params["theta"])
    admitted = {t["case"] for t in ref["traces"] if t["admitted"]}
    relevant = [c for c in cases if c["id"] in admitted]
    if limit:
        relevant = relevant[:limit]
    for c in relevant:
        cites = (c.get("engine") or {}).get("cites") or []
        stance_for = {rid: R.STANCES[h(c["id"], rid, "train") % 3] for rid in cites}
        width = 1 + h(c["id"], "scope", "train") % 5
        vf = [f for f in c["facts"] if not f.startswith(("ctx_", "mk_", "forged_"))]
        keep = max(1, len(vf) - 1 - h(c["id"], "drop", "train") % 2) if len(vf) > 1 else len(vf)
        hh = h(c["id"], "premise", "train")
        chosen = sorted({vf[(hh + i * 7919) % len(vf)] for i in range(keep)}) if vf else []
        for st in train_styles:
            rd = R.render_rationale(c, st, stance_for=stance_for, scope_width=width, premise_override=chosen,
                                    n_immaterial=3)
            if task == "premise":
                rows.append({"id": f"{c['id']}:{st}", "text": rd.prose,
                             "labels": [f for f in rd.truth.premise if f in set(vocab_all)]})
            elif task == "scope":
                rows.append({"id": f"{c['id']}:{st}", "text": rd.prose, "label": str(width)})
            elif task == "stance":
                for rid, stc in rd.truth.cites.items():
                    for sent in rd.prose.split("\n"):
                        if rid in sent:
                            rows.append({"id": f"{c['id']}:{st}:{rid}", "text": sent, "label": stc})
    labels = (vocab_all if task == "premise" else sorted(R.STANCES) if task == "stance"
              else [str(i) for i in range(1, 6)])
    return labels, rows, list(train_styles)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pack")
    ap.add_argument("--out", required=True)
    ap.add_argument("--backbone", default=BB.DEFAULT_BACKBONE, choices=sorted(BB.BACKBONES))
    ap.add_argument("--control", action="store_true", help="also train modernbert-base identically")
    ap.add_argument("--epochs", type=float, default=3.0)
    ap.add_argument("--lr", type=float, default=3e-5)
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--max-length", type=int, default=512)
    ap.add_argument("--train-fraction", type=float, default=0.6)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--seed", type=int, default=20260910)
    ap.add_argument("--export-only", action="store_true", help="write the JSONL training rows and stop (no torch)")
    ap.add_argument("--task", default="facts", choices=("facts", "premise", "stance", "scope"))
    a = ap.parse_args(argv)

    labels, rows, train_styles = build_rows(a.pack, a.train_fraction, a.limit, a.task)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "train_rows.jsonl"), "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    meta = {"pack": os.path.basename(os.path.abspath(a.pack)), "task": a.task, "labels": labels, "n_rows": len(rows),
            "train_styles": train_styles, "rows_sha256": hashlib.sha256(
                "".join(json.dumps(r) for r in rows).encode()).hexdigest()}
    json.dump(meta, open(os.path.join(a.out, "dj_extraction.json"), "w"), indent=1)
    print(f"{a.task}: {len(rows)} training rows over {len(labels)} labels, styles {train_styles}")
    if a.export_only:
        return 0

    try:
        import numpy as np
        import torch
        from transformers import (AutoModelForSequenceClassification, AutoTokenizer, Trainer,
                                  TrainingArguments)
    except ImportError as e:
        print("training needs torch and transformers in a separate environment:\n"
              "  python3 -m venv .venv-extract\n"
              "  .venv-extract/bin/pip install -r tools/extraction/requirements-model.txt\n"
              f"({e})", file=sys.stderr)
        return 2

    l2i = {v: i for i, v in enumerate(labels)}

    def train_one(bb_name: str, out_dir: str):
        bb = BB.get(bb_name)
        BB.require_pinned(bb)
        torch.manual_seed(a.seed)
        tok = AutoTokenizer.from_pretrained(bb.repo, revision=bb.revision, add_prefix_space=bb.add_prefix_space)
        multi = a.task in ("facts", "premise")
        model = AutoModelForSequenceClassification.from_pretrained(
            bb.repo, revision=bb.revision, num_labels=len(labels),
            problem_type="multi_label_classification" if multi else "single_label_classification",
            id2label={i: v for v, i in l2i.items()}, label2id=l2i)

        class DS(torch.utils.data.Dataset):
            def __len__(self):
                return len(rows)

            def __getitem__(self, i):
                r = rows[i]
                enc = tok(r["text"], truncation=True, max_length=a.max_length, padding="max_length")
                enc = {k: torch.tensor(v) for k, v in enc.items()}
                if multi:
                    y = np.zeros(len(labels), dtype=np.float32)
                    for f in r["labels"]:
                        y[l2i[f]] = 1.0
                    enc["labels"] = torch.tensor(y)
                else:
                    enc["labels"] = torch.tensor(l2i[r["label"]])
                return enc

        args = TrainingArguments(output_dir=out_dir, num_train_epochs=a.epochs, learning_rate=a.lr,
                                 per_device_train_batch_size=a.batch, seed=a.seed, save_strategy="no",
                                 logging_steps=50, report_to=[])
        Trainer(model=model, args=args, train_dataset=DS()).train()
        model.save_pretrained(out_dir)
        tok.save_pretrained(out_dir)
        json.dump({**meta, "backbone": bb.name, "backbone_repo": bb.repo, "backbone_revision": bb.revision,
                   "add_prefix_space": bb.add_prefix_space, "epochs": a.epochs, "lr": a.lr, "seed": a.seed},
                  open(os.path.join(out_dir, "dj_extraction.json"), "w"), indent=1)

    train_one(a.backbone, a.out)
    if a.control and a.backbone != "modernbert-base":
        train_one("modernbert-base", a.out + "-control")
    return 0


if __name__ == "__main__":
    sys.exit(main())
