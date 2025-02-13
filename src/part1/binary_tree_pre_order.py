from src.util.local_types import BinaryNode

# get the head or root and return the visited values of the nodes
def pre_order_search(head: BinaryNode) -> list[int]:
    path = []
    def walk(curr):
        if not curr:
            return

        path.append(curr.value)
        walk(curr.left)
        walk(curr.right)

        return path

    return walk(head)
