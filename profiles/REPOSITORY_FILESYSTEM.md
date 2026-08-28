# Agnir Repository / Filesystem Profile 0.1

**Profile identifier:** `repository-filesystem/0.1`

This profile applies when the authorized Project Entry Point is a filesystem-style Project root, including a repository checkout/worktree, synced directory, hosted workspace filesystem, or equivalent hierarchical substrate.

This profile is not Agnir Core. It does not make filesystems, repositories, Git, GitHub, AI agents, Agent Skills, or any one agent-instruction filename universal Agnir requirements.

## 1. Discovery anchor

The Project root MUST contain top-level:

```text
AGNIR.yaml
```

An Executor that already knows this profile applies MUST inspect that anchor before relying on private execution context or hidden environment knowledge.

A filesystem indirection used as the authorized Project Entry Point (for example a symlink that resolves to one selected Project root) MAY be canonicalized before discovery, provided authority still selects exactly one Project root. The indirection does not authorize unrelated parent, child, sibling, or external memory.

## 2. Agent-operable Project activation and initialization

Agnir discovery and Agent activation are distinct concerns. `AGNIR.yaml` can only be discovered after an Executor knows to apply Agnir; therefore an Agent-operable repository MUST persist an activation route outside private chat or Agent memory.

For Projects intended to be resumed by general-purpose Agents through this profile, initialization MUST establish the following durable route:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

The reference activation contract is:

1. `README.md` MUST contain a canonical section headed `## Agnir Project Instructions`.
2. That section MUST state that the Project uses Agnir for durable continuity and MUST instruct an Agent, before Project work, to:
   - treat the Project root as the authorized Project Entry Point;
   - read top-level `AGNIR.yaml`;
   - load Current State and Next Actions;
   - load Decisions and Evidence when relevant;
   - prefer durable Agnir Project truth over chat history or private Agent memory unless superseded by a newer Principal instruction or directly observed current Project fact;
   - checkpoint material state, next-action, decision, and evidence changes at an intentional save/finish boundary.
3. Root `AGENTS.md` MUST point to the `README.md` **Agnir Project Instructions** section. `AGENTS.md` SHOULD remain a locator and SHOULD NOT duplicate the full activation contract, so the Project has one canonical instruction surface rather than two drifting copies.
4. Initialization MUST preserve unrelated existing README and `AGENTS.md` content. It MUST merge the Agnir section/reference rather than destructively replacing Project documentation or other Agent instructions.
5. Initialization MUST create or validate `AGNIR.yaml`, resolve all required memory locators, create any required initial durable memory, and persist at least one initialization Evidence object when Evidence is declared.
6. Initialization MUST finish with a fresh activation test from the Project root: resolve `AGENTS.md`, follow the README Agnir section, resolve `AGNIR.yaml`, load required continuity, and verify the Project no longer depends on the initialization conversation or initializing Agent's private memory.

### Existing AGENTS.md merge and conflict behavior

An Agent-operable initializer applying this profile MUST treat pre-existing root `AGENTS.md` as Project-owned instruction content, not as a replaceable Agnir template.

The reference behavior is:

1. If root `AGENTS.md` is absent, create a minimal Agent instruction file containing only the Agnir locator needed to reach README `Agnir Project Instructions`.
2. If root `AGENTS.md` exists, preserve existing unrelated instructions and merge only the minimal Agnir locator. Existing instructions MUST NOT be deleted, reordered, normalized, summarized, or silently rewritten merely to install Agnir.
3. If an equivalent Agnir locator already exists, the operation MUST be idempotent and MUST NOT create another copy.
4. Agnir content in `AGENTS.md` MUST remain locator-only. Current State, Next Actions, Decisions, Evidence, checkpoint procedure, and the full activation contract belong in their canonical Agnir locations, not as a duplicate `AGENTS.md` rule set.
5. The initializer MUST inspect for material conflicts before writing. A material conflict includes an existing instruction that directly contradicts the required activation route—for example, forbidding the Agent from reading/following `README.md`, forbidding `AGNIR.yaml`, disabling Agnir, or declaring a competing canonical Agnir instruction location.
6. If resolving a material conflict would require deleting, overriding, or reinterpreting an existing Project instruction, the initializer MUST NOT guess or silently overwrite it. It MUST surface the conflict to the Principal and MUST NOT report Agnir installation complete until the conflict is explicitly resolved and fresh activation passes.

Initializers SHOULD detect such conflicts in preflight before making any Agnir installation writes. A partially written setup does not satisfy this profile's completed initialization contract.

Once this route has been installed, a user SHOULD NOT need to repeat an Agnir bootstrap prompt for normal future work. An execution surface that does not automatically inspect Project instruction files may require one-time configuration to honor `AGENTS.md` / Project documentation; that execution-surface behavior is outside Agnir Core.

### Reference Agent Skill packaging

This reference repository publishes root `SKILL.md` as the Agent-facing procedure for applying this initialization contract. The user-facing request MAY remain a short intent statement such as “install and initialize Agnir”; the detailed procedural checklist belongs to the Skill, not to the user's prompt.

`SKILL.md` is a distribution/operation surface. It does not redefine this profile or Agnir Core, and another implementation MAY expose the same profile semantics through a different Agent Skill or non-Agent installer. After initialization, normal target-Project activation proceeds through the target Project's durable `AGENTS.md` → README → `AGNIR.yaml` route and does not depend on reopening the Skill repository.

