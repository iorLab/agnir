# Apache-2.0 + transparent README logo staging

Principal authorization: adopt **Apache License 2.0** for Agnir and remove the background color from the README logo presentation.

Staged changes on `maintenance/apache2-readme-transparent`:

- add the standard Apache License 2.0 text as root `LICENSE`;
- deterministically regenerate `brand/exports/agnir-horizontal-dark.svg` and `brand/exports/agnir-horizontal-light.svg` from the approved production masters;
- both horizontal exports are self-contained and transparent-background delivery derivatives;
- update English and Simplified Chinese README headers to use a theme-aware `<picture>` selecting the dark or light transparent self-contained lockup;
- update `brand/exports/README.md` to document the self-contained transparent horizontal exports;
- no approved brand geometry, Core/profile semantics, stable release identity, or published tag changes.

One-shot materialization workflow run `34091381247` completed the deterministic export generation and README patch, then removed its own temporary workflow file before the staging branch was proposed for merge.

Acceptance remains gated on PR synthetic-merge conformance, authoritative merge, post-merge conformance, GitHub license recognition, and README public-surface readback.
