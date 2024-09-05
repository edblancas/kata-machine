# we combine the use of a double linked list with a hash map to get constant
# time lookup, insertion and deletion from any place
from __future__ import annotations
from src.util.linked_list import ListNode
from dataclasses import dataclass

# we can use the key in the node or, a reverse lookup map to delete from 
# our maps lookup/revers_lookup when deleting the last element
@dataclass
class LRUNode[K, V]:
    key: K
    value: V 
    next: LRUNode[K, V] | None = None
    prev: LRUNode[K, V] | None = None

class LRU[K, V]:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.lookup = {}
        self.length = 0

    def update(self, key: K, value: V) -> None:
        ...

    def get(self, key: K) -> V | None:
        ...

class LRUReverseLookup[K,V]:
    ...
