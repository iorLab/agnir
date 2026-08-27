# Agnir Next Actions

1. Run and harden `conformance/check_agnir_0_1.py` against the repository/filesystem cold-start contract on the renamed canonical repository `iorLab/agnir`.
2. Add negative fixtures for broken locator, unsupported version, Project identity mismatch, and ambiguous/nested Project boundaries.
3. Add one materially non-repository backend fixture to demonstrate storage neutrality.
4. Add an external-memory locator fixture that distinguishes authorization failure from not-found without exposing secret values.
5. Add the multi-project workspace isolation case with independent Agnir state and locator-only workspace registry metadata.
6. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
7. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
8. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif delivery/provider semantics into Agnir Core.
9. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.

## Completed in the current implementation sequence

- Repository identity transition completed: `mattamior/rpm` was renamed and transferred to `iorLab/agnir`; `iorLab/zerolocal` became `iorLab/svif`; `iorLab/zerolocal-cloudflare-starter` became `iorLab/svif-cloudflare-starter`.
- Canonical Agnir repository references were reconciled to `iorLab/agnir` in `AGNIR.yaml`, the ChatGPT bootstrap shim, and durable Project state.
