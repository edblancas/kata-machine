from src.util.graph import GraphEdge, WeightedAdjacencyList

# O(V + E) time
def dfs(graph: WeightedAdjacencyList, source: int, needle: int) -> list[int] | None:
    path = []
    seen = [False] * len(graph)
    def walk(curr: int) -> bool:
        if seen[curr]:
            return False
        path.append(curr)
        seen[curr] = True
        if curr == needle:
            return True
        for edge in graph[curr]:
            if walk(edge.to):
                return True
        path.pop()
        return False

    walk(source)
    return path if path else None
