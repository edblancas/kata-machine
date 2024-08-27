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

    def insert_at(self, item: int, idx: int) -> None:
        node = ListNode(item)

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        if idx == 0 or self.length == 0:
            self.head = node

        if idx == self.length or self.length == 0:
            self.tail = node

        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        self.length += 1


    def remove(self, item: int) -> int | None:
        prev = None
        curr = self.head
        while curr != None:
            if curr.value == item:
                break
            prev = curr
            curr = curr.next

        if curr == None:
            return None

        self._remove(prev, curr)

        return curr.value


    def remove_at(self, idx: int) -> ListNode | None:
        prev = None
        curr = self.head
        for _ in range(idx):
            prev = curr
            curr = curr.next

        self._remove(prev, curr)

        return curr.value


    def _remove(self, prev, curr):
        if curr is self.head:
            self.head = curr.next
            # clean up, will python garbage collect the curr node if its prev
            # is still pointing to something? YES, cuz it uses reference counting
            # and the curr node ref count will be 0, so the mem will be freed up
            # python also free up unreachable cyclic refs.
            # SO THIS IS NOT NEEDED!
            if self.length > 1:
                curr.next.prev = None
            self.length -= 1
            return
        if not curr:
            self.tail = prev
            self.length -= 1
            return

        prev.next = curr.next
        curr.next.prev = prev
        curr.next = None
        curr.prev = None
        self.length -= 1

    def get(self, idx):
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        return curr.value


    def prepend(self, item):
        node = ListNode(item)
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, item):
        node = ListNode(item)
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
