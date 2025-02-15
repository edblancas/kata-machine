from src.util.graph import WeightedAdjacencyList
from heapq import heappop, heappush, heapify
from collections import deque

# no tests
def dijkstra_list(source: int, sink: int, adj_list: WeightedAdjacencyList) -> list[int]:
    return []

def dijkstra_dict(start: str, end: str, adj_list: dict[str, dict[str, int]]) -> list[str]:
    seen = set()
    prev = dict()
    dist = dict()
    lowest = [(0, start)]
    heapify(lowest)

    while lowest:
        curr_dist, curr = heappop(lowest)
        seen.add(curr)
        if curr == end:
            break

        adj_to_curr = adj_list[curr]
        for next, next_weight in adj_to_curr.items():
            if next in seen:
                continue
            dist_to_next = curr_dist + next_weight
            if dist_to_next < dist.get(next, float('inf')):
                dist[next] = dist_to_next
                prev[next] = curr
                heappush(lowest, (dist_to_next, next))

    print(prev)
    if prev.get(end) is None:
        return []

    curr = end
    path = deque()
    while prev.get(curr):
        path.appendleft(curr)
        curr = prev[curr]

    path.appendleft(start)

    return list(path)
