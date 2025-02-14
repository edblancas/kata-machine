# return the path that we took to the needle node or None if not found
from collections import deque

def bfs(adj_matrix: list[list[int]], source: int, needle: int) -> list[int] | None:
    q = deque([source])
    visited = set()
    prev = dict()

    while q:
        curr = q.popleft()
        visited.add(curr)
        if curr == needle:
            break
        for next, weight in enumerate(adj_matrix[curr]):
            if not weight:
                continue
            if next in visited:
                continue
            prev[next] = curr
            q.append(next)

    if not prev.get(needle):
        return None

    curr = needle
    path = deque()
    while prev.get(curr) != None:
        path.appendleft(curr)
        curr = prev[curr]

    path.appendleft(source)

    return list(path)
