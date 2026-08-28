# README language navigation deferred checkpoint — 2026-08-28

## Decision

A same-page English / Simplified Chinese language-switching treatment for the GitHub README was evaluated and deliberately **not adopted at this checkpoint**.

The active documentation layout remains:

- `README.md` — English entry point;
- `README.zh-CN.md` — Simplified Chinese entry point;
- each README links to the other as a separate Markdown document.

GitHub-native same-page alternatives such as anchor jumps or large `<details>` blocks may be revisited later, but they are not part of the current Agnir `0.1.0` publication surface.

## Scope

This checkpoint changes no README content, no Core `0.1` semantics, no `repository-filesystem/0.1` profile semantics, and no release compatibility identifiers.

It only records the current documentation-navigation choice so a future Executor does not infer that same-page language switching is an unfinished release blocker.

## Resume rule

Do not change the bilingual navigation behavior unless the Project explicitly revisits the language UX. The current publication path remains publication-only after the existing release-ready checks pass.
