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
        self.length = length
        self.head = None

    def insert_at(self, item: int, idx: int) -> None:
        if idx < 0:
            return None

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        node = ListNode(item)

        if idx == 0:
            self.head = node

        if curr.prev:
            curr.prev.next = node
        if curr.next:
            curr.next.prev = node
            curr.next = curr.next.next
        node.next = curr
        curr.prev = node
        self.length += 1


    def remove(self, item: int) -> int | None:
        if self.length == 0:
            return None

        curr = self.head
        i = 0
        while curr:
            if curr.value == item:
                return self.remove_at(i)
            curr = curr.next

        return None


    def remove_at(self, idx: int) -> ListNode | None:
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
        if curr.next:
            curr.next.prev = curr.prev
        self.length -= 1
        return curr.value



    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value


    def prepend(self, item):
        node = ListNode(item)
        if self.length == 0:
            self.head = node
            self.length += 1
            return

        self.head.prev = node
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, item):
        node = ListNode(item)
        if self.length == 0:
            self.head = node
            self.length += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node
        node.prev = curr
        self.length += 1
