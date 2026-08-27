# PPMP v2 -> Agnir 0.1 Migration

PPMP v2.0.0 / Persistent Project Memory / Sandminni is predecessor history. Migration to Agnir is explicit and semantic; renaming files or products is insufficient.

A predecessor Project reaches Agnir mode only when:

- required durable knowledge is preserved;
- target Agnir Core compatibility is declared;
- Current State, Next Actions, Decisions, and Evidence are resolvable as required;
- an authorized Project Entry Point resolves an Agnir Discovery Record and Locator Chain;
- a fresh Executor completes cold-start discovery without predecessor-private context;
- backend/adapter assumptions remain outside Core;
- material migration decisions and unresolved incompatibilities are durably recorded;
- predecessor conformance/history remains distinguishable from target Agnir conformance.

Migration-capable implementations MAY recognize `.chatgpt/project-memory.yaml` as an explicit predecessor fallback, but its presence alone never establishes Agnir conformance.

The recommended transition states are `PPMP v2 mode -> migration mode -> Agnir 0.1 mode`. Implementations MUST NOT silently promote a Project between these modes.
