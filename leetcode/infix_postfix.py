
def infix_to_postfix(expression):
    """
    Function turns infix expression into postfix expression by iterating over the expression
    and moving operators after their operands whilst maintaining order of precedence.

    :param expression: Space delimited parenthetical expression containing of letters and the operators * / + -
    :return: PostFix version of expression
    """

    '''
    1)Fix a priority level for each operator. For example, from high to low:
        3.    - (unary negation)
        2.    * /
        1.    + - (subtraction)
    2) If the token is an operand, do not stack it. Pass it to the output. 
    3) If token is an operator or parenthesis:
        3.1) if it is '(', push
        3.2) if it is ')', pop until '('
        3.3) push the incoming operator if its priority > top operator; otherwise pop.
        *The popped stack elements will be written to output. 
    4) Pop the remainder of the stack and write to the output (except left parenthesis)
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



'''
Scan the formula:
1) When the token is an operand, push into stack; 
2) When an operator is encountered: 
    2.1) If the operator is binary, then pop the stack twice 
    2.2) If the operator is unary (e.g. unary minus), pop once 
3) Perform the indicated operation on two poped numbers, and push the result back
4) The final result is the stack top.
'''
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


def postfix_to_infix(expression):
    stack = []
    prev_op = None
    operators = {'(', ')', '*', '/', '+', '-'}


    for exp in expression:
        if not exp in operators:
            stack.append(exp)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + exp + b )



if __name__ == '__main__':
    print(infix_to_postfix('(A+B)*C'))
    print(infix_to_postfix('A*B+C*D'))
    print(infix_to_postfix('(A+B)*C-(D-E)*(F+G)'))
    print(eval_postfix('78+32+/'))
