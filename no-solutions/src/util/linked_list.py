# for dataclass to work recursively defined
# https://stephantul.github.io/python/mypy/types/2024/02/05/hierarchy/
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
    
class ListInterface[T]:
    def __init__(self, length=0):
        self.length = length

    def remove_at(self, idx: int) -> T | None:
        pass

    def remove(self, item: T) -> T | None:
        pass

    def get(self, idx: T) -> T | None:
        pass

    def prepend(self, item: T) -> None:
        pass

    def append(self, item: T) -> None:
        pass

    def insert_at(self, item: T, idx: int) -> None:
        pass

@dataclass
class ListNode[T]:
    value: T
    next: ListNode[T] | None = None
    prev: ListNode[T] | None = None
