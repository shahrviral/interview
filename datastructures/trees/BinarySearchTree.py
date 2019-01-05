import sys


class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return str(self.data)


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert(self, data):
        if self.root:
            self._insert(self.root, data)
        else:
            self.root = Node(data)
        self.size += 1

    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left:
                self._insert(current_node.left, data)
            else:
                current_node.left = Node(data)
                current_node.left.parent = current_node
        elif data > current_node.data:
            if current_node.right:
                self._insert(current_node.right, data)
            else:
                current_node.right = Node(data)
                current_node.right.parent = current_node
        # If same data passed in, don't do anything

    def height(self):
        if self.root:
            return self._height(self.root, 0)
        return 0

    def _height(self, current_node, current_height):
        if current_node:
            left_height = self._height(current_node.left, current_height + 1)
            right_height = self._height(current_node.right, current_height + 1)
            return max(left_height, right_height)
        return current_height

    def search(self, data):
        return self._search(self.root, data) if self.root else False

    def _search(self, current_node, data):
        if data == current_node.data: return True
        if data < current_node.data and current_node.left:
            return self._search(current_node.left, data)
        elif data > current_node.data and current_node.right:
            return self._search(current_node.right, data)
        return False

    def find(self, data):
        if self.root:
            return self._find(self.root, data)

    def _find(self, current_node, data):
        if current_node.data == data:
            return current_node
        elif data < current_node.data and current_node.left:
            return self._find(current_node.left, data)
        elif data > current_node.data and current_node.right:
            return self._find(current_node.right, data)

    def delete(self, data):

        node = self.find(data)
        self._delete(node)

    def _delete(self, node):

        if node:

            node_parent = node.parent

            node_children_count = BinarySearchTree.get_number_of_children(node)

            # CASE 1 (node has no children)
            if node_children_count == 0:

                if node_parent:
                    # remove reference to node from parent node
                    if node_parent.left == node:
                        node_parent.left = None
                    else:
                        node_parent.right = None
                else:
                    self.root = None

            # CASE 2 (node has either left or right child)
            if node_children_count == 1:

                # get child node
                child = node.left if node.left else node.right

                if node_parent:
                    # replace parent node's reference to deleted node with deleted node's child
                    if node_parent.left == node:
                        node_parent.left = child
                    else:
                        node_parent.right = child
                else:
                    self.root = None
                # replace child's parent pointer with deleted node's parent pointer
                child.parent = node_parent

            # CASE 3 (node has 2 children) recursive case
            if node_children_count == 2:
                # Get in order successor of the node to be deleted, smallest value greater than node
                successor = BinarySearchTree.find_min_node(node.right)

                # copy value of successor to node
                node.data = successor.data

                self._delete(successor)

    def print_tree(self):
        print(self.in_order_traversal(self.root, []))

    def in_order_traversal(self, node, result):
        if node:
            result = self.in_order_traversal(node.left, result)
            result.append(node)
            result = self.in_order_traversal(node.right, result)
        return result

    @staticmethod
    def find_min_node(node):
        """ Find in order successor of node"""
        current = node
        while current.left:
            print(current)
            current = current.left
        return current

    @staticmethod
    def get_number_of_children(node):
        count = 0
        if node.left: count += 1
        if node.right: count += 1
        return count


def validate_binary_search_tree(root, min=-sys.maxsize, max=sys.maxsize):
    if root:
        return min < root.data < max and \
               validate_binary_search_tree(root.left, min, root.data) and \
               validate_binary_search_tree(root.right, root.data, max)

    return True


if __name__ == '__main__':
    # bst = BinarySearchTree(None)
    # bst.insert(35)
    # bst.insert(28)
    # bst.insert(22)
    # bst.insert(17)
    # bst.insert(24)
    # bst.insert(44)
    # bst.insert(30)
    # bst.insert(58)
    # bst.insert(6)
    # bst.insert(60)
    # bst.insert(20)
    # bst.insert(50)
    # bst.print_tree()
    # print(bst.search(22))
    # print(bst.search(100))
    bst = BinarySearchTree()
    for i in [50, 30, 40, 20, 70, 60, 80]:
        bst.insert(i)
    bst.print_tree()
    bst.delete(40)
    bst.print_tree()
    print(bst.height())
    print(bst.search(60))
    print(validate_binary_search_tree(bst.root))
