#!/usr/bin/env python3
"""Preview-only original audio + ripple wallpaper. Does NOT patch iOS sound files."""
from pathlib import Path
import math
import wave
import struct
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"build"/"extras"
OUT.mkdir(parents=True,exist_ok=True)
rate=24000
sounds={"lock":([560,440],0.21),"unlock":([420,660],0.23),"charge":([650,875,1100],0.32)}
for name,(pitches,duration) in sounds.items():
    frames=bytearray()
    for n in range(int(rate*duration)):
        t=n/rate
        index=min(int(t/duration*len(pitches)),len(pitches)-1)
        f=pitches[index]
        env=min(1,t/.009)*min(1,max(0,(duration-t)/.11))**1.6
        wavev=(math.sin(2*math.pi*f*t)+0.14*math.sin(4*math.pi*f*t))*0.20*env
        frames.extend(struct.pack("<h",int(32767*wavev)))
    with wave.open(str(OUT/(name+".wav")),"wb") as fh:
        fh.setnchannels(1);fh.setsampwidth(2);fh.setframerate(rate);fh.writeframes(frames)
width,height=1080,1920
img=Image.new("RGB",(width,height))
px=img.load()
for y in range(height):
    yy=y/height
    for x in range(width):
        xx=x/width
        wavev=math.sin(yy*25+math.sin(xx*4+yy)*.9)*9+math.sin(yy*67+math.cos(xx*7)*2)*3
        light=max(0,1-((xx-.5)**2*1.6+(yy-.26)**2*.7))
        px[x,y]=(int(8+12*light+wavev*.22),int(48+30*light+wavev*.65),int(85+48*light+wavev))
img.save(OUT/"Retro6-Waves-1080x1920.jpg",quality=91,optimize=True)
print("Generated 3 original preview-only sounds and a 1080×1920 wallpaper.")
