import unittest
from src.part1.singly_linked_list import SinglyLinkedList
from test.util.test_list import test_list

class TestSinglyLinkedList(unittest.TestCase):
    def test_singly_linked_list(self):
        list = SinglyLinkedList()
        test_list(self, list)
