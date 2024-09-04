# return the path that we took to the needle node or None if not found
from collections import deque

def bfs(adj_matrix: list[list[int]], source: int, needle: int) -> list[int] | None:
    queue = deque([source])
    visited = set()
    prev = [-1] * len(adj_matrix)
    while queue:
        next = queue.popleft()
        visited.add(next)
        if next == needle:
            break
        for idx_node, weight in enumerate(adj_matrix[next]):
            if weight > 0 and idx_node not in visited:
                queue.append(idx_node)
                prev[idx_node] = next

    next = prev[needle]
    path = []
    if next != -1:
        while next != source:
            path.append(next)
            next = prev[next]
        return [source] + list(reversed(path)) + [needle]
    return None
