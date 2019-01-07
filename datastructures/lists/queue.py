class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def is_empty(self):
        return not self.inbox and not self.outbox

    def enqueue(self, data):
        self.inbox.append(data)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()


if __name__ == '__main__':
    pass
