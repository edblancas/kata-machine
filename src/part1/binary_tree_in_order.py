def in_order_bst(root):
    path = []
    def walk(curr):
        if not curr:
            return 
        walk(curr.left)
        path.append(curr.value)
        walk(curr.right)
        return path

    return walk(root)
