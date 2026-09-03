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
from repository_filesystem_0_2_reference import (
    CORE_0_2_VERSION,
    PROFILE_0_2,
    discover_repository_filesystem_0_2,
)

ROOT = Path(__file__).resolve().parents[1]
SELF_PROJECT_ID = "urn:agnir:project:agnir-core"
SCHEMA = ROOT / "schemas" / "agnir-manifest-0.2.schema.json"

BINDINGS = {
    'selector: "refs/heads/main"': (
        "urn:agnir:lineage:authoritative",
        "refs/heads/main",
    ),
    'selector: "refs/heads/release/v0.2.0"': (
        "urn:agnir:lineage:v0.2.0",
        "refs/heads/release/v0.2.0",
    ),
    'selector: "refs/heads/release/v0.2.0-rc.1"': (
        "urn:agnir:lineage:v0.2.0-rc.1",
        "refs/heads/release/v0.2.0-rc.1",
    ),
}


def resolve_expected_binding(manifest: str) -> tuple[str, str]:
    matches = [value for marker, value in BINDINGS.items() if marker in manifest]
    if len(matches) != 1:
        fail("Core 0.2 Agnir self-host must expose exactly one recognized selector binding")
    return matches[0]


def require_stable_contracts() -> None:
    core02 = (ROOT / "spec" / "AGNIR_CORE_0_2.md").read_text(encoding="utf-8")
    for marker in (
        "# Agnir Core 0.2 — Normative Specification",
        "Stable normative compatibility contract",
        "Continuity Lineage",
        "AGNIR_LINEAGE_REQUIRED",
        "coherent target publication",
        "Stable Core `0.2` acceptance",
        "CORE_0_1_TO_0_2_MIGRATION.md",
    ):
        if marker not in core02:
            fail(f"stable Core 0.2 contract missing marker: {marker}")
    if "Release Candidate Normative Specification" in core02:
        fail("stable Core 0.2 contract still claims Release Candidate status")

    profile02 = (ROOT / "profiles" / "REPOSITORY_FILESYSTEM_0_2.md").read_text(encoding="utf-8")
    for marker in (
        "# Agnir Repository/Filesystem Profile 0.2",
        "repository-filesystem/0.2",
        "Stable normative profile",
        "logical lineage identity",
        "lineage_binding.selector",
        "Stable `repository-filesystem/0.2` conformance",
        "Core `0.1` migration",
    ):
        if marker not in profile02:
            fail(f"stable repository-filesystem/0.2 profile missing marker: {marker}")
    if "— Release Candidate" in profile02:
        fail("stable repository-filesystem/0.2 profile still claims Release Candidate status")


def require_rc_contracts() -> None:
    core02 = (ROOT / "spec" / "AGNIR_CORE_0_2.md").read_text(encoding="utf-8")
    if "Release Candidate Normative Specification" not in core02:
        fail("RC repository version requires the RC Core 0.2 contract")
    profile02 = (ROOT / "profiles" / "REPOSITORY_FILESYSTEM_0_2.md").read_text(encoding="utf-8")
    if "— Release Candidate" not in profile02:
        fail("RC repository version requires the RC profile contract")


def main() -> None:
    require_skill_package()

    try:
        activation = resolve_agent_activation(ROOT)
    except ActivationFailure as exc:
        fail(str(exc))
    if "AGNIR.yaml" not in activation.readme_section:
        fail("Core 0.2 self-host activation did not resolve AGNIR.yaml")

    manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
    expected_lineage, expected_selector = resolve_expected_binding(manifest)

    snapshot = discover_repository_filesystem_0_2(
        ROOT,
        expected_project_identity=SELF_PROJECT_ID,
        expected_lineage_identity=expected_lineage,
    )
    if snapshot.version != CORE_0_2_VERSION or snapshot.profile != PROFILE_0_2:
        fail("Agnir self-host did not resolve Core/profile 0.2")
    if "Durable continuity belongs to the Project" not in snapshot.state:
        fail("Core 0.2 cold start did not recover the durable ownership invariant")

    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Core 0.2 manifest schema is not valid JSON: {exc}")
    version_const = schema["properties"]["agnir"]["properties"]["version"]["const"]
    profile_const = schema["properties"]["agnir"]["properties"]["discovery_profile"]["const"]
    if version_const != CORE_0_2_VERSION or profile_const != PROFILE_0_2:
        fail("Core/profile 0.2 schema constants diverge")

    for marker in (
        'version: "0.2"',
        'discovery_profile: "repository-filesystem/0.2"',
        f'lineage: "{expected_lineage}"',
        'branch_continuity: "lineage-bound"',
        f'selector: "{expected_selector}"',
    ):
        if marker not in manifest:
            fail(f"Core 0.2 AGNIR.yaml missing required marker: {marker}")
    if expected_lineage == expected_selector:
        fail("logical lineage identity must not be inferred from the selector")

    repository_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if repository_version == "0.2.0":
        require_stable_contracts()
        if 'repository_version: "0.2.0"' not in manifest:
            fail("stable AGNIR.yaml does not declare repository_version 0.2.0")
    elif repository_version == "0.2.0-rc.1":
        require_rc_contracts()
    else:
        fail(f"unexpected Core 0.2 repository version: {repository_version}")

    release = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
    for marker in (
        repository_version,
        "Core compatibility line:** `0.2`",
        "repository-filesystem/0.2",
        "SKILL.md",
        "migration",
        "latest stable",
    ):
        if marker not in release:
            fail(f"RELEASE.md missing Core 0.2 release marker: {marker}")

    for path in (
        "spec/AGNIR_CORE.md",
        "profiles/REPOSITORY_FILESYSTEM.md",
        "schemas/agnir-manifest.schema.json",
        "conformance/repository_filesystem_reference.py",
        "conformance/agnir-0.1.md",
    ):
        if not (ROOT / path).exists():
            fail(f"Core/profile 0.2 source removed stable Core/profile 0.1 compatibility artifact: {path}")

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
