from src.part1.recursion_maze_solver import solve as maze_solver
import unittest
from src.util.local_types import Point

class TestRecursionMazeSolver(unittest.TestCase):
    def test_recursion_maze_solver(self):
        maze = [
            "xxxxxxxxxx x",
            "x        x x",
            "x        x x",
            "x xxxxxxxx x",
            "x          x",
            "x xxxxxxxxxx",
        ]

        mazeResult = [
            Point(x=10, y=0),
            Point(x=10, y=1),
            Point(x=10, y=2),
            Point(x=10, y=3),
            Point(x=10, y=4),
            Point(x=9, y=4),
            Point(x=8, y=4),
            Point(x=7, y=4),
            Point(x=6, y=4),
            Point(x=5, y=4),
            Point(x=4, y=4),
            Point(x=3, y=4),
            Point(x=2, y=4),
            Point(x=1, y=4),
            Point(x=1, y=5),
        ]

        # there is only one path through
        result = maze_solver(maze, "x", Point(x=10, y=0), Point(x=1, y=5))
        self.assertEqual(drawPath(maze, result), drawPath(maze, mazeResult))

def drawPath(data: list[str], path: list[Point]):
    data2 = list(map(lambda row: list(row), data))
    for p in path:
        if data2[p.y] and data2[p.y][p.x]:
            data2[p.y][p.x] = "*"
    return list(map(lambda row_of_cells: ''.join(row_of_cells), data2))
