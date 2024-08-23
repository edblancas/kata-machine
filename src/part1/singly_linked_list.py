from src.util.linked_list import ListInterface, ListNode

class SinglyLinkedList(ListInterface[int]):
    def __init__(self):
        self.length = 0
        self.head = None

    def prepend(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.length += 1
            return

        node = ListNode(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.length += 1
            return

        node = ListNode(value)
        curr = self.head
        for _ in range(self.length - 1):
            curr = curr.next

        curr.next = node
        self.length += 1

    def remove_at(self, idx):
        if self.length == 0:
            return
        elif self.length == 1:
            v = self.head.value
            self.head = None
            self.length -= 1
            return v
        elif idx == 0:
            tmp_node = self.head
            self.head = self.head.next
            tmp_node.next = None
            self.length -= 1
            return tmp_node.value
        elif idx >= self.length:
            return None
        else:
            curr = self.head
            before = None
            for _ in range(idx):
                before = curr
                curr = curr.next
            before.next = curr.next
            curr.next = None
            self.length -= 1
            return curr.value

    def get(self, idx):
        if idx >= self.length:
            return -1

        curr = self.head
        for _ in range(idx):
            curr = curr.next

        return curr.value

    def remove(self, value):
        if self.length == 0:
            return -1
        if self.length == 1:
            self.length = 0
            val = self.head.value
            self.head = None
            return val

        curr = self.head
        before = None
        for i in range(self.length):
            if curr.value == value:
                if i == 0:
                    tmp = self.head
                    self.head = self.head.next
                    tmp.next = None
                    self.length -= 1
                    return tmp.value

                self.length -= 1
                before.next = curr.next
                curr.next = None
                return curr.value
            before = curr
            curr = curr.next

        return None

