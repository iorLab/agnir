# v1.0.0 Gate Summary

Agnir `v1.0.0` means downstream Projects may treat Agnir's published Core compatibility and migration behavior as stable infrastructure.

The release should not be triggered by feature count. It requires all of the following classes of evidence:

1. Core semantics have no known essential primitive awaiting a foreseeable breaking redesign.
2. Compatibility, deprecation, unsupported-version, and migration behavior are explicit.
3. Fresh install, compatible upgrade, incompatible migration/rejection, idempotence, and Project-content preservation are tested.
4. Multiple materially different real Projects and execution surfaces have exercised Agnir.
5. Core abstractions have evidence beyond a single backend model where backend neutrality is claimed.
6. Normative conformance is release-blocking and reproducible from a fresh environment.
7. Failure classes and recovery/retry behavior are stable where interoperability depends on them.
8. No known publication/checkpoint path can expose Project state and continuity state that knowingly disagree.
9. Published specs and conformance are sufficient for an independent implementation.
10. Release creation, exact source revision, tagging, distribution verification, and superseding/rollback procedures are repeatable.

Recommended confidence floor before `v1.0.0`: at least three materially different real Projects, at least two materially different execution surfaces/adapters, at least one real compatible upgrade, and—if Parallel Continuity enters Core—VCS + non-VCS conformance plus at least one real Project using independent lineages and reconciliation. Run at least one explicit `1.0.0-rc` cycle with no release-blocking Core defect before final release.
