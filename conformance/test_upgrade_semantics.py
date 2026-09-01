from __future__ import annotations

import unittest

from upgrade_reference import (
    OperationalTarget,
    UpgradeMigrationRequired,
    UpgradeTargetRejected,
    apply_compatible_upgrade,
    classify_upgrade,
)


BASE_MANIFEST = {
    "agnir": {
        "version": "0.1",
        "discovery_profile": "repository-filesystem/0.1",
    },
    "project": {"identity": "urn:example:project:alpha"},
    "memory": {
        "state": ".agnir/state.md",
        "next_actions": ".agnir/next-actions.md",
        "decisions": ".agnir/decisions.md",
        "evidence": ".agnir/evidence/",
    },
    "extensions": {
        "example/custom": {"preserve": True},
    },
}

STABLE_TARGET = OperationalTarget(
    core_version="0.1",
    discovery_profile="repository-filesystem/0.1",
    distribution="agnir-agent-skill",
    release="0.1.0",
    source="iorLab/agnir",
    revision="0123456789abcdef",
    stable=True,
)


class UpgradeSemanticsTests(unittest.TestCase):
    def test_legacy_project_without_operations_provenance_is_compatible(self) -> None:
        self.assertEqual(classify_upgrade(BASE_MANIFEST, STABLE_TARGET), "compatible-upgrade")

    def test_compatible_upgrade_preserves_project_and_memory(self) -> None:
        upgraded, changed = apply_compatible_upgrade(BASE_MANIFEST, STABLE_TARGET)
        self.assertTrue(changed)
        self.assertEqual(upgraded["project"], BASE_MANIFEST["project"])
        self.assertEqual(upgraded["memory"], BASE_MANIFEST["memory"])
        self.assertEqual(upgraded["agnir"], BASE_MANIFEST["agnir"])
        self.assertEqual(upgraded["extensions"]["example/custom"], {"preserve": True})
        self.assertEqual(
            upgraded["extensions"]["agnir/operations"],
            {
                "distribution": "agnir-agent-skill",
                "release": "0.1.0",
                "source": "iorLab/agnir",
                "applied_revision": "0123456789abcdef",
            },
        )

    def test_same_operational_baseline_is_no_op(self) -> None:
        once, changed = apply_compatible_upgrade(BASE_MANIFEST, STABLE_TARGET)
        self.assertTrue(changed)
        twice, changed_again = apply_compatible_upgrade(once, STABLE_TARGET)
        self.assertFalse(changed_again)
        self.assertEqual(twice, once)

    def test_unstable_target_requires_explicit_opt_in(self) -> None:
        unstable = OperationalTarget(**{**STABLE_TARGET.__dict__, "stable": False})
        with self.assertRaises(UpgradeTargetRejected):
            classify_upgrade(BASE_MANIFEST, unstable)
        self.assertEqual(
            classify_upgrade(BASE_MANIFEST, unstable, allow_unstable=True),
            "compatible-upgrade",
        )

    def test_core_change_requires_migration(self) -> None:
        target = OperationalTarget(**{**STABLE_TARGET.__dict__, "core_version": "0.2"})
        with self.assertRaises(UpgradeMigrationRequired):
            classify_upgrade(BASE_MANIFEST, target)

    def test_profile_change_requires_migration(self) -> None:
        target = OperationalTarget(
            **{**STABLE_TARGET.__dict__, "discovery_profile": "repository-filesystem/0.2"}
        )
        with self.assertRaises(UpgradeMigrationRequired):
            classify_upgrade(BASE_MANIFEST, target)


if __name__ == "__main__":
    unittest.main()
