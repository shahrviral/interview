
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def search(root, data):
    if root.data == data:
        return True
    if root.left:
        return search(root.left, data)
    if root.right:
        return search(root.right, data)
    return False


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
    print(search(root, 'V'))
    print(search(root, 'D'))
    print(search(root.right, 'E'))

