from src.util.linked_list import ListInterface, ListNode


class SinglyLinkedList(ListInterface[int]):
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, item):
        if self.length == 0:
            self.head = ListNode(item)
            self.length += 1
            return

        node = ListNode(item)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, item) -> None:
        if self.head == None:
            self.head = ListNode(item)
            self.length += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(item)
        self.length += 1


    def remove_at(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        if self.length == 0:
            return None

        if idx == 0:
            v = self.head.value
            self.head = self.head.next
            self.length -= 1
            return v

        prev = None
        curr = self.head
        for _ in range(idx):
            prev = curr
            curr = curr.next

        prev.next = curr.next
        self.length -= 1
        return curr.value


    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        
        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value

    def remove(self, item):
        if self.length == 0:
            return None

        curr = self.head
        for i in range(self.length):
            if curr.value == item:
                return self.remove_at(i)
            curr = curr.next

        return None

    def print(self):
        l = ""
        curr = self.head
        while curr:
            l += str(curr.value) + "->"
            curr= curr.next
        print('length', self.length)
        print(l)
