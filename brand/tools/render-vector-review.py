#!/usr/bin/env python3
"""Render unclipped source-vs-vector QA panels for locked Agnir artwork.

This tool is intentionally conservative:
- source crops come from the approved 2026-09-02 board;
- vector panels use contain scaling only;
- artwork bounds are drawn explicitly;
- any artwork touching a panel boundary invalidates the review.

The tool does not modify artwork and must not be used to redesign the brand.
"""

from __future__ import annotations

import argparse
import io
import re
from pathlib import Path

import cairosvg
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CROPS = {
    "primary-mark": (70, 140, 390, 410),
    "wordmark": (575, 140, 860, 250),
    "horizontal-lockup": (980, 140, 1410, 330),
    "vertical-lockup": (610, 305, 810, 455),
}


def _font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _source_bbox(image: Image.Image):
    arr = np.asarray(image.convert("RGB"))
    mask = (arr < 242).any(axis=2)
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return (0, 0, image.width, image.height)
    return (int(xs.min()), int(ys.min()), int(xs.max() + 1), int(ys.max() + 1))


def _render_svg(path: Path, max_dim: int = 1600):
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r'viewBox=["\']\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)["\']',
        text,
    )
    width, height = (500.0, 500.0)
    if match:
        width, height = float(match.group(1)), float(match.group(2))
    scale = max_dim / max(width, height)
    png = cairosvg.svg2png(
        bytestring=text.encode("utf-8"),
        output_width=max(1, round(width * scale)),
        output_height=max(1, round(height * scale)),
    )
    image = Image.open(io.BytesIO(png)).convert("RGBA")
    bbox = image.getchannel("A").getbbox() or (0, 0, image.width, image.height)
    return image, bbox


def _vector_on_canvas(vector, bbox, source_art_size, canvas_size):
    art = vector.crop(bbox)
    target_w, target_h = source_art_size
    scale = min(target_w / art.width, target_h / art.height)
    width = max(1, round(art.width * scale))
    height = max(1, round(art.height * scale))
    art = art.resize((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 255))
    x = (canvas_size[0] - width) // 2
    y = (canvas_size[1] - height) // 2
    canvas.alpha_composite(art, (x, y))
    return canvas.convert("RGB"), (x, y, x + width, y + height)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board", required=True, type=Path)
    parser.add_argument("--primary-mark", required=True, type=Path)
    parser.add_argument("--wordmark", required=True, type=Path)
    parser.add_argument("--horizontal-lockup", required=True, type=Path)
    parser.add_argument("--vertical-lockup", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    vectors = {
        "primary-mark": args.primary_mark,
        "wordmark": args.wordmark,
        "horizontal-lockup": args.horizontal_lockup,
        "vertical-lockup": args.vertical_lockup,
    }
    labels = {
        "primary-mark": "Primary mark",
        "wordmark": "Wordmark",
        "horizontal-lockup": "Horizontal lockup",
        "vertical-lockup": "Vertical lockup",
    }

    board = Image.open(args.board).convert("RGB")
    page_w, left, gap, row_h, top = 1500, 60, 40, 360, 120
    col_w = (page_w - left * 2 - gap) // 2
    page_h = top + len(CROPS) * row_h + 90
    page = Image.new("RGB", (page_w, page_h), "white")
    draw = ImageDraw.Draw(page)
    draw.text((60, 35), "Agnir — Unclipped Source vs Vector QA", font=_font(28, True), fill=(25, 25, 25))
    draw.text(
        (60, 75),
        "Contain scaling only. Gray = safe panel; blue = detected artwork bounds.",
        font=_font(13),
        fill=(70, 70, 70),
    )

    for index, (key, crop) in enumerate(CROPS.items()):
        y0 = top + index * row_h
        draw.text((60, y0), f"{index + 1}. {labels[key]}", font=_font(18, True), fill=(25, 25, 25))
        source = board.crop(crop)
        source_bbox = _source_bbox(source)
        source_art = (source_bbox[2] - source_bbox[0], source_bbox[3] - source_bbox[1])
        vector, vector_bbox = _render_svg(vectors[key])

        max_w, max_h = col_w - 40, 250
        scale = min(max_w / source.width, max_h / source.height)
        display_size = (max(1, round(source.width * scale)), max(1, round(source.height * scale)))
        source_display = source.resize(display_size, Image.Resampling.LANCZOS)
        source_display_bbox = tuple(round(value * scale) for value in source_bbox)
        target_art = (max(1, round(source_art[0] * scale)), max(1, round(source_art[1] * scale)))
        vector_display, vector_display_bbox = _vector_on_canvas(vector, vector_bbox, target_art, display_size)

        py = y0 + 38
        for px, label, image, bbox in (
            (60, "SOURCE", source_display, source_display_bbox),
            (60 + col_w + gap, "VECTOR", vector_display, vector_display_bbox),
        ):
            draw.rounded_rectangle(
                (px - 10, py - 10, px + image.width + 10, py + image.height + 10),
                radius=10,
                outline=(190, 190, 190),
                width=2,
            )
            page.paste(image, (px, py))
            draw.rectangle(
                (px + bbox[0], py + bbox[1], px + bbox[2], py + bbox[3]),
                outline=(52, 120, 246),
                width=2,
            )
            draw.text((px, py + image.height + 15), label, font=_font(13), fill=(40, 40, 40))

    draw.text(
        (60, page_h - 55),
        "QA validity rule: artwork touching a panel boundary invalidates the review.",
        font=_font(13),
        fill=(70, 70, 70),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    page.save(args.out)


if __name__ == "__main__":
    main()
