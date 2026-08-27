# PPMP Next Steps

## Immediate

1. Complete **live production acceptance** of the Sandminni public website: verify the deployed Home, Quick Start, Reference, and copy interactions against Cloudflare. Repository Site CI runs `33050210045` and `33050497784` have verified dependency installation, Astro build, and Wrangler dry-run packaging successfully.
2. Synchronize this maintenance ChatGPT Project's actual external Project Instructions with `.chatgpt/PROJECT_INSTRUCTIONS.md`, then verify one new conversation performs v2 first-substantive-turn discovery and restore without legacy RPM naming. The current conversation proved the mechanical manifest/state bootstrap but exposed configuration drift in the external wording.
3. Synchronize the `mattamior/tree-hole` ChatGPT Project's actual external Project Instructions with its `.chatgpt/PROJECT_INSTRUCTIONS.md`, then verify a fresh conversation restores the migrated PPMP v2 / PPM state. Repository migration, durable-state preservation, application-source comparison, and CI/build validation are complete.

## Near term

- Explore Sandminni's visual identity and logo around **sand/grains**, **convergence or accumulation**, and **memory/durable continuity**.
- Decide whether and when to rename the GitHub repository from `mattamior/rpm`; repository naming is operational branding and no longer protocol semantics.
- Add an explicit LICENSE before broader public promotion.
- Decide on the public domain/Worker naming after the site migration is validated.
- Consider adding a committed site dependency lockfile so Site CI and Cloudflare builds resolve the same transitive dependency graph reproducibly; current top-level dependencies are pinned but `site/` has no lockfile.
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
- Migrated the real consuming repository `mattamior/tree-hole` from RPM v1 to PPMP v2 / PPM at the repository layer without relocating its durable memory files or changing executable application source.
- Promoted a migration finding into the reference repository backend: memory-only checkpoints should avoid unrelated CI/CD side effects when repository policy supports that, should be coalesced when practical, and must not conflate persistence verification with release verification.
- Added path-scoped Site CI and verified the Sandminni site builds and packages successfully for Cloudflare Workers.
- Made ChatGPT Project Instructions drift explicit in the adapter and added repository-backed intended-instructions snapshots for both the PPMP maintenance project and Tree Hole.
- Mechanically validated this maintenance Project's v2 self-hosted bootstrap in the current fresh conversation: the manifest, Current State, Next Steps, and relevant Decisions were loaded before substantive work. External naming/configuration synchronization remains a separate acceptance item.
