from node import Node
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    
    def __str__(self):
        return self.name
    

class  AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,animal):
        node=Node(animal)
        type=node.value.species
        name=node.value.name
        # print(node.value)
        # print(type)

        #if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        

        
    def dequeue(self, pref):
         #if the queue is empty
        if self.front == None:
            return "This queue is empty"
        if self.front == self.rear:
            self.rear = None
            #self.front = None
            if self.front.value.species==pref:
                temp = self.front
                self.front = self.front.next
                temp.next = None
                return temp.value
            else:
                return f"there's no {pref} in our queue"
        # print(self.front.value.name)
        temp1 =self.front
        temp2=self.front.next
        # print(temp1.value.name)
        # print(not temp2==None)
        # first node(front)
        if self.front.value.species==pref:
            self.front=self.front.next
            return temp1.value.name
        while temp2 is not None:
            # print("hello")
            if temp2.value.species==pref:
                temp1.next=temp2.next
                temp2.next=None
                # print("hi")
                return temp2.value.name
            temp2=temp2.next
            
        return f"there's no {pref} in our queue"

         
    # def __str__(self):
    #     cat_queue_str = ', '.join([str(animal) for animal in self.container])
    #     dog_queue_str = ', '.join([str(animal) for animal in self.container1])
    #     return f"Cat Queue: {cat_queue_str}\nDog Queue: {dog_queue_str}"



        
          
    

shelter = AnimalShelter()

cat1 = Animal("Whiskers_cat", "Cat")
(shelter.enqueue(cat1))
(shelter.enqueue(Animal('dog1','Dog')))

(shelter.enqueue(Animal('Fluffy_cat','Cat')))
(shelter.enqueue(Animal('dog2','Dog')))
print(shelter.dequeue('Dog'))
# print(shelter.dequeue('Cat'))
# print(shelter.dequeue('Cat'))

# # # # print(shelter.dequeue('Dog'))
# (shelter.enqueue(Animal('Rex_dog', 'Dog')))
# (shelter.enqueue(Animal('Rex2_cat', 'Dog')))

# print(shelter.dequeue('Dog'))
# print(shelter.dequeue('Dog'))
# print(shelter.dequeue('Dog'))
# shelter.enqueue(Animal('Rex', 'Dog'))

# print(shelter)




# shelter.enqueue(Animal('dog', 'Rex'))
# shelter.enqueue(Animal('cat', 'Garfield'))
# shelter.enqueue(Animal('dog', 'Fido'))

# print(shelter.dequeue('dog'))

# print(shelter.dequeue('snake'))

        

