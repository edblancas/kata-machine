from src.util.local_types import Point

# we could use a class Point or just a tuple with (x, y)
def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    visited = set()
    path = []
    def is_end(row, col):
        return row == end.y and col == end.x

    def cant_walk(row, col):
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
            return True
        if Point(col, row) in visited:
            return True
        if maze[row][col] == 'x':
            return True
        return False

    def walk(row, col):
        if cant_walk(row, col):
            return False
        if is_end(row, col):
            path.append(Point(col, row))
            return True

        path.append(Point(col, row))
        visited.add(Point(col, row))

        for rown, coln in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if walk(row + rown, col+ coln):
                return True

        path.pop()
        return False

    walk(start.y, start.x)
    print(path)
    return path

