#!/usr/bin/env python3
"""Generate placeholder equirectangular panoramas for the five scenes.

With --previews-only, keep the existing site/panos/<id>.jpg files (e.g. real
Skybox AI panoramas) untouched and only regenerate the -preview.jpg files.
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 allow_abbrev=False)
parser.add_argument(
    "--previews-only", action="store_true",
    help="leave site/panos/<id>.jpg untouched; only regenerate -preview.jpg files")
args = parser.parse_args()
PREVIEWS_ONLY = args.previews_only

W, H = 4096, 2048
SCENES = {
    "approach":     ((46, 58, 38),  (168, 154, 118)),  # mossy green -> sand
    "hearth":       ((38, 22, 12),  (196, 120, 60)),   # dark wood -> fire amber
    "painted-wall": ((52, 34, 24),  (178, 140, 96)),   # clay -> ochre
    "den":          ((22, 18, 16),  (92, 70, 56)),     # near-dark -> soft umber
    "loom":         ((30, 26, 34),  (140, 110, 130)),  # dusk -> woven mauve
}

if PREVIEWS_ONLY:
    missing = [n for n in SCENES if not os.path.isfile(f"site/panos/{n}.jpg")]
    if missing:
        for n in missing:
            print(f"site/panos/{n}.jpg missing — generate it or run without "
                  "--previews-only", file=sys.stderr)
        sys.exit(1)

def font(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

for name, (top, bottom) in SCENES.items():
    if PREVIEWS_ONLY:
        img = Image.open(f"site/panos/{name}.jpg")
    else:
        img = Image.new("RGB", (W, H))
        px = img.load()
        for y in range(H):
            t = y / (H - 1)
            row = tuple(int(a + (b - a) * t) for a, b in zip(top, bottom))
            for x in range(W):
                px[x, y] = row
        d = ImageDraw.Draw(img)
        d.line([(0, H // 2), (W, H // 2)], fill=(200, 190, 180), width=2)
        label = name.replace("-", " ").upper() + " · PLACEHOLDER"
        f = font(56)  # longest label ~981px, fits the 1024px quarter spacing
        tw = d.textlength(label, font=f)
        for i in range(4):  # readable at any viewing direction
            d.text(((W * i / 4 + W / 8) - tw / 2, H // 2 - 140), label,
                   font=f, fill=(255, 245, 230))
        img.save(f"site/panos/{name}.jpg", quality=80)
        print(f"site/panos/{name}.jpg")
    img.resize((512, 256), resample=Image.LANCZOS).save(
        f"site/panos/{name}-preview.jpg", quality=60)
    if PREVIEWS_ONLY:
        print(f"site/panos/{name}-preview.jpg")
