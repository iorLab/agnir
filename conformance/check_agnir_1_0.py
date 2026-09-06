#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from activation_reference import ActivationFailure, resolve_agent_activation
from check_agnir_0_1 import (
    fail,
    require_full_repository_tree,
    require_readme_diagrams,
    require_readme_entry_guide,
    require_readme_repository_tree,
    require_skill_package,
)
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
        "logical Continuity Lineage identity",
        "fresh",
        "no-op",
    ):
        if marker not in promotion:
            fail(f"0.2 -> 1.0 promotion contract missing marker: {marker}")


def main() -> None:
    require_skill_package()
    require_1_0_contracts()

    try:
        activation = resolve_agent_activation(ROOT)
    except ActivationFailure as exc:
        fail(str(exc))
    if "AGNIR.yaml" not in activation.readme_section:
        fail("Core 1.0 self-host activation did not resolve AGNIR.yaml")

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
    if repository_version not in {"1.0.0-rc.1", "1.0.0"}:
        fail(f"unexpected Core 1.0 repository version: {repository_version}")
    if f'repository_version: "{repository_version}"' not in manifest:
        fail(f"AGNIR.yaml does not declare repository_version {repository_version}")

    release = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
    for marker in (
        repository_version,
        "Core",
        "1.0",
        "repository-filesystem/1.0",
        "SKILL.md",
        "promotion",
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

    require_readme_entry_guide(
        "README.md",
        start_heading="## Start Here",
        surface_heading="## What Agnir Adds to a Project",
        architecture_heading="## Architecture Diagram",
        install_prompt="Install and initialize Agnir for this Project: https://github.com/iorLab/agnir",
        upgrade_prompt="Upgrade Agnir to the latest stable release: https://github.com/iorLab/agnir",
        existing_marker="No recurring Agnir prompt is required.",
        forbidden_checklist="Requirements:\n1.",
    )
    require_readme_entry_guide(
        "README.zh-CN.md",
        start_heading="## 从这里开始",
        surface_heading="## Agnir 会给 Project 增加什么",
        architecture_heading="## 架构图",
        install_prompt="为这个 Project 安装并初始化 Agnir：https://github.com/iorLab/agnir",
        upgrade_prompt="把这个 Project 的 Agnir 升级到最新稳定版：https://github.com/iorLab/agnir",
        existing_marker="不需要再给 Agent 任何 Agnir bootstrap 提示词。",
        forbidden_checklist="要求：\n1.",
    )
    require_readme_diagrams(
        "README.md",
        ("## Architecture Diagram", "## Continuity Flow"),
        architecture_markers=(
            "non-destructive setup",
            "EDIT: add activation locator only",
            "EDIT: add Agnir instructions only",
            "ADD: discovery anchor",
            "ADD: durable continuity",
        ),
        flow_forbidden_markers=("EDIT: add", "ADD: discovery", "ADD: durable"),
    )
    require_readme_diagrams(
        "README.zh-CN.md",
        ("## 架构图", "## 连续性流程"),
        architecture_markers=(
            "非破坏性 setup",
            "编辑：仅添加 activation locator",
            "编辑：仅添加 Agnir instructions",
            "新增：discovery anchor",
            "新增：durable continuity",
        ),
        flow_forbidden_markers=("编辑：仅添加", "新增：discovery", "新增：durable"),
    )
    require_readme_repository_tree("README.md", "## Repository structure")
    require_readme_repository_tree("README.zh-CN.md", "## 仓库结构")
    require_full_repository_tree()

    print(
        f"PASS: Agnir Core {snapshot.version} / {snapshot.profile} self-host "
        f"lineage {snapshot.lineage_identity} selector {expected_selector} repository {repository_version}"
    )


if __name__ == "__main__":
    main()
