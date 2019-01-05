
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data


def level_order_traversal(queue, result):
    if queue:
        node = queue.pop(0)
        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
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
