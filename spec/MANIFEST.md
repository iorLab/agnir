# Manifest Specification

Version: 1.0.0

Every RPM-enabled project MUST contain:

```text
.chatgpt/project-memory.yaml
```

The manifest identifies the RPM specification, project classification, Core memory paths, and active profiles.

## 1. Required structure

```yaml
rpm:
  version: 1.0.0
  spec_repository: mattamior/rpm

project:
  primary_type: software
  profiles:
    - software

memory:
  root: docs/project-memory
  state: PROJECT_STATE.md
  next_steps: NEXT_STEPS.md
  decisions: DECISIONS.md
  sessions: sessions

policy:
  checkpoint: event-driven
  session_logs: meaningful-only
  raw_transcripts: false
```

## 2. Field semantics

### `rpm.version`

Required. The specification version the project conforms to.

### `rpm.spec_repository`

Required. Repository containing the referenced RPM specification. RPM v1 reference source is `mattamior/rpm`.

### `project.primary_type`

Required. One of the supported primary types defined by `CLASSIFICATION.md`.

### `project.profiles`

Required. Non-empty list of active profiles. It SHOULD include `primary_type` unless the primary type is represented by `generic` for a special reason.

### `memory.root`

Required. Repository-relative directory containing RPM Core memory.

### Core path fields

`state`, `next_steps`, `decisions`, and `sessions` are paths relative to `memory.root` unless explicitly documented otherwise.

### `policy.checkpoint`

RPM v1 normative value is `event-driven`.

### `policy.session_logs`

RPM v1 recommended value is `meaningful-only`.

### `policy.raw_transcripts`

MUST be `false` for RPM v1. Raw chat transcripts are outside the RPM durable-memory model.

## 3. Optional fields

Projects MAY add:

```yaml
project:
  name: Example
  classification_note: "Software + product project"

extensions:
  software:
    architecture: docs/architecture
    adr: docs/decisions
  product:
    roadmap: docs/ROADMAP.md
```

Unknown optional fields MAY be ignored only when doing so cannot change the meaning of required RPM behavior.

## 4. Path rules

- Paths MUST be repository-relative.
- Paths MUST NOT traverse outside the repository.
- Secrets MUST NOT be stored in the manifest.
- A manifest SHOULD prefer stable canonical paths over generated or temporary locations.

## 5. Profile-specific configuration

Profiles MAY define extension paths under `extensions`.

An implementation SHOULD use declared paths when present and profile defaults otherwise.

Example:

```yaml
extensions:
  content:
    style_guide: docs/STYLE_GUIDE.md
    strategy: docs/CONTENT_STRATEGY.md
    backlog: docs/TOPIC_BACKLOG.md
```

## 6. Validation

On bootstrap, an implementation SHOULD validate:

- supported RPM version;
- known `primary_type`;
- non-empty profiles;
- existence or recoverability of required Core files;
- safe repository-relative paths;
- `raw_transcripts: false`.

Malformed manifests SHOULD be surfaced and repaired rather than silently guessed around.
