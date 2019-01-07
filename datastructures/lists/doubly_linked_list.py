class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        """Return if LinkedList is empty or not O(1)"""
        return not self.head

    def add(self, data):
        """Add node to beginning of LinkedList O(1)"""
        node = Node(data)
        if self.head is not None:
            self.insert_before_node(self.head, node)
        else:
            self.tail = node
            self.head = node
            self.length += 1

    def size(self):
        """Return size of LinkedList O(1)"""
        return self.length

    def search(self, data):
        """Return index of data if data exists in LinkedList, else throws ValueError O(N)"""
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                return position
            else:
                current = current.next
                position += 1
        raise ValueError(f'\'{data}\' not found in LinkedList')

    def contains(self, data):
        """Return if data is in LinkedList or not O(N)"""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Delete data from LinkedList O(N)"""
        current = self.head
        while current is not None:
            if current.data == data:
                current.data = None
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.length -= 1
                break
            else:
                current = current.next

    def append(self, data):
        """Append data to end of LinkedList O(1)"""
        node = Node(data)
        if self.tail is not None:
            self.insert_after_node(self.tail, node)
        else:
            self.add(node)

    def insert(self, data, index):
        current = self.head
        position = 0
        if index > self.size() - 1:
            raise IndexError('Index not in range of LinkedList')
        while current is not None:
            if position == index:
                self.insert_before_node(current, Node(data))
                break
            else:
                current = current.next
                position += 1

    def insert_after(self, node_data, data):
        """Insert data after given node in LinkedList O(N)"""
        current = self.head
        while current is not None:
            if current.data == node_data:
                self.insert_after_node(current, Node(data))
                break
            else:
                current = current.next

    def insert_before(self, node_data, data):
        """Insert data after given node in LinkedList O(N)"""
        current = self.head
        while current is not None:
            if current.data == node_data:
                self.insert_before_node(current, Node(data))
                break
            else:
                current = current.next

    def insert_before_node(self, node, new_node):
        if node.previous is not None:
            node.previous.next = new_node
            new_node.previous = node.previous
            new_node.next = node
            node.previous = new_node
        else:
            self.head = new_node
            new_node.next = node
            node.previous = new_node
        self.length += 1

    def insert_after_node(self, node, new_node):
        if node.next is not None:
            node.next.previous = new_node
            new_node.next = node.next
            new_node.previous = node
            node.next = new_node
        else:
            node.next = new_node
            new_node.previous = node
        self.length += 1

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current)
            current = current.next
        return '<->'.join(node.data for node in nodes)

    def report(self):
        current = self.head
        while current is not None:
            print(f'''--------------------------------------
Current Node: {current}
Previous Node: {current.previous}
Next Node: {current.next}
''')
            current = current.next


if __name__ == '__main__':
    pass
