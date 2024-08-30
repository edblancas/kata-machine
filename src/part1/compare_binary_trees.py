# Comparing two binary trees to see if they are equal in both shape and structure
# DFS preserves the shape of the traversal, BFS not

from src.util.local_types import BinaryNode

def compare_binary_trees(head: BinaryNode, head2: BinaryNode) -> bool:
    def compare_binary_trees_rec(node, node2):
        # structural check
        # have we made it to a point in both sub-trees in which we both cannot
        # recurse any further
        # are we both goin' to a null node together

        # that means that we structurally we are the same, cuz we both arrive at a nil together

        # this is the only base case that can ever be hit, we just have to keep
        # hitting nulls, so we know the structure is still the same at this point
        # when we hit the others the sub-tree becomes invalid, and
        # the whole tree becomes invalid
        if node is None and node2 is None:
            return True

        # strucural check
        # this means we structurally are not the same, cuz if one of us is null and
        # the other one is a node, we traverse to the same point and have different
        # structure

        # at this point we know that one of the nodes should be None and the other
        # not, this cuz the first check
        if  node is None or node2 is None:
            return False

        # value check
        # at this node we know that both nodes are not None
        if node.value != node2.value:
            return False

        # combine our left sub-tree with our right-subtree, ass long as they
        # are true we are true
        return compare_binary_trees_rec(node.left, node2.left) and \
            compare_binary_trees_rec(node.right, node2.right)

    return compare_binary_trees_rec(head, head2)
