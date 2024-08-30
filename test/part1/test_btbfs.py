import unittest
from src.util.tree import tree
from src.part1.btbfs import bfs

class TestBTBFS(unittest.TestCase):
    def test_btbst_path(self):
        self.assertEqual(bfs(tree), [20, 10, 50, 5, 15, 30, 100, 7, 29, 45])
