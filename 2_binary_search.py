from math import floor
import unittest

def binary_search(arr, needle) -> bool:
    if len(arr) == 0:
        return False

    hi = len(arr)
    lo = 0

    while lo < hi:
        m = floor(lo + (hi - lo)/2)
        v = arr[m]

        if v > needle:
            hi = m
        elif v < needle:
            lo = m + 1
        else:
            return True

    return False

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(binary_search([0, 1, 2, 3, 4], 4))
        self.assertTrue(binary_search([0, 1, 2, 3, 4], 5))


if __name__ == '__main__':
    unittest.main()
