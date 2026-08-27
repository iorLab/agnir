# Agnir Next Steps

## Immediate — make Agnir Core 0.1 testable

1. Review and tighten `spec/AGNIR_CORE_DRAFT.md` into a normative Agnir Core 0.1 draft while preserving the layer separation **Core -> Profiles -> Implementations -> Backends -> Adapters**.
2. Define the Discovery Record contract in testable terms:
   - required semantic fields;
   - version/compatibility declaration;
   - locator resolution rules;
   - stale/ambiguous/cyclic/unauthorized locator failures;
   - external-memory resolution requirements.
3. Define the first repository/filesystem discovery profile without making its path/layout Core. Evaluate whether the profile should standardize `AGNIR.yaml`, `.agnir/`, or another convention.
4. Write an explicit **PPMP v2 -> Agnir 0.1 migration mapping** covering Current State, Next Steps -> Next Actions, Decisions, checkpoint/evidence history, configuration, profiles, and discovery semantics.
5. Define compatibility behavior for projects that continue using PPMP v2 / PPM during transition. PPMP v2 conformance must remain predecessor conformance until an explicit migration succeeds.
6. Define Agnir conformance cases that prove the cold-start invariant instead of merely claiming platform neutrality.

## Svif dependency boundary

7. Coordinate with the independent Svif project in `iorLab/zerolocal`.
8. Keep the normative dependency at the **Agnir Core protocol** layer, not the Agnir implementation/backend/adapter layer.
9. Treat `Agnir Core 0.1` as the current draft compatibility target; freeze the exact release version/range only after the Agnir Core contract is stable enough to test.
10. Ensure Svif-specific lifecycle, verification, delivery, provider, and protected-secret rules do not leak into Agnir Core unless independently justified as general durable-continuity semantics.

## Shared workspace / separate durable memory

11. Continue using one ChatGPT Project or other execution workspace to coordinate Agnir and Svif when useful, while keeping their durable memories independent.
12. Do not create a shared mutable cross-project memory store. Persist cross-project decisions in each affected project according to local meaning.
13. Later define and validate a workspace-registry pattern that stores project/discovery locators only.
14. Use this workspace as a future conformance case: one execution environment, multiple Projects, isolated Agnir continuity, no durable context bleed.

## Conformance pressure cases

15. Add at least two materially different execution/storage arrangements after the Core contract is stable enough to test neutrality.
16. Include a fresh-executor cold-start case.
17. Include a multi-project workspace isolation case.
18. Include at least one case where Agnir state is not simply a Git repository `.chatgpt/` directory, so storage neutrality is demonstrated rather than assumed.

## Carry-over predecessor work

19. Preserve the existing PPMP v2 maintenance evidence and deferred tasks:
   - current maintenance-project fresh-conversation ChatGPT-adapter acceptance;
   - `mattamior/tree-hole` external Project Instructions synchronization and fresh restore test;
   - repository-backend checkpoint/CI side-effect findings;
   - Site CI evidence and optional browser acceptance;
   - license, dependency lockfile, repository/domain/Worker naming cleanup.
20. Resume those tasks only when it is clear whether the target is intentionally predecessor PPMP/PPM behavior or the Agnir line.

## Naming and packaging — deferred until contracts settle

21. Defer broad rename work for repository name, website/domain/Worker, predecessor implementation IDs, templates, and public branding until the Agnir 0.1 migration/compatibility contract is explicit.
22. Do not treat ChatGPT Skill, CLI, SDK, or any other integration form as Agnir Core architecture. These are implementations/adapters built after the contract is stable enough to implement repeatedly.
