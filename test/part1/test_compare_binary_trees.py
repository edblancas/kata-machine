import unittest
from src.util.tree import tree, tree2
from src.part1.compare_binary_trees import compare_binary_trees

class TestCompareBinaryTree(unittest.TestCase):
    def test_compare_binary_tree(self):
        self.assertFalse(compare_binary_trees(tree, tree2))
        self.assertTrue(compare_binary_trees(tree, tree))
