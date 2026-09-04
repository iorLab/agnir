# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and authoritative self-host

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id `381710267`, `draft=false`, `prerelease=false`;
- publication run `33711982062` success;
- authoritative Agnir lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported migration/regression surfaces for published `v0.1.1` Projects.

## Real-Project v1 evidence

Three materially different external Projects carry direct published Agnir `v0.2.0` evidence.

### Svif — authoritative published upgrade

`iorLab/svif` completed an authoritative published `v0.1.1` / Core-profile `0.1` -> published `v0.2.0` / Core-profile `0.2` migration. Target-owned lineage `urn:svif:lineage:authoritative` is separately bound to `refs/heads/main`. Candidate, publication, and post-integration runs were green. This satisfies the real upgrade-boundary gate and the real parallel-lineage/reconciliation Project gate.

### FishUp — real migration-line validation

`iorLab/fishup` exercised the published `v0.2.0` reference migration against its real `v0.1.1` / Core-profile `0.1` Project. Unauthorized rejection, authorized migration, byte-exact continuity/instruction preservation, idempotent re-apply, fresh 0.2 discovery, typecheck, and build passed in runs `33737783270` and `33737919224`. FishUp authoritative `main` remains intentionally unchanged because every main push performs production Cloudflare/D1 deployment outside the migration-validation authorization.

### VocaPort — authoritative fresh install

`iorLab/VocaPort` had no pre-existing `AGNIR.yaml` at captured main `18a30d0dd745dadd128042d2439318b3f8c3e47c`. Published Agnir `v0.2.0` was installed non-destructively and accepted on authoritative main.

- Project identity: `urn:agnir:project:vocaport`;
- authoritative lineage: `urn:vocaport:lineage:authoritative`;
- selector binding: `refs/heads/main`;
- validated target candidate: `37bc529f8c17af8deb1b0867932e4fa65f01d7e3`, tree `282a2d38814929660367ce8d5e87d71b65fd038f`;
- exact candidate validation run `33786785234`: success;
- authoritative publication verifier `33787496205`: success;
- post-install checkpoint `eb9a3cca54d6e5daa80fbacc72624a735057328b`, tree `dde72dd4c907f2ba172a3f062385dfaa17b53611`;
- checkpoint fresh-resume verifier `33787760565`: success.

Paired untouched/install runs `33769075075` / `33769051389` produced the same VocaPort product verification shape, so the observed `pnpm test` and native-shell failures are baseline/environment limitations rather than Agnir regressions.

## Cross-Agent execution-surface evidence — DSH

VocaPort completed an isolated two-session DSH execution-surface validation on branch `validation/dsh-execution-surface-v0.2.0` without changing authoritative VocaPort `main` or publishing validation continuity as target truth.

Accepted receipts:

- protocol baseline `439866051d7b9863565540fb592f408de64c1081`;
- Session 1 initial checkpoint `b4f87d3ebd86d647adc2b7b101498ca4c80e6287`;
- Session 1 corrected final checkpoint `29549ebf45071003ae3e885664c7c9e960d838eb`;
- Session 2 fresh-resume checkpoint `af9b9c0b725ae40d11e462f11e3a9392afed6d8a`;
- validation lineage `urn:vocaport:lineage:dsh-execution-surface-validation`, separately bound to `refs/heads/validation/dsh-execution-surface-v0.2.0`;
- canonical VocaPort main remained `eb9a3cca54d6e5daa80fbacc72624a735057328b` throughout.

Fresh Session 1 discovered Agnir from repository-owned instructions, loaded State/Next/Decisions/Evidence, performed real Project work and checkpointed. External review found one incorrect observation; the same session corrected it through a reversible empirical test while preserving the superseded result as audit history. Fresh Session 2, without Session 1 private context, recovered the corrected checkpoint solely from Project-owned continuity and checkpointed again.

This is accepted as the materially distinct second Agent execution surface relative to the existing ChatGPT/GitHub-connected Agnir operating path. GitHub Actions and VocaPort Web/Desktop/Android runtimes are not counted as additional Agent surfaces.

## Genuine mount-boundary evidence — accepted

Agnir self-hosting has now exercised `repository-filesystem/0.2` across a real Linux Docker bind-mount boundary on temporary branch `validation/mount-boundary-v0.2.0`. The validation lineage `urn:agnir:lineage:mount-boundary-validation` remained isolated from authoritative main continuity.

Final accepted receipts:

- captured authoritative main: `4eb15a5c6df80983b1b799a9311ffc79a1d868d9`;
- final validation head: `ce30bed039e1cd2d1d8cf27b3cd2492c6dd279fa`;
- final validation tree: `962b9ceb16e8a0e15c92f940a34415915d08bb5f`;
- accepted workflow run: `33860631526`;
- job: `100984005488`;
- artifact id: `9931961351`;
- artifact digest: `sha256:2c7bb33c87e4de0e95542cfb12b3759ecdb005c6085962856bb4a2ad052b25ce`.

Container A mounted the Project at `/workspace/project-a`, fresh-resolved Project identity/Core/profile/lineage and durable continuity, wrote a State + Evidence checkpoint through the mount, and was destroyed. Container B then mounted the same host Project at `/mnt/agnir-project-b`, independently fresh-resolved the same Project identity and logical lineage, recovered A's checkpoint despite the changed absolute root path, wrote a resume receipt, and was destroyed. The host independently observed the persisted checkpoint and resume.

Negative paths also passed: a read-only Project mount remained discoverable but rejected checkpoint writes with `EROFS`; both a missing selected Project root and an actual wrong/empty mounted root failed explicitly with `AGNIR_DISCOVERY_NOT_FOUND` and no sibling guessing.

Runs `33860211185` and `33860517098` had already passed every substantive mount-semantic step; their only failures were validation-harness cleanup defects involving generated `conformance/__pycache__/` ownership. The third run fixed only cleanup and completed fully green. The final artifact was downloaded and externally inspected, including actual `/proc/self/mountinfo` receipts and empty final Git status.

This satisfies the current v1 **real mount-boundary evidence** gate for a genuine bind-mounted-volume boundary. It does not claim universal behavior across every network filesystem/FUSE/Kubernetes volume implementation, nor a new backend/profile or additional Agent surface.

## v1 readiness — current

- Core semantics: **provisionally satisfied**;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **satisfied at the current minimum threshold (3)** via Svif + FishUp + VocaPort;
- materially different execution surfaces/adapters: **satisfied at the current minimum threshold (2)** — existing ChatGPT/GitHub-connected Agent path plus accepted VocaPort DSH evidence;
- real mount-boundary evidence: **satisfied** via accepted Agnir Docker bind-mount checkpoint/fresh-resume validation;
- independent-implementation documentation quality: **open**;
- explicit `1.0.0-rc` cycle: **future gate after independent-implementation evidence closes**.

No Agnir Core/profile `0.2` semantic defect has been exposed by the accepted real-Project, execution-surface, or mount-boundary evidence. The remaining external v1 evidence work is now concentrated in independent-implementation documentation quality; after that, the next release gate is an explicit `1.0.0-rc` cycle from an exact fresh candidate.
