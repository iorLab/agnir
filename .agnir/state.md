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

A clean independent challenge was run from public issue `iorLab/agnir#15` against exact source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`.

The preserved complete challenge archive was supplied by the Principal and independently rechecked:

- archive SHA-256: `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`;
- ZIP integrity passed;
- 19 files cover source classification, frozen Phase A reconstruction, ambiguity log, independent Phase B implementation/tests/receipts, Phase C comparison/probe, and final verdict.

The reviewer verdict was **`FAIL-IMPLEMENTATION`**: Phase A correctly reconstructed the published `0.2` manifest fields, but the frozen Phase B code later used incompatible shorthand fields and the wrong `policy.checkpoint` enum, so it rejected a valid published manifest. That session has now inspected reference code in Phase C and cannot be reused as the next fresh independent implementer.

The same challenge nevertheless recorded real public-contract drift, and a separate repository review confirmed additional ambiguity risk. This checkpoint repairs the public `0.2` material without changing Core/profile semantics:

- `spec/CORE_0_1_TO_0_2_MIGRATION.md` is brought into the stable normative status already asserted by `v0.2.0` release material;
- `SKILL.md` now distinguishes the experimental Core/profile `0.1` VCS extension from the normative Core/profile `0.2` VCS selector/binding/integration sources;
- `repository-filesystem/0.2` now explicitly maps Core-version mismatch, profile mismatch, Project/lineage mismatch, local locator escape, and real external authorization failure to machine-distinguishable semantics;
- conformance pressure now covers profile mismatch and local-locator escape and removes stale `experimental` naming;
- stale post-release/mount wording is refreshed.

Evidence detail: `.agnir/evidence/2026-09-05-independent-implementation-challenge-attempt-2.md`.

The independent-implementation gate remains **open**. Acceptance requires a new exact authoritative source revision and another genuinely fresh reviewer/session that has not seen prior challenge reports or reference implementation code.

## v1 readiness — current

- Core semantics: **provisionally satisfied**; reopen if fresh independent evidence exposes a semantic defect;
- compatibility/migration contract: **satisfied for current published lines after public-status consistency repair**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **satisfied at current minimum threshold (3)** via Svif + FishUp + VocaPort;
- materially different execution surfaces/adapters: **satisfied at current minimum threshold (2)**;
- real mount-boundary evidence: **satisfied**;
- independent-implementation documentation quality: **open — fresh rerun required**;
- Core/profile `1.0` promotion: **future, only after independent-implementation acceptance**;
- explicit repository `1.0.0-rc` cycle: **future final release gate after independent-implementation acceptance and any deliberate 1.0 contract promotion**.

No accepted real-Project, execution-surface, or mount evidence has exposed a breaking Core/profile `0.2` semantic defect. The immediate external work is now a fresh independent implementation against the repaired exact public source.
