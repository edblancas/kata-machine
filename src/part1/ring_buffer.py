# implement a ring buffer with an array
# i.e. a queue implemented with an array, enqueue to the tail, deque from the head
# note: just the enqueue and deque, and size should be checked in the tests.
#       but for better implementation purposes, the tail is checked and should be
#       point to the next position to enqueue


class RingBuffer:
    def __init__(self, capacity=3):
        self.length = 0
        self.capacity = capacity
        self.arr = [None] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item: int) -> None:
        if self.length == self.capacity:
            self._increase_capacity()
        pos = self.tail % self.capacity
        self.arr[pos] = item
        self.tail += 1
        self.length += 1

    def deque(self) -> int | None:
        if self.length == 0:
            return None
        value = self.arr[self.head]
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return value

    def _increase_capacity(self):
        new_arr = [None] * self.capacity * 2
        for i in range(self.capacity):
            pos = (self.head + i) % self.capacity
            new_arr[i] = self.arr[pos]
        self.arr = new_arr
        self.capacity *= 2
        self.head = 0
        self.tail = self.length
