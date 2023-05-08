from queue import Queue
from code_challenges.stack_and_queue.stack_file import Stack
from stack_queue_pseudo_file import stack_queue_pseudo
# queue1 = Queue()

# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)

# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())

stack1 = stack_queue_pseudo()

stack1.enqueue(1)
stack1.enqueue(2)
stack1.enqueue(3)

print(stack1.dequeue())



# print("size",stack1.get_size())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print("size",stack1.get_size())