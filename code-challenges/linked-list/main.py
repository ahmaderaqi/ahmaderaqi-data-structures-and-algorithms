from linked_list import Linked_list

if __name__ == "__main__":

    linked_list1 = Linked_list()

    linked_list1.insert("A")
    linked_list1.insert("B")
    linked_list1.insert("C")
    linked_list1.insert("D")
    linked_list1.insert_before("O","L")
    linked_list1.insert("g")

    # print(linked_list1)

    indexs=linked_list1.kth_value(-2)
    indexs=linked_list1.middle_node()


    print(linked_list1)
    print(linked_list1.kth_value(-2))