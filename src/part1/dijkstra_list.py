from src.util.graph import WeightedAdjacencyList
from heapq import heappop, heappush

# no tests
def dijkstra_list(source: int, sink: int, adj_list: WeightedAdjacencyList) -> list[int]:
    return []

def dijkstra_dict(start: str, end: str, adj_list: dict[str, dict[str, int]]) -> list[str]: ...
