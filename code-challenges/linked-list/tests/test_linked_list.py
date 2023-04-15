import pytest
from linked_list import Linked_list
# Test empty linked list
def test_empty_ll():
    ll = Linked_list()
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual

# # Test appending 3 nodes
def test_append_three_nodes(ll):
    expected = "3 --> Ahmad --> 10 -->  None"
    actual = str(ll)
    assert expected == actual

@pytest.fixture
def ll():
    ll = Linked_list()
    ll.insert(10)
    ll.insert("Ahmad")
    ll.insert(3)
    return ll