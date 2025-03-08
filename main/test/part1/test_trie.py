import unittest
from src.part1.trie import Trie

class TestTrie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.insert("foo")
        trie.insert("fool")
        trie.insert("foolish")
        trie.insert("bar")

        self.assertEqual(sorted(trie.find("foo")), [
            "foo",
            "fool",
            "foolish"
        ])

        trie.delete("fool")

        self.assertEqual(sorted(trie.find('fo')), [
            "foo",
            'foolish'
        ])

        trie.insert('food')

        self.assertEqual(sorted(trie.find('fo')), [
            "foo",
            'food',
            'foolish'
        ])
