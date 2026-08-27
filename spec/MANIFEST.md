# Configuration and Manifest

Version: 2.0.0

PPMP defines configuration semantics, not a mandatory file path or serialization format.

## Required semantic fields

A conforming project configuration MUST identify:

```yaml
ppmp:
  version: 2.0.0

project:
  primary_type: software
  profiles:
    - software

memory:
  state: <durable locator>
  next_steps: <durable locator>
  decisions: <durable locator>
  checkpoints: <durable locator or null>

policy:
  checkpoint: event-driven
  raw_transcripts: false
```

`ppmp.version` identifies the protocol version. `project.primary_type` and `project.profiles` follow `CLASSIFICATION.md`. Memory locators identify implementation-specific durable representations and MUST be resolvable by the implementation.

`policy.checkpoint` is `event-driven` in v2. `policy.raw_transcripts` MUST be `false` unless a separate explicit transcript/archive feature is being used outside PPMP Project Memory.

## Serialization

Implementations MAY add fields for implementation identity, backends, adapters, paths, namespaces, repositories, databases, or credentials references. Such fields MUST NOT be treated as protocol requirements.

The Persistent Project Memory (PPM) reference Skill uses a YAML file convention with its repository backend for interoperability; see `implementations/PERSISTENT_PROJECT_MEMORY.md`, `backends/REPOSITORY.md`, and `templates/project-memory.yaml`.

## Validation

Implementations SHOULD validate the protocol version, profiles, resolvable durable-memory locators, checkpoint policy, and implementation-specific requirements. Unknown extensions MAY be ignored only when doing so cannot change required behavior.
