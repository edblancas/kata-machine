# implement a ring buffer with an array
# i.e. a queue implemented with an array, enqueue to the tail, deque from the head

class RingBuffer:
    def __init__(self, capacity=3):
        self.length = 0
        self.capacity = capacity
        # the next attributes must be privates (start with an underscore _),
        # encapsulation, but for testing purposes we make them visible aka public
        # emulate a fix capacity array, same for all the operations
        self.arr = [None] * self.capacity
        self.head = -1
        self.tail = -1

    def queue(self, item:int) -> None:
        self.tail += 1
        self.length += 1
        if self.length == 1:
            self.head = self.tail
        if self.length > self.capacity:  # the capacity is full
            # double capacity is our simply strategy
            # python have other stategy like 1.125 size for smaller arrays
            # and 1.5 size for larger arrays
            self._increase_capacity()
        idx_add = self.tail % self.capacity
        self.arr[idx_add] = item

    def deque(self) -> int | None:
        if self.length == 0:
            return None
        idx_deque = self.head % self.capacity
        val = self.arr[idx_deque]
        # set to None, decrease the ref count so gc can free up mem
        self.arr[idx_deque] = None
        self.head += 1
        self.length -= 1
        if self.length == 0:
            self.head = -1
            self.tail = -1
        return val

    def _increase_capacity(self):
        old_capacity = self.capacity
        self.capacity *= 2
        tmp_arr = [None] * self.capacity
        for i in range(self.length):
            idx_get = (i + self.head) % old_capacity
            tmp_arr[i] = self.arr[idx_get]
        # the old array don't have a ref so it will be garbage collected
        self.arr = tmp_arr
        self.head = 0
        self.tail = self.length - 1

