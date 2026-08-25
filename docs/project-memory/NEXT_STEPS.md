# RPM Next Steps

## Immediate

1. Validate the self-hosted RPM bootstrap and checkpoint flow during normal maintenance conversations.
2. Use the first consuming-project upgrade or maintenance case to test whether RPM v1.0.0 instructions are sufficient without relying on cross-project chat memory.
3. Capture any confirmed specification defects or reusable compatibility requirements in the appropriate normative files rather than only in chat.

## Near term

- Review the original RPM design conversation only when useful for rationale, regression analysis, or detecting an omitted durable decision; do not treat it as authoritative state.
- Add specification changes only when a recurring need is demonstrated by consuming projects.
- Keep consumer-project state out of this repository unless it is elevated into a general RPM rule, example, or compatibility requirement.
- Follow `spec/VERSIONING.md` whenever normative behavior changes and assess migration impact for existing manifests.

## Open considerations

- Decide later whether RPM maintenance needs a specialized profile beyond `generic`; current classification is intentionally conservative.
- Consider adding a maintainer-specific instructions template only if it proves reusable enough to belong in the RPM standard rather than remaining specific to this ChatGPT Project.
- Consider whether design-rationale provenance needs a lightweight normative convention if future maintenance repeatedly requires reconstructing why a rule exists; do not add such a mechanism solely to archive conversations.
