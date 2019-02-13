
def infix_to_postfix(expression):
    """
    Function turns infix expression into postfix expression by iterating over the expression
    and moving operators after their operands whilst maintaining order of precedence.

    :param expression: Space delimited parenthetical expression containing of letters and the operators * / + -
    :return: PostFix version of expression
    """

    '''
    Basic Algorithm:
    1. Tokenize the string
    2. Create list to capture the result and stack to maintain parsed operators
    3. Iterate over tokens
    4. If token is letter or number, append to result list
    5. If token is (, push it onto the stack
    6. If token is ), keep appending to the result list the top of the stack until just after you reach its matching (
    7. Else token must be a operator, keep appending to the result list the top of the stack while the precdence of the
     of the operator is less than that of the token operator or the stack is empty
    8. Pust that token onto the top of the stack
    9. After going thru all the tokens, append the rest of the stack to the end of the result list
    '''
    operators = {'(', ')', '*', '/', '+', '-'}
    op_stack = []
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2}
    result = ''
    for exp in expression:
        if exp not in operators:
            result += exp
        elif exp == '(':
            op_stack.append(exp)
        elif exp == ')':
            while op_stack and op_stack[-1] != '(':
                result += op_stack.pop()
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and precedence[exp] <= precedence[op_stack[-1]]:
                result += op_stack.pop()
            op_stack.append(exp)
    while op_stack:
        result += op_stack.pop()
    return result


def eval_postfix(postfix_expression):

    operators = {'(', ')', '*', '/', '+', '-'}

    stack = []

    for exp in postfix_expression:
        if exp not in operators :
            stack.append(float(exp))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append({'+':a+b, '-':b-a, '*':a*b, '/':b/a}[exp])

    return stack[-1]




if __name__ == '__main__':
    print(infix_to_postfix('(A+B)*C'))
    print(infix_to_postfix('A*B+C*D'))
    print(infix_to_postfix('(A+B)*C-(D-E)*(F+G)'))
    print(eval_postfix('78+32+/'))
