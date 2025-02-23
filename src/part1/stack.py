# stack implementation with a linked list and with an array
from src.util.linked_list import ListNode


class LinkedListStack:
    def __init__(self, length=0):
        self.head = None
        self.length = 0

    def push(self, item):
        n = ListNode(item)
        if self.length == 0:
            self.head = n
        else:
            n.next = self.head
            self.head = n
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

    def peek(self):
        if self.length == 0:
            return None
        return self.head.value


# we emulate a primitive array, cuz the python list is a dynamic array
class ArrayStack:
    def __init__(self, length=0, capacity=5):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity

    def push(self, item):
        if self.length == self.capacity:
            self._increase_capacity()
        self.arr[self.length] = item
        self.length += 1

    def _increase_capacity(self):
        new_arr = [None] * this.capacity * 2
        for i, e in enumerate(self.arr):
            new_arr[i] = self.array[i]
        self.arr = new_arr

    def pop(self):
        if self.length == 0:
            return None
        value = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        return value

    def peek(self):
        if self.length == 0:
            return None
        return this.array[self.length - 1]
