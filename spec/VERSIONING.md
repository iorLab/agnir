# Versioning

Version: 2.0.0

PPMP follows Semantic Versioning.

- **MAJOR** — incompatible changes to Core semantics, required configuration semantics, conformance, or normative behavior.
- **MINOR** — backward-compatible profiles, optional fields, extension points, or capabilities.
- **PATCH** — clarifications and backward-compatible corrections.

The repository root `VERSION` declares the current PPMP protocol version.

A project MUST record the PPMP version it conforms to. An implementation MUST NOT silently reinterpret a project using a newer incompatible major version.

For the same supported MAJOR, an implementation may accept an equal/older MINOR. A newer unknown MINOR may be accepted only when unknown optional fields can be safely ignored. A different MAJOR requires explicit migration.

Upgrades MUST preserve durable project knowledge and MUST update the declared version only after the project conforms to the target semantics.

Implementation, backend, and adapter versions MAY evolve independently, but they MUST state which PPMP protocol versions they support.

## Historical boundary

RPM v1.0.0 is the predecessor design. PPMP v2.0.0 is an intentional incompatible protocol transition because repository/Git and ChatGPT-specific requirements are removed from the protocol layer. See `MIGRATION.md`.
