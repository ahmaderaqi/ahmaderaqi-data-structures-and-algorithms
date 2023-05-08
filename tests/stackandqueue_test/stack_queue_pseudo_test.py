from code_challenges.stack_and_queue.stack_queue_pseudo_file import stack_queue_pseudo




def test_enqueue_empty_queue1():
    queue = stack_queue_pseudo()
    queue.enqueue(10)
    assert queue.peek() == 10

def test_enqueue_nonempty_queue1():
    queue = stack_queue_pseudo()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.peek() == 1

def test_enqueue_and_dequeue_queue1():
    queue = stack_queue_pseudo()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    dequeued = queue.dequeue1()
    assert dequeued == 1
    assert queue.peek() == 2


