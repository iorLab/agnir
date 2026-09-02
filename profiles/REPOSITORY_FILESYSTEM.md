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

A filesystem indirection used as the authorized Project Entry Point MAY be canonicalized before discovery when authority still selects exactly one Project root. The indirection does not authorize unrelated parent, child, sibling, or external memory.

## 2. Agent-operable Project activation and initialization

Agnir discovery and Agent activation are distinct concerns. `AGNIR.yaml` can only be discovered after an Executor knows to apply Agnir; therefore an Agent-operable repository MUST persist an activation route outside private chat or Agent memory.

For Projects intended to be resumed by general-purpose Agents through this profile, initialization MUST establish:

```text
Project root
→ AGENTS.md
→ README.md / Agnir Project Instructions
→ AGNIR.yaml
→ declared durable memory
```

The reference activation contract is:

1. `README.md` MUST contain a canonical section headed `## Agnir Project Instructions`.
2. That section MUST state that the Project uses Agnir for durable continuity and instruct an Agent, before Project work, to treat the Project root as the authorized Project Entry Point, read top-level `AGNIR.yaml`, load Current State and Next Actions, load Decisions/Evidence when relevant, prefer current durable Project truth over older private context, and checkpoint material changes at intentional save/finish boundaries.
3. Root `AGENTS.md` MUST point to the README **Agnir Project Instructions** section and SHOULD remain locator-only for Agnir.
4. Initialization MUST preserve unrelated existing README and `AGENTS.md` content and merge rather than destructively replace it.
5. Initialization MUST create or validate `AGNIR.yaml`, resolve all required memory locators, create any required initial durable memory, and persist at least one initialization Evidence object when Evidence is declared.
6. Initialization MUST finish with a fresh activation test from the Project root and prove continuation no longer depends on the initialization conversation or initializing Agent's private memory.

### Existing AGENTS.md merge and conflict behavior

An Agent-operable initializer applying this profile MUST treat pre-existing root `AGENTS.md` as Project-owned instruction content, not as a replaceable Agnir template.

1. If root `AGENTS.md` is absent, create a minimal Agent instruction file containing only the Agnir locator needed to reach README `Agnir Project Instructions`.
2. If root `AGENTS.md` exists, preserve existing unrelated instructions and merge only the minimal Agnir locator. Existing instructions MUST NOT be deleted, reordered, normalized, summarized, or silently rewritten merely to install Agnir.
3. If an equivalent Agnir locator already exists, the operation MUST be idempotent and MUST NOT create another copy.
4. Agnir content in `AGENTS.md` MUST remain locator-only.
5. The initializer MUST inspect for material conflicts before writing.
6. If resolving a material conflict would require deleting, overriding, or reinterpreting an existing Project instruction, the initializer MUST NOT guess or silently overwrite it. It MUST surface the conflict to the Principal and MUST NOT report installation complete until explicitly resolved and fresh activation passes.

Initializers SHOULD detect such conflicts in preflight before making any Agnir installation writes. A partially written setup does not satisfy this profile's completed initialization contract.

Once this route has been installed, a user SHOULD NOT need to repeat an Agnir bootstrap prompt for normal future work. An execution surface that does not automatically inspect Project instruction files may require one-time configuration; that behavior is outside Agnir Core.

### Reference Agent Skill packaging

This reference repository publishes root `SKILL.md` as the Agent-facing procedure for applying installation, upgrade, resume, checkpoint, commit/push, and repair behavior. User-facing requests MAY remain short intent statements; the detailed procedural checklist belongs to the Skill, not to the user's prompt.

`SKILL.md` is a distribution/operation surface. It does not redefine this profile or Agnir Core. After initialization, normal target-Project activation proceeds through the target Project's durable `AGENTS.md` → README → `AGNIR.yaml` route and does not depend on reopening the Skill repository.

### Existing Project upgrade and operational provenance

Upgrade is distinct from initialization. A compatible operational upgrade MUST begin by activating the existing Project and preserving its authoritative continuity rather than rebuilding `.agnir/` from templates.

For an upgrade to remain compatible with this profile:

- the target Core compatibility line MUST remain `0.1`;
- the target profile compatibility line MUST remain `repository-filesystem/0.1`;
- `project.identity`, declared memory locators, durable memory contents, unrelated README/`AGENTS.md` content, and unrelated manifest extensions MUST be preserved unless a separately authorized migration changes them;
- changing only Agent Skill wording, activation procedure, operational tooling, or non-breaking conformance does not by itself change the profile compatibility line;
- if either Core or profile compatibility changes, the operation is a migration, not a compatible upgrade, and MUST NOT silently rewrite the Project to the new line.

A Project created before operational provenance was introduced remains valid. Missing provenance is not a reason to re-initialize the Project.

Repository/filesystem Projects MAY record the operational package that was last applied:

```yaml
extensions:
  agnir/operations:
    distribution: "agnir-agent-skill"
    release: "0.1.0"
    source: "iorLab/agnir"
    applied_revision: "<immutable source revision>"
```

`agnir/operations` is optional operational provenance. It is not Core identity, does not replace `agnir.version` or `agnir.discovery_profile`, and MUST NOT be used to redefine Project identity or continuity locators.

