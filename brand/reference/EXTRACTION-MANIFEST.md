# Agnir approved-reference extraction manifest — 2026-09-02

Status: **branch-local production-preparation record**. The visual authority remains `brand/APPROVED-VISUAL-REFERENCE.md` and the Principal-approved Today 10:42 AM reference set.

## Approved source

- Source attachment: `78820894-7679-4b2a-89eb-b3ff71300e8d.png`
- Dimensions: `1448 × 1086`
- SHA-256: `24b418a975369ea022db229aaa45e1a4993e982f8d4baec16c918a1a0a4b99ac`
- Applicable context: **Agnir-only** usage.

The co-brand/family authority remains attachment `1d00fb70-189b-4742-b4ac-c79be2668559.png`, SHA-256 `4110d285243b6241ac709e750cca1815a10ca41e27c3bb15e6c94b56e57fa4fb`.

## Final lossless raster extraction map

Coordinates are `(left, top, right, bottom)` in approved-source pixels. These final crops were visually inspected to exclude board headings/dividers where practical. They are QA/trace references, **not independently approved redesigns or vector masters**.

| Asset role | Crop box | Size | Derived PNG SHA-256 |
| --- | --- | --- | --- |
| Primary mark | `(110, 155, 355, 390)` | `245×235` | `66edc2f6dff61507775284a273b08222bc2d946a8f933bfce79a75657e3b9df0` |
| Wordmark | `(505, 145, 900, 245)` | `395×100` | `c93c3743284e14bcc3750472a7a31476ed8f30cdb5673117b3721140d1bd45c0` |
| Horizontal lockup | `(970, 165, 1400, 310)` | `430×145` | `d7f3d08be5d5c0efd20995f5cefa5665a1983300b1f8e22d07ce4f4fdc22bda6` |
| Vertical lockup | `(600, 295, 805, 455)` | `205×160` | `4320300782c57b8679e10caa85098a6ce07e4cf9fbd4ce8d58fb5b0705c6ad3f` |
| Light-background example | `(38, 575, 450, 740)` | `412×165` | `acb895e9be89c79c25a51ca7822c0629ebfbbfc1d4e37bedfa05a2467d763ec2` |
| Dark-background example | `(480, 575, 925, 740)` | `445×165` | `fa985aa9822864140c3f76555fe8ba7908c25ea5ac4d4b059bf530976551a30e` |
| Monochrome example | `(955, 575, 1375, 740)` | `420×165` | `eee75df574b046690bc38886738e46ea1f131be3c5da96166513f76cef074085` |
| App-icon example | `(40, 815, 190, 970)` | `150×155` | `14cf2ad3d7949e30e14855a57a3d04f15ca027cc53224f39bdd141a8fd1da219` |
| Social-card example | `(645, 820, 1015, 970)` | `370×150` | `20e95c74ee3acfca3e072429facffda836d5e1586394d1226e7f572b17766cd2` |

## Production rule

1. Reconstruct from the applicable approved board and these lossless crop references.
2. Do not substitute a regenerated `A`, ribbon-based Agnir mark, different typeface, reconciled palette, or redesigned particle field.
3. Agnir's approved solo mark is the **particle-built A with a central anchor** shown on the approved board.
4. Vectorization must be reviewed against the source crop before it can become a master.
5. The board is raster evidence; a crop's displayed pixel dimensions do not imply that the board contains a true 512px/128px source asset merely because the board labels one that way.
6. No upscaled crop may be represented as a genuine higher-resolution master.

## Binary-preservation boundary

The active GitHub connector on this execution surface exposes repository UTF-8 content writes but no local-file/binary upload action. Therefore the byte-exact source PNG and crop PNGs have been preserved in the current locked reference package and identified here by hashes, but are **not falsely claimed to be committed binary repository files**. A Git-capable/binary-upload execution surface should add the byte-exact approved source to `brand/reference/` before final `main` integration. Until then, never replace the source with a generated lookalike.
