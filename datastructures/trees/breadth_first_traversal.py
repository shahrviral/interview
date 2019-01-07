from binary_search_tree import Node


def level_order_traversal(queue, result):
    if queue:
        node = queue.pop(0)
        if node is not None:
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            result.append(node)
        result = level_order_traversal(queue, result)
    return result


if __name__ == '__main__':
    root = Node('A')
    queue = [root]
    root.left = Node('B')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.left.left = Node('G')
    root.left.right.right = Node('H')
    root.right = Node('C')
    root.right.right = Node('F')
    root.right.right.left = Node('I')

    print('Level-Order Traversal', level_order_traversal([root], []))
