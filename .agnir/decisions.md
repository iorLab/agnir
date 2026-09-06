# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Checkpoint and reconciliation semantics

- A checkpoint is an authoritative continuity transition, not an activity-log append.
- Reconcile Project truth first; unchanged truth is a checkpoint no-op.
- Material checkpoints construct a coherent candidate before publication and must not expose mixed generations as coherent truth.
- Stale-base writers surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile instead of overwriting newer truth.
- A revision/checkpoint receipt is not Project identity or logical lineage identity.
- Source/staging continuity is reconciliation input, never automatic target truth.

## Compatibility and stable 1.0 policy

- Core/profile compatibility-line changes remain explicit Project-owned migration/promotion operations and must not be silently rewritten as compatible package upgrades.
- Core/profile `0.1` → `0.2` remains a published stable migration contract.
- Core/profile `0.2` → `1.0` is the stable semantics-preserving promotion governed by `spec/CORE_0_2_TO_1_0_PROMOTION.md`.
- Core `1.0` and `repository-filesystem/1.0` stabilize the accepted `0.2` semantics without behavioral redesign.
- Existing valid `0.1` and `0.2` Projects remain supported by the `1.0.x` distribution; installing the distribution is not permission to relabel them as `1.0`.
- Historical `0.1` and `0.2` normative contracts, schemas, and evidence remain immutable history/compatibility surfaces.

## Identity, lineage, and VCS binding

- Project identity and logical Continuity Lineage identity are distinct; selector/binding and revision/checkpoint receipt are separate again.
- A selected Git ref/worktree is not itself logical lineage identity.
- Agnir-aware forks preserve Project identity while establishing a new logical lineage identity and selector binding; explicit selector rename/rebind may preserve lineage identity.
- Checkpoints are lineage-local by default and must not silently mutate sibling lineages.
- Integration is target reconciliation, not source-continuity copying.

## Repository/filesystem compatibility and failure mapping

- `repository-filesystem/0.2` and `repository-filesystem/1.0` each resolve one selected logical lineage plus durable memory locators; sibling enumeration is not required for ordinary cold start.
- A multi-version distribution dispatches according to the compatibility line actually declared. A 1.0 resolver does not silently accept 0.2 as 1.0, and a 0.2 resolver does not silently accept 1.0 as 0.2.
- A string-valued incompatible `agnir.version` declaration is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing, null, or wrong scalar/container Core-version serialization is `AGNIR_DISCOVERY_INCONSISTENT`.
- Local locator escape without an authorized external Locator Chain is `AGNIR_DISCOVERY_UNRESOLVABLE`; distinguishable denied external authorization is `AGNIR_DISCOVERY_UNAUTHORIZED`.
- State/Next Actions/non-null Decisions resolve to regular files; non-null Evidence resolves to a directory; baseline Evidence discovery exposes immediate regular-file children only.

## Independent implementation and RC acceptance

- The v1 independent-implementation gate is satisfied by issue #26, final verdict `PASS`.
- Core/profile `1.0` promotion was accepted on authoritative main through issue #27 / PR #28.
- Immutable `v1.0.0-rc.1` at `092945289f1a0a9803e4fe0583104aa380ceaadc` is accepted release evidence.
- RC workflow `34026167762` succeeded both on initial publication and a fresh immutable-source attempt; RC acceptance checkpoint is `afc07d062b957e8dbfe3f859834c787e64aa52be`.
- The RC tag must never be moved, retagged, or rewritten during stable publication.

## Stable v1.0.0 publication policy

- `release/v1.0.0` is a temporary staging/evidence lineage with logical identity `urn:agnir:lineage:v1.0.0` bound separately to selector `refs/heads/release/v1.0.0`.
- A green staging branch is not authoritative stable truth. Its product/package changes must be reconciled into `urn:agnir:lineage:authoritative` on `refs/heads/main`.
- Stable publication is **main-only** and remains dormant until authoritative exact-source conformance passes.
- The only stable publication arm message is `release: publish v1.0.0 stable` on `refs/heads/main`.
- Stable publication must create/verify immutable tag `v1.0.0` at that exact authoritative arm revision, create/verify a non-draft non-prerelease GitHub Release, verify `releases/latest == v1.0.0`, and verify accepted RC immutability.
- Stable publication does not authorize unrelated feature work or semantic redesign.

## Release and repository governance

- `v1.0.0` is a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.
- Repository `1.0.0`, Core `1.0`, and profile `repository-filesystem/1.0` align at the first stable 1.0 release while remaining distinct version axes in the architecture.
- `main` is the only intended long-lived authoritative branch. Release/validation/repair branches are temporary staging/evidence carriers and require explicit reconciliation before authoritative-main advancement.
- Published tags are immutable.
