# Agnir Next Actions

1. Rename `mattamior/rpm` to `mattamior/agnir`.
2. Immediately after the rename, reconcile canonical repository references in `AGNIR.yaml`, `.chatgpt/project-memory.yaml`, README/docs, Svif dependency references, and CI/reference URLs; run Agnir conformance on the renamed repository rather than relying on GitHub redirects.
3. Coordinate the subsequent repository renames `iorLab/zerolocal` -> `iorLab/svif` and `iorLab/zerolocal-cloudflare-starter` -> `iorLab/svif-cloudflare-starter` so cross-project durable references converge on the new names.
4. Run and harden `conformance/check_agnir_0_1.py` against the repository/filesystem cold-start contract.
5. Add negative fixtures for broken locator, unsupported version, Project identity mismatch, and ambiguous/nested Project boundaries.
6. Add one materially non-repository backend fixture to demonstrate storage neutrality.
7. Add an external-memory locator fixture that distinguishes authorization failure from not-found without exposing secret values.
8. Add the multi-project workspace isolation case with independent Agnir state and locator-only workspace registry metadata.
9. Validate PPMP v2 -> Agnir migration against one external predecessor Project and record the migration evidence envelope.
10. Freeze Agnir Core `0.1` release compatibility notation only after the above conformance pressure cases pass.
11. Coordinate Svif's continuity dependency against the protocol line only; do not leak Svif delivery/provider semantics into Agnir Core.
12. Keep incidental branch cleanup deferred until the new version is substantially complete; preserve `legacy/ppmp-v2.0.0` unchanged as predecessor history.
