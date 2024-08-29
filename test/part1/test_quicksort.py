import unittest
from src.part1.quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        arr = [100, 90, 3, 7, 4, 69, 420, 42]
        quicksort(arr)
        self.assertEqual(arr, [3, 4, 7, 42, 69, 90, 100, 420])
    
    def test_quicksort2(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        quicksort(arr)
        self.assertEqual(arr, [3, 4, 7, 9, 42, 69, 420])
