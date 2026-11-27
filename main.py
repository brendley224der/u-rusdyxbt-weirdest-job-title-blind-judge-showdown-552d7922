#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes a single job title (60 characters at most) to /output/entry.txt.

The title is a real-sounding job with one hilariously specific twist:
a professional mourner -- a genuine occupation in many cultures --
hired not for people, but for strangers' goldfish funerals. Tiny
coffins, a eulogy for a fish, a stranger paying for the ceremony:
specific enough to picture, absurd enough to land on first read.

Pure standard library. Deterministic: the output is a fixed string,
so every run writes byte-identical content.
"""

import os
import sys

TITLE = "Professional Mourner for Strangers' Goldfish Funerals"

# Sanity-guard the contract: 1..60 characters, not only whitespace.
assert 1 <= len(TITLE) <= 60, "title must be 1-60 characters"
assert TITLE.strip(), "title must not be only whitespace"


def output_dir() -> str:
    """Grader sandbox mounts /output; fall back to ./output locally."""
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main() -> int:
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TITLE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
