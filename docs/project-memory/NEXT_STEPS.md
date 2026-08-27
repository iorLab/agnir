# PPMP Next Steps

## Immediate

1. Validate the Cloudflare production build and live website after the Sandminni public-site integration, including Home, Quick Start, Reference, and copy interactions.
2. Validate one real consuming-project migration from RPM v1 to PPMP v2 using PPM and `spec/MIGRATION.md`.
3. Validate this repository's next fresh-conversation bootstrap using the v2 self-hosted manifest and ChatGPT adapter instructions.

## Near term

- Explore Sandminni's visual identity and logo around **sand/grains**, **convergence or accumulation**, and **memory/durable continuity**.
- Decide whether and when to rename the GitHub repository from `mattamior/rpm`; repository naming is operational branding and no longer protocol semantics.
- Add an explicit LICENSE before broader public promotion.
- Decide on the public domain/Worker naming after the site migration is validated.
- Add machine-readable conformance metadata when PPM versions or additional PPMP implementations need it.
- Add additional persistence backends or platform adapters only when driven by concrete implementation needs.

## Completed in v2 migration and brand finalization

- Established **PPMP — Persistent Project Memory Protocol** as the protocol identity.
- Established **Persistent Project Memory (PPM)** as the first reference Skill/implementation of PPMP.
- Selected **Sandminni** as the public product brand for the PPM reference implementation while preserving PPM as the technical implementation identity.
- Applied Sandminni consistently across the non-normative public website while preserving the PPMP protocol / PPM implementation boundary.
- Standardized the implementation machine identity as `persistent-project-memory`.
- Released the protocol lineage as **PPMP v2.0.0**, an explicit MAJOR migration from RPM v1.0.0.
- Separated protocol, implementation, repository backend, and ChatGPT adapter behavior.
- Migrated Core specification, profiles, examples, templates, self-hosted manifest, and public website content to v2 semantics.
- Corrected the temporary naming inversion that had incorrectly described iorMemory as the protocol.
- Superseded the short-lived iorMemory implementation name with PPM before production validation.
- Preserved RPM v1 as historical predecessor and documented explicit migration behavior.
