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

# this is a bit complicated cuz we need a mix of the base case with the 
# recursion step, so this get hairy really fast if you start running into
# this weird conditions
# options for this:
# - send a parent to the recursive call
# - do a condition in the base case for null check
def insert(head, value):
    if value <= head.value:
        if not head.left:
            head.left = BinaryNode(value)
        else:
            insert(head.left, value)
    else:
        if not head.right:
            head.right = BinaryNode(value)
        else:
            insert(head.right, value)

# cases:
# 1. node is a leaf, i.e. with no children: just delete it
# 2. node has one child: set parent to child
# 3. node with two children: we need to reduce our case to either 1 or 2,
#   Can do either one, or take a decicion based in the height, e.g. the one with the
#   greater heigh so it gets more balanced.
#     - largest element in our smaller side (sub-tree), go first left then all the way right
#     - smallest on the largest side (sub-tree), go first right then all the way left
#   Either one we can garantee one thing, we are gona encounter with one child or null,
#   but still have a left child when going right, in the case of all going left then right,
#   and now we know how to solve it.
# TODO
def delete(head, value):
    pass
