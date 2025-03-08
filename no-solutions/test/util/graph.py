#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)
matrix2: list[list[int]] = [
    [0, 3, 1,  0, 0, 0, 0],  # 0
    [0, 0, 0,  0, 1, 0, 0],
    [0, 0, 7,  0, 0, 0, 0],
    [0, 0, 0,  0, 0, 0, 0],
    [0, 1, 0,  5, 0, 2, 0],
    [0, 0, 18, 0, 0, 0, 1],
    [0, 0, 0,  1, 0, 0, 1],
]

from src.util.graph import WeightedAdjacencyList, GraphEdge

list2: WeightedAdjacencyList = [[None] for _ in range(7)]

#     >(1)<--->(4) ---->(5)
#    /          |       /|
# (0)     ------|------- |
#    \   v      v        v
#     >(2) --> (3) <----(6)
list2[0] = [
    GraphEdge(1, 3),
    GraphEdge(to= 2, weight= 1)
]
list2[1] = [
    GraphEdge(to= 4, weight= 1)
]
list2[2] = [
    GraphEdge(to= 3, weight= 7)
]
list2[3] = [ ]
list2[4] = [
    GraphEdge(to= 1, weight= 1),
    GraphEdge(to= 3, weight= 5),
    GraphEdge(to= 5, weight= 2)
]
list2[5] = [
    GraphEdge(to= 2, weight= 18),
    GraphEdge( to= 6, weight= 1)
]
list2[6] = [
    GraphEdge(to= 3, weight= 1)
]

dijksra_graph_dict = {
    'book': {'lp': 5, 'poster': 0},
    'lp': {'bass guitar': 15, 'drums': 20},
    'poster': {'bass guitar': 30, 'drums': 35},
    'bass guitar': {'piano': 20, 'poster':0},
    'drums': {'piano': 10},
    'piano': {}
}
