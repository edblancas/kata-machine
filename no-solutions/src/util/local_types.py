from __future__ import annotations
from dataclasses import dataclass

# frozen so it can be hashable to use in a set
@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass
class BinaryNode:
    value: int
    left: BinaryNode | None = None
    right: BinaryNode | None = None

