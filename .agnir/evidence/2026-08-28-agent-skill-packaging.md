# Agnir Agent Skill Packaging — 2026-08-28

## Problem

The earlier Quick Start conflated two different instruction surfaces: a user-facing installation request and the detailed procedure an Agent must execute. That made the user carry Agnir's internal implementation checklist and made the README itself act like the Skill procedure.

## Resolution

Agnir is now packaged as an Agent Skill through root `SKILL.md` with YAML frontmatter.

The boundary is:

```text
User
→ one-line install intent + Agnir repository URL
→ Agent locates iorLab/agnir
→ SKILL.md supplies the detailed Agent procedure
→ target Project is initialized
→ target AGENTS.md → target README Agnir Project Instructions → target AGNIR.yaml → durable memory
```

Reference user-facing prompts are intentionally short:

```text
Install and initialize Agnir for this Project: https://github.com/iorLab/agnir
```

```text
为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir
```

The detailed install / initialize / resume / checkpoint / repair procedure exists in `SKILL.md`, not in those prompts.

## Agent Skill contents

Root `SKILL.md`:

- identifies the Skill as `agnir` through YAML frontmatter;
- explains that the user does not carry the implementation checklist;
- classifies install/initialize, resume/use, checkpoint, and repair operations;
- applies `repository-filesystem/0.1` initialization safely while preserving unrelated target-Project content;
- installs the target Project's durable activation route;
- validates a fresh Project-root-only activation;
- keeps normal post-install runtime continuity independent from the installation conversation.

## Executable pressure

Added `conformance/test_skill_package.py` and extended `conformance/check_agnir_0_1.py` to require:

- root `SKILL.md` frontmatter and complete Agent procedure;
- exact bilingual one-line user install prompts;
- README references to `SKILL.md`;
- absence of the detailed numbered installation checklist from the user-facing Quick Start;
- continued durable target-Project activation and repository/filesystem conformance.

Skill packaging candidate `434f237dbcccfa8173a4d7f6be550ce9133bbc97` passed Agnir conformance run `33176730016`.

## Compatibility boundary

The Skill is an Agent-facing distribution/operation surface above Agnir Core and the repository/filesystem profile contract. It does not make Agent Skills, GitHub, or any particular execution platform a Core requirement.

This packaging was completed before the first `v0.1.0` publication. Core remains `0.1`, profile compatibility remains `repository-filesystem/0.1`, and repository SemVer remains `0.1.0`.
