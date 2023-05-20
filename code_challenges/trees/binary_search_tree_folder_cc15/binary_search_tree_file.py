class Node:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


tree1 = Tree()

node1 = Node("10")
tree1.root = node1

node2 = Node(8)
tree1.root.left = node2

node3 = Node(20)
tree1.root.right = node3

node4 = Node(6)
tree1.root.left.left = node4

node5 = Node(30)
tree1.root.left.right = node5

node6 = Node(19)
tree1.root.right.left = node6

def pre_order(root):
    if root is not None:
        print(root.value)
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)

def in_order(root):
    if root.left is not None:
        in_order(root.left)
    if root is not None:
        print(root.value)
    if root.right is not None:
        in_order(root.right)
    
def post_order(root):
    if root.left is not None:
        in_order(root.left)
    if root.right is not None:
        in_order(root.right)
    if root is not None:
        print(root.value)

def Add(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            Add(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            Add(root.right, value)

def Contains(root, value):
    if root is None:
        return False
    
    if value == root.value:
        return True
    elif value < root.value:
        return Contains(root.left, value)
    else:
        return Contains(root.right, value)