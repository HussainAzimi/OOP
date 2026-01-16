
from __future__ import annotations
from typing import List, Tuple, Iterable
from uuid import UUID
from sample_transaction import SampleEvent


class InsufficientVolumeError(Exception):
    """Raised when an action would make volume negative."""

class SampleTube:
    """A lab sample tube with a current volume (µL) and an event ledger."""
    def __init__(self, label: str):
        self.label = str(label)
        self._volume_uL: int = 0 # encapsulated state
        self._ledger: List[SampleEvent] = []

    # --- Properties ---
    @property
    def volume_uL(self) -> int:
        """Read-only current volume in microliters."""
        return self._volume_uL
    
    # --- Core behavior ---
    def add_volume(self, uL: int, memo: str = "add") -> SampleEvent:
        """Add volume to this tube. Use EAFP: create event first, then apply."""
        event = SampleEvent.add(uL, memo)

        self._volume_uL += event.volume_change_uL
        self._ledger.append(event)

        return event
    
    def consume_volume(self, uL: int, memo: str = "consume") -> SampleEvent:
        """Remove volume from this tube. Reject if volume would go negative."""
        event = SampleEvent.consume(uL, memo)

        if self._volume_uL + event.volume_change_uL < 0:
            raise InsufficientVolumeError(f"Cannot remove {uL} ul from {self._volume_uL} uL.")
        
        self._volume_uL += event.volume_change_uL
        self._ledger.append(event)

        return event

    def transfer_to(self, other: "SampleTube", uL: int) -> tuple[SampleEvent,
    SampleEvent]:
        """Aliquot uL from self to other as two events (consume here, add
        there)."""
        out_evt = self.consume_volume(uL, memo=f"Transfer to {other.label}")
        in_evt = other.add_volume(uL, memo=f"Transfer from {self.label}")

        return (out_evt, in_evt)

    def events(self) -> Tuple[SampleEvent, ...]:
        """Return a read-only view of the ledger (tuple)."""
        return tuple(self._ledger)

    def find_event(self, id: UUID) -> SampleEvent | None:
        for e in self._ledger:
          if e.id == id:
            return e
        return None
    
    def __repr__(self) -> str:
        return f"SampleTube(label='{self.label}', Volume='{self._volume_uL}µL, events={len(self._ledger)})"
