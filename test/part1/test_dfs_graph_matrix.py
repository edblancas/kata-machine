import unittest
from test.util.graph import matrix2
from src.part1.dfs_graph_matrix import dfs

class TestDFSGraphMatrix(unittest.TestCase):
    def test_dfs_graph_matrix(self):
        self.assertEqual(dfs(matrix2, 0, 6), [0, 1, 4, 5, 6])
        self.assertEqual(dfs(matrix2, 6, 0), None)

if __name__ == '__main__':
    unittest.main()
