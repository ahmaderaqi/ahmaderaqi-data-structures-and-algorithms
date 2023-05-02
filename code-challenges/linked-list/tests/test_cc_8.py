from linked_list import Linked_list

def test_cc1_1():
    linked_list1 = Linked_list()
    linked_list2 = Linked_list()

    linked_list1.insert(1)
    linked_list1.insert(3)
    linked_list1.insert(5)
    linked_list1.insert(7)

    linked_list2.insert(2)
    linked_list2.insert(4)
    linked_list2.insert(6)
    linked_list2.insert(8)
    lists=Linked_list.linked_list_zip(linked_list1,linked_list2)
    expected = "7 --> 8 --> 5 --> 6 --> 3 --> 4 --> 1 --> 2 -->  None"
    actual = lists
    assert expected == actual

def test_cc1_2():
    linked_list1 = Linked_list()
    linked_list2 = Linked_list()

    linked_list1.insert(1)
    linked_list1.insert(3)
    linked_list1.insert(5)
    linked_list1.insert(7)

    
    lists=Linked_list.linked_list_zip(linked_list1,linked_list2)
    expected = "7 --> 5 --> 3 --> 1 -->  None"
    actual = lists
    assert expected == actual

def test_cc1_3():
    linked_list1 = Linked_list()
    linked_list2 = Linked_list()

    

    
    lists=Linked_list.linked_list_zip(linked_list2,linked_list1)
    expected = "Empty LinkeList"
    actual = lists
    assert expected == actual