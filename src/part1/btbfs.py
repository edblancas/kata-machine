# breath first search ona binary tree
from src.util.local_types import BinaryNode
from collections import deque

def bfs(head: BinaryNode) -> list[int]:
    q = deque()
    q.append(head)
    path = []
    while q:
        curr = q.popleft()
        if not curr: continue
        path.append(curr.value)
        q.append(curr.left)
        q.append(curr.right)
    return path

def bfs_find(head: BinaryNode, needle: int) -> bool:
    q = deque()
    q.append(head)
    while q:
        curr = q.popleft()
        if not curr: continue
        if curr.value == needle: return True
        q.append(curr.left)
        q.append(curr.right)
    return False
