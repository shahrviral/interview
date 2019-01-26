from stack import Stack

def base_converter(num, base):

    digits = '0123456789ABCDEF'

    stack = Stack()

    while num > 0:
        stack.push(num % base) ## push the remainder of the num divided by 2 onto stack
                            # it will be the value in binary 0 or 1
        num = num // base # set number to be the floor division by 2

    res = ''
    while not stack.isEmpty():
        res += str(digits[stack.pop()])
    return res

if __name__ == '__main__':
    print(base_converter(25, 2))
    print(base_converter(25, 16))
    print(base_converter(250, 16))