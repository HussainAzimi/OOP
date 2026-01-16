from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4, UUID
UTC = timezone.utc


@dataclass(frozen=True)
class SampleEvent:
    """Immutable record of a sample volume change (in microliters).
       volume_change_uL: positive for additions, negative for removals
    """
    id: UUID
    volume_change_uL: int
    memo: str
    ts: datetime
    
    @property
    def amount(self):
        return self._volume_change_uL
    

    # TODO: implement add() and consume() classmethods
    @classmethod
    def add(cls, uL: int, memo: str = "add") -> "SampleEvent":
        """Create an event representing adding uL microliters (must be > 0)."""
        if not isinstance(uL, int):
            raise TypeError("volume must be an integer.")
        if uL <= 0:
            raise ValueError("Addition must be greater than 0.")
        
        return cls(  # Event for positive change
            id = uuid4(),
            volume_change_uL = uL,
            memo = memo,
            tst = datetime.now(timezone.utc)
        )
    
    @classmethod
    def consume(cls, uL: int, memo: str = "consume") -> "SampleEvent":
        """Create an event representing consuming uL microliters (must be > 0)."""
        if not isinstance(uL, int):
            raise TypeError("Volume must be an integer.")
        if uL <= 0:
            raise ValueError("Consumption must be greater than 0.")
        
        return cls( # Event for negative change
            id = uuid4(),
            volume_change_uL = -uL,
            memo = memo,
            tst = datetime.now(timezone.utc)
        )