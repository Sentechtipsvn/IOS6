#!/usr/bin/env python3
"""SVG source -> SnowBoard IconBundles PNG, no Apple assets."""
import json
from pathlib import Path
import cairosvg
from PIL import Image
from io import BytesIO
ROOT=Path(__file__).resolve().parents[1]
APP=json.loads((ROOT/"data"/"apps.json").read_text(encoding="utf-8"))
SRC=ROOT/"assets"/"icons"
OUTPUT=ROOT/"build"/"Sentech Retro 6.theme"
ICONS=OUTPUT/"IconBundles"
ICONS.mkdir(parents=True,exist_ok=True)
(OUTPUT/"Info.plist").write_text('<?xml version="1.0" encoding="UTF-8"?><plist version="1.0"><dict><key>CFBundleName</key><string>Sentech Retro 6</string></dict></plist>')
assert len({a["bundle_id"] for a in APP})==len(APP)
for a in APP:
    source=SRC/(a["id"]+".svg")
    data=cairosvg.svg2png(url=str(source),output_width=540,output_height=540)
    image=Image.open(BytesIO(data)).convert("RGBA").resize((180,180),Image.Resampling.LANCZOS)
    for suffix in ("-large.png",".png"):
        image.save(ICONS/(a["bundle_id"]+suffix),optimize=True)
print("Rendered",len(APP),"original icon designs /",len(APP)*2,"PNG files")
