from src.part1.ring_buffer import RingBuffer
import unittest

# tdd done right!
class TestRingBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = RingBuffer(capacity=3)

    def test_queue_deque(self):
        self.buffer.queue(5)
        self.assertEqual(self.buffer.deque(), 5)
        self.assertEqual(self.buffer.deque(), None)
        self.assertEqual(self.buffer.length, 0)

    def test_full_capacity(self):
        self.buffer.queue(0)
        self.buffer.queue(1)
        self.buffer.queue(2)
        self.assertEqual(self.buffer.length, 3)
        self.assertEqual(self.buffer.deque(), 0)
        self.assertEqual(self.buffer.deque(), 1)
        self.assertEqual(self.buffer.deque(), 2)
        self.assertEqual(self.buffer.length, 0)

    def test_increase_capacity(self):
        self.buffer.queue(0)
        self.buffer.queue(1)
        self.buffer.queue(2)
        self.assertEqual(self.buffer.capacity, 3)
        self.buffer.queue(3)
        self.assertEqual(self.buffer.length, 4)
        self.assertEqual(self.buffer.capacity, 6)
        self.assertEqual(self.buffer.head, 0)
        self.assertEqual(self.buffer.tail, 3)
        self.assertEqual(self.buffer.deque(), 0)
        self.assertEqual(self.buffer.deque(), 1)
        self.assertEqual(self.buffer.deque(), 2)
        self.assertEqual(self.buffer.deque(), 3)
        self.assertEqual(self.buffer.length, 0)

    def test_reset_head_tail(self):
        self.buffer.queue(0)
        self.buffer.queue(1)
        self.buffer.queue(2)
        self.assertEqual(self.buffer.capacity, 3)
        self.assertEqual(self.buffer.deque(), 0)
        self.assertEqual(self.buffer.length, 2)
        self.assertEqual(self.buffer.head, 1)
        self.assertEqual(self.buffer.tail, 2)
        self.assertEqual(self.buffer.deque(), 1)
        self.assertEqual(self.buffer.head, 2)
        self.assertEqual(self.buffer.tail, 2)
        self.assertEqual(self.buffer.deque(), 2)
        self.assertEqual(self.buffer.head, -1)
        self.assertEqual(self.buffer.tail, -1)

    def test_circular_head_tail(self):
        self.buffer.queue(0)
        self.buffer.queue(1)
        self.buffer.queue(2)
        self.assertEqual(self.buffer.capacity, 3)
        self.assertEqual(self.buffer.deque(), 0)
        self.assertEqual(self.buffer.length, 2)
        self.assertEqual(self.buffer.head, 1)
        self.assertEqual(self.buffer.tail, 2)
        self.assertEqual(self.buffer.deque(), 1)
        self.assertEqual(self.buffer.head, 2)
        self.assertEqual(self.buffer.tail, 2)
        self.buffer.queue(3)
        self.assertEqual(self.buffer.head, 2)
        self.assertEqual(self.buffer.tail, 3)
        self.assertEqual(self.buffer.length, 2)
        self.buffer.queue(4)
        self.assertEqual(self.buffer.head, 2)
        self.assertEqual(self.buffer.tail, 4)
        self.assertEqual(self.buffer.length, 3)
        self.assertEqual(self.buffer.arr, [3, 4 ,2])
        self.buffer.queue(5)
        self.assertEqual(self.buffer.arr, [2, 3, 4, 5, None, None])
        self.assertEqual(self.buffer.capacity, 6)
        self.assertEqual(self.buffer.head, 0)
        self.assertEqual(self.buffer.tail, 3)
        self.assertEqual(self.buffer.length, 4)
