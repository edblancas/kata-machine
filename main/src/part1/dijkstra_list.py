from src.util.graph import WeightedAdjacencyList
from heapq import heappop, heappush

# Primeagen says that a question in interviews is the count the no. of islands

# O((|V|+|E|)log|V|) time
# - We use a set to get the unvisited/processed nodes/vertices O(|V|), the while
# - We get the minimum from heap O(log|V|)
# - As we use an adjecency list we visit all the edges O(|E|), the for loop
# - and update distance O(log|V|)
# So, O(|V|*log|V| + |E|*log|V|) = O((|V| + |E|) * log|V|)

# We could add two paths for the same node with differnt cost to the min heap,
# we always get the minimum, but then the size of the heap will be |E| and NOT
# |V|.

# So we need to update cost for that path in the min heap, for that we need the
# implementation of update will need a map to keep the index of the node as K
# and as V the nodes of the heap, i.e. (cost, idx_node), then heapify up/down.
# How to heapify if the node is one in the middle of the tree?
# https://stackoverflow.com/questions/46996064/how-to-update-elements-within-a-heap-priority-queue
# As we only update when the cost decreases, then we only need to fix the upper
# tree thus heapify up.

def dijkstra_list(source: int, sink: int, adj_list: WeightedAdjacencyList) -> list[int]:
    return []

def dijkstra_dict(start: str, end: str, adj_list: dict[str, dict[str, int]]) -> list[str]:
    prev = {}
    processed = set()
    min_heap = [(0, start)]  # cost 0 to get to start from start
    min_distances = {k: float('inf') for k in adj_list}

    while min_heap:
        distance_curr, curr = heappop(min_heap)
        if curr in processed: continue
        for neighbor in adj_list[curr]:
            # improvement, do not add to the heap
            if neighbor in processed: continue
            new_distance_to_neighbor = distance_curr + adj_list[curr][neighbor]
            # if we include >= then if two paths have the same cost will take the last discovered
            if min_distances[neighbor] > new_distance_to_neighbor:
                min_distances[neighbor] = new_distance_to_neighbor
                # set curr to the partent of neighbor
                prev[neighbor] = curr
                heappush(min_heap, (new_distance_to_neighbor, neighbor))
        processed.add(curr)

    # we could use a queue for better performance but the complexity time will not change
    path = []
    # if we found a path to end
    if end in prev:
        curr = end
        # if the K doesnt exist return None, with dict[K] will raise an error
        while prev.get(curr):
            path.append(curr)
            curr = prev[curr]

        # as the start has no parent, that is where the while stops
        # then we add it here
        path.append(start)
        path.reverse()

    return path

