# iorMemory

Status: Reference Skill implementation of PPMP v2.0.0

iorMemory is the first reference Skill/implementation of the Persistent Project Memory Protocol (PPMP).

iorMemory is responsible for turning PPMP semantics into concrete operational behavior: discovering configuration through an adapter, reading and writing durable Core state through a backend, applying profile rules, checkpointing material changes, validating protocol compatibility, and reporting persistence outcomes accurately.

iorMemory MUST keep protocol requirements distinct from implementation conventions. A capability is not a PPMP requirement merely because iorMemory implements it.

## Initial stack

The first supported stack is:

- PPMP protocol v2;
- iorMemory Skill/reference implementation;
- repository/Git persistence backend;
- ChatGPT Project adapter.

This stack intentionally preserves the proven RPM v1 workflow while making each layer replaceable.

## Conformance

An iorMemory release SHOULD declare supported PPMP protocol versions, supported backends/adapters, and any implementation-specific extensions. Extensions SHOULD be namespaced so they cannot be mistaken for protocol fields.
