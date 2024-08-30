# breath first search ona binary tree
from src.util.local_types import BinaryNode
from collections import deque

def bfs(head: BinaryNode) -> list[int]:
    path = []
    q: deque = deque()
    # append at the tail
    q.append(head)
    while len(q) > 0:
        node = q.popleft()
        path.append(node.value)
        if node.left:
            q.append(node.left) 
        if node.right:
            q.append(node.right) 

    return path
