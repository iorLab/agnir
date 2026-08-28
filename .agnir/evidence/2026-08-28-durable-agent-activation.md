# Durable Agent Activation — 2026-08-28

## Problem

The first README Quick Start still required a user to paste an Agnir prompt into an already initialized Project, while the initialization prompt assumed the Agent already knew what Agnir meant. That left a bootstrap gap: durable memory existed, but the instruction telling a future general-purpose Agent to load that memory was not itself guaranteed to be durable.

## Resolution

For Agent-operable Projects using `repository-filesystem/0.1`, initialization now persists this reference activation route:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

The profile now requires the README section to carry the canonical Agnir activation semantics and requires root `AGENTS.md` to point to that section rather than duplicate the full contract. Initialization must preserve unrelated existing README/AGENTS content and finish with a fresh-agent activation test.

The user-facing initialization prompt is self-contained: it explains what Agnir is, creates/validates the manifest and durable memory, installs the README activation instruction and `AGENTS.md` locator, and verifies a fresh Project-root-only resume path.

An already initialized Project therefore requires no recurring Agnir bootstrap prompt. Execution surfaces that do not inspect Project instruction files may require one-time surface configuration, which is outside Agnir Core.

## Executable pressure

Added:

- root `AGENTS.md` self-host activation locator;
- `conformance/activation_reference.py`;
- `conformance/test_agent_activation.py`;
- self-host checker activation before `AGNIR.yaml` discovery.

The fixture proves successful Project-root-only activation and negative cases for missing `AGENTS.md`, an unresolved README reference, incomplete canonical README activation, and duplicated/forked activation rules in `AGENTS.md`.

Implementation head `39d1e029e2b6fe8d47417f1e60c10dcbb0aef80c` passed Agnir conformance run `33165874089`.

## Compatibility boundary

This change was completed before the first `v0.1.0` publication. It is part of the initial `repository-filesystem/0.1` Agent-operable initialization contract. It does not change Agnir Core `0.1`: Core remains agent-, filesystem-, repository-, and execution-surface-neutral.
