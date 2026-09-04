# Agnir Next Actions

This validation lineage is staged to produce genuine mount-boundary evidence for the remaining Agnir v1 gate.

1. Run `.github/workflows/agnir-mount-boundary-validation.yml` on `validation/mount-boundary-v0.2.0`.
2. Require all positive-path checks to pass: Container A activation/discovery, mounted checkpoint persistence, Container A destruction, Container B fresh resume at a different mount path, and host receipt verification.
3. Require all negative-path checks to pass: read-only mount rejects checkpoint write; missing selected Project mount fails discovery explicitly; wrong/empty Project mount fails discovery explicitly.
4. Preserve the runtime receipt artifact and exact workflow run/job IDs for external review.
5. After external review, record the acceptance or defect in authoritative Agnir continuity. Do not merge this validation lineage into `main`.
6. If accepted, mark genuine mount-boundary evidence satisfied and move the v1 main line to independent-implementation documentation evidence.

## Acceptance boundary

The gate is not satisfied merely because Docker ran. The evidence must show the same Project identity and logical lineage resolving across different in-container Project paths, a checkpoint written through the bind mount surviving destruction of the first container, a fresh second container recovering it from Project-owned continuity, and explicit failure when the Project is absent/wrong/read-only for the relevant operation.
