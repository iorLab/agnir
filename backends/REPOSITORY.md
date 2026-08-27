# Repository Persistence Backend

Status: Reference backend used by Persistent Project Memory (PPM)
Protocol: PPMP v2.0.0

This backend serializes PPMP Project Memory into files within a repository and may use Git commits as durable checkpoint evidence.

## Reference layout

```text
.chatgpt/project-memory.yaml
docs/project-memory/
  PROJECT_STATE.md
  NEXT_STEPS.md
  DECISIONS.md
  sessions/
```

These paths are backend conventions, not PPMP protocol requirements.

The YAML manifest SHOULD identify `ppmp.version`, implementation, backend, adapter, project classification, file locators, and policy.

Repository content is the canonical durable representation for this backend. Chats and model memory are working context only.

Paths MUST be repository-relative, MUST NOT traverse outside the repository, and MUST NOT contain secrets. Writes SHOULD preserve useful existing content and SHOULD be committed coherently when Git is available and authorized.

Documentation-only checkpoints MUST NOT modify production code merely to manufacture a checkpoint. Git success MUST be verified before reporting a commit as durable.
