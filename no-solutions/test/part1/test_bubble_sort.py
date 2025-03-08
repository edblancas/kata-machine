import unittest
from src.part1.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        bubble_sort(arr)
        self.assertEqual(arr, [3, 4, 7, 9, 42, 69, 420])
