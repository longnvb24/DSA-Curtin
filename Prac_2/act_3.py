# https://www.inchcalculator.com/base-converter/
def decimal_to_base(n, base):
    """
    Recursive convertion a Decimal (Base 10) to any Base(2-16)
    """
    if type(base) != int or not (2 <= base <= 16):
        raise ValueError("Base should be an integer in interval 2-16")
    elif type(n) != int:
        raise ValueError("Input should be an integer")

    digits = "0123456789ABCDEF"  # characters stand for numbers

    if n == 0:
        return "0"

    def helper(n):
        if n == 0:
            return ""
        return helper(n // base) + digits[n % base]

    if n < 0:
        return "-" + helper(-n)
    return helper(n)

def getInteger(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Wrong input, please enter an integer.")
    return number


def getBase(prompt):
    base = None
    while base is None:
        try:
            base = int(input(prompt))
            if not (2 <= base <= 16):
                raise ValueError
        except ValueError:
            base = None
            print("Wrong input, base must be an integer between 2 and 16.")
    return base


def main():
    num = getInteger("Enter a decimal number: ")
    base = getBase("Enter the base (2-16): ")
    result = decimal_to_base(num, base)
    print(f"{num} in base {base} is: {result}")

if __name__ == '__main__':
    main()
