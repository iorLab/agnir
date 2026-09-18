# ChatGPT Project locator simplification candidate

Date: 2026-09-18
Branch: `fix/chatgpt-project-locator-minimal`
External conversation reference: https://chatgpt.com/share/6aad0f54-7ab0-83e8-8e8d-9aff4de22cd8

## Trigger

The Principal reported a real Agnir initialization attempt in ChatGPT web where the installer repeatedly proposed overly detailed Project Instructions. Only after several rounds of correction did it converge on the desired simple persistent instruction.

This is material adoption feedback because fresh-session recovery depends on users being able to configure an execution surface correctly without understanding or editing Agnir's internal procedure.

## Root cause

The stable documentation already says the execution-surface bootstrap must **append Project locator only**.

However, root `SKILL.md` contradicted that rule for ChatGPT Projects by providing a persistent handoff that duplicated:

- `AGNIR.yaml` continuity loading;
- repository-managed durable-truth authority;
- ChatGPT memory versus Project truth;
- checkpoint behavior before finish/commit/push.

Those semantics are already Project-owned behind the activation route:

`AGENTS.md -> AGNIR.md -> AGNIR.yaml -> durable continuity`.

The surface handoff had therefore become a second, partial procedure copy instead of a locator.

## Candidate correction

The ChatGPT Project handoff is reduced to:

```text
Canonical Project: <owner/repository> (<ref>)
At the first substantive turn of every new conversation, open it, read root AGENTS.md, and follow it before doing Project work.
```

The Skill explicitly forbids copying Agnir discovery, continuity-authority, checkpoint, or repository-operation semantics into persistent Project Instructions when they are already reachable through the repository activation route.

README English/Chinese surfaces now make the same minimality rule explicit.

## Conformance intent

`conformance/test_skill_package.py` now requires the ChatGPT handoff block to equal the short locator form and rejects reintroduction of `AGNIR.yaml`, durable-truth, ChatGPT-memory, checkpoint, Current State, or Next Actions semantics into that block.

## Semantic boundary

This change is packaging/onboarding hardening only.

Unchanged:

- Agnir Core `1.0`;
- `repository-filesystem/1.0`;
- Project identity / Continuity Lineage semantics;
- checkpoint semantics;
- repository activation via `AGENTS.md -> AGNIR.md`;
- requirement to verify execution-surface activation separately when needed.

## Acceptance boundary

Candidate acceptance requires:

1. repository conformance success;
2. inspection that the persistent ChatGPT handoff remains locator-only;
3. a genuinely fresh ChatGPT Project initialization trial in which the installer offers the short locator without repeated Principal simplification.

Until those checks pass and target reconciliation occurs, this is candidate evidence rather than authoritative-main acceptance.
