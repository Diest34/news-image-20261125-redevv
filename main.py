#!/usr/bin/env python3
"""Entry for make.fun news-image-20261125.

Copies the bundled front-page image to the harness output path.
The image sums up the world news of Wednesday, 25 November 2026:
the Houthis threatening Jeddah's ports as the Saudi-led coalition
strikes Hodeidah, the Brooklyn jury convicting Huawei on 10 of 12
counts, gunmen holding 25 hostage in a Cartagena supermarket,
Zelensky accusing the U.S. of blocking paid missile deliveries,
and Germany forecasting a record one-trillion-euro tax haul.

Runs with no network and writes identical bytes on every run.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
