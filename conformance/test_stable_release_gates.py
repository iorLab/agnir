from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


@unittest.skipUnless(VERSION == "0.2.0", "v0.2.0 stable package gate applies only to the v0.2.0 source tree")
class StableZeroTwoReleaseGateTests(unittest.TestCase):
    def test_repository_package_is_stable_0_2_0(self) -> None:
        self.assertEqual(VERSION, "0.2.0")
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
        self.assertIn("Stable normative profile", profile)

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


@unittest.skipUnless(VERSION == "1.0.0", "v1.0.0 stable package gate applies only to the v1.0.0 source tree")
class StableOneZeroReleaseGateTests(unittest.TestCase):
    def test_repository_package_is_stable_1_0_0(self) -> None:
        self.assertEqual(VERSION, "1.0.0")
        manifest = (ROOT / "AGNIR.yaml").read_text(encoding="utf-8")
        for marker in (
            'version: "1.0"',
            'discovery_profile: "repository-filesystem/1.0"',
            'repository_version: "1.0.0"',
            'branch_continuity: "lineage-bound"',
            'integration_reconciliation: "required"',
        ):
            self.assertIn(marker, manifest)
        bindings = (
            ('lineage: "urn:agnir:lineage:v1.0.0"', 'selector: "refs/heads/release/v1.0.0"'),
            ('lineage: "urn:agnir:lineage:authoritative"', 'selector: "refs/heads/main"'),
        )
        self.assertTrue(any(lineage in manifest and selector in manifest for lineage, selector in bindings))
        self.assertNotIn('repository_version: "1.0.0-rc.1"', manifest)

    def test_core_profile_and_promotion_are_stable_normative_contracts(self) -> None:
        core = (ROOT / "spec/AGNIR_CORE_1_0.md").read_text(encoding="utf-8")
        profile = (ROOT / "profiles/REPOSITORY_FILESYSTEM_1_0.md").read_text(encoding="utf-8")
        promotion = (ROOT / "spec/CORE_0_2_TO_1_0_PROMOTION.md").read_text(encoding="utf-8")
        self.assertIn("Stable normative compatibility contract", core)
        self.assertIn("Stable normative profile", profile)
        self.assertIn("Stable normative promotion contract", promotion)
        self.assertNotIn("Candidate stable compatibility contract", core)
        self.assertNotIn("Candidate stable normative profile", profile)
        self.assertNotIn("Candidate normative promotion contract", promotion)

    def test_release_package_records_rc_and_main_only_publication_boundary(self) -> None:
        release = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
        for marker in (
            "# Agnir 1.0.0 Stable Release Package",
            "**Repository version:** `1.0.0`",
            "**Core compatibility line:** `1.0`",
            "repository-filesystem/1.0",
            "Accepted release candidate",
            "v1.0.0-rc.1",
            "latest stable",
            "release: publish v1.0.0 stable",
            "authoritative `main`",
        ):
            self.assertIn(marker, release)

    def test_readmes_expose_stable_1_0_package_without_candidate_wording(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn("Repository stable package: `v1.0.0`", english)
        self.assertIn("Accepted release candidate: `v1.0.0-rc.1`", english)
        self.assertIn("Repository stable package：`v1.0.0`", chinese)
        self.assertIn("已接受 release candidate：`v1.0.0-rc.1`", chinese)
        self.assertNotIn("Promotion candidate in development", english)
        self.assertNotIn("正在开发的 promotion candidate", chinese)

    def test_historical_compatibility_surfaces_remain_present(self) -> None:
        for path in (
            "spec/AGNIR_CORE.md",
            "profiles/REPOSITORY_FILESYSTEM.md",
            "schemas/agnir-manifest.schema.json",
            "spec/AGNIR_CORE_0_2.md",
            "profiles/REPOSITORY_FILESYSTEM_0_2.md",
            "schemas/agnir-manifest-0.2.schema.json",
            "spec/CORE_0_1_TO_0_2_MIGRATION.md",
            "conformance/repository_filesystem_reference.py",
            "conformance/repository_filesystem_0_2_reference.py",
        ):
            self.assertTrue((ROOT / path).exists(), path)

    def test_workflow_has_main_only_stable_publication_gate(self) -> None:
        workflow = (ROOT / ".github/workflows/conformance.yml").read_text(encoding="utf-8")
        for marker in (
            "publish-v1-0-0:",
            "Publish v1.0.0 stable release",
            "github.ref == 'refs/heads/main'",
            "release: publish v1.0.0 stable",
            'accepted_rc="v1.0.0-rc.1"',
            'tag="v1.0.0"',
            "prerelease=false",
            'test "${latest}" = "${tag}"',
        ):
            self.assertIn(marker, workflow)


if __name__ == "__main__":
    unittest.main()
