import unittest
from src.part1.dijkstra_list import dijkstra_dict
from test.util.graph import dijksra_graph_dict

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        self.assertEqual(dijkstra_dict("book", 'piano', dijksra_graph_dict),
                         ['book', 'lp', 'drums', 'piano'])
