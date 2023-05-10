from queue_file import Queue
from stack_file import Stack
from stack_queue_pseudo_file import stack_queue_pseudo
from stack_queue_animal_shelter import Animal
from stack_queue_animal_shelter import AnimalShelter

# queue1 = Queue()

# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)

# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())
# print(queue1.dequeue())

# stack1 = stack_queue_pseudo()

# stack1.enqueue(1)
# stack1.enqueue(2)
# stack1.enqueue(3)

# print(stack1.dequeue())

animal1=Animal("Cat","roro")
animal2=Animal("Dog","fefe")
animal3=Animal("Cat","gege")
animal4=Animal("Dog","lll")


shelt=AnimalShelter()
shelt.enqueue(animal1)
shelt.enqueue(animal2)
shelt.enqueue(animal3)
shelt.enqueue(animal4)
print(shelt.dequeue())
print(shelt.dequeue())
print(shelt.dequeue())
print(shelt.dequeue())
print(shelt.dequeue())


# print("size",stack1.get_size())
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())
# print("size",stack1.get_size())