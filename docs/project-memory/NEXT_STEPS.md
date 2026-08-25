# RPM Next Steps

## Immediate

1. Use the dedicated RPM ChatGPT Project as the maintenance workspace for this repository.
2. Set that ChatGPT Project to Project-only memory.
3. Add maintainer-focused Project Instructions that identify `mattamior/rpm` as the authoritative RPM specification repository.
4. On future RPM work, load `.chatgpt/project-memory.yaml`, `PROJECT_STATE.md`, and `NEXT_STEPS.md` before substantive changes.

## Near term

- Validate the self-hosted RPM setup during normal maintenance conversations.
- Add specification changes only when a recurring need is demonstrated by consuming projects.
- Keep consumer-project state out of this repository unless it is elevated into a general RPM rule, example, or compatibility requirement.
- Use versioning and migration rules when normative behavior changes.

## Open considerations

- Decide later whether RPM maintenance needs a specialized profile beyond `generic`; current classification is intentionally conservative.
- Consider adding a maintainer-specific instructions template only if it proves reusable enough to belong in the public RPM standard rather than being specific to this ChatGPT Project.
