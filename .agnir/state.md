# Agnir Current State

Durable continuity belongs to the Project.

Authoritative `main` carries the Agnir `1.0.0` stable source package and has passed the publication-precondition checkpoint. The exact prepublication checkpoint is `b99ea0d37cca852df023ef9071d4102c0376f0fe`; workflow `34038863673`, repository job `101501837860`, passed self-host cold start, historical Core/profile 0.1/0.2 regressions, Core/profile 1.0, 0.2→1.0 promotion, VCS/non-VCS lineage behavior, stable package gates, and the complete `test_*.py` suite. The stable publication job was correctly skipped at that checkpoint.

Stable `v1.0.0` publication is now **armed** by the sole exact-message transition `release: publish v1.0.0 stable`. No protocol, schema, resolver, package, README, or compatibility semantic change is part of this transition.

## Accepted release evidence

- accepted RC: `v1.0.0-rc.1` -> `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- RC Release id `383536840`;
- RC workflow `34026167762` attempts 1 and 2: success;
- RC acceptance checkpoint `afc07d062b957e8dbfe3f859834c787e64aa52be`;
- accepted stable staging source `65b5484b62bbd413d0984d5c952bc0a653da1964`, run `34030660332`;
- accepted staging checkpoint `5f88a9c8bcc67753012f8bcae533241482dc1a7d`, run `34030753962`;
- target validation revision `ab5dcc3341d39631e843499632739864a90bba14`, run `34030934536`;
- authoritative-main verification of that target: run `34030974021`, repository job `101480276759`;
- publication-precondition checkpoint `b99ea0d37cca852df023ef9071d4102c0376f0fe`, run `34038863673`, repository job `101501837860`.

## Current boundary

Wait for both jobs on this exact arm revision: `repository-filesystem` and `Publish v1.0.0 stable release`. If either fails, stable publication is not accepted. If both succeed, independently verify the immutable `v1.0.0` tag/Release/latest-state and accepted RC immutability before final canonical checkpointing.
