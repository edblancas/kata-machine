# Comparing two binary trees to see if they are equal in both shape and structure
# DFS preserves the shape of the traversal, BFS not

from src.util.local_types import BinaryNode

def compare_binary_trees(head: BinaryNode, head2: BinaryNode) -> bool:
    if head is None and head2 is None:
        return True
    if head is None or head2 is None:
        return False
    if head.value != head2.value:
        return False
    return (compare_binary_trees(head.left, head2.left) and 
            compare_binary_trees(head.right, head2.right))
