from __future__ import annotations
from src.util.linked_list import ListNode
from dataclasses import dataclass

@dataclass
class LRUNode[K, V]:
    key: K
    value: V 
    next: LRUNode[K, V] | None = None
    prev: LRUNode[K, V] | None = None


class LRUNoLookup[K, V]:
    def __init__(self, capacity=3):
        self.capacity = capacity

    def update(self, key: K, value: V) -> None: ...

    def get(self, key: K) -> V | None: ...


class Node[V]:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __hash__(self):
        return hash(self.value)

class LRU[V]:
    def __init__(self, capacity=3):
        self.capacity = capacity

    def update(self, key: K, value: V) -> None: ...

    def get(self, key: K) -> V | None: ...
