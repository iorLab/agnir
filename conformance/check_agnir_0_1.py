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
        "spec/AGNIR_CORE.md",
        "spec/AGNIR_DISCOVERY.md",
        "spec/MIGRATION_PPMP_V2.md",
        "profiles/REPOSITORY_FILESYSTEM.md",
        "history/PREDECESSOR.md",
        "conformance/core_reference.py",
        "conformance/repository_filesystem_reference.py",
        "conformance/test_repository_filesystem_failures.py",
        "conformance/sqlite_backend_reference.py",
        "conformance/test_sqlite_backend.py",
    ]
    for path in required_active:
        if not (ROOT / path).exists():
            fail(f"missing active Agnir artifact: {path}")

    require_readme_diagrams("README.md", ("## Architecture Diagram", "## Continuity Flow"))
    require_readme_diagrams("README.zh-CN.md", ("## 架构图", "## 连续性流程"))

    forbidden = [
        "docs",
        "adapters",
        "backends",
        "examples",
        "implementations",
        "site",
        "templates",
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
