# Agnir Next Actions

Agnir `v0.2.0-rc.1` is formally published as a prerelease at immutable tag target `50a8cd565954e7e8055b8b628e2d620ac7357bab`. Stable `latest` remains `v0.1.1`.

1. **Retire validation-only refs when a safe delete-ref path is available.** Draft PR #7 is already closed unmerged. Preserve validation commits/runs as Evidence and do not repurpose those refs as authoritative or release targets.
2. **Observe/stabilize the RC.** Use `v0.2.0-rc.1` for additional real install/migration/parallel-lineage pressure when useful. Any release-blocking Core/profile defect requires a new RC; never move the existing tag.
3. **Plan safe reconciliation back into authoritative `main`.** Stage accepted RC changes against current main, reconcile main continuity before target advancement, validate the exact candidate tree, then advance main coherently. Do not ordinary-merge release-line continuity into main.
4. **Decide final stable `v0.2.0` only after the RC cycle.** Stable publication remains separate from RC success; preserve `v0.1.1` as latest stable until an actually published stable `v0.2.0` exists.
5. Continue broader real-Project/execution-surface evidence toward `v1.0.0` and `V1_RELEASE_CRITERIA.md`.

## Published RC receipts

- tag `v0.2.0-rc.1` -> `50a8cd565954e7e8055b8b628e2d620ac7357bab`;
- Release id `381532232`;
- publication/conformance run `33675638723` success;
- Release `prerelease=true`, `draft=false`;
- post-publication checkpoint `df745e2486b1d3f5ab2b07e701a9a6f91451a056`; run `33676002813` success;
- Draft PR #7 closed with `merged=false`;
- `releases/latest` -> stable `v0.1.1` Release id `380414987`.

## Invariants

- Durable continuity belongs to the Project.
- Project identity != logical lineage identity != selector/revision receipt.
- Compatibility-line changes require explicit migration.
- Target publication is coherent and stale candidates fail.
- Published tags are immutable.
- RC/prerelease is not `latest stable`.
- `main` remains the only intended long-lived authoritative branch.
