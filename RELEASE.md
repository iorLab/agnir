# Agnir 1.0.0 Stable Release Package

**Repository version:** `1.0.0`

**Core compatibility line:** `1.0`

**Repository/filesystem profile:** `repository-filesystem/1.0`

## Status

Agnir `v1.0.0` is **published stable**. The immutable tag points to exact authoritative revision `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`; GitHub Release id `383612171` is non-draft and non-prerelease; `releases/latest` resolves to `v1.0.0`.

This source line is the Agnir `1.0.0` stable release package. Core `1.0` and `repository-filesystem/1.0` are stable normative contracts; the explicit Core/profile `0.2` → `1.0` Project promotion contract is also stable normative material.

`latest stable` remains a publication property, not a moving-branch property. Stable-upgrade resolution now selects the published non-prerelease `v1.0.0` release. Later metadata/maintenance commits on `main` do not change the immutable source revision identified by the `v1.0.0` tag.

Stable publication was main-only and armed only by the exact commit message:

```text
release: publish v1.0.0 stable
```

Publication workflow `34039014354` passed both its initial cycle and a fresh immutable-source attempt. Attempt 1 repository/publication jobs were `101502237380` / `101502271312`; attempt 2 jobs were `101502430280` / `101502473422`.

## Accepted release candidate

Stable `v1.0.0` is based on the accepted immutable RC evidence cycle:

- RC tag: `v1.0.0-rc.1`;
- exact RC revision: `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC GitHub Release id: `383536840`;
- publication/conformance workflow: `34026167762`, attempt 1 success;
- fresh immutable-source verification: workflow `34026167762`, attempt 2 success;
- fresh repository job: `101467699247` success;
- idempotent publication-verification job: `101467723379` success;
- RC acceptance checkpoint: `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- RC tag remains immutable and must not be moved or rewritten after stable publication.

The stable release did not introduce a new continuity model after the RC. Stable preparation was limited to status/package/publication reconciliation and release-gate repairs that did not materially change the accepted Core/profile behavior.

## What v1.0.0 stabilizes

Agnir `v1.0.0` is the first long-term stable public compatibility commitment for the Project-owned durable continuity model proven under Core/profile `0.2` and promoted without behavioral redesign to Core/profile `1.0`.

Stable normative contracts:

- `spec/AGNIR_CORE_1_0.md`;
- `profiles/REPOSITORY_FILESYSTEM_1_0.md`;
- `schemas/agnir-manifest-1.0.schema.json`;
- `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

The stable 1.0 model preserves:

- Project-owned durable continuity;
- Project identity distinct from logical Continuity Lineage identity;
- selector/binding distinct from lineage identity and revision receipts;
- Current State / Next Actions / Decisions / Evidence semantics;
- exact compatibility-line dispatch;
- lineage-local checkpoints and stale-base rejection;
- source continuity as reconciliation input rather than automatic target truth;
- coherent target publication;
- VCS and non-VCS neutrality at Core level;
- machine-distinguishable discovery/checkpoint/lineage failures.

## Historical compatibility remains supported

Repository `1.0.0` is a multi-version distribution. Historical published compatibility surfaces remain present and are not rewritten as 1.0 history:

- Core/profile `0.1` + `repository-filesystem/0.1`;
- Core/profile `0.2` + `repository-filesystem/0.2`;
- explicit `0.1` → `0.2` migration under `spec/CORE_0_1_TO_0_2_MIGRATION.md`;
- explicit semantics-preserving `0.2` → `1.0` promotion under `spec/CORE_0_2_TO_1_0_PROMOTION.md`.

Installing or upgrading to the `1.0.x` distribution does not itself authorize rewriting an existing valid `0.2` Project to `1.0`. A Project may remain on its supported compatibility line until an explicit Project-owned promotion is authorized.

## Independent implementation and real-world evidence

The v1 readiness baseline was closed before the RC cycle. Accepted evidence includes:

- clean independent-implementation `PASS` from issue #26 against exact source `eabc599d589f2c3dfe6b3d9508a093d120f33c95`;
- accepted artifact SHA-256 `a466c98e6a1dcda5e0174c6769f0ecc4ee73e51932ed02ce67d59580622ed847`;
- direct boundary matrix `81/81` pass and required semantic receipts `19/19` pass;
- three materially different real Projects: Svif, FishUp, and VocaPort;
- two materially different execution surfaces/adapters;
- accepted VCS and non-VCS lineage evidence;
- accepted real upgrade and real parallel-lineage reconciliation evidence;
- genuine Linux Docker bind-mount fresh-remount/read-only/wrong-root evidence.

These receipts established that the 1.0 promotion is a stability commitment over already pressure-tested semantics rather than a feature-count milestone.

## Stable publication invariant

The stable tag points to the exact authoritative `main` publication-arm revision. A temporary release/staging lineage is reconciliation input only and cannot become authoritative merely because it passed CI.

The completed publication sequence required:

1. the `release/v1.0.0` staging lineage to pass the full conformance suite as repository `1.0.0` / Core `1.0` / `repository-filesystem/1.0`;
2. the accepted staging result to be reconciled into the authoritative lineage rather than copied wholesale;
3. authoritative `main` to pass exact-source conformance with its own lineage identity/binding;
4. the exact main commit message `release: publish v1.0.0 stable` to arm publication;
5. `refs/tags/v1.0.0` to point to that exact authoritative arm revision;
6. GitHub Release `v1.0.0` to be `draft=false` and `prerelease=false`;
7. `releases/latest` to resolve to `v1.0.0`;
8. `v1.0.0-rc.1` to remain at `092945289f1a0a9803e4fe0583104aa380ceaadc`.

All eight conditions were verified. Published tags are immutable by Project policy.

## Activation and Skill boundary

Root `SKILL.md` remains the canonical Agent-facing install / initialize / migrate / promote / upgrade / resume / checkpoint / commit / push / lineage-integration / repair procedure. User-facing requests remain short.

A repository/filesystem Project persists activation through `AGENTS.md` → README `Agnir Project Instructions` → `AGNIR.yaml` → selected durable continuity. Execution-surface bootstrap/configuration remains locator-only adapter behavior outside Agnir Core and outside Project-owned durable memory.

The `1.0.x` distribution may operate a supported `0.1`, `0.2`, or `1.0` Project by dispatching according to the compatibility declarations the Project actually owns.
