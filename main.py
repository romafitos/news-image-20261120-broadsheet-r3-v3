#!/usr/bin/env python3
"""Copy the pre-rendered front page to the output directory.

The page itself is frontpage.html, rendered to entry.png (1024x1024)
with headless Chromium; the render is byte-identical across runs.
Standard library only; no network.
"""
import os
import shutil


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    shutil.copyfile(src, os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
