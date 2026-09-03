# Agnir Current State

Agnir `v0.2.0` is the published latest stable release and is safely reconciled into authoritative `main`. Durable continuity belongs to the Project; Project identity, logical Continuity Lineage, backend selector/binding, and revision receipts remain distinct concepts.

## Stable release and authoritative self-host

- stable tag `v0.2.0` -> `fc84095ed5d500be9e1b43a4af0e93356571bbd4`;
- GitHub Release id `381710267`, `draft=false`, `prerelease=false`;
- publication run `33711982062` success;
- authoritative Agnir lineage `urn:agnir:lineage:authoritative`, separately bound to `refs/heads/main`;
- Core/profile `0.2` / `repository-filesystem/0.2` are stable; Core/profile `0.1` remain supported migration/regression surfaces for published `v0.1.1` Projects.

## Real-Project v1 evidence

Three materially different external Projects now carry direct published Agnir `v0.2.0` evidence:

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

The install preserved existing VocaPort `AGENTS.md` and README content as exact prefixes, left bilingual Project instructions/docs, product code/config, and release workflows unchanged, and used the published Agnir activation and `repository-filesystem/0.2` resolver. Paired untouched/install runs `33769075075` / `33769051389` showed identical product verification behavior: WASM bootstrap, typecheck, Web build, and downloads build succeeded on both; `pnpm test` and native-shell check failed on both. Those failures are therefore VocaPort baseline limitations rather than Agnir regressions.

No Agnir Core/profile `0.2` semantic defect was exposed by Svif, FishUp, or VocaPort.

## v1 readiness — current

- Core semantics: **provisionally satisfied**;
- compatibility/migration contract: **satisfied for current published lines**;
- real upgrade boundary: **satisfied** via Svif;
- real parallel continuity/reconciliation Project: **satisfied** via Svif;
- VCS + non-VCS lineage conformance: **satisfied**;
- materially different real Projects: **satisfied at the current minimum threshold (3)** via Svif + FishUp + VocaPort;
- materially different execution surfaces/adapters: **open** — product runtime diversity does not count; Agnir itself still needs a second distinct execution surface/adapter with fresh activation/resume/checkpoint evidence;
- real mount-boundary evidence: **open / explicitly unproven**;
- independent-implementation documentation quality: **open**;
- explicit `1.0.0-rc` cycle: **future gate after the remaining evidence gates close**.

The dated readiness snapshot in `V1_RELEASE_CRITERIA.md` remains a historical non-normative snapshot; current canonical readiness is this State plus current Evidence/Next Actions until the next formal gate-map refresh.
