#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from activation_reference import ActivationFailure, resolve_agent_activation
from repository_filesystem_reference import (
    CORE_VERSION,
    PROFILE,
    DiscoveryFailure,
    discover_repository_filesystem,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "agnir-manifest.schema.json"
SELF_PROJECT_ID = "urn:agnir:project:agnir-core"
REPOSITORY_VERSION = "0.1.0"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_skill_package() -> None:
    path = ROOT / "SKILL.md"
    if not path.exists():
        fail("missing root SKILL.md Agent Skill entrypoint")
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with Agent Skill YAML frontmatter")
    for marker in (
        "name: agnir",
        "description:",
        "Do not require the user to carry Agnir's implementation checklist",
        "## Install or initialize Agnir",
        "### Merge existing AGENTS.md safely",
        "preserve its existing unrelated content",
        "equivalent Agnir locator already exists",
        "do not guess and do not overwrite it",
        "report the exact conflict to the Principal",
        "## Upgrade an existing Agnir Project",
        "latest stable release",
        "Do not silently treat `main`",
        "AGNIR_UPGRADE_MIGRATION_REQUIRED",
        "agnir/operations",
        "applied_revision",
        "## Resume or use an existing Agnir Project",
        "## Checkpoint",
        "## Commit and push integration",
        "AGNIR_CHECKPOINT_CONFLICT",
        "提交代码",
        "提交推送",
        "## Repair",
        "AGNIR.yaml",
        "AGENTS.md",
        "Agnir Project Instructions",
        ".agnir/state.md",
        ".agnir/next-actions.md",
        ".agnir/decisions.md",
        ".agnir/evidence/",
        "fresh activation test",
    ):
        if marker not in text:
            fail(f"SKILL.md missing required Agent procedure marker: {marker}")


def require_readme_quick_start(
    path: str,
    *,
    quick_start_heading: str,
    architecture_heading: str,
    install_prompt: str,
    existing_marker: str,
    forbidden_checklist: str,
) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for marker in (
        quick_start_heading,
        install_prompt,
        existing_marker,
        "SKILL.md",
        "AGENTS.md",
        "Agnir Project Instructions",
    ):
        if marker not in text:
            fail(f"{path} missing required user-facing Quick Start marker: {marker}")

    quick_start_position = text.find(quick_start_heading)
    architecture_position = text.find(architecture_heading)
    if quick_start_position < 0 or architecture_position < 0 or quick_start_position > architecture_position:
        fail(f"{path} must present Quick Start before architecture material")

    quick_start = text[quick_start_position:architecture_position]
    if forbidden_checklist in quick_start:
        fail(f"{path} must keep the Agent implementation checklist in SKILL.md, not the user Quick Start")


def require_readme_diagrams(path: str, headings: tuple[str, str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if text.count("```mermaid") < 2:
        fail(f"{path} must contain at least two Mermaid diagrams")
    for heading in headings:
        if heading not in text:
            fail(f"{path} missing required diagram section: {heading}")
    for marker in ("SKILL.md", "AGENTS.md", "README", "AGNIR.yaml"):
        if marker not in text:
            fail(f"{path} diagrams/explanation missing install/activation marker: {marker}")


def require_readme_repository_tree(path: str, heading: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for marker in (
        heading,
        "agnir/",
        "├── spec/",
        "├── profiles/",
        "├── conformance/",
        "├── .agnir/",
        "├── history/",
        "SKILL.md",
        "AGENTS.md",
        "activation_reference.py",
        "checkpoint_reference.py",
        "test_skill_package.py",
        "REPOSITORY_TREE.md",
        "RELEASE.md",
    ):
        if marker not in text:
            fail(f"{path} missing required repository-structure marker: {marker}")


def require_full_repository_tree() -> None:
    text = (ROOT / "REPOSITORY_TREE.md").read_text(encoding="utf-8")
    for marker in (
        "# Repository Tree",
        "spec/",
        "AGNIR_CORE.md",
        "AGNIR_DISCOVERY.md",
        "profiles/",
        "REPOSITORY_FILESYSTEM.md",
        "schemas/",
        "agnir-manifest.schema.json",
        "conformance/",
        "activation_reference.py",
        "agents_merge_reference.py",
        "checkpoint_reference.py",
        "upgrade_reference.py",
        "test_checkpoint_semantics.py",
        "test_upgrade_semantics.py",
        "test_agent_activation.py",
        "test_agents_merge.py",
        "test_skill_package.py",
        "repository_filesystem_reference.py",
        "external_memory_reference.py",
        "locator_chain_reference.py",
        "sqlite_backend_reference.py",
        "workspace_registry_reference.py",
        ".agnir/",
        "evidence/",
        "history/",
        "PREDECESSOR.md",
        "MIGRATION_PPMP_V2.md",
        "BRANCH_ARCHIVE.md",
        ".github/",
        "conformance.yml",
        "SKILL.md",
        "AGENTS.md",
        "AGNIR.yaml",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "RELEASE.md",
        "VERSION",
    ):
        if marker not in text:
            fail(f"REPOSITORY_TREE.md missing required structure marker: {marker}")


def main() -> None:
    require_skill_package()

    try:
        activation = resolve_agent_activation(ROOT)
    except ActivationFailure as exc:
        fail(str(exc))
    if "AGNIR.yaml" not in activation.readme_section:
        fail("self-hosted Agent activation did not resolve the canonical Agnir instruction")

    try:
        snapshot = discover_repository_filesystem(
            ROOT,
            expected_project_identity=SELF_PROJECT_ID,
        )
    except DiscoveryFailure as exc:
        fail(str(exc))

    if "Durable continuity belongs to the Project" not in snapshot.state:
        fail("cold-start fixture did not recover the expected material durable fact")

    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"manifest schema is not valid JSON: {exc}")
    version_const = schema["properties"]["agnir"]["properties"]["version"]["const"]
    profile_const = schema["properties"]["agnir"]["properties"]["discovery_profile"]["const"]
    if version_const != snapshot.version or profile_const != snapshot.profile:
        fail("manifest and JSON Schema version/profile declarations diverge")
    if snapshot.version != CORE_VERSION or snapshot.profile != PROFILE:
        fail("self-hosted discovery returned an unexpected Core/profile line")

    repository_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if repository_version != REPOSITORY_VERSION:
        fail(f"expected repository release version {REPOSITORY_VERSION}, got {repository_version}")

    manifest_text = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    if "predecessor_ref:" in manifest_text:
        fail("active AGNIR.yaml must not depend on a retired predecessor branch ref")

    core_text = (ROOT / "spec" / "AGNIR_CORE.md").read_text(encoding="utf-8")
    for marker in (
        "Checkpoints and authoritative transition",
        "no-op",
        "mixed checkpoint generations",
        "AGNIR_CHECKPOINT_CONFLICT",
    ):
        if marker not in core_text:
            fail(f"Agnir Core missing checkpoint invariant marker: {marker}")

    profile_text = (ROOT / "profiles" / "REPOSITORY_FILESYSTEM.md").read_text(encoding="utf-8")
    if ".chatgpt/project-memory.yaml" in profile_text:
        fail("active repository/filesystem profile must not define predecessor bootstrap fallback")
    for marker in (
        "Agent-operable Project activation and initialization",
        "Existing AGENTS.md merge and conflict behavior",
        "AGENTS.md",
        "Agnir Project Instructions",
        "fresh activation test",
        "SHOULD NOT need to repeat an Agnir bootstrap prompt",
        "MUST NOT guess or silently overwrite it",
        "Existing Project upgrade and operational provenance",
        "agnir/operations",
        "applied_revision",
        "latest stable release",
        "MUST NOT silently interpret a moving `main`",
        "Commit and push event integration",
        "提交代码",
        "提交推送",
        "one revision",
    ):
        if marker not in profile_text:
            fail(f"repository/filesystem profile missing activation/upgrade/event contract marker: {marker}")

    release_text = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
    for marker in (
        REPOSITORY_VERSION,
        'Core compatibility line:** `0.1`',
        'repository-filesystem/0.1',
        'SKILL.md',
        'upgrade',
        'AGENTS.md',
        'Agnir Project Instructions',
    ):
        if marker not in release_text:
            fail(f"RELEASE.md missing release marker: {marker}")

    required_active = [
        "SKILL.md",
        "AGENTS.md",
        "README.md",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "RELEASE.md",
        "spec/AGNIR_CORE.md",
        "spec/AGNIR_DISCOVERY.md",
        "profiles/REPOSITORY_FILESYSTEM.md",
        "history/PREDECESSOR.md",
        "history/MIGRATION_PPMP_V2.md",
        "history/BRANCH_ARCHIVE.md",
        "conformance/activation_reference.py",
        "conformance/agents_merge_reference.py",
        "conformance/checkpoint_reference.py",
        "conformance/upgrade_reference.py",
        "conformance/test_checkpoint_semantics.py",
        "conformance/test_upgrade_semantics.py",
        "conformance/test_agent_activation.py",
        "conformance/test_agents_merge.py",
        "conformance/test_skill_package.py",
        "conformance/core_reference.py",
        "conformance/repository_filesystem_reference.py",
        "conformance/test_repository_filesystem_failures.py",
        "conformance/test_repository_filesystem_boundaries.py",
        "conformance/sqlite_backend_reference.py",
        "conformance/test_sqlite_backend.py",
        "conformance/external_memory_reference.py",
        "conformance/test_external_memory_authorization.py",
        "conformance/workspace_registry_reference.py",
        "conformance/test_workspace_isolation.py",
        "conformance/locator_chain_reference.py",
        "conformance/test_locator_chain_failures.py",
    ]
    for path in required_active:
        if not (ROOT / path).exists():
            fail(f"missing active Agnir artifact: {path}")

    require_readme_quick_start(
        "README.md",
        quick_start_heading="## 30-second Quick Start",
        architecture_heading="## Architecture Diagram",
        install_prompt="Install and initialize Agnir for this Project: https://github.com/iorLab/agnir",
        existing_marker="No recurring Agnir prompt is required.",
        forbidden_checklist="Requirements:\n1.",
    )
    require_readme_quick_start(
        "README.zh-CN.md",
        quick_start_heading="## 30 秒快速开始",
        architecture_heading="## 架构图",
        install_prompt="为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir",
        existing_marker="不需要再给 Agent 任何 Agnir bootstrap 提示词。",
        forbidden_checklist="要求：\n1.",
    )
    require_readme_diagrams("README.md", ("## Architecture Diagram", "## Continuity Flow"))
    require_readme_diagrams("README.zh-CN.md", ("## 架构图", "## 连续性流程"))
    require_readme_repository_tree("README.md", "## Repository structure")
    require_readme_repository_tree("README.zh-CN.md", "## 仓库结构")
    require_full_repository_tree()

    forbidden = [
        "docs",
        "adapters",
        "backends",
        "examples",
        "implementations",
        "site",
        "templates",
        "spec/MIGRATION_PPMP_V2.md",
        "spec/AGNIR_CORE_DRAFT.md",
        "spec/AGNIR_DISCOVERY_DRAFT.md",
        "spec/AGNIR_MIGRATION_DRAFT.md",
        "spec/CORE.md",
        "spec/BOOTSTRAP.md",
        "spec/MANIFEST.md",
        "profiles/REPOSITORY_FILESYSTEM_DRAFT.md",
        "profiles/generic.md",
        ".chatgpt",
        ".github/workflows/site-ci.yml",
        "目录树.md",
    ]
    for path in forbidden:
        if (ROOT / path).exists():
            fail(f"predecessor or execution-surface-specific artifact remains active on main: {path}")

    print(
        f"PASS: Agnir Skill + Core {snapshot.version} / {snapshot.profile} repository release {repository_version} "
        f"for {snapshot.project_identity}; transactional checkpoint, compatible upgrade, and repository commit-intent boundaries enforced"
    )


if __name__ == "__main__":
    main()
