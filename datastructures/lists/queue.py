class QueueSimple:
    def __init__(self):
        self.length = 0
        self.arr = []

    def is_empty(self):
        return not self.length

    def enqueue(self, data):
        self.arr.append(data)

    def dequeue(self):
        return self.arr.pop(0)

    def __repr__(self):
        return str(self.arr)


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

    def __repr__(self):
        return f"{self.inbox} | {self.outbox}"


def test_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert not q.is_empty()
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()
