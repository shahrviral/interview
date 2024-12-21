class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def __repr__(self):
        return str(self.items)


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.size() == 2
    s.pop()
    assert not s.is_empty()
    s.pop()
    assert s.is_empty()
