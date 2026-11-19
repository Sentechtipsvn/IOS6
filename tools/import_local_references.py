#!/usr/bin/env python3
"""LOCAL-ONLY iOS 6 reference image importer.

Consumes a copy/ZIP of the user's reference fork, overlays matching icon PNGs
onto a separate SnowBoard theme, and NEVER uploads/exposes these raster images.
This script does not imply a grant of copyright or trademark permissions.
"""
import argparse
import io
import json
import plistlib
import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCE_THEME = ROOT / "build" / "Sentech Retro 6.theme"
TARGET_THEME = ROOT / "build" / "iOS 6 Reference Local.theme"
MAP_FILE = ROOT / "data" / "reference-map.json"


class SourceLibrary:
    def __init__(self, value):
        self.path = Path(value).expanduser().resolve()
        if not self.path.exists():
            raise FileNotFoundError(self.path)
        self.zipped = self.path.is_file()
        self.archive = zipfile.ZipFile(self.path) if self.zipped else None
        if self.archive:
            self.filenames = self.archive.namelist()

    def get(self, relpath):
        path = Path(relpath)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("Unsafe reference source path: " + relpath)
        normal = path.as_posix()
        if self.archive:
            candidates = [p for p in self.filenames if p == normal or p.endswith("/" + normal)]
            if len(candidates) != 1:
                return None
            with self.archive.open(candidates[0]) as f:
                return f.read()
        p = (self.path / path).resolve()
        if not p.is_relative_to(self.path):
            raise ValueError("Reference escapes source folder: " + relpath)
        return p.read_bytes() if p.is_file() else None

    def close(self):
        if self.archive:
            self.archive.close()


def normalized_icon(data, size=180):
    with Image.open(io.BytesIO(data)) as original:
        im = ImageOps.exif_transpose(original).convert("RGBA")
        im = ImageOps.fit(im, (size, size), method=Image.Resampling.LANCZOS)
    # Apple-era screenshots often have jpg backgrounds at the corners.
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=32, fill=255)
    im.putalpha(ImageChops.multiply(im.getchannel("A"), mask))
    return im


def main():
    parser = argparse.ArgumentParser(description="Prepare a local-only reference theme from a locally held reference archive or folder.")
    parser.add_argument("--source", required=True, help="Downloaded iOS-6-Icons ZIP or extracted directory")
    parser.add_argument("--limit", type=int, default=0, help="Optional first N icons for smoke testing")
    args = parser.parse_args()
    if not SOURCE_THEME.exists():
        raise SystemExit("Generate original theme first: python3 tools/generate.py")
    if TARGET_THEME.exists():
        shutil.rmtree(TARGET_THEME)
    shutil.copytree(SOURCE_THEME, TARGET_THEME)
    info = TARGET_THEME / "Info.plist"
    with info.open("rb") as f:
        props = plistlib.load(f)
    props["CFBundleName"] = "iOS 6 Reference (Local)"
    with info.open("wb") as f:
        plistlib.dump(props, f)
    icons = TARGET_THEME / "IconBundles"
    mapping = json.loads(MAP_FILE.read_text(encoding="utf-8"))["mappings"]
    library = SourceLibrary(args.source)
    imported, missing = [], []
    try:
        for item in mapping[:args.limit or None]:
            source = library.get(item["source_path"])
            if source is None:
                missing.append(item["app"])
                continue
            img = normalized_icon(source)
            for suffix in ("-large.png", ".png"):
                img.save(icons / (item["bundle_id"] + suffix), optimize=True)
            imported.append(item["app"])
    finally:
        library.close()
    (TARGET_THEME / "LOCAL_REFERENCE_NOTICE.txt").write_text(
        "Local reference test only. Third-party and Apple assets are owned by their respective rights holders. "
        "Do not redistribute this theme or upload its contents to public builds.\n", encoding="utf-8"
    )
    print(f"Imported {len(imported)} locally held icon references; missing {len(missing)}.")
    print("Missing:", ", ".join(missing) if missing else "none")
    print("Output:", TARGET_THEME)
    if not imported:
        sys.exit("Nothing imported: confirm --source points to the extracted fork or ZIP.")


if __name__ == "__main__":
    main()
