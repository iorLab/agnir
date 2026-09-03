# v1 evidence gap map established — 2026-09-03

Status: **current readiness map recorded; no v1 release claim.**

`V1_RELEASE_CRITERIA.md` now carries a non-normative evidence snapshot that maps each existing v1 gate to current evidence without weakening the normative requirements.

## Newly closed / clarified sub-gates

- real upgrade boundary: satisfied by Svif published `v0.1.1` -> published `v0.2.0` migration;
- real parallel continuity/reconciliation Project: satisfied via Svif;
- VCS + non-VCS lineage conformance: green;
- repeatable 0.2 RC/stable release operations: demonstrated;
- current published compatibility/migration contract: explicit and conformance-backed.

## Still open before v1

- at least two additional materially different real Projects, bringing the qualifying external set to at least three;
- a clearly distinct second execution surface/adapter with fresh activation/resume evidence;
- genuine mount-boundary pressure in a mount-capable environment;
- independent-implementation quality proof/review;
- an explicit `1.0.0-rc` cycle with every normative suite green from the exact candidate.

Other gates are marked provisionally satisfied where current evidence is strong but future real evidence can reopen them, especially Core semantic completeness, failure behavior, and publication/checkpoint integrity.

## Receipts used

- Agnir stable release `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- Agnir stable-main verification run `33712492531`;
- Svif downstream migration source `267f3d706e4fba67f2fb4a3a7ea33e80b9fb48ef`, run `33724859300`;
- Svif target-reconciled publication `2b5b92ab234d4c1b0d6596bbb0b8439eb6e05cfa`, candidate run `33725164044`, main run `33725240001`;
- Svif post-integration checkpoint `eba1b8538c4692a08bf69452525b735d23564599`, run `33727957648`;
- Agnir evidence ingestion `b1d1a8c784839aaf0822d542fdf820341d4699b2`, run `33728196706`;
- Agnir post-evidence checkpoint `8ca37712b9ddfa0207893ceb82c850e36f4b2fcd`, run `33728480626` success.

This map is intended to drive evidence acquisition rather than trigger a version bump. `v1.0.0` remains blocked until every normative gate is actually satisfied.
