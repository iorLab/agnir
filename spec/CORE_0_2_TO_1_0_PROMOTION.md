# Agnir Core/Profile 0.2 → 1.0 Stability Promotion

**Status:** Candidate normative promotion contract for the Agnir `1.0.0` release line.

## 1. Purpose

Core/profile `1.0` is the first long-term stable compatibility commitment for the semantics proven under Core `0.2` + `repository-filesystem/0.2`.

This promotion is intentionally **semantics-preserving**. It does not introduce a new continuity model, new lineage semantics, new checkpoint semantics, or a new repository/filesystem storage model. The purpose of the new compatibility identifiers is to mark the point at which those proven semantics become the stable 1.0 contract.

Historical Core/profile `0.1` and `0.2` contracts remain immutable. They are not renamed or rewritten in place.

## 2. Repository release vs compatibility promotion

Repository release `v1.0.0` and Core/profile compatibility versions remain distinct version axes.

A repository `1.0.x` distribution MAY support Projects that still declare Core/profile `0.1` or `0.2` by dispatching them to their published compatibility resolvers. Merely installing or running a `1.0.x` distribution MUST NOT silently rewrite a Project's Discovery Record from `0.2` to `1.0`.

A fresh Project that intentionally adopts the stable 1.0 line declares:

```yaml
agnir:
  version: "1.0"
  discovery_profile: "repository-filesystem/1.0"
```

A Project that already declares Core/profile `0.2` MAY remain on that supported compatibility line. Changing its serialized compatibility declaration to `1.0` is an explicit Project-owned promotion operation governed by this document.

## 3. Promotion authorization

Because `agnir.version` and `agnir.discovery_profile` are normative compatibility declarations, changing them is not an ordinary compatible operational upgrade.

A conforming operation that would rewrite an authoritative Core/profile `0.2` Project to Core/profile `1.0` MUST require explicit Principal/policy authorization for the compatibility-line promotion.

Until authorization is established, the operation MUST leave authoritative Project state unchanged and surface semantics equivalent to:

`AGNIR_UPGRADE_MIGRATION_REQUIRED`

This requirement applies to the compatibility-declaration rewrite. It does not mean a repository `1.0.x` distribution is forbidden from continuing to resolve an unchanged `0.2` Project through the published `0.2` resolver.

## 4. Required preservation

An authorized `0.2` → `1.0` promotion MUST preserve, unless a separately authorized Project change explicitly says otherwise:

- `project.identity` exactly;
- the selected durable `continuity.lineage` identity exactly;
- Current State semantics and content;
- Next Actions semantics and content;
- Decisions semantics/content and nullability;
- Evidence semantics/content and nullability;
- existing valid memory locators;
- Project policy fields;
- unrelated extensions;
- unrelated Project-owned files and instructions;
- valid selector/binding semantics such as `agnir/vcs` metadata that are independent of the Core/profile compatibility identifier.

The promotion MUST NOT trim, normalize, rename, regenerate, or reinterpret Project identity or logical lineage identity merely because the compatibility identifier changes.

The promotion MUST NOT relocate durable memory solely to perform the version promotion.

## 5. Required compatibility changes

For a repository/filesystem Project, the normative compatibility declaration changes from:

```yaml
agnir:
  version: "0.2"
  discovery_profile: "repository-filesystem/0.2"
```

to:

```yaml
agnir:
  version: "1.0"
  discovery_profile: "repository-filesystem/1.0"
```

The resulting Discovery Record MUST satisfy `schemas/agnir-manifest-1.0.schema.json` and the target-shape/failure rules in `profiles/REPOSITORY_FILESYSTEM_1_0.md`.

Operational distribution metadata MAY also be updated separately by the release/Skill adapter, but such metadata is not Core/profile identity and is not required to define the compatibility promotion itself.

## 6. Semantic equivalence rule

Core/profile `1.0` is a stability promotion of the accepted `0.2` semantics.

Unless an explicit 1.0 document states a deliberate difference, every normative behavior in the following accepted `0.2` contracts remains behaviorally equivalent in `1.0`:

- Project identity and Project ownership;
- Continuity Lineage identity/selection/isolation;
- Discovery Record semantics;
- cold-start/fresh-resume behavior;
- required durable memory semantics;
- repository/filesystem locator authority and target shape;
- flat baseline Evidence behavior;
- checkpoint no-op/material/stale-base behavior;
- failure classification semantics;
- VCS selector/binding/fork/rebind distinctions;
- lineage integration/reconciliation/coherent publication;
- backend neutrality.

A change that materially alters one of those semantics is not a promotion-only change and MUST be treated as a separate compatibility-design decision rather than smuggled into 1.0.

## 7. Staging and authoritative publication

