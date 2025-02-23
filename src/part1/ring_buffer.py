# implement a ring buffer with an array
# i.e. a queue implemented with an array, enqueue to the tail, deque from the head
# note: just the enqueue and deque, and size should be checked in the tests.
#       but for better implementation purposes, the tail is checked and should be
#       point to the next position to enqueue


class RingBuffer:
    def __init__(self, capacity=3): ...

    def queue(self, item: int) -> None: ...

    def deque(self) -> int | None: ...

    def _increase_capacity(self): ...
