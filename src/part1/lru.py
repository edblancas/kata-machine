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
        node = self.lookup.get(key)
        if node:
            self._detach(node)
            self._prepend(node)
            node.value = value
            return
        node = LRUNode(key, value)
        self._prepend(node)
        self.lookup[key] = node
        self.length += 1
        self._trim_cache()

    def get(self, key: K) -> V | None:
        node = self.lookup.get(key)
        if not node:
            return None
        self._detach(node)
        # *1
        # self.length -= 1
        self._prepend(node)
        # *1
        # self.length += 1
        return node.value

    def _detach(self, node):
        # not needed, the else of the nexts if manages it
        # if self.length == 1:
        #     self.head = None
        #     self.tail = None
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None

    def _prepend(self, node):
        # *1
        # use it if we decrease increase lenght
        # each time we _detach and _prepend
        # if self.length == 0:
        # use it if we do not increase decrease
        # at _detach and _prepend
        if not self.head:
            self.tail = node
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def _trim_cache(self):
        if self.capacity < self.length:
            tmp_tail_key = self.tail.key
            self._detach(self.tail)
            self.length -= 1
            del self.lookup[tmp_tail_key]


class LRUReverseLookup[K,V]:
    ...
