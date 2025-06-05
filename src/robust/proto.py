from __future__ import annotations
from typing import Protocol


class Splittable(Protocol):
    cost: int
    name: str

    def split_in_half(self) -> tuple[Splittable, Splittable]:
        pass


class BLTSandwich:
    def __init__(self):
        self.cost = 6.95
        self.name = "BLT"

    def split_in_half(self) -> tuple[BLTSandwich, BLTSandwich]:
        pass
