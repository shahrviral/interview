from stack import Stack


def paren_balance_checker(paren_str):
    stack = Stack()
    balanced = True

    for p in paren_str:
        if p == '(':
            stack.push(p)
        else: # paren is }
            if stack.isEmpty(): # we don't have a matching (
                balanced = False
                break
            else:
                stack.pop()
    return balanced and stack.isEmpty() # make sure all ( have been removed from the stack and balance flag still set


if __name__ == '__main__':
    print(paren_balance_checker('()((()))'))
    print(paren_balance_checker('()((())'))
    print(paren_balance_checker('()(((())'))
