# stack and queue
A stack is a data structure that follows the Last-In-First-Out (LIFO) principle.
A queue, on the other hand, follows the First-In-First-Out (FIFO) principle
## Whiteboard Process
![asset_0000000000000245_1613806948_example_stack(1)](https://user-images.githubusercontent.com/118004544/236326097-74154e89-e7cc-412a-a8f8-9d89a4ed1201.png)

![images](https://user-images.githubusercontent.com/118004544/236326279-537f9c2a-b190-4aa7-b850-86c707ea07a1.png)


![lab10](https://user-images.githubusercontent.com/118004544/236330163-3735cc26-94ee-46c5-9bde-b61ce090c21c.jpg)


## Approach & Efficiency
adding and deleting elements from and to a stack and queue

## Algorithm of stack:
 ### The algorithm for adding an element to a stack (also known as "pushing" onto the stack) is:

1. Check if the stack is full. If the stack is full, return an error as the stack cannot accommodate any more elements.

2. If the stack is not full, increment the top pointer to indicate that the top of the stack has moved up.

3. Add the new element to the position pointed to by the top pointer.

4. Return success.

### The algorithm for adding an element to a queue (also known as "enqueueing" onto the queue) is:

1 Check if the queue is full. If the queue is full, return an error as the queue cannot accommodate any more elements.

2 If the queue is not full, increment the rear pointer to indicate that the rear of the queue has moved back.

3 Add the new element to the position pointed to by the rear pointer.

4 Return success.

Big O
time complexity is O(1)
space complexity is O(1)

## Solution
|Code challenge10  |    [code1](./main.py)
|Code challenge10  |    [code1](./stack.py)
|Code challenge10  |    [code1](./queue.py)

