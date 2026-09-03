# Agnir Current State

Agnir `v0.2.0-rc.1` is formally published as a **prerelease** at immutable tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`. GitHub Release id `381532232` is `prerelease=true`, `draft=false`; `releases/latest` still resolves to stable `v0.1.1`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, revision receipt, or Continuity Lineage.

## Reconciled authoritative-main target state — 2026-09-03

This checkpoint defines the reconciled target truth for accepting the published RC line into authoritative `main` without copying release-line continuity as target truth.

Captured integration receipts:

- target authoritative `main`: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`;
- accepted source `release/v0.2.0-rc.1`: `866604c4532003538fd6a0b565be9c1ef1c8a034`;
- merge base: the same target revision `f0b2cbd...`;
- source relation: 13 commits ahead, 0 behind; no concurrent main-side divergence at staging time;
- immutable published RC tag: `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`;
- publication/conformance run: `33675638723`;
- post-publication release-line verification: `df745e2486b1d3f5ab2b07e701a9a6f91451a056`, run `33676002813` success;
- release-line hygiene checkpoint: `866604c4532003538fd6a0b565be9c1ef1c8a034`, run `33676171048` success.

The accepted Project/package tree comes from the verified release line, including the promoted Core/profile contracts, bilingual documentation, Skill procedure, release metadata, migration/fresh-install conformance, and release publication evidence. Release-line State and Next Actions are not copied as authoritative-main truth.

## Authoritative main continuity migration

Project identity remains `urn:agnir:project:agnir-core` and all declared memory locators remain unchanged.

Authoritative main now uses Core `0.2` / `repository-filesystem/0.2` with logical Continuity Lineage `urn:agnir:lineage:authoritative`, separately bound to selector `refs/heads/main`. The logical lineage ID is a Project semantic, not a ref name or commit receipt; an explicit future ref rename may rebind this same lineage without changing its identity.

This is the explicit migration of main's former Core/profile `0.1` implicit single line into one Core/profile `0.2` logical lineage. It preserves still-valid main obligations while accepting verified RC results. The operational package recorded on main is repository release `0.2.0-rc.1` at the immutable published revision `50a8cd...`.

## Release status after reconciliation

- repository source line: `0.2.0-rc.1`;
- Core compatibility: `0.2`;
- profile: `repository-filesystem/0.2`;
- latest published stable release remains `v0.1.1` until an actual stable `v0.2.0` is published;
- `v0.2.0-rc.1` remains immutable prerelease evidence and must never be moved;
- final stable `v0.2.0` remains a separate exact-candidate publication decision.

The target-advancing Git revision carrying this reconciled State is itself the checkpoint receipt; its SHA does not need to be embedded into the content that determines that SHA. `.agnir/next-actions.md` is the canonical resume order.
