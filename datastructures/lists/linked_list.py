class Node:
    def __init__(self, data=None, next=None):
        pass

    def __repr__(self):
        pass


class LinkedList:
    def __init__(self):
        pass

    def is_empty(self):
        """Return if LinkedList is empty or not O(1)"""
        pass

    def add(self, data):
        """Add node to beginning of LinkedList O(1)"""
        pass

    def size(self):
        """Return size of LinkedList O(N)"""
        pass

    def ssize(self):
        """Return size of LinkedList O(1)"""
        pass

    def search(self, data):
        """Return index of data if data exists in LinkedList, else throws ValueError O(N)"""
        pass

    def contains(self, data):
        """Return if data is in LinkedList or not O(N)"""
        pass

    def delete(self, data):
        """Delete data from LinkedList O(N)"""
        pass

    def append(self, data):
        """Append data to end of LinkedList O(N)"""
        pass

    def insert(self, data, index):
        """Insert data at index in LinkedList O(N)"""
        pass

    def insert_after(self, node, data):
        """Insert data after given node in LinkedList O(N)"""
        pass

    def insert_before(self, node, data):
        """Insert data after given node in LinkedList O(N)"""
        pass

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current)
            current = current.next
        return '->'.join(node.data for node in nodes)

    def report(self):
        current = self.head
        while current is not None:
            print(f'''--------------------------------------
Current Node: {current}
Next Node: {current.next}
''')
            current = current.next


if __name__ == '__main__':
    pass
