from src.util.linked_list import ListInterface, ListNode


class SinglyLinkedList(ListInterface[int]):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item):
        n = ListNode(item)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
        self.length += 1

    def append(self, item) -> None:
        n = ListNode(item)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.length += 1

    def remove_at(self, idx):
        if idx < 0 or idx >= self.length:
            raise Exception('oh no!')

        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        if idx == 0:
            tmp = self.head
            self.head = self.head.next
            self.length -= 1
            return tmp.value

        curr = self.head
        prev = None
        for _ in range(idx):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        self.length -= 1

        return curr.value


    def get(self, idx):
        if idx < 0 or idx >= self.length:
            raise Exception('oh no!')

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value

    def remove(self, item):
        if self.length == 0:
            raise Exception('oh no !')

        curr = self.head
        for i in range(self.length - 1):
            if curr.value == item:
                return self.remove_at(i)
        return None 


