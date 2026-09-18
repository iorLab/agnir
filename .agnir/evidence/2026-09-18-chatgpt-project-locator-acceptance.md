# ChatGPT Project locator simplification acceptance

Date: 2026-09-18

## Accepted result

The Principal accepted the locator-only ChatGPT Project Instruction as the permanent Agnir packaging direction, conditional on preserving Agnir continuity.

Accepted handoff:

```text
Canonical Project: <owner/repository> (<ref>)
At the first substantive turn of every new conversation, open it, read root AGENTS.md, and follow it before doing Project work.
```

## Why continuity is preserved

The persistent ChatGPT Project Instruction is not the continuity store and is not the Agnir procedure. Its only job is to locate the canonical Project and enter the Project-owned activation route.

The durable chain remains:

`AGENTS.md -> AGNIR.md -> AGNIR.yaml -> selected durable continuity`

Therefore removing duplicated `AGNIR.yaml`, durable-truth, checkpoint, and repository-operation prose from ChatGPT Project Instructions does not remove those semantics. It makes one Project-owned copy authoritative and reduces semantic drift between execution-surface configuration and repository truth.

This guarantee is within the Agnir integration contract: a fresh execution surface must honor its persistent locator and be able to access the canonical Project. Agnir cannot independently guarantee behavior of a surface that ignores its configured instructions or cannot access the Project.

## Implementation receipts

- implementation PR: `#58`;
- candidate source head: `6be7d8a3587ed2c043a41f6ec0b4c48c60ea2c6d`;
- PR conformance run: `35334360203` — success;
- authoritative squash merge: `2c62d026c48405c3e299f0f57d6a674b3f6f9e1c`;
- authoritative post-merge conformance run: `35353464865` — success;
- candidate evidence: `.agnir/evidence/2026-09-18-chatgpt-project-locator-simplification.md`.

The conformance suite now requires the ChatGPT handoff block to remain exactly locator-oriented and rejects reintroduction of duplicated `AGNIR.yaml`, durable-truth, ChatGPT-memory, checkpoint, Current State, or Next Actions semantics into that block.

## Semantic boundary

No Agnir Core/profile change occurred.

Unchanged:

- Core `1.0`;
- `repository-filesystem/1.0`;
- Project identity and Continuity Lineage semantics;
- checkpoint semantics;
- repository activation and fresh recovery semantics.

This is accepted packaging/onboarding hardening.

## Follow-up observation

A genuinely fresh ChatGPT Project initialization should be observed when the next natural case occurs. The expected behavior is that the installer offers the accepted short locator directly. If it again generates a long Project Instruction, treat that as an execution-surface packaging regression and keep the locator-only contract intact.
