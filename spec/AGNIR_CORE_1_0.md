# Agnir Core 1.0 — Normative Specification

**Status:** Candidate stable compatibility contract for the Agnir `1.0.0` release line.

## 1. Purpose

Agnir Core `1.0` is the first long-term stable compatibility commitment for the project-owned durable continuity semantics proven under Core `0.2`.

The ownership rule remains:

> The Project persists; Executors and execution environments may change.

Core `1.0` MUST NOT require Git, GitHub, VCS branches, repositories, filesystems, ChatGPT, an AI agent, a conversational interface, or any single storage layout.

## 2. Stability-promotion rule

Core `1.0` is a **semantics-preserving stability promotion** of Core `0.2`, not a redesigned continuity model.

Except for the compatibility identifier changing from `0.2` to `1.0`, the status changing from pre-1.0 to stable 1.0 commitment, and the explicit promotion/compatibility rules in this document, the normative semantics of `spec/AGNIR_CORE_0_2.md` §§1 and 3–14 are incorporated into Core `1.0` **without behavioral change**.

Therefore the following Core `0.2` semantics are normative Core `1.0` semantics:

- Project ownership and Project identity;
- Continuity Lineage identity, selection, isolation, and integration;
- durable Current State / Next Actions / Decisions / Evidence semantics;
- Discovery Record semantics and cold-start/fresh-resume invariants;
- lineage-local checkpoint coherence and stale-base rejection;
- target reconciliation and coherent integration publication;
- truth-reconciliation order;
- machine-distinguishable discovery/checkpoint/lineage failure classes;
- backend neutrality;
- VCS selector/binding/revision separation from logical lineage identity.

A Core `1.0` implementation MUST NOT introduce a behavioral difference from the incorporated `0.2` rules unless a later published `1.x` contract explicitly defines that compatible extension.

## 3. Compatibility identifier

A Core `1.0` Discovery Record provides semantics equivalent to:

```yaml
agnir:
  version: "1.0"
project:
  identity: <durable-project-identity>
continuity:
  lineage: <selected-durable-logical-lineage-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

The representation remains semantic, not serialization-specific. Profiles define the concrete discovery-profile identifier and serialized constraints.

A conforming Core `1.0` resolver MUST NOT silently interpret a Discovery Record declaring another Core compatibility version as if it declared `1.0`.

## 4. Relationship to Core 0.2

Core `0.2` remains a published supported compatibility line. A repository/distribution that contains Core `1.0` MAY continue to resolve an unchanged Core `0.2` Project through the published `0.2` resolver.

The existence of Core `1.0` MUST NOT by itself force every Core `0.2` Project to rewrite its Discovery Record.

If a Project chooses to change its authoritative compatibility declaration from Core `0.2` to Core `1.0`, that explicit Project-owned transition is governed by `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

A Core `1.0` implementation MUST NOT silently treat the compatibility-identifier change as an ordinary packaging upgrade.

## 5. Relationship to Core 0.1

Core `0.1` remains a historical supported compatibility/migration surface. It lacks explicit Continuity Lineage semantics and MUST NOT be silently relabeled as Core `1.0`.

A Project moving from Core `0.1` to `1.0` preserves both published boundaries:

1. explicit `0.1` → `0.2` migration under `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
2. explicit semantics-preserving `0.2` → `1.0` promotion under `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

A higher-level tool MAY compose those steps, but MUST preserve the observable safety, authorization, identity, lineage-selection, stale-source, idempotence, and fresh-resume semantics of each boundary.

## 6. Stable compatibility commitment

For the `1.x` line, downstream Projects may rely on the Core `1.0` semantics above remaining compatible across repository releases that continue to declare Core `1.0`.

Backward-compatible clarifications, additional optional profiles/extensions, stronger conformance, packaging changes, and implementation repairs MAY occur without changing the Core compatibility identifier when they do not materially alter required Core behavior.

A future change that requires existing conforming Core `1.0` Projects or implementations to reinterpret required behavior incompatibly MUST use a new Core compatibility line and explicit migration/rejection semantics rather than silently redefining Core `1.0`.

## 7. Failure classes

Core `1.0` retains the accepted Core `0.2` machine-visible failure semantics, including:

- `AGNIR_DISCOVERY_PROJECT_MISMATCH`
- `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`
- `AGNIR_DISCOVERY_UNRESOLVABLE`
- `AGNIR_CHECKPOINT_CONFLICT`
- `AGNIR_LINEAGE_REQUIRED`
- `AGNIR_LINEAGE_NOT_FOUND`
- `AGNIR_LINEAGE_RECONCILIATION_REQUIRED`
- `AGNIR_LINEAGE_INTEGRATION_CONFLICT`

Profiles/adapters MAY expose more specific compatible backend failures in addition to these semantic classes.

## 8. Conformance

Core `1.0` conformance MUST exercise the incorporated Core `0.2` semantics under the `1.0` compatibility identifier rather than merely assuming equivalence from documentation.

Before stable publication, the repository `1.0.0-rc` cycle MUST include at least:

- fresh Core `1.0` discovery/resume;
- checkpoint no-op/material/stale behavior;
- lineage selection/isolation/integration;
- VCS and non-VCS lineage evidence where required by the release criteria;
- failure-path coverage;
- Core `0.2` compatibility regression;
- explicit `0.2` → `1.0` promotion conformance;
- composed `0.1` → `0.2` → `1.0` migration/promotion coverage;
- Agnir self-hosting and exact-source release verification.

The normative promotion boundary is `spec/CORE_0_2_TO_1_0_PROMOTION.md`.