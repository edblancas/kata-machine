import unittest
from src.part1.stack import LinkedListStack, ArrayStack

class TestStack(unittest.TestCase):
    def test_linked_list_stack(self):
        stack = LinkedListStack()
        self._test(stack)

    def test_array_list_stack(self):
        stack = ArrayStack()
        self._test(stack)

    def _test(self, stack):
        stack.push(5)
        stack.push(7)
        stack.push(9)

        self.assertEqual(stack.pop(), 9)
        self.assertEqual(stack.length, 2)

        stack.push(11)
        self.assertEqual(stack.pop(), 11)
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), None)

        # just wanted to make sure that I could not blow up myself when i remove
        # everything
        stack.push(69)
        self.assertEqual(stack.peek(), 69)
        self.assertEqual(stack.length, 1)
