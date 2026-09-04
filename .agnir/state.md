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

The gate has now produced two preserved clean external attempts plus one earlier lost-session attempt. None closes the gate, but each materially improved the public contract and conformance pressure.

### Preserved challenge #15 — `FAIL-IMPLEMENTATION`

Issue `iorLab/agnir#15` ran against exact source `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`.

- preserved archive SHA-256: `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`;
- reviewer Phase A reconstructed the published 0.2 manifest correctly;
- frozen Phase B later used incompatible shorthand serialization, so the direct verdict was `FAIL-IMPLEMENTATION`;
- the same review exposed public-contract drift, which was repaired before the next clean attempt.

That repair landed on authoritative main as `5b73acf914e323ce337a0af295d5a9e96eaafdc8`, with main conformance run `33896653132` success.

### Independent challenge #17 — `FAIL-CONFORMANCE`

Issue `iorLab/agnir#17` then ran from a genuinely fresh reviewer against exact source `5b73acf914e323ce337a0af295d5a9e96eaafdc8`.

Preserved archive receipt:

- archive SHA-256: `a2408dec4c0e3badebaa9cb67043219e67f36b7c85fa5f7c160435afabe7d523`;
- archive contains 80 entries and passed local ZIP integrity inspection;
- Phase A and Phase B freeze verification passed before reference inspection;
- independent Phase B resolver/checkpoint implementation passed **21/21** recorded scenarios;
- the direct schema-conforming positive fixture was accepted and the direct schema-derived forbidden-extra-field fixture was rejected.

Final verdict: **`FAIL-CONFORMANCE`**. Phase C demonstrated that the pinned `conformance/repository_filesystem_0_2_reference.py` did not enforce the normative `schemas/agnir-manifest-0.2.schema.json`: its scalar parser ignored forbidden additional/shorthand fields even though the schema has `additionalProperties: false`. The review also exposed a narrower machine-visible omission around absent `agnir.version` versus a present incompatible version.

### Reference/schema repair — accepted into main

PR `#18` repaired executable reference pressure without redesigning Core/profile semantics:

- repository-filesystem/0.2 reference now parses YAML and validates the exact published JSON Schema;
- forbidden additional/shorthand fields are rejected as `AGNIR_DISCOVERY_INCONSISTENT` rather than silently ignored;
- the profile now explicitly distinguishes missing required `agnir.version` (`AGNIR_DISCOVERY_INCONSISTENT`) from a present incompatible Core version (`AGNIR_DISCOVERY_UNSUPPORTED_VERSION`);
- positive schema-valid optional-field and negative forbidden-extra-field conformance cases are locked in;
- conformance dependencies are pinned in `conformance/requirements.txt` and installed by CI.

Accepted receipts:

- repair PR head: `b753ad65548e81b30a7f0d189034284fde0f2002`;
- PR conformance run `33907695244`: success;
- merged authoritative main repair: `a0b322d4e7f4e62e2ed77121b0a1b4e3b2328d1a`;
- authoritative main conformance run `33907748617`: success.

Evidence detail: `.agnir/evidence/2026-09-05-independent-implementation-challenge-attempt-3.md`.

The independent-implementation gate remains **open**. The next evidence must come from another genuinely fresh reviewer against the exact post-checkpoint public source, with no access to prior challenge reports/issues or reference code before its allowed Phase C boundary.

## v1 readiness — current

- Core semantics: **provisionally satisfied**; reopen if fresh independent evidence exposes a semantic defect;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **satisfied at current minimum threshold (3)** via Svif + FishUp + VocaPort;
- materially different execution surfaces/adapters: **satisfied at current minimum threshold (2)**;
- real mount-boundary evidence: **satisfied**;
- independent-implementation documentation quality: **open — another fresh rerun required after reference/schema repair**;
- Core/profile `1.0` promotion: **future, only after independent-implementation acceptance**;
- explicit repository `1.0.0-rc` cycle: **future final release gate after independent-implementation acceptance and deliberate 1.0 contract promotion**.

No accepted real-Project, execution-surface, mount, or independent Phase B evidence has exposed a breaking Core/profile `0.2` semantic defect. The immediate external work is one more clean independent implementation against the repaired exact authoritative source.
