# we combine the use of a double linked list with a hash map to get constant
# time lookup, insertion and deletion from any place
from __future__ import annotations
from src.util.linked_list import ListNode
from dataclasses import dataclass


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
        self.hash_map = {}
        self.length = 0

    def update(self, key: K, value: V) -> None:
        node = self.hash_map.get(key)

        if not node and self.length == 0:
            node = LRUNode(key, value)
            self.tail = node
            self.head = node
            self.hash_map[key] = node
            self.length += 1
            return

        if not node:
            node = LRUNode(key, value)
            self.hash_map[key] = node
            self.length += 1
            self.head.prev = node
            node.next = self.head
            self.head = node
            if self.length > self.capacity:
                # not needed as gc of py will collect it
                prev_tail = self.tail
                self.tail = self.tail.prev
                prev_tail.prev = None
                del self.hash_map[prev_tail.key]
                self.length -= 1
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        self.tail = node
        # only true when there are 2 items and we update the tail
        if self.tail == node:
            self.tail = node.next

        if self.length > self.capacity:
            # not needed as gc of py will collect it
            prev_tail = self.tail
            self.tail = self.tail.prev
            prev_tail.prev = None
            del self.hash_map[prev_tail.key]
            self.length -= 1

    def get(self, key: K) -> V | None:
        node = self.hash_map.get(key)
        if not node:
            return None

        if node == self.head:
            return node.value

        node.prev.next = node.next
        if self.tail != node:
            node.next.prev = node.prev
        node.prev = None
        node.next = self.head
        self.tail = node
        # only true when there are 2 items and we update the tail
        if self.tail == node:
            self.tail = node.next

        return node.value

