# Agnir Next Steps

## Immediate — converge Agnir Core 0.1

1. Reconcile `spec/AGNIR_CORE_DRAFT.md`, `spec/AGNIR_DISCOVERY_DRAFT.md`, and `spec/AGNIR_MIGRATION_DRAFT.md` into one coherent normative Agnir Core 0.1 model without collapsing profiles/backends/adapters into Core.
2. Decide the first repository/filesystem discovery profile anchor. Evaluate top-level `AGNIR.yaml`, `.agnir/manifest.yaml`, and any better alternative against:
   - cold-start discoverability;
   - migration from `.chatgpt/project-memory.yaml`;
   - human readability;
   - implementation simplicity;
   - support for external memory locators;
   - avoiding accidental Core dependence on Git/repository layout.
3. Specify the repository/filesystem profile's handling of optional VCS/ref metadata as profile/backend extensions rather than Core semantics.
4. Define exact Discovery Record extension/versioning rules and profile declaration semantics.
5. Turn the draft discovery failure taxonomy into normative error classes or normative semantic categories.
6. Define executable cold-start conformance fixtures that prove discovery from only a Project Entry Point.

## Migration and compatibility

7. Validate the PPMP v2 -> Agnir migration draft against at least this repository's current self-hosted PPMP/PPM layout and one external predecessor project.
8. Preserve explicit `PPMP v2 mode -> migration mode -> Agnir 0.1 mode` transitions; do not let tooling silently claim target conformance.
9. Define what durable evidence a migration must record, including source version, target version, preserved knowledge, unresolved incompatibilities, and cold-start acceptance result.
10. Keep physical path/repository/brand renames separate from semantic migration completion.

## Svif dependency boundary

11. Coordinate with the independent Svif project in `iorLab/zerolocal`.
12. Keep the normative dependency at the **Agnir Core protocol** layer, not the Agnir implementation/backend/adapter layer.
13. Treat `Agnir Core 0.1` as the current draft compatibility target; freeze the exact release version/range only after the normative Core/discovery contract is stable enough to test.
14. Ensure Svif lifecycle, delivery, provider, and stricter protected-secret rules do not leak into Agnir Core unless independently justified as general durable-continuity semantics.

## Conformance pressure cases

15. Add a repository/filesystem cold-start case using the future Agnir discovery profile.
16. Add at least one materially non-repository persistence case so storage neutrality is demonstrated rather than asserted.
17. Include a fresh-executor cold-start case where the executor receives no memory path outside the normal discovery route.
18. Include a multi-project workspace isolation case: one execution workspace, multiple Projects, independent Agnir continuity, no durable context bleed.
19. Include an external-memory locator case with explicit authorization failure behavior if practical.

## Shared workspace / separate durable memory

20. Continue using one ChatGPT Project or other execution workspace to coordinate Agnir and Svif when useful, while keeping their durable memories independent.
21. Do not create a shared mutable cross-project memory store. Persist cross-project decisions in each affected Project according to local meaning.
22. Later define and validate a workspace-registry pattern that stores project/discovery locators only.

## Carry-over predecessor work

23. Preserve the existing PPMP v2 maintenance evidence and deferred tasks:
   - current maintenance-project fresh-conversation ChatGPT-adapter acceptance;
   - `mattamior/tree-hole` external Project Instructions synchronization and fresh restore test;
   - repository-backend checkpoint/CI side-effect findings;
   - Site CI evidence and optional browser acceptance;
   - license, dependency lockfile, repository/domain/Worker naming cleanup.
24. Resume those tasks only when it is clear whether the target is intentionally predecessor PPMP/PPM behavior or the Agnir line.

## Naming and packaging — deferred until contracts settle

25. Defer broad rename work for repository name, website/domain/Worker, predecessor implementation IDs, templates, and public branding until Agnir 0.1 migration/compatibility is explicit.
26. Do not treat ChatGPT Skill, CLI, SDK, or any other integration form as Agnir Core architecture. These are implementations/adapters built after the contract is stable enough to implement repeatedly.
