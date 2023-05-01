from linked_list import Linked_list
from linked_list import linked_list_zip


from node import Node

if __name__ == "__main__":

    linked_list1 = Linked_list()
    linked_list2 = Linked_list()

    # linked_list1.insert(1)
    # linked_list1.insert(3)
    # linked_list1.insert(5)
    # linked_list1.insert(7)

    linked_list2.insert(2)
    linked_list2.insert(4)
    linked_list2.insert(6)
    linked_list2.insert(8)
    
    # linked_list1.insert_before("O","L")
    # linked_list1.insert("g")

    # print(linked_list1)

    # indexs=linked_list1.kth_value(-2)
    # indexs=linked_list1.middle_node()


    print(linked_list1)
    print(linked_list2)

    ziper=linked_list_zip(linked_list1,linked_list2)
    print(ziper)

    # # Create the first linked list: 1 -> 2 -> 3
    # l1 = Node(1)
    # l1.next = Node(2)
    # l1.next.next = Node(3)

    # # Create the second linked list: 4 -> 5 -> 6
    # l2 = Node(4)
    # l2.next = Node(5)
    # l2.next.next = Node(6)
    # zipped = zip_lists(linked_list1, l2)
    # curr = zipped
    # while curr:
    #     print(curr.value, end=' ')
    #     curr = curr.next