# stack implementation with a linked list and with an array
from src.util.linked_list import ListNode


class LinkedListStack:
    def __init__(self, length=0):
        self.head = None
        self.length = length

    def push(self, item):
        node = ListNode(item)

        if self.length == 0:
            self.head = node
            self.length += 1
            return

        node.next = self.head
        self.head = node
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
        self.length = length
        self.arr = [None] * capacity
        self.capacity = capacity

    def push(self, item):
        if self.length == self.capacity:
            new_arr = [None] * self.capacity * 2
            for i in range(self.capacity):
                new_arr[i] = self.arr[i]
            self.capacity *= 2
            self.arr = new_arr
        self.arr[self.length] = item
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        value = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        return value

    def peek(self):
        return self.arr[self.length-1]
