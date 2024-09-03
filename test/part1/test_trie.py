import unittest
from src.part1.trie import Trie

class TestTrie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.insert("foo")
        trie.insert("fool")
        trie.insert("foolish")
        trie.insert("bar")

        self.assertEqual(trie.find("foo").sort(), [
            "foo",
            "fool",
            "foolish"
        ])

        trie .delete("fool")

        self.assertEqual(trie.find('fo').sort(), [
            "foo",
            'foolish'
        ])
