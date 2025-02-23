# queue implementation with a linked list
from src.util.linked_list import ListNode


class Queue:
    def __init__(self, length=0):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, item):
        n = ListNode(item)
        if self.length == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.length += 1


    def deque(self):
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
