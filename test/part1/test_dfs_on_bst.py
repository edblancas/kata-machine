from src.part1.dfs_on_bst import dfs, insert
import unittest
from src.util.tree import tree_factory
from src.part1.binary_tree_in_order import in_order_bst

class TestDFSOnBST(unittest.TestCase):
    def setUp(self):
        self.tree = tree_factory()

    def test_dfs_on_bst(self):
        self.assertTrue(dfs(self.tree, 45))
        self.assertTrue(dfs(self.tree, 7))
        self.assertFalse(dfs(self.tree, 69))

    def test_insertion_on_bfs(self):
        insert(self.tree, 101)
        self.assertEqual(in_order_bst(self.tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 100, 101])
