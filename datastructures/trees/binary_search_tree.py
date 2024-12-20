import sys


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        pass

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self, root=None):
        pass

    def insert(self, data):
        pass

    def _insert(self, current_node, data):
        pass
        # If same data passed in, don't do anything

    def height(self):
        pass

    def _height(self, current_node, current_height):
        pass

    def contains(self, data):
        pass

    def _contains(self, current_node, data):
        pass

    def find(self, data):
        pass

    def _find(self, current_node, data):
        pass

    def delete(self, data):
        pass

    def _delete(self, node):
        pass

    def print_tree(self, traversal='in-order'):

        if traversal == 'in-order':
            print(self.in_order_traversal(self.root, []))
        elif traversal == 'pre-order':
            print(self.pre_order_traversal(self.root, []))
        elif traversal == 'post-order':
            print(self.post_order_traversal(self.root, []))
        elif traversal == 'level-order':
            print(self.in_order_traversal([self.root], []))

    def pre_order_traversal(self, node, result):
        pass

    def in_order_traversal(self, node, result):
        pass

    def post_order_traversal(self, node, result):
        pass

    def level_order_traversal(self, queue, result):
        pass

    @staticmethod
    def find_min_node(node):
        """ Find in order successor of node"""
        pass

    @staticmethod
    def get_number_of_children(node):
        pass

def validate_binary_search_tree(root, min=-sys.maxsize, max=sys.maxsize):
    pass


if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in [50, 30, 40, 20, 70, 60, 80]:
        bst.insert(i)
    bst.print_tree()
    bst.delete(40)
    bst.print_tree()
    print(bst.height())
    print(bst.contains(60))
    print(validate_binary_search_tree(bst.root))
