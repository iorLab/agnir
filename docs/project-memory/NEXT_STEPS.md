# iorMemory Next Steps

## Immediate

1. Validate the Cloudflare production build and live website after the iorMemory v2 migration, including Home, Quick Start, Reference, and copy interactions.
2. Validate one real consuming-project migration from RPM v1 to iorMemory v2 / PPM using `spec/MIGRATION.md`.
3. Validate this repository's next fresh-conversation bootstrap using the v2 self-hosted manifest and ChatGPT adapter instructions.

## Near term

- Decide whether and when to rename the GitHub repository from `mattamior/rpm`; repository naming is operational branding and no longer protocol semantics.
- Add an explicit LICENSE before broader public promotion.
- Decide on the public domain/Worker naming after the site migration is validated.
- Add machine-readable conformance metadata if multiple PPM versions or implementations emerge.
- Add additional persistence backends or platform adapters only when driven by concrete implementation needs.

## Completed in v2 migration

- Established **iorMemory** as the protocol identity.
- Established **Persistent Project Memory (PPM)** as the initial reference Skill/implementation.
- Released the protocol lineage as **v2.0.0**, an explicit MAJOR migration from RPM v1.0.0.
- Separated protocol, implementation, repository backend, and ChatGPT adapter behavior.
- Migrated Core specification, profiles, examples, templates, self-hosted manifest, and public website content to v2 terminology and semantics.
- Preserved RPM v1 as historical predecessor and documented explicit migration behavior.
