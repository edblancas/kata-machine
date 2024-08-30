def in_order_bst(root):
    path = []
    def in_order_bst_aux(node):
        if not node:
            return
        in_order_bst_aux(node.left)
        path.append(node.value)
        in_order_bst_aux(node.right)
    in_order_bst_aux(root)
    return path
