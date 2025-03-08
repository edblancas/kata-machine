import unittest
from src.util.tree import tree
from src.part1.binary_tree_in_order import in_order_bst

class TestInOrderBinaryTree(unittest.TestCase):
    def test_in_order(self):
        self.assertEqual(in_order_bst(tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 100])
