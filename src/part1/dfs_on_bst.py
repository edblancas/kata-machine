# with Depth-First implement find, insert,and delete of a binary search tree aka BST.
# remember the property of a binary search tree:
#  all to the left of the root is <=
#  all to the right of the root is >
#  the same applies to every node
from src.util.local_types import BinaryNode

def dfs(head: BinaryNode, needle: int) -> bool:
    return search(head, needle)

def search(head: BinaryNode | None, needle: int) -> bool:
    if not head:
        return False

    if head.value == needle:
        return True

    # we dont need both ifs
    # also the out is wrong cuz we are searching both side
    # the whole point is just search one side
    # if needle <= head.value:
        # out = search(head.left, needle)
    # elif needle > head.value:
        # out = search(head.right, needle)
    if needle <= head.value:
        return search(head.left, needle)

    return search(head.right, needle)
