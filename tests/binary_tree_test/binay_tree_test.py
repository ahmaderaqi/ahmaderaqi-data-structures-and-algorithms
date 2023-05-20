from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import post_order
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import pre_order
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import in_order

from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Tree
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Add
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Contains

from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Node
import pytest


@pytest.fixture
def bst_tree():
    root = Node(50)
    (root, 30)
    Add(root, 20)
    Add(root, 40)
    Add(root, 70)
    Add(root, 60)
    Add(root, 80)
    return root

def test_contains_value_existing_value():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)
    
    assert Contains(root, 40) == True
    assert Contains(root, 60) == True
    assert Contains(root, 50) == True

def test_contains_value_nonexistent_value():
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    assert Contains(root, 10) == False
    assert Contains(root, 90) == False
    assert Contains(root, 45) == False

def test_contains_value_empty_tree():
    root = None

    assert Contains(root, 10) == False
    assert Contains(root, 20) == False
    assert Contains(root, 30) == False