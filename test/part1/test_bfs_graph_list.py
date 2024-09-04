import unittest
from src.part1.bfs_graph_list import bfs
from test.util.graph import list2

class TestBFSGraphList(unittest.TestCase):
    def test_bfs_graph_list(self):
        self.assertEqual(bfs(list2, 0, 6), [0, 1, 4, 5, 6])
        self.assertEqual(bfs(list2, 6, 0), None)
