"""
Assemble docs/explorer.html — the browsable case reporter.

The corpus payload is gzipped and base64-encoded into the page, so the artifact
is self-contained: no external data fetch, no CDN beyond the font stylesheet.
About 0.97 MB on the wire for 5,000 cases with their English explanations.

    python3 generator/build_explorer.py

Run build_docs.py first: this reads corpus/explorer_data.json.
"""

import base64
import gzip
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def main():
    with open(os.path.join(ROOT, "corpus", "explorer_data.json")) as fh:
        data = json.load(fh)
    # `why` duplicates a sentence already inside the English explanation.
    for c in data["cases"]:
        c.pop("why", None)
    raw = json.dumps(data, separators=(",", ":")).encode()
    payload = base64.b64encode(gzip.compress(raw, 9, mtime=0)).decode()

    head = open(os.path.join(HERE, "explorer", "head.html")).read()
    tail = open(os.path.join(HERE, "explorer", "tail.html")).read()
    page = head + '\n<script>window.__SEMIFAB__="' + payload + '";</script>\n' + tail

    out = os.path.join(ROOT, "docs", "explorer.html")
    with open(out, "w") as fh:
        fh.write(page)
    print(f"docs/explorer.html  {len(page):,} bytes "
          f"({len(raw):,} raw, {len(payload):,} encoded)")


if __name__ == "__main__":
    main()
