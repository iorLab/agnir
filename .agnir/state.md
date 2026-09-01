# Agnir Current State

Agnir `v0.1.1` is formally published as the current stable repository release. The execution-surface activation handoff repair passed repository conformance and the real ChatGPT `skills-hub` fresh-context regression before publication.

Durable continuity belongs to the Project, not an Executor, conversation, execution environment, repository host, or storage implementation.

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

## Stable upgrade status

`latest stable release` now resolves to published `v0.1.1`. Existing compatible Agnir Projects on Core `0.1` / `repository-filesystem/0.1` may upgrade from `v0.1.0` to `v0.1.1` as a compatible operational upgrade. Such an upgrade preserves Project identity, declared memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions, while optionally recording `extensions.agnir/operations` provenance.

Core/profile compatibility changes remain migration-required and must surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than being silently rewritten.

## Repository and documentation invariants

Root `SKILL.md` remains the canonical Agent-facing operational package. The Project-owned activation route remains `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → declared durable memory. Execution-surface configuration stays outside the Project-owned tree and remains locator-only.

Transactional checkpoint semantics, stale-base `AGNIR_CHECKPOINT_CONFLICT`, contextual commit/push intent, one-revision preference, prompt-free Project activation, and safe non-destructive `AGENTS.md` merge remain active.

## Branch governance

`main` remains the only intended long-lived authoritative branch. Historical recovery and releases use immutable commit SHAs/tags rather than live legacy refs.
