from src.part1.min_heap import MinHeap
import unittest

class TestMinHeap(unittest.TestCase):
    def test_min_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.length, 0)
        heap.insert(5)
        heap.insert(3)
        heap.insert(69)
        heap.insert(420)
        heap.insert(4)
        heap.insert(1)
        heap.insert(8)
        heap.insert(7)

        self.assertEqual(heap.length, 8)
        self.assertEqual(heap.delete(), 1)
        self.assertEqual(heap.delete(), 3)
        self.assertEqual(heap.delete(), 4)
        self.assertEqual(heap.delete(), 5)
        self.assertEqual(heap.length, 4)
        self.assertEqual(heap.delete(), 7)
        self.assertEqual(heap.delete(), 8)
        self.assertEqual(heap.delete(), 69)
        self.assertEqual(heap.delete(), 420)
        self.assertEqual(heap.length, 0)


if __name__ == '__main__':
    unittest.main()
