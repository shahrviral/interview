class Node:
    def __init__(self, data=None, left=None, right=None):
        pass

    def __repr__(self):
        return str(self.data)


class BinaryTree:

    def __init__(self, root=None):
        pass

    def insert(self, data):
        pass

    def _insert(self, queue, data):
        pass

    def traverse(self):
        pass

    def level_order_traversal(self, queue, result):
        pass


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert('a')
    bt.insert('b')
    bt.insert('c')
    bt.insert('d')
    print(bt.traverse())
