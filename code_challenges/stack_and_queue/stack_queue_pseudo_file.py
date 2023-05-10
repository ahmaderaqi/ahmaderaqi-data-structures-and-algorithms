from code_challenges.stack_and_queue.stack_file import Stack
class stack_queue_pseudo:
    """
    in this class we are using two stacks to implement a queue
    """
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        """this method adding an item to the first stack"""
        self.in_stack.push(item)

    def dequeue(self):
        """this method pop from the first stack and push it to the second stack"""
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                item = self.in_stack.pop()
                self.out_stack.push(item)
        if self.out_stack.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.out_stack.pop()