# results/

Reports only — the JSON summaries each stage prints with `--out`. The facts
snapshots (`facts_extracted_*.json`, ~23 MB each) and the calibration
readings (`readings_*.jsonl`) that the same runs write are **not** kept here;
`run_roundtrip.py <pack> --backend cued --out DIR` regenerates them in about
twenty seconds per pack. Every figure in `../README.md` is read from these
files; corpus 2.1.0 (release 5.14.0).
