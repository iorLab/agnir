# Agnir Active Decisions

This file records active durable decisions required to operate and evolve Agnir safely. Superseded chronology remains available through Git history and `.agnir/evidence/`.

## Project ownership and protocol boundary

- Agnir is a **project-owned durable continuity protocol**. The Project persists; Executors, conversations, execution environments, storage mechanisms, repository hosts, selectors, VCS refs, and integrations may change.
- Agnir Core is storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.
- Required durable semantics remain Current State, Next Actions, Decisions, and Evidence / Checkpoints.
- Svif is a separate Project orchestration product and may consume Agnir through a Continuity Provider integration. Agnir remains independently usable without Svif.

## Name origin and product meaning

- The project name **Agnir** is taken from Icelandic `agnir`, the nominative plural of `ögn`, meaning a tiny bit or particle.
- The metaphor maps to durable continuity being reconstructed from small discoverable pieces of Project truth rather than one Executor's private conversation context.
- The metaphor does not require one physical file/object per semantic category.

## Agent-operable activation and execution-surface handoff

- Root `SKILL.md` is the canonical Agent-facing operational procedure. User-facing install/upgrade requests remain short intents; the user does not carry Agnir's implementation checklist.
- An initialized repository Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared selected durable memory.
- `AGENTS.md` remains locator-only for Agnir; unrelated Project instructions are preserved, equivalent locators are idempotent, and material conflicts block completed activation until explicitly resolved.
- Repository activation and execution-surface activation are separate completion dimensions. Surface settings contain only enough persistent locator/bootstrap information to reach the Project; they do not duplicate Project durable truth or the Agnir procedure.
- Required persistent surface configuration that is pending or unverified blocks a claim that full fresh activation passed. ChatGPT Project Instructions remain the first concrete locator-only surface adapter, not an Agnir Core dependency.

## Checkpoint, commit, and push semantics

- A checkpoint is an authoritative continuity transition, not an activity-log append.
- Reconcile Project truth first. If authoritative continuity already represents it, checkpoint evaluation is a no-op.
- Material checkpoints construct a coherent candidate before publication and minimize writes to semantic categories that changed.
- Completed checkpoints must not expose mixed generations as coherent truth. Use atomic publication where available or durable generation/revision/transaction/pointer semantics otherwise.
- Stale-base writers surface `AGNIR_CHECKPOINT_CONFLICT`, re-resolve, and reconcile instead of overwriting newer truth.
- In repository context, authorized `commit` / `提交代码` means checkpoint evaluation before commit; `commit and push` / `提交推送` adds push and actual destination-ref verification.
- When Project and continuity changes can be represented together, prefer one VCS revision. A commit SHA may be a checkpoint receipt but must not be embedded as identity in the content that determines it.

## Compatible operational upgrade vs compatibility migration

- Upgrade is not re-initialization. Compatible operational upgrades preserve `project.identity`, memory locators/content, unrelated README/`AGENTS.md` instructions, unrelated extensions, and still-valid execution-surface locators.
- `latest stable` means an actually published stable tag/release. Moving `main`, prerelease branches, or untagged revisions are not silently substituted.
- Optional `extensions.agnir/operations` records which operational package was actually applied; it does not define Core/profile compatibility, Project identity, or lineage identity.
- A Core/profile compatibility-line change is migration-required and must surface `AGNIR_UPGRADE_MIGRATION_REQUIRED`-class behavior instead of a silent compatible rewrite.
- Core/profile `0.1` → `0.2` is a published stable migration contract. Existing `0.1` Projects remain supported compatibility/regression surfaces; the current published stable line is Core/profile `0.2`.

## Core 0.2 Continuity Lineages

- Core `0.2` generalizes Core `0.1`'s single implicit continuity line into multiple independently advancing **Continuity Lineages** owned by one Project.
- Project identity and logical lineage identity are distinct. Creating, selecting, advancing, integrating, rebinding a selector, or retiring a lineage does not implicitly create a new Project.
- Logical lineage identity is durable within Project scope and is not defined by a backend selector/locator or revision/checkpoint receipt.
- Git refs/worktrees are selector/binding context; Git SHAs, database generations, and snapshot revisions are checkpoint receipts/conflict tokens.
- Ordinary lineage-local work resolves exactly one lineage from explicit Principal/task/adapter input, trusted already-selected context, or an explicit default. Core does not require scanning sibling lineages.
- Missing deterministic lineage selection fails with `AGNIR_LINEAGE_REQUIRED` semantics. A selected unresolved/mismatched lineage/binding fails explicitly rather than falling back.
- Checkpoints are lineage-local by default and must not silently mutate sibling lineages.

## VCS lineage binding and fork behavior

- A selected Git ref/worktree is not itself logical lineage identity.
- Core/profile `0.2` VCS selector/binding/fork/rebind/integration semantics are governed by `spec/AGNIR_CORE_0_2.md` plus `profiles/REPOSITORY_FILESYSTEM_0_2.md`; the experimental `profiles/VCS_BRANCH_CONTINUITY.md` remains a Core/profile `0.1` compatibility/design surface and is not the normative `0.2` contract.
- An Agnir-aware lineage fork preserves Project identity and inherited baseline while establishing a new logical lineage identity and a new selector→lineage binding.
- When Agnir controls the fork, new lineage identity, selector binding, and coherent inherited/reconciled continuity must become visible together; sequential visible writes that temporarily expose copied source binding under the new selector are not the conforming publication path.
- Explicit ref rename/rebind may preserve logical lineage identity while changing selector string.
- External branch copy/rename with stale or ambiguous binding metadata is a classification/repair condition; Agnir must not guess fork vs rename.
- Ref deletion/recreation does not automatically restore a former lineage merely because the textual ref name matches.

