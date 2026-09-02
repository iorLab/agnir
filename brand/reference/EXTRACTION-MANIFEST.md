# Agnir approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `78820894-7679-4b2a-89eb-b3ff71300e8d.png`
- Dimensions: `1448 × 1086`
- SHA-256: `24b418a975369ea022db229aaa45e1a4993e982f8d4baec16c918a1a0a4b99ac`
- Applicable context: **Agnir-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## QA-safe lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. The bounds below supersede earlier review crops that were shown to be too tight or to include misleading neighboring panel content. They deliberately retain white safety margin around the approved artwork so antialiasing, descenders, particles and lockup edges cannot be clipped during review.

These crops are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | QA-safe crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(70, 140, 390, 410)` | `320×270` | `d5e98d916dc86d62218d7d8fc0b6535c19e7c47f4aff66449c3270f948a070bf` |
| Wordmark | `(575, 140, 860, 250)` | `285×110` | `ecc3234740fa03c697c56de8698e283bb53f21c8646ee4665c3b49895ff19607` |
| Horizontal lockup | `(980, 140, 1410, 330)` | `430×190` | `3ad515e4b0521272ae982e524b5c0b470e717042d83f9aba0fc19cc547685744` |
| Vertical lockup | `(610, 305, 810, 455)` | `200×150` | `3b019ecc9e2a11713a870e5cdd937b54720cd73e6a4ef0bc45e03fbbff36cb0a` |
| Light-background example | `(40, 556, 447, 740)` | `407×184` | `7483c332e4784e99c4595ef1f468e61d4f94a8ff1acdc19c65bba5fc8508be33` |
| Dark-background example | `(482, 556, 920, 740)` | `438×184` | `de4f1eadd74ca20302911be6a06423725d10699dcf93ce7fc7e85f904ab438d7` |
| Monochrome example | `(958, 556, 1368, 740)` | `410×184` | `9119598d3b36541da17b1cf366c52b2ed1a7c276741a1b70c94c9d30b1b818f1` |
| App-icon example | `(42, 802, 190, 965)` | `148×163` | `376af1cf3ddd6dbe2eae194047cfb19c7c7a8e99be9c1c8a20ad7771356b6492` |
| Social-card example | `(635, 802, 1015, 972)` | `380×170` | `816dde2340f5aea11e5cf0139cc0db40b4794ab39c7536453342451f173cba46` |

## Review rendering rules

1. Review panels must use **contain**, never crop/cover/fill-to-edge.
2. Source and vector must be shown on separate canvases with explicit safety margin.
3. A review image is invalid if approved artwork or rendered vector artwork touches the panel boundary.
4. Source/vector artwork bounds should be displayed or otherwise checked before Principal review.
5. Do not compensate for a clipped source crop by inventing geometry in the vector candidate; correct the crop first.
6. An unclipped review can reveal real candidate mismatch that a clipped review concealed. Fix the candidate rather than the presentation.

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated `A`, ribbon-based Agnir mark, different typeface, reconciled palette, or redesigned particle field.
3. Agnir's approved solo mark is the **particle-built A with a central anchor** shown on the approved board.
4. Vectorization must be reviewed against the source crop before it can become a master.
5. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
6. No upscaled crop may be represented as a genuine higher-resolution master.

## Binary-preservation boundary

The byte-exact approved board and crop PNGs remain preserved by SHA-256 in the locked local reference package. The current connector can create repository text and Git objects, but there is no direct local-file binary upload bridge suitable for the multi-megabyte byte-exact approved PNG. Final byte-exact binary preservation remains a pre-`main` integration gate; until then, never replace the approved source with a regenerated lookalike.
