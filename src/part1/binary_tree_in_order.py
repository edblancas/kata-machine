def in_order_bst(root):
    path = []
    def walk(node):
        if node is None:
            return
        walk(node.left)
        path.append(node.value)
        walk(node.right)
        return path
    return walk(root)
