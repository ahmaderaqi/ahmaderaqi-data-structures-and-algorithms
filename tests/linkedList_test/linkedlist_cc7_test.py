# import pytest
# from code_challenges.linked_list.linked_list import Linked_list

# # testing code challenge 7
# def test_cc1_empty():
#     lists=Linked_list()
#     expected = "empty list"
#     actual = lists.kth_value(5)
#     assert expected == actual

# def test_cc1_one():
#     lists=Linked_list()
#     lists.insert('A')
#     expected = 'A'
#     actual = lists.kth_value(0)
#     assert expected == actual

# def test_cc1_negative():
#     lists=Linked_list()
#     lists.insert('A')
#     expected = "negative index is denied"
#     actual = lists.kth_value(-8)
#     assert expected == actual

# def test_cc1_outofrange():
#     lists=Linked_list()
#     lists.insert('A')
#     expected = "out of range, you have 1 node and you can insert between 0 and 0 only"
#     actual = lists.kth_value(2)
#     assert expected == actual