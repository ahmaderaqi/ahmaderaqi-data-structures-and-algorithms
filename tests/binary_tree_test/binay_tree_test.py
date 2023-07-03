from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import BinarySearchTree
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import BinaryTree
from code_challenges.trees.binary_search_tree_folder_cc15.binary_search_tree_file import Node
import pytest






def test_binary_search_tree():
    bst = BinarySearchTree()

    # Add nodes
    bst.add(5)
    bst.add(2)
    bst.add(7)
    bst.add(1)
    bst.add(4)

    # Check if values are present in the tree
    assert bst.contains(4) is True
    assert bst.contains(6) is False
    assert bst.contains(2) is True
    assert bst.contains(10) is False

def test_binary_tree_traversals():
    bt = BinaryTree()

    # Create the binary tree
    bt.root = Node(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)

    # Perform pre-order traversal
    pre_order_result = bt.pre_order_traversal()
    assert pre_order_result == [1, 2, 4, 5, 3]

    # Perform in-order traversal
    in_order_result = bt.in_order_traversal()
    assert in_order_result == [4, 2, 5, 1, 3]

    # Perform post-order traversal
    post_order_result = bt.post_order_traversal()
    assert post_order_result == [4, 5, 2, 3, 1]
if __name__ == "__main__":
    pytest.main()
