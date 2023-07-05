# binary tree and binary search tree
finding the maximum value in a binary tree

![lab16](https://github.com/ahmaderaqi/ahmaderaqi-data-structures-and-algorithms/assets/118004544/19264960-f04d-4e0b-bc5a-5226e1f067a2)


## Approach & Efficiency
finding the maximum value in a binary tree

# algorithm
1. Start with the root node of the binary tree.
2. If the root node is empty (None), raise a ValueError indicating that the tree is empty.
3. Initialize a variable `max_value` to negative infinity (`float('-inf')`).
4. Recursively traverse the tree using a depth-first search approach:
   - If the current node is empty (None), return negative infinity (`float('-inf')`).
   - Compare the value of the current node with `max_value`.
   - Update `max_value` if the value of the current node is greater.
   - Recursively find the maximum value in the left subtree and store it in a variable `left_max`.
   - Recursively find the maximum value in the right subtree and store it in a variable `right_max`.
   - Compare `left_max` and `right_max` with `max_value` and update `max_value` if necessary.
   - Return `max_value` as the maximum value found in the current subtree.
5. After the recursive traversal, `max_value` will contain the maximum value in the entire tree.
6. Return `max_value` as the maximum value stored in the tree.



# big O
time complexity of O(n)
space complexity of O(1)

## Solution

|Code challenge15  |    [code1](../binary_search_tree_file.py)

