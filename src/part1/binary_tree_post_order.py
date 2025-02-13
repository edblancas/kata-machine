def post_order_bst(head):
    path = []
    def walk(curr):
        if not curr: return
        walk(curr.left)
        walk(curr.right)
        path.append(curr.value)
    walk(head)
    return path
