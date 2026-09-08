#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from activation_reference import ActivationFailure, resolve_agent_activation
from repository_filesystem_1_0_reference import (
    CORE_1_0_VERSION,
    PROFILE_1_0,
    discover_repository_filesystem_1_0,
)


ROOT = Path(__file__).resolve().parents[1]
SELF_PROJECT_ID = "urn:agnir:project:agnir-core"
SCHEMA = ROOT / "schemas" / "agnir-manifest-1.0.schema.json"

BINDINGS = {
    'selector: "refs/heads/main"': (
        "urn:agnir:lineage:authoritative",
        "refs/heads/main",
    ),
    'selector: "refs/heads/release/v1.0.0-rc.1"': (
        "urn:agnir:lineage:v1.0.0-rc.1",
        "refs/heads/release/v1.0.0-rc.1",
    ),
    'selector: "refs/heads/release/v1.0.0"': (
        "urn:agnir:lineage:v1.0.0",
        "refs/heads/release/v1.0.0",
    ),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def resolve_expected_binding(manifest: str) -> tuple[str, str]:
    matches = [value for marker, value in BINDINGS.items() if marker in manifest]
    if len(matches) != 1:
        fail("Core 1.0 Agnir self-host must expose exactly one recognized selector binding")
    return matches[0]


def require_1_0_contracts() -> None:
    core = (ROOT / "spec" / "AGNIR_CORE_1_0.md").read_text(encoding="utf-8")
    for marker in (
        "# Agnir Core 1.0",
        "stability promotion",
        "Core `0.2`",
        "Continuity Lineage",
        "AGNIR_LINEAGE_REQUIRED",
        "coherent target publication",
    ):
        if marker not in core:
            fail(f"Core 1.0 contract missing marker: {marker}")

    profile = (ROOT / "profiles" / "REPOSITORY_FILESYSTEM_1_0.md").read_text(encoding="utf-8")
    for marker in (
        "repository-filesystem/1.0",
        "Core `1.0`",
        "agnir-manifest-1.0.schema.json",
        "repository-filesystem/0.2",
        "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
        "AGNIR_DISCOVERY_INCONSISTENT",
    ):
        if marker not in profile:
            fail(f"repository-filesystem/1.0 profile missing marker: {marker}")

    promotion = (ROOT / "spec" / "CORE_0_2_TO_1_0_PROMOTION.md").read_text(encoding="utf-8")
    for marker in (
        "AGNIR_UPGRADE_MIGRATION_REQUIRED",
        "AGNIR_MIGRATION_CONFLICT",
        "Project identity",
        "logical lineage identity",
        "fresh",
        "no-op",
    ):
        if marker not in promotion:
            fail(f"0.2 -> 1.0 promotion contract missing marker: {marker}")


def require_1_0_distribution_surface() -> None:
    for path in (
        "SKILL.md",
        "AGENTS.md",
        "AGNIR.md",
        "AGNIR.yaml",
        "README.md",
        "README.zh-CN.md",
        "REPOSITORY_TREE.md",
        "RELEASE.md",
        "VERSIONING.md",
        "conformance/activation_reference.py",
        "conformance/agents_merge_reference.py",
        "conformance/operation_dispatch_reference.py",
        "conformance/test_agent_activation.py",
        "conformance/test_agents_merge.py",
        "conformance/test_operation_dispatch.py",
    ):
        if not (ROOT / path).exists():
            fail(f"missing 1.0.x distribution surface: {path}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for marker in (
        "## Install or initialize Agnir",
        "canonical Executor-facing Project activation and operation surface",
        "backward-compatible locator only",
        "Agnir `1.0.1` is an activation/packaging reliability patch over `1.0.0`",
        "checkpoint evaluation",
        "Project-defined pre-commit policy when declared",
        "Do not execute an isolated Git commit path",
        "## Repair",
    ):
        if marker not in skill:
            fail(f"SKILL.md missing 1.0.x activation-hardening marker: {marker}")

    instructions = (ROOT / "AGNIR.md").read_text(encoding="utf-8")
    for marker in (
        "# Agnir Project Instructions",
        "Project Entry Point",
        "AGNIR.yaml",
        "Current State",
        "Next Actions",
        "Decisions",
        "Evidence",
        "checkpoint evaluation",
        "AGNIR_CHECKPOINT_CONFLICT",
        "提交",
        "Project-defined pre-commit policy",
        "A legitimate checkpoint no-op does not require an `.agnir/` diff",
    ):
        if marker not in instructions:
            fail(f"AGNIR.md missing activation/operation marker: {marker}")

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if "AGNIR.md" not in agents or "Current State" in agents or "Next Actions" in agents:
        fail("AGENTS.md must remain a minimal locator to AGNIR.md")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    heading = "## Agnir Project Instructions"
    if heading not in readme:
        fail("README.md missing backward-compatible Agnir Project Instructions heading")
    section = readme.split(heading, 1)[1].split("\n## ", 1)[0]
    if "AGNIR.md" not in section or "backward-compatible locator" not in section:
        fail("README activation compatibility section must point to AGNIR.md")
    for forbidden in ("Current State", "Next Actions", "AGNIR_CHECKPOINT_CONFLICT"):
        if forbidden in section:
            fail("README compatibility locator must not fork AGNIR.md procedure")

    tree = (ROOT / "REPOSITORY_TREE.md").read_text(encoding="utf-8")
    for marker in ("AGNIR.md", "operation_dispatch_reference.py", "test_operation_dispatch.py"):
        if marker not in tree:
            fail(f"REPOSITORY_TREE.md missing v1.0.1 surface marker: {marker}")


def require_public_entry_surfaces() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
    for text, markers in (
        (
            english,
            (
                "## Start Here",
                "Install and initialize Agnir for this Project: https://github.com/iorLab/agnir",
                "Upgrade Agnir to the latest stable release: https://github.com/iorLab/agnir",
                "No recurring Agnir prompt is required.",
                "Project root\n→ AGENTS.md\n→ AGNIR.md\n→ AGNIR.yaml",
                "## What Agnir Adds to a Project",
                "## Architecture Diagram",
                "## Continuity Flow",
            ),
        ),
        (
            chinese,
            (
                "## 从这里开始",
                "为这个项目安装并初始化 Agnir：https://github.com/iorLab/agnir",
                "把这个项目的 Agnir 升级到最新稳定版：https://github.com/iorLab/agnir",
                "项目根目录\n→ AGENTS.md\n→ AGNIR.md\n→ AGNIR.yaml",
                "## Agnir 会给项目增加什么",
                "## 架构图",
                "## 连续性流程",
            ),
        ),
    ):
        for marker in markers:
            if marker not in text:
                fail(f"public README surface missing marker: {marker}")


def main() -> None:
    require_1_0_contracts()
    require_1_0_distribution_surface()
    require_public_entry_surfaces()

    try:
        activation = resolve_agent_activation(ROOT)
    except ActivationFailure as exc:
        fail(str(exc))
    if activation.route != "agnir-md":
        fail("1.0.x self-host must use direct AGNIR.md activation")
    if activation.instructions_path.name != "AGNIR.md":
        fail("1.0.x self-host did not resolve AGNIR.md as canonical Project instructions")
    if "AGNIR.yaml" not in activation.instructions:
        fail("1.0.x self-host activation did not resolve AGNIR.yaml")

    manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    expected_lineage, expected_selector = resolve_expected_binding(manifest)

    snapshot = discover_repository_filesystem_1_0(
        ROOT,
        expected_project_identity=SELF_PROJECT_ID,
        expected_lineage_identity=expected_lineage,
    )
    if snapshot.version != CORE_1_0_VERSION or snapshot.profile != PROFILE_1_0:
        fail("Agnir self-host did not resolve exact Core/profile 1.0")
    if "Durable continuity belongs to the Project" not in snapshot.state:
        fail("Core 1.0 cold start did not recover the durable ownership invariant")

    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Core 1.0 manifest schema is not valid JSON: {exc}")
    version_const = schema["properties"]["agnir"]["properties"]["version"]["const"]
    profile_const = schema["properties"]["agnir"]["properties"]["discovery_profile"]["const"]
    if version_const != CORE_1_0_VERSION or profile_const != PROFILE_1_0:
        fail("Core/profile 1.0 schema constants diverge")

    for marker in (
        'version: "1.0"',
        'discovery_profile: "repository-filesystem/1.0"',
        f'lineage: "{expected_lineage}"',
        'branch_continuity: "lineage-bound"',
        f'selector: "{expected_selector}"',
    ):
        if marker not in manifest:
            fail(f"Core 1.0 AGNIR.yaml missing required marker: {marker}")
    if expected_lineage == expected_selector:
        fail("logical lineage identity must not be inferred from the selector")

    repository_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if repository_version not in {"1.0.0-rc.1", "1.0.0", "1.0.1"}:
        fail(f"unexpected Core 1.0 repository version: {repository_version}")
    if f'repository_version: "{repository_version}"' not in manifest:
        fail(f"AGNIR.yaml does not declare repository_version {repository_version}")

    release = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
    for marker in (
        "Core compatibility line",
        "1.0",
        "repository-filesystem/1.0",
        "SKILL.md",
        "latest stable",
    ):
        if marker not in release:
            fail(f"RELEASE.md missing Core 1.0 release marker: {marker}")

    for path in (
        "spec/AGNIR_CORE.md",
        "profiles/REPOSITORY_FILESYSTEM.md",
        "schemas/agnir-manifest.schema.json",
        "spec/AGNIR_CORE_0_2.md",
        "profiles/REPOSITORY_FILESYSTEM_0_2.md",
        "schemas/agnir-manifest-0.2.schema.json",
        "spec/CORE_0_1_TO_0_2_MIGRATION.md",
        "spec/CORE_0_2_TO_1_0_PROMOTION.md",
    ):
        if not (ROOT / path).exists():
            fail(f"Core/profile 1.0 source removed supported compatibility artifact: {path}")

    print(
        f"PASS: Agnir Core {snapshot.version} / {snapshot.profile} self-host "
        f"via {activation.route}; lineage {snapshot.lineage_identity} selector {expected_selector} "
        f"repository {repository_version}"
    )


if __name__ == "__main__":
    main()
