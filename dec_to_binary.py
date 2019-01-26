from stack import Stack

def dec_to_binary(num):

    stack = Stack()

    while num > 0:
        stack.push(num % 2) ## push the remainder of the num divided by 2 onto stack
                            # it will be the value in binary 0 or 1
        num = num // 2 # set number to be the floor division by 2

    res = ''
    while not stack.isEmpty():
        res += str(stack.pop())
    return res

if __name__ == '__main__':
    print(dec_to_binary(8))
    print(dec_to_binary(56432))