#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from repository_filesystem_reference import (
    CORE_VERSION,
    PROFILE,
    DiscoveryFailure,
    discover_repository_filesystem,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "agnir-manifest.schema.json"
SELF_PROJECT_ID = "urn:agnir:project:agnir-core"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_readme_diagrams(path: str, headings: tuple[str, str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    if text.count("```mermaid") < 2:
        fail(f"{path} must contain at least two Mermaid diagrams")
    for heading in headings:
        if heading not in text:
            fail(f"{path} missing required diagram section: {heading}")


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
        "REPOSITORY_TREE.md",
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
        ".github/",
        "conformance.yml",
        "AGNIR.yaml",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "VERSION",
    ):
        if marker not in text:
            fail(f"REPOSITORY_TREE.md missing required full-tree marker: {marker}")


def main() -> None:
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

    required_active = [
        "README.md",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "spec/AGNIR_CORE.md",
        "spec/AGNIR_DISCOVERY.md",
        "profiles/REPOSITORY_FILESYSTEM.md",
        "history/PREDECESSOR.md",
        "history/MIGRATION_PPMP_V2.md",
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
        f"PASS: Agnir {snapshot.version} repository/filesystem cold-start structure "
        f"for {snapshot.project_identity}"
    )


if __name__ == "__main__":
    main()
