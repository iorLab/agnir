# Agnir Next Actions

Agnir `0.1.0` is release-ready. Development work required for the initial stable release is complete, including the root Agent Skill package, safe existing-`AGENTS.md` merge behavior, and durable target-Project activation.

1. **Publication only:** after explicit authorization, create tag `v0.1.0` on the intended publication commit and/or create the GitHub Release.
2. After publication, keep Core `0.1` and `repository-filesystem/0.1` frozen compatibility lines. Any `0.1.x` maintenance must remain non-breaking.
3. Preserve the packaging boundary: README gives the user one short installation request; root `SKILL.md` owns the detailed Agent install / initialize / resume / checkpoint / repair procedure.
4. Preserve the post-install activation invariant for Agent-operable repository Projects: Project root → `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → durable memory.
5. Preserve the target `AGENTS.md` merge invariant: absent means create a minimal locator; existing means non-destructive merge; equivalent locator means idempotent no-op; material conflict means surface to the Principal and do not silently overwrite or claim installation complete.
6. Existing initialized Projects must not require a recurring Agnir bootstrap prompt. If an execution surface ignores Project instruction files, handle that as one-time surface configuration rather than duplicating Agnir procedure in user prompts.
7. Keep target `AGENTS.md` locator-only and the target README Agnir section canonical; do not let them drift into competing instruction copies.
8. Reconcile future Svif dependency updates against stable Agnir Core/profile semantics, not Skill packaging internals or historical material.
9. Keep real mount-boundary validation as optional additional evidence when a real mount-capable environment exists; do not represent ordinary directories as mount evidence.
10. Keep the current bilingual README navigation (`README.md` ↔ `README.zh-CN.md`) unchanged unless the Project explicitly revisits same-page language UX.

## Documentation and conformance maintenance

- Both READMEs must keep a user-facing Quick Start before architecture material.
- The new-Project Quick Start must retain the one-line install prompt and point the Agent to root `SKILL.md`; it must not embed the Agent implementation checklist.
- Root `SKILL.md` must remain self-contained enough for an Agent that has only the user's short installation intent plus access to this repository.
- Existing-Project Quick Start must state that correctly initialized Projects do not need a repeated Agnir prompt.
- `conformance/test_agents_merge.py` must continue to pressure-test existing-content preservation, minimal creation, idempotence, and explicit conflict failure.
- Architecture/continuity changes must update both language diagrams in the same change set.
- `REPOSITORY_TREE.md` must track added/removed/moved files and material responsibility changes.
- Self-hosting conformance must continue to validate Skill packaging before Agent activation / `AGNIR.yaml` discovery and run the full `test_*.py` suite.

## Stable release baseline completed

- Core compatibility `0.1` frozen.
- Repository/filesystem profile compatibility `repository-filesystem/0.1` frozen for first publication.
- Repository SemVer `0.1.0`.
- Root `SKILL.md` is the canonical Agent-facing operational package.
- Bilingual READMEs expose one-line user installation prompts rather than the internal checklist.
- `conformance/test_skill_package.py` and self-host checker enforce the user-prompt / Skill-procedure boundary.
- `conformance/agents_merge_reference.py` and `test_agents_merge.py` enforce the non-destructive target-`AGENTS.md` merge baseline.
- Durable target-Project activation remains covered by `activation_reference.py` and `test_agent_activation.py`.
- All nine discovery failure classes have executable pressure.
- Non-repository SQLite continuity, external authorization, multi-project isolation, Locator Chain failures, symlink boundaries, and real Git worktree cold start are covered.
- Safe-merge candidate `8b07f25b4ec3decbec0b2e410778db3b247cac47` passed the repository-filesystem CI job in workflow run `33185018378`.
- Main-only branch governance remains in force.
