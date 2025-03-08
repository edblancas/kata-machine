# with Depth-First implement find, insert,and delete of a binary search tree aka BST.
# remember the property of a binary search tree:
#  all to the left of the root is <=
#  all to the right of the root is >
#  the same applies to every node
from src.util.local_types import BinaryNode

def dfs(head: BinaryNode, needle: int) -> bool:
    return search(head, needle)

def search(head: BinaryNode | None, needle: int) -> bool:
    if head is None:
        return False
    if head.value == needle:
        return True
    return search(head.left, needle) or search(head.right, needle)

def insert(head, value):
    if value <= head.value:
        if head.left:
            insert(head.left, value)
        else:
            head.left = BinaryNode(value)
    else:
        if head.right:
            insert(head.right, value)
        else:
            head.right = BinaryNode(value)

def get_min(node: BinaryNode) -> BinaryNode:
    """Helper: returns the node with the minimum value in a (non-empty) subtree."""
    current = node
    while current.left:
        current = current.left
    return current

def delete(head: BinaryNode | None, value: int) -> BinaryNode | None:
    """
    Deletes the node with the given value from the BST.
    Returns the new (sub)tree root.
    """
    if head is None:
        return None
    if value < head.value:
        head.left = delete(head.left, value)
    elif value > head.value:
        head.right = delete(head.right, value)
    else:
        # Node found.
        if head.left is None:
            return head.right
        elif head.right is None:
            return head.left
        else:
            # Node with two children: use the in‑order successor (minimum in right subtree)
            min_node = get_min(head.right)
            head.value = min_node.value
            head.right = delete(head.right, min_node.value)
    return head
