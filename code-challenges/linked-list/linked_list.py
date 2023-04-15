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