# Agnir Next Actions

Agnir `0.1.0` is release-ready. Development work required for the initial stable release is complete, including durable Agent activation for Agent-operable `repository-filesystem/0.1` Projects.

1. **Publication only:** after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release.
2. After publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines. Any `0.1.x` maintenance must remain non-breaking.
3. Preserve the Agent activation invariant for Agent-operable repository Projects: Project root → `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → durable memory.
4. Existing initialized Projects should not require a recurring Agnir bootstrap prompt; if an execution surface ignores Project instruction files, handle that as one-time surface configuration rather than duplicating Agnir rules in user prompts.
5. Keep `AGENTS.md` locator-only and the README Agnir section canonical; do not let the two drift into competing instruction copies.
6. Reconcile future Svif dependency updates against stable Agnir Core/profile semantics, not repository internals or historical material.
7. Keep real mount-boundary validation as optional additional evidence when a real mount-capable environment exists; do not represent ordinary directories as mount evidence.
8. Keep the current bilingual README navigation (`README.md` ↔ `README.zh-CN.md`) unchanged unless the Project explicitly revisits same-page language UX.

## Documentation and conformance maintenance

- Both READMEs must keep the operational Quick Start before architecture material.
- Existing-Project Quick Start must state that correctly initialized Projects do not need a repeated Agnir prompt.
- New-Project initialization must remain self-contained and install the README canonical activation section plus root `AGENTS.md` locator while preserving unrelated existing content.
- Architecture/continuity changes must update both language diagrams in the same change set.
- `REPOSITORY_TREE.md` must track added/removed/moved files and material responsibility changes.
- Self-hosting conformance must continue to resolve Agent activation before `AGNIR.yaml` discovery and run the full `test_*.py` suite.

## Stable release baseline completed

- Core compatibility `0.1` frozen.
- Repository/filesystem profile compatibility `repository-filesystem/0.1` frozen for first publication.
- Repository SemVer `0.1.0`.
- All nine discovery failure classes have executable pressure.
- Non-repository SQLite continuity, external authorization, multi-project isolation, Locator Chain failures, symlink boundaries, and real Git worktree cold start are covered.
- Durable Agent activation implementation head `39d1e029e2b6fe8d47417f1e60c10dcbb0aef80c` passed conformance run `33165874089`.
- Activation evidence: `.agnir/evidence/2026-08-28-durable-agent-activation.md`.
- Main-only branch governance remains in force.
