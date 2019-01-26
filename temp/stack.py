class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push('a')
    stack.push('b')
    print(stack.peek())
    stack.push('c')
    print(stack.isEmpty())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())