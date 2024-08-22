import unittest
import math
import random

from src.part1.two_crystal_balls import two_crystal_balls

class TestTwoCrystalBalls(unittest.TestCase):
    def test_two_crystal_balls(self):
        """
        two crystal balls
        """
        idx = math.floor(random.random() * 10_000)
        data = [False] * 10_000

        for i in range(idx, len(data)):
            data[i] = True

        self.assertEqual(two_crystal_balls(data), idx)
        self.assertEqual(two_crystal_balls([False] * 821), -1)

if __name__ == '__main__':
    unittest.main()
