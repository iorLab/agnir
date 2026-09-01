# Agnir Next Actions

Agnir `v0.1.0` is formally published and verified on exact candidate `2a0cb7bf2068b11f361e315670b2f2dc497b2588`.

1. Synchronize `RELEASE.md` from pre-publication wording to the already-published `v0.1.0` state without changing the immutable release tag.
2. Continue real existing-Project upgrade validation against published stable `v0.1.0`. Svif is already one successful compatible-upgrade case; add broader Project/surface evidence as useful while preserving Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions.
3. Record `agnir/operations` provenance when known; legacy Projects without provenance remain valid compatible-upgrade inputs.
4. Treat Core/profile changes as migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.
5. Preserve transactional checkpoint no-op/coherent publication semantics, stale-base safety, repository commit/push integration, prompt-free activation, non-destructive `AGENTS.md` merge, and the README `Start Here -> Agnir Project Instructions -> Architecture` audience split.
6. Keep real mount-boundary validation optional until a genuine mount-capable environment exists.

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
