from act_1 import DSAStack, DSAQueue


def parseTerms(equation):
    terms = DSAQueue(len(equation) + 1)
    number = ""

    for ch in equation:
        if ch == '+' or ch == '-' or ch == '*' or ch == '/' \
                or ch == '(' or ch == ')' or ch == ' ':
            if number != "":                       # the number ends here
                terms.enqueue(number)
                number = ""
            if ch != ' ':
                terms.enqueue(ch)
        else:
            number = number + ch                   # still inside a number

    if number != "":                               # the equation may end on one
        terms.enqueue(number)

    return terms


def precedenceOf(theOp):
    """+ and - give 1, * and / give 2."""
    if theOp == '+' or theOp == '-':
        return 1
    elif theOp == '*' or theOp == '/':
        return 2
    else:
        raise Exception(f"Unknown operator: {theOp}")


def executeOperation(op, op1, op2):
    """Do the binary operation op on op1 and op2."""
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    else:
        raise Exception(f"Unknown operator: {op}")


def parseInfixToPostfix(equation):
    """Infix -> postfix queue."""
    terms = parseTerms(equation)
    opStack = DSAStack(terms.count + 1)
    postfixQueue = DSAQueue(terms.count + 1)

    while not terms.isEmpty():
        term = terms.dequeue()

        if term == '(':
            opStack.push(term)                     # '(' goes straight on

        elif term == ')':
            while opStack.peek() != '(':           # pop the sub-equation
                postfixQueue.enqueue(opStack.pop())
            opStack.pop()                          # drop the '('

        elif term == '+' or term == '-' or term == '*' or term == '/':
            while (not opStack.isEmpty() and opStack.peek() != '('
                   and precedenceOf(opStack.peek()) >= precedenceOf(term)):
                postfixQueue.enqueue(opStack.pop())
            opStack.push(term)                     # always push the new operator

        else:
            postfixQueue.enqueue(float(term))      # the term is an operand

    while not opStack.isEmpty():                   # pop what is left
        op = opStack.pop()
        if op == '(':
            raise Exception("A '(' has no matching ')'")
        postfixQueue.enqueue(op)

    return postfixQueue


def evaluatePostfix(postfixQueue):
    """Evaluate the postfix queue. This time the stack holds the operands."""
    operandStack = DSAStack(postfixQueue.count + 1)

    while not postfixQueue.isEmpty():
        term = postfixQueue.dequeue()

        if term == '+' or term == '-' or term == '*' or term == '/':
            op2 = operandStack.pop()               # popped first  -> right
            op1 = operandStack.pop()               # popped second -> left
            operandStack.push(executeOperation(term, op1, op2))
        else:
            operandStack.push(term)

    return operandStack.pop()


def solve(equation):
    """Parse to postfix, then evaluate."""
    return evaluatePostfix(parseInfixToPostfix(equation))


if __name__ == "__main__":
    print("Spaces are optional, e.g.  (10.3*(14+3.2))/(5+2-4*3)")

    equation = input("\nEquation (or 'q' to quit): ")
    while equation != "q":
        try:
            postfixQueue = parseInfixToPostfix(equation)

            postfix = ""                           # check the parsing first
            for i in range(postfixQueue.count):
                postfix = postfix + str(postfixQueue.data[i]) + " "

            print(f"  Postfix: {postfix}")
            print(f"  Result : {evaluatePostfix(postfixQueue)}")
        except Exception as e:
            print(f"  Error: {e}")
        equation = input("\nEquation (or 'q' to quit): ")
