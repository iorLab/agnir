# PPMP v2 -> Agnir Core 0.1 Migration Draft

**Status:** Transition mapping; not a released migration specification  
**Source lineage:** PPMP v2.0.0 / Persistent Project Memory / Sandminni  
**Target lineage:** Agnir Core 0.1

## 1. Migration rule

The transition from PPMP v2 to Agnir is explicit and non-cosmetic.

PPMP v2.0.0 remains a released predecessor protocol. A Project conforming to PPMP v2 MUST NOT be described as Agnir-conforming until an explicit migration or compatibility layer establishes the Agnir Core 0.1 semantics, including the cold-start discovery invariant.

Agnir uses a new version namespace. The numeric version `2.0.0` is not carried forward as an Agnir version merely to preserve chronology.

## 2. Semantic mapping

| PPMP v2 | Agnir Core 0.1 target | Migration treatment |
|---|---|---|
| Project | Project | Preserve; strengthen ownership independence from Executor/environment |
| Current State | Current State | Preserve |
| Next Steps | Next Actions | Rename/generalize; preserve content |
| Decisions | Decisions | Preserve |
| Checkpoint History | Evidence / Checkpoints | Generalize; preserve relevant historical evidence |
| protocol Core | Agnir Core | Re-evaluate normatively; do not copy implementation leakage |
| profiles | Agnir Profiles | Preserve only when semantics remain domain-level durable-memory concerns |
| implementation | Implementation | Preserve layer boundary; predecessor IDs do not become Core |
| persistence backend | Backend | Preserve layer boundary |
| platform adapter | Adapter | Preserve layer boundary |
| bootstrap | Cold-start discovery | Strengthen from implementation-convention discovery to explicit Project Entry Point / Discovery Record / Locator Chain semantics |
| user instruction in authority hierarchy | Principal instruction/policy | Neutral terminology |
| model/session context | Executor-private context | Generalize beyond AI/chat |

## 3. Semantics preserved from PPMP v2

The following predecessor semantics remain strong Agnir candidates and SHOULD be preserved unless a later Agnir Core decision explicitly changes them:

- current truth is distinct from chronology;
- Current State prefers present truth over accumulated history;
- required current facts must not exist only in checkpoint history;
- durable continuity must not require raw conversation transcripts;
- a verified claim requires evidence rather than assertion;
- durable state must not be invented when evidence is missing;
- material uncertainty is surfaced rather than guessed;
- project-specific durable state remains within the Project's memory boundary;
- checkpoints are intentional material persistence boundaries;
- persistence technology is not a Core identity;
- profiles are composable and should be activated conservatively.

## 4. Semantics strengthened or changed

### 4.1 Project ownership becomes explicit

PPMP v2 already removed Git/repository and ChatGPT from protocol requirements. Agnir strengthens this into a direct ownership invariant:

> Durable memory belongs to the Project, not to an Executor, execution environment, platform, backend, or adapter.

Migration documentation and implementations SHOULD remove wording that implies Project Memory is primarily "AI memory" or belongs to a specific agent/session.

### 4.2 Discovery becomes normative

PPMP v2 bootstrap currently relies on implementation/platform conventions to discover configuration. Agnir 0.1 makes the **ability to resolve durable memory from an authorized Project Entry Point without predecessor-private context** part of Core continuity.

A migrated Project therefore needs:

1. a Project Entry Point;
2. a Discovery Record or semantically equivalent durable discovery representation;
3. a resolvable Locator Chain to Current State and Next Actions;
4. an Agnir version/compatibility declaration;
5. explicit discovery failure when locators are stale, missing, ambiguous, cyclic, or unauthorized.

A repository path such as `.chatgpt/project-memory.yaml` MAY satisfy this through a repository/filesystem profile, but the path itself is not Agnir Core.

### 4.3 Neutral roles

References to `user`, `agent`, `AI`, `conversation`, or `model memory` in normative role semantics SHOULD migrate to:

- **Principal** — authority/intent/policy;
- **Executor** — entity performing operations;
- **Executor-private context** — non-durable context that MUST NOT be required for continuity.

ChatGPT-specific behavior remains valid only inside a ChatGPT adapter.

### 4.4 New version namespace

Agnir begins at the `0.1` line. PPMP v2.0.0 is not "Agnir v2".

Migration tools MUST record both the source lineage and target Agnir version so that historical claims remain interpretable.

