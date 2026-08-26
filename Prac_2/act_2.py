def gcd(a,b):
    """
    Recursive function to find the greatest common divisor (GCD) of two non-negative integers a
    and b using the Euclidean algorithm.
    """
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

def getNumber(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Wrong input, please enter an integer.")
    return number

def main():
    a = getNumber("Enter the first number: ")
    b = getNumber("Enter the second number: ")
    print(gcd(a, b))

if __name__ == '__main__':
    main()