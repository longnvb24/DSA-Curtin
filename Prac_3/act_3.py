from act_1 import DSAStack, DSAQueue

def precedenceOf(theOp):
    """Return precedence of operator: + - returns 1, * / returns 2."""
    if theOp == '+' or theOp == '-':
        return 1
    elif theOp == '*' or theOp == '/':
        return 2
    else:
        raise Exception(f"Unknown operator: {theOp}")


def isNumber(token):
    """Return True if the token is a valid number (int or float)."""
    try:
        float(token)
        return True
    except ValueError:
        return False


def parseInfixToPostfix(equation):
    """Convert infix expression to postfix queue.
    Stack holds operators, queue holds the postfix result."""
    if equation is None or equation.strip() == "":
        raise ValueError("Empty expression. Please enter something.")

    opStack = DSAStack(100)
    postfixQueue = DSAQueue(100)

    for token in equation.split():
        c = token

        if c == '(':
            # (: Push onto stack
            opStack.push(c)

        elif c == ')':
            # ): Pop from stack until '(' is encountered
            while not opStack.isEmpty() and opStack.peek() != '(':
                postfixQueue.enqueue(opStack.pop())
            if opStack.isEmpty():
                raise ValueError("Unbalanced parentheses: extra ')'")
            opStack.pop()                  # remove '(' from stack, do not enqueue

        elif c == '+' or c == '-' or c == '*' or c == '/':
            # Pop operators from stack with precedence >= current operator
            while (not opStack.isEmpty()
                   and opStack.peek() != '('
                   and precedenceOf(opStack.peek()) >= precedenceOf(c)):
                postfixQueue.enqueue(opStack.pop())
            opStack.push(c)

        elif isNumber(c):
            # Number
            postfixQueue.enqueue(float(c))

        else:
            # Not a number, not an operator, not a bracket -> invalid input
            raise ValueError(
                f"Invalid token '{token}'. Only numbers, + - * / and ( ) are allowed, "
                f"separated by spaces."
            )

    # No more tokens: pop remaining operators from stack to queue
    while not opStack.isEmpty():
        op = opStack.pop()
        if op == '(':
            raise ValueError("Unbalanced parentheses: missing ')'")
        postfixQueue.enqueue(op)

    return postfixQueue


def executeOperation(op, op1, op2):
    """Execute the operation op on operands op1 and op2."""
    if op == '+':
        result = op1 + op2
    elif op == '-':
        result = op1 - op2
    elif op == '*':
        result = op1 * op2
    elif op == '/':
        if op2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = op1 / op2
    else:
        raise Exception(f"Unknown operator: {op}")
    return result


def evaluatePostfix(postfixQueue):
    """Evaluate the postfix queue. This stack holds numbers."""
    operandStack = DSAStack(100)

    while not postfixQueue.isEmpty():
        token = postfixQueue.dequeue()

        if isinstance(token, str):
            # Operator: pop two operands, compute, and push result back
            if operandStack.count < 2:
                raise ValueError(f"Invalid expression: operator '{token}' is missing operand(s)")
            op2 = operandStack.pop()       # pop first -> right operand
            op1 = operandStack.pop()       # pop second -> left operand
            operandStack.push(executeOperation(token, op1, op2))
        else:
            # Number: push onto stack
            operandStack.push(token)

    if operandStack.isEmpty():
        raise ValueError("Invalid expression: no result")
    result = operandStack.pop()
    if not operandStack.isEmpty():
        raise Exception("Invalid expression: extra operand(s) left")
    return result


def solve(equation):
    """Solve the infix expression and return the result as a float."""
    postfixQueue = parseInfixToPostfix(equation)
    return evaluatePostfix(postfixQueue)


def showQueue(q):
    """Display the contents of the queue on the screen (used for debugging the parsing steps)."""
    text = ""
    for i in range(q.count):
        text = text + str(q.data[i]) + " "
    return text.strip()


def readEquation(prompt="Enter an expression (or 'q' to quit): "):
    """Keep asking until the user types a valid expression.
    Returns the equation string, or None if the user wants to quit."""
    while True:
        equation = input(prompt).strip()

        if equation.lower() in ("q", "quit", "exit"):
            return None

        try:
            # Try parsing + evaluating. If it works, the input is valid.
            solve(equation)
            return equation
        except ZeroDivisionError as e:
            print(f"  Error: {e}. Please try again.\n")
        except ValueError as e:
            print(f"  Invalid input: {e}\n")
        except Exception as e:
            print(f"  Invalid expression: {e}\n")


if __name__ == "__main__":
    equations = [
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "5 - 3",
        "10 - 2 - 3",
        "20 / 4 / 5",
        "( 1 + 2 ) * ( 3 + 4 )",
        "3.5 * 2",
    ]

    print("Demo cases:")
    for eq in equations:
        postfix = showQueue(parseInfixToPostfix(eq))
        print(f"{eq:24} -> {postfix:26} = {solve(eq)}")

    print("\nOr try by yourself:")
    print("Separate every token with a space, e.g.  ( 3 + 4 ) * 2")
    while True:
        equation = readEquation()
        if equation is None:
            print("Bye!")
            break
        postfix = showQueue(parseInfixToPostfix(equation))
        print(f"  Postfix: {postfix}")
        print(f"  Result : {solve(equation)}\n")
