# iorMemory Next Steps

## Immediate

1. Update the public website presentation from RPM v1 language to iorMemory v2 / Persistent Project Memory terminology while keeping it non-normative.
2. Migrate remaining profile and example headers/configuration to iorMemory v2 and remove stale RPM-v1-only normative wording.
3. Validate the repository-backed PPM bootstrap/checkpoint flow using the v2 manifest/template in this maintenance project.
4. Decide whether and when to rename the GitHub repository from `mattamior/rpm`; repository naming is now operational branding, not protocol semantics.

## Near term

- Add an explicit LICENSE before broader public promotion.
- Consider a dedicated iorMemory domain after website content and repository identity are aligned.
- Add conformance metadata/version declarations for future PPM releases.
- Add additional persistence backends or platform adapters only when there is a concrete implementation need.
- Preserve RPM v1 history and migration rationale without archiving raw conversations.

## Validation

- Confirm all normative v2 files agree on version 2.0.0 and layer boundaries.
- Confirm no protocol-level requirement depends on Git, repository paths, `.chatgpt/`, or ChatGPT-specific lifecycle events.
- Confirm RPM v1 projects are treated as requiring explicit migration.
