import unittest

from part1.linear_search import linear_search as linear_fn


class TestSum(unittest.TestCase):
    def test_linear_search(self):
        """
        linear search array
        """
        foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        result = linear_fn(foo, 69)
        self.assertTrue(result)
        self.assertEqual(linear_fn(foo, 1336), False)
        self.assertEqual(linear_fn(foo, 69420), True)
        self.assertEqual(linear_fn(foo, 69421), False)
        self.assertEqual(linear_fn(foo, 1), True)
        self.assertEqual(linear_fn(foo, 0), False)

if __name__ == '__main__':
    unittest.main()
