# PPMP Next Steps

## Immediate

1. Validate the Cloudflare production build and live website after the PPMP v2 / iorMemory naming correction, including Home, Quick Start, Reference, and copy interactions.
2. Validate one real consuming-project migration from RPM v1 to PPMP v2 using iorMemory and `spec/MIGRATION.md`.
3. Validate this repository's next fresh-conversation bootstrap using the v2 self-hosted manifest and ChatGPT adapter instructions.

## Near term

- Decide whether and when to rename the GitHub repository from `mattamior/rpm`; repository naming is operational branding and no longer protocol semantics.
- Add an explicit LICENSE before broader public promotion.
- Decide on the public domain/Worker naming after the site migration is validated.
- Add machine-readable conformance metadata when iorMemory versions or additional PPMP implementations need it.
- Add additional persistence backends or platform adapters only when driven by concrete implementation needs.

## Completed in v2 migration

- Established **PPMP — Persistent Project Memory Protocol** as the protocol identity.
- Established **iorMemory** as the first reference Skill/implementation of PPMP.
- Released the protocol lineage as **PPMP v2.0.0**, an explicit MAJOR migration from RPM v1.0.0.
- Separated protocol, implementation, repository backend, and ChatGPT adapter behavior.
- Migrated Core specification, profiles, examples, templates, self-hosted manifest, and public website content to v2 semantics.
- Corrected the temporary naming inversion that had incorrectly described iorMemory as the protocol and Persistent Project Memory as the implementation.
- Preserved RPM v1 as historical predecessor and documented explicit migration behavior.
