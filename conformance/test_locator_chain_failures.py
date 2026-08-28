from __future__ import annotations

import unittest

from core_reference import DiscoveryFailure
from locator_chain_reference import (
    ChainRecord,
    LocatorChainReference,
    LocatorChainRegistry,
    MemoryObject,
)


PROJECT = "urn:test:agnir-chain"


class LocatorChainFailureTests(unittest.TestCase):
    def assert_failure(self, code: str, callback) -> None:
        with self.assertRaises(DiscoveryFailure) as raised:
            callback()
        self.assertEqual(raised.exception.code, code)

    def test_cycle_is_detected_before_fabricating_continuity(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record("locator:a", ChainRecord(PROJECT, next_locator="locator:b"))
        registry.put_record("locator:b", ChainRecord(PROJECT, next_locator="locator:a"))

        self.assert_failure(
            "AGNIR_DISCOVERY_CYCLE",
            lambda: LocatorChainReference(registry).resolve(
                "locator:a",
                expected_project_identity=PROJECT,
            ),
        )

    def test_superseded_record_is_stale(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record(
            "locator:stale",
            ChainRecord(
                PROJECT,
                state_locator="memory:state",
                next_actions_locator="memory:next",
                superseded=True,
            ),
        )
        registry.put_memory("memory:state", MemoryObject("old-state", "cp-1"))
        registry.put_memory("memory:next", MemoryObject("old-next", "cp-1"))

        self.assert_failure(
            "AGNIR_DISCOVERY_STALE",
            lambda: LocatorChainReference(registry).resolve(
                "locator:stale",
                expected_project_identity=PROJECT,
            ),
        )

    def test_non_authoritative_record_is_stale(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record(
            "locator:replica",
            ChainRecord(
                PROJECT,
                state_locator="memory:state",
                next_actions_locator="memory:next",
                authoritative=False,
            ),
        )
        registry.put_memory("memory:state", MemoryObject("replica-state", "cp-1"))
        registry.put_memory("memory:next", MemoryObject("replica-next", "cp-1"))

        self.assert_failure(
            "AGNIR_DISCOVERY_STALE",
            lambda: LocatorChainReference(registry).resolve(
                "locator:replica",
                expected_project_identity=PROJECT,
            ),
        )

    def test_different_checkpoint_generations_are_inconsistent(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record(
            "locator:project",
            ChainRecord(
                PROJECT,
                state_locator="memory:state",
                next_actions_locator="memory:next",
            ),
        )
        registry.put_memory("memory:state", MemoryObject("new-state", "cp-2"))
        registry.put_memory("memory:next", MemoryObject("old-next", "cp-1"))

        self.assert_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            lambda: LocatorChainReference(registry).resolve(
                "locator:project",
                expected_project_identity=PROJECT,
            ),
        )

    def test_hop_cannot_also_claim_terminal_memory(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record(
            "locator:contradictory",
            ChainRecord(
                PROJECT,
                next_locator="locator:next",
                state_locator="memory:state",
            ),
        )

        self.assert_failure(
            "AGNIR_DISCOVERY_INCONSISTENT",
            lambda: LocatorChainReference(registry).resolve(
                "locator:contradictory",
                expected_project_identity=PROJECT,
            ),
        )

    def test_consistent_multi_hop_chain_resolves(self) -> None:
        registry = LocatorChainRegistry()
        registry.put_record("locator:entry", ChainRecord(PROJECT, next_locator="locator:record"))
        registry.put_record(
            "locator:record",
            ChainRecord(
                PROJECT,
                state_locator="memory:state",
                next_actions_locator="memory:next",
            ),
        )
        registry.put_memory("memory:state", MemoryObject("current-state", "cp-3"))
        registry.put_memory("memory:next", MemoryObject("current-next", "cp-3"))

        snapshot = LocatorChainReference(registry).resolve(
            "locator:entry",
            expected_project_identity=PROJECT,
        )

        self.assertEqual(snapshot.project_identity, PROJECT)
        self.assertEqual(snapshot.checkpoint_id, "cp-3")
        self.assertEqual(snapshot.state, "current-state")
        self.assertEqual(snapshot.next_actions, "current-next")


if __name__ == "__main__":
    unittest.main()
