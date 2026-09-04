#!/usr/bin/env python3
"""Build approved Agnir derivatives from locked production masters.

Geometry source is only brand/masters/agnir-mark.svg and agnir-wordmark.svg.
32/16px favicon variants may prune only particles below deterministic
visibility thresholds; this is a size derivative, not a redesign.
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
MARK_VIEWBOX = "31.300 27.655 299.831 215.346"
WORD_VIEWBOX = "0 0 230 88"
BRAND_ORANGE = "#C2812E"


def body(text: str) -> str:
    match = re.search(r"<svg\b[^>]*>(.*)</svg>\s*$", text, re.S)
    if not match:
        raise ValueError("invalid SVG")
    return match.group(1)


def nested(x, y, w, h, viewbox, svg_body):
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" '
            f'viewBox="{viewbox}" preserveAspectRatio="none">{svg_body}</svg>')


def recolor_word(word_body: str, color: str) -> str:
    return word_body.replace('fill="#111111"', f'fill="{color}"')


def gray(value: str) -> str:
    h = value.lstrip("#")
    r, g, b = [int(h[i:i+2], 16) for i in (0, 2, 4)]
    y = round(0.2126*r + 0.7152*g + 0.0722*b)
    return f"#{y:02X}{y:02X}{y:02X}"


def grayscale_mark(mark_body: str) -> str:
    return re.sub(r'fill="(#[0-9A-Fa-f]{6})"',
                  lambda m: f'fill="{gray(m.group(1))}"', mark_body)


def prune(mark_text: str, threshold: float) -> str:
    root = ET.fromstring(mark_text)
    q_circle = f"{{{NS}}}circle"
    q_path = f"{{{NS}}}path"
    for child in list(root):
        if child.tag == q_circle and float(child.attrib.get("r", "0")) < threshold:
            root.remove(child)
        elif child.tag == q_path:
            child.set("fill-opacity", "0.60")
    return ET.tostring(root, encoding="unicode")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--out", type=Path, default=Path("brand/exports"))
    parser.add_argument("--png", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    out = (repo / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)

    mark_text = (repo / "brand/masters/agnir-mark.svg").read_text(encoding="utf-8")
    word_text = (repo / "brand/masters/agnir-wordmark.svg").read_text(encoding="utf-8")
    mark_body, word_body = body(mark_text), body(word_text)

    files = {
        "agnir-horizontal-light.svg": f'<svg xmlns="{NS}" viewBox="0 0 430 190">{nested(23,29,174,153,MARK_VIEWBOX,mark_body)}{nested(203,74,205,81,WORD_VIEWBOX,recolor_word(word_body, BRAND_ORANGE))}</svg>',
        "agnir-horizontal-dark.svg": f'<svg xmlns="{NS}" viewBox="0 0 430 190">{nested(23,29,174,153,MARK_VIEWBOX,mark_body)}{nested(203,74,205,81,WORD_VIEWBOX,recolor_word(word_body, "#FFFFFF"))}</svg>',
        "agnir-horizontal-monochrome.svg": f'<svg xmlns="{NS}" viewBox="0 0 430 190">{nested(23,29,174,153,MARK_VIEWBOX,grayscale_mark(mark_body))}{nested(203,74,205,81,WORD_VIEWBOX,word_body)}</svg>',
        "agnir-app-icon.svg": f'<svg xmlns="{NS}" viewBox="0 0 512 512"><rect x="24" y="24" width="464" height="464" rx="92" fill="#FFFFFF"/>{nested(76,110,360,259,MARK_VIEWBOX,mark_body)}</svg>',
        "agnir-favicon.svg": f'<svg xmlns="{NS}" viewBox="0 0 256 256">{nested(18,43,220,158,MARK_VIEWBOX,mark_body)}</svg>',
        "agnir-favicon-32-source.svg": prune(mark_text, 2.8),
        "agnir-favicon-16-source.svg": prune(mark_text, 4.2),
    }
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")

    if args.png:
        import cairosvg
        cairosvg.svg2png(url=str(out / "agnir-app-icon.svg"), write_to=str(out / "agnir-app-icon-512.png"), output_width=512, output_height=512)
        for size in (128, 64):
            cairosvg.svg2png(url=str(out / "agnir-favicon.svg"), write_to=str(out / f"agnir-favicon-{size}.png"), output_width=size, output_height=size)
        for size in (32, 16):
            cairosvg.svg2png(url=str(out / f"agnir-favicon-{size}-source.svg"), write_to=str(out / f"agnir-favicon-{size}.png"), output_width=size, output_height=size)


if __name__ == "__main__":
    main()
