# RPM Next Steps

## Immediate

1. Design the normative architecture for **PPMP — Persistent Project Memory Protocol**, separating protocol semantics from implementation, persistence backend, and platform adapter behavior.
2. Produce a concrete RPM v1.0.0 classification/migration map for existing `spec/`, `profiles/`, and `templates/`: PPMP Core vs iorMemory implementation vs repository backend vs ChatGPT adapter.
3. Decide the target repository and directory strategy before renaming or moving normative files; preserve RPM v1 history and avoid destructive rename work before the migration design is explicit.
4. Define the initial **iorMemory** reference implementation boundary and its relationship to PPMP.

## Migration design

- Define PPMP's platform-neutral meaning of a Project and persistent/durable Project Memory.
- Define which current Core artifacts are protocol concepts versus one possible serialization/file representation.
- Generalize manifest/configuration semantics so PPMP does not require `.chatgpt/project-memory.yaml` or repository-relative paths.
- Move repository/Git-specific persistence and commit behavior into the iorMemory repository backend.
- Move ChatGPT first-substantive-turn bootstrap, `.chatgpt/` conventions, and Project isolation behavior into a ChatGPT adapter.
- Retain useful RPM v1 concepts including current-state vs history separation, decisions, next steps, meaningful session/checkpoint records, state vocabulary, conservative classification, composable profiles, event-driven persistence criteria, and compatibility/versioning where they remain protocol-level concerns.
- Define migration/versioning posture explicitly. Current working direction is to treat RPM v1.0.0 as the repository/ChatGPT-oriented prototype and introduce PPMP as a newly named protocol rather than silently reinterpret RPM v1.
- Decide whether the current `mattamior/rpm` repository is renamed/restructured or retained as historical/migration source after PPMP is formalized.
- Update the public website only after the protocol/implementation naming and repository migration strategy are settled.

## Existing operational follow-up

- Validate the deployed RPM website in a browser, including Home, Quick Start, Reference, and copy interactions.
- Continue validating the self-hosted RPM bootstrap and checkpoint flow while RPM v1 remains the active maintenance mechanism.
- Decide the public release posture, repository visibility, explicit LICENSE, and eventual custom domain in light of the PPMP/iorMemory transition.

## Open considerations

- Determine the canonical public identity and repository naming for PPMP versus iorMemory.
- Determine how multiple PPMP implementations advertise conformance and how implementation-specific extensions are namespaced.
- Determine whether persistence backends and platform adapters should have formal PPMP extension interfaces/profiles or remain implementation-level conventions initially.
- Consider future adapters for non-ChatGPT AI project/agent environments only after the platform-neutral protocol boundary is stable.
- Preserve design rationale without turning raw conversations into durable archives.
