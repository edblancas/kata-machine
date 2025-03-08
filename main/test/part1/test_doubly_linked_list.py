import unittest
from src.part1.doubly_linked_list import DoublyLinkedList
from test.util.test_list import test_insert_at_double_linked_list

class TestDoublyLinkedList(unittest.TestCase):
    def test_doubly_linked_list(self):
        list = DoublyLinkedList()
        test_insert_at_double_linked_list(self, list)
