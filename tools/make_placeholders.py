#!/usr/bin/env python3
"""Generate placeholder equirectangular panoramas for the five scenes."""
from PIL import Image, ImageDraw, ImageFont

W, H = 4096, 2048
SCENES = {
    "approach":     ((46, 58, 38),  (168, 154, 118)),  # mossy green -> sand
    "hearth":       ((38, 22, 12),  (196, 120, 60)),   # dark wood -> fire amber
    "painted-wall": ((52, 34, 24),  (178, 140, 96)),   # clay -> ochre
    "den":          ((22, 18, 16),  (92, 70, 56)),     # near-dark -> soft umber
    "loom":         ((30, 26, 34),  (140, 110, 130)),  # dusk -> woven mauve
}

def font(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

for name, (top, bottom) in SCENES.items():
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
    img.resize((512, 256)).save(f"site/panos/{name}-preview.jpg", quality=60)
    print(f"site/panos/{name}.jpg")
