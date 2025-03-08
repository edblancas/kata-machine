import unittest
from src.part1.bfs_graph_matrix import bfs
from test.util.graph import matrix2

class TestBFSGraphMatrix(unittest.TestCase):
    def test_bfs_graph_matrix(self):
        self.assertEqual(bfs(matrix2, 0, 6), [0, 1, 4, 5, 6])
        self.assertEqual(bfs(matrix2, 6, 0), None)
