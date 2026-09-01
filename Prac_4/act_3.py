from act_1 import DSALinkedList

def getMenuChoice():
    choice = -1
    valid = False
    while not valid:
        try:
            choice = int(input("Enter choice: "))
            if 0 <= choice <= 5:
                valid = True
            else:
                print("Choice must be between 0 and 5.")
        except ValueError:
            print("Please enter a number.")
    return choice

def displayList(myList):
    if myList.isEmpty():
        print("The list is empty.")
    else:
        current = myList.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    myList = DSALinkedList()
    choice = -1
    while choice != 0:
        print("\nDSALinkedList Menu")
        print("1. Insert First   2. Insert Last")
        print("3. Remove First   4. Remove Last")
        print("5. Display list   0. Quit")
        choice = getMenuChoice()

        if choice == 1:
            value = input("Value to insert at front: ")
            myList.insertFirst(value)
            print(f"Inserted '{value}' at the front.")

        elif choice == 2:
            value = input("Value to insert at end: ")
            myList.insertLast(value)
            print(f"Inserted '{value}' at the end.")

        elif choice == 3:
            try:
                removed = myList.removeFirst()
                print(f"Removed '{removed}' from the front.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 4:
            try:
                removed = myList.removeLast()
                print(f"Removed '{removed}' from the end.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 5:
            print("List contents:")
            displayList(myList)

        elif choice == 0:
            print("Goodbye.")

if __name__ == "__main__":
    main()