from dataclasses import dataclass

@dataclass
class GraphEdge:
    to: int
    weight: int

type WeightedAdjacencyList = list[GraphEdge]
