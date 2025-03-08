from src.util.local_types import BinaryNode

# get the head or root and return the visited values of the nodes
def pre_order_search(head: BinaryNode) -> list[int]:
    path = []
    def walk(curr):
        if curr is None:
            return
        path.append(curr.value)
        walk(curr.left)
        walk(curr.right)
    walk(head)
    return path
