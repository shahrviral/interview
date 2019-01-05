class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data


def pre_order_traversal(node, result):
    if node:
        result.append(node)
        result = pre_order_traversal(node.left, result)
        result = pre_order_traversal(node.right, result)
    return result


def in_order_traversal(node, result):
    if node:
        result = in_order_traversal(node.left, result)
        result.append(node)
        result = in_order_traversal(node.right, result)
    return result


def post_order_traversal(node, result):
    if node:
        result = post_order_traversal(node.left, result)
        result = post_order_traversal(node.right, result)
        result.append(node)
    return result


if __name__ == '__main__':
    root = Node('A')

    root.left = Node('B')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.left.left = Node('G')
    root.left.right.right = Node('H')
    root.right = Node('C')
    root.right.right = Node('F')
    root.right.right.left = Node('I')

    print('Pre-Order Traversal', pre_order_traversal(root, []))
    print()
    print('In-Order Traversal', in_order_traversal(root, []))
    print()
    print('Post-Order Traversal', post_order_traversal(root, []))
