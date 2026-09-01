# Agnir Next Actions

Agnir `0.1.0` pre-publication readiness is reopened because the accepted existing-Project upgrade contract is a material operational-surface change that must be included before the first stable publication.

1. **Publish one coherent upgrade implementation checkpoint** containing Skill upgrade procedure, repository/filesystem upgrade/provenance rules, executable upgrade classification, release gate updates, repository structure map updates, and durable Project continuity.
2. **Verify that exact revision** with the full GitHub Actions `Agnir conformance` workflow. Do not reuse the previously passing candidate `05103320afa25085d2cb9b65b249a8ad63e883e9` as evidence for the new upgrade semantics.
3. If the workflow fails, repair the earliest failed invariant in a new coherent checkpoint rather than patching individual files independently.
4. If the workflow passes, record the implementation revision and run/job as the new verified `0.1.0` publication candidate. A later observation-only checkpoint must not recursively redefine the candidate.
5. **Publication remains separately authorized:** only after explicit Principal authorization create tag `v0.1.0` / GitHub Release on the intended verified candidate.
6. After stable publication, upgrade older compatible Projects with the first-class `upgrade` operation. `latest stable` must resolve the published stable tag/release; it must not silently fall back to `main`.
7. Preserve compatible-upgrade invariants: keep Project identity, memory locators/content, unrelated README/`AGENTS.md`, and unrelated extensions; add/update only Agnir-owned procedure/provenance and material upgrade Evidence.
8. Treat Core/profile changes as migration-required, not compatible upgrade; surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` rather than silently changing compatibility lines.
9. Preserve optional `agnir/operations` provenance semantics and same-baseline upgrade no-op behavior.
10. Preserve transactional checkpoint, repository commit/push intent, activation, safe `AGENTS.md` merge, and Core storage/VCS neutrality.
11. Keep real mount-boundary validation optional until a real mount-capable environment exists.

## Stable maintenance constraints

- Root `SKILL.md` is the canonical Agent-facing operational package.
- `RELEASE.md` is the publication contract.
- `README.md` and `README.zh-CN.md` remain semantically synchronized for the activation/continuity surfaces they document.
- `.agnir/evidence/` remains represented by directory responsibility rather than per-evidence filename registration.
- `main` remains the only long-lived authoritative branch.
