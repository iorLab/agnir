# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and authoritative self-host

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id `381710267`, `draft=false`, `prerelease=false`;
- publication run `33711982062` success;
- authoritative Agnir lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported migration/regression surfaces for published `v0.1.1` Projects.

## Real-Project and execution-surface v1 evidence

The current minimum real-Project threshold is satisfied by materially different Projects:

- **Svif** — authoritative published `v0.1.1` / Core-profile `0.1` -> published `v0.2.0` / Core-profile `0.2` migration plus real parallel-lineage/reconciliation evidence;
- **FishUp** — real published-reference migration-line validation with unauthorized rejection, authorized migration, preservation, idempotence, fresh resume, typecheck, and build; production `main` intentionally unchanged because every main push has separate Cloudflare/D1 side effects;
- **VocaPort** — authoritative fresh `v0.2.0` install plus fresh-resume verification.

The materially distinct execution-surface threshold is satisfied by the existing ChatGPT/GitHub-connected Agent path plus the accepted VocaPort two-session DSH fresh activation/checkpoint/fresh-resume experiment. GitHub Actions and application runtimes are not counted as additional Agent surfaces.

## Genuine mount-boundary evidence — accepted

Agnir self-hosting exercised `repository-filesystem/0.2` across a real Linux Docker bind-mount boundary on isolated validation lineage `urn:agnir:lineage:mount-boundary-validation`.

Accepted receipts:

- captured authoritative main: `4eb15a5c6df80983b1b799a9311ffc79a1d868d9`;
- final validation head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`;
- final validation tree: `962b9ceb16e8a0e15c92f940a34415915d08bb5f`;
- workflow run/job: `33860631526` / `100984005488`;
- artifact id: `9931961351`;
- artifact digest: `sha256:2c7bb33c87e4de0e95542cfb12b3759ecdb005c6085962856bb4a2ad052b25ce`.

Container A checkpointed through `/workspace/project-a`, was destroyed, and a fresh Container B recovered the same Project identity/logical lineage and A's durable checkpoint from the same Project remounted at `/mnt/agnir-project-b`. Host persistence, read-only `EROFS` rejection, and explicit missing/wrong-root `AGNIR_DISCOVERY_NOT_FOUND` behavior were also verified. This closes the current v1 real mount-boundary gate without claiming universal behavior across every network filesystem/FUSE/Kubernetes volume substrate.

## Independent-implementation documentation gate — open

The gate now has three preserved clean external attempts plus one earlier lost-session attempt. None closes the gate yet, but the latest attempt materially strengthens the evidence that the public contract and reference are aligned.

### Challenge #15 — `FAIL-IMPLEMENTATION`

Issue `iorLab/agnir#15` ran against exact source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`.

- preserved archive SHA-256: `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`;
- Phase A reconstructed the published 0.2 manifest correctly;
- frozen Phase B later used incompatible shorthand serialization, so the direct verdict was `FAIL-IMPLEMENTATION`;
- the review also exposed public-contract drift, which was repaired before the next clean attempt.

### Challenge #17 — `FAIL-CONFORMANCE`

Issue `iorLab/agnir#17` ran against exact source `5b73acf914e323ce337a0af295d5a9e96eaafdc8`.

- preserved archive SHA-256: `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`;
- Phase B passed 21/21 recorded scenarios plus direct positive/negative schema fixtures;
- Phase C showed the reference resolver did not enforce the normative `additionalProperties: false` schema rule;
- final verdict: `FAIL-CONFORMANCE`.

PR `#18` repaired that reference/schema mismatch without redesigning Core/profile semantics. PR run `33907695244` and authoritative-main run `33907748617` succeeded. The repaired reference/schema state was checkpointed at `7e844fe8bde08be8288dbf05393e5e03601ea4f0` with main run `33907919438` success.

### Challenge #19 — `FAIL-IMPLEMENTATION`, documentation/reference dimensions pass

Issue `iorLab/agnir#19` ran from another fresh reviewer against exact source `7e844fe8bde08be8288dbf05393e5e03601ea4f0`.

Preserved archive receipt:

- archive SHA-256 independently recomputed: `7258e231a9acd22ed74b0dd42ff65ff54b32207f92ff55d08d26404e8dc85854`;
- 62 ZIP entries; archive integrity passed;
- bundled complete SHA-256 manifest verified every covered deliverable;
- Phase A and Phase B freeze receipts remained unchanged after Phase C reference inspection;
- Phase A found **no behavior-material documentation ambiguity/conflict/omission**;
- Phase B passed **12/12 unit tests and 30/30 machine-readable receipt cases**;
- direct schema/profile positive fixture passed and direct negative fixture was rejected correctly;
- checkpoint no-op/material/stale, fresh resume, preservation, lineage isolation, failure mapping, external authorization simulation, and optional VCS binding pressure passed.

Final verdict: **`FAIL-IMPLEMENTATION`** due one post-freeze edge-case defect in the independent resolver. Explicit YAML `agnir.version: null` was mapped to `AGNIR_DISCOVERY_UNSUPPORTED_VERSION`; the public schema/profile and pinned reference instead treat null as schema-invalid malformed serialization and therefore `AGNIR_DISCOVERY_INCONSISTENT`. The reviewer correctly did not modify frozen Phase B after reference inspection.

Crucially, challenge #19 reported the **documentation-sufficiency dimension as passing** and found **no reference/published-contract contradiction**. The remaining blocker is therefore not a newly identified Agnir product-contract defect; it is the frozen independent implementation's one machine-visible dispatch error.

Evidence detail: `.agnir/evidence/2026-09-05-independent-implementation-challenge-attempt-4.md`.

The independent-implementation gate remains **open** because acceptance requires the frozen independent implementation itself to conform. The next attempt must come from another genuinely fresh reviewer after Phase C exposure. To reduce repeated transcription edge failures without providing private answers, the challenge procedure should require a compact schema-derived negative mutation matrix before Phase B freeze, with expected results still derived solely from the public pinned contract.

## v1 readiness — current

- Core semantics: **provisionally satisfied**; reopen if fresh independent evidence exposes a semantic defect;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **satisfied at current minimum threshold (3)** via Svif + FishUp + VocaPort;
- materially different execution surfaces/adapters: **satisfied at current minimum threshold (2)**;
- real mount-boundary evidence: **satisfied**;
- independent-implementation documentation quality: **open — documentation/reference dimensions passed #19, but a fresh conforming implementation PASS is still required**;
- Core/profile `1.0` promotion: **future, only after independent-implementation acceptance**;
- explicit repository `1.0.0-rc` cycle: **future final release gate after independent-implementation acceptance and deliberate 1.0 contract promotion**.

No accepted real-Project, execution-surface, mount, or external review evidence has exposed a breaking Core/profile `0.2` semantic defect. The immediate external work is another clean independent implementation; if it passes, the next work is the deliberate Core/profile `0.2` -> `1.0` stability promotion and repository `1.0.0-rc` preparation.
