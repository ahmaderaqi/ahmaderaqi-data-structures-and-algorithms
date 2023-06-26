# binary tree and binary search tree
printing binary tree pre,in and post order.
and inserting a value in binary search tree and check if it contains a specific value## Whiteboard Process

![lab15](https://github.com/ahmaderaqi/ahmaderaqi-data-structures-and-algorithms/assets/118004544/8cc09a6b-85fb-4c7d-a990-68950630103a)


## Approach & Efficiency
printing binary tree pre,in and post order.
and inserting a value in binary search tree and check if it contains a specific value# algorithm and big O

# for binary tree
## pre-order
1. If the current node is null, return.
2. Print the value of the current node.
3. Recursively call the preorder function on the left subtree.
4. Recursively call the preorder function on the right subtree.
### Big O
time O(n)
space O(n)


## post-order
1. If the current node is null, return.
2. Recursively call the postorder function on the left subtree.
3. Recursively call the postorder function on the right subtree.
4. Print the value of the current node.ee.
### Big O
time O(n)
space O(n)

## in-order
1. If the current node is null, return.
2. Recursively call the inorder function on the left subtree.
3. Print the value of the current node.
4.Recursively call the inorder function on the right subtree.
### Big O
time O(n)
space O(n)


## add
1. If the tree is empty (root is None), create a new node with the given value and set it as the root.
2. If the value of the node to be inserted is less than the current node's value, go to the left subtree.
3. If the left child of the current node is None, create a new node with the given value and set it as the left child of the current node.
4. If the left child is not None, recursively repeat step 2 with the left child as the new current node.
5. If the value of the node to be inserted is greater than the current node's value, go to the right subtree.
6. If the right child of the current node is None, create a new node with the given value and set it as the right child of the current node.
7. If the right child is not None, recursively repeat step 3 with the right child as the new current node.
### Big O
time O(n)
space O(n)




## Solution

|Code challenge15  |    [code1](./binary_search_tree_file.py)

