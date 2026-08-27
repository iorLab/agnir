# Agnir Next Steps

## Immediate — identity, protocol boundary, and migration design

1. Treat **PPMP v2.0.0 / PPM / Sandminni** as the immediate predecessor architecture and released evidence base. Do not silently relabel predecessor conformance claims as Agnir conformance.
2. Define Agnir's target layer model and naming. Resolve whether Agnir is:
   - the single umbrella identity for protocol + implementation family; or
   - the project/product identity above a subordinate technical protocol/implementation naming layer.
3. Define Agnir Core as **project-owned durable memory/continuity** with no normative dependency on Git, GitHub, repository hosting, ChatGPT, conversational interfaces, a particular AI agent, local-vs-remote execution, or a specific storage layout.
4. Formalize the generalized **cold-start / fresh-executor discovery** invariant: a compatible executor with no predecessor-private context must be able to discover and interpret the project's durable state and resume safely.
5. Specify discovery semantics for both colocated and externally stored Agnir state. The project must be able to declare or expose a durable locator without requiring a particular filesystem path or VCS.
6. Re-evaluate the existing PPMP v2 protocol/implementation/backend/adapter separation and preserve it where still correct. The migration should remove naming/platform leakage, not discard valid architecture.
7. Decide the versioning and compatibility strategy for the transition from RPM v1 -> PPMP v2 -> Agnir. The new Agnir lineage must make incompatible semantic changes explicit.
8. Only after items 2-7 are stable enough, design the concrete rename/migration of:
   - protocol/spec names and identifiers;
   - PPM implementation names and machine IDs;
   - Sandminni public branding;
   - repository name `mattamior/rpm` if desired;
   - website/domain/Worker naming;
   - adapter/backend documentation and examples;
   - self-hosted maintenance memory labels.

## Svif dependency boundary

9. Coordinate with the independent Svif project in `iorLab/zerolocal`.
10. Define a versioned Agnir contract that Svif can depend on without making Agnir depend on Svif.
11. Keep Agnir useful outside software-delivery projects, provider workflows, CI/CD, and cloud deployment.
12. Decide whether Svif requires Agnir specifically or an Agnir-defined compatibility interface/profile that permits alternative conforming implementations.
13. Ensure Svif-specific lifecycle, provider, verification, delivery, and trust-boundary semantics do not leak into Agnir Core unless independently justified as durable-memory semantics.

## Shared workspace / separate durable memory

14. Allow one ChatGPT Project or other execution workspace to coordinate Agnir and Svif development, but keep their durable project memories independent.
15. Do not create a shared mutable cross-project memory store. Persist cross-project decisions separately in each affected project.
16. Define a future workspace-registry pattern that stores project/discovery locators only and cannot become a second source of mutable project state.
17. Use this setup later as a multi-project conformance case: one executor environment, multiple projects, isolated Agnir continuity, no durable context bleed.

## Carry-over predecessor work

18. Preserve the existing PPMP v2 maintenance evidence and deferred tasks:
   - current maintenance-project fresh-conversation ChatGPT-adapter acceptance;
   - `mattamior/tree-hole` external Project Instructions synchronization and fresh restore test;
   - repository-backend checkpoint/CI side-effect findings;
   - Site CI evidence and optional browser acceptance;
   - license, dependency lockfile, repository/domain/Worker naming cleanup.
19. Re-run or finish these only when it is clear whether the acceptance target is intentionally predecessor PPMP/PPM behavior or the new Agnir behavior, to avoid spending validation effort on configuration that will immediately be renamed.

## Later conformance work

20. Add concrete Agnir conformance cases across at least two materially different execution/storage surfaces after the Core contract is stable enough to test neutrality rather than merely claim it.
21. Include a fresh-executor case and a multi-project workspace isolation case in that evidence set.
22. Add additional backends/adapters only when concrete pressure demonstrates missing Core boundaries.
