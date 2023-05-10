from code_challenges.stack_and_queue.stack_queue_animal_shelter import AnimalShelter
from code_challenges.stack_and_queue.stack_queue_animal_shelter import Animal





def test_enqueue_empty_queue1():
    animal=Animal("cat","cat1")
    queue = AnimalShelter(animal)
    
    assert queue.peek() == "cat1"

def test_enqueue_nonempty_queue1():
    animal1=Animal("cat","cat1")
    animal2=Animal("cat","cat2")
    animal3=Animal("cat","dog1")
    animal4=Animal("cat","dog2")
    queue = AnimalShelter(animal1)
    queue.enqueue(animal1)
    queue.enqueue(animal2)
    queue.enqueue(animal3)
    queue.enqueue(animal4)

    assert queue.peek() == "cat1"

def test_enqueue_and_dequeue_queue1():
    animal1=Animal("cat","cat1")
    animal2=Animal("cat","cat2")
    animal3=Animal("cat","dog1")
    animal4=Animal("cat","dog2")
    queue = AnimalShelter(animal1)
    queue.enqueue(animal1)
    queue.enqueue(animal2)
    queue.enqueue(animal3)
    queue.enqueue(animal4)
    dequeued = queue.dequeue1()
    assert dequeued == 1
    assert queue.peek() == 2


