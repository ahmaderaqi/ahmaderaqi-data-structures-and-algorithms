from node import Node

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return ("stack is empty")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("this stack is empty")
        
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def pop_specific_value(self,val):
        if self.top is None:
            return None
        value=self.top.value
        if value==val:
            self.size -= 1
            self.top=self.top.next
            return val
        temp1=self.top
        temp2=self.top.next
        while temp2 is not None:
            if temp2.value==val:
                self.size -= 1
                temp1.next=temp2.next
                temp2.next=None
                return temp2.value
            temp1=temp1.next
            temp2=temp2.next
        return False
        