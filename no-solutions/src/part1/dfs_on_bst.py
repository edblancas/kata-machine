# with Depth-First implement find, insert,and delete of a binary search tree aka BST.
# remember the property of a binary search tree:
#  all to the left of the root is <=
#  all to the right of the root is >
#  the same applies to every node
from src.util.local_types import BinaryNode

def dfs(head: BinaryNode, needle: int) -> bool:
    return search(head, needle)

def search(head: BinaryNode | None, needle: int) -> bool: ...

def insert(head, value): ...

def delete(head: BinaryNode | None, value: int) -> BinaryNode | None:...
