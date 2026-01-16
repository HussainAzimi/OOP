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
# TODO: implement add() and consume() classmethods
@classmethod
def add(cls, uL: int, memo: str = "add") -> "SampleEvent":
"""Create an event representing adding uL microliters (must be > 0)."""
# TODO: validate uL is int and > 0; create event with positive change
raise NotImplementedError
@classmethod
def consume(cls, uL: int, memo: str = "consume") -> "SampleEvent":
"""Create an event representing consuming uL microliters (must be > 0)."""
# TODO: validate uL is int and > 0; create event with NEGATIVE change