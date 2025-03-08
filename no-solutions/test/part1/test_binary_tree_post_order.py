import unittest
from src.part1.binary_tree_post_order import post_order_bst
from src.util.tree import tree

class TestPostOrder(unittest.TestCase):
    def test_post_order(self):
        self.assertEqual(post_order_bst(tree), [7, 5, 15, 10, 29, 45, 30, 100, 50, 20])
