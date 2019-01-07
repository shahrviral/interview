class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root:
            self._insert([self.root], data)
        else:
            self.root = Node(data)

    def _insert(self, queue, data):
        if queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = Node(data)
            elif node.right is None:
                node.right = Node(data)
            else:
                queue.append(node.left)
                queue.append(node.right)
                self._insert(queue, data)

    def traverse(self):
        return self.level_order_traversal([self.root], [])

    def level_order_traversal(self, queue, result):
        if queue:
            node = queue.pop(0)
            if node is not None:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                result.append(node)
            result = self.level_order_traversal(queue, result)
        return result


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert('a')
    bt.insert('b')
    bt.insert('c')
    bt.insert('d')
    print(bt.traverse())
