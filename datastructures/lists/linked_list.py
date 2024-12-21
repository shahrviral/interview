import pytest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        """Return if LinkedList is empty or not O(1)"""
        return not self.head

    def add(self, data):
        """Add node to beginning of LinkedList O(1)"""
        node = Node(data)
        node.next = self.head
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
        raise ValueError(f"'{data}' not found in LinkedList")

    def contains(self, data):
        """Return if data is in LinkedList or not O(N)"""
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def delete(self, data):
        """Delete data from LinkedList O(N)"""
        current = self.head
        previous = None
        while current:
            if current.data == data:
                current.data = None
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.length -= 1
                break
            else:
                previous = current
                current = current.next

    def append(self, data):
        """Append data to end of LinkedList O(N)"""
        current = self.head
        new_node = Node(data)
        if not current:
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def insert(self, data, index):
        """Insert data at index in LinkedList O(N)"""
        previous = None
        current = self.head
        new_node = Node(data)
        position = 0
        if index > self.size() - 1:
            raise IndexError("Index not in range of LinkedList")
        while current:
            if position == index:
                if previous:
                    new_node.next = current
                    previous.next = new_node
                else:
                    new_node.next = current
                    self.head = new_node
                self.length += 1
                break
            else:
                previous = current
                current = current.next
                position += 1

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current)
            current = current.next
        return "->".join(node.data for node in nodes)


def test_linked_list():
    ll = LinkedList()
    ll.add("A")
    assert ll.size() == 1
    assert ll.ssize() == 1
    assert ll.head.data == "A"
    ll.append("B")
    assert ll.search("B") == 1
    assert ll.ssize() == 2
    ll.append("C")
    ll.insert("X", 0)
    assert ll.ssize() == 4
    ll.insert("Y", 3)
    with pytest.raises(IndexError):
        ll.insert("Q", 9)
    assert ll.search("X") == 0
    assert ll.search("B") == 2
    assert ll.search("C") == 4
    assert ll.search("A") == 1
    with pytest.raises(ValueError):
        ll.search("W")
    assert ll.contains("X")
    assert ll.contains("B")
    assert ll.contains("C")
    assert not ll.contains("W")
    ll.delete("X")
    assert ll.ssize() == 4
    assert ll.head.data == "A"
    ll.delete("C")
    assert ll.search("Y") == 2
    ll.delete("B")
    assert ll.search("Y") == 1
