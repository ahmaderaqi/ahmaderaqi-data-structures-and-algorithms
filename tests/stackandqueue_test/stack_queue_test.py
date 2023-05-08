from code_challenges.stack_and_queue.stack_file import Stack
from code_challenges.stack_and_queue.queue_file import Queue


def test_push_empty_stack():
    stack = stack()
    stack.push(10)
    assert stack.peek() == 10

def test_push_nonempty_stack():
    stack = stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.peek() == 4

def test_push_and_pop_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    popped = stack.pop()
    assert popped == 3
    assert stack.peek() == 2

def test_enqueue_empty_queue():
    queue = Queue()
    queue.enqueue(10)
    assert queue.peek() == 10

def test_enqueue_nonempty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.peek() == 1

def test_enqueue_and_dequeue_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    dequeued = queue.dequeue()
    assert dequeued == 1
    assert queue.peek() == 2


