from src.util.local_types import Point
from dataclasses import astuple

# we could use a class Point or just a tuple with (x, y)
def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = set()
    path = []
    def solve_aux(curr):
        if curr.y < 0 or curr.y >= len(maze):
            return False
        if curr.x < 0 or curr.x >= len(maze[0]):
            return False
        if maze[curr.y][curr.x] == 'x':
            return False
        if astuple(curr) in visited:
            return False
        if curr == end:
            path.append(curr)
            return True

        visited.add(astuple(curr))
        path.append(curr)

        for d in dirs:
            if solve_aux(Point(curr.x + d[0], curr.y + d[1])):
                return True

        path.pop()
        return False

    solve_aux(start)
    return path
