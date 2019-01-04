class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        """Return if LinkedList is empty or not O(1)"""
        return not self.head

    def add(self, data):
        """Add node to beginning of LinkedList O(1)"""
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    def size(self):
        """Return size of LinkedList O(N)"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def ssize(self):
        """Return size of LinkedList O(1)"""
        return self.length

    def search(self, data):
        """Return index of data if data exists in LinkedList, else throws ValueError O(N)"""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            else:
                current = current.next
                position += 1
        raise ValueError(f'\'{data}\' not found in LinkedList')

    def contains(self, data):
        """Return if data is in LinkedList or not O(N)"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Delete data from LinkedList O(N)"""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                current.data = None
                if not previous:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.length -= 1
                break
            else:
                previous = current
                current = current.next

    def append(self, data):
        """Append data to end of LinkedList O(N)"""
        current = self.head
        node = Node(data)
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.length += 1

    def insert(self, data, index):
        """Insert data at index in LinkedList O(N)"""
        node = Node(data)
        current = self.head
        previous = None
        position = 0
        if index > self.size() - 1:
            raise IndexError('Index not in range of LinkedList')
        while current:
            if position == index:
                if not previous:
                    node.next = self.head
                    self.head = node
                else:
                    node.next = current
                    previous.next = node
                self.length += 1
                break
            else:
                previous = current
                current = current.next
                position += 1

    def insert_after(self, node, data):
        """Insert data after given node in LinkedList O(N)"""
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == node:
                new_node.next = current.next
                current.next = new_node
                self.length += 1
                break
            else:
                current = current.next

    def insert_before(self, node, data):
        """Insert data after given node in LinkedList O(N)"""
        new_node = Node(data)
        current = self.head
        previous = None
        while current:
            if current.data == node:
                if not previous:
                    new_node.next = current
                    self.head = new_node
                else:
                    new_node.next = current
                    previous.next = new_node
                self.length += 1
                break
            else:
                previous = current
                current = current.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return '->'.join(node.data for node in nodes)

    def report(self):
        current = self.head
        while current:
            print(f'''--------------------------------------
Current Node: {current}
Next Node: {current.next}
''')
            current = current.next


if __name__ == '__main__':
    pass
