import unittest
from src.part1.mergesort import mergesort, mergesort_iter

class TestMergesort(unittest.TestCase):
    def test_mergesort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        self.assertEqual(mergesort(arr), [3, 4, 7, 9, 42, 69, 420])

    def test_mergesort_iter(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        self.assertEqual(mergesort_iter(arr), [3, 4, 7, 9, 42, 69, 420])
