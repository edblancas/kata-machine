from src.util.local_types import BinaryNode

# get the head or root and return the visited values of the nodes
def pre_order_search(head: BinaryNode) -> list[int]:
    path = []
    def pre_order_search_aux(node):
        if not node:
            return
        path.append(node.value)
        pre_order_search_aux(node.left)
        pre_order_search_aux(node.right)
    pre_order_search_aux(head)
    return path
