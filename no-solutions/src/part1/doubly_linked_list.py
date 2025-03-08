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

    def insert_at(self, item: int, idx: int) -> None: ...

    def remove(self, item: int) -> int | None: ...

    def remove_at(self, idx: int) -> int | None: ...

    def get(self, idx): ...

    def prepend(self, item): ...

    def append(self, item): ...
