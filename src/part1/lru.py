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


@dataclass
class Node[V]:
    value: V 
    next: LRUNode[V] | None = None
    prev: LRUNode[V] | None = None

class LRU[K, V]:
    def __init__(self, capacity=3):
        self.capacity = capacity

    def update(self, key: K, value: V) -> None: ...

    def get(self, key: K) -> V | None: ...
