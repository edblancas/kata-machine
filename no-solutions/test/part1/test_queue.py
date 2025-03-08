import unittest
from src.part1.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()

        q.enqueue(5)
        q.enqueue(7)
        q.enqueue(9)

        self.assertEqual(q.deque(), 5)
        self.assertEqual(q.length, 2)

        q.enqueue(11)

        self.assertEqual(q.deque(), 7)
        self.assertEqual(q.deque(), 9)
        self.assertEqual(q.peek(), 11)
        self.assertEqual(q.deque(), 11)
        self.assertEqual(q.deque(), None)
        self.assertEqual(q.length, 0)

        q.enqueue(69)
        self.assertEqual(q.peek(), 69)
        self.assertEqual(q.length, 1)
