from src.util.graph import WeightedAdjacencyList
from collections import deque

def bfs(graph: WeightedAdjacencyList, source: int, needle: int) -> list[int] | None:
    queue = deque([source])
    processed = set()
    parent = [-1] * len(graph)
    while queue:
        curr = queue.popleft()
        if curr in processed:
            continue
        if needle == curr:
            break
        processed.add(curr)
        for neighbor in graph[curr]:
            if neighbor.to in processed:
                continue
            queue.append(neighbor.to)
            parent[neighbor.to] = curr

    path: deque[int] = deque([needle])
    curr = parent[needle]
    if curr == -1:
        return None
    while curr != -1:
        path.appendleft(curr)
        curr = parent[curr]
    return list(path)
