import unittest
from src.part1.recursion_sum_of_n import sum_of_n_rec, sum_of_n_tail_rec, sum_of_n_iter

class TestRecSumN(unittest.TestCase):
    def test_sum_n_rec(self):
        self.assertEqual(sum_of_n_rec(3), 6)

    def test_sum_n_tail_rec(self):
        self.assertEqual(sum_of_n_tail_rec(3, 0), 6)

    def test_sum_n_iter(self):
        self.assertEqual(sum_of_n_iter(3, 0), 6)
