from stack import Stack


def symbol_balance_checker(symbol_str):
    stack = Stack()
    balanced = True

    symbols = {')' : '(', ']' : '[', '}' : '{'}

    for symbol in symbol_str:
        if symbol in symbols.values():
            stack.push(symbol)
        else: # symbol is closer
            if stack.isEmpty(): # we don't have any openers
                balanced = False
                brea
            else:
                if stack.pop() != symbols[symbol]:
                    balanced = False
                    break
    return balanced and stack.isEmpty() # make sure all ( have been removed from the stack and balance flag still set


if __name__ == '__main__':
    print(symbol_balance_checker('()((()))'))
    print(symbol_balance_checker('()((())'))
    print(symbol_balance_checker('()(((())'))
    print(symbol_balance_checker('{{([][])}()}'))
    print(symbol_balance_checker('[{()]'))
