import unittest
from src.part1.mergesort import mergesort, mergesort_rec_2

class TestMergesort(unittest.TestCase):
    def test_mergesort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        mergesort(arr)
        self.assertEqual(arr, [3, 4, 7, 9, 42, 69, 420])

    def test_mergesort2(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        self.assertEqual(mergesort_rec_2(arr), [3, 4, 7, 9, 42, 69, 420])
