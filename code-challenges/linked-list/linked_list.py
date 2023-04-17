from node import Node

class Linked_list:
    def __init__(self) -> None:
        self.head=None

    def insert(self,value):

        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            self.head=node
            self.head.next=current
    
    def __str__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def include(self,key):


        temp = self.head

        # 1. Empty linked list
        if (temp is None):
            return False
        
        # 2. If the target is the first node
        if (temp is not None):
            if(temp.value == key):
                return True
            
        # search for the key and delete the target node
        while(temp is not None):
            if temp.value == key:
                return True
            prev = temp
            temp = temp.next

        # 3. The key does not Exists
        if(temp is None):
            return False

        # unlinke the target node from the linkedlist
        prev.next = temp.next
        temp = None
        return True
    
    def append(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def insert_before(self,value,new_value):
        node= Node(new_value)
        if self.head is None:
            head = node
        elif self.head.next is None:
            node.next=head
            head=node
        else:
            current=self.head
            while current.value!=value:
                prev=current
                current=current.next
                if current is None:
                    break
            prev.next=node
            node.next=current
    
    def insert_after(self,value,new_value):
        node= Node(new_value)
        if self.head is None:
            head = node
        elif self.head.next is None:
           self.head.next=node
        
        else:
            current=self.head
            front=self.head.next
            while current.value!=value:
                current=current.next
                front=front.next
                if current.next is None:
                    break
                
            current.next=node
            node.next=front
        
