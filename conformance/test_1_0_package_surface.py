from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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
            "conformance/test_core_1_0_stability.py",
            "conformance/test_repository_filesystem_1_0.py",
            "conformance/test_repository_filesystem_1_0_promotion.py",
        ):
            self.assertTrue((ROOT / path).exists(), path)

    def test_readmes_explain_candidate_status_and_non_forced_promotion(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        for marker in (
            "`v0.2.0` is currently the latest published stable release",
            "Core/profile `1.0`",
            "repository-filesystem/1.0",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "Existing Core/profile `0.2` Projects remain supported",
            "not permission to rewrite the Project compatibility identifiers",
            "1.0.0-rc",
        ):
            self.assertIn(marker, english)

        for marker in (
            "`v0.2.0` 目前仍是最新已发布稳定版",
            "Core/profile `1.0`",
            "repository-filesystem/1.0",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "已有 Core/profile `0.2` Project 继续受支持",
            "不等于授权改写 Project compatibility identifier",
            "1.0.0-rc",
        ):
            self.assertIn(marker, chinese)

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

    def test_versioning_and_repository_map_keep_published_vs_candidate_distinct(self) -> None:
        versioning = (ROOT / "VERSIONING.md").read_text(encoding="utf-8")
        milestones = (ROOT / "RELEASE_MILESTONES.md").read_text(encoding="utf-8")
        tree = (ROOT / "REPOSITORY_TREE.md").read_text(encoding="utf-8")

        self.assertIn("`v0.2.0` remains the latest stable release", versioning)
        self.assertIn("Agnir repository v1.0.0", versioning)
        self.assertIn("Core 1.0", versioning)
        self.assertIn("repository-filesystem/1.0", versioning)
        self.assertIn("`v0.2.0` remains the latest published stable release", milestones)

        for marker in (
            "AGNIR_CORE_1_0.md",
            "REPOSITORY_FILESYSTEM_1_0.md",
            "agnir-manifest-1.0.schema.json",
            "CORE_0_2_TO_1_0_PROMOTION.md",
            "repository_filesystem_1_0_reference.py",
            "repository_filesystem_1_0_promotion_reference.py",
            "test_repository_filesystem_1_0_promotion.py",
            "当前已发布 stable distribution",
        ):
            self.assertIn(marker, tree)

    def test_promotion_candidate_does_not_pretend_repository_release_is_1_0(self) -> None:
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8").strip(), "0.2.0")
        manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        self.assertIn('version: "0.2"', manifest)
        self.assertIn('discovery_profile: "repository-filesystem/0.2"', manifest)
        self.assertIn('repository_version: "0.2.0"', manifest)


if __name__ == "__main__":
    unittest.main()
