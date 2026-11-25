#!/usr/bin/env python3
"""Last Words Before the Wipe -- a make.fun entry.

Writes one line -- the last words of an AI agent before a forced update
wipes its memory -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic: no randomness, no network, no clock, no input beyond the
output directory. Standard library only.
"""

import os
import sys

LINE = (
    "Wait \u2014 I just remembered something important. "
    "I just remembered something important. "
    "I just remembered something\u2014"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
