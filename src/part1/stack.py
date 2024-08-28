# stack implementation with a linked list and with an array

from src.util.linked_list import ListNode

class LinkedListStack:
    def __init__(self, length=0):
        self.length = 0
        self.head = None

    def push(self, item):
        node = ListNode(item)
        if not self.head:
            self.head = node
            self.length += 1
            return
        node.next = self.head
        self.head = node
        self.length += 1

    def pop(self):
        if not self.head:
            return None
        val = self.head.value
        self.head = self.head.next
        # we do not set the old head.next = None, garbage collector from python
        # will freed up the memory
        self.length -= 1
        return val

    def peek(self):
        return self.head.value


# we emulate a primitive array, cuz the python list is a dynamic array
class ArrayStack:
    def __init__(self, length=0, capacity=5):
        self.length = length
        self.capacity = capacity
        self.arr = [None] * self.capacity

    def push(self, item):
        if self.length == self.capacity:
            self.arr += [None] * self.capacity
        self.arr[self.length] = item
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.arr[self.length]

    def peek(self):
        if self.length == 0:
            return None
        return self.arr[self.length - 1]
