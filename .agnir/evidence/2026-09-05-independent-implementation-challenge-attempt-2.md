# Independent implementation challenge — preserved attempt 2

Date: 2026-09-05
Status: failed attempt; evidence retained; v1 documentation gate remains open

## Challenge

- public challenge: `iorLab/agnir#15`;
- pinned source: `d4d5c5a441766ca5993366429ecf6235d7c2a7bc`;
- execution context: fresh unpersonalized Temporary Chat, isolated from prior Agnir challenge material/private design context as required by the issue;
- complete challenge archive supplied by the Principal and independently rechecked before this checkpoint;
- archive SHA-256: `1426e0c4a3b9030944ad2694aaf9ff7daf4690b3f7fb1ce8cab9ba3f1dcc4a61`;
- ZIP integrity: `unzip -t` passed with no errors;
- archive contained 19 challenge files covering source classification, frozen Phase A reconstruction, ambiguity log, independently authored Phase B implementation/tests/receipts, Phase C comparison/probe, and final verdict.

The archive itself is not treated as a repository-hosted normative source. This Evidence records the verified challenge outcome and the public repository corrections it triggered.

## Reviewer verdict

Final challenge verdict: **`FAIL-IMPLEMENTATION`**.

The reviewer correctly reconstructed the published Core/profile `0.2` serialization during frozen Phase A, including `agnir.discovery_profile` and `memory.next_actions`, but the independently authored Phase B code later used incompatible shorthand fields (`agnir.profile`, `memory.next`) and the wrong `policy.checkpoint` enum. Phase C demonstrated that this implementation rejected a valid published `0.2` manifest. The reviewer therefore correctly classified the immediate run failure as an independent implementation defect rather than a missing-documentation explanation for those specific fields.

Because Phase C exposed the reference implementation, this reviewer/session is no longer eligible to serve as the fresh independent implementer for the next acceptance attempt.

## Public-source defects and latitude still recorded by the challenge

The failed run nevertheless preserved public-contract findings that must not be ignored merely because the direct verdict was `FAIL-IMPLEMENTATION`:

1. `spec/CORE_0_1_TO_0_2_MIGRATION.md` still labeled itself `Draft` / `Experimental` and claimed Core `0.1` remained the published stable line, while `RELEASE.md` listed that same file among stable normative `v0.2.0` contracts. This is a genuine public status conflict.
2. `conformance/test_repository_filesystem_0_2.py` still used the stale test name `test_experimental_schema_declares_core_and_profile_0_2` after the schema/profile became stable.
3. Phase C recorded machine-visible latitude around failure classification for profile mismatch and local-locator escape. The reference resolver uses `AGNIR_DISCOVERY_INCONSISTENT` for profile mismatch and `AGNIR_DISCOVERY_UNRESOLVABLE` for a local locator escaping the selected Project root without an authorized external Locator Chain.
4. Separately rechecked against the same pinned public source, root `SKILL.md` told all VCS branch/worktree/integration work to apply `profiles/VCS_BRANCH_CONTINUITY.md`, even though that file explicitly defines an experimental Core/profile `0.1` extension and deliberately predates Core `0.2` logical Continuity Lineage semantics. Core/profile `0.2` already carries its normative VCS selector/binding/fork/rebind/integration semantics in `spec/AGNIR_CORE_0_2.md` and `profiles/REPOSITORY_FILESYSTEM_0_2.md`.
5. `RELEASE.md` and `.agnir/decisions.md` still contained stale text saying real mount-boundary behavior was unproven despite accepted 2026-09-04 bind-mount evidence.

## Repair decision

Before another independent attempt, authoritative public material must be made internally consistent without changing Core/profile `0.2` semantics:

- promote the migration document's metadata/text to the stable normative status already established by the published release;
- distinguish Core/profile `0.1` VCS extension applicability from Core/profile `0.2` VCS normative sources in `SKILL.md`;
- make repository-filesystem `0.2` failure mapping explicit for Core-version mismatch, profile mismatch, identity/lineage mismatch, local locator failure, and actual external authorization failure;
- add conformance pressure for those mappings and remove stale `experimental` naming;
- refresh stale post-release/mount readiness wording;
- preserve the failed independent implementation as evidence rather than correcting its frozen Phase B code.

These are stable `0.2.x` documentation/conformance repairs, not a Core compatibility redesign.

## Gate consequence

The independent-implementation v1 gate remains **open**. A new exact authoritative source revision must be produced and verified after the public repairs above. Acceptance then requires another genuinely fresh independent reviewer/session that has not seen prior challenge reports or reference implementation code.

Core/profile `1.0` promotion and the explicit repository `1.0.0-rc` cycle remain downstream of a successful independent-implementation gate; they must not be mixed into this repair evidence.
