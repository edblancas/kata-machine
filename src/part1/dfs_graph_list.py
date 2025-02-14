from src.util.graph import GraphEdge, WeightedAdjacencyList

def dfs(graph: WeightedAdjacencyList, source: int, needle: int) -> list[int] | None:
    path = []
    visited = set()

    def walk(curr):
        if curr == needle:
            path.append(curr)
            return True
        if curr in visited:
            return False

        visited.add(curr)
        path.append(curr)

        adj_to_curr = graph[curr]
        for next in adj_to_curr:
            if walk(next.to):
                return True

        path.pop()
        return False

    walk(source)
    return path or None
