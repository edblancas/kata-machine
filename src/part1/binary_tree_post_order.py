def walk(curr, path):
    if curr is None:
        return
    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.value)
    return path

def post_order_bst(head):
    return walk(head, [])
