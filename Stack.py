class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def __repr__(self):
        return str(self.items)


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())
    stack.push('v')
    stack.push('b')
    stack.push('d')
    print(stack)
    print(stack.is_empty())
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack.size())

