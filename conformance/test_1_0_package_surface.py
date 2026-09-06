from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


class OneZeroPackageSurfaceTests(unittest.TestCase):
    def test_public_1_0_contract_surfaces_exist(self) -> None:
        for path in (
            "spec/AGNIR_CORE_1_0.md",
            "profiles/REPOSITORY_FILESYSTEM_1_0.md",
            "schemas/agnir-manifest-1.0.schema.json",
            "spec/CORE_0_2_TO_1_0_PROMOTION.md",
            "conformance/core_1_0_reference.py",
            "conformance/repository_filesystem_1_0_reference.py",
            "conformance/repository_filesystem_1_0_promotion_reference.py",
            "conformance/check_agnir_1_0.py",
            "conformance/test_core_1_0_stability.py",
            "conformance/test_repository_filesystem_1_0.py",
            "conformance/test_repository_filesystem_1_0_promotion.py",
        ):
            self.assertTrue((ROOT / path).exists(), path)

    def test_readmes_explain_release_status_and_non_forced_promotion(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        for marker in (
            "Core `1.0`",
            "repository-filesystem/1.0",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "Existing Core/profile `0.1` and `0.2` Projects remain supported",
        ):
            self.assertIn(marker, english)
        for marker in (
            "Core `1.0`",
            "repository-filesystem/1.0",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "已有 Core/profile `0.1` 与 `0.2` Project 继续受支持",
        ):
            self.assertIn(marker, chinese)

        if VERSION == "1.0.0":
            self.assertIn("Repository stable package: `v1.0.0`", english)
            self.assertIn("Accepted release candidate: `v1.0.0-rc.1`", english)
            self.assertIn("Repository stable package：`v1.0.0`", chinese)
            self.assertIn("已接受 release candidate：`v1.0.0-rc.1`", chinese)
            self.assertNotIn("Promotion candidate in development", english)
            self.assertNotIn("正在开发的 promotion candidate", chinese)
        else:
            self.assertIn("`v0.2.0`", english)
            self.assertIn("1.0.0-rc", english)
            self.assertIn("`v0.2.0`", chinese)
            self.assertIn("1.0.0-rc", chinese)

    def test_skill_dispatches_0_1_0_2_and_1_0_without_silent_relabeling(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for marker in (
            "Core/profile `0.1`",
            "Core/profile `0.2`",
            "Core/profile `1.0`",
            "spec/CORE_0_2_TO_1_0_PROMOTION.md",
            "does not authorize silently interpreting or rewriting a valid `0.2` Project as `1.0`",
            "Existing supported `0.2` Projects may remain on `0.2`",
            "AGNIR_MIGRATION_CONFLICT",
        ):
            self.assertIn(marker, skill)

    def test_versioning_and_repository_map_keep_release_axes_distinct(self) -> None:
        versioning = (ROOT / "VERSIONING.md").read_text(encoding="utf-8")
        milestones = (ROOT / "RELEASE_MILESTONES.md").read_text(encoding="utf-8")
        tree = (ROOT / "REPOSITORY_TREE.md").read_text(encoding="utf-8")

        for marker in (
            "Agnir repository v1.0.0",
            "Core 1.0",
            "repository-filesystem/1.0",
            "v1.0.0-rc.1",
        ):
            self.assertIn(marker, versioning)
        self.assertIn("Core `1.0` + `repository-filesystem/1.0`", milestones)
        self.assertIn("v1.0.0-rc.1", milestones)

        for marker in (
            "AGNIR_CORE_1_0.md",
            "REPOSITORY_FILESYSTEM_1_0.md",
            "agnir-manifest-1.0.schema.json",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "check_agnir_1_0.py",
            "repository_filesystem_1_0_reference.py",
            "repository_filesystem_1_0_promotion_reference.py",
            "test_1_0_package_surface.py",
            "test_repository_filesystem_1_0_promotion.py",
            "当前 stable distribution source package",
        ):
            self.assertIn(marker, tree)

    def test_source_tree_version_matches_its_self_host_compatibility(self) -> None:
        manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        self.assertIn(VERSION, {"0.2.0", "1.0.0-rc.1", "1.0.0"})
        if VERSION == "0.2.0":
            self.assertIn('version: "0.2"', manifest)
            self.assertIn('discovery_profile: "repository-filesystem/0.2"', manifest)
            self.assertIn('repository_version: "0.2.0"', manifest)
            self.assertNotIn('repository_version: "1.0.0-rc.1"', manifest)
        elif VERSION == "1.0.0-rc.1":
            self.assertIn('version: "1.0"', manifest)
            self.assertIn('discovery_profile: "repository-filesystem/1.0"', manifest)
            self.assertIn('repository_version: "1.0.0-rc.1"', manifest)
            self.assertIn('lineage: "urn:agnir:lineage:v1.0.0-rc.1"', manifest)
            self.assertIn('selector: "refs/heads/release/v1.0.0-rc.1"', manifest)
        else:
            self.assertIn('version: "1.0"', manifest)
            self.assertIn('discovery_profile: "repository-filesystem/1.0"', manifest)
            self.assertIn('repository_version: "1.0.0"', manifest)
            self.assertTrue(
                'selector: "refs/heads/release/v1.0.0"' in manifest
                or 'selector: "refs/heads/main"' in manifest
            )

    def test_v1_rc_publication_is_exact_source_and_dormant_until_arm_commit(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text(encoding="utf-8")
        for marker in (
            "publish-v1-0-0-rc-1:",
            "Publish v1.0.0-rc.1 prerelease",
            "refs/heads/release/v1.0.0-rc.1",
            "rc: arm v1.0.0-rc.1 publication",
            'test "$(cat VERSION)" = "1.0.0-rc.1"',
            "python conformance/check_agnir_1_0.py",
            'tag="v1.0.0-rc.1"',
            "prerelease=true",
        ):
            self.assertIn(marker, workflow)

    def test_v1_stable_publication_is_main_only_and_dormant_until_arm_commit(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text(encoding="utf-8")
        for marker in (
            "publish-v1-0-0:",
            "Publish v1.0.0 stable release",
            "github.ref == 'refs/heads/main'",
            "release: publish v1.0.0 stable",
            'test "$(cat VERSION)" = "1.0.0"',
            'tag="v1.0.0"',
            "prerelease=false",
            'test "${latest}" = "${tag}"',
            'accepted_rc="v1.0.0-rc.1"',
        ):
            self.assertIn(marker, workflow)

    def test_self_host_ci_dispatches_by_repository_version(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "conformance.yml").read_text(encoding="utf-8")
        for marker in (
            "Repository self-host cold-start",
            "0.2.0|0.2.0-rc.1",
            "python conformance/check_agnir_0_2.py",
            "1.0.0|1.0.0-rc.1",
            "python conformance/check_agnir_1_0.py",
        ):
            self.assertIn(marker, workflow)


if __name__ == "__main__":
    unittest.main()
