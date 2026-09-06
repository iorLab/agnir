# Agnir Current State

Agnir `v0.2.0` remains the published latest stable release. This selected continuity is the temporary `v1.0.0-rc.1` release lineage, intentionally promoted to Core `1.0` + `repository-filesystem/1.0` and now authorized to enter the exact immutable prerelease publication workflow.

Durable continuity belongs to the Project. Project identity remains `urn:agnir:project:agnir-core`; this lineage identity is `urn:agnir:lineage:v1.0.0-rc.1`, separately bound to `refs/heads/release/v1.0.0-rc.1`.

## Verified publication basis

- source authoritative checkpoint: `11148c3063e63dd1ea7450b9d538ac1eccec5639`, run `34025693977` success;
- first complete green RC-source candidate: `e4d5ad8f7e4013314401ecf3d987edb66f509ce5`, run `34026056687` success;
- candidate evidence checkpoint: `c05199291b8eda9ccceca8b918545773e330ad75`, run `34026116079` success;
- repository version: `1.0.0-rc.1`;
- Core/profile: `1.0` / `repository-filesystem/1.0`;
- logical lineage: `urn:agnir:lineage:v1.0.0-rc.1`;
- selector: `refs/heads/release/v1.0.0-rc.1`;
- latest stable remains `v0.2.0`.

The candidate and its receipt checkpoint both passed the complete release-branch conformance suite. Publication is therefore armed by the exact commit message required by the workflow. The armed revision itself is the workflow's `GITHUB_SHA`; it must independently pass the same repository conformance job before the publication job may create or validate tag/release `v1.0.0-rc.1`.

No immutable RC publication result is claimed yet by this state. After the workflow completes, verify exact tag target, Release flags, and latest-stable behavior before checkpointing publication success.
