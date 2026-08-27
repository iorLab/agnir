# Agnir 0.1 Conformance — initial executable layer

This main-line conformance layer validates the repository/filesystem discovery contract without relabeling PPMP v2 evidence.

Current executable checks cover:

- top-level `AGNIR.yaml` exists;
- declared Core and discovery-profile versions are `0.1` and `repository-filesystem/0.1`;
- Project identity is present;
- state and next-actions locators resolve from the Project root;
- decisions/evidence locators resolve when non-null;
- authoritative memory contains a material Agnir fact recoverable without predecessor chat context;
- the reference JSON Schema is syntactically valid and declares the same required version/profile constants.

This is a structural cold-start fixture, not complete release conformance. Negative failure fixtures, non-repository persistence, external-memory authorization, nested-boundary cases, and multi-project isolation remain required before release-quality neutrality claims.
