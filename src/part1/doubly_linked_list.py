# interface LinkedList
#   length: number
#   insert_at(item: T, index: number): void
#   remove(item: T) T | undefined
#   remove_at(index: number): T | undefined
#   append(item: T): void
#   prepend(item: T): void
#   get(index: number) T | undefined
from src.util.linked_list import ListInterface, ListNode

class DoublyLinkedList(ListInterface):
    def __init__(self, length=0):
        super().__init__(length)
        self.head = None
        self.tail = None
        self.lengthf = 0

    def insert_at(self, item: int, idx: int) -> None:
        if idx < 0 or idx >= self.length or self.length == 0:
            return None
        if idx == 0:
            self.prepend(item)
            return
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        n = ListNode(item)
        n.next = curr
        n.prev = curr.prev
        curr.prev = n
        curr.prev.next = n
        self.length += 1

    def remove(self, item: int) -> int | None:
        if self.length == 0:
            return None
        curr = self.head
        for i in range(self.length):
            if curr.value == item:
                return self.remove_at(i)
        return None

    def remove_at(self, idx: int) -> int | None:
        if idx < 0 or idx >= self.length or self.length == 0:
            return None
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1
        return curr.value

    def get(self, idx):
        if idx < 0 or idx >= self.length or self.length == 0:
            return None
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        return curr.value

    def prepend(self, item):
        n = ListNode(item)
        if self.length == 0:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.length += 1

    def append(self, item):
        n = ListNode(item)
        if self.length == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.length += 1
