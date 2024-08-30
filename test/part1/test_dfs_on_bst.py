from src.part1.dfs_on_bst import dfs
import unittest
from src.util.tree import tree

class TestDFSOnBST(unittest.TestCase):
    def test_dfs_on_bst(self):
        self.assertTrue(dfs(tree, 45))
        self.assertTrue(dfs(tree, 7))
        self.assertFalse(dfs(tree, 69))
