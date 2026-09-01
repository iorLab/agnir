# Existing Project upgrade implementation checkpoint — 2026-09-01

## Accepted direction

The Principal approved making upgrade of already Agnir-enabled Projects a first-class operation before upgrading older Projects.

## Problem

Before this change, the Agent Skill classified install/initialize, resume/use, checkpoint, commit/push, and repair, but did not define an upgrade operation. Existing initialized Projects could remain self-describing and resumable while their persisted activation/procedure lagged newer Agnir operational behavior.

## Implemented contract

- upgrade is distinct from re-initialization;
- compatible upgrade preserves Project identity, memory locators/content, unrelated Project instructions, and unrelated manifest extensions;
- target Core/profile compatibility must remain `0.1` / `repository-filesystem/0.1` for compatible operational upgrade;
- Core/profile changes are migration-required and surface `AGNIR_UPGRADE_MIGRATION_REQUIRED` semantics;
- a Project without operational provenance remains a valid compatible-upgrade input;
- optional `agnir/operations` provenance records distribution, release, source, and immutable applied revision;
- same-baseline upgrade is a no-op;
- `latest stable` resolves an actually published stable tag/release and must not silently fall back to moving `main` or an untagged revision;
- non-stable upgrade targets require explicit Principal authorization;
- compatible VCS upgrade should publish Agnir-owned procedure/provenance and continuity changes in one coherent revision and finish with fresh activation;
- normal resume does not automatically upgrade or require network access to the distribution source.

## Executable pressure

New conformance reference/tests cover:

- legacy compatible Project without operations provenance;
- preservation of Project identity, memory locators, and unrelated extensions;
- same operational baseline no-op;
- rejection of an unstable target without explicit opt-in;
- migration-required classification when Core or profile compatibility changes.

## Release consequence

The previously verified `0.1.0` candidate predates this accepted pre-publication operational contract. Release readiness is reopened until the implementation revision passes the full exact-revision conformance workflow. Its resulting Git revision will be the backend receipt; this evidence intentionally does not attempt to embed that future revision in itself.