A conforming promotion MUST NOT expose a mixed compatibility generation as completed authoritative truth.

The abstract sequence is:

1. resolve and validate the authoritative Core/profile `0.2` source;
2. verify explicit promotion authorization;
3. capture a source revision/generation/receipt sufficient to detect stale publication;
4. construct a complete Core/profile `1.0` candidate while authoritative `0.2` truth remains unchanged;
5. validate the candidate against the 1.0 schema/profile and verify required preservation;
6. immediately before publication, verify the authoritative source has not advanced materially since staging;
7. publish the new Discovery Record and any required compatibility metadata as one coherent authoritative transition;
8. fresh-resolve the Project through the Core/profile `1.0` resolver and verify the same Project identity, logical lineage identity, and durable continuity.

If the backend can use an atomic transaction or pointer/revision switch, implementations SHOULD use it. Otherwise they MUST provide equivalent generation/receipt semantics that prevent a compatible fresh resolver from accepting a partially promoted Project as completed truth.

## 8. Stale and conflicting promotion

If the authoritative source advances materially after the promotion candidate was staged, publication MUST fail rather than overwrite newer truth.

Recommended semantic class:

`AGNIR_MIGRATION_CONFLICT`

The implementation MUST re-resolve and reconstruct the promotion candidate before retrying.

A promotion request MUST also fail with migration-conflict semantics if it attempts to reinterpret an already-promoted Project as a materially different Project identity, lineage identity, locator set, or incompatible target contract without an explicit separately authorized migration.

## 9. Idempotence

Repeating an already completed `0.2` → `1.0` promotion against a Project that already declares the same valid Core/profile `1.0` target and preserves the same durable identity/continuity MUST be a no-op.

A no-op promotion MUST NOT rewrite durable continuity merely to create activity.

An already-1.0 Project that does not match the expected Project/lineage identity or valid target contract MUST fail explicitly rather than be silently rebound or repaired by the promotion path.

## 10. Relationship to Core/profile 0.1

Core/profile `0.1` does not have Continuity Lineage semantics and therefore MUST NOT be silently relabeled directly as Core/profile `1.0`.

A supported `0.1` Project reaches `1.0` by preserving the existing explicit migration semantics:

```text
Core/profile 0.1
  → explicit 0.1 → 0.2 migration
  → explicit semantics-preserving 0.2 → 1.0 promotion
```

An implementation MAY expose that sequence through one higher-level user operation, but the observable safety semantics of both boundaries MUST still hold. In particular, the 0.1→0.2 initial-lineage selection/normalization and preservation rules MUST NOT be bypassed.

## 11. Failure and dispatch semantics

A distribution that supports multiple compatibility lines SHOULD inspect the declared compatibility version/profile and dispatch to the matching resolver.

- a valid `0.2` manifest resolved as `0.2` remains supported and is not an error merely because `1.0` exists;
- a selected `repository-filesystem/1.0` manifest MUST satisfy the 1.0 schema/profile exactly;
- a 1.0 resolver MUST NOT silently accept a `0.2` declaration as if it were `1.0`;
- a 0.2 resolver MUST NOT silently accept a `1.0` declaration as if it were `0.2`;
- an attempt to rewrite 0.2 compatibility declarations to 1.0 without explicit authorization surfaces `AGNIR_UPGRADE_MIGRATION_REQUIRED`;
- stale/conflicting promotion publication surfaces `AGNIR_MIGRATION_CONFLICT` or a more specific backend conflict in addition to that semantic class.

## 12. Conformance requirements

Before Core/profile `1.0` may be used by an Agnir `1.0.0-rc` candidate, conformance MUST demonstrate at least:

1. fresh Core/profile 1.0 install and cold-start discovery;
2. fresh resume of an already-published 1.0 Project;
3. 1.0 schema/profile failure mapping equivalent to the accepted 0.2 semantics;
4. 1.0 checkpoint no-op, material publication, stale-base rejection, preservation, and fresh resume;
5. 1.0 lineage isolation and integration/reconciliation semantics;
6. unchanged 0.1 and 0.2 compatibility regression coverage;
7. unauthorized 0.2→1.0 rewrite rejection with `AGNIR_UPGRADE_MIGRATION_REQUIRED` semantics;
8. authorized 0.2→1.0 promotion preserving Project identity, lineage identity, durable memory, locators, policy/extensions, and unrelated Project content;
9. repeated same promotion is a no-op;
10. stale-source promotion is rejected without overwriting newer truth;
11. fresh 1.0 discovery after promotion;
12. supported 0.1→0.2→1.0 composed path preserves the established 0.1→0.2 migration semantics.

The explicit repository `1.0.0-rc` cycle remains a separate release gate after this promotion contract and its conformance are complete.