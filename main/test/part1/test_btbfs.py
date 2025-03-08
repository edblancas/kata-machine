import unittest
from src.util.tree import tree
from src.part1.btbfs import bfs, bfs_find

class TestBTBFS(unittest.TestCase):
    def test_btbst_path(self):
        self.assertEqual(bfs(tree), [20, 10, 50, 5, 15, 30, 100, 7, 29, 45])

    def test_btbst_find(self):
        self.assertTrue(bfs_find(tree, 45))
        self.assertTrue(bfs_find(tree, 7))
        self.assertFalse(bfs_find(tree, 69))
