# Agnir Current State

Agnir `v0.1.1` is the immutable published stable baseline for this temporary migration validation. Its tag target is `e9712357ab590e5c1e5357b3cf3219d07d789aff`.

**Durable continuity belongs to the Project**, not to an Executor, conversation, execution environment, repository host, storage implementation, VCS selector, or Continuity Lineage.

## Published-v0.1.1 to Core 0.2 RC validation — 2026-09-03

This temporary real-repository validation lineage starts directly from immutable `v0.1.1` and applies verified RC operational package baseline `bee78b2c9bb8c5ce5916d08691019dcde939b813`.

Project identity remains `urn:agnir:project:agnir-core`. Core/profile are explicitly migrated from `0.1` / `repository-filesystem/0.1` to `0.2` / `repository-filesystem/0.2`.

Logical Continuity Lineage is `urn:agnir:lineage:validation:v0.2.0-rc.1-from-v0.1.1`, separately bound to selector `refs/heads/release/validation-v0.2.0-rc.1-from-v0.1.1`. Selector and revision receipt are not lineage identity.

The published `v0.1.1` Decisions blob and complete Evidence tree are preserved as the migration baseline. The source State/Next Actions blobs remain immutably recoverable from the source tag and are recorded by SHA in the new migration Evidence. Their obsolete publication-candidate actions are reconciled rather than misrepresented as current target-lineage work; the durable ownership, activation, checkpoint, upgrade, and release invariants that remain true are retained by the RC package and Decisions/Evidence.

This branch is validation-only. It is not authoritative, must not be merged into `main`, and must never become the RC tag target.
