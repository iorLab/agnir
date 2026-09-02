# Agnir approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `78820894-7679-4b2a-89eb-b3ff71300e8d.png`
- Dimensions: `1448 × 1086`
- SHA-256: `24b418a975369ea022db229aaa45e1a4993e982f8d4baec16c918a1a0a4b99ac`
- Applicable context: **Agnir-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. These crops are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | Crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(105, 145, 355, 390)` | `250×245` | `57ab06e4b0698de37a6c797cdc7dfa7e47ea827d4f9e110961e5251dc4d9aba6` |
| Wordmark | `(505, 135, 885, 235)` | `380×100` | `e048f59bf7c1c02c6f0bbd37933ea067d8f8b03562060b6cdc634a481229c643` |
| Horizontal lockup | `(965, 160, 1362, 305)` | `397×145` | `4e68ac463fbcf6b18c5900ab8e2e5cdb01763a1189add80e9a1b62cb5cc6a871` |
| Vertical lockup | `(500, 270, 900, 500)` | `400×230` | `c1653c0d4f0f21cb25bf3ddc20a09a389324a7339553c304e78b988fcbf499c4` |
| Light-background example | `(40, 556, 447, 740)` | `407×184` | `cda9b4c536f27d0f8cd8a68bb74a246e56dcf01f893c071afbd656e41cd9d321` |
| Dark-background example | `(482, 556, 920, 740)` | `438×184` | `d690191d9f6320f45d25681b6a17419ce9a8a9e9983a144445a8575a5b9187fd` |
| Monochrome example | `(958, 556, 1368, 740)` | `410×184` | `de6183931d9c6dbff8be1cb574a1a8495400d510514a794f0e886f0c578fca62` |
| App-icon example | `(42, 802, 190, 965)` | `148×163` | `b8b4ac3827261a7ae1544073829ad49916e89929f7682c68c05f450415c19850` |
| Social-card example | `(635, 802, 1015, 972)` | `380×170` | `80e203afd3ab5faf4287c2a1fac60a5ca5b5659cbafb72900b07e3dee4c60f62` |

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated `A`, ribbon-based Agnir mark, different typeface, reconciled palette, or redesigned particle field.
3. Agnir's approved solo mark is the **particle-built A with a central anchor** shown on the approved board.
4. Vectorization must be reviewed against the source crop before it can become a master.
5. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
6. No upscaled crop may be represented as a genuine higher-resolution master.

## Binary-preservation boundary

The active GitHub connector on this execution surface exposes repository UTF-8 content writes but no local-file/binary upload action. Therefore the byte-exact source PNG and crop PNGs have been preserved in the current locked reference package and identified here by hashes, but are **not falsely claimed to be committed binary repository files**. A Git-capable/binary-upload execution surface should add the byte-exact approved source to `brand/reference/` before final `main` integration. Until then, never replace the source with a generated lookalike.
