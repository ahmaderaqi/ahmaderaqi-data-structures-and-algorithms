class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_intersection(root1, root2):
    values1 = set()
    result = set()

    
    def traverse_tree(node, value):
        if node:
            value.add(node.val)
            traverse_tree(node.left, value)
            traverse_tree(node.right, value)

    
    traverse_tree(root1, values1)

    
    def find_common(node, values):
        if node:
            if node.val in values1:
                result.add(node.val)
            find_common(node.left, values)
            find_common(node.right, values)

    
    find_common(root2, result)

    return result
