# Agnir Next Actions

Agnir `v0.1.0` is formally published and verified on exact candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`.

1. Delete temporary branch `release-v0.1.0-candidate`; it existed only to let the GitHub web Release UI create `v0.1.0` on the verified candidate and is not a long-lived branch.
2. Synchronize `README.md`, `README.zh-CN.md`, and `RELEASE.md` from pre-publication wording to published `v0.1.0` status without changing the published tag.
3. Begin real existing-Project upgrade validation against published stable `v0.1.0`. Preserve Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
4. Record `agnir/operations` provenance when known; legacy Projects without provenance remain valid compatible-upgrade inputs.
5. Treat Core/profile changes as migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.
6. Preserve transactional checkpoint no-op/coherent publication semantics, stale-base safety, repository commit/push integration, prompt-free activation, and non-destructive `AGENTS.md` merge.
7. Keep real mount-boundary validation optional until a genuine mount-capable environment exists.

## Published release verification

- tag: `v0.1.0`
- tag target: `2a0cb7bf2068b11f361e315670b2f2dc497b2588`
- GitHub Release id: `380187574`
- published at: `2026-09-01T03:09:36Z`
- draft: false
- prerelease: false

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- `RELEASE.md` is the publication/maintenance contract.
- `.agnir/evidence/` remains represented by directory responsibility rather than per-evidence filename registration.
- `main` is the only intended long-lived authoritative branch.
