import unittest
from src.part1.mergesort import mergesort

class TestMergesort(unittest.TestCase):
    def test_mergesort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        mergesort(arr)
        self.assertEqual(arr, [3, 4, 7, 9, 42, 69, 420])
