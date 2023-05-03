from node import Node

class Linked_list:
    """
        in this class, we will add most methods that's related to the linked list such as insert, delete, search 
        """
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
        """
        in this method, you should insert a value and it will be added at the begining of the linked list
        """

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
        """
        in this method, you should insert a value and it will be added at the end of the linked list
        """
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = node
    
    def insert_before(self,value,new_value):
        """
        in this method, you should insert a value that's included in the linked list and another value to be added
        before the spcific value and you will get the new linked list with the new value
        """
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
        """
        in this method, you should insert a value that's included in the linked list and another value to be added
        after the spcific value and you will get the new linked list with the new value
        """
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
        
    def kth_value(self,k):
        """
        in this method, you should insert the index and you will get the value of this index
        
        """
        counter=0
        temp=self.head
        # calculate the length of the linked list
        while temp!=None:
            counter+=1
            temp=temp.next
        ##############

        # if self.head.next==None and k>0:
        #     return "out of range, you have only one node and you can insert 0 only"
        if k<0:
            return "negative index is denied"
        elif self.head==None:
            return "empty list"
        elif self.head.next==None and k==0:
            return self.head.value
        elif k>=counter:
            return f"out of range, you have {counter} node and you can insert between 0 and {counter-1} only"
        else:
            newval=self.head
            for i in range(counter-k-1):
                newval=newval.next
            return newval.valu
        
    def  middle_node(self):
        """
        in this method, we will get the middle value of the linked list
        """
        counter=0
        temp=self.head
        if self.head==None:
            return "empty list"
        elif self.head.next==None:
            return self.head.value
        # calculate the length of the linked list
        while temp!=None:
            counter+=1
            temp=temp.next
        ##############
        newval=self.head
        if counter%2==1:
            cc=int(counter/2)
            for i in range(cc):
                newval=newval.next
            return newval.value
        else:
            cc=int(counter/2)
            for i in range(cc):
                newval=newval.next
            return newval.value
    
    def linked_list_zip(ll1, ll2):
        if not ll1:
            return ll2
        if not ll2:
            return ll1

        temp1 = ll1.head
        temp2 = ll2.head

        while temp1 and temp2:
            next1 = temp1.next
            next2 = temp2.next

            temp1.next = temp2
            temp2.next = next1

            temp1 = next1
            temp2 = next2

        if temp2:
            temp1.next = temp2

        return str(ll1) 
    

       




# def linked_list_zip(ll1,ll2):
#         if not ll1:
#             return ll2
#         if not ll2:
#             return ll1
#         temp1=ll1.head
#         temp11=ll1.head

#         temp2=ll2.head
#         temp22=ll2.head

#         while temp1 and temp2:
#             temp1.next=temp2
#             temp2.next=temp11.next

#             temp1=temp11.next
#             temp11=temp1

#             temp2=temp22.next
#             temp22=temp2





# def zip_lists(l1, l2):
#     if not l1:
#         return l2
#     if not l2:
#         return l1

#     # create a new linked list by alternating between nodes from l1 and l2
#     head = l1
#     tail = head.next
#     curr = l2
#     while tail and curr:
#         head.next = curr
#         curr = curr.next
#         head.next.next = tail
#         head = tail
#         tail = head.next

#     # append remaining nodes from l1 or l2, if any
#     if not tail:
#         head.next = curr

#     return l1