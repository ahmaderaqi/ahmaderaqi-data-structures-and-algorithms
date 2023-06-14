import pytest
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import BinaryTree
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Node


def test_find_maximum_value():
    # Create the binary tree
    bt = BinaryTree()

    # Empty tree case
    with pytest.raises(ValueError):
        bt.find_maximum_value()

    # Tree with single node
    bt.root = Node(5)
    assert bt.find_maximum_value() == 5

    # Tree with multiple nodes
    bt.root = Node(1)
    bt.root.left = Node(5)
    bt.root.right = Node(3)
    bt.root.left.left = Node(9)
    bt.root.left.right = Node(2)
    bt.root.right.left = Node(7)
    bt.root.right.right = Node(4)

    assert bt.find_maximum_value() == 9

    # Tree with negative values
    bt.root = Node(-5)
    bt.root.left = Node(-3)
    bt.root.right = Node(-7)
    bt.root.left.left = Node(-1)
    bt.root.left.right = Node(-9)
    bt.root.right.left = Node(-2)
    bt.root.right.right = Node(-4)

    assert bt.find_maximum_value() == -1


if __name__ == "__main__":
    pytest.main()
