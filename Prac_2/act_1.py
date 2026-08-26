"""
Compute Factorial and Fibonacci by both Iterative and Recursive
"""

def factWithIterative(n):
    if type(n) != int or n < 0:
        raise ValueError("Input should be a positive integer")
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factWithRecursive(n):
    if type(n) != int or n < 0:
        raise ValueError("Input should be a positive integer")
    result = 1
    if n == 0:
        result = 1
    else:
        result = n * factWithRecursive(n-1)
    return result

def fibonacciIterative(n):
    if type(n) != int or n < 0:
        raise ValueError("Input should be a positive integer")
    currVal = 1
    lastVal = 0
    fibVal = 0

    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        for i in range(2,n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def fibonacciRecursive(n):
    if type(n) != int or n < 0:
        raise ValueError("Input should be a positive integer")
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    return result

def getNumber(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
            if number < 0:
                raise ValueError
        except ValueError:
            number = None
            print("Wrong input, please enter a positive integer.")
    return number


def main():
    choice = ""
    while choice != "0":
        print("\n1. Factorial (Iterative)")
        print("2. Factorial (Recursive)")
        print("3. Fibonacci (Iterative)")
        print("4. Fibonacci (Recursive)")
        print("0. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            n = getNumber("Enter a number: ")
            print(f"Factorial of {n} with Iterative: {factWithIterative(n)}")
        elif choice == "2":
            n = getNumber("Enter a number: ")
            print(f"Factorial of {n} with Recursive: {factWithRecursive(n)}")
        elif choice == "3":
            n = getNumber("Enter a number: ")
            print(f"The {n}th Fibonacci number with Iterative is: {fibonacciIterative(n)}")
        elif choice == "4":
            n = getNumber("Enter a number: ")
            print(f"The {n}th Fibonacci number with Recursive is: {fibonacciRecursive(n)}")
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Wrong choice, please pick 0-4.")


if __name__ == "__main__":
    main()