# Agnir approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `78820894-7679-4b2a-89eb-b3ff71300e8d.png`
- Dimensions: `1448 × 1086`
- SHA-256: `24b418a975369ea022db229aaa45e1a4993e982f8d4baec16c918a1a0a4b99ac`
- Applicable context: **Agnir-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Corrected lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. A second visual-QA pass found that earlier wordmark / lockup bounds were too tight and could clip glyph or mark edges. The coordinates below supersede those earlier crop bounds.

These crops are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | Crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(90, 150, 365, 395)` | `275×245` | `de4dbafca75afa81381aaab051a22f106dac027c5a74e0fff70a56037888b8d0` |
| Wordmark | `(555, 135, 900, 270)` | `345×135` | `b8a978363a9189a2918eda18b43c94736f4c2caa4da1dcd8e32c33a74f5e0ae8` |
| Horizontal lockup | `(995, 145, 1430, 345)` | `435×200` | `2db8bf1d923d873346a7b30776ba260dc481cfa4dcb7f4331c7ab7d41da81f63` |
| Vertical lockup review region | `(590, 290, 820, 450)` | `230×160` | derived from approved board; use only for lockup visual regression |
| Light-background example | `(40, 556, 447, 740)` | `407×184` | `7483c332e4784e99c4595ef1f468e61d4f94a8ff1acdc19c65bba5fc8508be33` |
| Dark-background example | `(482, 556, 920, 740)` | `438×184` | `de4f1eadd74ca20302911be6a06423725d10699dcf93ce7fc7e85f904ab438d7` |
| Monochrome example | `(958, 556, 1368, 740)` | `410×184` | `9119598d3b36541da17b1cf366c52b2ed1a7c276741a1b70c94c9d30b1b818f1` |
| App-icon example | `(42, 802, 190, 965)` | `148×163` | `376af1cf3ddd6dbe2eae194047cfb19c7c7a8e99be9c1c8a20ad7771356b6492` |
| Social-card example | `(635, 802, 1015, 972)` | `380×170` | `816dde2340f5aea11e5cf0139cc0db40b4794ab39c7536453342451f173cba46` |

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated `A`, ribbon-based Agnir mark, different typeface, reconciled palette, or redesigned particle field.
3. Agnir's approved solo mark is the **particle-built A with a central anchor** shown on the approved board.
4. Vectorization must be reviewed against the source crop before it can become a master.
5. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
6. No upscaled crop may be represented as a genuine higher-resolution master.
7. If a crop boundary is later shown to clip approved content, correct the manifest first; do not compensate by inventing geometry in the vector master.

## Binary-preservation boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 in the locked local reference package. The current connector can create repository text and Git objects, but there is no direct local-file binary upload bridge suitable for the multi-megabyte byte-exact approved PNG. Final byte-exact binary preservation remains a pre-`main` integration gate; until then, never replace the approved source with a regenerated lookalike.
