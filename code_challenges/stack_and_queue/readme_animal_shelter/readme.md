# stack_queue_animal_shelter
implementing a queue that has an animal's shelter
## Whiteboard Process

![lab12](https://github.com/ahmaderaqi/ahmaderaqi-data-structures-and-algorithms/assets/118004544/6a53d81e-de9b-41bb-9f68-97c3a238f099)


## Approach & Efficiency
implementing a queue that has an animal's shelter

## Algorithm of stack:
1. Create two queues one for cats and the other is for dogs
2. if the user enqueues a cat, then it will be added to the cat's queue.
3. if the user enqueues a dog, then it will be added to the dog's queue.
4. To enqueue an item:
   1. if it's empty, it will be added and the front and the rear will point on it
   2. if it's not, the element will be added at the end of the queue 
5. To dequeue an item:
   1. if it's empty, it will return that the queue is empty
   2. if it's not, we will reverse the array and then remove the last element(first element of the queue)
    




## Big O
The time complexity of enqueueing an item in a queue implemented using two stacks is O(1)
The time complexity of dequeuing an item from a queue implemented using two stacks is O(n) 
The space complexity of a queue implemented using two stacks is O(n).
## Solution

|Code challenge12  |    [code1](../stack_queue_animal_shelter.py)

