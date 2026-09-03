from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class StableReleaseGateTests(unittest.TestCase):
    def test_repository_package_is_stable_0_2_0(self) -> None:
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8").strip(), "0.2.0")

        manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        for marker in (
            'version: "0.2"',
            'discovery_profile: "repository-filesystem/0.2"',
            'repository_version: "0.2.0"',
            'continuity:',
            'branch_continuity: "lineage-bound"',
            'integration_reconciliation: "required"',
        ):
            self.assertIn(marker, manifest)
        self.assertNotIn('repository_version: "0.2.0-rc.1"', manifest)

    def test_core_and_profile_are_stable_normative_contracts(self) -> None:
        core = (ROOT / "spec/AGNIR_CORE_0_2.md").read_text(encoding="utf-8")
        profile = (ROOT / "profiles/REPOSITORY_FILESYSTEM_0_2.md").read_text(encoding="utf-8")

        self.assertIn("# Agnir Core 0.2 — Normative Specification", core)
        self.assertIn("Stable normative compatibility contract", core)
        self.assertNotIn("Release Candidate Normative Specification", core)

        self.assertIn("# Agnir Repository/Filesystem Profile 0.2", profile)
        self.assertIn("Stable normative profile", profile)
        self.assertNotIn("— Release Candidate", profile)

    def test_release_and_versioning_describe_stable_semantics(self) -> None:
        release = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
        versioning = (ROOT / "VERSIONING.md").read_text(encoding="utf-8")

        for marker in (
            "# Agnir 0.2.0 Stable Release",
            "**Repository version:** `0.2.0`",
            "**Core compatibility line:** `0.2`",
            "repository-filesystem/0.2",
            "non-prerelease",
            "releases/latest",
            "exact published `v0.1.1` manifest blob",
        ):
            self.assertIn(marker, release)

        self.assertIn("Status: active pre-1.0 versioning policy", versioning)
        self.assertIn("`0.2.0-rc.1` → `0.2.0`", versioning)
        self.assertIn("latest stable", versioning)
        self.assertNotIn("Status: design draft", versioning)

    def test_readmes_expose_stable_core_0_2_without_rc_as_active_line(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        for text in (english, chinese):
            self.assertIn("Core `0.2`", text)
            self.assertIn("repository-filesystem/0.2", text)
            self.assertIn("0.2.0", text)
            self.assertNotIn("repository is preparing `v0.2.0-rc.1`", text)
            self.assertNotIn("仓库正在准备 `v0.2.0-rc.1`", text)
            self.assertNotIn("compatibility candidate exercised by `v0.2.0-rc.1`", text)

    def test_stable_release_branch_binding_is_identity_separate(self) -> None:
        manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        if 'selector: "refs/heads/release/v0.2.0"' in manifest:
            self.assertIn('lineage: "urn:agnir:lineage:v0.2.0"', manifest)
            self.assertNotEqual("urn:agnir:lineage:v0.2.0", "refs/heads/release/v0.2.0")
        elif 'selector: "refs/heads/main"' in manifest:
            self.assertIn('lineage: "urn:agnir:lineage:authoritative"', manifest)
        else:
            self.fail("stable 0.2 package has no recognized authoritative/release selector binding")

    def test_0_1_compatibility_and_migration_surfaces_remain_present(self) -> None:
        for path in (
            "spec/AGNIR_CORE.md",
            "profiles/REPOSITORY_FILESYSTEM.md",
            "schemas/agnir-manifest.schema.json",
            "conformance/repository_filesystem_reference.py",
            "conformance/test_repository_filesystem_failures.py",
            "conformance/test_repository_filesystem_boundaries.py",
            "conformance/test_rc_release_gates.py",
            "spec/CORE_0_1_TO_0_2_MIGRATION.md",
        ):
            self.assertTrue((ROOT / path).exists(), path)


if __name__ == "__main__":
    unittest.main()
