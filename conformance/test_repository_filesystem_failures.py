from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from repository_filesystem_reference import (
    DiscoveryFailure,
    discover_repository_filesystem,
    select_unique_project_root,
)


PARENT_ID = "urn:test:agnir-parent"
CHILD_ID = "urn:test:agnir-child"


def write_project(
    root: Path,
    *,
    identity: str,
    version: str = "0.1",
    state_locator: str = ".agnir/state.md",
    create_state: bool = True,
) -> None:
    (root / ".agnir/evidence").mkdir(parents=True)
    if create_state:
        (root / ".agnir/state.md").write_text(f"# State\n{identity}\n", encoding="utf-8")
    (root / ".agnir/next-actions.md").write_text("# Next\ncontinue\n", encoding="utf-8")
    (root / ".agnir/decisions.md").write_text("# Decisions\nfixture\n", encoding="utf-8")
    (root / "AGNIR.yaml").write_text(
        "agnir:\n"
        f'  version: "{version}"\n'
        '  discovery_profile: "repository-filesystem/0.1"\n\n'
        "project:\n"
        f'  identity: "{identity}"\n\n'
        "memory:\n"
        f'  state: "{state_locator}"\n'
        '  next_actions: ".agnir/next-actions.md"\n'
        '  decisions: ".agnir/decisions.md"\n'
        '  evidence: ".agnir/evidence/"\n',
        encoding="utf-8",
    )


class RepositoryFilesystemNegativeFixtures(unittest.TestCase):
    def assert_failure(self, code: str, callback) -> None:
        with self.assertRaises(DiscoveryFailure) as raised:
            callback()
        self.assertEqual(raised.exception.code, code)

    def test_missing_discovery_record_is_not_found(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assert_failure(
                "AGNIR_DISCOVERY_NOT_FOUND",
                lambda: discover_repository_filesystem(directory),
            )

    def test_broken_required_locator_is_unresolvable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(
                root,
                identity=PARENT_ID,
                state_locator=".agnir/missing-state.md",
                create_state=False,
            )
            self.assert_failure(
                "AGNIR_DISCOVERY_UNRESOLVABLE",
                lambda: discover_repository_filesystem(
                    root,
                    expected_project_identity=PARENT_ID,
                ),
            )

    def test_unsupported_version_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, identity=PARENT_ID, version="9.9")
            self.assert_failure(
                "AGNIR_DISCOVERY_UNSUPPORTED_VERSION",
                lambda: discover_repository_filesystem(
                    root,
                    expected_project_identity=PARENT_ID,
                ),
            )

    def test_project_identity_mismatch_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_project(root, identity=CHILD_ID)
            self.assert_failure(
                "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                lambda: discover_repository_filesystem(
                    root,
                    expected_project_identity=PARENT_ID,
                ),
            )

    def test_multiple_unselected_candidate_roots_are_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            first = workspace / "one"
            second = workspace / "two"
            first.mkdir()
            second.mkdir()
            write_project(first, identity=PARENT_ID)
            write_project(second, identity=CHILD_ID)

            self.assert_failure(
                "AGNIR_DISCOVERY_AMBIGUOUS",
                lambda: select_unique_project_root([first, second]),
            )

    def test_nested_projects_respect_the_selected_root_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory) / "parent"
            child = parent / "child"
            parent.mkdir()
            child.mkdir()
            write_project(parent, identity=PARENT_ID)
            write_project(child, identity=CHILD_ID)

            parent_snapshot = discover_repository_filesystem(
                parent,
                expected_project_identity=PARENT_ID,
            )
            child_snapshot = discover_repository_filesystem(
                child,
                expected_project_identity=CHILD_ID,
            )

            self.assertEqual(parent_snapshot.project_root, parent.resolve())
            self.assertEqual(parent_snapshot.project_identity, PARENT_ID)
            self.assertIn(PARENT_ID, parent_snapshot.state)
            self.assertNotIn(CHILD_ID, parent_snapshot.state)

            self.assertEqual(child_snapshot.project_root, child.resolve())
            self.assertEqual(child_snapshot.project_identity, CHILD_ID)
            self.assertIn(CHILD_ID, child_snapshot.state)
            self.assertNotIn(PARENT_ID, child_snapshot.state)

            self.assert_failure(
                "AGNIR_DISCOVERY_PROJECT_MISMATCH",
                lambda: discover_repository_filesystem(
                    child,
                    expected_project_identity=PARENT_ID,
                ),
            )


if __name__ == "__main__":
    unittest.main()
