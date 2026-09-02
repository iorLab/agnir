# Agnir Current State

Agnir `v0.1.1` remains the formally published stable repository release, immutably anchored to `e9712357ab590e5c1e5357b3cf3219d07d789aff`. **Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, storage implementation, repository host, VCS branch, selector, or Continuity Lineage.

## Core 0.2 safe main integration completed — 2026-09-02

The combined PR `#4` + PR `#5` Core `0.2` Project result has been integrated into authoritative `main` through the Agnir-aware publication path.

Exact integrated revision: `a32c9143687b72426617ddd701b90ffd237a111c`.

- first parent: previous authoritative `main` `1bbdb5b258645ec7c5e0109c9b17dbaac004e625`;
- second parent: Core `0.2` source checkpoint `68cc443d6c44929f1b71d9d534e9b0f73f9745bf`;
- exact tree: `759766c34e0f39f0c8d51bea1af22d7d41ad591c`.

A temporary validation PR `#6` produced test merge `270265a4d76b92553176a5a0b281f9202b7644fd`; its tree SHA was exactly the same `759766c...` as the candidate. Candidate-tree conformance run `33653019074` passed every gate while authoritative `main` remained unchanged.

Immediately before publication, fresh ref reads still observed `main` at `1bbdb5b...` and source `feature/core-0.2-lineage` at `68cc443d...`. `main` then advanced once directly to exact candidate `a32c914...`, with no feature-truth-first/follow-up-repair interval.

Authoritative-main push run `33653087179` passed stable Core `0.1` self-hosting, VCS branch continuity, Core `0.2` non-VCS/VCS mapping, repository-filesystem `0.2`, VCS lineage binding, semantic and concrete `0.1`→`0.2` migration, and the full suite.

## Compatibility and release status

- published stable repository release remains `v0.1.1`;
- stable tag target remains `e9712357ab590e5c1e5357b3cf3219d07d789aff`;
- the repository still self-hosts Core `0.1` + `repository-filesystem/0.1` on authoritative `main`;
- Core `0.2` + `repository-filesystem/0.2` contracts/conformance are now integrated on `main` as the **pre-RC** line, not yet published as stable compatibility;
- `VERSION` and operational provenance remain `0.1.1` until the RC release change is intentionally constructed.

## PR integration result

- PR `#4` was automatically recognized as merged through ancestry when `main` advanced to `a32c914...`;
- temporary validation PR `#6` was likewise recognized as merged at the exact candidate revision;
- stacked PR `#5` could not be auto-recognized because its base remained the feature branch. Its head is already the second-parent ancestry of `a32c914...`; a completion comment was recorded and the PR was closed without creating another merge path.

## Core 0.2 readiness

Synthetic/backend/profile/migration gates, the first real Svif consumer validation, exact candidate-tree validation, coherent main publication, and authoritative-main conformance are all green.

The next release boundary is `v0.2.0-rc.1`. RC work should occur on a temporary release branch, deliberately promote the intended Core/profile contracts, update repository release metadata, exercise fresh install, and validate explicit published `v0.1.1` Core/profile `0.1` → Core/profile `0.2` migration/resume before final `v0.2.0` publication.

`.agnir/next-actions.md` is the canonical resume order. Exact integration evidence is recorded in `.agnir/evidence/2026-09-02-core-0.2-main-integration-completed.md`.
