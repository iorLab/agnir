# Software Profile

Version: 1.0.0

Use this profile for projects whose durable work centers on source code, systems, infrastructure, testing, deployment, schemas, or implementation.

## Core extensions

Create these lazily when durable information justifies them:

### Architecture

Default location:

```text
docs/architecture/
```

Create architecture documentation when system boundaries, components, data flow, runtime topology, or integration contracts are important enough that `PROJECT_STATE.md` would become overloaded.

### ADRs

Default location:

```text
docs/decisions/
```

Create an ADR when a decision is:

- high impact;
- expected to remain relevant for a long time;
- based on meaningful alternatives or trade-offs;
- costly to rediscover later.

Do not create ADRs for trivial implementation details.

`DECISIONS.md` SHOULD remain the lightweight index and MAY link to ADRs.

### Testing

Default location:

```text
docs/testing/
```

Create when test strategy, fixtures, CI validation, integration environments, or verification procedures have durable complexity.

### Deployment

Default location:

```text
docs/deployment/
```

Create when environments, infrastructure bindings, release procedures, migrations, rollback steps, or deployment constraints need durable operational documentation.

### CHANGELOG

Maintain `CHANGELOG.md` only when shipped changes or releases have user-visible or operational significance. Do not use it as a duplicate session log.

## Persistence triggers specific to software

Persist when:

- architecture changes;
- a root cause is established for a significant bug;
- a migration or schema strategy is confirmed;
- CI behavior or validation requirements materially change;
- deployment topology or environment configuration changes;
- a feature reaches Completed or Verified state;
- test evidence changes confidence in project status;
- an important dependency or compatibility constraint is established.

## Verification

Software claims SHOULD identify verification evidence when relevant, such as:

- test suite results;
- workflow run status;
- build output;
- deployment confirmation;
- runtime inspection;
- commit, PR, or release references.

"Implemented" is not equivalent to "Verified".

## Recommended manifest extension

```yaml
extensions:
  software:
    architecture: docs/architecture
    adr: docs/decisions
    testing: docs/testing
    deployment: docs/deployment
    changelog: CHANGELOG.md
```

All extension paths are optional and SHOULD be materialized lazily.
