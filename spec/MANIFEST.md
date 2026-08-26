# Configuration and Manifest

Version: 2.0.0

iorMemory defines configuration semantics, not a mandatory file path or serialization format.

## Required semantic fields

A conforming project configuration MUST identify:

```yaml
iormemory:
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

`iormemory.version` identifies the protocol version. `project.primary_type` and `project.profiles` follow `CLASSIFICATION.md`. Memory locators identify implementation-specific durable representations and MUST be resolvable by the implementation.

`policy.checkpoint` is `event-driven` in v2. `policy.raw_transcripts` MUST be `false` unless a separate explicit transcript/archive feature is being used outside iorMemory Project Memory.

## Serialization

Implementations MAY add fields for backends, adapters, paths, namespaces, repositories, databases, or credentials references. Such fields MUST NOT be treated as protocol requirements.

The PPM repository backend uses a YAML file convention for interoperability; see `backends/REPOSITORY.md` and `templates/project-memory.yaml`.

## Validation

Implementations SHOULD validate the protocol version, profiles, resolvable durable-memory locators, checkpoint policy, and implementation-specific requirements. Unknown extensions MAY be ignored only when doing so cannot change required behavior.
