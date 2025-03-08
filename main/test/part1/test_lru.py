import unittest
from src.part1.lru import LRU

class TestLRU(unittest.TestCase):
    def test_test_lru(self):
        lru = LRU[str, int](3)

        self.assertEqual(lru.get('foo'), None)
        lru.update('foo', 69)
        self.assertEqual(lru.get('foo'), 69)

        lru.update('bar', 420)
        self.assertEqual(lru.get('bar'), 420)

        lru.update('baz', 1337)
        self.assertEqual(lru.get('baz'), 1337)

        lru.update('ball', 69420)
        self.assertEqual(lru.get('ball'), 69420)
        self.assertEqual(lru.get('foo'), None)
        self.assertEqual(lru.get('bar'), 420)
        # this will evict baz
        lru.update('foo', 69)
        self.assertEqual(lru.get('bar'), 420)
        self.assertEqual(lru.get('foo'), 69)

        self.assertEqual(lru.get('baz'), None)

        # here the doubly linked list is
        # head-> foo - bar - ball <-tail
        # foo.next points to bar
        # bar.next points to ball
        # bar.prev points to foo
        # ball.prev points to bar
