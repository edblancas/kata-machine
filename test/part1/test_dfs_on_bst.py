from src.part1.dfs_on_bst import dfs, insert, delete
import unittest
from src.util.tree import tree_factory
from src.part1.binary_tree_in_order import in_order_bst

class TestDFSOnBST(unittest.TestCase):
    def setUp(self):
        self.tree = tree_factory()

    def test_dfs_on_bst(self):
        self.assertTrue(dfs(self.tree, 45))
        self.assertTrue(dfs(self.tree, 7))
        self.assertFalse(dfs(self.tree, 69))

    def test_insertion_on_bfs(self):
        insert(self.tree, 101)
        self.assertEqual(in_order_bst(self.tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 100, 101])

    def test_delete_leaf(self):
        # 7 is a leaf node in this tree.
        new_tree = delete(self.tree, 7)
        self.assertFalse(dfs(new_tree, 7))
        self.assertEqual(in_order_bst(new_tree), [5, 10, 15, 20, 29, 30, 45, 50, 100])

    def test_delete_node_with_one_child(self):
        # Insert 101 so that node 100 gets a right child.
        insert(self.tree, 101)
        new_tree = delete(self.tree, 100)
        self.assertFalse(dfs(new_tree, 100))
        # The expected in‑order traversal now is:
        # [5, 7, 10, 15, 20, 29, 30, 45, 50, 101]
        self.assertEqual(in_order_bst(new_tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 101])

    def test_delete_node_with_two_children(self):
        # Deleting 45, which has two children, should replace it with its in‑order successor.
        new_tree = delete(self.tree, 45)
        self.assertFalse(dfs(new_tree, 45))
        # The expected in‑order traversal after deletion:
        # [5, 7, 10, 15, 20, 29, 30, 50, 100]
        self.assertEqual(in_order_bst(new_tree), [5, 7, 10, 15, 20, 29, 30, 50, 100])

    def test_delete_nonexistent(self):
        # Deleting a value not present in the tree should leave the tree unchanged.
        new_tree = delete(self.tree, 999)
        self.assertEqual(in_order_bst(new_tree), [5, 7, 10, 15, 20, 29, 30, 45, 50, 100])

