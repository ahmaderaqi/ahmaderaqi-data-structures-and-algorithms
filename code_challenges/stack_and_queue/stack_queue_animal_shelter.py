class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    
    def __str__(self):
        return self.name
    

class  AnimalShelter():
    def __init__(self):
        
        
       
        self.cat_queue=[]
        self.dog_queue=[]
        self.container=[]
        self.container1=[]

    def enqueue(self,animal):
      if animal.species == "Cat":
            self.cat_queue.append(animal.name)
           
            return self.cat_queue

        
      elif animal.species == "Dog":
            self.dog_queue.append(animal.name)
            return self.dog_queue

        
    def dequeue(self, pref):
         if pref=="Cat":
            #  if len(self.cat_queue)==0:
            #     return "I Have no cats"
            
             while len(self.cat_queue)!=0:
                self.container.append(self.cat_queue.pop())
           
             return self.container.pop()
    
         elif pref=="Dog":
            #  if len(self.dog_queue)==0:
            #     return "I Have no Dogs"
            
             while len(self.dog_queue)!=0:
                self.container1.append(self.dog_queue.pop())
            #  self.cat_queue= self.container1
            
             return self.container1.pop()
         
    # def __str__(self):
    #     cat_queue_str = ', '.join([str(animal) for animal in self.container])
    #     dog_queue_str = ', '.join([str(animal) for animal in self.container1])
    #     return f"Cat Queue: {cat_queue_str}\nDog Queue: {dog_queue_str}"



        
          
    

shelter = AnimalShelter()

cat1 = Animal("Whiskers_cat", "Cat")
(shelter.enqueue(cat1))
(shelter.enqueue(Animal('Fluffy_cat','Cat')))
(shelter.enqueue(Animal('yuio_cat','Cat')))
print(shelter.dequeue('Cat'))
print(shelter.dequeue('Cat'))
print(shelter.dequeue('Cat'))

# # # print(shelter.dequeue('Dog'))
(shelter.enqueue(Animal('Rex_dog', 'Dog')))
(shelter.enqueue(Animal('Rex2_cat', 'Dog')))

print(shelter.dequeue('Dog'))
print(shelter.dequeue('Dog'))
# print(shelter.dequeue('Dog'))
# shelter.enqueue(Animal('Rex', 'Dog'))

# print(shelter)




# shelter.enqueue(Animal('dog', 'Rex'))
# shelter.enqueue(Animal('cat', 'Garfield'))
# shelter.enqueue(Animal('dog', 'Fido'))

# print(shelter.dequeue('dog'))

# print(shelter.dequeue('snake'))

        

