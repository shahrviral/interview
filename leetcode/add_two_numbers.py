class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    res = current = ListNode(0)

    p = l1
    q = l2

    carry = 0

    while p or q:
        i = j = 0
        if p:
            i = p.val
            p = p.next
        if q:
            j = q.val
            q = q.next
        carry, val = divmod(i + j + carry, 10)
        current.next = ListNode(val)
        current = current.next
    return res.next


if __name__ == '__main__':
    l = ListNode(2)
    l.next = ListNode(4)
    l.next.next = ListNode(3)

    m = ListNode(5)
    m.next = ListNode(6)
    m.next.next = ListNode(4)

    res = add_two_numbers(l, m)

    a = []
    while res:
        a.append(res.val)
        res = res.next
    print(a)
