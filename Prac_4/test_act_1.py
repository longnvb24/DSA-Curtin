from act_1 import DSALinkedList

print("--- Test DSALinkedList ---")

# 1. Initial state
ll = DSALinkedList()
assert ll.isEmpty() == True, "a new list must be empty"
assert ll.head is None, "a new list must have head as None"
assert ll.tail is None, "a new list must have tail as None"
print("PASS: initial state")

# 2. insertFirst into an empty list
ll.insertFirst(2.0)
assert ll.isEmpty() == False, "the list is not empty any more"
assert ll.head.data == 2.0, "the new node becomes the head"
assert ll.tail.data == 2.0, "the only node is both the head and the tail"
assert ll.head.prev is None, "head.prev must be None"
assert ll.tail.next is None, "tail.next must be None"
print("PASS: insertFirst into an empty list")

# 3. insertFirst + insertLast, list becomes [1.0, 2.0, 3.0]
ll.insertFirst(1.0)
ll.insertLast(3.0)
assert ll.head.data == 1.0, "walk forwards: first value"
assert ll.head.next.data == 2.0, "walk forwards: second value"
assert ll.head.next.next.data == 3.0, "walk forwards: third value"
assert ll.head.next.next.next is None, "the last node must not point further"
assert ll.tail.data == 3.0, "walk backwards: first value"
assert ll.tail.prev.data == 2.0, "walk backwards: second value"
assert ll.tail.prev.prev.data == 1.0, "walk backwards: third value"
assert ll.tail.prev.prev.prev is None, "the first node must not point back"
print("PASS: insertFirst + insertLast")

# 4. insertBefore, list becomes [1.0, 2.0, 2.5, 3.0]
ll.insertBefore(3.0, 2.5)
assert ll.head.next.next.data == 2.5, "the new node sits before 3.0"
assert ll.tail.prev.data == 2.5, "the prev link into the new node"
assert ll.tail.data == 3.0, "the tail does not change"
print("PASS: insertBefore in the middle")

# 5. insertBefore the head, list becomes [0.5, 1.0, 2.0, 2.5, 3.0]
ll.insertBefore(1.0, 0.5)
assert ll.head.data == 0.5, "the head must be updated"
assert ll.head.prev is None, "the new head must not point back"
assert ll.head.next.data == 1.0, "the old head is now second"
print("PASS: insertBefore the head")

# 6. peek and find return a value
assert ll.peekFirst() == 0.5, "peekFirst returns the first value"
assert ll.peekLast() == 3.0, "peekLast returns the last value"
assert ll.head.data == 0.5, "peek must not remove anything"
assert ll.find(2.0) == True, "find a value that is in the list"
assert ll.find(9.0) == False, "find a value that is not in the list"
print("PASS: peekFirst + peekLast + find")

# 7. removeFirst and removeLast, list becomes [1.0, 2.0, 2.5]
assert ll.removeFirst() == 0.5, "removeFirst returns the value, not the node"
assert ll.head.data == 1.0, "the second node becomes the head"
assert ll.head.prev is None, "the new head must not point back"
assert ll.removeLast() == 3.0, "removeLast returns the value"
assert ll.tail.data == 2.5, "the second last node becomes the tail"
assert ll.tail.next is None, "the new tail must not point further"
print("PASS: removeFirst + removeLast")

# 8. removeValue in the middle, list becomes [1.0, 2.5]
assert ll.removeValue(2.0) == 2.0, "removeValue returns the value"
assert ll.head.next.data == 2.5, "the gap must be closed going forwards"
assert ll.tail.prev.data == 1.0, "the gap must be closed going backwards"
print("PASS: removeValue in the middle")

# 9. A one-item list
ll.removeFirst()
assert ll.head.data == 2.5, "one item left"
assert ll.head is ll.tail, "the only node must be both the head and the tail"
ll.removeLast()
assert ll.isEmpty() == True, "removing the only item empties the list"
assert ll.tail is None, "the tail must be reset, not left on a deleted node"
print("PASS: one-item list")

# 10. The list must still work after being emptied
ll.insertLast(7.0)
assert ll.head.data == 7.0, "the head is set again"
assert ll.tail.data == 7.0, "the tail is set again"
ll.removeFirst()
assert ll.isEmpty() == True, "back to empty"
print("PASS: reuse after empty")

# 11. Error cases on an empty list
try:
    ll.removeFirst()
    assert False, "removeFirst on an empty list must raise ValueError"
except ValueError:
    print("PASS: removeFirst raises ValueError")

try:
    ll.removeLast()
    assert False, "removeLast on an empty list must raise ValueError"
except ValueError:
    print("PASS: removeLast raises ValueError")

try:
    ll.peekFirst()
    assert False, "peekFirst on an empty list must raise ValueError"
except ValueError:
    print("PASS: peekFirst raises ValueError")

try:
    ll.peekLast()
    assert False, "peekLast on an empty list must raise ValueError"
except ValueError:
    print("PASS: peekLast raises ValueError")

try:
    ll.removeValue(9.0)
    assert False, "removeValue with a missing value must raise ValueError"
except ValueError:
    print("PASS: removeValue raises ValueError")

print("\nAll tests passed.")