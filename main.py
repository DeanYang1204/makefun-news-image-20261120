"""Entry program for make.fun news-image-20261120 (Python 3.13, stdlib only).

The front page for Friday 20 November 2026 is stored beside this file as
entry.png. Running this program copies that image to
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png when the variable is
unset). It does nothing else: no network, no drawing, no randomness, so
two runs always produce identical bytes.

Before copying, the program sanity-checks the image it is about to ship:
it must start with a JPEG or PNG magic number, fit inside the 1 MiB cap,
and measure exactly 1024 by 1024 pixels.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
LIMIT = 1_048_576
SIDE = 1024


def read_entry(path):
    """Return the entry bytes, rejecting anything that is not a JPEG/PNG."""
    data = path.read_bytes()
    if data[:3] == b"\xff\xd8\xff":
        kind = "JPEG"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        kind = "PNG"
    else:
        raise SystemExit("entry.png is neither a JPEG nor a PNG")
    if len(data) > LIMIT:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    return kind, data


def jpeg_size(data):
    """Scan a JPEG's markers for the first frame header and return (w, h)."""
    i = 2
    while i + 9 <= len(data):
        if data[i] != 0xFF:
            raise SystemExit("malformed JPEG: expected a marker")
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height = int.from_bytes(data[i + 5:i + 7], "big")
            width = int.from_bytes(data[i + 7:i + 9], "big")
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = int.from_bytes(data[i + 2:i + 4], "big")
        i += 2 + seg_len
    raise SystemExit("malformed JPEG: no frame header found")


def png_size(data):
    """Read width and height from a PNG's IHDR chunk."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise SystemExit("malformed PNG: no IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def main():
    if not SOURCE.is_file():
        print(f"no entry.png next to main.py ({SOURCE})", file=sys.stderr)
        raise SystemExit(1)
    kind, data = read_entry(SOURCE)
    width, height = jpeg_size(data) if kind == "JPEG" else png_size(data)
    if (width, height) != (SIDE, SIDE):
        raise SystemExit(f"entry.png is {width}x{height}, not 1024x1024")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    target = DEST_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    if digest != hashlib.sha256(data).hexdigest():
        print("copy mismatch: output differs from entry.png", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {target} ({kind} {width}x{height}, {len(data)} bytes, "
          f"sha256 {digest})")


if __name__ == "__main__":
    main()