This activation convention is profile-level guidance for Agent-operable repository Projects. Non-Agent Executors that are directly given the applicable profile implementation may begin at `AGNIR.yaml` as described by Core cold-start semantics.

## 3. Reference serialization

The profile uses YAML compatible with `schemas/agnir-manifest.schema.json`.

Required semantic shape:

```yaml
agnir:
  version: "0.1"
  discovery_profile: "repository-filesystem/0.1"
project:
  identity: <durable-project-identity>
memory:
  state: <locator>
  next_actions: <locator>
  decisions: <locator-or-null>
  evidence: <locator-or-null>
```

Relative locators resolve from the Project root. Absolute filesystem paths SHOULD be avoided unless the Project intentionally accepts that portability constraint.

A relative locator that traverses filesystem indirection outside the selected Project root MUST NOT be treated as an implicitly authorized external Locator Chain merely because the target is readable. External memory requires an explicit durable authorized binding/Locator Chain.

## 4. Profile and extension versioning

- `agnir.version` is the Core major.minor line as a string.
- `agnir.discovery_profile` is `<profile-name>/<major.minor>`.
- This profile requires `repository-filesystem/0.1`.
- A breaking change to the discovery anchor, required serialization, relative-locator interpretation, selected-root authority semantics, or stable activation route for Agent-operable Projects requires a new profile compatibility line after publication.
- A change only to the reference Skill's wording, packaging, or implementation procedure does not by itself change profile compatibility if the same profile contract remains satisfied.
- `extensions` keys use `<owner>/<name>` namespaces.
- `agnir/*` extension namespaces are reserved for Agnir-defined extensions.
- Extensions MUST NOT redefine Core fields while claiming the same Core version.

## 5. Project identity and selected-root authority

`project.identity` MUST be non-empty. URI/URN forms are RECOMMENDED for identities intended to survive backend or host changes. Opaque identifiers MAY be used when the Project boundary makes them unambiguous.

Nested Projects are allowed, but each Project Entry Point MUST select one Project root. Implementations MUST NOT silently walk into an unrelated parent/child Project when the selected boundary already determines authority.

A parent and child directory may each contain their own authoritative `AGNIR.yaml`. Once one of those roots has been selected as the authorized Project Entry Point, the existence of the other does **not** make the selected root ambiguous; discovery remains scoped to the selected root. `AGNIR_DISCOVERY_AMBIGUOUS` applies earlier, when multiple candidate Project roots exist and no authority rule has selected exactly one.

A detected identity mismatch at the selected root MUST surface `AGNIR_DISCOVERY_PROJECT_MISMATCH` rather than searching a parent or child root for a more convenient identity.

## 6. Colocated memory

`.agnir/` is the recommended reference layout for colocated memory, but it is not authoritative by name. `AGNIR.yaml` locators are authoritative.

A Project MAY locate memory elsewhere, including outside the Project root, when the active backend/adapter provides a durable authorized Locator Chain.

## 7. Repository/VCS extension

Repository-aware implementations MAY declare repository metadata under an extension namespace, for example:

```yaml
extensions:
  agnir/repository:
    canonical: "owner/name"
    authoritative_ref: "main"
```

This extension is profile/backend metadata, not Core identity. A non-default authoritative ref MUST be durably discoverable; a fresh Executor cannot be expected to remember it from a prior session.

A Git worktree is a valid filesystem-style Project root when the selected worktree contains the authoritative top-level `AGNIR.yaml` and its declared continuity locators resolve for that worktree. Agnir discovery MUST NOT depend on `.git` being a directory rather than Git's worktree metadata file.

## 8. Discovery order

For an Agent-operable repository initialized under the reference activation contract:

1. receive the authorized Project root;
2. resolve root `AGENTS.md`;
3. follow its pointer to `README.md` **Agnir Project Instructions**;
4. read `AGNIR.yaml`;
5. validate Core/profile compatibility;
6. verify Project identity;
7. resolve required memory locators;
8. load Current State and Next Actions;
9. load Decisions/Evidence as required;
10. surface Agnir discovery failure semantics.

A non-Agent Executor or adapter that already knows this profile applies MAY begin at step 4.

Implementations MUST NOT silently search arbitrary sibling repositories, user home directories, old chat logs, or historical predecessor layouts when `AGNIR.yaml` is missing.

## 9. Conformance

A profile conformance case SHOULD begin with only the Project root and profile implementation. It MUST prove discovery of `AGNIR.yaml`, version and identity validation, resolution of Current State and Next Actions, recovery of at least one material durable fact, and correct failure for at least one broken-locator case.

An Agent-operable initialization conformance case additionally MUST prove that a fresh Agent activation context can start with only the Project root, resolve `AGENTS.md` to the canonical README Agnir instruction, and then complete Agnir discovery without any repeated user bootstrap prompt or prior conversation.

The reference Agent-initialization conformance also pressure-tests non-destructive merge into an existing `AGENTS.md`, minimal creation when it is absent, idempotent existing locator behavior, and explicit failure on a contradictory existing Agent instruction rather than silent overwrite.

The active reference conformance suite additionally pressure-tests explicit `NOT_FOUND`, `UNRESOLVABLE`, `UNSUPPORTED_VERSION`, `PROJECT_MISMATCH`, and pre-root-selection `AMBIGUOUS` semantics, isolation between explicitly selected nested Project roots, a symlinked Project Entry Point, rejection of relative-locator symlink escape without an explicit external binding, and Git worktree cold start.

Real mount-boundary behavior remains an environment-dependent pressure case. It MUST NOT be claimed proven by simulating a mount with an ordinary directory.
