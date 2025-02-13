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
        if idx < 0 or idx >= self.length:
            raise Error('oh no!')
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        node = ListNode(item)

        node.next = curr
        node.prev = curr.prev
        curr.prev.next = node
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
            i += 1


    def remove_at(self, idx: int) -> ListNode | None:
        node = self._get_node_at(idx)
        val = node.value
        if idx == 0:
            self.head = node.next
        elif idx == self.length - 1:
            self.tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return val


    def get(self, idx):
        return self._get_node_at(idx).value


    def _get_node_at(self, idx):
        if idx < 0 or idx >= self.length:
            raise Error('oh no!')

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr


    def prepend(self, item):
        node = ListNode(item)
        self.length += 1

        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node


    def append(self, item):
        self.length += 1
        node = ListNode(item)

        if not self.head:
            self.head = node
            self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
