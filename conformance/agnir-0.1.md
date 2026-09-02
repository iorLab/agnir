# Agnir 0.1 Conformance

This conformance layer validates stable Agnir Core `0.1`, `repository-filesystem/0.1`, and the repository's Agnir Agent Skill packaging without importing predecessor protocol requirements. It also contains experimental pressure for the repository/VCS branch-continuity extension; those extension cases do not redefine the stable Core/profile compatibility lines.

## Stable baseline

The executable suite covers:

- root `SKILL.md` Agent Skill frontmatter and the presence of the complete Agent-facing install / initialize / resume / checkpoint / commit / push / repair procedure;
- separation of the one-line user-facing install request from the detailed Agent-facing procedure;
- bilingual README Quick Starts pointing Agents to `SKILL.md` without embedding the internal installation checklist;
- non-destructive merge of the minimal Agnir locator into an existing `AGENTS.md` while preserving existing Project instructions;
- minimal `AGENTS.md` creation when absent, idempotent handling of an equivalent locator, and explicit conflict failure instead of silent overwrite when existing instructions contradict durable Agnir activation;
- self-hosting Agent activation from Project root through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml`;
- prompt-free fresh-Agent activation for an initialized Agent-operable repository Project;
- failure when the Agent activation locator is missing, does not reference the canonical README instruction, or forks an incomplete/duplicated activation contract;
- self-hosting `AGNIR.yaml` cold start;
- Core/profile version agreement and Project identity validation;
- required Current State / Next Actions resolution and optional Decisions / Evidence resolution;
- checkpoint no-op evaluation without synthetic durable mutation;
- coherent checkpoint publication as one authoritative generation and rejection of stale-base publication through `AGNIR_CHECKPOINT_CONFLICT` semantics;
- repository-context commit intent (`commit`, `提交`, `提交代码`) as checkpoint-before-commit and commit-and-push intent (`提交推送`) as checkpoint + commit + push + verification guidance;
- observed commits triggering evaluation rather than unconditional Agnir mutation;
- all named discovery failure classes: `NOT_FOUND`, `AMBIGUOUS`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, `UNRESOLVABLE`, `UNAUTHORIZED`, `CYCLE`, `STALE`, and `INCONSISTENT`;
- selected-root isolation for nested Projects;
- durable non-repository SQLite continuity, checkpoint, and fresh-resolver resume;
- external-memory authorization semantics using authorization references rather than plaintext secrets;
- multi-project workspace isolation with locator-only registry metadata;
- substrate-neutral Locator Chain cycle, stale, and material inconsistency pressure;
- symlinked Project Entry Point behavior and rejection of implicit symlink escape;
- real Git worktree cold start;
- bilingual README/documentation structure and exhaustive repository-tree maintenance.

`SKILL.md` is an Agent-facing distribution/operation surface, not an Agnir Core requirement that every Executor use an Agent Skill mechanism. Repository commit/push wording and hooks are integration semantics rather than Core keywords or VCS dependencies. The `AGENTS.md` merge reference is conformance-only pressure for the repository/filesystem Agent-operable initialization contract, not a production installer. The Agent activation fixture is a repository/filesystem profile pressure case, not a Core requirement that every Executor be an AI Agent or that every backend use `AGENTS.md` / `README.md`.

The reference models under `conformance/` are executable pressure tools, not promoted production implementations or mandatory backends.

## Experimental repository/VCS branch-continuity pressure

`profiles/VCS_BRANCH_CONTINUITY.md` adds an experimental extension layer on top of the stable repository/filesystem profile. Its executable pressure currently proves:

- working-ref selection prefers explicit task/adapter scope, then current checkout/worktree context, then a declared default; it never scans sibling branches to guess, and missing selection surfaces `AGNIR_VCS_REF_REQUIRED`;
- a real Git `main` worktree and feature worktree can resolve the same `project.identity` while carrying different branch-local Current State after divergence;
- a branch-local checkpoint snapshot does not mutate a sibling branch snapshot;
- merge, rebase, and cherry-pick are continuity-integration boundaries that require explicit target reconciliation rather than automatic source-state promotion;
- a real Git merge can be staged without advancing `main`, have conflicting branch-local continuity explicitly reconciled, and then advance the target exactly once to a two-parent merge revision whose Agnir state already describes the integrated target;
- integration across different Project identities is rejected;
- rebase/history rewrite can replace revision receipts without redefining Project identity or otherwise coherent branch truth;
- push verification follows the actual destination ref, while a claim of authoritative publication additionally requires the declared `authoritative_ref`.

The target-ref publication case is important: “merge first, repair Agnir afterward” is not the preferred branch-continuity-safe sequence when the first merge revision would expose source-branch state as target truth. An Agnir-aware integration should stage the Project merge/result, reconcile target continuity, and publish both together when it controls target ref advancement. External/server-side integration that has already advanced an unreconciled target is recovery territory and must surface `AGNIR_VCS_RECONCILIATION_REQUIRED` until repaired.

These cases intentionally do **not** introduce a durable generic `lineage.id`, change Agnir Core `0.1`, or change the `repository-filesystem/0.1` discovery schema. Their purpose is to pressure-test branch-aware repository behavior before deciding whether any storage-neutral continuity-lineage invariant deserves a future Core compatibility line.

## Known unproven boundary

A real mount-boundary case remains unproven because the current environment does not provide a real mount-capable fixture. An ordinary directory MUST NOT be represented as equivalent mount evidence.

A generic non-VCS continuity-lineage abstraction is also intentionally unproven. Current branch tests establish repository/VCS behavior only; they are insufficient evidence by themselves to promote `lineage` into Agnir Core.

## Release interpretation

Passing the stable portion of this suite establishes the reference repository's published Core `0.1` / profile `repository-filesystem/0.1` conformance baseline and the Agent Skill packaging boundary. For checkpoint semantics it additionally proves no-op behavior, coherent single-generation publication, and stale-base conflict rejection in a substrate-neutral reference model. For an Agent-operable repository initialized under the reference convention, it additionally proves that existing root Agent instructions are preserved during Agnir locator installation, explicit contradictory instructions are surfaced rather than overwritten, the activation route itself is durable, future Agents do not require the original initialization prompt or conversation, and repository-context commit/push intent remains a durable checkpoint boundary.

Passing the experimental branch-continuity tests establishes only the behavior claimed by `agnir/vcs-branch-continuity/0.1`; it does not by itself graduate that extension into the stable Core/profile contract.

It does not imply that every possible backend, adapter, filesystem, authorization system, Agent Skill installer, VCS, repository hook, Agent instruction mechanism, semantic conflict form, or execution environment has been tested.
