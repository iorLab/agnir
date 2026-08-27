# Agnir Next Steps

## Immediate — converge Agnir Core 0.1

1. Reconcile `spec/AGNIR_CORE_DRAFT.md`, `spec/AGNIR_DISCOVERY_DRAFT.md`, `spec/AGNIR_MIGRATION_DRAFT.md`, and `profiles/REPOSITORY_FILESYSTEM_DRAFT.md` into one coherent normative Agnir Core/profile set without collapsing profiles/backends/adapters into Core.
2. Define the exact `AGNIR.yaml` schema/versioning rules for the repository/filesystem profile, including extension namespaces, optional profile declarations, and validation behavior.
3. Define recommended Project identity forms and collision/boundary rules without requiring one globally centralized identity system.
4. Specify repository/filesystem handling for nested Projects, symlinks, mounts, worktrees, and optional VCS/ref extensions.
5. Turn the draft discovery failure taxonomy into normative semantic error categories and define what conformance evidence is required for each relevant class.
6. Define executable cold-start conformance fixtures that prove discovery from only a Project Entry Point.

## Migration and compatibility

7. Validate the PPMP v2 -> Agnir migration draft against this repository's current self-hosted PPMP/PPM layout and at least one external predecessor project.
8. Preserve explicit `PPMP v2 mode -> migration mode -> Agnir 0.1 mode` transitions; do not let tooling silently claim target conformance.
9. Define the durable migration evidence envelope: source version, target version, preserved knowledge, changed semantics, unresolved incompatibilities, and cold-start acceptance result.
10. Keep physical path/repository/brand renames separate from semantic migration completion.
11. Do not create this repository's own authoritative `AGNIR.yaml` yet merely because the profile draft exists; self-migrate only when the draft schema/conformance procedure is stable enough to validate rather than assume.

## Svif dependency boundary

12. Coordinate with the independent Svif project in `iorLab/zerolocal`.
13. Keep the normative dependency at the **Agnir Core protocol** layer, not the Agnir implementation/backend/adapter layer.
14. Treat `Agnir Core 0.1` as the current draft compatibility target; freeze the exact release version/range only after the normative Core/discovery contract is stable enough to test.
15. Ensure Svif lifecycle, delivery, provider, and stricter protected-secret rules do not leak into Agnir Core unless independently justified as general durable-continuity semantics.

## Conformance pressure cases

16. Add a repository/filesystem cold-start case using top-level `AGNIR.yaml` from only a Project root.
17. Add at least one materially non-repository persistence case so storage neutrality is demonstrated rather than asserted.
18. Include a fresh-executor cold-start case where the executor receives no memory path outside the normal discovery route.
19. Include a multi-project workspace isolation case: one execution workspace, multiple Projects, independent Agnir continuity, no durable context bleed.
20. Include an external-memory locator case with explicit authorization failure behavior if practical.
21. Include one broken-locator case and one Project-identity-mismatch case so failure semantics are tested, not only happy-path discovery.

## Shared workspace / separate durable memory

22. Continue using one ChatGPT Project or other execution workspace to coordinate Agnir and Svif when useful, while keeping their durable memories independent.
23. Do not create a shared mutable cross-project memory store. Persist cross-project decisions in each affected Project according to local meaning.
24. Later define and validate a workspace-registry pattern that stores only Project roots or `AGNIR.yaml`/equivalent discovery locators.

## Carry-over predecessor work

25. Preserve the existing PPMP v2 maintenance evidence and deferred tasks:
   - current maintenance-project fresh-conversation ChatGPT-adapter acceptance;
   - `mattamior/tree-hole` external Project Instructions synchronization and fresh restore test;
   - repository-backend checkpoint/CI side-effect findings;
   - Site CI evidence and optional browser acceptance;
   - license, dependency lockfile, repository/domain/Worker naming cleanup.
26. Resume those tasks only when it is clear whether the target is intentionally predecessor PPMP/PPM behavior or the Agnir line.

## Naming and packaging — deferred until contracts settle

27. Defer broad rename work for repository name, website/domain/Worker, predecessor implementation IDs, templates, and public branding until Agnir 0.1 migration/compatibility is explicit.
28. Do not treat ChatGPT Skill, CLI, SDK, or any other integration form as Agnir Core architecture. These are implementations/adapters built after the contract is stable enough to implement repeatedly.

## Branch governance — cleanup deferred

29. Treat `main` as the authoritative active Agnir line and `legacy/ppmp-v2.0.0` as the preserved predecessor line.
30. Ignore temporary, redundant, or incidental branches during active architecture work unless one causes a real conflict or ambiguity.
31. After the new Agnir version is substantially complete, review and delete non-authoritative branches in one deliberate cleanup pass.
