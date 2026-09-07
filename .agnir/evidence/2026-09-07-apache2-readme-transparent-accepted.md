# Apache-2.0 + transparent README lockup acceptance

Principal authorization: **`同意，按 Apache-2.0 + 透明 README logo 推进`**.

## Accepted repository licensing

- Root `LICENSE` contains the Apache License, Version 2.0.
- GitHub repository host readback recognizes `license.key = apache-2.0`, `license.name = Apache License 2.0`, and SPDX `Apache-2.0`.
- `CONTRIBUTING.md` and `CONTRIBUTING.zh-CN.md` provide the public contribution entry points and align intentional contributions with repository Apache-2.0 terms unless explicitly stated otherwise.
- Licensing does not alter Core/profile semantics, Project/lineage identity, stable release identity, or published tags.

## Accepted README branding

- Both README language variants use a theme-aware `<picture>` surface.
- Dark mode selects `brand/exports/agnir-horizontal-dark.svg`; light mode selects `brand/exports/agnir-horizontal-light.svg`.
- The two horizontal SVG exports were deterministically regenerated from approved `brand/masters/` geometry using `brand/tools/build-production-derivatives.py`.
- The accepted exports are self-contained and transparent-background; no background `<rect>` or external nested `<image>` dependency is part of the rendered README asset.
- Approved brand geometry is unchanged.

## Receipts

- deterministic one-shot materialization: workflow run `34091381247`, job `101645375363` — success;
- PR #37 synthetic-merge conformance: run `34091609897`, repository job `101646061660` — success;
- authoritative squash merge: `66784f9ca962d919761a1e2bb4fd3676434b37ef`;
- authoritative post-merge conformance: run `34091660524`, repository job `101646233499` — success;
- authoritative README readback confirms the theme-aware transparent `<picture>` block;
- GitHub repository metadata readback confirms Apache License 2.0 / SPDX `Apache-2.0`.

## Wave 0 consequence

Repository license/contribution presentation is closed. The remaining Wave 0 host metadata item is GitHub topics.
