import pytest
from code_challenges.hash_table.TreeIntersection.tree_intersection import tree_intersection
from code_challenges.hash_table.TreeIntersection.tree_intersection import Tree


def test_tree_intersection():
    root1 = Tree(1)
    root1.left = Tree(2)
    root1.right = Tree(3)
    root1.left.left = Tree(4)
    root1.left.right = Tree(5)

    root2 = Tree(2)
    root2.left = Tree(4)
    root2.right = Tree(6)
    root2.left.left = Tree(8)

    intersection = tree_intersection(root1, root2)

    assert intersection == {2, 4}

    empty_intersection = tree_intersection(None, None)
    assert empty_intersection == set()

    no_common_values_root1 = Tree(1)
    no_common_values_root1.left = Tree(2)
    no_common_values_root1.right = Tree(3)

    no_common_values_root2 = Tree(4)
    no_common_values_root2.left = Tree(5)
    no_common_values_root2.right = Tree(6)

    no_common_intersection = tree_intersection(no_common_values_root1, no_common_values_root2)
    assert no_common_intersection == set()

    single_node_intersection = tree_intersection(Tree(1), Tree(1))
    assert single_node_intersection == {1}

    print("All tests pass")


if __name__ == "__main__":
    pytest.main()
