# Persistent Project Memory (PPM)

Status: Reference implementation for iorMemory v2.0.0

Persistent Project Memory is the initial reference Skill/implementation of the iorMemory protocol.

PPM is responsible for turning protocol semantics into concrete operational behavior: discovering configuration through an adapter, reading and writing durable Core state through a backend, applying profile rules, checkpointing material changes, validating protocol compatibility, and reporting persistence outcomes accurately.

PPM MUST keep protocol requirements distinct from implementation conventions. A capability is not an iorMemory requirement merely because PPM implements it.

## Initial stack

The first supported stack is:

- iorMemory protocol v2;
- PPM implementation;
- repository/Git persistence backend;
- ChatGPT Project adapter.

This stack intentionally preserves the proven RPM v1 workflow while making each layer replaceable.

## Conformance

A PPM release SHOULD declare supported iorMemory protocol versions, supported backends/adapters, and any implementation-specific extensions. Extensions SHOULD be namespaced so they cannot be mistaken for protocol fields.
