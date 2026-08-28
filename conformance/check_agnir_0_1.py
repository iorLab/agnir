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


def require_readme_quick_start(
    path: str,
    *,
    quick_start_heading: str,
    architecture_heading: str,
    existing_marker: str,
    init_marker: str,
) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for marker in (
        quick_start_heading,
        existing_marker,
        init_marker,
        "AGENTS.md",
        "README.md",
        "Agnir Project Instructions",
        "Project Entry Point",
        "AGNIR.yaml",
        "repository-filesystem/0.1",
        ".agnir/state.md",
        ".agnir/next-actions.md",
        ".agnir/decisions.md",
        ".agnir/evidence/",
        "checkpoint",
    ):
        if marker not in text:
            fail(f"{path} missing required operational quick-start marker: {marker}")

    quick_start_position = text.find(quick_start_heading)
    architecture_position = text.find(architecture_heading)
    if quick_start_position < 0 or architecture_position < 0 or quick_start_position > architecture_position:
        fail(f"{path} must present the operational Quick Start before architecture material")


def require_readme_diagrams(path: str, headings: tuple[str, str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if text.count("```mermaid") < 2:
        fail(f"{path} must contain at least two Mermaid diagrams")
    for heading in headings:
        if heading not in text:
            fail(f"{path} missing required diagram section: {heading}")
    for marker in ("AGENTS.md", "README", "AGNIR.yaml"):
        if marker not in text:
            fail(f"{path} diagrams/explanation missing activation-path marker: {marker}")


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
        "AGENTS.md",
        "activation_reference.py",
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
        "test_agent_activation.py",
        "repository_filesystem_reference.py",
        "external_memory_reference.py",
        "locator_chain_reference.py",
        "sqlite_backend_reference.py",
        "workspace_registry_reference.py",
        "test_repository_filesystem_boundaries.py",
        "test_external_memory_authorization.py",
        "test_workspace_isolation.py",
        ".agnir/",
        "2026-08-28-negative-discovery-fixtures.md",
        "history/",
        "PREDECESSOR.md",
        "MIGRATION_PPMP_V2.md",
        "BRANCH_ARCHIVE.md",
        ".github/",
        "conformance.yml",
        "AGENTS.md",
        "AGNIR.yaml",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "RELEASE.md",
        "VERSION",
    ):
        if marker not in text:
            fail(f"REPOSITORY_TREE.md missing required full-tree marker: {marker}")


def main() -> None:
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

    profile_text = (ROOT / "profiles" / "REPOSITORY_FILESYSTEM.md").read_text(encoding="utf-8")
    if ".chatgpt/project-memory.yaml" in profile_text:
        fail("active repository/filesystem profile must not define predecessor bootstrap fallback")
    for marker in (
        "Agent-operable Project activation and initialization",
        "AGENTS.md",
        "Agnir Project Instructions",
        "fresh activation test",
        "SHOULD NOT need to repeat an Agnir bootstrap prompt",
    ):
        if marker not in profile_text:
            fail(f"repository/filesystem profile missing activation contract marker: {marker}")

    release_text = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
    for marker in (
        REPOSITORY_VERSION,
        'Core compatibility line:** `0.1`',
        'repository-filesystem/0.1',
        'AGENTS.md',
        'Agnir Project Instructions',
    ):
        if marker not in release_text:
            fail(f"RELEASE.md missing release marker: {marker}")

    required_active = [
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
        "conformance/test_agent_activation.py",
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
        existing_marker="No recurring Agnir prompt is required.",
        init_marker="The initialization request must be self-contained",
    )
    require_readme_quick_start(
        "README.zh-CN.md",
        quick_start_heading="## 30 秒快速开始",
        architecture_heading="## 架构图",
        existing_marker="不需要每次再给 Agent 一段 Agnir 提示词。",
        init_marker="初始化提示词必须是**自包含**的",
    )
    require_readme_diagrams("README.md", ("## Architecture Diagram", "## Continuity Flow"))
    require_readme_diagrams("README.zh-CN.md", ("## 架构图", "## 连续性流程"))
    require_readme_repository_tree("README.md", "## Repository Structure")
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
        f"PASS: Agnir {snapshot.version} / {snapshot.profile} repository release {repository_version} "
        f"for {snapshot.project_identity}; durable Agent activation resolved"
    )


if __name__ == "__main__":
    main()