When the Principal asks for the **latest stable release**, an implementation MUST resolve an actually published stable release/tag. It MUST NOT silently interpret a moving `main` branch, another moving branch, or an untagged revision as stable. A non-stable target MAY be used only with explicit authorization.

A compatible upgrade SHOULD non-destructively merge the target Agnir-owned activation/procedure content, update operational provenance, checkpoint material upgrade facts, and finish with a fresh activation test. In VCS, the implementation SHOULD publish the Project upgrade and its continuity update as one coherent revision when possible. If the same operational baseline is already applied and no material drift exists, the upgrade result SHOULD be a no-op.

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
- A change only to the reference Skill's wording, packaging, implementation procedure, or compatible operational upgrade behavior does not by itself change profile compatibility if the same profile contract remains satisfied.
- `extensions` keys use `<owner>/<name>` namespaces.
- `agnir/*` extension namespaces are reserved for Agnir-defined extensions.
- Extensions MUST NOT redefine Core fields while claiming the same Core version.

## 5. Project identity and selected-root authority

`project.identity` MUST be non-empty. URI/URN forms are RECOMMENDED for identities intended to survive backend or host changes. Opaque identifiers MAY be used when the Project boundary makes them unambiguous.

Nested Projects are allowed, but each Project Entry Point MUST select one Project root. Implementations MUST NOT silently walk into an unrelated parent/child Project when the selected boundary already determines authority.

A parent and child directory may each contain their own authoritative `AGNIR.yaml`. Once one root is selected as the authorized Project Entry Point, the existence of the other does not make the selected root ambiguous. `AGNIR_DISCOVERY_AMBIGUOUS` applies before authority has selected exactly one root.

A detected identity mismatch at the selected root MUST surface `AGNIR_DISCOVERY_PROJECT_MISMATCH` rather than searching for a more convenient identity.

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

This extension is profile/backend metadata, not Core identity. A non-default authoritative ref MUST be durably discoverable.

`authoritative_ref` identifies repository publication authority; it is not necessarily the active checkout/ref and MUST NOT be interpreted as the only ref on which Agnir continuity may be evaluated or checkpointed.

A Git worktree is a valid filesystem-style Project root when the selected worktree contains authoritative top-level `AGNIR.yaml` and its declared continuity locators resolve for that worktree. Discovery MUST NOT depend on `.git` being a directory rather than Git worktree metadata.

Branch-aware repository implementations MAY additionally apply the experimental `agnir/vcs-branch-continuity/0.1` extension defined in `profiles/VCS_BRANCH_CONTINUITY.md`. That extension treats branch/ref names as VCS locators/runtime observations rather than Project identity, permits branch-local continuity after divergence, and requires explicit target continuity reconciliation across merge/rebase/cherry-pick integration boundaries. It does not change Agnir Core `0.1` or this profile's discovery compatibility line.

### Commit and push event integration

For a repository-aware implementation that can create or observe VCS revisions, commit/push intent is a natural checkpoint boundary without making VCS part of Agnir Core.

- When an authorized Principal asks the Executor to commit Project changes, the implementation SHOULD evaluate and reconcile material Agnir continuity **before** creating the VCS revision.
- When both Project changes and Agnir continuity changes can be represented in the same VCS revision, the implementation SHOULD publish them together in one revision rather than creating a follow-up checkpoint-only revision.
- If checkpoint evaluation finds no material continuity change, the implementation SHOULD leave Agnir memory unchanged and proceed with the requested commit.
- When the request includes push/publication, the implementation SHOULD verify after push that the intended published revision reached the **actual destination ref** selected by the authorized operation.
- If the operation additionally claims that authoritative repository truth was published and `agnir/repository.authoritative_ref` is declared, the destination MUST match that authoritative ref and the implementation SHOULD verify the intended revision there. A feature-branch push MUST NOT be silently redirected to or reported as publication of the authoritative ref merely because `authoritative_ref` exists.
- Observing a commit created by another Executor, web UI, CI, IDE, or other mechanism MAY trigger checkpoint evaluation. Observation alone MUST NOT imply an unconditional continuity write.
- Repository hooks such as `pre-commit` or `pre-push` MAY implement these events, but hooks are adapter/implementation mechanisms and MUST NOT become a discovery or continuity dependency.
- A VCS-generated revision identifier MAY be used as the backend checkpoint receipt. The checkpoint content MUST NOT be required to embed its own resulting revision identifier.

Agent-facing integrations MAY recognize phrases such as `commit`, `commit and push`, `提交`, `提交代码`, and `提交推送` when repository context makes VCS intent clear. Such phrases are integration vocabulary, not Core keywords.

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

An Agent-operable initialization conformance case additionally MUST prove fresh activation from only the Project root and the durable activation route.

Compatible-upgrade conformance SHOULD prove that an old Project with valid Core/profile compatibility but missing operational provenance can be upgraded without changing Project identity or memory locators; that the same applied provenance yields a no-op; that non-stable targets require explicit opt-in; and that Core/profile changes are classified as migration rather than silently applied.

The active reference suite additionally pressure-tests non-destructive `AGENTS.md` merge, all named discovery failures, multi-project isolation, transactional checkpoint semantics, external authorization, symlink boundaries, real Git worktree cold start, and experimental branch-local VCS continuity/reconciliation behavior.

Real mount-boundary behavior remains an environment-dependent pressure case. It MUST NOT be claimed proven by simulating a mount with an ordinary directory.
