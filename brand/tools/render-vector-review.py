#!/usr/bin/env python3
"""Render clean or diagnostic source-vs-vector QA for locked Agnir artwork.

Default output is Principal-facing CLEAN review: no debug boxes or crop overlays.
Use --diagnostic for engineering output with detected artwork bounds.

This tool never modifies brand artwork.
"""
from __future__ import annotations
import argparse, io
from pathlib import Path
import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CROPS = {
    "primary-mark": (60, 145, 425, 400),
    "wordmark": (575, 140, 860, 250),
    "horizontal-lockup": (980, 140, 1410, 330),
    "vertical-lockup": (610, 305, 810, 455),
}
LABELS = {
    "primary-mark": "Primary mark",
    "wordmark": "Wordmark",
    "horizontal-lockup": "Horizontal lockup",
    "vertical-lockup": "Vertical lockup",
}

def _font(size: int, bold: bool = False):
    path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    return ImageFont.truetype(str(path), size) if path.exists() else ImageFont.load_default()

def _render_svg(path: Path, width: int = 1400) -> Image.Image:
    # url= preserves relative references for candidate lockups.
    data = cairosvg.svg2png(url=str(path), output_width=width)
    rgba = Image.open(io.BytesIO(data)).convert("RGBA")
    canvas = Image.new("RGBA", rgba.size, "white")
    canvas.alpha_composite(rgba)
    return canvas.convert("RGB")

def _art_bbox(key: str, image: Image.Image):
    arr = np.asarray(image.convert("RGB"), dtype=np.int16)
    dist = np.linalg.norm(255 - arr, axis=2)
    black = arr.max(axis=2) < 190
    chroma = (arr.max(axis=2) - arr.min(axis=2)) > 5
    colored = (dist > 8) & chroma
    mask = colored if key == "primary-mark" else black if key == "wordmark" else (colored | black)
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return (0, 0, image.width, image.height)
    return (int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1))

def _contain(image: Image.Image, max_w: int, max_h: int):
    scale = min(max_w / image.width, max_h / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.Resampling.LANCZOS), scale

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--board", required=True, type=Path)
    p.add_argument("--primary-mark", required=True, type=Path)
    p.add_argument("--wordmark", required=True, type=Path)
    p.add_argument("--horizontal-lockup", required=True, type=Path)
    p.add_argument("--vertical-lockup", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--diagnostic", action="store_true", help="draw detected artwork bounds; never use as Principal-facing approval image")
    args = p.parse_args()

    vectors = {
        "primary-mark": args.primary_mark,
        "wordmark": args.wordmark,
        "horizontal-lockup": args.horizontal_lockup,
        "vertical-lockup": args.vertical_lockup,
    }
    board = Image.open(args.board).convert("RGB")
    page_w, left, gap, row_h, top = 1500, 60, 40, 355, 120
    col_w = (page_w - left * 2 - gap) // 2
    page_h = top + len(CROPS) * row_h + 80
    page = Image.new("RGB", (page_w, page_h), "white")
    draw = ImageDraw.Draw(page)
    mode = "Diagnostic" if args.diagnostic else "Clean"
    draw.text((60, 35), f"Agnir — {mode} Source vs Vector QA", font=_font(28, True), fill=(25,25,25))
    subtitle = "Blue = detected artwork bounds." if args.diagnostic else "No diagnostic bounds, no crop/cover, no debug overlays."
    draw.text((60, 76), subtitle, font=_font(13), fill=(70,70,70))

    for index, (key, crop) in enumerate(CROPS.items()):
        y0 = top + index * row_h
        draw.text((60, y0), f"{index+1}. {LABELS[key]}", font=_font(18, True), fill=(25,25,25))
        source = board.crop(crop)
        vector = _render_svg(vectors[key])
        for col, (kind, image) in enumerate((("SOURCE", source), ("VECTOR", vector))):
            px, py = 60 + col * (col_w + gap), y0 + 38
            panel_h = 250
            draw.rounded_rectangle((px, py, px + col_w, py + panel_h), radius=10, outline=(195,195,195), width=2)
            rendered, scale = _contain(image, col_w - 34, panel_h - 24)
            x = px + (col_w - rendered.width)//2
            y = py + (panel_h - rendered.height)//2
            page.paste(rendered, (x,y))
            if args.diagnostic:
                b = _art_bbox(key, image)
                sb = tuple(round(v * scale) for v in b)
                draw.rectangle((x+sb[0], y+sb[1], x+sb[2], y+sb[3]), outline=(52,120,246), width=2)
            draw.text((px+8, py+panel_h+10), kind, font=_font(13), fill=(45,45,45))

    footer = "Diagnostic images are engineering evidence only; Principal approval uses clean review output." if args.diagnostic else "Clean review output is suitable for Principal visual review; use --diagnostic separately for engineering bounds."
    draw.text((60, page_h-50), footer, font=_font(13), fill=(70,70,70))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    page.save(args.out)

if __name__ == "__main__":
    main()
