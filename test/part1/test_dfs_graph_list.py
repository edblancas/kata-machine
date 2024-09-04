import unittest
from test.util.graph import list2
from src.part1.dfs_graph_list import dfs

class TestDFSGraphList(unittest.TestCase):
    def test_dfs_graph_list(self):
        self.assertEqual(dfs(list2, 0, 6), [0, 1, 4, 5, 6])
        self.assertEqual(dfs(list2, 6, 0), None)
