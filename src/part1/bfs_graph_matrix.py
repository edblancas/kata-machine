# return the path that we took to the needle node or None if not found
from collections import deque

def bfs(adj_matrix: list[list[int]], source: int, needle: int) -> list[int] | None: ...
