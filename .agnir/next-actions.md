# Agnir Next Actions

Agnir `v0.2.0-rc.1` is published as an immutable prerelease. Authoritative `main` is reconciled to Core `0.2` / `repository-filesystem/0.2` on logical lineage `urn:agnir:lineage:authoritative`, separately bound to selector `refs/heads/main`. Stable `latest` remains `v0.1.1`.

1. **Fresh-verify authoritative main after target publication.** Require Core/profile `0.2` self-host cold start, stable Core/profile `0.1` regression pressure, VCS/lineage/profile/migration coverage, RC fresh-install/published-migration coverage, and the full suite on the exact published main revision. If verification exposes a defect, repair from newly resolved main truth; do not move the existing RC tag.
2. **Observe/stabilize `v0.2.0-rc.1`.** Use the immutable RC for additional real install, migration, and parallel-lineage pressure when useful. Any release-blocking Core/profile defect requires a new RC rather than mutating `v0.2.0-rc.1`.
3. **Decide and construct stable `v0.2.0` separately.** Only after the RC cycle is accepted, build an exact stable candidate from authoritative main, update stable-release metadata deliberately, validate exact-candidate conformance and upgrade/migration behavior, then publish an immutable stable tag/release. Until then `v0.1.1` remains latest stable.
4. **Retire temporary validation/integration refs when a safe delete-ref path is available.** Preserve their commits/runs as Evidence and never repurpose them as authoritative or release targets.
5. Continue broader real-Project/execution-surface evidence toward `v1.0.0` and `V1_RELEASE_CRITERIA.md`.

## Current receipts

- pre-reconciliation main: `f0b2cbd5329adb6ac7309076d7ea09337bb057c5`;
- accepted release-line head: `866604c4532003538fd6a0b565be9c1ef1c8a034`;
- immutable RC tag: `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`;
- RC Release id: `381532232`;
- publication/conformance run: `33675638723` success;
- release post-publication run: `33676002813` success;
- release hygiene run: `33676171048` success.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Source continuity is reconciliation input, not target truth.
- Core/profile compatibility changes require explicit migration.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch.
