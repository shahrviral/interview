from binary_search_tree import Node


def pre_order_traversal(node, result):
    pass


def in_order_traversal(node, result):
    pass


def post_order_traversal(node, result):
    pass


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
