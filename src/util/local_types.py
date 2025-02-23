from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass
class BinaryNode:
    value: int
    left: BinaryNode | None = None
    right: BinaryNode | None = None

