from __future__ import annotations
from src.util.linked_list import ListNode
from dataclasses import dataclass

# with a key in the node, we avoid using a reverseLookup to remove the
# last node when timming the cache

@dataclass
class LRUNode[K, V]:
    key: K
    value: V 
    next: LRUNode[K, V] | None = None
    prev: LRUNode[K, V] | None = None


class LRU2[K, V]:
    def __init__(self, capacity=3):
        self.capacity = capacity

    def update(self, key: K, value: V) -> None: ...

    def get(self, key: K) -> V | None: ...


# without the frozen the class will throw an error cuz is unhashable when add to dict as key
# with the frozen we cannot set next or prev
@dataclass(frozen=True)
class Node2[V]:
    value: V 
    next: LRUNode[V] | None = None
    prev: LRUNode[V] | None = None

# this works but the dunder hash should only include self.value, if we include next or prev
# will throw an error as it will be called recursively
class Node[V]:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __hash__(self):
        return hash(self.value)

class LRU[K, V]:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.lookup = dict()
        self.reverseLookup = dict()

    def update(self, key: K, value: V) -> None:
        # if node exists:
            # get the node, update the value
            # dettach node, and prepend
        # if not:
            # if len == capacity: trim cache
            # create new node and prepend it
        node = self.lookup.get(key)
        if not node:
            node = Node(value)
            self.length += 1
            self._prepend(node)
            self._trim_cache()
            self.lookup[key] = node
            self.reverseLookup[node] = key
        else:
            self._dettach(node)
            self._prepend(node)


    def get(self, key: K) -> V | None:
        # if len == 0 or key not exist in lookup: return none
        # get node, save ref to return at end
        # dettach the node and prepend it
        node = self.lookup.get(key)
        if self.length == 0 or not node:
            return None

        self._dettach(node)
        self._prepend(node)

        return node.value


    def _dettach(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev

        node.next = None
        node.prev = None


    def _prepend(self, node):
        if not self.head:
            self.tail = node
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def _trim_cache(self):
        # do it only when the capacity >= length, cuz we increase the length
        # before running trim_cache
        # also we do the check here cuz we didn't before running it in update
        # fan of early returns XD
        if self.length <= self.capacity:
            return
        # remove tail
        # delete from lookup and reverseLookup
        tail = self.tail
        self._dettach(tail)
        key = self.reverseLookup[tail]
        del self.lookup[key]
        del self.reverseLookup[tail]
        self.length -= 1
