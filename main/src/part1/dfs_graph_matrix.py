# the easiest way is to convert the matrix to a adj list
# but can be done like in the maze solver
def dfs(graph: list[list[int]], source: int, needle: int) -> list[int] | None:
    processed = set()
    path = []

    def dfs_rec(curr: int):
        if curr == needle:
            path.append(curr)
            return True
        if curr in processed:
            return False
        processed.add(curr)
        path.append(curr)
        for neighbor, weight in enumerate(graph[curr]):
            # improvement so dont go one more level deep in the call stack
            # and return until the base cases
            if neighbor in processed: continue
            if weight > 0 and dfs_rec(neighbor):
                return True
        path.pop()

    dfs_rec(source)
    return path or None
