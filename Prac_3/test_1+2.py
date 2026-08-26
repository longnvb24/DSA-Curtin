from act_1 import DSAStack, DSAQueue
from act_2 import ShufflingQueue, CircularQueue


def test_stack(cls):
    s = cls(3)

    # Initialize
    assert s.isEmpty() == True
    assert s.isFull() == False

    # Push and peek
    s.push('a')
    s.push('b')
    assert s.peek() == 'b'
    assert s.count == 2

    # Pop
    s.push('c')
    assert s.isFull() == True
    assert s.pop() == 'c'
    assert s.pop() == 'b'
    assert s.pop() == 'a'
    assert s.isEmpty() == True

    # Pop with empty array
    try:
        s.pop()
        assert False, "Pop with empty array"
    except AssertionError:
        raise
    except Exception:
        pass

    # Push with full array
    s.push(1); s.push(2); s.push(3)
    try:
        s.push(4)
        assert False, "Push with full array"
    except AssertionError:
        raise
    except Exception:
        pass
    assert s.count == 3

    print(f"{cls.__name__}: PASS")


def test_queue(cls):
    """Test for Queue, Suffling, Circular."""
    q = cls(3)

    # Initialize
    assert q.isEmpty() == True
    assert q.isFull() == False

    # Enqueue and peek
    q.enqueue('a')
    q.enqueue('b')
    assert q.peek() == 'a'
    assert q.count == 2

    # Dequeue
    q.enqueue('c')
    assert q.isFull() == True
    assert q.dequeue() == 'a'
    assert q.dequeue() == 'b'
    assert q.dequeue() == 'c'
    assert q.isEmpty() == True

    # Dequeue with empty array
    try:
        q.dequeue()
        assert False, "Dequeue with empty array"
    except AssertionError:
        raise
    except Exception:
        pass

    # Enqueue with full array
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    try:
        q.enqueue(4)
        assert False, "Enqueue with full array"
    except AssertionError:
        raise
    except Exception:
        pass
    assert q.count == 3

    print(f"{cls.__name__}: PASS")


def test_wraparound():
    """Test index for circular queue."""
    q = CircularQueue(3)
    q.enqueue('A'); q.enqueue('B'); q.enqueue('C')   # initial full array: front = 0, rear = 2
    assert q.dequeue() == 'A'                        # front turns to 1, rear = 2
    q.enqueue('D')                                   # rear turns to 0 (wrap-around)

    assert q.peek() == 'B'          # peek at front = 1
    assert q.dequeue() == 'B'
    assert q.dequeue() == 'C'
    assert q.dequeue() == 'D'
    assert q.isEmpty() == True

    print("CircularQueue wrap-around: PASS")


test_stack(DSAStack)

for cls in (DSAQueue, ShufflingQueue, CircularQueue):
    test_queue(cls)

test_wraparound()

print("\nAll tests passed.")