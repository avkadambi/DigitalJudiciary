"""`python -m app` / `dj-serve` — start the single-container service (see serve.py)."""
from __future__ import annotations

import os
import runpy
import sys


def main() -> None:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, root)
    runpy.run_path(os.path.join(root, "serve.py"), run_name="__main__")


if __name__ == "__main__":
    main()
