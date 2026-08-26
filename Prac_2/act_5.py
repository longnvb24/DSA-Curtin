def moveDisk(n, src, dest, level):
    """Print the move of a disk"""
    indent = " " * (8 * (level - 1))          # 8 spaces for each level of recursion
    print(f"{indent}Recursion Level={level}")
    print(f"{indent}Moving Disk {n} from Source {src} to Destination {dest}")
    print(f"{indent}n={n}, src={src}, dest={dest}")
    print()


def towers(n, src, dest, aux=None, level=1):
    """
    Solve the Towers of Hanoi problem.
    """
    if aux is None:
        aux = 6 - src - dest

    # base case
    if n == 1:
        moveDisk(1, src, dest, level)
        return                                 # stops the recursive branch here

    towers(n - 1, src, aux, dest, level + 1)   # move n-1 disks from src to aux
    moveDisk(n, src, dest, level)              # move the largest disk from src to dest
    towers(n - 1, aux, dest, src, level + 1)   # move n-1 disks from aux to dest


def main():
    n = 0
    valid = False

    while not valid:
        try:
            n = int(input("Enter the number of disks: "))
            if n <= 0:
                print("Error: The number of disks must be a positive integer (n >= 1).")
            else:
                valid = True
        except ValueError:
            print("Error: Please enter an integer (not text).")

    print(f"towers({n}, 1, 3)")
    towers(n, 1, 3)
    print(f"... # There are {2 ** n - 1} moves for this problem.")


if __name__ == "__main__":
    main()