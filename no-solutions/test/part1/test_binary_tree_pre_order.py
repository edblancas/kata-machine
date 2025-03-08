import unittest
from src.part1.binary_tree_pre_order import pre_order_search
from src.util.tree import tree

class TestPreOrder(unittest.TestCase):
    def test_pre_order(self):
        self.assertEqual(pre_order_search(tree), [20, 10, 5, 7, 15, 50, 30, 29, 45, 100])
