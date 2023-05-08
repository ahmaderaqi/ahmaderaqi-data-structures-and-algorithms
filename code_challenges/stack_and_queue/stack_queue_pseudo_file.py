from code_challenges.stack_and_queue.stack_file import Stack
class stack_queue_pseudo:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                item = self.in_stack.pop()
                self.out_stack.push(item)
        if self.out_stack.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.out_stack.pop()