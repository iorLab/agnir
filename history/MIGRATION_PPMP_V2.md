# Historical PPMP v2 -> Agnir Migration Guide

> **Status:** historical / optional migration guidance. This document is **not** part of the active Agnir Core `0.1` specification, conformance baseline, compatibility contract, or release gate.

PPMP v2.0.0 / Persistent Project Memory / Sandminni is predecessor history preserved on `legacy/ppmp-v2.0.0`. Agnir `main` is a greenfield protocol line and does not require backward compatibility with PPMP.

This guide exists only for a consumer that deliberately chooses to migrate an old PPMP Project into a new Agnir Project. Such a migration is explicit and semantic; renaming files or products is insufficient.

For an intentional migration, a useful transition should preserve these properties:

- material durable Project knowledge that the operator chooses to carry forward is explicitly reconciled;
- the target Project independently declares its Agnir Core compatibility;
- Current State, Next Actions, Decisions, and Evidence are resolvable as required by the target Agnir Project;
- an authorized Project Entry Point resolves the target Agnir Discovery Record and Locator Chain;
- a fresh Executor can cold-start the target Project without predecessor-private conversational context;
- backend/adapter assumptions remain outside Agnir Core;
- migration decisions and unresolved incompatibilities are recorded when they remain material to the target Project;
- predecessor history remains distinguishable from current Agnir conformance and evidence.

A migration tool **may** recognize predecessor artifacts such as `.chatgpt/project-memory.yaml` when the operator explicitly invokes migration behavior. Their presence alone never establishes Agnir conformance and must not affect greenfield Agnir discovery.

A consumer may model an explicit transition such as `PPMP v2 -> migration operation -> Agnir Project`, but Agnir Core itself does not define or require those modes.

For current Agnir semantics, use `spec/AGNIR_CORE.md`, `spec/AGNIR_DISCOVERY.md`, the applicable profile under `profiles/`, and the active conformance suite. Those current artifacts take precedence over this historical guide.