## 5. Configuration mapping

A predecessor semantic configuration such as:

```yaml
ppmp:
  version: 2.0.0
project:
  primary_type: software
  profiles:
    - software
memory:
  state: docs/project-memory/PROJECT_STATE.md
  next_steps: docs/project-memory/NEXT_STEPS.md
  decisions: docs/project-memory/DECISIONS.md
  checkpoints: docs/project-memory/sessions
```

may migrate semantically to an Agnir Discovery Record equivalent to:

```yaml
agnir:
  version: 0.1
project:
  identity: <durable-project-identity>
  profiles:
    - software
memory:
  state: <durable-locator>
  next_actions: <durable-locator>
  decisions: <durable-locator-or-null>
  evidence: <durable-locator-or-null>
```

This example is a semantic mapping, not a mandatory filename or YAML serialization.

Implementation/backend/adapter fields from predecessor manifests MAY be retained as extensions when they remain accurate. They MUST NOT be reclassified as Agnir Core requirements.

## 6. Repository-backed PPMP/PPM migration profile

A common predecessor project uses:

- `.chatgpt/project-memory.yaml`;
- repository-backed durable files;
- PPM as implementation;
- ChatGPT as adapter.

A migration MAY preserve those physical files initially if it:

1. preserves all durable Project knowledge;
2. changes the declared target semantics to Agnir only after an Agnir-compatible Discovery Record can be resolved;
3. maps `next_steps` to `next_actions` semantically even if the physical filename remains unchanged during transition;
4. ensures the Project Entry Point has a durable route to the Discovery Record;
5. verifies cold-start discovery from a fresh Executor without relying on prior chat/model context;
6. records that repository and ChatGPT behavior are profile/backend/adapter choices, not Core;
7. records the migration as a durable Project decision/evidence event.

Physical rename of `.chatgpt/`, files, repository, or product branding MAY occur later and MUST NOT be confused with semantic migration completion.

## 7. External-memory migration

If predecessor memory is moved outside the immediate Project substrate, migration is incomplete until:

- the Project Entry Point durably resolves the external Discovery Record or memory root;
- authorization required to follow the Locator Chain is defined;
- failure to access the external state is surfaced explicitly;
- no predecessor Executor-private secret locator is required;
- a fresh Executor can recover the same authoritative current state.

Moving data to a database or API without a Project-discoverable locator does not satisfy Agnir cold-start continuity.

## 8. Profile migration

PPMP profiles SHOULD be reviewed individually.

A profile carries forward when its concepts describe recurring durable Project memory rather than implementation mechanics. Fields that describe a Git repository, ChatGPT behavior, CI side effects, or backend-specific paths SHOULD move to a backend/adapter/profile implementation layer as appropriate.

Profile migration MUST preserve project-specific durable knowledge even when the target schema changes.

## 9. Compatibility modes

During transition, implementations MAY support three explicit modes:

1. **PPMP v2 mode** — Project remains predecessor-conforming only.
2. **Migration mode** — predecessor state is read and transformed, but Agnir conformance is not yet claimed.
3. **Agnir 0.1 mode** — target semantics and cold-start discovery have been validated.

An implementation MUST NOT silently treat mode 1 as mode 3.

## 10. Migration acceptance

A PPMP v2 Project is migrated to Agnir 0.1 only when all of the following hold:

- required durable knowledge is preserved;
- target Agnir version/compatibility is explicitly declared;
- Current State, Next Actions, Decisions, and Evidence/Checkpoints are resolvable as required;
- a Project Entry Point can resolve the Discovery Record and Locator Chain;
- a fresh Executor can complete cold-start discovery without predecessor-private context;
- backend/adapter-specific assumptions are not represented as Agnir Core requirements;
- material migration decisions and unresolved incompatibilities are durably recorded;
- predecessor conformance/history remains distinguishable from target Agnir conformance.

## 11. Self-hosting this repository

`mattamior/rpm` currently identifies the Project as Agnir while maintaining its own durable state through PPMP v2 / PPM, the repository backend, and the ChatGPT adapter.

That is an intentional **migration-mode** configuration. It demonstrates continuity across the architecture transition without pretending the Agnir 0.1 conformance contract is already released or satisfied.

The repository should switch its self-hosted maintenance memory to Agnir mode only after the target Discovery Record/profile and cold-start acceptance procedure are concrete enough to validate.
