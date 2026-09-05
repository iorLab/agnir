# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Checkpoint, commit, and publication semantics

- A checkpoint is an authoritative continuity transition, not an activity-log append.
- Reconcile Project truth first; unchanged truth is a checkpoint no-op.
- Material checkpoints construct a coherent candidate before publication and must not expose mixed generations as coherent truth.
- Stale-base writers surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile instead of overwriting newer truth.
- A revision/checkpoint receipt is not Project identity or logical lineage identity.

## Compatible operational upgrade vs compatibility migration

- Upgrade is not re-initialization. Compatible operational upgrades preserve Project identity, durable truth, unrelated Project instructions/content, and still-valid locators.
- A Core/profile compatibility-line change is migration-required and must not be silently rewritten as a compatible upgrade.
- Core/profile `0.1` → `0.2` is a published stable migration contract; existing `0.1` Projects remain supported compatibility/regression surfaces.
- For an authoritative source still on Core `0.1`, explicit migration authorization has precedence over validation of migration-only target choices. An unauthorized 0.1→0.2 request therefore surfaces `AGNIR_UPGRADE_MIGRATION_REQUIRED` even when proposed initial-lineage input is empty or otherwise unusable.
- For the published 0.1→0.2 migration, a **string-valued** initial-lineage input is normalized before emptiness, persistence, idempotence, or conflict comparison by removing leading/trailing Unicode code points whose `White_Space` property is `Yes`, using the exact set frozen in `spec/CORE_0_1_TO_0_2_MIGRATION.md`. This normalization rule is migration-specific and does not redefine the general Core 0.2 identity representation contract.
- Inputs that normalize to the same initial lineage are the same migration target; a normalized-empty input fails with `AGNIR_LINEAGE_REQUIRED` after migration authorization is established.

## Core 0.2 Continuity Lineages

- Core `0.2` generalizes Core `0.1`'s single implicit continuity line into multiple independently advancing Continuity Lineages owned by one Project.
- Project identity and logical lineage identity are distinct; selector/binding and checkpoint receipt are separate again.
- Logical lineage identity is durable within Project scope and is not defined by a backend selector/locator or revision/checkpoint receipt.
- Ordinary lineage-local work resolves exactly one lineage from explicit input, trusted selected context, or explicit default; missing deterministic selection fails rather than scanning siblings.
- Checkpoints are lineage-local by default and must not silently mutate sibling lineages.

## VCS lineage binding and integration

- A selected Git ref/worktree is not itself logical lineage identity.
- Core/profile `0.2` VCS selector/binding/fork/rebind/integration semantics are governed by `spec/AGNIR_CORE_0_2.md` plus `profiles/REPOSITORY_FILESYSTEM_0_2.md`; the older `profiles/VCS_BRANCH_CONTINUITY.md` remains Core/profile `0.1` compatibility/design material.
- Agnir-aware forks preserve Project identity while establishing a new logical lineage identity and selector binding; selector rename/rebind may preserve lineage identity.
- Integration is target reconciliation, not source-continuity copying. Source continuity is input, never automatic target truth.
- When Agnir controls publication, stage without target advancement, reconcile, publish integrated Project + reconciled target continuity coherently, then fresh-verify. Relevant source/target advancement invalidates stale integration candidates.

## Repository/filesystem 0.2 and failure mapping

- `repository-filesystem/0.2` resolves one selected logical lineage plus its durable memory locators; sibling enumeration is not required for ordinary cold start.
- A string-valued incompatible `agnir.version` declaration is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing, null, or wrong scalar/container Core-version serialization is `AGNIR_DISCOVERY_INCONSISTENT`. Profile mismatch after 0.2 profile selection is also inconsistent serialization/profile state rather than unsupported Core.
- A local locator escaping the selected Project root without authorized external Locator Chain is `AGNIR_DISCOVERY_UNRESOLVABLE`; distinguishable denied external authorization is `AGNIR_DISCOVERY_UNAUTHORIZED`.
- State/Next Actions/non-null Decisions resolve to regular files; non-null Evidence resolves to a directory; baseline Evidence discovery exposes immediate regular-file children only.
- Filesystem indirection does not waive selected-root authority: local Evidence indirection may resolve to an in-root regular file but must not read an out-of-root canonical target without authorized external binding.

## Independent-implementation evidence policy

- The v1 independent-implementation gate is **satisfied** by issue #26 against exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`.
- The accepted run preserved Phase A reconstruction/freeze → independent Phase B implementation/freeze → Phase C reference inspection; its final verdict was `PASS`, with no concurrent documentation, conformance, or implementation failure class.
- The accepted artifact SHA-256 is `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`; Phase A freeze is `1b422ad2ce17ed046baf488a180fe288f0a6d6599e642a5f3403d74d8d46eb56`; Phase B freeze is `6d75402a99795eddd1781a8e075584834995868becb9ae8fb7a74a5b20b86cde`.
- No additional fresh independent challenge is required merely for repetition. The gate reopens only if later work materially changes the public contract or new evidence exposes a real interoperability defect.

## Core/profile 1.0 promotion policy

- The next active release stage is deliberate promotion of the proven Core/profile `0.2` semantics to stable Core/profile `1.0`, followed by an explicit repository `1.0.0-rc` cycle.
- Promotion is a **stability/compatibility commitment**, not an opportunity to add unrelated features or redesign the Core model.
- Historical `v0.2.0`, Core `0.2`, profile `repository-filesystem/0.2`, and their evidence remain immutable history; they are not renamed or rewritten in place.
- The exact `0.2` → `1.0` serialized compatibility/promotion mechanics must be specified publicly before implementation. Existing `0.2` manifests must not be silently reinterpreted as `1.0` merely to simplify release mechanics.
- The promotion candidate must define preservation, idempotence/conflict behavior, fresh 1.0 discovery/resume, and supported historical compatibility lines, then lock them with conformance before an RC is created.
- If promotion work discovers a need for a material semantic redesign, that is not a promotion-only change and must reopen the relevant compatibility/readiness decision instead of being bundled into 1.0 by implication.

## Release and repository governance

- `v1.0.0` is a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.
- Repository `1.0.0`, Core `1.0`, and profile `repository-filesystem/1.0` are intended to align at the first stable 1.0 release, while remaining distinct version axes in the architecture.
- `main` is the only intended long-lived authoritative branch. Release/validation/repair branches are temporary staging/evidence carriers and require explicit reconciliation before authoritative-main advancement.
- Published tags are immutable. Stable `0.2.x` maintenance may repair documentation, conformance, packaging, or implementation without silently redefining Core/profile `0.2` semantics.
