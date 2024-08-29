from src.util.local_types import Point

# we could use a class Point or just a tuple with (x, y)
def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    path = []
    visited = set()
    def solve_rec(col, row):
        if not can_enter(col, row):
            return False
        p = Point(col, row)
        path.append(p)
        # set visited, str is unmutable
        #maze[row][col] = 'v'
        # use a set instead 
        visited.add(tuple([col, row]))
        if p == end:
            return True
        if solve_rec(col, row - 1) or \
            solve_rec(col + 1, row) or \
            solve_rec(col, row + 1) or \
            solve_rec(col - 1, row):
            return True
        path.pop()
        return False

    def can_enter(col, row):
         # maze[row][col] != 'v' and \
        if row >= 0 and row < len(maze) and \
            col >= 0 and col < len(maze[0]) and \
            (col, row) not in visited and \
            maze[row][col] != 'x':
            return True
        return False

    if solve_rec(start.x, start.y):
        return path

    return []

