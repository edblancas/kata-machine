import unittest

from part1.binary_search_list import binary_search as binary_fn


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        """
        binary search array
        """
        foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        result = binary_fn(foo, 69)
        self.assertTrue(result)
        self.assertEqual(binary_fn(foo, 1336), False)
        self.assertEqual(binary_fn(foo, 69420), True)
        self.assertEqual(binary_fn(foo, 69421), False)
        self.assertEqual(binary_fn(foo, 1), True)
        self.assertEqual(binary_fn(foo, 0), False)

if __name__ == '__main__':
    unittest.main()
