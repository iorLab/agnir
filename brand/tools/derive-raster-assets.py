#!/usr/bin/env python3
"""Derive fidelity-preserving raster brand assets from approved white-background crops.

This tool does not redesign, vectorize, or invent brand geometry. It removes the
white presentation background by solving a simple white-matte compositing model,
then emits transparent PNGs and square icon derivatives with a SHA-256 manifest.

Upscaled outputs are explicitly marked as raster-derived upscales in the manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

ROLES = ("primary-mark", "wordmark", "horizontal-lockup", "vertical-lockup")
ICON_SIZES = (512, 256, 128, 64, 32, 16)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def white_to_alpha(image: Image.Image, noise_floor: float = 0.015) -> Image.Image:
    """Recover an RGBA approximation from artwork composited over white.

    Alpha is inferred from the maximum RGB deficit from white; RGB is then
    un-premultiplied against white. This is intended for the locked brand crops,
    whose marks/wordmarks are rendered on white. It must not be used as a generic
    background-removal algorithm for arbitrary images.
    """

    rgb = np.asarray(image.convert("RGB"), dtype=np.float32)
    deficit = 255.0 - rgb
    alpha = np.max(deficit, axis=2) / 255.0
    alpha = np.where(alpha < noise_floor, 0.0, alpha)

    a = alpha[..., None]
    foreground = np.zeros_like(rgb)
    nonzero = alpha > 1e-6
    foreground[nonzero] = (
        rgb[nonzero] - 255.0 * (1.0 - a[nonzero])
    ) / a[nonzero]
    foreground = np.clip(foreground, 0.0, 255.0)

    rgba = np.dstack((foreground, alpha * 255.0)).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def square_fit(image: Image.Image, size: int, padding_fraction: float) -> Image.Image:
    pad = round(size * padding_fraction)
    available = max(1, size - 2 * pad)
    scale = min(available / image.width, available / image.height)
    new_size = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    resized = image.resize(new_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.alpha_composite(
        resized,
        ((size - resized.width) // 2, (size - resized.height) // 2),
    )
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--brand", required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "brand": args.brand,
        "derivation": "approved white-background raster crop -> transparent raster derivative",
        "warning": "Raster derivatives are not vector masters. Upscaled outputs are explicitly flagged.",
        "assets": {},
    }

    primary_native_max = None
    primary_rgba = None

    for role in ROLES:
        source = args.source_dir / f"{role}.png"
        if not source.exists():
            raise SystemExit(f"missing required crop: {source}")
        source_image = Image.open(source)
        rgba = white_to_alpha(source_image)
        target = args.out_dir / f"{role}-transparent.png"
        rgba.save(target, optimize=True)
        manifest["assets"][target.name] = {
            "source": source.name,
            "width": rgba.width,
            "height": rgba.height,
            "sha256": sha256(target),
            "raster_derived_upscale": False,
        }
        if role == "primary-mark":
            primary_rgba = rgba
            primary_native_max = max(rgba.width, rgba.height)

    assert primary_rgba is not None and primary_native_max is not None

    for size in ICON_SIZES:
        padding = 0.08 if size >= 64 else 0.05
        icon = square_fit(primary_rgba, size, padding)
        target = args.out_dir / f"icon-{size}.png"
        icon.save(target, optimize=True)
        manifest["assets"][target.name] = {
            "source": "primary-mark-transparent.png",
            "width": size,
            "height": size,
            "sha256": sha256(target),
            "raster_derived_upscale": size > primary_native_max,
        }

    (args.out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
