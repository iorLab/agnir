# Persistent Project Memory (PPM)

Status: Reference Skill implementation of PPMP v2.0.0

Persistent Project Memory (PPM) is the first reference Skill/implementation of the Persistent Project Memory Protocol (PPMP). Its public product brand is **Sandminni**.

PPM is responsible for turning PPMP semantics into concrete operational behavior: discovering configuration through an adapter, reading and writing durable Core state through a backend, applying profile rules, checkpointing material changes, validating protocol compatibility, and reporting persistence outcomes accurately.

PPM MUST keep protocol requirements distinct from implementation conventions. A capability is not a PPMP requirement merely because PPM implements it.

## Initial stack

The first supported stack is:

- PPMP protocol v2;
- Persistent Project Memory (PPM) Skill/reference implementation, branded as Sandminni;
- repository/Git persistence backend;
- ChatGPT Project adapter.

This stack intentionally preserves the proven RPM v1 workflow while making each layer replaceable.

## Identity

The human-readable technical implementation name is **Persistent Project Memory**, abbreviated **PPM**. Reference manifests use the stable machine identifier `persistent-project-memory` rather than the bare acronym.

The public-facing product brand is **Sandminni**. The brand is intentionally separate from the protocol and implementation identifiers so product presentation can evolve without changing PPMP conformance semantics or stable machine identity.

Sandminni's visual metaphor is durable memory accumulating grain by grain. Future brand and logo work should explore the related motifs of **sand/grains**, **convergence or accumulation**, and **memory/durable continuity**.

## Conformance

A PPM release SHOULD declare supported PPMP protocol versions, supported backends/adapters, and any implementation-specific extensions. Extensions SHOULD be namespaced so they cannot be mistaken for protocol fields.
