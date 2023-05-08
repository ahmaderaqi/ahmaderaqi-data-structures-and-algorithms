# stack_queue_pseudo
using two stack to implement a queue
## Whiteboard Process

![images](https://user-images.githubusercontent.com/118004544/236326279-537f9c2a-b190-4aa7-b850-86c707ea07a1.png)


![lab11](https://user-images.githubusercontent.com/118004544/236876268-83e05126-b65b-4127-86ba-20882ef92604.jpg)


## Approach & Efficiency
adding and deleting elements from and to a stack and queue

## Algorithm of stack:
1. Create two stacks, `in_stack` and `out_stack`.
2. To enqueue an item, push it onto the `in_stack`.
3. To dequeue an item:
   1. If the `out_stack` is not empty, pop the top item from the `out_stack` and return it.
   2. If the `out_stack` is empty:
      1. Pop all items from the `in_stack` and push them onto the `out_stack` in reverse order.
      2. If the `in_stack` is also empty, raise an `IndexError` indicating that the queue is empty.
      3. Pop the top item from the `out_stack` and return it.
4. Repeat step 3 until the item is dequeued.

### summary of my algorithm
These steps outline the basic logic of the algorithm. When we enqueue an item, we simply push it onto the `in_stack`. When we dequeue an item, we first check if the `out_stack` is not empty. If it is not empty, we can simply pop the top item from the `out_stack` and return it. If it is empty, we need to pop all items from the `in_stack` and push them onto the `out_stack` in reverse order. We then pop the top item from the `out_stack` and return it. If both stacks are empty, we raise an `IndexError` indicating that the queue is empty.

## Big O
The time complexity of enqueueing an item in a queue implemented using two stacks is O(1)
The time complexity of dequeuing an item from a queue implemented using two stacks is O(n) 
The space complexity of a queue implemented using two stacks is O(n).
## Solution
|Code challenge10  |    [code1](./main.py)
|Code challenge10  |    [code1](./stack.py)
|Code challenge10  |    [code1](./queue.py)

