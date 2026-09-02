# Agnir Current State

Agnir `v0.1.1` is formally published as the current stable repository release. The execution-surface activation handoff repair passed repository conformance and the real ChatGPT `skills-hub` fresh-context regression before publication.

Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.

## Active experimental branch — 2026-09-02

A temporary development branch, `feature/multibranch-continuity`, is actively pressure-testing multi-branch Agnir behavior while `main` remains the only long-lived authoritative branch for this repository.

- Project identity remains `urn:agnir:project:agnir-core` on both `main` and the feature branch.
- Draft PR: `#4` — `Add branch-aware VCS continuity extension`.
- Experimental extension: `agnir/vcs-branch-continuity/0.1` in `profiles/VCS_BRANCH_CONTINUITY.md`.
- Stable compatibility is unchanged: Agnir Core `0.1` + `repository-filesystem/0.1`.
- Branch/ref names remain VCS locators/runtime observations, not Project identity and not a new Core field.
- A generic durable `lineage.id` remains deliberately deferred until non-VCS evidence shows that a storage-neutral lineage concept belongs in Core.

The branch currently implements:

- branch-local continuity isolation for divergent refs/worktrees;
- merge/rebase/cherry-pick as explicit continuity-reconciliation boundaries;
- `AGNIR_VCS_RECONCILIATION_REQUIRED` when an integration result exists but target continuity has not been reconciled;
- Project-identity preservation across rebase/history rewrite while commit/revision IDs remain checkpoint receipts rather than identity;
- destination-ref-first push verification, with `authoritative_ref` enforced only for an explicit authoritative-publication claim;
- Agent Skill and bilingual README guidance for the same semantics;
- an explicit experimental CI step separate from stable `0.1` self-hosting conformance.

A focused isolated execution of the seven new branch-continuity tests passed, including a real Git worktree divergence case. Full repository CI is **not yet proven on this branch**: GitHub has not emitted an Actions run/status for the connector-created PR synchronizations, and the current head has no combined commit statuses. This absence must not be reported as a pass.

The feature branch now carries its own Agnir checkpoint rather than pretending `main`'s pre-branch Current State is sufficient. If/when this work is merged, `main` MUST reconcile the actual merge result and publish a new target-branch checkpoint; this feature-branch Current State MUST NOT be promoted wholesale into `main`.

Evidence: `.agnir/evidence/2026-09-02-multibranch-continuity-development.md`.

## Published release

- repository release: `0.1.1`
- Git tag: `v0.1.1`
- tag target: `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- GitHub Release id: `380414987`
- Release title: `Agnir v0.1.1`
- published at: `2026-09-01T10:47:58Z`
- draft: false
- prerelease: false
- exact-candidate conformance run: `33499092957`
- publication workflow run: `33499228486`

The tag resolves directly to exact verified candidate `e9712357ab590e5c1e5357b3cf3219d07d789aff`. Later `main` checkpoints are post-release maintenance and do not redefine the immutable `v0.1.1` release target.

## Active compatibility contract

- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
- published repository release: `0.1.1`
- Agnir Core remains storage-, platform-, VCS-, repository-, Agent-, Skill-, and execution-surface-neutral.

## v0.1.1 patch result

The patch closes the execution-surface completion gap discovered during real ChatGPT web Project initialization of `mattamior/skills-hub`:

- repository activation and execution-surface activation are separate completion dimensions;
- surfaces that require persistent Project/workspace configuration are configured when possible or receive a copy-ready locator-only handoff;
- pending/unverified required surface configuration blocks a claim that full fresh activation passed;
- ChatGPT Project Instructions remain an execution-surface adapter and do not duplicate Project durable truth or the full Agnir procedure;
- completion reporting distinguishes repository activation from execution-surface activation;
- bilingual README architecture/continuity documentation and executable regression pressure preserve the boundary.

The real `skills-hub` regression passed after the persistent locator-only Project Instructions were configured: a genuinely fresh conversation, given only an ordinary Project-status request, located `mattamior/skills-hub` and began reading root `AGENTS.md`, `AGNIR.yaml`, and declared durable continuity without a repeated Agnir bootstrap prompt.

Evidence:

- `.agnir/evidence/2026-09-01-execution-surface-activation-regression.md`
- `.agnir/evidence/2026-09-01-v0.1.1-execution-surface-validation.md`
- `.agnir/evidence/2026-09-01-v0.1.1-publication.md`

## Existing-Project upgrade validation

A real compatible upgrade from the pre-provenance Agnir setup in `mattamior/skills-hub` to published `v0.1.1` has passed.

- target Project pre-upgrade revision: `f94c3894ec9412724607febbc27b25408a9a90cc`
- upgrade revision: `f8ec9fbb429df6a8eaa0aa837906a5897ffbb210`
- classification: compatible operational upgrade
- preserved Core/profile: `0.1` / `repository-filesystem/0.1`
- preserved Project identity and all declared memory locators/content
- recorded `extensions.agnir/operations` release `0.1.1` with applied revision `e9712357ab590e5c1e5357b3cf3219d07d789aff`
- target repository validation workflow: `Validate skills` run `33500075237`
- target validation conclusion: `success`

The target Project's existing README Agnir contract and locator-only `AGENTS.md` already satisfied the v0.1.1 repository activation contract, so they were not rewritten. The ChatGPT Project locator established during the earlier fresh-context regression remained valid because canonical repository/ref, activation route, Project identity, and memory locators did not change.

Evidence: `.agnir/evidence/2026-09-01-v0.1.1-existing-project-upgrade-validation.md`.

## Stable upgrade status

`latest stable release` resolves to published `v0.1.1`. Existing compatible Agnir Projects on Core `0.1` / `repository-filesystem/0.1` may upgrade to `v0.1.1` as a compatible operational upgrade. Such an upgrade preserves Project identity, declared memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions, while optionally recording `extensions.agnir/operations` provenance.

Core/profile compatibility changes remain migration-required and must surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than being silently rewritten.

## Repository and documentation invariants

Root `SKILL.md` remains the canonical Agent-facing operational package. The Project-owned activation route remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory. Execution-surface configuration stays outside the Project-owned tree and remains locator-only.

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free Project activation, and safe non-destructive `AGENTS.md` merge remain active. On the experimental branch, branch-local checkpoint isolation and integration reconciliation are additional extension-level invariants under pressure.

## Branch governance

`main` remains the only intended long-lived authoritative branch. `feature/multibranch-continuity` is a temporary development branch with branch-local continuity for the duration of its work. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
