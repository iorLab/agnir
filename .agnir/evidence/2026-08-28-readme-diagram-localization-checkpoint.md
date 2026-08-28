# README Diagram Localization Checkpoint — 2026-08-28

## Scope

This checkpoint records the current Agnir documentation architecture after the bilingual README and comprehension-first diagram work.

## Durable facts

- `README.md` is the English project entry point.
- `README.zh-CN.md` is the Simplified Chinese project entry point.
- Both READMEs contain a current Architecture Diagram and Continuity Flow using Mermaid.
- Layer-model, discovery, Project-boundary, durable-continuity, or continuity-flow changes must update affected diagrams in both languages in the same change set.
- Localized diagrams are comprehension-first, not literal translations.
- In Simplified Chinese diagrams, each important node should communicate what the node is and what responsibility it has without requiring the reader to understand the English term first. English terminology may remain as a secondary parenthetical label where useful.
- This localization rule does not create a second semantic model; all localized READMEs describe the same canonical Agnir protocol architecture.

## Implementation evidence

- Chinese diagram clarification commit: `0f9f9ec3371fa6560d237bf7224adf5430bc0a19`.
- Localization-policy decision commit: `fbcbef93cd17434999e431b3d7af3af4c810c351`.
- Agnir conformance run `33142765236`: success.
- Repository/filesystem conformance job completed successfully.

## Resume point

Continue Agnir from the existing Core `0.1` conformance priorities: negative discovery fixtures, storage-neutral evidence, external-memory authorization, and multi-project isolation. Documentation diagrams must evolve in the same change set whenever those changes alter the layer model, discovery behavior, or continuity flow.
