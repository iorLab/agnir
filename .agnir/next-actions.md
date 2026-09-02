# Agnir Next Actions

Agnir `v0.1.0` remains the published stable release. The real `mattamior/skills-hub` ChatGPT execution-surface regression has passed, and `main` is being prepared as the repository `0.1.1` publication candidate without changing Core `0.1` or `repository-filesystem/0.1`.

1. Let the release-preparation changes settle on one final `0.1.1` publication-candidate revision and run the full GitHub Actions `Agnir conformance` workflow on that exact revision.
2. If and only if that exact candidate passes, create immutable tag `v0.1.1` and GitHub Release `Agnir v0.1.1` pointing to that exact verified revision; do not retarget publication to a later moving `main` head.
3. After publication, reconcile durable state/provenance to record the actual `v0.1.1` tag target, Release metadata, and verification run without changing the immutable tag.
4. Validate a compatible existing-Project upgrade from published `v0.1.0` to published `v0.1.1`, preserving Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
5. Continue broader real Project/surface validation as useful, while preserving the distinction between Project-owned activation and execution-surface locator adapters.
6. Preserve transactional checkpoint no-op/coherent publication semantics, stale-base safety, repository commit/push integration, prompt-free Project activation, non-destructive `AGENTS.md` merge, execution-surface handoff separation, and the README `Start Here -> Agnir Project Instructions -> Project surface -> Architecture` audience split.
7. Keep real mount-boundary validation optional until a genuine mount-capable environment exists.

## Closed v0.1.1 regression gate

- real execution surface: ChatGPT web Project `skills-hub`
- canonical target: `mattamior/skills-hub` / `main`
- persistent locator-only Project Instructions: configured
- genuinely fresh conversation: passed
- repeated bootstrap prompt/repository address in fresh conversation: not required
- durable Evidence: `.agnir/evidence/2026-09-01-v0.1.1-execution-surface-validation.md`

## Candidate compatibility

- Core compatibility: `0.1`
- repository/filesystem profile: `repository-filesystem/0.1`
- candidate repository SemVer: `0.1.1`
- currently published stable repository release: `0.1.0`

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- Required execution-surface settings are adapters/locators, not Project memory or Agnir Core.
- `RELEASE.md` is the publication contract for `0.1.1`.
- `.agnir/evidence/` remains represented by directory responsibility rather than per-evidence filename registration.
- `main` is the only intended long-lived authoritative branch.

## RC migration validation — 2026-09-03

This validation branch has completed the compatibility transition from the immutable published `v0.1.1` Project baseline to the explicitly authorized `0.2.0-rc.1` package baseline.

Next action for this temporary lineage is only to run fresh activation/discovery and the full conformance suite, record the result back on the RC release lineage, then retire this validation branch. Do not merge this validation branch into `main` or use it as the RC tag target.
