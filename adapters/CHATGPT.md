# ChatGPT Adapter

Status: Reference platform adapter used by Persistent Project Memory (PPM)
Protocol: PPMP v2.0.0

The ChatGPT adapter maps ChatGPT Project behavior to the platform-neutral PPMP lifecycle as implemented by PPM.

## Bootstrap trigger

At the first substantive turn of a new conversation, the adapter SHOULD discover the project's configured durable memory. With the reference repository backend, it checks `.chatgpt/project-memory.yaml`.

If configuration is missing, it SHOULD offer PPM initialization. If present, it validates the declared PPMP version, loads Current State and Next Steps, reads Decisions when relevant, and loads profile/history material only on demand.

This first-substantive-turn rule is a ChatGPT adapter convention, not a PPMP protocol requirement. The adapter does not assume a reliable project-open event.

## Project isolation

ChatGPT Project-only memory MAY be used, but durable continuity MUST NOT depend on implicit cross-project or cross-conversation model memory. The configured durable backend remains the recovery mechanism.

## Explicit checkpoint phrases

When the user says “收尾”, “结束”, “先到这里”, “checkpoint”, “save progress”, or an equivalent explicit end/save instruction, the adapter SHOULD invoke a final PPM checkpoint before finishing substantive work.

## Project Instructions configuration

The reference bootstrap text lives in `templates/PROJECT_INSTRUCTIONS.md`. Project Instructions should remain a small bootstrap hook; full normative behavior belongs in the PPMP specification and PPM implementation documentation.

ChatGPT Project Instructions are external platform configuration. Updating a repository manifest, template, PPM implementation, or PPMP documentation does **not** update the actual Project Instructions configured in ChatGPT.

After a migration or implementation/adapter change that affects bootstrap wording, naming, discovery, or checkpoint behavior, acceptance SHOULD verify the actual ChatGPT Project Instructions against the intended current configuration and SHOULD exercise a fresh conversation to confirm first-substantive-turn discovery and restore behavior.

A repository-backed project MAY keep a project-specific snapshot of its intended ChatGPT Project Instructions so configuration drift is reviewable and recoverable. Such a snapshot is adapter/project configuration, not PPMP protocol semantics, and it does not replace the actual Project Instructions configured on the platform.
