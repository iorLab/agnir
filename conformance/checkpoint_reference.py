from __future__ import annotations

from dataclasses import dataclass


class CheckpointConflict(RuntimeError):
    code = "AGNIR_CHECKPOINT_CONFLICT"


@dataclass(frozen=True)
class ContinuityCandidate:
    state: str
    next_actions: str
    decisions: str | None
    evidence: tuple[tuple[str, str], ...] = ()


@dataclass(frozen=True)
class PublishedCheckpoint:
    revision: int
    checkpoint_id: str
    continuity: ContinuityCandidate


class CheckpointStoreReference:
    """Conformance-only model for Core checkpoint publication semantics.

    The model is deliberately substrate-neutral. A production backend may use a
    database transaction, immutable generation + pointer swap, VCS revision, or
    another publication primitive. The invariant under pressure is that a fresh
    reader observes either the previous complete checkpoint or the next complete
    checkpoint, never an accepted mixture of both.
    """

    def __init__(self, initial: ContinuityCandidate) -> None:
        self._current = PublishedCheckpoint(
            revision=0,
            checkpoint_id="checkpoint-0",
            continuity=initial,
        )

    @property
    def current(self) -> PublishedCheckpoint:
        return self._current

    def evaluate(self, candidate: ContinuityCandidate) -> bool:
        """Return True only when durable continuity materially changed."""
        return candidate != self._current.continuity

    def publish(
        self,
        *,
        base_revision: int,
        candidate: ContinuityCandidate,
    ) -> tuple[PublishedCheckpoint, bool]:
        if base_revision != self._current.revision:
            raise CheckpointConflict(
                f"{CheckpointConflict.code}: base revision {base_revision} is stale; "
                f"authoritative revision is {self._current.revision}"
            )

        if not self.evaluate(candidate):
            return self._current, False

        next_revision = self._current.revision + 1
        self._current = PublishedCheckpoint(
            revision=next_revision,
            checkpoint_id=f"checkpoint-{next_revision}",
            continuity=candidate,
        )
        return self._current, True
