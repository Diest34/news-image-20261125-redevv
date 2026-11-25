#!/usr/bin/env python3
"""News Image — 25 November 2026.

Reproduces this entry's image: the program takes the entry artwork that
ships alongside it in the repository and places an exact copy at
``/output/entry.png``. Nothing about the picture is generated or altered
here; the script exists so the entry can be rebuilt deterministically and
so the delivered file can be checked byte for byte.

Usage:
    python3 main.py
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path


SOURCE_NAME = "entry.png"
OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.png"

# The eight magic bytes every PNG file starts with.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME

    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1

    with source.open("rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            print(f"error: {source} is not a PNG file", file=sys.stderr)
            return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(source, OUTPUT_PATH)

    source_hash = sha256_of(source)
    output_hash = sha256_of(OUTPUT_PATH)
    if source_hash != output_hash:
        print(
            f"error: hash mismatch after copy "
            f"({source_hash} != {output_hash})",
            file=sys.stderr,
        )
        return 1

    size = OUTPUT_PATH.stat().st_size
    print(f"wrote {OUTPUT_PATH} ({size} bytes, sha256 {output_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
