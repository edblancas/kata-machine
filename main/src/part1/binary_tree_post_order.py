def post_order_bst(head):
    path = []
    def post_order_bst_rec(node):
        if not node:
            return
        post_order_bst_rec(node.left)
        post_order_bst_rec(node.right)
        path.append(node.value)
    post_order_bst_rec(head)
    return path