## Lineage integration and target publication

- Integration is target reconciliation, not source-continuity copying.
- Target continuity is reconciled from the actual integrated Project candidate, prior target truth, relevant source continuity/Evidence, and current Principal intent/policy.
- Source State / Next Actions / Decisions / Evidence are inputs, never automatic target truth.
- When Agnir controls the path, target advancement is a publication boundary: capture target/source receipts → stage candidate while target remains unchanged → reconcile target → construct target checkpoint → publish integrated Project + reconciled target continuity together → fresh verify.
- Target or relevant source advancement after staging invalidates the candidate; stale integration must fail/re-resolve.
- A merge-first/follow-up-continuity-repair sequence is recovery-oriented, not the intended conforming normal path when Agnir knowingly controls publication.
- Cross-Project integration does not bypass Project identity validation.

## Repository/filesystem 0.2 and failure mapping

- `repository-filesystem/0.2` resolves one selected logical `continuity.lineage` plus its durable memory locators. Sibling enumeration is not required for ordinary cold-start resume.
- Stable `repository-filesystem/0.1` resolvers reject Core/profile `0.2` rather than silently interpreting it.
- A string-valued incompatible `agnir.version` declaration is `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; missing, explicit null, or wrong scalar/container Core-version serialization is schema-invalid and `AGNIR_DISCOVERY_INCONSISTENT`. After the `repository-filesystem/0.2` profile has been selected, a profile identifier mismatch is also `AGNIR_DISCOVERY_INCONSISTENT`.
- A local locator that escapes the selected Project root without an authorized external Locator Chain is `AGNIR_DISCOVERY_UNRESOLVABLE`; `AGNIR_DISCOVERY_UNAUTHORIZED` applies when a known external locator requires authorization that is absent or denied.
- Local State/Next Actions/non-null Decisions resolve to regular files; non-null local Evidence resolves to a directory and baseline discovery exposes only immediate regular-file children rather than recursively traversing nested directories.
- Filesystem indirection does not authorize external local Evidence: an immediate Evidence entry may resolve through an in-root indirection to an in-root regular file, but a canonical target outside the selected Project root must not be read without an authorized external Locator Chain and is `AGNIR_DISCOVERY_UNRESOLVABLE` on the ordinary local path.
- A Core `0.1` Project's one implicit continuity line becomes exactly one initial/default Core `0.2` logical lineage while preserving Project identity and material State / Next Actions / Decisions / Evidence.
- Migration is explicit, idempotent, cold-start verifiable, and conflict-safe. Repeating the same migration is a no-op; conflicting silent initial-lineage rebinding is a migration conflict.
- Concrete repository/filesystem migration stages against authoritative source state, rejects stale source mutation, publishes coherently, and verifies fresh Core/profile `0.2` discovery.

## Independent-implementation evidence policy

- v1 documentation quality must be demonstrated by a fresh implementer/reviewer who does not rely on private Agnir design-chat history or previous challenge clarification.
- A reviewer must reconstruct the public contract before inspecting `conformance/*_reference.py`, then independently implement or precisely specify the resolver/checkpoint path and preserve auditable receipts.
- A failed implementation is preserved as evidence but does not close the gate. Once Phase C exposes reference code, that session is no longer eligible as the fresh implementer for the next acceptance attempt.
- Public ambiguities or contradictions found by a challenge are repaired in public material; the gate is rerun from a new exact source revision and a genuinely fresh context.
- Core/profile `1.0` promotion and repository `1.0.0-rc` remain downstream of a successful independent-implementation gate.

## Real evidence and release direction

- Core `0.2` has non-VCS SQLite and VCS mapping/binding evidence, concrete profile/migration evidence, and real consumer evidence.
- Svif proved explicit migration, two independently advancing lineages, staged integration without target advancement, target reconciliation before publication, coherent target advancement, and independent source resume.
- FishUp and VocaPort add materially different migration/fresh-install evidence; VocaPort DSH provides the second accepted Agent execution surface.
- Genuine Linux Docker bind-mount checkpoint/fresh-resume evidence was accepted on 2026-09-04, including read-only checkpoint rejection and explicit missing/wrong-root discovery failures. The current v1 mount-boundary gate is satisfied; broader network filesystem/FUSE/Kubernetes-volume robustness remains optional future evidence.
- `v1.0.0` remains a stability/compatibility commitment governed by `V1_RELEASE_CRITERIA.md`, not a feature-count threshold.

## Documentation and repository governance

- `README.md` and `README.zh-CN.md` are parallel entry documents and preserve equivalent architecture, activation, migration, handoff, lineage, and continuity meaning.
- Before the architecture diagram they remain intentionally concise: Start Here / 从这里开始 → canonical Agnir Project Instructions → installed Project surface → Architecture.
- `REPOSITORY_TREE.md` is the exhaustive responsibility map; `.agnir/evidence/` is represented by directory responsibility rather than every Evidence filename.
- `main` is the only intended long-lived authoritative branch. Release/validation/repair branches are temporary evidence/staging carriers and require explicit reconciliation before authoritative-main advancement.
- Published tags are immutable. Stable `0.2.x` maintenance may repair documentation, conformance, packaging, or implementation without silently redefining Core/profile `0.2` semantics.
