class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        pass

    def add(self, data):
        pass

    def size(self):
        pass

    def search(self):
        pass

    def contains(self, data):
        pass

    def delete(self, data):
        pass

    def append(self, data):
        pass

    def insert(self, data, index):
        pass

    def insert_after(self, node, data):
        pass

    def insert_before(self, node, data):
        pass

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return '->'.join(node.data for node in nodes)