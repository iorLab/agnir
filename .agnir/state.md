# Agnir Current State

Durable continuity belongs to the Project.

An authoritative-target candidate for Agnir `v1.0.0` has been constructed from exact authoritative base `11148c3063e63dd1ea7450b9d538ac1eccec5639` plus the accepted stable staging checkpoint `5f88a9c8bcc67753012f8bcae533241482dc1a7d`.

The target candidate preserves authoritative Project identity `urn:agnir:project:agnir-core`, logical Continuity Lineage identity `urn:agnir:lineage:authoritative`, and selector `refs/heads/main`. Release-lineage continuity was not copied wholesale; accepted staging state/evidence were reconciled into target-specific truth.

Stable publication remains **not armed**. The intended sequence is exact target-candidate CI, one more authoritative-main stale check, coherent target advancement, exact-main CI, then a separate exact publication-arm commit.

## Accepted inputs

- authoritative target base: `11148c3063e63dd1ea7450b9d538ac1eccec5639`;
- accepted stable staging revision: `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`, repository job `101479440549`, success;
- accepted stable staging checkpoint: `5f88a9c8bcc67753012f8bcae533241482dc1a7d`, run `34030753962`, repository job `101479690113`, success;
- accepted immutable RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC Release id `383536840`;
- RC workflow `34026167762` attempts 1 and 2: success;
- RC acceptance checkpoint `afc07d062b957e8dbfe3f859834c787e64aa52be`.

## Target package

- repository version: `1.0.0`;
- Core/profile: `1.0` / `repository-filesystem/1.0`;
- stable Core/profile/promotion contracts are normative;
- historical Core/profile `0.1` and `0.2` compatibility/migration surfaces remain shipped and tested;
- stable publication is main-only and exact-source gated;
- accepted RC immutability is a stable publication precondition.

No breaking Core/profile semantic change was introduced after accepted RC. Remaining work is target validation, authoritative advancement, publication, and final receipt checkpointing.
