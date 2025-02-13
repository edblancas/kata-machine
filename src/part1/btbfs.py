# breath first search ona binary tree
from src.util.local_types import BinaryNode
from collections import deque

def bfs(head: BinaryNode) -> list[int]:
    q = deque([head])
    path = []

    while q:
        next = q.popleft()

        path.append(next.value)

        if next.left: q.append(next.left)
        if next.right: q.append(next.right)

    return path


def bfs_find(head: BinaryNode, needle: int) -> bool:
    q = deque([head])
    
    while q:
        next = q.popleft()
        if not next: continue

        if next.value == needle: return True
        q.append(next.left)
        q.append(next.right)

    return False
