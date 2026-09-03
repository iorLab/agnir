from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from activation_reference import resolve_agent_activation
from core_reference import DiscoveryFailure
from repository_filesystem_0_2_migration_reference import (
    publish_repository_filesystem_0_2_migration,
    stage_repository_filesystem_0_1_to_0_2,
)
from repository_filesystem_0_2_reference import discover_repository_filesystem_0_2
from repository_filesystem_reference import discover_repository_filesystem


PUBLISHED_V0_1_1_MANIFEST_BLOB = "0d26a9ffb947f551af335963ef753e7c0758c505"
PUBLISHED_V0_1_1_MANIFEST = '''agnir:
  version: "0.1"
  discovery_profile: "repository-filesystem/0.1"

project:
  identity: "urn:agnir:project:agnir-core"
  profiles:
    - generic

memory:
  state: ".agnir/state.md"
  next_actions: ".agnir/next-actions.md"
  decisions: ".agnir/decisions.md"
  evidence: ".agnir/evidence/"

policy:
  checkpoint: event-driven

extensions:
  agnir/repository:
    canonical: "iorLab/agnir"
    authoritative_ref: "main"
'''


def _git_blob_sha(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def _write_activation(root: Path) -> None:
    (root / "AGENTS.md").write_text(
        "# Project instructions\n\nFollow README.md section Agnir Project Instructions.\n",
        encoding="utf-8",
    )
    (root / "README.md").write_text(
        """# RC fixture\n\n## Agnir Project Instructions\n\nTreat this repository root as the authorized Project Entry Point. Read top-level AGNIR.yaml before Project work. Load Current State and Next Actions for the selected continuity. Load Decisions and Evidence when relevant. Reconcile material durable truth at an intentional checkpoint.\n""",
        encoding="utf-8",
    )


def _write_memory(root: Path, *, state: str, next_actions: str) -> None:
    memory = root / ".agnir"
    evidence = memory / "evidence"
    evidence.mkdir(parents=True)
    (memory / "state.md").write_text(state, encoding="utf-8")
    (memory / "next-actions.md").write_text(next_actions, encoding="utf-8")
    (memory / "decisions.md").write_text("Preserve Project identity across compatibility migration.\n", encoding="utf-8")
    (evidence / "fixture.md").write_text("Published-shape migration fixture.\n", encoding="utf-8")


class RCReleaseGateTests(unittest.TestCase):
    def test_published_v0_1_1_manifest_fixture_is_exact(self) -> None:
        self.assertEqual(_git_blob_sha(PUBLISHED_V0_1_1_MANIFEST), PUBLISHED_V0_1_1_MANIFEST_BLOB)

    def test_fresh_core_0_2_install_cold_starts_without_predecessor_context(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "fresh-project"
            root.mkdir()
            _write_activation(root)
            _write_memory(root, state="fresh 0.2 project\n", next_actions="continue real project work\n")
            (root / "AGNIR.yaml").write_text(
                '''agnir:
  version: "0.2"
  discovery_profile: "repository-filesystem/0.2"

project:
  identity: "urn:agnir:test:rc-fresh-install"

continuity:
  lineage: "urn:agnir:test:lineage:initial"

memory:
  state: ".agnir/state.md"
  next_actions: ".agnir/next-actions.md"
  decisions: ".agnir/decisions.md"
  evidence: ".agnir/evidence/"

policy:
  checkpoint: event-driven
''',
                encoding="utf-8",
            )

            activation = resolve_agent_activation(root)
            self.assertIn("AGNIR.yaml", activation.readme_section)
            snapshot = discover_repository_filesystem_0_2(
                root,
                expected_project_identity="urn:agnir:test:rc-fresh-install",
                expected_lineage_identity="urn:agnir:test:lineage:initial",
            )
            self.assertEqual(snapshot.version, "0.2")
            self.assertEqual(snapshot.profile, "repository-filesystem/0.2")
            self.assertEqual(snapshot.state, "fresh 0.2 project\n")
            self.assertEqual(snapshot.next_actions, "continue real project work\n")
            self.assertIn("fixture.md", snapshot.evidence)

            with self.assertRaises(DiscoveryFailure) as ctx:
                discover_repository_filesystem(root)
            self.assertEqual(ctx.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

    def test_published_v0_1_1_shape_migrates_and_fresh_resumes_as_core_0_2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "published-v0.1.1-project"
            root.mkdir()
            _write_activation(root)
            _write_memory(
                root,
                state="Durable continuity belongs to the Project.\n",
                next_actions="validate explicit Core 0.2 migration and fresh resume\n",
            )
            (root / "AGNIR.yaml").write_text(PUBLISHED_V0_1_1_MANIFEST, encoding="utf-8")

            before = discover_repository_filesystem(
                root,
                expected_project_identity="urn:agnir:project:agnir-core",
            )
            self.assertEqual(before.version, "0.1")
            memory_paths = [
                root / ".agnir/state.md",
                root / ".agnir/next-actions.md",
                root / ".agnir/decisions.md",
                root / ".agnir/evidence/fixture.md",
            ]
            memory_before = {path: path.read_bytes() for path in memory_paths}
            manifest_before = (root / "AGNIR.yaml").read_text(encoding="utf-8")

            lineage = "urn:agnir:test:lineage:migrated-from-v0.1.1"
            candidate = stage_repository_filesystem_0_1_to_0_2(
                root,
                lineage_identity=lineage,
                authorized=True,
                expected_project_identity="urn:agnir:project:agnir-core",
            )
            self.assertTrue(candidate.changed)
            self.assertEqual((root / "AGNIR.yaml").read_text(encoding="utf-8"), manifest_before)

            migrated, changed = publish_repository_filesystem_0_2_migration(candidate)
            self.assertTrue(changed)
            self.assertEqual(migrated.project_identity, before.project_identity)
            self.assertEqual(migrated.lineage_identity, lineage)
            self.assertEqual(migrated.state, before.state)
            self.assertEqual(migrated.next_actions, before.next_actions)
            for path, content in memory_before.items():
                self.assertEqual(path.read_bytes(), content)

            activation = resolve_agent_activation(root)
            self.assertIn("Project Entry Point", activation.readme_section)
            resumed = discover_repository_filesystem_0_2(
                root,
                expected_project_identity="urn:agnir:project:agnir-core",
                expected_lineage_identity=lineage,
            )
            self.assertEqual(resumed.state, "Durable continuity belongs to the Project.\n")
            self.assertEqual(
                resumed.next_actions,
                "validate explicit Core 0.2 migration and fresh resume\n",
            )

            with self.assertRaises(DiscoveryFailure) as ctx:
                discover_repository_filesystem(root)
            self.assertEqual(ctx.exception.code, "AGNIR_DISCOVERY_UNSUPPORTED_VERSION")

            repeat = stage_repository_filesystem_0_1_to_0_2(
                root,
                lineage_identity=lineage,
                authorized=True,
                expected_project_identity="urn:agnir:project:agnir-core",
            )
            self.assertFalse(repeat.changed)
            repeated_snapshot, repeated_changed = publish_repository_filesystem_0_2_migration(repeat)
            self.assertFalse(repeated_changed)
            self.assertEqual(repeated_snapshot.lineage_identity, lineage)


if __name__ == "__main__":
    unittest.main()
