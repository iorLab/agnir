# ChatGPT Adapter

Status: Reference platform adapter for Persistent Project Memory
Protocol: iorMemory v2.0.0

The ChatGPT adapter maps ChatGPT Project behavior to the platform-neutral iorMemory lifecycle.

## Bootstrap trigger

At the first substantive turn of a new conversation, the adapter SHOULD discover the project's configured durable memory. With the reference repository backend, it checks `.chatgpt/project-memory.yaml`.

If configuration is missing, it SHOULD offer initialization. If present, it validates the declared iorMemory version, loads Current State and Next Steps, reads Decisions when relevant, and loads profile/history material only on demand.

This first-substantive-turn rule is a ChatGPT adapter convention, not an iorMemory protocol requirement. The adapter does not assume a reliable project-open event.

## Project isolation

ChatGPT Project-only memory MAY be used, but durable continuity MUST NOT depend on implicit cross-project or cross-conversation model memory. The configured durable backend remains the recovery mechanism.

## Explicit checkpoint phrases

When the user says “收尾”, “结束”, “先到这里”, “checkpoint”, “save progress”, or an equivalent explicit end/save instruction, the adapter SHOULD invoke a final PPM checkpoint before finishing substantive work.

## Minimal Project Instructions

The reference text lives in `templates/PROJECT_INSTRUCTIONS.md`. Project Instructions should remain a small bootstrap hook; full normative behavior belongs in the iorMemory specification and PPM implementation documentation.
