# implement a ring buffer with an array
# i.e. a queue implemented with an array, enqueue to the tail, deque from the head


class RingBuffer:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.head = -1
        self.tail = -1
        self.length = 0
        self.arr = [None] * capacity

    def queue(self, item: int) -> None:
        if self.length == self.capacity:
            self._increase_capacity()

        self.tail += 1
        if self.length == 0:
            self.head = self.tail
        self.arr[self.tail % self.capacity] = item
        self.length += 1

    def deque(self) -> int | None:
        if self.length == 0:
            return None
        value = self.arr[self.head % self.capacity]
        self.arr[self.head % self.capacity] = None
        self.head += 1
        self.length -= 1
        if self.length == 0:
            self.head, self.tail = -1, -1
        return value

    def _increase_capacity(self):
        new_arr = [None] * self.capacity * 2
        for i in range(self.length):
            new_arr[i] = self.arr[(i + self.head) % self.capacity]
        self.capacity *= 2
        self.head = 0
        self.tail = self.length - 1
        self.arr = new_arr
