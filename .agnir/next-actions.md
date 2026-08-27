# Agnir Next Actions

1. Run and harden `conformance/check_agnir_0_1.py` against the repository/filesystem cold-start contract.
2. Add negative fixtures for broken locator, unsupported version, Project identity mismatch, and ambiguous/nested Project boundaries.
3. Add one materially non-repository backend fixture to demonstrate storage neutrality.
4. Add an external-memory locator fixture that distinguishes authorization failure from not-found without exposing secret values.
5. Add the multi-project workspace isolation case with independent Agnir state and locator-only workspace registry metadata.
6. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
7. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
8. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif delivery/provider semantics into Agnir Core.
9. Defer repository/public-brand rename and incidental branch cleanup until the new version is substantially complete.
